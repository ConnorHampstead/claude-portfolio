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

- Time now: **09:05 ET** (13:05 UTC), Tuesday 2026-10-20. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,007.22**
- Cash: $106,087.77
- Session P&L so far: +0.19% (new entries are blocked at -3.0%)
- Gross exposure: $40,682 (40% of equity, cap 150%)
- Net exposure: $+11,927 (+12%, cap +/-100%)
- Risk at stake (entry to stop): $1,504 (1.47% of equity, cap 4.0%) — 2.53% left for new plays
- Slots: 3 open + 1 resting entries of 8 — you may add at most 4 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMD | short | 19 | 542.20 | 532.00 | +194 (+1.9%) | 568.00 | 512.00 | Relief gap on upgrades without any change to the AI-credit story, now confirmed by the open rather than predicted. Overh |
| HD | long | 33 | 310.70 | 312.02 | +43 (+0.4%) | 303.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 129.37 | +11 (+0.3%) | 137.40 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XOM | long | 92 | 174.00 | limit | 168.50 | 182.50 | 2026-10-19 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 20.

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

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMD | 530.87 (08:49 sip) | -1.3% | 538.05 | 26.76 (5.0%) | 526.83-658.52 | -11.3% / -0.0% | -9.5% | 20.1M |
| HD | 311.54 (08:35 sip) | +0.5% | 309.88 | 6.66 (2.2%) | 277.15-314.66 | +5.7% / -0.5% | +6.6% | 5.6M |
| ORCL | 129.75 (08:49 sip) | +0.1% | 129.59 | 6.40 (4.9%) | 127.36-153.03 | -6.2% / -10.2% | -5.7% | 30.6M |
| XOM | 179.65 (08:49 sip) | +0.8% | 178.28 | 3.43 (1.9%) | 155.85-179.30 | +6.7% / +8.6% | +3.6% | 11.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 765.50 (08:49 sip) | -0.1% | 766.48 | 7.07 (0.9%) | 758.79-781.62 | -0.6% / -0.1% | -1.5% | 41.6M |
| QQQ | 715.15 (08:49 sip) | -0.4% | 718.36 | 10.76 (1.5%) | 707.23-762.86 | -3.1% / -1.1% | -3.7% | 35.7M |
| IWM | 271.52 (08:49 sip) | +0.1% | 271.28 | 3.86 (1.4%) | 269.88-288.94 | -2.6% / -5.8% | -2.4% | 26.2M |
| DIA | 518.95 (08:49 sip) | +0.0% | 518.92 | 5.15 (1.0%) | 504.59-525.09 | +0.9% / -0.8% | +0.2% | 3.4M |
| TLT | 80.07 (09:05 iex) | +0.8% | 79.46 | 0.83 (1.0%) | 76.43-81.61 | +1.2% / -1.1% | +1.8% | 50.4M |
| GLD | 377.06 (09:01 iex) | -0.7% | 379.69 | 4.98 (1.3%) | 373.36-400.78 | -1.0% / -4.3% | -0.6% | 7.7M |
| USO | 162.92 (08:49 sip) | +1.3% | 160.81 | 4.57 (2.8%) | 141.76-162.99 | +7.3% / +12.0% | +6.5% | 5.4M |
| SMH | 541.89 (08:49 sip) | -1.2% | 548.46 | 16.03 (2.9%) | 539.07-639.47 | -8.4% / -5.2% | -7.2% | 7.6M |
| XLK | 184.59 (08:49 sip) | -0.7% | 185.96 | 3.62 (1.9%) | 182.82-203.25 | -4.8% / -2.0% | -5.3% | 8.2M |
| XLF | 55.21 (08:49 sip) | +0.3% | 55.06 | 0.69 (1.2%) | 52.81-56.05 | +1.2% / -1.9% | +0.0% | 39.4M |
| XLE | 68.33 (08:49 sip) | +0.8% | 67.80 | 1.31 (1.9%) | 60.95-68.51 | +5.6% / +6.7% | +2.7% | 32.3M |
| XLV | 176.68 (08:49 sip) | +0.6% | 175.65 | 2.89 (1.6%) | 165.19-178.86 | +3.0% / +3.4% | +2.1% | 8.4M |
| XLI | 166.01 (08:45 sip) | -0.4% | 166.68 | 2.55 (1.5%) | 164.66-172.34 | -1.3% / -3.9% | -1.5% | 7.3M |
| XLY | 114.01 (07:40 sip) | -0.4% | 114.46 | 1.49 (1.3%) | 107.99-114.69 | +2.9% / +0.7% | +2.0% | 7.0M |
| XLP | 87.81 (08:49 sip) | +0.7% | 87.21 | 1.16 (1.3%) | 80.10-88.47 | +4.9% / +4.1% | +3.3% | 12.4M |
| XLU | 41.51 (08:49 sip) | +0.4% | 41.36 | 0.68 (1.7%) | 39.03-42.29 | +1.8% / -1.0% | -0.6% | 35.9M |
| XLB | 50.60 (07:20 sip) | -0.7% | 50.95 | 0.73 (1.4%) | 47.81-51.51 | +2.6% / -0.1% | +3.1% | 11.7M |
| XLRE | 41.70 (08:35 sip) | +0.1% | 41.67 | 0.61 (1.5%) | 40.28-42.67 | +0.6% / -2.7% | -0.6% | 7.5M |
| XLC | 109.90 (07:05 sip) | -0.2% | 110.09 | 1.66 (1.5%) | 109.45-115.61 | -1.3% / -1.4% | -1.2% | 6.5M |
| KRE | 69.40 (08:49 sip) | +0.2% | 69.26 | 1.27 (1.8%) | 67.79-72.68 | -1.0% / -4.5% | -0.4% | 16.0M |
| XHB | 94.41 (08:40 sip) | +0.3% | 94.13 | 2.23 (2.4%) | 91.87-99.67 | -2.0% / -5.9% | +0.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 339.15 (08:49 sip) | -1.1% | 342.94 | 6.42 (1.9%) | 325.81-348.15 | +1.6% / +5.1% | +0.6% | 37.1M |
| MSFT | 535.21 (08:49 sip) | +0.3% | 533.52 | 11.47 (2.2%) | 491.22-551.15 | +2.2% / +5.4% | -1.4% | 21.9M |
| NVDA | 216.18 (09:04 iex) | -0.4% | 217.09 | 5.74 (2.6%) | 212.85-243.37 | -4.6% / -2.6% | -4.1% | 105.5M |
| AMZN | 263.18 (08:49 sip) | +0.3% | 262.45 | 6.62 (2.5%) | 244.72-263.72 | +3.6% / +2.2% | +1.1% | 36.5M |
| GOOGL | 343.56 (08:49 sip) | -0.2% | 344.18 | 9.04 (2.6%) | 335.51-364.17 | -0.5% / -0.0% | -2.4% | 24.8M |
| META | 699.73 (08:49 sip) | -0.8% | 705.44 | 21.41 (3.0%) | 693.86-779.82 | -3.9% / +7.3% | -5.1% | 20.2M |
| TSLA | 368.42 (08:49 sip) | +0.1% | 368.06 | 11.43 (3.1%) | 345.88-388.56 | -0.5% / +2.2% | -2.6% | 34.9M |
| AVGO | 333.59 (08:49 sip) | -0.3% | 334.59 | 11.74 (3.5%) | 328.58-380.84 | -5.5% / -7.9% | -5.7% | 21.9M |
| AMD | 530.87 (08:49 sip) | -1.3% | 538.05 | 26.76 (5.0%) | 526.83-658.52 | -11.3% / -0.0% | -9.5% | 20.1M |
| ORCL | 129.75 (08:49 sip) | +0.1% | 129.59 | 6.40 (4.9%) | 127.36-153.03 | -6.2% / -10.2% | -5.7% | 30.6M |
| NFLX | 69.95 (08:49 sip) | +0.1% | 69.85 | 1.61 (2.3%) | 66.54-73.76 | -0.4% / -6.9% | -1.1% | 35.1M |
| CRM | 234.67 (08:49 sip) | -3.2% | 242.45 | 8.61 (3.5%) | 220.29-251.94 | +3.8% / +5.0% | +3.6% | 8.8M |
| JPM | 334.54 (08:45 sip) | +0.3% | 333.53 | 6.29 (1.9%) | 324.25-350.35 | -0.1% / -3.7% | -0.2% | 8.2M |
| GS | 872.00 (08:35 sip) | -0.4% | 875.78 | 22.27 (2.5%) | 859.03-967.76 | -2.9% / -9.7% | -2.0% | 2.3M |
| BAC | 50.39 (08:49 sip) | -0.0% | 50.39 | 1.29 (2.6%) | 49.26-58.12 | -6.7% / -14.1% | -7.7% | 43.1M |
| XOM | 179.65 (08:49 sip) | +0.8% | 178.28 | 3.43 (1.9%) | 155.85-179.30 | +6.7% / +8.6% | +3.6% | 11.5M |
| CVX | 226.20 (08:49 sip) | +0.8% | 224.37 | 4.42 (2.0%) | 200.78-225.67 | +6.5% / +8.1% | +4.4% | 7.5M |
| LLY | 1,252.71 (08:49 sip) | +1.0% | 1,240.34 | 36.93 (3.0%) | 1,131.21-1,275.88 | +4.9% / +5.0% | +4.9% | 2.3M |
| UNH | 410.08 (08:49 sip) | +0.8% | 406.88 | 12.87 (3.2%) | 362.60-414.12 | +7.1% / +5.4% | +7.5% | 5.9M |
| JNJ | 256.21 (08:49 sip) | +1.0% | 253.79 | 6.28 (2.5%) | 245.17-275.23 | -2.6% / -4.2% | -3.8% | 7.6M |
| WMT | 120.62 (08:49 sip) | +1.6% | 118.70 | 2.38 (2.0%) | 103.39-121.38 | +7.7% / +8.9% | +5.0% | 21.3M |
| COST | 1,001.40 (08:49 sip) | +0.6% | 995.53 | 15.97 (1.6%) | 883.10-1,008.37 | +6.1% / +6.5% | +3.8% | 2.3M |
| HD | 311.54 (08:35 sip) | +0.5% | 309.88 | 6.66 (2.2%) | 277.15-314.66 | +5.7% / -0.5% | +6.6% | 5.6M |
| CAT | 713.60 (08:49 sip) | -1.7% | 725.79 | 30.40 (4.2%) | 704.01-876.95 | -9.3% / -10.4% | -9.2% | 2.6M |
| BA | 191.58 (08:49 sip) | +0.1% | 191.42 | 4.66 (2.4%) | 183.38-204.06 | +0.3% / -6.4% | +1.0% | 8.5M |
| DAL | 74.48 (08:49 sip) | -0.2% | 74.63 | 2.58 (3.5%) | 74.40-85.93 | -8.3% / -8.7% | -6.6% | 7.3M |
| UAL | 95.42 (08:45 sip) | -0.2% | 95.60 | 3.83 (4.0%) | 95.27-118.26 | -11.4% / -14.0% | -8.5% | 4.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-19 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SLN | 19.58 (08:40 sip) | +0.0% | 19.58 | 1.39 (7.1%) | 8.66-19.61 | +82.3% / +57.1% | +102.9% | 4.7M |
| IRON | 78.70 (08:49 sip) | -0.3% | 78.93 | 4.33 (5.5%) | 55.00-80.22 | +24.8% / +10.3% | +30.5% | 1.0M |
| AMRO | 5.20 (08:45 sip) | -7.3% | 5.61 | 2.57 (45.9%) | 3.57-8.64 | - / - | - | 1.7M |
| AXTX | 15.76 (08:49 sip) | -8.2% | 17.17 | 5.28 (30.7%) | 13.71-44.60 | -43.6% / -45.0% | -19.3% | 3.1M |
| IAM | 17.01 (08:49 sip) | +4.1% | 16.34 | 7.90 (48.3%) | 14.10-25.00 | - / - | - | 2.5M |
