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

- Time now: **09:05 ET** (13:05 UTC, 14:05 Stockholm), Friday 2026-10-30. The cash session opens at 09:30 ET (14:30 Stockholm), in 25 min, and closes at 16:00 ET (21:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,709.05**
- Cash: $91,149.59
- Session P&L so far: -0.02% (new entries are blocked at -3.0%)
- Gross exposure: $53,002 (52% of equity, cap 150%)
- Net exposure: $+15,139 (+15%, cap +/-100%)
- Risk at stake (entry to stop): $1,585 (1.54% of equity, cap 4.0%) — 2.46% left for new plays
- Slots: 3 open + 2 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 72.82 | -34 (-0.3%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| META | short | 9 | 616.20 | 611.25 | +45 (+0.8%) | 643.00 | 580.00 | Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward  |
| TSLA | long | 17 | 398.69 | 395.31 | -57 (-0.8%) | 395.00 | 421.00 | Relative strength at the range top while megacap tech chops; a clean 20d-high break opens room toward 420. |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GOOGL | short | 48 | 279.80 | stop | 290.50 | 258.40 | 2026-10-29 |
| XLE | long | 243 | 70.00 | stop | 67.90 | 73.20 | 2026-10-28 |

### Record

32 closed trades: 12W / 20L, total +2.86R, net $+2,767 realized. Shorts taken: 30.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| MSFT | long | close | -0.80R | $-324 | 38% |
| XLV | long | target | +1.65R | $+837 | 40% |
| NVDA | short | close | -0.76R | $-190 | 35% |
| XOM | long | stop | -0.07R | $-37 | 37% |
| BA | short | target | +1.52R | $+379 | 34% |

### Ideas you passed on, replayed against the tape

70 resolved: 18 reached target first, 33 stop first, 13 never reached the entry, 6 expired, 0 ambiguous. Average -0.08R across the 57 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-23 pre-market | META | short | Already through the prior target after -11.9% in 5d; chasing. AVGO is the cleane | never filled | - | 33% |
| 2026-10-16 pre-market | XLE | long | Energy +50% YTD with Brent at $105; XOM's intraday reversal from its high yester | expired | +0.35R | 35% |
| 2026-10-22 open | META | short | Short on a bounce after the -5.9% earnings break; no slot, would be a 5th AI-cap | never filled | - | 33% |
| 2026-10-15 pre-market | TLT | long | The flight-to-safety rally is fighting a 6.3% PPI print; two-sided, no edge. | expired | +1.21R | 35% |
| 2026-10-15 pre-market | NVDA | short | At its 20d low after -6.8% in 5 days; duplicates the semis factor I'm exiting at | expired | +0.94R | 34% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| KRE | 72.85 (08:49 sip) | -0.0% | 72.86 | 1.29 (1.8%) | 67.79-73.45 | +3.3% / +1.4% | +0.6% | 14.7M |
| META | 613.42 (08:49 sip) | -1.8% | 624.52 | 26.29 (4.2%) | 609.00-771.27 | -10.4% / -6.6% | -3.7% | 22.6M |
| TSLA | 395.08 (09:01 iex) | -2.0% | 403.30 | 13.56 (3.4%) | 349.33-410.85 | +6.3% / +9.4% | +7.7% | 37.3M |
| GOOGL | 280.28 (08:49 sip) | -1.2% | 283.82 | 10.78 (3.8%) | 280.36-359.40 | -15.8% / -16.6% | -12.5% | 31.1M |
| XLE | 69.73 (08:49 sip) | +1.5% | 68.71 | 1.42 (2.1%) | 61.86-69.86 | +2.9% / +6.3% | +1.7% | 31.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 761.42 (08:49 sip) | -1.0% | 769.36 | 7.11 (0.9%) | 758.68-781.62 | -0.2% / +0.3% | +0.7% | 37.8M |
| QQQ | 697.10 (09:04 iex) | -2.5% | 715.34 | 12.56 (1.8%) | 701.16-762.86 | -2.2% / -1.3% | +1.5% | 36.9M |
| IWM | 282.22 (08:49 sip) | -0.6% | 284.01 | 3.61 (1.3%) | 269.88-285.26 | +2.3% / -0.1% | +2.7% | 24.3M |
| DIA | 522.16 (08:49 sip) | -0.1% | 522.73 | 4.99 (1.0%) | 507.73-528.45 | +0.7% / +0.3% | -1.0% | 3.3M |
| TLT | 81.81 (09:03 iex) | +0.4% | 81.49 | 0.82 (1.0%) | 76.43-81.92 | +2.6% / +1.5% | -0.3% | 39.3M |
| GLD | 362.57 (08:49 sip) | -1.6% | 368.57 | 5.13 (1.4%) | 364.33-385.22 | -2.2% / -5.9% | -0.1% | 8.0M |
| USO | 170.64 (08:49 sip) | +1.5% | 168.19 | 4.86 (2.9%) | 141.76-169.96 | +7.4% / +12.6% | +3.5% | 4.7M |
| SMH | 532.50 (08:56 iex) | -5.2% | 561.67 | 18.44 (3.3%) | 520.53-639.47 | -2.4% / -2.0% | +7.3% | 8.8M |
| XLK | 182.08 (08:49 sip) | -3.5% | 188.74 | 4.24 (2.2%) | 181.50-203.25 | -1.6% / -0.5% | +3.5% | 8.7M |
| XLF | 57.31 (08:49 sip) | +0.6% | 56.94 | 0.72 (1.3%) | 53.21-57.23 | +3.2% / +1.9% | +0.5% | 32.3M |
| XLE | 69.73 (08:49 sip) | +1.5% | 68.71 | 1.42 (2.1%) | 61.86-69.86 | +2.9% / +6.3% | +1.7% | 31.3M |
| XLV | 186.95 (08:49 sip) | +1.6% | 184.04 | 3.15 (1.7%) | 165.19-184.85 | +5.3% / +7.2% | +1.5% | 8.8M |
| XLI | 169.52 (08:45 sip) | -0.4% | 170.13 | 2.58 (1.5%) | 162.97-172.34 | +1.1% / -0.4% | +2.0% | 7.4M |
| XLY | 114.54 (08:25 sip) | -1.4% | 116.20 | 1.67 (1.4%) | 109.50-116.77 | +2.6% / +2.7% | +1.0% | 7.1M |
| XLP | 90.29 (08:49 sip) | +2.4% | 88.18 | 1.39 (1.6%) | 80.10-89.99 | +3.1% / +4.6% | -2.0% | 14.1M |
| XLU | 43.55 (08:49 sip) | +1.0% | 43.14 | 0.62 (1.4%) | 39.58-43.25 | +3.3% / +3.6% | +0.6% | 29.9M |
| XLB | 52.58 (08:35 sip) | +0.1% | 52.53 | 0.67 (1.3%) | 48.51-52.53 | +4.0% / +3.2% | +1.6% | 10.6M |
| XLRE | 43.48 (08:40 sip) | +1.0% | 43.06 | 0.65 (1.5%) | 40.28-43.21 | +2.9% / +1.2% | +1.3% | 8.0M |
| XLC | 100.28 (08:49 sip) | -0.9% | 101.21 | 1.87 (1.8%) | 100.13-113.17 | -7.1% / -8.6% | -5.8% | 6.7M |
| KRE | 72.85 (08:49 sip) | -0.0% | 72.86 | 1.29 (1.8%) | 67.79-73.45 | +3.3% / +1.4% | +0.6% | 14.7M |
| XHB | 101.57 (08:49 sip) | +0.3% | 101.27 | 2.43 (2.4%) | 91.87-101.29 | +5.1% / +2.8% | +2.1% | 2.2M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 345.02 (09:04 iex) | -1.1% | 348.91 | 6.06 (1.7%) | 330.61-351.73 | +2.2% / +5.0% | +0.2% | 38.8M |
| MSFT | 527.28 (08:49 sip) | -0.5% | 530.14 | 11.16 (2.1%) | 513.66-551.15 | -0.1% / +3.5% | +1.7% | 21.2M |
| NVDA | 208.47 (08:56 iex) | -2.4% | 213.66 | 5.94 (2.8%) | 210.18-243.37 | -4.2% / -3.7% | +0.7% | 100.1M |
| AMZN | 225.74 (08:56 iex) | -7.4% | 243.79 | 7.00 (2.9%) | 241.24-265.34 | -4.4% / -4.3% | -2.6% | 38.2M |
| GOOGL | 280.28 (08:49 sip) | -1.2% | 283.82 | 10.78 (3.8%) | 280.36-359.40 | -15.8% / -16.6% | -12.5% | 31.1M |
| META | 613.42 (08:49 sip) | -1.8% | 624.52 | 26.29 (4.2%) | 609.00-771.27 | -10.4% / -6.6% | -3.7% | 22.6M |
| TSLA | 395.08 (09:01 iex) | -2.0% | 403.30 | 13.56 (3.4%) | 349.33-410.85 | +6.3% / +9.4% | +7.7% | 37.3M |
| AVGO | 330.00 (08:56 iex) | -4.3% | 345.00 | 11.66 (3.4%) | 320.23-380.84 | -0.6% / -2.3% | +6.7% | 21.7M |
| AMD | 514.50 (09:00 iex) | -9.2% | 566.42 | 28.43 (5.0%) | 502.60-658.52 | -1.8% / +3.4% | +11.5% | 19.6M |
| ORCL | 133.65 (08:49 sip) | -4.2% | 139.56 | 7.65 (5.5%) | 122.76-148.48 | +3.2% / -1.5% | +11.2% | 31.4M |
| NFLX | 62.54 (09:00 iex) | +0.8% | 62.05 | 2.10 (3.4%) | 61.39-73.07 | -8.5% / -15.0% | -7.5% | 44.1M |
| CRM | 230.00 (08:49 sip) | -0.4% | 230.90 | 9.66 (4.2%) | 220.29-252.42 | -2.8% / -3.1% | -7.7% | 7.1M |
| JPM | 344.55 (08:49 sip) | +0.3% | 343.58 | 6.49 (1.9%) | 325.07-345.75 | +2.7% / +0.3% | +2.1% | 6.9M |
| GS | 912.00 (08:49 sip) | -1.7% | 927.73 | 24.97 (2.7%) | 859.03-939.38 | +3.7% / -2.2% | +4.1% | 2.3M |
| BAC | 51.32 (08:49 sip) | +0.3% | 51.14 | 1.25 (2.5%) | 49.26-54.93 | -1.9% / -9.7% | +0.1% | 40.7M |
| XOM | 186.50 (08:49 sip) | +1.8% | 183.29 | 4.02 (2.2%) | 161.39-184.88 | +4.8% / +9.5% | +2.8% | 11.5M |
| CVX | 234.90 (08:49 sip) | +1.5% | 231.46 | 4.71 (2.0%) | 201.96-234.08 | +5.1% / +8.9% | +2.1% | 7.3M |
| LLY | 1,413.05 (08:45 sip) | +2.9% | 1,373.70 | 43.95 (3.2%) | 1,131.21-1,408.38 | +11.5% / +15.1% | +5.1% | 2.4M |
| UNH | 416.39 (08:49 sip) | +1.3% | 410.91 | 12.86 (3.1%) | 364.47-426.55 | +3.5% / +5.6% | -3.3% | 6.0M |
| JNJ | 280.00 (08:49 sip) | +1.7% | 275.20 | 7.39 (2.7%) | 245.17-278.05 | +5.9% / +3.7% | +2.8% | 7.8M |
| WMT | 123.80 (08:49 sip) | +2.1% | 121.25 | 2.54 (2.1%) | 103.39-122.40 | +5.4% / +10.4% | +0.1% | 19.6M |
| COST | 1,014.77 (08:40 sip) | +2.0% | 994.61 | 16.67 (1.7%) | 908.32-1,019.94 | +2.3% / +5.8% | -2.2% | 2.1M |
| HD | 332.56 (08:45 sip) | +1.1% | 328.98 | 7.51 (2.3%) | 279.76-329.01 | +8.0% / +6.8% | +0.4% | 4.8M |
| CAT | 632.00 (08:45 sip) | -2.4% | 647.39 | 30.88 (4.8%) | 631.01-874.87 | -14.1% / -17.6% | -7.8% | 3.0M |
| BA | 171.25 (08:49 sip) | -0.8% | 172.65 | 5.76 (3.3%) | 165.01-196.93 | -7.4% / -12.4% | -7.9% | 10.1M |
| DAL | 80.31 (08:49 sip) | -1.6% | 81.64 | 3.09 (3.8%) | 74.14-85.93 | +2.5% / +1.6% | +3.0% | 7.2M |
| UAL | 103.11 (08:45 sip) | -2.0% | 105.21 | 4.89 (4.7%) | 94.54-115.20 | +1.5% / -2.4% | +3.1% | 5.2M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-29 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| PCLA | 9.88 (08:49 sip) | -11.0% | 11.10 | 0.82 (7.4%) | 5.71-12.40 | +69.5% / +58.7% | +82.5% | 1.5M |
| GKOS | 242.50 (08:35 sip) | +0.0% | 242.48 | 10.47 (4.3%) | 146.38-243.71 | +39.5% / +40.8% | +37.2% | 1.3M |
| ADT | 9.88 (08:49 sip) | +0.1% | 9.87 | 0.37 (3.8%) | 6.19-9.99 | +44.5% / +42.9% | +41.2% | 15.1M |
| BHC | 8.78 (08:45 sip) | -1.5% | 8.91 | 0.42 (4.7%) | 5.61-9.04 | +40.5% / +43.5% | +37.3% | 3.9M |
| PRCH | 20.72 (08:45 sip) | -0.8% | 20.89 | 1.17 (5.6%) | 16.07-21.30 | +18.4% / +21.7% | +16.4% | 1.9M |
| TDOC | 8.62 (08:49 sip) | -1.3% | 8.73 | 0.42 (4.8%) | 5.42-8.99 | +42.5% / +41.0% | +38.1% | 4.7M |
| CROX | 151.50 (08:30 sip) | +0.8% | 150.26 | 6.15 (4.1%) | 114.08-151.82 | +24.6% / +25.4% | +24.2% | 1.2M |
| PURR | 11.28 (08:54 iex) | -8.2% | 12.29 | 0.84 (6.9%) | 8.47-13.05 | +18.9% / +7.7% | +41.6% | 14.2M |
| IOVA | 9.15 (08:57 iex) | -4.3% | 9.56 | 1.20 (12.6%) | 9.35-15.37 | -31.3% / -16.0% | -32.4% | 13.9M |
| AIOK | 20.68 (08:49 sip) | +9.5% | 18.89 | 4.35 (23.0%) | 3.90-29.90 | - / - | +344.5% | 7.2M |
| NOW | 108.82 (08:49 sip) | -0.8% | 109.67 | 9.08 (8.3%) | 108.68-159.50 | -23.7% / -21.2% | -30.1% | 15.9M |
| MVLL | 19.98 (08:49 sip) | -12.1% | 22.74 | 4.40 (19.3%) | 21.82-45.89 | -28.9% / -26.3% | -7.1% | 2.3M |
| GGLL | 63.80 (08:49 sip) | -2.6% | 65.50 | 6.02 (9.2%) | 63.70-108.08 | -31.1% / -32.9% | -25.1% | 2.1M |
| ALNY | 173.37 (08:45 sip) | -0.4% | 174.00 | 11.45 (6.6%) | 172.31-238.96 | -22.5% / -26.8% | -23.4% | 1.9M |
| SFM | 48.67 (08:49 sip) | +1.4% | 48.00 | 3.85 (8.0%) | 47.35-69.53 | -25.3% / -31.7% | -30.3% | 3.2M |
