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

Research is done: hot CPI and PPI, a global chip sell-off, and money moving into bonds and defensive stocks. Writing the brief now.

# Pre-market brief — Thursday 2026-10-15 (09:05 ET / 15:05 Stockholm)

### 1. Tape
The AI and semiconductor sell-off sped up overnight. The Kospi closed −7.6% after circuit breakers halted trading, SK hynix fell −11% and Advantest −14%. Micron and Western Digital are −4% to −6% pre-market, and TSM is −2% even after a record quarter. NQ futures are −1.1%, ES −0.3% and Dow +0.3% (verified: Benzinga/Bloomberg pre-market pieces). The 08:30 PPI was very hot: +1.3% m/m and 6.3% y/y, against roughly 0.5% and 5.3% expected. Treasuries still rallied. The 10-year is −8 to −11 bp at about 5.08–5.10% and TLT is +1.8%, because flight-to-safety demand outweighed the inflation print. Money is rotating, not leaving: staples (XLP +1.7%, WMT +3%), healthcare (XLV +1.2%, LLY +1.7%), gold and bonds are bid, and energy is holding at its highs. **Regime: risk-off rotation out of AI/semis and long-duration growth into defensives.** The edge is short tech/cyclicals and long defensives, but semis are now 5 days and ~10% into the move, so new shorts there are late. I'd rather harvest the semis short and add the defensive long.

### 2. Calendar
| Time ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| Wed 08:30 | 14:30 | Sep CPI (released yesterday) | 3.7% y/y vs 3.6%; core 0.3% m/m vs 0.2%. Nasdaq −1.88% on the day | All |
| 08:30 | 14:30 | Sep PPI | **+1.3% m/m / 6.3% y/y vs 0.5% / 5.3%.** Hottest since 2022. Bonds rallied anyway | IWM, XOM |
| 08:30 | 14:30 | Sep retail sales | +0.8% m/m vs 0.3% expected. Flat in real terms | WMT |
| 08:30 | 14:30 | Jobless claims | Not verified | — |
| BMO | — | TSM, PNC, USB, SCHW, BNY, MRSH, PLD | TSM record Q3 but −2% pre-market | SMH |
| AMC | 22:00+ | AA, IBKR, JBHT | — | — |
| Fri BMO | — | TRV, TFC | — | — |

### 3. Open positions
- **SMH short (587.00, stop 595, target 556).** Thesis intact and paying: memory repricing, the CXMT headline and fears about AI funding. Pre-market is 548.89, **below the 556 target**, so the buy-to-cover limit should fill at the open (about +4.7R on 8.00/share of risk). I am leaving it alone and taking the target. After −9.6% in 5 days and a Kospi circuit-breaker day, the risk of a capitulation bounce is high, and I'd rather bank the planned exit than trail it into a reversal. No `manage` entry.
- **IWM short (272.99, stop 277.50, target 267).** Thesis **weakening.** It was a rates trade, but yields are falling 8–11 bp this morning and IWM is +0.1% while QQQ is −1.2%. Money leaving mega-cap tech can land in small caps. I'm keeping it because the hot PPI keeps rate-hike risk alive and IWM is still under its 20d/50d averages. **Stop tightened to 275.60** (about 1 ATR above pre-market and above the 20d-low breakdown area), which cuts open risk from 4.51 to 2.61 per share. Target unchanged.
- **XOM long (171.98, stop 170.80, target 179).** Thesis intact: energy leads, and PPI was energy-driven. At 178.10 it is 0.90 from target. **Stop raised to 175.50**, about 2 below the 177.43 breakout level, which locks in about +3R of the roughly 5R open gain. Target stays at 179.

### 4. New plays

**WMT long**

