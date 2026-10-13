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

# Pre-market brief: Tuesday 2026-10-13 (09:05 ET / 15:05 Stockholm)

### 1. Tape
The market is split. Nasdaq-100 futures are down about 0.6–0.8% while Dow futures are up 0.2–0.8%, depending on the source and the time. Chips are selling off again across the world. China's CXMT said it has made progress on a denser memory-cell design ("4F²"), and the KOSPI fell 5.5–6% overnight, with SK Hynix down about 10% and Samsung down about 7%. In US pre-market, Micron is down about 3–4%, SanDisk about 5% and WDC about 6%. In the data table, SMH is at 578.66 (−2.1%) and AMD at 581.70 (−2.1%), which leaves SMH −6.8% over five days. Money is moving into banks, healthcare and staples: GS +3.5% (925.00), UNH +4.4% (395.07), XLP +1.1% and above its 20-day high, and WMT and COST both above their 20-day highs. Oil is easing from the Houthi spike. Brent is about $104.6, down 1.9%, after briefly trading above $105, and WTI is about $92. The 10-year yield is about 5.19%, below last week's high near 5.4%. VIX is about 15.3. This is rotation, not risk-off. The short edge is in semis and the long edge is in defensives and in names that beat on earnings.

### 2. Calendar

| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| Pre-mkt (out) | — | JPM Q3 | EPS $5.57 vs about $5.92 consensus (miss, FICC weak). Stock still +0.5 to +1.9% pre-market. | XLF |
| Pre-mkt (out) | — | GS Q3 | Revenue $18.68B vs $16.71B (big beat). Stock +3.5%. | passed GS |
| Pre-mkt (out) | — | UNH Q3 | Adjusted EPS $4.69 vs $4.14, 2026 guidance raised. Stock +4.4%. | UNH play |
| Pre-mkt (out) | — | JNJ Q3 | EPS $2.59 (+$0.06 beat), guidance raised to $11.05–11.15. Stock −2.2% (2027 patent-cliff worry). | passed JNJ |
| Pre-mkt (out) | — | WFC, C Q3 | WFC profit up on loan growth. I have not verified the details. | XLF |
| 06:00 (out) | 12:00 | NFIB small business index | I have not verified the figure. | — |
| 10:00 | 16:00 | Existing home sales (Sep) | I have not verified the consensus. | — |
| Wed 08:30 | Wed 14:30 | **September CPI** | Headline +0.6% m/m (3.6% y/y), core +0.2% m/m (2.5% y/y) | all. Ambient macro risk under rule 8, not a binary event |
| Thu 08:30 | Thu 14:30 | PPI, retail sales, jobless claims, Philly Fed | Retail sales +0.3% | all |
| Fri | | Fed Chair Warsh speaks | December hike about 75% priced on Polymarket | all |

### 3. Open positions and resting entries
- **MSFT long** (527.65 entry, last 543.95, stop 528 at breakeven, target 548): **thesis intact.** MSFT is holding up (+0.5%) while the rest of tech sells off, and the target is 0.7% away. I am keeping the levels as they are. The stop is already at breakeven, and moving it to about 532 would put it inside one ATR (12.2) on a day when tech is volatile. No change.
- **XOM long** (171.98 entry, last 173.21, stop 167.80, target 179): **thesis intact, slightly weaker.** Brent has come off its high, but XOM is still higher pre-market and sits above its 20-day high of 172.55. The stop is below the breakout level and about 1.6 ATR away. Hold with no change. If Brent falls under $100 I would close it, and I'll note that for the review.
- No resting entries.

### 4. New plays

**UNH: long on the post-earnings pullback**

| Field | Value |
|---|---|
| Ticker | UNH |
| Direction | Long |
| Catalyst | Q3 beat and raised guidance on 2026-10-13 pre-market: adjusted EPS $4.69 vs $4.14, 2026 guidance up on medical-cost control and Optum margins |
| Thesis | A beat-and-raise from a name that has been under pressure tends to keep drifting up for several days. The gap takes UNH above its 20-day high of 387.52. Buying a fade toward 391 puts the entry near the breakout level instead of at the opening high. |
| Entry | Limit 391.00 (pre-market 395.07) |
| Stop | 381.00. That is below the 387.52 breakout, and a fade to there would mean the market has rejected the earnings gap. It is about 1.1 ATR from entry. |
| Target | 410.00 (+1.9R) |
| Risk tier | 0.5. An earnings gap can fade sharply, and a limit buy into a fade carries extra risk. |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 42% |
| Invalidation | UNH closes back below 387.5 (the gap fails), or managed-care peers sell off on a policy headline |
| What I'd be wrong about | Gaps on the open often keep going, so the limit fills only if the stock is fading, and a fade is the weaker outcome for this trade. UNH also has a history of big rallies that later unwind. |

