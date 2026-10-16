# Blitz course brief

**Status: proposal for discussion.** We want a complete beginner to make and
understand a small Blitz program, including the distinction between editing
source, compiling it and running the resulting program. Experienced readers
should be able to enter later without missing the environment's particular rules.

The proposed switch puzzle remains a candidate for review. Its smallest playable
form must justify the teaching load before we choose it as an opening. Blitz
need not share AMOS's project, pace or lesson count, and neither language is a
compulsory introduction to assembly.

Apply the [charter](../../../PROJECT.md),
[curriculum specification](../../../specifications/curriculum.md) and
[unit guidance](../../../specifications/unit.md). The
[tooling brief](../tooling-feasibility.md) covers the execution options.

## Audience and outcomes

Assume no previous programming course. Explain values, variables, decisions,
repetition, routines and collections when the program needs them. Describe the
knowledge used at later entry points and offer optional Foundations explanations.

By the end of the introduction, readers should be able to edit, compile, run,
stop, save and reopen their source; explain a complete input-to-output action;
predict a short state change; recover from an error; and make a modest extension
with diminishing guidance. A working copied listing is one checkpoint, not the
whole outcome. Parents and teachers need explanations and useful questions, with
no compulsory marks or completion gates.

## Project choices

| Choice | What the learner makes | Why consider it | What could make it unsuitable |
| --- | --- | --- | --- |
| Switch puzzle, candidate | A small board of lit and unlit cells; selecting a cell changes it and its immediate neighbours; the goal is all lights off | A deliberate action produces a traceable state change. It gives arrays and routines a purpose without requiring continuous moving graphics at the outset. | A seemingly small puzzle can become hard to solve, and the board representation may arrive before the reader is ready. |

The puzzle is not selected because Blitz is uniquely suited to puzzles. It is a
candidate way to teach the language before making display machinery compulsory.
The same decision would be revisited if the native prototype is awkward to
build, unsatisfying to play or hard to explain. The
[cross-track comparison](../amos/opening-candidates.md) rejects paddle-and-ball
as a default alternative because Volley and Brick Bash already teach closely
related play. A switch puzzle shares a board representation with other games,
but the neighbour-changing rule must provide a distinct playing experience.
Compare its final scope with the inherited Gridlock puzzle proposal before
approval; its catalogue description alone does not settle that question.

## Proposed opening stages

These are inspectable teaching stages, not executed checkpoints or fixed lesson
boundaries. Explain every required setup line and retain complete source in
code-samples. Split a stage if it contains too much new material.

| Stage | Result and purpose | New idea explained locally | Observable check |
| --- | --- | --- | --- |
| A compiled message | Show a message, edit it and recover from a deliberate compile error | Source, compilation, execution and the named editor controls | The new message appears only after rebuilding; the repaired source runs again. |
| Keep the source | Save, close, reopen and rebuild the changed version | Source versus executable; exact file format and storage | Reopen the actual saved edit and rebuild it rather than rerunning an old executable. |
| One switch | Show an on/off value and let an action change it | Assignment, a decision and repeated interaction, taught in small steps | Predict two activations; distinguish a new action from a held input. |
| Four switches | Show a row of four states and select one | An indexed collection and a counted display loop | Change the first and last item without touching another; explain the index range. |
| A playable row | A selected switch also changes its neighbours; clear the row to finish | Neighbour rules and boundaries | Trace a centre move and an end move. No access falls outside the row. |
| Name the work | Separate changing a switch and drawing its state as the duplicated work becomes visible | Routines and their inputs | Change the display without changing the puzzle rule, then check both. |
| A small board | Extend the row into a provisional 4 by 4 board with labelled positions | Rows, columns and an explicitly taught representation | A move at the right edge cannot wrap into the next row. Check every corner. |
| Make rounds worthwhile | Supply a few deliberate starting boards, a move count, completion feedback and reset | Initial state, turn counting and transitions | One legal activation counts once; reset restores the board and count; completion does not continue accepting puzzle moves. |
| Finish and vary | Provide instructions, replay and exit; let the learner author a starting board | A complete play cycle and a small independent change | Play, finish, restart, reset during play, exit and reopen the source; explain a changed rule or board. |

