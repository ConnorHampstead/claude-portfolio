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

## Pre-market brief: Wednesday 2026-10-07 (09:05 ET / 15:05 Stockholm)

### 1. Tape
Yesterday the S&P 500 (+0.58%) and the Nasdaq (+0.45%) both closed at record highs. This morning futures are lower: S&P −0.3/−0.4%, Nasdaq-100 −0.6/−0.7%, Dow −0.6/−0.8%. SPY is 776.19 and QQQ 754.64 (table). Rates are driving it.

- **Rates:** the 30-year Treasury yield is ~5.70–5.72%, the highest since 2002. The 10-year rose about 8bp to a 5.35% high (verified: Reuters via Investing.com, Yahoo). TLT is at 76.56, below its 20-day low.
- **Oil:** Brent is back above $101 on new Houthi/Hormuz attacks and a tropical-storm threat in the Gulf. WTI is near $90. That reverses Monday's G7-release selloff, which my resting XLE short was built on.
- **Gold** is −2% (GLD 374.57, below its 20-day low).
- **Chips** are weak: MU −2.8%, SMH −1.7%.

The regime is a record-high tape running into a rates wall: an equity market narrow and extended over a bond market that keeps breaking. The short side has a modest edge today in anything rate-sensitive. Mega-cap tech is still the only consistent bid.

### 2. Calendar
Stockholm is ET +6h (CEST until Oct 25).

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 07:00 | 13:00 | MBA mortgage applications | Released. **I could not verify the figure** | HD short (proposed) |
| Pre-mkt | – | STZ earnings (reported last night) | Beat, but cut its operating-margin forecast; stock −4/−5% | none |
| 10:30 | 16:30 | EIA crude inventories | consensus not verified | XOM (proposed) |
| 13:00 | 19:00 | Treasury auction (10-year reopening expected; **size and timing not verified**) | – | IWM, HD, all |
| 14:00 | 20:00 | **FOMC minutes (Sept 15–16 meeting, 25bp hike to 3.75–4.00%)** | Market prices about 20% odds of an October hike. The minutes may show a broader debate than the unanimous vote suggested | everything; IWM, HD most |
| After close | – | COST September sales (Telsey: +10.1% total comp, 6.5% core); LEVI, APLD earnings | – | none held |
| Tue 10/13 | – | JNJ earnings; big banks report from Tuesday | – | JNJ short; this rules out bank shorts |

Under rule 8 the minutes and the auction are ambient risk. I handle them through stop placement and tier.

### 3. Open positions and resting entries
- **CAT long** (861.00, pre-market 846.20, stop 849.00): **invalidated**. My own invalidation was "breaks out, then closes back under 850", and pre-market is already under the stop. A stop order only triggers in the regular session, so it should fire at or near the open. I am leaving the stop to do its job rather than widen it. No change.
- **IWM long** (281.50, last 278.94, stop 276.90): **weakening**. The thesis needed rates to reverse, and the 30-year just made a 24-year high. The stop sits 1.45 above the 275.45 20-day low, which is the structural line. I hold and do not widen; the minutes are the test.
- **JNJ short** (254.46, last 256.45, stop 259.90): **intact but slipping**. Defensives are bid on a red tape. Earnings are 10/13, inside the horizon by Tuesday, so I must close it by Monday's brief at the latest (rule 8). Hold for now.
- **MSFT long** (527.65, last 527.10, stop 515): **intact**. It is holding above the 522.85 breakout level. Hold.
- **NVDA long** (236.40, last 237.24, stop 233): **intact**. It is above the 234.50 pivot even with chips −1.7%. Hold.
- **XLE short, resting sell stop 62.20: cancel.** The thesis was the oil premium unwinding after the G7 release. Brent is back above $100 on new Hormuz attacks plus a Gulf storm threat, and XLE is 64.00, near the 64.10 stop. If the entry filled now, it would be because of a reversal I haven't analysed, not because of the thesis. Cancelling frees about 0.5% of risk.

### 4. New plays

**HD short (sell stop)**

