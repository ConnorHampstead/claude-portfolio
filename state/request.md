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

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Monday 2026-11-09. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,014.08**
- Cash: $117,953.54
- Session P&L so far: +0.41% (new entries are blocked at -3.0%)
- Gross exposure: $14,939 (15% of equity, cap 150%)
- Net exposure: $-14,939 (-15%, cap +/-100%)
- Risk at stake (entry to stop): $604 (0.59% of equity, cap 4.0%) — 3.41% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AVGO | short | 18 | 302.03 | 302.63 | -11 (-0.2%) | 316.00 | 281.00 | A megacap chip fading from its opening print shows supply meeting the post-crash bounce; continuation retests the 290.12 |
| NVDA | short | 54 | 194.96 | 175.78 | +1,036 (+9.8%) | 201.50 | 178.00 | The largest AI-capex position has lost its 20-day range while semis sell off even on good news. The path of least resist |

### Record

44 closed trades: 14W / 30L, total -0.32R, net $+2,003 realized. Shorts taken: 37.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |
| KRE | long | stop | -0.04R | $-10 | 37% |
| SMH | short | target | +1.72R | $+873 | 34% |
| GOOGL | short | stop | -1.00R | $-522 | 30% |

### Ideas you passed on, replayed against the tape

100 resolved: 31 reached target first, 42 stop first, 20 never reached the entry, 7 expired, 0 ambiguous. Average +0.10R across the 80 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-11-02 pre-market | UAL | long | Chasing a +4.6% gap whose catalyst is a single Iran headline that can reverse ov | never filled | - | 40% |
| 2026-10-30 pre-market | LLY | long | Chasing +2.9% above the 20d high; defensive exposure already taken via XLP. | stop | -1.21R | 36% |
| 2026-11-04 open | XLF | long | Breakout above the 57.70 20d high, but stacks with KRE near the 40% financials s | stop | -1.19R | 38% |
| 2026-10-27 pre-market | META | short | A third AI short into an AI-financing relief bid, with MSFT/GOOGL read-through W | target | +1.39R | 33% |
| 2026-11-05 pre-market | AMD | short | Below its 20d low, but the 6.6% ATR makes the stop wide and it doubles the semis | target | +1.40R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AVGO | 302.77 (08:49 sip) | +3.1% | 293.69 | 15.14 (5.2%) | 289.77-360.69 | -11.6% / -15.5% | -9.9% | 23.9M |
| NVDA | 175.64 (09:04 iex) | -5.9% | 186.64 | 8.02 (4.3%) | 181.46-228.86 | -11.8% / -15.1% | -8.8% | 118.4M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 742.20 (08:49 sip) | +0.9% | 735.29 | 11.12 (1.5%) | 732.71-779.40 | -3.7% / -3.9% | -2.7% | 47.1M |
| QQQ | 662.05 (09:01 iex) | +0.9% | 656.10 | 16.61 (2.5%) | 647.05-749.79 | -7.3% / -9.0% | -5.0% | 49.9M |
| IWM | 277.76 (08:49 sip) | +1.5% | 273.67 | 4.73 (1.7%) | 269.88-286.17 | -1.1% / -2.9% | -2.0% | 25.5M |
| DIA | 518.57 (08:49 sip) | +1.2% | 512.22 | 7.40 (1.4%) | 508.66-536.60 | -1.7% / -1.5% | -0.9% | 3.9M |
| TLT | 82.20 (09:00 iex) | +0.3% | 81.92 | 0.77 (0.9%) | 77.41-82.42 | +1.8% / +2.5% | +0.5% | 38.3M |
| GLD | 377.50 (08:49 sip) | +1.3% | 372.52 | 6.68 (1.8%) | 354.67-384.88 | -0.1% / -3.2% | +4.7% | 8.9M |
| USO | 142.88 (08:49 sip) | -3.7% | 148.41 | 5.90 (4.0%) | 142.96-171.82 | -6.7% / -2.5% | -12.1% | 5.3M |
| SMH | 465.84 (08:49 sip) | +0.4% | 463.96 | 24.64 (5.3%) | 445.59-598.45 | -13.6% / -18.0% | -11.2% | 11.6M |
| XLK | 165.60 (08:49 sip) | +0.5% | 164.74 | 5.53 (3.4%) | 162.14-198.18 | -10.2% / -12.5% | -8.2% | 12.1M |
| XLF | 57.84 (08:49 sip) | +1.2% | 57.16 | 1.00 (1.7%) | 54.02-60.04 | +1.7% / +2.3% | +1.2% | 35.6M |
| XLE | 61.30 (08:49 sip) | -0.5% | 61.62 | 1.84 (3.0%) | 61.20-70.15 | -8.2% / -5.1% | -12.0% | 36.3M |
| XLV | 186.87 (08:49 sip) | +1.1% | 184.80 | 3.79 (2.1%) | 169.48-192.32 | +2.7% / +6.7% | -0.0% | 11.4M |
| XLI | 165.78 (08:49 sip) | +1.9% | 162.67 | 3.21 (2.0%) | 161.74-172.40 | -2.9% / -3.9% | -2.8% | 8.9M |
| XLY | 119.55 (08:35 sip) | +1.7% | 117.58 | 2.46 (2.1%) | 110.67-122.92 | +2.0% / +3.8% | +1.9% | 9.1M |
| XLP | 90.32 (08:49 sip) | +0.3% | 90.08 | 1.78 (2.0%) | 83.39-93.40 | +2.3% / +6.1% | +0.7% | 19.0M |
| XLU | 43.63 (08:49 sip) | +1.2% | 43.13 | 0.62 (1.4%) | 41.09-44.09 | +1.3% / +3.5% | -0.7% | 27.8M |
| XLB | 52.78 (08:45 sip) | +1.6% | 51.95 | 0.96 (1.8%) | 49.16-54.63 | +0.7% / +2.1% | -1.5% | 12.2M |
| XLRE | 44.35 (08:35 sip) | +0.8% | 44.00 | 0.75 (1.7%) | 41.31-45.34 | +2.9% / +3.7% | +1.9% | 8.4M |
| XLC | 106.38 (08:35 sip) | +1.5% | 104.79 | 2.16 (2.1%) | 99.33-113.17 | -1.5% / -4.5% | +4.9% | 8.1M |
| KRE | 73.00 (08:10 sip) | +1.1% | 72.20 | 1.64 (2.3%) | 67.79-75.80 | +1.0% / +0.7% | +0.3% | 15.0M |
| XHB | no trade today | - | 102.29 | 3.15 (3.1%) | 91.87-108.78 | +3.7% / +4.1% | +1.3% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 344.13 (08:49 sip) | +0.5% | 342.37 | 9.02 (2.6%) | 325.33-355.38 | -0.3% / +1.9% | -0.7% | 48.9M |
| MSFT | 542.44 (08:59 iex) | +2.2% | 530.61 | 15.88 (3.0%) | 504.96-559.15 | -0.2% / +2.7% | +1.7% | 25.8M |
| NVDA | 175.64 (09:04 iex) | -5.9% | 186.64 | 8.02 (4.3%) | 181.46-228.86 | -11.8% / -15.1% | -8.8% | 118.4M |
| AMZN | 267.73 (09:02 iex) | +3.3% | 259.30 | 9.76 (3.8%) | 229.36-273.23 | +2.0% / +2.1% | +7.9% | 48.5M |
| GOOGL | 291.79 (09:04 iex) | +2.5% | 284.78 | 11.30 (4.0%) | 276.92-359.40 | -10.3% / -14.5% | +1.8% | 39.1M |
| META | 629.00 (09:00 iex) | +3.1% | 610.15 | 23.83 (3.9%) | 583.80-771.27 | -7.9% / -9.6% | -0.8% | 25.2M |
| TSLA | 360.13 (08:49 sip) | +0.5% | 358.22 | 17.99 (5.0%) | 338.15-414.23 | -5.8% / -3.7% | -10.4% | 40.1M |
| AVGO | 302.77 (08:49 sip) | +3.1% | 293.69 | 15.14 (5.2%) | 289.77-360.69 | -11.6% / -15.5% | -9.9% | 23.9M |
| AMD | 466.34 (08:49 sip) | +3.9% | 449.04 | 38.02 (8.5%) | 402.10-606.20 | -14.8% / -17.9% | -11.0% | 27.6M |
| ORCL | 117.00 (08:49 sip) | +0.8% | 116.10 | 8.89 (7.7%) | 109.21-148.48 | -10.2% / -16.4% | -11.2% | 43.6M |
| NFLX | 63.47 (08:49 sip) | +0.1% | 63.41 | 2.21 (3.5%) | 61.39-73.07 | -4.3% / -10.7% | +2.1% | 46.6M |
| CRM | 215.98 (08:45 sip) | +1.1% | 213.65 | 9.50 (4.4%) | 211.00-252.42 | -9.5% / -10.8% | -6.8% | 7.4M |
| JPM | 339.10 (09:03 iex) | +1.4% | 334.49 | 7.88 (2.4%) | 326.40-359.80 | -0.8% / -1.9% | -0.8% | 7.5M |
| GS | 883.00 (08:49 sip) | +2.0% | 865.82 | 28.69 (3.3%) | 854.45-939.38 | -3.1% / -7.1% | -3.2% | 2.4M |
| BAC | 50.19 (08:49 sip) | +1.5% | 49.42 | 1.23 (2.5%) | 49.17-54.93 | -3.1% / -10.5% | -1.2% | 44.5M |
| XOM | 164.96 (08:49 sip) | -0.5% | 165.87 | 5.20 (3.1%) | 163.51-188.50 | -6.5% / -1.7% | -11.4% | 13.8M |
| CVX | 211.47 (08:49 sip) | -0.5% | 212.61 | 5.74 (2.7%) | 210.43-236.48 | -5.2% / -1.1% | -9.7% | 8.2M |
| LLY | 1,366.56 (08:54 iex) | +0.9% | 1,354.00 | 52.81 (3.9%) | 1,158.40-1,453.00 | +4.0% / +11.5% | -4.5% | 3.0M |
| UNH | 395.70 (08:40 sip) | +0.4% | 394.15 | 11.98 (3.0%) | 372.80-426.55 | -2.6% / +1.0% | -3.2% | 6.1M |
| JNJ | 279.00 (08:40 sip) | +1.0% | 276.22 | 7.86 (2.8%) | 245.17-282.01 | +4.4% / +3.9% | +1.1% | 8.2M |
| WMT | 125.28 (08:49 sip) | -0.2% | 125.52 | 3.22 (2.6%) | 111.31-131.82 | +4.1% / +11.6% | +1.6% | 22.5M |
| COST | 1,053.50 (08:45 sip) | -0.0% | 1,053.56 | 20.80 (2.0%) | 945.30-1,081.55 | +5.0% / +10.8% | +4.1% | 2.4M |
| HD | 350.33 (08:49 sip) | +2.0% | 343.47 | 10.08 (2.9%) | 288.51-362.44 | +7.0% / +11.1% | +4.3% | 4.8M |
| CAT | 571.32 (08:49 sip) | +2.3% | 558.63 | 30.62 (5.5%) | 550.81-810.07 | -18.3% / -26.4% | -10.3% | 3.8M |
| BA | 176.10 (08:49 sip) | +1.6% | 173.40 | 6.32 (3.6%) | 165.01-193.28 | -4.4% / -9.9% | +1.1% | 10.1M |
| DAL | 91.07 (08:49 sip) | +4.4% | 87.20 | 3.54 (4.1%) | 74.14-89.92 | +8.6% / +8.1% | +8.8% | 6.7M |
| UAL | 117.25 (08:49 sip) | +4.0% | 112.74 | 5.82 (5.2%) | 94.54-117.01 | +8.8% / +5.0% | +8.2% | 5.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-11-06 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IONL | 7.20 (08:49 sip) | -1.6% | 7.32 | 1.07 (14.6%) | 4.36-11.73 | -0.9% / -32.6% | +10.6% | 1.3M |
| IONX | 12.86 (09:04 iex) | -1.1% | 13.01 | 1.90 (14.6%) | 7.72-21.08 | -1.3% / -33.7% | +10.2% | 1.3M |
| KRMN | 45.30 (08:49 sip) | -0.7% | 45.61 | 3.66 (8.0%) | 29.34-45.90 | +26.5% / +27.1% | +14.2% | 3.7M |
| FLY | 20.86 (08:49 sip) | +0.5% | 20.76 | 1.77 (8.5%) | 14.45-20.88 | +16.0% / +2.2% | +15.8% | 3.4M |
| IREZ | 21.70 (08:45 sip) | +7.9% | 20.12 | 5.55 (27.6%) | 11.67-35.88 | -1.1% / +44.0% | -11.6% | 1.8M |
| AEHL | 12.00 (08:49 sip) | -4.0% | 12.50 | 2.24 (17.9%) | 6.17-30.60 | +36.6% / +43.2% | +71.0% | 2.6M |
