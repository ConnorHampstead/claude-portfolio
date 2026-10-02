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

# Pre-market brief: Friday 2026-10-02 (written 09:05 ET / 15:05 Stockholm)

## 1. Tape
September payrolls came out at 08:30 ET and were weak: **+29k against roughly 90k expected, and unemployment rose to 4.2% from 4.1%** (verified: CNN, Yahoo). The market read it as good news because it lowers the chance of a rate hike. The 10-year yield fell to about **5.18%** from about 5.33% yesterday, and the 30-year to 5.57%. October hike odds were cut to roughly 16%, from 64% a week ago (Yahoo, single source). Futures are up: SPY 770.59 (+0.9%), QQQ +1.4%, IWM +1.5%, TLT +0.9%, SMH +2.3%. Oil is down: USO is −4.2% and Brent is near $99, after reports that the EU is discussing releases of diesel and crude stocks. Nike fell 3–6% after hours on a revenue miss, high-single-digit revenue decline guidance and layoffs. The regime this morning is **risk-on rate relief**, after a stretch where rising yields drove the tape. **The edge today is long**, mainly in rate-sensitive and AI names. The main risk is that a soft payroll print turns into a growth scare by the afternoon, and nothing looks at the book after 10:05.

## 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Sept NFP / unemployment | **+29k vs ~90k; UR 4.2% vs 4.1%.** Yields −15bp, futures +0.9–1.4% | XLRE, UNH shorts; IWM; all longs |
| 10:00 | 16:00 | Factory orders (Aug) | cons. −0.1% | minor |
| — | — | Fed speakers today | could not verify a schedule | all |
| AMC yesterday | — | NKE Q1 FY27 | EPS 0.48 vs 0.43 beat; revenue $11.21B vs $11.4B miss; FY revenue guided down high-single digits | none held |

## 3. Open positions and resting entries
Resting entries are cleared before the weekend, so tonight every unfilled entry goes away.

- **UNH short** (363.57, stop 375.50, target 345): **intact.** Pre-market it is +0.4% while SPY is +0.9%, so it is still weaker than the market and sits under its 20-day average. Hold, no change.
- **XLRE short** (40.46, stop 41.15, target 39.40): **weakening.** The trade was a bet on rising rates, and a 15bp drop in the 10-year works directly against it. So far XLRE has only gained 0.4% (40.84), which is muted. The stop is 0.31 away, inside one ATR (0.52), so I can't tighten it in a useful way. The review decides (see section 7).
- **XLU short, sell stop 38.95: cancel.** It is also a rising-rates trade, and it would get the same rate-relief hit. The trigger is 2.5% below the 39.93 pre-market price, so it is very unlikely to fill before tonight's clearing anyway. Cancelling frees about 0.5% of risk and one slot.
- **NVDA long, buy stop 234.70: keep.** Pre-market is already 235.98, above the 20-day high of 234.50, so it should trigger at the open. Semiconductors are leading (SMH +2.3%). Filling near 236 lifts the risk to about 0.58%. Accepted.
- **DAL long, buy stop 85.80: keep.** Pre-market is 86.15, above the 20-day high of 85.47, so it should trigger at the open. Oil −4% and lower yields both help airlines (UAL +3.1%).
- **MSFT long, buy stop 523: keep.** Last trade 518.65; the 20-day high is 522.85. If it is not triggered today, it is cleared tonight.

## 4. New plays

**IWM long**
| Field | Value |
|---|---|
| Ticker | IWM |
| Direction | Long |
| Catalyst | 2026-10-02 NFP miss (+29k): 10y yield −15bp to 5.18%, hike odds cut from 64% to 16% |
| Thesis | Small caps have suffered most from the rise in yields (−4.5% vs 50-day average, −2.2% vs 20-day). They are the most direct equity play on a turn in rates. A pullback into part of the gap gives a better entry than chasing +1.5%. |
| Entry | 281.50 limit (pre-market 283.08, prior close 279.02) |
| Stop | 276.90: about 1.25 ATR below entry and above the 20-day low of 275.45. A move back there means the payroll rally has failed. |
| Target | 289.50 (+1.74R) |
| Risk tier | 0.5: this enters on a gap from a macro print into an index that was in a downtrend |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target first) | 40% |
| Invalidation | The 10-year moves back above 5.30%, or the payroll miss becomes a growth scare (IWM loses ground to SPY while yields fall) |
| What I'd be wrong about | 29k with unemployment rising is close to stall speed. Small caps are the most exposed to a slowdown, so "bad news is good" could flip to "bad news is bad" within days. |

