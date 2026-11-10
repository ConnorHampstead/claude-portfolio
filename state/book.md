## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Tuesday 2026-11-10. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,660.32**
- Cash: $96,285.92
- Session P&L so far: -0.03% (new entries are blocked at -3.0%)
- Gross exposure: $31,298 (30% of equity, cap 150%)
- Net exposure: $-6,199 (-6%, cap +/-100%)
- Risk at stake (entry to stop): $1,017 (0.99% of equity, cap 4.0%) — 3.01% left for new plays
- Slots: 1 open + 2 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 265.60 | -204 (-3.1%) | 263.50 | 293.00 | Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong rela |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| DAL | long | 69 | 89.50 | limit | 85.80 | 96.50 | 2026-11-09 |
| QQQ | short | 29 | 646.50 | stop | 664.00 | 615.00 | 2026-11-09 |

### Record

46 closed trades: 15W / 31L, total +0.91R, net $+2,879 realized. Shorts taken: 38.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| AVGO | short | close | -0.92R | $-232 | 37% |
| NVDA | short | target | +2.15R | $+1,108 | 37% |
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |
| KRE | long | stop | -0.04R | $-10 | 37% |

### Ideas you passed on, replayed against the tape

106 resolved: 31 reached target first, 46 stop first, 20 never reached the entry, 9 expired, 0 ambiguous. Average +0.07R across the 86 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-27 pre-market | XLU | long | Defensive breakout against today's risk-on rotation; FOMC tomorrow; XLV already  | expired | +0.91R | 35% |
| 2026-10-27 pre-market | TLT | long | 20d-high breakout, but FOMC and PCE make the inflation side a coin flip. | expired | -0.07R | 33% |
| 2026-11-06 pre-market | XHB | short | Rate-repricing short on the hot payrolls; read-through not yet confirmed and I d | stop | -0.87R | 35% |
| 2026-11-06 open | XHB | short | Rate-repricing thesis weakened by softer UMich inflation expectations at 10:00. | stop | -0.84R | 30% |
| 2026-11-06 pre-market | AMD | short | Bounce-short candidate, but the 8.9% ATR makes the stop very wide and it duplica | stop | -0.79R | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMZN | 265.29 (09:02 iex) | -0.6% | 266.93 | 10.56 (4.0%) | 229.36-275.34 | +4.8% / +5.1% | +8.7% | 49.7M |
| DAL | 91.75 (08:49 sip) | -0.1% | 91.80 | 3.58 (3.9%) | 74.14-92.49 | +13.5% / +13.5% | +10.0% | 6.7M |
| QQQ | 671.02 (08:57 iex) | -1.2% | 679.35 | 17.62 (2.6%) | 647.05-744.20 | -3.5% / -5.6% | -0.3% | 51.4M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 747.95 (08:58 iex) | -0.6% | 752.69 | 11.98 (1.6%) | 732.71-778.75 | -1.2% / -1.6% | +0.1% | 48.7M |
| QQQ | 671.02 (08:57 iex) | -1.2% | 679.35 | 17.62 (2.6%) | 647.05-744.20 | -3.5% / -5.6% | -0.3% | 51.4M |
| IWM | 280.03 (09:02 iex) | -0.9% | 282.51 | 5.05 (1.8%) | 269.88-286.17 | +2.0% / +0.3% | +1.2% | 26.1M |
| DIA | 523.25 (08:49 sip) | -0.0% | 523.33 | 7.77 (1.5%) | 508.66-536.60 | +0.4% / +0.7% | +0.8% | 3.9M |
| TLT | 81.48 (08:51 iex) | -0.6% | 81.96 | 0.74 (0.9%) | 77.41-82.42 | +1.6% / +2.6% | +0.3% | 39.0M |
| GLD | 372.00 (08:49 sip) | -2.0% | 379.53 | 6.97 (1.8%) | 354.67-384.88 | +1.8% / -1.3% | +4.9% | 9.0M |
| USO | 138.44 (08:49 sip) | -3.0% | 142.66 | 6.04 (4.2%) | 139.44-171.82 | -10.1% / -6.4% | -9.1% | 5.5M |
| SMH | 476.50 (08:49 sip) | -2.2% | 487.41 | 25.35 (5.2%) | 445.59-588.68 | -8.3% / -13.6% | -4.1% | 12.0M |
| XLK | 168.65 (08:49 sip) | -1.3% | 170.88 | 5.72 (3.3%) | 162.14-196.34 | -6.2% / -9.1% | -1.9% | 12.6M |
| XLF | 58.10 (08:58 iex) | +0.2% | 57.99 | 1.01 (1.7%) | 54.02-60.04 | +2.9% / +3.8% | +0.7% | 36.4M |
| XLE | 61.19 (08:49 sip) | -1.2% | 61.94 | 1.82 (2.9%) | 60.85-70.15 | -7.4% / -4.6% | -7.9% | 37.4M |
| XLV | 189.10 (08:49 sip) | +0.4% | 188.33 | 3.77 (2.0%) | 169.48-192.32 | +4.2% / +8.5% | +2.0% | 11.6M |
| XLI | 166.68 (08:49 sip) | -1.3% | 168.89 | 3.48 (2.1%) | 161.74-172.40 | +0.8% / -0.2% | -0.5% | 9.2M |
| XLY | 120.55 (08:45 sip) | -0.4% | 121.01 | 2.63 (2.2%) | 110.67-122.92 | +4.6% / +6.8% | +2.4% | 9.3M |
| XLP | 91.33 (08:49 sip) | +0.5% | 90.89 | 1.79 (2.0%) | 84.11-93.40 | +2.8% / +6.9% | +0.1% | 19.5M |
| XLU | 43.65 (08:49 sip) | -0.3% | 43.79 | 0.64 (1.5%) | 41.09-44.09 | +2.6% / +5.0% | +0.3% | 28.3M |
| XLB | 52.77 (08:45 sip) | -0.3% | 52.94 | 1.01 (1.9%) | 49.23-54.63 | +2.3% / +4.1% | -1.4% | 12.5M |
| XLRE | 44.56 (08:45 sip) | -0.2% | 44.64 | 0.76 (1.7%) | 41.31-45.34 | +4.1% / +5.1% | +2.3% | 8.5M |
| XLC | 107.84 (08:45 sip) | +0.4% | 107.36 | 2.29 (2.1%) | 99.33-113.17 | +1.1% / -2.0% | +7.1% | 8.1M |
| KRE | 73.31 (08:49 sip) | -0.2% | 73.45 | 1.64 (2.2%) | 67.79-75.80 | +2.5% / +2.5% | -0.4% | 15.3M |
| XHB | 104.89 (08:40 sip) | -1.0% | 105.96 | 3.30 (3.1%) | 91.87-108.78 | +6.8% / +7.8% | +1.3% | 2.5M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 352.36 (08:50 iex) | +0.5% | 350.69 | 9.42 (2.7%) | 325.33-355.38 | +2.0% / +4.2% | +3.7% | 50.0M |
| MSFT | 542.88 (08:49 sip) | -0.4% | 545.18 | 16.54 (3.0%) | 504.96-559.15 | +2.6% / +5.4% | +7.5% | 26.2M |
| NVDA | 176.22 (09:04 iex) | -1.4% | 178.67 | 8.78 (4.9%) | 170.24-228.64 | -14.6% / -18.4% | -11.6% | 138.0M |
| AMZN | 265.29 (09:02 iex) | -0.6% | 266.93 | 10.56 (4.0%) | 229.36-275.34 | +4.8% / +5.1% | +8.7% | 49.7M |
| GOOGL | 287.50 (08:59 iex) | -0.2% | 288.15 | 11.66 (4.0%) | 276.92-359.40 | -8.3% / -13.1% | +3.3% | 40.0M |
| META | 637.82 (09:00 iex) | -0.6% | 641.37 | 24.74 (3.9%) | 583.80-771.27 | -2.5% / -5.1% | +5.7% | 24.9M |
| TSLA | 371.55 (08:49 sip) | -1.7% | 378.05 | 18.70 (4.9%) | 338.15-414.23 | -0.6% / +1.4% | -6.4% | 40.9M |
| AVGO | 312.74 (08:56 iex) | -2.1% | 319.48 | 16.50 (5.2%) | 289.77-359.25 | -3.3% / -7.9% | -0.9% | 25.0M |
| AMD | 497.81 (09:03 iex) | -2.1% | 508.58 | 41.07 (8.1%) | 402.10-606.20 | -2.8% / -7.1% | +8.9% | 29.4M |
| ORCL | 117.58 (08:49 sip) | -1.8% | 119.79 | 8.78 (7.3%) | 109.21-148.48 | -6.8% / -13.3% | +0.5% | 43.9M |
| NFLX | 63.90 (08:49 sip) | -0.1% | 63.95 | 2.12 (3.3%) | 61.39-73.07 | -3.0% / -9.5% | +2.6% | 47.2M |
| CRM | 214.60 (08:45 sip) | -0.2% | 214.94 | 9.16 (4.3%) | 211.00-252.42 | -8.6% / -9.9% | -5.0% | 7.3M |
| JPM | 343.60 (08:49 sip) | +0.4% | 342.08 | 8.01 (2.3%) | 326.40-359.80 | +1.4% / +0.4% | +0.4% | 7.6M |
| GS | 907.34 (08:49 sip) | +0.1% | 906.22 | 29.73 (3.3%) | 854.45-939.38 | +1.3% / -2.5% | +0.8% | 2.4M |
| BAC | 50.71 (08:49 sip) | +0.3% | 50.55 | 1.25 (2.5%) | 49.17-54.85 | -0.4% / -8.1% | +2.0% | 44.8M |
| XOM | 162.93 (08:49 sip) | -1.1% | 164.73 | 5.03 (3.1%) | 162.84-188.50 | -6.9% / -2.5% | -8.3% | 14.2M |
| CVX | 208.50 (08:45 sip) | -1.1% | 210.78 | 5.61 (2.7%) | 208.74-236.48 | -6.0% / -2.0% | -7.5% | 8.3M |
| LLY | 1,415.49 (08:49 sip) | +0.3% | 1,411.95 | 52.40 (3.7%) | 1,158.40-1,453.00 | +7.5% / +15.8% | +0.1% | 3.1M |
| UNH | 399.30 (08:49 sip) | +0.4% | 397.62 | 11.23 (2.8%) | 372.80-426.55 | -2.0% / +1.9% | -0.7% | 6.1M |
| JNJ | 284.39 (08:49 sip) | +0.8% | 282.11 | 7.83 (2.8%) | 245.17-282.73 | +6.2% / +6.0% | +4.3% | 8.2M |
| WMT | 126.55 (08:49 sip) | +0.7% | 125.66 | 3.18 (2.5%) | 112.21-131.82 | +3.7% / +11.3% | -1.6% | 23.0M |
| COST | 1,069.19 (08:45 sip) | +0.3% | 1,066.18 | 21.49 (2.0%) | 952.37-1,081.55 | +5.7% / +11.8% | +2.5% | 2.5M |
| HD | 352.00 (08:49 sip) | -0.4% | 353.42 | 10.48 (3.0%) | 289.57-362.44 | +9.0% / +14.1% | +3.6% | 4.8M |
| CAT | 573.00 (08:49 sip) | -4.3% | 598.88 | 31.73 (5.3%) | 550.81-790.82 | -11.2% / -20.7% | -2.4% | 3.9M |
| BA | 171.08 (08:49 sip) | -0.8% | 172.38 | 6.70 (3.9%) | 165.01-193.28 | -4.6% / -10.1% | -1.7% | 10.5M |
| DAL | 91.75 (08:49 sip) | -0.1% | 91.80 | 3.58 (3.9%) | 74.14-92.49 | +13.5% / +13.5% | +10.0% | 6.7M |
| UAL | 120.00 (08:49 sip) | -0.3% | 120.38 | 5.96 (5.0%) | 94.54-122.08 | +15.3% / +12.0% | +10.2% | 5.6M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-11-09 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| GFR | 7.72 (08:40 sip) | -0.1% | 7.73 | 0.46 (6.0%) | 5.41-7.81 | +17.9% / +21.7% | +25.7% | 1.7M |
| COHX | 10.18 (08:49 sip) | -11.4% | 11.49 | 2.22 (19.3%) | 5.88-21.97 | -9.6% / -42.0% | +18.5% | 1.7M |
| UVIX | 40.35 (08:58 iex) | +7.3% | 37.61 | 6.69 (17.8%) | 32.32-53.38 | -3.6% / -1.0% | -11.5% | 4.0M |
| DAMD | 9.86 (08:49 sip) | +4.2% | 9.46 | 2.02 (21.4%) | 8.97-16.68 | -16.6% / -16.8% | -30.2% | 4.1M |
| BEZ | 7.75 (08:49 sip) | +9.6% | 7.07 | 1.70 (24.1%) | 5.31-10.82 | -2.6% / +7.9% | -12.8% | 5.8M |
