# Loops and repetition: assessor notes

No learner is available and no trial has run. These are expectations and a method
for collecting future evidence, not observed learner outcomes.

Record prior experience, route, date, site/preview revision, browser/version, OS,
viewport and physical input device with consent. Keep personal information out
of the public record. Begin with one route; the second route taken by the same
learner measures transfer after practice rather than untouched independent entry.
Assembly lesson 4 assumes its earlier assembly material, not prior BASIC.

Ask for the prediction before a run, replay or answer reveal. Record help as
navigation, syntax or conceptual help. Use independent, helped, not completed or
skipped outcomes with reasons. Do not supply the explanation and count the result
as independent. Stop when the learner wishes. Avoid universal timing thresholds.

| Task | Expected reasoning or observation |
| --- | --- |
| Foundations 1 | Inclusive 1–3 gives three turns; 1–1 gives one; 1–0 gives none under the taught pseudocode convention. Do not silently apply this to every machine loop. |
| Foundations 2 | WHILE checks before the body, so zero lives skips it. REPEAT executes the body before checking. The initial value, body update and exact stopping condition all matter. |
| Foundations 3 | Three guesses, one secret assignment. The back edge returns to ASK inside the round, not to the earlier assignment. |
| Foundations 4 | Another 7 is allowed. New selection does not imply a value different from the last selection. |
| Foundations 5 | Assignment inside the loop changes the target during the search; earlier clues no longer constrain one fixed answer. Do not claim this makes winning impossible in every run. |
| Foundations 6 | New range/messages and a justified trace, with once-per-round and per-guess work distinguished. Copying the given values alone is insufficient transfer evidence. |
| BASIC 1–2 | Correct final count is three; jumping back to counter initialisation resets it before each subsequent guess, so the endpoint no longer records all attempts. Return to the input line and retest. |
| BASIC 3–4 | The lesson's fixed seed yields the same first secret. Normal selection also permits repeats. Fixed seeds help reproduce a run; a short sample does not establish fairness or security. |
| BASIC 5 | Random range, accepted guesses and player instructions must agree. Use known endpoint secrets instead of waiting for chance to produce them. |
| Assembly 1–2 | Eight writes use $4000 through $4700; $4800 is the pointer after the last increment, not another write. Four turns stop at $4300 and do not clear untouched rows. |
| Assembly 3 | The body runs before DJNZ decrements B. Zero wraps to 255; the body therefore runs 256 times. That explanation is source-checked here; this slice's maintained live verifier executes counts 4 and 8, not the unsafe zero case. |
| Assembly 4 | All eight writes target $4000. The final pattern replaces earlier values. Restore `inc d` and retest actual destinations. |
| Assembly 5 | Artwork transfer uses an executed source and same-tab state; stale drafts are not evidence of current machine output. Keep the edited download and explain the actual writes. |

The native audit driver's pre/post-test programs use explicit BASIC `IF`/`GO TO`
routes; they do not implement native BASIC WHILE or REPEAT statements. Its
post-test toy starts with zero, displays it once, decrements to -1 and then stops
under a greater-than-zero continuation guard. Do not describe that as a playable
lives rule or as equivalent to every possible UNTIL condition.

Optional pattern discovery and return are research tasks. Its 8-bit LFSR is a
different generator from Sinclair BASIC's ROM implementation, and illustrative
code is not an execution-qualified pattern. Record whether the connection helps
rather than requiring an intermediate implementation from a beginner.

| Task | Prediction | Observation/explanation | Help | Outcome |
| --- | --- | --- | --- | --- |
| Discovery | Pending | Pending | Pending | Pending |
| Entry/turn count | Pending | Pending | Pending | Pending |
| Round versus guess | Pending | Pending | Pending | Pending |
| Modify/diagnose | Pending | Pending | Pending | Pending |
| Create/transfer | Pending | Pending | Pending | Pending |
| Optional pattern/return | Pending | Pending | Pending | Pending |

Use comparable before/after tasks while accounting for practice effects. A
coached second attempt is not independent proof of improved learning.
