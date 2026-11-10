#!/usr/bin/env bash
#
# The weekly review. Run by .github/workflows/review.yml on Saturdays, or by
# hand with the same env vars set.
#
# It settles the week, hands the model the closed trades that have no thesis
# verdict and the week's session logs, and keeps two things: the review, in
# reviews/weekly/<date>.md, and its verdicts, in journal.csv's thesis_verdict
# column. It places and changes no orders and edits no prompt. What it finds
# reaches the desk only when someone merges a line into prompts/lessons.md.
#
set -euo pipefail

DATE="$(date -u +%Y-%m-%d)"
DRY_RUN="${DRY_RUN:-}"
mkdir -p reviews/weekly state/dryrun

if [ -n "$DRY_RUN" ]; then
  OUT="state/dryrun/review-${DATE}.md"
  echo "*** DRY RUN - no verdict is recorded ***"
else
  OUT="reviews/weekly/${DATE}.md"
  if [ -s "$OUT" ]; then
    echo "${OUT} is already written - nothing to do."
    exit 0
  fi
fi

echo "::group::Settle the week"
python3 desk.py reconcile
# Informational, as in session.sh: a failure here must not stop the review.
python3 desk.py shadow || true
python3 desk.py score | tee state/score.txt
python3 desk.py review-prep --out state/review-material.md
echo "::endgroup::"

echo "::group::Review"
{
  echo "Write this week's review. Today is ${DATE}."
  echo
  echo "## The record to date"
  echo
  echo '```'
  cat state/score.txt
  echo '```'
  echo
  cat state/review-material.md
} > state/review-request.md
bash scripts/ask.sh state/review-request.md prompts/review-weekly.md "$OUT"
echo "::endgroup::"

if [ -z "$DRY_RUN" ]; then
  python3 desk.py verdicts "$OUT"
fi
