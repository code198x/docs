# Meteor Storm — first assembly game brief

**Status:** The user selected Meteor Storm as the first replacement assembly
project. The [implemented prototype](prototype.md) is accepted after native play. Its
[teaching progression](lesson-brief.md) is proposed; checkpoints and lesson prose
are not yet implemented.
**Target:** Stock 48K ZX Spectrum, PAL, Z80 assembly, keyboard, tape loading.
**Role:** First-game trial under the [replacement opening](../../assembly/opening.md).

Apply [the charter](../../../../PROJECT.md) and [game-brief guidance](../../../../specifications/brief.md).

## Experience and scope

Pilot a small ship through a meteor storm to reach clear space. Read the incoming
paths, find a gap and decide when to cross towards it. The destination supplies a
finite goal: survive the passage, rather than collect an arbitrary quota or play
until an inevitable loss.

Use most of the screen for the storm, with a compact timer, speed and score display.
The ship starts near the bottom and initially moves horizontally. Meteors enter
from above at independent X positions and different speeds, so the player dodges
individual trajectories and faster meteors overtake slower ones. The user rejected
uniform rows with gaps as boring. Use a scattered, verified field for the next
trial. The user requested a timed fixed-course run with unlimited boost. Holding Space
doubles forward progress; releasing returns to normal speed. Faster travel
shortens reaction time and increases scoring opportunities. Use the accepted gentle sideways meteor drift and vertical star motion. Screen motion represents travelling through the field, not gravity.

Encounters should have an opening, increasing pressure and a final passage into
clear space. Preserve the accepted duration, speeds, one-life rule and density.
The opening should offer a decision promptly without placing a hazard on the
ship before the player has control. Do not make the whole field a tiny central
play area or rely on a random generator to produce survivable gaps.

The user requested gentle horizontal variation and collectible bonuses after
completing the straight-falling trial first time. Meteors now receive small
left/right/straight drifts, limited to one pixel every four updates after native
feedback. Stars must fall straight down. Add distinct stars worth 10 points, letting players
choose whether a collection is worth leaving a safe position. Stars award 20 points while boosting. Award a larger finish bonus for a faster
successful run. Preserve the time and score at the result, with separate best
successful time and best score across retries. Collecting a star must not damage
the ship.
Shooting, bosses, upgrades, free rotation, thrust physics and elaborate scenery
are outside the initial scope. A driving game is a later possibility, not part
of this first game or a settled next slot.

## Controls and feedback

Controls are O/P for direct left/right steering, Space to start or hold for unlimited boost, R to
retry at a result and Q to return to the title during play. Holding both movement
keys leaves the ship still. There is no inertia in the first trial. Explain the
controls and destination before starting and retain compact movement reminders.

The ship and meteors need distinct silhouettes, with shape carrying information
independently of colour. Create their original pixel artwork alongside the code.
Motion must reveal a meteor's trajectory early enough to react. Show time, speed and score clearly; distinguish impact, destruction and arrival.

One life: the first meteor contact ends the run immediately. This replaces the
initial hull/recovery trial at the user's request. Collecting a star is harmless.
A sound reinforces impact feedback without extending play after destruction.

Finishing the spawn sequence alone does not mean the ship is safe: let the last
hazards pass before arrival. Fatal contact takes precedence over arrival in the
same update. Result screens explain whether the ship escaped or was destroyed;
retry resets the encounter sequence, positions, hull, timers and inputs.

## Learning and representation

Give registers, memory, branches, loops and routines a purpose through input,
position, movement, drawing, contact and a small set of active objects. Explain
the new concept beside the observable change. BASIC and Foundations attendance
are not prerequisites.

Store ship position and meteor position, movement and activity in explicit data.
The image is drawn from that state. Contact uses an explained geometric bound,
not colours or screen pixels. Teach the chosen approximation and ensure fast
meteors cannot skip through the ship between updates. Cosmetic palette changes
must not change the rules.

Begin with one meteor, then add a small fixed-capacity collection for overlapping
trajectories. Teach its layout and iteration rather than importing an engine.
Represent authored encounters as straightforward data once repetition makes the
need clear. Rendering choices should follow the accepted motion: investigate
smooth pixel movement without imposing masking, pre-shifting and buffering all
at once. A plain background is acceptable if objects remain readable and motion
leaves no trails.

Maths supplies position, velocity and contact explanations; The Craft supplies
readability, anticipation and difficulty. Explain immediate essentials locally
and link only to shared material that actually exists.

## Proposed runnable stages

| Stage | Observable result | New idea and change | Check |
|---|---|---|---|
| Ship under control | A learner-drawn ship crosses the playfield | State, input, bounds, drawing and a clock | Held input, both keys, edges and clean redraw |
| One approaching meteor | An impact or safe pass has a visible consequence | Independent movement and geometric contact | Hit, near miss, edge contact and one impact per object |
| Find a passage | Several paths create a choice of gap and crossing time | Active-object collection and authored encounter data | Readable trajectories, reachable gaps and bounded object count |
| Through the storm | An encounter sequence ends in destruction or clear space | Progress, hull, end conditions and event ordering | Successful passage, failure, final hazard clearance and terminal precedence |
| Fly again | Instructions, title, retry and tape recovery | Input transitions, complete reset and packaging | Held start key, repeated attempts, title return and fresh loading |

These are prototype concerns, not a fixed lesson count. Exact teaching stages
and edits follow acceptance of the native game.

## Tools and verification

Maintain sources at `code-samples/sinclair-zx-spectrum/assembly/meteor-storm/`.
Build with Asm198x using explicit `--dialect pasmonext --cpu z80` and a tape output
with loader. State entry address, stack and interrupt assumptions. Use Emu198x's
stock 48K model and record actual tool and ROM identities. Host-side preparation
does not add target hardware. No build or execution result is claimed by this brief.

Check fresh tape loading, steering, meteor lifecycle, contact, scoring, event
exhaustion, arrival, destruction, reset and repeated play. Verify a successful
route through each encounter and through the complete sequence. Inspect captures,
measure update behaviour and listen to sound; then have the user play. Separate
scripted correctness from human judgements of readability, responsiveness and fun.

Reshape the prototype if staying in one lane wins, crossing opportunities are
unreadable, damage feels arbitrary, encounters repeat without developing, or the
rendering machinery dominates the teaching. Improve the central passage before
adding further systems. The selected premise is not a reason to
accept an uninteresting first game.
