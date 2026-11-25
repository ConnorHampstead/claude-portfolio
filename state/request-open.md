Produce the post-open review.

The cash session has been open for about 35 minutes. This morning's pre-market
brief is below, followed by the live book and market data, which now include
today's opening prices. This is the second and last decision point of the day:
after this review, nothing looks at the book until tomorrow's pre-market brief.

What this session is for:

- **Fills at the open.** Check every entry that filled since the morning. An
  entry that filled on a gap through its limit sits closer to its stop than
  planned: it risks less than it was sized for, which is not a reason to close
  it. Close it through `manage` only if what caused the gap is the invalidation
  you wrote this morning. Otherwise its bracket stands.
- **Open positions.** The same test as the morning: closed only on the recorded
  invalidation, its own binary event before tomorrow's brief, or its tenth
  session. No stop is tightened.
- **The morning's plans for this review.** The 08:30 and 10:00 ET data have
  printed and the opening range is set. For each thing the morning brief said it
  would decide after the open or after the data, decide now: act, or say why not.
- **Resting entries** the open has made stale: amend or cancel them.
- **New plays**, under the same rules as the morning, pass-2 research
  included. Orders now go into a trading market: a limit at or through the last
  price fills immediately, and a `market` entry is sized from the last price.

Do not re-trade the morning's reasoning without new information. Reversing a
morning call needs something that happened since it was written: a print, a
headline, or what the open did. Everything in the morning's rules still binds:
search before you write, verified prices only (the market data table counts),
prose alone moves nothing, risk tiers, caps. If the morning's plan stands
unchanged, say so in a few lines and emit the JSON with empty arrays.

Keep the review short:

### 1. Since the open
Two or three sentences: what printed, how the market opened, and what changed
versus the morning brief.

### 2. Fills, positions and resting entries
Each position: keep, or close and which of the three conditions applies. Each
resting entry: keep, amend or cancel, and why.

### 3. The morning's plans
Each plan the morning left for this review: acted on, not triggered, or dropped.
One line each.

### 4. New plays
The same table as the pre-market brief.

### 5. Passing on
One line each. Ideas with real levels also go in the `passed` array, where they
are scored.

### 6. For tomorrow
Any level or condition you would act on tomorrow. Tomorrow's pre-market brief is
shown this review. "None" is fine.

Then the JSON block, in the same schema as the morning.

Your probability estimates are scored against outcomes, on the bracket as you
submit it. Start from the base rate in "Your record" and move off it only for
reasons you name.

## What the record has shown so far

*As of 2026-11-09, 45 closed trades. Merged by the operator from the reviews. The
samples are small: each line is the working assumption, not a settled finding,
and "Your record" in the book state has the current figures.*

- **Managing positions has cost money.** Left alone, the 45 brackets would have
  made about 5R. As managed they made under 2R: moved stops gave up about 2.4R
  over 11 trades and closes by hand about 1.7R over 9. Hence the default of
  leaving the bracket as submitted.
- **Your probabilities have not told good ideas from bad.** Almost all sat
  between 0.30 and 0.47, on average exactly at breakeven for the reward:risk
  stated, and scored no better than saying the base rate every time (about 42%
  of 116 brackets reached target first). Start from the base rate.
- **Small probes did not pay.** Conviction-2 plays averaged -0.15R over 18
  trades and took slots, while the ideas you passed on averaged +0.10R over 80.
  Low-conviction ideas are now scored in the shadow book instead of traded.

## This morning's pre-market brief

I've finished the research and am writing the brief: one QQQ breakdown short at half risk, and six other ideas logged with levels as passes.

# Pre-market brief: Wednesday 2026-11-25

*Written 09:05 ET (15:05 Stockholm, ET+6). The cash session opens 09:30 ET (15:30 Stockholm). Markets are closed Thursday for Thanksgiving, and Friday closes early at 13:00 ET (19:00 Stockholm). Resting entries are cleared before the holiday, so anything placed today has to fill today.*

**Today's call:** one new order, a QQQ short that only triggers if QQQ breaks below its 20-day low. No other idea clears positive expected value on my own numbers. The book is flat; HD stopped out yesterday at −1.01R.

## 1. Tape

**The AI selloff deepened overnight and spread.**
- **Asia:** Taiwan's benchmark fell about 5–8% (sources differ), KOSPI −5 to −6%, Tokyo Electron −12.5%.
- **Credit stress on AI spending:**
  - WSJ reports wider tech credit spreads and higher costs to insure tech debt (via BigGo).
  - Mizuho cut its 2027 and 2028 AI capex forecasts.
  - BNP Exane downgraded MU and cut its target 54%.
- **US futures at about 07:20 ET:** Nasdaq-100 −3.0%, S&P 500 −2.0%, Dow −1.3%.
- **At 09:04:** QQQ 616.98 (−3.3%), SPY 704.39 (−2.0%), SMH −5.1%, NVDA −6.5%, MU −9%.
- **VIX:** 30.76, up from 26.36.

