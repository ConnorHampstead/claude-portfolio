"""check / submit: validation, sizing, admission, submission, the shadow book."""

import json
import unittest
from datetime import timedelta
from types import SimpleNamespace
from unittest import mock

from tests.support import CONFIG, DeskCase, desk


def play(ticker, direction="long", entry=100.0, stop=98.0, target=104.0, **kw):
    p = {"ticker": ticker, "direction": direction, "entry_type": "limit", "entry": entry,
         "stop": stop, "targets": [target], "conviction": 3, "p_target_first": 0.45}
    p.update(kw)
    return p


class Check(DeskCase):
    def setUp(self):
        super().setUp()
        for sym, px in {"AAA": 100.0, "BBB": 50.0, "CCC": 200.0, "DDD": 100.0,
                        "EEE": 100.0, "XHB": 95.5}.items():
            self.fake.prices[sym] = px

    def test_nanosecond_snapshots_with_the_delayed_tape(self):
        """The 2026-09-24 crash: a snapshot trade time with a nanosecond
        fraction compared against the delayed consolidated bar's time."""
        self.fake.trade_time["AAA"] = self.NOW - timedelta(minutes=2)
        self.fake.bars[("5Min", "AAA")] = [
            {"t": (self.NOW - timedelta(minutes=40)).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "o": 99, "h": 100, "l": 99, "c": 99.5, "v": 1}]
        out, code = self.check({"plays": [play("AAA")]})
        self.assertEqual(code, 0, out)
        self.assertIn("SESSION", out)

    def test_delayed_tape_is_the_reference_when_iex_is_stale(self):
        """Pre-market IEX can be yesterday's print. The consolidated tape as of
        15 minutes ago should be what a crossed stop trigger is judged by."""
        self.fake.trade_time["BBB"] = self.NOW - timedelta(days=1)
        self.fake.prices["BBB"] = 56.20
        self.fake.bars[("5Min", "BBB")] = [
            {"t": (self.NOW - timedelta(minutes=25)).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "o": 55.95, "h": 55.96, "l": 55.85, "c": 55.88, "v": 1}]
        out, _ = self.check({"plays": [play("BBB", "short", 55.90, 57.70, 52.90,
                                            entry_type="stop", risk_pct=0.5)]})
        self.assertIn("already above the last price 55.88", out)

    def test_risk_tiers_size_the_play(self):
        out, _ = self.check({"plays": [
            play("AAA", risk_pct=0.5), play("BBB", entry=50, stop=49, target=53, risk_pct=0.25),
            play("CCC", entry=200, stop=190, target=230, risk_pct=2.0)]})
        self.assertIn("qty 250  notional $25,000  risk $500.00", out)      # 0.5% / $2
        self.assertIn("qty 250  notional $12,500  risk $250.00", out)      # 0.25% / $1
        self.assertIn("risk_pct 2.0 is over the 1.0% per-trade cap", out)  # cut to 1%
        self.assertIn("qty 100  notional $20,000  risk $1,000.00", out)

    def test_bad_inputs_are_rejected_not_crashes(self):
        out, code = self.check({"plays": [
            play("AAA", conviction="high"), play("BBB", entry=50, stop=51, target=53),
            play("CCC", risk_pct=0.01)]})
        self.assertEqual(code, 0)
        self.assertIn("conviction must be a number", out)
        self.assertIn("long stop 51.0 must be below entry 50.0", out)
        self.assertIn("below the 0.1% floor", out)

    def test_not_shortable(self):
        self.fake.not_shortable.add("XHB")
        out, _ = self.check({"plays": [play("XHB", "short", 95.1, 98.7, 89.8)]})
        self.assertIn("XHB is not shortable", out)

    def test_market_entry_sized_from_the_last_price(self):
        out, _ = self.check({"plays": [play("AAA", entry=95, stop=96, target=110,
                                            entry_type="market")]})
        self.assertIn("market entry sized from the last price 100.00", out)
        self.assertIn("entry 100.00 (market)  stop 96.00", out)

    def test_admission_by_conviction_against_the_caps(self):
        # Each is a 50%-of-equity long; net caps at 100%, so only two fit, and
        # the highest conviction two get in whatever order the brief lists them.
        out, _ = self.check({"plays": [
            play("AAA", conviction=2), play("DDD", conviction=5), play("EEE", conviction=4),
            play("BBB", entry=50, stop=49.5, target=52, risk_pct=0.25, conviction=1)]})
        adm = out[out.index("BOOK-LEVEL ADMISSION"):]
        self.assertLess(adm.index("+ DDD"), adm.index("+ EEE"))
        self.assertIn("x AAA    dropped: net exposure would be +150%", adm)
        # A smaller play behind a dropped one still gets its own check.
        self.assertIn("x BBB    dropped: net exposure would be +125%", adm)

    def test_held_and_resting_names_cannot_be_stacked(self):
        self.fake.position("AAA", 100, 95, 100)
        self.fake.bracket("DDD", "long", "stop", 50, 105, 100, 115)
        out, _ = self.check({"plays": [play("AAA"), play("DDD")]})
        self.assertIn("AAA    dropped: already held", out)
        self.assertIn("DDD    dropped: already has a resting entry", out)

    def test_resting_entries_count_toward_the_caps(self):
        self.fake.bracket("DDD", "long", "stop", 500, 105, 104, 115)  # 52.5% notional
        out, _ = self.check({"plays": [play("AAA")]})
        self.assertIn("book now: 1 positions/resting entries, gross 52%", out)
        self.assertIn("x AAA    dropped: net exposure would be +102%", out)

    def test_daily_loss_limit_blocks_every_new_play(self):
        self.fake.equity, self.fake.last_equity = 96_900, 100_000
        out, _ = self.check({"plays": [play("AAA")]})
        self.assertIn("DAILY LOSS LIMIT HIT", out)
        self.assertIn("0 approved", out)

    def test_states_what_the_plays_own_numbers_are_worth(self):
        out, _ = self.check({"plays": [play("AAA")]})   # 45% of +2R against 55% of -1R
        self.assertIn("stated EV +0.35R   (breakeven P at 2.00R is 33%)", out)

    def test_rule_8_from_the_briefs_own_earnings_date(self):
        """Today is 2026-09-24. The rule was in the prompt and nowhere else."""
        out, _ = self.check({"plays": [
            play("AAA", earnings_date="2026-09-28"),
            play("BBB", entry=50, stop=49, target=53, earnings_date="2026-09-28",
                 event_trade=True),
            play("CCC", entry=200, stop=196, target=212, earnings_date="2026-09-28",
                 event_trade=True, risk_pct=0.5),
            play("DDD", earnings_date="2026-11-05"), play("EEE", earnings_date=None),
            play("XHB", entry=95.5, stop=93.5, target=99.5)]})
        blocks = {b.split()[1]: b for b in out.split("\n  [")[1:]}
        self.assertIn("REJECTED] AAA", out)
        self.assertIn("AAA reports on 2026-09-28, 4 day(s) away - rule 8", blocks["AAA"])
        self.assertIn("event trade into BBB's earnings must be risk_pct 0.5 or less", blocks["BBB"])
        self.assertIn("! event trade: CCC reports on 2026-09-28", blocks["CCC"])
        for sym in ("DDD", "EEE"):
            self.assertTrue(blocks[sym].startswith("OK]"), blocks[sym])
            self.assertNotIn("rule 8", blocks[sym])
        self.assertIn("no earnings_date given - rule 8 was not checked", blocks["XHB"])

    def test_the_universe_floor(self):
        self.fake.prices["PENNY"] = 3.0
        self.fake.daily_history("THIN", [100.0], vol=50_000)
        self.fake.prices["THIN"] = 100.0
        out, _ = self.check({"plays": [play("PENNY", entry=3.0, stop=2.9, target=3.3),
                                       play("THIN")]})
        self.assertIn("PENNY trades at 3.00, under the $5 floor", out)
        self.assertIn("THIN averages 0.05M shares a day, under the 1M floor", out)


