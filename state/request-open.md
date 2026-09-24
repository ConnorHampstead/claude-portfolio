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

# Pre-market brief: Thursday 2026-09-24

*Written 09:05 ET (15:05 Stockholm). The cash session opens 09:30 ET / 15:30 Stockholm.*

### 1. Tape
The bond market is in charge. On Wednesday the 10-year yield rose 15 bp to **5.11%**, its highest since 2007. The trigger was a hot S&P Global flash PMI (fastest activity since July 2021, input costs up on energy) plus a weak auction. Markets now price another Fed hike in October, after the mid-September hike. The S&P fell 0.75% and the Nasdaq 1.1% (verified: CNN, Yahoo). The selling is spreading this morning. Alpaca pre-market has SPY 764.39 (−0.4%), QQQ 734.98 (−0.8%), SMH −1.9%, ORCL −4.4%. WTI is +1.6% at about $93.7 and XOM/CVX are up about 1%. Xi Jinping's arrival and Bessent's extension of the trade truce to Jan 10, 2027 have not lifted futures. The regime is **risk-off, driven by rates**. Rate-sensitive groups (small caps, homebuilders, banks, utilities, REITs) are already below their 20- and 50-day averages, and the last leader, tech, is now cracking. **The short side has the edge today.**

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Initial jobless claims | **197K actual** vs 196K prior. Still near cycle lows and doesn't argue against a hike. Futures stayed weak. Continuing claims: consensus 1,750K, actual not verified | All; supports the rates-higher thesis |
| Pre-mkt | Pre-mkt | DRI earnings | Missed and trading lower (not a name I trade; the price was not verified) | none |
| 10:00 | 16:00 | New home sales | Still ahead. Builder sentiment is 32 and the MBA 30-year rate is 7.12% | XHB short |
| 11:00 | 17:00 | KC Fed manufacturing | Still ahead | minor |
| Intraday | — | Heavy slate of Fed speakers this week (10+ appearances; today's times not verified) | Hawkish risk | all |
| 13:00 (not verified) | 19:00 | 7-year note auction: weekly schedule inferred, not confirmed | Another weak auction would add to the move | IWM, XHB, BAC shorts |
| After close | ~22:05 | COST earnings | — | none (COST excluded under rule 8) |
| Fri 08:30 | 14:30 | Durable goods; PCE listed for Fri | Upcoming | all |

None of the names I hold or propose has a company-specific binary inside the horizon. Micron reports 9/30. That is not an SMH-level binary under rule 8, but it is part of why I won't short semis.

### 3. Open positions and resting entries
**BAC short** (267 @ 55.80, last 56.12). Thesis **intact**. Financials are still heavy: XLF is 54.57, next to its 20-day low of 54.46, and BAC is −7.4% vs its 20-day average. **The book state shows no live stop order.** The reconcile log shows only the 52.90 take-profit leg. I am re-sending the stop at **57.70**, the original level (1.4 ATR above entry, above the breakdown shelf) with target 52.90, through `manage`, so the position is protected. It is a hold.

**AAPL resting buy stop 346.00** (stop 338.50, target 358). Keep it. Last is 336.93, so the order only fills if AAPL breaks its record high in a falling tape. That would be real relative strength, which the order is designed to catch, and the Xi summit/truce news could plausibly provide it. The harness clears it before the weekend anyway.

### 4. New plays

**A. IWM short (sell-stop breakdown)**
| Field | Value |
|---|---|
| Ticker | IWM |
| Direction | Short |
| Catalyst | 10-year at 5.11% on 9/23 (19-year high), an October hike being priced after September's, claims 197K this morning; IWM pre-market 280.87 is already under its 20d low 281.03 |
| Thesis | Small caps are the most rate-sensitive broad equity group (floating-rate debt, no AI tailwind). IWM is −2.7%/−4.1% vs its 20d/50d averages while SPY is still above both. A clean break of the 20-day low in a rising-yield tape should run to about 2.5 ATR. |
| Entry | Sell stop 279.80 (below pre-market and the 20d low) |
| Stop | 285.80. That is above the prior close of 281.92 plus about 1 ATR; getting back there means the breakdown failed (6.0 = 1.7× ATR, 2.1%) |
| Target | 271.00 (+1.47R) |
| Risk tier | 1.0. The trade goes with the trend and the macro driver, on the index expression with the least single-name gap risk |
| Time horizon | 2–5 days |
| Conviction | 4 |
| P(target first) | 42% |
| Invalidation | The 10-year falls back under 5.0%, or a trade-deal headline from the Xi visit sparks a broad squeeze that retakes 283 |
| What I'd be wrong about | IWM is already at the bottom of its range after a 5-day decline, so shorts are crowded. One soft Fed-speaker line or a strong 7-year auction could reverse yields fast. |

**B. ORCL short (sell-stop continuation)**
| Field | Value |
|---|---|
| Ticker | ORCL |
| Direction | Short |
| Catalyst | 9/24: new layoff round, Project Jupiter data-center loans trading stressed after an S&P downgrade to just above junk, 10-year at 5.1%. Pre-market 138.18 (−4.4%), under the 20d low of 139.00 |
| Thesis | ORCL is the most balance-sheet-exposed AI-capex name, and 5% yields hit leveraged capex stories hardest. The stock has gone from the mid-160s to the 130s, and a fresh 20-day low on credit-stress news is a continuation setup, not an exhaustion one. |
| Entry | Sell stop 136.50 (below pre-market, so it needs follow-through after the open) |
| Stop | 144.60, just above the prior close of 144.56. A full gap fill means the news was absorbed (8.1 ≈ 1.04 ATR from entry, 5.9%) |
| Target | 124.50 (+1.48R) |
| Risk tier | 0.5. The ATR is 5.4% and the stock has gapped, so gap risk in both directions is unusual |
| Time horizon | 1–5 days |
| Conviction | 3 |
| P(target first) | 38% |
| Invalidation | ORCL reclaims 141 in the first hour; the review cancels it |
| What I'd be wrong about | Gap-downs on layoff news often get bought, since cost cuts are margin-positive. The price figures come from a thin, promotional news aggregator (timothysykes.com), although the Alpaca print of 138.18 confirms the move. |

**C. XHB short (probe)**
| Field | Value |
|---|---|
| Ticker | XHB |
| Direction | Short |
| Catalyst | MBA 30-year mortgage rate 7.12% (week to 9/18), NAHB sentiment 32 in September, 10-year at 5.11% on 9/23; new home sales at 10:00 today |
| Thesis | Homebuilders are the most direct equity expression of mortgage rates above 7%. XHB is −6.7% vs its 50d average and close to its 20d low of 95.26. |
| Entry | Sell stop 95.10 |
| Stop | 98.70, above the 9/23 close of 97.09 plus about 0.7 ATR (3.6 = 1.6 ATR) |
| Target | 89.80 (+1.47R) |
| Risk tier | 0.25. It is a probe because the thesis overlaps with IWM and BAC. The 07:50 pre-market print is thin |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target first) | 37% |
| Invalidation | A strong new-home-sales beat and XHB back above 97.50 |
| What I'd be wrong about | Builders ripped on Tuesday, which shows buyers are waiting. Daily mortgage rates fell for two days in a row (6.92% on 9/23). |

