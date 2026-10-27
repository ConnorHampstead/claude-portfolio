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

# Pre-market brief: Tuesday 2026-10-27

*Clock note: Stockholm is still **ET + 5h** this week, because Europe changed its clocks on 25 Oct and the US changes on 1 Nov. Today's open at 09:30 ET is 14:30 Stockholm, and the 10:00 ET data is 15:00 Stockholm.*

### 1. Tape
Monday was a risk-on day for AI. Anthropic's IPO filing (H1 revenue $1.16B, +1,304% year on year) lifted the Philadelphia semiconductor index 2.8%. This morning that bid continues in the chips but is fading at the index level: S&P and Dow futures are about flat, and the Yahoo snapshot had Nasdaq futures −0.4% earlier. Alpaca at 08:49 ET shows SPY +0.4%, QQQ +0.4% and SMH +1.6%. AVGO is +3.3% on a **$63B financing package (BofA, Blackstone, Citi, MS) for Anthropic's compute built on Broadcom XPUs**. Oil, Treasuries and volatility are calm:

- Brent is about $115–116, flat to −0.5%. Saudi, Turkish and Pakistani officials held talks in Tehran, which Tehran called "very good".
- The 10-year is 4.98%.
- VIX is 17.7, down 3.6%.

The market is waiting for three things: the FOMC (the two-day meeting starts today, decision Wed 14:00 ET), MSFT and GOOGL after Wednesday's close, and AMZN on Thursday. The regime is a pre-event chop with the AI-credit fear being actively unwound. That runs against the two AI shorts I hold. I give the long side a slight edge today. Over 1–5 days I expect a two-way tape set by Wednesday's prints.

### 2. Calendar
| Event | ET | Stockholm | Status | Touches |
|---|---|---|---|---|
| Durable goods (Sep) | 08:30 | 13:30 | **Released: +1.8%** after −0.2% in August (Census, verified). I couldn't verify the consensus. Futures did not visibly react. | XLI, BA |
| BA Q3 | pre-mkt | — | **Released:** adj. EPS −0.34 vs −0.25 expected; revenue $24.2B vs $23.9B; FCF +$464M. BA is −2.1% on IEX at 09:02. | BA play |
| KO, GLW Q3 | pre-mkt | — | Released. GLW +3.3% pre-market. | none |
| Case-Shiller / FHFA (Aug) | 09:00 | 14:00 | Released. **I couldn't verify the actual figures.** | XHB (not held) |
| Consumer confidence (Oct), new home sales, Richmond Fed | 10:00 | 15:00 | Ahead. Confidence consensus 81.0. | KRE, TSLA, XLY |
| V, STX earnings | AMC | ~21:05 | Ahead. PYPL timing conflicts across sources (before or after the open). | none held |
| FOMC decision | Wed 14:00 | Wed 19:00 | Hold expected | whole book |
| MSFT, GOOGL | Wed AMC | Wed ~21:05 | Ahead | NVDA, ORCL by read-through |
| AMZN, Q3 GDP | Thu | Thu | Ahead | all |
| **XOM Q3** | Fri 06:30 | 11:30 | Ahead | **XOM: exit by the Thu 10/29 review** |

### 3. Open positions and resting entries
- **KRE long** (73.06 → 72.80, stop 71.25, target 76.20). **Intact.** The 73.42 high is just overhead; the FOMC is a two-sided risk. Hold, no change.
- **NVDA short** (212.38 → 218.43, stop 222, target 198). **Weakening, close to invalidated.** The thesis was AI-infrastructure funding stress. The Anthropic IPO and the $63B XPU financing are direct evidence against it, and NVDA is pressing the 220 line I gave as invalidation. Monday's review rule ("trades above 218 → stop to 219") was not executed; the live stop is still 222. I am keeping 222, which is 1.6% away and about 0.6 ATR. **For the review: close it if NVDA is above 220 at 10:05.**
- **ORCL short** (129.70 → 128.34, stop 130, target 116.50). **Weakening** for the same AI-financing reason. The stop is at breakeven plus 0.30, so the remaining risk is tiny. Hold and let the stop decide.
- **XLV long** (179.57 → 179.01, stop 176.40, target 184.80). **Intact but stalling**, and the AI risk-on bid is pulling money away from defensives. Hold.
- **XOM long** (180.75 → 183.39, stop 178.90, target 189). **Intact**, with Brent at about $115. The Saudi–Iran talks are a de-escalation headline risk, and earnings Friday force an exit by Thursday anyway. **I am raising the stop to 180.40**, just under entry and above the 180.26 breakout level, so the trade cannot turn into a meaningful loser in its last two days. The new stop is 2.99 below the last trade (about 0.75 ATR), so it could be shaken out. I accept that: holding through earnings is not an option, so there is little left to protect.
- No resting entries.

