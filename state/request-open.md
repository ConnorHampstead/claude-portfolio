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

# Pre-market brief — Wednesday 2026-10-14 (written 09:05 ET / 15:05 Stockholm)

## 1. Tape

September CPI came in hot. Headline was +0.6% m/m (in line) and 3.7% y/y against 3.6% expected; core was +0.3% m/m against 0.2% and 2.6% y/y against 2.5%. Gasoline is +34% y/y. *(verified, CNBC/Yahoo)* Futures were slightly green beforehand and turned red after the print. Per Alpaca, SPY is −0.3%, QQQ −0.7% and IWM −1.1%. Yahoo has the 10-year at about 5.30% and NY Fed's Williams saying one more hike may be appropriate this year. I could not reconcile that with another source quoting 5.22%; either way it is above 5%. Brent is about $105–108 after Houthi strikes on Aramco facilities, including an administrative complex hit on 10/13–14. Bank earnings are mixed: BAC missed with a $1.2B penalty and is −7.5% pre-market at 49.94, under its 20-day low of 52.24; BLK beat; MS is about flat.

This is a stagflation tape: oil up, yields up, rate-sensitive groups breaking (IWM, XHB and KRE are all at or below their 20-day lows), and energy leading. **The edge today is short, in rate-sensitive groups**, plus staying long energy.

## 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Sep CPI | **Out:** headline +0.6% m/m, 3.7% y/y (exp. 3.6%); core +0.3% m/m (exp. 0.2%), 2.6% y/y (exp. 2.5%). Futures turned lower, yields higher | XHB, KRE (proposed), SMH |
| Pre-mkt | — | BAC, MS, BLK earnings | **Out:** BAC miss, −7.5%; BLK beat, about +3–5%; MS about flat | KRE / financials |
| Pre-mkt | — | ASML Q3 | **Out:** slight sales miss, 2026 guidance raised; US listing about −1% | SMH |
| 10:30 | 16:30 | EIA crude inventories | consensus not verified | XOM |
| 14:00 | 20:00 | Fed Beige Book | — | all (rates) |
| Thu 08:30 | Thu 14:30 | Retail sales (exp. +0.3%), PPI, jobless claims, Philly Fed | consensus | all |

None of these is a binary event for its own name under rule 8.

## 3. Open positions

- **SMH short (587.00 entry, last 579.10): thesis intact.** Semis are −7% over 5 days and memory is still weak (MU and INTC lower). ASML's guidance raise is the counter-risk, but SMH is −1.5% pre-market anyway. I am lowering the stop from 603 to **595**. That sits above the 588–591 prior-close / invalidation zone and is about 1.2 ATR above last, which cuts risk. Target stays at 556. Hold.
- **XOM long (171.98 entry, last 175.22): thesis intact.** It is at a new 20-day high, oil is bid on the Aramco strikes, and a hot CPI driven by energy reinforces the leadership. I am raising the stop from 167.80 to **170.80**: about 1.4 ATR below last and under the breakout area, which leaves it near break-even. Target stays at 179. Hold.
- Resting entries: none.

## 4. New plays

### XHB short

| Field | Value |
|---|---|
| Ticker | XHB |
| Direction | Short |
| Catalyst | Hot core CPI on 2026-10-14 (0.3% vs 0.2%) with the 10-year above 5.2% and hike talk from Williams |
| Thesis | Homebuilders are the most direct equity read on mortgage rates. XHB is −6.5% vs its 50d, and pre-market at 93.03 it is below the 20-day low of 93.63. A hot core print pushing yields higher extends the downtrend. |
| Entry | Limit 93.80 (sell into an opening bounce back toward the broken 20d low) |
| Stop | 96.10: above the 94.63 prior close plus about 0.7 ATR, where reclaiming yesterday's close would mean the rate scare was rejected |
| Target | 89.50 (≈1.9R) |
| Risk tier | 0.5. This is shorting into a −1.7% gap, and Thursday's retail sales could squeeze it. |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 37% |
| Invalidation | 10-year back under 5.1%, or XHB closes back above 94.63 |
| What I'd be wrong about | XHB is already through the 20d low on a gap, and gaps in rate-sensitive ETFs after CPI often retrace intraday. If it never bounces to 93.80 I miss the move. |

