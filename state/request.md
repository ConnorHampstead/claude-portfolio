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

- Time now: **09:05 ET** (13:05 UTC), Monday 2026-10-19. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$101,582.72**
- Cash: $95,786.20
- Session P&L so far: -0.19% (new entries are blocked at -3.0%)
- Gross exposure: $14,423 (14% of equity, cap 150%)
- Net exposure: $+5,797 (+6%, cap +/-100%)
- Risk at stake (entry to stop): $508 (0.50% of equity, cap 4.0%) — 3.50% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| HD | long | 33 | 310.70 | 306.35 | -144 (-1.4%) | 303.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 130.70 | -33 (-0.8%) | 137.40 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 18.

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
| HD | 307.09 (08:49 sip) | -0.8% | 309.63 | 6.58 (2.1%) | 277.15-314.66 | +5.9% / -0.8% | +6.5% | 5.7M |
| ORCL | 130.65 (08:49 sip) | +1.9% | 128.23 | 6.96 (5.4%) | 127.36-153.03 | -7.8% / -11.3% | -9.3% | 30.6M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 766.92 (08:49 sip) | +0.5% | 763.25 | 6.89 (0.9%) | 758.79-781.62 | -1.0% / -0.5% | -2.0% | 42.1M |
| QQQ | 718.91 (09:03 iex) | +1.3% | 709.80 | 10.08 (1.4%) | 707.23-762.86 | -4.4% / -2.3% | -5.5% | 36.2M |
| IWM | 271.70 (08:49 sip) | +0.5% | 270.44 | 3.96 (1.5%) | 269.88-288.94 | -3.2% / -6.3% | -3.0% | 26.1M |
| DIA | 517.89 (08:49 sip) | -0.2% | 519.10 | 5.22 (1.0%) | 504.59-525.09 | +0.9% / -0.8% | +0.6% | 3.4M |
| TLT | 79.93 (08:49 sip) | -0.1% | 80.05 | 0.84 (1.0%) | 76.43-81.61 | +1.8% / -0.4% | +2.7% | 50.2M |
| GLD | 381.56 (08:49 sip) | -0.1% | 382.01 | 5.14 (1.3%) | 373.36-400.78 | -0.6% / -3.8% | -0.7% | 7.8M |
| USO | 160.26 (08:49 sip) | -0.9% | 161.76 | 4.75 (2.9%) | 141.76-162.38 | +8.4% / +13.4% | +9.1% | 5.5M |
| SMH | 556.50 (08:49 sip) | +3.1% | 539.79 | 15.64 (2.9%) | 539.07-639.47 | -10.2% / -6.8% | -10.5% | 7.7M |
| XLK | 186.59 (08:49 sip) | +1.7% | 183.47 | 3.46 (1.9%) | 182.82-203.25 | -6.3% / -3.3% | -7.7% | 8.2M |
| XLF | 55.25 (08:49 sip) | -0.5% | 55.52 | 0.70 (1.3%) | 52.81-56.20 | +2.0% / -1.1% | +1.4% | 39.4M |
| XLE | 67.60 (08:49 sip) | -0.9% | 68.24 | 1.33 (2.0%) | 60.95-68.29 | +6.8% / +7.8% | +4.9% | 32.7M |
| XLV | 175.59 (08:49 sip) | -0.6% | 176.71 | 2.93 (1.7%) | 165.19-178.86 | +3.9% / +4.2% | +3.5% | 8.5M |
| XLI | 168.92 (08:49 sip) | +0.7% | 167.76 | 2.57 (1.5%) | 164.66-172.34 | -0.8% / -3.5% | -0.9% | 7.5M |
| XLY | 113.00 (08:30 sip) | +0.5% | 112.46 | 1.39 (1.2%) | 107.99-114.69 | +1.2% / -1.1% | -0.3% | 7.0M |
| XLP | 86.95 (08:49 sip) | -0.8% | 87.62 | 1.17 (1.3%) | 80.10-88.47 | +5.8% / +4.6% | +5.0% | 12.2M |
| XLU | 42.13 (08:49 sip) | -0.2% | 42.21 | 0.67 (1.6%) | 39.03-42.29 | +4.0% / +0.9% | +1.9% | 35.7M |
| XLB | 50.99 (07:50 sip) | +0.1% | 50.92 | 0.75 (1.5%) | 47.81-51.51 | +2.7% / -0.2% | +3.0% | 11.8M |
| XLRE | 42.14 (08:15 sip) | -0.0% | 42.16 | 0.60 (1.4%) | 40.28-42.67 | +1.7% / -1.7% | +1.3% | 7.4M |
| XLC | no trade today | - | 110.32 | 1.65 (1.5%) | 109.66-115.61 | -1.3% / -1.2% | -0.1% | 6.7M |
| KRE | 69.71 (08:49 sip) | -0.1% | 69.81 | 1.32 (1.9%) | 67.79-72.87 | -0.4% / -4.0% | +1.2% | 16.0M |
| XHB | 95.14 (08:20 sip) | +0.2% | 94.91 | 2.23 (2.4%) | 91.87-99.67 | -1.3% / -5.4% | +0.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 341.88 (08:49 sip) | -0.5% | 343.46 | 6.69 (1.9%) | 325.81-348.15 | +1.8% / +5.5% | +2.0% | 37.1M |
| MSFT | 528.60 (08:49 sip) | -0.1% | 529.05 | 11.74 (2.2%) | 491.22-551.15 | +1.7% / +4.7% | -1.1% | 22.4M |
| NVDA | 218.18 (08:49 sip) | +1.9% | 214.13 | 5.76 (2.7%) | 212.85-243.37 | -6.2% / -4.0% | -6.6% | 106.2M |
| AMZN | 255.05 (08:53 iex) | +2.0% | 250.00 | 5.90 (2.4%) | 244.72-263.70 | -1.3% / -2.8% | -4.7% | 35.9M |
| GOOGL | 342.95 (08:54 iex) | +0.7% | 340.59 | 8.96 (2.6%) | 335.51-364.17 | -1.7% / -1.1% | -3.1% | 25.3M |
| META | 710.50 (08:49 sip) | +0.2% | 709.33 | 22.11 (3.1%) | 679.60-779.82 | -3.6% / +8.3% | -1.3% | 21.8M |
| TSLA | 355.54 (08:49 sip) | +0.2% | 354.72 | 10.86 (3.1%) | 345.88-388.56 | -4.2% / -1.3% | -7.3% | 34.7M |
| AVGO | 339.42 (08:49 sip) | +3.2% | 328.75 | 11.80 (3.6%) | 328.58-380.84 | -7.5% / -10.0% | -9.1% | 22.4M |
| AMD | 547.50 (08:49 sip) | +3.5% | 528.75 | 26.28 (5.0%) | 526.83-658.52 | -13.4% / -1.6% | -13.0% | 21.3M |
| ORCL | 130.65 (08:49 sip) | +1.9% | 128.23 | 6.96 (5.4%) | 127.36-153.03 | -7.8% / -11.3% | -9.3% | 30.6M |
| NFLX | 70.04 (08:49 sip) | -0.7% | 70.53 | 1.65 (2.3%) | 66.54-73.87 | +0.3% / -6.1% | +0.3% | 35.2M |
| CRM | 237.89 (08:49 sip) | -1.2% | 240.70 | 8.57 (3.6%) | 220.29-251.94 | +3.2% / +4.7% | +5.0% | 9.0M |
| JPM | 337.70 (08:49 sip) | -0.6% | 339.72 | 6.12 (1.8%) | 324.25-352.74 | +1.5% / -2.0% | +2.0% | 8.2M |
| GS | 880.00 (08:49 sip) | -0.1% | 881.26 | 22.32 (2.5%) | 859.03-967.76 | -2.8% / -9.4% | -1.6% | 2.3M |
| BAC | 50.90 (08:49 sip) | -0.6% | 51.23 | 1.25 (2.4%) | 49.26-58.28 | -5.8% / -13.1% | -5.7% | 42.6M |
| XOM | 176.84 (08:49 sip) | -1.2% | 178.98 | 3.52 (2.0%) | 155.85-179.16 | +7.7% / +9.4% | +5.9% | 11.8M |
| CVX | 222.61 (08:49 sip) | -1.1% | 224.99 | 4.50 (2.0%) | 200.78-225.31 | +7.3% / +8.8% | +6.1% | 7.5M |
| LLY | 1,247.96 (08:45 sip) | -0.7% | 1,257.03 | 37.21 (3.0%) | 1,131.21-1,275.88 | +6.6% / +6.5% | +6.6% | 2.3M |
| UNH | 398.68 (08:49 sip) | -0.7% | 401.43 | 12.67 (3.2%) | 362.60-414.12 | +6.0% / +4.0% | +5.8% | 5.9M |
| JNJ | 252.90 (08:45 sip) | -1.0% | 255.56 | 6.44 (2.5%) | 245.17-275.23 | -2.2% / -3.5% | -2.2% | 7.4M |
| WMT | 117.63 (08:49 sip) | -1.0% | 118.81 | 2.53 (2.1%) | 103.39-121.38 | +8.4% / +9.1% | +6.7% | 21.7M |
| COST | 981.98 (08:49 sip) | -0.7% | 989.11 | 16.04 (1.6%) | 883.10-1,008.37 | +5.9% / +5.9% | +4.5% | 2.3M |
| HD | 307.09 (08:49 sip) | -0.8% | 309.63 | 6.58 (2.1%) | 277.15-314.66 | +5.9% / -0.8% | +6.5% | 5.7M |
| CAT | 742.22 (08:49 sip) | +1.6% | 730.76 | 29.88 (4.1%) | 704.01-876.95 | -9.2% / -10.1% | -8.7% | 2.5M |
| BA | 190.08 (08:49 sip) | -0.1% | 190.21 | 4.85 (2.6%) | 183.38-204.06 | -0.6% / -7.4% | -0.1% | 8.5M |
| DAL | 76.20 (08:25 sip) | +1.1% | 75.37 | 2.53 (3.4%) | 75.06-85.93 | -7.9% / -8.2% | -8.0% | 7.5M |
| UAL | 97.49 (08:35 sip) | +1.4% | 96.10 | 3.82 (4.0%) | 96.07-118.26 | -11.7% / -14.1% | -10.6% | 4.5M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-16 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IAM | 23.40 (08:30 sip) | -1.7% | 23.81 | 6.09 (25.6%) | 16.15-25.00 | - / - | - | 2.5M |
| NBIZ | 31.38 (08:49 sip) | -15.3% | 37.05 | 3.66 (9.9%) | 17.01-37.98 | +61.0% / +36.9% | +65.6% | 2.2M |
| CORD | 4.41 (08:49 sip) | -12.7% | 5.05 | 0.51 (10.1%) | 2.52-5.51 | +56.4% / +57.8% | +58.3% | 15.9M |
| IREZ | 17.77 (08:49 sip) | -11.7% | 20.13 | 1.78 (8.8%) | 6.82-20.56 | +82.5% / +86.0% | +58.0% | 2.6M |
| SMCZ | 6.49 (08:30 sip) | -8.5% | 7.09 | 0.58 (8.2%) | 3.66-7.15 | +51.7% / +20.8% | +65.7% | 2.6M |
| AAOZ | 17.66 (08:49 sip) | -9.9% | 19.61 | 2.28 (11.6%) | 7.63-19.72 | +54.6% / +55.8% | +92.4% | 1.8M |
| NBIL | 14.07 (08:49 sip) | +15.2% | 12.21 | 3.47 (28.4%) | 11.85-30.43 | -48.6% / -50.2% | -46.2% | 4.8M |
| NBIG | 9.63 (08:49 sip) | +14.5% | 8.41 | 2.39 (28.4%) | 8.15-20.96 | -48.7% / -50.3% | -46.1% | 3.2M |
| NEBX | 14.31 (08:49 sip) | +14.0% | 12.55 | 3.53 (28.1%) | 12.12-31.11 | -48.5% / -50.1% | -46.0% | 2.4M |
| CRWG | 9.39 (08:49 sip) | +12.3% | 8.36 | 2.23 (26.7%) | 7.90-20.68 | -49.5% / -56.0% | -47.5% | 4.0M |
| CWVX | 7.85 (08:49 sip) | +12.1% | 7.00 | 1.85 (26.5%) | 6.60-17.26 | -49.3% / -55.8% | -47.4% | 2.1M |
