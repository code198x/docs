# Night Patrol — BASIC prototype brief

**Status:** The user selected the stealth interpretation, resolving the older
missile-defence catalogue description, and requested larger maps. The native
prototype is approved, including the 30 × 18 corridor map, widening sight fan
and stationary corner scans. Preserve this gameplay endpoint when planning
lessons. The user agreed the [ten-lesson progression](lesson-brief.md); its
[eight checkpoints](lessons.md) are implemented with 96 native check groups passed.
The user-approved overview and ten lessons are published in Hidden worlds;
[publication evidence](lessons.md#publication) records release and live checks.

## Experience and first scope

Steal a file from an archive, then return to its entrance without being seen.
One guard walks a fixed rectangular patrol. At each corner it stays in place
for two scan phases: look back along the previous corridor, then face the next
corridor. It moves on at the following guard update. Walking faces its direction
of travel; scanning uses the same visible fan and detection rules.
An amber fan shows the guard's sight up to five cells ahead, widening with
distance. Walls clip the fan, including diagonals touching wall corners. Both moving
into the existing fan and being reached by its next position cause capture.
Walking onto the guard also causes capture. The guard keeps moving while the
player stands still.

The first map is 30 columns by 18 rows, using columns 1–30 and screen rows 2–19.
It has a narrow patrol circuit, wider corners and wall-screened recesses.
The file and entrance branch from that circuit; there is no open-room bypass. The file starts at (27,3), the
entrance at (3,16), and the guard at (7,5), facing east. All coordinates here are
one-based map positions. The patrol runs through (24,5), (24,14), (7,14), then
back to (7,5). The whole playable map remains visible.

I/J/K/L move up/left/down/right; held keys repeat. R restores the complete trial,
and Q quits. A fresh press is required after an ending. There is no lives tax,
score, time limit, random placement or multi-floor commitment. Immediate retry
supports learning the patrol. Completion means returning with the file; reaching
the entrance without it does not win.

## Rules and presentation

The map array owns wall collision and fan blocking. Neither colour nor rendered
screen characters are consulted for game rules. Walls are stored as a glyph
code in that array after loading, but they remain logical map data. A separate
string mask records current visibility. Screen attributes display the mask but
are never read for collision or detection. The prototype prepares wall-clipped
visibility changes as ordinary DATA for each fixed patrol position. During play,
BASIC updates only cells entering or leaving sight. This avoids tracing and
redrawing an entire fan every step; the geometry generator is retained alongside
the source and audited against the maintained map. The agreed progression teaches this preparation through a small hand-worked
example before introducing the complete supplied table.

The player moves before the guard advances. Check the existing fan and guard
contact before taking the file or recognising an exit. Then advance the guard
on every second update and check its new fan. Returning safely with the file
ends the trial before another guard movement. Corner scans occur after arrival. Each scan facing lasts one guard interval
(two player updates), giving the player time to react to the visible change.

Use a dark floor, bright blue brick walls, a white player, cyan file, green exit
and amber guard/fan. Distinct glyphs and direction arrows supplement colour.
The title explains the symbols and controls; the top message states whether to
find the file or return. Character graphics are authored byte rows in DATA.
The trial is deliberately silent.

## Target and timing

Stock 48K PAL ZX Spectrum, Sinclair BASIC, keyboard and tape, using the native
family emulator with a configured ROM. Enter through ROM keyword keys and save
an auto-starting tape. The host is a development tool, not a runtime dependency.

Wait at least eight PAL frames between completed updates. Printing and BASIC
interpretation add time, so this is not a promised fixed movement frequency.
Only changed entity/fan cells are redrawn during play. The guard advances on
alternate updates, letting the player move faster; map coverage and actual
control response must be judged in native play before increasing complexity.

## Verification and review

Check map dimensions, closed edges, floor connectivity, a safe opening and a
complete reachable round trip. An independent host model can search timed routes,
but the maintained BASIC must execute them through ordinary keys. Observe memory
without writing it; do not fake a winning state for the play review.

Check wall rejection, current-fan contact, guard movement without input, all
four turns, wall occlusion, moving-fan capture, file pickup, return, result
freeze, complete reset, ignored keys, uppercase movement and quit. Compare the
native visibility mask and state transitions with the coordinate model. Record
source, tape and emulator identities, captures and measured update costs.

The trial earns further work if cover and timing create readable choices on the
larger map. A safe host route does not establish enjoyable play. If crossing
feels trivial, improve the route or cover arrangement before adding guards;
if redraws make movement hard to control, measure the cost before shrinking the
map. No assembly port or artificial BASIC failure target is implied.
