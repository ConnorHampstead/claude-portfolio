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

# Pre-market brief: Friday 2026-10-16 (09:05 ET / 15:05 Stockholm)

### 1. Tape
The sell-off has paused. ES is about +0.1–0.4% and YM +0.1–0.3%, while NQ is −0.3% because semis are still heavy (SMH −1.1% pre-market, heading for a ninth straight losing session). Thursday's strength was broad. The S&P rose +0.33% and the Nasdaq was flat, but the equal-weight S&P gained +1.36%. Energy has passed +50% YTD and healthcare is at records (verified: Fortune, Yahoo live blog). Overnight in Bangkok, Fed Chair Warsh gave no signal of an October hike. CME odds of a hold are now about 85%, up from about 65% earlier in the week. The 10-year is at about 5.07–5.09%, well below this week's 5.3% peak. Hot inflation data keeps arriving all the same: September import prices were +1.1% m/m and +8.1% y/y. **Regime:** money is rotating out of AI and long-duration tech and into defensives, energy and the broader equal-weight market. Hike fear is easing, which takes pressure off the rate-sensitive groups. **Edge today: long the rotation (healthcare, staples, housing). Short only the specific AI-credit names, not the index.**

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| Overnight | — | Warsh at IMF, Bangkok | No signal of an October hike; "won't prejudge" October/December. Hold odds about 85% | All; IWM short (bullish small caps) |
| 08:30 | 14:30 | Sep import/export prices | **Import +1.1% m/m, +8.1% y/y**, largest since 2022 (fuel +4.8%); export +2.2%. I didn't verify the consensus. Futures barely moved | Rates, XLE |
| 09:15 | 15:15 | Sep industrial production / capacity utilization | Consensus +0.4% m/m (manufacturing +0.3%) | XLI, CAT |
| BMO | — | TRV beat but −4%; TFC missed ($1.16 vs $1.19), −2%; AA (reported Thursday AMC) +2% | — | XLF / KRE (not held) |
| Next week | — | NFLX 10/20 AMC; TSLA and META next week | — | Rule 8 blocks NFLX/TSLA |

Thursday's jobless claims were 199K against 197K prior. Today is a Friday: the harness clears unfilled resting entries before the weekend, so new stop or limit entries only live for today's session.

### 3. Open positions and resting entries
- **IWM short (272.99, stop 275.60, target 267): invalidated. Close at market.** Yesterday's brief set 274.50 as the line where the thesis dies. IWM closed at 275.08 and trades 275.44 pre-market, just 0.16 under the stop. The rates premise behind the trade has also reversed: Warsh took October off the table and the 10-year is about 20 bp off its peak. Equal-weight +1.36% is exactly the small-cap rotation I named as the risk. Closing at about −0.54R versus a stop fill at −0.58R saves little money. The point is that I don't hold a position whose thesis I have already declared dead. `manage` close.
- **HD buy stop 310.60 / 303 / 322: keep.** Pre-market is 309.81 and the 20d high is 309.10, so it is about to trigger. Easing yields and the hold odds support housing. If it fills, the stop is 1.2 ATR away.
- **WMT limit 117.50 / 115.20 / 122.10: keep.** Pre-market is 118.18, about 0.3 ATR above the limit. The staples thesis is intact (XLP +0.4% pre-market). It gets cleared tonight if unfilled.
- **CAT short limit 745 / 772 / 700: keep through today, then let it expire.** Pre-market is 731 and the limit needs a +1.9% bounce. The industrial production print at 09:15 could produce one. The thesis (AI capex unwind) is unchanged, and the order dies at the weekend clear either way.

### 4. New plays

**XLV long (buy-stop breakout)**

