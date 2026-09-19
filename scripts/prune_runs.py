#!/usr/bin/env python3
"""
prune_runs.py - delete Actions runs that never did any work.

Most runs of desk.yml and weekend.yml exit without acting: a duplicate trigger
that finds the day already done, a non-trading day, or a late trigger that
stands down past its deadline. They bury the runs that matter.

A run is deleted when its work step ("Run session" / "Cancel resting entries")
was skipped and the run ended success or cancelled. The work step, not the
hold step, is the test: a late trigger runs the hold as a no-op and then
stands down, and older runs predate the hold step entirely. Runs that were
cancelled before any job started (superseded in the concurrency queue) go too.

Always kept:
    - failures and timeouts, work step or not
    - runs whose work step cannot be found (e.g. after a rename) - these print
      a warning instead, so a renamed step can never turn into deleted sessions
    - runs younger than --min-age-hours

Also deletes this workflow's own successful runs, which would otherwise be a
new do-nothing run every day.

Read-only unless you pass --confirm. Needs GITHUB_TOKEN (actions: write) and
GITHUB_REPOSITORY (owner/name).

    python3 scripts/prune_runs.py                  # list what would go
    python3 scripts/prune_runs.py --confirm        # delete it
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

WORK_STEPS = {
    "desk.yml": "Run session",
    "weekend.yml": "Cancel resting entries",
}
SELF = "prune-runs.yml"

API = "https://api.github.com"


def api(method: str, path: str):
    req = urllib.request.Request(
        API + path,
        method=method,
        headers={
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req) as res:
        body = res.read()
        return json.loads(body) if body else None


def completed_runs(repo: str, workflow: str, since: datetime):
    page = 1
    while True:
        data = api(
            "GET",
            f"/repos/{repo}/actions/workflows/{workflow}/runs"
            f"?status=completed&created=%3E%3D{since:%Y-%m-%d}&per_page=100&page={page}",
        )
        yield from data["workflow_runs"]
        if len(data["workflow_runs"]) < 100:
            return
        page += 1


def verdict(repo: str, run: dict, work_step: str | None) -> tuple[bool, str]:
    """(delete?, reason). Only returns True for a run that provably did nothing."""
    conclusion = run["conclusion"]
    if conclusion not in ("success", "cancelled"):
        return False, f"keep: {conclusion}"

    if work_step is None:  # this workflow's own runs
        return conclusion == "success", f"own run, {conclusion}"

    jobs = api("GET", f"/repos/{repo}/actions/runs/{run['id']}/jobs")["jobs"]
    steps = [s for j in jobs for s in (j.get("steps") or [])]
    if not steps:
        if conclusion == "cancelled":
            return True, "cancelled before starting"
        return False, "keep: no step data"

    work = next((s for s in steps if s["name"] == work_step), None)
    if work is None:
        print(f"WARNING: run {run['id']} has no step named {work_step!r} - "
              f"renamed? Kept.", file=sys.stderr)
        return False, "keep: work step not found"
    if work["conclusion"] == "skipped":
        return True, f"{work_step!r} skipped, {conclusion}"
    return False, f"keep: {work_step!r} {work['conclusion']}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--confirm", action="store_true", help="actually delete")
    # 90 = GitHub's default run retention, so every run that still exists is
    # considered and no one-off backlog pass is needed.
    ap.add_argument("--days", type=int, default=90,
                    help="look back this many days (default 90)")
    ap.add_argument("--min-age-hours", type=float, default=24,
                    help="never touch runs younger than this (default 24)")
    args = ap.parse_args()

    repo = os.environ["GITHUB_REPOSITORY"]
    now = datetime.now(timezone.utc)
    since = now - timedelta(days=args.days)
    cutoff = now - timedelta(hours=args.min_age_hours)

    deleted = kept = 0
    for workflow, work_step in [*WORK_STEPS.items(), (SELF, None)]:
        try:
            runs = list(completed_runs(repo, workflow, since))
        except urllib.error.HTTPError as e:
            if e.code == 404:  # workflow file not on the default branch yet
                continue
            raise
        for run in runs:
            created = datetime.fromisoformat(run["created_at"].replace("Z", "+00:00"))
            if created > cutoff:
                continue
            delete, reason = verdict(repo, run, work_step)
            label = f"{run['created_at']}  {workflow:<16} {run['event']:<17} {run['id']}"
            if not delete:
                kept += 1
                continue
            if args.confirm:
                api("DELETE", f"/repos/{repo}/actions/runs/{run['id']}")
            print(f"{'deleted' if args.confirm else 'would delete'}  {label}  ({reason})")
            deleted += 1

    verb = "Deleted" if args.confirm else "Would delete"
    print(f"\n{verb} {deleted} run(s), kept {kept}.")
    if not args.confirm and deleted:
        print("Read-only. Pass --confirm to delete.")


if __name__ == "__main__":
    main()
