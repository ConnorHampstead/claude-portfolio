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

## Your last post-open review (2026-11-19)

*For continuity: what you were watching and why. The book state below is
current and overrides anything here.*

# Post-open review: Thursday 2026-11-19, 10:05 ET (16:05 Stockholm; ET+6 today)

I'm opening nothing new and leaving the GLD and HD short brackets as they are. PANW's opening range failed both of the morning's conditions.

### 1. Since the open

- **Indices:** the tape opened as the futures pointed, but the gains are narrow. QQQ is +2.1% and SPY +1.0%, while IWM (−0.1%) and DIA (+0.1%) are flat. All of the gain is in tech and semis (SMH +4.1%, XLK +3.1%).
- **Defensives:** they are being sold hard. XLP is −1.8%, XLV −1.2% and XLU −1.0%. KO is −3.2%, PM −3.4% and below its 20-day low, MO −3.5%, and UNH −2.2% after Wednesday's −10.2%.
- **Rates and dollar:** the 10-year is about 5.10% (+3bp, Yahoo ticker) and DXY about 103.6–103.7 (FXStreet). Neither moved on the softer claims and Philly Fed prints.
- **ANT:** it became eligible to trade at 10:00 ET, with market makers bidding about $99.60 against the $83 pricing. I found no confirmed first trade (NBC, 10:02 ET).
- **10:00 ET data:** the only scheduled item I can find is the Conference Board LEI, consensus 0%. I could not verify the actual print. Existing home sales came out Nov 12, not today.
- **Net:** nothing here changes the morning's view.

### 2. Fills, positions and resting entries

- **GLD short** (session 2 of 10; entry 345.91, stop 355.50, target 330.00; last 339.90): **keep.**
  - The invalidation needs DXY below 102.50 *and* December-hike odds below 70%. DXY is about 103.6–103.7 and a December hike is still about 90% priced, so it has not happened.
  - GLD is an ETF and has no binary event of its own.
- **HD short** (session 3 of 10; entry 343.57, stop 353.50, target 323.50; last 335.67): **keep.**
  - The invalidation is a daily close above 347.51. Today's high so far is 336.38, so it has not happened.
  - HD reported on Nov 17 and has nothing of its own scheduled.
- **Fills / resting entries:** none.

### 3. The morning's plans

- **PANW long:** **not triggered.**
  - Condition (a) failed: it opened at 355.81 and the 09:30–10:00 low was **354.20**, under the required 360.00.
  - Condition (b) failed: it was **364.97** at 10:04 (StockAnalysis), not in the 368–375 band.
  - The low held above 353.36, so the drop condition never came into play. The morning's pass stands, and it is already in the shadow book.
- **GLD:** the close condition was not met (see above).
- **HD:** the close condition cannot be judged until the close. Tomorrow's brief checks it.
- **WMT:** no action, as planned. It opened at 123.68, low 123.27, and is back to 125.61, the reversal the morning flagged.

### 4. New plays

**None.** I looked at three candidates and none clears the bar:

- **UNH short continuation:**
  - The catalyst is verified. CMS proposed rule CMS-6098-P was announced Nov 16. It would extrapolate Medicare Advantage RADV audits back to payment year 2018, with recoveries of about $9B per audit year industry-wide. Comments are open to Jan 19, 2027.
  - But the stock is already −13% in five days, with the drop on 3x normal volume. The stop has to clear today's 353.85 high, which puts it 1.3 ATR away. EV is negative at the base rate.
- **XLP / staples short:**
  - I could not find a dated reason for the KO, PM, MO, HSY and STZ selloff beyond "rotation and rates". Yahoo's PM note was a thin, unsourced list.
  - I can't explain the move, so it isn't a trade.
- **ZS long (cyber read-across):**
  - Its fiscal Q1 report is estimated for about Nov 27. That is a calendar estimate (mfn.se), not confirmed, but it is inside 7 days, so rule 8 excludes it.
  - It is also already +9.7%, which is 1.6 ATR.

### 5. Passing on

- **UNH short** (sell stop 339.50 / stop 358.00 / target 310.00, 1.59R, P 0.36, EV −0.07R):
  - I'm starting from the 38% base rate and shading it down because the stock is stretched about 3 ATR in five days.
  - Next earnings are mid-January 2027, inferred and not confirmed.
