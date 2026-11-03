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

Research is done. AAPL is gapping down after earnings, PLTR is lower, AMD reports tonight, voting in the midterms is under way, and oil is up again after a US strike on Iran. Next I'll write the brief.

# Pre-market brief: Tuesday 2026-11-03, 09:05 ET / 15:05 Stockholm

### 1. Tape
The open is mixed and splits by sector. Dow futures are about −0.7/−0.8%, S&P futures about −0.1%, and Nasdaq-100 futures +0.2/+0.4% (verified: StockTitan, TradingKey). Semis are bouncing ahead of AMD's report tonight (SMH 522.45, +2.8%; NVDA +2.3%; AMD +4.6%). Mega-cap software and platforms are not: AAPL is −4.2% at 324.23 after a weak gross-margin guide (45–46% against a 46.3% estimate, with memory costs rising), PLTR is about −8% after earnings, and SHOP is about −16%. Brent is back above $105 after a US strike on Iran's Qeshm Island, but it has given back little of Monday's ~7% fall (sources disagree on the exact figure; USO in the table is −1.5%, which may reflect Monday's settle). The 10-year is around 4.91%. The midterms are being voted on today and results arrive tonight, after the review, so they are overnight gap risk on everything we hold. The regime is still rotation out of AI-capex and mega-cap tech into financials, staples and cyclicals, with a short-covering bounce in semis inside it. **Edge: short, in mega-cap tech that has failed on earnings.** Today's semis strength is a bounce into a binary event.

### 2. Calendar
| Time ET | Stockholm | Event | Status / consensus | Touches |
|---|---|---|---|---|
| Overnight | — | AAPL FQ4 (Mon after close) | Revenue $114.48B beat $113.39B; Dec-qtr GM guide 45–46% against 46.3% est.; stock −4.2% pre-market | AAPL (new) |
| Overnight | — | PLTR Q3 (Mon after close) | Beat and raised, but TCV only +6%; stock about −8% pre-market | SMH/AI sentiment |
| 07:00 approx | 13:00 | PFE, YUM, ZBRA, IT earnings | PFE beat and is flat; ZBRA and IT −6% | none |
| 10:00 | 16:00 | JOLTS (Sep), factory orders | Could not verify consensus | KRE, XHB through rates |
| All day | — | US midterm elections | Results after the close and overnight | everything; gap risk |
| After close | after 22:00 | AMD Q3 | Consensus about $13.09B revenue, $1.95 EPS (single source) | SMH short |
| Fri 11-06 | — | October payrolls | — | XHB, KRE |

### 3. Open positions and resting entries
- **GOOGL short** (279.61 → 279.82, stop 290.50, target 258.40). **Intact.** It is pinned near the 276.92 20-day low and lagging the Nasdaq bounce. Hold.
- **META short** (616.20 → 608.67, stop 643, target 580). **Intact.** It sits right at the 606.41 20-day low; a break of that level is the continuation. Hold.
- **ORCL short** (122.52 → 120.70, stop 130.40, target 110.40). **Intact.** The $20B debt-plus-equity financing is still overhanging the stock and the offering has not priced. The +1.2% pre-market move is sympathy with semis. Hold.
- **SMH short** (518.88 → 522.45, stop 541, target 486). **Weakening in the short run, intact structurally.** It is bouncing 2.8% into AMD tonight. AMD's earnings are not a binary event under rule 8 for an ETF position, but they are real gap risk. The stop sits 18.5 above the market, below 1 ATR, and at full size that is a 1R loss. Last week's thesis, a breakdown of the AI-capex leader group, is not invalidated by a pre-event squeeze. Hold, with the rule for the review in section 7.
- **KRE long** (73.06 → 73.86, stop 71.25, target 76.20). **Intact.** It is near the 74.19 20-day high, and a steep curve with the 10-year at about 4.9% helps. Hold.
- **XLP long** (89.90 → 90.06, stop 88.00, target 93.50). **Intact, but being tested.** It is −0.8% pre-market as money rotates back into semis for the day. It is still above the 89.99 retest level, and the 88 stop sits below the breakout zone. Hold.
- **XHB resting long limit 103.00** (last 104.38, stop 100.90, target 107.20). **Keep.** It is a retest buy of yesterday's breakout above 102.86. A rates spike overnight after the midterms could fill it on a gap. That is the known risk of a limit order, and the 100.90 stop sits under Friday's close.