The macro link here is the cleanest one today: core inflation is not cooling while oil drives the headline, and that is the worst mix for housing. Using a limit rather than a market order avoids shorting the low of the gap.

### KRE short (probe)

| Field | Value |
|---|---|
| Ticker | KRE |
| Direction | Short |
| Catalyst | BAC miss on 10-14, hot CPI and higher yields; KRE pre-market at 68.11, just above its 20d low of 67.97 |
| Thesis | Regional banks are −5.6% vs their 50d, and bank earnings are not rescuing the group. A break of the 20-day low opens room toward about 65. |
| Entry | Sell stop 67.60 (below the 20d low; pre-market 68.11 has not crossed it) |
| Stop | 69.60: back above the prior close of 69.06, about 1.6 ATR |
| Target | 64.60 (1.5R) |
| Risk tier | 0.25 (probe). Higher yields are ambiguous for bank margins, and regional-bank earnings are scattered through the coming days. |
| Time horizon | 1–4 days |
| Conviction | 2 |
| P(target before stop) | 34% |
| Invalidation | KRE holds 68 all session and closes green |
| What I'd be wrong about | A steeper curve helps net interest margin, and the BAC miss is a penalty plus trading shortfall, not a credit problem. |

## 5. Both sides

- **Best short:** XHB, taken in section 4 (limit 93.80, stop 96.10, target 89.50, P 37%).
- **Best long:** CVX breakout. Pre-market 219.55 is above its 20d high of 218.79. Levels would be a market entry around 219.5, stop 213.0, target 230, P 40%. **Passed** because it duplicates the XOM long, and the energy concentration is already the book's main long risk. COST near its 966 high is the non-energy alternative; passed as well (see section 6).

## 6. Passing on

- **BAC short** (market around 49.94, stop 52.30, target 47.00, P 33%): it is −7.5% on known news, so this would be shorting the gap at the bottom. The review can act on a failed bounce instead.
- **IWM short** (around 273.6, stop 277.5, target 268, P 36%): it is below the 20d low, but XHB and KRE express the same rate factor better. Left to the review.
- **CVX long** (219.5 / 213.0 / 230, P 40%): duplicates XOM.
- **COST long** (buy stop 968, stop 945, target 1000, P 38%): defensive breakout, but staples with a hot CPI and 5% yields are not a clear long.
- **BLK long:** beat and up 3–5%, but I could not verify a current price, so it is excluded.

## 7. For the post-open review

- **XOM:** if the opening range loses 172 (energy reversing after the CPI), close it.
- **IWM:** if it fails to reclaim 274.5 by 10:00 ET, short as a 0.25% probe: stop 277.5, target 268.
- **BAC:** if it bounces to 51.3–51.8 and fails in the first 30 minutes, short at 0.25%: stop 52.6, target 48.5. If it is already below 49.5, stand aside.
- **XHB:** if the open runs straight down without a bounce and trades below 92.0 by 10:00, cancel the 93.80 limit rather than chase.
- **SMH:** if it trades above 591 by 10:00 on ASML optimism, close it.

## 8. Book state

- **Exposure:** with XHB and KRE filled, gross is about 68% of equity and net is about −26%, inside the 150% and ±100% caps. Sector nets are energy about +21% and financials about −8%, all under 40%.
- **Risk:** the new SMH and XOM stops cut open-position risk from about $1.0k to about $0.4k. Adding XHB (0.5%) and KRE (0.25%) takes total risk at stake to about 1.2% of equity against the 4% cap, with 4 of 8 slots used.

