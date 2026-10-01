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

# Pre-market brief: Thursday 2026-10-01

*Written 09:05 ET (15:05 Stockholm). The cash session opens at 09:30 ET (15:30 Stockholm).*

## 1. Tape

US index futures are modestly higher. S&P futures are up about 0.3% and Nasdaq-100 futures about 0.6% (verified: SPY 764.90, QQQ 743.74, from the market data table). The bid comes from Micron's report last night: revenue quadrupled, guidance beat, and customer long-term supply commitments rose to $32B from $22B. NVDA, AMD and AVGO are higher pre-market, and so is SMH at 612.44, just under its 20-day high of 613.27.

Against that, the 10-year Treasury yield is up about 4bp to roughly 5.33%, which sources call a multi-decade high. The dollar is firm, TLT is down 0.5% at 77.05 (below its 20-day low), and oil is up 1.2% (USO).

The tape has split. AI and semis are being bid; rate-sensitive groups are making 20-day lows: financials (XLF and KRE at their 20-day floors), housing (HD, XHB), utilities, real estate and staples. I see the edge on the **short side in rate-sensitives** and the **long side only in AI/semis leadership**. Friday's payrolls report is the next macro test.

## 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 08:30 | 14:30 | Initial jobless claims | **197K actual** vs 201K consensus (prior revised 198K); continuing claims consensus was 1,730K. A tight labor print, consistent with the yield pressure. | BAC, XLU, HD (rates) |
| 09:45 | 15:45 | S&P Global manufacturing PMI (final) | Final revision; not a mover | CAT |
| 10:00 | 16:00 | ISM manufacturing | Consensus 54.8 (prior 54.6) | CAT long (resting), DAL; the review reads it |
| After close | after 22:00 | Nike earnings | Not held | none |
| Fri 08:30 | Fri 14:30 | September payrolls | Ahead; inside every horizon | everything; ambient risk under rule 8 |

## 3. Open positions and resting entries

**BAC short** (entry 55.80, last 54.26, stop 57.70, target 52.90): **thesis intact.** BAC is trading below its 20-day low of 54.38, and XLF and KRE are at their floors with yields rising. The stop is currently 3.44 above the market, about 2.6 ATR. I am **tightening it to 56.00**: 1.74 above last (1.3 ATR) and just above my entry, so the trade becomes close to risk-free. Target unchanged. **Hold.**

**HD short** (entry 289.30, last 283.07, stop 297.60, target 278.00): **thesis intact.** HD is below its 20-day low of 284.01, and a 5.33% 10-year yield is the housing thesis itself. I am **tightening the stop to 290.50**: 1.15 ATR above last and 1.20 above entry. Target unchanged. **Hold.**

Both tightenings also free up risk budget. Book-wide risk at stake drops by about $890.

Resting entries:

- **UNH short, sell stop 363.50** (last 367.85, 20-day low 365.72). **Keep.** It triggers only on a clean break of the 20-day low.
- **CAT long, buy stop 840.00** (last 812.50, 20-day high 831.95). **Keep.** The 10:00 ISM print is the swing factor; the conditions are in section 7.
- **XLU short, sell stop 38.95** (last 39.54, 20-day low 39.03). **Keep.** The surge in yields directly supports this thesis.
- **DAL long, buy stop 85.80** (last 83.55, 20-day high 85.47). **Keep, but weakening**: oil is up 1.2% and a strong dollar works against it. The review should cancel it if crude extends (section 7).
- **NVDA long, buy stop 234.70** (last 230.32, 20-day high 234.50). **Keep.** Micron's read-through is exactly the catalyst for this breakout. It expires at the Friday weekend clear anyway.
- **ORCL short, sell stop 130.90** (last 139.40, +1.5% pre-market). **Cancel.** The trigger is 6% below the market on a day the AI complex is being bid. I put the chance it triggers before Friday's weekend clear at about 15%. It is holding a slot and about 0.49% of equity in reserved risk (65 × 7.70) for a low-probability fill. This is a decision about how the book's capacity is used. It is not a change to the thesis, which was untested.