- **XLP short** (market 89.50 / stop 91.60 / target 86.40, 1.48R, P 0.37, EV −0.08R): a one-day rotation I couldn't tie to a source.
- **QQQ fade short** (limit 686.00 near the 20-day average / stop 707.00 / target 650.00, 1.71R, P 0.35, EV −0.05R):
  - This tests the morning's "the short side has the edge" view, but it has no dated catalyst. Conviction 2.
- **ZS long:** excluded by rule 8, with earnings estimated about Nov 27. No levels.
- **PDD long:** +12% is 3.7 ATR already spent, and I couldn't verify the results against consensus. No levels.

### 6. For tomorrow (Fri Nov 20)

- **HD:** close the position if Thursday's close is above 347.51. Otherwise hold.
- **GLD:** close only if DXY is below 102.50 *and* December-hike odds are below 70%.
- **ANT debut:** if QQQ gives back its gap and closes below 659.51 (Wednesday's close), the AI relief has failed. Look at index or semis shorts on a new catalyst, not on the narrative.
- **PANW:**
  - A long needs a hold above 354.20 (today's low) and an entry no higher than about 368, with the stop under 347.
  - Above 375 the room to the 406.88 20-day high is too small.
- **Also on the calendar:**
  - INTU and GAP report after the close.
  - TTWO may disclose GTA VI sales.
  - Resting entries are cleared before the weekend, and Thanksgiving week follows.

**Book state:** gross 36%, net −36% (caps 150% / ±100%); risk at stake 1.05% of equity (cap 4%); 2 of 8 slots. Nothing changes.

```json
{
  "date": "2026-11-19",
  "no_trade": true,
  "session_note": "Narrow AI/ANT-IPO relief rally (QQQ +2.1%, IWM/DIA flat) with defensives sold and 10y ~5.10%, DXY ~103.6; PANW failed both opening-range conditions (low 354.20 < 360, 364.97 at 10:04 outside 368-375); UNH/XLP shorts negative EV, ZS excluded by earnings ~Nov 27. Would act on a QQQ close back below 659.51 with a dated catalyst, or PANW holding 354.20 with entry <=368.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "UNH",
      "direction": "short",
      "entry_type": "stop",
      "entry": 339.50,
      "stop": 358.00,
      "targets": [310.00],
      "p_target_first": 0.36,
      "reason": "CMS RADV extrapolation proposal (CMS-6098-P, Nov 16; ~$9B/audit year industry-wide, comments to Jan 19 2027) verified, but UNH is already -13% in 5 days (-10.2% Nov 18 on 3x volume); stop must clear today's 353.85 high, 1.3 ATR. EV about -0.07R."
    },
    {
      "ticker": "XLP",
      "direction": "short",
      "entry_type": "market",
      "entry": 89.50,
      "stop": 91.60,
      "targets": [86.40],
      "p_target_first": 0.37,
      "reason": "Defensive rotation (KO -3.2%, PM -3.4% below its 20d low, MO -3.5%) with 10y ~5.10%, but no dated catalyst found at source; a one-day rotation on an AI relief day often reverses. 1.48R, EV about -0.08R."
    },
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "limit",
      "entry": 686.00,
      "stop": 707.00,
      "targets": [650.00],
      "p_target_first": 0.35,
      "reason": "Fade of the single-event ANT relief rally at the ~686 20d average in a hawkish-Fed downtrend, but there is no dated catalyst beyond the narrative; conviction 2. EV about -0.05R."
    }
  ]
}
```

Sources:
- [StockAnalysis: PANW quote, 10:04 ET](https://stockanalysis.com/stocks/panw/)
- [Robinhood: PANW](https://robinhood.com/us/en/stocks/PANW/)
- [Benzinga: PANW soars](https://www.benzinga.com/markets/large-cap/26/11/63422632/palo-alto-networks-stock-soars-investors-cheer-strong-outlook-applied-compute-acquisition)
- [FX Leaders: PANW +9%](https://www.fxleaders.com/news/2026/11/19/palo-alto-networks-stock-forecast-panw-q1-earningsc/)
- [Yahoo Finance live, Nov 19](https://finance.yahoo.com/markets/live/stock-market-today-thursday-november-19-dow-sp-500-nasdaq-anthropic-ipo-live-141306032.html)
- [NBC: Anthropic IPO live updates](https://www.nbcnews.com/business/markets/live-blog/anthropic-ipo-live-updates-rcna610159)
- [CBS: Anthropic Nasdaq debut](https://www.cbsnews.com/news/anthropic-ipo-nasdaq-debut-claude-ai/)
- [Crypto Briefing: ANT indicated at $100](https://cryptobriefing.com/anthropic-shares-indicated-open-100-ipo/)
- [FXStreet: DXY off its 19-month high](https://www.fxstreet.com/news/us-dollar-takes-a-breather-after-rally-to-19-month-high-202611191423)
- [FXStreet: claims 203K](https://www.fxstreet.com/news/us-initial-jobless-claims-rose-to-203k-last-week-202611191337)
- [JournalArta: market open](https://journalarta.com/en/2026/11/19/stock-market-today-nasdaq-rises-at-the-open-while-dow-holds-near-flat/)
- [TechFlow: Nasdaq opens +1.6%](https://www.techflowpost.com/en-US/newsletter/145808)
- [HeyGoTrade: UNH and the CMS audit proposal](https://www.heygotrade.com/en/news/unitedhealth-unh-stock-news-november-19-2026/)
- [MarketBeat: UNH −10.2%](https://www.marketbeat.com/instant-alerts/price-unitedhealth-group-nyse-unh-stock-falls-102-heres-what-happened-2026-11-18/)
- [GuruFocus: UNH regulatory concerns](https://www.gurufocus.com/news/9208180/unitedhealth-group-unh-shares-drop-over-8-amid-regulatory-concerns-on-november-18-2026)
- [FX Leaders: $9B clawback](https://www.fxleaders.com/news/2026/11/18/unitedhealth-faces-9-billion-industry-clawback-under-new-cms-rules-sending-unh-stock-below-350/)
- [Yahoo search result: PM quote, 10:02 ET](https://finance.yahoo.com/quote/PM/)
- [24/7 Wall St: staples, Nov 19](https://247wallst.com/investing/2026/11/19/4-high-yield-consumer-staples-stocks-retirees-should-buy-before-december/)
- [TradingView: KO and TD Cowen](https://www.tradingview.com/news/gurufocus:36d954ccf094b:0-coca-cola-stocks-move-lower-even-as-td-cowen-names-it-top-2027-pick/)
- [mfn.se: Zscaler calendar (estimated date)](https://mfn.se/all/a/zscaler-inc/zscaler-hosts-2026-investor-day-reaffirms-first-quarter-and-fiscal-2027-guidance-545a473b)
- [RTTNews: Zscaler reaffirms Q1 FY27 guidance](https://www.rttnews.com/3696784/zscaler-reaffirms-q1-fy27-guidance.aspx)
- [ForexCracked: CB LEI calendar](https://www.forexcracked.com/economic-calendar/usd-cb-leading-economic-index-m-m/)
- [StockAnalysis: October existing home sales (released Nov 12)](https://stockanalysis.com/news/existing-home-sales-16-year-low-october-2026/)
- [HDFC Sky: Dow −561 on Nov 18](https://hdfcsky.com/news/dow-jones-sinks-561-points-as-hawkish-fed-minutes-and-unitedhealth-collapse-november-19-2026)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Friday 2026-11-20. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,722.78**
- Cash: $140,670.03
- Session P&L so far: +0.32% (new entries are blocked at -3.0%)
- Gross exposure: $36,947 (36% of equity, cap 150%)
- Net exposure: $-36,947 (-36%, cap +/-100%)
- Risk at stake (entry to stop): $1,082 (1.04% of equity, cap 4.0%) — 2.96% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 345.91 | 326.66 | +1,155 (+5.6%) | -19% | 355.50 | 330.00 |
| HD | short | 51 | 343.57 | 340.15 | +174 (+1.0%) | -17% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **GLD**, opened 2026-11-18 (session 3 of at most 10), submitted with stop 359 and target 333, P 36%. Thesis: Gold is trending down on rising real rates and the strongest dollar in 18 months (-4.6% in 5 days, below its 20d and 50d averages). A US-session break below the overnight low (GLD 350.50, under its 352.91 20-day low) confirms the move toward the $3,800 and then ~$3,650 area. The stop entry stays unfilled if Warsh or the minutes turn dovish. Invalidation: DXY back below 102.50 with market-implied December-hike odds below 70%.
- **HD**, opened 2026-11-17 (session 4 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Your record

51 closed trades: 16W / 35L, total +0.37R, net $+2,410 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 51 | 18 | 30 | +0.01R |
| The same trades, bracket left alone | 51 | | | +0.03R |
| Ideas you passed on, or the caps dropped | 111 | 40 | 61 | +0.05R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 44 | 48% |
| 35%-40% | 73 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 149 brackets reached target first. Your Brier score is 0.240; saying 39% every time scores 0.238. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| LOW | short | stop | -0.67R | $-343 | 37% |
| IWM | short | target | +1.67R | $+853 | 36% |
| AMZN | long | stop | -1.20R | $-303 | 36% |
| DAL | long | stop | -0.60R | $-154 | 37% |
| XLE | short | close | -1.02R | $-521 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| GLD | 327.09 (08:58 iex) | -2.4% | 335.18 | 7.37 (2.2%) | 335.05-380.18 | -7.6% / -11.0% | -5.6% | 9.7M |
| HD | 339.05 (08:49 sip) | +0.7% | 336.68 | 10.52 (3.1%) | 316.15-362.44 | -0.5% / +7.1% | -3.3% | 4.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 710.04 (08:49 sip) | -0.8% | 715.87 | 14.70 (2.1%) | 715.65-775.64 | -4.7% / -6.0% | -5.4% | 52.5M |
| QQQ | 636.34 (09:04 iex) | -1.3% | 645.04 | 19.73 (3.1%) | 644.34-726.14 | -5.6% / -9.5% | -6.3% | 52.2M |
| IWM | 263.25 (08:49 sip) | -0.4% | 264.22 | 5.91 (2.2%) | 263.74-286.17 | -4.7% / -5.3% | -5.1% | 24.5M |
| DIA | 489.22 (08:49 sip) | -0.2% | 490.24 | 9.23 (1.9%) | 490.18-536.00 | -5.2% / -5.1% | -6.1% | 3.9M |
| TLT | 80.91 (08:49 sip) | +0.7% | 80.35 | 0.73 (0.9%) | 79.11-82.42 | -0.7% / +0.8% | +0.8% | 35.1M |
| GLD | 327.09 (08:58 iex) | -2.4% | 335.18 | 7.37 (2.2%) | 335.05-380.18 | -7.6% / -11.0% | -5.6% | 9.7M |
| USO | 137.01 (08:49 sip) | -0.8% | 138.09 | 5.73 (4.1%) | 135.01-171.82 | -8.9% / -9.1% | -5.5% | 5.0M |
| SMH | 434.98 (08:49 sip) | -2.8% | 447.48 | 27.46 (6.1%) | 445.32-571.00 | -10.7% / -18.8% | -10.8% | 11.8M |
| XLK | 157.10 (08:49 sip) | -2.2% | 160.69 | 6.52 (4.1%) | 159.63-191.55 | -7.7% / -13.2% | -7.5% | 13.8M |
| XLF | 55.53 (08:49 sip) | -0.1% | 55.58 | 1.09 (2.0%) | 55.30-60.04 | -2.9% / -0.6% | -4.5% | 36.9M |
| XLE | 60.57 (08:49 sip) | -0.5% | 60.89 | 1.79 (2.9%) | 60.43-70.15 | -6.4% / -6.0% | -5.3% | 36.6M |
| XLV | 178.26 (08:49 sip) | +0.5% | 177.46 | 3.76 (2.1%) | 176.96-192.32 | -3.8% / +0.7% | -5.5% | 12.5M |
| XLI | 160.60 (08:49 sip) | -0.5% | 161.36 | 3.67 (2.3%) | 160.83-172.40 | -3.5% / -4.1% | -4.8% | 8.9M |
| XLY | 115.14 (08:30 sip) | -0.6% | 115.88 | 2.95 (2.5%) | 112.83-122.92 | -1.7% / +1.5% | -3.8% | 9.4M |
| XLP | 90.90 (08:49 sip) | +1.2% | 89.86 | 1.65 (1.8%) | 86.36-93.48 | -0.3% / +4.3% | -1.3% | 20.3M |
| XLU | 43.27 (08:49 sip) | +0.6% | 43.01 | 0.62 (1.4%) | 42.39-44.40 | -0.8% / +2.7% | -1.8% | 24.1M |
| XLB | 49.35 (08:45 sip) | -0.1% | 49.42 | 1.13 (2.3%) | 49.32-54.63 | -5.1% / -2.7% | -5.6% | 12.5M |
| XLRE | 43.10 (08:49 sip) | +0.5% | 42.88 | 0.69 (1.6%) | 41.78-45.34 | -1.9% / +0.8% | -3.3% | 7.8M |
| XLC | 102.40 (08:25 sip) | -0.4% | 102.76 | 2.39 (2.3%) | 99.33-109.26 | -1.8% / -5.6% | -4.5% | 8.1M |
| KRE | 69.29 (08:49 sip) | +0.0% | 69.26 | 1.59 (2.3%) | 68.66-75.80 | -4.3% / -3.0% | -4.5% | 14.8M |
| XHB | no trade today | - | 97.89 | 3.31 (3.4%) | 97.19-108.78 | -3.6% / -0.5% | -3.4% | 2.3M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 349.35 (09:00 iex) | +0.0% | 349.21 | 9.01 (2.6%) | 325.08-360.83 | +0.5% / +2.3% | -1.6% | 47.9M |
| MSFT | 487.96 (08:59 iex) | -2.1% | 498.30 | 18.77 (3.8%) | 495.55-558.07 | -4.9% / -4.0% | -4.5% | 28.6M |
| NVDA | 142.68 (09:02 iex) | -2.3% | 145.98 | 11.90 (8.2%) | 145.71-219.99 | -21.4% / -30.1% | -12.2% | 260.8M |
| AMZN | 252.67 (09:04 iex) | -1.8% | 257.37 | 11.20 (4.4%) | 229.36-275.34 | -0.0% / +0.8% | -3.8% | 50.6M |
| GOOGL | 271.23 (09:02 iex) | -0.5% | 272.66 | 10.66 (3.9%) | 272.36-326.40 | -6.7% / -15.8% | -8.7% | 43.5M |
| META | 579.34 (09:03 iex) | -2.8% | 596.22 | 22.04 (3.7%) | 583.80-648.45 | -4.2% / -12.1% | -4.4% | 21.2M |
| TSLA | 365.00 (09:05 iex) | -2.5% | 374.41 | 18.40 (4.9%) | 338.15-414.23 | -3.0% / -0.4% | -5.8% | 36.4M |
| AVGO | 341.04 (09:05 iex) | -1.6% | 346.65 | 20.87 (6.0%) | 289.77-369.82 | +4.0% / +0.8% | -4.9% | 28.2M |
| AMD | 465.71 (09:04 iex) | -4.8% | 489.19 | 50.89 (10.4%) | 402.10-594.00 | -4.8% / -11.8% | -16.4% | 39.6M |
| ORCL | 106.67 (08:49 sip) | -3.5% | 110.57 | 8.20 (7.4%) | 109.21-148.48 | -10.7% / -16.8% | -13.0% | 40.7M |
| NFLX | 58.46 (08:49 sip) | +0.0% | 58.46 | 1.91 (3.3%) | 58.18-67.82 | -6.8% / -13.8% | -6.7% | 39.6M |
| CRM | 182.75 (08:49 sip) | -0.3% | 183.31 | 8.91 (4.9%) | 182.51-250.99 | -17.0% / -20.6% | -15.7% | 7.2M |
| JPM | 318.49 (08:49 sip) | -0.5% | 320.22 | 8.55 (2.7%) | 317.43-359.80 | -5.2% / -5.2% | -6.6% | 6.6M |
| GS | 837.99 (08:49 sip) | -1.1% | 847.53 | 30.36 (3.6%) | 843.88-939.38 | -5.6% / -6.8% | -7.2% | 2.1M |
| BAC | 48.40 (08:49 sip) | -0.4% | 48.57 | 1.21 (2.5%) | 48.05-53.02 | -3.3% / -8.4% | -3.8% | 34.3M |
| XOM | 158.18 (08:49 sip) | -0.5% | 158.93 | 4.74 (3.0%) | 158.60-187.32 | -7.3% / -5.7% | -5.8% | 14.7M |
| CVX | 205.60 (08:49 sip) | -0.4% | 206.50 | 5.40 (2.6%) | 204.31-234.53 | -5.5% / -3.4% | -3.8% | 8.4M |
| LLY | 1,354.98 (08:49 sip) | +0.3% | 1,351.12 | 43.97 (3.3%) | 1,256.10-1,475.25 | -2.0% / +7.2% | -5.2% | 3.1M |
| UNH | 337.30 (08:49 sip) | +2.1% | 330.48 | 15.94 (4.8%) | 324.67-425.25 | -17.1% / -15.1% | -18.4% | 6.4M |
| JNJ | 268.75 (08:49 sip) | +0.6% | 267.14 | 7.01 (2.6%) | 262.40-290.25 | -2.7% / -0.1% | -5.8% | 7.6M |
| WMT | 127.90 (08:49 sip) | +1.5% | 126.04 | 3.14 (2.5%) | 118.11-131.82 | +0.9% / +8.4% | -0.1% | 22.5M |
| COST | 1,108.20 (08:49 sip) | +1.3% | 1,093.83 | 20.97 (1.9%) | 978.87-1,123.67 | +4.0% / +11.4% | +0.1% | 2.5M |
| HD | 339.05 (08:49 sip) | +0.7% | 336.68 | 10.52 (3.1%) | 316.15-362.44 | -0.5% / +7.1% | -3.3% | 4.8M |
| CAT | 522.11 (08:49 sip) | -2.8% | 537.37 | 27.99 (5.2%) | 535.53-732.73 | -12.2% / -25.3% | -11.2% | 4.0M |
| BA | 159.50 (08:49 sip) | -0.6% | 160.51 | 4.87 (3.0%) | 158.92-189.66 | -6.8% / -13.3% | -6.4% | 10.6M |
| DAL | 82.75 (08:45 sip) | -0.5% | 83.17 | 3.18 (3.8%) | 75.33-92.52 | -1.9% / +1.1% | -3.9% | 6.0M |
| UAL | 104.80 (08:49 sip) | -0.7% | 105.53 | 5.45 (5.2%) | 96.39-122.08 | -3.3% / -2.3% | -5.1% | 5.2M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| HUM | 389.74 (08:49 sip) | +2.6% | 380.00 | 23.27 (6.1%) | 373.17-462.87 | -10.1% / -7.2% | -14.4% | 1.7M |
| KDP | 35.07 (08:49 sip) | +1.9% | 34.41 | 1.49 (4.3%) | 34.09-38.28 | -4.0% / +2.7% | -2.9% | 23.6M |
| HCA | 469.14 (07:45 sip) | +1.9% | 460.33 | 17.58 (3.8%) | 439.83-521.48 | -5.2% / +0.4% | -8.1% | 1.5M |
| CL | 98.66 (08:49 sip) | +1.8% | 96.88 | 2.22 (2.3%) | 90.47-101.81 | +0.2% / +5.8% | -1.0% | 5.5M |
| GIS | 35.11 (08:49 sip) | +1.8% | 34.48 | 1.16 (3.4%) | 32.82-37.02 | +0.0% / +2.1% | +2.9% | 8.1M |
| ADP | 306.57 (08:49 sip) | +1.8% | 301.19 | 6.62 (2.2%) | 282.73-316.14 | -0.1% / +5.9% | -2.2% | 2.4M |
| AMGN | 444.00 (08:49 sip) | +1.8% | 436.30 | 11.96 (2.7%) | 432.75-481.21 | -4.3% / +2.2% | -6.0% | 2.6M |
| TTWO | 212.22 (08:49 sip) | +1.7% | 208.65 | 13.52 (6.5%) | 183.86-237.41 | +0.0% / +0.5% | -8.1% | 4.6M |
| INTU | 279.65 (08:49 sip) | -9.8% | 310.02 | 13.79 (4.4%) | 302.59-366.47 | -8.2% / -2.3% | -8.9% | 2.8M |
| ROST | 206.00 (08:45 sip) | -6.3% | 219.88 | 8.71 (4.0%) | 218.43-249.30 | -5.1% / -4.9% | -7.3% | 2.3M |
| SNDK | 88.51 (09:04 iex) | -6.2% | 94.40 | 12.90 (13.7%) | 93.67-176.06 | -25.4% / -44.7% | -19.4% | 105.4M |
| TSM | 332.88 (08:54 iex) | -5.5% | 352.09 | 20.54 (5.8%) | 351.14-440.88 | -11.3% / -17.0% | -13.2% | 15.6M |
| ARM | 167.66 (09:02 iex) | -5.4% | 177.17 | 15.65 (8.8%) | 163.13-237.88 | -10.1% / -26.8% | -11.3% | 5.9M |
| DELL | 295.91 (08:49 sip) | -5.3% | 312.54 | 34.32 (11.0%) | 305.80-507.38 | -18.6% / -34.4% | -15.8% | 7.5M |
| WDC | 282.33 (09:03 iex) | -4.9% | 296.78 | 26.87 (9.1%) | 258.61-402.23 | -7.7% / -21.3% | -4.6% | 8.2M |
| MRVL | 131.96 (08:49 sip) | -4.7% | 138.47 | 15.72 (11.4%) | 132.54-253.66 | -21.5% / -37.8% | -15.8% | 31.5M |
