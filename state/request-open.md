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

## Pre-market brief, Wednesday 2026-10-28 (09:05 ET / 14:05 Stockholm)

### 1. Tape
Semis drove the tape higher yesterday. The SOX rose 3.6% for a third straight up day on the Anthropic IPO filing, and the S&P 500 gained 0.6% to 7,722 while the Nasdaq added 1.2%. This morning SK Hynix's record quarter (operating profit up about 7x) is lifting memory and AI names: NQ futures are up about 0.4%, ES about 0.1%, and the Dow is down about 0.2%. Oil is the other side of the story. Brent is around $115 and WTI around $101.5 (+1.5–2%) after the Houthis claimed a missile strike on Ras Tanura, and after reports that Washington has told Gulf states to prepare for renewed strikes on Iran after the Nov 3 midterms. The 10-year is about 4.99%. The day is set by the FOMC at 14:00 ET, where a hold is about 92% priced and a "hawkish pause" is the common call, and then by MSFT and GOOGL after the close. The regime is a narrow AI-led risk-on with an inflation and oil undercurrent. The edge on index direction is flat. On themes it is long energy, and short the AI losers where the earnings have already landed (META).

### 2. Calendar
| Time ET | Stockholm | Event | Status / consensus | Touches |
|---|---|---|---|---|
| 07:00 | 12:00 | MBA mortgage apps | Released; no market impact found (not verified) | KRE |
| 08:30 | 13:30 | Adv. goods trade balance (Sep) | Released; I could not verify the figure; futures did not move on it | — |
| pre-mkt | — | Earnings: GEV (beat, $4.81 vs $4.00), VRT (beat and raise), BSX (guide cut), BIIB (beat), RCL, SPGI, JCI up; HOOD −7–8%, ENPH −18% | Released | XLV (BSX) |
| 10:30 | 15:30 | EIA crude inventories | Ahead | XLE play |
| 14:00 | 19:00 | FOMC decision, then presser at 14:30 | Hold at 3.75–4.00% expected; risk is a hawkish tone | All |
| After close | ~21:05 | MSFT, GOOGL (also NOW, F, CMG, TMUS, EBAY today) | Ahead | NVDA, META, TSLA, QQQ |
| Thu 10/29 AMC | — | AMZN | Ahead | — |
| Fri 10/30 BMO | — | XOM, CVX | Ahead | XLE play (ETF, see below) |

### 3. Open positions
- **NVDA short (212.38, last ~219.4, stop 222): thesis invalidated. Close.** The thesis was that the bounce had failed. Instead semis put in a third up day (SOX +3.6% yesterday), and SK Hynix is adding AI-memory momentum this morning. Holding into MSFT/GOOGL capex guidance tonight risks a gap through 222. Taking about −0.75R now is better than giving the event a free option on a full or larger loss.
- **TSLA long (398.69, last ~410, stop 384, target 421): intact.** It is above the 408.45 20-day high. I'm raising the stop to 395. That is just under the 397–399 breakout zone, and the position no longer costs a full R if FOMC or MSFT/GOOGL reverse it overnight. The target stays at 421.
- **KRE long (73.06, last 72.41, stop 71.25): intact.** A steep curve with the 10-year near 5% supports NIMs. The stop is about 1 ATR below the 20-day high band. Hold.
- **XLV long (179.57, last 178.05, stop 176.40): weakening.** BSX cut guidance and JNJ is down 1.2% pre-market, and yesterday the money rotated into semis rather than defensives. The structure still holds, with XLV 3.4% above its 20-day average. Hold, leaving the stop where it is; the review has a condition below.
- There are no resting entries.

### 4. New plays

