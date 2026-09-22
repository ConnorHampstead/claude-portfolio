#!/usr/bin/env python3
"""
desk.py - paper trading desk harness for Alpaca.

Takes a JSON block of proposed trades (emitted by Claude alongside its morning
brief), enforces the risk rules, sizes positions from the stop, submits bracket
orders to an Alpaca PAPER account, and logs everything for later scoring.

The same JSON block may carry a "manage" array for positions that are already
open - new stops, new targets, or a close. Those are applied to the live exit
orders and run even on a "no_trade" day, since standing down applies to new
entries only.

Commands:
    check     Validate a plays file and print the sized plan. Sends nothing.
    submit    Same as check, then actually submit. Requires --confirm.
    status    Account state: equity, exposure, positions, loss-limit headroom.
    reconcile Pull fills from Alpaca and update the journal with outcomes.
    score     Performance and calibration report from the journal.
    shadow    Replay passed ideas against the tape and score them.
    stale     List (and optionally cancel) unfilled entry orders.
    flatten   Close all open positions and cancel all orders. Requires --confirm.

Every command is read-only unless you pass --confirm.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dependency. Run:  pip install requests")

# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------

PAPER_BASE = "https://paper-api.alpaca.markets"
DATA_BASE = "https://data.alpaca.markets"

HERE = Path(__file__).resolve().parent
JOURNAL = HERE / "journal.csv"
CONFIG = HERE / "config.json"

DEFAULT_CONFIG = {
    "risk_per_trade_pct": 1.0,      # max % of equity risked entry-to-stop, per trade
    "min_risk_pct": 0.1,            # smallest per-play risk_pct accepted
    "max_open_risk_pct": 4.0,       # entry-to-stop risk across the whole book
    "max_positions": 8,             # open positions + resting entries
    "max_gross_exposure_pct": 150,  # longs + |shorts|, % of equity
    "max_net_exposure_pct": 100,    # |longs - shorts|, % of equity
    "max_position_pct": 50,         # max notional in any single name, % of equity
    "daily_loss_limit_pct": 3.0,    # flatten + stand down past this
    "min_conviction": 1,            # reject plays below this
    "time_in_force": "gtc",         # gtc or day
    "data_feed": "iex",             # iex (free) or sip (paid)
    "allow_shorts": True,
    # Market data table in `prep`: watchlist groups, then the day's movers
    # filtered to the tradable universe.
    "watchlist": {},
    "movers_show": 8,               # per side, after filtering
    "min_price": 5.0,
    "min_avg_volume": 1_000_000,
    # Shadow book replay windows, in trading sessions from the session date.
    "shadow_entry_sessions": 5,     # an entry not reached by then never filled
    "shadow_exit_sessions": 10,     # neither level by then: expired
}

# stop / target are the live levels and move with `manage`. The *_initial
# columns are the levels the play was submitted with and never change: R is
# measured against the initial stop, and p_target_first was a statement about
# the initial target and stop.
JOURNAL_FIELDS = [
    "play_id", "logged_at", "session_date", "ticker", "direction",
    "entry_type", "entry_planned", "stop", "target",
    "stop_initial", "target_initial", "qty",
    "risk_usd", "risk_pct_equity", "conviction", "p_target_first",
    "time_horizon", "catalyst", "thesis", "invalidation", "bear_case",
    "order_id", "status", "entry_fill", "exit_fill", "exit_reason",
    "pnl_usd", "r_multiple", "hit_target_first", "closed_at",
    "thesis_verdict", "notes", "session", "model",
]

# Ideas the brief looked at with real levels and did not take, plus plays the
# caps dropped. No orders: each is replayed against intraday bars afterwards,
# so standing aside is scored the same way a trade is.
SHADOW = HERE / "shadow.csv"
SHADOW_FIELDS = [
    "shadow_id", "logged_at", "session_date", "session", "model", "source",
    "ticker", "direction", "entry_type", "entry", "stop", "target",
    "p_target_first", "reason", "status", "entry_fill", "filled_at",
    "exit_price", "exit_at", "outcome", "r_multiple", "hit_target_first",
    "evaluated_through",
]


def load_config() -> dict:
    cfg = dict(DEFAULT_CONFIG)
    if CONFIG.exists():
        try:
            cfg.update(json.loads(CONFIG.read_text()))
        except json.JSONDecodeError as e:
            sys.exit(f"config.json is not valid JSON: {e}")
    return cfg


def creds() -> dict:
    key = os.environ.get("ALPACA_API_KEY_ID")
    secret = os.environ.get("ALPACA_API_SECRET_KEY")
    if not key or not secret:
        sys.exit(
            "Missing credentials. Set them first:\n"
            "  export ALPACA_API_KEY_ID=...\n"
            "  export ALPACA_API_SECRET_KEY=...\n"
            "Generate paper keys at https://app.alpaca.markets under Paper Trading."
        )
    return {
        "APCA-API-KEY-ID": key,
        "APCA-API-SECRET-KEY": secret,
        "Content-Type": "application/json",
    }


# --------------------------------------------------------------------------
# API helpers
# --------------------------------------------------------------------------

def api(method: str, path: str, base: str = PAPER_BASE, **kwargs):
    url = f"{base}{path}"
    try:
        r = requests.request(method, url, headers=creds(), timeout=30, **kwargs)
    except requests.RequestException as e:
        sys.exit(f"Network error calling {path}: {e}")
    if r.status_code >= 400:
        detail = r.text[:400]
        if r.status_code in (401, 403):
            detail += "\n(Check your keys are PAPER keys, not live keys.)"
        raise RuntimeError(f"{method} {path} -> {r.status_code}: {detail}")
    return r.json() if r.text else {}


def get_account() -> dict:
    return api("GET", "/v2/account")


def get_positions() -> list:
    return api("GET", "/v2/positions")


def get_clock() -> dict:
    return api("GET", "/v2/clock")


def get_asset(symbol: str) -> dict:
    return api("GET", f"/v2/assets/{symbol.upper()}")


def get_snapshots(symbols: list[str], feed: str) -> dict:
    if not symbols:
        return {}
    params = {"symbols": ",".join(s.upper() for s in symbols), "feed": feed}
    try:
        data = api("GET", "/v2beta1/stocks/snapshots", base=DATA_BASE, params=params)
    except RuntimeError:
        # Older/alternate endpoint shape
        data = api("GET", "/v2/stocks/snapshots", base=DATA_BASE, params=params)
    return data.get("snapshots", data)


def get_open_orders(symbol: str | None = None) -> list:
    params = {"status": "open", "nested": "true", "limit": 500}
    if symbol:
        params["symbols"] = symbol.upper()
    return api("GET", "/v2/orders", params=params)


def exit_legs(symbol: str, pos_side: str, orders: list | None = None) -> dict:
    """Find the live take-profit / stop-loss orders protecting an open position.

    After a bracket entry fills, its two children stay open as an OCO pair. They
    come back either nested under the parent or as top-level orders, so walk both.
    The exit legs are the ones facing opposite the position.
    """
    symbol = symbol.upper()
    exit_side = "sell" if pos_side == "long" else "buy"
    found = {"take_profit": None, "stop_loss": None}

    def walk(nodes):
        for o in nodes or []:
            walk(o.get("legs"))
            if (o.get("symbol") or "").upper() != symbol:
                continue
            if o.get("side") != exit_side:
                continue
            otype = o.get("type")
            if otype == "limit" and not found["take_profit"]:
                found["take_profit"] = o
            elif otype in ("stop", "stop_limit", "trailing_stop") and not found["stop_loss"]:
                found["stop_loss"] = o

    walk(orders if orders is not None else get_open_orders(symbol))
    return found


def pending_entry(symbol: str, orders: list | None = None) -> dict | None:
    """The resting, still-unfilled entry order for a symbol, if there is one.

    A bracket entry that has not filled yet holds its stop and target as child
    legs, so its levels are amendable even though no position exists. Without
    this, a brief that moves a stop the morning after submitting the entry is
    rejected as "no position to manage" and the stop silently never moves.
    """
    symbol = symbol.upper()
    for o in orders if orders is not None else get_open_orders(symbol):
        if (o.get("symbol") or "").upper() != symbol:
            continue
        if o.get("parent_id"):
            continue  # a child leg, not the entry
        if o.get("filled_qty") not in ("0", 0, None):
            continue  # partially filled: a position exists, manage that instead
        if o.get("order_class") == "oco":
            continue  # a leftover exit pair, never an entry
        return o
    return None


def leg_price(order: dict | None) -> float | None:
    if not order:
        return None
    for field in ("stop_price", "limit_price"):
        if order.get(field):
            return float(order[field])
    return None


def split_resting(orders: list, positions: list) -> tuple[list, list]:
    """Split unfilled top-level orders into (entries, exits).

    Exit orders look exactly like entries from here: both rest unfilled at the
    top level once they are not nested under a bracket parent. An order facing
    an open position is protecting it, never opening one, and an OCO pair is an
    exit by construction.
    """
    held = {p["symbol"].upper(): ("long" if float(p["qty"]) > 0 else "short")
            for p in positions}

    def is_exit(o):
        if o.get("order_class") == "oco":
            return True
        side = held.get((o.get("symbol") or "").upper())
        if side is None:
            return False
        return o.get("side") == ("sell" if side == "long" else "buy")

    unfilled = [o for o in orders if o.get("filled_qty") in ("0", 0, None)
                and not o.get("parent_id")]
    return ([o for o in unfilled if not is_exit(o)],
            [o for o in unfilled if is_exit(o)])


def book_commitments(cfg: dict, equity: float, positions: list, orders: list,
                     journal: list[dict], prices: dict | None = None) -> dict:
    """What the book already has on, counting resting entries as if filled.

    An entry resting from an earlier session is a position waiting to happen:
    it takes a slot, and when it fills it adds its notional and its risk. The
    caps have to see it, or two briefs a day apart can jointly overshoot them.
    Risk is entry-to-stop per rule 1, floored at zero - a stop trailed past
    entry has nothing left at stake.
    """
    prices = prices or {}
    open_rows = {r["ticker"].upper(): r for r in journal
                 if r.get("r_multiple") in ("", None)
                 and r.get("exit_reason") != "never filled"}
    budget = equity * cfg["risk_per_trade_pct"] / 100.0

    book = {"count": 0, "gross": 0.0, "net": 0.0, "risk": 0.0,
            "held": set(), "resting": [], "resting_symbols": set()}

    for p in positions:
        sym = p["symbol"].upper()
        mv = float(p["market_value"])
        qty = abs(float(p["qty"]))
        side = "long" if float(p["qty"]) > 0 else "short"
        avg = float(p["avg_entry_price"])
        stop = leg_price(exit_legs(sym, side, orders)["stop_loss"])
        if stop is None:
            try:
                stop = float(open_rows.get(sym, {}).get("stop") or "")
            except ValueError:
                stop = None
        if stop is None:
            risk = budget  # unprotected and unknown: assume a full trade's risk
        else:
            risk = qty * max(0.0, (avg - stop) if side == "long" else (stop - avg))
        book["count"] += 1
        book["gross"] += abs(mv)
        book["net"] += mv
        book["risk"] += risk
        book["held"].add(sym)

    entries, _ = split_resting(orders, positions)
    for o in entries:
        sym = (o.get("symbol") or "").upper()
        side = "long" if o.get("side") == "buy" else "short"
        qty = abs(float(o.get("qty") or 0))
        entry = float(o.get("limit_price") or o.get("stop_price")
                      or prices.get(sym) or 0)
        stop = target = None
        for leg in o.get("legs") or []:
            if leg.get("type") in ("stop", "stop_limit", "trailing_stop"):
                stop = leg_price(leg)
            elif leg.get("type") == "limit":
                target = leg_price(leg)
        risk = qty * abs(entry - stop) if (stop is not None and entry) else budget
        notional = qty * entry
        book["count"] += 1
        book["gross"] += notional
        book["net"] += notional if side == "long" else -notional
        book["risk"] += risk
        book["resting_symbols"].add(sym)
        book["resting"].append({
            "symbol": sym, "side": side, "qty": qty, "type": o.get("type"),
            "entry": entry, "stop": stop, "target": target,
            "submitted": (o.get("submitted_at") or "")[:10],
        })
    return book


def parse_ts(value: str | None) -> datetime | None:
    """Alpaca timestamp -> aware datetime. Tolerates nanosecond fractions."""
    if not value:
        return None
    s = value.replace("Z", "+00:00")
    if "." in s:
        head, rest = s.split(".", 1)
        frac = "".join(ch for ch in rest if ch.isdigit())
        tz = rest[len(frac):]
        s = f"{head}.{frac[:6]}{tz}"
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        return None


ET = "America/New_York"


def et_today() -> str:
    from zoneinfo import ZoneInfo
    return datetime.now(ZoneInfo(ET)).strftime("%Y-%m-%d")


def fetch_bars(symbols: list[str], timeframe: str, start: str, end: str | None,
               feed: str, adjustment: str = "all") -> dict[str, list[dict]]:
    """Historical bars per symbol, oldest first, following pagination."""
    out: dict[str, list[dict]] = {}
    for i in range(0, len(symbols), 100):
        params = {"symbols": ",".join(symbols[i:i + 100]), "timeframe": timeframe,
                  "start": start, "adjustment": adjustment, "feed": feed,
                  "limit": 10000}
        if end:
            params["end"] = end
        while True:
            data = api("GET", "/v2/stocks/bars", base=DATA_BASE, params=params)
            for sym, bars in (data.get("bars") or {}).items():
                out.setdefault(sym.upper(), []).extend(bars or [])
            token = data.get("next_page_token")
            if not token:
                break
            params["page_token"] = token
    return out


def history_bars(symbols: list[str], feed: str, end: str,
                 timeframe: str = "1Day", start: str | None = None,
                 adjustment: str = "all") -> tuple[dict, str]:
    """Bars up to `end`, consolidated (SIP) when the plan allows it.

    The free plan serves SIP history as long as it stops more than 15 minutes
    ago, and SIP is the whole tape: IEX alone is a couple of percent of volume,
    which makes its averages useless for a volume filter and its highs and
    lows narrower than what actually traded. Falls back to the configured
    feed. Returns (bars, feed used).
    """
    if start is None:
        start = (datetime.fromisoformat(end[:10]) - timedelta(days=110)).strftime("%Y-%m-%d")
    for f in dict.fromkeys(("sip", feed)):
        try:
            return fetch_bars(symbols, timeframe, start, end, f, adjustment), f
        except RuntimeError:
            continue
    raise RuntimeError(f"no bars for {len(symbols)} symbols on sip or {feed}")


def fetch_movers(top: int = 50) -> dict:
    """Alpaca's movers screener: {"gainers": [...], "losers": [...], "last_updated"}."""
    return api("GET", "/v1beta1/screener/stocks/movers", base=DATA_BASE,
               params={"top": top})


