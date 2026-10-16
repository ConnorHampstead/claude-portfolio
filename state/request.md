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

- Time now: **09:05 ET** (13:05 UTC), Friday 2026-10-16. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$101,737.00**
- Cash: $132,607.56
- Session P&L so far: -0.06% (new entries are blocked at -3.0%)
- Gross exposure: $73,908 (73% of equity, cap 150%)
- Net exposure: $-1,239 (-1%, cap +/-100%)
- Risk at stake (entry to stop): $1,297 (1.27% of equity, cap 4.0%) — 2.73% left for new plays
- Slots: 1 open + 3 resting entries of 8 — you may add at most 4 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| IWM | short | 112 | 272.99 | 275.61 | -294 (-1.0%) | 275.60 | 267.00 | Small caps are the most rate-sensitive index; IWM opened below its 20d low 274.52 and is pinned at the session low, -4.7 |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| HD | long | 33 | 310.60 | stop | 303.00 | 322.00 | 2026-10-15 |
| CAT | short | 9 | 745.00 | limit | 772.00 | 700.00 | 2026-10-15 |
| WMT | long | 222 | 117.50 | limit | 115.20 | 122.10 | 2026-10-15 |

### Record

19 closed trades: 7W / 12L, total -0.46R, net $+2,040 realized. Shorts taken: 17.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |
| NVDA | long | stop | -0.38R | $-235 | 40% |

### Ideas you passed on, replayed against the tape

