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

# Pre-market brief: Friday 2026-11-20, 09:05 ET (15:05 Stockholm; ET+6 today)

I'm opening nothing new today, and both open brackets stay as submitted. GLD is already trading below its 330 target before the open.

### 1. Tape

**Thursday reversed hard.**
- At 10:05 ET the S&P was +1% and QQQ +2.1%. By the close the S&P was −2.02% at 7,175.83, the Nasdaq −2.25% and the Dow −2.19% (−1,101 points). All eleven sectors fell (Benzinga/TradingView; Fool).
- QQQ closed at 645.04, below Wednesday's 659.51. That is the "AI relief has failed" condition last night's review set.
- NVDA closed at 145.98 (−3.3%), a 52-week low. Thursday's range was 158.13 to 145.71, on 323M shares against a 200M average (HeyGoTrade).
- After the close, CNBC reported (17:49 ET) that California's Attorney General has subpoenaed NVDA over chips reaching China and investor disclosures. The WSJ reports an SEC civil probe. This comes on top of Huang's Nov 12 resignation.
- AMD fell 7.7% after a Hunterbrook short report, which AMD denies.
- ANT closed its debut at 97.17. That is +17% on the $83 pricing but far below its 111.50 open, and it is down 6–10% pre-market.

**This morning:**
- Nasdaq-100 futures are about −1.5%, S&P about −0.65% and the Dow about −0.1%.
- Chips, memory and optical names are leading lower: SMH −2.8%, TSM −5.5%, AMD −4.8%, ARM −5.4%, MRVL −4.7%, SNDK −6.2%, WDC −4.9%.
- AVGO is −1.6% on a Korean industry report (Chosun Biz, relayed by TrendForce and Counterpoint) that Google will buy HBM directly for its MediaTek-built TPU 8t, bypassing Broadcom.
- Gold is −2.4% (GLD 327.09; spot under $3,600).
- Havens are bid: TLT +0.7%, XLP +1.2%, XLU +0.6%. The 10-year is 5.00%, against about 5.10% yesterday morning.
- Hawkish backdrop: December-hike odds are 98.7% (CME FedWatch via Benzinga) and DXY is about 103.85.
- Geopolitics: the US naval blockade of Hormuz is still in place, and a vessel off Oman was hit by an "unknown projectile" Thursday (UKMTO). Even so, WTI is about −1% near $82.

**Regime and edge:**
- This is a risk-off trend in AI and growth under a Fed that is still hiking. The short side has the trend edge.
- But the edge is in the trend, not in today's price. SPY is −5.4% in 5 days and sits under its 20-day low (715.65). QQQ is −6.3% in 5 days. Every short candidate is already 2 ATR or more into its catalyst. And next week is Thanksgiving week, which tends to drift higher on thin volume (a general prior, not verified this session).

### 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| Thu after close | — | INTU, ROST, GAP, KEYS, ESTC, BSP earnings | **INTU**: FQ1 EPS $2.91 beat, but Credit Karma growth guide cut to 3–7% (from 11–13%) and FY revenue cut to $23.08–23.37B. Mailchimp sold to Bending Spoons for $3.68B. Pre-market −9.8%. **ROST**: Q3 EPS $1.91 beat and FY guide raised, but Q4 EPS guide of $2.16–2.25 is under the ~$2.28 estimate; −3% to −6%. | Passes |
| 08:25 | 14:25 | Fed Gov. Waller, welcoming remarks at the College Fed Challenge | Already happened, but **I could not find coverage of what he said.** His Nov 18 line ("shock people"; 50bp or a January signal) is the latest I can verify. | All |
| 10:00 | 16:00 | UMich sentiment, final November | Prelim 51.0, with 1-year inflation expectations at 4.3% (October 4.7%). Final consensus not found. | Review |
| 12:15 | 18:15 | Fed Gov. Cook | Still ahead | All |
| TBA | — | Waller again (Fed Challenge finals) | Still ahead | All |
| Next week | — | Thanksgiving: closed Thu Nov 26, early close Fri Nov 27 | — | Horizon |

No macro release today is a binary event for anything held. HD and GLD have no company events of their own inside ten sessions.

### 3. Open positions and resting entries

