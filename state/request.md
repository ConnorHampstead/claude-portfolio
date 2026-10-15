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

- Time now: **09:05 ET** (13:05 UTC), Thursday 2026-10-15. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,353.25**
- Cash: $128,264.78
- Session P&L so far: +0.56% (new entries are blocked at -3.0%)
- Gross exposure: $69,012 (67% of equity, cap 150%)
- Net exposure: $-25,912 (-25%, cap +/-100%)
- Risk at stake (entry to stop): $896 (0.88% of equity, cap 4.0%) — 3.12% left for new plays
- Slots: 3 open + 0 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| IWM | short | 112 | 272.99 | 271.74 | +140 (+0.5%) | 277.50 | 267.00 | Small caps are the most rate-sensitive index; IWM opened below its 20d low 274.52 and is pinned at the session low, -4.7 |
| SMH | short | 31 | 587.00 | 549.25 | +1,170 (+6.4%) | 595.00 | 556.00 | Semis are -6.8% over 5 days and below their 20d average while the memory complex is being repriced. A bounce toward the  |
| XOM | long | 121 | 171.98 | 178.10 | +741 (+3.6%) | 170.80 | 179.00 | Energy is the clear sector leader with XLE and XOM through 20-day highs. Geopolitical escalation risk keeps the oil prem |

### Record

17 closed trades: 5W / 12L, total -3.93R, net $+310 realized. Shorts taken: 16.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |
| NVDA | long | stop | -0.38R | $-235 | 40% |
| IWM | long | close | -1.16R | $-590 | 40% |
| JNJ | short | stop | -1.02R | $-550 | 38% |

### Ideas you passed on, replayed against the tape