Reasoning: the earnings are now behind it, so rule 8 does not apply and there is nothing company-specific left in the horizon. Healthcare is one of the sectors taking the money leaving chips, with XLV at 173.17, above its 20-day high. I'm using a limit rather than a market order because I won't chase a 4.4% gap in the first minutes of trading.

**SMH: short on a bounce into the gap**

| Field | Value |
|---|---|
| Ticker | SMH |
| Direction | Short |
| Catalyst | CXMT memory-architecture news on 2026-10-13 (KOSPI −6%, SK Hynix −10%). Second day in a row of chip-led selling. |
| Thesis | Semis are down 6.8% in five days and have dropped below their 20-day average. Overseas, the memory complex is being repriced. A bounce toward the prior close of 590.99 should run into sellers. |
| Entry | Sell limit 587.00 (pre-market 578.66) |
| Stop | 603.00. That is above the prior close and above about 600, where a bounce would have filled the whole gap. It is about 1.2 ATR from entry. |
| Target | 556.00 (+1.9R) |
| Risk tier | 0.5. Semis are still above their 50-day average (+2.0%), so this is a short against the larger trend. My short record is also poor (14 taken, mostly stopped out). |
| Time horizon | 1–4 days |
| Conviction | 3 |
| P(target before stop) | 38% |
| Invalidation | SMH reclaims 591 and closes there, or CPI comes in soft on Wednesday and sets off a rush back into growth stocks |
| What I'd be wrong about | Similar CXMT-type scares have been bought before, and SMH's 20-day range has a 540 low, so dip buyers have been active. If the stock never bounces to 587, I miss the trade. A soft CPI tomorrow could also squeeze the shorts. |

The SMH short and the MSFT long are both tech, so they partly offset. MSFT is software with no memory exposure, so the pair is also a deliberate relative-value position.

### 5. Both sides
- **Best long:** UNH, limit 391, stop 381, target 410, P = 42%. **Taken** (section 4).
- **Best short:** SMH, limit 587, stop 603, target 556, P = 38%. **Taken** (section 4). I also looked at AMD (581.70, still +11.9% vs its 50-day average) and NVDA (224.13). Both are the same chip factor, so I'm using one expression.

### 6. Passing on
- **GS long** at about 925 market, stop 903, target 965, P = 38%. The revenue beat is large, but GS is −9.3% vs its 50-day average, so this would be buying a gap against the trend, and UNH is already my earnings-gap trade.
- **JNJ short** at about 258, stop 266, target 246, P = 33%. JNJ is down despite raising guidance because of the patent cliff. I was stopped out shorting JNJ two weeks ago, and selling a stock that just raised guidance is a fight with the fundamentals.
- **AMD short** at about 581.70, stop 606, target 545, P = 35%. Same factor as SMH, wider ATR (3.8%), and it would mean shorting into a gap.
- **COST/WMT long.** Both are breaking out of their ranges with staples, but both are extended (WMT +7.6% over five days). I'd want a pullback, and I couldn't find a structural level close enough to define the risk.
- **MU/SNDK short.** Neither is in my verified table and the pre-market quotes I found are thin, so I'm not trading either.

### 7. For the post-open review
- **SMH:** if it never bounces and trades below its opening-range low and under 572 by 10:00, cancel the 587 limit and consider a market short with a stop at 592 and a target at 552, at 0.5 risk. If it reclaims 591 by 10:00, cancel the limit, because the gap has filled and the short thesis is weaker.
- **UNH:** if the open holds above 395 and the 391 limit is clearly not going to fill, leave the limit in place and do not chase. If UNH trades under 387 by 10:00, the earnings gap is failing: cancel the limit, and close the position if it has already filled.
- **XOM:** close it if Brent is printing under $100. Otherwise, hold.
- **Existing home sales at 10:00:** no position depends on this release.

