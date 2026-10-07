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

- Time now: **09:05 ET** (13:05 UTC), Wednesday 2026-10-07. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$100,996.65**
- Cash: $51,591.63
- Session P&L so far: -0.78% (new entries are blocked at -3.0%)
- Gross exposure: $116,924 (116% of equity, cap 150%)
- Net exposure: $+32,673 (+32%, cap +/-100%)
- Risk at stake (entry to stop): $2,370 (2.35% of equity, cap 4.0%) — 1.65% left for new plays
- Slots: 5 open + 1 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 34% of equity in notional: at 1% risk its stop must be at least 2.9% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 34% of equity in notional: at 1% risk its stop must be at least 2.9% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| CAT | long | 10 | 861.00 | 849.00 | -120 (-1.4%) | 849.00 | 896.00 | Industrial momentum leader with data-center power exposure; a break of the one-month ceiling at 858.87 opens a measured  |
| IWM | long | 111 | 281.50 | 278.85 | -294 (-0.9%) | 276.90 | 289.50 | Small caps are the most rate-damaged group (-4.5% vs 50d) and the most direct beneficiary of a rates reversal. A limit h |
| JNJ | short | 99 | 254.46 | 256.50 | -202 (-0.8%) | 259.90 | 247.10 | Defensive under rate pressure with persistent relative weakness (Stelara biosimilar overhang). A break of the 20d low op |
| MSFT | long | 36 | 527.65 | 528.00 | +12 (+0.1%) | 515.00 | 548.00 | MSFT is +3.2% vs 20d and +6.2% vs 50d and has held up under higher rates. A break of 522.85 clears a three-week ceiling  |
| NVDA | long | 69 | 236.40 | 236.93 | +37 (+0.2%) | 233.00 | 246.00 | Only mega-cap with a dated positive catalyst and green on a red tape. A break through the 20d high of 234.50 means range |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XLE | short | 269 | 62.20 | stop | 64.10 | 59.60 | 2026-10-06 |

### Record

11 closed trades: 4W / 7L, total -0.62R, net $+1,567 realized. Shorts taken: 11.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| WMT | short | stop | -1.00R | $-254 | 34% |
| UNH | short | stop | -1.01R | $-253 | 36% |
| DAL | long | close | -0.53R | $-291 | 42% |
| XLRE | short | stop | -1.01R | $-529 | 40% |
| BAC | short | target | +1.53R | $+774 | 36% |

### Ideas you passed on, replayed against the tape

