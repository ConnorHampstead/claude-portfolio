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

# Pre-market brief: Friday 2026-10-30

*Written 09:05 ET / 14:05 Stockholm. The cash session opens 09:30 ET (14:30 Stockholm). This is the last session of October, and every resting entry is cleared before the weekend, so today's stop entries only live today.*

### 1. Tape
The AI-capex unwind took a third leg overnight. Amazon is −7.4% pre-market at 225.74 (Alpaca). It missed on EPS and revenue, spent over $77B on capex in Q3, and trailing-twelve-month free cash flow was about −$42B. Intel is about −25% on a Q4 guide of roughly −20% quarter on quarter, plus a PC inventory correction it expects to run into 1H27. That dragged semis: SMH −5.2%, AMD −9.2%, NVDA −2.4%. QQQ is −2.5% and SPY −1.0%, but DIA is flat. Money is going into defensives and energy instead: XLP +2.4%, XLV +1.6%, XLE +1.5% (XOM and CVX beat this morning), TLT +0.4% with the 10-year at about 4.95%. WTI is around $104 and Brent around $113 on talk of US military action against Iran. The regime is rotation, not liquidation. **The edge is short tech and semis, long defensives and energy.**

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Q3 Employment Cost Index | **Out: +0.8% q/q vs +0.8% expected** (Q2 +0.9%). Smallest gain since Q2 2021. Wages +0.7%, benefits +0.9%. Neutral; no futures reaction worth noting | TLT, KRE |
| pre-mkt | – | XOM, CVX Q3 | **Out: both beat**; XOM +1.8%, CVX +1.5% pre-market | XLE resting entry |
| 09:45 | 14:45 | Chicago PMI | Consensus 54.8 (prior 58.8) | general |
| Mon 11-02 (thin source) | – | AAPL earnings | Benzinga gives Nov 2. Not verified with Apple; not trading AAPL because of it | – |
| Tue 11-03 | – | AMD earnings | Scheduled | Rules out AMD; SMH carries it as other-company risk |
| all day | – | Month-end rebalancing; Iran headlines | XLP had its best month since launch (+11.3%), so rebalancing could sell it | XLP play, XLE |

### 3. Open positions and resting entries
- **META short** (616.20, last 613.42; stop 643, target 580). **Intact.** The capex-without-cloud thesis is exactly what the tape is trading today, and the 609.00 20-day low is near. Hold on the existing levels.
- **TSLA long** (398.69, last 395.08; stop 395.00). **Invalidated in practice.** The relative-strength-at-range-top premise does not survive a −2.5% QQQ gap. The live stop will almost certainly fire at the open, and that is the exit; I am not widening it. No manage entry.
- **KRE long** (73.06, last 72.85; stop 71.25, target 76.20). **Intact.** Financials are bid in the rotation (XLF +0.6%, a new 20-day high pre-market), and the curve and NIM thesis is untouched by the tech selloff. Hold.
- **GOOGL short stop entry at 279.80** (stop 290.50, target 258.40). **Keep.** Pre-market is 280.28, so the trigger is still below the market (by 0.48). It continues the worst post-earnings break in 20+ years, and AMZN is confirming the theme. Together with META, communications shorts come to about 18% of equity, inside the sector cap.
- **XLE long stop entry at 70.00** (stop 67.90, target 73.20). **Keep.** Pre-market is 69.73, under the 69.86 20-day high. Oil above $100 plus the XOM/CVX beats is exactly the catalyst the breakout trigger was waiting for.

### 4. New plays

**SMH short: breakdown below the 20-day low**
| Field | Value |
|---|---|
| Ticker | SMH |
| Direction | Short |
| Catalyst | Intel's Q4 guide (about −20% q/q) and PC inventory correction into 1H27, released 2026-10-29 after the close; AMZN capex and FCF shock the same night |
| Thesis | Semis are the most crowded part of the AI-capex trade, and today brings a demand warning (INTC) on top of a payer under strain (AMZN). A break of the 520.53 20-day low turns a gap into a range breakdown, with the 50-day already lost. |
| Entry | 519.00, sell stop (pre-market 532.50, so the trigger is beyond the market) |
| Stop | 541.00. That is back above the 20-day-low shelf and about 1.2 ATR (ATR 18.44); a reclaim there means the breakdown failed. |
| Target | 486.00 (1.5R) |
| Risk tier | 0.5. It would be the second down day in a row of a −5% move, and there is short-squeeze risk into month-end. |
| Time horizon | 1–4 days (the entry only lives today) |
| Conviction | 3 |
| P(target before stop) | 0.34 |
| Invalidation | SMH holds 520 into the close and NVDA reclaims 213. |
| What I'd be wrong about | INTC is a PC story, not AI, so the market may separate the two. Semis were +7.3% in five days before today, so this could be just a pullback inside an uptrend. |