### 8. Book state
If both entries fill, gross exposure is about 78% (cap 150%) and net about +42% (cap ±100%). Risk at stake is about 1.5% of equity (cap 4%) and 4 of 8 slots are used. Net tech is about flat (MSFT long against the SMH short), and healthcare is about 20%.

```json
{
  "date": "2026-10-13",
  "no_trade": false,
  "session_note": "Rotation tape: chips hit by CXMT memory news (KOSPI -6%), banks/healthcare/staples bid on earnings; buy UNH beat-and-raise on a fade, short SMH into a bounce, hold MSFT and XOM.",
  "plays": [
    {
      "ticker": "UNH",
      "direction": "long",
      "entry_type": "limit",
      "entry": 391.00,
      "stop": 381.00,
      "targets": [410.00],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.42,
      "catalyst": "Q3 beat and 2026 guidance raise reported 2026-10-13 pre-market (adj EPS 4.69 vs 4.14); gap above 20d high 387.52.",
      "thesis": "Beat-and-raise from a beaten-down name tends to drift higher for days. Buying a fade toward 391 puts the entry near the breakout level instead of at the opening high.",
      "invalidation": "Close back under 387.5 (gap rejected) or a managed-care policy headline hitting peers.",
      "bear_case": "Opening gaps in UNH have faded before; the limit fills only on weakness, which is the less favorable path."
    },
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "limit",
      "entry": 587.00,
      "stop": 603.00,
      "targets": [556.00],
      "time_horizon": "1-4 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.38,
      "catalyst": "CXMT 4F2 memory-architecture news 2026-10-13; KOSPI -6%, SK Hynix -10%; second day of chip-led selling.",
      "thesis": "Semis are -6.8% over 5 days and below their 20d average while the memory complex is being repriced. A bounce toward the 590.99 prior close should meet supply.",
      "invalidation": "Reclaim and close above 591, or a soft CPI on 10-14 sparking a growth chase.",
      "bear_case": "Similar scares have been bought (20d low 540 held); still above 50d average; may never bounce to fill; soft CPI squeeze risk."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "GS",
      "direction": "long",
      "entry_type": "market",
      "entry": 925.00,
      "stop": 903.00,
      "targets": [965.00],
      "p_target_first": 0.38,
      "reason": "Big revenue beat but -9.3% vs 50d; would be buying a gap against the trend, and UNH is the earnings-gap trade."
    },
    {
      "ticker": "JNJ",
      "direction": "short",
      "entry_type": "market",
      "entry": 258.00,
      "stop": 266.00,
      "targets": [246.00],
      "p_target_first": 0.33,
      "reason": "Down on patent-cliff worry despite raising guidance; shorting a guidance raise, and I was stopped out shorting JNJ recently."
    },
    {
      "ticker": "AMD",
      "direction": "short",
      "entry_type": "market",
      "entry": 581.70,
      "stop": 606.00,
      "targets": [545.00],
      "p_target_first": 0.35,
      "reason": "Same chip factor as the SMH short; wider ATR and would be shorting into the gap."
    }
  ]
}
```