The limit sits about halfway into the gap. If IWM keeps running and never comes back to 281.50, I miss the trade, and I accept that. Buying the open at +1.5% would put the entry about 1.6 ATR from a sensible stop, with a worse R.

**XLE short (probe)**
| Field | Value |
|---|---|
| Ticker | XLE |
| Direction | Short |
| Catalyst | Oil −3–4% on 2026-10-02 after EU talks on diesel and crude stock releases; USO −4.2% |
| Thesis | If XLE breaks its 20-day low (60.95), the oil risk premium is coming out. A stop entry below the low only fills if the break actually happens. |
| Entry | 60.85 sell stop (pre-market 61.91, so the trigger is not crossed) |
| Stop | 62.60: back above today's pre-market level means the break failed |
| Target | 58.30 (+1.46R) |
| Risk tier | 0.25: geopolitical headlines (US military deployments) can bring the oil premium back overnight. It also overlaps the DAL long, since both win if oil falls. |
| Time horizon | 1–5 days |
| Conviction | 2 |
| P(target first) | 33% |
| Invalidation | Brent back above $102, or a new Middle East escalation |
| What I'd be wrong about | A stock release is still only being discussed, and supply is still tight. The headline-driven drop could fully reverse. |

## 5. Both sides
- **Best long: IWM**, entry 281.50, stop 276.90, target 289.50, P = 40%. Taken.
- **Best short: NKE** on its post-earnings revenue miss and guide-down. I **could not verify a current pre-market price** (reports range from −3% to −6%), so it has no levels and is excluded. The best short I could put levels on is **XLE**, sell stop 60.85, stop 62.60, target 58.30, P = 33%. Taken as a probe.

## 6. Passing on
- **NKE short:** price not verified, so no levels and no trade. I would look at it again tomorrow if it holds below its gap.
- **XHB long** (+2.4% to 99.10): same rate-relief trade as IWM, already extended in pre-market. One rates long is enough. In `passed` at limit 97.80, stop 95.40, target 101.80, P = 38%.
- **TLT long:** I'd be holding the rate view directly as well as through IWM, and it is already +0.9%. No levels given.
- **WDC short** (−7% on Toshiba HDD capacity news): price not verified.

## 7. For the post-open review
- **XLRE:** if it trades **above 41.00 at 10:05 ET**, the rate-relief move is hitting REITs, so close it at market and don't wait for the 41.15 stop. If it is below 40.70, hold.
- **NVDA / DAL fills:** if either filled and is already **below its trigger by 10:05** (NVDA < 233.50, DAL < 85.00), the breakout failed at the open. Close it.
- **IWM:** if it opens and holds above 284 without coming near 281.50, do not chase. Leave the limit; it is cleared tonight.
- **If yields reverse:** if the 10-year is back above 5.28% by 10:05, cancel the IWM limit.

## 8. Book state
- Exposure: if every order fills, gross is about 125% of equity; the net shrinks from −16% toward about +20%. Both are inside the caps.
- Risk at stake: after the XLU cancel and the NVDA/DAL gap fills, about 2.1% existing plus 0.75% new, roughly **2.9% of the 4% cap**. Slots: 7 of 8.

