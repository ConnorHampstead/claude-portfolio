"""Session timing: calendar guards, the wait, and DST."""

import unittest
from datetime import datetime, timezone

from tests.support import POST_OPEN, DeskCase, desk


class Calendar(DeskCase):
    def calendar(self, **kw):
        kw.setdefault("before_open", None)
        kw.setdefault("open_window", None)
        return self.run_cmd(desk.cmd_calendar, **kw)

    def test_pre_market_deadline(self):
        out, code = self.calendar(before_open=5)            # 09:07, open 09:30
        self.assertEqual(code, 0, out)
        self.freeze(datetime(2026, 9, 24, 13, 27, tzinfo=timezone.utc))  # 09:27
        out, code = self.calendar(before_open=5)
        self.assertEqual(code, 1)
        self.assertIn("DEADLINE MISSED", out)

    def test_post_open_window(self):
        self.freeze(POST_OPEN)                               # 36 min after the open
        out, code = self.calendar(open_window=[30, 120])
        self.assertEqual(code, 0, out)
        for hh, mm, why in ((13, 45, "15 min in: too early"), (15, 45, "135 min in: too late")):
            self.freeze(datetime(2026, 9, 24, hh, mm, tzinfo=timezone.utc))
            _, code = self.calendar(open_window=[30, 120])
            self.assertEqual(code, 1, why)

    def test_weekend(self):
        self.freeze(datetime(2026, 9, 26, 13, 7, tzinfo=timezone.utc))
        out, code = self.calendar()
        self.assertEqual(code, 1)
        self.assertIn("not a US trading day", out)

    def test_wait_returns_at_once_when_the_target_has_passed(self):
        self.freeze(POST_OPEN)
        out, _ = self.run_cmd(desk.cmd_wait, before_open=None, after_open=35,
                              before_close=None, time=None, tz=None)
        self.assertIn("past", out)


class DaylightSaving(unittest.TestCase):
    def test_open_in_utc_follows_new_york(self):
        summer = desk.session_bounds({"date": "2026-09-24", "open": "09:30", "close": "16:00"})
        winter = desk.session_bounds({"date": "2026-12-03", "open": "09:30", "close": "16:00"})
        self.assertEqual((summer[0].hour, summer[1].hour), (13, 20))
        self.assertEqual((winter[0].hour, winter[1].hour), (14, 21))

    def test_half_day(self):
        _, close = desk.session_bounds({"date": "2026-11-27", "open": "09:30", "close": "13:00"})
        self.assertEqual(close, datetime(2026, 11, 27, 18, 0, tzinfo=timezone.utc))


if __name__ == "__main__":
    unittest.main()
