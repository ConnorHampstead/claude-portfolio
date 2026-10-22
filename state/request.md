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

- Time now: **09:05 ET** (13:05 UTC, 15:05 Stockholm), Thursday 2026-10-22. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,778.06**
- Cash: $97,885.87
- Session P&L so far: +0.96% (new entries are blocked at -3.0%)
- Gross exposure: $74,658 (73% of equity, cap 150%)
- Net exposure: $+16,888 (+16%, cap +/-100%)
- Risk at stake (entry to stop): $2,124 (2.07% of equity, cap 4.0%) — 1.93% left for new plays
- Slots: 5 open + 2 resting entries of 8 — you may add at most 1 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMD | short | 19 | 542.20 | 526.42 | +300 (+2.9%) | 558.00 | 512.00 | Relief gap on upgrades without any change to the AI-credit story, now confirmed by the open rather than predicted. Overh |
| CVX | long | 78 | 224.48 | 229.37 | +381 (+2.2%) | 218.00 | 236.00 | Energy leads the rotation away from AI capex and the oil tape still points up. A retest of the breakout and Monday's 224 |
| GOOGL | short | 28 | 332.42 | 328.88 | +99 (+1.1%) | 341.50 | 320.00 | Relative weakness breaking the floor of the 20-day range on a tech-bid day; failed floor opens ~4% to 320. |
| HD | long | 33 | 310.70 | 314.07 | +111 (+1.1%) | 309.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 125.82 | +128 (+3.0%) | 137.40 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XOM | long | 97 | 180.60 | stop | 175.40 | 189.00 | 2026-10-21 |
| NVDA | short | 26 | 212.40 | stop | 222.00 | 198.00 | 2026-10-20 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 23.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |

### Ideas you passed on, replayed against the tape

