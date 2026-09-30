## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (13:05 UTC), Wednesday 2026-09-30. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$101,541.77**
- Cash: $140,283.64
- Session P&L so far: -0.30% (new entries are blocked at -3.0%)
- Gross exposure: $92,705 (91% of equity, cap 150%)
- Net exposure: $-34,748 (-34%, cap +/-100%)
- Risk at stake (entry to stop): $3,282 (3.23% of equity, cap 4.0%) — 0.77% left for new plays
- Slots: 3 open + 4 resting entries of 8 — you may add at most 1 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| BA | short | 33 | 187.31 | 192.50 | -171 (-2.8%) | 194.90 | 176.00 | Safety headline on the MAX and a broken 20d floor, -7.6% vs 50d. A trade below today's 187.58 low means the opening rang |
| BAC | short | 267 | 55.80 | 55.10 | +187 (+1.3%) | 57.70 | 52.90 | Weakest large bank (-7.5% vs 20d avg). A break below today's opening low confirms the 20d-low support failed and opens a |
| HD | short | 61 | 289.30 | 289.80 | -30 (-0.2%) | 297.60 | 278.00 | Cleanest equity expression of frozen housing under 7%+ mortgages; -9.9% vs 50d with fresh 52-week lows. A trade below 28 |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XLU | short | 423 | 38.95 | stop | 40.15 | 37.55 | 2026-09-29 |
| DAL | long | 149 | 85.80 | stop | 82.40 | 90.50 | 2026-09-29 |
| NVDA | long | 69 | 234.70 | stop | 227.40 | 246.00 | 2026-09-28 |
| ORCL | short | 65 | 130.90 | stop | 138.60 | 119.00 | 2026-09-28 |

### Record

4 closed trades: 2W / 2L, total +0.57R, net $+1,558 realized. Shorts taken: 5.

