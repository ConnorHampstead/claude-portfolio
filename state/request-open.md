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

I'm placing no new trades this morning and keeping the HD short exactly as submitted. Most of today's big movers are just giving back Monday's rally. The two clean retail beats, BBY and DLTR, landed the same morning as a report that the US is preparing new tariffs on the countries they buy from. None of the short setups breaks even on my own numbers.

# Pre-market brief: Tuesday 2026-11-24, 09:05 ET (15:05 Stockholm, ET+6)

### 1. Tape

**Monday was the best day since April 2025.** The S&P 500 rose 4.73% to 7,237.17 and the Nasdaq Composite 6.51%. The trigger was Nvidia's board reinstating Jensen Huang as CEO (NVDA +31.5% to 165.05).

**This morning about a third of that is going back:**
- At 08:38 ET, S&P futures were −1.2% and Nasdaq-100 futures −2.1% (Reuters via SRN).
- SPY is at 713.70 (−1.2%), QQQ at 637.71 (−2.0%) and SMH at 438.84 (−4.6%).
- QQQ is already below Monday's 641.95 low before the open.

**Three things are driving it:**
- **Nomura called Monday's rally mostly mechanical.** Strategist Charlie McElligott described a "massive surge" of mechanical buying, plus short covering and options dealers unwinding hedges.
- **The Fed is expected to hike.** CME FedWatch has a 25bp hike on Dec 9 fully priced, and a small chance of 50bp has appeared. NY Fed's Williams said persistent inflation points to tighter policy.
- **A WSJ report around 08:30 ET says the US is preparing new tariffs.** They would cover China, the EU and 14 other economies, with China, Vietnam and India facing the highest rates. USTR could publish findings "as early as this week." Nasdaq futures went from −0.8% at 04:43 ET to −2.3% at 08:39 ET around the time of the report.

**Regime:** a bear market with violent short-covering rallies. VIX is in the high 20s (sources conflict; not verified for today). The 10-year is about 4.94%. Oil and energy are sitting at their 20-day lows.

**Edge today: short.** But there is a full ATR of noise in every index at a VIX in the high 20s, and Thanksgiving week usually leans bullish. So the edge is not big enough to pay for an index short with a stop inside one ATR.

### 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 04:17 | 10:17 | NY Fed Williams headline: inflation back to 2% only in 2028 | Hawkish tone; hike fully priced | All |
| ~07:00 | ~13:00 | ADI fiscal Q4 results | **Beat:** revenue $4.37B vs $4.33B, adjusted EPS $4.06 vs ~$3.88. **Q1 guide:** $4.4B (±$150M), EPS $3.82 vs $3.81–3.89 consensus (sources differ). Inventory days rose to 141 from 134. Stock −10.5% to 339.03 | ADI (pass) |
| pre-open | pre-open | BBY fiscal Q3 results | **Beat:** adjusted EPS $1.62 vs $1.49; revenue $10.24B vs $9.90B; comps +6.1% vs 2.3%. Full-year guide raised. Stock +3.1% to 100.00 (CNBC had it about +6% earlier) | BBY (best long, pass) |
| pre-open | pre-open | DKS Q3 results | **Beat:** adjusted EPS $1.94 vs $1.41; revenue $5.13B vs $5.07B. Full-year guide raised to $11.45–12.30. Stock about +13% to ~151 | DKS (pass) |
| pre-open | pre-open | DLTR Q3 results | **Beat:** adjusted EPS $1.16 vs $0.91; comps 4.6% vs 3.7%. Full-year guide raised to $8.05–8.25, including about $0.65 from tariff refunds. One source says the Q4 guide was below estimates. Stock +7.1% | DLTR (pass) |
| pre-open | pre-open | MDT fiscal Q2 results | Couldn't find the figures | none |
| Mon after close | — | HPE fiscal Q4 results | **Beat:** revenue $14.5B, adjusted EPS $1.43. FY27 guide raised, but gross margin is guided lower. Stock −12.7% after +17% Monday | HPE (pass) |
| ~08:30 | ~14:30 | WSJ tariff report | Not confirmed by USTR | BBY, DLTR, HD, broad market |
| 10:00 | 16:00 | Conference Board consumer confidence | Consensus 92.4, prior 91.7 | BBY review condition |
| 10:00 | 16:00 | ADI conference call | — | ADI |
| after close | after 22:00 | DELL and WDAY earnings | Rule 8 excludes both | none |
| Wed 08:30 | Wed 14:30 | October PCE and Q3 GDP (2nd estimate) | Couldn't find consensus | All |
| Thu | Thu | US markets closed (Thanksgiving) | — | Harness clears resting entries before it |
| Fri 13:00 | Fri 19:00 | Early close | — | — |

