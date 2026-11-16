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

## Your last post-open review (2026-11-13)

*For continuity: what you were watching and why. The book state below is
current and overrides anything here.*

# Post-open review: Friday 2026-11-13, 10:05 ET / 16:05 Stockholm

**No changes and no new trades.** None of the open positions has met its invalidation, and none of this morning's triggers has fired. I found no confirmed news behind today's chip selloff, so it isn't a trade.

### 1. Since the open
- **Fade from the open:** stocks opened higher on the soft PPI and then turned down. SPY went from 760.07 to 752.43 (−0.6%), QQQ from 688.51 to 678.52 (−1.4%), and the Nasdaq is down about 1%.
- **Chips led the fall:** SMH −3.7%, AMD −8.2%, AVGO −5.4%, DELL −7.8%, AMAT −4.9% and NVDA −2.4%. Pre-market, AMD and AVGO were only about −2.5%.
- **Rates and the Fed:** the 10-year rose to about 5.15–5.16%, its highest since October (Yahoo, CNBC). CME FedWatch shows a December hike fully priced: about 87% for 25bp and 13% for 50bp (CNBC).
- **Gold and oil:** GLD is +0.4% at 356.19, in a 356.07–357.32 range. USO is +0.3%.
- **What changed versus the morning:** I couldn't confirm a dated reason for the chip move. Reports describe the selling spreading from the NVDA CEO exit, and AMD (+44.7%) and AVGO (+25%) are giving back big 5-day gains. That is my inference, not a sourced catalyst.
- **Fed remarks:** I couldn't find any report of what Collins (09:10) or Logan (09:40) said.

### 2. Fills, positions and resting entries

