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

Research is mostly done: GOOGL is down 11% after earnings, MSFT is up after its beat, CAT is down 11% on guidance, LLY is up 4.6%, GDP and PCE are out, and the Fed held yesterday. Next I'm writing the brief and the orders.

# Pre-market brief — Thursday 2026-10-29

*Clock: 09:05 ET = 14:05 Stockholm. Europe has gone back to standard time but the US has not yet, so the gap is **ET+5** until Nov 1. All Stockholm times below use +5.*

## 1. Tape
The Fed held rates yesterday as expected, with **two dissents in favour of a hike** (verified: CNBC, Bloomberg/AP). Overnight, mega-cap results split on whether AI spending pays off:
- **Alphabet is down about 11% pre-market (288.12).** Search revenue disappointed and cash burn jumped, even with cloud growing over 100%.
- **MSFT is up 1.9% (541.00)** after beating.
- **CAT is down 11% (632.69).** It beat on EPS at 7.20 vs 7.04 but left guidance unchanged, and the "AI power" trade sold off with it.
- **LLY is up 4.6% (1,347.96)** on its GLP-1 numbers.
- NOW and FTNT are down double digits.

Futures: NQ about −1.2%, ES about −0.4%, Dow roughly flat to slightly lower. 10-year yield 5.01%, VIX about 17.1, WTI about $101.5 (−1.4% on a renewed US–Iran diplomatic push). Defensives, financials and health care are bid (XLV +2.3%, XLP +1.5%, XLF +1.4%). The regime is **rotation out of AI-capex names into defensives and financials, not broad risk-off**. The edge is short AI-capex and software, long health care, financials and selected mega-caps that are actually monetising.

## 2. Calendar
| Time ET | Stockholm | Event | Actual vs consensus | Touches |
|---|---|---|---|---|
| 08:30 | 13:30 | Q3 GDP (advance) | **3.4% vs 3.2%**, Q2 was 2.2% | All; supports KRE/XLF |
| 08:30 | 13:30 | Initial claims | **194K vs 199K** | Hawkish lean |
| 08:30 | 13:30 | Sept PCE / core PCE | Headline 0.5% m/m (in line), 3.6% y/y; core 0.3% m/m (in line), **3.1% y/y vs 3.0% prior** | Rates; MSFT/tech multiples |
| Pre-mkt | — | CAT, LLY, MRK earnings | CAT beat but no raise, −11%; LLY beat, +4.6% | XLV (LLY, MRK holdings) |
| After close | ~21:00+ | **AMZN**, INTC (MA also cited, timing not verified) | AMZN: EPS ~1.96, revenue ~$202B | META short (read-across on AI capex), MSFT |
| Wed (done) | — | FOMC hold, 2 hawkish dissents | — | Rates |

The reaction to the data is muted. Strong growth plus sticky core inflation keeps hike risk alive. The 10-year is flat around 5%.

## 3. Open positions and resting entries
- **XLV long** (179.57, last 183.82): **intact and working**. The LLY beat has pushed it through its 20d high of 182.25, and the 184.80 target is 0.5% away, so it will probably fill today. **Raise the stop to 179.80** (just above entry; it gives up the gap only if the whole breakout fails). Target stays. *manage: update.*
- **KRE long** (73.06, last 72.60): **intact**. The GDP beat and steeper curve help, and XLF is +1.4%. 20d high 73.42. Hold at 71.25 / 76.20.
- **META short** (616.20, last 617.21): **intact, arguably stronger**. Alphabet's punishment for cash burn is the same "capex without a payoff" theme. META is green pre-market, but that looks like rotation inside communication services, not a thesis break. The 643 stop is about 1 ATR away. Hold. AMZN tonight is a read-across risk in either direction; not a reason to exit.
- **TSLA long** (398.69, last 404.80): **intact** below its 20d high of 410.85. Hold at 395 / 421. Moving the stop to breakeven would put it inside the 14-point ATR, so it stays where it is.
- **XLE buy-stop at 70.00 (resting)**: keep it. Oil is softer on the diplomacy headlines, but the order needs a break above the 69.86 20d high to trigger, and it only fills if the tape agrees. XOM/CVX may report tomorrow (date not verified). Because XLE is an ETF, rule 8 does not apply.

