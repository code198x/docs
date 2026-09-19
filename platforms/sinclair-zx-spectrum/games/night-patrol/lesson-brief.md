# Night Patrol — teaching progression

**Status:** The user agreed the ten-lesson progression and authorised creation
and verification of its eight teaching checkpoints. The prototype endpoint is
approved. All eight checkpoints are implemented, with 96 native execution groups passed;
see [implementation and evidence](lessons.md).
The overview and ten website lessons are now authored for local review. Publication remains separate.

## Endpoint and audience

Build the approved 30 × 18 archive in stock 48K PAL Sinclair BASIC: logical wall
collision, file retrieval and return, a continuously advancing patrol, a widening
wall-blocked sight fan, and stationary look-back and next-corridor scans at each
corner. Keep the accepted controls, difficulty, silence and retry behaviour.

The final checkpoint must be byte-identical to
`code-samples/sinclair-zx-spectrum/basic/night-patrol/prototype/night-patrol.bas`.
The approval hash and current execution evidence are in [the prototype record](prototype.md).
Teaching sources will live beside the prototype under `night-patrol/teaching/`.

Readers use variables, decisions, loops, strings and subroutines, with local
recaps where each becomes useful. Explain numbered lines and RUN at the opening;
link to the existing Spectrum setup and saving guidance. No previous game,
Python knowledge or assembly course is required. This is a game-AI project:
behaviour, perception and readable patterns, with no machine-learning prerequisite.

## Runnable sequence

| Lesson | Checkpoint | Result | New idea and observable check |
|---|---|---|---|
| Draw the archive | archive | The full map, entrance and file appear | DATA/READ/RESTORE, a two-dimensional string array, row/column coordinates and character graphics. Create and explain the glyph bytes and map rows. Count 30 columns and 18 rows; locate the entrance and file. Explain the normal STOP report. |
| Walk the corridors | movement | I/J/K/L move the player; walls stop movement | INKEY$, direction offsets, proposed versus accepted position, restoring the old square and a release gate for held R. The map owns collision. Check all four directions, held keys, uppercase input and blocked moves. |
| Take the file home | mission | An unguarded retrieval game with win, retry and quit | A carried-file flag, objective order and result state; reuse the release gate before a fresh result-menu press. Returning empty-handed does not win; retry restores the file. This is explicitly an intermediate game without danger. |
| Keep a patrol moving | patrol | One guard walks the circuit independently of player input; contact is dangerous | Direction vectors, corner coordinates, a player-update counter and a minimum clock wait. Explain the ROM frame-counter byte and wrap. Stand still to watch a complete lap; check guard contact and frozen endings. Sight is not implemented yet. |
| Look around at corners | scans | The guard stops, looks back, checks the next corridor, then moves | Behaviour phases as records of position and facing. Repeated positions with different facings represent scans. Convert the walking rule to a phase table explicitly. Trace all eight stationary changes and the loop from phase 60 to phase 1. |
| Mark what can be seen | sight | A stationary guard has the opening fan; entering it causes capture | Temporarily hold the guard at its opening position to isolate perception. Teach fan shape, wall clipping, a logical visibility string and its screen display. Construct the small opening mask from coordinates; check a visible side cell and a blocked cell. The stationary guard is a labelled diagnostic stage. |
| Prepare the sight changes | reuse sight; inspectable data exercise | Two consecutive masks become a small, explained change record | Work out cells entering, leaving and remaining visible. Read one real record, then inspect the supplied complete table and its generator. Explain preparation on the development host versus execution on the Spectrum. This lesson produces data understanding, not another game checkpoint. |
| Move the field of view | stealth | The patrol and corner scans run with the fan and both detection checks | Apply prepared changes to the mask and attributes, restore entity graphics, then check new sight. Explain why the player's move is checked against current sight before the guard advances. Complete the retrieval and demonstrate capture by a stationary look-back. |
| Finish Night Patrol | finished | The complete approved program, including title, legend and reliable input/retry | Explain remaining integration changes: key buffering, reset of phase and visibility, once-only map preparation, result controls and saving entry point. Check every path through title, play, capture, win, retry and quit. This fulfils the finished-game promise. |
| Keep Night Patrol | reuse finished | A saved tape loads and starts in a fresh emulator | SAVE with LINE 10, tape export and recovery. Reopen, play, retry and quit. Explain that saving the program does not preserve an active attempt after auto-start resets the game. |

The eight checkpoints are archive, movement, mission, patrol, scans,
sight, stealth and finished. Lessons 7 and 10 reuse a program already built.
The count follows distinct teaching jobs: perception and preparing its changes
need space of their own. Do not squeeze either into unexplained supplied code.

## Teach the prepared data, not a hidden engine

The host prepares a fixed patrol's visibility; the Spectrum runs the game.
Provide the complete DATA table as a separately identified, inspectable source
include. Explain its schema before inserting it. The learner derives a small
example by hand; they need not manually calculate every cell of every phase.
The optional generator reproduces the larger table without adding a Python
runtime dependency to the game.

Teach the geometry locally in lesson 6, using a diagram and short pseudocode.
For each facing, consider five successive forward distances. Their candidate
widths are 1, 3, 5, 7 and 9 cells. For a target at distance `depth` and side offset
`offset`, inspect successive forward positions, rounding the interpolated side
offset with `floor(offset * distance / depth + 0.5)`. Any wall blocks that target.
When a sample steps diagonally, either adjacent wall blocks the corner too.
This is the game's discrete sight rule, not a claim about physically exact vision.

