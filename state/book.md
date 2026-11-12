## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Thursday 2026-11-12. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,158.33**
- Cash: $119,651.62
- Session P&L so far: +0.18% (new entries are blocked at -3.0%)
- Gross exposure: $67,306 (66% of equity, cap 150%)
- Net exposure: $-42,034 (-41%, cap +/-100%)
- Risk at stake (entry to stop): $1,781 (1.74% of equity, cap 4.0%) — 2.26% left for new plays
- Slots: 2 open + 3 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 269.19 | -118 (-1.8%) | +6% | 263.50 | 293.00 |
| IWM | short | 85 | 281.03 | 281.81 | -67 (-0.3%) | -23% | 287.00 | 271.00 |

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
| Ideas you passed on, or the caps dropped | 89 | 31 | 49 | +0.03R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 33 | 45% |
| 35%-40% | 59 | 31% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 124 brackets reached target first. Your Brier score is 0.238; saying 39% every time scores 0.237. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMZN | 269.05 (09:04 iex) | +1.1% | 266.17 | 10.31 (3.9%) | 229.36-275.34 | +4.0% / +4.6% | +0.1% | 50.6M |
| IWM | 281.51 (08:49 sip) | -0.6% | 283.09 | 5.23 (1.8%) | 269.88-286.17 | +1.9% / +0.6% | -0.3% | 24.7M |
| GLD | 356.39 (08:56 iex) | -2.4% | 365.17 | 7.13 (2.0%) | 354.67-384.88 | -1.7% / -4.6% | -2.0% | 8.9M |
| DAL | 90.14 (08:45 sip) | -1.3% | 91.32 | 3.27 (3.6%) | 74.14-92.52 | +11.0% / +12.1% | +2.3% | 6.6M |
| QQQ | 681.75 (08:53 iex) | -1.3% | 690.38 | 17.69 (2.6%) | 647.05-729.43 | -1.2% / -4.0% | -0.2% | 51.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 755.12 (08:57 iex) | -0.6% | 759.81 | 12.15 (1.6%) | 732.71-775.64 | -0.1% / -0.6% | -0.9% | 48.6M |
| QQQ | 681.75 (08:53 iex) | -1.3% | 690.38 | 17.69 (2.6%) | 647.05-729.43 | -1.2% / -4.0% | -0.2% | 51.5M |
| IWM | 281.51 (08:49 sip) | -0.6% | 283.09 | 5.23 (1.8%) | 269.88-286.17 | +1.9% / +0.6% | -0.3% | 24.7M |
| DIA | 523.25 (08:55 iex) | -0.2% | 524.44 | 7.77 (1.5%) | 508.66-536.60 | +0.5% / +1.0% | -1.6% | 3.9M |
| TLT | 80.66 (09:00 iex) | -0.3% | 80.92 | 0.71 (0.9%) | 79.01-82.42 | -0.0% / +1.3% | -1.0% | 38.3M |
| GLD | 356.39 (08:56 iex) | -2.4% | 365.17 | 7.13 (2.0%) | 354.67-384.88 | -1.7% / -4.6% | -2.0% | 8.9M |
| USO | 142.52 (08:49 sip) | +0.7% | 141.47 | 6.06 (4.3%) | 138.47-171.82 | -10.1% / -7.3% | -2.7% | 5.5M |
| SMH | 488.04 (08:58 iex) | -3.7% | 506.96 | 25.55 (5.0%) | 445.59-571.00 | -3.2% / -9.8% | +0.5% | 12.3M |
| XLK | 170.52 (08:49 sip) | -2.2% | 174.36 | 5.86 (3.4%) | 162.14-191.55 | -3.2% / -7.0% | -1.2% | 13.0M |
| XLF | 58.78 (08:49 sip) | +0.3% | 58.63 | 1.00 (1.7%) | 54.59-60.04 | +3.3% / +4.9% | -1.0% | 34.7M |
| XLE | 64.17 (08:49 sip) | +1.3% | 63.37 | 1.79 (2.8%) | 60.43-70.15 | -4.6% / -2.4% | -0.2% | 37.6M |
| XLV | 190.15 (08:49 sip) | +0.6% | 188.95 | 3.73 (2.0%) | 175.27-192.32 | +3.5% / +8.4% | -0.4% | 11.4M |
| XLI | 170.52 (08:49 sip) | -0.3% | 170.97 | 3.44 (2.0%) | 161.74-172.40 | +2.0% / +1.1% | +0.9% | 8.9M |
| XLY | 120.59 (08:35 sip) | -0.3% | 120.99 | 2.60 (2.1%) | 111.70-122.92 | +3.8% / +6.5% | -1.1% | 9.4M |
| XLP | 92.00 (08:49 sip) | +0.6% | 91.45 | 1.69 (1.9%) | 86.36-93.40 | +2.7% / +7.3% | -0.5% | 19.7M |
| XLU | 43.91 (08:49 sip) | +0.2% | 43.82 | 0.61 (1.4%) | 41.28-44.09 | +2.2% / +4.9% | +0.5% | 26.8M |
| XLB | 52.93 (08:15 sip) | -0.2% | 53.02 | 1.00 (1.9%) | 49.90-54.63 | +1.8% / +4.2% | -1.6% | 12.4M |
| XLRE | 44.60 (08:35 sip) | +0.0% | 44.59 | 0.73 (1.6%) | 41.60-45.34 | +3.3% / +4.9% | -1.2% | 8.3M |
| XLC | 108.02 (08:15 sip) | -0.5% | 108.60 | 2.21 (2.0%) | 99.33-112.90 | +2.6% / -0.8% | +3.5% | 8.0M |
| KRE | 72.96 (08:49 sip) | +0.0% | 72.95 | 1.55 (2.1%) | 68.72-75.80 | +1.2% / +1.7% | -1.6% | 14.8M |
| XHB | 102.85 (08:15 sip) | -0.2% | 103.10 | 3.20 (3.1%) | 94.05-108.78 | +2.9% / +4.8% | -4.1% | 2.6M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 357.84 (09:05 iex) | +0.7% | 355.36 | 9.57 (2.7%) | 325.08-355.64 | +3.1% / +5.3% | +1.8% | 48.8M |
| MSFT | 522.20 (09:05 iex) | +0.2% | 521.12 | 17.51 (3.4%) | 504.96-559.15 | -1.8% / +0.6% | -6.2% | 26.7M |
| NVDA | 155.38 (09:04 iex) | -10.6% | 173.73 | 9.14 (5.3%) | 165.89-222.19 | -14.8% / -20.0% | -13.2% | 166.3M |
| AMZN | 269.05 (09:04 iex) | +1.1% | 266.17 | 10.31 (3.9%) | 229.36-275.34 | +4.0% / +4.6% | +0.1% | 50.6M |
| GOOGL | 295.56 (08:57 iex) | +0.7% | 293.45 | 11.09 (3.8%) | 276.92-352.15 | -4.8% / -11.0% | +1.6% | 40.2M |
| META | 626.54 (08:58 iex) | -0.4% | 628.77 | 21.23 (3.4%) | 583.80-743.97 | -2.7% / -7.3% | -0.2% | 24.4M |
| TSLA | 386.05 (08:49 sip) | -1.2% | 390.84 | 18.34 (4.7%) | 338.15-414.23 | +2.4% / +4.6% | +1.5% | 41.1M |
| AVGO | 351.89 (09:04 iex) | +1.9% | 345.22 | 17.86 (5.2%) | 289.77-356.85 | +4.9% / -0.1% | +6.1% | 26.0M |
| AMD | 563.69 (09:01 iex) | +2.0% | 552.90 | 42.82 (7.7%) | 402.10-579.18 | +6.8% / +0.4% | +13.1% | 32.1M |
| ORCL | 123.14 (08:56 iex) | -4.1% | 128.38 | 9.16 (7.1%) | 109.21-148.48 | +1.0% / -6.5% | +3.8% | 43.1M |
| NFLX | 64.28 (08:49 sip) | -0.4% | 64.54 | 1.84 (2.8%) | 61.39-73.07 | -1.1% / -7.8% | -2.8% | 46.6M |
| CRM | 217.50 (08:49 sip) | -0.2% | 218.01 | 8.67 (4.0%) | 208.88-252.42 | -6.5% / -8.0% | -4.0% | 7.2M |
| JPM | 343.80 (08:49 sip) | +0.1% | 343.39 | 7.94 (2.3%) | 330.40-359.80 | +1.5% / +0.9% | -2.5% | 6.9M |
| GS | 915.44 (08:49 sip) | -1.2% | 926.81 | 29.41 (3.2%) | 854.45-939.38 | +3.2% / +0.1% | -0.1% | 2.2M |
| BAC | 50.62 (08:49 sip) | -0.1% | 50.67 | 1.21 (2.4%) | 49.17-53.02 | +0.2% / -7.1% | -1.9% | 38.7M |
| XOM | 169.00 (08:49 sip) | +1.4% | 166.71 | 4.92 (2.9%) | 160.11-188.50 | -5.3% / -1.4% | -1.5% | 14.2M |
| CVX | 216.28 (08:49 sip) | +1.4% | 213.28 | 5.46 (2.6%) | 206.01-236.48 | -4.5% / -0.9% | -1.7% | 8.3M |
| LLY | 1,455.44 (08:54 iex) | +1.3% | 1,437.29 | 51.83 (3.6%) | 1,230.66-1,453.00 | +7.4% / +16.8% | +1.4% | 3.1M |
| UNH | 403.30 (08:45 sip) | +0.1% | 402.94 | 11.32 (2.8%) | 388.00-426.55 | -1.1% / +3.1% | -1.6% | 5.5M |
| JNJ | 281.50 (08:35 sip) | +0.4% | 280.41 | 7.25 (2.6%) | 251.50-283.25 | +4.4% / +5.2% | +1.5% | 7.5M |
| WMT | 126.43 (08:49 sip) | +0.6% | 125.67 | 3.11 (2.5%) | 116.63-131.82 | +2.7% / +10.5% | -2.7% | 22.8M |
| COST | 1,095.00 (08:49 sip) | +0.7% | 1,087.61 | 21.84 (2.0%) | 975.80-1,091.92 | +6.7% / +13.4% | +3.9% | 2.4M |
| HD | 351.66 (08:49 sip) | +0.1% | 351.31 | 9.99 (2.8%) | 301.42-362.44 | +6.5% / +13.0% | -1.2% | 4.7M |
| CAT | 592.46 (08:49 sip) | -1.5% | 601.61 | 31.32 (5.2%) | 550.81-743.23 | -8.5% / -19.5% | +1.7% | 4.0M |
| BA | 173.24 (08:49 sip) | -0.7% | 174.54 | 6.40 (3.7%) | 165.01-193.28 | -2.7% / -8.3% | -1.4% | 10.6M |
| DAL | 90.14 (08:45 sip) | -1.3% | 91.32 | 3.27 (3.6%) | 74.14-92.52 | +11.0% / +12.1% | +2.3% | 6.6M |
| UAL | 116.00 (08:45 sip) | -2.0% | 118.37 | 5.34 (4.5%) | 94.54-122.08 | +11.4% / +9.6% | +2.3% | 5.6M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| HUBS | 219.94 (08:45 sip) | +8.4% | 202.88 | 13.84 (6.8%) | 188.25-271.60 | -13.1% / -11.3% | -6.4% | 1.3M |
| EW | 108.04 (04:05 sip) | +2.1% | 105.81 | 3.45 (3.3%) | 85.54-106.05 | +12.4% / +17.9% | +6.5% | 4.9M |
| EOG | 156.40 (08:49 sip) | +1.7% | 153.77 | 4.88 (3.2%) | 144.14-165.93 | -1.5% / +3.2% | +4.6% | 3.3M |
| OXY | 58.19 (08:49 sip) | +1.7% | 57.24 | 1.92 (3.4%) | 53.86-64.95 | -5.8% / -4.3% | -0.2% | 10.2M |
| ICE | 183.37 (07:45 sip) | +1.5% | 180.59 | 4.61 (2.6%) | 153.90-180.71 | +8.8% / +13.2% | +3.2% | 3.6M |
| VLO | 369.00 (08:49 sip) | +1.5% | 363.71 | 19.35 (5.3%) | 341.51-456.50 | -8.2% / -9.0% | -0.4% | 3.2M |
| SYK | 323.00 (08:25 sip) | +1.3% | 318.79 | 12.37 (3.9%) | 282.18-349.48 | +2.8% / +9.2% | -6.1% | 3.3M |
| DG | 139.22 (08:45 sip) | +1.3% | 137.44 | 5.41 (3.9%) | 124.62-144.61 | +2.8% / +7.5% | -3.0% | 2.3M |
| SMCI | 27.37 (09:03 iex) | -10.1% | 30.43 | 2.41 (7.9%) | 25.81-37.45 | -4.7% / -17.7% | +2.8% | 44.2M |
| SNDK | 893.76 (09:04 iex) | -8.6% | 977.69 | 108.99 (11.1%) | 803.97-1,424.48 | -16.3% / -33.4% | -5.8% | 11.8M |
| MSTR | 114.70 (08:49 sip) | -6.3% | 122.35 | 8.50 (7.0%) | 118.43-155.69 | -10.9% / -15.1% | -14.2% | 18.1M |
| MU | 761.81 (09:01 iex) | -6.1% | 811.30 | 63.34 (7.8%) | 650.00-990.00 | -4.5% / -14.6% | +2.0% | 31.4M |
| DELL | 351.66 (08:49 sip) | -5.9% | 373.68 | 34.04 (9.1%) | 315.00-507.38 | -11.8% / -25.1% | +0.4% | 7.6M |
| STX | 526.00 (08:49 sip) | -4.7% | 551.72 | 54.23 (9.8%) | 449.28-718.65 | -9.8% / -26.5% | -1.0% | 6.3M |
| BABA | 96.80 (08:49 sip) | -4.6% | 101.52 | 3.19 (3.1%) | 97.48-112.17 | -2.2% / -5.6% | -3.6% | 9.5M |
| MRVL | 161.30 (08:49 sip) | -4.4% | 168.80 | 18.22 (10.8%) | 132.54-253.66 | -16.5% / -26.9% | +5.6% | 30.2M |
