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

- Time now: **09:05 ET** (13:05 UTC, 14:05 Stockholm), Thursday 2026-10-29. The cash session opens at 09:30 ET (14:30 Stockholm), in 25 min, and closes at 16:00 ET (21:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,930.25**
- Cash: $61,906.50
- Session P&L so far: +0.65% (new entries are blocked at -3.0%)
- Gross exposure: $69,175 (67% of equity, cap 150%)
- Net exposure: $+58,034 (+56%, cap +/-100%)
- Risk at stake (entry to stop): $1,578 (1.53% of equity, cap 4.0%) — 2.47% left for new plays
- Slots: 4 open + 1 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 44% of equity in notional: at 1% risk its stop must be at least 2.3% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 72.60 | -65 (-0.6%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| META | short | 9 | 616.20 | 618.95 | -25 (-0.4%) | 643.00 | 580.00 | Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward  |
| TSLA | long | 17 | 398.69 | 405.19 | +111 (+1.6%) | 395.00 | 421.00 | Relative strength at the range top while megacap tech chops; a clean 20d-high break opens room toward 420. |
| XLV | long | 160 | 179.57 | 183.73 | +666 (+2.3%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XLE | long | 243 | 70.00 | stop | 67.90 | 73.20 | 2026-10-28 |

### Record

30 closed trades: 11W / 19L, total +2.01R, net $+2,254 realized. Shorts taken: 28.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| NVDA | short | close | -0.76R | $-190 | 35% |
| XOM | long | stop | -0.07R | $-37 | 37% |
| BA | short | target | +1.52R | $+379 | 34% |
| ORCL | short | stop | -0.06R | $-16 | 33% |
| UAL | short | stop | -0.45R | $-315 | 40% |

### Ideas you passed on, replayed against the tape

68 resolved: 18 reached target first, 33 stop first, 12 never reached the entry, 5 expired, 0 ambiguous. Average -0.09R across the 56 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-22 open | META | short | Short on a bounce after the -5.9% earnings break; no slot, would be a 5th AI-cap | never filled | - | 33% |
| 2026-10-15 pre-market | TLT | long | The flight-to-safety rally is fighting a 6.3% PPI print; two-sided, no edge. | expired | +1.21R | 35% |
| 2026-10-15 pre-market | NVDA | short | At its 20d low after -6.8% in 5 days; duplicates the semis factor I'm exiting at | expired | +0.94R | 34% |
| 2026-10-23 open | CAT | short | Under its 695 20d low, but the Q3 earnings date is likely inside the horizon and | stop | -1.04R | 38% |
| 2026-10-22 pre-market | AVGO | short | Same AI factor as the existing shorts; no slot. | stop | -1.10R | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| KRE | 72.60 (08:40 sip) | +0.7% | 72.11 | 1.24 (1.7%) | 67.79-73.42 | +2.4% / +0.3% | +2.1% | 15.3M |
| META | 617.21 (09:00 iex) | +0.8% | 612.49 | 25.55 (4.2%) | 609.00-771.27 | -12.7% / -8.1% | -12.2% | 21.6M |
| TSLA | 404.80 (08:57 iex) | +0.1% | 404.22 | 14.06 (3.5%) | 349.33-410.85 | +7.3% / +10.0% | +4.6% | 37.7M |
| XLV | 183.82 (08:49 sip) | +2.3% | 179.72 | 3.04 (1.7%) | 165.19-182.25 | +3.4% / +4.8% | +0.4% | 8.5M |
| XLE | 69.11 (08:49 sip) | +1.0% | 68.45 | 1.40 (2.0%) | 61.04-69.86 | +3.0% / +6.1% | +0.4% | 32.2M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 769.20 (08:49 sip) | -0.4% | 772.31 | 7.09 (0.9%) | 758.68-781.62 | +0.2% / +0.7% | -0.1% | 38.2M |
| QQQ | 718.63 (09:03 iex) | -1.0% | 725.61 | 11.94 (1.6%) | 701.16-762.86 | -0.9% / +0.1% | +0.1% | 36.8M |
| IWM | 282.01 (08:49 sip) | +0.3% | 281.29 | 3.50 (1.2%) | 269.88-284.64 | +1.5% / -1.2% | +1.7% | 24.9M |
| DIA | 523.29 (08:49 sip) | -0.3% | 524.68 | 5.10 (1.0%) | 504.59-528.45 | +1.2% / +0.6% | -0.6% | 3.4M |
| TLT | 81.24 (08:49 sip) | +0.3% | 80.99 | 0.80 (1.0%) | 76.43-81.92 | +2.2% / +0.9% | +0.9% | 42.2M |
| GLD | 368.60 (08:49 sip) | -1.3% | 373.51 | 5.13 (1.4%) | 364.33-385.22 | -1.1% / -4.9% | -1.4% | 7.9M |
| USO | 165.81 (08:49 sip) | -0.5% | 166.57 | 4.66 (2.8%) | 141.76-169.96 | +7.0% / +12.1% | +4.2% | 4.8M |
| SMH | 556.49 (08:49 sip) | -2.0% | 567.67 | 18.58 (3.3%) | 520.53-639.47 | -1.8% / -1.0% | +2.0% | 8.8M |
| XLK | 188.32 (08:45 sip) | -1.4% | 191.00 | 4.14 (2.2%) | 181.50-203.25 | -0.7% / +0.8% | +1.3% | 8.9M |
| XLF | 56.89 (08:49 sip) | +1.4% | 56.13 | 0.69 (1.2%) | 52.81-56.67 | +2.0% / +0.5% | +0.2% | 32.7M |
| XLE | 69.11 (08:49 sip) | +1.0% | 68.45 | 1.40 (2.0%) | 61.04-69.86 | +3.0% / +6.1% | +0.4% | 32.2M |
| XLV | 183.82 (08:49 sip) | +2.3% | 179.72 | 3.04 (1.7%) | 165.19-182.25 | +3.4% / +4.8% | +0.4% | 8.5M |
| XLI | 167.64 (08:49 sip) | -0.5% | 168.49 | 2.49 (1.5%) | 162.97-172.34 | +0.2% / -1.5% | +0.1% | 7.5M |
| XLY | 116.19 (08:49 sip) | +0.7% | 115.33 | 1.65 (1.4%) | 107.99-116.22 | +2.2% / +1.9% | -0.2% | 7.1M |
| XLP | 88.14 (09:00 iex) | +1.5% | 86.84 | 1.33 (1.5%) | 80.10-89.99 | +2.0% / +3.1% | -0.3% | 14.0M |
| XLU | 42.91 (08:49 sip) | +1.0% | 42.49 | 0.60 (1.4%) | 39.10-42.97 | +2.2% / +2.0% | +1.2% | 31.7M |
| XLB | 51.93 (08:40 sip) | +0.1% | 51.86 | 0.65 (1.3%) | 47.81-51.90 | +3.1% / +1.9% | +1.1% | 11.2M |
| XLRE | 42.57 (08:15 sip) | +1.0% | 42.13 | 0.64 (1.5%) | 40.28-43.21 | +1.0% / -1.0% | +0.2% | 8.1M |
| XLC | 101.26 (08:49 sip) | -1.8% | 103.14 | 1.78 (1.7%) | 102.62-113.17 | -5.7% / -7.1% | -5.4% | 6.5M |
| KRE | 72.60 (08:40 sip) | +0.7% | 72.11 | 1.24 (1.7%) | 67.79-73.42 | +2.4% / +0.3% | +2.1% | 15.3M |
| XHB | 99.00 (07:05 sip) | +1.1% | 97.97 | 2.26 (2.3%) | 91.87-99.71 | +1.9% / -0.6% | +2.5% | 2.1M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 348.01 (08:59 iex) | +1.2% | 343.83 | 6.22 (1.8%) | 325.81-351.73 | +0.9% / +3.6% | -0.0% | 38.5M |
| MSFT | 541.00 (08:51 iex) | +1.9% | 531.01 | 10.65 (2.0%) | 512.17-551.15 | +0.2% / +3.9% | -0.4% | 20.2M |
| NVDA | 213.86 (08:49 sip) | -0.7% | 215.38 | 6.05 (2.8%) | 210.18-243.37 | -3.8% / -3.0% | -3.0% | 101.2M |
| AMZN | 247.91 (08:49 sip) | -2.6% | 254.60 | 6.67 (2.6%) | 246.12-265.34 | -0.2% / -0.2% | -3.0% | 35.6M |
| GOOGL | 288.12 (09:02 iex) | -11.3% | 324.89 | 8.05 (2.5%) | 316.60-359.40 | -4.4% / -4.9% | -2.9% | 25.7M |
| META | 617.21 (09:00 iex) | +0.8% | 612.49 | 25.55 (4.2%) | 609.00-771.27 | -12.7% / -8.1% | -12.2% | 21.6M |
| TSLA | 404.80 (08:57 iex) | +0.1% | 404.22 | 14.06 (3.5%) | 349.33-410.85 | +7.3% / +10.0% | +4.6% | 37.7M |
| AVGO | 342.00 (08:49 iex) | -2.8% | 351.81 | 11.20 (3.2%) | 320.23-380.84 | +1.4% / -0.5% | +4.1% | 22.0M |
| AMD | 562.99 (08:49 sip) | -2.7% | 578.44 | 28.68 (5.0%) | 502.60-658.52 | -0.2% / +6.0% | +4.7% | 19.6M |
| ORCL | 142.26 (08:49 sip) | -1.6% | 144.54 | 7.63 (5.3%) | 122.76-148.48 | +7.0% / +2.0% | +11.9% | 30.7M |
| NFLX | 62.59 (08:58 iex) | +1.0% | 61.99 | 2.15 (3.5%) | 61.51-73.07 | -9.0% / -15.5% | -4.7% | 43.9M |
| CRM | 229.72 (08:49 sip) | -5.1% | 242.11 | 8.73 (3.6%) | 220.29-252.42 | +1.7% / +1.8% | +0.1% | 7.2M |
| JPM | 344.02 (08:49 sip) | +1.4% | 339.30 | 6.24 (1.8%) | 324.25-344.40 | +1.7% / -1.0% | +1.2% | 7.0M |
| GS | 937.00 (08:49 sip) | +1.3% | 925.17 | 25.38 (2.7%) | 859.03-931.00 | +3.6% / -2.7% | +2.3% | 2.3M |
| BAC | 51.59 (08:49 sip) | +1.5% | 50.85 | 1.24 (2.4%) | 49.26-54.93 | -2.7% / -10.5% | +0.1% | 42.1M |
| XOM | 184.20 (08:49 sip) | +1.2% | 182.02 | 3.95 (2.2%) | 160.81-184.88 | +4.7% / +9.0% | +2.2% | 11.5M |
| CVX | 232.43 (08:49 sip) | +1.4% | 229.20 | 4.64 (2.0%) | 201.96-234.08 | +4.6% / +8.1% | +1.1% | 7.3M |
| LLY | 1,347.96 (08:49 sip) | +4.6% | 1,288.30 | 37.38 (2.9%) | 1,131.21-1,321.21 | +5.5% / +8.1% | +1.4% | 2.3M |
| UNH | 415.00 (08:49 sip) | +1.9% | 407.10 | 13.29 (3.3%) | 362.60-426.55 | +3.2% / +4.8% | -2.4% | 6.0M |
| JNJ | 277.00 (08:49 sip) | +2.2% | 271.04 | 7.36 (2.7%) | 245.17-272.75 | +4.6% / +2.1% | +5.1% | 7.9M |
| WMT | 121.59 (08:49 sip) | +2.4% | 118.77 | 2.44 (2.1%) | 103.39-122.40 | +4.1% / +8.3% | +0.8% | 20.0M |
| COST | 999.56 (08:49 sip) | +1.7% | 982.73 | 16.35 (1.7%) | 903.77-1,021.45 | +1.4% / +4.4% | -1.6% | 2.1M |
| HD | 322.68 (08:35 sip) | +1.6% | 317.56 | 7.06 (2.2%) | 277.15-327.92 | +5.1% / +3.0% | +1.1% | 4.9M |
| CAT | 632.69 (08:49 sip) | -11.3% | 713.38 | 25.93 (3.6%) | 679.50-874.87 | -6.4% / -9.6% | -3.4% | 2.7M |
| BA | 168.15 (08:49 sip) | +0.6% | 167.14 | 5.47 (3.3%) | 165.01-196.93 | -10.8% / -15.6% | -13.1% | 9.9M |
| DAL | 81.34 (08:49 sip) | +1.2% | 80.35 | 3.16 (3.9%) | 74.14-85.93 | +0.7% / +0.0% | +3.5% | 7.3M |
| UAL | 104.80 (08:40 sip) | +1.3% | 103.43 | 4.88 (4.7%) | 94.54-115.20 | -0.5% / -4.2% | +1.7% | 5.2M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-28 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AIOK | 25.35 (08:49 sip) | -9.9% | 28.14 | 3.87 (13.8%) | 3.90-29.90 | - / - | +481.4% | 7.3M |
| AXGN | 49.64 (08:25 sip) | +0.8% | 49.25 | 2.20 (4.5%) | 34.11-49.97 | +32.2% / +15.1% | +35.0% | 2.0M |
| GMAB | 56.55 (08:49 sip) | -1.3% | 57.29 | 2.44 (4.3%) | 33.73-59.97 | +45.3% / +58.3% | +44.8% | 6.4M |
| SKUU | 20.40 (08:49 sip) | -4.1% | 21.28 | 2.11 (9.9%) | 13.64-31.80 | +1.7% / -12.2% | +28.9% | 2.5M |
| SKHX | 12.06 (08:49 sip) | -3.8% | 12.54 | 1.25 (9.9%) | 8.07-18.93 | +1.0% / -13.1% | +28.4% | 2.9M |
| SKHL | 7.78 (08:45 sip) | -4.4% | 8.14 | 0.80 (9.9%) | 5.24-12.21 | +1.3% / -12.6% | +28.4% | 2.4M |
| BCAX | 9.65 (08:49 sip) | -1.2% | 9.76 | 1.48 (15.1%) | 8.90-19.23 | -42.6% / -52.1% | -45.5% | 1.6M |
| SKDD | 7.82 (08:49 sip) | +3.9% | 7.53 | 1.27 (16.8%) | 6.22-12.85 | -19.9% / -14.8% | -31.2% | 4.1M |
| RAPP | 22.58 (08:49 sip) | +0.4% | 22.50 | 2.72 (12.1%) | 22.06-34.48 | -21.8% / -40.3% | -10.2% | 1.2M |
