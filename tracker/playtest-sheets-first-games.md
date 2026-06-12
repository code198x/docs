# Playtest sheets — the four first games (2026-06-12)

All four game 1s are script-verified to their win states (the winnability gate), but
scripts prove mechanics, not feel. These sheets are for the human pass: what to play,
what to feel for, and which numbers are already data when something feels wrong.

**How to file findings:** tuning issues → table/constant edits in the game's final unit
(cheap by design — that's what the tables were for), re-run the checked-in win script
after any change. Wants-a-new-mechanic findings → the game-2 briefs, not retrofits.

---

## Flock (Amiga) — `code-samples/commodore-amiga/assembly/flock/unit-18/flock.adf`

Run: `emu198x-amiga --disk flock.adf`. Joystick port 2 / gamepad.

Feel for:
- **The buffered hop.** Tap mid-cooldown — the hop should serve the instant she's ready,
  *never* double-fire, and a banked right-hop must actually go right. Try deliberately
  drumming the stick.
- **Rides.** Boarding the bale and the duck — does the carry feel locked-on? Does the
  duck's dive telegraph (the warning frame) read in time at level 2+?
- **The nerve system.** Does the tremble read as "she's frightened" or as flicker? Is the
  bolt threshold fair at level 3?
- **The black sheep gamble.** Are you tempted? (If never: bonus too small or risk too
  large.)
- **The curve.** Levels 2–4: which one is the wall? Does level 4 repeating feel like a
  plateau or a grind?
- **Audio.** Does the jingle survive five title visits? Sting lengths vs the dwell.

Tunable data: `leveltab` rows (lane speeds 16.16, duck stamina, nerve threshold),
`WINWAIT`/`ENDWAIT`, `SKITTISH`, `BLACK_BONUS`, `SHEPHERD_BONUS`, hop cooldown.

## Gloaming (Spectrum) — `code-samples/sinclair-zx-spectrum/assembly/gloaming/unit-21/steps/step-01.asm`

Run: assemble to `.sna`, load in Fuse or `emu198x-spectrum`. Keys QAOP + Space.

Feel for:
- **Held-key movement speed.** Movement is one cell per frame while held — at 50 Hz, is a
  held key controllable or a wall-magnet? (Scripts only ever tapped. A human will hold.)
- **The draught.** `DRAUGHT_SPEED 8` (one cell per 8 frames) — menace or wallpaper?
- **Three phrases.** Chime/fanfare/sting pitch and length — the blocking pauses should
  feel like punctuation, not lag.
- **The lock.** `LOCK 25` after each screen — long enough to stop accidental skips, short
  enough not to feel deaf?

Tunable data: `DRAUGHT_SPEED`, `LIVES`, `LOCK`, the phrase tables' `B`/`C` pairs,
lamp positions in `lamp_data`.

## Starfield (C64) — `code-samples/commodore-64/assembly/starfield/unit-17/steps/step-02.prg`

Run: `emu198x-c64 --load step-02.prg` (or VICE). Joystick port 2.

Feel for:
- **The wave ramp.** Wave 1→2 doubles the fall speed — cliff or curve? Where do *you* die?
- **The spawn column.** Enemies cluster in a narrow x band (raster-seeded spawns under a
  frame-locked loop are nearly constant). Does it read as a pattern to exploit (fine,
  arcade-y) or as a bug (needs a stirred seed — note for a tuning pass)?
- **Parking.** The turret strategy (sit in the column, hold fire) — dominant or just
  viable? Dominant might want spawn stirring or a dive behaviour in game 2.
- **The dwell.** Death with fire held: does GAME OVER hold long enough to read?
- **The jingle.** Twinkle Twinkle over repeated visits — charming or grating?

Tunable data: `wave_speed_tbl`, `WAVE_TOP`, kills-per-wave (the `cmp #10`), `ui_lock`
loads (60/25), jingle durations, ship speed (2 px/frame).

## Dash (NES) — `code-samples/nintendo-entertainment-system/assembly/dash/unit-17/dash.nes`

Run: `emu198x-nes --rom dash.nes` (needs a UI build) or any NES emulator. Pad 1.

Feel for:
- **The jump.** Fifteen-pixel carry, spike now needs ~8px precision — tight-but-fair or
  trial-and-error? (This is the game's core verb; if it feels bad, everything does.)
- **The route.** Coin → platform → wall → coin: does a level loop stay fun on the third
  lap, or is it a chore? (If chore: game 2's scrolling world is the answer, not more
  retrofits.)
- **The grace window.** 60 frames, blinking — does it read? Do you understand why you
  survived?
- **The curve.** Level 2's obstacle at 3 px/frame, level 4 at 4 — where's the wall?
- **Audio.** Camptown on loop; fanfare vs sting lengths.

Tunable data: `level_speed_tbl`, `LEVEL_TOP`, `hurt_timer` load (60), blink bit, phrase
tables, `OBSTACLE_SPEED` baseline, spike position in `level_ground_spike_row`.

---

After the pass: tuning edits land per game with the win script re-run (the gate applies
after any mechanics/tuning change — see the winnability gate in
[`decisions/commercial-bar-revamp.md`](../decisions/commercial-bar-revamp.md)).
