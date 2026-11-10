"""scripts/session.sh and scripts/review.sh end to end, with claude and desk.py
stubbed out."""

import os
import re
import shutil
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

STUB_DESK = '''
import os, sys
args = sys.argv[1:]
with open("desk-calls.txt", "a") as f:
    f.write(" ".join(args) + "\\n")
after = lambda flag: args[args.index(flag) + 1]
if args[0] == "prep":
    size = int(open("book-size").read()) if os.path.exists("book-size") else 0
    open(after("--out"), "w").write("## Current book state\\n" + "x" * size)
if args[0] == "review-prep":
    open(after("--out"), "w").write("## Closed trades without a thesis verdict\\n")
if args[0] == "transcript":
    # The real one writes what there is and then refuses it.
    open(after("--brief"), "w").write(open(args[1]).read())
    if os.path.exists("transcript-fails"):
        sys.exit("The model run did not finish cleanly")
print("desk.py", " ".join(args))
'''

STUB_CLAUDE = '''#!/usr/bin/env bash
# The prompt is the argument after -p; record it, the flags and what it can see.
printf '%s' "$2" > claude-prompt.txt
printf '%s\\n' "$@" > claude-args.txt
printf '%s' "${ALPACA_API_KEY_ID:-unset}" > claude-env.txt
echo '{"type":"result","subtype":"success","is_error":false,"result":"Brief text."}'
'''


@unittest.skipUnless(shutil.which("bash"), "needs bash")
class ScriptCase(unittest.TestCase):
    SCRIPT = "scripts/session.sh"

    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="session-sh-"))
        shutil.copytree(REPO / "scripts", self.dir / "scripts")
        shutil.copytree(REPO / "prompts", self.dir / "prompts")
        (self.dir / "desk.py").write_text(STUB_DESK)
        bin_dir = self.dir / "bin"
        bin_dir.mkdir()
        (bin_dir / "claude").write_text(STUB_CLAUDE)
        (bin_dir / "claude").chmod(0o755)
        self.env = {**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}",
                    "ALPACA_API_KEY_ID": "broker-key"}
        for k in ("DRY_RUN", "SESSION", "DESK_MODEL", "DESK_EFFORT"):
            self.env.pop(k, None)
        self.date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def run_script(self, **env):
        return subprocess.run(["bash", self.SCRIPT], cwd=self.dir, capture_output=True,
                              text=True, env={**self.env, **env}, timeout=60)

    def calls(self):
        f = self.dir / "desk-calls.txt"
        return f.read_text().splitlines() if f.exists() else []

    def claude_args(self):
        return (self.dir / "claude-args.txt").read_text().split("\n")

    def flag(self, name):
        args = self.claude_args()
        return args[args.index(name) + 1]


class SessionScript(ScriptCase):
    def test_pre_market(self):
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        calls = self.calls()
        self.assertIn("stale --older-than 5 --confirm", calls)
        self.assertTrue(any(
            c.startswith("transcript ") and c.endswith(
                f"--brief briefs/{self.date}.md --log briefs/{self.date}.research.txt "
                "--min-research 1") for c in calls), calls)
        # The journal records the model and the effort together.
        self.assertIn(f"submit briefs/{self.date}.md --confirm --session pre-market "
                      "--model claude-opus-5-5/xhigh", calls)
        self.assertTrue((self.dir / f"briefs/{self.date}.submit.txt").exists())
        prompt = (self.dir / "claude-prompt.txt").read_text()
        self.assertTrue(prompt.startswith("Produce today's pre-market brief."))
        self.assertLess(prompt.index("## What the record has shown so far"),
                        prompt.index("## Current book state"))

    def test_the_model_gets_web_search_and_nothing_else(self):
        """It used to run with Read, Edit and Write available and edits
        pre-approved, in a checkout holding desk.py, with the broker keys in
        its environment."""
        self.run_script()
        self.assertEqual(self.flag("--tools"), "WebSearch,WebFetch")
        self.assertEqual(self.flag("--allowedTools"), "WebSearch,WebFetch")
        self.assertEqual((self.flag("--model"), self.flag("--effort")),
                         ("claude-opus-5-5", "xhigh"))
        self.assertTrue(self.flag("--system-prompt").startswith("## ROLE"))
        for gone in ("--permission-mode", "--append-system-prompt"):
            self.assertNotIn(gone, self.claude_args())
        self.assertEqual((self.dir / "claude-env.txt").read_text(), "unset")

    def test_pre_market_is_shown_the_last_review_but_not_todays(self):
        (self.dir / "briefs").mkdir()
        for day, body in (("2026-01-02", "EARLIER REVIEW"), ("2026-01-05", "LAST REVIEW"),
                          (self.date, "TODAYS REVIEW")):
            (self.dir / f"briefs/{day}-open.md").write_text(body)
        self.run_script()
        prompt = (self.dir / "claude-prompt.txt").read_text()
        self.assertLess(prompt.index("## Your last post-open review (2026-01-05)"),
                        prompt.index("LAST REVIEW"))
        self.assertLess(prompt.index("LAST REVIEW"), prompt.index("## Current book state"))
        for other in ("EARLIER REVIEW", "TODAYS REVIEW"):
            self.assertNotIn(other, prompt)

    def test_a_run_that_did_not_finish_reaches_nothing(self):
        (self.dir / "transcript-fails").write_text("")
        r = self.run_script()
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(any(c.startswith(("check", "submit")) for c in self.calls()))

    def test_open_session_reads_the_morning_brief(self):
        (self.dir / "briefs").mkdir()
        (self.dir / f"briefs/{self.date}.md").write_text("MORNING BRIEF BODY")
        r = self.run_script(SESSION="open")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        calls = self.calls()
        self.assertFalse(any(c.startswith("stale") for c in calls), "stale runs pre-market only")
        self.assertIn(f"submit briefs/{self.date}-open.md --confirm --session open "
                      "--model claude-opus-5-5/xhigh", calls)
        for name in (f"briefs/{self.date}-open.md", f"briefs/{self.date}-open.submit.txt",
                     "state/book-open.md", "state/request-open.md"):
            self.assertTrue((self.dir / name).exists(), name)
        prompt = (self.dir / "claude-prompt.txt").read_text()
        self.assertTrue(prompt.startswith("Produce the post-open review."))
        self.assertLess(prompt.index("MORNING BRIEF BODY"), prompt.index("## Current book state"))

    def test_open_session_without_a_morning_brief(self):
        r = self.run_script(SESSION="open")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("No pre-market brief ran today", (self.dir / "claude-prompt.txt").read_text())

    def test_dry_run_submits_nothing_and_logs_its_plays_to_be_scored(self):
        r = self.run_script(DRY_RUN="1", DESK_EFFORT="high")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        calls = self.calls()
        self.assertFalse(any(c.startswith("submit") for c in calls))
        self.assertIn("stale --older-than 5", calls)
        self.assertIn(f"check state/dryrun/{self.date}.md --log-shadow --session pre-market "
                      "--model claude-opus-5-5/high", calls)
        self.assertEqual(self.flag("--effort"), "high")
        self.assertTrue((self.dir / f"state/dryrun/{self.date}.md").exists())
        self.assertFalse((self.dir / "briefs" / f"{self.date}.submit.txt").exists())

    def test_unknown_session(self):
        r = self.run_script(SESSION="lunch")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("Unknown SESSION 'lunch'", r.stdout)

    def test_request_too_long_for_one_argument(self):
        (self.dir / "book-size").write_text("125000")
        r = self.run_script()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("too long for one argument", r.stdout)
        self.assertFalse((self.dir / "claude-prompt.txt").exists())
        self.assertFalse(any(c.startswith("submit") for c in self.calls()))


