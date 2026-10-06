# dispatch

Triggers the GitHub Actions workflows on a clock that keeps time. GitHub's
`schedule` event ran 4-6 hours late on this repo, every day; `workflow_dispatch`
starts in seconds. So the clock lives here and GitHub only supplies the runner.

| Job | Workflow | Cloudflare cron |
|---|---|---|
| Pre-market brief | `desk.yml` | 08:55 ET, Mon-Fri |
| Post-open review | `desk.yml`, `session=open` | 09:55 ET, Mon-Fri |
| Weekend cleanup | `weekend.yml` | 15:40 ET, Fri |

Each job has a target (pre-market: 25 min before the open, 09:05 ET; post-open:
35 min after it, 10:05 ET; weekend: 10 min before the close) and holds its
runner until then. Each dispatch sits 10 min ahead of its target, short enough
that a runner is never tied up for long. On the half-day after Thanksgiving the
close is 13:00 ET, so the weekend cleanup arrives after it and cancels straight
away; that is still well before Monday's open.

Each call passes `dry_run=false`, and `session` for the two desk jobs (the
workflow defaults it to `pre-market`). A duplicate dispatch - a manual one on
top of the scheduled one - queues behind the `trading-desk` concurrency group
and exits on the workflow's already-ran check, which is per session.

There is no second trigger. A systemd timer on a desktop served as a backup
until 2026-09-28; it was removed because a machine that was off caught up on
waking, once per timer, and a weekend cleanup that catches up midweek cancels
every resting entry. If a Cloudflare dispatch fails, that session is missed -
re-run it by hand from the Actions tab if it is still inside its window.

The workflows' `dry_run` input defaults to `true`, so anything that
dispatches them must pass `dry_run=false` explicitly or it will never trade.

Passing it is not enough on its own. A `type: boolean` input arrives as a real
boolean from the Actions tab, but as the **string** `"false"` from the dispatch
API - which is what the Worker uses, and what `gh workflow run -f` sends.
A bare `${{ inputs.dry_run }}` is truthy for that string, so every dispatched
run came out a dry run while manual ones traded. The workflows compare against
both forms; do not simplify that expression.

## Token

The Worker needs one fine-grained PAT (GitHub → Settings → Developer settings →
Fine-grained tokens):

- Repository access: only `claude-portfolio`
- Permissions: **Actions: Read and write**
- Set an expiry and a calendar reminder a week before it.

Anyone holding it can start a live session. The already-ran marker and the
session windows cap that at one of each session per day.

## Cloudflare Worker

Cron Triggers work on the Workers free plan (5 per account; this uses 3).
Cloudflare cron is UTC-only, so each cron lists both the EDT and EST hour and
`src/index.ts` dispatches only on the one matching New York time.

Weekdays are written as names (`MON-FRI`, `FRI`), never numbers. Cloudflare
counts 1 = Sunday .. 7 = Saturday, not standard cron's 0 = Sunday, so the
original `1-5` ran Sunday-Thursday: the Friday session never dispatched and the
Friday cleanup ran on Thursday (2026-09-24/25). The Worker also checks the
weekday in New York before dispatching, and `tests/test_schedule.py` fails on
a numeric weekday.

```sh
cd dispatch
npm install
npx wrangler login
npx wrangler secret put GH_TOKEN
npx wrangler deploy
```

Test locally without trading. The dry-run variable is essential here: without
it the curl below sends a live dispatch.

```sh
printf 'GH_TOKEN=github_pat_...\nDISPATCH_DRY_RUN=true\n' > .dev.vars
npm run dev          # delete .dev.vars when done - it holds a live token
# another terminal; `time` is epoch *milliseconds* and must fall in the 08:xx ET
# hour, or the Worker skips it as the other DST slot. The older /__scheduled
# route ignores `time` and uses the real clock.
# 1790081700000 = Tue 2026-09-22 12:55 UTC = 08:55 ET.
curl "http://localhost:8787/cdn-cgi/handler/scheduled?cron=55+12,13+*+*+MON-FRI&time=1790081700000"
```

After it runs for real, check Worker → Observability → Logs for
`dispatched desk.yml`. A 401 means the token expired.
