# Commodore 64 BASIC V2 Curriculum

**Platform:** Commodore 64
**Language:** BASIC V2 (stock, no extensions)
**Games:** 4
**Total Units:** 256 (4 × 64)

---

## Overview

The C64 BASIC V2 curriculum teaches programming fundamentals through four complete games. Each game is completable in under 500 lines of stock BASIC V2. No Simons' BASIC, no cartridge extensions — just what shipped in every C64's ROM.

BASIC V2 has no graphics commands, no sound commands, no sprite commands. Everything is PEEK and POKE. This is the lesson — and the bridge. Every POKE writes to a hardware register. Every PEEK reads one. By the end of this track, the learner understands memory-mapped I/O not as an abstract concept but as the thing they've been doing all along. The transition to assembly becomes "same registers, faster access."

BASIC is not a prerequisite for the assembly track. The two tracks are independent.

---

## Structure

| Game | Units | Role |
|------|-------|------|
| 1 | 64 | First program — grid strategy game using PRINT and INPUT |
| 2 | 64 | Screen memory — character grid action via POKE |
| 3 | 64 | VIC-II — sprite game via hardware register POKEs |
| 4 | 64 | SID — music + game combining sound and gameplay |
| **Total** | **256** | |

Each game has 4 phases of 16 units. Each unit is 60-120 minutes and produces a working result.

The progression mirrors the hardware: pure BASIC → screen RAM → VIC-II sprites → SID sound. Each game adds a layer of hardware interaction.

---

## Game Sequence

### Game 1: Grid Strategy Game

**Units:** 64 (4 phases × 16 units)
**Genre:** Grid-based strategy
**Inspired by:** Battleships, Minesweeper, magazine strategy type-ins

**Concept:** A grid-based strategy game where the player types coordinates and the screen reveals information. Battleships: call out grid references, hit or miss, sink the fleet. Or Minesweeper: uncover cells, count adjacent mines, flag dangers. The game has replay value, genuine decision-making, and needs nothing beyond PRINT, INPUT, and arrays. A real game from line 1, no POKE required.

**Skills taught:**
- C64 BASIC environment and screen editor
- Variables (numeric and string)
- PRINT and INPUT statements
- IF/THEN logic and relational operators
- FOR/NEXT loops
- Arrays (DIM) for grid state
- RND for randomisation
- GOSUB/RETURN for subroutines
- Game state tracking (hits, misses, remaining targets)
- Grid display formatting (TAB, SPC, cursor positioning)
- Two-player mode (alternating turns)
- Difficulty levels (grid size, number of targets)
- Win/lose conditions and replay prompt

**Why first:** A strategy game is immediately engaging — real decisions, real consequences — without needing any knowledge of C64 hardware. The learner focuses entirely on programming logic: loops, conditionals, arrays, subroutines. The game works on any computer with BASIC, but the C64's screen editor makes editing comfortable. POKE comes in Game 2; for now, pure BASIC.

---

### Game 2: Character Grid Action Game

**Units:** 64 (4 phases × 16 units)
**Genre:** Character grid action (maze or chase)
**Inspired by:** Compute!'s Gazette type-ins, magazine action games

**Concept:** A maze or chase game where everything is POKE. The player moves through a character-based world — POKE 1024+offset, charcode puts a character on screen. POKE 55296+offset, colour colours it. PEEK(1024+offset) reads what's there — wall, enemy, or collectible. The game looks like a Compute!'s Gazette type-in: colourful character graphics, responsive controls, satisfying gameplay.

**Skills taught:**
- Screen RAM ($0400-$07E7) — 40×25 character grid
- Colour RAM ($D800-$DBE7) — per-character colour
- POKE for writing screen and colour memory
- PEEK for reading screen state (collision detection)
- CHR$ codes for character graphics (hearts, diamonds, blocks, arrows)
- Border and background colour ($D020, $D021)
- Joystick reading via PEEK(56320) — CIA port 2
- Coordinate calculation (row × 40 + column)
- Game loop with joystick input
- Simple enemy AI (move toward player, random patrol)
- Maze generation or level data in DATA statements
- Score display via POKE to specific screen positions
- Lives, game-over, level progression
- Speed considerations (POKE is faster than PRINT for positioned output)

