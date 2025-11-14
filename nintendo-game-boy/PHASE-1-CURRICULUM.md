# Phase 1 Curriculum: Sharp SM83 Assembly + Hardware Fundamentals (Lessons 1-256)

> **⚠️ STRUCTURED:** This curriculum uses granular documentation files for better organisation and context efficiency.

## Primary Documentation

**Start here:** [`phase-1/overview.md`](phase-1/overview.md)

This provides the Phase 1 overview with philosophy, structure, and learning outcomes for Game Boy assembly development.

## Detailed Documentation

| What you need | Where to find it |
|---------------|------------------|
| **Tier 1 details** (Pocket Platformer, L1-32) | [`phase-1/tier-1/README.md`](phase-1/tier-1/README.md) |
| **Tier 2 details** (Block Fall, L33-64) | [`phase-1/tier-2/README.md`](phase-1/tier-2/README.md) |
| **Tier 3 details** (Circuit Race, L65-96) | [`phase-1/tier-3/README.md`](phase-1/tier-3/README.md) |
| **Tier 4 details** (Crystal Quest, L97-128) | [`phase-1/tier-4/README.md`](phase-1/tier-4/README.md) |
| **Tier 5 details** (Flipper Pro, L129-160) | [`phase-1/tier-5/README.md`](phase-1/tier-5/README.md) |
| **Tier 6 details** (Cave Explorer, L161-192) | [`phase-1/tier-6/README.md`](phase-1/tier-6/README.md) |
| **Tier 7 details** (Monster Trainer, L193-224) | [`phase-1/tier-7/README.md`](phase-1/tier-7/README.md) |
| **Tier 8 details** (Puzzle Link, L225-256) | [`phase-1/tier-8/README.md`](phase-1/tier-8/README.md) |
| **Individual lesson specs** | [`phase-1/tier-{1-8}/lesson-NNN.md`](phase-1/) |

## Why This Structure?

**Organised by tier and lesson**

**Benefits:**
- **60-70% less context** when working on specific lessons
- **Better organisation** with clear hierarchy (phase → tier → lesson)
- **Easier navigation** to find specific game or concept
- **Scalable** for all phases and platforms

## Game Boy-Specific Features

This curriculum highlights the Game Boy's unique characteristics:

- **Handheld gaming** - Design for short play sessions, battery efficiency
- **Sharp SM83 CPU** - Z80-like but with unique instruction set
- **4-shade LCD** - Creative use of limited palette (white, light grey, dark grey, black)
- **Hardware sprites** - 40 sprites via OAM, 10 per scanline
- **Tile-based graphics** - Background and window layers
- **Link cable** - Two-player connectivity (serial communication)
- **Save battery RAM** - Persistent save data in cartridge
- **Portable design patterns** - Quick saves, pick-up-and-play gameplay
- **Global success** - 118.7 million units sold, defining handheld gaming

## Curriculum Structure

### Phase 1: Sharp SM83 Assembly + Hardware Fundamentals (256 lessons)

**Total:** 256 lessons across 8 tiers
**Outcome:** 8 complete original games, assembly programming mastery, handheld game design expertise

### Tier Breakdown

**Tier 1 (L1-32):** Pocket Snake - First portable game
- First Game Boy assembly program
- Sharp SM83 fundamentals (registers, instruction set)
- ROM header and cartridge structure
- LCD control (LCDC register)
- Tile data and 4-shade optimization
- OAM sprite basics (snake head)
- D-pad input (handheld controls)
- **Playable:** Lesson 3 (move snake with D-pad)
- **Complete:** Lesson 7 (food, collision, high score in SRAM)
- **Pattern focus:** Assembly basics, tiles, sprites, handheld input
- **Game Boy showcase:** 4-shade graphics optimization, battery-efficient code

**Tier 2 (L33-64):** Shade Shift - 4-shade puzzle
- Puzzle game using all 4 LCD shades
- Match shades to clear blocks
- Shade-based mechanics (light beats dark, etc.)
- Creative use of limited palette
- Window layer for HUD (persistent score)
- **Playable:** Lesson 35 (match shades to clear)
- **Complete:** Lesson 39 (combos, level progression)
- **Pattern focus:** 4-shade optimization, palette manipulation, window layer
- **Game Boy showcase:** 4-shade LCD as gameplay mechanic, dithering techniques

