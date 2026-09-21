# Meteor Storm — teaching progression

**Status:** The user accepted the native game: “Sorted. Perfect. Let's proceed
with this.” The user also agreed the separate introductory/game split. The eight introductory
and fourteen game lessons remain provisional boundaries; checkpoints and lessons
are not yet implemented.

Apply the [opening design](../../assembly/opening.md), [game brief](brief.md),
[unit specification](../../../../specifications/unit.md) and [execution record](prototype.md).
The endpoint lives in `code-samples/sinclair-zx-spectrum/assembly/meteor-storm/prototype/`.

## What makes this a module

**A game is changing state, observed through a picture, at a measured rate.**
Meteor Storm makes that distinction useful: input changes the ship, objects move
independently, geometry decides contact, and boost changes progress through a
course without changing what a second means. The score gives a reason to choose
risk; records give a reason to replay.

Meteor Storm follows the separate [Meet Assembly module](../../assembly/meet-assembly.md).
That introduction owns the first build, bytes and memory, simple drawing, flags,
loops, calls and stack, keyboard input, bounded marker movement, clock awareness
and the first debugger exercise. The game applies and deepens those ideas.

The fourteen game lessons below propose thirteen new runnable checkpoints; the
final reload lesson reuses the finished source. These boundaries remain provisional.
No BASIC or Foundations attendance is required. Readers arrive from the introductory
module or with equivalent experience; recap immediate concepts locally.

Start a fresh Meteor Storm project with complete source for the small drawing/input
basis, explicitly linked to the introductory experiments. No unexplained engine or
prior game binary is inherited. A controllable ship develops into a one-meteor
dodge before pools, scores and records.

## Proposed sequence

| Lesson | Runnable result | Main explanation and evidence |
|---|---|---|
| 1. Move between columns | Accepted ship artwork and smooth movement with clean erasure (`pixel-motion`) | Recap the introductory marker and its routine contracts, then add bit offsets and shifted sprite data; XOR on the chosen plain background. Expand to the accepted original artwork. Construct a shift by hand before explaining host-generated tables, stride and row count. Show the method's overlap limitations. |
| 2. Give movement a clock | Input and movement update on a frame clock (`clocked-steering`) | Deepen the introductory clock experiment: private IM2 setup, a small handler, register preservation, EI/DI, HALT, vector setup and a frame counter. Establish startup/stack assumptions explicitly. Explain the 25 Hz update choice and byte wrap; do not equate a delay loop with elapsed time. |
| 3. Something is coming | One meteor approaches at its own speed (`one-meteor`) | Independent X/Y and velocity; erase, update, draw and retire. Ship movement does not move the meteor. Predict arrival from distance and speed. |
| 4. Hit or near miss | First meteor contact ends the attempt (`first-dodge`) | Explicit inset rectangles, comparisons and event ordering. Use stored geometry, never pixel colour. Give impact a brief audible and visible consequence. Check edge contact and near misses; use the familiar debugger to trace a collision decision. |
| 5. More than one | Several independent meteors (`object-pool`) | Fixed-size records, offsets, index registers, iteration, active/free slots and capacity. Draw the memory layout and trace two different objects. No generic entity system. |
| 6. A storm with an end | A reproducible scattered course reaches clear space (`fixed-course`) | Event data, spawn intervals, varied positions/speeds and event exhaustion. Explain host-prepared random-looking data versus runtime randomness. Wait for the last object to leave; a depleted event table is not yet a win. |
| 7. Read the drift | Gentle sideways meteor motion (`drift`) | Signed byte offsets, a slower horizontal cadence, bounds and reflection. Trace leftward addition and an edge reversal. Preserve the accepted one-pixel-per-four-course-steps drift. |
| 8. Leave the safe path | Vertical stars award points (`stars`) | Object kind selects drawing and contact behaviour. Stars retire once, award points once and never damage the ship. Explain score units and decimal display; distinguish simulation data from display text. |
| 9. Race the clock | A normal-speed run has a measured finish time (`timed-course`) | Separate frame time, simulation steps and course progress. Use a multi-byte counter, carry and integer conversion to seconds/hundredths. The display is a representation of the clock, not the clock itself. |
| 10. Hold on to boost | Hold Space for unlimited 2X travel and doubled star value (`boost`) | Two simulation steps per update, continuous held input, release behaviour and speed-dependent scoring. Check collision at both steps and make completion/fatal-contact precedence explicit. |
| 11. Keep up with the machine | Boost retains its cadence in a dense field (`render-budget`) | Measure work against the frame budget. Keep previous image positions so both physics steps run but each meteor is redrawn once. Explain why reducing drawing work must preserve collision checks and gameplay. |
| 12. Beat your record | Finish bonus plus separate best time and score (`records`) | Comparisons, sentinels, persistent versus per-run state, and integer bonus arithmetic. Failed runs cannot set a best time; retries preserve records. Explain that session records are not disk persistence. |
| 13. Make the game explain itself | Accepted title, HUD, result, retry and quit (`finished`) | Explicit phases, input release and complete reset. Centre text from its actual length and enforce screen bounds. Keep final values, controls, artwork, one-life rule and scoring identical to the accepted game. |
| 14. Keep and share the game | Fresh tape load of the same `finished` source | Assemble the distribution tape and reload on a fresh 48K machine. Distinguish tape loading from a debugging snapshot. Play, finish or fail, retry and return to title. |

