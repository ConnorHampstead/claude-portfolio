# Paper Trading Desk — Alpaca Harness

<!-- PERFORMANCE:START -->

![Performance](state/performance.png)

| | Desk | SPY buy & hold |
|---|---|---|
| Return | +2.17% | +0.15% |
| Max drawdown | -1.57% | -3.06% |
| Avg. gross exposure | 17% | 100% |

*36 sessions, 4 closed trades, updated 2026-09-23.*

The desk holds cash most of the time and SPY does not, so this is not a like-for-like comparison — read it alongside the exposure row rather than as a scoreboard. SPY is dividend- and split-adjusted.

**Sample is far too small to mean anything.** At this length the curve is dominated by noise; a rising line is not evidence of edge. See the calibration table for a measure that becomes informative sooner.

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
pip install --require-hashes -r requirements.txt

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

**Managing positions already open.** `plays` only opens new positions. To move a
stop, lift a target, or exit early, the brief's JSON block carries a `manage`
array alongside `plays`:

```json
"manage": [
  {"ticker": "LLY", "action": "update", "stop": 1242.00, "target": 1293.00,
   "reason": "Thesis matured; trailing the stop above entry to lock the gain."}
]
```

`check` prints the old level next to the new one; `submit --confirm` replaces the
live exit orders on Alpaca (creating them if the position has none) and writes the
new levels back to `journal.csv`. `"action": "close"` cancels the resting orders
and exits at market instead.

Two things this deliberately does *not* do. It does not act on the prose brief —
section 3 saying "raise the stop to 1242" moves nothing on its own, so the model
is instructed to write both. And `no_trade: true` does not suppress it: standing
down means opening nothing new, not leaving open risk unmanaged. Rule 1 still
applies, so widening a stop past 1% entry-to-stop risk is rejected; tightening
one always passes.

**Evening or next morning.**

```bash
python3 desk.py reconcile     # pulls fills, computes R multiples
python3 desk.py score         # performance + calibration report
python3 desk.py status        # current book
```

**Weekly.** Handled automatically once CI is running — the daily session cancels
entries older than 5 days, and the Friday job clears the rest before the weekend
(see section 10). To do it by hand:

```bash
python3 desk.py stale --older-than 5           # list
python3 desk.py stale --older-than 5 --confirm # cancel
```

Unfilled GTC limit orders otherwise accumulate and fill weeks later on an
unrelated move, wrecking your attribution.

**Kill switch.** If `status` reports the daily loss limit breached:

```bash
python3 desk.py flatten --confirm
```

---

## 3. How sizing works

You never specify position size; Claude never specifies position size. Claude
picks a risk tier per play (`risk_pct`: 1.0 core, 0.5 half, 0.25 probe) and the
harness derives the size from it:

```
shares = floor( (equity × risk_pct) / |entry − stop| )
```

At $100k equity and 1% risk, a $5-wide stop gives 200 shares — $1,000 at risk
regardless of the share price. This removes an entire class of arithmetic error
from the model and makes rule 1 structural rather than advisory. `risk_pct` above
`risk_per_trade_pct` is cut to it; omitted, it defaults to it. The smaller tiers
exist so the model can put a lower-conviction view on as a small scored position
instead of passing on it, and so that rule 8's "halve size into the event" is
something it can actually do.

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

Across the book — max 8 positions, gross exposure ≤ 150% of equity, net
exposure within ±100%, total risk at stake (entry to stop) ≤ 4% of equity, one
position per name (no adding to a name already held or resting, no duplicates in
one brief), and the 3% daily loss limit, which blocks all new submissions once
breached. Entries still resting unfilled count towards every one of these as if
they had filled.

Plays are admitted highest conviction first. A play that would breach a cap is
dropped on its own; the plays behind it are still considered, so a small probe
can go in where a full-size trade did not fit. `prep` tells the model how much
room is left, including how tight a stop the remaining gross and net room allow,
since it never sees the notional its own plays will carry.

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

Sorted by what Claude *said* would happen against what *did*. The statement
was about the target and stop the play was submitted with, so that is what it is
scored against: `stop_initial` and `target_initial` in the journal, not the live
levels `manage` may have moved since. When the levels were moved and the exit
does not show which initial level price reached first, the trade still counts for
P&L and R but is left out of calibration, and `score` says how many. Systematic
overconfidence shows up here in twenty trades, long before P&L says anything
reliable. A Brier score above 0.25 means the stated probabilities are worse than
a coin flip and the model's conviction carries no information.