### 4. New plays
There are 3 slots and 2.82% of risk room. I am not adding AI exposure in either direction into Wednesday. Both plays are probes on names whose own catalysts have already passed.

**BA short: post-earnings break of the 20-day low**

| Field | Value |
|---|---|
| Ticker | BA |
| Direction | Short |
| Catalyst | Q3 reported 2026-10-27 pre-market: adj. EPS −0.34 vs −0.25 expected. BA is −2.1% pre-market (184.41 on IEX), 2 points above the 182.40 20-day low. |
| Thesis | A miss on per-share earnings, despite the revenue and FCF beat, puts BA under its 20-day range. A break of 182.40 on earnings-day volume points to post-earnings drift. BA is already 6% below its 50-day average. |
| Entry | Sell stop 182.20, below the 20-day low and below pre-market |
| Stop | 188.60: above Monday's 188.31 close. Filling the earnings gap means the market has forgiven the print. About 1.5 ATR. |
| Target | 172.50 (+1.5R) |
| Risk tier | 0.25, a probe. The print was mixed (the FCF beat is what bulls care about), and selling an earnings gap is a trade I have not scored here. |
| Time horizon | 1–4 days |
| Conviction | 2 |
| P(target before stop) | 34% |
| Invalidation | BA reclaims 188 or closes green today, or an upgrade wave defends it on FCF |
| What I'd be wrong about | FCF beat a guide of "low hundreds of millions" and the backlog is a record $745B. The EPS miss may be noise, and the open could reverse higher. |

**TSLA long: 20-day-high breakout**

| Field | Value |
|---|---|
| Ticker | TSLA |
| Direction | Long |
| Catalyst | 2026-10-27: TSLA +1.2% pre-market at 396.29, against a 397.27 20-day high, +6.4% over 5 days. AI and autonomy beta is getting a bid from the Anthropic risk-on move. Its earnings have passed. |
| Thesis | Relative strength at the top of the range while megacap tech struggles. A clean break of 397.27 opens room toward 420. |
| Entry | Buy stop 399.00 |
| Stop | 384.00: back inside the range, below Monday's 391.62 close, about 1.15 ATR |
| Target | 421.00 (+1.47R) |
| Risk tier | 0.25, a probe. The breakout is extended and comes right before the Fed and megacap prints. |
| Time horizon | 1–4 days |
| Conviction | 2 |
| P(target before stop) | 35% |
| Invalidation | QQQ loses its 701 20-day low, or a breakout that fails back under 392 |
| What I'd be wrong about | It is +6% in 5 days and buying 20-day-high breakouts has paid poorly in this record. A hawkish FOMC hits high-multiple names first. |

### 5. Both sides
- **Best long:** TSLA breakout (399 stop entry / 384 / 421, P 35%). Taken as a probe.
- **Best short:** BA post-earnings breakdown (182.20 / 188.60 / 172.50, P 34%). Taken as a probe. Next best was a META sell stop at 624 under its 627.80 20-day low (stop 652, target 585, P 33%). **Passed:** it is another AI-capex short just as AI financing is being re-rated upward, and the MSFT/GOOGL read-through lands Wednesday.

### 6. Passing on
- **META short (624 / 652 / 585, P 33%):** it would stack a third AI short into a relief bid with Wednesday's prints ahead.
- **CVX long (buy stop 234.40, stop 228.50, target 244, P 36%):** it duplicates the energy exposure I am exiting by Thursday. Its own earnings are Fri 30 Oct, inside a 5-day hold, so rule 8 also blocks it.
- **XLU long (buy stop 42.95, stop 42.00, target 44.40, P 35%):** a defensive breakout fighting today's risk-on rotation, with the FOMC on rate-sensitive names tomorrow. XLV already covers the defensive view.
- **TLT long (buy stop 82.05, stop 80.70, target 84.20, P 33%):** the FOMC tomorrow and PCE Friday make it a coin flip.
- **AVGO long on the financing news:** chasing a +3.3% gap in a 3.4%-ATR name, with MSFT/GOOGL capex as a binary-like event Wednesday.
- **XLC short at its 20-day low:** about 40% of the fund is GOOGL and META, so it is in effect holding GOOGL into its print.

