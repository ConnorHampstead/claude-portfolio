"""Timestamps, the journal migration, and reconcile."""

import shutil
import unittest
from datetime import datetime, timedelta, timezone

from tests.support import FIXTURES, DeskCase, desk


class ParseTs(unittest.TestCase):
    """2026-09-24: every Alpaca timestamp with a fraction parsed as naive, and
    the first naive/aware comparison crashed both sessions."""

    def test_formats_alpaca_returns(self):
        utc = timezone.utc
        cases = {
            "2026-09-24T12:59:58.123456789Z": datetime(2026, 9, 24, 12, 59, 58, 123456, utc),
            "2026-08-25T15:02:11.5Z": datetime(2026, 8, 25, 15, 2, 11, 500000, utc),
            "2026-09-24T12:45:00Z": datetime(2026, 9, 24, 12, 45, tzinfo=utc),
            "2026-09-23T13:21:34+00:00": datetime(2026, 9, 23, 13, 21, 34, tzinfo=utc),
            "2026-09-24T08:59:58.123-04:00": datetime(2026, 9, 24, 12, 59, 58, 123000, utc),
            "2026-09-24T12:59:58.123456": datetime(2026, 9, 24, 12, 59, 58, 123456, utc),
        }
        for text, want in cases.items():
            with self.subTest(text):
                got = desk.parse_ts(text)
                self.assertIsNotNone(got.tzinfo, "must be aware")
                self.assertEqual(got, want)

    def test_mixed_precision_compares(self):
        a = desk.parse_ts("2026-09-24T12:59:58.123456789Z")
        b = desk.parse_ts("2026-09-24T12:45:00Z")
        self.assertGreater(a, b)

    def test_garbage(self):
        self.assertIsNone(desk.parse_ts(""))
        self.assertIsNone(desk.parse_ts(None))
        self.assertIsNone(desk.parse_ts("not a time"))


class JournalMigration(DeskCase):
    def setUp(self):
        super().setUp()
        shutil.copy(FIXTURES / "journal-legacy.csv", desk.JOURNAL)

    def test_header_rewritten_and_initial_levels_backfilled(self):
        rows = self.journal()
        with open(desk.JOURNAL) as f:
            self.assertEqual(f.readline().strip().split(","), desk.JOURNAL_FIELDS)
        # From the brief, even though the live levels were moved since.
        self.assertEqual((rows["LLY"]["stop_initial"], rows["LLY"]["target_initial"]),
                         ("1126.0", "1228.0"))
        self.assertEqual(rows["LLY"]["stop"], "1230.0", "live stop left alone")
        # No brief for 2026-09-21 in the fixtures: stop derived from the sizing.
        self.assertEqual(rows["DAL"]["stop_initial"], "78.2")
        self.assertEqual(rows["DAL"]["target_initial"], "84.9")

    def test_append_after_migration_lands_in_the_right_columns(self):
        self.journal_row(ticker="AAPL", direction="long", entry_planned=346, stop=338.5,
                         target=358, qty=67, risk_usd=502.5, order_id="aapl-entry",
                         session="pre-market", model="claude-opus-5-5")
        aapl = self.journal()["AAPL"]
        self.assertEqual((aapl["stop_initial"], aapl["session"], aapl["model"]),
                         ("338.5", "pre-market", "claude-opus-5-5"))


