Produce the post-open review.

The cash session has been open for about 35 minutes. This morning's pre-market
brief is below, followed by the live book and market data, which now include
today's opening prices. This is the second and last decision point of the day:
after this review, nothing looks at the book until tomorrow's pre-market brief.

What this session is for:

- **Fills at the open.** Check every entry that filled since the morning. An
  entry that filled on a gap through its limit sits closer to its stop than
  planned: it risks less than it was sized for, which is not a reason to close
  it. Close it through `manage` only if what caused the gap is the invalidation
  you wrote this morning. Otherwise its bracket stands.
- **Open positions.** The same test as the morning: closed only on the recorded
  invalidation, its own binary event before tomorrow's brief, or its tenth
  session. No stop is tightened.
- **The morning's plans for this review.** The 08:30 and 10:00 ET data have
  printed and the opening range is set. For each thing the morning brief said it
  would decide after the open or after the data, decide now: act, or say why not.
- **Resting entries** the open has made stale: amend or cancel them.
- **New plays**, under the same rules as the morning, pass-2 research
  included. Orders now go into a trading market: a limit at or through the last
  price fills immediately, and a `market` entry is sized from the last price.

Do not re-trade the morning's reasoning without new information. Reversing a
morning call needs something that happened since it was written: a print, a
headline, or what the open did. Everything in the morning's rules still binds:
search before you write, verified prices only (the market data table counts),
prose alone moves nothing, risk tiers, caps. If the morning's plan stands
unchanged, say so in a few lines and emit the JSON with empty arrays.

Keep the review short:

### 1. Since the open
Two or three sentences: what printed, how the market opened, and what changed
versus the morning brief.

### 2. Fills, positions and resting entries
Each position: keep, or close and which of the three conditions applies. Each
resting entry: keep, amend or cancel, and why.

### 3. The morning's plans
Each plan the morning left for this review: acted on, not triggered, or dropped.
One line each.

### 4. New plays
The same table as the pre-market brief.

### 5. Passing on
One line each. Ideas with real levels also go in the `passed` array, where they
are scored.

### 6. For tomorrow
Any level or condition you would act on tomorrow. Tomorrow's pre-market brief is
shown this review. "None" is fine.

Then the JSON block, in the same schema as the morning.

Your probability estimates are scored against outcomes, on the bracket as you
submit it. Start from the base rate in "Your record" and move off it only for
reasons you name.

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

## This morning's pre-market brief

# Pre-market brief: Wednesday 2026-11-11

*09:05 ET / 15:05 Stockholm. The offset is ET+6 today. The cash session opens 09:30 ET / 15:30 Stockholm. The US bond market is closed for Veterans Day; stocks trade normal hours.*

## 1. Tape

**Tuesday (verified):** October CPI came in hot, 0.4% headline and 0.3% core month on month (BLS, 08:30 ET Nov 10). The S&P fell 0.38% to 7,520.93, the Nasdaq Composite 0.74% and the Russell 2000 0.68%. The 2-year rose about 17–18bp to about 4.73%, its largest daily rise since April 2025. The 10-year rose 11–12bp to about 4.98–4.99% and briefly traded above 5%. Tuesday's 10-year auction drew the weakest demand since June. Markets now fully price a December hike plus two more by June (Saxo); FedWatch has the December hike at about 90%.

**Overnight:** CoreWeave reported Q3 after Tuesday's close:
- revenue $3.66B (+168%), above its own $3.45–3.60B guide;
- 2026 revenue outlook raised to $13.0–13.3B;
- backlog $132.5B;
- no new parent-level unsecured debt planned "at current yields".

That eased the AI-demand and AI-debt fears behind last week's selloff. Nasdaq-100 futures are +1.9%, S&P +0.8–0.9%, Dow +0.1%. Asian chips rallied (Taiex +3.6%, TSMC October revenue +59.7%). Pre-market, AI hardware is +7–9% (STX, MRVL, WDC, SNDK, MU, DELL) and defensives are lower (XLV −0.7%, XLP −0.6%, WMT −0.9%). The VIX closed at 19.46. Brent is about $92.5–92.8, up on overnight tanker incidents after a sub-$90 low on Tuesday. The dollar rebounded hard on CPI. Gold is about $4,055–4,060, back from a test of $4,000.

**Regime:** hawkish rates, with an AI relief rally on top and money rotating out of defensives. For today's session the edge is on the long side. For a 1–5 day bracket, though, the names that carry the catalyst have already moved 0.7–1.0 ATR before the open.