Sources: [Yahoo Finance live, Oct 13](https://finance.yahoo.com/markets/live/stock-market-today-tuesday-october-13-dow-sp-500-nasdaq-080236234.html), [Sunday Guardian futures](https://sundayguardianlive.com/business/us-stock-market-today-dow-futures-gain-018-sp-500-slips-013-nasdaq-falls-059-as-bank-earnings-offer-support-chip-stocks-slide-and-oil-prices-ease-check-what-investors-should-know-304917/), [BNN Bloomberg](https://www.bnnbloomberg.ca/markets/2026/10/13/wall-street-mixed-in-early-trading-as-big-us-banks-report-earnings-chip-stocks-fall-again/), [CNBC premarket movers](https://www.cnbc.com/2026/10/13/stocks-making-the-biggest-moves-premarket-jpm-mu-unh.html), [Yahoo Micron/CXMT](https://finance.yahoo.com/markets/stocks/articles/micron-stock-drops-china-cxmt-173326080.html), [TradingKey memory premarket](https://www.tradingkey.com/analysis/stocks/us-stocks/262213838-us-premarket-memory-chips-micron-sandisk-wd-fall-tradingkey), [GuruFocus JNJ](https://www.gurufocus.com/news/9120656/johnson-johnson-jnj-shares-dip-after-q3-results-and-raised-2026-outlook), [investingLive week ahead](https://investinglive.com/news/week-ahead-us-inflation-and-retail-sales-lead-a-busy-economic-calendar-be-aware/), [Rio Times Fed/oil](https://www.riotimesonline.com/global-economy-briefing-october-12-2026), [Bloomingbit Brent](https://en.bloomingbit.io/feed/news/121982)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Tuesday 2026-10-13. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$100,530.97**
- Cash: $79,495.12
- Session P&L so far: +0.06% (new entries are blocked at -3.0%)
- Gross exposure: $39,232 (39% of equity, cap 150%)
- Net exposure: $+2,838 (+3%, cap +/-100%)
- Risk at stake (entry to stop): $1,002 (1.00% of equity, cap 4.0%) — 3.00% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| XOM | long | 121 | 171.98 | 173.84 | +225 (+1.1%) | 167.80 | 179.00 | Energy is the clear sector leader with XLE and XOM through 20-day highs. Geopolitical escalation risk keeps the oil prem |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| SMH | short | 31 | 587.00 | limit | 603.00 | 556.00 | 2026-10-13 |

### Record

17 closed trades: 5W / 12L, total -3.93R, net $+310 realized. Shorts taken: 15.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |
| NVDA | long | stop | -0.38R | $-235 | 40% |
| IWM | long | close | -1.16R | $-590 | 40% |
| JNJ | short | stop | -1.02R | $-550 | 38% |

### Ideas you passed on, replayed against the tape

28 resolved: 5 reached target first, 18 stop first, 4 never reached the entry, 1 expired, 0 ambiguous. Average -0.40R across the 24 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-13 pre-market | GS | long | Big revenue beat but -9.3% vs 50d; would be buying a gap against the trend, and  | stop | -0.91R | 38% |
| 2026-10-01 pre-market | MSFT | long | dropped by the caps: would be 9 positions and resting entries, cap is 8 | target | +1.71R | 40% |
| 2026-10-05 open | GS | short | Weak (-1.4%) and near 20d low 881, but a third rates-factor short on top of JNJ/ | stop | -1.64R | 35% |
| 2026-10-06 pre-market | GS | short | Bank earnings around 10/14 at the edge of the horizon; financials bouncing pre-m | stop | -1.22R | 34% |
| 2026-10-07 pre-market | TLT | short | Purest rates-trend trade, but it doubles the HD factor and works against the IWM | stop | -1.08R | 38% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| XOM | 173.81 (10:04 iex) | +1.0% | 172.15 | 173.44 / 172.65-174.05 | 3.29 (1.9%) | 155.85-172.55 | +5.1% / +6.5% | +5.0% | 13.0M |
| SMH | 583.57 (10:04 iex) | -1.3% | 590.99 | 578.01 / 574.75-584.12 | 13.27 (2.2%) | 540.11-639.47 | -1.4% / +2.0% | -6.8% | 6.2M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 777.46 (10:05 iex) | -0.1% | 778.10 | 777.34 / 777.16-778.75 | 6.25 (0.8%) | 747.74-781.62 | +1.2% / +1.5% | +0.4% | 43.7M |
| QQQ | 743.94 (10:04 iex) | -0.3% | 746.04 | 739.53 / 738.83-744.18 | 8.46 (1.1%) | 699.27-762.86 | +0.9% / +2.9% | -1.3% | 33.7M |
| IWM | 276.49 (10:05 iex) | -0.5% | 277.90 | 277.98 / 276.34-278.70 | 3.59 (1.3%) | 274.52-288.94 | -1.3% / -4.4% | -1.9% | 24.9M |
| DIA | 517.10 (10:05 iex) | -0.2% | 517.91 | 522.74 / 517.13-522.80 | 4.58 (0.9%) | 504.70-522.55 | +0.7% / -1.3% | +1.1% | 3.4M |
| TLT | 78.24 (10:05 iex) | +0.2% | 78.05 | 78.56 / 78.22-78.57 | 0.85 (1.1%) | 76.43-81.61 | -1.1% / -3.2% | +1.2% | 48.4M |
| GLD | 381.82 (10:04 iex) | -0.1% | 382.15 | 383.93 / 381.78-384.00 | 5.84 (1.5%) | 374.23-403.15 | -1.4% / -3.8% | +0.7% | 8.1M |
| USO | 151.27 (10:04 iex) | +0.2% | 151.03 | 150.10 / 149.84-151.37 | 5.34 (3.5%) | 141.76-163.35 | +1.2% / +8.2% | +4.9% | 5.7M |
| SMH | 583.57 (10:04 iex) | -1.3% | 590.99 | 578.01 / 574.75-584.12 | 13.27 (2.2%) | 540.11-639.47 | -1.4% / +2.0% | -6.8% | 6.2M |
| XLK | 196.04 (10:05 iex) | -0.2% | 196.36 | 194.20 / 193.92-196.14 | 2.77 (1.4%) | 182.21-203.25 | +0.7% / +3.7% | -2.3% | 7.3M |
| XLF | 54.67 (10:05 iex) | -0.7% | 55.05 | 55.42 / 54.66-55.65 | 0.62 (1.1%) | 52.81-56.79 | +0.8% / -2.3% | +2.2% | 38.0M |
| XLE | 66.60 (10:05 iex) | +0.9% | 66.01 | 66.50 / 66.29-66.81 | 1.25 (1.9%) | 60.95-66.42 | +4.3% / +5.5% | +4.0% | 34.0M |
| XLV | 169.86 (10:05 iex) | -1.2% | 171.99 | 172.36 / 169.70-172.79 | 2.63 (1.5%) | 165.19-172.03 | +1.9% / +2.0% | +2.8% | 8.0M |
| XLI | 167.75 (10:05 iex) | -0.8% | 169.15 | 168.74 / 167.74-168.89 | 2.32 (1.4%) | 166.18-172.34 | -0.0% / -3.4% | -0.6% | 7.3M |
| XLY | 112.22 (10:05 iex) | -0.0% | 112.27 | 112.30 / 112.21-112.92 | 1.31 (1.2%) | 107.99-113.29 | +1.4% / -1.7% | +1.7% | 6.7M |
| XLP | 84.20 (10:05 iex) | -0.2% | 84.41 | 85.02 / 84.16-85.12 | 0.99 (1.2%) | 80.10-84.41 | +2.7% / +0.9% | +4.2% | 10.7M |
| XLU | 41.11 (10:05 iex) | -1.2% | 41.63 | 41.80 / 41.09-41.81 | 0.63 (1.5%) | 39.03-41.64 | +3.0% / -0.8% | +4.2% | 33.8M |
| XLB | 49.41 (10:05 iex) | -0.1% | 49.44 | 49.70 / 49.39-49.91 | 0.71 (1.4%) | 47.81-50.88 | -0.3% / -3.3% | -0.1% | 11.5M |
| XLRE | 41.60 (10:05 iex) | -0.8% | 41.92 | 42.34 / 41.62-42.34 | 0.57 (1.4%) | 40.28-43.13 | +0.8% / -2.8% | +3.1% | 6.9M |
| XLC | 112.69 (10:05 iex) | +1.1% | 111.45 | 111.59 / 111.44-113.17 | 1.42 (1.3%) | 109.66-115.61 | -0.4% / -0.2% | -0.1% | 6.4M |
| KRE | 68.94 (10:05 iex) | -0.9% | 69.56 | 69.79 / 68.89-70.21 | 1.21 (1.7%) | 67.97-74.30 | -1.7% / -5.1% | -1.2% | 16.0M |
| XHB | 93.96 (10:04 iex) | -0.1% | 94.05 | 94.81 / 93.90-95.30 | 2.08 (2.2%) | 93.63-99.67 | -2.6% / -7.3% | -2.3% | 1.9M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.31 (10:05 iex) | +1.3% | 340.97 | 344.69 / 341.12-348.15 | 6.42 (1.9%) | 325.81-345.34 | +1.5% / +5.6% | +2.4% | 37.3M |
| MSFT | 550.82 (10:05 iex) | +1.8% | 541.15 | 544.64 / 544.28-551.13 | 12.21 (2.3%) | 487.23-542.74 | +5.7% / +7.9% | +3.0% | 22.2M |
| NVDA | 225.81 (10:05 iex) | -0.2% | 226.32 | 224.34 / 223.06-226.17 | 5.26 (2.3%) | 211.16-243.37 | -0.5% / +1.7% | -5.3% | 107.1M |
| AMZN | 262.05 (10:05 iex) | +1.0% | 259.53 | 259.44 / 259.19-262.80 | 5.57 (2.1%) | 244.30-263.70 | +2.9% / +0.3% | +3.2% | 36.7M |
| GOOGL | 356.41 (10:05 iex) | +1.0% | 352.72 | 356.06 / 353.49-358.55 | 8.10 (2.3%) | 335.51-364.17 | +1.9% / +1.9% | +1.8% | 25.6M |
| META | 768.22 (10:05 iex) | +3.4% | 742.96 | 735.99 / 734.84-771.15 | 22.46 (3.0%) | 655.68-779.82 | +2.8% / +15.5% | +0.1% | 22.0M |
| TSLA | 373.75 (10:05 iex) | -1.1% | 378.03 | 372.32 / 371.30-375.40 | 10.86 (2.9%) | 345.88-388.56 | +2.3% / +6.2% | -0.2% | 35.5M |
| AVGO | 355.80 (10:05 iex) | +0.3% | 354.73 | 349.27 / 348.11-356.10 | 10.31 (2.9%) | 335.20-380.84 | -0.3% / -4.3% | -2.1% | 23.3M |
| AMD | 590.10 (10:05 iex) | -0.7% | 594.24 | 577.50 / 570.60-590.76 | 22.42 (3.8%) | 497.51-658.52 | -1.5% / +11.9% | -5.9% | 21.7M |
| ORCL | 139.65 (10:05 iex) | +1.6% | 137.39 | 135.91 / 135.55-140.18 | 6.12 (4.5%) | 131.10-153.03 | -2.7% / -5.5% | -3.2% | 29.9M |
| NFLX | 71.01 (10:04 iex) | +0.6% | 70.61 | 71.16 / 70.84-71.52 | 1.47 (2.1%) | 66.54-79.48 | -0.8% / -6.2% | +4.6% | 37.4M |
| CRM | 244.79 (10:05 iex) | +4.6% | 233.92 | 236.00 / 234.70-244.78 | 7.72 (3.3%) | 220.29-261.87 | -0.2% / +3.6% | +1.8% | 10.4M |
| JPM | 331.57 (10:05 iex) | -0.8% | 334.30 | 339.97 / 331.56-344.36 | 4.91 (1.5%) | 324.25-353.83 | -0.9% / -4.0% | +1.1% | 8.5M |
| GS | 893.87 (10:05 iex) | -0.0% | 893.95 | 923.00 / 894.77-931.00 | 18.47 (2.1%) | 868.52-988.28 | -2.8% / -9.3% | +0.1% | 2.3M |
| BAC | 53.72 (10:05 iex) | -1.6% | 54.58 | 54.44 / 53.73-54.85 | 0.92 (1.7%) | 52.24-59.92 | -1.9% / -8.7% | +1.1% | 38.4M |
| XOM | 173.81 (10:04 iex) | +1.0% | 172.15 | 173.44 / 172.65-174.05 | 3.29 (1.9%) | 155.85-172.55 | +5.1% / +6.5% | +5.0% | 13.0M |
| CVX | 216.83 (10:04 iex) | +0.9% | 215.00 | 217.00 / 215.95-217.41 | 4.13 (1.9%) | 200.78-217.78 | +3.4% / +5.3% | +4.1% | 9.5M |
| LLY | 1,177.35 (10:04 iex) | -0.4% | 1,182.62 | 1,187.04 / 1,173.81-1,193.30 | 34.69 (2.9%) | 1,131.21-1,215.00 | +1.6% / +0.7% | +3.5% | 2.2M |
| UNH | 375.74 (10:05 iex) | -0.7% | 378.52 | 397.62 / 375.45-399.88 | 8.89 (2.3%) | 362.60-387.52 | +1.0% / -2.2% | -0.0% | 5.1M |
| JNJ | 250.24 (10:04 iex) | -5.1% | 263.73 | 254.56 / 250.00-256.18 | 5.10 (1.9%) | 251.17-275.23 | -0.3% / -0.5% | +4.3% | 6.9M |
| WMT | 114.11 (10:04 iex) | +0.9% | 113.08 | 114.22 / 113.87-114.83 | 2.24 (2.0%) | 103.39-113.14 | +4.9% / +4.3% | +7.6% | 21.8M |
| COST | 960.57 (10:04 iex) | +0.1% | 959.44 | 965.73 / 959.83-966.00 | 16.04 (1.7%) | 883.10-960.74 | +4.5% / +3.0% | +3.9% | 2.4M |
| HD | 291.42 (10:05 iex) | +0.3% | 290.62 | 295.00 / 291.18-296.60 | 6.23 (2.1%) | 277.15-311.13 | -0.7% / -7.9% | +3.4% | 5.6M |
| CAT | 777.85 (10:04 iex) | -2.7% | 799.37 | 791.00 / 774.64-792.70 | 25.53 (3.2%) | 774.48-876.95 | -1.8% / -2.7% | -5.8% | 2.4M |
| BA | 186.28 (10:05 iex) | -1.7% | 189.50 | 189.10 / 186.32-189.10 | 5.89 (3.1%) | 184.01-212.40 | -2.4% / -9.4% | -1.7% | 9.2M |
| DAL | 78.87 (10:04 iex) | -1.5% | 80.11 | 80.70 / 78.73-80.70 | 2.47 (3.1%) | 76.89-86.17 | -2.7% / -4.1% | -3.6% | 8.4M |
| UAL | 102.00 (10:05 iex) | -2.3% | 104.44 | 104.35 / 102.02-104.91 | 3.91 (3.7%) | 104.29-118.26 | -5.3% / -8.7% | -5.1% | 4.3M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-13 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| BMBL | 5.96 (10:05 iex) | +56.7% | 3.80 | 5.98 / 5.95-5.98 | 0.20 (5.3%) | 2.44-3.98 | +38.8% / +36.0% | +49.0% | 4.1M |
| NBIZ | 27.41 (09:59 iex) | +11.4% | 24.60 | 26.87 / 26.59-27.41 | 2.64 (10.7%) | 17.01-27.94 | +11.4% / -15.9% | +17.2% | 2.3M |
| IREZ | 14.38 (10:04 iex) | +10.3% | 13.04 | 14.15 / 14.10-14.65 | 1.07 (8.2%) | 6.82-13.16 | +37.0% / +22.8% | +31.3% | 2.5M |
| VEEA | 5.26 (09:54 iex) | +14.1% | 4.61 | 4.65 / 4.65-5.50 | 1.11 (24.0%) | 2.08-8.88 | +12.4% / +49.3% | -19.4% | 24.1M |
| SKDD | 9.71 (10:03 iex) | +9.5% | 8.87 | 9.98 / 9.64-9.98 | 0.56 (6.4%) | 6.22-8.94 | +23.2% / -4.8% | +41.0% | 4.0M |
| CRMG | 8.82 (10:04 iex) | +8.9% | 8.10 | 8.28 / 8.16-8.85 | 0.52 (6.4%) | 7.21-10.37 | -1.8% / +2.6% | +2.9% | 1.2M |
| WFF | 9.01 (10:05 iex) | -47.9% | 17.28 | 14.90 / 8.32-15.55 | 4.54 (26.3%) | 1.75-50.60 | +400.7% / +562.5% | +654.6% | 9.5M |
| ASTX | 5.79 (10:04 iex) | -18.3% | 7.09 | 6.22 / 5.79-6.35 | 1.42 (20.1%) | 5.92-11.90 | -27.2% / -38.2% | -24.7% | 6.3M |
| SNDX | 13.68 (10:05 iex) | -17.3% | 16.55 | 14.61 / 13.49-14.74 | 0.81 (4.9%) | 16.37-18.94 | -6.5% / -12.7% | -7.2% | 2.0M |
| CIFR | 10.88 (10:05 iex) | -16.3% | 13.00 | 11.26 / 10.70-11.32 | 1.03 (7.9%) | 12.88-19.75 | -20.0% / -22.3% | -16.0% | 33.2M |
