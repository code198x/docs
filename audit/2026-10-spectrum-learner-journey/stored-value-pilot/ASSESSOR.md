# Stored values: assessor notes

Status: prepared for review; no learner trial. The owner reports that no learner
is currently available. Do not infer educational effectiveness from technical
execution or from these expected answers.

## Trial method

Use [the prompts](LEARNER-TASKS.md) with consent. Keep identifying details out of
public records. Give the learner one entry route, with no preceding route
required. Record prior experience, chosen route and whether the first relevant
lesson is found without a supplied link. Provide the link only after recording
discovery difficulty. A person who completes BASIC before assembly is testing
transfer on the second route, not independent assembly entry.

Record the site's deployment identity, date, OS/browser version, viewport and
physical input/device. Use a local preview containing the proposed Foundations
fix for route F until it is published. A narrow desktop viewport does not
establish physical mobile, touch-keyboard or Safari behaviour.

Ask for a prediction before a run or reveal. Record it verbatim where practical,
then record the observed result and the explanation. Allow normal lesson links.
If help is needed, first ask what is unclear; distinguish help finding a control,
help reading syntax and help with the underlying concept. Do not quietly supply
the explanation and count the task as independent success.

Classify each task: completed independently; completed with navigation/syntax
help; completed with conceptual help; not completed; or skipped, with reason.
Record timing as an observation, not a universal usability threshold. Stop when
the learner wants to stop. A small pilot identifies difficulties and possible
improvements; it cannot establish population-wide effectiveness.

## Expected reasoning

| Task | Expected result | Evidence of understanding |
| --- | --- | --- |
| F1 | `Score: 0`, `Score: 0`, `Score: 100`; final `score` is 100 | Reads do not consume the value; assignment replaces it. |
| F2 | `3`, `3`, `1`; final `lives` is 1 | Earlier output records an earlier read, not a live reference to the variable. |
| F3 | Check `life` versus `lives` | The names differ. Do not demand a particular error message from pseudocode whose runtime errors are unspecified. |
| F4 | New example has two reads before one replacement and a final read | Learner can choose values/names and explain the changing instruction without copying the worked listing. |
| B1–B2 | `ONE`, `ONE`, `TWO`; earlier output remains | Explain `LET`, `PRINT`, the text literal and variable name, without treating `$` as part of the stored text. |
| B3 | First `ONE`, then `2 Variable not found` at line 30; line 40 is not reached | Diagnose the different name, repair that line, predict the recovered output. |
| B4 | An original listing meeting the same read/replace requirement | Predict before running and keep the current edited artefact. Download alone does not prove a working reload. |
| A1 | Initial bitmap `%10101010` (170), attribute 71 | Label names an address; memory byte, register and screen byte are distinct stores. Colour also depends on the attribute. |
| A2 | Editing alone leaves machine state unchanged; rerunning writes `%11110000` (240) | Distinguish source text, assembly and execution. |
| A3 | Final bitmap `%00001111` (15), not `%11111111` | The later write replaces `$4000`; neither bitmap write targets `pattern`. The screen inspector alone does not prove the source byte is unchanged. |
| A4 | First bitmap byte remains 240, next is 15 | Explain destination address and repair the second destination to `$4000`. Inspect the actual screen; the eight-pixel magnifier covers only the first byte. |
| A5 | Second write determines the final first-byte pattern | New patterns and explanation demonstrate adaptation beyond supplied values. |

Optional Vault reading tests the usefulness of the connection, not recall of
descriptor sizes or addresses. Record unfamiliar terms and whether the learner
can return to the lesson. The article's `reviewed: true` is editorial metadata,
not a beginner-comprehension result.

## Observation record

Copy this table for each anonymous trial. Do not populate it with AI answers.

| Task | Prediction | Observation/explanation | Help needed | Outcome |
| --- | --- | --- | --- | --- |
| Discovery | Pending | Pending | Pending | Pending |
| Read/predict | Pending | Pending | Pending | Pending |
| Modify | Pending | Pending | Pending | Pending |
| Diagnose/repair | Pending | Pending | Pending | Pending |
| Create/transfer | Pending | Pending | Pending | Pending |
| Optional depth/return | Pending | Pending | Pending | Pending |

Before/after technical checks establish implementation behaviour. To compare
learning before and after, account for practice effects: repeating the same
prompt with the same learner after explaining its answer is not independent
evidence that the revised wording teaches better.