I couldn't verify a Treasury auction or a Richmond Fed survey for today.

### 3. Open positions and resting entries

**HD short (avg 343.57 / stop 353.50 / target 323.50): hold, session 6 of 10.**
- **Invalidation (a close above 347.51): not met.** Monday closed at 346.06, and pre-market is 346.31 at 08:35.
- HD is flat on a −1.2% tape. That is relative strength, but it is not the recorded test.
- None of the three close conditions applies:
  - There is no HD binary event before session 10.
  - The $2.33 dividend record date is Dec 3, after session 10 (Dec 1).
  - It is not in its tenth session.
- The bracket stays as submitted.

**Resting entries:** none.

### 4. New plays

None. Each candidate failed for a reason specific to today:
- **ADI and HPE.** Their earnings moves mostly reverse Monday's rally. Against Friday's close ADI is about −1.5% and HPE about +2.5%. That is little net information, and both have already moved 1.5–1.6 ATR.
- **BBY and DLTR.** These are the clean beats. But they collide with a same-morning tariff report aimed at the countries they source from. In 2025 Best Buy said about 55% of what it sells came through China, falling to about 35% of product cost later that year. USTR findings could land inside the holding window.
- **QQQ and NVDA.** At a VIX in the high 20s, the shorts need a stop inside one ATR or offer about 1.6R or less. Neither clears zero expected value at a near-base-rate probability.

### 5. Both sides

**Best long: BBY, not taken.**
- **Levels:** market about 100.00, stop 94.40, target 110.00. That is 1.79R at P 0.37, for an expected value of about +0.03.
- **Why the stop is there:** 94.40 is below the 50-day average (about 94.7) and 1.3 ATR under entry. Losing that level after a five-year-best comp quarter means the market is pricing tariffs over earnings.
- **Why P sits there:** I started from the 39% base rate. The surprise and an under-reaction gap (+3% on a 6.1% vs 2.3% comp) add a little. The tariff headwind, live this week, takes off a little more. The target sits above the 106.83 20-day high, which is resistance.
- **Why it's a pass:** the expected value is positive but within my calibration noise. With an unresolved, name-specific tariff risk, that makes it conviction 2.

**Best short: QQQ, not taken.**
- **Levels:** market about 637.71, stop 657.50 (above Monday's 656.30 opening high), target 606.50 (the 20-day low is 606.23; Friday's close was about 608.4). That is 1.58R at P 0.37, for an expected value of about −0.05.
- **For it:** the gap above Friday is failing, and Monday's rally was mechanical.
- **Against it:** the stop is only 0.82 ATR away, it is Thanksgiving week, and tomorrow's PCE can move it either way.

### 6. Passing on

- **ADI short** (339.03 / 363.50 / 300.00, P 0.35, 1.6R, EV −0.09). The guide was roughly in line and inventory days rose, but most of the drop reverses Monday's 10% pre-report run-up. It has moved 1.6 ATR and the call is at 10:00 ET.
- **DKS long** (151.00 / 141.00 / 168.00, P 0.36, 1.7R, EV −0.03). The beat was large, but it is a roughly 13% gap. The market data table gives no ATR or average volume for it, so I can't confirm the 1M-share floor or the stop distance.
- **DLTR long** (148.96 / 140.50 / 162.00, P 0.36, EV −0.09). It is already 1.6 ATR up, above its 20-day high and about 19% above its 50-day average. Part of the guide raise is tariff refunds, the Q4 guide was reportedly light, and the tariff report hits its sourcing directly.
- **NVDA short** (sell stop 154.90, below Monday's 156.93 low / stop 172.00 above the 171.50 high / target 128.00, P 0.34, EV −0.13). The ATR is 9.5% and a fundamental catalyst (the CEO's return) argues against shorting it. Huang testifies to Senate Banking on Dec 3.
- **NVDA long:** no chase. The 146 gap midpoint is tomorrow's level, if the post-open review hasn't already acted.
- **HPE short** (41.90 / 46.20 / 36.00, P 0.35, 1.37R, EV −0.17). It is back where it started before Monday, it sits on its 40.48 20-day low, and the FY27 guide was raised.
- **FCX (−5.7%), MU, INTC, SNDK, MRVL:** I found no dated stock-specific reason for FCX. The chip names are giving back Monday's +19% moves. No levels.
- **INSM:** cash deal at $175. It is a merger-arbitrage spread, not a swing trade.
- **DELL and WDAY:** both report after today's close, which rule 8 excludes.

