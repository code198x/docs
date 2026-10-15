# Boolean conditions assessor notes

No learner is available. All learner outcomes are **not observed**. Keep this
file separate from the learner tasks during a trial. Source, ROM/Z80 execution
and browser checks do not establish educational effectiveness.

Record relevant experience, the page revision, device/browser, predictions,
explanations, changes of mind and help supplied. Distinguish independent work,
understanding after reading the answer, coaching, incomplete work and uncertain
evidence. Ask for an explanation without teaching it first. A learner can pause,
read an answer or stop; there is no score or completion time to enforce.

| Task | Expected distinction | Learner outcome |
| --- | --- | --- |
| 1 | For inputs 00,01,10,11: AND 0001; OR 0111; XOR 0110. Both-true is the last row and separates OR/XOR. | Not observed |
| 2 | A AND A and A OR A both equal A. Adding an AND cannot add passing cases; adding an OR cannot remove them. Either may change nothing. Repeated tests of the same fixed score produce only 00/11. | Not observed |
| 3 | Original guard passes only button=1, onGround=1, stunned=0. Removing NOT instead passes 111; the result differs in rows 110 and 111. | Not observed |
| 4 | Both columns are 1000 in 00,01,10,11 order. Equal Boolean results for the same inputs do not establish runtime cost, errors or side effects. | Not observed |
| 5 | Original guard is FALSE; renamed guard is TRUE. The stored alive flag violates alive = NOT dead. Recompute or maintain the complementary facts before relying on the rename. | Not observed |
| 6 | NOT (paused OR finished) and (NOT paused) AND (NOT finished), columns 1000. An example wrong alternative is NOT (paused AND finished), column 1110: rows 01/10 expose it. Other correct forms accepted. | Not observed |
| Optional BASIC | g<1 and g>10 reject the same range failures as their OR, with the same unchanged input. Neither range test alone rejects 6.5; keep the integer check. | Not observed |
| Optional Pattern | Death wins over pause under this pattern's stated policy. A different priority is another design decision; the Boolean table alone does not choose it. | Not observed |

Do not mark a full truth table wrong because a game's rules make some rows
unreachable. Ask the learner to distinguish the complete Boolean input space
from states that the chosen inputs can produce. Conversely, a missing Boolean
row cannot be justified by silently assuming a game invariant.

The native audit is configuration-specific. For 0/1 operands, actual Spectrum
BASIC results and Z80 operations match the selected Boolean rows. BASIC <> is
used for the differing-input result; this is not a Spectrum XOR keyword. Spectrum
10 AND 5 returns 10 and 10 OR 0 returns 10. Those numeric operations are not a
universal Boolean representation or Z80 bit-mask rule. The two tested expressions
0 AND (1/0) and 1 OR (1/0) report Number too big: do not assume a guard prevents
all evaluation of the other operand in every language.

The public lesson does not prescribe an order of evaluation for jobs with side
effects. De Morgan's truth-value laws remain valid; a table alone does not prove
all runtime behaviour. In particular, do not claim that applying De Morgan's
laws necessarily changes evaluation order or breaks short-circuiting.

Record observed confusions as concrete symptoms, check existing issues, and
file confirmed blockers in the owning repository. Keep #114/#115/#124 open for
remaining coverage and learner evidence. Continue the separate audit queue while
learner trials are unavailable; only guide-pack expansion is paused.
