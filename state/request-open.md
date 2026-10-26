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

# Pre-market brief: Monday 2026-10-26

*Clock note: Europe moved its clocks back on Sunday 25 Oct and the US has not yet. Stockholm is **ET + 5h** this week. The 09:30 ET open is 14:30 Stockholm.*

### 1. Tape
Friday closed in risk-off rotation. The Dow fell 1.23% (−653 pts) and the S&P 500 fell 0.52% to 7,623.68. The Nasdaq lost only 0.21% because chips bounced and industrials and consumer names took the hit. US crude topped $100 as fear of a renewed US-Iran conflict rose (verified: TheStreet, Yahoo). This morning is a relief bid. ES is +0.3%, NQ +0.25–0.55%, Dow futures +0.35–0.5%. Brent is −1.9% at about $114.5 on profit-taking, even though Houthi attacks on Saudi Arabia went on over the weekend. VIX is about 19.2, the 10-year yield about 4.99%, gold +0.5%. Alpaca pre-market shows the same picture: SPY +0.3%, SMH +1.3%, USO −2.4%, XLE −1.3%, AAPL −1.2% after reports of cut iPhone 18 Pro component orders. The market is looking ahead to the heaviest week of earnings season: MSFT and GOOGL Wednesday after the close, AMZN Thursday. It is also waiting for the FOMC decision on Wednesday, where a "hawkish pause" is expected, plus Q3 GDP and September PCE. The regime is defensive rotation with a pre-event bounce. I give the long side a small intraday edge today. Over the 1–5 day window I still see the edge with relative-strength longs against AI-capex shorts, which is how the book is already built.

### 2. Calendar
| Event | ET | Stockholm | Status | Touches |
|---|---|---|---|---|
| Chicago Fed NAI (Sep) | 08:30 | 13:30 | Released. Consensus −0.1; **I couldn't verify the actual figure.** No visible futures reaction. | none |
| Dallas Fed mfg (Oct) | 10:30 | 15:30 | Ahead | XLI |
| FOMC decision | Wed 14:00 | Wed 19:00 | Hold expected, hawkish tone | whole book |
| GOOGL, MSFT earnings | Wed AMC | Wed ~21:30 | Ahead | **GOOGL short: must be flat before** |
| AMZN, INTC, (AAPL/META likely) earnings | Thu AMC | Thu evening | Ahead | NVDA, ORCL by read-through |
| Q3 GDP / Sep PCE | Thu–Fri 08:30 | 13:30 | Ahead | all |
| **XOM Q3 earnings** | Fri 30 Oct, 06:30 ET | 11:30 | Ahead (verified, XOM IR) | **XOM long: exit by Thursday** |

### 3. Open positions
- **GOOGL short** (332.42 → 321.83, stop 330, target 320). Intact and 1.8 from target. It reports Wednesday after the close, so under rule 8 this must not be held into the print. Hold today. **If the target hasn't filled, tomorrow's (Tue 10/27) brief closes it.** Stop unchanged; 330 is about 1 ATR away and locks in +0.3R.
- **NVDA short** (212.38 → 213.20, stop 222, target 198). Intact but not working: the 20-day low at 210.18 held Friday. Hold. Friday's review rule carries over: if it trades above 218 by 10:05, cut the stop to 219.
- **ORCL short** (129.70 → 127.34, stop 130 at breakeven, target 116.50). Intact. Hold.
- **UAL short** (99.14 → 98.99, stop 103, target 92.50). Weakening: oil is down 2% today. The premise, a fresh oil high, is still in place but fading. Hold; the stop defines the risk. The review closes it if UAL trades above 102.
- **XLI short** (163.26 → 165.70, stop 166.20, target 158). Weakening. The cyclicals-under-oil-pressure thesis loses fuel as oil falls, and CAT is +1.3% pre-market. The stop is only 0.5 away and I am leaving it there. It sits above the zone that would mean XLI has reclaimed its range, and widening it would be hoping. If it stops, the thesis was wrong.
- **XLV long** (179.57 → 179.34, stop 176.40, target 184.80). Intact; defensive rotation is still the dominant flow. Hold.
- **XOM long** (180.75 → 180.70, stop 175.40, target 189). Weakening. The breakout over 180.26 is being retested as oil pulls back. It reports Fri 30 Oct pre-market, so **the exit deadline is the Thursday 10/29 post-open review.** I would not open this position today. For the review: close it if XOM is below 178 at 10:05 (failed breakout).
- No resting entries.

