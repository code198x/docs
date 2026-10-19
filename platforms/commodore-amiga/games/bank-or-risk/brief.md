# Bank or risk AMOS opening game

**Status: the five-round score chase, personal best, scorecard and one rescue
are approved extensions to the accepted opening game.** The
[prototype record](prototype.md) distinguishes the earlier early-ending
implementation from the extended native teaching route and its evidence.
Build a solo dice game around keeping a total or risking another roll.
It is the first game in the [AMOS course](../../amos/course-brief.md).

## Experience and first scope

Roll one six-sided die to build a round total. Before each further roll, choose
whether to bank that total or risk adding another number. A total above 10
busts: the round contributes zero. Exactly 10 banks automatically. Banking
secures the current total and begins the next round.

The current challenge is **five completed rounds**, limit **10**, with **30**
as the first goal. Continue after reaching 30 or losing the possibility of
reaching it. The final score gives the next attempt something to beat. Keep a
personal best across in-program replays, updated only after all five rounds;
quitting an unfinished challenge does not record its partial score. This record
starts at zero when the program starts and is not written to disk.

Show five awards, the current points at risk, secured score, completed count,
target and best. The current slot is a question mark, future slots are dashes,
and a completed bust is zero. These are different states, even though unplayed
storage entries are initialised to zero.

Give one rescue per challenge. When an available rescue meets a bust, retain
the bust total and ask: U undoes that roll, or B accepts zero and keeps rescue.
Undo restores the pre-roll total and last accepted face, spends the rescue and
leaves the round active. The player can bank or risk another roll. A later bust
with no rescue completes immediately. Q abandons a pending round without award.

This extension replaces the earlier prototype's immediate success/impossibility
endings. Reachability can still inform the message, but all five rounds remain
worth playing for a score. The user approved this after reviewing the game's
limited replay appeal. The earlier browser acceptance establishes the original
scale. The user has since played the native rescue endpoint and reported
that it works well, while requesting brighter colour, more space and an animated
roll. The arcade presentation remains subject to review.

Keep one die and one player. Cards, a dealer, betting money, a computer opponent,
multiple dice, disk records, pointer controls and a campaign remain outside this
scope. A brief explained die reveal, visible once-only award and acknowledgement
of the first target crossing support feedback without adding game rules.
Decisions have no reaction timer. The resemblance to Blackjack/Pontoon is the
bank-or-continue decision near a limit, not its card or dealer rules.

## Rules and state

| Situation | Result |
| --- | --- |
| Start/replay | Secured 0, completed 0, current total 0, empty scorecard, rescue 1. Keep Best on replay. |
| Roll below the limit | Add one value from 1 through 6 and show its face. A held key supplies one roll. |
| New total below 10 | Ask for another fresh roll or bank choice. |
| New total exactly 10 | Secure 10 once and finish the round. Equality is not a bust. |
| Bust with rescue available | Keep total/face visible, offer U/B/Q, and leave score, completed count and scorecard unchanged. |
| U at the rescue question | Restore pre-roll total/face, spend rescue, continue the same round. |
| B at the rescue question | Award zero, complete the round, preserve rescue. Never bank the bust total. |
| Bust with rescue spent | Award zero and complete the round immediately. |
| Bank after a valid roll | Award the total once and complete the round. |
| Complete a round | Add award once, increment completed once, write that scorecard entry once. |
| Reach 30 before round 5 | Acknowledge the first crossing and continue building the score. |
| Target becomes impossible | Explain it without ending the remaining rounds. |
| Complete round 5 | Hold the final result; compare with Best using a strict greater-than test. No sixth round. |
| Invalid input / B before rolling | Keep the appropriate state unchanged. U has no ordinary-play action. |
| Replay | Reset score, card, rescue and per-challenge flags; preserve Best and fresh-key handling. |
| Quit | Return to the editor without banking or recording unfinished work. |

A round award differs from the displayed total. A bust can show 12 while its
award is 0; an undecided rescue question has no completed award yet. The card's
completed entries sum to secured points. The renderer and preview cannot award,
spend rescue, advance the counter or update Best.

## Risk and target checks

The original no-rescue calculations below describe the earlier prototype.
Finishing all five rounds alone does not change whether a given policy reaches
30; the personal-best goal gives later rounds a purpose. Rescue does change
outcome probabilities and needs its own analysis.

The exact [extension model](replay_value_check.py), retained with the
[execution record](../../../../audit/2026-10-amos-bank-or-risk-replay-value/REPORT.md),
compares fixed banking policies, with and without undoing the first bust.
For an ideal independent fair die, banking at 6 reaches 30 in 86.836201% without
rescue and 96.898956% with that rescue policy; mean final score rises from
34.993999 to 36.541691. Banking at 7 with that policy reaches 30 less often
(90.319243%) but gives a higher mean score (38.021534). Target probability and
score chasing are different objectives. These are mathematical policy results,
not AMOS random-generator measurements, human win rates or evidence of fun.

Keep 30 for the welcoming first goal. Best-score play supplies the longer-lived
challenge. Human play should assess whether the rescue feels useful and the
five-round loop invites another attempt before increasing the target.

### Earlier no-rescue analysis

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
or sound as an unexplained timing mechanism. The initial text trial checked
rules; the [drawing audit](../../../../audit/2026-10-amos-bank-or-risk-die/REPORT.md)
checks the fixed/supplied faces and stored-roll picture. The [board audit](../../../../audit/2026-10-amos-bank-or-risk-board/REPORT.md)
checks grouped labels and supplied snapshots. The
[sound record](../../../../audit/2026-10-amos-bank-or-risk-sound/REPORT.md)
checks tone variations and once-only cues with native PCM. Listening acceptance
and remaining teaching checkpoints still need their own evidence.

The prototype acceptance run must cover rolls 1 and 6, totals 9/10/11, banking
exactly once, a bust preserving earlier points, target equality, continuation when the target
is unreachable, all five rounds, scorecard/score agreement, personal-best
higher/lower/tie behaviour, both rescue choices and spent/reset rescue, invalid
and held input, replay, quit and fresh save/reopen. Inspect graphics and listen to cues
if present. Negative controls must reject an equal-limit bust and a bust that
awards its displayed total.

Native play should check whether the accepted design remains readable and
responsive with AMOS input, graphics and sound. Revisit tuning if native play
reveals a concrete problem; additional complexity is not the next goal.
A real beginner should later try the opening without coaching. Until
then, keep design analysis, native correctness, human play and learning evidence
separate. The rest of the AMOS lineup and any language implementation remain
independent decisions.