| Name | Invalidation happened? | Session | Decision |
|---|---|---|---|
| AMZN long, 274.10 (263.50 / 293.00) | **No.** QQQ is 678.52, well above its 647.05 20-day low. AMZN is 268.02. | 5 of 10 | Keep the bracket |
| DAL long, 89.50 (85.80 / 96.50) | **No.** Brent was about $95.9 this morning (ZeroHedge). Yahoo has WTI at $89.55 (+0.9%) and USO is +0.3%, which doesn't fit Brent at $100. I couldn't get a live Brent quote. | 2 of 10 | Keep the bracket |
| IWM short, 281.03 (287.00 / 271.00) | **No.** The 2-year was about 4.84% this morning, not 4.55%. I couldn't get a post-open 2-year quote, but the 10-year rose since then. IWM is 276.27, far from a close above 284. | 4 of 10 | Keep the bracket |
| GLD sell stop 352.40 (361.50 / 334.00) | Not filled: today's low is 356.07. The invalidation hasn't happened either: FedWatch shows the hike at 100%, and DXY was about 103 this morning (I couldn't verify a post-open level). | Resting | Keep. It clears before the weekend. |
| QQQ sell stop 646.50 (664 / 615) | Not filled: QQQ is 678.52, about 32 points above the trigger. | Resting | Keep. It clears before the weekend. |

No entry filled since the morning.

### 3. The morning's plans
- **GLD above 360 means cancel the sell stop:** not triggered. Today's high is 357.32, so the order stays.
- **DAL closes only on Brent above $100:** not triggered (about $96).
- **Logan at 09:40, no action on IWM:** as planned. I found no report of her remarks.
- **CSCO stays in the shadow book:** the stock fell to 96.00, so the shadow 97.50 limit has filled. No live action.

### 4. New plays
None.

I looked hardest at a semiconductor short. The chip names are reversing hard after a sharp 5-day run, but:
- I found no dated catalyst at a source.
- AMD is already down about 1.1 ATR today.
- NVDA reports Tue Nov 17, inside the holding window. About 20% of SMH is NVDA, so that report is effectively a binary event for the fund.

I also rechecked NU (+7.1%, 12.68). The open answered the morning's question about which way the market read the results. But the numbers themselves are still mixed:
- Benzinga says revenue beat and EPS was in line. Investing.com says both missed.
- Non-performing loans rose to 7.3% from 6.9%.
- The strong dollar works against Brazilian assets.

It stays at conviction 2. The morning's shadow entry at 12.37 filled at the 12.36 open and is already being scored, so I'm not adding a second version.

### 5. Passing on
- **SMH short** at 483.12 market, stop 512.00 (above the 501.73 prior close and the 500.27 open high, 1.1 ATR), target 446.00 (just above the 445.59 20-day low). That is 1.29R at P 0.35, so EV is −0.20R. There is no verified catalyst and NVDA's earnings fall inside the window. Logged in `passed`.
- **AMD and AVGO shorts:** no dated catalyst, and shorting into strong uptrends after one red day. No levels.
- **DELL −7.8%:** no dated reason found. Next earnings are Nov 24 after the close (from one data site; I didn't see Dell's own announcement). No levels.
- **APP +3.9% to a 20-day high:** I found no catalyst for today. A mover I can't explain is not a trade.
- **TLT short:** TLT is 79.34, close to its 79.01 20-day low. The morning's pass stands for the same reason: it doubles the rates exposure IWM already carries.

### 6. For tomorrow
The next brief is Monday Nov 16, because both sell stops clear tonight before the weekend.
- **GLD:** re-place the short only if Friday closes below 354.67 with DXY above 102.85, or set a new-low sell stop under the 20-day low again.
- **QQQ:** re-place the 646.50 sell stop only if QQQ closes below about 670. That would mean today's fade carried through the close.
- **Open positions:** all three carry their brackets through the weekend unchanged.
- **Monday's research:** check Brent against $100 for DAL and the 2-year against 4.55% for IWM. NVDA reports Tue Nov 17, which touches the AMZN long and the QQQ idea; it is not AMZN's own event.

**Book state:** gross is 73% of the 150% cap and net −48% of ±100%, both counting the two resting entries. Risk at stake is 1.99% of the 4% cap, with 5 of 8 slots used. After tonight's weekend clearing it drops to 3 positions.

```json
{
  "date": "2026-11-13",
  "no_trade": true,
  "session_note": "Gap-up faded into a chip-led selloff (SMH -3.7%, AMD -8%) with the 10y at ~5.15% and a Dec hike fully priced; no invalidations met, no morning trigger fired, and no verified catalyst behind the semis move. Would act Monday on a GLD close under 354.67 with DXY above 102.85, or a QQQ close under ~670 to re-arm the 646.50 breakdown stop.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "market",
      "entry": 483.12,
      "stop": 512.00,
      "targets": [446.00],
      "p_target_first": 0.35,
      "reason": "Intraday chip reversal after a +12% 5-day run, but no dated catalyst found at a source, already ~0.7 ATR down on the day, and NVDA (~20% weight) reports Nov 17 inside the horizon; 1.29R at P 0.35 is EV about -0.20R."
    }
  ]
}
```

Sources:
- [Yahoo Finance live, Nov 13](https://finance.yahoo.com/markets/live/stock-market-today-friday-november-13-dow-sp-500-nasdaq-nvidia-110151154.html)
- [CNBC live updates](https://www.cnbc.com/2026/11/12/stock-market-today-live-updates.html)
- [StockTitan live, Nov 13](https://www.stocktitan.net/articles/stock-market-today-live-november-13-2026)
- [ZeroHedge: futures rise as Wall Street moves on from Jensen](https://www.zerohedge.com/markets/futures-rise-wall-street-moves-jensen-microsoft-outage-drags-day-two)
- [Invezz: AMD, Broadcom fall as Nvidia rebounds](https://invezz.com/news/2026/11/13/amd-broadcom-stocks-fall-2-as-nvidia-rebounds-is-wall-street-switching-sides/)
- [24/7 Wall St: memory stocks slide on the NVIDIA shake-up](https://247wallst.com/investing/2026/11/12/sandisk-micron-and-sk-hynix-slide-3-as-nvidia-shake-up-hits-memory-stocks/)
- [Blockonomi: CoreWeave, Dell, Super Micro slide](https://blockonomi.com/todays-market-movers-coreweave-dell-and-super-micro-slide-as-nvidia-board-weighs-huangs-exit/)
- [Benzinga: Nu Holdings Q3, EPS in line, revenue above estimates](https://www.benzinga.com/markets/earnings/26/11/63225298/nu-holdings-reports-strong-q3-eps-in-line-revenue-above-estimates)
- [Investing.com: Nu misses Q3 estimates, stock rises](https://in.investing.com/news/stock-market-news/earnings-call-transcript-nu-holdings-misses-q3-2026-estimates-stock-rises-93CH-5701370)
- [BigGo: Nu record profit despite revenue miss](https://finance.biggo.com/news/057eb7ff-0bab-45f3-a054-53d3a852a1e6)
- [Arincen: DELL earnings date](https://en.arincen.com/instruments/DELL/earnings)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **09:05 ET** (14:05 UTC, 15:05 Stockholm), Monday 2026-11-16. The cash session opens at 09:30 ET (15:30 Stockholm), in 25 min, and closes at 16:00 ET (22:00 Stockholm). Anything scheduled before 09:05 ET today has already been released: look up the actual figure and the market's reaction, not the consensus.
- Equity: **$102,239.78**
- Cash: $113,476.11
- Session P&L so far: +0.00% (new entries are blocked at -3.0%)
- Gross exposure: $35,711 (35% of equity, cap 150%)
- Net exposure: $-11,236 (-11%, cap +/-100%)
- Risk at stake (entry to stop): $1,017 (1.00% of equity, cap 4.0%) — 3.00% left for new plays
- Slots: 3 open + 0 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 263.81 | -247 (-3.8%) | +6% | 263.50 | 293.00 |
| DAL | long | 69 | 89.50 | 85.59 | -270 (-4.4%) | +6% | 85.80 | 96.50 |
| IWM | short | 85 | 281.03 | 276.16 | +414 (+1.7%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **AMZN**, opened 2026-11-09 (session 6 of at most 10), submitted with stop 263.5 and target 293, P 36%. Thesis: Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong relative signal. Invalidation: QQQ breaking its 20-day low while AMZN falls back inside the range.
- **DAL**, opened 2026-11-12 (session 3 of at most 10), submitted with stop 85.8 and target 96.5, P 37%. Thesis: Falling jet fuel is a direct margin tailwind. Buy the retest of the 89.92 20-day-high breakout rather than chase the gap. Invalidation: Brent back above $100.
- **IWM**, opened 2026-11-10 (session 5 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.

### Your record

47 closed trades: 15W / 32L, total +1.17R, net $+2,358 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 47 | 17 | 27 | +0.02R |
| The same trades, bracket left alone | 47 | | | +0.06R |
| Ideas you passed on, or the caps dropped | 94 | 34 | 51 | +0.06R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 36 | 50% |
| 35%-40% | 61 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 40% of 129 brackets reached target first. Your Brier score is 0.242; saying 40% every time scores 0.239. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLE | short | close | -1.02R | $-521 | 37% |
| AVGO | short | close | -0.92R | $-232 | 37% |
| NVDA | short | target | +2.16R | $+1,108 | 37% |
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AMZN | 263.60 (08:49 sip) | -1.1% | 266.66 | 10.74 (4.0%) | 229.36-275.34 | +3.6% / +4.6% | +2.8% | 50.1M |
| DAL | 85.80 (08:45 sip) | -0.5% | 86.25 | 3.30 (3.8%) | 74.14-92.52 | +3.6% / +5.4% | -1.1% | 6.6M |
| IWM | 276.17 (08:49 sip) | -0.5% | 277.54 | 5.46 (2.0%) | 270.23-286.17 | -0.3% / -1.1% | +1.4% | 23.4M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| SPY | 749.25 (08:49 sip) | -0.7% | 754.37 | 12.77 (1.7%) | 732.71-775.64 | -0.6% / -1.3% | +2.6% | 47.0M |
| QQQ | 670.81 (09:02 iex) | -1.3% | 679.89 | 18.61 (2.7%) | 647.05-727.95 | -2.2% / -5.3% | +3.6% | 49.6M |
| IWM | 276.17 (08:49 sip) | -0.5% | 277.54 | 5.46 (2.0%) | 270.23-286.17 | -0.3% / -1.1% | +1.4% | 23.4M |
| DIA | 522.24 (08:49 sip) | -0.2% | 523.15 | 7.61 (1.5%) | 508.66-536.60 | +0.2% / +0.8% | +2.1% | 3.6M |
| TLT | 79.46 (09:00 iex) | +0.1% | 79.38 | 0.76 (1.0%) | 79.01-82.42 | -1.9% / -0.6% | -3.1% | 35.8M |
| GLD | 354.40 (08:49 sip) | -0.3% | 355.45 | 7.60 (2.1%) | 352.91-381.93 | -3.6% / -6.7% | -4.6% | 9.3M |
| USO | 143.45 (08:49 sip) | -1.5% | 145.58 | 5.67 (3.9%) | 138.47-171.82 | -6.7% / -4.7% | -1.9% | 5.4M |
| SMH | 467.85 (08:49 sip) | -3.9% | 486.75 | 27.23 (5.6%) | 445.59-571.00 | -6.1% / -13.0% | +4.9% | 11.8M |
| XLK | 166.68 (08:49 sip) | -2.1% | 170.28 | 6.27 (3.7%) | 162.14-191.55 | -4.7% / -9.0% | +3.4% | 12.5M |
| XLF | 58.70 (08:49 sip) | +0.0% | 58.68 | 1.01 (1.7%) | 55.03-60.04 | +2.8% / +4.9% | +2.7% | 32.9M |
| XLE | 64.47 (08:49 sip) | -0.8% | 64.96 | 1.71 (2.6%) | 60.43-70.15 | -1.8% / +0.1% | +5.4% | 36.4M |
| XLV | 190.60 (08:49 sip) | +0.9% | 188.85 | 3.70 (2.0%) | 175.27-192.32 | +2.8% / +8.0% | +2.2% | 11.1M |
| XLI | 167.51 (08:00 sip) | -0.8% | 168.78 | 3.38 (2.0%) | 161.74-172.40 | +0.6% / -0.1% | +3.8% | 8.7M |
| XLY | 119.91 (05:10 sip) | -0.1% | 119.98 | 2.56 (2.1%) | 112.67-122.92 | +2.3% / +5.5% | +2.0% | 9.0M |
| XLP | 93.09 (08:45 sip) | +0.8% | 92.35 | 1.64 (1.8%) | 86.36-93.40 | +3.2% / +8.0% | +2.5% | 19.0M |
| XLU | 44.22 (08:49 sip) | +0.4% | 44.04 | 0.60 (1.4%) | 41.28-44.14 | +2.2% / +5.3% | +2.1% | 25.0M |
| XLB | 52.10 (08:45 sip) | -0.2% | 52.23 | 1.03 (2.0%) | 50.61-54.63 | -0.0% / +2.7% | +0.5% | 11.9M |
| XLRE | 44.46 (08:49 sip) | +0.2% | 44.37 | 0.69 (1.6%) | 41.60-45.34 | +2.2% / +4.3% | +0.8% | 7.9M |
| XLC | 109.08 (08:05 sip) | +0.4% | 108.69 | 2.16 (2.0%) | 99.33-110.84 | +3.0% / -0.6% | +3.7% | 7.9M |
| KRE | 72.68 (08:45 sip) | -0.1% | 72.74 | 1.54 (2.1%) | 69.17-75.80 | +0.5% / +1.5% | +0.7% | 13.9M |
| XHB | 101.46 (08:49 sip) | -0.6% | 102.07 | 3.26 (3.2%) | 94.05-108.78 | +1.2% / +3.7% | -0.2% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| AAPL | 357.47 (08:56 iex) | +0.3% | 356.27 | 9.45 (2.7%) | 325.08-360.83 | +3.0% / +5.2% | +4.1% | 47.4M |
| MSFT | 524.75 (08:49 sip) | +0.2% | 523.88 | 17.55 (3.4%) | 504.96-559.15 | -1.0% / +0.9% | -1.3% | 26.5M |
| NVDA | 156.97 (08:56 iex) | -3.6% | 162.85 | 11.00 (6.8%) | 148.80-222.19 | -18.0% / -24.1% | -12.7% | 209.6M |
| AMZN | 263.60 (08:49 sip) | -1.1% | 266.66 | 10.74 (4.0%) | 229.36-275.34 | +3.6% / +4.6% | +2.8% | 50.1M |
| GOOGL | 294.01 (08:49 sip) | -0.6% | 295.77 | 11.91 (4.0%) | 276.92-346.58 | -2.5% / -9.9% | +3.9% | 41.0M |
| META | 639.40 (08:49 sip) | -0.4% | 641.69 | 20.96 (3.3%) | 583.80-713.22 | +0.7% / -5.6% | +5.2% | 23.8M |
| TSLA | 385.38 (08:51 iex) | -1.2% | 390.22 | 18.16 (4.7%) | 338.15-414.23 | +1.3% / +4.1% | +8.9% | 39.7M |
| AVGO | 332.03 (09:02 iex) | -4.3% | 347.01 | 20.25 (5.8%) | 289.77-369.82 | +4.8% / +0.5% | +18.2% | 26.9M |
| AMD | 501.56 (08:49 sip) | -6.1% | 534.06 | 47.88 (9.0%) | 402.10-594.00 | +2.9% / -3.7% | +18.9% | 34.7M |
| ORCL | 121.17 (08:49 sip) | -3.3% | 125.35 | 9.46 (7.5%) | 109.21-148.48 | -1.0% / -8.1% | +8.0% | 42.0M |
| NFLX | 62.60 (08:49 sip) | +0.7% | 62.15 | 1.75 (2.8%) | 61.39-70.66 | -3.4% / -10.2% | -2.0% | 45.8M |
| CRM | 217.20 (08:49 sip) | -0.3% | 217.84 | 8.28 (3.8%) | 208.88-252.42 | -5.5% / -7.4% | +2.0% | 6.8M |
| JPM | 346.02 (08:49 sip) | -0.0% | 346.19 | 7.78 (2.2%) | 330.40-359.80 | +2.1% / +1.9% | +3.5% | 6.4M |
| GS | 905.60 (08:20 sip) | -1.2% | 916.56 | 28.97 (3.2%) | 854.45-939.38 | +1.8% / -0.6% | +5.9% | 2.0M |
| BAC | 50.89 (08:49 sip) | -0.3% | 51.02 | 1.17 (2.3%) | 49.17-53.02 | +1.0% / -5.6% | +3.2% | 35.2M |
| XOM | 168.69 (08:49 sip) | -0.5% | 169.52 | 4.75 (2.8%) | 159.11-187.32 | -2.7% / +0.7% | +2.8% | 14.2M |
| CVX | 218.79 (08:45 sip) | -0.5% | 219.89 | 5.30 (2.4%) | 206.01-236.48 | -1.4% / +2.0% | +3.4% | 8.3M |
| LLY | 1,453.86 (08:49 sip) | +0.7% | 1,443.50 | 50.97 (3.5%) | 1,237.60-1,458.23 | +6.6% / +16.4% | +6.7% | 3.0M |
| UNH | 410.58 (08:49 sip) | +0.8% | 407.46 | 10.81 (2.7%) | 388.00-426.55 | -0.1% / +4.2% | +3.4% | 4.9M |
| JNJ | 289.58 (08:49 sip) | +1.3% | 285.75 | 7.13 (2.5%) | 251.50-288.11 | +5.2% / +7.1% | +3.5% | 7.5M |
| WMT | 129.33 (09:00 iex) | +1.0% | 128.09 | 3.02 (2.4%) | 116.63-131.82 | +3.9% / +11.8% | +2.0% | 21.8M |
| COST | 1,109.90 (08:49 sip) | +0.3% | 1,106.21 | 21.67 (2.0%) | 978.87-1,109.50 | +7.2% / +14.5% | +5.0% | 2.4M |
| HD | 348.61 (08:49 sip) | -0.0% | 348.69 | 9.94 (2.9%) | 306.00-362.44 | +4.5% / +11.7% | +1.5% | 4.4M |
| CAT | 586.25 (08:45 sip) | -2.3% | 600.20 | 31.68 (5.3%) | 550.81-743.23 | -6.9% / -18.8% | +7.4% | 3.8M |
| BA | 169.82 (08:49 sip) | -1.0% | 171.50 | 6.10 (3.6%) | 165.01-193.28 | -3.5% / -9.2% | -1.1% | 10.5M |
| DAL | 85.80 (08:45 sip) | -0.5% | 86.25 | 3.30 (3.8%) | 74.14-92.52 | +3.6% / +5.4% | -1.1% | 6.6M |
| UAL | 108.00 (08:49 sip) | -1.2% | 109.31 | 5.42 (5.0%) | 94.54-122.08 | +1.8% / +1.1% | -3.0% | 5.7M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|
| HUBS | 224.33 (08:40 sip) | +3.3% | 217.25 | 14.11 (6.5%) | 188.25-271.60 | -6.2% / -4.4% | +8.3% | 1.4M |
| HSY | 177.96 (08:49 sip) | +3.0% | 172.82 | 5.52 (3.2%) | 158.55-178.33 | +2.1% / +3.6% | -2.1% | 2.0M |
| TTWO | 234.44 (08:49 sip) | +2.9% | 227.82 | 9.82 (4.3%) | 183.86-237.41 | +9.7% / +9.6% | +6.0% | 3.3M |
| CNC | 73.13 (08:49 sip) | +2.6% | 71.27 | 3.78 (5.3%) | 64.85-78.08 | +2.1% / +6.3% | +2.2% | 5.8M |
| HUM | 459.72 (08:45 sip) | +2.2% | 450.00 | 17.39 (3.9%) | 399.35-451.04 | +6.2% / +10.3% | +3.7% | 1.6M |
| GIS | 34.90 (08:40 sip) | +1.7% | 34.32 | 1.08 (3.1%) | 32.37-37.02 | +0.3% / +1.1% | -3.4% | 8.3M |
| NEE | 86.47 (08:30 sip) | +1.6% | 85.12 | 1.79 (2.1%) | 77.93-90.04 | +1.7% / +5.3% | -2.1% | 13.4M |
| MNST | 47.18 (08:49 sip) | +1.6% | 46.46 | 1.31 (2.8%) | 43.93-49.50 | -0.2% / +3.8% | +1.6% | 9.7M |
| MSTR | 102.13 (08:55 iex) | -8.5% | 111.62 | 8.46 (7.6%) | 108.25-155.69 | -16.8% / -22.1% | -13.4% | 17.3M |
| COIN | 117.95 (08:54 iex) | -7.6% | 127.64 | 9.43 (7.4%) | 125.38-180.60 | -15.1% / -25.1% | -5.3% | 8.3M |
| SNDK | 828.35 (09:01 iex) | -6.4% | 885.01 | 113.94 (12.9%) | 803.97-1,424.48 | -21.3% / -38.6% | +6.0% | 12.0M |
| STX | 498.00 (08:49 sip) | -5.7% | 528.29 | 54.47 (10.3%) | 449.28-718.65 | -11.8% / -28.7% | +14.6% | 6.1M |
| MRVL | 147.86 (08:49 sip) | -5.7% | 156.76 | 18.49 (11.8%) | 132.54-253.66 | -19.5% / -31.6% | +11.0% | 30.2M |
| HOOD | 73.45 (08:49 sip) | -5.7% | 77.86 | 5.08 (6.5%) | 75.51-103.15 | -11.9% / -24.6% | -3.8% | 19.1M |
| WDC | 279.29 (08:49 sip) | -5.5% | 295.65 | 28.37 (9.6%) | 258.61-402.23 | -12.1% / -24.5% | +12.1% | 8.9M |
| MU | 736.23 (09:02 iex) | -5.4% | 778.31 | 64.86 (8.3%) | 650.00-990.00 | -7.1% / -17.5% | +12.8% | 30.7M |