## 4. New plays

**MSFT long**
| Field | Value |
|---|---|
| Ticker | MSFT |
| Direction | Long |
| Catalyst | FQ1 beat after the close on 2026-10-28; +1.9% pre-market against a −1.2% NQ |
| Thesis | The market now pays for AI spending that shows up as revenue. MSFT is the counter-example to GOOGL and META, and capital rotating within mega-caps should keep flowing to it. Post-earnings drift for a beat in a weak tape tends to persist for 2–5 days. |
| Entry | Limit 537.00 (buys a modest fade of the gap, not the pre-market high) |
| Stop | 522.00: below the prior close of 531 and the mid-range. A full gap fill plus more means the beat has been rejected |
| Target | 567.00 (+2.0R), above the 551 20d high |
| Risk tier | 0.5: the tape is selling AI names and the Nasdaq tone is poor |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target first) | 38% |
| Invalidation | MSFT gives up its gain and goes red today while QQQ stabilises, which would show relative weakness. |
| What I'd be wrong about | The AI-capex unwind is a whole-factor de-rating, and MSFT is the next-largest capex spender. A beat-and-pop can be sold within a day, the way CAT was. |

**CRM short, breakdown probe**
| Field | Value |
|---|---|
| Ticker | CRM |
| Direction | Short |
| Catalyst | Software de-rating after NOW and FTNT fell double digits on earnings (2026-10-29); CRM −5.1% pre-market in sympathy |
| Thesis | If CRM breaks its 220.29 20d low, the sympathy move becomes a range breakdown and the software unwind extends. |
| Entry | Sell-stop at 219.80, below the 20d low (pre-market 229.72, so the trigger is valid) |
| Stop | 229.00: back above today's pre-market level, so the breakdown has failed |
| Target | 201.40 (2.0R) |
| Risk tier | 0.25: a sympathy trade, already well extended |
| Time horizon | 1–4 days |
| Conviction | 2 |
| P(target first) | 32% |
| Invalidation | Software bounces into the close and CRM reclaims 230 before triggering. |
| What I'd be wrong about | CRM didn't report anything itself. Sympathy gaps often fill, and the 20d low may hold as support. CRM's own earnings are normally early December, outside the horizon (date not verified this session). |

## 5. Both sides
- **Best long:** MSFT, 537 limit / 522 stop / 567 target, 38%. Taken.
- **Best short:** GOOGL continuation below its opening range after the −11% earnings gap. I can't set a sensible trigger before seeing the opening range, so it goes to the review. For scoring, the pass logs a bounce-short at 300 limit / 312 stop / 276 target, 35%. CRM is the short taken now, as a probe.

## 6. Passing on
- **GOOGL short**: the levels depend on the opening range, so it's left to the review. Logged as 300 / 312 / 276.
- **CAT short**: the 11% gap is already the move. Shorting at the open sits at maximum extension. A bounce-short at 655 / stop 680 / target 610 is logged at 34%.
- **LLY long**: strong breakout, but adding it to XLV would push net health care past the 40% cap at a meaningful size. Logged at market 1348 / 1290 / 1440, 40%.
- **AMZN**: reports tonight. Rule 8, and I have no edge on the print.
- **SMH/NVDA short**: duplicates the META short in the AI factor. Risk budget is better spent elsewhere.

## 7. For the post-open review
- **GOOGL:** if it trades below its 09:30–10:00 low and stays under 295, short with the stop above the opening-range high (at least 300) and target 270, at 0.5% risk. If it reclaims 300, do nothing.
- **MSFT:** if the 537 limit hasn't filled and MSFT holds above 541 at 10:00 with QQQ off its lows, cancel the limit and re-enter at market with the 522 stop (still 0.5%). If MSFT is red by 10:00, cancel the limit.
- **XLV:** if the target filled, consider LLY or XLP at 0.5% using the freed health-care room. If XLV is back under 182.25, the 179.80 stop stands.
- **CAT:** short only if it breaks below its opening-range low and stays under 625. Stop at 650, target 595, 0.25%.

