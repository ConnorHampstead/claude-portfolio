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

I've finished the research (NVDA CEO probe, oil, CPI tomorrow, this week's earnings) and am writing the brief now.

# Pre-market brief — Monday 2026-11-09 (09:05 ET / 15:05 Stockholm)

### 1. Tape
Futures are bouncing after last week's tech-led rout. SPY is +0.9% at 742.20, QQQ +0.9% at 662.05 and IWM +1.5%. Asia rallied hard overnight: Taiwan +5% after its worst week in two decades. NVDA is the exception at **−5.9% (175.64)**. Nvidia's board has opened an investigation into Jensen Huang after he admitted a relationship with a woman reported to be a suspected Chinese intelligence operative (Bloomberg, CNBC). Oil is falling again: Brent is near $95–97 after a 17% weekly drop, because Trump called further Iran strikes "highly unlikely", although attacks on shipping in Hormuz are continuing. USO is −3.7% and XLE sits at its 20-day low. The 10-year is at 4.84% and the dollar index is 101.8 (−0.4%). Kitco reports that futures price roughly an 80% chance of a December **hike**, which is the macro force behind the AI/tech derating. Last week's selloff was also blamed on Democratic midterm wins raising AI and data-centre regulation fears. The regime is a relief bounce inside a downtrend in tech and semis, with rotation into cyclicals, airlines and defensives. **The edge for the 1–5 day horizon is short tech on a failed bounce; today's open favours longs, so I'm expressing shorts as breakdown triggers rather than selling into the bounce.**

### 2. Calendar
| Event | ET | Stockholm | Status / consensus | Touches |
|---|---|---|---|---|
| No tier-1 US data today | – | – | – | – |
| NVDA board probe headlines | ongoing | ongoing | Released overnight; NVDA −5.9% pre-market | NVDA short |
| **Oct CPI** | Tue 11-10 08:30 | 14:30 | Headline ~+0.3% m/m, core ~+0.2% m/m (previously 0.6% / 0.3%). One preview calls it "likely hot". Not fully verified | QQQ, AMZN, AVGO, all |
| CoreWeave Q3 | Tue 11-10 after close | ~22:05 | Revenue ~$3.54B expected | AVGO, QQQ (AI capex read-through) |
| Cisco, Applied Materials | Thu 11-12 after close | – | CSCO EPS ~$1.32; AMAT EPS ~$4.06 | AVGO, QQQ |
| PPI (Oct) | Fri 11-13 08:30 | 14:30 | – | all |

None of these is the company's own binary event for any name I hold or propose under rule 8.

### 3. Open positions
- **NVDA short (194.96, stop 201.50, target 178.00): intact and paid.** Pre-market is 175.64, below the target. The buy-to-cover limit at 178 should fill at or near the open, for about +2.6–3.0R. I'm letting it take the target rather than trailing. The catalyst is a governance headline that can be bought on any reassuring statement from the board, and the stock is already 3.2% below its 20-day low after a −8.8% week. Banking a 3R gap is the disciplined choice. **No manage entry**, because the existing bracket does the job.
- **AVGO short (302.03, stop 316.00, target 281.00): intact but being tested.** Pre-market is +3.1% at 302.77, in line with the semis bounce. It is still 11.6% below its 20-day average and its earnings are not until December. The stop sits about 1 ATR above, over Friday's bounce area. Hold and leave the levels unchanged.
- No resting entries.

### 4. New plays

**A. QQQ short — breakdown trigger**
| Field | Value |
|---|---|
| Ticker | QQQ |
| Direction | Short |
| Catalyst | Monday relief bounce into Tue 11-10 CPI with ~80% Dec-hike pricing; CRWV Tue after close, AMAT/CSCO Thu |
| Thesis | The bounce is a gap in a tape where rate-hike pricing and AI-regulation fear are derating tech (QQQ −7.3% vs 20d avg). If the bounce fails and QQQ loses the 647.05 20-day low, the move is continuation toward the next leg down. |
| Entry | Sell stop 646.50 (pre-market 662.05, so the trigger is well beyond the market) |
| Stop | 664.00: above today's pre-market bounce high area, about 1.05 ATR (2.7%) above entry. If QQQ breaks down and then reclaims 664, the breakdown failed. |
| Target | 615.00 (+1.8R) |
| Risk tier | 0.5: a breakdown trigger in a bouncing tape, with CPI binary-like macro risk overnight |
| Time horizon | 1–5 days |
| Conviction | 3 |
| P(target before stop) | 38% |
| Invalidation | A cool CPI (core ≤0.2%) with QQQ closing back above 680 |
| What I'd be wrong about | Positioning is already washed out after a week this ugly. A trigger at the 20-day low is exactly where short-covering bounces start, and a cool CPI could squeeze it violently. |

