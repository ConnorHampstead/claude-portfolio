## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Tuesday 2026-10-13. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$100,530.97**
- Cash: $79,495.12
- Session P&L so far: +0.06% (new entries are blocked at -3.0%)
- Gross exposure: $39,232 (39% of equity, cap 150%)
- Net exposure: $+2,838 (+3%, cap +/-100%)
- Risk at stake (entry to stop): $1,002 (1.00% of equity, cap 4.0%) — 3.00% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| XOM | long | 121 | 171.98 | 173.84 | +225 (+1.1%) | 167.80 | 179.00 | Energy is the clear sector leader with XLE and XOM through 20-day highs. Geopolitical escalation risk keeps the oil prem |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| SMH | short | 31 | 587.00 | limit | 603.00 | 556.00 | 2026-10-13 |

### Record

17 closed trades: 5W / 12L, total -3.93R, net $+310 realized. Shorts taken: 15.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |
| NVDA | long | stop | -0.38R | $-235 | 40% |
| IWM | long | close | -1.16R | $-590 | 40% |
| JNJ | short | stop | -1.02R | $-550 | 38% |

### Ideas you passed on, replayed against the tape

28 resolved: 5 reached target first, 18 stop first, 4 never reached the entry, 1 expired, 0 ambiguous. Average -0.40R across the 24 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-13 pre-market | GS | long | Big revenue beat but -9.3% vs 50d; would be buying a gap against the trend, and  | stop | -0.91R | 38% |
| 2026-10-01 pre-market | MSFT | long | dropped by the caps: would be 9 positions and resting entries, cap is 8 | target | +1.71R | 40% |
| 2026-10-05 open | GS | short | Weak (-1.4%) and near 20d low 881, but a third rates-factor short on top of JNJ/ | stop | -1.64R | 35% |
| 2026-10-06 pre-market | GS | short | Bank earnings around 10/14 at the edge of the horizon; financials bouncing pre-m | stop | -1.22R | 34% |
| 2026-10-07 pre-market | TLT | short | Purest rates-trend trade, but it doubles the HD factor and works against the IWM | stop | -1.08R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| XOM | 173.81 (10:04 iex) | +1.0% | 172.15 | 173.44 / 172.65-174.05 | 3.29 (1.9%) | 155.85-172.55 | +5.1% / +6.5% | +5.0% | 13.0M |
| SMH | 583.57 (10:04 iex) | -1.3% | 590.99 | 578.01 / 574.75-584.12 | 13.27 (2.2%) | 540.11-639.47 | -1.4% / +2.0% | -6.8% | 6.2M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 777.46 (10:05 iex) | -0.1% | 778.10 | 777.34 / 777.16-778.75 | 6.25 (0.8%) | 747.74-781.62 | +1.2% / +1.5% | +0.4% | 43.7M |
| QQQ | 743.94 (10:04 iex) | -0.3% | 746.04 | 739.53 / 738.83-744.18 | 8.46 (1.1%) | 699.27-762.86 | +0.9% / +2.9% | -1.3% | 33.7M |
| IWM | 276.49 (10:05 iex) | -0.5% | 277.90 | 277.98 / 276.34-278.70 | 3.59 (1.3%) | 274.52-288.94 | -1.3% / -4.4% | -1.9% | 24.9M |
| DIA | 517.10 (10:05 iex) | -0.2% | 517.91 | 522.74 / 517.13-522.80 | 4.58 (0.9%) | 504.70-522.55 | +0.7% / -1.3% | +1.1% | 3.4M |
| TLT | 78.24 (10:05 iex) | +0.2% | 78.05 | 78.56 / 78.22-78.57 | 0.85 (1.1%) | 76.43-81.61 | -1.1% / -3.2% | +1.2% | 48.4M |
| GLD | 381.82 (10:04 iex) | -0.1% | 382.15 | 383.93 / 381.78-384.00 | 5.84 (1.5%) | 374.23-403.15 | -1.4% / -3.8% | +0.7% | 8.1M |
| USO | 151.27 (10:04 iex) | +0.2% | 151.03 | 150.10 / 149.84-151.37 | 5.34 (3.5%) | 141.76-163.35 | +1.2% / +8.2% | +4.9% | 5.7M |
| SMH | 583.57 (10:04 iex) | -1.3% | 590.99 | 578.01 / 574.75-584.12 | 13.27 (2.2%) | 540.11-639.47 | -1.4% / +2.0% | -6.8% | 6.2M |
| XLK | 196.04 (10:05 iex) | -0.2% | 196.36 | 194.20 / 193.92-196.14 | 2.77 (1.4%) | 182.21-203.25 | +0.7% / +3.7% | -2.3% | 7.3M |
| XLF | 54.67 (10:05 iex) | -0.7% | 55.05 | 55.42 / 54.66-55.65 | 0.62 (1.1%) | 52.81-56.79 | +0.8% / -2.3% | +2.2% | 38.0M |
| XLE | 66.60 (10:05 iex) | +0.9% | 66.01 | 66.50 / 66.29-66.81 | 1.25 (1.9%) | 60.95-66.42 | +4.3% / +5.5% | +4.0% | 34.0M |
| XLV | 169.86 (10:05 iex) | -1.2% | 171.99 | 172.36 / 169.70-172.79 | 2.63 (1.5%) | 165.19-172.03 | +1.9% / +2.0% | +2.8% | 8.0M |
| XLI | 167.75 (10:05 iex) | -0.8% | 169.15 | 168.74 / 167.74-168.89 | 2.32 (1.4%) | 166.18-172.34 | -0.0% / -3.4% | -0.6% | 7.3M |
| XLY | 112.22 (10:05 iex) | -0.0% | 112.27 | 112.30 / 112.21-112.92 | 1.31 (1.2%) | 107.99-113.29 | +1.4% / -1.7% | +1.7% | 6.7M |
| XLP | 84.20 (10:05 iex) | -0.2% | 84.41 | 85.02 / 84.16-85.12 | 0.99 (1.2%) | 80.10-84.41 | +2.7% / +0.9% | +4.2% | 10.7M |
| XLU | 41.11 (10:05 iex) | -1.2% | 41.63 | 41.80 / 41.09-41.81 | 0.63 (1.5%) | 39.03-41.64 | +3.0% / -0.8% | +4.2% | 33.8M |
| XLB | 49.41 (10:05 iex) | -0.1% | 49.44 | 49.70 / 49.39-49.91 | 0.71 (1.4%) | 47.81-50.88 | -0.3% / -3.3% | -0.1% | 11.5M |
| XLRE | 41.60 (10:05 iex) | -0.8% | 41.92 | 42.34 / 41.62-42.34 | 0.57 (1.4%) | 40.28-43.13 | +0.8% / -2.8% | +3.1% | 6.9M |
| XLC | 112.69 (10:05 iex) | +1.1% | 111.45 | 111.59 / 111.44-113.17 | 1.42 (1.3%) | 109.66-115.61 | -0.4% / -0.2% | -0.1% | 6.4M |
| KRE | 68.94 (10:05 iex) | -0.9% | 69.56 | 69.79 / 68.89-70.21 | 1.21 (1.7%) | 67.97-74.30 | -1.7% / -5.1% | -1.2% | 16.0M |
| XHB | 93.96 (10:04 iex) | -0.1% | 94.05 | 94.81 / 93.90-95.30 | 2.08 (2.2%) | 93.63-99.67 | -2.6% / -7.3% | -2.3% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.31 (10:05 iex) | +1.3% | 340.97 | 344.69 / 341.12-348.15 | 6.42 (1.9%) | 325.81-345.34 | +1.5% / +5.6% | +2.4% | 37.3M |
| MSFT | 550.82 (10:05 iex) | +1.8% | 541.15 | 544.64 / 544.28-551.13 | 12.21 (2.3%) | 487.23-542.74 | +5.7% / +7.9% | +3.0% | 22.2M |
| NVDA | 225.81 (10:05 iex) | -0.2% | 226.32 | 224.34 / 223.06-226.17 | 5.26 (2.3%) | 211.16-243.37 | -0.5% / +1.7% | -5.3% | 107.1M |
| AMZN | 262.05 (10:05 iex) | +1.0% | 259.53 | 259.44 / 259.19-262.80 | 5.57 (2.1%) | 244.30-263.70 | +2.9% / +0.3% | +3.2% | 36.7M |
| GOOGL | 356.41 (10:05 iex) | +1.0% | 352.72 | 356.06 / 353.49-358.55 | 8.10 (2.3%) | 335.51-364.17 | +1.9% / +1.9% | +1.8% | 25.6M |
| META | 768.22 (10:05 iex) | +3.4% | 742.96 | 735.99 / 734.84-771.15 | 22.46 (3.0%) | 655.68-779.82 | +2.8% / +15.5% | +0.1% | 22.0M |
| TSLA | 373.75 (10:05 iex) | -1.1% | 378.03 | 372.32 / 371.30-375.40 | 10.86 (2.9%) | 345.88-388.56 | +2.3% / +6.2% | -0.2% | 35.5M |
| AVGO | 355.80 (10:05 iex) | +0.3% | 354.73 | 349.27 / 348.11-356.10 | 10.31 (2.9%) | 335.20-380.84 | -0.3% / -4.3% | -2.1% | 23.3M |
| AMD | 590.10 (10:05 iex) | -0.7% | 594.24 | 577.50 / 570.60-590.76 | 22.42 (3.8%) | 497.51-658.52 | -1.5% / +11.9% | -5.9% | 21.7M |
| ORCL | 139.65 (10:05 iex) | +1.6% | 137.39 | 135.91 / 135.55-140.18 | 6.12 (4.5%) | 131.10-153.03 | -2.7% / -5.5% | -3.2% | 29.9M |
| NFLX | 71.01 (10:04 iex) | +0.6% | 70.61 | 71.16 / 70.84-71.52 | 1.47 (2.1%) | 66.54-79.48 | -0.8% / -6.2% | +4.6% | 37.4M |
| CRM | 244.79 (10:05 iex) | +4.6% | 233.92 | 236.00 / 234.70-244.78 | 7.72 (3.3%) | 220.29-261.87 | -0.2% / +3.6% | +1.8% | 10.4M |
| JPM | 331.57 (10:05 iex) | -0.8% | 334.30 | 339.97 / 331.56-344.36 | 4.91 (1.5%) | 324.25-353.83 | -0.9% / -4.0% | +1.1% | 8.5M |
| GS | 893.87 (10:05 iex) | -0.0% | 893.95 | 923.00 / 894.77-931.00 | 18.47 (2.1%) | 868.52-988.28 | -2.8% / -9.3% | +0.1% | 2.3M |
| BAC | 53.72 (10:05 iex) | -1.6% | 54.58 | 54.44 / 53.73-54.85 | 0.92 (1.7%) | 52.24-59.92 | -1.9% / -8.7% | +1.1% | 38.4M |
| XOM | 173.81 (10:04 iex) | +1.0% | 172.15 | 173.44 / 172.65-174.05 | 3.29 (1.9%) | 155.85-172.55 | +5.1% / +6.5% | +5.0% | 13.0M |
| CVX | 216.83 (10:04 iex) | +0.9% | 215.00 | 217.00 / 215.95-217.41 | 4.13 (1.9%) | 200.78-217.78 | +3.4% / +5.3% | +4.1% | 9.5M |
| LLY | 1,177.35 (10:04 iex) | -0.4% | 1,182.62 | 1,187.04 / 1,173.81-1,193.30 | 34.69 (2.9%) | 1,131.21-1,215.00 | +1.6% / +0.7% | +3.5% | 2.2M |
| UNH | 375.74 (10:05 iex) | -0.7% | 378.52 | 397.62 / 375.45-399.88 | 8.89 (2.3%) | 362.60-387.52 | +1.0% / -2.2% | -0.0% | 5.1M |
| JNJ | 250.24 (10:04 iex) | -5.1% | 263.73 | 254.56 / 250.00-256.18 | 5.10 (1.9%) | 251.17-275.23 | -0.3% / -0.5% | +4.3% | 6.9M |
| WMT | 114.11 (10:04 iex) | +0.9% | 113.08 | 114.22 / 113.87-114.83 | 2.24 (2.0%) | 103.39-113.14 | +4.9% / +4.3% | +7.6% | 21.8M |
| COST | 960.57 (10:04 iex) | +0.1% | 959.44 | 965.73 / 959.83-966.00 | 16.04 (1.7%) | 883.10-960.74 | +4.5% / +3.0% | +3.9% | 2.4M |
| HD | 291.42 (10:05 iex) | +0.3% | 290.62 | 295.00 / 291.18-296.60 | 6.23 (2.1%) | 277.15-311.13 | -0.7% / -7.9% | +3.4% | 5.6M |
| CAT | 777.85 (10:04 iex) | -2.7% | 799.37 | 791.00 / 774.64-792.70 | 25.53 (3.2%) | 774.48-876.95 | -1.8% / -2.7% | -5.8% | 2.4M |
| BA | 186.28 (10:05 iex) | -1.7% | 189.50 | 189.10 / 186.32-189.10 | 5.89 (3.1%) | 184.01-212.40 | -2.4% / -9.4% | -1.7% | 9.2M |
| DAL | 78.87 (10:04 iex) | -1.5% | 80.11 | 80.70 / 78.73-80.70 | 2.47 (3.1%) | 76.89-86.17 | -2.7% / -4.1% | -3.6% | 8.4M |
| UAL | 102.00 (10:05 iex) | -2.3% | 104.44 | 104.35 / 102.02-104.91 | 3.91 (3.7%) | 104.29-118.26 | -5.3% / -8.7% | -5.1% | 4.3M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-13 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BMBL | 5.96 (10:05 iex) | +56.7% | 3.80 | 5.98 / 5.95-5.98 | 0.20 (5.3%) | 2.44-3.98 | +38.8% / +36.0% | +49.0% | 4.1M |
| NBIZ | 27.41 (09:59 iex) | +11.4% | 24.60 | 26.87 / 26.59-27.41 | 2.64 (10.7%) | 17.01-27.94 | +11.4% / -15.9% | +17.2% | 2.3M |
| IREZ | 14.38 (10:04 iex) | +10.3% | 13.04 | 14.15 / 14.10-14.65 | 1.07 (8.2%) | 6.82-13.16 | +37.0% / +22.8% | +31.3% | 2.5M |
| VEEA | 5.26 (09:54 iex) | +14.1% | 4.61 | 4.65 / 4.65-5.50 | 1.11 (24.0%) | 2.08-8.88 | +12.4% / +49.3% | -19.4% | 24.1M |
| SKDD | 9.71 (10:03 iex) | +9.5% | 8.87 | 9.98 / 9.64-9.98 | 0.56 (6.4%) | 6.22-8.94 | +23.2% / -4.8% | +41.0% | 4.0M |
| CRMG | 8.82 (10:04 iex) | +8.9% | 8.10 | 8.28 / 8.16-8.85 | 0.52 (6.4%) | 7.21-10.37 | -1.8% / +2.6% | +2.9% | 1.2M |
| WFF | 9.01 (10:05 iex) | -47.9% | 17.28 | 14.90 / 8.32-15.55 | 4.54 (26.3%) | 1.75-50.60 | +400.7% / +562.5% | +654.6% | 9.5M |
| ASTX | 5.79 (10:04 iex) | -18.3% | 7.09 | 6.22 / 5.79-6.35 | 1.42 (20.1%) | 5.92-11.90 | -27.2% / -38.2% | -24.7% | 6.3M |
| SNDX | 13.68 (10:05 iex) | -17.3% | 16.55 | 14.61 / 13.49-14.74 | 0.81 (4.9%) | 16.37-18.94 | -6.5% / -12.7% | -7.2% | 2.0M |
| CIFR | 10.88 (10:05 iex) | -16.3% | 13.00 | 11.26 / 10.70-11.32 | 1.03 (7.9%) | 12.88-19.75 | -20.0% / -22.3% | -16.0% | 33.2M |
