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