## 8. Book state
- **Exposure:** gross about 67% now, plus MSFT (~18%) and CRM (~6%) if they fill, for about 91% against a 150% cap. Net about +68% if both fill, against ±100%.
- **Risk at stake:** 1.53%, falling to about 1.0% once the XLV stop moves to 179.80, plus 0.75% new, for about 1.8% against a 4% cap. Slots: 5 + 2 = 7 of 8.

```json
{
  "date": "2026-10-29",
  "no_trade": false,
  "session_note": "Rotation out of AI-capex (GOOGL -11%, CAT -11%) into health care/financials; long the monetiser MSFT at half size, probe a software breakdown in CRM, GOOGL/CAT continuation shorts left to the review.",
  "plays": [
    {
      "ticker": "MSFT",
      "direction": "long",
      "entry_type": "limit",
      "entry": 537.00,
      "stop": 522.00,
      "targets": [567.00],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "FQ1 beat reported 2026-10-28 after close; +1.9% pre-market vs NQ -1.2%.",
      "thesis": "Market is paying for AI spend that shows up as revenue; MSFT is the counter-example to GOOGL/META and should attract rotation within mega-caps. Post-earnings drift on a beat into a weak tape.",
      "invalidation": "MSFT turns red on the day while QQQ stabilises.",
      "bear_case": "The AI-capex unwind is factor-wide and MSFT is a top capex spender; beat-and-pop can be sold like CAT."
    },
    {
      "ticker": "CRM",
      "direction": "short",
      "entry_type": "stop",
      "entry": 219.80,
      "stop": 229.00,
      "targets": [201.40],
      "time_horizon": "1-4 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.32,
      "catalyst": "Software de-rating after NOW and FTNT double-digit earnings drops on 2026-10-29; CRM -5.1% pre-market.",
      "thesis": "A break below the 220.29 20-day low turns a sympathy gap into a range breakdown and extends the software unwind.",
      "invalidation": "Software bounces and CRM reclaims 230 before triggering.",
      "bear_case": "No company-specific news; sympathy gaps often fill and the 20d low may hold."
    }
  ],
  "manage": [
    {
      "ticker": "XLV",
      "action": "update",
      "stop": 179.80,
      "reason": "LLY-driven breakout above the 182.25 20d high, target 0.5% away; lift stop just above entry so a failed breakout scratches instead of losing 1R."
    }
  ],
  "passed": [
    {
      "ticker": "GOOGL",
      "direction": "short",
      "entry_type": "limit",
      "entry": 300.00,
      "stop": 312.00,
      "targets": [276.00],
      "p_target_first": 0.35,
      "reason": "Post-earnings continuation short needs the opening range to place; left to the post-open review."
    },
    {
      "ticker": "CAT",
      "direction": "short",
      "entry_type": "limit",
      "entry": 655.00,
      "stop": 680.00,
      "targets": [610.00],
      "p_target_first": 0.34,
      "reason": "-11% gap already the move; only a bounce or an opening-range breakdown offers location."
    },
    {
      "ticker": "LLY",
      "direction": "long",
      "entry_type": "market",
      "entry": 1348.00,
      "stop": 1290.00,
      "targets": [1440.00],
      "p_target_first": 0.40,
      "reason": "Strong earnings breakout, but stacked on XLV it breaches the 40% health care sector cap at meaningful size."
    }
  ]
}
```