| Field | Value |
|---|---|
| Ticker | HD |
| Direction | Short |
| Catalyst | 2026-10-07: 30-year yield at 5.70%, the highest since 2002, a direct hit to mortgage rates and housing turnover. FOMC minutes at 14:00 ET |
| Thesis | HD is the cleanest rate-victim large cap: −10.2% vs its 50-day average, −3.3% vs its 20-day, red pre-market (284.64). A break of the 277.15 20-day low on a fresh rates high should extend toward 260 |
| Entry | Sell stop 276.90. Pre-market is 284.64, so the trigger is valid |
| Stop | 287.50: above the 286.69 prior close, which an intraday failure would have to reclaim. 10.60 risk, ~1.65 ATR |
| Target | 260.00. 1.6R |
| Risk tier | 0.5. A breakdown entry, and my breakdown shorts have had a poor hit rate here (WMT, UNH, XRLE all stopped) |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 32% |
| Invalidation | Minutes read dovish and the 10-year falls back under 5.20%, or HD reclaims 287 after triggering |
| What I'd be wrong about | HD is already −10% from its 50-day average and close to the bottom of its range. Shorting a fresh low into a possible yield blow-off top is exactly where these trades reverse |

Reasoning: rates are the dominant force on the tape, and this is my best expression of it on the short side outside financials. Financials are off limits because bank earnings start 10/13. The stop entry means I am only short if the market confirms the break. The XLRE short (−1.01R) and two passed XHB longs (both of which lost) show rate-sensitive names are volatile around this level. That is why this is half size.

**XOM long (buy stop, probe)**

| Field | Value |
|---|---|
| Ticker | XOM |
| Direction | Long |
| Catalyst | 2026-10-07: Brent back above $101 on Houthi/Hormuz attacks plus a Gulf tropical-storm threat; XOM +1.0% pre-market (166.08) on a red tape |
| Thesis | Energy is the one sector with a live supply shock, and XOM is relatively strong (+2.4% vs its 50-day average). A break of the 169.64 20-day high would show money rotating in rather than just a headline pop |
| Entry | Buy stop 169.80 |
| Stop | 163.50: back under today's pre-market and the prior 164.48 close, ~1.95 ATR |
| Target | 179.00. 1.46R |
| Risk tier | 0.25. This is a headline-driven commodity trade, and two days ago I was short the same sector |
| Time horizon | 1–5 days |
| Conviction | 2 |
| P(target before stop) | 34% |
| Invalidation | Brent back under $97, or a de-escalation headline |
| What I'd be wrong about | G7 reserve barrels are still flowing, and oil has whipsawed for weeks. One calm day in the Gulf and the breakout fails |

### 5. Both sides
- **Best short:** HD, sell stop 276.90, stop 287.50, target 260, P 32%. **Taken.**
- **Best long:** XOM, buy stop 169.80, stop 163.50, target 179, P 34%. **Taken** as a probe.
- **Longs blocked by the sector cap:** AAPL (+0.9% pre-market on a red tape) would be the stronger long, but tech is ~35% of equity against the 40% cap. Not placeable.

### 6. Passing on
- **COST long** (946.33, above its 937.04 20-day high): its own September sales report comes after the close today. That is a binary event, and I have no edge on the comp.
- **TLT short** (76.56, under its 20-day low): it is the purest expression of the rates trend, but it doubles HD and works against my IWM long. Short at 76.50, stop 78.40, target 73.50, P 38%. Passed.
- **BAC / GS / KRE shorts:** the trend is down, but bank earnings start 10/13, inside the horizon. KRE: sell stop 67.80, stop 70.30, target 64.50, P 33%. Passed.
- **XHB short** (96.56): same factor as HD; one housing short is enough. Sell stop 93.90, stop 98.30, target 88.50, P 33%. Passed.

### 7. For the post-open review
- **CAT:** the stop should fill near the open. If CAT opens above 849 and holds, leave it. Do not widen.
- **IWM:** if it opens under 277.50 and the 10-year is above 5.36% by 10:00, close it rather than wait for the stop. The rates-reversal thesis would be dead.
- **HD:** if it gaps toward 278 at the open, leave the sell stop alone. Do not chase it with a market order.
- **JNJ:** hold. It must be closed by Monday 10/12 because of the 10/13 earnings.

### 8. Book state
If both new entries fill, with XLE cancelled and CAT still counted: gross ≈ 120% (cap 150%), net ≈ +43% (cap ±100%), 7 of 8 slots, risk at stake ≈ 2.6% (cap 4%).