**XLP long: buying a pullback to the breakout level**
| Field | Value |
|---|---|
| Ticker | XLP |
| Direction | Long |
| Catalyst | Rotation out of tech on 2026-10-30 (PG, KO and WMT about +2% pre-market) |
| Thesis | Money leaving AI-capex names is going into staples. A pullback toward the 89.99 20-day high, which today's gap cleared, is a retest of the breakout, and it buys the theme cheaper than the +2.4% gap. |
| Entry | 89.90, limit (pre-market 90.29) |
| Stop | 88.00. That is below yesterday's 88.18 close; losing it fills the gap and kills the breakout. It is about 1.4 ATR. |
| Target | 93.50 (1.9R) |
| Risk tier | 0.5. Staples are up 11.3% in October, the best month since launch, so month-end rebalancing could sell them. |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 0.38 |
| Invalidation | XLP closes back under 89 while QQQ recovers. That would make this a one-day hedge flow, not a rotation. |
| What I'd be wrong about | It is extended after a record month, and a 2.4% gap in a staples ETF is often faded. The limit fills only if that fade starts. |

### 5. Both sides
- **Best short:** SMH, sell stop at 519 / stop 541 / target 486, P 0.34. Taken. The runner-up is AMZN after the earnings gap. It needs an opening range to place, so it goes to the review (section 7) and into `passed`.
- **Best long:** XLP, limit at 89.90 / stop 88.00 / target 93.50, P 0.38. Taken. The XLE resting breakout entry is the other long expression.

### 6. Passing on
- **AMZN short at market** (~225.7 / stop 236 / target 205, P 0.35): a −7.4% gap is already the move, and the opening range gives better location. Left to the review.
- **NVDA short** (sell stop 205 / stop 215 / target 188, P 0.30): it duplicates SMH, and NVDA shorts have been my weakest group (last one −0.76R).
- **LLY long** (~1413 / stop 1350 / target 1520, P 0.36): chasing +2.9% above the 20-day high, and XLV-type defensive exposure is already covered by XLP.
- **AMD short:** its own earnings on 11-03 are inside the horizon (rule 8). No levels.
- **AAPL:** likely earnings 11-02 (thin source). No position.

### 7. For the post-open review
- **AMZN:** if by 10:00 ET it cannot reclaim 230 and breaks the opening-range low, short with the stop above the opening-range high (about 236 at most) and target 210, at 0.5 risk. If it reclaims 232 and holds, pass.
- **TSLA:** confirm the stop filled. If it somehow held above 395 with QQQ recovering, leave it alone.
- **XLP:** if it opens below 89.90 and the gap fill runs toward 88.5, the limit may have filled close to the stop. Close it if it trades under 88.4 by 10:00.
- **Chicago PMI at 09:45:** a print well under 50 strengthens the defensive tilt; no action tied to it.

### 8. Book state
If everything fills: gross is about 88% of equity (cap 150%) and net is about +27% (cap ±100%). Risk at stake is about 2.54% (cap 4%), and roughly 2.5% once TSLA stops out. Slots: 7 of 8, then 6 after TSLA exits.