def market_stats(bars: list[dict], snap: dict, today: str) -> dict | None:
    """Levels a brief needs, from completed daily bars plus today's snapshot."""
    hist = [b for b in bars if b["t"][:10] < today]
    if len(hist) < 2:
        return None
    closes = [b["c"] for b in hist]
    trs = [max(b["h"] - b["l"], abs(b["h"] - p["c"]), abs(b["l"] - p["c"]))
           for p, b in zip(hist, hist[1:])]
    mean = lambda xs: sum(xs) / len(xs) if xs else None
    s = {
        "prev": closes[-1],
        "atr": mean(trs[-14:]),
        "sma20": mean(closes[-20:]) if len(closes) >= 20 else None,
        "sma50": mean(closes[-50:]) if len(closes) >= 50 else None,
        "hi20": max(b["h"] for b in hist[-20:]),
        "lo20": min(b["l"] for b in hist[-20:]),
        "chg5": closes[-1] / closes[-6] - 1 if len(closes) >= 6 else None,
        "adv": mean([b["v"] for b in hist[-20:]]),
        "last": None, "last_t": None, "today": None,
    }
    trade = (snap or {}).get("latestTrade") or {}
    t = parse_ts(trade.get("t"))
    if t and trade.get("p"):
        from zoneinfo import ZoneInfo
        t_et = t.astimezone(ZoneInfo(ET))
        if t_et.strftime("%Y-%m-%d") == today:
            s["last"], s["last_t"] = float(trade["p"]), t_et
    day = (snap or {}).get("dailyBar") or {}
    if (day.get("t") or "")[:10] == today and day.get("o"):
        s["today"] = {k: float(day[k]) for k in ("o", "h", "l")}
    return s


def market_data_section(cfg: dict, held: list[str], resting: list[str],
                        market_open: bool) -> list[str]:
    """Markdown tables of prices and levels for the brief, grouped.

    Never raises: the brief is better written without this table than not
    written at all.
    """
    today = et_today()
    groups: list[tuple[str, list[str]]] = []
    mine = list(dict.fromkeys(held + resting))
    if mine:
        groups.append(("Your positions and resting entries", mine))
    for name, syms in (cfg.get("watchlist") or {}).items():
        groups.append((name, [s.upper() for s in syms]))

    movers, movers_note = {"gainers": [], "losers": []}, ""
    try:
        m = fetch_movers()
        for side in ("gainers", "losers"):
            movers[side] = [x for x in m.get(side) or []
                            if float(x.get("price") or 0) >= cfg["min_price"]
                            and str(x.get("symbol", "")).isalpha()]
        ts = parse_ts(m.get("last_updated"))
        if ts:
            from zoneinfo import ZoneInfo
            movers_note = f", screener as of {ts.astimezone(ZoneInfo(ET)):%Y-%m-%d %H:%M} ET"
    except RuntimeError as e:
        movers_note = f" - screener unavailable ({str(e)[:80]})"
    mover_syms = [x["symbol"].upper() for side in ("gainers", "losers")
                  for x in movers[side]]

    everything = list(dict.fromkeys([s for _, g in groups for s in g] + mover_syms))
    out = ["\n### Market data\n"]
    try:
        from zoneinfo import ZoneInfo
        midnight = datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=ZoneInfo(ET))
        bars, used = history_bars(everything, cfg["data_feed"],
                                  midnight.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
        snaps = get_snapshots(everything, cfg["data_feed"]) or {}
    except RuntimeError as e:
        return out + [f"*Unavailable this session: {str(e)[:200]}. Search for levels.*"]
    stats = {s: market_stats(bars.get(s, []), snaps.get(s) or {}, today) for s in everything}

    vol_note = ("consolidated volume" if used == "sip"
                else f"{used.upper()} volume only, a small slice of the tape")
    out.append(
        f"*From Alpaca. History and averages are completed sessions ({used.upper()}, "
        f"{vol_note}); last is today's latest {cfg['data_feed'].upper()} trade, which "
        "pre-market is a thin single-venue print - confirm it for anything you trade. "
        "A level taken from this table counts as verified. ATR is the 14-session "
        "average true range: a stop inside one ATR of entry is inside ordinary "
        "daily noise.*")

    def pct(x):
        return f"{x * 100:+.1f}%" if x is not None else "-"

    def fmt(x):
        return "-" if x is None else f"{x:,.2f}"

    def row(sym):
        s = stats.get(sym)
        if not s:
            return f"| {sym} | no data |" + " |" * (8 if market_open else 7)
        last = s["last"]
        cells = [
            sym,
            f"{last:,.2f} ({s['last_t']:%H:%M})" if last else "no trade today",
            pct(last / s["prev"] - 1) if last else "-",
            fmt(s["prev"]),
        ]
        if market_open:
            d = s["today"]
            cells.append(f"{d['o']:,.2f} / {d['l']:,.2f}-{d['h']:,.2f}" if d else "-")
        cells += [
            f"{s['atr']:,.2f} ({s['atr'] / s['prev'] * 100:.1f}%)" if s["atr"] else "-",
            f"{s['lo20']:,.2f}-{s['hi20']:,.2f}",
            " / ".join(pct(s["prev"] / m - 1) if m else "-" for m in (s["sma20"], s["sma50"])),
            pct(s["chg5"]),
            f"{s['adv'] / 1e6:,.1f}M" if s["adv"] else "-",
        ]
        return "| " + " | ".join(cells) + " |"

    head = ["Symbol", "Last (ET)", "vs prev", "Prev close"]
    if market_open:
        head.append("Today open / low-high")
    head += ["ATR14", "20d low-high", "Prev vs 20d / 50d avg", "5d", "Avg vol 20d"]
    header = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]

    for name, syms in groups:
        out += [f"\n#### {name}\n"] + header + [row(s) for s in syms]

    liquid = lambda sym: ((stats.get(sym) or {}).get("adv") or 0) >= cfg["min_avg_volume"] \
        if used == "sip" else True
    shown = {side: [x for x in movers[side] if liquid(x["symbol"].upper())][:cfg["movers_show"]]
             for side in ("gainers", "losers")}
    out.append(f"\n#### Movers (at least ${cfg['min_price']:g}"
               + (f" and {cfg['min_avg_volume'] / 1e6:g}M average volume" if used == "sip" else "")
               + f"{movers_note})\n")
    if shown["gainers"] or shown["losers"]:
        out += header + [row(x["symbol"].upper()) for side in ("gainers", "losers")
                         for x in shown[side]]
    else:
        out.append("*None passed the filter.*")
    return out


def last_price(snap: dict) -> float | None:
    """Best available reference price from a snapshot payload."""
    for key, field in (
        ("latestTrade", "p"),
        ("dailyBar", "c"),
        ("prevDailyBar", "c"),
        ("minuteBar", "c"),
    ):
        node = snap.get(key) or {}
        if node.get(field):
            return float(node[field])
    return None


# --------------------------------------------------------------------------
# Sizing and validation
# --------------------------------------------------------------------------

def size_position(equity: float, entry: float, stop: float, risk_pct: float) -> tuple[int, float]:
    """Derive share count from the stop distance. Returns (qty, risk_usd)."""
    per_share_risk = abs(entry - stop)
    if per_share_risk <= 0:
        return 0, 0.0
    budget = equity * (risk_pct / 100.0)
    qty = math.floor(budget / per_share_risk)
    return max(qty, 0), qty * per_share_risk


def validate_play(play: dict, ctx: dict) -> tuple[list[str], list[str], dict]:
    """Returns (errors, warnings, enriched). Errors block submission."""
    errors, warnings = [], []
    cfg, equity = ctx["cfg"], ctx["equity"]

    required = ["ticker", "direction", "entry", "stop", "targets"]
    for field in required:
        if play.get(field) in (None, "", []):
            errors.append(f"missing required field '{field}'")
    if errors:
        return errors, warnings, {}

    symbol = str(play["ticker"]).upper().strip()
    direction = str(play["direction"]).lower().strip()
    if direction not in ("long", "short"):
        errors.append(f"direction must be long or short, got '{direction}'")
        return errors, warnings, {}

    try:
        entry = float(play["entry"])
        stop = float(play["stop"])
        targets = [float(t) for t in play["targets"]]
    except (TypeError, ValueError):
        errors.append("entry/stop/targets must be numbers")
        return errors, warnings, {}

    target = targets[0]

    # A market entry fills wherever the market is, not at the level the brief
    # wrote down, so size and check it from the last price when there is one.
    if str(play.get("entry_type", "limit")).lower() == "market":
        ref = ctx["prices"].get(symbol)
        if ref:
            if abs(entry - ref) / ref > 0.005:
                warnings.append(f"market entry sized from the last price {ref:.2f}, "
                                f"not the stated {entry}")
            entry = ref

    # Geometry
    if direction == "long":
        if stop >= entry:
            errors.append(f"long stop {stop} must be below entry {entry}")
        if target <= entry:
            errors.append(f"long target {target} must be above entry {entry}")
    else:
        if stop <= entry:
            errors.append(f"short stop {stop} must be above entry {entry}")
        if target >= entry:
            errors.append(f"short target {target} must be below entry {entry}")

    # Reward:risk
    rr = None
    if abs(entry - stop) > 0:
        rr = abs(target - entry) / abs(entry - stop)
        if rr < 1.0:
            warnings.append(f"reward:risk is only {rr:.2f}R")

    # Probability and conviction
    p = play.get("p_target_first")
    if p is None:
        warnings.append("no p_target_first given - trade cannot be scored for calibration")
    else:
        try:
            p = float(p)
            if p > 100:
                errors.append(f"p_target_first {p} is not a probability")
                p = None
            elif 2 <= p <= 100:
                p = p / 100.0          # stated as a percentage
            elif 1 < p < 2:
                errors.append(
                    f"p_target_first {p} is ambiguous - use 0.65 or 65, not {p}"
                )
                p = None
            elif not 0 < p < 1:
                errors.append(
                    f"p_target_first must be strictly between 0 and 1 "
                    f"(no certainties), got {p}"
                )
                p = None
        except (TypeError, ValueError):
            errors.append("p_target_first must be a number")
            p = None

    conviction = play.get("conviction")
    try:
        if conviction is not None and float(conviction) < cfg["min_conviction"]:
            errors.append(f"conviction {conviction} below floor {cfg['min_conviction']}")
    except (TypeError, ValueError):
        errors.append(f"conviction must be a number 1-5, got '{conviction}'")

    # Risk tier. The play picks how much of the budget it spends; the harness
    # still derives the share count and never lets it exceed rule 1.
    cap_pct = cfg["risk_per_trade_pct"]
    risk_pct = cap_pct
    if play.get("risk_pct") not in (None, ""):
        try:
            risk_pct = float(play["risk_pct"])
        except (TypeError, ValueError):
            errors.append(f"risk_pct must be a number, got '{play['risk_pct']}'")
            risk_pct = cap_pct
        if risk_pct > cap_pct:
            warnings.append(f"risk_pct {risk_pct} is over the {cap_pct}% per-trade cap "
                            f"- sized at {cap_pct}%")
            risk_pct = cap_pct
        elif risk_pct < cfg["min_risk_pct"]:
            errors.append(f"risk_pct {risk_pct} is below the {cfg['min_risk_pct']}% floor")

    # Tradability
    try:
        asset = get_asset(symbol)
        if not asset.get("tradable"):
            errors.append(f"{symbol} is not tradable on Alpaca")
        if direction == "short":
            if not cfg["allow_shorts"]:
                errors.append("shorts disabled in config")
            elif not asset.get("shortable"):
                errors.append(f"{symbol} is not shortable")
            elif not asset.get("easy_to_borrow"):
                warnings.append(f"{symbol} is hard to borrow")
    except RuntimeError as e:
        errors.append(f"could not look up {symbol}: {e}")

    # Sizing
    qty, risk_usd = size_position(equity, entry, stop, risk_pct)
    if qty < 1:
        errors.append(
            f"stop is too wide to take even 1 share within "
            f"{risk_pct}% of equity (per-share risk "
            f"${abs(entry - stop):.2f})"
        )

    notional = qty * entry
    cap = equity * cfg["max_position_pct"] / 100.0
    if notional > cap:
        errors.append(
            f"notional ${notional:,.0f} is {notional / equity * 100:.0f}% of equity, "
            f"over the {cfg['max_position_pct']}% single-name cap - the stop is too "
            f"tight for this risk budget"
        )

    # Reference price sanity - catches stale or hallucinated levels
    ref = ctx["prices"].get(symbol)
    if ref:
        drift = abs(entry - ref) / ref
        if drift > 0.10:
            errors.append(
                f"entry {entry} is {drift:.0%} away from last price {ref:.2f} - "
                "verify this level, it looks stale"
            )
        elif drift > 0.03:
            warnings.append(f"entry {entry} is {drift:.1%} from last price {ref:.2f}")
    else:
        warnings.append(f"no reference price for {symbol} - could not sanity-check entry")

    # An entry on the wrong side of the market is not the order it looks like:
    # a stop trigger already passed fires at the open, and a limit through the
    # market fills there. Warnings only - the reference can be a stale IEX print.
    entry_type = str(play.get("entry_type", "limit")).lower()
    if ref:
        long = direction == "long"
        if entry_type == "stop" and (entry <= ref if long else entry >= ref):
            warnings.append(
                f"stop entry {entry} is already {'below' if long else 'above'} the "
                f"last price {ref:.2f} - it triggers at the open like a market order")
        if entry_type == "limit" and (entry > ref if long else entry < ref):
            warnings.append(
                f"limit {entry} is through the last price {ref:.2f} - it will fill "
                "at the open, not at a pullback")

    enriched = {
        "symbol": symbol, "direction": direction, "entry": entry, "stop": stop,
        "target": target, "qty": qty, "risk_usd": risk_usd, "notional": notional,
        "rr": rr, "p": p, "ref": ref, "risk_pct": risk_pct,
        "entry_type": entry_type,
    }
    return errors, warnings, enriched


