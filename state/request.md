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

- Time now: **09:05 ET** (13:05 UTC, 15:05 Stockholm), Friday 2026-10-23. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,199.37**
- Cash: $92,967.61
- Session P&L so far: -0.04% (new entries are blocked at -3.0%)
- Gross exposure: $65,050 (63% of equity, cap 150%)
- Net exposure: $+27,750 (+27%, cap +/-100%)
- Risk at stake (entry to stop): $1,466 (1.42% of equity, cap 4.0%) — 2.58% left for new plays
- Slots: 4 open + 1 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| GOOGL | short | 28 | 332.42 | 321.65 | +302 (+3.2%) | 337.00 | 320.00 | Relative weakness breaking the floor of the 20-day range on a tech-bid day; failed floor opens ~4% to 320. |
| NVDA | short | 26 | 212.38 | 212.27 | +3 (+0.1%) | 222.00 | 198.00 | A break of the 212.85 20d low confirms Monday's bounce failed in the bellwether and opens a move toward 198. |
| ORCL | short | 33 | 129.70 | 124.99 | +155 (+3.6%) | 132.00 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |
| XLV | long | 160 | 179.57 | 180.51 | +150 (+0.5%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XOM | long | 97 | 180.60 | stop | 175.40 | 189.00 | 2026-10-21 |

### Record

23 closed trades: 9W / 14L, total +1.41R, net $+2,598 realized. Shorts taken: 23.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| CVX | long | stop | -0.23R | $-117 | 40% |
| AMD | short | target | +1.17R | $+575 | 42% |
| HD | long | target | +1.47R | $+373 | 37% |
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |

### Ideas you passed on, replayed against the tape

57 resolved: 17 reached target first, 28 stop first, 9 never reached the entry, 3 expired, 0 ambiguous. Average -0.07R across the 48 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-16 pre-market | SMH | short | Ninth straight down day; factor already banked at target 10/15; only a bounce sa | never filled | - | 35% |
| 2026-10-09 pre-market | DAL | short | Q3 miss and FY cut are real, but oil is falling the same day, easing the fuel he | expired | -0.43R | 33% |
| 2026-10-22 pre-market | META | short | Post-earnings break under the 20d low, but it would be a fifth AI-capex short an | target | +1.36R | 33% |
| 2026-10-16 open | AMD | short | Chasing a -9.4% 5-day move 14 points above the 20d low, with a ~1 ATR stop, into | target | +1.41R | 33% |
| 2026-10-15 pre-market | XLP | long | Same staples view as WMT; 1.4-ATR gap; no need to double up. | target | +2.00R | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| GOOGL | 321.58 (08:49 sip) | -0.8% | 324.22 | 8.48 (2.6%) | 322.00-359.40 | -5.8% / -5.6% | -7.2% | 24.1M |
| NVDA | 212.03 (08:57 iex) | -0.1% | 212.21 | 6.15 (2.9%) | 211.26-243.37 | -6.2% / -4.7% | -2.3% | 106.8M |
| ORCL | 124.46 (08:49 sip) | -0.9% | 125.54 | 6.66 (5.3%) | 122.76-146.40 | -7.6% / -12.2% | -6.6% | 29.6M |
| XLV | 180.62 (08:49 sip) | -0.4% | 181.30 | 3.11 (1.7%) | 165.19-182.25 | +5.4% / +6.3% | +2.3% | 8.6M |
| XOM | 179.20 (08:45 sip) | +0.5% | 178.23 | 3.77 (2.1%) | 159.27-180.31 | +5.0% / +7.9% | +2.0% | 11.4M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 760.13 (08:54 iex) | -0.5% | 763.96 | 7.30 (1.0%) | 758.79-781.62 | -0.9% / -0.4% | -1.0% | 40.9M |
| QQQ | 703.00 (09:03 iex) | -0.2% | 704.47 | 12.04 (1.7%) | 701.90-762.86 | -4.4% / -3.0% | -3.2% | 37.0M |
| IWM | 274.87 (08:53 iex) | -0.7% | 276.67 | 3.75 (1.4%) | 269.88-284.64 | -0.3% / -3.5% | +0.6% | 25.7M |
| DIA | 523.31 (08:49 sip) | -0.9% | 527.89 | 5.15 (1.0%) | 504.59-528.45 | +2.3% / +1.1% | +1.3% | 3.3M |
| TLT | 81.79 (09:04 iex) | +0.1% | 81.74 | 0.85 (1.0%) | 76.43-81.92 | +4.0% / +1.8% | +2.2% | 50.2M |
| GLD | 369.06 (08:49 sip) | +0.0% | 369.00 | 5.17 (1.4%) | 368.35-394.22 | -3.0% / -6.6% | -3.6% | 8.2M |
| USO | 165.57 (08:49 sip) | +1.9% | 162.51 | 4.39 (2.7%) | 141.76-163.77 | +7.1% / +11.6% | +3.3% | 5.1M |
| SMH | 523.74 (08:49 sip) | +0.1% | 523.35 | 18.07 (3.5%) | 520.53-639.47 | -11.2% / -9.2% | -6.4% | 8.2M |
| XLK | 181.85 (08:49 sip) | -0.3% | 182.34 | 4.04 (2.2%) | 181.50-203.25 | -6.0% / -3.9% | -3.6% | 8.7M |
| XLF | 56.30 (08:49 sip) | -0.6% | 56.65 | 0.70 (1.2%) | 52.81-56.67 | +3.7% / +1.1% | +2.5% | 36.4M |
| XLE | 68.03 (08:49 sip) | +0.7% | 67.57 | 1.44 (2.1%) | 60.95-68.78 | +3.9% / +5.6% | +1.5% | 32.0M |
| XLV | 180.62 (08:49 sip) | -0.4% | 181.30 | 3.11 (1.7%) | 165.19-182.25 | +5.4% / +6.3% | +2.3% | 8.6M |
| XLI | 165.64 (08:49 sip) | -0.7% | 166.73 | 2.61 (1.6%) | 164.66-172.34 | -1.1% / -3.3% | -0.7% | 7.5M |
| XLY | 114.31 (08:40 sip) | -0.6% | 115.01 | 1.50 (1.3%) | 107.99-116.22 | +2.8% / +1.4% | +1.4% | 7.2M |
| XLP | 89.52 (08:49 sip) | -0.5% | 89.99 | 1.30 (1.4%) | 80.10-89.99 | +7.1% / +7.1% | +3.8% | 13.5M |
| XLU | 42.70 (08:45 sip) | -0.4% | 42.87 | 0.70 (1.6%) | 39.03-42.88 | +4.6% / +2.7% | +2.9% | 36.7M |
| XLB | 51.45 (08:40 sip) | -0.5% | 51.69 | 0.70 (1.4%) | 47.81-51.71 | +3.7% / +1.5% | +2.2% | 11.4M |
| XLRE | 42.96 (08:49 sip) | +1.0% | 42.52 | 0.62 (1.5%) | 40.28-42.61 | +2.5% / -0.5% | +1.3% | 7.8M |
| XLC | 106.19 (08:45 sip) | -1.1% | 107.42 | 1.66 (1.5%) | 106.73-113.52 | -3.1% / -3.7% | -4.5% | 6.5M |
| KRE | 71.89 (08:49 sip) | -0.7% | 72.41 | 1.29 (1.8%) | 67.79-72.43 | +3.5% / +0.2% | +3.8% | 16.1M |
| XHB | 97.67 (08:10 sip) | -1.5% | 99.20 | 2.31 (2.3%) | 91.87-99.28 | +3.4% / -0.1% | +3.6% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 347.51 (09:03 iex) | -0.2% | 348.22 | 6.08 (1.7%) | 325.81-348.36 | +2.8% / +6.0% | +1.8% | 38.2M |
| MSFT | 518.61 (08:49 sip) | -0.5% | 521.08 | 11.38 (2.2%) | 497.25-551.15 | -1.0% / +2.6% | -3.4% | 21.5M |
| NVDA | 212.03 (08:57 iex) | -0.1% | 212.21 | 6.15 (2.9%) | 211.26-243.37 | -6.2% / -4.7% | -2.3% | 106.8M |
| AMZN | 248.75 (08:49 sip) | -0.7% | 250.38 | 7.11 (2.8%) | 244.72-265.34 | -1.6% / -2.2% | -1.7% | 36.3M |
| GOOGL | 321.58 (08:49 sip) | -0.8% | 324.22 | 8.48 (2.6%) | 322.00-359.40 | -5.8% / -5.6% | -7.2% | 24.1M |
| META | 642.99 (08:49 sip) | -0.9% | 648.85 | 25.57 (3.9%) | 639.69-771.27 | -10.3% / -2.1% | -11.9% | 19.9M |
| TSLA | 374.29 (08:49 sip) | -0.1% | 374.58 | 12.03 (3.2%) | 345.88-388.86 | +1.3% / +3.2% | +3.3% | 37.1M |
| AVGO | 321.53 (08:51 iex) | -0.5% | 323.24 | 11.88 (3.7%) | 321.02-380.84 | -7.7% / -9.8% | -6.1% | 21.7M |
| AMD | 508.31 (08:49 sip) | +0.1% | 507.93 | 29.12 (5.7%) | 502.60-658.52 | -14.3% / -6.2% | -9.7% | 19.7M |
| ORCL | 124.46 (08:49 sip) | -0.9% | 125.54 | 6.66 (5.3%) | 122.76-146.40 | -7.6% / -12.2% | -6.6% | 29.6M |
| NFLX | 66.80 (08:49 sip) | -0.4% | 67.05 | 2.02 (3.0%) | 64.10-73.07 | -3.4% / -10.0% | -7.7% | 41.7M |
| CRM | 248.70 (08:40 sip) | -0.6% | 250.29 | 8.68 (3.5%) | 220.29-252.42 | +6.6% / +7.0% | +1.4% | 8.1M |
| JPM | 334.70 (08:49 sip) | -0.5% | 336.54 | 6.16 (1.8%) | 324.25-344.40 | +0.9% / -2.4% | +0.3% | 7.8M |
| GS | 882.00 (08:49 sip) | -1.0% | 891.30 | 24.29 (2.7%) | 859.03-935.83 | -0.5% / -7.3% | +0.0% | 2.3M |
| BAC | 50.65 (08:49 sip) | -0.8% | 51.08 | 1.29 (2.5%) | 49.26-56.74 | -4.0% / -11.8% | -1.2% | 42.7M |
| XOM | 179.20 (08:45 sip) | +0.5% | 178.23 | 3.77 (2.1%) | 159.27-180.31 | +5.0% / +7.9% | +2.0% | 11.4M |
| CVX | 228.37 (08:49 sip) | +0.7% | 226.68 | 4.86 (2.1%) | 201.96-229.04 | +6.0% / +8.2% | +3.4% | 7.3M |
| LLY | 1,302.91 (08:35 sip) | -0.3% | 1,306.69 | 39.62 (3.0%) | 1,131.21-1,321.21 | +8.9% / +10.2% | +4.4% | 2.3M |
| UNH | 423.36 (08:49 sip) | -0.4% | 424.98 | 13.24 (3.1%) | 362.60-426.55 | +9.8% / +9.8% | +4.5% | 6.1M |
| JNJ | 265.98 (08:49 sip) | -0.6% | 267.61 | 6.92 (2.6%) | 245.17-273.78 | +3.2% / +1.0% | +5.7% | 7.9M |
| WMT | 120.90 (08:49 sip) | -0.2% | 121.12 | 2.52 (2.1%) | 103.39-121.38 | +8.5% / +10.8% | +2.8% | 21.3M |
| COST | 1,011.66 (07:45 sip) | -0.6% | 1,018.21 | 15.82 (1.6%) | 883.10-1,018.86 | +6.7% / +8.5% | +4.1% | 2.3M |
| HD | 324.30 (08:40 sip) | -1.0% | 327.73 | 7.15 (2.2%) | 277.15-327.92 | +10.6% / +5.8% | +6.3% | 5.4M |
| CAT | 698.50 (08:49 sip) | -0.8% | 704.05 | 30.74 (4.4%) | 695.33-876.95 | -10.6% / -12.3% | -4.3% | 2.6M |
| BA | 185.95 (08:49 sip) | -0.9% | 187.55 | 3.98 (2.1%) | 183.38-201.40 | -1.1% / -7.1% | -0.6% | 8.1M |
| DAL | 78.00 (08:49 sip) | -1.6% | 79.26 | 2.98 (3.8%) | 74.14-85.93 | -1.8% / -2.2% | +1.5% | 7.5M |
| UAL | 100.28 (08:45 sip) | -1.7% | 102.00 | 4.78 (4.7%) | 94.54-115.71 | -3.8% / -7.0% | +0.7% | 5.0M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-22 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| BHVN | 14.85 (08:49 sip) | +1.1% | 14.69 | 0.98 (6.6%) | 10.70-16.54 | +19.5% / +8.8% | +28.5% | 3.3M |
| AAOZ | 22.71 (08:49 sip) | -2.2% | 23.22 | 2.51 (10.8%) | 7.63-24.03 | +65.5% / +74.7% | +41.4% | 1.9M |
| LITZ | 33.37 (08:49 sip) | -3.6% | 34.60 | 3.44 (9.9%) | 16.35-34.99 | +44.4% / +21.5% | +26.9% | 1.9M |
| SOXS | 52.88 (09:04 iex) | -1.1% | 53.45 | 4.30 (8.0%) | 28.46-54.31 | +41.7% / +28.0% | +22.5% | 78.5M |
| AVTX | 7.17 (08:05 sip) | -3.8% | 7.45 | 1.18 (15.9%) | 6.85-15.99 | -43.6% / -54.3% | -38.0% | 2.4M |
| TTMI | 75.11 (08:49 sip) | +1.7% | 73.89 | 10.72 (14.5%) | 71.71-137.88 | -35.3% / -37.7% | -27.1% | 3.8M |
| AXTX | 14.90 (08:49 sip) | +7.5% | 13.86 | 4.73 (34.1%) | 13.48-44.60 | -50.3% / -53.4% | -24.5% | 3.5M |
| COHX | 10.94 (08:49 sip) | +1.7% | 10.76 | 3.28 (30.5%) | 10.37-31.06 | -50.2% / -54.3% | -33.0% | 1.5M |
