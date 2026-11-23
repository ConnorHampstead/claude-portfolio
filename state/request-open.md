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

# Pre-market brief: Monday 2026-11-23, 09:05 ET (15:05 Stockholm)

No new trades today. I looked at nine names and the indices, and every setup came out at roughly zero expected value on my own numbers. The HD short stays as submitted: it is in session 5 of 10 and its invalidation has not happened.

### 1. Tape

**Friday was a rout.** The S&P 500 fell 3.7% to 6,910.39 and closed in correction, the Nasdaq Composite fell 5.3%, and the S&P lost 8.6% on the week. That is its worst week since April 2025, and the Nasdaq's worst since March 2020. The VIX ended near 36. The selling centred on AI and semis, with three reasons cited:
- AI capex doubts;
- midterm wins for candidates who want to slow data-centre building;
- a weak Anthropic post-IPO tape.

**This morning has reversed most of it.** Nvidia's board reinstated Jensen Huang as CEO, effective immediately. The company release says US government officials told the board his return poses no national-security risk; it was issued after Trump urged the rehire on Sunday. CrowdStrike also announced an all-stock purchase of Zscaler.
- **Index ETFs at 09:03–09:05:** SPY 719.67 (+4.3%), QQQ 651.00 (+7.0%).
- **Semis:** SMH +16.4%, NVDA 164.67 (+31.2%).
- **Elsewhere:** VIX about 31.9 (−11%), gold +4%, crude −2.4%. The 10-year is about 4.91–4.96%; sources conflict. A December hike is still about 96% priced.

**Regime:** a violent relief rally inside a correction, with a Fed hiking into weaker data. Today's edge is long, but the gap has already priced most of it. NVDA is back near its pre-resignation level. QQQ has retraced about 60% of last week's fall before the open.

**Short side:** managed care is breaking down on a second hostile CMS proposal in a week (UNH −6.1%). CRWD is −5.6% as the acquirer.

### 2. Calendar

Stockholm is ET+6 today (verified from the book clock).

| Time ET / Stockholm | Event | Status / consensus | Touches |
|---|---|---|---|
| 08:30 / 14:30 | Chicago Fed National Activity Index (Oct) | Prior 0.07. **I could not find the actual print.** | Ambient |
| Pre-market | NVDA reinstates Huang (company release); CRWD Q3 FY27 plus $43.9B Zscaler deal at 1.135 CRWD per ZS | Already out. NVDA +31%. CRWD −5.6% at 216.52, ZS +22% at 238.27 (implied value about 245.75, a ~3% arb spread) | Indices, HD (beta) |
| Pre-market | CMS CY2028 Medicare Advantage proposed rule (Star Ratings overhaul) | Already out. CMS estimates about $107B in MA payment cuts over 2028–37 ($11.5B in 2031). UNH −6.1%, CVS −3.8%, HUM −3.3%, ELV −3.6% | UNH (passed) |
| 09:45 / 15:45 | S&P Global flash PMIs (Nov) | Mfg 54.5 (prior 54.9), services 55.7 (prior 56.1), composite prior 55.9 | Review |
| Time not verified | NY Fed's Williams speaks | Fox Business lists it; I found no time | Ambient |
| After close | HPE (call 17:00 ET / 23:00), Zoom, Agilent | Not held | — |
| Tue 11/24 | ADI 07:00 ET; Conference Board confidence (est 92.0, time not stated); Dell after close | — | — |
| Wed 11/25 08:30 / 14:30 | Q3 GDP 2nd estimate (3.4%); Oct PCE (core +0.3% m/m, 3.2% y/y) | Consensus | Everything |
| Thu 11/26 | Closed (Thanksgiving) | The harness clears resting entries before the holiday | — |
| Fri 11/27 | Early close 13:00 ET / 19:00 | — | — |
| Dec 1–2 | Huang closed-door House interviews | NVDA's own scheduled event | NVDA (passed) |
| Dec 8–9 | FOMC | ~96% priced for a 25bp hike | — |

