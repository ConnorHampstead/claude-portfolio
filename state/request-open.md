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

# Pre-market brief: Friday 2026-11-27 (Black Friday half day)

**Time:** 09:05 ET (15:05 Stockholm, ET+6 today). The cash session opens 09:30 ET (15:30 Stockholm) and stocks close early at 13:00 ET (19:00 Stockholm); bonds close at 14:00 ET (20:00 Stockholm). The post-open review runs at about 10:05 ET (16:05 Stockholm). Nothing runs after that before Monday.

**Decision:** one new play, a half-risk SPY long on a pullback limit. It clears the bar only narrowly, at about +0.04R on my own numbers. Everything else goes to the shadow book with levels.

## 1. Tape

**Wednesday.** Wednesday was a washout reversal, and that is the fact the session turns on.
- The S&P 500 fell to 6,970.11 (−3.2%) and closed at 7,182.78 (−0.25%).
- The Dow erased an 1,100-point loss and closed +0.33%.
- Reuters had the Nasdaq-100 briefly down 20% from its record, i.e. touching bear-market territory, before it closed −0.64%.
- The selloff was tied to AI regulation fears after the Democratic midterm sweep, new tariff proposals, and core PCE at 3.3%.

**Overnight.** Over the holiday the rest of the world rallied.
- China's State Council called for state-backed "national team" funds to support the market. The CSI Semiconductor index rose a record 17.4%, and the Kospi rose about 4.3%.
- Brazil's Ibovespa rose 6.1% Thursday after Lula picked Bradesco chairman Trabuco as finance minister.

**Pre-market** (Alpaca table, 08:49 ET):

| | Pre-market | Change |
|---|---|---|
| SPY | 728.07 | +1.6% |
| QQQ | 648.44 | +2.3% |
| SMH | 439.04 | +3.9% |
| VIX | about 25.3 | from 26.8 at Wednesday's close and about 34 intraday Wednesday |

**Macro is still hawkish:**
- CME FedWatch prices a December hike at about 97–99%, and January at about 60%.
- The 10-year yield is about 4.85–4.92%.
- Q3 GDP was revised up to 4.3%.
- WTI is about $85–86 (+2–2.5%) on Hormuz and Saudi attacks, with OPEC+ meeting Sunday.

**Regime:** a high-volatility bear-market rally on thin holiday volume. Over the next few sessions I think the long side has a modest edge because of the capitulation-style reversal. I would not chase today's gap.

## 2. Calendar

| Time ET / Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|
| 08:30 / 14:30 (released) | Advance goods trade balance, Oct | **−$149.5B** vs about −$133B consensus (imports +; capital goods imports +8.5% m/m) | SPY; futures barely moved, still +1.6% |
| 08:30 / 14:30 (released) | Wholesale inventories, Oct | **+0.9%** vs about +0.5–0.7% | none |
| 08:30 / 14:30 (released) | Retail inventories, Oct | **+0.8%** | none |
| 13:00 / 19:00 | Early equity close (bonds 14:00 / 20:00) | — | SPY limit (good-till-cancelled) |
| Sun 11-29 | OPEC+ meeting | — | none (energy passed) |
| Mon 12-01 10:00 / 16:00 | JOLTS, Oct | — | SPY |
| Mon 12-01 | Huang closed-door House interview (export probe) | — | SPY (NVDA weight) |
| Tue 12-01 16:30 / 22:30 | MRVL Q3 FY27 call, results after close (Marvell IR) | revenue guide $3.15B ±5% | none |
| Wed 12-03 | Huang at the Senate Banking public hearing | — | SPY |
| Fri 12-04 08:30 / 14:30 | November payrolls | — | SPY |
| Wed 12-09 14:00 / 20:00 | FOMC decision (day 9 of the SPY horizon) | +25bp about 97–99% priced | SPY |

Two aggregators (Unusual Whales, Swingfolio) say MRVL "beat Q3". Marvell's own IR page says it reports Dec 1, so I treat both aggregators as unreliable today.

## 3. Open positions and resting entries

None. The QQQ 604 sell stop never triggered and was cleared before Thursday's holiday; the book shows 0 resting. Nothing to manage.

## 4. New plays

