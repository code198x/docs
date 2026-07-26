# Starfield — Brief

**Title (working):** Starfield
**System / Track:** Commodore 64 / assembly
**Position:** Rung 0 — the first game after the *Meet the Machine* primer, sharing rung 0 (char/screen + colour memory) with it. See [c64-assembly-lineup.md](../../../../decisions/c64-assembly-lineup.md); the two shipped anchors are locked.
**Scope:** 18 units across two phases; counts illustrative, not a target (per [curriculum-structure.md](../../../../decisions/curriculum-structure.md)).
**Constraint position:** period-faithful — see Section 5.
**Status:** Written retrospectively, 2026-07-26. Records the game as shipped (units 1–17) and the summit designed for unit 18.

---

## Section 1: Pedagogical Role

Starfield is the first game on the C64 assembly track. It takes a learner who has met the 6510 in the primer and turns out a complete arcade program: a sprite on screen, then movement, firing, enemies, collision, score, waves, lives, a starfield, a title screen, a rising curve and an ending.

It sits at rung 0 with the primer — char and screen memory are the rung's technique — but it also *introduces* hardware sprites, SID and the frame-synced game loop at primer depth, so the games above it deepen those instead of meeting them cold. That is the deliberate C64 mirror of "Shadowkeep introduces masking; Lamplight deepens it".

## Section 2: Classic Ancestors

- ***Space Invaders*** (Taito, 1978) — the clearable cohort. The summit borrows its shape directly: a fixed set of enemies that can be finished.
- ***Galaxian*** (Namco, 1979) — attackers descending over a drifting starfield.
- ***Galaga*** (Namco, 1981) — waves that escalate, and attackers that come for the player's column.

**What we take:** the descent, the escalating wave, the final screen that can be cleared.
**What we leave:** formation choreography, diving attack runs, the tractor beam, two-ship play.

## Section 3: Remix Unit

**The enemies come for *your* column.** The spawn column is drawn from an 8-bit LFSR spread across the whole field the ship can reach, and each enemy then homes toward the ship's X — one frame in two, tightening to three in four from wave 7 (`unit-17/steps/step-04.asm:342–353`). No static position is safe, which is what separates this from a score treadmill: combined with a curve that has a top, the game reads as a siege you can break.

## Section 4: Core Experience

**Core verb: slide and fire.** Every second, read where the scattered descent is heading, slide the ship under it, hold the button. Across a session, nine waves quicken and thicken until every sprite the machine has is in play at once, and then one last cohort has to be cleared.

## Section 5: Constraint Position

**Period-faithful.** Everything here was ordinary in commercial 1983–85 C64 product, including the LFSR — a small, well-precedented replacement for the beginner's raster-as-random trick.

**In active use:**

- VIC-II hardware sprites — positions `$d000`–`$d00f`, the 9th X bit at `$d010`, enable at `$d015`, colours `$d027`–`$d02e`. Eight sprites exactly: ship (0), bullet (1), six enemies (2–7).
- Screen RAM `$0400` and colour RAM for the HUD readouts and the row-12 banners.
- `$d012` polled for frame sync; `$d020`/`$d021` for border and background.
- Joystick port 2 at `$dc00`.
- SID, two voices.
- An 8-bit LFSR at `$32` for spawn columns.

**Deliberately avoided,** and where each is reserved:

- Custom charsets and tile maps — Maze Raider (rung 2).
- Interrupt-driven raster splits — Night Raid (rung 3). Starfield polls `$d012`; it does not take the interrupt.
- Smooth hardware scrolling — Velocity (rung 4).
- Sprite multiplexing — Hornet (rung 5).
- Bitmap mode, and music beyond the two SFX voices.

**The sprite budget is the real ceiling.** Eight hardware sprites, minus the ship and the bullet, leaves six — which is why the swarm caps at six, and why the summit is every sprite the C64 has, on screen together.

## Section 6: Visual Direction

Single-colour hardware sprites on a black field: white ship, green enemies, white bullet. A parallax starfield drifts behind everything and keeps drifting in every state, including the title and both endings — white for the near layer, greys for the far ones. HUD readouts sit in the screen corners: a four-digit BCD score, the lives count, and a single-digit wave readout `W`.