**XLE long: probe on an oil-driven breakout**
| Field | Value |
|---|---|
| Ticker | XLE |
| Direction | Long |
| Catalyst | 2026-10-27/28: Houthi missile claim on Ras Tanura (550k b/d), reports of US strikes on Iran resuming after Nov 3, Brent about $115, UBS raising its oil forecast to about $110 through year-end |
| Thesis | Energy is already 5.9% above its 50-day average and USO is up 1.9% pre-market. A move through the 69.86 20-day high would confirm that equities are repricing $100+ oil while the AI trade takes the headlines. |
| Entry | Buy stop at 70.00 (pre-market 68.67; the trigger is above the market) |
| Stop | 67.90. That is about 1.4 ATR below the trigger and under this morning's pre-market level; back there, the breakout has failed. |
| Target | 73.20 (+1.5R) |
| Risk tier | 0.5. The catalyst is geopolitical headline risk, a Qatar-brokered Iran deal could gap it down, and XOM and CVX (about 40% of the ETF) report Friday. Under rule 8 an ETF is not a single-name binary, but the weight is worth flagging. |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 38% |
| Invalidation | Brent back under $108, or a signed Iran deal |
| What I'd be wrong about | Oil is already extreme and crowded. My last XOM long scratched. Any de-escalation headline unwinds it fast, and a hawkish Fed hits cyclicals. |

**META short: probe on post-earnings drift breaking the range low**
| Field | Value |
|---|---|
| Ticker | META |
| Direction | Short |
| Catalyst | Earnings reported 10/21. The stock is down 10.7% over 5 days and sits at its 619.21 20-day low (pre-market 621.56). The next earnings are in January, so there is no rule-8 event inside the horizon. |
| Thesis | The market is punishing META's capex without a cloud business to monetize it. A break below the 20-day low continues the drift toward 580. |
| Entry | Sell stop at 616.50 (below pre-market and below the 619.21 low) |
| Stop | 643.00. That is about 1 ATR above the trigger and above the 640s pre-breakdown area. |
| Target | 580.00 (+1.38R) |
| Risk tier | 0.25. GOOGL/MSFT tonight could produce a sympathy bounce in ad and AI names, and META has 4.1% ATR noise. |
| Time horizon | 1–4 days |
| Conviction | 2 |
| P(target before stop) | 35% |
| Invalidation | GOOGL ad revenue beats strongly and META reclaims 640 |
| What I'd be wrong about | It is down 12% from its highs and oversold, so a strong GOOGL Search/ads print could spark a sharp short-covering rally. |

### 5. Both sides
- **Best long:** XLE, 70.00 stop entry, stop 67.90, target 73.20, P = 38%. Taken.
- **Best short:** META, 616.50 stop entry, stop 643, target 580, P = 35%. Taken as a probe. I also looked at HOOD (−7–8% on the miss) but could not verify a pre-market price, so no levels. On UAL (oil up, −1.5% pre-market), my last UAL short stopped out; it is passed below with levels.

### 6. Passing on
- **UAL short** (101.50 stop entry / 106.50 / 95.00, P 33%): the oil headwind is real, but it has a 4.8% ATR and the stock is up 7% over 5 days. It is in `passed`.
- **XLC short** (102.90 stop entry / 106.00 / 98.00, P 33%): this is GOOGL earnings exposure tonight in disguise, and it overlaps META. In `passed`.
- **HOOD short:** post-earnings drift, but there is no verified price, so no levels.
- **GEV long:** the beat is mostly priced (+0.5% pre-market at about 900) and I have no ATR or range data.
- **TLT long** (82.05 / 80.70 / 84.20, P 30%): a hawkish-pause risk at 14:00 ET, with oil feeding inflation. In `passed`.

### 7. For the post-open review
- **NVDA:** closed at market at the open. Confirm the fill.
- **XLV:** if it is below 177.00 at 10:05 with health care leading the S&P lower on the BSX read-through, close it rather than carry it into FOMC. Above 177, hold.
- **XLE:** if it has already triggered and is back under 69.50 by 10:05, close it, because the breakout failed.
- **META:** if it triggered at the open and is back above 625 by 10:05, close it.
- **TSLA:** if it is back under 400 at 10:05 with QQQ red, close it rather than trail it.

