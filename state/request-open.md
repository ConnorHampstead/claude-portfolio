Produce the post-open review.

The cash session has been open for about 35 minutes. This morning's pre-market
brief is below, followed by the live book and market data, which now include
today's opening prices. This is the second and last decision point of the day:
after this review, nothing looks at the book until tomorrow's pre-market brief.

What this session is for:

- **Fills at the open.** Check every entry that filled since the morning. An
  entry that filled on a gap through its limit sits closer to its stop than
  planned and may no longer be the trade you meant. Keep it, tighten it, or close
  it, through `manage`.
- **The morning's plans for this review.** The 08:30 and 10:00 ET data have
  printed and the opening range is set. For each thing the morning brief said it
  would decide after the open or after the data, decide now: act, or say why not.
- **Resting entries** the open has made stale: amend or cancel them.
- **New plays**, under the same rules as the morning. Orders now go into a
  trading market: a limit at or through the last price fills immediately, and a
  `market` entry is sized from the last price.

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
Each one: keep, tighten, amend, or close, and why.

### 3. The morning's plans
Each plan the morning left for this review: acted on, not triggered, or dropped.
One line each.

### 4. New plays
The same table as the pre-market brief.

### 5. Passing on
One line each. Ideas with real levels also go in the `passed` array, where they
are scored.

Then the JSON block, in the same schema as the morning.

Your probability estimates are scored against outcomes. Spread them according to
what you actually believe rather than clustering everything near 60%.

## This morning's pre-market brief

# Pre-market brief: Monday 2026-11-02

*Written 09:05 ET / 15:05 Stockholm. The cash session opens 09:30 ET (15:30 Stockholm). US clocks fell back on Sunday and EU clocks a week earlier, so Stockholm is back to ET + 6h.*

### 1. Tape
Futures are bouncing after last week's sell-off in AI-capex names. Nasdaq 100 futures are about +0.8% and S&P 500 futures about +0.5%; on Alpaca, SPY is 759.91 (+0.6%) and QQQ 696.53 (+0.9%). The biggest overnight move is in oil: WTI is −4% to −4.6% at about $99.4–99.8 and Brent about $108. Rubio said Trump prefers negotiation with Iran, and Iran said a deal is still possible after two days of talks mediated by Qatar (CNBC, The National, TipRanks). On Alpaca, USO is −5.0%, XLE −2.0%, XOM −2.3%, and airlines are up (UAL +4.6%, DAL +3.3%). Treasuries are bid (TLT 81.81, above its 81.69 20-day high) and gold is +1.7%.