| Field | Value |
|---|---|
| Ticker | XLV |
| Direction | Long |
| Catalyst | Healthcare at record highs (2026-10-15) as money rotates out of tech; Warsh's no-hike-signal on 10/16 eases pressure on defensives' valuations |
| Thesis | Healthcare has been the main recipient of this week's money leaving tech: +5.4% in 5 days, +2.6% intraday yesterday. A move through the 178.86 20d high, set during yesterday's spike, would confirm the leadership is continuing rather than fading. |
| Entry | Buy stop 179.10 (pre-market 177.70, so the trigger is valid) |
| Stop | 175.40: below yesterday's 177.19 close; a fill followed by a drop back under it means the breakout failed. 3.70 ≈ 1.25 ATR |
| Target | 184.60 (1.49R) |
| Risk tier | 0.5: buying strength after +5.4% in 5 days, 4.4% above the 20d average |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 40% |
| Invalidation | Semis/AI bounce hard and money rotates back into tech, so XLV leads on the downside |
| What I'd be wrong about | Yesterday's 178.86 high was a spike that faded into the close (177.19). It may be a blow-off top, and the breakout may trigger once and then reverse. |

Why a buy stop and not a limit: the gap-fill lesson from ROST and ANET says to buy confirmation, not catch a level. A limit would sit inside a range that just rejected. The 184.60 target is only about 3% above the trigger, which fits a 5-day holding window for a sector that has moved 5% in 5 days.

**ORCL short (breakdown probe)**

| Field | Value |
|---|---|
| Ticker | ORCL |
| Direction | Short |
| Catalyst | AI-credit stress. S&P cut ORCL to BBB-, one notch above junk. Debt is about $169B, CDS sit near 2008 highs, and CoreWeave is −4% pre-market on the same leverage worries (10/14–10/16) |
| Thesis | ORCL is the large-cap name most exposed to the market pricing AI build-out credit risk. It fell −8.8% on 10/14, partly retraced, and is −0.9% pre-market at 133.20. A break below the 130 support named in coverage would open the way to new lows. |
| Entry | Sell stop 129.80 (pre-market 133.20, so the trigger is valid) |
| Stop | 137.40: above the retrace zone and pre-market level; 7.60 ≈ 1.1 ATR (ATR is 5.1%) |
| Target | 116.50 (1.75R) |
| Risk tier | 0.25 (probe): very volatile, the downgrade is already in the price, and short-covering risk is high after a 9% day |
| Time horizon | 1–5 days |
| Conviction | 2 |
| P(target before stop) | 33% |
| Invalidation | ORCL holds 130 into the close, or it announces a credit-positive financing (an Apollo/Goldman deal on equity-friendly terms) |
| What I'd be wrong about | The bad news is well known and the stock found buyers after 10/14. A financing announcement or a semis bounce could squeeze it 10% fast. |

Earnings check: ORCL's fiscal Q2 report falls in December, outside the holding window (inferred from its usual calendar, not verified for 2026).

### 5. Both sides
- **Best long:** XLV breakout, 179.10 / 175.40 / 184.60, P 40%. Taken at 0.5.
- **Best short:** ORCL breakdown, 129.80 / 137.40 / 116.50, P 33%. Taken as a 0.25 probe. I also looked at the SMH, NVDA and AMD shorts. They are on the right side, but SMH is in its ninth down day and I already banked that factor at target on 10/15, so I passed (see below).

