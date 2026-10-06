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

# Pre-market brief: Tuesday 2026-10-06 (09:05 ET / 15:05 Stockholm)

### 1. Tape
Monday was a record session for the Nasdaq Composite (+1.05% to 27,477.31). The S&P 500 rose 0.66% to 7,773.95, the Dow 0.18% and the Russell 2000 0.50% (verified: Investrade/TheStreet). This morning futures are up again: Nasdaq-100 +0.4/0.5%, S&P +0.25/0.4%, Dow +0.4/0.5%. SPY is 777.28 and QQQ 760.08, both above their 20-day highs (table).

The strange part of the picture is rates. Yahoo reports the 10-year near 5.27–5.31%, a 24-year closing high, and the 30-year at 5.66%. Equities are ignoring it because of AI momentum (NVDA, plus strong numbers from Foxconn) and falling oil. WTI is −2.4% to about $87.3 and Brent about $98. G7 agreed to release 100M barrels from reserves, with diesel front-loaded into the first 20 days, and Gulf exports are recovering. USO (141.65) is trading below its 20-day low.

The regime is a narrow, tech-led risk-on rally with rotation out of energy. The long side has the edge in mega-cap tech and cyclicals. The short side has the edge in energy and in rate-sensitive defensives.

### 2. Calendar
Stockholm is on CEST until Oct 25, so it is ET +6h.

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:15 | 14:15 | ADP weekly | Released. I could not verify the figure | all |
| 08:30 | 14:30 | Trade balance, Aug | **−$105.6B vs −$100.8B expected.** Advance goods −$132.6B vs −$115B, the widest since Mar 2025. Futures barely moved | GDP-tracking noise; nothing in the book |
| Day | – | Fed: Williams, Bowman, Cook, Schmid (times not verified) | Williams: "no need for urgency", one more hike late this year possible. Market prices ~20% odds of an October hike | IWM, all longs |
| 13:00 | 19:00 | $58B 3-year auction | – | IWM, rate-sensitive names |
| 16:30 | 22:30 | API crude inventories | – | XLE short (proposed) |
| After close | – | STZ, others | – | none held |

Both FOMC minutes and PEP (Thursday) fall inside the horizon. Under rule 8 they are ambient risk, not binary events for my names.

### 3. Open positions and resting entries
- **NVDA long** (236.40 entry, last 241.05): thesis **intact**. Momentum leader, trading through its 20-day high of 240.10. **Raise stop 227.40 → 233.00.** That is below the 234.50 breakout pivot and ~1.5 ATR under the current price, so if the breakout fails I am out near break-even, not down 1R. Target stays at 246.
- **MSFT long** (527.65, last 530.00): **intact**, at the 532.35 top of its 20-day range. **Raise stop 510 → 515.00**, ~1.2 ATR below the price and under the 522.85 breakout level. Target stays at 548.
- **IWM long** (281.50, last 284.22): **intact but weak**. Small caps are lagging the record tape with the 10-year at 5.3%; the 3-year auction is today's test. The 276.90 stop is above the 20-day low of 275.45. **Hold, no change.**
- **JNJ short** (254.46, last 253.20): **intact**. Sitting on the 20-day low of 252.51, −7% in 5 days. Earnings are 10/13, outside the horizon. **Hold, no change.**
- **WMT short** (103.40, last 104.85): **weakening**. It is −1.3% against me and 0.75 below the stop, and staples have stopped falling on a risk-on tape. The stop at 105.60 is the original invalidation, so I leave it there and do not widen it.
- No resting entries.

### 4. New plays

**XLE short (sell stop)**

| Field | Value |
|---|---|
| Ticker | XLE |
| Direction | Short |
| Catalyst | 2026-10-06: WTI −2.4% to ~$87.3 after the G7 100M bbl release (diesel front-loaded over 20 days) and Gulf exports recovering. USO is already below its 20-day low |
| Thesis | Energy is the one sector still above its 50-day average (+2.5%) while the oil premium unwinds. Equities lag crude on the way down, so XLE should follow USO toward its 60.95 20-day low and below |
| Entry | Sell stop 62.20 (pre-market 62.90, so the trigger is valid) |
| Stop | 64.10: above the 63.45 prior close plus ~0.5 buffer, 1.55 ATR from entry |
| Target | 59.60, below the 20-day low of 60.95. 1.37R |
| Risk tier | 0.5. Houthi/Saudi headline gap risk is real |
| Time horizon | 1–5 days |
| Conviction | 3 |
| P(target before stop) | 37% |
| Invalidation | Brent reclaims $100, or a new attack on Gulf supply |
| What I'd be wrong about | Oil has already fallen ~$15 from its highs and the release is priced. One Hormuz headline reverses the whole move overnight |

