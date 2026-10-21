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

# Pre-market brief: Wednesday 2026-10-21

*Written at 09:05 ET (15:05 Stockholm). Stockholm is ET+6 today. The cash session opens at 09:30 ET (15:30 Stockholm).*

### 1. Tape
Futures are mildly bid: NQ +0.5%, ES +0.2%, Dow flat (TipRanks, 05:35 ET). Yesterday the Dow closed +1.02% at 52,496 and the S&P +0.28% at 7,712.57, while the Nasdaq slipped 0.02% (verified, Yahoo). The rally ran through healthcare, biotech and industrials while mega-cap tech lagged.

Overnight brought two pieces of AI-demand news. Super Micro raised its fiscal-Q1 revenue guide to $18.5–19.5B from $14.5–15.5B and is +12–13% pre-market. SpaceX is +8–10% on 161% revenue growth and talk of a merger with Tesla. Semis are catching a bid: SMH +1.5%, AMD +1.8%, NVDA +1.8% (Alpaca). That cuts directly against my AI-credit shorts.

Elsewhere:
- **NFLX** is −6.7% at 64.07 after a weak Q4 guide and an ad-revenue cut to about $2.7B from $3B. That is below its 20-day low of 66.54.
- **ISRG** is −6 to −8% (antitrust charge, warning on 2027 pricing), **T** −4.6% and **TMO** −2.5%. Healthcare is soft pre-market (XLV −0.9%) and staples are lower (XLP −0.7%).
- **Brent** is about $110 (+1.4%) on attacks on tankers near Hormuz and on Saudi facilities.
- **Rates and vol:** the 10-year is about 5.10–5.12% and roughly flat. VIX is about 17.4.

The regime is still a rotation away from AI capex, but today opens with a counter-move into semis, and META, TSLA, LRCX, TXN and IBM all report tonight. **Edge today:** long energy and short the single-name losers from earnings (NFLX). I am not adding to AI shorts into tonight's reports.

### 2. Calendar
| Time ET / Stockholm | Event | Status / consensus | Touches |
|---|---|---|---|
| BMO | T, TMO, others | Out. **T:** EPS beat (0.65 vs 0.60), raised guidance, but postpaid phone adds of 379K missed 387K; stock −4.6%. **TMO:** beat ($6.68 vs $6.40, revenue $12.14B), stock −2.5% | none |
| BMO (Tue AMC) | NFLX, SMCI (pre-announcement), ISRG, SpaceX | Out. NFLX −6.7%, SMCI +12%, ISRG −6 to −8%, SpaceX +8% | NFLX (new short); SMCI hurts the AMD/NVDA/ORCL shorts |
| 10:30 / 16:30 | EIA crude inventories | Prior −8.56M | CVX, XOM |
| 13:00 / 19:00 | 20-year bond auction | Prior 5.42% | HD (rates) |
| AMC 16:00+ / 22:00+ | META (implied ±6.7%), TSLA (±5.9%), LRCX, TXN, IBM | Ahead | AMD, ORCL, NVDA by sentiment. These are other companies' reports, so not binary under rule 8, but they are the main overnight risk to the AI shorts |
| Thu 08:30 / 14:30 | Initial jobless claims | Consensus 200K | all |
| Fri 09:45 / 15:45 | S&P flash PMIs | Services 58.0, manufacturing 55.5 | all |

No Fed speakers were found in the calendar feed. I could not verify whether any are scheduled.

