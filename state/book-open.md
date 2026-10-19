## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Monday 2026-10-19. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,668.29**
- Cash: $95,786.20
- Session P&L so far: -0.10% (new entries are blocked at -3.0%)
- Gross exposure: $46,270 (46% of equity, cap 150%)
- Net exposure: $+6,042 (+6%, cap +/-100%)
- Risk at stake (entry to stop): $1,518 (1.49% of equity, cap 4.0%) — 2.51% left for new plays
- Slots: 2 open + 2 resting entries of 8 — you may add at most 4 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| HD | long | 33 | 310.70 | 307.51 | -105 (-1.0%) | 303.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 129.26 | +14 (+0.3%) | 137.40 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XOM | long | 92 | 174.00 | limit | 168.50 | 182.50 | 2026-10-19 |
| SMH | short | 28 | 566.00 | limit | 584.00 | 540.00 | 2026-10-19 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 19.

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
| HD | 307.50 (10:04 iex) | -0.7% | 309.63 | 306.55 / 306.04-308.07 | 6.58 (2.1%) | 277.15-314.66 | +5.9% / -0.8% | +6.5% | 5.7M |
| ORCL | 129.31 (10:05 iex) | +0.8% | 128.23 | 130.66 / 129.18-130.81 | 6.96 (5.4%) | 127.36-153.03 | -7.8% / -11.3% | -9.3% | 30.6M |
| XOM | 178.75 (10:05 iex) | -0.1% | 178.98 | 178.45 / 177.23-179.30 | 3.52 (2.0%) | 155.85-179.16 | +7.7% / +9.4% | +5.9% | 11.8M |
| SMH | 548.11 (10:05 iex) | +1.5% | 539.79 | 556.73 / 547.77-556.73 | 15.64 (2.9%) | 539.07-639.47 | -10.2% / -6.8% | -10.5% | 7.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 766.28 (10:05 iex) | +0.4% | 763.25 | 767.23 / 765.84-768.06 | 6.89 (0.9%) | 758.79-781.62 | -1.0% / -0.5% | -2.0% | 42.1M |
| QQQ | 717.05 (10:05 iex) | +1.0% | 709.80 | 719.58 / 716.64-720.22 | 10.08 (1.4%) | 707.23-762.86 | -4.4% / -2.3% | -5.5% | 36.2M |
| IWM | 270.83 (10:04 iex) | +0.1% | 270.44 | 271.82 / 270.74-272.60 | 3.96 (1.5%) | 269.88-288.94 | -3.2% / -6.3% | -3.0% | 26.1M |
| DIA | 518.38 (09:59 iex) | -0.1% | 519.10 | 518.40 / 517.79-519.10 | 5.22 (1.0%) | 504.59-525.09 | +0.9% / -0.8% | +0.6% | 3.4M |
| TLT | 79.89 (10:05 iex) | -0.2% | 80.05 | 79.90 / 79.77-79.98 | 0.84 (1.0%) | 76.43-81.61 | +1.8% / -0.4% | +2.7% | 50.2M |
| GLD | 380.14 (10:04 iex) | -0.5% | 382.01 | 381.43 / 379.67-381.93 | 5.14 (1.3%) | 373.36-400.78 | -0.6% / -3.8% | -0.7% | 7.8M |
| USO | 159.57 (10:04 iex) | -1.4% | 161.76 | 159.00 / 158.76-159.94 | 4.75 (2.9%) | 141.76-162.38 | +8.4% / +13.4% | +9.1% | 5.5M |
| SMH | 548.11 (10:05 iex) | +1.5% | 539.79 | 556.73 / 547.77-556.73 | 15.64 (2.9%) | 539.07-639.47 | -10.2% / -6.8% | -10.5% | 7.7M |
| XLK | 185.77 (10:05 iex) | +1.3% | 183.47 | 186.96 / 185.63-187.18 | 3.46 (1.9%) | 182.82-203.25 | -6.3% / -3.3% | -7.7% | 8.2M |
| XLF | 55.30 (10:04 iex) | -0.4% | 55.52 | 55.36 / 55.24-55.50 | 0.70 (1.3%) | 52.81-56.20 | +2.0% / -1.1% | +1.4% | 39.4M |
| XLE | 68.31 (10:05 iex) | +0.1% | 68.24 | 67.95 / 67.90-68.51 | 1.33 (2.0%) | 60.95-68.29 | +6.8% / +7.8% | +4.9% | 32.7M |
| XLV | 176.44 (10:05 iex) | -0.2% | 176.71 | 175.72 / 175.56-177.35 | 2.93 (1.7%) | 165.19-178.86 | +3.9% / +4.2% | +3.5% | 8.5M |
| XLI | 166.90 (10:04 iex) | -0.5% | 167.76 | 168.38 / 166.70-168.48 | 2.57 (1.5%) | 164.66-172.34 | -0.8% / -3.5% | -0.9% | 7.5M |
| XLY | 113.22 (10:04 iex) | +0.7% | 112.46 | 112.93 / 112.67-113.41 | 1.39 (1.2%) | 107.99-114.69 | +1.2% / -1.1% | -0.3% | 7.0M |
| XLP | 87.45 (10:05 iex) | -0.2% | 87.62 | 86.85 / 86.83-87.46 | 1.17 (1.3%) | 80.10-88.47 | +5.8% / +4.6% | +5.0% | 12.2M |
| XLU | 41.74 (10:05 iex) | -1.1% | 42.21 | 42.13 / 41.67-42.18 | 0.67 (1.6%) | 39.03-42.29 | +4.0% / +0.9% | +1.9% | 35.7M |
| XLB | 50.81 (10:05 iex) | -0.2% | 50.92 | 51.03 / 50.69-51.10 | 0.75 (1.5%) | 47.81-51.51 | +2.7% / -0.2% | +3.0% | 11.8M |
| XLRE | 41.73 (10:05 iex) | -1.0% | 42.16 | 42.08 / 41.72-42.09 | 0.60 (1.4%) | 40.28-42.67 | +1.7% / -1.7% | +1.3% | 7.4M |
| XLC | 109.59 (10:05 iex) | -0.7% | 110.32 | 110.22 / 109.47-110.50 | 1.65 (1.5%) | 109.66-115.61 | -1.3% / -1.2% | -0.1% | 6.7M |
| KRE | 69.58 (10:05 iex) | -0.3% | 69.81 | 69.83 / 69.47-69.94 | 1.32 (1.9%) | 67.79-72.87 | -0.4% / -4.0% | +1.2% | 16.0M |
| XHB | 94.37 (10:05 iex) | -0.6% | 94.91 | 95.39 / 94.07-95.71 | 2.23 (2.4%) | 91.87-99.67 | -1.3% / -5.4% | +0.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.53 (10:05 iex) | +0.6% | 343.46 | 340.77 / 340.12-346.00 | 6.69 (1.9%) | 325.81-348.15 | +1.8% / +5.5% | +2.0% | 37.1M |
| MSFT | 532.26 (10:05 iex) | +0.6% | 529.05 | 528.71 / 528.06-532.65 | 11.74 (2.2%) | 491.22-551.15 | +1.7% / +4.7% | -1.1% | 22.4M |
| NVDA | 215.38 (10:05 iex) | +0.6% | 214.13 | 218.09 / 214.70-218.18 | 5.76 (2.7%) | 212.85-243.37 | -6.2% / -4.0% | -6.6% | 106.2M |
| AMZN | 256.90 (10:05 iex) | +2.8% | 250.00 | 255.49 / 255.18-257.73 | 5.90 (2.4%) | 244.72-263.70 | -1.3% / -2.8% | -4.7% | 35.9M |
| GOOGL | 344.15 (10:05 iex) | +1.0% | 340.59 | 343.54 / 341.85-345.85 | 8.96 (2.6%) | 335.51-364.17 | -1.7% / -1.1% | -3.1% | 25.3M |
| META | 694.85 (10:05 iex) | -2.0% | 709.33 | 706.82 / 694.41-708.83 | 22.11 (3.1%) | 679.60-779.82 | -3.6% / +8.3% | -1.3% | 21.8M |
| TSLA | 360.93 (10:05 iex) | +1.7% | 354.72 | 357.36 / 354.47-362.89 | 10.86 (3.1%) | 345.88-388.56 | -4.2% / -1.3% | -7.3% | 34.7M |
| AVGO | 334.13 (10:05 iex) | +1.6% | 328.75 | 338.75 / 333.85-339.22 | 11.80 (3.6%) | 328.58-380.84 | -7.5% / -10.0% | -9.1% | 22.4M |
| AMD | 540.74 (10:05 iex) | +2.3% | 528.75 | 552.27 / 541.15-553.61 | 26.28 (5.0%) | 526.83-658.52 | -13.4% / -1.6% | -13.0% | 21.3M |
| ORCL | 129.31 (10:05 iex) | +0.8% | 128.23 | 130.66 / 129.18-130.81 | 6.96 (5.4%) | 127.36-153.03 | -7.8% / -11.3% | -9.3% | 30.6M |
| NFLX | 69.43 (10:05 iex) | -1.6% | 70.53 | 69.75 / 69.02-70.22 | 1.65 (2.3%) | 66.54-73.87 | +0.3% / -6.1% | +0.3% | 35.2M |
| CRM | 238.00 (10:04 iex) | -1.1% | 240.70 | 238.47 / 236.90-240.92 | 8.57 (3.6%) | 220.29-251.94 | +3.2% / +4.7% | +5.0% | 9.0M |
| JPM | 337.83 (10:05 iex) | -0.6% | 339.72 | 339.22 / 336.70-341.01 | 6.12 (1.8%) | 324.25-352.74 | +1.5% / -2.0% | +2.0% | 8.2M |
| GS | 882.52 (10:04 iex) | +0.1% | 881.26 | 885.88 / 878.55-887.00 | 22.32 (2.5%) | 859.03-967.76 | -2.8% / -9.4% | -1.6% | 2.3M |
| BAC | 51.19 (10:05 iex) | -0.1% | 51.23 | 51.25 / 51.02-51.53 | 1.25 (2.4%) | 49.26-58.28 | -5.8% / -13.1% | -5.7% | 42.6M |
| XOM | 178.75 (10:05 iex) | -0.1% | 178.98 | 178.45 / 177.23-179.30 | 3.52 (2.0%) | 155.85-179.16 | +7.7% / +9.4% | +5.9% | 11.8M |
| CVX | 225.46 (10:05 iex) | +0.2% | 224.99 | 223.88 / 223.12-225.67 | 4.50 (2.0%) | 200.78-225.31 | +7.3% / +8.8% | +6.1% | 7.5M |
| LLY | 1,253.69 (10:04 iex) | -0.3% | 1,257.03 | 1,243.39 / 1,240.23-1,257.33 | 37.21 (3.0%) | 1,131.21-1,275.88 | +6.6% / +6.5% | +6.6% | 2.3M |
| UNH | 406.15 (10:04 iex) | +1.2% | 401.43 | 399.69 / 399.20-408.40 | 12.67 (3.2%) | 362.60-414.12 | +6.0% / +4.0% | +5.8% | 5.9M |
| JNJ | 253.69 (10:05 iex) | -0.7% | 255.56 | 254.43 / 253.12-255.56 | 6.44 (2.5%) | 245.17-275.23 | -2.2% / -3.5% | -2.2% | 7.4M |
| WMT | 118.98 (10:05 iex) | +0.1% | 118.81 | 118.41 / 118.05-119.14 | 2.53 (2.1%) | 103.39-121.38 | +8.4% / +9.1% | +6.7% | 21.7M |
| COST | 992.11 (10:05 iex) | +0.3% | 989.11 | 985.57 / 985.01-993.92 | 16.04 (1.6%) | 883.10-1,008.37 | +5.9% / +5.9% | +4.5% | 2.3M |
| HD | 307.50 (10:04 iex) | -0.7% | 309.63 | 306.55 / 306.04-308.07 | 6.58 (2.1%) | 277.15-314.66 | +5.9% / -0.8% | +6.5% | 5.7M |
| CAT | 721.07 (10:04 iex) | -1.3% | 730.76 | 739.50 / 719.61-740.00 | 29.88 (4.1%) | 704.01-876.95 | -9.2% / -10.1% | -8.7% | 2.5M |
| BA | 189.66 (10:04 iex) | -0.3% | 190.21 | 190.02 / 188.72-190.50 | 4.85 (2.6%) | 183.38-204.06 | -0.6% / -7.4% | -0.1% | 8.5M |
| DAL | 75.14 (10:04 iex) | -0.3% | 75.37 | 76.74 / 74.94-76.82 | 2.53 (3.4%) | 75.06-85.93 | -7.9% / -8.2% | -8.0% | 7.5M |
| UAL | 95.89 (10:03 iex) | -0.2% | 96.10 | 97.57 / 95.85-98.13 | 3.82 (4.0%) | 96.07-118.26 | -11.7% / -14.1% | -10.6% | 4.5M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-19 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SLN | 19.57 (10:04 iex) | +125.5% | 8.68 | 19.59 / 19.57-19.61 | 0.64 (7.4%) | 8.66-12.50 | -16.3% / -29.5% | -12.0% | 1.1M |
| AXTX | 16.48 (10:03 iex) | +16.2% | 14.18 | 16.48 / 16.03-17.53 | 5.46 (38.5%) | 13.71-44.60 | -54.9% / -55.8% | -46.1% | 3.0M |
| KORU | 11.96 (10:04 iex) | +12.4% | 10.64 | 12.48 / 11.95-12.48 | 1.78 (16.7%) | 10.45-23.93 | -44.1% / -46.3% | -40.4% | 25.6M |
| IAM | 15.64 (10:03 iex) | -34.3% | 23.81 | 21.00 / 15.64-21.54 | 6.09 (25.6%) | 16.15-25.00 | - / - | - | 2.5M |
