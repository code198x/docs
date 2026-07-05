# Dash — Design-Stress Pass (2026-07-05)

Adversarial refutation of the **shipped** NES (ca65) assembly first game, *Dash*.
Target program: `code-samples/nintendo-entertainment-system/assembly/dash/unit-17/dash.asm`
(unit 17, "The Last Yard" — the final, complete program). Every claim below is
checked against that source. Stance: the player who wants to win cheaply, the kid
mashing buttons — never the designer's friend.

**Verdict up front:** Dash **clears** the jeopardy bar and the winnability gate as
shipped. It is drivable to a win (level turn — `capture/level-two-run.script.json`)
and to a loss (`capture/lose-sting.script.json`); a real fail state exists and is
reachable. **Zero BREAKS.** The residue is one soft-tension BLEEDS and three
BLEMISHES. The three house specimens this methodology was seeded from are **all
verifiably CLOSED in unit 17** — with a clean before/after diff against unit 16.

What Dash actually *is* (this matters, because two specimens assume a traversal
platformer): a **single static screen**, no scrolling. The runner starts at x=60 on
the ground and moves left/right by D-pad. One diamond obstacle sweeps right-to-left
on the ground and loops. Three coins (x=32, x=128 on a platform, x=200 behind a
short wall) must all be collected to turn the level over; the obstacle then quickens
from a speed table. Lose all three lives → GAME OVER. It is a jump-and-collect, not
an auto-runner — despite the index page's pitch (see Blemish 3).

---

## Findings

### Specimen verdicts (the priority three)

**1. Spike pit untraversable — CLOSED.**
Scenario tested: "a required gap one pixel wider than the jump leaves half the level
unreachable." In the shipped level data the hazard is a **single** spike tile —
`level_ground_spike_row: .byte 3,3,3,3, 3,3,3,3, 3,3,15,3 ...` (col 10 = x80-87,
8px). Diff evidence: unit 16 shipped a **two-tile** spike (`3,3,15,15`, cols 10-11,
16px) — that is the "one pixel wider than the jump" the unit-17 narrative confesses;
unit 17 halves it. Physics are unchanged across units (`JUMP_VEL=$F6` = -10,
`GRAVITY=1`), giving ~18 airborne frames. **Decisive point:** the spike hazard check
is gated on `on_ground` (line 500, `lda on_ground / beq @no_hazard`), so an airborne
player is *never* pricked regardless of horizontal reach — you clear the spike by
being in the air over col 10, and 18 airborne frames × 1px/frame of D-pad travel
(18px) comfortably exceeds the 8px tile. The right half of the level (coin at x=200)
is reachable: traced frame-by-frame, a jump from the ground carries the runner up
past the wall's top (row 24, y=192), lands on the wall crown (y=184), and walks/hops
off the far side to x≥193 where coin 2 collects. The winning capture script drives
exactly this and reaches L2. No required gap exceeds the jump. **Closed.**

**2. Respawn cascade — CLOSED.**
Scenario tested: "fixed respawn + moving hazard + no grace = three lives in three
frames." `take_damage`'s survivor branch (`@still_alive`, lines 690-702) resets the
runner to the fixed start (x=60, y=200) **and sets `hurt_timer = 60`**. Both damage
paths are gated on it: obstacle collision (line 463, `lda hurt_timer / bne
@no_collide`) and spike hazard (line 495-498, which also `dec hurt_timer` once per
frame). So a minimum of **60 frames (~1 s)** of full invulnerability follows every
non-fatal hit; three deaths therefore cost ≥120 frames, not three. Diff evidence:
unit 16 had **no `hurt_timer` at all** — the cascade was live there and is the "three
lives in three frames" the narrative confesses. The i-frames are even shown (player
sprite blinks, lines 560-566). **Closed.** (Minor note: `next_level` does not itself
set grace, but it resets `obstacle_x=255` (far away) and teleports the runner to
x=60, so there is no level-turn cascade either.)

**3. Self-collecting coin — CLOSED.**
Scenario tested: "a reset that doesn't reset every plane — a collectible auto-collects
on restart." `next_level` (lines 755-790) restores all three coins via `place_coins`
**and** teleports the runner back to the gate (x=60, y=200). The comment names the
exact bug and the fix: "Leave them where they stand and the respawned coin under
their feet collects itself on the next frame. Every reset, every plane." Verified:
after `place_coins` the coins sit at x=32/128/200; the runner is at x=60; the
`check_collect` AABB test (player_x+8 vs coin_x etc.) does not overlap any of them,
so nothing auto-collects. The same holds at initial spawn (`init_game_screen` also
places player at x=60). **Closed.**

---

### BLEEDS

**F1 — Obstacle-immune perches + no timer = jeopardy is soft and optional.**
- **Scenario:** The obstacle is fixed at ground height (`oam_buffer+4 = FLOOR_Y`,
  set once, never varied) and its collision is gated on `player_y >= FLOOR_Y-7`
  (=193; line 468-470). Any surface above that line is immune. The platform (row 20,
  x96-159, top y=160 → stand at y=152) and the wall crown (y=184) both sit above 193.
  There is **no timer** anywhere in the program. So a patient player jumps onto the
  platform, waits for the single, fully-predictable obstacle to sweep to the far side,
  drops for a coin, and retreats — collecting all three coins at near-zero risk. The
  laziest *survival* play is even cheaper: hold A to bunny-hop (jump re-fires the
  frame you land because the A test is level-triggered, line 274) and you are on the
  ground ~1 frame per hop.
