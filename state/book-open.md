## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Tuesday 2026-11-17. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,676.76**
- Cash: $143,294.09
- Session P&L so far: +0.10% (new entries are blocked at -3.0%)
- Gross exposure: $61,647 (60% of equity, cap 150%)
- Net exposure: $-61,647 (-60%, cap +/-100%)
- Risk at stake (entry to stop): $1,524 (1.48% of equity, cap 4.0%) — 2.52% left for new plays
- Slots: 2 open + 1 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 40% of equity in notional: at 1% risk its stop must be at least 2.5% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| HD | short | 51 | 343.57 | 342.38 | +60 (+0.3%) | -17% | 353.50 | 323.50 |
| IWM | short | 85 | 281.03 | 272.42 | +732 (+3.1%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **HD**, opened 2026-11-17 (session 1 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.
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

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| HD | 342.85 (10:05 iex) | -1.3% | 347.51 | 335.07 / 334.44-346.75 | 9.96 (2.9%) | 310.64-362.44 | +3.5% / +11.1% | -1.7% | 4.5M |
| IWM | 272.44 (10:05 iex) | -0.2% | 272.94 | 272.04 / 271.55-273.05 | 5.61 (2.1%) | 270.23-286.17 | -2.0% / -2.6% | -3.4% | 23.7M |
| GLD | 353.45 (10:05 iex) | +0.1% | 352.93 | 353.87 / 353.42-354.92 | 7.57 (2.1%) | 351.96-380.88 | -4.0% / -7.1% | -7.0% | 9.6M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 737.99 (10:05 iex) | -0.3% | 739.95 | 738.39 / 737.47-739.69 | 13.51 (1.8%) | 732.71-775.64 | -2.3% / -3.1% | -1.7% | 48.5M |
| QQQ | 661.13 (10:05 iex) | -0.1% | 661.75 | 663.06 / 659.70-663.36 | 19.23 (2.9%) | 647.05-727.95 | -4.5% / -7.7% | -2.6% | 49.9M |
| IWM | 272.44 (10:05 iex) | -0.2% | 272.94 | 272.04 / 271.55-273.05 | 5.61 (2.1%) | 270.23-286.17 | -2.0% / -2.6% | -3.4% | 23.7M |
| DIA | 512.74 (10:05 iex) | -0.6% | 515.68 | 511.04 / 510.96-514.12 | 8.04 (1.6%) | 508.66-536.60 | -1.2% / -0.6% | -1.5% | 3.7M |
| TLT | 79.27 (10:04 iex) | -0.1% | 79.38 | 79.31 / 79.23-79.36 | 0.78 (1.0%) | 79.11-82.42 | -1.9% / -0.5% | -3.1% | 35.8M |
| GLD | 353.45 (10:05 iex) | +0.1% | 352.93 | 353.87 / 353.42-354.92 | 7.57 (2.1%) | 351.96-380.88 | -4.0% / -7.1% | -7.0% | 9.6M |
| USO | 142.07 (10:04 iex) | +1.5% | 140.03 | 142.58 / 141.94-142.74 | 5.90 (4.2%) | 138.36-171.82 | -9.7% / -8.3% | -1.8% | 5.4M |
| SMH | 461.81 (10:04 iex) | -0.0% | 461.90 | 466.43 / 459.63-466.43 | 27.80 (6.0%) | 445.59-571.00 | -10.1% / -17.2% | -5.2% | 11.9M |
| XLK | 164.15 (10:05 iex) | -0.4% | 164.76 | 165.49 / 163.88-165.53 | 6.43 (3.9%) | 162.14-191.55 | -7.2% / -11.7% | -3.6% | 12.7M |
| XLF | 57.80 (10:05 iex) | -0.6% | 58.18 | 57.71 / 57.69-58.02 | 1.04 (1.8%) | 55.17-60.04 | +1.7% / +4.0% | +0.3% | 33.4M |
| XLE | 64.10 (10:05 iex) | +0.6% | 63.69 | 64.09 / 63.91-64.55 | 1.70 (2.7%) | 60.43-70.15 | -3.4% / -1.9% | +2.8% | 36.5M |
| XLV | 186.15 (10:04 iex) | -0.9% | 187.88 | 185.72 / 185.42-186.86 | 3.83 (2.0%) | 177.07-192.32 | +2.0% / +7.2% | -0.2% | 11.3M |
| XLI | 166.29 (10:05 iex) | +0.4% | 165.66 | 165.45 / 165.37-166.90 | 3.54 (2.1%) | 161.74-172.40 | -1.3% / -1.8% | -1.9% | 8.9M |
| XLY | 118.47 (10:05 iex) | +0.3% | 118.15 | 117.64 / 117.60-118.69 | 2.63 (2.2%) | 112.83-122.92 | +0.5% / +3.8% | -2.4% | 9.1M |
| XLP | 92.29 (10:05 iex) | -0.3% | 92.60 | 91.85 / 91.78-92.73 | 1.66 (1.8%) | 86.36-93.48 | +3.2% / +8.0% | +1.9% | 19.2M |
| XLU | 43.88 (10:04 iex) | -0.5% | 44.12 | 43.74 / 43.72-43.98 | 0.60 (1.4%) | 41.44-44.40 | +2.1% / +5.4% | +0.8% | 24.7M |
| XLB | 51.83 (10:05 iex) | +0.7% | 51.47 | 51.32 / 51.25-52.04 | 1.05 (2.0%) | 50.61-54.63 | -1.5% / +1.2% | -2.8% | 12.1M |
| XLRE | 44.13 (10:03 iex) | -0.3% | 44.25 | 43.98 / 43.90-44.22 | 0.70 (1.6%) | 41.78-45.34 | +1.6% / +4.0% | -0.9% | 7.9M |
| XLC | 106.67 (10:05 iex) | -0.1% | 106.82 | 106.45 / 106.08-106.84 | 2.29 (2.1%) | 99.33-110.84 | +1.4% / -2.2% | -0.5% | 8.0M |
| KRE | 72.15 (10:05 iex) | -0.1% | 72.19 | 71.91 / 71.61-72.24 | 1.56 (2.2%) | 69.40-75.80 | -0.5% / +0.8% | -1.7% | 14.2M |
| XHB | 101.38 (10:00 iex) | +0.4% | 101.01 | 100.28 / 99.89-101.74 | 3.26 (3.2%) | 94.23-108.78 | -0.2% / +2.7% | -4.7% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 354.62 (10:05 iex) | +0.5% | 352.78 | 352.83 / 351.81-355.29 | 9.48 (2.7%) | 325.08-360.83 | +1.8% / +3.9% | +0.7% | 48.2M |
| MSFT | 511.08 (10:05 iex) | -1.3% | 517.99 | 514.57 / 509.88-515.64 | 17.89 (3.5%) | 504.96-559.15 | -2.0% / -0.3% | -5.0% | 27.1M |
| NVDA | 155.10 (10:05 iex) | -0.7% | 156.14 | 156.90 / 154.76-157.46 | 11.33 (7.3%) | 148.80-222.19 | -20.2% / -26.7% | -12.6% | 221.4M |
| AMZN | 258.92 (10:05 iex) | +0.5% | 257.75 | 257.27 / 257.10-259.35 | 11.03 (4.3%) | 229.36-275.34 | +0.3% / +1.2% | -3.4% | 49.7M |
| GOOGL | 282.49 (10:05 iex) | -0.4% | 283.72 | 283.33 / 280.89-284.09 | 12.32 (4.3%) | 276.92-344.77 | -5.6% / -13.3% | -1.5% | 41.7M |
| META | 623.69 (10:05 iex) | -0.4% | 626.41 | 624.21 / 619.36-627.48 | 21.69 (3.5%) | 583.80-713.22 | -1.1% / -7.9% | -2.3% | 23.6M |
| TSLA | 382.12 (10:05 iex) | +0.6% | 379.74 | 382.19 / 378.92-382.84 | 18.00 (4.7%) | 338.15-414.23 | -1.6% / +1.2% | +0.4% | 39.3M |
| AVGO | 339.71 (10:05 iex) | +1.9% | 333.40 | 335.99 / 334.86-341.50 | 20.44 (6.1%) | 289.77-369.82 | +0.8% / -3.3% | +4.4% | 27.4M |
| AMD | 504.71 (10:05 iex) | +0.1% | 504.28 | 512.44 / 497.80-512.44 | 47.89 (9.5%) | 402.10-594.00 | -2.5% / -9.2% | -0.8% | 35.6M |
| ORCL | 117.47 (10:05 iex) | -1.4% | 119.09 | 119.02 / 117.05-120.90 | 9.51 (8.0%) | 109.21-148.48 | -5.5% / -12.2% | -0.6% | 41.8M |
| NFLX | 60.71 (10:05 iex) | -0.1% | 60.75 | 60.66 / 60.29-60.93 | 1.83 (3.0%) | 60.48-70.66 | -4.9% / -11.7% | -5.0% | 45.9M |
| CRM | 200.11 (10:05 iex) | -6.9% | 214.83 | 209.01 / 199.63-211.00 | 8.15 (3.8%) | 208.88-252.42 | -6.2% / -8.3% | -0.1% | 6.7M |
| JPM | 335.11 (10:05 iex) | -0.9% | 338.21 | 333.57 / 332.32-336.73 | 8.24 (2.4%) | 330.40-359.80 | -0.3% / -0.3% | -1.1% | 6.4M |
| GS | 888.59 (10:05 iex) | -0.3% | 891.54 | 888.06 / 882.51-892.43 | 29.74 (3.3%) | 854.45-939.38 | -1.1% / -3.0% | -1.6% | 2.2M |
| BAC | 50.00 (10:05 iex) | -0.2% | 50.08 | 49.80 / 49.63-50.15 | 1.22 (2.4%) | 49.17-53.02 | -0.8% / -6.9% | -0.9% | 34.6M |
| XOM | 168.14 (10:05 iex) | +0.8% | 166.87 | 167.46 / 167.46-169.42 | 4.66 (2.8%) | 159.11-187.32 | -3.9% / -1.0% | +1.9% | 14.3M |
| CVX | 218.13 (10:04 iex) | +0.5% | 217.14 | 217.58 / 217.00-219.45 | 5.22 (2.4%) | 206.01-236.48 | -2.5% / +0.7% | +3.0% | 8.1M |
| LLY | 1,427.12 (10:05 iex) | -0.3% | 1,431.67 | 1,415.99 / 1,410.00-1,432.28 | 52.53 (3.7%) | 1,256.10-1,475.25 | +4.9% / +15.0% | +1.5% | 3.1M |
| UNH | 389.75 (10:05 iex) | -5.4% | 412.02 | 399.23 / 389.12-399.99 | 10.98 (2.7%) | 388.00-426.55 | +1.0% / +5.2% | +3.6% | 4.9M |
| JNJ | 280.20 (10:05 iex) | -0.8% | 282.55 | 279.42 / 277.56-281.00 | 7.39 (2.6%) | 254.56-290.25 | +3.5% / +5.8% | +0.2% | 7.5M |
| WMT | 128.28 (10:05 iex) | -0.1% | 128.41 | 127.61 / 127.43-129.01 | 3.06 (2.4%) | 116.63-131.82 | +3.8% / +11.7% | +2.2% | 21.9M |
| COST | 1,119.16 (10:05 iex) | +0.5% | 1,113.74 | 1,109.26 / 1,109.26-1,123.25 | 21.39 (1.9%) | 978.87-1,117.00 | +7.4% / +14.8% | +4.5% | 2.4M |
| HD | 342.85 (10:05 iex) | -1.3% | 347.51 | 335.07 / 334.44-346.75 | 9.96 (2.9%) | 310.64-362.44 | +3.5% / +11.1% | -1.7% | 4.5M |
| CAT | 575.06 (10:04 iex) | +0.8% | 570.49 | 573.54 / 571.49-580.86 | 32.26 (5.7%) | 550.81-743.23 | -10.4% / -22.3% | -4.7% | 3.9M |
| BA | 167.64 (10:03 iex) | +1.5% | 165.22 | 165.00 / 164.65-168.13 | 5.09 (3.1%) | 164.71-193.28 | -6.3% / -12.1% | -4.2% | 10.6M |
| DAL | 85.95 (10:04 iex) | -0.8% | 86.60 | 86.49 / 85.53-86.60 | 3.24 (3.7%) | 74.14-92.52 | +3.3% / +5.7% | -5.7% | 6.5M |
| UAL | 109.63 (10:05 iex) | -1.0% | 110.76 | 109.41 / 109.06-110.52 | 5.41 (4.9%) | 94.54-122.08 | +2.4% / +2.5% | -8.0% | 5.8M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SNAP | 5.38 (10:05 iex) | +5.7% | 5.09 | 5.12 / 5.07-5.43 | 0.35 (6.8%) | 4.85-6.59 | -9.7% / -10.8% | +0.8% | 44.2M |
| ARM | 183.99 (10:05 iex) | +5.1% | 175.05 | 179.25 / 177.03-184.93 | 16.79 (9.6%) | 163.13-237.88 | -13.7% / -29.0% | -6.0% | 5.8M |
| MCHP | 60.45 (10:05 iex) | +3.1% | 58.64 | 60.21 / 59.27-60.49 | 4.87 (8.3%) | 54.83-81.22 | -17.1% / -20.1% | -4.6% | 16.0M |
| VRT | 194.47 (10:04 iex) | +3.1% | 188.67 | 191.97 / 191.97-197.68 | 20.94 (11.1%) | 170.80-254.73 | -9.3% / -17.8% | -5.9% | 8.7M |
| NEM | 113.35 (10:05 iex) | +2.8% | 110.31 | 110.50 / 110.44-114.40 | 5.02 (4.6%) | 104.51-127.28 | -3.5% / -6.3% | -11.9% | 7.0M |
| MPWR | 1,349.07 (10:05 iex) | +2.7% | 1,314.00 | 1,329.00 / 1,311.75-1,353.62 | 106.23 (8.1%) | 1,125.00-1,513.49 | +3.6% / +2.2% | -5.3% | 1.1M |
| ALB | 90.49 (10:00 iex) | +2.6% | 88.16 | 89.58 / 89.33-91.76 | 3.91 (4.4%) | 87.78-102.28 | -6.7% / -14.2% | -11.1% | 2.5M |
| ENTG | 143.66 (10:04 iex) | +2.6% | 140.02 | 142.73 / 141.34-145.75 | 12.75 (9.1%) | 124.14-170.06 | -3.1% / -5.1% | -0.0% | 3.8M |
| HUBS | 216.97 (10:03 iex) | -6.5% | 231.98 | 226.06 / 216.06-226.06 | 14.72 (6.3%) | 188.25-271.60 | +0.2% / +2.2% | +12.6% | 1.5M |
| JD | 25.79 (10:05 iex) | -6.4% | 27.54 | 25.75 / 25.65-26.41 | 0.73 (2.6%) | 25.05-29.34 | +2.5% / +2.5% | -3.0% | 9.2M |
| DOCU | 74.92 (10:02 iex) | -6.1% | 79.82 | 77.95 / 74.84-78.45 | 2.82 (3.5%) | 75.56-85.90 | -1.5% / +7.5% | +2.7% | 2.3M |
| MDB | 300.42 (10:05 iex) | -5.2% | 316.92 | 317.00 / 297.51-319.44 | 20.62 (6.5%) | 296.54-400.88 | -9.5% / -12.9% | -3.2% | 1.3M |
| WDAY | 183.99 (10:03 iex) | -5.2% | 194.06 | 189.67 / 182.60-190.06 | 7.43 (3.8%) | 185.78-212.91 | -2.5% / +0.4% | +2.0% | 2.1M |
| TEAM | 142.35 (10:05 iex) | -5.1% | 149.94 | 148.34 / 140.73-149.08 | 11.43 (7.6%) | 143.88-229.96 | -20.4% / -21.6% | -3.2% | 3.4M |
| HUM | 437.96 (10:05 iex) | -5.0% | 461.25 | 447.00 / 431.78-447.00 | 17.77 (3.9%) | 399.35-462.87 | +8.3% / +12.7% | +9.0% | 1.6M |
| INTU | 329.08 (10:04 iex) | -4.8% | 345.56 | 339.34 / 327.59-341.50 | 12.67 (3.7%) | 319.02-366.47 | +1.1% / +8.9% | +2.2% | 2.8M |
