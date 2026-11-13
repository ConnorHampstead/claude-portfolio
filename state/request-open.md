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

# Pre-market brief: Friday 2026-11-13, 09:05 ET / 15:05 Stockholm

**One new order: a GLD sell-stop short at 352.40, at half risk.** It only fills if gold makes a new 13-month low today. AMZN, DAL and IWM keep their brackets unchanged, because none of their invalidations has happened. Nothing else cleared conviction 3 with a positive expected value.

## 1. Tape

Futures are modestly higher (S&P +0.2–0.4%, Nasdaq-100 about flat). October PPI printed slightly soft at 08:30, and Thursday's NVDA shock is fading: NVDA is +2.3% pre-market after Huang resigned, with Kress as interim CEO.

The regime underneath is a hawkish repricing:
- **Yields:** the 10-year is about 5.12–5.13% after a ~13.5bp jump Thursday, its highest since October. The 2-year is down 4bp to about 4.84% on softer oil.
- **Fed:** a 25bp December hike is fully priced, with small odds of 50bp.
- **Dollar:** DXY is 103.05–103.23, near a 19-month high and up about 1.5% on the week.
- **Gold and bitcoin:** gold hit a 13-month low of $3,853 Thursday and is bouncing to about $3,900. Bitcoin is under $70k.

Equities have been resilient to all this (SPY +3.3% over 5 days, QQQ +6.4%), and rotation inside AI is the main equity story. **The edge is on the short side in the rates, dollar and gold complex. Index equities are chop.**

## 2. Calendar

Stockholm is ET+6 today: the US clock change was Nov 1 and the EU's Oct 25, so the gap is the usual one.

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Oct PPI | **Already out.** Headline +0.3% m/m vs +0.4% expected. Core +0.3%, in line. Ex food, energy and trade +0.5%. 6.5% y/y, highest since Nov 2022. Sept revised up to +1.4%. Futures extended gains and yields were mixed. | IWM, GLD |
| 08:30 | 14:30 | Goolsbee (CNBC) | Already out: inflation "broadening", with "stalled progress" | IWM, GLD |
| 09:10 | 15:10 | Collins, opening remarks | Hawkish lean in recent remarks | IWM, GLD |
| 09:40 | 15:40 | Logan (Dallas) | Said Nov 10 the Fed needs "at least two more" 25bp hikes | IWM, GLD |
| 10:35 / 10:50 | 16:35 / 16:50 | Collins (Bloomberg TV) / Bowman (supervision) | — | — |
| 12:00 | 18:00 | Daly | — | GLD |
| 19:00 | 01:00 Sat | Jefferson | — | — |
| Next week | | Retail sales Tue Nov 17 08:30 ET; NVDA earnings Tue Nov 17; FOMC minutes; HD, LOW and WMT earnings | — | QQQ, AMZN |

