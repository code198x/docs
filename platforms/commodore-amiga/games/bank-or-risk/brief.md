# Bank or risk AMOS opening game

**Status: game direction agreed; rules and numerical tuning prepared for native
prototype review.** Build a solo dice game around the choice to keep a total or
risk another roll. The risk increases as the total approaches a visible limit.
It is the proposed first game in the [AMOS course](../../amos/course-brief.md).
No AMOS prototype or replacement lessons are delivered by this brief.

## Experience and first scope

Roll one six-sided die to build a round total. Before each further roll, choose
whether to bank that total or risk adding another number. A total above 21
busts: the round contributes zero. Exactly 21 banks automatically. Banking
secures the current total and begins the next round.

The provisional challenge is **90 points across at most five rounds**. Show the
limit, round, current total, secured score and target together. The player has
time to consider the choice; there is no reaction timer. End with success at
the target, or failure when the remaining rounds cannot possibly reach it.
Retain the result and offer a fresh challenge or exit.

The appeal is the decision before a roll: what could be gained, what could be
lost, and how much the session still needs. Near the target, banking a modest
total can be the right choice; after low earlier scores, taking a risk may be
the only way to stay in contention. These numbers are tuning for a play trial,
not an approved difficulty or a claim about beginner success rates.

Keep one die and one player. Cards, a dealer, betting money, a computer opponent,
multiple dice, persistent records, animation, pointer controls and a campaign
are outside the first prototype. The resemblance to Blackjack/Pontoon is the
bank-or-continue decision near a limit; this is not an implementation of their
card or dealer rules.

## Rules and state

| Situation | Result |
| --- | --- |
| Start a challenge | Secured score 0, round 1, current total 0. The first roll is required before banking. |
| Roll at a current total below 21 | Add one value from 1 through 6, showing the value and new total. |
| New total below 21 | Wait for a new roll or bank choice. Do not roll again automatically. |
| New total exactly 21 | Secure 21 once and finish the round. Equality is not a bust. |
| New total above 21 | Show the bust total, secure zero for that round and preserve earlier secured points. |
| Bank after a roll | Add the current total to secured points once and finish the round. |
| Finish a round | Evaluate the secured score and remaining opportunities before beginning another round at zero. |
| Target reached | Hold a success result; no further rolls change the score. |
| Secured score plus 21 times remaining rounds is below target | Hold a failure result and explain why the challenge has ended. |
| Invalid input or bank before the first roll | Keep score, round and total unchanged; repeat the relevant prompt. |
| Replay at a result | Restore the full initial state, including input readiness; do not retain an earlier total. |
| Quit | Return to the editor through the checked route. An unfinished total is not banked by quitting. |

The completed-round count is distinct from the number shown for an active round.
There are at most five completed rounds. Finish and scoring work happens once
per completed round. A held key must not supply another roll, bank twice, or
start and act in the next round. After resolving a round, show what was secured
and require a fresh continue action if the challenge can continue.

With this tuning, one bust makes the challenge unreachable: even four perfect
rounds provide only 84. The failure screen should make that consequence clear.
Earlier secured points remain visible even though the target is missed. If this
feels too severe in native play, adjust the rounds and target together and rerun
the rules analysis; do not imply that bust only consumes a recoverable round.

## Risk and target checks

Assume an ideal die with six equally likely independent outcomes for this design
analysis. Totals through 15 cannot bust on the next roll. At 16, one outcome
busts; at 17, two do; at 18, three do; at 19, four do; at 20, five do. At 21
the round has already finished. The visible total therefore changes the risk.

A policy of banking whenever the total first reaches 16 never busts: the last
safe roll starts at 15 or less and cannot exceed 21. Five such rounds secure
at least 80. A target at or below 80 would allow that policy to succeed every
time, so it would not require the player to engage with the risky decision.

The exact ideal-die model in [rules_check.py](rules_check.py) compares that safe
policy with choices that maximise the chance of reaching 90. It also checks the
same current total under different remaining needs. This is a rules and tuning
check, not evidence about AMOS's random generator, player behaviour or fun.
The [analysis record](rules-analysis.md) gives the results and rerun command.

Do not teach optimal play as an upfront requirement. Let learners predict which
rolls would bust and explain a choice. The deeper probability analysis can be
optional material after the game works.

## Target and working route

