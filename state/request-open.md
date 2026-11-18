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

I'm placing one new trade, a LOW short at half risk, and amending the resting GLD short. The open HD short is left alone.

### 1. Tape
Lowe's (LOW) beat with tariff-refund help and is down about 5% pre-market. Gold is at a 14-month low. Index futures are up modestly on Nvidia (NVDA) but small caps are lagging, so the edge today is on the short side of rate-sensitive names: housing, small caps and gold.

- **NVDA:** Revenue was $115.8B against about $109B expected, and Q4 guidance is about $130B against about $125B. The stock is +2.9% to 159.94. Gross-margin guidance is down to 71–72%, and the 10-Q is delayed with no explanation.
- **Futures:** S&P +0.3–0.4%, Nasdaq-100 +0.8%, Dow flat, Russell 2000 −0.2%. VIX is 23.8 (−6.5%). Semis lead (SMH +2.3%).
- **Rates and the Fed:** the 10-year is flat at 5.10% and the dollar is near a 19-month high. A December hike is about 97% priced, and Waller has floated 50bp.
- **Gold:** below $3,800 for the first time since September 2025 (−2%). GLD is 346.99, under its 351.96 20-day low.
- **Regime:** a bear market driven by rate hikes. Today's tech bounce comes after a −8% to −17% month for semis, and rate-sensitive names are not joining it.

### 2. Calendar (Stockholm is ET+6 today)

| ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 06:47 | 12:47 | LOW Q3 | Adjusted EPS $3.10 vs $2.88, but it includes $0.34 of tariff refunds, so about **$2.76 without them, a miss**. Comps +1.8%. FY EPS held at $12.25. Operating-margin guidance cut to about 11.5% from 11.6%. Stock −5.2% | LOW (new), HD |
| pre | pre | TJX Q3 | Comps +4%, EPS in line. **Q4 EPS guidance $1.42–1.45 vs about $1.48–1.51 consensus.** Stock +6% | pass |
| pre | pre | TGT Q3 | EPS $2.65 incl. $0.50 of refunds; guidance raised. Stock about −1% | none |
| 07:00 | 13:00 | MBA mortgage applications | 30-year rate 7.35%, up from 7.21% | LOW, HD |
| 08:30 | 14:30 | Housing starts / permits (Oct) | Starts 1.309M vs about 1.25M expected. **Permits −7.4% to 1.295M, the lowest since Sep 2025; single-family −8.7%.** XHB −0.7%, TLT +0.3% | LOW, HD |
| 10:00 | 16:00 | Pending home sales (Oct) | Prior −7.3%; consensus not found | LOW, HD |
| 10:30 | 16:30 | EIA crude inventories | — | none |
| 13:00 | 19:00 | $16B 20-year auction | Recent 10-year at 5.020%, 30-year at 5.441% | GLD |
| 14:00 | 20:00 | FOMC minutes (Oct 27–28) | Fed held at 3.75–4.00%, vote 10–2 | all |
| after close | after close | PANW earnings; Anthropic prices its IPO (range $70–78, guided to the top or above) | ANT lists Thursday | software (pass) |

### 3. Open positions and resting entries

**HD short (session 2 of 10): hold, bracket unchanged.**
- The invalidation is a close above 347.51. It hasn't happened: HD closed at 339.01 yesterday and is 332.71 pre-market.
- LOW's refund-flattered print reinforces the thesis.

**GLD sell stop at 350.50: amend the stop to 355.50 and the target to 330.00.**
- Gold has already fallen through the trigger pre-market (346.99). The stop will fire at the open, around 347.
- On the original levels that fill would risk 12 points against 14 of reward (1.17R). At about 0.39 probability that is roughly −0.15R expected.
- The new stop sits above yesterday's 354.92 high and the broken 351.96 20-day low. If GLD gets back there, the breakdown has failed.
- At a 347 fill, the planned 8.5 points (60 shares, about $510 at risk) and a 2R target are restored. This is a resting entry, so amending it is within policy.
- The original cancel condition (a trade above 362) stays.

### 4. New plays