```json
{
  "date": "2026-10-30",
  "no_trade": false,
  "session_note": "AI-capex unwind leg three (AMZN -7%, INTC -25%, SMH -5%) with rotation into staples/health/energy; short semis on breakdown, buy staples pullback, keep GOOGL/XLE triggers.",
  "plays": [
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "stop",
      "entry": 519.00,
      "stop": 541.00,
      "targets": [486.00],
      "time_horizon": "1-4 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.34,
      "catalyst": "Intel Q4 guide ~-20% q/q and PC inventory correction into 1H27 (2026-10-29 AMC) plus AMZN capex/FCF shock.",
      "thesis": "Semis are the most crowded AI-capex expression; a break of the 520.53 20d low converts the gap into a range breakdown below the 50d.",
      "invalidation": "SMH holds 520 into the close and NVDA reclaims 213.",
      "bear_case": "INTC is a PC story, not AI; semis were +7% in 5 days so this may be a dip inside an uptrend, with month-end squeeze risk."
    },
    {
      "ticker": "XLP",
      "direction": "long",
      "entry_type": "limit",
      "entry": 89.90,
      "stop": 88.00,
      "targets": [93.50],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "Rotation out of tech on 2026-10-30; PG, KO, WMT ~+2% pre-market after AMZN/INTC misses.",
      "thesis": "Money leaving AI-capex names is going to staples; a pullback to the 89.99 breakout level is a retest that buys the rotation cheaper than the gap.",
      "invalidation": "XLP closes back below 89 while QQQ recovers.",
      "bear_case": "Record +11.3% October; month-end rebalancing and a fade of a 2.4% staples gap."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "AMZN",
      "direction": "short",
      "entry_type": "market",
      "entry": 225.74,
      "stop": 236.00,
      "targets": [205.00],
      "p_target_first": 0.35,
      "reason": "Post-earnings -7.4% gap is already the move; left to the post-open review for opening-range location."
    },
    {
      "ticker": "NVDA",
      "direction": "short",
      "entry_type": "stop",
      "entry": 205.00,
      "stop": 215.00,
      "targets": [188.00],
      "p_target_first": 0.30,
      "reason": "Duplicates the SMH short; NVDA shorts have been my weakest here."
    },
    {
      "ticker": "LLY",
      "direction": "long",
      "entry_type": "market",
      "entry": 1413.00,
      "stop": 1350.00,
      "targets": [1520.00],
      "p_target_first": 0.36,
      "reason": "Chasing +2.9% above the 20d high; defensive exposure already taken via XLP."
    }
  ]
}
```

