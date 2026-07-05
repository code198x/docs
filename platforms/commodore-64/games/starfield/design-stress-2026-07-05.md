# Starfield — Design-Stress Pass (2026-07-05)

Adversarial refutation of the **shipped** C64 assembly first game. Target build:
`code-samples/commodore-64/assembly/starfield/unit-17/steps/step-02.asm` (the
cumulative final program, 1064 lines). Stance: the player who wants to win
cheaply, not the designer's friend. Every finding is a falsifiable scenario
checked against shipped code, not the brief.

**Bottom line:** Starfield does **not** clear the jeopardy + winnability-gate bar
as shipped. Loss is reachable *only by deliberately bad play* (the death capture
scripts drive the ship into an enemy). Under optimal play the fail state is
**unreachable** — two independent immortality strategies exist, one of which is
the methodology's own house specimen and is **STILL LIVE**. The winnability gate
passes only *vacuously* (loss can be scripted, but cannot be forced), which is
exactly the gap `a-game-needs-jeopardy.md` says closes the loophole.

---

## Findings (severity-ordered)

### BREAKS 1 — The turret park is STILL LIVE (named specimen: CONFIRMED)

**Scenario:** Park the ship under the spawn column, hold fire, never move. Every
enemy funnels straight down into the bullet stream and dies before it reaches the
ship. Player scores freely and never loses.

**Code evidence — the seed clusters:**
`spawn_enemy` (step-02.asm:577) sets each enemy's column from one source only:

```
lda $d012          ; raster line -> "pseudo-random" column
and #$7f           ; 0..127
clc
adc #$30           ; X = 48..175
sta enemy_x_tbl,x
```

There is **no per-enemy offset, no PRNG state, no spreading term** — the column is
purely a function of *what raster line the beam is on at the instant of the call*.
And that instant is nearly fixed:

- **Every frame is raster-synced to line 255** at the top of `game_loop`
  (step-02.asm:88, `cmp #$ff`). All game logic runs from a fixed beam position.
- **Respawns happen at fixed code locations.** The fall-off-bottom respawn
  (:336) and the flash-done respawn (:343) both sit inside `enemy_loop`, a fixed
  cycle offset past the line-255 sync — the beam has advanced a near-constant
  number of raster lines by the time `$d012` is read, so `$d012 & $7f` lands in a
  narrow band (roughly the teens–twenties → X ≈ 63–76). Frame-to-frame jitter is
  only a few lines (the parallax star loop's move/no-move branches and joystick
  deltas), i.e. **a few pixels**.
- **The initial wave is worse.** `enter_game` calls `spawn_enemy` three times
  back-to-back (:714–722), ~50 cycles apart — *under one raster line*. All three
  opening enemies get an X within 0–1 of each other and descend the **same
  column, single-file**, only staggered in Y.

**Why the cluster beats the aim tolerance:** the collision test treats
`|bulletX − enemyX| < 16` as a hit (`cmp #$10`, :387). The whole spawn band is
~10–16px wide — *narrower than the hit tolerance*. A bullet fired straight up from
one parked X therefore covers the entire cluster; the player never has to track.

**Why the park is safe, not just productive:** a hit enemy is set to flash for 8
frames (`lda #$08 / sta flash_tbl,x`, :409) and during the flash the enemy loop
**freezes it in place** (:342, does not fall) *and* the ship-collision loop
**skips it** (:470–471, `lda flash_tbl,x / bne next_ship_check`). So the moment
you hit an enemy it becomes harmless for 8 frames, then respawns at the top. With
one bullet clearing each descending enemy well before it closes the last gap
(wave-1 fall is 1px/frame; capped at 3px/frame — see BREAKS 3), nothing reaches
the ship. And even a rare slip costs almost nothing: `death_timer` grants 90
frames of invulnerability on a hit (:531).

**Verdict: STILL LIVE.** The mitigation the specimen warned about was never
applied to the shipped spawn code.

**Current answer:** none.

**Suggested direction (one):** give the column a real per-spawn seed —
e.g. an 8-bit LFSR advanced once per spawn, or at minimum `(prng + enemy_index *
40)` so the three lanes are forced apart by more than the 16px hit tolerance.
(Pedagogy note: an LFSR is a *net-positive* teaching addition, not a budget hit —
see Finding "Pedagogy" below.)

---

### BREAKS 2 — Half the playfield is a permanent no-death zone (sit-still immortality)

**Scenario:** Fly to the right third of the screen, stop, do nothing. You are
immortal indefinitely (you also score nothing — this is the pure-survival cheese,
distinct from BREAKS 1 which scores). Even simpler than the turret park: no aim,
no timing, no button.

**Code evidence:** Enemies only ever occupy **X 48..175** (`spawn_enemy`,
:582–583). The ship clamps to **X 24..320** — the right clamp allows the ship
well past 255 (`cmp #63` against the 9th-bit half, :220). The ship-collision test
needs `|shipX − enemyX| < 16` *and* the ship's 9th X bit clear:

```
lda $d010
and #%00000001     ; ship past X=255 -> bit set -> skip the whole check
bne next_ship_check
```
(step-02.asm:482–484)

So any ship X ≥ 191 is safe: at 9th-bit-clear positions 191–255 the nearest
possible enemy (X 175) is ≥16px away, and at X ≥ 256 the check is skipped
outright. That is **≈129px of the ~296px playfield (≈44%) where the player cannot
be touched by any enemy, ever.** Park there and the fail state is structurally
unreachable.

