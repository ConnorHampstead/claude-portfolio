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

I've finished the research. Here is the brief.

# Pre-market brief: Tuesday 2026-09-29 (written 09:05 ET / 15:05 Stockholm)

## 1. Tape
Monday was a risk-off day. The S&P 500 fell 0.8%, the Nasdaq 1.1% and the Dow 347 points, as the US–Iran standoff over Hormuz pushed oil higher and bonds lower. Trump rejected Iran's offer to reopen the strait, and WTI settled around $92.60 and Brent around $105 (verified, Rio Times). This morning is a small bounce led by chips. SPY is +0.1% (766.57), QQQ +0.3% and SMH +0.9%. USO is −2.8% and XLE −1.1%, while Dow futures lag.

The backdrop is the key point. The Fed hiked 25bp on 9/16 to 3.75–4.00% and 16 of 18 officials pencil in another hike. The 10-year crossed 5% for the first time since 2007 (verified, CNBC). The regime is a **rates-and-oil squeeze on rate-sensitive sectors, with rotation into semis.** XLU is −8.4% against its 50-day average, XLF −4.6%, XHB −5.9% and XLY −4.8%, while SMH is +5.9% and QQQ +3.3%. The edge is **short** in rate-sensitive sectors and **long** only in the semis/AI leadership. Today's bounce is thin, and I read it as oversold relief rather than a change of regime.