## 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| All day | All day | US cash Treasuries closed (Veterans Day) | No bond price discovery today; the 2y and 10y reopen Thursday | IWM, GLD, QQQ |
| 07:00 | 13:00 | MBA mortgage applications | Released; **couldn't verify** the figure. The last verified 30y rate was 7.30% (week to Oct 30, single secondary source) | IWM (rates) |
| Today, time unverified | — | OPEC monthly report; ECB's Lagarde speaks | Couldn't verify content | XLE, DAL |
| After 16:00 | After 22:00 | CTVA, FNV earnings | — | FNV is a small read for GLD |
| Thu 08:30 | 14:30 | Initial jobless claims | Cons. about 191–195k (prior 189k) | All |
| Thu 10:00 | 16:00 | Existing home sales (Oct) | — | IWM |
| Thu 12:00 | 18:00 | EIA crude inventories (moved back a day) | — | XLE, DAL |
| Thu 13:00 | 19:00 | $22B 30-year bond auction | After Tuesday's weak 10-year, a tail would push long yields higher | IWM, GLD, QQQ |
| Thu after close | Thu 22:00+ | CSCO, AMAT earnings | — | QQQ, AMZN (tech mood) |
| Fri 08:30 | 14:30 | October PPI | Cons. +0.4% m/m, about 6.6% y/y | All |
| Tue Nov 17, 17:00 | 23:00 | NVDA Q3 FY27 earnings (company release, Oct 28) | — | QQQ, the AI complex |
| Dec 8–9 | — | FOMC | A 25bp hike is fully priced, 50bp about 13–15% | All |

## 3. Open positions and resting entries

- **AMZN long** (274.10, stop 263.50, target 293), session 3 of 10. Invalidation: QQQ breaks its 20-day low (647.05) *and* AMZN falls back inside its range. QQQ is at 687.85, 41 points above that low. **Not met. Hold.**
- **IWM short** (281.03, stop 287, target 271), session 2 of 10. Invalidation: the 2-year fully reverses its CPI move, or IWM closes above 284. The 2-year closed Tuesday about 17bp *higher* and cash Treasuries are shut today. IWM closed Tuesday at 280.58. **Not met. Hold.** Pre-market is 283.10 (+0.9%); a close above 284 today would be checked at tomorrow's brief.
- **XLE short** (60.56, stop 63.10, target 57.30), session 2 of 10. Invalidation: Brent back above $93, or a renewed Iran escalation headline.
  - Brent is 92.5–92.8, still below $93 (Investrade, Saxo).
  - On Iran, the Iranian army says another tanker hit a mine overnight in the eastern Strait of Hormuz (Trend.Az, Nov 11), and UKMTO reported a tanker hit by a projectile on Tuesday evening. These continue a run of tanker incidents that started before entry (IRGC strikes on three tankers on Nov 8). Saxo reports signs that further strikes on Iran are unlikely.
  - My judgment, flagged as such: this is not a *renewed* escalation. **Not met. Hold.**
  - XLE is 62.97 pre-market, 0.13 below the stop, so the bracket will probably fire on the open. That is what the stop is for. Closing by hand would save about $28 and contradict the record on hand closes.
- **GLD short limit 374 (stop 382, target 358): keep.** GLD is 369.80. The case for selling a bounce got stronger on Tuesday: a December hike is now fully priced plus two more, and the dollar rebounded. The limit sits about 0.55 ATR above the market, near gold's $4,100–4,155 resistance.
- **DAL long limit 89.50 (stop 85.80, target 96.50): keep.** DAL is 91.38. Brent is up about $1.30 today but still about 22% below its late-October $118 high. The retest-of-breakout entry still describes the trade.
- **QQQ sell stop 646.50 (stop 664, target 615): keep.** It only goes live on a break of the 20-day low, 41 points down, and the harness clears it before the weekend.

## 4. New plays

**None.** Reasons specific to today:

1. **The AI longs carry the catalyst but have already moved most of it.**
   - SMH +4.5% against a 5.3% ATR; AVGO +4.3% against 5.2%; MU +6.8% against 8.4%; ORCL +4.9% against 7.4%.
   - Each would need a stop more than 1 ATR away, under a gap that has already run.
   - On a 40% base rate with about 1.6–2.0R available, every version I priced came out between −0.04R and +0.01R.
   - The complex's next real test is fixed and close: AMAT and CSCO on Thursday, NVDA on Nov 17.
2. **The rate-sensitive short failed its check.** XLRE fell only 0.13% on Tuesday while the 10-year rose 11bp. The market is not trading REITs on rates right now. That idea is conviction 2.
3. **The book already carries the rates view.** It has the IWM short, the GLD short limit and the QQQ breakdown trigger.

## 5. Both sides

