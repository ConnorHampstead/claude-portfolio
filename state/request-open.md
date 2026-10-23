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

Research is done: oil hit a five-month high, chips sold off hard yesterday, and FOMC and GOOGL earnings are dated for next week. Writing the brief now.

# Pre-market brief: Friday 2026-10-23, 09:05 ET / 15:05 Stockholm

### 1. Tape
Thursday was the worst S&P day since July (−1.21% to 7,663) and the Nasdaq fell 2.6%. Semiconductors dropped about 6.7% after Lam Research warned of supply constraints into 2027. Combined with Meta raising capex and Tesla cutting it, that revived the question of what AI spending actually returns. AI and chip names made up about 93% of the Nasdaq-100's loss (verified: Yahoo, Stocktitan, Techtimes). Overnight, Brent touched $115.84, its highest since May, after Houthi strikes on Saudi Arabia and reports of possible US/Israeli strikes on Iran. Futures are mildly lower: SPY 760.13 (−0.5%), QQQ 703.00 (−0.2%), DIA −0.9%. Chips are flat to slightly bid after the rout (SMH +0.1%, NVDA 212.03).

The regime is risk-off rotation: AI capex is being sold, and energy, health care and staples are holding near their 20-day highs. Shorts keep the edge in AI and in oil-sensitive names. But it is a Friday after a capitulation-style chip day, so a reflex bounce is the main risk to fresh tech shorts, and Iran headlines over the weekend can push oil either way.

### 2. Calendar
| Event | ET | Stockholm | Actual / consensus | Touches |
|---|---|---|---|---|
| AXP, Autoliv and ~28 other pre-open earnings | before 09:30 | before 15:30 | AXP EPS 4.68 vs 4.50 est, revenue just under; Autoliv missed (−6%) | none |
| S&P Global flash PMIs (Oct) | 09:45 | 15:45 | Services ~57.9 (prior 58.8), Mfg ~55.4 (prior 55.9). Thinly sourced consensus | all, mostly through rates |
| UMich sentiment, final Oct | 10:00 | 16:00 | Prelim 46.3, with inflation expectations rising | XLV, UAL (consumer) |
| Weekend: Iran/Houthi headlines | — | — | Brent ~$114; Israel's army chief reportedly sees no need to strike before Israel's Oct 27 election | XOM, UAL |
| Next week: FOMC Oct 27–28 (decision 14:00 ET Wed) | — | — | Hold expected after the September hike; December hike favoured | all |
| GOOGL earnings Wed Oct 28, after the close | — | — | EPS est. ~3.03 | GOOGL short must be flat by the Oct 27 close (rule 8) |

### 3. Open positions and resting entries
- **GOOGL short** (332.42 → 321.58; stop 337, target 320): **intact.** It is under the 322.00 20-day low and 1.6 from target. Earnings land on Oct 28, so the trade has at most two sessions left after today. **Tighten the stop to 330.00**, about one ATR above the market and below the 334.76 close from two days ago. That locks in about +0.09R at the stop and stops a weekend squeeze from giving back the gain. Target stays at 320.
- **NVDA short** (212.38 → 212.03; stop 222, target 198): **intact but untested.** Entry was the break of the 20-day low, and it is sitting on that line after a −6.7% sector day. **Hold at 222 / 198.** The stop is 1.6 ATR away, which is the room a post-rout bounce needs.
- **ORCL short** (129.70 → 124.46; stop 132, target 116.50): **intact.** This is still the AI-credit proxy and it sits 1.7 above its 20-day low. **Tighten the stop to 130.00**, the broken support and roughly breakeven. That is 0.83 ATR away, tight, but a reclaim of 130 would mean the breakdown failed. I'd rather not carry +0.4R of open profit into a weekend at full risk. Target stays at 116.50.
- **XLV long** (179.57 → 180.62; stop 176.40, target 184.80): **intact.** The rotation thesis is working: XLV is near its 20-day high of 182.25 and holding while SPY is red. **Hold.**
- **XOM resting buy stop 180.60** (stop 175.40, target 189): **keep.** Last is 179.20, so the trigger is still above the market. Brent at a five-month high is exactly the condition this order was built for. It gets cleared before the weekend if it doesn't fill today.