class Submit(DeskCase):
    def setUp(self):
        super().setUp()
        for sym, px in {"AAA": 100.0, "BBB": 55.885, "CCC": 200.0, "EEE": 100.0}.items():
            self.fake.prices[sym] = px

    def test_orders_journal_and_shadow(self):
        out, code = self.submit({"plays": [
            play("AAA"), play("EEE", conviction=2),                    # 50% each: net 100%
            play("CCC", entry=200, stop=196, target=212, conviction=1)],  # dropped: net cap
            "passed": [
                {"ticker": "BBB", "direction": "short", "entry_type": "stop", "entry": 55.5,
                 "stop": 57.0, "targets": [52.0], "p_target_first": 0.4, "reason": "location"},
                {"ticker": "BBB", "direction": "short", "entry": 80, "stop": 82,
                 "targets": [75], "reason": "stale level"}]},
            session="open", model="claude-opus-5-5")
        self.assertEqual(code, 0, out)
        bodies = self.post_bodies()
        self.assertEqual([b["symbol"] for b in bodies], ["AAA", "EEE"])
        self.assertEqual((bodies[0]["order_class"], bodies[0]["qty"]), ("bracket", "500"))
        aaa = self.journal()["AAA"]
        self.assertEqual((aaa["stop_initial"], aaa["target_initial"], aaa["session"],
                          aaa["model"]), ("98.0", "104.0", "open", "claude-opus-5-5"))
        shadow = {(r["ticker"], r["source"]) for r in self.shadow()}
        self.assertEqual(shadow, {("CCC", "dropped"), ("BBB", "passed")})
        self.assertIn("not a real level", out)

    def test_crossed_stop_entry_is_not_placed_and_does_not_fail_the_run(self):
        """BAC 2026-09-23: a sell stop at 55.90 with pre-market at 55.885."""
        out, code = self.submit({"plays": [
            play("BBB", "short", 55.90, 57.70, 52.90, entry_type="stop", risk_pct=0.5),
            play("AAA")]})
        self.assertEqual(code, 0, out)
        self.assertIn("BBB stop entry 55.90 not placed: the market (55.885) had already "
                      "crossed the trigger", out)
        self.assertEqual([b["symbol"] for b in self.post_bodies()], ["BBB", "AAA"])
        self.assertNotIn("BBB", self.journal())
        self.assertEqual([(r["ticker"], r["source"]) for r in self.shadow()],
                         [("BBB", "not placed")])

    def test_any_other_rejection_fails_the_run(self):
        self.fake.refuse["AAA"] = "insufficient buying power"
        out, code = self.submit({"plays": [play("AAA")]})
        self.assertEqual(code, 1)
        self.assertIn("THE BOOK DOES NOT MATCH THE BRIEF", out)

    def test_no_trade_day_still_logs_passes_and_manages(self):
        out, code = self.submit({"no_trade": True, "plays": [play("AAA")], "passed": [
            {"ticker": "AAA", "direction": "long", "entry": 97, "stop": 95, "targets": [101]}]})
        self.assertEqual(code, 0, out)
        self.assertEqual(self.post_bodies(), [])
        self.assertEqual(len(self.shadow()), 1)

    def test_check_never_sends(self):
        out, _ = self.check({"plays": [play("AAA")]})
        self.assertEqual(self.post_bodies(), [])
        self.assertIn("Validation only - `check` never sends.", out)
        self.assertNotIn("Dry run", out)
        self.assertEqual(self.shadow(), [])

    def test_under_the_conviction_floor_is_scored_not_placed(self):
        (self.tmp / "config.json").write_text(json.dumps({**CONFIG, "min_conviction": 3}))
        out, code = self.submit({"plays": [play("AAA", conviction=2), play("EEE")]})
        self.assertEqual(code, 0, out)
        self.assertIn("x AAA    dropped: conviction 2 is under the 3 needed to trade", out)
        self.assertEqual([b["symbol"] for b in self.post_bodies()], ["EEE"])
        (row,) = self.shadow()
        self.assertEqual((row["ticker"], row["source"], row["p_target_first"]),
                         ("AAA", "dropped", "0.45"))

    def test_one_shadow_row_per_idea_per_day(self):
        """The review re-lists what the morning passed on; 25 of the first 114
        shadow rows were the same idea counted twice."""
        xle = {"ticker": "CCC", "direction": "short", "entry": 201, "stop": 205,
               "targets": [193], "p_target_first": 0.4, "reason": "location"}
        self.submit({"plays": [play("AAA")], "passed": [xle]})
        out, _ = self.submit({"plays": [], "passed": [
            xle, {**xle, "direction": "long", "entry": 199, "stop": 195, "targets": [207]},
            {"ticker": "AAA", "direction": "long", "entry": 99, "stop": 97, "targets": [103]}]},
            session="open")
        self.assertIn(". CCC    short already logged or traded today - not counted twice", out)
        self.assertIn(". AAA    long  already logged or traded today", out)
        self.assertEqual([(r["ticker"], r["direction"], r["session"]) for r in self.shadow()],
                         [("CCC", "short", "pre-market"), ("CCC", "long", "open")])

    def test_a_pass_that_is_placed_later_the_same_day_is_a_trade(self):
        self.submit({"plays": [], "passed": [
            {"ticker": "AAA", "direction": "long", "entry": 99, "stop": 97, "targets": [103]},
            {"ticker": "CCC", "direction": "long", "entry": 199, "stop": 195, "targets": [207]}]})
        out, code = self.submit({"plays": [play("AAA")]}, session="open")
        self.assertEqual(code, 0, out)
        rows = {r["ticker"]: r for r in self.shadow()}
        self.assertEqual((rows["AAA"]["status"], rows["AAA"]["outcome"]), ("resolved", "taken"))
        self.assertEqual(rows["CCC"]["status"], "pending")
        self.assertEqual([r["ticker"] for r in desk.passes(self.shadow())], ["CCC"])

    def test_a_dry_run_scores_what_it_would_have_placed(self):
        """How a prompt or model change is tried before it trades."""
        doc = {"plays": [play("AAA")], "passed": [
            {"ticker": "CCC", "direction": "long", "entry": 199, "stop": 195, "targets": [207]}]}
        out, code = self.check(doc, log_shadow=True, session="open", model="new-model/high")
        self.assertEqual(code, 0, out)
        self.assertIn("Dry run: 2 idea(s) logged to the shadow book", out)
        self.assertEqual(self.post_bodies(), [])
        self.assertEqual([(r["ticker"], r["source"], r["model"]) for r in self.shadow()],
                         [("CCC", "dry run", "new-model/high"), ("AAA", "dry run", "new-model/high")])
        # The real session the same day is not deduplicated against the dry run.
        self.submit(doc)
        self.assertEqual([(r["ticker"], r["source"]) for r in self.shadow()][2:],
                         [("CCC", "passed")])
        self.assertEqual([r["ticker"] for r in desk.passes(self.shadow())], ["CCC"])
        self.check(doc, log_shadow=True)   # and a second dry run adds nothing
        self.assertEqual(len(self.shadow()), 3)


