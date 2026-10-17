# AMOS course brief

**Status: bank-or-risk game direction agreed; course sequence proposed.** We
want a complete beginner to make and understand small games in AMOS, then grow
towards more substantial Amiga games. An experienced programmer should be able
to enter later without missing AMOS-specific explanations.

The opening will build towards a solo dice game: approach a visible limit, bank
what you have or risk another roll, and lose the current unbanked total if you go
over. The [game brief](../games/bank-or-risk/brief.md) proposes the first native
trial's scope and tuning. The [comparison](opening-candidates.md) distinguishes
this activity from the curriculum's existing dice experiments.

Apply the [charter](../../../PROJECT.md),
[curriculum specification](../../../specifications/curriculum.md) and
[unit guidance](../../../specifications/unit.md). The
[tooling brief](../tooling-feasibility.md) identifies the facilities this course
would need. AMOS remains a full language track; assembly is an optional direction.

## Audience and outcomes

Assume the reader can enter text and use a keyboard. Explain the editor,
program, variable, decision, loop and routine where each becomes useful.
Foundations supplies optional depth, not missing prerequisites. Include the
keyboard mapping and exact recovery steps for the named emulator.

By the end of the opening, the reader should be able to:

- Enter, run, stop, edit, save and reopen a small AMOS program.
- Explain how a player's choice changes a stored value and the visible result.
- Predict a short sequence of decisions and repeated turns.
- Repair a small fault using an expected result and a reduced example.
- Make a modest variation with hints available, then explain and check it.

These are authoring outcomes to investigate with learners, not examination gates.
Parents and teachers should have prompts, explanatory answers and a record of
what help was needed. No learner trial is currently available.

## Progression through the full track

The opening should establish confidence through small playable programs and
careful explanations. Subsequent games can combine movement, input, graphics,
sound, collections and routines as each experience needs them. Later projects
can explore richer behaviour, connected worlds, asset workflows, storage,
presentation and measured performance, towards games as substantial as AMOS and
the chosen machine configuration reasonably allow.

This is a direction for growth, not a selected lineup, fixed set of tiers or
requirement to teach every facility before making a game. A small first game
sets the starting teaching load; it does not set the track's eventual ambition.
Choose each next game for the experience and understanding it adds.

Games should be distinct across tracks and systems by default. The
[comparison](opening-candidates.md) rules out a falling-object catcher and
paddle game as default openings because their play overlaps existing material.
A point-and-click adventure introduces too many interacting responsibilities for
the current opening brief. Keep short drawing experiments where they help
explain the actual game.

## First game and teaching progression

The player's central choice should be visible before sophisticated graphics are
needed: keep a useful total or risk losing it for a better result. A short
session target gives that choice a changing purpose. The game brief provisionally
uses one six-sided die, a round limit of 10, five rounds and a 30-point target;
those numbers require native play review.

Start with a small message and save/reopen exercise, then show one roll and add
its result to a stored total. Introduce the limit decision, then input and
repetition, then the ability to bank. A complete single round precedes the
session target. Explain that the target creates a reason to balance safety
against the points still needed; do not pretend that the single-round scoring
example alone demands risky play.

Grow the session in separate stages: retain secured points, count finished
rounds, evaluate the target and reset for replay. Teach the difference between
current total, awarded points and secured score. A bust can show 11 while
awarding zero and preserving earlier points. Finish scoring once before asking
for another input.

The [game brief's stage table](../games/bank-or-risk/brief.md) gives the broad
sequence and checks. The [teaching map](../games/bank-or-risk/teaching-map.md)
splits the busiest stages into proposed checkpoints, with state responsibilities,
entry routes and explanatory answers. Split stages further when their teaching
load warrants it. Keep complete maintained sources in code-samples with exact
add, replace and delete
instructions. Every required line must have been explained before it runs.
There is no fixed lesson count, frame-rate target or need for an unexplained
screen, input or game framework.

## Presentation and participation

Start with readable text and labelled totals. Add original die artwork and short
result cues through separate, explained steps. Labels and numbers must carry all
meaning with sound off and without relying on colour. An input should cause one
action, and a held key must not roll repeatedly or act in a later round.

Let readers choose wording and presentation while explaining which numeric
changes alter the game. Use small prescribed roll sequences to investigate
boundaries before relying on ordinary random play; identify the test setup.
Ask for predictions, action traces and diagnoses before revealing explanations.
A useful fault is treating exactly 10 as a bust. A useful variation changes a
setting and explains how the checks and target must change with it.

The [rules analysis](../games/bank-or-risk/rules-analysis.md) establishes some
mathematical design properties under an ideal die. It neither runs AMOS nor
proves that the game is enjoyable. Keep probability optimisation optional;
reasoning about the possible next roll is enough for the opening.

## Experienced entry

Provide a short environment route covering run, stop, save, reopen and error
recovery. At project boundaries, describe the knowledge used, show a complete
small starting state and offer a prediction or change to help readers choose
where to enter. Answers remain available and do not unlock progression.
Experience in another language does not imply knowledge of AMOS input, screen
or storage behaviour.

## Existing material and replacement checks

The current [Meet AMOS source](https://github.com/code198x/website/tree/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/commodore-amiga/amos/meet-amos)
contains useful explanations of variables, decisions, loops, procedures,
palettes and drawing. Reuse passages where they serve the chosen program; the
existing unit order does not determine the course. Bobs, collision, AMAL and more
substantial sound work can enter later games when needed.

| Current weakness | Required replacement check |
| --- | --- |
| The overview expects earlier programming knowledge | A newcomer can follow every essential explanation locally. |
| Unit 12 promises later edge handling that unit 14 does not supply | Every promised technique has a taught, runnable stage and corresponding checks. |
| Suggested actions can repeat while input or contact remains true | Distinguish one accepted action from held input, including result sounds and replay. |
| Unit 17 treats recognising commands as readiness | Include a complete action trace, a repair and a small variation without a supplied full solution. |
| The dedicated saving lesson arrives at unit 16 | Save and independently reopen an edited program near the start. |

Use the retained [execution record](../../../audit/2026-10-amiga-unit-five/REPORT.md)
for its named configuration only: AMOS Professional 2.00, official source revision
`533b4b1f5acd604814513f78e02c7b4796cb0531`, FS-UAE 3.2.35, PAL A1200/68020,
2 MB chip and 8 MB fast memory, Kickstart and Workbench 3.1. This is a development
baseline, not a minimum requirement or qualification of the proposed game.

## First prototype and review

Use the [game brief](../games/bank-or-risk/brief.md) for native prototype scope,
source location, concrete rules and acceptance cases. Check one roll, limit
boundaries, banking, session score, ending, replay and exit in the named original
runtime. Check the learner's save/reopen route early.

The agreed mechanic gives us a game direction, not acceptance of numerical
balance or a replacement lesson sequence. Play should establish whether the
bank-or-roll choice remains interesting and whether the failure consequence is
fair. The short session must not become a reason to introduce several unexplained
state variables in one step.

If the first trial is unsatisfying, reconsider tuning and the size of its opening
stages before adding features. A later uncoached beginner trial must establish
what readers understand. No later AMOS lineup is selected. Preserve existing
public routes until checked replacements and necessary redirects are ready.