- **Current answer:** none. No timer, no perch-seeking hazard, one deterministic
  obstacle.
- **Steelman:** two of three coins (x=32 mid-air, x=200 ground) force brief ground
  excursions, so the run isn't *entirely* perch-camped, and a careless player genuinely
  does lose (the lose script proves it). Jeopardy *exists*; it is just avoidable with
  patience. That keeps this a BLEEDS, not a BREAKS — the game is losable, the tension
  is thin.
- **Direction (≤1):** give the sweep some urgency the perch can't sit out — e.g. a
  second obstacle at platform height, or a slow coin-decay / level countdown so
  camping costs something.

---

### BLEMISHES

**F2 — Score HUD is a single digit; it garbles after 10 cumulative coins.**
- **Scenario:** `score` increments once per coin and never resets between levels
  (only at `init_game_screen`). The HUD renders it as **one** tile: `lda score / clc
  / adc #DIGIT_ZERO / sta PPUDATA` (NMI, lines 1204-1207). At 10 coins (reached
  partway through level 4) `score+DIGIT_ZERO` = tile 15 = the **spike glyph**; higher
  scores index letter tiles. The score readout shows garbage from the 10th coin on.
- **Current answer:** none (lives cap at 3 and the level digit clamps at 9, but score
  has no cap).
- **Direction:** either clamp/units-digit the score tile, or make it a two-digit
  readout.

**F3 — Index page pitches a game Dash isn't.**
- **Scenario:** `website/.../dash/index.mdx` sells "a fast-paced **side-scrolling
  runner**", "the world **rushes past**", "a **scrolling world** that gets faster",
  and lists "Scrolling — hardware scroll registers" as a skill. The shipped game has
  **no scrolling** — it's a static single screen with manual L/R movement and one
  looping obstacle. The page is also stale (`status: "in-progress"`, `units: []`,
  "Coming Soon") for a game that is complete through unit 17.
- **Current answer:** mismatch stands; a reader arrives expecting a Chrome-dino
  auto-runner and meets a static jump-and-collect.
- **Direction:** reconcile the index copy with the shipped mechanic (jump-and-collect
  on a fixed screen, accelerating obstacle) and flip the status/units metadata.

**F4 — Coin 2 (x=200) hides behind a wall the player may read as scenery.**
- **Scenario:** the wall (rows 24-25, x176-191) is drawn as plain ground tiles and
  is only two tiles tall. A player who walks (rather than bunny-hops) right hits it at
  x≈168 with the coin visible beyond and no explicit signal that jumping over/onto it
  is the route. Reachability is fine (the natural hold-right-and-hop "dash" carries you
  over it — traced and confirmed), but the read is soft for a *first* NES game.
- **Current answer:** relies on the player defaulting to bunny-hop-right.
- **Direction:** make the wall read as climbable (distinct tile) or nudge coin 2 to a
  spot the intended hop plainly reaches.

---

## Closed holes (verified in code)

- **Respawn cascade** — `hurt_timer=60` grace gates both damage paths; ≥60 frames
  between deaths (lines 463, 495-498, 701-702). Absent in unit 16.
- **Self-collecting coin on level turn / initial spawn** — runner teleported to x=60,
  no coin overlaps (lines 764-767, `place_coins`, `check_collect` AABB).
- **Spike untraversable** — single 8px tile, hazard `on_ground`-gated; right half
  reachable (lines 495-529, level data 1378-1380). Was 16px in unit 16.
- **`coins_left` underflow** — max three collects per level, `next_level` fires the
  same frame it hits 0 (lines 450-453); no wrap.
- **Bottomless pit / infinite fall** — ground rows 26-29 span the full width; the
  spike tile is non-zero so it still stops a fall. No column lacks a floor.
- **Y-wrap above screen** — clamped (lines 380-389).
- **Obstacle can't camp on the respawn point** — it always moves and loops; grace
  covers the overlap window; it never stalls on the player.
- **Speed-table index over-read** — clamped at `LEVEL_TOP` (lines 778-783); level
  digit clamped at 9 (line 1223).

## Open questions (playtest only)

- Does a *first-time* player discover the wall-hop to coin 2, or stall at x≈168 and
  conclude the coin is unreachable? (F4 — feel, not logic.)
- Is the no-timer camping (F1) something a real learner-player actually does, or does
  the absence of forward pressure just read as "boring" rather than "exploitable"?
  Boredom test needs eyes on a full three-coin run.
- On the landing frame after a bunny-hop, is the ~1-frame `on_ground` window wide
  enough for the fastest obstacle (speed 4) to land a hit, or is hold-A effectively
  invincible in practice?

## What gates a fix before the next build

**Nothing gates the build.** No BREAKS; the winnability gate and jeopardy bar are
both satisfied by shipped code and existing capture scripts. The three specimens are
closed. Recommended (non-gating) for polish, in order: **F2** (score glyph corruption
is a visible defect a reviewer will screenshot), then **F3** (the index page
misdescribes the game), then **F1/F4** as design-feel items for a later revisit.
