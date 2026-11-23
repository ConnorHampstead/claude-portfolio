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

## Your last post-open review (2026-11-20)

*For continuity: what you were watching and why. The book state below is
current and overrides anything here.*

# Post-open review: Friday 2026-11-20, 10:05 ET (16:05 Stockholm)

No new trades, and HD's bracket stays as submitted. GLD's short closed at its target for +2.15R. Session P&L is +0.01%, so the daily loss limit is not in play.

### 1. Since the open

**Mixed open.**
- **SPY** is flat at 716.25. It opened at 713.61 with a range of 711.72–718.26.
- **QQQ** is −0.7% at 640.22. Its high so far is 643.21, nowhere near the 655–660 retest.
- **Leaders and laggards.** The Dow (+1.0%), staples (XLP +1.9%) and healthcare (XLV +1.5%) are leading. Semis are lagging (SMH −3.2%), along with memory and storage (SNDK −8.1%, MU −6%, STX −5.8%, WDC −5.1%).
- **Rates.** Treasuries are rallying on haven demand. The 10-year is about 4.97–4.98%, down about 7bp, and the 2-year is about 4.70% (CNBC, Bloomberg). FedWatch still prices a December hike at 98.7%.
- **Waller's 08:25 remarks** were welcoming remarks only, with no policy content in the Fed's posted text.
- **UMich final** (10:00 ET): I could not find the print yet. The consensus was 51.0, with 1-year inflation expectations at 4.3% in the preliminary reading. This changes no order either way.

**What changed versus the morning brief:** AVGO fell from 343.01 at the open to 330.00 at 10:05, below the morning's ≤345 level. That still doesn't trigger the plan, which required confirmation from the source. I found the same Chosun Biz, TrendForce, Digitimes and Counterpoint chain, plus a Bernstein estimate of about $50B in savings. All of it is still industry reporting, and one outlet says none of the reports carried comment from Google or Broadcom.

### 2. Fills, positions and resting entries

**GLD short: closed at the 330 target, +2.15R (+$1,097).** It opened at 326.96, through the target. Nothing to do.

**HD short: keep.** It is in session 4 of 10. Last 345.42, intraday high 346.98; stop 353.50 and target 323.50 are both live.
- **Invalidation not met.** It needs a daily *close* above 347.51, and none has happened yet. The 4:00 PM close decides it, and nothing reviews the book before then. If HD closes above 347.51, Monday's brief closes it on that condition.
- **Why it's up:** HD is +2.6% with XHB +1.8%. That is consistent with the bond rally (my inference). I found no HD-specific headline.
- **Events:** none of its own.
- Under the management rules the stop stays where it is.

**Resting entries:** none.

### 3. The morning's plans

- **GLD:** target filled at the open. Done.
- **HD:** held. The test is the close above 347.51, which hasn't happened.
- **UMich:** the print was not found. No order depended on it.
- **AVGO short:** not triggered. The price condition (≤345) is met, but the required confirmation from Google or Broadcom is not. It is also now at its day low, −4.8% and about 0.8 ATR on the day. With the morning's 373.50 stop and a 305 target, R:R would be about 0.57.
- **QQQ short:** not triggered. It never got within 12 points of the 655–660 retest zone, and the morning said not to chase.

### 4. New plays

**None.** Today's movers have no dated reason I could verify at source:
- Memory names are down 5–8%, but they are already −13% to −19% over five sessions.
- Beaten-down software is bouncing (HUBS +7.5%, TEAM +6%, NOW +4.1%, WDAY +4.2%). I found no Nov 20 headline for it; it looks like rotation out of hardware, which is my inference.
- UNH is +4.5%, a bounce after the CMS audit selloff, with no fresh release found.
- GOOGL is +3%. A possible reason is the HBM cost-savings story, but that is unverified.

None of these is a catalyst I could check.

### 5. Passing on