def validate_manage(item: dict, ctx: dict) -> tuple[list[str], list[str], dict]:
    """Validate one position-management instruction against the live book.

    These act on positions that already exist, so nothing here is sized: the
    share count is whatever is open. Returns (errors, warnings, enriched).
    """
    errors, warnings = [], []
    cfg, equity = ctx["cfg"], ctx["equity"]

    if not item.get("ticker"):
        return ["missing required field 'ticker'"], warnings, {}
    symbol = str(item["ticker"]).upper().strip()

    action = str(item.get("action", "update")).lower().strip()
    if action not in ("update", "close"):
        return [f"action must be update or close, got '{action}'"], warnings, {}

    pos = next((p for p in ctx["positions"] if p["symbol"].upper() == symbol), None)
    resting = None
    if pos is None:
        try:
            resting = pending_entry(symbol)
        except RuntimeError as e:
            return [f"could not read open orders for {symbol}: {e}"], warnings, {}
        if resting is None:
            return ([f"no open {symbol} position and no resting entry order to "
                     "manage - use 'plays' to open one"], warnings, {})

    if pos is not None:
        pos_side = "long" if float(pos["qty"]) > 0 else "short"
        qty = abs(int(float(pos["qty"])))
        avg_entry = float(pos["avg_entry_price"])
        ref = ctx["prices"].get(symbol) or float(pos.get("current_price") or 0) or None
        # Levels are checked against the market: a stop on the wrong side of it
        # fires the moment it is accepted.
        guard_ref, guard_label = ref, "last price"
    else:
        pos_side = "long" if resting.get("side") == "buy" else "short"
        qty = abs(int(float(resting.get("qty") or 0)))
        avg_entry = float(resting.get("limit_price") or resting.get("stop_price") or 0)
        ref = ctx["prices"].get(symbol) or None
        # Nothing is filled yet and the legs are held until it is, so the market
        # price does not constrain them - the entry they hang off does.
        guard_ref, guard_label = (avg_entry or None), "entry"
        warnings.append(
            f"{symbol} entry is still resting unfilled at {avg_entry:.2f} - "
            + ("cancelling it" if action == "close"
               else "amending the bracket legs it will open with"))

    stop = target = None
    try:
        if item.get("stop") is not None:
            stop = float(item["stop"])
        if item.get("target") is not None:
            target = float(item["target"])
        elif item.get("targets"):
            target = float(item["targets"][0])
    except (TypeError, ValueError):
        return ["stop/target must be numbers"], warnings, {}

    if action == "update" and stop is None and target is None:
        errors.append("update needs at least one of 'stop' or 'target'")

    if action == "update" and guard_ref:
        # A level on the wrong side of the reference is one that resolves the
        # moment it goes live: against the market for an open position, against
        # the entry for a bracket that has not filled yet.
        fix = "close the position instead" if pos is not None else "re-enter instead"
        if pos_side == "long":
            if stop is not None and stop >= guard_ref:
                errors.append(
                    f"long stop {stop:.2f} is at or above {guard_label} "
                    f"{guard_ref:.2f} - it would trigger immediately; {fix}"
                )
            if target is not None and target <= guard_ref:
                errors.append(
                    f"long target {target:.2f} is at or below {guard_label} "
                    f"{guard_ref:.2f} - it would fill immediately; {fix}"
                )
        else:
            if stop is not None and stop <= guard_ref:
                errors.append(
                    f"short stop {stop:.2f} is at or below {guard_label} "
                    f"{guard_ref:.2f} - it would trigger immediately; {fix}"
                )
            if target is not None and target >= guard_ref:
                errors.append(
                    f"short target {target:.2f} is at or above {guard_label} "
                    f"{guard_ref:.2f} - it would fill immediately; {fix}"
                )
        for label, level in (("stop", stop), ("target", target)):
            if level is not None and abs(level - guard_ref) / guard_ref > 0.25:
                errors.append(
                    f"{label} {level:.2f} is {abs(level - guard_ref) / guard_ref:.0%} "
                    f"away from {guard_label} {guard_ref:.2f} - verify this level, "
                    "it looks stale"
                )
    elif action == "update" and not guard_ref:
        warnings.append(f"no reference price for {symbol} - could not sanity-check levels")

    if stop is not None and target is not None:
        if pos_side == "long" and stop >= target:
            errors.append(f"long stop {stop:.2f} is not below target {target:.2f}")
        if pos_side == "short" and stop <= target:
            errors.append(f"short stop {stop:.2f} is not above target {target:.2f}")

    # Rule 1 still binds: widening a stop must not put more than the risk budget
    # back at stake, measured entry-to-stop like any other trade.
    risk_usd = 0.0
    if stop is not None:
        per_share = (avg_entry - stop) if pos_side == "long" else (stop - avg_entry)
        risk_usd = max(0.0, per_share) * qty
        budget = equity * cfg["risk_per_trade_pct"] / 100.0
        if risk_usd > budget:
            errors.append(
                f"stop {stop:.2f} puts ${risk_usd:,.2f} "
                f"({risk_usd / equity * 100:.2f}% of equity) at risk against the "
                f"{avg_entry:.2f} average entry, over the "
                f"{cfg['risk_per_trade_pct']}% per-trade cap"
            )

    try:
        legs = exit_legs(symbol, pos_side)
    except RuntimeError as e:
        errors.append(f"could not read open orders for {symbol}: {e}")
        legs = {"take_profit": None, "stop_loss": None}

    if action == "update":
        for leg, level, label in (("stop_loss", stop, "stop"),
                                  ("take_profit", target, "take-profit")):
            if level is None or legs[leg]:
                continue
            if resting is not None:
                # Placing a fresh exit against an unfilled entry would be a
                # naked order in the opposite direction, not protection.
                errors.append(
                    f"the resting {symbol} entry has no {label} leg to amend - "
                    "cancel it and re-enter with the levels you want"
                )
            else:
                warnings.append(
                    f"no live {label} order found - a new one will be created")

    enriched = {
        "symbol": symbol, "action": action, "side": pos_side, "qty": qty,
        "entry_order": resting, "avg_entry": avg_entry, "ref": ref,
        "stop": stop, "target": target,
        "old_stop": leg_price(legs["stop_loss"]),
        "old_target": leg_price(legs["take_profit"]),
        "legs": legs, "risk_usd": risk_usd,
        # Filled in by apply_manage with the levels that actually landed, so
        # the journal records the live orders rather than the intent.
        "applied": {"stop": None, "target": None},
        # Failures apply_manage can recover from but must not hide.
        "failures": [],
        "reason": item.get("reason", ""),
    }
    return errors, warnings, enriched


def apply_manage(m: dict, tif: str) -> list[str]:
    """Push one validated management instruction to Alpaca. Returns log lines."""
    symbol, side, qty = m["symbol"], m["side"], m["qty"]
    exit_side = "sell" if side == "long" else "buy"
    log = []

    if m["action"] == "close" and m.get("entry_order"):
        # Nothing is filled, so there is no position to close - killing the
        # entry takes its held legs with it.
        api("DELETE", f"/v2/orders/{m['entry_order']['id']}")
        log.append(f"resting entry cancelled x{qty}")
        return log

    if m["action"] == "close":
        for leg in ("take_profit", "stop_loss"):
            order = m["legs"][leg]
            if order:
                try:
                    api("DELETE", f"/v2/orders/{order['id']}")
                except RuntimeError as e:
                    log.append(f"could not cancel {leg} ({e})")
                    m["failures"].append(
                        f"{leg} still resting after the close - it can open a "
                        f"reverse position ({e})")
        resp = api("DELETE", f"/v2/positions/{symbol}")
        log.append(f"close order sent x{qty} [{resp.get('status', 'submitted')}]")
        return log

    replaced = {"stop_loss": m["stop"], "take_profit": m["target"]}
    missing = {}
    for leg, level in replaced.items():
        label = "stop" if leg == "stop_loss" else "target"
        if level is None:
            continue
        order = m["legs"][leg]
        if not order:
            missing[leg] = level
            continue
        # A brief that moves one level restates the other unchanged. Alpaca
        # rejects a replace that changes nothing (422 "order parameters are not
        # changed"), so send only the legs that actually move - otherwise the
        # restated one fails the whole instruction and takes the real change,
        # or the missing protection below, down with it.
        current = leg_price(order)
        if current is not None and abs(current - level) < 0.005:
            log.append(f"{label} already at {level:.2f}, left alone")
            m["applied"][label] = level
            continue
        field = "stop_price" if leg == "stop_loss" else "limit_price"
        # One leg failing must not abort the other, and must not stop the
        # missing-protection step below from running.
        try:
            resp = api("PATCH", f"/v2/orders/{order['id']}", json={field: f"{level:.2f}"})
        except RuntimeError as e:
            log.append(f"x {label} -> {level:.2f} REJECTED BY ALPACA: {e}")
            continue
        m["legs"][leg] = resp or order
        m["applied"][label] = level
        log.append(f"{label} -> {level:.2f} [{resp.get('status', 'replaced')}]")

    if not missing:
        return log

    label_of = {"stop_loss": "stop", "take_profit": "target"}

    def oco_body(stop_level, target_level):
        return {
            "symbol": symbol, "qty": str(qty), "side": exit_side,
            "type": "limit", "time_in_force": tif, "order_class": "oco",
            "take_profit": {"limit_price": f"{target_level:.2f}"},
            "stop_loss": {"stop_price": f"{stop_level:.2f}"},
        }

    def single_body(leg, level):
        body = {"symbol": symbol, "qty": str(qty), "side": exit_side,
                "time_in_force": tif}
        if leg == "stop_loss":
            body.update({"type": "stop", "stop_price": f"{level:.2f}"})
        else:
            body.update({"type": "limit", "limit_price": f"{level:.2f}"})
        return body

    # Nothing live to amend on this side, so place fresh protection. If the
    # other side IS live, it gets folded into the new pair rather than left
    # beside it: two independent exits for one position means whichever fills
    # first leaves the other resting, and that opens a reverse position.
    survivor = survivor_leg = None
    if len(missing) == 1:
        other = "take_profit" if "stop_loss" in missing else "stop_loss"
        level = leg_price(m["legs"][other])
        if m["legs"][other] and level is not None:
            survivor, survivor_leg = m["legs"][other], other
            missing[other] = level

    if survivor is not None:
        # Alpaca will not accept a second exit for quantity this one holds, so
        # the pair has to replace it.
        try:
            api("DELETE", f"/v2/orders/{survivor['id']}")
            # It is gone until the pair below replaces it, so it stops counting
            # as applied - nothing should record a level that is not resting.
            m["applied"][label_of[survivor_leg]] = None
        except RuntimeError as e:
            log.append(f"x could not cancel the live {label_of[survivor_leg]} to "
                       f"pair it ({e}) - leaving it and placing the other side alone")
            missing.pop(survivor_leg)
            survivor = None

    if len(missing) == 2:
        try:
            resp = api("POST", "/v2/orders",
                       json=oco_body(missing["stop_loss"], missing["take_profit"]))
        except RuntimeError as e:
            # The survivor, if there was one, is already cancelled - so fall
            # through and place both sides standalone. Unlinked protection
            # beats none while the position is open.
            log.append(f"x OCO pair REJECTED BY ALPACA: {e} - placing each "
                       "side on its own instead")
        else:
            m["applied"].update({"stop": missing["stop_loss"],
                                 "target": missing["take_profit"]})
            log.append(
                f"new OCO stop {missing['stop_loss']:.2f} / target "
                f"{missing['take_profit']:.2f} [{resp.get('status', 'submitted')}]"
            )
            return log

    for leg, level in missing.items():
        label = label_of[leg]
        try:
            resp = api("POST", "/v2/orders", json=single_body(leg, level))
        except RuntimeError as e:
            log.append(f"x new {label} {level:.2f} REJECTED BY ALPACA: {e}")
            continue
        m["applied"][label] = level
        log.append(f"new {label} {level:.2f} [{resp.get('status', 'submitted')}]")
    return log


def conviction_of(p: dict) -> float:
    try:
        return float(p["raw"].get("conviction") or 0)
    except (TypeError, ValueError):
        return 0.0


def admit_plays(planned: list[dict], ctx: dict) -> tuple[list[dict], list[tuple], str | None]:
    """Admit plays against the book-level caps, highest conviction first.

    Returns (admitted, dropped, blocker). Each play is checked against what is
    already on the book plus everything admitted ahead of it, so one play too
    many costs that play, not the whole brief - and a smaller play further down
    can still fit where a larger one did not. Ties keep the brief's order.
    blocker is set when nothing may be admitted at all (the daily loss limit).
    """
    cfg, equity = ctx["cfg"], ctx["equity"]
    if ctx["daily_pnl_pct"] <= -cfg["daily_loss_limit_pct"]:
        return [], [], (f"DAILY LOSS LIMIT HIT ({ctx['daily_pnl_pct']:.2f}%) - "
                        "no new positions until next session")

    book = ctx["book"]
    count, gross, net, risk = book["count"], book["gross"], book["net"], book["risk"]
    gross_cap = equity * cfg["max_gross_exposure_pct"] / 100.0
    net_cap = equity * cfg["max_net_exposure_pct"] / 100.0
    risk_cap = equity * cfg["max_open_risk_pct"] / 100.0
    pct = (lambda x: x / equity * 100) if equity else (lambda x: 0.0)

    admitted, dropped, seen = [], [], set()
    order = sorted(enumerate(planned), key=lambda ip: (-conviction_of(ip[1]), ip[0]))
    for _, p in order:
        sym = p["symbol"]
        signed = p["notional"] if p["direction"] == "long" else -p["notional"]
        why = None
        if sym in book["held"]:
            why = "already held - one position per name; use manage to change it"
        elif sym in book["resting_symbols"]:
            why = ("already has a resting entry - use manage to amend or cancel "
                   "it instead of stacking a second")
        elif sym in seen:
            why = "appears twice in the same brief"
        elif count + 1 > cfg["max_positions"]:
            why = (f"would be {count + 1} positions and resting entries, cap is "
                   f"{cfg['max_positions']}")
        elif gross + p["notional"] > gross_cap:
            why = (f"gross exposure would be {pct(gross + p['notional']):.0f}% of "
                   f"equity, cap is {cfg['max_gross_exposure_pct']}%")
        elif abs(net + signed) > net_cap:
            why = (f"net exposure would be {pct(net + signed):+.0f}% of equity, cap is "
                   f"+/-{cfg['max_net_exposure_pct']}%")
        elif risk + p["risk_usd"] > risk_cap:
            why = (f"risk at stake would be {pct(risk + p['risk_usd']):.2f}% of equity, "
                   f"cap is {cfg['max_open_risk_pct']}%")
        seen.add(sym)
        if why:
            dropped.append((p, why))
            continue
        count += 1
        gross += p["notional"]
        net += signed
        risk += p["risk_usd"]
        p["book_after"] = {"gross": pct(gross), "net": pct(net), "risk": pct(risk)}
        admitted.append(p)
    return admitted, dropped, None