All three shorts express the same driver: rates keep rising. Together they risk 1.75% of equity. I accept the correlation because that driver is the tape's regime, and I kept the two narrower expressions at reduced size.

### 5. Both sides
- **Best short:** IWM sell stop 279.80 / stop 285.80 / target 271.00, P = 42%. **Taken.**
- **Best long:** XOM limit 160.50 / stop 155.00 / target 169.50, P = 40%. **Passed.** Oil-driven inflation is the same driver as my shorts, so XOM would be a natural hedge. But oil is −4.7% over 5 days and the Middle East diplomacy headlines could cut WTI sharply. The resting AAPL breakout is already my long exposure.

### 6. Passing on
- **XOM long** (limit 160.50 / stop 155 / target 169.50, P 0.40): Middle East diplomacy headline risk to oil. The 5-day trend is down.
- **SMH short** (sell stop 580 / stop 600 / target 552, P 0.33): this would short the leadership group, counter-trend (+10% in 5 days), with the MU report on 9/30 as a bullish catalyst. It is not worth shorting until 575 breaks.
- **XLU short** (sell stop 39.60 / stop 40.60 / target 38.20, P 0.38): the rate thesis is right, but in a risk-off tape defensives catch a bid, and I already have three rate shorts.
- **KRE short**: overlaps with the BAC short and financials exposure. No levels.
- **COST**: earnings after the close today (rule 8).

