# Drift — prototype brief

**Status:** The user agreed to try a bounded stock BASIC prototype after Brick Bash, noting that it might be challenging in BASIC. The user subsequently docked successfully but found speed hard to read. The revised speed/direction readout and docking cue were accepted after further successful docking. The user agreed to develop the [teaching progression](lesson-brief.md); [six executed checkpoints](lessons.md) now support eight lessons, authored with their overview for local review.
**Target:** Stock 48K PAL ZX Spectrum, Sinclair BASIC, keyboard, ROM tape loading. No machine-code helper or runtime extension.
**Sources:** `code-samples/sinclair-zx-spectrum/basic/drift/prototype/`. The inherited catalogue proposal supplies a name and rotation/inertia theme, not an agreed full design.

## Experience

Turn a small ship, apply short burns, coast and thrust against its motion to brake. Enter a marked docking box almost stopped. There is no automatic drag: pointing somewhere does not change existing velocity. One fixed arena and one docking target make the first trial about control, not content volume. Walls end the attempt; restart restores the starting state.

O/P rotate anticlockwise/clockwise through eight headings. SPACE applies thrust in the current heading; turning and thrust are separate actions in this first trial. S starts, R retries and Q quits. The initial position is below and left of the dock, so approaching it requires managing both velocity components. A speed cap keeps motion inspectable. Docking requires the ship's centre in the inner box and resultant speed at most 0.4 pixels per update.

The intended appeal is a soft arrival earned through planning burns. The risk is that slow BASIC updates, drawing flicker or coarse rotation make corrections frustrating. Successful native docking with the revised feedback establishes the accepted baseline for lesson development. If the control loop is too slow, reduce repeated drawing/arithmetic and reassess the representation within BASIC. Performance/assembly revisits remain deferred.

## Representation and presentation

Position and velocity are separate two-component quantities. Rotation changes heading; thrust changes velocity; velocity changes position. Eight direction vectors and triangle vertices are calculated once at startup with SIN/COS. The update loop looks them up. This retains a visible connection between angles and motion while avoiding trigonometry on every update.

An original small white vector triangle shows orientation. A rectangular dock, textual instructions and a quiet arena give it room to move. Colour never determines collision or docking. The prototype is deliberately silent. All graphics are drawn by the maintained BASIC source; no external artwork is required.

## Development and verification

| Stage | Result | New idea | Check |
|---|---|---|---|
| Steering trial | Turn a triangle in an arena | Heading table and pixel drawing | Eight orientations and safe erasure |
| Free flight | Burn, coast and counterthrust | Two-component acceleration and retained velocity | Release preserves velocity; rotation alone preserves velocity |
| Docking trial | Arrive slowly, crash or retry | Speed and position as separate conditions | Fast passage does not win; slow arrival does; complete reset and quit |

These are prototype concerns, not a fixed lesson count. ROM-enter the listing, save a self-starting tape and reload into a fresh emulator. Drive checks by keyboard; read state for comparison without injecting it. Retain source/tape identities, original captures, measured update timing and the tested emulator/ROM configuration. Check held keys, direction wrap, speed cap, both velocity components, all walls, win/failure freeze, restart and exit. Native playability and original-hardware performance remain separate claims.