### 8. Book state
Once both entries fill (NVDA closed), gross is about 50% of equity in longs plus a META short notional of about 4%, so roughly 54% against the 150% cap. Net is about +43% against ±100%. Six of 8 slots are used. Risk at stake is about 1.0% of equity (cap 4%): roughly KRE 0.18, XLV 0.50, TSLA 0.06, XLE 0.5 and META 0.25, with the NVDA and TSLA changes taking out about 0.43.

```json
{
  "date": "2026-10-28",
  "no_trade": false,
  "session_note": "AI-led risk-on (SK Hynix) vs Brent $115 and 10y ~5% into a 14:00 ET hawkish-pause FOMC and MSFT/GOOGL AMC; close the invalidated NVDA short, trail TSLA, add an XLE breakout long (0.5) and a META post-earnings breakdown short probe (0.25).",
  "plays": [
    {
      "ticker": "XLE",
      "direction": "long",
      "entry_type": "stop",
      "entry": 70.00,
      "stop": 67.90,
      "targets": [73.20],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "2026-10-27/28 Houthi strike claim on Ras Tanura and reports of US strikes on Iran resuming after Nov 3 midterms; Brent ~$115, UBS raises forecast.",
      "thesis": "Energy equities are repricing $100+ oil; a break of the 69.86 20d high confirms the breakout while AI dominates headlines.",
      "invalidation": "Brent back under $108 or a signed US-Iran deal.",
      "bear_case": "Crowded oil trade; de-escalation headline or hawkish Fed could reverse it, and XOM/CVX (~40% of XLE) report Fri 10/30."
    },
    {
      "ticker": "META",
      "direction": "short",
      "entry_type": "stop",
      "entry": 616.50,
      "stop": 643.00,
      "targets": [580.00],
      "time_horizon": "1-4 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.35,
      "catalyst": "Post-10/21-earnings drift: -10.7% in 5 days, sitting on the 619.21 20d low pre-market at 621.56; no earnings inside horizon.",
      "thesis": "Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward 580.",
      "invalidation": "Strong GOOGL ads print and META reclaims 640.",
      "bear_case": "Oversold after a 12% drop; GOOGL/MSFT strength tonight could trigger a sharp short-covering bounce."
    }
  ],
  "manage": [
    {
      "ticker": "NVDA",
      "action": "close",
      "reason": "Breakdown thesis invalidated by a three-day semis rally and SK Hynix blowout; do not carry the short into MSFT/GOOGL capex guidance tonight."
    },
    {
      "ticker": "TSLA",
      "action": "update",
      "stop": 395.00,
      "reason": "Above the 408.45 20d high; trail the stop just under the 397-399 breakout zone ahead of FOMC and MSFT/GOOGL."
    }
  ],
  "passed": [
    {
      "ticker": "UAL",
      "direction": "short",
      "entry_type": "stop",
      "entry": 101.50,
      "stop": 106.50,
      "targets": [95.00],
      "p_target_first": 0.33,
      "reason": "Oil headwind real but 4.8% ATR and +7% in 5d; last UAL short stopped out."
    },
    {
      "ticker": "XLC",
      "direction": "short",
      "entry_type": "stop",
      "entry": 102.90,
      "stop": 106.00,
      "targets": [98.00],
      "p_target_first": 0.33,
      "reason": "Effectively a bet on GOOGL earnings tonight, and overlaps the META short."
    },
    {
      "ticker": "TLT",
      "direction": "long",
      "entry_type": "stop",
      "entry": 82.05,
      "stop": 80.70,
      "targets": [84.20],
      "p_target_first": 0.30,
      "reason": "Hawkish-pause FOMC risk with oil feeding inflation."
    }
  ]
}
```