```json
{
  "date": "2026-10-07",
  "no_trade": false,
  "session_note": "Record-high equities running into a 30y yield at a 2002 high and Brent back above $100; cancel the oil-unwind XLE short, add a half-size HD rate-victim breakdown short and a probe XOM breakout long.",
  "plays": [
    {
      "ticker": "HD",
      "direction": "short",
      "entry_type": "stop",
      "entry": 276.90,
      "stop": 287.50,
      "targets": [260.00],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.32,
      "catalyst": "2026-10-07: 30y Treasury yield 5.70%, highest since 2002, 10y 5.35%; FOMC minutes 14:00 ET.",
      "thesis": "HD is the cleanest large-cap rate victim (-10.2% vs 50d). A break of the 277.15 20d low on a fresh rates high should extend toward 260.",
      "invalidation": "Dovish minutes take the 10y back under 5.20%, or HD reclaims 287 after triggering.",
      "bear_case": "Already deeply extended to the downside; shorting fresh lows into a possible yield blow-off is where these reverse."
    },
    {
      "ticker": "XOM",
      "direction": "long",
      "entry_type": "stop",
      "entry": 169.80,
      "stop": 163.50,
      "targets": [179.00],
      "time_horizon": "1-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.34,
      "catalyst": "2026-10-07: Brent back above $101 on Houthi/Hormuz attacks and a Gulf tropical-storm threat; XOM +1% pre-market on a red tape.",
      "thesis": "Energy has the only live supply shock and XOM shows relative strength; a break of the 169.64 20d high shows rotation rather than a headline pop.",
      "invalidation": "Brent back under $97 or a de-escalation headline.",
      "bear_case": "G7 reserve barrels still flowing and oil has whipsawed for weeks; one quiet day in the Gulf fails the breakout."
    }
  ],
  "manage": [
    {
      "ticker": "XLE",
      "action": "close",
      "reason": "Cancel the resting short: the oil-unwind thesis is contradicted by Brent back above $100 on new Hormuz attacks; XLE 64.00 is near the stop."
    }
  ],
  "passed": [
    {
      "ticker": "TLT",
      "direction": "short",
      "entry_type": "limit",
      "entry": 76.50,
      "stop": 78.40,
      "targets": [73.50],
      "p_target_first": 0.38,
      "reason": "Purest rates-trend trade, but it doubles the HD factor and works against the IWM long."
    },
    {
      "ticker": "KRE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 67.80,
      "stop": 70.30,
      "targets": [64.50],
      "p_target_first": 0.33,
      "reason": "Bank earnings start 10/13, inside the horizon."
    },
    {
      "ticker": "XHB",
      "direction": "short",
      "entry_type": "stop",
      "entry": 93.90,
      "stop": 98.30,
      "targets": [88.50],
      "p_target_first": 0.33,
      "reason": "Same housing/rates factor as the HD short; one is enough."
    }
  ]
}
```

