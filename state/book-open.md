## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Thursday 2026-11-19. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$103,111.28**
- Cash: $140,670.03
- Session P&L so far: +0.13% (new entries are blocked at -3.0%)
- Gross exposure: $37,559 (36% of equity, cap 150%)
- Net exposure: $-37,559 (-36%, cap +/-100%)
- Risk at stake (entry to stop): $1,082 (1.05% of equity, cap 4.0%) — 2.95% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 345.91 | 339.92 | +359 (+1.7%) | -20% | 355.50 | 330.00 |
| HD | short | 51 | 343.57 | 336.54 | +359 (+2.0%) | -17% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **GLD**, opened 2026-11-18 (session 2 of at most 10), submitted with stop 359 and target 333, P 36%. Thesis: Gold is trending down on rising real rates and the strongest dollar in 18 months (-4.6% in 5 days, below its 20d and 50d averages). A US-session break below the overnight low (GLD 350.50, under its 352.91 20-day low) confirms the move toward the $3,800 and then ~$3,650 area. The stop entry stays unfilled if Warsh or the minutes turn dovish. Invalidation: DXY back below 102.50 with market-implied December-hike odds below 70%.
- **HD**, opened 2026-11-17 (session 3 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Your record

51 closed trades: 16W / 35L, total +0.37R, net $+2,410 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 51 | 18 | 30 | +0.01R |
| The same trades, bracket left alone | 51 | | | +0.03R |
| Ideas you passed on, or the caps dropped | 105 | 37 | 58 | +0.02R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 41 | 49% |
| 35%-40% | 70 | 29% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 38% of 143 brackets reached target first. Your Brier score is 0.239; saying 38% every time scores 0.237. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GLD | 339.90 (10:04 iex) | -0.4% | 341.19 | 339.88 / 339.20-340.52 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| HD | 335.67 (10:03 iex) | -0.6% | 337.64 | 335.00 / 332.34-336.38 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 737.23 (10:05 iex) | +1.0% | 730.20 | 737.46 / 735.42-739.90 | 14.32 (2.0%) | 726.79-775.64 | -3.1% / -4.2% | -3.9% | 51.4M |
| QQQ | 673.12 (10:05 iex) | +2.1% | 659.51 | 671.09 / 670.13-675.20 | 19.71 (3.0%) | 646.64-726.14 | -3.9% / -7.7% | -4.5% | 51.8M |
| IWM | 269.82 (10:04 iex) | -0.1% | 270.12 | 271.07 / 269.12-271.80 | 5.84 (2.2%) | 267.87-286.17 | -2.8% / -3.3% | -4.6% | 24.2M |
| DIA | 502.08 (10:05 iex) | +0.1% | 501.73 | 503.95 / 501.17-504.43 | 8.81 (1.8%) | 500.03-536.60 | -3.5% / -3.1% | -4.3% | 3.8M |
| TLT | 79.90 (10:04 iex) | -0.4% | 80.22 | 80.08 / 79.86-80.10 | 0.73 (0.9%) | 79.11-82.42 | -0.9% / +0.6% | -0.9% | 36.4M |
| GLD | 339.90 (10:04 iex) | -0.4% | 341.19 | 339.88 / 339.20-340.52 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| USO | 138.86 (10:03 iex) | +2.0% | 136.11 | 138.96 / 138.73-139.45 | 5.75 (4.2%) | 135.01-171.82 | -10.9% / -10.7% | -3.8% | 5.1M |
| SMH | 478.16 (10:04 iex) | +4.1% | 459.54 | 472.70 / 471.32-479.96 | 28.70 (6.2%) | 445.32-571.00 | -8.9% / -16.9% | -9.4% | 12.1M |
| XLK | 168.83 (10:04 iex) | +3.1% | 163.81 | 167.47 / 167.18-169.30 | 6.73 (4.1%) | 159.63-191.55 | -6.5% / -11.8% | -6.1% | 13.3M |
| XLF | 56.37 (10:04 iex) | -0.1% | 56.42 | 56.51 / 56.28-56.63 | 1.06 (1.9%) | 55.74-60.04 | -1.5% / +0.9% | -3.8% | 35.6M |
| XLE | 61.29 (10:04 iex) | +0.0% | 61.29 | 61.71 / 61.26-61.94 | 1.81 (3.0%) | 60.43-70.15 | -6.3% / -5.4% | -3.3% | 37.1M |
| XLV | 178.97 (10:05 iex) | -1.2% | 181.17 | 180.40 / 178.58-181.25 | 3.73 (2.1%) | 177.07-192.32 | -1.9% / +3.0% | -4.1% | 12.0M |
| XLI | 164.82 (10:04 iex) | +0.1% | 164.66 | 165.76 / 164.37-166.00 | 3.56 (2.2%) | 161.74-172.40 | -1.7% / -2.2% | -3.7% | 8.9M |
| XLY | 118.97 (10:04 iex) | -0.2% | 119.20 | 119.59 / 118.74-119.71 | 2.79 (2.3%) | 112.83-122.92 | +1.2% / +4.5% | -1.5% | 9.2M |
| XLP | 89.50 (10:05 iex) | -1.8% | 91.18 | 90.03 / 89.33-90.15 | 1.67 (1.8%) | 86.36-93.48 | +1.1% / +6.0% | -0.3% | 20.0M |
| XLU | 43.13 (10:05 iex) | -1.0% | 43.55 | 43.33 / 43.04-43.44 | 0.60 (1.4%) | 42.01-44.40 | +0.4% / +4.0% | -0.6% | 23.9M |
| XLB | 50.12 (10:04 iex) | -0.7% | 50.46 | 50.29 / 49.87-50.35 | 1.09 (2.2%) | 50.12-54.63 | -3.3% / -0.7% | -4.8% | 12.2M |
| XLRE | 43.28 (10:04 iex) | -0.8% | 43.62 | 43.52 / 43.23-43.52 | 0.66 (1.5%) | 41.78-45.34 | -0.1% / +2.5% | -2.2% | 7.9M |
| XLC | 105.98 (10:05 iex) | +0.4% | 105.58 | 106.72 / 105.76-107.11 | 2.21 (2.1%) | 99.33-109.26 | +0.6% / -3.1% | -2.8% | 7.9M |
| KRE | 70.40 (10:04 iex) | -0.2% | 70.52 | 70.60 / 70.25-70.86 | 1.54 (2.2%) | 70.19-75.80 | -2.8% / -1.3% | -3.3% | 14.5M |
| XHB | 99.71 (10:03 iex) | -1.0% | 100.75 | 100.44 / 99.18-100.48 | 3.28 (3.3%) | 94.86-108.78 | -0.8% / +2.4% | -2.3% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 349.69 (10:05 iex) | -0.8% | 352.45 | 353.01 / 348.50-355.28 | 9.43 (2.7%) | 325.08-360.83 | +1.4% / +3.4% | -0.8% | 48.2M |
| MSFT | 523.22 (10:05 iex) | +3.1% | 507.31 | 519.50 / 518.30-526.49 | 17.88 (3.5%) | 495.55-558.07 | -3.4% / -2.2% | -2.5% | 28.2M |
| NVDA | 156.16 (10:05 iex) | +3.4% | 150.96 | 152.91 / 152.54-158.13 | 11.92 (7.9%) | 148.80-219.99 | -20.1% / -28.2% | -13.1% | 250.9M |
| AMZN | 271.44 (10:05 iex) | +1.4% | 267.74 | 272.57 / 270.77-274.00 | 11.00 (4.1%) | 229.36-275.34 | +4.1% / +4.9% | +0.6% | 50.4M |
| GOOGL | 293.81 (10:04 iex) | +4.0% | 282.44 | 294.30 / 289.74-295.43 | 9.50 (3.4%) | 276.92-331.43 | -4.2% / -13.1% | -3.8% | 42.4M |
| META | 626.34 (10:04 iex) | +1.6% | 616.38 | 624.60 / 621.67-630.06 | 20.75 (3.4%) | 583.80-681.07 | -1.4% / -9.3% | -2.0% | 22.4M |
| TSLA | 386.68 (10:05 iex) | +0.8% | 383.72 | 389.90 / 385.38-393.60 | 17.96 (4.7%) | 338.15-414.23 | -0.6% / +2.1% | -1.8% | 37.7M |
| AVGO | 366.31 (10:05 iex) | +3.5% | 354.05 | 362.99 / 361.65-369.26 | 20.97 (5.9%) | 289.77-369.82 | +6.6% / +2.9% | +2.6% | 28.3M |
| AMD | 545.08 (10:04 iex) | +2.8% | 530.14 | 542.17 / 537.09-554.99 | 50.16 (9.5%) | 402.10-594.00 | +3.0% / -4.5% | -4.1% | 37.5M |
| ORCL | 117.17 (10:04 iex) | +2.9% | 113.89 | 116.67 / 116.01-118.50 | 8.36 (7.3%) | 109.21-148.48 | -8.5% / -14.8% | -11.3% | 41.2M |
| NFLX | 60.10 (10:05 iex) | +0.5% | 59.82 | 60.03 / 59.88-60.45 | 1.85 (3.1%) | 59.41-67.82 | -5.3% / -12.2% | -7.3% | 40.6M |
| CRM | 193.08 (10:04 iex) | +1.4% | 190.40 | 191.63 / 191.35-195.39 | 8.49 (4.5%) | 186.45-252.42 | -15.1% / -18.0% | -12.7% | 7.2M |
| JPM | 326.27 (10:05 iex) | +0.7% | 324.11 | 326.38 / 325.87-328.27 | 8.50 (2.6%) | 323.71-359.80 | -4.2% / -4.2% | -5.6% | 6.6M |
| GS | 885.58 (10:03 iex) | +1.4% | 873.18 | 885.55 / 879.98-891.25 | 30.40 (3.5%) | 854.45-939.38 | -2.9% / -4.3% | -5.8% | 2.1M |
| BAC | 49.10 (10:05 iex) | +0.4% | 48.91 | 49.31 / 48.95-49.37 | 1.23 (2.5%) | 48.74-53.02 | -2.8% / -8.2% | -3.5% | 34.4M |
| XOM | 159.92 (10:05 iex) | -0.4% | 160.58 | 161.32 / 159.95-162.07 | 4.86 (3.0%) | 159.11-187.32 | -6.9% / -4.7% | -3.1% | 14.6M |
| CVX | 206.25 (10:05 iex) | +0.2% | 205.88 | 207.48 / 206.21-208.11 | 5.58 (2.7%) | 204.31-234.53 | -6.2% / -3.7% | -2.7% | 8.3M |
| LLY | 1,364.74 (10:05 iex) | -1.3% | 1,382.75 | 1,369.38 / 1,361.97-1,382.00 | 46.44 (3.4%) | 1,256.10-1,475.25 | +0.4% / +10.1% | -3.7% | 3.1M |
| UNH | 342.22 (10:04 iex) | -2.2% | 349.91 | 351.13 / 340.19-353.85 | 14.59 (4.2%) | 342.45-426.55 | -13.2% / -10.4% | -13.2% | 5.6M |
| JNJ | 266.41 (10:05 iex) | -2.3% | 272.70 | 269.61 / 265.79-270.60 | 7.08 (2.6%) | 259.04-290.25 | -0.7% / +2.0% | -2.7% | 7.6M |
| WMT | 125.61 (10:05 iex) | -1.4% | 127.36 | 123.68 / 123.27-125.67 | 3.09 (2.4%) | 117.83-131.82 | +2.2% / +10.0% | +1.3% | 22.3M |
| COST | 1,087.95 (10:04 iex) | -0.8% | 1,096.62 | 1,089.56 / 1,086.24-1,094.56 | 21.91 (2.0%) | 978.87-1,123.67 | +4.6% / +12.1% | +0.8% | 2.5M |
| HD | 335.67 (10:03 iex) | -0.6% | 337.64 | 335.00 / 332.34-336.38 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |
| CAT | 563.81 (10:04 iex) | +0.9% | 558.77 | 567.94 / 559.03-569.77 | 27.74 (5.0%) | 550.81-732.73 | -9.9% / -22.9% | -7.1% | 4.0M |
| BA | 163.73 (10:03 iex) | +0.5% | 162.91 | 163.80 / 163.11-164.22 | 4.74 (2.9%) | 161.75-193.19 | -6.1% / -12.4% | -6.7% | 10.5M |
| DAL | 84.78 (10:04 iex) | -0.1% | 84.88 | 85.08 / 83.30-85.30 | 3.24 (3.8%) | 75.33-92.52 | +0.4% / +3.3% | -7.1% | 6.0M |
| UAL | 107.30 (10:04 iex) | -0.3% | 107.63 | 107.41 / 105.09-107.55 | 5.50 (5.1%) | 96.39-122.08 | -1.2% / -0.4% | -9.1% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| PDD | 86.82 (10:05 iex) | +12.1% | 77.45 | 82.44 / 82.02-87.38 | 2.57 (3.3%) | 76.27-85.42 | -2.5% / -2.3% | -2.0% | 5.8M |
| ZS | 217.06 (10:05 iex) | +9.7% | 197.83 | 202.01 / 201.46-218.10 | 12.34 (6.2%) | 180.47-267.87 | -9.6% / -6.2% | +2.1% | 2.4M |
| STX | 565.19 (10:05 iex) | +9.6% | 515.90 | 546.90 / 536.54-565.38 | 49.84 (9.7%) | 449.28-718.65 | -10.0% / -28.2% | -6.5% | 6.0M |
| OKTA | 213.90 (10:04 iex) | +9.4% | 195.61 | 203.25 / 202.00-214.33 | 14.91 (7.6%) | 164.18-228.72 | +1.1% / -1.6% | +7.3% | 4.9M |
| WDC | 315.03 (10:05 iex) | +9.3% | 288.19 | 306.17 / 300.82-315.74 | 27.33 (9.5%) | 258.61-402.23 | -11.1% / -24.2% | -8.0% | 8.4M |
| INTC | 59.36 (10:05 iex) | +8.6% | 54.67 | 57.54 / 57.28-59.32 | 6.11 (11.2%) | 51.51-95.68 | -19.8% / -40.7% | -12.5% | 147.0M |
| DDOG | 181.29 (10:04 iex) | +8.5% | 167.11 | 174.80 / 173.66-182.39 | 14.90 (8.9%) | 162.11-285.00 | -21.6% / -30.6% | -9.4% | 4.8M |
| SNDK | 833.60 (10:05 iex) | +7.4% | 776.22 | 811.47 / 804.01-846.76 | 111.84 (14.4%) | 749.39-1,408.45 | -25.2% / -43.9% | -20.6% | 12.9M |
| ZTS | 82.21 (10:04 iex) | -3.9% | 85.57 | 84.84 / 82.18-85.13 | 3.19 (3.7%) | 76.51-89.29 | +4.4% / +11.8% | +3.6% | 4.6M |
| MO | 73.59 (10:05 iex) | -3.5% | 76.26 | 75.30 / 73.54-75.45 | 1.71 (2.2%) | 72.30-79.97 | -0.3% / +4.9% | -1.5% | 8.3M |
| PM | 186.18 (10:04 iex) | -3.4% | 192.73 | 190.26 / 186.07-191.54 | 5.29 (2.7%) | 191.07-214.35 | -4.0% / -1.9% | -1.8% | 4.9M |
| KO | 94.91 (10:05 iex) | -3.2% | 98.09 | 96.21 / 94.73-96.68 | 1.81 (1.8%) | 90.58-100.56 | +2.6% / +7.3% | +0.5% | 18.7M |
| W | 106.00 (10:05 iex) | -3.1% | 109.35 | 107.85 / 105.68-108.68 | 7.07 (6.5%) | 105.17-127.99 | -3.7% / +1.3% | -4.4% | 2.1M |
| NKE | 35.23 (10:05 iex) | -3.0% | 36.31 | 35.75 / 35.11-36.00 | 1.62 (4.5%) | 34.96-41.10 | -5.0% / -1.4% | -5.2% | 24.0M |
| HSY | 170.78 (10:03 iex) | -2.9% | 175.94 | 173.01 / 170.78-174.39 | 5.59 (3.2%) | 158.55-178.42 | +3.2% / +5.3% | +0.6% | 2.0M |
| STZ | 139.48 (10:03 iex) | -2.9% | 143.62 | 141.53 / 139.48-141.55 | 4.45 (3.1%) | 128.06-149.43 | +2.5% / +12.0% | -0.3% | 2.3M |