Reasoning: this is the cleanest short on today's tape. The catalyst is dated and physical, and the stop entry only engages if the selling carries into equities. I passed on a CVX short at the 20-day low on 9/29 for location reasons. This entry sits mid-range with room to the 20-day low.

**CAT long (buy stop, probe)**

| Field | Value |
|---|---|
| Ticker | CAT |
| Direction | Long |
| Catalyst | 2026-10-06: CAT +0.9% pre-market to 855.51, against its 20-day high of 858.87, on a record-setting cyclical/AI-capex tape |
| Thesis | Industrial momentum name (+4.3% vs 20-day average) with data-center power exposure. A break above 858.87 clears a one-month ceiling |
| Entry | Buy stop 860.00 |
| Stop | 836.00: back below Monday's 848 close and inside the old range, ~1.1 ATR from entry |
| Target | 896.00. 1.5R |
| Risk tier | 0.25. Probe: a cyclical breakout while the 10-year is at 5.3% is not a clean setup |
| Time horizon | 1–5 days |
| Conviction | 2 |
| P(target before stop) | 36% |
| Invalidation | Breaks out, then closes back under 850 |
| What I'd be wrong about | Breakouts in this account have failed often. A rate shock from the auction or Fed speakers hits cyclicals first. One source says CAT's all-time high was 1,062 in June, which conflicts with the table's 50-day average (~822). **I could not verify it** and am not relying on it |

### 5. Both sides
- **Best long:** AMD at 643.47 (+1.9% pre-market, 20-day high 645.46, +22.5% vs 50-day average). Levels: buy stop 647, stop 618, target 690, P 40%. **Passed.** Tech is already ~35% of equity through MSFT and NVDA, against the 40% sector cap, so there is no room. CAT is the long I'm taking instead.
- **Best short:** XLE, sell stop 62.20, stop 64.10, target 59.60, P 37%. **Taken.**

### 6. Passing on
- **AMD long:** sector cap (above).
- **DAL long** (84.08, falling oil helps airlines): same oil factor as the XLE short, and I lost on DAL last week. Buy stop 86.30, stop 82.40, target 91, P 35%.
- **GS short** (900, 20-day low 881, −10.5% vs 50-day average): bank earnings start around 10/14, right at the edge of the horizon, and financials are bouncing pre-market. Sell stop 879, stop 915, target 835, P 34%.

### 7. For the post-open review
- **XLE:** if it opens below 62.20, the stop entry fills at the open. If that fill is below 61.70, the stop is too far away, so tighten it to 63.60.
- **CAT:** if it gaps above 866, cancel the entry. The fill would be too extended over the pivot.
- **WMT:** if it trades above 105.30 at 10:00 while XLP is green, close it rather than waiting for the 105.60 stop.
- **IWM:** hold through the 13:00 auction. No action at the review unless it trades below 279.

### 8. Book state
With both new entries resting and both counted as filled, slots are 7/8. Risk at stake falls to ~2.0% after the NVDA and MSFT stop raises and rises by 0.75% from the new plays: about 2.8% of 4%. Gross is ~119% of 150% if both fill. Net is about +34% (CAT adds ~10%, XLE subtracts ~16%). Tech stays ~35% of the 40% sector cap.

