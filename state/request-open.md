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

# Pre-market brief — Thursday 2026-10-22

*Written 09:05 ET / 15:05 Stockholm. The offset today is ET+6.*

### 1. Tape
Risk-off, and the AI-capex unwind is moving to the next leg. S&P futures are −1.0%, Nasdaq-100 −1.7% and Dow −0.7% (QQQ 713.2, SPY 766.3 on the Alpaca table). Last night's prints were sold even where they beat:
- **META** (−2.5% at 680, under its 20-day low of 681.05): it beat on revenue (+26%), but Q3 free cash flow was −$2.1B, its first negative quarter since 2012, and the company gave no 2027 capex outlook.
- **LRCX** (−7%): record quarter, but the December guide was wide around consensus.
- **TSLA** (−3.7%): cut its capex guidance.
- **IBM:** −5%.
- **AMD:** −4.4% at 528, sitting on its 20-day low of 524.6.

Oil is the second driver. Brent is about $111.9, its highest since May, after the IRGC claimed hits on seven vessels in and near Hormuz. Gold is −1.2% and TLT is +1.0% (yields lower). Defensives are bid: XLP +1.0%, XLV +0.6%, WMT/COST +1%. **The edge today is short**, specifically in AI-capex names. The book already holds four of those shorts, so the question today is risk management and diversification, not adding more of the same factor.

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Initial jobless claims | **194k actual vs 200k consensus.** A 3-month low. Futures did not respond; the tape is driven by earnings and oil. | HD (rates) |
| 10:00 | 16:00 | Conference Board LEI (Sep) | Minor | — |
| 10:30 | 16:30 | EIA natural gas storage | — | CVX/XOM, marginal |
| 11:00 | 17:00 | KC Fed manufacturing | Minor | — |
| AMC | 22:00+ | INTC, WDC, NEM, DECK earnings | INTC EPS est. ≈$0.39–0.40, revenue ≈$16.5B | NVDA/AMD shorts via semis read-across (gap risk tonight) |
| Ongoing | — | Hormuz / Saudi strike headlines | Brent $111.9 | CVX, XOM, airlines |

Rule 8 dates for current names: GOOGL reports Oct 28 AMC (exit by Oct 27). XOM and CVX are expected to report around Oct 30; I could not verify the exact date, so I treat Oct 29 as the exit deadline for both.

### 3. Open positions and resting entries
- **AMD short** (542.20 entry, last 528.40): **intact and working.** It is sitting on the 20-day low of 524.6, and the 512 target is 1.2% beyond it. A bounce off that floor is the main risk, so I'm cutting the stop from 558 to **545**, just under yesterday's 552.7 close and only 2.8 above entry. A full gap-fill means the move failed. Target stays at 512.
- **ORCL short** (129.70, last 126.05): **intact.** The AI-credit thesis is getting fresh evidence from META's negative FCF. Stop cut from 137.40 to **132.00**, above yesterday's 129.13 close and near entry. Target 116.5 stays.
- **GOOGL short** (332.42, last 328.83): **intact**, now under the 20-day low of 330.38. Stop cut from 341.50 to **337.00**, above the 334.76 close and the broken floor. Target 320 stays. A hard exit by the Oct 27 close is required (earnings Oct 28).
- **CVX long** (224.48, last 228.80): **intact.** Brent made a new 5-month high, and CVX is above its 20-day high of 228.48 pre-market. Stop raised from 218 to **223.00**, under Monday's 224 retest zone and about 1.2 ATR below last. Target 236 stays. Exit by Oct 29 for earnings.
- **HD long** (310.70, last 313.75): **intact but quiet.** Yields are falling, which is the thesis, but it is a risk-off tape. Hold on the existing 309 stop / 322 target. No change.
- **XOM resting buy stop 180.60** (pre-market 179.70, 20-day high 180.26): **keep.** The trigger is still above market and oil confirms. Energy notional if it fills is CVX ≈$17.8k + XOM ≈$17.5k ≈ 34% of equity, under the 40% sector cap.
- **NVDA resting sell stop 212.40** (pre-market 216.89, 20-day low 212.77): **keep.** It only fires on a break of the range floor, which today's tape makes more likely. If it fills, it adds a fifth AI-factor short, and I accept that because the stop-entry needs confirmation.

Cutting those four stops takes about $940 off risk at stake (~2.07% → ~1.15% before new plays).

### 4. New plays