34 resolved: 7 reached target first, 21 stop first, 5 never reached the entry, 1 expired, 0 ambiguous. Average -0.36R across the 29 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-14 open | BAC | short | Morning plan: stand aside below 49.5; -8.6% with no bounce to sell. | stop | -0.96R | 35% |
| 2026-10-12 open | SMH | short | Weakest group today but still uptrend vs 50d; stop ~1 ATR is noise and short rec | target | +1.34R | 35% |
| 2026-10-13 open | UNH | short | The beat-and-raise gap fully reversed below yesterday's close, but I found no he | stop | -1.15R | 34% |
| 2026-10-07 pre-market | KRE | short | Bank earnings start 10/13, inside the horizon. | never filled | - | 33% |
| 2026-10-13 pre-market | AMD | short | Same chip factor as the SMH short; wider ATR and would be shorting into the gap. | stop | -1.17R | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IWM | 271.61 (08:49 sip) | +0.1% | 271.37 | 3.67 (1.4%) | 270.35-288.94 | -3.3% / -6.3% | -2.3% | 25.5M |
| SMH | 548.89 (08:58 iex) | -2.8% | 564.74 | 14.30 (2.5%) | 557.56-639.47 | -6.3% / -2.6% | -9.6% | 6.6M |
| XOM | 178.10 (08:49 sip) | +0.6% | 177.01 | 3.21 (1.8%) | 155.85-177.43 | +7.4% / +8.9% | +7.9% | 13.0M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 767.12 (09:04 iex) | -0.3% | 769.60 | 6.36 (0.8%) | 757.97-781.62 | -0.1% / +0.3% | -1.0% | 42.5M |
| QQQ | 719.91 (08:59 iex) | -1.2% | 728.95 | 8.96 (1.2%) | 712.58-762.86 | -1.8% / +0.4% | -3.8% | 34.6M |
| IWM | 271.61 (08:49 sip) | +0.1% | 271.37 | 3.67 (1.4%) | 270.35-288.94 | -3.3% / -6.3% | -2.3% | 25.5M |
| DIA | 517.64 (08:49 sip) | +0.4% | 515.63 | 4.93 (1.0%) | 504.70-522.80 | +0.3% / -1.6% | +0.9% | 3.3M |
| TLT | 80.34 (09:04 iex) | +1.8% | 78.89 | 0.79 (1.0%) | 76.43-81.61 | +0.2% / -2.0% | +2.3% | 47.9M |
| GLD | 379.96 (09:05 iex) | +1.1% | 375.99 | 5.84 (1.6%) | 373.36-403.15 | -2.6% / -5.4% | +0.0% | 7.8M |
| USO | 153.50 (08:49 sip) | -0.0% | 153.56 | 4.89 (3.2%) | 141.76-157.55 | +3.3% / +8.9% | +6.7% | 5.4M |
| SMH | 548.89 (08:58 iex) | -2.8% | 564.74 | 14.30 (2.5%) | 557.56-639.47 | -6.3% / -2.6% | -9.6% | 6.6M |
| XLK | 187.37 (08:49 sip) | -1.6% | 190.43 | 3.02 (1.6%) | 186.51-203.25 | -2.9% / +0.4% | -5.4% | 7.5M |
| XLF | 54.95 (08:49 sip) | +0.8% | 54.52 | 0.67 (1.2%) | 52.81-56.20 | +0.1% / -3.1% | +1.4% | 38.3M |
| XLE | 67.81 (08:49 sip) | +0.3% | 67.63 | 1.22 (1.8%) | 60.95-67.72 | +6.4% / +7.5% | +6.7% | 32.5M |
| XLV | 176.00 (08:49 sip) | +1.2% | 173.96 | 2.77 (1.6%) | 165.19-173.99 | +2.8% / +2.9% | +3.1% | 8.3M |
| XLI | 167.16 (08:45 sip) | +0.1% | 167.04 | 2.48 (1.5%) | 165.69-172.34 | -1.2% / -4.3% | -0.5% | 7.3M |
| XLY | 111.36 (07:25 sip) | -0.1% | 111.50 | 1.25 (1.1%) | 107.99-113.29 | +0.5% / -2.1% | +0.1% | 6.3M |
| XLP | 87.49 (08:45 sip) | +1.7% | 86.06 | 1.04 (1.2%) | 80.10-86.06 | +4.5% / +2.9% | +5.3% | 10.7M |
| XLU | 42.07 (08:49 sip) | +0.8% | 41.72 | 0.64 (1.5%) | 39.03-41.95 | +3.0% / -0.4% | +1.4% | 34.5M |
| XLB | 50.08 (08:20 sip) | +0.8% | 49.67 | 0.70 (1.4%) | 47.81-50.78 | +0.3% / -2.8% | +1.4% | 11.4M |
| XLRE | 42.01 (08:45 sip) | +1.3% | 41.49 | 0.58 (1.4%) | 40.28-42.81 | -0.0% / -3.5% | +2.3% | 7.0M |
| XLC | no trade today | - | 110.82 | 1.49 (1.3%) | 109.66-115.61 | -0.9% / -0.7% | -0.4% | 6.6M |
| KRE | 68.99 (08:49 sip) | +0.7% | 68.54 | 1.26 (1.8%) | 67.79-73.37 | -2.5% / -6.0% | -0.5% | 15.5M |
| XHB | 93.50 (06:10 sip) | +0.7% | 92.84 | 2.12 (2.3%) | 91.87-99.67 | -3.6% / -8.0% | -2.2% | 1.8M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 345.42 (08:59 iex) | +0.7% | 342.96 | 6.58 (1.9%) | 325.81-348.15 | +1.8% / +5.7% | +1.9% | 38.3M |
| MSFT | 530.18 (08:49 sip) | -0.7% | 533.69 | 12.23 (2.3%) | 491.10-551.15 | +3.4% / +6.0% | +0.7% | 22.8M |
| NVDA | 217.24 (08:49 sip) | -1.8% | 221.30 | 5.63 (2.5%) | 217.15-243.37 | -3.2% / -0.8% | -6.8% | 108.0M |
| AMZN | 249.25 (08:53 iex) | -1.9% | 254.08 | 5.53 (2.2%) | 244.72-263.70 | +0.3% / -1.5% | -2.2% | 36.2M |
| GOOGL | 344.90 (08:49 sip) | -0.8% | 347.64 | 8.04 (2.3%) | 335.51-364.17 | +0.3% / +0.7% | -0.8% | 26.1M |
| META | 727.77 (08:54 iex) | -1.3% | 737.54 | 22.50 (3.1%) | 660.28-779.82 | +0.9% / +13.5% | +2.3% | 22.1M |
| TSLA | 361.39 (08:52 iex) | -1.6% | 367.16 | 10.95 (3.0%) | 345.88-388.56 | -1.0% / +2.6% | -2.8% | 34.8M |
| AVGO | 339.62 (08:49 sip) | -1.9% | 346.25 | 10.81 (3.1%) | 342.82-380.84 | -3.0% / -6.1% | -8.0% | 22.9M |
| AMD | 551.00 (08:49 sip) | -3.5% | 570.82 | 24.27 (4.3%) | 527.60-658.52 | -6.6% / +6.7% | -11.6% | 21.7M |
| ORCL | 127.89 (09:04 iex) | -2.0% | 130.55 | 6.60 (5.1%) | 129.23-153.03 | -7.3% / -10.0% | -8.7% | 30.6M |
| NFLX | 71.21 (08:49 sip) | +0.9% | 70.57 | 1.53 (2.2%) | 66.54-76.96 | +0.1% / -6.1% | +1.2% | 38.1M |
| CRM | 235.38 (08:45 sip) | -0.2% | 235.95 | 8.06 (3.4%) | 220.29-247.00 | +1.3% / +3.6% | +5.1% | 10.1M |
| JPM | 339.40 (08:49 sip) | +1.2% | 335.28 | 5.94 (1.8%) | 324.25-352.74 | -0.1% / -3.5% | +1.7% | 8.6M |
| GS | 880.00 (08:49 sip) | +0.1% | 878.72 | 20.57 (2.3%) | 866.00-967.76 | -3.7% / -10.3% | -1.0% | 2.4M |
| BAC | 51.89 (08:49 sip) | +1.0% | 51.39 | 1.24 (2.4%) | 49.26-58.49 | -6.6% / -13.5% | -4.0% | 41.5M |
| XOM | 178.10 (08:49 sip) | +0.6% | 177.01 | 3.21 (1.8%) | 155.85-177.43 | +7.4% / +8.9% | +7.9% | 13.0M |
| CVX | 223.18 (08:45 sip) | +0.5% | 222.04 | 4.18 (1.9%) | 200.78-222.55 | +6.5% / +8.1% | +8.2% | 9.4M |
| LLY | 1,228.96 (08:49 sip) | +1.7% | 1,208.74 | 34.37 (2.8%) | 1,131.21-1,216.71 | +3.4% / +2.7% | +1.7% | 2.3M |
| UNH | 399.05 (08:49 sip) | +0.9% | 395.62 | 11.18 (2.8%) | 362.60-399.88 | +5.3% / +2.5% | +5.2% | 5.7M |
| JNJ | 257.58 (08:49 sip) | +1.4% | 253.91 | 5.97 (2.4%) | 245.17-275.23 | -3.4% / -4.2% | -1.8% | 7.7M |
| WMT | 119.68 (09:01 iex) | +3.0% | 116.16 | 2.32 (2.0%) | 103.39-116.24 | +7.1% / +7.0% | +7.4% | 22.3M |
| COST | 994.02 (08:49 sip) | +1.2% | 982.00 | 17.02 (1.7%) | 883.10-982.64 | +6.2% / +5.3% | +4.2% | 2.4M |
| HD | 301.10 (08:49 sip) | +1.9% | 295.51 | 5.89 (2.0%) | 277.15-310.40 | +1.3% / -5.8% | +3.4% | 5.7M |
| CAT | 732.38 (08:49 sip) | -2.2% | 748.98 | 28.30 (3.8%) | 742.01-876.95 | -7.8% / -8.4% | -8.0% | 2.5M |
| BA | 185.50 (08:49 sip) | +0.5% | 184.66 | 5.56 (3.0%) | 183.38-204.06 | -3.9% / -10.9% | -1.9% | 8.9M |
| DAL | 76.87 (08:40 sip) | +0.6% | 76.44 | 2.49 (3.3%) | 75.91-85.93 | -6.9% / -7.6% | -7.6% | 8.4M |
| UAL | 99.12 (08:49 sip) | +0.2% | 98.96 | 3.83 (3.9%) | 97.70-118.26 | -9.8% / -12.6% | -10.2% | 4.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-14 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| BSP | 52.25 (08:49 sip) | -2.3% | 53.46 | 4.06 (7.6%) | 31.43-58.56 | +47.0% / +34.4% | +30.2% | 4.0M |
| AEHL | 9.85 (08:49 sip) | -14.3% | 11.49 | 2.85 (24.8%) | 6.75-30.60 | +18.1% / +53.0% | -6.7% | 1.2M |
| LQDA | 33.86 (08:49 sip) | -0.2% | 33.94 | 7.07 (20.8%) | 22.31-74.74 | -27.2% / -45.9% | +27.2% | 6.4M |
| IREZ | 17.71 (08:49 sip) | +8.9% | 16.26 | 1.33 (8.2%) | 6.82-16.37 | +62.1% / +52.3% | +51.3% | 2.6M |
| AAOZ | 17.07 (08:49 sip) | +9.5% | 15.59 | 2.05 (13.1%) | 7.63-15.84 | +26.9% / +25.8% | +80.6% | 1.7M |
| NBIZ | 33.11 (08:49 sip) | +8.6% | 30.48 | 2.82 (9.2%) | 17.01-31.24 | +37.8% / +8.1% | +54.4% | 2.2M |
| BEZ | 6.97 (08:49 sip) | +10.5% | 6.31 | 0.76 (12.1%) | 4.08-6.50 | +21.4% / -17.8% | +41.0% | 5.5M |
| LITZ | 27.98 (08:49 sip) | +9.4% | 25.58 | 3.08 (12.0%) | 16.35-29.28 | +11.5% / -15.0% | +43.4% | 2.1M |
| CRWG | 8.76 (08:57 iex) | -11.2% | 9.86 | 2.06 (20.9%) | 9.36-20.68 | -42.5% / -49.3% | -47.1% | 3.1M |
| CWVX | 7.66 (08:49 sip) | -7.0% | 8.23 | 1.71 (20.7%) | 7.81-17.26 | -42.5% / -49.2% | -47.2% | 1.9M |