Banners are nine characters at row 12, column 16 (`$05f0`): `GAME OVER`, and now `ALL CLEAR`. The two are the same length by design, so the victory routine is a structural twin of the one the learner already wrote.

## Section 7: Audio Direction

SID, two voices, no music engine.

- **Voice 1** — the laser on fire, the wave-advance chirp, *Twinkle Twinkle, Little Star* under the title, and the victory sting, written as a resolution of that title motif and not as new material.
- **Voice 2** — noise-waveform explosions, and the sting on a life lost.

No sampled audio, no three-voice music, no MOD-style playback.

## Section 8: Level Design Direction

There are no levels. The curve is the level design.

- **Waves 1–8 — an endless stream.** Ten kills clears a wave. Fall speed comes from a five-entry table that clamps at 3px per frame; the swarm grows from three enemies to six, one more every other wave; from wave 7 the homing tightens.
- **Wave 9 — the summit.** A finite cohort of six at full speed and full pull. A killed enemy stays dead and decrements `remaining`; an enemy that reaches the bottom still wraps to the top and must be shot. Clear all six and the game is won.

**The asymmetry between those two respawn paths is deliberate.** Suppressing both would let a player win by dodging and never firing, so only the kill path is made terminal. The cohort is finite by kills, not by time.

## Section 9: Polish Direction

Title screen with its jingle and a fire debounce (`ui_lock`), so a held button cannot skip it. A dwell on both endings so they land before fire returns to the title. Explosions burn as a white flash that is excluded from both collision tests while it lasts, so a dying enemy can neither be re-hit for points nor kill the ship. Ninety frames of invulnerability after a life is lost, so there is no spawn-camping death loop. A play-again loop from either ending.

## Section 10: Anti-goals

- **No boss.** A mothership finale was considered and rejected: it is a second concept for a closing unit, and bosses are spoken for later on the track.
- **No score-based win.** The score is a record, not a goal.
- **No endless mode after the win.** The summit is the point.
- No scrolling, no multiplexing, no tile maps, no charset work.
- No combat depth — one bullet in flight, one button.

## Section 11: Phase Trajectory

| Phase | Units | Hours | What ships |
|---|---|---|---|
| **Ignition** | 1–16 | 16–24 | The whole arcade loop, from a sprite on screen to a title screen: movement, screen edges, firing, enemies, collision, explosions, score, waves, death, three lives, the starfield, the title. |
| **The Curve** | 17–18 | 2–4 | Unit 17 repairs the jeopardy — LFSR spawn across the full field, 9-bit collision, homing, and a curve that keeps bending past the speed table. Unit 18 gives the curve a top: the finite ninth wave and `ALL CLEAR`. |

## Section 12: Ship Test (Multi-axis)

Per phase, all five axes. Verification is emulator-based; real-hardware verification is suspended per [commercial-bar-revamp.md](../../../../decisions/commercial-bar-revamp.md).

**Ignition**

- **Code:** every unit assembles (Asm198x, acme dialect); the ship steers crisply; bullet-versus-enemy collision is correct in both 9-bit halves; passes the Definition of Done.
- **Visuals:** sprites read cleanly against the drifting starfield; the HUD is legible; magazine-screenshot test met on a mid-wave still.
- **Audio:** laser and explosion present, mixed so neither masks the other.
- **Level design:** playable end to end; the wave curve rises in even steps from the opening wave, with no jump a first-time player cannot read.
- **Polish:** title, game over, three lives, play-again loop; no soft-locks, no crashes.

**The Curve**

- **Code:** the LFSR spreads spawns wider than the 16px hit tolerance; both collision tests are 9-bit aware; `remaining` cannot underflow; passes the Definition of Done.
- **Visuals:** six enemies plus ship and bullet render together without sprite loss; `ALL CLEAR` occupies the same slot as `GAME OVER`.
- **Audio:** the wave chirp and the victory sting are present, and the sting resolves the title motif.
- **Level design:** **winnable by scripted run** per the per-game winnability gate. The win script pokes `wave` to 9 and `remaining` to 1, then takes the final enemy with real fire input — an engineered setup driving real game logic. The loss script is re-verified against the rebuilt program. Both live in `capture/`. Neither the turret park nor a static right-side position survives.
- **Polish:** both endings dwell and return to the title; the win cannot be reached by dodging alone.

