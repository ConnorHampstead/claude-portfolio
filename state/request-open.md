Produce the post-open review.

The cash session has been open for about 35 minutes. This morning's pre-market
brief is below, followed by the live book and market data, which now include
today's opening prices. This is the second and last decision point of the day:
after this review, nothing looks at the book until tomorrow's pre-market brief.

What this session is for:

- **Fills at the open.** Check every entry that filled since the morning. An
  entry that filled on a gap through its limit sits closer to its stop than
  planned: it risks less than it was sized for, which is not a reason to close
  it. Close it through `manage` only if what caused the gap is the invalidation
  you wrote this morning. Otherwise its bracket stands.
- **Open positions.** The same test as the morning: closed only on the recorded
  invalidation, its own binary event before tomorrow's brief, or its tenth
  session. No stop is tightened.
- **The morning's plans for this review.** The 08:30 and 10:00 ET data have
  printed and the opening range is set. For each thing the morning brief said it
  would decide after the open or after the data, decide now: act, or say why not.
- **Resting entries** the open has made stale: amend or cancel them.
- **New plays**, under the same rules as the morning, pass-2 research
  included. Orders now go into a trading market: a limit at or through the last
  price fills immediately, and a `market` entry is sized from the last price.

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
Each position: keep, or close and which of the three conditions applies. Each
resting entry: keep, amend or cancel, and why.

### 3. The morning's plans
Each plan the morning left for this review: acted on, not triggered, or dropped.
One line each.

### 4. New plays
The same table as the pre-market brief.

### 5. Passing on
One line each. Ideas with real levels also go in the `passed` array, where they
are scored.

### 6. For tomorrow
Any level or condition you would act on tomorrow. Tomorrow's pre-market brief is
shown this review. "None" is fine.

Then the JSON block, in the same schema as the morning.

Your probability estimates are scored against outcomes, on the bracket as you
submit it. Start from the base rate in "Your record" and move off it only for
reasons you name.

## What the record has shown so far

*As of 2026-11-09, 45 closed trades. Merged by the operator from the reviews. The
samples are small: each line is the working assumption, not a settled finding,
and "Your record" in the book state has the current figures.*

- **Managing positions has cost money.** Left alone, the 45 brackets would have
  made about 5R. As managed they made under 2R: moved stops gave up about 2.4R
  over 11 trades and closes by hand about 1.7R over 9. Hence the default of
  leaving the bracket as submitted.
- **Your probabilities have not told good ideas from bad.** Almost all sat
  between 0.30 and 0.47, on average exactly at breakeven for the reward:risk
  stated, and scored no better than saying the base rate every time (about 42%
  of 116 brackets reached target first). Start from the base rate.
- **Small probes did not pay.** Conviction-2 plays averaged -0.15R over 18
  trades and took slots, while the ideas you passed on averaged +0.10R over 80.
  Low-conviction ideas are now scored in the shadow book instead of traded.

## This morning's pre-market brief

# Pre-market brief: Monday 2026-11-16, 09:05 ET / 15:05 Stockholm

## 1. Tape

Futures are lower, and the selling is concentrated in tech:
- **US futures:** Nasdaq-100 −1.4%, S&P 500 −0.6%, Dow about −0.2% (CNBC, 09:04 ET). QQQ trades 670.81 pre-market (−1.3%). SMH is −3.9% and NVDA −3.6%.
- **Asia led the chip selling:** Taiwan's Taiex fell 6.0% and the Kospi 3.6–4.0%. SK Hynix fell 6% (ZeroHedge, TradingKey). The Nikkei fell 2.4% after Japan's Q3 GDP shrank.
- **The AI complex:** NVDA reports Tuesday after the close with an implied move of about ±7.8%. It is the company's first report since Huang left. Anthropic's IPO prices Wednesday and starts trading Thursday: about 825M shares at $70–78, roughly $60B of new supply for AI-tech holders.
- **Crypto:** bitcoin fell to about $62K on Sunday on ETF outflows and about $2B of liquidations. COIN, MSTR and HOOD are down 5.7–8.5% pre-market.
- **Macro (ZeroHedge, FinanceFeeds):** the 10-year is about 5.13% and the 2-year about 4.85%. DXY is about 103.5, its highest since April 2025. A December hike is priced at 91–94%. Spot gold fell to $3,832 overnight, its lowest since October 2025, and trades about $3,870.
- **Regime:** risk-off rotation. Money is leaving AI, semis and crypto for healthcare and staples (XLV +0.9%, XLP +0.8%, JNJ, LLY and WMT higher) on rising real rates and a strong dollar.
- **Which side has the edge:** the short side. But the cleanest short (semis) runs straight into NVDA's print, so the short I take is in gold, where the driver is the dollar and rates.

## 2. Calendar

Stockholm is ET+6 today (from the book-state clock).

