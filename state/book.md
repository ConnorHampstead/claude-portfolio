## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Tuesday 2026-11-17. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,669.02**
- Cash: $125,772.02
- Session P&L so far: +0.09% (new entries are blocked at -3.0%)
- Gross exposure: $44,133 (43% of equity, cap 150%)
- Net exposure: $-44,133 (-43%, cap +/-100%)
- Risk at stake (entry to stop): $1,018 (0.99% of equity, cap 4.0%) — 3.01% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| IWM | short | 85 | 281.03 | 271.80 | +784 (+3.3%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **IWM**, opened 2026-11-10 (session 6 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.

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

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IWM | 271.60 (08:49 sip) | -0.5% | 272.94 | 5.61 (2.1%) | 270.23-286.17 | -2.0% / -2.6% | -3.4% | 23.7M |
| GLD | 352.48 (08:49 sip) | -0.1% | 352.93 | 7.57 (2.1%) | 351.96-380.88 | -4.0% / -7.1% | -7.0% | 9.6M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 738.80 (08:51 iex) | -0.2% | 739.95 | 13.51 (1.8%) | 732.71-775.64 | -2.3% / -3.1% | -1.7% | 48.5M |
| QQQ | 663.31 (08:49 sip) | +0.2% | 661.75 | 19.23 (2.9%) | 647.05-727.95 | -4.5% / -7.7% | -2.6% | 49.9M |
| IWM | 271.60 (08:49 sip) | -0.5% | 272.94 | 5.61 (2.1%) | 270.23-286.17 | -2.0% / -2.6% | -3.4% | 23.7M |
| DIA | 511.61 (08:49 sip) | -0.8% | 515.68 | 8.04 (1.6%) | 508.66-536.60 | -1.2% / -0.6% | -1.5% | 3.7M |
| TLT | 79.33 (08:49 sip) | -0.1% | 79.38 | 0.78 (1.0%) | 79.11-82.42 | -1.9% / -0.5% | -3.1% | 35.8M |
| GLD | 352.48 (08:49 sip) | -0.1% | 352.93 | 7.57 (2.1%) | 351.96-380.88 | -4.0% / -7.1% | -7.0% | 9.6M |
| USO | 142.00 (08:49 sip) | +1.4% | 140.03 | 5.90 (4.2%) | 138.36-171.82 | -9.7% / -8.3% | -1.8% | 5.4M |
| SMH | 466.65 (08:49 sip) | +1.0% | 461.90 | 27.80 (6.0%) | 445.59-571.00 | -10.1% / -17.2% | -5.2% | 11.9M |
| XLK | 165.50 (08:49 sip) | +0.4% | 164.76 | 6.43 (3.9%) | 162.14-191.55 | -7.2% / -11.7% | -3.6% | 12.7M |
| XLF | 57.79 (08:49 sip) | -0.7% | 58.18 | 1.04 (1.8%) | 55.17-60.04 | +1.7% / +4.0% | +0.3% | 33.4M |
| XLE | 64.00 (08:49 sip) | +0.5% | 63.69 | 1.70 (2.7%) | 60.43-70.15 | -3.4% / -1.9% | +2.8% | 36.5M |
| XLV | 185.97 (08:49 sip) | -1.0% | 187.88 | 3.83 (2.0%) | 177.07-192.32 | +2.0% / +7.2% | -0.2% | 11.3M |
| XLI | 165.56 (08:35 sip) | -0.1% | 165.66 | 3.54 (2.1%) | 161.74-172.40 | -1.3% / -1.8% | -1.9% | 8.9M |
| XLY | 117.55 (04:05 sip) | -0.5% | 118.15 | 2.63 (2.2%) | 112.83-122.92 | +0.5% / +3.8% | -2.4% | 9.1M |
| XLP | 91.88 (08:49 sip) | -0.8% | 92.60 | 1.66 (1.8%) | 86.36-93.48 | +3.2% / +8.0% | +1.9% | 19.2M |
| XLU | 44.00 (08:49 sip) | -0.3% | 44.12 | 0.60 (1.4%) | 41.44-44.40 | +2.1% / +5.4% | +0.8% | 24.7M |
| XLB | no trade today | - | 51.47 | 1.05 (2.0%) | 50.61-54.63 | -1.5% / +1.2% | -2.8% | 12.1M |
| XLRE | 44.14 (08:45 sip) | -0.2% | 44.25 | 0.70 (1.6%) | 41.78-45.34 | +1.6% / +4.0% | -0.9% | 7.9M |
| XLC | 106.05 (08:20 sip) | -0.7% | 106.82 | 2.29 (2.1%) | 99.33-110.84 | +1.4% / -2.2% | -0.5% | 8.0M |
| KRE | 71.90 (08:25 sip) | -0.4% | 72.19 | 1.56 (2.2%) | 69.40-75.80 | -0.5% / +0.8% | -1.7% | 14.2M |
| XHB | 100.29 (08:40 sip) | -0.7% | 101.01 | 3.26 (3.2%) | 94.23-108.78 | -0.2% / +2.7% | -4.7% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 350.86 (09:04 iex) | -0.5% | 352.78 | 9.48 (2.7%) | 325.08-360.83 | +1.8% / +3.9% | +0.7% | 48.2M |
| MSFT | 514.40 (09:00 iex) | -0.7% | 517.99 | 17.89 (3.5%) | 504.96-559.15 | -2.0% / -0.3% | -5.0% | 27.1M |
| NVDA | 157.80 (09:03 iex) | +1.1% | 156.14 | 11.33 (7.3%) | 148.80-222.19 | -20.2% / -26.7% | -12.6% | 221.4M |
| AMZN | 259.00 (09:00 iex) | +0.5% | 257.75 | 11.03 (4.3%) | 229.36-275.34 | +0.3% / +1.2% | -3.4% | 49.7M |
| GOOGL | 282.50 (08:49 sip) | -0.4% | 283.72 | 12.32 (4.3%) | 276.92-344.77 | -5.6% / -13.3% | -1.5% | 41.7M |
| META | 621.18 (08:49 sip) | -0.8% | 626.41 | 21.69 (3.5%) | 583.80-713.22 | -1.1% / -7.9% | -2.3% | 23.6M |
| TSLA | 381.48 (08:51 iex) | +0.5% | 379.74 | 18.00 (4.7%) | 338.15-414.23 | -1.6% / +1.2% | +0.4% | 39.3M |
| AVGO | 336.99 (08:52 iex) | +1.1% | 333.40 | 20.44 (6.1%) | 289.77-369.82 | +0.8% / -3.3% | +4.4% | 27.4M |
| AMD | 511.97 (08:49 sip) | +1.5% | 504.28 | 47.89 (9.5%) | 402.10-594.00 | -2.5% / -9.2% | -0.8% | 35.6M |
| ORCL | 118.67 (08:51 iex) | -0.4% | 119.09 | 9.51 (8.0%) | 109.21-148.48 | -5.5% / -12.2% | -0.6% | 41.8M |
| NFLX | 60.70 (08:53 iex) | -0.1% | 60.75 | 1.83 (3.0%) | 60.48-70.66 | -4.9% / -11.7% | -5.0% | 45.9M |
| CRM | 210.48 (08:49 sip) | -2.0% | 214.83 | 8.15 (3.8%) | 208.88-252.42 | -6.2% / -8.3% | -0.1% | 6.7M |
| JPM | 335.12 (08:49 sip) | -0.9% | 338.21 | 8.24 (2.4%) | 330.40-359.80 | -0.3% / -0.3% | -1.1% | 6.4M |
| GS | 888.00 (08:45 sip) | -0.4% | 891.54 | 29.74 (3.3%) | 854.45-939.38 | -1.1% / -3.0% | -1.6% | 2.2M |
| BAC | 49.84 (08:49 sip) | -0.5% | 50.08 | 1.22 (2.4%) | 49.17-53.02 | -0.8% / -6.9% | -0.9% | 34.6M |
| XOM | 167.55 (08:49 sip) | +0.4% | 166.87 | 4.66 (2.8%) | 159.11-187.32 | -3.9% / -1.0% | +1.9% | 14.3M |
| CVX | 217.40 (08:45 sip) | +0.1% | 217.14 | 5.22 (2.4%) | 206.01-236.48 | -2.5% / +0.7% | +3.0% | 8.1M |
| LLY | 1,413.20 (08:49 sip) | -1.3% | 1,431.67 | 52.53 (3.7%) | 1,256.10-1,475.25 | +4.9% / +15.0% | +1.5% | 3.1M |
| UNH | 399.89 (08:49 sip) | -2.9% | 412.02 | 10.98 (2.7%) | 388.00-426.55 | +1.0% / +5.2% | +3.6% | 4.9M |
| JNJ | 279.38 (08:45 sip) | -1.1% | 282.55 | 7.39 (2.6%) | 254.56-290.25 | +3.5% / +5.8% | +0.2% | 7.5M |
| WMT | 127.25 (08:49 sip) | -0.9% | 128.41 | 3.06 (2.4%) | 116.63-131.82 | +3.8% / +11.7% | +2.2% | 21.9M |
| COST | 1,106.50 (08:45 sip) | -0.7% | 1,113.74 | 21.39 (1.9%) | 978.87-1,117.00 | +7.4% / +14.8% | +4.5% | 2.4M |
| HD | 337.51 (08:49 sip) | -2.9% | 347.51 | 9.96 (2.9%) | 310.64-362.44 | +3.5% / +11.1% | -1.7% | 4.5M |
| CAT | 573.00 (08:49 sip) | +0.4% | 570.49 | 32.26 (5.7%) | 550.81-743.23 | -10.4% / -22.3% | -4.7% | 3.9M |
| BA | 164.35 (08:49 sip) | -0.5% | 165.22 | 5.09 (3.1%) | 164.71-193.28 | -6.3% / -12.1% | -4.2% | 10.6M |
| DAL | 85.75 (08:49 sip) | -1.0% | 86.60 | 3.24 (3.7%) | 74.14-92.52 | +3.3% / +5.7% | -5.7% | 6.5M |
| UAL | 108.86 (08:49 sip) | -1.7% | 110.76 | 5.41 (4.9%) | 94.54-122.08 | +2.4% / +2.5% | -8.0% | 5.8M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| TEL | 224.49 (08:00 sip) | +5.2% | 213.45 | 8.78 (4.1%) | 204.63-230.00 | -1.1% / -0.0% | -2.4% | 2.1M |
| MRVL | 151.63 (09:04 iex) | +4.3% | 145.36 | 18.53 (12.7%) | 132.54-253.66 | -23.6% / -36.1% | -6.0% | 30.5M |
| NKE | 39.64 (09:04 iex) | +3.6% | 38.26 | 1.27 (3.3%) | 36.84-41.10 | -0.3% / +3.7% | -4.1% | 21.6M |
| KKR | 98.01 (08:49 sip) | +2.7% | 95.47 | 3.74 (3.9%) | 87.19-103.84 | -0.0% / +0.7% | -2.7% | 4.7M |
| MPWR | 1,347.00 (08:49 sip) | +2.5% | 1,314.00 | 106.23 (8.1%) | 1,125.00-1,513.49 | +3.6% / +2.2% | -5.3% | 1.1M |
| MCHP | 60.03 (08:49 sip) | +2.4% | 58.64 | 4.87 (8.3%) | 54.83-81.22 | -17.1% / -20.1% | -4.6% | 16.0M |
| GLW | 108.50 (08:49 sip) | +2.2% | 106.17 | 8.66 (8.2%) | 101.59-136.45 | -12.0% / -24.3% | -8.2% | 10.8M |
| ALB | 90.00 (08:49 sip) | +2.1% | 88.16 | 3.91 (4.4%) | 87.78-102.28 | -6.7% / -14.2% | -11.1% | 2.5M |
| JD | 25.32 (08:49 sip) | -8.1% | 27.54 | 0.73 (2.6%) | 25.05-29.34 | +2.5% / +2.5% | -3.0% | 9.2M |
| BABA | 87.57 (08:49 sip) | -3.4% | 90.62 | 3.82 (4.2%) | 90.57-111.17 | -10.6% / -14.8% | -14.0% | 10.9M |
| HUM | 446.00 (08:45 sip) | -3.3% | 461.25 | 17.77 (3.9%) | 399.35-462.87 | +8.3% / +12.7% | +9.0% | 1.6M |
| CVS | 85.74 (08:49 sip) | -3.2% | 88.59 | 3.53 (4.0%) | 77.33-94.83 | -0.8% / -0.6% | +3.9% | 11.3M |
| CHTR | 134.80 (08:35 sip) | -3.0% | 138.95 | 7.24 (5.2%) | 101.11-139.77 | +17.5% / +17.1% | +14.6% | 3.0M |
| CNC | 73.14 (08:45 sip) | -2.2% | 74.77 | 3.68 (4.9%) | 64.85-78.08 | +6.6% / +11.2% | +9.1% | 6.1M |
| WDAY | 190.00 (08:05 sip) | -2.1% | 194.06 | 7.43 (3.8%) | 185.78-212.91 | -2.5% / +0.4% | +2.0% | 2.1M |
| ACN | 242.75 (08:49 sip) | -2.0% | 247.70 | 9.82 (4.0%) | 232.57-271.76 | -1.7% / +14.0% | -2.6% | 5.6M |