| Field | Value |
|---|---|
| Ticker | LOW |
| Direction | Short |
| Catalyst | Lowe's Q3, 2026-11-18 06:47 ET (CNBC, Newsquawk, Startup Fortune). Without the $0.34 tariff refund, EPS of about $2.76 misses $2.88–2.89 and is below last year. FY EPS guidance unchanged despite the refund; operating-margin guidance cut. Zelman downgraded it to Underperform days earlier. Same morning: permits at a 14-month low and mortgage rates at 7.35% |
| Thesis | Same setup as the HD short that is working: LOW ran +10% above its 50-day average into a print whose underlying earnings missed. Rates are rising and housing is weakening. Short a bounce into the gap and target the 20-day low. |
| Entry | Sell limit 212.50. LOW is 209.00 pre-market; 212.50 is a retest of about 30% of the gap and sits inside today's pre-market range |
| Stop | 221.50: above the 220.46 pre-earnings close. If the gap fully fills, the market has rejected the miss. That is 1.23 ATR |
| Target | 194.50, just above the 194.43 20-day low. **2.0R** |
| Risk tier | 0.5%: it adds to the same housing/rates factor as HD, and it is a short against an uptrend |
| Time horizon | 3–10 sessions |
| Next earnings | About 2027-02-24. That is inferred from the Feb 25, 2026 pattern, not confirmed. Not an event trade |
| Conviction | 3 |
| P(target first) | **0.37.** Starting from the 39% base rate, I took a little off because the target is 2.5 ATR away. The underlying miss plus a negative reaction (a drift setup) roughly offsets the risk that a gap-down on a headline beat gets bought, with Thanksgiving seasonality ahead. EV = 0.37 × 2 − 0.63 = +0.11R |
| Invalidation | LOW closes above 220.46 (gap fully filled) before the stop |
| What I'd be wrong about | It is a headline beat-and-raise on sales: comps +1.8% against about 0.4% expected, online +17%. Gaps down on beats in a market already −3% this month often reverse, and the trade doubles up on HD's factor |

The sector check: Consumer Discretionary would be about −28% net (HD −16%, LOW about −12%) against the 40% cap.

### 5. Both sides

- **Best short: LOW**, taken as above (212.50 / 221.50 / 194.50, P 0.37).
- **Best long: NVDA, passed.** Market about 159.94, stop 147.50 (under the 148.80 20-day low), target 185.00 (2.0R), P 0.33, EV about −0.01R. The beat-and-raise is real. Against it: the 10-Q is delayed with no explanation (due by Dec 4), the board is split on CEO succession, margin guidance is down, and it would be a counter-trend entry. Conviction 2.

### 6. Passing on

- **TJX long** (limit 136.00 / stop 131.50 / target 145.00, P 0.35): already +6% (1.9 ATR) on in-line EPS, with Q4 and full-year EPS guidance below consensus. It looks like positioning relief. Conviction 2.
- **IWM breakdown short** (sell stop 267.40 / stop 274.00 / target 257.50, P 0.38, EV about −0.05R): the regime fits, but I just took target on this, and the stop is based on ATR because I couldn't verify yesterday's high.
- **CRM short** (sell stop 189.50 / stop 199.50 / target 172.00, P 0.33): after −9.5% yesterday, the Anthropic supply overhang ends when ANT lists Thursday. Earnings on Dec 2 (confirmed by Salesforce IR) fall inside the horizon.
- **TTWO / ROST / XHB:**
  - TTWO is a GTA VI launch "sell-the-news" coin flip.
  - ROST's sympathy move: I didn't verify its earnings date.
  - XHB: LOW is the cleaner expression.

### 7. For the post-open review

- **LOW:** if it is unfilled and below its opening range, leave the limit; don't chase. If it filled and is above 218, take no action; the stop covers it.
- **GLD:** record the fill price. If it filled below 344, the risk is still within the 0.5–0.7% range; take no action.
- **Pending home sales at 10:00:** informational only.

### 8. Book state

- **Exposure:** gross about 48% of the 150% cap; net about −48% of ±100% once LOW fills.
- **Risk at stake:** about 1.5% of the 4% cap (HD $506, GLD about $510 at a 347 fill, LOW about $517), with 3 of 8 slots used.

