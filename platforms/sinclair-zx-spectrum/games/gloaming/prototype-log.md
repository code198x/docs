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

## 2026-07-01 — round 4: the wall found at dusk 5 → the dawn breaks

**Playtest round 4 (Steve), deepening build:** held dusks 1–4 (paces 16, 13, 11, 9)
first session — the curve works. **Dusk 5 at pace 8 is "damn near impossible"** —
the same pace judged "much too aggressive" as a raw opening in round 3. Pace 8 is
the human wall for this game; the old table's tail (7, 6, 5) was superhuman dead
data nobody would ever see.

**Decision (recommended in-session; Steve away, proceeding, trivially reversible):
the night is five watches, and it ends in DAWN BREAKS.** Table retuned to
16, 13, 11, 9, **9** — the final watch is the pace the playtest *beat*: the climax,
not the ceiling. Endless-arcade dropped: a run that always dies at the same wall is
the wrong shape for the track's completion headline; *you held the square until
morning* is a real ending. Brief §10 amended same-day. STATE_DAWN added; Space
after dawn returns to the title (the run is complete), THE NIGHT IS HELD stays the
per-dusk interstitial.

**Verified (six checks, screenshots):** dusk-1 win → held screen; Space → dusk 2
with lives carried; fifth-watch win → DAWN BREAKS in the golden square; Space →
title; loss → NIGHT FALLS; idle probe still hunted down. All green.

**Remaining in the reshape:** the best-night pips (title-screen go-again row, dawn
filling it), then the audio pass (weak chime + a dawn deserves better than the
reused fanfare), then Steve's full unassisted run — title to DAWN BREAKS — as the
reachability capstone before decompose/re-author.

## 2026-07-02 — round 5: the hybrid — the dark becomes a character

**Dawn verdict (Steve): earned.** Then the design leap: Steve's vision of the dark as
"a creeping pool of blackness" (Mashadar, *Wheel of Time* — creditable by name under
the inspired-by amendment). Hybrid chosen over cosmetic-trail and full-replace: the
wisp keeps hunting (all validated work stands) and now **trails a tendril of solid
night** — ring-buffered so the oldest cell always releases (no permanent walls, no
trap analysis, fixed memory); reach per watch = dusk_lentab 6/9/12/15/18, the curve's
second axis. Counter-force: **light pools** — lit lamps warm their eight neighbours,
pool cells are tendril-immune. Dark blocks the player, never kills; the wisp's touch
keeps the lethality.

**Discovery — the stipple is load-bearing.** First build: mechanics live, screen
unchanged. The ground had no bitmap (another brief§6-vs-build divergence: "sparse
stipple" was never drawn), so glow recolours painted nothing and dark-on-black
vanished. fill_ground textures the square once at init — and pools + tendril became
visible as pure attr changes. The magazine-screenshot test (§6) now passes: the held
screen shows eight lamps in eight pools. **Confession: on the Spectrum, a feature's
visibility can live in a different subsystem from its logic — we built the rules
before the canvas.** Teach with the pools/tendril unit.

**Verified (five checks):** held + deepen, dawn, loss, the character shot (tendril +
pool in one frame), idle probe. All green on the textured build.

**Steve's own framing, banked:** "this also makes it a slightly different game — let's
see if it feels right." Round-6 playtest decides whether the hybrid stays. Still
queued behind it: gathering pause, interior buildings, corner rotation, dawn sweep,
best-night pips, audio pass, the unassisted capstone run.

## 2026-07-02 — round 6: absence doesn't read — the dark needs a body

**Playtest round 6 (Steve):** two visual findings — the tendril hard to see, the
walls not attractive enough.

**The tendril fix is a design lesson worth teaching:** the dark was rendered as
*absence* (black-on-black void cells), and absence doesn't read at cell scale — the
eye skips a hole in sparse stipple. Mist is a *presence*: dark cells now carry a
dense swirl texture in bright blue ink, and the tendril reads instantly as glowing
cold veins. Same rule, same byte-compare structure — only the body changed.
**Confession: we rendered "nothing" and expected it to look like something.**

**Walls:** the brief's brickwork ("reads as built, solid") — mortar courses,
staggered verticals — blitted wherever the wall attribute bit is set, so interior
buildings will arrive pre-bricked and the win ramp turns the brick golden.

All five checks green. Round 7 is the hybrid verdict proper, now that the hybrid
can actually be seen.

## 2026-07-02 — round 7: gaps in the night — two rules bugs, one design trade

**Playtest round 7 (Steve):** graphics approved ("a lot better"), but visible
*gaps* mid-tendril. Two causes: (1) re-crossing its own tail didn't refresh the
ring's claim, so the old entry expired mid-vein; (2) pool immunity meant crossing
a pool left a hole once the pool died.

**Fixes:** re-crossed cells re-push and releases scan for newer claims
(tendril_claimed); and — the design trade — **pool immunity became pool
resilience**: the tendril takes pooled ground, but released cells inside a live
pool return to glow (pooled_at). Better fiction too: the dark can cross spilt
light, but the light returns. **Confession: both bugs were invisible until the
antagonist was watchable — rendering exposed rules.** Pools still block nothing;
the DARK-blocks-player rule is unchanged.

All five checks green. Round 8: the hybrid verdict, gap-free.

## 2026-07-02 — round 8: hybrid approved; the routing update lands

**Playtest round 8 (Steve): "this feels right so far"** — the hybrid stands. The
gaps fix (round 7) held.

**Landed behind the verdict:** the gathering (GATHER 120 — the dark holds ~2.4s at
each dusk's start; recoil keeps the short beat), corner rotation (the dark enters
NE/SE/SW/NW by watch, deterministic, recoil returns it to the watch's corner), and
the brief-§6 interior buildings (two 4×3 brick blocks, data-driven, solid to the
player, ghosted by the wisp — the seek asymmetry made spatial).

All five checks green. **Remaining:** dawn sweep, best-night pips, audio pass
(weak chime + a dawn phrase), then the unassisted title-to-dawn capstone run.

## 2026-07-02 — round 9: the buildings multiply the tendril — soften the opening

**Playtest round 9 (Steve):** "the tendril makes life VERY difficult" — and he
**lost at watch 2 with seven rounds of practice**. Diagnosis: the features
multiplied — in the open square a tendril was an annoyance; with buildings the
player moves in *lanes*, and a tendril across a lane is a closed door (the wisp
even threads mist through the buildings themselves). Each dark cell became worth
more the moment the geometry landed.

**Fix (data-only):** dusk_lentab 6/9/12/15/18 → **3/6/9/13/18** — the opening
watch shows a three-cell wake to learn from; the final watch still strangles.
Same law as the pace table: **readable before it's a threat.** A practised
player losing early is the calibration signal for a first game — the learner
arrives with zero rounds of practice.

All five checks green (data change, no layout shift). Round 10: does watch 1
teach and watch 5 threaten?
