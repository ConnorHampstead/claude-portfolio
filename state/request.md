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

- Time now: **09:05 ET** (13:05 UTC), Thursday 2026-09-24. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$101,449.65**
- Cash: $116,455.05
- Session P&L so far: -0.05% (new entries are blocked at -3.0%)
- Gross exposure: $38,187 (38% of equity, cap 150%)
- Net exposure: $+8,177 (+8%, cap +/-100%)
- Risk at stake (entry to stop): $1,010 (1.00% of equity, cap 4.0%) — 3.00% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| BAC | short | 267 | 55.80 | 56.20 | -107 (-0.7%) | 57.7 (no live order) | 52.90 | Weakest large bank (-7.5% vs 20d avg). A break below today's opening low confirms the 20d-low support failed and opens a |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| AAPL | long | 67 | 346.00 | stop | 338.50 | 358.00 | 2026-09-23 |

### Record

4 closed trades: 2W / 2L, total +0.57R, net $+1,558 realized. Shorts taken: 1.

### Last 4 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| DAL | long | stop | +1.00R | $+999 | 46% |
| LLY | long | stop | +1.76R | $+1,654 | 52% |
| ROST | long | stop | -1.18R | $-336 | 47% |
| ANET | long | stop | -1.01R | $-758 | 45% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| BAC | 56.12 (08:49 sip) | +0.2% | 56.00 | 1.38 (2.5%) | 55.73-63.83 | -7.4% / -9.0% | -3.3% | 37.6M |
| AAPL | 336.93 (08:49 sip) | -0.0% | 337.02 | 7.24 (2.1%) | 308.80-345.34 | +3.1% / +4.9% | +1.4% | 43.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 764.39 (09:03 iex) | -0.4% | 767.81 | 6.90 (0.9%) | 747.74-775.14 | +0.5% / +1.1% | +2.1% | 42.9M |
| QQQ | 734.98 (09:03 iex) | -0.8% | 741.21 | 9.60 (1.3%) | 699.27-748.35 | +3.3% / +4.3% | +5.3% | 32.8M |
| IWM | 280.87 (08:49 sip) | -0.4% | 281.92 | 3.50 (1.2%) | 281.03-299.61 | -2.7% / -4.1% | -0.7% | 21.6M |
| DIA | 513.10 (08:49 sip) | -0.2% | 514.30 | 5.39 (1.0%) | 511.11-536.49 | -2.0% / -2.3% | +0.1% | 3.3M |
| TLT | 80.18 (08:49 sip) | -0.3% | 80.46 | 0.74 (0.9%) | 80.22-83.28 | -1.5% / -2.0% | -0.5% | 32.7M |
| GLD | 392.72 (09:01 iex) | -0.0% | 392.88 | 7.34 (1.9%) | 388.39-424.95 | -2.3% / -0.4% | +0.3% | 10.4M |
| USO | 150.66 (09:03 iex) | +1.2% | 148.83 | 5.41 (3.6%) | 125.41-163.35 | +1.9% / +10.7% | -4.7% | 5.5M |
| SMH | 590.21 (08:49 sip) | -1.9% | 601.41 | 16.17 (2.7%) | 537.73-608.66 | +6.5% / +6.5% | +10.2% | 6.5M |
| XLK | 192.88 (08:49 sip) | -1.3% | 195.34 | 3.21 (1.6%) | 180.50-196.68 | +4.3% / +6.4% | +6.3% | 6.8M |
| XLF | 54.57 (08:49 sip) | +0.1% | 54.54 | 0.78 (1.4%) | 54.46-58.39 | -3.9% / -4.2% | -2.1% | 33.7M |
| XLE | 63.08 (08:49 sip) | +1.1% | 62.37 | 1.34 (2.1%) | 60.95-65.78 | -2.0% / +1.9% | -2.0% | 32.1M |
| XLV | 169.25 (08:49 sip) | +0.3% | 168.80 | 2.26 (1.3%) | 164.48-174.17 | -0.1% / +1.3% | +1.0% | 7.5M |
| XLI | 168.99 (08:45 sip) | -0.7% | 170.10 | 2.27 (1.3%) | 167.04-180.42 | -1.2% / -4.4% | +1.1% | 7.6M |
| XLY | 110.59 (04:05 sip) | -0.1% | 110.65 | 1.68 (1.5%) | 109.38-117.58 | -2.4% / -3.7% | +0.6% | 6.0M |
| XLP | 83.00 (08:45 sip) | +0.7% | 82.43 | 0.84 (1.0%) | 81.73-86.12 | -1.4% / -2.2% | -0.4% | 9.8M |
| XLU | 39.89 (08:49 sip) | +0.4% | 39.75 | 0.58 (1.5%) | 39.71-43.39 | -5.0% / -8.0% | -3.1% | 21.9M |
| XLB | 50.30 (08:30 sip) | +0.0% | 50.28 | 0.73 (1.5%) | 49.65-53.84 | -2.1% / -2.4% | +0.3% | 11.0M |
| XLRE | 41.88 (08:10 sip) | +0.1% | 41.84 | 0.53 (1.3%) | 41.81-45.08 | -3.1% / -5.2% | -1.4% | 5.3M |
| XLC | 112.15 (07:05 sip) | -0.4% | 112.56 | 1.91 (1.7%) | 109.95-115.61 | +0.3% / +1.4% | -0.1% | 4.9M |
| KRE | 70.38 (08:40 sip) | +0.0% | 70.38 | 1.24 (1.8%) | 70.36-75.07 | -3.7% / -5.8% | -2.7% | 13.1M |
| XHB | 96.53 (07:50 sip) | -0.6% | 97.09 | 2.20 (2.3%) | 95.26-106.55 | -2.5% / -6.7% | +0.9% | 1.8M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 336.93 (08:49 sip) | -0.0% | 337.02 | 7.24 (2.1%) | 308.80-345.34 | +3.1% / +4.9% | +1.4% | 43.7M |
| MSFT | 498.61 (09:01 iex) | -0.4% | 500.59 | 10.87 (2.2%) | 486.00-517.78 | +0.2% / +6.3% | +2.1% | 21.6M |
| NVDA | 223.05 (08:49 sip) | -1.1% | 225.51 | 5.49 (2.4%) | 208.93-234.50 | +2.0% / +4.8% | +5.4% | 132.7M |
| AMZN | 246.38 (08:49 sip) | -1.2% | 249.27 | 5.45 (2.2%) | 244.30-267.56 | -2.3% / -2.7% | +1.3% | 34.9M |
| GOOGL | 336.96 (08:49 iex) | -0.3% | 337.83 | 9.11 (2.7%) | 327.74-364.17 | -1.2% / -2.1% | -1.5% | 27.0M |
| META | 731.12 (08:49 sip) | -1.7% | 744.10 | 27.53 (3.7%) | 555.66-763.90 | +16.0% / +21.7% | +10.6% | 22.3M |
| TSLA | 376.56 (08:49 sip) | -0.9% | 380.12 | 13.01 (3.4%) | 342.53-386.70 | +4.7% / +8.9% | +6.2% | 39.3M |
| AVGO | 349.92 (08:59 iex) | -1.4% | 354.99 | 11.44 (3.2%) | 335.20-375.91 | -1.0% / -5.9% | +4.8% | 27.6M |
| AMD | 599.00 (08:49 sip) | -2.5% | 614.61 | 25.99 (4.2%) | 440.50-624.69 | +19.8% / +22.9% | +19.9% | 21.0M |
| ORCL | 138.18 (09:00 iex) | -4.4% | 144.56 | 7.82 (5.4%) | 139.00-170.70 | -3.5% / +1.9% | +1.0% | 31.8M |
| NFLX | 71.45 (08:49 sip) | +0.1% | 71.36 | 2.36 (3.3%) | 70.11-83.60 | -8.1% / -5.7% | -6.6% | 32.4M |
| CRM | 237.00 (08:49 sip) | -0.2% | 237.58 | 9.01 (3.8%) | 198.60-267.80 | -3.8% / +12.8% | -5.0% | 17.1M |
| JPM | 337.90 (08:45 sip) | +0.1% | 337.53 | 7.54 (2.2%) | 336.98-362.86 | -4.3% / -4.5% | -3.3% | 7.3M |
| GS | 932.20 (08:45 sip) | -0.4% | 936.36 | 28.16 (3.0%) | 922.00-1,057.38 | -6.2% / -8.6% | -0.2% | 2.0M |
| BAC | 56.12 (08:49 sip) | +0.2% | 56.00 | 1.38 (2.5%) | 55.73-63.83 | -7.4% / -9.0% | -3.3% | 37.6M |
| XOM | 163.12 (08:49 sip) | +1.2% | 161.23 | 4.05 (2.5%) | 155.32-169.64 | -0.5% / +1.8% | -1.3% | 14.8M |
| CVX | 207.80 (08:49 sip) | +1.1% | 205.51 | 4.77 (2.3%) | 197.82-217.78 | -1.6% / +3.1% | -2.9% | 10.0M |
| LLY | 1,156.29 (08:45 sip) | +0.5% | 1,150.99 | 27.76 (2.4%) | 1,113.29-1,235.78 | +0.0% / -2.1% | +1.2% | 2.4M |
| UNH | 371.43 (08:49 sip) | +0.0% | 371.29 | 10.27 (2.8%) | 366.00-404.04 | -3.7% / -7.0% | -1.1% | 5.1M |
| JNJ | 270.46 (08:35 sip) | +0.5% | 269.17 | 5.09 (1.9%) | 260.68-281.07 | -0.1% / +2.2% | +0.7% | 6.6M |
| WMT | 111.01 (08:49 sip) | +0.4% | 110.53 | 1.84 (1.7%) | 102.27-111.23 | +3.6% / +1.0% | +2.8% | 23.3M |
| COST | 910.49 (08:49 sip) | +0.6% | 904.70 | 11.77 (1.3%) | 885.50-964.45 | -1.2% / -3.2% | +1.2% | 2.1M |
| HD | 295.86 (08:49 sip) | -0.3% | 296.72 | 6.45 (2.2%) | 295.39-336.96 | -5.0% / -9.4% | -1.9% | 4.2M |
| CAT | 797.57 (08:49 sip) | -1.8% | 812.02 | 21.04 (2.6%) | 771.39-832.99 | +1.0% / -2.5% | +3.7% | 2.4M |
| BA | 199.16 (08:49 sip) | -0.4% | 199.93 | 5.75 (2.9%) | 195.46-215.29 | -3.1% / -7.1% | -1.0% | 6.2M |
| DAL | 81.10 (08:49 sip) | -0.8% | 81.75 | 2.17 (2.7%) | 75.99-84.99 | +2.5% / -2.9% | +5.0% | 6.8M |
| UAL | 109.54 (08:49 sip) | -1.1% | 110.72 | 3.77 (3.4%) | 104.15-119.73 | +1.1% / -5.1% | +4.2% | 3.7M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-09-23 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| WHLR | 4.44 (08:49 sip) | -18.4% | 5.44 | 1.07 (19.6%) | 1.65-14.78 | +11.7% / -72.6% | +57.9% | 5.9M |
| ARTL | 5.02 (08:49 sip) | -31.3% | 7.31 | 1.37 (18.7%) | 3.45-15.73 | +32.6% / +7.8% | +94.9% | 1.4M |
| IPDN | 4.30 (08:49 sip) | -20.7% | 5.42 | 0.97 (17.9%) | 2.96-7.70 | +47.0% / -26.8% | +77.1% | 3.0M |
| TJGC | 23.68 (06:05 sip) | +1.7% | 23.28 | 2.03 (8.7%) | 5.99-23.87 | +96.8% / +209.2% | +111.3% | 1.6M |
| DBGI | 5.56 (08:49 sip) | -2.6% | 5.71 | 1.15 (20.2%) | 3.14-8.60 | +11.4% / -50.8% | +39.3% | 2.1M |
| JAGX | 8.12 (08:49 sip) | -8.9% | 8.91 | 5.70 (64.0%) | 2.35-41.53 | +1.0% / -30.2% | +155.0% | 2.1M |
| CGEM | 16.79 (08:35 sip) | -0.5% | 16.87 | 1.26 (7.5%) | 16.78-23.19 | -20.8% / -14.6% | -18.2% | 1.0M |
| GRML | 13.00 (08:49 sip) | +16.2% | 11.19 | 2.12 (18.9%) | 2.82-18.21 | +114.7% / +40.3% | +273.6% | 19.5M |
| ALKT | 14.10 (08:49 sip) | -3.4% | 14.60 | 1.16 (7.9%) | 14.19-20.87 | -24.2% / -23.3% | -22.9% | 1.8M |