**B. AMZN long — relative-strength breakout (probe)**
| Field | Value |
|---|---|
| Ticker | AMZN |
| Direction | Long |
| Catalyst | Leading megacap through last week's crash (+7.9% 5d, above its 20/50d averages); pre-market +3.3% at 267.73, nearing the 273.23 20-day high |
| Thesis | AMZN is the one megacap the market is paying for while chips are liquidated. A break of the 20-day high in this tape shows rotation within tech toward cloud and retail, away from chip capex. |
| Entry | Buy stop 274.00 |
| Stop | 263.50: about 1.1 ATR below; back inside the range means the breakout failed |
| Target | 293.00 (+1.8R) |
| Risk tier | 0.25: a long against a tech downtrend, with CPI tomorrow |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 36% |
| Invalidation | A broad tech breakdown (the QQQ trigger firing) at the same time |
| What I'd be wrong about | In a hike-pricing tape the last leader often gets sold last, and that is a flaw in the thesis, not a strength. |

**C. DAL long — oil-collapse beneficiary, pullback entry (probe)**
| Field | Value |
|---|---|
| Ticker | DAL |
| Direction | Long |
| Catalyst | Brent −17% last week and lower again today on Iran de-escalation; DAL gapping +4.4% to 91.07, above its 89.92 20-day high |
| Thesis | Falling jet fuel is a direct earnings tailwind. I'd buy a retest of the breakout level rather than chase the gap. |
| Entry | Limit 89.50 |
| Stop | 85.80: about 1 ATR below, back into the prior range under the 5-day breakout base |
| Target | 96.50 (+1.9R) |
| Risk tier | 0.25: the catalyst is a geopolitical headline, and Hormuz shipping attacks continue |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 37% |
| Invalidation | Brent back above $100 |
| What I'd be wrong about | It is a one-headline trade. A single tanker strike reverses oil, and with it the whole airline complex. |

### 5. Both sides
- **Best short:** QQQ breakdown, sell stop 646.50 / stop 664 / target 615, P 38%. Taken (play A).
- **Best long:** AMZN breakout, buy stop 274 / stop 263.50 / target 293, P 36%. Taken as a probe (play B).

### 6. Passing on
- **XLE short** (sell stop 60.90 / stop 62.90 / target 57.50, P 33%): the direction is right, but it comes after a −12% week, and live Hormuz attacks make a squeeze likely. Logged in `passed`.
- **UAL long** (limit 115.50 / stop 110.00 / target 126.00, P 35%): the same thesis as DAL with a wider ATR (5.2%). One airline is enough. Logged in `passed`.
- **SMH short** (sell stop 444.00 / stop 470.00 / target 400.00, P 35%): it would stack on AVGO plus QQQ in semis. Logged in `passed`.
- **New NVDA short:** not possible while the current short is open, and the move is already gapped out.
- **CAT short:** bouncing +2.3% after an 18% collapse below its 20-day average, so the location is bad.

### 7. For the post-open review
- **NVDA:** confirm the 178 cover filled. If NVDA opened above 178, which is unlikely, hold the bracket.
- **AVGO:** if it holds above 310 at 10:00 with SMH green, tighten the stop to 312. If it is fading below 293.69, the prior close, hold.
- **QQQ:** if the bounce has fully faded and QQQ is below 655 by 10:00, the 646.50 trigger stays. If QQQ is above 670, keep it anyway, since the trigger is only live on a breakdown.
- **DAL:** if it opens below 89.50 and trades under 88, the limit will have filled low. Close it if it is below 87.50.

### 8. Book state
If every order fills, with NVDA closed: gross is about AVGO 5.4k + QQQ ~30k + AMZN ~8k + DAL ~7k, roughly 49%, against the 150% cap. Net is about −20%, against ±100%. Risk at stake is about 0.25% (AVGO) + 0.5% + 0.25% + 0.25% ≈ 1.25%, against the 4% cap. That is 4 slots of 8.