**Why here:** This is where the C64's personality appears. POKE 1024,81 puts a ball on screen — the learner is writing to hardware memory for the first time. PEEK reads it back — collision detection is just "what's at this memory address?" The joystick (PEEK 56320) introduces hardware input. Every concept maps directly to what the assembly track does with LDA/STA instead of PEEK/POKE.

---

### Game 3: Sprite Game

**Units:** 64 (4 phases × 16 units)
**Genre:** Sprite-based action game
**Inspired by:** Type-in sprite games, simple shooters

**Concept:** A game using VIC-II hardware sprites, controlled entirely through POKE. Enable sprites (POKE 53269), set X/Y positions (POKE 53248+n), define shapes via sprite data pointers, detect collisions (PEEK 53278). Design sprites using DATA statements — 63 bytes of pixel data per frame. The game has real sprites that move smoothly over the background, but updating everything from BASIC is visibly slow. That tension is the point.

**Skills taught:**
- VIC-II sprite registers:
  - Enable ($D015 / 53269)
  - X/Y position ($D000-$D00F / 53248-53263)
  - X high bit ($D010 / 53264)
  - Colour ($D027-$D02E / 53287-53294)
  - Multicolour mode ($D01C / 53276)
  - Expand X/Y ($D017, $D01D)
  - Sprite-sprite collision ($D01E / 53278)
  - Sprite-background collision ($D01F / 53279)
- Sprite data pointers (bank offset + block number)
- Sprite shape design using DATA statements
  - 24×21 pixels = 63 bytes per frame
  - Binary/decimal conversion for rows
- Animation via pointer switching (multiple frames)
- Smooth sprite movement (sub-character-cell precision)
- Bullet sprites (limited count, recycling)
- Enemy sprite patterns
- Combining sprites with character background
- The speed problem: BASIC can't update 8 sprites and run game logic at 50fps

**Why here:** Hardware sprites are the C64's magic — smooth, colourful, independent of the background. But controlling them from BASIC exposes the interpreter's limitations starkly: the sprites glide smoothly (hardware handles that) but the game logic crawls. The learner experiences both the power of memory-mapped hardware and the cost of an interpreted language. Every register they POKE here is the same register they'll STA in assembly.

---

### Game 4: Music + Game

**Units:** 64 (4 phases × 16 units)
**Genre:** Action game with SID sound
**Inspired by:** Games with SID music, magazine music programs

**Concept:** A game that combines gameplay with SID sound — shooting triggers attack sounds, collecting items plays melodies, background music runs throughout. All audio is via POKE to SID registers ($D400-$D418). The game demonstrates both the SID's extraordinary capability (three voices, filters, ADSR envelopes) and BASIC's inability to do it justice in real-time. A simple melody plays while the game runs; attempting complex music while handling input shows exactly where BASIC breaks down.

**Skills taught:**
- SID register layout ($D400-$D418 / 54272-54296):
  - Frequency (low/high bytes per voice)
  - Pulse width (for pulse waveform)
  - Control register (waveform select, gate bit)
  - Attack/Decay, Sustain/Release (ADSR envelope)
  - Filter cutoff, resonance, filter mode
  - Volume ($D418 / 54296)
- Three independent voices
- Waveform types (triangle, sawtooth, pulse, noise)
- ADSR envelope design (sharp attack for percussion, slow release for pads)
- Playing notes by frequency (lookup table in DATA)
- Sound effects (laser, explosion, collect, death)
- Simple music playback via timer loop
- Filter control (low-pass, high-pass, band-pass)
- Combining music and sound effects (voice allocation)
- The timing problem: music requires regular updates that BASIC can't guarantee during gameplay
- Music data format (note, duration, voice assignments)
- Why interrupt-driven music (assembly) solves the timing problem

**Why last:** The SID is the C64's soul. This game teaches its registers, its capabilities, and its potential — while honestly demonstrating that BASIC can't keep up. Playing a melody while handling joystick input and updating game state produces audible glitches as the interpreter falls behind. This is not a failure — it's the motivation. The learner understands exactly what assembly's interrupt-driven music routines will solve, because they've felt the problem firsthand.

---

## Changelog

- **v4.0 (2026-03-09):** Major restructure. Reduced from 8 to 4 games. Standardised to 64 units per game (256 total). Each game targets under 500 lines. Progression reframed around hardware layers: pure BASIC → screen RAM → VIC-II → SID. Previous 8-game curriculum preserved in game outline files for reference.
- **v3.0 (2026-01-18):** Initial 8-game curriculum.
