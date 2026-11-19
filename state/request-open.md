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

# Pre-market brief: Thursday 2026-11-19, 09:05 ET (15:05 Stockholm; ET+6 today, per the book state)

I'm opening nothing new today and leaving both shorts (GLD, HD) on their brackets.

## 1. Tape

**Overnight and pre-market**
- S&P futures are up about 1% and Nasdaq-100 futures about 1.8–2%. SPY is at 737.72 (+1.0%) and QQQ at 671.70 (+1.8%). This follows five straight S&P declines.
- The bounce is mostly about one deal. Anthropic priced its IPO at $83, above its $70–78 range. It raised about $81.3B at roughly a $1.5T fully diluted valuation, the largest IPO on record, and lists today as ANT.
- That lifted the companies that own stakes in it: GOOGL is +4.1% (about 1.8B shares, worth roughly $149B at $83) and AMZN +1.7%.
- It also lifted AI infrastructure (SMH +2.5%; STX, WDC and SNDK up about 5% after a week of heavy losses).
- PANW is +8.6% after raising its full-year guidance, and other cybersecurity names followed: CRWD +5.5%, NET +4.5%, with ZS and FTNT also up.

**Macro**
- The backdrop is still hostile. The 10-year yield is about 5.08% and DXY about 103.8, near a 19-month high.
- A December 9 hike is about 90% priced for 25bp, with about 10% on 50bp after Waller raised the half-point option.
- This morning's data was softer: claims 203K against 197K expected, and Philly Fed 6.3 against about 20. Futures did not react much.
- Defensives and gold are lagging: XLP −0.8%, WMT −1.6% after its report, and GLD at its 20-day low.

**Regime and edge**
- The regime is a downtrend: SPY is 3.1% under its 20-day average and below its 50-day. Today's relief bounce rests on a single event.
- I see **no edge at the open**. Over the 1–5 day horizon, the short side has the slight edge, given rates, the dollar and the trend.
- I could not verify a current VIX level; the last figure I found was 19.45 on Nov 11.

## 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Initial jobless claims (week to Nov 14) | **203K** vs 197K expected (prior revised 202K). Continuing claims 1.763M (+70K). Slightly soft; futures barely moved. | GLD (rates/dollar) |
| 08:30 | 14:30 | Philly Fed manufacturing (Nov) | **6.3** vs about 20 expected (prior 20.9). Employment index 11.6. One headline says prices paid jumped, but I couldn't verify the figure. Bearish for the dollar on paper; DXY is still about 103.8. | GLD |
| Pre-mkt | – | WMT Q3 FY27 | Adj. EPS $0.65 vs $0.64; revenue $188.84B vs $187.27B; US comps +2.9%, in line. Full-year EPS guide raised to $2.84–2.89 from $2.80–2.87. Stock 125.36 (−1.6%). One analysis puts Q4 guidance at $0.73–0.78 vs $0.78 consensus; not verified at source. | HD (read-across), WMT idea |
| Pre-mkt | – | PDD Q3 | Revenue flat on the year at RMB108.3B; net income RMB29.5B vs 29.3B a year ago. Stock +5.7%. I didn't verify the consensus. | – |
| Pre-mkt | – | WSM Q3 | Comps +5.1%; full-year outlook reiterated (8-K). Yahoo's snapshot has it −7%; not in my data table, price not verified. | – |
| ~10:00 | ~16:00 | Possibly existing home sales / LEI | **Not verified as scheduled today.** | HD |
| After the 09:30 open (likely late morning) | – | ANT (Anthropic) first trade on Nasdaq | Priced at $83. Volatility source for GOOGL, AMZN and AI names. ANT itself is not tradable here (no volume history). | – |
| After close | – | INTU, GAP, BULL earnings | – | – |
| Fri Nov 20 | – | Possible first GTA VI sales disclosure (Oppenheimer) | Company event for TTWO | TTWO idea |
| Dec 9 | – | FOMC | 25bp hike about 90% priced | GLD |

Thanksgiving week is next. The market is closed Nov 26 and closes early Nov 27. Resting entries are cleared before weekends and holidays.

## 3. Open positions and resting entries

**GLD short** (session 2 of 10, entry 345.91, stop 355.50, target 330.00; last 340.37)
- **Invalidation met? No.** It needs DXY below 102.50 *and* December-hike odds below 70%.
  - DXY is about 103.8 (TradingView and FXEmpire, Nov 18–19).
  - CME FedWatch as reported Thursday shows about 90% for 25bp plus 10% for 50bp.