**Tier 3 (L65-96):** Battery Quest - Save/resume adventure
- Action-adventure with multiple screens
- Collect items, unlock areas
- Battery-backed SRAM saves (MBC1/MBC3)
- Checksum validation for save data
- Resume exactly where you left off
- **Playable:** Lesson 67 (explore screens, collect items)
- **Complete:** Lesson 71 (save/load works, 5-10 screens)
- **Pattern focus:** Save battery RAM, checksums, screen transitions
- **Game Boy showcase:** Persistent saves, pick-up-and-play handheld design

**Tier 4 (L97-128):** Sprite Storm - 40 sprites, 10-per-scanline
- Shooter with MANY bullets/enemies
- Manage 40 sprite limit creatively
- 10-per-scanline limit (sprite priority)
- Sprite multiplexing techniques
- Visual feedback when hitting limits
- **Playable:** Lesson 99 (shoot with many sprites visible)
- **Complete:** Lesson 103 (waves, sprite management mastery)
- **Pattern focus:** OAM management, sprite limits, multiplexing
- **Game Boy showcase:** Hardware sprite limits as design challenge

**Tier 5 (L129-160):** Power Saver - Battery-efficient gameplay
- Game designed for maximum battery life
- Halt mode when waiting for input
- STOP mode for pause
- Efficient LCD updates (minimal VBlank work)
- Battery indicator mechanic
- **Playable:** Lesson 131 (gameplay with halt modes)
- **Complete:** Lesson 135 (full battery optimization, measurable efficiency)
- **Pattern focus:** HALT/STOP modes, battery efficiency, low-power programming
- **Game Boy showcase:** Battery life programming unique to handhelds

**Tier 6 (L161-192):** Quick Play - Short-session design
- Collection of 2-minute micro-games
- Perfect for handheld play bursts
- Auto-save after each game
- Track cumulative progress
- Designed for bus/train gaming
- **Playable:** Lesson 163 (2-3 micro-games work)
- **Complete:** Lesson 167 (5 micro-games, auto-save, progress tracking)
- **Pattern focus:** Short-session design, auto-save, handheld UX
- **Game Boy showcase:** Portable gaming philosophy, instant engagement

**Tier 7 (L193-224):** Link Battle - Two-player serial
- Simple two-player battle via link cable
- Serial I/O protocol (master/slave)
- Data synchronization between Game Boys
- Disconnect detection and recovery
- Turn-based combat or simultaneous action
- **Playable:** Lesson 195 (link cable communication works)
- **Complete:** Lesson 199 (full two-player game, sync, error handling)
- **Pattern focus:** Serial I/O, link cable protocol, synchronization
- **Game Boy showcase:** Link cable multiplayer unique to Game Boy

**Tier 8 (L225-256):** Sunlight Challenge - LCD contrast game
- Gameplay that works in various lighting
- High-contrast visuals for outdoor play
- Shade selection optimized for sunlight
- Visual clarity testing
- Bonus: Super Game Boy detection
- **Playable:** Lesson 227 (high-contrast gameplay works)
- **Complete:** Lesson 231 (outdoor-optimized, SGB detection)
- **Pattern focus:** LCD contrast optimization, outdoor visibility, SGB detection
- **Game Boy showcase:** Physical LCD characteristics, real-world portability

## Original Games for Phase 1

All games are 100% original concepts designed specifically for Game Boy capabilities and handheld play patterns.

### 1. Pocket Snake (Tier 1, L1-32)
**Genre:** Classic snake with handheld optimization
**Description:** Snake game optimized for Game Boy - 4-shade graphics, battery-efficient, high score saved to cartridge SRAM
**Technical focus:** Assembly basics, tiles/sprites, D-pad input, 4-shade optimization, SRAM saves
**Game Boy showcase:** 4-shade graphics, battery efficiency, portable controls
**Playable:** Lesson 3 | **Complete:** Lesson 7

