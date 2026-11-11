## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Wednesday 2026-11-11. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,165.95**
- Cash: $133,070.63
- Session P&L so far: -0.30% (new entries are blocked at -3.0%)
- Gross exposure: $80,905 (79% of equity, cap 150%)
- Net exposure: $-55,446 (-54%, cap +/-100%)
- Risk at stake (entry to stop): $2,323 (2.27% of equity, cap 4.0%) — 1.73% left for new plays
- Slots: 3 open + 3 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 46% of equity in notional: at 1% risk its stop must be at least 2.2% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 273.10 | -24 (-0.4%) | +6% | 263.50 | 293.00 |
| IWM | short | 85 | 281.03 | 283.05 | -172 (-0.7%) | -24% | 287.00 | 271.00 |
| XLE | short | 213 | 60.56 | 62.91 | -502 (-3.9%) | -13% | 63.10 | 57.30 |

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
| Ideas you passed on, or the caps dropped | 87 | 31 | 47 | +0.05R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 32 | 47% |
| 35%-40% | 57 | 32% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 40% of 121 brackets reached target first. Your Brier score is 0.241; saying 40% every time scores 0.239. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMZN | 272.90 (08:49 sip) | +0.7% | 270.87 | 10.68 (3.9%) | 229.36-275.34 | +6.1% / +6.6% | +8.0% | 50.4M |
| IWM | 283.10 (08:54 iex) | +0.9% | 280.58 | 5.21 (1.9%) | 269.88-286.17 | +1.2% / -0.3% | +0.3% | 25.7M |
| XLE | 62.97 (08:49 sip) | +1.2% | 62.21 | 1.88 (3.0%) | 60.43-70.15 | -6.7% / -4.2% | -6.7% | 37.6M |
| GLD | 369.80 (08:49 sip) | +0.1% | 369.36 | 7.57 (2.0%) | 354.67-384.88 | -0.7% / -3.7% | +2.8% | 9.2M |
| DAL | 91.38 (08:49 sip) | -0.9% | 92.20 | 3.48 (3.8%) | 74.14-92.52 | +13.1% / +13.6% | +10.7% | 6.6M |
| QQQ | 687.85 (09:02 iex) | +1.9% | 674.76 | 17.87 (2.6%) | 647.05-740.53 | -3.7% / -6.2% | -1.5% | 51.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 757.04 (08:49 sip) | +0.9% | 749.92 | 12.11 (1.6%) | 732.71-776.35 | -1.4% / -1.9% | -0.6% | 49.4M |
| QQQ | 687.85 (09:02 iex) | +1.9% | 674.76 | 17.87 (2.6%) | 647.05-740.53 | -3.7% / -6.2% | -1.5% | 51.9M |
| IWM | 283.10 (08:54 iex) | +0.9% | 280.58 | 5.21 (1.9%) | 269.88-286.17 | +1.2% / -0.3% | +0.3% | 25.7M |
| DIA | 523.27 (08:49 sip) | +0.3% | 521.73 | 7.74 (1.5%) | 508.66-536.60 | +0.1% / +0.4% | +0.9% | 3.9M |
| TLT | 80.82 (09:01 iex) | -0.1% | 80.88 | 0.80 (1.0%) | 77.41-82.42 | +0.1% / +1.2% | -0.3% | 39.6M |
| GLD | 369.80 (08:49 sip) | +0.1% | 369.36 | 7.57 (2.0%) | 354.67-384.88 | -0.7% / -3.7% | +2.8% | 9.2M |
| USO | 142.70 (08:49 sip) | +0.9% | 141.45 | 6.05 (4.3%) | 138.47-171.82 | -10.5% / -7.3% | -10.6% | 5.5M |
| SMH | 505.35 (08:49 sip) | +4.5% | 483.63 | 25.77 (5.3%) | 445.59-580.08 | -8.1% / -14.1% | -6.7% | 12.1M |
| XLK | 173.71 (08:49 sip) | +2.8% | 168.91 | 5.82 (3.4%) | 162.14-194.66 | -6.6% / -10.0% | -4.3% | 12.8M |
| XLF | 58.19 (08:45 sip) | -0.2% | 58.29 | 1.02 (1.7%) | 54.02-60.04 | +3.1% / +4.3% | +1.9% | 35.7M |
| XLE | 62.97 (08:49 sip) | +1.2% | 62.21 | 1.88 (3.0%) | 60.43-70.15 | -6.7% / -4.2% | -6.7% | 37.6M |
| XLV | 187.48 (08:40 sip) | -0.7% | 188.88 | 3.79 (2.0%) | 170.65-192.32 | +3.9% / +8.6% | +2.6% | 11.6M |
| XLI | 170.59 (08:15 sip) | +1.1% | 168.73 | 3.50 (2.1%) | 161.74-172.40 | +0.7% / -0.2% | -1.5% | 9.1M |
| XLY | 121.02 (07:35 sip) | -0.0% | 121.05 | 2.63 (2.2%) | 110.67-122.92 | +4.2% / +6.7% | +3.2% | 9.4M |
| XLP | 90.48 (08:49 sip) | -0.6% | 91.03 | 1.81 (2.0%) | 84.61-93.40 | +2.6% / +6.9% | +2.3% | 19.6M |
| XLU | 43.70 (08:45 sip) | -0.1% | 43.73 | 0.65 (1.5%) | 41.24-44.09 | +2.2% / +4.8% | +0.7% | 27.8M |
| XLB | 53.00 (08:35 sip) | +0.3% | 52.85 | 1.03 (2.0%) | 49.23-54.63 | +1.8% / +3.9% | +0.5% | 12.5M |
| XLRE | 44.44 (05:10 sip) | -0.3% | 44.58 | 0.75 (1.7%) | 41.31-45.34 | +3.6% / +5.0% | +2.1% | 8.5M |
| XLC | 108.06 (08:15 sip) | +0.3% | 107.76 | 2.28 (2.1%) | 99.33-112.90 | +1.7% / -1.6% | +6.2% | 8.1M |
| KRE | 73.27 (08:35 sip) | +0.2% | 73.09 | 1.67 (2.3%) | 67.79-75.80 | +1.7% / +2.0% | +0.3% | 15.3M |
| XHB | 103.70 (08:15 sip) | +0.5% | 103.17 | 3.42 (3.3%) | 91.87-108.78 | +3.5% / +4.9% | +1.2% | 2.5M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 347.34 (08:49 sip) | -0.3% | 348.51 | 9.49 (2.7%) | 325.33-355.38 | +1.2% / +3.3% | +5.0% | 49.5M |
| MSFT | 536.50 (08:49 sip) | +0.6% | 533.16 | 17.29 (3.2%) | 504.96-559.15 | +0.4% / +3.0% | +2.3% | 26.3M |
| NVDA | 174.85 (08:59 iex) | +3.5% | 168.89 | 9.29 (5.5%) | 165.89-226.00 | -18.1% / -22.5% | -18.3% | 155.3M |
| AMZN | 272.90 (08:49 sip) | +0.7% | 270.87 | 10.68 (3.9%) | 229.36-275.34 | +6.1% / +6.6% | +8.0% | 50.4M |
| GOOGL | 290.70 (08:49 sip) | +1.2% | 287.38 | 11.41 (4.0%) | 276.92-359.40 | -7.6% / -13.1% | +2.6% | 40.3M |
| META | 650.32 (08:49 iex) | +1.4% | 641.39 | 23.90 (3.7%) | 583.80-761.50 | -1.6% / -5.3% | +3.3% | 24.4M |
| TSLA | 385.15 (08:49 sip) | +1.4% | 379.78 | 18.31 (4.8%) | 338.15-414.23 | -0.2% / +1.8% | -4.7% | 41.2M |
| AVGO | 346.33 (08:58 iex) | +4.3% | 331.98 | 17.29 (5.2%) | 289.77-354.25 | +0.9% / -4.0% | -0.0% | 25.5M |
| AMD | 543.79 (09:04 iex) | +5.5% | 515.21 | 42.65 (8.3%) | 402.10-591.88 | -0.6% / -6.1% | +6.5% | 30.9M |
| ORCL | 123.71 (08:49 sip) | +4.9% | 117.98 | 8.71 (7.4%) | 109.21-148.48 | -7.3% / -14.2% | -6.5% | 43.8M |
| NFLX | 63.07 (08:49 sip) | -0.3% | 63.26 | 1.88 (3.0%) | 61.39-73.07 | -3.5% / -10.0% | -0.3% | 47.1M |
| CRM | 215.52 (08:49 sip) | +1.0% | 213.48 | 9.09 (4.3%) | 208.88-252.42 | -8.8% / -10.2% | -3.9% | 7.2M |
| JPM | 343.15 (08:49 sip) | +0.3% | 342.07 | 7.95 (2.3%) | 326.40-359.80 | +1.2% / +0.5% | +1.2% | 7.2M |
| GS | 926.00 (08:45 sip) | +1.7% | 910.19 | 29.62 (3.3%) | 854.45-939.38 | +1.6% / -1.9% | +1.6% | 2.2M |
| BAC | 50.88 (08:49 sip) | +0.4% | 50.68 | 1.24 (2.5%) | 49.17-53.02 | +0.1% / -7.5% | +2.1% | 43.7M |
| XOM | 165.90 (08:49 sip) | +0.9% | 164.47 | 5.16 (3.1%) | 160.11-188.50 | -6.8% / -2.7% | -7.3% | 14.2M |
| CVX | 212.85 (08:49 sip) | +0.8% | 211.22 | 5.72 (2.7%) | 206.01-236.48 | -5.6% / -1.8% | -6.2% | 8.4M |
| LLY | 1,415.94 (08:49 sip) | -1.1% | 1,432.29 | 53.57 (3.7%) | 1,174.24-1,453.00 | +8.0% / +17.0% | +1.6% | 3.2M |
| UNH | 402.52 (08:45 sip) | -0.6% | 405.12 | 11.42 (2.8%) | 382.29-426.55 | -0.5% / +3.7% | +0.2% | 5.7M |
| JNJ | 277.71 (08:49 sip) | -1.1% | 280.78 | 7.77 (2.8%) | 248.50-283.25 | +5.1% / +5.4% | +5.5% | 7.7M |
| WMT | 124.42 (08:49 sip) | -0.9% | 125.55 | 3.19 (2.5%) | 113.38-131.82 | +3.0% / +10.8% | +0.6% | 23.0M |
| COST | 1,084.00 (08:49 sip) | +1.7% | 1,066.14 | 21.46 (2.0%) | 958.58-1,081.55 | +5.1% / +11.5% | +4.6% | 2.5M |
| HD | 347.75 (08:45 sip) | -0.9% | 351.00 | 10.50 (3.0%) | 289.57-362.44 | +7.3% / +13.1% | +5.2% | 4.8M |
| CAT | 602.85 (08:49 sip) | +3.1% | 584.57 | 32.66 (5.6%) | 550.81-768.52 | -12.1% / -22.1% | -6.3% | 4.0M |
| BA | 173.66 (08:49 sip) | +0.2% | 173.38 | 6.67 (3.8%) | 165.01-193.28 | -3.6% / -9.2% | +0.0% | 10.6M |
| DAL | 91.38 (08:49 sip) | -0.9% | 92.20 | 3.48 (3.8%) | 74.14-92.52 | +13.1% / +13.6% | +10.7% | 6.6M |
| UAL | 119.61 (08:40 sip) | -0.8% | 120.56 | 5.59 (4.6%) | 94.54-122.08 | +14.5% / +11.9% | +12.5% | 5.6M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| STX | 547.25 (08:49 sip) | +9.1% | 501.62 | 54.27 (10.8%) | 449.28-751.81 | -19.1% / -33.7% | -17.3% | 6.1M |
| MRVL | 167.70 (08:49 sip) | +8.6% | 154.39 | 18.53 (12.0%) | 132.54-264.30 | -25.0% / -33.4% | -10.2% | 29.8M |
| WDC | 312.88 (08:49 sip) | +8.2% | 289.20 | 28.27 (9.8%) | 258.61-402.23 | -15.7% / -27.7% | -16.7% | 9.3M |
| SNDK | 929.54 (08:49 sip) | +8.1% | 859.99 | 107.74 (12.5%) | 803.97-1,461.80 | -27.7% / -41.8% | -23.7% | 11.4M |
| DELL | 360.30 (08:50 iex) | +7.8% | 334.38 | 33.23 (9.9%) | 315.00-547.63 | -22.3% / -33.1% | -18.1% | 7.7M |
| TER | 263.26 (08:49 sip) | +7.3% | 245.40 | 23.80 (9.7%) | 211.63-371.71 | -16.6% / -29.3% | -8.9% | 4.6M |
| GLW | 119.97 (08:49 sip) | +7.0% | 112.13 | 8.15 (7.3%) | 101.83-147.17 | -10.4% / -21.6% | -11.1% | 10.9M |
| MU | 774.59 (09:04 iex) | +6.8% | 725.11 | 60.62 (8.4%) | 650.00-990.00 | -15.2% / -23.9% | -15.2% | 31.0M |
| NUE | 251.60 (08:15 sip) | -1.9% | 256.47 | 11.73 (4.6%) | 244.64-287.70 | -2.0% / +0.6% | -6.2% | 1.6M |
| AMT | 187.00 (07:25 sip) | -1.8% | 190.37 | 6.28 (3.3%) | 175.78-202.50 | +2.3% / +7.5% | +1.6% | 3.4M |
| DG | 135.00 (08:49 sip) | -1.7% | 137.31 | 5.69 (4.1%) | 123.86-144.61 | +3.0% / +7.5% | +5.2% | 2.3M |
| CHTR | 132.00 (08:49 sip) | -1.5% | 134.06 | 6.97 (5.2%) | 101.11-134.92 | +19.0% / +11.8% | +17.8% | 3.0M |
| EW | 102.53 (07:05 sip) | -1.4% | 104.01 | 3.35 (3.2%) | 84.83-105.37 | +11.6% / +16.2% | +9.3% | 4.8M |
| ACN | 255.00 (08:10 sip) | -1.4% | 258.51 | 11.95 (4.6%) | 212.71-271.76 | +4.6% / +21.7% | +1.6% | 6.3M |
| SYK | 319.99 (07:25 sip) | -1.3% | 324.29 | 12.60 (3.9%) | 278.57-349.48 | +5.2% / +11.1% | +4.4% | 3.2M |
| ABNB | 184.43 (08:49 sip) | -1.3% | 186.90 | 7.09 (3.8%) | 163.82-197.87 | +7.5% / +10.5% | +11.9% | 4.6M |