The Fed-speaker times come from a single source (ZeroHedge's schedule). **VIX:** I couldn't verify a level for today. The last ones I have are 17.49 Wednesday (Saxo) and 19.92 on Nov 9 (FRED), so it is still easing off the Nov 5 spike to 28.18.

Overnight earnings: AMAT beat, guiding Q1 to $11.1B against $10.89B expected, and is flat pre-market at about $380.6 (Benzinga). CSCO is −3.1% at 98.88 even though it beat and raised: revenue $18.5B (+24%) and fiscal-2027 revenue guidance raised to $74.8–75.8B. The selling is on gross margin (GAAP 63.7% vs 65.5%), a flat Q2 guide of $18.0–18.2B, and product orders that disappointed.

## 3. Open positions and resting entries

| Name | Session | Invalidation happened? | Decision |
|---|---|---|---|
| AMZN long, 274.10, bracket 263.50 / 293.00 | 5 of 10 | **No.** The test is QQQ breaking its 647.05 20-day low while AMZN falls back inside its range. QQQ is 689.65 pre-market and AMZN 269.74. | Hold, bracket unchanged |
| DAL long, 89.50, bracket 85.80 / 96.50 | 2 of 10 | **No.** The test is Brent above $100. Brent is about $95.9–96.0 (BNN Bloomberg $96.04, ZeroHedge $95.88). DAL is 87.00, near its stop, which is not a reason to act. | Hold, bracket unchanged |
| IWM short, 281.03, bracket 287.00 / 271.00 | 4 of 10 | **No.** The tests are the 2-year back at 4.55% (it is about 4.84%) or a close above 284 (Thursday closed 278.44). | Hold, bracket unchanged |
| QQQ sell stop 646.50, bracket 664 / 615 | resting | It sits about 43 points under the market, below the 20-day low, so it only fires on a real breakdown. | Keep. The harness clears it before the weekend; Monday decides whether to put it back. |

**Note on last night's GLD plan.** The plan needed Thursday to close below 354.67 with DXY above 102.85. GLD closed at 354.89. **The condition was not met**, so I am not placing the planned short on a retest from below at about 355. The play below is a different trigger, a new low, and I'm saying so here so nobody reads it as the same plan.

## 4. New plays

### GLD short (sell stop)

| Field | Value |
|---|---|
| Ticker | GLD |
| Direction | Short |
| Catalyst | Gold hit a 13-month low of $3,853 on Nov 12 after the hot CPI and hawkish Fed talk (BullionVault, Nov 12). Logan said Nov 10 that at least two more 25bp hikes are needed. A December 25bp hike is fully priced (CNBC PPI story, Nov 13). DXY is about 103.2, near a 19-month high (ZeroHedge and FXStreet, Nov 13). |
| Thesis | A strong dollar and a hiking Fed take away gold's support. Thursday's break of the 20-day low closed just back above the level, and today is a soft-PPI bounce. A fresh low under Thursday's 352.91 would mean the second attempt at breaking support has worked, which is a better entry than yesterday's chase. |
| Entry | **Sell stop at 352.40**, 0.51 under Thursday's 352.91 low. Pre-market is 355.71 (Alpaca 08:49 SIP), so the trigger is below the market. It is live today only, since resting entries are cleared before the weekend. |
| Stop | **361.50**, 9.10 away (1.19 ATR). That is above Thursday's 354.89 close and today's bounce. A new low that reverses back over 361.5 is a failed breakdown. |
| Target | **334.00**, 18.40 away, **2.02R** |
| Risk tier | **0.5%.** A filled position is held over the weekend while the Iran war is live, so there is unusual gap risk. Gold is also already −5.5% over 5 days (about 3.6 ATR). |
| Time horizon | 3–8 sessions |
| Next earnings | None (ETF). Not an event trade. |
| Conviction | 3 |
| P(target before stop) | **0.36.** I started from the 40% base rate and took it down for the extension and the weekend gap risk. I left it above my 35–40% bucket's 31% hit rate because the macro driver is verified and ongoing, and the entry needs a confirming new low. EV = 0.36 × 2.02 − 0.64 = **+0.09R**. |
| Invalidation | DXY closes below 102.00, or CME FedWatch December hike odds fall below 50%. |
| What I'd be wrong about | The hike is already fully priced, so the marginal hawkish news may be spent. Gold has fallen 8% in 20 sessions and is due a reflexive bounce, and a Hormuz headline over the weekend could gap it up. My 35–40% calls have hit only 31% of the time. At that rate this trade is about −0.07R. |

## 5. Both sides

- **Best short: GLD**, sell stop 352.40, stop 361.50, target 334.00, P 0.36. Taken above.
- **Best long: CSCO** buying the dip after a beat and raise. Limit 97.50, stop 93.00 (under the 93.35 20-day low), target 106.50 (2.0R), P 0.34, EV about +0.02R. **Passed.** Margin compression is a real reason to sell the stock, and buying earnings gap-downs has shown no edge for me. Conviction 2. Its next earnings are roughly mid-Feb 2027; I couldn't verify the exact date.

Other shorts I looked at:
- TLT breaking down: passed, see section 6.
- XHB and homebuilders: no dated catalyst beyond rates, which the IWM short already expresses.
- LOW: couldn't verify the reported Stifel downgrade to sell, and its earnings look to be next week. No levels.
- MSFT on the outage: transient. No levels.

## 6. Passing on

- **TLT short**, sell stop 78.90, stop 80.40, target 75.90, P 0.33, EV about −0.01R. It is already −2.7% over 5 days, the hike is priced, and the 2-year is easing today. It would also double the rates exposure the IWM short already carries.
- **NU long** at 12.37 market, stop 11.15, target 14.80, P 0.32. Q3 net income was a record $1.09B (+31%, Business Wire), but one report says it narrowly missed estimates, so I can't be sure which way the surprise went. A strong dollar works against Brazilian assets. Conviction 2.
- **CSCO long:** above.
- **TRV +3.7%, HUM +2.3%, PWR +2.3%:** I found no dated catalyst, and the prints are thin pre-market ones. A mover I can't explain is not a trade.
- **PANW +2.9%** on a KeyBanc upgrade: earnings Nov 18, so rule 8 blocks it. **NVDA:** earnings Nov 17, blocked.
- **AMAT:** a beat-and-raise that drew no reaction. Nothing to trade.
- **MOD +30%** on a Bloomberg report of Samsung takeover talks that Samsung won't confirm: I won't take an unconfirmed merger-arb position.

## 7. For the post-open review

- **GLD:** if it trades above 360 by 10:05 (a reversal on soft PPI or dovish Fed talk), cancel the 352.40 sell stop, because the breakdown premise is failing. If the order has already filled, leave the bracket alone.
- **DAL:** close only if Brent is above $100, which is the invalidation.
- **Logan at 09:40 ET:** no action either way on IWM. Its invalidation is the 2-year at 4.55% or a close above 284.
- **CSCO:** stays in the shadow book. No live action.

## 8. Book state

- **If GLD fills:** gross is about 73% of the 150% cap and net about −48% of ±100%, counting the QQQ resting order, which clears tonight.
- **Risk at stake** is about 1.99% of the 4.0% cap, with 5 of 8 slots used.

```json
{
  "date": "2026-11-13",
  "no_trade": false,
  "session_note": "Hawkish repricing (10y ~5.13%, Dec hike fully priced, DXY ~103.2 near 19-month high) with resilient equities; PPI +0.3% vs +0.4% soft. One play: GLD sell stop under Thursday's 13-month low at half risk; existing brackets untouched, no invalidations met.",
  "plays": [
    {
      "ticker": "GLD",
      "direction": "short",
      "entry_type": "stop",
      "entry": 352.40,
      "stop": 361.50,
      "targets": [334.00],
      "time_horizon": "3-8 sessions",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.36,
      "earnings_date": null,
      "event_trade": false,
      "catalyst": "Gold 13-month low $3,853 on Nov 12 (BullionVault) on hot CPI and Fed hike pricing; Dec 25bp hike fully priced (CNBC Nov 13); DXY ~103.2 near 19-month high (ZeroHedge Nov 13); Logan Nov 10 called for at least two more hikes.",
      "thesis": "Strong dollar and a hiking Fed remove gold's support. Thursday's break of the 20d low closed just back above it; a fresh low under 352.91 confirms the second breakdown attempt and is a better entry than chasing Thursday.",
      "invalidation": "DXY closes below 102.00, or CME FedWatch December hike odds fall below 50%.",
      "bear_case": "Hike fully priced so marginal hawkish news may be spent; gold already -8% in 20 sessions and due a bounce; weekend Iran/Hormuz headline gap risk; my 35-40% bucket has hit only 31%."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "CSCO",
      "direction": "long",
      "entry_type": "limit",
      "entry": 97.50,
      "stop": 93.00,
      "targets": [106.50],
      "p_target_first": 0.34,
      "reason": "Beat-and-raise (Q1 FY27 rev $18.5B +24%, FY guide raised to $74.8-75.8B) sold -3.1% on gross margin and a flat Q2 guide; dip-buys of earnings gaps have no demonstrated edge, conviction 2, EV ~+0.02R; next earnings ~mid-Feb 2027, unverified."
    },
    {
      "ticker": "TLT",
      "direction": "short",
      "entry_type": "stop",
      "entry": 78.90,
      "stop": 80.40,
      "targets": [75.90],
      "p_target_first": 0.33,
      "reason": "10y 5.13% but already -2.7% in 5d, hike fully priced, 2y easing today; duplicates IWM rates exposure; EV ~-0.01R."
    },
    {
      "ticker": "NU",
      "direction": "long",
      "entry_type": "market",
      "entry": 12.37,
      "stop": 11.15,
      "targets": [14.80],
      "p_target_first": 0.32,
      "reason": "Record Q3 net income $1.09B (+31%) but one report says it narrowly missed estimates, so the surprise direction is unclear; strong dollar is a headwind for Brazilian assets; conviction 2."
    }
  ]
}
```

Sources:
- [Yahoo Finance live, Nov 13](https://finance.yahoo.com/markets/live/stock-market-today-friday-november-13-dow-sp-500-nasdaq-nvidia-110151154.html)
- [StockTitan live, Nov 13](https://www.stocktitan.net/articles/stock-market-today-live-november-13-2026)
- [TipRanks, Nov 13](https://www.tipranks.com/news/stock-market-today-nov-13-u-s-stocks-wobble-ahead-of-ppi-data)
- [BNN Bloomberg, Nov 13](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/11/13/us-futures-climb-as-wall-street-keeps-an-eye-on-nvidia-microsoft-and-producer-prices/)
- [ZeroHedge: futures rise as Wall Street moves on from Jensen](https://www.zerohedge.com/markets/futures-rise-wall-street-moves-jensen-microsoft-outage-drags-day-two)
- [CNBC: PPI report, October 2026](https://www.cnbc.com/2026/11/13/ppi-inflation-report-october-2026.html)
- [Seeking Alpha: PPI rises less than expected](https://seekingalpha.com/news/4672315-ppi-inflation-rises-less-than-expected-in-october)
- [Tribune: PPI 6.5% annually](https://www.tribuneindia.com/news/inflation-rate/us-producer-prices-rise-6-5-pc-annually-in-october-highest-since-november-2022)
- [fedratecalc November 2026 calendar](https://fedratecalc.com/us-economic-calendar/november-2026/)
- [AMAT Q4 FY26 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0000006951/000162828026073360/exhibit991q42026earningsre.htm)
- [Benzinga: Applied Materials sees another record year](https://www.benzinga.com/markets/large-cap/26/11/63231559/applied-materials-sees-another-record-year-in-2027)
- [TradingKey: AMAT stalls](https://www.tradingkey.com/analysis/stocks/us-stocks/262304041-applied-materials-expects-30-percent-equipment-growth-amat-stalls-below-405-45-november-13-2026-tradingkey)
- [Cisco IR: Q1 FY27 earnings](https://investor.cisco.com/news/news-details/2026/CISCO-REPORTS-FIRST-QUARTER-EARNINGS/default.aspx)
- [StockTitan: Cisco Q1](https://www.stocktitan.net/news/CSCO/cisco-reports-first-quarter-42972jcsdwos.html)
- [Business Wire: Nu Holdings Q3 2026](https://www.businesswire.com/news/home/20261112222106/en/Nu-Holdings-Ltd.-Reports-Third-Quarter-2026-Financial-Results)
- [Investing.com: Nu Q3 net income](https://www.investing.com/news/company-news/nu-holdings-reports-q3-net-income-of-11-billion-up-31-yoy-93CH-5023382)
- [BullionVault: gold 13-month low](https://www.bullionvault.com/gold-news/gold-price-news/gold-inflation-fed-rate-hikes-111220261)
- [FXStreet: gold retakes $3,900](https://www.fxstreet.com/news/gold-recovers-from-ytd-low-retakes-3-900-fed-hike-bets-and-bullish-usd-to-cap-gains-202611130403)
- [FinanceFeeds: gold price today](https://financefeeds.com/gold-price-today-3888-friday-ppi-day-after-13-month-low-bull-3963-bear-3800/)
- [CNN: bond yields surge](https://www.cnn.com/2026/11/10/investing/bond-yields-inflation-fed)
- [Investinglive: Logan two more hikes](https://investinglive.com/central-banks/fed-s-logan-it-s-clear-that-fed-needs-at-least-two-more-quarter-point-rate-hikes/)
- [FRED VIXCLS](https://fred.stlouisfed.org/graph/?g=JicV)
- [Cboe: week of 11/9/2026](https://www.cboe.com/insights/posts/week-of-11-9-2026-no-contagion-yet-equity-vol-spikes-macro-vol-fades)
- [Trefis: DR Horton](https://www.trefis.com/stock/dhi/articles/622675/what-is-behind-the-move-in-dr-horton-stock/2026-11-04)
- [CNBC TRV quote](https://www.cnbc.com/quotes/TRV)
- [Benzinga: Humana Q3](https://www.benzinga.com/markets/earnings/26/11/62986759/humana-stock-rises-after-narrower-than-expected-loss-raised-2026-profit-outlook)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Friday 2026-11-13. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,429.12**
- Cash: $113,476.11
- Session P&L so far: +0.22% (new entries are blocked at -3.0%)
- Gross exposure: $74,402 (73% of equity, cap 150%)
- Net exposure: $-49,530 (-48%, cap +/-100%)
- Risk at stake (entry to stop): $2,035 (1.99% of equity, cap 4.0%) — 2.01% left for new plays
- Slots: 3 open + 2 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 268.04 | -145 (-2.2%) | +6% | 263.50 | 293.00 |
| DAL | long | 69 | 89.50 | 87.00 | -172 (-2.8%) | +6% | 85.80 | 96.50 |
| IWM | short | 85 | 281.03 | 276.27 | +404 (+1.7%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **AMZN**, opened 2026-11-09 (session 5 of at most 10), submitted with stop 263.5 and target 293, P 36%. Thesis: Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong relative signal. Invalidation: QQQ breaking its 20-day low while AMZN falls back inside the range.
- **DAL**, opened 2026-11-12 (session 2 of at most 10), submitted with stop 85.8 and target 96.5, P 37%. Thesis: Falling jet fuel is a direct margin tailwind. Buy the retest of the 89.92 20-day-high breakout rather than chase the gap. Invalidation: Brent back above $100.
- **IWM**, opened 2026-11-10 (session 4 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GLD | short | 56 | 352.40 | stop | 361.50 | 334.00 | 2026-11-13 |
| QQQ | short | 29 | 646.50 | stop | 664.00 | 615.00 | 2026-11-09 |

### Your record

47 closed trades: 15W / 32L, total +1.17R, net $+2,358 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 47 | 17 | 27 | +0.02R |
| The same trades, bracket left alone | 47 | | | +0.06R |
| Ideas you passed on, or the caps dropped | 92 | 34 | 49 | +0.08R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 36 | 50% |
| 35%-40% | 59 | 31% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 40% of 127 brackets reached target first. Your Brier score is 0.243; saying 40% every time scores 0.240. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLE | short | close | -1.02R | $-521 | 37% |
| AVGO | short | close | -0.92R | $-232 | 37% |
| NVDA | short | target | +2.16R | $+1,108 | 37% |
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AMZN | 268.02 (10:05 iex) | +0.2% | 267.44 | 269.94 / 267.08-270.05 | 10.56 (3.9%) | 229.36-275.34 | +4.3% / +5.0% | +2.8% | 50.6M |
| DAL | 87.00 (10:05 iex) | +0.5% | 86.55 | 87.47 / 86.86-87.84 | 3.34 (3.9%) | 74.14-92.52 | +4.7% / +6.0% | +1.4% | 6.6M |
| IWM | 276.27 (10:05 iex) | -0.8% | 278.44 | 278.95 / 275.98-279.17 | 5.36 (1.9%) | 269.88-286.17 | +0.2% / -0.9% | +2.8% | 24.2M |
| GLD | 356.19 (10:05 iex) | +0.4% | 354.89 | 356.27 / 356.07-357.32 | 7.66 (2.2%) | 352.91-384.88 | -4.1% / -7.1% | -5.5% | 9.2M |
| QQQ | 678.52 (10:05 iex) | -1.4% | 688.17 | 688.51 / 678.08-688.75 | 18.16 (2.6%) | 647.05-727.95 | -1.3% / -4.2% | +6.4% | 50.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 752.43 (10:05 iex) | -0.6% | 757.12 | 760.07 / 752.08-760.12 | 12.45 (1.6%) | 732.71-775.64 | -0.3% / -1.0% | +3.3% | 48.3M |
| QQQ | 678.52 (10:05 iex) | -1.4% | 688.17 | 688.51 / 678.08-688.75 | 18.16 (2.6%) | 647.05-727.95 | -1.3% / -4.2% | +6.4% | 50.9M |
| IWM | 276.27 (10:05 iex) | -0.8% | 278.44 | 278.95 / 275.98-279.17 | 5.36 (1.9%) | 269.88-286.17 | +0.2% / -0.9% | +2.8% | 24.2M |
| DIA | 522.54 (10:04 iex) | +0.0% | 522.47 | 524.82 / 522.33-524.99 | 7.54 (1.4%) | 508.66-536.60 | +0.1% / +0.6% | +1.6% | 3.8M |
| TLT | 79.34 (10:04 iex) | -0.5% | 79.72 | 79.30 / 79.11-79.38 | 0.76 (1.0%) | 79.01-82.42 | -1.5% / -0.2% | -2.7% | 36.3M |
| GLD | 356.19 (10:05 iex) | +0.4% | 354.89 | 356.27 / 356.07-357.32 | 7.66 (2.2%) | 352.91-384.88 | -4.1% / -7.1% | -5.5% | 9.2M |
| USO | 146.58 (10:04 iex) | +0.3% | 146.07 | 146.69 / 146.26-146.99 | 5.88 (4.0%) | 138.47-171.82 | -6.9% / -4.4% | -1.4% | 5.6M |
| SMH | 483.12 (10:05 iex) | -3.7% | 501.73 | 499.93 / 481.98-500.27 | 26.50 (5.3%) | 445.59-571.00 | -3.7% / -10.6% | +12.1% | 12.1M |
| XLK | 169.57 (10:04 iex) | -2.4% | 173.77 | 173.58 / 169.55-173.65 | 6.09 (3.5%) | 162.14-191.55 | -3.1% / -7.3% | +7.0% | 12.8M |
| XLF | 58.50 (10:05 iex) | +0.5% | 58.21 | 58.60 / 58.46-58.70 | 1.01 (1.7%) | 55.03-60.04 | +2.3% / +4.1% | +1.2% | 33.6M |
| XLE | 64.30 (10:05 iex) | -0.0% | 64.33 | 64.93 / 64.16-64.97 | 1.74 (2.7%) | 60.43-70.15 | -3.0% / -0.9% | +4.4% | 37.3M |
| XLV | 187.85 (10:04 iex) | +0.0% | 187.83 | 188.45 / 187.22-188.77 | 3.75 (2.0%) | 175.27-192.32 | +2.6% / +7.6% | +1.6% | 11.2M |
| XLI | 168.56 (10:05 iex) | -0.5% | 169.44 | 170.54 / 168.26-170.72 | 3.34 (2.0%) | 161.74-172.40 | +1.0% / +0.3% | +4.3% | 8.8M |
| XLY | 120.12 (10:05 iex) | -0.3% | 120.46 | 120.88 / 120.03-120.97 | 2.60 (2.2%) | 111.84-122.92 | +3.0% / +5.9% | +2.4% | 9.5M |
| XLP | 91.83 (10:05 iex) | +0.9% | 91.06 | 91.66 / 91.43-92.04 | 1.63 (1.8%) | 86.36-93.40 | +2.0% / +6.6% | -0.2% | 19.2M |
| XLU | 43.84 (10:05 iex) | +0.1% | 43.81 | 43.96 / 43.78-44.04 | 0.60 (1.4%) | 41.28-44.14 | +1.9% / +4.8% | +1.2% | 25.9M |
| XLB | 52.15 (10:04 iex) | -0.4% | 52.34 | 52.68 / 52.06-52.68 | 1.01 (1.9%) | 50.61-54.63 | +0.3% / +2.9% | +0.0% | 12.1M |
| XLRE | 44.30 (10:04 iex) | -0.1% | 44.36 | 44.54 / 44.30-44.57 | 0.70 (1.6%) | 41.60-45.34 | +2.5% / +4.3% | +0.1% | 8.1M |
| XLC | 108.84 (10:04 iex) | +1.2% | 107.56 | 108.30 / 108.21-109.22 | 2.18 (2.0%) | 99.33-112.90 | +1.9% / -1.7% | +3.1% | 7.9M |
| KRE | 72.36 (10:04 iex) | -0.2% | 72.52 | 72.88 / 72.33-72.92 | 1.54 (2.1%) | 69.17-75.80 | +0.4% / +1.2% | +0.3% | 14.3M |
| XHB | 101.64 (10:04 iex) | +0.3% | 101.32 | 102.11 / 101.51-102.50 | 3.26 (3.2%) | 94.05-108.78 | +0.8% / +3.0% | -2.4% | 2.5M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 358.47 (10:05 iex) | +1.0% | 354.88 | 357.96 / 357.84-360.83 | 9.50 (2.7%) | 325.08-359.37 | +2.8% / +4.9% | +3.2% | 48.4M |
| MSFT | 519.88 (10:05 iex) | -0.6% | 523.00 | 519.98 / 513.82-523.57 | 17.48 (3.3%) | 504.96-559.15 | -1.3% / +0.8% | -2.4% | 26.4M |
| NVDA | 162.17 (10:05 iex) | -2.4% | 166.19 | 169.91 / 161.23-170.00 | 10.66 (6.4%) | 148.80-222.19 | -17.4% / -23.0% | -8.5% | 197.4M |
| AMZN | 268.02 (10:05 iex) | +0.2% | 267.44 | 269.94 / 267.08-270.05 | 10.56 (3.9%) | 229.36-275.34 | +4.3% / +5.0% | +2.8% | 50.6M |
| GOOGL | 300.00 (10:05 iex) | +0.4% | 298.70 | 302.98 / 299.93-304.97 | 11.43 (3.8%) | 276.92-350.66 | -2.3% / -9.2% | +5.7% | 40.9M |
| META | 633.22 (10:05 iex) | +1.5% | 623.61 | 627.21 / 625.00-637.24 | 20.93 (3.4%) | 583.80-738.49 | -2.6% / -8.2% | +3.1% | 24.1M |
| TSLA | 388.84 (10:05 iex) | -2.2% | 397.45 | 401.99 / 388.01-404.40 | 18.63 (4.7%) | 338.15-414.23 | +3.6% / +6.1% | +15.6% | 41.2M |
| AVGO | 344.82 (10:05 iex) | -5.4% | 364.36 | 356.54 / 343.93-358.47 | 19.09 (5.2%) | 289.77-369.82 | +10.4% / +5.5% | +25.0% | 26.8M |
| AMD | 537.21 (10:05 iex) | -8.2% | 585.30 | 566.78 / 535.66-571.14 | 44.61 (7.6%) | 402.10-594.00 | +12.8% / +5.8% | +44.7% | 33.4M |
| ORCL | 122.75 (10:05 iex) | -3.4% | 127.11 | 127.50 / 122.45-128.00 | 9.31 (7.3%) | 109.21-148.48 | +0.3% / -7.2% | +10.4% | 42.6M |
| NFLX | 63.76 (10:05 iex) | +1.7% | 62.69 | 62.87 / 62.47-63.94 | 1.83 (2.9%) | 61.39-71.90 | -3.2% / -9.9% | -4.4% | 46.2M |
| CRM | 217.76 (10:04 iex) | +0.1% | 217.57 | 220.00 / 216.25-220.00 | 8.50 (3.9%) | 208.88-252.42 | -6.1% / -7.9% | -2.2% | 7.0M |
| JPM | 344.48 (10:05 iex) | +0.5% | 342.82 | 346.41 / 343.82-346.80 | 7.84 (2.3%) | 330.40-359.80 | +1.2% / +0.8% | +1.6% | 6.6M |
| GS | 910.84 (10:05 iex) | -0.3% | 913.60 | 922.70 / 909.48-923.50 | 29.31 (3.2%) | 854.45-939.38 | +1.6% / -1.2% | +5.1% | 2.1M |
| BAC | 50.67 (10:05 iex) | +0.3% | 50.51 | 50.89 / 50.59-50.92 | 1.20 (2.4%) | 49.17-53.02 | -0.0% / -7.0% | +1.5% | 37.4M |
| XOM | 169.92 (10:05 iex) | +0.1% | 169.78 | 171.43 / 169.29-171.71 | 4.82 (2.8%) | 160.11-188.50 | -3.4% / +0.3% | +2.7% | 14.3M |
| CVX | 217.55 (10:04 iex) | +0.6% | 216.35 | 218.28 / 216.56-218.62 | 5.30 (2.4%) | 206.01-236.48 | -3.1% / +0.5% | +1.6% | 8.4M |
| LLY | 1,426.68 (10:05 iex) | +0.1% | 1,425.55 | 1,429.91 / 1,419.77-1,435.35 | 50.51 (3.5%) | 1,237.60-1,458.23 | +6.0% / +15.5% | +4.6% | 3.0M |
| UNH | 403.73 (10:05 iex) | -0.3% | 405.13 | 407.89 / 403.52-408.00 | 11.13 (2.7%) | 388.00-426.55 | -0.6% / +3.6% | +2.4% | 5.2M |
| JNJ | 285.75 (10:04 iex) | +0.8% | 283.52 | 285.00 / 284.03-286.42 | 7.28 (2.6%) | 251.50-286.08 | +5.0% / +6.3% | +4.1% | 7.5M |
| WMT | 127.61 (10:05 iex) | +1.1% | 126.19 | 126.73 / 126.22-128.18 | 3.03 (2.4%) | 116.63-131.82 | +2.8% / +10.6% | -1.2% | 22.0M |
| COST | 1,103.92 (10:04 iex) | +1.1% | 1,092.21 | 1,094.59 / 1,092.64-1,106.12 | 21.59 (2.0%) | 978.87-1,102.84 | +6.5% / +13.5% | +2.5% | 2.4M |
| HD | 345.69 (10:04 iex) | -0.7% | 348.26 | 344.00 / 343.26-346.35 | 9.89 (2.8%) | 306.00-362.44 | +4.9% / +11.8% | -0.5% | 4.5M |
| CAT | 598.63 (10:04 iex) | -1.1% | 605.28 | 611.93 / 598.63-611.93 | 31.33 (5.2%) | 550.81-743.23 | -7.0% / -18.6% | +9.3% | 3.9M |
| BA | 170.14 (10:04 iex) | -0.8% | 171.55 | 171.49 / 169.89-171.75 | 6.20 (3.6%) | 165.01-193.28 | -3.9% / -9.5% | -0.6% | 10.6M |
| DAL | 87.00 (10:05 iex) | +0.5% | 86.55 | 87.47 / 86.86-87.84 | 3.34 (3.9%) | 74.14-92.52 | +4.7% / +6.0% | +1.4% | 6.6M |
| UAL | 111.30 (10:04 iex) | +0.0% | 111.25 | 112.17 / 111.03-112.79 | 5.46 (4.9%) | 94.54-122.08 | +4.2% / +2.9% | +0.7% | 5.7M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| NU | 12.68 (10:05 iex) | +7.1% | 11.83 | 12.36 / 12.10-12.74 | 0.70 (5.9%) | 11.21-15.41 | -8.0% / -14.3% | +0.8% | 84.9M |
| APP | 408.98 (10:05 iex) | +3.9% | 393.68 | 395.55 / 391.49-413.45 | 25.15 (6.4%) | 225.19-413.60 | +32.0% / +31.1% | +10.6% | 5.8M |
| TTD | 16.02 (10:05 iex) | +3.5% | 15.47 | 15.63 / 15.45-16.04 | 0.86 (5.6%) | 12.01-16.42 | +16.5% / +17.3% | +20.8% | 21.5M |
| CHTR | 136.55 (10:05 iex) | +2.9% | 132.66 | 133.14 / 133.13-137.37 | 7.23 (5.4%) | 101.11-139.04 | +15.0% / +11.3% | +5.4% | 3.0M |
| KDP | 36.30 (10:05 iex) | +2.5% | 35.42 | 35.73 / 35.57-36.87 | 1.32 (3.7%) | 34.13-38.28 | -0.8% / +6.7% | -4.0% | 19.6M |
| SPOT | 613.20 (10:03 iex) | +2.5% | 598.51 | 600.93 / 598.35-614.81 | 21.61 (3.6%) | 508.01-635.00 | +3.7% / +10.4% | -2.6% | 1.9M |
| ADSK | 265.75 (10:04 iex) | +2.4% | 259.48 | 265.65 / 261.40-267.96 | 9.17 (3.5%) | 234.34-279.24 | +2.6% / +11.0% | -3.6% | 1.9M |
| LVS | 40.16 (10:05 iex) | +2.1% | 39.33 | 39.57 / 39.47-40.18 | 1.17 (3.0%) | 34.75-41.73 | +3.1% / +1.7% | -3.9% | 6.8M |
| DELL | 342.06 (10:05 iex) | -7.8% | 371.17 | 367.51 / 339.77-375.27 | 36.35 (9.8%) | 315.00-507.38 | -11.3% / -25.2% | +17.1% | 7.2M |
| SNDK | 871.52 (10:05 iex) | -7.0% | 937.46 | 915.86 / 866.87-939.53 | 111.64 (11.9%) | 803.97-1,424.48 | -18.1% / -35.6% | +16.2% | 11.8M |
| MRVL | 154.88 (10:05 iex) | -5.8% | 164.45 | 161.81 / 153.78-163.89 | 18.46 (11.2%) | 132.54-253.66 | -17.1% / -28.6% | +23.1% | 30.1M |
| WDC | 293.80 (10:05 iex) | -5.6% | 311.21 | 305.13 / 292.74-312.00 | 28.25 (9.1%) | 258.61-402.23 | -8.0% / -21.1% | +16.3% | 9.0M |
| CSCO | 96.48 (10:05 iex) | -5.4% | 102.01 | 100.15 / 96.00-100.75 | 4.01 (3.9%) | 93.35-112.69 | -2.0% / -5.4% | +6.6% | 19.6M |
| TER | 250.30 (10:05 iex) | -5.1% | 263.75 | 259.42 / 249.03-263.96 | 23.54 (8.9%) | 211.63-351.95 | -7.6% / -23.4% | +24.0% | 4.5M |
| ARM | 189.93 (10:05 iex) | -4.9% | 199.78 | 196.52 / 188.79-199.39 | 15.79 (7.9%) | 163.13-239.42 | -3.7% / -19.8% | +19.8% | 5.8M |
| AMAT | 362.20 (10:05 iex) | -4.9% | 380.95 | 376.01 / 360.65-381.37 | 26.38 (6.9%) | 316.95-427.66 | -1.0% / -13.3% | +19.3% | 8.3M |