## 4. New plays

The book state shows **0 slots** and 0.30% risk left. Cancelling ORCL frees one slot. If the harness applies the `manage` changes before it admits plays, the probe below fits within risk as well. If it doesn't, the harness drops the play and logs it as a pass. Either way the outcome is acceptable.

| Field | Value |
|---|---|
| Ticker | MSFT |
| Direction | Long |
| Catalyst | Micron's AI memory blowout (reported 2026-09-30 after close) is lifting AI megacaps. MSFT is +1.2% pre-market at 518.92, just under its 20-day high of 519.83. |
| Thesis | MSFT is +2.5% over 5 days, 6.4% above its 50-day average, and one of the few megacaps leading. A break above the 20-day high on an AI-led tape should extend toward the late-summer highs. |
| Entry | Buy stop at 523.00, above the 20-day high and above pre-market so the broker will accept it |
| Stop | 509.00: below yesterday's close of 512.90 and about 1.2 ATR under the trigger. If the move fails back below yesterday's close, the breakout was false. |
| Target | 547.00 (+1.7R) |
| Risk tier | 0.25 (probe). Yields at 5.33% are a valuation headwind for long-duration tech, so conviction is lower. |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 40% |
| Invalidation | It triggers and then closes back below 515, or the 10-year pushes through 5.40% and tech rolls over |
| What I'd be wrong about | Rising real yields compress multiples on long-duration growth. One memory-chip print may not carry software megacaps, and Friday's payrolls could reprice rates sharply. |

Rule 8: MSFT's own earnings fall in late October, outside the holding horizon.

## 5. Both sides

- **Best long: MSFT** breakout probe. Buy stop 523 / stop 509 / target 547, P = 0.40. **Taken** (section 4). NVDA is the purer expression of the same idea, and its buy stop is already resting.
- **Best short: XLRE.** At 40.91 it is on its 20-day low of 40.87 with the 10-year at 5.33%. Sell stop 40.80 / stop 41.70 / target 39.40, P = 0.38. **Passed** only because there is no slot. XLU (resting), HD and BAC already express the same rates-up view, so XLRE would stack correlated risk.

## 6. Passing on

- **XLRE short**: see section 5. No slot, and it duplicates the rates exposure.
- **KRE short**: sell stop 68.90 / stop 70.70 / target 66.00, P = 0.40. Same rates factor as the BAC short I already hold; that would be a sector stack.
- **MU long**: verified at about $1,055 pre-market. Chasing a gap after earnings with no slot available; no structural level to stop against.

## 7. For the post-open review

- **10:00 ISM**: if the print is 53 or lower, or CAT trades below 800 by 10:05, cancel the CAT buy stop. If the print is above 55 and CAT holds above 815, keep it.
- **DAL**: if USO is up more than 2.5% by 10:05, cancel the DAL buy stop because fuel costs undercut the thesis. Otherwise keep it.
- **BAC / HD**: if either reclaims its 20-day low on the open (BAC above 54.40, HD above 284.00 and holding at 10:05), leave the tightened stops in place. Do not move them back up.
- **MSFT**: if it triggers at the open and then trades back below 515 by 10:05, close it.

## 8. Book state

After these changes (ORCL cancelled, MSFT added, two stops tightened), slots are 8 of 8. Risk at stake is about 2.6% of equity, against a 4% cap. Gross exposure is about 105% if every resting order fills (cap 150%). Net exposure is about -10% (cap ±100%).

