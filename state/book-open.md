## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Tuesday 2026-10-20. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$102,025.00**
- Cash: $88,578.33
- Session P&L so far: +0.21% (new entries are blocked at -3.0%)
- Gross exposure: $47,919 (47% of equity, cap 150%)
- Net exposure: $+7,924 (+8%, cap +/-100%)
- Risk at stake (entry to stop): $1,564 (1.53% of equity, cap 4.0%) — 2.47% left for new plays
- Slots: 4 open + 1 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMD | short | 19 | 542.20 | 535.48 | +128 (+1.2%) | 558.00 | 512.00 | Relief gap on upgrades without any change to the AI-credit story, now confirmed by the open rather than predicted. Overh |
| CVX | long | 78 | 224.48 | 224.83 | +27 (+0.2%) | 218.00 | 236.00 | Energy leads the rotation away from AI capex and the oil tape still points up. A retest of the breakout and Monday's 224 |
| HD | long | 33 | 310.70 | 314.70 | +132 (+1.3%) | 303.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 130.34 | -21 (-0.5%) | 137.40 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| NVDA | short | 26 | 212.40 | stop | 222.00 | 198.00 | 2026-10-20 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 21.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |

### Ideas you passed on, replayed against the tape

43 resolved: 10 reached target first, 25 stop first, 7 never reached the entry, 1 expired, 0 ambiguous. Average -0.30R across the 36 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-08 pre-market | UAL | short | Oil-cost victim, but DAL reports 10/09 pre-market and has lifted the group befor | target | +1.21R | 33% |
| 2026-10-14 pre-market | BAC | short | Already -7.5% on the earnings miss; shorting the gap low. Review may short a fai | stop | -1.05R | 33% |
| 2026-10-13 open | JPM | short | Fading its gap after an EPS miss, but close to the 324 20-day low with little ro | stop | -0.82R | 33% |
| 2026-10-14 open | XHB | short | Morning play rejected by broker: not shortable. | stop | -0.73R | 37% |
| 2026-10-09 pre-market | XLE | long | Energy +4.1% over 5d and de-escalation removes the bid; wrong day to buy the dip | never filled | - | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AMD | 535.54 (10:05 iex) | -0.5% | 538.05 | 530.02 / 524.60-535.64 | 26.76 (5.0%) | 526.83-658.52 | -11.3% / -0.0% | -9.5% | 20.1M |
| CVX | 224.81 (10:05 iex) | +0.2% | 224.37 | 226.91 / 224.11-227.28 | 4.42 (2.0%) | 200.78-225.67 | +6.5% / +8.1% | +4.4% | 7.5M |
| HD | 314.76 (10:04 iex) | +1.6% | 309.88 | 313.48 / 310.64-317.62 | 6.66 (2.2%) | 277.15-314.66 | +5.7% / -0.5% | +6.6% | 5.6M |
| ORCL | 130.34 (10:05 iex) | +0.6% | 129.59 | 128.51 / 127.45-130.71 | 6.40 (4.9%) | 127.36-153.03 | -6.2% / -10.2% | -5.7% | 30.6M |
| NVDA | 215.14 (10:05 iex) | -0.9% | 217.09 | 215.96 / 212.77-216.46 | 5.74 (2.6%) | 212.85-243.37 | -4.6% / -2.6% | -4.1% | 105.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 767.79 (10:05 iex) | +0.2% | 766.48 | 765.87 / 764.25-768.38 | 7.07 (0.9%) | 758.79-781.62 | -0.6% / -0.1% | -1.5% | 41.6M |
| QQQ | 716.36 (10:05 iex) | -0.3% | 718.36 | 715.27 / 710.39-716.88 | 10.76 (1.5%) | 707.23-762.86 | -3.1% / -1.1% | -3.7% | 35.7M |
| IWM | 273.56 (10:05 iex) | +0.8% | 271.28 | 271.53 / 271.29-274.32 | 3.86 (1.4%) | 269.88-288.94 | -2.6% / -5.8% | -2.4% | 26.2M |
| DIA | 522.66 (10:04 iex) | +0.7% | 518.92 | 519.15 / 518.46-523.53 | 5.15 (1.0%) | 504.59-525.09 | +0.9% / -0.8% | +0.2% | 3.4M |
| TLT | 80.00 (10:05 iex) | +0.7% | 79.46 | 80.06 / 80.02-80.20 | 0.83 (1.0%) | 76.43-81.61 | +1.2% / -1.1% | +1.8% | 50.4M |
| GLD | 377.76 (10:05 iex) | -0.5% | 379.69 | 377.91 / 377.26-378.96 | 4.98 (1.3%) | 373.36-400.78 | -1.0% / -4.3% | -0.6% | 7.7M |
| USO | 160.78 (10:04 iex) | -0.0% | 160.81 | 162.70 / 160.67-162.77 | 4.57 (2.8%) | 141.76-162.99 | +7.3% / +12.0% | +6.5% | 5.4M |
| SMH | 544.37 (10:04 iex) | -0.7% | 548.46 | 541.85 / 536.23-544.98 | 16.03 (2.9%) | 539.07-639.47 | -8.4% / -5.2% | -7.2% | 7.6M |
| XLK | 185.05 (10:04 iex) | -0.5% | 185.96 | 184.29 / 182.81-185.23 | 3.62 (1.9%) | 182.82-203.25 | -4.8% / -2.0% | -5.3% | 8.2M |
| XLF | 55.67 (10:05 iex) | +1.1% | 55.06 | 55.19 / 55.17-55.85 | 0.69 (1.2%) | 52.81-56.05 | +1.2% / -1.9% | +0.0% | 39.4M |
| XLE | 67.86 (10:05 iex) | +0.1% | 67.80 | 68.45 / 67.56-68.48 | 1.31 (1.9%) | 60.95-68.51 | +5.6% / +6.7% | +2.7% | 32.3M |
| XLV | 179.06 (10:05 iex) | +1.9% | 175.65 | 177.43 / 177.31-179.79 | 2.89 (1.6%) | 165.19-178.86 | +3.0% / +3.4% | +2.1% | 8.4M |
| XLI | 166.28 (10:05 iex) | -0.2% | 166.68 | 165.75 / 164.96-166.61 | 2.55 (1.5%) | 164.66-172.34 | -1.3% / -3.9% | -1.5% | 7.3M |
| XLY | 115.17 (10:04 iex) | +0.6% | 114.46 | 114.97 / 114.56-115.50 | 1.49 (1.3%) | 107.99-114.69 | +2.9% / +0.7% | +2.0% | 7.0M |
| XLP | 87.90 (10:05 iex) | +0.8% | 87.21 | 87.81 / 87.60-88.31 | 1.16 (1.3%) | 80.10-88.47 | +4.9% / +4.1% | +3.3% | 12.4M |
| XLU | 41.85 (10:05 iex) | +1.2% | 41.36 | 41.60 / 41.44-41.98 | 0.68 (1.7%) | 39.03-42.29 | +1.8% / -1.0% | -0.6% | 35.9M |
| XLB | 50.76 (10:05 iex) | -0.4% | 50.95 | 50.70 / 50.61-50.97 | 0.73 (1.4%) | 47.81-51.51 | +2.6% / -0.1% | +3.1% | 11.7M |
| XLRE | 42.15 (10:04 iex) | +1.2% | 41.67 | 41.92 / 41.86-42.34 | 0.61 (1.5%) | 40.28-42.67 | +0.6% / -2.7% | -0.6% | 7.5M |
| XLC | 110.13 (10:04 iex) | +0.0% | 110.09 | 110.04 / 109.65-110.35 | 1.66 (1.5%) | 109.45-115.61 | -1.3% / -1.4% | -1.2% | 6.5M |
| KRE | 70.54 (10:05 iex) | +1.8% | 69.26 | 69.40 / 69.40-70.89 | 1.27 (1.8%) | 67.79-72.68 | -1.0% / -4.5% | -0.4% | 16.0M |
| XHB | 95.15 (10:04 iex) | +1.1% | 94.13 | 94.50 / 94.23-95.72 | 2.23 (2.4%) | 91.87-99.67 | -2.0% / -5.9% | +0.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 342.15 (10:05 iex) | -0.2% | 342.94 | 339.86 / 338.70-343.03 | 6.42 (1.9%) | 325.81-348.15 | +1.6% / +5.1% | +0.6% | 37.1M |
| MSFT | 528.95 (10:05 iex) | -0.9% | 533.52 | 534.32 / 525.84-534.32 | 11.47 (2.2%) | 491.22-551.15 | +2.2% / +5.4% | -1.4% | 21.9M |
| NVDA | 215.14 (10:05 iex) | -0.9% | 217.09 | 215.96 / 212.77-216.46 | 5.74 (2.6%) | 212.85-243.37 | -4.6% / -2.6% | -4.1% | 105.5M |
| AMZN | 262.62 (10:05 iex) | +0.1% | 262.45 | 264.07 / 260.42-265.34 | 6.62 (2.5%) | 244.72-263.72 | +3.6% / +2.2% | +1.1% | 36.5M |
| GOOGL | 343.30 (10:05 iex) | -0.3% | 344.18 | 343.64 / 341.00-344.32 | 9.04 (2.6%) | 335.51-364.17 | -0.5% / -0.0% | -2.4% | 24.8M |
| META | 683.85 (10:05 iex) | -3.1% | 705.44 | 694.98 / 681.18-696.00 | 21.41 (3.0%) | 693.86-779.82 | -3.9% / +7.3% | -5.1% | 20.2M |
| TSLA | 370.98 (10:05 iex) | +0.8% | 368.06 | 370.41 / 363.64-372.00 | 11.43 (3.1%) | 345.88-388.56 | -0.5% / +2.2% | -2.6% | 34.9M |
| AVGO | 336.71 (10:05 iex) | +0.6% | 334.59 | 334.34 / 330.80-337.25 | 11.74 (3.5%) | 328.58-380.84 | -5.5% / -7.9% | -5.7% | 21.9M |
| AMD | 535.54 (10:05 iex) | -0.5% | 538.05 | 530.02 / 524.60-535.64 | 26.76 (5.0%) | 526.83-658.52 | -11.3% / -0.0% | -9.5% | 20.1M |
| ORCL | 130.34 (10:05 iex) | +0.6% | 129.59 | 128.51 / 127.45-130.71 | 6.40 (4.9%) | 127.36-153.03 | -6.2% / -10.2% | -5.7% | 30.6M |
| NFLX | 70.22 (10:05 iex) | +0.5% | 69.85 | 69.84 / 69.50-70.64 | 1.61 (2.3%) | 66.54-73.76 | -0.4% / -6.9% | -1.1% | 35.1M |
| CRM | 240.89 (10:05 iex) | -0.6% | 242.45 | 235.75 / 235.60-243.93 | 8.61 (3.5%) | 220.29-251.94 | +3.8% / +5.0% | +3.6% | 8.8M |
| JPM | 337.61 (10:02 iex) | +1.2% | 333.53 | 333.97 / 332.55-338.99 | 6.29 (1.9%) | 324.25-350.35 | -0.1% / -3.7% | -0.2% | 8.2M |
| GS | 880.14 (10:05 iex) | +0.5% | 875.78 | 870.46 / 864.12-882.86 | 22.27 (2.5%) | 859.03-967.76 | -2.9% / -9.7% | -2.0% | 2.3M |
| BAC | 50.65 (10:05 iex) | +0.5% | 50.39 | 50.18 / 50.01-50.88 | 1.29 (2.6%) | 49.26-58.12 | -6.7% / -14.1% | -7.7% | 43.1M |
| XOM | 178.19 (10:04 iex) | -0.1% | 178.28 | 179.90 / 177.69-180.26 | 3.43 (1.9%) | 155.85-179.30 | +6.7% / +8.6% | +3.6% | 11.5M |
| CVX | 224.81 (10:05 iex) | +0.2% | 224.37 | 226.91 / 224.11-227.28 | 4.42 (2.0%) | 200.78-225.67 | +6.5% / +8.1% | +4.4% | 7.5M |
| LLY | 1,298.99 (10:04 iex) | +4.7% | 1,240.34 | 1,263.50 / 1,260.17-1,304.31 | 36.93 (3.0%) | 1,131.21-1,275.88 | +4.9% / +5.0% | +4.9% | 2.3M |
| UNH | 417.32 (10:05 iex) | +2.6% | 406.88 | 410.12 / 408.28-417.12 | 12.87 (3.2%) | 362.60-414.12 | +7.1% / +5.4% | +7.5% | 5.9M |
| JNJ | 259.17 (10:04 iex) | +2.1% | 253.79 | 257.48 / 256.42-260.43 | 6.28 (2.5%) | 245.17-275.23 | -2.6% / -4.2% | -3.8% | 7.6M |
| WMT | 119.50 (10:04 iex) | +0.7% | 118.70 | 120.54 / 119.18-120.54 | 2.38 (2.0%) | 103.39-121.38 | +7.7% / +8.9% | +5.0% | 21.3M |
| COST | 998.49 (10:03 iex) | +0.3% | 995.53 | 1,000.70 / 994.75-1,003.00 | 15.97 (1.6%) | 883.10-1,008.37 | +6.1% / +6.5% | +3.8% | 2.3M |
| HD | 314.76 (10:04 iex) | +1.6% | 309.88 | 313.48 / 310.64-317.62 | 6.66 (2.2%) | 277.15-314.66 | +5.7% / -0.5% | +6.6% | 5.6M |
| CAT | 719.36 (10:05 iex) | -0.9% | 725.79 | 711.00 / 708.75-721.59 | 30.40 (4.2%) | 704.01-876.95 | -9.3% / -10.4% | -9.2% | 2.6M |
| BA | 190.29 (10:04 iex) | -0.6% | 191.42 | 190.54 / 189.40-191.00 | 4.66 (2.4%) | 183.38-204.06 | +0.3% / -6.4% | +1.0% | 8.5M |
| DAL | 75.84 (10:05 iex) | +1.6% | 74.63 | 74.30 / 74.14-76.19 | 2.58 (3.5%) | 74.40-85.93 | -8.3% / -8.7% | -6.6% | 7.3M |
| UAL | 97.44 (10:04 iex) | +1.9% | 95.60 | 95.06 / 94.54-97.87 | 3.83 (4.0%) | 95.27-118.26 | -11.4% / -14.0% | -8.5% | 4.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-20 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BRZE | 45.34 (10:05 iex) | +50.9% | 30.04 | 45.53 / 45.28-45.58 | 1.51 (5.0%) | 22.27-31.00 | +11.7% / +6.5% | +3.4% | 2.0M |
| SAIQ | 5.14 (10:04 iex) | +50.7% | 3.41 | 4.62 / 4.52-5.28 | 2.06 (60.4%) | 1.76-12.95 | -44.6% / -61.3% | -8.1% | 5.1M |
| MYGN | 5.45 (10:05 iex) | +29.3% | 4.21 | 5.30 / 5.25-5.94 | 0.28 (6.7%) | 3.76-4.83 | -0.2% / +14.3% | +0.2% | 1.7M |
