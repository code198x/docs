# Observe interpreter-trace reasoning

Use the [learner tasks](LEARNER-TASKS.md) after the proposed unit. No actual learner
trial has run. Record prior experience, first predictions, explanations, revisions
and assistance. Ask how the learner reached an answer before offering a hint.

| Task | Expected reasoning | Watch for |
| --- | --- | --- |
| Changed start and bound | Totals 6, 7, 8, 9; output 9; four additions | Treating the initial value as a visit count, or stopping before the inclusive end |
| Changed increment | Totals 7, 9, 11, 13; output 13; still four visits | Doubling the visit count instead of the amount added |
| Reset each visit | Every visit resets to 5, then reaches 7; output 7 | Carrying the earlier partial sum across the next reset |
| Evidence layers | Four executions of the source update; no processor instruction count or measured extra time | Calling a BASIC token a CPU instruction, or deriving time from the final value |
| Optional empty range | No body visits; the initial total still reaches the outside SHOW | Assuming no visits means no continuation |

Do not require specialist names. A learner can explain that the processor runs
many lower-level steps to carry out the source operation. An execution trace
could count machine instructions; a named timing experiment could measure total
cost. Attributing a portion of time to interpretation would need more evidence
than observing that a shorter loop finishes sooner.

Keep arithmetic success separate from understanding those evidence limits. If
using BASIC, record source, machine, output and operating help separately. Adding
PRINT inside the loop changes the executed program; its trace is not a timing
measurement of the original program.

Mark each objective as independent / after explanation / after coaching / not yet
shown. Do not convert expected answers into learner results or infer retention
from one session. A later fresh example can probe retention if its delay and
assistance are recorded. File reproducible obstacles as bounded issues after
checking existing open and closed findings.