```json
{
  "date": "2026-11-18",
  "no_trade": false,
  "session_note": "Rate-hike regime (Dec hike ~97% priced, 10y 5.10%, gold 14-month low) with an NVDA-led tech relief bounce; shorting the rate-sensitive laggards: LOW on a refund-flattered underlying miss, GLD through its 20d low (bracket re-set for the gap).",
  "plays": [
    {
      "ticker": "LOW",
      "direction": "short",
      "entry_type": "limit",
      "entry": 212.50,
      "stop": 221.50,
      "targets": [194.50],
      "time_horizon": "3-10 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.37,
      "earnings_date": "2027-02-24",
      "event_trade": false,
      "catalyst": "LOW Q3 2026-11-18 06:47 ET: adj EPS $3.10 includes $0.34 tariff refund (~$2.76 ex-refund vs $2.88-2.89 consensus), FY EPS held at $12.25, op margin guide cut to ~11.5%; Zelman Underperform days earlier; Oct permits -7.4% to 14-month low, MBA 30y 7.35%.",
      "thesis": "LOW ran +10% above its 50d into a print whose underlying EPS missed, with housing weakening and the Fed hiking. Short a retest of the gap, mirroring the working HD short, toward the 20d low.",
      "invalidation": "LOW closes above 220.46 (pre-earnings close, gap fully filled) on any session before the stop.",
      "bear_case": "Headline beat with comps +1.8% vs ~0.4% and raised sales guide; gap-downs on beats in an oversold tape often reverse, and this doubles HD's housing/rates factor."
    }
  ],
  "manage": [
    {
      "ticker": "GLD",
      "action": "update",
      "stop": 355.50,
      "target": 330.00,
      "reason": "Resting entry, not yet filled: GLD is 346.99 pre-market, through the 350.50 trigger, so it fills near 347; re-set to stop above the Nov 17 354.92 high and broken 351.96 20d low, keeping the planned ~8.5-pt risk and a 2R target from the expected fill."
    }
  ],
  "passed": [
    {
      "ticker": "NVDA",
      "direction": "long",
      "entry_type": "market",
      "entry": 159.94,
      "stop": 147.50,
      "targets": [185.00],
      "p_target_first": 0.33,
      "reason": "Beat-and-raise verified (rev $115.8B vs ~$109B, Q4 guide ~$130B vs ~$125B), but the 10-Q is delayed with no explanation, the board is split on the CEO search, GM guide is lower, and it is counter-trend. Conviction 2."
    },
    {
      "ticker": "TJX",
      "direction": "long",
      "entry_type": "limit",
      "entry": 136.00,
      "stop": 131.50,
      "targets": [145.00],
      "p_target_first": 0.35,
      "reason": "+6% (1.9 ATR) on in-line EPS with Q4 and FY EPS guides below consensus; the move looks like positioning relief. Conviction 2."
    },
    {
      "ticker": "IWM",
      "direction": "short",
      "entry_type": "stop",
      "entry": 267.40,
      "stop": 274.00,
      "targets": [257.50],
      "p_target_first": 0.38,
      "reason": "Breakdown under the 267.87 20d low fits the hike regime, but I just took target on it, the stop is ATR-based (the Nov 17 high is unverified), and EV is about -0.05R."
    },
    {
      "ticker": "CRM",
      "direction": "short",
      "entry_type": "stop",
      "entry": 189.50,
      "stop": 199.50,
      "targets": [172.00],
      "p_target_first": 0.33,
      "reason": "Anthropic supply overhang ends when ANT lists Thursday; already -9.5% Nov 17; earnings Dec 2 (Salesforce IR) inside the horizon."
    }
  ]
}
```

