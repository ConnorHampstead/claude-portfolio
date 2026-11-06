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

Research is done. I'm writing the brief now: closing XLP, tightening the NVDA stop, and adding one resting SMH short.

# Pre-market brief: Friday 2026-11-06

### 1. Tape
On Thursday the AI selloff turned into a crash:
- The Nasdaq fell 5.52% into correction territory, its worst day since April 2025.
- The S&P fell 4.36% and the Dow 3.44%.
- NVDA lost about 9% and the VIX jumped 11.6 points.
- The trigger is worry that the Democratic midterm wins in states that host data centers will slow the AI build-out.

The Nikkei fell 6% overnight. This morning chips are bouncing: AMD +8.5%, AVGO +5.6% and SMH +5.3% to 471.4. LRCX is up about 11% on a $25B buyback.

October payrolls came in hot:
- +165K against about 60K expected, with +84K of upward revisions.
- Unemployment 4.1%, average hourly earnings +0.4% m/m.
- Coverage says this firms up expectations of a Fed **hike** in December.
- The 10-year is up about 4bp to 4.88%.
- S&P futures gave back part of their gain to +0.2%. Dow futures are −1%, Nasdaq +1.5%, VIX 26.4.

Money is going back out of the defensives it had sheltered in: XLP −2.0%, WMT −2.1%, HD −2.7%, XLV −1.6%.

The regime is high volatility with a broken trend in AI hardware. Today looks like a short-covering bounce after a capitulation day, with rates as a new headwind. **The edge is short, but on location: sell bounces into resistance, not at the open after a +5% gap.**

### 2. Calendar
| Event | ET | Stockholm | Actual / consensus | Touches |
|---|---|---|---|---|
| October payrolls | 08:30 | 14:30 | **+165K** vs ~60K; unemployment 4.1% vs 4.2%; AHE +0.4% m/m; +84K revisions. Yields up, Nasdaq futures pared gains slightly | Everything; rate-hike repricing hurts XLP and defensives |
| Moderna, Humana, Oklo earnings | pre-mkt | pre-mkt | MRNA +10% on a beat and raise | None |
| UMich sentiment (prelim) | 10:00 | 16:00 | Not yet released; I could not verify the consensus | Seen by the review |
| Weekend | — | — | The harness cancels resting entries before the weekend | CAT, SMH |

### 3. Open positions and resting entries
- **NVDA short** (entry 194.96, last 189.20, +4.2% pre-market; stop 204.50, target 178). **Thesis intact.** Thursday's −9% confirmed the breakdown, and today's bounce is short-covering. I am tightening the stop to **201.50**, just above the old 200.92 20-day low that broke. If NVDA gets back above that level, the breakdown has failed. The stop is 1.6 ATR above last. Target unchanged.
- **XLP long** (entry 89.90, last 89.41; stop 91.20 sits *above* the market). The resting stop will fire at the open. The thesis is also being **invalidated** today: money is leaving defensives, not arriving, and a hot payroll print with hike talk works against staples. I am **closing at market** rather than widening the stop to stay in a trade whose premise has reversed. The loss is about −0.5R, below the original 88.80 stop risk.
- **CAT short, resting limit at 605** (last 572.11). It needs a 6% rally to fill, and the harness clears it before the weekend anyway. **Keep it** for today in case industrials squeeze.

### 4. New plays

**SMH short: sell the bounce at resistance**

| Field | Value |
|---|---|
| Ticker | SMH |
| Direction | Short |
| Catalyst | Bounce of +5.3% pre-market on 2026-11-06 after a −20% week; hot payrolls bring December hike risk on top of data-center policy risk |
| Thesis | Rallies after a capitulation day usually stall under the breakdown zone. 485–490 is Thursday morning's pre-market level and the gap area under the 504.27 close from 11-04. I am selling a test of it, not the open. |
| Entry | 488.00 limit (last 471.43) |
| Stop | 509.00, above the 504.27 close from 11-04. Reclaiming that level means the crash is being fully retraced. |
| Target | 450.00, just above the 445.59 20-day low (1.8R) |
| Risk tier | 0.5: same trade family as the NVDA short, ATR 5.3%, VIX 26 |
| Time horizon | 1–4 days |
| Conviction | 3 |
| P(target before stop) | 38% (conditional on a fill) |
| Invalidation | SMH closes above 500 with breadth across memory and equipment names, or data-center policy fears are walked back |
| What I'd be wrong about | V-shaped recoveries after a −5% Nasdaq day are common (April 2025). LRCX's buyback and the MU strength may mean dip buyers are in charge, and a hold above 488 could squeeze to 510. |

