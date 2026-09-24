"""Shared set-up: a fake Alpaca, a frozen clock, and a scratch directory.

Nothing here touches the repo's journal.csv, shadow.csv, config.json or
state/ - desk.py's paths are pointed at a temporary directory per test.
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import io
import json
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

import desk  # noqa: E402
from tests.fake_alpaca import FakeAlpaca  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"

# Fixed rather than read from the repo, so tuning config.json never breaks a test.
CONFIG = {
    "risk_per_trade_pct": 1.0, "min_risk_pct": 0.1, "max_open_risk_pct": 4.0,
    "max_positions": 8, "max_gross_exposure_pct": 150, "max_net_exposure_pct": 100,
    "max_position_pct": 50, "daily_loss_limit_pct": 3.0, "min_conviction": 1,
    "time_in_force": "gtc", "data_feed": "iex", "allow_shorts": True,
    "watchlist": {"Test list": ["SPY"]}, "movers_show": 8, "min_price": 5.0,
    "min_avg_volume": 1_000_000, "shadow_entry_sessions": 5, "shadow_exit_sessions": 10,
}

# Thursday 2026-09-24, 09:07 ET: the pre-market session.
PRE_MARKET = datetime(2026, 9, 24, 13, 7, tzinfo=timezone.utc)
# The same day, 10:06 ET: the post-open review.
POST_OPEN = datetime(2026, 9, 24, 14, 6, tzinfo=timezone.utc)


def frozen_datetime(now: datetime):
    class Frozen(datetime):
        @classmethod
        def now(cls, tz=None):
            return now.astimezone(tz) if tz else now.replace(tzinfo=None)
    return Frozen


class DeskCase(unittest.TestCase):
    NOW = PRE_MARKET

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="desk-test-"))
        shutil.copytree(FIXTURES / "briefs", self.tmp / "briefs")
        (self.tmp / "config.json").write_text(json.dumps(CONFIG))
        self._saved = {k: getattr(desk, k)
                       for k in ("api", "HERE", "JOURNAL", "SHADOW", "CONFIG", "datetime")}
        desk.HERE = self.tmp
        desk.JOURNAL = self.tmp / "journal.csv"
        desk.SHADOW = self.tmp / "shadow.csv"
        desk.CONFIG = self.tmp / "config.json"
        self.fake = FakeAlpaca(self.NOW)
        desk.api = self.fake
        self.freeze(self.NOW)

    def tearDown(self):
        for k, v in self._saved.items():
            setattr(desk, k, v)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def freeze(self, now: datetime):
        desk.datetime = frozen_datetime(now)
        self.fake.now = now

    def run_cmd(self, fn, **kwargs) -> tuple[str, int]:
        """Run a desk command; returns (stdout, exit code)."""
        buf, code = io.StringIO(), 0
        with contextlib.redirect_stdout(buf):
            try:
                fn(argparse.Namespace(**kwargs))
            except SystemExit as e:
                code = e.code if isinstance(e.code, int) else 1
        return buf.getvalue(), code

    def brief(self, doc: dict, name: str = "brief.md") -> str:
        path = self.tmp / name
        path.write_text("Prose above the block.\n\n```json\n" + json.dumps(doc) + "\n```\n")
        return str(path)

    def check(self, doc: dict, **kw) -> tuple[str, int]:
        return self.run_cmd(lambda a: desk.cmd_check(a, submit=False), file=self.brief(doc), **kw)

    def submit(self, doc: dict, **kw) -> tuple[str, int]:
        kw.setdefault("session", "pre-market")
        kw.setdefault("model", "test-model")
        return self.run_cmd(desk.cmd_submit, file=self.brief(doc), confirm=True, **kw)

    def journal(self) -> dict[str, dict]:
        return {r["ticker"]: r for r in desk.read_journal()}

    def shadow(self) -> list[dict]:
        return desk.read_shadow()

    def journal_row(self, **fields):
        """Append a journal row as submit would have written it."""
        row = {"play_id": "t" + fields["ticker"].lower(), "logged_at": "2026-09-01T13:07:00+00:00",
               "session_date": "2026-09-01", "entry_type": "limit", "status": "filled",
               "p_target_first": 0.45, "conviction": 3}
        row.update(fields)
        row.setdefault("stop_initial", row["stop"])
        row.setdefault("target_initial", row["target"])
        desk.append_journal(row)

    def post_bodies(self, symbol: str | None = None) -> list[dict]:
        return [b for m, p, _, b in self.fake.calls
                if m == "POST" and p == "/v2/orders" and (symbol is None or b["symbol"] == symbol)]


def read_csv(path) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))