### 4. New plays

**UAL short**
| Field | Value |
|---|---|
| Ticker | UAL |
| Direction | Short |
| Catalyst | Brent hit $115.84 on 2026-10-23 after Houthi strikes on Saudi Arabia, with US strike fears on Iran over the weekend; UAL is −1.7% pre-market at 100.28 |
| Thesis | Jet fuel is airlines' biggest variable cost, and a fresh five-month oil high with a widening Gulf conflict hits their margins directly. UAL is already −3.8% under its 20-day average, so it is the weak side of the oil trade. |
| Entry | Market at the open (~100.3 pre-market, IEX/SIP verified) |
| Stop | 106.00: above the 102.00 prior close plus ~0.8 ATR (1.2 ATR from entry), so a full gap-fill and continuation would invalidate it |
| Target | 92.50, below the 94.54 20-day low (~1.35R) |
| Risk tier | 0.5: the main risk is a weekend de-escalation headline (Trump has delayed strikes before and Brent fell 10% then), which is gap risk |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 40% |
| Invalidation | Brent back under $108, or UAL reclaims 102 with the market red |
| What I'd be wrong about | Airlines hedge fuel, and the sector has mostly ignored this spike so far (UAL is +0.7% over 5 days). The oil move may already be priced in, and a ceasefire headline would squeeze it hard. |

**AVGO short (probe, stop entry)**
| Field | Value |
|---|---|
| Ticker | AVGO |
| Direction | Short |
| Catalyst | Thursday's Lam-led chip rout (2026-10-22) left AVGO at 321.53, 0.5 above its 321.02 20-day low |
| Thesis | If the post-rout bounce fails and AVGO breaks its 20-day low, the AI-capex unwind has a new leg in the custom-silicon leader. A sell stop only fires on confirmation, not into the bounce. |
| Entry | Sell stop 317.00 (1.4% under last; this is the break of the 20-day low with a buffer) |
| Stop | 333.00: back above Thursday's close of 323.24 plus a margin (1.35 ATR) |
| Target | 293.00 (1.5R) |
| Risk tier | 0.25: this is a fourth AI-factor short, and it would be entering a Friday bounce. Last time I passed on META and AVGO for exactly this reason, and META then hit its target. This probe gets that view scored. |
| Time horizon | 1–5 days |
| Conviction | 2 |
| P(target before stop) | 36% |
| Invalidation | SMH reclaims 540, or NVDA reclaims 218 |
| What I'd be wrong about | Capitulation days (SOX −6.7%) usually get a multi-day reflex bounce, and AVGO is −7.7% under its 20-day average already. |

### 5. Both sides
- **Best long: XOM** buy stop 180.60, stop 175.40, target 189, P 42%. It is already resting.
- **Best short: UAL** at market ~100.3, stop 106, target 92.50, P 40%. Taken.

### 6. Passing on
- **LLY long** (buy stop 1,325, stop 1,270, target 1,410, P 35%): it is the same defensive-rotation factor as XLV, it is extended (+8.9% over its 20-day average), and I don't want to double the bet.
- **META short on a bounce** (limit 660, stop 686, target 620, P 33%): it has already traded through yesterday's 640 target. Shorting it now would be chasing after −11.9% over 5 days, and AVGO is the cleaner probe.
- **DAL short:** the same oil view as UAL, with less room before its 20-day low (74.14). One airline is enough.
- **TLT long breakout:** it sits at its 20-day high, but $114 oil pushes the inflation side against the growth scare. That's a coin flip, so no levels.