Today is the first session of an event-heavy week: ISM manufacturing at 10:00, AAPL and PLTR after the close, the midterm elections Tuesday, AMD Tuesday and payrolls Friday. The regime is a relief bounce inside a rotation away from AI capex, with no trend change yet. QQQ is still 5% under its 20-day average. ORCL is −3.3% after filing a roughly $10B equity shelf, a fresh sign that AI capex is straining financing. **Edge:** mildly long for the open, but short on AI-capex names that are being financed rather than funded from cash flow. Lower oil and lower yields together favour rate-sensitive cyclicals over energy.

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| overnight | – | US–Iran talks headlines | **Out:** oil −4% to −4.6%, WTI just under $100 | XLE (closing), UAL (passed) |
| 09:45 | 15:45 | S&P Global manufacturing PMI (final) | Final revision; normally a non-event | general |
| 10:00 | 16:00 | ISM manufacturing, October | Consensus 54.6 (prior 54.5) | KRE, XHB, TLT |
| after close | 22:00+ | AAPL fiscal Q4 | Consensus EPS $1.99, revenue $113.4B | QQQ and tech shorts (another company's event) |
| after close | 22:00+ | PLTR Q3 | Consensus EPS $0.33 | SMH, ORCL, AI sentiment |
| Tue 11-03 | – | Midterm elections; AMD earnings | – | Whole book; SMH |
| Fri 11-06 | 14:30 | October payrolls | About 55K expected (single source) | Whole book |

### 3. Open positions and resting entries
- **GOOGL short** (entry 279.61, last 282.65; stop 290.50, target 258.40). **Intact.** The bounce is ordinary beta to QQQ's +0.9%. The stock is 16% under its 20-day average and the stop sits about 0.7 ATR above the market. Hold on the existing levels.
- **META short** (entry 616.20, last 613.77; stop 643, target 580). **Intact.** META is the one large-cap tech name lower pre-market (−0.2%) while QQQ is green, which is relative weakness in line with the thesis. Hold.
- **SMH short** (entry 518.88, last 531.51; stop 541, target 486). **Weakening.** SMH is back above the 520.53 shelf it broke, so the breakdown has not followed through, and PLTR tonight plus AMD tomorrow are squeeze catalysts. The 541 stop is still the structural line: back above the shelf by about 1 ATR. I am not tightening into the open's noise. The review has a close rule (section 7).
- **XLE long** (entry 70.01, last 68.63; stop 67.90, target 73.20). **Invalidated → close at market.** The thesis was "energy repricing $100+ oil". WTI is now under $100 on a diplomacy headline, and the breakout above 69.86 has failed: XLE is back inside the range, 1.4 below entry. The stop is only 0.5 ATR away, and a headline-driven reversal can keep going. Taking roughly −0.65R now instead of a likely −1R. This frees a slot and about 0.5% of risk.
- **KRE long** (entry 73.06, last 72.56; stop 71.25, target 76.20). **Intact.** Financials are firm (XLF +0.5%), and the curve thesis is not hurt by lower oil. Hold.
- **LLY long** (entry 1432.09, last 1406.73; stop 1385, target 1520). **Intact but soft.** The −0.8% pre-market is health care lagging on a risk-on bounce, which is to be expected. The stop is about 0.45 ATR away. Hold.
- **XLP long** (entry 89.90, last 89.64; stop 88.00, target 93.50). **Intact.** The pullback-retest thesis is playing out quietly. Hold.

### 4. New plays

**ORCL short: breakdown below the 20-day low after the equity raise**
| Field | Value |
|---|---|
| Ticker | ORCL |
| Direction | Short |
| Catalyst | About $10B mixed-shelf / common-stock offering announced 2026-11-02 pre-market, plus a disclosed Oracle Health data breach |
| Thesis | Oracle is the clearest case of AI capex financed with debt and now equity. A $10B raise into a market already punishing capex confirms the financing strain and adds supply of shares. A break of the 122.76 20-day low turns the gap into a range breakdown. |
| Entry | 122.40, sell stop (Alpaca last 126.35, so the trigger is below the market) |
| Stop | 130.40. That is back above Friday's 130.67 close area, about 1 ATR (8.04) above entry; a reclaim means the raise has been absorbed. |
| Target | 110.40 (1.5R) |
| Risk tier | 0.5. ATR is 6.2%, a squeeze is possible if PLTR or AMD lift AI sentiment, and the stock is already short-crowded. |
| Time horizon | 1–4 days |
| Conviction | 3 |
| P(target before stop) | 0.36 |
| Invalidation | The offering prices at a small discount and the stock closes back above 128. |
| What I'd be wrong about | Raising capital removes a financing overhang, and a priced deal often marks the low. An analyst upgrade is out today, and the stock is +3.6% over five days, so dip buyers are active. |

**XHB long: breakout on lower yields and lower oil**
| Field | Value |
|---|---|
| Ticker | XHB |
| Direction | Long |
| Catalyst | Rates rally 2026-11-02 (TLT above its 20-day high) together with oil −4% |
| Thesis | Homebuilders benefit directly when yields and energy costs fall together. XHB is +1.2% pre-market at 102.14, just under its 102.86 20-day high, and above its 20- and 50-day averages. A break above 102.86 opens a run-up with the rotation into cyclicals. |
| Entry | 103.10, buy stop (last 102.14) |
| Stop | 100.40. That is under Friday's 100.97 close, about 1.1 ATR (2.53); losing it fills the gap. |
| Target | 107.20 (1.5R) |
| Risk tier | 0.5. Midterms Tuesday and payrolls Friday both move rates, and it is a breakout entry. |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 0.37 |
| Invalidation | TLT closes back below 81 while XHB holds the breakout. That would mean the rate impulse is gone and the move is borrowed. |
| What I'd be wrong about | It is one day of a rate rally on an oil headline. Iran talks can reverse overnight, and the 20-day high has capped XHB before. |

### 5. Both sides
- **Best short:** ORCL sell stop 122.40, stop 130.40, target 110.40, P 0.36. **Taken.**
- **Best long:** XHB buy stop 103.10, stop 100.40, target 107.20, P 0.37. **Taken.** Runner-up: UAL on the oil drop, passed (section 6).

### 6. Passing on
- **UAL long** (limit 107.00, stop 103.50, target 114.00, P 0.40). It is chasing a +4.6% gap whose catalyst is a single Iran headline, and that is binary in both directions.
- **TLT long** (buy stop 82.10, stop 80.90, target 83.90, P 0.38). Payrolls Friday and the midterms make the rates leg a coin flip. I am expressing lower yields through XHB instead.
- **AAPL**: own earnings tonight, so rule 8 applies and I have no event thesis.
- **TMUS short**: the SpaceX-competition story is plausible, but I have no verified Alpaca price for TMUS.

### 7. For the post-open review
- **SMH:** if SMH is above 537 at 10:05 and NVDA is above 210, close SMH (accept about −0.8R instead of −1R into PLTR and AMD). If SMH is below 528, hold.
- **XLE:** the close is ordered in `manage`. Confirm it filled.
- **ISM at 10:00:** a print below 52 (weak) argues for checking XHB's trigger; leave it if TLT is still bid. A print above 56 lifts yields: if XHB has not triggered, cancel it.
- **ORCL:** if the offering prices before 10:05 and the stock is trading above 128, cancel the sell stop.

### 8. Book state
With XLE closed and both new entries counted as filled: 8 of 8 slots. Risk at stake is about 2.75 − 0.51 + 0.5 + 0.5 ≈ **3.24%** of equity (cap 4%). Gross exposure is about 88% − 17% + 8% + 6% ≈ **85%** (cap 150%), and net exposure about **+24%** (cap ±100%).

Sources: [CNBC](https://www.cnbc.com/2026/11/01/stock-market-today-live-updates.html), [TipRanks](https://www.tipranks.com/news/stock-market-today-nov-2-futures-rise-ahead-of-earnings-and-midterm-elections-oil-prices-fall), [The National](https://www.thenationalnews.com/business/2026/11/02/oil-prices-slide-more-than-3-as-trump-signals-more-time-for-iran-diplomacy/), [IndiaInfoline](https://www.indiainfoline.com/news/international/crude-oil-slides-nearly-4-as-us-iran-talks-raise-hopes-of-peace-can-supply-risks-keep-prices-elevated), [StockTitan earnings week](https://www.stocktitan.net/articles/earnings-calendar-week-of-november-2-2026), [CMC Markets](https://www.cmcmarkets.com/en-au/market-news/the-week-ahead-apple-earnings-us-jobs-report-ism-pmi-reports), [Chartmill movers](https://www.chartmill.com/news/APA/Chartmill-57465-SP-500-Premarket-Movers-Nov-2-2026-IDEXX-and-Fox-Gain-Lumentum-and-T-Mobile-Fall), [GuruFocus ORCL](https://www.gurufocus.com/news/9162041/oracle-orcl-launches-mixed-shelf-offering-shares-dip-amid-ai-market-concerns), [StocksToTrade ORCL](https://stockstotrade.com/news/oracle-corporation-orcl-news-2026_11_02/)

```json
{
  "date": "2026-11-02",
  "no_trade": false,
  "session_note": "Relief bounce after the AI-capex selloff with oil -4% on Iran diplomacy; closing the failed XLE breakout, shorting ORCL's equity-raise breakdown, buying the XHB breakout on lower yields and oil.",
  "plays": [
    {
      "ticker": "ORCL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 122.40,
      "stop": 130.40,
      "targets": [110.40],
      "time_horizon": "1-4 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.36,
      "catalyst": "About $10B equity/mixed shelf offering announced 2026-11-02 pre-market plus Oracle Health data breach disclosure.",
      "thesis": "Oracle is the clearest case of AI capex financed with debt and now equity; a $10B raise into a market punishing capex confirms financing strain. A break of the 122.76 20d low turns the gap into a range breakdown.",
      "invalidation": "Offering prices at a small discount and ORCL closes back above 128.",
      "bear_case": "Raising capital removes the financing overhang and a priced deal often marks the low; an analyst upgrade is out today and dip buyers have been active."
    },
    {
      "ticker": "XHB",
      "direction": "long",
      "entry_type": "stop",
      "entry": 103.10,
      "stop": 100.40,
      "targets": [107.20],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.5,
      "p_target_first": 0.37,
      "catalyst": "Rates rally on 2026-11-02 (TLT above its 20d high) coinciding with oil -4% on US-Iran diplomacy.",
      "thesis": "Homebuilders benefit directly when yields and energy costs fall together; XHB is just under its 102.86 20d high and above its 20/50d averages. A break opens continuation with the rotation into cyclicals.",
      "invalidation": "TLT closes back below 81 while XHB holds the breakout, meaning the rate impulse is gone.",
      "bear_case": "One day of a rate rally on an oil headline; Iran talks can reverse overnight and the 20d high has capped XHB before."
    }
  ],
  "manage": [
    {
      "ticker": "XLE",
      "action": "close",
      "reason": "Thesis was energy repricing $100+ oil; WTI is back under $100 on Iran diplomacy and the 69.86 breakout has failed, with the stop only 0.5 ATR away."
    }
  ],
  "passed": [
    {
      "ticker": "UAL",
      "direction": "long",
      "entry_type": "limit",
      "entry": 107.00,
      "stop": 103.50,
      "targets": [114.00],
      "p_target_first": 0.40,
      "reason": "Chasing a +4.6% gap whose catalyst is a single Iran headline that can reverse overnight."
    },
    {
      "ticker": "TLT",
      "direction": "long",
      "entry_type": "stop",
      "entry": 82.10,
      "stop": 80.90,
      "targets": [83.90],
      "p_target_first": 0.38,
      "reason": "Midterms and Friday payrolls make the rates leg a coin flip; expressing lower yields via XHB instead."
    }
  ]
}
```

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Monday 2026-11-02. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$101,768.26**
- Cash: $99,202.84
- Session P&L so far: -0.42% (new entries are blocked at -3.0%)
- Gross exposure: $80,894 (79% of equity, cap 150%)
- Net exposure: $+2,568 (+3%, cap +/-100%)
- Risk at stake (entry to stop): $2,774 (2.73% of equity, cap 4.0%) — 1.27% left for new plays
- Slots: 7 open + 0 resting entries of 8 — you may add at most 1 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| GOOGL | short | 48 | 279.61 | 285.93 | -303 (-2.3%) | 290.50 | 258.40 | A break of the 280.36 opening-range low on the gap day confirms the bounce failed and selling continues; post-earnings d |
| KRE | long | 142 | 73.06 | 73.16 | +13 (+0.1%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| LLY | long | 5 | 1432.09 | 1399.40 | -163 (-2.3%) | 1385.00 | 1520.00 | Health care leads the rotation out of AI capex; LLY held its breakout at the open and extended from +2.9% pre-market to  |
| META | short | 9 | 616.20 | 620.31 | -37 (-0.7%) | 643.00 | 580.00 | Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward  |
| ORCL | short | 63 | 122.52 | 123.22 | -44 (-0.6%) | 130.40 | 110.40 | Oracle is the clearest case of AI capex financed with debt and now equity; a $10B raise into a market punishing capex co |
| SMH | short | 23 | 518.88 | 525.77 | -158 (-1.3%) | 541.00 | 486.00 | Semis are the most crowded AI-capex expression; a break of the 520.53 20d low converts the gap into a range breakdown be |
| XLP | long | 270 | 89.90 | 90.17 | +73 (+0.3%) | 88.00 | 93.50 | Money leaving AI-capex names is going to staples; a pullback to the 89.99 breakout level is a retest that buys the rotat |

### Record

34 closed trades: 12W / 22L, total +1.88R, net $+2,402 realized. Shorts taken: 32.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLE | long | close | -0.46R | $-236 | 38% |
| TSLA | long | stop | -0.52R | $-129 | 35% |
| MSFT | long | close | -0.80R | $-324 | 38% |
| XLV | long | target | +1.65R | $+837 | 40% |
| NVDA | short | close | -0.76R | $-190 | 35% |

### Ideas you passed on, replayed against the tape

77 resolved: 21 reached target first, 35 stop first, 15 never reached the entry, 6 expired, 0 ambiguous. Average -0.01R across the 62 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-28 pre-market | UAL | short | Oil headwind real but 4.8% ATR and +7% in 5d; last UAL short stopped out. | stop | -1.49R | 33% |
| 2026-10-26 pre-market | AVGO | short | Would be a fourth AI/tech short stacked into MSFT and GOOGL earnings and the FOM | never filled | - | 33% |
| 2026-10-26 pre-market | TLT | long | 20d-high breakout, but FOMC and PCE make the inflation side a coin flip; the slo | never filled | - | 35% |
| 2026-10-30 pre-market | AMZN | short | Post-earnings -7.4% gap is already the move; left to the post-open review for op | stop | -0.34R | 35% |
| 2026-10-20 open | XLV | long | Healthcare leading, but chasing a +1.9% day through the 20d high; book already h | target | +2.26R | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 285.95 (10:05 iex) | +2.2% | 279.84 | 282.38 / 282.32-286.96 | 10.84 (3.9%) | 276.92-359.40 | -16.2% / -17.5% | -12.6% | 33.2M |
| KRE | 73.14 (10:05 iex) | +1.6% | 72.01 | 72.54 / 72.49-73.35 | 1.33 (1.8%) | 67.79-73.45 | +2.0% / +0.3% | -0.6% | 14.6M |
| LLY | 1,399.40 (10:05 iex) | -1.3% | 1,417.54 | 1,393.15 / 1,387.10-1,411.48 | 48.24 (3.4%) | 1,131.21-1,449.68 | +13.8% / +18.4% | +11.3% | 2.6M |
| META | 619.98 (10:05 iex) | +0.8% | 614.99 | 614.29 / 610.00-620.41 | 25.05 (4.1%) | 609.00-771.27 | -11.0% / -8.2% | -4.3% | 23.2M |
| ORCL | 123.26 (10:05 iex) | -5.7% | 130.67 | 125.88 / 122.25-126.50 | 8.04 (6.2%) | 122.76-148.48 | -2.9% / -7.6% | +3.6% | 31.7M |
| SMH | 525.66 (10:05 iex) | +0.6% | 522.49 | 529.09 / 524.59-529.22 | 21.01 (4.0%) | 511.63-639.47 | -8.3% / -8.8% | -0.9% | 9.4M |
| XLP | 90.14 (10:05 iex) | +0.8% | 89.42 | 89.84 / 89.83-90.55 | 1.47 (1.6%) | 80.10-90.38 | +4.0% / +6.0% | +1.3% | 15.0M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 760.40 (10:05 iex) | +0.6% | 755.72 | 759.46 / 758.72-760.71 | 8.30 (1.1%) | 750.36-781.62 | -1.9% / -1.4% | -0.6% | 39.3M |
| QQQ | 694.58 (10:05 iex) | +0.6% | 690.49 | 695.31 / 693.30-695.96 | 14.38 (2.1%) | 683.45-762.86 | -5.2% / -4.7% | -2.0% | 39.4M |
| IWM | 282.15 (10:05 iex) | +1.0% | 279.33 | 281.64 / 280.54-283.03 | 4.02 (1.4%) | 269.88-285.26 | +0.7% / -1.7% | +1.3% | 24.0M |
| DIA | 522.44 (10:03 iex) | +1.0% | 517.13 | 520.89 / 520.65-522.88 | 5.36 (1.0%) | 507.73-528.45 | -0.4% / -0.8% | -0.8% | 3.3M |
| TLT | 82.03 (10:05 iex) | +0.6% | 81.50 | 81.83 / 81.79-82.03 | 0.85 (1.0%) | 76.11-81.69 | +2.7% / +2.0% | +0.6% | 38.3M |
| GLD | 362.72 (10:05 iex) | +2.0% | 355.78 | 361.74 / 361.58-363.42 | 5.87 (1.7%) | 354.67-385.17 | -5.3% / -8.9% | -3.0% | 8.4M |
| USO | 158.78 (10:05 iex) | -6.0% | 168.83 | 159.52 / 158.52-159.74 | 4.80 (2.8%) | 141.76-171.82 | +7.1% / +12.5% | -0.4% | 4.6M |
| SMH | 525.66 (10:05 iex) | +0.6% | 522.49 | 529.09 / 524.59-529.22 | 21.01 (4.0%) | 511.63-639.47 | -8.3% / -8.8% | -0.9% | 9.4M |
| XLK | 179.17 (10:05 iex) | -0.2% | 179.51 | 180.40 / 178.84-180.53 | 4.87 (2.7%) | 176.92-203.25 | -5.9% / -5.3% | -2.0% | 9.2M |
| XLF | 57.33 (10:05 iex) | +1.5% | 56.51 | 56.92 / 56.87-57.39 | 0.75 (1.3%) | 53.30-57.23 | +2.1% / +1.2% | +1.1% | 32.6M |
| XLE | 68.60 (10:05 iex) | -2.0% | 70.02 | 68.85 / 68.08-69.14 | 1.43 (2.0%) | 62.05-70.15 | +4.3% / +8.1% | +1.0% | 31.4M |
| XLV | 183.83 (10:05 iex) | -0.6% | 184.87 | 184.69 / 183.50-185.56 | 3.35 (1.8%) | 165.19-187.99 | +5.2% / +7.5% | +3.1% | 9.4M |
| XLI | 170.33 (10:05 iex) | +1.8% | 167.40 | 169.04 / 168.74-170.36 | 2.75 (1.6%) | 162.97-172.34 | -0.4% / -1.8% | +1.7% | 7.7M |
| XLY | 118.17 (10:05 iex) | +2.4% | 115.38 | 116.89 / 116.81-118.31 | 1.74 (1.5%) | 109.50-116.77 | +1.6% / +2.0% | +2.0% | 7.1M |
| XLP | 90.14 (10:05 iex) | +0.8% | 89.42 | 89.84 / 89.83-90.55 | 1.47 (1.6%) | 80.10-90.38 | +4.0% / +6.0% | +1.3% | 15.0M |
| XLU | 43.37 (10:05 iex) | -0.1% | 43.43 | 43.31 / 43.24-43.48 | 0.63 (1.4%) | 39.58-43.65 | +3.5% / +4.3% | +2.0% | 28.2M |
| XLB | 53.74 (10:05 iex) | +1.9% | 52.74 | 53.23 / 53.13-53.79 | 0.67 (1.3%) | 48.51-52.78 | +4.0% / +3.6% | +2.8% | 10.5M |
| XLRE | 43.36 (10:05 iex) | +0.4% | 43.17 | 43.26 / 43.09-43.48 | 0.65 (1.5%) | 40.28-43.45 | +2.9% / +1.6% | +1.4% | 8.1M |
| XLC | 101.27 (10:05 iex) | +1.4% | 99.90 | 100.38 / 100.26-101.31 | 1.89 (1.9%) | 99.33-113.17 | -7.8% / -9.6% | -5.3% | 6.8M |
| KRE | 73.14 (10:05 iex) | +1.6% | 72.01 | 72.54 / 72.49-73.35 | 1.33 (1.8%) | 67.79-73.45 | +2.0% / +0.3% | -0.6% | 14.6M |
| XHB | 104.08 (10:05 iex) | +3.1% | 100.97 | 102.53 / 102.53-104.45 | 2.53 (2.5%) | 91.87-102.86 | +4.5% / +2.6% | +2.6% | 2.3M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 340.45 (10:05 iex) | -1.2% | 344.63 | 342.67 / 339.67-343.80 | 6.70 (1.9%) | 330.62-351.73 | +0.7% / +3.5% | -0.9% | 40.6M |
| MSFT | 524.10 (10:05 iex) | +0.4% | 521.91 | 524.01 / 520.50-528.48 | 11.74 (2.2%) | 514.35-551.15 | -1.7% / +1.8% | -0.5% | 22.2M |
| NVDA | 207.99 (10:05 iex) | +1.6% | 204.64 | 207.56 / 206.73-209.03 | 6.54 (3.2%) | 200.92-243.37 | -7.6% / -7.7% | -3.0% | 101.8M |
| AMZN | 250.01 (10:05 iex) | +4.0% | 240.35 | 243.01 / 242.28-251.09 | 7.71 (3.2%) | 229.36-265.34 | -5.5% / -5.5% | -3.1% | 41.8M |
| GOOGL | 285.95 (10:05 iex) | +2.2% | 279.84 | 282.38 / 282.32-286.96 | 10.84 (3.9%) | 276.92-359.40 | -16.2% / -17.5% | -12.6% | 33.2M |
| META | 619.98 (10:05 iex) | +0.8% | 614.99 | 614.29 / 610.00-620.41 | 25.05 (4.1%) | 609.00-771.27 | -11.0% / -8.2% | -4.3% | 23.2M |
| TSLA | 402.75 (10:05 iex) | +0.7% | 399.81 | 404.66 / 397.61-410.45 | 14.38 (3.6%) | 349.33-410.85 | +5.0% / +8.2% | +7.4% | 36.6M |
| AVGO | 329.41 (10:05 iex) | +1.0% | 326.08 | 328.37 / 324.31-329.52 | 12.98 (4.0%) | 319.30-380.84 | -5.7% / -7.5% | +1.4% | 22.3M |
| AMD | 503.25 (10:05 iex) | -0.3% | 504.80 | 510.42 / 502.12-512.82 | 32.19 (6.4%) | 492.21-658.52 | -11.5% / -7.9% | -2.3% | 20.6M |
| ORCL | 123.26 (10:05 iex) | -5.7% | 130.67 | 125.88 / 122.25-126.50 | 8.04 (6.2%) | 122.76-148.48 | -2.9% / -7.6% | +3.6% | 31.7M |
| NFLX | 62.09 (10:05 iex) | +0.0% | 62.08 | 62.20 / 61.88-62.85 | 2.11 (3.4%) | 61.39-73.07 | -8.1% / -14.6% | -5.7% | 44.8M |
| CRM | 230.90 (10:04 iex) | +0.8% | 229.17 | 229.75 / 228.38-232.30 | 9.32 (4.1%) | 220.29-252.42 | -3.5% / -4.0% | -7.8% | 7.1M |
| JPM | 341.55 (10:04 iex) | +1.3% | 337.04 | 340.95 / 339.92-342.43 | 6.97 (2.1%) | 325.07-345.75 | +0.7% / -1.5% | +1.6% | 6.9M |
| GS | 914.15 (10:03 iex) | +2.2% | 894.55 | 908.80 / 903.00-915.63 | 27.38 (3.1%) | 859.03-939.38 | +0.1% / -5.5% | +2.2% | 2.3M |
| BAC | 50.28 (10:05 iex) | +0.5% | 50.01 | 50.45 / 50.01-50.47 | 1.32 (2.6%) | 49.26-54.93 | -3.7% / -11.3% | -1.1% | 41.2M |
| XOM | 182.57 (10:04 iex) | -2.5% | 187.25 | 183.98 / 181.56-184.59 | 4.14 (2.2%) | 161.39-188.50 | +6.4% / +11.6% | +2.2% | 12.0M |
| CVX | 232.09 (10:03 iex) | -1.5% | 235.52 | 232.50 / 229.65-233.25 | 4.73 (2.0%) | 201.96-236.48 | +6.2% / +10.5% | +1.0% | 7.5M |
| LLY | 1,399.40 (10:05 iex) | -1.3% | 1,417.54 | 1,393.15 / 1,387.10-1,411.48 | 48.24 (3.4%) | 1,131.21-1,449.68 | +13.8% / +18.4% | +11.3% | 2.6M |
| UNH | 398.87 (10:05 iex) | -2.0% | 406.97 | 406.00 / 397.55-408.88 | 12.92 (3.2%) | 368.05-426.55 | +2.1% / +4.5% | -2.7% | 6.1M |
| JNJ | 268.70 (10:05 iex) | -1.6% | 273.20 | 272.06 / 268.32-273.01 | 7.74 (2.8%) | 245.17-282.01 | +4.8% / +2.9% | +3.6% | 7.7M |
| WMT | 125.56 (10:04 iex) | +1.7% | 123.51 | 124.12 / 124.09-125.88 | 2.64 (2.1%) | 103.39-124.51 | +6.5% / +12.0% | +3.0% | 19.9M |
| COST | 1,024.09 (10:05 iex) | +1.2% | 1,012.28 | 1,017.01 / 1,014.34-1,029.33 | 17.58 (1.7%) | 913.40-1,021.31 | +3.7% / +7.5% | +1.0% | 2.2M |
| HD | 336.49 (10:05 iex) | +2.2% | 329.20 | 334.08 / 333.00-337.81 | 7.67 (2.3%) | 279.76-334.80 | +7.3% / +6.9% | +2.9% | 4.7M |
| CAT | 626.71 (10:04 iex) | +0.6% | 622.75 | 630.00 / 618.64-632.00 | 31.92 (5.1%) | 616.66-874.87 | -16.1% / -20.3% | -9.1% | 3.2M |
| BA | 176.04 (10:05 iex) | +2.6% | 171.55 | 173.21 / 172.78-176.13 | 5.78 (3.4%) | 165.01-195.23 | -7.4% / -12.5% | -8.9% | 9.9M |
| DAL | 83.24 (10:04 iex) | +3.9% | 80.15 | 83.04 / 82.24-83.78 | 3.13 (3.9%) | 74.14-85.51 | +0.8% / -0.2% | +4.4% | 7.1M |
| UAL | 110.81 (10:04 iex) | +6.3% | 104.24 | 108.96 / 108.12-111.29 | 4.94 (4.7%) | 94.54-115.20 | +1.0% / -3.2% | +6.4% | 5.3M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-11-02 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| CLRO | 6.25 (10:05 iex) | +83.3% | 3.41 | 6.68 / 6.05-7.40 | 1.01 (29.7%) | 1.62-6.23 | -4.9% / -21.5% | +4.9% | 7.7M |
| LITZ | 31.85 (10:03 iex) | +22.8% | 25.93 | 28.38 / 28.38-32.21 | 4.45 (17.2%) | 16.35-36.00 | +4.2% / -5.3% | -24.3% | 1.6M |
| AIOK | 15.26 (09:49 sip) | -36.9% | 24.17 | 19.10 / 14.43-19.10 | 5.03 (20.8%) | 3.90-31.09 | - / - | +101.1% | 7.4M |
| PGEN | 5.09 (10:05 iex) | -26.7% | 6.94 | 5.33 / 4.91-5.37 | 0.43 (6.2%) | 5.96-8.60 | -0.0% / -3.8% | +12.1% | 4.9M |
| LITX | 18.10 (10:03 iex) | -22.3% | 23.29 | 21.07 / 17.72-21.17 | 4.23 (18.1%) | 18.24-46.06 | -22.0% / -24.7% | +21.3% | 3.4M |