| ET | Stockholm | Event | Actual / consensus | Touches |
|---|---|---|---|---|
| 05:00 | 11:00 | Fed's Barr (AI and financial stability) | Remarks not found | — |
| 08:30 | 14:30 | Empire State manufacturing, Nov | **7.8** vs about 16.7–18 consensus, prior 25.5. New orders 3.0; employment 18.1, its highest since June 2022 (CNBC, Finviz). Futures were already lower before it; I can't separate its effect from the chip selling. | IWM, GLD |
| 09:05 | 15:05 | Fed's Williams | Remarks not yet reported | IWM, GLD |
| 11:30 | 17:30 | 13- and 26-week bill auctions | — | — |
| 12:00 | 18:00 | **Fed Chair Warsh** opens the Fed's productivity and jobs conference | Ahead. He usually avoids forward guidance. | GLD (the order triggers only on a hawkish break), IWM |
| 14:15 | 20:15 | Fed's Hammack | Ahead | — |
| Today, pre-market | — | Tyson, Aramark (ARMK about −5% on a Q4 miss) | — | — |
| Tue 08:30 / 09:15 | 14:30 / 15:15 | October retail sales (+0.2% m/m, control +0.4%), import prices, industrial production | Consensus (Finviz) | GLD, IWM |
| Tue after the close | about 22:05+ | **NVDA fiscal Q3**, implied about ±7.8% | Ahead | AMZN, QQQ, SMH |
| Wed 14:00 | 20:00 | FOMC minutes (October meeting) | Ahead | GLD, IWM |
| Wed / Thu | — | Anthropic prices Wednesday and trades Thursday as ANT. GTA VI launches Thursday. HD, TJX, LOW, TGT and WMT report this week; I didn't verify the exact days. | — | TTWO (passed) |
| Thu 08:30 | 14:30 | Jobless claims (196K expected), Philly Fed (19.2) | Consensus | — |

## 3. Open positions and resting entries

| Position | Invalidation happened? | Session | Decision |
|---|---|---|---|
| **AMZN long**, 274.10 (stop 263.50 / target 293.00) | **No.** The test is QQQ breaking its 20-day low of 647.05 while AMZN falls back inside its range. QQQ is 670.81 pre-market. | 6 of 10 | **Hold, bracket unchanged.** Pre-market 263.60 is 0.10 above the stop, so it will probably stop out at the open. That is what the stop is for. |
| **DAL long**, 89.50 (85.80 / 96.50) | **No.** The test is Brent above $100. Brent is $93.3–96.1 (CNBC $96.13, ZeroHedge about $95.15, TradingKey $93.28). Airlines are down more than 1% after Friday's nationwide FAA ground stop, which followed an air-traffic-control communications failure (CoinCentral, CNBC). That is not the recorded invalidation. | 3 of 10 | **Hold, bracket unchanged.** Pre-market 85.80 is exactly at the stop. |
| **IWM short**, 281.03 (287.00 / 271.00) | **No.** The test is the 2-year fully reversing the CPI move, or a close above 284. The 2-year is about 4.85% (ZeroHedge), not 4.55%. IWM closed Friday at 277.54 and trades 276.17. | 5 of 10 | **Hold, bracket unchanged.** |

There are no resting entries. Friday's GLD and QQQ sell stops were cleared over the weekend. On Friday's re-arm conditions:
- **QQQ:** re-arm only on a Friday close below about 670. It closed at 679.89, so the condition isn't met. I'm not re-arming it, because NVDA reports tomorrow (see section 6).
- **GLD:** the first condition, a close below 354.67, isn't met: it closed at 355.45. The second, a new-low sell stop under the 20-day low, is what I'm doing in section 4, with the trigger moved below the overnight spot low.

## 4. New plays

### GLD short (breakdown sell stop)

| Field | Value |
|---|---|
| Ticker | GLD |
| Direction | Short |
| Catalyst | Spot gold broke its 2026 low overnight, touching **$3,832 on Mon Nov 16** (lowest since Oct 2025), as the dollar index hit about 103.5 (highest since Apr 2025) and December-hike odds reached 91–94%. Read at FinanceFeeds and FXEmpire (Nov 16), with Reuters spot $3,840.52 at 06:41 GMT cited via FinanceFeeds, and ZeroHedge for DXY and yields. The hawkish run of Fed speakers (Waller open to 50bp; Jefferson, Collins and Schmid on inflation) comes from a summary (ZeroHedge), not the speeches themselves. |
| Thesis | Gold is falling on rising real rates and the strongest dollar in 18 months: −4.6% in 5 days, 3.6% below its 20-day average and 6.7% below its 50-day. If the US session confirms the overnight break by taking GLD below about the $3,830 spot equivalent, the next supports analysts cite are $3,823 and then $3,800, and the trend has room toward about $3,650 over two weeks. The stop entry means the order only fills if the break is confirmed. A dovish Warsh at noon leaves it unfilled. |
| Entry | **Sell stop 350.50.** That is below the 352.91 20-day low and below the overnight $3,832 spot low (GLD/spot ratio about 0.0915 from 354.40 against about $3,872). Pre-market is 354.40, so the trigger is beyond the market. |
| Stop | **359.00** (8.50 = 1.12 ATR). Above Friday's 355–357 range and the 357.32 intraday high I saw on Friday, and about $3,920 spot, above the $3,903 pivot. Reclaiming it means the breakdown failed. |
| Target | **333.00** (spot about $3,640). 17.50 = 2.06R. |
| Risk tier | **0.5%.** Conviction 3. It is also the same hawkish-Fed bet as the open IWM short, and gold's RSI is about 33, close to oversold. |
| Time horizon | 3–7 sessions |
| Next earnings | None (ETF). Not an event trade. |
| Conviction | 3 |
| P(target before stop) | **0.36.** I started from the 40% base rate over 129 brackets and took it down to about 0.35 because a 2R target is farther than the average bracket. The trend and the macro driver point the same way, which adds about +0.01. A fill only comes with a confirmed new low, but that is offset by the oversold reading and by Hormuz headlines that could bring back a safe-haven bid. EV = 0.36 × 2.06 − 0.64 = **+0.10R**. |
| Invalidation | DXY back below 102.50 while the market-implied odds of a December hike fall under 70%. That would mean the rates-and-dollar driver has reversed. |
| What I'd be wrong about | December is fully priced. A Fed chair who avoids guidance, or minutes that show a split committee, can set off a short-covering rally in a market already near oversold. A Strait of Hormuz escalation (tankers hitting mines were reported this morning) is a safe-haven tail that a rates trade doesn't hedge. |