def validate_passed(item: dict, ctx: dict) -> tuple[list[str], dict]:
    """Check one passed idea well enough to score it. Returns (errors, enriched).

    No order is placed, so there is nothing to size or borrow - but the levels
    still have to be real, or the replay scores an idea that never existed.
    """
    errors = []
    for field in ("ticker", "direction", "entry", "stop"):
        if item.get(field) in (None, ""):
            errors.append(f"missing '{field}'")
    if errors:
        return errors, {}
    symbol = str(item["ticker"]).upper().strip()
    direction = str(item["direction"]).lower().strip()
    entry_type = str(item.get("entry_type", "limit")).lower()
    try:
        entry, stop = float(item["entry"]), float(item["stop"])
        target = float(item["target"] if item.get("target") is not None
                       else item["targets"][0])
    except (KeyError, IndexError, TypeError, ValueError):
        return ["entry, stop and target must be numbers"], {}
    if direction not in ("long", "short"):
        return [f"direction must be long or short, got '{direction}'"], {}
    if entry_type not in ("limit", "stop", "market"):
        return [f"entry_type must be limit, stop or market, got '{entry_type}'"], {}
    long = direction == "long"
    if (stop >= entry or target <= entry) if long else (stop <= entry or target >= entry):
        errors.append(f"{direction} levels out of order: entry {entry}, stop {stop}, "
                      f"target {target}")
    ref = ctx["prices"].get(symbol)
    if ref and abs(entry - ref) / ref > 0.10:
        errors.append(f"entry {entry} is {abs(entry - ref) / ref:.0%} from last price "
                      f"{ref:.2f} - not a real level")
    p = item.get("p_target_first")
    try:
        p = float(p) if p not in (None, "") else None
        if p is not None and 2 <= p <= 100:
            p /= 100.0
        if p is not None and not 0 < p < 1:
            errors.append(f"p_target_first {item['p_target_first']} is not a probability")
    except (TypeError, ValueError):
        errors.append(f"p_target_first must be a number, got '{p}'")
    return errors, {
        "symbol": symbol, "direction": direction, "entry_type": entry_type,
        "entry": entry, "stop": stop, "target": target, "p": p,
        "reason": str(item.get("reason", "")),
    }


# --------------------------------------------------------------------------
# Order submission
# --------------------------------------------------------------------------

def build_order(p: dict, tif: str) -> dict:
    side = "buy" if p["direction"] == "long" else "sell"
    order = {
        "symbol": p["symbol"],
        "qty": str(p["qty"]),
        "side": side,
        "time_in_force": tif,
        "order_class": "bracket",
        "take_profit": {"limit_price": f"{p['target']:.2f}"},
        "stop_loss": {"stop_price": f"{p['stop']:.2f}"},
    }
    if p["entry_type"] == "market":
        order["type"] = "market"
    elif p["entry_type"] == "stop":
        order["type"] = "stop"
        order["stop_price"] = f"{p['entry']:.2f}"
    else:
        order["type"] = "limit"
        order["limit_price"] = f"{p['entry']:.2f}"
    return order


# --------------------------------------------------------------------------
# Journal
# --------------------------------------------------------------------------

def ensure_journal():
    if not JOURNAL.exists():
        with JOURNAL.open("w", newline="") as f:
            csv.DictWriter(f, fieldnames=JOURNAL_FIELDS).writeheader()
        return
    with JOURNAL.open(newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames == JOURNAL_FIELDS:
            return
        rows = list(reader)
    # Older header. Rewrite it before anything appends, or new rows land under
    # the wrong columns. Rows from before the *_initial columns existed get them
    # filled in from what they were submitted with.
    for row in rows:
        stop0, target0 = submitted_levels(row)
        if row.get("stop_initial") in ("", None) and stop0 is not None:
            row["stop_initial"] = stop0
        if row.get("target_initial") in ("", None) and target0 is not None:
            row["target_initial"] = target0
    write_journal(rows)


def submitted_levels(row: dict) -> tuple[float | None, float | None]:
    """The stop and target a journal row was submitted with, recovered for rows
    logged before stop_initial / target_initial were recorded.

    The brief that proposed the play is the source. Failing that, the stop is
    exact from the sizing (risk_usd = qty x entry-to-stop distance), and the
    target falls back to whatever the row holds now.
    """
    stop0 = target0 = None
    brief = HERE / "briefs" / f"{row.get('session_date', '')}.md"
    try:
        doc = parse_plays(brief.read_text())
        for p in doc.get("plays", []):
            if str(p.get("ticker", "")).upper().strip() == row["ticker"].upper():
                stop0, target0 = float(p["stop"]), float(p["targets"][0])
                break
    except (OSError, ValueError, KeyError, TypeError, IndexError):
        pass
    try:
        if stop0 is None:
            entry, qty = float(row["entry_planned"]), float(row["qty"])
            dist = float(row["risk_usd"]) / qty
            stop0 = round(entry - dist if row["direction"] == "long" else entry + dist, 2)
        if target0 is None and row.get("target"):
            target0 = float(row["target"])
    except (KeyError, ValueError, ZeroDivisionError):
        pass
    return stop0, target0


def initial_levels(row: dict) -> tuple[float | None, float | None]:
    """(stop, target) the play was submitted with - what R and calibration use."""
    out = []
    for key, live in (("stop_initial", "stop"), ("target_initial", "target")):
        for k in (key, live):
            try:
                out.append(float(row[k]))
                break
            except (KeyError, TypeError, ValueError):
                continue
        else:
            out.append(None)
    return out[0], out[1]


def read_journal() -> list[dict]:
    ensure_journal()
    with JOURNAL.open(newline="") as f:
        return list(csv.DictReader(f))


def write_journal(rows: list[dict]):
    with JOURNAL.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=JOURNAL_FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in JOURNAL_FIELDS})


def update_journal_levels(symbol: str, stop=None, target=None, note: str = "") -> bool:
    """Rewrite the stop/target on the open journal row for a symbol.

    Keeps the journal (and therefore `prep`, which the brief is written from)
    honest about where the live orders actually sit.
    """
    rows = read_journal()
    hit = None
    for row in rows:
        if row.get("ticker", "").upper() != symbol.upper():
            continue
        if row.get("r_multiple") not in ("", None):
            continue  # already closed out
        hit = row
    if hit is None:
        return False
    if stop is not None:
        hit["stop"] = stop
    if target is not None:
        hit["target"] = target
    if note:
        hit["notes"] = " | ".join(x for x in (hit.get("notes", ""), note) if x)
    write_journal(rows)
    return True


def append_journal(row: dict):
    ensure_journal()
    with JOURNAL.open("a", newline="") as f:
        csv.DictWriter(f, fieldnames=JOURNAL_FIELDS).writerow(
            {k: row.get(k, "") for k in JOURNAL_FIELDS}
        )


def read_shadow() -> list[dict]:
    if not SHADOW.exists():
        return []
    with SHADOW.open(newline="") as f:
        return list(csv.DictReader(f))


def write_shadow(rows: list[dict]):
    with SHADOW.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SHADOW_FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in SHADOW_FIELDS})


def append_shadow(new: list[dict]):
    if new:
        write_shadow(read_shadow() + new)


# --------------------------------------------------------------------------
# Context
# --------------------------------------------------------------------------

def build_context(symbols: list[str]) -> dict:
    cfg = load_config()
    acct = get_account()
    equity = float(acct["equity"])
    last_equity = float(acct.get("last_equity") or equity)
    daily_pnl = equity - last_equity
    daily_pnl_pct = (daily_pnl / last_equity * 100) if last_equity else 0.0

    prices = {}
    try:
        snaps = get_snapshots(symbols, cfg["data_feed"])
        for sym, snap in (snaps or {}).items():
            price = last_price(snap or {})
            if price:
                prices[sym.upper()] = price
    except RuntimeError as e:
        print(f"  ! could not fetch reference prices: {e}", file=sys.stderr)

    positions = get_positions()
    # Not caught: without the open orders the caps cannot see resting entries,
    # and admitting new risk blind is worse than failing the run.
    orders = get_open_orders()
    book = book_commitments(cfg, equity, positions, orders, read_journal(), prices)

    return {
        "cfg": cfg, "account": acct, "equity": equity,
        "daily_pnl": daily_pnl, "daily_pnl_pct": daily_pnl_pct,
        "positions": positions, "prices": prices, "orders": orders, "book": book,
    }


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def parse_plays(text: str) -> dict:
    """The JSON block from a brief. Raises ValueError if there is none."""
    # Tolerate the JSON being wrapped in a markdown fence
    if "```" in text:
        chunks = text.split("```")
        for chunk in chunks:
            chunk = chunk.strip()
            if chunk.startswith("json"):
                chunk = chunk[4:].strip()
            if chunk.startswith("{"):
                text = chunk
                break
    return json.loads(text)


