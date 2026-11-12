## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Thursday 2026-11-12. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,441.93**
- Cash: $119,651.62
- Session P&L so far: +0.46% (new entries are blocked at -3.0%)
- Gross exposure: $67,196 (66% of equity, cap 150%)
- Net exposure: $-41,751 (-41%, cap +/-100%)
- Risk at stake (entry to stop): $1,781 (1.74% of equity, cap 4.0%) — 2.26% left for new plays
- Slots: 2 open + 3 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 272.79 | -31 (-0.5%) | +6% | 263.50 | 293.00 |
| IWM | short | 85 | 281.03 | 279.49 | +131 (+0.5%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **AMZN**, opened 2026-11-09 (session 4 of at most 10), submitted with stop 263.5 and target 293, P 36%. Thesis: Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong relative signal. Invalidation: QQQ breaking its 20-day low while AMZN falls back inside the range.
- **IWM**, opened 2026-11-10 (session 3 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GLD | short | 32 | 374.00 | limit | 382.00 | 358.00 | 2026-11-10 |
| DAL | long | 69 | 89.50 | limit | 85.80 | 96.50 | 2026-11-09 |
| QQQ | short | 29 | 646.50 | stop | 664.00 | 615.00 | 2026-11-09 |

### Your record

47 closed trades: 15W / 32L, total +1.17R, net $+2,358 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 47 | 17 | 27 | +0.02R |
| The same trades, bracket left alone | 46 | | | +0.04R |
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
| AMZN | 272.78 (10:05 iex) | +2.5% | 266.17 | 268.09 / 267.62-273.58 | 10.31 (3.9%) | 229.36-275.34 | +4.0% / +4.6% | +0.1% | 50.6M |
| IWM | 279.61 (10:05 iex) | -1.2% | 283.09 | 281.43 / 279.08-282.20 | 5.23 (1.8%) | 269.88-286.17 | +1.9% / +0.6% | -0.3% | 24.7M |
| GLD | 354.51 (10:05 iex) | -2.9% | 365.17 | 357.63 / 354.17-357.76 | 7.13 (2.0%) | 354.67-384.88 | -1.7% / -4.6% | -2.0% | 8.9M |
| DAL | 89.72 (10:04 iex) | -1.8% | 91.32 | 90.68 / 89.60-91.04 | 3.27 (3.6%) | 74.14-92.52 | +11.0% / +12.1% | +2.3% | 6.6M |
| QQQ | 685.77 (10:05 iex) | -0.7% | 690.38 | 680.29 / 679.83-688.40 | 17.69 (2.6%) | 647.05-729.43 | -1.2% / -4.0% | -0.2% | 51.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 756.93 (10:05 iex) | -0.4% | 759.81 | 753.99 / 753.67-758.84 | 12.15 (1.6%) | 732.71-775.64 | -0.1% / -0.6% | -0.9% | 48.6M |
| QQQ | 685.77 (10:05 iex) | -0.7% | 690.38 | 680.29 / 679.83-688.40 | 17.69 (2.6%) | 647.05-729.43 | -1.2% / -4.0% | -0.2% | 51.5M |
| IWM | 279.61 (10:05 iex) | -1.2% | 283.09 | 281.43 / 279.08-282.20 | 5.23 (1.8%) | 269.88-286.17 | +1.9% / +0.6% | -0.3% | 24.7M |
| DIA | 523.19 (10:04 iex) | -0.2% | 524.44 | 524.38 / 523.19-525.82 | 7.77 (1.5%) | 508.66-536.60 | +0.5% / +1.0% | -1.6% | 3.9M |
| TLT | 80.31 (10:05 iex) | -0.8% | 80.92 | 80.75 / 80.27-80.81 | 0.71 (0.9%) | 79.01-82.42 | -0.0% / +1.3% | -1.0% | 38.3M |
| GLD | 354.51 (10:05 iex) | -2.9% | 365.17 | 357.63 / 354.17-357.76 | 7.13 (2.0%) | 354.67-384.88 | -1.7% / -4.6% | -2.0% | 8.9M |
| USO | 142.43 (10:04 iex) | +0.7% | 141.47 | 141.99 / 141.49-142.43 | 6.06 (4.3%) | 138.47-171.82 | -10.1% / -7.3% | -2.7% | 5.5M |
| SMH | 495.26 (10:05 iex) | -2.3% | 506.96 | 485.01 / 484.50-500.57 | 25.55 (5.0%) | 445.59-571.00 | -3.2% / -9.8% | +0.5% | 12.3M |
| XLK | 172.17 (10:05 iex) | -1.3% | 174.36 | 169.85 / 169.35-172.89 | 5.86 (3.4%) | 162.14-191.55 | -3.2% / -7.0% | -1.2% | 13.0M |
| XLF | 58.59 (10:05 iex) | -0.1% | 58.63 | 58.87 / 58.52-59.08 | 1.00 (1.7%) | 54.59-60.04 | +3.3% / +4.9% | -1.0% | 34.7M |
| XLE | 63.73 (10:05 iex) | +0.6% | 63.37 | 63.88 / 63.42-63.88 | 1.79 (2.8%) | 60.43-70.15 | -4.6% / -2.4% | -0.2% | 37.6M |
| XLV | 188.90 (10:05 iex) | -0.0% | 188.95 | 190.17 / 188.35-190.66 | 3.73 (2.0%) | 175.27-192.32 | +3.5% / +8.4% | -0.4% | 11.4M |
| XLI | 169.97 (10:04 iex) | -0.6% | 170.97 | 170.46 / 169.68-171.06 | 3.44 (2.0%) | 161.74-172.40 | +2.0% / +1.1% | +0.9% | 8.9M |
| XLY | 121.72 (10:05 iex) | +0.6% | 120.99 | 121.00 / 121.00-122.19 | 2.60 (2.1%) | 111.70-122.92 | +3.8% / +6.5% | -1.1% | 9.4M |
| XLP | 91.44 (10:05 iex) | -0.0% | 91.45 | 92.04 / 91.20-92.15 | 1.69 (1.9%) | 86.36-93.40 | +2.7% / +7.3% | -0.5% | 19.7M |
| XLU | 43.89 (10:05 iex) | +0.2% | 43.82 | 44.03 / 43.86-44.09 | 0.61 (1.4%) | 41.28-44.09 | +2.2% / +4.9% | +0.5% | 26.8M |
| XLB | 52.67 (10:05 iex) | -0.7% | 53.02 | 53.09 / 52.62-53.20 | 1.00 (1.9%) | 49.90-54.63 | +1.8% / +4.2% | -1.6% | 12.4M |
| XLRE | 44.41 (10:05 iex) | -0.4% | 44.59 | 44.72 / 44.38-44.74 | 0.73 (1.6%) | 41.60-45.34 | +3.3% / +4.9% | -1.2% | 8.3M |
| XLC | 108.14 (10:05 iex) | -0.4% | 108.60 | 108.58 / 108.08-108.80 | 2.21 (2.0%) | 99.33-112.90 | +2.6% / -0.8% | +3.5% | 8.0M |
| KRE | 72.41 (10:05 iex) | -0.7% | 72.95 | 73.07 / 72.23-73.11 | 1.55 (2.1%) | 68.72-75.80 | +1.2% / +1.7% | -1.6% | 14.8M |
| XHB | 102.90 (10:04 iex) | -0.2% | 103.10 | 103.02 / 102.83-104.01 | 3.20 (3.1%) | 94.05-108.78 | +2.9% / +4.8% | -4.1% | 2.6M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 358.67 (10:05 iex) | +0.9% | 355.36 | 357.81 / 355.92-359.33 | 9.57 (2.7%) | 325.08-355.64 | +3.1% / +5.3% | +1.8% | 48.8M |
| MSFT | 525.04 (10:05 iex) | +0.8% | 521.12 | 521.10 / 520.50-526.29 | 17.51 (3.4%) | 504.96-559.15 | -1.8% / +0.6% | -6.2% | 26.7M |
| NVDA | 160.84 (10:05 iex) | -7.4% | 173.73 | 150.99 / 148.80-163.09 | 9.14 (5.3%) | 165.89-222.19 | -14.8% / -20.0% | -13.2% | 166.3M |
| AMZN | 272.78 (10:05 iex) | +2.5% | 266.17 | 268.09 / 267.62-273.58 | 10.31 (3.9%) | 229.36-275.34 | +4.0% / +4.6% | +0.1% | 50.6M |
| GOOGL | 295.74 (10:05 iex) | +0.8% | 293.45 | 293.77 / 293.69-296.93 | 11.09 (3.8%) | 276.92-352.15 | -4.8% / -11.0% | +1.6% | 40.2M |
| META | 623.11 (10:05 iex) | -0.9% | 628.77 | 625.42 / 621.50-630.32 | 21.23 (3.4%) | 583.80-743.97 | -2.7% / -7.3% | -0.2% | 24.4M |
| TSLA | 391.73 (10:05 iex) | +0.2% | 390.84 | 386.36 / 385.20-396.20 | 18.34 (4.7%) | 338.15-414.23 | +2.4% / +4.6% | +1.5% | 41.1M |
| AVGO | 360.60 (10:05 iex) | +4.5% | 345.22 | 356.51 / 354.72-365.71 | 17.86 (5.2%) | 289.77-356.85 | +4.9% / -0.1% | +6.1% | 26.0M |
| AMD | 562.55 (10:05 iex) | +1.7% | 552.90 | 569.28 / 554.90-578.78 | 42.82 (7.7%) | 402.10-579.18 | +6.8% / +0.4% | +13.1% | 32.1M |
| ORCL | 124.43 (10:05 iex) | -3.1% | 128.38 | 123.33 / 123.05-126.10 | 9.16 (7.1%) | 109.21-148.48 | +1.0% / -6.5% | +3.8% | 43.1M |
| NFLX | 63.28 (10:05 iex) | -1.9% | 64.54 | 64.27 / 62.87-64.30 | 1.84 (2.8%) | 61.39-73.07 | -1.1% / -7.8% | -2.8% | 46.6M |
| CRM | 215.33 (10:04 iex) | -1.2% | 218.01 | 218.53 / 213.77-219.35 | 8.67 (4.0%) | 208.88-252.42 | -6.5% / -8.0% | -4.0% | 7.2M |
| JPM | 343.86 (10:05 iex) | +0.1% | 343.39 | 345.75 / 343.45-347.20 | 7.94 (2.3%) | 330.40-359.80 | +1.5% / +0.9% | -2.5% | 6.9M |
| GS | 917.18 (10:05 iex) | -1.0% | 926.81 | 916.76 / 916.40-927.00 | 29.41 (3.2%) | 854.45-939.38 | +3.2% / +0.1% | -0.1% | 2.2M |
| BAC | 50.51 (10:05 iex) | -0.3% | 50.67 | 50.65 / 50.41-50.93 | 1.21 (2.4%) | 49.17-53.02 | +0.2% / -7.1% | -1.9% | 38.7M |
| XOM | 167.92 (10:05 iex) | +0.7% | 166.71 | 168.25 / 167.34-168.47 | 4.92 (2.9%) | 160.11-188.50 | -5.3% / -1.4% | -1.5% | 14.2M |
| CVX | 214.58 (10:04 iex) | +0.6% | 213.28 | 215.00 / 214.12-215.71 | 5.46 (2.6%) | 206.01-236.48 | -4.5% / -0.9% | -1.7% | 8.3M |
| LLY | 1,445.01 (10:04 iex) | +0.5% | 1,437.29 | 1,446.55 / 1,433.17-1,460.00 | 51.83 (3.6%) | 1,230.66-1,453.00 | +7.4% / +16.8% | +1.4% | 3.1M |
| UNH | 403.08 (10:05 iex) | +0.0% | 402.94 | 405.08 / 399.99-405.72 | 11.32 (2.8%) | 388.00-426.55 | -1.1% / +3.1% | -1.6% | 5.5M |
| JNJ | 282.87 (10:05 iex) | +0.9% | 280.41 | 284.38 / 281.11-285.48 | 7.25 (2.6%) | 251.50-283.25 | +4.4% / +5.2% | +1.5% | 7.5M |
| WMT | 126.14 (10:05 iex) | +0.4% | 125.67 | 126.86 / 125.48-127.66 | 3.11 (2.5%) | 116.63-131.82 | +2.7% / +10.5% | -2.7% | 22.8M |
| COST | 1,093.60 (10:05 iex) | +0.6% | 1,087.61 | 1,096.27 / 1,089.39-1,102.84 | 21.84 (2.0%) | 975.80-1,091.92 | +6.7% / +13.4% | +3.9% | 2.4M |
| HD | 351.97 (10:05 iex) | +0.2% | 351.31 | 355.07 / 351.62-356.46 | 9.99 (2.8%) | 301.42-362.44 | +6.5% / +13.0% | -1.2% | 4.7M |
| CAT | 594.94 (10:04 iex) | -1.1% | 601.61 | 592.91 / 590.70-600.59 | 31.32 (5.2%) | 550.81-743.23 | -8.5% / -19.5% | +1.7% | 4.0M |
| BA | 174.01 (10:05 iex) | -0.3% | 174.54 | 173.47 / 172.88-175.10 | 6.40 (3.7%) | 165.01-193.28 | -2.7% / -8.3% | -1.4% | 10.6M |
| DAL | 89.72 (10:04 iex) | -1.8% | 91.32 | 90.68 / 89.60-91.04 | 3.27 (3.6%) | 74.14-92.52 | +11.0% / +12.1% | +2.3% | 6.6M |
| UAL | 115.45 (10:04 iex) | -2.5% | 118.37 | 116.29 / 115.34-117.30 | 5.34 (4.5%) | 94.54-122.08 | +11.4% / +9.6% | +2.3% | 5.6M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| HUBS | 215.83 (10:06 iex) | +6.4% | 202.88 | 207.06 / 205.05-216.84 | 13.84 (6.8%) | 188.25-271.60 | -13.1% / -11.3% | -6.4% | 1.3M |
| ALL | 268.35 (10:06 iex) | +2.4% | 262.18 | 267.85 / 266.02-268.84 | 7.11 (2.7%) | 238.39-281.11 | +2.5% / +6.6% | -2.6% | 1.7M |
| BKNG | 163.39 (10:06 iex) | +2.0% | 160.21 | 161.38 / 159.00-163.56 | 6.76 (4.2%) | 146.28-174.30 | +1.0% / -2.4% | -6.3% | 8.0M |
| EXPE | 264.60 (10:03 iex) | +1.9% | 259.79 | 261.60 / 260.52-265.99 | 17.19 (6.6%) | 245.31-326.40 | -8.2% / -6.6% | -17.8% | 2.2M |
| VLO | 370.16 (10:06 iex) | +1.8% | 363.71 | 365.00 / 361.91-370.06 | 19.35 (5.3%) | 341.51-456.50 | -8.2% / -9.0% | -0.4% | 3.2M |
| MPC | 409.04 (10:05 iex) | +1.5% | 402.84 | 404.50 / 402.35-409.41 | 20.90 (5.2%) | 367.71-493.98 | -7.3% / -4.7% | +2.6% | 2.4M |
| ANET | 199.26 (10:06 iex) | +1.3% | 196.68 | 193.15 / 190.82-200.48 | 11.89 (6.0%) | 158.34-199.46 | +10.2% / +2.2% | +10.2% | 8.6M |
| MCD | 278.40 (10:06 iex) | +1.3% | 274.80 | 277.00 / 276.91-279.79 | 7.00 (2.5%) | 240.01-283.53 | +5.9% / +10.0% | -1.9% | 5.8M |
| SMCI | 27.90 (10:06 iex) | -8.3% | 30.43 | 27.21 / 26.96-28.30 | 2.41 (7.9%) | 25.81-37.45 | -4.7% / -17.7% | +2.8% | 44.2M |
| MSTR | 113.70 (10:06 iex) | -7.1% | 122.35 | 114.03 / 112.32-115.00 | 8.50 (7.0%) | 118.43-155.69 | -10.9% / -15.1% | -14.2% | 18.1M |
| SNDK | 909.77 (10:06 iex) | -6.9% | 977.69 | 886.86 / 869.46-937.88 | 108.99 (11.1%) | 803.97-1,424.48 | -16.3% / -33.4% | -5.8% | 11.8M |
| BABA | 94.69 (10:06 iex) | -6.7% | 101.52 | 95.51 / 93.42-95.92 | 3.19 (3.1%) | 97.48-112.17 | -2.2% / -5.6% | -3.6% | 9.5M |
| KDP | 36.05 (10:06 iex) | -5.8% | 38.25 | 36.50 / 35.88-36.78 | 1.17 (3.1%) | 33.65-38.28 | +7.3% / +15.5% | +4.0% | 18.7M |
| MOS | 21.57 (10:05 iex) | -5.4% | 22.80 | 22.33 / 21.43-22.40 | 1.04 (4.6%) | 16.99-23.73 | +16.9% / +5.4% | +5.5% | 11.4M |
| MU | 770.93 (10:06 iex) | -5.0% | 811.30 | 769.31 / 767.50-798.35 | 63.34 (7.8%) | 650.00-990.00 | -4.5% / -14.6% | +2.0% | 31.4M |
| PANW | 318.22 (10:06 iex) | -4.9% | 334.47 | 323.69 / 315.35-325.50 | 20.68 (6.2%) | 312.12-406.88 | -5.6% / -9.1% | -3.9% | 6.2M |
