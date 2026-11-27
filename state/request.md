Produce today's pre-market brief.

You are running unattended. No one will review this before it reaches the account,
so everything below matters more than it would in a conversation:

- **Search before you write anything, in two passes.** Your training data is
  stale by default. First the tape: overnight moves, pre-market gaps, today's
  economic calendar, earnings due today, and news since the previous close.
  Then each candidate: its catalyst at the source, its next earnings date, how
  far it has already moved, its current price. You have about twenty minutes
  and every lookup is logged beside the brief; a candidate you did not check is
  a pass, not a play.
- **Never state a price you have not verified this session.** Any entry more than
  10% from the last traded price is rejected automatically, so a fabricated level
  costs you the trade. If you could not confirm a current price for a symbol,
  leave that play out and say so in the brief.
- **Work from the clock in the book state below.** It gives the current time and
  when the cash session opens. Every release scheduled before that time has
  already printed: look up the actual figure and how futures reacted, and reason
  from it. Only what is still ahead of you is consensus.
- **Look at both sides, and beyond the watchlist.** Name the best long and the
  best short you found, with levels, whether or not you take them. The movers
  table at the end of the book state is where names outside the watchlist come
  from. A view you hold at conviction 1 or 2 is not a trade: give it its levels
  in `passed`, where it is scored against what the tape did at no risk.
- **Leave open positions alone.** Each one's bracket stays as you submitted it
  unless the invalidation you recorded at entry has happened, its own binary
  event is next, or it is in its tenth session. The book state quotes the
  invalidation and counts the sessions. Price being near the stop is not a
  reason to close, and no stop is tightened.
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
- **A change you only describe in prose does not happen.** Closing a position,
  or amending or cancelling a resting entry, must also appear in the `manage`
  array of the JSON block, including on a `no_trade` day. The stops shown in
  the book state below are the live resting orders.

Write the full prose brief as specified, then the JSON block. The prose is the
permanent record of your reasoning and is committed to a public repository, so
write it to be read months from now by someone checking whether your stated
reasoning matched what actually happened. That applies to what you pass on as
much as to what you trade.

Your probability estimates are scored against outcomes, on the bracket as you
submit it. "Your record" in the book state shows how they have held up so far.
Start each estimate from the base rate there and move off it only for reasons
you name: a number chosen to sit just above what the reward:risk needs carries
no information.

## What the record has shown so far

*As of 2026-11-09, 45 closed trades. Merged by the operator from the reviews. The
samples are small: each line is the working assumption, not a settled finding,
and "Your record" in the book state has the current figures.*

- **Managing positions has cost money.** Left alone, the 45 brackets would have
  made about 5R. As managed they made under 2R: moved stops gave up about 2.4R
  over 11 trades and closes by hand about 1.7R over 9. Hence the default of
  leaving the bracket as submitted.
- **Your probabilities have not told good ideas from bad.** Almost all sat
  between 0.30 and 0.47, on average exactly at breakeven for the reward:risk
  stated, and scored no better than saying the base rate every time (about 42%
  of 116 brackets reached target first). Start from the base rate.
- **Small probes did not pay.** Conviction-2 plays averaged -0.15R over 18
  trades and took slots, while the ideas you passed on averaged +0.10R over 80.
  Low-conviction ideas are now scored in the shadow book instead of traded.

## Your last post-open review (2026-11-25)

*For continuity: what you were watching and why. The book state below is
current and overrides anything here.*

# Post-open review: Wednesday 2026-11-25, 10:05 ET (16:05 Stockholm)

**No changes to the book and no new plays.** The QQQ sell stop at 604 stays in place. Its fall-back-to-the-review range was 604–630, and QQQ is at 617.73. The WMT long that this morning flagged for re-scoring met its condition, but it scores about −0.01R, so I'm passing.

### 1. Since the open
- **No new 10:00 ET data.**
  - The final UMich reading came out on Nov 20, not today.
  - CNBC's live post at 10:04 lists no 10:00 release.
  - The 08:30 numbers stand as written this morning (core PCE 3.3% vs 3.2%).