def load_plays(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        sys.exit(f"No such file: {path}")
    try:
        return parse_plays(p.read_text())
    except json.JSONDecodeError as e:
        sys.exit(f"{path} is not valid JSON: {e}")


def cmd_check(args, submit: bool = False):
    doc = load_plays(args.file)
    plays = doc.get("plays", [])
    manage = doc.get("manage", []) or []
    passed = doc.get("passed", []) or []
    session_date = doc.get("date") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    session = getattr(args, "session", None) or "pre-market"
    model = getattr(args, "model", None) or ""

    if doc.get("no_trade"):
        plays = []  # no_trade governs new entries only, never position management

    if not plays and not manage and not passed:
        print(f"\n{session_date}: no trades proposed.")
        if doc.get("session_note"):
            print(f"  {doc['session_note']}")
        return

    symbols = [p.get("ticker", "") for p in plays if p.get("ticker")]
    symbols += [m.get("ticker", "") for m in manage if m.get("ticker")]
    symbols += [x.get("ticker", "") for x in passed if x.get("ticker")]
    ctx = build_context(symbols)
    cfg = ctx["cfg"]

    print(f"\n{'=' * 68}")
    print(f"  SESSION {session_date}   equity ${ctx['equity']:,.2f}   "
          f"day P&L {ctx['daily_pnl_pct']:+.2f}%")
    print(f"{'=' * 68}")

    managed = []
    if manage:
        print(f"\n  POSITION MANAGEMENT")
        for item in manage:
            errors, warnings, m = validate_manage(item, ctx)
            tag = item.get("ticker", "?")
            if errors:
                print(f"\n  [REJECTED] {tag}")
                for err in errors:
                    print(f"      x {err}")
                continue
            managed.append(m)
            if m["action"] == "close":
                print(f"\n  [OK] {m['symbol']} CLOSE x{m['qty']}")
            else:
                print(f"\n  [OK] {m['symbol']} UPDATE x{m['qty']} "
                      f"({m['side']}, avg {m['avg_entry']:.2f})")
                if m["stop"] is not None:
                    old = f"{m['old_stop']:.2f}" if m["old_stop"] else "none"
                    print(f"      stop   {old} -> {m['stop']:.2f}")
                if m["target"] is not None:
                    old = f"{m['old_target']:.2f}" if m["old_target"] else "none"
                    print(f"      target {old} -> {m['target']:.2f}")
                if m["stop"] is not None:
                    print(f"      risk-at-stake ${m['risk_usd']:,.2f} "
                          f"({m['risk_usd'] / ctx['equity'] * 100:.2f}% of equity)")
            if m["reason"]:
                print(f"      {m['reason']}")
            for w in warnings:
                print(f"      ! {w}")
        print(f"\n  {'-' * 64}")

    approved, rejected = [], []
    for play in plays:
        errors, warnings, e = validate_play(play, ctx)
        tag = play.get("ticker", "?")
        if errors:
            rejected.append((tag, errors))
            print(f"\n  [REJECTED] {tag}")
            for err in errors:
                print(f"      x {err}")
            continue
        e["raw"] = play
        approved.append(e)
        print(f"\n  [OK] {e['symbol']} {e['direction'].upper()}")
        print(f"      entry {e['entry']:.2f} ({e['entry_type']})  "
              f"stop {e['stop']:.2f}  target {e['target']:.2f}"
              + (f"  [{e['rr']:.2f}R]" if e["rr"] else ""))
        print(f"      qty {e['qty']}  notional ${e['notional']:,.0f}  "
              f"risk ${e['risk_usd']:,.2f} "
              f"({e['risk_usd'] / ctx['equity'] * 100:.2f}% of equity, "
              f"tier {e['risk_pct']:g}%)")
        if e["p"] is not None:
            print(f"      P(target first) {e['p']:.0%}   "
                  f"conviction {play.get('conviction', '-')}")
        for w in warnings:
            print(f"      ! {w}")

    # Book-level caps govern new exposure only. Management of positions that
    # are already open is unaffected, so it goes through whatever happens here.
    dropped, blocker = [], None
    if approved:
        approved, dropped, blocker = admit_plays(approved, ctx)
        book = ctx["book"]
        eq = ctx["equity"] or 1
        print(f"\n  {'-' * 64}")
        print(f"  BOOK-LEVEL ADMISSION   highest conviction first")
        print(f"      book now: {book['count']} positions/resting entries, "
              f"gross {book['gross'] / eq * 100:.0f}%, net {book['net'] / eq * 100:+.0f}%, "
              f"risk at stake {book['risk'] / eq * 100:.2f}%")
        if blocker:
            print(f"      x {blocker}")
        for p in approved:
            after = p["book_after"]
            print(f"      + {p['symbol']:<6} admitted  -> gross {after['gross']:.0f}%, "
                  f"net {after['net']:+.0f}%, risk {after['risk']:.2f}%")
        for p, why in dropped:
            print(f"      x {p['symbol']:<6} dropped: {why}")

    # The shadow book: ideas passed on with real levels, plus plays the caps
    # dropped. No orders - they are replayed against the tape afterwards.
    logged_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    shadow_rows = []

    def shadow_row(e, source, p, reason):
        return {
            "shadow_id": uuid.uuid4().hex[:8], "logged_at": logged_at,
            "session_date": session_date, "session": session, "model": model,
            "source": source, "ticker": e["symbol"], "direction": e["direction"],
            "entry_type": e["entry_type"], "entry": e["entry"], "stop": e["stop"],
            "target": e["target"], "p_target_first": "" if p is None else p,
            "reason": reason, "status": "pending",
        }

    for p, why in dropped:
        shadow_rows.append(shadow_row(p, "dropped", p["p"], f"dropped by the caps: {why}"))
    if passed:
        print(f"\n  {'-' * 64}")
        print(f"  PASSED IDEAS   logged to the shadow book and scored later, no orders")
        for item in passed:
            errors, e = validate_passed(item, ctx)
            if errors:
                print(f"      x {item.get('ticker', '?'):<6} not logged: {'; '.join(errors)}")
                continue
            shadow_rows.append(shadow_row(e, "passed", e["p"], e["reason"]))
            print(f"      . {e['symbol']:<6} {e['direction']:<5} {e['entry_type']} "
                  f"{e['entry']:.2f}  stop {e['stop']:.2f}  target {e['target']:.2f}"
                  + (f"  P {e['p']:.0%}" if e["p"] is not None else ""))

    total_risk = sum(p["risk_usd"] for p in approved)
    print(f"\n  {'-' * 64}")
    if plays:
        n_dropped = len(dropped) or (len(plays) - len(rejected) if blocker else 0)
        print(f"  {len(approved)} approved, {len(rejected)} rejected"
              + (f", {n_dropped} dropped by book-level caps" if n_dropped else "")
              + f".  Total new risk ${total_risk:,.2f} "
                f"({total_risk / ctx['equity'] * 100:.2f}% of equity)")
    elif doc.get("no_trade"):
        print(f"  No new positions today.")
    if managed:
        print(f"  {len(managed)} position update(s) pending.")
    if shadow_rows:
        print(f"  {len(shadow_rows)} idea(s) for the shadow book.")

    if not approved and not managed and not shadow_rows:
        return
    if not submit:
        print("\n  Dry run. Re-run with `submit --confirm` to send these.\n")
        return
    if not args.confirm:
        print("\n  Add --confirm to actually submit.\n")
        return

    # Written first: it needs nothing from Alpaca, and the record of what was
    # passed on should not depend on whether an order went through.
    append_shadow(shadow_rows)

    clock = get_clock()
    if (approved or managed) and not clock.get("is_open"):
        print(f"\n  ! Market is closed. Next open: {clock.get('next_open')}")
        print("    Orders will queue. Market orders will fill at the next open.")

    print()
    # Anything the brief decided, that validation passed, and that then failed
    # to reach Alpaca. A session that does not place the stop it called for has
    # not done its job, however tidy the rest of the output looks.
    failures = []
    for m in managed:
        try:
            lines = apply_manage(m, cfg["time_in_force"])
        except RuntimeError as e:
            print(f"  x {m['symbol']} MANAGE REJECTED BY ALPACA: {e}")
            failures.append(f"{m['symbol']}: manage instruction rejected ({e})")
            continue
        for line in lines:
            print(f"  ~ {m['symbol']} {line}")
        failures.extend(f"{m['symbol']}: {f}" for f in m["failures"])
        if m["action"] == "update":
            for label, want in (("stop", m["stop"]), ("target", m["target"])):
                if want is not None and m["applied"][label] is None:
                    failures.append(
                        f"{m['symbol']}: {label} {want:.2f} is not resting at Alpaca")
        if m["action"] == "close":
            update_journal_levels(
                m["symbol"],
                note=f"{session_date}: close requested"
                     + (f" - {m['reason']}" if m["reason"] else ""),
            )
        else:
            applied = m["applied"]
            if applied["stop"] is None and applied["target"] is None:
                print(f"  x {m['symbol']} no level changed - journal left as it was")
                continue
            note = f"{session_date}: levels updated"
            if m["reason"]:
                note += f" - {m['reason']}"
            # Only what Alpaca accepted, so a half-applied update cannot leave
            # the journal (and tomorrow's brief, written from it) claiming a
            # stop that is not resting anywhere.
            if not update_journal_levels(m["symbol"], applied["stop"],
                                         applied["target"], note):
                print(f"  ! {m['symbol']} has no open journal row - "
                      "orders updated, journal not")

    for p in approved:
        order_body = build_order(p, cfg["time_in_force"])
        play_id = uuid.uuid4().hex[:8]
        try:
            resp = api("POST", "/v2/orders", json=order_body)
        except RuntimeError as e:
            print(f"  x {p['symbol']} REJECTED BY ALPACA: {e}")
            failures.append(f"{p['symbol']}: entry order rejected ({e})")
            continue
        raw = p["raw"]
        append_journal({
            "play_id": play_id,
            "logged_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "session_date": session_date,
            "ticker": p["symbol"], "direction": p["direction"],
            "entry_type": p["entry_type"], "entry_planned": p["entry"],
            "stop": p["stop"], "target": p["target"],
            "stop_initial": p["stop"], "target_initial": p["target"],
            "qty": p["qty"],
            "risk_usd": round(p["risk_usd"], 2),
            "risk_pct_equity": round(p["risk_usd"] / ctx["equity"] * 100, 3),
            "conviction": raw.get("conviction", ""),
            "p_target_first": p["p"] if p["p"] is not None else "",
            "time_horizon": raw.get("time_horizon", ""),
            "catalyst": raw.get("catalyst", ""),
            "thesis": raw.get("thesis", ""),
            "invalidation": raw.get("invalidation", ""),
            "bear_case": raw.get("bear_case", ""),
            "order_id": resp.get("id", ""),
            "status": resp.get("status", "submitted"),
            "session": session, "model": model,
        })
        print(f"  > {p['symbol']} {p['direction']} x{p['qty']} "
              f"submitted [{resp.get('status')}]  id={resp.get('id', '')[:8]}")
    print(f"\n  Logged to {JOURNAL.name}\n")

    if failures:
        # Non-zero so the workflow goes red. Everything above has already run,
        # including the journal writes, so the record of what was attempted
        # survives - the exit code exists to make the gap impossible to miss,
        # not to abandon the session.
        print(f"  {'-' * 64}")
        print("  THE BOOK DOES NOT MATCH THE BRIEF")
        for f in failures:
            print(f"      x {f}")
        print()
        sys.exit(1)


def cmd_submit(args):
    cmd_check(args, submit=True)


def cmd_status(args):
    cfg = load_config()
    acct = get_account()
    positions = get_positions()
    equity = float(acct["equity"])
    last_equity = float(acct.get("last_equity") or equity)
    daily_pnl = equity - last_equity
    daily_pnl_pct = (daily_pnl / last_equity * 100) if last_equity else 0
    gross = sum(abs(float(p["market_value"])) for p in positions)
    net = sum(float(p["market_value"]) for p in positions)

    clock = get_clock()
    print(f"\n{'=' * 68}")
    print(f"  BOOK STATE   market {'OPEN' if clock.get('is_open') else 'closed'}")
    print(f"{'=' * 68}")
    print(f"  Equity          ${equity:,.2f}")
    print(f"  Cash            ${float(acct['cash']):,.2f}")
    print(f"  Day P&L         ${daily_pnl:+,.2f}  ({daily_pnl_pct:+.2f}%)")
    print(f"  Gross exposure  ${gross:,.2f}  ({gross / equity * 100:.1f}% of equity)")
    print(f"  Net exposure    ${net:+,.2f}  ({net / equity * 100:+.1f}%)")
    print(f"  Positions       {len(positions)} / {cfg['max_positions']}")

    room = cfg["daily_loss_limit_pct"] + daily_pnl_pct
    if daily_pnl_pct <= -cfg["daily_loss_limit_pct"]:
        print(f"\n  *** DAILY LOSS LIMIT BREACHED - flatten and stand down ***")
    else:
        print(f"  Loss-limit room {room:.2f}% before the {cfg['daily_loss_limit_pct']}% "
              f"kill switch")

    if positions:
        print(f"\n  {'SYM':<7}{'SIDE':<7}{'QTY':>6}{'AVG':>11}{'LAST':>11}"
              f"{'P&L $':>12}{'P&L %':>9}")
        print(f"  {'-' * 63}")
        for p in sorted(positions, key=lambda x: -abs(float(x["market_value"]))):
            print(f"  {p['symbol']:<7}{p['side']:<7}{abs(int(float(p['qty']))):>6}"
                  f"{float(p['avg_entry_price']):>11.2f}"
                  f"{float(p['current_price']):>11.2f}"
                  f"{float(p['unrealized_pl']):>+12.2f}"
                  f"{float(p['unrealized_plpc']) * 100:>+8.2f}%")
    print()


def exit_fills(entry: dict, symbol: str, exit_side: str) -> list[dict]:
    """Every filled order that closed part of a position, oldest first.

    The exit is not always a leg of the bracket that opened the position.
    `manage` replaces legs (a replace is a new order with a new id), places
    fresh OCO pairs when protection is missing, and closes at market - none of
    which appear under the entry's `legs`. So take the bracket's own legs, then
    every closed order in the symbol submitted after the entry filled. Without
    nested=true each leg of an OCO comes back as an order of its own.
    """
    since = parse_ts(entry.get("filled_at"))
    seen, out = set(), []

    def take(nodes):
        for o in nodes or []:
            take(o.get("legs"))
            if o.get("id") in seen:
                continue
            seen.add(o.get("id"))
            if (o.get("symbol") or "").upper() != symbol:
                continue
            if o.get("side") != exit_side or not o.get("filled_avg_price"):
                continue
            if float(o.get("filled_qty") or 0) <= 0:
                continue
            filled = parse_ts(o.get("filled_at"))
            if since and filled and filled < since:
                continue
            out.append(o)

    take(entry.get("legs"))
    if since:
        # `after` filters on submission time. A second of slack costs nothing:
        # the fill-time check above is what actually decides.
        after = (since - timedelta(seconds=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        take(api("GET", "/v2/orders", params={
            "status": "closed", "symbols": symbol, "after": after,
            "direction": "asc", "limit": 500,
        }))
    epoch = datetime.min.replace(tzinfo=timezone.utc)
    out.sort(key=lambda o: parse_ts(o.get("filled_at")) or epoch)
    return out


def cmd_reconcile(args):
    rows = read_journal()
    if not rows:
        print("Journal is empty.")
        return
    updated, never_filled = 0, 0
    for row in rows:
        if row.get("r_multiple") not in ("", None):
            continue  # already closed out
        if row.get("exit_reason") == "never filled":
            continue  # already resolved as a non-trade
        oid = row.get("order_id")
        if not oid:
            continue
        try:
            order = api("GET", f"/v2/orders/{oid}", params={"nested": "true"})
        except RuntimeError as e:
            print(f"  ! {row['ticker']}: {e}")
            continue

        row["status"] = order.get("status", row.get("status", ""))
        entry_fill = order.get("filled_avg_price")

        # An entry that was cancelled or expired without filling is a prediction
        # that never became a trade. It must not sit in the journal looking like
        # an open position, and it cannot be scored - you can't measure whether
        # price hit a target from an entry you never took.
        if not entry_fill and row["status"] in ("canceled", "cancelled",
                                                "expired", "rejected"):
            row["exit_reason"] = "never filled"
            row["closed_at"] = order.get("canceled_at") or order.get("expired_at") or ""
            never_filled += 1
            print(f"  {row['ticker']:<6} never filled ({row['status']})")
            continue

        if not entry_fill:
            continue
        entry_fill = float(entry_fill)
        row["entry_fill"] = round(entry_fill, 4)

        long = row["direction"] == "long"
        symbol = row["ticker"].upper()
        qty = float(order.get("filled_qty") or row["qty"])
        try:
            fills = exit_fills(order, symbol, "sell" if long else "buy")
        except RuntimeError as e:
            print(f"  ! {row['ticker']}: could not read its exit orders: {e}")
            continue

        # Walk the exits oldest first until they account for the whole
        # position. Positions in one name never overlap (the harness will not
        # open a name already held), so the first `qty` shares sold after the
        # entry filled are this trade's.
        remaining, proceeds, last = qty, 0.0, None
        for o in fills:
            take = min(float(o["filled_qty"]), remaining)
            proceeds += take * float(o["filled_avg_price"])
            remaining -= take
            last = o
            if remaining <= 1e-9:
                break
        if last is None or remaining > 1e-9:
            continue  # still open, or not fully out yet

        exit_fill = proceeds / qty
        otype = last.get("type")
        exit_reason = ("target" if otype == "limit"
                       else "stop" if otype in ("stop", "stop_limit", "trailing_stop")
                       else "close")

        # Measured against the levels the play was submitted with. The live
        # stop may have been trailed past entry, and dividing by that turns a
        # winner into a loss.
        stop0, target0 = initial_levels(row)
        pnl = ((exit_fill - entry_fill) if long else (entry_fill - exit_fill)) * qty
        denom = ((entry_fill - stop0) if long else (stop0 - entry_fill)) if stop0 else 0
        r = (pnl / qty / denom) if denom > 0 else 0.0

        # p_target_first was about the initial target and stop. On an untouched
        # bracket the exit answers that directly. Once `manage` has moved the
        # levels, the fills only answer it when the exit was at or past the
        # initial target; otherwise which level price reached first is not
        # visible here, and the trade is left out of calibration.
        stop_now, target_now = row.get("stop"), row.get("target")
        moved = any(
            now not in ("", None) and init is not None
            and abs(float(now) - init) >= 0.005
            for now, init in ((stop_now, stop0), (target_now, target0)))
        if target0 is not None and (exit_fill >= target0 if long else exit_fill <= target0):
            hit = "1"
        elif exit_reason == "stop" and not moved:
            hit = "0"
        else:
            hit = ""

        row.update({
            "exit_fill": round(exit_fill, 4),
            "exit_reason": exit_reason,
            "pnl_usd": round(pnl, 2),
            "r_multiple": round(r, 3),
            "hit_target_first": hit,
            "closed_at": last.get("filled_at", "") or "",
        })
        updated += 1
        print(f"  closed {row['ticker']:<6} {exit_reason:<7} "
              f"{r:+.2f}R  ${pnl:+,.2f}"
              + ("" if hit else "  (levels were moved - not scored for calibration)"))

    write_journal(rows)
    print(f"\n  {updated} trade(s) closed out"
          + (f", {never_filled} never filled" if never_filled else "") + ".")
    if updated:
        print("  Fill in `thesis_verdict` by hand: right/wrong thesis vs right/wrong outcome.\n")


def replay_idea(row: dict, bars: list[dict], sessions: list[tuple], cfg: dict,
                now_limit: datetime) -> dict:
    """Replay one shadow idea against regular-session 5-minute bars.

    Fills and exits follow what the live bracket would have done: a limit
    fills at its price, or at the bar's open when the bar opens through it (a
    gap); a stop entry likewise; a market entry at the first bar's open; the
    exits the same way. Where one bar holds more than the order of events can
    be read from, the idea is marked ambiguous and left out of calibration
    rather than guessed. R is measured against the planned entry-to-stop
    distance. Returns the fields to update; status stays "pending" until the
    windows have closed or a level has been hit.
    """
    long = row["direction"] == "long"
    entry, stop, target = float(row["entry"]), float(row["stop"]), float(row["target"])
    etype = row.get("entry_type") or "limit"
    risk = abs(entry - stop) or 1e-9
    live_from = parse_ts(row["logged_at"])
    entry_days = sessions[:cfg["shadow_entry_sessions"]]
    exit_days = sessions[:cfg["shadow_exit_sessions"]]
    entry_set = {d for d, _, _ in entry_days}
    windows = {d: (o, c) for d, o, c in exit_days}

    from zoneinfo import ZoneInfo
    et = ZoneInfo(ET)
    usable = []
    for b in bars:
        t = parse_ts(b["t"])
        if t is None or t < live_from or t >= now_limit:
            continue
        day = t.astimezone(et).strftime("%Y-%m-%d")
        if day in windows and windows[day][0] <= t < windows[day][1]:
            usable.append((t, day, b))
    usable.sort(key=lambda x: x[0])

    def done(outcome, exit_px=None, exit_t=None):
        r = ""
        if exit_px is not None:
            r = round(((exit_px - fill) if long else (fill - exit_px)) / risk, 3)
        return {"status": "resolved", "outcome": outcome,
                "entry_fill": "" if fill is None else round(fill, 4),
                "filled_at": filled_at.isoformat() if filled_at else "",
                "exit_price": "" if exit_px is None else round(exit_px, 4),
                "exit_at": exit_t.isoformat() if exit_t else "",
                "r_multiple": r,
                "hit_target_first": {"target": "1", "stop": "0"}.get(outcome, ""),
                "evaluated_through": now_limit.isoformat(timespec="minutes")}

    def beyond_stop(px):
        return px <= stop if long else px >= stop

    def beyond_target(px):
        return px >= target if long else px <= target

    fill = filled_at = None
    for t, day, b in usable:
        o, h, l, c = (float(b[k]) for k in ("o", "h", "l", "c"))
        lo_hit, hi_hit = (l, h) if long else (h, l)  # adverse, favourable extremes
        if fill is None:
            if day not in entry_set:
                break
            at_open = False
            if etype == "market":
                fill, at_open = o, True
            elif etype == "stop":  # trigger in the favourable direction
                if (o >= entry) if long else (o <= entry):
                    fill, at_open = o, True
                elif (h >= entry) if long else (l <= entry):
                    fill = entry
            else:
                if (o <= entry) if long else (o >= entry):
                    fill, at_open = o, True
                elif (l <= entry) if long else (h >= entry):
                    fill = entry
            if fill is None:
                continue
            filled_at = t
            s_hit, t_hit = beyond_stop(lo_hit), beyond_target(hi_hit)
            stop_px = min(stop, fill) if long else max(stop, fill)
            tgt_px = max(target, fill) if long else min(target, fill)
            if at_open:
                if s_hit and t_hit:
                    return done("ambiguous")
                if s_hit:
                    return done("stop", stop_px, t)
                if t_hit:
                    return done("target", tgt_px, t)
            else:
                # Mid-bar fill. A limit is reached on the way towards the stop,
                # so a stop in the same bar came after it; a target may have
                # come before. A stop entry is the mirror image.
                if etype == "limit" and s_hit and not t_hit:
                    return done("stop", stop, t)
                if etype == "stop" and t_hit and not s_hit:
                    return done("target", target, t)
                if s_hit or t_hit:
                    return done("ambiguous")
            continue
        if beyond_stop(o):
            return done("stop", o, t)
        if beyond_target(o):
            return done("target", o, t)
        s_hit, t_hit = beyond_stop(lo_hit), beyond_target(hi_hit)
        if s_hit and t_hit:
            return done("ambiguous")
        if s_hit:
            return done("stop", stop, t)
        if t_hit:
            return done("target", target, t)

    pending = {"status": "pending", "evaluated_through": now_limit.isoformat(timespec="minutes")}
    if fill is None:
        if entry_days and entry_days[-1][2] <= now_limit:
            return done("never filled")
        return pending
    if exit_days and len(exit_days) == cfg["shadow_exit_sessions"] \
            and exit_days[-1][2] <= now_limit:
        return done("expired", float(usable[-1][2]["c"]), usable[-1][0])
    return {**pending, "entry_fill": round(fill, 4), "filled_at": filled_at.isoformat()}


def cmd_shadow(args):
    """Replay pending shadow ideas against the tape and record what happened."""
    rows = read_shadow()
    pending = [r for r in rows if r.get("status") != "resolved"]
    if not pending:
        print("  No pending ideas in the shadow book.")
        return
    cfg = load_config()
    # Consolidated history is free once it is 15 minutes old.
    now_limit = datetime.now(timezone.utc) - timedelta(minutes=16)

    first = min(r["session_date"] for r in pending)
    last = (now_limit + timedelta(days=1)).strftime("%Y-%m-%d")
    end_cal = (datetime.strptime(last, "%Y-%m-%d") + timedelta(days=30)).strftime("%Y-%m-%d")
    cal = api("GET", "/v2/calendar", params={"start": first, "end": end_cal})
    all_sessions = [(d["date"], *session_bounds(d)) for d in cal]

    by_symbol: dict[str, list[dict]] = {}
    for r in pending:
        by_symbol.setdefault(r["ticker"].upper(), []).append(r)

    resolved = 0
    for sym, group in by_symbol.items():
        start = min(parse_ts(r["logged_at"]) for r in group)
        if start >= now_limit:
            continue
        try:
            bars, _ = history_bars([sym], cfg["data_feed"],
                                   now_limit.strftime("%Y-%m-%dT%H:%M:%SZ"),
                                   timeframe="5Min", adjustment="raw",
                                   start=start.strftime("%Y-%m-%dT%H:%M:%SZ"))
        except RuntimeError as e:
            print(f"  ! {sym}: {e}")
            continue
        for r in group:
            sessions = [s for s in all_sessions if s[0] >= r["session_date"]]
            r.update(replay_idea(r, bars.get(sym, []), sessions, cfg, now_limit))
            if r["status"] == "resolved":
                resolved += 1
                print(f"  {r['ticker']:<6} {r['direction']:<5} {r['outcome']:<12} "
                      + (f"{float(r['r_multiple']):+.2f}R" if r["r_multiple"] != "" else "")
                      + f"  ({r['source']} {r['session_date']})")
    write_shadow(rows)
    print(f"\n  {resolved} idea(s) resolved, "
          f"{sum(1 for r in rows if r.get('status') != 'resolved')} still pending.")


def calibration_rows(rows: list[dict]) -> list[dict]:
    return [r for r in rows if r.get("p_target_first") not in ("", None)
            and r.get("hit_target_first") not in ("", None)]


def print_calibration(scored: list[dict], what: str):
    """Stated probability against outcome, bucketed, with a Brier score."""
    print(f"\n  {'-' * 64}")
    print(f"  CALIBRATION   {len(scored)} {what} with a stated probability")
    print(f"  {'-' * 64}")
    buckets = [(0, .5), (.5, .6), (.6, .7), (.7, .8), (.8, .9), (.9, 1.01)]
    print(f"  {'stated':<14}{'n':>4}{'mean said':>12}{'actual':>10}")
    brier = 0.0
    for lo, hi in buckets:
        in_b = [r for r in scored if lo <= float(r["p_target_first"]) < hi]
        if not in_b:
            continue
        said = sum(float(r["p_target_first"]) for r in in_b) / len(in_b)
        hit = sum(int(r["hit_target_first"]) for r in in_b) / len(in_b)
        flag = "  <-- overconfident" if said - hit > 0.15 else ""
        print(f"  {lo:.0%}-{hi if hi <= 1 else 1:.0%}{'':<7}{len(in_b):>4}"
              f"{said:>11.0%}{hit:>10.0%}{flag}")
    for r in scored:
        brier += (float(r["p_target_first"]) - int(r["hit_target_first"])) ** 2
    brier /= len(scored)
    print(f"\n  Brier score     {brier:.3f}   "
          f"(0 = perfect, 0.25 = coin flip, lower is better)")
    if len(scored) < 20:
        print(f"  ! Only {len(scored)} samples - treat this as directional, not conclusive.")


def shadow_summary(rows: list[dict]) -> dict:
    """Counts and hypothetical R for the resolved part of the shadow book."""
    done = [r for r in rows if r.get("status") == "resolved"]
    by = lambda o: [r for r in done if r.get("outcome") == o]
    rs = [float(r["r_multiple"]) for r in done if r.get("r_multiple") not in ("", None)]
    return {
        "logged": len(rows), "resolved": len(done),
        "never": len(by("never filled")), "target": len(by("target")),
        "stop": len(by("stop")), "expired": len(by("expired")),
        "ambiguous": len(by("ambiguous")),
        "avg_r": sum(rs) / len(rs) if rs else None, "n_r": len(rs),
    }


def print_shadow_report(trades: list[dict]):
    shadow = read_shadow()
    if not shadow:
        return
    s = shadow_summary(shadow)
    print(f"\n{'=' * 68}")
    print(f"  SHADOW BOOK   {s['logged']} ideas passed on or dropped, {s['resolved']} resolved")
    print(f"{'=' * 68}")
    print(f"  Never filled    {s['never']}")
    print(f"  Target first    {s['target']}")
    print(f"  Stop first      {s['stop']}")
    print(f"  Expired         {s['expired']}   (neither level inside the window)")
    print(f"  Ambiguous       {s['ambiguous']}   (both in one bar - not scored)")
    if s["avg_r"] is not None:
        taken = [float(r["r_multiple"]) for r in trades]
        print(f"  Avg R if taken  {s['avg_r']:+.2f}R over {s['n_r']} filled ideas"
              + (f"   (trades actually taken: {sum(taken) / len(taken):+.2f}R)" if taken else ""))
        print("  A shadow book that out-earns the trades taken says the filter is "
              "rejecting\n  the better ideas.")
    scored = calibration_rows(shadow)
    if scored:
        print_calibration(scored, "passed ideas")
    both = calibration_rows(trades) + scored
    if scored and calibration_rows(trades):
        print_calibration(both, "trades and passed ideas together")


def cmd_score(args):
    all_rows = read_journal()
    rows = [r for r in all_rows if r.get("r_multiple") not in ("", None)]

    unfilled = [r for r in all_rows if r.get("exit_reason") == "never filled"]
    proposed = len(rows) + len(unfilled)
    if proposed:
        fill_rate = len(rows) / proposed * 100
        print(f"\n  Entry fill rate  {fill_rate:.0f}%  "
              f"({len(rows)} filled / {proposed} proposed, "
              f"{len(unfilled)} never reached)")
        if fill_rate < 50 and proposed >= 10:
            print("  ! Over half of proposed entries never filled. The levels are "
                  "probably unrealistic\n    rather than the theses being wrong.")

    if not rows:
        print("No closed trades yet. Run `reconcile` first.")
        print_shadow_report(rows)
        return

    rs = [float(r["r_multiple"]) for r in rows]
    pnls = [float(r["pnl_usd"]) for r in rows]
    wins = [x for x in rs if x > 0]
    losses = [x for x in rs if x <= 0]
    n = len(rs)

    print(f"\n{'=' * 68}")
    print(f"  PERFORMANCE   {n} closed trades")
    print(f"{'=' * 68}")
    print(f"  Net P&L         ${sum(pnls):+,.2f}")
    print(f"  Win rate        {len(wins) / n * 100:.1f}%  ({len(wins)}W / {len(losses)}L)")
    if wins:
        print(f"  Avg win         {sum(wins) / len(wins):+.2f}R")
    if losses:
        print(f"  Avg loss        {sum(losses) / len(losses):+.2f}R")
    print(f"  Expectancy      {sum(rs) / n:+.2f}R per trade")
    print(f"  Total R         {sum(rs):+.2f}R")
    print(f"  Best / worst    {max(rs):+.2f}R / {min(rs):+.2f}R")

    # Equity-curve drawdown in R terms
    peak, dd, cum = 0.0, 0.0, 0.0
    for r in rs:
        cum += r
        peak = max(peak, cum)
        dd = min(dd, cum - peak)
    print(f"  Max drawdown    {dd:.2f}R")

    # Calibration
    scored = calibration_rows(rows)
    unscorable = sum(1 for r in rows if r.get("hit_target_first") in ("", None))
    if unscorable:
        print(f"\n  {unscorable} closed trade(s) left out of calibration: their levels "
              "were moved\n  or they were closed by hand, so the fills do not show "
              "whether the\n  initial target or the initial stop came first.")
    if scored:
        print_calibration(scored, "trades")

    verdicts = [r.get("thesis_verdict", "").strip().lower() for r in rows]
    lucky = sum(1 for v in verdicts if v in ("wrong thesis right outcome", "lucky"))
    if lucky:
        print(f"\n  ! {lucky} trade(s) marked wrong-thesis/right-outcome. "
              f"These are the dangerous ones.")
    if not any(verdicts):
        print(f"\n  Note: thesis_verdict column is empty. Fill it in to separate "
              f"skill from luck.")
    print_shadow_report(rows)
    print()


def market_hours_utc() -> tuple[dict, datetime, datetime] | None:
    """Today's session as (calendar_day, open_utc, close_utc), or None.

    None means today is not a US trading day. Both times come from Alpaca's
    calendar rather than a hardcoded 09:30/16:00, so US daylight saving and
    half-day early closes (the day after Thanksgiving, Christmas Eve) are
    handled without this code knowing they exist.
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    days = api("GET", "/v2/calendar", params={"start": today, "end": today})
    if not days:
        return None
    return (days[0], *session_bounds(days[0]))


def session_bounds(day: dict) -> tuple[datetime, datetime]:
    """(open_utc, close_utc) for one entry of Alpaca's calendar."""
    from zoneinfo import ZoneInfo

    base = datetime.strptime(day["date"], "%Y-%m-%d")

    def et_to_utc(hhmm: str, fallback: str) -> datetime:
        hh, mm = (hhmm or fallback).split(":")[:2]
        return base.replace(hour=int(hh), minute=int(mm),
                            tzinfo=ZoneInfo(ET)).astimezone(timezone.utc)

    return et_to_utc(day.get("open"), "09:30"), et_to_utc(day.get("close"), "16:00")


def cmd_wait(args):
    """Sleep until a target time, then return. No-op if that time already passed.

    Used to hold a CI job open so the work lands at a predictable time
    regardless of when the triggering cron actually started. GitHub's scheduled
    triggers are delayed unpredictably (observed: 2+ hours), but a job that is
    already running can simply wait out the difference.

    The target is either a fixed wall clock (--time/--tz) or, preferably,
    derived from today's actual session (--before-open/--after-open/
    --before-close). The derived form is correct across daylight saving on
    both sides and on half-day early closes; a fixed wall clock is not.
    """
    import time

    if any(x is not None for x in (args.before_open, args.after_open, args.before_close)):
        hours = market_hours_utc()
        if hours is None:
            print("Not a US trading day - nothing to wait for, proceeding now.")
            return
        _, open_utc, close_utc = hours
        if args.before_open is not None:
            target_utc = open_utc - timedelta(minutes=args.before_open)
            label = f"{args.before_open} min before the open ({open_utc:%H:%M} UTC)"
        elif args.after_open is not None:
            target_utc = open_utc + timedelta(minutes=args.after_open)
            label = f"{args.after_open} min after the open ({open_utc:%H:%M} UTC)"
        else:
            target_utc = close_utc - timedelta(minutes=args.before_close)
            label = f"{args.before_close} min before the close ({close_utc:%H:%M} UTC)"
    else:
        if not args.tz:
            sys.exit("--time requires --tz (e.g. --tz Europe/Stockholm)")
        from zoneinfo import ZoneInfo
        tz = ZoneInfo(args.tz)
        hh, mm = args.time.split(":")
        # Anchored to today in --tz. It never rolls forward to tomorrow: a
        # target that has already passed is a no-op, not a 23-hour sleep.
        target_utc = datetime.now(tz).replace(
            hour=int(hh), minute=int(mm), second=0, microsecond=0
        ).astimezone(timezone.utc)
        label = f"{args.time} {args.tz}"

    now_utc = datetime.now(timezone.utc)
    secs = (target_utc - now_utc).total_seconds()

    if secs <= 0:
        print(f"Already {abs(secs) / 60:.0f} min past {label} "
              f"({target_utc.isoformat()}) - proceeding now.")
        return

    print(f"Holding open {secs / 60:.1f} min until {label} "
          f"({target_utc.isoformat()})...")
    sys.stdout.flush()          # so the log shows the wait before it starts
    time.sleep(secs)
    print("Target time reached.")


def cmd_calendar(args):
    """Exit 0 if today is a US trading day, 1 if not. For CI guards.

    With --before-open, also requires that the market has not yet opened (plus a
    margin). A delayed run that lands after the open is writing a "pre-market"
    brief with the market already trading — a different information set from
    every other session, which quietly corrupts comparisons across the record.
    Standing down costs one session; running anyway costs comparability.
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # A RuntimeError here is an API failure and is deliberately NOT caught: it
    # propagates to main(), which exits non-zero, and the CI guard stands the
    # session down. Failing closed is the right default when we cannot confirm
    # the market is open. Only a malformed calendar payload is tolerated below.
    try:
        hours = market_hours_utc()
    except (ValueError, KeyError, TypeError) as e:
        print(f"  ! could not resolve the session times ({e}) - not enforcing deadline.")
        sys.exit(0)

    if hours is None:
        print(f"{today} is not a US trading day - standing down.")
        sys.exit(1)

    d, open_utc, close_utc = hours
    print(f"{today} is a trading day (open {d.get('open')} close {d.get('close')} ET)")

    if args.open_window is not None:
        # The post-open review is written from the first stretch of the
        # session. Too early and the open has not settled; too late and it is
        # a different session from every other review in the record.
        lo, hi = args.open_window
        mins = (datetime.now(timezone.utc) - open_utc).total_seconds() / 60
        if lo <= mins <= hi and datetime.now(timezone.utc) < close_utc:
            print(f"  {mins:.0f} min after the open - inside the {lo}-{hi} min window.")
            sys.exit(0)
        print(f"  OUTSIDE THE WINDOW: {mins:.0f} min after the open, window is "
              f"{lo}-{hi} min. Standing down.")
        sys.exit(1)

    if args.before_open is None:
        sys.exit(0)

    now = datetime.now(timezone.utc)
    deadline = open_utc - timedelta(minutes=args.before_open)
    mins = (open_utc - now).total_seconds() / 60

    if now >= deadline:
        state = f"{abs(mins):.0f} min after the open" if mins < 0 \
            else f"only {mins:.0f} min before the open"
        print(f"  DEADLINE MISSED: it is {state}, and the cutoff is "
              f"{args.before_open} min before.")
        print(f"  Standing down. A post-open brief is not comparable with the rest "
              f"of the record.")
        sys.exit(1)

    print(f"  {mins:.0f} min before the open - inside the pre-market window.")
    sys.exit(0)


def cmd_prep(args):
    """Markdown block of current book state, to paste into the brief request."""
    from zoneinfo import ZoneInfo

    cfg = load_config()
    acct = get_account()
    positions = get_positions()
    equity = float(acct["equity"])
    last_equity = float(acct.get("last_equity") or equity)
    daily_pnl_pct = ((equity - last_equity) / last_equity * 100) if last_equity else 0

    journal = read_journal()
    by_symbol = {}
    for r in journal:
        if r.get("r_multiple") in ("", None) and r.get("exit_reason") != "never filled":
            by_symbol[r["ticker"]] = r

    try:
        live_orders = get_open_orders()
    except RuntimeError:
        live_orders = []
    book = book_commitments(cfg, equity, positions, live_orders, journal)
    pct = lambda x: x / equity * 100 if equity else 0.0

    # The clock, stated outright. The brief used to be told it was written
    # before the 08:30 ET releases, and after the session moved to 09:05 ET it
    # kept discarding prints it had found because the prompt said they could
    # not exist yet.
    now = datetime.now(timezone.utc)
    et = ZoneInfo("America/New_York")
    now_et = now.astimezone(et)
    try:
        hours = market_hours_utc()
    except (RuntimeError, ValueError, KeyError, TypeError):
        hours = None
    clock = f"**{now_et:%H:%M} ET** ({now:%H:%M} UTC), {now_et:%A %Y-%m-%d}"
    if hours is None:
        clock += ". The US market is closed today."
    else:
        _, open_utc, close_utc = hours
        mins = (open_utc - now).total_seconds() / 60
        if mins > 0:
            clock += (f". The cash session opens at {open_utc.astimezone(et):%H:%M} ET, "
                      f"in {mins:.0f} min, and closes at {close_utc.astimezone(et):%H:%M} ET. "
                      f"Anything scheduled before {now_et:%H:%M} ET today has already "
                      "been released: look up the actual figure and the market's "
                      "reaction, not the consensus.")
        elif now < close_utc:
            clock += (f". The cash session opened {-mins:.0f} min ago and closes at "
                      f"{close_utc.astimezone(et):%H:%M} ET.")
        else:
            clock += ". Today's cash session has closed."

    out = []
    out.append(f"## Current book state")
    out.append(f"*Auto-generated. These are live figures - use them, do not estimate.*\n")
    out.append(f"- Time now: {clock}")
    out.append(f"- Equity: **${equity:,.2f}**")
    out.append(f"- Cash: ${float(acct['cash']):,.2f}")
    out.append(f"- Session P&L so far: {daily_pnl_pct:+.2f}% "
               f"(new entries are blocked at -{cfg['daily_loss_limit_pct']}%)")
    out.append(f"- Gross exposure: ${book['gross']:,.0f} ({pct(book['gross']):.0f}% of "
               f"equity, cap {cfg['max_gross_exposure_pct']}%)")
    out.append(f"- Net exposure: ${book['net']:+,.0f} ({pct(book['net']):+.0f}%, "
               f"cap +/-{cfg['max_net_exposure_pct']}%)")
    risk_left = max(0.0, cfg["max_open_risk_pct"] - pct(book["risk"]))
    out.append(f"- Risk at stake (entry to stop): ${book['risk']:,.0f} "
               f"({pct(book['risk']):.2f}% of equity, cap {cfg['max_open_risk_pct']}%) "
               f"— {risk_left:.2f}% left for new plays")
    slots = max(0, cfg["max_positions"] - book["count"])
    out.append(f"- Slots: {len(positions)} open + {len(book['resting'])} resting "
               f"entries of {cfg['max_positions']} — you may add at most {slots} more")
    if book["resting"] or positions:
        out.append("- *Gross, net, risk and slots count resting entries as if filled.*")

    # Sizing is derived, so the model cannot see notional. Tell it how tight a
    # stop the remaining room allows, or it proposes plays the caps then drop.
    gross_room = pct(cfg["max_gross_exposure_pct"] * equity / 100 - book["gross"])
    net_now = pct(book["net"])
    for side, net_room in (("long", cfg["max_net_exposure_pct"] - net_now),
                           ("short", cfg["max_net_exposure_pct"] + net_now)):
        room = min(cfg["max_position_pct"], gross_room, net_room)
        if room <= 0:
            out.append(f"- A new {side} does not fit: no gross or net room left.")
        else:
            out.append(f"- A new {side} can be up to {room:.0f}% of equity in notional: "
                       f"at 1% risk its stop must be at least {100 / room:.1f}% from "
                       f"entry (half that at 0.5%, a quarter at 0.25%).")

    if positions:
        out.append(f"\n### Open positions\n")
        out.append("*Stop and target are the live resting orders. To change them, put the "
                   "position in the `manage` array of your JSON block — prose alone does "
                   "not move an order.*\n")
        out.append("| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        for p in positions:
            j = by_symbol.get(p["symbol"], {})
            thesis = (j.get("thesis") or "-").replace("|", "/")[:120]
            legs = exit_legs(p["symbol"], p["side"], live_orders)
            stop = leg_price(legs["stop_loss"])
            target = leg_price(legs["take_profit"])
            stop_s = f"{stop:.2f}" if stop else f"{j.get('stop', '-')} (no live order)"
            target_s = f"{target:.2f}" if target else f"{j.get('target', '-')} (no live order)"
            out.append(
                f"| {p['symbol']} | {p['side']} | {abs(int(float(p['qty'])))} "
                f"| {float(p['avg_entry_price']):.2f} | {float(p['current_price']):.2f} "
                f"| {float(p['unrealized_pl']):+,.0f} ({float(p['unrealized_plpc']) * 100:+.1f}%) "
                f"| {stop_s} | {target_s} | {thesis} |"
            )
    else:
        out.append(f"\n*No open positions.*")

    if book["resting"]:
        out.append(f"\n### Resting entries (unfilled, carried from earlier sessions)\n")
        out.append("*These are live GTC orders and fill without you. Re-proposing the name "
                   "in `plays` is rejected; to change the levels use `manage` with "
                   "`update`, to withdraw the idea use `manage` with `close`. Unfilled "
                   "entries are cancelled after 5 days and before every weekend.*\n")
        out.append("| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |")
        out.append("|---|---|---|---|---|---|---|---|")
        fmt = lambda x: f"{x:.2f}" if x else "-"
        for e in book["resting"]:
            out.append(f"| {e['symbol']} | {e['side']} | {e['qty']:g} | {fmt(e['entry'])} "
                       f"| {e['type']} | {fmt(e['stop'])} | {fmt(e['target'])} "
                       f"| {e['submitted']} |")

    closed = [r for r in journal if r.get("r_multiple") not in ("", None)]
    if closed:
        rs = [float(r["r_multiple"]) for r in closed]
        wins = sum(1 for x in rs if x > 0)
        out.append(f"\n### Record\n")
        out.append(f"{len(closed)} closed trades: {wins}W / {len(closed) - wins}L, "
                   f"total {sum(rs):+.2f}R, net ${sum(float(r['pnl_usd']) for r in closed):+,.0f} "
                   f"realized. Shorts taken: "
                   f"{sum(1 for r in journal if r.get('direction') == 'short')}.")
    recent = sorted(closed, key=lambda r: r.get("closed_at", ""), reverse=True)[:5]
    if recent:
        out.append(f"\n### Last {len(recent)} closed trades\n")
        out.append("| Symbol | Direction | Exit | R | P&L | You said |")
        out.append("|---|---|---|---|---|---|")
        for r in recent:
            p = r.get("p_target_first", "")
            p_str = f"{float(p):.0%}" if p else "-"
            out.append(
                f"| {r['ticker']} | {r['direction']} | {r.get('exit_reason', '-')} "
                f"| {float(r['r_multiple']):+.2f}R | ${float(r['pnl_usd']):+,.0f} | {p_str} |"
            )

    # What the ideas it passed on went on to do. Without this a pass can never
    # be wrong on the record, and standing aside is free.
    shadow = read_shadow()
    done = [r for r in shadow if r.get("status") == "resolved"]
    if done:
        s = shadow_summary(shadow)
        out.append(f"\n### Ideas you passed on, replayed against the tape\n")
        out.append(f"{s['resolved']} resolved: {s['target']} reached target first, "
                   f"{s['stop']} stop first, {s['never']} never reached the entry, "
                   f"{s['expired']} expired, {s['ambiguous']} ambiguous."
                   + (f" Average {s['avg_r']:+.2f}R across the {s['n_r']} that would "
                      "have filled." if s["avg_r"] is not None else ""))
        recent = sorted(done, key=lambda r: r.get("exit_at") or r.get("evaluated_through", ""),
                        reverse=True)[:5]
        out.append("\n| Session | Symbol | Direction | Why passed | Outcome | R | You said |")
        out.append("|---|---|---|---|---|---|---|")
        for r in recent:
            p, rm = r.get("p_target_first"), r.get("r_multiple")
            why = (r.get("reason") or "-").replace("|", "/")[:80]
            out.append(
                f"| {r['session_date']} {r.get('session', '')} | {r['ticker']} "
                f"| {r['direction']} | {why} | {r['outcome']} "
                f"| {f'{float(rm):+.2f}R' if rm not in ('', None) else '-'} "
                f"| {f'{float(p):.0%}' if p not in ('', None) else '-'} |")

    market_open = bool(hours) and hours[1] <= now < hours[2]
    out += market_data_section(cfg, [p["symbol"].upper() for p in positions],
                               [e["symbol"] for e in book["resting"]], market_open)

    text = "\n".join(out) + "\n"
    if args.out:
        Path(args.out).write_text(text)
        print(f"Wrote book state to {args.out}")
    else:
        print(text)


EQUITY_CSV = HERE / "state" / "equity.csv"
EQUITY_FIELDS = ["date", "equity", "cash", "gross_exposure", "net_exposure", "positions"]

README_START = "<!-- PERFORMANCE:START -->"
README_END = "<!-- PERFORMANCE:END -->"


def snapshot_equity():
    """Append today's book snapshot to equity.csv. Idempotent per date."""
    acct = get_account()
    positions = get_positions()
    equity = float(acct["equity"])
    row = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "equity": round(equity, 2),
        "cash": round(float(acct["cash"]), 2),
        "gross_exposure": round(sum(abs(float(p["market_value"])) for p in positions), 2),
        "net_exposure": round(sum(float(p["market_value"]) for p in positions), 2),
        "positions": len(positions),
    }
    EQUITY_CSV.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    if EQUITY_CSV.exists():
        with EQUITY_CSV.open(newline="") as f:
            rows = [r for r in csv.DictReader(f) if r["date"] != row["date"]]
    rows.append(row)
    rows.sort(key=lambda r: r["date"])
    with EQUITY_CSV.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EQUITY_FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in EQUITY_FIELDS})
    return rows