The trigger sits just under the overnight spot low, so it fills only if the US session makes a new low. That would most likely come at Warsh's noon remarks, Tuesday's retail sales or Wednesday's minutes. The order is good-till-cancelled and is cleared before the weekend. This adds about 21% short notional to a book whose only other macro short (IWM) has the same driver. The stop entry is what keeps the correlation acceptable: a dovish surprise prevents the fill rather than hitting a stop.

## 5. Both sides

- **Best short: GLD**, sell stop 350.50 / stop 359.00 / target 333.00, P 0.36. Taken (section 4).
  - The most obvious short is semis: **SMH** at about 467.85 / stop 500.00 / target 420.00, P 0.33, 1.49R, EV −0.18R. It is passed and logged. The global chip rout is real and dated (Taiex −6% today). But NVDA's Tuesday print is about 20% of SMH with a ±7.8% implied move, and sentiment on NVDA is washed out: −32% from its October high. A single-sourced FT report (via TradingKey; I couldn't find the FT piece) has Huang's backers pushing for his return. Shorting into that is a coin flip with squeeze risk.
- **Best long: CNC**, limit 72.40 / stop 68.40 / target 79.40, P 0.37, 1.75R, EV +0.02R. Passed at conviction 2.
  - The catalyst is verified and dated: on Fri Nov 13, CMS let states delay enforcement of the Medicaid work requirement to June 30, 2027 (Washington Post and The Hill headlines; Townhall; rallies.ai).
  - About 2.5% was priced in Friday after hours and +2.6% pre-market (73.13, about 0.5 ATR). The delay is optional for states and enforcement still formally starts Jan 1, 2027.
  - What's left doesn't clear zero EV by enough to trade. Next earnings is estimated at late January to about Feb 8, 2027; I couldn't confirm the date.

## 6. Passing on

- **SMH short** (467.85 / 500.00 / 420.00, P 0.33): NVDA reports Tuesday after the close and it is about 20% of the fund. There is Huang-return squeeze risk, and EV is negative. Logged.
- **QQQ sell stop** (646.00 / 666.00 / 610.00, P 0.35, 1.8R, EV −0.02): Friday's re-arm condition (a close below 670) wasn't met, and NVDA is about 8–9% of QQQ. I'll revisit after the print. Logged.
- **COIN short on a retest of the broken 20-day low** (sell limit 124.50 / 134.50 / 104.50, P 0.32): the catalyst is dated (bitcoin to about $62K on Nov 15, roughly $2B of liquidations and ETF outflows from Nov 5 to 13). But the stock has already gapped about 1 ATR to 117.95, and bitcoin bounced above $65K on Sunday. Conviction 2. Next earnings is about Feb 11, 2027 (Wall Street Horizon estimate, not confirmed). Logged.
- **CNC long**: see section 5. Conviction 2. Logged.
- **XLV breakout** (buy stop 192.60 / 188.60 / 199.60, P 0.37): the rotation is clear, but there is no dated catalyst for the fund, it is 8% above its 50-day average, and my last XLV long stopped out. Logged.
- **TTWO** (+2.9% into the Thursday GTA VI launch): a launch is not a rule-8 binary, but it is a sell-the-news setup with no edge I can name. Shadow short at sell limit 241.00 / 251.00 / 221.00, P 0.30, conviction 1. Logged.
- **HUM** (+2.2%, above its 451.04 20-day high on an RBC upgrade to Outperform, per Investing.com and MarketBeat): an analyst upgrade alone is a thin catalyst. No levels.
- **HSY +3.0% and HUBS +3.3%**: I couldn't find a dated reason for either. Unexplained movers aren't trades.
- **MU −5.4%**: ZeroHedge cites a fatal accident at its Taichung fab. My own search found no confirmation, and a supply disruption can cut either way for memory pricing. No levels.
- **INTC about −5%**: a shareholder class action is a weak catalyst. No levels.

## 7. For the post-open review

