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

- Time now: **09:05 ET** (13:05 UTC), Monday 2026-10-05. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$101,841.82**
- Cash: $62,148.19
- Session P&L so far: +0.11% (new entries are blocked at -3.0%)
- Gross exposure: $55,351 (54% of equity, cap 150%)
- Net exposure: $+39,694 (+39%, cap +/-100%)
- Risk at stake (entry to stop): $1,382 (1.36% of equity, cap 4.0%) — 2.64% left for new plays
- Slots: 3 open + 0 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| IWM | long | 111 | 281.50 | 281.85 | +39 (+0.1%) | 276.90 | 289.50 | Small caps are the most rate-damaged group (-4.5% vs 50d) and the most direct beneficiary of a rates reversal. A limit h |
| NVDA | long | 69 | 236.40 | 235.32 | -75 (-0.5%) | 227.40 | 246.00 | Only mega-cap with a dated positive catalyst and green on a red tape. A break through the 20d high of 234.50 means range |
| UNH | short | 21 | 363.57 | 372.80 | -194 (-2.5%) | 375.50 | 345.00 | Relative weakness in managed care: -5.2% vs 50d, losing its 20d floor while the market rallies. A trade below 363.50 con |

### Record

9 closed trades: 4W / 5L, total +1.39R, net $+2,074 realized. Shorts taken: 8.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| DAL | long | close | -0.53R | $-291 | 42% |
| XLRE | short | stop | -1.01R | $-529 | 40% |
| BAC | short | target | +1.53R | $+774 | 36% |
| HD | short | target | +1.36R | $+691 | 40% |
| BA | short | close | -0.52R | $-130 | 35% |

### Ideas you passed on, replayed against the tape

