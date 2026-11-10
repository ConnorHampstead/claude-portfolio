# Monthly review: what to read and what to write

*Instructions for the monthly review routine. The routine's own prompt keeps the
mechanics (the schedule gate, syncing `main`, committing only the new report and
pushing it); this file is what it reads and writes in between. It is versioned
here so that a change to the review is a commit like any other.*

The review is read-only. Never write to `journal.csv`, `shadow.csv`,
`config.json`, `prompts/`, `state/` or `briefs/`. The one file you create is
`reviews/YYYY-MM.md`.

## Read

- `README.md` sections 5 and 11: how the score is built, and the log of what
  changed and when. Section 11 holds the checkpoint this report is measured
  against.
- `python3 desk.py score` (works offline, no keys). Use its figures rather than
  recounting: closed trades, the same trades with every bracket left alone,
  the shadow book, and calibration against the base rate.
- `journal.csv` and `shadow.csv` for anything `score` does not break down.
  `r_multiple` and `bracket_r` are profit over the risk budgeted. Reports
  written before 2026-11-10 quote R over the fill-to-stop distance, so their
  per-trade figures differ slightly from today's. `source` = `dry run` rows in
  `shadow.csv` are not passes; `outcome` = `taken` rows were traded after all.
  The `model` column carries the model and effort that wrote each idea.
- `reviews/weekly/` since the last monthly report: the thesis verdicts and each
  week's process counts. `thesis_verdict` in the journal is filled in by those
  reviews. Never fill it in yourself.
- Every earlier report in `reviews/`, oldest first. They are the memory of the
  series: carry their open observations forward and say whether each has
  strengthened, weakened or been resolved.
- `prompts/lessons.md`: what the desk is currently told its record shows.
- Where useful, the `briefs/` and their `.research.txt` logs for trades closed
  since the last report.

## The standard of evidence

One trade's R has a standard deviation of about 1.2. An average over n trades
therefore has a standard error of about 1.2 / sqrt(n): 0.27R at n = 20, 0.17R
at n = 50, 0.12R at n = 100.

- Give every average with its n and its standard error.
- Call something a pattern only at n of 20 or more and a difference of at least
  two standard errors. Below that it is an observation, and the report says so
  in those words.
- When comparing two groups, the standard error of the difference is what
  counts, not each group's own.
- Split by model and effort only when the pin has changed, and treat each label
  as its own sample.

## Write `reviews/YYYY-MM.md`

About one page of plain markdown.

1. **Header.** Date, period covered, trades closed and shadow ideas resolved in
   the period.
2. **Results.** Period and cumulative: net P&L, expectancy with its standard
   error, the same trades with brackets left alone, the shadow book, and the
   Brier score next to the score of always stating the base rate. One line per
   closed trade with its thesis verdict.
3. **The checkpoint.** Each test in README section 11's current checkpoint:
   the count so far, whether it can be decided yet, and the decision if it can.
4. **Process.** From the weekly reviews: interventions outside the three
   allowed reasons, sessions with thin research, rules the desk keeps running
   into. Counts, not adjectives.
5. **Patterns and observations.** Two to five, each labelled as one or the
   other under the standard above. Verdict mix belongs here: how many wins were
   `wrong thesis right outcome`.
6. **Follow-up** on earlier reports' open observations.
7. **Proposed lessons.** At most three lines that could replace or join those
   in `prompts/lessons.md`, each with the numbers behind it. Propose a line only
   for a pattern, never for an observation. Say which existing line, if any,
   the record no longer supports. The operator merges these by hand; do not
   edit the file.
8. **Open observations** for next month.

Everything stated must come from the repository's data. Mark anything inferred.
