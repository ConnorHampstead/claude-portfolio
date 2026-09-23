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

# Pre-market brief: Wednesday 2026-09-23

*Written 09:20 ET (15:20 Stockholm). The cash session opens 09:30 ET / 15:30 Stockholm.*

### 1. Tape
The Nasdaq closed Tuesday at a second straight record, 27,244, on AI-infrastructure strength led by Meta's Muse agent. The S&P 500 was flat at about 7,765 and the Dow lost 0.4% (verified: Yahoo/CNBC recaps). WTI fell almost 3% to $89.62 on Tuesday, but USO is +1.3% pre-market at 146.01 (Alpaca). Futures are mixed: SPY 772.82 (−0.1%), QQQ 746.01 (−0.2%). The market is rotating, not moving as a whole. Semis are extended: SMH is +12% in 5 days and AMD +24%. Financials are breaking down. XLF is 3.8% under its 20-day average, BAC and KRE are sitting on their 20-day lows, and a reported 10-year yield near 5% with a near-flat curve is squeezing expected net interest margins. That yield figure comes from one aggregated search source and I have not confirmed it independently. **Edge:** long in mega-cap tech leadership, short in financials. The index itself has no directional edge today.

### 2. Calendar
| Time ET | Stockholm | Event | Status / consensus | Touches |
|---|---|---|---|---|
| Pre-mkt | Pre-mkt | GIS, PAYX, CTAS earnings | Out, but I did not check the prints. None of them is a name I trade | none |
| 10:30 | 16:30 | EIA weekly crude inventories | Still ahead. Oil is bouncing pre-market | DAL |
| Intraday (times not verified) | — | Fed: Powell, Bowman, Bostic speak | Still ahead. Powell on rates matters with the 10-year near 5% | BAC short, AAPL long |
| Thu 08:30 | 14:30 | Jobless claims; New Home Sales Thu | Upcoming | all |
| Fri 08:30 | 14:30 | Durable goods; PCE listed for Sep 26 | Upcoming | all |

None of these is a company-specific binary under rule 8. DAL reports on Oct 9 and the big banks in mid-October, both outside the horizon. AAPL has nothing scheduled.

### 3. Open positions
**DAL long** (457 sh @ 80.38, stop 82.40, target 84.90). Thesis **intact but weakening today.** Oil is bouncing pre-market and DAL was last printed at 82.54, 1.6% below its 83.92 close and 0.14 above the stop. The stop already locks in about +$920 (roughly +2R on the original risk). I'm leaving it where it is. The trade has paid, and widening a profit-locking stop because the open looks bad is exactly the reinterpretation I'm not supposed to make. If the open trades through 82.40 the gain is banked; if it holds, the 84.90 target is still 1.1 ATR away. **Hold, no change.**

No resting entries.

### 4. New plays

**A. BAC short (sell-stop breakdown)**
| Field | Value |
|---|---|
| Ticker | BAC |
| Direction | Short |
| Catalyst | The bank sector is breaking down this week (JPM −3%, BAC −2% on 9/22) on NIM pressure from a ~5% 10-year and a flat curve, plus BAC's weak IB-fee guide on 9/14. BAC closed at 56.20, just above its 20-day low of 56.06 |
| Thesis | BAC is the weakest large bank: −7.5% vs its 20-day average and −8.8% vs its 50-day. A break of the 20-day low starts a new leg down, and nothing company-specific is scheduled before mid-October earnings. |
| Entry | Sell stop 55.90 (under the 20-day low) |
| Stop | 57.70. That puts price back above Tuesday's close area and reclaims the breakdown; 1.8 is 1.25× ATR (1.44) |
| Target | 52.90 (+1.67R) |
| Risk tier | 0.5. It's a short into an already-stretched decline, where a snapback is the main risk |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target first) | 38% |
| Invalidation | Financials reverse together (XLF back above 56) or a dovish Powell steepens the curve |
| What I'd be wrong about | The sector is oversold after a 5-day slide, and buyers step in at the lows. A bull-steepening would help NIM expectations. |