```json
{
  "date": "2026-10-02",
  "no_trade": false,
  "session_note": "Payrolls +29k vs ~90k, UR 4.2%: 10y -15bp to 5.18%, hike odds slashed; risk-on rate relief, edge long. Adding IWM rate-relief long on pullback, XLE breakdown probe; cancelling rate-up XLU short.",
  "plays": [
    {
      "ticker": "IWM",
      "direction": "long",
      "entry_type": "limit",
      "entry": 281.50,
      "stop": 276.90,
      "targets": [289.50],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.40,
      "catalyst": "2026-10-02 September NFP +29k vs ~90k, UR 4.2%; 10y yield fell to 5.18% from ~5.33%, October hike odds cut to ~16%.",
      "thesis": "Small caps are the most rate-damaged group (-4.5% vs 50d) and the most direct beneficiary of a rates reversal. A limit halfway into the +1.5% gap gives a better entry than chasing.",
      "invalidation": "10y back above 5.30%, or IWM underperforming SPY on falling yields (growth-scare read).",
      "bear_case": "29k with rising unemployment is near stall speed; bad-news-is-good can flip to bad-news-is-bad and small caps are most exposed."
    },
    {
      "ticker": "XLE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 60.85,
      "stop": 62.60,
      "targets": [58.30],
      "time_horizon": "1-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.33,
      "catalyst": "2026-10-02 oil -3-4% on EU talks to release diesel/crude stocks; USO -4.2% pre-market.",
      "thesis": "A break of XLE's 20d low (60.95) would confirm the oil risk premium unwinding; the stop entry only fills on that confirmation.",
      "invalidation": "Brent back above $102 or a fresh Middle East escalation headline.",
      "bear_case": "Stock releases are only being discussed and supply is tight; geopolitical premium can reprice overnight. Overlaps the DAL long (both win on falling oil)."
    }
  ],
  "manage": [
    {
      "ticker": "XLU",
      "action": "close",
      "reason": "Rising-rates short contradicted by 15bp yield drop on weak payrolls; trigger 2.5% away and order would be weekend-cleared anyway. Frees risk and a slot."
    }
  ],
  "passed": [
    {
      "ticker": "XHB",
      "direction": "long",
      "entry_type": "limit",
      "entry": 97.80,
      "stop": 95.40,
      "targets": [101.80],
      "p_target_first": 0.38,
      "reason": "Same rate-relief factor as the IWM long, already +2.4% pre-market; one rates long is enough."
    }
  ]
}
```

