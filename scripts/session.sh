#!/usr/bin/env bash
#
# One trading session, end to end. Run by .github/workflows/desk.yml,
# or by hand locally with the same env vars set.
#
#   SESSION=pre-market  (default) the morning brief, ~25 min before the open
#   SESSION=open        the post-open review, ~35 min after it
#
set -euo pipefail

# An unset GitHub secret expands to an empty string, and an empty auth variable
# is worse than an absent one — Claude Code resolves credentials in precedence
# order and an empty high-precedence var can shadow the one you meant to use.
for v in ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN CLAUDE_CODE_OAUTH_TOKEN; do
  if [ -z "${!v:-}" ]; then unset "$v" || true; fi
done

DATE="$(date -u +%Y-%m-%d)"
DRY_RUN="${DRY_RUN:-}"
SESSION="${SESSION:-pre-market}"
# Pinned, not an alias: a model change is a change to the experiment, and the
# journal records which model wrote each play.
export DESK_MODEL="${DESK_MODEL:-claude-opus-5-5}"
SUBMIT_RC=0
mkdir -p briefs state

case "$SESSION" in
  pre-market) SFX=""; REQUEST_TEMPLATE="prompts/daily-request.md" ;;
  open)       SFX="-open"; REQUEST_TEMPLATE="prompts/open-request.md" ;;
  *) echo "Unknown SESSION '${SESSION}' - expected pre-market or open."; exit 1 ;;
esac

if [ -n "$DRY_RUN" ]; then
  # Write to a scratch dir so a test run can never clobber a real brief, and
  # never submits. Everything up to and including validation still executes.
  mkdir -p state/dryrun
  BRIEF="state/dryrun/${DATE}${SFX}.md"
  CHECK="state/dryrun/${DATE}${SFX}.check.txt"
  echo "*** DRY RUN - no orders will be submitted, no real brief overwritten ***"
else
  BRIEF="briefs/${DATE}${SFX}.md"
  CHECK="briefs/${DATE}${SFX}.check.txt"
fi
echo "Session: ${SESSION}   model: ${DESK_MODEL}"

echo "::group::Settle previous session"
python3 desk.py reconcile | tee "state/reconcile${SFX}.txt"
# Replays the ideas earlier briefs passed on. Informational: a failure here
# must not stop the session, so it is not allowed to fail the script.
python3 desk.py shadow | tee "state/shadow${SFX}.txt" || true
if [ "$SESSION" = "pre-market" ]; then
  # Only kill entry orders older than the max holding horizon. A limit order
  # resting from yesterday is still a live thesis; one from last week is not.
  if [ -n "$DRY_RUN" ]; then
    python3 desk.py stale --older-than 5 | tee state/stale.txt
  else
    python3 desk.py stale --older-than 5 --confirm | tee state/stale.txt
  fi
fi
python3 desk.py prep --out "state/book${SFX}.md"
cat "state/book${SFX}.md"
echo "::endgroup::"

echo "::group::Generate brief"
{
  cat "$REQUEST_TEMPLATE"
  echo
  if [ "$SESSION" = "open" ]; then
    echo "## This morning's pre-market brief"
    echo
    cat "briefs/${DATE}.md" 2>/dev/null \
      || echo "*No pre-market brief ran today. Work from the book state alone.*"
    echo
  fi
  cat "state/book${SFX}.md"
} > "state/request${SFX}.md"

# Linux caps a single argument at 128 KiB. The open session's request carries
# the morning brief and the market tables, around 30 KiB - fail loudly rather
# than have exec refuse it if that ever grows.
if [ "$(wc -c < "state/request${SFX}.md")" -gt 120000 ]; then
  echo "::error::state/request${SFX}.md is over 120 KB - too long for one argument."
  exit 1
fi

# WebSearch and WebFetch only. No Bash, no Write - the model produces text and
# nothing else. Everything that touches the account goes through desk.py, which
# validates independently.
claude -p "$(cat "state/request${SFX}.md")" \
  --append-system-prompt "$(cat prompts/system.md)" \
  --allowedTools "WebSearch,WebFetch" \
  --permission-mode acceptEdits \
  --model "$DESK_MODEL" \
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
python3 desk.py check "${BRIEF}" | tee "${CHECK}"
echo "::endgroup::"

if [ -n "$DRY_RUN" ]; then
  echo "::group::Submit (SKIPPED - dry run)"
  echo "Dry run complete. The plan above was validated but not sent."
  echo "Brief:      ${BRIEF}"
  echo "Validation: ${CHECK}"
  echo "::endgroup::"
else
  echo "::group::Submit"
  # Not fatal on the spot. An order that did not reach Alpaca must fail the
  # run, but the scoring, status and chart below are how you find out what the
  # book actually looks like afterwards - so they still run, and the exit code
  # is carried to the end of the script.
  SUBMIT_RC=0
  python3 desk.py submit "${BRIEF}" --confirm --session "$SESSION" --model "$DESK_MODEL" \
    | tee "briefs/${DATE}${SFX}.submit.txt" || SUBMIT_RC=$?
  echo "::endgroup::"
fi

echo "::group::Score"
python3 desk.py score | tee state/score.txt
python3 desk.py status | tee state/status.txt
echo "::endgroup::"

echo "::group::Performance chart"
# Snapshots equity, redraws the curve against SPY, and rewrites the block
# between the PERFORMANCE markers in README.md.
python3 desk.py chart --update-readme
echo "::endgroup::"

if [ "${SUBMIT_RC}" -ne 0 ]; then
  echo "::error::Not every order reached Alpaca - see the Submit group. The"\
       "book does not match the brief; check state/status.txt before the open."
  exit "${SUBMIT_RC}"
fi