## Section 13: Pattern Library Extractions

- **framework** — frame sync by polling the raster register, giving every frame a fixed beam position. C64 in implementation; the idea generalises.
- **rendering** — hardware sprite setup and the 9th-bit X problem: positions past 255, and the EOR bit-flip that handles the wrap. C64-specific.
- **physics** — pseudo-random spawn from an 8-bit LFSR, deliberately spread wider than the collision tolerance so spawns cannot cluster inside it. Cross-platform.
- **framework** — homing toward a target column, rate-limited by frame parity so the pull is firm without being a lunge. Cross-platform.
- **framework** — flash-then-respawn: a dying enemy excluded from both collision tests while it burns. Cross-platform.
- **framework** — the terminal finite wave: an endless stream becomes a clearable cohort, which is what an ending is. Cross-platform.
- **ui** — multi-byte BCD score and a single-digit stage readout. Cross-platform.

## Section 14: Vault Tie-ins

All of these resolve today.

- *Space Invaders* — the clearable cohort the summit borrows (`vault/games/space-invaders`).
- *Galaxian* — descending attackers over a starfield (`vault/games/galaxian`).
- *Galaga* — escalating waves, and attackers that come for you (`vault/games/galaga`).
- VIC-II — sprites, the 9th X bit, the raster register (`vault/hardware/vic-ii`).
- SID chip — the two SFX voices and the title jingle (`vault/hardware/sid-chip`).
- 6510 — the CPU (`vault/hardware/6510`).
- Commodore 64 — the system (`vault/systems/commodore-64`).
- Random numbers — the LFSR (`vault/techniques/random-numbers`).
- Attract mode — the title screen and its jingle (`vault/techniques/attract-mode`).

## Optional: Risks

1. **The summit changes a shipped game.** *Mitigation:* never-regress — Starfield stays `complete` in the catalogue until the rebuilt program provably passes both the winnability gate and the Definition of Done, per [endpoint-first-authoring.md](../../../../decisions/endpoint-first-authoring.md) as amended 2026-07-01.
2. **The captures are blocked on tooling.** The win and loss runs need Emu198x built, and no binaries exist locally. The design does not depend on their outcome, but the gate cannot close until they run.
3. **Nine waves is a long run to script.** *Mitigation:* the gate permits engineered setups, so the win script pokes `wave` and `remaining` instead of playing out ninety kills.

## Anchored In

- [c64-assembly-lineup.md](../../../../decisions/c64-assembly-lineup.md) — rung and lineup position; the shipped anchors are locked.
- [commercial-bar-revamp.md](../../../../decisions/commercial-bar-revamp.md) — the Definition of Done and the per-game winnability gate.
- [a-game-needs-jeopardy.md](../../../../decisions/a-game-needs-jeopardy.md) — a fail state is constitutive; the mirror of the gap this brief closes.
- [constraint-position.md](../../../../decisions/constraint-position.md) — period-faithful, period-possible, modern scene.
- [incremental-construction-units.md](../../../../decisions/incremental-construction-units.md) — the cumulative `steps/` format unit 18 is built to.
- [october-2026-launch-spec.md](../../../../decisions/october-2026-launch-spec.md) — Starfield as half of the C64 finishable bar.
- [design-stress-2026-07-05.md](design-stress-2026-07-05.md) — the adversarial pass that found the game unlosable, and whose repairs landed in unit 17.

## Changelog

| Date | Change |
|---|---|
| 2026-07-26 | Written retrospectively. Records the game as shipped through unit 17 and the summit designed for unit 18 — wave 9 as a finite cohort, cleared by kills, ending in `ALL CLEAR`. Fills the gap the launch-readiness review found: Starfield shipped `complete` with no brief, so its win condition had no canonical home and its absence went unnoticed until the winnability gate was audited. |