```json
{
  "date": "2026-10-06",
  "no_trade": false,
  "session_note": "Tech-led record tape despite 10y ~5.3%; oil -2.4% on G7 reserve release. Short energy breakdown, probe CAT breakout, tighten tech stops.",
  "plays": [
    {
      "ticker": "XLE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 62.20,
      "stop": 64.10,
      "targets": [59.60],
      "time_horizon": "1-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.37,
      "catalyst": "2026-10-06 WTI -2.4% to ~$87 after G7 100M bbl reserve release (diesel front-loaded) and recovering Gulf exports; USO below its 20d low.",
      "thesis": "Energy is the only sector still above its 50d avg while the oil premium unwinds. XLE should follow crude toward and through its 60.95 20d low.",
      "invalidation": "Brent reclaims $100 or a fresh Gulf supply disruption.",
      "bear_case": "Oil already well off highs and the release is priced; one Hormuz/Houthi headline reverses it overnight."
    },
    {
      "ticker": "CAT",
      "direction": "long",
      "entry_type": "stop",
      "entry": 860.00,
      "stop": 836.00,
      "targets": [896.00],
      "time_horizon": "1-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.36,
      "catalyst": "2026-10-06 CAT +0.9% pre-market to 855.5 against its 858.87 20d high on a record risk-on tape.",
      "thesis": "Industrial momentum leader with data-center power exposure; a break of the one-month ceiling at 858.87 opens a measured move toward 896.",
      "invalidation": "Breaks out then closes back under 850.",
      "bear_case": "10y at a 24-year high hits cyclicals first; breakouts have failed often in this account."
    }
  ],
  "manage": [
    {
      "ticker": "NVDA",
      "action": "update",
      "stop": 233.00,
      "reason": "Breakout through 20d high holding; stop moved under the 234.50 pivot to cut risk to near break-even."
    },
    {
      "ticker": "MSFT",
      "action": "update",
      "stop": 515.00,
      "reason": "At top of 20d range; stop raised under the 522.85 breakout level with ~1.2 ATR buffer to reduce risk."
    }
  ],
  "passed": [
    {
      "ticker": "AMD",
      "direction": "long",
      "entry_type": "stop",
      "entry": 647.00,
      "stop": 618.00,
      "targets": [690.00],
      "p_target_first": 0.40,
      "reason": "Best long on the tape, but tech is ~35% of equity against the 40% sector cap."
    },
    {
      "ticker": "DAL",
      "direction": "long",
      "entry_type": "stop",
      "entry": 86.30,
      "stop": 82.40,
      "targets": [91.00],
      "p_target_first": 0.35,
      "reason": "Same falling-oil factor as the XLE short; one oil bet is enough."
    },
    {
      "ticker": "GS",
      "direction": "short",
      "entry_type": "stop",
      "entry": 879.00,
      "stop": 915.00,
      "targets": [835.00],
      "p_target_first": 0.34,
      "reason": "Bank earnings around 10/14 at the edge of the horizon; financials bouncing pre-market."
    }
  ]
}
```

