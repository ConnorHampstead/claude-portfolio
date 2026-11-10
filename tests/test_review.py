"""The transcript split, and the weekly review's material and verdicts."""

import argparse
import contextlib
import io
import json
import unittest

from tests.support import DeskCase, desk

SEARCH = {"type": "assistant", "message": {"content": [
    {"type": "text", "text": "Checking futures."},
    {"type": "tool_use", "name": "WebSearch", "input": {"query": "S&P 500 futures premarket"}}]}}
FETCH = {"type": "assistant", "message": {"content": [
    {"type": "tool_use", "name": "WebFetch",
     "input": {"url": "https://example.com/release", "prompt": "the figure"}}]}}
DONE = {"type": "result", "subtype": "success", "is_error": False, "num_turns": 3,
        "duration_ms": 412000, "result": "The brief.\n\n```json\n{\"plays\": []}\n```"}


class Transcript(DeskCase):
    def split(self, events, min_research=1):
        path = self.tmp / "transcript.jsonl"
        path.write_text("\n".join(["not json"] + [json.dumps(e) for e in events]) + "\n")
        out, code = self.run_cmd(desk.cmd_transcript, file=str(path),
                                 brief=str(self.tmp / "brief.md"),
                                 log=str(self.tmp / "brief.research.txt"),
                                 min_research=min_research)
        return out, code, (self.tmp / "brief.md").read_text(), \
            (self.tmp / "brief.research.txt").read_text().splitlines()

    def test_brief_and_research_log(self):
        out, code, brief, log = self.split([{"type": "system"}, SEARCH, {"type": "user"},
                                            FETCH, DONE])
        self.assertEqual(code, 0, out)
        self.assertEqual(brief, DONE["result"] + "\n")
        self.assertEqual(log, ["2 lookups in 3 turns, 412 s",
                               "WebSearch: S&P 500 futures premarket",
                               "WebFetch: https://example.com/release"])

    def test_a_brief_written_from_memory_is_refused_but_kept(self):
        """Nothing recorded whether a session had searched at all."""
        out, code, brief, log = self.split([DONE])
        self.assertEqual(code, 1)
        self.assertEqual(log, ["0 lookups in 3 turns, 412 s"])
        self.assertTrue(brief.startswith("The brief."), "kept for the record")
        _, code, _, _ = self.split([DONE], min_research=0)   # the weekly review's setting
        self.assertEqual(code, 0)

    def test_a_run_that_did_not_finish(self):
        for events in ([SEARCH],                                   # killed by the timeout
                       [SEARCH, {**DONE, "is_error": True, "subtype": "error_max_turns"}],
                       [SEARCH, {**DONE, "result": ""}]):
            with self.subTest(events=len(events)):
                _, code, _, _ = self.split(events)
                self.assertEqual(code, 1)

    def test_a_failed_run_says_why(self):
        """2026-11-10: a session died at the account's usage limit and the
        run's public metadata said only 'exit code 1'."""
        path = self.tmp / "transcript.jsonl"
        path.write_text(json.dumps({**DONE, "is_error": True, "result": "Usage limit\nreached"}))
        with self.assertRaises(SystemExit) as e, contextlib.redirect_stdout(io.StringIO()):
            desk.cmd_transcript(argparse.Namespace(file=str(path), brief=str(self.tmp / "b.md"),
                                                   log=None, min_research=0))
        self.assertIn("::error::", e.exception.code)
        self.assertIn("(success): Usage limit reached.", e.exception.code)


class WeeklyReview(DeskCase):
    def setUp(self):
        super().setUp()
        closed = dict(direction="long", entry_planned=100, entry_fill=100, stop=98, target=104,
                      qty=100, risk_usd=200, exit_reason="stop", exit_fill=98, pnl_usd=-200,
                      r_multiple=-1.0, closed_at="2026-09-23T15:00:00Z")
        self.journal_row(ticker="LLY", thesis="Guidance raise.", invalidation="A close under 99.",
                         bracket_outcome="stop", bracket_r=-1.0, **closed)
        self.journal_row(ticker="ANET", thesis_verdict="wrong thesis wrong outcome", **closed)
        self.journal_row(ticker="DAL", direction="long", entry_planned=80, stop=78, target=84,
                         qty=100, risk_usd=200, entry_fill=80)   # still open

    def test_material_is_the_unjudged_trades_and_the_weeks_logs(self):
        briefs = self.tmp / "briefs"
        (briefs / "2026-09-23.submit.txt").write_text("> LLY long x100 submitted")
        (briefs / "2026-09-23.check.txt").write_text("the same validation again")
        (briefs / "2026-09-24.check.txt").write_text("[REJECTED] XLE")
        (briefs / "2026-09-24.research.txt").write_text("14 lookups in 9 turns, 380 s")
        (briefs / "2026-09-10.submit.txt").write_text("two weeks ago")
        out, _ = self.run_cmd(desk.cmd_review_prep, out=None, limit=15)
        self.assertIn("### tlly: LLY long, proposed 2026-09-01 (pre-market)", out)
        self.assertIn("-1.00R, $-200. Left alone the bracket ended in stop at -1.00R", out)
        self.assertIn("- Invalidation: A close under 99.", out)
        for absent in ("tanet", "tdal", "the same validation again", "two weeks ago"):
            self.assertNotIn(absent, out)
        for present in ("### 2026-09-23.submit.txt", "[REJECTED] XLE", "14 lookups in 9 turns"):
            self.assertIn(present, out)

    def test_verdicts_fill_only_blank_closed_rows(self):
        review = self.brief({"verdicts": [
            {"play_id": "tlly", "verdict": "Right thesis / wrong outcome"},
            {"play_id": "tanet", "verdict": "right thesis right outcome"},   # judged already
            {"play_id": "tdal", "verdict": "right thesis right outcome"},    # still open
            {"play_id": "tlly", "verdict": "probably fine"},
            {"play_id": "nope", "verdict": "wrong thesis wrong outcome"}]}, "review.md")
        out, code = self.run_cmd(desk.cmd_verdicts, file=review)
        self.assertEqual(code, 0, out)
        self.assertIn("1 thesis verdict(s) recorded", out)
        self.assertIn("x tlly: not recorded ('probably fine')", out)
        self.assertIn("x nope: not recorded", out)
        rows = self.journal()
        self.assertEqual(rows["LLY"]["thesis_verdict"], "right thesis wrong outcome")
        self.assertEqual(rows["ANET"]["thesis_verdict"], "wrong thesis wrong outcome")
        self.assertEqual(rows["DAL"]["thesis_verdict"], "")


if __name__ == "__main__":
    unittest.main()