class ReviewScript(ScriptCase):
    SCRIPT = "scripts/review.sh"
    PINS = {"DESK_MODEL": "claude-opus-5-5", "DESK_EFFORT": "xhigh"}

    def test_reviews_the_week_and_records_its_verdicts(self):
        r = self.run_script(**self.PINS)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = f"reviews/weekly/{self.date}"
        calls = self.calls()
        self.assertEqual(calls[:4], ["reconcile", "shadow", "score",
                                     "review-prep --out state/review-material.md"])
        self.assertTrue(calls[4].endswith(f"--brief {out}.md --log {out}.research.txt "
                                          "--min-research 0"), calls)
        self.assertEqual(calls[5:], [f"verdicts {out}.md"])
        self.assertIn("--system-prompt\n## ROLE\n\nYou are reviewing one week",
                      (self.dir / "claude-args.txt").read_text())
        self.assertEqual(self.flag("--tools"), "WebSearch,WebFetch")
        prompt = (self.dir / "claude-prompt.txt").read_text()
        self.assertIn("desk.py score", prompt)
        self.assertIn("## Closed trades without a thesis verdict", prompt)

        r = self.run_script(**self.PINS)            # a second trigger the same day
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("already written", r.stdout)
        self.assertEqual(len(self.calls()), 6)

    def test_dry_run_records_no_verdict(self):
        r = self.run_script(DRY_RUN="1", **self.PINS)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(any(c.startswith("verdicts") for c in self.calls()))
        self.assertTrue((self.dir / f"state/dryrun/review-{self.date}.md").exists())
        self.assertFalse((self.dir / f"reviews/weekly/{self.date}.md").exists())

    def test_runs_only_with_a_pinned_model_and_effort(self):
        r = self.run_script()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("pinned in the workflow", r.stderr)
        self.assertFalse((self.dir / "claude-prompt.txt").exists())


class Pins(unittest.TestCase):
    """The model, the effort and the CLI version are part of the experiment.
    They are written in three places; this is what keeps them the same."""

    def test_both_workflows_and_the_script_default_agree(self):
        read = lambda name: (REPO / name).read_text()
        desk, review = read(".github/workflows/desk.yml"), read(".github/workflows/review.yml")
        session = read("scripts/session.sh")
        for pattern in (r"DESK_MODEL: (\S+)", r"DESK_EFFORT: (\S+)", r"claude-code@(\S+)"):
            with self.subTest(pattern):
                (pinned,) = set(re.findall(pattern, desk))
                self.assertRegex(pinned, r"^[\w.-]+$", "an exact value, not an expression")
                self.assertEqual(set(re.findall(pattern, review)), {pinned})
        for var in ("DESK_MODEL", "DESK_EFFORT"):
            (pinned,) = set(re.findall(rf"{var}: (\S+)", desk))
            self.assertIn(f'export {var}="${{{var}:-{pinned}}}"', session)


if __name__ == "__main__":
    unittest.main()