**XLV long (probe-plus, 0.5)**

| Field | Value |
|---|---|
| Ticker | XLV |
| Direction | Long |
| Catalyst | 2026-10-22: risk-off rotation out of AI capex into defensives. XLV is +0.6% pre-market at 180.10, above its 20-day high of 180.06, with LLY +1.2%, UNH +0.9% and JNJ +1.3%. |
| Thesis | Money leaving AI capex is going to staples and health care, and XLV is breaking out of its 20-day range on that flow. It also diversifies a book made of four correlated AI shorts plus energy. |
| Entry | Limit 179.60, a modest pullback into the breakout and not chasing the open |
| Stop | 176.40. About 1.1 ATR (2.99) below entry and back inside the range; a failure there means the breakout failed. |
| Target | 184.80 (≈1.6R) |
| Risk tier | 0.5. ETF breakout with a clean structure, but a defensive rotation can reverse quickly if tech bounces. |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 40% |
| Invalidation | A tech-led reversal day in which XLV closes back under 178 |
| What I'd be wrong about | XLV is +4.4% over its 20-day average and +2.9% in 5 days, so it is extended. A one-day defensive bid on an oil scare often fades once the headlines cool. |

### 5. Both sides
- **Best long:** XLV, above (limit 179.60 / stop 176.40 / target 184.80, 40%). Runner-up: WMT at 119.25 toward its 20-day high of 121.38. Same factor as XLV, so it would be a second slot I don't have.
- **Best short:** META's post-earnings break under its 20-day low (681.05). Sell stop 674, stop 699 (above the gap-fill toward 697.5), target 640, P = 33%. **Passed.**
  - It would be a fifth AI-capex short in the book, and the last slot goes to diversification.
  - Day-one mega-cap earnings gaps often bounce: GOOGL/AMZN dip-buyers showed up at the open yesterday, and NFLX's gap failed on Oct 21.
  - Logged in `passed`.

### 6. Passing on
- **META short** (674 / 699 / 640): factor concentration, last slot. See above.
- **AVGO short** under its 328.58 20-day low (pre-market 326.6): same factor again. Sell stop 324, stop 338, target 305, P 35%.
- **LRCX:** −7% earnings gap. Not in the verified data table, so no levels.
- **Airlines (DAL/UAL) short** on oil: both sit just above their 20-day lows with an ATR around 4%. Gap-down chase; last week's DAL pass stopped out.
- **TSLA short:** −3.7% gap into the middle of its range (345.9–388.8). No structure.

### 7. For the post-open review
- **AMD:** if it trades under 524.6 (20-day low) by 10:00 and holds, leave it alone, since the target is 512. If it reclaims 540 by 10:00, consider closing it rather than waiting for the 545 stop.
- **XLV:** if the open is above 181 and the 179.60 limit looks unlikely to fill, the review may raise the limit to 180.30 (stop 176.40 unchanged). If XLV opens red under 179, leave the limit.
- **Slot use:** if XLV is clearly not going to fill and META is under 675 at 10:00 without reclaiming 686, the review may cancel XLV and take the META short (stop 699, target 640, 0.25 tier).
- **CVX:** if Brent reverses below $107 on a de-escalation headline, close CVX and cancel the XOM entry.

### 8. Book state
- **Exposure:** if XLV fills (~0.5% risk, ≈$16k notional), gross is about $91k (≈88%), well under 150%. Net is about +$33k (≈+32%), within ±100%.
- **Risk:** at stake is about 1.15% + 0.5% ≈ **1.65%** of the 4% cap. 8 of 8 slots used, counting the XOM and NVDA resting entries.