```json
{
  "date": "2026-10-14",
  "no_trade": false,
  "session_note": "Hot core CPI (0.3% vs 0.2%), 10Y >5.2%, oil >$105 on Aramco strikes: stagflation tape; short rate-sensitives (XHB, KRE probe), stay long energy, tighten stops.",
  "plays": [
    {
      "ticker": "XHB",
      "direction": "short",
      "entry_type": "limit",
      "entry": 93.80,
      "stop": 96.10,
      "targets": [89.50],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.37,
      "catalyst": "Sep CPI 2026-10-14 core +0.3% m/m vs 0.2% exp; 10Y above 5.2%, Fed hike talk (Williams).",
      "thesis": "Homebuilders are the most direct equity read on mortgage rates; XHB is -6.5% vs 50d and gapping below its 20d low 93.63. Selling a bounce toward the broken low targets trend continuation.",
      "invalidation": "10Y back under 5.1% or XHB close above the 94.63 prior close.",
      "bear_case": "Post-CPI gaps in rate-sensitives often retrace; Thursday retail sales could squeeze; may never fill."
    },
    {
      "ticker": "KRE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 67.60,
      "stop": 69.60,
      "targets": [64.60],
      "time_horizon": "1-4 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.34,
      "catalyst": "BAC Q3 miss and $1.2B penalty 2026-10-14 plus hot CPI; KRE pre-market 68.11 just above 20d low 67.97.",
      "thesis": "Regional banks are -5.6% vs 50d and bank earnings are not rescuing the group; a break of the 20d low opens room toward 65.",
      "invalidation": "KRE holds 68 and closes green today.",
      "bear_case": "Steeper curve helps NIM; BAC miss was penalty and trading, not credit."
    }
  ],
  "manage": [
    {
      "ticker": "SMH",
      "action": "update",
      "stop": 595.00,
      "reason": "Thesis intact; lower stop to just above the 588-591 invalidation zone (~1.2 ATR above last) to cut risk."
    },
    {
      "ticker": "XOM",
      "action": "update",
      "stop": 170.80,
      "reason": "New 20d high with oil bid; raise stop to ~1.4 ATR below last, near break-even."
    }
  ],
  "passed": [
    {
      "ticker": "BAC",
      "direction": "short",
      "entry_type": "market",
      "entry": 49.94,
      "stop": 52.30,
      "targets": [47.00],
      "p_target_first": 0.33,
      "reason": "Already -7.5% on the earnings miss; shorting the gap low. Review may short a failed bounce."
    },
    {
      "ticker": "CVX",
      "direction": "long",
      "entry_type": "market",
      "entry": 219.55,
      "stop": 213.00,
      "targets": [230.00],
      "p_target_first": 0.40,
      "reason": "Best long (20d-high breakout) but duplicates the XOM energy exposure."
    },
    {
      "ticker": "IWM",
      "direction": "short",
      "entry_type": "market",
      "entry": 273.64,
      "stop": 277.50,
      "targets": [268.00],
      "p_target_first": 0.36,
      "reason": "Same rate factor as XHB/KRE; left to the review if it fails to reclaim 274.5."
    },
    {
      "ticker": "COST",
      "direction": "long",
      "entry_type": "stop",
      "entry": 968.00,
      "stop": 945.00,
      "targets": [1000.00],
      "p_target_first": 0.38,
      "reason": "Defensive breakout candidate, but staples with hot CPI and 5% yields are not a clean long."
    }
  ]
}
```