| Field | Value |
|---|---|
| Ticker | WMT |
| Direction | Long |
| Catalyst | Deutsche Bank upgrade to Buy, PT 136 from 113 (2026-10-15), on top of a hot PPI driving rotation into staples |
| Thesis | WMT is the cleanest beneficiary of the inflation-plus-defensive rotation. It closed at a 20d high (116.16 vs high 116.24) and is gapping +3% to 119.68 on a named upgrade. A pullback toward the breakout area should be bought in this tape. |
| Entry | Limit 117.50 (gives back about 2.2 of the gap) |
| Stop | 115.20: under the prior close / 20d-high breakout zone (116.16–116.24). A fill and then a loss of that zone means the breakout failed |
| Target | 122.10 (2.0R) |
| Risk tier | 0.5: chasing a 1.5-ATR gap, and the stop sits at about 1 ATR (2.32) |
| Time horizon | 2–5 days |
| Conviction | 3 |
| P(target before stop) | 42% |
| Invalidation | Staples give back the gap into the close while semis bounce, i.e. the rotation reverses |
| What I'd be wrong about | Gaps on analyst upgrades often fade. WMT is already +7.4% in 5 days and trades at a premium valuation that a quick rates turn could hit. |

The 117.50 limit fills only if the gap fades by about 2/3 of an ATR. If WMT just runs, I miss it, and I accept that rather than paying the open price.

**CAT short**

| Field | Value |
|---|---|
| Ticker | CAT |
| Direction | Short |
| Catalyst | Fourth straight down session. Pre-market 732.38 is below the 20d low of 742.01 after −3.3% yesterday. AI capex worries plus rate-hike fears after CPI/PPI |
| Thesis | CAT is the industrial proxy for AI/data-center power capex, and that is the trade being unwound globally. It is about 30% off its June peak and below its 20d/50d averages. A reflex bounce into the broken 742 level is the place to sell. |
| Entry | Limit 745.00 (retest of the broken 20d low) |
| Stop | 772.00: about 1 ATR above entry, back above yesterday's 748.98 close and the breakdown area |
| Target | 700.00 (1.67R) |
| Risk tier | 0.25 (probe): late in a −8% 5-day move, and falling yields this morning could spark a cyclical bounce |
| Time horizon | 2–5 days |
| Conviction | 2 |
| P(target before stop) | 36% |
| Invalidation | It reclaims 760 on a semis bounce, or the market treats the falling yields as relief for cyclicals |
| What I'd be wrong about | It is oversold, and the bond rally removes one of the main reasons it fell (the 30-year at 5.73% on 10/7). The entry may never fill, or it may fill and squeeze. Q3 earnings are expected in late October; I didn't verify the date. I believe it falls outside a 5-day hold. |

### 5. Both sides
- **Best long:** WMT at a 117.50 limit / 115.20 stop / 122.10 target, P 42%. Taken.
- **Best short:** more semis (AMD at 551, −11.6% in 5 days), but that would be adding at a 5-day extreme on a capitulation-style morning. Passed: short at 565 limit / 595 stop / 520 target, P 33%. CAT at 0.25 is the short I'm actually taking.

### 6. Passing on
- **AMD short:** described above. Too extended, and ATR is 4.3%.
- **XLP long, 86.80 / 85.60 / 89.20:** same staples view as WMT. Doubling it adds nothing, and the gap is 1.4 ATR.
- **TLT long, 79.80 / 78.70 / 82.00:** the bond rally is fighting a 6.3% PPI print. Two-sided, and I have no edge.
- **NVDA short, 222 / 229 / 208:** sits at its 20d low. Same factor as the SMH short I'm banking.
- **QQQ short:** same reason. I'm already exiting the semis exposure at target by choice.

### 7. For the post-open review
- **SMH:** confirm the 556 target filled at the open. If the open somehow comes above 556 (unlikely, pre-market is 549), leave the bracket as is.
- **IWM:** if IWM trades above 274.50 by 10:00 on small-cap rotation (yields falling), close it. The thesis would be invalid at that point.
- **WMT:** if it opens and holds above 119 through 10:00, don't chase. Leave the limit resting. If staples reverse red, cancel it.
- **CAT:** if CAT reclaims 750 by 10:00 with semis bouncing, cancel the 745 limit.