### 4. New plays
One slot left and 1.84% of risk room.

| Field | Value |
|---|---|
| Ticker | KRE |
| Direction | Long |
| Catalyst | Pressing the 72.80 20-day high (pre-market 72.65, +3.8% over 5 days) after regional-bank earnings came out clean in mid-October; the yield curve is steep, with the 10-year near 5% |
| Thesis | Regional banks are one of the few groups making new 20-day highs while the AI-capex trade unwinds. Wider net interest margins and a steeper curve support them. A break of the range top opens a measured move of about 1 range-height. |
| Entry | Buy stop 73.05 |
| Stop | 71.25: back inside the range, about 1.4 ATR, below last week's breakout base |
| Target | 76.20 (+1.75R) |
| Risk tier | 0.25, a probe: thin catalyst, and a hawkish FOMC is a two-sided risk for banks |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 37% |
| Invalidation | XLF loses 55.00, or the curve flattens hard after the FOMC |
| What I'd be wrong about | A 5%-yield, higher-for-longer Fed tightens credit and deposit pricing. Regional-bank rallies have repeatedly failed at range highs. |

Sources on the catalyst are thin and partly promotional (Seeking Alpha and Admiral pieces). The price levels are verified from Alpaca.

### 5. Both sides
- **Best long:** KRE breakout, taken above (73.05 / 71.25 / 76.20, P 37%).
- **Best short:** AAPL on the iPhone 18 Pro order cuts (market about 343.40, stop 352, target 326, P 33%). **Passed** because AAPL reports this week (expected Thursday; I couldn't verify the exact date), so rule 8 bars it. Next best: an AVGO re-break of its 20-day low with a sell stop at 319. **Passed** because the book already carries three AI and tech shorts.

### 6. Passing on
- **AAPL short:** company earnings inside the horizon (rule 8).
- **META, AMZN shorts:** own earnings Wednesday/Thursday (rule 8).
- **AVGO short (stop entry 319, stop 334, target 296, P 33%):** would stack a fourth AI short into MSFT and GOOGL earnings.
- **TLT long breakout (buy stop 82.05, stop 80.70, target 84.20, P 35%):** the FOMC and PCE are a coin flip on the inflation side, and the slot went to KRE.
- **XP, NU (Brazil election crash):** chasing a 25–50% gap with no defined structure.

### 7. For the post-open review
- **NVDA:** if it trades above 218, cut the stop to 219.
- **UAL:** if it trades above 102, close it.
- **XOM:** if it is below 178 at 10:05, close it (failed breakout as oil falls). Otherwise hold, with a hard exit by the Thu 10/29 review.
- **XLI:** no action. Let the 166.20 stop decide.
- **GOOGL:** if the target is not hit, tomorrow's brief sends a `close`.
- **KRE:** if it is unfilled and SPY is below 758.68 (the 20-day low) at 10:05, cancel it.

### 8. Book state
If KRE fills: gross about 112% of equity (cap 150%), net about −2% (cap ±100%), 8 of 8 slots. Risk at stake about 2.41% of equity (cap 4%).

```json
{
  "date": "2026-10-26",
  "no_trade": false,
  "session_note": "Pre-FOMC/mega-cap-earnings relief bid with oil -2%; book already short AI capex and long defensives/energy, so the last slot goes to a KRE 20d-high breakout probe.",
  "plays": [
    {
      "ticker": "KRE",
      "direction": "long",
      "entry_type": "stop",
      "entry": 73.05,
      "stop": 71.25,
      "targets": [76.20],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.37,
      "catalyst": "KRE pressing its 72.80 20-day high on 2026-10-26 (+3.8% 5d) after clean mid-October regional-bank earnings, with a steep curve and the 10y near 5%.",
      "thesis": "Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support them. A range-top break opens a measured move of about one range-height.",
      "invalidation": "XLF loses 55.00, or the curve flattens hard after Wednesday's FOMC.",
      "bear_case": "Higher-for-longer at 5% squeezes credit and deposits; KRE range-high breakouts have repeatedly failed."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "AAPL",
      "direction": "short",
      "entry_type": "market",
      "entry": 343.40,
      "stop": 352.00,
      "targets": [326.00],
      "p_target_first": 0.33,
      "reason": "Best short (iPhone 18 Pro order cuts), but its own earnings are inside the horizon (rule 8)."
    },
    {
      "ticker": "AVGO",
      "direction": "short",
      "entry_type": "stop",
      "entry": 319.00,
      "stop": 334.00,
      "targets": [296.00],
      "p_target_first": 0.33,
      "reason": "Would be a fourth AI/tech short stacked into MSFT and GOOGL earnings and the FOMC."
    },
    {
      "ticker": "TLT",
      "direction": "long",
      "entry_type": "stop",
      "entry": 82.05,
      "stop": 80.70,
      "targets": [84.20],
      "p_target_first": 0.35,
      "reason": "20d-high breakout, but FOMC and PCE make the inflation side a coin flip; the slot went to KRE."
    }
  ]
}
```

Sources: [Yahoo live](https://finance.yahoo.com/markets/live/stock-market-today-monday-october-26-dow-sp-500-nasdaq-101153035.html), [US News/Reuters futures](https://money.usnews.com/investing/news/articles/2026-10-26/us-stock-futures-edge-up-as-oil-falls-heading-into-earnings-barrage), [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-26/us-stock-futures-gain-ahead-of-big-tech-earnings-fed-decision), [Tradingeconomics Brent](https://tradingeconomics.com/commodity/brent-crude-oil), [CNBC oil](https://www.cnbc.com/2026/10/26/oil-prices-today-wti-brent.html), [Yahoo Friday close](https://finance.yahoo.com/markets/world-indices/articles/major-us-stock-indexes-fared-201458598.html), [TheStreet Oct 23](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-23-2026), [Stocktitan earnings week](https://www.stocktitan.net/articles/earnings-calendar-week-of-october-26-2026), [XOM IR](https://investor.exxonmobil.com/company-information/press-releases/detail/1212/exxonmobil-to-release-third-quarter-2026-financial-results), [Yahoo AAPL](https://finance.yahoo.com/markets/stocks/articles/apple-shares-fall-1-9-105051749.html), [Benzinga movers](https://www.benzinga.com/trading-ideas/movers/26/10/62582848/why-surgery-partners-shares-are-trading-higher-by-over-20-here-are-20-stocks-moving-premarket), [Seeking Alpha KRE](https://seekingalpha.com/news/4531121-top-regional-bank-stocks-by-sa-quant-as-ubs-najarian-is-bullish-on-sector-for-2026), [Admiral Markets](https://admiralmarkets.com/analytics/traders-blog/midland-states-bancorp-stock-msbi-regional-banks)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:12 ET** (14:12 UTC, 15:12 Stockholm), Monday 2026-10-26. The cash session opened 43 min ago and closes at 16:00 ET (21:00 Stockholm).
- Equity: **$102,790.43**
- Cash: $65,798.82
- Session P&L so far: -0.36% (new entries are blocked at -3.0%)
- Gross exposure: $77,272 (75% of equity, cap 150%)
- Net exposure: $+36,992 (+36%, cap +/-100%)
- Risk at stake (entry to stop): $1,941 (1.89% of equity, cap 4.0%) — 2.11% left for new plays
- Slots: 6 open + 0 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 73.31 | +36 (+0.3%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| NVDA | short | 26 | 212.38 | 214.29 | -50 (-0.9%) | 222.00 | 198.00 | A break of the 212.85 20d low confirms Monday's bounce failed in the bellwether and opens a move toward 198. |
| ORCL | short | 33 | 129.70 | 125.30 | +145 (+3.4%) | 130.00 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |
| UAL | short | 103 | 99.14 | 101.30 | -223 (-2.2%) | 103.00 | 92.50 | Jet fuel is airlines' largest variable cost; a fresh oil high with a widening Gulf conflict hits margins directly, and U |
| XLV | long | 160 | 179.57 | 180.77 | +192 (+0.7%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |
| XOM | long | 97 | 180.75 | 183.49 | +265 (+1.5%) | 175.40 | 189.00 | Energy remains the leading sector; a break of the 180.26 20-day high with oil at a 5-month high extends the trend. |

### Record

25 closed trades: 10W / 15L, total +1.83R, net $+2,434 realized. Shorts taken: 26.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLI | short | stop | -1.00R | $-526 | 36% |
| GOOGL | short | target | +1.42R | $+362 | 35% |
| CVX | long | stop | -0.23R | $-117 | 40% |
| AMD | short | target | +1.17R | $+575 | 42% |
| HD | long | target | +1.47R | $+373 | 37% |

### Ideas you passed on, replayed against the tape

62 resolved: 18 reached target first, 30 stop first, 11 never reached the entry, 3 expired, 0 ambiguous. Average -0.08R across the 51 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-19 pre-market | AMD | short | Same idea as the SMH short with twice the noise; one semi short is enough. | never filled | - | 38% |
| 2026-10-19 pre-market | BAC | short | Post-earnings damage already priced; my last bank short stopped out. | never filled | - | 30% |
| 2026-10-14 pre-market | CVX | long | Best long (20d-high breakout) but duplicates the XOM energy exposure. | target | +1.70R | 40% |
| 2026-10-19 pre-market | AMZN | long | Buying an upgrade gap in a heavy data-center spender while the capex-credit stor | stop | -1.06R | 38% |
| 2026-10-20 pre-market | AAPL | short | Analyst downgrade gap of only 1 ATR in a mega-cap that has held up defensively. | stop | -0.99R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| KRE | 73.29 (10:12 iex) | +1.1% | 72.46 | 72.52 / 72.52-73.36 | 1.29 (1.8%) | 67.79-72.80 | +3.5% / +0.4% | +3.8% | 16.3M |
| NVDA | 214.30 (10:12 iex) | +1.6% | 210.96 | 213.10 / 212.61-215.98 | 5.98 (2.8%) | 210.18-243.37 | -6.5% / -5.1% | -1.5% | 106.2M |
| ORCL | 125.12 (10:12 iex) | -0.8% | 126.16 | 126.06 / 123.81-126.30 | 6.63 (5.3%) | 122.76-146.40 | -6.8% / -11.4% | -1.6% | 29.4M |
| UAL | 101.31 (10:12 iex) | +3.5% | 97.93 | 98.80 / 98.37-101.50 | 4.90 (5.0%) | 94.54-115.20 | -7.0% / -10.3% | +1.9% | 5.1M |
| XLV | 180.78 (10:12 iex) | +0.8% | 179.28 | 179.76 / 179.76-181.15 | 3.14 (1.7%) | 165.19-182.25 | +3.9% / +5.0% | +1.5% | 8.7M |
| XOM | 183.43 (10:12 iex) | +0.1% | 183.21 | 181.86 / 181.52-184.34 | 3.93 (2.1%) | 159.27-183.75 | +7.2% / +10.5% | +2.4% | 11.4M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 764.01 (10:12 iex) | +0.5% | 759.97 | 762.25 / 761.63-764.45 | 7.18 (0.9%) | 758.68-781.62 | -1.3% / -0.9% | -0.4% | 40.8M |
| QQQ | 707.97 (10:12 iex) | +0.5% | 704.40 | 707.07 / 705.58-709.57 | 12.06 (1.7%) | 701.16-762.86 | -4.2% / -2.9% | -0.8% | 37.0M |
| IWM | 277.82 (10:12 iex) | +0.8% | 275.75 | 276.17 / 276.00-278.05 | 3.69 (1.3%) | 269.88-284.64 | -0.5% / -3.6% | +2.0% | 25.6M |
| DIA | 524.32 (10:12 iex) | +0.6% | 521.37 | 523.88 / 522.64-524.63 | 5.33 (1.0%) | 504.59-528.45 | +0.9% / -0.1% | +0.4% | 3.4M |
| TLT | 81.83 (10:12 iex) | +0.6% | 81.34 | 81.66 / 81.65-81.85 | 0.83 (1.0%) | 76.43-81.92 | +3.3% / +1.3% | +1.6% | 48.8M |
| GLD | 366.81 (10:12 iex) | +0.1% | 366.61 | 367.30 / 365.54-367.50 | 5.33 (1.5%) | 364.33-385.22 | -3.3% / -7.1% | -4.0% | 8.3M |
| USO | 165.32 (10:12 iex) | -2.5% | 169.53 | 166.11 / 164.86-166.68 | 4.63 (2.7%) | 141.76-169.96 | +11.0% / +15.7% | +4.8% | 5.1M |
| SMH | 532.99 (10:12 iex) | +1.1% | 527.20 | 531.39 / 530.20-537.13 | 18.37 (3.5%) | 520.53-639.47 | -10.0% / -8.3% | -2.3% | 8.4M |
| XLK | 184.19 (10:12 iex) | +0.5% | 183.23 | 184.11 / 183.43-184.96 | 4.14 (2.3%) | 181.50-203.25 | -5.2% / -3.3% | -0.1% | 8.8M |
| XLF | 56.28 (10:12 iex) | +0.7% | 55.90 | 56.07 / 56.00-56.34 | 0.71 (1.3%) | 52.81-56.67 | +2.2% / -0.1% | +0.7% | 36.4M |
| XLE | 69.44 (10:12 iex) | +0.2% | 69.33 | 68.63 / 68.62-69.86 | 1.47 (2.1%) | 60.95-69.72 | +6.0% / +8.1% | +1.6% | 32.1M |
| XLV | 180.78 (10:12 iex) | +0.8% | 179.28 | 179.76 / 179.76-181.15 | 3.14 (1.7%) | 165.19-182.25 | +3.9% / +5.0% | +1.5% | 8.7M |
| XLI | 166.16 (10:12 iex) | +0.9% | 164.62 | 165.52 / 165.44-166.23 | 2.68 (1.6%) | 162.97-172.34 | -2.1% / -4.3% | -1.9% | 7.5M |
| XLY | 115.03 (10:12 iex) | +1.7% | 113.10 | 113.96 / 113.82-115.18 | 1.56 (1.4%) | 107.99-116.22 | +1.0% / -0.2% | +0.6% | 7.2M |
| XLP | 88.61 (10:12 iex) | +0.4% | 88.26 | 88.08 / 88.06-88.76 | 1.37 (1.6%) | 80.10-89.99 | +4.7% / +4.9% | +0.7% | 14.0M |
| XLU | 42.67 (10:12 iex) | +0.3% | 42.56 | 42.45 / 42.45-42.81 | 0.69 (1.6%) | 39.03-42.88 | +3.5% / +2.0% | +0.8% | 36.1M |
| XLB | 51.53 (10:12 iex) | +0.4% | 51.31 | 51.45 / 51.34-51.59 | 0.67 (1.3%) | 47.81-51.71 | +2.8% / +0.8% | +0.8% | 11.3M |
| XLRE | 42.93 (10:12 iex) | +0.8% | 42.57 | 42.57 / 42.57-42.97 | 0.65 (1.5%) | 40.28-43.21 | +2.5% / -0.3% | +1.0% | 8.0M |
| XLC | 104.52 (10:12 iex) | -0.9% | 105.51 | 105.11 / 104.07-105.17 | 1.69 (1.6%) | 105.50-113.17 | -4.5% / -5.3% | -4.4% | 6.5M |
| KRE | 73.29 (10:12 iex) | +1.1% | 72.46 | 72.52 / 72.52-73.36 | 1.29 (1.8%) | 67.79-72.80 | +3.5% / +0.4% | +3.8% | 16.3M |
| XHB | 98.95 (10:12 iex) | +0.6% | 98.38 | 98.64 / 98.09-99.14 | 2.34 (2.4%) | 91.87-99.28 | +2.6% / -0.7% | +3.7% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 343.95 (10:12 iex) | -1.1% | 347.73 | 343.92 / 341.03-346.21 | 6.19 (1.8%) | 325.81-351.73 | +2.6% / +5.5% | +1.2% | 38.7M |
| MSFT | 525.66 (10:12 iex) | +0.2% | 524.51 | 527.84 / 521.69-529.12 | 11.04 (2.1%) | 502.22-551.15 | -0.4% / +3.2% | -0.9% | 20.3M |
| NVDA | 214.30 (10:12 iex) | +1.6% | 210.96 | 213.10 / 212.61-215.98 | 5.98 (2.8%) | 210.18-243.37 | -6.5% / -5.1% | -1.5% | 106.2M |
| AMZN | 249.38 (10:12 iex) | +0.6% | 248.00 | 249.47 / 247.23-250.49 | 7.08 (2.9%) | 244.72-265.34 | -2.5% / -3.0% | -0.8% | 35.9M |
| GOOGL | 319.08 (10:12 iex) | -0.4% | 320.21 | 320.89 / 317.62-321.35 | 8.39 (2.6%) | 320.18-359.40 | -6.7% / -6.6% | -6.0% | 23.8M |
| META | 631.70 (10:12 iex) | -1.7% | 642.62 | 638.64 / 629.02-641.70 | 25.28 (3.9%) | 633.27-771.27 | -10.5% / -3.2% | -9.4% | 19.3M |
| TSLA | 393.56 (10:12 iex) | +5.7% | 372.22 | 383.82 / 383.73-394.93 | 11.70 (3.1%) | 345.88-388.86 | +0.6% / +2.3% | +4.9% | 36.5M |
| AVGO | 325.67 (10:12 iex) | +1.2% | 321.68 | 324.63 / 323.25-327.82 | 11.79 (3.7%) | 320.23-380.84 | -7.8% / -9.7% | -2.2% | 21.7M |
| AMD | 518.20 (10:12 iex) | +0.3% | 516.79 | 523.20 / 514.33-526.86 | 29.27 (5.7%) | 502.60-658.52 | -12.0% / -4.7% | -2.3% | 19.5M |
| ORCL | 125.12 (10:12 iex) | -0.8% | 126.16 | 126.06 / 123.81-126.30 | 6.63 (5.3%) | 122.76-146.40 | -6.8% / -11.4% | -1.6% | 29.4M |
| NFLX | 65.23 (10:12 iex) | -0.9% | 65.85 | 65.15 / 64.86-65.50 | 2.10 (3.2%) | 64.10-73.07 | -4.8% / -11.3% | -6.6% | 42.4M |
| CRM | 247.71 (10:10 iex) | -0.3% | 248.57 | 247.76 / 245.93-250.99 | 8.74 (3.5%) | 220.29-252.42 | +5.5% / +5.9% | +3.3% | 8.0M |
| JPM | 335.96 (10:12 iex) | +1.3% | 331.58 | 334.00 / 333.16-336.21 | 6.37 (1.9%) | 324.25-344.40 | -0.5% / -3.7% | -2.4% | 7.5M |
| GS | 888.79 (10:12 iex) | +1.5% | 875.68 | 886.50 / 881.32-891.88 | 24.44 (2.8%) | 859.03-932.00 | -1.9% / -8.6% | -0.6% | 2.3M |
| BAC | 51.26 (10:12 iex) | +1.4% | 50.56 | 50.73 / 50.73-51.49 | 1.30 (2.6%) | 49.26-56.67 | -4.4% / -12.3% | -1.3% | 42.7M |
| XOM | 183.43 (10:12 iex) | +0.1% | 183.21 | 181.86 / 181.52-184.34 | 3.93 (2.1%) | 159.27-183.75 | +7.2% / +10.5% | +2.4% | 11.4M |
| CVX | 232.78 (10:12 iex) | -0.2% | 233.21 | 231.70 / 230.53-233.99 | 4.99 (2.1%) | 201.96-233.74 | +8.3% / +10.9% | +3.7% | 7.4M |
| LLY | 1,285.22 (10:12 iex) | +0.9% | 1,273.46 | 1,286.39 / 1,277.10-1,296.90 | 41.34 (3.2%) | 1,131.21-1,321.21 | +5.7% / +7.3% | +1.3% | 2.3M |
| UNH | 419.38 (10:12 iex) | +0.3% | 418.09 | 418.99 / 415.87-420.75 | 13.08 (3.1%) | 362.60-426.55 | +7.4% / +7.9% | +4.2% | 6.1M |
| JNJ | 270.24 (10:12 iex) | +2.4% | 263.81 | 266.74 / 265.75-272.25 | 7.03 (2.7%) | 245.17-273.78 | +1.8% / -0.5% | +3.2% | 7.9M |
| WMT | 121.54 (10:12 iex) | +1.4% | 119.89 | 119.65 / 119.58-121.61 | 2.63 (2.2%) | 103.39-122.40 | +6.9% / +9.6% | +0.9% | 21.3M |
| COST | 1,014.27 (10:12 iex) | +1.1% | 1,003.32 | 1,000.96 / 999.08-1,012.41 | 16.40 (1.6%) | 903.77-1,021.45 | +4.7% / +6.9% | +1.4% | 2.2M |
| HD | 320.36 (10:12 iex) | +0.2% | 319.83 | 319.50 / 317.78-321.31 | 7.61 (2.4%) | 277.15-327.92 | +7.5% / +3.4% | +3.3% | 5.3M |
| CAT | 685.00 (10:12 iex) | -0.1% | 685.37 | 685.41 / 679.61-691.33 | 29.72 (4.3%) | 679.61-874.87 | -12.0% / -14.1% | -6.0% | 2.7M |
| BA | 187.74 (10:12 iex) | -0.3% | 188.35 | 188.26 / 186.08-189.50 | 4.18 (2.2%) | 182.40-196.93 | -0.4% / -6.4% | -1.0% | 8.1M |
| DAL | 78.52 (10:12 iex) | +2.3% | 76.78 | 77.07 / 77.06-78.65 | 3.08 (4.0%) | 74.14-85.93 | -4.4% / -4.9% | +1.9% | 7.4M |
| UAL | 101.31 (10:12 iex) | +3.5% | 97.93 | 98.80 / 98.37-101.50 | 4.90 (5.0%) | 94.54-115.20 | -7.0% / -10.3% | +1.9% | 5.1M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-26 10:12 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| CLRO | 5.48 (10:12 iex) | +68.6% | 3.25 | 4.33 / 4.02-5.81 | 0.59 (18.1%) | 1.62-6.00 | -9.4% / -25.9% | +8.7% | 3.4M |
| SGRY | 23.00 (10:12 iex) | +46.0% | 15.75 | 23.03 / 22.95-23.14 | 0.55 (3.5%) | 13.11-16.16 | +9.5% / +10.7% | +7.8% | 1.8M |
| XNCR | 30.32 (10:11 iex) | +20.4% | 25.18 | 32.31 / 28.93-33.60 | 1.41 (5.6%) | 21.97-26.35 | +2.4% / -0.5% | +10.2% | 1.4M |
| SAIQ | 7.30 (10:12 iex) | +19.3% | 6.12 | 6.92 / 6.54-7.54 | 1.60 (26.1%) | 1.76-12.95 | +17.3% / -27.4% | +93.7% | 9.8M |
| RRC | 52.71 (10:12 iex) | +15.8% | 45.52 | 50.64 / 50.00-53.36 | 1.21 (2.7%) | 36.75-45.73 | +11.4% / +12.0% | +5.3% | 2.7M |
| TSLG | 5.44 (10:12 iex) | +11.7% | 4.87 | 5.18 / 5.18-5.47 | 0.31 (6.4%) | 4.28-5.36 | +0.1% / +2.0% | +9.2% | 60.6M |
| XP | 14.88 (10:12 iex) | -51.1% | 30.41 | 14.51 / 13.78-15.78 | 1.43 (4.7%) | 19.78-32.73 | +8.7% / +35.4% | +4.0% | 13.2M |
| EWZS | 10.83 (10:12 iex) | -35.3% | 16.74 | 10.88 / 10.30-11.49 | 0.55 (3.3%) | 12.71-17.15 | +7.9% / +19.9% | +6.7% | 2.7M |
| AIOK | 8.77 (09:56 sip) | -27.0% | 12.02 | 9.72 / 8.12-9.88 | 2.14 (17.8%) | 3.90-15.59 | - / - | +186.2% | 4.0M |
| STNE | 8.07 (10:12 iex) | -29.7% | 11.48 | 7.13 / 7.06-8.22 | 0.54 (4.7%) | 8.95-12.49 | +3.6% / +12.0% | +1.8% | 7.0M |
| PAGS | 8.52 (10:12 iex) | -25.6% | 11.44 | 7.75 / 7.50-8.92 | 0.43 (3.8%) | 8.66-11.76 | +8.6% / +18.7% | +4.0% | 4.8M |
| ITUB | 7.34 (10:12 iex) | -24.1% | 9.67 | 7.47 / 7.24-7.79 | 0.29 (3.0%) | 7.92-10.20 | +2.9% / +13.8% | +2.4% | 41.5M |
| EWZ | 32.56 (10:12 iex) | -23.6% | 42.59 | 31.71 / 31.40-32.92 | 0.88 (2.1%) | 35.97-43.90 | +3.4% / +10.7% | +1.8% | 54.6M |
| AVBP | 16.11 (10:12 iex) | -23.3% | 21.00 | 18.34 / 15.56-18.46 | 2.41 (11.5%) | 11.36-30.90 | +0.4% / -19.7% | +26.1% | 2.3M |