def fetch_portfolio_history() -> dict:
    """Daily mark-to-market equity from Alpaca. Returns {date: equity}."""
    for period in ("all", "1A", "3M", "1M"):
        try:
            h = api("GET", "/v2/account/portfolio/history",
                    params={"period": period, "timeframe": "1D",
                            "pnl_reset": "no_reset"})
            ts, eq = h.get("timestamp") or [], h.get("equity") or []
            if ts and eq:
                out = {}
                for t, e in zip(ts, eq):
                    if e:
                        d = datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d")
                        out[d] = float(e)
                if out:
                    return out
        except RuntimeError:
            continue
    return {}


def fetch_spy(start: str, end: str, feed: str) -> dict:
    """Split- and dividend-adjusted SPY daily closes. Returns {date: close}."""
    params = {"symbols": "SPY", "timeframe": "1Day", "start": start, "end": end,
              "feed": feed, "limit": 10000, "adjustment": "all"}
    try:
        data = api("GET", "/v2/stocks/bars", base=DATA_BASE, params=params)
    except RuntimeError as e:
        print(f"  ! could not fetch SPY bars: {e}", file=sys.stderr)
        return {}
    bars = (data.get("bars") or {}).get("SPY") or []
    return {b["t"][:10]: float(b["c"]) for b in bars if b.get("c")}