### 8. Book state
After the SMH cover and the new orders: gross is about 60% of equity (XOM ~21k, IWM short ~30k, WMT ~26k, CAT ~3k), net about +20%. Risk at stake is about 1.4% (IWM ~0.29%, XOM 0%, WMT 0.5%, CAT 0.25%) against the 4% cap. 5 slots used of 8.

```json
{
  "date": "2026-10-15",
  "no_trade": false,
  "session_note": "Risk-off rotation: global AI/semis rout plus hot PPI, but bonds, staples and healthcare are bid. Banking the SMH short at target, tightening IWM/XOM, adding a staples long on a pullback and a CAT short probe on a bounce.",
  "plays": [
    {
      "ticker": "WMT",
      "direction": "long",
      "entry_type": "limit",
      "entry": 117.50,
      "stop": 115.20,
      "targets": [122.10],
      "time_horizon": "2-5 days",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.42,
      "catalyst": "Deutsche Bank upgrade to Buy (PT 136) on 2026-10-15 plus hot PPI driving rotation into staples.",
      "thesis": "WMT is the cleanest beneficiary of the inflation/defensive rotation, gapping above its 20d high on an upgrade. Buy a pullback toward the 116.2 breakout zone.",
      "invalidation": "Staples give back the gap while semis bounce, i.e. the rotation reverses.",
      "bear_case": "Upgrade gaps often fade, WMT is already +7.4% in 5 days, and its premium valuation is rate-sensitive."
    },
    {
      "ticker": "CAT",
      "direction": "short",
      "entry_type": "limit",
      "entry": 745.00,
      "stop": 772.00,
      "targets": [700.00],
      "time_horizon": "2-5 days",
      "conviction": 2,
      "risk_pct": 0.25,
      "p_target_first": 0.36,
      "catalyst": "Pre-market break below the 20d low of 742 on 2026-10-15 amid the global AI-capex unwind and rate-hike fears after CPI/PPI.",
      "thesis": "CAT trades as a proxy for AI power capex, which is being unwound globally, and sits below its 20d/50d averages. Sell a bounce into the broken 742 level.",
      "invalidation": "Reclaims 760 on a semis bounce, or falling yields spark a cyclical rally.",
      "bear_case": "Oversold after -8% in 5 days and -30% from peak; the bond rally removes a key reason for the decline."
    }
  ],
  "manage": [
    {
      "ticker": "IWM",
      "action": "update",
      "stop": 275.60,
      "reason": "Rates thesis weakening as yields fall 8-11bp and IWM outperforms QQQ; tighten to ~1 ATR above pre-market."
    },
    {
      "ticker": "XOM",
      "action": "update",
      "stop": 175.50,
      "reason": "0.90 from target; lock in about +3R below the 177.43 breakout level."
    }
  ],
  "passed": [
    {
      "ticker": "AMD",
      "direction": "short",
      "entry_type": "limit",
      "entry": 565.00,
      "stop": 595.00,
      "targets": [520.00],
      "p_target_first": 0.33,
      "reason": "Right direction but -11.6% in 5 days on a capitulation-style morning; same factor as the SMH short being banked."
    },
    {
      "ticker": "XLP",
      "direction": "long",
      "entry_type": "limit",
      "entry": 86.80,
      "stop": 85.60,
      "targets": [89.20],
      "p_target_first": 0.40,
      "reason": "Same staples view as WMT; 1.4-ATR gap; no need to double up."
    },
    {
      "ticker": "TLT",
      "direction": "long",
      "entry_type": "limit",
      "entry": 79.80,
      "stop": 78.70,
      "targets": [82.00],
      "p_target_first": 0.35,
      "reason": "The flight-to-safety rally is fighting a 6.3% PPI print; two-sided, no edge."
    },
    {
      "ticker": "NVDA",
      "direction": "short",
      "entry_type": "limit",
      "entry": 222.00,
      "stop": 229.00,
      "targets": [208.00],
      "p_target_first": 0.34,
      "reason": "At its 20d low after -6.8% in 5 days; duplicates the semis factor I'm exiting at target."
    }
  ]
}
```

