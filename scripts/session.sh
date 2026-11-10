#!/usr/bin/env bash
#
# One trading session, end to end. Run by .github/workflows/desk.yml,
# or by hand locally with the same env vars set.
#
#   SESSION=pre-market  (default) the morning brief, ~25 min before the open
#   SESSION=open        the post-open review, ~35 min after it
#
set -euo pipefail

DATE="$(date -u +%Y-%m-%d)"
DRY_RUN="${DRY_RUN:-}"
SESSION="${SESSION:-pre-market}"
# Pinned, not an alias or a default: the model and how hard it is asked to
# think are both part of the experiment, and the journal records them
# together on every play.
export DESK_MODEL="${DESK_MODEL:-claude-opus-5-5}"
export DESK_EFFORT="${DESK_EFFORT:-xhigh}"
LABEL="${DESK_MODEL}/${DESK_EFFORT}"
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
echo "Session: ${SESSION}   model: ${DESK_MODEL}   effort: ${DESK_EFFORT}"

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
  # What the reviews have established, merged by hand. Until this file the
  # reviews wrote to reviews/ and nothing the desk learned reached the brief.
  if [ -s prompts/lessons.md ]; then
    cat prompts/lessons.md
    echo
  fi
  if [ "$SESSION" = "open" ]; then
    echo "## This morning's pre-market brief"
    echo
    cat "briefs/${DATE}.md" 2>/dev/null \
      || echo "*No pre-market brief ran today. Work from the book state alone.*"
    echo
  else
    # The brief is asked to name the level it would act at tomorrow, and
    # tomorrow's brief never saw it. The last review is short by design.
    PREV="$(ls briefs/*-open.md 2>/dev/null | grep -v "/${DATE}-open.md" | tail -n1 || true)"
    if [ -n "$PREV" ]; then
      echo "## Your last post-open review ($(basename "$PREV" -open.md))"
      echo
      echo "*For continuity: what you were watching and why. The book state below is"
      echo "current and overrides anything here.*"
      echo
      cat "$PREV"
      echo
    fi
  fi
  cat "state/book${SFX}.md"
} > "state/request${SFX}.md"

# ask.sh runs the model with web search and nothing else, and refuses a brief
# that was written without looking anything up.
bash scripts/ask.sh "state/request${SFX}.md" prompts/system.md "${BRIEF}" 1
echo "::endgroup::"

echo "::group::Validate"
# check never blocks: bad plays are rejected individually and the good ones proceed.
if [ -n "$DRY_RUN" ]; then
  # A dry run's plays are logged to the shadow book and scored, which is how
  # a prompt or model change is tried on a branch before it trades.
  python3 desk.py check "${BRIEF}" --log-shadow --session "$SESSION" --model "$LABEL" \
    | tee "${CHECK}"
else
  python3 desk.py check "${BRIEF}" | tee "${CHECK}"
fi
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
  python3 desk.py submit "${BRIEF}" --confirm --session "$SESSION" --model "$LABEL" \
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
