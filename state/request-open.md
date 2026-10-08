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

## Pre-market brief: Thursday 2026-10-08 (09:05 ET / 15:05 Stockholm)

### 1. Tape
Oil is behind the move. Brent is about $105 and WTI about $92.75, both up roughly 5%. Behind it: the US military has been told to prepare Iran contingency options, a tanker north of Qatar was hit by projectiles, and Houthi attacks on Saudi infrastructure continue. Yields are back toward the highs: the 10-year is 5.28–5.35% depending on the source and the 30-year about 5.66–5.70%. Yesterday's FOMC minutes read as hawkish and unanimous behind the September hike. Index futures are down 0.5–1.0%. In the Alpaca table, SPY is 774.11 (−0.4%), QQQ −0.6%, IWM 275.59 (−0.8%, at its 20-day low of 275.45), SMH −1.6%, USO +3.7%, XLE +1.9% and XLP +0.4%. The regime is stagflation risk-off on top of indices near record highs: energy and defensives lead, while rate-sensitives and semis lag. **The edge today is short rates/duration and long energy/defensives.**

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Initial jobless claims | **197K, matching the 197K reported in the Yahoo live blog** (one preview had 200K). No market reaction; oil is driving the tape | All |
| pre-mkt | — | PEP Q3 | Revenue $25.27B vs $25.0B expected, but profit outlook lowered | XLP context |
| 10:00 | 16:00 | Wholesale inventories (Aug) | Consensus +0.7% | Minor |
| 10:30 | 16:30 | EIA natural gas storage | — | XOM, minor |
| 13:00 | 19:00 | $22B 30-year bond auction | Prior yield 5.308% | TLT short, HD, MSFT/NVDA via rates |
| TBD | — | Fed's Waller, "Economic Outlook" (Istanbul) | Time not verified | Rates |
| Tomorrow pre-mkt | — | DAL Q3 (consensus EPS about $1.83 per Alphastreet) | — | Airlines; the reason UAL is passed |

### 3. Open positions and resting entries
- **IWM long (281.50, stop 276.90): thesis invalidated. Close.** The trade was a bet on rates reversing lower. Instead the 10-year is back toward 5.35% on an oil shock, and IWM is 275.59 pre-market, already below the stop and on its 20-day low. The stop would fire at the open anyway. I am closing it explicitly because the thesis is dead, not because of the stop. Expected result about −1.2R, worse than −1R because of the gap.
- **MSFT long (527.65, stop 515, target 548): intact. Hold.** It is 528.91 (−0.2%), still above the 522.85 breakout, and holding up better than QQQ. No change.
- **NVDA long (236.40, stop 233, target 246): weakening. Hold.** It is 235.31 with SMH −1.6%. The stop is 2.3 away, about 0.45 ATR, so a semis flush could take it. I am not widening it. The trade was sized to that stop, and if it goes, it goes.
- **XOM resting buy stop 169.80 (stop 163.50, target 179): keep.** Pre-market is 167.60 (+2.2%) and the 20-day high is 169.64. Oil +5% is exactly the condition this order was waiting for. If XOM gaps through the trigger at the open, it fills there, which is acceptable.
- **HD resting sell stop 276.90 (stop 287.50, target 260): keep.** HD is 284.09 and the 20-day low is 277.15. Rising yields support the thesis, and the trigger is well below the market.

### 4. New plays

**COST long**
| Field | Value |
|---|---|
| Ticker | COST |
| Direction | Long |
| Catalyst | 2026-10-07 after the close: September comparable sales +11.4% (US +12.5%), +7.6% excluding gas and FX; e-commerce +19%. Pre-market is 950.82 (+0.9%), above the 948.58 20-day high |
| Thesis | Defensive quality with a fresh fundamental beat, breaking out while the tape rotates away from rate and growth risk. A stagflation tape favours staples with pricing power, and COST benefits from higher gas prices through its fuel sales. A confirmed break above 956 should extend toward 990–995 |
| Entry | Buy stop at 956.00 |
| Stop | 931.00 (−2.6%, about 1.6 ATR). That is back inside the old range and below yesterday's close of 942.25 by a margin, so the breakout would have failed |
| Target | 995.00 (+1.56R) |
| Risk tier | 0.5. A breakout entry in an expensive name, and the September comp excluding gas showed a slowing trend before this print |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 38% |
| Invalidation | It fills and then closes back under 948, or XLP turns red while the S&P falls |
| What I'd be wrong about | Comps had slowed three months in a row before September. The headline is flattered by gas prices and the Labor Day shift (+50bp). At about 50× earnings, a 7.6% underlying comp may already be priced in, and Truist's "Hold" says as much |

