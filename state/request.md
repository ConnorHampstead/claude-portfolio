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

- Time now: **09:05 ET** (13:05 UTC), Tuesday 2026-09-29. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$101,545.53**
- Cash: $140,283.64
- Session P&L so far: -0.16% (new entries are blocked at -3.0%)
- Gross exposure: $63,441 (62% of equity, cap 150%)
- Net exposure: $-31,052 (-31%, cap +/-100%)
- Risk at stake (entry to stop): $2,268 (2.23% of equity, cap 4.0%) — 1.77% left for new plays
- Slots: 3 open + 2 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| BA | short | 33 | 187.31 | 184.83 | +82 (+1.3%) | 194.90 | 176.00 | Safety headline on the MAX and a broken 20d floor, -7.6% vs 50d. A trade below today's 187.58 low means the opening rang |
| BAC | short | 267 | 55.80 | 55.60 | +53 (+0.4%) | 57.70 | 52.90 | Weakest large bank (-7.5% vs 20d avg). A break below today's opening low confirms the 20d-low support failed and opens a |
| HD | short | 61 | 289.30 | 291.69 | -146 (-0.8%) | 297.60 | 278.00 | Cleanest equity expression of frozen housing under 7%+ mortgages; -9.9% vs 50d with fresh 52-week lows. A trade below 28 |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| NVDA | long | 69 | 234.70 | stop | 227.40 | 246.00 | 2026-09-28 |
| ORCL | short | 65 | 130.90 | stop | 138.60 | 119.00 | 2026-09-28 |

### Record