Sources: [Benzinga pre-market](https://www.benzinga.com/markets/equities/26/10/62374362/stock-market-today-sp-500-nasdaq-100-futures-fall-as-chip-stock-sell-off-intensifies-skhy-tsm-rklb-in-focus), [Bloomberg futures](https://www.bloomberg.com/news/articles/2026-10-15/us-stock-futures-today-coreweave-dell-fmc-intel-micron-penske), [CNBC Asia tech rout](https://www.cnbc.com/2026/10/15/sk-hynix-samsung-softbank-stocks-asia-tech-rout-ai-funding-worries.html), [CNN PPI/retail sales](https://www.cnn.com/2026/10/15/economy/us-retail-sales-wholesale-inflation-ppi-september), [Bloomberg Treasuries](https://www.bloomberg.com/news/articles/2026-10-15/treasuries-extend-gains-as-equities-selloff-dents-risk-sentiment), [ETFSI note on yields](https://tradelogic1019.substack.com/p/etf-sector-intelligence-etfsi-morning-207), [Benzinga earnings Oct 15](https://www.benzinga.com/news/earnings/26/10/62376670/earnings-scheduled-october-15-2026), [Tradingpedia WMT upgrade](https://www.tradingpedia.com/2026/10/15/walmart-soars-premarket-as-deutsche-bank-upgrades-to-buy/), [GuruFocus CAT](https://www.gurufocus.com/news/9123975/caterpillar-cat-shares-fall-amid-inflation-concerns-and-ai-sector-weakness)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (14:05 UTC), Thursday 2026-10-15. The cash session opened 35 min ago and closes at 16:00 ET.
- Equity: **$102,096.97**
- Cash: $132,608.01
- Session P&L so far: +0.31% (new entries are blocked at -3.0%)
- Gross exposure: $63,301 (62% of equity, cap 150%)
- Net exposure: $-11,131 (-11%, cap +/-100%)
- Risk at stake (entry to stop): $1,046 (1.02% of equity, cap 4.0%) — 2.98% left for new plays
- Slots: 1 open + 2 resting entries of 8 — you may add at most 5 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%, a quarter at 0.25%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Stop | Target | Original thesis |
|---|---|---|---|---|---|---|---|---|
| IWM | short | 112 | 272.99 | 272.42 | +63 (+0.2%) | 275.60 | 267.00 | Small caps are the most rate-sensitive index; IWM opened below its 20d low 274.52 and is pinned at the session low, -4.7 |

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| CAT | short | 9 | 745.00 | limit | 772.00 | 700.00 | 2026-10-15 |
| WMT | long | 222 | 117.50 | limit | 115.20 | 122.10 | 2026-10-15 |

### Record

19 closed trades: 7W / 12L, total -0.46R, net $+2,040 realized. Shorts taken: 17.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| XOM | long | stop | +0.84R | $+425 | 42% |
| SMH | short | target | +2.63R | $+1,306 | 38% |
| UNH | long | stop | -1.04R | $-406 | 42% |
| MSFT | long | target | +1.18R | $+748 | 38% |
| NVDA | long | stop | -0.38R | $-235 | 40% |

### Ideas you passed on, replayed against the tape

37 resolved: 9 reached target first, 22 stop first, 5 never reached the entry, 1 expired, 0 ambiguous. Average -0.30R across the 32 that would have filled.

| Session | Symbol | Direction | Why passed | Outcome | R | You said |
|---|---|---|---|---|---|---|
| 2026-10-02 open | NKE | short | stop entry 34.90 not placed: the market (33.21) had already crossed the trigger | stop | -2.14R | 35% |
| 2026-10-08 open | COST | long | Cancelled resting buy stop after the open faded the whole comp gap from 953.29 t | target | +1.67R | 28% |
| 2026-10-14 pre-market | COST | long | Defensive breakout candidate, but staples with hot CPI and 5% yields are not a c | target | +1.39R | 38% |
| 2026-10-14 open | BAC | short | Morning plan: stand aside below 49.5; -8.6% with no bounce to sell. | stop | -0.96R | 35% |
| 2026-10-12 open | SMH | short | Weakest group today but still uptrend vs 50d; stop ~1 ATR is noise and short rec | target | +1.34R | 35% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| IWM | 272.48 (10:05 iex) | +0.4% | 271.37 | 271.42 / 270.86-272.50 | 3.67 (1.4%) | 270.35-288.94 | -3.3% / -6.3% | -2.3% | 25.5M |
| CAT | 712.35 (10:05 iex) | -4.9% | 748.98 | 725.08 / 704.11-727.24 | 28.30 (3.8%) | 742.01-876.95 | -7.8% / -8.4% | -8.0% | 2.5M |
| WMT | 120.38 (10:05 iex) | +3.6% | 116.16 | 120.00 / 119.64-121.38 | 2.32 (2.0%) | 103.39-116.24 | +7.1% / +7.0% | +7.4% | 22.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 767.02 (10:05 iex) | -0.3% | 769.60 | 766.24 / 764.43-767.44 | 6.36 (0.8%) | 757.97-781.62 | -0.1% / +0.3% | -1.0% | 42.5M |
| QQQ | 719.36 (10:05 iex) | -1.3% | 728.95 | 718.55 / 715.46-721.15 | 8.96 (1.2%) | 712.58-762.86 | -1.8% / +0.4% | -3.8% | 34.6M |
| IWM | 272.48 (10:05 iex) | +0.4% | 271.37 | 271.42 / 270.86-272.50 | 3.67 (1.4%) | 270.35-288.94 | -3.3% / -6.3% | -2.3% | 25.5M |
| DIA | 517.73 (10:05 iex) | +0.4% | 515.63 | 518.00 / 516.17-518.78 | 4.93 (1.0%) | 504.70-522.80 | +0.3% / -1.6% | +0.9% | 3.3M |
| TLT | 80.39 (10:05 iex) | +1.9% | 78.89 | 80.47 / 80.28-80.49 | 0.79 (1.0%) | 76.43-81.61 | +0.2% / -2.0% | +2.3% | 47.9M |
| GLD | 380.49 (10:05 iex) | +1.2% | 375.99 | 380.88 / 380.33-381.49 | 5.84 (1.6%) | 373.36-403.15 | -2.6% / -5.4% | +0.0% | 7.8M |
| USO | 154.49 (10:03 iex) | +0.6% | 153.56 | 154.78 / 153.90-154.91 | 4.89 (3.2%) | 141.76-157.55 | +3.3% / +8.9% | +6.7% | 5.4M |
| SMH | 545.30 (10:05 iex) | -3.4% | 564.74 | 545.84 / 540.64-551.20 | 14.30 (2.5%) | 557.56-639.47 | -6.3% / -2.6% | -9.6% | 6.6M |
| XLK | 186.23 (10:05 iex) | -2.2% | 190.43 | 186.44 / 184.85-187.49 | 3.02 (1.6%) | 186.51-203.25 | -2.9% / +0.4% | -5.4% | 7.5M |
| XLF | 54.72 (10:05 iex) | +0.4% | 54.52 | 54.88 / 54.59-54.97 | 0.67 (1.2%) | 52.81-56.20 | +0.1% / -3.1% | +1.4% | 38.3M |
| XLE | 66.59 (10:05 iex) | -1.5% | 67.63 | 67.78 / 66.46-67.90 | 1.22 (1.8%) | 60.95-67.72 | +6.4% / +7.5% | +6.7% | 32.5M |
| XLV | 178.42 (10:05 iex) | +2.6% | 173.96 | 176.63 / 176.22-178.54 | 2.77 (1.6%) | 165.19-173.99 | +2.8% / +2.9% | +3.1% | 8.3M |
| XLI | 165.31 (10:04 iex) | -1.0% | 167.04 | 166.60 / 164.66-166.94 | 2.48 (1.5%) | 165.69-172.34 | -1.2% / -4.3% | -0.5% | 7.3M |
| XLY | 112.37 (10:05 iex) | +0.8% | 111.50 | 111.94 / 111.70-112.38 | 1.25 (1.1%) | 107.99-113.29 | +0.5% / -2.1% | +0.1% | 6.3M |
| XLP | 88.03 (10:05 iex) | +2.3% | 86.06 | 87.57 / 87.47-88.45 | 1.04 (1.2%) | 80.10-86.06 | +4.5% / +2.9% | +5.3% | 10.7M |
| XLU | 41.59 (10:05 iex) | -0.3% | 41.72 | 42.19 / 41.59-42.20 | 0.64 (1.5%) | 39.03-41.95 | +3.0% / -0.4% | +1.4% | 34.5M |
| XLB | 50.16 (10:05 iex) | +1.0% | 49.67 | 50.17 / 49.90-50.43 | 0.70 (1.4%) | 47.81-50.78 | +0.3% / -2.8% | +1.4% | 11.4M |
| XLRE | 41.92 (10:05 iex) | +1.0% | 41.49 | 41.97 / 41.90-42.17 | 0.58 (1.4%) | 40.28-42.81 | -0.0% / -3.5% | +2.3% | 7.0M |
| XLC | 112.26 (10:05 iex) | +1.3% | 110.82 | 110.65 / 110.28-112.31 | 1.49 (1.3%) | 109.66-115.61 | -0.9% / -0.7% | -0.4% | 6.6M |
| KRE | 69.24 (10:04 iex) | +1.0% | 68.54 | 69.00 / 68.72-69.36 | 1.26 (1.8%) | 67.79-73.37 | -2.5% / -6.0% | -0.5% | 15.5M |
| XHB | 95.20 (10:04 iex) | +2.5% | 92.84 | 94.41 / 94.13-95.47 | 2.12 (2.3%) | 91.87-99.67 | -3.6% / -8.0% | -2.2% | 1.8M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 345.76 (10:05 iex) | +0.8% | 342.96 | 346.95 / 344.82-347.85 | 6.58 (1.9%) | 325.81-348.15 | +1.8% / +5.7% | +1.9% | 38.3M |
| MSFT | 534.06 (10:05 iex) | +0.1% | 533.69 | 533.99 / 531.22-539.32 | 12.23 (2.3%) | 491.10-551.15 | +3.4% / +6.0% | +0.7% | 22.8M |
| NVDA | 215.43 (10:05 iex) | -2.7% | 221.30 | 215.30 / 212.87-215.97 | 5.63 (2.5%) | 217.15-243.37 | -3.2% / -0.8% | -6.8% | 108.0M |
| AMZN | 251.66 (10:05 iex) | -1.0% | 254.08 | 250.89 / 248.65-251.78 | 5.53 (2.2%) | 244.72-263.70 | +0.3% / -1.5% | -2.2% | 36.2M |
| GOOGL | 350.42 (10:05 iex) | +0.8% | 347.64 | 344.69 / 340.61-350.60 | 8.04 (2.3%) | 335.51-364.17 | +0.3% / +0.7% | -0.8% | 26.1M |
| META | 733.66 (10:05 iex) | -0.5% | 737.54 | 725.86 / 715.58-735.45 | 22.50 (3.1%) | 660.28-779.82 | +0.9% / +13.5% | +2.3% | 22.1M |
| TSLA | 356.86 (10:05 iex) | -2.8% | 367.16 | 360.57 / 355.27-360.60 | 10.95 (3.0%) | 345.88-388.56 | -1.0% / +2.6% | -2.8% | 34.8M |
| AVGO | 337.29 (10:05 iex) | -2.6% | 346.25 | 338.01 / 334.63-340.26 | 10.81 (3.1%) | 342.82-380.84 | -3.0% / -6.1% | -8.0% | 22.9M |
| AMD | 538.59 (10:05 iex) | -5.6% | 570.82 | 540.00 / 530.29-550.81 | 24.27 (4.3%) | 527.60-658.52 | -6.6% / +6.7% | -11.6% | 21.7M |
| ORCL | 131.09 (10:05 iex) | +0.4% | 130.55 | 128.07 / 128.00-131.13 | 6.60 (5.1%) | 129.23-153.03 | -7.3% / -10.0% | -8.7% | 30.6M |
| NFLX | 72.31 (10:05 iex) | +2.5% | 70.57 | 71.55 / 71.33-72.64 | 1.53 (2.2%) | 66.54-76.96 | +0.1% / -6.1% | +1.2% | 38.1M |
| CRM | 243.00 (10:05 iex) | +3.0% | 235.95 | 238.50 / 238.02-243.72 | 8.06 (3.4%) | 220.29-247.00 | +1.3% / +3.6% | +5.1% | 10.1M |
| JPM | 333.15 (10:05 iex) | -0.6% | 335.28 | 337.25 / 332.69-337.25 | 5.94 (1.8%) | 324.25-352.74 | -0.1% / -3.5% | +1.7% | 8.6M |
| GS | 862.40 (10:05 iex) | -1.9% | 878.72 | 879.00 / 859.56-882.55 | 20.57 (2.3%) | 866.00-967.76 | -3.7% / -10.3% | -1.0% | 2.4M |
| BAC | 51.38 (10:05 iex) | -0.0% | 51.39 | 51.46 / 51.09-51.87 | 1.24 (2.4%) | 49.26-58.49 | -6.6% / -13.5% | -4.0% | 41.5M |
| XOM | 175.56 (10:04 iex) | -0.8% | 177.01 | 178.63 / 175.45-178.69 | 3.21 (1.8%) | 155.85-177.43 | +7.4% / +8.9% | +7.9% | 13.0M |
| CVX | 220.72 (10:04 iex) | -0.6% | 222.04 | 222.82 / 220.57-223.46 | 4.18 (1.9%) | 200.78-222.55 | +6.5% / +8.1% | +8.2% | 9.4M |
| LLY | 1,260.63 (10:05 iex) | +4.3% | 1,208.74 | 1,235.04 / 1,230.66-1,261.13 | 34.37 (2.8%) | 1,131.21-1,216.71 | +3.4% / +2.7% | +1.7% | 2.3M |
| UNH | 405.85 (10:05 iex) | +2.6% | 395.62 | 401.45 / 400.00-409.37 | 11.18 (2.8%) | 362.60-399.88 | +5.3% / +2.5% | +5.2% | 5.7M |
| JNJ | 259.96 (10:03 iex) | +2.4% | 253.91 | 257.36 / 257.00-262.44 | 5.97 (2.4%) | 245.17-275.23 | -3.4% / -4.2% | -1.8% | 7.7M |
| WMT | 120.38 (10:05 iex) | +3.6% | 116.16 | 120.00 / 119.64-121.38 | 2.32 (2.0%) | 103.39-116.24 | +7.1% / +7.0% | +7.4% | 22.3M |
| COST | 1,002.99 (10:04 iex) | +2.1% | 982.00 | 997.78 / 997.00-1,008.37 | 17.02 (1.7%) | 883.10-982.64 | +6.2% / +5.3% | +4.2% | 2.4M |
| HD | 307.25 (10:05 iex) | +4.0% | 295.51 | 305.51 / 301.42-307.83 | 5.89 (2.0%) | 277.15-310.40 | +1.3% / -5.8% | +3.4% | 5.7M |
| CAT | 712.35 (10:05 iex) | -4.9% | 748.98 | 725.08 / 704.11-727.24 | 28.30 (3.8%) | 742.01-876.95 | -7.8% / -8.4% | -8.0% | 2.5M |
| BA | 185.57 (10:04 iex) | +0.5% | 184.66 | 185.65 / 184.38-186.72 | 5.56 (3.0%) | 183.38-204.06 | -3.9% / -10.9% | -1.9% | 8.9M |
| DAL | 76.10 (10:05 iex) | -0.4% | 76.44 | 76.66 / 75.56-76.72 | 2.49 (3.3%) | 75.91-85.93 | -6.9% / -7.6% | -7.6% | 8.4M |
| UAL | 99.14 (10:05 iex) | +0.2% | 98.96 | 98.96 / 98.13-99.35 | 3.83 (3.9%) | 97.70-118.26 | -9.8% / -12.6% | -10.2% | 4.4M |

#### Movers (at least $5 and 1M average volume, screener as of 2026-10-15 10:05 ET)

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| IREZ | 19.94 (10:05 iex) | +22.6% | 16.26 | 18.08 / 17.67-20.29 | 1.33 (8.2%) | 6.82-16.37 | +62.1% / +52.3% | +51.3% | 2.6M |
| NBIZ | 37.01 (10:03 iex) | +21.4% | 30.48 | 34.12 / 33.65-37.57 | 2.82 (9.2%) | 17.01-31.24 | +37.8% / +8.1% | +54.4% | 2.2M |
| LITZ | 30.46 (10:04 iex) | +19.1% | 25.58 | 28.50 / 28.40-31.12 | 3.08 (12.0%) | 16.35-29.28 | +11.5% / -15.0% | +43.4% | 2.1M |
| AAOZ | 18.51 (10:04 iex) | +18.7% | 15.59 | 17.47 / 17.30-18.94 | 2.05 (13.1%) | 7.63-15.84 | +26.9% / +25.8% | +80.6% | 1.7M |
| CORD | 5.37 (10:05 iex) | +16.2% | 4.62 | 5.22 / 5.13-5.49 | 0.36 (7.9%) | 2.52-4.75 | +48.1% / +45.3% | +65.6% | 14.2M |
| BEZ | 7.33 (10:03 iex) | +16.2% | 6.31 | 7.14 / 6.93-7.56 | 0.76 (12.1%) | 4.08-6.50 | +21.4% / -17.8% | +41.0% | 5.5M |
| SMCZ | 6.56 (10:04 iex) | +15.3% | 5.69 | 6.18 / 6.10-6.78 | 0.48 (8.5%) | 3.66-5.75 | +25.7% / -6.8% | +49.3% | 3.0M |
| SNDQ | 18.16 (10:05 iex) | +14.5% | 15.86 | 17.91 / 17.64-18.74 | 1.15 (7.3%) | 8.90-15.88 | +37.4% / +6.0% | +41.4% | 26.0M |
| FMC | 5.14 (10:05 iex) | -36.4% | 8.09 | 5.12 / 4.84-5.46 | 0.43 (5.3%) | 8.04-10.78 | -11.5% / -21.6% | -11.0% | 4.8M |
| RKLX | 8.85 (10:04 iex) | -26.3% | 12.00 | 9.94 / 8.26-10.39 | 1.87 (15.6%) | 11.85-21.34 | -29.9% / -33.5% | -33.4% | 3.3M |
| IREX | 5.52 (10:03 iex) | -22.9% | 7.16 | 6.36 / 5.36-6.51 | 1.55 (21.6%) | 7.05-19.64 | -47.5% / -50.1% | -39.5% | 2.0M |
| AXTX | 16.07 (10:03 iex) | -23.2% | 20.93 | 18.00 / 15.58-18.25 | 5.54 (26.5%) | 19.97-44.60 | -35.9% / -36.7% | -42.6% | 2.8M |
| NEBX | 12.70 (10:04 iex) | -21.4% | 16.15 | 14.23 / 12.21-14.35 | 3.36 (20.8%) | 15.56-31.11 | -36.2% / -36.8% | -40.0% | 2.3M |
| NBIG | 8.53 (10:05 iex) | -21.5% | 10.87 | 9.59 / 8.26-9.72 | 2.28 (21.0%) | 10.48-20.96 | -36.1% / -36.7% | -40.0% | 2.8M |
| NBIL | 12.46 (10:04 iex) | -21.2% | 15.81 | 14.01 / 11.97-14.18 | 3.30 (20.9%) | 15.23-30.43 | -36.0% / -36.6% | -39.9% | 4.4M |
| AAOX | 5.12 (10:04 iex) | -19.6% | 6.37 | 5.61 / 4.91-5.66 | 1.94 (30.4%) | 6.29-15.65 | -38.6% / -50.4% | -53.5% | 13.1M |