Reasoning: this is the cleanest long on a day when growth and rates are both hit. Relative strength comes with a dated catalyst. Using a buy stop rather than a market order means I only own it if buyers confirm above the pre-market high.

**TLT short**
| Field | Value |
|---|---|
| Ticker | TLT |
| Direction | Short |
| Catalyst | Oil +5% on 2026-10-08 brings back inflation risk; the minutes were hawkish (10/07); a $22B 30-year auction is at 13:00 ET today |
| Thesis | Long duration is in a confirmed downtrend (−4.5% vs the 50-day). An oil-led inflation scare with a hawkish Fed gives no reason for a bid. A break of the 76.43 20-day low opens the way to 73.50 |
| Entry | Sell stop at 76.35. Pre-market is 76.91, so the trigger is valid |
| Stop | 77.95 (+2.1%, about 1.9 ATR). That is above the recent consolidation, and a reclaim of it would mean the breakdown has failed |
| Target | 73.50 (+1.78R) |
| Risk tier | 0.5. TLT is near multi-decade yield highs, where short squeezes are violent, and the auction is a two-way event |
| Time horizon | 1–5 days |
| Conviction | 2 |
| P(target before stop) | 36% |
| Invalidation | De-escalation with Iran sending Brent back under $97, or a strong 30-year auction (stop-through) with TLT closing back above 77.50 |
| What I'd be wrong about | Yields at 2002 highs attract real-money buyers. An oil shock can turn into a growth scare that bids duration. And I am already short rates through the HD resting order |

Reasoning: with IWM closed, the book no longer holds a rates long that this trade would offset. Yesterday's TLT pass, which was declined for exactly that conflict, no longer applies. HD may never fill, and TLT is the purer way to express the view.

### 5. Both sides
- **Best long:** COST, buy stop 956, stop 931, target 995, P 38%. **Taken** (0.5).
- **Best short:** TLT, sell stop 76.35, stop 77.95, target 73.50, P 36%. **Taken** (0.5).
- **Shorts I also looked at:** UAL (direct oil-cost victim, −2.5% pre-market), XLRE (at its 20-day low), SMH (−1.6%). See section 6.

### 6. Passing on
- **UAL short** (107.45; sell stop 104.40, stop 110.50, target 97.00, P 33%): the oil thesis is right, but DAL reports tomorrow before the open. Delta's last few prints lifted the group, and that is a gap risk I cannot bracket.
- **XLRE short** (40.44; sell stop 40.30, stop 41.40, target 38.60, P 33%): same rates factor as TLT and HD. Three rates shorts is too many.
- **SMH short:** counter-trend against a strong uptrend (+8.7% vs the 50-day), and it would hedge my own NVDA/MSFT in a muddled way. No levels logged.
- **CVX long:** duplicates the XOM resting order. One energy breakout is enough.
- **Bank shorts (GS/BAC/KRE):** their own earnings start 10/13, inside the horizon (rule 8).

### 7. For the post-open review
- **IWM:** confirm it is flat. If the close somehow did not execute and the position is still open, close it.
- **COST:** if it triggers at the open and is back under 948 by 10:05, close it, because the breakout failed. If it opens under 948, leave the order resting.
- **XOM:** if it gaps through 169.80 and fills, then fades under 167 by 10:05 while Brent stays above $102, hold; the stop is at 163.50. If Brent has reversed under $100 by then, close.
- **NVDA:** if SMH is below −2.5% at 10:05 and NVDA is under 234, close rather than wait for the 233 stop. No action otherwise.
- **TLT:** no action before the 13:00 auction. The bracket handles it.

