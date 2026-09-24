"""An in-memory Alpaca for the tests.

Shaped after what the live paper API actually returned, including the parts
that broke the desk in September 2026:

- Timestamps carry nanosecond fractions (2026-09-24T12:59:58.123456789Z).
  parse_ts once read the offset's digits as part of the fraction and returned
  naive datetimes, which crashed both sessions on 2026-09-24.
- A filled bracket's stop leg is "held" and missing from the open-orders list;
  only the take-profit comes back. The book read "no live order" for stops
  that were in place (DAL 2026-09-22, BAC 2026-09-24).
- A stop entry the price has already crossed is refused with a 422 (BAC
  2026-09-23).
- Replacing an order with unchanged parameters is a 422 (DAL 2026-09-22).
- SIP data is refused when it is less than 15 minutes old.
- /v2beta1/stocks/snapshots does not exist; desk.py falls back to /v2.
"""

from __future__ import annotations

import copy
import itertools
import json
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

# Top-level orders the open-orders list returns. "held" is absent on purpose.
OPEN_VISIBLE = {"new", "accepted", "pending_new", "partially_filled"}
TERMINAL = {"filled", "canceled", "expired", "replaced", "rejected"}


def ts(dt: datetime) -> str:
    """Alpaca-style UTC timestamp with a nanosecond fraction."""
    dt = dt.astimezone(timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%S.") + f"{dt.microsecond:06d}789Z"


def et(day: str, hhmm: str) -> datetime:
    h, m = map(int, hhmm.split(":"))
    return datetime.fromisoformat(day).replace(hour=h, minute=m, tzinfo=ET).astimezone(timezone.utc)


def bar(t: datetime, o, h, l, c, v=1000) -> dict:
    return {"t": t.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "o": o, "h": h, "l": l, "c": c, "v": v}


def http_error(method, path, code, body) -> RuntimeError:
    # The same shape desk.api raises for a 4xx, with Alpaca's compact JSON:
    # {"code":42210000,"market_price":"55.885",...}
    return RuntimeError(f"{method} {path} -> {code}: {json.dumps(body, separators=(',', ':'))}")


class FakeAlpaca:
    def __init__(self, now: datetime, equity: float = 100_000.0,
                 last_equity: float | None = None):
        self.now = now
        self.equity = equity
        self.last_equity = equity if last_equity is None else last_equity
        self.cash = equity
        self.positions: list[dict] = []
        self.orders: list[dict] = []      # top-level orders; legs nested
        self.prices: dict[str, float] = {}     # symbol -> current price
        self.trade_time: dict[str, datetime] = {}  # symbol -> latest trade time
        self.daily: dict[str, dict] = {}        # symbol -> today's o/h/l
        self.bars: dict[tuple[str, str], list[dict]] = {}
        self.movers = {"gainers": [], "losers": [], "last_updated": None}
        self.not_shortable: set[str] = set()
        self.refuse: dict[str, str] = {}   # symbol -> message for POST /v2/orders
        self.no_sip = False
        self.page_size = 1000
        self.open_time, self.close_time = "09:30", "16:00"
        self.calls: list[tuple] = []
        self._ids = itertools.count(1)

    # -- building state ------------------------------------------------------
    def new_id(self) -> str:
        return f"ord-{next(self._ids):04d}"

    def order(self, symbol, side, otype, qty, *, status="new", limit=None, stop=None,
              filled_qty=0, fill=None, submitted=None, filled_at=None,
              order_class="simple", legs=None, oid=None) -> dict:
        return {
            "id": oid or self.new_id(), "symbol": symbol, "side": side, "type": otype,
            "qty": str(qty), "status": status,
            "limit_price": None if limit is None else str(limit),
            "stop_price": None if stop is None else str(stop),
            "filled_qty": str(filled_qty),
            "filled_avg_price": None if fill is None else str(fill),
            "submitted_at": ts(submitted or self.now),
            "filled_at": ts(filled_at) if filled_at else None,
            "order_class": order_class, "legs": legs,
        }

    def bracket(self, symbol, direction, entry_type, qty, entry, stop, target, *,
                fill=None, filled_at=None, submitted=None, oid=None) -> dict:
        """A bracket as Alpaca holds it: legs held until the entry fills, then
        the take-profit works and the stop leg stays held."""
        side, exit_side = ("buy", "sell") if direction == "long" else ("sell", "buy")
        filled = fill is not None
        parent = self.order(
            symbol, side, entry_type, qty, status="filled" if filled else "new",
            limit=entry if entry_type == "limit" else None,
            stop=entry if entry_type == "stop" else None,
            filled_qty=qty if filled else 0, fill=fill, submitted=submitted,
            filled_at=filled_at, order_class="bracket", oid=oid)
        parent["legs"] = [
            self.order(symbol, exit_side, "limit", qty, status="new" if filled else "held",
                       limit=target, submitted=submitted, order_class="bracket"),
            self.order(symbol, exit_side, "stop", qty, status="held",
                       stop=stop, submitted=submitted, order_class="bracket"),
        ]
        self.orders.append(parent)
        return parent

    def position(self, symbol, qty, avg, price):
        qty = float(qty)
        self.positions.append({
            "symbol": symbol, "qty": str(int(qty)), "side": "long" if qty > 0 else "short",
            "avg_entry_price": str(avg), "current_price": str(price),
            "market_value": str(round(qty * price, 2)),
            "unrealized_pl": str(round(qty * (price - avg), 2)),
            "unrealized_plpc": str(round((price - avg) / avg * (1 if qty > 0 else -1), 4)),
        })
        self.prices[symbol] = price

    def daily_history(self, symbol, closes: list[float], days: int = 70, vol=5_000_000):
        """Completed daily bars ending yesterday, one per weekday."""
        today = self.now.astimezone(ET).date()
        dates, d = [], today - timedelta(days=1)
        while len(dates) < days:
            if d.weekday() < 5:
                dates.append(d)
            d -= timedelta(days=1)
        dates.reverse()
        closes = (closes * days)[-days:] if len(closes) < days else closes[-days:]
        self.bars[("1Day", symbol)] = [
            bar(datetime.combine(dd, datetime.min.time(), ET), c, c * 1.01, c * 0.99, c, vol)
            for dd, c in zip(dates, closes)]

    # -- routing -------------------------------------------------------------
    def flat(self):
        for o in self.orders:
            yield o
            yield from o.get("legs") or []

    def find(self, oid):
        return next((o for o in self.flat() if o["id"] == oid), None)

    def __call__(self, method, path, base=None, **kw):
        params = dict(kw.get("params") or {})
        body = kw.get("json")
        self.calls.append((method, path, params, body))

        if path == "/v2/account":
            return {"equity": str(self.equity), "last_equity": str(self.last_equity),
                    "cash": str(self.cash)}
        if path == "/v2/positions" and method == "GET":
            return copy.deepcopy(self.positions)
        if path.startswith("/v2/positions/") and method == "DELETE":
            return self.close_position(path.rsplit("/", 1)[1])
        if path == "/v2/clock":
            day = self.calendar_day(self.now.astimezone(ET).date())
            is_open = bool(day) and day[0] <= self.now < day[1]
            return {"is_open": is_open, "next_open": "2026-09-25T09:30:00-04:00"}
        if path == "/v2/calendar":
            return self.calendar(params["start"], params["end"])
        if path.startswith("/v2/assets/"):
            sym = path.rsplit("/", 1)[1]
            return {"symbol": sym, "tradable": True,
                    "shortable": sym not in self.not_shortable, "easy_to_borrow": True}
        if path == "/v2beta1/stocks/snapshots":
            raise http_error(method, path, 404, {"message": "Not Found"})
        if path == "/v2/stocks/snapshots":
            return self.snapshots(params["symbols"].split(","))
        if path == "/v2/stocks/bars":
            return self.get_bars(method, path, params)
        if path == "/v1beta1/screener/stocks/movers":
            return copy.deepcopy(self.movers)
        if path == "/v2/orders" and method == "GET":
            return self.list_orders(params)
        if path == "/v2/orders" and method == "POST":
            return self.post_order(method, path, body)
        if path.startswith("/v2/orders/"):
            oid = path.rsplit("/", 1)[1]
            o = self.find(oid)
            if o is None:
                raise http_error(method, path, 404, {"message": "order not found"})
            if method == "GET":
                return copy.deepcopy(o)
            if method == "PATCH":
                return self.patch_order(method, path, o, body)
            if method == "DELETE":
                self.cancel_group(o)
                return {}
        raise AssertionError(f"FakeAlpaca has no route for {method} {path} {params}")

    # -- endpoints -----------------------------------------------------------
    def calendar_day(self, d: date):
        if d.weekday() >= 5:
            return None
        return et(d.isoformat(), self.open_time), et(d.isoformat(), self.close_time)

    def calendar(self, start, end):
        d, last, out = date.fromisoformat(start[:10]), date.fromisoformat(end[:10]), []
        while d <= last:
            if d.weekday() < 5:
                out.append({"date": d.isoformat(), "open": self.open_time,
                            "close": self.close_time})
            d += timedelta(days=1)
        return out

    def snapshots(self, symbols):
        out = {}
        for s in symbols:
            if s not in self.prices:
                continue
            snap = {"latestTrade": {"t": ts(self.trade_time.get(s, self.now)),
                                    "p": self.prices[s]}}
            if s in self.daily:
                d = self.daily[s]
                day = self.now.astimezone(ET).date()
                snap["dailyBar"] = {"t": f"{day.isoformat()}T04:00:00Z", **d, "c": self.prices[s]}
            out[s] = snap
        return out

    def get_bars(self, method, path, params):
        start = datetime.fromisoformat(params["start"].replace("Z", "+00:00")) \
            if "T" in params["start"] else datetime.fromisoformat(params["start"]).replace(tzinfo=timezone.utc)
        end = datetime.fromisoformat(params["end"].replace("Z", "+00:00")) if params.get("end") else self.now
        if params.get("feed") == "sip" and (self.no_sip or end > self.now - timedelta(minutes=15)):
            raise http_error(method, path, 403,
                             {"message": "subscription does not permit querying recent SIP data"})
        items = []
        for sym in params["symbols"].split(","):
            for b in self.bars.get((params["timeframe"], sym), []):
                t = datetime.fromisoformat(b["t"].replace("Z", "+00:00"))
                if start <= t < end:
                    items.append((sym, b))
        offset = int(params.get("page_token") or 0)
        page = items[offset:offset + self.page_size]
        out: dict[str, list] = {}
        for sym, b in page:
            out.setdefault(sym, []).append(b)
        more = offset + self.page_size < len(items)
        return {"bars": out, "next_page_token": str(offset + self.page_size) if more else None}

    def list_orders(self, params):
        status = params.get("status", "open")
        syms = set(filter(None, (params.get("symbols") or "").split(",")))
        after = params.get("after")
        after = datetime.fromisoformat(after.replace("Z", "+00:00")) if after else None

        def wanted(o, open_list):
            if syms and o["symbol"] not in syms:
                return False
            if open_list and o["status"] not in OPEN_VISIBLE:
                return False
            if not open_list and o["status"] not in TERMINAL:
                return False
            if after and datetime.fromisoformat(o["submitted_at"][:19] + "+00:00") <= after:
                return False
            return True

        if status == "open":
            out = []
            for o in self.orders:
                if wanted(o, True):
                    out.append(copy.deepcopy(o))  # legs nested, held ones included
                else:
                    # parent done: legs come back on their own - but not held ones
                    out += [copy.deepcopy(l) for l in o.get("legs") or [] if wanted(l, True)]
            return out
        # Closed orders come back flat: each leg as an order of its own.
        return [copy.deepcopy({**o, "legs": None}) for o in self.flat() if wanted(o, False)]

    def post_order(self, method, path, body):
        sym = body["symbol"]
        if sym in self.refuse:
            raise http_error(method, path, 422, {"code": 42210000, "message": self.refuse[sym]})
        price = self.prices.get(sym)
        if body["type"] == "stop" and body.get("order_class") != "oco" and price is not None:
            stop = float(body["stop_price"])
            if body["side"] == "sell" and stop >= price:
                raise http_error(method, path, 422, {
                    "code": 42210000, "market_price": str(price),
                    "message": "stop price must be less than current price",
                    "stop_price": body["stop_price"]})
            if body["side"] == "buy" and stop <= price:
                raise http_error(method, path, 422, {
                    "code": 42210000, "market_price": str(price),
                    "message": "stop price must be greater than current price",
                    "stop_price": body["stop_price"]})
        qty = int(body["qty"])
        if body.get("order_class") == "bracket":
            direction = "long" if body["side"] == "buy" else "short"
            entry = body.get("limit_price") or body.get("stop_price")
            o = self.bracket(sym, direction, body["type"], qty, entry,
                             body["stop_loss"]["stop_price"], body["take_profit"]["limit_price"])
        elif body.get("order_class") == "oco":
            o = self.order(sym, body["side"], "limit", qty, limit=body["take_profit"]["limit_price"],
                           order_class="oco")
            o["legs"] = [self.order(sym, body["side"], "stop", qty, status="held",
                                    stop=body["stop_loss"]["stop_price"], order_class="oco")]
            self.orders.append(o)
        else:
            o = self.order(sym, body["side"], body["type"], qty, limit=body.get("limit_price"),
                           stop=body.get("stop_price"))
            self.orders.append(o)
        out = copy.deepcopy(o)
        out["status"] = "pending_new" if o["status"] == "new" else o["status"]
        return out

    def patch_order(self, method, path, o, body):
        field, value = next(iter(body.items()))
        if o.get(field) is not None and abs(float(o[field]) - float(value)) < 0.005:
            raise http_error(method, path, 422, {"code": 42210000,
                                                 "message": "order parameters are not changed"})
        o[field] = value
        return {**copy.deepcopy(o), "status": "replaced"}

    def cancel_group(self, o):
        # "If any one of the orders is canceled, any remaining open order in the
        # group is canceled." A group is a parent and its legs.
        for parent in self.orders:
            group = [parent] + list(parent.get("legs") or [])
            if any(x["id"] == o["id"] for x in group):
                for x in group:
                    if x["status"] not in TERMINAL:
                        x["status"] = "canceled"
                return
        o["status"] = "canceled"

    def close_position(self, sym):
        pos = next(p for p in self.positions if p["symbol"] == sym)
        self.positions.remove(pos)
        qty = abs(int(float(pos["qty"])))
        side = "sell" if float(pos["qty"]) > 0 else "buy"
        o = self.order(sym, side, "market", qty, status="filled", filled_qty=qty,
                       fill=self.prices[sym], filled_at=self.now)
        self.orders.append(o)
        return {**copy.deepcopy(o), "status": "accepted"}