### 2. Shade Shift (Tier 2, L33-64)
**Genre:** 4-shade puzzle game
**Description:** Match and clear blocks using Game Boy's 4 shades as core mechanic. Light beats dark!
**Technical focus:** Palette manipulation, shade-based logic, window layer HUD, dithering
**Game Boy showcase:** 4-shade LCD as gameplay feature, creative use of limited palette
**Playable:** Lesson 35 | **Complete:** Lesson 39

### 3. Battery Quest (Tier 3, L65-96)
**Genre:** Save/resume adventure
**Description:** Multi-screen adventure with battery-backed saves. Resume exactly where you left off!
**Technical focus:** MBC cartridge, battery SRAM, save/load, checksums, screen transitions
**Game Boy showcase:** Persistent saves, pick-up-and-play handheld design
**Playable:** Lesson 67 | **Complete:** Lesson 71

### 4. Sprite Storm (Tier 4, L97-128)
**Genre:** Bullet-hell shooter
**Description:** Manage 40 sprites and 10-per-scanline limit creatively. Bullets and enemies everywhere!
**Technical focus:** OAM management, sprite limits, multiplexing, priority system
**Game Boy showcase:** Hardware sprite constraints as design challenge
**Playable:** Lesson 99 | **Complete:** Lesson 103

### 5. Power Saver (Tier 5, L129-160)
**Genre:** Battery-efficient puzzle
**Description:** Game designed for maximum battery life - uses HALT/STOP modes intelligently
**Technical focus:** HALT mode, STOP mode, efficient VBlank, low-power programming
**Game Boy showcase:** Battery life optimization unique to handhelds
**Playable:** Lesson 131 | **Complete:** Lesson 135

### 6. Quick Play (Tier 6, L161-192)
**Genre:** Micro-game collection
**Description:** 2-minute games perfect for bus rides. Auto-saves progress between games.
**Technical focus:** Short-session design, auto-save, progress tracking, handheld UX
**Game Boy showcase:** Portable gaming philosophy, instant pick-up-and-play
**Playable:** Lesson 163 | **Complete:** Lesson 167

### 7. Link Battle (Tier 7, L193-224)
**Genre:** Two-player link cable battle
**Description:** Battle another Game Boy via link cable. Turn-based or simultaneous action!
**Technical focus:** Serial I/O, link cable protocol, master/slave, synchronization, disconnect handling
**Game Boy showcase:** Link cable multiplayer unique to Game Boy
**Playable:** Lesson 195 | **Complete:** Lesson 199

### 8. Sunlight Challenge (Tier 8, L225-256)
**Genre:** High-contrast outdoor game
**Description:** Designed to be playable in direct sunlight! High contrast, outdoor-optimized shades.
**Technical focus:** LCD contrast optimization, outdoor visibility, shade selection, Super Game Boy detection
**Game Boy showcase:** Physical LCD characteristics, real-world portable conditions
**Playable:** Lesson 227 | **Complete:** Lesson 231

## What Students Master

### Sharp SM83 Assembly Language
- Register set (A, B, C, D, E, H, L, F, SP, PC)
- Instruction set (Z80-like but distinct differences)
- Addressing modes (register, immediate, indirect, indexed)
- 8-bit and 16-bit operations
- Bit manipulation instructions
- Stack operations
- Efficient code patterns for limited CPU

### Game Boy Hardware
- **CPU:** Sharp SM83 @ 4.19MHz (Z80-like custom chip)
- **LCD:** 160×144 pixels, 4 shades
- **Background layer:** 256×256 tile map (32×32 tiles)
- **Window layer:** Overlay for HUD elements
- **Sprites:** 40 OAM sprites, 8×8 or 8×16, 10 per scanline limit
- **Tile VRAM:** 384 tiles, 8×8 each, 2bpp format
- **Palettes:** BGP, OBP0, OBP1 registers (4 shades each)
- **Memory map:** ROM banks, VRAM, Work RAM, OAM, I/O registers
- **Joypad:** D-pad + A, B, Select, Start

### Memory-Mapped I/O
- **LCD control (LCDC):** Enable/disable display, BG, window, sprites
- **LCD status (STAT):** VBlank, HBlank, scanline interrupts
- **Scroll registers:** SCX, SCY, WX, WY
- **Palette registers:** BGP, OBP0, OBP1
- **Joypad register:** P1 (with button matrix)
- **Serial I/O:** SB, SC for link cable
- **Timer registers:** DIV, TIMA, TMA, TAC
- **Interrupt registers:** IE, IF

