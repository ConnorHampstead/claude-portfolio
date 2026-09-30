Produce the post-open review.

The cash session has been open for about 35 minutes. This morning's pre-market
brief is below, followed by the live book and market data, which now include
today's opening prices. This is the second and last decision point of the day:
after this review, nothing looks at the book until tomorrow's pre-market brief.

What this session is for:

- **Fills at the open.** Check every entry that filled since the morning. An
  entry that filled on a gap through its limit sits closer to its stop than
  planned and may no longer be the trade you meant. Keep it, tighten it, or close
  it, through `manage`.
- **The morning's plans for this review.** The 08:30 and 10:00 ET data have
  printed and the opening range is set. For each thing the morning brief said it
  would decide after the open or after the data, decide now: act, or say why not.
- **Resting entries** the open has made stale: amend or cancel them.
- **New plays**, under the same rules as the morning. Orders now go into a
  trading market: a limit at or through the last price fills immediately, and a
  `market` entry is sized from the last price.

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
Each one: keep, tighten, amend, or close, and why.

### 3. The morning's plans
Each plan the morning left for this review: acted on, not triggered, or dropped.
One line each.

### 4. New plays
The same table as the pre-market brief.

### 5. Passing on
One line each. Ideas with real levels also go in the `passed` array, where they
are scored.

Then the JSON block, in the same schema as the morning.

Your probability estimates are scored against outcomes. Spread them according to
what you actually believe rather than clustering everything near 60%.

## This morning's pre-market brief

# Pre-market brief — Wednesday 2026-09-30 (written 09:05 ET / 15:05 Stockholm)

## 1. Tape
The 08:30 data came in soft on inflation and firm on activity. August core PCE was 3.0% y/y against 3.3% expected (+0.2% m/m), and headline was 3.4% against 3.7%. Real spending rose 0.6% m/m, the biggest gain since March 2025. ADP private payrolls were +90k against 70k expected (all verified: BEA coverage via FXStreet, Bloomberg and CNBC). Bonds took it mildly: the 10-year is about 5.23%, down roughly 2bp from Tuesday's 19-year highs near 5.25–5.27%, and the 30-year printed a 2002 high Tuesday. Futures are only modestly firmer, with SPY 766.74 (+0.3%) and QQQ 741.39 (+0.5%). The regime is still a rates-driven grind: the 10-year above 5%, a Fed that has been hiking, and oil elevated (USO +1.8%). Today's inflation miss is the first real relief for that regime in weeks, so I think longs have a slight edge today. The 5-day trend still favours shorts in rate-sensitives, which is where my book already sits (net −34%).

## 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Aug PCE / core PCE | **Actual** headline 3.4% y/y (exp 3.7%), core 3.0% (exp 3.3%), core +0.2% m/m. Soft. 10-year −2bp, futures +0.2–0.3% | HD, XLU, BAC shorts (negative for them at the margin) |
| 08:30 | 14:30 | Aug personal spending | **Actual** real +0.6% m/m, strongest since Mar-2025 | Consumer / HD |
| 08:15 | 14:15 | ADP September | **Actual** +90k vs 70k exp (prior 38k) | Broad |
| 08:30 | 14:30 | Q2 GDP final | Released; I could not verify the figure | — |
| 09:45 | 15:45 | Chicago PMI Sep | Consensus 51.2 (prior 47.1) | CAT, DAL |
| 10:30 | 16:30 | EIA crude inventories | — | DAL (fuel) |
| Intraday | — | Several Fed speakers; Williams has already pushed back on back-to-back hike pricing | — | All |
| After close (~16:05) | ~22:05 | **Micron FQ4 earnings**. Implied move ~7–8% | NVDA resting buy stop (sympathy) |