def max_drawdown(series: list[float]) -> float:
    peak, dd = series[0], 0.0
    for v in series:
        peak = max(peak, v)
        dd = min(dd, (v - peak) / peak)
    return dd * 100


def cmd_chart(args):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    cfg = load_config()
    rows = snapshot_equity()

    curve = fetch_portfolio_history()
    if not curve:
        # Fall back to our own record if Alpaca's history is unavailable.
        curve = {r["date"]: float(r["equity"]) for r in rows}
    if len(curve) < 2:
        print("Not enough history to plot yet — need at least two sessions.")
        return

    dates = sorted(curve)
    spy = fetch_spy(dates[0], dates[-1], cfg["data_feed"])

    # Only compare on dates where both series exist.
    common = [d for d in dates if d in spy]
    use_bench = len(common) >= 2

    d_desk = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
    v_desk = [curve[d] for d in dates]
    n_desk = [v / v_desk[0] * 100 for v in v_desk]

    if use_bench:
        d_bench = [datetime.strptime(d, "%Y-%m-%d") for d in common]
        v_bench = [spy[d] for d in common]
        n_bench = [v / v_bench[0] * 100 for v in v_bench]

    # ---- plot -----------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=160)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    ax.plot(d_desk, n_desk, color="#1a7f7a", linewidth=2.0, label="Desk", zorder=3)
    if use_bench:
        ax.plot(d_bench, n_bench, color="#9aa0a6", linewidth=1.6,
                linestyle="--", label="S&P 500 (SPY, buy & hold)", zorder=2)

    ax.axhline(100, color="#d0d0d0", linewidth=0.9, zorder=1)
    ax.fill_between(d_desk, 100, n_desk,
                    where=[v >= 100 for v in n_desk],
                    color="#1a7f7a", alpha=0.08, zorder=0, interpolate=True)
    ax.fill_between(d_desk, 100, n_desk,
                    where=[v < 100 for v in n_desk],
                    color="#c0392b", alpha=0.08, zorder=0, interpolate=True)

    ax.set_ylabel("Normalised (start = 100)", fontsize=9, color="#444")
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    ax.grid(True, axis="y", color="#eeeeee", linewidth=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#cccccc")
    ax.tick_params(colors="#666", labelsize=8)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    # Whole-day ticks only. The default locator drops to sub-day intervals on
    # short ranges, which renders as the same date repeated.
    span = max(1, (d_desk[-1] - d_desk[0]).days)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=max(1, span // 8)))
    fig.autofmt_xdate(rotation=0, ha="center")

    closed = [r for r in read_journal() if r.get("r_multiple") not in ("", None)]
    sessions = len(dates)

    # Small samples are persuasive in a way they have no right to be. Say so
    # on the image itself, because the image is what gets looked at.
    if sessions < 30 or len(closed) < 20:
        ax.text(0.5, 0.5,
                f"PRELIMINARY\n{sessions} sessions, {len(closed)} closed "
                f"{'trade' if len(closed) == 1 else 'trades'}\n"
                "not yet a meaningful sample",
                transform=ax.transAxes, ha="center", va="center",
                fontsize=15, color="#b0b0b0", alpha=0.55, weight="bold",
                linespacing=1.5, zorder=5)

    ax.set_title("Paper desk vs. buy-and-hold", fontsize=11,
                 color="#222", loc="left", pad=12)
    fig.tight_layout()
    out_png = HERE / "state" / "performance.png"
    fig.savefig(out_png, facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_png.relative_to(HERE)}")

    # ---- stats ----------------------------------------------------------
    desk_ret = (v_desk[-1] / v_desk[0] - 1) * 100
    desk_dd = max_drawdown(v_desk)
    exposures = [float(r["gross_exposure"]) / float(r["equity"]) * 100
                 for r in rows if float(r.get("equity") or 0) > 0]
    avg_exp = sum(exposures) / len(exposures) if exposures else 0.0

    lines = [README_START, "", f"![Performance](state/performance.png)", ""]
    lines.append(f"| | Desk | SPY buy & hold |")
    lines.append("|---|---|---|")
    if use_bench:
        bench_ret = (v_bench[-1] / v_bench[0] - 1) * 100
        bench_dd = max_drawdown(v_bench)
        lines.append(f"| Return | {desk_ret:+.2f}% | {bench_ret:+.2f}% |")
        lines.append(f"| Max drawdown | {desk_dd:.2f}% | {bench_dd:.2f}% |")
    else:
        lines.append(f"| Return | {desk_ret:+.2f}% | — |")
        lines.append(f"| Max drawdown | {desk_dd:.2f}% | — |")
    lines.append(f"| Avg. gross exposure | {avg_exp:.0f}% | 100% |")
    lines.append("")
    trade_word = "trade" if len(closed) == 1 else "trades"
    lines.append(f"*{sessions} sessions, {len(closed)} closed {trade_word}, "
                 f"updated {dates[-1]}.*")
    lines.append("")
    lines.append("The desk holds cash most of the time and SPY does not, so this "
                 "is not a like-for-like comparison — read it alongside the "
                 "exposure row rather than as a scoreboard. "
                 "SPY is dividend- and split-adjusted.")
    if sessions < 30 or len(closed) < 20:
        lines.append("")
        lines.append("**Sample is far too small to mean anything.** At this length "
                     "the curve is dominated by noise; a rising line is not evidence "
                     "of edge. See the calibration table for a measure that becomes "
                     "informative sooner.")
    lines.append("")
    lines.append(README_END)
    block = "\n".join(lines)

    if args.update_readme:
        readme = HERE / "README.md"
        text = readme.read_text()
        if README_START in text and README_END in text:
            pre = text.split(README_START)[0]
            post = text.split(README_END, 1)[1]
            readme.write_text(pre + block + post)
            print("Updated README.md performance block.")
        else:
            print(f"! README.md has no {README_START} / {README_END} markers - "
                  f"add them where you want the chart.")
    else:
        print("\n" + block)


def cmd_stale(args):
    orders = api("GET", "/v2/orders", params={"status": "open", "nested": "true"})

    # Cancelling an exit does not abandon a thesis, it strips an open position
    # of its stop - and weekend.yml runs this with no age filter, so without
    # the split the Friday cleanup would take every protective order off the
    # book before two days of news.
    unfilled, protecting = split_resting(orders, get_positions())
    if protecting:
        print(f"\n  {len(protecting)} resting exit order(s) left alone "
              "(protecting an open position):")
        for o in protecting:
            print(f"    {o['symbol']:<7}{o['side']:<6}x{o['qty']:<6} "
                  f"{o.get('order_class') or o['type']:<8}"
                  f"@{o.get('limit_price') or o.get('stop_price') or '-'}")

    if args.older_than is not None:
        now = datetime.now(timezone.utc)
        aged = []
        for o in unfilled:
            try:
                sub = datetime.fromisoformat(
                    o["submitted_at"].replace("Z", "+00:00")
                )
                if (now - sub).days >= args.older_than:
                    aged.append(o)
            except (KeyError, ValueError):
                continue
        unfilled = aged

    if not unfilled:
        print(f"\n  No unfilled entry orders"
              + (f" older than {args.older_than}d" if args.older_than else "") + ".\n")
        return
    print(f"\n  {len(unfilled)} unfilled entry order(s):")
    for o in unfilled:
        print(f"    {o['symbol']:<7}{o['side']:<6}x{o['qty']:<6} "
              f"{o['type']:<7}@{o.get('limit_price') or o.get('stop_price')}  "
              f"submitted {o['submitted_at'][:10]}  id={o['id'][:8]}")
    if args.confirm:
        for o in unfilled:
            api("DELETE", f"/v2/orders/{o['id']}")
            print(f"    cancelled {o['symbol']}")
        print()
    else:
        print("\n  Add --confirm to cancel all of these.\n")


def cmd_flatten(args):
    positions = get_positions()
    if not positions and not args.confirm:
        print("\n  No open positions.\n")
        return
    print(f"\n  This will close {len(positions)} position(s) and cancel all orders.")
    if not args.confirm:
        print("  Add --confirm to proceed.\n")
        return
    api("DELETE", "/v2/positions", params={"cancel_orders": "true"})
    print("  Book flattened and orders cancelled.\n")


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Alpaca paper trading desk harness.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check", help="validate and size a plays file, send nothing")
    p.add_argument("file")
    p.set_defaults(func=lambda a: cmd_check(a, submit=False))

    p = sub.add_parser("submit", help="validate, size, and submit a plays file")
    p.add_argument("file")
    p.add_argument("--confirm", action="store_true", help="actually send the orders")
    p.add_argument("--session", choices=["pre-market", "open"], default="pre-market",
                   help="which session wrote the brief, recorded in the journal")
    p.add_argument("--model", default=os.environ.get("DESK_MODEL", ""),
                   help="model that wrote the brief, recorded in the journal")
    p.set_defaults(func=cmd_submit)

    p = sub.add_parser("status", help="account, exposure, positions, loss-limit room")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("reconcile", help="pull fills and close out journal rows")
    p.set_defaults(func=cmd_reconcile)

    p = sub.add_parser("score", help="performance and calibration report")
    p.set_defaults(func=cmd_score)

    p = sub.add_parser("shadow", help="replay passed ideas against the tape and score them")
    p.set_defaults(func=cmd_shadow)

    p = sub.add_parser("wait", help="hold open until a target time, no-op if already past")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--before-open", type=int, metavar="MIN",
                   help="wait until MIN minutes before today's open (preferred)")
    g.add_argument("--after-open", type=int, metavar="MIN",
                   help="wait until MIN minutes after today's open")
    g.add_argument("--before-close", type=int, metavar="MIN",
                   help="wait until MIN minutes before today's close")
    g.add_argument("--time", metavar="HH:MM",
                   help="wait until this fixed wall-clock time; needs --tz")
    p.add_argument("--tz", metavar="IANA_TZ",
                   help="timezone for --time, e.g. Europe/Stockholm")
    p.set_defaults(func=cmd_wait)

    p = sub.add_parser("calendar", help="exit 0 if today is a US trading day, else 1")
    p.add_argument("--before-open", type=int, metavar="MIN",
                   help="also require at least MIN minutes remain before the open")
    p.add_argument("--open-window", type=int, nargs=2, metavar=("FROM", "TO"),
                   help="also require it to be FROM-TO minutes after today's open")
    p.set_defaults(func=cmd_calendar)

    p = sub.add_parser("prep", help="markdown book state for the brief request")
    p.add_argument("--out", help="write to this file instead of stdout")
    p.set_defaults(func=cmd_prep)

    p = sub.add_parser("chart", help="equity curve vs SPY, and README stats block")
    p.add_argument("--update-readme", action="store_true",
                   help="rewrite the PERFORMANCE block in README.md")
    p.set_defaults(func=cmd_chart)

    p = sub.add_parser("stale", help="list or cancel unfilled entry orders")
    p.add_argument("--confirm", action="store_true", help="cancel them")
    p.add_argument("--older-than", type=int, metavar="DAYS",
                   help="only those submitted at least this many days ago")
    p.set_defaults(func=cmd_stale)

    p = sub.add_parser("flatten", help="close everything (kill switch)")
    p.add_argument("--confirm", action="store_true")
    p.set_defaults(func=cmd_flatten)

    args = ap.parse_args()
    try:
        args.func(args)
    except RuntimeError as e:
        sys.exit(f"\nAPI error: {e}\n")
    except KeyboardInterrupt:
        sys.exit("\nInterrupted.")


if __name__ == "__main__":
    main()