Sources: [Yahoo Finance live Oct 7](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-october-7-dow-sp-500-nasdaq-080241833.html), [Reuters via Investing.com](https://www.investing.com/news/economy-news/wall-st-futures-slip-as-yields-and-oil-rebound-fed-minutes-in-focus-4936151), [US News Fed minutes preview](https://money.usnews.com/investing/news/articles/2026-10-07/fed-minutes-could-detail-rate-hike-decision-policy-path), [investingLive minutes preview](https://investinglive.com/central-banks/fed-minutes-preview-one-more-hike-guidance-meets-softer-data-as-october-odds-fade/), [Fool on COST sales Oct 7](https://www.fool.com/investing/2026/10/04/costco-s-underlying-sales-growth-has-slowed-3-months-in-a-row-its-september-report-comes-oct-7/), [Telsey COST via Investing.com](https://ca.investing.com/news/stock-market-news/telsey-reiterates-costco-stock-rating-on-strong-september-sales-outlook-93CH-4865290)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Wednesday 2026-10-07. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$100,628.12**
- Cash: $59,977.13
- Session P&L so far: -1.15% (new entries are blocked at -3.0%)
- Gross exposure: $111,811 (111% of equity, cap 150%)
- Net exposure: $+34,429 (+34%, cap +/-100%)
- Risk at stake (entry to stop): $2,490 (2.47% of equity, cap 4.0%) — 1.53% left for new plays
- Slots: 4 open + 2 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 39% of equity in notional: at 1% risk its stop must be at least 2.6% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 39% of equity in notional: at 1% risk its stop must be at least 2.6% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| IWM | long | 111 | 281.50 | 278.12 | -375 (-1.2%) | 276.90 | 289.50 | Small caps are the most rate-damaged group (-4.5% vs 50d) and the most direct beneficiary of a rates reversal. A limit h |
| JNJ | short | 99 | 254.46 | 259.36 | -485 (-1.9%) | 259.90 | 247.10 | Defensive under rate pressure with persistent relative weakness (Stelara biosimilar overhang). A break of the 20d low op |
| MSFT | long | 36 | 527.65 | 527.59 | -2 (-0.0%) | 515.00 | 548.00 | MSFT is +3.2% vs 20d and +6.2% vs 50d and has held up under higher rates. A break of 522.85 clears a three-week ceiling  |
| NVDA | long | 69 | 236.40 | 238.60 | +152 (+0.9%) | 233.00 | 246.00 | Only mega-cap with a dated positive catalyst and green on a red tape. A break through the 20d high of 234.50 means range |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XOM | long | 40 | 169.80 | stop | 163.50 | 179.00 | 2026-10-07 |
| HD | short | 47 | 276.90 | stop | 287.50 | 260.00 | 2026-10-07 |

### Record

12 closed trades: 4W / 8L, total -1.52R, net $+1,343 realized. Shorts taken: 12.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| CAT | long | stop | -0.90R | $-224 | 36% |
| WMT | short | stop | -1.00R | $-254 | 34% |
| UNH | short | stop | -1.01R | $-253 | 36% |
| DAL | long | close | -0.53R | $-291 | 42% |
| XLRE | short | stop | -1.01R | $-529 | 40% |

### Ideas you passed on, replayed against the tape

11 resolved: 2 reached target first, 6 stop first, 2 never reached the entry, 1 expired, 0 ambiguous. Average -0.25R across the 9 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-09-30 pre-market | XHB | long | Soft-PCE housing relief would fight my own HD short; a 2bp yield dip is not a re | never filled | - | 35% |
| 2026-09-23 pre-market | KRE | short | Same financials thesis as BAC short; avoiding doubling sector exposure and regio | expired | +0.36R | 35% |
| 2026-09-29 pre-market | CVX | short | Pure Iran-headline trade sitting at the 20d low; wrong location. | never filled | - | 38% |
| 2026-10-02 pre-market | XHB | long | Same rate-relief factor as the IWM long, already +2.4% pre-market; one rates lon | stop | -1.00R | 38% |
| 2026-10-02 open | XHB | long | Faded from 98.73 open to 97.67; same rate factor as the resting IWM limit. | stop | -0.98R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| IWM | 278.09 (10:05 iex) | -1.2% | 281.34 | 278.25 / 277.87-279.04 | 3.70 (1.3%) | 275.45-293.39 | -0.8% / -3.5% | +0.8% | 25.0M |
| JNJ | 258.98 (10:01 iex) | +1.6% | 254.78 | 256.21 / 255.73-258.98 | 4.81 (1.9%) | 251.17-275.23 | -4.2% / -3.9% | -4.8% | 6.8M |
| MSFT | 527.67 (10:05 iex) | -0.3% | 529.30 | 530.73 / 525.68-531.66 | 12.21 (2.3%) | 486.00-535.69 | +4.9% / +7.3% | +4.0% | 21.9M |
| NVDA | 238.63 (10:05 iex) | -0.3% | 239.24 | 237.69 / 237.06-238.90 | 5.37 (2.2%) | 208.93-243.37 | +6.4% / +8.9% | +5.3% | 109.9M |
| XOM | 164.82 (10:04 iex) | +0.2% | 164.48 | 165.60 / 164.82-166.86 | 3.23 (2.0%) | 155.85-169.64 | +0.8% / +2.4% | +1.9% | 13.8M |
| HD | 284.67 (10:04 iex) | -0.7% | 286.69 | 285.00 / 283.95-285.98 | 6.40 (2.2%) | 277.15-313.38 | -3.3% / -10.2% | -0.5% | 5.2M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 774.50 (10:05 iex) | -0.6% | 779.09 | 775.77 / 774.09-776.15 | 6.90 (0.9%) | 747.74-781.62 | +1.8% / +2.0% | +1.9% | 46.3M |
| QQQ | 753.11 (10:05 iex) | -0.9% | 759.66 | 753.80 / 751.75-754.83 | 9.58 (1.3%) | 699.27-762.86 | +3.9% / +5.6% | +2.9% | 33.6M |
| IWM | 278.09 (10:05 iex) | -1.2% | 281.34 | 278.25 / 277.87-279.04 | 3.70 (1.3%) | 275.45-293.39 | -0.8% / -3.5% | +0.8% | 25.0M |
| DIA | 509.62 (10:03 iex) | -1.0% | 514.56 | 510.47 / 509.30-511.62 | 4.73 (0.9%) | 504.70-526.15 | -0.3% / -2.1% | +0.3% | 3.4M |
| TLT | 76.74 (10:05 iex) | -0.7% | 77.28 | 76.46 / 76.43-76.74 | 0.85 (1.1%) | 76.69-81.98 | -2.8% / -4.5% | -0.8% | 50.1M |
| GLD | 375.44 (10:04 iex) | -1.8% | 382.27 | 374.98 / 374.23-375.89 | 6.03 (1.6%) | 376.88-406.56 | -2.2% / -3.6% | -0.2% | 8.5M |
| USO | 145.55 (10:04 iex) | +0.4% | 144.91 | 146.22 / 145.43-147.07 | 5.47 (3.8%) | 141.76-163.35 | -3.9% / +5.1% | +1.1% | 6.4M |
| SMH | 620.98 (10:05 iex) | -1.8% | 632.50 | 621.10 / 618.78-623.18 | 14.20 (2.2%) | 537.73-639.47 | +7.1% / +10.4% | +4.2% | 6.0M |
| XLK | 200.13 (10:04 iex) | -0.9% | 202.00 | 200.11 / 199.63-200.64 | 2.94 (1.5%) | 181.87-203.25 | +4.9% / +7.9% | +3.9% | 7.3M |
| XLF | 53.53 (10:05 iex) | -0.9% | 54.01 | 53.53 / 53.42-53.69 | 0.68 (1.3%) | 52.81-57.41 | -2.0% / -4.5% | +0.0% | 37.3M |
| XLE | 63.69 (10:05 iex) | -0.1% | 63.75 | 64.04 / 63.68-64.51 | 1.15 (1.8%) | 60.95-65.78 | +0.8% / +2.8% | +3.6% | 34.8M |
| XLV | 168.86 (10:05 iex) | +1.1% | 167.09 | 167.89 / 167.43-169.09 | 2.38 (1.4%) | 164.48-171.87 | -0.5% / -0.7% | -2.1% | 8.0M |
| XLI | 168.25 (10:04 iex) | -1.9% | 171.58 | 169.71 / 167.89-170.21 | 2.23 (1.3%) | 166.18-173.69 | +1.2% / -2.5% | +1.4% | 7.4M |
| XLY | 110.89 (10:05 iex) | -0.7% | 111.72 | 111.03 / 110.88-111.50 | 1.46 (1.3%) | 107.99-113.29 | +0.8% / -2.2% | +2.4% | 6.7M |
| XLP | 82.12 (10:05 iex) | +0.4% | 81.80 | 82.08 / 81.89-82.29 | 0.90 (1.1%) | 80.10-84.33 | -0.4% / -2.4% | -0.1% | 10.9M |
| XLU | 40.90 (10:05 iex) | -0.6% | 41.16 | 40.99 / 40.85-41.09 | 0.60 (1.5%) | 39.03-43.21 | +1.4% / -2.5% | +3.7% | 32.2M |
| XLB | 49.05 (10:05 iex) | -1.4% | 49.73 | 49.29 / 48.99-49.41 | 0.74 (1.5%) | 47.81-51.91 | -0.3% / -3.1% | +1.3% | 11.8M |
| XLRE | 40.81 (10:05 iex) | -0.7% | 41.10 | 41.13 / 40.80-41.18 | 0.50 (1.2%) | 40.41-43.54 | -2.0% / -5.4% | -0.6% | 6.3M |
| XLC | 110.83 (10:05 iex) | -0.7% | 111.65 | 111.32 / 110.65-111.51 | 1.81 (1.6%) | 109.66-115.61 | -0.4% / +0.2% | +0.2% | 6.1M |
| KRE | 68.88 (10:05 iex) | -1.7% | 70.07 | 69.27 / 68.69-69.42 | 1.21 (1.7%) | 67.97-74.43 | -2.1% / -5.1% | +0.3% | 15.3M |
| XHB | 94.62 (10:05 iex) | -2.8% | 97.37 | 95.55 / 94.54-96.07 | 2.09 (2.1%) | 94.08-100.34 | +0.2% / -4.8% | +0.4% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 335.16 (10:05 iex) | +0.5% | 333.63 | 336.91 / 332.78-338.67 | 6.42 (1.9%) | 309.90-345.34 | +0.1% / +3.5% | +1.3% | 41.9M |
| MSFT | 527.67 (10:05 iex) | -0.3% | 529.30 | 530.73 / 525.68-531.66 | 12.21 (2.3%) | 486.00-535.69 | +4.9% / +7.3% | +4.0% | 21.9M |
| NVDA | 238.63 (10:05 iex) | -0.3% | 239.24 | 237.69 / 237.06-238.90 | 5.37 (2.2%) | 208.93-243.37 | +6.4% / +8.9% | +5.3% | 109.9M |
| AMZN | 255.12 (10:05 iex) | -0.5% | 256.29 | 254.23 / 253.17-255.61 | 5.28 (2.1%) | 244.30-259.49 | +2.0% / -0.4% | +3.9% | 35.9M |
| GOOGL | 346.02 (10:05 iex) | -0.5% | 347.68 | 346.82 / 343.07-347.25 | 8.86 (2.5%) | 327.74-364.17 | +1.2% / +0.7% | +2.0% | 27.4M |
| META | 722.89 (10:05 iex) | -2.2% | 738.88 | 738.14 / 721.90-738.71 | 28.39 (3.8%) | 638.06-779.82 | +4.3% / +17.2% | +0.0% | 23.4M |
| TSLA | 375.80 (10:05 iex) | -1.3% | 380.68 | 378.31 / 375.62-382.35 | 11.67 (3.1%) | 345.88-386.83 | +3.8% / +8.7% | +7.9% | 36.1M |
| AVGO | 370.44 (10:05 iex) | -1.4% | 375.81 | 372.26 / 369.12-374.34 | 10.62 (2.8%) | 335.20-380.84 | +6.0% / +1.0% | +5.8% | 24.5M |
| AMD | 636.56 (10:05 iex) | -2.0% | 649.42 | 634.30 / 633.16-648.48 | 25.32 (3.9%) | 480.33-658.52 | +11.7% / +25.2% | +6.9% | 22.2M |
| ORCL | 143.30 (10:05 iex) | -1.0% | 144.77 | 142.54 / 141.37-144.70 | 6.08 (4.2%) | 131.58-166.00 | +0.3% / +0.1% | +5.1% | 35.0M |
| NFLX | 68.87 (10:05 iex) | +0.3% | 68.69 | 68.81 / 68.50-69.19 | 1.80 (2.6%) | 66.54-81.02 | -5.3% / -9.0% | -2.3% | 35.7M |
| CRM | 223.44 (10:04 iex) | -0.7% | 224.99 | 225.24 / 222.80-225.80 | 8.12 (3.6%) | 221.18-261.87 | -5.6% / +1.3% | -0.1% | 11.4M |
| JPM | 326.31 (10:05 iex) | -1.5% | 331.28 | 327.20 / 325.07-328.45 | 5.85 (1.8%) | 324.25-358.26 | -2.9% / -5.2% | -0.6% | 8.5M |
| GS | 869.72 (10:04 iex) | -3.1% | 897.18 | 880.85 / 868.52-883.79 | 20.32 (2.3%) | 881.00-1,042.99 | -5.1% / -9.8% | -2.1% | 2.2M |
| BAC | 53.23 (10:05 iex) | -1.6% | 54.09 | 53.19 / 52.91-53.43 | 0.95 (1.8%) | 52.89-63.83 | -5.4% / -10.4% | -1.6% | 39.2M |
| XOM | 164.82 (10:04 iex) | +0.2% | 164.48 | 165.60 / 164.82-166.86 | 3.23 (2.0%) | 155.85-169.64 | +0.8% / +2.4% | +1.9% | 13.8M |
| CVX | 206.64 (10:05 iex) | -0.5% | 207.58 | 208.44 / 206.54-210.14 | 3.89 (1.9%) | 200.78-217.78 | -0.4% / +2.5% | +1.6% | 9.8M |
| LLY | 1,182.24 (10:05 iex) | +2.1% | 1,157.49 | 1,173.62 / 1,166.00-1,187.00 | 32.29 (2.8%) | 1,113.29-1,215.00 | +0.4% / -1.4% | -2.3% | 2.2M |
| UNH | 376.43 (10:05 iex) | +0.0% | 376.32 | 375.92 / 375.07-379.19 | 7.54 (2.0%) | 362.60-404.04 | +0.0% / -3.6% | +0.4% | 5.0M |
| JNJ | 258.98 (10:01 iex) | +1.6% | 254.78 | 256.21 / 255.73-258.98 | 4.81 (1.9%) | 251.17-275.23 | -4.2% / -3.9% | -4.8% | 6.8M |
| WMT | 108.17 (10:05 iex) | +0.9% | 107.20 | 107.53 / 107.40-108.27 | 2.21 (2.1%) | 103.39-111.23 | +0.1% / -1.3% | +0.4% | 22.2M |
| COST | 944.49 (10:02 iex) | +0.9% | 935.68 | 941.23 / 937.60-944.49 | 15.16 (1.6%) | 883.10-937.04 | +2.9% / +0.3% | +1.2% | 2.4M |
| HD | 284.67 (10:04 iex) | -0.7% | 286.69 | 285.00 / 283.95-285.98 | 6.40 (2.2%) | 277.15-313.38 | -3.3% / -10.2% | -0.5% | 5.2M |
| CAT | 820.40 (10:05 iex) | -5.0% | 863.44 | 846.00 / 818.90-846.00 | 22.61 (2.6%) | 772.86-876.95 | +5.9% / +5.0% | +4.5% | 2.3M |
| BA | 187.71 (10:04 iex) | -1.1% | 189.82 | 188.18 / 186.65-188.84 | 6.38 (3.4%) | 184.01-212.40 | -4.1% / -10.3% | +1.1% | 8.7M |
| DAL | 83.08 (10:04 iex) | -0.7% | 83.66 | 82.19 / 81.80-83.08 | 2.43 (2.9%) | 76.89-86.17 | +2.3% / -0.4% | -1.4% | 7.7M |
| UAL | 109.94 (10:04 iex) | -1.7% | 111.87 | 109.33 / 108.95-110.05 | 4.04 (3.6%) | 104.59-118.26 | +1.3% / -3.2% | -0.7% | 4.1M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-07 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| PENG | 74.25 (10:04 iex) | +15.6% | 64.21 | 67.30 / 65.70-75.89 | 3.52 (5.5%) | 46.19-64.58 | +18.9% / +19.7% | +15.1% | 2.3M |
| APUS | 8.31 (10:03 iex) | +16.5% | 7.13 | 8.00 / 7.52-8.96 | 1.79 (25.1%) | 1.51-9.14 | +107.4% / +78.1% | +42.0% | 10.4M |
| AAOZ | 8.76 (10:03 iex) | +12.7% | 7.77 | 8.20 / 8.04-8.86 | 1.86 (23.9%) | 7.63-16.50 | -41.1% / -47.1% | -43.5% | 1.1M |
| TJGC | 31.00 (09:49 sip) | +11.4% | 27.82 | 26.54 / 23.73-31.91 | 5.45 (19.6%) | 10.40-36.76 | +30.6% / +128.9% | -20.0% | 1.0M |
| GDXD | 24.42 (09:49 sip) | +11.1% | 21.99 | 24.22 / 24.15-25.00 | 1.80 (8.2%) | 15.25-23.66 | +11.8% / -5.6% | +3.3% | 2.5M |
| SMST | 12.64 (10:04 iex) | +9.8% | 11.51 | 12.47 / 12.34-12.85 | 1.80 (15.6%) | 10.70-23.74 | -25.6% / -63.8% | -12.8% | 1.8M |
| BULL | 5.80 (10:05 iex) | -20.3% | 7.28 | 5.82 / 5.51-6.02 | 0.36 (4.9%) | 6.86-9.82 | -7.8% / -10.4% | +1.5% | 12.2M |
| HESM | 32.73 (10:05 iex) | -15.4% | 38.69 | 36.05 / 32.22-36.05 | 0.84 (2.2%) | 36.96-41.29 | -0.9% / -2.1% | +2.8% | 1.3M |
| FCEL | 17.77 (10:05 iex) | -13.9% | 20.65 | 18.92 / 17.78-19.10 | 1.41 (6.8%) | 14.71-21.06 | +21.8% / +11.8% | +22.2% | 5.8M |
| AAOX | 13.42 (10:03 iex) | -13.3% | 15.47 | 14.50 / 13.21-14.89 | 1.48 (9.5%) | 8.15-15.65 | +48.6% / +18.3% | +63.5% | 9.6M |
