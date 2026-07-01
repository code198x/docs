# Gloaming — prototype discovery log (validate-and-repair pass)

The endpoint-first discovery log (✦ convention in
[decisions/endpoint-first-authoring.md](../../../../decisions/endpoint-first-authoring.md)),
kept for the 2026-07 validate-and-repair pass. The shipped game (unit 21, `step-01.asm`)
is the starting point; the reshape contract is brief §10.

## 2026-07-01 — baseline: gate re-run + first human playtest

**Gate re-run (machine):** both checked-in scripts (`step-01-won`, `step-01-sting`) run
green on the current Emu198x release build (rebuilt from 2026-07-01 HEAD; screenshots
byte-identical to the 9 Jun binary — the ULA timing fix was Pentagon-class only). Win
reaches THE NIGHT IS HELD + fanfare; loss reaches NIGHT FALLS + sting.

**Human playtest (Steve), shipped build — findings:**

| # | Sheet question | Finding | Disposition |
|---|---|---|---|
| 1 | Held-key movement | **WAY TOO FAST** — one cell/frame at 50 Hz confirmed as wall-magnet | Repair: repeat-gate (step on press, then every N frames held); tune N by feel |
| 2 | The draught | "Just bouncing — not very *menacing*" | Reshape (brief §10): seek-the-nearest-light replaces the bounce |
| 3 | Three phrases | Didn't register as distinct musical beats | Watch: re-ask after the speed fix slows the game down; may need nothing |
| 4 | `LOCK 25` | Player never noticed it | **Pass** — an input lock is working precisely when it's invisible |
| 5 | Unassisted win | **Won first time** | Reachability confirmed ✓ — but zero challenge; confirms the missing curve (brief §10 "the night deepens") |
| 6 | Win-screen walls | Magenta flood — **bug**, not a glow | Repair: win recolour should be the warm-yellow vocabulary of §6 |

**Reading:** findings 1+5 compound — the player is 8× faster than the draught *and* the
draught doesn't hunt, so the shipped game cannot threaten anyone. The reshape isn't
gold-plating; the baseline proves the game has no antagonist in practice.

**Order of work from here:** prototype workspace forks unit-21's `step-01.asm`
(never edit shipped units in place — "never regress the launch"). Commit-sized
teachable increments; win + loss scripts re-run after each. Repairs first
(speed gate, magenta), then the reshape (seek rule → dusk table → best-night pips),
then re-playtest.

## 2026-07-01 — round 2: repairs approved; the seek lands; the recoil discovery

**Playtest round 2 (Steve), repaired build:** movement at `PLAYER_REPEAT 6` approved
("that works"). New finding: **the dusk chime is weak** ("a bit crap") — audio polish
item, deferred to its own pass alongside the three-phrases re-listen.

**The seek rule landed** (brief §10): `draught_step`'s bounce replaced by
seek-the-nearest-light — Manhattan scan over lit lamps *plus the lamplighter's own
flame*, step one cell along the greater-distance axis, ties sideways, 4-connected.
**Walls don't stop the night** — the wisp drifts through stone: fiction-true, more
menacing, and it deletes the pathfinding/stuck-in-a-building problem class outright.
Design call made in-session; playtest to confirm it reads.

**Discovery — the recoil.** First menace probe (no input after Space): NIGHT FALLS in
~250 frames — *too* fast. `lose_life` reset the player to START but left the draught
standing at the catch-site; under the old bounce that was invisible, under the hunt it
meant a catch stripped every remaining life in seconds (the wisp camps the respawn).
Fix: the taking costs the night its reach — the wisp recoils to its far corner, so
every life buys a whole fresh chase. Probe after: mid-game alive at frame 250 with the
wisp bearing down; NIGHT FALLS by ~500 frames idle (~10s, Pac-Man-honest).
**Confession material: a hunting antagonist exposes respawn-fairness assumptions the
wallpaper version never tested.** Teach with unit 15 (lives).

**Gate state:** win + loss scripts green on the seek build (tap choreography;
poke addresses re-derived from the `.sym` after each layout shift — scripts now
regenerate from symbols, not hardcoded addresses). Menace probe added as a third
checked-in verification: an idle player must lose.

**Open for round 3 (Steve):** does the dark feel like it *wants* the lamps? Is
`DRAUGHT_SPEED 8` fair for dusk 1? Does wall-ghosting read as intent or bug? Then:
the dusk table ("the night deepens") and the best-night pips.

## 2026-07-01 — round 3: "MUCH too aggressive" → the dusk table lands

**Playtest round 3 (Steve), seek build:** the hunt at one step per 8 frames is
**much too aggressive even as an opening** — the raw seek gave the wisp no gentle
mode. The contracted fix was already queued: the curve.

**The night deepens (brief §10), implemented:** `dusk_table` (16, 13, 11, 9, 8, 7,
6, 5 frames per step; deeper dusks hold the last entry) replaces the constant —
dusk 1 at half the round-3 aggression *on purpose*: the hunt must be readable
before it's a threat. A run is now a night: THE NIGHT IS HELD is the dusk
interstitial (Space → deeper dusk, square re-darkened, lives carried); only NIGHT
FALLS ends the run. Score = dusks survived.

**Verified:** win gate green; deepening screenshot-verified (fresh dusk, carried
lives); loss gate green; idle probe still loses at dusk-1 pace.

**Design question parked for Steve:** §10 contracted the endless-arcade shape
(dusks until the night wins). The alternative with a *completion* beat: a fixed
night — survive N dusks and **dawn breaks**, a true win that fits both the title
and the track's "I finished a real game" headline. Decide before the best-night
pips (it changes what they count).