### 7. For the post-open review
- **NVDA:** close it if it is above 220 at 10:05. Otherwise hold with the 222 stop.
- **BA:** if the entry is unfilled and BA trades above 188 (the gap is filled), cancel. If it filled and BA is back above 185.50 by 10:05, close it, because the break failed.
- **TSLA:** if it is unfilled and QQQ is below 710 at 10:05, cancel. If it filled and is back under 395, close it.
- **XOM:** no action today. It must be closed at the latest by the Thu 10/29 review.
- **KRE / XLV / ORCL:** no action. If confidence prints well below 81 at 10:00, that hurts KRE, but the stop stands.

### 8. Book state
If both entries fill: gross is about 80% of equity (cap 150%) and net about +46% (cap ±100%), using 7 of 8 slots. Risk at stake is about 1.5% of equity (cap 4%), after the XOM stop raise cuts about 0.14%.

```json
{
  "date": "2026-10-27",
  "no_trade": false,
  "session_note": "Pre-FOMC/megacap chop with AI-financing relief (Anthropic IPO, $63B AVGO-XPU deal) undercutting AI shorts; two 0.25 probes on post-catalyst names (BA breakdown, TSLA breakout), XOM stop raised to near breakeven ahead of Friday earnings.",
  "plays": [
    {
      "ticker": "BA",
      "direction": "short",
      "entry_type": "stop",
      "entry": 182.20,
      "stop": 188.60,
      "targets": [172.50],
      "time_horizon": "1-4 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.34,
      "catalyst": "Q3 reported 2026-10-27 pre-market: adj EPS -0.34 vs -0.25 est; stock -2.1% pre-market at 184.41, 2 points above the 182.40 20d low.",
      "thesis": "Per-share miss puts BA under its 20-day range; a break of 182.40 on earnings-day volume signals post-earnings drift in a name already 6% below its 50d average.",
      "invalidation": "BA reclaims 188 / fills the gap, or closes green today on FCF-driven upgrades.",
      "bear_case": "FCF of $464M beat guidance and backlog is a record $745B; the EPS miss may be noise and the open may reverse up."
    },
    {
      "ticker": "TSLA",
      "direction": "long",
      "entry_type": "stop",
      "entry": 399.00,
      "stop": 384.00,
      "targets": [421.00],
      "time_horizon": "1-4 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.35,
      "catalyst": "2026-10-27 TSLA +1.2% pre-market at 396.29 against its 397.27 20d high (+6.4% 5d) on the Anthropic-led AI risk-on bid; earnings already past.",
      "thesis": "Relative strength at the range top while megacap tech chops; a clean 20d-high break opens room toward 420.",
      "invalidation": "QQQ loses 701, or the breakout fails back under 392.",
      "bear_case": "Extended +6% in 5 days into FOMC and MSFT/GOOGL prints; 20d-high breakouts have scored poorly in this record."
    }
  ],
  "manage": [
    {
      "ticker": "XOM",
      "action": "update",
      "stop": 180.40,
      "reason": "Earnings Fri 10/30 force an exit by Thursday; Saudi-Iran talks add de-escalation risk. Stop raised to just under entry and above the 180.26 breakout."
    }
  ],
  "passed": [
    {
      "ticker": "META",
      "direction": "short",
      "entry_type": "stop",
      "entry": 624.00,
      "stop": 652.00,
      "targets": [585.00],
      "p_target_first": 0.33,
      "reason": "A third AI short into an AI-financing relief bid, with MSFT/GOOGL read-through Wednesday."
    },
    {
      "ticker": "CVX",
      "direction": "long",
      "entry_type": "stop",
      "entry": 234.40,
      "stop": 228.50,
      "targets": [244.00],
      "p_target_first": 0.36,
      "reason": "Duplicates XOM energy exposure, and its own Oct 30 earnings fall inside the horizon (rule 8)."
    },
    {
      "ticker": "XLU",
      "direction": "long",
      "entry_type": "stop",
      "entry": 42.95,
      "stop": 42.00,
      "targets": [44.40],
      "p_target_first": 0.35,
      "reason": "Defensive breakout against today's risk-on rotation; FOMC tomorrow; XLV already holds the defensive view."
    },
    {
      "ticker": "TLT",
      "direction": "long",
      "entry_type": "stop",
      "entry": 82.05,
      "stop": 80.70,
      "targets": [84.20],
      "p_target_first": 0.33,
      "reason": "20d-high breakout, but FOMC and PCE make the inflation side a coin flip."
    }
  ]
}
```