### 6. Passing on
- **SMH short, limit 566 / stop 584 / target 535, P 35%:** nine straight down days. I'd only sell a bounce, and the factor has already paid me once.
- **XLE long, buy stop 68.00 / stop 66.00 / target 71.50, P 35%:** Brent is at $105 and the sector is +50% YTD. Yesterday XOM reversed from 178.63 down to 175.50 intraday, a sign of exhaustion near the highs.
- **TSLA long:** +2.9% pre-market on the Roadster news, but its earnings come next week inside the holding window (rule 8; I didn't verify the date). No levels given.
- **NFLX short:** −3.5% pre-market after the layoffs and the content-chief exit, but it reports 10/20 AMC. Rule 8.
- **CRWV short:** I couldn't verify a price, so it is excluded.

### 7. For the post-open review
- **IWM:** confirm the market close filled.
- **HD:** if the buy stop triggers and HD falls back below 307 by 10:00, close it as a failed breakout.
- **XLV:** if XLV opens below 176.50 and healthcare leads the losers (tech bounces), cancel the buy stop.
- **ORCL:** if ORCL opens above 136 on an AI/semis bounce, cancel the sell stop.
- **CAT:** if the 09:15 industrial production print is strong and CAT trades above 750, cancel the limit.

### 8. Book state
After closing IWM and assuming every resting entry and new play fills: gross is about 72% of equity (cap 150%) and net about +50% (cap ±100%). The largest sector is healthcare at about 26% (cap 40%). Risk at stake is about 1.75% of equity (cap 4%), with 6 of 8 slots used.

```json
{
  "date": "2026-10-16",
  "no_trade": false,
  "session_note": "Sell-off paused: Warsh no-hike signal, yields off peak, equal-weight rotation into healthcare/staples/housing. Closing the invalidated IWM short, adding an XLV breakout and an ORCL credit-breakdown probe.",
  "plays": [
    {
      "ticker": "XLV",
      "direction": "long",
      "entry_type": "stop",
      "entry": 179.10,
      "stop": 175.40,
      "targets": [184.60],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.40,
      "catalyst": "Healthcare at record highs 2026-10-15 on rotation out of tech; Warsh no-hike signal 10/16.",
      "thesis": "Healthcare is the primary recipient of this week's money leaving tech. A move through the 178.86 20d high confirms the leadership is continuing rather than fading.",
      "invalidation": "Semis/AI bounce hard and money rotates back to tech, XLV leading on the downside.",
      "bear_case": "Yesterday's 178.86 high was a spike that faded to 177.19; possible blow-off, and the breakout may trigger then reverse."
    },
    {
      "ticker": "ORCL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 129.80,
      "stop": 137.40,
      "targets": [116.50],
      "time_horizon": "1-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.33,
      "catalyst": "AI-credit stress 10/14-10/16: S&P cut to BBB-, ~$169B debt, CDS near 2008 highs, CoreWeave -4% premarket.",
      "thesis": "ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the way to new lows below the 127.60 20d low.",
      "invalidation": "Holds 130 into the close, or announces credit-positive financing.",
      "bear_case": "The bad news is well known and buyers stepped in after the -8.8% day; a financing headline or semis bounce could squeeze it 10%."
    }
  ],
  "manage": [
    {
      "ticker": "IWM",
      "action": "close",
      "reason": "Thesis invalidated: closed 275.08 above the 274.50 invalidation line; Warsh took October hike off the table and equal-weight/small caps are leading."
    }
  ],
  "passed": [
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "limit",
      "entry": 566.00,
      "stop": 584.00,
      "targets": [535.00],
      "p_target_first": 0.35,
      "reason": "Ninth straight down day; factor already banked at target 10/15; only a bounce sale would make sense."
    },
    {
      "ticker": "XLE",
      "direction": "long",
      "entry_type": "stop",
      "entry": 68.00,
      "stop": 66.00,
      "targets": [71.50],
      "p_target_first": 0.35,
      "reason": "Energy +50% YTD with Brent at $105; XOM's intraday reversal from its high yesterday suggests exhaustion."
    }
  ]
}
```

Sources: [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-16-2026), [Yahoo live](https://finance.yahoo.com/markets/live/stock-market-today-dow-sp-500-nasdaq-futures-mixed-amid-volatile-week-112939401.html), [Fortune](https://fortune.com/2026/10/16/bloodletting-stocks-stanched-investors-buy-dip-rotate-out-of-tech/), [CNBC premarket movers](https://www.cnbc.com/2026/10/16/stocks-making-the-biggest-moves-premarket-tsla-spcx-aa-crwv.html), [CNBC Warsh](https://www.cnbc.com/2026/10/16/feds-warsh-says-ai-development-path-will-be-very-bumpy-.html), [Bloomberg Warsh](https://www.bloomberg.com/news/articles/2026-10-16/warsh-boosts-market-expectations-of-fed-hold-in-october), [IndexBox import prices](https://www.indexbox.io/blog/us-import-and-export-prices-rise-sharply-in-september-2026/), [ADM day ahead](https://www.admisi.com/macroeconomics-the-day-ahead-for-16-october-2026/), [Yahoo Oracle debt](https://finance.yahoo.com/technology/ai/articles/oracle-courts-apollo-goldman-ai-072925320.html), [Startup Fortune S&P downgrade](https://startupfortune.com/sps-downgrade-leaves-oracle-financing-openais-bet-years-before-it-pays-off/), [FX Leaders ORCL 130](https://www.fxleaders.com/news/2026/10/14/oracle-stock-orcl-breaks-130-support-as-coreweave-debt-concerns-rattle-ai-cloud-stocks/), [24/7 Wall St NFLX](https://247wallst.com/investing/2026/10/16/netflix-is-cutting-about-1000-jobs-and-its-content-chief-is-out-days-before-earnings/)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Friday 2026-10-16. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$101,821.04**
- Cash: $91,506.23
- Session P&L so far: +0.02% (new entries are blocked at -3.0%)
- Gross exposure: $71,925 (71% of equity, cap 150%)
- Net exposure: $+49,948 (+49%, cap +/-100%)
- Risk at stake (entry to stop): $1,765 (1.73% of equity, cap 4.0%) — 2.27% left for new plays
- Slots: 1 open + 4 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| HD | long | 33 | 310.70 | 312.57 | +62 (+0.6%) | 303.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| ORCL | short | 33 | 129.80 | stop | 137.40 | 116.50 | 2026-10-16 |
| XLV | long | 137 | 179.10 | stop | 175.40 | 184.60 | 2026-10-16 |
| CAT | short | 9 | 745.00 | limit | 772.00 | 700.00 | 2026-10-15 |
| WMT | long | 222 | 117.50 | limit | 115.20 | 122.10 | 2026-10-15 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 18.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |

### Ideas you passed on, replayed against the tape

42 resolved: 9 reached target first, 25 stop first, 7 never reached the entry, 1 expired, 0 ambiguous. Average -0.35R across the 35 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-14 pre-market | BAC | short | Already -7.5% on the earnings miss; shorting the gap low. Review may short a fai | stop | -1.05R | 33% |
| 2026-10-13 open | JPM | short | Fading its gap after an EPS miss, but close to the 324 20-day low with little ro | stop | -0.82R | 33% |
| 2026-10-14 open | XHB | short | Morning play rejected by broker: not shortable. | stop | -0.73R | 37% |
| 2026-10-09 pre-market | XLE | long | Energy +4.1% over 5d and de-escalation removes the bid; wrong day to buy the dip | never filled | - | 35% |
| 2026-10-09 open | NVDA | long | Withdrawn after the open: semis faded the whole rebound, invalidating the follow | never filled | - | 30% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| HD | 312.58 (10:04 iex) | +1.4% | 308.24 | 309.66 / 308.32-314.57 | 6.45 (2.1%) | 277.15-309.10 | +5.6% / -1.5% | +4.3% | 5.8M |
| ORCL | 132.38 (10:05 iex) | -1.6% | 134.47 | 133.49 / 131.37-133.80 | 6.85 (5.1%) | 127.60-153.03 | -4.0% / -7.2% | -0.5% | 30.7M |
| XLV | 177.84 (10:04 iex) | +0.4% | 177.19 | 178.20 / 177.25-178.28 | 2.96 (1.7%) | 165.19-178.86 | +4.4% / +4.6% | +5.4% | 8.6M |
| CAT | 741.59 (10:02 iex) | +0.8% | 735.64 | 734.36 / 730.00-742.55 | 30.24 (4.1%) | 704.01-876.95 | -9.1% / -9.8% | -7.6% | 2.6M |
| WMT | 119.08 (10:05 iex) | +1.0% | 117.87 | 118.07 / 118.07-119.48 | 2.57 (2.2%) | 103.39-121.38 | +8.1% / +8.4% | +6.6% | 22.9M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 771.43 (10:05 iex) | -0.0% | 771.79 | 773.24 / 771.02-773.25 | 6.53 (0.8%) | 757.97-781.62 | +0.1% / +0.6% | -0.3% | 42.2M |
| QQQ | 721.50 (10:05 iex) | -0.9% | 728.00 | 725.52 / 720.28-725.96 | 9.52 (1.3%) | 714.34-762.86 | -2.0% / +0.2% | -2.6% | 35.2M |
| IWM | 275.03 (10:05 iex) | -0.0% | 275.08 | 275.52 / 274.87-275.91 | 3.76 (1.4%) | 270.35-288.94 | -1.8% / -4.9% | -0.9% | 26.0M |
| DIA | 524.43 (10:03 iex) | +0.6% | 521.07 | 522.90 / 522.26-525.02 | 4.99 (1.0%) | 504.59-522.69 | +1.3% / -0.5% | +1.9% | 3.3M |
| TLT | 80.14 (10:05 iex) | +0.2% | 79.97 | 79.69 / 79.67-80.24 | 0.87 (1.1%) | 76.43-81.61 | +1.6% / -0.6% | +2.7% | 50.1M |
| GLD | 383.51 (10:04 iex) | +0.2% | 382.71 | 381.34 / 381.07-384.29 | 6.03 (1.6%) | 373.36-403.15 | -0.7% / -3.7% | +1.1% | 7.8M |
| USO | 156.34 (10:04 iex) | -0.6% | 157.31 | 156.97 / 156.31-157.68 | 4.80 (3.0%) | 141.76-158.10 | +5.7% / +10.9% | +6.6% | 5.4M |
| SMH | 549.51 (10:05 iex) | -1.7% | 558.84 | 551.28 / 547.00-553.31 | 15.37 (2.8%) | 540.59-639.47 | -7.3% / -3.6% | -8.0% | 7.1M |
| XLK | 186.64 (10:05 iex) | -1.3% | 189.19 | 188.34 / 186.18-188.54 | 3.26 (1.7%) | 184.84-203.25 | -3.5% / -0.3% | -4.3% | 7.8M |
| XLF | 55.87 (10:05 iex) | +1.1% | 55.27 | 55.59 / 55.55-56.02 | 0.69 (1.2%) | 52.81-56.20 | +1.5% / -1.7% | +1.9% | 39.1M |
| XLE | 67.26 (10:05 iex) | +1.1% | 66.56 | 67.11 / 67.02-67.56 | 1.28 (1.9%) | 60.95-67.90 | +4.5% / +5.5% | +2.0% | 32.3M |
| XLV | 177.84 (10:04 iex) | +0.4% | 177.19 | 178.20 / 177.25-178.28 | 2.96 (1.7%) | 165.19-178.86 | +4.4% / +4.6% | +5.4% | 8.6M |
| XLI | 169.35 (10:05 iex) | +0.9% | 167.89 | 168.23 / 167.90-169.73 | 2.56 (1.5%) | 164.66-172.34 | -0.7% / -3.6% | -0.3% | 7.4M |
| XLY | 114.35 (10:04 iex) | +0.8% | 113.41 | 114.41 / 113.92-114.68 | 1.31 (1.2%) | 107.99-113.56 | +2.2% / -0.4% | +1.5% | 6.4M |
| XLP | 87.74 (10:05 iex) | +1.2% | 86.68 | 87.34 / 87.22-87.86 | 1.16 (1.3%) | 80.10-88.47 | +5.0% / +3.6% | +3.9% | 11.5M |
| XLU | 42.15 (10:05 iex) | +1.2% | 41.65 | 41.84 / 41.62-42.17 | 0.66 (1.6%) | 39.03-42.20 | +2.8% / -0.5% | +1.4% | 35.2M |
| XLB | 51.31 (10:05 iex) | +1.5% | 50.56 | 50.87 / 50.80-51.49 | 0.74 (1.5%) | 47.81-50.70 | +2.1% / -1.0% | +2.6% | 11.7M |
| XLRE | 42.35 (10:05 iex) | +0.9% | 41.99 | 42.17 / 42.00-42.36 | 0.60 (1.4%) | 40.28-42.67 | +1.2% / -2.2% | +2.8% | 7.3M |
| XLC | 112.04 (10:05 iex) | -0.4% | 112.44 | 112.67 / 111.91-112.90 | 1.57 (1.4%) | 109.66-115.61 | +0.6% / +0.7% | +0.3% | 6.7M |
| KRE | 70.59 (10:05 iex) | +1.2% | 69.75 | 70.09 / 69.94-70.92 | 1.30 (1.9%) | 67.79-72.87 | -0.6% / -4.2% | +0.2% | 15.8M |
| XHB | 97.23 (10:02 iex) | +1.5% | 95.75 | 95.83 / 95.57-97.23 | 2.17 (2.3%) | 91.87-99.67 | -0.5% / -4.8% | +0.1% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 344.07 (10:05 iex) | +0.6% | 342.00 | 346.06 / 342.03-347.82 | 6.52 (1.9%) | 325.81-348.15 | +1.5% / +5.2% | +0.5% | 38.5M |
| MSFT | 536.87 (10:05 iex) | -0.5% | 539.44 | 541.31 / 534.84-543.82 | 11.35 (2.1%) | 491.10-551.15 | +4.0% / +6.9% | +3.2% | 23.1M |
| NVDA | 216.41 (10:05 iex) | -0.4% | 217.23 | 216.56 / 215.07-216.80 | 5.96 (2.7%) | 212.85-243.37 | -5.0% / -2.6% | -5.7% | 109.6M |
| AMZN | 253.27 (10:05 iex) | -0.6% | 254.76 | 255.09 / 252.90-255.54 | 5.76 (2.3%) | 244.72-263.70 | +0.5% / -1.1% | +0.3% | 36.4M |
| GOOGL | 344.36 (10:04 iex) | -1.4% | 349.22 | 348.01 / 344.17-350.66 | 8.45 (2.4%) | 335.51-364.17 | +0.7% / +1.3% | +0.3% | 26.2M |
| META | 727.79 (10:05 iex) | -1.2% | 736.72 | 736.16 / 726.17-738.49 | 22.31 (3.0%) | 660.28-779.82 | +0.4% / +12.9% | +2.2% | 22.2M |
| TSLA | 368.38 (10:05 iex) | +1.6% | 362.44 | 369.14 / 363.45-370.58 | 10.44 (2.9%) | 345.88-388.56 | -2.3% / +1.0% | -3.3% | 34.2M |
| AVGO | 338.17 (10:05 iex) | -1.8% | 344.33 | 338.49 / 336.22-339.59 | 11.29 (3.3%) | 334.61-380.84 | -3.5% / -6.2% | -4.4% | 23.1M |
| AMD | 544.59 (10:05 iex) | -3.1% | 562.23 | 547.23 / 540.40-550.96 | 26.22 (4.7%) | 530.09-658.52 | -8.1% / +4.8% | -9.4% | 21.8M |
| ORCL | 132.38 (10:05 iex) | -1.6% | 134.47 | 133.49 / 131.37-133.80 | 6.85 (5.1%) | 127.60-153.03 | -4.0% / -7.2% | -0.5% | 30.7M |
| NFLX | 71.24 (10:05 iex) | -1.9% | 72.61 | 69.86 / 69.76-71.90 | 1.65 (2.3%) | 66.54-73.87 | +3.2% / -3.4% | +1.5% | 38.7M |
| CRM | 244.18 (10:04 iex) | -1.0% | 246.74 | 250.57 / 243.94-251.94 | 8.43 (3.4%) | 220.29-247.18 | +5.9% / +7.8% | +8.3% | 9.7M |
| JPM | 341.34 (10:05 iex) | +1.7% | 335.53 | 339.45 / 338.25-343.75 | 5.96 (1.8%) | 324.25-352.74 | +0.1% / -3.3% | +1.2% | 8.7M |
| GS | 899.98 (10:05 iex) | +1.0% | 891.28 | 895.89 / 894.00-909.87 | 21.45 (2.4%) | 859.03-967.76 | -2.0% / -8.7% | +1.0% | 2.4M |
| BAC | 52.11 (10:05 iex) | +0.8% | 51.70 | 52.14 / 51.73-52.34 | 1.25 (2.4%) | 49.26-58.28 | -5.5% / -12.6% | -3.6% | 42.0M |
| XOM | 176.00 (10:03 iex) | +0.8% | 174.68 | 176.49 / 175.44-177.37 | 3.41 (2.0%) | 155.85-178.69 | +5.6% / +7.1% | +3.7% | 13.0M |
| CVX | 222.10 (10:05 iex) | +1.3% | 219.32 | 221.85 / 220.41-223.41 | 4.35 (2.0%) | 200.78-223.46 | +5.0% / +6.4% | +3.7% | 9.4M |
| LLY | 1,267.00 (10:04 iex) | +1.2% | 1,251.61 | 1,256.00 / 1,255.01-1,267.00 | 37.08 (3.0%) | 1,131.21-1,275.88 | +6.7% / +6.2% | +7.0% | 2.4M |
| UNH | 400.08 (10:05 iex) | -1.6% | 406.67 | 410.35 / 395.52-412.37 | 11.93 (2.9%) | 362.60-414.12 | +7.8% / +5.3% | +9.6% | 6.0M |
| JNJ | 257.01 (10:05 iex) | +1.5% | 253.28 | 255.52 / 254.13-257.27 | 6.46 (2.6%) | 245.17-275.23 | -3.4% / -4.4% | -1.2% | 7.9M |
| WMT | 119.08 (10:05 iex) | +1.0% | 117.87 | 118.07 / 118.07-119.48 | 2.57 (2.2%) | 103.39-121.38 | +8.1% / +8.4% | +6.6% | 22.9M |
| COST | 986.22 (10:05 iex) | +0.8% | 978.01 | 982.86 / 980.66-987.59 | 16.24 (1.7%) | 883.10-1,008.37 | +5.3% / +4.8% | +3.2% | 2.4M |
| HD | 312.58 (10:04 iex) | +1.4% | 308.24 | 309.66 / 308.32-314.57 | 6.45 (2.1%) | 277.15-309.10 | +5.6% / -1.5% | +4.3% | 5.8M |
| CAT | 741.59 (10:02 iex) | +0.8% | 735.64 | 734.36 / 730.00-742.55 | 30.24 (4.1%) | 704.01-876.95 | -9.1% / -9.8% | -7.6% | 2.6M |
| BA | 191.50 (10:05 iex) | +1.5% | 188.73 | 190.12 / 189.18-191.90 | 5.55 (2.9%) | 183.38-204.06 | -1.6% / -8.5% | +0.5% | 8.6M |
| DAL | 78.48 (10:04 iex) | +0.5% | 78.08 | 78.07 / 78.07-79.00 | 2.46 (3.1%) | 75.54-85.93 | -4.8% / -5.3% | -4.7% | 8.4M |
| UAL | 102.19 (10:03 iex) | +0.9% | 101.31 | 101.25 / 101.25-102.75 | 3.73 (3.7%) | 97.70-118.26 | -7.4% / -10.0% | -5.7% | 4.5M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-16 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| NBIZ | 33.40 (10:01 iex) | +12.5% | 29.68 | 31.95 / 31.77-33.90 | 3.29 (11.1%) | 17.01-37.98 | +32.8% / +7.1% | +31.2% | 2.2M |
| CWVX | 7.85 (09:58 iex) | -14.6% | 9.19 | 8.00 / 7.62-8.15 | 1.79 (19.4%) | 6.65-17.26 | -35.0% / -42.6% | -30.0% | 1.9M |
| CRWG | 9.32 (10:05 iex) | -15.2% | 10.99 | 9.59 / 9.22-9.76 | 2.15 (19.6%) | 7.96-20.68 | -35.1% / -42.8% | -30.2% | 3.4M |
| OMER | 16.08 (10:05 iex) | -14.4% | 18.79 | 17.94 / 16.05-17.94 | 0.73 (3.9%) | 17.68-21.24 | -2.1% / +3.1% | -1.7% | 1.2M |
| TLK | 11.04 (10:04 iex) | -13.7% | 12.78 | 10.86 / 10.60-11.17 | 0.26 (2.0%) | 12.38-14.28 | -2.2% / -9.5% | -0.8% | 1.2M |
| EIDO | 10.12 (10:04 iex) | -13.4% | 11.68 | 9.99 / 9.98-10.12 | 0.16 (1.3%) | 11.52-12.49 | -1.9% / -5.9% | +0.1% | 1.2M |
| CCOI | 7.26 (10:05 iex) | -13.1% | 8.35 | 8.12 / 7.23-8.14 | 0.76 (9.2%) | 7.13-10.30 | -1.5% / -10.2% | -12.7% | 2.2M |