Title/retry polish waits until the central game works, but instructions, visible
consequences and a way to repeat each experiment do not. Every checkpoint states
its controls and recovery path. Full source accompanies precise editing actions;
optional diffs never carry the essential instructions.

## Complexity to handle deliberately

The prototype is evidence that the game works, not a lesson order. Its early
IM2 setup, pre-shifted graphics, indexed pool and text formatting would overwhelm
a beginner if presented as one starter listing. Develop each helper in a small
visible experiment, explain its contract and retain a route back to its source.
Do not hide essential work behind “paste this engine”.

The introductory module uses an eight-row shape and character-aligned movement.
The game expands that explained basis into the accepted ship and meteor artwork. Fixed arrays and course tables have concrete sizes
and meanings. Show at least one hand-worked sprite shift and event record before
using host generation. The host makes data; it does not make the target machine
more capable.

The clock lesson may need splitting if vector setup and interrupt handling
crowd out understanding. The same applies to smooth drawing and the measured
boost optimisation. Split for a coherent explanation, not an instruction quota.
A small supplied routine is acceptable only with an explained dependency and a
clear point where its implementation is taught.

Registers/flags, memory, bit operations, signed arithmetic, indexed data, stack,
interrupts and timing all earn a place here. Matrix algebra, general physics,
AI, scrolling scenery, bank switching, disk saves and an exhaustive instruction
survey do not. BASIC-to-assembly performance comparisons remain a later return.

## Checkpoint and endpoint obligations

Before writing the full lesson prose, build and execute the proposed checkpoints
in the sample repository. Record source transitions and observable outcomes.
Use a complete program for each stage, with targeted experiments that test a
claim rather than merely repeating its implementation.

Preserve the accepted endpoint as the behavioural reference. The prototype has
residual recovery state from an earlier multi-hit version and code arranged for
iteration; do not teach obsolete machinery as if the one-life game needs it.
Any cleanup for the teaching endpoint must be explicit and execution-checked
against the accepted movement, contacts, scores, timing, input and records.
Retain the accepted source and its hashes so the comparison remains inspectable.
Do not claim source identity if the teaching implementation is refactored.

In addition to stage-specific checks, verify normal and full-boost passage,
boost release, first-hit loss, star scoring, gentle drift, vertical stars,
frame cadence, score/time records, retry reset, title bounds and fresh tape
loading. Independently derive worked arithmetic and trace answers. Cite primary
hardware/instruction sources when authoring; emulator observations establish
this program's behaviour, not the whole hardware specification. Listen to any
published sound capture before claiming its audio has been reviewed.

Next work: implement the separate introductory experiments first, then the
Meteor Storm handoff, smooth ship movement and one-meteor dodge. This brief does not
authorise publication or retire existing URLs by itself.