The limit fills only if the bounce runs another 3.5% today or in a later session. That is the point: I don't want to short at 471 into a squeeze. The entry is cancelled before the weekend, so this is effectively a test of today's high.

### 5. Both sides
- **Best short:** SMH limit 488 / stop 509 / target 450, P 38%. **Taken** (section 4).
- **Best long:** AMZN, the strongest megacap (+6.7% over 5 days, 261.93, 20-day high 273.23). A buy stop at 274.00, stop 261.00, target 296.00, P 33%. **Passed**: it is still an AI-capex name, and with a hike being priced, a breakout through 274 this week is unlikely.
- **ABNB long** on its beat and raise (+13% pre-market). I could not verify a price, so **excluded**.

### 6. Passing on
- **AMD short on the bounce** (limit 465, stop 505, target 410, P 35%): its 8.9% ATR makes the stop very wide, and it duplicates SMH.
- **XHB short on the rate repricing** (market ~102.4, stop 106.50, target 96.00, P 35%): I can't see the rates read-through in homebuilder flows yet. It's a plausible probe, but I don't want a second new idea in a VIX-26 tape.
- **QQQ long on the bounce:** counter-trend chasing a gap, with no level.
- **AMZN breakout long:** above.

### 7. For the post-open review
- **SMH:** if SMH rallies through 488 in the opening range and holds above 495 at 10:05, the limit has filled into strength. Close it if it is above 500. If the opening range fades below 465, leave the limit resting.
- **NVDA:** if NVDA trades above 198 by 10:05 with SMH above 485, cover at market rather than wait for the 201.50 stop.
- **UMich at 10:00:** a jump in inflation expectations makes the hike case stronger, so keep the shorts as they are. No action on longs.
- **XLP:** confirm the exit filled.

### 8. Book state
With XLP closed and SMH filled: NVDA short about $10.2K and SMH short about $12K, plus CAT resting at about $7K. Gross is about 29% (cap 150%) and net about −29% (cap ±100%). Tech net short is about −22%, inside the 40% sector cap. Risk at stake: NVDA about 0.34%, SMH 0.5% and CAT 0.25%, about 1.1% in total (cap 4%).