- **AVGO short, re-levelled from here:** market about 330.00, stop 352.00 (above the 346.65 prior close and 343.01 open, about 1.05 ATR), target 297.00 (above the 289.77 20-day low). That is 1.5R at P 0.36, which is the 38% base less the single-source catalyst and a short taken at the day low. EV is about −0.10. Earnings are Dec 9 after the close (company release). Conviction 2; it goes in `passed`.
- **XLP long:** the 90.40 limit never had a fill chance; XLP opened at 90.93 and is now 91.59. That leaves 1.8 points to the 93.48 20-day high against a stop under 89.86, which is no better than 1:1. No levels.
- **QQQ, NVDA, INTU, ROST shorts:** the morning's reasons stand. NVDA is −2.9% and QQQ −0.7%, further into extension with nothing new at source.
- **Memory shorts (SNDK, MU, WDC, STX) and software longs (HUBS, TEAM, NOW):** I can't explain the moves at source. No levels.

### 6. For tomorrow (Monday Nov 23, Thanksgiving week)

- **HD:** if Friday's close is above 347.51, close it at Monday's brief on the recorded invalidation. Otherwise the bracket stands.
- **AVGO:** a short becomes conviction 3 at the 0.5 tier only if Google or Broadcom confirms direct HBM purchasing at source. The entry would be a bounce sell at 345–350, stop 373.50, target 305.
  - Dec 9 earnings are 16 days from Monday, so the rule-8 window is clear until Dec 1.
  - Without confirmation, I would not chase below 330.
- **QQQ:** the short only works on a failed retest of 655–660. A gap lower Monday is not an entry.

**Book state:** gross 17% and net −17% of equity (caps 150% / ±100%); risk at stake 0.49% (cap 4%); 1 of 8 slots used.

```json
{
  "date": "2026-11-20",
  "no_trade": true,
  "session_note": "Mixed open: SPY flat, QQQ -0.7%, Dow +1%, semis/memory -3% to -8%, havens bid (10y ~4.97%, XLP +1.9%); Dec hike still 98.7%. GLD short hit its 330 target (+2.15R). HD held (close >347.51 is the invalidation; intraday high 346.98). AVGO fell to 330 but the HBM report is still unconfirmed by Google/Broadcom; QQQ never retested 655-660. No new trade: would act on company-source confirmation of Google bypassing Broadcom on HBM (AVGO short 345-350, stop 373.50, 0.5 tier) or a failed QQQ retest of 655-660.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "AVGO",
      "direction": "short",
      "entry_type": "market",
      "entry": 330.00,
      "stop": 352.00,
      "targets": [297.00],
      "p_target_first": 0.36,
      "reason": "Down 4.8% on the day to 330.00 (day low) on the Chosun Biz/TrendForce/Digitimes report that Google will buy HBM directly for TPU 8t; still no Google or Broadcom comment. Stop above 346.65 prior close/343.01 open (~1.05 ATR), target above 289.77 20d low; earnings Dec 9 AMC. 1.5R, EV about -0.10: single-sourced and shorting the day low. Conviction 2."
    }
  ]
}
```