```json
{
  "date": "2026-10-22",
  "no_trade": false,
  "session_note": "Risk-off: META/LRCX/TSLA earnings reignite AI-capex fears, Brent $112 on Hormuz attacks. Book already holds the AI-short factor; tightening its stops and using the last slot for a defensive XLV long.",
  "plays": [
    {
      "ticker": "XLV",
      "direction": "long",
      "entry_type": "limit",
      "entry": 179.60,
      "stop": 176.40,
      "targets": [184.80],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.40,
      "catalyst": "2026-10-22 rotation out of AI capex into defensives after META/LRCX/TSLA earnings; XLV +0.6% pre-market above 20d high 180.06.",
      "thesis": "Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diversifies a book built around correlated AI shorts.",
      "invalidation": "Tech-led reversal with XLV closing back under 178.",
      "bear_case": "XLV is extended (+4.4% vs 20d average, +2.9% in 5 days); oil-scare defensive bids often fade quickly."
    }
  ],
  "manage": [
    {"ticker": "AMD", "action": "update", "stop": 545.00, "reason": "Short working into the 20d low at 524.6; stop cut to just above entry, below yesterday's close; a gap-fill means the move failed."},
    {"ticker": "ORCL", "action": "update", "stop": 132.00, "reason": "META negative FCF supports the AI-credit thesis; stop cut to above yesterday's 129.13 close to protect the trade."},
    {"ticker": "GOOGL", "action": "update", "stop": 337.00, "reason": "Under the 20d low; stop cut to above the 334.76 close and the broken floor. Exit by Oct 27 before earnings."},
    {"ticker": "CVX", "action": "update", "stop": 223.00, "reason": "Brent at a 5-month high, CVX above its 20d high; stop raised under Monday's 224 retest to cut risk."}
  ],
  "passed": [
    {
      "ticker": "META",
      "direction": "short",
      "entry_type": "stop",
      "entry": 674.00,
      "stop": 699.00,
      "targets": [640.00],
      "p_target_first": 0.33,
      "reason": "Post-earnings break under the 20d low, but it would be a fifth AI-capex short and the last slot went to diversification; day-one gaps often bounce."
    },
    {
      "ticker": "AVGO",
      "direction": "short",
      "entry_type": "stop",
      "entry": 324.00,
      "stop": 338.00,
      "targets": [305.00],
      "p_target_first": 0.35,
      "reason": "Same AI factor as the existing shorts; no slot."
    }
  ]
}
```

