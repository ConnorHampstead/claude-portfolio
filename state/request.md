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

- Time now: **09:05 ET** (13:05 UTC, 14:05 Stockholm), Tuesday 2026-10-27. The cash session opens at 09:30 ET (14:30 Stockholm), in 25 min, and closes at 16:00 ET (21:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,135.70**
- Cash: $55,272.31
- Session P&L so far: -0.27% (new entries are blocked at -3.0%)
- Gross exposure: $66,624 (65% of equity, cap 150%)
- Net exposure: $+46,863 (+46%, cap +/-100%)
- Risk at stake (entry to stop): $1,204 (1.18% of equity, cap 4.0%) — 2.82% left for new plays
- Slots: 5 open + 0 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 72.92 | -20 (-0.2%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| NVDA | short | 26 | 212.38 | 217.85 | -142 (-2.6%) | 222.00 | 198.00 | A break of the 212.85 20d low confirms Monday's bounce failed in the bellwether and opens a move toward 198. |
| ORCL | short | 33 | 129.70 | 127.76 | +64 (+1.5%) | 130.00 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |
| XLV | long | 160 | 179.57 | 178.69 | -141 (-0.5%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |
| XOM | long | 97 | 180.75 | 183.49 | +266 (+1.5%) | 178.90 | 189.00 | Energy remains the leading sector; a break of the 180.26 20-day high with oil at a 5-month high extends the trend. |

### Record

26 closed trades: 10W / 16L, total +1.38R, net $+2,118 realized. Shorts taken: 26.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| UAL | short | stop | -0.45R | $-315 | 40% |
| XLI | short | stop | -1.00R | $-526 | 36% |
| GOOGL | short | target | +1.42R | $+362 | 35% |
| CVX | long | stop | -0.23R | $-117 | 40% |
| AMD | short | target | +1.17R | $+575 | 42% |

### Ideas you passed on, replayed against the tape

63 resolved: 18 reached target first, 31 stop first, 11 never reached the entry, 3 expired, 0 ambiguous. Average -0.10R across the 52 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-21 pre-market | UNH | long | Healthcare soft pre-market on ISRG/TMO; prefer to spend the risk on energy. | stop | -1.00R | 35% |
| 2026-10-19 pre-market | AMD | short | Same idea as the SMH short with twice the noise; one semi short is enough. | never filled | - | 38% |
| 2026-10-19 pre-market | BAC | short | Post-earnings damage already priced; my last bank short stopped out. | never filled | - | 30% |
| 2026-10-14 pre-market | CVX | long | Best long (20d-high breakout) but duplicates the XOM energy exposure. | target | +1.70R | 40% |
| 2026-10-19 pre-market | AMZN | long | Buying an upgrade gap in a heavy data-center spender while the capex-credit stor | stop | -1.06R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| KRE | 72.80 (08:00 sip) | +0.1% | 72.73 | 1.28 (1.8%) | 67.79-73.42 | +3.7% / +0.9% | +5.0% | 16.1M |
| NVDA | 218.43 (08:49 sip) | +1.1% | 216.00 | 6.14 (2.8%) | 210.18-243.37 | -4.0% / -2.8% | -0.5% | 103.6M |
| ORCL | 128.34 (08:49 sip) | +1.8% | 126.06 | 6.62 (5.2%) | 122.76-146.40 | -6.6% / -11.2% | -2.7% | 28.7M |
| XLV | 179.01 (08:45 sip) | -0.2% | 179.28 | 3.10 (1.7%) | 165.19-182.25 | +3.7% / +4.8% | +2.1% | 8.7M |
| XOM | 183.39 (08:49 sip) | -0.6% | 184.54 | 3.93 (2.1%) | 159.27-184.59 | +7.3% / +11.0% | +3.5% | 11.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 768.22 (08:49 sip) | +0.4% | 765.37 | 7.25 (0.9%) | 758.68-781.62 | -0.6% / -0.2% | -0.1% | 40.2M |
| QQQ | 715.27 (09:04 iex) | +0.4% | 712.20 | 12.36 (1.7%) | 701.16-762.86 | -3.0% / -1.8% | -0.9% | 36.5M |
| IWM | 278.27 (08:49 sip) | +0.5% | 276.99 | 3.63 (1.3%) | 269.88-284.64 | -0.0% / -3.0% | +2.1% | 25.2M |
| DIA | 524.30 (08:49 sip) | +0.3% | 522.97 | 5.36 (1.0%) | 504.59-528.45 | +1.2% / +0.2% | +0.8% | 3.4M |
| TLT | 81.74 (08:49 sip) | +0.1% | 81.68 | 0.83 (1.0%) | 76.43-81.92 | +3.5% / +1.8% | +2.8% | 46.9M |
| GLD | 369.10 (09:00 iex) | +0.3% | 367.82 | 5.31 (1.4%) | 364.33-385.22 | -2.8% / -6.6% | -3.1% | 7.9M |
| USO | 165.29 (08:49 sip) | -0.6% | 166.23 | 4.78 (2.9%) | 141.76-169.96 | +8.2% / +12.9% | +3.4% | 4.9M |
| SMH | 550.10 (08:49 sip) | +1.6% | 541.62 | 19.10 (3.5%) | 520.53-639.47 | -7.0% / -5.7% | -1.2% | 8.6M |
| XLK | 187.75 (08:49 sip) | +0.8% | 186.32 | 4.24 (2.3%) | 181.50-203.25 | -3.4% / -1.7% | +0.2% | 8.8M |
| XLF | 56.29 (08:49 sip) | +0.5% | 56.02 | 0.72 (1.3%) | 52.81-56.67 | +2.3% / +0.1% | +1.7% | 35.5M |
| XLE | 69.29 (08:49 sip) | -0.5% | 69.64 | 1.48 (2.1%) | 60.95-69.86 | +5.9% / +8.3% | +2.7% | 31.9M |
| XLV | 179.01 (08:45 sip) | -0.2% | 179.28 | 3.10 (1.7%) | 165.19-182.25 | +3.7% / +4.8% | +2.1% | 8.7M |
| XLI | 167.90 (08:40 sip) | +0.6% | 166.96 | 2.71 (1.6%) | 162.97-172.34 | -0.7% / -2.7% | +0.2% | 7.5M |
| XLY | 114.90 (08:30 sip) | +0.6% | 114.26 | 1.63 (1.4%) | 107.99-116.22 | +1.8% / +0.9% | -0.2% | 7.2M |
| XLP | 87.72 (08:45 sip) | -0.3% | 87.96 | 1.38 (1.6%) | 80.10-89.99 | +4.0% / +4.5% | +0.9% | 14.0M |
| XLU | 42.71 (08:49 sip) | +0.4% | 42.55 | 0.63 (1.5%) | 39.03-42.88 | +3.1% / +2.1% | +2.9% | 35.2M |
| XLB | 51.41 (08:49 sip) | +0.1% | 51.38 | 0.66 (1.3%) | 47.81-51.71 | +2.7% / +1.0% | +0.8% | 11.3M |
| XLRE | no trade today | - | 42.80 | 0.64 (1.5%) | 40.28-43.21 | +2.9% / +0.4% | +2.7% | 8.0M |
| XLC | 103.87 (07:40 sip) | +0.0% | 103.85 | 1.76 (1.7%) | 103.55-113.17 | -5.7% / -6.6% | -5.7% | 6.8M |
| KRE | 72.80 (08:00 sip) | +0.1% | 72.73 | 1.28 (1.8%) | 67.79-73.42 | +3.7% / +0.9% | +5.0% | 16.1M |
| XHB | no trade today | - | 97.95 | 2.33 (2.4%) | 91.87-99.32 | +2.1% / -1.0% | +4.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 342.70 (08:49 sip) | -0.4% | 343.91 | 6.39 (1.9%) | 325.81-351.73 | +1.4% / +4.1% | +0.3% | 39.2M |
| MSFT | 529.26 (08:49 sip) | -0.6% | 532.60 | 11.12 (2.1%) | 502.40-551.15 | +0.9% / +4.6% | -0.2% | 20.3M |
| NVDA | 218.43 (08:49 sip) | +1.1% | 216.00 | 6.14 (2.8%) | 210.18-243.37 | -4.0% / -2.8% | -0.5% | 103.6M |
| AMZN | 250.70 (08:49 sip) | +0.6% | 249.09 | 6.94 (2.8%) | 245.14-265.34 | -2.2% / -2.5% | -5.1% | 35.9M |
| GOOGL | 318.50 (08:49 sip) | +0.5% | 316.80 | 8.42 (2.7%) | 316.60-359.40 | -7.3% / -7.4% | -8.0% | 24.1M |
| META | 628.04 (09:03 iex) | -0.4% | 630.56 | 25.92 (4.1%) | 627.80-771.27 | -11.6% / -5.1% | -10.6% | 19.5M |
| TSLA | 396.29 (08:54 iex) | +1.2% | 391.62 | 13.15 (3.4%) | 345.88-397.27 | +5.4% / +7.4% | +6.4% | 37.2M |
| AVGO | 340.11 (08:49 sip) | +3.3% | 329.17 | 11.23 (3.4%) | 320.23-380.84 | -5.3% / -7.3% | -1.6% | 21.6M |
| AMD | 541.00 (08:49 sip) | +1.8% | 531.28 | 28.48 (5.4%) | 502.60-658.52 | -8.9% / -2.1% | -1.3% | 19.3M |
| ORCL | 128.34 (08:49 sip) | +1.8% | 126.06 | 6.62 (5.2%) | 122.76-146.40 | -6.6% / -11.2% | -2.7% | 28.7M |
| NFLX | 63.57 (08:49 sip) | -0.5% | 63.90 | 2.20 (3.5%) | 62.86-73.07 | -7.2% / -13.6% | -8.5% | 43.0M |
| CRM | 245.16 (08:49 sip) | -1.0% | 247.61 | 8.56 (3.5%) | 220.29-252.42 | +4.7% / +5.0% | +2.1% | 7.8M |
| JPM | 336.54 (08:40 sip) | +0.7% | 334.04 | 6.50 (1.9%) | 324.25-344.40 | +0.3% / -2.8% | +0.2% | 7.3M |
| GS | 908.65 (08:49 sip) | +1.7% | 893.28 | 25.33 (2.8%) | 859.03-931.00 | +0.2% / -6.5% | +2.0% | 2.3M |
| BAC | 50.95 (08:49 sip) | +0.9% | 50.52 | 1.34 (2.6%) | 49.26-55.55 | -4.1% / -11.9% | +0.3% | 42.8M |
| XOM | 183.39 (08:49 sip) | -0.6% | 184.54 | 3.93 (2.1%) | 159.27-184.59 | +7.3% / +11.0% | +3.5% | 11.3M |
| CVX | 231.20 (08:49 sip) | -0.3% | 232.01 | 4.97 (2.1%) | 201.96-234.08 | +7.1% / +10.0% | +3.4% | 7.3M |
| LLY | 1,277.00 (08:30 sip) | -0.2% | 1,279.14 | 40.36 (3.2%) | 1,131.21-1,321.21 | +5.7% / +7.6% | +3.1% | 2.3M |
| UNH | 410.00 (08:49 sip) | -0.2% | 410.70 | 13.50 (3.3%) | 362.60-426.55 | +5.1% / +5.9% | +0.9% | 6.1M |
| JNJ | 265.50 (08:45 sip) | -0.3% | 266.30 | 7.33 (2.8%) | 245.17-272.36 | +2.9% / +0.4% | +4.9% | 7.9M |
| WMT | 119.96 (08:49 sip) | -0.3% | 120.29 | 2.57 (2.1%) | 103.39-122.40 | +6.7% / +9.8% | +1.3% | 21.2M |
| COST | 999.60 (08:49 sip) | -0.6% | 1,005.16 | 16.26 (1.6%) | 903.77-1,021.45 | +4.5% / +7.0% | +1.0% | 2.1M |
| HD | 321.23 (08:49 sip) | +0.6% | 319.38 | 7.57 (2.4%) | 277.15-327.92 | +6.8% / +3.4% | +3.1% | 5.2M |
| CAT | 703.28 (08:45 sip) | +1.6% | 692.13 | 28.86 (4.2%) | 679.50-874.87 | -10.5% / -12.9% | -4.4% | 2.7M |
| BA | 184.41 (09:02 iex) | -2.1% | 188.31 | 4.15 (2.2%) | 182.40-196.93 | -0.5% / -6.0% | -1.6% | 7.6M |
| DAL | 80.50 (08:40 sip) | +1.7% | 79.16 | 3.05 (3.9%) | 74.14-85.93 | -1.2% / -1.7% | +6.1% | 7.4M |
| UAL | 102.56 (08:49 sip) | +1.9% | 100.69 | 4.85 (4.8%) | 94.54-115.20 | -3.9% / -7.3% | +5.3% | 5.1M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-26 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SGRY | 23.22 (08:30 sip) | -0.1% | 23.25 | 1.07 (4.6%) | 13.11-23.29 | +56.9% / +61.5% | +58.1% | 4.6M |
| VEEA | 5.99 (08:49 sip) | -1.6% | 6.08 | 1.00 (16.4%) | 2.08-7.09 | +38.7% / +77.6% | +49.8% | 12.8M |
| XP | 16.20 (08:49 sip) | +3.1% | 15.71 | 2.50 (15.9%) | 13.78-32.73 | -43.4% / -30.1% | -48.1% | 19.5M |
| ORIC | 9.19 (08:49 sip) | +2.6% | 8.96 | 1.07 (12.0%) | 8.88-14.31 | -27.8% / -30.3% | -29.6% | 1.7M |
| EWZS | 11.86 (09:02 iex) | +3.6% | 11.45 | 0.97 (8.5%) | 10.30-17.15 | -25.9% / -17.9% | -28.9% | 3.6M |
| STNE | 8.53 (08:45 sip) | +2.4% | 8.33 | 0.81 (9.8%) | 7.06-12.49 | -24.5% / -18.5% | -27.5% | 8.3M |
| AVBP | 15.30 (08:15 sip) | -0.4% | 15.36 | 1.64 (10.7%) | 11.36-30.90 | -24.1% / -40.6% | -14.4% | 2.6M |
| PAGS | 8.73 (08:49 sip) | +2.0% | 8.56 | 0.68 (7.9%) | 7.50-11.76 | -18.6% / -11.2% | -23.1% | 5.6M |