6 resolved: 2 reached target first, 4 stop first, 0 never reached the entry, 0 expired, 0 ambiguous. Average -0.11R across the 6 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-09-30 pre-market | TSLA | short | Best short: break of 20d low 349.92, but Q3 deliveries (~Oct 2) are a company bi | stop | -1.00R | 38% |
| 2026-10-01 pre-market | KRE | short | Same rates factor as BAC short already held; no slot. | stop | -1.00R | 40% |
| 2026-09-23 pre-market | SMH | long | Leadership group but +12% in 5 days; only worth owning on a pullback, not chasin | target | +1.67R | 40% |
| 2026-10-01 open | KRE | short | Broke 20d low but same financials/rates factor as BAC short already held. | stop | -0.99R | 40% |
| 2026-09-23 pre-market | BAC | short | stop entry 55.90 not placed: the market (55.885) had already crossed the trigger | target | +1.67R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IWM | 281.56 (08:49 sip) | +0.0% | 281.52 | 3.77 (1.3%) | 275.45-295.41 | -1.1% / -3.6% | -0.2% | 24.3M |
| NVDA | 235.30 (08:49 sip) | +0.6% | 233.95 | 5.15 (2.2%) | 208.93-237.88 | +4.6% / +7.3% | +3.9% | 111.4M |
| UNH | 373.16 (08:49 sip) | +0.3% | 371.90 | 7.34 (2.0%) | 362.60-404.04 | -1.7% / -5.1% | -1.2% | 5.1M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 768.60 (08:52 iex) | -0.1% | 769.64 | 7.12 (0.9%) | 747.74-775.14 | +0.7% / +1.0% | -0.2% | 46.2M |
| QQQ | 747.41 (08:49 sip) | -0.3% | 749.58 | 9.82 (1.3%) | 699.27-754.54 | +3.0% / +4.7% | +0.7% | 34.0M |
| IWM | 281.56 (08:49 sip) | +0.0% | 281.52 | 3.77 (1.3%) | 275.45-295.41 | -1.1% / -3.6% | -0.2% | 24.3M |
| DIA | 510.43 (08:49 sip) | -0.1% | 511.10 | 5.15 (1.0%) | 504.70-535.14 | -1.3% / -2.8% | -1.2% | 3.4M |
| TLT | 77.16 (08:58 iex) | -0.4% | 77.48 | 0.85 (1.1%) | 76.76-82.17 | -3.2% / -4.5% | -1.9% | 47.8M |
| GLD | 381.10 (08:49 sip) | +0.3% | 380.14 | 6.67 (1.8%) | 376.88-408.00 | -3.3% / -4.1% | -3.4% | 8.8M |
| USO | 145.35 (08:59 iex) | -1.4% | 147.37 | 5.98 (4.1%) | 138.01-163.35 | -2.2% / +7.3% | -0.6% | 6.6M |
| SMH | 628.20 (08:49 sip) | -0.4% | 630.60 | 14.55 (2.3%) | 537.73-636.25 | +8.0% / +10.7% | +4.0% | 6.5M |
| XLK | 199.50 (08:49 sip) | -0.2% | 199.81 | 3.05 (1.5%) | 181.87-201.39 | +4.5% / +7.3% | +1.8% | 7.3M |
| XLF | 53.52 (08:49 sip) | +0.1% | 53.49 | 0.75 (1.4%) | 52.81-58.17 | -3.6% / -5.6% | -2.5% | 38.0M |
| XLE | 62.65 (08:49 sip) | -0.3% | 62.82 | 1.22 (1.9%) | 60.95-65.78 | -0.7% / +1.6% | +1.3% | 34.6M |
| XLV | 165.78 (08:49 sip) | -0.2% | 166.18 | 2.23 (1.3%) | 164.48-171.87 | -1.1% / -1.1% | -2.6% | 8.1M |
| XLI | 169.80 (08:49 sip) | -0.1% | 169.95 | 2.29 (1.4%) | 166.18-175.30 | -0.0% / -3.7% | -0.3% | 7.4M |
| XLY | 109.88 (08:49 sip) | -0.1% | 110.04 | 1.56 (1.4%) | 107.99-115.49 | -1.0% / -3.6% | -0.5% | 6.7M |
| XLP | 80.71 (08:45 sip) | +0.2% | 80.53 | 0.88 (1.1%) | 80.13-84.74 | -2.2% / -4.1% | -1.9% | 11.0M |
| XLU | 39.95 (08:49 sip) | +0.3% | 39.83 | 0.55 (1.4%) | 39.03-43.39 | -2.4% / -6.1% | +0.8% | 29.6M |
| XLB | 48.92 (08:35 sip) | +0.1% | 48.86 | 0.73 (1.5%) | 47.81-52.43 | -2.5% / -4.9% | -1.9% | 11.7M |
| XLRE | 40.80 (08:35 sip) | -0.0% | 40.81 | 0.52 (1.3%) | 40.41-43.91 | -3.3% / -6.4% | -1.8% | 5.9M |
| XLC | 110.44 (08:49 sip) | +0.1% | 110.32 | 1.86 (1.7%) | 109.66-115.61 | -1.6% / -0.8% | -2.3% | 5.9M |
| KRE | 70.74 (08:49 sip) | -0.1% | 70.78 | 1.31 (1.8%) | 67.97-75.07 | -1.7% / -4.4% | -1.1% | 15.4M |
| XHB | no trade today | - | 96.70 | 2.18 (2.3%) | 94.08-102.95 | -0.9% / -5.8% | -1.6% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 332.00 (08:49 sip) | -0.5% | 333.69 | 6.50 (1.9%) | 309.90-345.34 | +0.5% / +3.5% | -2.2% | 42.4M |
| MSFT | 521.00 (09:05 iex) | +0.7% | 517.53 | 11.85 (2.3%) | 486.00-522.85 | +3.2% / +6.2% | +0.3% | 21.3M |
| NVDA | 235.30 (08:49 sip) | +0.6% | 233.95 | 5.15 (2.2%) | 208.93-237.88 | +4.6% / +7.3% | +3.9% | 111.4M |
| AMZN | 251.40 (08:55 iex) | -0.0% | 251.52 | 5.37 (2.1%) | 244.30-261.12 | -0.0% / -2.0% | +0.7% | 35.2M |
| GOOGL | 342.33 (08:49 sip) | -0.3% | 343.50 | 9.17 (2.7%) | 327.74-364.17 | +0.3% / -0.2% | -0.1% | 27.5M |
| META | 725.61 (08:49 sip) | -0.3% | 728.08 | 28.91 (4.0%) | 604.79-779.82 | +4.7% / +16.6% | -3.1% | 23.7M |
| TSLA | 367.81 (08:49 sip) | -0.8% | 370.59 | 11.46 (3.1%) | 345.88-386.83 | +1.6% / +6.6% | -0.4% | 38.4M |
| AVGO | 355.97 (08:49 sip) | +0.2% | 355.14 | 9.95 (2.8%) | 335.20-372.02 | +0.4% / -4.7% | +0.7% | 25.1M |
| AMD | 627.52 (08:49 iex) | -1.0% | 633.91 | 25.24 (4.0%) | 458.00-645.46 | +11.9% / +23.4% | +0.5% | 22.7M |
| ORCL | 142.13 (08:49 sip) | -0.1% | 142.30 | 6.34 (4.5%) | 131.58-170.70 | -2.5% / -0.9% | +3.8% | 36.3M |
| NFLX | 67.24 (08:49 sip) | +0.3% | 67.06 | 1.95 (2.9%) | 66.75-82.69 | -8.8% / -11.3% | -5.7% | 35.8M |
| CRM | 235.55 (08:40 sip) | +0.4% | 234.69 | 7.88 (3.4%) | 221.18-263.14 | -2.6% / +6.8% | +0.3% | 12.1M |
| JPM | 331.82 (08:49 sip) | -0.2% | 332.38 | 7.04 (2.1%) | 325.87-362.86 | -3.7% / -5.6% | -3.1% | 8.4M |
| GS | 904.63 (08:45 sip) | +0.2% | 902.56 | 24.28 (2.7%) | 881.00-1,043.84 | -5.9% / -9.8% | -3.5% | 2.1M |
| BAC | 53.91 (08:49 sip) | +0.3% | 53.75 | 1.11 (2.1%) | 52.89-63.83 | -7.4% / -11.4% | -5.2% | 38.9M |
| XOM | 163.40 (08:40 sip) | -0.4% | 164.01 | 3.59 (2.2%) | 155.85-169.64 | +0.8% / +2.4% | +2.1% | 14.1M |
| CVX | 205.70 (08:25 sip) | -0.5% | 206.69 | 4.17 (2.0%) | 200.78-217.78 | -0.9% / +2.4% | +1.1% | 9.8M |
| LLY | 1,142.00 (08:40 sip) | -0.1% | 1,142.85 | 31.20 (2.7%) | 1,113.29-1,215.00 | -0.7% / -2.8% | -3.4% | 2.3M |
| UNH | 373.16 (08:49 sip) | +0.3% | 371.90 | 7.34 (2.0%) | 362.60-404.04 | -1.7% / -5.1% | -1.2% | 5.1M |
| JNJ | 255.76 (08:45 sip) | -0.1% | 256.03 | 4.87 (1.9%) | 255.12-277.80 | -4.3% / -3.5% | -5.6% | 6.6M |
| WMT | 103.96 (08:49 sip) | -0.3% | 104.26 | 2.06 (2.0%) | 103.58-111.23 | -2.6% / -4.1% | -3.4% | 22.3M |
| COST | 919.15 (08:40 sip) | -0.2% | 920.65 | 15.12 (1.6%) | 883.10-931.09 | +1.4% / -1.3% | -0.2% | 2.4M |
| HD | 283.50 (08:49 sip) | +0.2% | 282.85 | 6.64 (2.3%) | 277.15-321.80 | -5.6% / -11.9% | -3.5% | 5.1M |
| CAT | 842.00 (08:30 sip) | -0.4% | 845.42 | 20.73 (2.5%) | 772.86-858.87 | +4.2% / +2.7% | +2.9% | 2.3M |
| BA | 193.77 (08:49 sip) | +0.1% | 193.56 | 7.18 (3.7%) | 184.01-215.29 | -3.2% / -8.8% | -2.3% | 8.5M |
| DAL | 84.61 (08:49 sip) | +0.6% | 84.09 | 2.44 (2.9%) | 76.89-86.17 | +3.3% / +0.0% | -1.0% | 7.4M |
| UAL | 113.18 (08:40 sip) | +0.6% | 112.51 | 4.07 (3.6%) | 104.59-118.26 | +2.0% / -2.9% | -1.3% | 3.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-02 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SDEV | 10.10 (08:49 sip) | +35.0% | 7.48 | 0.82 (10.9%) | 0.78-7.65 | +345.4% / +480.3% | +402.0% | 26.3M |
| XRPN | 41.59 (08:49 sip) | +5.5% | 39.42 | 3.71 (9.4%) | 10.51-53.00 | +202.1% / +242.3% | +272.6% | 1.1M |
| NXL | 5.25 (08:49 sip) | -8.4% | 5.73 | 1.07 (18.7%) | 4.00-10.98 | +17.0% / -26.7% | +30.5% | 3.2M |
| IART | 12.74 (07:45 sip) | +0.5% | 12.68 | 0.87 (6.9%) | 12.63-16.78 | -19.5% / -24.3% | -21.3% | 1.0M |
| WDCX | 14.93 (08:49 sip) | +4.3% | 14.31 | 1.95 (13.6%) | 12.86-21.01 | -16.6% / -25.4% | -18.3% | 2.3M |