- **The open was as weak as expected, then bounced.**
  - At the open: Nasdaq −3.3%, S&P −2.3% (CNBC).
  - **QQQ** made its low at 607.74, 1.5 points above the 20-day low of 606.23, then bounced to 617.73, near the top of its opening range.
  - **SPY** is 704.10, also near its range high of 704.55.
  - **VIX** is about 33.7–33.9, up from 30.8 pre-market.
- **New single-name information:**
  - **Deere** reported at 06:15 ET. FY27 net income guidance is $4.50–5.25B against about $5.9B consensus (CMeLite, Stocktitan/PRNewswire). The stock fell 3.7% pre-market and opened −4.2%, then reversed to +2.6% on 13.8× normal volume.
  - **HPQ** is +9.6% after printing as high as 32.05.
- **What hasn't changed:** the tariff and Fed backdrop.
  - I couldn't get a fresh CME FedWatch figure for today. An InvestmentNews page that came up turned out to be from Sept 30, so I discarded it.
  - Nothing I found suggests the December hike probability has fallen toward the 60% invalidation.

### 2. Fills, positions and resting entries
- **Open positions:** none.
- **QQQ sell stop at 604 (stop 628.50, target 555): keep.**
  - Last trade 617.73 is inside the 604–630 band the morning set for "leave it resting."
  - The trigger is still below today's low (607.74), so it is still valid at the broker.
  - Neither invalidation has happened: no sign that FedWatch fell below 60%, and no USTR withdrawal of the Section 301 proposal.
  - If it doesn't fill today, the harness clears it before Thursday's holiday.

### 3. The morning's plans
- **QQQ: not triggered, left resting.** QQQ is 617.73. It is not above 630, so the cancel condition wasn't met, and it hasn't broken 604.
- **WMT: condition met, re-scored, passed.**
  - The condition held: SPY is −2.0% (more than −1.5%), and WMT is 132.74, above its old 20-day high of 132.42.
  - **Re-scored bracket:** market 132.74 / stop 127.40 / target 141.00, which is 1.55R. P = 0.39 (the base rate; I found no new reason to move it). Value is 0.39 × 1.55 − 0.61 = **−0.01R**.
  - The catalyst (the Nov 19 earnings) is still six sessions old, and WMT is 12.6% above its 50-day average.
- **Index long: not triggered.** SPY is 704.10, short of the 712 reclaim level, and VIX is about 34, not below 28.

### 4. New plays
None. Every candidate below failed pass 2 or came out at zero or negative expected value.

### 5. Passing on
| Idea | Levels | P | Why I passed |
|---|---|---|---|
| WMT long | Market 132.74 / stop 127.40 / target 141.00 (1.55R) | 0.39 | Re-scored above: about −0.01R, with a stale catalyst and an extended stock. |
| DE long (post-earnings reversal) | Market 629.64 / stop 602.00 / target 685.00 (2.0R) | 0.32 | Details below. |
| HPQ long | Market 30.64 / stop 29.20 / target 33.50 (2.0R) | 0.30 | Details below. |
| AAPL short (tariff catch-down) | Market 350.48 / stop 361.50 / target 328.00 (2.0R) | 0.30 | Details below. |

- **DE long.**
  - The guidance missed badly. Morgan Stanley said it "weakens" their thesis.
  - I couldn't find a source for the reversal. The best guess is that the bad news was already priced in after a 7% drop the week before.
  - It is up 2.3 ATR off its low in 35 minutes, and the market is shut Thursday. A move I can't explain at its source is not a trade.
- **HPQ long.**
  - Sources conflict on the reaction: a 14–17% after-hours spike faded, and the stock is now +9.6% after printing as high as 32.05.
  - Goldman says the guidance midpoint is about −11% year on year on a comparable basis.
  - It is already 2.5 ATR up today, so buying now would be chasing.