### 7. For the post-open review
- **ORCL:** if the 136.50 stop has not triggered and ORCL trades back above 141 by 10:05, cancel the entry. If it has filled and ORCL is back above 140, close it.
- **IWM:** if it filled and IWM is back above 282.50 (the prior close area) at 10:05, close it; the breakdown failed. If it has not filled and IWM is above 283, cancel.
- **XHB:** after new home sales at 10:00, cancel the entry if XHB trades above 97.50 (a big beat).
- **BAC:** confirm the 57.70 stop is live. If XLF reclaims 55.30 with BAC above 57, tighten the stop to 57.20.
- **AAPL:** no action unless it trades above 346 and immediately loses 342. In that case close the fill.

### 8. Book state
If everything fills, the longs are AAPL (about $23K) and the shorts are BAC, IWM, ORCL and XHB. Short notional: BAC about $15K, IWM about $48K, ORCL about $6K, XHB about $7K, so gross is about 97% (cap 150%) and net about −52% (cap ±100%).
Risk at stake: 0.5 (BAC) + 0.5 (AAPL) + 1.0 (IWM) + 0.5 (ORCL) + 0.25 (XHB) = **2.75%** against the 4% cap. Slots: 6 of 8.

```json
{
  "date": "2026-09-24",
  "no_trade": false,
  "session_note": "Rates-driven risk-off: 10y at 5.11% (2007 high), October hike being priced, claims 197K; shorting rate-sensitive breakdowns (IWM core, ORCL half, XHB probe), re-arming the missing BAC stop, keeping the AAPL breakout order.",
  "plays": [
    {
      "ticker": "IWM",
      "direction": "short",
      "entry_type": "stop",
      "entry": 279.80,
      "stop": 285.80,
      "targets": [271.00],
      "time_horizon": "2-5 days",
      "conviction": 4,
      "risk_pct": 1.0,
      "p_target_first": 0.42,
      "catalyst": "10y yield 5.11% on 9/23 (highest since 2007), October Fed hike being priced, jobless claims 197K on 9/24; IWM pre-market 280.87 already under 20d low 281.03.",
      "thesis": "Small caps are the most rate-sensitive broad equity group and are -2.7%/-4.1% vs 20d/50d while SPY is above both. A break of the 20-day low in a rising-yield tape should extend ~2.5 ATR.",
      "invalidation": "10y back below 5.0% or a Xi-visit trade headline squeezes IWM back above 283.",
      "bear_case": "Already at range lows after a 5-day slide; crowded short; one dovish Fed remark or strong 7y auction reverses yields."
    },
    {
      "ticker": "ORCL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 136.50,
      "stop": 144.60,
      "targets": [124.50],
      "time_horizon": "1-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "9/24 layoff round plus stressed Project Jupiter data-center loans after S&P downgrade; pre-market 138.18 (-4.4%) below 20d low 139.00, with 10y at 5.1%.",
      "thesis": "Most balance-sheet-exposed AI-capex name in a 5% yield world; a fresh 20d low on credit-stress news is continuation, not exhaustion.",
      "invalidation": "Reclaims 141 in the first hour of trade.",
      "bear_case": "Layoff gap-downs are often bought as margin-positive; news source partly thin/promotional."
    },
    {
      "ticker": "XHB",
      "direction": "short",
      "entry_type": "stop",
      "entry": 95.10,
      "stop": 98.70,
      "targets": [89.80],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.37,
      "catalyst": "MBA 30y mortgage 7.12%, NAHB sentiment 32 in September, 10y 5.11% on 9/23; new home sales 10:00 ET 9/24.",
      "thesis": "Homebuilders are the direct equity expression of 7%+ mortgages; XHB is -6.7% vs 50d and near its 20d low 95.26.",
      "invalidation": "Strong new home sales beat and XHB back above 97.50.",
      "bear_case": "Builders rallied hard Tuesday; daily mortgage rates eased two days running; overlaps IWM/BAC thesis."
    }
  ],
  "manage": [
    {
      "ticker": "BAC",
      "action": "update",
      "stop": 57.70,
      "target": 52.90,
      "reason": "Book state shows no live stop order; re-arming the original 57.70 stop (thesis intact, financials still at 20d lows)."
    }
  ],
  "passed": [
    {
      "ticker": "XOM",
      "direction": "long",
      "entry_type": "limit",
      "entry": 160.50,
      "stop": 155.00,
      "targets": [169.50],
      "p_target_first": 0.40,
      "reason": "Best long: oil-inflation hedge, but Middle East diplomacy headline risk and oil -4.7% over 5 days."
    },
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "stop",
      "entry": 580.00,
      "stop": 600.00,
      "targets": [552.00],
      "p_target_first": 0.33,
      "reason": "Counter-trend against leadership (+10% 5d) with MU earnings 9/30 a bullish catalyst."
    },
    {
      "ticker": "XLU",
      "direction": "short",
      "entry_type": "stop",
      "entry": 39.60,
      "stop": 40.60,
      "targets": [38.20],
      "p_target_first": 0.38,
      "reason": "Rate thesis right but defensives catch bids in risk-off; already three rate-driven shorts."
    }
  ]
}
```