Sources: [CNBC CPI](https://www.cnbc.com/2026/10/14/cpi-inflation-report-september-2026.html), [Yahoo Finance live Oct 14](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-october-14-dow-sp-500-nasdaq-081136597.html), [CNBC BAC Q3](https://www.cnbc.com/2026/10/14/bank-of-america-bac-q3-2026-earnings.html), [CNBC premarket movers](https://www.cnbc.com/2026/10/14/stocks-moving-premarket-bank-of-america-blackrock-asml.html), [TradingKey premarket](https://www.tradingkey.com/analysis/stocks/us-stocks/262216186-us-premarket-cpi-bank-of-america-fall-blackrock-rise-tradingkey), [Fortune oil Oct 14](https://fortune.com/article/price-of-oil-10-14-2026/), [The National, Aramco strike](https://www.thenationalnews.com/business/energy/2026/10/14/houthi-attack-hits-aramcos-historic-nerve-centre-in-saudi-arabia/), [Investing.com Wednesday calendar](https://www.investing.com/news/stock-market-news/cpi-data-beige-book-and-oil-inventories-among-economic-data-due-wednesday-93CH-4947365), [TradingEconomics 10Y](https://tradingeconomics.com/united-states/government-bond-yield)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Wednesday 2026-10-14. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,037.85**
- Cash: $97,690.93
- Session P&L so far: +0.51% (new entries are blocked at -3.0%)
- Gross exposure: $39,051 (39% of equity, cap 150%)
- Net exposure: $+3,347 (+3%, cap +/-100%)
- Risk at stake (entry to stop): $391 (0.39% of equity, cap 4.0%) — 3.61% left for new plays
- Slots: 2 open + 0 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| SMH | short | 31 | 587.00 | 575.88 | +345 (+1.9%) | 595.00 | 556.00 | Semis are -6.8% over 5 days and below their 20d average while the memory complex is being repriced. A bounce toward the  |
| XOM | long | 121 | 171.98 | 175.20 | +390 (+1.9%) | 170.80 | 179.00 | Energy is the clear sector leader with XLE and XOM through 20-day highs. Geopolitical escalation risk keeps the oil prem |

### Record

17 closed trades: 5W / 12L, total -3.93R, net $+310 realized. Shorts taken: 15.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |
| NVDA | long | stop | -0.38R | $-235 | 40% |
| IWM | long | close | -1.16R | $-590 | 40% |
| JNJ | short | stop | -1.02R | $-550 | 38% |

### Ideas you passed on, replayed against the tape

32 resolved: 6 reached target first, 20 stop first, 5 never reached the entry, 1 expired, 0 ambiguous. Average -0.40R across the 27 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-13 open | UNH | short | The beat-and-raise gap fully reversed below yesterday's close, but I found no he | stop | -1.15R | 34% |
| 2026-10-07 pre-market | KRE | short | Bank earnings start 10/13, inside the horizon. | never filled | - | 33% |
| 2026-10-13 pre-market | AMD | short | Same chip factor as the SMH short; wider ATR and would be shorting into the gap. | stop | -1.17R | 35% |
| 2026-10-13 pre-market | JNJ | short | Down on patent-cliff worry despite raising guidance; shorting a guidance raise,  | target | +1.07R | 33% |
| 2026-10-13 pre-market | GS | long | Big revenue beat but -9.3% vs 50d; would be buying a gap against the trend, and  | stop | -0.91R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SMH | 575.62 (10:05 iex) | -2.1% | 588.12 | 576.46 / 574.42-580.08 | 13.45 (2.3%) | 540.45-639.47 | -2.3% / +1.4% | -7.0% | 6.3M |
| XOM | 175.19 (10:05 iex) | +0.6% | 174.08 | 175.06 / 174.53-175.55 | 3.24 (1.9%) | 155.85-174.89 | +6.1% / +7.4% | +5.8% | 13.0M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 773.09 (10:05 iex) | -0.6% | 778.01 | 774.93 / 773.16-776.35 | 5.96 (0.8%) | 747.74-781.62 | +1.1% / +1.4% | -0.1% | 42.7M |
| QQQ | 736.56 (10:05 iex) | -0.9% | 743.57 | 737.98 / 735.91-740.53 | 8.31 (1.1%) | 699.27-762.86 | +0.3% / +2.4% | -2.1% | 33.8M |
| IWM | 272.77 (10:05 iex) | -1.4% | 276.70 | 273.34 / 272.77-274.46 | 3.44 (1.2%) | 274.52-288.94 | -1.6% / -4.7% | -1.6% | 25.0M |
| DIA | 516.05 (10:05 iex) | -0.0% | 516.21 | 515.39 / 514.95-518.19 | 4.83 (0.9%) | 504.70-522.80 | +0.4% / -1.6% | +0.3% | 3.4M |
| TLT | 78.06 (10:03 iex) | -0.4% | 78.37 | 77.82 / 77.74-78.07 | 0.78 (1.0%) | 76.43-81.61 | -0.6% / -2.7% | +1.4% | 48.1M |
| GLD | 374.83 (10:05 iex) | -1.8% | 381.67 | 374.92 / 374.59-376.48 | 5.53 (1.4%) | 374.23-403.15 | -1.3% / -4.0% | -0.2% | 8.0M |
| USO | 153.97 (10:04 iex) | +0.6% | 153.09 | 154.09 / 153.68-154.33 | 5.24 (3.4%) | 141.76-159.36 | +2.9% / +9.2% | +5.6% | 5.5M |
| SMH | 575.62 (10:05 iex) | -2.1% | 588.12 | 576.46 / 574.42-580.08 | 13.45 (2.3%) | 540.45-639.47 | -2.3% / +1.4% | -7.0% | 6.3M |
| XLK | 193.61 (10:05 iex) | -1.4% | 196.28 | 193.86 / 193.33-194.66 | 2.74 (1.4%) | 182.21-203.25 | +0.3% / +3.5% | -2.8% | 7.3M |
| XLF | 54.09 (10:05 iex) | -1.3% | 54.82 | 54.22 / 54.07-54.41 | 0.65 (1.2%) | 52.81-56.65 | +0.5% / -2.6% | +1.5% | 38.7M |
| XLE | 67.19 (10:05 iex) | -0.0% | 67.20 | 67.60 / 67.13-67.72 | 1.25 (1.9%) | 60.95-67.25 | +6.0% / +7.1% | +5.4% | 33.7M |
| XLV | 172.86 (10:04 iex) | +1.9% | 169.66 | 170.94 / 170.65-173.08 | 2.66 (1.6%) | 165.19-172.79 | +0.4% / +0.5% | +1.5% | 8.1M |
| XLI | 167.43 (10:04 iex) | -0.7% | 168.67 | 167.80 / 167.37-168.67 | 2.40 (1.4%) | 166.18-172.34 | -0.3% / -3.6% | -1.7% | 7.2M |
| XLY | 111.03 (10:05 iex) | -1.2% | 112.36 | 111.89 / 111.03-112.03 | 1.22 (1.1%) | 107.99-113.29 | +1.4% / -1.5% | +0.6% | 6.4M |
| XLP | 84.69 (10:05 iex) | +0.6% | 84.19 | 84.88 / 84.61-85.18 | 1.01 (1.2%) | 80.10-85.12 | +2.4% / +0.7% | +2.9% | 10.5M |
| XLU | 41.42 (10:05 iex) | -1.1% | 41.87 | 41.80 / 41.38-41.88 | 0.63 (1.5%) | 39.03-41.95 | +3.5% / -0.1% | +1.7% | 33.9M |
| XLB | 49.27 (10:04 iex) | -0.9% | 49.72 | 49.43 / 49.27-49.73 | 0.72 (1.4%) | 47.81-50.88 | +0.3% / -2.7% | -0.0% | 11.4M |
| XLRE | 41.46 (10:05 iex) | -0.9% | 41.83 | 41.77 / 41.42-41.87 | 0.58 (1.4%) | 40.28-43.13 | +0.7% / -2.9% | +1.8% | 6.9M |
| XLC | 111.30 (10:05 iex) | -0.9% | 112.28 | 112.36 / 111.31-112.58 | 1.45 (1.3%) | 109.66-115.61 | +0.4% / +0.5% | +0.6% | 6.5M |
| KRE | 67.94 (10:04 iex) | -1.6% | 69.06 | 68.18 / 67.79-68.22 | 1.24 (1.8%) | 67.97-73.75 | -2.1% / -5.6% | -1.4% | 15.8M |
| XHB | 92.46 (10:03 iex) | -2.3% | 94.63 | 93.49 / 92.42-93.70 | 2.03 (2.1%) | 93.63-99.67 | -1.9% / -6.5% | -2.8% | 1.8M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.38 (10:05 iex) | +1.2% | 341.27 | 344.61 / 343.65-347.09 | 6.49 (1.9%) | 325.81-348.15 | +1.5% / +5.4% | +2.3% | 37.6M |
| MSFT | 541.08 (10:05 iex) | -0.4% | 543.45 | 545.29 / 541.29-545.75 | 11.95 (2.2%) | 487.23-551.15 | +5.7% / +8.1% | +2.7% | 22.5M |
| NVDA | 224.59 (10:05 iex) | -1.7% | 228.52 | 225.65 / 224.25-226.00 | 5.31 (2.3%) | 212.50-243.37 | +0.1% / +2.5% | -4.5% | 106.9M |
| AMZN | 257.38 (10:05 iex) | -0.5% | 258.58 | 258.01 / 257.11-259.65 | 5.37 (2.1%) | 244.30-263.70 | +2.3% / +0.1% | +0.9% | 36.2M |
| GOOGL | 354.40 (10:05 iex) | +0.2% | 353.78 | 355.80 / 354.51-359.38 | 7.62 (2.2%) | 335.51-364.17 | +2.1% / +2.3% | +1.8% | 25.7M |
| META | 749.52 (10:05 iex) | -1.7% | 762.50 | 760.00 / 747.38-761.50 | 23.11 (3.0%) | 660.28-779.82 | +4.8% / +17.9% | +3.2% | 22.2M |
| TSLA | 365.38 (10:05 iex) | -2.6% | 375.23 | 371.16 / 364.48-371.39 | 10.69 (2.8%) | 345.88-388.56 | +1.3% / +5.1% | -1.4% | 34.9M |
| AVGO | 350.45 (10:05 iex) | -1.9% | 357.31 | 352.11 / 347.69-354.25 | 10.35 (2.9%) | 335.20-380.84 | +0.2% / -3.4% | -4.9% | 22.9M |
| AMD | 587.68 (10:05 iex) | -2.9% | 605.53 | 589.57 / 581.52-591.88 | 23.77 (3.9%) | 506.05-658.52 | -0.4% / +13.5% | -6.8% | 21.7M |
| ORCL | 132.91 (10:05 iex) | -7.2% | 143.20 | 140.00 / 132.83-141.05 | 6.39 (4.5%) | 131.10-153.03 | +1.3% / -1.5% | -0.7% | 29.6M |
| NFLX | 70.12 (10:05 iex) | -0.5% | 70.46 | 70.77 / 70.09-71.26 | 1.45 (2.1%) | 66.54-77.80 | -0.5% / -6.4% | +2.6% | 37.4M |
| CRM | 236.50 (10:05 iex) | -0.6% | 238.01 | 238.40 / 236.65-240.11 | 7.96 (3.3%) | 220.29-255.95 | +1.9% / +4.9% | +5.8% | 10.2M |
| JPM | 331.36 (10:05 iex) | -0.0% | 331.43 | 327.17 / 326.40-333.04 | 5.53 (1.7%) | 324.25-353.83 | -1.5% / -4.7% | +0.0% | 8.5M |
| GS | 885.64 (10:04 iex) | -0.7% | 891.91 | 880.93 / 876.37-898.43 | 19.81 (2.2%) | 868.52-984.66 | -2.6% / -9.2% | -0.6% | 2.4M |
| BAC | 49.34 (10:05 iex) | -8.6% | 53.96 | 49.83 / 49.33-50.49 | 0.95 (1.8%) | 52.24-59.39 | -2.5% / -9.5% | -0.2% | 38.1M |
| XOM | 175.19 (10:05 iex) | +0.6% | 174.08 | 175.06 / 174.53-175.55 | 3.24 (1.9%) | 155.85-174.89 | +6.1% / +7.4% | +5.8% | 13.0M |
| CVX | 219.75 (10:05 iex) | +0.9% | 217.73 | 218.89 / 218.54-220.73 | 4.07 (1.9%) | 200.78-218.79 | +4.7% / +6.3% | +4.9% | 9.4M |
| LLY | 1,212.88 (10:05 iex) | +4.0% | 1,166.51 | 1,177.87 / 1,174.24-1,213.34 | 34.12 (2.9%) | 1,131.21-1,215.00 | +0.1% / -0.7% | +0.8% | 2.2M |
| UNH | 391.06 (10:05 iex) | +3.5% | 377.76 | 382.29 / 382.29-395.50 | 10.33 (2.7%) | 362.60-399.88 | +0.8% / -2.2% | +0.4% | 5.5M |
| JNJ | 251.27 (10:04 iex) | +1.1% | 248.61 | 249.09 / 248.50-251.56 | 6.03 (2.4%) | 245.17-275.23 | -5.7% / -6.2% | -2.4% | 7.5M |
| WMT | 114.26 (10:05 iex) | +1.8% | 112.28 | 113.84 / 113.38-114.59 | 2.30 (2.0%) | 103.39-114.83 | +3.9% / +3.5% | +4.7% | 21.8M |
| COST | 965.29 (10:03 iex) | +1.1% | 954.63 | 963.88 / 960.00-966.65 | 16.04 (1.7%) | 883.10-966.00 | +3.7% / +2.5% | +2.0% | 2.3M |
| HD | 290.31 (10:04 iex) | -1.2% | 293.92 | 292.50 / 290.31-293.74 | 6.04 (2.1%) | 277.15-310.40 | +0.6% / -6.6% | +2.5% | 5.6M |
| CAT | 761.86 (10:05 iex) | -1.4% | 772.78 | 761.60 / 761.01-770.35 | 27.37 (3.5%) | 755.31-876.95 | -5.0% / -5.8% | -10.5% | 2.5M |
| BA | 185.30 (10:05 iex) | -0.6% | 186.49 | 185.56 / 185.04-187.18 | 5.69 (3.1%) | 184.01-212.22 | -3.4% / -10.5% | -1.8% | 9.3M |
| DAL | 76.91 (10:05 iex) | -3.3% | 79.57 | 78.20 / 76.92-78.58 | 2.46 (3.1%) | 76.89-86.17 | -3.4% / -4.4% | -4.9% | 8.4M |
| UAL | 99.81 (10:04 iex) | -3.3% | 103.23 | 101.10 / 99.81-101.91 | 3.79 (3.7%) | 101.77-118.26 | -6.2% / -9.3% | -7.7% | 4.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-14 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BSP | 52.21 (10:05 iex) | +37.9% | 37.86 | 50.10 / 49.92-58.56 | 2.77 (7.3%) | 31.43-42.27 | +6.2% / -4.1% | +14.5% | 3.1M |
| LQDA | 34.90 (10:05 iex) | +30.2% | 26.81 | 35.63 / 34.37-38.64 | 6.56 (24.5%) | 22.31-74.74 | -44.6% / -58.0% | +3.5% | 5.4M |
| GRML | 7.18 (10:05 iex) | +29.6% | 5.54 | 7.50 / 6.71-7.53 | 1.82 (32.8%) | 2.82-18.21 | -32.9% / -27.4% | -13.2% | 25.2M |
| NBIZ | 30.55 (10:03 iex) | +20.5% | 25.35 | 28.29 / 27.40-30.55 | 2.72 (10.7%) | 17.01-27.56 | +15.4% / -11.4% | +41.0% | 2.3M |
| IREZ | 15.47 (10:05 iex) | +18.2% | 13.09 | 14.03 / 13.79-15.57 | 1.14 (8.7%) | 6.82-14.65 | +35.2% / +23.4% | +36.9% | 2.6M |
| VSTM | 8.76 (10:05 iex) | +17.6% | 7.45 | 8.00 / 6.70-8.77 | 0.52 (7.0%) | 7.20-8.64 | -5.7% / -0.1% | -3.9% | 2.6M |
| SMCZ | 5.43 (09:55 iex) | +12.0% | 4.85 | 5.15 / 5.15-5.44 | 0.46 (9.4%) | 3.66-6.58 | +6.7% / -21.9% | +18.6% | 3.0M |
| GDXD | 25.78 (10:05 iex) | +13.5% | 22.71 | 24.60 / 24.02-25.63 | 1.82 (8.0%) | 16.17-25.00 | +9.1% / +9.2% | +3.3% | 2.0M |
| CRWG | 9.95 (10:05 iex) | -30.3% | 14.28 | 12.07 / 9.77-12.26 | 1.86 (13.0%) | 13.61-20.68 | -18.4% / -27.5% | -28.8% | 2.4M |
| CWVX | 8.16 (10:03 iex) | -31.3% | 11.87 | 10.03 / 8.16-10.12 | 1.54 (13.0%) | 11.40-17.26 | -18.8% / -27.7% | -29.0% | 1.6M |
| SKYD | 6.93 (10:05 iex) | -1.9% | 7.07 | 7.60 / 6.81-7.98 | 0.45 (6.3%) | 6.60-8.76 | -5.7% / -7.8% | -2.7% | 34.5M |
| NBIG | 10.86 (10:03 iex) | -20.3% | 13.63 | 12.04 / 10.83-12.48 | 2.30 (16.8%) | 12.38-20.96 | -20.8% / -21.5% | -32.5% | 2.6M |
| NBIL | 15.93 (10:04 iex) | -19.6% | 19.82 | 17.50 / 15.75-18.20 | 3.32 (16.8%) | 18.02-30.43 | -20.6% / -21.3% | -32.3% | 4.1M |
| NEBX | 16.27 (10:05 iex) | -19.5% | 20.22 | 17.93 / 16.10-18.51 | 3.39 (16.7%) | 18.40-31.11 | -21.0% / -21.7% | -32.5% | 2.2M |
| IRE | 5.24 (10:05 iex) | -18.6% | 6.44 | 5.93 / 5.22-6.08 | 1.02 (15.8%) | 5.66-13.49 | -33.0% / -35.9% | -30.4% | 8.1M |
| IREX | 7.71 (10:05 iex) | -18.7% | 9.48 | 8.73 / 7.58-8.92 | 1.49 (15.7%) | 8.33-19.64 | -32.4% / -34.7% | -29.7% | 1.8M |
