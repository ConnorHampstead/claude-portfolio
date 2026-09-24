"""The shadow book: replaying passed ideas against the tape, and reporting them."""

import unittest
from datetime import datetime, timezone

from tests.support import CONFIG, DeskCase, desk
from tests.fake_alpaca import bar, et

DAYS = ["2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18",
        "2026-09-21", "2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25"]
SESSIONS = [(d, *desk.session_bounds({"date": d, "open": "09:30", "close": "16:00"})) for d in DAYS]
LATER = datetime(2026, 10, 1, tzinfo=timezone.utc)
D = DAYS[0]


def idea(direction="long", entry_type="limit", entry=100, stop=98, target=104,
         logged="2026-09-14T13:10:00.123456789Z"):
    return {"direction": direction, "entry_type": entry_type, "entry": entry, "stop": stop,
            "target": target, "logged_at": logged, "session_date": D}


def replay(row, bars, now=LATER):
    return desk.replay_idea(row, bars, SESSIONS, CONFIG, now)


class Replay(unittest.TestCase):
    def test_limit_fills_mid_bar_then_target(self):
        r = replay(idea(), [bar(et(D, "09:30"), 101, 101.5, 100.5, 101),
                            bar(et(D, "09:35"), 101, 101, 99.8, 100.2),
                            bar(et(D, "09:40"), 100.2, 104.3, 100.1, 104)])
        self.assertEqual((r["outcome"], r["entry_fill"], r["r_multiple"]), ("target", 100, 2.0))
        self.assertEqual(r["hit_target_first"], "1")

    def test_gap_through_the_limit_fills_at_the_open(self):
        """ROST 2026-08-21: limit 242.50, opened 237.84, stopped at 236."""
        r = replay(idea(entry=242.5, stop=236, target=258),
                   [bar(et(D, "09:30"), 237.84, 238.5, 235.5, 236)])
        self.assertEqual((r["outcome"], r["entry_fill"], r["exit_price"]), ("stop", 237.84, 236))
        self.assertEqual(r["hit_target_first"], "0")

    def test_both_levels_in_one_bar_is_ambiguous(self):
        r = replay(idea(), [bar(et(D, "09:30"), 101, 101.5, 99.9, 100.5),
                            bar(et(D, "09:35"), 100.5, 104.5, 97.5, 100)])
        self.assertEqual((r["outcome"], r["hit_target_first"], r["r_multiple"]), ("ambiguous", "", ""))

    def test_overnight_gap_through_the_stop_exits_at_the_open(self):
        r = replay(idea(), [bar(et(D, "09:30"), 101, 101.5, 99.9, 100.5),
                            bar(et(DAYS[1], "09:30"), 97, 97.5, 96, 97)])
        self.assertEqual((r["outcome"], r["exit_price"], r["r_multiple"]), ("stop", 97, -1.5))

    def test_short_breakdown_ignores_bars_before_it_was_logged(self):
        r = replay(idea("short", "stop", 50, 51, 47, logged="2026-09-14T14:10:00.5Z"),
                   [bar(et(D, "10:00"), 50.5, 50.6, 46.0, 46.2),   # before logging
                    bar(et(D, "10:15"), 50.5, 50.6, 49.9, 50.1),
                    bar(et(D, "10:20"), 50.1, 50.2, 46.9, 47.1)])
        self.assertEqual((r["outcome"], r["entry_fill"], r["r_multiple"]), ("target", 50, 3.0))

    def test_never_filled_after_the_entry_window(self):
        r = replay(idea(), [bar(et(d, "10:00"), 101, 102, 100.5, 101) for d in DAYS])
        self.assertEqual((r["outcome"], r["hit_target_first"]), ("never filled", ""))

    def test_expired_after_the_exit_window(self):
        r = replay(idea(), [bar(et(d, "10:00"), 100.5, 101, 99.5, 100.5) for d in DAYS])
        self.assertEqual((r["outcome"], r["r_multiple"]), ("expired", 0.25))

    def test_pending_while_the_windows_are_open(self):
        r = replay(idea(), [bar(et(D, "09:30"), 101, 101.5, 99.9, 100.5)],
                   now=datetime(2026, 9, 15, 15, tzinfo=timezone.utc))
        self.assertEqual((r["status"], r["entry_fill"]), ("pending", 100))

    def test_after_hours_bars_are_ignored(self):
        r = replay(idea(), [bar(et(D, "09:30"), 101, 101.5, 100.5, 101),
                            bar(et(D, "16:05"), 99, 99, 90, 90)])
        self.assertNotEqual(r.get("outcome"), "stop")


class ShadowCommand(DeskCase):
    NOW = datetime(2026, 9, 24, 20, 30, tzinfo=timezone.utc)

    def test_replays_through_the_api_and_reports(self):
        desk.append_shadow([
            {"shadow_id": "a", "logged_at": "2026-09-22T14:10:00+00:00", "session_date": "2026-09-22",
             "session": "open", "source": "passed", "ticker": "XLE", "direction": "short",
             "entry_type": "limit", "entry": 64.5, "stop": 66.2, "target": 61, "p_target_first": 0.4,
             "reason": "wrong location", "status": "pending"},
            {"shadow_id": "b", "logged_at": "2026-09-22T14:10:00+00:00", "session_date": "2026-09-22",
             "session": "open", "source": "dropped", "ticker": "TSLA", "direction": "long",
             "entry_type": "limit", "entry": 248, "stop": 243, "target": 262, "p_target_first": 0.45,
             "reason": "caps", "status": "pending"}])
        self.fake.bars[("5Min", "XLE")] = [bar(et("2026-09-22", "10:30"), 64.2, 64.6, 64.1, 64.5),
                                           bar(et("2026-09-22", "10:35"), 64.5, 64.5, 60.8, 61)]
        self.fake.no_sip = True  # the plan refusing SIP must fall back, not fail
        out, code = self.run_cmd(desk.cmd_shadow)
        self.assertEqual(code, 0, out)
        rows = {r["ticker"]: r for r in self.shadow()}
        self.assertEqual(rows["XLE"]["outcome"], "target")
        self.assertAlmostEqual(float(rows["XLE"]["r_multiple"]), 2.059, places=3)
        self.assertEqual(rows["TSLA"]["status"], "pending")

        out, _ = self.run_cmd(desk.cmd_score)
        self.assertIn("SHADOW BOOK   2 ideas passed on or dropped, 1 resolved", out)
        self.assertIn("Target first    1", out)

        prep, _ = self.run_cmd(desk.cmd_prep, out=None)
        self.assertIn("| 2026-09-22 open | XLE | short | wrong location | target | +2.06R | 40% |", prep)


if __name__ == "__main__":
    unittest.main()