### Last 4 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| DAL | long | stop | +1.00R | $+999 | 46% |
| LLY | long | stop | +1.76R | $+1,654 | 52% |
| ROST | long | stop | -1.18R | $-336 | 47% |
| ANET | long | stop | -1.01R | $-758 | 45% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| BA | 192.39 (08:49 sip) | +2.5% | 187.68 | 6.57 (3.5%) | 184.01-215.29 | -7.4% / -12.0% | -5.1% | 7.5M |
| BAC | 55.02 (08:49 sip) | +0.1% | 54.96 | 1.33 (2.4%) | 54.73-63.83 | -7.3% / -10.1% | -2.2% | 36.6M |
| HD | 290.00 (08:40 sip) | +0.7% | 288.04 | 6.44 (2.2%) | 287.34-324.44 | -5.5% / -11.0% | -5.7% | 4.7M |
| XLU | 39.80 (08:49 sip) | +0.2% | 39.71 | 0.58 (1.5%) | 39.03-43.39 | -3.7% / -7.2% | -2.0% | 24.8M |
| DAL | 85.10 (08:49 sip) | +0.3% | 84.87 | 2.47 (2.9%) | 75.99-85.47 | +5.4% / +1.0% | +1.1% | 7.1M |
| NVDA | 228.64 (08:50 iex) | +0.6% | 227.21 | 5.37 (2.4%) | 208.93-234.50 | +2.1% / +4.8% | -0.7% | 113.6M |
| ORCL | 136.58 (08:49 sip) | -0.9% | 137.79 | 7.70 (5.6%) | 131.58-170.70 | -6.4% / -3.4% | -7.6% | 35.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 766.74 (08:49 sip) | +0.3% | 764.20 | 6.97 (0.9%) | 747.74-775.14 | +0.0% / +0.4% | -1.2% | 44.0M |
| QQQ | 741.39 (09:05 iex) | +0.5% | 737.93 | 9.99 (1.4%) | 699.27-748.35 | +2.1% / +3.4% | -1.3% | 33.4M |
| IWM | 280.11 (08:49 sip) | +0.4% | 279.01 | 3.60 (1.3%) | 277.41-295.41 | -2.7% / -4.7% | -2.9% | 23.2M |
| DIA | 514.16 (08:49 sip) | +0.2% | 512.88 | 5.01 (1.0%) | 510.42-536.38 | -1.5% / -2.5% | -1.0% | 3.4M |
| TLT | 78.27 (09:04 iex) | +0.1% | 78.23 | 0.83 (1.1%) | 77.84-82.50 | -3.3% / -4.3% | -4.3% | 40.1M |
| GLD | 386.39 (08:56 iex) | +0.9% | 382.89 | 7.25 (1.9%) | 376.88-413.54 | -3.4% / -3.3% | -4.3% | 9.7M |
| USO | 145.90 (08:49 sip) | +1.8% | 143.35 | 6.18 (4.3%) | 136.09-163.35 | -4.3% / +5.0% | -0.5% | 6.6M |
| SMH | 608.24 (08:49 sip) | +0.2% | 606.90 | 16.16 (2.7%) | 537.73-613.27 | +5.8% / +6.9% | -0.1% | 6.5M |
| XLK | 195.30 (08:49 sip) | +0.4% | 194.50 | 3.27 (1.7%) | 181.87-196.94 | +2.8% / +5.1% | -0.9% | 6.9M |
| XLF | 54.17 (08:49 sip) | +0.3% | 54.01 | 0.75 (1.4%) | 53.72-58.39 | -3.7% / -4.9% | -1.4% | 36.5M |
| XLE | 61.88 (08:49 sip) | +0.6% | 61.54 | 1.31 (2.1%) | 60.95-65.78 | -3.2% / -0.1% | -0.4% | 34.1M |
| XLV | 170.47 (08:45 sip) | -0.2% | 170.73 | 2.24 (1.3%) | 164.48-173.82 | +1.1% / +1.9% | +0.5% | 7.7M |
| XLI | 169.40 (08:35 sip) | +0.2% | 169.13 | 2.30 (1.4%) | 167.04-175.30 | -0.9% / -4.5% | -0.7% | 7.7M |
| XLY | 108.92 (07:10 sip) | -0.2% | 109.15 | 1.54 (1.4%) | 108.68-116.81 | -2.5% / -4.6% | -2.8% | 6.4M |
| XLP | 82.16 (08:49 sip) | +0.4% | 81.85 | 0.88 (1.1%) | 81.29-85.60 | -1.4% / -2.7% | -1.1% | 10.8M |
| XLU | 39.80 (08:49 sip) | +0.2% | 39.71 | 0.58 (1.5%) | 39.03-43.39 | -3.7% / -7.2% | -2.0% | 24.8M |
| XLB | 49.31 (08:35 sip) | +0.4% | 49.10 | 0.69 (1.4%) | 48.91-53.27 | -3.1% / -4.6% | -2.8% | 11.2M |
| XLRE | 41.56 (08:49 sip) | +0.5% | 41.34 | 0.51 (1.2%) | 41.07-44.02 | -3.0% / -5.7% | -2.7% | 5.6M |
| XLC | 111.64 (07:40 sip) | +0.2% | 111.47 | 1.92 (1.7%) | 109.95-115.61 | -0.7% / +0.4% | -1.8% | 5.5M |
| KRE | 70.11 (08:45 sip) | +0.4% | 69.83 | 1.26 (1.8%) | 69.45-75.07 | -3.7% / -6.0% | -1.9% | 14.2M |
| XHB | 97.80 (08:00 sip) | +0.9% | 96.97 | 2.12 (2.2%) | 95.26-102.95 | -1.3% / -6.1% | -2.5% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 330.50 (08:49 sip) | +0.3% | 329.40 | 6.78 (2.1%) | 309.90-345.34 | -0.5% / +2.3% | -3.0% | 42.6M |
| MSFT | 510.51 (08:54 iex) | +0.3% | 508.96 | 11.73 (2.3%) | 486.00-519.40 | +1.8% / +6.1% | +2.2% | 21.1M |
| NVDA | 228.64 (08:50 iex) | +0.6% | 227.21 | 5.37 (2.4%) | 208.93-234.50 | +2.1% / +4.8% | -0.7% | 113.6M |
| AMZN | 247.00 (08:49 sip) | +0.1% | 246.67 | 5.22 (2.1%) | 244.30-261.12 | -2.4% / -3.7% | -3.3% | 33.9M |
| GOOGL | 345.34 (08:49 sip) | +1.3% | 340.92 | 8.49 (2.5%) | 327.74-364.17 | -0.3% / -0.9% | -2.9% | 26.1M |
| META | 731.81 (08:49 sip) | -0.9% | 738.79 | 29.93 (4.1%) | 555.66-779.82 | +9.3% / +19.4% | +0.3% | 24.1M |
| TSLA | 351.80 (08:49 sip) | -0.3% | 352.84 | 11.00 (3.1%) | 349.92-386.83 | -3.4% / +1.6% | -6.9% | 38.8M |
| AVGO | 357.73 (08:49 sip) | +0.7% | 355.10 | 9.91 (2.8%) | 335.20-372.02 | -0.2% / -5.3% | -2.6% | 27.5M |
| AMD | 608.00 (08:49 sip) | +0.1% | 607.57 | 26.04 (4.3%) | 440.50-639.00 | +12.1% / +19.4% | -2.6% | 22.2M |
| ORCL | 136.58 (08:49 sip) | -0.9% | 137.79 | 7.70 (5.6%) | 131.58-170.70 | -6.4% / -3.4% | -7.6% | 35.8M |
| NFLX | 69.96 (08:49 sip) | -0.5% | 70.30 | 2.14 (3.0%) | 68.88-83.60 | -7.0% / -7.0% | -2.6% | 33.3M |
| CRM | 226.80 (08:49 sip) | +0.7% | 225.31 | 8.07 (3.6%) | 221.18-267.80 | -8.0% / +4.5% | -3.4% | 13.0M |
| JPM | 335.55 (09:01 iex) | +0.2% | 334.98 | 7.09 (2.1%) | 333.33-362.86 | -4.1% / -5.2% | -1.5% | 8.0M |
| GS | 919.01 (08:45 sip) | +0.3% | 916.24 | 27.06 (3.0%) | 903.85-1,043.84 | -6.2% / -9.5% | -3.5% | 2.1M |
| BAC | 55.02 (08:49 sip) | +0.1% | 54.96 | 1.33 (2.4%) | 54.73-63.83 | -7.3% / -10.1% | -2.2% | 36.6M |
| XOM | 162.50 (08:49 sip) | +0.7% | 161.35 | 3.82 (2.4%) | 155.85-169.64 | -0.9% / +1.1% | +1.7% | 14.1M |
| CVX | 205.44 (08:49 sip) | +0.5% | 204.38 | 4.59 (2.2%) | 200.78-217.78 | -2.4% / +1.7% | +1.0% | 10.0M |
| LLY | 1,185.90 (08:49 sip) | +0.1% | 1,184.63 | 28.54 (2.4%) | 1,113.29-1,197.79 | +2.8% / +0.6% | +1.2% | 2.3M |
| UNH | 375.40 (08:49 sip) | +0.1% | 374.94 | 8.07 (2.2%) | 366.00-404.04 | -2.0% / -5.2% | +0.5% | 5.1M |
| JNJ | 267.95 (08:10 sip) | +0.1% | 267.57 | 5.02 (1.9%) | 260.68-281.07 | -0.9% / +0.9% | -0.6% | 6.3M |
| WMT | 107.18 (08:49 sip) | +0.4% | 106.80 | 2.04 (1.9%) | 104.66-111.23 | -0.6% / -2.1% | -3.0% | 22.2M |
| COST | 923.70 (08:35 sip) | -0.1% | 924.59 | 14.43 (1.6%) | 883.10-952.10 | +1.6% / -1.0% | +2.8% | 2.4M |
| HD | 290.00 (08:40 sip) | +0.7% | 288.04 | 6.44 (2.2%) | 287.34-324.44 | -5.5% / -11.0% | -5.7% | 4.7M |
| CAT | 833.00 (09:01 iex) | +0.8% | 826.64 | 20.67 (2.5%) | 771.39-830.50 | +2.6% / -0.1% | +2.3% | 2.4M |
| BA | 192.39 (08:49 sip) | +2.5% | 187.68 | 6.57 (3.5%) | 184.01-215.29 | -7.4% / -12.0% | -5.1% | 7.5M |
| DAL | 85.10 (08:49 sip) | +0.3% | 84.87 | 2.47 (2.9%) | 75.99-85.47 | +5.4% / +1.0% | +1.1% | 7.1M |
| UAL | 113.00 (08:35 sip) | +0.3% | 112.65 | 4.25 (3.8%) | 104.15-118.26 | +2.7% / -3.0% | -2.2% | 3.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-09-29 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IOVA | 14.47 (08:49 sip) | +0.1% | 14.45 | 0.89 (6.1%) | 7.97-15.30 | +48.0% / +87.1% | +35.8% | 17.2M |
| QURE | 24.86 (08:49 sip) | +1.4% | 24.51 | 3.16 (12.9%) | 22.47-50.97 | -42.7% / -44.5% | -45.9% | 2.8M |
