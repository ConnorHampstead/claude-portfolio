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

## Your last post-open review (2026-11-17)

*For continuity: what you were watching and why. The book state below is
current and overrides anything here.*

## Post-open review: Tuesday 2026-11-17, 10:05 ET / 16:05 Stockholm

I'm changing nothing and opening nothing new. All three brackets stay as submitted.

### 1. Since the open

- **The open:** stocks opened lower (CNBC, about 09:31: S&P −0.3%, Dow −0.6%). SPY is now 737.99 (−0.3%), QQQ 661.13 (−0.1%), DIA −0.6%.
- **Data printed since the morning:**
  - Import prices were hot at +1.1% against +0.7% expected (CNBC).
  - Industrial production fell 0.4% against +0.1% expected, mostly because utilities dropped 4.3%. Manufacturing output was a bit better than expected at +0.3% against +0.2%, and capacity utilisation was 76.4% against 76.8% (Fed G.17, via ANI and Rio Times).
  - NAHB came in at **25 against a 29 estimate**, down from 29, the lowest in over a year. That figure comes from one search snippet; I couldn't open the page.
- **The tape barely reacted:** TLT is −0.1% and XHB +0.4%.
- **Home Depot:** CNBC adds that HD's guidance implies Q4 adjusted EPS of $2.77 against $2.81 consensus. That fits the short thesis.
- **New since the morning:** software is selling off hard (CRM −6.9%, WDAY, INTU, MDB, TEAM, DOCU all about −5%), and managed care has fallen further (UNH −5.4%, HUM −5%). Neither move has a dated catalyst I could confirm.
- **Net change versus the morning:** nothing that touches the theses behind the open positions.

### 2. Fills, positions and resting entries

**HD short: filled at 343.57 (session 1 of 10). Keep.**
- It filled on the bounce to 346.75, not on a gap through the limit, so it carries its full planned risk.
- The invalidation is a close above 347.51. It hasn't happened: the high was 346.75 and the last trade is 342.85.
- The NAHB miss and the CNBC Q4 math fit the thesis.

**IWM short: session 6 of 10. Keep.**
- The invalidation is a close above 284, or the 2-year fully reversing its CPI move. Neither has happened: IWM is at 272.44.
- Today's low was 271.55, against the 271.00 target.

**GLD sell stop at 350.50: resting. Keep.**
- GLD is at 353.45, so the trigger is still below the market and below the 351.96 20-day low.
- The cancel condition (a trade above 362.00) hasn't happened; today's high was 354.92.

### 3. The morning's plans

- **HD:** the limit filled. The bracket stands, with no discretionary action, as planned.
- **IWM:** the target hasn't been reached. No action, as planned.
- **GLD:** above 362 didn't happen. The order stays resting.
- **Industrial production, Hammack and NAHB:** informational only. Nothing triggered.

### 4. New plays

None. Here is what I looked at:

- **CRM short.** It broke its 208.88 20-day low on heavy selling. The only explanation I found is generic: TradingKey cites "enterprise monetization skepticism" and sector rotation, with no named report, downgrade or Anthropic headline. A mover I can't explain is not a trade. CRM's next earnings date is about Dec 2, an estimate; I couldn't confirm it.
- **UNH short.** It is already down about 2 ATR (22 points against a 10.98 ATR) on the CRUSH proposal. Coverage is thin: GuruFocus and Seeking Alpha. Analysts still call the rule protracted and likely to be litigated. Shorting into the 388.00 20-day low after the move has happened offers no new edge.
- **Homebuilders on the NAHB miss.** XHB is up 0.4%, so the tape isn't trading the print. A short would also stack Consumer Discretionary on top of HD.
- **TLT on the hot import prices.** TLT is −0.1% and still above its 79.11 low. Nothing has changed the morning's reason to pass: it would be a third bet on the same rates factor.

### 5. Passing on

