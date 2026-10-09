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

Futures and news are checked (Delta missed, Apple's iPhone order cuts, oil easing on Iran comments, UMich due at 10:00). I'm writing the brief now.

# Pre-market brief — Friday 2026-10-09

### 1. Tape
Futures are higher: ES about +0.3–0.4%, NQ about +0.7–0.8%, Dow flat. Two things drive it. Oil eased after Trump said the US would not attack Iran before the midterms (Brent about $102.6, −1.6%), and tech is recovering Thursday's AI selloff after Bloomberg reported OpenAI expects ≥$70B annualized revenue by year-end. That undercuts Thursday's "$20B lower" story. The 10y is about 5.23–5.26%, still near 2002 highs. VIX is about 15.2. Semis lead pre-market (SMH +1.4%, NVDA +1.5%, AMD +1.4%, AVGO +1.5%). Apple is the notable laggard at −2.5% (331.85) on reports it cut iPhone 18 Pro component orders ≥15%. The regime is choppy, rotating risk-on into a weekend, with CPI/PPI next week. The edge is modestly long in index terms, but the cleanest single-name setup today is on the short side (AAPL).

### 2. Calendar
| Event | ET | Stockholm | Status / figure | Touches |
|---|---|---|---|---|
| DAL Q3 earnings | pre-mkt | — | **Out:** adj EPS $1.72 vs ~$1.75–1.82 est, rev $17.59B vs $17.67B; FY guide cut to $5.10–5.60 on fuel (+62% y/y). DAL −2.5% pre at 80.05 | airlines (passed) |
| Trump: no Iran strike before midterms | overnight | — | Brent −1.6% to ~$102.6 | XOM resting long, TLT resting short |
| UMich sentiment (prelim, Oct) | 10:00 | 16:00 | Consensus 47.6 (Sep final 48.1); expectations 46.1. Inflation expectations are the part that matters | TLT, AAPL, all |
| Next week: Sep CPI and PPI mid-week (exact days not verified); Monday 10/12 Columbus Day, bond market closed and equities open (inferred from the usual schedule) | — | — | ambient risk under rule 8 | all |

### 3. Open positions and resting entries
- **MSFT long** (527.65, stop 515, target 548): **intact.** Pre-market is 527.50 on the tech rebound, holding above the 522.85 breakout level. The stop sits 1 ATR below entry under the breakout. Hold with no change.
- **XOM resting buy stop 169.80**: **cancel.** The thesis was oil-shock follow-through to a fresh 20d high. Today's catalyst is the reverse (Iran de-escalation, Brent down), and a breakout fill into falling crude is a poor location. It also frees about 0.25% of risk.
- **TLT resting sell stop 76.35**: **keep.** The yields-at-2002-highs thesis is weakened by the oil drop but not invalidated. The 10y is still about 5.25% and CPI is next week. The trigger is about 1.8% below the 77.78 pre-market price, so it only fills on a genuine break of the 76.43 20d low, which is the condition the thesis needs. The harness clears it before the weekend anyway.
- **HD resting sell stop 276.90**: **keep.** It is 6% below pre-market and won't fill today barring a shock. It is harmless and will be cleared before the weekend.

### 4. New plays

**AAPL short (half tier)**
| Field | Value |
|---|---|
| Ticker | AAPL |
| Direction | Short |
| Catalyst | 2026-10-09 reports that Apple cut October iPhone 18 Pro/Pro Max component orders ≥15% from plan on weaker demand, after a $100 price hike |
| Thesis | A demand-side datapoint on the flagship cycle lands while the stock sits +5.6% over its 50d. A break of the 325.81 20d low confirms that holders are repricing the cycle rather than buying the dip, which opens a move toward 312. |
| Entry | Sell stop 325.40 (below 20d low 325.81; pre-market 331.85, verified Alpaca) |
| Stop | 336.50: above today's gap level / pre-market area. If AAPL recovers there, the gap has filled and the report is being dismissed. That is 1.8 ATR from entry. |
| Target | 312.00 (−13.4 vs 11.1 risk = 1.2R) |
| Risk tier | 0.5: it goes against an intact intermediate uptrend, and single-source supply-chain reports are often walked back |
| Time horizon | 1–5 days |
| Conviction | 3 |
| P(target before stop) | 0.40 |
| Invalidation | A credible denial or a sell-side read that the cuts are a Pro→base mix shift; AAPL closing back above 340 |
| What I'd be wrong about | Supply-chain order-cut stories have a long history of being faded. With semis and NQ bid, money may rotate back into mega-cap tech and leave this as a one-day gap. |

Apple's earnings are expected late October (not verified), which is outside the 5-day horizon. The single-source flag applies: the report reaches me via TipRanks summarizing supply-chain sources.

**NVDA long (probe)**
| Field | Value |
|---|---|
| Ticker | NVDA |
| Direction | Long |
| Catalyst | 2026-10-09 Bloomberg report that OpenAI expects ≥$70B annualized revenue by year-end, reversing Thursday's AI-demand scare; semis lead pre-market |
| Thesis | Thursday's AI selloff rested on a revenue story that is now contradicted. A push through 237.60 means the rebound has buyers beyond the open, with room to the 243.37 20d high and beyond. |
| Entry | Buy stop 237.60 (pre-market 233.94 iex, verified) |
| Stop | 228.80: under Thursday's 230.48 close. Losing that means the rebound failed completely. That is 1.6 ATR from entry. |
| Target | 251.00 (1.5R) |
| Risk tier | 0.25: the rebound is headline-driven, and the last two AI-momentum longs/passes (AVGO, AMD) stopped out |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 0.36 |
| Invalidation | The OpenAI revenue story is muddied again, or SMH gives back its pre-market gain by the close |
| What I'd be wrong about | Thursday's drop may be about crowding, not one headline. A buy stop into a gap-up Friday often fills near the high of the day. |

### 5. Both sides
- **Best short:** AAPL, sell stop 325.40 / stop 336.50 / target 312, P 0.40. **Taken** (section 4).
- **Best long:** NVDA, buy stop 237.60 / stop 228.80 / target 251, P 0.36. **Taken as a probe.**

### 6. Passing on
- **DAL short**, sell stop 76.70 / stop 82.60 / target 70.00, P 0.33. The miss and guide cut are real, but the stock falls on the same day oil falls. The fuel headwind behind the cut is easing, and the CEO says demand is strong, so the two drivers conflict.
- **XLE long**, limit 64.20 / stop 62.60 / target 67.40, P 0.35. Energy is +4.1% over 5d, and de-escalation removes the bid. It is the wrong day to buy the dip in oil names.
- **XOM** (cancelled resting order) is not re-proposed as a pass; it is the same idea as XLE.

### 7. For the post-open review
- **AAPL:** if it trades below 328 by 10:05 with SPY green, the relative weakness is confirmed. The review may cancel the stop entry and short at market, keeping stop 336.50 and target 312 at the 0.5 tier. If AAPL has reclaimed 336, cancel the entry.
- **NVDA:** if it opens above 237.60 and the fill sits above 239, keep it. If it fills and immediately loses 234, close.
- **UMich 10:00:** a 1-yr inflation expectation jump with a 10y back above 5.30% supports keeping TLT. A soft print plus falling oil means cancel TLT.
- **MSFT:** no action unless it loses 520 on the open. In that case, tighten the stop to 515 or hold it there; no widening.

### 8. Book state
After cancelling XOM and adding AAPL (0.5%) and NVDA (0.25%), risk at stake is about 2.2% of equity (cap 4%). Gross is about 74% if every resting entry filled; net is about −16% (cap ±100%). Slots: 1 open + 4 resting = 5 of 8. Tech sector net is about MSFT +19k, NVDA +6.7k, AAPL −14.6k ≈ +11% of equity (cap 40%).

```json
{
  "date": "2026-10-09",
  "no_trade": false,
  "session_note": "Risk-on rebound in tech as oil eases on Iran de-escalation; shorting AAPL's break of 20d low on iPhone order-cut report, probing NVDA rebound breakout; cancelling XOM breakout long.",
  "plays": [
    {
      "ticker": "AAPL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 325.40,
      "stop": 336.50,
      "targets": [312.00],
      "time_horizon": "1-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.40,
      "catalyst": "2026-10-09 reports Apple cut October iPhone 18 Pro/Pro Max component orders >=15% on weaker demand after a $100 price hike.",
      "thesis": "Demand-side datapoint on the flagship cycle with the stock +5.6% over its 50d. A break of the 325.81 20d low confirms repricing rather than dip-buying, opening 312.",
      "invalidation": "Credible denial or mix-shift explanation; AAPL closing back above 340.",
      "bear_case": "Supply-chain order-cut stories are frequently faded, and with semis/NQ bid money may rotate back into mega-cap tech."
    },
    {
      "ticker": "NVDA",
      "direction": "long",
      "entry_type": "stop",
      "entry": 237.60,
      "stop": 228.80,
      "targets": [251.00],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.36,
      "catalyst": "2026-10-09 Bloomberg: OpenAI expects >=$70B annualized revenue by year-end, contradicting Thursday's AI-demand scare; semis lead pre-market.",
      "thesis": "Thursday's AI selloff rested on a revenue story now contradicted. A push through 237.60 shows follow-through buyers with room to the 243.37 20d high and beyond.",
      "invalidation": "OpenAI revenue story muddied again, or SMH gives back its pre-market gain by the close.",
      "bear_case": "Thursday's drop may reflect crowding rather than one headline; a buy stop into a gap-up Friday often fills near the day's high."
    }
  ],
  "manage": [
    {
      "ticker": "XOM",
      "action": "close",
      "reason": "Oil-breakout thesis decayed: Brent -1.6% on Trump saying no Iran strike before midterms; buying a 20d-high breakout into falling crude is the wrong location."
    }
  ],
  "passed": [
    {
      "ticker": "DAL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 76.70,
      "stop": 82.60,
      "targets": [70.00],
      "p_target_first": 0.33,
      "reason": "Q3 miss and FY cut are real, but oil is falling the same day, easing the fuel headwind behind the cut; CEO says demand strong."
    },
    {
      "ticker": "XLE",
      "direction": "long",
      "entry_type": "limit",
      "entry": 64.20,
      "stop": 62.60,
      "targets": [67.40],
      "p_target_first": 0.35,
      "reason": "Energy +4.1% over 5d and de-escalation removes the bid; wrong day to buy the dip in oil."
    }
  ]
}
```

Sources: [Yahoo Finance live, Oct 9](https://finance.yahoo.com/markets/live/stock-market-today-friday-october-9-dow-sp-500-nasdaq-080148117.html), [TheStreet, Oct 9](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-09-2026), [Investrade morning preview](https://investrade.com/morning-preview-october-09-2026/), [CNBC on DAL Q3](https://www.cnbc.com/2026/10/09/delta-air-lines-dal-q3-2026-earnings.html), [TipRanks on AAPL](https://www.tipranks.com/news/why-is-apple-stock-aapl-falling-in-premarket-today-oct-9), [TipRanks premarket chips](https://www.tipranks.com/news/chip-stocks-nvidia-amd-and-broadcom-gain-premarket-while-apple-aapl-drops-whats-moving-markets-today-oct-9), [Trading Economics Brent](https://tradingeconomics.com/commodity/brent-crude-oil), [Admiral Markets UMich preview](https://admiralmarkets.com/analytics/traders-blog/michigan-consumer-sentiment-october-2026-what-to-expect-on-9-october), [Trading Economics 10y](https://tradingeconomics.com/united-states/government-bond-yield)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Friday 2026-10-09. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$99,959.79**
- Cash: $80,967.27
- Session P&L so far: +0.18% (new entries are blocked at -3.0%)
- Gross exposure: $77,124 (77% of equity, cap 150%)
- Net exposure: $-25,833 (-26%, cap +/-100%)
- Risk at stake (entry to stop): $2,199 (2.20% of equity, cap 4.0%) — 1.80% left for new plays
- Slots: 1 open + 4 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| MSFT | long | 36 | 527.65 | 527.57 | -3 (-0.0%) | 515.00 | 548.00 | MSFT is +3.2% vs 20d and +6.2% vs 50d and has held up under higher rates. A break of 522.85 clears a three-week ceiling  |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| NVDA | long | 28 | 237.60 | stop | 228.80 | 251.00 | 2026-10-09 |
| AAPL | short | 45 | 325.40 | stop | 336.50 | 312.00 | 2026-10-09 |
| TLT | short | 312 | 76.35 | stop | 77.95 | 73.50 | 2026-10-08 |
| HD | short | 47 | 276.90 | stop | 287.50 | 260.00 | 2026-10-07 |

### Record

15 closed trades: 4W / 11L, total -4.08R, net $-32 realized. Shorts taken: 14.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| NVDA | long | stop | -0.38R | $-235 | 40% |
| IWM | long | close | -1.16R | $-590 | 40% |
| JNJ | short | stop | -1.02R | $-550 | 38% |
| CAT | long | stop | -0.90R | $-224 | 36% |
| WMT | short | stop | -1.00R | $-254 | 34% |

### Ideas you passed on, replayed against the tape

17 resolved: 4 reached target first, 10 stop first, 2 never reached the entry, 1 expired, 0 ambiguous. Average -0.16R across the 15 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-08 pre-market | XLRE | short | Same rates factor as the TLT short and HD resting order; a third rates short is  | stop | -1.00R | 33% |
| 2026-09-28 pre-market | UAL | short | Oil-pain short is purely an Iran-headline bet; binary reversal risk on any deal. | target | +1.94R | 36% |
| 2026-10-06 open | AVGO | long | Breaking 20d high 372.02 on AI tape, but tech is ~35% of equity against the 40%  | stop | -1.00R | 40% |
| 2026-10-06 pre-market | AMD | long | Best long on the tape, but tech is ~35% of equity against the 40% sector cap. | stop | -1.03R | 40% |
| 2026-09-28 pre-market | XOM | long | Headline-driven oil spike with weak 5d energy relative strength; not chasing. | target | +1.95R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| MSFT | 527.79 (10:04 iex) | +1.0% | 522.61 | 528.05 / 526.24-531.60 | 12.43 (2.4%) | 487.23-535.69 | +2.9% / +4.8% | +1.9% | 22.3M |
| NVDA | 230.98 (10:05 iex) | +0.2% | 230.48 | 233.85 / 230.66-233.92 | 5.35 (2.3%) | 208.93-243.37 | +1.9% / +4.2% | -0.2% | 110.5M |
| AAPL | 332.25 (10:05 iex) | -2.4% | 340.42 | 331.69 / 330.70-333.80 | 6.23 (1.8%) | 325.81-345.34 | +1.6% / +5.6% | +3.1% | 38.6M |
| TLT | 77.63 (10:05 iex) | -0.3% | 77.87 | 77.71 / 77.59-77.73 | 0.87 (1.1%) | 76.43-81.61 | -1.7% / -3.5% | +0.2% | 49.6M |
| HD | 291.61 (10:05 iex) | -1.3% | 295.47 | 294.99 / 290.50-295.50 | 6.67 (2.3%) | 277.15-312.67 | +0.3% / -6.9% | +4.6% | 5.5M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 775.60 (10:05 iex) | +0.2% | 773.93 | 776.24 / 775.14-776.84 | 6.81 (0.9%) | 747.74-781.62 | +0.9% / +1.1% | +1.3% | 46.1M |
| QQQ | 749.19 (10:05 iex) | +0.2% | 747.58 | 752.55 / 748.55-752.87 | 9.76 (1.3%) | 699.27-762.86 | +1.6% / +3.5% | +0.7% | 34.4M |
| IWM | 278.66 (10:05 iex) | +0.4% | 277.57 | 278.21 / 277.46-279.01 | 3.73 (1.3%) | 274.52-290.68 | -1.7% / -4.7% | -0.5% | 25.7M |
| DIA | 512.70 (10:04 iex) | +0.2% | 511.65 | 511.79 / 511.67-513.54 | 4.78 (0.9%) | 504.70-526.15 | -0.7% / -2.6% | +0.6% | 3.4M |
| TLT | 77.63 (10:05 iex) | -0.3% | 77.87 | 77.71 / 77.59-77.73 | 0.87 (1.1%) | 76.43-81.61 | -1.7% / -3.5% | +0.2% | 49.6M |
| GLD | 383.65 (10:05 iex) | +1.3% | 378.62 | 383.98 / 383.37-384.69 | 5.84 (1.5%) | 374.23-403.65 | -2.6% / -4.6% | -1.1% | 8.4M |
| USO | 148.01 (10:04 iex) | +0.3% | 147.58 | 146.85 / 146.80-148.01 | 5.76 (3.9%) | 141.76-163.35 | -1.5% / +6.4% | -1.6% | 6.1M |
| SMH | 605.99 (10:04 iex) | -0.2% | 607.27 | 615.14 / 604.26-615.54 | 14.34 (2.4%) | 537.73-639.47 | +2.0% / +5.3% | -1.7% | 6.4M |
| XLK | 197.75 (10:04 iex) | -0.0% | 197.78 | 199.40 / 197.41-199.41 | 2.97 (1.5%) | 181.87-203.25 | +2.0% / +5.0% | -0.0% | 7.5M |
| XLF | 54.33 (10:05 iex) | +0.2% | 54.23 | 54.25 / 54.21-54.54 | 0.69 (1.3%) | 52.81-57.41 | -1.1% / -3.9% | +1.4% | 38.9M |
| XLE | 65.57 (10:05 iex) | +0.5% | 65.24 | 64.96 / 64.94-65.70 | 1.28 (2.0%) | 60.95-65.72 | +3.2% / +4.8% | +4.1% | 35.6M |
| XLV | 169.97 (10:05 iex) | +1.1% | 168.16 | 167.73 / 167.52-170.43 | 2.69 (1.6%) | 164.48-171.87 | -0.0% / -0.1% | +1.2% | 8.2M |
| XLI | 168.72 (10:04 iex) | +0.2% | 168.40 | 168.71 / 167.91-169.06 | 2.39 (1.4%) | 166.18-172.45 | -0.6% / -4.1% | -0.1% | 7.6M |
| XLY | 112.42 (10:04 iex) | +0.6% | 111.71 | 112.36 / 112.21-112.75 | 1.38 (1.2%) | 107.99-113.29 | +0.9% / -2.2% | +2.7% | 6.7M |
| XLP | 83.17 (10:05 iex) | -0.3% | 83.42 | 82.97 / 82.96-83.47 | 0.98 (1.2%) | 80.10-84.33 | +1.6% / -0.3% | +3.8% | 11.0M |
| XLU | 41.11 (10:04 iex) | +0.1% | 41.07 | 40.98 / 40.97-41.30 | 0.61 (1.5%) | 39.03-42.65 | +1.5% / -2.4% | +3.5% | 34.0M |
| XLB | 49.54 (10:04 iex) | +0.5% | 49.27 | 49.45 / 49.17-49.61 | 0.74 (1.5%) | 47.81-50.98 | -0.9% / -3.8% | +1.5% | 11.9M |
| XLRE | 41.26 (10:03 iex) | +1.0% | 40.85 | 41.22 / 41.17-41.47 | 0.53 (1.3%) | 40.28-43.23 | -2.1% / -5.5% | +0.4% | 6.6M |
| XLC | 111.10 (10:05 iex) | -0.9% | 112.07 | 111.29 / 110.92-111.60 | 1.70 (1.5%) | 109.66-115.61 | -0.1% / +0.5% | +1.9% | 6.1M |
| KRE | 69.14 (10:05 iex) | -0.6% | 69.59 | 69.38 / 68.91-69.62 | 1.27 (1.8%) | 67.97-74.43 | -2.2% / -5.4% | -0.5% | 16.2M |
| XHB | 95.10 (10:04 iex) | -0.6% | 95.68 | 95.69 / 94.58-96.02 | 2.20 (2.3%) | 93.63-99.67 | -1.3% / -6.0% | -1.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 332.25 (10:05 iex) | -2.4% | 340.42 | 331.69 / 330.70-333.80 | 6.23 (1.8%) | 325.81-345.34 | +1.6% / +5.6% | +3.1% | 38.6M |
| MSFT | 527.79 (10:04 iex) | +1.0% | 522.61 | 528.05 / 526.24-531.60 | 12.43 (2.4%) | 487.23-535.69 | +2.9% / +4.8% | +1.9% | 22.3M |
| NVDA | 230.98 (10:05 iex) | +0.2% | 230.48 | 233.85 / 230.66-233.92 | 5.35 (2.3%) | 208.93-243.37 | +1.9% / +4.2% | -0.2% | 110.5M |
| AMZN | 258.42 (10:05 iex) | +1.7% | 254.06 | 256.32 / 256.00-259.00 | 5.43 (2.1%) | 244.30-260.14 | +0.9% / -1.7% | +2.3% | 36.7M |
| GOOGL | 351.70 (10:05 iex) | +1.0% | 348.29 | 351.40 / 350.31-353.90 | 8.81 (2.5%) | 335.03-364.17 | +0.9% / +0.7% | +3.0% | 26.8M |
| META | 718.26 (10:05 iex) | -0.4% | 720.89 | 726.01 / 716.66-726.96 | 27.43 (3.8%) | 645.69-779.82 | +0.8% / +13.4% | -0.7% | 21.9M |
| TSLA | 384.66 (10:05 iex) | +2.6% | 375.00 | 382.38 / 381.23-388.53 | 11.07 (3.0%) | 345.88-386.83 | +2.0% / +6.2% | +5.9% | 35.7M |
| AVGO | 363.26 (10:05 iex) | +0.9% | 360.14 | 365.73 / 362.67-366.63 | 10.59 (2.9%) | 335.20-380.84 | +1.4% / -3.2% | +4.8% | 24.3M |
| AMD | 615.35 (10:05 iex) | -0.9% | 620.68 | 626.89 / 611.22-627.37 | 24.71 (4.0%) | 480.33-658.52 | +4.6% / +17.9% | +0.8% | 22.4M |
| ORCL | 139.49 (10:05 iex) | +3.2% | 135.19 | 136.70 / 136.49-141.10 | 5.84 (4.3%) | 131.10-165.39 | -4.8% / -6.7% | -1.7% | 33.7M |
| NFLX | 71.19 (10:05 iex) | -0.5% | 71.57 | 70.50 / 70.32-72.10 | 1.55 (2.2%) | 66.54-81.02 | -0.6% / -5.1% | +5.5% | 37.4M |
| CRM | 227.37 (10:05 iex) | -0.2% | 227.80 | 229.60 / 226.66-230.71 | 7.86 (3.4%) | 220.29-261.87 | -3.7% / +1.8% | -3.8% | 10.8M |
| JPM | 330.93 (10:05 iex) | -0.1% | 331.42 | 331.20 / 330.70-332.56 | 5.85 (1.8%) | 324.25-358.26 | -2.3% / -5.0% | -0.0% | 8.7M |
| GS | 880.11 (10:03 iex) | -0.3% | 882.59 | 887.68 / 879.37-887.68 | 19.61 (2.2%) | 868.52-1,042.99 | -5.2% / -10.9% | -1.6% | 2.2M |
| BAC | 53.48 (10:05 iex) | -0.2% | 53.61 | 53.41 / 53.41-53.80 | 1.00 (1.9%) | 52.24-63.83 | -4.8% / -10.7% | -0.2% | 40.5M |
| XOM | 169.46 (10:04 iex) | +0.6% | 168.50 | 167.87 / 167.82-169.88 | 3.55 (2.1%) | 155.85-169.64 | +3.2% / +4.6% | +2.9% | 13.4M |
| CVX | 212.57 (10:04 iex) | +0.5% | 211.55 | 211.05 / 210.71-212.86 | 4.27 (2.0%) | 200.78-217.78 | +1.8% / +4.0% | +2.1% | 9.5M |
| LLY | 1,169.42 (10:05 iex) | -0.0% | 1,169.60 | 1,153.56 / 1,151.67-1,172.49 | 37.10 (3.2%) | 1,113.29-1,215.00 | +1.0% / -0.3% | +1.7% | 2.3M |
| UNH | 376.60 (10:05 iex) | +1.5% | 370.95 | 373.94 / 373.02-387.52 | 8.05 (2.2%) | 362.60-389.33 | -1.0% / -4.5% | +1.6% | 5.0M |
| JNJ | 259.32 (10:04 iex) | +1.1% | 256.48 | 255.09 / 254.99-259.32 | 5.08 (2.0%) | 251.17-275.23 | -3.2% / -3.1% | -0.8% | 6.8M |
| WMT | 110.64 (10:05 iex) | +0.1% | 110.56 | 110.00 / 109.93-111.51 | 2.31 (2.1%) | 103.39-111.23 | +2.9% / +2.0% | +6.0% | 22.6M |
| COST | 944.20 (10:04 iex) | -0.4% | 947.92 | 945.00 / 944.20-951.29 | 15.94 (1.7%) | 883.10-953.25 | +3.8% / +1.8% | +3.6% | 2.4M |
| HD | 291.61 (10:05 iex) | -1.3% | 295.47 | 294.99 / 290.50-295.50 | 6.67 (2.3%) | 277.15-312.67 | +0.3% / -6.9% | +4.6% | 5.5M |
| CAT | 798.08 (10:04 iex) | +0.2% | 796.18 | 796.22 / 791.19-802.06 | 26.04 (3.3%) | 772.86-876.95 | -2.3% / -3.2% | -3.7% | 2.4M |
| BA | 190.37 (10:04 iex) | +1.4% | 187.75 | 187.99 / 187.60-190.81 | 6.16 (3.3%) | 184.01-212.40 | -4.3% / -10.8% | -2.4% | 9.2M |
| DAL | 80.69 (10:04 iex) | -1.8% | 82.14 | 79.68 / 79.16-81.14 | 2.47 (3.0%) | 76.89-86.17 | -0.1% / -2.0% | -2.4% | 8.0M |
| UAL | 105.66 (10:05 iex) | -1.7% | 107.44 | 106.44 / 104.29-107.18 | 4.16 (3.9%) | 104.59-118.26 | -2.9% / -6.6% | -3.9% | 4.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-09 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| VEEA | 5.66 (10:04 iex) | +46.3% | 3.87 | 5.53 / 5.40-6.24 | 0.89 (23.0%) | 1.53-8.88 | +2.4% / +29.0% | +11.5% | 21.3M |
| NVAX | 12.36 (10:05 iex) | +12.3% | 11.01 | 11.17 / 11.03-12.76 | 0.91 (8.3%) | 9.13-13.38 | +4.7% / +16.8% | +3.9% | 7.3M |
| HUM | 432.00 (10:05 iex) | +11.6% | 387.12 | 450.49 / 432.00-456.50 | 15.18 (3.9%) | 369.13-415.77 | -0.6% / +0.1% | +2.0% | 1.3M |
| DNA | 12.59 (10:04 iex) | +11.0% | 11.34 | 11.76 / 11.48-12.71 | 1.76 (15.5%) | 6.52-18.22 | +13.0% / +33.8% | -9.3% | 3.4M |
| NN | 12.85 (10:04 iex) | +10.8% | 11.60 | 13.00 / 12.62-13.19 | 0.99 (8.6%) | 10.77-15.88 | -18.5% / -24.5% | -15.7% | 2.8M |
| XRPN | 19.14 (10:05 iex) | -20.9% | 24.20 | 20.88 / 18.87-20.90 | 7.52 (31.1%) | 10.53-53.00 | +48.5% / +88.8% | +3.3% | 1.7M |
| ALHC | 7.14 (10:05 iex) | -18.0% | 8.71 | 6.91 / 6.01-7.36 | 0.50 (5.7%) | 7.37-13.33 | -0.8% / -25.8% | +12.5% | 13.6M |
| ASTX | 7.30 (10:05 iex) | -17.4% | 8.84 | 8.05 / 7.19-8.47 | 1.34 (15.2%) | 8.48-11.90 | -12.0% / -23.9% | -1.8% | 4.6M |
