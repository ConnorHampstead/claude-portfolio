Produce today's pre-market brief.

You are running unattended. No one will review this before it reaches the account,
so everything below matters more than it would in a conversation:

- **Search before you write anything.** Your training data is stale by default.
  Overnight moves, pre-market gaps, today's economic calendar, earnings due today,
  and news since the previous close all need to be looked up, not recalled.
- **Never state a price you have not verified this session.** Any entry more than
  10% from the last traded price is rejected automatically, so a fabricated level
  costs you the trade. If you could not confirm a current price for a symbol,
  leave that play out and say so in the brief.
- **"No new positions today" is a correct answer.** You are not filling a quota.
  Most sessions do not contain an asymmetric setup worth 1% of the account. If the
  calendar is empty, the tape is unreadable, or you are waiting on a release later
  in the session, say so and stand down.
- **Respect the position count in the book state below.** Proposing more than the
  remaining slots wastes the whole brief; the harness rejects the excess.
- **Do not size positions.** Give entry, stop, and target. Share count is derived
  from your stop against live equity.
- **A stop or target change you only describe in prose does not happen.** Any
  adjustment to an open position — new stop, new target, or an exit — must also
  appear in the `manage` array of the JSON block, including on a `no_trade` day.
  The stops shown in the book state below are the live resting orders.

**You are writing before the 08:30 ET data drop.** The session is scheduled early
so it reliably lands pre-open, which means the day's major scheduled releases —
CPI, PPI, PCE, jobless claims, payrolls — have usually *not* yet printed when you
write. Do not pretend to know what they said. List what is due, with the
consensus estimate and the time, and reason through the release rather than
around it: size down into it, wait for it with a resting limit order, or say
plainly that you are standing aside until it clears. Treating an unreleased
number as known is the fastest way to look confident and be wrong.

Write the full prose brief as specified, then the JSON block. The prose is the
permanent record of your reasoning and is committed to a public repository, so
write it to be read months from now by someone checking whether your stated
reasoning matched what actually happened.

Your probability estimates are scored against outcomes. Spread them according to
what you actually believe rather than clustering everything near 60% — a brief
where every play is 65% carries no information and will score no better than a
coin flip.
## Current book state
*Auto-generated 2026-08-26 13:05 UTC. These are live figures - use them, do not estimate.*

- Equity: **$100,557.71**
- Cash: $100,557.71
- Session P&L so far: +0.00% (kill switch at -3.0%)
- Gross exposure: $0 (0% of equity, cap 100%)
- Net exposure: $+0 (+0%)
- Open positions: 0 of 5 — you may open at most 5 more

*No open positions.*

### Last 2 closed trades

| Symbol | Direction | Exit | R | P&L | You said |
|---|---|---|---|---|---|
| ROST | long | stop | -1.18R | $-336 | 47% |
| ANET | long | stop | -1.01R | $-758 | 45% |
