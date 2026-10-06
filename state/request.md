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

- Time now: **09:05 ET** (13:05 UTC), Tuesday 2026-10-06. The cash session opens at 09:30 ET, in 25 min, and closes at 16:00 ET. Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,551.33**
- Cash: $72,346.79
- Session P&L so far: +0.47% (new entries are blocked at -3.0%)
- Gross exposure: $104,471 (102% of equity, cap 150%)
- Net exposure: $+30,205 (+29%, cap +/-100%)
- Risk at stake (entry to stop): $2,559 (2.50% of equity, cap 4.0%) — 1.50% left for new plays
- Slots: 5 open + 0 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 48% of equity in notional: at 1% risk its stop must be at least 2.1% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 48% of equity in notional: at 1% risk its stop must be at least 2.1% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| IWM | long | 111 | 281.50 | 284.57 | +341 (+1.1%) | 276.90 | 289.50 | Small caps are the most rate-damaged group (-4.5% vs 50d) and the most direct beneficiary of a rates reversal. A limit h |
| JNJ | short | 99 | 254.46 | 253.39 | +106 (+0.4%) | 259.90 | 247.10 | Defensive under rate pressure with persistent relative weakness (Stelara biosimilar overhang). A break of the 20d low op |
| MSFT | long | 36 | 527.65 | 530.15 | +90 (+0.5%) | 510.00 | 548.00 | MSFT is +3.2% vs 20d and +6.2% vs 50d and has held up under higher rates. A break of 522.85 clears a three-week ceiling  |
| NVDA | long | 69 | 236.40 | 241.52 | +353 (+2.2%) | 227.40 | 246.00 | Only mega-cap with a dated positive catalyst and green on a red tape. A break through the 20d high of 234.50 means range |
| WMT | short | 115 | 103.40 | 104.76 | -156 (-1.3%) | 105.60 | 100.10 | Staples are the weakest sector and WMT sits on its 20d low; a break targets the 99-100 area near the 52-week low. |

### Record

10 closed trades: 4W / 6L, total +0.38R, net $+1,822 realized. Shorts taken: 10.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| UNH | short | stop | -1.01R | $-253 | 36% |
| DAL | long | close | -0.53R | $-291 | 42% |
| XLRE | short | stop | -1.01R | $-529 | 40% |
| BAC | short | target | +1.53R | $+774 | 36% |
| HD | short | target | +1.36R | $+691 | 40% |

### Ideas you passed on, replayed against the tape

