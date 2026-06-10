# Decision: C64 BASIC — Volumes 2–4 lineup

> **STATUS: Active.** Accepted 2026-06-10 as part of the 2026 lineup replan. Records the
> coming-soon lineup appended after the shipped Volume 1. Volume 1 (the `meet-c64-basic` primer
> + 8 First Programs) is **locked** and untouched. Counts are flexible (no fixed unit counts);
> names are working titles pending the [inspired-by-not-clones-naming.md](inspired-by-not-clones-naming.md)
> pass. The catalogue is authoritative
> (`website/src/content/modules/commodore-64/basic.yaml`).

## The decision

C64 BASIC climbs **two ladders at once**, and that is what makes the track its own thing
(distinct from Spectrum BASIC, which teaches the same portable concepts):

- a **concept ladder** — the portable programming ideas (output → variables → decisions → loops →
  arrays → state → real-time → data → maths → persistence), shared with every BASIC track; and
- a **POKE-the-hardware ladder** — turning the bare Commodore BASIC v2 into a games machine. CBM
  BASIC gives you no `SPRITE`, no `SOUND`, no `PLOT`; the C64's fame (16 colours, hardware sprites,
  the SID, smooth scroll, raster effects) is all reached by writing numbers into memory with POKE
  and reading them back with PEEK. Sequencing that as a first-class spine keeps the
  one-new-poke-per-game promise honest.

Volume 1 already started both (screen POKE in Skyline, the jiffy clock in Reflex, SID-as-a-voice in
Bleeper, the joystick in Rover). Volumes 2–4 deepen each rung deliberately, one new capability per
game.

## Lineup (appended as coming-soon)

**Volume 2 — Boards and Sprites** (grids, strings, the first real sprites):
Gridlock (2D arrays) · Codebreaker (strings) · **Meet the VIC-II** (teaching) · Glyph (custom
characters, H4) · Skater (hardware sprites, H5 — the headline) · Nibbler (state machines) · Bouncer
(sprite collision, H6) · Treasure Map (READ/DATA) · Quizmaster (menus).

**Volume 3 — Worlds and Sound** (motion maths, full SID, raster):
Vectors (SIN/COS) · Cascade (gravity over a grid) · Soundsmith (full SID, H7) · Raster (raster reads,
H8) · Defender Lite (many sprites + readout) · Dungeon (procedural data + inventory) · Trackside
(pseudo-3D) · Showtime (mini-game collection).

**Volume 4 — Systems and Saves** (persistence, scrolling, the capstone):
Smooth Pt 1/2 (smooth scrolling, H9 → multi-screen world) · Vault Pt 1/2 (persistence → full
state save) · Arena (two-sprite combat) · Conductor (SID-synced gameplay) · Builder (save-backed
sandbox) · Showpiece (capstone — integrates everything).

## Key choices

- **A "Meet the VIC-II" teaching module opens the hardware run** (before Glyph/Skater). The shipped
  Volume 1 taught hardware *inside* games; the VIC-II sprite/charset model is heavy enough to earn a
  short `kind: teaching` module, mirroring how `meet-c64-basic` opens the track. (Confirmed
  2026-06-10.)
- **Custom characters (H4) before hardware sprites (H5).** A redefined-char *background* (Glyph)
  exists before the first sprite (Skater) moves over it.
- **Hardware sprites (H5) land as early as the language allows** (Skater, Volume 2). By then the
  learner has grids and the joystick loop, so sprites add *one* thing (the memory-mapped sprite
  registers), not six.
- **Smooth scrolling (H9) is deliberately last** (Volume 4) — the C64's Amiga-envy effect, reached
  only once every sprite/char/collision/raster rung below it is owned.
- **~8 games per volume** mirrors the shipped Volume 1 and the Spectrum BASIC lattice, but the budget
  is *one new thing per game*, not a count.

## Still open

- **Working titles** — Skater, Defender Lite, Builder are placeholders pending the naming pass.
- **Volume 4 split pairs** (Smooth, Vault) — borrowed from the Spectrum BASIC tour-then-deepen
  pattern; confirm at build time whether those games want splitting or stay single.
- **Showtime as a mini-game collection** — sanctioned by [modules-not-games.md](modules-not-games.md),
  but watch the genre ceiling before it wants splitting.

## Provenance

Applied from `docs/tracker/lineup-replan/c64-basic.md` (the reviewed proposal). Reconciliation
against binding records found C64 BASIC clean (pure append; no shipped module reordered or dropped;
no stub-scaffold debt — unit files exist only for the 9 shipped modules).