No manage changes.

### 4. New plays

**AAPL short: post-earnings failed retest**
| Field | Value |
|---|---|
| Ticker | AAPL |
| Direction | Short |
| Catalyst | 2026-11-02 FQ4 report: Dec-qtr GM guide 45–46% against 46.3% est., memory-cost pressure, iPad miss; stock −4.2% pre-market at 324.23, below the 330.62 20-day low |
| Thesis | Margin compression from memory costs is a multi-quarter story, not a one-day reset, and the tape is punishing mega-cap tech that disappoints (GOOGL, META, MSFT this cycle). A bounce back to the broken 20-day low at about 330 is the place to sell. |
| Entry | 330.00 limit (sell), back at the broken 20-day low of 330.62 |
| Stop | 338.80. Above the 338.32 prior close, so a full gap fill proves the market shrugged the guide off. Risk 8.80, about 1.3 ATR. |
| Target | 312.00 (2.05R) |
| Risk tier | 0.25. Probe size: it would be the fifth tech/AI-adjacent short, with tech-sector net exposure near the 40% cap, and mega-cap earnings gaps often get bought. |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 0.33 |
| Invalidation | AAPL reclaims and closes above 334 within two sessions, or a rally back above 330 from a broad tech squeeze holds through the close |
| What I'd be wrong about | Apple's gap-downs are bought more reliably than other mega-caps': revenue beat, buybacks, and the guide misses by only about 0.3–1.3pt. It may never bounce to 330, leaving no fill and no exposure, or bounce straight through to fill the gap. |

### 5. Both sides
- **Best short: AAPL**, taken above as a 0.25 probe.
- **Best long: XLI** at a 171.00 limit, stop 167.50, target 177.00, P = 0.35. Industrials are leading the rotation (+0.7% pre-market, near the 172.34 20-day high). Passed: no slot is left after AAPL, and it overlaps the cyclical long already in XHB and KRE.

### 6. Passing on
- **XLI long**: see above; no slot.
- **PLTR short**: −8% to about 163.80 (seen in one pre-market source and not in my market table). I could not confirm the level well enough to trade it, and it would stack more AI shorts.
- **SHOP short**: −16% gap. The move already happened; a pass with no levels.
- **SMH / AMD into earnings, either side**: it is a coin flip on a binary event, and I am already short SMH.

### 7. For the post-open review
- **AAPL:** if it opens weak and breaks its opening-range low with no bounce toward 330 by 10:05, leave the limit in place; do not chase below 320. If it is already back above 334 by 10:05 (the gap is being bought), cancel the limit.
- **SMH:** if SMH is above 535 at 10:05 with NVDA above 212, close it before AMD (take about −0.7R rather than risk a full −1R overnight gap). Otherwise hold.
- **JOLTS at 10:00:** a sharply strong print that pushes the 10-year toward 5% argues for cancelling the XHB limit. Otherwise keep it.

### 8. Book state
If AAPL fills: 8 of 8 slots. Risk at stake is about 2.97% + 0.25% ≈ **3.22%** (cap 4%). Gross exposure is about 96% + 9% ≈ **105%** (cap 150%), and net about **+12%** (cap ±100%).

