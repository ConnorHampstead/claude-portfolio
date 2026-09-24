"""Exit legs and manage, and the book state prep writes for the brief."""

import unittest
from datetime import datetime, timedelta, timezone

from tests.support import POST_OPEN, DeskCase, desk
from tests.fake_alpaca import et


class HeldStopLeg(DeskCase):
    """A filled bracket's stop leg is held and missing from the open-orders
    list. BAC 2026-09-24 read "no live order" with its 57.70 stop in place,
    and both briefs that day tried to re-arm it."""

    def setUp(self):
        super().setUp()
        f = self.fake
        self.entry = f.bracket("BAC", "short", "stop", 267, 55.80, 57.70, 52.90, fill=55.80,
                               filled_at=self.NOW - timedelta(hours=20),
                               submitted=self.NOW - timedelta(hours=21))
        f.position("BAC", -267, 55.80, 56.20)
        self.journal_row(ticker="BAC", direction="short", entry_type="stop", entry_planned=55.8,
                         stop=57.7, target=52.9, qty=267, risk_usd=507.3,
                         order_id=self.entry["id"])

    def test_the_open_list_really_hides_it(self):
        legs = desk.exit_legs("BAC", "short", desk.get_open_orders())
        self.assertIsNotNone(legs["take_profit"])
        self.assertIsNone(legs["stop_loss"])

    def test_found_on_the_entry_order(self):
        legs = desk.exit_legs("BAC", "short", desk.get_open_orders(), self.entry["id"])
        self.assertEqual(desk.leg_price(legs["stop_loss"]), 57.70)

    def test_prep_shows_the_stop(self):
        out, _ = self.run_cmd(desk.cmd_prep, out=None)
        row = next(l for l in out.splitlines() if l.startswith("| BAC | short"))
        self.assertIn("| 57.70 | 52.90 |", row)
        self.assertNotIn("no live order", row)
        self.assertIn("Risk at stake (entry to stop): $507", out)

    def test_restating_the_stop_touches_nothing(self):
        out, code = self.submit({"no_trade": True, "plays": [], "manage": [
            {"ticker": "BAC", "action": "update", "stop": 57.70, "target": 52.90}]})
        self.assertEqual(code, 0, out)
        self.assertIn("stop   57.70 -> 57.70", out)
        self.assertIn("stop already at 57.70, left alone", out)
        self.assertEqual([c for c in self.fake.calls if c[0] in ("PATCH", "DELETE", "POST")], [])

    def test_moving_the_held_stop_replaces_it(self):
        out, code = self.submit({"plays": [], "manage": [
            {"ticker": "BAC", "action": "update", "stop": 57.00}]})
        self.assertEqual(code, 0, out)
        patches = [c for c in self.fake.calls if c[0] == "PATCH"]
        self.assertEqual(len(patches), 1)
        self.assertEqual(patches[0][3], {"stop_price": "57.00"})
        self.assertEqual(self.journal()["BAC"]["stop"], "57.0")
        self.assertEqual(self.journal()["BAC"]["stop_initial"], "57.7")

    def test_widening_past_the_risk_budget_is_rejected(self):
        out, _ = self.check({"plays": [], "manage": [
            {"ticker": "BAC", "action": "update", "stop": 60.00}]})
        self.assertIn("over the 1.0% per-trade cap", out)

    def test_close(self):
        out, code = self.submit({"plays": [], "manage": [{"ticker": "BAC", "action": "close"}]})
        self.assertEqual(code, 0, out)
        self.assertIn("close order sent x267", out)
        self.assertEqual(self.fake.positions, [])


class MissingProtection(DeskCase):
    """A position whose exits are really gone gets a fresh OCO pair, folding
    in the surviving leg rather than leaving two unlinked exits."""

    def test_new_oco_replaces_the_lone_survivor(self):
        f = self.fake
        entry = f.bracket("DAL", "long", "limit", 457, 80.4, 78.2, 84.9, fill=80.3846,
                          filled_at=self.NOW - timedelta(days=1))
        entry["legs"][1]["status"] = "canceled"  # the stop really is gone
        f.position("DAL", 457, 80.3846, 84.68)
        self.journal_row(ticker="DAL", direction="long", entry_planned=80.4, stop=78.2,
                         target=84.9, qty=457, risk_usd=1005.4, order_id=entry["id"])
        out, code = self.submit({"plays": [], "manage": [
            {"ticker": "DAL", "action": "update", "stop": 82.40, "target": 84.90}]})
        self.assertEqual(code, 0, out)
        self.assertIn("stop   none -> 82.40", out)
        self.assertIn("new OCO stop 82.40 / target 84.90", out)
        oco = [b for b in self.post_bodies("DAL") if b.get("order_class") == "oco"]
        self.assertEqual(len(oco), 1)


