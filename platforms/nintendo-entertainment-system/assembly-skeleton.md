# Nintendo Entertainment System Track — Lightweight Skeleton

**STATUS: Post-October work, lightweight only.** Per `docs/decisions/october-2026-launch-spec.md`, NES / Nightshade is deferred. This skeleton is *no-commit* — North Star, volume themes, candidate game lineup only. No per-game scope, no naming lock-in, no tech-tree detail. Awaits Spectrum methodology validation before becoming a full track structure.

Captured 2026-05-19 alongside [c64-track-skeleton.md](c64-track-skeleton.md) and [amiga-track-skeleton.md](amiga-track-skeleton.md) for cross-platform methodology check.

## North Star

The NES teaches the *console game* — the dedicated platform that does one thing (play games) and does it with hardware optimised for tile-based action. Where Spectrum and C64 were home computers running games among other tasks, **NES was a games-only machine**. The design vocabulary is hardware sprites + tile maps + scrolling backgrounds + an APU built for music + a controller built for games. Mapper chips on cartridges extend memory transparently — the player doesn't see them but the developer designs around them. 60Hz NTSC pacing is faster than 50Hz PAL. The Famicom Disk System and PAL/NTSC variants add platform-internal complexity.

Nightshade (Game 1, concept locked per [revamp.md](revamp.md)) is the canonical demonstration.

## Volume themes (working-draft)

| Volume | Theme | What it teaches |
|--------|-------|-----------------|
| **V1** *The Tile and the Sprite* | Foundational | PPU fundamentals — name tables, sprites, attributes, palette |
| **V2** *Side-Scrolling Worlds* | Platformer | Mario / Castlevania / Mega Man tradition |
| **V3** *Action and Adventure* | Combat-led | Ninja Gaiden / Zelda / Metroid / Contra |
| **V4** *Console RPG* | Long-form | Final Fantasy / Dragon Quest / Crystalis tradition |

## Candidate games (~16, working-draft)

| # | Working name / placeholder | Canonical tradition |
|---|----------------------------|---------------------|
| 1 | **Nightshade** (concept locked) | TBD per concept doc |
| 2 | [Single-Screen Platformer] | Donkey Kong / Mario Bros. (NES) |
| 3 | [Side-Scrolling Platformer] | Super Mario Bros. (Nintendo 1985) |
| 4 | [Sword-and-Monster Platformer] | Castlevania (Konami 1986) |
| 5 | [Robot-Master Action] | Mega Man (Capcom 1987) |
| 6 | [Open Exploration Platformer] | Metroid (Nintendo 1986) |
| 7 | [Overworld + Dungeons] | The Legend of Zelda (Nintendo 1986) |
| 8 | [Console RPG] | Final Fantasy / Dragon Quest (Square / Enix 1986-87) |
| 9 | [Kinetic Action] | Ninja Gaiden (Tecmo 1988) |
| 10 | [Run-and-Gun] | Contra (Konami 1987) |
| 11 | [Fighting / One-on-One] | Punch-Out!! (Nintendo 1987) |
| 12 | [Top-Down Racing] | Excitebike (Nintendo 1984) |
| 13 | [Multi-Genre Extreme] | Battletoads (Rare 1991) |
| 14 | [Falling-Block Puzzle] | Tetris NES (Nintendo 1989) |
| 15 | [Single-Screen Puzzle] | Solomon's Key (Tecmo 1986) |
| 16 | [Continuous-Scroll Platformer] | Adventure Island (Hudson 1986) |

Plus possible additions: Bubble Bobble NES, Bionic Commando, R-Type NES port, Kid Icarus (mapper-rich), Crystalis (RPG with NES sound mastery), Duck Hunt (light-gun).

## Methodology generalisation check (Spectrum → NES)

| Spectrum element | Translates to NES? |
|------------------|---------------------|
| **Trunk Layers 1-4** | Different shape — NES doesn't have a software-sprite era. Trunk would be: PPU + name-tables, hardware sprites + DMA, scrolling backgrounds, mapper basics. Same depth of intro, different content. |
| **Branch A** (Adventure Depth) | Yes — Zelda, Metroid, Crystalis |
| **Branch B** (Platformer) | **Massively expanded** — NES platformer canon is enormous. Mario, Castlevania, Mega Man, Metroid, Kid Icarus, Adventure Island, Battletoads, Bionic Commando... Branch B may be the *biggest* branch on NES |
| **Branch C** (Scrolling and Density) | Hardware-supported on NES. Different teaching — APU + PPU make scroll free; design is about *what you do with* free scroll |
| **Branch D** (Real-World Sim) | Less prominent on NES — sport games exist but the platform was less sim-focused |
| **Branch E** (True 3D) | Minimal on NES — 3D was very rare. Maybe Battlezone-style |
| **Branch F** (Cross-cutting Specials) | Different — NES has cartridge-chip variants (MMC1-5, etc.) as cross-cutting concerns |
| **Branch G** (Audio Hardware) | **Different content** — APU (2 pulse + triangle + noise + DPCM) replaces SID/AY/beeper. C64-style hardware audio but with different specifics |
| **Three cross-cutting axes** | Engineering Practices content is 6502-specific (similar to C64 — close-but-different to Z80 idioms). Production Craft includes cartridge mapper handling, EEPROM saves, region differences (NTSC/PAL) |
| **Layer model** | Different — NES has no L+1 128K equivalent. Possible L+1 = expansion-audio mappers (VRC6, etc.). Possible L+4 = modern homebrew scene tooling (NESDev) |
| **Naming convention** | Yes — applies universally |

**Methodology generalises conceptually but with different per-axis content.** Trunk Layers may need substantial rework — NES doesn't have a "software sprite primer" phase, so the foundational ramp is different. Branch B is much heavier. Branch D less prominent. Branch G has APU-specific content. **NES needs the most adaptation of the three platforms.**

## What this skeleton does NOT commit to

(Same as C64 — see [c64-track-skeleton.md](c64-track-skeleton.md))

## Status

Skeleton — captured 2026-05-19. Post-October work. No commitment. Awaits Spectrum methodology validation before becoming a full track structure document.
