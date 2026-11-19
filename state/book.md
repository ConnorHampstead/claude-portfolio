## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Thursday 2026-11-19. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,247.85**
- Cash: $140,670.03
- Session P&L so far: +0.26% (new entries are blocked at -3.0%)
- Gross exposure: $37,422 (36% of equity, cap 150%)
- Net exposure: $-37,422 (-36%, cap +/-100%)
- Risk at stake (entry to stop): $1,082 (1.05% of equity, cap 4.0%) — 2.95% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 345.91 | 340.16 | +345 (+1.7%) | -20% | 355.50 | 330.00 |
| HD | short | 51 | 343.57 | 333.58 | +509 (+2.9%) | -16% | 353.50 | 323.50 |

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

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| GLD | 340.37 (08:49 sip) | -0.2% | 341.19 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| HD | 333.58 (08:49 sip) | -1.2% | 337.64 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 737.72 (08:58 iex) | +1.0% | 730.20 | 14.32 (2.0%) | 726.79-775.64 | -3.1% / -4.2% | -3.9% | 51.4M |
| QQQ | 671.70 (09:02 iex) | +1.8% | 659.51 | 19.71 (3.0%) | 646.64-726.14 | -3.9% / -7.7% | -4.5% | 51.8M |
| IWM | 271.40 (08:49 sip) | +0.5% | 270.12 | 5.84 (2.2%) | 267.87-286.17 | -2.8% / -3.3% | -4.6% | 24.2M |
| DIA | 504.23 (08:49 sip) | +0.5% | 501.73 | 8.81 (1.8%) | 500.03-536.60 | -3.5% / -3.1% | -4.3% | 3.8M |
| TLT | 80.11 (08:49 sip) | -0.1% | 80.22 | 0.73 (0.9%) | 79.11-82.42 | -0.9% / +0.6% | -0.9% | 36.4M |
| GLD | 340.37 (08:49 sip) | -0.2% | 341.19 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| USO | 138.71 (08:49 sip) | +1.9% | 136.11 | 5.75 (4.2%) | 135.01-171.82 | -10.9% / -10.7% | -3.8% | 5.1M |
| SMH | 471.16 (08:49 sip) | +2.5% | 459.54 | 28.70 (6.2%) | 445.32-571.00 | -8.9% / -16.9% | -9.4% | 12.1M |
| XLK | 167.11 (08:49 sip) | +2.0% | 163.81 | 6.73 (4.1%) | 159.63-191.55 | -6.5% / -11.8% | -6.1% | 13.3M |
| XLF | 56.53 (08:45 sip) | +0.2% | 56.42 | 1.06 (1.9%) | 55.74-60.04 | -1.5% / +0.9% | -3.8% | 35.6M |
| XLE | 61.60 (08:49 sip) | +0.5% | 61.29 | 1.81 (3.0%) | 60.43-70.15 | -6.3% / -5.4% | -3.3% | 37.1M |
| XLV | 180.57 (08:49 sip) | -0.3% | 181.17 | 3.73 (2.1%) | 177.07-192.32 | -1.9% / +3.0% | -4.1% | 12.0M |
| XLI | 165.65 (08:49 sip) | +0.6% | 164.66 | 3.56 (2.2%) | 161.74-172.40 | -1.7% / -2.2% | -3.7% | 8.9M |
| XLY | 119.77 (08:49 sip) | +0.5% | 119.20 | 2.79 (2.3%) | 112.83-122.92 | +1.2% / +4.5% | -1.5% | 9.2M |
| XLP | 90.43 (08:49 sip) | -0.8% | 91.18 | 1.67 (1.8%) | 86.36-93.48 | +1.1% / +6.0% | -0.3% | 20.0M |
| XLU | 43.50 (08:49 sip) | -0.1% | 43.55 | 0.60 (1.4%) | 42.01-44.40 | +0.4% / +4.0% | -0.6% | 23.9M |
| XLB | 50.41 (08:45 sip) | -0.1% | 50.46 | 1.09 (2.2%) | 50.12-54.63 | -3.3% / -0.7% | -4.8% | 12.2M |
| XLRE | 43.69 (08:40 sip) | +0.2% | 43.62 | 0.66 (1.5%) | 41.78-45.34 | -0.1% / +2.5% | -2.2% | 7.9M |
| XLC | 106.56 (08:49 sip) | +0.9% | 105.58 | 2.21 (2.1%) | 99.33-109.26 | +0.6% / -3.1% | -2.8% | 7.9M |
| KRE | 70.80 (08:10 sip) | +0.4% | 70.52 | 1.54 (2.2%) | 70.19-75.80 | -2.8% / -1.3% | -3.3% | 14.5M |
| XHB | 100.80 (08:20 sip) | +0.0% | 100.75 | 3.28 (3.3%) | 94.86-108.78 | -0.8% / +2.4% | -2.3% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 353.56 (08:49 sip) | +0.3% | 352.45 | 9.43 (2.7%) | 325.08-360.83 | +1.4% / +3.4% | -0.8% | 48.2M |
| MSFT | 515.07 (08:49 sip) | +1.5% | 507.31 | 17.88 (3.5%) | 495.55-558.07 | -3.4% / -2.2% | -2.5% | 28.2M |
| NVDA | 152.98 (09:05 iex) | +1.3% | 150.96 | 11.92 (7.9%) | 148.80-219.99 | -20.1% / -28.2% | -13.1% | 250.9M |
| AMZN | 272.19 (08:54 iex) | +1.7% | 267.74 | 11.00 (4.1%) | 229.36-275.34 | +4.1% / +4.9% | +0.6% | 50.4M |
| GOOGL | 293.88 (09:02 iex) | +4.1% | 282.44 | 9.50 (3.4%) | 276.92-331.43 | -4.2% / -13.1% | -3.8% | 42.4M |
| META | 623.00 (08:49 sip) | +1.1% | 616.38 | 20.75 (3.4%) | 583.80-681.07 | -1.4% / -9.3% | -2.0% | 22.4M |
| TSLA | 391.92 (09:02 iex) | +2.1% | 383.72 | 17.96 (4.7%) | 338.15-414.23 | -0.6% / +2.1% | -1.8% | 37.7M |
| AVGO | 361.80 (08:49 sip) | +2.2% | 354.05 | 20.97 (5.9%) | 289.77-369.82 | +6.6% / +2.9% | +2.6% | 28.3M |
| AMD | 536.98 (08:49 sip) | +1.3% | 530.14 | 50.16 (9.5%) | 402.10-594.00 | +3.0% / -4.5% | -4.1% | 37.5M |
| ORCL | 117.29 (09:03 iex) | +3.0% | 113.89 | 8.36 (7.3%) | 109.21-148.48 | -8.5% / -14.8% | -11.3% | 41.2M |
| NFLX | 60.02 (09:03 iex) | +0.3% | 59.82 | 1.85 (3.1%) | 59.41-67.82 | -5.3% / -12.2% | -7.3% | 40.6M |
| CRM | 190.27 (08:49 sip) | -0.1% | 190.40 | 8.49 (4.5%) | 186.45-252.42 | -15.1% / -18.0% | -12.7% | 7.2M |
| JPM | 326.79 (08:45 sip) | +0.8% | 324.11 | 8.50 (2.6%) | 323.71-359.80 | -4.2% / -4.2% | -5.6% | 6.6M |
| GS | 888.00 (08:49 sip) | +1.7% | 873.18 | 30.40 (3.5%) | 854.45-939.38 | -2.9% / -4.3% | -5.8% | 2.1M |
| BAC | 49.28 (08:49 sip) | +0.8% | 48.91 | 1.23 (2.5%) | 48.74-53.02 | -2.8% / -8.2% | -3.5% | 34.4M |
| XOM | 160.82 (08:49 sip) | +0.1% | 160.58 | 4.86 (3.0%) | 159.11-187.32 | -6.9% / -4.7% | -3.1% | 14.6M |
| CVX | 206.05 (08:49 sip) | +0.1% | 205.88 | 5.58 (2.7%) | 204.31-234.53 | -6.2% / -3.7% | -2.7% | 8.3M |
| LLY | 1,371.80 (08:59 iex) | -0.8% | 1,382.75 | 46.44 (3.4%) | 1,256.10-1,475.25 | +0.4% / +10.1% | -3.7% | 3.1M |
| UNH | 350.79 (08:49 sip) | +0.3% | 349.91 | 14.59 (4.2%) | 342.45-426.55 | -13.2% / -10.4% | -13.2% | 5.6M |
| JNJ | 270.55 (08:49 sip) | -0.8% | 272.70 | 7.08 (2.6%) | 259.04-290.25 | -0.7% / +2.0% | -2.7% | 7.6M |
| WMT | 125.36 (08:49 sip) | -1.6% | 127.36 | 3.09 (2.4%) | 117.83-131.82 | +2.2% / +10.0% | +1.3% | 22.3M |
| COST | 1,092.86 (08:40 sip) | -0.3% | 1,096.62 | 21.91 (2.0%) | 978.87-1,123.67 | +4.6% / +12.1% | +0.8% | 2.5M |
| HD | 333.58 (08:49 sip) | -1.2% | 337.64 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |
| CAT | 568.08 (08:49 sip) | +1.7% | 558.77 | 27.74 (5.0%) | 550.81-732.73 | -9.9% / -22.9% | -7.1% | 4.0M |
| BA | 164.32 (08:49 sip) | +0.9% | 162.91 | 4.74 (2.9%) | 161.75-193.19 | -6.1% / -12.4% | -6.7% | 10.5M |
| DAL | 85.21 (08:45 sip) | +0.4% | 84.88 | 3.24 (3.8%) | 75.33-92.52 | +0.4% / +3.3% | -7.1% | 6.0M |
| UAL | 107.27 (08:45 sip) | -0.3% | 107.63 | 5.50 (5.1%) | 96.39-122.08 | -1.2% / -0.4% | -9.1% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| PANW | 369.00 (08:49 sip) | +8.6% | 339.92 | 20.20 (5.9%) | 301.28-406.88 | -2.2% / -7.3% | +1.6% | 6.9M |
| ENTG | 153.99 (08:40 sip) | +7.1% | 143.78 | 12.29 (8.5%) | 124.14-170.06 | -0.3% / -2.6% | -6.8% | 3.8M |
| PDD | 81.86 (08:49 sip) | +5.7% | 77.45 | 2.57 (3.3%) | 76.27-85.42 | -2.5% / -2.3% | -2.0% | 5.8M |
| STX | 545.00 (08:49 sip) | +5.6% | 515.90 | 49.84 (9.7%) | 449.28-718.65 | -10.0% / -28.2% | -6.5% | 6.0M |
| CRWD | 250.09 (08:49 sip) | +5.5% | 237.03 | 15.15 (6.4%) | 213.22-272.29 | -0.9% / -3.6% | +3.5% | 9.2M |
| SNDK | 813.59 (09:03 iex) | +4.8% | 776.22 | 111.84 (14.4%) | 749.39-1,408.45 | -25.2% / -43.9% | -20.6% | 12.9M |
| WDC | 301.96 (08:49 sip) | +4.8% | 288.19 | 27.33 (9.5%) | 258.61-402.23 | -11.1% / -24.2% | -8.0% | 8.4M |
| NET | 314.60 (08:49 sip) | +4.5% | 300.91 | 23.53 (7.8%) | 233.62-337.00 | +1.4% / -6.0% | -4.5% | 4.4M |
| TTWO | 210.00 (08:49 sip) | -3.1% | 216.61 | 13.02 (6.0%) | 183.86-237.41 | +3.9% / +4.3% | -6.4% | 4.3M |
| BABA | 82.71 (08:59 iex) | -2.0% | 84.37 | 4.04 (4.8%) | 84.22-111.17 | -15.0% / -20.0% | -16.9% | 11.7M |
| NEM | 102.67 (08:49 sip) | -1.8% | 104.53 | 5.50 (5.3%) | 102.35-127.28 | -7.9% / -10.6% | -11.8% | 7.3M |
| SPOT | 597.00 (08:30 sip) | -1.5% | 605.84 | 20.99 (3.5%) | 536.75-635.00 | +2.0% / +10.7% | -0.5% | 1.8M |
| BMY | 58.73 (08:49 sip) | -1.4% | 59.56 | 1.92 (3.2%) | 59.48-65.54 | -4.2% / -3.1% | -5.3% | 10.3M |
| W | 107.90 (08:20 sip) | -1.3% | 109.35 | 7.07 (6.5%) | 105.17-127.99 | -3.7% / +1.3% | -4.4% | 2.1M |
| HCA | 470.18 (07:10 sip) | -1.3% | 476.35 | 17.31 (3.6%) | 439.83-521.48 | -1.9% / +4.0% | -5.9% | 1.5M |
| MDLZ | 65.73 (08:49 sip) | -1.3% | 66.56 | 1.63 (2.4%) | 61.51-68.92 | +1.6% / +6.1% | -0.2% | 8.3M |