class ApiRetry(unittest.TestCase):
    """One timeout or 5xx on a read used to cost the whole session. A write
    is never repeated: a second POST could place the order twice."""

    def call(self, method, *replies):
        def reply(r):
            return r if isinstance(r, Exception) else SimpleNamespace(
                status_code=r, text="{}", json=lambda: {"status": r})
        with mock.patch.object(desk.requests, "request",
                               side_effect=[reply(r) for r in replies]) as request, \
                mock.patch.object(desk.time, "sleep"), \
                mock.patch.object(desk, "creds", return_value={}):
            try:
                return desk.api(method, "/v2/orders"), request.call_count
            except RuntimeError as e:
                return e, request.call_count

    def test_reads_are_retried(self):
        self.assertEqual(self.call("GET", 503, 200), ({"status": 200}, 2))
        self.assertEqual(self.call("GET", desk.requests.ConnectionError("reset"), 429, 200),
                         ({"status": 200}, 3))
        err, n = self.call("GET", 503, 503, 503)
        self.assertIsInstance(err, RuntimeError)
        self.assertEqual(n, 3)

    def test_a_refusal_is_not_a_retry(self):
        err, n = self.call("GET", 404, 200)
        self.assertIsInstance(err, RuntimeError)
        self.assertEqual(n, 1)

    def test_writes_are_sent_once(self):
        for method in ("POST", "PATCH", "DELETE"):
            err, n = self.call(method, 503, 200)
            self.assertIsInstance(err, RuntimeError, method)
            self.assertEqual(n, 1, method)


if __name__ == "__main__":
    unittest.main()