Use AMOS Professional 2.00 from official revision
`533b4b1f5acd604814513f78e02c7b4796cb0531`. The existing
[execution baseline](../../../../audit/2026-10-amiga-unit-five/REPORT.md) uses
FS-UAE 3.2.35, PAL A1200/68020, 2 MB chip and 8 MB fast memory, Kickstart and
Workbench 3.1. It qualifies selected earlier programs, not this game or a minimum
hardware requirement. Supply the firmware and OS through the established lawful
route; keep media out of the source repository.

Maintain the later native prototype in code-samples under
`commodore-amiga/amos/bank-or-risk/prototype/`. Check the actual AMOS random-number
range, seeding behaviour, input and stop controls against the named runtime and
original manual before writing their lesson explanations. Keep any deterministic
test sequence separate from normal random play and identify its method.

Save the learner's source early, reopen it in a fresh session and run the edited
version. Distinguish a saved source program from a screenshot or emulator state.
A host-side rules model supplies neither the AMOS program nor its save evidence.

## Proposed teaching sequence

These are stages to split into lessons as necessary, with complete maintained
sources and explicit edits. Introduce every required line before relying on it.

| Stage | Result | Idea to explain locally | Check |
| --- | --- | --- | --- |
| State the challenge | Display an inviting message and the limit; edit the words | Instructions, strings, run and return to editing | Edited output appears; deliberate syntax error can be repaired. |
| Keep the program | Save and reopen the edited source | Filename, storage and source versus output | The fresh session runs the saved edit. |
| Make one roll | Show one die result | Random selection and its exact integer range | Prescribed boundary results are 1 and 6; ordinary runs stay within range without claiming a finite sample proves fairness. |
| Add a roll | Combine a stored total and a new result | Assignment and addition | Explain old total, rolled value and new total separately. |
| Read the limit | Display active, exact-limit and bust results using prescribed examples | Comparisons and decisions | Totals 20, 21 and 22 take their intended paths. |
| Choose another roll | Repeat while the round is active, with a reliable quit | Input and repetition, taught in separate steps | One accepted choice requests one roll; waiting does not change the total. |
| Keep or risk it | Bank ends the round with its score; bust scores zero | A player's decision and distinct displayed total versus awarded points | Bank preserves the shown points; bust can show 22 while awarding zero. |
| Build a challenge | Retain secured points across rounds, count finished rounds, and show the target | Values with different lifetimes, introduced separately | The current total resets while secured points remain; each result is counted once. |
| Finish deliberately | End at the target or when it is unreachable; offer replay and exit | Session conditions, reset and input boundaries, introduced separately | Known success and failure sequences; no extra round, repeated bank or stale replay input. |
| Improve and investigate | Add an original die-face picture, readable layout and short result cues in separate stages | Counted drawing or a named drawing routine when useful; sound tied to an event | Numbers and picture agree, labels remain legible, result cues fire once, and play works muted. |

The first complete single-round game precedes the session challenge. Explain that
the session target adds a reason to balance safety against the points still
needed; a score-maximising single-round example alone has a safe stopping rule.
There is no required fixed lesson count or lesson duration.

Provide prediction, diagnosis and a small independent variation with hints.
For example, explain why changing `>` to `>=` wrongly rejects a perfect 21, or
trace what must reset after banking. A changed limit requires reconsidering the
target and tests; it is not an isolated cosmetic edit.

## Distinctness and finishing

The [opening comparison](../../amos/opening-candidates.md) records the inspected
cross-track material. Spectrum Dice Roller and C64 Tally explore frequencies;
their player chooses a sample or watches accumulation. This game asks the player
to secure points or expose the current total to a growing risk of loss. Sharing
a die and random-number syntax does not repeat that activity. No existing game
is commissioned for a deliberate revisit here.

Use readable text first. Add an original die image and sound through explained
stages, with numbers and labels carrying every essential result. Keep the current
total, limit and secured score visually distinct. Leave enough time to read a
roll; do not use blocking decoration or sound as an unexplained timing mechanism.

The prototype acceptance run must cover rolls 1 and 6, totals 20/21/22, banking
exactly once, a bust preserving earlier points, target equality, an unreachable
target, final-round completion, invalid input, held/released input, repeated
rounds, replay, quit and fresh save/reopen. Inspect graphics and listen to cues
if present. Negative controls must reject an equal-limit bust and a bust that
awards its displayed total.

Native play should answer whether the decision remains interesting, whether a
bust ending the challenge feels fair, and whether the target invites another
attempt. A real beginner should later try the opening without coaching. Until
then, keep design analysis, native correctness, human play and learning evidence
separate. The rest of the AMOS lineup and any language implementation remain
independent decisions.