## 3. Open positions and resting entries
- **BA short** (entry 187.31, last 192.39, stop 194.90, target 176): **thesis invalidated → CLOSE at market.** The short rested on the MAX 10 certification delay and a broken 20-day floor. Overnight the Pentagon picked Boeing over Northrop for the F/A-XX sixth-generation strike fighter, a contract worth more than $20B (verified: CNBC, Investing.com). That is a material fundamental positive, and the stock is +2.5% pre-market, 2.5 points from my stop. I'm not going to sit through a gap-driven squeeze toward the stop on a thesis a major contract win has now contradicted. I accept roughly −0.67R now rather than a likely −1R. This is a thesis exit, not a stop-out, and the log should record it that way.
- **BAC short** (55.80, last 55.02, stop 57.70, target 52.90): **intact.** It sits on the 20-day low of 54.73. Soft PCE is a mild headwind, but the rates regime has not reversed on a 2bp move. Hold with no change.
- **HD short** (289.30, last 290.00, stop 297.60, target 278): **intact but vulnerable today.** Strong real spending plus softer inflation is the worst combination for this short. The stop is 1.2 ATR above; hold. See the review note.
- **XLU resting sell stop 38.95** (stop 40.15, target 37.55): **keep.** Pre-market is 39.80, so the trigger is 0.85 away and needs a renewed yield push to fire. That is exactly the condition it is meant to capture.
- **DAL resting buy stop 85.80** (stop 82.40, target 90.50): **keep.** Pre-market is 85.10, against a 20-day high of 85.47. USO +1.8% is a mild headwind, and the review note from yesterday still stands.
- **NVDA resting buy stop 234.70** (stop 227.40, target 246): **keep.** Pre-market is 228.64. MU reports after the close, so a fill today would carry the MU sympathy risk overnight. The stop is 1.4 ATR and the tier was already set with that in mind.
- **ORCL resting sell stop 130.90** (stop 138.60, target 119): **keep.** Pre-market is 136.58, well above the trigger.

## 4. New plays

### CAT long (breakout on soft-PCE / activity rebound)
| Field | Value |
|---|---|
| Ticker | CAT |
| Direction | Long |
| Catalyst | Soft core PCE (3.0% vs 3.3%) plus strong real spending (+0.6%) on 9/30, and Chicago PMI at 09:45 is expected to jump to 51.2 from 47.1. CAT is pre-market 833.00 (IEX, +0.8%), above its 20-day high of 830.50 |
| Thesis | CAT is the strongest large-cap industrial on the table: +2.6% vs its 20-day average and +2.3% over 5 days while XLI is −0.7%. A soft-inflation / strong-activity print is the best macro mix for cyclical capex. A push through the pre-market high confirms a range breakout toward the mid-800s. The stock is still ~20% under its June ATH (verified: Fool/Yahoo), so there is no overhead ATH supply nearby. |
| Entry | Buy stop 840.00, above the pre-market 833 and the 20-day high 830.50 |
| Stop | 812.00: under Tuesday's ~815.5 low (single-source, stock-page data) and back inside the old range. 1.35 ATR from entry |
| Target | 885.00 (+1.6R) |
| Risk tier | 0.5. It is a breakout into a 5%+ 10-year regime, and CAT carries a ~2.5% ATR |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 40% |
| Invalidation | The 10-year back above 5.27% (a new high) within the horizon, or CAT back under 825 after triggering |
| What I'd be wrong about | Soft PCE doesn't change the Fed path if spending is this strong. Hot spending can push yields higher, and cyclicals then get sold again. Breakouts in this tape (ANET, ROST) have failed. |

The trigger sits above the pre-market print so the broker accepts it. At 840 the entry sits ~1% over the pre-market price, which avoids buying the first uptick on a thin print.

## 5. Both sides
- **Best long:** the CAT buy stop at 840, stop 812, target 885, P = 40%. Taken (section 4).
- **Best short:** TSLA breakdown below the 20-day low of 349.92. Sell stop 347.50, stop 362.00, target 325.00, P = 38%. **Passed.** Q3 deliveries are expected around Oct 2, which is the company's own scheduled figure and effectively a binary under rule 8. The slot and risk room also go to CAT and the existing shorts. I also looked at NOC after it lost F/A-XX (−3.5% pre-market), but it isn't in my data table and I couldn't verify a level, so it is excluded. MRNA's Citi downgrade to Sell (−6%) was excluded for the same reason (unverified price).

## 6. Passing on
- **TSLA short** 347.50 / 362 / 325, P 38%: deliveries binary inside the horizon; see above.
- **XHB long** (soft PCE, housing relief), buy stop 99.50 / stop 95.80 / target 104.50, P 35%: it would directly hedge my HD short against its own thesis, and a 2bp yield move isn't a regime change.
- **NOC short**, **MRNA short**: no verified price. Excluded.