Sources:
- [Yahoo Finance live, Nov 18](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-november-18-dow-sp-500-nasdaq-nvidia-anthropic-ipo-090613569.html)
- [CNBC premarket movers, Nov 18](https://www.cnbc.com/2026/11/18/stocks-moving-the-most-today-live-updates.html)
- [CNBC: Lowe's Q3](https://cnbc.com/2026/11/18/lowes-low-q3-2026-earnings.html)
- [Startup Fortune: Lowe's tariff refund](https://startupfortune.com/lowes-beats-third-quarter-estimates-but-shares-fall-as-tariff-refund-flatters-the-profit/)
- [Newsquawk premarket movers](https://www.newsquawk.com/headlines/us-premarket-movers-nvda-tjx-low-fcx-ttwo-tgt-fix-aaoi-dlb)
- [TradingKey US pre-market](https://www.tradingkey.com/analysis/stocks/us-stocks/262311015-us-pre-market-nvda-anthropic-tradingkey)
- [CNBC: Nvidia Q3 FY27](https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html)
- [Yahoo: Nvidia delayed 10-Q](https://finance.yahoo.com/markets/stocks/articles/nvidia-delayed-10-q-draws-040618822.html)
- [mlq.ai: Gold below $3,800](https://mlq.ai/news/gold-falls-below-3800-to-its-lowest-since-september-2025-as-traders-price-a-december-fed-hike-before-the-minutes/)
- [ActionForex: Gold one-year low](https://www.actionforex.com/action-insight/market-overview/661273-gold-hits-one-year-low-ahead-of-fomc-minutes-as-fed-rate-path-takes-center-stage/)
- [mlq.ai: Housing starts October](https://mlq.ai/news/us-housing-starts-rebound-nearly-10-in-october-as-building-permits-fall-to-their-lowest-in-more-than-a-year/)
- [Census new residential construction](https://www.census.gov/construction/nrc/pdf/newresconst_202610.pdf)
- [Investing.com: TJX](https://au.investing.com/news/stock-market-news/tjx-stock-surges-on-revenue-beat-strong-guidance-93CH-4780325)
- [MarketBeat: TJX Q4 guidance](https://www.marketbeat.com/instant-alerts/guidance-tjx-companies-nyse-tjx-announces-q4-2027-earnings-guidance-2026-11-18/)
- [Kitco: Waller/Logan](https://www.kitco.com/news/article/2026-11-10/feds-waller-and-logan-signal-readiness-hike-higher-and-faster-50-bps-table)
- [CNBC: Anthropic IPO price](https://www.cnbc.com/2026/11/17/anthropic-ipo-price.html)
- [Salesforce IR: Q3 FY27 date](https://investor.salesforce.com/news/news-details/2026/Salesforce-Announces-Date-of-Third-Quarter-Fiscal-2027-Earnings-Release-and-Webcast/default.aspx)
- [Treasury 20-year announcement](https://fiscaldata.treasury.gov/static-data/published-reports/auctions-query/announcements/A_20261112_5.pdf)
- [Yahoo: LOW next earnings pattern](https://finance.yahoo.com/news/heres-expect-lowes-next-earnings-133928550.html)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Wednesday 2026-11-18. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,920.32**
- Cash: $153,301.93
- Session P&L so far: -0.05% (new entries are blocked at -3.0%)
- Gross exposure: $50,382 (49% of equity, cap 150%)
- Net exposure: $-50,382 (-49%, cap +/-100%)
- Risk at stake (entry to stop): $1,419 (1.38% of equity, cap 4.0%) — 2.62% left for new plays
- Slots: 3 open + 0 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 345.91 | 344.73 | +71 (+0.3%) | -20% | 355.50 | 330.00 |
| HD | short | 51 | 343.57 | 336.97 | +337 (+1.9%) | -17% | 353.50 | 323.50 |
| LOW | short | 57 | 215.58 | 219.52 | -225 (-1.8%) | -12% | 221.50 | 194.50 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **GLD**, opened 2026-11-18 (session 1 of at most 10), submitted with stop 359 and target 333, P 36%. Thesis: Gold is trending down on rising real rates and the strongest dollar in 18 months (-4.6% in 5 days, below its 20d and 50d averages). A US-session break below the overnight low (GLD 350.50, under its 352.91 20-day low) confirms the move toward the $3,800 and then ~$3,650 area. The stop entry stays unfilled if Warsh or the minutes turn dovish. Invalidation: DXY back below 102.50 with market-implied December-hike odds below 70%.
- **HD**, opened 2026-11-17 (session 2 of at most 10), submitted with stop 353.5 and target 323.5, P 36%. Thesis: HD ran ~19.5% into the print on flat estimates at ~22x forward; the print gave no reason to pay more and the gap broke the 344.31 channel support with 10y yields at 5.1% and the Fed talking hikes. Short a failed retest of broken support toward the 330/316 supports. Invalidation: HD closes above 347.51 (pre-earnings close, gap fully filled) on any session before the stop, e.g. after a strong LOW print on Nov 18.
- **LOW**, opened 2026-11-18 (session 1 of at most 10), submitted with stop 221.5 and target 194.5, P 37%. Thesis: LOW ran +10% above its 50d into a print whose underlying EPS missed, with housing weakening and the Fed hiking. Short a retest of the gap, mirroring the working HD short, toward the 20d low. Invalidation: LOW closes above 220.46 (pre-earnings close, gap fully filled) on any session before the stop.

### Your record

50 closed trades: 16W / 34L, total +1.03R, net $+2,753 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 50 | 18 | 29 | +0.02R |
| The same trades, bracket left alone | 50 | | | +0.04R |
| Ideas you passed on, or the caps dropped | 103 | 37 | 56 | +0.04R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 41 | 49% |
| 35%-40% | 67 | 30% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 39% of 140 brackets reached target first. Your Brier score is 0.241; saying 39% every time scores 0.239. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

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

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GLD | 344.70 (10:05 iex) | -2.2% | 352.48 | 346.31 / 344.51-346.31 | 7.55 (2.1%) | 351.96-380.18 | -3.7% / -7.0% | -4.6% | 9.7M |
| HD | 336.94 (10:05 iex) | -0.6% | 339.01 | 331.25 / 330.31-338.16 | 10.50 (3.1%) | 311.14-362.44 | +0.6% / +8.2% | -3.4% | 4.7M |
| LOW | 218.90 (10:05 iex) | -0.7% | 220.46 | 212.07 / 211.00-219.90 | 7.33 (3.3%) | 194.43-235.00 | +2.1% / +10.3% | -4.9% | 3.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 732.63 (10:05 iex) | +0.0% | 732.44 | 733.35 / 728.72-735.06 | 14.14 (1.9%) | 727.00-775.64 | -3.1% / -4.0% | -2.3% | 50.4M |
| QQQ | 659.83 (10:05 iex) | +0.4% | 656.95 | 661.02 / 654.00-662.65 | 20.01 (3.0%) | 646.64-727.95 | -4.7% / -8.2% | -2.6% | 51.2M |
| IWM | 270.69 (10:05 iex) | +0.6% | 269.05 | 268.15 / 267.89-271.60 | 5.81 (2.2%) | 267.87-286.17 | -3.3% / -3.8% | -4.1% | 23.9M |
| DIA | 503.70 (10:03 iex) | -0.7% | 507.31 | 505.45 / 501.99-506.22 | 8.57 (1.7%) | 505.29-536.60 | -2.6% / -2.1% | -2.8% | 3.7M |
| TLT | 79.93 (10:05 iex) | +0.5% | 79.55 | 79.91 / 79.82-80.16 | 0.74 (0.9%) | 79.11-82.42 | -1.7% / -0.2% | -1.6% | 36.1M |
| GLD | 344.70 (10:05 iex) | -2.2% | 352.48 | 346.31 / 344.51-346.31 | 7.55 (2.1%) | 351.96-380.18 | -3.7% / -7.0% | -4.6% | 9.7M |
| USO | 138.35 (10:03 iex) | -1.3% | 140.24 | 139.74 / 137.69-139.81 | 5.73 (4.1%) | 138.36-171.82 | -8.9% / -8.1% | -0.9% | 5.1M |
| SMH | 461.49 (10:05 iex) | +0.3% | 460.10 | 467.98 / 453.98-469.50 | 28.38 (6.2%) | 445.32-571.00 | -9.7% / -17.2% | -4.9% | 12.1M |
| XLK | 163.93 (10:04 iex) | +0.4% | 163.26 | 164.87 / 161.96-165.39 | 6.70 (4.1%) | 159.63-191.55 | -7.5% / -12.3% | -3.3% | 13.1M |
| XLF | 56.59 (10:05 iex) | -0.8% | 57.07 | 56.78 / 56.56-57.01 | 1.09 (1.9%) | 55.64-60.04 | -0.4% / +2.0% | -2.1% | 35.1M |
| XLE | 62.29 (10:05 iex) | -1.7% | 63.36 | 63.00 / 61.64-63.28 | 1.75 (2.8%) | 60.43-70.15 | -3.6% / -2.4% | +1.8% | 35.7M |
| XLV | 183.83 (10:04 iex) | -0.8% | 185.24 | 183.73 / 183.23-185.28 | 3.77 (2.0%) | 177.07-192.32 | +0.4% / +5.5% | -1.9% | 11.5M |
| XLI | 164.93 (10:05 iex) | +0.1% | 164.75 | 164.59 / 163.77-165.65 | 3.62 (2.2%) | 161.74-172.40 | -1.7% / -2.2% | -2.4% | 8.8M |
| XLY | 118.82 (10:04 iex) | +1.5% | 117.10 | 117.24 / 117.20-119.16 | 2.70 (2.3%) | 112.83-122.92 | -0.4% / +2.8% | -3.3% | 9.2M |
| XLP | 91.36 (10:05 iex) | -0.1% | 91.46 | 90.82 / 90.59-91.59 | 1.69 (1.9%) | 86.36-93.48 | +1.7% / +6.5% | +0.5% | 19.4M |
| XLU | 43.49 (10:05 iex) | +0.2% | 43.42 | 43.20 / 43.19-43.61 | 0.62 (1.4%) | 41.87-44.40 | +0.3% / +3.7% | -0.7% | 25.0M |
| XLB | 50.49 (10:05 iex) | -0.7% | 50.84 | 50.28 / 50.12-50.62 | 1.10 (2.2%) | 50.76-54.63 | -2.7% / -0.0% | -3.8% | 12.2M |
| XLRE | 43.52 (10:04 iex) | -0.2% | 43.59 | 43.28 / 43.25-43.60 | 0.70 (1.6%) | 41.78-45.34 | -0.0% / +2.5% | -2.2% | 7.9M |
| XLC | 105.76 (10:05 iex) | +0.5% | 105.26 | 105.68 / 105.27-106.15 | 2.33 (2.2%) | 99.33-109.88 | +0.2% / -3.5% | -2.3% | 8.1M |
| KRE | 70.74 (10:05 iex) | -0.2% | 70.85 | 70.74 / 70.66-71.20 | 1.57 (2.2%) | 70.15-75.80 | -2.3% / -0.9% | -3.1% | 14.4M |
| XHB | 99.96 (10:05 iex) | +0.9% | 99.09 | 98.20 / 98.00-100.28 | 3.30 (3.3%) | 94.81-108.78 | -2.2% / +0.8% | -4.0% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 354.93 (10:05 iex) | +0.9% | 351.91 | 352.05 / 351.87-356.32 | 9.62 (2.7%) | 325.08-360.83 | +1.4% / +3.5% | +1.1% | 48.2M |
| MSFT | 505.81 (10:05 iex) | -0.1% | 506.24 | 505.49 / 501.86-508.50 | 18.80 (3.7%) | 496.51-559.15 | -4.0% / -2.6% | -5.0% | 27.7M |
| NVDA | 154.96 (10:05 iex) | -0.3% | 155.46 | 159.15 / 153.27-159.70 | 11.49 (7.4%) | 148.80-222.19 | -19.3% / -26.6% | -8.0% | 237.8M |
| AMZN | 263.49 (10:05 iex) | +2.2% | 257.89 | 259.68 / 259.51-264.32 | 11.21 (4.3%) | 229.36-275.34 | +0.4% / +1.2% | -4.8% | 49.9M |
| GOOGL | 283.28 (10:05 iex) | +1.1% | 280.20 | 282.98 / 281.41-284.97 | 12.31 (4.4%) | 276.92-337.27 | -5.8% / -14.0% | -2.5% | 42.4M |
| META | 617.35 (10:05 iex) | -0.2% | 618.87 | 620.56 / 613.79-620.81 | 21.58 (3.5%) | 583.80-713.22 | -1.7% / -9.0% | -3.5% | 23.4M |
| TSLA | 384.61 (10:05 iex) | +1.2% | 380.11 | 385.24 / 379.35-389.27 | 17.65 (4.6%) | 338.15-414.23 | -1.6% / +1.2% | +0.1% | 38.8M |
| AVGO | 349.06 (10:05 iex) | +2.2% | 341.60 | 349.04 / 340.74-351.89 | 20.71 (6.1%) | 289.77-369.82 | +3.1% / -0.8% | +2.9% | 27.9M |
| AMD | 513.16 (10:05 iex) | +1.9% | 503.41 | 510.44 / 495.20-519.80 | 48.80 (9.7%) | 402.10-594.00 | -2.4% / -9.3% | -2.3% | 36.7M |
| ORCL | 115.60 (10:05 iex) | +0.5% | 115.00 | 116.30 / 113.62-117.44 | 8.64 (7.5%) | 109.21-148.48 | -8.2% / -14.6% | -2.5% | 41.7M |
| NFLX | 59.69 (10:05 iex) | +0.0% | 59.68 | 59.70 / 59.66-60.39 | 1.86 (3.1%) | 59.41-67.82 | -5.9% / -12.9% | -5.7% | 44.3M |
| CRM | 187.85 (10:04 iex) | -3.4% | 194.52 | 193.07 / 186.84-193.50 | 9.13 (4.7%) | 193.41-252.42 | -14.2% / -16.6% | -8.9% | 7.0M |
| JPM | 327.75 (10:05 iex) | -0.7% | 329.96 | 327.52 / 326.79-330.09 | 8.50 (2.6%) | 328.74-359.80 | -2.7% / -2.6% | -3.5% | 6.6M |
| GS | 875.07 (10:04 iex) | -0.3% | 877.52 | 880.00 / 867.29-880.00 | 30.50 (3.5%) | 854.45-939.38 | -2.6% / -4.2% | -3.6% | 2.1M |
| BAC | 49.14 (10:05 iex) | -0.6% | 49.44 | 49.20 / 49.05-49.48 | 1.26 (2.5%) | 49.08-53.02 | -2.0% / -7.7% | -2.4% | 34.2M |
| XOM | 164.49 (10:05 iex) | -1.6% | 167.21 | 165.92 / 162.45-166.96 | 4.63 (2.8%) | 159.11-187.32 | -3.5% / -0.8% | +2.3% | 14.3M |
| CVX | 209.48 (10:05 iex) | -2.3% | 214.35 | 212.60 / 207.25-213.58 | 5.24 (2.4%) | 204.31-234.53 | -2.7% / +0.2% | +2.3% | 8.2M |
| LLY | 1,402.97 (10:04 iex) | -0.9% | 1,415.55 | 1,407.93 / 1,399.14-1,423.11 | 51.93 (3.7%) | 1,256.10-1,475.25 | +3.2% / +13.1% | -1.0% | 3.1M |
| UNH | 372.92 (10:05 iex) | -4.3% | 389.68 | 387.14 / 371.99-387.53 | 11.96 (3.1%) | 387.14-426.55 | -4.1% / -0.4% | -3.8% | 5.0M |
| JNJ | 276.64 (10:04 iex) | -0.7% | 278.70 | 275.55 / 275.55-278.72 | 7.14 (2.6%) | 254.56-290.25 | +1.7% / +4.3% | -0.7% | 7.5M |
| WMT | 127.07 (10:05 iex) | -0.4% | 127.52 | 126.51 / 125.07-127.08 | 3.10 (2.4%) | 116.63-131.82 | +2.7% / +10.5% | +1.6% | 21.8M |
| COST | 1,106.23 (10:04 iex) | -0.3% | 1,110.08 | 1,104.00 / 1,097.50-1,110.45 | 21.62 (1.9%) | 978.87-1,123.67 | +6.4% / +14.0% | +4.1% | 2.5M |
| HD | 336.94 (10:05 iex) | -0.6% | 339.01 | 331.25 / 330.31-338.16 | 10.50 (3.1%) | 311.14-362.44 | +0.6% / +8.2% | -3.4% | 4.7M |
| CAT | 561.74 (10:04 iex) | -1.6% | 570.79 | 576.25 / 552.75-578.00 | 31.72 (5.6%) | 550.81-743.23 | -9.3% / -21.8% | -2.4% | 3.9M |
| BA | 163.06 (10:04 iex) | -0.5% | 163.91 | 163.43 / 161.90-163.69 | 5.07 (3.1%) | 163.30-193.28 | -6.3% / -12.3% | -5.5% | 10.5M |
| DAL | 85.56 (10:04 iex) | +1.5% | 84.30 | 84.37 / 84.29-86.20 | 3.25 (3.9%) | 75.33-92.52 | +0.1% / +2.8% | -8.6% | 6.2M |
| UAL | 108.72 (10:04 iex) | +2.2% | 106.35 | 106.01 / 106.01-109.55 | 5.53 (5.2%) | 96.24-122.08 | -2.1% / -1.6% | -11.8% | 5.7M |

#### Today's biggest movers among 269 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| TJX | 142.73 (10:05 iex) | +9.9% | 129.85 | 137.01 / 134.05-143.07 | 4.07 (3.1%) | 129.39-147.17 | -6.4% / -4.3% | -4.8% | 6.4M |
| TTWO | 217.01 (10:05 iex) | +6.4% | 203.93 | 212.57 / 210.50-221.00 | 12.03 (5.9%) | 183.86-237.41 | -2.0% / -1.8% | -9.2% | 3.8M |
| LYFT | 17.76 (10:05 iex) | +6.3% | 16.71 | 16.68 / 16.65-17.91 | 0.88 (5.3%) | 15.81-18.84 | -1.4% / +3.3% | -1.8% | 11.5M |
| TGT | 169.55 (10:05 iex) | +6.3% | 159.53 | 160.99 / 159.95-169.78 | 5.44 (3.4%) | 144.30-166.43 | +2.1% / +2.7% | -1.4% | 3.9M |
| RBLX | 46.44 (10:05 iex) | +5.5% | 44.00 | 43.67 / 43.43-46.99 | 3.69 (8.4%) | 41.36-56.08 | -11.9% / -8.9% | -14.0% | 10.0M |
| PANW | 324.12 (10:05 iex) | +4.8% | 309.29 | 313.75 / 311.63-325.88 | 19.76 (6.4%) | 301.28-406.88 | -11.1% / -15.6% | -5.2% | 6.3M |
| OKTA | 180.98 (10:05 iex) | +3.7% | 174.54 | 177.92 / 174.52-181.93 | 14.69 (8.4%) | 164.18-228.72 | -10.1% / -12.0% | -2.1% | 4.9M |
| ROST | 228.27 (10:03 iex) | +3.5% | 220.45 | 226.68 / 221.13-228.80 | 8.24 (3.7%) | 219.06-249.30 | -5.3% / -4.7% | -7.7% | 2.1M |
| FCX | 51.49 (10:05 iex) | -6.9% | 55.30 | 52.18 / 50.48-52.63 | 3.10 (5.6%) | 54.73-68.94 | -11.1% / -18.2% | -8.3% | 12.8M |
| NEM | 105.04 (10:05 iex) | -5.6% | 111.26 | 106.80 / 104.72-107.60 | 5.09 (4.6%) | 104.51-127.28 | -2.5% / -5.2% | -7.3% | 7.1M |
| VLO | 348.36 (10:05 iex) | -4.2% | 363.77 | 360.57 / 344.18-361.83 | 17.33 (4.8%) | 341.51-440.94 | -5.0% / -9.0% | +3.7% | 3.2M |
| HUM | 425.10 (10:04 iex) | -4.1% | 443.34 | 441.44 / 415.84-443.52 | 19.09 (4.3%) | 399.35-462.87 | +3.9% / +8.1% | +1.2% | 1.6M |
| CNC | 69.75 (10:04 iex) | -3.9% | 72.55 | 71.45 / 68.90-72.41 | 3.60 (5.0%) | 64.85-78.08 | +3.3% / +7.7% | +3.4% | 6.2M |
| AA | 35.88 (10:05 iex) | -3.7% | 37.27 | 36.54 / 35.56-36.62 | 1.66 (4.5%) | 37.11-42.14 | -5.9% / -11.2% | -6.8% | 4.5M |
| OXY | 54.54 (10:05 iex) | -3.5% | 56.52 | 55.80 / 54.42-56.30 | 1.89 (3.3%) | 53.86-64.95 | -5.7% / -5.2% | -0.7% | 10.7M |
| TMUS | 162.02 (10:03 iex) | -3.5% | 167.90 | 166.52 / 161.84-167.01 | 6.09 (3.6%) | 143.75-175.00 | +5.3% / +3.0% | -0.7% | 6.3M |