Sources: [Yahoo Finance live, Oct 30](https://finance.yahoo.com/markets/live/stock-market-today-friday-october-30-dow-sp-500-nasdaq-083236552.html), [Yahoo: futures fall on AMZN, INTC](https://finance.yahoo.com/markets/stocks/articles/us-stock-futures-fall-amzn-100738749.html), [Yahoo: AMD falls on Intel outlook](https://finance.yahoo.com/markets/stocks/articles/amd-shares-fall-6-5-102611265.html), [GuruFocus: AMD/Intel](https://www.gurufocus.com/news/9158327/amd-stock-drops-amid-intels-weak-earnings-outlook), [investingLive: ECI](https://investinglive.com/news/us-employment-cost-index-for-q3-0-8-vs-0-8-expected/), [Investing.com: ECI and Chicago PMI due Friday](https://www.investing.com/news/stock-market-news/employment-cost-index-and-chicago-pmi-data-due-friday-93CH-4984851), [Benzinga: Walmart's best month since 1999, staples record](https://www.benzinga.com/etfs/sector-etfs/26/10/62546738/walmart-stock-best-month-since-1999-record-staples-rally), [CNBC live](https://www.cnbc.com/2026/10/29/stock-market-today-live-updates.html), [Benzinga: Apple Nov 2 earnings](https://www.benzinga.com/trading-ideas/movers/26/10/62557439/can-apple-top-nvidia-iphone-duo-and-nov-2-earnings-hold-the-key)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC, 15:05 Stockholm), Friday 2026-10-30. The cash session opened 35 min ago and closes at 16:00 ET (21:00 Stockholm).
- Equity: **$102,280.59**
- Cash: $69,934.02
- Session P&L so far: -0.44% (new entries are blocked at -3.0%)
- Gross exposure: $82,438 (81% of equity, cap 150%)
- Net exposure: $+20,409 (+20%, cap +/-100%)
- Risk at stake (entry to stop): $2,553 (2.50% of equity, cap 4.0%) — 1.50% left for new plays
- Slots: 5 open + 1 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| GOOGL | short | 48 | 279.61 | 281.08 | -71 (-0.5%) | 290.50 | 258.40 | A break of the 280.36 opening-range low on the gap day confirms the bounce failed and selling continues; post-earnings d |
| KRE | long | 142 | 73.06 | 72.46 | -85 (-0.8%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| META | short | 9 | 616.20 | 620.64 | -40 (-0.7%) | 643.00 | 580.00 | Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward  |
| XLE | long | 243 | 70.01 | 69.97 | -11 (-0.1%) | 67.90 | 73.20 | Energy equities are repricing $100+ oil; a break of the 69.86 20d high confirms the breakout while AI dominates headline |
| XLP | long | 270 | 89.90 | 89.38 | -140 (-0.6%) | 88.00 | 93.50 | Money leaving AI-capex names is going to staples; a pullback to the 89.99 breakout level is a retest that buys the rotat |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| SMH | short | 23 | 519.00 | stop | 541.00 | 486.00 | 2026-10-30 |

### Record

33 closed trades: 12W / 21L, total +2.34R, net $+2,638 realized. Shorts taken: 31.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| TSLA | long | stop | -0.52R | $-129 | 35% |
| MSFT | long | close | -0.80R | $-324 | 38% |
| XLV | long | target | +1.65R | $+837 | 40% |
| NVDA | short | close | -0.76R | $-190 | 35% |
| XOM | long | stop | -0.07R | $-37 | 37% |

### Ideas you passed on, replayed against the tape

74 resolved: 21 reached target first, 34 stop first, 13 never reached the entry, 6 expired, 0 ambiguous. Average +0.01R across the 61 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-30 pre-market | AMZN | short | Post-earnings -7.4% gap is already the move; left to the post-open review for op | stop | -0.34R | 35% |
| 2026-10-20 open | XLV | long | Healthcare leading, but chasing a +1.9% day through the 20d high; book already h | target | +2.26R | 35% |
| 2026-10-23 pre-market | LLY | long | Same defensive-rotation factor as the XLV long; extended +8.9% vs 20d average. | target | +1.70R | 35% |
| 2026-10-29 pre-market | LLY | long | Strong earnings breakout, but stacked on XLV it breaches the 40% health care sec | target | +1.85R | 40% |
| 2026-10-23 pre-market | META | short | Already through the prior target after -11.9% in 5d; chasing. AVGO is the cleane | never filled | - | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 281.01 (10:05 iex) | -1.0% | 283.82 | 280.98 / 279.00-281.99 | 10.78 (3.8%) | 280.36-359.40 | -15.8% / -16.6% | -12.5% | 31.1M |
| KRE | 72.45 (10:05 iex) | -0.6% | 72.86 | 73.02 / 72.37-73.17 | 1.29 (1.8%) | 67.79-73.45 | +3.3% / +1.4% | +0.6% | 14.7M |
| META | 620.10 (10:05 iex) | -0.7% | 624.52 | 614.10 / 610.13-621.19 | 26.29 (4.2%) | 609.00-771.27 | -10.4% / -6.6% | -3.7% | 22.6M |
| XLE | 69.97 (10:05 iex) | +1.8% | 68.71 | 69.52 / 69.28-70.14 | 1.42 (2.1%) | 61.86-69.86 | +2.9% / +6.3% | +1.7% | 31.3M |
| XLP | 89.38 (10:05 iex) | +1.4% | 88.18 | 89.95 / 89.33-90.38 | 1.39 (1.6%) | 80.10-89.99 | +3.1% / +4.6% | -2.0% | 14.1M |
| SMH | 531.82 (10:05 iex) | -5.3% | 561.67 | 532.78 / 529.34-535.32 | 18.44 (3.3%) | 520.53-639.47 | -2.4% / -2.0% | +7.3% | 8.8M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 760.33 (10:05 iex) | -1.2% | 769.36 | 761.38 / 759.44-761.46 | 7.11 (0.9%) | 758.68-781.62 | -0.2% / +0.3% | +0.7% | 37.8M |
| QQQ | 697.45 (10:05 iex) | -2.5% | 715.34 | 697.21 / 694.05-698.54 | 12.56 (1.8%) | 701.16-762.86 | -2.2% / -1.3% | +1.5% | 36.9M |
| IWM | 280.92 (10:05 iex) | -1.1% | 284.01 | 282.01 / 280.88-282.71 | 3.61 (1.3%) | 269.88-285.26 | +2.3% / -0.1% | +2.7% | 24.3M |
| DIA | 520.55 (10:04 iex) | -0.4% | 522.73 | 521.85 / 520.29-522.02 | 4.99 (1.0%) | 507.73-528.45 | +0.7% / +0.3% | -1.0% | 3.3M |
| TLT | 81.63 (10:05 iex) | +0.2% | 81.49 | 81.86 / 81.61-82.03 | 0.82 (1.0%) | 76.43-81.92 | +2.6% / +1.5% | -0.3% | 39.3M |
| GLD | 358.23 (10:05 iex) | -2.8% | 368.57 | 361.44 / 358.32-361.68 | 5.13 (1.4%) | 364.33-385.22 | -2.2% / -5.9% | -0.1% | 8.0M |
| USO | 170.60 (10:05 iex) | +1.4% | 168.19 | 169.75 / 169.66-170.83 | 4.86 (2.9%) | 141.76-169.96 | +7.4% / +12.6% | +3.5% | 4.7M |
| SMH | 531.82 (10:05 iex) | -5.3% | 561.67 | 532.78 / 529.34-535.32 | 18.44 (3.3%) | 520.53-639.47 | -2.4% / -2.0% | +7.3% | 8.8M |
| XLK | 181.77 (10:05 iex) | -3.7% | 188.74 | 182.11 / 180.85-182.29 | 4.24 (2.2%) | 181.50-203.25 | -1.6% / -0.5% | +3.5% | 8.7M |
| XLF | 56.65 (10:05 iex) | -0.5% | 56.94 | 57.19 / 56.53-57.20 | 0.72 (1.3%) | 53.21-57.23 | +3.2% / +1.9% | +0.5% | 32.3M |
| XLE | 69.97 (10:05 iex) | +1.8% | 68.71 | 69.52 / 69.28-70.14 | 1.42 (2.1%) | 61.86-69.86 | +2.9% / +6.3% | +1.7% | 31.3M |
| XLV | 186.69 (10:05 iex) | +1.4% | 184.04 | 186.75 / 186.41-187.99 | 3.15 (1.7%) | 165.19-184.85 | +5.3% / +7.2% | +1.5% | 8.8M |
| XLI | 169.15 (10:05 iex) | -0.6% | 170.13 | 169.07 / 168.84-170.19 | 2.58 (1.5%) | 162.97-172.34 | +1.1% / -0.4% | +2.0% | 7.4M |
| XLY | 115.27 (10:05 iex) | -0.8% | 116.20 | 114.89 / 114.47-115.62 | 1.67 (1.4%) | 109.50-116.77 | +2.6% / +2.7% | +1.0% | 7.1M |
| XLP | 89.38 (10:05 iex) | +1.4% | 88.18 | 89.95 / 89.33-90.38 | 1.39 (1.6%) | 80.10-89.99 | +3.1% / +4.6% | -2.0% | 14.1M |
| XLU | 43.46 (10:05 iex) | +0.7% | 43.14 | 43.44 / 43.35-43.65 | 0.62 (1.4%) | 39.58-43.25 | +3.3% / +3.6% | +0.6% | 29.9M |
| XLB | 52.31 (10:05 iex) | -0.4% | 52.53 | 52.45 / 52.29-52.75 | 0.67 (1.3%) | 48.51-52.53 | +4.0% / +3.2% | +1.6% | 10.6M |
| XLRE | 43.05 (10:04 iex) | -0.0% | 43.06 | 43.40 / 43.05-43.45 | 0.65 (1.5%) | 40.28-43.21 | +2.9% / +1.2% | +1.3% | 8.0M |
| XLC | 100.63 (10:05 iex) | -0.6% | 101.21 | 100.28 / 99.72-100.72 | 1.87 (1.8%) | 100.13-113.17 | -7.1% / -8.6% | -5.8% | 6.7M |
| KRE | 72.45 (10:05 iex) | -0.6% | 72.86 | 73.02 / 72.37-73.17 | 1.29 (1.8%) | 67.79-73.45 | +3.3% / +1.4% | +0.6% | 14.7M |
| XHB | 101.24 (10:05 iex) | -0.0% | 101.27 | 101.65 / 101.19-102.86 | 2.43 (2.4%) | 91.87-101.29 | +5.1% / +2.8% | +2.1% | 2.2M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.08 (10:05 iex) | -1.1% | 348.91 | 346.63 / 344.13-348.77 | 6.06 (1.7%) | 330.61-351.73 | +2.2% / +5.0% | +0.2% | 38.8M |
| MSFT | 523.12 (10:05 iex) | -1.3% | 530.14 | 526.36 / 514.35-526.36 | 11.16 (2.1%) | 513.66-551.15 | -0.1% / +3.5% | +1.7% | 21.2M |
| NVDA | 207.74 (10:05 iex) | -2.8% | 213.66 | 208.89 / 205.71-209.06 | 5.94 (2.8%) | 210.18-243.37 | -4.2% / -3.7% | +0.7% | 100.1M |
| AMZN | 238.12 (10:05 iex) | -2.3% | 243.79 | 232.54 / 229.36-240.18 | 7.00 (2.9%) | 241.24-265.34 | -4.4% / -4.3% | -2.6% | 38.2M |
| GOOGL | 281.01 (10:05 iex) | -1.0% | 283.82 | 280.98 / 279.00-281.99 | 10.78 (3.8%) | 280.36-359.40 | -15.8% / -16.6% | -12.5% | 31.1M |
| META | 620.10 (10:05 iex) | -0.7% | 624.52 | 614.10 / 610.13-621.19 | 26.29 (4.2%) | 609.00-771.27 | -10.4% / -6.6% | -3.7% | 22.6M |
| TSLA | 397.51 (10:05 iex) | -1.4% | 403.30 | 392.99 / 387.52-397.95 | 13.56 (3.4%) | 349.33-410.85 | +6.3% / +9.4% | +7.7% | 37.3M |
| AVGO | 329.17 (10:05 iex) | -4.6% | 345.00 | 330.71 / 326.75-331.98 | 11.66 (3.4%) | 320.23-380.84 | -0.6% / -2.3% | +6.7% | 21.7M |
| AMD | 516.11 (10:05 iex) | -8.9% | 566.42 | 509.00 / 507.38-520.40 | 28.43 (5.0%) | 502.60-658.52 | -1.8% / +3.4% | +11.5% | 19.6M |
| ORCL | 134.52 (10:05 iex) | -3.6% | 139.56 | 133.62 / 131.07-135.12 | 7.65 (5.5%) | 122.76-148.48 | +3.2% / -1.5% | +11.2% | 31.4M |
| NFLX | 62.67 (10:05 iex) | +1.0% | 62.05 | 62.73 / 61.68-62.98 | 2.10 (3.4%) | 61.39-73.07 | -8.5% / -15.0% | -7.5% | 44.1M |
| CRM | 234.17 (10:04 iex) | +1.4% | 230.90 | 231.85 / 228.90-234.40 | 9.66 (4.2%) | 220.29-252.42 | -2.8% / -3.1% | -7.7% | 7.1M |
| JPM | 338.03 (10:05 iex) | -1.6% | 343.58 | 345.29 / 337.00-345.29 | 6.49 (1.9%) | 325.07-345.75 | +2.7% / +0.3% | +2.1% | 6.9M |
| GS | 902.12 (10:05 iex) | -2.8% | 927.73 | 905.10 / 893.10-906.89 | 24.97 (2.7%) | 859.03-939.38 | +3.7% / -2.2% | +4.1% | 2.3M |
| BAC | 50.28 (10:05 iex) | -1.7% | 51.14 | 51.03 / 50.08-51.34 | 1.25 (2.5%) | 49.26-54.93 | -1.9% / -9.7% | +0.1% | 40.7M |
| XOM | 187.69 (10:05 iex) | +2.4% | 183.29 | 185.98 / 185.88-188.47 | 4.02 (2.2%) | 161.39-184.88 | +4.8% / +9.5% | +2.8% | 11.5M |
| CVX | 235.50 (10:05 iex) | +1.7% | 231.46 | 234.01 / 233.22-236.33 | 4.71 (2.0%) | 201.96-234.08 | +5.1% / +8.9% | +2.1% | 7.3M |
| LLY | 1,433.67 (10:05 iex) | +4.4% | 1,373.70 | 1,426.41 / 1,417.38-1,449.68 | 43.95 (3.2%) | 1,131.21-1,408.38 | +11.5% / +15.1% | +5.1% | 2.4M |
| UNH | 409.89 (10:05 iex) | -0.2% | 410.91 | 415.00 / 410.19-416.11 | 12.86 (3.1%) | 364.47-426.55 | +3.5% / +5.6% | -3.3% | 6.0M |
| JNJ | 278.35 (10:05 iex) | +1.1% | 275.20 | 280.00 / 277.86-282.01 | 7.39 (2.7%) | 245.17-278.05 | +5.9% / +3.7% | +2.8% | 7.8M |
| WMT | 123.34 (10:05 iex) | +1.7% | 121.25 | 123.14 / 122.75-123.97 | 2.54 (2.1%) | 103.39-122.40 | +5.4% / +10.4% | +0.1% | 19.6M |
| COST | 1,011.92 (10:05 iex) | +1.7% | 994.61 | 1,013.90 / 1,008.01-1,016.63 | 16.67 (1.7%) | 908.32-1,019.94 | +2.3% / +5.8% | -2.2% | 2.1M |
| HD | 329.04 (10:05 iex) | +0.0% | 328.98 | 333.35 / 328.68-334.80 | 7.51 (2.3%) | 279.76-329.01 | +8.0% / +6.8% | +0.4% | 4.8M |
| CAT | 635.76 (10:05 iex) | -1.8% | 647.39 | 627.32 / 621.85-637.25 | 30.88 (4.8%) | 631.01-874.87 | -14.1% / -17.6% | -7.8% | 3.0M |
| BA | 173.00 (10:05 iex) | +0.2% | 172.65 | 171.10 / 171.10-173.13 | 5.76 (3.3%) | 165.01-196.93 | -7.4% / -12.4% | -7.9% | 10.1M |
| DAL | 79.48 (10:05 iex) | -2.6% | 81.64 | 80.52 / 79.49-80.65 | 3.09 (3.8%) | 74.14-85.93 | +2.5% / +1.6% | +3.0% | 7.2M |
| UAL | 102.68 (10:05 iex) | -2.4% | 105.21 | 103.75 / 102.58-103.75 | 4.89 (4.7%) | 94.54-115.20 | +1.5% / -2.4% | +3.1% | 5.2M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-30 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AIOK | 28.64 (10:04 iex) | +51.6% | 18.89 | 20.72 / 20.51-28.66 | 4.35 (23.0%) | 3.90-29.90 | - / - | +344.5% | 7.2M |
| GDYN | 11.79 (10:05 iex) | +24.3% | 9.49 | 10.48 / 10.30-11.88 | 0.39 (4.1%) | 7.58-9.62 | +15.9% / +18.4% | +10.9% | 1.1M |
| CDNA | 88.60 (10:05 iex) | +23.9% | 71.52 | 80.61 / 80.44-90.87 | 4.17 (5.8%) | 61.19-73.43 | +6.6% / +21.0% | +3.4% | 1.3M |
| SOXS | 50.24 (10:05 iex) | +20.5% | 41.68 | 50.15 / 49.14-50.77 | 5.12 (12.3%) | 28.46-54.38 | +2.4% / -1.0% | -22.0% | 78.2M |
| SMST | 16.22 (10:04 iex) | +18.6% | 13.68 | 15.62 / 15.62-17.14 | 1.76 (12.9%) | 10.70-16.40 | +2.4% / -22.6% | +3.8% | 1.6M |
| FMC | 5.61 (10:05 iex) | +18.1% | 4.75 | 5.27 / 5.16-5.70 | 0.59 (12.5%) | 4.37-9.30 | -28.6% / -48.2% | -5.4% | 8.4M |
| AAOZ | 19.18 (10:02 iex) | +19.2% | 16.09 | 19.20 / 18.42-19.73 | 3.03 (18.8%) | 7.63-24.22 | +5.6% / +13.5% | -30.7% | 2.0M |
| DAMD | 11.31 (10:01 iex) | +17.0% | 9.67 | 11.64 / 11.25-11.68 | 1.05 (10.9%) | 7.63-12.43 | -1.9% / -18.7% | -21.0% | 3.1M |
| INTW | 7.52 (10:05 iex) | -57.6% | 17.74 | 8.58 / 6.96-8.72 | 2.02 (11.4%) | 15.04-34.28 | -16.0% / -22.9% | +15.5% | 4.6M |
| ATEC | 7.75 (10:05 iex) | -31.8% | 11.37 | 6.88 / 6.81-7.79 | 0.55 (4.8%) | 9.80-12.20 | +5.4% / +11.6% | +0.1% | 2.8M |
| INTC | 65.61 (10:05 iex) | -28.7% | 92.07 | 68.36 / 64.12-68.77 | 5.08 (5.5%) | 84.64-126.00 | -7.1% / -9.4% | +7.7% | 98.4M |
| RDDT | 99.16 (10:04 iex) | -23.5% | 129.60 | 100.25 / 95.00-101.98 | 8.23 (6.4%) | 126.37-164.94 | -13.4% / -14.5% | -13.7% | 4.9M |
| SOXL | 81.64 (10:05 iex) | -20.3% | 102.39 | 81.79 / 80.25-84.19 | 12.29 (12.0%) | 80.22-169.83 | -13.5% / -16.0% | +24.7% | 89.5M |