Sources: [CNN – jobs report](https://www.cnn.com/2026/10/02/economy/us-jobs-report-september-final), [Yahoo Finance live](https://finance.yahoo.com/markets/live/stock-market-today-friday-october-2-dow-sp-500-nasdaq-september-jobs-report-080623878.html), [Yahoo jobs live](https://finance.yahoo.com/economy/live/september-jobs-report-live-updates-labor-market-124648123.html), [The National – oil](https://www.thenationalnews.com/business/energy/2026/10/02/oil-prices-stable-amid-mixed-supply-signals-from-the-middle-east/), [Trading Economics – Brent](https://tradingeconomics.com/commodity/brent-crude-oil), [WTOP – Nike Q1](https://wtop.com/news/2026/10/nike-fiscal-q1-earnings-snapshot), [CNBC – Nike](https://www.cnbc.com/2026/10/01/nike-nke-q1-2027-earnings.html)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Friday 2026-10-02. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$102,071.21**
- Cash: $80,862.57
- Session P&L so far: -0.60% (new entries are blocked at -3.0%)
- Gross exposure: $86,150 (84% of equity, cap 150%)
- Net exposure: $+52,985 (+52%, cap +/-100%)
- Risk at stake (entry to stop): $2,435 (2.39% of equity, cap 4.0%) — 1.61% left for new plays
- Slots: 3 open + 3 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 48% of equity in notional: at 1% risk its stop must be at least 2.1% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| DAL | long | 149 | 86.06 | 84.12 | -289 (-2.3%) | 82.40 | 90.50 | Buyers absorbed a fuel-cost downgrade on 9/28 and DAL closed near highs. A break of the 20d high with oil fading opens a |
| NVDA | long | 69 | 236.40 | 237.29 | +62 (+0.4%) | 227.40 | 246.00 | Only mega-cap with a dated positive catalyst and green on a red tape. A break through the 20d high of 234.50 means range |
| UNH | short | 21 | 363.57 | 366.60 | -64 (-0.8%) | 375.50 | 345.00 | Relative weakness in managed care: -5.2% vs 50d, losing its 20d floor while the market rallies. A trade below 363.50 con |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XLE | short | 146 | 60.85 | stop | 62.60 | 58.30 | 2026-10-02 |
| IWM | long | 111 | 281.50 | limit | 276.90 | 289.50 | 2026-10-02 |
| MSFT | long | 18 | 523.00 | stop | 509.00 | 547.00 | 2026-10-01 |

### Record

8 closed trades: 4W / 4L, total +1.92R, net $+2,365 realized. Shorts taken: 8.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLRE | short | stop | -1.01R | $-529 | 40% |
| BAC | short | target | +1.53R | $+774 | 36% |
| HD | short | target | +1.36R | $+691 | 40% |
| BA | short | close | -0.52R | $-130 | 35% |
| DAL | long | stop | +1.00R | $+999 | 46% |

### Ideas you passed on, replayed against the tape

6 resolved: 2 reached target first, 4 stop first, 0 never reached the entry, 0 expired, 0 ambiguous. Average -0.11R across the 6 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-09-30 pre-market | TSLA | short | Best short: break of 20d low 349.92, but Q3 deliveries (~Oct 2) are a company bi | stop | -1.00R | 38% |
| 2026-10-01 pre-market | KRE | short | Same rates factor as BAC short already held; no slot. | stop | -1.00R | 40% |
| 2026-09-23 pre-market | SMH | long | Leadership group but +12% in 5 days; only worth owning on a pullback, not chasin | target | +1.67R | 40% |
| 2026-10-01 open | KRE | short | Broke 20d low but same financials/rates factor as BAC short already held. | stop | -0.99R | 40% |
| 2026-09-23 pre-market | BAC | short | stop entry 55.90 not placed: the market (55.885) had already crossed the trigger | target | +1.67R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| DAL | 84.14 (10:05 iex) | +0.0% | 84.13 | 85.76 / 83.48-86.17 | 2.43 (2.9%) | 76.89-85.47 | +3.7% / +0.1% | +1.7% | 7.2M |
| NVDA | 237.28 (10:05 iex) | +2.8% | 230.86 | 236.05 / 234.53-237.84 | 5.32 (2.3%) | 208.93-234.50 | +3.3% / +6.1% | +2.8% | 111.3M |
| UNH | 366.39 (10:03 iex) | +0.3% | 365.20 | 365.14 / 364.47-367.16 | 7.44 (2.0%) | 362.60-404.04 | -3.8% / -7.1% | -2.6% | 5.2M |
| XLE | 62.37 (10:05 iex) | -0.5% | 62.70 | 61.86 / 61.86-62.73 | 1.28 (2.0%) | 60.95-65.78 | -1.0% / +1.5% | +0.2% | 34.4M |
| IWM | 283.08 (10:05 iex) | +1.5% | 279.02 | 282.33 / 281.90-283.33 | 3.65 (1.3%) | 275.45-295.41 | -2.2% / -4.5% | -0.9% | 23.7M |
| MSFT | 517.80 (10:05 iex) | +1.0% | 512.80 | 519.25 / 515.00-522.50 | 12.20 (2.4%) | 486.00-522.85 | +2.3% / +5.8% | +3.0% | 21.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 771.75 (10:05 iex) | +1.0% | 763.99 | 770.58 / 769.07-772.09 | 6.95 (0.9%) | 747.74-775.14 | -0.0% / +0.3% | -0.4% | 46.0M |
| QQQ | 753.81 (10:05 iex) | +1.6% | 742.03 | 751.31 / 749.10-753.76 | 9.79 (1.3%) | 699.27-748.35 | +2.2% / +3.8% | +0.1% | 33.8M |
| IWM | 283.08 (10:05 iex) | +1.5% | 279.02 | 282.33 / 281.90-283.33 | 3.65 (1.3%) | 275.45-295.41 | -2.2% / -4.5% | -0.9% | 23.7M |
| DIA | 511.83 (10:05 iex) | +0.6% | 508.62 | 512.54 / 510.28-513.06 | 5.10 (1.0%) | 504.70-536.38 | -2.0% / -3.2% | -0.8% | 3.5M |
| TLT | 78.29 (10:05 iex) | +0.7% | 77.71 | 77.93 / 77.86-78.27 | 0.84 (1.1%) | 76.76-82.17 | -3.1% / -4.3% | -1.8% | 45.6M |
| GLD | 384.54 (10:05 iex) | +0.5% | 382.76 | 384.45 / 383.17-385.22 | 6.72 (1.8%) | 376.88-413.54 | -3.0% / -3.4% | -2.3% | 9.0M |
| USO | 143.37 (10:04 iex) | -4.4% | 150.02 | 143.56 / 142.86-145.36 | 5.80 (3.9%) | 138.01-163.35 | -0.3% / +9.3% | -2.0% | 6.4M |
| SMH | 636.11 (10:05 iex) | +3.0% | 617.81 | 632.27 / 629.00-636.22 | 15.44 (2.5%) | 537.73-620.91 | +6.5% / +8.6% | +2.9% | 6.4M |
| XLK | 201.13 (10:05 iex) | +1.7% | 197.81 | 201.00 / 199.87-201.16 | 3.19 (1.6%) | 181.87-198.54 | +3.9% / +6.5% | +1.6% | 7.2M |
| XLF | 53.51 (10:05 iex) | +0.1% | 53.46 | 53.58 / 53.34-53.76 | 0.77 (1.4%) | 52.81-58.39 | -4.0% / -5.7% | -2.0% | 38.1M |
| XLE | 62.37 (10:05 iex) | -0.5% | 62.70 | 61.86 / 61.86-62.73 | 1.28 (2.0%) | 60.95-65.78 | -1.0% / +1.5% | +0.2% | 34.4M |
| XLV | 165.99 (10:05 iex) | -0.1% | 166.20 | 166.54 / 165.37-166.85 | 2.36 (1.4%) | 164.48-173.50 | -1.3% / -1.0% | -2.2% | 8.1M |
| XLI | 169.49 (10:05 iex) | +0.5% | 168.64 | 170.20 / 168.82-171.00 | 2.41 (1.4%) | 166.18-175.30 | -0.9% / -4.6% | -0.1% | 7.5M |
| XLY | 110.49 (10:05 iex) | +1.5% | 108.81 | 109.89 / 109.88-110.56 | 1.51 (1.4%) | 107.99-116.81 | -2.3% / -4.7% | -1.4% | 6.6M |
| XLP | 80.42 (10:04 iex) | +0.1% | 80.33 | 80.48 / 80.18-80.73 | 0.94 (1.2%) | 80.14-85.09 | -2.7% / -4.3% | -1.7% | 11.1M |
| XLU | 39.91 (10:05 iex) | +0.6% | 39.68 | 39.88 / 39.78-40.20 | 0.56 (1.4%) | 39.03-43.39 | -3.1% / -6.7% | +0.8% | 27.6M |
| XLB | 49.22 (10:05 iex) | +1.4% | 48.54 | 48.83 / 48.80-49.22 | 0.72 (1.5%) | 47.81-53.27 | -3.5% / -5.5% | -2.3% | 11.7M |
| XLRE | 41.02 (10:04 iex) | +0.8% | 40.68 | 40.94 / 40.77-41.30 | 0.52 (1.3%) | 40.41-43.91 | -3.9% / -6.9% | -2.3% | 5.8M |
| XLC | 110.76 (10:05 iex) | +0.7% | 109.94 | 110.31 / 110.07-110.81 | 1.97 (1.8%) | 109.66-115.61 | -2.0% / -1.0% | -3.6% | 5.8M |
| KRE | 70.89 (10:05 iex) | +1.3% | 69.95 | 70.55 / 70.46-71.36 | 1.28 (1.8%) | 67.97-75.07 | -3.1% / -5.6% | -1.4% | 15.0M |
| XHB | 97.67 (10:04 iex) | +0.9% | 96.78 | 98.73 / 97.23-99.13 | 2.10 (2.2%) | 94.08-102.95 | -1.1% / -5.9% | -0.0% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 332.74 (10:05 iex) | +0.7% | 330.32 | 333.26 / 330.61-333.46 | 6.50 (2.0%) | 309.90-345.34 | -0.4% / +2.5% | -1.7% | 42.6M |
| MSFT | 517.80 (10:05 iex) | +1.0% | 512.80 | 519.25 / 515.00-522.50 | 12.20 (2.4%) | 486.00-522.85 | +2.3% / +5.8% | +3.0% | 21.7M |
| NVDA | 237.28 (10:05 iex) | +2.8% | 230.86 | 236.05 / 234.53-237.84 | 5.32 (2.3%) | 208.93-234.50 | +3.3% / +6.1% | +2.8% | 111.3M |
| AMZN | 252.73 (10:05 iex) | +1.8% | 248.23 | 251.42 / 250.76-253.56 | 5.42 (2.2%) | 244.30-261.12 | -1.5% / -3.1% | -0.5% | 34.9M |
| GOOGL | 345.01 (10:05 iex) | +2.0% | 338.24 | 341.26 / 341.16-345.00 | 9.45 (2.8%) | 327.74-364.17 | -1.3% / -1.6% | -1.2% | 27.4M |
| META | 735.31 (10:05 iex) | +1.3% | 725.93 | 733.25 / 727.49-741.58 | 29.26 (4.0%) | 603.87-779.82 | +5.2% / +16.7% | -6.6% | 24.0M |
| TSLA | 371.18 (10:05 iex) | +4.8% | 354.11 | 360.01 / 359.41-371.73 | 10.76 (3.0%) | 345.88-386.83 | -3.0% / +2.2% | -6.3% | 38.8M |
| AVGO | 354.55 (10:05 iex) | +3.2% | 343.64 | 349.99 / 347.42-354.75 | 10.26 (3.0%) | 335.20-372.02 | -2.9% / -8.0% | -1.9% | 26.9M |
| AMD | 642.12 (10:05 iex) | +4.3% | 615.73 | 636.34 / 630.76-642.73 | 25.67 (4.2%) | 440.50-639.00 | +10.4% / +20.3% | -2.2% | 22.5M |
| ORCL | 143.88 (10:05 iex) | +4.2% | 138.07 | 142.09 / 141.21-143.88 | 6.51 (4.7%) | 131.58-170.70 | -5.8% / -3.5% | -1.1% | 35.8M |
| NFLX | 67.50 (10:05 iex) | -0.5% | 67.85 | 67.60 / 67.17-67.87 | 2.12 (3.1%) | 67.79-83.60 | -8.7% / -10.3% | -5.4% | 35.1M |
| CRM | 237.11 (10:04 iex) | +0.2% | 236.69 | 238.11 / 235.09-239.00 | 8.36 (3.5%) | 221.18-267.80 | -2.4% / +8.5% | -0.6% | 12.5M |
| JPM | 331.79 (10:05 iex) | -0.4% | 333.18 | 334.00 / 330.68-334.85 | 7.32 (2.2%) | 325.87-362.86 | -3.9% / -5.5% | -1.6% | 8.4M |
| GS | 903.09 (10:02 iex) | +0.7% | 896.67 | 905.50 / 901.36-913.00 | 26.70 (3.0%) | 881.00-1,043.84 | -7.2% / -10.7% | -2.9% | 2.2M |
| BAC | 53.62 (10:05 iex) | -0.2% | 53.73 | 53.89 / 53.40-54.00 | 1.33 (2.5%) | 52.89-63.83 | -8.2% / -11.7% | -4.1% | 38.7M |
| XOM | 163.37 (10:03 iex) | -0.3% | 163.82 | 161.55 / 161.55-164.13 | 3.76 (2.3%) | 155.85-169.64 | +0.7% / +2.4% | +1.0% | 14.2M |
| CVX | 206.19 (10:05 iex) | -0.4% | 207.10 | 204.80 / 204.45-207.26 | 4.42 (2.1%) | 200.78-217.78 | -0.8% / +2.7% | +0.7% | 9.8M |
| LLY | 1,154.85 (10:04 iex) | +0.4% | 1,149.85 | 1,153.82 / 1,141.55-1,157.74 | 31.91 (2.8%) | 1,113.29-1,215.00 | -0.2% / -2.3% | -2.7% | 2.3M |
| UNH | 366.39 (10:03 iex) | +0.3% | 365.20 | 365.14 / 364.47-367.16 | 7.44 (2.0%) | 362.60-404.04 | -3.8% / -7.1% | -2.6% | 5.2M |
| JNJ | 256.81 (10:05 iex) | -0.7% | 258.66 | 259.38 / 256.44-259.38 | 4.99 (1.9%) | 258.33-278.89 | -3.8% / -2.6% | -4.4% | 6.4M |
| WMT | 104.11 (10:04 iex) | -0.1% | 104.26 | 104.94 / 104.02-105.14 | 2.15 (2.1%) | 103.58-111.23 | -2.8% / -4.2% | -3.1% | 22.4M |
| COST | 913.88 (10:05 iex) | -0.1% | 914.94 | 921.18 / 912.66-921.18 | 15.52 (1.7%) | 883.10-931.09 | +0.8% / -2.0% | +2.1% | 2.4M |
| HD | 285.61 (10:05 iex) | +1.1% | 282.46 | 286.56 / 284.22-287.70 | 6.60 (2.3%) | 277.15-321.80 | -6.3% / -12.3% | -3.3% | 5.1M |
| CAT | 843.04 (10:04 iex) | +2.0% | 826.35 | 840.80 / 836.46-858.87 | 21.67 (2.6%) | 772.86-833.62 | +2.1% / +0.2% | +2.6% | 2.3M |
| BA | 192.53 (10:05 iex) | +0.1% | 192.28 | 193.87 / 190.59-195.35 | 6.98 (3.6%) | 184.01-215.29 | -4.3% / -9.6% | -2.3% | 8.1M |
| DAL | 84.14 (10:05 iex) | +0.0% | 84.13 | 85.76 / 83.48-86.17 | 2.43 (2.9%) | 76.89-85.47 | +3.7% / +0.1% | +1.7% | 7.2M |
| UAL | 112.57 (10:05 iex) | +0.7% | 111.78 | 114.75 / 111.51-114.76 | 4.10 (3.7%) | 104.59-118.26 | +1.5% / -3.6% | +0.5% | 3.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-02 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SDEV | 6.48 (10:05 iex) | +77.0% | 3.66 | 5.06 / 4.98-6.81 | 0.53 (14.5%) | 0.78-4.54 | +171.1% / +215.0% | +183.7% | 18.7M |
| APLX | 8.05 (10:04 iex) | +20.0% | 6.71 | 7.28 / 7.21-8.05 | 0.93 (13.9%) | 6.39-10.18 | -17.0% / -28.1% | -21.4% | 2.1M |
| CRDU | 12.51 (10:04 iex) | +19.5% | 10.47 | 10.95 / 10.63-12.51 | 1.04 (10.0%) | 5.47-11.07 | +33.7% / -12.9% | +13.1% | 7.2M |
| NXL | 5.48 (09:49 iex) | -27.4% | 7.55 | 5.63 / 5.29-5.85 | 0.92 (12.1%) | 4.00-10.98 | +54.7% / -5.5% | +73.4% | 3.1M |
| WDCX | 14.38 (10:05 iex) | -19.8% | 17.92 | 14.85 / 14.21-15.21 | 1.76 (9.8%) | 14.08-21.01 | +3.7% / -8.0% | +4.8% | 1.4M |
| IREZ | 8.47 (10:05 iex) | -14.4% | 9.89 | 9.32 / 8.54-9.45 | 0.96 (9.7%) | 6.82-11.66 | +13.2% / -21.6% | +27.0% | 3.1M |