## 2. Calendar
| Event | ET | Stockholm | Status / consensus | Touches |
|---|---|---|---|---|
| Conf. Board Consumer Confidence (Sep) | 10:00 | 16:00 | Ahead. I could not verify a consensus figure | HD, BAC, XLU, DAL |
| JOLTS (Aug) | 10:00 | 16:00 | Ahead. Consensus not verified | Rates → all positions |
| Micron Q4 earnings | Wed 9/30 after close | Wed ~22:05 | MU is +1.7% pre-market going in | NVDA resting long (another company's earnings, so not a rule-8 binary) |
| GDP | Wed 9/30 08:30 | 14:30 | Ahead | All |
| Nike earnings | Thu 10/1 after close | ~22:15 | Ahead | None |
| Payrolls | Fri 10/2 08:30 | 14:30 | Ahead (some releases may still be disrupted by the aftermath of the 2025 shutdown) | All |
| Iran/Hormuz headlines | continuous | — | Live | DAL, energy, and rates through oil |

Nothing had been released by 09:05 today that I could find. The first prints are at 10:00, and the post-open review sees them.

## 3. Open positions and resting entries
- **BA short** (187.31, last 185.26, stop 194.90, target 176.00): **thesis intact.** Price sits just above the 20-day low of 184.01, −13.7% against the 50-day average, and the stop is about 1.5 ATR away. Hold with no change. A daily close under 184 opens the path to target.
- **BAC short** (55.80, last 55.66, stop 57.70, target 52.90): **intact.** A 5% 10-year and a hiking Fed are bad for bank credit and fees, and BAC sits right on its 20-day low of 55.37. Hold.
- **HD short** (289.30, last 291.87, stop 297.60, target 278.00): **intact but not working yet.** It is up 0.7% pre-market on the broad bounce. Mortgage rates keyed to a 5% 10-year are the thesis, and that has only gotten stronger. The stop is 1.3 ATR above the current price, so I leave it where it is. If HD reclaims 297 the market is telling me it doesn't care.
- **NVDA resting buy stop at 234.70** (stop 227.40, target 246.00): **keep.** The trigger sits above the 20-day high of 234.50, and pre-market is 230.39, so it is still valid. Semis lead the tape. MU reports Wednesday after the close, which could move NVDA in sympathy either way. That is ambient risk, and the stop is 1.4 ATR from entry.
- **ORCL resting sell stop at 130.90** (stop 138.60, target 119.00): **keep.** The trigger sits under the 20-day low of 131.58, and pre-market is 132.68. The news flow is still negative: the Project Jupiter force-majeure notice on 9/24 and fresh layoffs on 9/28 (verified, single-source aggregator).

## 4. New plays

### DAL long (breakout)
| Field | Value |
|---|---|
| Ticker | DAL |
| Direction | Long |
| Catalyst | USO −2.8% pre-market on 9/29, which eases fuel costs. DAL is +1.5% pre-market at 85.30, against a 20-day high of 85.47 |
| Thesis | On 9/28 DAL traded down to 82.80 on a BMO target cut and fuel costs, then closed at 84.03 (verified, Schaeffer's). Buyers absorbed a bad headline. A break of the 20-day high while oil fades starts a move back toward the July highs (ATH 95.67). |
| Entry | Buy stop 85.80 |
| Stop | 82.40: below Monday's 82.80 reversal low, 1.4 ATR from entry |
| Target | 90.50 (+1.38R) |
| Risk tier | 0.5. The trade is hostage to Iran/oil headlines, which gives it unusual gap risk |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 42% |
| Invalidation | Brent back above $108 on a Hormuz escalation, or DAL loses 84 after triggering |
| What I'd be wrong about | Oil is the whole trade. One headline reverses today's dip, and airlines gap down through the stop. |

Why this is the long I take: it is the cleanest long outside semis, and I already have semis through NVDA. It also partly hedges the book's short-cyclical tilt, since airlines gain when oil falls. Earnings are expected around 10/8–10/9, which is outside the horizon. I have not verified that date and am inferring it from Delta's usual schedule.

### XLU short (breakdown)
| Field | Value |
|---|---|
| Ticker | XLU |
| Direction | Short |
| Catalyst | 10-year at or above 5% after the 9/16 hike, with another hike signaled. The 10:00 JOLTS and confidence prints and Wednesday's GDP are the rate catalysts |
| Thesis | Utilities are bond proxies and the weakest sector on the board: −5.1% against the 20-day average and −8.4% against the 50-day. XLU sits 0.29 above its 20-day low of 39.06. A break under the low with yields pinned near 5% extends the trend. |
| Entry | Sell stop 38.95 (pre-market 39.35) |
| Stop | 40.15: above the 5-day consolidation, about 2.1 ATR from entry |
| Target | 37.55 (+1.17R) |
| Risk tier | 0.5. It stacks the same rate factor as HD and BAC, so it is kept at half |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 45% |
| Invalidation | The 10-year falls back below about 4.85% on soft JOLTS/GDP, or XLU closes back above 40 |
| What I'd be wrong about | Utilities also have an AI-power growth narrative, and after an 8% slide a weak labor print could squeeze them hard. |

## 5. Both sides
- **Best long:** DAL buy stop 85.80 / 82.40 / 90.50, P = 42%. **Taken.** I still hold the NVDA breakout as a resting order.
- **Best short:** XLU sell stop 38.95 / 40.15 / 37.55, P = 45%. **Taken.** I also looked at XLRE (no pre-market trade yet, prior close 41.35, 20-day low 41.22) and GS/JPM. Those are the same factor as XLU and BAC, and XLRE had no print I could check.

## 6. Passing on
- **AMD long** (pre-market 614, World Labs deal): the move is extended at +19.9% against the 50-day average and the ATR is 4.3%. A breakout above 639 needs a 10-point-wide stop, and it overlaps NVDA and semis. Passed, with levels in the JSON.
- **SMH buy stop 610**: the same factor as NVDA, whose order is already resting.
- **XLE/CVX short**: oil falling today, but it depends entirely on Iran headlines and CVX sits near its 20-day low. The location is wrong.
- **FICO, SMMT pre-market movers**: news gaps, and I could not verify levels.

## 7. For the post-open review
- **JOLTS and consumer confidence at 10:00.** If the 10-year pushes up and XLU breaks 39.06, the XLU order handles it. If yields drop sharply (10-year −8bp or more) and XLU is above 39.6, cancel the XLU entry.
- **HD:** if it trades above 296 in the first 30 minutes on a hot bounce, consider closing it rather than taking the full stop. It is not yet a close signal.
- **DAL:** if oil (USO) reverses above 150 by 10:00, cancel the DAL buy stop.
- **NVDA:** if it fills early on MU enthusiasm and the opening range low is under 229, leave the stop at 227.40.

## 8. Book state
If everything fills: gross is about 62% plus NVDA and ORCL already counted, plus about 29% for DAL (about $25k of notional at 0.5%) and about 43% for XLU (about $42k). That is roughly 134%, within the 150% cap. Net is about −31% + DAL +25% − XLU 42% ≈ −48%, within ±100%. Net sector exposure: utilities short about −42% of equity. That is at or above the 40% cap, so the harness may trim or drop the play. Risk at stake would be 2.23% + 0.5% + 0.5% = 3.23% of the 4% cap, with 7 of 8 slots used.

```json
{
  "date": "2026-09-29",
  "no_trade": false,
  "session_note": "Rates (10y ~5%, Fed hiking) and Iran-oil regime: short rate-sensitives, long only leadership; small relief bounce pre-market. Adding breakout DAL long and breakdown XLU short at half risk; existing shorts and resting NVDA/ORCL stops kept.",
  "plays": [
    {
      "ticker": "DAL",
      "direction": "long",
      "entry_type": "stop",
      "entry": 85.80,
      "stop": 82.40,
      "targets": [90.50],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.42,
      "catalyst": "USO -2.8% premarket 9/29 easing fuel costs; DAL +1.5% premarket against 20d high 85.47 after absorbing a BMO PT cut on 9/28 (82.80 low, 84.03 close).",
      "thesis": "Buyers absorbed a fuel-cost downgrade on 9/28 and DAL closed near highs. A break of the 20d high with oil fading opens a retrace toward the July highs.",
      "invalidation": "Brent back above $108 on Hormuz escalation, or DAL loses 84 after triggering.",
      "bear_case": "The trade is purely oil; a single Iran headline gaps airlines through the stop."
    },
    {
      "ticker": "XLU",
      "direction": "short",
      "entry_type": "stop",
      "entry": 38.95,
      "stop": 40.15,
      "targets": [37.55],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.45,
      "catalyst": "10y Treasury at/above 5% after the 9/16 Fed hike with another signaled; JOLTS/confidence 9/29, GDP 9/30, payrolls 10/2 as rate catalysts.",
      "thesis": "Utilities are the weakest sector (-8.4% vs 50d) as bond proxies under 5% yields. A break of the 20d low 39.06 extends the trend.",
      "invalidation": "10y back below ~4.85% on soft data, or XLU closes back above 40.",
      "bear_case": "AI-power demand narrative plus an 8% slide makes utilities squeeze-prone on any soft labor print."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "AMD",
      "direction": "long",
      "entry_type": "stop",
      "entry": 640.00,
      "stop": 612.00,
      "targets": [680.00],
      "p_target_first": 0.40,
      "reason": "Extended +19.9% vs 50d with 4.3% ATR; overlaps the resting NVDA semis exposure."
    },
    {
      "ticker": "SMH",
      "direction": "long",
      "entry_type": "stop",
      "entry": 610.50,
      "stop": 592.00,
      "targets": [640.00],
      "p_target_first": 0.45,
      "reason": "Same factor as resting NVDA breakout; one semis expression is enough ahead of MU earnings."
    },
    {
      "ticker": "CVX",
      "direction": "short",
      "entry_type": "stop",
      "entry": 200.50,
      "stop": 207.50,
      "targets": [190.00],
      "p_target_first": 0.38,
      "reason": "Pure Iran-headline trade sitting at the 20d low; wrong location."
    }
  ]
}
```

Sources:
- [TheStreet – Stock Market Today Sept 29, 2026](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-29-2026)
- [Bloomberg – US Stock Futures Rise as Traders Await Key Economic Data](https://www.bloomberg.com/news/articles/2026-09-29/us-stock-futures-rise-as-traders-await-key-economic-data)
- [Rio Times – Oil settles higher after Trump rejects Iran Hormuz offer](https://www.riotimesonline.com/oil-markets-latam-tuesday-september-29-2026/)
- [CNBC – Fed rate decision September 2026](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html)
- [CNBC – 10-year yield back to 5%](https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html)
- [CNBC – Premarket movers Sept 29](https://www.cnbc.com/2026/09/29/stocks-making-the-biggest-moves-premarket-fair-isaac-spacex-amd-more.html)
- [Current Logic – Morning brief Sept 29](https://currentlogic.substack.com/p/the-morning-brief-september-29-2026)
- [Seeking Alpha – Micron, Nike headline earnings](https://seekingalpha.com/article/4949815-micron-nike-to-headline-earnings-next-week-gdp-numbers-awaited)
- [Timothy Sykes – Oracle layoffs / Project Jupiter](https://www.timothysykes.com/news/oracle-corporation-orcl-news-2026_09_28/)
- [Schaeffer's – Delta dinged by bear note, fuel costs](https://www.schaeffersresearch.com/content/news/2026/09/28/delta-stock-dinged-by-bear-note-higher-fuel-costs)
- [Investing.com – JOLTS and consumer confidence due Tuesday](https://ng.investing.com/news/stock-market-news/jolts-job-openings-and-consumer-confidence-among-data-due-tuesday-93CH-2712613)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Tuesday 2026-09-29. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,523.02**
- Cash: $140,283.64
- Session P&L so far: -0.18% (new entries are blocked at -3.0%)
- Gross exposure: $92,723 (91% of equity, cap 150%)
- Net exposure: $-34,766 (-34%, cap +/-100%)
- Risk at stake (entry to stop): $3,282 (3.23% of equity, cap 4.0%) — 0.77% left for new plays
- Slots: 3 open + 4 resting entries of 8 — you may add at most 1 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| BA | short | 33 | 187.31 | 190.13 | -93 (-1.5%) | 194.90 | 176.00 | Safety headline on the MAX and a broken 20d floor, -7.6% vs 50d. A trade below today's 187.58 low means the opening rang |
| BAC | short | 267 | 55.80 | 55.34 | +121 (+0.8%) | 57.70 | 52.90 | Weakest large bank (-7.5% vs 20d avg). A break below today's opening low confirms the 20d-low support failed and opens a |
| HD | short | 61 | 289.30 | 290.31 | -62 (-0.4%) | 297.60 | 278.00 | Cleanest equity expression of frozen housing under 7%+ mortgages; -9.9% vs 50d with fresh 52-week lows. A trade below 28 |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XLU | short | 423 | 38.95 | stop | 40.15 | 37.55 | 2026-09-29 |
| DAL | long | 149 | 85.80 | stop | 82.40 | 90.50 | 2026-09-29 |
| NVDA | long | 69 | 234.70 | stop | 227.40 | 246.00 | 2026-09-28 |
| ORCL | short | 65 | 130.90 | stop | 138.60 | 119.00 | 2026-09-28 |

### Record

4 closed trades: 2W / 2L, total +0.57R, net $+1,558 realized. Shorts taken: 5.

### Last 4 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| DAL | long | stop | +1.00R | $+999 | 46% |
| LLY | long | stop | +1.76R | $+1,654 | 52% |
| ROST | long | stop | -1.18R | $-336 | 47% |
| ANET | long | stop | -1.01R | $-758 | 45% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BA | 190.17 (10:05 iex) | +3.1% | 184.39 | 185.30 / 185.00-190.83 | 6.52 (3.5%) | 184.01-215.29 | -9.4% / -13.7% | -8.3% | 7.2M |
| BAC | 55.34 (10:05 iex) | -0.2% | 55.47 | 55.40 / 55.16-55.55 | 1.40 (2.5%) | 55.37-63.83 | -7.0% / -9.4% | -4.3% | 37.2M |
| HD | 290.35 (10:05 iex) | +0.2% | 289.89 | 290.91 / 289.27-291.83 | 6.40 (2.2%) | 289.31-326.84 | -5.5% / -10.7% | -2.5% | 4.6M |
| XLU | 39.41 (10:05 iex) | +0.4% | 39.25 | 39.16 / 39.03-39.62 | 0.57 (1.5%) | 39.06-43.39 | -5.1% / -8.4% | -3.5% | 23.9M |
| DAL | 84.38 (10:05 iex) | +0.4% | 84.03 | 85.01 / 84.10-85.32 | 2.49 (3.0%) | 75.99-85.47 | +4.9% / -0.0% | +1.9% | 7.1M |
| NVDA | 229.86 (10:05 iex) | +0.4% | 228.86 | 231.02 / 229.57-232.82 | 5.15 (2.3%) | 208.93-234.50 | +3.0% / +5.8% | +0.7% | 114.7M |
| ORCL | 133.98 (10:05 iex) | +1.0% | 132.60 | 132.86 / 132.53-134.85 | 7.25 (5.5%) | 131.58-170.70 | -10.2% / -6.9% | -10.7% | 34.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 764.96 (10:05 iex) | -0.1% | 765.61 | 766.81 / 764.63-766.98 | 6.99 (0.9%) | 747.74-775.14 | +0.2% / +0.7% | -1.0% | 44.1M |
| QQQ | 738.25 (10:05 iex) | +0.2% | 736.53 | 740.13 / 736.26-740.58 | 10.02 (1.4%) | 699.27-748.35 | +2.1% / +3.3% | -0.7% | 33.7M |
| IWM | 279.55 (10:05 iex) | -0.2% | 280.02 | 280.26 / 279.44-281.05 | 3.65 (1.3%) | 278.80-295.41 | -2.6% / -4.5% | -1.9% | 23.1M |
| DIA | 512.94 (10:04 iex) | -0.2% | 514.02 | 513.79 / 512.66-514.26 | 5.08 (1.0%) | 510.42-536.38 | -1.5% / -2.3% | -1.1% | 3.4M |
| TLT | 78.32 (10:04 iex) | -0.4% | 78.62 | 78.52 / 78.20-78.52 | 0.84 (1.1%) | 78.27-82.50 | -3.1% / -4.0% | -3.9% | 38.2M |
| GLD | 381.80 (10:05 iex) | +1.0% | 377.91 | 380.94 / 380.68-381.83 | 7.37 (2.0%) | 376.88-413.54 | -5.0% / -4.5% | -5.1% | 9.7M |
| USO | 146.57 (10:01 iex) | -2.3% | 150.01 | 145.43 / 145.17-146.67 | 5.99 (4.0%) | 132.38-163.35 | +0.5% / +10.2% | +1.2% | 6.4M |
| SMH | 609.89 (10:05 iex) | +1.6% | 600.01 | 609.20 / 604.99-610.31 | 15.76 (2.6%) | 537.73-609.66 | +5.0% / +5.9% | +0.7% | 6.4M |
| XLK | 195.26 (10:04 iex) | +0.4% | 194.53 | 196.04 / 194.47-196.10 | 3.24 (1.7%) | 181.87-196.94 | +3.1% / +5.3% | -0.2% | 6.8M |
| XLF | 54.08 (10:05 iex) | -0.2% | 54.19 | 54.17 / 54.00-54.34 | 0.74 (1.4%) | 54.14-58.39 | -3.7% / -4.6% | -3.1% | 35.1M |
| XLE | 61.58 (10:05 iex) | -0.8% | 62.10 | 61.15 / 60.95-61.78 | 1.31 (2.1%) | 61.42-65.78 | -2.5% / +0.9% | -0.6% | 33.9M |
| XLV | 169.97 (10:05 iex) | -0.8% | 171.26 | 170.55 / 170.03-171.54 | 2.12 (1.2%) | 164.48-173.82 | +1.5% / +2.3% | +1.3% | 7.6M |
| XLI | 169.40 (10:04 iex) | +0.4% | 168.78 | 169.12 / 169.01-170.48 | 2.34 (1.4%) | 167.04-175.78 | -1.2% / -4.8% | -0.7% | 7.7M |
| XLY | 108.94 (10:04 iex) | -0.1% | 109.00 | 109.35 / 108.68-109.49 | 1.60 (1.5%) | 108.91-116.88 | -3.0% / -4.8% | -2.9% | 6.3M |
| XLP | 81.80 (10:05 iex) | -0.6% | 82.28 | 81.58 / 81.44-81.81 | 0.89 (1.1%) | 81.33-85.60 | -1.0% / -2.2% | +0.4% | 10.4M |
| XLU | 39.41 (10:05 iex) | +0.4% | 39.25 | 39.16 / 39.03-39.62 | 0.57 (1.5%) | 39.06-43.39 | -5.1% / -8.4% | -3.5% | 23.9M |
| XLB | 49.25 (10:05 iex) | -0.4% | 49.47 | 49.39 / 49.18-49.55 | 0.70 (1.4%) | 48.94-53.27 | -2.6% / -3.9% | -0.5% | 11.2M |
| XLRE | 41.45 (10:04 iex) | +0.2% | 41.35 | 41.20 / 41.07-41.52 | 0.52 (1.3%) | 41.22-44.02 | -3.2% / -5.9% | -2.9% | 5.7M |
| XLC | 111.15 (10:05 iex) | -0.0% | 111.18 | 111.46 / 110.95-111.49 | 1.95 (1.8%) | 109.95-115.61 | -1.0% / +0.1% | -3.1% | 5.1M |
| KRE | 70.42 (10:05 iex) | -0.2% | 70.55 | 70.54 / 70.34-70.98 | 1.23 (1.7%) | 70.09-75.07 | -2.9% / -5.2% | -2.0% | 13.9M |
| XHB | 97.31 (10:04 iex) | +0.0% | 97.30 | 97.61 / 97.05-97.99 | 2.14 (2.2%) | 95.26-103.69 | -1.2% / -5.9% | +0.4% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 332.82 (10:05 iex) | -1.6% | 338.40 | 336.95 / 332.06-337.08 | 6.75 (2.0%) | 309.90-345.34 | +2.4% / +5.1% | -0.2% | 42.8M |
| MSFT | 504.27 (10:04 iex) | -1.0% | 509.22 | 508.47 / 502.40-509.42 | 11.26 (2.2%) | 486.00-519.40 | +1.9% / +6.6% | +1.5% | 21.4M |
| NVDA | 229.86 (10:05 iex) | +0.4% | 228.86 | 231.02 / 229.57-232.82 | 5.15 (2.3%) | 208.93-234.50 | +3.0% / +5.8% | +0.7% | 114.7M |
| AMZN | 245.49 (10:05 iex) | -0.3% | 246.15 | 246.71 / 245.15-247.41 | 5.41 (2.2%) | 244.30-264.36 | -2.8% / -3.9% | -4.8% | 34.5M |
| GOOGL | 339.63 (10:05 iex) | -0.9% | 342.75 | 341.95 / 339.45-342.84 | 8.89 (2.6%) | 327.74-364.17 | +0.2% / -0.4% | -3.4% | 26.8M |
| META | 721.12 (10:05 iex) | +0.8% | 715.62 | 725.00 / 720.05-727.50 | 31.28 (4.4%) | 555.66-779.82 | +7.2% / +16.0% | -3.5% | 23.6M |
| TSLA | 353.40 (10:05 iex) | -1.1% | 357.45 | 358.40 / 352.01-358.74 | 11.17 (3.1%) | 347.15-386.83 | -2.4% / +2.8% | -4.8% | 40.2M |
| AVGO | 359.45 (10:05 iex) | +2.8% | 349.57 | 357.00 / 355.79-361.26 | 9.69 (2.8%) | 335.20-372.07 | -2.0% / -6.9% | -3.6% | 27.7M |
| AMD | 618.49 (10:05 iex) | +1.7% | 607.87 | 616.68 / 607.70-623.95 | 26.20 (4.3%) | 440.50-639.00 | +13.6% / +19.9% | -1.2% | 22.0M |
| ORCL | 133.98 (10:05 iex) | +1.0% | 132.60 | 132.86 / 132.53-134.85 | 7.25 (5.5%) | 131.58-170.70 | -10.2% / -6.9% | -10.7% | 34.3M |
| NFLX | 70.79 (10:05 iex) | +2.3% | 69.23 | 70.33 / 70.17-71.36 | 2.05 (3.0%) | 68.88-83.60 | -9.1% / -8.4% | -5.6% | 33.1M |
| CRM | 227.03 (10:05 iex) | -0.1% | 227.27 | 227.27 / 223.43-227.55 | 8.49 (3.7%) | 221.18-267.80 | -7.8% / +6.0% | -3.9% | 13.4M |
| JPM | 335.56 (10:05 iex) | -0.3% | 336.59 | 337.00 / 335.14-338.75 | 7.25 (2.2%) | 335.28-362.86 | -3.9% / -4.7% | -4.4% | 8.0M |
| GS | 913.10 (10:04 iex) | -0.3% | 916.28 | 918.25 / 911.72-919.62 | 27.87 (3.0%) | 914.50-1,043.84 | -6.7% / -9.7% | -4.5% | 2.1M |
| BAC | 55.34 (10:05 iex) | -0.2% | 55.47 | 55.40 / 55.16-55.55 | 1.40 (2.5%) | 55.37-63.83 | -7.0% / -9.4% | -4.3% | 37.2M |
| XOM | 160.94 (10:05 iex) | -1.0% | 162.52 | 160.22 / 159.27-161.38 | 3.91 (2.4%) | 155.85-169.64 | -0.2% / +2.0% | +2.7% | 14.6M |
| CVX | 205.00 (10:05 iex) | -0.7% | 206.37 | 203.05 / 202.70-205.44 | 4.72 (2.3%) | 200.78-217.78 | -1.5% / +2.8% | +1.3% | 10.3M |
| LLY | 1,182.54 (10:05 iex) | -0.2% | 1,184.78 | 1,186.05 / 1,179.15-1,192.94 | 28.21 (2.4%) | 1,113.29-1,197.79 | +2.9% / +0.7% | +1.7% | 2.3M |
| UNH | 374.35 (10:04 iex) | -0.9% | 377.83 | 374.88 / 373.60-376.59 | 9.63 (2.5%) | 366.00-404.04 | -1.4% / -4.7% | +0.1% | 5.2M |
| JNJ | 268.38 (10:05 iex) | -1.3% | 271.95 | 269.11 / 268.42-271.89 | 4.80 (1.8%) | 260.68-281.07 | +0.8% / +2.7% | +0.9% | 6.5M |
| WMT | 106.23 (10:05 iex) | -2.3% | 108.73 | 107.75 / 105.52-107.90 | 1.86 (1.7%) | 102.84-111.23 | +1.2% / -0.4% | +1.2% | 22.6M |
| COST | 920.37 (10:04 iex) | -0.3% | 922.92 | 916.93 / 915.93-924.46 | 14.32 (1.6%) | 883.10-952.10 | +1.3% / -1.2% | +2.7% | 2.4M |
| HD | 290.35 (10:05 iex) | +0.2% | 289.89 | 290.91 / 289.27-291.83 | 6.40 (2.2%) | 289.31-326.84 | -5.5% / -10.7% | -2.5% | 4.6M |
| CAT | 824.73 (10:05 iex) | +0.6% | 819.95 | 826.53 / 821.72-829.74 | 20.69 (2.5%) | 771.39-830.50 | +1.9% / -1.0% | +0.4% | 2.4M |
| BA | 190.17 (10:05 iex) | +3.1% | 184.39 | 185.30 / 185.00-190.83 | 6.52 (3.5%) | 184.01-215.29 | -9.4% / -13.7% | -8.3% | 7.2M |
| DAL | 84.38 (10:05 iex) | +0.4% | 84.03 | 85.01 / 84.10-85.32 | 2.49 (3.0%) | 75.99-85.47 | +4.9% / -0.0% | +1.9% | 7.1M |
| UAL | 112.19 (10:05 iex) | +0.6% | 111.51 | 113.67 / 111.76-113.79 | 4.24 (3.8%) | 104.15-118.26 | +1.9% / -4.1% | -2.5% | 3.9M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-09-29 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| IOVA | 13.92 (10:05 iex) | +26.7% | 10.99 | 12.80 / 12.78-14.10 | 0.61 (5.5%) | 7.66-11.16 | +16.3% / +45.9% | +7.9% | 13.9M |
| BEX | 39.69 (10:02 iex) | +20.2% | 33.02 | 35.63 / 35.18-40.25 | 5.00 (15.1%) | 19.86-41.30 | -1.0% / +18.4% | -8.8% | 2.4M |
| AXTX | 37.53 (10:04 iex) | +19.1% | 31.50 | 33.87 / 33.10-38.39 | 5.13 (16.3%) | 17.76-38.96 | +14.8% / +1.2% | -16.3% | 2.8M |
| QURE | 25.38 (10:05 iex) | -35.1% | 39.11 | 23.85 / 22.47-26.00 | 2.08 (5.3%) | 36.82-50.97 | -11.1% / -12.1% | -11.7% | 1.4M |
