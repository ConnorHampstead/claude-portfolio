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

## Your last post-open review (2026-11-24)

*For continuity: what you were watching and why. The book state below is
current and overrides anything here.*

# Post-open review: Tuesday 2026-11-24, 10:05 ET (16:05 Stockholm, ET+6)

**No new trades, and HD is held.** Consumer confidence beat forecasts by about 11 points, but BBY fell back below its open, so the morning's BBY entry didn't trigger. Nothing else that moved has a catalyst and a positive expected value on my numbers.

### 1. Since the open

**Consumer confidence was a big upside surprise.** The Conference Board released it at 10:00 ET (16:00 Stockholm):

| | November | October | Consensus |
|---|---|---|---|
| Headline | **103.3** | 91.9 (revised; previews had 91.7) | 92.1–92.5 |
| Present situation | 132.8 | — | — |
| Expectations | 83.6 | — | — |
| 12-month inflation expectations | 5.7% | — | — |

- Planned durable-goods spending rose.
- The only source is the Conference Board's own release on PR Newswire. That is the primary source, but secondary coverage hasn't caught up yet.

**The tape is a rotation, not a broad selloff:**
- **Tech is down:** SMH −6.2%, AMD −8.4%, MU −8.5%, NVDA −6.3% to 154.59. That puts NVDA below Monday's 156.93 low, so the morning's shadow NVDA sell stop at 154.90 would have filled.
- **Most other sectors are up:** XLV +2.3%, XLP +1.7%, DIA +0.6%, IWM +0.6%.
- **The indexes are recovering:** SPY is at 719.65, up from a 715.18 open and near its high. QQQ is at 640.57, inside the morning's 630–645 band.

**What changed versus the morning:**
- The breadth is better than the brief assumed, which weakens the case for an index short.
- ADI has fallen further: −15.8% to 319.00, against 339.03 pre-market.
- Nothing new has come out on the WSJ tariff report. I found no USTR release.

### 2. Fills, positions and resting entries

**HD short (343.57 / stop 353.50 / target 323.50): hold, session 6 of 10.**
- **Invalidation (a close above 347.51): not met.** HD is at 348.34, above 347.51 during the session, but the test is the close, and the session closes at 16:00 ET.
- **No HD news today.** The CEO change took effect Nov 23 but was announced Nov 17 and is already priced. HD has no binary event before tomorrow, and it is not in its tenth session.
- **The bracket stands.** The confidence beat is a headwind for this short, but it isn't the recorded invalidation. The stop is 0.5 ATR above the price and may fire today; that is its job.

**Resting entries:** none. **Fills since the morning:** none.

### 3. The morning's plans

- **BBY long (needed ≥101.00, above its open, and confidence ≥92.4): not triggered, dropped.** Confidence passed easily, but BBY is at 98.23, below its 99.22 open and the 101 trigger. That is also under 99, the level where the morning said to do nothing. The stock faded after a beat on both the company's results and the macro print, so the tariff worry is setting the price.
- **QQQ: no short in the review, as planned.** At 640.57 it is neither above 645 (gap failure off) nor below 630.
- **NVDA: nothing, as planned.** The 143–147 level carries over to tomorrow.
- **ADI: nothing, as planned.** It is down another 5 points into the call and is now 2.5 ATR down on the day.

### 4. New plays

None. What I checked:
- **PINS (+12.8%):** TheFly reports that Pinterest amended the change-in-control terms of its equity plan, and announced a Microsoft Advertising tie-up. Both items come second-hand through a news aggregator, and the move is takeover speculation 2.7 ATR in.
- **TXN, MPWR and ENTG:** these fell in sympathy with ADI's in-line guide during a chip rout. I found no news of their own.
- **HUM, LLY and the healthcare names:** they are rising with the rotation. I found no dated catalyst for any of them today.
- **Shorting semis:** already a full ATR down on the day, so it would be a chase.

### 5. Passing on

