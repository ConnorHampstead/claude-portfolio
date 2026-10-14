Produce today's pre-market brief.

You are running unattended. No one will review this before it reaches the account,
so everything below matters more than it would in a conversation:

- **Search before you write anything.** Your training data is stale by default.
  Overnight moves, pre-market gaps, today's economic calendar, earnings due today,
  and news since the previous close all need to be looked up, not recalled.
- **Never state a price you have not verified this session.** Any entry more than
  10% from the last traded price is rejected automatically, so a fabricated level
  costs you the trade. If you could not confirm a current price for a symbol,
  leave that play out and say so in the brief.
- **Work from the clock in the book state below.** It gives the current time and
  when the cash session opens. Every release scheduled before that time has
  already printed: look up the actual figure and how futures reacted, and reason
  from it. Only what is still ahead of you is consensus.
- **Look at both sides.** Name the best long and the best short you found, with
  levels, whether or not you take them. A view held at lower conviction is a probe
  at `risk_pct` 0.25, not a pass. What you do pass on with real levels goes in
  `passed`, where it is scored against what the tape did.
- **Anything conditional is an order now, or a note for the review.** The only
  later look today is the post-open review at about 10:05 ET; after it nothing
  runs until tomorrow. A decision that waits on the open or the 10:00 data goes
  in "For the post-open review" with its levels. Anything later is an order now:
  "if it holds X" is a resting limit at X, "if it breaks Y" a stop entry at Y. A
  plan that only lives in the prose never executes.
- **Respect the caps in the book state below.** They count resting entries as if
  filled. Plays are admitted highest conviction first and the rest are dropped,
  so the book state's room figures are what you have to work with.
- **Choose a risk tier, not a size.** Give entry, stop, target and `risk_pct`.
  Share count is derived from your stop and tier against live equity.
- **A stop or target change you only describe in prose does not happen.** Any
  adjustment to an open position or a resting entry — new stop, new target, an
  exit, or a cancel — must also appear in the `manage` array of the JSON block,
  including on a `no_trade` day. The stops shown in the book state below are the
  live resting orders.

Write the full prose brief as specified, then the JSON block. The prose is the
permanent record of your reasoning and is committed to a public repository, so
write it to be read months from now by someone checking whether your stated
reasoning matched what actually happened. That applies to what you pass on as
much as to what you trade.

Your probability estimates are scored against outcomes. Spread them according to
what you actually believe rather than clustering everything near 60% — a brief
where every play is 65% carries no information and will score no better than a
coin flip.

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (13:05 UTC), Wednesday 2026-10-14. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$100,980.02**
- Cash: $97,690.93
- Session P&L so far: +0.45% (new entries are blocked at -3.0%)
- Gross exposure: $39,073 (39% of equity, cap 150%)
- Net exposure: $+3,289 (+3%, cap +/-100%)
- Risk at stake (entry to stop): $1,002 (0.99% of equity, cap 4.0%) — 3.01% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| SMH | short | 31 | 587.00 | 577.16 | +305 (+1.7%) | 603.00 | 556.00 | Semis are -6.8% over 5 days and below their 20d average while the memory complex is being repriced. A bounce toward the  |
| XOM | long | 121 | 171.98 | 175.05 | +371 (+1.8%) | 167.80 | 179.00 | Energy is the clear sector leader with XLE and XOM through 20-day highs. Geopolitical escalation risk keeps the oil prem |

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

