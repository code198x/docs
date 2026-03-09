# Nintendo NES Curriculum

**Platform:** Nintendo Entertainment System (NES / Famicom)
**Killer Feature:** PPU — tile-based graphics mastery
**Assembly Games:** 4
**BASIC Games:** None (no BASIC gateway — assembly from the start)
**Total Units:** 1,408

---

## Overview

The NES curriculum teaches 6502 assembly programming through four complete games. The sequence begins with the PPU — the heart of NES development — and progresses through battery-backed saves, mapper bank switching, and advanced scanline techniques until learners can produce commercial-quality cartridge ROMs.

The NES is fundamentally tile-based. Everything is 8×8 tiles: backgrounds built from pattern tables arranged in nametables, sprites limited to 64 objects with 8 per scanline. Understanding the PPU is understanding the NES. This curriculum embraces that architecture, teaching learners to think in tiles.

By the final game, learners will have skills matching professional NES developers of the late 1980s and early 1990s.

---

## Assembly Track

### Structure

| Game | Units | Phases | Units/Phase | Role |
|------|-------|--------|-------------|------|
| 1 | 128 | 8 | 16 | Accessible entry — PPU fundamentals through the NES's natural genre |
| 2 | 256 | 8 | 32 | Signature technique — battery SRAM, overworld/dungeon design |
| 3 | 512 | 16 | 32 | Ambitious — MMC3 mapper, large connected world |
| 4 | 512 | 16 | 32 | Capstone — advanced MMC3, DMC audio, multi-region support |
| **Total** | **1,408** | | | |

---

### Game 1: Scrolling Platformer

**Units:** 128 (8 phases)
**Genre:** Scrolling platformer
**Inspired by:** Super Mario Bros, Mega Man, DuckTales
**Working title:** Dash

**Concept:** Run, jump, and power-up through scrolling tile-based worlds. The NES was built for this — nametables provide the world, OAM sprites provide the characters, PPUSCROLL provides the camera. The learner has a character on screen in unit 1, jumping by unit 3, and the world scrolls by mid-game.

This game uses NROM (no mapper) — 32 KB PRG, 8 KB CHR. Everything fits in the cartridge's base configuration, teaching the learner to work within constraints before mappers expand them.

**Skills taught:**
- 6502 fundamentals (registers, addressing, zero page, stack)
- PPU setup (pattern tables, nametables, palettes, OAM)
- Background tile rendering (level layout via nametable writes)
- Sprite rendering via OAM DMA ($4014)
- Controller input ($4016/$4017)
- Gravity and jump physics (velocity, acceleration, variable height)
- Tile-based collision detection (metatiles, solid/empty/one-way)
- NES hardware scrolling (PPUSCROLL, nametable mirroring)
- Camera following with nametable seam management
- Player animation states (idle, run, jump, fall, climb)
- Enemy patterns (patrol, chase, projectile)
- Power-up system (abilities, health, temporary effects)
- APU sound basics (pulse, triangle, noise channels)
- Level data structures (metatiles, RLE compression)
- World structure (4 themed worlds, 4 levels each)
- Boss encounters
- Title screen, game-over, lives, score

**Why first:** Super Mario Bros defines the NES. A scrolling platformer teaches the PPU through its most natural use: tiles become platforms, sprites become characters, scrolling becomes the world opening up. NROM forces the learner to fit everything in 32 KB — a discipline that makes mapper-based games feel spacious by comparison.

---

### Game 2: Top-Down Adventure

**Units:** 256 (8 phases × 32 units)
**Genre:** Top-down adventure
**Inspired by:** The Legend of Zelda, StarTropics
**Working title:** Wyrdstone

**Concept:** Explore an overworld, enter dungeons, find items, defeat bosses. The world is a grid of interconnected screens; entering a dungeon transitions to a different tileset and layout. Items found in dungeons unlock new areas of the overworld. Combat is real-time: swing a sword, dodge enemies, use sub-weapons.

This game introduces battery-backed SRAM — the player's progress persists across power cycles. It also demonstrates that the NES is not just a platformer machine.

**Skills taught:**
- Screen-transition scrolling (push-scroll between screens)
- Overworld map structure (grid of screens, each a nametable)
- Dungeon structure (separate tileset, room-based layout)
- Tileset switching between overworld and dungeons
- Real-time melee combat (sword swing, hit detection, knockback)
- Enemy AI variety (patrol, chase, ranged attack, boss patterns)
- Item system (sword upgrades, shield, sub-weapons, keys)
- HUD design (health hearts, item display, rupee/key counts)
- Battery-backed SRAM ($6000-$7FFF) for save files
- Save/load system with multiple slots
- NPC interaction (text display, item shops)
- Puzzle elements (push blocks, switches, locked doors)
- APU music (overworld theme, dungeon theme, boss theme)
- APU sound design (sword slash, item collect, enemy hit, door open)
- Palette animation (water shimmer, torch flicker)
- 5+ dungeon themes with unique enemies and bosses
- Progressive item gating (items unlock overworld areas)