class Prep(DeskCase):
    def setUp(self):
        super().setUp()
        f = self.fake
        f.daily_history("SPY", [650.0 + i for i in range(70)])
        f.daily_history("BAC", [56.2])
        f.prices.update({"SPY": 720.0, "BAC": 56.2})

    def prep(self):
        out, code = self.run_cmd(desk.cmd_prep, out=None)
        self.assertEqual(code, 0, out)
        return out

    def test_clock_before_the_open(self):
        out = self.prep()
        self.assertIn("Time now: **09:07 ET** (13:07 UTC), Thursday 2026-09-24", out)
        self.assertIn("opens at 09:30 ET, in 23 min", out)
        self.assertIn("Anything scheduled before 09:07 ET today has already been released", out)

    def test_clock_after_the_open(self):
        self.freeze(POST_OPEN)
        self.assertIn("The cash session opened 36 min ago", self.prep())

    def test_record_and_last_trades(self):
        self.journal_row(ticker="LLY", direction="long", entry_planned=1165, stop=1230,
                         target=1300, stop_initial=1126, target_initial=1228, qty=25,
                         risk_usd=975, r_multiple=1.757, pnl_usd=1653.75, exit_reason="stop",
                         closed_at="2026-08-25T19:59:11Z")
        self.journal_row(ticker="ANET", direction="long", entry_planned=207, stop=193.2,
                         target=228, qty=72, risk_usd=993.6, r_multiple=-1.01, pnl_usd=-758.4,
                         exit_reason="stop", closed_at="2026-08-05T14:01:04Z")
        out = self.prep()
        self.assertIn("2 closed trades: 1W / 1L, total +0.75R, net $+895 realized", out)
        self.assertLess(out.index("| LLY |"), out.index("| ANET |"))

    def test_resting_entries_and_room(self):
        self.fake.bracket("AAPL", "long", "stop", 67, 346, 338.5, 358)
        out = self.prep()
        self.assertIn("| AAPL | long | 67 | 346.00 | stop | 338.50 | 358.00 |", out)
        self.assertIn("Slots: 0 open + 1 resting entries of 8", out)
        self.assertIn("A new long can be up to 50% of equity in notional", out)

    def test_unplaced_plays_are_shown_to_the_review(self):
        desk.append_shadow([{"shadow_id": "x", "logged_at": "2026-09-24T13:07:20+00:00",
                             "session_date": "2026-09-24", "session": "pre-market",
                             "source": "not placed", "ticker": "BAC", "direction": "short",
                             "entry_type": "stop", "entry": 55.9, "stop": 57.7, "target": 52.9,
                             "reason": "stop entry 55.90 not placed", "status": "pending"}])
        out = self.prep()
        self.assertIn("### Plays from earlier today that were not placed", out)
        self.assertIn("| BAC | short | stop 55.9 | 57.7 | 52.9 |", out)

    def test_market_table_prefers_the_newer_price_and_says_which(self):
        f = self.fake
        f.trade_time["BAC"] = self.NOW - timedelta(days=1)      # IEX: yesterday's print
        f.trade_time["SPY"] = self.NOW - timedelta(minutes=1)   # IEX: fresh
        for sym, px in (("BAC", 55.88), ("SPY", 700.0)):
            f.bars[("5Min", sym)] = [{"t": et("2026-09-24", "08:45").strftime("%Y-%m-%dT%H:%M:%SZ"),
                                      "o": px, "h": px, "l": px, "c": px, "v": 1}]
        self.journal_row(ticker="BAC", direction="short", entry_planned=55.8, stop=57.7,
                         target=52.9, qty=267, risk_usd=507.3, order_id="none")
        f.position("BAC", -267, 55.8, 56.2)
        out = self.prep()
        self.assertIn("| BAC | 55.88 (08:50 sip) | -0.6% | 56.20 |", out)
        self.assertIn("| SPY | 720.00 (09:06 iex) |", out)
        self.assertIn("(SIP, consolidated volume)", out)

    def test_falls_back_to_iex_without_sip(self):
        self.fake.no_sip = True
        out = self.prep()
        self.assertIn("(IEX, IEX volume only", out)
        self.assertIn("thin single-venue print", out)

    def test_movers_filtered_and_labelled_when_stale(self):
        f = self.fake
        for sym, px, vol in (("MOVR", 30.0, 5e6), ("THIN", 40.0, 5e4), ("PENNY", 3.0, 5e6)):
            f.daily_history(sym, [px], vol=vol)
            f.prices[sym] = px
        f.movers = {"gainers": [{"symbol": s, "price": p} for s, p in
                                (("MOVR", 36), ("THIN", 44), ("PENNY", 3.2), ("ABCDW", 9))],
                    "losers": [], "last_updated": "2026-09-23T23:59:00.123456789Z"}
        out = self.prep()
        movers = out[out.index("#### Movers"):]
        self.assertIn("PREVIOUS session's movers", movers)
        self.assertIn("| MOVR |", movers)
        for sym in ("THIN", "PENNY", "ABCDW"):
            self.assertNotIn(f"| {sym} |", movers)

    def test_market_data_failure_does_not_stop_the_brief(self):
        def broken(method, path, base=None, **kw):
            if path == "/v2/stocks/bars":
                raise RuntimeError("GET /v2/stocks/bars -> 500: {}")
            return fake(method, path, base, **kw)
        fake = self.fake
        desk.api = broken
        out = self.prep()
        self.assertIn("### Market data", out)
        self.assertIn("Unavailable this session", out)


if __name__ == "__main__":
    unittest.main()