11 resolved: 2 reached target first, 6 stop first, 2 never reached the entry, 1 expired, 0 ambiguous. Average -0.25R across the 9 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-09-30 pre-market | XHB | long | Soft-PCE housing relief would fight my own HD short; a 2bp yield dip is not a re | never filled | - | 35% |
| 2026-09-23 pre-market | KRE | short | Same financials thesis as BAC short; avoiding doubling sector exposure and regio | expired | +0.36R | 35% |
| 2026-09-29 pre-market | CVX | short | Pure Iran-headline trade sitting at the 20d low; wrong location. | never filled | - | 38% |
| 2026-10-02 pre-market | XHB | long | Same rate-relief factor as the IWM long, already +2.4% pre-market; one rates lon | stop | -1.00R | 38% |
| 2026-10-02 open | XHB | long | Faded from 98.73 open to 97.67; same rate factor as the resting IWM limit. | stop | -0.98R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| CAT | 846.20 (08:49 sip) | -2.0% | 863.44 | 22.61 (2.6%) | 772.86-876.95 | +5.9% / +5.0% | +4.5% | 2.3M |
| IWM | 278.94 (08:49 sip) | -0.9% | 281.34 | 3.70 (1.3%) | 275.45-293.39 | -0.8% / -3.5% | +0.8% | 25.0M |
| JNJ | 256.45 (08:49 sip) | +0.7% | 254.78 | 4.81 (1.9%) | 251.17-275.23 | -4.2% / -3.9% | -4.8% | 6.8M |
| MSFT | 527.10 (08:49 sip) | -0.4% | 529.30 | 12.21 (2.3%) | 486.00-535.69 | +4.9% / +7.3% | +4.0% | 21.9M |
| NVDA | 237.24 (08:49 sip) | -0.8% | 239.24 | 5.37 (2.2%) | 208.93-243.37 | +6.4% / +8.9% | +5.3% | 109.9M |
| XLE | 64.00 (08:49 sip) | +0.4% | 63.75 | 1.15 (1.8%) | 60.95-65.78 | +0.8% / +2.8% | +3.6% | 34.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 776.19 (08:49 sip) | -0.4% | 779.09 | 6.90 (0.9%) | 747.74-781.62 | +1.8% / +2.0% | +1.9% | 46.3M |
| QQQ | 754.64 (09:03 iex) | -0.7% | 759.66 | 9.58 (1.3%) | 699.27-762.86 | +3.9% / +5.6% | +2.9% | 33.6M |
| IWM | 278.94 (08:49 sip) | -0.9% | 281.34 | 3.70 (1.3%) | 275.45-293.39 | -0.8% / -3.5% | +0.8% | 25.0M |
| DIA | 510.56 (08:49 sip) | -0.8% | 514.56 | 4.73 (0.9%) | 504.70-526.15 | -0.3% / -2.1% | +0.3% | 3.4M |
| TLT | 76.56 (08:51 iex) | -0.9% | 77.28 | 0.85 (1.1%) | 76.69-81.98 | -2.8% / -4.5% | -0.8% | 50.1M |
| GLD | 374.57 (08:57 iex) | -2.0% | 382.27 | 6.03 (1.6%) | 376.88-406.56 | -2.2% / -3.6% | -0.2% | 8.5M |
| USO | 145.53 (08:49 sip) | +0.4% | 144.91 | 5.47 (3.8%) | 141.76-163.35 | -3.9% / +5.1% | +1.1% | 6.4M |
| SMH | 621.55 (08:49 sip) | -1.7% | 632.50 | 14.20 (2.2%) | 537.73-639.47 | +7.1% / +10.4% | +4.2% | 6.0M |
| XLK | 200.24 (08:49 sip) | -0.9% | 202.00 | 2.94 (1.5%) | 181.87-203.25 | +4.9% / +7.9% | +3.9% | 7.3M |
| XLF | 53.67 (08:49 sip) | -0.6% | 54.01 | 0.68 (1.3%) | 52.81-57.41 | -2.0% / -4.5% | +0.0% | 37.3M |
| XLE | 64.00 (08:49 sip) | +0.4% | 63.75 | 1.15 (1.8%) | 60.95-65.78 | +0.8% / +2.8% | +3.6% | 34.8M |
| XLV | 167.69 (08:49 sip) | +0.4% | 167.09 | 2.38 (1.4%) | 164.48-171.87 | -0.5% / -0.7% | -2.1% | 8.0M |
| XLI | 170.78 (08:49 sip) | -0.5% | 171.58 | 2.23 (1.3%) | 166.18-173.69 | +1.2% / -2.5% | +1.4% | 7.4M |
| XLY | 111.21 (08:00 sip) | -0.5% | 111.72 | 1.46 (1.3%) | 107.99-113.29 | +0.8% / -2.2% | +2.4% | 6.7M |
| XLP | 81.97 (08:40 sip) | +0.2% | 81.80 | 0.90 (1.1%) | 80.10-84.33 | -0.4% / -2.4% | -0.1% | 10.9M |
| XLU | 40.97 (08:49 sip) | -0.5% | 41.16 | 0.60 (1.5%) | 39.03-43.21 | +1.4% / -2.5% | +3.7% | 32.2M |
| XLB | 49.49 (08:49 sip) | -0.5% | 49.73 | 0.74 (1.5%) | 47.81-51.91 | -0.3% / -3.1% | +1.3% | 11.8M |
| XLRE | 40.99 (08:20 sip) | -0.3% | 41.10 | 0.50 (1.2%) | 40.41-43.54 | -2.0% / -5.4% | -0.6% | 6.3M |
| XLC | no trade today | - | 111.65 | 1.81 (1.6%) | 109.66-115.61 | -0.4% / +0.2% | +0.2% | 6.1M |
| KRE | 69.33 (08:49 sip) | -1.1% | 70.07 | 1.21 (1.7%) | 67.97-74.43 | -2.1% / -5.1% | +0.3% | 15.3M |
| XHB | 96.56 (07:30 sip) | -0.8% | 97.37 | 2.09 (2.1%) | 94.08-100.34 | +0.2% / -4.8% | +0.4% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 336.52 (08:49 sip) | +0.9% | 333.63 | 6.42 (1.9%) | 309.90-345.34 | +0.1% / +3.5% | +1.3% | 41.9M |
| MSFT | 527.10 (08:49 sip) | -0.4% | 529.30 | 12.21 (2.3%) | 486.00-535.69 | +4.9% / +7.3% | +4.0% | 21.9M |
| NVDA | 237.24 (08:49 sip) | -0.8% | 239.24 | 5.37 (2.2%) | 208.93-243.37 | +6.4% / +8.9% | +5.3% | 109.9M |
| AMZN | 253.95 (08:49 sip) | -0.9% | 256.29 | 5.28 (2.1%) | 244.30-259.49 | +2.0% / -0.4% | +3.9% | 35.9M |
| GOOGL | 346.55 (08:49 sip) | -0.3% | 347.68 | 8.86 (2.5%) | 327.74-364.17 | +1.2% / +0.7% | +2.0% | 27.4M |
| META | 733.55 (08:49 sip) | -0.7% | 738.88 | 28.39 (3.8%) | 638.06-779.82 | +4.3% / +17.2% | +0.0% | 23.4M |
| TSLA | 377.90 (08:49 sip) | -0.7% | 380.68 | 11.67 (3.1%) | 345.88-386.83 | +3.8% / +8.7% | +7.9% | 36.1M |
| AVGO | 371.96 (08:49 sip) | -1.0% | 375.81 | 10.62 (2.8%) | 335.20-380.84 | +6.0% / +1.0% | +5.8% | 24.5M |
| AMD | 637.22 (09:02 iex) | -1.9% | 649.42 | 25.32 (3.9%) | 480.33-658.52 | +11.7% / +25.2% | +6.9% | 22.2M |
| ORCL | 142.20 (08:49 sip) | -1.8% | 144.77 | 6.08 (4.2%) | 131.58-166.00 | +0.3% / +0.1% | +5.1% | 35.0M |
| NFLX | 68.85 (08:49 sip) | +0.2% | 68.69 | 1.80 (2.6%) | 66.54-81.02 | -5.3% / -9.0% | -2.3% | 35.7M |
| CRM | 225.27 (08:49 sip) | +0.1% | 224.99 | 8.12 (3.6%) | 221.18-261.87 | -5.6% / +1.3% | -0.1% | 11.4M |
| JPM | 326.90 (08:49 sip) | -1.3% | 331.28 | 5.85 (1.8%) | 324.25-358.26 | -2.9% / -5.2% | -0.6% | 8.5M |
| GS | 881.55 (08:49 sip) | -1.7% | 897.18 | 20.32 (2.3%) | 881.00-1,042.99 | -5.1% / -9.8% | -2.1% | 2.2M |
| BAC | 53.28 (08:45 sip) | -1.5% | 54.09 | 0.95 (1.8%) | 52.89-63.83 | -5.4% / -10.4% | -1.6% | 39.2M |
| XOM | 166.08 (08:49 sip) | +1.0% | 164.48 | 3.23 (2.0%) | 155.85-169.64 | +0.8% / +2.4% | +1.9% | 13.8M |
| CVX | 208.77 (08:49 sip) | +0.6% | 207.58 | 3.89 (1.9%) | 200.78-217.78 | -0.4% / +2.5% | +1.6% | 9.8M |
| LLY | 1,169.04 (08:49 sip) | +1.0% | 1,157.49 | 32.29 (2.8%) | 1,113.29-1,215.00 | +0.4% / -1.4% | -2.3% | 2.2M |
| UNH | 374.05 (08:49 sip) | -0.6% | 376.32 | 7.54 (2.0%) | 362.60-404.04 | +0.0% / -3.6% | +0.4% | 5.0M |
| JNJ | 256.45 (08:49 sip) | +0.7% | 254.78 | 4.81 (1.9%) | 251.17-275.23 | -4.2% / -3.9% | -4.8% | 6.8M |
| WMT | 108.03 (08:49 sip) | +0.8% | 107.20 | 2.21 (2.1%) | 103.39-111.23 | +0.1% / -1.3% | +0.4% | 22.2M |
| COST | 946.33 (08:49 sip) | +1.1% | 935.68 | 15.16 (1.6%) | 883.10-937.04 | +2.9% / +0.3% | +1.2% | 2.4M |
| HD | 284.64 (08:49 sip) | -0.7% | 286.69 | 6.40 (2.2%) | 277.15-313.38 | -3.3% / -10.2% | -0.5% | 5.2M |
| CAT | 846.20 (08:49 sip) | -2.0% | 863.44 | 22.61 (2.6%) | 772.86-876.95 | +5.9% / +5.0% | +4.5% | 2.3M |
| BA | 187.83 (08:49 sip) | -1.0% | 189.82 | 6.38 (3.4%) | 184.01-212.40 | -4.1% / -10.3% | +1.1% | 8.7M |
| DAL | 82.30 (08:45 sip) | -1.6% | 83.66 | 2.43 (2.9%) | 76.89-86.17 | +2.3% / -0.4% | -1.4% | 7.7M |
| UAL | 110.00 (08:49 sip) | -1.7% | 111.87 | 4.04 (3.6%) | 104.59-118.26 | +1.3% / -3.2% | -0.7% | 4.1M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-06 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| APUS | 7.48 (08:49 sip) | +4.9% | 7.13 | 1.79 (25.1%) | 1.51-9.14 | +107.4% / +78.1% | +42.0% | 10.4M |
| OPCH | 31.03 (08:49 sip) | +0.1% | 31.00 | 1.16 (3.7%) | 22.29-31.11 | +30.1% / +30.6% | +35.9% | 5.4M |
| XRPN | 19.00 (08:49 sip) | -1.0% | 19.20 | 6.46 (33.7%) | 10.51-53.00 | +29.0% / +56.7% | +48.8% | 1.4M |
| AVBP | 15.15 (08:49 sip) | +0.4% | 15.09 | 2.69 (17.8%) | 11.36-31.49 | -46.8% / -48.9% | -48.9% | 1.6M |
| AEHG | 7.26 (08:57 iex) | -2.3% | 7.43 | 1.43 (19.2%) | 6.01-10.62 | -11.4% / -22.5% | -18.4% | 1.5M |
| SAIQ | 4.22 (08:49 sip) | -18.2% | 5.16 | 2.02 (39.2%) | 1.76-12.95 | -43.0% / -48.5% | -50.6% | 3.7M |