The `thesis_verdict` column in `journal.csv` is deliberately left blank for you to
fill in by hand, with one of: `right thesis right outcome`, `right thesis wrong
outcome`, `wrong thesis right outcome`, `wrong thesis wrong outcome`. No script
can judge this, and the third category — profitable trades for reasons that
weren't real — is the one that will fool you if you only watch the equity curve.

### The shadow book

A trade that is never taken can never be wrong on the record, which makes
standing aside free and pushes the model towards it. So the brief puts every
idea it passes on with real levels in a `passed` array, and plays the caps drop
are added automatically. `desk.py shadow` (run at the start of every session)
replays each one against five-minute bars as if its bracket had been live: the
entry fills at its level, or at the bar's open on a gap through it, and the
exits the same way, over at most 5 sessions for the entry and 10 in total.
Where one bar holds both levels the order cannot be read and the idea is marked
ambiguous rather than guessed. Bars are consolidated (SIP) history, which the
free plan serves once it is 15 minutes old, falling back to IEX.

`score` reports the shadow book next to the real trades, with its own
calibration table and one combined with the trades; `prep` shows the model how
its recent passes turned out. Two things to read from it: calibration fills up
several times faster than from trades alone, and a shadow book that out-earns
the trades actually taken says the filter is turning down the better ideas.

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
| `prompts/system.md` | System prompt: rules, brief format, JSON schema. |
| `prompts/daily-request.md` | The pre-market request, followed by the book state. |
| `prompts/open-request.md` | The post-open request, followed by the morning brief and the book state. |
| `example-plays.json` | Shape reference; use with `check` to test setup. |
| `journal.csv` | Created on first submit. Your permanent decision record. |
| `shadow.csv` | Ideas passed on with levels, and plays the caps dropped, replayed against the tape. |

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

GitHub's own `schedule` trigger is not used. On this repo it fired 4-6 hours
late every day, which put every scheduled session past the open. The workflows
are started by `workflow_dispatch` from [`dispatch/`](dispatch/README.md)
instead, which begins within seconds:

- **Cloudflare Worker cron** (primary): the pre-market brief at 08:55 ET and the
  post-open review at 09:55 ET weekdays, weekend cleanup at 13:50 ET Fridays -
  10 min, 10 min and 2h ahead of each job's target.
- **systemd user timer** (backup): 09:00, 10:00 and 14:50 ET - 5 min, 5 min and
  1h ahead.

Both desk sessions run `desk.yml`, told apart by its `session` input. The
pre-market brief holds until 25 minutes before the open, derived from Alpaca's
calendar, and the guard (`calendar --before-open 5`) stands it down rather than
write a "pre-market" brief with the market already trading. The post-open
review holds until 35 minutes after the open, once the 10:00 ET releases are out
and the opening range has formed, and its guard (`calendar --open-window 30
120`) stands it down outside that stretch. A missed session costs one data
point; an inconsistent information set costs the comparability of the whole
record.

The review reads the morning's brief, sees the fills and the open, and can
manage, cancel and open positions under the same rules. After it nothing looks
at the book until the next morning.

The model is pinned (`DESK_MODEL` in `desk.yml`, `claude-opus-5-5`), not the
`opus` alias, and every journal and shadow row records it. Changing it is a
change to the experiment: note it in section 11.

Duplicate triggers are harmless. They queue behind the `trading-desk`
concurrency group and exit on `briefs/<date>.submit.txt` (or
`briefs/<date>-open.submit.txt` for the review), which is written only after a
real submit. Dry runs don't create it. To force a re-run, delete that file.

`workflow_dispatch` also lets you trigger a run by hand from the Actions tab
(dry run by default). **Do that first**, before trusting the dispatchers - it's
the fastest way to find a missing secret.

### What each run commits

```
briefs/2026-08-05.md          full prose brief + JSON block
briefs/2026-08-05.check.txt   validation: what was approved, what was rejected, why
briefs/2026-08-05.submit.txt  what actually reached the account
briefs/2026-08-05-open.*      the same three for the post-open review
journal.csv                   updated with fills and R multiples
shadow.csv                    passed ideas and dropped plays, replayed and scored
state/                        book state, request, score
```

The brief is committed **before** outcomes are known. That timestamp is the whole
value of running this in public — it's a preregistration you can't quietly revise.
Don't rewrite history in this repo, even to fix a typo in a thesis.

### Failure modes to watch

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

---

## 10. Weekend cleanup (`.github/workflows/weekend.yml`)

A second workflow runs Fridays at 19:00 UTC — an hour before the US close in
summer, two in winter — and cancels **every** unfilled entry order, regardless of
age.