**Two dated items landed this morning:**
1. **Tariffs.** The US proposed Section 301 "excess capacity" tariffs on 14 trading partners, including China, the EU, Japan, Korea, Taiwan and India.
   - China gets an extra 20% on top of the 2018 duties.
   - A hearing comes first, and the tariffs may not take effect until January (CNBC).
2. **Inflation.** October core PCE was 3.3% y/y against 3.2% expected. Headline was in line at 3.8%.

**The rate backdrop gives equities no cushion:**
- CME FedWatch (via Reuters) shows a 97% chance of a December hike and 63% for January.
- The 10-year closed Tuesday at 4.90%.
- TLT is +1.0% on haven demand.
- Gold is at a 15-month low (GLD −2.3%).

**Breadth is defensive.** Staples (XLP +0.5%, WMT and COST at 20-day highs) and energy are flat to green; everything else is red. Deutsche Bank's Reid calls it "rotation rather than indiscriminate selloff".

**Regime:** a risk-off trend led by tech, with the Fed hiking into an AI-capex bust. **The edge is short**, but QQQ is already 0.87 ATR down at the open, so the place to short is a break below the 20-day low, not the open.

## 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Oct PCE | Headline +0.3% m/m, 3.8% y/y (in line). **Core +0.3% m/m, 3.3% y/y vs 3.2%**. Futures held their losses. | QQQ short |
| 08:30 | 14:30 | Oct personal income / spending | Income +0.7% (tied to Medicare rebates). Nominal spending +0.3%, real about flat. Saving rate 4.1% (from 3.6%). | Macro |
| 08:30 | 14:30 | Q3 GDP, second estimate | **4.3%** (advance estimate was 3.4%). Gross domestic purchases price index revised down 0.3pp to 2.7%. | Macro |
| 08:30 | 14:30 | Initial jobless claims | **189K** vs about 200K expected (prior 202K revised) | Supports the hawkish case |
| 08:30 | 14:30 | Oct durable goods | **+0.2% vs +0.6%** | Mild miss |
| 10:00 / 10:30 | 16:00 / 16:30 | Usual pre-holiday slots (UMich final, EIA crude) | **I did not verify a schedule.** Treat as unknown. | — |
| 14:00 | 20:00 | Fed Beige Book (per Swingfolio's calendar, not confirmed elsewhere) | Narrative only | QQQ short (the trigger could fire after this) |
| Thu 11-26 | — | US markets closed | — | Holiday gap risk |
| Fri 11-27 | 13:00 close (19:00) | Half-day session | — | — |
| Dec 1 and Dec 3 | — | Huang (NVDA) congressional interviews | Company-specific | Reason for passing on NVDA |

**Earnings reported last night**, all dated 11-24 after the close. None is a play:

| Name | Pre-market | What happened |
|---|---|---|
| DELL | −7% | Beat and raised, per aggregators |
| WDAY | −6 to −7% | Beat; free cash flow missed |
| ADSK | −5% | Beat and raised |
| HPQ | Table shows +3.4%; Investing.com reports a decline | Beat; FY27 EPS guide $3.15–3.45 vs about $3.17–3.18 consensus |
| URBN | −12 to −13% | Comps +4.4% vs 5.3% expected |
| AMBA | −33% | Guide cut |
| NTNX | −14% | CEO to step down |

## 3. Open positions and resting entries

- **Open positions: none.** HD's stop at 353.50 filled for −1.01R. The record shows that result as it happened, and I'm not revisiting it.
- **Resting entries: none.**

## 4. New plays

### QQQ short (breakdown trigger)

| Field | Value |
|---|---|
| Ticker | QQQ |
| Direction | Short |
| Catalyst | Three dated items, all from 2026-11-25: (1) the USTR's Section 301 tariff proposal on 14 partners, including Taiwan, Korea and Japan, the chip supply chain (CNBC); (2) October core PCE at 3.3% vs 3.2%, with a December hike about 97% priced (CNBC, Swingfolio/Reuters FedWatch); (3) the overnight Asian chip crash, wider tech credit spreads (WSJ via BigGo) and Mizuho's capex cut. |
| Thesis | QQQ is −15% from its 726.14 20-day high and the Fed is hiking into it, so there is no policy backstop. A break below the 606.23 20-day low means the bounce from Monday's NVDA spike has fully failed. Under tighter credit, the next leg is mechanical de-risking of AI exposure. |
| Entry | **Sell stop 604.00.** That is below the 20-day low of 606.23; pre-market is 616.98, so the trigger is beyond the market. |
| Stop | **628.50.** That is 24.5 points, about 1.0 ATR (24.36). A move back above about 628 means the breakdown was rejected and the gap is more than half filled, so the thesis is wrong. |
| Target | **555.00**, 49 points, **2.0R** |
| Risk tier | **0.5%**: conviction 3, a breakdown entry after a two-day drop of about 5% in QQQ, and the stock market is shut Thursday. |
| Time horizon | 2–7 sessions |
| Next earnings | n/a (ETF). Not an event trade. |
| Conviction | 3 |
| P(target before stop) | **0.35** |
| Invalidation | CME FedWatch December hike probability drops below 60% (from about 97%), or the USTR withdraws or suspends the Section 301 proposal. |
| What I'd be wrong about | VIX at 31 after a 15% drawdown is where bear-market rallies start; NVDA's +31% on Monday shows how hard this tape squeezes. Shorts often cover before a holiday, and a breakdown entry fills after much of the move. |

**How I got to 0.35:**
- My base rate is 38% across 167 brackets, which have averaged about 1.6–1.8R. A 2R bracket on a random walk starts nearer 0.33.
- Adding about +0.02: the fresh catalysts all point the same way, and the trend is confirmed (−9.9% vs the 50-day average, VIX rising).
- Holding it there: the pre-holiday seasonal bias and how stretched QQQ already is.
- The 35–40% bucket in my record has hit only 30% (84 ideas), so I'm not going higher.

**Value:** 0.35 × 2.0 − 0.65 = **+0.05R**. That is thin but positive, so it's taken at the smaller tier. If the trigger doesn't fire today, the harness clears it before the holiday and nothing is lost.

## 5. Both sides

- **Best short:** the QQQ breakdown above, taken. Sell stop 604.00 / stop 628.50 / target 555.00, P 0.35.
- **Best long:** a WMT pullback limit, passed.
  - Levels: limit 131.60 / stop 127.40 / target 140.00 (2.0R), P 0.32.
  - WMT is a defensive leader at a new 20-day high (133.15 against a 20-day high of 132.42). It beat and raised on 11-19, though press reports say the stock fell about 7% that day.
  - The catalyst is six sessions old, and WMT is already about +12.7% off its 118.11 20-day low. Any tech bounce would rotate money back out of staples.
  - Value: 0.32 × 2 − 0.68 = −0.04R. Pass.

## 6. Passing on

| Idea | Levels | P | Why I passed |
|---|---|---|---|
| WMT long | Limit 131.60 / stop 127.40 / target 140.00 | 0.32 | As above: an old catalyst, late in the rally. |
| GLD short | Limit 323.00 / stop 331.00 / target 307.00 | 0.33 | Right direction (hike pricing, a 15-month low), but −7.7% in 5 days into the widely watched $3,500 support on futures. The bounce limit is the only sensible location, and the value is still about −0.01R. |
| NVDA long | Market 145.26 / stop 127.00 / target 181.50 | 0.30 | This is the zone yesterday's review named, but company-specific binaries are stacked up: Republican committee chairs' interviews with Huang in early December, the board's independent investigation, and Trump's talk of a government stake and a pardon. Asian chips crashed overnight. A stop at 140 would be 0.3 ATR, inside noise. |
| DELL long | Market 273.64 / stop 233.00 / target 355.00 | 0.28 | Beat and raised (adjusted EPS $9.45 vs $6.59, FY revenue raised to $202B, per Swingfolio and Investing.com), but **I couldn't verify the figures at Dell's own release**. Sellers point to memory-cost pressure on margins. ATR is 13.6%, and it would be a buy against the trend in an AI unwind. |
| HPQ long | Market 28.90 / stop 27.35 / target 32.00 | 0.30 | The FY27 guide of $3.15–3.45 is only slightly above the $3.17–3.18 consensus, and the midpoint is flat year on year (FY26 included $0.15 of tariff refunds). Sources conflict on the pre-market reaction (+3.4% in the table, a decline per Investing.com). |
| ORCL short | Sell stop 99.90 / stop 109.60 / target 80.50 | 0.30 | The AI-debt poster child, but it's already −6.4% today. ATR is 7.8%, and its fiscal Q2 earnings, likely around Dec 9–10 (**not verified**), would fall inside the horizon. |

Not given levels:
- **URBN and WDAY:** I could not verify either catalyst at the source or get a current price.
- **AMBA:** −33% is fully priced.
- **Semi shorts (MU, SMH):** ATRs of 8–12% and already −5 to −9% today, so a short now would be a chase.

## 7. For the post-open review (about 10:05 ET / 16:05 Stockholm)

- **QQQ sell stop at 604:**
  - If QQQ trades **above 630 at 10:05**, the gap is being bought and the breakdown is less likely. **Cancel the entry.**
  - Between 604 and 630, leave it resting.
  - If it has filled, the bracket stands as submitted.
- **WMT:** if SPY is still down more than 1.5% at 10:05 and WMT holds above 132.42 (the old 20-day high), a long at the review with stop 127.40 and target 141 is worth re-scoring. On today's numbers it is not positive, so the default is still to pass.
- **No index long at the review** unless SPY reclaims 712 or higher (about half the gap) with VIX back under 28. Even then it would only be a note for Friday, because it conflicts with the QQQ trigger.

## 8. Book state

- **If the QQQ trigger fills:** gross about 12% (cap 150%), net about −12% (cap ±100%), tech/QQQ about −12% (cap 40%).
- **Risk at stake:** 0.50% (cap 4%), with 1 of 8 slots used. If it doesn't fill, the book stays flat.

```json
{
  "date": "2026-11-25",
  "no_trade": false,
  "session_note": "Risk-off AI unwind deepening (Asia chips crashed, QQQ -3.3% pre-market, VIX 30.8) plus Section 301 tariff proposal and core PCE 3.3% vs 3.2% with a Dec hike ~97% priced. Edge is short, but the open is a bad location at 0.87 ATR down, so the only order is a 0.5-tier QQQ breakdown trigger below the 606.23 20-day low. Defensive longs (WMT/XLP) and contrarian AI longs (DELL/NVDA) don't clear positive EV.",
  "plays": [
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "stop",
      "entry": 604.00,
      "stop": 628.50,
      "targets": [555.00],
      "time_horizon": "2-7 sessions",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.35,
      "earnings_date": null,
      "event_trade": false,
      "catalyst": "2026-11-25: USTR proposed Section 301 excess-capacity tariffs on 14 partners incl. Taiwan/Korea/Japan (CNBC); Oct core PCE 3.3% y/y vs 3.2% with Dec hike ~97% priced (CNBC, Reuters FedWatch via Swingfolio); overnight Asian chip crash, wider tech credit spreads (WSJ via BigGo), Mizuho AI capex cut.",
      "thesis": "QQQ is -15% from its 726 20-day high with the Fed hiking, so there is no policy backstop. A break of the 606.23 20-day low confirms Monday's NVDA-led bounce has fully failed. With credit tightening, the next leg is mechanical de-risking of AI exposure.",
      "invalidation": "CME FedWatch December hike probability falls below 60% (from ~97%), or USTR withdraws or suspends the Section 301 proposal.",
      "bear_case": "VIX 31 after a 15% drawdown is where bear-market rallies begin (NVDA +31% Monday); pre-holiday short covering and seasonality; a breakdown entry fills after much of the move."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "WMT",
      "direction": "long",
      "entry_type": "limit",
      "entry": 131.60,
      "stop": 127.40,
      "targets": [140.00],
      "p_target_first": 0.32,
      "reason": "Best long: defensive leader at a new 20-day high, but the catalyst (11-19 beat and raise) is 6 sessions old, it is +12.7% off the 118.11 20-day low, and a tech bounce would rotate money out. EV about -0.04R."
    },
    {
      "ticker": "GLD",
      "direction": "short",
      "entry_type": "limit",
      "entry": 323.00,
      "stop": 331.00,
      "targets": [307.00],
      "p_target_first": 0.33,
      "reason": "Right direction (hike pricing, 15-month low, below the 320.95 20-day low), but -7.7% in 5 days into the widely watched $3,500 futures support; only a bounce limit is acceptable, and EV is still about -0.01R."
    },
    {
      "ticker": "NVDA",
      "direction": "long",
      "entry_type": "market",
      "entry": 145.26,
      "stop": 127.00,
      "targets": [181.50],
      "p_target_first": 0.30,
      "reason": "In the 143-147 zone yesterday's review named, but company-specific binaries are stacked: congressional interviews with Huang in early Dec, the board's independent probe, and Trump's stake and pardon talk. Asian chips crashed overnight; ATR is 10.4%; a 140 stop is 0.3 ATR."
    },
    {
      "ticker": "DELL",
      "direction": "long",
      "entry_type": "market",
      "entry": 273.64,
      "stop": 233.00,
      "targets": [355.00],
      "p_target_first": 0.28,
      "reason": "Beat and raise (per aggregators; not verified at Dell's own release) but -7% on memory-cost margin worries; a counter-trend buy in an AI unwind with ATR at 13.6%."
    },
    {
      "ticker": "HPQ",
      "direction": "long",
      "entry_type": "market",
      "entry": 28.90,
      "stop": 27.35,
      "targets": [32.00],
      "p_target_first": 0.30,
      "reason": "FY27 EPS guide of $3.15-3.45 is only slightly above the ~$3.17-3.18 consensus, and the midpoint is flat y/y (FY26 included $0.15 of tariff refunds); sources conflict on the pre-market reaction."
    },
    {
      "ticker": "ORCL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 99.90,
      "stop": 109.60,
      "targets": [80.50],
      "p_target_first": 0.30,
      "reason": "AI-debt bellwether below its 20-day low, but already -6.4% today, ATR 7.8%, and fiscal Q2 earnings (likely around Dec 9-10, not verified) would fall inside the horizon."
    }
  ]
}
```

Sources:
- [CNBC live updates, Nov 25 (futures, PCE, tariffs, movers)](https://cnbc.com/2026/11/24/stock-market-today-live-updates-.html)
- [CNBC: US proposes Section 301 tariffs on 14 trading partners](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html)
- [Swingfolio pre-market summary, Nov 25](https://swingfolio.com/daily/us/2026-11-25/morning)
- [JournalArta: S&P futures -1.93%](https://journalarta.com/en/2026/11/25/sp-500-futures-fall-to-7078-50-as-tariff-and-ai-concerns-weigh-on-stocks/)
- [Investing.com: Nvidia, chipmakers slide; Dell falls despite outlook](https://www.investing.com/news/stock-market-news/nvidia-chipmakers-slide-premarket-dell-falls-despite-upbeat-outlook-5050581)
- [BigGo Finance: chip slide, Trump Nvidia stake talk, Asia selloff](https://finance.biggo.com/news/3666ab4b-585f-40b8-96d4-2afc2a755af8)
- [MLQ: PCE 3.8%, core 3.3%](https://mlq.ai/news/pce-inflation-rises-to-38-in-october-as-core-prices-climb-33-the-fastest-since-late-2023/)
- [The Earnings Madness: PCE prices October](https://theearningsmadness.com/news/pce-prices-october-2026)
- [IndexBox: Q3 GDP second estimate 4.3%](https://www.indexbox.io/blog/us-gdp-growth-accelerates-to-43-in-third-quarter-bea-second-estimate-shows/)
- [BEA: GDP second estimate, Q3 2026](https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-3rd-quarter-2026)
- [NVIDIA IR: board reinstates Jensen Huang](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Board-Reinstates-Jensen-Huang-as-President-CEO-and-Board-Director/default.aspx)
- [Forbes: Huang disclosed more affairs before reinstatement](https://www.forbes.com/sites/siladityaray/2026/11/24/nvidia-ceo-jensen-huang-disclosed-more-affairs-to-board-before-reinstatement-report-says/)
- [HP Inc 8-K exhibit 99.1, Q4 FY26](https://www.sec.gov/Archives/edgar/data/0000047217/000004721726000054/hp103126exhibit991q426.htm)
- [Investing.com: HP shares fall premarket on PC margin concerns](https://au.investing.com/news/earnings/hp-stock-reverses-course-after-hours-despite-quarterly-results-beat-dividend-bump-4794154)
- [Startup Fortune: HP FY27 profit forecast vs estimates](https://startupfortune.com/hp-inc-forecasts-fiscal-2027-profit-above-wall-streets-estimate-as-memory-costs-ease/)
- [Supermarket News: Walmart Q3 raise](https://www.supermarketnews.com/finance/walmart-raises-full-year-outlook-after-strong-third-quarter-sales-ecommerce-growth)
- [Nasdaq/Zacks: Walmart beats, raises, and falls 7%](https://www.nasdaq.com/articles/walmart-beats-raises-and-falls-7-heres-why)
- [Kitco PM report, Nov 24](https://www.kitco.com/news/article/2026-11-24/gold-silver-extend-losses-tech-stocks-slide-fed-inflation-test-looms-kitco)
- [TradingKey: gold near 15-month low, $3,500 test](https://www.tradingkey.com/analysis/commodities/metal/262321662-gold-hovers-near-15-month-low-ahead-us-pce-3500-test-tradingkey)
- [Fidelity: 2026 market holidays](https://www.fidelity.com/learning-center/smart-money/stock-market-holidays)
- [Heygotrade: GOOGL Nov 24](https://www.heygotrade.com/en/news/google-googl-stock-news-november-25-2026/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Wednesday 2026-11-25. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,973.84**
- Cash: $102,973.84
- Session P&L so far: +0.00% (new entries are blocked at -3.0%)
- Gross exposure: $12,684 (12% of equity, cap 150%)
- Net exposure: $-12,684 (-12%, cap +/-100%)
- Risk at stake (entry to stop): $514 (0.50% of equity, cap 4.0%) — 3.50% left for new plays
- Slots: 0 open + 1 resting entries of 8 — you may add at most 7 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

*No open positions.*

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| QQQ | short | 21 | 604.00 | stop | 628.50 | 555.00 | 2026-11-25 |

### Your record

53 closed trades: 17W / 36L, total +1.50R, net $+2,991 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 53 | 19 | 31 | +0.03R |
| The same trades, bracket left alone | 53 | | | +0.05R |
| Ideas you passed on, or the caps dropped | 131 | 48 | 73 | +0.07R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 51 | 49% |
| 35%-40% | 86 | 30% |
| 40%-45% | 27 | 48% |
| 45%-50% | 5 | 20% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 171 brackets reached target first. Your Brier score is 0.242; saying 39% every time scores 0.238. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| HD | short | stop | -1.01R | $-516 | 36% |
| GLD | short | target | +2.15R | $+1,097 | 36% |
| LOW | short | stop | -0.67R | $-343 | 37% |
| IWM | short | target | +1.67R | $+853 | 36% |
| AMZN | long | stop | -1.20R | $-303 | 36% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| QQQ | 617.73 (10:05 iex) | -3.2% | 638.10 | 617.10 / 607.74-619.32 | 24.36 (3.8%) | 606.23-726.14 | -4.9% / -9.9% | -2.9% | 61.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 704.10 (10:05 iex) | -2.0% | 718.78 | 703.19 / 695.45-704.55 | 17.65 (2.5%) | 686.75-775.64 | -3.3% / -5.2% | -1.9% | 63.0M |
| QQQ | 617.73 (10:05 iex) | -3.2% | 638.10 | 617.10 / 607.74-619.32 | 24.36 (3.8%) | 606.23-726.14 | -4.9% / -9.9% | -2.9% | 61.3M |
| IWM | 263.18 (10:05 iex) | -1.5% | 267.14 | 263.23 / 260.84-263.51 | 6.61 (2.5%) | 256.32-286.17 | -2.9% / -3.7% | -0.7% | 27.6M |
| DIA | 493.25 (10:04 iex) | -1.3% | 499.74 | 492.06 / 488.62-493.26 | 10.11 (2.0%) | 479.40-536.00 | -2.6% / -2.9% | -1.4% | 4.2M |
| TLT | 82.39 (10:05 iex) | +1.1% | 81.49 | 82.37 / 82.31-82.50 | 0.75 (0.9%) | 79.11-82.42 | +0.7% / +2.1% | +2.4% | 38.5M |
| GLD | 318.19 (10:05 iex) | -2.2% | 325.45 | 318.02 / 316.49-318.29 | 8.28 (2.5%) | 320.95-380.18 | -8.7% / -12.6% | -7.7% | 10.8M |
| USO | 139.30 (10:04 iex) | +2.9% | 135.43 | 137.78 / 137.25-139.30 | 4.69 (3.5%) | 132.28-171.82 | -7.9% / -10.1% | -3.4% | 4.8M |
| SMH | 404.77 (10:05 iex) | -5.2% | 426.75 | 402.67 / 394.82-407.15 | 34.19 (8.0%) | 396.85-571.00 | -11.8% / -21.5% | -7.2% | 13.4M |
| XLK | 151.36 (10:05 iex) | -3.6% | 157.09 | 150.86 / 148.39-151.91 | 8.05 (5.1%) | 148.09-191.55 | -7.4% / -14.4% | -3.8% | 16.5M |
| XLF | 55.67 (10:05 iex) | -0.8% | 56.11 | 55.50 / 55.34-55.66 | 1.11 (2.0%) | 54.42-60.04 | -1.9% / +0.5% | -1.7% | 42.0M |
| XLE | 60.80 (10:05 iex) | +0.6% | 60.45 | 60.06 / 59.63-60.83 | 1.49 (2.5%) | 59.55-70.15 | -5.2% / -6.2% | -4.6% | 37.1M |
| XLV | 183.18 (10:05 iex) | -0.8% | 184.72 | 184.13 / 181.69-184.60 | 3.90 (2.1%) | 176.71-192.32 | +0.0% / +4.3% | -0.3% | 13.6M |
| XLI | 159.19 (10:05 iex) | -1.5% | 161.61 | 158.43 / 157.41-159.33 | 4.07 (2.5%) | 155.70-172.40 | -2.8% / -3.6% | -1.9% | 9.5M |
| XLY | 114.92 (10:05 iex) | -2.4% | 117.72 | 115.81 / 113.85-115.86 | 3.04 (2.6%) | 112.03-122.92 | -0.3% / +2.9% | +0.5% | 10.0M |
| XLP | 92.22 (10:05 iex) | +0.4% | 91.88 | 92.18 / 91.86-92.48 | 1.53 (1.7%) | 86.36-93.48 | +1.4% / +6.0% | +0.5% | 22.0M |
| XLU | 43.47 (10:04 iex) | +0.2% | 43.40 | 43.32 / 43.28-43.52 | 0.64 (1.5%) | 42.42-44.40 | -0.1% / +3.3% | -0.0% | 26.0M |
| XLB | 49.95 (10:05 iex) | -0.4% | 50.17 | 49.73 / 49.48-49.92 | 1.17 (2.3%) | 48.21-54.63 | -3.1% / -1.1% | -1.3% | 13.1M |
| XLRE | 43.44 (10:05 iex) | -0.1% | 43.46 | 43.48 / 43.23-43.55 | 0.70 (1.6%) | 41.78-45.34 | -0.6% / +2.1% | -0.3% | 7.9M |
| XLC | 103.04 (10:05 iex) | -1.3% | 104.45 | 102.50 / 101.41-103.08 | 2.60 (2.5%) | 99.33-109.26 | +0.0% / -3.5% | -0.8% | 8.3M |
| KRE | 69.29 (10:05 iex) | -0.7% | 69.76 | 69.05 / 68.92-69.39 | 1.50 (2.1%) | 68.14-75.80 | -2.9% / -1.9% | -1.5% | 15.6M |
| XHB | 100.25 (10:04 iex) | -1.0% | 101.28 | 100.21 / 99.64-101.37 | 3.12 (3.1%) | 96.34-108.78 | -0.3% / +2.8% | +2.2% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 350.48 (10:05 iex) | -1.0% | 354.07 | 353.48 / 347.70-353.84 | 8.15 (2.3%) | 325.08-360.83 | +1.8% / +3.4% | +0.6% | 50.8M |
| MSFT | 484.40 (10:05 iex) | -2.4% | 496.13 | 485.23 / 477.39-487.27 | 17.47 (3.5%) | 481.03-558.07 | -4.3% / -4.3% | -1.8% | 31.0M |
| NVDA | 145.11 (10:05 iex) | -6.6% | 155.38 | 144.00 / 141.17-145.96 | 16.15 (10.4%) | 124.50-219.99 | -11.6% / -24.2% | -0.1% | 338.1M |
| AMZN | 241.42 (10:05 iex) | -4.3% | 252.29 | 243.12 / 237.61-244.44 | 10.79 (4.3%) | 229.36-275.34 | -2.1% / -1.1% | -2.2% | 54.1M |
| GOOGL | 267.99 (10:05 iex) | -4.0% | 279.05 | 265.10 / 262.73-268.41 | 11.78 (4.2%) | 264.22-326.40 | -2.3% / -12.7% | -0.4% | 46.8M |
| META | 582.81 (10:05 iex) | -1.2% | 589.82 | 575.01 / 567.75-586.74 | 24.88 (4.2%) | 558.68-648.45 | -4.2% / -12.4% | -4.7% | 19.2M |
| TSLA | 364.02 (10:05 iex) | -5.4% | 384.68 | 370.21 / 357.68-370.51 | 21.48 (5.6%) | 338.15-414.23 | +0.3% / +2.1% | +1.2% | 35.9M |
| AVGO | 288.29 (10:05 iex) | -4.2% | 301.08 | 286.98 / 278.00-288.77 | 24.00 (8.0%) | 289.77-369.82 | -8.6% / -11.8% | -11.9% | 31.8M |
| AMD | 383.78 (10:05 iex) | -7.1% | 413.27 | 382.78 / 371.50-388.79 | 55.60 (13.5%) | 396.01-594.00 | -17.0% / -24.9% | -17.9% | 45.5M |
| ORCL | 101.84 (10:05 iex) | -7.0% | 109.50 | 103.24 / 99.34-104.18 | 8.49 (7.8%) | 100.25-148.48 | -9.4% / -16.2% | -4.8% | 42.8M |
| NFLX | 58.17 (10:05 iex) | -1.2% | 58.87 | 57.96 / 57.09-58.27 | 1.96 (3.3%) | 56.56-67.49 | -4.8% / -11.6% | -1.4% | 40.3M |
| CRM | 194.10 (10:05 iex) | +0.4% | 193.26 | 190.36 / 188.20-194.30 | 8.52 (4.4%) | 179.91-244.64 | -8.8% / -14.8% | -0.6% | 7.4M |
| JPM | 311.90 (10:05 iex) | -1.6% | 317.10 | 310.56 / 309.49-312.67 | 8.80 (2.8%) | 309.18-359.80 | -5.3% / -5.5% | -3.9% | 7.3M |
| GS | 784.66 (10:04 iex) | -2.6% | 806.02 | 779.34 / 772.74-786.23 | 35.09 (4.4%) | 786.66-939.38 | -8.9% / -10.2% | -8.1% | 2.4M |
| BAC | 47.75 (10:05 iex) | -1.7% | 48.56 | 47.17 / 46.94-47.84 | 1.25 (2.6%) | 46.88-53.02 | -2.5% / -7.1% | -1.8% | 36.2M |
| XOM | 159.49 (10:05 iex) | +0.8% | 158.23 | 158.12 / 156.83-159.56 | 3.88 (2.5%) | 156.67-187.32 | -5.8% / -5.8% | -5.4% | 15.1M |
| CVX | 211.16 (10:05 iex) | +1.2% | 208.73 | 208.00 / 207.19-211.10 | 4.72 (2.3%) | 204.31-234.53 | -3.0% / -2.2% | -2.6% | 8.7M |
| LLY | 1,393.13 (10:05 iex) | -1.0% | 1,407.59 | 1,405.00 / 1,375.01-1,412.99 | 43.30 (3.1%) | 1,258.81-1,475.25 | +1.0% / +10.3% | -0.6% | 3.3M |
| UNH | 342.15 (10:04 iex) | +0.1% | 341.88 | 338.50 / 334.80-342.26 | 16.51 (4.8%) | 319.13-416.19 | -11.7% / -11.7% | -12.3% | 7.5M |
| JNJ | 274.48 (10:05 iex) | -0.7% | 276.46 | 278.32 / 273.50-279.88 | 6.73 (2.4%) | 262.89-288.81 | +0.8% / +3.8% | -0.3% | 8.2M |
| WMT | 132.74 (10:05 iex) | +0.3% | 132.31 | 132.49 / 131.87-133.19 | 2.99 (2.3%) | 118.11-132.42 | +4.6% / +12.6% | +3.8% | 24.6M |
| COST | 1,093.88 (10:05 iex) | +0.2% | 1,091.71 | 1,093.49 / 1,086.24-1,098.00 | 19.53 (1.8%) | 952.12-1,094.75 | +5.0% / +12.9% | +1.1% | 2.6M |
| HD | 353.73 (10:05 iex) | +0.0% | 353.69 | 355.00 / 350.71-357.07 | 9.56 (2.7%) | 316.15-362.44 | +3.2% / +11.7% | +4.3% | 5.2M |
| CAT | 523.92 (10:05 iex) | -3.1% | 540.63 | 518.99 / 512.51-525.41 | 29.50 (5.5%) | 508.11-732.73 | -8.0% / -23.2% | -5.3% | 4.2M |
| BA | 162.51 (10:04 iex) | -0.7% | 163.59 | 161.35 / 159.55-162.66 | 5.34 (3.3%) | 155.56-179.19 | -3.2% / -10.2% | -0.2% | 8.7M |
| DAL | 80.46 (10:04 iex) | -4.8% | 84.50 | 82.48 / 79.72-82.48 | 3.18 (3.8%) | 78.66-92.52 | -1.0% / +2.4% | +0.2% | 5.9M |
| UAL | 101.89 (10:03 iex) | -5.5% | 107.80 | 104.56 / 101.38-104.95 | 5.29 (4.9%) | 100.28-122.08 | -1.8% / -0.1% | +1.4% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| HPQ | 30.64 (10:05 iex) | +9.6% | 27.94 | 29.95 / 29.70-32.05 | 1.07 (3.8%) | 26.95-33.50 | -3.7% / -9.1% | -2.7% | 14.4M |
| HSY | 181.63 (10:04 iex) | +2.9% | 176.56 | 179.46 / 178.05-181.86 | 5.43 (3.1%) | 158.55-180.19 | +2.8% / +5.6% | +1.6% | 2.2M |
| CHTR | 139.64 (10:04 iex) | +2.8% | 135.87 | 136.23 / 134.19-139.86 | 8.14 (6.0%) | 104.06-142.60 | +7.6% / +15.4% | -1.9% | 3.0M |
| ACN | 238.45 (10:04 iex) | +2.6% | 232.32 | 234.66 / 232.27-238.98 | 8.96 (3.9%) | 216.13-271.76 | -5.8% / +4.4% | -2.9% | 5.1M |
| DOW | 29.71 (10:05 iex) | +2.6% | 28.95 | 28.83 / 28.73-29.76 | 1.13 (3.9%) | 28.16-34.85 | -9.3% / -4.6% | -7.7% | 8.0M |
| DKNG | 16.53 (10:05 iex) | +2.6% | 16.11 | 15.81 / 15.64-16.60 | 1.46 (9.1%) | 15.43-23.89 | -16.4% / -19.4% | -10.5% | 18.8M |
| DE | 629.64 (10:04 iex) | +2.6% | 613.76 | 587.99 / 580.51-629.64 | 21.62 (3.5%) | 605.34-698.91 | -6.8% / -7.2% | -5.5% | 1.3M |
| DVN | 42.31 (10:05 iex) | +2.4% | 41.33 | 41.25 / 40.98-42.37 | 1.66 (4.0%) | 40.60-52.28 | -8.1% / -12.5% | -4.9% | 12.8M |
| LRCX | 179.08 (10:05 iex) | -8.7% | 196.16 | 182.82 / 175.76-183.50 | 19.49 (9.9%) | 181.77-260.58 | -10.4% / -25.8% | -6.9% | 14.2M |
| SNDK | 71.53 (10:05 iex) | -8.2% | 77.95 | 71.31 / 69.03-72.59 | 13.86 (17.8%) | 74.83-176.06 | -32.3% / -52.4% | -21.8% | 113.6M |
| MU | 579.39 (10:05 iex) | -8.0% | 629.79 | 575.00 / 557.33-584.38 | 75.53 (12.0%) | 585.25-990.00 | -17.3% / -30.2% | -11.6% | 36.0M |
| AMAT | 299.37 (10:05 iex) | -7.5% | 323.76 | 300.21 / 294.94-302.50 | 30.86 (9.5%) | 300.62-425.88 | -10.7% / -23.2% | -7.2% | 9.0M |
| TER | 197.91 (10:05 iex) | -7.2% | 213.22 | 199.01 / 193.35-200.61 | 24.30 (11.4%) | 201.74-316.80 | -13.7% / -34.1% | -8.9% | 4.6M |
| ARM | 150.27 (10:05 iex) | -7.0% | 161.56 | 149.54 / 143.55-151.59 | 18.27 (11.3%) | 150.37-237.88 | -14.4% / -31.8% | -11.9% | 6.5M |
| GLW | 94.93 (10:05 iex) | -6.8% | 101.87 | 95.38 / 92.78-95.64 | 9.69 (9.5%) | 93.49-132.93 | -10.4% / -23.8% | -6.1% | 10.6M |
| MRVL | 122.82 (10:05 iex) | -6.7% | 131.57 | 122.84 / 119.10-124.35 | 16.23 (12.3%) | 120.56-253.66 | -18.3% / -39.4% | -11.5% | 34.7M |
