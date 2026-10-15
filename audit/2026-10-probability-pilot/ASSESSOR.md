# Counts, shares and chance: assessor notes

Use with the separate [task sheet](LEARNER-TASKS.md). Keep these notes away from
initial predictions. Record prior experience, device/machine, help and whether an
answer preceded execution. Do not coach towards the expected numbers and then
record unaided success. There is no learner result or pass-rate threshold yet.

1. Five exact shares are 100/7 percent; the last is 200/7 percent. The display
   rounds these to five entries of 14.3 and one of 28.6, totalling 100.1. Counts total
   seven and exact shares total 100. Rounding changes the representation, not the
   recorded events. Accept exact fractions or equivalent reasoning; a calculator
   result without an explanation does not establish the distinction.
2. Face six stays at two out of eight, now 25%. Face two rises to two. The
   denominator changes for every share. This need not make the next six more or
   less likely under the separate independent fair-die model.
3. Under the stated independent model both faces still have chance one sixth.
   No compensation is owed by the next roll. A finite short history alone does
   not establish fairness, independence or properties of a pseudorandom generator.
   Do not generalise the ideal assumption into a claim that Spectrum RND produces
   independent physical events or exactly uniform mapped faces.
4. Inspect six counts, their sum, the positive total, the percentage formula and
   rounding before changing data. Preserve observed counts; remove a forced display
   adjustment if the aim is independently rounded shares. The count sum and exact
   shares can be correct while displayed totals differ from 100. Dividing by zero
   is invalid; count first or present a not-yet-defined share. Do not silently use
   zero percent to mean a calculated ratio of zero to zero. We did not execute a
   zero-denominator fault in this pilot.
5. At line 1120 replace the percentage calculation with
   `LET pc=INT (10000*t(j)/n+0.5)/100`, preserving its row assignment and other
   lines. This applies nearest rounding to non-negative counts at two decimals.
   Check all six displayed values against the actual counts/total; BASIC may omit
   trailing zeros. Counts must still be non-negative integers summing to twelve.
   Rounded totals may still differ from 100. This learner extension is prepared,
   not freshly executed by our unit 3 one-decimal audit; record technical or input
   failures rather than assuming the proposed edit worked.
6. Accept a bounded question with a recordable outcome, such as comparing shares
   across fresh batches. Require a count-total invariant and a limit on inference:
   neither an even nor an uneven finite display proves the generator fair. Adding
   to an existing sample shares observations with its predecessor; it is not an
   independent replicate. A novel runnable extension is optional, not a condition
   of a sound experimental plan.

For each task distinguish independent reasoning, a revised answer after observation,
a correct answer after help, and unresolved confusion. Preserve the learner's own
explanation rather than replacing it with these notes. Successful entry, copied
arithmetic and an explanation of why it works are different observations. These
prompts are prototypes; effectiveness, difficulty, transfer and retention remain
unverified until learners try them.
