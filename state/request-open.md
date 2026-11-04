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

Quick update: slots are full (8 of 8), so today's brief is mainly about managing the existing positions. I've checked the overnight news (the Democratic midterm sweep, AMD's earnings beat, the ADP print), and the AAPL short is already through its stop pre-market. Writing the brief now.

# Pre-market brief: Wednesday 2026-11-04 (09:05 ET / 15:05 Stockholm, ET+6)

### 1. Tape
Democrats won both chambers of Congress overnight, and Trump said he would accept the result. That removed a source of uncertainty, and buyers came into the broad index dip. In the Alpaca table, SPY is +1.2%, DIA +2.1% and IWM +1.8%, but QQQ is only +0.2% and SMH −1.6%. The market is splitting, not rising evenly. AI data-center names are being sold on fears that Democratic governors in Texas, Ohio and Georgia will restrict new builds: ORCL is −3.1%, NVDA −1.2%, TSLA −5.3%, and sources report CRWV/IREN down 3–4% (sourced, not checked against my table). Renewables are rallying (FSLR about +8%, reported, not checked). AMD beat (EPS $2.09 vs $1.95, revenue $13.4B vs $13.1B) and is up about 5–6%, yet SMH is lower. That means the AMD beat is not pulling the AI-infrastructure group up with it. Gold is +3.1% and USO −2.9%. **The regime is rotation out of AI-capex into cyclicals, defensives and small caps, which is the book's existing thesis.** I see the edge long in breadth (banks, homebuilders, staples) and short in AI infrastructure. Mega-cap platforms (AAPL, MSFT, AMZN, META, GOOGL) are being bought, and that hurts three of my shorts.

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:15 | 14:15 | ADP Oct payrolls | **86k actual vs 67k est** (Sep revised to 86k); job-changer pay growth fastest since Mar 2024. A mild hawkish lean, but TLT is still +0.3%, so the reaction is muted. | KRE, XHB, XLP |
| 09:45 | 15:45 | S&P Global services PMI (final) | est 57.9, prev 58.8 | all |
| 10:00 | 16:00 | ISM services Oct | prev 54.9 headline, prices 74.0. A hot prices index is a risk to XHB. | XHB, KRE |
| 10:30 | 16:30 | EIA crude inventories | — | none directly |
| Prior evening | — | AMD Q3 | beat; stock about +5–6% pre-market | SMH |

I did not verify which other companies report today. None of my holdings report inside the horizon as far as I know.

### 3. Open positions
- **AAPL short (0.25 tier).** Pre-market is 339.33, above the 338.80 stop. **Invalidated.** My stated invalidation was "closes back above 334", and it has rallied 2.2% with the mega-caps. The stop will trigger at the open anyway. I am closing it explicitly so it is not left to a gap fill. Loss is about −1.05R. **Close.**
- **GOOGL short.** 283.97 vs entry 279.61, stop 290.50. **Weakening.** It is back above the 280.36 break level I traded. The stop stays outside ordinary noise (290.5 is 0.6 ATR above). Hold. The review should close it if it trades above 288 at 10:05 with QQQ green.
- **META short.** 630 vs entry 616.20, stop 643. **Weakening.** The mega-cap bid is working against it. The stop is 0.57 ATR away; hold, no change.
- **ORCL short.** 122.25 (−3.1%) vs entry 122.52. **Intact and strengthening.** The data-center-moratorium story is exactly the debt-funded-capex risk in my thesis. I am tightening the stop from 130.40 to **129.00**: still more than 0.8 ATR above the 126.19 prior close, which a failed gap-down rally would have to reclaim first. Target 110.40 unchanged.
- **SMH short.** 510.48 vs entry 518.88. **Intact.** It is falling even with a strong AMD print, which is the tell. I am tightening the stop from 541 to **532.00**: above the 520.53 broken 20d low plus half an ATR, and above yesterday's 518.52 close. This cuts risk by about $207. Target 486.
- **KRE long.** 74.23 at a new 20d high (74.19). **Intact.** I am raising the stop from 71.25 to **72.00**, under the 72.88 prior close by more than half an ATR and 1.06 below entry. Target 76.20.
- **XHB long.** 104.40 vs entry 102.93. **Intact.** I am raising the stop from 100.90 to **101.80**, under the 102.86 breakout and 2.6 below last (about 1 ATR). Target 107.20.
- **XLP long.** 90.93 at its 20d high. **Intact.** I am raising the stop from 88.00 to **88.80**, under the prior close of 88.95 and 2.1 below last (1.4 ATR). Target 93.50.

No resting entries.

### 4. New plays
None. All 8 slots are taken and the harness allows 0 new plays. Closing AAPL frees a slot only after the open, so the review can use it (see §7).

### 5. Both sides
- **Best short: NVDA breakdown.** Sell stop at 200.40, under the 200.92 20d low; stop 208.50, which is above the 206.69 prior close; target 184.00 (about 2R); P = 0.36. It fits the data-center-policy story, but there is no slot, and it would stack a fifth AI-tech short on top of SMH, which overlaps it. **Passed.**
- **Best long: HD.** Breakout to 346 (+3.7%) above the 341.54 20d high. Limit 342.00 on a retest; stop 334.00, under the breakout by about 1 ATR; target 358.00 (2R); P = 0.40. No slot, and it duplicates XHB's housing exposure. HD reports mid-November; I did not verify the date, so I would check it before taking the trade. **Passed.**

### 6. Passing on
- **NVDA short** and **HD long**: as above, no slot.
- **TSLA short** (−5.3% to 377 on the Democratic sweep): the move has already happened, and the 3.8% ATR means a sensible stop gives poor R. No levels.
- **FSLR/RUN long** (renewables gap up): I could not verify the prices in my table. Excluded.
- **AMD long** after earnings: it gapped about 6% while the group is falling. I would be chasing a gap against the sector.

### 7. For the post-open review
- **The AAPL slot frees up.** If ORCL's opening range holds below 124 and NVDA is below 202 at 10:05, consider the NVDA short with the §5 levels at a 0.25–0.5 tier. Otherwise use the slot for nothing.
- **GOOGL:** above 288 at 10:05 with QQQ positive → close it (about −0.75R) instead of carrying it to the 290.50 stop.
- **ISM services at 10:00:** if the prices index is ≥76 and TLT turns red, close half the case for XHB by keeping its new 101.80 stop. If the 10-year breaks to a new high, close XHB outright.
- **META:** above 640 at 10:05 → close it.

### 8. Book state
Once AAPL closes and the stops are tightened: 7 of 8 slots. Risk at stake falls from 3.20% to roughly **2.0%** of equity (cap 4%). Gross is about **96%** (cap 150%) and net about **+21%** (cap ±100%).

Sources: [TipRanks](https://www.tipranks.com/news/stock-market-today-nov-4-futures-rise-after-democrats-sweep-midterm-elections), [Yahoo Finance live](https://finance.yahoo.com/markets/live/stock-market-today-dow-sp-500-nasdaq-midterm-elections-091834396.html), [Benzinga](https://www.benzinga.com/markets/equities/26/11/62854452/stock-market-today-dow-jones-sp-500-futures-rise-as-democrats-take-control-of-congress-amd-amgn-nvo-in-focus), [Investing.com premarket movers](https://www.investing.com/news/stock-market-news/premarket-movers-trump-media-ai-infrastructure-stocks-fall-amd-jumps-4998777), [Yahoo AI data center/renewables](https://finance.yahoo.com/energy/articles/ai-data-center-stocks-dip-113427491.html), [CNBC](https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html), [Benzinga Gerstner](https://www.benzinga.com/markets/equities/26/11/62856685/crwv-apld-iren-stocks-slip-as-brad-gerstner-warns-democratic-midterm-gains-could-put-10–15-gw-of-ai-dat), [Investing.com ADP](https://www.investing.com/news/economic-indicators/us-private-payrolls-rise-by-86000-in-october-adp-says-4999417), [Investing.com calendar](https://ph.investing.com/news/stock-market-news/adp-jobs-report-services-pmi-and-oil-inventories-among-data-due-wednesday-93CH-2671538), [Chartmill premarket](https://www.chartmill.com/news/FTK/Chartmill-57770-Premarket-Movers-Nov-4-2026-Gainers-and-Losers)

```json
{
  "date": "2026-11-04",
  "no_trade": true,
  "session_note": "Democratic midterm sweep: breadth rally plus AI data-center selloff, i.e. the book's rotation thesis. No slots free; closing the invalidated AAPL short and tightening stops. The review may use the freed slot for an NVDA breakdown short if ORCL/NVDA stay weak at 10:05.",
  "plays": [],
  "manage": [
    {"ticker": "AAPL", "action": "close", "reason": "Pre-market 339.33 is above the 338.80 stop and the 334 invalidation; mega-cap bid. Exit rather than leave it to a gap fill."},
    {"ticker": "ORCL", "action": "update", "stop": 129.00, "reason": "Data-center moratorium fears confirm the thesis; tighten stop to 129, still >0.8 ATR above the 126.19 prior close."},
    {"ticker": "SMH", "action": "update", "stop": 532.00, "reason": "Falling despite AMD beat; tighten stop to above the 520.53 broken 20d low plus 0.5 ATR, cutting risk."},
    {"ticker": "KRE", "action": "update", "stop": 72.00, "reason": "New 20d high; raise stop under the 72.88 prior close."},
    {"ticker": "XHB", "action": "update", "stop": 101.80, "reason": "Trail stop under the 102.86 breakout, about 1 ATR below last."},
    {"ticker": "XLP", "action": "update", "stop": 88.80, "reason": "At 20d high; raise stop under the 88.95 prior close, 1.4 ATR below last."}
  ],
  "passed": [
    {"ticker": "NVDA", "direction": "short", "entry_type": "stop", "entry": 200.40, "stop": 208.50, "targets": [184.00], "p_target_first": 0.36, "reason": "Best short: breakdown below the 200.92 20d low on data-center policy risk, but no slot and overlaps SMH."},
    {"ticker": "HD", "direction": "long", "entry_type": "limit", "entry": 342.00, "stop": 334.00, "targets": [358.00], "p_target_first": 0.40, "reason": "Best long: breakout above the 341.54 20d high; no slot, duplicates XHB, earnings date unverified."}
  ]
}
```

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Wednesday 2026-11-04. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,348.66**
- Cash: $79,087.95
- Session P&L so far: +0.93% (new entries are blocked at -3.0%)
- Gross exposure: $46,999 (46% of equity, cap 150%)
- Net exposure: $+23,261 (+23%, cap +/-100%)
- Risk at stake (entry to stop): $749 (0.73% of equity, cap 4.0%) — 3.27% left for new plays
- Slots: 3 open + 0 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 74.08 | +145 (+1.4%) | 72.00 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| SMH | short | 23 | 518.88 | 516.05 | +65 (+0.5%) | 532.00 | 486.00 | Semis are the most crowded AI-capex expression; a break of the 520.53 20d low converts the gap into a range breakdown be |
| XLP | long | 270 | 89.90 | 91.15 | +338 (+1.4%) | 88.80 | 93.50 | Money leaving AI-capex names is going to staples; a pullback to the 89.99 breakout level is a retest that buys the rotat |

### Record

40 closed trades: 13W / 27L, total -0.69R, net $+1,814 realized. Shorts taken: 33.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| GOOGL | short | stop | -1.00R | $-522 | 30% |
| ORCL | short | stop | -0.84R | $-418 | 36% |
| XHB | long | target | +2.18R | $+1,071 | 38% |
| META | short | stop | -0.59R | $-142 | 35% |
| AAPL | short | close | -1.75R | $-443 | 33% |

### Ideas you passed on, replayed against the tape

85 resolved: 25 reached target first, 37 stop first, 16 never reached the entry, 7 expired, 0 ambiguous. Average +0.06R across the 69 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-11-02 pre-market | XHB | long | dropped by the caps: would be 9 positions and resting entries, cap is 8 | target | +1.52R | 37% |
| 2026-11-03 open | CRM | short | Fresh break of the 220.29 20d low on -4% day; sell a retest. No slot left and it | stop | -1.29R | 35% |
| 2026-10-28 open | ENPH | short | Post-earnings -15%, already far below its 20d low; 5.8% ATR, and a break of toda | never filled | - | 33% |
| 2026-10-21 open | NFLX | short | Gap-down failed at the open; price back at the old 20d low 66.54, so the breakdo | expired | +0.01R | 30% |
| 2026-10-26 pre-market | AAPL | short | Best short (iPhone 18 Pro order cuts), but its own earnings are inside the horiz | target | +2.13R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| KRE | 74.07 (10:05 iex) | +1.6% | 72.88 | 74.62 / 74.03-75.67 | 1.36 (1.9%) | 67.79-74.19 | +2.8% / +1.6% | +0.4% | 15.2M |
| SMH | 516.03 (10:05 iex) | -0.5% | 518.52 | 511.17 / 505.77-522.20 | 21.11 (4.1%) | 506.44-625.89 | -7.1% / -9.2% | -7.1% | 9.8M |
| XLP | 91.16 (10:05 iex) | +2.5% | 88.95 | 90.62 / 90.27-91.28 | 1.51 (1.7%) | 81.69-90.99 | +2.4% / +5.2% | +2.1% | 16.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 767.98 (10:05 iex) | +1.8% | 754.35 | 763.03 / 762.64-768.22 | 8.52 (1.1%) | 750.36-779.42 | -1.8% / -1.6% | -2.0% | 39.4M |
| QQQ | 698.97 (10:05 iex) | +2.0% | 685.28 | 688.43 / 687.87-699.41 | 14.54 (2.1%) | 680.33-758.30 | -4.9% / -5.3% | -5.0% | 41.5M |
| IWM | 283.49 (10:05 iex) | +1.3% | 279.79 | 284.17 / 283.08-286.17 | 3.85 (1.4%) | 269.88-285.26 | +1.0% / -1.2% | -0.1% | 23.9M |
| DIA | 528.65 (10:05 iex) | +2.2% | 517.06 | 527.73 / 527.02-529.78 | 5.21 (1.0%) | 508.35-528.45 | -0.5% / -0.7% | -1.2% | 3.4M |
| TLT | 81.25 (10:05 iex) | +0.2% | 81.11 | 81.37 / 81.12-81.52 | 0.82 (1.0%) | 76.11-82.17 | +1.7% / +1.5% | -0.2% | 37.7M |
| GLD | 369.86 (10:05 iex) | +3.0% | 359.26 | 369.58 / 369.46-371.28 | 5.78 (1.6%) | 354.67-385.17 | -3.9% / -7.4% | -3.5% | 8.5M |
| USO | 153.78 (10:04 iex) | -2.8% | 158.17 | 153.22 / 152.38-153.78 | 5.46 (3.5%) | 142.47-171.82 | -0.5% / +4.7% | -3.5% | 4.9M |
| SMH | 516.03 (10:05 iex) | -0.5% | 518.52 | 511.17 / 505.77-522.20 | 21.11 (4.1%) | 506.44-625.89 | -7.1% / -9.2% | -7.1% | 9.8M |
| XLK | 179.49 (10:05 iex) | +1.7% | 176.51 | 176.34 / 176.12-179.98 | 4.96 (2.8%) | 173.91-201.56 | -6.2% / -6.8% | -6.8% | 9.9M |
| XLF | 58.16 (10:05 iex) | +1.7% | 57.19 | 58.46 / 57.98-58.52 | 0.75 (1.3%) | 53.41-57.70 | +2.7% / +2.4% | +2.3% | 33.7M |
| XLE | 64.40 (10:05 iex) | -3.4% | 66.68 | 65.92 / 64.13-65.95 | 1.57 (2.4%) | 63.04-70.15 | -1.1% / +2.7% | -2.2% | 32.7M |
| XLV | 186.49 (10:05 iex) | +1.3% | 184.02 | 187.71 / 186.37-188.06 | 3.11 (1.7%) | 165.19-187.99 | +3.7% / +6.8% | +2.7% | 9.9M |
| XLI | 168.62 (10:05 iex) | -1.6% | 171.32 | 170.83 / 168.11-170.98 | 2.80 (1.6%) | 162.97-172.40 | +1.9% / +0.7% | +2.0% | 8.0M |
| XLY | 121.72 (10:05 iex) | +3.7% | 117.33 | 119.78 / 119.61-121.79 | 1.95 (1.7%) | 110.58-119.20 | +2.8% / +3.7% | +1.6% | 7.6M |
| XLP | 91.16 (10:05 iex) | +2.5% | 88.95 | 90.62 / 90.27-91.28 | 1.51 (1.7%) | 81.69-90.99 | +2.4% / +5.2% | +2.1% | 16.3M |
| XLU | 42.91 (10:05 iex) | -1.2% | 43.42 | 43.36 / 42.83-43.38 | 0.59 (1.4%) | 40.63-43.80 | +2.8% / +4.2% | +1.3% | 26.5M |
| XLB | 53.30 (10:05 iex) | +1.4% | 52.59 | 53.37 / 53.24-53.69 | 0.77 (1.5%) | 48.70-54.03 | +3.0% / +3.3% | +1.6% | 10.8M |
| XLRE | 44.40 (10:05 iex) | +1.7% | 43.67 | 44.32 / 44.10-44.55 | 0.63 (1.4%) | 40.28-43.72 | +3.4% / +2.9% | +2.9% | 8.1M |
| XLC | 105.05 (10:05 iex) | +3.6% | 101.44 | 103.53 / 103.39-105.11 | 1.84 (1.8%) | 99.33-113.17 | -5.5% / -7.9% | -2.1% | 7.3M |
| KRE | 74.07 (10:05 iex) | +1.6% | 72.88 | 74.62 / 74.03-75.67 | 1.36 (1.9%) | 67.79-74.19 | +2.8% / +1.6% | +0.4% | 15.2M |
| XHB | 106.40 (10:04 iex) | +4.3% | 101.98 | 104.98 / 104.00-107.97 | 2.70 (2.6%) | 91.87-104.90 | +4.9% / +3.8% | +2.8% | 2.3M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 353.29 (10:05 iex) | +6.4% | 331.90 | 341.85 / 340.99-353.56 | 7.31 (2.2%) | 325.33-351.73 | -3.0% / -0.6% | -4.4% | 43.7M |
| MSFT | 554.27 (10:05 iex) | +6.4% | 520.99 | 543.70 / 542.30-557.18 | 13.01 (2.5%) | 504.96-551.15 | -1.6% / +1.3% | -1.9% | 22.6M |
| NVDA | 205.53 (10:05 iex) | -0.6% | 206.69 | 203.55 / 200.94-206.79 | 6.61 (3.2%) | 200.92-239.08 | -5.2% / -6.6% | -5.2% | 100.9M |
| AMZN | 271.01 (10:05 iex) | +8.1% | 250.69 | 264.97 / 263.85-271.44 | 8.35 (3.3%) | 229.36-265.34 | -1.2% / -1.2% | -1.0% | 42.9M |
| GOOGL | 294.06 (10:05 iex) | +5.0% | 280.03 | 283.53 / 283.40-294.50 | 10.31 (3.7%) | 276.92-359.40 | -14.4% / -16.7% | -12.6% | 35.2M |
| META | 632.66 (10:05 iex) | +1.9% | 621.03 | 641.00 / 629.00-643.09 | 22.82 (3.7%) | 606.41-771.27 | -8.5% / -7.6% | +0.1% | 23.5M |
| TSLA | 386.57 (10:05 iex) | -3.0% | 398.50 | 379.80 / 375.50-386.62 | 14.99 (3.8%) | 349.33-414.23 | +4.1% / +7.3% | -2.2% | 36.6M |
| AVGO | 331.84 (10:05 iex) | -0.1% | 332.13 | 326.86 / 326.03-334.12 | 12.95 (3.9%) | 319.30-376.97 | -2.7% / -5.4% | -3.0% | 21.5M |
| AMD | 497.30 (10:05 iex) | +2.8% | 483.90 | 485.25 / 476.50-514.61 | 32.42 (6.7%) | 466.07-648.48 | -12.6% / -11.8% | -13.6% | 22.0M |
| ORCL | 126.92 (10:05 iex) | +0.6% | 126.19 | 121.78 / 121.78-129.85 | 7.94 (6.3%) | 118.43-148.48 | -4.8% / -10.2% | -3.3% | 37.0M |
| NFLX | 66.11 (10:05 iex) | +4.2% | 63.42 | 64.55 / 64.02-66.34 | 2.09 (3.3%) | 61.39-73.07 | -5.4% / -11.9% | +1.4% | 45.1M |
| CRM | 231.81 (10:05 iex) | +4.3% | 222.20 | 229.00 / 228.00-231.96 | 9.44 (4.2%) | 214.67-252.42 | -6.3% / -7.2% | -7.8% | 7.1M |
| JPM | 345.12 (10:05 iex) | +2.1% | 337.98 | 346.00 / 342.21-348.17 | 6.07 (1.8%) | 325.07-345.75 | +0.7% / -1.1% | +0.7% | 7.0M |
| GS | 911.09 (10:05 iex) | +1.7% | 896.09 | 920.31 / 899.60-930.66 | 24.60 (2.7%) | 859.03-939.38 | +0.2% / -4.8% | -1.7% | 2.3M |
| BAC | 51.03 (10:05 iex) | +2.8% | 49.66 | 51.26 / 50.73-51.38 | 1.03 (2.1%) | 49.17-54.93 | -3.6% / -11.1% | -2.0% | 43.2M |
| XOM | 171.49 (10:05 iex) | -3.4% | 177.46 | 174.26 / 170.69-174.61 | 4.46 (2.5%) | 163.46-188.50 | +0.0% / +5.4% | -1.4% | 12.3M |
| CVX | 219.15 (10:05 iex) | -2.7% | 225.27 | 222.56 / 217.33-223.01 | 4.93 (2.2%) | 204.86-236.48 | +0.7% / +5.2% | -1.3% | 7.7M |
| LLY | 1,420.62 (10:05 iex) | +0.8% | 1,409.38 | 1,441.00 / 1,418.06-1,445.96 | 48.13 (3.4%) | 1,131.21-1,449.68 | +10.8% / +17.1% | +9.9% | 2.7M |
| UNH | 402.24 (10:05 iex) | -0.5% | 404.44 | 396.60 / 392.50-404.44 | 11.31 (2.8%) | 368.50-426.55 | +0.8% / +3.7% | -1.4% | 6.0M |
| JNJ | 269.64 (10:05 iex) | +1.3% | 266.17 | 272.41 / 269.32-273.12 | 6.85 (2.6%) | 245.17-282.01 | +1.5% / +0.3% | -1.0% | 7.6M |
| WMT | 128.48 (10:05 iex) | +2.9% | 124.86 | 127.02 / 125.84-128.83 | 2.71 (2.2%) | 107.40-127.94 | +5.8% / +12.4% | +4.6% | 20.3M |
| COST | 1,038.42 (10:05 iex) | +1.9% | 1,019.26 | 1,036.83 / 1,028.50-1,043.02 | 18.41 (1.8%) | 936.22-1,042.57 | +3.3% / +7.9% | +2.9% | 2.2M |
| HD | 345.33 (10:05 iex) | +3.5% | 333.66 | 346.01 / 343.79-351.55 | 8.43 (2.5%) | 282.84-341.54 | +6.9% / +8.3% | +4.8% | 4.7M |
| CAT | 593.75 (10:05 iex) | -4.8% | 623.94 | 609.45 / 590.81-609.45 | 29.22 (4.7%) | 609.89-843.99 | -13.2% / -19.4% | -12.5% | 3.4M |
| BA | 177.19 (10:04 iex) | +2.2% | 173.31 | 177.00 / 176.03-179.10 | 5.90 (3.4%) | 165.01-193.28 | -5.6% / -10.9% | +3.1% | 10.0M |
| DAL | 85.89 (10:04 iex) | +3.1% | 83.28 | 85.89 / 85.55-87.17 | 3.14 (3.8%) | 74.14-84.70 | +4.7% / +3.6% | +2.2% | 6.8M |
| UAL | 111.53 (10:05 iex) | +4.0% | 107.21 | 112.17 / 111.05-113.97 | 5.17 (4.8%) | 94.54-112.01 | +4.1% / -0.2% | +2.4% | 5.3M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-11-04 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| YOU | 61.40 (10:05 iex) | +28.6% | 47.76 | 51.40 / 50.80-61.41 | 1.46 (3.1%) | 41.45-48.65 | +6.1% / +10.9% | +4.9% | 1.3M |
| KD | 16.09 (10:05 iex) | +24.3% | 12.94 | 14.91 / 14.62-16.59 | 0.70 (5.4%) | 11.22-15.23 | -2.7% / +1.0% | -8.6% | 4.0M |
| ARRY | 5.72 (10:05 iex) | +23.3% | 4.64 | 5.13 / 5.12-5.96 | 0.28 (6.1%) | 3.09-4.69 | +31.1% / +16.5% | +36.9% | 7.9M |
| GDXU | 77.73 (10:02 iex) | +19.6% | 65.00 | 75.95 / 74.88-79.40 | 9.24 (14.2%) | 60.78-110.15 | -25.8% / -45.8% | -21.2% | 1.9M |
| AIOK | 11.74 (10:05 iex) | +17.5% | 9.99 | 11.99 / 11.22-12.95 | 6.03 (60.4%) | 3.90-31.09 | - / - | -25.6% | 6.8M |
| IREZ | 24.40 (10:04 iex) | +18.7% | 20.55 | 23.02 / 21.98-24.40 | 3.97 (19.3%) | 9.91-26.82 | +13.1% / +57.1% | +11.3% | 1.6M |
| NRIX | 15.42 (10:05 iex) | -40.3% | 25.82 | 17.22 / 15.38-17.28 | 1.20 (4.6%) | 21.23-27.99 | +3.8% / +3.5% | -3.3% | 2.9M |
| FIS | 30.25 (10:05 iex) | -22.4% | 38.99 | 30.60 / 29.92-32.40 | 1.40 (3.6%) | 33.38-40.79 | +7.1% / +6.0% | +9.5% | 6.1M |
| MOD | 99.21 (10:05 iex) | -20.9% | 125.45 | 115.50 / 96.88-116.47 | 9.28 (7.4%) | 121.25-189.67 | -16.4% / -23.4% | -8.1% | 1.6M |
| GDXD | 24.65 (10:03 iex) | -19.2% | 30.52 | 25.31 / 23.78-25.81 | 2.82 (9.3%) | 20.76-32.41 | +21.7% / +44.1% | +20.9% | 1.5M |
| UVIX | 33.69 (10:05 iex) | -18.0% | 41.09 | 36.20 / 33.83-36.31 | 4.52 (11.0%) | 32.32-47.25 | +11.1% / +8.8% | +8.6% | 3.0M |
