## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Friday 2026-11-20. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,722.78**
- Cash: $140,670.03
- Session P&L so far: +0.32% (new entries are blocked at -3.0%)
- Gross exposure: $36,947 (36% of equity, cap 150%)
- Net exposure: $-36,947 (-36%, cap +/-100%)
- Risk at stake (entry to stop): $1,082 (1.04% of equity, cap 4.0%) — 2.96% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 345.91 | 326.66 | +1,155 (+5.6%) | -19% | 355.50 | 330.00 |
| HD | short | 51 | 343.57 | 340.15 | +174 (+1.0%) | -17% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **GLD**, opened 2026-11-18 (session 3 of at most 10), submitted with stop 359 and target 333, P 36%. Thesis: Gold is trending down on rising real rates and the strongest dollar in 18 months (-4.6% in 5 days, below its 20d and 50d averages). A US-session break below the overnight low (GLD 350.50, under its 352.91 20-day low) confirms the move toward the $3,800 and then ~$3,650 area. The stop entry stays unfilled if Warsh or the minutes turn dovish. Invalidation: DXY back below 102.50 with market-implied December-hike odds below 70%.
- **HD**, opened 2026-11-17 (session 4 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Your record

51 closed trades: 16W / 35L, total +0.37R, net $+2,410 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 51 | 18 | 30 | +0.01R |
| The same trades, bracket left alone | 51 | | | +0.03R |
| Ideas you passed on, or the caps dropped | 111 | 40 | 61 | +0.05R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 44 | 48% |
| 35%-40% | 73 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 149 brackets reached target first. Your Brier score is 0.240; saying 39% every time scores 0.238. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| LOW | short | stop | -0.67R | $-343 | 37% |
| IWM | short | target | +1.67R | $+853 | 36% |
| AMZN | long | stop | -1.20R | $-303 | 36% |
| DAL | long | stop | -0.60R | $-154 | 37% |
| XLE | short | close | -1.02R | $-521 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| GLD | 327.09 (08:58 iex) | -2.4% | 335.18 | 7.37 (2.2%) | 335.05-380.18 | -7.6% / -11.0% | -5.6% | 9.7M |
| HD | 339.05 (08:49 sip) | +0.7% | 336.68 | 10.52 (3.1%) | 316.15-362.44 | -0.5% / +7.1% | -3.3% | 4.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 710.04 (08:49 sip) | -0.8% | 715.87 | 14.70 (2.1%) | 715.65-775.64 | -4.7% / -6.0% | -5.4% | 52.5M |
| QQQ | 636.34 (09:04 iex) | -1.3% | 645.04 | 19.73 (3.1%) | 644.34-726.14 | -5.6% / -9.5% | -6.3% | 52.2M |
| IWM | 263.25 (08:49 sip) | -0.4% | 264.22 | 5.91 (2.2%) | 263.74-286.17 | -4.7% / -5.3% | -5.1% | 24.5M |
| DIA | 489.22 (08:49 sip) | -0.2% | 490.24 | 9.23 (1.9%) | 490.18-536.00 | -5.2% / -5.1% | -6.1% | 3.9M |
| TLT | 80.91 (08:49 sip) | +0.7% | 80.35 | 0.73 (0.9%) | 79.11-82.42 | -0.7% / +0.8% | +0.8% | 35.1M |
| GLD | 327.09 (08:58 iex) | -2.4% | 335.18 | 7.37 (2.2%) | 335.05-380.18 | -7.6% / -11.0% | -5.6% | 9.7M |
| USO | 137.01 (08:49 sip) | -0.8% | 138.09 | 5.73 (4.1%) | 135.01-171.82 | -8.9% / -9.1% | -5.5% | 5.0M |
| SMH | 434.98 (08:49 sip) | -2.8% | 447.48 | 27.46 (6.1%) | 445.32-571.00 | -10.7% / -18.8% | -10.8% | 11.8M |
| XLK | 157.10 (08:49 sip) | -2.2% | 160.69 | 6.52 (4.1%) | 159.63-191.55 | -7.7% / -13.2% | -7.5% | 13.8M |
| XLF | 55.53 (08:49 sip) | -0.1% | 55.58 | 1.09 (2.0%) | 55.30-60.04 | -2.9% / -0.6% | -4.5% | 36.9M |
| XLE | 60.57 (08:49 sip) | -0.5% | 60.89 | 1.79 (2.9%) | 60.43-70.15 | -6.4% / -6.0% | -5.3% | 36.6M |
| XLV | 178.26 (08:49 sip) | +0.5% | 177.46 | 3.76 (2.1%) | 176.96-192.32 | -3.8% / +0.7% | -5.5% | 12.5M |
| XLI | 160.60 (08:49 sip) | -0.5% | 161.36 | 3.67 (2.3%) | 160.83-172.40 | -3.5% / -4.1% | -4.8% | 8.9M |
| XLY | 115.14 (08:30 sip) | -0.6% | 115.88 | 2.95 (2.5%) | 112.83-122.92 | -1.7% / +1.5% | -3.8% | 9.4M |
| XLP | 90.90 (08:49 sip) | +1.2% | 89.86 | 1.65 (1.8%) | 86.36-93.48 | -0.3% / +4.3% | -1.3% | 20.3M |
| XLU | 43.27 (08:49 sip) | +0.6% | 43.01 | 0.62 (1.4%) | 42.39-44.40 | -0.8% / +2.7% | -1.8% | 24.1M |
| XLB | 49.35 (08:45 sip) | -0.1% | 49.42 | 1.13 (2.3%) | 49.32-54.63 | -5.1% / -2.7% | -5.6% | 12.5M |
| XLRE | 43.10 (08:49 sip) | +0.5% | 42.88 | 0.69 (1.6%) | 41.78-45.34 | -1.9% / +0.8% | -3.3% | 7.8M |
| XLC | 102.40 (08:25 sip) | -0.4% | 102.76 | 2.39 (2.3%) | 99.33-109.26 | -1.8% / -5.6% | -4.5% | 8.1M |
| KRE | 69.29 (08:49 sip) | +0.0% | 69.26 | 1.59 (2.3%) | 68.66-75.80 | -4.3% / -3.0% | -4.5% | 14.8M |
| XHB | no trade today | - | 97.89 | 3.31 (3.4%) | 97.19-108.78 | -3.6% / -0.5% | -3.4% | 2.3M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 349.35 (09:00 iex) | +0.0% | 349.21 | 9.01 (2.6%) | 325.08-360.83 | +0.5% / +2.3% | -1.6% | 47.9M |
| MSFT | 487.96 (08:59 iex) | -2.1% | 498.30 | 18.77 (3.8%) | 495.55-558.07 | -4.9% / -4.0% | -4.5% | 28.6M |
| NVDA | 142.68 (09:02 iex) | -2.3% | 145.98 | 11.90 (8.2%) | 145.71-219.99 | -21.4% / -30.1% | -12.2% | 260.8M |
| AMZN | 252.67 (09:04 iex) | -1.8% | 257.37 | 11.20 (4.4%) | 229.36-275.34 | -0.0% / +0.8% | -3.8% | 50.6M |
| GOOGL | 271.23 (09:02 iex) | -0.5% | 272.66 | 10.66 (3.9%) | 272.36-326.40 | -6.7% / -15.8% | -8.7% | 43.5M |
| META | 579.34 (09:03 iex) | -2.8% | 596.22 | 22.04 (3.7%) | 583.80-648.45 | -4.2% / -12.1% | -4.4% | 21.2M |
| TSLA | 365.00 (09:05 iex) | -2.5% | 374.41 | 18.40 (4.9%) | 338.15-414.23 | -3.0% / -0.4% | -5.8% | 36.4M |
| AVGO | 341.04 (09:05 iex) | -1.6% | 346.65 | 20.87 (6.0%) | 289.77-369.82 | +4.0% / +0.8% | -4.9% | 28.2M |
| AMD | 465.71 (09:04 iex) | -4.8% | 489.19 | 50.89 (10.4%) | 402.10-594.00 | -4.8% / -11.8% | -16.4% | 39.6M |
| ORCL | 106.67 (08:49 sip) | -3.5% | 110.57 | 8.20 (7.4%) | 109.21-148.48 | -10.7% / -16.8% | -13.0% | 40.7M |
| NFLX | 58.46 (08:49 sip) | +0.0% | 58.46 | 1.91 (3.3%) | 58.18-67.82 | -6.8% / -13.8% | -6.7% | 39.6M |
| CRM | 182.75 (08:49 sip) | -0.3% | 183.31 | 8.91 (4.9%) | 182.51-250.99 | -17.0% / -20.6% | -15.7% | 7.2M |
| JPM | 318.49 (08:49 sip) | -0.5% | 320.22 | 8.55 (2.7%) | 317.43-359.80 | -5.2% / -5.2% | -6.6% | 6.6M |
| GS | 837.99 (08:49 sip) | -1.1% | 847.53 | 30.36 (3.6%) | 843.88-939.38 | -5.6% / -6.8% | -7.2% | 2.1M |
| BAC | 48.40 (08:49 sip) | -0.4% | 48.57 | 1.21 (2.5%) | 48.05-53.02 | -3.3% / -8.4% | -3.8% | 34.3M |
| XOM | 158.18 (08:49 sip) | -0.5% | 158.93 | 4.74 (3.0%) | 158.60-187.32 | -7.3% / -5.7% | -5.8% | 14.7M |
| CVX | 205.60 (08:49 sip) | -0.4% | 206.50 | 5.40 (2.6%) | 204.31-234.53 | -5.5% / -3.4% | -3.8% | 8.4M |
| LLY | 1,354.98 (08:49 sip) | +0.3% | 1,351.12 | 43.97 (3.3%) | 1,256.10-1,475.25 | -2.0% / +7.2% | -5.2% | 3.1M |
| UNH | 337.30 (08:49 sip) | +2.1% | 330.48 | 15.94 (4.8%) | 324.67-425.25 | -17.1% / -15.1% | -18.4% | 6.4M |
| JNJ | 268.75 (08:49 sip) | +0.6% | 267.14 | 7.01 (2.6%) | 262.40-290.25 | -2.7% / -0.1% | -5.8% | 7.6M |
| WMT | 127.90 (08:49 sip) | +1.5% | 126.04 | 3.14 (2.5%) | 118.11-131.82 | +0.9% / +8.4% | -0.1% | 22.5M |
| COST | 1,108.20 (08:49 sip) | +1.3% | 1,093.83 | 20.97 (1.9%) | 978.87-1,123.67 | +4.0% / +11.4% | +0.1% | 2.5M |
| HD | 339.05 (08:49 sip) | +0.7% | 336.68 | 10.52 (3.1%) | 316.15-362.44 | -0.5% / +7.1% | -3.3% | 4.8M |
| CAT | 522.11 (08:49 sip) | -2.8% | 537.37 | 27.99 (5.2%) | 535.53-732.73 | -12.2% / -25.3% | -11.2% | 4.0M |
| BA | 159.50 (08:49 sip) | -0.6% | 160.51 | 4.87 (3.0%) | 158.92-189.66 | -6.8% / -13.3% | -6.4% | 10.6M |
| DAL | 82.75 (08:45 sip) | -0.5% | 83.17 | 3.18 (3.8%) | 75.33-92.52 | -1.9% / +1.1% | -3.9% | 6.0M |
| UAL | 104.80 (08:49 sip) | -0.7% | 105.53 | 5.45 (5.2%) | 96.39-122.08 | -3.3% / -2.3% | -5.1% | 5.2M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| HUM | 389.74 (08:49 sip) | +2.6% | 380.00 | 23.27 (6.1%) | 373.17-462.87 | -10.1% / -7.2% | -14.4% | 1.7M |
| KDP | 35.07 (08:49 sip) | +1.9% | 34.41 | 1.49 (4.3%) | 34.09-38.28 | -4.0% / +2.7% | -2.9% | 23.6M |
| HCA | 469.14 (07:45 sip) | +1.9% | 460.33 | 17.58 (3.8%) | 439.83-521.48 | -5.2% / +0.4% | -8.1% | 1.5M |
| CL | 98.66 (08:49 sip) | +1.8% | 96.88 | 2.22 (2.3%) | 90.47-101.81 | +0.2% / +5.8% | -1.0% | 5.5M |
| GIS | 35.11 (08:49 sip) | +1.8% | 34.48 | 1.16 (3.4%) | 32.82-37.02 | +0.0% / +2.1% | +2.9% | 8.1M |
| ADP | 306.57 (08:49 sip) | +1.8% | 301.19 | 6.62 (2.2%) | 282.73-316.14 | -0.1% / +5.9% | -2.2% | 2.4M |
| AMGN | 444.00 (08:49 sip) | +1.8% | 436.30 | 11.96 (2.7%) | 432.75-481.21 | -4.3% / +2.2% | -6.0% | 2.6M |
| TTWO | 212.22 (08:49 sip) | +1.7% | 208.65 | 13.52 (6.5%) | 183.86-237.41 | +0.0% / +0.5% | -8.1% | 4.6M |
| INTU | 279.65 (08:49 sip) | -9.8% | 310.02 | 13.79 (4.4%) | 302.59-366.47 | -8.2% / -2.3% | -8.9% | 2.8M |
| ROST | 206.00 (08:45 sip) | -6.3% | 219.88 | 8.71 (4.0%) | 218.43-249.30 | -5.1% / -4.9% | -7.3% | 2.3M |
| SNDK | 88.51 (09:04 iex) | -6.2% | 94.40 | 12.90 (13.7%) | 93.67-176.06 | -25.4% / -44.7% | -19.4% | 105.4M |
| TSM | 332.88 (08:54 iex) | -5.5% | 352.09 | 20.54 (5.8%) | 351.14-440.88 | -11.3% / -17.0% | -13.2% | 15.6M |
| ARM | 167.66 (09:02 iex) | -5.4% | 177.17 | 15.65 (8.8%) | 163.13-237.88 | -10.1% / -26.8% | -11.3% | 5.9M |
| DELL | 295.91 (08:49 sip) | -5.3% | 312.54 | 34.32 (11.0%) | 305.80-507.38 | -18.6% / -34.4% | -15.8% | 7.5M |
| WDC | 282.33 (09:03 iex) | -4.9% | 296.78 | 26.87 (9.1%) | 258.61-402.23 | -7.7% / -21.3% | -4.6% | 8.2M |
| MRVL | 131.96 (08:49 sip) | -4.7% | 138.47 | 15.72 (11.4%) | 132.54-253.66 | -21.5% / -37.8% | -15.8% | 31.5M |