**B. AAPL long (buy-stop breakout)**
| Field | Value |
|---|---|
| Ticker | AAPL |
| Direction | Long |
| Catalyst | Apple set an all-time high of 345.34 on 9/22, and the upgraded Mac mini and Mac Studio start delivering today (9/23). It's 343.04 pre-market (+1.0%), and mega-cap tech is leading |
| Thesis | A clean break above the record high, with the tape rewarding tech, should run about 1.5 ATR over the next few days. |
| Entry | Buy stop 346.00 |
| Stop | 338.50. That is back inside Tuesday's range; 7.5 is about 1.05× ATR (7.14) |
| Target | 358.00 (+1.6R) |
| Risk tier | 0.5. A breakout entry at a record high carries failure risk, and UBS has published a bearish target (iPhone 18 demand in China is weak) |
| Time horizon | 1–5 days |
| Conviction | 3 |
| P(target first) | 40% |
| Invalidation | The breakout fails back under 340 on the day it fills, or QQQ loses 740 |
| What I'd be wrong about | Breakouts at record highs often fail intraday. Pre-market was only 340.58 at 08:00, so the +1% is thin, and a rising 10-year hurts long-duration tech. |

### 5. Both sides
- **Best long:** AAPL buy stop 346 / stop 338.50 / target 358, P = 40%. **Taken.**
- **Best short:** BAC sell stop 55.90 / stop 57.70 / target 52.90, P = 38%. **Taken.**

### 6. Passing on
- **KRE short** (sell stop 70.80 / stop 72.90 / target 67.60, P 0.35): same thesis as BAC. I'm not doubling up on financials, and regional banks snap back more sharply.
- **SMH long on a pullback** (limit 590 / stop 572 / target 620, P 0.40): the leader, but +12% in 5 days is too stretched to chase. It's only worth owning on a pullback.
- **AMD:** +24% in 5 days with a 4.1% ATR. Extended, with no defined risk at this location. No levels.

### 7. For the post-open review
- **DAL:** if the stop fills at the open, record the win and do nothing else. If DAL holds 82.40 through 10:00 and is back above 83.50, leave it.
- **AAPL:** if it opens above 346 and immediately loses 343, close the fill.
- **BAC:** if it gaps below 55 at the open, the sell stop fills badly (about 2.7 from the stop). Cancel it if the opening fill is under 55.00 and price is bouncing.

### 8. Book state
If both entries fill: gross about 37% + 2 × ~40% notional ≈ 110% (cap 150%); net stays near +37% because the long and the short offset (cap ±100%). Risk at stake ≈ 1.0% (0.5 + 0.5; the DAL stop is above its entry), against the 4% cap. Slots: 3 of 8.

```json
{
  "date": "2026-09-23",
  "no_trade": false,
  "session_note": "Rotation tape: Nasdaq records on AI, financials breaking down on NIM/yield pressure. Pairing an AAPL breakout long with a BAC breakdown short, both half size; DAL held with profit-locked stop.",
  "plays": [
    {
      "ticker": "BAC",
      "direction": "short",
      "entry_type": "stop",
      "entry": 55.90,
      "stop": 57.70,
      "targets": [52.90],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "Bank-sector breakdown week of 9/21 (JPM -3%, BAC -2% on 9/22) on NIM pressure from ~5% 10y and flat curve; BAC closed 56.20 on its 20d low 56.06.",
      "thesis": "Weakest large bank, -7.5% vs 20d and -8.8% vs 50d avg. A break of the 20d low opens a further leg down with no company event before mid-October earnings.",
      "invalidation": "XLF reclaims 56 or a dovish Powell steepens the curve and financials reverse as a group.",
      "bear_case": "Sector oversold after a 5-day slide; support at the lows may produce a sharp snapback."
    },
    {
      "ticker": "AAPL",
      "direction": "long",
      "entry_type": "stop",
      "entry": 346.00,
      "stop": 338.50,
      "targets": [358.00],
      "time_horizon": "1-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.40,
      "catalyst": "All-time high 345.34 set 9/22; Mac mini/Mac Studio deliveries begin 9/23; pre-market +1% at 343.04 with mega-cap tech leading.",
      "thesis": "A clean break above the record high in a tape rewarding tech should extend roughly 1.5 ATR over several days.",
      "invalidation": "Breakout fails back below 340 on the fill day or QQQ loses 740.",
      "bear_case": "Record-high breakouts often fail intraday; UBS bearish target on weak China iPhone demand; rising 10y yield hurts duration."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "KRE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 70.80,
      "stop": 72.90,
      "targets": [67.60],
      "p_target_first": 0.35,
      "reason": "Same financials thesis as BAC short; avoiding doubling sector exposure and regionals snap back harder."
    },
    {
      "ticker": "SMH",
      "direction": "long",
      "entry_type": "limit",
      "entry": 590.00,
      "stop": 572.00,
      "targets": [620.00],
      "p_target_first": 0.40,
      "reason": "Leadership group but +12% in 5 days; only worth owning on a pullback, not chasing at 607."
    }
  ]
}
```