Sources: [StockTitan](https://www.stocktitan.net/articles/stock-market-today-live-november-3-2026), [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262267546-us-premarket-futures-mixed-aapl-down-4-pltr-down-8-amd-earnings-ahead-tradingkey), [CNBC premarket movers](https://www.cnbc.com/2026/11/03/stocks-making-the-biggest-moves-premarket-pfe-pltr-aapl-zbra.html), [CNBC Apple/Palantir](https://www.cnbc.com/2026/11/03/apple-palantir-stock-earnings.html), [Tradingpedia](https://www.tradingpedia.com/2026/11/03/apple-shares-fall-as-margin-outlook-china-eclipse-beat/), [Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-november-3-dow-sp-500-nasdaq-midterms-amd-090846378.html), [TT News oil](https://www.ttnews.com/articles/oil-prices-us-attacks-iran), [Trading Economics Brent](https://tradingeconomics.com/commodity/brent-crude-oil), [KuCoin PLTR](https://www.kucoin.com/news/flash/palantir-stock-drops-8-15-in-premarket-despite-strong-q3-earnings), [TradingKey AMD](https://www.tradingkey.com/analysis/stocks/us-stocks/262267536-ahead-amd-earnings-shares-up-premarket-helios-volume-pc-demand-tradingkey)

```json
{
  "date": "2026-11-03",
  "no_trade": false,
  "session_note": "Mixed open on midterm day: AAPL/PLTR punished on earnings while semis squeeze into AMD tonight; rotation regime intact. Holding all positions, adding an AAPL post-earnings short probe on a bounce to the broken 20d low.",
  "plays": [
    {
      "ticker": "AAPL",
      "direction": "short",
      "entry_type": "limit",
      "entry": 330.00,
      "stop": 338.80,
      "targets": [312.00],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.33,
      "catalyst": "2026-11-02 FQ4 report: Dec-qtr gross-margin guide 45-46% vs 46.3% est on memory costs, iPad miss; stock -4.2% pre-market below the 330.62 20d low.",
      "thesis": "Memory-cost margin compression is multi-quarter and the tape is punishing mega-cap tech that disappoints. A bounce to the broken 20d low near 330 is the place to sell, with the stop above the full gap fill.",
      "invalidation": "AAPL closes back above 334 within two sessions, or a broad tech squeeze carries it above 330 into the close.",
      "bear_case": "Apple gap-downs get bought reliably; revenue beat and buybacks, and the guide miss is small. It may never bounce to 330 or may fill the gap outright."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "XLI",
      "direction": "long",
      "entry_type": "limit",
      "entry": 171.00,
      "stop": 167.50,
      "targets": [177.00],
      "p_target_first": 0.35,
      "reason": "Best long: industrials leading the rotation near the 172.34 20d high, but no slot left and overlaps XHB/KRE cyclical exposure."
    }
  ]
}
```

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Tuesday 2026-11-03. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,115.17**
- Cash: $90,890.96
- Session P&L so far: -1.02% (new entries are blocked at -3.0%)
- Gross exposure: $107,845 (106% of equity, cap 150%)
- Net exposure: $+11,224 (+11%, cap +/-100%)
- Risk at stake (entry to stop): $3,284 (3.22% of equity, cap 4.0%) — 0.78% left for new plays
- Slots: 8 open + 0 resting entries of 8 — you may add at most 0 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 44% of equity in notional: at 1% risk its stop must be at least 2.3% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 44% of equity in notional: at 1% risk its stop must be at least 2.3% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AAPL | short | 29 | 330.06 | 333.00 | -85 (-0.9%) | 338.80 | 312.00 | Memory-cost margin compression is multi-quarter and the tape is punishing mega-cap tech that disappoints. A bounce to th |
| GOOGL | short | 48 | 279.61 | 277.84 | +85 (+0.6%) | 290.50 | 258.40 | A break of the 280.36 opening-range low on the gap day confirms the bounce failed and selling continues; post-earnings d |
| KRE | long | 142 | 73.06 | 73.43 | +53 (+0.5%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| META | short | 9 | 616.20 | 615.11 | +10 (+0.2%) | 643.00 | 580.00 | Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward  |
| ORCL | short | 63 | 122.52 | 124.75 | -140 (-1.8%) | 130.40 | 110.40 | Oracle is the clearest case of AI capex financed with debt and now equity; a $10B raise into a market punishing capex co |
| SMH | short | 23 | 518.88 | 518.35 | +12 (+0.1%) | 541.00 | 486.00 | Semis are the most crowded AI-capex expression; a break of the 520.53 20d low converts the gap into a range breakdown be |
| XHB | long | 242 | 102.93 | 103.15 | +53 (+0.2%) | 100.90 | 107.20 | Homebuilders benefit when yields and energy costs fall together; the breakout above 102.86 is confirmed. Buying the firs |
| XLP | long | 270 | 89.90 | 89.42 | -128 (-0.5%) | 88.00 | 93.50 | Money leaving AI-capex names is going to staples; a pullback to the 89.99 breakout level is a retest that buys the rotat |

### Record

35 closed trades: 12W / 23L, total +1.31R, net $+2,268 realized. Shorts taken: 33.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| LLY | long | stop | -0.57R | $-134 | 40% |
| XLE | long | close | -0.46R | $-236 | 38% |
| TSLA | long | stop | -0.52R | $-129 | 35% |
| MSFT | long | close | -0.80R | $-324 | 38% |
| XLV | long | target | +1.65R | $+837 | 40% |

### Ideas you passed on, replayed against the tape

81 resolved: 24 reached target first, 36 stop first, 15 never reached the entry, 6 expired, 0 ambiguous. Average +0.06R across the 66 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-26 pre-market | AAPL | short | Best short (iPhone 18 Pro order cuts), but its own earnings are inside the horiz | target | +2.13R | 33% |
| 2026-10-29 pre-market | CAT | short | -11% gap already the move; only a bounce or an opening-range breakdown offers lo | target | +1.80R | 34% |
| 2026-10-27 pre-market | CVX | long | Duplicates XOM energy exposure, and its own Oct 30 earnings fall inside the hori | stop | -1.00R | 36% |
| 2026-10-30 open | AMZN | long | Gap reversal from -7.4% to -2.3% is real demand, but price is still under the 24 | target | +1.49R | 33% |
| 2026-10-28 pre-market | UAL | short | Oil headwind real but 4.8% ATR and +7% in 5d; last UAL short stopped out. | stop | -1.49R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 332.91 (10:05 iex) | -1.6% | 338.32 | 325.58 / 325.33-334.48 | 6.80 (2.0%) | 330.62-351.73 | -1.2% / +1.4% | -1.6% | 42.1M |
| GOOGL | 277.76 (10:05 iex) | -0.4% | 278.99 | 280.23 / 277.80-281.36 | 10.93 (3.9%) | 276.92-359.40 | -15.6% / -17.4% | -11.9% | 34.3M |
| KRE | 73.42 (10:05 iex) | -0.4% | 73.73 | 73.68 / 73.02-73.76 | 1.38 (1.9%) | 67.79-74.19 | +4.2% / +2.7% | +1.4% | 15.1M |
| META | 614.87 (10:05 iex) | +1.3% | 606.73 | 610.53 / 610.10-616.74 | 23.54 (3.9%) | 606.41-771.27 | -11.3% / -9.6% | -3.8% | 23.4M |
| ORCL | 124.65 (10:05 iex) | +4.6% | 119.22 | 122.00 / 121.35-125.23 | 8.30 (7.0%) | 118.43-148.48 | -10.7% / -15.4% | -5.4% | 33.7M |
| SMH | 518.21 (10:05 iex) | +1.9% | 508.31 | 520.68 / 517.26-524.44 | 21.73 (4.3%) | 506.44-639.47 | -9.8% / -11.1% | -6.2% | 9.6M |
| XHB | 103.17 (10:05 iex) | -1.3% | 104.58 | 104.02 / 102.57-104.61 | 2.70 (2.6%) | 91.87-104.90 | +7.8% / +6.3% | +6.8% | 2.3M |
| XLP | 89.44 (10:05 iex) | -1.5% | 90.83 | 89.90 / 89.21-90.24 | 1.51 (1.7%) | 81.03-90.99 | +5.0% / +7.5% | +3.3% | 15.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 753.16 (10:05 iex) | +0.1% | 752.10 | 752.72 / 752.39-754.68 | 8.97 (1.2%) | 750.36-781.62 | -2.2% / -1.9% | -1.7% | 39.6M |
| QQQ | 684.80 (10:04 iex) | +0.5% | 681.09 | 684.41 / 683.18-687.28 | 15.23 (2.2%) | 680.33-762.86 | -6.0% / -5.9% | -4.4% | 40.9M |
| IWM | 280.02 (10:05 iex) | +0.3% | 279.14 | 279.84 / 279.34-280.71 | 4.10 (1.5%) | 269.88-285.26 | +0.7% / -1.6% | +0.8% | 24.1M |
| DIA | 515.87 (10:05 iex) | -0.7% | 519.34 | 517.06 / 515.19-517.57 | 5.29 (1.0%) | 508.35-528.45 | -0.1% / -0.3% | -0.7% | 3.3M |
| TLT | 81.08 (10:05 iex) | -0.8% | 81.73 | 81.44 / 81.08-81.45 | 0.86 (1.1%) | 76.11-82.17 | +2.7% / +2.2% | +0.5% | 37.7M |
| GLD | 360.96 (10:04 iex) | -0.2% | 361.65 | 361.25 / 360.94-361.86 | 6.17 (1.7%) | 354.67-385.17 | -3.5% / -7.1% | -1.7% | 8.6M |
| USO | 156.88 (10:04 iex) | +0.0% | 156.87 | 157.44 / 156.83-157.96 | 5.45 (3.5%) | 141.76-171.82 | -0.9% / +4.2% | -5.6% | 4.8M |
| SMH | 518.21 (10:05 iex) | +1.9% | 508.31 | 520.68 / 517.26-524.44 | 21.73 (4.3%) | 506.44-639.47 | -9.8% / -11.1% | -6.2% | 9.6M |
| XLK | 176.16 (10:04 iex) | +1.1% | 174.22 | 175.41 / 174.80-177.28 | 5.19 (3.0%) | 173.91-203.25 | -8.1% / -8.0% | -6.5% | 9.6M |
| XLF | 57.14 (10:05 iex) | -0.7% | 57.56 | 57.36 / 56.96-57.47 | 0.76 (1.3%) | 53.41-57.70 | +3.7% / +3.0% | +2.7% | 33.2M |
| XLE | 66.71 (10:05 iex) | -0.8% | 67.25 | 66.62 / 66.46-67.48 | 1.54 (2.3%) | 62.93-70.15 | -0.1% / +3.7% | -3.4% | 32.5M |
| XLV | 184.88 (10:05 iex) | +0.2% | 184.60 | 183.68 / 183.62-185.72 | 3.27 (1.8%) | 165.19-187.99 | +4.6% / +7.2% | +3.0% | 9.7M |
| XLI | 170.77 (10:05 iex) | +0.6% | 169.71 | 170.82 / 170.34-171.34 | 2.82 (1.7%) | 162.97-172.34 | +1.0% / -0.3% | +1.6% | 7.8M |
| XLY | 117.16 (10:05 iex) | -0.9% | 118.16 | 118.32 / 116.83-118.39 | 1.96 (1.7%) | 110.58-119.20 | +3.7% / +4.4% | +3.4% | 7.4M |
| XLP | 89.44 (10:05 iex) | -1.5% | 90.83 | 89.90 / 89.21-90.24 | 1.51 (1.7%) | 81.03-90.99 | +5.0% / +7.5% | +3.3% | 15.8M |
| XLU | 43.40 (10:05 iex) | -0.6% | 43.67 | 43.56 / 43.29-43.64 | 0.61 (1.4%) | 40.41-43.80 | +3.6% / +4.8% | +2.6% | 27.8M |
| XLB | 52.80 (10:05 iex) | -1.6% | 53.67 | 53.50 / 52.78-53.53 | 0.72 (1.3%) | 48.70-54.03 | +5.4% / +5.4% | +4.5% | 10.7M |
| XLRE | 43.47 (10:04 iex) | -0.4% | 43.64 | 43.50 / 43.30-43.57 | 0.64 (1.5%) | 40.28-43.72 | +3.7% / +2.7% | +2.0% | 8.1M |
| XLC | 100.67 (10:05 iex) | +0.4% | 100.26 | 100.50 / 100.17-100.89 | 1.89 (1.9%) | 99.33-113.17 | -7.0% / -9.1% | -3.5% | 6.9M |
| KRE | 73.42 (10:05 iex) | -0.4% | 73.73 | 73.68 / 73.02-73.76 | 1.38 (1.9%) | 67.79-74.19 | +4.2% / +2.7% | +1.4% | 15.1M |
| XHB | 103.17 (10:05 iex) | -1.3% | 104.58 | 104.02 / 102.57-104.61 | 2.70 (2.6%) | 91.87-104.90 | +7.8% / +6.3% | +6.8% | 2.3M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 332.91 (10:05 iex) | -1.6% | 338.32 | 325.58 / 325.33-334.48 | 6.80 (2.0%) | 330.62-351.73 | -1.2% / +1.4% | -1.6% | 42.1M |
| MSFT | 511.35 (10:05 iex) | +0.8% | 507.12 | 509.49 / 507.82-512.60 | 12.79 (2.5%) | 504.96-551.15 | -4.3% / -1.2% | -4.8% | 22.6M |
| NVDA | 207.70 (10:05 iex) | +2.8% | 202.06 | 207.88 / 205.93-209.14 | 6.74 (3.3%) | 200.92-243.37 | -8.0% / -8.8% | -6.5% | 101.4M |
| AMZN | 246.48 (10:05 iex) | +0.3% | 245.63 | 248.68 / 245.95-249.82 | 8.36 (3.4%) | 229.36-265.34 | -3.3% / -3.3% | -1.4% | 42.7M |
| GOOGL | 277.76 (10:05 iex) | -0.4% | 278.99 | 280.23 / 277.80-281.36 | 10.93 (3.9%) | 276.92-359.40 | -15.6% / -17.4% | -11.9% | 34.3M |
| META | 614.87 (10:05 iex) | +1.3% | 606.73 | 610.53 / 610.10-616.74 | 23.54 (3.9%) | 606.41-771.27 | -11.3% / -9.6% | -3.8% | 23.4M |
| TSLA | 402.25 (10:05 iex) | -0.4% | 403.82 | 406.49 / 400.91-406.50 | 15.09 (3.7%) | 349.33-414.23 | +5.7% / +9.0% | +3.1% | 36.6M |
| AVGO | 332.72 (10:05 iex) | +3.3% | 322.23 | 328.97 / 326.60-335.74 | 13.02 (4.0%) | 319.30-380.84 | -6.2% / -8.4% | -2.1% | 22.2M |
| AMD | 486.58 (10:05 iex) | +4.2% | 466.84 | 479.99 / 473.54-497.40 | 32.99 (7.1%) | 466.07-658.52 | -17.0% / -14.8% | -12.1% | 21.5M |
| ORCL | 124.65 (10:05 iex) | +4.6% | 119.22 | 122.00 / 121.35-125.23 | 8.30 (7.0%) | 118.43-148.48 | -10.7% / -15.4% | -5.4% | 33.7M |
| NFLX | 62.33 (10:05 iex) | -0.0% | 62.34 | 62.57 / 61.90-63.02 | 2.12 (3.4%) | 61.39-73.07 | -7.4% / -13.8% | -2.4% | 45.0M |
| CRM | 217.23 (10:04 iex) | -4.0% | 226.18 | 222.40 / 214.67-222.59 | 9.08 (4.0%) | 220.29-252.42 | -4.6% / -5.4% | -8.7% | 7.1M |
| JPM | 339.45 (10:04 iex) | -0.3% | 340.58 | 340.00 / 338.63-340.75 | 6.42 (1.9%) | 325.07-345.75 | +1.6% / -0.4% | +2.0% | 7.0M |
| GS | 896.18 (10:05 iex) | -0.3% | 898.72 | 903.00 / 894.54-903.53 | 26.12 (2.9%) | 859.03-939.38 | +0.5% / -4.8% | +0.6% | 2.3M |
| BAC | 49.66 (10:05 iex) | +0.2% | 49.57 | 49.37 / 49.17-49.70 | 1.30 (2.6%) | 49.26-54.93 | -4.2% / -11.7% | -1.9% | 41.9M |
| XOM | 178.09 (10:04 iex) | -0.9% | 179.67 | 178.00 / 177.87-180.30 | 4.48 (2.5%) | 162.94-188.50 | +1.6% / +6.9% | -2.6% | 12.2M |
| CVX | 225.40 (10:05 iex) | -1.0% | 227.77 | 224.71 / 224.46-227.56 | 5.04 (2.2%) | 204.86-236.48 | +2.2% / +6.6% | -1.8% | 7.6M |
| LLY | 1,420.22 (10:05 iex) | +0.7% | 1,410.99 | 1,398.63 / 1,393.47-1,436.32 | 48.60 (3.4%) | 1,131.21-1,449.68 | +12.0% / +17.6% | +10.3% | 2.6M |
| UNH | 398.08 (10:05 iex) | -0.6% | 400.44 | 398.52 / 397.00-402.08 | 12.04 (3.0%) | 368.50-426.55 | +0.2% / +2.7% | -2.5% | 6.1M |
| JNJ | 269.75 (10:04 iex) | -0.3% | 270.56 | 268.51 / 267.74-270.56 | 6.82 (2.5%) | 245.17-282.01 | +3.4% / +1.9% | +1.6% | 7.6M |
| WMT | 125.51 (10:05 iex) | -1.7% | 127.69 | 126.56 / 125.12-126.85 | 2.77 (2.2%) | 104.50-127.94 | +9.1% / +15.3% | +6.2% | 20.4M |
| COST | 1,026.35 (10:04 iex) | -1.4% | 1,040.55 | 1,031.57 / 1,021.00-1,034.77 | 18.87 (1.8%) | 917.64-1,042.57 | +5.9% / +10.2% | +3.7% | 2.2M |
| HD | 334.17 (10:05 iex) | -2.0% | 341.15 | 337.25 / 332.11-338.78 | 8.12 (2.4%) | 282.13-341.54 | +10.1% / +10.7% | +6.8% | 4.7M |
| CAT | 618.21 (10:05 iex) | +0.7% | 613.62 | 618.94 / 617.01-623.22 | 30.36 (4.9%) | 609.89-874.87 | -16.1% / -21.1% | -11.3% | 3.3M |
| BA | 175.03 (10:05 iex) | -0.2% | 175.40 | 175.26 / 173.84-176.40 | 5.95 (3.4%) | 165.01-193.28 | -4.9% / -10.2% | -6.9% | 10.0M |
| DAL | 83.12 (10:05 iex) | -0.4% | 83.42 | 83.91 / 82.92-84.70 | 3.25 (3.9%) | 74.14-85.51 | +4.9% / +3.9% | +5.4% | 7.1M |
| UAL | 108.80 (10:04 iex) | -0.4% | 109.24 | 110.30 / 108.28-111.25 | 5.27 (4.8%) | 94.54-115.20 | +5.9% / +1.6% | +8.5% | 5.3M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-11-03 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AEHR | 62.41 (10:05 iex) | +21.3% | 51.47 | 57.20 / 54.01-63.44 | 6.49 (12.6%) | 50.52-107.93 | -24.5% / -37.7% | -9.1% | 2.8M |
| BEX | 19.95 (10:05 iex) | +20.5% | 16.56 | 18.88 / 18.62-20.47 | 4.01 (24.2%) | 15.66-42.45 | -36.1% / -44.5% | -9.6% | 3.4M |
| AXTX | 13.39 (10:05 iex) | +18.4% | 11.31 | 11.51 / 11.18-13.61 | 4.09 (36.1%) | 10.87-44.60 | -45.0% / -56.3% | -30.9% | 4.8M |
| SUPN | 29.34 (10:04 iex) | -30.0% | 41.92 | 28.35 / 28.35-31.20 | 2.04 (4.9%) | 37.54-44.31 | +1.4% / -1.2% | +2.8% | 1.1M |
| AIOK | 10.07 (09:53 iex) | -20.2% | 12.63 | 11.01 / 9.32-11.21 | 5.88 (46.6%) | 3.90-31.09 | - / - | +37.9% | 7.1M |
| BEZ | 6.45 (10:04 iex) | -20.5% | 8.11 | 6.95 / 6.23-7.13 | 1.23 (15.1%) | 4.18-9.16 | +25.9% / +19.3% | +2.5% | 5.0M |
| ADTN | 5.03 (10:03 iex) | -19.9% | 6.28 | 6.18 / 5.03-6.20 | 0.29 (4.6%) | 6.28-7.91 | -8.0% / -11.6% | -4.1% | 1.5M |
| IREZ | 22.09 (09:49 sip) | -16.8% | 26.56 | 25.47 / 22.09-26.08 | 3.75 (14.1%) | 9.12-26.82 | +50.7% / +105.7% | +22.1% | 1.6M |
| ADEA | 17.37 (10:03 iex) | -16.0% | 20.67 | 17.21 / 16.95-17.94 | 1.17 (5.7%) | 19.89-26.34 | -7.3% / -14.9% | -3.5% | 1.2M |
| DT | 47.33 (10:05 iex) | -14.2% | 55.13 | 46.00 / 45.52-49.20 | 2.49 (4.5%) | 54.88-66.30 | -11.5% / -4.5% | -14.1% | 7.8M |