- **BBY long** at 98.23 market, stop 94.40, target 110.00, about 3.1R. I put P at 0.25: a 3R bracket starts near 0.25 on a random walk, and the fade below the open after a confidence beat keeps it there. EV is about +0.02. The morning's conditions are not met. Logged.
- **ADI long** at 319.00 market, stop 295.00 (1 ATR), target 346.00 (Friday's close, about 345.92), 1.1R. P 0.38, EV about −0.19. This is buying against the trend in the middle of a chip rout. The guide was in line and Cantor raised its target, but there's no reversal sign. Logged.
- **TXN long** at 266.83 market, stop 248.50 (1 ATR), target 291.00 (yesterday's close), 1.3R. P 0.37, EV about −0.14. It is a sympathy drop down near its 262.29 20-day low, with no news of its own. I didn't look up its earnings date, and the levels are for scoring only. Logged.
- **PINS long:** no levels. It is speculation on a plan amendment, it has already moved 2.7 ATR, and the only source is a news aggregator's write-up.
- **DLTR (153.09, +10.1%):** now 2.3 ATR up and above its 20-day high. The morning's reasons for passing still apply, and more strongly.

### 6. For tomorrow

Wednesday's PCE and Q3 GDP come out at 08:30 ET (14:30 Stockholm), before the brief.
- **HD:** if today closes above 347.51, close the position at tomorrow's open. That is the recorded invalidation, condition 1. If it closes at or below 347.51, hold the bracket.
- **QQQ:** if today closes below 630 and PCE is hot, consider a short with the stop above 657.50 and the target at 606.50. Today's breadth argues against it unless both conditions hold.
- **NVDA:** a print in the 143–147 zone that holds 140 is a long at the 0.5 tier.
- **BBY:** only if it closes back above 100.73 (today's high) after PCE, with the same 94.40 stop and 110 target. Below that, the tariff report is setting the price.
- **Timing:** resting entries are cleared before Thursday's holiday, so anything placed Wednesday must fill that day or Friday.

**Book once orders fill (none today):** gross 17% (cap 150%), net −17% (cap ±100%), consumer discretionary −17% (cap 40%). Risk at stake 0.49% (cap 4%), 1 of 8 slots used.

```json
{
  "date": "2026-11-24",
  "no_trade": true,
  "session_note": "Rotation tape: semis -6% (SMH, NVDA below Monday's low) while breadth improves (DIA/IWM +0.6%, XLV +2.3%) after a big consumer confidence beat (103.3 vs ~92.3). The morning's BBY trigger failed: 98.23 is below its 99.22 open and the 101 condition. No new idea clears positive EV with a verified catalyst. Would act: HD close if today closes >347.51; QQQ short on a close <630 plus a hot PCE; NVDA long at 0.5 in 143-147 holding 140; BBY only on a close >100.73.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "BBY",
      "direction": "long",
      "entry_type": "market",
      "entry": 98.23,
      "stop": 94.40,
      "targets": [110.00],
      "p_target_first": 0.25,
      "reason": "Morning review condition not met: 98.23 (10:04) below the 99.22 open and the 101 trigger despite consumer confidence at 103.3. The fade after a beat on both the results and the macro print says tariff risk is setting the price. A 3.1R bracket with the stop 0.9 ATR away; EV about +0.02."
    },
    {
      "ticker": "ADI",
      "direction": "long",
      "entry_type": "market",
      "entry": 319.00,
      "stop": 295.00,
      "targets": [346.00],
      "p_target_first": 0.38,
      "reason": "Counter-trend after -15.8% (2.5 ATR) on an in-line Q1 guide; now about 8% below Friday's ~345.92 pre-rally close. Cantor raised its target, but a chip-sector rout is underway (SMH -6.2%) and there's no reversal signal. 1.1R, EV about -0.19."
    },
    {
      "ticker": "TXN",
      "direction": "long",
      "entry_type": "market",
      "entry": 266.83,
      "stop": 248.50,
      "targets": [291.00],
      "p_target_first": 0.37,
      "reason": "Sympathy drop of 8.4% on ADI's guide and the chip rout, with no news of its own found. Near its 262.29 20-day low. Earnings date not looked up (shadow only). 1.3R, EV about -0.14."
    }
  ]
}
```

Sources:
- [Conference Board via PR Newswire: US Consumer Confidence Surged in November](https://www.prnewswire.com/news-releases/us-consumer-confidence-surged-in-november-302949447.html)
- [Yahoo Finance live blog, Nov 24](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-november-24-dow-sp-500-nasdaq-rebound-090614276.html)
- [Investing.com: CB Consumer Confidence preview](https://in.investing.com/news/stock-market-news/cb-consumer-confidence-highlights-economic-data-due-tuesday-93CH-5721796)
- [StockAnalysis: BBY quote](https://stockanalysis.com/stocks/bby/)
- [TipRanks: Best Buy comps +6.1%, holiday guide](https://www.tipranks.com/news/best-buys-bby-comparable-sales-jump-6-1-ahead-of-black-friday-whats-next-for-holiday-spending)
- [CNBC: Best Buy Q3 FY27](https://www.cnbc.com/2026/11/24/best-buy-bby-q3-2027-earnings.html)
- [TradingView/StockStory: Why are Best Buy shares soaring](https://www.tradingview.com/news/stockstory:4637c8861094b:0-why-are-best-buy-shares-soaring-today/)
- [Seeking Alpha: ADI slides after in-line Q1 outlook](https://seekingalpha.com/news/4676118-analog-devices-shares-slide-after-its-inline-q1-outlook?feed_item_type=news)
- [Benzinga: ADI analyst forecasts](https://www.benzinga.com/analyst-stock-ratings/price-target/26/11/63525866/analog-devices-to-rally-over-66-here-are-10-top-analyst-forecasts-for-monday)
- [StockAnalysis: PINS quote and news](https://stockanalysis.com/stocks/pins/)
- [Home Depot IR: McPhail named CEO effective Nov 23](https://ir.homedepot.com/news-releases/2026/11-17-2026-104320345)
- [TT News: Home Depot names McPhail CEO](https://www.ttnews.com/articles/home-depot-mcphail-ceo)
- [StockAnalysis: HD](https://stockanalysis.com/stocks/hd/)
- [Wiley: Section 301 forced-labor tariffs (background)](https://www.wiley.law/alert-New-Forced-Labor-Tariffs-Imposed-on-60-US-Trading-Partners)
- [Quiver Quant: Humana / Medicare Advantage sentiment (undated)](https://www.quiverquant.com/news/Humana+Rises+as+Medicare+Advantage+Sentiment+Improves)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Wednesday 2026-11-25. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
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
| Ideas you passed on, or the caps dropped | 127 | 45 | 72 | +0.04R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 50 | 48% |
| 35%-40% | 84 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 5 | 20% |
| 50%-60% | 1 | 100% |

Base rate: 38% of 167 brackets reached target first. Your Brier score is 0.239; saying 38% every time scores 0.236. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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
| SPY | 704.39 (08:49 sip) | -2.0% | 718.78 | 17.65 (2.5%) | 686.75-775.64 | -3.3% / -5.2% | -1.9% | 63.0M |
| QQQ | 616.98 (09:04 iex) | -3.3% | 638.10 | 24.36 (3.8%) | 606.23-726.14 | -4.9% / -9.9% | -2.9% | 61.3M |
| IWM | 263.72 (08:49 sip) | -1.3% | 267.14 | 6.61 (2.5%) | 256.32-286.17 | -2.9% / -3.7% | -0.7% | 27.6M |
| DIA | 493.20 (08:49 sip) | -1.3% | 499.74 | 10.11 (2.0%) | 479.40-536.00 | -2.6% / -2.9% | -1.4% | 4.2M |
| TLT | 82.27 (09:03 iex) | +1.0% | 81.49 | 0.75 (0.9%) | 79.11-82.42 | +0.7% / +2.1% | +2.4% | 38.5M |
| GLD | 318.08 (08:57 iex) | -2.3% | 325.45 | 8.28 (2.5%) | 320.95-380.18 | -8.7% / -12.6% | -7.7% | 10.8M |
| USO | 137.32 (08:49 sip) | +1.4% | 135.43 | 4.69 (3.5%) | 132.28-171.82 | -7.9% / -10.1% | -3.4% | 4.8M |
| SMH | 405.00 (08:49 sip) | -5.1% | 426.75 | 34.19 (8.0%) | 396.85-571.00 | -11.8% / -21.5% | -7.2% | 13.4M |
| XLK | 151.20 (08:49 sip) | -3.7% | 157.09 | 8.05 (5.1%) | 148.09-191.55 | -7.4% / -14.4% | -3.8% | 16.5M |
| XLF | 55.70 (08:49 sip) | -0.7% | 56.11 | 1.11 (2.0%) | 54.42-60.04 | -1.9% / +0.5% | -1.7% | 42.0M |
| XLE | 60.17 (08:49 sip) | -0.5% | 60.45 | 1.49 (2.5%) | 59.55-70.15 | -5.2% / -6.2% | -4.6% | 37.1M |
| XLV | 184.42 (08:49 sip) | -0.2% | 184.72 | 3.90 (2.1%) | 176.71-192.32 | +0.0% / +4.3% | -0.3% | 13.6M |
| XLI | 158.91 (08:45 sip) | -1.7% | 161.61 | 4.07 (2.5%) | 155.70-172.40 | -2.8% / -3.6% | -1.9% | 9.5M |
| XLY | 115.90 (08:49 sip) | -1.5% | 117.72 | 3.04 (2.6%) | 112.03-122.92 | -0.3% / +2.9% | +0.5% | 10.0M |
| XLP | 92.36 (08:49 sip) | +0.5% | 91.88 | 1.53 (1.7%) | 86.36-93.48 | +1.4% / +6.0% | +0.5% | 22.0M |
| XLU | 43.40 (08:49 sip) | +0.0% | 43.40 | 0.64 (1.5%) | 42.42-44.40 | -0.1% / +3.3% | -0.0% | 26.0M |
| XLB | 49.60 (08:35 sip) | -1.1% | 50.17 | 1.17 (2.3%) | 48.21-54.63 | -3.1% / -1.1% | -1.3% | 13.1M |
| XLRE | 43.42 (08:35 sip) | -0.1% | 43.46 | 0.70 (1.6%) | 41.78-45.34 | -0.6% / +2.1% | -0.3% | 7.9M |
| XLC | 102.29 (08:25 sip) | -2.1% | 104.45 | 2.60 (2.5%) | 99.33-109.26 | +0.0% / -3.5% | -0.8% | 8.3M |
| KRE | 69.25 (08:49 sip) | -0.7% | 69.76 | 1.50 (2.1%) | 68.14-75.80 | -2.9% / -1.9% | -1.5% | 15.6M |
| XHB | 101.01 (05:10 sip) | -0.3% | 101.28 | 3.12 (3.1%) | 96.34-108.78 | -0.3% / +2.8% | +2.2% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 351.29 (08:49 sip) | -0.8% | 354.07 | 8.15 (2.3%) | 325.08-360.83 | +1.8% / +3.4% | +0.6% | 50.8M |
| MSFT | 481.70 (08:58 iex) | -2.9% | 496.13 | 17.47 (3.5%) | 481.03-558.07 | -4.3% / -4.3% | -1.8% | 31.0M |
| NVDA | 145.26 (09:03 iex) | -6.5% | 155.38 | 16.15 (10.4%) | 124.50-219.99 | -11.6% / -24.2% | -0.1% | 338.1M |
| AMZN | 243.25 (09:04 iex) | -3.6% | 252.29 | 10.79 (4.3%) | 229.36-275.34 | -2.1% / -1.1% | -2.2% | 54.1M |
| GOOGL | 264.67 (09:03 iex) | -5.2% | 279.05 | 11.78 (4.2%) | 264.22-326.40 | -2.3% / -12.7% | -0.4% | 46.8M |
| META | 576.50 (08:49 sip) | -2.3% | 589.82 | 24.88 (4.2%) | 558.68-648.45 | -4.2% / -12.4% | -4.7% | 19.2M |
| TSLA | 370.50 (08:59 iex) | -3.7% | 384.68 | 21.48 (5.6%) | 338.15-414.23 | +0.3% / +2.1% | +1.2% | 35.9M |
| AVGO | 286.30 (09:04 iex) | -4.9% | 301.08 | 24.00 (8.0%) | 289.77-369.82 | -8.6% / -11.8% | -11.9% | 31.8M |
| AMD | 383.52 (08:59 iex) | -7.2% | 413.27 | 55.60 (13.5%) | 396.01-594.00 | -17.0% / -24.9% | -17.9% | 45.5M |
| ORCL | 102.51 (08:59 iex) | -6.4% | 109.50 | 8.49 (7.8%) | 100.25-148.48 | -9.4% / -16.2% | -4.8% | 42.8M |
| NFLX | 58.03 (08:49 sip) | -1.4% | 58.87 | 1.96 (3.3%) | 56.56-67.49 | -4.8% / -11.6% | -1.4% | 40.3M |
| CRM | 189.02 (08:45 sip) | -2.2% | 193.26 | 8.52 (4.4%) | 179.91-244.64 | -8.8% / -14.8% | -0.6% | 7.4M |
| JPM | 313.00 (08:49 sip) | -1.3% | 317.10 | 8.80 (2.8%) | 309.18-359.80 | -5.3% / -5.5% | -3.9% | 7.3M |
| GS | 789.85 (08:49 sip) | -2.0% | 806.02 | 35.09 (4.4%) | 786.66-939.38 | -8.9% / -10.2% | -8.1% | 2.4M |
| BAC | 47.86 (08:49 sip) | -1.4% | 48.56 | 1.25 (2.6%) | 46.88-53.02 | -2.5% / -7.1% | -1.8% | 36.2M |
| XOM | 158.64 (08:49 sip) | +0.3% | 158.23 | 3.88 (2.5%) | 156.67-187.32 | -5.8% / -5.8% | -5.4% | 15.1M |
| CVX | 208.98 (08:45 sip) | +0.1% | 208.73 | 4.72 (2.3%) | 204.31-234.53 | -3.0% / -2.2% | -2.6% | 8.7M |
| LLY | 1,408.43 (08:49 sip) | +0.1% | 1,407.59 | 43.30 (3.1%) | 1,258.81-1,475.25 | +1.0% / +10.3% | -0.6% | 3.3M |
| UNH | 338.00 (08:49 sip) | -1.1% | 341.88 | 16.51 (4.8%) | 319.13-416.19 | -11.7% / -11.7% | -12.3% | 7.5M |
| JNJ | 278.03 (08:49 sip) | +0.6% | 276.46 | 6.73 (2.4%) | 262.89-288.81 | +0.8% / +3.8% | -0.3% | 8.2M |
| WMT | 133.15 (08:57 iex) | +0.6% | 132.31 | 2.99 (2.3%) | 118.11-132.42 | +4.6% / +12.6% | +3.8% | 24.6M |
| COST | 1,095.00 (08:49 sip) | +0.3% | 1,091.71 | 19.53 (1.8%) | 952.12-1,094.75 | +5.0% / +12.9% | +1.1% | 2.6M |
| HD | 353.48 (08:40 sip) | -0.1% | 353.69 | 9.56 (2.7%) | 316.15-362.44 | +3.2% / +11.7% | +4.3% | 5.2M |
| CAT | 520.59 (08:49 sip) | -3.7% | 540.63 | 29.50 (5.5%) | 508.11-732.73 | -8.0% / -23.2% | -5.3% | 4.2M |
| BA | 161.79 (08:49 sip) | -1.1% | 163.59 | 5.34 (3.3%) | 155.56-179.19 | -3.2% / -10.2% | -0.2% | 8.7M |
| DAL | 83.00 (08:49 sip) | -1.8% | 84.50 | 3.18 (3.8%) | 78.66-92.52 | -1.0% / +2.4% | +0.2% | 5.9M |
| UAL | 105.59 (08:35 sip) | -2.1% | 107.80 | 5.29 (4.9%) | 100.28-122.08 | -1.8% / -0.1% | +1.4% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| HPQ | 28.90 (08:54 iex) | +3.4% | 27.94 | 1.07 (3.8%) | 26.95-33.50 | -3.7% / -9.1% | -2.7% | 14.4M |
| GIS | 36.00 (08:45 sip) | +1.2% | 35.59 | 1.17 (3.3%) | 32.82-37.02 | +2.5% / +5.4% | +2.6% | 8.6M |
| BMY | 62.69 (08:49 sip) | +1.1% | 62.02 | 1.87 (3.0%) | 57.88-65.54 | +0.4% / +1.4% | +1.1% | 10.7M |
| COP | 136.06 (07:05 sip) | +1.1% | 134.64 | 3.78 (2.8%) | 130.26-153.27 | -3.3% / -1.3% | -3.5% | 7.6M |
| MO | 75.59 (08:40 sip) | +1.0% | 74.82 | 1.70 (2.3%) | 72.75-79.97 | -2.2% / +2.3% | -3.4% | 8.9M |
| MDLZ | 67.63 (08:35 sip) | +0.9% | 67.01 | 1.40 (2.1%) | 61.51-68.92 | +1.5% / +6.2% | +0.4% | 9.0M |
| KO | 98.50 (08:57 iex) | +0.9% | 97.62 | 1.94 (2.0%) | 90.58-100.56 | +1.3% / +6.0% | -1.2% | 20.1M |
| PAYX | 115.99 (04:10 sip) | +0.8% | 115.08 | 2.97 (2.6%) | 106.67-122.72 | +0.5% / +4.7% | +0.9% | 2.7M |
| MU | 573.00 (09:04 iex) | -9.0% | 629.79 | 75.53 (12.0%) | 585.25-990.00 | -17.3% / -30.2% | -11.6% | 36.0M |
| SNDK | 71.23 (09:05 iex) | -8.6% | 77.95 | 13.86 (17.8%) | 74.83-176.06 | -32.3% / -52.4% | -21.8% | 113.6M |
| DELL | 273.64 (09:04 iex) | -7.3% | 295.28 | 40.28 (13.6%) | 274.35-507.00 | -17.5% / -36.1% | -8.5% | 9.2M |
| ARM | 150.67 (08:49 sip) | -6.7% | 161.56 | 18.27 (11.3%) | 150.37-237.88 | -14.4% / -31.8% | -11.9% | 6.5M |
| AMAT | 302.52 (08:49 sip) | -6.6% | 323.76 | 30.86 (9.5%) | 300.62-425.88 | -10.7% / -23.2% | -7.2% | 9.0M |
| MRVL | 122.95 (08:53 iex) | -6.6% | 131.57 | 16.23 (12.3%) | 120.56-253.66 | -18.3% / -39.4% | -11.5% | 34.7M |
| STX | 451.00 (08:49 sip) | -6.5% | 482.48 | 53.06 (11.0%) | 449.28-718.65 | -11.2% / -30.3% | -4.3% | 5.8M |
| LRCX | 183.60 (08:49 sip) | -6.4% | 196.16 | 19.49 (9.9%) | 181.77-260.58 | -10.4% / -25.8% | -6.9% | 14.2M |