Work through the actual opening guard at (7,5), facing east. Its visible cells
include (9,4) and (9,6), so the fan extends beyond the centre line. The square
(13,5) is beyond its five-cell range. A separate cover example uses the guard
at (7,12), facing north: (9,9) is within the candidate cone but walls block it.
Distinguish a cell outside the cone from a candidate rejected by a wall.

The display has a 32-column stride even though the map is 30 columns wide.
A visibility cell is `32 * row + column`; for (9,5), it is 169. The 608-character
mask reserves room for all indexed map positions, including unused margin slots.
A space means unseen and `!` means visible. The game reads this logical string
for detection. Recover a row with `INT(cell / 32)` and the column with
`cell - 32 * row`. The stationary checkpoint can display its cells with PRINT
and PAPER; direct attribute updates arrive with the moving fan in lesson 8.
POKE displays the mask’s result; it never reads an attribute to decide
whether the player has been seen.

Lesson 7 should decode the actual first movement record:

```text
8210 DATA 8,5,1,10,5,-168,-137,-201,141,173
```

The guard is at (8,5), facing east. Ten cells are visible after the change;
five cells change. Remove (8,5), (9,4) and (9,6), then add (13,4) and (13,5).
The other visible cells remain. The visible total and change count answer
different questions. Negative values mean removal, not negative map positions;
ABS recovers the cell index. Explain READ's advancing position and why the next
phase explicitly RESTOREs its own record.

The initial mask is a full addition record at line 8900. Runtime phases 1–60
use `8200 + 10 * phase`. Phase 60 finishes at the opening position and facing;
the next phase is 1. Line 8200 is the zero-change phase-zero record, while startup
uses the full initial mask. Explain the zero-change guard before FOR/NEXT as an explicit no-work return. Sinclair BASIC skips an empty FOR range;
do not claim otherwise.

For display, derive the attribute address from the screen row offset:
`22528 + 32 * (row + 1) + column`, hence `22560 + cell`. Explain INK, PAPER and
BRIGHT bit values before the POKE expression. Walk through the ordinary floor
value 71 and lit value 119, and the file/entrance colour exceptions. Introduce
CHR$, CODE/USR and the relevant memory addresses where used, with checked manual
references during authoring. The prepared cells contain visibility decisions;
they are not executable machine code.

Treat map, patrol and visibility data as a matched set. Changing a wall, route
or fan requires regenerating and validating the sight table. A coordinate edit
alone is not a valid optional experiment once prepared visibility is in use.
Offer a small paper-data exercise to everyone and a documented generator workflow
as an optional extension for readers who want custom levels.

## Editing, pacing and explanations

The opening checkpoint is a new program. Show its complete listing without an
instruction to add every numbered line. Later stages need maintained exact
add/replace/delete instructions and full runnable source. Mark the temporary
stationary guard explicitly and show how movement returns in lesson 8.

Teach the working game loop before its hardware details: read input, propose a
move, reject a wall, check current danger, update the objective, advance a guard
phase when due, check new danger, draw and wait. The accepted implementation's
precise statement order must govern the finished explanation. Returning safely
with the file ends play before another guard phase.

Keep the clear relationship between map state, visibility state and drawing.
Explain the cost of repeated work using the measured prototype experience and
small traces. Do not add a deliberately slow, full-map redraw checkpoint merely
to create an optimisation story. Eight PAL frames are a minimum wait after work,
not a promised update frequency; scans and walking can take different times.

The final source retains direction-array setup and an unused fifth glyph from
earlier prototype work. Direction arrays have a role in the early walking
checkpoint; do not invent a role for them or the unused glyph in the finished
phase-table game, or silently change the accepted source to tidy them away.

Select prediction and tracing questions where they clarify a distinction: why
colour changes do not move a wall; why a stationary guard can catch someone;
why visible count differs from changed count; why a mask must reset on retry;
and why looking back creates risk for a player following behind. Supply reasoned
answers without turning them into compulsory assessments.

## Verification and authoring boundary

The approved prototype has 18 native execution groups. They verify the endpoint,
not the intermediate sources by themselves. During implementation, enter and save
all eight checkpoints through ROM keys and load each fresh. Reconstruct their
editing transitions and require final source identity with the approval hash.
Run the complete prototype suite against the independently built finished tape.

Check map boundaries, movement and held/unusual keys, empty-handed return, pickup,
reset, independent patrol movement, all eight scans, mask correctness for every
map cell, wall and corner occlusion, entering sight, moving sight, stationary
scan capture, both endings and fresh-tape recovery. For preparation, compare the
full masks and accumulated changes over multiple laps, including phase wrap and
zero-change records. Inspect timing in native play and capture media through the
verified frame-based path; blank debug-stepped PNGs are not lesson illustrations.

Before website authoring, verify primary Spectrum manual passages for string
arrays/slices, DATA/READ/RESTORE, graphics, attributes, keyboard buffering and
system variables. Link only to existing shared explanations after reading them;
local instructions must remain sufficient. Check catalogue grouping and the
retained Night Patrol numeric identity against current site data. No new family,
assembly revisit, extra guard, random patrol or multi-floor campaign is implied.

The checkpoints and lesson pages are implemented. Review the local overview and
ten lessons before publication; the approved gameplay source remains unchanged.