**Current answer:** none. (Same root as BREAKS 1 — the enemy X band is far
narrower than the field the ship can occupy.)

**Suggested direction (one):** widen the enemy spawn X to span the ship's full
travel (and/or give enemies horizontal drift toward the ship's column) so no
static ship position is out of reach.

---

### BLEEDS 3 — Difficulty caps at wave 5 and never rises again (tension collapse + boredom)

**Scenario:** Play past wave 5. Nothing ever gets harder. Minute 10 is
mechanically identical to minute 2.

**Code evidence:** The only difficulty lever is fall speed, and it is a 5-entry
table clamped at the last index:

```
WAVE_TOP = 4
wave_speed_tbl: !byte 1, 2, 2, 3, 3     ; (step-02.asm:813-815)
```
`advance_wave` clamps the index at `WAVE_TOP` (:770–772), so `fall_speed` is
**3px/frame forever from wave 5 on**. Enemy **count never changes** (always 3),
there are no formations, no new enemy behaviour, no player progression. The
program's own comment concedes it: *"the physics admits it ran out of new
ideas."* The wave number keeps climbing (and the HUD digit caps at 9), but the
game underneath is flat. Even absent the two BREAKS, a ceiling of "3 enemies,
single column, 3px/frame" is thin pressure; combined with them it is none.

**Current answer:** the climbing wave *number* — cosmetic only.

**Suggested direction (one):** once the speed table tops out, escalate a second
axis (enemy count, or a second column, or spawn cadence) so the curve keeps
bending after wave 5.

---

### BLEMISH 4 — Score silently wraps at 100

**Scenario:** Score 100 kills (trivial under BREAKS 1). The two-digit BCD score
(`sed / adc #$01`, :431–435) rolls 99 → 00 with the carry discarded. The readout
resets to "00" and is meaningless thereafter. No high-score, no win threshold, so
the only feedback loop the game has quietly breaks. Minor because it needs a long
sitting to hit, and the game has no win state riding on it.

**Current answer:** none.

---

### BLEMISH 5 — Right half of the field is a dead firing zone

The collision test rules out any bullet whose 9th X bit is set (`check_x`,
:381–383) — bullets fired from X > 255 hit nothing. It is *consistent* with
BREAKS 2 (enemies never go there) rather than a standalone bug, but it means the
right portion of the screen is inert for both offence and defence: you can neither
be hit nor hit back there. Discoverability-neutral; noted for completeness.

---

## Closed holes (verified in code — not findings)

- **Death-frame-one / respawn safety.** On losing a life the ship respawns at a
  fixed safe start (X 172, Y 220) with a 90-frame invulnerability window
  (`death_timer`, :531) during which `ship_collision` is skipped (:464–466). No
  spawn-camping death loop.
- **Exploding-enemy double-jeopardy.** A flashing enemy is excluded from both the
  bullet-collision loop (:367–368) and the ship-collision loop (:470–471), so a
  mid-explosion enemy can neither be re-hit for extra points nor kill the ship.
  Clean.
- **9th-bit X wrap.** Ship and bullet handle the $00↔$FF X wrap with the Primer's
  EOR bit-flip (:197–234); collision rules out cross-half false positives via the
  9th-bit gates (:381, :482). No wrap-around phantom hits.
- **Title/game-over fire debounce.** `ui_lock` (:135, :149) eats the press that
  ended the previous screen, so a held fire button can't skip the title or
  instantly restart from game-over. No input bleed across states.
- **Loss is drivable by script.** `unit-11/capture/death.script.json` forces a
  collision and reaches game-over — the loss *path* exists and is exercised. (It
  just isn't reachable under optimal play — see BREAKS 1 & 2.)

---

## Open questions (playtest-only — cannot be settled from code)

- **Exact cluster width in the emulator.** The static analysis puts the respawn
  band at ~10–16px; a scripted "park and hold fire" run in Emu198x would confirm
  the live width and whether any wave-5 (3px/frame) case ever slips an enemy past
  a parked, firing ship. Expectation from code: it does not.
- **Discoverability of the exploits.** Whether a first-time learner *stumbles*
  into the turret park or the right-side dead zone within a minute, or only finds
  them deliberately, is a playtest question. Structurally both are trivially
  discoverable (the opening wave descends a single visible column; parking right
  is the obvious "avoid" instinct).

---

## What gates a fix before the next build

- **BREAKS 1 (turret park)** and **BREAKS 2 (right-side no-death zone)** each
  independently violate the jeopardy bar: the shipped game cannot be *lost* under
  optimal play, so the winnability gate passes only vacuously. **Both gate a
  fix.** They share a root cause — the enemy X band (48–175) is both narrow
  (clusters) and narrower than the ship's travel (leaves a safe zone) — so a
  single change (a real per-spawn PRNG that spans the full field, forcing lanes
  apart by more than the 16px hit tolerance) closes both at once.
- **BLEEDS 3 (difficulty cap)** should ride the same build: fixing spawns without
  restoring a rising curve leaves the game winnable-to-loss but still flat by
  wave 5.
- **Pedagogy check:** the fix is *aligned* with the teaching route, not in
  tension with it. The current spawn "randomness" is the beginner raster-as-random
  trick; replacing it with an 8-bit LFSR (or an index-spaced column) is a
  legitimate, small, well-precedented technique that *adds* to the budget rather
  than blowing it. No teaching route is broken by closing the holes.
- **Blemishes 4 & 5** do not gate; fold into the same pass if convenient.
