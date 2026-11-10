#!/usr/bin/env bash
#
# One model run, the same way for every caller (session.sh, review.sh):
#
#   ask.sh REQUEST_FILE SYSTEM_PROMPT_FILE OUT_FILE [MIN_LOOKUPS]
#
# Writes the model's final text to OUT_FILE and the list of what it looked up
# to OUT_FILE with .research.txt in place of .md. Exits non-zero if the run did
# not finish, or looked up fewer than MIN_LOOKUPS things.
#
set -euo pipefail

REQUEST="$1" SYSTEM="$2" OUT="$3" MIN_LOOKUPS="${4:-0}"
: "${DESK_MODEL:?set by the caller - pinned in the workflow}"
: "${DESK_EFFORT:?set by the caller - pinned in the workflow}"

# An unset GitHub secret expands to an empty string, and an empty auth variable
# is worse than an absent one — Claude Code resolves credentials in precedence
# order and an empty high-precedence var can shadow the one you meant to use.
for v in ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN CLAUDE_CODE_OAUTH_TOKEN; do
  if [ -z "${!v:-}" ]; then unset "$v" || true; fi
done

# Linux caps a single argument at 128 KiB. The open session's request carries
# the morning brief and the market tables, around 40 KiB - fail loudly rather
# than have exec refuse it if that ever grows.
if [ "$(wc -c < "$REQUEST")" -gt 120000 ]; then
  echo "::error::${REQUEST} is over 120 KB - too long for one argument."
  exit 1
fi

# WebSearch and WebFetch are the only tools that exist for this run: --tools
# sets what the model has, --allowedTools only what it may use unasked. The
# old flags (--allowedTools with --permission-mode acceptEdits) left Read,
# Edit and Write in place and approved the edits, so a fetched page that
# talked the model into it could have rewritten desk.py ahead of the submit
# that follows. The broker keys are kept out of its environment for the same
# reason.
#
# --system-prompt replaces Claude Code's own coding-agent prompt instead of
# adding to it. The transcript goes to a scratch file; desk.py splits it into
# the text and the list of what was looked up. 25 minutes bounds a hung run so
# it cannot hold the next session's place in the queue; the turn limit is only
# a backstop behind it, and is high because a run that hits it has no brief.
TRANSCRIPT="$(mktemp)"
env -u ALPACA_API_KEY_ID -u ALPACA_API_SECRET_KEY \
  timeout 25m claude -p "$(cat "$REQUEST")" \
  --system-prompt "$(cat "$SYSTEM")" \
  --tools "WebSearch,WebFetch" \
  --allowedTools "WebSearch,WebFetch" \
  --model "$DESK_MODEL" \
  --effort "$DESK_EFFORT" \
  --max-turns 80 \
  --output-format stream-json --verbose \
  > "$TRANSCRIPT" \
  || echo "::warning::claude exited $? - the transcript decides whether there is anything to act on."
python3 desk.py transcript "$TRANSCRIPT" --brief "$OUT" \
  --log "${OUT%.md}.research.txt" --min-research "$MIN_LOOKUPS"
cat "$OUT"