39 resolved: 9 reached target first, 22 stop first, 7 never reached the entry, 1 expired, 0 ambiguous. Average -0.30R across the 32 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-09 pre-market | XLE | long | Energy +4.1% over 5d and de-escalation removes the bid; wrong day to buy the dip | never filled | - | 35% |
| 2026-10-09 open | NVDA | long | Withdrawn after the open: semis faded the whole rebound, invalidating the follow | never filled | - | 30% |
| 2026-10-02 open | NKE | short | stop entry 34.90 not placed: the market (33.21) had already crossed the trigger | stop | -2.14R | 35% |
| 2026-10-08 open | COST | long | Cancelled resting buy stop after the open faded the whole comp gap from 953.29 t | target | +1.67R | 28% |
| 2026-10-14 pre-market | COST | long | Defensive breakout candidate, but staples with hot CPI and 5% yields are not a c | target | +1.39R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IWM | 275.44 (08:49 sip) | +0.1% | 275.08 | 3.76 (1.4%) | 270.35-288.94 | -1.8% / -4.9% | -0.9% | 26.0M |
| HD | 309.81 (08:49 sip) | +0.5% | 308.24 | 6.45 (2.1%) | 277.15-309.10 | +5.6% / -1.5% | +4.3% | 5.8M |
| CAT | 731.00 (08:35 sip) | -0.6% | 735.64 | 30.24 (4.1%) | 704.01-876.95 | -9.1% / -9.8% | -7.6% | 2.6M |
| WMT | 118.18 (08:49 sip) | +0.3% | 117.87 | 2.57 (2.2%) | 103.39-121.38 | +8.1% / +8.4% | +6.6% | 22.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 773.24 (09:03 iex) | +0.2% | 771.79 | 6.53 (0.8%) | 757.97-781.62 | +0.1% / +0.6% | -0.3% | 42.2M |
| QQQ | 726.50 (08:59 iex) | -0.2% | 728.00 | 9.52 (1.3%) | 714.34-762.86 | -2.0% / +0.2% | -2.6% | 35.2M |
| IWM | 275.44 (08:49 sip) | +0.1% | 275.08 | 3.76 (1.4%) | 270.35-288.94 | -1.8% / -4.9% | -0.9% | 26.0M |
| DIA | 521.89 (08:49 sip) | +0.2% | 521.07 | 4.99 (1.0%) | 504.59-522.69 | +1.3% / -0.5% | +1.9% | 3.3M |
| TLT | 79.95 (08:49 sip) | -0.0% | 79.97 | 0.87 (1.1%) | 76.43-81.61 | +1.6% / -0.6% | +2.7% | 50.1M |
| GLD | 382.67 (08:49 sip) | -0.0% | 382.71 | 6.03 (1.6%) | 373.36-403.15 | -0.7% / -3.7% | +1.1% | 7.8M |
| USO | 156.53 (08:49 sip) | -0.5% | 157.31 | 4.80 (3.0%) | 141.76-158.10 | +5.7% / +10.9% | +6.6% | 5.4M |
| SMH | 552.83 (08:50 iex) | -1.1% | 558.84 | 15.37 (2.8%) | 540.59-639.47 | -7.3% / -3.6% | -8.0% | 7.1M |
| XLK | 188.94 (08:45 sip) | -0.1% | 189.19 | 3.26 (1.7%) | 184.84-203.25 | -3.5% / -0.3% | -4.3% | 7.8M |
| XLF | 55.31 (08:40 sip) | +0.1% | 55.27 | 0.69 (1.2%) | 52.81-56.20 | +1.5% / -1.7% | +1.9% | 39.1M |
| XLE | 67.03 (08:49 sip) | +0.7% | 66.56 | 1.28 (1.9%) | 60.95-67.90 | +4.5% / +5.5% | +2.0% | 32.3M |
| XLV | 177.70 (08:49 sip) | +0.3% | 177.19 | 2.96 (1.7%) | 165.19-178.86 | +4.4% / +4.6% | +5.4% | 8.6M |
| XLI | 168.02 (08:35 sip) | +0.1% | 167.89 | 2.56 (1.5%) | 164.66-172.34 | -0.7% / -3.6% | -0.3% | 7.4M |
| XLY | 114.16 (08:45 sip) | +0.7% | 113.41 | 1.31 (1.2%) | 107.99-113.56 | +2.2% / -0.4% | +1.5% | 6.4M |
| XLP | 87.01 (08:45 sip) | +0.4% | 86.68 | 1.16 (1.3%) | 80.10-88.47 | +5.0% / +3.6% | +3.9% | 11.5M |
| XLU | 41.71 (08:49 sip) | +0.1% | 41.65 | 0.66 (1.6%) | 39.03-42.20 | +2.8% / -0.5% | +1.4% | 35.2M |
| XLB | 50.65 (08:15 sip) | +0.2% | 50.56 | 0.74 (1.5%) | 47.81-50.70 | +2.1% / -1.0% | +2.6% | 11.7M |
| XLRE | no trade today | - | 41.99 | 0.60 (1.4%) | 40.28-42.67 | +1.2% / -2.2% | +2.8% | 7.3M |
| XLC | 115.77 (05:15 sip) | +3.0% | 112.44 | 1.57 (1.4%) | 109.66-115.61 | +0.6% / +0.7% | +0.3% | 6.7M |
| KRE | 69.70 (08:35 sip) | -0.1% | 69.75 | 1.30 (1.9%) | 67.79-72.87 | -0.6% / -4.2% | +0.2% | 15.8M |
| XHB | 95.55 (08:10 sip) | -0.2% | 95.75 | 2.17 (2.3%) | 91.87-99.67 | -0.5% / -4.8% | +0.1% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 348.08 (08:49 sip) | +1.8% | 342.00 | 6.52 (1.9%) | 325.81-348.15 | +1.5% / +5.2% | +0.5% | 38.5M |
| MSFT | 540.34 (08:49 sip) | +0.2% | 539.44 | 11.35 (2.1%) | 491.10-551.15 | +4.0% / +6.9% | +3.2% | 23.1M |
| NVDA | 216.83 (08:49 sip) | -0.2% | 217.23 | 5.96 (2.7%) | 212.85-243.37 | -5.0% / -2.6% | -5.7% | 109.6M |
| AMZN | 254.61 (08:49 sip) | -0.1% | 254.76 | 5.76 (2.3%) | 244.72-263.70 | +0.5% / -1.1% | +0.3% | 36.4M |
| GOOGL | 349.09 (08:53 iex) | -0.0% | 349.22 | 8.45 (2.4%) | 335.51-364.17 | +0.7% / +1.3% | +0.3% | 26.2M |
| META | 736.00 (09:03 iex) | -0.1% | 736.72 | 22.31 (3.0%) | 660.28-779.82 | +0.4% / +12.9% | +2.2% | 22.2M |
| TSLA | 373.11 (09:02 iex) | +2.9% | 362.44 | 10.44 (2.9%) | 345.88-388.56 | -2.3% / +1.0% | -3.3% | 34.2M |
| AVGO | 341.15 (08:49 sip) | -0.9% | 344.33 | 11.29 (3.3%) | 334.61-380.84 | -3.5% / -6.2% | -4.4% | 23.1M |
| AMD | 552.00 (08:49 sip) | -1.8% | 562.23 | 26.22 (4.7%) | 530.09-658.52 | -8.1% / +4.8% | -9.4% | 21.8M |
| ORCL | 133.20 (09:00 iex) | -0.9% | 134.47 | 6.85 (5.1%) | 127.60-153.03 | -4.0% / -7.2% | -0.5% | 30.7M |
| NFLX | 70.09 (08:49 sip) | -3.5% | 72.61 | 1.65 (2.3%) | 66.54-73.87 | +3.2% / -3.4% | +1.5% | 38.7M |
| CRM | 250.81 (08:49 sip) | +1.7% | 246.74 | 8.43 (3.4%) | 220.29-247.18 | +5.9% / +7.8% | +8.3% | 9.7M |
| JPM | 336.25 (08:49 sip) | +0.2% | 335.53 | 5.96 (1.8%) | 324.25-352.74 | +0.1% / -3.3% | +1.2% | 8.7M |
| GS | 890.00 (08:25 sip) | -0.1% | 891.28 | 21.45 (2.4%) | 859.03-967.76 | -2.0% / -8.7% | +1.0% | 2.4M |
| BAC | 51.71 (08:49 sip) | +0.0% | 51.70 | 1.25 (2.4%) | 49.26-58.28 | -5.5% / -12.6% | -3.6% | 42.0M |
| XOM | 176.12 (08:50 iex) | +0.8% | 174.68 | 3.41 (2.0%) | 155.85-178.69 | +5.6% / +7.1% | +3.7% | 13.0M |
| CVX | 220.66 (08:49 sip) | +0.6% | 219.32 | 4.35 (2.0%) | 200.78-223.46 | +5.0% / +6.4% | +3.7% | 9.4M |
| LLY | 1,256.38 (08:30 sip) | +0.4% | 1,251.61 | 37.08 (3.0%) | 1,131.21-1,275.88 | +6.7% / +6.2% | +7.0% | 2.4M |
| UNH | 409.80 (08:49 sip) | +0.8% | 406.67 | 11.93 (2.9%) | 362.60-414.12 | +7.8% / +5.3% | +9.6% | 6.0M |
| JNJ | 254.10 (08:49 sip) | +0.3% | 253.28 | 6.46 (2.6%) | 245.17-275.23 | -3.4% / -4.4% | -1.2% | 7.9M |
| WMT | 118.18 (08:49 sip) | +0.3% | 117.87 | 2.57 (2.2%) | 103.39-121.38 | +8.1% / +8.4% | +6.6% | 22.9M |
| COST | 979.98 (08:40 sip) | +0.2% | 978.01 | 16.24 (1.7%) | 883.10-1,008.37 | +5.3% / +4.8% | +3.2% | 2.4M |
| HD | 309.81 (08:49 sip) | +0.5% | 308.24 | 6.45 (2.1%) | 277.15-309.10 | +5.6% / -1.5% | +4.3% | 5.8M |
| CAT | 731.00 (08:35 sip) | -0.6% | 735.64 | 30.24 (4.1%) | 704.01-876.95 | -9.1% / -9.8% | -7.6% | 2.6M |
| BA | 190.48 (08:49 sip) | +0.9% | 188.73 | 5.55 (2.9%) | 183.38-204.06 | -1.6% / -8.5% | +0.5% | 8.6M |
| DAL | 78.10 (08:45 sip) | +0.0% | 78.08 | 2.46 (3.1%) | 75.54-85.93 | -4.8% / -5.3% | -4.7% | 8.4M |
| UAL | 101.25 (08:49 sip) | -0.1% | 101.31 | 3.73 (3.7%) | 97.70-118.26 | -7.4% / -10.0% | -5.7% | 4.5M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-15 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| FMC | 5.49 (08:49 sip) | -2.3% | 5.62 | 0.64 (11.3%) | 4.84-10.67 | -37.0% / -45.0% | -37.0% | 6.2M |
