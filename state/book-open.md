## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Wednesday 2026-11-11. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,166.71**
- Cash: $133,070.63
- Session P&L so far: -0.30% (new entries are blocked at -3.0%)
- Gross exposure: $80,712 (79% of equity, cap 150%)
- Net exposure: $-55,442 (-54%, cap +/-100%)
- Risk at stake (entry to stop): $2,323 (2.27% of equity, cap 4.0%) — 1.73% left for new plays
- Slots: 3 open + 3 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 46% of equity in notional: at 1% risk its stop must be at least 2.2% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 269.13 | -119 (-1.8%) | +6% | 263.50 | 293.00 |
| IWM | short | 85 | 281.03 | 281.84 | -69 (-0.3%) | -23% | 287.00 | 271.00 |
| XLE | short | 213 | 60.56 | 62.93 | -506 (-3.9%) | -13% | 63.10 | 57.30 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **AMZN**, opened 2026-11-09 (session 3 of at most 10), submitted with stop 263.5 and target 293, P 36%. Thesis: Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong relative signal. Invalidation: QQQ breaking its 20-day low while AMZN falls back inside the range.
- **IWM**, opened 2026-11-10 (session 2 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.
- **XLE**, opened 2026-11-10 (session 2 of at most 10), submitted with stop 63.1 and target 57.3, P 37%. Thesis: Energy is breaking down as the Iran risk premium unwinds; a break of the 60.85 20d low continues the trend toward 57. Invalidation: Brent back above $93 or a renewed Iran escalation headline.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GLD | short | 32 | 374.00 | limit | 382.00 | 358.00 | 2026-11-10 |
| DAL | long | 69 | 89.50 | limit | 85.80 | 96.50 | 2026-11-09 |
| QQQ | short | 29 | 646.50 | stop | 664.00 | 615.00 | 2026-11-09 |

### Your record

46 closed trades: 15W / 31L, total +2.19R, net $+2,879 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 46 | 17 | 26 | +0.05R |
| The same trades, bracket left alone | 45 | | | +0.07R |
| Ideas you passed on, or the caps dropped | 89 | 31 | 49 | +0.03R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 33 | 45% |
| 35%-40% | 58 | 31% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 123 brackets reached target first. Your Brier score is 0.239; saying 39% every time scores 0.238. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| AVGO | short | close | -0.92R | $-232 | 37% |
| NVDA | short | target | +2.16R | $+1,108 | 37% |
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |
| KRE | long | stop | -0.04R | $-10 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AMZN | 269.08 (10:05 iex) | -0.7% | 270.87 | 273.31 / 268.14-274.87 | 10.68 (3.9%) | 229.36-275.34 | +6.1% / +6.6% | +8.0% | 50.4M |
| IWM | 281.84 (10:05 iex) | +0.4% | 280.58 | 282.99 / 281.48-283.09 | 5.21 (1.9%) | 269.88-286.17 | +1.2% / -0.3% | +0.3% | 25.7M |
| XLE | 62.92 (10:05 iex) | +1.1% | 62.21 | 62.85 / 62.34-63.02 | 1.88 (3.0%) | 60.43-70.15 | -6.7% / -4.2% | -6.7% | 37.6M |
| GLD | 367.80 (10:05 iex) | -0.4% | 369.36 | 369.36 / 367.50-369.38 | 7.57 (2.0%) | 354.67-384.88 | -0.7% / -3.7% | +2.8% | 9.2M |
| DAL | 91.62 (10:04 iex) | -0.6% | 92.20 | 91.82 / 91.06-92.05 | 3.48 (3.8%) | 74.14-92.52 | +13.1% / +13.6% | +10.7% | 6.6M |
| QQQ | 686.28 (10:05 iex) | +1.7% | 674.76 | 687.28 / 683.60-689.02 | 17.87 (2.6%) | 647.05-740.53 | -3.7% / -6.2% | -1.5% | 51.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 756.31 (10:05 iex) | +0.9% | 749.92 | 756.80 / 754.90-757.95 | 12.11 (1.6%) | 732.71-776.35 | -1.4% / -1.9% | -0.6% | 49.4M |
| QQQ | 686.28 (10:05 iex) | +1.7% | 674.76 | 687.28 / 683.60-689.02 | 17.87 (2.6%) | 647.05-740.53 | -3.7% / -6.2% | -1.5% | 51.9M |
| IWM | 281.84 (10:05 iex) | +0.4% | 280.58 | 282.99 / 281.48-283.09 | 5.21 (1.9%) | 269.88-286.17 | +1.2% / -0.3% | +0.3% | 25.7M |
| DIA | 521.10 (10:05 iex) | -0.1% | 521.73 | 522.79 / 520.77-523.16 | 7.74 (1.5%) | 508.66-536.60 | +0.1% / +0.4% | +0.9% | 3.9M |
| TLT | 80.70 (10:05 iex) | -0.2% | 80.88 | 80.75 / 80.61-80.76 | 0.80 (1.0%) | 77.41-82.42 | +0.1% / +1.2% | -0.3% | 39.6M |
| GLD | 367.80 (10:05 iex) | -0.4% | 369.36 | 369.36 / 367.50-369.38 | 7.57 (2.0%) | 354.67-384.88 | -0.7% / -3.7% | +2.8% | 9.2M |
| USO | 143.01 (10:04 iex) | +1.1% | 141.45 | 142.66 / 142.47-143.37 | 6.05 (4.3%) | 138.47-171.82 | -10.5% / -7.3% | -10.6% | 5.5M |
| SMH | 501.92 (10:05 iex) | +3.8% | 483.63 | 504.99 / 496.01-505.50 | 25.77 (5.3%) | 445.59-580.08 | -8.1% / -14.1% | -6.7% | 12.1M |
| XLK | 173.66 (10:05 iex) | +2.8% | 168.91 | 173.80 / 172.50-174.30 | 5.82 (3.4%) | 162.14-194.66 | -6.6% / -10.0% | -4.3% | 12.8M |
| XLF | 58.23 (10:05 iex) | -0.1% | 58.29 | 58.09 / 58.02-58.33 | 1.02 (1.7%) | 54.02-60.04 | +3.1% / +4.3% | +1.9% | 35.7M |
| XLE | 62.92 (10:05 iex) | +1.1% | 62.21 | 62.85 / 62.34-63.02 | 1.88 (3.0%) | 60.43-70.15 | -6.7% / -4.2% | -6.7% | 37.6M |
| XLV | 187.00 (10:05 iex) | -1.0% | 188.88 | 187.42 / 186.98-188.10 | 3.79 (2.0%) | 170.65-192.32 | +3.9% / +8.6% | +2.6% | 11.6M |
| XLI | 169.85 (10:05 iex) | +0.7% | 168.73 | 169.99 / 169.17-170.40 | 3.50 (2.1%) | 161.74-172.40 | +0.7% / -0.2% | -1.5% | 9.1M |
| XLY | 120.69 (10:05 iex) | -0.3% | 121.05 | 121.14 / 120.70-121.47 | 2.63 (2.2%) | 110.67-122.92 | +4.2% / +6.7% | +3.2% | 9.4M |
| XLP | 90.36 (10:05 iex) | -0.7% | 91.03 | 90.45 / 90.34-90.98 | 1.81 (2.0%) | 84.61-93.40 | +2.6% / +6.9% | +2.3% | 19.6M |
| XLU | 43.69 (10:05 iex) | -0.1% | 43.73 | 43.68 / 43.57-43.78 | 0.65 (1.5%) | 41.24-44.09 | +2.2% / +4.8% | +0.7% | 27.8M |
| XLB | 52.83 (10:05 iex) | -0.0% | 52.85 | 52.87 / 52.61-52.97 | 1.03 (2.0%) | 49.23-54.63 | +1.8% / +3.9% | +0.5% | 12.5M |
| XLRE | 44.45 (10:05 iex) | -0.3% | 44.58 | 44.41 / 44.38-44.63 | 0.75 (1.7%) | 41.31-45.34 | +3.6% / +5.0% | +2.1% | 8.5M |
| XLC | 108.03 (10:05 iex) | +0.2% | 107.76 | 108.03 / 107.90-108.45 | 2.28 (2.1%) | 99.33-112.90 | +1.7% / -1.6% | +6.2% | 8.1M |
| KRE | 72.89 (10:05 iex) | -0.3% | 73.09 | 73.02 / 72.60-73.10 | 1.67 (2.3%) | 67.79-75.80 | +1.7% / +2.0% | +0.3% | 15.3M |
| XHB | 102.26 (10:05 iex) | -0.9% | 103.17 | 103.19 / 102.28-103.23 | 3.42 (3.3%) | 91.87-108.78 | +3.5% / +4.9% | +1.2% | 2.5M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 353.42 (10:05 iex) | +1.4% | 348.51 | 349.49 / 349.32-354.44 | 9.49 (2.7%) | 325.33-355.38 | +1.2% / +3.3% | +5.0% | 49.5M |
| MSFT | 527.49 (10:05 iex) | -1.1% | 533.16 | 534.37 / 526.62-534.76 | 17.29 (3.2%) | 504.96-559.15 | +0.4% / +3.0% | +2.3% | 26.3M |
| NVDA | 173.25 (10:05 iex) | +2.6% | 168.89 | 172.77 / 170.77-175.13 | 9.29 (5.5%) | 165.89-226.00 | -18.1% / -22.5% | -18.3% | 155.3M |
| AMZN | 269.08 (10:05 iex) | -0.7% | 270.87 | 273.31 / 268.14-274.87 | 10.68 (3.9%) | 229.36-275.34 | +6.1% / +6.6% | +8.0% | 50.4M |
| GOOGL | 290.53 (10:05 iex) | +1.1% | 287.38 | 290.11 / 289.50-291.84 | 11.41 (4.0%) | 276.92-359.40 | -7.6% / -13.1% | +2.6% | 40.3M |
| META | 638.90 (10:05 iex) | -0.4% | 641.39 | 647.24 / 637.52-648.45 | 23.90 (3.7%) | 583.80-761.50 | -1.6% / -5.3% | +3.3% | 24.4M |
| TSLA | 389.72 (10:05 iex) | +2.6% | 379.78 | 386.75 / 386.35-392.67 | 18.31 (4.8%) | 338.15-414.23 | -0.2% / +1.8% | -4.7% | 41.2M |
| AVGO | 352.66 (10:05 iex) | +6.2% | 331.98 | 349.86 / 348.10-354.50 | 17.29 (5.2%) | 289.77-354.25 | +0.9% / -4.0% | -0.0% | 25.5M |
| AMD | 538.08 (10:05 iex) | +4.4% | 515.21 | 543.07 / 522.65-543.40 | 42.65 (8.3%) | 402.10-591.88 | -0.6% / -6.1% | +6.5% | 30.9M |
| ORCL | 125.79 (10:05 iex) | +6.6% | 117.98 | 124.28 / 124.15-126.88 | 8.71 (7.4%) | 109.21-148.48 | -7.3% / -14.2% | -6.5% | 43.8M |
| NFLX | 63.22 (10:05 iex) | -0.1% | 63.26 | 62.84 / 62.75-63.75 | 1.88 (3.0%) | 61.39-73.07 | -3.5% / -10.0% | -0.3% | 47.1M |
| CRM | 214.79 (10:05 iex) | +0.6% | 213.48 | 214.91 / 213.50-215.85 | 9.09 (4.3%) | 208.88-252.42 | -8.8% / -10.2% | -3.9% | 7.2M |
| JPM | 343.04 (10:05 iex) | +0.3% | 342.07 | 342.89 / 340.82-343.84 | 7.95 (2.3%) | 326.40-359.80 | +1.2% / +0.5% | +1.2% | 7.2M |
| GS | 922.81 (10:05 iex) | +1.4% | 910.19 | 927.50 / 912.59-928.38 | 29.62 (3.3%) | 854.45-939.38 | +1.6% / -1.9% | +1.6% | 2.2M |
| BAC | 50.73 (10:05 iex) | +0.1% | 50.68 | 50.87 / 50.33-50.87 | 1.24 (2.5%) | 49.17-53.02 | +0.1% / -7.5% | +2.1% | 43.7M |
| XOM | 165.97 (10:05 iex) | +0.9% | 164.47 | 165.14 / 164.46-166.10 | 5.16 (3.1%) | 160.11-188.50 | -6.8% / -2.7% | -7.3% | 14.2M |
| CVX | 212.39 (10:05 iex) | +0.6% | 211.22 | 212.31 / 210.88-212.41 | 5.72 (2.7%) | 206.01-236.48 | -5.6% / -1.8% | -6.2% | 8.4M |
| LLY | 1,419.19 (10:05 iex) | -0.9% | 1,432.29 | 1,418.08 / 1,414.37-1,427.75 | 53.57 (3.7%) | 1,174.24-1,453.00 | +8.0% / +17.0% | +1.6% | 3.2M |
| UNH | 398.53 (10:05 iex) | -1.6% | 405.12 | 404.39 / 396.95-404.74 | 11.42 (2.8%) | 382.29-426.55 | -0.5% / +3.7% | +0.2% | 5.7M |
| JNJ | 277.13 (10:05 iex) | -1.3% | 280.78 | 277.96 / 276.67-278.66 | 7.77 (2.8%) | 248.50-283.25 | +5.1% / +5.4% | +5.5% | 7.7M |
| WMT | 124.52 (10:05 iex) | -0.8% | 125.55 | 124.33 / 124.30-126.07 | 3.19 (2.5%) | 113.38-131.82 | +3.0% / +10.8% | +0.6% | 23.0M |
| COST | 1,073.19 (10:05 iex) | +0.7% | 1,066.14 | 1,080.51 / 1,072.57-1,091.92 | 21.46 (2.0%) | 958.58-1,081.55 | +5.1% / +11.5% | +4.6% | 2.5M |
| HD | 346.66 (10:05 iex) | -1.2% | 351.00 | 348.43 / 344.31-348.43 | 10.50 (3.0%) | 289.57-362.44 | +7.3% / +13.1% | +5.2% | 4.8M |
| CAT | 594.87 (10:05 iex) | +1.8% | 584.57 | 600.70 / 588.50-601.28 | 32.66 (5.6%) | 550.81-768.52 | -12.1% / -22.1% | -6.3% | 4.0M |
| BA | 174.08 (10:04 iex) | +0.4% | 173.38 | 172.81 / 172.18-174.27 | 6.67 (3.8%) | 165.01-193.28 | -3.6% / -9.2% | +0.0% | 10.6M |
| DAL | 91.62 (10:04 iex) | -0.6% | 92.20 | 91.82 / 91.06-92.05 | 3.48 (3.8%) | 74.14-92.52 | +13.1% / +13.6% | +10.7% | 6.6M |
| UAL | 118.51 (10:05 iex) | -1.7% | 120.56 | 119.38 / 118.35-119.79 | 5.59 (4.6%) | 94.54-122.08 | +14.5% / +11.9% | +12.5% | 5.6M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SNDK | 969.93 (10:05 iex) | +12.8% | 859.99 | 928.04 / 920.11-970.40 | 107.74 (12.5%) | 803.97-1,461.80 | -27.7% / -41.8% | -23.7% | 11.4M |
| DELL | 367.67 (10:05 iex) | +10.0% | 334.38 | 360.40 / 358.52-368.35 | 33.23 (9.9%) | 315.00-547.63 | -22.3% / -33.1% | -18.1% | 7.7M |
| MU | 795.99 (10:05 iex) | +9.8% | 725.11 | 777.00 / 763.05-794.84 | 60.62 (8.4%) | 650.00-990.00 | -15.2% / -23.9% | -15.2% | 31.0M |
| STX | 547.16 (10:05 iex) | +9.1% | 501.62 | 546.24 / 533.14-547.70 | 54.27 (10.8%) | 449.28-751.81 | -19.1% / -33.7% | -17.3% | 6.1M |
| MRVL | 166.53 (10:05 iex) | +7.9% | 154.39 | 167.04 / 162.50-168.22 | 18.53 (12.0%) | 132.54-264.30 | -25.0% / -33.4% | -10.2% | 29.8M |
| INTC | 62.22 (10:05 iex) | +7.0% | 58.13 | 61.77 / 60.95-62.50 | 6.47 (11.1%) | 51.51-101.34 | -26.2% / -39.9% | -4.0% | 148.4M |
| SMCI | 29.74 (10:05 iex) | +7.0% | 27.79 | 29.62 / 29.12-29.80 | 2.35 (8.5%) | 25.81-38.02 | -13.7% / -25.1% | -11.5% | 43.7M |
| WDC | 308.83 (10:05 iex) | +6.8% | 289.20 | 309.04 / 301.71-310.97 | 28.27 (9.8%) | 258.61-402.23 | -15.7% / -27.7% | -16.7% | 9.3M |
| ABNB | 181.05 (10:05 iex) | -3.1% | 186.90 | 182.71 / 178.80-183.73 | 7.09 (3.8%) | 163.82-197.87 | +7.5% / +10.5% | +11.9% | 4.6M |
| SE | 74.47 (10:05 iex) | -3.0% | 76.80 | 77.00 / 74.31-77.10 | 3.76 (4.9%) | 71.53-100.00 | -3.8% / -17.7% | +0.0% | 8.9M |
| KMB | 107.60 (10:05 iex) | -2.9% | 110.76 | 109.02 / 107.67-109.18 | 3.78 (3.4%) | 97.84-112.91 | +2.6% / +7.9% | +6.0% | 7.2M |
| CI | 294.93 (10:05 iex) | -2.7% | 303.13 | 300.73 / 295.50-302.22 | 8.73 (2.9%) | 283.56-318.05 | +0.9% / +5.8% | +2.6% | 1.7M |
| GIS | 33.67 (10:05 iex) | -2.7% | 34.60 | 34.09 / 33.69-34.21 | 1.23 (3.6%) | 31.68-37.02 | +1.7% / +1.0% | +1.5% | 8.9M |
| ACN | 251.81 (10:05 iex) | -2.6% | 258.51 | 254.88 / 251.81-255.95 | 11.95 (4.6%) | 212.71-271.76 | +4.6% / +21.7% | +1.6% | 6.3M |
| SYK | 316.39 (10:05 iex) | -2.4% | 324.29 | 319.23 / 316.85-320.70 | 12.60 (3.9%) | 278.57-349.48 | +5.2% / +11.1% | +4.4% | 3.2M |
| BMY | 61.34 (10:05 iex) | -2.3% | 62.80 | 62.00 / 61.44-62.11 | 1.70 (2.7%) | 56.58-65.54 | +1.9% / +1.5% | +1.8% | 10.9M |