**GLD short** (session 3 of 10; entry 345.91, stop 355.50, target 330.00; pre-market 327.09): **hold.**
- **Invalidation not met.** It needs DXY below 102.50 *and* December-hike odds below 70%. DXY is about 103.85 and the odds are 98.7%.
- GLD is an ETF and has no binary event.
- Pre-market is already below the 330 target. The resting buy-to-cover limit should fill at or near the opening print, for roughly +1.6R on the entry-to-stop risk. No action is needed.

**HD short** (session 4 of 10; entry 343.57, stop 353.50, target 323.50; pre-market 339.05): **hold.**
- **Invalidation not met.** It needs a close above 347.51; Thursday closed at 336.68.
- HD reported Nov 17 and has nothing of its own scheduled.

**Resting entries:** none.

### 4. New plays

**None.** Each candidate was checked against its catalyst, its extension and the EV on my own numbers. Every one comes out at about 0R or below (section 6). The specific reason is not "the tape is uncertain":
- The short catalysts are verified, but the moves have already happened. INTU is gapping 2.2 ATR. NVDA is −22% in nine sessions and −38% over seven weeks (CNBC). AMD is −16% in 5 days. QQQ is −6.3% in 5 days at its 20-day low.
- The one laggard with a fresh catalyst, AVGO, rests on a single unconfirmed Korean industry report, with no Google or Broadcom comment.
- The long candidates are a haven bid with no dated catalyst.
- Resting entries are cleared before the weekend, so a bounce-sell limit placed today lives for one session only.

### 5. Both sides

**Best short: AVGO.** Sell limit 352.00 on a retest of Thursday's broken 345 low and Wednesday's 354.05 close; stop 373.50; target 310.00. That is 1.95R, P 0.34, EV about 0.
- **Verified:** Thursday was an outside reversal. It opened at 362.94, made a high of 369.26 against the 369.82 Nov 12 high (a double top), and closed at 346.65 near its 345.00 low on 26.1M shares (StockAnalysis). Pre-market is 341.04. AVGO is still +4% above its 20-day average while SMH is −10.7% below its own, so the catch-down room is real.
- **Next earnings:** Dec 9 after the close (company release). That is more than 7 days away and about session 12, outside the horizon.
- **Why P 0.34, not the 39% base:**
  - The fill needs a 3% intraday bounce on a −1.5% Nasdaq morning.
  - The target sits beyond the 327.80 Nov 16 low.
  - The catalyst is single-sourced with no company comment.
- **Conviction 2. Passed.**

**Best long: XLP.** Limit 90.40, stop 88.40, target 93.40 (the 20-day high is 93.48). That is 1.5R, P 0.38, EV −0.05.
- Haven rotation, with the 10-year down about 10bp and staples bid pre-market (CL +1.8%, GIS +1.8%, KDP +1.9%, WMT +1.5%).
- Thursday morning's staples selloff was the mirror of the AI rally that reversed. That is rotation, not a dated catalyst, so I pass it. Conviction 2.

**Others on the short side:** NVDA (the strongest verified catalyst), INTU, QQQ and ROST. All are in section 6. AMD's Hunterbrook report I could not find at its source.

### 6. Passing on