### 8. Book state
After closing IWM and if every entry fills: gross about 98% (cap 150%), net about +24% (cap ±100%), 6 of 8 slots. Risk at stake about 2.45% of equity (cap 4%). Tech is about 35% of equity (cap 40%). Session P&L is −0.39%, so the loss block is not in play.

```json
{
  "date": "2026-10-08",
  "no_trade": false,
  "session_note": "Stagflation risk-off: Brent ~$105 on Iran/Hormuz escalation, 10y back to ~5.3%. Close invalidated IWM rates long; add half-size TLT breakdown short and half-size COST breakout long on strong September comps; keep XOM/HD triggers.",
  "plays": [
    {
      "ticker": "COST",
      "direction": "long",
      "entry_type": "stop",
      "entry": 956.00,
      "stop": 931.00,
      "targets": [995.00],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "2026-10-07 post-close: September comps +11.4% (US +12.5%, ex-gas/FX +7.6%), e-comm +19%; pre-market 950.82 above the 948.58 20d high.",
      "thesis": "Defensive quality with a fresh fundamental beat breaking out while the tape rotates out of rate and growth risk. A confirmed break above 956 should extend toward 990-995.",
      "invalidation": "Fills then closes back under 948, or XLP turns red with the S&P falling.",
      "bear_case": "Underlying comps had slowed three months running; headline flattered by gas and Labor Day shift; ~50x P/E may already price the print."
    },
    {
      "ticker": "TLT",
      "direction": "short",
      "entry_type": "stop",
      "entry": 76.35,
      "stop": 77.95,
      "targets": [73.50],
      "time_horizon": "1-5 days",
      "conviction": 2,
      "risk_pct": 0.5,
      "p_target_first": 0.36,
      "catalyst": "2026-10-08: oil +5% on Iran escalation reignites inflation risk after hawkish 10/07 minutes; $22B 30y auction 13:00 ET.",
      "thesis": "Duration is in a confirmed downtrend (-4.5% vs 50d); an oil-led inflation scare with a hawkish Fed gives no bid. A break of the 76.43 20d low targets 73.50.",
      "invalidation": "Iran de-escalation with Brent under $97, or a strong 30y auction and a TLT close above 77.50.",
      "bear_case": "Yields at 2002 highs draw real-money buyers; an oil shock can morph into a growth scare that bids duration."
    }
  ],
  "manage": [
    {
      "ticker": "IWM",
      "action": "close",
      "reason": "Rates-reversal thesis invalidated: 10y back toward 5.35% on an oil shock; IWM 275.59 pre-market is already through the 276.90 stop at its 20d low."
    }
  ],
  "passed": [
    {
      "ticker": "UAL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 104.40,
      "stop": 110.50,
      "targets": [97.00],
      "p_target_first": 0.33,
      "reason": "Oil-cost victim, but DAL reports 10/09 pre-market and has lifted the group before; unbracketable gap risk."
    },
    {
      "ticker": "XLRE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 40.30,
      "stop": 41.40,
      "targets": [38.60],
      "p_target_first": 0.33,
      "reason": "Same rates factor as the TLT short and HD resting order; a third rates short is too concentrated."
    }
  ]
}
```