9 resolved: 2 reached target first, 6 stop first, 1 never reached the entry, 0 expired, 0 ambiguous. Average -0.33R across the 8 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-09-29 pre-market | CVX | short | Pure Iran-headline trade sitting at the 20d low; wrong location. | never filled | - | 38% |
| 2026-10-02 pre-market | XHB | long | Same rate-relief factor as the IWM long, already +2.4% pre-market; one rates lon | stop | -1.00R | 38% |
| 2026-10-02 open | XHB | long | Faded from 98.73 open to 97.67; same rate factor as the resting IWM limit. | stop | -0.98R | 38% |
| 2026-09-30 pre-market | TSLA | short | Best short: break of 20d low 349.92, but Q3 deliveries (~Oct 2) are a company bi | stop | -1.00R | 38% |
| 2026-10-01 pre-market | KRE | short | Same rates factor as BAC short already held; no slot. | stop | -1.00R | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| IWM | 284.22 (08:49 sip) | +0.3% | 283.38 | 3.85 (1.4%) | 275.45-295.33 | -0.3% / -2.9% | +1.2% | 24.7M |
| JNJ | 253.20 (08:49 sip) | +0.1% | 252.93 | 4.67 (1.8%) | 252.51-275.23 | -5.1% / -4.6% | -7.0% | 6.9M |
| MSFT | 530.00 (08:49 sip) | +0.9% | 525.18 | 12.17 (2.3%) | 486.00-532.35 | +4.4% / +7.1% | +3.1% | 21.8M |
| NVDA | 241.05 (08:49 sip) | +0.9% | 238.90 | 5.38 (2.3%) | 208.93-240.10 | +6.6% / +9.2% | +4.4% | 111.0M |
| WMT | 104.85 (08:49 sip) | -0.2% | 105.07 | 2.08 (2.0%) | 103.39-111.23 | -1.8% / -3.3% | -3.4% | 22.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 777.28 (08:49 sip) | +0.3% | 774.83 | 7.28 (0.9%) | 747.74-776.61 | +1.4% / +1.6% | +1.2% | 46.7M |
| QQQ | 760.08 (08:59 iex) | +0.5% | 756.20 | 9.96 (1.3%) | 699.27-756.92 | +3.7% / +5.4% | +2.7% | 33.7M |
| IWM | 284.22 (08:49 sip) | +0.3% | 283.38 | 3.85 (1.4%) | 275.45-295.33 | -0.3% / -2.9% | +1.2% | 24.7M |
| DIA | 514.15 (08:49 sip) | +0.4% | 512.11 | 5.17 (1.0%) | 504.70-529.17 | -0.9% / -2.5% | -0.4% | 3.5M |
| TLT | 77.32 (08:49 sip) | +0.3% | 77.11 | 0.88 (1.1%) | 76.69-82.13 | -3.3% / -4.9% | -1.5% | 49.4M |
| GLD | 381.96 (08:49 sip) | +0.6% | 379.55 | 6.62 (1.7%) | 376.88-406.56 | -3.1% / -4.3% | +0.4% | 8.5M |
| USO | 141.65 (08:49 sip) | -1.6% | 143.99 | 5.79 (4.0%) | 142.07-163.35 | -4.5% / +4.7% | -4.0% | 6.6M |
| SMH | 636.45 (08:49 sip) | +0.4% | 633.90 | 14.53 (2.3%) | 537.73-636.25 | +7.9% / +11.0% | +5.6% | 6.2M |
| XLK | 202.15 (08:49 sip) | +0.6% | 200.93 | 3.04 (1.5%) | 181.87-201.39 | +4.7% / +7.7% | +3.3% | 7.4M |
| XLF | 53.98 (08:49 sip) | +0.2% | 53.88 | 0.76 (1.4%) | 52.81-57.62 | -2.5% / -4.8% | -0.6% | 38.1M |
| XLE | 62.90 (08:45 sip) | -0.9% | 63.45 | 1.23 (1.9%) | 60.95-65.78 | +0.3% / +2.5% | +2.2% | 34.8M |
| XLV | 167.93 (08:00 sip) | +0.3% | 167.37 | 2.25 (1.3%) | 164.48-171.87 | -0.3% / -0.5% | -2.3% | 8.2M |
| XLI | 170.99 (08:45 sip) | +0.5% | 170.10 | 2.30 (1.4%) | 166.18-175.24 | +0.2% / -3.5% | +0.8% | 7.5M |
| XLY | 110.90 (08:30 sip) | +0.4% | 110.42 | 1.49 (1.3%) | 107.99-114.38 | -0.4% / -3.3% | +1.3% | 6.8M |
| XLP | 81.12 (08:45 sip) | +0.1% | 81.04 | 0.88 (1.1%) | 80.10-84.33 | -1.4% / -3.4% | -1.5% | 11.0M |
| XLU | 40.42 (08:49 sip) | +1.1% | 39.97 | 0.55 (1.4%) | 39.03-43.39 | -1.7% / -5.5% | +1.8% | 30.6M |
| XLB | 49.64 (08:25 sip) | +0.3% | 49.50 | 0.79 (1.6%) | 47.81-52.34 | -0.9% / -3.6% | +0.1% | 11.8M |
| XLRE | 40.79 (08:30 sip) | +0.3% | 40.67 | 0.52 (1.3%) | 40.41-43.89 | -3.3% / -6.6% | -1.6% | 6.2M |
| XLC | 111.85 (07:05 sip) | +0.2% | 111.61 | 1.88 (1.7%) | 109.66-115.61 | -0.4% / +0.3% | +0.4% | 6.1M |
| KRE | 70.51 (08:40 sip) | +0.2% | 70.39 | 1.32 (1.9%) | 67.97-74.82 | -1.9% / -4.8% | -0.2% | 15.2M |
| XHB | no trade today | - | 96.30 | 2.18 (2.3%) | 94.08-102.45 | -1.0% / -6.0% | -1.0% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 332.63 (08:49 sip) | -0.1% | 332.89 | 6.49 (1.9%) | 309.90-345.34 | +0.1% / +3.3% | -1.6% | 42.1M |
| MSFT | 530.00 (08:49 sip) | +0.9% | 525.18 | 12.17 (2.3%) | 486.00-532.35 | +4.4% / +7.1% | +3.1% | 21.8M |
| NVDA | 241.05 (08:49 sip) | +0.9% | 238.90 | 5.38 (2.3%) | 208.93-240.10 | +6.6% / +9.2% | +4.4% | 111.0M |
| AMZN | 253.37 (08:49 sip) | +0.8% | 251.40 | 5.23 (2.1%) | 244.30-259.49 | +0.0% / -2.2% | +2.1% | 35.6M |
| GOOGL | 347.38 (08:49 sip) | +0.3% | 346.47 | 9.10 (2.6%) | 327.74-364.17 | +1.0% / +0.5% | +1.1% | 27.7M |
| META | 743.69 (08:49 sip) | +0.2% | 741.90 | 28.69 (3.9%) | 609.26-779.82 | +5.7% / +18.2% | +3.7% | 23.7M |
| TSLA | 381.55 (08:49 sip) | +0.7% | 378.73 | 12.06 (3.2%) | 345.88-386.83 | +3.5% / +8.6% | +6.0% | 37.2M |
| AVGO | 364.78 (08:49 sip) | +0.6% | 362.51 | 9.91 (2.7%) | 335.20-372.02 | +2.4% / -2.6% | +3.7% | 24.5M |
| AMD | 643.47 (08:49 sip) | +1.9% | 631.75 | 24.79 (3.9%) | 480.33-645.46 | +10.0% / +22.5% | +3.9% | 22.4M |
| ORCL | 144.00 (08:49 sip) | +1.1% | 142.48 | 6.30 (4.4%) | 131.58-170.70 | -1.9% / -1.2% | +7.5% | 35.9M |
| NFLX | 67.53 (08:49 sip) | +0.0% | 67.50 | 1.81 (2.7%) | 66.54-81.02 | -7.5% / -10.6% | -2.5% | 35.6M |
| CRM | 231.71 (08:49 sip) | +0.8% | 229.79 | 7.88 (3.4%) | 221.18-261.87 | -4.1% / +3.9% | +1.1% | 11.9M |
| JPM | 332.20 (08:49 sip) | +0.4% | 330.73 | 6.41 (1.9%) | 324.25-358.26 | -3.4% / -5.5% | -1.3% | 8.4M |
| GS | 900.00 (08:49 sip) | +0.7% | 893.46 | 23.17 (2.6%) | 881.00-1,043.84 | -6.2% / -10.5% | -2.5% | 2.2M |
| BAC | 54.38 (08:49 sip) | +0.7% | 54.00 | 1.08 (2.0%) | 52.89-63.83 | -6.3% / -10.8% | -2.7% | 39.3M |
| XOM | 162.47 (08:49 sip) | -0.9% | 164.00 | 3.50 (2.1%) | 155.85-169.64 | +0.6% / +2.3% | +0.9% | 13.9M |
| CVX | 204.60 (08:49 sip) | -0.9% | 206.47 | 4.15 (2.0%) | 200.78-217.78 | -1.0% / +2.1% | +0.0% | 9.9M |
| LLY | 1,148.55 (08:49 sip) | +0.5% | 1,143.12 | 30.97 (2.7%) | 1,113.29-1,215.00 | -0.7% / -2.7% | -3.5% | 2.3M |
| UNH | 379.37 (08:49 sip) | +0.2% | 378.58 | 7.54 (2.0%) | 362.60-404.04 | +0.3% / -3.2% | +0.2% | 5.1M |
| JNJ | 253.20 (08:49 sip) | +0.1% | 252.93 | 4.67 (1.8%) | 252.51-275.23 | -5.1% / -4.6% | -7.0% | 6.9M |
| WMT | 104.85 (08:49 sip) | -0.2% | 105.07 | 2.08 (2.0%) | 103.39-111.23 | -1.8% / -3.3% | -3.4% | 22.3M |
| COST | 921.23 (08:49 sip) | -0.2% | 923.52 | 14.54 (1.6%) | 883.10-931.09 | +1.7% / -1.0% | +0.1% | 2.4M |
| HD | 283.05 (08:49 sip) | +0.7% | 281.15 | 6.43 (2.3%) | 277.15-321.50 | -5.6% / -12.2% | -3.0% | 5.2M |
| CAT | 855.51 (08:49 sip) | +0.9% | 848.14 | 22.26 (2.6%) | 772.86-858.87 | +4.3% / +3.1% | +3.4% | 2.3M |
| BA | 194.10 (08:49 sip) | +0.7% | 192.72 | 7.19 (3.7%) | 184.01-215.29 | -3.2% / -9.1% | +4.5% | 8.6M |
| DAL | 84.08 (08:49 sip) | +1.2% | 83.08 | 2.47 (3.0%) | 76.89-86.17 | +1.9% / -1.1% | -1.1% | 7.5M |
| UAL | 111.60 (08:49 sip) | +1.5% | 110.00 | 4.04 (3.7%) | 104.59-118.26 | -0.2% / -4.9% | -1.4% | 4.0M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-05 19:59 ET - the PREVIOUS session's movers; the screener does not update before the open)

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| MI | 3.46 (08:59 iex) | -50.6% | 7.00 | 0.97 (13.8%) | 0.73-10.42 | +199.0% / +54.0% | +195.4% | 8.4M |
| SAIQ | 5.72 (08:49 sip) | -14.2% | 6.67 | 1.89 (28.4%) | 1.76-12.95 | -28.3% / -34.2% | -37.3% | 3.5M |
| VEEA | 5.06 (08:49 sip) | -11.5% | 5.72 | 1.24 (21.7%) | 1.53-8.88 | +70.3% / +95.9% | +100.0% | 21.0M |
| PTC | 193.36 (08:49 sip) | +0.6% | 192.26 | 7.99 (4.2%) | 126.79-196.05 | +38.1% / +33.8% | +37.6% | 3.1M |
| XP | 28.18 (08:49 sip) | +0.1% | 28.15 | 1.30 (4.6%) | 18.79-29.00 | +35.9% / +51.9% | +39.1% | 10.4M |
| PCVX | 72.50 (08:49 sip) | -1.8% | 73.82 | 4.58 (6.2%) | 55.09-90.75 | +25.1% / +25.3% | +26.7% | 2.2M |
| RXO | 28.65 (08:45 sip) | +0.0% | 28.65 | 1.49 (5.2%) | 18.56-29.11 | +39.3% / +34.8% | +42.2% | 2.9M |