| Field | Value |
|---|---|
| Ticker | SPY |
| Direction | Long |
| Catalyst | **Nov 25 washout reversal.** S&P went from 6,970.11 (−3.2%) to 7,182.78 (−0.25%) and the NDX briefly touched −20% (Reuters, via Fox Business, Swingfolio and gsmglobalnews). **Nov 26–27 follow-through:** China's State Council market-support call, global risk-on, VIX about 25 from about 34. **Prior plan:** the last review's index-long condition (SPY reclaims 712 and VIX < 28) is now met. |
| Thesis | Wednesday's 3% intraday reversal with positive breadth, plus a global follow-through gap, makes the 695 area a candidate capitulation low. Bear-market rallies from such lows usually run to the 50-day average before they are tested. I buy a partial gap fill rather than the open. |
| Entry | Buy limit 722.00 (about the midpoint of today's gap, 716.70 → 728.07) |
| Stop | 692.00. Wednesday's SPY low is **inferred** at about 695.5 (SPX 6,970.11 × the SPY/SPX ratio of 0.09978), so the stop sits below it. A break means the capitulation low failed. Distance is 30 points = 1.8 ATR, 4.2%. |
| Target | 760.00, just above the 50-day average (about 757.6, derived from 716.70 / 0.946). 38 points = **1.27R** |
| Risk tier | 0.5%. A counter-trend entry: SPY is 3.2% below its 20-day average and 5.4% below its 50-day average. Conviction is 3. |
| Time horizon | 3–10 sessions |
| Next earnings | n/a (ETF). Not an event trade. |
| Conviction | 3 |
| P(target before stop) | **0.46.** Random walk for a 30-down / 38-up bracket gives 0.44. My 39% base rate on roughly 1.5–2R brackets is consistent with a random walk. I add about 2pp for post-washout drift and no more because of the priced hiking cycle. Value is 0.46 × 1.27 − 0.54 = **+0.04R**. |
| Invalidation | A daily VIX close above 32 (the panic has resumed), or CME FedWatch showing above 50% odds of a **50bp** December hike. |
| What I'd be wrong about | Bear-market rallies fail at the 20-day average (about 740), short of 760. The week ahead stacks the Huang testimony (Dec 1 and 3), payrolls (Dec 4) and a near-certain hike (Dec 9). The half-day gap is on thin volume. A limit fill at 722 may itself be the sign the bounce is failing. |

**Reasoning.** This is a level-based bounce trade, not a fundamental call. On my own numbers its edge is thin. It is placed because:
- the conditions set before the move are now met;
- the stop sits at a dated structural low;
- the value is positive, at half size.

A conviction-3, +0.04R idea is close to the line. I am not pretending otherwise.

## 5. Both sides

**Best long: SPY** (section 4). Limit 722 / stop 692 / target 760, P 0.46.

**Best short: QQQ, retest of the 20-day average** (passed). Sell limit 664 / stop 690 / target 612 (2.0R), P 0.33, value about −0.01R.
- QQQ's 20-day average is about 666.6 and its trend is down, with the Huang hearings coming.
- But it directly contradicts the SPY long: one of the two must lose.
- The value is not positive anyway.

**Other shorts I looked at:**
- **VRTX** continuation after the FDA delay
- **MO** as the acquirer in a possible Imperial Brands bid
- **PANW** on the whistleblower lawsuit

## 6. Passing on

| Idea | Levels | P | Why I passed |
|---|---|---|---|
| QQQ short | limit 664 / 690 / 612 | 0.33 | See section 5: about −0.01R, and contradicts SPY. |
| VRTX long (fade the PDUFA delay) | mkt 518.31 / 499 / 545 (1.38R) | 0.38 | **What happened:** FDA extended the povetacicept review to Feb 28, 2027 after a major amendment. Vertex's release came out after the close Nov 25 (Investing.com); I couldn't open Vertex's own release, the newsroom returned 403. **Analysts:** JPM keeps 95% probability of approval, Citi keeps Buy. **Price:** the −8% drop only unwinds the pre-PDUFA run-up (prior close was +7.4% vs the 50-day average), and the Citizen Petition on IgG monitoring is unresolved. **Value:** about −0.10R. |
| MO short (acquirer overhang) | mkt 74.35 / 77.10 / 70.20 (1.51R) | 0.32 | **What happened:** Altria confirmed a possible all-cash Imperial offer on Nov 26 and calls it "very early stage"; the put-up-or-shut-up deadline is Dec 24. **Risk:** if Altria walks away, the stock pops. **Value:** about −0.20R. |
| PANW short | mkt 347.43 / 370 / 305 (1.88R) | 0.30 | **What happened:** an ex-RVP's SDNY suit alleging pulled-forward bookings, which the company calls "meritless," and Northland cut estimates. **Data:** premarket prints conflict across sources (+1.4% to −2.9%). **Value:** about −0.14R. |
| NU long (Brazil catch-up) | mkt 13.82 / 12.90 / 15.20 (1.5R) | 0.34 | **What happened:** the Trabuco catalyst is verified, but the ADR gap only catches up to Thursday's Ibovespa +6%. **Price:** already 2.4 ATR, and PT factions are resisting the pick. **Value:** about −0.15R. |
| META long | mkt 629.81 / 595 / 680 (1.44R) | 0.36 | **What happened:** the catalyst is a Fortune report of Amazon–Muse *talks*, with no deal. **Price:** up 7% in 1.5 sessions. **Value:** about −0.12R. |
| WMT long (pullback) | limit 129.50 / 125.50 / 136.50 (1.75R) | 0.36 | **What happened:** the Nov 19 earnings catalyst is now 7 sessions old. **Value:** about −0.01R. |
| DE, SMH, memory names (SNDK, MU), BRZ ADRs | no levels | — | **DE:** not in the data table. I infer a Wednesday close of about 641 and Bernstein's new $640 target sits below the price. **Semis and memory:** ATRs of 8–17% make a 3–10% gap a chase. |

## 7. For the post-open review (about 10:05 ET / 16:05 Stockholm)

**SPY limit 722:**
- **Unfilled and VIX above 28 at 10:05:** cancel it. The prior plan's VIX condition has failed.
- **Unfilled and SPY above 735:** leave it resting and do not convert to market. Re-scored, a market buy at 735 with stop 692 and target 760 is negative.
- **Filled:** leave the bracket alone, whatever the price.

**No other conditional entries.** If VRTX reclaims 525 (its 50-day average area) by 10:05 the review may re-score the long, but a short below 513.80 would be a chase.

**Level for next week:** QQQ at 660–668 going into the Huang hearings is where the short gets another look, and only if SPY is flat by then.

## 8. Book state

- **Once filled:** SPY long about $12.3k notional, about 12% gross and +12% net (caps 150% and ±100%). No sector exposure beyond the broad index.
- **Risk at stake:** about 0.5% of 4.0%. Slots 1/8.

```json
{
  "date": "2026-11-27",
  "no_trade": false,
  "session_note": "Half-day post-holiday gap-up (SPY +1.6%, QQQ +2.3%, VIX ~25) after Wednesday's washout reversal (SPX 6,970 -> 7,183, NDX briefly -20%); hawkish Fed (~98% Dec hike) unchanged. One half-risk SPY long on a gap-midpoint limit with stop under the Wednesday low; everything else negative EV and logged.",
  "plays": [
    {
      "ticker": "SPY",
      "direction": "long",
      "entry_type": "limit",
      "entry": 722.00,
      "stop": 692.00,
      "targets": [760.00],
      "time_horizon": "3-10 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.46,
      "earnings_date": null,
      "event_trade": false,
      "catalyst": "Nov 25 washout reversal: S&P 500 from 6,970.11 (-3.2%) to 7,182.78 close (-0.25%), Nasdaq-100 briefly -20% from record (Reuters via Fox Business/Swingfolio); Nov 26-27 global follow-through on China State Council market-support call (CSI semis +17.4%), VIX ~25 from ~34 intraday. Prior review's index-long condition (SPY > 712, VIX < 28) now met.",
      "thesis": "A 3% intraday reversal with positive breadth plus a global follow-through gap makes ~695.5 (inferred SPY equivalent of SPX 6,970) a candidate capitulation low. Bear-market rallies from such lows usually reach the 50-day average (~757.6) before being tested. Buying a partial gap fill rather than the open.",
      "invalidation": "A daily VIX close above 32, or CME FedWatch showing above 50% probability of a 50bp December hike.",
      "bear_case": "Rally fails at the 20-day average (~740); Huang testimony Dec 1/3, payrolls Dec 4 and a ~98%-priced Dec 9 hike stack inside the horizon; half-day gap on thin volume; a fill at 722 may itself signal the bounce failing."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "limit",
      "entry": 664.00,
      "stop": 690.00,
      "targets": [612.00],
      "p_target_first": 0.33,
      "reason": "Best short: bear-rally fade at the ~666.6 20-day average with Huang hearings ahead, but it directly contradicts the SPY long and is ~-0.01R."
    },
    {
      "ticker": "VRTX",
      "direction": "long",
      "entry_type": "market",
      "entry": 518.31,
      "stop": 499.00,
      "targets": [545.00],
      "p_target_first": 0.38,
      "reason": "Fade of the -8% povetacicept PDUFA extension (to Feb 28, 2027, major amendment; JPM 95% PoA, Citi Buy), but the drop just unwinds the pre-PDUFA run-up and the IgG-monitoring citizen petition is unresolved. About -0.10R."
    },
    {
      "ticker": "MO",
      "direction": "short",
      "entry_type": "market",
      "entry": 74.35,
      "stop": 77.10,
      "targets": [70.20],
      "p_target_first": 0.32,
      "reason": "Acquirer overhang after Altria confirmed a possible all-cash Imperial Brands offer (Nov 26, very early stage, PUSU Dec 24); a walk-away would pop the stock. About -0.20R."
    },
    {
      "ticker": "PANW",
      "direction": "short",
      "entry_type": "market",
      "entry": 347.43,
      "stop": 370.00,
      "targets": [305.00],
      "p_target_first": 0.30,
      "reason": "Ex-RVP SDNY suit alleging premature bookings plus Northland estimate cuts, but the company calls it meritless and premarket prints conflict across sources. About -0.14R."
    },
    {
      "ticker": "NU",
      "direction": "long",
      "entry_type": "market",
      "entry": 13.82,
      "stop": 12.90,
      "targets": [15.20],
      "p_target_first": 0.34,
      "reason": "Brazil catch-up to Thursday's Ibovespa +6.1% on the Trabuco finance-minister pick; the gap is the catch-up itself, 2.4 ATR, with PT resistance to the pick. About -0.15R."
    },
    {
      "ticker": "META",
      "direction": "long",
      "entry_type": "market",
      "entry": 629.81,
      "stop": 595.00,
      "targets": [680.00],
      "p_target_first": 0.36,
      "reason": "Relative-strength leader on a Fortune report of Amazon-Muse talks (no deal); +7% in 1.5 sessions. About -0.12R."
    },
    {
      "ticker": "WMT",
      "direction": "long",
      "entry_type": "limit",
      "entry": 129.50,
      "stop": 125.50,
      "targets": [136.50],
      "p_target_first": 0.36,
      "reason": "Prior review's pullback level, but the Nov 19 earnings catalyst is stale and defensives lag in a risk-on bounce. About -0.01R."
    }
  ]
}
```

Sources:
- [Yahoo Finance live: futures, VIX, yields, Nov 27](https://finance.yahoo.com/markets/live/stock-market-today-firday-november-27-dow-sp-500-nasdaq-black-friday-holiday-091152065.html)
- [StockInvest premarket digest: China State Council, CSI semis, FedWatch, calendar](https://stockinvest.us/digest/digest-us-premarket-2026-11-27)
- [Swingfolio morning: VIX, Brazil ADRs, calendar (MRVL claim contradicted by IR)](https://swingfolio.com/daily/us/2026-11-27/morning)
- [Unusual Whales premarket brief (MRVL claim contradicted by IR)](https://unusualwhales.com/news/premarket-brief-stocks-rebound-thanksgiving-vertex-2026-11-27)
- [Benzinga via TradingView: FedWatch 98.8%, yields, PANW, DE, HPQ](https://www.tradingview.com/news/benzinga:59e33908c094b:0-stock-market-today-dow-s-p-500-nasdaq-100-futures-rise-as-wall-street-returns-to-wrap-up-holiday-shortened-week-spcx-panw-hpq-in-focus/)
- [24/7 Wall St: futures above 7,300](https://247wallst.com/investing/2026/11/27/stock-futures-rip-on-thanksgiving-night-as-sp-500-futures-top-7300/)
- [Fox Business: Nov 25 close, Dow erases 1,100-point loss](https://www.foxbusiness.com/markets/stocks-11-25-2026)
- [gsmglobalnews: Nov 25 close](https://gsmglobalnews.com/article/d20261125-mktclose1.html)
- [Chip Dispatch: Nasdaq plunged 4.6%, closed −0.6%](https://chipdispatch.com/articles/nasdaq-plunged-4-6-intraday-closed-down-just-0-6)
- [Investing.com: Vertex FDA extension (Nov 25, 16:44)](https://www.investing.com/news/stock-market-news/vertex-shares-drop-75-as-fda-extends-review-for-kidney-drug-povetacicept-5051552)
- [Investing.com: JPMorgan on VRTX delay (Nov 26)](https://www.investing.com/news/analyst-ratings/vertex-stock-rating-reiterated-by-jpmorgan-after-povetacicept-pdufa-delay-93CH-5052108)
- [TipRanks/Fly: Citi on Vertex delay](https://www.tipranks.com/news/the-fly/vertex-fda-review-delay-not-thesis-changing-says-citi-thefly-news)
- [Reuters via Investing.com: Altria weighs Imperial offer](https://investing.com/news/stock-market-news/altria-weighs-possible-offer-for-uks-imperial-brands-5052505)
- [TipRanks/Fly: Altria confirms potential cash offer](https://www.tipranks.com/news/the-fly/altria-confirms-potential-cash-offer-for-imperial-brands-thefly-news)
- [Finexus: PANW lawsuit and Northland cuts](https://api.finexus.net/api/news/earnings/129964/html)
- [GuruFocus: NU premarket without company news](https://www.gurufocus.com/news/9228533/nu-holdings-nu-stock-jumps-83-premarket-without-company-news)
- [PiQ: Ibovespa +6.1% on Trabuco](https://piqmarkets.com/story/brazil-s-ibovespa-jumps-6-1-as-lula-names-banker-trabuco-finance-minister)
- [Startup Fortune: Brazil stocks and Trabuco](https://startupfortune.com/brazil-stocks-surge-6-before-lula-confirms-banker-trabuco-for-finance/)
- [HeyGoTrade: META +3.4% on Amazon Muse talks](https://www.heygotrade.com/en/news/meta-meta-stock-news-november-26-2026/)
- [Investing.com: Bernstein raises DE target to $640](https://www.investing.com/news/analyst-ratings/bernstein-socgen-raises-deere-stock-price-target-to-640-on-fy27-recovery-outlook-93CH-5053505)
- [Marvell IR: Q3 FY27 results call Dec 1](https://investor.marvell.com/news-events/press-releases/detail/1041/marvell-technology-inc-announces-conference-call-to-review-third-quarter-of-fiscal-year-2027-financial-results)
- [MarketIntelLabs: December hike odds 94–97%](https://marketintellabs.com/research/december-fed-rate-hike-odds)
- [ActionForex: goods trade deficit $149.5B](https://www.actionforex.com/live-comments/662315-us-goods-trade-deficit-widens-to-149-5b-as-capital-goods-imports-surge/)
- [MLQ: goods trade deficit widens](https://mlq.ai/news/us-goods-trade-deficit-widens-to-1495-billion-as-imports-jump/)
- [Senate Banking: export-controls hearing with Huang](https://www.banking.senate.gov/hearings/protecting-americas-ai-advantage-oversight-of-us-export-controls)
- [Latin Times: Huang before House committees](https://www.latintimes.com/jensen-huang-nvidia-house-committees-chip-probe-601470)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Friday 2026-11-27. The cash session opened 35 min ago and closes at 13:00 ET (19:00 Stockholm).
- Equity: **$102,942.53**
- Cash: $90,700.49
- Session P&L so far: -0.03% (new entries are blocked at -3.0%)
- Gross exposure: $12,242 (12% of equity, cap 150%)
- Net exposure: $+12,242 (+12%, cap +/-100%)
- Risk at stake (entry to stop): $509 (0.49% of equity, cap 4.0%) — 3.51% left for new plays
- Slots: 1 open + 0 resting entries of 8 — you may add at most 7 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| SPY | long | 17 | 721.96 | 720.12 | -31 (-0.3%) | +12% | 692.00 | 760.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **SPY**, opened 2026-11-27 (session 1 of at most 10), submitted with stop 692 and target 760, P 46%. Thesis: A 3% intraday reversal with positive breadth plus a global follow-through gap makes ~695.5 (inferred SPY equivalent of SPX 6,970) a candidate capitulation low. Bear-market rallies from such lows usually reach the 50-day average (~757.6) before being tested. Buying a partial gap fill rather than the open. Invalidation: A daily VIX close above 32, or CME FedWatch showing above 50% probability of a 50bp December hike.

### Your record

53 closed trades: 17W / 36L, total +1.50R, net $+2,991 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 53 | 19 | 31 | +0.03R |
| The same trades, bracket left alone | 53 | | | +0.05R |
| Ideas you passed on, or the caps dropped | 137 | 48 | 78 | +0.03R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 54 | 46% |
| 35%-40% | 88 | 30% |
| 40%-45% | 27 | 48% |
| 45%-50% | 5 | 20% |
| 50%-60% | 1 | 100% |

Base rate: 38% of 176 brackets reached target first. Your Brier score is 0.239; saying 38% every time scores 0.236. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 720.15 (10:05 iex) | +0.5% | 716.70 | 725.86 / 719.91-726.09 | 16.88 (2.4%) | 686.75-775.64 | -3.2% / -5.4% | -1.8% | 65.2M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 720.15 (10:05 iex) | +0.5% | 716.70 | 725.86 / 719.91-726.09 | 16.88 (2.4%) | 686.75-775.64 | -3.2% / -5.4% | -1.8% | 65.2M |
| QQQ | 637.46 (10:05 iex) | +0.6% | 633.93 | 645.73 / 637.15-645.89 | 23.32 (3.7%) | 606.23-718.07 | -4.9% / -10.3% | -3.9% | 63.9M |
| IWM | 270.97 (10:05 iex) | +0.8% | 268.87 | 271.82 / 270.69-272.45 | 6.23 (2.3%) | 256.32-286.17 | -2.0% / -3.0% | -0.5% | 28.4M |
| DIA | 504.20 (10:01 iex) | +0.6% | 501.27 | 506.70 / 503.52-506.78 | 9.56 (1.9%) | 479.40-536.00 | -2.0% / -2.6% | +0.0% | 4.3M |
| TLT | 81.72 (10:05 iex) | -0.6% | 82.24 | 81.81 / 81.71-81.94 | 0.80 (1.0%) | 79.11-82.81 | +1.5% / +3.0% | +2.5% | 39.2M |
| GLD | 333.09 (10:04 iex) | +1.7% | 327.45 | 333.16 / 332.06-333.88 | 8.87 (2.7%) | 313.96-380.18 | -7.5% / -11.7% | -4.0% | 11.2M |
| USO | 139.37 (10:00 iex) | -0.4% | 139.89 | 139.98 / 139.37-140.06 | 4.76 (3.4%) | 132.28-171.82 | -4.0% / -7.0% | +2.8% | 4.6M |
| SMH | 423.66 (10:05 iex) | +0.3% | 422.46 | 435.31 / 421.85-435.55 | 32.34 (7.7%) | 393.88-565.87 | -11.4% / -21.9% | -8.1% | 13.8M |
| XLK | 156.56 (10:05 iex) | +0.5% | 155.79 | 159.01 / 156.22-159.30 | 7.64 (4.9%) | 148.09-189.34 | -7.2% / -14.8% | -4.9% | 17.1M |
| XLF | 56.95 (10:05 iex) | +0.8% | 56.51 | 57.00 / 56.90-57.16 | 1.02 (1.8%) | 54.42-60.04 | -1.2% / +1.2% | +0.2% | 42.6M |
| XLE | 61.87 (10:05 iex) | +1.6% | 60.90 | 61.57 / 61.55-62.05 | 1.40 (2.3%) | 59.55-70.15 | -3.9% / -5.5% | -0.6% | 37.0M |
| XLV | 182.85 (10:05 iex) | -0.5% | 183.68 | 183.18 / 182.76-184.10 | 3.62 (2.0%) | 176.71-192.32 | -0.6% / +3.6% | +1.4% | 13.9M |
| XLI | 164.41 (10:04 iex) | +0.9% | 162.95 | 165.23 / 164.17-165.25 | 3.98 (2.4%) | 155.70-172.40 | -1.8% / -2.7% | -1.0% | 9.7M |
| XLY | 118.64 (10:05 iex) | +1.0% | 117.49 | 118.92 / 118.39-119.26 | 2.90 (2.5%) | 112.03-122.92 | -0.6% / +2.6% | -1.4% | 10.1M |
| XLP | 92.56 (10:04 iex) | +0.3% | 92.30 | 92.01 / 91.95-92.56 | 1.45 (1.6%) | 87.39-93.48 | +1.6% / +6.3% | +1.2% | 22.5M |
| XLU | 43.63 (10:05 iex) | +0.0% | 43.61 | 43.69 / 43.57-43.77 | 0.60 (1.4%) | 42.63-44.40 | +0.3% / +3.7% | +0.1% | 26.2M |
| XLB | 51.75 (10:05 iex) | +1.1% | 51.21 | 51.75 / 51.58-51.94 | 1.12 (2.2%) | 48.21-54.63 | -1.0% / +0.9% | +1.5% | 13.3M |
| XLRE | 44.08 (10:04 iex) | +0.5% | 43.86 | 44.02 / 43.95-44.12 | 0.68 (1.6%) | 42.40-45.34 | +0.1% / +3.0% | +0.6% | 7.9M |
| XLC | 106.69 (10:04 iex) | +1.2% | 105.38 | 107.03 / 106.51-107.35 | 2.59 (2.5%) | 99.33-109.26 | +0.8% / -2.5% | -0.2% | 8.2M |
| KRE | 70.15 (10:05 iex) | +0.5% | 69.83 | 70.27 / 70.12-70.59 | 1.31 (1.9%) | 68.14-75.80 | -2.7% / -1.8% | -1.0% | 15.8M |
| XHB | 103.65 (10:03 iex) | -0.0% | 103.67 | 104.29 / 103.37-104.29 | 3.08 (3.0%) | 96.34-108.78 | +1.7% / +5.1% | +2.9% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 356.61 (10:05 iex) | +0.3% | 355.58 | 358.21 / 355.74-358.91 | 8.03 (2.3%) | 325.08-360.83 | +2.0% / +3.7% | +0.9% | 51.7M |
| MSFT | 490.39 (10:05 iex) | +0.1% | 489.93 | 499.24 / 489.00-500.46 | 17.04 (3.5%) | 477.39-558.07 | -5.1% / -5.5% | -3.4% | 30.9M |
| NVDA | 145.78 (10:05 iex) | -2.4% | 149.30 | 151.82 / 145.39-151.98 | 15.83 (10.6%) | 124.50-215.33 | -13.4% / -26.7% | -1.1% | 351.8M |
| AMZN | 250.03 (10:05 iex) | +2.3% | 244.43 | 250.45 / 248.45-251.35 | 10.46 (4.3%) | 229.36-275.34 | -5.0% / -4.2% | -8.7% | 55.4M |
| GOOGL | 270.52 (10:05 iex) | -0.9% | 273.10 | 278.96 / 270.52-279.58 | 11.63 (4.3%) | 262.73-304.97 | -3.5% / -14.2% | -3.3% | 45.7M |
| META | 623.42 (10:05 iex) | +2.2% | 609.89 | 628.49 / 620.80-630.09 | 24.31 (4.0%) | 558.68-648.45 | -0.9% / -9.3% | -1.1% | 18.3M |
| TSLA | 391.34 (10:05 iex) | +2.9% | 380.14 | 391.34 / 384.66-395.25 | 20.05 (5.3%) | 338.15-414.23 | -0.5% / +0.8% | -0.9% | 35.8M |
| AVGO | 307.42 (10:05 iex) | +2.2% | 300.86 | 306.39 / 304.75-309.31 | 23.14 (7.7%) | 278.00-369.82 | -8.0% / -11.6% | -15.0% | 32.4M |
| AMD | 400.64 (10:05 iex) | -1.3% | 406.03 | 420.10 / 399.68-420.27 | 52.47 (12.9%) | 370.40-594.00 | -17.0% / -26.0% | -23.4% | 47.2M |
| ORCL | 104.40 (10:05 iex) | +0.5% | 103.88 | 106.53 / 104.20-107.25 | 8.32 (8.0%) | 99.34-144.61 | -12.6% / -20.1% | -8.8% | 40.6M |
| NFLX | 60.46 (10:05 iex) | +1.8% | 59.41 | 60.01 / 59.98-61.01 | 1.94 (3.3%) | 56.56-67.49 | -3.7% / -10.3% | -0.7% | 40.5M |
| CRM | 198.50 (10:01 iex) | +0.7% | 197.21 | 197.53 / 196.65-200.39 | 8.67 (4.4%) | 179.91-234.62 | -5.9% / -12.7% | +3.6% | 7.4M |
| JPM | 322.38 (10:04 iex) | +1.8% | 316.74 | 321.94 / 321.43-323.61 | 7.73 (2.4%) | 309.18-359.80 | -5.1% / -5.4% | -2.3% | 7.4M |
| GS | 805.92 (10:05 iex) | +0.6% | 801.03 | 818.60 / 805.00-819.26 | 31.80 (4.0%) | 772.74-939.38 | -8.8% / -10.5% | -8.3% | 2.5M |
| BAC | 49.08 (10:05 iex) | +1.1% | 48.54 | 49.24 / 49.03-49.34 | 1.14 (2.4%) | 46.88-53.02 | -2.3% / -6.8% | -0.8% | 36.8M |
| XOM | 160.44 (10:04 iex) | +1.5% | 158.08 | 159.76 / 159.59-160.94 | 3.48 (2.2%) | 156.67-187.32 | -5.3% / -5.9% | -1.6% | 15.5M |
| CVX | 214.18 (10:05 iex) | +1.5% | 210.95 | 213.14 / 213.00-214.79 | 4.36 (2.1%) | 204.31-234.53 | -1.6% / -1.2% | +2.5% | 8.7M |
| LLY | 1,384.48 (10:04 iex) | -0.6% | 1,392.22 | 1,388.78 / 1,383.73-1,404.28 | 40.02 (2.9%) | 1,328.39-1,475.25 | -0.5% / +8.7% | +0.7% | 3.3M |
| UNH | 351.74 (10:05 iex) | +1.6% | 346.19 | 350.50 / 349.00-353.56 | 15.91 (4.6%) | 319.13-416.11 | -9.9% / -10.4% | -1.1% | 7.6M |
| JNJ | 273.93 (10:05 iex) | -0.0% | 273.94 | 272.86 / 272.62-275.03 | 6.46 (2.4%) | 263.37-288.81 | -0.2% / +2.8% | +1.0% | 8.3M |
| WMT | 132.15 (10:04 iex) | +0.2% | 131.94 | 131.81 / 131.69-132.34 | 2.81 (2.1%) | 119.66-133.19 | +3.8% / +11.8% | +3.6% | 25.0M |
| COST | 1,096.04 (10:04 iex) | +0.8% | 1,086.81 | 1,085.17 / 1,085.17-1,097.00 | 17.93 (1.6%) | 956.23-1,098.00 | +3.9% / +11.9% | +1.9% | 2.7M |
| HD | 361.44 (10:04 iex) | +0.0% | 361.26 | 360.00 / 358.10-362.50 | 9.45 (2.6%) | 322.68-363.65 | +4.8% / +13.7% | +7.0% | 5.4M |
| CAT | 553.34 (10:05 iex) | +1.8% | 543.69 | 560.82 / 551.54-562.74 | 28.98 (5.3%) | 508.11-664.47 | -6.1% / -22.2% | -2.7% | 4.3M |
| BA | 166.07 (10:04 iex) | +0.9% | 164.53 | 167.50 / 164.59-167.50 | 5.23 (3.2%) | 155.56-179.19 | -2.6% / -9.3% | +1.0% | 8.0M |
| DAL | 83.45 (10:03 iex) | +0.6% | 82.95 | 83.81 / 83.19-84.05 | 3.10 (3.7%) | 78.66-92.52 | -2.9% / +0.4% | -2.3% | 5.9M |
| UAL | 105.34 (10:03 iex) | +0.8% | 104.52 | 106.06 / 104.64-106.11 | 5.09 (4.9%) | 100.28-122.08 | -4.9% / -3.1% | -2.9% | 5.5M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SNDK | 79.26 (10:05 iex) | +7.7% | 73.61 | 79.92 / 77.10-80.69 | 12.56 (17.1%) | 67.02-173.23 | -33.1% / -54.4% | -24.1% | 116.1M |
| NU | 13.05 (10:05 iex) | +5.6% | 12.36 | 13.42 / 13.04-13.52 | 0.61 (5.0%) | 11.21-13.25 | +2.7% / -7.3% | +2.3% | 70.6M |
| SHOP | 140.42 (10:04 iex) | +5.3% | 133.40 | 139.04 / 138.57-142.16 | 8.17 (6.1%) | 122.83-168.55 | -7.9% / -13.0% | -4.3% | 8.6M |
| PINS | 20.73 (10:05 iex) | +5.1% | 19.71 | 19.96 / 19.81-20.75 | 0.92 (4.6%) | 16.30-21.60 | +4.3% / -0.7% | +11.4% | 15.1M |
| CHTR | 154.56 (10:05 iex) | +4.9% | 147.27 | 147.88 / 146.87-154.81 | 8.37 (5.7%) | 106.04-147.88 | +14.8% / +24.8% | +5.8% | 3.1M |
| DELL | 310.31 (10:05 iex) | +4.5% | 297.06 | 307.02 / 297.10-312.42 | 38.53 (13.0%) | 265.00-493.50 | -14.7% / -34.9% | -5.1% | 10.3M |
| BABA | 90.04 (10:04 iex) | +4.4% | 86.26 | 89.94 / 89.50-90.58 | 4.01 (4.6%) | 80.96-111.17 | -9.4% / -16.2% | +2.2% | 13.6M |
| LYFT | 17.67 (10:05 iex) | +4.1% | 16.97 | 17.16 / 17.10-17.68 | 0.92 (5.4%) | 15.65-18.84 | +0.4% / +3.9% | -3.6% | 12.0M |
| VRTX | 517.26 (10:05 iex) | -8.3% | 564.12 | 516.50 / 502.90-522.28 | 15.75 (2.8%) | 513.80-571.75 | +3.9% / +7.4% | +5.2% | 1.6M |
| DLTR | 149.02 (10:01 iex) | -2.1% | 152.21 | 152.00 / 149.02-153.78 | 5.92 (3.9%) | 127.52-156.99 | +8.7% / +19.7% | +6.9% | 2.6M |
| TJX | 143.12 (10:05 iex) | -2.0% | 146.09 | 145.27 / 143.03-145.97 | 4.30 (2.9%) | 129.39-147.44 | +5.7% / +6.1% | +4.1% | 8.3M |
| MRNA | 216.91 (10:05 iex) | -1.8% | 220.84 | 223.95 / 215.98-229.35 | 17.66 (8.0%) | 189.98-280.80 | -2.8% / +4.0% | +12.2% | 9.6M |
| NCLH | 16.70 (10:04 iex) | -1.8% | 17.00 | 17.23 / 16.66-17.23 | 0.76 (4.5%) | 15.94-19.09 | -4.2% / +5.6% | -5.5% | 21.1M |
| PANW | 349.99 (10:04 iex) | -1.7% | 356.14 | 343.44 / 338.57-354.01 | 19.84 (5.6%) | 301.28-390.00 | +4.8% / -2.7% | +4.8% | 8.2M |
| RCL | 309.54 (10:04 iex) | -1.5% | 314.11 | 318.01 / 309.07-318.01 | 12.50 (4.0%) | 295.21-342.32 | -1.5% / +8.4% | -2.0% | 2.0M |
| TMO | 675.93 (10:05 iex) | -1.4% | 685.52 | 687.99 / 675.11-688.84 | 19.80 (2.9%) | 661.60-727.56 | -1.5% / +0.5% | -1.0% | 1.9M |
