#!/usr/bin/env bash
#
# One trading session, end to end. Run by .github/workflows/desk.yml,
# or by hand locally with the same env vars set.
#
set -euo pipefail

DATE="$(date -u +%Y-%m-%d)"
BRIEF="briefs/${DATE}.md"
mkdir -p briefs state

echo "::group::Settle previous session"
python3 desk.py reconcile | tee state/reconcile.txt
# Only kill entry orders older than the max holding horizon. A limit order
# resting from yesterday is still a live thesis; one from last week is not.
python3 desk.py stale --older-than 5 --confirm | tee state/stale.txt
python3 desk.py prep --out state/book.md
cat state/book.md
echo "::endgroup::"

echo "::group::Generate brief"
{
  cat prompts/daily-request.md
  echo
  cat state/book.md
} > state/request.md

# WebSearch and WebFetch only. No Bash, no Write - the model produces text and
# nothing else. Everything that touches the account goes through desk.py, which
# validates independently.
claude -p "$(cat state/request.md)" \
  --append-system-prompt "$(cat prompts/system.md)" \
  --allowedTools "WebSearch,WebFetch" \
  --permission-mode acceptEdits \
  --model opus \
  --max-turns 40 \
  --output-format text \
  | tee "${BRIEF}"
echo "::endgroup::"

if [ ! -s "${BRIEF}" ]; then
  echo "Brief is empty - Claude produced no output. Aborting before submission."
  exit 1
fi

echo "::group::Validate"
# check never blocks: bad plays are rejected individually and the good ones proceed.
python3 desk.py check "${BRIEF}" | tee "briefs/${DATE}.check.txt"
echo "::endgroup::"

echo "::group::Submit"
python3 desk.py submit "${BRIEF}" --confirm | tee "briefs/${DATE}.submit.txt"
echo "::endgroup::"

echo "::group::Score"
python3 desk.py score | tee state/score.txt
python3 desk.py status | tee state/status.txt
echo "::endgroup::"