## 7. For the post-open review
- **BA:** closed at market in this brief. If for any reason the close did not execute, close it.
- **HD:** if the 10-year is at or below 5.18% by 10:05 and HD trades ≥ 295, close it; the soft-inflation / strong-spending mix is running against it. Otherwise hold.
- **Chicago PMI (09:45):** a print ≥ 53 supports CAT; keep the buy stop. A print ≤ 47 (another contraction) means cancel the CAT entry if it has not filled.
- **XLU:** if the 10-year is down ≥ 6bp by 10:00 and XLU is above 40.0, cancel the XLU entry.
- **NVDA:** if it fills before 10:05, leave the stop at 227.40 into MU.

## 8. Book state
BA closes, which frees about 0.25% of risk and one slot. With CAT added at 0.5% and all resting entries filled, total risk at stake is ~3.5% of the 4.0% cap, with 7 of 8 slots. Gross is roughly 91% − 6% (BA) + 18% (CAT ≈ $18k at 0.5% on a 28-point stop) ≈ 103% of the 150% cap. Net is about −34% + 6% + 18% ≈ −10%, within ±100%. Industrials net about +18%, within the 40% cap.

Sources: [CNBC premarket movers](https://www.cnbc.com/2026/09/30/stocks-making-the-biggest-moves-premarket-hood-ba-mrna-.html), [FXStreet PCE](https://www.fxstreet.com/news/us-core-pce-inflation-set-to-rise-in-august-pressuring-the-federal-reserve-202609300830), [Bloomberg PCE](https://www.bloomberg.com/news/articles/2026-09-30/us-consumer-spending-rises-by-most-in-a-year-core-pce-up-0-2), [CNBC ADP](https://www.cnbc.com/2026/09/30/private-sector-jobs-rose-by-90000-in-september-better-than-expected-adp-reports.html), [CNBC BA F/A-XX](https://www.cnbc.com/2026/09/29/boeing-fighter-contract-pentagon.html), [CNBC 30y yield](https://www.cnbc.com/2026/09/29/treasury-yields-bonds.html), [Yahoo futures](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-30-dow-sp-500-nasdaq-080339262.html), [Investing.com MU preview](https://www.investing.com/news/stock-market-news/micron-earnings-outlook-what-to-watch-ahead-of-the-september-30-report-93CH-4911385), [Fool CAT](https://www.fool.com/investing/2026/09/29/stock-split-watch-is-caterpillar-next/)

```json
{
  "date": "2026-09-30",
  "no_trade": false,
  "session_note": "Soft core PCE (3.0% vs 3.3%) gives first relief to a 5%+ 10y regime; closing BA short on F/A-XX win (thesis broken), adding half-risk CAT breakout long, keeping rate-sensitive shorts and resting stops.",
  "plays": [
    {
      "ticker": "CAT",
      "direction": "long",
      "entry_type": "stop",
      "entry": 840.00,
      "stop": 812.00,
      "targets": [885.00],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.40,
      "catalyst": "9/30 soft core PCE (3.0% vs 3.3%) with +0.6% real spending; Chicago PMI 09:45 expected rebound to 51.2; CAT pre-market 833 above 20d high 830.50.",
      "thesis": "Strongest large-cap industrial (+2.3% 5d vs XLI -0.7%). Soft-inflation/strong-activity mix favours cyclical capex; a push through pre-market high confirms a range breakout toward mid-800s with no nearby ATH supply.",
      "invalidation": "10-year makes a new high above 5.27%, or CAT back below 825 after triggering.",
      "bear_case": "Strong spending keeps the Fed hiking and yields rising; breakouts in this tape have failed (ANET, ROST)."
    }
  ],
  "manage": [
    {
      "ticker": "BA",
      "action": "close",
      "reason": "Thesis invalidated: Pentagon awarded Boeing the $20B+ F/A-XX fighter over NOC; BA +2.5% pre-market near stop. Thesis exit, not stop-out."
    }
  ],
  "passed": [
    {
      "ticker": "TSLA",
      "direction": "short",
      "entry_type": "stop",
      "entry": 347.50,
      "stop": 362.00,
      "targets": [325.00],
      "p_target_first": 0.38,
      "reason": "Best short: break of 20d low 349.92, but Q3 deliveries (~Oct 2) are a company binary inside the horizon; slot/risk go to CAT."
    },
    {
      "ticker": "XHB",
      "direction": "long",
      "entry_type": "stop",
      "entry": 99.50,
      "stop": 95.80,
      "targets": [104.50],
      "p_target_first": 0.35,
      "reason": "Soft-PCE housing relief would fight my own HD short; a 2bp yield dip is not a regime change."
    }
  ]
}
```

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Wednesday 2026-09-30. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,800.93**
- Cash: $133,972.50
- Session P&L so far: -0.04% (new entries are blocked at -3.0%)
- Gross exposure: $101,254 (99% of equity, cap 150%)
- Net exposure: $-13,057 (-13%, cap +/-100%)
- Risk at stake (entry to stop): $3,536 (3.47% of equity, cap 4.0%) — 0.53% left for new plays
- Slots: 2 open + 5 resting entries of 8 — you may add at most 1 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| BAC | short | 267 | 55.80 | 54.77 | +274 (+1.8%) | 57.70 | 52.90 | Weakest large bank (-7.5% vs 20d avg). A break below today's opening low confirms the 20d-low support failed and opens a |
| HD | short | 61 | 289.30 | 287.65 | +101 (+0.6%) | 297.60 | 278.00 | Cleanest equity expression of frozen housing under 7%+ mortgages; -9.9% vs 50d with fresh 52-week lows. A trade below 28 |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| CAT | long | 18 | 840.00 | stop | 812.00 | 885.00 | 2026-09-30 |
| XLU | short | 423 | 38.95 | stop | 40.15 | 37.55 | 2026-09-29 |
| DAL | long | 149 | 85.80 | stop | 82.40 | 90.50 | 2026-09-29 |
| NVDA | long | 69 | 234.70 | stop | 227.40 | 246.00 | 2026-09-28 |
| ORCL | short | 65 | 130.90 | stop | 138.60 | 119.00 | 2026-09-28 |

### Record

5 closed trades: 2W / 3L, total +0.05R, net $+1,428 realized. Shorts taken: 5.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| BA | short | close | -0.52R | $-130 | 35% |
| DAL | long | stop | +1.00R | $+999 | 46% |
| LLY | long | stop | +1.76R | $+1,654 | 52% |
| ROST | long | stop | -1.18R | $-336 | 47% |
| ANET | long | stop | -1.01R | $-758 | 45% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BAC | 54.77 (10:05 iex) | -0.3% | 54.96 | 54.92 / 54.61-55.11 | 1.33 (2.4%) | 54.73-63.83 | -7.3% / -10.1% | -2.2% | 36.6M |
| HD | 287.50 (10:05 iex) | -0.2% | 288.04 | 290.40 / 286.64-290.54 | 6.44 (2.2%) | 287.34-324.44 | -5.5% / -11.0% | -5.7% | 4.7M |
| CAT | 818.55 (10:05 iex) | -1.0% | 826.64 | 828.50 / 817.15-831.95 | 20.67 (2.5%) | 771.39-830.50 | +2.6% / -0.1% | +2.3% | 2.4M |
| XLU | 39.63 (10:05 iex) | -0.2% | 39.71 | 39.83 / 39.45-39.94 | 0.58 (1.5%) | 39.03-43.39 | -3.7% / -7.2% | -2.0% | 24.8M |
| DAL | 83.85 (10:05 iex) | -1.2% | 84.87 | 84.85 / 83.48-85.14 | 2.47 (2.9%) | 75.99-85.47 | +5.4% / +1.0% | +1.1% | 7.1M |
| NVDA | 231.37 (10:05 iex) | +1.8% | 227.21 | 229.27 / 228.79-232.35 | 5.37 (2.4%) | 208.93-234.50 | +2.1% / +4.8% | -0.7% | 113.6M |
| ORCL | 136.91 (10:05 iex) | -0.6% | 137.79 | 136.54 / 134.75-138.15 | 7.70 (5.6%) | 131.58-170.70 | -6.4% / -3.4% | -7.6% | 35.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 768.73 (10:05 iex) | +0.6% | 764.20 | 766.41 / 766.00-768.65 | 6.97 (0.9%) | 747.74-775.14 | +0.0% / +0.4% | -1.2% | 44.0M |
| QQQ | 743.98 (10:05 iex) | +0.8% | 737.93 | 740.19 / 739.76-744.26 | 9.99 (1.4%) | 699.27-748.35 | +2.1% / +3.4% | -1.3% | 33.4M |
| IWM | 279.73 (10:05 iex) | +0.3% | 279.01 | 280.16 / 279.06-280.32 | 3.60 (1.3%) | 277.41-295.41 | -2.7% / -4.7% | -2.9% | 23.2M |
| DIA | 513.00 (10:03 iex) | +0.0% | 512.88 | 513.99 / 512.36-514.16 | 5.01 (1.0%) | 510.42-536.38 | -1.5% / -2.5% | -1.0% | 3.4M |
| TLT | 78.00 (10:05 iex) | -0.3% | 78.23 | 78.16 / 77.92-78.21 | 0.83 (1.1%) | 77.84-82.50 | -3.3% / -4.3% | -4.3% | 40.1M |
| GLD | 383.09 (10:05 iex) | +0.1% | 382.89 | 384.36 / 382.70-384.59 | 7.25 (1.9%) | 376.88-413.54 | -3.4% / -3.3% | -4.3% | 9.7M |
| USO | 145.78 (10:05 iex) | +1.7% | 143.35 | 147.14 / 145.79-147.17 | 6.18 (4.3%) | 136.09-163.35 | -4.3% / +5.0% | -0.5% | 6.6M |
| SMH | 610.34 (10:05 iex) | +0.6% | 606.90 | 609.76 / 608.07-611.95 | 16.16 (2.7%) | 537.73-613.27 | +5.8% / +6.9% | -0.1% | 6.5M |
| XLK | 196.73 (10:05 iex) | +1.1% | 194.50 | 195.47 / 195.26-196.88 | 3.27 (1.7%) | 181.87-196.94 | +2.8% / +5.1% | -0.9% | 6.9M |
| XLF | 53.80 (10:05 iex) | -0.4% | 54.01 | 53.99 / 53.70-54.02 | 0.75 (1.4%) | 53.72-58.39 | -3.7% / -4.9% | -1.4% | 36.5M |
| XLE | 61.75 (10:05 iex) | +0.3% | 61.54 | 61.82 / 61.70-62.06 | 1.31 (2.1%) | 60.95-65.78 | -3.2% / -0.1% | -0.4% | 34.1M |
| XLV | 169.50 (10:05 iex) | -0.7% | 170.73 | 170.05 / 169.39-170.49 | 2.24 (1.3%) | 164.48-173.82 | +1.1% / +1.9% | +0.5% | 7.7M |
| XLI | 168.57 (10:05 iex) | -0.3% | 169.13 | 169.57 / 168.17-169.79 | 2.30 (1.4%) | 167.04-175.30 | -0.9% / -4.5% | -0.7% | 7.7M |
| XLY | 109.35 (10:05 iex) | +0.2% | 109.15 | 109.26 / 108.61-109.40 | 1.54 (1.4%) | 108.68-116.81 | -2.5% / -4.6% | -2.8% | 6.4M |
| XLP | 81.84 (10:04 iex) | -0.0% | 81.85 | 82.28 / 81.79-82.30 | 0.88 (1.1%) | 81.29-85.60 | -1.4% / -2.7% | -1.1% | 10.8M |
| XLU | 39.63 (10:05 iex) | -0.2% | 39.71 | 39.83 / 39.45-39.94 | 0.58 (1.5%) | 39.03-43.39 | -3.7% / -7.2% | -2.0% | 24.8M |
| XLB | 49.22 (10:05 iex) | +0.2% | 49.10 | 49.29 / 49.08-49.40 | 0.69 (1.4%) | 48.91-53.27 | -3.1% / -4.6% | -2.8% | 11.2M |
| XLRE | 41.09 (10:04 iex) | -0.6% | 41.34 | 41.52 / 41.04-41.56 | 0.51 (1.2%) | 41.07-44.02 | -3.0% / -5.7% | -2.7% | 5.6M |
| XLC | 112.20 (10:05 iex) | +0.7% | 111.47 | 111.47 / 111.19-112.25 | 1.92 (1.7%) | 109.95-115.61 | -0.7% / +0.4% | -1.8% | 5.5M |
| KRE | 69.74 (10:05 iex) | -0.1% | 69.83 | 69.83 / 69.52-70.26 | 1.26 (1.8%) | 69.45-75.07 | -3.7% / -6.0% | -1.9% | 14.2M |
| XHB | 97.10 (10:03 iex) | +0.1% | 96.97 | 97.68 / 96.97-97.82 | 2.12 (2.2%) | 95.26-102.95 | -1.3% / -6.1% | -2.5% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 338.38 (10:05 iex) | +2.7% | 329.40 | 330.80 / 330.14-338.24 | 6.78 (2.1%) | 309.90-345.34 | -0.5% / +2.3% | -3.0% | 42.6M |
| MSFT | 519.01 (10:05 iex) | +2.0% | 508.96 | 511.61 / 510.31-519.76 | 11.73 (2.3%) | 486.00-519.40 | +1.8% / +6.1% | +2.2% | 21.1M |
| NVDA | 231.37 (10:05 iex) | +1.8% | 227.21 | 229.27 / 228.79-232.35 | 5.37 (2.4%) | 208.93-234.50 | +2.1% / +4.8% | -0.7% | 113.6M |
| AMZN | 250.34 (10:05 iex) | +1.5% | 246.67 | 246.79 / 246.08-250.60 | 5.22 (2.1%) | 244.30-261.12 | -2.4% / -3.7% | -3.3% | 33.9M |
| GOOGL | 351.65 (10:05 iex) | +3.1% | 340.92 | 344.15 / 344.03-352.01 | 8.49 (2.5%) | 327.74-364.17 | -0.3% / -0.9% | -2.9% | 26.1M |
| META | 729.75 (10:05 iex) | -1.2% | 738.79 | 730.04 / 721.30-733.47 | 29.93 (4.1%) | 555.66-779.82 | +9.3% / +19.4% | +0.3% | 24.1M |
| TSLA | 348.90 (10:05 iex) | -1.1% | 352.84 | 352.01 / 345.88-352.50 | 11.00 (3.1%) | 349.92-386.83 | -3.4% / +1.6% | -6.9% | 38.8M |
| AVGO | 355.42 (10:05 iex) | +0.1% | 355.10 | 357.04 / 354.20-357.90 | 9.91 (2.8%) | 335.20-372.02 | -0.2% / -5.3% | -2.6% | 27.5M |
| AMD | 604.69 (10:04 iex) | -0.5% | 607.57 | 609.48 / 602.16-615.17 | 26.04 (4.3%) | 440.50-639.00 | +12.1% / +19.4% | -2.6% | 22.2M |
| ORCL | 136.91 (10:05 iex) | -0.6% | 137.79 | 136.54 / 134.75-138.15 | 7.70 (5.6%) | 131.58-170.70 | -6.4% / -3.4% | -7.6% | 35.8M |
| NFLX | 70.04 (10:05 iex) | -0.4% | 70.30 | 70.20 / 69.68-70.20 | 2.14 (3.0%) | 68.88-83.60 | -7.0% / -7.0% | -2.6% | 33.3M |
| CRM | 231.00 (10:04 iex) | +2.5% | 225.31 | 225.40 / 224.43-231.94 | 8.07 (3.6%) | 221.18-267.80 | -8.0% / +4.5% | -3.4% | 13.0M |
| JPM | 334.46 (10:05 iex) | -0.2% | 334.98 | 334.89 / 333.95-336.34 | 7.09 (2.1%) | 333.33-362.86 | -4.1% / -5.2% | -1.5% | 8.0M |
| GS | 911.08 (10:05 iex) | -0.6% | 916.24 | 915.00 / 909.13-916.05 | 27.06 (3.0%) | 903.85-1,043.84 | -6.2% / -9.5% | -3.5% | 2.1M |
| BAC | 54.77 (10:05 iex) | -0.3% | 54.96 | 54.92 / 54.61-55.11 | 1.33 (2.4%) | 54.73-63.83 | -7.3% / -10.1% | -2.2% | 36.6M |
| XOM | 162.80 (10:04 iex) | +0.9% | 161.35 | 162.23 / 161.80-163.32 | 3.82 (2.4%) | 155.85-169.64 | -0.9% / +1.1% | +1.7% | 14.1M |
| CVX | 205.35 (10:04 iex) | +0.5% | 204.38 | 205.09 / 204.63-206.14 | 4.59 (2.2%) | 200.78-217.78 | -2.4% / +1.7% | +1.0% | 10.0M |
| LLY | 1,187.03 (10:04 iex) | +0.2% | 1,184.63 | 1,186.49 / 1,181.70-1,190.93 | 28.54 (2.4%) | 1,113.29-1,197.79 | +2.8% / +0.6% | +1.2% | 2.3M |
| UNH | 365.82 (10:05 iex) | -2.4% | 374.94 | 374.93 / 366.15-374.93 | 8.07 (2.2%) | 366.00-404.04 | -2.0% / -5.2% | +0.5% | 5.1M |
| JNJ | 266.25 (10:04 iex) | -0.5% | 267.57 | 267.91 / 266.02-268.48 | 5.02 (1.9%) | 260.68-281.07 | -0.9% / +0.9% | -0.6% | 6.3M |
| WMT | 106.35 (10:04 iex) | -0.4% | 106.80 | 106.97 / 106.07-107.03 | 2.04 (1.9%) | 104.66-111.23 | -0.6% / -2.1% | -3.0% | 22.2M |
| COST | 921.69 (10:05 iex) | -0.3% | 924.59 | 926.39 / 919.46-926.39 | 14.43 (1.6%) | 883.10-952.10 | +1.6% / -1.0% | +2.8% | 2.4M |
| HD | 287.50 (10:05 iex) | -0.2% | 288.04 | 290.40 / 286.64-290.54 | 6.44 (2.2%) | 287.34-324.44 | -5.5% / -11.0% | -5.7% | 4.7M |
| CAT | 818.55 (10:05 iex) | -1.0% | 826.64 | 828.50 / 817.15-831.95 | 20.67 (2.5%) | 771.39-830.50 | +2.6% / -0.1% | +2.3% | 2.4M |
| BA | 188.59 (10:05 iex) | +0.5% | 187.68 | 192.05 / 187.18-192.99 | 6.57 (3.5%) | 184.01-215.29 | -7.4% / -12.0% | -5.1% | 7.5M |
| DAL | 83.85 (10:05 iex) | -1.2% | 84.87 | 84.85 / 83.48-85.14 | 2.47 (2.9%) | 75.99-85.47 | +5.4% / +1.0% | +1.1% | 7.1M |
| UAL | 111.56 (10:04 iex) | -1.0% | 112.65 | 112.56 / 110.81-112.93 | 4.25 (3.8%) | 104.15-118.26 | +2.7% / -3.0% | -2.2% | 3.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-09-30 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| MSGY | 5.98 (10:02 iex) | +34.7% | 4.44 | 4.93 / 4.79-6.78 | 1.37 (30.9%) | 1.73-11.42 | +81.4% / +78.0% | +119.8% | 4.8M |
| USDE | 17.80 (10:05 iex) | +16.2% | 15.32 | 16.04 / 16.04-18.10 | 1.96 (12.8%) | 5.87-17.50 | +52.9% / +154.9% | +13.1% | 5.4M |
| CAPR | 9.79 (10:05 iex) | +14.2% | 8.57 | 10.01 / 9.55-10.72 | 0.62 (7.2%) | 8.15-11.00 | -4.0% / +2.5% | -8.2% | 3.0M |
| IONX | 31.37 (10:05 iex) | +14.3% | 27.45 | 27.75 / 27.62-31.20 | 3.10 (11.3%) | 18.01-32.56 | +17.4% / +10.6% | +14.8% | 1.4M |
| RKLX | 19.25 (10:02 iex) | +12.4% | 17.12 | 17.62 / 17.50-19.25 | 1.80 (10.5%) | 13.30-20.14 | +6.9% / -6.4% | -7.0% | 3.0M |
| TRLV | 10.80 (10:05 iex) | -12.9% | 12.41 | 10.86 / 10.40-11.17 | 0.74 (5.9%) | 10.71-12.93 | +4.5% / +18.6% | -0.5% | 2.4M |
