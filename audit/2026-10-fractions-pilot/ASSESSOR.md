# Fractions: assessor notes

No learner trial has occurred. Keep this sheet separate. Record prior experience,
chosen entry route, first predictions, actions, observed output, explanations and
help. Do not coach the first attempt; accept uncertainty. Separate tool failures
from conceptual mistakes.

| Task | Expected evidence |
| --- | --- |
| 1 | A half fits within appropriate binary precision/range; a tenth requires a recurring binary expansion. Printed digits need not show all stored information. Representability does not guarantee a particular input-conversion routine. |
| 2 | On the recorded native target, result 0. A small addition was lost at a large magnitude. Do not generalise that every calculation is inexact or every error grows. |
| 3 | 384/256 = 1.5; high byte 1 and low byte 128. Keeping only high byte gives 1, losing the half. |
| 4 | Stored 384 + 128 = 512; decoded value 2. Same-scale addition works while the result fits. |
| 5 | Nearest integer 26; 26/256 = 0.1015625. At scale 10 the stored integer 1 means exactly 1/10. |
| 6 | INT takes the whole part for this nonnegative range; it does not preserve the fraction. Record finding the optional link, table explanation and return separately. |
| 7 | Both print 0.5 on the recorded configuration. Display alone cannot settle storage equality. Native raw bytes differed; investigation is open in docs #63, so do not invent a cause or treat this as a learner error. |
| 8 | Whole-part extraction was confused with full decoding. Different scales must be converted to a common scale before direct integer addition. |
| 9 | Accept any consistent design. Unsigned 8-bit scale 2 reaches 127.5 and represents halves; position 100 means stored 200, plus a half-step 1 gives 201, decoded 100.5. Unsigned 16-bit scale 256 also works. Check chosen maximum, step, sum and allowed rounding. Timing needs a named target and actual workload evidence. |

For conceptual tasks record independent / after rereading / after a prompt /
not demonstrated. Record technical completion separately from explanation. Do
not combine one trial into an educational-effectiveness score.

Hypotheses: naming width/scale and separating display, storage and interpretation
may prevent false “never exact” beliefs and accidental loss of fractions. The
optional BASIC link may support transfer. These remain unverified.

File deduplicated findings with exact task/revision, first response, actions,
observed output and help given. Save anonymous evidence, not invented names,
quotations or outcomes. The broader umbrella requirements remain open.
