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

## 2026-07-02 — round 10: the eraser problem — the night withdraws

**Playtest round 10 (Steve):** the greedy nearest-light rule made the wisp a
perfectly efficient eraser — stuck behind a building, you watch it undo your
latest lamp; "a pain in the bum to win."

**Fix — the scatter lesson:** after a snuff, the wisp **withdraws** to its home
corner and only resumes hunting on arrival (draught_mode flag; deterministic;
reuses the corner machinery). Every snuff buys a guaranteed window; the re-entry
quarter is plannable. Hunt → snuff → withdraw → hunt is the game's rhythm now.
If the pressure still reads as too laser-focused, the escalation is oldest-lit
targeting (the dark reclaims the ground it lost first) — parked unless needed.

All five checks green. Round 11: does the rhythm read, and is the window enough?

## 2026-07-02 — round 11: geometry inequity — the night rests at home

**Playtest round 11 (Steve):** still hard as the pace rises; watch 3 specifically
brutal — its entry corner sits nearly on the close lamp pair by the walls, so the
withdraw round-trip was a few cells and the snuff window vanished exactly where
two lamps needed defending.

**Fix:** WREST 48 — the wisp rests at home after each withdrawal, so the window
holds regardless of corner-to-cluster distance. One constant evens all four
watches' geometry. **Still parked if pair-camping persists:** oldest-lit
targeting (the dark reclaims the ground it lost first).

All five checks green. Round 12: is watch 3 fair now, and does the whole night
curve?

## 2026-07-02 — round 12: oldest-lit — the night bears grudges

**Chosen by Steve** after the rest beat left watch 3's pair-camping intact. The
wisp now targets the **oldest lit lamp** (lit-order queue; push on light, remove
on snuff) — its next grievance is usually across the square, so camping a pair is
structurally impossible. With nothing lit it hunts the lamplighter's flame:
**your first lamp turns the hunt away from you** — the opening teaches itself.
Nearest-light scan and manhattan retired; chase step, withdrawal, rest unchanged.
Brief §10 behaviour block annotated (rounds 10–12 evolution).

All five checks green; idle probe still loses. Round 13: is watch 3 beatable,
and does the whole hunt now read as a creature with a memory?

## 2026-07-02 — round 13: the finishing tier — dawn sweep + the longest night

**Tuning note first (Steve): "we may have made it too easy"** after oldest-lit —
banked for the capstone calibration; every knob is data (dusk_table, dusk_lentab,
WREST, GATHER).

**Built:** the **dawn sweep** (morning descends row by row, ground to gold, mist
burning off — a second of ceremony between the dawn text and the fanfare) and
**your longest night** (five title pips, one per watch survived, best run, dawn
fills it; recorded at NIGHT FALLS and the dawn, never reset in play; no digits).
That was brief §10's last unbuilt feature — **the reshape's feature set is now
complete.**