Sources: [Yahoo Finance live](https://finance.yahoo.com/markets/live/stock-market-today-thursday-october-29-dow-sp-500-nasdaq-alphabet-microsoft-081708101.html), [BNN Bloomberg](https://www.bnnbloomberg.ca/markets/2026/10/29/world-shares-and-us-futures-are-mixed-after-google-parent-alphabets-earnings-disappoint/), [FXStreet GDP](https://www.fxstreet.com/news/united-states-economy-grows-34-in-third-quarter-vs-32-expected-202610291232), [FXStreet claims](https://fxstreet.com/news/us-initial-jobless-claims-dropped-to-194k-last-week-202610291236), [FXTribune core PCE](https://fxtribune.com/news/us-core-pce-inflation-rises-to-3-1-in-september-2026/), [24/7 Wall St on CAT](https://247wallst.com/investing/2026/10/29/caterpillar-beat-earnings-and-still-dropped-9-the-ai-power-trade-just-hit-the-same-wall-as-software/), [EnergyNow oil](https://energynow.com/2026/10/oil-prices-fall-as-renewed-u-s-iran-peace-efforts-ease-supply-fears-wti-near-101-50-brent-slips-below-114/), [CNBC Fed](https://cnbc.com/2026/10/28/fed-meeting-today-live-updates.html), [MarketBeat AMZN](https://www.marketbeat.com/stocks/NASDAQ/AMZN/earnings/), [Blumify Apple date](https://blumify.io/markets/apple)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC, 15:05 Stockholm), Thursday 2026-10-29. The cash session opened 35 min ago and closes at 16:00 ET (21:00 Stockholm).
- Equity: **$102,875.03**
- Cash: $73,320.98
- Session P&L so far: +0.60% (new entries are blocked at -3.0%)
- Gross exposure: $63,747 (62% of equity, cap 150%)
- Net exposure: $+40,629 (+39%, cap +/-100%)
- Risk at stake (entry to stop): $1,725 (1.68% of equity, cap 4.0%) — 2.32% left for new plays
- Slots: 4 open + 2 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 73.22 | +22 (+0.2%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| META | short | 9 | 616.20 | 624.91 | -78 (-1.4%) | 643.00 | 580.00 | Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward  |
| MSFT | long | 34 | 533.93 | 526.88 | -240 (-1.3%) | 522.00 | 567.00 | Market is paying for AI spend that shows up as revenue; MSFT is the counter-example to GOOGL/META and should attract rot |
| TSLA | long | 17 | 398.69 | 403.99 | +90 (+1.3%) | 395.00 | 421.00 | Relative strength at the range top while megacap tech chops; a clean 20d-high break opens room toward 420. |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| CRM | short | 27 | 219.80 | stop | 229.00 | 201.40 | 2026-10-29 |
| XLE | long | 243 | 70.00 | stop | 67.90 | 73.20 | 2026-10-28 |

### Record

31 closed trades: 12W / 19L, total +3.66R, net $+3,091 realized. Shorts taken: 29.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XLV | long | target | +1.65R | $+837 | 40% |
| NVDA | short | close | -0.76R | $-190 | 35% |
| XOM | long | stop | -0.07R | $-37 | 37% |
| BA | short | target | +1.52R | $+379 | 34% |
| ORCL | short | stop | -0.06R | $-16 | 33% |

### Ideas you passed on, replayed against the tape

68 resolved: 18 reached target first, 33 stop first, 12 never reached the entry, 5 expired, 0 ambiguous. Average -0.09R across the 56 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-22 open | META | short | Short on a bounce after the -5.9% earnings break; no slot, would be a 5th AI-cap | never filled | - | 33% |
| 2026-10-15 pre-market | TLT | long | The flight-to-safety rally is fighting a 6.3% PPI print; two-sided, no edge. | expired | +1.21R | 35% |
| 2026-10-15 pre-market | NVDA | short | At its 20d low after -6.8% in 5 days; duplicates the semis factor I'm exiting at | expired | +0.94R | 34% |
| 2026-10-23 open | CAT | short | Under its 695 20d low, but the Q3 earnings date is likely inside the horizon and | stop | -1.04R | 38% |
| 2026-10-22 pre-market | AVGO | short | Same AI factor as the existing shorts; no slot. | stop | -1.10R | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| KRE | 73.23 (10:05 iex) | +1.6% | 72.11 | 72.63 / 72.63-73.45 | 1.24 (1.7%) | 67.79-73.42 | +2.4% / +0.3% | +2.1% | 15.3M |
| META | 625.29 (10:05 iex) | +2.1% | 612.49 | 620.92 / 616.80-625.37 | 25.55 (4.2%) | 609.00-771.27 | -12.7% / -8.1% | -12.2% | 21.6M |
| MSFT | 526.89 (10:05 iex) | -0.8% | 531.01 | 540.01 / 525.25-541.29 | 10.65 (2.0%) | 512.17-551.15 | +0.2% / +3.9% | -0.4% | 20.2M |
| TSLA | 403.94 (10:05 iex) | -0.1% | 404.22 | 405.62 / 400.50-406.43 | 14.06 (3.5%) | 349.33-410.85 | +7.3% / +10.0% | +4.6% | 37.7M |
| CRM | 233.28 (10:05 iex) | -3.6% | 242.11 | 229.17 / 225.04-233.01 | 8.73 (3.6%) | 220.29-252.42 | +1.7% / +1.8% | +0.1% | 7.2M |
| XLE | 68.82 (10:05 iex) | +0.5% | 68.45 | 68.90 / 68.55-69.22 | 1.40 (2.0%) | 61.04-69.86 | +3.0% / +6.1% | +0.4% | 32.2M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 769.87 (10:05 iex) | -0.3% | 772.31 | 768.80 / 767.27-769.82 | 7.09 (0.9%) | 758.68-781.62 | +0.2% / +0.7% | -0.1% | 38.2M |
| QQQ | 716.85 (10:05 iex) | -1.2% | 725.61 | 716.55 / 711.62-717.01 | 11.94 (1.6%) | 701.16-762.86 | -0.9% / +0.1% | +0.1% | 36.8M |
| IWM | 284.86 (10:05 iex) | +1.3% | 281.29 | 282.44 / 282.15-284.72 | 3.50 (1.2%) | 269.88-284.64 | +1.5% / -1.2% | +1.7% | 24.9M |
| DIA | 523.43 (10:05 iex) | -0.2% | 524.68 | 522.94 / 521.31-523.08 | 5.10 (1.0%) | 504.59-528.45 | +1.2% / +0.6% | -0.6% | 3.4M |
| TLT | 81.39 (10:04 iex) | +0.5% | 80.99 | 81.39 / 81.36-81.86 | 0.80 (1.0%) | 76.43-81.92 | +2.2% / +0.9% | +0.9% | 42.2M |
| GLD | 369.14 (10:05 iex) | -1.2% | 373.51 | 368.80 / 368.34-369.94 | 5.13 (1.4%) | 364.33-385.22 | -1.1% / -4.9% | -1.4% | 7.9M |
| USO | 165.14 (10:04 iex) | -0.9% | 166.57 | 164.31 / 163.36-165.14 | 4.66 (2.8%) | 141.76-169.96 | +7.0% / +12.1% | +4.2% | 4.8M |
| SMH | 560.77 (10:04 iex) | -1.2% | 567.67 | 558.92 / 555.73-561.53 | 18.58 (3.3%) | 520.53-639.47 | -1.8% / -1.0% | +2.0% | 8.8M |
| XLK | 189.26 (10:05 iex) | -0.9% | 191.00 | 188.92 / 187.72-189.28 | 4.14 (2.2%) | 181.50-203.25 | -0.7% / +0.8% | +1.3% | 8.9M |
| XLF | 57.13 (10:05 iex) | +1.8% | 56.13 | 56.72 / 56.67-57.23 | 0.69 (1.2%) | 52.81-56.67 | +2.0% / +0.5% | +0.2% | 32.7M |
| XLE | 68.82 (10:05 iex) | +0.5% | 68.45 | 68.90 / 68.55-69.22 | 1.40 (2.0%) | 61.04-69.86 | +3.0% / +6.1% | +0.4% | 32.2M |
| XLV | 183.89 (10:05 iex) | +2.3% | 179.72 | 182.97 / 182.10-184.85 | 3.04 (1.7%) | 165.19-182.25 | +3.4% / +4.8% | +0.4% | 8.5M |
| XLI | 169.19 (10:05 iex) | +0.4% | 168.49 | 167.62 / 167.45-169.17 | 2.49 (1.5%) | 162.97-172.34 | +0.2% / -1.5% | +0.1% | 7.5M |
| XLY | 116.20 (10:05 iex) | +0.8% | 115.33 | 115.76 / 115.13-116.16 | 1.65 (1.4%) | 107.99-116.22 | +2.2% / +1.9% | -0.2% | 7.1M |
| XLP | 87.59 (10:05 iex) | +0.9% | 86.84 | 87.83 / 87.42-88.08 | 1.33 (1.5%) | 80.10-89.99 | +2.0% / +3.1% | -0.3% | 14.0M |
| XLU | 42.93 (10:05 iex) | +1.0% | 42.49 | 42.93 / 42.86-43.25 | 0.60 (1.4%) | 39.10-42.97 | +2.2% / +2.0% | +1.2% | 31.7M |
| XLB | 52.17 (10:05 iex) | +0.6% | 51.86 | 51.72 / 51.72-52.22 | 0.65 (1.3%) | 47.81-51.90 | +3.1% / +1.9% | +1.1% | 11.2M |
| XLRE | 42.77 (10:04 iex) | +1.5% | 42.13 | 42.64 / 42.43-43.00 | 0.64 (1.5%) | 40.28-43.21 | +1.0% / -1.0% | +0.2% | 8.1M |
| XLC | 101.50 (10:05 iex) | -1.6% | 103.14 | 101.18 / 100.13-101.47 | 1.78 (1.7%) | 102.62-113.17 | -5.7% / -7.1% | -5.4% | 6.5M |
| KRE | 73.23 (10:05 iex) | +1.6% | 72.11 | 72.63 / 72.63-73.45 | 1.24 (1.7%) | 67.79-73.42 | +2.4% / +0.3% | +2.1% | 15.3M |
| XHB | 99.94 (10:05 iex) | +2.0% | 97.97 | 97.85 / 97.42-99.83 | 2.26 (2.3%) | 91.87-99.71 | +1.9% / -0.6% | +2.5% | 2.1M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 349.77 (10:05 iex) | +1.7% | 343.83 | 348.10 / 347.30-351.43 | 6.22 (1.8%) | 325.81-351.73 | +0.9% / +3.6% | -0.0% | 38.5M |
| MSFT | 526.89 (10:05 iex) | -0.8% | 531.01 | 540.01 / 525.25-541.29 | 10.65 (2.0%) | 512.17-551.15 | +0.2% / +3.9% | -0.4% | 20.2M |
| NVDA | 213.25 (10:05 iex) | -1.0% | 215.38 | 214.49 / 212.09-215.33 | 6.05 (2.8%) | 210.18-243.37 | -3.8% / -3.0% | -3.0% | 101.2M |
| AMZN | 245.70 (10:05 iex) | -3.5% | 254.60 | 246.95 / 241.24-248.46 | 6.67 (2.6%) | 246.12-265.34 | -0.2% / -0.2% | -3.0% | 35.6M |
| GOOGL | 286.27 (10:05 iex) | -11.9% | 324.89 | 286.88 / 280.36-288.20 | 8.05 (2.5%) | 316.60-359.40 | -4.4% / -4.9% | -2.9% | 25.7M |
| META | 625.29 (10:05 iex) | +2.1% | 612.49 | 620.92 / 616.80-625.37 | 25.55 (4.2%) | 609.00-771.27 | -12.7% / -8.1% | -12.2% | 21.6M |
| TSLA | 403.94 (10:05 iex) | -0.1% | 404.22 | 405.62 / 400.50-406.43 | 14.06 (3.5%) | 349.33-410.85 | +7.3% / +10.0% | +4.6% | 37.7M |
| AVGO | 342.59 (10:05 iex) | -2.6% | 351.81 | 342.11 / 338.84-344.27 | 11.20 (3.2%) | 320.23-380.84 | +1.4% / -0.5% | +4.1% | 22.0M |
| AMD | 568.62 (10:05 iex) | -1.7% | 578.44 | 561.82 / 560.63-572.88 | 28.68 (5.0%) | 502.60-658.52 | -0.2% / +6.0% | +4.7% | 19.6M |
| ORCL | 139.78 (10:05 iex) | -3.3% | 144.54 | 144.13 / 139.42-144.61 | 7.63 (5.3%) | 122.76-148.48 | +7.0% / +2.0% | +11.9% | 30.7M |
| NFLX | 62.15 (10:05 iex) | +0.3% | 61.99 | 62.48 / 61.39-62.62 | 2.15 (3.5%) | 61.51-73.07 | -9.0% / -15.5% | -4.7% | 43.9M |
| CRM | 233.28 (10:05 iex) | -3.6% | 242.11 | 229.17 / 225.04-233.01 | 8.73 (3.6%) | 220.29-252.42 | +1.7% / +1.8% | +0.1% | 7.2M |
| JPM | 344.50 (10:04 iex) | +1.5% | 339.30 | 344.50 / 342.48-345.40 | 6.24 (1.8%) | 324.25-344.40 | +1.7% / -1.0% | +1.2% | 7.0M |
| GS | 933.76 (10:05 iex) | +0.9% | 925.17 | 937.19 / 925.03-938.50 | 25.38 (2.7%) | 859.03-931.00 | +3.6% / -2.7% | +2.3% | 2.3M |
| BAC | 51.84 (10:05 iex) | +1.9% | 50.85 | 51.74 / 51.51-51.90 | 1.24 (2.4%) | 49.26-54.93 | -2.7% / -10.5% | +0.1% | 42.1M |
| XOM | 183.34 (10:05 iex) | +0.7% | 182.02 | 183.76 / 182.30-184.39 | 3.95 (2.2%) | 160.81-184.88 | +4.7% / +9.0% | +2.2% | 11.5M |
| CVX | 231.07 (10:03 iex) | +0.8% | 229.20 | 232.25 / 230.29-232.95 | 4.64 (2.0%) | 201.96-234.08 | +4.6% / +8.1% | +1.1% | 7.3M |
| LLY | 1,385.96 (10:05 iex) | +7.6% | 1,288.30 | 1,332.73 / 1,330.00-1,408.38 | 37.38 (2.9%) | 1,131.21-1,321.21 | +5.5% / +8.1% | +1.4% | 2.3M |
| UNH | 408.83 (10:05 iex) | +0.4% | 407.10 | 413.71 / 406.90-414.76 | 13.29 (3.3%) | 362.60-426.55 | +3.2% / +4.8% | -2.4% | 6.0M |
| JNJ | 275.13 (10:04 iex) | +1.5% | 271.04 | 275.31 / 274.44-278.05 | 7.36 (2.7%) | 245.17-272.75 | +4.6% / +2.1% | +5.1% | 7.9M |
| WMT | 120.37 (10:05 iex) | +1.3% | 118.77 | 121.05 / 119.66-121.05 | 2.44 (2.1%) | 103.39-122.40 | +4.1% / +8.3% | +0.8% | 20.0M |
| COST | 988.00 (10:05 iex) | +0.5% | 982.73 | 995.14 / 986.12-995.14 | 16.35 (1.7%) | 903.77-1,021.45 | +1.4% / +4.4% | -1.6% | 2.1M |
| HD | 325.37 (10:05 iex) | +2.5% | 317.56 | 324.27 / 322.68-326.63 | 7.06 (2.2%) | 277.15-327.92 | +5.1% / +3.0% | +1.1% | 4.9M |
| CAT | 659.16 (10:05 iex) | -7.6% | 713.38 | 636.33 / 631.01-659.77 | 25.93 (3.6%) | 679.50-874.87 | -6.4% / -9.6% | -3.4% | 2.7M |
| BA | 170.20 (10:05 iex) | +1.8% | 167.14 | 168.25 / 167.74-170.30 | 5.47 (3.3%) | 165.01-196.93 | -10.8% / -15.6% | -13.1% | 9.9M |
| DAL | 82.50 (10:05 iex) | +2.7% | 80.35 | 81.45 / 81.20-82.59 | 3.16 (3.9%) | 74.14-85.93 | +0.7% / +0.0% | +3.5% | 7.3M |
| UAL | 106.81 (10:05 iex) | +3.3% | 103.43 | 104.72 / 104.41-106.77 | 4.88 (4.7%) | 94.54-115.20 | -0.5% / -4.2% | +1.7% | 5.2M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-29 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| ADT | 9.94 (10:05 iex) | +34.1% | 7.41 | 9.88 / 9.39-9.99 | 0.20 (2.6%) | 6.03-7.60 | +11.4% / +8.1% | +9.0% | 7.4M |
| GKOS | 232.34 (10:05 iex) | +28.1% | 181.43 | 212.83 / 207.41-232.76 | 6.53 (3.6%) | 146.38-187.94 | +6.8% / +6.0% | +2.6% | 1.1M |
| PRCH | 20.92 (10:05 iex) | +28.3% | 16.30 | 19.47 / 18.74-21.30 | 0.84 (5.2%) | 16.07-18.75 | -6.5% / -4.6% | -12.3% | 1.6M |
| TDOC | 8.52 (10:05 iex) | +23.8% | 6.88 | 7.92 / 7.90-8.99 | 0.29 (4.2%) | 5.42-6.92 | +15.2% / +11.9% | +9.2% | 3.9M |
| CROX | 147.90 (10:05 iex) | +23.6% | 119.69 | 140.00 / 139.32-150.68 | 4.08 (3.4%) | 114.08-127.28 | +0.5% / +0.3% | +1.0% | 1.0M |
| BHC | 8.32 (10:05 iex) | +20.2% | 6.92 | 7.66 / 7.58-8.58 | 0.28 (4.0%) | 5.61-6.97 | +11.9% / +12.2% | +7.3% | 2.2M |
| CVNA | 69.05 (10:05 iex) | +16.9% | 59.05 | 65.28 / 63.81-69.08 | 3.00 (5.1%) | 55.91-66.02 | -2.5% / -10.4% | -0.2% | 8.6M |
| PWP | 14.94 (10:03 iex) | +15.5% | 12.94 | 14.29 / 14.22-15.34 | 0.91 (7.0%) | 12.12-16.53 | -8.2% / -12.8% | +3.8% | 1.9M |
| IOVA | 10.35 (10:05 iex) | -30.1% | 14.81 | 10.73 / 10.21-11.58 | 0.93 (6.3%) | 12.31-15.37 | +4.6% / +30.5% | +1.3% | 11.7M |
| MVLL | 23.41 (10:02 iex) | -24.3% | 30.94 | 23.83 / 22.26-24.50 | 4.06 (13.1%) | 23.77-45.89 | -5.3% / -0.2% | +4.0% | 2.0M |
| GGLL | 66.81 (10:05 iex) | -24.1% | 88.02 | 67.21 / 63.70-68.00 | 4.55 (5.2%) | 83.37-108.08 | -8.9% / -10.5% | -5.8% | 1.6M |
| NOW | 115.14 (10:05 iex) | -23.3% | 150.13 | 120.91 / 112.37-121.50 | 6.33 (4.2%) | 133.47-159.50 | +3.5% / +7.6% | -2.0% | 12.5M |
| FTNT | 139.18 (10:05 iex) | -20.0% | 174.08 | 127.92 / 127.40-138.52 | 7.57 (4.3%) | 166.22-197.13 | -4.3% / +1.3% | +0.0% | 4.0M |
| SFM | 50.05 (10:05 iex) | -19.3% | 62.00 | 47.42 / 47.35-50.90 | 3.01 (4.8%) | 60.47-69.53 | -4.7% / -12.5% | -5.4% | 2.4M |
| AIOK | 22.94 (10:01 iex) | -18.5% | 28.14 | 22.38 / 20.43-23.30 | 3.87 (13.8%) | 3.90-29.90 | - / - | +481.4% | 7.3M |
| ALNY | 196.50 (10:05 iex) | -15.4% | 232.40 | 185.59 / 179.87-199.50 | 7.88 (3.4%) | 215.46-251.71 | +2.3% / -2.8% | +3.2% | 1.4M |