Sources:
- [CNBC: Treasury yields sharply lower as investors flee to havens (Nov 20)](https://www.cnbc.com/amp/2026/11/20/treasury-yields-bonds-inflation.html)
- [Bloomberg: Treasuries add to steep weekly gain (Nov 20)](https://www.bloomberg.com/news/articles/2026-11-20/treasuries-eye-longest-rally-in-five-months-on-haven-demand)
- [Federal Reserve: Waller welcoming remarks, College Fed Challenge (Nov 20)](https://www.federalreserve.gov/newsevents/speech/waller20261120a.htm)
- [TipRanks: Waller/Cook preview](https://www.tipranks.com/news/investors-pile-into-u-s-bonds-as-fed-governors-eye-rate-hikes-ahead-of-oil-rig-data)
- [TrendForce: Google eyes direct HBM purchases (Nov 18)](https://www.trendforce.com/news/2026/11/18/news-google-reportedly-eyes-direct-hbm-purchases-for-tpus-reducing-broadcom-related-costs/)
- [Digitimes: Google looks to bypass Broadcom with direct HBM purchases](https://www.digitimes.com/news/a20261119VL217/google-hbm-broadcom-mediatek-2027.html)
- [BigGo: Bernstein estimates $50B savings](https://finance.biggo.com/news/b4d1fa73-eef1-4cc3-b0af-0ce914aa1470)
- [mlq.ai: Google HBM bypass, industry reports](https://mlq.ai/news/google-moves-to-buy-hbm-directly-for-its-mediatek-built-ai-chips-bypassing-broadcom-industry-reports-say/)
- [Futu: memory margin pressure angle](https://news.futunn.com/en/post/1005145439/google-to-bypass-broadcom-and-procure-hbm-directly-cost-reduction)
- [StockTitan: Stock market today live, Nov 20](https://www.stocktitan.net/articles/stock-market-today-live-november-20-2026)
- [24/7 Wall St.: AMD, TSM pre-market chip selloff (Nov 20)](https://247wallst.com/investing/2026/11/20/amd-stock-drops-another-7-0-before-the-bell-and-taiwan-semiconductor-slides-4-2-as-nasdaq-futures-fall-1-6-after-asias-chip-selloff/)
- [Opening Bell Daily: Nasdaq swing Nov 19–20](https://www.openingbelldailynews.com/p/nasdaq-swing-nov-20-2026)
- [Admiral Markets: UMich final November preview](https://admiralmarkets.com/education/articles/forex-analysis/michigan-consumer-sentiment-final-november-2026-preview)
- [XTB: Economic calendar, final UMich and Fed speakers](https://www.xtb.com/en/market-analysis/economic-calendar-final-us-consumer-sentiment-data-and-speeches-by-fed-officials)
- [Advisor Perspectives: preliminary November sentiment](https://www.advisorperspectives.com/dshort/updates/2026/11/06/consumer-sentiment-recovers-significantly)
- [Trefis: UnitedHealth Nov 18 drop on CMS audit proposal](https://www.trefis.com/stock/unh/articles/626878/what-just-happened-to-unitedhealth-stock/2026-11-19)
- [MarketBeat: Home Depot quote and Q3 results](https://www.marketbeat.com/stocks/NYSE/HD/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Monday 2026-11-23. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,584.83**
- Cash: $121,012.04
- Session P&L so far: -0.13% (new entries are blocked at -3.0%)
- Gross exposure: $17,427 (17% of equity, cap 150%)
- Net exposure: $-17,427 (-17%, cap +/-100%)
- Risk at stake (entry to stop): $506 (0.49% of equity, cap 4.0%) — 3.51% left for new plays
- Slots: 1 open + 0 resting entries of 8 — you may add at most 7 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| HD | short | 51 | 343.57 | 341.71 | +95 (+0.5%) | -17% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **HD**, opened 2026-11-17 (session 5 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Your record

52 closed trades: 17W / 35L, total +2.52R, net $+3,507 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 52 | 19 | 30 | +0.05R |
| The same trades, bracket left alone | 52 | | | +0.07R |
| Ideas you passed on, or the caps dropped | 125 | 45 | 70 | +0.05R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 48 | 50% |
| 35%-40% | 83 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 5 | 20% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 164 brackets reached target first. Your Brier score is 0.242; saying 39% every time scores 0.238. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| GLD | short | target | +2.15R | $+1,097 | 36% |
| LOW | short | stop | -0.67R | $-343 | 37% |
| IWM | short | target | +1.67R | $+853 | 36% |
| AMZN | long | stop | -1.20R | $-303 | 36% |
| DAL | long | stop | -0.60R | $-154 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| HD | 344.58 (08:30 sip) | +1.6% | 339.04 | 10.42 (3.1%) | 316.15-362.44 | -0.1% / +7.6% | -2.8% | 5.0M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 719.67 (09:03 iex) | +4.3% | 689.81 | 16.07 (2.3%) | 686.75-775.64 | -7.8% / -9.2% | -8.6% | 58.4M |
| QQQ | 651.00 (09:03 iex) | +7.0% | 608.45 | 21.13 (3.5%) | 606.23-726.14 | -10.3% / -14.4% | -10.5% | 57.4M |
| IWM | 262.47 (08:49 sip) | +2.3% | 256.61 | 6.28 (2.4%) | 256.32-286.17 | -7.1% / -7.8% | -7.5% | 26.3M |
| DIA | 492.05 (09:00 iex) | +2.3% | 481.08 | 9.90 (2.1%) | 479.40-536.00 | -6.7% / -6.7% | -7.9% | 4.0M |
| TLT | 81.07 (09:04 iex) | -0.5% | 81.45 | 0.78 (1.0%) | 79.11-82.42 | +0.7% / +2.1% | +2.6% | 36.6M |
| GLD | 335.45 (09:05 iex) | +3.9% | 322.87 | 7.81 (2.4%) | 320.95-380.18 | -10.4% / -13.9% | -9.2% | 10.3M |
| USO | 135.01 (08:49 sip) | -3.3% | 139.63 | 5.13 (3.7%) | 135.01-171.82 | -7.0% / -7.9% | -4.1% | 4.9M |
| SMH | 465.57 (09:04 iex) | +16.4% | 400.06 | 29.20 (7.3%) | 396.85-571.00 | -19.1% / -26.9% | -17.8% | 12.6M |
| XLK | 154.62 (08:49 sip) | +3.8% | 149.01 | 6.92 (4.6%) | 148.09-191.55 | -13.6% / -19.2% | -12.5% | 15.2M |
| XLF | 55.40 (08:45 sip) | +1.5% | 54.57 | 1.12 (2.1%) | 54.42-60.04 | -4.6% / -2.3% | -7.0% | 39.5M |
| XLE | 60.55 (08:49 iex) | +0.1% | 60.51 | 1.68 (2.8%) | 60.34-70.15 | -6.4% / -6.4% | -6.9% | 37.0M |
| XLV | 177.09 (08:59 iex) | -0.1% | 177.24 | 3.88 (2.2%) | 176.71-192.32 | -3.9% / +0.5% | -6.1% | 13.0M |
| XLI | 159.60 (08:49 sip) | +2.1% | 156.37 | 3.89 (2.5%) | 155.70-172.40 | -6.3% / -6.9% | -7.4% | 9.2M |
| XLY | 115.41 (08:15 sip) | +2.6% | 112.46 | 3.03 (2.7%) | 112.03-122.92 | -4.5% / -1.5% | -6.3% | 9.7M |
| XLP | 90.80 (08:49 sip) | +0.4% | 90.46 | 1.69 (1.9%) | 86.36-93.48 | +0.2% / +4.8% | -2.0% | 21.0M |
| XLU | 43.06 (08:49 sip) | +0.9% | 42.69 | 0.64 (1.5%) | 42.42-44.40 | -1.6% / +1.9% | -3.1% | 24.7M |
| XLB | 49.21 (08:25 sip) | +1.8% | 48.34 | 1.17 (2.4%) | 48.21-54.63 | -6.9% / -4.8% | -7.4% | 13.0M |
| XLRE | 42.99 (08:45 sip) | +1.2% | 42.46 | 0.72 (1.7%) | 41.78-45.34 | -2.8% / -0.2% | -4.3% | 7.9M |
| XLC | 102.78 (08:40 sip) | +2.7% | 100.03 | 2.58 (2.6%) | 99.33-109.26 | -4.2% / -7.9% | -8.0% | 8.4M |
| KRE | 69.41 (08:45 sip) | +1.6% | 68.32 | 1.58 (2.3%) | 68.14-75.80 | -5.3% / -4.2% | -6.1% | 15.1M |
| XHB | 98.18 (07:30 sip) | +1.6% | 96.60 | 3.30 (3.4%) | 96.34-108.78 | -4.8% / -1.8% | -5.4% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 347.29 (09:05 iex) | +1.4% | 342.56 | 9.36 (2.7%) | 325.08-360.83 | -1.4% / +0.3% | -3.8% | 49.9M |
| MSFT | 503.96 (08:57 iex) | +4.0% | 484.52 | 18.64 (3.8%) | 481.03-558.07 | -7.2% / -6.6% | -7.3% | 30.2M |
| NVDA | 164.67 (09:05 iex) | +31.2% | 125.53 | 12.84 (10.2%) | 124.50-219.99 | -30.8% / -39.4% | -22.9% | 288.5M |
| AMZN | 256.85 (09:05 iex) | +4.1% | 246.82 | 11.29 (4.6%) | 229.36-275.34 | -4.1% / -3.2% | -7.4% | 53.1M |
| GOOGL | 281.24 (09:05 iex) | +6.0% | 265.29 | 11.42 (4.3%) | 264.22-326.40 | -8.3% / -17.7% | -10.3% | 45.5M |
| META | 592.19 (09:04 iex) | +5.6% | 560.84 | 23.63 (4.2%) | 558.68-648.45 | -9.3% / -17.1% | -12.6% | 21.7M |
| TSLA | 367.72 (09:04 iex) | +6.3% | 345.82 | 19.36 (5.6%) | 338.15-414.23 | -10.1% / -7.9% | -11.4% | 37.0M |
| AVGO | 308.35 (09:02 iex) | +1.3% | 304.41 | 23.29 (7.7%) | 289.77-369.82 | -8.4% / -11.2% | -12.3% | 30.4M |
| AMD | 457.28 (09:04 iex) | +7.7% | 424.39 | 52.59 (12.4%) | 402.10-594.00 | -16.6% / -23.3% | -20.5% | 42.4M |
| ORCL | 114.99 (09:05 iex) | +13.6% | 101.19 | 8.06 (8.0%) | 100.25-148.48 | -17.4% / -23.3% | -19.3% | 42.2M |
| NFLX | 57.99 (08:56 iex) | +2.2% | 56.73 | 2.03 (3.6%) | 56.56-67.49 | -8.9% / -15.8% | -8.7% | 41.1M |
| CRM | 183.50 (08:49 sip) | +1.6% | 180.62 | 9.06 (5.0%) | 179.91-250.99 | -16.9% / -21.4% | -17.1% | 7.3M |
| JPM | 313.95 (08:49 sip) | +1.1% | 310.53 | 9.00 (2.9%) | 309.18-359.80 | -7.7% / -7.8% | -10.3% | 7.0M |
| GS | 809.00 (08:45 sip) | +2.3% | 790.69 | 33.10 (4.2%) | 786.66-939.38 | -11.5% / -12.6% | -13.7% | 2.3M |
| BAC | 47.80 (08:49 sip) | +1.6% | 47.04 | 1.27 (2.7%) | 46.88-53.02 | -6.0% / -10.7% | -7.8% | 35.5M |
| XOM | 159.60 (08:49 sip) | -0.2% | 159.99 | 4.41 (2.8%) | 158.60-187.32 | -6.1% / -5.0% | -5.6% | 15.0M |
| CVX | 208.25 (08:40 sip) | -0.1% | 208.37 | 5.13 (2.5%) | 204.31-234.53 | -4.1% / -2.5% | -4.5% | 8.5M |
| LLY | 1,345.00 (09:03 iex) | -0.2% | 1,347.11 | 43.28 (3.2%) | 1,258.81-1,475.25 | -2.6% / +6.4% | -6.7% | 3.2M |
| UNH | 319.00 (08:49 sip) | -6.1% | 339.85 | 16.10 (4.7%) | 324.67-420.86 | -13.9% / -12.6% | -16.6% | 6.8M |
| JNJ | 272.94 (08:35 sip) | +0.9% | 270.47 | 6.99 (2.6%) | 264.20-290.25 | -1.7% / +1.1% | -5.3% | 7.9M |
| WMT | 128.43 (08:49 sip) | +0.4% | 127.95 | 3.15 (2.5%) | 118.11-131.82 | +2.1% / +9.7% | -0.1% | 23.7M |
| COST | 1,103.00 (08:40 sip) | +0.1% | 1,102.15 | 20.87 (1.9%) | 978.87-1,123.67 | +4.3% / +11.8% | -0.4% | 2.6M |
| HD | 344.58 (08:30 sip) | +1.6% | 339.04 | 10.42 (3.1%) | 316.15-362.44 | -0.1% / +7.6% | -2.8% | 5.0M |
| CAT | 527.27 (08:49 sip) | +3.3% | 510.45 | 28.65 (5.6%) | 508.11-732.73 | -15.4% / -28.4% | -15.0% | 4.1M |
| BA | 158.62 (08:49 sip) | +1.8% | 155.89 | 5.12 (3.3%) | 155.56-189.66 | -8.6% / -15.3% | -9.1% | 10.8M |
| DAL | 82.66 (08:40 sip) | +3.3% | 80.01 | 3.26 (4.1%) | 77.06-92.52 | -5.8% / -2.8% | -7.2% | 6.1M |
| UAL | 105.06 (08:45 sip) | +4.0% | 101.03 | 5.43 (5.4%) | 98.37-122.08 | -7.5% / -6.4% | -7.6% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| ZS | 238.27 (09:02 iex) | +22.3% | 194.82 | 12.42 (6.4%) | 180.47-267.87 | -9.1% / -8.3% | +1.2% | 2.4M |
| KLAC | 153.57 (09:04 iex) | +21.0% | 126.87 | 10.64 (8.4%) | 125.72-171.05 | -15.1% / -24.7% | -16.6% | 15.0M |
| SMCI | 25.91 (09:04 iex) | +19.7% | 21.65 | 2.49 (11.5%) | 21.46-36.40 | -25.1% / -38.1% | -19.4% | 46.5M |
| MRVL | 143.99 (09:04 iex) | +17.8% | 122.28 | 15.01 (12.3%) | 120.56-253.66 | -28.5% / -44.5% | -22.0% | 32.9M |
| LRCX | 215.65 (09:02 iex) | +17.7% | 183.27 | 17.42 (9.5%) | 181.77-260.58 | -17.6% / -31.4% | -18.9% | 13.7M |
| MU | 697.82 (09:05 iex) | +17.4% | 594.51 | 68.34 (11.5%) | 585.25-990.00 | -24.4% / -34.8% | -23.6% | 33.9M |
| SNDK | 92.12 (09:04 iex) | +16.3% | 79.24 | 13.23 (16.7%) | 78.25-176.06 | -35.5% / -52.9% | -28.4% | 108.6M |
| TSM | 367.53 (09:05 iex) | +15.3% | 318.71 | 21.77 (6.8%) | 318.48-440.88 | -18.7% / -24.5% | -20.1% | 17.0M |
| CRWD | 216.52 (09:04 iex) | -5.6% | 229.44 | 15.34 (6.7%) | 213.22-272.29 | -3.6% / -7.1% | +1.2% | 9.2M |
| CVS | 77.75 (08:49 sip) | -3.8% | 80.84 | 3.91 (4.8%) | 77.33-94.77 | -7.0% / -8.2% | -9.5% | 13.0M |
| ELV | 380.41 (08:25 sip) | -3.6% | 394.48 | 16.21 (4.1%) | 383.17-448.54 | -6.4% / -5.1% | -8.2% | 1.5M |
| HUM | 377.00 (08:45 sip) | -3.3% | 390.00 | 23.32 (6.0%) | 373.17-462.87 | -7.4% / -4.6% | -13.3% | 1.8M |
| CNC | 62.89 (08:49 sip) | -1.4% | 63.78 | 3.89 (6.1%) | 63.29-78.08 | -8.2% / -5.4% | -10.5% | 6.5M |
| CI | 268.88 (08:45 sip) | -0.7% | 270.90 | 9.75 (3.6%) | 267.22-318.05 | -8.2% / -6.0% | -8.8% | 1.9M |
| EW | 101.23 (08:40 sip) | -0.6% | 101.85 | 3.14 (3.1%) | 87.90-108.00 | +1.8% / +10.4% | -4.9% | 5.2M |
| PSX | 238.30 (08:45 sip) | -0.4% | 239.33 | 10.30 (4.3%) | 238.33-292.99 | -7.9% / -10.2% | -9.2% | 3.6M |
