"""scripts/session.sh end to end, with claude and desk.py stubbed out."""

import os
import shutil
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

STUB_DESK = '''
import sys
with open("desk-calls.txt", "a") as f:
    f.write(" ".join(sys.argv[1:]) + "\\n")
if sys.argv[1] == "prep":
    size = int(open("book-size").read()) if __import__("os").path.exists("book-size") else 0
    open(sys.argv[sys.argv.index("--out") + 1], "w").write("## Current book state\\n" + "x" * size)
print("desk.py", " ".join(sys.argv[1:]))
'''

STUB_CLAUDE = '''#!/usr/bin/env bash
# The prompt is the argument after -p; record it and the flags.
printf '%s' "$2" > claude-prompt.txt
printf '%s\\n' "$@" > claude-args.txt
echo "Brief text."
echo '```json'
echo '{"no_trade": true, "plays": []}'
echo '```'
'''


@unittest.skipUnless(shutil.which("bash"), "needs bash")
class SessionScript(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="session-sh-"))
        shutil.copytree(REPO / "scripts", self.dir / "scripts")
        shutil.copytree(REPO / "prompts", self.dir / "prompts")
        (self.dir / "desk.py").write_text(STUB_DESK)
        bin_dir = self.dir / "bin"
        bin_dir.mkdir()
        (bin_dir / "claude").write_text(STUB_CLAUDE)
        (bin_dir / "claude").chmod(0o755)
        self.env = {**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}"}
        for k in ("DRY_RUN", "SESSION", "DESK_MODEL"):
            self.env.pop(k, None)
        self.date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def run_session(self, **env):
        return subprocess.run(["bash", "scripts/session.sh"], cwd=self.dir, capture_output=True,
                              text=True, env={**self.env, **env}, timeout=60)

    def calls(self):
        return (self.dir / "desk-calls.txt").read_text().splitlines()

    def test_pre_market(self):
        r = self.run_session()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        calls = self.calls()
        self.assertIn("stale --older-than 5 --confirm", calls)
        self.assertIn(f"submit briefs/{self.date}.md --confirm --session pre-market "
                      "--model claude-opus-5-5", calls)
        self.assertTrue((self.dir / f"briefs/{self.date}.submit.txt").exists())
        prompt = (self.dir / "claude-prompt.txt").read_text()
        self.assertTrue(prompt.startswith("Produce today's pre-market brief."))
        args = (self.dir / "claude-args.txt").read_text().splitlines()
        self.assertEqual(args[args.index("--model") + 1], "claude-opus-5-5")
        self.assertEqual(args[args.index("--allowedTools") + 1], "WebSearch,WebFetch")

    def test_open_session_reads_the_morning_brief(self):
        (self.dir / "briefs").mkdir()
        (self.dir / f"briefs/{self.date}.md").write_text("MORNING BRIEF BODY")
        r = self.run_session(SESSION="open")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        calls = self.calls()
        self.assertFalse(any(c.startswith("stale") for c in calls), "stale runs pre-market only")
        self.assertIn(f"submit briefs/{self.date}-open.md --confirm --session open "
                      "--model claude-opus-5-5", calls)
        for name in (f"briefs/{self.date}-open.md", f"briefs/{self.date}-open.submit.txt",
                     "state/book-open.md", "state/request-open.md"):
            self.assertTrue((self.dir / name).exists(), name)
        prompt = (self.dir / "claude-prompt.txt").read_text()
        self.assertTrue(prompt.startswith("Produce the post-open review."))
        self.assertLess(prompt.index("MORNING BRIEF BODY"), prompt.index("## Current book state"))

    def test_open_session_without_a_morning_brief(self):
        r = self.run_session(SESSION="open")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("No pre-market brief ran today", (self.dir / "claude-prompt.txt").read_text())

    def test_dry_run_submits_nothing(self):
        r = self.run_session(DRY_RUN="1")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        calls = self.calls()
        self.assertFalse(any(c.startswith("submit") for c in calls))
        self.assertIn("stale --older-than 5", calls)
        self.assertTrue((self.dir / f"state/dryrun/{self.date}.md").exists())
        self.assertFalse((self.dir / "briefs" / f"{self.date}.submit.txt").exists())

    def test_unknown_session(self):
        r = self.run_session(SESSION="lunch")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("Unknown SESSION 'lunch'", r.stdout)

    def test_request_too_long_for_one_argument(self):
        (self.dir / "book-size").write_text("125000")
        r = self.run_session()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("too long for one argument", r.stdout)
        self.assertFalse((self.dir / "claude-prompt.txt").exists())


if __name__ == "__main__":
    unittest.main()
