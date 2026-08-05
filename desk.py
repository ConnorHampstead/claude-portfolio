#!/usr/bin/env python3
"""
desk.py - paper trading desk harness for Alpaca.

Takes a JSON block of proposed trades (emitted by Claude alongside its morning
brief), enforces the risk rules, sizes positions from the stop, submits bracket
orders to an Alpaca PAPER account, and logs everything for later scoring.

Commands:
    check     Validate a plays file and print the sized plan. Sends nothing.
    submit    Same as check, then actually submit. Requires --confirm.
    status    Account state: equity, exposure, positions, loss-limit headroom.
    reconcile Pull fills from Alpaca and update the journal with outcomes.
    score     Performance and calibration report from the journal.
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
from datetime import datetime, timezone
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
    "risk_per_trade_pct": 1.0,      # max % of equity risked entry-to-stop
    "max_positions": 5,             # max concurrent open positions
    "max_gross_exposure_pct": 100,  # max gross notional as % of equity
    "max_position_pct": 50,         # max notional in any single name, % of equity
    "daily_loss_limit_pct": 3.0,    # flatten + stand down past this
    "min_conviction": 1,            # reject plays below this
    "time_in_force": "gtc",         # gtc or day
    "data_feed": "iex",             # iex (free) or sip (paid)
    "allow_shorts": True,
}

JOURNAL_FIELDS = [
    "play_id", "logged_at", "session_date", "ticker", "direction",
    "entry_type", "entry_planned", "stop", "target", "qty",
    "risk_usd", "risk_pct_equity", "conviction", "p_target_first",
    "time_horizon", "catalyst", "thesis", "invalidation", "bear_case",
    "order_id", "status", "entry_fill", "exit_fill", "exit_reason",
    "pnl_usd", "r_multiple", "hit_target_first", "closed_at",
    "thesis_verdict", "notes",
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
    if conviction is not None and float(conviction) < cfg["min_conviction"]:
        errors.append(f"conviction {conviction} below floor {cfg['min_conviction']}")

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
    qty, risk_usd = size_position(equity, entry, stop, cfg["risk_per_trade_pct"])
    if qty < 1:
        errors.append(
            f"stop is too wide to take even 1 share within "
            f"{cfg['risk_per_trade_pct']}% of equity (per-share risk "
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

    enriched = {
        "symbol": symbol, "direction": direction, "entry": entry, "stop": stop,
        "target": target, "qty": qty, "risk_usd": risk_usd, "notional": notional,
        "rr": rr, "p": p, "ref": ref,
        "entry_type": str(play.get("entry_type", "limit")).lower(),
    }
    return errors, warnings, enriched


def portfolio_checks(planned: list[dict], ctx: dict) -> list[str]:
    """Rules that apply across the whole book, not to individual plays."""
    problems = []
    cfg, equity = ctx["cfg"], ctx["equity"]
    open_count = len(ctx["positions"])

    if open_count + len(planned) > cfg["max_positions"]:
        problems.append(
            f"would hold {open_count + len(planned)} positions, cap is "
            f"{cfg['max_positions']} ({open_count} already open)"
        )

    open_notional = sum(abs(float(p["market_value"])) for p in ctx["positions"])
    new_notional = sum(p["notional"] for p in planned)
    gross_pct = (open_notional + new_notional) / equity * 100 if equity else 0
    if gross_pct > cfg["max_gross_exposure_pct"]:
        problems.append(
            f"gross exposure would be {gross_pct:.0f}% of equity, cap is "
            f"{cfg['max_gross_exposure_pct']}%"
        )

    held = {p["symbol"] for p in ctx["positions"]}
    for p in planned:
        if p["symbol"] in held:
            problems.append(f"{p['symbol']} is already held - no adding via this path")

    seen = set()
    for p in planned:
        if p["symbol"] in seen:
            problems.append(f"{p['symbol']} appears twice in the same brief")
        seen.add(p["symbol"])

    if ctx["daily_pnl_pct"] <= -cfg["daily_loss_limit_pct"]:
        problems.append(
            f"DAILY LOSS LIMIT HIT ({ctx['daily_pnl_pct']:.2f}%) - "
            "no new positions until next session"
        )
    return problems


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


def append_journal(row: dict):
    ensure_journal()
    with JOURNAL.open("a", newline="") as f:
        csv.DictWriter(f, fieldnames=JOURNAL_FIELDS).writerow(
            {k: row.get(k, "") for k in JOURNAL_FIELDS}
        )


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

    return {
        "cfg": cfg, "account": acct, "equity": equity,
        "daily_pnl": daily_pnl, "daily_pnl_pct": daily_pnl_pct,
        "positions": get_positions(), "prices": prices,
    }


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def load_plays(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        sys.exit(f"No such file: {path}")
    text = p.read_text()
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
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        sys.exit(f"{path} is not valid JSON: {e}")


def cmd_check(args, submit: bool = False):
    doc = load_plays(args.file)
    plays = doc.get("plays", [])
    session_date = doc.get("date") or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if doc.get("no_trade") or not plays:
        print(f"\n{session_date}: no trades proposed.")
        if doc.get("session_note"):
            print(f"  {doc['session_note']}")
        return

    ctx = build_context([p.get("ticker", "") for p in plays if p.get("ticker")])
    cfg = ctx["cfg"]

    print(f"\n{'=' * 68}")
    print(f"  SESSION {session_date}   equity ${ctx['equity']:,.2f}   "
          f"day P&L {ctx['daily_pnl_pct']:+.2f}%")
    print(f"{'=' * 68}")

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
              f"({e['risk_usd'] / ctx['equity'] * 100:.2f}% of equity)")
        if e["p"] is not None:
            print(f"      P(target first) {e['p']:.0%}   "
                  f"conviction {play.get('conviction', '-')}")
        for w in warnings:
            print(f"      ! {w}")

    problems = portfolio_checks(approved, ctx)
    if problems:
        print(f"\n  {'-' * 64}\n  BOOK-LEVEL VIOLATIONS")
        for pr in problems:
            print(f"      x {pr}")
        print("\n  Nothing submitted. Fix the brief and re-run.")
        return

    total_risk = sum(p["risk_usd"] for p in approved)
    print(f"\n  {'-' * 64}")
    print(f"  {len(approved)} approved, {len(rejected)} rejected.  "
          f"Total new risk ${total_risk:,.2f} "
          f"({total_risk / ctx['equity'] * 100:.2f}% of equity)")

    if not submit:
        print("\n  Dry run. Re-run with `submit --confirm` to send these.\n")
        return
    if not args.confirm:
        print("\n  Add --confirm to actually submit.\n")
        return

    clock = get_clock()
    if not clock.get("is_open"):
        print(f"\n  ! Market is closed. Next open: {clock.get('next_open')}")
        print("    Orders will queue. Market orders will fill at the next open.")

    print()
    for p in approved:
        order_body = build_order(p, cfg["time_in_force"])
        play_id = uuid.uuid4().hex[:8]
        try:
            resp = api("POST", "/v2/orders", json=order_body)
        except RuntimeError as e:
            print(f"  x {p['symbol']} REJECTED BY ALPACA: {e}")
            continue
        raw = p["raw"]
        append_journal({
            "play_id": play_id,
            "logged_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "session_date": session_date,
            "ticker": p["symbol"], "direction": p["direction"],
            "entry_type": p["entry_type"], "entry_planned": p["entry"],
            "stop": p["stop"], "target": p["target"], "qty": p["qty"],
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
        })
        print(f"  > {p['symbol']} {p['direction']} x{p['qty']} "
              f"submitted [{resp.get('status')}]  id={resp.get('id', '')[:8]}")
    print(f"\n  Logged to {JOURNAL.name}\n")


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


def cmd_reconcile(args):
    rows = read_journal()
    if not rows:
        print("Journal is empty.")
        return
    updated = 0
    for row in rows:
        if row.get("r_multiple") not in ("", None):
            continue  # already closed out
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
        if not entry_fill:
            continue
        entry_fill = float(entry_fill)
        row["entry_fill"] = round(entry_fill, 4)

        exit_fill, exit_reason, closed_at = None, None, None
        for leg in order.get("legs") or []:
            if leg.get("status") == "filled" and leg.get("filled_avg_price"):
                exit_fill = float(leg["filled_avg_price"])
                exit_reason = "target" if leg.get("type") == "limit" else "stop"
                closed_at = leg.get("filled_at", "")
        if exit_fill is None:
            continue

        qty = int(float(row["qty"]))
        stop = float(row["stop"])
        if row["direction"] == "long":
            pnl = (exit_fill - entry_fill) * qty
            denom = entry_fill - stop
        else:
            pnl = (entry_fill - exit_fill) * qty
            denom = stop - entry_fill
        r = (pnl / qty / denom) if denom else 0.0

        row.update({
            "exit_fill": round(exit_fill, 4),
            "exit_reason": exit_reason,
            "pnl_usd": round(pnl, 2),
            "r_multiple": round(r, 3),
            "hit_target_first": "1" if exit_reason == "target" else "0",
            "closed_at": closed_at or "",
        })
        updated += 1
        print(f"  closed {row['ticker']:<6} {exit_reason:<7} "
              f"{r:+.2f}R  ${pnl:+,.2f}")

    write_journal(rows)
    print(f"\n  {updated} trade(s) closed out. Journal updated.")
    if updated:
        print("  Fill in `thesis_verdict` by hand: right/wrong thesis vs right/wrong outcome.\n")


def cmd_score(args):
    rows = [r for r in read_journal() if r.get("r_multiple") not in ("", None)]
    if not rows:
        print("No closed trades yet. Run `reconcile` first.")
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
    scored = [r for r in rows if r.get("p_target_first") not in ("", None)
              and r.get("hit_target_first") not in ("", None)]
    if scored:
        print(f"\n  {'-' * 64}")
        print(f"  CALIBRATION   {len(scored)} trades with a stated probability")
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

    verdicts = [r.get("thesis_verdict", "").strip().lower() for r in rows]
    lucky = sum(1 for v in verdicts if v in ("wrong thesis right outcome", "lucky"))
    if lucky:
        print(f"\n  ! {lucky} trade(s) marked wrong-thesis/right-outcome. "
              f"These are the dangerous ones.")
    if not any(verdicts):
        print(f"\n  Note: thesis_verdict column is empty. Fill it in to separate "
              f"skill from luck.")
    print()


def cmd_calendar(args):
    """Exit 0 if today is a US trading day, 1 if not. For CI guards."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    days = api("GET", "/v2/calendar", params={"start": today, "end": today})
    if days:
        d = days[0]
        print(f"{today} is a trading day (open {d.get('open')} "
              f"close {d.get('close')} ET)")
        sys.exit(0)
    print(f"{today} is not a US trading day - standing down.")
    sys.exit(1)


