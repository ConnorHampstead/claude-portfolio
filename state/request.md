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

## Your last post-open review (2026-11-18)

*For continuity: what you were watching and why. The book state below is
current and overrides anything here.*

## Post-open review, Wed 2026-11-18, 10:05 ET (16:05 Stockholm, ET+6)

I'm making no changes and opening nothing new. All three short positions keep their brackets, and every idea I looked at goes to the shadow book.

### 1. Since the open
- **Pending home sales (10:00 ET):** down 4.7% on the month and 16.7% on the year, with every region lower. It is the second straight record low ([NAR release](https://www.globenewswire.com/news-release/2026/11/18/3405853/0/en/pending-home-sales-decreased-4-7-in-october-according-to-nar-report.html)).
- **The market bought housing and retail anyway:**
  - LOW opened at 212.07, hit 211.00 and has since run to 219.90. It is 218.90 now.
  - HD went from 330.31 to 336.94.
  - XHB is up 0.9% and XLY up 1.5%.
  - TGT went from roughly flat before the open to +6.3%, and TJX is up 9.9%.
  - What changed since the morning: buyers are paying up for consumer strength. Target's comps rose 5.6% against 3.8% expected, with traffic up 5%.
- **Indices:** the S&P is flat and the Dow is down 0.7%.
- **NVDA:** its rally faded from 159.70 to 154.96, now below yesterday's close ([Investing/Reuters](https://investing.com/news/stock-market-news/sp-500-nasdaq-open-higher-as-nvidia-forecast-eases-ai-jitters-5036411)).
- **Gold and miners:** gold is down 2.5% and miners are following (FCX −6.9%, NEM −5.6%).

### 2. Fills, positions and resting entries
- **GLD short (filled at 345.91, session 1): keep.**
  - The stop fired at the 346.31 open, so $575 is at risk (0.56%).
  - The invalidation (DXY below 102.50 *and* December-hike odds below 70%) has not happened. The dollar is near a 19-month high and a hike is about 97% priced.
- **HD short (session 2): keep.** The invalidation is a close above 347.51; HD is at 336.94.
- **LOW short (filled at 215.58, session 1): keep.**
  - The limit filled on the rebound, above 212.50, so the stop is only 5.92 points away (0.81 ATR). It risks $337 instead of the planned $517. That is not a reason to close.
  - The invalidation is a close above 220.46; LOW is at 218.90 intraday. If the bounce goes on, the 221.50 stop is there for it.
  - The record pending-home-sales number supports the thesis. The bid in the stock does not, but that is price action, not the invalidation.
- **Resting entries:** none.

### 3. The morning's plans
- **LOW:** it filled and is above 218, so per the plan, no action.
- **GLD:** it filled at 345.91, not below 344, so per the plan, no action.
- **Pending home sales:** −4.7%, a record low. Logged as information only; nothing changes.

### 4. New plays
None. The best new idea was a TGT long, and I'm passing on it at conviction 2:
- **The catalyst checks out at the source** ([Target release](https://corporate.target.com/press/release/2026/11/target-corporation-reports-third-quarter-earnings), [CNBC](https://www.cnbc.com/2026/11/18/target-tgt-q3-2026-earnings.html)):
  - Comps rose 5.6% against 3.8% expected, with traffic up 5%.
  - Full-year EPS guidance was raised to $10.65–11.40 from $9.90–10.90.
  - Without the $0.50 tariff refund, EPS is about $2.15 against $2.07 expected, still a modest beat.
- **Why I'm not taking it today:**
  - The 52-week high is 170.75 ([Wedbush](https://investor.wedbush.com/wedbush/quote?Symbol=NY%3ATGT)), just above today's 169.78 high.
  - The stock is up 60% this year, and the average analyst price target is below the price ([TIKR](https://www.tikr.com/blog/target-stock-is-up-60-in-2026-wall-streets-average-target-now-sits-below-it)).
  - Walmart, the most direct comparison, reports tomorrow before the open. Sources say the date is confirmed, but the time is not; most likely about 07:00 ET (13:00 Stockholm).
- **The entry is stuck either way:**
  - A pullback limit at 166.50 would most likely fill on a Walmart-driven gap down. That is the ROST/ANET pattern, where a gap fills the limit right next to the stop.
  - Buying at the market now needs a 10-point stop (1.9 ATR). That only leaves room for a 1.5R target, and the expected value comes out at about zero.
- **Next earnings:** about 2027-03-02. That is inferred from the 2026-03-03 report date, not confirmed.

### 5. Passing on
- **TGT long** (limit 166.50 / stop 159.40 / target 180.50, about 2R, P 0.36): the reasons are in section 4. Conviction 2.
- **UNH short** (market 372.92 / stop 390.50 / target 338.00, P 0.32, expected value −0.04R):
  - This is the second day of the CMS proposal to widen Medicare Advantage audits, published Nov 17 ([TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262310909-unitedhealth-falls-cms-crush-audit-rule-unh-385-23-support-november-18-2026-tradingkey)).
  - I found no new headline today. The stock is already about 9.5% lower over two days, so this would be a chase.
- **NVDA short** (market 154.96 / stop 166.50 / target 132.00, P 0.33):
  - The beat-and-raise fading to red is a bearish sign.
  - Against it: the stop has to be 1 ATR (11.5 points), the delayed 10-Q is a company-specific event due by Dec 4, and Anthropic lists tomorrow. Conviction 2.
- **NEM / FCX shorts:** the same gold and rates factor as the GLD short I already hold. No levels.
- **CRM:** the morning's 189.50 sell stop was not placed. CRM has since traded through it (187.85), so the shadow book will score it.

### 6. For tomorrow
- **TGT long:** act if Walmart's Nov 19 report doesn't cut full-year guidance *and* TGT holds above 166.43 (the 20-day high it broke today) before the open. Stop 159.40, target about 180.
- **LOW:** if it closes between 220.46 and 221.50 without hitting the stop, tomorrow's brief closes it on the invalidation.
- **HD:** close only on a close above 347.51.
- **GLD:** close only if DXY is below 102.50 *and* December-hike odds are below 70%.
- **Book after today:** gross 49% (cap 150%), net −49% (cap ±100%), risk at stake 1.38% (cap 4%), 3 of 8 slots. Consumer Discretionary net is −29% against the 40% cap.

```json
{
  "date": "2026-11-18",
  "no_trade": true,
  "session_note": "Record-low pending home sales (-4.7% m/m) but the open bought housing/retail (LOW 211->219.9, TGT +6%, XLY +1.5%); all three shorts held on unmet invalidations. No new play: TGT long waits for WMT's Nov 19 report and a hold above 166.43.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "TGT",
      "direction": "long",
      "entry_type": "limit",
      "entry": 166.50,
      "stop": 159.40,
      "targets": [180.50],
      "p_target_first": 0.36,
      "reason": "Verified Q3 beat (comps +5.6% vs 3.8%, traffic +5%, FY EPS guide raised to $10.65-11.40) and breakout above 20d high, but 52w high 170.75 overhead, +60% YTD with average analyst target below price, and a pullback-limit fill would be adversely selected by WMT's Nov 19 pre-market report. Conviction 2."
    },
    {
      "ticker": "UNH",
      "direction": "short",
      "entry_type": "market",
      "entry": 372.92,
      "stop": 390.50,
      "targets": [338.00],
      "p_target_first": 0.32,
      "reason": "Day 2 of CMS CRUSH Medicare Advantage audit proposal (Nov 17); no new catalyst found today and already ~-9.5% in two sessions, -1.4 ATR today. Chase; EV about -0.04R."
    },
    {
      "ticker": "NVDA",
      "direction": "short",
      "entry_type": "market",
      "entry": 154.96,
      "stop": 166.50,
      "targets": [132.00],
      "p_target_first": 0.33,
      "reason": "Beat-and-raise faded from 159.70 to below the prior close, a bearish reaction, but needs an 11.5-pt (1 ATR) stop, its own delayed 10-Q is due by Dec 4, and the Anthropic listing Thursday is a volatility source. Conviction 2."
    }
  ]
}
```

Sources:
- [NAR: Pending home sales −4.7% in October (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/11/18/3405853/0/en/pending-home-sales-decreased-4-7-in-october-according-to-nar-report.html)
- [Yahoo Finance live, Nov 18](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-november-18-dow-sp-500-nasdaq-nvidia-earnings-anthropic-ipo-143530588.html)
- [Investing.com/Reuters: S&P, Nasdaq open higher](https://investing.com/news/stock-market-news/sp-500-nasdaq-open-higher-as-nvidia-forecast-eases-ai-jitters-5036411)
- [investingLive: Target, TJX, Lowe's macro signals](https://investinglive.com/stocks/macro-signals-from-today-s-earnings-target-tjx-and-lowe-s/)
- [Target Q3 press release](https://corporate.target.com/press/release/2026/11/target-corporation-reports-third-quarter-earnings)
- [Target 8-K exhibit (SEC)](https://www.sec.gov/Archives/edgar/data/0000027419/000002741926000051/a2026q3ex-99.htm)
- [CNBC: Target Q3](https://www.cnbc.com/2026/11/18/target-tgt-q3-2026-earnings.html)
- [Qz: Target Q3](https://qz.com/target-earnings-sales-growth-forecast-raised-111826)
- [Target Q4 2025 release date (Mar 3, 2026)](https://corporate.target.com/press/release/2026/03/target-corporation-reports-fourth-quarter-and-full-year-2025-earnings)
- [Wedbush TGT quote (52-week range)](https://investor.wedbush.com/wedbush/quote?Symbol=NY%3ATGT)
- [TIKR: Target up 60% in 2026](https://www.tikr.com/blog/target-stock-is-up-60-in-2026-wall-streets-average-target-now-sits-below-it)
- [Walmart earnings date](https://days.to/walmart-earnings)
- [TipRanks: Walmart earnings](https://www.tipranks.com/stocks/gb:0r1w/earnings)
- [Invezz: Lowe's falls despite beat](https://invezz.com/news/2026/11/18/lowes-stock-falls-4-despite-earnings-beat-as-tariff-refunds-lift-profit/)
- [CNBC movers Nov 18](https://www.cnbc.com/2026/11/18/stocks-moving-the-most-today-live-updates.html)
- [TradingKey: UNH falls on CMS CRUSH rule](https://www.tradingkey.com/analysis/stocks/us-stocks/262310909-unitedhealth-falls-cms-crush-audit-rule-unh-385-23-support-november-18-2026-tradingkey)
- [Heygotrade: UNH Nov 18](https://www.heygotrade.com/en/news/unitedhealth-unh-stock-news-november-18-2026/)
- [GuruFocus: Humana falls on CMS](https://www.gurufocus.com/news/9205492/humana-stocks-fall-424-as-cms-targets-9-billion-yearly-in-overpayments)
- [Trefis: FCX drop](https://www.trefis.com/stock/fcx/articles/625809/why-did-freeport-mcmoran-stock-fall-nearly-7/2026-11-17)
- [Rio Times: copper six-month low](https://riotimesonline.com/copper-markets-latam-tuesday-november-17-2026)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Thursday 2026-11-19. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,247.85**
- Cash: $140,670.03
- Session P&L so far: +0.26% (new entries are blocked at -3.0%)
- Gross exposure: $37,422 (36% of equity, cap 150%)
- Net exposure: $-37,422 (-36%, cap +/-100%)
- Risk at stake (entry to stop): $1,082 (1.05% of equity, cap 4.0%) — 2.95% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 345.91 | 340.16 | +345 (+1.7%) | -20% | 355.50 | 330.00 |
| HD | short | 51 | 343.57 | 333.58 | +509 (+2.9%) | -16% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **GLD**, opened 2026-11-18 (session 2 of at most 10), submitted with stop 359 and target 333, P 36%. Thesis: Gold is trending down on rising real rates and the strongest dollar in 18 months (-4.6% in 5 days, below its 20d and 50d averages). A US-session break below the overnight low (GLD 350.50, under its 352.91 20-day low) confirms the move toward the $3,800 and then ~$3,650 area. The stop entry stays unfilled if Warsh or the minutes turn dovish. Invalidation: DXY back below 102.50 with market-implied December-hike odds below 70%.
- **HD**, opened 2026-11-17 (session 3 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Your record

51 closed trades: 16W / 35L, total +0.37R, net $+2,410 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 51 | 18 | 30 | +0.01R |
| The same trades, bracket left alone | 51 | | | +0.03R |
| Ideas you passed on, or the caps dropped | 105 | 37 | 58 | +0.02R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 41 | 49% |
| 35%-40% | 70 | 29% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 38% of 143 brackets reached target first. Your Brier score is 0.239; saying 38% every time scores 0.237. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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
| GLD | 340.37 (08:49 sip) | -0.2% | 341.19 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| HD | 333.58 (08:49 sip) | -1.2% | 337.64 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 737.72 (08:58 iex) | +1.0% | 730.20 | 14.32 (2.0%) | 726.79-775.64 | -3.1% / -4.2% | -3.9% | 51.4M |
| QQQ | 671.70 (09:02 iex) | +1.8% | 659.51 | 19.71 (3.0%) | 646.64-726.14 | -3.9% / -7.7% | -4.5% | 51.8M |
| IWM | 271.40 (08:49 sip) | +0.5% | 270.12 | 5.84 (2.2%) | 267.87-286.17 | -2.8% / -3.3% | -4.6% | 24.2M |
| DIA | 504.23 (08:49 sip) | +0.5% | 501.73 | 8.81 (1.8%) | 500.03-536.60 | -3.5% / -3.1% | -4.3% | 3.8M |
| TLT | 80.11 (08:49 sip) | -0.1% | 80.22 | 0.73 (0.9%) | 79.11-82.42 | -0.9% / +0.6% | -0.9% | 36.4M |
| GLD | 340.37 (08:49 sip) | -0.2% | 341.19 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| USO | 138.71 (08:49 sip) | +1.9% | 136.11 | 5.75 (4.2%) | 135.01-171.82 | -10.9% / -10.7% | -3.8% | 5.1M |
| SMH | 471.16 (08:49 sip) | +2.5% | 459.54 | 28.70 (6.2%) | 445.32-571.00 | -8.9% / -16.9% | -9.4% | 12.1M |
| XLK | 167.11 (08:49 sip) | +2.0% | 163.81 | 6.73 (4.1%) | 159.63-191.55 | -6.5% / -11.8% | -6.1% | 13.3M |
| XLF | 56.53 (08:45 sip) | +0.2% | 56.42 | 1.06 (1.9%) | 55.74-60.04 | -1.5% / +0.9% | -3.8% | 35.6M |
| XLE | 61.60 (08:49 sip) | +0.5% | 61.29 | 1.81 (3.0%) | 60.43-70.15 | -6.3% / -5.4% | -3.3% | 37.1M |
| XLV | 180.57 (08:49 sip) | -0.3% | 181.17 | 3.73 (2.1%) | 177.07-192.32 | -1.9% / +3.0% | -4.1% | 12.0M |
| XLI | 165.65 (08:49 sip) | +0.6% | 164.66 | 3.56 (2.2%) | 161.74-172.40 | -1.7% / -2.2% | -3.7% | 8.9M |
| XLY | 119.77 (08:49 sip) | +0.5% | 119.20 | 2.79 (2.3%) | 112.83-122.92 | +1.2% / +4.5% | -1.5% | 9.2M |
| XLP | 90.43 (08:49 sip) | -0.8% | 91.18 | 1.67 (1.8%) | 86.36-93.48 | +1.1% / +6.0% | -0.3% | 20.0M |
| XLU | 43.50 (08:49 sip) | -0.1% | 43.55 | 0.60 (1.4%) | 42.01-44.40 | +0.4% / +4.0% | -0.6% | 23.9M |
| XLB | 50.41 (08:45 sip) | -0.1% | 50.46 | 1.09 (2.2%) | 50.12-54.63 | -3.3% / -0.7% | -4.8% | 12.2M |
| XLRE | 43.69 (08:40 sip) | +0.2% | 43.62 | 0.66 (1.5%) | 41.78-45.34 | -0.1% / +2.5% | -2.2% | 7.9M |
| XLC | 106.56 (08:49 sip) | +0.9% | 105.58 | 2.21 (2.1%) | 99.33-109.26 | +0.6% / -3.1% | -2.8% | 7.9M |
| KRE | 70.80 (08:10 sip) | +0.4% | 70.52 | 1.54 (2.2%) | 70.19-75.80 | -2.8% / -1.3% | -3.3% | 14.5M |
| XHB | 100.80 (08:20 sip) | +0.0% | 100.75 | 3.28 (3.3%) | 94.86-108.78 | -0.8% / +2.4% | -2.3% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 353.56 (08:49 sip) | +0.3% | 352.45 | 9.43 (2.7%) | 325.08-360.83 | +1.4% / +3.4% | -0.8% | 48.2M |
| MSFT | 515.07 (08:49 sip) | +1.5% | 507.31 | 17.88 (3.5%) | 495.55-558.07 | -3.4% / -2.2% | -2.5% | 28.2M |
| NVDA | 152.98 (09:05 iex) | +1.3% | 150.96 | 11.92 (7.9%) | 148.80-219.99 | -20.1% / -28.2% | -13.1% | 250.9M |
| AMZN | 272.19 (08:54 iex) | +1.7% | 267.74 | 11.00 (4.1%) | 229.36-275.34 | +4.1% / +4.9% | +0.6% | 50.4M |
| GOOGL | 293.88 (09:02 iex) | +4.1% | 282.44 | 9.50 (3.4%) | 276.92-331.43 | -4.2% / -13.1% | -3.8% | 42.4M |
| META | 623.00 (08:49 sip) | +1.1% | 616.38 | 20.75 (3.4%) | 583.80-681.07 | -1.4% / -9.3% | -2.0% | 22.4M |
| TSLA | 391.92 (09:02 iex) | +2.1% | 383.72 | 17.96 (4.7%) | 338.15-414.23 | -0.6% / +2.1% | -1.8% | 37.7M |
| AVGO | 361.80 (08:49 sip) | +2.2% | 354.05 | 20.97 (5.9%) | 289.77-369.82 | +6.6% / +2.9% | +2.6% | 28.3M |
| AMD | 536.98 (08:49 sip) | +1.3% | 530.14 | 50.16 (9.5%) | 402.10-594.00 | +3.0% / -4.5% | -4.1% | 37.5M |
| ORCL | 117.29 (09:03 iex) | +3.0% | 113.89 | 8.36 (7.3%) | 109.21-148.48 | -8.5% / -14.8% | -11.3% | 41.2M |
| NFLX | 60.02 (09:03 iex) | +0.3% | 59.82 | 1.85 (3.1%) | 59.41-67.82 | -5.3% / -12.2% | -7.3% | 40.6M |
| CRM | 190.27 (08:49 sip) | -0.1% | 190.40 | 8.49 (4.5%) | 186.45-252.42 | -15.1% / -18.0% | -12.7% | 7.2M |
| JPM | 326.79 (08:45 sip) | +0.8% | 324.11 | 8.50 (2.6%) | 323.71-359.80 | -4.2% / -4.2% | -5.6% | 6.6M |
| GS | 888.00 (08:49 sip) | +1.7% | 873.18 | 30.40 (3.5%) | 854.45-939.38 | -2.9% / -4.3% | -5.8% | 2.1M |
| BAC | 49.28 (08:49 sip) | +0.8% | 48.91 | 1.23 (2.5%) | 48.74-53.02 | -2.8% / -8.2% | -3.5% | 34.4M |
| XOM | 160.82 (08:49 sip) | +0.1% | 160.58 | 4.86 (3.0%) | 159.11-187.32 | -6.9% / -4.7% | -3.1% | 14.6M |
| CVX | 206.05 (08:49 sip) | +0.1% | 205.88 | 5.58 (2.7%) | 204.31-234.53 | -6.2% / -3.7% | -2.7% | 8.3M |
| LLY | 1,371.80 (08:59 iex) | -0.8% | 1,382.75 | 46.44 (3.4%) | 1,256.10-1,475.25 | +0.4% / +10.1% | -3.7% | 3.1M |
| UNH | 350.79 (08:49 sip) | +0.3% | 349.91 | 14.59 (4.2%) | 342.45-426.55 | -13.2% / -10.4% | -13.2% | 5.6M |
| JNJ | 270.55 (08:49 sip) | -0.8% | 272.70 | 7.08 (2.6%) | 259.04-290.25 | -0.7% / +2.0% | -2.7% | 7.6M |
| WMT | 125.36 (08:49 sip) | -1.6% | 127.36 | 3.09 (2.4%) | 117.83-131.82 | +2.2% / +10.0% | +1.3% | 22.3M |
| COST | 1,092.86 (08:40 sip) | -0.3% | 1,096.62 | 21.91 (2.0%) | 978.87-1,123.67 | +4.6% / +12.1% | +0.8% | 2.5M |
| HD | 333.58 (08:49 sip) | -1.2% | 337.64 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |
| CAT | 568.08 (08:49 sip) | +1.7% | 558.77 | 27.74 (5.0%) | 550.81-732.73 | -9.9% / -22.9% | -7.1% | 4.0M |
| BA | 164.32 (08:49 sip) | +0.9% | 162.91 | 4.74 (2.9%) | 161.75-193.19 | -6.1% / -12.4% | -6.7% | 10.5M |
| DAL | 85.21 (08:45 sip) | +0.4% | 84.88 | 3.24 (3.8%) | 75.33-92.52 | +0.4% / +3.3% | -7.1% | 6.0M |
| UAL | 107.27 (08:45 sip) | -0.3% | 107.63 | 5.50 (5.1%) | 96.39-122.08 | -1.2% / -0.4% | -9.1% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| PANW | 369.00 (08:49 sip) | +8.6% | 339.92 | 20.20 (5.9%) | 301.28-406.88 | -2.2% / -7.3% | +1.6% | 6.9M |
| ENTG | 153.99 (08:40 sip) | +7.1% | 143.78 | 12.29 (8.5%) | 124.14-170.06 | -0.3% / -2.6% | -6.8% | 3.8M |
| PDD | 81.86 (08:49 sip) | +5.7% | 77.45 | 2.57 (3.3%) | 76.27-85.42 | -2.5% / -2.3% | -2.0% | 5.8M |
| STX | 545.00 (08:49 sip) | +5.6% | 515.90 | 49.84 (9.7%) | 449.28-718.65 | -10.0% / -28.2% | -6.5% | 6.0M |
| CRWD | 250.09 (08:49 sip) | +5.5% | 237.03 | 15.15 (6.4%) | 213.22-272.29 | -0.9% / -3.6% | +3.5% | 9.2M |
| SNDK | 813.59 (09:03 iex) | +4.8% | 776.22 | 111.84 (14.4%) | 749.39-1,408.45 | -25.2% / -43.9% | -20.6% | 12.9M |
| WDC | 301.96 (08:49 sip) | +4.8% | 288.19 | 27.33 (9.5%) | 258.61-402.23 | -11.1% / -24.2% | -8.0% | 8.4M |
| NET | 314.60 (08:49 sip) | +4.5% | 300.91 | 23.53 (7.8%) | 233.62-337.00 | +1.4% / -6.0% | -4.5% | 4.4M |
| TTWO | 210.00 (08:49 sip) | -3.1% | 216.61 | 13.02 (6.0%) | 183.86-237.41 | +3.9% / +4.3% | -6.4% | 4.3M |
| BABA | 82.71 (08:59 iex) | -2.0% | 84.37 | 4.04 (4.8%) | 84.22-111.17 | -15.0% / -20.0% | -16.9% | 11.7M |
| NEM | 102.67 (08:49 sip) | -1.8% | 104.53 | 5.50 (5.3%) | 102.35-127.28 | -7.9% / -10.6% | -11.8% | 7.3M |
| SPOT | 597.00 (08:30 sip) | -1.5% | 605.84 | 20.99 (3.5%) | 536.75-635.00 | +2.0% / +10.7% | -0.5% | 1.8M |
| BMY | 58.73 (08:49 sip) | -1.4% | 59.56 | 1.92 (3.2%) | 59.48-65.54 | -4.2% / -3.1% | -5.3% | 10.3M |
| W | 107.90 (08:20 sip) | -1.3% | 109.35 | 7.07 (6.5%) | 105.17-127.99 | -3.7% / +1.3% | -4.4% | 2.1M |
| HCA | 470.18 (07:10 sip) | -1.3% | 476.35 | 17.31 (3.6%) | 439.83-521.48 | -1.9% / +4.0% | -5.9% | 1.5M |
| MDLZ | 65.73 (08:49 sip) | -1.3% | 66.56 | 1.63 (2.4%) | 61.51-68.92 | +1.6% / +6.1% | -0.2% | 8.3M |
