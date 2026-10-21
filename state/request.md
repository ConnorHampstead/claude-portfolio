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

- Time now: **09:05 ET** (13:05 UTC, 15:05 Stockholm), Wednesday 2026-10-21. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$101,868.32**
- Cash: $88,578.32
- Session P&L so far: -0.22% (new entries are blocked at -3.0%)
- Gross exposure: $48,306 (47% of equity, cap 150%)
- Net exposure: $+7,768 (+8%, cap +/-100%)
- Risk at stake (entry to stop): $1,432 (1.41% of equity, cap 4.0%) — 2.59% left for new plays
- Slots: 4 open + 1 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMD | short | 19 | 542.20 | 545.55 | -64 (-0.6%) | 558.00 | 512.00 | Relief gap on upgrades without any change to the AI-credit story, now confirmed by the open rather than predicted. Overh |
| CVX | long | 78 | 224.48 | 225.53 | +82 (+0.5%) | 218.00 | 236.00 | Energy leads the rotation away from AI capex and the oil tape still points up. A retest of the breakout and Monday's 224 |
| HD | long | 33 | 310.70 | 316.53 | +192 (+1.9%) | 307.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 132.77 | -101 (-2.4%) | 137.40 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |

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

47 resolved: 11 reached target first, 26 stop first, 8 never reached the entry, 2 expired, 0 ambiguous. Average -0.27R across the 39 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-14 open | KRE | short | Morning play rejected by broker: not shortable. | never filled | - | 34% |
| 2026-10-07 pre-market | XHB | short | Same housing/rates factor as the HD short; one is enough. | expired | -0.52R | 33% |
| 2026-10-20 pre-market | DAL | short | Oil-cost victim, but at its 20d low with UAL reporting tonight; gap-risk coin fl | stop | -1.04R | 35% |
| 2026-10-15 open | LLY | long | 1.3 ATR above its 20d high after +4.3%; chasing a gap. | target | +2.00R | 40% |
| 2026-10-08 pre-market | UAL | short | Oil-cost victim, but DAL reports 10/09 pre-market and has lifted the group befor | target | +1.21R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMD | 544.21 (08:49 sip) | +1.8% | 534.74 | 27.36 (5.1%) | 524.60-658.52 | -11.2% / -0.9% | -11.7% | 19.4M |
| CVX | 225.53 (08:35 sip) | -0.1% | 225.71 | 4.64 (2.1%) | 201.96-227.28 | +6.6% / +8.4% | +3.7% | 7.5M |
| HD | 315.80 (08:40 sip) | +0.2% | 315.11 | 6.76 (2.1%) | 277.15-317.71 | +7.3% / +1.4% | +7.2% | 5.6M |
| ORCL | 132.72 (08:49 iex) | +1.2% | 131.14 | 6.62 (5.1%) | 127.36-148.11 | -4.5% / -8.9% | -8.4% | 30.4M |
| NVDA | 220.40 (08:49 sip) | +1.8% | 216.47 | 5.78 (2.7%) | 212.77-243.37 | -4.7% / -2.8% | -5.3% | 104.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 770.92 (08:49 sip) | +0.2% | 769.05 | 7.13 (0.9%) | 758.79-781.62 | -0.2% / +0.2% | -1.2% | 41.6M |
| QQQ | 722.29 (09:05 iex) | +0.6% | 717.63 | 11.13 (1.6%) | 707.23-762.86 | -3.0% / -1.2% | -3.5% | 35.2M |
| IWM | 276.65 (08:49 sip) | +0.3% | 275.78 | 4.08 (1.5%) | 269.88-286.18 | -0.8% / -4.1% | -0.3% | 26.2M |
| DIA | 526.16 (08:49 sip) | +0.3% | 524.36 | 5.29 (1.0%) | 504.59-526.17 | +1.9% / +0.3% | +1.6% | 3.4M |
| TLT | 80.32 (08:49 sip) | +0.2% | 80.13 | 0.85 (1.1%) | 76.43-81.18 | +2.1% / -0.2% | +2.2% | 50.7M |
| GLD | 378.08 (08:49 sip) | +0.1% | 377.65 | 4.92 (1.3%) | 373.36-395.50 | -1.2% / -4.7% | -1.1% | 7.7M |
| USO | 160.09 (08:49 sip) | -0.3% | 160.61 | 4.75 (3.0%) | 141.76-162.99 | +6.6% / +11.4% | +4.9% | 5.4M |
| SMH | 554.76 (08:49 sip) | +1.5% | 546.36 | 16.87 (3.1%) | 536.23-639.47 | -8.3% / -5.5% | -7.1% | 7.6M |
| XLK | 187.25 (08:49 sip) | +1.0% | 185.44 | 3.74 (2.0%) | 182.81-203.25 | -4.8% / -2.3% | -5.5% | 8.3M |
| XLF | 55.91 (08:49 sip) | +0.3% | 55.72 | 0.70 (1.3%) | 52.81-56.03 | +2.3% / -0.6% | +1.6% | 36.9M |
| XLE | 67.98 (08:49 sip) | +0.0% | 67.97 | 1.38 (2.0%) | 60.95-68.51 | +5.4% / +6.7% | +1.1% | 32.4M |
| XLV | 178.20 (08:45 sip) | -0.9% | 179.82 | 3.03 (1.7%) | 165.19-180.06 | +5.2% / +5.7% | +6.0% | 8.4M |
| XLI | 168.00 (08:25 sip) | +0.7% | 166.80 | 2.57 (1.5%) | 164.66-172.34 | -1.1% / -3.7% | -1.1% | 7.5M |
| XLY | 115.80 (08:40 sip) | +0.3% | 115.50 | 1.53 (1.3%) | 107.99-116.22 | +3.7% / +1.7% | +2.8% | 7.0M |
| XLP | 87.16 (08:45 sip) | -0.7% | 87.75 | 1.11 (1.3%) | 80.10-88.47 | +5.3% / +4.6% | +4.2% | 12.7M |
| XLU | 42.08 (08:49 sip) | +0.5% | 41.88 | 0.69 (1.6%) | 39.03-42.29 | +2.9% / +0.3% | +0.0% | 35.8M |
| XLB | 51.24 (07:20 sip) | +0.0% | 51.23 | 0.73 (1.4%) | 47.81-51.51 | +3.1% / +0.5% | +3.0% | 11.7M |
| XLRE | 42.49 (08:45 sip) | +0.3% | 42.38 | 0.62 (1.5%) | 40.28-42.48 | +2.3% / -1.0% | +1.3% | 7.6M |
| XLC | 109.32 (08:35 sip) | -0.8% | 110.19 | 1.63 (1.5%) | 109.45-114.08 | -1.1% / -1.3% | -1.9% | 6.3M |
| KRE | 70.65 (08:35 sip) | +0.0% | 70.62 | 1.32 (1.9%) | 67.79-71.93 | +1.0% / -2.5% | +2.3% | 16.0M |
| XHB | 96.50 (08:30 sip) | +0.3% | 96.22 | 2.28 (2.4%) | 91.87-99.13 | +0.4% / -3.6% | +1.7% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 338.59 (08:49 sip) | -0.3% | 339.50 | 6.01 (1.8%) | 325.81-348.15 | +0.6% / +3.8% | -0.5% | 36.9M |
| MSFT | 530.58 (08:49 sip) | -0.2% | 531.87 | 11.30 (2.1%) | 491.22-551.15 | +1.6% / +5.0% | -2.1% | 21.6M |
| NVDA | 220.40 (08:49 sip) | +1.8% | 216.47 | 5.78 (2.7%) | 212.77-243.37 | -4.7% / -2.8% | -5.3% | 104.7M |
| AMZN | 262.93 (08:49 sip) | +0.1% | 262.63 | 6.51 (2.5%) | 244.72-265.34 | +3.5% / +2.4% | +1.6% | 36.2M |
| GOOGL | 336.71 (08:49 sip) | -1.0% | 340.27 | 8.67 (2.5%) | 335.51-359.40 | -1.5% / -1.1% | -3.8% | 24.2M |
| META | 691.10 (08:49 sip) | -0.5% | 694.25 | 21.90 (3.2%) | 681.05-779.82 | -5.1% / +5.3% | -9.0% | 19.6M |
| TSLA | 379.77 (09:01 iex) | +1.6% | 373.71 | 11.76 (3.1%) | 345.88-388.56 | +1.1% / +3.5% | -0.4% | 35.0M |
| AVGO | 337.47 (08:49 sip) | +0.9% | 334.37 | 11.96 (3.6%) | 328.58-380.84 | -5.1% / -7.6% | -6.4% | 21.7M |
| AMD | 544.21 (08:49 sip) | +1.8% | 534.74 | 27.36 (5.1%) | 524.60-658.52 | -11.2% / -0.9% | -11.7% | 19.4M |
| ORCL | 132.72 (08:49 iex) | +1.2% | 131.14 | 6.62 (5.1%) | 127.36-148.11 | -4.5% / -8.9% | -8.4% | 30.4M |
| NFLX | 64.07 (08:49 sip) | -6.7% | 68.69 | 1.73 (2.5%) | 66.54-73.07 | -1.8% / -8.2% | -2.5% | 36.7M |
| CRM | 241.30 (08:49 sip) | -0.5% | 242.43 | 8.55 (3.5%) | 220.29-251.94 | +3.6% / +4.6% | +1.9% | 8.5M |
| JPM | 337.37 (08:49 sip) | +0.6% | 335.26 | 6.42 (1.9%) | 324.25-344.40 | +0.5% / -3.0% | +1.2% | 7.9M |
| GS | 895.50 (08:49 sip) | +1.2% | 884.81 | 23.57 (2.7%) | 859.03-954.98 | -1.6% / -8.5% | -0.8% | 2.3M |
| BAC | 51.00 (08:49 sip) | +0.7% | 50.64 | 1.33 (2.6%) | 49.26-56.74 | -5.7% / -13.3% | -6.2% | 43.0M |
| XOM | 177.91 (08:10 sip) | +0.0% | 177.86 | 3.60 (2.0%) | 159.27-180.26 | +5.8% / +8.1% | +2.2% | 11.5M |
| CVX | 225.53 (08:35 sip) | -0.1% | 225.71 | 4.64 (2.1%) | 201.96-227.28 | +6.6% / +8.4% | +3.7% | 7.5M |
| LLY | 1,276.00 (08:45 sip) | -0.6% | 1,283.66 | 37.77 (2.9%) | 1,131.21-1,311.75 | +8.0% / +8.6% | +10.0% | 2.3M |
| UNH | 418.27 (08:45 sip) | -0.2% | 419.26 | 13.32 (3.2%) | 362.60-422.40 | +9.7% / +8.5% | +11.0% | 6.0M |
| JNJ | 257.47 (08:45 sip) | -0.7% | 259.36 | 6.49 (2.5%) | 245.17-275.23 | -0.3% / -2.1% | +4.3% | 7.7M |
| WMT | 116.94 (08:49 sip) | -0.8% | 117.85 | 2.37 (2.0%) | 103.39-121.38 | +6.6% / +8.0% | +5.0% | 21.5M |
| COST | 988.20 (08:35 sip) | -0.6% | 994.61 | 15.74 (1.6%) | 883.10-1,008.37 | +5.4% / +6.3% | +4.2% | 2.3M |
| HD | 315.80 (08:40 sip) | +0.2% | 315.11 | 6.76 (2.1%) | 277.15-317.71 | +7.3% / +1.4% | +7.2% | 5.6M |
| CAT | 738.76 (08:49 sip) | +1.9% | 725.24 | 30.67 (4.2%) | 704.01-876.95 | -8.9% / -10.3% | -6.2% | 2.6M |
| BA | 192.34 (08:49 sip) | +1.0% | 190.47 | 4.34 (2.3%) | 183.38-204.06 | +0.0% / -6.5% | +2.1% | 8.4M |
| DAL | 77.29 (08:49 sip) | +0.8% | 76.66 | 2.78 (3.6%) | 74.14-85.93 | -5.4% / -5.9% | -3.4% | 7.3M |
| UAL | 98.42 (08:49 sip) | +0.7% | 97.77 | 4.17 (4.3%) | 94.54-115.71 | -8.6% / -11.7% | -5.3% | 4.6M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-20 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SAIQ | 5.78 (08:49 sip) | -15.5% | 6.84 | 2.06 (30.1%) | 1.76-12.95 | +14.7% / -21.7% | +63.2% | 8.0M |
| BRZE | 45.45 (08:45 sip) | -0.3% | 45.57 | 2.45 (5.4%) | 22.27-45.61 | +63.4% / +59.7% | +57.5% | 5.1M |
| MYGN | 5.66 (08:49 sip) | +2.2% | 5.54 | 0.39 (7.1%) | 3.95-5.95 | +29.0% / +48.5% | +35.8% | 2.8M |