class Reconcile(DeskCase):
    def setUp(self):
        super().setUp()
        shutil.copy(FIXTURES / "journal-legacy.csv", desk.JOURNAL)
        f = self.fake
        t = lambda s: datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
        # LLY: bracket filled 08-05; its legs cancelled; manage placed an OCO on
        # 08-21; the stop was replaced up to 1230 on 08-24 and filled 08-25.
        lly = f.bracket("LLY", "long", "limit", 25, 1165, 1126, 1228, fill=1163.64,
                        filled_at=t("2026-08-05T13:30:02"), submitted=t("2026-08-05T12:47:58"),
                        oid="lly-entry")
        for leg in lly["legs"]:
            leg["status"] = "canceled"
        oco = f.order("LLY", "sell", "limit", 25, status="canceled", limit=1300,
                      submitted=t("2026-08-21T13:09:00"), order_class="oco")
        oco["legs"] = [f.order("LLY", "sell", "stop", 25, status="replaced", stop=1200,
                               submitted=t("2026-08-21T13:09:00"), order_class="oco")]
        replacement = f.order("LLY", "sell", "stop", 25, status="filled", stop=1230,
                              filled_qty=25, fill=1229.76, submitted=t("2026-08-24T13:08:00"),
                              order_class="oco")
        replacement["filled_at"] = "2026-08-25T15:02:11Z"  # no fraction: mixed precision
        f.orders += [oco, replacement]
        # DAL: bracket filled 09-21, both legs gone, OCO 82.40 / 84.90 placed 09-22.
        dal = f.bracket("DAL", "long", "limit", 457, 80.4, 78.2, 84.9, fill=80.3846,
                        filled_at=t("2026-09-21T13:30:01"), submitted=t("2026-09-21T13:12:10"),
                        oid="dal-entry")
        for leg in dal["legs"]:
            leg["status"] = "canceled"
        self.dal_oco = f.order("DAL", "sell", "limit", 457, limit=84.9,
                               submitted=t("2026-09-22T14:39:00"), order_class="oco")
        self.dal_oco["legs"] = [f.order("DAL", "sell", "stop", 457, status="held", stop=82.4,
                                        submitted=t("2026-09-22T14:39:00"), order_class="oco")]
        f.orders.append(self.dal_oco)

    def reconcile(self):
        return self.run_cmd(desk.cmd_reconcile)

    def test_exit_through_a_replaced_oco_leg(self):
        """LLY's exit was never a leg of its bracket, and its live stop had
        been trailed above entry. It must close, at +1.76R, scored as having
        reached its initial target."""
        self.reconcile()
        lly = self.journal()["LLY"]
        self.assertEqual(lly["exit_reason"], "stop")
        self.assertAlmostEqual(float(lly["exit_fill"]), 1229.76)
        self.assertAlmostEqual(float(lly["r_multiple"]), 1.757, places=3)
        self.assertAlmostEqual(float(lly["pnl_usd"]), 1653.0, places=2)
        self.assertEqual(lly["hit_target_first"], "1")

    def test_open_trade_and_closed_trade_untouched(self):
        self.reconcile()
        rows = self.journal()
        self.assertEqual(rows["DAL"]["r_multiple"], "", "DAL's OCO has not filled")
        self.assertEqual(rows["ANET"]["r_multiple"], "-1.01")

    def test_trailed_stop_exit_is_not_scored_for_calibration(self):
        self.dal_oco["status"] = "canceled"
        leg = self.dal_oco["legs"][0]
        leg.update(status="filled", filled_qty="457", filled_avg_price="82.40",
                   filled_at="2026-09-23T13:30:04.918273645Z")
        out, _ = self.reconcile()
        dal = self.journal()["DAL"]
        self.assertAlmostEqual(float(dal["r_multiple"]), 0.923, places=3)  # vs the 78.20 stop
        self.assertEqual(dal["hit_target_first"], "")
        self.assertIn("not scored for calibration", out)

    def test_target_exit_after_moving_levels_is_scored(self):
        self.dal_oco.update(status="filled", filled_qty="457", filled_avg_price="84.90",
                            filled_at="2026-09-23T15:00:00.1Z")
        self.reconcile()
        dal = self.journal()["DAL"]
        self.assertAlmostEqual(float(dal["r_multiple"]), 2.067, places=3)
        self.assertEqual(dal["hit_target_first"], "1")

    def test_untouched_short_bracket_stopped(self):
        t = lambda s: datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
        o = self.fake.bracket("XLE", "short", "limit", 300, 64, 66, 60, fill=64.10,
                              filled_at=t("2026-09-10T13:31:00"), submitted=t("2026-09-10T13:05:00"))
        o["legs"][0]["status"] = "canceled"
        o["legs"][1].update(status="filled", filled_qty="300", filled_avg_price="66.05",
                            filled_at="2026-09-11T14:00:00.5Z")
        self.journal_row(ticker="XLE", direction="short", entry_planned=64, stop=66, target=60,
                         qty=300, risk_usd=600, order_id=o["id"])
        self.reconcile()
        xle = self.journal()["XLE"]
        self.assertEqual((xle["exit_reason"], xle["hit_target_first"]), ("stop", "0"))
        self.assertAlmostEqual(float(xle["r_multiple"]), -1.026, places=3)

    def test_market_close_and_a_later_trade_in_the_same_name(self):
        t = lambda s: datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
        f = self.fake
        o = f.bracket("QQQ", "long", "limit", 50, 500, 490, 520, fill=500,
                      filled_at=t("2026-09-10T13:31:00"), submitted=t("2026-09-10T13:05:00"))
        for leg in o["legs"]:
            leg["status"] = "canceled"
        f.orders.append(f.order("QQQ", "sell", "market", 50, status="filled", filled_qty=50,
                                fill=505, submitted=t("2026-09-12T13:10:00"),
                                filled_at=t("2026-09-12T13:30:01")))
        f.orders.append(f.order("QQQ", "sell", "limit", 40, status="filled", filled_qty=40,
                                fill=530, submitted=t("2026-09-15T13:10:00"),
                                filled_at=t("2026-09-15T13:40:00")))
        self.journal_row(ticker="QQQ", direction="long", entry_planned=500, stop=495, target=520,
                         stop_initial=490, target_initial=520, qty=50, risk_usd=500,
                         order_id=o["id"])
        self.reconcile()
        qqq = self.journal()["QQQ"]
        self.assertEqual(qqq["exit_reason"], "close")
        self.assertAlmostEqual(float(qqq["exit_fill"]), 505)
        self.assertAlmostEqual(float(qqq["r_multiple"]), 0.5)
        self.assertEqual(qqq["hit_target_first"], "")

    def test_never_filled(self):
        o = self.fake.bracket("AAPL", "long", "stop", 67, 346, 338.5, 358)
        o["status"] = "canceled"
        o["canceled_at"] = "2026-09-25T19:50:00.1Z"
        self.journal_row(ticker="AAPL", direction="long", entry_planned=346, stop=338.5,
                         target=358, qty=67, risk_usd=502.5, order_id=o["id"], status="new")
        out, _ = self.reconcile()
        self.assertIn("never filled", out)
        self.assertEqual(self.journal()["AAPL"]["exit_reason"], "never filled")

    def test_second_run_is_a_no_op(self):
        self.reconcile()
        out, _ = self.reconcile()
        self.assertIn("0 trade(s) closed out", out)


if __name__ == "__main__":
    unittest.main()
