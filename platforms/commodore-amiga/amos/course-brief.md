# AMOS course brief

**Status: proposal for discussion.** We want a complete beginner to make
something personal in AMOS, understand how it works, and become able to change
it with less guidance. An experienced programmer should be able to enter later
without missing the AMOS-specific explanations.

The recommended opening is a small drawing toy, developed through short
creations. A collecting game is an alternative worth comparing before choosing
the project. Neither choice requires Blitz to follow the same sequence.

Apply the [charter](../../../PROJECT.md),
[curriculum specification](../../../specifications/curriculum.md) and
[unit guidance](../../../specifications/unit.md). The
[tooling brief](../tooling-feasibility.md) identifies the facilities this course
would need. AMOS remains a full language track; assembly is an optional direction.

## Audience and outcomes

Assume the reader can enter text and use a keyboard and pointer. Explain the
editor, program, variable, decision, loop and routine where each becomes useful.
Foundations supplies optional depth, not missing prerequisites. Include a
keyboard mapping and exact recovery steps for the named emulator.

By the end of the introduction, the reader should be able to:

- Enter, run, stop, edit, save and reopen a small AMOS program.
- Explain how input changes stored state and how that state affects the picture.
- Predict a short sequence of decisions or repeated actions.
- Find and repair a small fault using an expected result and a reduced example.
- Add a modest feature with hints available, then explain and check the change.

These are authoring outcomes to investigate with learners, not examination gates.
Parents and teachers should have prompts, explanatory answers and a record of
what help was needed. No learner trial is currently available.

## Project choices

| Choice | What the learner makes | Why consider it | What could make it unsuitable |
| --- | --- | --- | --- |
| Drawing toy, recommended for the first prototype | A canvas where a held button draws, with a small choice of brush sizes, clear and exit controls | The learner authors the picture. Coordinates, input and repetition visibly affect something they care about. | Pointer mapping, canvas boundaries or brush controls could demand too much machinery before the first useful result. |
| Collecting game | A controllable object collects a target, receives feedback and starts another round | Movement, collision, score and sound have a shared purpose. | It needs more interacting state and rules before it feels complete. A generic demonstration may offer too little creative choice. |

The drawing toy is a creative program, not a promised finished game. Later game
projects should meet the charter's finishing standard. A drawing toy earns its
place only if it prepares the learner to build and reason about those projects.

## Proposed opening stages

These are teaching stages to split into lessons as necessary. They are not
executed programs or a fixed lesson count. Each stage needs complete maintained
source in code-samples and explicit editing instructions.

| Stage | Result and purpose | New idea explained locally | Observable check |
| --- | --- | --- | --- |
| First marks | Run a tiny program that draws a recognisable arrangement; change it into a picture of your own | Instructions, execution order and the exact editor controls | Change one mark, rerun and distinguish the new source from the earlier result. |
| Keep your work | Save the program, leave the editing session and reopen it | Source files, filenames and storage versus the temporary running picture | Reopen and rerun the edited version; recover from a deliberately wrong filename without overwriting the good file. |
| Place and repeat | Position marks with named values, then repeat a pattern | Coordinates, assignment and counted repetition, taught in separate steps | Predict which mark changes after changing one value; trace the counter for three passes. |
| Follow the pointer | Show a position marker and provide a reliable way to stop | Reading input repeatedly, a continuing loop and exit | Move, stop and leave the program through the documented control; explain why a stationary pointer does not stop execution. |
| Draw deliberately | Draw while the button is held, inside a visible canvas | Conditions, held input and boundary checks | Hold, release, cross each edge and re-enter. No marks should appear in the controls area. |
| Choose a brush | Offer two brush sizes and a clear action with visible feedback | Brush state; one activation versus repeated held input | Hold the selection control: it must not cycle uncontrollably. Clearing preserves the selected brush and usable controls. |
| Make a named job | Extract a repeated drawing or controls task when duplication becomes inconvenient | Define, call and return from a routine; parameters only if the task needs them | Change the shared routine once and predict all affected output. |
| Finish and extend | Provide readable instructions, new-canvas and exit actions; add one personally chosen variation | Initialisation, reset and a small integration task | Draw, change brush, clear, draw again, exit and reopen the saved source. Explain which state each action changes. |