**Why here:** The Legend of Zelda proved the NES could sustain worlds beyond linear levels. This game teaches fundamentally different skills from the platformer: screen-based navigation instead of scrolling, real-time combat instead of jumping, and persistent state via battery SRAM. The overworld/dungeon duality teaches tileset management — a skill that pays off massively when mappers provide more CHR banks in Game 3.

---

### Game 3: Metroidvania

**Units:** 512 (16 phases × 32 units)
**Genre:** Metroidvania
**Inspired by:** Metroid, Castlevania III, Kid Icarus
**Working title:** Abyssal Gate

**Concept:** Explore a massive interconnected world. Acquire abilities that open new areas. Backtrack through familiar rooms that now reveal hidden paths. The world is too large for the cartridge's base configuration — this game introduces the MMC3 mapper, with bank switching for PRG code and CHR graphics, and a scanline counter for split-screen effects.

Five regions, each with a distinct visual theme, tileset, enemy set, and boss. The player acquires 8+ abilities (wall jump, double jump, dash, morph, charge beam, missiles, bombs, grapple) that gate progression through the world. Multiple endings based on completion percentage and time.

**Skills taught:**
- MMC3 mapper setup and bank switching
  - PRG bank switching (8 KB switchable banks)
  - CHR bank switching (multiple tilesets per region)
  - Scanline counter (IRQ at specific scanline for screen splits)
- Large world design (5 regions × 40+ rooms)
- Non-linear progression with ability gating
- Ability system (8+ movement and combat abilities)
- Backtracking design (old areas reveal new paths with new abilities)
- Map system with fog of war (explored vs. unexplored)
- Minimap display using scanline IRQ for HUD split
- Advanced enemy AI (region-specific behaviours, mini-bosses)
- Boss design (5 major bosses granting abilities, multi-phase patterns)
- Environmental storytelling (background details, item placement)
- Advanced APU music (per-region themes, boss themes, ambient tracks)
- DMC sample introduction (bass drums, impact sounds)
- Battery-backed SRAM with multiple save slots
- Percentage tracking and multiple endings
- Sprite management under 8-per-scanline limit (flicker, priority)
- Scrolling within rooms (some rooms wider/taller than one screen)
- Room transition effects
- Sequence breaking consideration (designing for creative players)

**Why here:** Metroid shows what bank switching enables: a world too large for the cartridge to hold at once. The MMC3's scanline counter allows a fixed HUD above a scrolling play area — a technique used by nearly every late-era NES game. Building a Metroidvania teaches level design at a scale the first two games couldn't reach, and the ability-gating design forces the learner to think about world structure in ways that linear games never demand.

---

### Game 4: Capstone

**Units:** 512 (16 phases × 32 units)
**Genre:** Multi-style action game with late-era NES polish
**Inspired by:** Kirby's Adventure, Batman: Return of the Joker, Little Samson
**Working title:** Starweave

**Concept:** A weaver's apprentice climbs through five realms to repair the sky-loom where constellations are woven. Each realm has a distinct gameplay style: forest platforming, underwater swimming, wind-affected gliding, mechanical puzzle-solving, and vertical star-thread weaving. CHR animation for flowing water and shimmering thread. Advanced DMC for sampled bass and voice. Cinematic cutscenes between realms. The NES pushed to Kirby's Adventure levels of visual and audio polish.

The capstone's new material is production polish: NTSC/PAL compatibility, advanced MMC3 techniques, professional ROM image creation, and the kind of visual/audio polish that characterised the NES's final commercial years.

**Skills taught:**
- All techniques from Games 1-3 at mastery level
- Advanced MMC3 techniques (mid-frame bank switching, CHR animation)
- CHR bank switching for animated backgrounds (waterfalls, fire, machinery)
- Multiple gameplay modes within one game (varied section types)
- Advanced DMC audio (sampled bass, percussion, voice clips)
- Full APU soundtrack with DMC integration
- NTSC/PAL detection and adaptation (timing, speed, music pitch)
- Scanline effects (parallax via IRQ timing, water reflections)
- Advanced sprite techniques (large metasprite bosses, flicker management)
- Cinematic sequences (cutscenes using nametable animation)
- Professional ROM image layout and bank organisation
- Memory management across PRG banks (code, data, music, levels)
- Difficulty balancing and playtesting methodology
- Credits sequence with scrolling text and graphics
- Title screen with attract mode / demo playback
- Testing across configurations (NTSC, PAL, various emulators, flash carts)

**Why last:** The capstone proves the learner can produce a game matching the quality of the NES's final commercial years — games like Kirby's Adventure that squeezed extraordinary results from familiar hardware. The multi-style gameplay prevents it from being "another platformer" while the NTSC/PAL support, advanced CHR animation, and DMC audio represent techniques that only appeared in the most polished late-era releases.

---

## Changelog

- **v4.0 (2026-03-09):** Major restructure. Reduced from 16 to 4 assembly games. No-repetition rule across primary platforms. Every game inspired by a real commercial release. Previous 16-game curriculum preserved in game outline files for reference.
- **v3.0 (2026-01-18):** Initial 16-game curriculum.