Sources: [Yahoo Finance live Oct 6](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-october-6-dow-sp-500-nasdaq-080526166.html), [TheStreet Oct 6](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-06-2026), [Investrade morning preview](https://investrade.com/morning-preview-october-06-2026/), [CNBC Oct 5](https://www.cnbc.com/2026/10/04/stock-market-today-live-updates.html), [investingLive goods trade](https://investinglive.com/news/us-advance-goods-trade-balance-for-august-132-6-billion-vs-115-00-billion-expected/), [Trading Economics trade balance](https://tradingeconomics.com/united-states/balance-of-trade), [Yahoo G7 oil release](https://finance.yahoo.com/energy/articles/oil-slips-g7-agrees-release-140827505.html), [Trading Economics crude](https://tradingeconomics.com/commodity/crude-oil), [Yahoo Fed October hike odds](https://finance.yahoo.com/economy/policy/articles/fed-may-time-next-interest-173209828.html), [Trading Economics yields](https://tradingeconomics.com/united-states/government-bond-yield/news/509638), [Fool CAT](https://www.fool.com/investing/2026/10/03/caterpillar-trades-above-800-heres-why-it-could-be/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Tuesday 2026-10-06. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$102,701.26**
- Cash: $51,591.64
- Session P&L so far: +0.62% (new entries are blocked at -3.0%)
- Gross exposure: $117,803 (115% of equity, cap 150%)
- Net exposure: $+34,378 (+33%, cap +/-100%)
- Risk at stake (entry to stop): $2,500 (2.43% of equity, cap 4.0%) — 1.57% left for new plays
- Slots: 5 open + 1 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 35% of equity in notional: at 1% risk its stop must be at least 2.8% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 35% of equity in notional: at 1% risk its stop must be at least 2.8% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| CAT | long | 10 | 861.00 | 873.18 | +122 (+1.4%) | 836.00 | 896.00 | Industrial momentum leader with data-center power exposure; a break of the one-month ceiling at 858.87 opens a measured  |
| IWM | long | 111 | 281.50 | 283.52 | +224 (+0.7%) | 276.90 | 289.50 | Small caps are the most rate-damaged group (-4.5% vs 50d) and the most direct beneficiary of a rates reversal. A limit h |
| JNJ | short | 99 | 254.46 | 252.33 | +211 (+0.8%) | 259.90 | 247.10 | Defensive under rate pressure with persistent relative weakness (Stelara biosimilar overhang). A break of the 20d low op |
| MSFT | long | 36 | 527.65 | 533.03 | +194 (+1.0%) | 515.00 | 548.00 | MSFT is +3.2% vs 20d and +6.2% vs 50d and has held up under higher rates. A break of 522.85 clears a three-week ceiling  |
| NVDA | long | 69 | 236.40 | 242.01 | +387 (+2.4%) | 233.00 | 246.00 | Only mega-cap with a dated positive catalyst and green on a red tape. A break through the 20d high of 234.50 means range |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XLE | short | 269 | 62.20 | stop | 64.10 | 59.60 | 2026-10-06 |

### Record

11 closed trades: 4W / 7L, total -0.62R, net $+1,567 realized. Shorts taken: 11.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| WMT | short | stop | -1.00R | $-254 | 34% |
| UNH | short | stop | -1.01R | $-253 | 36% |
| DAL | long | close | -0.53R | $-291 | 42% |
| XLRE | short | stop | -1.01R | $-529 | 40% |
| BAC | short | target | +1.53R | $+774 | 36% |

### Ideas you passed on, replayed against the tape

9 resolved: 2 reached target first, 6 stop first, 1 never reached the entry, 0 expired, 0 ambiguous. Average -0.33R across the 8 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-09-29 pre-market | CVX | short | Pure Iran-headline trade sitting at the 20d low; wrong location. | never filled | - | 38% |
| 2026-10-02 pre-market | XHB | long | Same rate-relief factor as the IWM long, already +2.4% pre-market; one rates lon | stop | -1.00R | 38% |
| 2026-10-02 open | XHB | long | Faded from 98.73 open to 97.67; same rate factor as the resting IWM limit. | stop | -0.98R | 38% |
| 2026-09-30 pre-market | TSLA | short | Best short: break of 20d low 349.92, but Q3 deliveries (~Oct 2) are a company bi | stop | -1.00R | 38% |
| 2026-10-01 pre-market | KRE | short | Same rates factor as BAC short already held; no slot. | stop | -1.00R | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| CAT | 873.57 (10:04 iex) | +3.0% | 848.14 | 853.00 / 851.47-875.90 | 22.26 (2.6%) | 772.86-858.87 | +4.3% / +3.1% | +3.4% | 2.3M |
| IWM | 283.53 (10:05 iex) | +0.1% | 283.38 | 284.40 / 283.18-284.64 | 3.85 (1.4%) | 275.45-295.33 | -0.3% / -2.9% | +1.2% | 24.7M |
| JNJ | 252.38 (10:04 iex) | -0.2% | 252.93 | 254.15 / 252.20-254.15 | 4.67 (1.8%) | 252.51-275.23 | -5.1% / -4.6% | -7.0% | 6.9M |
| MSFT | 532.99 (10:05 iex) | +1.5% | 525.18 | 531.68 / 528.78-534.39 | 12.17 (2.3%) | 486.00-532.35 | +4.4% / +7.1% | +3.1% | 21.8M |
| NVDA | 242.04 (10:05 iex) | +1.3% | 238.90 | 242.10 / 240.76-243.37 | 5.38 (2.3%) | 208.93-240.10 | +6.6% / +9.2% | +4.4% | 111.0M |
| XLE | 63.26 (10:05 iex) | -0.3% | 63.45 | 62.97 / 62.93-63.43 | 1.23 (1.9%) | 60.95-65.78 | +0.3% / +2.5% | +2.2% | 34.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 780.00 (10:05 iex) | +0.7% | 774.83 | 778.16 / 777.96-780.16 | 7.28 (0.9%) | 747.74-776.61 | +1.4% / +1.6% | +1.2% | 46.7M |
| QQQ | 761.38 (10:05 iex) | +0.7% | 756.20 | 760.50 / 759.10-761.70 | 9.96 (1.3%) | 699.27-756.92 | +3.7% / +5.4% | +2.7% | 33.7M |
| IWM | 283.53 (10:05 iex) | +0.1% | 283.38 | 284.40 / 283.18-284.64 | 3.85 (1.4%) | 275.45-295.33 | -0.3% / -2.9% | +1.2% | 24.7M |
| DIA | 515.27 (10:04 iex) | +0.6% | 512.11 | 514.31 / 513.49-515.64 | 5.17 (1.0%) | 504.70-529.17 | -0.9% / -2.5% | -0.4% | 3.5M |
| TLT | 77.14 (10:04 iex) | +0.0% | 77.11 | 77.17 / 77.08-77.22 | 0.88 (1.1%) | 76.69-82.13 | -3.3% / -4.9% | -1.5% | 49.4M |
| GLD | 380.98 (10:05 iex) | +0.4% | 379.55 | 381.46 / 380.65-381.79 | 6.62 (1.7%) | 376.88-406.56 | -3.1% / -4.3% | +0.4% | 8.5M |
| USO | 141.98 (10:04 iex) | -1.4% | 143.99 | 142.32 / 141.80-142.32 | 5.79 (4.0%) | 142.07-163.35 | -4.5% / +4.7% | -4.0% | 6.6M |
| SMH | 638.69 (10:05 iex) | +0.8% | 633.90 | 638.38 / 635.17-639.47 | 14.53 (2.3%) | 537.73-636.25 | +7.9% / +11.0% | +5.6% | 6.2M |
| XLK | 202.87 (10:05 iex) | +1.0% | 200.93 | 202.48 / 201.89-203.01 | 3.04 (1.5%) | 181.87-201.39 | +4.7% / +7.7% | +3.3% | 7.4M |
| XLF | 54.22 (10:05 iex) | +0.6% | 53.88 | 54.04 / 53.91-54.27 | 0.76 (1.4%) | 52.81-57.62 | -2.5% / -4.8% | -0.6% | 38.1M |
| XLE | 63.26 (10:05 iex) | -0.3% | 63.45 | 62.97 / 62.93-63.43 | 1.23 (1.9%) | 60.95-65.78 | +0.3% / +2.5% | +2.2% | 34.8M |
| XLV | 167.91 (10:04 iex) | +0.3% | 167.37 | 168.00 / 167.78-169.03 | 2.25 (1.3%) | 164.48-171.87 | -0.3% / -0.5% | -2.3% | 8.2M |
| XLI | 172.20 (10:04 iex) | +1.2% | 170.10 | 170.70 / 170.26-172.24 | 2.30 (1.4%) | 166.18-175.24 | +0.2% / -3.5% | +0.8% | 7.5M |
| XLY | 111.14 (10:05 iex) | +0.7% | 110.42 | 110.84 / 110.65-111.28 | 1.49 (1.3%) | 107.99-114.38 | -0.4% / -3.3% | +1.3% | 6.8M |
| XLP | 81.42 (10:04 iex) | +0.5% | 81.04 | 81.07 / 81.03-81.45 | 0.88 (1.1%) | 80.10-84.33 | -1.4% / -3.4% | -1.5% | 11.0M |
| XLU | 40.69 (10:05 iex) | +1.8% | 39.97 | 40.39 / 40.39-40.92 | 0.55 (1.4%) | 39.03-43.39 | -1.7% / -5.5% | +1.8% | 30.6M |
| XLB | 49.55 (10:05 iex) | +0.1% | 49.50 | 49.55 / 49.45-49.76 | 0.79 (1.6%) | 47.81-52.34 | -0.9% / -3.6% | +0.1% | 11.8M |
| XLRE | 41.13 (10:04 iex) | +1.1% | 40.67 | 40.80 / 40.74-41.13 | 0.52 (1.3%) | 40.41-43.89 | -3.3% / -6.6% | -1.6% | 6.2M |
| XLC | 111.51 (10:04 iex) | -0.1% | 111.61 | 111.98 / 111.09-112.03 | 1.88 (1.7%) | 109.66-115.61 | -0.4% / +0.3% | +0.4% | 6.1M |
| KRE | 70.85 (10:05 iex) | +0.7% | 70.39 | 70.61 / 70.44-70.90 | 1.32 (1.9%) | 67.97-74.82 | -1.9% / -4.8% | -0.2% | 15.2M |
| XHB | 97.39 (10:04 iex) | +1.1% | 96.30 | 96.70 / 96.57-97.39 | 2.18 (2.3%) | 94.08-102.45 | -1.0% / -6.0% | -1.0% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 332.12 (10:05 iex) | -0.2% | 332.89 | 332.40 / 330.63-333.68 | 6.49 (1.9%) | 309.90-345.34 | +0.1% / +3.3% | -1.6% | 42.1M |
| MSFT | 532.99 (10:05 iex) | +1.5% | 525.18 | 531.68 / 528.78-534.39 | 12.17 (2.3%) | 486.00-532.35 | +4.4% / +7.1% | +3.1% | 21.8M |
| NVDA | 242.04 (10:05 iex) | +1.3% | 238.90 | 242.10 / 240.76-243.37 | 5.38 (2.3%) | 208.93-240.10 | +6.6% / +9.2% | +4.4% | 111.0M |
| AMZN | 252.66 (10:04 iex) | +0.5% | 251.40 | 253.40 / 251.08-253.70 | 5.23 (2.1%) | 244.30-259.49 | +0.0% / -2.2% | +2.1% | 35.6M |
| GOOGL | 345.57 (10:05 iex) | -0.3% | 346.47 | 347.37 / 344.69-348.09 | 9.10 (2.6%) | 327.74-364.17 | +1.0% / +0.5% | +1.1% | 27.7M |
| META | 739.29 (10:05 iex) | -0.4% | 741.90 | 746.73 / 736.83-747.60 | 28.69 (3.9%) | 609.26-779.82 | +5.7% / +18.2% | +3.7% | 23.7M |
| TSLA | 380.12 (10:05 iex) | +0.4% | 378.73 | 381.98 / 378.52-383.33 | 12.06 (3.2%) | 345.88-386.83 | +3.5% / +8.6% | +6.0% | 37.2M |
| AVGO | 373.56 (10:05 iex) | +3.0% | 362.51 | 366.91 / 364.01-373.19 | 9.91 (2.7%) | 335.20-372.02 | +2.4% / -2.6% | +3.7% | 24.5M |
| AMD | 644.19 (10:05 iex) | +2.0% | 631.75 | 648.00 / 628.00-649.88 | 24.79 (3.9%) | 480.33-645.46 | +10.0% / +22.5% | +3.9% | 22.4M |
| ORCL | 145.16 (10:04 iex) | +1.9% | 142.48 | 143.93 / 143.86-146.12 | 6.30 (4.4%) | 131.58-170.70 | -1.9% / -1.2% | +7.5% | 35.9M |
| NFLX | 67.56 (10:05 iex) | +0.1% | 67.50 | 67.46 / 67.34-67.94 | 1.81 (2.7%) | 66.54-81.02 | -7.5% / -10.6% | -2.5% | 35.6M |
| CRM | 229.41 (10:04 iex) | -0.2% | 229.79 | 231.75 / 228.10-233.00 | 7.88 (3.4%) | 221.18-261.87 | -4.1% / +3.9% | +1.1% | 11.9M |
| JPM | 333.09 (10:04 iex) | +0.7% | 330.73 | 332.73 / 331.07-333.63 | 6.41 (1.9%) | 324.25-358.26 | -3.4% / -5.5% | -1.3% | 8.4M |
| GS | 902.52 (10:03 iex) | +1.0% | 893.46 | 901.57 / 896.00-903.28 | 23.17 (2.6%) | 881.00-1,043.84 | -6.2% / -10.5% | -2.5% | 2.2M |
| BAC | 54.24 (10:05 iex) | +0.5% | 54.00 | 54.27 / 53.88-54.41 | 1.08 (2.0%) | 52.89-63.83 | -6.3% / -10.8% | -2.7% | 39.3M |
| XOM | 163.97 (10:04 iex) | -0.0% | 164.00 | 163.06 / 162.94-164.10 | 3.50 (2.1%) | 155.85-169.64 | +0.6% / +2.3% | +0.9% | 13.9M |
| CVX | 206.01 (10:04 iex) | -0.2% | 206.47 | 205.56 / 204.89-206.63 | 4.15 (2.0%) | 200.78-217.78 | -1.0% / +2.1% | +0.0% | 9.9M |
| LLY | 1,163.57 (10:04 iex) | +1.8% | 1,143.12 | 1,147.15 / 1,144.00-1,176.66 | 30.97 (2.7%) | 1,113.29-1,215.00 | -0.7% / -2.7% | -3.5% | 2.3M |
| UNH | 378.49 (10:04 iex) | -0.0% | 378.58 | 379.03 / 377.78-380.39 | 7.54 (2.0%) | 362.60-404.04 | +0.3% / -3.2% | +0.2% | 5.1M |
| JNJ | 252.38 (10:04 iex) | -0.2% | 252.93 | 254.15 / 252.20-254.15 | 4.67 (1.8%) | 252.51-275.23 | -5.1% / -4.6% | -7.0% | 6.9M |
| WMT | 105.50 (10:05 iex) | +0.4% | 105.07 | 104.50 / 104.50-105.86 | 2.08 (2.0%) | 103.39-111.23 | -1.8% / -3.3% | -3.4% | 22.3M |
| COST | 926.38 (10:04 iex) | +0.3% | 923.52 | 921.32 / 919.00-928.33 | 14.54 (1.6%) | 883.10-931.09 | +1.7% / -1.0% | +0.1% | 2.4M |
| HD | 284.53 (10:05 iex) | +1.2% | 281.15 | 283.23 / 282.13-284.96 | 6.43 (2.3%) | 277.15-321.50 | -5.6% / -12.2% | -3.0% | 5.2M |
| CAT | 873.57 (10:04 iex) | +3.0% | 848.14 | 853.00 / 851.47-875.90 | 22.26 (2.6%) | 772.86-858.87 | +4.3% / +3.1% | +3.4% | 2.3M |
| BA | 190.73 (10:05 iex) | -1.0% | 192.72 | 193.00 / 190.51-193.22 | 7.19 (3.7%) | 184.01-215.29 | -3.2% / -9.1% | +4.5% | 8.6M |
| DAL | 85.21 (10:04 iex) | +2.6% | 83.08 | 84.24 / 83.94-85.75 | 2.47 (3.0%) | 76.89-86.17 | +1.9% / -1.1% | -1.1% | 7.5M |
| UAL | 113.97 (10:04 iex) | +3.6% | 110.00 | 111.86 / 110.93-115.20 | 4.04 (3.7%) | 104.59-118.26 | -0.2% / -4.9% | -1.4% | 4.0M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-06 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| IPDN | 5.68 (10:04 iex) | +83.2% | 3.10 | 6.28 / 5.14-6.78 | 1.00 (32.3%) | 2.95-7.70 | -15.8% / -49.2% | -20.3% | 3.2M |
| APUS | 6.31 (10:04 iex) | +37.5% | 4.59 | 4.91 / 4.71-6.64 | 1.53 (33.4%) | 1.51-9.14 | +43.6% / +15.1% | -28.2% | 8.2M |
| JAGX | 6.31 (10:03 iex) | +33.4% | 4.73 | 6.56 / 6.03-6.93 | 6.04 (127.6%) | 2.35-41.53 | -25.7% / -54.9% | -21.4% | 4.9M |
| OPCH | 31.03 (10:05 iex) | +32.8% | 23.37 | 31.04 / 31.00-31.08 | 0.72 (3.1%) | 22.29-24.88 | -0.4% / -0.8% | +2.1% | 2.2M |
| ASTX | 11.37 (10:03 iex) | +20.8% | 9.41 | 9.91 / 9.88-11.40 | 1.28 (13.6%) | 8.48-12.88 | -8.2% / -19.0% | -8.6% | 4.1M |
| LABX | 18.58 (09:59 iex) | +19.2% | 15.59 | 16.74 / 16.34-18.77 | 1.69 (10.8%) | 7.80-16.96 | +22.0% / +26.3% | +5.6% | 1.3M |
| MVLL | 44.52 (10:04 iex) | +18.2% | 37.66 | 37.53 / 36.60-45.89 | 3.11 (8.3%) | 23.80-40.07 | +17.1% / +32.7% | +15.3% | 2.4M |
| XRPN | 19.20 (10:05 iex) | -50.3% | 38.65 | 22.51 / 17.22-23.60 | 4.94 (12.8%) | 10.51-53.00 | +167.4% / +220.0% | +265.5% | 1.3M |
| SAIQ | 5.04 (09:51 iex) | -24.4% | 6.67 | 5.42 / 4.76-5.46 | 1.89 (28.4%) | 1.76-12.95 | -28.3% / -34.2% | -37.3% | 3.5M |