Yahoo's live blog said "wholesale inflation data due Monday". The BLS shows October PPI came out Nov 13 and the next is Dec 15, so I treat today as having no PPI release.

### 3. Open positions and resting entries

**HD short (entry 343.57, stop 353.50, target 323.50): hold, session 5 of 10.**
- **Invalidation (close above 347.51): not met.** Friday closed at 339.04. Pre-market is 344.58 (+1.6%, 08:30 SIP), carried up by the broad rally.
- **Own events:** none. Q3 was reported Nov 17. I didn't verify the ex-date of the $2.33 dividend declared Nov 19; a short owes it if held across.
- **Action:** none of the three close conditions applies, so the bracket stays as submitted. If HD closes above 347.51 today, tomorrow's brief closes it on the recorded invalidation.

**Resting entries:** none.

### 4. New plays

**None.** Every candidate came out at roughly zero EV on my numbers (section 6).

### 5. Both sides

**Best long: NVDA, buy limit 155.00, stop 141.00, target 190.00, P 0.31.**
- **Catalyst:** the reinstatement, verified in Nvidia's own release dated Nov 23.
- **The case:** a 25% retrace of the gap that holds would be the place to own a removed overhang. The stop sits well under the 148.80 low of Nov 12, the day he resigned. 190 is above the ~181 20-day average and the 173.73 pre-resignation close.
- **Why I pass:**
  - The gap is already 3 ATR.
  - Last week NVDA reportedly closed below its pre-market price in all five sessions. That is a headline I could not open.
  - Huang's House interviews on Dec 1–2 fall inside the window.
  - EV is about +0.08, which is too thin.

