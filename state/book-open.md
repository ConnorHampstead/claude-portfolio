## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Monday 2026-11-16. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,438.09**
- Cash: $125,772.29
- Session P&L so far: +0.20% (new entries are blocked at -3.0%)
- Gross exposure: $44,364 (43% of equity, cap 150%)
- Net exposure: $-44,364 (-43%, cap +/-100%)
- Risk at stake (entry to stop): $1,018 (0.99% of equity, cap 4.0%) — 3.01% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| IWM | short | 85 | 281.03 | 274.52 | +553 (+2.3%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **IWM**, opened 2026-11-10 (session 5 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 350.50 | stop | 359.00 | 333.00 | 2026-11-16 |

### Your record

49 closed trades: 15W / 34L, total -0.64R, net $+1,900 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 49 | 17 | 29 | -0.01R |
| The same trades, bracket left alone | 49 | | | +0.01R |
| Ideas you passed on, or the caps dropped | 97 | 34 | 54 | +0.02R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 39 | 46% |
| 35%-40% | 63 | 29% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 38% of 134 brackets reached target first. Your Brier score is 0.237; saying 38% every time scores 0.236. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| AMZN | long | stop | -1.20R | $-303 | 36% |
| DAL | long | stop | -0.60R | $-154 | 37% |
| XLE | short | close | -1.02R | $-521 | 37% |
| AVGO | short | close | -0.92R | $-232 | 37% |
| NVDA | short | target | +2.16R | $+1,108 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| IWM | 274.54 (10:05 iex) | -1.1% | 277.54 | 276.10 / 274.57-276.54 | 5.46 (2.0%) | 270.23-286.17 | -0.3% / -1.1% | +1.4% | 23.4M |
| GLD | 355.47 (10:05 iex) | +0.0% | 355.45 | 354.13 / 353.97-356.29 | 7.60 (2.1%) | 352.91-381.93 | -3.6% / -6.7% | -4.6% | 9.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 744.77 (10:05 iex) | -1.3% | 754.37 | 749.67 / 744.92-749.82 | 12.77 (1.7%) | 732.71-775.64 | -0.6% / -1.3% | +2.6% | 47.0M |
| QQQ | 665.25 (10:05 iex) | -2.2% | 679.89 | 671.04 / 665.50-672.15 | 18.61 (2.7%) | 647.05-727.95 | -2.2% / -5.3% | +3.6% | 49.6M |
| IWM | 274.54 (10:05 iex) | -1.1% | 277.54 | 276.10 / 274.57-276.54 | 5.46 (2.0%) | 270.23-286.17 | -0.3% / -1.1% | +1.4% | 23.4M |
| DIA | 520.49 (10:04 iex) | -0.5% | 523.15 | 522.98 / 520.29-523.09 | 7.61 (1.5%) | 508.66-536.60 | +0.2% / +0.8% | +2.1% | 3.6M |
| TLT | 79.73 (10:05 iex) | +0.4% | 79.38 | 79.51 / 79.47-79.72 | 0.76 (1.0%) | 79.01-82.42 | -1.9% / -0.6% | -3.1% | 35.8M |
| GLD | 355.47 (10:05 iex) | +0.0% | 355.45 | 354.13 / 353.97-356.29 | 7.60 (2.1%) | 352.91-381.93 | -3.6% / -6.7% | -4.6% | 9.3M |
| USO | 142.06 (10:04 iex) | -2.4% | 145.58 | 142.69 / 138.36-142.69 | 5.67 (3.9%) | 138.47-171.82 | -6.7% / -4.7% | -1.9% | 5.4M |
| SMH | 464.89 (10:05 iex) | -4.5% | 486.75 | 468.71 / 462.56-473.33 | 27.23 (5.6%) | 445.59-571.00 | -6.1% / -13.0% | +4.9% | 11.8M |
| XLK | 165.72 (10:05 iex) | -2.7% | 170.28 | 166.58 / 165.51-167.75 | 6.27 (3.7%) | 162.14-191.55 | -4.7% / -9.0% | +3.4% | 12.5M |
| XLF | 58.52 (10:05 iex) | -0.3% | 58.68 | 58.78 / 58.45-58.81 | 1.01 (1.7%) | 55.03-60.04 | +2.8% / +4.9% | +2.7% | 32.9M |
| XLE | 63.81 (10:05 iex) | -1.8% | 64.96 | 64.52 / 63.80-64.69 | 1.71 (2.6%) | 60.43-70.15 | -1.8% / +0.1% | +5.4% | 36.4M |
| XLV | 189.91 (10:05 iex) | +0.6% | 188.85 | 190.70 / 189.68-191.33 | 3.70 (2.0%) | 175.27-192.32 | +2.8% / +8.0% | +2.2% | 11.1M |
| XLI | 167.29 (10:05 iex) | -0.9% | 168.78 | 167.72 / 167.44-168.49 | 3.38 (2.0%) | 161.74-172.40 | +0.6% / -0.1% | +3.8% | 8.7M |
| XLY | 118.67 (10:05 iex) | -1.1% | 119.98 | 119.62 / 118.64-119.81 | 2.56 (2.1%) | 112.67-122.92 | +2.3% / +5.5% | +2.0% | 9.0M |
| XLP | 92.98 (10:05 iex) | +0.7% | 92.35 | 93.22 / 92.71-93.48 | 1.64 (1.8%) | 86.36-93.40 | +3.2% / +8.0% | +2.5% | 19.0M |
| XLU | 44.31 (10:05 iex) | +0.6% | 44.04 | 44.23 / 44.19-44.40 | 0.60 (1.4%) | 41.28-44.14 | +2.2% / +5.3% | +2.1% | 25.0M |
| XLB | 52.17 (10:05 iex) | -0.1% | 52.23 | 52.22 / 51.95-52.30 | 1.03 (2.0%) | 50.61-54.63 | -0.0% / +2.7% | +0.5% | 11.9M |
| XLRE | 44.45 (10:05 iex) | +0.2% | 44.37 | 44.57 / 44.45-44.66 | 0.69 (1.6%) | 41.60-45.34 | +2.2% / +4.3% | +0.8% | 7.9M |
| XLC | 107.34 (10:05 iex) | -1.2% | 108.69 | 109.03 / 107.28-109.11 | 2.16 (2.0%) | 99.33-110.84 | +3.0% / -0.6% | +3.7% | 7.9M |
| KRE | 72.50 (10:05 iex) | -0.3% | 72.74 | 72.83 / 72.41-73.02 | 1.54 (2.1%) | 69.17-75.80 | +0.5% / +1.5% | +0.7% | 13.9M |
| XHB | 102.30 (10:05 iex) | +0.2% | 102.07 | 102.01 / 101.80-102.60 | 3.26 (3.2%) | 94.05-108.78 | +1.2% / +3.7% | -0.2% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 353.65 (10:04 iex) | -0.7% | 356.27 | 357.12 / 353.42-357.14 | 9.45 (2.7%) | 325.08-360.83 | +3.0% / +5.2% | +4.1% | 47.4M |
| MSFT | 520.74 (10:05 iex) | -0.6% | 523.88 | 525.09 / 518.81-527.95 | 17.55 (3.4%) | 504.96-559.15 | -1.0% / +0.9% | -1.3% | 26.5M |
| NVDA | 159.34 (10:05 iex) | -2.2% | 162.85 | 159.00 / 158.11-163.20 | 11.00 (6.8%) | 148.80-222.19 | -18.0% / -24.1% | -12.7% | 209.6M |
| AMZN | 260.44 (10:05 iex) | -2.3% | 266.66 | 262.39 / 260.17-262.92 | 10.74 (4.0%) | 229.36-275.34 | +3.6% / +4.6% | +2.8% | 50.1M |
| GOOGL | 287.21 (10:05 iex) | -2.9% | 295.77 | 293.81 / 287.23-294.14 | 11.91 (4.0%) | 276.92-346.58 | -2.5% / -9.9% | +3.9% | 41.0M |
| META | 627.71 (10:05 iex) | -2.2% | 641.69 | 640.00 / 627.68-640.88 | 20.96 (3.3%) | 583.80-713.22 | +0.7% / -5.6% | +5.2% | 23.8M |
| TSLA | 377.66 (10:05 iex) | -3.2% | 390.22 | 387.01 / 376.84-389.80 | 18.16 (4.7%) | 338.15-414.23 | +1.3% / +4.1% | +8.9% | 39.7M |
| AVGO | 329.86 (10:05 iex) | -4.9% | 347.01 | 332.20 / 328.88-334.69 | 20.25 (5.8%) | 289.77-369.82 | +4.8% / +0.5% | +18.2% | 26.9M |
| AMD | 510.61 (10:05 iex) | -4.4% | 534.06 | 503.44 / 502.22-526.20 | 47.88 (9.0%) | 402.10-594.00 | +2.9% / -3.7% | +18.9% | 34.7M |
| ORCL | 120.55 (10:05 iex) | -3.8% | 125.35 | 122.78 / 120.25-123.14 | 9.46 (7.5%) | 109.21-148.48 | -1.0% / -8.1% | +8.0% | 42.0M |
| NFLX | 61.63 (10:05 iex) | -0.8% | 62.15 | 62.98 / 61.48-62.98 | 1.75 (2.8%) | 61.39-70.66 | -3.4% / -10.2% | -2.0% | 45.8M |
| CRM | 215.72 (10:05 iex) | -1.0% | 217.84 | 217.92 / 213.57-219.20 | 8.28 (3.8%) | 208.88-252.42 | -5.5% / -7.4% | +2.0% | 6.8M |
| JPM | 343.80 (10:03 iex) | -0.7% | 346.19 | 345.57 / 343.68-346.52 | 7.78 (2.2%) | 330.40-359.80 | +2.1% / +1.9% | +3.5% | 6.4M |
| GS | 896.31 (10:04 iex) | -2.2% | 916.56 | 906.49 / 893.77-908.99 | 28.97 (3.2%) | 854.45-939.38 | +1.8% / -0.6% | +5.9% | 2.0M |
| BAC | 50.52 (10:05 iex) | -1.0% | 51.02 | 50.85 / 50.42-50.90 | 1.17 (2.3%) | 49.17-53.02 | +1.0% / -5.6% | +3.2% | 35.2M |
| XOM | 168.00 (10:05 iex) | -0.9% | 169.52 | 169.53 / 167.26-170.25 | 4.75 (2.8%) | 159.11-187.32 | -2.7% / +0.7% | +2.8% | 14.2M |
| CVX | 217.27 (10:04 iex) | -1.2% | 219.89 | 220.03 / 216.57-220.03 | 5.30 (2.4%) | 206.01-236.48 | -1.4% / +2.0% | +3.4% | 8.3M |
| LLY | 1,465.37 (10:05 iex) | +1.5% | 1,443.50 | 1,453.75 / 1,453.01-1,475.25 | 50.97 (3.5%) | 1,237.60-1,458.23 | +6.6% / +16.4% | +6.7% | 3.0M |
| UNH | 411.84 (10:05 iex) | +1.1% | 407.46 | 412.00 / 409.74-415.19 | 10.81 (2.7%) | 388.00-426.55 | -0.1% / +4.2% | +3.4% | 4.9M |
| JNJ | 286.99 (10:04 iex) | +0.4% | 285.75 | 288.98 / 286.57-290.25 | 7.13 (2.5%) | 251.50-288.11 | +5.2% / +7.1% | +3.5% | 7.5M |
| WMT | 128.82 (10:05 iex) | +0.6% | 128.09 | 129.83 / 128.51-129.85 | 3.02 (2.4%) | 116.63-131.82 | +3.9% / +11.8% | +2.0% | 21.8M |
| COST | 1,107.24 (10:05 iex) | +0.1% | 1,106.21 | 1,111.44 / 1,105.03-1,117.00 | 21.67 (2.0%) | 978.87-1,109.50 | +7.2% / +14.5% | +5.0% | 2.4M |
| HD | 348.46 (10:04 iex) | -0.1% | 348.69 | 348.52 / 346.21-349.21 | 9.94 (2.9%) | 306.00-362.44 | +4.5% / +11.7% | +1.5% | 4.4M |
| CAT | 582.76 (10:04 iex) | -2.9% | 600.20 | 588.00 / 582.50-592.00 | 31.68 (5.3%) | 550.81-743.23 | -6.9% / -18.8% | +7.4% | 3.8M |
| BA | 167.71 (10:04 iex) | -2.2% | 171.50 | 170.21 / 167.71-170.50 | 6.10 (3.6%) | 165.01-193.28 | -3.5% / -9.2% | -1.1% | 10.5M |
| DAL | 87.44 (10:02 iex) | +1.4% | 86.25 | 86.00 / 85.62-88.10 | 3.30 (3.8%) | 74.14-92.52 | +3.6% / +5.4% | -1.1% | 6.6M |
| UAL | 112.13 (10:04 iex) | +2.6% | 109.31 | 108.37 / 108.37-113.24 | 5.42 (5.0%) | 94.54-122.08 | +1.8% / +1.1% | -3.0% | 5.7M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| CNC | 75.03 (10:04 iex) | +5.3% | 71.27 | 74.04 / 73.92-75.36 | 3.78 (5.3%) | 64.85-78.08 | +2.1% / +6.3% | +2.2% | 5.8M |
| LUV | 46.48 (10:05 iex) | +3.4% | 44.94 | 45.16 / 44.95-46.58 | 1.71 (3.8%) | 38.50-47.01 | +3.3% / +7.3% | +1.1% | 6.6M |
| GIS | 35.44 (10:05 iex) | +3.2% | 34.32 | 34.84 / 34.83-35.48 | 1.08 (3.1%) | 32.37-37.02 | +0.3% / +1.1% | -3.4% | 8.3M |
| ELV | 443.29 (10:05 iex) | +3.2% | 429.69 | 438.27 / 438.27-444.56 | 13.31 (3.1%) | 406.90-450.69 | +0.5% / +3.5% | +1.0% | 1.4M |
| NUE | 259.04 (10:04 iex) | +2.9% | 251.73 | 254.79 / 253.01-259.10 | 11.16 (4.4%) | 244.64-287.70 | -3.9% / -1.3% | +2.8% | 1.6M |
| HSY | 177.62 (10:05 iex) | +2.8% | 172.82 | 177.31 / 174.68-178.03 | 5.52 (3.2%) | 158.55-178.33 | +2.1% / +3.6% | -2.1% | 2.0M |
| HCA | 511.38 (10:04 iex) | +2.5% | 499.05 | 505.47 / 505.47-516.35 | 19.05 (3.8%) | 439.83-521.48 | +3.9% / +10.2% | +0.8% | 1.4M |
| SBUX | 108.94 (10:05 iex) | +2.3% | 106.44 | 107.73 / 107.69-109.47 | 3.10 (2.9%) | 96.09-110.85 | +2.4% / +7.8% | +1.6% | 8.0M |
| SNDK | 815.28 (10:05 iex) | -7.9% | 885.01 | 828.23 / 799.00-838.48 | 113.94 (12.9%) | 803.97-1,424.48 | -21.3% / -38.6% | +6.0% | 12.0M |
| MRVL | 145.02 (10:05 iex) | -7.5% | 156.76 | 148.11 / 144.09-148.96 | 18.49 (11.8%) | 132.54-253.66 | -19.5% / -31.6% | +11.0% | 30.2M |
| MPWR | 1,287.93 (10:05 iex) | -7.4% | 1,390.54 | 1,319.69 / 1,286.58-1,329.40 | 102.15 (7.3%) | 1,125.00-1,513.49 | +9.9% / +8.3% | +16.8% | 1.1M |
| MU | 722.75 (10:05 iex) | -7.1% | 778.31 | 734.58 / 718.54-739.12 | 64.86 (8.3%) | 650.00-990.00 | -7.1% / -17.5% | +12.8% | 30.7M |
| TER | 232.25 (10:05 iex) | -6.9% | 249.55 | 237.61 / 229.70-238.85 | 24.21 (9.7%) | 211.63-351.95 | -11.4% / -27.2% | +14.4% | 4.5M |
| ENTG | 137.33 (10:04 iex) | -6.8% | 147.41 | 140.32 / 135.43-140.70 | 12.67 (8.6%) | 124.14-170.06 | +1.8% / -0.1% | +15.2% | 3.8M |
| MSTR | 104.08 (10:05 iex) | -6.8% | 111.62 | 103.73 / 103.28-105.79 | 8.46 (7.6%) | 108.25-155.69 | -16.8% / -22.1% | -13.4% | 17.3M |
| ARM | 177.69 (10:04 iex) | -6.7% | 190.53 | 180.51 / 176.78-181.83 | 16.08 (8.4%) | 163.13-237.88 | -7.3% / -23.2% | +9.1% | 5.8M |
