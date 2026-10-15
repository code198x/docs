# Decisions and boundaries: assessor notes

No learner trial has run. The owner reports that no learner is available; these
notes specify what to observe rather than filling the gap with AI responses.

Use one independent entry route per initial trial. Record prior experience,
date, site/preview revision, browser/version, OS, viewport and input device, with
consent and without public identifying details. Assembly lesson 8 assumes the
earlier assembly sequence; it is not an independent first programming lesson.
Do not make BASIC completion an assembly prerequisite. A later route attempted
by the same learner measures transfer after practice, not untouched entry.

Ask for the prediction before revealing or running. Record the learner's
explanation and help needed. Distinguish navigation help, syntax help and help
with the concept. Use outcomes of independent, helped, not completed or skipped
with reason. Timing is an observation, not a pass threshold. Do not call a task
independent after supplying its answer.

| Task | Expected observation/reasoning |
| --- | --- |
| Foundations 1 | Inputs and computed output can differ while the instruction sequence stays fixed. `IF` makes an instruction conditional. |
| Foundations 2 | Strictly greater than zero is false for -1 and 0, true for 1. The comparison does not assign to `guess`. |
| Foundations 3 | Equality with zero is true only for 0 among these cases. |
| Foundations 4 | Zero disproves the claim. A prompt does not enforce an input range. A condition can be always true at a point only under actual constraints on values reaching that point. |
| Foundations 5 | Learner chooses a new secret, uses mutually exclusive comparisons to the same secret and explains the three cases. Do not accept copying the given values alone as transfer. |
| BASIC 1 | 4 → Too low; 7 → Correct!; 9 → Too high. All three numbered conditions are tested. Independent `IF`s are not a pseudocode `ELSE IF` chain. |
| BASIC 2 | 0 gets Too low in lesson 5; validation is added in lesson 6. Rejecting 0 here would describe a different program. |
| BASIC 3 | With `<` changed to `>` on line 50, 9 prints both Too low and Too high; 4 gets neither. Restore `<` and rerun lower/equal/higher cases. |
| BASIC 4 | New secret, genuinely new test values and one justified message per numeric case. |
| Assembly 1–2 | Faulty branch skips left movement at nonzero position. Loading A does not change RAM. `or a` sets Z according to A without decrementing the position. Inspect the observed state, not just the displayed source. |
| Assembly 3–4 | Repaired `jr z,wait_frame` skips the decrement at position 0 and falls through at an ordinary nonzero position. One ordinary move is insufficient boundary evidence. |
| Assembly 5 | A working position can coexist with the wrong erase pattern. Actual pointed data distinguishes the fault; retest erasure as well as position. |

The assembly Z flag is processor state set by instructions, not a named BASIC
Boolean variable or an independently reevaluated condition. The test values
here are unsigned screen positions; do not infer a signed arithmetic rule for
all Z80 comparisons from this one zero test.

For optional Vault reading, record whether the connection helps and whether the
learner returns successfully. Editorial review metadata does not prove beginner
readability. Do not require recall of advanced state-machine examples.

Copy an anonymous observation sheet for an actual trial:

| Task | Prediction | Observed result/explanation | Help | Outcome |
| --- | --- | --- | --- | --- |
| Discovery | Pending | Pending | Pending | Pending |
| Predict/explain | Pending | Pending | Pending | Pending |
| Modify | Pending | Pending | Pending | Pending |
| Diagnose/repair | Pending | Pending | Pending | Pending |
| Boundary | Pending | Pending | Pending | Pending |
| Create/transfer | Pending | Pending | Pending | Pending |
| Optional connection/return | Pending | Pending | Pending | Pending |

Repeated prompts after instruction have practice effects. Use the existing and
proposed pages to inspect presentation changes, but do not treat a coached
second attempt as independent proof of better learning.