**Best short: UNH, sell limit 331.00, stop 348.50, target 298.00, P 0.35.**
- **Catalyst:** the CMS Star Ratings proposal. CMS actuary figures are quoted via Investing.com (TD Cowen: "particularly negative for UNH and HUM") and the Healthcare Labyrinth analysis. I could not open the HHS release (403), so this rests on secondary sources.
- **Levels:** the bounce-sell sits about halfway into today's gap. The stop is above Friday's 339.85 close and about 1.1 ATR above entry.
- **Why I pass:**
  - UNH is already about −22% in six sessions and −1.3 ATR today.
  - The payment effects start in 2031.
  - The sector bounced +4.5% Friday after the RADV shock (CMS's audit-recovery proposal of Nov 18), so dip buyers are active.
  - At 1.89R, P 0.35 gives EV ≈ 0.

**Also examined on the short side:** QQQ fade at a 655–668 retest, an NVDA gap fade, CRWD (acquirer with arbitrage pressure), and AVGO (+1.3% while semis are +16%; the Google HBM story is still unconfirmed by Google or Broadcom).

### 6. Passing on

- **UNH short** (levels above). EV ≈ 0, the stock is extended, and the source is secondary. Conviction 2.
- **NVDA long** (levels above). The gap has priced the reinstatement, and the stock has its own scheduled event Dec 1–2. Conviction 2.
- **QQQ short, sell limit 662, stop 684, target 618, P 0.32.**
  - The stop sits above the ~678 20-day average and the ~680 close of Nov 13; the target sits above Friday's 608.45 close.
  - At 2.0R, EV is about −0.04.
  - Against it: a first relief day after seven down days, a real catalyst, and Thanksgiving seasonality. Conviction 2.
- **CRWD long, market ~216.50, stop 198, target 246, P 0.34.**
  - For: a record $419M of net new ARR and a raised guide.
  - Against: arbitrage hedging of the all-stock deal keeps selling pressure on the acquirer. JPMorgan says the deal dilutes growth and FCF margins.
  - EV −0.12.
- **ZS:** merger arbitrage (~3% spread), not a directional trade.
- **Semis ex-NVDA (KLAC +21%, MU +17%, LRCX +18%, TSM +15%):** no catalyst of their own found beyond sympathy and Citi's memory note. I can't explain the moves at source. No levels.
- **GLD +3.9% / USO −3.3%:** no dated reason found for gold; oil is at its 20-day low ahead of OPEC+ on Nov 29. No levels.
- **HUM/CVS shorts:** the same CMS catalyst as UNH and less extended, but I have no data-table levels for HUM and the source is secondary. No levels.

### 7. For the post-open review (≈10:05 ET / 16:05 Stockholm)

- **QQQ:** if QQQ is below 640 at 10:05 (the gap failing, more than a quarter given back), the review may place a sell limit at 652, stop 676, target 612 (1.67R), at 0.5 tier, conviction 3. If QQQ is above 655 and making highs, no index short; the 662 level stays shadow-only.
- **NVDA:** if NVDA is between 150 and 158 at 10:05 and has held 148.80, the review may buy at 0.5 tier with stop 141 and target 190. Above 158, no chase. Below 148.80 the gap has failed: no trade.
- **UNH:** if it has bounced to 328–333 and is rolling over, the review may place the 331 / 348.50 / 298 short at 0.5 tier, conviction 3. Below 315, no chase.
- **PMIs (09:45):** a services print above 57 with yields rising adds weight to the QQQ condition. No order depends on the print alone.
- **HD:** no action. Tomorrow's brief applies the 347.51 close test.

### 8. Book state

- **Exposure:** gross ~17%, net −17% of equity (caps 150% / ±100%).
- **Risk and slots:** risk at stake 0.49% (cap 4%); 1 of 8 slots.
- **Today's orders:** none, so these figures are unchanged.

```json
{
  "date": "2026-11-23",
  "no_trade": true,
  "session_note": "Relief gap after a 7-day, -8.6% week: NVDA reinstated Huang (+31%), SPY +4.3%, QQQ +7%, VIX ~32, Dec hike ~96%. Gap already prices the catalyst; UNH (CMS Stars proposal) is extended. Best ideas are near zero EV. Would act on: QQQ below 640 at 10:05 (short 652/676/612, 0.5 tier), NVDA holding 150-158 above 148.80 (long, stop 141, target 190, 0.5 tier), or UNH failing at a 328-333 bounce (short 331/348.50/298, 0.5 tier). HD held, invalidation not met.",
  "plays": [],
  "manage": [],
  "passed": [
    {
      "ticker": "UNH",
      "direction": "short",
      "entry_type": "limit",
      "entry": 331.00,
      "stop": 348.50,
      "targets": [298.00],
      "p_target_first": 0.35,
      "reason": "CMS CY2028 MA proposed rule (Stars overhaul, ~$107B cuts 2028-37 per CMS actuaries, via Investing.com/TD Cowen and Healthcare Labyrinth; HHS page unreadable). UNH -6.1% pre-market at 319, about -22% in 6 sessions; bounce-sell into the gap, stop above Friday's 339.85 close. EV ~0 at 1.89R; extended and secondary-sourced. Conviction 2."
    },
    {
      "ticker": "NVDA",
      "direction": "long",
      "entry_type": "limit",
      "entry": 155.00,
      "stop": 141.00,
      "targets": [190.00],
      "p_target_first": 0.31,
      "reason": "Huang reinstated as CEO (Nvidia release, Nov 23); +31% pre-market to 164.67, about 3 ATR, near the 173.73 pre-resignation close. Buy a 25% gap retrace; stop under the 148.80 Nov 12 low. House interviews Dec 1-2 inside the window; EV +0.08 too thin. Conviction 2."
    },
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "limit",
      "entry": 662.00,
      "stop": 684.00,
      "targets": [618.00],
      "p_target_first": 0.32,
      "reason": "Fade a relief gap (651 pre-market, +7%) into the 655-668 retest zone under the ~678 20-day average. Against it: first rebound day after 7 down days on a real catalyst, plus holiday seasonality. EV about -0.04. Conviction 2."
    },
    {
      "ticker": "CRWD",
      "direction": "long",
      "entry_type": "market",
      "entry": 216.50,
      "stop": 198.00,
      "targets": [246.00],
      "p_target_first": 0.34,
      "reason": "Record $419M net new ARR and raised FY27 guide (8-K, Nov 23), but the all-stock ZS deal (1.135x) leaves arbitrage hedging pressure on the acquirer and JPM calls it dilutive to growth and FCF margins. -5.6% pre-market near the 213.22 20-day low. EV -0.12. Conviction 2."
    }
  ]
}
```

Sources:
- [NVIDIA: Board reinstates Jensen Huang (Nov 23)](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director)
- [GlobeNewswire: NVIDIA reinstatement release](https://www.globenewswire.com/news-release/2026/11/23/3408381/0/en/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director.html)
- [Yahoo Finance: Trump U-turn on Huang](https://finance.yahoo.com/markets/stocks/article/nvidia-stock-jumps-as-dc-makes-stunning-u-turn-on-jensen-huang-113419437.html)
- [Yahoo Finance live: Nov 23 market](https://finance.yahoo.com/markets/live/stock-market-today-monday-november-23-dow-sp-500-nasdaq-091118583.html)
- [Yahoo/Investing.com: Premarket movers](https://finance.yahoo.com/markets/stocks/articles/premarket-movers-chip-stocks-lead-124424524.html)
- [QUE.com: Futures roar back, week calendar](https://que.com/futures-roar-back-monday-morning-after-wall-streets-worst-week-in-18-months-but-the-real-tests-are-still-ahead/)
- [Fox Business: Nov 23 futures](https://www.foxbusiness.com/markets/stocks-november-23-2026)
- [ABF Journal: Nasdaq plunge and the Fed](https://www.abfjournal.com/middle-market-debt-weekly-nasdaqs-10-plunge-collides-with-a-fed-openly-debating-a-50-basis-point-december-hike/)
- [CrowdStrike 8-K Ex 99.1 (Q3 FY27)](https://www.sec.gov/Archives/edgar/data/0001535527/000153552726000035/crwd-20261123xex991.htm)
- [CrowdStrike 8-K (deal)](https://www.sec.gov/Archives/edgar/data/0001535527/000110465926130785/tm2630454d1_ex99-1.htm)
- [Invezz: CRWD falls on ZS deal](https://invezz.com/news/2026/11/23/crowdstrike-stock-falls-after-agreeing-to-buy-zscaler-for-43-9b/)
- [Investing.com: CRWD analyst reaction](https://www.investing.com/news/analyst-ratings/crowdstrike-stock-holds-buy-rating-as-zscaler-deal-talks-emerge-93CH-5045455)
- [Investing.com: Health insurers slide on MA proposal](https://www.investing.com/news/stock-market-news/health-insurer-stocks-slide-as-medicare-advantage-proposal-threatens-payments-5045476)
- [Healthcare Labyrinth: CMS second Stars overhaul](https://www.healthcarelabyrinth.com/cms-proposes-a-second-overhaul-of-medicare-advantage-stars/)
- [HHS press release (unreadable, 403)](https://www.hhs.gov/press-room/cms-proposes-medicare-advantage-reforms-competition-quality-beneficiary-choice.html)
- [days.to: UNH Q4 date (unconfirmed)](https://days.to/when-is/unitedhealth-earnings)
- [BLS PPI release](https://www.bls.gov/news.release/ppi.nr0.htm)
- [TheWrap: NVDA falls as Huang resigns](https://www.thewrap.com/industry-news/business/nvidia-ceo-jensen-huang-resignation-stock-reaction/)
- [IBTimes: NVDA $159 after resignation](https://www.ibtimes.com.au/nvidia-shares-fall-jensen-huang-resigns-ceo-1878502)
- [Quackonomist pre-market headline (unreadable, 403)](https://quackonomist.substack.com/p/quackonomist-pre-market-23-nov-2026)
- [Tradersunion: yields rise Monday](https://tradersunion.com/news/economic-data/show/4371722-us-treasury-yields-rise-wall-street/)
- [MarketScreener: futures rise pre-bell](https://www.marketscreener.com/news/us-equity-futures-rise-pre-bell-as-nvidia-starts-off-week-strong-ce7851dadb80f724)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Monday 2026-11-23. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$103,514.96**
- Cash: $121,012.04
- Session P&L so far: -0.20% (new entries are blocked at -3.0%)
- Gross exposure: $17,497 (17% of equity, cap 150%)
- Net exposure: $-17,497 (-17%, cap +/-100%)
- Risk at stake (entry to stop): $506 (0.49% of equity, cap 4.0%) — 3.51% left for new plays
- Slots: 1 open + 0 resting entries of 8 — you may add at most 7 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| HD | short | 51 | 343.57 | 343.08 | +25 (+0.1%) | -17% | 353.50 | 323.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **HD**, opened 2026-11-17 (session 5 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.

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
| HD | 343.00 (10:04 iex) | +1.2% | 339.04 | 342.14 / 339.25-343.50 | 10.42 (3.1%) | 316.15-362.44 | -0.1% / +7.6% | -2.8% | 5.0M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 722.17 (10:05 iex) | +4.7% | 689.81 | 724.38 / 713.53-724.81 | 16.07 (2.3%) | 686.75-775.64 | -7.8% / -9.2% | -8.6% | 58.4M |
| QQQ | 650.81 (10:05 iex) | +7.0% | 608.45 | 655.98 / 641.95-656.30 | 21.13 (3.5%) | 606.23-726.14 | -10.3% / -14.4% | -10.5% | 57.4M |
| IWM | 264.45 (10:05 iex) | +3.1% | 256.61 | 266.02 / 262.86-266.08 | 6.28 (2.4%) | 256.32-286.17 | -7.1% / -7.8% | -7.5% | 26.3M |
| DIA | 494.60 (10:05 iex) | +2.8% | 481.08 | 494.22 / 489.80-494.55 | 9.90 (2.1%) | 479.40-536.00 | -6.7% / -6.7% | -7.9% | 4.0M |
| TLT | 81.41 (10:04 iex) | -0.0% | 81.45 | 81.09 / 81.08-81.42 | 0.78 (1.0%) | 79.11-82.42 | +0.7% / +2.1% | +2.6% | 36.6M |
| GLD | 336.36 (10:05 iex) | +4.2% | 322.87 | 337.98 / 335.40-338.00 | 7.81 (2.4%) | 320.95-380.18 | -10.4% / -13.9% | -9.2% | 10.3M |
| USO | 134.95 (10:05 iex) | -3.4% | 139.63 | 136.52 / 135.20-136.56 | 5.13 (3.7%) | 135.01-171.82 | -7.0% / -7.9% | -4.1% | 4.9M |
| SMH | 460.10 (10:05 iex) | +15.0% | 400.06 | 469.31 / 449.64-469.35 | 29.20 (7.3%) | 396.85-571.00 | -19.1% / -26.9% | -17.8% | 12.6M |
| XLK | 162.84 (10:05 iex) | +9.3% | 149.01 | 164.52 / 159.90-164.79 | 6.92 (4.6%) | 148.09-191.55 | -13.6% / -19.2% | -12.5% | 15.2M |
| XLF | 55.65 (10:05 iex) | +2.0% | 54.57 | 55.66 / 55.26-55.76 | 1.12 (2.1%) | 54.42-60.04 | -4.6% / -2.3% | -7.0% | 39.5M |
| XLE | 60.72 (10:05 iex) | +0.3% | 60.51 | 60.50 / 60.34-60.98 | 1.68 (2.8%) | 60.34-70.15 | -6.4% / -6.4% | -6.9% | 37.0M |
| XLV | 179.31 (10:05 iex) | +1.2% | 177.24 | 177.25 / 177.24-179.59 | 3.88 (2.2%) | 176.71-192.32 | -3.9% / +0.5% | -6.1% | 13.0M |
| XLI | 161.64 (10:05 iex) | +3.4% | 156.37 | 161.92 / 160.28-162.41 | 3.89 (2.5%) | 155.70-172.40 | -6.3% / -6.9% | -7.4% | 9.2M |
| XLY | 116.79 (10:05 iex) | +3.9% | 112.46 | 116.48 / 115.59-116.74 | 3.03 (2.7%) | 112.03-122.92 | -4.5% / -1.5% | -6.3% | 9.7M |
| XLP | 89.67 (10:05 iex) | -0.9% | 90.46 | 89.59 / 89.46-90.12 | 1.69 (1.9%) | 86.36-93.48 | +0.2% / +4.8% | -2.0% | 21.0M |
| XLU | 42.88 (10:05 iex) | +0.5% | 42.69 | 42.87 / 42.82-43.23 | 0.64 (1.5%) | 42.42-44.40 | -1.6% / +1.9% | -3.1% | 24.7M |
| XLB | 49.34 (10:05 iex) | +2.1% | 48.34 | 49.62 / 49.01-49.68 | 1.17 (2.4%) | 48.21-54.63 | -6.9% / -4.8% | -7.4% | 13.0M |
| XLRE | 42.81 (10:04 iex) | +0.8% | 42.46 | 43.13 / 42.80-43.17 | 0.72 (1.7%) | 41.78-45.34 | -2.8% / -0.2% | -4.3% | 7.9M |
| XLC | 102.67 (10:05 iex) | +2.6% | 100.03 | 103.31 / 101.62-103.34 | 2.58 (2.6%) | 99.33-109.26 | -4.2% / -7.9% | -8.0% | 8.4M |
| KRE | 69.39 (10:05 iex) | +1.6% | 68.32 | 69.51 / 69.00-69.96 | 1.58 (2.3%) | 68.14-75.80 | -5.3% / -4.2% | -6.1% | 15.1M |
| XHB | 98.38 (10:04 iex) | +1.8% | 96.60 | 98.80 / 97.58-98.89 | 3.30 (3.4%) | 96.34-108.78 | -4.8% / -1.8% | -5.4% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 349.17 (10:05 iex) | +1.9% | 342.56 | 347.87 / 345.44-349.76 | 9.36 (2.7%) | 325.08-360.83 | -1.4% / +0.3% | -3.8% | 49.9M |
| MSFT | 504.85 (10:05 iex) | +4.2% | 484.52 | 506.00 / 499.62-509.15 | 18.64 (3.8%) | 481.03-558.07 | -7.2% / -6.6% | -7.3% | 30.2M |
| NVDA | 166.50 (10:05 iex) | +32.6% | 125.53 | 167.04 / 156.93-169.53 | 12.84 (10.2%) | 124.50-219.99 | -30.8% / -39.4% | -22.9% | 288.5M |
| AMZN | 255.49 (10:05 iex) | +3.5% | 246.82 | 260.26 / 251.25-262.48 | 11.29 (4.6%) | 229.36-275.34 | -4.1% / -3.2% | -7.4% | 53.1M |
| GOOGL | 281.58 (10:05 iex) | +6.1% | 265.29 | 284.27 / 275.36-284.60 | 11.42 (4.3%) | 264.22-326.40 | -8.3% / -17.7% | -10.3% | 45.5M |
| META | 589.27 (10:05 iex) | +5.1% | 560.84 | 591.72 / 579.78-595.00 | 23.63 (4.2%) | 558.68-648.45 | -9.3% / -17.1% | -12.6% | 21.7M |
| TSLA | 390.00 (10:05 iex) | +12.8% | 345.82 | 374.89 / 371.95-389.56 | 19.36 (5.6%) | 338.15-414.23 | -10.1% / -7.9% | -11.4% | 37.0M |
| AVGO | 309.18 (10:05 iex) | +1.6% | 304.41 | 321.00 / 304.56-324.46 | 23.29 (7.7%) | 289.77-369.82 | -8.4% / -11.2% | -12.3% | 30.4M |
| AMD | 447.69 (10:05 iex) | +5.5% | 424.39 | 477.75 / 432.20-477.75 | 52.59 (12.4%) | 402.10-594.00 | -16.6% / -23.3% | -20.5% | 42.4M |
| ORCL | 114.40 (10:05 iex) | +13.1% | 101.19 | 116.73 / 112.98-118.70 | 8.06 (8.0%) | 100.25-148.48 | -17.4% / -23.3% | -19.3% | 42.2M |
| NFLX | 57.86 (10:05 iex) | +2.0% | 56.73 | 58.56 / 57.23-58.61 | 2.03 (3.6%) | 56.56-67.49 | -8.9% / -15.8% | -8.7% | 41.1M |
| CRM | 184.12 (10:05 iex) | +1.9% | 180.62 | 183.31 / 181.68-184.49 | 9.06 (5.0%) | 179.91-250.99 | -16.9% / -21.4% | -17.1% | 7.3M |
| JPM | 318.18 (10:05 iex) | +2.5% | 310.53 | 319.19 / 315.00-321.61 | 9.00 (2.9%) | 309.18-359.80 | -7.7% / -7.8% | -10.3% | 7.0M |
| GS | 824.82 (10:05 iex) | +4.3% | 790.69 | 831.01 / 814.96-834.54 | 33.10 (4.2%) | 786.66-939.38 | -11.5% / -12.6% | -13.7% | 2.3M |
| BAC | 48.28 (10:05 iex) | +2.6% | 47.04 | 48.28 / 47.69-48.49 | 1.27 (2.7%) | 46.88-53.02 | -6.0% / -10.7% | -7.8% | 35.5M |
| XOM | 158.83 (10:05 iex) | -0.7% | 159.99 | 157.94 / 157.15-159.54 | 4.41 (2.8%) | 158.60-187.32 | -6.1% / -5.0% | -5.6% | 15.0M |
| CVX | 208.22 (10:04 iex) | -0.1% | 208.37 | 206.00 / 205.34-209.12 | 5.13 (2.5%) | 204.31-234.53 | -4.1% / -2.5% | -4.5% | 8.5M |
| LLY | 1,371.28 (10:04 iex) | +1.8% | 1,347.11 | 1,345.11 / 1,344.00-1,374.71 | 43.28 (3.2%) | 1,258.81-1,475.25 | -2.6% / +6.4% | -6.7% | 3.2M |
| UNH | 333.11 (10:04 iex) | -2.0% | 339.85 | 322.30 / 319.13-333.56 | 16.10 (4.7%) | 324.67-420.86 | -13.9% / -12.6% | -16.6% | 6.8M |
| JNJ | 271.75 (10:05 iex) | +0.5% | 270.47 | 269.85 / 267.36-272.21 | 6.99 (2.6%) | 264.20-290.25 | -1.7% / +1.1% | -5.3% | 7.9M |
| WMT | 127.39 (10:05 iex) | -0.4% | 127.95 | 126.64 / 125.84-127.94 | 3.15 (2.5%) | 118.11-131.82 | +2.1% / +9.7% | -0.1% | 23.7M |
| COST | 1,089.64 (10:05 iex) | -1.1% | 1,102.15 | 1,090.52 / 1,088.63-1,097.99 | 20.87 (1.9%) | 978.87-1,123.67 | +4.3% / +11.8% | -0.4% | 2.6M |
| HD | 343.00 (10:04 iex) | +1.2% | 339.04 | 342.14 / 339.25-343.50 | 10.42 (3.1%) | 316.15-362.44 | -0.1% / +7.6% | -2.8% | 5.0M |
| CAT | 547.03 (10:05 iex) | +7.2% | 510.45 | 554.79 / 538.40-560.00 | 28.65 (5.6%) | 508.11-732.73 | -15.4% / -28.4% | -15.0% | 4.1M |
| BA | 161.46 (10:05 iex) | +3.6% | 155.89 | 160.00 / 159.10-161.19 | 5.12 (3.3%) | 155.56-189.66 | -8.6% / -15.3% | -9.1% | 10.8M |
| DAL | 83.07 (10:03 iex) | +3.8% | 80.01 | 83.48 / 82.14-83.87 | 3.26 (4.1%) | 77.06-92.52 | -5.8% / -2.8% | -7.2% | 6.1M |
| UAL | 106.41 (10:05 iex) | +5.3% | 101.03 | 106.78 / 104.39-106.79 | 5.43 (5.4%) | 98.37-122.08 | -7.5% / -6.4% | -7.6% | 5.4M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| DELL | 341.52 (10:05 iex) | +22.8% | 278.02 | 376.54 / 322.31-379.03 | 34.69 (12.5%) | 274.35-507.38 | -25.8% / -40.9% | -19.3% | 7.9M |
| MRVL | 145.73 (10:05 iex) | +19.2% | 122.28 | 145.95 / 139.40-146.53 | 15.01 (12.3%) | 120.56-253.66 | -28.5% / -44.5% | -22.0% | 32.9M |
| SMCI | 25.77 (10:05 iex) | +19.0% | 21.65 | 26.27 / 25.16-26.27 | 2.49 (11.5%) | 21.46-36.40 | -25.1% / -38.1% | -19.4% | 46.5M |
| MU | 704.96 (10:05 iex) | +18.6% | 594.51 | 690.87 / 666.66-703.35 | 68.34 (11.5%) | 585.25-990.00 | -24.4% / -34.8% | -23.6% | 33.9M |
| ZS | 228.64 (10:05 iex) | +17.4% | 194.82 | 238.01 / 226.21-247.90 | 12.42 (6.4%) | 180.47-267.87 | -9.1% / -8.3% | +1.2% | 2.4M |
| ARM | 177.57 (10:05 iex) | +16.7% | 152.20 | 183.29 / 171.46-184.13 | 16.77 (11.0%) | 150.37-237.88 | -21.6% / -36.5% | -20.1% | 6.3M |
| SNDK | 92.22 (10:05 iex) | +16.4% | 79.24 | 98.56 / 88.34-99.07 | 13.23 (16.7%) | 78.25-176.06 | -35.5% / -52.9% | -28.4% | 108.6M |
| TSM | 369.39 (10:05 iex) | +15.9% | 318.71 | 385.49 / 362.04-386.90 | 21.77 (6.8%) | 318.48-440.88 | -18.7% / -24.5% | -20.1% | 17.0M |
| CRWD | 208.06 (10:05 iex) | -9.3% | 229.44 | 217.97 / 206.02-225.51 | 15.34 (6.7%) | 213.22-272.29 | -3.6% / -7.1% | +1.2% | 9.2M |
| STZ | 137.10 (10:04 iex) | -3.4% | 141.87 | 140.00 / 137.10-141.00 | 4.22 (3.0%) | 128.06-149.43 | +0.9% / +10.0% | -2.6% | 2.3M |
| GIS | 34.62 (10:05 iex) | -3.1% | 35.74 | 34.78 / 34.50-35.15 | 1.21 (3.4%) | 32.82-37.02 | +3.5% / +5.7% | +4.1% | 8.5M |
| MNST | 42.45 (10:05 iex) | -2.8% | 43.69 | 43.83 / 42.24-43.98 | 1.41 (3.2%) | 43.51-49.50 | -5.0% / -2.7% | -6.0% | 10.7M |
| MO | 73.16 (10:05 iex) | -2.3% | 74.87 | 73.81 / 73.14-74.36 | 1.69 (2.3%) | 72.30-79.97 | -2.1% / +2.6% | -4.8% | 8.6M |
| CMCSA | 24.35 (10:05 iex) | -2.2% | 24.90 | 24.48 / 24.29-24.71 | 0.70 (2.8%) | 21.46-25.84 | +3.1% / +9.2% | -1.0% | 28.9M |
| CHTR | 126.06 (10:04 iex) | -2.1% | 128.73 | 127.52 / 125.35-129.11 | 8.12 (6.3%) | 101.11-142.60 | +4.3% / +9.0% | -7.0% | 3.0M |
| DOW | 28.49 (10:05 iex) | -1.9% | 29.03 | 29.23 / 28.39-29.27 | 1.19 (4.1%) | 28.94-34.85 | -10.5% / -4.4% | -12.1% | 8.2M |