Sources: [Yahoo live Oct 28](https://ca.finance.yahoo.com/news/live/stock-market-today-wednesday-october-28-dow-sp-500-nasdaq-fed-meeting-decision-080642111.html), [Investrade morning preview](https://investrade.com/morning-preview-october-28-2026/), [CNBC premarket movers](https://www.cnbc.com/2026/10/28/stocks-making-the-biggest-moves-premarket-ulbi-slhy-hood-enph.html), [HDFC Sky Oct 27 close](https://hdfcsky.com/news/nasdaq-jumps-1-2percent-as-chip-stocks-rally-oil-slides-and-fed-meeting-begins-october-28-2026), [The National: oil](https://www.thenationalnews.com/business/energy/2026/10/28/oil-prices-up-due-to-houthi-strikes-and-us-threat-to-renew-iran-war/), [CNBC oil](https://www.cnbc.com/2026/10/28/oil-price-today-wti-brent-hormuz.html), [Daily Sabah Brent](https://www.dailysabah.com/business/energy/brent-prices-hit-115-amid-concerns-over-saudi-refinery-attack), [Yahoo HOOD](https://finance.yahoo.com/markets/stocks/article/robinhood-stock-falls-7-after-earnings-miss-despite-record-trading-volumes-230753553.html), [Sentisense earnings dates](https://sentisense.ai/blog/big-tech-earnings-this-week/), [Investing.com GEV](https://ng.investing.com/news/stock-market-news/earnings-call-transcript-ge-vernova-tops-q3-2026-forecasts-on-orders-and-cash-93CH-2763481), [Kiplinger Fed](https://www.kiplinger.com/investing/live/fed-meeting-updates-and-commentary-october-2026)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC, 15:05 Stockholm), Wednesday 2026-10-28. The cash session opened 35 min ago and closes at 16:00 ET (21:00 Stockholm).
- Equity: **$102,220.49**
- Cash: $61,906.63
- Session P&L so far: -0.09% (new entries are blocked at -3.0%)
- Gross exposure: $68,443 (67% of equity, cap 150%)
- Net exposure: $+57,321 (+56%, cap +/-100%)
- Risk at stake (entry to stop): $1,578 (1.54% of equity, cap 4.0%) — 2.46% left for new plays
- Slots: 4 open + 1 resting entries of 8 — you may add at most 3 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 44% of equity in notional: at 1% risk its stop must be at least 2.3% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| KRE | long | 142 | 73.06 | 72.29 | -109 (-1.1%) | 71.25 | 76.20 | Regional banks are among the few groups making new highs while AI capex unwinds; NIM widening and a steep curve support  |
| META | short | 9 | 616.20 | 617.90 | -15 (-0.3%) | 643.00 | 580.00 | Market is punishing META capex without a cloud business to monetize it; a break of the 20d low extends the drift toward  |
| TSLA | long | 17 | 398.69 | 399.17 | +8 (+0.1%) | 395.00 | 421.00 | Relative strength at the range top while megacap tech chops; a clean 20d-high break opens room toward 420. |
| XLV | long | 160 | 179.57 | 180.13 | +90 (+0.3%) | 176.40 | 184.80 | Capital leaving AI capex is rotating into staples and health care, and XLV is breaking out of its 20-day range. It diver |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| XLE | long | 243 | 70.00 | stop | 67.90 | 73.20 | 2026-10-28 |

### Record

30 closed trades: 11W / 19L, total +2.01R, net $+2,254 realized. Shorts taken: 28.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| NVDA | short | close | -0.76R | $-190 | 35% |
| XOM | long | stop | -0.07R | $-37 | 37% |
| BA | short | target | +1.52R | $+379 | 34% |
| ORCL | short | stop | -0.06R | $-16 | 33% |
| UAL | short | stop | -0.45R | $-315 | 40% |

### Ideas you passed on, replayed against the tape

65 resolved: 18 reached target first, 33 stop first, 11 never reached the entry, 3 expired, 0 ambiguous. Average -0.13R across the 54 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-23 open | CAT | short | Under its 695 20d low, but the Q3 earnings date is likely inside the horizon and | stop | -1.04R | 38% |
| 2026-10-22 pre-market | AVGO | short | Same AI factor as the existing shorts; no slot. | stop | -1.10R | 35% |
| 2026-10-21 pre-market | UNH | long | Healthcare soft pre-market on ISRG/TMO; prefer to spend the risk on energy. | stop | -1.00R | 35% |
| 2026-10-19 pre-market | AMD | short | Same idea as the SMH short with twice the noise; one semi short is enough. | never filled | - | 38% |
| 2026-10-19 pre-market | BAC | short | Post-earnings damage already priced; my last bank short stopped out. | never filled | - | 30% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| KRE | 72.29 (10:05 iex) | -0.4% | 72.58 | 72.58 / 72.25-72.81 | 1.23 (1.7%) | 67.79-73.42 | +3.3% / +0.8% | +2.8% | 15.8M |
| META | 618.01 (10:05 iex) | -0.4% | 620.19 | 621.63 / 614.10-624.42 | 25.40 (4.1%) | 619.21-771.27 | -12.3% / -6.8% | -10.7% | 20.8M |
| TSLA | 399.50 (10:05 iex) | -2.0% | 407.46 | 410.21 / 399.05-410.85 | 13.78 (3.4%) | 345.88-408.45 | +8.9% / +11.3% | +9.0% | 37.9M |
| XLV | 180.15 (10:05 iex) | +0.5% | 179.18 | 177.63 / 177.07-180.37 | 2.99 (1.7%) | 165.19-182.25 | +3.4% / +4.6% | -0.4% | 8.7M |
| XLE | 68.27 (10:05 iex) | +0.1% | 68.21 | 68.47 / 68.14-68.61 | 1.49 (2.2%) | 61.04-69.86 | +3.2% / +5.9% | +0.4% | 32.0M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 770.83 (10:05 iex) | +0.2% | 769.66 | 771.43 / 769.24-771.70 | 7.28 (0.9%) | 758.68-781.62 | -0.1% / +0.4% | +0.1% | 39.8M |
| QQQ | 722.67 (10:05 iex) | +0.2% | 721.25 | 724.12 / 720.30-724.73 | 12.55 (1.7%) | 701.16-762.86 | -1.6% / -0.5% | +0.5% | 36.7M |
| IWM | 280.88 (10:05 iex) | +0.2% | 280.18 | 280.35 / 279.94-281.22 | 3.57 (1.3%) | 269.88-284.64 | +1.1% / -1.7% | +1.6% | 25.0M |
| DIA | 523.63 (10:05 iex) | +0.1% | 523.28 | 523.02 / 522.80-524.34 | 5.11 (1.0%) | 504.59-528.45 | +1.1% / +0.3% | -0.2% | 3.4M |
| TLT | 81.68 (10:05 iex) | +0.1% | 81.63 | 81.72 / 81.61-81.75 | 0.79 (1.0%) | 76.43-81.92 | +3.2% / +1.7% | +1.9% | 44.1M |
| GLD | 370.95 (10:04 iex) | -0.4% | 372.28 | 371.29 / 370.76-371.40 | 5.07 (1.4%) | 364.33-385.22 | -1.5% / -5.3% | -1.4% | 7.8M |
| USO | 166.82 (10:02 iex) | +1.8% | 163.88 | 166.55 / 166.34-167.08 | 4.74 (2.9%) | 141.76-169.96 | +6.0% / +10.8% | +2.0% | 4.7M |
| SMH | 565.75 (10:05 iex) | +1.4% | 557.98 | 564.32 / 560.51-565.98 | 19.42 (3.5%) | 520.53-639.47 | -3.8% / -2.7% | +2.1% | 8.7M |
| XLK | 190.28 (10:05 iex) | +0.4% | 189.49 | 190.58 / 189.38-190.90 | 4.34 (2.3%) | 181.50-203.25 | -1.6% / +0.0% | +2.2% | 8.9M |
| XLF | 55.88 (10:05 iex) | +0.0% | 55.88 | 55.84 / 55.80-56.06 | 0.71 (1.3%) | 52.81-56.67 | +1.8% / -0.0% | +0.3% | 34.2M |
| XLE | 68.27 (10:05 iex) | +0.1% | 68.21 | 68.47 / 68.14-68.61 | 1.49 (2.2%) | 61.04-69.86 | +3.2% / +5.9% | +0.4% | 32.0M |
| XLV | 180.15 (10:05 iex) | +0.5% | 179.18 | 177.63 / 177.07-180.37 | 2.99 (1.7%) | 165.19-182.25 | +3.4% / +4.6% | -0.4% | 8.7M |
| XLI | 168.01 (10:05 iex) | +0.1% | 167.92 | 168.95 / 167.29-168.95 | 2.49 (1.5%) | 162.97-172.34 | -0.1% / -2.0% | +0.7% | 7.5M |
| XLY | 114.97 (10:05 iex) | -0.4% | 115.45 | 115.37 / 114.91-115.67 | 1.65 (1.4%) | 107.99-116.22 | +2.6% / +2.0% | -0.0% | 7.1M |
| XLP | 86.74 (10:05 iex) | -0.5% | 87.15 | 86.43 / 86.36-86.88 | 1.41 (1.6%) | 80.10-89.99 | +2.7% / +3.5% | -0.7% | 13.9M |
| XLU | 42.70 (10:05 iex) | -0.4% | 42.85 | 42.83 / 42.47-42.97 | 0.62 (1.4%) | 39.10-42.89 | +3.4% / +2.9% | +2.3% | 33.6M |
| XLB | 51.52 (10:05 iex) | -0.5% | 51.78 | 51.42 / 51.27-51.67 | 0.65 (1.2%) | 47.81-51.88 | +3.3% / +1.8% | +1.1% | 11.2M |
| XLRE | 41.96 (10:03 iex) | -1.1% | 42.44 | 42.16 / 41.78-42.23 | 0.64 (1.5%) | 40.28-43.21 | +1.9% / -0.4% | +0.1% | 8.1M |
| XLC | 103.31 (10:05 iex) | -0.3% | 103.58 | 103.38 / 103.17-103.88 | 1.74 (1.7%) | 103.20-113.17 | -5.6% / -6.8% | -6.0% | 6.6M |
| KRE | 72.29 (10:05 iex) | -0.4% | 72.58 | 72.58 / 72.25-72.81 | 1.23 (1.7%) | 67.79-73.42 | +3.3% / +0.8% | +2.8% | 15.8M |
| XHB | 98.97 (10:03 iex) | -0.2% | 99.16 | 99.14 / 98.33-99.58 | 2.24 (2.3%) | 91.87-99.32 | +3.2% / +0.4% | +3.1% | 2.0M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.34 (10:05 iex) | -0.5% | 347.10 | 346.94 / 344.63-347.20 | 6.36 (1.8%) | 325.81-351.73 | +2.1% / +4.8% | +2.2% | 39.2M |
| MSFT | 529.06 (10:05 iex) | -0.4% | 531.33 | 532.08 / 529.18-534.57 | 11.07 (2.1%) | 510.31-551.15 | +0.4% / +4.2% | -0.1% | 20.2M |
| NVDA | 218.32 (10:05 iex) | +0.2% | 217.94 | 219.91 / 217.31-219.99 | 6.20 (2.8%) | 210.18-243.37 | -2.9% / -1.9% | +0.7% | 102.7M |
| AMZN | 253.44 (10:05 iex) | +0.1% | 253.10 | 252.89 / 252.47-255.36 | 6.87 (2.7%) | 246.08-265.34 | -0.7% / -0.8% | -3.6% | 35.9M |
| GOOGL | 324.94 (10:05 iex) | +1.4% | 320.58 | 323.85 / 323.17-326.40 | 8.37 (2.6%) | 316.60-359.40 | -5.9% / -6.2% | -5.8% | 24.5M |
| META | 618.01 (10:05 iex) | -0.4% | 620.19 | 621.63 / 614.10-624.42 | 25.40 (4.1%) | 619.21-771.27 | -12.3% / -6.8% | -10.7% | 20.8M |
| TSLA | 399.50 (10:05 iex) | -2.0% | 407.46 | 410.21 / 399.05-410.85 | 13.78 (3.4%) | 345.88-408.45 | +8.9% / +11.3% | +9.0% | 37.9M |
| AVGO | 347.76 (10:05 iex) | +1.6% | 342.33 | 349.48 / 345.10-351.62 | 11.84 (3.5%) | 320.23-380.84 | -1.4% / -3.3% | +2.4% | 21.9M |
| AMD | 564.22 (10:05 iex) | +0.7% | 560.26 | 572.93 / 561.25-573.96 | 29.65 (5.3%) | 502.60-658.52 | -3.6% / +3.0% | +4.8% | 19.5M |
| ORCL | 130.56 (10:05 iex) | +0.0% | 130.53 | 131.32 / 129.59-131.81 | 6.82 (5.2%) | 122.76-146.40 | -3.1% / -7.9% | -0.5% | 27.7M |
| NFLX | 61.81 (10:05 iex) | -1.1% | 62.52 | 61.91 / 61.66-62.65 | 2.21 (3.5%) | 62.48-73.07 | -8.7% / -15.2% | -9.0% | 43.7M |
| CRM | 242.71 (10:05 iex) | +0.8% | 240.89 | 237.52 / 237.01-244.19 | 8.74 (3.6%) | 220.29-252.42 | +1.5% / +1.7% | -0.6% | 7.5M |
| JPM | 335.80 (10:05 iex) | +0.0% | 335.79 | 337.38 / 335.17-337.53 | 6.31 (1.9%) | 324.25-344.40 | +0.8% / -2.1% | +0.2% | 7.2M |
| GS | 917.46 (10:05 iex) | +0.6% | 911.77 | 920.00 / 913.99-922.00 | 24.86 (2.7%) | 859.03-931.00 | +2.3% / -4.3% | +3.0% | 2.3M |
| BAC | 50.77 (10:05 iex) | +0.2% | 50.68 | 50.90 / 50.64-50.99 | 1.29 (2.6%) | 49.26-55.11 | -3.4% / -11.2% | +0.1% | 42.5M |
| XOM | 180.91 (10:04 iex) | +0.6% | 179.91 | 180.59 / 180.00-181.37 | 4.05 (2.3%) | 160.81-184.88 | +4.1% / +8.0% | +1.2% | 11.6M |
| CVX | 229.28 (10:05 iex) | +0.5% | 228.23 | 228.88 / 228.34-229.58 | 4.92 (2.2%) | 201.96-234.08 | +4.8% / +7.9% | +1.1% | 7.3M |
| LLY | 1,291.17 (10:03 iex) | +0.7% | 1,281.91 | 1,268.55 / 1,260.34-1,293.37 | 38.70 (3.0%) | 1,131.21-1,321.21 | +5.5% / +7.7% | -0.1% | 2.4M |
| UNH | 413.38 (10:05 iex) | +0.7% | 410.39 | 407.00 / 405.00-414.68 | 13.06 (3.2%) | 362.60-426.55 | +4.5% / +5.7% | -2.1% | 6.1M |
| JNJ | 269.67 (10:05 iex) | +0.3% | 268.73 | 265.83 / 264.20-269.79 | 7.21 (2.7%) | 245.17-272.36 | +3.8% / +1.3% | +3.6% | 7.9M |
| WMT | 118.67 (10:05 iex) | -0.5% | 119.32 | 118.42 / 118.11-118.88 | 2.57 (2.2%) | 103.39-122.40 | +5.2% / +8.9% | +1.2% | 20.6M |
| COST | 982.47 (10:05 iex) | -1.0% | 992.13 | 983.61 / 980.32-984.73 | 16.48 (1.7%) | 903.77-1,021.45 | +2.7% / +5.5% | -0.2% | 2.1M |
| HD | 319.18 (10:05 iex) | +0.2% | 318.50 | 317.55 / 316.94-320.43 | 7.59 (2.4%) | 277.15-327.92 | +6.0% / +3.2% | +1.1% | 5.1M |
| CAT | 712.41 (10:05 iex) | -0.1% | 713.31 | 730.00 / 709.24-732.73 | 26.49 (3.7%) | 679.50-874.87 | -7.0% / -9.9% | -1.4% | 2.7M |
| BA | 166.06 (10:05 iex) | -1.3% | 168.18 | 167.99 / 165.01-170.20 | 5.39 (3.2%) | 167.41-196.93 | -10.7% / -15.5% | -11.7% | 9.5M |
| DAL | 81.67 (10:05 iex) | +0.3% | 81.45 | 81.26 / 81.20-82.08 | 3.14 (3.9%) | 74.14-85.93 | +1.9% / +1.2% | +6.2% | 7.4M |
| UAL | 104.98 (10:05 iex) | +0.3% | 104.71 | 104.32 / 103.91-105.55 | 5.00 (4.8%) | 94.54-115.20 | +0.4% / -3.3% | +7.1% | 5.2M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-28 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BRAI | 5.28 (10:04 iex) | +59.5% | 3.31 | 4.93 / 4.44-5.31 | 0.76 (23.0%) | 2.10-5.62 | -23.8% / -34.5% | -22.8% | 3.0M |
| AIOK | 16.87 (10:04 iex) | +25.7% | 13.42 | 17.53 / 16.02-18.99 | 2.82 (21.0%) | 3.90-17.72 | - / - | +172.2% | 5.9M |
| SKHX | 12.23 (10:05 iex) | +23.3% | 9.92 | 11.56 / 11.43-12.18 | 1.19 (12.0%) | 8.07-18.93 | -21.4% / -31.3% | +6.6% | 2.6M |
| SKUU | 20.64 (10:04 iex) | +22.9% | 16.80 | 19.58 / 19.38-20.64 | 2.00 (11.9%) | 13.64-31.80 | -21.0% / -30.7% | +6.9% | 2.3M |
| AXGN | 45.91 (10:05 iex) | +22.6% | 37.46 | 45.45 / 43.50-46.30 | 1.37 (3.6%) | 34.11-43.09 | +1.5% / -12.5% | +3.6% | 1.5M |
| SKHL | 7.93 (10:05 iex) | +22.8% | 6.46 | 7.53 / 7.42-7.88 | 0.76 (11.8%) | 5.24-12.21 | -20.9% / -30.6% | +7.0% | 2.2M |
| GMAB | 52.48 (10:05 iex) | +17.5% | 44.67 | 44.63 / 44.35-52.91 | 1.44 (3.2%) | 33.73-45.45 | +16.5% / +25.1% | +14.3% | 5.2M |
| WEN | 7.08 (10:05 iex) | +15.2% | 6.14 | 7.04 / 7.01-7.20 | 0.26 (4.2%) | 5.94-6.82 | -3.1% / -14.1% | -5.8% | 5.2M |
| SKDD | 7.88 (10:05 iex) | -23.3% | 10.28 | 8.53 / 7.91-8.69 | 1.12 (10.9%) | 6.22-12.85 | +9.7% / +15.4% | -10.8% | 3.6M |
| BBNX | 18.02 (10:05 iex) | -15.8% | 21.39 | 18.71 / 17.84-20.07 | 1.14 (5.3%) | 16.32-22.29 | +16.6% / +11.2% | +20.6% | 1.0M |
| SAIQ | 6.39 (10:03 iex) | -15.0% | 7.52 | 6.77 / 6.27-6.77 | 1.52 (20.2%) | 1.76-10.46 | +54.2% / -9.3% | +9.9% | 10.5M |
| ENPH | 25.18 (10:04 iex) | -15.4% | 29.76 | 23.85 / 23.83-25.91 | 1.74 (5.8%) | 28.59-34.19 | -6.7% / -13.5% | -7.7% | 5.3M |
| SLS | 10.49 (10:05 iex) | -13.8% | 12.17 | 12.14 / 9.71-12.44 | 0.91 (7.5%) | 9.75-12.70 | +5.3% / -1.5% | +1.6% | 5.8M |