This is a deliberately different policy from the daily session, which only
cancels entries older than the 5-day holding horizon. The weekend case is
specific: an order resting from Friday can fill on Monday's open into a thesis
written before two days of news it never saw. The price gets honoured; the
reasoning behind it doesn't. Cancelling and letting Monday's brief re-propose the
idea, if it still holds, keeps every filled trade tied to reasoning that was
current when it filled.

It shares a `concurrency` group with the daily session, so the two can never run
simultaneously. `workflow_dispatch` defaults to a dry run that lists what would
be cancelled without touching anything.

If you'd rather let entries survive the weekend, delete the file. The daily
age-based cleanup is independent.

### Never-filled entries

Cancelling raises a question the journal has to answer: what is a play that was
proposed but never entered?

It's a prediction that didn't become a trade. `reconcile` now marks these with
`exit_reason = "never filled"` so they don't sit in the journal looking like open
positions, and they're excluded from win rate, expectancy, and calibration — you
cannot score whether price hit a target from an entry you never took.

But the *rate* is worth watching, so `score` reports it:

```
Entry fill rate  33%  (1 filled / 3 proposed, 2 never reached)
```

A low fill rate is diagnostic in a way the P&L isn't. It means the entry levels
are being set somewhere price doesn't go — too far below the market on longs,
waiting for pullbacks that never come. That's a fixable flaw in how the model
picks levels, and it's entirely invisible if you only look at the trades that
did fill.

---

## 11. Changes to the experiment

Changes to the prompt, the rules or the harness make sessions before and after
them different experiments. They are listed here by the first session they
apply to, so the record can be read in segments.

**2026-09-23**

- *Timing.* Since 2026-08-18 the brief has run at 09:05 ET, but the request still
  told the model it was writing before the 08:30 ET releases, and it discarded
  prints it found as a result (CPI on 2026-09-11). `prep` now states the current
  time and that anything scheduled before it has printed.
- *Rule 8* now covers the company's own binaries only. Macro releases, FOMC and
  other companies' earnings are ambient risk, handled with stop and tier. It had
  been read as covering any macro event inside five days, which is nearly always.
- *Risk tiers* (`risk_pct` 1.0 / 0.5 / 0.25), gross 150% with net ±100%, total
  open risk ≤ 4%, 8 slots, admission by conviction. Previously 1% flat, gross
  100%, 5 slots, and one cap breach blocked every new play in the brief.
- *Prompt.* Both sides named every session; conditional plans are placed as
  orders, or left for the post-open review with their levels; standing aside is
  no longer framed as the default-correct answer; the account is described as
  margin, not cash.
- *Scoring fix.* `reconcile` missed any exit that `manage` had replaced or
  re-placed, and measured R against the live stop instead of the one submitted.
  LLY (2026-08-05, stopped at about 1229.76 on 2026-08-25, about +1.76R) was
  missing from the record the model was shown each morning, which read 0W/2L.
- *Model pinned* to `claude-opus-5-5` (previously the `opus` alias, which
  resolved to whatever the pinned CLI version shipped with). Journal rows now
  record `model` and `session`.
- *Market data.* `prep` appends an Alpaca table to the book state: last trade,
  prior close, ATR, 20/50-day averages, 20-day range and 5-day change for held
  and resting names, a watchlist (`config.json`), and the day's movers filtered to
  the tradable universe. Until now the model found every price by web search.
- *Shadow book.* Passed ideas and dropped plays are replayed and scored
  (section 5).
- *Post-open review.* A second session at 10:05 ET (section 8). Before this the
  brief was the only decision point, and 19 of 24 no-trade briefs deferred their
  decision to "after the open or the data", which nothing ever acted on.
- *Stop entries past their trigger* (from the 2026-09-23 run). A sell stop at
  BAC 55.90 was refused because pre-market had already traded 55.885; the run
  failed and the prompt had wrongly said such an order fires at the open. It is
  now recorded as not placed, scored in the shadow book and shown to the
  post-open review. The market table's last price now also comes from the
  consolidated tape 15 minutes delayed (free on the basic plan) when that is
  more recent than the IEX print, which is thin before the open, and the movers
  screener is labelled when it is still the previous session's.

**2026-09-24 - nothing executed**

Both sessions ran and wrote briefs, but `check` crashed before submitting (a
timestamp-parsing bug from the 2026-09-23 changes), so none of that day's plays
or `manage` instructions reached Alpaca. The briefs stay in the record as
written. Fixed the same day. The book state had also been reporting filled
brackets' stops as "no live order": Alpaca holds a bracket's stop leg while the
take-profit works, and the open-orders list does not return it, so missing legs
are now looked up on the entry order.