49 resolved: 11 reached target first, 28 stop first, 8 never reached the entry, 2 expired, 0 ambiguous. Average -0.30R across the 41 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-14 pre-market | IWM | short | Same rate factor as XHB/KRE; left to the review if it fails to reclaim 274.5. | stop | -1.08R | 36% |
| 2026-10-19 open | NVDA | short | Gap already faded to near the 212.85 20-day low; little room to the floor. | stop | -0.95R | 35% |
| 2026-10-14 open | KRE | short | Morning play rejected by broker: not shortable. | never filled | - | 34% |
| 2026-10-07 pre-market | XHB | short | Same housing/rates factor as the HD short; one is enough. | expired | -0.52R | 33% |
| 2026-10-20 pre-market | DAL | short | Oil-cost victim, but at its 20d low with UAL reporting tonight; gap-risk coin fl | stop | -1.04R | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMD | 528.40 (08:49 sip) | -4.4% | 552.72 | 27.67 (5.0%) | 524.60-658.52 | -7.7% / +2.1% | -3.2% | 19.5M |
| CVX | 228.80 (08:40 sip) | +0.9% | 226.78 | 4.62 (2.0%) | 201.96-228.48 | +6.5% / +8.5% | +2.1% | 7.5M |
| GOOGL | 328.83 (09:03 iex) | -1.8% | 334.76 | 8.11 (2.4%) | 330.38-359.40 | -3.0% / -2.6% | -3.7% | 23.9M |
| HD | 313.75 (08:30 sip) | -0.1% | 314.14 | 6.61 (2.1%) | 277.15-317.71 | +6.7% / +1.3% | +6.3% | 5.5M |
| ORCL | 126.05 (08:49 sip) | -2.4% | 129.13 | 6.69 (5.2%) | 127.36-146.40 | -5.4% / -10.1% | -1.1% | 30.6M |
| XOM | 179.70 (08:49 sip) | +0.9% | 178.09 | 3.58 (2.0%) | 159.27-180.26 | +5.4% / +8.0% | +0.6% | 11.4M |
| NVDA | 216.89 (08:51 iex) | -2.3% | 221.97 | 5.89 (2.7%) | 212.77-243.37 | -2.2% / -0.4% | +0.3% | 104.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 766.26 (08:49 sip) | -0.9% | 773.09 | 7.07 (0.9%) | 758.79-781.62 | +0.3% / +0.7% | +0.5% | 40.4M |
| QQQ | 713.21 (09:04 iex) | -1.7% | 725.20 | 11.27 (1.6%) | 707.23-762.86 | -1.9% / -0.2% | -0.5% | 35.2M |
| IWM | 274.98 (08:49 sip) | -0.5% | 276.48 | 3.88 (1.4%) | 269.88-284.64 | -0.5% / -3.7% | +1.9% | 25.8M |
| DIA | 525.08 (08:49 sip) | -0.5% | 527.70 | 5.17 (1.0%) | 504.59-527.79 | +2.4% / +1.0% | +2.4% | 3.3M |
| TLT | 81.02 (08:49 sip) | +1.0% | 80.24 | 0.80 (1.0%) | 76.43-80.56 | +2.2% / -0.0% | +1.7% | 49.8M |
| GLD | 374.41 (08:49 sip) | -1.2% | 378.95 | 4.93 (1.3%) | 373.36-394.22 | -0.7% / -4.3% | +0.8% | 7.7M |
| USO | 162.52 (08:49 sip) | +1.7% | 159.80 | 4.67 (2.9%) | 141.76-162.99 | +5.7% / +10.3% | +4.1% | 5.4M |
| SMH | 537.50 (08:49 sip) | -3.4% | 556.70 | 16.81 (3.0%) | 536.23-639.47 | -6.2% / -3.6% | -1.4% | 7.7M |
| XLK | 184.92 (08:49 sip) | -1.9% | 188.54 | 3.79 (2.0%) | 182.81-203.25 | -3.1% / -0.7% | -1.0% | 8.5M |
| XLF | 55.82 (08:49 sip) | -0.4% | 56.04 | 0.68 (1.2%) | 52.81-56.15 | +2.8% / -0.0% | +2.8% | 36.2M |
| XLE | 68.73 (08:49 sip) | +0.8% | 68.16 | 1.34 (2.0%) | 60.95-68.64 | +5.2% / +6.8% | +0.8% | 31.9M |
| XLV | 180.10 (08:49 sip) | +0.6% | 178.94 | 2.99 (1.7%) | 165.19-180.06 | +4.4% / +5.1% | +2.9% | 8.5M |
| XLI | 167.19 (08:30 sip) | -0.7% | 168.31 | 2.52 (1.5%) | 164.66-172.34 | -0.2% / -2.6% | +0.8% | 7.4M |
| XLY | 114.10 (08:35 sip) | -1.2% | 115.53 | 1.52 (1.3%) | 107.99-116.22 | +3.5% / +1.8% | +3.6% | 7.0M |
| XLP | 88.00 (08:49 sip) | +1.0% | 87.11 | 1.14 (1.3%) | 80.10-88.47 | +4.2% / +3.8% | +1.2% | 12.8M |
| XLU | 42.09 (08:49 sip) | +0.2% | 42.00 | 0.67 (1.6%) | 39.03-42.29 | +3.0% / +0.6% | +0.7% | 36.5M |
| XLB | 51.11 (08:45 sip) | -0.4% | 51.32 | 0.69 (1.3%) | 47.81-51.51 | +3.2% / +0.8% | +3.3% | 11.6M |
| XLRE | 42.06 (06:15 sip) | +0.0% | 42.06 | 0.63 (1.5%) | 40.28-42.61 | +1.5% / -1.6% | +1.4% | 7.6M |
| XLC | 108.05 (08:49 sip) | -0.8% | 108.97 | 1.59 (1.5%) | 108.61-114.08 | -2.0% / -2.4% | -1.7% | 6.5M |
| KRE | 70.44 (08:40 sip) | -0.3% | 70.62 | 1.24 (1.7%) | 67.79-71.93 | +1.0% / -2.4% | +3.0% | 16.0M |
| XHB | 94.91 (06:40 sip) | -0.7% | 95.60 | 2.21 (2.3%) | 91.87-99.13 | -0.2% / -3.9% | +3.0% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 343.78 (09:03 iex) | -0.1% | 343.99 | 5.95 (1.7%) | 325.81-348.15 | +1.8% / +5.0% | +0.3% | 37.1M |
| MSFT | 531.71 (08:55 iex) | -0.2% | 532.95 | 11.12 (2.1%) | 491.22-551.15 | +1.5% / +5.1% | -0.1% | 21.3M |
| NVDA | 216.89 (08:51 iex) | -2.3% | 221.97 | 5.89 (2.7%) | 212.77-243.37 | -2.2% / -0.4% | +0.3% | 104.5M |
| AMZN | 257.15 (08:49 sip) | -2.0% | 262.37 | 6.47 (2.5%) | 244.72-265.34 | +3.1% / +2.4% | +3.3% | 35.5M |
| GOOGL | 328.83 (09:03 iex) | -1.8% | 334.76 | 8.11 (2.4%) | 330.38-359.40 | -3.0% / -2.6% | -3.7% | 23.9M |
| META | 680.21 (09:00 iex) | -2.5% | 697.52 | 22.56 (3.2%) | 681.05-779.82 | -4.4% / +5.5% | -5.4% | 19.6M |
| TSLA | 372.35 (09:04 iex) | -3.7% | 386.47 | 12.41 (3.2%) | 345.88-388.84 | +4.4% / +6.7% | +5.3% | 35.8M |
| AVGO | 326.60 (09:02 iex) | -3.3% | 337.80 | 11.66 (3.5%) | 328.58-380.84 | -3.9% / -6.2% | -2.4% | 21.4M |
| AMD | 528.40 (08:49 sip) | -4.4% | 552.72 | 27.67 (5.0%) | 524.60-658.52 | -7.7% / +2.1% | -3.2% | 19.5M |
| ORCL | 126.05 (08:49 sip) | -2.4% | 129.13 | 6.69 (5.2%) | 127.36-146.40 | -5.4% / -10.1% | -1.1% | 30.6M |
| NFLX | 65.42 (08:49 sip) | +0.6% | 65.04 | 1.92 (3.0%) | 64.10-73.07 | -6.6% / -12.9% | -7.8% | 40.1M |
| CRM | 244.00 (08:45 sip) | +0.9% | 241.78 | 8.34 (3.4%) | 220.29-251.94 | +3.2% / +3.9% | +2.5% | 8.2M |
| JPM | 333.25 (08:20 sip) | -0.6% | 335.19 | 6.19 (1.8%) | 324.25-344.40 | +0.4% / -2.9% | -0.0% | 7.9M |
| GS | 890.05 (08:49 sip) | -1.6% | 904.72 | 23.64 (2.6%) | 859.03-935.83 | +0.8% / -6.2% | +3.0% | 2.3M |
| BAC | 50.42 (08:45 sip) | -0.7% | 50.78 | 1.27 (2.5%) | 49.26-56.74 | -5.0% / -12.7% | -1.2% | 42.9M |
| XOM | 179.70 (08:49 sip) | +0.9% | 178.09 | 3.58 (2.0%) | 159.27-180.26 | +5.4% / +8.0% | +0.6% | 11.4M |
| CVX | 228.80 (08:40 sip) | +0.9% | 226.78 | 4.62 (2.0%) | 201.96-228.48 | +6.5% / +8.5% | +2.1% | 7.5M |
| LLY | 1,286.50 (08:49 sip) | +1.2% | 1,270.75 | 38.03 (3.0%) | 1,131.21-1,311.75 | +6.4% / +7.4% | +5.1% | 2.3M |
| UNH | 420.55 (08:49 sip) | +0.9% | 417.00 | 13.15 (3.2%) | 362.60-422.40 | +8.4% / +7.8% | +5.4% | 6.0M |
| JNJ | 261.10 (08:49 sip) | +1.3% | 257.78 | 6.38 (2.5%) | 245.17-275.23 | -0.7% / -2.6% | +1.5% | 7.7M |
| WMT | 119.25 (08:49 sip) | +1.2% | 117.80 | 2.38 (2.0%) | 103.39-121.38 | +6.2% / +7.9% | +1.4% | 21.2M |
| COST | 1,008.00 (08:49 sip) | +1.0% | 998.31 | 15.17 (1.5%) | 883.10-1,008.37 | +5.3% / +6.6% | +1.7% | 2.3M |
| HD | 313.75 (08:30 sip) | -0.1% | 314.14 | 6.61 (2.1%) | 277.15-317.71 | +6.7% / +1.3% | +6.3% | 5.5M |
| CAT | 720.53 (08:40 sip) | -2.7% | 740.21 | 29.86 (4.0%) | 704.01-876.95 | -6.6% / -8.2% | -1.2% | 2.6M |
| BA | 190.95 (08:49 sip) | -0.7% | 192.28 | 3.99 (2.1%) | 183.38-201.40 | +1.2% / -5.2% | +4.1% | 8.2M |
| DAL | 75.76 (08:45 sip) | -2.5% | 77.67 | 2.88 (3.7%) | 74.14-85.93 | -4.0% / -4.4% | +1.6% | 7.4M |
| UAL | 98.99 (08:40 sip) | -2.6% | 101.67 | 4.59 (4.5%) | 94.54-115.71 | -4.6% / -7.7% | +2.7% | 4.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-21 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| BETR | 14.85 (08:49 sip) | -4.7% | 15.58 | 1.60 (10.3%) | 7.51-15.95 | +46.3% / +28.9% | +91.9% | 1.2M |
| AVEX | 10.80 (08:49 sip) | +11.6% | 9.68 | 1.22 (12.6%) | 9.64-17.15 | -33.7% / -41.1% | -31.7% | 2.3M |