### 7. For the post-open review
- **NVDA:** if it trades above 218 by 10:05 (yesterday's bounce zone), cut the stop to 219. If it is under 210, leave it.
- **UAL:** if it fills above 102 (a gap-up open on de-escalation news), close it. The thesis's premise is gone.
- **GOOGL:** if the 320 target hits, it's done. Otherwise there is a hard exit by the Mon Oct 27 close, and the Monday brief must send a `close`.
- **AVGO:** if SMH is above +3% at 10:05, cancel the sell stop.

### 8. Book state
Counting resting entries as filled and after the stop changes: gross ~77% of equity (cap 150%), net ~+13% (cap ±100%), 7/8 slots, risk at stake ~2.0% of equity (cap 4%).

```json
{
  "date": "2026-10-23",
  "no_trade": false,
  "session_note": "Risk-off rotation after Thursday's chip rout, with Brent at a 5-month high ($114-116). Shorting UAL on oil (half risk) and probing an AVGO 20d-low break; tightening GOOGL and ORCL stops before the weekend.",
  "plays": [
    {
      "ticker": "UAL",
      "direction": "short",
      "entry_type": "market",
      "entry": 100.28,
      "stop": 106.00,
      "targets": [92.50],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.40,
      "catalyst": "Brent touched $115.84 on 2026-10-23 (5-month high) on Houthi strikes on Saudi Arabia and US-Iran strike fears; UAL -1.7% pre-market.",
      "thesis": "Jet fuel is airlines' largest variable cost; a fresh oil high with a widening Gulf conflict hits margins directly, and UAL is already below its 20d average. Target is under the 94.54 20d low.",
      "invalidation": "Brent back under $108, or UAL reclaims 102 on a red tape.",
      "bear_case": "Fuel hedges and a market that has ignored the spike so far (+0.7% in 5d); a weekend ceasefire headline would squeeze it."
    },
    {
      "ticker": "AVGO",
      "direction": "short",
      "entry_type": "stop",
      "entry": 317.00,
      "stop": 333.00,
      "targets": [293.00],
      "time_horizon": "1-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.36,
      "catalyst": "Lam-led semiconductor rout on 2026-10-22 left AVGO 0.5 above its 321.02 20d low.",
      "thesis": "A failed post-rout bounce and a break of the 20d low extend the AI-capex unwind into custom silicon. The stop entry fires only on confirmation.",
      "invalidation": "SMH reclaims 540, or NVDA reclaims 218.",
      "bear_case": "Capitulation days usually bring a multi-day reflex bounce; AVGO is already 7.7% under its 20d average."
    }
  ],
  "manage": [
    {"ticker": "GOOGL", "action": "update", "stop": 330.00, "reason": "1.6 from target with earnings Oct 28; stop cut to ~1 ATR above last, below the 334.76 close, to lock a small gain into the weekend."},
    {"ticker": "ORCL", "action": "update", "stop": 130.00, "reason": "Stop moved to the broken 130 support (~breakeven); a reclaim means the breakdown failed. Protects +0.4R over the weekend."}
  ],
  "passed": [
    {
      "ticker": "LLY",
      "direction": "long",
      "entry_type": "stop",
      "entry": 1325.00,
      "stop": 1270.00,
      "targets": [1410.00],
      "p_target_first": 0.35,
      "reason": "Same defensive-rotation factor as the XLV long; extended +8.9% vs 20d average."
    },
    {
      "ticker": "META",
      "direction": "short",
      "entry_type": "limit",
      "entry": 660.00,
      "stop": 686.00,
      "targets": [620.00],
      "p_target_first": 0.33,
      "reason": "Already through the prior target after -11.9% in 5d; chasing. AVGO is the cleaner probe of the same factor."
    }
  ]
}
```

Sources: [Yahoo futures](https://finance.yahoo.com/markets/stocks/articles/nasdaq-dow-p-500-futures-101348956.html), [Yahoo Oct 22 close](https://finance.yahoo.com/markets/article/stock-market-today-thursday-october-22-dow-sp-500-nasdaq-tesla-meta-112217857.html), [Stocktitan](https://www.stocktitan.net/articles/why-is-nasdaq-down-today-october-22-2026-ai-chip-stocks), [Techtimes](https://www.techtimes.com/articles/329406/20261023/chip-stocks-lose-200-billion-equipment-makers-warning-counters-nvidias-ai-optimism.htm), [CNBC oil](https://www.cnbc.com/2026/10/23/oil-price-brent-wti-iran-war-saudi-arabia.html), [Bloomberg oil](https://www.bloomberg.com/news/articles/2026-10-22/latest-oil-market-news-and-analysis-for-oct-23), [Tradingeconomics Brent](https://tradingeconomics.com/commodity/brent-crude-oil/news/535543), [Investing.com calendar](https://ca.investing.com/news/stock-market-news/pmi-data-and-consumer-sentiment-among-economic-releases-due-friday-93CH-4897586), [UMich prelim](https://www.marketreview.com/news/us-consumer-sentiment-46-3-october-2026/), [MarketBeat GOOGL earnings](https://www.marketbeat.com/earnings/reports/2026-10-28-alphabet-inc-stock/), [FOMC date](https://fedratecalc.com/fed-rate-decision/), [Admiral Markets Fed](https://admiralmarkets.com/analytics/traders-blog/fed-rate-decision-october-2026), [Investing.com premarket movers](https://www.investing.com/news/stock-market-news/premarket-movers-crown-castle-jumps-75-on-spacex-talks-autoliv-slides-4969100), [CoinCentral AXP](https://coincentral.com/american-express-axp-stock-gains-after-third-quarter-earnings-beat), [24/7 Wall St chips](https://247wallst.com/investing/2026/10/22/chip-stocks-fall-as-supply-warning-deepens-ai-selloff-marvell-and-amd-sink-8-intel-drops-7)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC, 16:05 Stockholm), Friday 2026-10-23. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$103,202.61**
- Cash: $85,645.92
- Session P&L so far: -0.03% (new entries are blocked at -3.0%)
- Gross exposure: $80,262 (78% of equity, cap 150%)
- Net exposure: $+12,484 (+12%, cap +/-100%)
- Risk at stake (entry to stop): $2,249 (2.18% of equity, cap 4.0%) — 1.82% left for new plays
- Slots: 6 open + 1 resting entries of 8 — you may add at most 1 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| GOOGL | short | 28 | 332.42 | 323.65 | +246 (+2.6%) | 330.00 | 320.00 | Relative weakness breaking the floor of the 20-day range on a tech-bid day; failed floor opens ~4% to 320. |
| NVDA | short | 26 | 212.38 | 212.85 | -12 (-0.2%) | 222.00 | 198.00 | A break of the 212.85 20d low confirms Monday's bounce failed in the bellwether and opens a move toward 198. |
| ORCL | short | 33 | 129.70 | 126.19 | +116 (+2.7%) | 130.00 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |
| UAL | short | 103 | 99.14 | 97.64 | +154 (+1.5%) | 106.00 | 92.50 | Jet fuel is airlines' largest variable cost; a fresh oil high with a widening Gulf conflict hits margins directly, and U |
| XLV | long | 160 | 179.57 | 179.78 | +34 (+0.1%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |
| XOM | long | 97 | 180.75 | 181.53 | +76 (+0.4%) | 175.40 | 189.00 | Energy remains the leading sector; a break of the 180.26 20-day high with oil at a 5-month high extends the trend. |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| AVGO | short | 16 | 317.00 | stop | 333.00 | 293.00 | 2026-10-23 |

### Record

23 closed trades: 9W / 14L, total +1.41R, net $+2,598 realized. Shorts taken: 25.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| CVX | long | stop | -0.23R | $-117 | 40% |
| AMD | short | target | +1.17R | $+575 | 42% |
| HD | long | target | +1.47R | $+373 | 37% |
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |

### Ideas you passed on, replayed against the tape

60 resolved: 18 reached target first, 30 stop first, 9 never reached the entry, 3 expired, 0 ambiguous. Average -0.08R across the 51 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-14 pre-market | CVX | long | Best long (20d-high breakout) but duplicates the XOM energy exposure. | target | +1.70R | 40% |
| 2026-10-19 pre-market | AMZN | long | Buying an upgrade gap in a heavy data-center spender while the capex-credit stor | stop | -1.06R | 38% |
| 2026-10-20 pre-market | AAPL | short | Analyst downgrade gap of only 1 ATR in a mega-cap that has held up defensively. | stop | -0.99R | 33% |
| 2026-10-16 pre-market | SMH | short | Ninth straight down day; factor already banked at target 10/15; only a bounce sa | never filled | - | 35% |
| 2026-10-09 pre-market | DAL | short | Q3 miss and FY cut are real, but oil is falling the same day, easing the fuel he | expired | -0.43R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 323.58 (10:05 iex) | -0.2% | 324.22 | 321.14 / 320.18-324.04 | 8.48 (2.6%) | 322.00-359.40 | -5.8% / -5.6% | -7.2% | 24.1M |
| NVDA | 212.91 (10:05 iex) | +0.3% | 212.21 | 211.04 / 210.18-213.31 | 6.15 (2.9%) | 211.26-243.37 | -6.2% / -4.7% | -2.3% | 106.8M |
| ORCL | 126.12 (10:05 iex) | +0.5% | 125.54 | 124.87 / 124.39-126.78 | 6.66 (5.3%) | 122.76-146.40 | -7.6% / -12.2% | -6.6% | 29.6M |
| UAL | 97.55 (10:04 iex) | -4.4% | 102.00 | 100.01 / 97.55-100.98 | 4.78 (4.7%) | 94.54-115.71 | -3.8% / -7.0% | +0.7% | 5.0M |
| XLV | 179.81 (10:05 iex) | -0.8% | 181.30 | 180.40 / 179.15-180.74 | 3.11 (1.7%) | 165.19-182.25 | +5.4% / +6.3% | +2.3% | 8.6M |
| XOM | 181.53 (10:05 iex) | +1.9% | 178.23 | 179.37 / 179.00-182.06 | 3.77 (2.1%) | 159.27-180.31 | +5.0% / +7.9% | +2.0% | 11.4M |
| AVGO | 325.10 (10:05 iex) | +0.6% | 323.24 | 321.50 / 320.23-325.90 | 11.88 (3.7%) | 321.02-380.84 | -7.7% / -9.8% | -6.1% | 21.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 760.58 (10:05 iex) | -0.4% | 763.96 | 759.90 / 759.14-761.32 | 7.30 (1.0%) | 758.79-781.62 | -0.9% / -0.4% | -1.0% | 40.9M |
| QQQ | 705.36 (10:05 iex) | +0.1% | 704.47 | 702.20 / 701.16-706.08 | 12.04 (1.7%) | 701.90-762.86 | -4.4% / -3.0% | -3.2% | 37.0M |
| IWM | 274.80 (10:05 iex) | -0.7% | 276.67 | 274.84 / 274.05-275.39 | 3.75 (1.4%) | 269.88-284.64 | -0.3% / -3.5% | +0.6% | 25.7M |
| DIA | 522.05 (10:04 iex) | -1.1% | 527.89 | 522.70 / 521.59-523.59 | 5.15 (1.0%) | 504.59-528.45 | +2.3% / +1.1% | +1.3% | 3.3M |
| TLT | 81.42 (10:05 iex) | -0.4% | 81.74 | 81.79 / 81.42-81.80 | 0.85 (1.0%) | 76.43-81.92 | +4.0% / +1.8% | +2.2% | 50.2M |
| GLD | 368.15 (10:05 iex) | -0.2% | 369.00 | 368.94 / 368.08-369.25 | 5.17 (1.4%) | 368.35-394.22 | -3.0% / -6.6% | -3.6% | 8.2M |
| USO | 167.49 (10:05 iex) | +3.1% | 162.51 | 166.17 / 166.04-167.89 | 4.39 (2.7%) | 141.76-163.77 | +7.1% / +11.6% | +3.3% | 5.1M |
| SMH | 528.54 (10:05 iex) | +1.0% | 523.35 | 522.61 / 521.33-529.57 | 18.07 (3.5%) | 520.53-639.47 | -11.2% / -9.2% | -6.4% | 8.2M |
| XLK | 183.00 (10:05 iex) | +0.4% | 182.34 | 181.82 / 181.55-183.14 | 4.04 (2.2%) | 181.50-203.25 | -6.0% / -3.9% | -3.6% | 8.7M |
| XLF | 56.11 (10:05 iex) | -1.0% | 56.65 | 56.20 / 56.08-56.35 | 0.70 (1.2%) | 52.81-56.67 | +3.7% / +1.1% | +2.5% | 36.4M |
| XLE | 68.82 (10:05 iex) | +1.8% | 67.57 | 68.08 / 67.76-69.01 | 1.44 (2.1%) | 60.95-68.78 | +3.9% / +5.6% | +1.5% | 32.0M |
| XLV | 179.81 (10:05 iex) | -0.8% | 181.30 | 180.40 / 179.15-180.74 | 3.11 (1.7%) | 165.19-182.25 | +5.4% / +6.3% | +2.3% | 8.6M |
| XLI | 163.30 (10:05 iex) | -2.1% | 166.73 | 165.01 / 163.17-165.06 | 2.61 (1.6%) | 164.66-172.34 | -1.1% / -3.3% | -0.7% | 7.5M |
| XLY | 113.13 (10:05 iex) | -1.6% | 115.01 | 114.06 / 113.18-114.10 | 1.50 (1.3%) | 107.99-116.22 | +2.8% / +1.4% | +1.4% | 7.2M |
| XLP | 88.74 (10:05 iex) | -1.4% | 89.99 | 89.59 / 88.66-89.94 | 1.30 (1.4%) | 80.10-89.99 | +7.1% / +7.1% | +3.8% | 13.5M |
| XLU | 42.44 (10:05 iex) | -1.0% | 42.87 | 42.73 / 42.42-42.81 | 0.70 (1.6%) | 39.03-42.88 | +4.6% / +2.7% | +2.9% | 36.7M |
| XLB | 51.17 (10:05 iex) | -1.0% | 51.69 | 51.41 / 51.16-51.67 | 0.70 (1.4%) | 47.81-51.71 | +3.7% / +1.5% | +2.2% | 11.4M |
| XLRE | 42.72 (10:05 iex) | +0.5% | 42.52 | 43.16 / 42.67-43.21 | 0.62 (1.5%) | 40.28-42.61 | +2.5% / -0.5% | +1.3% | 7.8M |
| XLC | 106.53 (10:05 iex) | -0.8% | 107.42 | 105.94 / 105.86-106.73 | 1.66 (1.5%) | 106.73-113.52 | -3.1% / -3.7% | -4.5% | 6.5M |
| KRE | 72.09 (10:05 iex) | -0.4% | 72.41 | 71.97 / 71.89-72.79 | 1.29 (1.8%) | 67.79-72.43 | +3.5% / +0.2% | +3.8% | 16.1M |
| XHB | 97.80 (10:03 iex) | -1.4% | 99.20 | 97.96 / 97.69-98.65 | 2.31 (2.3%) | 91.87-99.28 | +3.4% / -0.1% | +3.6% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 348.02 (10:05 iex) | -0.1% | 348.22 | 349.12 / 347.28-351.73 | 6.08 (1.7%) | 325.81-348.36 | +2.8% / +6.0% | +1.8% | 38.2M |
| MSFT | 521.33 (10:05 iex) | +0.0% | 521.08 | 518.11 / 515.70-522.36 | 11.38 (2.2%) | 497.25-551.15 | -1.0% / +2.6% | -3.4% | 21.5M |
| NVDA | 212.91 (10:05 iex) | +0.3% | 212.21 | 211.04 / 210.18-213.31 | 6.15 (2.9%) | 211.26-243.37 | -6.2% / -4.7% | -2.3% | 106.8M |
| AMZN | 248.75 (10:05 iex) | -0.7% | 250.38 | 248.64 / 246.45-249.65 | 7.11 (2.8%) | 244.72-265.34 | -1.6% / -2.2% | -1.7% | 36.3M |
| GOOGL | 323.58 (10:05 iex) | -0.2% | 324.22 | 321.14 / 320.18-324.04 | 8.48 (2.6%) | 322.00-359.40 | -5.8% / -5.6% | -7.2% | 24.1M |
| META | 645.04 (10:05 iex) | -0.6% | 648.85 | 638.17 / 633.27-647.01 | 25.57 (3.9%) | 639.69-771.27 | -10.3% / -2.1% | -11.9% | 19.9M |
| TSLA | 368.48 (10:05 iex) | -1.6% | 374.58 | 372.95 / 365.31-375.93 | 12.03 (3.2%) | 345.88-388.86 | +1.3% / +3.2% | +3.3% | 37.1M |
| AVGO | 325.10 (10:05 iex) | +0.6% | 323.24 | 321.50 / 320.23-325.90 | 11.88 (3.7%) | 321.02-380.84 | -7.7% / -9.8% | -6.1% | 21.7M |
| AMD | 515.66 (10:05 iex) | +1.5% | 507.93 | 510.75 / 508.36-518.28 | 29.12 (5.7%) | 502.60-658.52 | -14.3% / -6.2% | -9.7% | 19.7M |
| ORCL | 126.12 (10:05 iex) | +0.5% | 125.54 | 124.87 / 124.39-126.78 | 6.66 (5.3%) | 122.76-146.40 | -7.6% / -12.2% | -6.6% | 29.6M |
| NFLX | 67.07 (10:05 iex) | +0.0% | 67.05 | 67.00 / 66.61-67.82 | 2.02 (3.0%) | 64.10-73.07 | -3.4% / -10.0% | -7.7% | 41.7M |
| CRM | 245.99 (10:05 iex) | -1.7% | 250.29 | 248.59 / 242.30-249.41 | 8.68 (3.5%) | 220.29-252.42 | +6.6% / +7.0% | +1.4% | 8.1M |
| JPM | 331.98 (10:05 iex) | -1.4% | 336.54 | 333.00 / 330.40-335.14 | 6.16 (1.8%) | 324.25-344.40 | +0.9% / -2.4% | +0.3% | 7.8M |
| GS | 884.59 (10:04 iex) | -0.8% | 891.30 | 880.07 / 870.82-884.64 | 24.29 (2.7%) | 859.03-935.83 | -0.5% / -7.3% | +0.0% | 2.3M |
| BAC | 50.77 (10:05 iex) | -0.6% | 51.08 | 50.73 / 50.30-50.88 | 1.29 (2.5%) | 49.26-56.74 | -4.0% / -11.8% | -1.2% | 42.7M |
| XOM | 181.53 (10:05 iex) | +1.9% | 178.23 | 179.37 / 179.00-182.06 | 3.77 (2.1%) | 159.27-180.31 | +5.0% / +7.9% | +2.0% | 11.4M |
| CVX | 231.18 (10:04 iex) | +2.0% | 226.68 | 228.19 / 227.98-231.76 | 4.86 (2.1%) | 201.96-229.04 | +6.0% / +8.2% | +3.4% | 7.3M |
| LLY | 1,285.26 (10:05 iex) | -1.6% | 1,306.69 | 1,304.15 / 1,275.01-1,307.92 | 39.62 (3.0%) | 1,131.21-1,321.21 | +8.9% / +10.2% | +4.4% | 2.3M |
| UNH | 421.58 (10:05 iex) | -0.8% | 424.98 | 424.30 / 420.34-425.25 | 13.24 (3.1%) | 362.60-426.55 | +9.8% / +9.8% | +4.5% | 6.1M |
| JNJ | 263.82 (10:05 iex) | -1.4% | 267.61 | 265.82 / 262.42-266.02 | 6.92 (2.6%) | 245.17-273.78 | +3.2% / +1.0% | +5.7% | 7.9M |
| WMT | 120.31 (10:05 iex) | -0.7% | 121.12 | 121.58 / 120.14-122.40 | 2.52 (2.1%) | 103.39-121.38 | +8.5% / +10.8% | +2.8% | 21.3M |
| COST | 1,010.88 (10:05 iex) | -0.7% | 1,018.21 | 1,016.90 / 1,009.75-1,021.45 | 15.82 (1.6%) | 883.10-1,018.86 | +6.7% / +8.5% | +4.1% | 2.3M |
| HD | 319.52 (10:05 iex) | -2.5% | 327.73 | 325.00 / 319.47-325.91 | 7.15 (2.2%) | 277.15-327.92 | +10.6% / +5.8% | +6.3% | 5.4M |
| CAT | 684.99 (10:05 iex) | -2.7% | 704.05 | 694.37 / 681.56-696.05 | 30.74 (4.4%) | 695.33-876.95 | -10.6% / -12.3% | -4.3% | 2.6M |
| BA | 184.88 (10:05 iex) | -1.4% | 187.55 | 185.81 / 182.40-185.81 | 3.98 (2.1%) | 183.38-201.40 | -1.1% / -7.1% | -0.6% | 8.1M |
| DAL | 76.20 (10:05 iex) | -3.9% | 79.26 | 77.37 / 76.10-77.48 | 2.98 (3.8%) | 74.14-85.93 | -1.8% / -2.2% | +1.5% | 7.5M |
| UAL | 97.55 (10:04 iex) | -4.4% | 102.00 | 100.01 / 97.55-100.98 | 4.78 (4.7%) | 94.54-115.71 | -3.8% / -7.0% | +0.7% | 5.0M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-23 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BEZ | 8.71 (10:04 iex) | +20.4% | 7.24 | 8.19 / 8.04-9.12 | 0.82 (11.3%) | 4.08-7.77 | +30.1% / -0.0% | +12.2% | 5.7M |
| SAIQ | 6.46 (10:03 iex) | +22.3% | 5.28 | 6.74 / 6.36-6.92 | 2.05 (38.8%) | 1.76-12.95 | -2.8% / -38.1% | +64.5% | 9.5M |
| RHI | 42.65 (10:04 iex) | +13.2% | 37.68 | 41.95 / 41.00-44.86 | 1.54 (4.1%) | 32.27-38.79 | +7.3% / -2.6% | +9.6% | 1.8M |
| CCI | 87.75 (10:05 iex) | +11.3% | 78.83 | 91.02 / 87.42-91.56 | 3.12 (4.0%) | 65.32-83.26 | +6.8% / +6.8% | -1.5% | 5.0M |
| BEX | 16.92 (10:04 iex) | -20.3% | 21.24 | 18.49 / 15.68-18.99 | 4.31 (20.3%) | 19.77-42.95 | -34.4% / -30.6% | -16.8% | 2.7M |
| LKQ | 18.20 (10:05 iex) | -19.0% | 22.47 | 18.16 / 17.21-18.21 | 0.68 (3.0%) | 21.23-23.48 | +0.7% / -5.1% | +0.5% | 3.3M |
| TNGX | 23.17 (10:05 iex) | -17.0% | 27.93 | 25.54 / 22.81-25.94 | 1.67 (6.0%) | 20.98-27.98 | +17.2% / +16.9% | +23.0% | 3.8M |
| PHAT | 5.84 (10:04 iex) | -16.7% | 7.01 | 6.72 / 5.58-6.76 | 0.40 (5.7%) | 6.52-7.72 | -1.5% / -12.7% | -6.5% | 1.2M |