Sources: [TheStreet Oct 27](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-27-2026), [Yahoo futures](https://finance.yahoo.com/markets/stocks/articles/us-stock-futures-edge-lower-102329525.html), [TipRanks](https://www.tipranks.com/news/stock-market-today-oct-27-futures-edge-higher-ahead-of-key-earnings-and-the-feds-rate-decision), [Tradingeconomics Brent](https://tradingeconomics.com/commodity/brent-crude-oil), [Fortune oil](https://fortune.com/article/price-of-oil-10-27-2026/), [CBS Iran live](https://www.cbsnews.com/live-updates/iran-war-trump-us-diplomacy-oil-prices-strait-of-hormuz/), [Census durable goods](https://www.census.gov/manufacturing/m3/adv/pdf/durgd.pdf), [Tradingeconomics durables](https://tradingeconomics.com/united-states/durable-goods-orders/news/505177), [financecalendar confidence](https://www.financecalendar.com/event/us-consumer-confidence-october-2026/), [Newsquawk BA](https://www.newsquawk.com/headlines/boeing-company-ba-q3-2026-usd-adj-eps--034-exp--025-revenue-242bln-exp-239bln), [Stocktitan BA](https://www.stocktitan.net/news/BA/boeing-reports-third-quarter-9vgnsenhgf74.html), [CNBC BA](https://www.cnbc.com/2026/10/27/-boeing-ba-q3-2026-earnings.html), [TipRanks AI chips](https://www.tipranks.com/news/why-broadcom-amd-and-nvidia-stocks-are-rising-in-premarket-today-october-27), [Benzinga AVGO](https://www.benzinga.com/markets/tech/26/10/62613053/why-is-broadcom-stock-gaining-tuesday-2), [Spreadex megacap preview](https://www.spreadex.com/financials/news-analysis/financial-trading-blog/26-10-2026), [MarketBeat Visa](https://www.marketbeat.com/earnings/reports/2026-10-27-visa-inc-stock/), [TipRanks PYPL](https://www.tipranks.com/stocks/pypl/earnings)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC, 15:05 Stockholm), Tuesday 2026-10-27. The cash session opened 35 min ago and closes at 16:00 ET (21:00 Stockholm).
- Equity: **$102,067.20**
- Cash: $44,198.84
- Session P&L so far: -0.33% (new entries are blocked at -3.0%)
- Gross exposure: $76,219 (75% of equity, cap 150%)
- Net exposure: $+50,762 (+50%, cap +/-100%)
- Risk at stake (entry to stop): $1,548 (1.52% of equity, cap 4.0%) — 2.48% left for new plays
- Slots: 5 open + 1 resting entries of 8 — you may add at most 2 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 72.37 | -98 (-0.9%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| NVDA | short | 26 | 212.38 | 216.24 | -100 (-1.8%) | 222.00 | 198.00 | A break of the 212.85 20d low confirms Monday's bounce failed in the bellwether and opens a move toward 198. |
| TSLA | long | 17 | 398.69 | 402.23 | +60 (+0.9%) | 384.00 | 421.00 | Relative strength at the range top while megacap tech chops; a clean 20d-high break opens room toward 420. |
| XLV | long | 160 | 179.57 | 178.87 | -112 (-0.4%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |
| XOM | long | 97 | 180.75 | 183.06 | +224 (+1.3%) | 180.40 | 189.00 | Energy remains the leading sector; a break of the 180.26 20-day high with oil at a 5-month high extends the trend. |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| BA | short | 39 | 182.20 | stop | 188.60 | 172.50 | 2026-10-27 |

### Record

27 closed trades: 10W / 17L, total +1.32R, net $+2,102 realized. Shorts taken: 27.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| ORCL | short | stop | -0.06R | $-16 | 33% |
| UAL | short | stop | -0.45R | $-315 | 40% |
| XLI | short | stop | -1.00R | $-526 | 36% |
| GOOGL | short | target | +1.42R | $+362 | 35% |
| CVX | long | stop | -0.23R | $-117 | 40% |

### Ideas you passed on, replayed against the tape

64 resolved: 18 reached target first, 32 stop first, 11 never reached the entry, 3 expired, 0 ambiguous. Average -0.11R across the 53 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-22 pre-market | AVGO | short | Same AI factor as the existing shorts; no slot. | stop | -1.10R | 35% |
| 2026-10-21 pre-market | UNH | long | Healthcare soft pre-market on ISRG/TMO; prefer to spend the risk on energy. | stop | -1.00R | 35% |
| 2026-10-19 pre-market | AMD | short | Same idea as the SMH short with twice the noise; one semi short is enough. | never filled | - | 38% |
| 2026-10-19 pre-market | BAC | short | Post-earnings damage already priced; my last bank short stopped out. | never filled | - | 30% |
| 2026-10-14 pre-market | CVX | long | Best long (20d-high breakout) but duplicates the XOM energy exposure. | target | +1.70R | 40% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| KRE | 72.39 (10:05 iex) | -0.5% | 72.73 | 73.02 / 72.27-73.13 | 1.28 (1.8%) | 67.79-73.42 | +3.7% / +0.9% | +5.0% | 16.1M |
| NVDA | 216.22 (10:05 iex) | +0.1% | 216.00 | 218.36 / 215.53-218.50 | 6.14 (2.8%) | 210.18-243.37 | -4.0% / -2.8% | -0.5% | 103.6M |
| TSLA | 402.26 (10:05 iex) | +2.7% | 391.62 | 397.87 / 395.25-404.00 | 13.15 (3.4%) | 345.88-397.27 | +5.4% / +7.4% | +6.4% | 37.2M |
| XLV | 178.88 (10:05 iex) | -0.2% | 179.28 | 178.49 / 177.93-179.64 | 3.10 (1.7%) | 165.19-182.25 | +3.7% / +4.8% | +2.1% | 8.7M |
| XOM | 183.00 (10:05 iex) | -0.8% | 184.54 | 183.63 / 183.15-184.88 | 3.93 (2.1%) | 159.27-184.59 | +7.3% / +11.0% | +3.5% | 11.3M |
| BA | 183.77 (10:05 iex) | -2.4% | 188.31 | 183.50 / 182.77-187.86 | 4.15 (2.2%) | 182.40-196.93 | -0.5% / -6.0% | -1.6% | 7.6M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 765.98 (10:05 iex) | +0.1% | 765.37 | 767.34 / 765.60-768.36 | 7.25 (0.9%) | 758.68-781.62 | -0.6% / -0.2% | -0.1% | 40.2M |
| QQQ | 715.20 (10:05 iex) | +0.4% | 712.20 | 715.11 / 714.35-718.19 | 12.36 (1.7%) | 701.16-762.86 | -3.0% / -1.8% | -0.9% | 36.5M |
| IWM | 277.13 (10:05 iex) | +0.1% | 276.99 | 277.96 / 276.91-278.13 | 3.63 (1.3%) | 269.88-284.64 | -0.0% / -3.0% | +2.1% | 25.2M |
| DIA | 522.11 (10:04 iex) | -0.2% | 522.97 | 523.20 / 521.78-524.15 | 5.36 (1.0%) | 504.59-528.45 | +1.2% / +0.2% | +0.8% | 3.4M |
| TLT | 81.55 (10:04 iex) | -0.2% | 81.68 | 81.65 / 81.49-81.69 | 0.83 (1.0%) | 76.43-81.92 | +3.5% / +1.8% | +2.8% | 46.9M |
| GLD | 369.82 (10:05 iex) | +0.5% | 367.82 | 368.45 / 368.45-370.02 | 5.31 (1.4%) | 364.33-385.22 | -2.8% / -6.6% | -3.1% | 7.9M |
| USO | 166.33 (10:04 iex) | +0.1% | 166.23 | 165.66 / 164.94-166.63 | 4.78 (2.9%) | 141.76-169.96 | +8.2% / +12.9% | +3.4% | 4.9M |
| SMH | 549.44 (10:05 iex) | +1.4% | 541.62 | 549.17 / 547.16-553.03 | 19.10 (3.5%) | 520.53-639.47 | -7.0% / -5.7% | -1.2% | 8.6M |
| XLK | 187.60 (10:05 iex) | +0.7% | 186.32 | 187.57 / 187.27-188.59 | 4.24 (2.3%) | 181.50-203.25 | -3.4% / -1.7% | +0.2% | 8.8M |
| XLF | 55.84 (10:05 iex) | -0.3% | 56.02 | 56.27 / 55.79-56.32 | 0.72 (1.3%) | 52.81-56.67 | +2.3% / +0.1% | +1.7% | 35.5M |
| XLE | 69.02 (10:05 iex) | -0.9% | 69.64 | 69.28 / 69.02-69.70 | 1.48 (2.1%) | 60.95-69.86 | +5.9% / +8.3% | +2.7% | 31.9M |
| XLV | 178.88 (10:05 iex) | -0.2% | 179.28 | 178.49 / 177.93-179.64 | 3.10 (1.7%) | 165.19-182.25 | +3.7% / +4.8% | +2.1% | 8.7M |
| XLI | 167.49 (10:04 iex) | +0.3% | 166.96 | 167.85 / 167.09-167.97 | 2.71 (1.6%) | 162.97-172.34 | -0.7% / -2.7% | +0.2% | 7.5M |
| XLY | 114.40 (10:05 iex) | +0.1% | 114.26 | 114.85 / 114.38-114.90 | 1.63 (1.4%) | 107.99-116.22 | +1.8% / +0.9% | -0.2% | 7.2M |
| XLP | 87.48 (10:05 iex) | -0.5% | 87.96 | 87.25 / 87.19-87.61 | 1.38 (1.6%) | 80.10-89.99 | +4.0% / +4.5% | +0.9% | 14.0M |
| XLU | 42.62 (10:04 iex) | +0.2% | 42.55 | 42.64 / 42.51-42.76 | 0.63 (1.5%) | 39.03-42.88 | +3.1% / +2.1% | +2.9% | 35.2M |
| XLB | 51.44 (10:04 iex) | +0.1% | 51.38 | 51.23 / 51.21-51.62 | 0.66 (1.3%) | 47.81-51.71 | +2.7% / +1.0% | +0.8% | 11.3M |
| XLRE | 42.50 (10:02 iex) | -0.7% | 42.80 | 42.51 / 42.46-42.69 | 0.64 (1.5%) | 40.28-43.21 | +2.9% / +0.4% | +2.7% | 8.0M |
| XLC | 103.38 (10:05 iex) | -0.5% | 103.85 | 103.57 / 103.22-103.90 | 1.76 (1.7%) | 103.55-113.17 | -5.7% / -6.6% | -5.7% | 6.8M |
| KRE | 72.39 (10:05 iex) | -0.5% | 72.73 | 73.02 / 72.27-73.13 | 1.28 (1.8%) | 67.79-73.42 | +3.7% / +0.9% | +5.0% | 16.1M |
| XHB | 97.44 (10:04 iex) | -0.5% | 97.95 | 98.46 / 97.27-98.58 | 2.33 (2.4%) | 91.87-99.32 | +2.1% / -1.0% | +4.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 343.62 (10:05 iex) | -0.1% | 343.91 | 343.17 / 342.41-345.10 | 6.39 (1.9%) | 325.81-351.73 | +1.4% / +4.1% | +0.3% | 39.2M |
| MSFT | 528.50 (10:05 iex) | -0.8% | 532.60 | 532.67 / 528.40-533.89 | 11.12 (2.1%) | 502.40-551.15 | +0.9% / +4.6% | -0.2% | 20.3M |
| NVDA | 216.22 (10:05 iex) | +0.1% | 216.00 | 218.36 / 215.53-218.50 | 6.14 (2.8%) | 210.18-243.37 | -4.0% / -2.8% | -0.5% | 103.6M |
| AMZN | 249.40 (10:05 iex) | +0.1% | 249.09 | 250.29 / 248.73-251.27 | 6.94 (2.8%) | 245.14-265.34 | -2.2% / -2.5% | -5.1% | 35.9M |
| GOOGL | 317.60 (10:05 iex) | +0.3% | 316.80 | 317.01 / 316.86-319.96 | 8.42 (2.7%) | 316.60-359.40 | -7.3% / -7.4% | -8.0% | 24.1M |
| META | 623.38 (10:05 iex) | -1.1% | 630.56 | 627.39 / 621.48-628.01 | 25.92 (4.1%) | 627.80-771.27 | -11.6% / -5.1% | -10.6% | 19.5M |
| TSLA | 402.26 (10:05 iex) | +2.7% | 391.62 | 397.87 / 395.25-404.00 | 13.15 (3.4%) | 345.88-397.27 | +5.4% / +7.4% | +6.4% | 37.2M |
| AVGO | 341.01 (10:05 iex) | +3.6% | 329.17 | 339.34 / 337.40-345.67 | 11.23 (3.4%) | 320.23-380.84 | -5.3% / -7.3% | -1.6% | 21.6M |
| AMD | 550.27 (10:05 iex) | +3.6% | 531.28 | 539.47 / 538.50-555.01 | 28.48 (5.4%) | 502.60-658.52 | -8.9% / -2.1% | -1.3% | 19.3M |
| ORCL | 130.51 (10:05 iex) | +3.5% | 126.06 | 126.88 / 126.86-130.92 | 6.62 (5.2%) | 122.76-146.40 | -6.6% / -11.2% | -2.7% | 28.7M |
| NFLX | 63.17 (10:05 iex) | -1.1% | 63.90 | 63.40 / 62.93-63.87 | 2.20 (3.5%) | 62.86-73.07 | -7.2% / -13.6% | -8.5% | 43.0M |
| CRM | 243.17 (10:04 iex) | -1.8% | 247.61 | 245.20 / 242.78-248.08 | 8.56 (3.5%) | 220.29-252.42 | +4.7% / +5.0% | +2.1% | 7.8M |
| JPM | 335.50 (10:05 iex) | +0.4% | 334.04 | 337.04 / 334.54-337.51 | 6.50 (1.9%) | 324.25-344.40 | +0.3% / -2.8% | +0.2% | 7.3M |
| GS | 909.30 (10:04 iex) | +1.8% | 893.28 | 912.00 / 906.61-915.42 | 25.33 (2.8%) | 859.03-931.00 | +0.2% / -6.5% | +2.0% | 2.3M |
| BAC | 50.59 (10:05 iex) | +0.1% | 50.52 | 50.94 / 50.51-51.10 | 1.34 (2.6%) | 49.26-55.55 | -4.1% / -11.9% | +0.3% | 42.8M |
| XOM | 183.00 (10:05 iex) | -0.8% | 184.54 | 183.63 / 183.15-184.88 | 3.93 (2.1%) | 159.27-184.59 | +7.3% / +11.0% | +3.5% | 11.3M |
| CVX | 230.80 (10:04 iex) | -0.5% | 232.01 | 230.96 / 230.48-232.27 | 4.97 (2.1%) | 201.96-234.08 | +7.1% / +10.0% | +3.4% | 7.3M |
| LLY | 1,284.62 (10:03 iex) | +0.4% | 1,279.14 | 1,273.50 / 1,272.07-1,296.71 | 40.36 (3.2%) | 1,131.21-1,321.21 | +5.7% / +7.6% | +3.1% | 2.3M |
| UNH | 411.13 (10:05 iex) | +0.1% | 410.70 | 412.72 / 408.71-412.98 | 13.50 (3.3%) | 362.60-426.55 | +5.1% / +5.9% | +0.9% | 6.1M |
| JNJ | 267.42 (10:05 iex) | +0.4% | 266.30 | 265.25 / 264.83-267.71 | 7.33 (2.8%) | 245.17-272.36 | +2.9% / +0.4% | +4.9% | 7.9M |
| WMT | 119.64 (10:05 iex) | -0.5% | 120.29 | 119.69 / 119.26-120.06 | 2.57 (2.1%) | 103.39-122.40 | +6.7% / +9.8% | +1.3% | 21.2M |
| COST | 998.91 (10:04 iex) | -0.6% | 1,005.16 | 1,001.57 / 997.31-1,002.82 | 16.26 (1.6%) | 903.77-1,021.45 | +4.5% / +7.0% | +1.0% | 2.1M |
| HD | 317.25 (10:04 iex) | -0.7% | 319.38 | 318.34 / 316.46-319.59 | 7.57 (2.4%) | 277.15-327.92 | +6.8% / +3.4% | +3.1% | 5.2M |
| CAT | 705.13 (10:05 iex) | +1.9% | 692.13 | 703.76 / 699.43-708.36 | 28.86 (4.2%) | 679.50-874.87 | -10.5% / -12.9% | -4.4% | 2.7M |
| BA | 183.77 (10:05 iex) | -2.4% | 188.31 | 183.50 / 182.77-187.86 | 4.15 (2.2%) | 182.40-196.93 | -0.5% / -6.0% | -1.6% | 7.6M |
| DAL | 78.64 (10:05 iex) | -0.7% | 79.16 | 80.01 / 78.53-80.74 | 3.05 (3.9%) | 74.14-85.93 | -1.2% / -1.7% | +6.1% | 7.4M |
| UAL | 100.41 (10:04 iex) | -0.3% | 100.69 | 101.94 / 100.33-102.57 | 4.85 (4.8%) | 94.54-115.20 | -3.9% / -7.3% | +5.3% | 5.1M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-27 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AIOK | 15.49 (10:04 iex) | +69.1% | 9.16 | 13.60 / 13.60-17.72 | 2.30 (25.1%) | 3.90-15.59 | - / - | +130.2% | 3.9M |
| SOFX | 6.90 (10:04 iex) | +21.5% | 5.68 | 6.86 / 6.63-7.11 | 0.50 (8.9%) | 5.32-7.37 | -11.3% / -28.6% | +1.6% | 1.5M |
| NEBX | 12.57 (10:04 iex) | +19.4% | 10.53 | 11.37 / 11.28-13.01 | 2.88 (27.4%) | 10.05-31.11 | -47.1% / -54.6% | -20.3% | 2.9M |
| NBIG | 8.45 (10:04 iex) | +19.2% | 7.09 | 7.69 / 7.59-8.75 | 1.95 (27.5%) | 6.76-20.96 | -47.1% / -54.5% | -20.2% | 4.1M |
| NBIL | 12.32 (10:04 iex) | +18.9% | 10.36 | 11.14 / 11.03-12.75 | 2.83 (27.3%) | 9.81-30.43 | -46.8% / -54.2% | -19.8% | 6.1M |
| BEX | 20.65 (09:53 iex) | +12.8% | 18.31 | 20.09 / 19.60-21.62 | 4.46 (24.4%) | 15.66-42.95 | -39.9% / -39.3% | -21.1% | 3.2M |
| IREX | 5.51 (10:04 iex) | +15.8% | 4.76 | 4.90 / 4.81-5.57 | 1.33 (28.0%) | 4.14-15.26 | -47.6% / -62.9% | -17.6% | 4.4M |
| SAIQ | 7.70 (10:02 iex) | +14.4% | 6.73 | 7.23 / 7.23-8.09 | 1.55 (23.0%) | 1.76-11.74 | +34.0% / -19.4% | +97.4% | 10.3M |
| INOD | 47.19 (10:04 iex) | -21.2% | 59.91 | 48.62 / 44.58-48.90 | 3.62 (6.0%) | 50.68-75.19 | -2.1% / -0.4% | +10.9% | 1.1M |
| NBIZ | 34.76 (10:03 iex) | -17.7% | 42.25 | 39.08 / 32.60-39.44 | 4.97 (11.8%) | 17.01-44.03 | +51.6% / +61.4% | +21.4% | 1.8M |
| BEZ | 6.66 (10:04 iex) | -15.8% | 7.91 | 7.07 / 6.43-7.31 | 1.02 (13.0%) | 4.08-9.16 | +34.8% / +9.7% | +13.3% | 5.6M |
| IREZ | 18.80 (10:01 iex) | -13.6% | 21.76 | 21.16 / 18.15-21.59 | 2.86 (13.1%) | 8.32-24.83 | +46.4% / +82.6% | +14.4% | 1.9M |