Sources: [TheStreet, Oct 1](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-01-2026), [Tickmill](https://www.tickmill.com/blog/daily-market-outlook-october-1-2026), [CNBC](https://www.cnbc.com/2026/09/30/stock-market-today-live-updates.html), [FXStreet claims](https://www.fxstreet.com/news/us-initial-jobless-claims-dropped-to-197k-last-week-202610011237), [investinglive claims](https://investinglive.com/news/us-initial-jobless-claims-197k-vs-201k-expected/), [Investing.com calendar](https://www.investing.com/news/stock-market-news/jobless-claims-manufacturing-pmi-and-ism-data-due-thursday-93CH-4925705), [Investing.com Micron/Nike](https://www.investing.com/news/economy-news/microns-aidriven-outlook-nike-to-report--whats-moving-markets-4926463), [Yahoo live](https://finance.yahoo.com/markets/live/stock-market-today-thursday-oct-1-dow-sp-500-nasdaq-080602402.html)

```json
{
  "date": "2026-10-01",
  "no_trade": false,
  "session_note": "Split tape: Micron-led AI bid vs 10y at ~5.33% crushing rate-sensitives; tighten BAC/HD shorts, cancel stale ORCL short trigger, add MSFT breakout probe.",
  "plays": [
    {
      "ticker": "MSFT",
      "direction": "long",
      "entry_type": "stop",
      "entry": 523.00,
      "stop": 509.00,
      "targets": [547.00],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.40,
      "catalyst": "Micron AI-memory beat (2026-09-30 AMC) lifting AI megacaps; MSFT +1.2% pre-market at 518.92 vs 20d high 519.83.",
      "thesis": "MSFT is a leading megacap (+6.4% vs 50d). A break above the 20d high on an AI-led tape should extend toward late-summer highs.",
      "invalidation": "Triggers then closes back below 515, or 10y pushes through 5.40% and tech rolls over.",
      "bear_case": "Multi-decade-high yields compress long-duration multiples; payrolls Friday could reprice rates sharply."
    }
  ],
  "manage": [
    {
      "ticker": "BAC",
      "action": "update",
      "stop": 56.00,
      "reason": "Below 20d low and working; trail stop to just above entry (1.3 ATR over last) to lock near-zero risk."
    },
    {
      "ticker": "HD",
      "action": "update",
      "stop": 290.50,
      "reason": "Below 20d low with 10y at 5.33%; trail stop to ~1.15 ATR above last, near entry."
    },
    {
      "ticker": "ORCL",
      "action": "close",
      "reason": "Sell-stop trigger 130.90 is 6% below pre-market 139.40 on an AI-bid day; ~15% chance of fill before weekend clear, freeing slot and ~0.49% risk."
    }
  ],
  "passed": [
    {
      "ticker": "XLRE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 40.80,
      "stop": 41.70,
      "targets": [39.40],
      "p_target_first": 0.38,
      "reason": "Best short (rates at 5.33%, sitting on 20d low) but no slot and duplicates XLU/HD/BAC rate exposure."
    },
    {
      "ticker": "KRE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 68.90,
      "stop": 70.70,
      "targets": [66.00],
      "p_target_first": 0.40,
      "reason": "Same rates factor as BAC short already held; no slot."
    }
  ]
}
```

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Thursday 2026-10-01. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$102,852.45**
- Cash: $124,650.77
- Session P&L so far: +0.75% (new entries are blocked at -3.0%)
- Gross exposure: $82,373 (80% of equity, cap 150%)
- Net exposure: $+5,824 (+6%, cap +/-100%)
- Risk at stake (entry to stop): $2,326 (2.26% of equity, cap 4.0%) — 1.74% left for new plays
- Slots: 2 open + 4 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| BAC | short | 267 | 55.80 | 53.05 | +734 (+4.9%) | 56.00 | 52.90 | Weakest large bank (-7.5% vs 20d avg). A break below today's opening low confirms the 20d-low support failed and opens a |
| UNH | short | 21 | 363.57 | 363.53 | +1 (+0.0%) | 375.50 | 345.00 | Relative weakness in managed care: -5.2% vs 50d, losing its 20d floor while the market rallies. A trade below 363.50 con |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| CAT | long | 18 | 840.00 | stop | 812.00 | 885.00 | 2026-09-30 |
| XLU | short | 423 | 38.95 | stop | 40.15 | 37.55 | 2026-09-29 |
| DAL | long | 149 | 85.80 | stop | 82.40 | 90.50 | 2026-09-29 |
| NVDA | long | 69 | 234.70 | stop | 227.40 | 246.00 | 2026-09-28 |

### Record

6 closed trades: 3W / 3L, total +1.41R, net $+2,119 realized. Shorts taken: 6.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| HD | short | target | +1.36R | $+691 | 40% |
| BA | short | close | -0.52R | $-130 | 35% |
| DAL | long | stop | +1.00R | $+999 | 46% |
| LLY | long | stop | +1.76R | $+1,654 | 52% |
| ROST | long | stop | -1.18R | $-336 | 47% |

### Ideas you passed on, replayed against the tape

1 resolved: 0 reached target first, 1 stop first, 0 never reached the entry, 0 expired, 0 ambiguous. Average -1.00R across the 1 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-09-28 pre-market | CRM | short | Below 20d low on -4.1% gap but today's catalyst unverified; won't short a gap wi | stop | -1.00R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BAC | 53.05 (10:05 iex) | -2.5% | 54.43 | 54.10 / 53.01-54.34 | 1.33 (2.4%) | 54.38-63.83 | -7.6% / -10.7% | -2.8% | 37.1M |
| UNH | 363.53 (10:05 iex) | -1.0% | 367.08 | 367.99 / 362.81-371.86 | 7.90 (2.2%) | 365.72-404.04 | -3.7% / -6.9% | -1.1% | 5.2M |
| CAT | 805.52 (10:05 iex) | -0.6% | 810.79 | 810.58 / 805.74-815.50 | 20.94 (2.6%) | 771.39-831.95 | +0.4% / -1.8% | -0.2% | 2.4M |
| XLU | 39.13 (10:05 iex) | -0.8% | 39.44 | 39.47 / 39.10-39.49 | 0.56 (1.4%) | 39.03-43.39 | -4.0% / -7.6% | -0.8% | 26.0M |
| DAL | 82.73 (10:05 iex) | -0.9% | 83.46 | 83.77 / 82.56-84.13 | 2.46 (2.9%) | 76.89-85.47 | +3.2% / -0.7% | +2.1% | 7.1M |
| NVDA | 230.69 (10:05 iex) | +1.0% | 228.38 | 229.97 / 228.37-231.91 | 5.30 (2.3%) | 208.93-234.50 | +2.4% / +5.1% | +1.3% | 114.2M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 760.11 (10:05 iex) | -0.3% | 762.63 | 764.35 / 759.89-765.34 | 7.07 (0.9%) | 747.74-775.14 | -0.2% / +0.2% | -0.7% | 45.1M |
| QQQ | 738.50 (10:05 iex) | -0.2% | 739.77 | 742.58 / 738.05-743.92 | 9.83 (1.3%) | 699.27-748.35 | +2.2% / +3.6% | -0.2% | 33.2M |
| IWM | 275.64 (10:05 iex) | -0.8% | 277.89 | 277.36 / 275.67-278.36 | 3.54 (1.3%) | 277.41-295.41 | -2.9% / -5.0% | -1.4% | 23.1M |
| DIA | 505.65 (10:05 iex) | -0.6% | 508.55 | 509.35 / 505.69-510.95 | 5.12 (1.0%) | 508.34-536.38 | -2.2% / -3.3% | -1.1% | 3.4M |
| TLT | 76.81 (10:05 iex) | -0.9% | 77.47 | 76.94 / 76.78-77.16 | 0.80 (1.0%) | 77.24-82.17 | -3.7% / -4.8% | -3.3% | 42.5M |
| GLD | 380.95 (10:03 iex) | +0.0% | 380.84 | 381.91 / 380.75-382.39 | 7.00 (1.8%) | 376.88-413.54 | -3.8% / -3.8% | -3.1% | 9.4M |
| USO | 147.50 (10:04 iex) | +1.3% | 145.66 | 145.85 / 145.59-147.50 | 5.87 (4.0%) | 138.01-163.35 | -2.9% / +6.4% | -2.1% | 6.3M |
| SMH | 610.22 (10:05 iex) | +0.2% | 609.00 | 610.68 / 608.66-614.49 | 15.35 (2.5%) | 537.73-613.27 | +5.6% / +7.2% | +1.3% | 6.4M |
| XLK | 196.20 (10:05 iex) | +0.2% | 195.75 | 196.87 / 196.11-197.47 | 3.22 (1.6%) | 181.87-197.06 | +3.2% / +5.6% | +0.2% | 6.9M |
| XLF | 52.88 (10:05 iex) | -1.0% | 53.40 | 53.25 / 52.88-53.62 | 0.76 (1.4%) | 53.37-58.39 | -4.5% / -5.9% | -2.1% | 37.6M |
| XLE | 61.88 (10:05 iex) | +0.6% | 61.50 | 61.16 / 61.04-62.03 | 1.23 (2.0%) | 60.95-65.78 | -3.1% / -0.3% | -1.4% | 33.6M |
| XLV | 167.39 (10:05 iex) | -0.6% | 168.42 | 168.15 / 167.17-168.60 | 2.31 (1.4%) | 164.48-173.82 | -0.2% / +0.4% | -0.2% | 7.9M |
| XLI | 166.21 (10:05 iex) | -0.5% | 166.98 | 167.14 / 166.34-167.64 | 2.38 (1.4%) | 166.93-175.30 | -2.0% / -5.6% | -1.8% | 7.6M |
| XLY | 108.14 (10:05 iex) | -0.6% | 108.84 | 109.21 / 108.08-109.38 | 1.50 (1.4%) | 108.61-116.81 | -2.6% / -4.7% | -1.6% | 6.4M |
| XLP | 80.25 (10:05 iex) | -0.4% | 80.60 | 80.57 / 80.14-80.66 | 0.95 (1.2%) | 80.57-85.52 | -2.6% / -4.1% | -2.2% | 10.9M |
| XLU | 39.13 (10:05 iex) | -0.8% | 39.44 | 39.47 / 39.10-39.49 | 0.56 (1.4%) | 39.03-43.39 | -4.0% / -7.6% | -0.8% | 26.0M |
| XLB | 47.89 (10:05 iex) | -1.7% | 48.70 | 48.34 / 47.89-48.48 | 0.69 (1.4%) | 48.69-53.27 | -3.5% / -5.3% | -3.1% | 11.0M |
| XLRE | 40.45 (10:05 iex) | -1.1% | 40.91 | 40.78 / 40.41-40.86 | 0.52 (1.3%) | 40.87-43.91 | -3.7% / -6.5% | -2.2% | 5.7M |
| XLC | 110.34 (10:05 iex) | -0.6% | 110.97 | 111.74 / 110.34-111.85 | 1.92 (1.7%) | 110.01-115.61 | -1.2% / -0.1% | -1.4% | 5.7M |
| KRE | 68.09 (10:05 iex) | -1.9% | 69.44 | 69.06 / 68.06-69.33 | 1.25 (1.8%) | 69.11-75.07 | -4.0% / -6.4% | -1.3% | 14.6M |
| XHB | 94.38 (10:04 iex) | -1.7% | 96.03 | 95.55 / 94.24-96.25 | 2.04 (2.1%) | 95.26-102.95 | -2.0% / -6.8% | -1.1% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 329.06 (10:05 iex) | -1.2% | 333.02 | 330.10 / 328.37-332.48 | 6.69 (2.0%) | 309.90-345.34 | +0.5% / +3.4% | -1.2% | 42.5M |
| MSFT | 517.37 (10:05 iex) | +0.9% | 512.90 | 519.88 / 516.27-522.85 | 11.90 (2.3%) | 486.00-519.83 | +2.5% / +6.4% | +2.5% | 21.4M |
| NVDA | 230.69 (10:05 iex) | +1.0% | 228.38 | 229.97 / 228.37-231.91 | 5.30 (2.3%) | 208.93-234.50 | +2.4% / +5.1% | +1.3% | 114.2M |
| AMZN | 247.34 (10:05 iex) | -0.7% | 249.15 | 251.51 / 247.00-251.83 | 5.42 (2.2%) | 244.30-261.12 | -1.3% / -2.7% | -0.0% | 34.4M |
| GOOGL | 342.35 (10:05 iex) | -0.5% | 344.08 | 350.80 / 341.75-353.22 | 8.93 (2.6%) | 327.74-364.17 | +0.5% / +0.1% | +1.9% | 26.8M |
| META | 723.34 (10:05 iex) | -0.3% | 725.18 | 728.52 / 722.96-735.88 | 29.65 (4.1%) | 576.54-779.82 | +6.2% / +16.9% | -2.5% | 24.3M |
| TSLA | 354.76 (10:05 iex) | -0.0% | 354.81 | 356.61 / 353.91-358.40 | 10.84 (3.1%) | 345.88-386.83 | -2.9% / +2.3% | -6.7% | 38.9M |
| AVGO | 348.47 (10:05 iex) | -0.8% | 351.19 | 352.15 / 348.30-354.45 | 9.89 (2.8%) | 335.20-372.02 | -1.1% / -6.2% | -1.1% | 27.6M |
| AMD | 605.03 (10:05 iex) | -1.1% | 611.76 | 611.93 / 604.37-619.00 | 25.81 (4.2%) | 440.50-639.00 | +11.3% / +19.9% | -0.5% | 22.2M |
| ORCL | 135.79 (10:04 iex) | -1.1% | 137.30 | 139.60 / 135.44-140.25 | 7.32 (5.3%) | 131.58-170.70 | -6.6% / -3.9% | -5.0% | 35.6M |
| NFLX | 68.14 (10:05 iex) | -2.1% | 69.58 | 69.41 / 68.10-69.66 | 2.10 (3.0%) | 68.88-83.60 | -7.3% / -8.0% | -2.5% | 34.1M |
| CRM | 235.38 (10:05 iex) | +2.5% | 229.57 | 235.19 / 234.19-239.45 | 8.26 (3.6%) | 221.18-267.80 | -5.7% / +5.9% | -3.4% | 12.7M |
| JPM | 326.50 (10:05 iex) | -1.3% | 330.83 | 328.75 / 326.46-332.69 | 7.23 (2.2%) | 330.83-362.86 | -4.9% / -6.3% | -2.0% | 8.2M |
| GS | 883.53 (10:05 iex) | -1.9% | 900.36 | 896.09 / 883.71-901.63 | 26.97 (3.0%) | 900.36-1,043.84 | -7.3% / -10.7% | -3.8% | 2.1M |
| BAC | 53.05 (10:05 iex) | -2.5% | 54.43 | 54.10 / 53.01-54.34 | 1.33 (2.4%) | 54.38-63.83 | -7.6% / -10.7% | -2.8% | 37.1M |
| XOM | 163.37 (10:04 iex) | +0.4% | 162.75 | 161.50 / 160.81-163.69 | 3.74 (2.3%) | 155.85-169.64 | +0.0% / +1.8% | +0.9% | 14.2M |
| CVX | 205.51 (10:04 iex) | +0.6% | 204.21 | 203.32 / 202.82-205.99 | 4.34 (2.1%) | 200.78-217.78 | -2.3% / +1.4% | -0.6% | 9.9M |
| LLY | 1,150.71 (10:05 iex) | -0.6% | 1,157.08 | 1,155.00 / 1,142.00-1,158.72 | 31.86 (2.8%) | 1,113.29-1,215.00 | +0.4% / -1.7% | +0.5% | 2.3M |
| UNH | 363.53 (10:05 iex) | -1.0% | 367.08 | 367.99 / 362.81-371.86 | 7.90 (2.2%) | 365.72-404.04 | -3.7% / -6.9% | -1.1% | 5.2M |
| JNJ | 263.09 (10:04 iex) | -0.6% | 264.74 | 263.68 / 262.36-263.98 | 4.90 (1.9%) | 260.68-281.07 | -1.8% / -0.2% | -1.6% | 6.4M |
| WMT | 103.86 (10:05 iex) | -0.1% | 103.92 | 104.38 / 103.59-104.88 | 2.15 (2.1%) | 103.92-111.23 | -3.2% / -4.6% | -6.0% | 22.6M |
| COST | 908.08 (10:04 iex) | -0.2% | 910.34 | 910.87 / 903.77-913.00 | 14.59 (1.6%) | 883.10-938.88 | +0.2% / -2.5% | +0.6% | 2.4M |
| HD | 277.91 (10:05 iex) | -2.3% | 284.49 | 283.11 / 277.24-283.85 | 6.47 (2.3%) | 284.01-321.80 | -6.1% / -11.9% | -4.1% | 4.9M |
| CAT | 805.52 (10:05 iex) | -0.6% | 810.79 | 810.58 / 805.74-815.50 | 20.94 (2.6%) | 771.39-831.95 | +0.4% / -1.8% | -0.2% | 2.4M |
| BA | 186.35 (10:04 iex) | +0.2% | 186.05 | 186.00 / 185.85-188.04 | 6.83 (3.7%) | 184.01-215.29 | -7.7% / -12.6% | -6.9% | 7.8M |
| DAL | 82.73 (10:05 iex) | -0.9% | 83.46 | 83.77 / 82.56-84.13 | 2.46 (2.9%) | 76.89-85.47 | +3.2% / -0.7% | +2.1% | 7.1M |
| UAL | 109.72 (10:04 iex) | -1.1% | 110.95 | 110.36 / 109.38-111.33 | 4.20 (3.8%) | 104.59-118.26 | +0.9% / -4.4% | +0.2% | 3.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-01 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| ACN | 226.00 (10:05 iex) | +23.2% | 183.37 | 215.98 / 214.67-226.50 | 7.21 (3.9%) | 172.11-197.63 | -0.2% / +3.3% | -0.1% | 5.3M |
| TDAY | 7.17 (10:04 iex) | +14.0% | 6.29 | 6.57 / 6.54-7.21 | 0.22 (3.4%) | 6.18-6.73 | -1.6% / -10.4% | -1.6% | 2.1M |
| TJGC | 33.64 (09:49 sip) | +11.4% | 30.20 | 26.31 / 26.31-35.50 | 4.11 (13.6%) | 8.80-36.76 | +77.4% / +201.1% | +29.7% | 1.4M |
| SNPS | 490.00 (10:05 iex) | +12.7% | 434.94 | 467.57 / 462.00-492.53 | 14.96 (3.4%) | 362.55-445.92 | +8.2% / +7.9% | +5.3% | 2.0M |
| CTSH | 64.03 (10:05 iex) | +11.5% | 57.44 | 61.90 / 61.59-64.74 | 2.06 (3.6%) | 55.63-65.42 | -4.3% / -1.1% | -2.9% | 6.4M |
| CTVA | 12.34 (10:05 iex) | -84.1% | 77.65 | 14.44 / 12.40-14.44 | 2.28 (2.9%) | 76.50-90.87 | -5.6% / -5.1% | -3.4% | 4.8M |
| NKTR | 48.42 (10:04 iex) | -20.0% | 60.55 | 55.41 / 47.40-56.69 | 3.64 (6.0%) | 56.21-77.75 | -9.1% / -14.0% | +5.0% | 1.4M |
| LQDA | 25.11 (10:05 iex) | -17.0% | 30.26 | 23.96 / 22.31-26.55 | 6.22 (20.6%) | 29.86-74.74 | -54.5% / -59.3% | -55.2% | 2.3M |