### 3. Open positions and resting entries
- **AMD short** (entry 542.20, last about 544.2, stop 558, target 512)
  - **Thesis: weakening.** SMCI's huge guidance raise is hard evidence of AI demand, and semis are bid.
  - Stop 558 is structural (above last week's breakdown area) and the position risks only about 0.3% of equity. **Hold.**
  - The review should cut it if AMD trades above 552 at 10:05 (details in section 7).
  - The overnight risk is a META capex raise tonight.
- **ORCL short** (entry 129.70, last 132.7, stop 137.40, target 116.50)
  - **Thesis: weakening, not broken.** ORCL is still under its 20-day and 50-day averages.
  - The stop is above the 135–137 shelf. **Hold** unchanged.
- **CVX long** (entry 224.48, last 225.5, stop 218, target 236)
  - **Thesis: intact.** Brent is back at $110 on a fresh supply threat.
  - EIA at 10:30 is the near-term swing. **Hold** unchanged.
- **HD long** (entry 310.70, last about 316, stop 307, target 322)
  - **Thesis: intact.** HD is +7.2% over five days and sits just under its 20-day high of 317.71.
  - **Raise the stop to 309.00.** That is about 1 ATR under last, and it turns the trade into roughly breakeven-or-better while leaving room for the 20-year auction. Target 322 is unchanged.
- **NVDA resting sell-stop** at 212.40 (stop 222, target 198)
  - NVDA is at 220.40, so the trigger is 3.6% away. It only fires on a real breakdown under the 20-day low of 212.77, which would be the thesis confirming itself.
  - **Keep.**

AI-short cluster risk: AMD about $300 plus ORCL about $254 plus NVDA about $250 (if triggered) ≈ 0.8% of equity, all on the same factor. That is acceptable, but I will not add more of it.

### 4. New plays

**NFLX short**

| Field | Value |
|---|---|
| Ticker | NFLX |
| Direction | Short |
| Catalyst | Q3 report 2026-10-20 AMC: Q4 guide disappointed, 2026 ad-revenue target cut from about $3B to about $2.7B; −6.7% pre-market |
| Thesis | A guidance cut that gaps the stock below its 20-day range (low 66.54) tends to keep drifting lower as estimates come down. The ad business was the growth story, and it is the piece being cut. A break under the pre-market level confirms that sellers control the open. |
| Entry | Sell-stop at 63.40, below pre-market 64.07 |
| Stop | 66.60. That reclaims the old 20-day low and fills most of the gap; above it the gap is failing. |
| Target | 59.00 (≈1.4R) |
| Risk tier | 0.5. It is post-event and gap-prone, and a reflex bounce is possible. |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 42% |
| Invalidation | A close back above 66.5, or sell-side defending the quarter on day one with upgrades |
| What I'd be wrong about | A 6–7% gap can already price the guide. Day-one gap-downs in mega-caps often bounce, and a stop 5% away gives up a lot if it does. |

The sell-stop means I only get short if the open confirms weakness rather than bouncing. If NFLX bounces from the open, the order sits unfilled and costs nothing.

**XOM long, breakout**

| Field | Value |
|---|---|
| Ticker | XOM |
| Direction | Long |
| Catalyst | Brent back at $110 on 2026-10-21 after attacks on tankers near Hormuz and on Saudi facilities; EIA inventories at 10:30 ET |
| Thesis | Energy is still the leading sector: XLE is +5.4% over its 20-day average and USO +11% over its 50-day. XOM is 1.3% under its 20-day high of 180.26, and a break through it with oil at a 5-month high extends the trend. |
| Entry | Buy-stop at 180.60, above the 20-day high; last 177.91 |
| Stop | 175.40. That is about 1.45 ATR below the trigger, under the breakout zone and back inside the range. |
| Target | 189.00 (≈1.6R) |
| Risk tier | 0.5. It is correlated with the CVX long, and oil is headline-driven both ways. |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 37% |
| Invalidation | Brent back below $105 on de-escalation or US–Iran talks |
| What I'd be wrong about | Monday showed that oil gives back gains quickly on diplomacy headlines. Breakouts at a 5-month oil high can mark the blow-off rather than the start. |

With this fill, energy exposure would be about $34k, or 33% of equity, under the 40% sector cap.

### 5. Both sides
- **Best long:** XOM buy-stop at 180.60, stop 175.40, target 189, P = 37%. Taken.
- **Best short:** NFLX sell-stop at 63.40, stop 66.60, target 59, P = 42%. Taken.

On the short side I also looked at ISRG, T and the semis. For the semis, I am already short three AI names and SMCI argues against adding a fourth.

### 6. Passing on
- **UNH long, buy-stop 423 / stop 410 / target 445, P = 35%:** healthcare is soft pre-market on ISRG and TMO. I would rather spend the risk on energy. Goes in `passed`.
- **ISRG short:** it is not in the Alpaca table and I could not verify a live price, so it is excluded.
- **T short:** same problem, no verified level. Excluded.
- **META and TSLA:** they report tonight (rule 8), and a trade on the event itself would be a coin flip.
- **SMCI long, chasing +12%:** a gap chase in a name with a weak governance history.

### 7. For the post-open review
- **AMD:** if it is above 552 at 10:05 with SMH holding +1.5% or better, close it before tonight's META and LRCX reports. Below 540, hold.
- **NFLX:** if the sell-stop has not triggered and NFLX is reclaiming 66 or more, cancel it. If it is filled and trading under 63, hold.
- **CVX and XOM:** if Brent is below $107 by 10:05, cancel the XOM buy-stop.
- **HD:** hold above 309. Nothing to do unless it is back below entry.

### 8. Book state
- **Exposure if everything fills (including the NVDA trigger):** gross about $48k + $16k (NFLX) + $16k (XOM) ≈ $80k, about 79% of the 150% cap. Net is roughly +8%.
- **Risk at stake:** about 1.41% + 0.5% + 0.5% − about 0.05% saved on HD ≈ 2.36% of the 4% cap. 7 of 8 slots used.

```json
{
  "date": "2026-10-21",
  "no_trade": false,
  "session_note": "SMCI guide raise lifts semis against the AI-credit shorts; holding them but not adding into META/LRCX tonight. Adding NFLX post-guidance breakdown short and XOM breakout long with Brent at $110; HD stop raised.",
  "plays": [
    {
      "ticker": "NFLX",
      "direction": "short",
      "entry_type": "stop",
      "entry": 63.40,
      "stop": 66.60,
      "targets": [59.00],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.42,
      "catalyst": "Q3 report 2026-10-20 AMC: weak Q4 guide and 2026 ad revenue cut to ~$2.7B from ~$3B; -6.7% pre-market below 20d low 66.54.",
      "thesis": "Guidance-cut gap below the 20-day range tends to drift lower as estimates reset. A break under pre-market levels confirms sellers own the open.",
      "invalidation": "Close back above 66.5 or day-one sell-side defense with upgrades.",
      "bear_case": "A 6-7% gap may fully price the guide; mega-cap day-one gaps often bounce."
    },
    {
      "ticker": "XOM",
      "direction": "long",
      "entry_type": "stop",
      "entry": 180.60,
      "stop": 175.40,
      "targets": [189.00],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.5,
      "p_target_first": 0.37,
      "catalyst": "Brent ~$110 on 2026-10-21 after Hormuz tanker and Saudi facility attacks; EIA 10:30 ET.",
      "thesis": "Energy remains the leading sector; a break of the 180.26 20-day high with oil at a 5-month high extends the trend.",
      "invalidation": "Brent back below $105 on de-escalation or US-Iran talks.",
      "bear_case": "Oil reverses fast on diplomacy headlines; breakout at a 5-month oil high may be the blow-off."
    }
  ],
  "manage": [
    {
      "ticker": "HD",
      "action": "update",
      "stop": 309.00,
      "reason": "Up 7% in 5 days near the 20d high; raise stop to ~1 ATR below last, near breakeven, ahead of the 20-year auction."
    }
  ],
  "passed": [
    {
      "ticker": "UNH",
      "direction": "long",
      "entry_type": "stop",
      "entry": 423.00,
      "stop": 410.00,
      "targets": [445.00],
      "p_target_first": 0.35,
      "reason": "Healthcare soft pre-market on ISRG/TMO; prefer to spend the risk on energy."
    }
  ]
}
```

Sources: [TipRanks](https://www.tipranks.com/news/stock-market-today-oct-21-futures-rise-on-latest-earnings-spacex-stock-soars-on-q3-beat-and-merger-talks), [TradingKey pre-market](https://www.tradingkey.com/analysis/stocks/us-stocks/262228945-us-premarket-spcx-surges-smci-soars-nflx-plunges-tesla-meta-earnings-tradingkey), [CNBC movers](https://www.cnbc.com/2026/10/21/stocks-making-the-biggest-moves-premarket-spcx-smci-nflx-more.html), [Yahoo Oct 20 close](https://finance.yahoo.com/markets/stocks/articles/markets-news-oct-20-2026-103252254.html), [5paisa Brent](https://www.5paisa.com/blog/crude-oil-price-today-brent-at-11032-wti-at-9952-after-indian-market-close-on-october-21), [Investing.com calendar](https://www.investing.com/news/stock-market-news/us-economic-calendar-preview-key-releases-for-the-week-of-oct-1923-2026-93CH-4958178), [Saxo options brief](https://home.saxo/content/articles/options/cancellation-not-calm---options-brief---21-october-2026-21102026), [GuruFocus AT&T](https://www.gurufocus.com/news/9133816/att-t-shares-dip-46-premarket-after-q3-earnings-beat-but-subscriber-growth-misses), [Investing.com TMO](https://www.investing.com/news/transcripts/earnings-call-transcript-thermo-fisher-tops-q3-2026-estimates-but-shares-slip-93CH-4962855), [CNBC Treasuries](https://www.cnbc.com/2026/10/21/bonds-us-treasurys-yields.html)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC, 16:05 Stockholm), Wednesday 2026-10-21. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$101,948.50**
- Cash: $88,578.32
- Session P&L so far: -0.14% (new entries are blocked at -3.0%)
- Gross exposure: $75,686 (74% of equity, cap 150%)
- Net exposure: $+15,289 (+15%, cap +/-100%)
- Risk at stake (entry to stop): $2,379 (2.33% of equity, cap 4.0%) — 1.67% left for new plays
- Slots: 4 open + 3 resting entries of 8 — you may add at most 1 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| AMD | short | 19 | 542.20 | 543.42 | -23 (-0.2%) | 558.00 | 512.00 | Relief gap on upgrades without any change to the AI-credit story, now confirmed by the open rather than predicted. Overh |
| CVX | long | 78 | 224.48 | 226.06 | +123 (+0.7%) | 218.00 | 236.00 | Energy leads the rotation away from AI capex and the oil tape still points up. A retest of the breakout and Monday's 224 |
| HD | long | 33 | 310.70 | 313.25 | +84 (+0.8%) | 309.00 | 322.00 | Falling long yields help housing most and HD is the liquid leader; a break of the 20d high would confirm the rotation sp |
| ORCL | short | 33 | 129.70 | 129.41 | +10 (+0.2%) | 137.40 | 116.50 | ORCL is the large cap most exposed to the market pricing AI build-out credit risk. A break of the 130 support opens the  |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XOM | long | 97 | 180.60 | stop | 175.40 | 189.00 | 2026-10-21 |
| NFLX | short | 159 | 63.40 | stop | 66.60 | 59.00 | 2026-10-21 |
| NVDA | short | 26 | 212.40 | stop | 222.00 | 198.00 | 2026-10-20 |

### Record

20 closed trades: 7W / 13L, total -1.00R, net $+1,767 realized. Shorts taken: 22.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| IWM | short | close | -0.54R | $-274 | 42% |
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |

### Ideas you passed on, replayed against the tape

48 resolved: 11 reached target first, 27 stop first, 8 never reached the entry, 2 expired, 0 ambiguous. Average -0.29R across the 40 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-19 open | NVDA | short | Gap already faded to near the 212.85 20-day low; little room to the floor. | stop | -0.95R | 35% |
| 2026-10-14 open | KRE | short | Morning play rejected by broker: not shortable. | never filled | - | 34% |
| 2026-10-07 pre-market | XHB | short | Same housing/rates factor as the HD short; one is enough. | expired | -0.52R | 33% |
| 2026-10-20 pre-market | DAL | short | Oil-cost victim, but at its 20d low with UAL reporting tonight; gap-risk coin fl | stop | -1.04R | 35% |
| 2026-10-15 open | LLY | long | 1.3 ATR above its 20d high after +4.3%; chasing a gap. | target | +2.00R | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AMD | 543.18 (10:05 iex) | +1.6% | 534.74 | 546.00 / 537.36-554.32 | 27.36 (5.1%) | 524.60-658.52 | -11.2% / -0.9% | -11.7% | 19.4M |
| CVX | 226.07 (10:05 iex) | +0.2% | 225.71 | 225.90 / 224.19-226.46 | 4.64 (2.1%) | 201.96-227.28 | +6.6% / +8.4% | +3.7% | 7.5M |
| HD | 313.52 (10:04 iex) | -0.5% | 315.11 | 316.39 / 313.50-316.46 | 6.76 (2.1%) | 277.15-317.71 | +7.3% / +1.4% | +7.2% | 5.6M |
| ORCL | 129.47 (10:05 iex) | -1.3% | 131.14 | 133.12 / 128.09-133.52 | 6.62 (5.1%) | 127.36-148.11 | -4.5% / -8.9% | -8.4% | 30.4M |
| XOM | 177.30 (10:04 iex) | -0.3% | 177.86 | 177.72 / 176.15-178.10 | 3.60 (2.0%) | 159.27-180.26 | +5.8% / +8.1% | +2.2% | 11.5M |
| NFLX | 66.47 (10:05 iex) | -3.2% | 68.69 | 64.21 / 64.10-67.11 | 1.73 (2.5%) | 66.54-73.07 | -1.8% / -8.2% | -2.5% | 36.7M |
| NVDA | 220.03 (10:05 iex) | +1.6% | 216.47 | 220.89 / 219.54-222.16 | 5.78 (2.7%) | 212.77-243.37 | -4.7% / -2.8% | -5.3% | 104.7M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 769.91 (10:05 iex) | +0.1% | 769.05 | 771.18 / 769.73-771.34 | 7.13 (0.9%) | 758.79-781.62 | -0.2% / +0.2% | -1.2% | 41.6M |
| QQQ | 722.39 (10:05 iex) | +0.7% | 717.63 | 722.20 / 719.71-723.54 | 11.13 (1.6%) | 707.23-762.86 | -3.0% / -1.2% | -3.5% | 35.2M |
| IWM | 276.25 (10:05 iex) | +0.2% | 275.78 | 276.85 / 276.25-277.62 | 4.08 (1.5%) | 269.88-286.18 | -0.8% / -4.1% | -0.3% | 26.2M |
| DIA | 523.71 (10:05 iex) | -0.1% | 524.36 | 526.83 / 523.61-526.85 | 5.29 (1.0%) | 504.59-526.17 | +1.9% / +0.3% | +1.6% | 3.4M |
| TLT | 80.34 (10:04 iex) | +0.3% | 80.13 | 80.31 / 80.25-80.47 | 0.85 (1.1%) | 76.43-81.18 | +2.1% / -0.2% | +2.2% | 50.7M |
| GLD | 378.34 (10:02 iex) | +0.2% | 377.65 | 379.19 / 378.19-379.32 | 4.92 (1.3%) | 373.36-395.50 | -1.2% / -4.7% | -1.1% | 7.7M |
| USO | 159.55 (10:02 iex) | -0.7% | 160.61 | 159.41 / 158.57-159.55 | 4.75 (3.0%) | 141.76-162.99 | +6.6% / +11.4% | +4.9% | 5.4M |
| SMH | 553.33 (10:04 iex) | +1.3% | 546.36 | 556.42 / 550.93-558.53 | 16.87 (3.1%) | 536.23-639.47 | -8.3% / -5.5% | -7.1% | 7.6M |
| XLK | 187.23 (10:05 iex) | +1.0% | 185.44 | 187.53 / 186.54-187.93 | 3.74 (2.0%) | 182.81-203.25 | -4.8% / -2.3% | -5.5% | 8.3M |
| XLF | 55.73 (10:05 iex) | +0.0% | 55.72 | 56.04 / 55.64-56.06 | 0.70 (1.3%) | 52.81-56.03 | +2.3% / -0.6% | +1.6% | 36.9M |
| XLE | 68.04 (10:05 iex) | +0.1% | 67.97 | 67.86 / 67.51-68.06 | 1.38 (2.0%) | 60.95-68.51 | +5.4% / +6.7% | +1.1% | 32.4M |
| XLV | 177.87 (10:05 iex) | -1.1% | 179.82 | 177.75 / 177.75-179.68 | 3.03 (1.7%) | 165.19-180.06 | +5.2% / +5.7% | +6.0% | 8.4M |
| XLI | 168.23 (10:04 iex) | +0.9% | 166.80 | 168.33 / 167.89-168.84 | 2.57 (1.5%) | 164.66-172.34 | -1.1% / -3.7% | -1.1% | 7.5M |
| XLY | 115.35 (10:04 iex) | -0.1% | 115.50 | 115.80 / 115.17-115.89 | 1.53 (1.3%) | 107.99-116.22 | +3.7% / +1.7% | +2.8% | 7.0M |
| XLP | 87.22 (10:05 iex) | -0.6% | 87.75 | 87.08 / 86.91-87.51 | 1.11 (1.3%) | 80.10-88.47 | +5.3% / +4.6% | +4.2% | 12.7M |
| XLU | 42.01 (10:05 iex) | +0.3% | 41.88 | 42.25 / 41.87-42.26 | 0.69 (1.6%) | 39.03-42.29 | +2.9% / +0.3% | +0.0% | 35.8M |
| XLB | 51.07 (10:04 iex) | -0.3% | 51.23 | 51.21 / 50.98-51.27 | 0.73 (1.4%) | 47.81-51.51 | +3.1% / +0.5% | +3.0% | 11.7M |
| XLRE | 42.20 (10:04 iex) | -0.4% | 42.38 | 42.49 / 42.16-42.61 | 0.62 (1.5%) | 40.28-42.48 | +2.3% / -1.0% | +1.3% | 7.6M |
| XLC | 109.53 (10:05 iex) | -0.6% | 110.19 | 109.03 / 108.61-109.87 | 1.63 (1.5%) | 109.45-114.08 | -1.1% / -1.3% | -1.9% | 6.3M |
| KRE | 70.44 (10:04 iex) | -0.2% | 70.62 | 70.82 / 70.44-71.07 | 1.32 (1.9%) | 67.79-71.93 | +1.0% / -2.5% | +2.3% | 16.0M |
| XHB | 96.00 (10:00 iex) | -0.2% | 96.22 | 96.61 / 95.95-96.61 | 2.28 (2.4%) | 91.87-99.13 | +0.4% / -3.6% | +1.7% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 340.89 (10:05 iex) | +0.4% | 339.50 | 339.36 / 338.83-341.35 | 6.01 (1.8%) | 325.81-348.15 | +0.6% / +3.8% | -0.5% | 36.9M |
| MSFT | 529.62 (10:05 iex) | -0.4% | 531.87 | 529.96 / 525.02-531.39 | 11.30 (2.1%) | 491.22-551.15 | +1.6% / +5.0% | -2.1% | 21.6M |
| NVDA | 220.03 (10:05 iex) | +1.6% | 216.47 | 220.89 / 219.54-222.16 | 5.78 (2.7%) | 212.77-243.37 | -4.7% / -2.8% | -5.3% | 104.7M |
| AMZN | 259.83 (10:05 iex) | -1.1% | 262.63 | 262.97 / 259.31-263.08 | 6.51 (2.5%) | 244.72-265.34 | +3.5% / +2.4% | +1.6% | 36.2M |
| GOOGL | 333.05 (10:05 iex) | -2.1% | 340.27 | 336.99 / 331.45-337.27 | 8.67 (2.5%) | 335.51-359.40 | -1.5% / -1.1% | -3.8% | 24.2M |
| META | 709.78 (10:05 iex) | +2.2% | 694.25 | 697.98 / 692.38-711.85 | 21.90 (3.2%) | 681.05-779.82 | -5.1% / +5.3% | -9.0% | 19.6M |
| TSLA | 385.84 (10:05 iex) | +3.2% | 373.71 | 381.43 / 380.51-388.82 | 11.76 (3.1%) | 345.88-388.56 | +1.1% / +3.5% | -0.4% | 35.0M |
| AVGO | 335.45 (10:05 iex) | +0.3% | 334.37 | 338.04 / 334.66-338.94 | 11.96 (3.6%) | 328.58-380.84 | -5.1% / -7.6% | -6.4% | 21.7M |
| AMD | 543.18 (10:05 iex) | +1.6% | 534.74 | 546.00 / 537.36-554.32 | 27.36 (5.1%) | 524.60-658.52 | -11.2% / -0.9% | -11.7% | 19.4M |
| ORCL | 129.47 (10:05 iex) | -1.3% | 131.14 | 133.12 / 128.09-133.52 | 6.62 (5.1%) | 127.36-148.11 | -4.5% / -8.9% | -8.4% | 30.4M |
| NFLX | 66.47 (10:05 iex) | -3.2% | 68.69 | 64.21 / 64.10-67.11 | 1.73 (2.5%) | 66.54-73.07 | -1.8% / -8.2% | -2.5% | 36.7M |
| CRM | 240.79 (10:04 iex) | -0.7% | 242.43 | 241.40 / 237.23-244.18 | 8.55 (3.5%) | 220.29-251.94 | +3.6% / +4.6% | +1.9% | 8.5M |
| JPM | 334.00 (10:05 iex) | -0.4% | 335.26 | 337.12 / 333.93-337.12 | 6.42 (1.9%) | 324.25-344.40 | +0.5% / -3.0% | +1.2% | 7.9M |
| GS | 892.92 (10:05 iex) | +0.9% | 884.81 | 900.00 / 891.53-901.04 | 23.57 (2.7%) | 859.03-954.98 | -1.6% / -8.5% | -0.8% | 2.3M |
| BAC | 50.77 (10:05 iex) | +0.2% | 50.64 | 51.09 / 50.52-51.22 | 1.33 (2.6%) | 49.26-56.74 | -5.7% / -13.3% | -6.2% | 43.0M |
| XOM | 177.30 (10:04 iex) | -0.3% | 177.86 | 177.72 / 176.15-178.10 | 3.60 (2.0%) | 159.27-180.26 | +5.8% / +8.1% | +2.2% | 11.5M |
| CVX | 226.07 (10:05 iex) | +0.2% | 225.71 | 225.90 / 224.19-226.46 | 4.64 (2.1%) | 201.96-227.28 | +6.6% / +8.4% | +3.7% | 7.5M |
| LLY | 1,265.88 (10:05 iex) | -1.4% | 1,283.66 | 1,266.90 / 1,261.08-1,279.28 | 37.77 (2.9%) | 1,131.21-1,311.75 | +8.0% / +8.6% | +10.0% | 2.3M |
| UNH | 415.49 (10:05 iex) | -0.9% | 419.26 | 421.80 / 415.89-421.80 | 13.32 (3.2%) | 362.60-422.40 | +9.7% / +8.5% | +11.0% | 6.0M |
| JNJ | 255.31 (10:05 iex) | -1.6% | 259.36 | 257.50 / 255.29-257.75 | 6.49 (2.5%) | 245.17-275.23 | -0.3% / -2.1% | +4.3% | 7.7M |
| WMT | 117.37 (10:05 iex) | -0.4% | 117.85 | 116.90 / 116.63-117.96 | 2.37 (2.0%) | 103.39-121.38 | +6.6% / +8.0% | +5.0% | 21.5M |
| COST | 991.86 (10:04 iex) | -0.3% | 994.61 | 990.57 / 988.47-996.80 | 15.74 (1.6%) | 883.10-1,008.37 | +5.4% / +6.3% | +4.2% | 2.3M |
| HD | 313.52 (10:04 iex) | -0.5% | 315.11 | 316.39 / 313.50-316.46 | 6.76 (2.1%) | 277.15-317.71 | +7.3% / +1.4% | +7.2% | 5.6M |
| CAT | 734.54 (10:04 iex) | +1.3% | 725.24 | 745.00 / 733.00-745.00 | 30.67 (4.2%) | 704.01-876.95 | -8.9% / -10.3% | -6.2% | 2.6M |
| BA | 192.04 (10:04 iex) | +0.8% | 190.47 | 191.84 / 190.97-193.28 | 4.34 (2.3%) | 183.38-204.06 | +0.0% / -6.5% | +2.1% | 8.4M |
| DAL | 78.17 (10:05 iex) | +2.0% | 76.66 | 76.94 / 76.19-78.80 | 2.78 (3.6%) | 74.14-85.93 | -5.4% / -5.9% | -3.4% | 7.3M |
| UAL | 101.79 (10:05 iex) | +4.1% | 97.77 | 97.51 / 96.24-101.98 | 4.17 (4.3%) | 94.54-115.71 | -8.6% / -11.7% | -5.3% | 4.6M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-21 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPAL | 19.89 (10:04 iex) | +24.1% | 16.03 | 18.87 / 18.37-20.07 | 1.68 (10.5%) | 14.53-23.10 | -10.3% / -4.5% | -11.6% | 1.0M |
| SMCX | 10.19 (10:05 iex) | +24.6% | 8.18 | 10.19 / 9.92-10.69 | 1.58 (19.4%) | 7.41-16.85 | -36.8% / -35.1% | -32.8% | 4.3M |
| SPAX | 11.83 (10:05 iex) | +23.7% | 9.56 | 11.23 / 10.91-11.93 | 1.00 (10.5%) | 8.64-13.78 | -10.3% / -4.8% | -11.5% | 2.1M |
| SPCU | 15.43 (10:05 iex) | +23.6% | 12.48 | 14.60 / 14.23-15.54 | 1.32 (10.6%) | 11.28-18.02 | -10.4% / -5.2% | -11.6% | 1.5M |
| SPCM | 20.23 (10:05 iex) | +23.5% | 16.37 | 19.13 / 18.64-20.36 | 1.70 (10.4%) | 14.76-23.46 | -10.0% / -4.1% | -11.2% | 1.0M |
| SPCH | 11.62 (10:05 iex) | +23.6% | 9.40 | 11.00 / 10.71-11.70 | 0.99 (10.6%) | 8.49-13.55 | -10.2% / -4.9% | -11.3% | 22.1M |
| SPCF | 19.32 (10:04 iex) | +23.2% | 15.68 | 18.29 / 17.81-19.49 | 1.64 (10.5%) | 14.11-22.53 | -10.0% / -4.6% | -11.1% | 1.6M |
| LOFF | 19.59 (10:04 iex) | +23.3% | 15.89 | 18.58 / 18.06-19.70 | 1.66 (10.5%) | 14.32-22.79 | -9.9% / -4.2% | -11.1% | 1.8M |
| SMCZ | 4.97 (10:03 iex) | -25.8% | 6.70 | 5.08 / 4.64-5.27 | 0.64 (9.5%) | 3.66-7.39 | +37.0% / +17.7% | +38.1% | 2.5M |
| SNK | 10.77 (10:03 iex) | -25.2% | 14.40 | 11.87 / 10.77-12.29 | 1.20 (8.3%) | 10.21-15.67 | +6.2% / -6.5% | +12.3% | 2.6M |
| SPCQ | 7.90 (10:03 iex) | -24.3% | 10.43 | 8.64 / 7.90-8.93 | 0.89 (8.5%) | 7.50-11.52 | +5.3% / -8.7% | +12.0% | 2.2M |
| SPCG | 11.28 (10:03 iex) | -24.4% | 14.92 | 12.40 / 11.28-12.83 | 1.25 (8.4%) | 10.64-16.29 | +5.8% / -6.5% | +11.6% | 1.5M |
| SSPC | 6.55 (10:03 iex) | -24.6% | 8.69 | 7.20 / 6.55-7.47 | 0.73 (8.4%) | 6.21-9.54 | +5.5% / -7.2% | +11.4% | 15.4M |
| SAIQ | 5.33 (10:04 iex) | -22.1% | 6.84 | 5.60 / 5.12-5.72 | 2.06 (30.1%) | 1.76-12.95 | +14.7% / -21.7% | +63.2% | 8.0M |
| AVEX | 11.37 (10:05 iex) | -20.7% | 14.34 | 11.65 / 11.08-12.44 | 0.97 (6.7%) | 13.55-17.15 | -4.0% / -14.0% | +0.8% | 1.7M |
| BEZ | 6.38 (10:05 iex) | -11.2% | 7.18 | 6.44 / 6.14-6.76 | 0.72 (10.0%) | 4.08-7.77 | +31.3% / -2.8% | +35.0% | 5.6M |
