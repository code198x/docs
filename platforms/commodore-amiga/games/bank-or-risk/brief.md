# Bank or risk AMOS opening game

**Status: browser playtest accepted at 10/5/30; native rules, input and
save/reopen checked on the recorded Emu198x configuration.** The
[prototype record](prototype.md) identifies source, probes and execution evidence.
Build a solo dice game around the choice to keep a total or risk another roll. The risk increases as the total approaches a visible limit.
It is the proposed first game in the [AMOS course](../../amos/course-brief.md).
The prototype record distinguishes native execution from pending presentation
stages and replacement lessons.

## Experience and first scope

Roll one six-sided die to build a round total. Before each further roll, choose
whether to bank that total or risk adding another number. A total above 10
busts: the round contributes zero. Exactly 10 banks automatically. Banking
secures the current total and begins the next round.

The accepted opening challenge is **30 points across at most five rounds**, with a
round limit of **10**. Show the limit, round, current total, secured score and
target together. The player has
time to consider the choice; there is no reaction timer. End with success at
the target, or failure when the remaining rounds cannot possibly reach it.
Retain the result and offer a fresh challenge or exit.

The appeal is the decision before a roll: what could be gained, what could be
lost, and how much the session still needs. Near the target, banking a modest
total can be the right choice; after low earlier scores, taking a risk may be
the only way to stay in contention. The user accepted the browser playtest's
scope and tuning as appropriate for the first game. Retain that simplicity while
developing the native AMOS version. This does not establish beginner success
rates or qualify the native implementation.

Keep one die and one player. Cards, a dealer, betting money, a computer opponent,
multiple dice, persistent records, animation, pointer controls and a campaign
are outside the first prototype. The resemblance to Blackjack/Pontoon is the
bank-or-continue decision near a limit; this is not an implementation of their
card or dealer rules.

## Rules and state

| Situation | Result |
| --- | --- |
| Start a challenge | Secured score 0, round 1, current total 0. The first roll is required before banking. |
| Roll at a current total below 10 | Add one value from 1 through 6, showing the value and new total. |
| New total below 10 | Wait for a new roll or bank choice. Do not roll again automatically. |
| New total exactly 10 | Secure 10 once and finish the round. Equality is not a bust. |
| New total above 10 | Show the bust total, secure zero for that round and preserve earlier secured points. |
| Bank after a roll | Add the current total to secured points once and finish the round. |
| Finish a round | Evaluate the secured score and remaining opportunities before beginning another round at zero. |
| Target reached | Hold a success result; no further rolls change the score. |
| Secured score plus 10 times remaining rounds is below target | Hold a failure result and explain why the challenge has ended. |
| Invalid input or bank before the first roll | Keep score, round and total unchanged; repeat the relevant prompt. |
| Replay at a result | Restore the full initial state, including input readiness; do not retain an earlier total. |
| Quit | Return to the editor through the checked route. An unfinished total is not banked by quitting. |

The completed-round count is distinct from the number shown for an active round.
There are at most five completed rounds. Finish and scoring work happens once
per completed round. A held key must not supply another roll, bank twice, or
start and act in the next round. After resolving a round, show what was secured
and require a fresh continue action if the challenge can continue.

A bust consumes one round, not the entire challenge. After an opening bust,
four rounds can still secure up to 40 points, so the target of 30 remains
reachable. Recovery depends on the score and rounds remaining: a sufficiently
late bust can still make the target impossible. Explain that outcome through the
visible secured score and remaining opportunities.

## Risk and target checks

Assume an ideal die with six equally likely independent outcomes for this design
analysis. Totals through 4 cannot bust on the next roll. At 5, one outcome busts;
at 6, two do; at 7, three do; at 8, four do; at 9, five do. At 10 the round has
already finished. The visible total therefore changes the risk.

A policy of banking whenever the total first reaches 5 never busts, but guarantees
only 25 points across five rounds. It reaches the target of 30 in 80.630706% of
ideal-die challenges. Always banking at 6 or above accepts some risk and succeeds
in 86.836201%; pushing to 7 lowers that to 77.922639%. Taking more risk is not
always better.

Choosing according to the current total, secured score and rounds remaining can
raise the mathematical success probability to 95.320953%. After the first round
busts, the corresponding best possible recovery chance is 60.126571%. These are
policy calculations, not measured human win rates. A bust can leave a credible
route back while safe play does not guarantee success.

The [analysis record](rules-analysis.md) compares limits 10, 12 and 21, including
the earlier 21/5/90 setting. The recommended 10/5/30 trial keeps the same game
mechanics, makes rounds shorter in expected roll count and favours a welcoming
first experience. Target 32 is a harder comparison for native play if 30 feels
unrewarding; it is not an additional difficulty menu to build now.