- The Philly Fed miss is a dovish data point, but it does not meet either condition.
- **Hold**; the bracket is unchanged.

**HD short** (session 3 of 10, entry 343.57, stop 353.50, target 323.50; last 333.58)
- **Invalidation met? No.** It needs a close above 347.51; the prior close was 337.64, and it is 333.58 pre-market.
- HD has no binary event of its own ahead (it reported Nov 17).
- **Hold**; the bracket is unchanged.

**Resting entries:** none.

## 4. New plays

**None.** No candidate cleared the bar of a catalyst verified at source, conviction 3 or higher, and positive expected value on my own numbers:

- **The verified catalysts are already priced.**
  - PANW has moved about 3 ATR in two sessions: +9.9% Wednesday before the report, then +8.6% pre-market.
  - GOOGL's move is a mark on an IPO that prices out after the review has run.
- **The short ideas don't pay enough.** At the 38% base rate, none of them reaches positive EV with a stop outside one ATR.

## 5. Both sides

**Best long: PANW. Passed at conviction 2.**
- **Levels:** market about 369.00, stop 347.00, target 405.00. That is 1.64R at P 0.38, so EV ≈ 0.00R.
- **The catalyst is verified at source.** The [SEC 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000030/ex991q127earningsrelease.htm) dated Nov 18:
  - Revenue $3.44B (+39%); next-generation security ARR $9.73B (+66%); RPO $21.0B (+35%).
  - Full-year revenue guidance $14.52–14.57B, up from $14.10–14.20B per Reuters; full-year non-GAAP EPS $4.26–4.30.
  - Applied Compute acquisition, $4.5B per Reuters.
  - At least nine brokers raised targets to $370–460 (KeyBanc and Piper $450, BTIG $442).
- **Why I'm passing anyway:**
  - The stock was about 309 on Tuesday. It has gained about 60 points (3 ATR at an ATR of 20.2) into and on the print.
  - The consensus target (about 400–406) and the 20-day high (406.88) leave about 36 points of room. A stop outside the gap's 353 support has to sit about 22 points away.
  - Starting from the 38% base rate (and my 35–40% bucket has hit only 29%), the EV is zero.
  - Next earnings: inferred mid-to-late Feb 2027, not confirmed.

