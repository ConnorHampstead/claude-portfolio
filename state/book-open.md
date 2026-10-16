## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Friday 2026-10-16. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,821.04**
- Cash: $91,506.23
- Session P&L so far: +0.02% (new entries are blocked at -3.0%)
- Gross exposure: $71,925 (71% of equity, cap 150%)
- Net exposure: $+49,948 (+49%, cap +/-100%)
- Risk at stake (entry to stop): $1,765 (1.73% of equity, cap 4.0%) — 2.27% left for new plays
- Slots: 1 open + 4 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| HD | long | 33 | 310.70 | 312.57 | +62 (+0.6%) | 303.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| ORCL | short | 33 | 129.80 | stop | 137.40 | 116.50 | 2026-10-16 |
| XLV | long | 137 | 179.10 | stop | 175.40 | 184.60 | 2026-10-16 |
| CAT | short | 9 | 745.00 | limit | 772.00 | 700.00 | 2026-10-15 |
| WMT | long | 222 | 117.50 | limit | 115.20 | 122.10 | 2026-10-15 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 18.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |

### Ideas you passed on, replayed against the tape

42 resolved: 9 reached target first, 25 stop first, 7 never reached the entry, 1 expired, 0 ambiguous. Average -0.35R across the 35 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-14 pre-market | BAC | short | Already -7.5% on the earnings miss; shorting the gap low. Review may short a fai | stop | -1.05R | 33% |
| 2026-10-13 open | JPM | short | Fading its gap after an EPS miss, but close to the 324 20-day low with little ro | stop | -0.82R | 33% |
| 2026-10-14 open | XHB | short | Morning play rejected by broker: not shortable. | stop | -0.73R | 37% |
| 2026-10-09 pre-market | XLE | long | Energy +4.1% over 5d and de-escalation removes the bid; wrong day to buy the dip | never filled | - | 35% |
| 2026-10-09 open | NVDA | long | Withdrawn after the open: semis faded the whole rebound, invalidating the follow | never filled | - | 30% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| HD | 312.58 (10:04 iex) | +1.4% | 308.24 | 309.66 / 308.32-314.57 | 6.45 (2.1%) | 277.15-309.10 | +5.6% / -1.5% | +4.3% | 5.8M |
| ORCL | 132.38 (10:05 iex) | -1.6% | 134.47 | 133.49 / 131.37-133.80 | 6.85 (5.1%) | 127.60-153.03 | -4.0% / -7.2% | -0.5% | 30.7M |
| XLV | 177.84 (10:04 iex) | +0.4% | 177.19 | 178.20 / 177.25-178.28 | 2.96 (1.7%) | 165.19-178.86 | +4.4% / +4.6% | +5.4% | 8.6M |
| CAT | 741.59 (10:02 iex) | +0.8% | 735.64 | 734.36 / 730.00-742.55 | 30.24 (4.1%) | 704.01-876.95 | -9.1% / -9.8% | -7.6% | 2.6M |
| WMT | 119.08 (10:05 iex) | +1.0% | 117.87 | 118.07 / 118.07-119.48 | 2.57 (2.2%) | 103.39-121.38 | +8.1% / +8.4% | +6.6% | 22.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 771.43 (10:05 iex) | -0.0% | 771.79 | 773.24 / 771.02-773.25 | 6.53 (0.8%) | 757.97-781.62 | +0.1% / +0.6% | -0.3% | 42.2M |
| QQQ | 721.50 (10:05 iex) | -0.9% | 728.00 | 725.52 / 720.28-725.96 | 9.52 (1.3%) | 714.34-762.86 | -2.0% / +0.2% | -2.6% | 35.2M |
| IWM | 275.03 (10:05 iex) | -0.0% | 275.08 | 275.52 / 274.87-275.91 | 3.76 (1.4%) | 270.35-288.94 | -1.8% / -4.9% | -0.9% | 26.0M |
| DIA | 524.43 (10:03 iex) | +0.6% | 521.07 | 522.90 / 522.26-525.02 | 4.99 (1.0%) | 504.59-522.69 | +1.3% / -0.5% | +1.9% | 3.3M |
| TLT | 80.14 (10:05 iex) | +0.2% | 79.97 | 79.69 / 79.67-80.24 | 0.87 (1.1%) | 76.43-81.61 | +1.6% / -0.6% | +2.7% | 50.1M |
| GLD | 383.51 (10:04 iex) | +0.2% | 382.71 | 381.34 / 381.07-384.29 | 6.03 (1.6%) | 373.36-403.15 | -0.7% / -3.7% | +1.1% | 7.8M |
| USO | 156.34 (10:04 iex) | -0.6% | 157.31 | 156.97 / 156.31-157.68 | 4.80 (3.0%) | 141.76-158.10 | +5.7% / +10.9% | +6.6% | 5.4M |
| SMH | 549.51 (10:05 iex) | -1.7% | 558.84 | 551.28 / 547.00-553.31 | 15.37 (2.8%) | 540.59-639.47 | -7.3% / -3.6% | -8.0% | 7.1M |
| XLK | 186.64 (10:05 iex) | -1.3% | 189.19 | 188.34 / 186.18-188.54 | 3.26 (1.7%) | 184.84-203.25 | -3.5% / -0.3% | -4.3% | 7.8M |
| XLF | 55.87 (10:05 iex) | +1.1% | 55.27 | 55.59 / 55.55-56.02 | 0.69 (1.2%) | 52.81-56.20 | +1.5% / -1.7% | +1.9% | 39.1M |
| XLE | 67.26 (10:05 iex) | +1.1% | 66.56 | 67.11 / 67.02-67.56 | 1.28 (1.9%) | 60.95-67.90 | +4.5% / +5.5% | +2.0% | 32.3M |
| XLV | 177.84 (10:04 iex) | +0.4% | 177.19 | 178.20 / 177.25-178.28 | 2.96 (1.7%) | 165.19-178.86 | +4.4% / +4.6% | +5.4% | 8.6M |
| XLI | 169.35 (10:05 iex) | +0.9% | 167.89 | 168.23 / 167.90-169.73 | 2.56 (1.5%) | 164.66-172.34 | -0.7% / -3.6% | -0.3% | 7.4M |
| XLY | 114.35 (10:04 iex) | +0.8% | 113.41 | 114.41 / 113.92-114.68 | 1.31 (1.2%) | 107.99-113.56 | +2.2% / -0.4% | +1.5% | 6.4M |
| XLP | 87.74 (10:05 iex) | +1.2% | 86.68 | 87.34 / 87.22-87.86 | 1.16 (1.3%) | 80.10-88.47 | +5.0% / +3.6% | +3.9% | 11.5M |
| XLU | 42.15 (10:05 iex) | +1.2% | 41.65 | 41.84 / 41.62-42.17 | 0.66 (1.6%) | 39.03-42.20 | +2.8% / -0.5% | +1.4% | 35.2M |
| XLB | 51.31 (10:05 iex) | +1.5% | 50.56 | 50.87 / 50.80-51.49 | 0.74 (1.5%) | 47.81-50.70 | +2.1% / -1.0% | +2.6% | 11.7M |
| XLRE | 42.35 (10:05 iex) | +0.9% | 41.99 | 42.17 / 42.00-42.36 | 0.60 (1.4%) | 40.28-42.67 | +1.2% / -2.2% | +2.8% | 7.3M |
| XLC | 112.04 (10:05 iex) | -0.4% | 112.44 | 112.67 / 111.91-112.90 | 1.57 (1.4%) | 109.66-115.61 | +0.6% / +0.7% | +0.3% | 6.7M |
| KRE | 70.59 (10:05 iex) | +1.2% | 69.75 | 70.09 / 69.94-70.92 | 1.30 (1.9%) | 67.79-72.87 | -0.6% / -4.2% | +0.2% | 15.8M |
| XHB | 97.23 (10:02 iex) | +1.5% | 95.75 | 95.83 / 95.57-97.23 | 2.17 (2.3%) | 91.87-99.67 | -0.5% / -4.8% | +0.1% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 344.07 (10:05 iex) | +0.6% | 342.00 | 346.06 / 342.03-347.82 | 6.52 (1.9%) | 325.81-348.15 | +1.5% / +5.2% | +0.5% | 38.5M |
| MSFT | 536.87 (10:05 iex) | -0.5% | 539.44 | 541.31 / 534.84-543.82 | 11.35 (2.1%) | 491.10-551.15 | +4.0% / +6.9% | +3.2% | 23.1M |
| NVDA | 216.41 (10:05 iex) | -0.4% | 217.23 | 216.56 / 215.07-216.80 | 5.96 (2.7%) | 212.85-243.37 | -5.0% / -2.6% | -5.7% | 109.6M |
| AMZN | 253.27 (10:05 iex) | -0.6% | 254.76 | 255.09 / 252.90-255.54 | 5.76 (2.3%) | 244.72-263.70 | +0.5% / -1.1% | +0.3% | 36.4M |
| GOOGL | 344.36 (10:04 iex) | -1.4% | 349.22 | 348.01 / 344.17-350.66 | 8.45 (2.4%) | 335.51-364.17 | +0.7% / +1.3% | +0.3% | 26.2M |
| META | 727.79 (10:05 iex) | -1.2% | 736.72 | 736.16 / 726.17-738.49 | 22.31 (3.0%) | 660.28-779.82 | +0.4% / +12.9% | +2.2% | 22.2M |
| TSLA | 368.38 (10:05 iex) | +1.6% | 362.44 | 369.14 / 363.45-370.58 | 10.44 (2.9%) | 345.88-388.56 | -2.3% / +1.0% | -3.3% | 34.2M |
| AVGO | 338.17 (10:05 iex) | -1.8% | 344.33 | 338.49 / 336.22-339.59 | 11.29 (3.3%) | 334.61-380.84 | -3.5% / -6.2% | -4.4% | 23.1M |
| AMD | 544.59 (10:05 iex) | -3.1% | 562.23 | 547.23 / 540.40-550.96 | 26.22 (4.7%) | 530.09-658.52 | -8.1% / +4.8% | -9.4% | 21.8M |
| ORCL | 132.38 (10:05 iex) | -1.6% | 134.47 | 133.49 / 131.37-133.80 | 6.85 (5.1%) | 127.60-153.03 | -4.0% / -7.2% | -0.5% | 30.7M |
| NFLX | 71.24 (10:05 iex) | -1.9% | 72.61 | 69.86 / 69.76-71.90 | 1.65 (2.3%) | 66.54-73.87 | +3.2% / -3.4% | +1.5% | 38.7M |
| CRM | 244.18 (10:04 iex) | -1.0% | 246.74 | 250.57 / 243.94-251.94 | 8.43 (3.4%) | 220.29-247.18 | +5.9% / +7.8% | +8.3% | 9.7M |
| JPM | 341.34 (10:05 iex) | +1.7% | 335.53 | 339.45 / 338.25-343.75 | 5.96 (1.8%) | 324.25-352.74 | +0.1% / -3.3% | +1.2% | 8.7M |
| GS | 899.98 (10:05 iex) | +1.0% | 891.28 | 895.89 / 894.00-909.87 | 21.45 (2.4%) | 859.03-967.76 | -2.0% / -8.7% | +1.0% | 2.4M |
| BAC | 52.11 (10:05 iex) | +0.8% | 51.70 | 52.14 / 51.73-52.34 | 1.25 (2.4%) | 49.26-58.28 | -5.5% / -12.6% | -3.6% | 42.0M |
| XOM | 176.00 (10:03 iex) | +0.8% | 174.68 | 176.49 / 175.44-177.37 | 3.41 (2.0%) | 155.85-178.69 | +5.6% / +7.1% | +3.7% | 13.0M |
| CVX | 222.10 (10:05 iex) | +1.3% | 219.32 | 221.85 / 220.41-223.41 | 4.35 (2.0%) | 200.78-223.46 | +5.0% / +6.4% | +3.7% | 9.4M |
| LLY | 1,267.00 (10:04 iex) | +1.2% | 1,251.61 | 1,256.00 / 1,255.01-1,267.00 | 37.08 (3.0%) | 1,131.21-1,275.88 | +6.7% / +6.2% | +7.0% | 2.4M |
| UNH | 400.08 (10:05 iex) | -1.6% | 406.67 | 410.35 / 395.52-412.37 | 11.93 (2.9%) | 362.60-414.12 | +7.8% / +5.3% | +9.6% | 6.0M |
| JNJ | 257.01 (10:05 iex) | +1.5% | 253.28 | 255.52 / 254.13-257.27 | 6.46 (2.6%) | 245.17-275.23 | -3.4% / -4.4% | -1.2% | 7.9M |
| WMT | 119.08 (10:05 iex) | +1.0% | 117.87 | 118.07 / 118.07-119.48 | 2.57 (2.2%) | 103.39-121.38 | +8.1% / +8.4% | +6.6% | 22.9M |
| COST | 986.22 (10:05 iex) | +0.8% | 978.01 | 982.86 / 980.66-987.59 | 16.24 (1.7%) | 883.10-1,008.37 | +5.3% / +4.8% | +3.2% | 2.4M |
| HD | 312.58 (10:04 iex) | +1.4% | 308.24 | 309.66 / 308.32-314.57 | 6.45 (2.1%) | 277.15-309.10 | +5.6% / -1.5% | +4.3% | 5.8M |
| CAT | 741.59 (10:02 iex) | +0.8% | 735.64 | 734.36 / 730.00-742.55 | 30.24 (4.1%) | 704.01-876.95 | -9.1% / -9.8% | -7.6% | 2.6M |
| BA | 191.50 (10:05 iex) | +1.5% | 188.73 | 190.12 / 189.18-191.90 | 5.55 (2.9%) | 183.38-204.06 | -1.6% / -8.5% | +0.5% | 8.6M |
| DAL | 78.48 (10:04 iex) | +0.5% | 78.08 | 78.07 / 78.07-79.00 | 2.46 (3.1%) | 75.54-85.93 | -4.8% / -5.3% | -4.7% | 8.4M |
| UAL | 102.19 (10:03 iex) | +0.9% | 101.31 | 101.25 / 101.25-102.75 | 3.73 (3.7%) | 97.70-118.26 | -7.4% / -10.0% | -5.7% | 4.5M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-16 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| NBIZ | 33.40 (10:01 iex) | +12.5% | 29.68 | 31.95 / 31.77-33.90 | 3.29 (11.1%) | 17.01-37.98 | +32.8% / +7.1% | +31.2% | 2.2M |
| CWVX | 7.85 (09:58 iex) | -14.6% | 9.19 | 8.00 / 7.62-8.15 | 1.79 (19.4%) | 6.65-17.26 | -35.0% / -42.6% | -30.0% | 1.9M |
| CRWG | 9.32 (10:05 iex) | -15.2% | 10.99 | 9.59 / 9.22-9.76 | 2.15 (19.6%) | 7.96-20.68 | -35.1% / -42.8% | -30.2% | 3.4M |
| OMER | 16.08 (10:05 iex) | -14.4% | 18.79 | 17.94 / 16.05-17.94 | 0.73 (3.9%) | 17.68-21.24 | -2.1% / +3.1% | -1.7% | 1.2M |
| TLK | 11.04 (10:04 iex) | -13.7% | 12.78 | 10.86 / 10.60-11.17 | 0.26 (2.0%) | 12.38-14.28 | -2.2% / -9.5% | -0.8% | 1.2M |
| EIDO | 10.12 (10:04 iex) | -13.4% | 11.68 | 9.99 / 9.98-10.12 | 0.16 (1.3%) | 11.52-12.49 | -1.9% / -5.9% | +0.1% | 1.2M |
| CCOI | 7.26 (10:05 iex) | -13.1% | 8.35 | 8.12 / 7.23-8.14 | 0.76 (9.2%) | 7.13-10.30 | -1.5% / -10.2% | -12.7% | 2.2M |