Sources: [Yahoo 9/22 market live](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-september-22-nasdaq-dow-sp-500-080625961.html), [CNBC 9/22](https://www.cnbc.com/2026/09/22/stock-market-today-live-updates.html), [Spectrum 9/22](https://spectrumlocalnews.com/us/snplus/business/2026/09/22/wall-street-september-22-2026), [StrongBuyAnalytics 9/23 outlook](https://strongbuyanalytics.com/stock-market-outlook), [24/7 Wall St. banks](https://247wallst.com/investing/2026/09/22/jpmorgan-chase-falls-3-despite-new-20b-qia-partnership-goldman-sachs-eases-bank-of-america-slips/), [Motley Fool BAC 9/14](https://www.fool.com/coverage/stock-market-today/2026/09/14/stock-market-today-sept-14-bank-of-america-slides-on-investment-banking-fee-surprise/), [Ad-hoc News DAL](https://www.ad-hoc-news.de/boerse/news/corporate-news/delta-air-lines-stock-gains-1-72-percent-as-earnings-near/70165633), [Stocktwits AAPL/UBS](https://stocktwits.com/news-articles/markets/equity/apple-s-i-phone-18-demand-improves-at-the-margin-china-remains-weak-spot-says-ubs-latest-target-implies-13-downside-potential/cZMEtpuRBJQ), [Public.com AAPL pre-market](https://public.com/stocks/aapl/pre-market), [Letters to a Young Investor calendar](https://letterstoayounginvestor.substack.com/p/weekly-economic-calendar-september-a9f), [FX Leaders MU](https://www.fxleaders.com/news/2026/09/22/micron-stock-forecast-mu-1000-earnings/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Wednesday 2026-09-23. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,556.45**
- Cash: $101,556.45
- Session P&L so far: -0.60% (new entries are blocked at -3.0%)
- Gross exposure: $23,182 (23% of equity, cap 150%)
- Net exposure: $+23,182 (+23%, cap +/-100%)
- Risk at stake (entry to stop): $502 (0.49% of equity, cap 4.0%) — 3.51% left for new plays
- Slots: 0 open + 1 resting entries of 8 — you may add at most 7 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

*No open positions.*

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| AAPL | long | 67 | 346.00 | stop | 338.50 | 358.00 | 2026-09-23 |

### Plays from earlier today that were not placed

*The broker refused these: the market had already crossed the stop entry's trigger before the open. There is no order and no position. Re-propose one in `plays` if it is still a trade at today's prices, or leave it; either way it is scored as a pass.*

| Symbol | Direction | Entry | Stop | Target | Why |
|---|---|---|---|---|---|
| BAC | short | stop 55.9 | 57.7 | 52.9 | stop entry 55.90 not placed: the market (55.885) had already crossed the trigger |

### Record

4 closed trades: 2W / 2L, total +0.57R, net $+1,558 realized. Shorts taken: 0.

### Last 4 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| DAL | long | stop | +1.00R | $+999 | 46% |
| LLY | long | stop | +1.76R | $+1,654 | 52% |
| ROST | long | stop | -1.18R | $-336 | 47% |
| ANET | long | stop | -1.01R | $-758 | 45% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is today's latest IEX trade, which pre-market is a thin single-venue print - confirm it for anything you trade. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 337.61 (10:05) | -0.6% | 339.75 | 341.07 / 337.00-341.73 | 7.14 (2.1%) | 308.21-345.34 | +4.3% / +5.9% | +2.5% | 43.4M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 770.53 (10:05) | -0.4% | 773.38 | 772.83 / 770.38-773.00 | 6.74 (0.9%) | 747.74-775.14 | +1.3% / +1.9% | +2.4% | 41.6M |
| QQQ | 742.99 (10:05) | -0.6% | 747.46 | 747.08 / 742.49-747.12 | 9.27 (1.2%) | 699.27-748.35 | +4.4% / +5.2% | +6.2% | 32.4M |
| IWM | 283.98 (10:05) | -1.1% | 287.21 | 285.99 / 283.84-286.17 | 3.38 (1.2%) | 281.03-299.61 | -1.2% / -2.4% | +0.7% | 21.1M |
| DIA | 516.53 (10:02) | -0.3% | 518.00 | 515.89 / 515.80-517.40 | 5.41 (1.0%) | 511.11-536.49 | -1.4% / -1.7% | -0.4% | 3.3M |
| TLT | 81.07 (10:03) | -0.8% | 81.75 | 81.48 / 80.98-81.50 | 0.66 (0.8%) | 80.46-83.28 | -0.1% / -0.5% | +1.3% | 31.8M |
| GLD | 393.32 (10:04) | -1.7% | 400.07 | 395.35 / 392.54-395.35 | 7.23 (1.8%) | 388.39-428.14 | -1.0% / +1.5% | +1.5% | 10.6M |
| USO | 147.67 (10:03) | +2.5% | 144.08 | 146.85 / 146.52-148.07 | 5.30 (3.7%) | 125.41-163.35 | -0.6% / +7.7% | -11.0% | 5.5M |
| SMH | 600.56 (10:04) | -1.1% | 607.46 | 605.38 / 597.94-606.28 | 16.01 (2.6%) | 537.73-608.66 | +8.0% / +7.5% | +12.1% | 6.5M |
| XLK | 195.41 (10:04) | -0.4% | 196.27 | 196.65 / 195.21-196.66 | 3.11 (1.6%) | 180.38-196.50 | +5.2% / +7.0% | +6.9% | 6.8M |
| XLF | 54.77 (10:05) | -0.1% | 54.80 | 54.49 / 54.47-54.91 | 0.81 (1.5%) | 54.55-58.39 | -3.8% / -3.8% | -3.3% | 32.8M |
| XLE | 62.66 (10:05) | +1.4% | 61.78 | 62.15 / 62.06-62.80 | 1.33 (2.1%) | 60.95-65.78 | -2.9% / +1.2% | -5.7% | 31.6M |
| XLV | 169.81 (10:04) | -0.0% | 169.89 | 170.10 / 169.53-170.97 | 2.26 (1.3%) | 164.48-175.15 | +0.4% / +2.1% | +1.7% | 7.4M |
| XLI | 170.80 (10:05) | +0.3% | 170.27 | 169.66 / 169.61-170.81 | 2.29 (1.3%) | 167.04-180.47 | -1.4% / -4.4% | +1.1% | 7.6M |
| XLY | 110.96 (10:05) | -1.2% | 112.33 | 111.90 / 110.79-112.08 | 1.60 (1.4%) | 109.38-118.31 | -1.2% / -2.3% | +1.5% | 5.9M |
| XLP | 82.37 (10:04) | -0.4% | 82.73 | 82.70 / 82.29-82.95 | 0.86 (1.0%) | 81.73-86.44 | -1.2% / -1.9% | -0.5% | 9.7M |
| XLU | 39.85 (10:05) | -1.7% | 40.53 | 40.36 / 39.84-40.41 | 0.57 (1.4%) | 40.45-43.39 | -3.6% / -6.4% | -1.2% | 21.1M |
| XLB | 50.17 (10:05) | -0.7% | 50.53 | 50.22 / 50.05-50.30 | 0.78 (1.5%) | 49.65-53.84 | -1.9% / -1.9% | +0.1% | 10.9M |
| XLRE | 42.19 (10:05) | -0.7% | 42.50 | 42.10 / 42.10-42.30 | 0.51 (1.2%) | 42.15-45.09 | -1.9% / -3.8% | -0.5% | 5.1M |
| XLC | 112.53 (10:05) | -0.9% | 113.53 | 113.52 / 112.40-113.52 | 1.97 (1.7%) | 109.95-115.61 | +1.2% / +2.3% | -0.1% | 4.7M |
| KRE | 70.88 (10:05) | -0.4% | 71.19 | 71.04 / 70.83-71.32 | 1.32 (1.9%) | 71.17-75.07 | -2.9% / -4.9% | -3.3% | 12.8M |
| XHB | 97.91 (10:03) | -1.5% | 99.41 | 98.25 / 97.77-98.42 | 2.15 (2.2%) | 95.26-106.92 | -0.6% / -4.7% | +2.3% | 1.8M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 337.61 (10:05) | -0.6% | 339.75 | 341.07 / 337.00-341.73 | 7.14 (2.1%) | 308.21-345.34 | +4.3% / +5.9% | +2.5% | 43.4M |
| MSFT | 500.70 (10:05) | +0.5% | 498.00 | 501.79 / 500.47-509.34 | 10.42 (2.1%) | 484.30-517.78 | -0.2% / +6.3% | +0.2% | 21.6M |
| NVDA | 227.99 (10:05) | -0.4% | 228.87 | 228.06 / 227.62-228.91 | 5.89 (2.6%) | 208.93-234.50 | +3.8% / +6.5% | +7.9% | 134.2M |
| AMZN | 250.07 (10:05) | -1.9% | 254.98 | 253.57 / 249.75-253.82 | 5.14 (2.0%) | 244.30-267.56 | -0.3% / -0.5% | +2.6% | 34.0M |
| GOOGL | 343.23 (10:05) | -2.3% | 351.16 | 349.78 / 341.90-349.90 | 8.64 (2.5%) | 327.74-364.17 | +2.6% / +1.7% | +1.8% | 26.2M |
| META | 753.83 (10:05) | +2.3% | 736.60 | 748.13 / 739.59-763.62 | 27.25 (3.7%) | 555.66-757.27 | +16.4% / +20.8% | +10.0% | 21.2M |
| TSLA | 386.29 (10:05) | +2.0% | 378.90 | 380.36 / 378.87-386.45 | 13.13 (3.5%) | 342.53-384.04 | +4.7% / +8.5% | +6.3% | 39.1M |
| AVGO | 358.17 (10:05) | -1.7% | 364.54 | 362.00 / 356.98-362.51 | 11.15 (3.1%) | 335.20-375.91 | +1.6% / -3.5% | +7.6% | 27.3M |
| AMD | 617.17 (10:05) | -1.1% | 623.77 | 621.73 / 614.51-624.44 | 25.51 (4.1%) | 440.50-624.52 | +23.2% / +25.1% | +23.7% | 21.2M |
| ORCL | 147.46 (10:05) | -1.2% | 149.20 | 148.33 / 145.81-148.33 | 7.96 (5.3%) | 139.00-170.70 | -0.4% / +5.4% | +6.3% | 31.3M |
| NFLX | 71.31 (10:04) | -1.2% | 72.16 | 72.08 / 71.08-72.24 | 2.46 (3.4%) | 70.11-83.60 | -7.7% / -4.7% | -7.4% | 32.2M |
| CRM | 236.56 (10:05) | +1.4% | 233.28 | 234.41 / 234.41-238.72 | 9.23 (4.0%) | 198.60-267.80 | -5.0% / +11.5% | -8.6% | 17.0M |
| JPM | 338.55 (10:05) | -0.4% | 340.00 | 337.25 / 337.23-339.67 | 7.77 (2.3%) | 337.30-362.86 | -3.9% / -3.9% | -3.5% | 7.2M |
| GS | 949.84 (10:04) | +0.0% | 949.49 | 935.08 / 935.08-950.72 | 28.34 (3.0%) | 922.00-1,058.34 | -5.4% / -7.7% | -2.8% | 2.0M |
| BAC | 56.09 (10:05) | -0.2% | 56.20 | 55.91 / 55.91-56.46 | 1.44 (2.6%) | 56.06-63.83 | -7.5% / -8.8% | -5.6% | 36.9M |
| XOM | 161.21 (10:04) | +1.6% | 158.71 | 159.82 / 159.68-161.65 | 3.97 (2.5%) | 155.32-169.64 | -2.1% / +0.5% | -6.3% | 15.1M |
| CVX | 205.80 (10:04) | +1.7% | 202.41 | 203.85 / 203.81-206.17 | 4.68 (2.3%) | 197.82-217.78 | -2.9% / +1.8% | -7.1% | 10.0M |
| LLY | 1,159.18 (10:04) | -0.9% | 1,170.14 | 1,176.26 / 1,155.35-1,188.31 | 26.83 (2.3%) | 1,113.29-1,264.73 | +1.3% / -0.5% | +3.0% | 2.4M |
| UNH | 367.61 (10:04) | -1.4% | 372.95 | 369.99 / 366.10-371.51 | 10.12 (2.7%) | 372.41-404.04 | -3.6% / -6.8% | -0.8% | 5.0M |
| JNJ | 270.33 (10:04) | +0.4% | 269.19 | 269.70 / 269.70-271.57 | 5.39 (2.0%) | 260.68-281.07 | -0.1% / +2.4% | +0.7% | 6.5M |
| WMT | 110.39 (10:05) | +0.2% | 110.12 | 110.24 / 110.17-111.20 | 1.81 (1.6%) | 102.27-110.19 | +3.5% / +0.5% | +1.9% | 23.5M |
| COST | 894.27 (10:04) | -0.6% | 899.41 | 898.60 / 893.70-901.19 | 12.30 (1.4%) | 885.50-969.05 | -2.1% / -3.8% | -0.2% | 2.1M |
| HD | 300.40 (10:04) | -1.6% | 305.35 | 302.49 / 299.72-303.98 | 6.15 (2.0%) | 295.39-337.01 | -2.8% / -7.0% | -0.0% | 4.1M |
| CAT | 807.46 (10:04) | -0.1% | 808.01 | 803.76 / 798.83-808.61 | 21.35 (2.6%) | 771.39-834.45 | +0.5% / -3.2% | +3.1% | 2.3M |
| BA | 202.99 (10:04) | +2.7% | 197.72 | 197.97 / 197.97-202.99 | 5.65 (2.9%) | 195.46-215.29 | -4.4% / -8.2% | -5.7% | 5.9M |
| DAL | 82.64 (10:05) | -1.5% | 83.92 | 82.73 / 82.25-83.10 | 2.20 (2.6%) | 75.99-84.99 | +5.1% / -0.4% | +6.4% | 6.8M |
| UAL | 113.11 (10:04) | -1.8% | 115.21 | 113.80 / 112.55-114.20 | 3.81 (3.3%) | 104.15-119.73 | +4.9% / -1.4% | +7.8% | 3.7M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-09-23 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| WHLR | 7.09 (10:05) | +279.1% | 1.87 | 5.21 / 4.89-8.27 | 0.64 (34.4%) | 1.65-14.78 | -64.4% / -91.2% | -40.8% | 1.2M |
| IPDN | 6.10 (09:55) | +56.4% | 3.90 | 6.92 / 5.96-7.67 | 0.76 (19.4%) | 2.96-6.60 | +7.8% / -48.5% | +17.1% | 1.7M |
| GDXD | 18.82 (10:01) | +14.4% | 16.45 | 18.70 / 18.70-18.92 | 1.88 (11.4%) | 14.25-21.03 | -4.5% / -43.8% | -14.0% | 3.9M |
| JAGX | 16.25 (10:02) | -52.8% | 34.46 | 14.80 / 14.80-18.90 | 3.90 (11.3%) | 2.35-41.53 | +280.0% / +160.3% | +922.9% | 1.5M |
| ALKT | 14.73 (10:05) | -18.5% | 18.09 | 15.70 / 14.21-15.70 | 0.95 (5.2%) | 17.79-20.87 | -7.4% / -5.3% | -6.0% | 1.5M |
| GDXU | 130.52 (10:05) | -13.9% | 151.51 | 137.29 / 128.94-137.29 | 15.31 (10.1%) | 121.45-200.30 | -2.7% / +19.7% | +12.8% | 1.6M |
| APPX | 12.05 (10:05) | -13.4% | 13.92 | 12.46 / 11.97-12.53 | 1.32 (9.5%) | 11.80-14.89 | +5.0% / -19.8% | -2.5% | 1.4M |
| BYND | 10.15 (10:03) | -11.8% | 11.51 | 11.05 / 9.87-11.05 | 0.80 (6.9%) | 9.81-14.59 | -3.0% / -19.7% | +15.2% | 1.0M |
| VOYG | 33.03 (10:04) | -12.0% | 37.53 | 32.70 / 32.19-33.54 | 2.21 (5.9%) | 31.96-38.33 | +8.6% / +11.7% | +8.8% | 1.3M |
| EXK | 9.37 (10:05) | -10.9% | 10.51 | 10.06 / 9.31-10.12 | 0.56 (5.4%) | 9.31-11.65 | -0.7% / +9.5% | +9.0% | 8.2M |
| AEHG | 7.93 (09:54) | -13.5% | 9.17 | 8.87 / 7.91-8.87 | 1.27 (13.9%) | 5.31-10.34 | +24.3% / -4.4% | +50.8% | 1.3M |