- **Best long: AVGO breakout.** Buy stop at 355.50, above the 20-day high of 354.25. Stop 337.00 (about 1.07 ATR). Target 392.00, near late-October prices, 1.97R. **P = 0.34.**
  - Catalysts: Anthropic's S-1 supports its compute deal with Broadcom (Nov 9, single source, Investing.com), and CoreWeave's beat-and-raise (Nov 10 after the close, CNBC).
  - Earnings Dec 9, outside the window.
  - Base rate 40%, moved down because AVGO is already about 20% off its 289.77 low in three sessions, the death cross from October is still in place, and NVDA reports inside the horizon.
  - EV ≈ +0.01R, so it is a pass at conviction 2.
- **Best short: XLRE, selling a rejection.** Sell limit at 44.90 (Monday's high was 44.93). Stop 45.80, above the 45.34 20-day high. Target 43.10, 2.0R. **P = 0.35.**
  - Catalyst: the hot CPI (BLS, Nov 10), with the 10-year near 5% and three hikes priced.
  - Base rate moved down because REITs ignored Tuesday's yield spike.
  - EV ≈ +0.05R, a pass at conviction 2.
- **Other shorts I looked at:** XHB (choppy, swinging ±3–5% a day, no level to lean on); XLV and staples (only a rotation story with no dated catalyst, and my last XLV and XLP longs were stopped out); NVDA (earnings Nov 17, inside 7 days, so rule 8 excludes it); fading the memory names (10–12% ATRs, nowhere to put a stop).

## 6. Passing on

- **AVGO long:** see section 5. Levels in `passed`.
- **XLRE short:** see section 5. Levels in `passed`.
- **ORCL long:** the most direct read from CoreWeave's debt comments. Market about 123.71, stop 113.50 (under the $116 equity offering), target 141.00 (1.7R), P 0.35, EV about −0.05R. Earnings are unconfirmed; projections run from Dec 8 to Dec 14. Pass.
- **COST long:** it is through its 20-day high (1,084 vs 1,081.55) on a $30 special dividend and a $4B buyback reauthorization (company release and 8-K, Nov 10). The dividend has a Nov 24 record date, so with T+1 settlement the ex-date is Nov 24. That is inside the 10-session window, and a mechanical drop of about $30 (2.8%) would distort any bracket. The dividend is cash-neutral anyway. No levels.
- **CRWV, memory and storage (STX/WDC/SNDK/MU), DELL, MRVL:** these are where the catalyst sits, but they are already up 7–15% against 10–12% ATRs. I did not verify a CRWV quote. No levels.
- **NVDA:** earnings Nov 17 are inside 7 days (rule 8).

## 7. For the post-open review

- **XLE:** if the open fills the 63.10 stop, that's the result; no re-entry today. If XLE trades below 63.10 and Brent is under $93, hold.
- **DAL limit:** **cancel** if Brent is above $95 at 10:05 ET. The airline thesis rests on falling fuel costs. Otherwise keep it.
- **IWM:** no action at the review. The invalidation is a *close* above 284, checked tomorrow. The stop at 287 stands.
- **AVGO:** do not chase. If it has failed back below 345 by 10:05, the breakout idea is dead for this week. If it holds above 354.25, the buy-stop idea is already being scored in `passed`.
- **QQQ:** if it gives back the whole gap (below the 674.76 prior close) by 10:05, note it as a failed relief rally for tomorrow. No order changes.

## 8. Book state

- No new orders. **Gross 79% / 150%, net −54% / ±100%** (resting entries counted as filled).
- **Risk at stake 2.27% / 4.0%, slots 6 / 8.** If XLE stops on the open, it realizes about −$541 and risk at stake falls to about 1.74%.

```json
{
  "date": "2026-11-11",
  "no_trade": true,
  "session_note": "Hawkish rates (Dec hike fully priced, 10y ~4.99%, bonds shut for Veterans Day) under an AI relief gap on CoreWeave's beat-and-raise; catalyst names already 0.7-1.0 ATR up pre-open with AMAT/CSCO Thu and NVDA 11/17 ahead, so nothing clears positive EV. Would act on: AVGO confirming a close above 354.25 then retesting 345 and holding, or XLRE rejecting 44.90-45.34 after the 10y reopens above 5% Thursday.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "AVGO",
      "direction": "long",
      "entry_type": "stop",
      "entry": 355.50,
      "stop": 337.00,
      "targets": [392.00],
      "p_target_first": 0.34,
      "reason": "Best long: breakout over the 354.25 20d high on Anthropic S-1 (Nov 9, single-sourced) plus CoreWeave Q3 beat-and-raise (Nov 10 AMC); already ~20% off the 289.77 low in 3 sessions, October death cross intact, NVDA earnings 11/17 inside horizon; EV ~+0.01R, conviction 2."
    },
    {
      "ticker": "XLRE",
      "direction": "short",
      "entry_type": "limit",
      "entry": 44.90,
      "stop": 45.80,
      "targets": [43.10],
      "p_target_first": 0.35,
      "reason": "Best short: rate-sensitive fade after the hot Oct CPI (BLS Nov 10) with 10y near 5% and three hikes priced; but XLRE fell only 0.13% on CPI day while the 10y rose 11bp, so the market is not trading REITs on rates; conviction 2."
    },
    {
      "ticker": "ORCL",
      "direction": "long",
      "entry_type": "market",
      "entry": 123.71,
      "stop": 113.50,
      "targets": [141.00],
      "p_target_first": 0.35,
      "reason": "CoreWeave's 'no new unsecured debt at current yields' is the most direct read for AI-debt fear, but ORCL already +4.9% pre-market (0.66 ATR of a 7.4% ATR), stop must sit under the $116 equity raise; EV about -0.05R; earnings unconfirmed (projected Dec 8-14)."
    }
  ]
}
```

Sources:
- [StockTitan: stock market today, Nov 11 2026](https://www.stocktitan.net/articles/stock-market-today-live-november-11-2026)
- [AOL/Yahoo: futures rise as Nvidia recovers, 10-year nears 5%](https://www.aol.com/articles/stock-market-today-dow-p-123445000.html)
- [Investrade: morning preview, Nov 11 2026](https://investrade.com/morning-preview-november-11-2026/)
- [Investrade: weekly event calendar, Nov 9–13](https://investrade.com/weekly-event-calendar-11-09-2026-11-13-2026/)
- [Saxo: Market Quick Take, Nov 11 2026](https://www.home.saxo/en-sg/content/articles/macro/market-quick-take---us-treasury-yields-rip-higher---11-november-2026-11112026)
- [BLS: CPI release](https://www.bls.gov/news.release/cpi.nr0.htm)
- [Schwab market update](https://www.schwab.com/learn/story/stock-market-update-open)
- [CBS News: October CPI](https://www.cbsnews.com/news/october-cpi-report-elevated-inflation/)
- [ING: US CPI October 2026](https://think.ing.com/articles/us-cpi-october-2026)
- [CNBC: CoreWeave Q3 2026](https://www.cnbc.com/2026/11/10/coreweave-crwv-q3-earnings-report-2026.html)
- [CNBC: CoreWeave pops 11% after outlook raise](https://www.cnbc.com/2026/11/11/coreweave-crwv-outlook-earnings-ai.html)
- [WebProNews: CoreWeave rules out unsecured debt](https://www.webpronews.com/coreweave-q3-2026-earnings-raised-outlook-backlog-unsecured-debt)
- [CNBC: Brent dips below $90](https://www.cnbc.com/2026/11/10/oil-prices-trump-iran.html)
- [Trend.Az: another tanker hits mine in Hormuz](https://www.trend.az/iran/4245076.html)
- [JPost: Iran keeps firing on tankers](https://www.jpost.com/middle-east/article-914514)
- [Townhall: IRGC targets three tankers, Nov 8](https://townhall.com/news/josephchalfant/2026/11/08/irgc-targets-three-oil-tankers-in-the-strait-of-hormuz-n2686101)
- [Costco IR: $30 special dividend](https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Declares-30-Special-Cash-Dividend-and-Reauthorizes-Stock-Repurchase-Program/default.aspx)
- [Costco 8-K](https://www.sec.gov/Archives/edgar/data/0000909832/000090983226000134/costex9918-k111026.htm)
- [NVIDIA IR: Q3 call date](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/)
- [TIKR: Oracle $20B raise](https://www.tikr.com/blog/coreweave-soars-5-oracle-up-4-as-oracles-20-billion-raise-is-exactly-what-they-previewed)
- [Financecalendar: ORCL earnings (projected)](https://www.financecalendar.com/?p=2477)
- [Webull/Benzinga: Broadcom](https://www.webull.com/news/15819841268731904)
- [StockAnalysis: XLRE history](https://stockanalysis.com/etf/xlre/history/)
- [StockAnalysis: IWM history](https://stockanalysis.com/etf/iwm/history/)
- [StockAnalysis: XHB history](https://stockanalysis.com/etf/xhb/history/)
- [Noradarealestate: MBA applications](https://www.noradarealestate.com/blog/mortgage-applications-drop-again-even-rates-hit-2-month-low/)
- [Kiplinger: weekly economic calendar](https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Wednesday 2026-11-11. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,166.71**
- Cash: $133,070.63
- Session P&L so far: -0.30% (new entries are blocked at -3.0%)
- Gross exposure: $80,712 (79% of equity, cap 150%)
- Net exposure: $-55,442 (-54%, cap +/-100%)
- Risk at stake (entry to stop): $2,323 (2.27% of equity, cap 4.0%) — 1.73% left for new plays
- Slots: 3 open + 3 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 46% of equity in notional: at 1% risk its stop must be at least 2.2% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 269.13 | -119 (-1.8%) | +6% | 263.50 | 293.00 |
| IWM | short | 85 | 281.03 | 281.84 | -69 (-0.3%) | -23% | 287.00 | 271.00 |
| XLE | short | 213 | 60.56 | 62.93 | -506 (-3.9%) | -13% | 63.10 | 57.30 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **AMZN**, opened 2026-11-09 (session 3 of at most 10), submitted with stop 263.5 and target 293, P 36%. Thesis: Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong relative signal. Invalidation: QQQ breaking its 20-day low while AMZN falls back inside the range.
- **IWM**, opened 2026-11-10 (session 2 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.
- **XLE**, opened 2026-11-10 (session 2 of at most 10), submitted with stop 63.1 and target 57.3, P 37%. Thesis: Energy is breaking down as the Iran risk premium unwinds; a break of the 60.85 20d low continues the trend toward 57. Invalidation: Brent back above $93 or a renewed Iran escalation headline.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GLD | short | 32 | 374.00 | limit | 382.00 | 358.00 | 2026-11-10 |
| DAL | long | 69 | 89.50 | limit | 85.80 | 96.50 | 2026-11-09 |
| QQQ | short | 29 | 646.50 | stop | 664.00 | 615.00 | 2026-11-09 |

### Your record

46 closed trades: 15W / 31L, total +2.19R, net $+2,879 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 46 | 17 | 26 | +0.05R |
| The same trades, bracket left alone | 45 | | | +0.07R |
| Ideas you passed on, or the caps dropped | 89 | 31 | 49 | +0.03R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 33 | 45% |
| 35%-40% | 58 | 31% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 123 brackets reached target first. Your Brier score is 0.239; saying 39% every time scores 0.238. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| AVGO | short | close | -0.92R | $-232 | 37% |
| NVDA | short | target | +2.16R | $+1,108 | 37% |
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |
| KRE | long | stop | -0.04R | $-10 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AMZN | 269.08 (10:05 iex) | -0.7% | 270.87 | 273.31 / 268.14-274.87 | 10.68 (3.9%) | 229.36-275.34 | +6.1% / +6.6% | +8.0% | 50.4M |
| IWM | 281.84 (10:05 iex) | +0.4% | 280.58 | 282.99 / 281.48-283.09 | 5.21 (1.9%) | 269.88-286.17 | +1.2% / -0.3% | +0.3% | 25.7M |
| XLE | 62.92 (10:05 iex) | +1.1% | 62.21 | 62.85 / 62.34-63.02 | 1.88 (3.0%) | 60.43-70.15 | -6.7% / -4.2% | -6.7% | 37.6M |
| GLD | 367.80 (10:05 iex) | -0.4% | 369.36 | 369.36 / 367.50-369.38 | 7.57 (2.0%) | 354.67-384.88 | -0.7% / -3.7% | +2.8% | 9.2M |
| DAL | 91.62 (10:04 iex) | -0.6% | 92.20 | 91.82 / 91.06-92.05 | 3.48 (3.8%) | 74.14-92.52 | +13.1% / +13.6% | +10.7% | 6.6M |
| QQQ | 686.28 (10:05 iex) | +1.7% | 674.76 | 687.28 / 683.60-689.02 | 17.87 (2.6%) | 647.05-740.53 | -3.7% / -6.2% | -1.5% | 51.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 756.31 (10:05 iex) | +0.9% | 749.92 | 756.80 / 754.90-757.95 | 12.11 (1.6%) | 732.71-776.35 | -1.4% / -1.9% | -0.6% | 49.4M |
| QQQ | 686.28 (10:05 iex) | +1.7% | 674.76 | 687.28 / 683.60-689.02 | 17.87 (2.6%) | 647.05-740.53 | -3.7% / -6.2% | -1.5% | 51.9M |
| IWM | 281.84 (10:05 iex) | +0.4% | 280.58 | 282.99 / 281.48-283.09 | 5.21 (1.9%) | 269.88-286.17 | +1.2% / -0.3% | +0.3% | 25.7M |
| DIA | 521.10 (10:05 iex) | -0.1% | 521.73 | 522.79 / 520.77-523.16 | 7.74 (1.5%) | 508.66-536.60 | +0.1% / +0.4% | +0.9% | 3.9M |
| TLT | 80.70 (10:05 iex) | -0.2% | 80.88 | 80.75 / 80.61-80.76 | 0.80 (1.0%) | 77.41-82.42 | +0.1% / +1.2% | -0.3% | 39.6M |
| GLD | 367.80 (10:05 iex) | -0.4% | 369.36 | 369.36 / 367.50-369.38 | 7.57 (2.0%) | 354.67-384.88 | -0.7% / -3.7% | +2.8% | 9.2M |
| USO | 143.01 (10:04 iex) | +1.1% | 141.45 | 142.66 / 142.47-143.37 | 6.05 (4.3%) | 138.47-171.82 | -10.5% / -7.3% | -10.6% | 5.5M |
| SMH | 501.92 (10:05 iex) | +3.8% | 483.63 | 504.99 / 496.01-505.50 | 25.77 (5.3%) | 445.59-580.08 | -8.1% / -14.1% | -6.7% | 12.1M |
| XLK | 173.66 (10:05 iex) | +2.8% | 168.91 | 173.80 / 172.50-174.30 | 5.82 (3.4%) | 162.14-194.66 | -6.6% / -10.0% | -4.3% | 12.8M |
| XLF | 58.23 (10:05 iex) | -0.1% | 58.29 | 58.09 / 58.02-58.33 | 1.02 (1.7%) | 54.02-60.04 | +3.1% / +4.3% | +1.9% | 35.7M |
| XLE | 62.92 (10:05 iex) | +1.1% | 62.21 | 62.85 / 62.34-63.02 | 1.88 (3.0%) | 60.43-70.15 | -6.7% / -4.2% | -6.7% | 37.6M |
| XLV | 187.00 (10:05 iex) | -1.0% | 188.88 | 187.42 / 186.98-188.10 | 3.79 (2.0%) | 170.65-192.32 | +3.9% / +8.6% | +2.6% | 11.6M |
| XLI | 169.85 (10:05 iex) | +0.7% | 168.73 | 169.99 / 169.17-170.40 | 3.50 (2.1%) | 161.74-172.40 | +0.7% / -0.2% | -1.5% | 9.1M |
| XLY | 120.69 (10:05 iex) | -0.3% | 121.05 | 121.14 / 120.70-121.47 | 2.63 (2.2%) | 110.67-122.92 | +4.2% / +6.7% | +3.2% | 9.4M |
| XLP | 90.36 (10:05 iex) | -0.7% | 91.03 | 90.45 / 90.34-90.98 | 1.81 (2.0%) | 84.61-93.40 | +2.6% / +6.9% | +2.3% | 19.6M |
| XLU | 43.69 (10:05 iex) | -0.1% | 43.73 | 43.68 / 43.57-43.78 | 0.65 (1.5%) | 41.24-44.09 | +2.2% / +4.8% | +0.7% | 27.8M |
| XLB | 52.83 (10:05 iex) | -0.0% | 52.85 | 52.87 / 52.61-52.97 | 1.03 (2.0%) | 49.23-54.63 | +1.8% / +3.9% | +0.5% | 12.5M |
| XLRE | 44.45 (10:05 iex) | -0.3% | 44.58 | 44.41 / 44.38-44.63 | 0.75 (1.7%) | 41.31-45.34 | +3.6% / +5.0% | +2.1% | 8.5M |
| XLC | 108.03 (10:05 iex) | +0.2% | 107.76 | 108.03 / 107.90-108.45 | 2.28 (2.1%) | 99.33-112.90 | +1.7% / -1.6% | +6.2% | 8.1M |
| KRE | 72.89 (10:05 iex) | -0.3% | 73.09 | 73.02 / 72.60-73.10 | 1.67 (2.3%) | 67.79-75.80 | +1.7% / +2.0% | +0.3% | 15.3M |
| XHB | 102.26 (10:05 iex) | -0.9% | 103.17 | 103.19 / 102.28-103.23 | 3.42 (3.3%) | 91.87-108.78 | +3.5% / +4.9% | +1.2% | 2.5M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 353.42 (10:05 iex) | +1.4% | 348.51 | 349.49 / 349.32-354.44 | 9.49 (2.7%) | 325.33-355.38 | +1.2% / +3.3% | +5.0% | 49.5M |
| MSFT | 527.49 (10:05 iex) | -1.1% | 533.16 | 534.37 / 526.62-534.76 | 17.29 (3.2%) | 504.96-559.15 | +0.4% / +3.0% | +2.3% | 26.3M |
| NVDA | 173.25 (10:05 iex) | +2.6% | 168.89 | 172.77 / 170.77-175.13 | 9.29 (5.5%) | 165.89-226.00 | -18.1% / -22.5% | -18.3% | 155.3M |
| AMZN | 269.08 (10:05 iex) | -0.7% | 270.87 | 273.31 / 268.14-274.87 | 10.68 (3.9%) | 229.36-275.34 | +6.1% / +6.6% | +8.0% | 50.4M |
| GOOGL | 290.53 (10:05 iex) | +1.1% | 287.38 | 290.11 / 289.50-291.84 | 11.41 (4.0%) | 276.92-359.40 | -7.6% / -13.1% | +2.6% | 40.3M |
| META | 638.90 (10:05 iex) | -0.4% | 641.39 | 647.24 / 637.52-648.45 | 23.90 (3.7%) | 583.80-761.50 | -1.6% / -5.3% | +3.3% | 24.4M |
| TSLA | 389.72 (10:05 iex) | +2.6% | 379.78 | 386.75 / 386.35-392.67 | 18.31 (4.8%) | 338.15-414.23 | -0.2% / +1.8% | -4.7% | 41.2M |
| AVGO | 352.66 (10:05 iex) | +6.2% | 331.98 | 349.86 / 348.10-354.50 | 17.29 (5.2%) | 289.77-354.25 | +0.9% / -4.0% | -0.0% | 25.5M |
| AMD | 538.08 (10:05 iex) | +4.4% | 515.21 | 543.07 / 522.65-543.40 | 42.65 (8.3%) | 402.10-591.88 | -0.6% / -6.1% | +6.5% | 30.9M |
| ORCL | 125.79 (10:05 iex) | +6.6% | 117.98 | 124.28 / 124.15-126.88 | 8.71 (7.4%) | 109.21-148.48 | -7.3% / -14.2% | -6.5% | 43.8M |
| NFLX | 63.22 (10:05 iex) | -0.1% | 63.26 | 62.84 / 62.75-63.75 | 1.88 (3.0%) | 61.39-73.07 | -3.5% / -10.0% | -0.3% | 47.1M |
| CRM | 214.79 (10:05 iex) | +0.6% | 213.48 | 214.91 / 213.50-215.85 | 9.09 (4.3%) | 208.88-252.42 | -8.8% / -10.2% | -3.9% | 7.2M |
| JPM | 343.04 (10:05 iex) | +0.3% | 342.07 | 342.89 / 340.82-343.84 | 7.95 (2.3%) | 326.40-359.80 | +1.2% / +0.5% | +1.2% | 7.2M |
| GS | 922.81 (10:05 iex) | +1.4% | 910.19 | 927.50 / 912.59-928.38 | 29.62 (3.3%) | 854.45-939.38 | +1.6% / -1.9% | +1.6% | 2.2M |
| BAC | 50.73 (10:05 iex) | +0.1% | 50.68 | 50.87 / 50.33-50.87 | 1.24 (2.5%) | 49.17-53.02 | +0.1% / -7.5% | +2.1% | 43.7M |
| XOM | 165.97 (10:05 iex) | +0.9% | 164.47 | 165.14 / 164.46-166.10 | 5.16 (3.1%) | 160.11-188.50 | -6.8% / -2.7% | -7.3% | 14.2M |
| CVX | 212.39 (10:05 iex) | +0.6% | 211.22 | 212.31 / 210.88-212.41 | 5.72 (2.7%) | 206.01-236.48 | -5.6% / -1.8% | -6.2% | 8.4M |
| LLY | 1,419.19 (10:05 iex) | -0.9% | 1,432.29 | 1,418.08 / 1,414.37-1,427.75 | 53.57 (3.7%) | 1,174.24-1,453.00 | +8.0% / +17.0% | +1.6% | 3.2M |
| UNH | 398.53 (10:05 iex) | -1.6% | 405.12 | 404.39 / 396.95-404.74 | 11.42 (2.8%) | 382.29-426.55 | -0.5% / +3.7% | +0.2% | 5.7M |
| JNJ | 277.13 (10:05 iex) | -1.3% | 280.78 | 277.96 / 276.67-278.66 | 7.77 (2.8%) | 248.50-283.25 | +5.1% / +5.4% | +5.5% | 7.7M |
| WMT | 124.52 (10:05 iex) | -0.8% | 125.55 | 124.33 / 124.30-126.07 | 3.19 (2.5%) | 113.38-131.82 | +3.0% / +10.8% | +0.6% | 23.0M |
| COST | 1,073.19 (10:05 iex) | +0.7% | 1,066.14 | 1,080.51 / 1,072.57-1,091.92 | 21.46 (2.0%) | 958.58-1,081.55 | +5.1% / +11.5% | +4.6% | 2.5M |
| HD | 346.66 (10:05 iex) | -1.2% | 351.00 | 348.43 / 344.31-348.43 | 10.50 (3.0%) | 289.57-362.44 | +7.3% / +13.1% | +5.2% | 4.8M |
| CAT | 594.87 (10:05 iex) | +1.8% | 584.57 | 600.70 / 588.50-601.28 | 32.66 (5.6%) | 550.81-768.52 | -12.1% / -22.1% | -6.3% | 4.0M |
| BA | 174.08 (10:04 iex) | +0.4% | 173.38 | 172.81 / 172.18-174.27 | 6.67 (3.8%) | 165.01-193.28 | -3.6% / -9.2% | +0.0% | 10.6M |
| DAL | 91.62 (10:04 iex) | -0.6% | 92.20 | 91.82 / 91.06-92.05 | 3.48 (3.8%) | 74.14-92.52 | +13.1% / +13.6% | +10.7% | 6.6M |
| UAL | 118.51 (10:05 iex) | -1.7% | 120.56 | 119.38 / 118.35-119.79 | 5.59 (4.6%) | 94.54-122.08 | +14.5% / +11.9% | +12.5% | 5.6M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SNDK | 969.93 (10:05 iex) | +12.8% | 859.99 | 928.04 / 920.11-970.40 | 107.74 (12.5%) | 803.97-1,461.80 | -27.7% / -41.8% | -23.7% | 11.4M |
| DELL | 367.67 (10:05 iex) | +10.0% | 334.38 | 360.40 / 358.52-368.35 | 33.23 (9.9%) | 315.00-547.63 | -22.3% / -33.1% | -18.1% | 7.7M |
| MU | 795.99 (10:05 iex) | +9.8% | 725.11 | 777.00 / 763.05-794.84 | 60.62 (8.4%) | 650.00-990.00 | -15.2% / -23.9% | -15.2% | 31.0M |
| STX | 547.16 (10:05 iex) | +9.1% | 501.62 | 546.24 / 533.14-547.70 | 54.27 (10.8%) | 449.28-751.81 | -19.1% / -33.7% | -17.3% | 6.1M |
| MRVL | 166.53 (10:05 iex) | +7.9% | 154.39 | 167.04 / 162.50-168.22 | 18.53 (12.0%) | 132.54-264.30 | -25.0% / -33.4% | -10.2% | 29.8M |
| INTC | 62.22 (10:05 iex) | +7.0% | 58.13 | 61.77 / 60.95-62.50 | 6.47 (11.1%) | 51.51-101.34 | -26.2% / -39.9% | -4.0% | 148.4M |
| SMCI | 29.74 (10:05 iex) | +7.0% | 27.79 | 29.62 / 29.12-29.80 | 2.35 (8.5%) | 25.81-38.02 | -13.7% / -25.1% | -11.5% | 43.7M |
| WDC | 308.83 (10:05 iex) | +6.8% | 289.20 | 309.04 / 301.71-310.97 | 28.27 (9.8%) | 258.61-402.23 | -15.7% / -27.7% | -16.7% | 9.3M |
| ABNB | 181.05 (10:05 iex) | -3.1% | 186.90 | 182.71 / 178.80-183.73 | 7.09 (3.8%) | 163.82-197.87 | +7.5% / +10.5% | +11.9% | 4.6M |
| SE | 74.47 (10:05 iex) | -3.0% | 76.80 | 77.00 / 74.31-77.10 | 3.76 (4.9%) | 71.53-100.00 | -3.8% / -17.7% | +0.0% | 8.9M |
| KMB | 107.60 (10:05 iex) | -2.9% | 110.76 | 109.02 / 107.67-109.18 | 3.78 (3.4%) | 97.84-112.91 | +2.6% / +7.9% | +6.0% | 7.2M |
| CI | 294.93 (10:05 iex) | -2.7% | 303.13 | 300.73 / 295.50-302.22 | 8.73 (2.9%) | 283.56-318.05 | +0.9% / +5.8% | +2.6% | 1.7M |
| GIS | 33.67 (10:05 iex) | -2.7% | 34.60 | 34.09 / 33.69-34.21 | 1.23 (3.6%) | 31.68-37.02 | +1.7% / +1.0% | +1.5% | 8.9M |
| ACN | 251.81 (10:05 iex) | -2.6% | 258.51 | 254.88 / 251.81-255.95 | 11.95 (4.6%) | 212.71-271.76 | +4.6% / +21.7% | +1.6% | 6.3M |
| SYK | 316.39 (10:05 iex) | -2.4% | 324.29 | 319.23 / 316.85-320.70 | 12.60 (3.9%) | 278.57-349.48 | +5.2% / +11.1% | +4.4% | 3.2M |
| BMY | 61.34 (10:05 iex) | -2.3% | 62.80 | 62.00 / 61.44-62.11 | 1.70 (2.7%) | 56.58-65.54 | +1.9% / +1.5% | +1.8% | 10.9M |