Sources: [Yahoo live 9/24](https://finance.yahoo.com/markets/live/stock-market-today-thursday-september-24-dow-sp-500-nasdaq-080352893.html), [Bloomberg 9/24](https://www.bloomberg.com/news/articles/2026-09-23/stock-market-today-dow-s-p-live-updates), [CNN: 10-year hits 5.1%](https://www.cnn.com/2026/09/23/investing/us-bond-market-fed), [Yahoo 9/23 recap](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-23-dow-sp-500-nasdaq-080556640.html), [Timothy Sykes ORCL 9/24 (thin source)](https://www.timothysykes.com/news/oracle-corporation-orcl-news-2026_09_24/), [Benzinga ORCL](https://www.benzinga.com/markets/large-cap/26/09/61942244/whats-going-on-with-oracle-stock-wednesday-4), [Benzinga housing stocks](https://www.benzinga.com/markets/economic-data/26/09/61947115/mortgage-rates-highest-since-2024-5-housing-stocks-kbh-rkt-len), [NAHB September](https://www.nahb.org/news-and-economics/press-releases/2026/09/builder-sentiment-falls-on-higher-interest-rates-and-costs), [Noradar mortgage rates 9/23](https://www.noradarealestate.com/blog/todays-mortgage-rates-september-23-2026-update/), [Investing.com claims preview](https://www.investing.com/news/stock-market-news/jobless-claims-building-permits-and-new-home-sales-due-thursday-93CH-4913711), [Investing.com MU 9/30](https://www.investing.com/news/stock-market-news/micron-earnings-outlook-what-to-watch-ahead-of-the-september-30-report-93CH-4911385)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Thursday 2026-09-24. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,378.90**
- Cash: $116,455.05
- Session P&L so far: -0.12% (new entries are blocked at -3.0%)
- Gross exposure: $38,258 (38% of equity, cap 150%)
- Net exposure: $+8,106 (+8%, cap +/-100%)
- Risk at stake (entry to stop): $1,010 (1.00% of equity, cap 4.0%) — 3.00% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| BAC | short | 267 | 55.80 | 56.47 | -178 (-1.2%) | 57.7 (no live order) | 52.90 | Weakest large bank (-7.5% vs 20d avg). A break below today's opening low confirms the 20d-low support failed and opens a |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| AAPL | long | 67 | 346.00 | stop | 338.50 | 358.00 | 2026-09-23 |

### Record

4 closed trades: 2W / 2L, total +0.57R, net $+1,558 realized. Shorts taken: 1.

### Last 4 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| DAL | long | stop | +1.00R | $+999 | 46% |
| LLY | long | stop | +1.76R | $+1,654 | 52% |
| ROST | long | stop | -1.18R | $-336 | 47% |
| ANET | long | stop | -1.01R | $-758 | 45% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BAC | 56.47 (10:05 iex) | +0.8% | 56.00 | 56.39 / 56.00-56.48 | 1.38 (2.5%) | 55.73-63.83 | -7.4% / -9.0% | -3.3% | 37.6M |
| AAPL | 337.12 (10:05 iex) | +0.0% | 337.02 | 336.55 / 334.30-337.60 | 7.24 (2.1%) | 308.80-345.34 | +3.1% / +4.9% | +1.4% | 43.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 765.98 (10:05 iex) | -0.2% | 767.81 | 764.07 / 763.62-765.97 | 6.90 (0.9%) | 747.74-775.14 | +0.5% / +1.1% | +2.1% | 42.9M |
| QQQ | 737.41 (10:05 iex) | -0.5% | 741.21 | 735.29 / 734.62-737.77 | 9.60 (1.3%) | 699.27-748.35 | +3.3% / +4.3% | +5.3% | 32.8M |
| IWM | 280.67 (10:05 iex) | -0.4% | 281.92 | 281.33 / 280.32-281.73 | 3.50 (1.2%) | 281.03-299.61 | -2.7% / -4.1% | -0.7% | 21.6M |
| DIA | 513.12 (10:05 iex) | -0.2% | 514.30 | 512.85 / 511.51-514.03 | 5.39 (1.0%) | 511.11-536.49 | -2.0% / -2.3% | +0.1% | 3.3M |
| TLT | 80.51 (10:04 iex) | +0.1% | 80.46 | 80.35 / 80.33-80.52 | 0.74 (0.9%) | 80.22-83.28 | -1.5% / -2.0% | -0.5% | 32.7M |
| GLD | 391.33 (10:05 iex) | -0.4% | 392.88 | 391.94 / 390.86-392.06 | 7.34 (1.9%) | 388.39-424.95 | -2.3% / -0.4% | +0.3% | 10.4M |
| USO | 151.34 (10:01 iex) | +1.7% | 148.83 | 151.06 / 151.04-151.93 | 5.41 (3.6%) | 125.41-163.35 | +1.9% / +10.7% | -4.7% | 5.5M |
| SMH | 594.67 (10:05 iex) | -1.1% | 601.41 | 591.62 / 588.92-596.34 | 16.17 (2.7%) | 537.73-608.66 | +6.5% / +6.5% | +10.2% | 6.5M |
| XLK | 193.56 (10:04 iex) | -0.9% | 195.34 | 193.00 / 192.61-193.68 | 3.21 (1.6%) | 180.50-196.68 | +4.3% / +6.4% | +6.3% | 6.8M |
| XLF | 54.60 (10:05 iex) | +0.1% | 54.54 | 54.63 / 54.31-54.81 | 0.78 (1.4%) | 54.46-58.39 | -3.9% / -4.2% | -2.1% | 33.7M |
| XLE | 62.92 (10:05 iex) | +0.9% | 62.37 | 63.07 / 62.45-63.09 | 1.34 (2.1%) | 60.95-65.78 | -2.0% / +1.9% | -2.0% | 32.1M |
| XLV | 170.76 (10:05 iex) | +1.2% | 168.80 | 168.87 / 168.72-170.93 | 2.26 (1.3%) | 164.48-174.17 | -0.1% / +1.3% | +1.0% | 7.5M |
| XLI | 169.38 (10:05 iex) | -0.4% | 170.10 | 168.72 / 168.42-169.28 | 2.27 (1.3%) | 167.04-180.42 | -1.2% / -4.4% | +1.1% | 7.6M |
| XLY | 110.36 (10:05 iex) | -0.3% | 110.65 | 110.16 / 110.13-110.73 | 1.68 (1.5%) | 109.38-117.58 | -2.4% / -3.7% | +0.6% | 6.0M |
| XLP | 82.87 (10:05 iex) | +0.5% | 82.43 | 82.91 / 82.78-83.07 | 0.84 (1.0%) | 81.73-86.12 | -1.4% / -2.2% | -0.4% | 9.8M |
| XLU | 39.73 (10:05 iex) | -0.1% | 39.75 | 39.88 / 39.65-39.89 | 0.58 (1.5%) | 39.71-43.39 | -5.0% / -8.0% | -3.1% | 21.9M |
| XLB | 50.06 (10:04 iex) | -0.4% | 50.28 | 50.14 / 49.97-50.23 | 0.73 (1.5%) | 49.65-53.84 | -2.1% / -2.4% | +0.3% | 11.0M |
| XLRE | 41.89 (10:05 iex) | +0.1% | 41.84 | 42.02 / 41.88-42.09 | 0.53 (1.3%) | 41.81-45.08 | -3.1% / -5.2% | -1.4% | 5.3M |
| XLC | 113.20 (10:05 iex) | +0.6% | 112.56 | 112.52 / 112.52-113.63 | 1.91 (1.7%) | 109.95-115.61 | +0.3% / +1.4% | -0.1% | 4.9M |
| KRE | 70.63 (10:05 iex) | +0.4% | 70.38 | 70.61 / 70.35-70.81 | 1.24 (1.8%) | 70.36-75.07 | -3.7% / -5.8% | -2.7% | 13.1M |
| XHB | 97.01 (10:01 iex) | -0.1% | 97.09 | 96.93 / 96.42-97.33 | 2.20 (2.3%) | 95.26-106.55 | -2.5% / -6.7% | +0.9% | 1.8M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 337.12 (10:05 iex) | +0.0% | 337.02 | 336.55 / 334.30-337.60 | 7.24 (2.1%) | 308.80-345.34 | +3.1% / +4.9% | +1.4% | 43.7M |
| MSFT | 492.73 (10:05 iex) | -1.6% | 500.59 | 495.22 / 491.23-495.68 | 10.87 (2.2%) | 486.00-517.78 | +0.2% / +6.3% | +2.1% | 21.6M |
| NVDA | 222.46 (10:05 iex) | -1.4% | 225.51 | 222.08 / 221.09-223.23 | 5.49 (2.4%) | 208.93-234.50 | +2.0% / +4.8% | +5.4% | 132.7M |
| AMZN | 246.10 (10:05 iex) | -1.3% | 249.27 | 246.02 / 245.65-247.52 | 5.45 (2.2%) | 244.30-267.56 | -2.3% / -2.7% | +1.3% | 34.9M |
| GOOGL | 338.51 (10:05 iex) | +0.2% | 337.83 | 336.22 / 336.02-339.57 | 9.11 (2.7%) | 327.74-364.17 | -1.2% / -2.1% | -1.5% | 27.0M |
| META | 762.38 (10:05 iex) | +2.5% | 744.10 | 744.36 / 743.01-764.00 | 27.53 (3.7%) | 555.66-763.90 | +16.0% / +21.7% | +10.6% | 22.3M |
| TSLA | 379.05 (10:05 iex) | -0.3% | 380.12 | 377.64 / 376.13-379.75 | 13.01 (3.4%) | 342.53-386.70 | +4.7% / +8.9% | +6.2% | 39.3M |
| AVGO | 348.46 (10:05 iex) | -1.8% | 354.99 | 349.21 / 347.39-349.71 | 11.44 (3.2%) | 335.20-375.91 | -1.0% / -5.9% | +4.8% | 27.6M |
| AMD | 614.82 (10:05 iex) | +0.0% | 614.61 | 600.51 / 599.24-624.84 | 25.99 (4.2%) | 440.50-624.69 | +19.8% / +22.9% | +19.9% | 21.0M |
| ORCL | 134.60 (10:05 iex) | -6.9% | 144.56 | 137.32 / 133.50-139.30 | 7.82 (5.4%) | 139.00-170.70 | -3.5% / +1.9% | +1.0% | 31.8M |
| NFLX | 71.67 (10:05 iex) | +0.4% | 71.36 | 71.60 / 71.21-72.00 | 2.36 (3.3%) | 70.11-83.60 | -8.1% / -5.7% | -6.6% | 32.4M |
| CRM | 238.12 (10:04 iex) | +0.2% | 237.58 | 240.64 / 237.00-242.09 | 9.01 (3.8%) | 198.60-267.80 | -3.8% / +12.8% | -5.0% | 17.1M |
| JPM | 338.20 (10:05 iex) | +0.2% | 337.53 | 338.12 / 335.90-339.37 | 7.54 (2.2%) | 336.98-362.86 | -4.3% / -4.5% | -3.3% | 7.3M |
| GS | 923.99 (10:05 iex) | -1.3% | 936.36 | 931.00 / 919.22-933.41 | 28.16 (3.0%) | 922.00-1,057.38 | -6.2% / -8.6% | -0.2% | 2.0M |
| BAC | 56.47 (10:05 iex) | +0.8% | 56.00 | 56.39 / 56.00-56.48 | 1.38 (2.5%) | 55.73-63.83 | -7.4% / -9.0% | -3.3% | 37.6M |
| XOM | 163.44 (10:04 iex) | +1.4% | 161.23 | 163.09 / 162.03-164.16 | 4.05 (2.5%) | 155.32-169.64 | -0.5% / +1.8% | -1.3% | 14.8M |
| CVX | 206.60 (10:05 iex) | +0.5% | 205.51 | 207.41 / 205.90-207.42 | 4.77 (2.3%) | 197.82-217.78 | -1.6% / +3.1% | -2.9% | 10.0M |
| LLY | 1,186.34 (10:05 iex) | +3.1% | 1,150.99 | 1,156.67 / 1,151.00-1,188.25 | 27.76 (2.4%) | 1,113.29-1,235.78 | +0.0% / -2.1% | +1.2% | 2.4M |
| UNH | 372.29 (10:05 iex) | +0.3% | 371.29 | 371.92 / 368.50-373.66 | 10.27 (2.8%) | 366.00-404.04 | -3.7% / -7.0% | -1.1% | 5.1M |
| JNJ | 272.77 (10:05 iex) | +1.3% | 269.17 | 269.52 / 269.01-275.23 | 5.09 (1.9%) | 260.68-281.07 | -0.1% / +2.2% | +0.7% | 6.6M |
| WMT | 109.09 (10:05 iex) | -1.3% | 110.53 | 111.17 / 109.17-111.17 | 1.84 (1.7%) | 102.27-111.23 | +3.6% / +1.0% | +2.8% | 23.3M |
| COST | 904.68 (10:04 iex) | -0.0% | 904.70 | 909.29 / 904.68-909.43 | 11.77 (1.3%) | 885.50-964.45 | -1.2% / -3.2% | +1.2% | 2.1M |
| HD | 295.50 (10:04 iex) | -0.4% | 296.72 | 296.00 / 294.32-299.10 | 6.45 (2.2%) | 295.39-336.96 | -5.0% / -9.4% | -1.9% | 4.2M |
| CAT | 802.02 (10:05 iex) | -1.2% | 812.02 | 798.87 / 794.20-802.29 | 21.04 (2.6%) | 771.39-832.99 | +1.0% / -2.5% | +3.7% | 2.4M |
| BA | 196.09 (10:05 iex) | -1.9% | 199.93 | 198.62 / 194.44-199.49 | 5.75 (2.9%) | 195.46-215.29 | -3.1% / -7.1% | -1.0% | 6.2M |
| DAL | 81.52 (10:02 iex) | -0.3% | 81.75 | 80.88 / 80.88-82.35 | 2.17 (2.7%) | 75.99-84.99 | +2.5% / -2.9% | +5.0% | 6.8M |
| UAL | 110.39 (10:01 iex) | -0.3% | 110.72 | 109.66 / 109.16-111.67 | 3.77 (3.4%) | 104.15-119.73 | +1.1% / -5.1% | +4.2% | 3.7M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-09-24 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GRML | 14.30 (10:04 iex) | +27.8% | 11.19 | 12.75 / 12.13-14.44 | 2.12 (18.9%) | 2.82-18.21 | +114.7% / +40.3% | +273.6% | 19.5M |
| P | 129.80 (10:05 iex) | +18.4% | 109.65 | 113.95 / 113.51-131.40 | 5.69 (5.2%) | 89.64-113.80 | +9.7% / +16.8% | +12.3% | 7.1M |
| USDE | 15.03 (10:05 iex) | +16.7% | 12.87 | 12.77 / 12.67-15.16 | 1.62 (12.6%) | 5.50-14.19 | +53.5% / +162.3% | +107.6% | 6.2M |
| BEZ | 6.22 (10:03 iex) | +12.2% | 5.54 | 6.23 / 6.04-6.50 | 0.95 (17.2%) | 5.08-12.15 | -25.6% / -52.1% | -5.2% | 2.9M |
| NBIL | 27.18 (10:03 iex) | +10.6% | 24.59 | 25.77 / 25.25-28.20 | 3.36 (13.7%) | 18.80-31.45 | +4.1% / -0.3% | +16.1% | 3.4M |
| NEBX | 27.36 (09:59 iex) | +8.4% | 25.23 | 26.28 / 25.86-28.90 | 3.41 (13.5%) | 19.35-32.27 | +4.1% / -0.4% | +16.4% | 1.8M |
| NBIG | 18.75 (10:00 iex) | +10.5% | 16.96 | 17.75 / 17.40-19.42 | 2.30 (13.5%) | 12.96-21.68 | +4.2% / -0.4% | +16.1% | 2.0M |
| JAGX | 6.69 (10:03 iex) | -24.9% | 8.91 | 7.03 / 6.42-7.39 | 5.70 (64.0%) | 2.35-41.53 | +1.0% / -30.2% | +155.0% | 2.1M |
| ORCX | 17.66 (10:04 iex) | -13.8% | 20.49 | 18.40 / 17.37-19.00 | 2.32 (11.3%) | 19.10-28.88 | -8.4% / -0.4% | +1.3% | 2.6M |
| ORCU | 6.30 (10:04 iex) | -13.9% | 7.32 | 6.56 / 6.21-6.78 | 0.83 (11.3%) | 6.82-10.30 | -8.3% / -0.3% | +1.3% | 5.6M |
| VKTX | 35.96 (10:05 iex) | -13.7% | 41.65 | 36.02 / 35.11-36.64 | 2.47 (5.9%) | 28.40-43.10 | +25.9% / +22.8% | +41.1% | 4.8M |