- **AAPL short.**
  - Section 301 covers China and India, but I found no dated source tying it to Apple today.
  - AAPL is acting as a mega-cap haven (−1.0%).
  - The catalyst is unverified.
- **Not given levels:**
  - **DAL and UAL** (−5%): I couldn't find a dated source for today's oil move (USO +2.9%).
  - **Semi shorts** (LRCX, AMAT, MU, AVGO): already −4% to −9% with ATRs of 8–12%, so a short now chases the move.

### 6. For tomorrow (Friday 11-27, half day, 13:00 ET / 19:00 Stockholm close)
- **QQQ:**
  - If the 604 trigger didn't fill, it has been cleared.
  - If QQQ opens Friday still above 606.23, a new breakdown trigger can go in below that day's low.
  - If it gapped below 606, don't chase. Only a bounce limit in the 625–630 area, stop above 650, is worth scoring.
- **DE:** consider it only if it holds above 613.76 (Wednesday's prior close) into Friday, and only once there is a dated analyst source explaining today's reversal.
- **WMT:** consider a long only on a pullback limit near 129.50 (the 132.42 breakout zone minus 1 ATR), not up here.

```json
{
  "date": "2026-11-25",
  "no_trade": true,
  "session_note": "Post-open: AI unwind continuing (Nasdaq -3.1%, VIX ~34) but QQQ bounced off 607.74 to 617.73, so the 604 breakdown trigger stays as planned. WMT met its re-score condition but is ~-0.01R; DE's reversal after a guide miss is unexplained at source; no new plays. I would act on a QQQ break of 606.23 (order resting) or a WMT pullback toward 129.50.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "WMT",
      "direction": "long",
      "entry_type": "market",
      "entry": 132.74,
      "stop": 127.40,
      "targets": [141.00],
      "p_target_first": 0.39,
      "reason": "Morning's review condition met (SPY -2.0%, WMT > 132.42) but re-scored at 1.55R with P at the 39% base rate gives about -0.01R; catalyst six sessions old, +12.6% vs 50-day average."
    },
    {
      "ticker": "DE",
      "direction": "long",
      "entry_type": "market",
      "entry": 629.64,
      "stop": 602.00,
      "targets": [685.00],
      "p_target_first": 0.32,
      "reason": "Reversed from -4.2% to +2.6% on 13.8x volume after FY27 net income guidance of $4.50-5.25B vs about $5.9B consensus; no source for the reversal, 2.3 ATR off the low in 35 minutes, holiday gap ahead. EV about -0.04R."
    },
    {
      "ticker": "HPQ",
      "direction": "long",
      "entry_type": "market",
      "entry": 30.64,
      "stop": 29.20,
      "targets": [33.50],
      "p_target_first": 0.30,
      "reason": "+9.6% after a choppy post-earnings path (14-17% after-hours spike, faded, re-rallied to 32.05); Goldman says the FY27 guide midpoint is about -11% y/y on a comparable basis; already 2.5 ATR up today, so this would be a chase."
    },
    {
      "ticker": "AAPL",
      "direction": "short",
      "entry_type": "market",
      "entry": 350.48,
      "stop": 361.50,
      "targets": [328.00],
      "p_target_first": 0.30,
      "reason": "Laggard catch-down idea on the Section 301 tariffs (China, India), but no dated source ties them to Apple today, and AAPL is trading as a mega-cap haven (-1.0%). Catalyst unverified."
    }
  ]
}
```

Sources:
- [CNBC live updates, Nov 25 (10:04 ET update: indices, VIX)](https://cnbc.com/2026/11/24/stock-market-today-live-updates-.html)
- [Stocktitan / PRNewswire: Deere Q4 FY26 release, 06:15 ET](https://www.stocktitan.net/news/DE/deere-reports-net-income-of-1-051-billion-for-fourth-quarter-4-860-o8y609mffx35.html)
- [CMeLite: Deere FY27 guidance vs consensus, Morgan Stanley comment](https://www.cmelitegroup.com/trends-and-insights/deere-shares-slide-as-fiscal-2027-guidance-falls-short-leaving-investors-asking-whether-it-is-realistic-or-conservative/)
- [MLQ: Deere FY27 outlook](https://mlq.ai/news/deere-forecasts-fiscal-2027-net-income-of-450-billion-to-525-billion-as-north-american-large-ag-demand-starts-to-improve/)
- [Blockonomi: DE slips pre-market](https://blockonomi.com/deere-de-stock-slips-as-large-ag-slump-offsets-revenue-beat-and-2027-guidance)
- [Invezz: HP popped after earnings, pared gains](https://invezz.com/news/2026/11/25/hp-stock-popped-after-earnings-beat-why-it-has-pared-gains-in-premarket/)
- [Pomegra: HPQ rally fades on FY2027 outlook](https://pomegra.io/news/hp-inc-hpq-q4-2026-14-rally-fades-on-fy2027-outlook)
- [Startup Fortune: HP FY27 forecast vs estimates](https://startupfortune.com/hp-inc-forecasts-fiscal-2027-profit-above-wall-streets-estimate-as-memory-costs-ease/)
- [Yahoo Finance: Nvidia, AMD, Micron sink as investors flee AI trade (Nov 25)](https://finance.yahoo.com/markets/article/nvidia-amd-micron-stocks-sink-as-investors-flee-ai-trade-134518921.html)
- [Stockanalysis: UMich November prelim (final was Nov 20)](https://stockanalysis.com/news/consumer-sentiment-rises-november-2026/)
- [InvestmentNews (dated Sept 30, 2026; stale and discarded)](https://www.investmentnews.com/equities/pce-data-cools-but-further-rate-hikes-loom/268415)
- [MarketScreener: WMT on track for record close](https://ca.marketscreener.com/quote/stock/WALMART-INC-4841/news/Walmart-on-Track-for-Record-High-Close-Data-Talk-30917318/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Friday 2026-11-27. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 13:00 ET (19:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,973.84**
- Cash: $102,973.84
- Session P&L so far: +0.00% (new entries are blocked at -3.0%)
- Gross exposure: $0 (0% of equity, cap 150%)
- Net exposure: $+0 (+0%, cap +/-100%)
- Risk at stake (entry to stop): $0 (0.00% of equity, cap 4.0%) — 4.00% left for new plays
- Slots: 0 open + 0 resting entries of 8 — you may add at most 8 more
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

*No open positions.*

### Your record

53 closed trades: 17W / 36L, total +1.50R, net $+2,991 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 53 | 19 | 31 | +0.03R |
| The same trades, bracket left alone | 53 | | | +0.05R |
| Ideas you passed on, or the caps dropped | 135 | 48 | 76 | +0.05R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 53 | 47% |
| 35%-40% | 87 | 30% |
| 40%-45% | 27 | 48% |
| 45%-50% | 5 | 20% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 174 brackets reached target first. Your Brier score is 0.240; saying 39% every time scores 0.237. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| HD | short | stop | -1.01R | $-516 | 36% |
| GLD | short | target | +2.15R | $+1,097 | 36% |
| LOW | short | stop | -0.67R | $-343 | 37% |
| IWM | short | target | +1.67R | $+853 | 36% |
| AMZN | long | stop | -1.20R | $-303 | 36% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 728.07 (08:49 sip) | +1.6% | 716.70 | 16.88 (2.4%) | 686.75-775.64 | -3.2% / -5.4% | -1.8% | 65.2M |
| QQQ | 648.44 (08:49 sip) | +2.3% | 633.93 | 23.32 (3.7%) | 606.23-718.07 | -4.9% / -10.3% | -3.9% | 63.9M |
| IWM | 272.57 (08:49 sip) | +1.4% | 268.87 | 6.23 (2.3%) | 256.32-286.17 | -2.0% / -3.0% | -0.5% | 28.4M |
| DIA | 508.08 (08:49 sip) | +1.4% | 501.27 | 9.56 (1.9%) | 479.40-536.00 | -2.0% / -2.6% | +0.0% | 4.3M |
| TLT | 81.81 (08:49 sip) | -0.5% | 82.24 | 0.80 (1.0%) | 79.11-82.81 | +1.5% / +3.0% | +2.5% | 39.2M |
| GLD | 334.15 (08:49 sip) | +2.0% | 327.45 | 8.87 (2.7%) | 313.96-380.18 | -7.5% / -11.7% | -4.0% | 11.2M |
| USO | 140.49 (08:49 sip) | +0.4% | 139.89 | 4.76 (3.4%) | 132.28-171.82 | -4.0% / -7.0% | +2.8% | 4.6M |
| SMH | 439.04 (08:50 iex) | +3.9% | 422.46 | 32.34 (7.7%) | 393.88-565.87 | -11.4% / -21.9% | -8.1% | 13.8M |
| XLK | 159.98 (08:49 sip) | +2.7% | 155.79 | 7.64 (4.9%) | 148.09-189.34 | -7.2% / -14.8% | -4.9% | 17.1M |
| XLF | 57.10 (08:45 sip) | +1.0% | 56.51 | 1.02 (1.8%) | 54.42-60.04 | -1.2% / +1.2% | +0.2% | 42.6M |
| XLE | 61.71 (08:49 sip) | +1.3% | 60.90 | 1.40 (2.3%) | 59.55-70.15 | -3.9% / -5.5% | -0.6% | 37.0M |
| XLV | 183.75 (08:49 sip) | +0.0% | 183.68 | 3.62 (2.0%) | 176.71-192.32 | -0.6% / +3.6% | +1.4% | 13.9M |
| XLI | 165.40 (08:20 sip) | +1.5% | 162.95 | 3.98 (2.4%) | 155.70-172.40 | -1.8% / -2.7% | -1.0% | 9.7M |
| XLY | 119.24 (08:25 sip) | +1.5% | 117.49 | 2.90 (2.5%) | 112.03-122.92 | -0.6% / +2.6% | -1.4% | 10.1M |
| XLP | 92.05 (08:49 sip) | -0.3% | 92.30 | 1.45 (1.6%) | 87.39-93.48 | +1.6% / +6.3% | +1.2% | 22.5M |
| XLU | 43.99 (08:49 sip) | +0.9% | 43.61 | 0.60 (1.4%) | 42.63-44.40 | +0.3% / +3.7% | +0.1% | 26.2M |
| XLB | 51.93 (08:40 sip) | +1.4% | 51.21 | 1.12 (2.2%) | 48.21-54.63 | -1.0% / +0.9% | +1.5% | 13.3M |
| XLRE | 43.92 (07:25 sip) | +0.1% | 43.86 | 0.68 (1.6%) | 42.40-45.34 | +0.1% / +3.0% | +0.6% | 7.9M |
| XLC | 107.12 (08:40 sip) | +1.7% | 105.38 | 2.59 (2.5%) | 99.33-109.26 | +0.8% / -2.5% | -0.2% | 8.2M |
| KRE | 70.39 (08:20 sip) | +0.8% | 69.83 | 1.31 (1.9%) | 68.14-75.80 | -2.7% / -1.8% | -1.0% | 15.8M |
| XHB | 104.26 (08:10 sip) | +0.6% | 103.67 | 3.08 (3.0%) | 96.34-108.78 | +1.7% / +5.1% | +2.9% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 358.71 (08:54 iex) | +0.9% | 355.58 | 8.03 (2.3%) | 325.08-360.83 | +2.0% / +3.7% | +0.9% | 51.7M |
| MSFT | 499.16 (08:49 sip) | +1.9% | 489.93 | 17.04 (3.5%) | 477.39-558.07 | -5.1% / -5.5% | -3.4% | 30.9M |
| NVDA | 152.75 (09:01 iex) | +2.3% | 149.30 | 15.83 (10.6%) | 124.50-215.33 | -13.4% / -26.7% | -1.1% | 351.8M |
| AMZN | 250.52 (09:05 iex) | +2.5% | 244.43 | 10.46 (4.3%) | 229.36-275.34 | -5.0% / -4.2% | -8.7% | 55.4M |
| GOOGL | 280.23 (08:49 sip) | +2.6% | 273.10 | 11.63 (4.3%) | 262.73-304.97 | -3.5% / -14.2% | -3.3% | 45.7M |
| META | 629.81 (08:49 sip) | +3.3% | 609.89 | 24.31 (4.0%) | 558.68-648.45 | -0.9% / -9.3% | -1.1% | 18.3M |
| TSLA | 390.30 (08:49 sip) | +2.7% | 380.14 | 20.05 (5.3%) | 338.15-414.23 | -0.5% / +0.8% | -0.9% | 35.8M |
| AVGO | 310.98 (08:57 iex) | +3.4% | 300.86 | 23.14 (7.7%) | 278.00-369.82 | -8.0% / -11.6% | -15.0% | 32.4M |
| AMD | 423.35 (08:49 sip) | +4.3% | 406.03 | 52.47 (12.9%) | 370.40-594.00 | -17.0% / -26.0% | -23.4% | 47.2M |
| ORCL | 107.84 (08:49 sip) | +3.8% | 103.88 | 8.32 (8.0%) | 99.34-144.61 | -12.6% / -20.1% | -8.8% | 40.6M |
| NFLX | 60.21 (08:49 sip) | +1.3% | 59.41 | 1.94 (3.3%) | 56.56-67.49 | -3.7% / -10.3% | -0.7% | 40.5M |
| CRM | 197.38 (08:49 sip) | +0.1% | 197.21 | 8.67 (4.4%) | 179.91-234.62 | -5.9% / -12.7% | +3.6% | 7.4M |
| JPM | 322.88 (08:49 sip) | +1.9% | 316.74 | 7.73 (2.4%) | 309.18-359.80 | -5.1% / -5.4% | -2.3% | 7.4M |
| GS | 822.25 (08:49 sip) | +2.6% | 801.03 | 31.80 (4.0%) | 772.74-939.38 | -8.8% / -10.5% | -8.3% | 2.5M |
| BAC | 49.37 (08:40 sip) | +1.7% | 48.54 | 1.14 (2.4%) | 46.88-53.02 | -2.3% / -6.8% | -0.8% | 36.8M |
| XOM | 160.14 (08:45 sip) | +1.3% | 158.08 | 3.48 (2.2%) | 156.67-187.32 | -5.3% / -5.9% | -1.6% | 15.5M |
| CVX | 213.29 (08:45 sip) | +1.1% | 210.95 | 4.36 (2.1%) | 204.31-234.53 | -1.6% / -1.2% | +2.5% | 8.7M |
| LLY | 1,386.82 (08:49 sip) | -0.4% | 1,392.22 | 40.02 (2.9%) | 1,328.39-1,475.25 | -0.5% / +8.7% | +0.7% | 3.3M |
| UNH | 348.55 (08:49 sip) | +0.7% | 346.19 | 15.91 (4.6%) | 319.13-416.11 | -9.9% / -10.4% | -1.1% | 7.6M |
| JNJ | 274.17 (08:49 sip) | +0.1% | 273.94 | 6.46 (2.4%) | 263.37-288.81 | -0.2% / +2.8% | +1.0% | 8.3M |
| WMT | 132.00 (08:49 sip) | +0.0% | 131.94 | 2.81 (2.1%) | 119.66-133.19 | +3.8% / +11.8% | +3.6% | 25.0M |
| COST | 1,086.03 (08:49 sip) | -0.1% | 1,086.81 | 17.93 (1.6%) | 956.23-1,098.00 | +3.9% / +11.9% | +1.9% | 2.7M |
| HD | 363.52 (08:49 sip) | +0.6% | 361.26 | 9.45 (2.6%) | 322.68-363.65 | +4.8% / +13.7% | +7.0% | 5.4M |
| CAT | 560.69 (08:45 sip) | +3.1% | 543.69 | 28.98 (5.3%) | 508.11-664.47 | -6.1% / -22.2% | -2.7% | 4.3M |
| BA | 167.98 (08:49 sip) | +2.1% | 164.53 | 5.23 (3.2%) | 155.56-179.19 | -2.6% / -9.3% | +1.0% | 8.0M |
| DAL | 84.31 (08:45 sip) | +1.6% | 82.95 | 3.10 (3.7%) | 78.66-92.52 | -2.9% / +0.4% | -2.3% | 5.9M |
| UAL | 106.53 (08:49 sip) | +1.9% | 104.52 | 5.09 (4.9%) | 100.28-122.08 | -4.9% / -3.1% | -2.9% | 5.5M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| NU | 13.82 (08:49 sip) | +11.8% | 12.36 | 0.61 (5.0%) | 11.21-13.25 | +2.7% / -7.3% | +2.3% | 70.6M |
| SNDK | 80.94 (09:04 iex) | +10.0% | 73.61 | 12.56 (17.1%) | 67.02-173.23 | -33.1% / -54.4% | -24.1% | 116.1M |
| STX | 502.77 (08:49 sip) | +6.4% | 472.33 | 49.81 (10.5%) | 432.04-718.65 | -11.2% / -31.2% | -8.4% | 5.4M |
| WDC | 289.82 (08:49 sip) | +6.4% | 272.45 | 27.15 (10.0%) | 244.77-402.23 | -10.0% / -25.4% | -5.5% | 7.9M |
| MRVL | 138.95 (08:49 sip) | +6.1% | 130.93 | 15.27 (11.7%) | 117.80-225.68 | -15.5% / -39.1% | -10.0% | 35.3M |
| ARM | 171.26 (09:02 iex) | +6.0% | 161.51 | 17.63 (10.9%) | 143.55-231.99 | -12.7% / -31.3% | -11.6% | 6.7M |
| MU | 636.53 (09:05 iex) | +5.9% | 601.25 | 70.99 (11.8%) | 548.13-971.01 | -19.1% / -32.9% | -14.7% | 37.1M |
| TER | 224.58 (08:49 sip) | +5.9% | 212.15 | 23.09 (10.9%) | 190.91-304.59 | -12.4% / -33.9% | -9.7% | 4.5M |
| VRTX | 518.31 (08:49 sip) | -8.1% | 564.12 | 15.75 (2.8%) | 513.80-571.75 | +3.9% / +7.4% | +5.2% | 1.6M |
| MO | 74.35 (08:49 sip) | -2.5% | 76.28 | 1.65 (2.2%) | 73.12-79.97 | -0.5% / +4.1% | +0.0% | 8.9M |
| PANW | 347.43 (08:49 sip) | -2.4% | 356.14 | 19.84 (5.6%) | 301.28-390.00 | +4.8% / -2.7% | +4.8% | 8.2M |
| AZN | 181.95 (08:40 sip) | -1.2% | 184.21 | 3.85 (2.1%) | 172.87-192.65 | +0.6% / +7.2% | +3.0% | 2.7M |
| EL | 108.76 (07:20 sip) | -0.8% | 109.61 | 4.24 (3.9%) | 99.22-115.28 | +1.5% / +6.6% | +5.4% | 4.1M |
| NVO | 40.66 (08:49 sip) | -0.8% | 40.97 | 1.22 (3.0%) | 37.75-43.24 | +1.6% / +3.9% | +3.9% | 13.7M |
| TRV | 404.01 (07:40 sip) | -0.7% | 406.86 | 8.57 (2.1%) | 385.68-418.00 | +2.0% / +5.7% | +3.9% | 1.5M |
| HSY | 181.30 (07:05 sip) | -0.7% | 182.57 | 5.57 (3.1%) | 158.55-183.98 | +5.7% / +9.0% | +3.8% | 2.2M |
