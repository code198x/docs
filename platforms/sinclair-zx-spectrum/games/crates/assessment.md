# Crates — source assessment

The user selected Crates after Sonar and asked to reconsider its former role at the end of BASIC. The [replacement brief](brief.md) proposes a smaller immediate teaching role: changing a grid safely. Selecting Crates does not by itself approve every proposed feature or a replacement lesson count.

## What exists

The website has an overview and six authored lessons under `src/content/curriculum/sinclair-zx-spectrum/basic/crates/`, with matching availability metadata under `src/content/units/sinclair-zx-spectrum/basic/crates.yaml`. The samples have six BASIC checkpoints ending at `sinclair-zx-spectrum/basic/crates/unit-06/crates.bas`. This is a source and prose review; the existing game was not executed during this assessment.

The retained brief and actual implementation differ materially:

| Subject | Retained material | What the source establishes | Replacement implication |
|---|---|---|---|
| Position | Overview and final lesson frame Crates as the end of Volume 2; user recalls it as the BASIC finale | No code depends on being a finale | Place it after Sonar without promising that it closes BASIC or opens a fixed Volume 3 |
| Scale | Brief specifies 12 topics, 5–8 levels and an approximate 60-line cap | Six source checkpoints; final source contains three DATA maps, one 5×5 and two 6×6 | Derive the lesson count from verified teaching states; start with one complete room |
| Collision | Brief promotes ATTR and colour as cell identity; overview caption also calls the screen the state | Final source reads and writes `g(r,c)` with floor/wall/target/crate/combined codes; player coordinates are separate | Keep the array model and correct the prose; do not introduce screen scraping as a required upgrade |
| Input | Lesson 2 calls INKEY$ the course's first real-time input and presents release-waiting as universally applicable | Final source waits for key release then a new key; earlier current-route games already poll keys | Teach deliberate single steps as a puzzle-specific policy; recall polling locally |
| Targets | A separate `ps` flag records the floor beneath the player for drawing | Underlying floor/target already remains in the grid | Trial drawing the underlying cell from the grid to avoid duplicated display state |
| Completion | Final source scans for cell code 2, advances rooms and repeats after the sentinel | Assumes valid maps and matching crate/target totals; ordinary completion uses PAUSE and any key | Validate map invariants and require deliberate continuation; verify held-key transitions |
| Recovery | Brief bans undo; restart appears late in the planned sequence | Final source has R restart, but no explicit Q exit | Put restart and exit into the first complete room; decide undo from play evidence |
| Counting | Brief discusses pushes, optimal play and par | Final source increments `moves` on walking and pushing | Name successful player steps accurately; no unsupported optimality claim or required par |
| Boundaries | Lesson 3 suggests an array lookup replaces edge checks | Destination and beyond-crate reads rely on surrounding walls | Check bounds before indexing, including learner-edited malformed maps |

Useful donor material includes the five cell codes, the separation of player position from the grid, text-map loading, the two-cell push check and restoring a target after moving a crate off it. These are implementation precedents to inspect, not proof that the current program, controls or puzzles satisfy the new brief.

## Teaching corrections to carry forward

Sonar records revealed knowledge; it does not scan a hidden world array for the nearest target. The replacement Crates explanation must connect to the actual published Sonar rather than its earlier multi-target design. DATA and string slicing need local explanations instead of attendance assumptions about Cipher or Three in a Row.

A single room with an ending and recovery can be a complete game. Remove the old claim that one solved room is only a demo. Likewise, a corner target may be a correct final position for a crate: explain non-target corner traps without claiming that every corner crate is a failure or that avoiding corners proves solvability.

Neither the existing three maps nor a proposed new set has been accepted as the new puzzle sequence. Preserve the old sources and public URLs while the replacement prototype is investigated. No replacement lessons were drafted or published in this assessment.