**Best short: WMT. Passed at conviction 2.**
- **Levels:** market 125.36, stop 130.00, target 118.00. That is 1.59R at P 0.37, so EV ≈ −0.04R.
- **The catalyst is verified** via [CNBC](https://www.cnbc.com/2026/11/19/walmart-wmt-q3-2026-earnings.html):
  - A narrow beat; comps of 2.9% in line and slowing from 4.5% a year earlier.
  - A small raise to the full-year guide (EPS midpoint up about 1%).
  - About 40x forward earnings, and the stock ran up into the print (+10% vs its 50-day average).
- **Why I'm passing:**
  - The reaction is only 0.65 ATR.
  - After its February 2026 report, WMT reversed a 3% pre-market drop the same morning.
  - To clear the 20-day high noise, the stop has to sit 1.5 ATR away.

**Other shorts I looked at:**
- TTWO: sell-the-news on GTA VI launch day, but a possible sales disclosure tomorrow.
- CRM: relative weakness, no bounce on a +1.8% Nasdaq day.
- NEM: the same gold factor as the GLD short I already hold.
- BABA: below its 20-day low, but −17% in 5 days, and its results timing is conflicting.

## 6. Passing on

- **PANW long** (369.00 / 347.00 / 405.00, P 0.38): a 3-ATR two-day run leaves too little room; EV about zero.
- **WMT short** (125.36 / 130.00 / 118.00, P 0.37): small reaction, needs a wide stop, and WMT has a history of reversing post-print drops. EV negative.
- **GOOGL long** (293.88 / 278.50 / 318.00, P 0.36): today's gap is the market pricing its Anthropic stake. The listing comes after the review, and sell-the-news on the debut is the obvious risk. EV about −0.07R.
- **TTWO short** (limit 212.00 / 226.00 / 190.00, P 0.34):
  - The stock is −3.1% on launch day despite the 99 Metacritic score and about $1.65B in first sales (Sensor Tower).
  - A company sales disclosure could come Nov 20 and gap it either way. EV −0.13R.
- **CRM short** (sell stop 186.00 under the 186.45 20-day low / 196.50 / 172.00, P 0.38): only 1.33R. Its own earnings are probably inside the horizon; I didn't verify the date this session.
- **NEM short** (sell stop 102.00 / 108.00 / 93.00, P 0.37): it would double the gold/rates factor I already hold in GLD.
- **TGT long:** yesterday's condition was half met. WMT did not cut its full-year guidance, but **I could not verify a current TGT price**, so it gets no levels and no order.
- **PDD long:** revenue was flat on the year and I couldn't verify the consensus. It is a China ADR facing the new US chip and data-center rules. No levels.
- **ANT:** a new listing with no volume history, so it is outside the universe.

## 7. For the post-open review

- **PANW:**
  - The default is pass.
  - The review may buy at market at **risk 0.5**, stop 347.00, target 405.00, only if both of these are true:
    - (a) PANW's 09:30–10:00 low is at or above 360.00 (the gap is holding);
    - (b) it trades between 368 and 375 at 10:05.
  - Above 375 the reward falls below 1.3R; do not chase it.
  - If it trades below 353.36 (the gap support), drop the idea for the session.
- **GLD:** close only if DXY is below 102.50 *and* December-hike odds are below 70%. Neither is close.
- **HD:** close only on a daily close above 347.51. The review cannot see the close, so tomorrow's brief checks it.
- **WMT:** no action whatever the opening range does; the needed stop distance doesn't improve intraday.

## 8. Book state

| | Now | Cap |
|---|---|---|
| Gross exposure | 36% | 150% |
| Net exposure | −36% | ±100% |
| Risk at stake | 1.05% of equity | 4% |
| Slots | 2 of 8 | |
| Consumer Discretionary net | −16% (HD) | 40% |

No new orders, so nothing changes.

```json
{
  "date": "2026-11-19",
  "no_trade": true,
  "session_note": "Anthropic-IPO relief bounce (NQ +1.8-2%) inside a hawkish-Fed downtrend (10y 5.08%, DXY ~103.8, Dec hike ~90%+); verified catalysts are already priced (PANW ~3 ATR in two sessions) and shorts (WMT, TTWO) lack reward:risk at the base rate. Would act on PANW only if the 09:30-10:00 low holds >=360 and it trades 368-375 at 10:05 (stop 347, target 405, 0.5 risk). GLD and HD held: invalidations unmet.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "PANW",
      "direction": "long",
      "entry_type": "market",
      "entry": 369.00,
      "stop": 347.00,
      "targets": [405.00],
      "p_target_first": 0.38,
      "reason": "Verified FQ1'27 beat-and-raise (8-K Nov 18: rev +39%, NGS ARR +66%, FY rev guide $14.52-14.57B from $14.10-14.20B; 9+ PT raises), but +9.9% Wed and +8.6% pre-market = ~3 ATR already; only ~36 pts to the 406.88 20d high / ~$406 consensus PT against a 22-pt stop. EV ~0 at base rate. Conviction 2."
    },
    {
      "ticker": "WMT",
      "direction": "short",
      "entry_type": "market",
      "entry": 125.36,
      "stop": 130.00,
      "targets": [118.00],
      "p_target_first": 0.37,
      "reason": "Narrow Q3 beat, in-line 2.9% comps, small FY guide raise, ~40x forward and +10% vs 50d into print; but the reaction is only -1.6% (0.65 ATR), WMT reversed a similar dip in Feb 2026, and the stop must be 1.5 ATR. EV about -0.04R. Conviction 2."
    },
    {
      "ticker": "GOOGL",
      "direction": "long",
      "entry_type": "market",
      "entry": 293.88,
      "stop": 278.50,
      "targets": [318.00],
      "p_target_first": 0.36,
      "reason": "+4.1% on the mark-to-market of its ~1.8B-share Anthropic stake after the $83 IPO pricing; the ANT debut comes after the review with clear sell-the-news risk, the stock is -13% vs its 50d avg in a falling tape, and it needs a 1.6 ATR stop. EV about -0.07R."
    },
    {
      "ticker": "TTWO",
      "direction": "short",
      "entry_type": "limit",
      "entry": 212.00,
      "stop": 226.00,
      "targets": [190.00],
      "p_target_first": 0.34,
      "reason": "Sell-the-news on GTA VI launch day (-3.1% pre-market despite a 99 Metacritic score and ~$1.65B first sales per Sensor Tower), but a possible company sales disclosure Nov 20 could gap it higher; ATR 6%. EV about -0.13R."
    },
    {
      "ticker": "CRM",
      "direction": "short",
      "entry_type": "stop",
      "entry": 186.00,
      "stop": 196.50,
      "targets": [172.00],
      "p_target_first": 0.38,
      "reason": "Relative weakness (flat on a +1.8% Nasdaq morning, -15% vs 20d avg) and AI-disruption pressure on software around the Anthropic listing, but only 1.33R, and its own early-December earnings (not verified this session) likely fall inside the horizon."
    },
    {
      "ticker": "NEM",
      "direction": "short",
      "entry_type": "stop",
      "entry": 102.00,
      "stop": 108.00,
      "targets": [93.00],
      "p_target_first": 0.37,
      "reason": "Breakdown under the 102.35 20d low with gold falling, but it is the same real-rates/dollar factor as the open GLD short; adding it doubles one bet."
    }
  ]
}
```

Sources:
- [Yahoo Finance live, Nov 19 (futures, WMT, ANT pricing, movers, oil, gold, 10y)](https://finance.yahoo.com/markets/live/stock-market-today-thursday-november-19-dow-sp-500-nasdaq-anthropic-ipo-090910916.html)
- [Stocktwits: futures before the Anthropic debut (NVDA, BABA, TTWO, after-close earnings)](https://stocktwits.com/news-articles/markets/equity/stock-futures-climb-ahead-of-anthropic-s-nasdaq-debut-nvda-baba-ttwo-sls-stocks-in-focus/cNbiED8R9iw)
- [Reuters via Investing.com: weekly jobless claims](https://www.investing.com/news/economy-news/us-weekly-jobless-claims-increase-slightly-5039110)
- [FXStreet: claims 203K](https://www.fxstreet.com/news/us-initial-jobless-claims-rose-to-203k-last-week-202611191337)
- [Newsquawk: Philly Fed 6.3 vs 20 expected](https://www.newsquawk.com/headlines/us-philadelphia-fed-manufacturing-index-nov-63-vs-exp-20-prev-209)
- [mlq.ai: claims and Philly Fed headline (page blocked; headline only)](https://mlq.ai/news/jobless-claims-edge-up-to-203000-as-the-philadelphia-fed-index-falls-to-a-six-month-low-and-prices-paid-jump/)
- [CNBC: Walmart Q3 FY27](https://www.cnbc.com/2026/11/19/walmart-wmt-q3-2026-earnings.html)
- [TradingKey: Walmart earnings today](https://www.tradingkey.com/analysis/stocks/us-stocks/262312955-walmart-earnings-today-wmt-three-report-losing-streak-125-10-november-19-2026-tradingkey)
- [Palo Alto Networks FQ1'27 release (SEC 8-K exhibit)](https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000030/ex991q127earningsrelease.htm)
- [Reuters via Investing.com: Palo Alto raises forecast, $4.5B Applied Compute deal](https://www.investing.com/news/stock-market-news/palo-alto-raises-annual-forecast-signs-45-billion-deal-for-applied-compute-5037460)
- [MarketScreener/Reuters: Palo Alto forecast powers cyber rally](https://www.marketscreener.com/news/palo-alto-s-raised-sales-forecast-powers-cybersecurity-stock-rally-ce785ed2d88cfe24)
- [TradingKey: PANW levels and Wednesday close](https://www.tradingkey.com/analysis/stocks/us-stocks/262312701-palo-alto-networks-raises-outlook-applied-compute-deal-panw-389-93-november-19-2026-tradingkey)
- [TipRanks/TheFly: PANW target raises](https://www.tipranks.com/news/the-fly/palo-alto-networks-price-target-raised-to-442-from-425-at-btig-thefly-news)
- [CoinCentral: today's market movers](https://coincentral.com/todays-market-movers-anthropic-google-palo-alto-walmart-and-more)
- [Invezz: Alphabet +4% on the Anthropic IPO](https://invezz.com/news/2026/11/19/alphabet-stock-rises-4-as-anthropic-ipo-boosts-investor-optimism/)
- [Blockonomi: Alphabet's stake valued at $149B](https://blockonomi.com/alphabet-googl-stock-rises-4-as-anthropic-ipo-values-googles-stake-at-149b/)
- [TradingView: DXY 103.91, Waller's 50bp option](https://www.tradingview.com/news/binance_news:5204ef80c094b:0-dollar-index-rises-to-103-91-highest-since-april-2025-as-fed-s-waller-reportedly-raises-50-bp-hike-option/)
- [FXEmpire: DXY holds 103.76](https://www.fxempire.com/forecasts/article/us-dollar-price-forecast-dxy-holds-103-76-as-fed-minutes-back-hikes-eur-usd-and-gbp-usd-stay-weak-1645653)
- [TipRanks: markets brace for claims after the minutes](https://www.tipranks.com/news/markets-brace-for-u-s-jobless-claims-and-factory-data-after-fed-minutes-lock-in-rate-hike-bets)
- [GlobeNewswire: PDD Q3 2026 results](https://www.globenewswire.com/news-release/2026/11/19/3406398/0/en/pdd-holdings-announces-third-quarter-2026-unaudited-financial-results.html)
- [Williams-Sonoma Q3 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0000719955/000071995526000244/exhibit991fy2026q3earnings.htm)
- [Yahoo: GTA VI sales top $1.6B](https://finance.yahoo.com/markets/stocks/articles/gta-vi-sales-top-1-093642746.html)
- [GuruFocus: TTWO on the 99 Metacritic score](https://www.gurufocus.com/news/9207732/taketwo-stocks-rise-485-premarket-as-gta-vi-hits-99-metacritic-before-launch)
- [TheStreet: VIX 19.45 (Nov 11)](https://pro.thestreet.com/stock-market-today/stocks-and-the-vix-fell-together-tuesday-heres-what-usually-comes-next)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Thursday 2026-11-19. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$103,111.28**
- Cash: $140,670.03
- Session P&L so far: +0.13% (new entries are blocked at -3.0%)
- Gross exposure: $37,559 (36% of equity, cap 150%)
- Net exposure: $-37,559 (-36%, cap +/-100%)
- Risk at stake (entry to stop): $1,082 (1.05% of equity, cap 4.0%) — 2.95% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 345.91 | 339.92 | +359 (+1.7%) | -20% | 355.50 | 330.00 |
| HD | short | 51 | 343.57 | 336.54 | +359 (+2.0%) | -17% | 353.50 | 323.50 |

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

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GLD | 339.90 (10:04 iex) | -0.4% | 341.19 | 339.88 / 339.20-340.52 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| HD | 335.67 (10:03 iex) | -0.6% | 337.64 | 335.00 / 332.34-336.38 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 737.23 (10:05 iex) | +1.0% | 730.20 | 737.46 / 735.42-739.90 | 14.32 (2.0%) | 726.79-775.64 | -3.1% / -4.2% | -3.9% | 51.4M |
| QQQ | 673.12 (10:05 iex) | +2.1% | 659.51 | 671.09 / 670.13-675.20 | 19.71 (3.0%) | 646.64-726.14 | -3.9% / -7.7% | -4.5% | 51.8M |
| IWM | 269.82 (10:04 iex) | -0.1% | 270.12 | 271.07 / 269.12-271.80 | 5.84 (2.2%) | 267.87-286.17 | -2.8% / -3.3% | -4.6% | 24.2M |
| DIA | 502.08 (10:05 iex) | +0.1% | 501.73 | 503.95 / 501.17-504.43 | 8.81 (1.8%) | 500.03-536.60 | -3.5% / -3.1% | -4.3% | 3.8M |
| TLT | 79.90 (10:04 iex) | -0.4% | 80.22 | 80.08 / 79.86-80.10 | 0.73 (0.9%) | 79.11-82.42 | -0.9% / +0.6% | -0.9% | 36.4M |
| GLD | 339.90 (10:04 iex) | -0.4% | 341.19 | 339.88 / 339.20-340.52 | 7.92 (2.3%) | 340.76-380.18 | -6.3% / -9.7% | -6.6% | 10.0M |
| USO | 138.86 (10:03 iex) | +2.0% | 136.11 | 138.96 / 138.73-139.45 | 5.75 (4.2%) | 135.01-171.82 | -10.9% / -10.7% | -3.8% | 5.1M |
| SMH | 478.16 (10:04 iex) | +4.1% | 459.54 | 472.70 / 471.32-479.96 | 28.70 (6.2%) | 445.32-571.00 | -8.9% / -16.9% | -9.4% | 12.1M |
| XLK | 168.83 (10:04 iex) | +3.1% | 163.81 | 167.47 / 167.18-169.30 | 6.73 (4.1%) | 159.63-191.55 | -6.5% / -11.8% | -6.1% | 13.3M |
| XLF | 56.37 (10:04 iex) | -0.1% | 56.42 | 56.51 / 56.28-56.63 | 1.06 (1.9%) | 55.74-60.04 | -1.5% / +0.9% | -3.8% | 35.6M |
| XLE | 61.29 (10:04 iex) | +0.0% | 61.29 | 61.71 / 61.26-61.94 | 1.81 (3.0%) | 60.43-70.15 | -6.3% / -5.4% | -3.3% | 37.1M |
| XLV | 178.97 (10:05 iex) | -1.2% | 181.17 | 180.40 / 178.58-181.25 | 3.73 (2.1%) | 177.07-192.32 | -1.9% / +3.0% | -4.1% | 12.0M |
| XLI | 164.82 (10:04 iex) | +0.1% | 164.66 | 165.76 / 164.37-166.00 | 3.56 (2.2%) | 161.74-172.40 | -1.7% / -2.2% | -3.7% | 8.9M |
| XLY | 118.97 (10:04 iex) | -0.2% | 119.20 | 119.59 / 118.74-119.71 | 2.79 (2.3%) | 112.83-122.92 | +1.2% / +4.5% | -1.5% | 9.2M |
| XLP | 89.50 (10:05 iex) | -1.8% | 91.18 | 90.03 / 89.33-90.15 | 1.67 (1.8%) | 86.36-93.48 | +1.1% / +6.0% | -0.3% | 20.0M |
| XLU | 43.13 (10:05 iex) | -1.0% | 43.55 | 43.33 / 43.04-43.44 | 0.60 (1.4%) | 42.01-44.40 | +0.4% / +4.0% | -0.6% | 23.9M |
| XLB | 50.12 (10:04 iex) | -0.7% | 50.46 | 50.29 / 49.87-50.35 | 1.09 (2.2%) | 50.12-54.63 | -3.3% / -0.7% | -4.8% | 12.2M |
| XLRE | 43.28 (10:04 iex) | -0.8% | 43.62 | 43.52 / 43.23-43.52 | 0.66 (1.5%) | 41.78-45.34 | -0.1% / +2.5% | -2.2% | 7.9M |
| XLC | 105.98 (10:05 iex) | +0.4% | 105.58 | 106.72 / 105.76-107.11 | 2.21 (2.1%) | 99.33-109.26 | +0.6% / -3.1% | -2.8% | 7.9M |
| KRE | 70.40 (10:04 iex) | -0.2% | 70.52 | 70.60 / 70.25-70.86 | 1.54 (2.2%) | 70.19-75.80 | -2.8% / -1.3% | -3.3% | 14.5M |
| XHB | 99.71 (10:03 iex) | -1.0% | 100.75 | 100.44 / 99.18-100.48 | 3.28 (3.3%) | 94.86-108.78 | -0.8% / +2.4% | -2.3% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 349.69 (10:05 iex) | -0.8% | 352.45 | 353.01 / 348.50-355.28 | 9.43 (2.7%) | 325.08-360.83 | +1.4% / +3.4% | -0.8% | 48.2M |
| MSFT | 523.22 (10:05 iex) | +3.1% | 507.31 | 519.50 / 518.30-526.49 | 17.88 (3.5%) | 495.55-558.07 | -3.4% / -2.2% | -2.5% | 28.2M |
| NVDA | 156.16 (10:05 iex) | +3.4% | 150.96 | 152.91 / 152.54-158.13 | 11.92 (7.9%) | 148.80-219.99 | -20.1% / -28.2% | -13.1% | 250.9M |
| AMZN | 271.44 (10:05 iex) | +1.4% | 267.74 | 272.57 / 270.77-274.00 | 11.00 (4.1%) | 229.36-275.34 | +4.1% / +4.9% | +0.6% | 50.4M |
| GOOGL | 293.81 (10:04 iex) | +4.0% | 282.44 | 294.30 / 289.74-295.43 | 9.50 (3.4%) | 276.92-331.43 | -4.2% / -13.1% | -3.8% | 42.4M |
| META | 626.34 (10:04 iex) | +1.6% | 616.38 | 624.60 / 621.67-630.06 | 20.75 (3.4%) | 583.80-681.07 | -1.4% / -9.3% | -2.0% | 22.4M |
| TSLA | 386.68 (10:05 iex) | +0.8% | 383.72 | 389.90 / 385.38-393.60 | 17.96 (4.7%) | 338.15-414.23 | -0.6% / +2.1% | -1.8% | 37.7M |
| AVGO | 366.31 (10:05 iex) | +3.5% | 354.05 | 362.99 / 361.65-369.26 | 20.97 (5.9%) | 289.77-369.82 | +6.6% / +2.9% | +2.6% | 28.3M |
| AMD | 545.08 (10:04 iex) | +2.8% | 530.14 | 542.17 / 537.09-554.99 | 50.16 (9.5%) | 402.10-594.00 | +3.0% / -4.5% | -4.1% | 37.5M |
| ORCL | 117.17 (10:04 iex) | +2.9% | 113.89 | 116.67 / 116.01-118.50 | 8.36 (7.3%) | 109.21-148.48 | -8.5% / -14.8% | -11.3% | 41.2M |
| NFLX | 60.10 (10:05 iex) | +0.5% | 59.82 | 60.03 / 59.88-60.45 | 1.85 (3.1%) | 59.41-67.82 | -5.3% / -12.2% | -7.3% | 40.6M |
| CRM | 193.08 (10:04 iex) | +1.4% | 190.40 | 191.63 / 191.35-195.39 | 8.49 (4.5%) | 186.45-252.42 | -15.1% / -18.0% | -12.7% | 7.2M |
| JPM | 326.27 (10:05 iex) | +0.7% | 324.11 | 326.38 / 325.87-328.27 | 8.50 (2.6%) | 323.71-359.80 | -4.2% / -4.2% | -5.6% | 6.6M |
| GS | 885.58 (10:03 iex) | +1.4% | 873.18 | 885.55 / 879.98-891.25 | 30.40 (3.5%) | 854.45-939.38 | -2.9% / -4.3% | -5.8% | 2.1M |
| BAC | 49.10 (10:05 iex) | +0.4% | 48.91 | 49.31 / 48.95-49.37 | 1.23 (2.5%) | 48.74-53.02 | -2.8% / -8.2% | -3.5% | 34.4M |
| XOM | 159.92 (10:05 iex) | -0.4% | 160.58 | 161.32 / 159.95-162.07 | 4.86 (3.0%) | 159.11-187.32 | -6.9% / -4.7% | -3.1% | 14.6M |
| CVX | 206.25 (10:05 iex) | +0.2% | 205.88 | 207.48 / 206.21-208.11 | 5.58 (2.7%) | 204.31-234.53 | -6.2% / -3.7% | -2.7% | 8.3M |
| LLY | 1,364.74 (10:05 iex) | -1.3% | 1,382.75 | 1,369.38 / 1,361.97-1,382.00 | 46.44 (3.4%) | 1,256.10-1,475.25 | +0.4% / +10.1% | -3.7% | 3.1M |
| UNH | 342.22 (10:04 iex) | -2.2% | 349.91 | 351.13 / 340.19-353.85 | 14.59 (4.2%) | 342.45-426.55 | -13.2% / -10.4% | -13.2% | 5.6M |
| JNJ | 266.41 (10:05 iex) | -2.3% | 272.70 | 269.61 / 265.79-270.60 | 7.08 (2.6%) | 259.04-290.25 | -0.7% / +2.0% | -2.7% | 7.6M |
| WMT | 125.61 (10:05 iex) | -1.4% | 127.36 | 123.68 / 123.27-125.67 | 3.09 (2.4%) | 117.83-131.82 | +2.2% / +10.0% | +1.3% | 22.3M |
| COST | 1,087.95 (10:04 iex) | -0.8% | 1,096.62 | 1,089.56 / 1,086.24-1,094.56 | 21.91 (2.0%) | 978.87-1,123.67 | +4.6% / +12.1% | +0.8% | 2.5M |
| HD | 335.67 (10:03 iex) | -0.6% | 337.64 | 335.00 / 332.34-336.38 | 10.42 (3.1%) | 313.56-362.44 | -0.1% / +7.6% | -3.9% | 4.8M |
| CAT | 563.81 (10:04 iex) | +0.9% | 558.77 | 567.94 / 559.03-569.77 | 27.74 (5.0%) | 550.81-732.73 | -9.9% / -22.9% | -7.1% | 4.0M |
| BA | 163.73 (10:03 iex) | +0.5% | 162.91 | 163.80 / 163.11-164.22 | 4.74 (2.9%) | 161.75-193.19 | -6.1% / -12.4% | -6.7% | 10.5M |
| DAL | 84.78 (10:04 iex) | -0.1% | 84.88 | 85.08 / 83.30-85.30 | 3.24 (3.8%) | 75.33-92.52 | +0.4% / +3.3% | -7.1% | 6.0M |
| UAL | 107.30 (10:04 iex) | -0.3% | 107.63 | 107.41 / 105.09-107.55 | 5.50 (5.1%) | 96.39-122.08 | -1.2% / -0.4% | -9.1% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| PDD | 86.82 (10:05 iex) | +12.1% | 77.45 | 82.44 / 82.02-87.38 | 2.57 (3.3%) | 76.27-85.42 | -2.5% / -2.3% | -2.0% | 5.8M |
| ZS | 217.06 (10:05 iex) | +9.7% | 197.83 | 202.01 / 201.46-218.10 | 12.34 (6.2%) | 180.47-267.87 | -9.6% / -6.2% | +2.1% | 2.4M |
| STX | 565.19 (10:05 iex) | +9.6% | 515.90 | 546.90 / 536.54-565.38 | 49.84 (9.7%) | 449.28-718.65 | -10.0% / -28.2% | -6.5% | 6.0M |
| OKTA | 213.90 (10:04 iex) | +9.4% | 195.61 | 203.25 / 202.00-214.33 | 14.91 (7.6%) | 164.18-228.72 | +1.1% / -1.6% | +7.3% | 4.9M |
| WDC | 315.03 (10:05 iex) | +9.3% | 288.19 | 306.17 / 300.82-315.74 | 27.33 (9.5%) | 258.61-402.23 | -11.1% / -24.2% | -8.0% | 8.4M |
| INTC | 59.36 (10:05 iex) | +8.6% | 54.67 | 57.54 / 57.28-59.32 | 6.11 (11.2%) | 51.51-95.68 | -19.8% / -40.7% | -12.5% | 147.0M |
| DDOG | 181.29 (10:04 iex) | +8.5% | 167.11 | 174.80 / 173.66-182.39 | 14.90 (8.9%) | 162.11-285.00 | -21.6% / -30.6% | -9.4% | 4.8M |
| SNDK | 833.60 (10:05 iex) | +7.4% | 776.22 | 811.47 / 804.01-846.76 | 111.84 (14.4%) | 749.39-1,408.45 | -25.2% / -43.9% | -20.6% | 12.9M |
| ZTS | 82.21 (10:04 iex) | -3.9% | 85.57 | 84.84 / 82.18-85.13 | 3.19 (3.7%) | 76.51-89.29 | +4.4% / +11.8% | +3.6% | 4.6M |
| MO | 73.59 (10:05 iex) | -3.5% | 76.26 | 75.30 / 73.54-75.45 | 1.71 (2.2%) | 72.30-79.97 | -0.3% / +4.9% | -1.5% | 8.3M |
| PM | 186.18 (10:04 iex) | -3.4% | 192.73 | 190.26 / 186.07-191.54 | 5.29 (2.7%) | 191.07-214.35 | -4.0% / -1.9% | -1.8% | 4.9M |
| KO | 94.91 (10:05 iex) | -3.2% | 98.09 | 96.21 / 94.73-96.68 | 1.81 (1.8%) | 90.58-100.56 | +2.6% / +7.3% | +0.5% | 18.7M |
| W | 106.00 (10:05 iex) | -3.1% | 109.35 | 107.85 / 105.68-108.68 | 7.07 (6.5%) | 105.17-127.99 | -3.7% / +1.3% | -4.4% | 2.1M |
| NKE | 35.23 (10:05 iex) | -3.0% | 36.31 | 35.75 / 35.11-36.00 | 1.62 (4.5%) | 34.96-41.10 | -5.0% / -1.4% | -5.2% | 24.0M |
| HSY | 170.78 (10:03 iex) | -2.9% | 175.94 | 173.01 / 170.78-174.39 | 5.59 (3.2%) | 158.55-178.42 | +3.2% / +5.3% | +0.6% | 2.0M |
| STZ | 139.48 (10:03 iex) | -2.9% | 143.62 | 141.53 / 139.48-141.55 | 4.45 (3.1%) | 128.06-149.43 | +2.5% / +12.0% | -0.3% | 2.3M |