Sources: [Yahoo Finance live](https://finance.yahoo.com/markets/live/stock-market-today-friday-november-6-dow-sp-500-nasdaq-jobs-report-091927729.html), [CNBC Morning Squawk](https://www.cnbc.com/2026/11/06/morning-squawk-blue-wave-stocks.html), [CNBC premarket movers](https://www.cnbc.com/2026/11/06/stocks-making-the-biggest-moves-premarket-moderna-airbnb-cloudflare-affirm-more.html), [TipRanks](https://www.tipranks.com/news/stock-market-today-nov-6-futures-mixed-as-nasdaq-futures-rebound-after-tech-selloff), [Yahoo chips rebound](https://finance.yahoo.com/technology/articles/u-chip-stocks-rebound-sharply-105433545.html), [Reuters via Investing.com](https://www.investing.com/news/stock-market-news/sp-500-futures-pare-gains-after-october-nonfarm-payrolls-data-5008177)

```json
{
  "date": "2026-11-06",
  "no_trade": false,
  "session_note": "Post-crash short-covering bounce in AI hardware plus a hot payroll print (+165K) bringing a December hike into view; closing the XLP long as the defensive rotation reverses, tightening the NVDA short, and placing a resting short on SMH at bounce resistance.",
  "plays": [
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "limit",
      "entry": 488.00,
      "stop": 509.00,
      "targets": [450.00],
      "time_horizon": "1-4 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "+5.3% pre-market bounce on 2026-11-06 after Nasdaq's -5.5% day; hot October payrolls raise December hike odds on top of data-center policy risk.",
      "thesis": "Rallies after a capitulation day usually stall beneath the breakdown zone; 485-490 is Thursday's pre-market level and below the 504.27 close from 11-04. Selling a test of it rather than the gap.",
      "invalidation": "SMH closes above 500 on broad semis strength, or data-center policy fears are walked back.",
      "bear_case": "V-shaped recoveries after a -5% Nasdaq day are common; LRCX's buyback and MU strength may mean dip buyers are in charge."
    }
  ],
  "manage": [
    {
      "ticker": "XLP",
      "action": "close",
      "reason": "Pre-market is 89.41, below the 91.20 stop, and the defensive-rotation thesis is reversing on the hot payrolls and the tech bounce; exit rather than widen."
    },
    {
      "ticker": "NVDA",
      "action": "update",
      "stop": 201.50,
      "reason": "Tightening to just above the broken 200.92 20-day low; reclaiming it means the breakdown failed."
    }
  ],
  "passed": [
    {
      "ticker": "AMZN",
      "direction": "long",
      "entry_type": "stop",
      "entry": 274.00,
      "stop": 261.00,
      "targets": [296.00],
      "p_target_first": 0.33,
      "reason": "Best long on relative strength, but it is still AI-capex exposed and a hike is being priced; a breakout is unlikely this week."
    },
    {
      "ticker": "AMD",
      "direction": "short",
      "entry_type": "limit",
      "entry": 465.00,
      "stop": 505.00,
      "targets": [410.00],
      "p_target_first": 0.35,
      "reason": "Bounce-short candidate, but the 8.9% ATR makes the stop very wide and it duplicates SMH."
    },
    {
      "ticker": "XHB",
      "direction": "short",
      "entry_type": "market",
      "entry": 102.44,
      "stop": 106.50,
      "targets": [96.00],
      "p_target_first": 0.35,
      "reason": "Rate-repricing short on the hot payrolls; read-through not yet confirmed and I don't want a second new idea at VIX 26."
    }
  ]
}
```

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Friday 2026-11-06. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,106.89**
- Cash: $112,517.58
- Session P&L so far: -1.18% (new entries are blocked at -3.0%)
- Gross exposure: $29,383 (29% of equity, cap 150%)
- Net exposure: $-29,383 (-29%, cap +/-100%)
- Risk at stake (entry to stop): $1,109 (1.09% of equity, cap 4.0%) — 2.91% left for new plays
- Slots: 1 open + 2 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| NVDA | short | 54 | 194.96 | 192.79 | +117 (+1.1%) | 201.50 | 178.00 | The largest AI-capex position has lost its 20-day range while semis sell off even on good news. The path of least resist |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| SMH | short | 24 | 488.00 | limit | 509.00 | 450.00 | 2026-11-06 |
| CAT | short | 12 | 605.00 | limit | 626.00 | 565.00 | 2026-11-04 |

### Record

44 closed trades: 14W / 30L, total -0.32R, net $+2,003 realized. Shorts taken: 36.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |
| KRE | long | stop | -0.04R | $-10 | 37% |
| SMH | short | target | +1.72R | $+873 | 34% |
| GOOGL | short | stop | -1.00R | $-522 | 30% |

### Ideas you passed on, replayed against the tape

99 resolved: 31 reached target first, 42 stop first, 19 never reached the entry, 7 expired, 0 ambiguous. Average +0.10R across the 80 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-30 pre-market | LLY | long | Chasing +2.9% above the 20d high; defensive exposure already taken via XLP. | stop | -1.21R | 36% |
| 2026-11-04 open | XLF | long | Breakout above the 57.70 20d high, but stacks with KRE near the 40% financials s | stop | -1.19R | 38% |
| 2026-10-27 pre-market | META | short | A third AI short into an AI-financing relief bid, with MSFT/GOOGL read-through W | target | +1.39R | 33% |
| 2026-11-05 pre-market | AMD | short | Below its 20d low, but the 6.6% ATR makes the stop wide and it doubles the semis | target | +1.40R | 33% |
| 2026-11-04 pre-market | NVDA | short | Best short: breakdown below the 200.92 20d low on data-center policy risk, but n | target | +2.02R | 36% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| NVDA | 192.99 (10:05 iex) | +6.3% | 181.60 | 191.10 / 187.00-194.89 | 7.46 (4.1%) | 181.46-233.92 | -15.0% / -17.7% | -15.0% | 113.4M |
| SMH | 470.14 (10:05 iex) | +5.0% | 447.73 | 473.41 / 464.77-476.05 | 23.94 (5.3%) | 445.59-615.54 | -17.7% / -21.1% | -20.3% | 11.0M |
| CAT | 565.40 (10:05 iex) | +2.1% | 553.64 | 571.82 / 555.77-572.00 | 30.84 (5.6%) | 550.81-810.07 | -20.5% / -27.5% | -14.5% | 3.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 739.14 (10:05 iex) | +0.8% | 733.00 | 734.82 / 734.58-742.11 | 10.97 (1.5%) | 732.71-779.42 | -4.2% / -4.3% | -4.7% | 45.2M |
| QQQ | 660.94 (10:05 iex) | +2.1% | 647.05 | 658.37 / 655.17-664.28 | 16.42 (2.5%) | 647.05-752.87 | -9.2% / -10.4% | -9.5% | 47.3M |
| IWM | 271.84 (10:05 iex) | +0.3% | 270.98 | 271.98 / 270.23-272.71 | 4.58 (1.7%) | 269.88-286.17 | -2.2% / -4.1% | -4.6% | 25.1M |
| DIA | 512.97 (10:05 iex) | -0.3% | 514.27 | 508.72 / 508.66-514.38 | 7.07 (1.4%) | 511.56-536.60 | -1.3% / -1.1% | -1.6% | 3.8M |
| TLT | 81.89 (10:05 iex) | -0.0% | 81.93 | 81.88 / 81.72-81.92 | 0.77 (0.9%) | 77.16-82.21 | +2.1% / +2.5% | +1.0% | 37.8M |
| GLD | 370.94 (10:05 iex) | -1.2% | 375.49 | 369.47 / 369.26-371.19 | 6.45 (1.7%) | 354.67-385.17 | +0.6% / -2.7% | +1.9% | 8.9M |
| USO | 148.32 (10:03 iex) | +0.1% | 148.21 | 148.35 / 146.76-148.76 | 6.00 (4.1%) | 142.96-171.82 | -6.8% / -2.4% | -11.9% | 5.3M |
| SMH | 470.14 (10:05 iex) | +5.0% | 447.73 | 473.41 / 464.77-476.05 | 23.94 (5.3%) | 445.59-615.54 | -17.7% / -21.1% | -20.3% | 11.0M |
| XLK | 166.52 (10:04 iex) | +2.5% | 162.38 | 166.96 / 165.47-168.10 | 5.45 (3.4%) | 162.14-199.41 | -12.3% / -14.0% | -14.0% | 11.4M |
| XLF | 57.21 (10:05 iex) | -0.5% | 57.50 | 56.73 / 56.63-57.48 | 0.96 (1.7%) | 54.02-60.04 | +2.5% / +2.9% | +1.0% | 35.6M |
| XLE | 62.00 (10:05 iex) | +0.6% | 61.63 | 61.38 / 61.20-62.30 | 1.82 (2.9%) | 61.63-70.15 | -8.4% / -5.1% | -10.3% | 35.6M |
| XLV | 184.09 (10:05 iex) | -0.4% | 184.91 | 181.42 / 181.14-185.00 | 3.60 (1.9%) | 167.52-192.32 | +3.1% / +6.9% | +0.5% | 10.9M |
| XLI | 163.04 (10:05 iex) | +0.4% | 162.47 | 162.62 / 161.74-163.54 | 3.20 (2.0%) | 162.04-172.40 | -3.2% / -4.2% | -4.5% | 8.7M |
| XLY | 117.83 (10:05 iex) | +0.2% | 117.64 | 116.78 / 116.50-118.11 | 2.45 (2.1%) | 110.67-122.92 | +2.3% / +3.9% | +1.2% | 8.9M |
| XLP | 89.98 (10:05 iex) | -1.4% | 91.25 | 89.00 / 88.87-90.08 | 1.66 (1.8%) | 82.96-93.40 | +4.0% / +7.7% | +3.5% | 18.1M |
| XLU | 43.02 (10:05 iex) | -0.6% | 43.30 | 42.77 / 42.63-43.05 | 0.63 (1.5%) | 40.97-44.09 | +1.9% / +3.9% | +0.4% | 27.2M |
| XLB | 52.01 (10:05 iex) | -0.6% | 52.33 | 51.69 / 51.55-52.11 | 0.92 (1.8%) | 49.16-54.63 | +1.7% / +2.9% | -0.4% | 11.8M |
| XLRE | 43.99 (10:04 iex) | -0.7% | 44.30 | 43.69 / 43.63-44.09 | 0.73 (1.7%) | 41.15-45.34 | +3.9% / +4.4% | +2.9% | 8.3M |
| XLC | 104.65 (10:05 iex) | +0.3% | 104.34 | 103.28 / 103.21-104.90 | 2.06 (2.0%) | 99.33-113.17 | -2.1% / -5.0% | +3.1% | 8.0M |
| KRE | 72.17 (10:05 iex) | -0.2% | 72.31 | 72.15 / 71.82-72.45 | 1.63 (2.3%) | 67.79-75.80 | +1.4% / +0.8% | -0.8% | 15.3M |
| XHB | 102.43 (10:04 iex) | -1.4% | 103.85 | 102.97 / 101.59-102.98 | 3.10 (3.0%) | 91.87-108.78 | +5.7% / +5.7% | +2.5% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 341.59 (10:05 iex) | -0.7% | 344.17 | 338.73 / 338.30-343.58 | 8.90 (2.6%) | 325.33-355.38 | +0.3% / +2.6% | -1.4% | 48.4M |
| MSFT | 529.79 (10:05 iex) | -1.1% | 535.93 | 525.69 / 524.47-532.44 | 15.42 (2.9%) | 504.96-559.15 | +0.8% / +3.8% | +1.1% | 25.4M |
| NVDA | 192.99 (10:05 iex) | +6.3% | 181.60 | 191.10 / 187.00-194.89 | 7.46 (4.1%) | 181.46-233.92 | -15.0% / -17.7% | -15.0% | 113.4M |
| AMZN | 262.55 (10:05 iex) | +0.9% | 260.21 | 259.81 / 258.53-263.55 | 10.34 (4.0%) | 229.36-273.23 | +2.3% / +2.5% | +6.7% | 48.0M |
| GOOGL | 288.08 (10:05 iex) | +1.9% | 282.57 | 284.91 / 284.61-290.49 | 11.16 (3.9%) | 276.92-359.40 | -11.9% / -15.4% | -0.4% | 38.2M |
| META | 617.67 (10:05 iex) | +2.1% | 605.08 | 608.00 / 606.66-622.19 | 23.47 (3.9%) | 583.80-771.27 | -9.4% / -10.2% | -3.1% | 25.0M |
| TSLA | 356.17 (10:05 iex) | +3.6% | 343.69 | 349.12 / 347.60-357.75 | 17.63 (5.1%) | 338.15-414.23 | -9.9% / -7.6% | -14.8% | 40.2M |
| AVGO | 302.34 (10:05 iex) | +3.7% | 291.53 | 311.13 / 301.31-311.52 | 14.40 (4.9%) | 290.12-366.63 | -13.1% / -16.5% | -15.5% | 23.1M |
| AMD | 452.27 (10:05 iex) | +11.8% | 404.40 | 444.43 / 433.93-459.63 | 35.90 (8.9%) | 402.10-627.37 | -24.4% / -26.1% | -28.6% | 26.0M |
| ORCL | 117.08 (10:05 iex) | +1.7% | 115.16 | 119.54 / 116.63-119.70 | 8.37 (7.3%) | 111.66-148.48 | -11.8% / -17.5% | -17.5% | 42.5M |
| NFLX | 63.97 (10:05 iex) | -2.4% | 65.56 | 63.80 / 63.46-64.27 | 2.15 (3.3%) | 61.39-73.07 | -1.5% / -8.1% | +5.7% | 46.2M |
| CRM | 213.65 (10:04 iex) | -3.9% | 222.41 | 216.71 / 212.99-218.77 | 9.12 (4.1%) | 214.67-252.42 | -6.1% / -7.4% | -3.7% | 7.3M |
| JPM | 338.06 (10:04 iex) | +0.2% | 337.34 | 333.15 / 333.00-339.34 | 7.81 (2.3%) | 326.40-359.80 | +0.1% / -1.2% | -1.8% | 7.4M |
| GS | 879.16 (10:04 iex) | +1.2% | 868.95 | 870.29 / 865.79-886.33 | 28.23 (3.2%) | 854.45-939.38 | -3.0% / -7.1% | -6.3% | 2.4M |
| BAC | 49.92 (10:05 iex) | +0.3% | 49.76 | 49.54 / 49.27-50.16 | 1.24 (2.5%) | 49.17-54.93 | -2.9% / -10.2% | -2.7% | 44.1M |
| XOM | 166.26 (10:05 iex) | +0.6% | 165.30 | 164.25 / 163.51-166.72 | 5.11 (3.1%) | 165.14-188.50 | -6.9% / -2.0% | -9.8% | 13.4M |
| CVX | 213.75 (10:04 iex) | +0.4% | 212.93 | 211.53 / 210.43-214.10 | 5.58 (2.6%) | 210.71-236.48 | -5.1% / -0.8% | -8.0% | 8.1M |
| LLY | 1,365.00 (10:05 iex) | +0.0% | 1,364.73 | 1,350.45 / 1,333.22-1,376.70 | 51.14 (3.7%) | 1,151.67-1,453.00 | +5.5% / +12.7% | -0.7% | 2.8M |
| UNH | 394.80 (10:05 iex) | -0.2% | 395.72 | 388.11 / 388.00-396.63 | 12.00 (3.0%) | 372.80-426.55 | -2.1% / +1.4% | -3.7% | 6.2M |
| JNJ | 270.76 (10:05 iex) | -0.6% | 272.32 | 267.56 / 265.55-271.40 | 7.37 (2.7%) | 245.17-282.01 | +3.2% / +2.5% | -1.0% | 8.0M |
| WMT | 124.98 (10:05 iex) | -2.1% | 127.72 | 124.15 / 123.03-125.54 | 2.98 (2.3%) | 109.93-131.82 | +6.5% / +14.0% | +5.3% | 21.9M |
| COST | 1,055.75 (10:05 iex) | -0.9% | 1,065.59 | 1,045.55 / 1,043.00-1,057.49 | 20.07 (1.9%) | 941.14-1,081.55 | +6.8% / +12.3% | +7.1% | 2.4M |
| HD | 341.49 (10:05 iex) | -2.4% | 349.94 | 341.00 / 338.12-343.00 | 9.64 (2.8%) | 288.51-362.44 | +9.9% / +13.3% | +6.4% | 4.8M |
| CAT | 565.40 (10:05 iex) | +2.1% | 553.64 | 571.82 / 555.77-572.00 | 30.84 (5.6%) | 550.81-810.07 | -20.5% / -27.5% | -14.5% | 3.7M |
| BA | 172.50 (10:05 iex) | +0.0% | 172.50 | 172.00 / 169.88-173.25 | 6.27 (3.6%) | 165.01-193.28 | -5.4% / -10.7% | -0.1% | 10.1M |
| DAL | 86.55 (10:05 iex) | +1.4% | 85.36 | 86.00 / 85.70-87.27 | 3.54 (4.1%) | 74.14-89.92 | +6.7% / +6.0% | +4.6% | 7.0M |
| UAL | 111.97 (10:04 iex) | +1.3% | 110.49 | 111.38 / 111.28-113.45 | 5.80 (5.3%) | 94.54-117.01 | +6.9% / +3.0% | +5.0% | 5.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-11-06 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| FROG | 98.49 (10:05 iex) | +32.0% | 74.62 | 94.99 / 89.32-98.76 | 6.81 (9.1%) | 73.97-103.40 | -20.4% / -20.2% | -24.5% | 2.1M |
| IREZ | 20.83 (09:59 iex) | -38.4% | 33.81 | 21.72 / 17.65-25.57 | 4.55 (13.5%) | 11.67-35.88 | +69.3% / +145.0% | +74.1% | 1.6M |
| DKNG | 16.95 (10:05 iex) | -27.9% | 23.52 | 17.24 / 16.60-17.84 | 0.96 (4.1%) | 18.35-23.89 | +13.9% / +8.8% | +13.5% | 12.3M |
| AEHL | 13.25 (10:04 iex) | -24.0% | 17.44 | 10.46 / 10.46-15.51 | 1.85 (10.6%) | 6.17-30.60 | +93.3% / +103.3% | +124.2% | 2.4M |
| STLN | 5.09 (10:05 iex) | -24.0% | 6.70 | 6.07 / 4.82-6.43 | 0.36 (5.4%) | 6.18-7.04 | +1.1% / +3.3% | +0.8% | 1.3M |
| DAMD | 12.62 (10:05 iex) | -24.0% | 16.61 | 13.28 / 12.01-14.10 | 1.57 (9.4%) | 8.39-16.68 | +49.1% / +43.5% | +71.8% | 3.5M |
| FIVN | 27.46 (10:05 iex) | -19.6% | 34.14 | 26.31 / 25.12-28.02 | 2.03 (5.9%) | 31.91-38.68 | -4.1% / -1.5% | -8.7% | 1.5M |
| NBIZ | 45.09 (10:04 iex) | -18.9% | 55.61 | 45.99 / 40.48-48.00 | 7.14 (12.8%) | 21.64-59.83 | +57.7% / +96.3% | +76.7% | 1.3M |
| OMDA | 15.40 (10:03 iex) | -18.7% | 18.95 | 16.01 / 15.22-16.28 | 0.94 (5.0%) | 17.48-22.00 | -0.7% / -6.8% | -3.6% | 1.1M |