Keep the first visual setup small and explain every required line. Do not carry
an unexplained screen, palette, mouse or event framework into the opening.
Start with a small useful version; teach restructuring when its purpose is visible.

The proposed endpoint is two brush sizes, one bounded canvas, clear, instructions
and exit. Picture export and reopening artwork need a separate verified format
and workflow; saving the program does not preserve a picture drawn during use.
An animated scene is a possible later creation, not another requirement hidden
inside this introduction.

## Presentation and participation

Let readers choose mark shapes, layout and a small palette while keeping controls
readable. Label controls and selected state so colour is not the only cue. The
initial drawing activity can be quiet; if an action gains sound, explain its
purpose, avoid retriggering it on every update and retain visible feedback.

Provide a checked keyboard alternative for essential actions and investigate a
keyboard-operated drawing mode. Its usability and lesson cost belong in the
prototype review. Do not imply that a pointer-based program is accessible to
every reader because the surrounding page supports a keyboard.

At meaningful milestones, ask for a prediction, a small diagnosis and an
independent variation with graduated hints. For example, add a third brush size
after recalling the two existing choices. Judge the explanation and boundary
checks as well as the visible result.

## Experienced entry

Keep a short environment route covering run, stop, save, reopen and error
recovery. At each project boundary, describe the knowledge used, show a complete
small starting state and offer a prediction or modification to help readers
choose their entry. Answers remain available and do not unlock progression.
Experience in another language does not imply knowledge of AMOS input, screen
or storage behaviour.

## Existing material and replacement checks

The current [Meet AMOS source](https://github.com/code198x/website/tree/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/commodore-amiga/amos/meet-amos)
contains useful explanations of variables, decisions, loops, procedures,
palettes and drawing. Reuse passages where they fit the new program; do not
retain the unit order as a requirement. Bobs, collision, AMAL and sound can enter
later projects when needed.

Before replacing the route, check these weaknesses against the new sequence:

| Current weakness | Required replacement check |
| --- | --- |
| The overview expects earlier programming knowledge | A newcomer can follow every essential explanation locally. |
| Unit 12 promises later edge handling that unit 14 does not supply | Every promised boundary technique has a taught, runnable stage and edge checks. |
| Some suggested actions can repeat while input or contact remains true | Check held, released and newly activated input separately wherever the action requires it. |
| Unit 17 treats recognition of familiar commands as readiness | Include a complete action trace, a repair and a small variation without a supplied full solution. |
| The dedicated saving lesson arrives at unit 16 | Save and independently reopen an edited program near the start. |

Use the retained [execution record](../../../audit/2026-10-amiga-unit-five/REPORT.md)
for its named configuration only: AMOS Professional 2.00, official source revision
`533b4b1f5acd604814513f78e02c7b4796cb0531`, FS-UAE 3.2.35, PAL A1200/68020,
2 MB chip and 8 MB fast memory, Kickstart and Workbench 3.1. This is a development
baseline, not a minimum requirement or qualification of the proposed toy.

## First prototype and decision

After project agreement, prototype first marks, save/reopen, pointer drawing,
bounded canvas, one brush change, clear and exit in the named original runtime.
Record the amount of unexplained machinery each stage would otherwise need.
Observe input and reset behaviour across time; inspect the actual picture.

Reconsider this recommendation if the input or setup burden dominates the
activity, if the intermediate programs are not enjoyable to change, or if learner
observation shows that the relationship between input, state and output remains
unclear. Compare the collecting-game alternative before committing to a full
replacement sequence. Preserve existing public routes until checked replacements
and any necessary redirects are ready.
