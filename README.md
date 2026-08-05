# Paper Trading Desk — Alpaca Harness

<!-- PERFORMANCE:START -->

*The performance chart appears here after the first session.*

<!-- PERFORMANCE:END -->


Takes the JSON block from Claude's morning brief, enforces the risk rules, sizes
positions from the stop, submits bracket orders to an Alpaca **paper** account,
and logs everything so you can score both P&L and calibration afterwards.

Nothing in here can touch real money: it only ever talks to
`paper-api.alpaca.markets`, and every command is read-only unless you pass
`--confirm`.

---

## 1. Setup

**Account.** Sign up at [alpaca.markets](https://alpaca.markets) — a paper-only
account needs just an email address. Once in, switch the dashboard to **Paper
Trading** (top-left toggle), then generate an API key pair. The secret is shown
exactly once.

While you're there, open the paper account settings and set the starting balance
to **$100,000** to match the system prompt. Leave the account type as margin even
though the prompt specifies no leverage — shorting requires it, and the harness
enforces the cash-like constraints itself.

**Install.**

```bash
pip install -r requirements.txt

export ALPACA_API_KEY_ID='PK...'
export ALPACA_API_SECRET_KEY='...'
```

Put those two exports in your `~/.zshrc` or `~/.bashrc` so they persist. Keys
beginning `PK` are paper keys; live keys begin `AK`. If you ever see an `AK` key
here, stop and regenerate.

**Verify.**

```bash
python3 desk.py status
python3 desk.py check example-plays.json
```

The second command should reject the example's stale AAPL level with a warning
about distance from the last price — that's the sanity check working.

---

## 2. Daily workflow

**Morning (Stockholm time, before 15:30).** Ask Claude for the brief. It returns
prose plus a fenced `json` block. Save the whole reply — the parser finds the JSON
inside markdown fences, so you can paste the entire response verbatim:

```bash
pbpaste > briefs/2026-08-05.md          # macOS
# or just save the reply from the Claude app
python3 desk.py check briefs/2026-08-05.md
```

`check` sends nothing. It prints each play with the derived share count, the
dollar risk, the reward:risk ratio, and any rule violations. Read this before
submitting — it's where hallucinated price levels get caught.

**Submit.**

```bash
python3 desk.py submit briefs/2026-08-05.md --confirm
```

Each play goes in as a bracket order: entry, plus an attached take-profit and
stop-loss that execute unattended. This is the point of the Alpaca route — you're
asleep or at work for most of the US session and the exits still happen.

**Evening or next morning.**

```bash
python3 desk.py reconcile     # pulls fills, computes R multiples
python3 desk.py score         # performance + calibration report
python3 desk.py status        # current book
```

**Weekly.**

```bash
python3 desk.py stale           # entry orders that never filled
python3 desk.py stale --confirm # cancel them
```

Unfilled GTC limit orders accumulate and will fill weeks later on an unrelated
move, wrecking your attribution. Clear them out when the thesis has expired.

**Kill switch.** If `status` reports the daily loss limit breached:

```bash
python3 desk.py flatten --confirm
```

---

## 3. How sizing works

You never specify position size; Claude never specifies position size. The
harness derives it:

```
shares = floor( (equity × risk_per_trade_pct) / |entry − stop| )
```

At $100k equity and 1% risk, a $5-wide stop gives 200 shares — $1,000 at risk
regardless of the share price. This removes an entire class of arithmetic error
from the model and makes rule 1 structural rather than advisory.

The consequence worth understanding: **tight stops produce large notionals.** A
2% stop at 1% risk is a 50% position. That's correct stop-based sizing, not a
bug, but it's why `max_position_pct` and `max_gross_exposure_pct` exist as
backstops. If a play needs more than half the account's notional to express 1% of
risk, the stop is too tight for the timeframe and the harness rejects it.

---

## 4. Rules enforced

Per play — bad geometry (stop on the wrong side of entry, target inside the
stop), untradable or unshortable symbols, entry levels more than 10% from the
last traded price, sizing below one share, single-name notional over 50% of
equity, and malformed or missing probabilities.

Across the book — max 5 concurrent positions, gross exposure ≤ 100% of equity,
no duplicate symbols in one brief, no adding to a name already held, and the 3%
daily loss limit, which blocks all new submissions once breached.

Edit `config.json` to change any of these. Change them between runs, not
mid-experiment.

---

## 5. Reading the score report

`score` gives the usual performance stats, then the part that matters:

```
CALIBRATION   5 trades with a stated probability
stated           n   mean said    actual
50%-60%          1        55%      100%
70%-80%          2        76%        0%  <-- overconfident
Brier score     0.427   (0.25 = coin flip)
```

Sorted by what Claude *said* would happen against what *did*. Systematic
overconfidence shows up here in twenty trades, long before P&L says anything
reliable. A Brier score above 0.25 means the stated probabilities are worse than
a coin flip and the model's conviction carries no information.

The `thesis_verdict` column in `journal.csv` is deliberately left blank for you to
fill in by hand, with one of: `right thesis right outcome`, `right thesis wrong
outcome`, `wrong thesis right outcome`, `wrong thesis wrong outcome`. No script
can judge this, and the third category — profitable trades for reasons that
weren't real — is the one that will fool you if you only watch the equity curve.

---

## 6. Known limitations

**Data feed.** Free Alpaca accounts get the IEX feed, which is a single venue
carrying a small slice of consolidated volume. Quotes can differ from what you see
on a consolidated chart, especially for less liquid names. Set `"data_feed":
"sip"` in `config.json` if you subscribe to the paid feed. This affects the
harness's price sanity check, not order fills.

**Fills are optimistic.** Alpaca simulates against real-time quotes, which is
better than mid-price backtesting but still doesn't model queue position, partial
fills on size, or gap-throughs on your stop. Expect the paper equity curve to
flatter the strategy.

**Pattern day trading.** Paper accounts simulate the PDT rule. Starting at $100k
you're clear, but if equity falls below $25,000 you'll be blocked from more than
three day trades in five sessions.

**No options, no corporate actions.** Splits and dividends don't process in paper
accounts, so anything held across an ex-date will look wrong.

**Timezone.** Alpaca timestamps are UTC; the US cash session is 15:30–22:00
Stockholm time (14:30–21:00 during the spring and autumn DST gaps, when the US and
EU shift on different dates). Bracket orders submitted while the market is closed
queue until the open, and market-type entries will fill at the opening auction
price — which on a gap is nowhere near where Claude thought it was entering. Prefer
`"entry_type": "limit"` for anything submitted overnight.

---

## 7. Files

| File | Purpose |
|---|---|
| `desk.py` | The harness. All commands. |
| `config.json` | Risk limits. Edit here, not in code. |
| `prompt-addendum.md` | Append to your system prompt so Claude emits parseable JSON. |
| `example-plays.json` | Shape reference; use with `check` to test setup. |
| `journal.csv` | Created on first submit. Your permanent decision record. |

Back up `journal.csv`. It's the experiment.

---

## 8. Running it unattended (GitHub Actions)

The repo ships a workflow that runs the whole session on a weekday schedule with
no machine of yours switched on. It reconciles yesterday, pulls live account
state, asks Claude for a brief, validates it, submits what passes, and commits
the brief, the validation output, and the updated journal back to the repo.

### Secrets

Repository Settings → Secrets and variables → Actions:

| Secret | Value |
|---|---|
| `ALPACA_API_KEY_ID` | Your paper key (`PK...`) |
| `ALPACA_API_SECRET_KEY` | Your paper secret |
| `CLAUDE_CODE_OAUTH_TOKEN` | Run `claude setup-token` locally and paste the result |

`claude setup-token` produces a long-lived token that authenticates against your
Pro subscription — no API key and no per-token billing. It's valid for about a
year, so put a calendar reminder to regenerate it.

To use API billing instead, swap the secret for `ANTHROPIC_API_KEY` and change the
env block in `.github/workflows/desk.yml` to match.

### Schedule

`cron: '0 12 * * 1-5'` — 12:00 UTC, weekdays. That's 14:00 Stockholm in summer and
13:00 in winter, both comfortably before the US open. Cron is always UTC, and
GitHub delays scheduled runs by 5–30 minutes under load, which is why the slot
sits well clear of the open rather than tight against it.

`workflow_dispatch` is also enabled, so you can trigger a run by hand from the
Actions tab. **Do that first**, before trusting the schedule — it's the fastest
way to find a missing secret.

### What each run commits

```
briefs/2026-08-05.md          full prose brief + JSON block
briefs/2026-08-05.check.txt   validation: what was approved, what was rejected, why
briefs/2026-08-05.submit.txt  what actually reached the account
journal.csv                   updated with fills and R multiples
state/                        book state, score, heartbeat
```

The brief is committed **before** outcomes are known. That timestamp is the whole
value of running this in public — it's a preregistration you can't quietly revise.
Don't rewrite history in this repo, even to fix a typo in a thesis.

### Failure modes to watch

The heartbeat file is written on every run, trading day or not, so the daily
commit keeps GitHub's 60-day inactivity auto-disable from silently killing the
schedule during a quiet stretch.

The `calendar` guard checks Alpaca's market calendar and stands the session down
on US holidays, so you won't get briefs written into a closed market.

The failure worth actually watching for is **silent search failure**. If
`WebSearch` stops working in CI, you won't get an error — you'll get a confident
brief written from stale training data. The signature is a sudden run of sessions
where every play is rejected for being too far from the last traded price. If you
see that in `check.txt` several days running, the model is working blind.

Set up email notification for failed workflow runs (GitHub Settings →
Notifications → Actions). A run that dies at 12:00 UTC while you're on holiday is
otherwise invisible until you come back.

---

## 9. The performance chart

`desk.py chart --update-readme` snapshots equity, redraws the curve, and rewrites
the block between the `PERFORMANCE` markers at the top of this file. It runs at
the end of every session, so the chart in the README is never more than a day
stale.

Equity comes from Alpaca's portfolio history endpoint, which is daily
mark-to-market including open positions — so the curve reflects unrealised P&L,
not just closed trades. A local copy is also appended to `state/equity.csv` each
run, which is what the chart falls back to if the endpoint is unavailable, and
what the average-exposure figure is computed from.

The benchmark is SPY, split- and dividend-adjusted, normalised to the same
starting value.

### Reading it honestly

**The comparison is not like-for-like, and the exposure row is what tells you
so.** The desk holds at most five positions and is frequently in cash; SPY is
100% invested at all times. If the desk returns half of SPY at a third of the
exposure, that is not underperformance — it's less risk taken. If it matches SPY
while fully invested, that's just beta, and you could have had it for free.

This is why the chart carries a **PRELIMINARY** watermark until 30 sessions and
20 closed trades. A rising line over three weeks is noise that happens to look
like skill, and a chart is far more persuasive than the number of samples behind
it justifies. The watermark disappears on its own once the sample supports
looking at it.

Even then, the equity curve is the *last* thing that becomes informative. The
calibration table in `desk.py score` tells you whether the model knows what it
knows, and it starts meaning something around twenty trades — long before the
P&L does.