Sources: [Yahoo Finance live, Oct 8](https://finance.yahoo.com/markets/live/stock-market-today-thursday-october-8-dow-sp-500-nasdaq-080537884.html), [Tickmill outlook, Oct 8](https://www.tickmill.com/blog/daily-market-outlook-october-8-2026), [Investrade morning preview](https://investrade.com/morning-preview-october-08-2026/), [StockAnalysis premarket](https://stockanalysis.com/markets/premarket/), [Rio Times, Oct 7](https://www.riotimesonline.com/global-economy-briefing-october-7-2026/), [TheStreet, Oct 7](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-07-2026), [FXStreet 30y auction](https://www.fxstreet.com/economic-calendar/event/ed51610a-f68b-42f7-8cb6-dcb99f2e582e), [Fed calendar, Oct 2026](https://www.federalreserve.gov/newsevents/2026-october.htm), [Costco September sales (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/10/07/3376846/0/en/costco-wholesale-corporation-reports-september-sales-results.html), [Truist on COST (Investing.com)](https://www.investing.com/news/analyst-ratings/truist-reiterates-hold-on-costco-stock-citing-strong-september-sales-93CH-4938252), [Alphastreet DAL preview](https://news.alphastreet.com/delta-air-lines-q3-2026-earnings-preview-october-9-street-expects-1-83-eps/amp/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Thursday 2026-10-08. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$100,215.33**
- Cash: $64,891.18
- Session P&L so far: -0.30% (new entries are blocked at -3.0%)
- Gross exposure: $98,071 (98% of equity, cap 150%)
- Net exposure: $+24,400 (+24%, cap +/-100%)
- Risk at stake (entry to stop): $2,440 (2.43% of equity, cap 4.0%) — 1.57% left for new plays
- Slots: 2 open + 4 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| MSFT | long | 36 | 527.65 | 531.08 | +123 (+0.6%) | 515.00 | 548.00 | MSFT is +3.2% vs 20d and +6.2% vs 50d and has held up under higher rates. A break of 522.85 clears a three-week ceiling  |
| NVDA | long | 69 | 236.40 | 234.85 | -107 (-0.7%) | 233.00 | 246.00 | Only mega-cap with a dated positive catalyst and green on a red tape. A break through the 20d high of 234.50 means range |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| TLT | short | 312 | 76.35 | stop | 77.95 | 73.50 | 2026-10-08 |
| COST | long | 20 | 956.00 | stop | 931.00 | 995.00 | 2026-10-08 |
| XOM | long | 40 | 169.80 | stop | 163.50 | 179.00 | 2026-10-07 |
| HD | short | 47 | 276.90 | stop | 287.50 | 260.00 | 2026-10-07 |

### Record

14 closed trades: 4W / 10L, total -3.70R, net $+202 realized. Shorts taken: 13.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | long | close | -1.16R | $-590 | 40% |
| JNJ | short | stop | -1.02R | $-550 | 38% |
| CAT | long | stop | -0.90R | $-224 | 36% |
| WMT | short | stop | -1.00R | $-254 | 34% |
| UNH | short | stop | -1.01R | $-253 | 36% |

### Ideas you passed on, replayed against the tape

12 resolved: 2 reached target first, 7 stop first, 2 never reached the entry, 1 expired, 0 ambiguous. Average -0.33R across the 10 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-01 open | CAT | long | Cancelled resting buy stop: failed to hold 815, cyclicals weak, trigger 1.6 ATR  | stop | -1.03R | 30% |
| 2026-09-30 pre-market | XHB | long | Soft-PCE housing relief would fight my own HD short; a 2bp yield dip is not a re | never filled | - | 35% |
| 2026-09-23 pre-market | KRE | short | Same financials thesis as BAC short; avoiding doubling sector exposure and regio | expired | +0.36R | 35% |
| 2026-09-29 pre-market | CVX | short | Pure Iran-headline trade sitting at the 20d low; wrong location. | never filled | - | 38% |
| 2026-10-02 pre-market | XHB | long | Same rate-relief factor as the IWM long, already +2.4% pre-market; one rates lon | stop | -1.00R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| MSFT | 531.06 (10:04 iex) | +0.2% | 529.76 | 529.80 / 528.52-533.51 | 11.92 (2.2%) | 486.00-535.69 | +4.6% / +6.8% | +3.3% | 22.0M |
| NVDA | 234.90 (10:05 iex) | -1.1% | 237.47 | 234.88 / 233.72-235.20 | 5.14 (2.2%) | 208.93-243.37 | +5.3% / +7.7% | +4.0% | 109.6M |
| TLT | 77.38 (10:05 iex) | +0.3% | 77.14 | 77.19 / 77.19-77.40 | 0.85 (1.1%) | 76.43-81.61 | -2.7% / -4.5% | -0.4% | 49.9M |
| COST | 941.84 (10:04 iex) | -0.0% | 942.25 | 953.29 / 941.19-953.29 | 15.52 (1.6%) | 883.10-948.58 | +3.4% / +1.1% | +3.5% | 2.4M |
| XOM | 168.20 (10:05 iex) | +2.5% | 164.05 | 167.11 / 166.71-168.79 | 3.34 (2.0%) | 155.85-169.64 | +0.5% / +2.0% | +0.8% | 13.6M |
| HD | 287.61 (10:05 iex) | +0.6% | 285.77 | 284.53 / 282.84-287.67 | 6.06 (2.1%) | 277.15-312.67 | -3.2% / -10.2% | +0.4% | 5.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 775.50 (10:05 iex) | -0.2% | 777.22 | 774.87 / 774.45-775.74 | 6.62 (0.9%) | 747.74-781.62 | +1.5% / +1.7% | +1.9% | 46.1M |
| QQQ | 753.77 (10:05 iex) | -0.5% | 757.73 | 753.97 / 752.16-754.95 | 9.20 (1.2%) | 699.27-762.86 | +3.3% / +5.1% | +2.4% | 33.4M |
| IWM | 276.14 (10:05 iex) | -0.6% | 277.70 | 276.32 / 275.68-276.89 | 3.70 (1.3%) | 275.45-290.68 | -1.9% / -4.7% | -0.1% | 25.2M |
| DIA | 511.10 (10:05 iex) | +0.0% | 511.02 | 509.01 / 508.87-511.11 | 4.78 (0.9%) | 504.70-526.15 | -0.9% / -2.7% | +0.5% | 3.5M |
| TLT | 77.38 (10:05 iex) | +0.3% | 77.14 | 77.19 / 77.19-77.40 | 0.85 (1.1%) | 76.43-81.61 | -2.7% / -4.5% | -0.4% | 49.9M |
| GLD | 377.90 (10:05 iex) | +0.5% | 375.88 | 377.85 / 377.50-378.67 | 5.91 (1.6%) | 374.23-403.65 | -3.5% / -5.3% | -1.3% | 8.4M |
| USO | 149.02 (10:05 iex) | +3.6% | 143.91 | 148.33 / 148.26-149.05 | 5.59 (3.9%) | 141.76-163.35 | -4.3% / +4.0% | -1.2% | 6.3M |
| SMH | 616.33 (10:05 iex) | -1.4% | 625.03 | 615.70 / 612.20-616.89 | 14.02 (2.2%) | 537.73-639.47 | +5.4% / +8.7% | +2.6% | 6.2M |
| XLK | 200.17 (10:04 iex) | -0.6% | 201.39 | 199.75 / 199.40-200.22 | 2.78 (1.4%) | 181.87-203.25 | +4.2% / +7.2% | +2.9% | 7.3M |
| XLF | 53.83 (10:05 iex) | +0.1% | 53.75 | 53.49 / 53.47-53.90 | 0.67 (1.2%) | 52.81-57.41 | -2.2% / -4.8% | +0.7% | 37.7M |
| XLE | 64.88 (10:05 iex) | +2.4% | 63.36 | 64.51 / 64.31-64.97 | 1.18 (1.9%) | 60.95-65.78 | +0.3% / +2.0% | +3.0% | 34.8M |
| XLV | 166.53 (10:05 iex) | -1.4% | 168.81 | 167.93 / 166.60-168.51 | 2.52 (1.5%) | 164.48-171.87 | +0.4% / +0.3% | +0.2% | 8.0M |
| XLI | 168.27 (10:05 iex) | +0.3% | 167.84 | 166.92 / 166.65-168.20 | 2.34 (1.4%) | 166.18-172.45 | -0.9% / -4.5% | +0.5% | 7.5M |
| XLY | 111.05 (10:04 iex) | -0.3% | 111.36 | 110.82 / 110.72-111.14 | 1.39 (1.2%) | 107.99-113.29 | +0.6% / -2.5% | +2.3% | 6.6M |
| XLP | 82.53 (10:05 iex) | +1.0% | 81.70 | 82.09 / 82.02-82.70 | 0.89 (1.1%) | 80.10-84.33 | -0.5% / -2.4% | +1.4% | 10.8M |
| XLU | 41.21 (10:05 iex) | +0.1% | 41.15 | 41.15 / 41.01-41.37 | 0.60 (1.5%) | 39.03-42.93 | +1.6% / -2.4% | +4.3% | 33.5M |
| XLB | 49.00 (10:04 iex) | +0.0% | 48.98 | 48.81 / 48.70-49.01 | 0.76 (1.5%) | 47.81-50.98 | -1.6% / -4.4% | +0.6% | 11.6M |
| XLRE | 40.47 (10:05 iex) | -0.2% | 40.57 | 40.46 / 40.38-40.60 | 0.51 (1.3%) | 40.41-43.25 | -2.9% / -6.4% | -0.8% | 6.4M |
| XLC | 111.50 (10:04 iex) | +0.2% | 111.26 | 111.46 / 111.29-111.83 | 1.76 (1.6%) | 109.66-115.61 | -0.8% / -0.2% | +0.3% | 6.1M |
| KRE | 69.02 (10:05 iex) | +0.2% | 68.89 | 68.76 / 68.58-69.15 | 1.24 (1.8%) | 67.97-74.43 | -3.5% / -6.5% | -0.8% | 15.7M |
| XHB | 94.66 (10:04 iex) | -0.2% | 94.89 | 94.16 / 93.63-94.78 | 2.13 (2.2%) | 93.97-99.67 | -2.1% / -6.9% | -1.2% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 337.37 (10:05 iex) | +0.2% | 336.67 | 336.81 / 335.90-337.65 | 6.26 (1.9%) | 316.51-345.34 | +0.7% / +4.5% | +1.1% | 40.2M |
| MSFT | 531.06 (10:04 iex) | +0.2% | 529.76 | 529.80 / 528.52-533.51 | 11.92 (2.2%) | 486.00-535.69 | +4.6% / +6.8% | +3.3% | 22.0M |
| NVDA | 234.90 (10:05 iex) | -1.1% | 237.47 | 234.88 / 233.72-235.20 | 5.14 (2.2%) | 208.93-243.37 | +5.3% / +7.7% | +4.0% | 109.6M |
| AMZN | 258.33 (10:05 iex) | -0.6% | 259.92 | 259.74 / 258.20-259.86 | 5.29 (2.0%) | 244.30-260.14 | +3.3% / +0.7% | +4.3% | 35.9M |
| GOOGL | 350.77 (10:05 iex) | +0.1% | 350.50 | 353.40 / 350.36-356.83 | 8.94 (2.6%) | 327.74-364.17 | +1.7% / +1.4% | +1.9% | 26.8M |
| META | 720.85 (10:05 iex) | -0.1% | 721.31 | 724.42 / 717.89-724.95 | 28.58 (4.0%) | 641.63-779.82 | +1.4% / +13.9% | -0.5% | 22.2M |
| TSLA | 372.44 (10:05 iex) | -1.4% | 377.81 | 374.43 / 371.56-375.96 | 11.09 (2.9%) | 345.88-386.83 | +2.9% / +7.4% | +6.5% | 35.7M |
| AVGO | 367.95 (10:05 iex) | -2.3% | 376.51 | 370.62 / 366.40-371.80 | 10.37 (2.8%) | 335.20-380.84 | +6.0% / +1.2% | +7.2% | 24.1M |
| AMD | 636.79 (10:05 iex) | -1.4% | 645.86 | 638.55 / 632.36-639.64 | 23.70 (3.7%) | 480.33-658.52 | +9.9% / +23.6% | +5.6% | 22.0M |
| ORCL | 141.09 (10:05 iex) | -1.7% | 143.56 | 142.19 / 140.57-142.24 | 5.69 (4.0%) | 131.58-166.00 | +0.1% / -1.1% | +4.6% | 34.4M |
| NFLX | 71.11 (10:05 iex) | +2.0% | 69.70 | 70.09 / 69.72-71.11 | 1.78 (2.6%) | 66.54-81.02 | -3.5% / -7.6% | +0.2% | 36.0M |
| CRM | 225.30 (10:04 iex) | +0.3% | 224.56 | 225.46 / 224.60-227.95 | 7.86 (3.5%) | 221.18-261.87 | -5.4% / +0.7% | -2.2% | 11.0M |
| JPM | 328.72 (10:04 iex) | -0.3% | 329.58 | 327.25 / 326.52-329.23 | 5.71 (1.7%) | 324.25-358.26 | -3.1% / -5.6% | +0.1% | 8.5M |
| GS | 885.64 (09:52 iex) | -0.2% | 887.21 | 880.57 / 876.77-887.21 | 19.80 (2.2%) | 868.52-1,042.99 | -5.4% / -10.6% | -1.5% | 2.2M |
| BAC | 52.94 (10:05 iex) | -1.1% | 53.52 | 52.98 / 52.82-53.20 | 0.96 (1.8%) | 52.89-63.83 | -5.7% / -11.1% | -1.7% | 38.9M |
| XOM | 168.20 (10:05 iex) | +2.5% | 164.05 | 167.11 / 166.71-168.79 | 3.34 (2.0%) | 155.85-169.64 | +0.5% / +2.0% | +0.8% | 13.6M |
| CVX | 210.99 (10:05 iex) | +2.8% | 205.15 | 209.32 / 208.96-211.00 | 4.08 (2.0%) | 200.78-217.78 | -1.3% / +1.1% | +0.5% | 9.6M |
| LLY | 1,151.49 (10:05 iex) | -3.1% | 1,188.72 | 1,183.50 / 1,153.60-1,186.09 | 34.23 (2.9%) | 1,113.29-1,215.00 | +2.8% / +1.3% | +2.7% | 2.3M |
| UNH | 372.29 (10:03 iex) | -1.0% | 375.98 | 375.38 / 372.00-376.45 | 7.91 (2.1%) | 362.60-396.82 | +0.1% / -3.5% | +2.4% | 4.9M |
| JNJ | 254.93 (10:04 iex) | -1.4% | 258.45 | 256.22 / 254.92-257.80 | 4.96 (1.9%) | 251.17-275.23 | -2.6% / -2.4% | -2.4% | 6.7M |
| WMT | 109.51 (10:03 iex) | +1.2% | 108.16 | 108.60 / 108.44-109.78 | 2.21 (2.0%) | 103.39-111.23 | +0.9% / -0.3% | +4.1% | 22.2M |
| COST | 941.84 (10:04 iex) | -0.0% | 942.25 | 953.29 / 941.19-953.29 | 15.52 (1.6%) | 883.10-948.58 | +3.4% / +1.1% | +3.5% | 2.4M |
| HD | 287.61 (10:05 iex) | +0.6% | 285.77 | 284.53 / 282.84-287.67 | 6.06 (2.1%) | 277.15-312.67 | -3.2% / -10.2% | +0.4% | 5.3M |
| CAT | 817.45 (10:04 iex) | +0.4% | 813.83 | 808.70 / 807.00-817.45 | 24.46 (3.0%) | 772.86-876.95 | -0.1% / -1.0% | +0.4% | 2.4M |
| BA | 186.35 (10:05 iex) | -1.0% | 188.32 | 185.90 / 184.25-186.44 | 6.16 (3.3%) | 184.01-212.40 | -4.4% / -10.7% | +1.2% | 8.8M |
| DAL | 82.59 (10:05 iex) | -0.5% | 82.97 | 81.71 / 81.50-82.78 | 2.42 (2.9%) | 76.89-86.17 | +1.2% / -1.1% | -0.6% | 7.8M |
| UAL | 108.56 (10:03 iex) | -1.5% | 110.17 | 107.73 / 107.70-109.57 | 4.00 (3.6%) | 104.59-118.26 | -0.4% / -4.4% | -0.7% | 4.2M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-08 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BIAF | 8.31 (10:04 iex) | +34.9% | 6.16 | 6.35 / 6.31-8.34 | 0.95 (15.4%) | 5.11-12.48 | -15.9% / -17.7% | -6.1% | 2.1M |
| IREZ | 11.87 (10:04 iex) | +10.5% | 10.74 | 11.22 / 11.13-11.93 | 0.96 (8.9%) | 6.82-10.90 | +19.9% / -4.7% | +9.6% | 2.7M |
| AAOZ | 9.48 (10:05 iex) | +9.8% | 8.63 | 9.35 / 9.04-9.87 | 1.81 (20.9%) | 7.63-16.50 | -33.5% / -38.6% | -39.0% | 1.2M |
| APUS | 5.81 (10:03 iex) | -17.6% | 7.05 | 6.43 / 5.65-6.50 | 1.98 (28.1%) | 1.51-9.84 | +91.8% / +76.9% | +41.0% | 11.4M |
