# Night Patrol — native prototype

The maintained sample is in
`code-samples/sinclair-zx-spectrum/basic/night-patrol/prototype/`.
The user approved the native corner-scanning version: a 30 × 18 archive,
narrow corridors and hiding recesses, a widening wall-blocked fan, file retrieval
and return to the entrance. The guard looks back and checks the next corridor
at every corner. This is the accepted gameplay endpoint for lesson planning;
the [ten-lesson progression](lesson-brief.md) is agreed and its
[eight checkpoints](lessons.md) are verified. Publication remains separate.

## Corner behaviour

At each corner, the guard stays on its square, looks back along the corridor it
just walked, then faces the next corridor before advancing. Each facing lasts
one guard interval: two player updates. The arrow and fan show the active facing;
the same wall clipping and capture rules apply during scans. The pattern repeats
predictably. There are 52 walking phases and eight stationary scan phases per lap.
The title explicitly warns that the guard looks back at corners.

This makes following directly behind the guard hazardous. The native checker
requires all eight corner-facing changes and a capture caused by a stationary
look-back, as well as a complete successful route.

## Visibility and runtime cost

Amber backgrounds show the exact detection mask. Walls block each sight line;
diagonal rays touching wall corners are blocked. The fan covers adjacent tiles
as it widens, so stepping one square sideways is no longer a general escape.
The narrow circuit makes the player share watched corridors to reach the file.
Recesses provide places to leave the patrol lane and wait.

The prototype uses generated ordinary DATA for this fixed map and patrol. Each
record describes a guard position and the cells entering or leaving sight. BASIC
updates a logical string mask and those screen attributes. Collision reads the
map and mask, never screen colours. No host or machine code runs the game.

The generator is retained beside the sample. Its geometry and DATA are audited
against the maintained map. The agreed progression explains visibility and data preparation with a
small worked mask before supplying the complete table.
The source keeps an eight-frame minimum wait, with the guard moving on alternate
updates. Actual BASIC execution adds time and must be measured in native play.

## Verification

The model finds a safe 78-update round trip with four waits. Its direct shortest
route is caught on move 28. This establishes a timing constraint, not enjoyable
difficulty. A wall blocks sight into the recess at (9,9) when the north-facing
guard is at (7,12).

The sample README contains reproduction commands. Build evidence records source,
tape, stored tokens and emulator identities. The checker uses ordinary keys and
read-only state observation to compare visibility and game transitions with the
coordinate model. It advances against the ROM interrupt counter after debug
stepping because mixing stepping and frame runs did not consistently advance
execution in the recorded binary. Screenshot files are diagnostic evidence and
must be inspected before public use.

`live-frames.png` was captured using ordinary frame advancement and inspected.
The checker’s debug-stepped PNGs can be blank in this emulator binary; they are
not publication assets. `verification/capture.py` reproduces the usable view.

The corner-scan revision passes 18 native execution groups, including all
eight stationary facing changes and capture during a look-back. Generated DATA,
source/token/TAP identity and block checksums pass. Observed non-result update
costs in PAL frames: {'player update': (18, 38), 'walking guard': (54, 85), 'scan': (68, 125)}. These include BASIC work and the minimum wait;
the user has accepted the native play feel. These measurements are not a fixed-rate claim.

Approved source SHA-256: `72d436d316de7f278934846d68bc0c7b2125509c105fc3135a89cbd0ddbd5ae8`.