### VBlank and Timing
- 60fps frame rate (59.7Hz precisely)
- VBlank period (1140 cycles)
- HBlank effects
- Interrupt-driven programming
- Frame timing and synchronisation
- Cycle counting for precision

### Game Boy ROM Structure
- ROM header ($0100-$014F)
- Nintendo logo data (verified by bootrom)
- Cartridge type and ROM/RAM sizes
- ROM banking (MBC1, MBC3, MBC5)
- Save battery RAM (persistence)
- Checksum calculation

### Portable Game Design
- **Short play sessions** - Levels completable in 2-5 minutes
- **Quick save/load** - Save anywhere or frequent checkpoints
- **Battery efficiency** - Optimise for longer play time
- **Pick-up-and-play** - Immediate engagement
- **On-screen tutorials** - No manual required
- **Link cable social play** - Trading, battling, co-op

### Advanced Techniques
- Sprite multiplexing (managing 10-per-scanline limit)
- STAT interrupt effects (HBlank manipulation)
- Window layer tricks (split screen, HUD)
- Tile animation
- Scrolling optimisation
- 4-shade dithering techniques
- Link cable protocols
- Save data integrity (checksums)

## 4-Shade Mastery

The Game Boy's 4-shade limitation requires creative techniques:

- **Dithering patterns** - Create illusion of more shades
- **Animation cycling** - Palette rotation for effects
- **Contrast management** - Ensure readability
- **Sprite overlay** - Layer sprites for depth
- **Tile design** - Work with shade limitations
- **UI clarity** - High contrast for buttons/text

## Link Cable Programming

Unique to Game Boy (and later Game Boy Color):

- **Serial I/O protocol** - Master/slave communication
- **Data synchronisation** - Ensure both sides in sync
- **Error handling** - Detect disconnections
- **Packet design** - Efficient data transfer
- **Game state sharing** - Trading, battling, co-op
- **Two-player patterns** - Turn-based, simultaneous, competitive

## Transfer Knowledge from Z80 Platforms

Students with ZX Spectrum experience will recognise:
- Similar instruction set (but Sharp SM83 has differences)
- Software sprite limitations (but GB has hardware sprites)
- Cycle counting importance
- Optimisation techniques

Approximately 70-80% of Z80 knowledge transfers to Sharp SM83.

## Comparison with NES and Other Handhelds

| Feature | Game Boy | NES | Game Gear | Lynx |
|---------|----------|-----|-----------|------|
| **CPU** | SM83 @ 4.2MHz | 6502 @ 1.79MHz | Z80 @ 3.58MHz | 65SC02 @ 4MHz |
| **Display** | 160×144, 4 shades | 256×240, 52 colors | 160×144, 4096 colors | 160×102, 4096 colors |
| **Sprites** | 40 (10/line) | 64 (8/line) | 64 (8/line) | Unlimited |
| **Battery Life** | 15-30 hours | N/A | 3-5 hours | 4-5 hours |
| **Success** | 118.7M units | 61.9M units | 10.6M units | 3M units |
| **Design** | Efficiency, longevity | Power, variety | Color at cost | Power at cost |

Game Boy's success: battery life, build quality, game library, affordability.

## Handheld Gaming Philosophy

This curriculum teaches not just Game Boy programming, but handheld game design:

1. **Respect battery life** - Efficient code, sleep modes
2. **Quick engagement** - Players can start in seconds
3. **Short sessions** - 2-10 minute play bursts
4. **Save flexibility** - Save anywhere or frequent checkpoints
5. **Portable UI** - Readable in various lighting
6. **Social features** - Link cable for shared experiences
7. **Replayability** - High scores, collections, achievements

## Navigation

- **View all phases:** [`./`](./)
- **Hardware references:** Coming soon (Sharp SM83, LCD controller, memory map)
- **Documentation index:** [`../START-HERE.md`](../START-HERE.md)

---

**Last updated:** 2025-11-04
**Version:** 1.0
**Status:** Overview complete, tier details and individual lessons to be created
