# dispatch

Triggers the GitHub Actions workflows on a clock that keeps time. GitHub's
`schedule` event ran 4-6 hours late on this repo, every day; `workflow_dispatch`
starts in seconds. So the clock lives here and GitHub only supplies the runner.

| Trigger | Desk (`desk.yml`) | Weekend (`weekend.yml`) |
|---|---|---|
| Cloudflare Worker cron (primary) | 08:55 ET, Mon-Fri | 13:50 ET, Fri |
| systemd user timer (backup) | 09:00 ET, Mon-Fri | 14:50 ET, Fri |

Each workflow has a target (desk: 25 min before the open, 09:05 ET; weekend:
10 min before the close) and holds its runner until then. The desk's primary
dispatch now sits 10 min ahead of that target rather than 2h, and the backup
5 min ahead of it rather than 1h. Both holds are short enough that a runner is
never tied up for long, and the session still finishes before the bell.

Both call `workflow_dispatch` with `dry_run=false`. Whichever lands second queues
behind the `trading-desk` concurrency group and exits on the workflow's
already-ran check. It waits in the queue without holding a runner, so a
duplicate costs a few seconds of runner time.

The workflows' `dry_run` input defaults to `true`, so anything else that
dispatches them must pass `dry_run=false` explicitly or it will never trade.

Passing it is not enough on its own. A `type: boolean` input arrives as a real
boolean from the Actions tab, but as the **string** `"false"` from the dispatch
API - which is what both triggers here use, and what `gh workflow run -f` sends.
A bare `${{ inputs.dry_run }}` is truthy for that string, so every dispatched
run came out a dry run while manual ones traded. The workflows compare against
both forms; do not simplify that expression.

## Tokens

Create **two** fine-grained PATs (GitHub → Settings → Developer settings →
Fine-grained tokens), one per trigger, so one expiring or leaking does not take
out both:

- Repository access: only `claude-portfolio`
- Permissions: **Actions: Read and write**
- Set an expiry and a calendar reminder a week before it.

Anyone holding either token can start a live session. The already-ran marker
and the pre-market guard cap that at one session per day inside the window.

## Cloudflare Worker

Cron Triggers work on the Workers free plan (5 per account; this uses 2).
Cloudflare cron is UTC-only, so each cron lists both the EDT and EST hour and
`src/index.ts` dispatches only on the one matching New York time.

```sh
cd dispatch
npm install
npx wrangler login
npx wrangler secret put GH_TOKEN     # first PAT
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
curl "http://localhost:8787/cdn-cgi/handler/scheduled?cron=55+12,13+*+*+1-5&time=1790081700000"
```

After it runs for real, check Worker → Observability → Logs for
`dispatched desk.yml`. A 401 means the token expired.

## systemd backup

```sh
mkdir -p ~/.config/daytrade ~/.config/systemd/user
printf 'GH_TOKEN=%s\n' 'github_pat_...' > ~/.config/daytrade/dispatch.env   # second PAT
chmod 600 ~/.config/daytrade/dispatch.env
cp systemd/* ~/.config/systemd/user/
loginctl enable-linger "$USER"      # fire even when logged out
systemctl --user daemon-reload
systemctl --user enable --now daytrade-desk.timer daytrade-weekend.timer
systemctl --user list-timers 'daytrade-*'
```

`systemctl --user start daytrade-dispatch@desk.service` sends a **live**
dispatch. To test the token without trading:

```sh
env $(cat ~/.config/daytrade/dispatch.env) \
  gh workflow run desk.yml --repo ConnorHampstead/claude-portfolio -f dry_run=true
```

Firing history: `journalctl --user -u 'daytrade-dispatch@*'`.

A user timer does not wake a suspended machine. `Persistent=true` fires on
resume instead; if that is after the window, the workflow's guard stands down.