Sources: [Bloomberg futures](https://www.bloomberg.com/news/articles/2026-10-22/us-futures-slip-as-risk-off-sentiment-dominates-with-oil-rising), [TradingKey pre-market](https://www.tradingkey.com/analysis/stocks/us-stocks/262232340-us-premarket-ai-stocks-pressure-tsla-ibm-drop-wdc-earnings-tradingkey), [Bloomberg claims](https://www.bloomberg.com/news/articles/2026-10-22/us-initial-jobless-claims-fall-to-three-month-low), [Investing.com META](https://www.investing.com/news/stock-market-news/meta-stock-drops-premarket-after-earnings-buy-the-dip-or-stay-put-93CH-4965991), [Invezz META](https://invezz.com/news/2026/10/22/why-are-meta-shares-slipping-in-premarket-trading-despite-third-quarter-beat/), [24/7 Wall St LRCX](https://247wallst.com/investing/2026/10/22/lam-research-just-posted-its-first-ever-40-operating-margin-but-sold-off/), [CNBC TSLA](https://www.cnbc.com/2026/10/21/tesla-tsla-q3-2026-earnings-report.html), [Trading Economics Brent](https://tradingeconomics.com/commodity/brent-crude-oil), [News Chronicle Hormuz](https://thenews-chronicle.com/oil-tops-111-as-iran-claims-seven-vessels-hit-near-strait-of-hormuz/), [MarketBeat INTC](https://www.marketbeat.com/instant-alerts/upcoming-intel-intc-expected-to-announce-earnings-on-thursday-2026-10-22/), [Kiplinger calendar](https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar), [Investrade weekly calendar](https://investrade.com/weekly-event-calendar-10-19-2026-10-23-2026/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC, 16:05 Stockholm), Thursday 2026-10-22. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,911.96**
- Cash: $69,154.67
- Session P&L so far: +1.09% (new entries are blocked at -3.0%)
- Gross exposure: $103,558 (101% of equity, cap 150%)
- Net exposure: $+45,752 (+44%, cap +/-100%)
- Risk at stake (entry to stop): $1,690 (1.64% of equity, cap 4.0%) — 2.36% left for new plays
- Slots: 6 open + 2 resting entries of 8 — you may add at most 0 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 49% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 49% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMD | short | 19 | 542.20 | 525.60 | +315 (+3.1%) | 545.00 | 512.00 | Relief gap on upgrades without any change to the AI-credit story, now confirmed by the open rather than predicted. Overh |
| CVX | long | 78 | 224.48 | 225.33 | +66 (+0.4%) | 223.00 | 236.00 | Energy leads the rotation away from AI capex and the oil tape still points up. A retest of the breakout and Monday's 224 |
| GOOGL | short | 28 | 332.42 | 328.13 | +120 (+1.3%) | 337.00 | 320.00 | Relative weakness breaking the floor of the 20-day range on a tech-bid day; failed floor opens ~4% to 320. |
| HD | long | 33 | 310.70 | 321.22 | +347 (+3.4%) | 309.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 127.48 | +73 (+1.7%) | 132.00 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |
| XLV | long | 160 | 179.57 | 181.00 | +230 (+0.8%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XOM | long | 97 | 180.60 | stop | 175.40 | 189.00 | 2026-10-21 |
| NVDA | short | 26 | 212.40 | stop | 222.00 | 198.00 | 2026-10-20 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 23.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |

### Ideas you passed on, replayed against the tape

50 resolved: 12 reached target first, 28 stop first, 8 never reached the entry, 2 expired, 0 ambiguous. Average -0.26R across the 42 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-15 pre-market | AMD | short | Right direction but -11.6% in 5 days on a capitulation-style morning; same facto | target | +1.50R | 33% |
| 2026-10-14 pre-market | IWM | short | Same rate factor as XHB/KRE; left to the review if it fails to reclaim 274.5. | stop | -1.08R | 36% |
| 2026-10-19 open | NVDA | short | Gap already faded to near the 212.85 20-day low; little room to the floor. | stop | -0.95R | 35% |
| 2026-10-14 open | KRE | short | Morning play rejected by broker: not shortable. | never filled | - | 34% |
| 2026-10-07 pre-market | XHB | short | Same housing/rates factor as the HD short; one is enough. | expired | -0.52R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AMD | 525.45 (10:05 iex) | -4.9% | 552.72 | 523.11 / 519.80-529.64 | 27.67 (5.0%) | 524.60-658.52 | -7.7% / +2.1% | -3.2% | 19.5M |
| CVX | 225.31 (10:05 iex) | -0.6% | 226.78 | 228.86 / 225.38-229.04 | 4.62 (2.0%) | 201.96-228.48 | +6.5% / +8.5% | +2.1% | 7.5M |
| GOOGL | 327.98 (10:05 iex) | -2.0% | 334.76 | 330.45 / 327.03-331.43 | 8.11 (2.4%) | 330.38-359.40 | -3.0% / -2.6% | -3.7% | 23.9M |
| HD | 321.10 (10:05 iex) | +2.2% | 314.14 | 313.86 / 313.56-321.36 | 6.61 (2.1%) | 277.15-317.71 | +6.7% / +1.3% | +6.3% | 5.5M |
| ORCL | 127.54 (10:05 iex) | -1.2% | 129.13 | 126.35 / 125.17-127.92 | 6.69 (5.2%) | 127.36-146.40 | -5.4% / -10.1% | -1.1% | 30.6M |
| XLV | 181.03 (10:05 iex) | +1.2% | 178.94 | 179.66 / 178.95-180.94 | 2.99 (1.7%) | 165.19-180.06 | +4.4% / +5.1% | +2.9% | 8.5M |
| XOM | 176.71 (10:04 iex) | -0.8% | 178.09 | 179.89 / 176.68-180.31 | 3.58 (2.0%) | 159.27-180.26 | +5.4% / +8.0% | +0.6% | 11.4M |
| NVDA | 216.62 (10:05 iex) | -2.4% | 221.97 | 217.22 / 215.68-218.88 | 5.89 (2.7%) | 212.77-243.37 | -2.2% / -0.4% | +0.3% | 104.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 767.22 (10:05 iex) | -0.8% | 773.09 | 766.37 / 765.43-767.66 | 7.07 (0.9%) | 758.79-781.62 | +0.3% / +0.7% | +0.5% | 40.4M |
| QQQ | 714.28 (10:05 iex) | -1.5% | 725.20 | 713.61 / 711.81-715.27 | 11.27 (1.6%) | 707.23-762.86 | -1.9% / -0.2% | -0.5% | 35.2M |
| IWM | 276.63 (10:05 iex) | +0.1% | 276.48 | 274.81 / 274.76-277.27 | 3.88 (1.4%) | 269.88-284.64 | -0.5% / -3.7% | +1.9% | 25.8M |
| DIA | 526.93 (10:04 iex) | -0.1% | 527.70 | 525.36 / 524.81-527.34 | 5.17 (1.0%) | 504.59-527.79 | +2.4% / +1.0% | +2.4% | 3.3M |
| TLT | 81.15 (10:05 iex) | +1.1% | 80.24 | 81.00 / 80.87-81.24 | 0.80 (1.0%) | 76.43-80.56 | +2.2% / -0.0% | +1.7% | 49.8M |
| GLD | 371.24 (10:05 iex) | -2.0% | 378.95 | 373.54 / 371.18-373.87 | 4.93 (1.3%) | 373.36-394.22 | -0.7% / -4.3% | +0.8% | 7.7M |
| USO | 161.95 (10:03 iex) | +1.3% | 159.80 | 163.30 / 161.77-163.55 | 4.67 (2.9%) | 141.76-162.99 | +5.7% / +10.3% | +4.1% | 5.4M |
| SMH | 538.67 (10:05 iex) | -3.2% | 556.70 | 536.85 / 535.18-540.73 | 16.81 (3.0%) | 536.23-639.47 | -6.2% / -3.6% | -1.4% | 7.7M |
| XLK | 185.16 (10:05 iex) | -1.8% | 188.54 | 184.93 / 184.46-185.48 | 3.79 (2.0%) | 182.81-203.25 | -3.1% / -0.7% | -1.0% | 8.5M |
| XLF | 56.49 (10:05 iex) | +0.8% | 56.04 | 55.83 / 55.81-56.49 | 0.68 (1.2%) | 52.81-56.15 | +2.8% / -0.0% | +2.8% | 36.2M |
| XLE | 67.27 (10:05 iex) | -1.3% | 68.16 | 68.74 / 67.25-68.78 | 1.34 (2.0%) | 60.95-68.64 | +5.2% / +6.8% | +0.8% | 31.9M |
| XLV | 181.03 (10:05 iex) | +1.2% | 178.94 | 179.66 / 178.95-180.94 | 2.99 (1.7%) | 165.19-180.06 | +4.4% / +5.1% | +2.9% | 8.5M |
| XLI | 166.33 (10:05 iex) | -1.2% | 168.31 | 166.90 / 165.61-167.36 | 2.52 (1.5%) | 164.66-172.34 | -0.2% / -2.6% | +0.8% | 7.4M |
| XLY | 115.44 (10:05 iex) | -0.1% | 115.53 | 114.29 / 114.17-115.51 | 1.52 (1.3%) | 107.99-116.22 | +3.5% / +1.8% | +3.6% | 7.0M |
| XLP | 88.36 (10:05 iex) | +1.4% | 87.11 | 87.99 / 87.86-88.46 | 1.14 (1.3%) | 80.10-88.47 | +4.2% / +3.8% | +1.2% | 12.8M |
| XLU | 42.31 (10:05 iex) | +0.7% | 42.00 | 42.11 / 42.01-42.30 | 0.67 (1.6%) | 39.03-42.29 | +3.0% / +0.6% | +0.7% | 36.5M |
| XLB | 51.10 (10:05 iex) | -0.4% | 51.32 | 51.03 / 50.76-51.17 | 0.69 (1.3%) | 47.81-51.51 | +3.2% / +0.8% | +3.3% | 11.6M |
| XLRE | 42.13 (10:05 iex) | +0.2% | 42.06 | 42.03 / 41.98-42.25 | 0.63 (1.5%) | 40.28-42.61 | +1.5% / -1.6% | +1.4% | 7.6M |
| XLC | 107.82 (10:05 iex) | -1.1% | 108.97 | 107.95 / 107.29-108.11 | 1.59 (1.5%) | 108.61-114.08 | -2.0% / -2.4% | -1.7% | 6.5M |
| KRE | 71.77 (10:05 iex) | +1.6% | 70.62 | 70.34 / 70.19-71.92 | 1.24 (1.7%) | 67.79-71.93 | +1.0% / -2.4% | +3.0% | 16.0M |
| XHB | 97.38 (10:00 iex) | +1.9% | 95.60 | 94.86 / 94.86-97.38 | 2.21 (2.3%) | 91.87-99.13 | -0.2% / -3.9% | +3.0% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.83 (10:05 iex) | +0.5% | 343.99 | 344.88 / 344.60-347.28 | 5.95 (1.7%) | 325.81-348.15 | +1.8% / +5.0% | +0.3% | 37.1M |
| MSFT | 526.26 (10:05 iex) | -1.3% | 532.95 | 533.68 / 525.13-533.68 | 11.12 (2.1%) | 491.22-551.15 | +1.5% / +5.1% | -0.1% | 21.3M |
| NVDA | 216.62 (10:05 iex) | -2.4% | 221.97 | 217.22 / 215.68-218.88 | 5.89 (2.7%) | 212.77-243.37 | -2.2% / -0.4% | +0.3% | 104.5M |
| AMZN | 253.77 (10:05 iex) | -3.3% | 262.37 | 258.27 / 251.86-258.41 | 6.47 (2.5%) | 244.72-265.34 | +3.1% / +2.4% | +3.3% | 35.5M |
| GOOGL | 327.98 (10:05 iex) | -2.0% | 334.76 | 330.45 / 327.03-331.43 | 8.11 (2.4%) | 330.38-359.40 | -3.0% / -2.6% | -3.7% | 23.9M |
| META | 656.67 (10:05 iex) | -5.9% | 697.52 | 676.35 / 648.26-681.07 | 22.56 (3.2%) | 681.05-779.82 | -4.4% / +5.5% | -5.4% | 19.6M |
| TSLA | 387.44 (10:05 iex) | +0.3% | 386.47 | 374.29 / 373.71-388.84 | 12.41 (3.2%) | 345.88-388.84 | +4.4% / +6.7% | +5.3% | 35.8M |
| AVGO | 329.97 (10:05 iex) | -2.3% | 337.80 | 326.60 / 326.18-330.75 | 11.66 (3.5%) | 328.58-380.84 | -3.9% / -6.2% | -2.4% | 21.4M |
| AMD | 525.45 (10:05 iex) | -4.9% | 552.72 | 523.11 / 519.80-529.64 | 27.67 (5.0%) | 524.60-658.52 | -7.7% / +2.1% | -3.2% | 19.5M |
| ORCL | 127.54 (10:05 iex) | -1.2% | 129.13 | 126.35 / 125.17-127.92 | 6.69 (5.2%) | 127.36-146.40 | -5.4% / -10.1% | -1.1% | 30.6M |
| NFLX | 65.99 (10:05 iex) | +1.5% | 65.04 | 65.02 / 65.02-67.24 | 1.92 (3.0%) | 64.10-73.07 | -6.6% / -12.9% | -7.8% | 40.1M |
| CRM | 245.25 (10:05 iex) | +1.4% | 241.78 | 244.60 / 242.70-248.60 | 8.34 (3.4%) | 220.29-251.94 | +3.2% / +3.9% | +2.5% | 8.2M |
| JPM | 336.03 (10:05 iex) | +0.3% | 335.19 | 332.28 / 332.26-336.22 | 6.19 (1.8%) | 324.25-344.40 | +0.4% / -2.9% | -0.0% | 7.9M |
| GS | 902.64 (10:05 iex) | -0.2% | 904.72 | 884.92 / 883.89-905.92 | 23.64 (2.6%) | 859.03-935.83 | +0.8% / -6.2% | +3.0% | 2.3M |
| BAC | 51.20 (10:05 iex) | +0.8% | 50.78 | 50.44 / 50.20-51.19 | 1.27 (2.5%) | 49.26-56.74 | -5.0% / -12.7% | -1.2% | 42.9M |
| XOM | 176.71 (10:04 iex) | -0.8% | 178.09 | 179.89 / 176.68-180.31 | 3.58 (2.0%) | 159.27-180.26 | +5.4% / +8.0% | +0.6% | 11.4M |
| CVX | 225.31 (10:05 iex) | -0.6% | 226.78 | 228.86 / 225.38-229.04 | 4.62 (2.0%) | 201.96-228.48 | +6.5% / +8.5% | +2.1% | 7.5M |
| LLY | 1,303.83 (10:05 iex) | +2.6% | 1,270.75 | 1,281.76 / 1,275.10-1,304.52 | 38.03 (3.0%) | 1,131.21-1,311.75 | +6.4% / +7.4% | +5.1% | 2.3M |
| UNH | 421.96 (10:04 iex) | +1.2% | 417.00 | 418.38 / 417.13-422.45 | 13.15 (3.2%) | 362.60-422.40 | +8.4% / +7.8% | +5.4% | 6.0M |
| JNJ | 262.50 (10:05 iex) | +1.8% | 257.78 | 260.54 / 259.04-263.13 | 6.38 (2.5%) | 245.17-275.23 | -0.7% / -2.6% | +1.5% | 7.7M |
| WMT | 118.15 (10:05 iex) | +0.3% | 117.80 | 119.36 / 117.84-119.44 | 2.38 (2.0%) | 103.39-121.38 | +6.2% / +7.9% | +1.4% | 21.2M |
| COST | 1,004.02 (10:05 iex) | +0.6% | 998.31 | 1,008.55 / 1,001.23-1,008.59 | 15.17 (1.5%) | 883.10-1,008.37 | +5.3% / +6.6% | +1.7% | 2.3M |
| HD | 321.10 (10:05 iex) | +2.2% | 314.14 | 313.86 / 313.56-321.36 | 6.61 (2.1%) | 277.15-317.71 | +6.7% / +1.3% | +6.3% | 5.5M |
| CAT | 714.72 (10:04 iex) | -3.4% | 740.21 | 721.37 / 709.55-722.40 | 29.86 (4.0%) | 704.01-876.95 | -6.6% / -8.2% | -1.2% | 2.6M |
| BA | 190.81 (10:05 iex) | -0.8% | 192.28 | 191.49 / 190.45-193.19 | 3.99 (2.1%) | 183.38-201.40 | +1.2% / -5.2% | +4.1% | 8.2M |
| DAL | 79.16 (10:05 iex) | +1.9% | 77.67 | 75.63 / 75.38-79.17 | 2.88 (3.7%) | 74.14-85.93 | -4.0% / -4.4% | +1.6% | 7.4M |
| UAL | 102.79 (10:05 iex) | +1.1% | 101.67 | 98.00 / 98.00-102.87 | 4.59 (4.5%) | 94.54-115.71 | -4.6% / -7.7% | +2.7% | 4.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-22 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SAIQ | 8.01 (10:05 iex) | +44.1% | 5.56 | 6.52 / 6.41-8.24 | 1.86 (33.5%) | 1.76-12.95 | -2.6% / -35.6% | +43.3% | 8.2M |
| BHVN | 15.46 (10:05 iex) | +31.6% | 11.75 | 16.10 / 15.06-16.54 | 0.70 (5.9%) | 10.70-13.63 | -3.8% / -13.0% | +7.5% | 1.9M |
| MLTX | 12.79 (10:05 iex) | +20.1% | 10.65 | 10.70 / 10.65-13.31 | 0.57 (5.4%) | 9.46-12.83 | -2.3% / -19.0% | +5.0% | 1.8M |
| IREZ | 21.08 (10:04 iex) | +13.4% | 18.59 | 20.41 / 20.14-21.43 | 2.24 (12.0%) | 7.42-21.90 | +44.8% / +65.9% | +14.3% | 2.3M |
| GDXD | 25.70 (09:53 iex) | +12.9% | 22.76 | 25.00 / 25.00-25.84 | 2.15 (9.4%) | 18.83-26.56 | +2.1% / +13.9% | -11.7% | 1.6M |
| AAOZ | 20.85 (10:01 iex) | +11.9% | 18.63 | 21.18 / 20.85-21.86 | 2.30 (12.3%) | 7.63-20.73 | +37.4% / +42.9% | +19.5% | 1.8M |
| SOXS | 49.23 (10:05 iex) | +11.2% | 44.29 | 49.82 / 48.66-50.38 | 3.82 (8.6%) | 28.46-50.12 | +20.6% / +6.7% | +4.2% | 77.9M |
| AVTX | 7.75 (10:05 iex) | -36.8% | 12.26 | 8.99 / 6.85-9.35 | 0.86 (7.0%) | 11.21-16.10 | -10.0% / -25.9% | +3.5% | 1.2M |
| TTMI | 78.98 (10:05 iex) | -22.7% | 102.15 | 83.68 / 77.60-84.09 | 9.12 (8.9%) | 92.15-137.88 | -12.6% / -14.7% | -1.1% | 3.0M |
| FPS | 25.71 (10:05 iex) | -19.0% | 31.76 | 27.18 / 25.04-27.31 | 2.54 (8.0%) | 29.45-41.61 | -13.1% / -9.0% | -2.9% | 7.8M |
| COHX | 12.21 (10:04 iex) | -15.3% | 14.41 | 12.79 / 11.95-12.88 | 3.27 (22.7%) | 12.07-31.06 | -35.1% / -40.2% | -19.5% | 1.4M |
| USDE | 10.11 (10:05 iex) | -14.8% | 11.87 | 10.84 / 10.10-10.89 | 1.30 (10.9%) | 9.64-18.11 | -11.4% / +24.6% | +0.3% | 2.6M |