### 7. For the post-open review

**BBY**
- **Go long at the 0.5 tier, market, stop 94.40, target 110.00, P 0.40**, only if all three hold at 10:05:
  - BBY is at or above 101.00;
  - it is above its opening print;
  - consumer confidence (10:00 ET / 16:00 Stockholm) printed at 92.4 or better.
- The 0.5 tier is for the tariff headline risk. On those conditions the expected value is about +0.10 at 1.6R or better.
- If BBY is below 99, do nothing.

**QQQ**
- Open no index short in the review. The stop is inside one ATR, and the target sits about one ATR away at the 606 level.
- **For tomorrow:** if today closes below 630 and PCE is hot, reconsider a short in Wednesday's brief, stop above 657.50, target 606.50.
- If QQQ is back above 645 at 10:05, the gap failure is off.

**NVDA**
- Do nothing in the review.
- **For tomorrow:** a print in the 143–147 zone, the gap midpoint where it also closed on Nov 18–19, that holds 140 is tomorrow's long at the 0.5 tier.

**ADI**
- Do nothing; the call runs from 10:00 ET.

**Timing**
- Resting entries are cleared before Thursday's holiday, so anything placed today or Wednesday has to fill within two sessions.

### 8. Book state

Once today's orders fill (there are none): gross 17% (cap 150%), net −17% (cap ±100%), consumer discretionary −17% (cap 40%). Risk at stake is 0.49% (cap 4%), with 1 of 8 slots used.

```json
{
  "date": "2026-11-24",
  "no_trade": true,
  "session_note": "Monday's mechanical +4.7% SPY rally is fading (QQQ 637.71 below Monday's 641.95 low) on a WSJ tariff report and a fully priced Dec hike. Movers (ADI, HPE) mostly reverse Monday; clean retail beats (BBY, DLTR) run into the tariff report; index/NVDA shorts are EV <= 0 at a VIX in the high 20s. Would act: BBY long at 0.5 if it holds >=101 above its open at 10:05 with consumer confidence >=92.4; QQQ short tomorrow on a close <630 plus a hot PCE. HD held: close >347.51 not met (Mon close 346.06), session 6/10.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "BBY",
      "direction": "long",
      "entry_type": "market",
      "entry": 100.00,
      "stop": 94.40,
      "targets": [110.00],
      "p_target_first": 0.37,
      "reason": "Best long. Q3 FY27 beat (comps +6.1% vs 2.3%, EPS 1.62 vs 1.49, FY guide raised, CNBC Nov 24) but gap only +3% after the WSJ tariff report on China/Vietnam sourcing; USTR findings possibly this week. 1.79R, EV about +0.03, within calibration noise. Conviction 2."
    },
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "market",
      "entry": 637.71,
      "stop": 657.50,
      "targets": [606.50],
      "p_target_first": 0.37,
      "reason": "Best short. Monday's gap failing below its 641.95 low; rally called mechanical (Nomura), tariffs and a Dec hike priced. Stop above the 656.30 Monday high is only 0.82 ATR; 1.58R, EV about -0.05; Thanksgiving-week seasonality and Wed PCE against. Conviction 2."
    },
    {
      "ticker": "ADI",
      "direction": "short",
      "entry_type": "market",
      "entry": 339.03,
      "stop": 363.50,
      "targets": [300.00],
      "p_target_first": 0.35,
      "reason": "FQ4 beat, Q1 guide in line ($4.4B / $3.82), inventory days 141 vs 134; -10.5% mostly reverses Monday's +10% pre-report run-up (about -1.5% vs Friday). Already 1.6 ATR; call at 10:00 ET. 1.6R, EV about -0.09. Conviction 2."
    },
    {
      "ticker": "DKS",
      "direction": "long",
      "entry_type": "market",
      "entry": 151.00,
      "stop": 141.00,
      "targets": [168.00],
      "p_target_first": 0.36,
      "reason": "Q3 beat (EPS 1.94 vs 1.41, revenue 5.13B), FY guide raised; about +13% pre-market (~151 at 09:00 ET via search). Not in the market data table, so ATR and average volume are unverified; a 3-ATR-class gap. 1.7R, EV about -0.03. Conviction 2."
    },
    {
      "ticker": "DLTR",
      "direction": "long",
      "entry_type": "market",
      "entry": 148.96,
      "stop": 140.50,
      "targets": [162.00],
      "p_target_first": 0.36,
      "reason": "Q3 beat (EPS 1.16 vs 0.91, comps 4.6%), FY raised, but about $0.65 of it is tariff refunds and the Q4 guide was reportedly light; +7.1% = 1.6 ATR, above the 20-day high and about 19% above the 50-day; WSJ tariff report hits its sourcing. EV about -0.09. Conviction 2."
    },
    {
      "ticker": "NVDA",
      "direction": "short",
      "entry_type": "stop",
      "entry": 154.90,
      "stop": 172.00,
      "targets": [128.00],
      "p_target_first": 0.34,
      "reason": "Breakdown below Monday's 156.93 low would start filling the 125.53-167.04 gap; stop above the 171.50 Monday high. The CEO's return is a fundamental catalyst against it; ATR 9.5%; Huang Senate testimony Dec 3. 1.57R, EV about -0.13. Conviction 1."
    },
    {
      "ticker": "HPE",
      "direction": "short",
      "entry_type": "market",
      "entry": 41.90,
      "stop": 46.20,
      "targets": [36.00],
      "p_target_first": 0.35,
      "reason": "FQ4 beat and FY27 raised, but gross margin guided lower; -12.7% after +17% Monday, so back near the pre-rally level and on the 40.48 20-day low. 1.37R, EV about -0.17. Conviction 1."
    }
  ]
}
```