- **AVGO short:** levels above. A thin single-source catalyst with EV about 0.
- **NVDA short** (limit 150.50 near Thursday's open and the prior 150.96 close / stop 163.00 above the 158.13 Thursday high / target 126.00; 1.96R, P 0.33, EV −0.02):
  - The catalyst is verified at CNBC (CA AG subpoena, Nov 19 17:49 ET), plus the WSJ SEC probe.
  - But the stock is −38% in seven weeks and reacted only −2.3% pre-market, which suggests the bad news is crowded in.
  - Next earnings are late February 2027 (inferred, not verified this session).
- **INTU short** (market about 279.65 / stop 297.00 / target 252.00; 1.59R, P 0.36, EV −0.07):
  - The guidance cut is verified from the call coverage.
  - But the gap is already 2.2 ATR, the stock is about −50% year on year, and EPS guidance ($22.88–23.12) was held, which puts it near 12x.
  - Next earnings are late February 2027 (inferred).
- **QQQ short** (market about 636.34 / stop 662.00 above Wednesday's 659.51 close / target 600.00; 1.42R, P 0.37, EV −0.11): −6.3% in 5 days, with no index catalyst beyond momentum, into Thanksgiving week.
- **ROST short** (market about 206.00 / stop 216.00 / target 192.00; 1.4R, P 0.35, EV −0.16): this was a beat-and-raise on the year with a slightly soft Q4. The gap is a valuation reset, not a thesis.
- **XLP long:** levels above.
- **TTWO long:** GTA VI launched Nov 19, and the shares are +1.7% pre-market with no sales figure released. The disclosure itself is an unscheduled company event I can't verify. No levels.

### 7. For the post-open review

- **GLD:** confirm the 330 target filled near the open. If GLD somehow opened above 330 and the position is still open, the bracket stands. No other action.
- **HD:** hold. The only test is a daily close above 347.51.
- **UMich at 10:00 ET:** record the final headline and the 1-year inflation expectation (prelim 4.3%). A revision to 4.6% or higher is a hawkish data point for Cook at 12:15. It changes no order on its own.
- **AVGO:** only act if Google or Broadcom confirm the HBM change at source before 10:05. Then short at market, stop 373.50, target 305.00, at conviction 3 and the 0.5 tier, provided the 10:04 price is at or below 345 (otherwise R:R is below 1.1). Without confirmation, do nothing.
- **QQQ:** if the first 30 minutes run back to 655–660 and the 10:04 price is still at or above 652 with a fresh negative AI headline, a short with stop 676 and target 615 is about 1.7R. That stop sits above about 673, Thursday's level inferred from +2.1% at 10:05 on 659.51; the session high is not verified. That would be 0.5 tier. Otherwise nothing. Do not chase below 630.

### 8. Book state

- **Now:** gross 36% and net −36% of equity (caps 150% / ±100%); risk at stake 1.04% (cap 4%); 2 of 8 slots.
- **After GLD's target fills:** gross about 17% and net about −17%; risk at stake about 0.49% (HD only); 1 of 8 slots.

```json
{
  "date": "2026-11-20",
  "no_trade": true,
  "session_note": "Risk-off AI/semis trend under a hiking Fed (Thu S&P -2.02% outside reversal, NQ futures -1.5%, 10y 5.00%, Dec hike 98.7%), but every short candidate is already 2+ ATR into its catalyst (INTU -2.2 ATR gap, NVDA -38% in 7 weeks, QQQ -6.3% in 5d at its 20d low) and the laggard AVGO rests on a single unconfirmed Korean report; longs are a haven bid with no catalyst. All candidate EVs <= 0. Would act on source confirmation of Google bypassing Broadcom on HBM (AVGO short <=345, stop 373.50) or a failed QQQ retest of 655-660 with a fresh headline. GLD short should hit its 330 target at the open; HD held.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "AVGO",
      "direction": "short",
      "entry_type": "limit",
      "entry": 352.00,
      "stop": 373.50,
      "targets": [310.00],
      "p_target_first": 0.34,
      "reason": "Best short. Thu outside reversal from 369.26 (double top vs 369.82 Nov 12) to close 346.65 near the 345.00 low; pre-market 341.04 on a Chosun Biz/TrendForce report that Google will buy HBM directly for TPU 8t. Single-sourced, no company comment; target sits beyond the 327.80 Nov 16 low; earnings Dec 9 (confirmed). 1.95R, EV about 0. Conviction 2."
    },
    {
      "ticker": "NVDA",
      "direction": "short",
      "entry_type": "limit",
      "entry": 150.50,
      "stop": 163.00,
      "targets": [126.00],
      "p_target_first": 0.33,
      "reason": "CA AG subpoena (CNBC, Nov 19 17:49 ET) and WSJ-reported SEC civil probe verified, after Huang's Nov 12 resignation; but -38% in seven weeks, 52w low 145.71 already broken pre-market (142.68), and only -2.3% reaction suggests crowded. Bounce-sell near Thu open/prior close, stop above Thu 158.13 high. 1.96R, EV -0.02."
    },
    {
      "ticker": "INTU",
      "direction": "short",
      "entry_type": "market",
      "entry": 279.65,
      "stop": 297.00,
      "targets": [252.00],
      "p_target_first": 0.36,
      "reason": "FQ1 beat but Credit Karma growth guide cut to 3-7% from 11-13% (AI discovery shift, rates) and FY revenue to $23.08-23.37B; Mailchimp sold for $3.68B. Gap already -9.8% (2.2 ATR), stock about -50% YoY, EPS guide held (about 12x). 1.59R, EV -0.07."
    },
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "market",
      "entry": 636.34,
      "stop": 662.00,
      "targets": [600.00],
      "p_target_first": 0.37,
      "reason": "Thu close 645.04 below Wed 659.51 met the 'AI relief failed' condition, but QQQ is -6.3% in 5d and under its 644.34 20d low into Thanksgiving week; no index-level catalyst beyond momentum. 1.42R, EV -0.11."
    },
    {
      "ticker": "ROST",
      "direction": "short",
      "entry_type": "market",
      "entry": 206.00,
      "stop": 216.00,
      "targets": [192.00],
      "p_target_first": 0.35,
      "reason": "Q3 EPS $1.91 beat and FY raised; only Q4 EPS guide $2.16-2.25 below ~$2.28. Gap is a valuation reset, not a broken thesis. 1.4R, EV -0.16."
    },
    {
      "ticker": "XLP",
      "direction": "long",
      "entry_type": "limit",
      "entry": 90.40,
      "stop": 88.40,
      "targets": [93.40],
      "p_target_first": 0.38,
      "reason": "Best long. Haven rotation (XLP +1.2%, 10y about 5.00% from about 5.10%, CL/GIS/KDP up) reversing Thursday morning's staples selloff, but no dated catalyst; target at the 93.48 20d high. 1.5R, EV -0.05. Conviction 2."
    }
  ]
}
```

Sources:
- [Benzinga/TradingView: futures, Thursday's close, yields, FedWatch, today's calendar](https://www.tradingview.com/news/benzinga:1c06a4673094b:0-stock-market-today-dow-jones-s-p-500-futures-fall-as-trump-weighs-iran-decision-intu-rost-keys-in-focus/)
- [CNBC: stocks moving Friday](https://www.cnbc.com/2026/11/20/stocks-moving-the-most-today-live-updates.html)
- [Investing.com: pre-market movers](https://www.investing.com/news/stock-market-news/premarket-movers-anthropic-slides-after-debut-intuit-tumbles-on-mailchimp-sale-5041130)
- [TradingKey: US pre-market, AVGO/HBM, chips, gold](https://www.tradingkey.com/analysis/stocks/us-stocks/262315308-us-pre-market-anthropic-tradingkey)
- [Fool: Nov 19 market, Nvidia](https://www.fool.com/coverage/stock-market-today/2026/11/19/stock-market-today-nov-19-nvidia-slides-as-investors-weigh-ceo-transition-fallout-despite-strong-q3-results/)
- [HeyGoTrade: NVDA Nov 19 close](https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-november-20-2026/)
- [CNBC: California AG subpoenas Nvidia](https://www.cnbc.com/2026/11/19/nvidia-california-bonta-subpoena-china-chips.html)
- [Yahoo: CA AG subpoena and SEC probe](https://finance.yahoo.com/markets/stocks/articles/california-attorney-general-subpoenas-nvidia-235558917.html)
- [Intuit Q1 FY27 call coverage (Yahoo)](https://finance.yahoo.com/markets/stocks/articles/intuit-intu-said-q1-earnings-001407071.html)
- [Intuit Q1: Credit Karma and Mailchimp (TradingView/SA)](https://www.tradingview.com/news/seekingalpha:91a0413ae094b:0-intuit-meets-fq1-earnings-estimates-credit-karma-hits-guidance-mailchimp-sale-disclosed/)
- [Ross Stores Q3 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0000745732/000074573226000047/q326exhibit991.htm)
- [Broadcom Q4 date announcement](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announce-fourth-quarter-and-fiscal-year-2026)
- [Google HBM bypassing Broadcom (mlq.ai; page fetch blocked, search summary only)](https://mlq.ai/news/google-moves-to-buy-hbm-directly-for-its-mediatek-built-ai-chips-bypassing-broadcom-industry-reports-say/)
- [StockAnalysis: AVGO price history](https://stockanalysis.com/stocks/avgo/history/)
- [GuruFocus: AVGO +4.21% on Nov 19 on the Anthropic placement](https://gurufocus.com/news/9210257/broadcom-stocks-rise-421-as-chip-supplier-joins-anthropics-26-billion-placement)
- [Waller: "shock people" (The Hill)](https://thehill.com/business/6228471-waller-fed-rate-hike-plan/)
- [TipRanks: Waller/Cook schedule](https://www.tipranks.com/news/investors-pile-into-u-s-bonds-as-fed-governors-eye-rate-hikes-ahead-of-oil-rig-data)
- [StockAnalysis: UMich preliminary November 51.0](https://stockanalysis.com/news/consumer-sentiment-rises-november-2026/)
- [Finviz: TTWO, GTA VI Nov 19 release confirmed](https://finviz.com/news/419805/take-two-shares-rise-over-3-after-quarterly-results-as-gta-vi-november-19-release-confirmed)
- [RTTNews (Nov 12, background)](https://www.rttnews.com/3713931/wall-street-poised-to-open-broadly-lower.aspx?type=uscom)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Friday 2026-11-20. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$103,395.38**
- Cash: $121,012.05
- Session P&L so far: +0.01% (new entries are blocked at -3.0%)
- Gross exposure: $17,617 (17% of equity, cap 150%)
- Net exposure: $-17,617 (-17%, cap +/-100%)
- Risk at stake (entry to stop): $506 (0.49% of equity, cap 4.0%) — 3.51% left for new plays
- Slots: 1 open + 0 resting entries of 8 — you may add at most 7 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| HD | short | 51 | 343.57 | 345.43 | -95 (-0.5%) | -17% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **HD**, opened 2026-11-17 (session 4 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Your record

52 closed trades: 17W / 35L, total +2.52R, net $+3,507 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 52 | 19 | 30 | +0.05R |
| The same trades, bracket left alone | 52 | | | +0.07R |
| Ideas you passed on, or the caps dropped | 115 | 40 | 65 | +0.02R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 44 | 48% |
| 35%-40% | 77 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 5 | 20% |
| 50%-60% | 1 | 100% |

Base rate: 38% of 154 brackets reached target first. Your Brier score is 0.239; saying 38% every time scores 0.236. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| HD | 345.42 (10:04 iex) | +2.6% | 336.68 | 341.70 / 339.26-346.98 | 10.52 (3.1%) | 316.15-362.44 | -0.5% / +7.1% | -3.3% | 4.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 716.25 (10:05 iex) | +0.1% | 715.87 | 713.61 / 711.72-718.26 | 14.70 (2.1%) | 715.65-775.64 | -4.7% / -6.0% | -5.4% | 52.5M |
| QQQ | 640.22 (10:05 iex) | -0.7% | 645.04 | 638.82 / 633.86-643.21 | 19.73 (3.1%) | 644.34-726.14 | -5.6% / -9.5% | -6.3% | 52.2M |
| IWM | 264.74 (10:05 iex) | +0.2% | 264.22 | 263.32 / 262.62-265.85 | 5.91 (2.2%) | 263.74-286.17 | -4.7% / -5.3% | -5.1% | 24.5M |
| DIA | 494.93 (10:05 iex) | +1.0% | 490.24 | 490.39 / 489.67-495.25 | 9.23 (1.9%) | 490.18-536.00 | -5.2% / -5.1% | -6.1% | 3.9M |
| TLT | 80.81 (10:04 iex) | +0.6% | 80.35 | 80.74 / 80.69-80.97 | 0.73 (0.9%) | 79.11-82.42 | -0.7% / +0.8% | +0.8% | 35.1M |
| GLD | 327.08 (10:05 iex) | -2.4% | 335.18 | 326.96 / 326.52-328.53 | 7.37 (2.2%) | 335.05-380.18 | -7.6% / -11.0% | -5.6% | 9.7M |
| USO | 136.10 (10:04 iex) | -1.4% | 138.09 | 136.61 / 135.34-136.66 | 5.73 (4.1%) | 135.01-171.82 | -8.9% / -9.1% | -5.5% | 5.0M |
| SMH | 433.32 (10:05 iex) | -3.2% | 447.48 | 438.10 / 427.56-438.44 | 27.46 (6.1%) | 445.32-571.00 | -10.7% / -18.8% | -10.8% | 11.8M |
| XLK | 158.03 (10:05 iex) | -1.7% | 160.69 | 158.71 / 156.23-158.96 | 6.52 (4.1%) | 159.63-191.55 | -7.7% / -13.2% | -7.5% | 13.8M |
| XLF | 55.91 (10:05 iex) | +0.6% | 55.58 | 55.68 / 55.53-56.02 | 1.09 (2.0%) | 55.30-60.04 | -2.9% / -0.6% | -4.5% | 36.9M |
| XLE | 61.32 (10:05 iex) | +0.7% | 60.89 | 60.71 / 60.48-61.38 | 1.79 (2.9%) | 60.43-70.15 | -6.4% / -6.0% | -5.3% | 36.6M |
| XLV | 180.04 (10:05 iex) | +1.5% | 177.46 | 179.00 / 178.84-180.06 | 3.76 (2.1%) | 176.96-192.32 | -3.8% / +0.7% | -5.5% | 12.5M |
| XLI | 161.97 (10:04 iex) | +0.4% | 161.36 | 160.91 / 160.50-162.35 | 3.67 (2.3%) | 160.83-172.40 | -3.5% / -4.1% | -4.8% | 8.9M |
| XLY | 116.94 (10:04 iex) | +0.9% | 115.88 | 115.62 / 115.09-116.97 | 2.95 (2.5%) | 112.83-122.92 | -1.7% / +1.5% | -3.8% | 9.4M |
| XLP | 91.59 (10:05 iex) | +1.9% | 89.86 | 90.93 / 90.78-91.58 | 1.65 (1.8%) | 86.36-93.48 | -0.3% / +4.3% | -1.3% | 20.3M |
| XLU | 43.31 (10:05 iex) | +0.7% | 43.01 | 43.27 / 43.12-43.34 | 0.62 (1.4%) | 42.39-44.40 | -0.8% / +2.7% | -1.8% | 24.1M |
| XLB | 49.87 (10:05 iex) | +0.9% | 49.42 | 49.42 / 49.30-49.91 | 1.13 (2.3%) | 49.32-54.63 | -5.1% / -2.7% | -5.6% | 12.5M |
| XLRE | 43.28 (10:05 iex) | +0.9% | 42.88 | 43.17 / 43.05-43.30 | 0.69 (1.6%) | 41.78-45.34 | -1.9% / +0.8% | -3.3% | 7.8M |
| XLC | 103.44 (10:05 iex) | +0.7% | 102.76 | 102.70 / 102.30-103.90 | 2.39 (2.3%) | 99.33-109.26 | -1.8% / -5.6% | -4.5% | 8.1M |
| KRE | 70.00 (10:05 iex) | +1.1% | 69.26 | 69.31 / 69.25-70.15 | 1.59 (2.3%) | 68.66-75.80 | -4.3% / -3.0% | -4.5% | 14.8M |
| XHB | 99.64 (10:04 iex) | +1.8% | 97.89 | 98.08 / 98.07-99.79 | 3.31 (3.4%) | 97.19-108.78 | -3.6% / -0.5% | -3.4% | 2.3M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 349.44 (10:05 iex) | +0.1% | 349.21 | 352.87 / 348.64-354.34 | 9.01 (2.6%) | 325.08-360.83 | +0.5% / +2.3% | -1.6% | 47.9M |
| MSFT | 502.73 (10:05 iex) | +0.9% | 498.30 | 493.69 / 490.87-503.74 | 18.77 (3.8%) | 495.55-558.07 | -4.9% / -4.0% | -4.5% | 28.6M |
| NVDA | 141.75 (10:05 iex) | -2.9% | 145.98 | 143.52 / 138.84-143.72 | 11.90 (8.2%) | 145.71-219.99 | -21.4% / -30.1% | -12.2% | 260.8M |
| AMZN | 258.57 (10:05 iex) | +0.5% | 257.37 | 253.37 / 251.12-259.94 | 11.20 (4.4%) | 229.36-275.34 | -0.0% / +0.8% | -3.8% | 50.6M |
| GOOGL | 280.81 (10:05 iex) | +3.0% | 272.66 | 274.32 / 272.83-283.02 | 10.66 (3.9%) | 272.36-326.40 | -6.7% / -15.8% | -8.7% | 43.5M |
| META | 586.65 (10:05 iex) | -1.6% | 596.22 | 582.72 / 573.48-588.58 | 22.04 (3.7%) | 583.80-648.45 | -4.2% / -12.1% | -4.4% | 21.2M |
| TSLA | 372.23 (10:05 iex) | -0.6% | 374.41 | 370.02 / 365.14-373.71 | 18.40 (4.9%) | 338.15-414.23 | -3.0% / -0.4% | -5.8% | 36.4M |
| AVGO | 330.00 (10:05 iex) | -4.8% | 346.65 | 343.01 / 330.00-343.01 | 20.87 (6.0%) | 289.77-369.82 | +4.0% / +0.8% | -4.9% | 28.2M |
| AMD | 467.18 (10:05 iex) | -4.5% | 489.19 | 471.23 / 453.73-474.68 | 50.89 (10.4%) | 402.10-594.00 | -4.8% / -11.8% | -16.4% | 39.6M |
| ORCL | 108.45 (10:04 iex) | -1.9% | 110.57 | 108.47 / 106.30-108.92 | 8.20 (7.4%) | 109.21-148.48 | -10.7% / -16.8% | -13.0% | 40.7M |
| NFLX | 58.95 (10:05 iex) | +0.8% | 58.46 | 58.26 / 58.26-59.35 | 1.91 (3.3%) | 58.18-67.82 | -6.8% / -13.8% | -6.7% | 39.6M |
| CRM | 188.61 (10:05 iex) | +2.9% | 183.31 | 183.31 / 183.26-188.69 | 8.91 (4.9%) | 182.51-250.99 | -17.0% / -20.6% | -15.7% | 7.2M |
| JPM | 319.99 (10:05 iex) | -0.1% | 320.22 | 320.76 / 317.95-320.88 | 8.55 (2.7%) | 317.43-359.80 | -5.2% / -5.2% | -6.6% | 6.6M |
| GS | 822.76 (10:05 iex) | -2.9% | 847.53 | 826.49 / 812.19-827.89 | 30.36 (3.6%) | 843.88-939.38 | -5.6% / -6.8% | -7.2% | 2.1M |
| BAC | 48.48 (10:05 iex) | -0.2% | 48.57 | 48.45 / 48.14-48.77 | 1.21 (2.5%) | 48.05-53.02 | -3.3% / -8.4% | -3.8% | 34.3M |
| XOM | 160.36 (10:04 iex) | +0.9% | 158.93 | 158.83 / 158.60-160.69 | 4.74 (3.0%) | 158.60-187.32 | -7.3% / -5.7% | -5.8% | 14.7M |
| CVX | 208.79 (10:05 iex) | +1.1% | 206.50 | 206.44 / 205.94-208.82 | 5.40 (2.6%) | 204.31-234.53 | -5.5% / -3.4% | -3.8% | 8.4M |
| LLY | 1,364.62 (10:05 iex) | +1.0% | 1,351.12 | 1,362.38 / 1,354.23-1,366.51 | 43.97 (3.3%) | 1,256.10-1,475.25 | -2.0% / +7.2% | -5.2% | 3.1M |
| UNH | 345.39 (10:05 iex) | +4.5% | 330.48 | 341.01 / 338.24-346.49 | 15.94 (4.8%) | 324.67-425.25 | -17.1% / -15.1% | -18.4% | 6.4M |
| JNJ | 271.37 (10:05 iex) | +1.6% | 267.14 | 270.36 / 269.47-272.15 | 7.01 (2.6%) | 262.40-290.25 | -2.7% / -0.1% | -5.8% | 7.6M |
| WMT | 129.69 (10:05 iex) | +2.9% | 126.04 | 127.40 / 127.18-129.80 | 3.14 (2.5%) | 118.11-131.82 | +0.9% / +8.4% | -0.1% | 22.5M |
| COST | 1,110.41 (10:04 iex) | +1.5% | 1,093.83 | 1,103.10 / 1,099.30-1,110.41 | 20.97 (1.9%) | 978.87-1,123.67 | +4.0% / +11.4% | +0.1% | 2.5M |
| HD | 345.42 (10:04 iex) | +2.6% | 336.68 | 341.70 / 339.26-346.98 | 10.52 (3.1%) | 316.15-362.44 | -0.5% / +7.1% | -3.3% | 4.8M |
| CAT | 534.23 (10:03 iex) | -0.6% | 537.37 | 528.42 / 524.50-538.98 | 27.99 (5.2%) | 535.53-732.73 | -12.2% / -25.3% | -11.2% | 4.0M |
| BA | 164.09 (10:04 iex) | +2.2% | 160.51 | 161.00 / 160.15-164.32 | 4.87 (3.0%) | 158.92-189.66 | -6.8% / -13.3% | -6.4% | 10.6M |
| DAL | 84.42 (10:01 iex) | +1.5% | 83.17 | 83.60 / 83.51-84.80 | 3.18 (3.8%) | 75.33-92.52 | -1.9% / +1.1% | -3.9% | 6.0M |
| UAL | 107.48 (10:04 iex) | +1.8% | 105.53 | 105.46 / 105.30-107.78 | 5.45 (5.2%) | 96.39-122.08 | -3.3% / -2.3% | -5.1% | 5.2M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| HUBS | 206.45 (10:05 iex) | +7.5% | 191.99 | 191.98 / 190.95-207.12 | 15.17 (7.9%) | 188.25-271.60 | -14.2% / -14.8% | -11.0% | 1.6M |
| TEAM | 140.93 (10:04 iex) | +6.0% | 133.01 | 131.08 / 131.04-141.13 | 10.24 (7.7%) | 132.49-228.13 | -24.2% / -29.6% | -12.7% | 3.7M |
| CPNG | 14.72 (10:05 iex) | +4.7% | 14.06 | 13.91 / 13.80-14.76 | 0.80 (5.7%) | 13.44-17.45 | -6.3% / -4.2% | -8.0% | 14.8M |
| MRNA | 208.05 (10:05 iex) | +4.4% | 199.33 | 199.23 / 196.50-209.37 | 18.49 (9.3%) | 179.53-280.80 | -11.6% / -3.6% | -13.8% | 11.3M |
| GIS | 35.94 (10:05 iex) | +4.2% | 34.48 | 35.01 / 34.93-35.98 | 1.16 (3.4%) | 32.82-37.02 | +0.0% / +2.1% | +2.9% | 8.1M |
| WDAY | 180.63 (10:05 iex) | +4.2% | 173.36 | 172.93 / 172.93-179.24 | 7.47 (4.3%) | 172.63-212.91 | -11.0% / -10.1% | -9.1% | 2.1M |
| ACN | 227.75 (10:05 iex) | +4.2% | 218.58 | 221.88 / 220.89-228.13 | 9.72 (4.4%) | 216.13-271.76 | -12.3% / -0.9% | -12.6% | 5.3M |
| NOW | 92.50 (10:05 iex) | +4.1% | 88.87 | 87.33 / 87.33-92.57 | 4.62 (5.2%) | 88.13-159.50 | -20.8% / -31.0% | -11.7% | 21.2M |
| SNDK | 86.71 (10:05 iex) | -8.1% | 94.40 | 89.98 / 85.63-90.67 | 12.90 (13.7%) | 93.67-176.06 | -25.4% / -44.7% | -19.4% | 105.4M |
| ANET | 176.60 (10:05 iex) | -6.9% | 189.59 | 185.09 / 174.28-185.82 | 13.53 (7.1%) | 158.34-212.16 | +4.0% / -1.6% | -8.2% | 8.7M |
| MU | 648.87 (10:05 iex) | -6.0% | 690.44 | 664.62 / 625.24-669.00 | 65.31 (9.5%) | 650.00-990.00 | -13.8% / -24.9% | -13.5% | 32.0M |
| NET | 285.61 (10:05 iex) | -6.0% | 303.68 | 300.00 / 281.00-300.88 | 22.63 (7.5%) | 233.62-337.00 | +2.3% / -5.1% | -4.7% | 4.4M |
| STX | 491.09 (10:05 iex) | -5.8% | 521.39 | 506.05 / 479.50-506.09 | 48.21 (9.2%) | 449.28-718.65 | -8.1% / -26.7% | -4.4% | 6.0M |
| DELL | 296.15 (10:05 iex) | -5.2% | 312.54 | 303.60 / 286.20-303.60 | 34.32 (11.0%) | 305.80-507.38 | -18.6% / -34.4% | -15.8% | 7.5M |
| ARM | 167.88 (10:05 iex) | -5.2% | 177.17 | 169.07 / 164.58-170.68 | 15.65 (8.8%) | 163.13-237.88 | -10.1% / -26.8% | -11.3% | 5.9M |
| WDC | 281.76 (10:05 iex) | -5.1% | 296.78 | 287.01 / 274.63-288.56 | 26.87 (9.1%) | 258.61-402.23 | -7.7% / -21.3% | -4.6% | 8.2M |