The exact ideal-die model in [rules_check.py](rules_check.py) checks risk,
context-dependent decisions and recovery. It cross-checks fixed-policy results
against a separate round-score distribution and convolution. It does not execute
AMOS, measure its random generator or establish fun. Native play must still
judge the numerical balance.

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
sources and explicit edits. The [teaching map](teaching-map.md) proposes smaller
checkpoints and supported investigations. Introduce every required line before
relying on it.

| Stage | Result | Idea to explain locally | Check |
| --- | --- | --- | --- |
| State the challenge | Display an inviting message and the limit; edit the words | Instructions, strings, run and return to editing | Edited output appears; deliberate syntax error can be repaired. |
| Keep the program | Save and reopen the edited source | Filename, storage and source versus output | The fresh session runs the saved edit. |
| Draw the die | Draw an original fixed face, then choose its palette in a separate step | Pixel coordinates, shapes and colour selection | Moving a pip changes the intended shape; text remains legible. |
| Make one roll | Show one die result | Random selection and its exact integer range | Prescribed boundary results are 1 and 6; ordinary runs stay within range without claiming a finite sample proves fairness. |
| Add a roll | Combine a stored total and a new result | Assignment and addition | Explain old total, rolled value and new total separately. |
| Read the limit | Display active, exact-limit and bust results using prescribed examples | Comparisons and decisions | Totals 9, 10 and 11 take their intended paths. |
| Show the face | Make the picture follow the stored roll | Decisions select a visual representation | All six supplied values produce matching pips and numbers; old pips are cleared. |
| Choose another roll | Repeat while the round is active, with a reliable quit | Input and repetition, taught in separate steps | One accepted choice requests one roll; waiting does not change the total. |
| Keep or risk it | Bank ends the round with its score; bust scores zero | A player's decision and distinct displayed total versus awarded points | Bank preserves the shown points; bust can show 11 while awarding zero. |
| Sound the result | Add bank and bust cues after once-only scoring is explained | Sound parameters and event timing, introduced separately | Listen to each cue; waiting, invalid input and held keys do not repeat it. |
| Build a challenge | Retain secured points across rounds, count finished rounds, and show the target | Values with different lifetimes, introduced separately | The current total resets while secured points remain; each result is counted once. |
| Arrange the board | Group current and secured points, remaining opportunities and target | Apply the taught drawing and palette facilities | Labels, picture and values agree after a bank and bust. |
| Finish deliberately | End at the target or when it is unreachable; offer replay and exit | Session conditions, reset and input boundaries, introduced separately | Known success and failure sequences; no extra round, repeated bank or stale replay input. |
| Sound success | Add a distinct session-success cue | Reuse the explained sound facilities at the ending | The success cue occurs once; its relationship to the final bank cue is deliberate. |
| Review and investigate | Check the complete presentation and make a small variation | Drawing and sound express the same rules | Numbers and picture agree, labels remain legible, result cues fire once, and play works muted. |

The first complete single-round game precedes the session challenge. Explain that
the session target adds a reason to balance safety against the points still
needed; a score-maximising single-round example alone has a safe stopping rule.
There is no required fixed lesson count or lesson duration.

Provide prediction, diagnosis and a small independent variation with hints.
For example, explain why changing `>` to `>=` wrongly rejects a perfect 10, or
trace what must reset after banking. A changed limit requires reconsidering the
target and tests; it is not an isolated cosmetic edit.

## Distinctness and finishing

The [opening comparison](../../amos/opening-candidates.md) records the inspected
cross-track material. Spectrum Dice Roller and C64 Tally explore frequencies;
their player chooses a sample or watches accumulation. This game asks the player
to secure points or expose the current total to a growing risk of loss. Sharing
a die and random-number syntax does not repeat that activity. No existing game
is commissioned for a deliberate revisit here.

The user agreed to develop graphics, palette choices and short event sounds
through the opening, rather than collecting them in a final presentation stage.
Use the [teaching map](teaching-map.md) for the smaller steps. Keep numbers and
labels carrying every essential result, and current total, limit and secured
score visually distinct. Leave enough time to read a roll; do not use decoration
or sound as an unexplained timing mechanism. The prepared silent text source
remains the initial rules trial; the planned visual and audible stages require
their own native checks before they become lesson sources.

The prototype acceptance run must cover rolls 1 and 6, totals 9/10/11, banking
exactly once, a bust preserving earlier points, target equality, an unreachable
target, final-round completion, invalid input, held/released input, repeated
rounds, replay, quit and fresh save/reopen. Inspect graphics and listen to cues
if present. Negative controls must reject an equal-limit bust and a bust that
awards its displayed total.

Native play should check whether the accepted design remains readable and
responsive with AMOS input, graphics and sound. Revisit tuning if native play
reveals a concrete problem; additional complexity is not the next goal.
A real beginner should later try the opening without coaching. Until
then, keep design analysis, native correctness, human play and learning evidence
separate. The rest of the AMOS lineup and any language implementation remain
independent decisions.