31 resolved: 6 reached target first, 19 stop first, 5 never reached the entry, 1 expired, 0 ambiguous. Average -0.37R across the 26 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-07 pre-market | KRE | short | Bank earnings start 10/13, inside the horizon. | never filled | - | 33% |
| 2026-10-13 pre-market | AMD | short | Same chip factor as the SMH short; wider ATR and would be shorting into the gap. | stop | -1.17R | 35% |
| 2026-10-13 pre-market | JNJ | short | Down on patent-cliff worry despite raising guidance; shorting a guidance raise,  | target | +1.07R | 33% |
| 2026-10-13 pre-market | GS | long | Big revenue beat but -9.3% vs 50d; would be buying a gap against the trend, and  | stop | -0.91R | 38% |
| 2026-10-01 pre-market | MSFT | long | dropped by the caps: would be 9 positions and resting entries, cap is 8 | target | +1.71R | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SMH | 579.10 (08:49 sip) | -1.5% | 588.12 | 13.45 (2.3%) | 540.45-639.47 | -2.3% / +1.4% | -7.0% | 6.3M |
| XOM | 175.22 (08:49 sip) | +0.7% | 174.08 | 3.24 (1.9%) | 155.85-174.89 | +6.1% / +7.4% | +5.8% | 13.0M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 775.93 (08:49 sip) | -0.3% | 778.01 | 5.96 (0.8%) | 747.74-781.62 | +1.1% / +1.4% | -0.1% | 42.7M |
| QQQ | 738.24 (09:05 iex) | -0.7% | 743.57 | 8.31 (1.1%) | 699.27-762.86 | +0.3% / +2.4% | -2.1% | 33.8M |
| IWM | 273.64 (08:49 sip) | -1.1% | 276.70 | 3.44 (1.2%) | 274.52-288.94 | -1.6% / -4.7% | -1.6% | 25.0M |
| DIA | 515.44 (08:49 sip) | -0.1% | 516.21 | 4.83 (0.9%) | 504.70-522.80 | +0.4% / -1.6% | +0.3% | 3.4M |
| TLT | 77.81 (08:49 sip) | -0.7% | 78.37 | 0.78 (1.0%) | 76.43-81.61 | -0.6% / -2.7% | +1.4% | 48.1M |
| GLD | 376.25 (08:49 sip) | -1.4% | 381.67 | 5.53 (1.4%) | 374.23-403.15 | -1.3% / -4.0% | -0.2% | 8.0M |
| USO | 154.66 (08:49 sip) | +1.0% | 153.09 | 5.24 (3.4%) | 141.76-159.36 | +2.9% / +9.2% | +5.6% | 5.5M |
| SMH | 579.10 (08:49 sip) | -1.5% | 588.12 | 13.45 (2.3%) | 540.45-639.47 | -2.3% / +1.4% | -7.0% | 6.3M |
| XLK | 194.57 (08:49 sip) | -0.9% | 196.28 | 2.74 (1.4%) | 182.21-203.25 | +0.3% / +3.5% | -2.8% | 7.3M |
| XLF | 54.30 (08:49 sip) | -0.9% | 54.82 | 0.65 (1.2%) | 52.81-56.65 | +0.5% / -2.6% | +1.5% | 38.7M |
| XLE | 67.71 (08:52 iex) | +0.8% | 67.20 | 1.25 (1.9%) | 60.95-67.25 | +6.0% / +7.1% | +5.4% | 33.7M |
| XLV | 170.55 (08:49 sip) | +0.5% | 169.66 | 2.66 (1.6%) | 165.19-172.79 | +0.4% / +0.5% | +1.5% | 8.1M |
| XLI | 167.20 (08:45 sip) | -0.9% | 168.67 | 2.40 (1.4%) | 166.18-172.34 | -0.3% / -3.6% | -1.7% | 7.2M |
| XLY | 111.96 (08:49 sip) | -0.4% | 112.36 | 1.22 (1.1%) | 107.99-113.29 | +1.4% / -1.5% | +0.6% | 6.4M |
| XLP | 84.56 (08:49 sip) | +0.4% | 84.19 | 1.01 (1.2%) | 80.10-85.12 | +2.4% / +0.7% | +2.9% | 10.5M |
| XLU | 41.80 (08:49 sip) | -0.2% | 41.87 | 0.63 (1.5%) | 39.03-41.95 | +3.5% / -0.1% | +1.7% | 33.9M |
| XLB | 49.52 (08:45 sip) | -0.4% | 49.72 | 0.72 (1.4%) | 47.81-50.88 | +0.3% / -2.7% | -0.0% | 11.4M |
| XLRE | 41.68 (08:49 sip) | -0.4% | 41.83 | 0.58 (1.4%) | 40.28-43.13 | +0.7% / -2.9% | +1.8% | 6.9M |
| XLC | 112.19 (08:49 sip) | -0.1% | 112.28 | 1.45 (1.3%) | 109.66-115.61 | +0.4% / +0.5% | +0.6% | 6.5M |
| KRE | 68.11 (08:49 sip) | -1.4% | 69.06 | 1.24 (1.8%) | 67.97-73.75 | -2.1% / -5.6% | -1.4% | 15.8M |
| XHB | 93.03 (08:49 sip) | -1.7% | 94.63 | 2.03 (2.1%) | 93.63-99.67 | -1.9% / -6.5% | -2.8% | 1.8M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 344.00 (09:02 iex) | +0.8% | 341.27 | 6.49 (1.9%) | 325.81-348.15 | +1.5% / +5.4% | +2.3% | 37.6M |
| MSFT | 544.70 (08:59 iex) | +0.2% | 543.45 | 11.95 (2.2%) | 487.23-551.15 | +5.7% / +8.1% | +2.7% | 22.5M |
| NVDA | 225.77 (09:00 iex) | -1.2% | 228.52 | 5.31 (2.3%) | 212.50-243.37 | +0.1% / +2.5% | -4.5% | 106.9M |
| AMZN | 258.65 (08:56 iex) | +0.0% | 258.58 | 5.37 (2.1%) | 244.30-263.70 | +2.3% / +0.1% | +0.9% | 36.2M |
| GOOGL | 357.17 (08:52 iex) | +1.0% | 353.78 | 7.62 (2.2%) | 335.51-364.17 | +2.1% / +2.3% | +1.8% | 25.7M |
| META | 756.38 (08:59 iex) | -0.8% | 762.50 | 23.11 (3.0%) | 660.28-779.82 | +4.8% / +17.9% | +3.2% | 22.2M |
| TSLA | 372.80 (08:49 sip) | -0.6% | 375.23 | 10.69 (2.8%) | 345.88-388.56 | +1.3% / +5.1% | -1.4% | 34.9M |
| AVGO | 354.04 (08:55 iex) | -0.9% | 357.31 | 10.35 (2.9%) | 335.20-380.84 | +0.2% / -3.4% | -4.9% | 22.9M |
| AMD | 593.20 (08:49 sip) | -2.0% | 605.53 | 23.77 (3.9%) | 506.05-658.52 | -0.4% / +13.5% | -6.8% | 21.7M |
| ORCL | 139.89 (08:49 sip) | -2.3% | 143.20 | 6.39 (4.5%) | 131.10-153.03 | +1.3% / -1.5% | -0.7% | 29.6M |
| NFLX | 70.88 (08:49 sip) | +0.6% | 70.46 | 1.45 (2.1%) | 66.54-77.80 | -0.5% / -6.4% | +2.6% | 37.4M |
| CRM | 236.98 (08:49 sip) | -0.4% | 238.01 | 7.96 (3.3%) | 220.29-255.95 | +1.9% / +4.9% | +5.8% | 10.2M |
| JPM | 327.94 (09:00 iex) | -1.1% | 331.43 | 5.53 (1.7%) | 324.25-353.83 | -1.5% / -4.7% | +0.0% | 8.5M |
| GS | 878.65 (08:49 sip) | -1.5% | 891.91 | 19.81 (2.2%) | 868.52-984.66 | -2.6% / -9.2% | -0.6% | 2.4M |
| BAC | 49.94 (08:49 sip) | -7.5% | 53.96 | 0.95 (1.8%) | 52.24-59.39 | -2.5% / -9.5% | -0.2% | 38.1M |
| XOM | 175.22 (08:49 sip) | +0.7% | 174.08 | 3.24 (1.9%) | 155.85-174.89 | +6.1% / +7.4% | +5.8% | 13.0M |
| CVX | 219.55 (08:49 sip) | +0.8% | 217.73 | 4.07 (1.9%) | 200.78-218.79 | +4.7% / +6.3% | +4.9% | 9.4M |
| LLY | 1,173.91 (08:49 sip) | +0.6% | 1,166.51 | 34.12 (2.9%) | 1,131.21-1,215.00 | +0.1% / -0.7% | +0.8% | 2.2M |
| UNH | 378.79 (08:49 sip) | +0.3% | 377.76 | 10.33 (2.7%) | 362.60-399.88 | +0.8% / -2.2% | +0.4% | 5.5M |
| JNJ | 249.85 (08:49 sip) | +0.5% | 248.61 | 6.03 (2.4%) | 245.17-275.23 | -5.7% / -6.2% | -2.4% | 7.5M |
| WMT | 113.11 (08:49 sip) | +0.7% | 112.28 | 2.30 (2.0%) | 103.39-114.83 | +3.9% / +3.5% | +4.7% | 21.8M |
| COST | 961.00 (08:45 sip) | +0.7% | 954.63 | 16.04 (1.7%) | 883.10-966.00 | +3.7% / +2.5% | +2.0% | 2.3M |
| HD | 291.51 (08:49 sip) | -0.8% | 293.92 | 6.04 (2.1%) | 277.15-310.40 | +0.6% / -6.6% | +2.5% | 5.6M |
| CAT | 763.00 (08:49 sip) | -1.3% | 772.78 | 27.37 (3.5%) | 755.31-876.95 | -5.0% / -5.8% | -10.5% | 2.5M |
| BA | 185.75 (08:49 sip) | -0.4% | 186.49 | 5.69 (3.1%) | 184.01-212.22 | -3.4% / -10.5% | -1.8% | 9.3M |
| DAL | 78.50 (08:49 sip) | -1.3% | 79.57 | 2.46 (3.1%) | 76.89-86.17 | -3.4% / -4.4% | -4.9% | 8.4M |
| UAL | 101.19 (08:49 sip) | -2.0% | 103.23 | 3.79 (3.7%) | 101.77-118.26 | -6.2% / -9.3% | -7.7% | 4.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-13 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| BMBL | 5.94 (08:49 sip) | -0.2% | 5.95 | 0.34 (5.8%) | 2.44-5.98 | +106.3% / +108.7% | +137.1% | 9.8M |