1. **AMZN and DAL** are both at or within 0.10 of their stops pre-market. If either stops at the open, there is no re-entry and no action. If either holds, its bracket stays untouched.
2. **GLD sell stop 350.50:**
   - If GLD opens below 350.50, the stop fills at the open. Accept it; the bracket stands.
   - If GLD trades above **362.00** before triggering (spot above about $3,955, through the $3,934 resistance, for example on Williams' 09:05 remarks), **cancel the entry**. The breakdown setup it describes would be gone.
   - Otherwise keep it resting through Warsh at noon.
3. **Semis:** open no semis or QQQ short in the review, even if SMH breaks its 445.59 20-day low by 10:00. NVDA's print comes first. Wednesday's brief re-evaluates SMH and QQQ: QQQ sell stop about 646 if QQQ closes Tuesday below 660 after the print.
4. **CNC** stays in the shadow book. The review can't promote a conviction-2 idea without new information. A gap fill back toward 71.27 by 10:00 would be new information to note, not a trade.

## 8. Book state

- **Exposure:** if GLD fills, gross is about 56% of the 150% cap and net about −32% of ±100%. The largest sector is the IWM short at −23% of the 40% sector cap; GLD alone is about −21%.
- **Risk and slots:** risk at stake is about 1.50% of the 4% cap (1.00% open plus 0.50% GLD), with 4 of 8 slots. It falls to about 1.0% and 2 open positions plus GLD if AMZN and DAL stop out at the open.

```json
{
  "date": "2026-11-16",
  "no_trade": false,
  "session_note": "Risk-off rotation: global chip rout (Taiex -6%) and crypto liquidation into NVDA's Tue print and Anthropic's $60B IPO, with DXY at an 18-month high and a Dec hike 91-94% priced. The only trade is a confirmation sell stop in GLD below the overnight $3,832 spot low at half risk; semis and QQQ shorts wait for NVDA, and AMZN/DAL/IWM keep their brackets (no invalidation met).",
  "plays": [
    {
      "ticker": "GLD",
      "direction": "short",
      "entry_type": "stop",
      "entry": 350.50,
      "stop": 359.00,
      "targets": [333.00],
      "time_horizon": "3-7 sessions",
      "conviction": 3,
      "risk_pct": 0.5,
      "p_target_first": 0.36,
      "earnings_date": null,
      "event_trade": false,
      "catalyst": "Mon 2026-11-16: spot gold broke its 2026 low to $3,832 overnight (lowest since Oct 2025; FinanceFeeds/FXEmpire, Reuters spot cited) as DXY hit ~103.5 (highest since Apr 2025) and December-hike odds reached 91-94% after hawkish Fed speakers.",
      "thesis": "Gold is trending down on rising real rates and the strongest dollar in 18 months (-4.6% in 5 days, below its 20d and 50d averages). A US-session break below the overnight low (GLD 350.50, under its 352.91 20-day low) confirms the move toward the $3,800 and then ~$3,650 area. The stop entry stays unfilled if Warsh or the minutes turn dovish.",
      "invalidation": "DXY back below 102.50 with market-implied December-hike odds below 70%.",
      "bear_case": "December is fully priced and gold's RSI is ~33, close to oversold; a guidance-free Warsh or split minutes can spark short covering, and a Strait of Hormuz escalation is a safe-haven tail."
    }
  ],
  "manage": [],
  "passed": [
    {
      "ticker": "SMH",
      "direction": "short",
      "entry_type": "market",
      "entry": 467.85,
      "stop": 500.00,
      "targets": [420.00],
      "p_target_first": 0.33,
      "reason": "Global chip rout is real and dated (Taiex -6% Nov 16), but NVDA (~20% of SMH) reports Tue after the close with a ~7.8% implied move, sentiment is washed out, and there is single-sourced Huang-return squeeze risk; EV about -0.18R."
    },
    {
      "ticker": "QQQ",
      "direction": "short",
      "entry_type": "stop",
      "entry": 646.00,
      "stop": 666.00,
      "targets": [610.00],
      "p_target_first": 0.35,
      "reason": "Friday's re-arm condition (close under 670) not met (closed 679.89); NVDA print Tuesday. Revisit Wednesday."
    },
    {
      "ticker": "COIN",
      "direction": "short",
      "entry_type": "limit",
      "entry": 124.50,
      "stop": 134.50,
      "targets": [104.50],
      "p_target_first": 0.32,
      "reason": "Dated catalyst (bitcoin to ~$62K on Nov 15 on ETF outflows and ~$2B of liquidations), but already gapped ~1 ATR below its 20d low and bitcoin bounced above $65K; short only on a retest, conviction 2."
    },
    {
      "ticker": "CNC",
      "direction": "long",
      "entry_type": "limit",
      "entry": 72.40,
      "stop": 68.40,
      "targets": [79.40],
      "p_target_first": 0.37,
      "reason": "Verified catalyst (CMS Nov 13 lets states delay Medicaid work-rule enforcement to Jun 30 2027), but ~5% already priced across Friday after hours and pre-market, and the delay is optional for states; EV ~+0.02R, conviction 2."
    },
    {
      "ticker": "XLV",
      "direction": "long",
      "entry_type": "stop",
      "entry": 192.60,
      "stop": 188.60,
      "targets": [199.60],
      "p_target_first": 0.37,
      "reason": "Defensive rotation is clear but there is no dated catalyst for the fund, it is +8% over its 50d average, and the recent XLV long stopped out; conviction 2."
    },
    {
      "ticker": "TTWO",
      "direction": "short",
      "entry_type": "limit",
      "entry": 241.00,
      "stop": 251.00,
      "targets": [221.00],
      "p_target_first": 0.30,
      "reason": "Sell-the-news idea into the Thursday GTA VI launch after +6% in 5 days, but no edge I can name; conviction 1, shadow only."
    }
  ]
}
```

Sources:
- [CNBC live updates, Nov 16](https://cnbc.com/2026/11/15/stock-market-today-live-updates.html)
- [ZeroHedge: futures slide as Asian chip carnage greets NVDA earnings week](https://www.zerohedge.com/markets/futures-slide-asian-chip-carnage-greets-nvidias-first-post-huang-earnings-week)
- [TradingKey: US pre-market, Nasdaq futures fall over 1%](https://www.tradingkey.com/analysis/stocks/us-stocks/262307008-us-nvda-nasdaq-futures-nvidia-jensen-huang-anthropic-ipo-tradingkey)
- [CoinCentral: today's market movers](https://coincentral.com/todays-market-movers-nvidia-falls-before-earnings-as-spacex-catches-starship-stage)
- [MarketScreener/Reuters: futures fall ahead of Nvidia earnings, Anthropic IPO](https://www.marketscreener.com/news/s-p-500-nasdaq-futures-slide-as-nvidia-earnings-anthropic-debut-loom-ce785eded080f124)
- [Finviz economic calendar, week of Nov 16](https://finviz.com/calendar/economic?dateFrom=2026-11-16)
- [FinanceFeeds: gold $3,872, lowest since Oct 2025, before the Warsh speech](https://financefeeds.com/gold-price-today-3872-monday-lowest-since-october-2025-warsh-speech-bull-4010-bear-3800/)
- [FXEmpire: gold near a one-year low, can it hold $3,852](https://www.fxempire.com/forecasts/article/gold-xauusd-silver-price-forecast-gold-near-one-year-low-can-it-hold-3852-1644760)
- [FXStreet: silver at yearly lows on hawkish Fed sentiment](https://www.fxstreet.com/news/silver-price-forecast-xag-usd-hits-yearly-lows-below-4750-amid-hawkish-fed-sentiment-202611160311)
- [Washington Post: states can delay the Medicaid work requirement six months (headline)](https://washingtonpost.com/health/2026/11/13/states-can-delay-controversial-medicaid-work-requirement-six-months)
- [The Hill: Trump delays Medicaid work requirement enforcement (headline)](https://thehill.com/policy/healthcare/6220069-trump-delays-medicaid-work-requirements/)
- [Townhall: CMS gives states six more months](https://townhall.com/news/scott-mcclallen/2026/11/14/cms-gives-states-six-more-months-before-medicaid-work-requirements-are-enforced-n2686453)
- [rallies.ai: health insurers rise on the Medicaid work-rule easing](https://rallies.ai/news/health-insurers-rise-as-us-temporarily-eases-medicaid-work-rule-enforcement-be69f2c64e04f319)
- [MarketBeat: Humana upgraded by RBC, Nov 16](https://marketbeat.com/instant-alerts/analyst-humana-nyse-hum-upgraded-to-outperform-at-royal-bank-of-canada-2026-11-16)
- [Cointelegraph: bitcoin falls to a four-month low near $62K](https://cointelegraph.com/markets/bitcoin-four-month-low-62k-crypto-market-selloff)
- [KuCoin: bitcoin drops to $62,000 on ETF outflows and liquidations](https://www.kucoin.com/news/flash/bitcoin-falls-to-62-000-dollar-three-month-low-amid-etf-outflows-and-liquidations)
- [Wall Street Horizon: Coinbase earnings calendar](https://www.wallstreethorizon.com/coinbase-earnings-calendar)
- [StreetInsider: CNC earnings estimate](https://www.streetinsider.com/ec_earnings.php?q=cnc)
- [Earnings Whispers: CNC](https://www.earningswhispers.com/stocks/CNC)

## Current book state
*Auto-generated. These are live figures - use them, do not estimate.*

- Time now: **10:05 ET** (15:05 UTC, 16:05 Stockholm), Monday 2026-11-16. The cash session opened 35 min ago and closes at 16:00 ET (22:00 Stockholm).
- Equity: **$102,438.09**
- Cash: $125,772.29
- Session P&L so far: +0.20% (new entries are blocked at -3.0%)
- Gross exposure: $44,364 (43% of equity, cap 150%)
- Net exposure: $-44,364 (-43%, cap +/-100%)
- Risk at stake (entry to stop): $1,018 (0.99% of equity, cap 4.0%) — 3.01% left for new plays
- Slots: 1 open + 1 resting entries of 8 — you may add at most 6 more
- *Gross, net, risk and slots count resting entries as if filled.*
- A new long can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).
- A new short can be up to 50% of equity in notional: at 1% risk its stop must be at least 2.0% from entry (half that at 0.5%).

### Open positions

*Stop and target are the live resting orders. To change them, put the position in the `manage` array of your JSON block — prose alone does not move an order. Share of equity is signed notional, for the sector cap.*

| Symbol | Side | Qty | Avg entry | Last | Unreal. P&L | Share of equity | Stop | Target |
|---|---|---|---|---|---|---|---|---|
| IWM | short | 85 | 281.03 | 274.52 | +553 (+2.3%) | -23% | 287.00 | 271.00 |

*What you wrote when you opened each one. The invalidation is the test for closing it early.*

- **IWM**, opened 2026-11-10 (session 5 of at most 10), submitted with stop 287 and target 271, P 36%. Thesis: Small caps are the most rate-sensitive equity cohort; a front-end repricing should pull IWM from +2% above its 20d average back toward the 270 range low. Invalidation: 2-year yields fully reverse the CPI move, or IWM closes above 284.

### Resting entries (unfilled, carried from earlier sessions)

*These are live GTC orders and fill without you. Re-proposing the name in `plays` is rejected; to change the levels use `manage` with `update`, to withdraw the idea use `manage` with `close`. Unfilled entries are cancelled after 5 days and before every weekend or market holiday.*

| Symbol | Side | Qty | Entry | Type | Stop | Target | Submitted |
|---|---|---|---|---|---|---|---|
| GLD | short | 60 | 350.50 | stop | 359.00 | 333.00 | 2026-11-16 |

### Your record

49 closed trades: 15W / 34L, total -0.64R, net $+1,900 realized.

*Every idea is scored on the bracket as you submitted it: which of the initial target and the initial stop came first, within 10 sessions. R is profit over the risk budgeted.*

| | Ideas | Target first | Stop first | Average R |
|---|---|---|---|---|
| Trades taken, as managed | 49 | 17 | 29 | -0.01R |
| The same trades, bracket left alone | 49 | | | +0.01R |
| Ideas you passed on, or the caps dropped | 97 | 34 | 54 | +0.02R |

What you said against what happened, trades and passes together:

| You said | Ideas | Reached target first |
|---|---|---|
| 0%-30% | 1 | 100% |
| 30%-35% | 39 | 46% |
| 35%-40% | 63 | 29% |
| 40%-45% | 26 | 46% |
| 45%-50% | 4 | 25% |
| 50%-60% | 1 | 100% |

Base rate: 38% of 134 brackets reached target first. Your Brier score is 0.237; saying 38% every time scores 0.236. Your probabilities are not yet telling the better ideas from the worse ones: start from the base rate and move off it only for a reason you can name.

### Last 5 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| AMZN | long | stop | -1.20R | $-303 | 36% |
| DAL | long | stop | -0.60R | $-154 | 37% |
| XLE | short | close | -1.02R | $-521 | 37% |
| AVGO | short | close | -0.92R | $-232 | 37% |
| NVDA | short | target | +2.16R | $+1,108 | 37% |

### Market data

*From Alpaca. History and averages are completed sessions (SIP, consolidated volume); last is the more recent of today's latest IEX trade and the consolidated tape as of 15 minutes ago, marked which; a stop entry's trigger has to be beyond it when the order goes in. A level taken from this table counts as verified. ATR is the 14-session average true range: a stop inside one ATR of entry is inside ordinary daily noise.*

#### Your positions and resting entries

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| IWM | 274.54 (10:05 iex) | -1.1% | 277.54 | 276.10 / 274.57-276.54 | 5.46 (2.0%) | 270.23-286.17 | -0.3% / -1.1% | +1.4% | 23.4M |
| GLD | 355.47 (10:05 iex) | +0.0% | 355.45 | 354.13 / 353.97-356.29 | 7.60 (2.1%) | 352.91-381.93 | -3.6% / -6.7% | -4.6% | 9.3M |

#### Indices, rates, commodities and sectors

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 744.77 (10:05 iex) | -1.3% | 754.37 | 749.67 / 744.92-749.82 | 12.77 (1.7%) | 732.71-775.64 | -0.6% / -1.3% | +2.6% | 47.0M |
| QQQ | 665.25 (10:05 iex) | -2.2% | 679.89 | 671.04 / 665.50-672.15 | 18.61 (2.7%) | 647.05-727.95 | -2.2% / -5.3% | +3.6% | 49.6M |
| IWM | 274.54 (10:05 iex) | -1.1% | 277.54 | 276.10 / 274.57-276.54 | 5.46 (2.0%) | 270.23-286.17 | -0.3% / -1.1% | +1.4% | 23.4M |
| DIA | 520.49 (10:04 iex) | -0.5% | 523.15 | 522.98 / 520.29-523.09 | 7.61 (1.5%) | 508.66-536.60 | +0.2% / +0.8% | +2.1% | 3.6M |
| TLT | 79.73 (10:05 iex) | +0.4% | 79.38 | 79.51 / 79.47-79.72 | 0.76 (1.0%) | 79.01-82.42 | -1.9% / -0.6% | -3.1% | 35.8M |
| GLD | 355.47 (10:05 iex) | +0.0% | 355.45 | 354.13 / 353.97-356.29 | 7.60 (2.1%) | 352.91-381.93 | -3.6% / -6.7% | -4.6% | 9.3M |
| USO | 142.06 (10:04 iex) | -2.4% | 145.58 | 142.69 / 138.36-142.69 | 5.67 (3.9%) | 138.47-171.82 | -6.7% / -4.7% | -1.9% | 5.4M |
| SMH | 464.89 (10:05 iex) | -4.5% | 486.75 | 468.71 / 462.56-473.33 | 27.23 (5.6%) | 445.59-571.00 | -6.1% / -13.0% | +4.9% | 11.8M |
| XLK | 165.72 (10:05 iex) | -2.7% | 170.28 | 166.58 / 165.51-167.75 | 6.27 (3.7%) | 162.14-191.55 | -4.7% / -9.0% | +3.4% | 12.5M |
| XLF | 58.52 (10:05 iex) | -0.3% | 58.68 | 58.78 / 58.45-58.81 | 1.01 (1.7%) | 55.03-60.04 | +2.8% / +4.9% | +2.7% | 32.9M |
| XLE | 63.81 (10:05 iex) | -1.8% | 64.96 | 64.52 / 63.80-64.69 | 1.71 (2.6%) | 60.43-70.15 | -1.8% / +0.1% | +5.4% | 36.4M |
| XLV | 189.91 (10:05 iex) | +0.6% | 188.85 | 190.70 / 189.68-191.33 | 3.70 (2.0%) | 175.27-192.32 | +2.8% / +8.0% | +2.2% | 11.1M |
| XLI | 167.29 (10:05 iex) | -0.9% | 168.78 | 167.72 / 167.44-168.49 | 3.38 (2.0%) | 161.74-172.40 | +0.6% / -0.1% | +3.8% | 8.7M |
| XLY | 118.67 (10:05 iex) | -1.1% | 119.98 | 119.62 / 118.64-119.81 | 2.56 (2.1%) | 112.67-122.92 | +2.3% / +5.5% | +2.0% | 9.0M |
| XLP | 92.98 (10:05 iex) | +0.7% | 92.35 | 93.22 / 92.71-93.48 | 1.64 (1.8%) | 86.36-93.40 | +3.2% / +8.0% | +2.5% | 19.0M |
| XLU | 44.31 (10:05 iex) | +0.6% | 44.04 | 44.23 / 44.19-44.40 | 0.60 (1.4%) | 41.28-44.14 | +2.2% / +5.3% | +2.1% | 25.0M |
| XLB | 52.17 (10:05 iex) | -0.1% | 52.23 | 52.22 / 51.95-52.30 | 1.03 (2.0%) | 50.61-54.63 | -0.0% / +2.7% | +0.5% | 11.9M |
| XLRE | 44.45 (10:05 iex) | +0.2% | 44.37 | 44.57 / 44.45-44.66 | 0.69 (1.6%) | 41.60-45.34 | +2.2% / +4.3% | +0.8% | 7.9M |
| XLC | 107.34 (10:05 iex) | -1.2% | 108.69 | 109.03 / 107.28-109.11 | 2.16 (2.0%) | 99.33-110.84 | +3.0% / -0.6% | +3.7% | 7.9M |
| KRE | 72.50 (10:05 iex) | -0.3% | 72.74 | 72.83 / 72.41-73.02 | 1.54 (2.1%) | 69.17-75.80 | +0.5% / +1.5% | +0.7% | 13.9M |
| XHB | 102.30 (10:05 iex) | +0.2% | 102.07 | 102.01 / 101.80-102.60 | 3.26 (3.2%) | 94.05-108.78 | +1.2% / +3.7% | -0.2% | 2.4M |

#### Large caps

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 353.65 (10:04 iex) | -0.7% | 356.27 | 357.12 / 353.42-357.14 | 9.45 (2.7%) | 325.08-360.83 | +3.0% / +5.2% | +4.1% | 47.4M |
| MSFT | 520.74 (10:05 iex) | -0.6% | 523.88 | 525.09 / 518.81-527.95 | 17.55 (3.4%) | 504.96-559.15 | -1.0% / +0.9% | -1.3% | 26.5M |
| NVDA | 159.34 (10:05 iex) | -2.2% | 162.85 | 159.00 / 158.11-163.20 | 11.00 (6.8%) | 148.80-222.19 | -18.0% / -24.1% | -12.7% | 209.6M |
| AMZN | 260.44 (10:05 iex) | -2.3% | 266.66 | 262.39 / 260.17-262.92 | 10.74 (4.0%) | 229.36-275.34 | +3.6% / +4.6% | +2.8% | 50.1M |
| GOOGL | 287.21 (10:05 iex) | -2.9% | 295.77 | 293.81 / 287.23-294.14 | 11.91 (4.0%) | 276.92-346.58 | -2.5% / -9.9% | +3.9% | 41.0M |
| META | 627.71 (10:05 iex) | -2.2% | 641.69 | 640.00 / 627.68-640.88 | 20.96 (3.3%) | 583.80-713.22 | +0.7% / -5.6% | +5.2% | 23.8M |
| TSLA | 377.66 (10:05 iex) | -3.2% | 390.22 | 387.01 / 376.84-389.80 | 18.16 (4.7%) | 338.15-414.23 | +1.3% / +4.1% | +8.9% | 39.7M |
| AVGO | 329.86 (10:05 iex) | -4.9% | 347.01 | 332.20 / 328.88-334.69 | 20.25 (5.8%) | 289.77-369.82 | +4.8% / +0.5% | +18.2% | 26.9M |
| AMD | 510.61 (10:05 iex) | -4.4% | 534.06 | 503.44 / 502.22-526.20 | 47.88 (9.0%) | 402.10-594.00 | +2.9% / -3.7% | +18.9% | 34.7M |
| ORCL | 120.55 (10:05 iex) | -3.8% | 125.35 | 122.78 / 120.25-123.14 | 9.46 (7.5%) | 109.21-148.48 | -1.0% / -8.1% | +8.0% | 42.0M |
| NFLX | 61.63 (10:05 iex) | -0.8% | 62.15 | 62.98 / 61.48-62.98 | 1.75 (2.8%) | 61.39-70.66 | -3.4% / -10.2% | -2.0% | 45.8M |
| CRM | 215.72 (10:05 iex) | -1.0% | 217.84 | 217.92 / 213.57-219.20 | 8.28 (3.8%) | 208.88-252.42 | -5.5% / -7.4% | +2.0% | 6.8M |
| JPM | 343.80 (10:03 iex) | -0.7% | 346.19 | 345.57 / 343.68-346.52 | 7.78 (2.2%) | 330.40-359.80 | +2.1% / +1.9% | +3.5% | 6.4M |
| GS | 896.31 (10:04 iex) | -2.2% | 916.56 | 906.49 / 893.77-908.99 | 28.97 (3.2%) | 854.45-939.38 | +1.8% / -0.6% | +5.9% | 2.0M |
| BAC | 50.52 (10:05 iex) | -1.0% | 51.02 | 50.85 / 50.42-50.90 | 1.17 (2.3%) | 49.17-53.02 | +1.0% / -5.6% | +3.2% | 35.2M |
| XOM | 168.00 (10:05 iex) | -0.9% | 169.52 | 169.53 / 167.26-170.25 | 4.75 (2.8%) | 159.11-187.32 | -2.7% / +0.7% | +2.8% | 14.2M |
| CVX | 217.27 (10:04 iex) | -1.2% | 219.89 | 220.03 / 216.57-220.03 | 5.30 (2.4%) | 206.01-236.48 | -1.4% / +2.0% | +3.4% | 8.3M |
| LLY | 1,465.37 (10:05 iex) | +1.5% | 1,443.50 | 1,453.75 / 1,453.01-1,475.25 | 50.97 (3.5%) | 1,237.60-1,458.23 | +6.6% / +16.4% | +6.7% | 3.0M |
| UNH | 411.84 (10:05 iex) | +1.1% | 407.46 | 412.00 / 409.74-415.19 | 10.81 (2.7%) | 388.00-426.55 | -0.1% / +4.2% | +3.4% | 4.9M |
| JNJ | 286.99 (10:04 iex) | +0.4% | 285.75 | 288.98 / 286.57-290.25 | 7.13 (2.5%) | 251.50-288.11 | +5.2% / +7.1% | +3.5% | 7.5M |
| WMT | 128.82 (10:05 iex) | +0.6% | 128.09 | 129.83 / 128.51-129.85 | 3.02 (2.4%) | 116.63-131.82 | +3.9% / +11.8% | +2.0% | 21.8M |
| COST | 1,107.24 (10:05 iex) | +0.1% | 1,106.21 | 1,111.44 / 1,105.03-1,117.00 | 21.67 (2.0%) | 978.87-1,109.50 | +7.2% / +14.5% | +5.0% | 2.4M |
| HD | 348.46 (10:04 iex) | -0.1% | 348.69 | 348.52 / 346.21-349.21 | 9.94 (2.9%) | 306.00-362.44 | +4.5% / +11.7% | +1.5% | 4.4M |
| CAT | 582.76 (10:04 iex) | -2.9% | 600.20 | 588.00 / 582.50-592.00 | 31.68 (5.3%) | 550.81-743.23 | -6.9% / -18.8% | +7.4% | 3.8M |
| BA | 167.71 (10:04 iex) | -2.2% | 171.50 | 170.21 / 167.71-170.50 | 6.10 (3.6%) | 165.01-193.28 | -3.5% / -9.2% | -1.1% | 10.5M |
| DAL | 87.44 (10:02 iex) | +1.4% | 86.25 | 86.00 / 85.62-88.10 | 3.30 (3.8%) | 74.14-92.52 | +3.6% / +5.4% | -1.1% | 6.6M |
| UAL | 112.13 (10:04 iex) | +2.6% | 109.31 | 108.37 / 108.37-113.24 | 5.42 (5.0%) | 94.54-122.08 | +1.8% / +1.1% | -3.0% | 5.7M |

#### Today's biggest movers among 270 other liquid names (at least $5 and 1M average volume)

*Last price against the prior close, largest moves each way. A stock that has moved this far today usually has a dated reason: find it.*

| Symbol | Last (ET) | vs prev | Prev close | Today open / low-high | ATR14 | 20d low-high | Prev vs 20d / 50d avg | 5d | Avg vol 20d |
|---|---|---|---|---|---|---|---|---|---|
| CNC | 75.03 (10:04 iex) | +5.3% | 71.27 | 74.04 / 73.92-75.36 | 3.78 (5.3%) | 64.85-78.08 | +2.1% / +6.3% | +2.2% | 5.8M |
| LUV | 46.48 (10:05 iex) | +3.4% | 44.94 | 45.16 / 44.95-46.58 | 1.71 (3.8%) | 38.50-47.01 | +3.3% / +7.3% | +1.1% | 6.6M |
| GIS | 35.44 (10:05 iex) | +3.2% | 34.32 | 34.84 / 34.83-35.48 | 1.08 (3.1%) | 32.37-37.02 | +0.3% / +1.1% | -3.4% | 8.3M |
| ELV | 443.29 (10:05 iex) | +3.2% | 429.69 | 438.27 / 438.27-444.56 | 13.31 (3.1%) | 406.90-450.69 | +0.5% / +3.5% | +1.0% | 1.4M |
| NUE | 259.04 (10:04 iex) | +2.9% | 251.73 | 254.79 / 253.01-259.10 | 11.16 (4.4%) | 244.64-287.70 | -3.9% / -1.3% | +2.8% | 1.6M |
| HSY | 177.62 (10:05 iex) | +2.8% | 172.82 | 177.31 / 174.68-178.03 | 5.52 (3.2%) | 158.55-178.33 | +2.1% / +3.6% | -2.1% | 2.0M |
| HCA | 511.38 (10:04 iex) | +2.5% | 499.05 | 505.47 / 505.47-516.35 | 19.05 (3.8%) | 439.83-521.48 | +3.9% / +10.2% | +0.8% | 1.4M |
| SBUX | 108.94 (10:05 iex) | +2.3% | 106.44 | 107.73 / 107.69-109.47 | 3.10 (2.9%) | 96.09-110.85 | +2.4% / +7.8% | +1.6% | 8.0M |
| SNDK | 815.28 (10:05 iex) | -7.9% | 885.01 | 828.23 / 799.00-838.48 | 113.94 (12.9%) | 803.97-1,424.48 | -21.3% / -38.6% | +6.0% | 12.0M |
| MRVL | 145.02 (10:05 iex) | -7.5% | 156.76 | 148.11 / 144.09-148.96 | 18.49 (11.8%) | 132.54-253.66 | -19.5% / -31.6% | +11.0% | 30.2M |
| MPWR | 1,287.93 (10:05 iex) | -7.4% | 1,390.54 | 1,319.69 / 1,286.58-1,329.40 | 102.15 (7.3%) | 1,125.00-1,513.49 | +9.9% / +8.3% | +16.8% | 1.1M |
| MU | 722.75 (10:05 iex) | -7.1% | 778.31 | 734.58 / 718.54-739.12 | 64.86 (8.3%) | 650.00-990.00 | -7.1% / -17.5% | +12.8% | 30.7M |
| TER | 232.25 (10:05 iex) | -6.9% | 249.55 | 237.61 / 229.70-238.85 | 24.21 (9.7%) | 211.63-351.95 | -11.4% / -27.2% | +14.4% | 4.5M |
| ENTG | 137.33 (10:04 iex) | -6.8% | 147.41 | 140.32 / 135.43-140.70 | 12.67 (8.6%) | 124.14-170.06 | +1.8% / -0.1% | +15.2% | 3.8M |
| MSTR | 104.08 (10:05 iex) | -6.8% | 111.62 | 103.73 / 103.28-105.79 | 8.46 (7.6%) | 108.25-155.69 | -16.8% / -22.1% | -13.4% | 17.3M |
| ARM | 177.69 (10:04 iex) | -6.7% | 190.53 | 180.51 / 176.78-181.83 | 16.08 (8.4%) | 163.13-237.88 | -7.3% / -23.2% | +9.1% | 5.8M |