Sources: [Bloomberg – NVDA probe](https://www.bloomberg.com/news/articles/2026-11-09/nvidia-shares-dip-on-robinhood-as-huang-affair-spurs-board-probe), [CNBC – NVDA](https://www.cnbc.com/2026/11/09/nvidia-jensen-huang-chinese-spy-investigation.html), [TipRanks – Nov 9](https://www.tipranks.com/news/stock-market-today-nov-9-nvidia-stock-falls-on-probe-into-ceo-huang-focus-on-inflation-data-ai-earnings), [Kitco/Reuters](https://www.kitco.com/news/off-the-wire/2026-11-09/stocks-find-firmer-ground-nvidia-woes-pose-fresh-test-oil-falls), [CNBC – oil](https://www.cnbc.com/2026/11/09/oil-falls-as-trump-says-new-iran-attacks-unlikely.html), [CPI calendar](https://cpichart.com/cpi-release-calendar/), [CoreWeave Nov 10](https://tech-insider.org/coreweave-earnings-nov-10-nebius-adobe-max-big-tech-week-2026/), [TipRanks earnings week](https://www.tipranks.com/news/major-earnings-this-week-nov-9-13-2026), [Benzinga – AVGO](https://www.benzinga.com/markets/tech/26/11/62770428/whats-going-on-with-broadcom-stock-monday-10)

```json
{
  "date": "2026-11-09",
  "no_trade": false,
  "session_note": "Relief bounce inside a rate-hike-driven tech downtrend; NVDA short covers at target on CEO-probe gap; shorts via QQQ breakdown trigger, small rotation longs in AMZN and DAL.",
  "plays": [
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "stop",
      "entry": 646.50,
      "stop": 664.00,
      "targets": [615.00],
      "time_horizon": "1-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "Failed Monday bounce into Tue 11-10 CPI with ~80% Dec-hike pricing; CRWV Tue, AMAT/CSCO Thu.",
      "thesis": "Tech is being derated by hike pricing and AI-regulation fears. Losing the 647.05 20-day low after a gap bounce means the bounce failed and the downtrend continues.",
      "invalidation": "Cool CPI (core <=0.2%) with QQQ closing back above 680.",
      "bear_case": "Washed-out positioning; breaking the 20d low is where short-covering bounces start, and a cool CPI could squeeze it."
    },
    {
      "ticker": "AMZN",
      "direction": "long",
      "entry_type": "stop",
      "entry": 274.00,
      "stop": 263.50,
      "targets": [293.00],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.36,
      "catalyst": "Relative-strength leader (+7.9% 5d) gapping +3.3% toward the 273.23 20-day high on 2026-11-09.",
      "thesis": "Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong relative signal.",
      "invalidation": "QQQ breaking its 20-day low while AMZN falls back inside the range.",
      "bear_case": "The last leader is often sold last in a rate-driven derating."
    },
    {
      "ticker": "DAL",
      "direction": "long",
      "entry_type": "limit",
      "entry": 89.50,
      "stop": 85.80,
      "targets": [96.50],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.37,
      "catalyst": "Brent -17% last week and lower again 2026-11-09 after Trump called new Iran strikes highly unlikely.",
      "thesis": "Falling jet fuel is a direct margin tailwind. Buy the retest of the 89.92 20-day-high breakout rather than chase the gap.",
      "invalidation": "Brent back above $100.",
      "bear_case": "A single-headline catalyst; one Hormuz tanker strike reverses oil and the airline trade."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "XLE",
      "direction": "short",
      "entry_type": "stop",
      "entry": 60.90,
      "stop": 62.90,
      "targets": [57.50],
      "p_target_first": 0.33,
      "reason": "Right direction, but -12% in 5 days with live Hormuz attacks makes a squeeze likely."
    },
    {
      "ticker": "UAL",
      "direction": "long",
      "entry_type": "limit",
      "entry": 115.50,
      "stop": 110.00,
      "targets": [126.00],
      "p_target_first": 0.35,
      "reason": "Same thesis as DAL with a wider ATR; one airline is enough."
    },
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "stop",
      "entry": 444.00,
      "stop": 470.00,
      "targets": [400.00],
      "p_target_first": 0.35,
      "reason": "Would stack semis exposure on top of the AVGO and QQQ shorts."
    }
  ]
}
```

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Monday 2026-11-09. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,799.98**
- Cash: $101,954.85
- Session P&L so far: +0.21% (new entries are blocked at -3.0%)
- Gross exposure: $37,127 (36% of equity, cap 150%)
- Net exposure: $-11,727 (-11%, cap +/-100%)
- Risk at stake (entry to stop): $1,269 (1.23% of equity, cap 4.0%) — 2.77% left for new plays
- Slots: 2 open + 2 resting entries of 8 — you may add at most 4 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMZN | long | 24 | 274.10 | 271.85 | -54 (-0.8%) | 263.50 | 293.00 | Money is rotating within tech toward AMZN and away from chip capex. A 20-day-high breakout in this tape is a strong rela |
| AVGO | short | 18 | 302.03 | 315.48 | -242 (-4.5%) | 316.00 | 281.00 | A megacap chip fading from its opening print shows supply meeting the post-crash bounce; continuation retests the 290.12 |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| DAL | long | 69 | 89.50 | limit | 85.80 | 96.50 | 2026-11-09 |
| QQQ | short | 29 | 646.50 | stop | 664.00 | 615.00 | 2026-11-09 |

### Record

45 closed trades: 15W / 30L, total +1.83R, net $+3,111 realized. Shorts taken: 38.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| NVDA | short | target | +2.15R | $+1,108 | 37% |
| XLP | long | close | -0.49R | $-251 | 38% |
| XLV | long | stop | -0.82R | $-422 | 40% |
| KRE | long | stop | -0.04R | $-10 | 37% |
| SMH | short | target | +1.72R | $+873 | 34% |

### Ideas you passed on, replayed against the tape

100 resolved: 31 reached target first, 42 stop first, 20 never reached the entry, 7 expired, 0 ambiguous. Average +0.10R across the 80 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-11-02 pre-market | UAL | long | Chasing a +4.6% gap whose catalyst is a single Iran headline that can reverse ov | never filled | - | 40% |
| 2026-10-30 pre-market | LLY | long | Chasing +2.9% above the 20d high; defensive exposure already taken via XLP. | stop | -1.21R | 36% |
| 2026-11-04 open | XLF | long | Breakout above the 57.70 20d high, but stacks with KRE near the 40% financials s | stop | -1.19R | 38% |
| 2026-10-27 pre-market | META | short | A third AI short into an AI-financing relief bid, with MSFT/GOOGL read-through W | target | +1.39R | 33% |
| 2026-11-05 pre-market | AMD | short | Below its 20d low, but the 6.6% ATR makes the stop wide and it doubles the semis | target | +1.40R | 33% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AMZN | 271.79 (10:05 iex) | +4.8% | 259.30 | 269.50 / 269.32-275.34 | 9.76 (3.8%) | 229.36-273.23 | +2.0% / +2.1% | +7.9% | 48.5M |
| AVGO | 315.44 (10:05 iex) | +7.4% | 293.69 | 305.00 / 304.29-315.66 | 15.14 (5.2%) | 289.77-360.69 | -11.6% / -15.5% | -9.9% | 23.9M |
| DAL | 91.25 (10:04 iex) | +4.6% | 87.20 | 90.36 / 90.08-91.70 | 3.54 (4.1%) | 74.14-89.92 | +8.6% / +8.1% | +8.8% | 6.7M |
| QQQ | 672.65 (10:05 iex) | +2.5% | 656.10 | 662.63 / 662.02-673.64 | 16.61 (2.5%) | 647.05-749.79 | -7.3% / -9.0% | -5.0% | 49.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 748.50 (10:05 iex) | +1.8% | 735.29 | 741.95 / 741.02-748.48 | 11.12 (1.5%) | 732.71-779.40 | -3.7% / -3.9% | -2.7% | 47.1M |
| QQQ | 672.65 (10:05 iex) | +2.5% | 656.10 | 662.63 / 662.02-673.64 | 16.61 (2.5%) | 647.05-749.79 | -7.3% / -9.0% | -5.0% | 49.9M |
| IWM | 279.33 (10:05 iex) | +2.1% | 273.67 | 277.47 / 276.81-279.33 | 4.73 (1.7%) | 269.88-286.17 | -1.1% / -2.9% | -2.0% | 25.5M |
| DIA | 520.27 (10:05 iex) | +1.6% | 512.22 | 518.58 / 517.24-520.39 | 7.40 (1.4%) | 508.66-536.60 | -1.7% / -1.5% | -0.9% | 3.9M |
| TLT | 82.09 (10:04 iex) | +0.2% | 81.92 | 82.26 / 82.05-82.28 | 0.77 (0.9%) | 77.41-82.42 | +1.8% / +2.5% | +0.5% | 38.3M |
| GLD | 377.09 (10:05 iex) | +1.2% | 372.52 | 378.20 / 376.90-378.47 | 6.68 (1.8%) | 354.67-384.88 | -0.1% / -3.2% | +4.7% | 8.9M |
| USO | 143.63 (10:02 iex) | -3.2% | 148.41 | 142.57 / 142.34-143.92 | 5.90 (4.0%) | 142.96-171.82 | -6.7% / -2.5% | -12.1% | 5.3M |
| SMH | 477.61 (10:05 iex) | +2.9% | 463.96 | 464.96 / 462.88-480.57 | 24.64 (5.3%) | 445.59-598.45 | -13.6% / -18.0% | -11.2% | 11.6M |
| XLK | 168.62 (10:05 iex) | +2.4% | 164.74 | 165.58 / 165.30-168.99 | 5.53 (3.4%) | 162.14-198.18 | -10.2% / -12.5% | -8.2% | 12.1M |
| XLF | 57.73 (10:05 iex) | +1.0% | 57.16 | 57.73 / 57.26-57.75 | 1.00 (1.7%) | 54.02-60.04 | +1.7% / +2.3% | +1.2% | 35.6M |
| XLE | 61.70 (10:05 iex) | +0.1% | 61.62 | 61.25 / 60.85-61.80 | 1.84 (3.0%) | 61.20-70.15 | -8.2% / -5.1% | -12.0% | 36.3M |
| XLV | 186.71 (10:05 iex) | +1.0% | 184.80 | 186.42 / 185.36-186.72 | 3.79 (2.1%) | 169.48-192.32 | +2.7% / +6.7% | -0.0% | 11.4M |
| XLI | 167.50 (10:05 iex) | +3.0% | 162.67 | 165.90 / 165.05-167.51 | 3.21 (2.0%) | 161.74-172.40 | -2.9% / -3.9% | -2.8% | 8.9M |
| XLY | 121.17 (10:05 iex) | +3.1% | 117.58 | 119.69 / 119.69-121.48 | 2.46 (2.1%) | 110.67-122.92 | +2.0% / +3.8% | +1.9% | 9.1M |
| XLP | 90.19 (10:05 iex) | +0.1% | 90.08 | 90.05 / 89.80-90.34 | 1.78 (2.0%) | 83.39-93.40 | +2.3% / +6.1% | +0.7% | 19.0M |
| XLU | 43.52 (10:05 iex) | +0.9% | 43.13 | 43.65 / 43.15-43.68 | 0.62 (1.4%) | 41.09-44.09 | +1.3% / +3.5% | -0.7% | 27.8M |
| XLB | 52.85 (10:05 iex) | +1.7% | 51.95 | 52.78 / 52.48-52.85 | 0.96 (1.8%) | 49.16-54.63 | +0.7% / +2.1% | -1.5% | 12.2M |
| XLRE | 44.59 (10:05 iex) | +1.3% | 44.00 | 44.51 / 44.26-44.56 | 0.75 (1.7%) | 41.31-45.34 | +2.9% / +3.7% | +1.9% | 8.4M |
| XLC | 107.06 (10:05 iex) | +2.2% | 104.79 | 106.25 / 106.22-107.47 | 2.16 (2.1%) | 99.33-113.17 | -1.5% / -4.5% | +4.9% | 8.1M |
| KRE | 73.44 (10:05 iex) | +1.7% | 72.20 | 73.25 / 72.98-73.50 | 1.64 (2.3%) | 67.79-75.80 | +1.0% / +0.7% | +0.3% | 15.0M |
| XHB | 105.20 (10:05 iex) | +2.8% | 102.29 | 104.05 / 103.82-105.33 | 3.15 (3.1%) | 91.87-108.78 | +3.7% / +4.1% | +1.3% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 348.96 (10:05 iex) | +1.9% | 342.37 | 345.00 / 344.78-350.34 | 9.02 (2.6%) | 325.33-355.38 | -0.3% / +1.9% | -0.7% | 48.9M |
| MSFT | 540.21 (10:05 iex) | +1.8% | 530.61 | 544.08 / 539.57-547.49 | 15.88 (3.0%) | 504.96-559.15 | -0.2% / +2.7% | +1.7% | 25.8M |
| NVDA | 177.97 (10:05 iex) | -4.6% | 186.64 | 172.99 / 170.24-178.85 | 8.02 (4.3%) | 181.46-228.86 | -11.8% / -15.1% | -8.8% | 118.4M |
| AMZN | 271.79 (10:05 iex) | +4.8% | 259.30 | 269.50 / 269.32-275.34 | 9.76 (3.8%) | 229.36-273.23 | +2.0% / +2.1% | +7.9% | 48.5M |
| GOOGL | 294.13 (10:05 iex) | +3.3% | 284.78 | 292.04 / 291.72-296.33 | 11.30 (4.0%) | 276.92-359.40 | -10.3% / -14.5% | +1.8% | 39.1M |
| META | 638.95 (10:04 iex) | +4.7% | 610.15 | 630.62 / 630.00-644.54 | 23.83 (3.9%) | 583.80-771.27 | -7.9% / -9.6% | -0.8% | 25.2M |
| TSLA | 376.08 (10:05 iex) | +5.0% | 358.22 | 360.19 / 360.02-378.88 | 17.99 (5.0%) | 338.15-414.23 | -5.8% / -3.7% | -10.4% | 40.1M |
| AVGO | 315.44 (10:05 iex) | +7.4% | 293.69 | 305.00 / 304.29-315.66 | 15.14 (5.2%) | 289.77-360.69 | -11.6% / -15.5% | -9.9% | 23.9M |
| AMD | 485.02 (10:05 iex) | +8.0% | 449.04 | 473.39 / 468.21-489.75 | 38.02 (8.5%) | 402.10-606.20 | -14.8% / -17.9% | -11.0% | 27.6M |
| ORCL | 118.30 (10:05 iex) | +1.9% | 116.10 | 117.03 / 114.91-119.20 | 8.89 (7.7%) | 109.21-148.48 | -10.2% / -16.4% | -11.2% | 43.6M |
| NFLX | 63.98 (10:05 iex) | +0.9% | 63.41 | 63.30 / 62.95-63.99 | 2.21 (3.5%) | 61.39-73.07 | -4.3% / -10.7% | +2.1% | 46.6M |
| CRM | 214.81 (10:03 iex) | +0.5% | 213.65 | 214.75 / 213.87-216.37 | 9.50 (4.4%) | 211.00-252.42 | -9.5% / -10.8% | -6.8% | 7.4M |
| JPM | 338.40 (10:05 iex) | +1.2% | 334.49 | 339.00 / 335.00-339.84 | 7.88 (2.4%) | 326.40-359.80 | -0.8% / -1.9% | -0.8% | 7.5M |
| GS | 899.57 (10:04 iex) | +3.9% | 865.82 | 885.08 / 878.62-900.30 | 28.69 (3.3%) | 854.45-939.38 | -3.1% / -7.1% | -3.2% | 2.4M |
| BAC | 50.28 (10:05 iex) | +1.8% | 49.42 | 50.05 / 49.73-50.36 | 1.23 (2.5%) | 49.17-54.93 | -3.1% / -10.5% | -1.2% | 44.5M |
| XOM | 164.79 (10:05 iex) | -0.6% | 165.87 | 163.81 / 162.84-165.55 | 5.20 (3.1%) | 163.51-188.50 | -6.5% / -1.7% | -11.4% | 13.8M |
| CVX | 211.06 (10:05 iex) | -0.7% | 212.61 | 210.85 / 209.68-212.25 | 5.74 (2.7%) | 210.43-236.48 | -5.2% / -1.1% | -9.7% | 8.2M |
| LLY | 1,395.00 (10:05 iex) | +3.0% | 1,354.00 | 1,365.40 / 1,364.58-1,396.16 | 52.81 (3.9%) | 1,158.40-1,453.00 | +4.0% / +11.5% | -4.5% | 3.0M |
| UNH | 394.73 (10:04 iex) | +0.1% | 394.15 | 397.71 / 394.24-398.50 | 11.98 (3.0%) | 372.80-426.55 | -2.6% / +1.0% | -3.2% | 6.1M |
| JNJ | 277.86 (10:05 iex) | +0.6% | 276.22 | 278.00 / 276.84-279.13 | 7.86 (2.8%) | 245.17-282.01 | +4.4% / +3.9% | +1.1% | 8.2M |
| WMT | 125.00 (10:05 iex) | -0.4% | 125.52 | 124.72 / 123.58-124.88 | 3.22 (2.6%) | 111.31-131.82 | +4.1% / +11.6% | +1.6% | 22.5M |
| COST | 1,051.79 (10:05 iex) | -0.2% | 1,053.56 | 1,048.55 / 1,045.73-1,053.71 | 20.80 (2.0%) | 945.30-1,081.55 | +5.0% / +10.8% | +4.1% | 2.4M |
| HD | 350.24 (10:05 iex) | +2.0% | 343.47 | 346.78 / 346.78-351.49 | 10.08 (2.9%) | 288.51-362.44 | +7.0% / +11.1% | +4.3% | 4.8M |
| CAT | 589.56 (10:05 iex) | +5.5% | 558.63 | 573.99 / 572.05-590.35 | 30.62 (5.5%) | 550.81-810.07 | -18.3% / -26.4% | -10.3% | 3.8M |
| BA | 175.30 (10:04 iex) | +1.1% | 173.40 | 177.39 / 174.00-177.39 | 6.32 (3.6%) | 165.01-193.28 | -4.4% / -9.9% | +1.1% | 10.1M |
| DAL | 91.25 (10:04 iex) | +4.6% | 87.20 | 90.36 / 90.08-91.70 | 3.54 (4.1%) | 74.14-89.92 | +8.6% / +8.1% | +8.8% | 6.7M |
| UAL | 119.92 (10:05 iex) | +6.4% | 112.74 | 117.92 / 117.50-120.75 | 5.82 (5.2%) | 94.54-117.01 | +8.8% / +5.0% | +8.2% | 5.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-11-09 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| GFR | 7.75 (10:02 iex) | +38.3% | 5.60 | 7.73 / 7.72-7.81 | 0.32 (5.8%) | 5.41-7.05 | -13.6% / -11.3% | -16.4% | 1.2M |
| BEX | 15.33 (10:05 iex) | +25.6% | 12.21 | 13.46 / 13.27-15.53 | 4.05 (33.2%) | 9.52-35.33 | -42.7% / -58.2% | -31.5% | 4.6M |
| COHX | 10.52 (10:00 iex) | +22.1% | 8.62 | 9.08 / 9.05-10.62 | 2.15 (24.9%) | 5.88-24.46 | -34.8% / -57.0% | -19.7% | 1.6M |
| CECO | 53.18 (10:04 iex) | +21.7% | 43.71 | 61.01 / 51.40-61.01 | 5.71 (13.1%) | 37.15-68.40 | -18.3% / -32.5% | -13.4% | 1.4M |
| LITX | 10.23 (10:02 iex) | +21.6% | 8.41 | 8.72 / 8.65-10.29 | 4.26 (50.7%) | 7.48-42.88 | -61.7% / -71.0% | -63.9% | 4.8M |
| BEZ | 6.92 (10:04 iex) | -25.3% | 9.26 | 8.31 / 6.92-8.46 | 1.57 (17.0%) | 4.95-10.82 | +29.0% / +39.7% | +21.8% | 5.6M |
| IONS | 29.43 (10:04 iex) | -25.3% | 39.42 | 32.27 / 28.11-32.58 | 1.71 (4.3%) | 38.30-45.84 | -8.0% / -15.8% | -9.4% | 2.7M |
| IBRX | 6.71 (10:05 iex) | -22.3% | 8.63 | 7.21 / 6.36-7.30 | 0.63 (7.3%) | 7.75-10.62 | -1.6% / -1.2% | +4.2% | 12.5M |
| LITZ | 40.30 (10:01 iex) | -21.2% | 51.11 | 48.73 / 39.70-49.52 | 6.79 (13.3%) | 17.93-57.71 | +62.6% / +79.6% | +97.1% | 1.2M |
| UVIX | 42.55 (10:03 iex) | -17.7% | 51.69 | 46.09 / 42.34-46.55 | 5.94 (11.5%) | 32.32-53.38 | +33.4% / +35.8% | +22.6% | 3.8M |
| DAMD | 10.73 (10:04 iex) | -16.8% | 12.90 | 11.50 / 10.56-11.77 | 1.82 (14.1%) | 8.97-16.68 | +13.8% / +12.1% | +9.7% | 3.8M |
| ARWR | 48.91 (10:05 iex) | -15.9% | 58.16 | 53.03 / 48.44-53.62 | 2.34 (4.0%) | 55.83-62.50 | -1.3% / -13.1% | -2.9% | 1.6M |