4 closed trades: 2W / 2L, total +0.57R, net $+1,558 realized. Shorts taken: 4.

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
| BA | 185.26 (08:49 sip) | +0.5% | 184.39 | 6.52 (3.5%) | 184.01-215.29 | -9.4% / -13.7% | -8.3% | 7.2M |
| BAC | 55.66 (08:49 sip) | +0.3% | 55.47 | 1.40 (2.5%) | 55.37-63.83 | -7.0% / -9.4% | -4.3% | 37.2M |
| HD | 291.87 (08:45 sip) | +0.7% | 289.89 | 6.40 (2.2%) | 289.31-326.84 | -5.5% / -10.7% | -2.5% | 4.6M |
| NVDA | 230.39 (08:49 sip) | +0.7% | 228.86 | 5.15 (2.3%) | 208.93-234.50 | +3.0% / +5.8% | +0.7% | 114.7M |
| ORCL | 132.68 (08:49 sip) | +0.1% | 132.60 | 7.25 (5.5%) | 131.58-170.70 | -10.2% / -6.9% | -10.7% | 34.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 766.57 (08:49 sip) | +0.1% | 765.61 | 6.99 (0.9%) | 747.74-775.14 | +0.2% / +0.7% | -1.0% | 44.1M |
| QQQ | 738.63 (08:49 sip) | +0.3% | 736.53 | 10.02 (1.4%) | 699.27-748.35 | +2.1% / +3.3% | -0.7% | 33.7M |
| IWM | 280.58 (08:49 sip) | +0.2% | 280.02 | 3.65 (1.3%) | 278.80-295.41 | -2.6% / -4.5% | -1.9% | 23.1M |
| DIA | 514.79 (08:49 sip) | +0.1% | 514.02 | 5.08 (1.0%) | 510.42-536.38 | -1.5% / -2.3% | -1.1% | 3.4M |
| TLT | 78.67 (08:49 sip) | +0.1% | 78.62 | 0.84 (1.1%) | 78.27-82.50 | -3.1% / -4.0% | -3.9% | 38.2M |
| GLD | 380.62 (08:56 iex) | +0.7% | 377.91 | 7.37 (2.0%) | 376.88-413.54 | -5.0% / -4.5% | -5.1% | 9.7M |
| USO | 145.84 (08:57 iex) | -2.8% | 150.01 | 5.99 (4.0%) | 132.38-163.35 | +0.5% / +10.2% | +1.2% | 6.4M |
| SMH | 605.34 (08:49 sip) | +0.9% | 600.01 | 15.76 (2.6%) | 537.73-609.66 | +5.0% / +5.9% | +0.7% | 6.4M |
| XLK | 195.34 (08:49 sip) | +0.4% | 194.53 | 3.24 (1.7%) | 181.87-196.94 | +3.1% / +5.3% | -0.2% | 6.8M |
| XLF | 54.32 (08:49 sip) | +0.2% | 54.19 | 0.74 (1.4%) | 54.14-58.39 | -3.7% / -4.6% | -3.1% | 35.1M |
| XLE | 61.42 (08:49 sip) | -1.1% | 62.10 | 1.31 (2.1%) | 61.42-65.78 | -2.5% / +0.9% | -0.6% | 33.9M |
| XLV | 171.60 (08:49 sip) | +0.2% | 171.26 | 2.12 (1.2%) | 164.48-173.82 | +1.5% / +2.3% | +1.3% | 7.6M |
| XLI | 169.50 (08:25 sip) | +0.4% | 168.78 | 2.34 (1.4%) | 167.04-175.78 | -1.2% / -4.8% | -0.7% | 7.7M |
| XLY | 108.82 (04:30 sip) | -0.2% | 109.00 | 1.60 (1.5%) | 108.91-116.88 | -3.0% / -4.8% | -2.9% | 6.3M |
| XLP | 81.92 (08:45 sip) | -0.4% | 82.28 | 0.89 (1.1%) | 81.33-85.60 | -1.0% / -2.2% | +0.4% | 10.4M |
| XLU | 39.35 (08:49 sip) | +0.3% | 39.25 | 0.57 (1.5%) | 39.06-43.39 | -5.1% / -8.4% | -3.5% | 23.9M |
| XLB | 49.73 (08:30 sip) | +0.5% | 49.47 | 0.70 (1.4%) | 48.94-53.27 | -2.6% / -3.9% | -0.5% | 11.2M |
| XLRE | no trade today | - | 41.35 | 0.52 (1.3%) | 41.22-44.02 | -3.2% / -5.9% | -2.9% | 5.7M |
| XLC | no trade today | - | 111.18 | 1.95 (1.8%) | 109.95-115.61 | -1.0% / +0.1% | -3.1% | 5.1M |
| KRE | 70.68 (08:30 sip) | +0.2% | 70.55 | 1.23 (1.7%) | 70.09-75.07 | -2.9% / -5.2% | -2.0% | 13.9M |
| XHB | no trade today | - | 97.30 | 2.14 (2.2%) | 95.26-103.69 | -1.2% / -5.9% | +0.4% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 336.85 (09:03 iex) | -0.5% | 338.40 | 6.75 (2.0%) | 309.90-345.34 | +2.4% / +5.1% | -0.2% | 42.8M |
| MSFT | 508.63 (09:00 iex) | -0.1% | 509.22 | 11.26 (2.2%) | 486.00-519.40 | +1.9% / +6.6% | +1.5% | 21.4M |
| NVDA | 230.39 (08:49 sip) | +0.7% | 228.86 | 5.15 (2.3%) | 208.93-234.50 | +3.0% / +5.8% | +0.7% | 114.7M |
| AMZN | 246.75 (08:49 sip) | +0.2% | 246.15 | 5.41 (2.2%) | 244.30-264.36 | -2.8% / -3.9% | -4.8% | 34.5M |
| GOOGL | 342.65 (08:51 iex) | -0.0% | 342.75 | 8.89 (2.6%) | 327.74-364.17 | +0.2% / -0.4% | -3.4% | 26.8M |
| META | 723.35 (08:49 sip) | +1.1% | 715.62 | 31.28 (4.4%) | 555.66-779.82 | +7.2% / +16.0% | -3.5% | 23.6M |
| TSLA | 359.00 (08:49 sip) | +0.4% | 357.45 | 11.17 (3.1%) | 347.15-386.83 | -2.4% / +2.8% | -4.8% | 40.2M |
| AVGO | 352.00 (08:49 sip) | +0.7% | 349.57 | 9.69 (2.8%) | 335.20-372.07 | -2.0% / -6.9% | -3.6% | 27.7M |
| AMD | 614.05 (08:49 sip) | +1.0% | 607.87 | 26.20 (4.3%) | 440.50-639.00 | +13.6% / +19.9% | -1.2% | 22.0M |
| ORCL | 132.68 (08:49 sip) | +0.1% | 132.60 | 7.25 (5.5%) | 131.58-170.70 | -10.2% / -6.9% | -10.7% | 34.3M |
| NFLX | 69.96 (08:49 sip) | +1.1% | 69.23 | 2.05 (3.0%) | 68.88-83.60 | -9.1% / -8.4% | -5.6% | 33.1M |
| CRM | 226.57 (08:49 sip) | -0.3% | 227.27 | 8.49 (3.7%) | 221.18-267.80 | -7.8% / +6.0% | -3.9% | 13.4M |
| JPM | 337.36 (08:45 sip) | +0.2% | 336.59 | 7.25 (2.2%) | 335.28-362.86 | -3.9% / -4.7% | -4.4% | 8.0M |
| GS | 921.44 (08:45 sip) | +0.6% | 916.28 | 27.87 (3.0%) | 914.50-1,043.84 | -6.7% / -9.7% | -4.5% | 2.1M |
| BAC | 55.66 (08:49 sip) | +0.3% | 55.47 | 1.40 (2.5%) | 55.37-63.83 | -7.0% / -9.4% | -4.3% | 37.2M |
| XOM | 160.63 (08:40 sip) | -1.2% | 162.52 | 3.91 (2.4%) | 155.85-169.64 | -0.2% / +2.0% | +2.7% | 14.6M |
| CVX | 203.89 (08:49 sip) | -1.2% | 206.37 | 4.72 (2.3%) | 200.78-217.78 | -1.5% / +2.8% | +1.3% | 10.3M |
| LLY | 1,188.06 (08:49 sip) | +0.3% | 1,184.78 | 28.21 (2.4%) | 1,113.29-1,197.79 | +2.9% / +0.7% | +1.7% | 2.3M |
| UNH | 377.84 (08:49 sip) | +0.0% | 377.83 | 9.63 (2.5%) | 366.00-404.04 | -1.4% / -4.7% | +0.1% | 5.2M |
| JNJ | 272.02 (08:10 sip) | +0.0% | 271.95 | 4.80 (1.8%) | 260.68-281.07 | +0.8% / +2.7% | +0.9% | 6.5M |
| WMT | 107.86 (08:49 sip) | -0.8% | 108.73 | 1.86 (1.7%) | 102.84-111.23 | +1.2% / -0.4% | +1.2% | 22.6M |
| COST | 918.58 (08:40 sip) | -0.5% | 922.92 | 14.32 (1.6%) | 883.10-952.10 | +1.3% / -1.2% | +2.7% | 2.4M |
| HD | 291.87 (08:45 sip) | +0.7% | 289.89 | 6.40 (2.2%) | 289.31-326.84 | -5.5% / -10.7% | -2.5% | 4.6M |
| CAT | 827.00 (08:45 sip) | +0.9% | 819.95 | 20.69 (2.5%) | 771.39-830.50 | +1.9% / -1.0% | +0.4% | 2.4M |
| BA | 185.26 (08:49 sip) | +0.5% | 184.39 | 6.52 (3.5%) | 184.01-215.29 | -9.4% / -13.7% | -8.3% | 7.2M |
| DAL | 85.30 (08:45 sip) | +1.5% | 84.03 | 2.49 (3.0%) | 75.99-85.47 | +4.9% / -0.0% | +1.9% | 7.1M |
| UAL | 113.28 (08:49 sip) | +1.6% | 111.51 | 4.24 (3.8%) | 104.15-118.26 | +1.9% / -4.1% | -2.5% | 3.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-09-28 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| KOD | 86.98 (08:49 sip) | -3.3% | 89.92 | 6.31 (7.0%) | 29.81-95.77 | +144.4% / +128.2% | +177.4% | 2.8M |
| CLRO | 4.48 (08:49 sip) | -12.2% | 5.10 | 0.53 (10.4%) | 3.34-6.00 | +10.9% / -3.9% | +14.3% | 1.5M |
| BEZ | 5.45 (08:49 sip) | -6.1% | 5.80 | 0.79 (13.7%) | 4.75-12.15 | -14.0% / -46.2% | +2.5% | 3.7M |
| JAGX | 5.55 (08:49 sip) | -7.8% | 6.02 | 5.99 (99.5%) | 2.35-41.53 | -23.9% / -49.0% | +125.5% | 3.7M |