- **CRM short:** short at market about 200.11, stop 210.50 (above the 209.01 open and the broken 208.88 low, about 1.3 ATR), target 180.00 (1.94R). P 0.33, so the expected value is about −0.03R. No catalyst I could verify, and earnings land around the end of the 10-session window.
- **UNH breakdown short:** sell stop 387.50 (under the 388.00 20-day low), stop 400.50 (above today's 399.99 high), target 361.50 (2.0R). P 0.33, expected value about −0.01R. It is already down about 2 ATR and the thin sources say the rule will be litigated.

### 6. For tomorrow

- **NVDA tonight:** reports about 16:20 ET (22:20 Stockholm). The stops are the only protection overnight. A relief squeeze is the main risk to a book that is net −60% (−80% if GLD triggers).
- **HD:** close it only if it closes above 347.51, for example after a strong Lowe's print. Lowe's reports before the open Wednesday, with its call at 09:00 ET (15:00 Stockholm).
- **TLT:** worth re-examining tomorrow only if it closes below 79.11 and the 10-year holds above 5.12%, at a sell stop of 78.95 / stop 80.40 / target 76.80. It would still have to clear the concentration objection.
- **Anthropic:** prices its IPO tomorrow and lists Thursday. Watch whether software keeps selling into the listing before taking any CRM or IGV-type short; a dated reason would be needed.

**Book state:**
- **Exposure:** gross about 60% of the 150% cap; net about −60% of ±100%. Both count GLD as filled.
- **Risk at stake:** 1.48% of the 4% cap, with 3 of 8 slots used.

```json
{
  "date": "2026-11-17",
  "no_trade": true,
  "session_note": "Data mixed-to-soft (import prices hot +1.1%, IP -0.4%, NAHB 25 vs 29) with little reaction; HD filled at 343.57 on the planned retest, IWM and GLD unchanged. Software and managed-care moves lack a verifiable dated catalyst; would act on a CRM/software short only with a named, dated reason, or on TLT only after a close below 79.11.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "CRM",
      "direction": "short",
      "entry_type": "market",
      "entry": 200.11,
      "stop": 210.50,
      "targets": [180.00],
      "p_target_first": 0.33,
      "reason": "-6.9% through the 208.88 20d low, but no dated catalyst found (TradingKey cites only generic monetization skepticism and rotation); earnings ~Dec 2 (est.) near the end of the horizon. EV ~-0.03R."
    },
    {
      "ticker": "UNH",
      "direction": "short",
      "entry_type": "stop",
      "entry": 387.50,
      "stop": 400.50,
      "targets": [361.50],
      "p_target_first": 0.33,
      "reason": "CRUSH proposed rule extended the selloff to -5.4% (~2 ATR) after the open; breakdown under the 388.00 20d low, but the move is largely spent and analysts expect litigation. EV ~-0.01R."
    }
  ]
}
```

Sources:
- [CNBC live updates, Nov 17 (posted under the 11/16 URL)](https://www.cnbc.com/2026/11/16/stock-market-today-live-updates.html)
- [ANI: Fed industrial production October](https://www.aninews.in/news/business/us-industrial-production-declines-04-pc-in-october-manufacturing-output-rises-03-pc-federal-reserve20261117200440/)
- [Rio Times: US October industrial output](https://www.riotimesonline.com/united-states-industrial-production-october-2026/)
- [InvestingLive: industrial production −0.4% vs +0.1% (403; snippet only)](https://investinglive.com/news/us-october-industrial-production-0-4-vs-0-1-expected/)
- [InvestingLive: NAHB 25 vs 29 estimate (403; snippet only)](https://investinglive.com/news/nahb-housing-market-index-for-november-25-vs-29-estimate/)
- [RISMedia: NAHB October lowest in 14 years](https://www.rismedia.com/2026/10/19/nahb-reports-lowest-builder-confidence-in-14-years/)
- [TradingKey: CRM opened down 5% on Nov 17](https://www.tradingkey.com/news/market-movers/262309214-market-movers-crm-20261117)
- [24/7 Wall St.: Salesforce, Nov 17](https://247wallst.com/investing/2026/11/17/salesforce-is-more-than-30-below-its-december-2024-high-but-1000-from-a-decade-ago-is-still-worth-more-than-2500/)
- [Investing.com: CRM quote and next earnings (est.)](https://www.investing.com/equities/salesforce-com)
- [Trefis: Anthropic IPO and Salesforce/ServiceNow](https://www.trefis.com/stock/crm/articles/624620/is-the-anthropic-ipo-bad-news-for-salesforce-and-servicenow-stock/2026-11-12)
- [Seeking Alpha: managed care drops on proposed Medicare fraud crackdown](https://seekingalpha.com/news/4673627-managed-care-drops-proposed-crackdown-medicare-fraud)
- [GuruFocus: UNH dips premarket on CRUSH (403; snippet only)](https://www.gurufocus.com/news/9205170/unitedhealth-unh-shares-dip-premarket-amid-new-federal-healthcare-fraud-regulations)
- [Qz: Dow falls as Home Depot drops ahead of Nvidia (403; headline only)](https://qz.com/dow-falls-337-points-home-depot-nvidia-earnings-111726)
- [Chartmill: S&P 500 premarket movers, Nov 17 (403; snippet only)](https://chartmill.com/news/MPWR/Chartmill-58824-SP-500-Premarket-Movers-on-Nov-17-Gainers-and-Losers)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Wednesday 2026-11-18. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$103,327.25**
- Cash: $120,259.25
- Session P&L so far: +0.35% (new entries are blocked at -3.0%)
- Gross exposure: $37,962 (37% of equity, cap 150%)
- Net exposure: $-37,962 (-37%, cap +/-100%)
- Risk at stake (entry to stop): $1,016 (0.98% of equity, cap 4.0%) — 3.02% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| HD | short | 51 | 343.57 | 332.00 | +590 (+3.4%) | -16% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **HD**, opened 2026-11-17 (session 2 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 350.50 | stop | 359.00 | 333.00 | 2026-11-16 |

### Your record

50 closed trades: 16W / 34L, total +1.03R, net $+2,753 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 50 | 18 | 29 | +0.02R |
| The same trades, bracket left alone | 50 | | | +0.04R |
| Ideas you passed on, or the caps dropped | 101 | 36 | 55 | +0.03R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 40 | 48% |
| 35%-40% | 66 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 138 brackets reached target first. Your Brier score is 0.240; saying 39% every time scores 0.238. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | short | target | +1.67R | $+853 | 36% |
| AMZN | long | stop | -1.20R | $-303 | 36% |
| DAL | long | stop | -0.60R | $-154 | 37% |
| XLE | short | close | -1.02R | $-521 | 37% |
| AVGO | short | close | -0.92R | $-232 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| HD | 332.71 (08:45 sip) | -1.9% | 339.01 | 10.50 (3.1%) | 311.14-362.44 | +0.6% / +8.2% | -3.4% | 4.7M |
| GLD | 346.99 (08:49 sip) | -1.6% | 352.48 | 7.55 (2.1%) | 351.96-380.18 | -3.7% / -7.0% | -4.6% | 9.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 735.11 (08:49 sip) | +0.4% | 732.44 | 14.14 (1.9%) | 727.00-775.64 | -3.1% / -4.0% | -2.3% | 50.4M |
| QQQ | 661.84 (09:00 iex) | +0.7% | 656.95 | 20.01 (3.0%) | 646.64-727.95 | -4.7% / -8.2% | -2.6% | 51.2M |
| IWM | 268.56 (08:49 sip) | -0.2% | 269.05 | 5.81 (2.2%) | 267.87-286.17 | -3.3% / -3.8% | -4.1% | 23.9M |
| DIA | 507.46 (08:49 sip) | +0.0% | 507.31 | 8.57 (1.7%) | 505.29-536.60 | -2.6% / -2.1% | -2.8% | 3.7M |
| TLT | 79.77 (08:59 iex) | +0.3% | 79.55 | 0.74 (0.9%) | 79.11-82.42 | -1.7% / -0.2% | -1.6% | 36.1M |
| GLD | 346.99 (08:49 sip) | -1.6% | 352.48 | 7.55 (2.1%) | 351.96-380.18 | -3.7% / -7.0% | -4.6% | 9.7M |
| USO | 139.21 (08:49 sip) | -0.7% | 140.24 | 5.73 (4.1%) | 138.36-171.82 | -8.9% / -8.1% | -0.9% | 5.1M |
| SMH | 470.60 (08:49 sip) | +2.3% | 460.10 | 28.38 (6.2%) | 445.32-571.00 | -9.7% / -17.2% | -4.9% | 12.1M |
| XLK | 165.19 (08:45 sip) | +1.2% | 163.26 | 6.70 (4.1%) | 159.63-191.55 | -7.5% / -12.3% | -3.3% | 13.1M |
| XLF | 57.01 (08:49 sip) | -0.1% | 57.07 | 1.09 (1.9%) | 55.64-60.04 | -0.4% / +2.0% | -2.1% | 35.1M |
| XLE | 62.97 (08:49 sip) | -0.6% | 63.36 | 1.75 (2.8%) | 60.43-70.15 | -3.6% / -2.4% | +1.8% | 35.7M |
| XLV | 184.25 (08:49 sip) | -0.5% | 185.24 | 3.77 (2.0%) | 177.07-192.32 | +0.4% / +5.5% | -1.9% | 11.5M |
| XLI | 164.91 (08:45 sip) | +0.1% | 164.75 | 3.62 (2.2%) | 161.74-172.40 | -1.7% / -2.2% | -2.4% | 8.8M |
| XLY | 117.12 (08:10 sip) | +0.0% | 117.10 | 2.70 (2.3%) | 112.83-122.92 | -0.4% / +2.8% | -3.3% | 9.2M |
| XLP | 90.93 (08:45 sip) | -0.6% | 91.46 | 1.69 (1.9%) | 86.36-93.48 | +1.7% / +6.5% | +0.5% | 19.4M |
| XLU | 43.35 (08:49 sip) | -0.2% | 43.42 | 0.62 (1.4%) | 41.87-44.40 | +0.3% / +3.7% | -0.7% | 25.0M |
| XLB | 50.45 (08:45 sip) | -0.8% | 50.84 | 1.10 (2.2%) | 50.76-54.63 | -2.7% / -0.0% | -3.8% | 12.2M |
| XLRE | 43.55 (08:49 sip) | -0.1% | 43.59 | 0.70 (1.6%) | 41.78-45.34 | -0.0% / +2.5% | -2.2% | 7.9M |
| XLC | 105.40 (08:49 sip) | +0.1% | 105.26 | 2.33 (2.2%) | 99.33-109.88 | +0.2% / -3.5% | -2.3% | 8.1M |
| KRE | 70.78 (08:40 sip) | -0.1% | 70.85 | 1.57 (2.2%) | 70.15-75.80 | -2.3% / -0.9% | -3.1% | 14.4M |
| XHB | 98.40 (08:45 sip) | -0.7% | 99.09 | 3.30 (3.3%) | 94.81-108.78 | -2.2% / +0.8% | -4.0% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 351.05 (09:03 iex) | -0.2% | 351.91 | 9.62 (2.7%) | 325.08-360.83 | +1.4% / +3.5% | +1.1% | 48.2M |
| MSFT | 504.10 (09:03 iex) | -0.4% | 506.24 | 18.80 (3.7%) | 496.51-559.15 | -4.0% / -2.6% | -5.0% | 27.7M |
| NVDA | 159.94 (09:03 iex) | +2.9% | 155.46 | 11.49 (7.4%) | 148.80-222.19 | -19.3% / -26.6% | -8.0% | 237.8M |
| AMZN | 259.99 (09:04 iex) | +0.8% | 257.89 | 11.21 (4.3%) | 229.36-275.34 | +0.4% / +1.2% | -4.8% | 49.9M |
| GOOGL | 283.44 (09:03 iex) | +1.2% | 280.20 | 12.31 (4.4%) | 276.92-337.27 | -5.8% / -14.0% | -2.5% | 42.4M |
| META | 617.14 (09:04 iex) | -0.3% | 618.87 | 21.58 (3.5%) | 583.80-713.22 | -1.7% / -9.0% | -3.5% | 23.4M |
| TSLA | 383.73 (09:00 iex) | +1.0% | 380.11 | 17.65 (4.6%) | 338.15-414.23 | -1.6% / +1.2% | +0.1% | 38.8M |
| AVGO | 349.40 (09:03 iex) | +2.3% | 341.60 | 20.71 (6.1%) | 289.77-369.82 | +3.1% / -0.8% | +2.9% | 27.9M |
| AMD | 514.00 (08:49 sip) | +2.1% | 503.41 | 48.80 (9.7%) | 402.10-594.00 | -2.4% / -9.3% | -2.3% | 36.7M |
| ORCL | 117.12 (08:49 sip) | +1.8% | 115.00 | 8.64 (7.5%) | 109.21-148.48 | -8.2% / -14.6% | -2.5% | 41.7M |
| NFLX | 59.56 (08:49 sip) | -0.2% | 59.68 | 1.86 (3.1%) | 59.41-67.82 | -5.9% / -12.9% | -5.7% | 44.3M |
| CRM | 192.67 (08:49 sip) | -1.0% | 194.52 | 9.13 (4.7%) | 193.41-252.42 | -14.2% / -16.6% | -8.9% | 7.0M |
| JPM | 331.44 (08:45 sip) | +0.4% | 329.96 | 8.50 (2.6%) | 328.74-359.80 | -2.7% / -2.6% | -3.5% | 6.6M |
| GS | 886.00 (08:49 sip) | +1.0% | 877.52 | 30.50 (3.5%) | 854.45-939.38 | -2.6% / -4.2% | -3.6% | 2.1M |
| BAC | 49.45 (08:49 sip) | +0.0% | 49.44 | 1.26 (2.5%) | 49.08-53.02 | -2.0% / -7.7% | -2.4% | 34.2M |
| XOM | 166.36 (08:49 sip) | -0.5% | 167.21 | 4.63 (2.8%) | 159.11-187.32 | -3.5% / -0.8% | +2.3% | 14.3M |
| CVX | 213.12 (08:35 sip) | -0.6% | 214.35 | 5.24 (2.4%) | 204.31-234.53 | -2.7% / +0.2% | +2.3% | 8.2M |
| LLY | 1,406.35 (08:49 sip) | -0.6% | 1,415.55 | 51.93 (3.7%) | 1,256.10-1,475.25 | +3.2% / +13.1% | -1.0% | 3.1M |
| UNH | 388.95 (08:49 sip) | -0.2% | 389.68 | 11.96 (3.1%) | 387.14-426.55 | -4.1% / -0.4% | -3.8% | 5.0M |
| JNJ | 277.29 (08:49 sip) | -0.5% | 278.70 | 7.14 (2.6%) | 254.56-290.25 | +1.7% / +4.3% | -0.7% | 7.5M |
| WMT | 125.80 (08:45 sip) | -1.3% | 127.52 | 3.10 (2.4%) | 116.63-131.82 | +2.7% / +10.5% | +1.6% | 21.8M |
| COST | 1,104.91 (08:45 sip) | -0.5% | 1,110.08 | 21.62 (1.9%) | 978.87-1,123.67 | +6.4% / +14.0% | +4.1% | 2.5M |
| HD | 332.71 (08:45 sip) | -1.9% | 339.01 | 10.50 (3.1%) | 311.14-362.44 | +0.6% / +8.2% | -3.4% | 4.7M |
| CAT | 575.25 (08:49 sip) | +0.8% | 570.79 | 31.72 (5.6%) | 550.81-743.23 | -9.3% / -21.8% | -2.4% | 3.9M |
| BA | 164.17 (08:49 sip) | +0.2% | 163.91 | 5.07 (3.1%) | 163.30-193.28 | -6.3% / -12.3% | -5.5% | 10.5M |
| DAL | 84.78 (08:49 sip) | +0.6% | 84.30 | 3.25 (3.9%) | 75.33-92.52 | +0.1% / +2.8% | -8.6% | 6.2M |
| UAL | 106.82 (08:35 sip) | +0.4% | 106.35 | 5.53 (5.2%) | 96.24-122.08 | -2.1% / -1.6% | -11.8% | 5.7M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| TJX | 137.69 (08:55 iex) | +6.0% | 129.85 | 4.07 (3.1%) | 129.39-147.17 | -6.4% / -4.3% | -4.8% | 6.4M |
| TTWO | 213.81 (08:53 iex) | +4.8% | 203.93 | 12.03 (5.9%) | 183.86-237.41 | -2.0% / -1.8% | -9.2% | 3.8M |
| ROST | 228.00 (08:10 sip) | +3.4% | 220.45 | 8.24 (3.7%) | 219.06-249.30 | -5.3% / -4.7% | -7.7% | 2.1M |
| SMCI | 24.88 (08:49 sip) | +3.1% | 24.14 | 2.66 (11.0%) | 23.29-37.45 | -20.9% / -32.8% | -13.1% | 48.7M |
| DELL | 332.70 (08:49 sip) | +3.1% | 322.79 | 37.07 (11.5%) | 305.80-507.38 | -19.2% / -33.4% | -3.5% | 7.5M |
| TER | 241.03 (08:49 sip) | +2.9% | 234.18 | 23.31 (10.0%) | 211.63-351.95 | -13.7% / -30.6% | -4.6% | 4.5M |
| TSM | 370.00 (08:49 sip) | +2.9% | 359.69 | 21.05 (5.9%) | 351.19-440.88 | -10.8% / -15.8% | -9.3% | 15.5M |
| HPE | 47.40 (08:45 sip) | +2.8% | 46.09 | 3.79 (8.2%) | 43.38-62.20 | -11.7% / -21.2% | -3.8% | 14.7M |
| LOW | 209.00 (08:49 sip) | -5.2% | 220.46 | 7.33 (3.3%) | 194.43-235.00 | +2.1% / +10.3% | -4.9% | 3.5M |
| FCX | 53.15 (08:49 sip) | -3.9% | 55.30 | 3.10 (5.6%) | 54.73-68.94 | -11.1% / -18.2% | -8.3% | 12.8M |
| NEM | 108.00 (08:49 sip) | -2.9% | 111.26 | 5.09 (4.6%) | 104.51-127.28 | -2.5% / -5.2% | -7.3% | 7.1M |
| PGR | 229.99 (08:20 sip) | -2.0% | 234.67 | 5.05 (2.2%) | 219.59-241.02 | +1.7% / +6.3% | +1.3% | 2.3M |
| JD | 24.96 (08:49 sip) | -1.8% | 25.43 | 0.86 (3.4%) | 25.05-29.34 | -5.1% / -5.2% | -10.2% | 10.2M |
| NKE | 35.23 (08:49 sip) | -1.7% | 35.85 | 1.59 (4.4%) | 35.36-41.10 | -6.4% / -2.7% | -7.3% | 23.7M |
| AA | 36.66 (08:49 sip) | -1.6% | 37.27 | 1.66 (4.5%) | 37.11-42.14 | -5.9% / -11.2% | -6.8% | 4.5M |
| CMG | 35.31 (08:49 sip) | -1.5% | 35.83 | 1.28 (3.6%) | 27.31-36.69 | +9.6% / +10.3% | -0.3% | 20.2M |