def cmd_prep(args):
    """Markdown block of current book state, to paste into the brief request."""
    cfg = load_config()
    acct = get_account()
    positions = get_positions()
    equity = float(acct["equity"])
    last_equity = float(acct.get("last_equity") or equity)
    daily_pnl_pct = ((equity - last_equity) / last_equity * 100) if last_equity else 0
    gross = sum(abs(float(p["market_value"])) for p in positions)
    net = sum(float(p["market_value"]) for p in positions)

    journal = read_journal()
    by_symbol = {}
    for r in journal:
        if r.get("r_multiple") in ("", None):
            by_symbol[r["ticker"]] = r

    out = []
    out.append(f"## Current book state")
    out.append(f"*Auto-generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC. "
               f"These are live figures - use them, do not estimate.*\n")
    out.append(f"- Equity: **${equity:,.2f}**")
    out.append(f"- Cash: ${float(acct['cash']):,.2f}")
    out.append(f"- Session P&L so far: {daily_pnl_pct:+.2f}% "
               f"(kill switch at -{cfg['daily_loss_limit_pct']}%)")
    out.append(f"- Gross exposure: ${gross:,.0f} ({gross / equity * 100:.0f}% of equity, "
               f"cap {cfg['max_gross_exposure_pct']}%)")
    out.append(f"- Net exposure: ${net:+,.0f} ({net / equity * 100:+.0f}%)")
    out.append(f"- Open positions: {len(positions)} of {cfg['max_positions']} "
               f"— you may open at most {max(0, cfg['max_positions'] - len(positions))} more")

    if positions:
        out.append(f"\n### Open positions\n")
        out.append("| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        for p in positions:
            j = by_symbol.get(p["symbol"], {})
            thesis = (j.get("thesis") or "-").replace("|", "/")[:120]
            out.append(
                f"| {p['symbol']} | {p['side']} | {abs(int(float(p['qty'])))} "
                f"| {float(p['avg_entry_price']):.2f} | {float(p['current_price']):.2f} "
                f"| {float(p['unrealized_pl']):+,.0f} ({float(p['unrealized_plpc']) * 100:+.1f}%) "
                f"| {j.get('stop', '-')} | {j.get('target', '-')} | {thesis} |"
            )
    else:
        out.append(f"\n*No open positions.*")

    closed = [r for r in journal if r.get("r_multiple") not in ("", None)]
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

    text = "\n".join(out) + "\n"
    if args.out:
        Path(args.out).write_text(text)
        print(f"Wrote book state to {args.out}")
    else:
        print(text)


def cmd_stale(args):
    orders = api("GET", "/v2/orders", params={"status": "open", "nested": "true"})
    unfilled = [o for o in orders if o.get("filled_qty") in ("0", 0, None)
                and not o.get("parent_id")]

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
    p.set_defaults(func=cmd_submit)

    p = sub.add_parser("status", help="account, exposure, positions, loss-limit room")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("reconcile", help="pull fills and close out journal rows")
    p.set_defaults(func=cmd_reconcile)

    p = sub.add_parser("score", help="performance and calibration report")
    p.set_defaults(func=cmd_score)

    p = sub.add_parser("calendar", help="exit 0 if today is a US trading day, else 1")
    p.set_defaults(func=cmd_calendar)

    p = sub.add_parser("prep", help="markdown book state for the brief request")
    p.add_argument("--out", help="write to this file instead of stdout")
    p.set_defaults(func=cmd_prep)

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