Prototype the smallest useful output and input route before choosing between
numbered text input and a graphical board. Teach the transition explicitly if
the course starts with text and later gains graphics. Do not put an unexplained
bitmap/slice/double-buffer framework behind the first switch.

For the provisional board, selecting a cell toggles itself and orthogonally
adjacent cells inside the board. Repeating the same move reverses that change.
Construct initial boards by applying recorded legal moves to the all-off board;
the reverse sequence supplies a solution to verify in the implementation.
Choose interesting boards with short solutions through play rather than assuming
that a small board needs few moves. Random boards, search algorithms and timed play are outside the
initial promise. The 4 by 4 size remains subject to the smaller prototype.

## Presentation and participation

Give lit and unlit cells distinct shapes or marks as well as colours. Keep the
selected position and instructions readable. Provide keyboard selection; pointer
control can be added after its coordinate mapping and activation behaviour are
taught. A short move or completion sound should reinforce visible feedback and
occur once per event. Verify sound in the original runtime before specifying its
commands; sound support is not established by the current graphics examples.

Let learners author board layouts and presentation. Before revealing solutions,
ask them to trace a move, diagnose a row-wrap fault and predict a reset. Supply
hints and reasoning for a small new board or rule variation without making
progress depend on solving the puzzle unaided.

## Language version and experienced entry

The existing checked opening uses AmiBlitz 3.13.0b and PED. Original Blitz BASIC
2 and Ted are a distinct compatibility route. We must decide whether the course
targets the original dialect, AmiBlitz, or a specifically tested common surface
before implementing a replacement sequence. Do not mix their editor shortcuts
or assume that successful compilation in one proves equivalence with the other.

Retain a short setup and recovery route for experienced programmers. At project
boundaries, show the starting program, explain language-specific behaviour and
offer a small prediction or change to help readers choose where to enter.
Optional references can cover number types and modes in more depth, but every
type and mode used must be explained at the point of use.

## Existing material and replacement checks

The current [Meet Blitz source](https://github.com/code198x/website/tree/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/commodore-amiga/blitz/meet-blitz)
contains reusable compilation, type, decision, loop and graphics explanations.
Choose their placement from the new program's needs. Scrolling and hardware
sprites can belong to later games without disappearing from the track.

| Current weakness | Required replacement check |
| --- | --- |
| The overview assumes previous programming knowledge | Each essential concept and syntax form is explained locally for a newcomer. |
| Unit 5 combines a large animated pattern, trigonometry and two drawing buffers | The first meaningful interaction can be explained without these prerequisites; add each later only for a demonstrated purpose. |
| Unit 6 onward returns to Ted and right-Amiga+X after the opening teaches PED | Every required instruction agrees with the selected editor and is checked through the learner's route. |
| Unit 9 calls port 1 the joystick but describes `Joyb(0)` as that stick's fire test | Each control names the device, port and actual stop behaviour in the checked configuration. |
| Later lessons make categorical fifty-frames-per-second and language-speed claims | State only measured timing for a named workload and configuration, or explain the mechanism without a performance guarantee. |
| The closer emphasises recognition of familiar lines | Include a trace of one complete move, a repair and an independently authored variation. |

The retained [unit-five execution record](../../../audit/2026-10-amiga-unit-five/REPORT.md)
uses AmiBlitz 3.13.0b, FS-UAE 3.2.35, PAL A1200/68020, 2 MB chip and 8 MB fast
memory, Kickstart and Workbench 3.1. It includes actual compilation and execution
of selected graphics variants. It does not qualify the proposed puzzle, stock
A500 output, another Blitz version or learner understanding.

## First prototype and decision

After agreeing the project and dialect, prototype the single switch and row,
then one small board, completion, reset and exit. Compare the simplest text and
graphical interaction routes for the amount of code and explanation required.
Record native execution, input behaviour, play observations and any supplied
assets separately.

Reconsider the puzzle if the rule needs too much explanation, the intermediate
programs are unrewarding, or the representation change dominates the learning.
Compare another distinct, smaller game if those failures persist. Develop lessons only after
the selected prototype is accepted; preserve current public content until a
checked replacement route exists. An uncoached beginner trial remains necessary
to assess the course's effectiveness when a learner becomes available.