Six checks green (the dawn script now continues to the title and verifies the
golden row). **Remaining:** the audio pass (chime redo + a dawn phrase — needs
Steve's ear), the difficulty calibration, then the unassisted title-to-dawn
capstone run → decompose → re-author.

## 2026-07-02 — round 14: the audio pass — the ear got a fast loop

**The enabling move first:** Build198x grew its second tool (the demand gate
fired on this exact round): `build198x beeper` turns phrase notation into an
audition WAV and the phrase's assembly block — same timing model both ways,
calibrated by regenerating rounds 1–13's hand-authored constants exactly.
Audition went from assemble→boot→capture→listen to edit→listen; every sound
below was chosen by Steve's ear from generated candidates.

**Chosen:** the title now *loops* — dusk bells (cold A4 tolls, the E5→C5
motif, a warm rise, D5 left hanging so the loop leans home), one note per
`title_step` pass, SPACE polled between notes. `chime_dusk` is retired, not
redone: every one-axis variant failed Steve's ear because the two bells were
a fragment doing a whole piece's job — inside the tune they already do it
well. The dawn gains `chime_dawn` (dusk's bell reversed, ending on the
dominant so `fanfare_held` answers it — auditioned *in sequence* with the
fanfare, which is what settled the vote). `blip_lit` finally rises as brief
§10 always said (C6→E6, the motif at blip speed); `blip_snuff` falls the
same third an octave down. One motif, title to dawn.

**Emulator verification caught a real bug:** with per-cell polling a 6-frame
SPACE tap vanished into a blocking cell. Fix: per-note steps plus
`title_rest` — the tune's silence polls every frame and latches the press.
A tap can land inside a note, never inside a rest. Title capture is 62.6%
audible over 10 s (the tune's own tone-to-rest ratio); the same tap that
was eaten now starts the game.

**Remaining:** the difficulty calibration ("we may have made it too easy" —
banked from round 13), then the unassisted title-to-dawn capstone run →
decompose → re-author. The audio pass is done.

## 2026-07-02 — round 14: the audio pass lands (parallel session) — gate green on it

**The audio pass arrived from Steve's parallel session** (code-samples f37c8a5):
title dusk bells (cold A4 tolls, the E5→C5 motif "a lamp lit far off", D5 left
hanging into the loop), the dawn phrase (dusk's bell reversed — C5-E5-G5, the G5
leaning on the dominant so the fanfare's C answers it), and lamp blips that quote
the dawn motif at blip speed (snuff falls the same third an octave down). Phrases
authored as .bpr files, routines emitted by `build198x beeper` — the demand gate
opened a beeper tool. The dawn sequence is now chime → sweep → fanfare ("G5
hangs, the sweep holds the breath, the fanfare's C answers").

**Gate re-verified on the audio build:** all endings + probe green; title-pips
check green; both WAVs (bells loop, dawn sequence) recorded with signal. One
script adaptation: the title now plays between polls, so gate-script Space taps
on the *title* hold 30 frames (a press must land whichever bell cell is playing)
— but the post-dawn tap had to stay short (4 frames): a 30-frame hold outlived
the title's 25-frame input lock and started a fresh run. **Confession: a title
tune changes the input contract of every screen that returns to the title.**
The dawn-candidates audition sheet committed as provenance.

**Remaining:** difficulty calibration (the "too easy" flag) + the unassisted
title-to-dawn capstone run → decompose.

## 2026-07-02 — round 15: THE CAPSTONE — played end to end, and won

**Steve, unassisted, title to DAWN BREAKS: "I love it. Played end to end. And
yes, I won."** The winnability gate's human half is passed on the reshaped game;
the six-script machine half is checked into `prototype/capture/` (win/deepening,
dawn/pips, loss, menace probe, two audio captures) with its address-derivation
and input-timing contract documented. The round-13 "too easy" flag did not
survive the finished night — no re-tune requested at the capstone.

**The prototype phase is complete.** The pilot's shape, for sizing the other
four launch games: **two working sessions across two days (2026-07-01 evening →
2026-07-02 afternoon), 15 playtest rounds, ~20 gated commits** — taking a
shipped, forward-authored game through validate-and-repair into a redesigned,
audio-complete, gate-proven prototype (plus a parallel audio session).

**Next phase — decompose:** the prototype's commit history is the unit-sequence
draft; this log holds the confessions (the recoil, the load-bearing stipple,
absence-doesn't-read, the input-contract lesson, the eraser problem). Then:
re-author the disproved units (12–15, 19, plus the new material — tendril,
pools, dawn, bells), realign the brief to the 14-section spec, and only then
does the rebuilt Gloaming replace the shipped one (never-regress guardrail).

## 2026-07-02 — decompose: teaching order ≠ discovery order — and two modules

**The decomposition settled with Steve.** Principle: the learner builds an iteration
only where feeling the failure teaches (the wall-magnet, the eraser problem); dead
iterations (the bounce, rules-before-canvas) are confessed, not built. Five calls made:
no bounce unit; nearest-then-oldest both taught; texture at unit 2; audio in each
module's finish phase; and the big one — **the reshaped game is no longer tiny, so
Gloaming becomes one game spanning two modules** (the pattern modules-not-games and the
gentle-ramp's revisit-modules amendment already blessed). Module 1 "Gloaming" (~20
units) keeps the tiny promise: single dusk, a draught that hunts you, lives, the win.
Module 2 (working title "The Long Night", ~10 units) is the reshape as a revisit
module — its secret curriculum is iteration itself. Ladder: Primer → Gloaming → The
Long Night → Shadowkeep. Gentle-ramp amended; per-unit-plan rewritten (supersedes
2026-06-01).

**Next:** derive + gate the module-1 cut from the proven prototype; realign the brief;
author module 1.

## 2026-07-02 — the module-1 cut: derived, assembled, gated

**The tiny first game exists as a build.** `gloaming-m1.asm` derived from the
proven prototype by scripted subtraction (assert-anchored transforms + label-span
deletion; no hand-retyped code — provenance is the proven file). Out: pools,
tendril, grudge queue, watches, dawn, title tune. In: texture, brick, buildings,
tamed key, warm ramp, hunt-the-player at pace 16, recoil, gather, single-dusk
win/loss, a best-lives pip row as the module-scale go-again, and a one-shot dusk
chime voiced from the bells' opening tolls. One derivation gotcha for the record:
the tail-label deletion swallowed `END start` — a subtraction script must respect
directives after the last label.

**Gate:** m1-won (held screen → title with pips), m1-sting, m1-probe (idle player
still hunted down) — all green, checked into capture/. **Remaining before module-1
authoring:** Steve's playtest of the cut (pace 16 hunt-only may need a nudge — it
has no snuff pressure), then the brief realignment, then units.

## 2026-07-02 — module-1 cut playtested: approved

**Steve on the tiny game: "It works for me, it's not TOO hard."** Pace-16
hunt-only is the right gentleness for a learner's first game — no retune. The
module-1 gate is fully closed: machine suite + human hands. Next: the brief
realignment, then module-1 authoring.

## 2026-07-03 — the deepening's one visible lie: draw_lives fixed

**Found during the module-2 route skeleton** (unit 6's "lives carry"
turned out to be un-photographable): `draw_lives` painted `LIVES` — the
constant — so every watch's `init_game` repainted three pips regardless
of the carried count. Lose a life, hold the dusk, and watch 2 opened
with a full row; a later loss then erased index (lives−1), leaving a
lit–dark–lit row. The bug arrived with the run/watch split and survived
all fifteen playtest rounds — nobody read the life row across a watch
boundary after a loss. m1 is unaffected (lives reset per game).

**Fix, approved by Steve:** `draw_lives` reads the carried `(lives)`.
Display-only — the loss logic always read memory. Re-gated: all six
suite scripts green (poke addresses re-derived from the fresh `.sym`,
a +2 shift; capture README updated), the skeleton re-derived, both
chain anchors re-verified. The fix is unit 6's diff on the route —
the deepening is what turns lives into a carried quantity.