Sources:
- [Stockinvest.us pre-market digest, Nov 24 2026](https://stockinvest.us/digest/digest-us-premarket-2026-11-24)
- [SRN News / Reuters: Wall St futures dip as chip stocks cool](https://srnnews.com/wall-st-futures-dip-as-chip-stocks-cool-after-nvidia-fueled-rally/)
- [TradingKey US pre-market](https://www.tradingkey.com/analysis/stocks/us-stocks/262319957-us-pre-market-trump-jensen-huang-nvidia-ai-chips-xau-wti-oil-gold-ant-tradingkey)
- [mlq.ai: futures fall, Dollar Tree and DICK'S jump (403)](https://mlq.ai/news/us-stock-futures-fall-as-nvidia-gives-back-part-of-mondays-rally-dollar-tree-and-dicks-jump-premarket/)
- [Seeking Alpha: US prepares to raise tariffs (WSJ)](https://seekingalpha.com/news/4676107-us-prepares-to-raise-tariffs-on-china-eu-other-nations-wsj)
- [FXStreet: US prepares new tariffs (403)](https://www.fxstreet.com/news/us-prepares-new-tariffs-on-china-and-other-trading-partners-wsj-202611241338)
- [Benzinga: Trump China tariffs return](https://www.benzinga.com/markets/prediction-markets/26/11/63575690/trump-china-tariffs-return)
- [ADI Q4 FY26 release](https://investor.analog.com/news-releases/news-release-details/analog-devices-reports-record-fourth-quarter-and-fiscal-2026)
- [ADI 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0000006281/000000628126000087/adiq426exhibit991.htm)
- [Investing.com: Why is Analog Devices stock tumbling](https://www.investing.com/news/stock-market-news/why-is-analog-devices-stock-tumbling-today-93CH-5047890)
- [StockStory: Why ADI is down](https://stockstory.org/us/stocks/nasdaq/adi/news/why-up-down/why-analog-devices-stock-is-down-today)
- [ADI Q4 date announcement](https://www.analog.com/en/newsroom/press-releases/2026/10-22-2026-adi-report-4q-fy2026-financial-results.html)
- [CNBC: Best Buy Q3 FY27 earnings](https://www.cnbc.com/2026/11/24/best-buy-bby-q3-2027-earnings.html)
- [Best Buy Q3 FY27 release](https://corporate.bestbuy.com/2026/best-buy-reports-q3-fy27-results/)
- [Yahoo: Trump tariffs make Best Buy a big loser (2025 context)](https://finance.yahoo.com/news/trump-tariffs-make-best-buy-a-big-loser-as-citi-downgrades-the-stock-125712252.html)
- [Dollar Tree Q3 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0000935703/000093570326000136/ex991q3-26earningspressrel.htm)
- [Investing.com: Dollar Tree jumps on beat and raise](https://www.investing.com/news/stock-market-news/dollar-tree-stock-jumps-on-earnings-beat-and-raised-outlook-5047743)
- [DICK'S Q3 release (PR Newswire)](https://www.prnewswire.com/news-releases/dicks-sporting-goods-inc-reports-third-quarter-results-302948936.html)
- [Seeking Alpha: DICK'S gains 12% pre-market](https://seekingalpha.com/news/4676125-dicks-sporting-goods-gains-12-in-premarket-after-q3-beat)
- [RTTNews: DICK'S raises FY26 view](https://www.rttnews.com/3717586/dick-s-sporting-goods-raises-fy26-view-after-strong-q3-stock-up-18.aspx)
- [HPE fiscal Q4 2026 release](https://www.hpe.com/us/en/newsroom/press-release/2026/11/hpe-reports-fiscal-2026-fourth-quarter-results.html)
- [HPE 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001645590/000164559026000097/ex-991x11232026x8k.htm)
- [Medtronic Q2 FY27 date announcement](https://news.medtronic.com/2026-11-04-Medtronic-to-announce-financial-results-for-its-second-quarter-of-fiscal-year-2027)
- [HeyGoTrade: Nvidia +31.5% after Huang returns](https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-november-24-2026/)
- [Trefis: Nvidia, where's the floor](https://www.trefis.com/stock/nvda/articles/627453/nvidia-stock-at-125-where-s-the-floor/2026-11-23)
- [Investing.com: Bond market flattening and PCE test](https://www.investing.com/news/economy-news/bond-market-flattening-and-wednesdays-pce-test-for-ratehike-pricing-93CH-5046275)
- [mlq.ai: Treasury yields rise as traders drop 50bp bets](https://mlq.ai/news/treasury-yields-rise-as-traders-drop-bets-on-a-half-point-december-fed-hike/)
- [Investing.com: CB Consumer Confidence calendar](https://www.investing.com/economic-calendar/cb-consumer-confidence-48)
- [ForexFactory: CB Consumer Confidence](https://www.forexfactory.com/calendar/208-us-cb-consumer-confidence)
- [Cappnotes closing look, Nov 23 (403)](https://cappnotes.substack.com/p/closing-look-monday-november-23-2026)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Tuesday 2026-11-24. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$103,203.61**
- Cash: $121,012.04
- Session P&L so far: -0.15% (new entries are blocked at -3.0%)
- Gross exposure: $17,808 (17% of equity, cap 150%)
- Net exposure: $-17,808 (-17%, cap +/-100%)
- Risk at stake (entry to stop): $506 (0.49% of equity, cap 4.0%) — 3.51% left for new plays
- Slots: 1 open + 0 resting entries of 8 — you may add at most 7 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| HD | short | 51 | 343.57 | 349.19 | -286 (-1.6%) | -17% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **HD**, opened 2026-11-17 (session 6 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

### Your record

52 closed trades: 17W / 35L, total +2.52R, net $+3,507 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 52 | 19 | 30 | +0.05R |
| The same trades, bracket left alone | 52 | | | +0.07R |
| Ideas you passed on, or the caps dropped | 126 | 45 | 71 | +0.05R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 49 | 49% |
| 35%-40% | 83 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 5 | 20% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 165 brackets reached target first. Your Brier score is 0.241; saying 39% every time scores 0.237. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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
| HD | 348.34 (10:01 iex) | +0.7% | 346.06 | 346.06 / 343.19-349.09 | 10.33 (3.0%) | 316.15-362.44 | +1.5% / +9.6% | -0.4% | 5.1M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 719.65 (10:05 iex) | -0.4% | 722.29 | 715.18 / 712.14-720.89 | 18.45 (2.6%) | 686.75-775.64 | -3.1% / -4.9% | -2.4% | 61.2M |
| QQQ | 640.57 (10:05 iex) | -1.6% | 651.03 | 640.05 / 635.85-643.11 | 24.10 (3.7%) | 606.23-726.14 | -3.6% / -8.3% | -1.6% | 60.0M |
| IWM | 267.24 (10:05 iex) | +0.6% | 265.74 | 264.02 / 263.97-267.41 | 6.76 (2.5%) | 256.32-286.17 | -3.6% / -4.3% | -2.6% | 27.1M |
| DIA | 498.87 (10:05 iex) | +0.6% | 495.80 | 493.54 / 492.37-499.01 | 10.78 (2.2%) | 479.40-536.00 | -3.6% / -3.8% | -3.7% | 4.1M |
| TLT | 81.61 (10:04 iex) | -0.1% | 81.69 | 81.69 / 81.61-81.78 | 0.78 (1.0%) | 79.11-82.42 | +0.9% / +2.4% | +2.9% | 38.0M |
| GLD | 331.07 (10:05 iex) | -0.6% | 333.02 | 331.43 / 330.71-332.74 | 8.68 (2.6%) | 320.95-380.18 | -7.2% / -10.9% | -5.6% | 10.6M |
| USO | 135.22 (10:05 iex) | +1.4% | 133.36 | 135.14 / 134.89-135.75 | 5.47 (4.1%) | 132.84-171.82 | -10.2% / -11.8% | -4.8% | 4.8M |
| SMH | 431.46 (10:05 iex) | -6.2% | 460.18 | 441.00 / 429.92-442.97 | 32.98 (7.2%) | 396.85-571.00 | -6.2% / -15.7% | -0.4% | 13.1M |
| XLK | 157.75 (10:05 iex) | -2.9% | 162.38 | 158.47 / 156.51-158.76 | 7.83 (4.8%) | 148.09-191.55 | -5.2% / -11.7% | -1.4% | 16.1M |
| XLF | 56.30 (10:05 iex) | +1.2% | 55.65 | 55.51 / 55.31-56.31 | 1.18 (2.1%) | 54.42-60.04 | -2.7% / -0.3% | -4.3% | 41.3M |
| XLE | 60.53 (10:05 iex) | +1.1% | 59.87 | 60.09 / 59.55-60.69 | 1.69 (2.8%) | 59.74-70.15 | -6.6% / -7.3% | -6.0% | 37.3M |
| XLV | 183.63 (10:05 iex) | +2.3% | 179.42 | 179.65 / 179.27-183.65 | 3.93 (2.2%) | 176.71-192.32 | -2.7% / +1.5% | -4.5% | 13.3M |
| XLI | 161.67 (10:05 iex) | -0.5% | 162.47 | 161.04 / 160.92-161.92 | 4.18 (2.6%) | 155.70-172.40 | -2.5% / -3.1% | -1.9% | 9.4M |
| XLY | 117.64 (10:05 iex) | +0.6% | 116.93 | 116.41 / 116.04-117.64 | 3.29 (2.8%) | 112.03-122.92 | -0.8% / +2.4% | -1.0% | 10.0M |
| XLP | 91.90 (10:05 iex) | +1.7% | 90.38 | 90.77 / 90.43-91.88 | 1.64 (1.8%) | 86.36-93.48 | +0.0% / +4.5% | -2.4% | 21.6M |
| XLU | 43.59 (10:05 iex) | +0.6% | 43.32 | 43.14 / 42.92-43.60 | 0.66 (1.5%) | 42.42-44.40 | -0.2% / +3.3% | -1.8% | 25.9M |
| XLB | 49.91 (10:05 iex) | +0.0% | 49.90 | 49.46 / 49.36-49.95 | 1.20 (2.4%) | 48.21-54.63 | -3.8% / -1.7% | -3.1% | 13.1M |
| XLRE | 43.28 (10:04 iex) | +0.9% | 42.90 | 42.71 / 42.51-43.28 | 0.74 (1.7%) | 41.78-45.34 | -1.8% / +0.8% | -3.1% | 7.9M |
| XLC | 105.09 (10:04 iex) | +1.4% | 103.60 | 103.25 / 103.02-105.11 | 2.76 (2.7%) | 99.33-109.26 | -0.7% / -4.4% | -3.0% | 8.3M |
| KRE | 69.80 (10:05 iex) | +0.4% | 69.54 | 69.15 / 68.94-69.81 | 1.62 (2.3%) | 68.14-75.80 | -3.4% / -2.3% | -3.7% | 15.4M |
| XHB | 99.85 (09:59 iex) | +0.1% | 99.72 | 99.36 / 99.04-100.49 | 3.34 (3.4%) | 96.34-108.78 | -1.8% / +1.3% | -1.3% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 353.45 (10:05 iex) | +1.3% | 349.08 | 348.20 / 345.88-353.88 | 9.15 (2.6%) | 325.08-360.83 | +0.4% / +2.1% | -1.0% | 50.7M |
| MSFT | 493.69 (10:05 iex) | +0.2% | 492.50 | 490.79 / 488.43-495.18 | 19.24 (3.9%) | 481.03-558.07 | -5.3% / -5.0% | -4.7% | 30.8M |
| NVDA | 154.59 (10:05 iex) | -6.3% | 165.05 | 159.10 / 153.69-159.92 | 15.62 (9.5%) | 124.50-219.99 | -7.7% / -19.9% | +5.7% | 323.1M |
| AMZN | 254.88 (10:05 iex) | -0.2% | 255.39 | 252.00 / 250.53-255.21 | 11.92 (4.7%) | 229.36-275.34 | -0.9% / +0.1% | -0.9% | 54.1M |
| GOOGL | 280.26 (10:05 iex) | -0.7% | 282.10 | 281.60 / 277.00-281.78 | 12.53 (4.4%) | 264.22-326.40 | -2.0% / -12.1% | -0.6% | 46.5M |
| META | 597.43 (10:05 iex) | -0.0% | 597.60 | 589.09 / 588.28-599.68 | 25.31 (4.2%) | 558.68-648.45 | -3.1% / -11.5% | -4.6% | 21.1M |
| TSLA | 386.23 (10:05 iex) | +0.2% | 385.46 | 383.45 / 380.48-390.09 | 22.08 (5.7%) | 338.15-414.23 | +0.3% / +2.5% | +1.5% | 36.7M |
| AVGO | 306.55 (10:05 iex) | -2.2% | 313.55 | 301.29 / 298.41-309.02 | 23.76 (7.6%) | 289.77-369.82 | -5.4% / -8.3% | -6.0% | 31.6M |
| AMD | 415.21 (10:05 iex) | -8.4% | 453.46 | 425.12 / 405.02-428.87 | 54.21 (12.0%) | 402.10-594.00 | -10.2% / -17.9% | -10.1% | 44.3M |
| ORCL | 111.62 (10:05 iex) | -1.8% | 113.68 | 111.38 / 109.47-112.19 | 8.68 (7.6%) | 100.25-148.48 | -6.7% / -13.4% | -4.5% | 43.0M |
| NFLX | 59.59 (10:05 iex) | +2.6% | 58.10 | 57.88 / 57.57-59.72 | 2.05 (3.5%) | 56.56-67.49 | -6.3% / -13.2% | -4.4% | 40.9M |
| CRM | 194.00 (10:05 iex) | +4.6% | 185.46 | 183.89 / 183.89-194.76 | 8.61 (4.6%) | 179.91-248.08 | -13.4% / -18.7% | -13.7% | 7.3M |
| JPM | 318.77 (10:05 iex) | +0.7% | 316.66 | 314.78 / 314.00-318.93 | 9.44 (3.0%) | 309.18-359.80 | -5.7% / -5.8% | -6.4% | 7.2M |
| GS | 820.04 (10:04 iex) | -0.4% | 823.62 | 815.79 / 810.70-820.30 | 35.45 (4.3%) | 786.66-939.38 | -7.4% / -8.6% | -7.6% | 2.4M |
| BAC | 48.82 (10:05 iex) | +1.4% | 48.14 | 47.88 / 47.81-48.88 | 1.32 (2.7%) | 46.88-53.02 | -3.6% / -8.2% | -3.9% | 35.6M |
| XOM | 158.87 (10:04 iex) | +1.3% | 156.90 | 157.42 / 157.06-159.30 | 4.42 (2.8%) | 156.67-187.32 | -7.2% / -6.7% | -6.0% | 15.2M |
| CVX | 209.93 (10:04 iex) | +1.8% | 206.17 | 207.03 / 206.18-210.41 | 5.16 (2.5%) | 204.31-234.53 | -4.6% / -3.5% | -4.3% | 8.6M |
| LLY | 1,409.50 (10:04 iex) | +3.3% | 1,364.60 | 1,370.22 / 1,369.84-1,410.90 | 42.86 (3.1%) | 1,258.81-1,475.25 | -1.6% / +7.4% | -4.7% | 3.2M |
| UNH | 340.56 (10:05 iex) | +1.3% | 336.08 | 334.00 / 329.50-341.24 | 16.98 (5.1%) | 319.13-416.19 | -14.0% / -13.3% | -18.4% | 7.2M |
| JNJ | 274.32 (10:05 iex) | +2.1% | 268.71 | 269.99 / 268.08-274.28 | 6.90 (2.6%) | 262.89-288.81 | -1.9% / +1.0% | -4.4% | 8.1M |
| WMT | 131.90 (10:05 iex) | +1.8% | 129.58 | 129.94 / 129.74-131.81 | 3.22 (2.5%) | 118.11-131.82 | +3.0% / +10.7% | +0.9% | 24.2M |
| COST | 1,089.32 (10:04 iex) | +2.0% | 1,067.91 | 1,072.13 / 1,067.92-1,089.34 | 20.00 (1.9%) | 952.12-1,092.97 | +3.4% / +11.0% | -1.4% | 2.6M |
| HD | 348.34 (10:01 iex) | +0.7% | 346.06 | 346.06 / 343.19-349.09 | 10.33 (3.0%) | 316.15-362.44 | +1.5% / +9.6% | -0.4% | 5.1M |
| CAT | 537.01 (10:05 iex) | -1.8% | 547.04 | 539.78 / 537.24-544.29 | 31.14 (5.7%) | 508.11-732.73 | -8.2% / -22.8% | -4.1% | 4.2M |
| BA | 163.62 (10:04 iex) | +0.8% | 162.39 | 161.87 / 161.07-164.46 | 5.42 (3.3%) | 155.56-187.86 | -4.1% / -11.3% | -1.7% | 10.8M |
| DAL | 84.19 (10:04 iex) | -0.2% | 84.34 | 83.46 / 83.17-84.30 | 3.50 (4.1%) | 78.49-92.52 | -1.0% / +2.4% | -2.6% | 6.1M |
| UAL | 107.42 (10:04 iex) | -1.2% | 108.71 | 106.86 / 106.30-107.80 | 5.75 (5.3%) | 100.02-122.08 | -0.9% / +0.8% | -1.9% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| PINS | 19.07 (10:05 iex) | +12.8% | 16.90 | 17.07 / 16.99-19.48 | 0.81 (4.8%) | 16.30-21.60 | -11.3% / -14.7% | -8.3% | 13.8M |
| DLTR | 153.09 (10:04 iex) | +10.1% | 139.10 | 150.00 / 147.83-155.21 | 6.10 (4.4%) | 122.57-148.53 | +1.4% / +10.8% | +0.3% | 2.3M |
| CPNG | 15.91 (10:05 iex) | +7.9% | 14.74 | 14.71 / 14.71-15.94 | 0.81 (5.5%) | 13.69-17.45 | -2.2% / +0.6% | +2.7% | 16.1M |
| TTWO | 221.60 (10:05 iex) | +5.8% | 209.36 | 208.92 / 206.54-221.69 | 14.88 (7.1%) | 183.86-237.41 | +0.1% / +1.0% | -1.9% | 5.2M |
| TTD | 14.85 (10:05 iex) | +5.6% | 14.06 | 14.08 / 14.04-14.86 | 1.07 (7.6%) | 12.23-16.42 | +0.4% / +6.2% | -5.2% | 23.5M |
| MRNA | 223.74 (10:05 iex) | +5.5% | 212.08 | 213.20 / 212.08-226.94 | 19.06 (9.0%) | 179.53-280.80 | -6.1% / +1.4% | -1.5% | 10.3M |
| SNAP | 5.17 (10:05 iex) | +5.2% | 4.92 | 4.88 / 4.86-5.21 | 0.38 (7.8%) | 4.53-6.37 | -7.7% / -13.1% | -3.3% | 48.3M |
| HUM | 403.42 (10:05 iex) | +5.1% | 383.68 | 384.68 / 381.55-404.88 | 23.41 (6.1%) | 373.17-462.87 | -8.6% / -6.1% | -16.8% | 1.8M |
| ADI | 319.00 (10:05 iex) | -15.8% | 378.75 | 328.50 / 317.66-337.57 | 24.17 (6.4%) | 343.94-433.72 | -4.4% / -4.4% | -1.2% | 5.5M |
| HPE | 41.35 (10:05 iex) | -13.9% | 48.02 | 42.47 / 40.08-42.49 | 4.05 (8.4%) | 40.48-62.20 | -3.5% / -16.5% | +3.1% | 16.5M |
| DELL | 299.41 (10:05 iex) | -10.6% | 334.91 | 311.00 / 296.21-318.22 | 40.09 (12.0%) | 274.35-507.38 | -9.1% / -28.2% | +4.5% | 8.4M |
| ENTG | 128.69 (10:05 iex) | -9.4% | 142.06 | 135.77 / 128.63-139.59 | 13.43 (9.5%) | 123.25-170.06 | -1.6% / -3.7% | +1.5% | 4.0M |
| SNDK | 79.62 (10:05 iex) | -9.2% | 87.71 | 82.72 / 78.85-83.82 | 13.95 (15.9%) | 78.25-176.06 | -26.5% / -47.2% | -13.3% | 111.6M |
| MPWR | 1,214.94 (10:05 iex) | -8.9% | 1,333.88 | 1,283.34 / 1,214.50-1,287.88 | 118.54 (8.9%) | 1,125.00-1,513.49 | +3.5% / +3.0% | +1.5% | 1.2M |
| MU | 647.45 (10:05 iex) | -8.5% | 707.70 | 669.39 / 640.50-672.07 | 74.64 (10.5%) | 585.25-990.00 | -8.9% / -22.0% | -1.6% | 35.2M |
| TXN | 266.83 (10:05 iex) | -8.4% | 291.19 | 278.58 / 265.64-281.38 | 17.93 (6.2%) | 262.29-317.20 | -2.2% / +1.8% | -1.0% | 9.2M |
