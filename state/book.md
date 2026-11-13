## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Friday 2026-11-13. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,234.57**
- Cash: $113,476.11
- Session P&L so far: +0.03% (new entries are blocked at -3.0%)
- Gross exposure: $54,927 (54% of equity, cap 150%)
- Net exposure: $-29,990 (-29%, cap +/-100%)
- Risk at stake (entry to stop): $1,525 (1.49% of equity, cap 4.0%) — 2.51% left for new plays
- Slots: 3 open + 1 resting entries of 8 — you may add at most 4 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 269.62 | -108 (-1.6%) | +6% | 263.50 | 293.00 |
| DAL | long | 69 | 89.50 | 86.92 | -178 (-2.9%) | +6% | 85.80 | 96.50 |
| IWM | short | 85 | 281.03 | 278.94 | +177 (+0.7%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **AMZN**, opened 2026-11-09 (session 5 of at most 10), submitted with stop 263.5 and target 293, P 36%. Thesis: Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong relative signal. Invalidation: QQQ breaking its 20-day low while AMZN falls back inside the range.
- **DAL**, opened 2026-11-12 (session 2 of at most 10), submitted with stop 85.8 and target 96.5, P 37%. Thesis: Falling jet fuel is a direct margin tailwind. Buy the retest of the 89.92 20-day-high breakout rather than chase the gap. Invalidation: Brent back above $100.
- **IWM**, opened 2026-11-10 (session 4 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
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

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMZN | 269.74 (08:49 sip) | +0.9% | 267.44 | 10.56 (3.9%) | 229.36-275.34 | +4.3% / +5.0% | +2.8% | 50.6M |
| DAL | 87.00 (08:49 sip) | +0.5% | 86.55 | 3.34 (3.9%) | 74.14-92.52 | +4.7% / +6.0% | +1.4% | 6.6M |
| IWM | 279.24 (08:49 sip) | +0.3% | 278.44 | 5.36 (1.9%) | 269.88-286.17 | +0.2% / -0.9% | +2.8% | 24.2M |
| QQQ | 689.65 (09:04 iex) | +0.2% | 688.17 | 18.16 (2.6%) | 647.05-727.95 | -1.3% / -4.2% | +6.4% | 50.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 760.34 (09:01 iex) | +0.4% | 757.12 | 12.45 (1.6%) | 732.71-775.64 | -0.3% / -1.0% | +3.3% | 48.3M |
| QQQ | 689.65 (09:04 iex) | +0.2% | 688.17 | 18.16 (2.6%) | 647.05-727.95 | -1.3% / -4.2% | +6.4% | 50.9M |
| IWM | 279.24 (08:49 sip) | +0.3% | 278.44 | 5.36 (1.9%) | 269.88-286.17 | +0.2% / -0.9% | +2.8% | 24.2M |
| DIA | 524.73 (08:49 sip) | +0.4% | 522.47 | 7.54 (1.4%) | 508.66-536.60 | +0.1% / +0.6% | +1.6% | 3.8M |
| TLT | 79.43 (09:00 iex) | -0.4% | 79.72 | 0.76 (1.0%) | 79.01-82.42 | -1.5% / -0.2% | -2.7% | 36.3M |
| GLD | 355.71 (08:49 sip) | +0.2% | 354.89 | 7.66 (2.2%) | 352.91-384.88 | -4.1% / -7.1% | -5.5% | 9.2M |
| USO | 146.58 (08:49 sip) | +0.3% | 146.07 | 5.88 (4.0%) | 138.47-171.82 | -6.9% / -4.4% | -1.4% | 5.6M |
| SMH | 501.16 (08:53 iex) | -0.1% | 501.73 | 26.50 (5.3%) | 445.59-571.00 | -3.7% / -10.6% | +12.1% | 12.1M |
| XLK | 173.93 (08:49 sip) | +0.1% | 173.77 | 6.09 (3.5%) | 162.14-191.55 | -3.1% / -7.3% | +7.0% | 12.8M |
| XLF | 58.59 (08:49 sip) | +0.7% | 58.21 | 1.01 (1.7%) | 55.03-60.04 | +2.3% / +4.1% | +1.2% | 33.6M |
| XLE | 64.77 (08:49 sip) | +0.7% | 64.33 | 1.74 (2.7%) | 60.43-70.15 | -3.0% / -0.9% | +4.4% | 37.3M |
| XLV | 188.92 (08:49 sip) | +0.6% | 187.83 | 3.75 (2.0%) | 175.27-192.32 | +2.6% / +7.6% | +1.6% | 11.2M |
| XLI | 170.01 (06:45 sip) | +0.3% | 169.44 | 3.34 (2.0%) | 161.74-172.40 | +1.0% / +0.3% | +4.3% | 8.8M |
| XLY | 121.25 (08:40 sip) | +0.7% | 120.46 | 2.60 (2.2%) | 111.84-122.92 | +3.0% / +5.9% | +2.4% | 9.5M |
| XLP | 91.30 (08:49 sip) | +0.3% | 91.06 | 1.63 (1.8%) | 86.36-93.40 | +2.0% / +6.6% | -0.2% | 19.2M |
| XLU | 44.05 (08:49 sip) | +0.5% | 43.81 | 0.60 (1.4%) | 41.28-44.14 | +1.9% / +4.8% | +1.2% | 25.9M |
| XLB | 52.96 (08:49 sip) | +1.2% | 52.34 | 1.01 (1.9%) | 50.61-54.63 | +0.3% / +2.9% | +0.0% | 12.1M |
| XLRE | 44.40 (08:45 sip) | +0.1% | 44.36 | 0.70 (1.6%) | 41.60-45.34 | +2.5% / +4.3% | +0.1% | 8.1M |
| XLC | 108.50 (08:35 sip) | +0.9% | 107.56 | 2.18 (2.0%) | 99.33-112.90 | +1.9% / -1.7% | +3.1% | 7.9M |
| KRE | 73.00 (08:40 sip) | +0.7% | 72.52 | 1.54 (2.1%) | 69.17-75.80 | +0.4% / +1.2% | +0.3% | 14.3M |
| XHB | 100.95 (07:55 sip) | -0.4% | 101.32 | 3.26 (3.2%) | 94.05-108.78 | +0.8% / +3.0% | -2.4% | 2.5M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 356.43 (09:01 iex) | +0.4% | 354.88 | 9.50 (2.7%) | 325.08-359.37 | +2.8% / +4.9% | +3.2% | 48.4M |
| MSFT | 518.31 (08:49 sip) | -0.9% | 523.00 | 17.48 (3.3%) | 504.96-559.15 | -1.3% / +0.8% | -2.4% | 26.4M |
| NVDA | 169.99 (09:05 iex) | +2.3% | 166.19 | 10.66 (6.4%) | 148.80-222.19 | -17.4% / -23.0% | -8.5% | 197.4M |
| AMZN | 269.74 (08:49 sip) | +0.9% | 267.44 | 10.56 (3.9%) | 229.36-275.34 | +4.3% / +5.0% | +2.8% | 50.6M |
| GOOGL | 302.86 (09:00 iex) | +1.4% | 298.70 | 11.43 (3.8%) | 276.92-350.66 | -2.3% / -9.2% | +5.7% | 40.9M |
| META | 626.04 (08:49 sip) | +0.4% | 623.61 | 20.93 (3.4%) | 583.80-738.49 | -2.6% / -8.2% | +3.1% | 24.1M |
| TSLA | 401.95 (08:52 iex) | +1.1% | 397.45 | 18.63 (4.7%) | 338.15-414.23 | +3.6% / +6.1% | +15.6% | 41.2M |
| AVGO | 356.26 (08:49 sip) | -2.2% | 364.36 | 19.09 (5.2%) | 289.77-369.82 | +10.4% / +5.5% | +25.0% | 26.8M |
| AMD | 570.98 (09:01 iex) | -2.4% | 585.30 | 44.61 (7.6%) | 402.10-594.00 | +12.8% / +5.8% | +44.7% | 33.4M |
| ORCL | 128.60 (08:49 sip) | +1.2% | 127.11 | 9.31 (7.3%) | 109.21-148.48 | +0.3% / -7.2% | +10.4% | 42.6M |
| NFLX | 63.02 (08:49 sip) | +0.5% | 62.69 | 1.83 (2.9%) | 61.39-71.90 | -3.2% / -9.9% | -4.4% | 46.2M |
| CRM | 219.47 (08:25 sip) | +0.9% | 217.57 | 8.50 (3.9%) | 208.88-252.42 | -6.1% / -7.9% | -2.2% | 7.0M |
| JPM | 346.00 (08:49 sip) | +0.9% | 342.82 | 7.84 (2.3%) | 330.40-359.80 | +1.2% / +0.8% | +1.6% | 6.6M |
| GS | 922.71 (08:49 sip) | +1.0% | 913.60 | 29.31 (3.2%) | 854.45-939.38 | +1.6% / -1.2% | +5.1% | 2.1M |
| BAC | 50.84 (08:49 sip) | +0.6% | 50.51 | 1.20 (2.4%) | 49.17-53.02 | -0.0% / -7.0% | +1.5% | 37.4M |
| XOM | 171.22 (08:49 sip) | +0.8% | 169.78 | 4.82 (2.8%) | 160.11-188.50 | -3.4% / +0.3% | +2.7% | 14.3M |
| CVX | 218.00 (08:49 sip) | +0.8% | 216.35 | 5.30 (2.4%) | 206.01-236.48 | -3.1% / +0.5% | +1.6% | 8.4M |
| LLY | 1,432.58 (08:49 sip) | +0.5% | 1,425.55 | 50.51 (3.5%) | 1,237.60-1,458.23 | +6.0% / +15.5% | +4.6% | 3.0M |
| UNH | 408.13 (08:45 sip) | +0.7% | 405.13 | 11.13 (2.7%) | 388.00-426.55 | -0.6% / +3.6% | +2.4% | 5.2M |
| JNJ | 284.31 (08:49 sip) | +0.3% | 283.52 | 7.28 (2.6%) | 251.50-286.08 | +5.0% / +6.3% | +4.1% | 7.5M |
| WMT | 126.77 (08:49 sip) | +0.5% | 126.19 | 3.03 (2.4%) | 116.63-131.82 | +2.8% / +10.6% | -1.2% | 22.0M |
| COST | 1,093.00 (08:45 sip) | +0.1% | 1,092.21 | 21.59 (2.0%) | 978.87-1,102.84 | +6.5% / +13.5% | +2.5% | 2.4M |
| HD | 345.75 (08:45 sip) | -0.7% | 348.26 | 9.89 (2.8%) | 306.00-362.44 | +4.9% / +11.8% | -0.5% | 4.5M |
| CAT | 611.02 (08:49 sip) | +0.9% | 605.28 | 31.33 (5.2%) | 550.81-743.23 | -7.0% / -18.6% | +9.3% | 3.9M |
| BA | 172.01 (08:49 sip) | +0.3% | 171.55 | 6.20 (3.6%) | 165.01-193.28 | -3.9% / -9.5% | -0.6% | 10.6M |
| DAL | 87.00 (08:49 sip) | +0.5% | 86.55 | 3.34 (3.9%) | 74.14-92.52 | +4.7% / +6.0% | +1.4% | 6.6M |
| UAL | 112.52 (08:49 sip) | +1.1% | 111.25 | 5.46 (4.9%) | 94.54-122.08 | +4.2% / +2.9% | +0.7% | 5.7M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| NU | 12.37 (08:49 sip) | +4.6% | 11.83 | 0.70 (5.9%) | 11.21-15.41 | -8.0% / -14.3% | +0.8% | 84.9M |
| TRV | 418.00 (07:50 sip) | +3.7% | 403.18 | 8.96 (2.2%) | 368.63-418.00 | +1.3% / +6.0% | +0.1% | 1.7M |
| PANW | 332.00 (08:49 sip) | +2.9% | 322.66 | 19.93 (6.2%) | 312.12-406.88 | -8.3% / -12.2% | +2.5% | 6.3M |
| OKTA | 187.50 (08:49 sip) | +2.7% | 182.54 | 14.26 (7.8%) | 164.18-228.72 | -6.8% / -7.7% | +6.6% | 5.1M |
| ZS | 198.38 (08:40 sip) | +2.7% | 193.22 | 12.93 (6.7%) | 184.63-267.87 | -13.7% / -7.6% | -5.2% | 2.4M |
| CRWD | 235.65 (08:49 sip) | +2.5% | 229.87 | 14.38 (6.3%) | 213.22-272.29 | -4.2% / -6.1% | +5.8% | 9.5M |
| HUM | 454.00 (08:00 sip) | +2.3% | 443.68 | 17.33 (3.9%) | 399.35-451.00 | +5.2% / +9.0% | +7.7% | 1.6M |
| PWR | 620.02 (08:35 sip) | +2.3% | 606.16 | 39.77 (6.6%) | 502.04-657.14 | +2.3% / -3.5% | +19.1% | 1.8M |
| CSCO | 98.88 (08:59 iex) | -3.1% | 102.01 | 4.01 (3.9%) | 93.35-112.69 | -2.0% / -5.4% | +6.6% | 19.6M |
| COIN | 128.10 (08:49 sip) | -2.0% | 130.67 | 9.71 (7.4%) | 129.41-183.40 | -14.4% / -23.9% | -4.5% | 8.4M |
| LOW | 223.25 (08:30 sip) | -1.9% | 227.46 | 7.00 (3.1%) | 193.43-235.00 | +7.4% / +14.6% | +0.1% | 3.4M |
| BIDU | 76.40 (08:49 sip) | -1.6% | 77.63 | 2.53 (3.3%) | 75.80-82.77 | -1.7% / -8.3% | -2.3% | 2.3M |
| BABA | 92.90 (08:49 sip) | -1.5% | 94.36 | 3.60 (3.8%) | 93.42-112.17 | -8.4% / -12.0% | -12.7% | 10.3M |
| SNDK | 926.56 (09:03 iex) | -1.2% | 937.46 | 111.64 (11.9%) | 803.97-1,424.48 | -18.1% / -35.6% | +16.2% | 11.8M |
| HOOD | 80.45 (08:49 sip) | -1.1% | 81.35 | 4.98 (6.1%) | 75.51-104.40 | -9.1% / -21.9% | +3.8% | 19.2M |
| TJX | 134.57 (08:45 sip) | -1.0% | 135.98 | 3.84 (2.8%) | 134.22-148.05 | -3.5% / +0.3% | -1.5% | 5.8M |
