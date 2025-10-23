# Phase 1: 6502 Assembly + Hardware Fundamentals (Nintendo Entertainment System)

**Lessons:** 1-512 (16 tiers × 32 lessons per tier)
**Language:** 6502 Assembly Language
**Focus:** Hardware mastery through classic arcade game development

## Philosophy

Phase 1 teaches 6502 assembly and NES hardware programming through building classic arcade games at 60fps. Unlike home computers, the NES has no BASIC layer—students begin directly with assembly language, learning to control the PPU, APU, and cartridge hardware through game development.

## Structure Overview

| Tier | Focus | Lessons | Key Concepts | Deliverable |
|------|-------|---------|--------------|-------------|
| 1 | **Pong** | 1-32 | 6502 basics, PPU fundamentals, background tiles | 2-player paddle game (60fps) |
| 2 | **Breakout** | 33-64 | OAM sprites, collision detection, controller input | Brick-breaking with smooth ball physics |
| 3 | **Space Invaders** | 65-96 | Sprite management, formations, bullet systems | Fixed shooter with formation enemies |
| 4 | **Galaxian** | 97-128 | Sprite multiplexing, curved movement, patterns | Diving enemies with smooth trajectories |
| 5 | **Pac-Man** | 129-160 | Tile maps, maze logic, AI pathfinding | Ghost AI with distinct behaviors |
| 6 | **Donkey Kong** | 161-192 | Platformer physics, multi-screen levels | Jumping, ladders, screen transitions |
| 7 | **Mario Bros.** | 193-224 | Advanced platforming, enemy bouncing | POW block, platform wrapping |
| 8 | **Excitebike** | 225-256 | Horizontal scrolling, nametable updates | Side-scrolling with obstacles |
| 9 | **Balloon Fight** | 257-288 | Multi-directional scrolling, physics | Floating physics, screen wrapping |
| 10 | **Ice Climber** | 289-320 | Vertical scrolling, multi-screen gameplay | Upward progression, platform breaking |
| 11 | **Advanced Scrolling** | 321-352 | Split-screen, status bars, attribute updates | Mid-frame PPU techniques |
| 12 | **APU Mastery** | 353-384 | Music engine, sound effects, all 5 channels | FamiTracker integration |
| 13 | **Mapper Basics** | 385-416 | MMC1/MMC3, bank switching, CHR swapping | Extended ROM capabilities |
| 14 | **Advanced Graphics** | 417-448 | CHR-RAM, dynamic tiles, sprite techniques | Runtime graphics updates |
| 15 | **Complete Game** | 449-480 | Full game integration, polish, optimization | Commercial-quality game |
| 16 | **Mastery Project** | 481-512 | Student choice - original game design | Portfolio-ready NES game |

## NES-Specific Focus Areas

### Hardware Understanding

**PPU (Picture Processing Unit):**
- Pattern tables (CHR data, 256 tiles each)
- Nametables (background maps, 32×30 tiles)
- Attribute tables (2×2 tile colour blocks)
- OAM (Object Attribute Memory, 64 sprites)
- Palettes (background and sprite, 4 colours each)
- Scrolling registers ($2005, $2006)
- VRAM access timing (VBlank window)

**6502 CPU:**
- MOS 6502 instruction set (no decimal mode)
- 1.79MHz clock (NTSC)
- 2KB CPU RAM ($0000-$07FF, mirrored)
- Zero page optimization ($00-$FF)
- Stack operations ($0100-$01FF)

**APU (Audio Processing Unit):**
- Pulse 1 and 2 (square waves, duty cycle)
- Triangle wave (bass tones)
- Noise (percussion, effects)
- DMC (Delta Modulation Channel, samples)
- Frame counter (4-step / 5-step modes)

**Memory Map:**
- $0000-$07FF: CPU RAM (2KB, mirrored to $1FFF)
- $2000-$2007: PPU registers (mirrored to $3FFF)
- $4000-$4017: APU and I/O registers
- $6000-$7FFF: Cartridge RAM (if present)
- $8000-$FFFF: Cartridge ROM (PRG-ROM)

### Sprite System Mastery

**OAM (Object Attribute Memory):**
- 64 sprite slots (4 bytes each)
- Byte 0: Y position
- Byte 1: Tile index
- Byte 2: Attributes (palette, flip, priority)
- Byte 3: X position
- DMA transfer ($4014) for fast updates

**8-sprites-per-scanline limit:**
- Hardware limitation (sprite 0 hit)
- Requires strategic sprite management
- Sprite flickering techniques
- Priority ordering

**Sprite sizes:**
- 8×8 mode: 256 unique tiles
- 8×16 mode: Better for characters, uses both pattern tables

### Background Tile System

**Nametables:**
- 4 nametable addresses ($2000, $2400, $2800, $2C00)
- Mirroring modes (horizontal, vertical, single-screen)
- 32×30 tiles visible (256×240 pixels)
- 33×31 tiles buffered (scrolling headroom)

**Attributes:**
- 2×2 tile blocks share 1 palette
- 4 background palettes available
- Strategic tile arrangement for colour

**Scrolling techniques:**
- Seam concealment (status bars)
- Nametable switching for large worlds
- Mid-frame scroll updates

### PPU Timing and VBlank

**Critical concept:**
- PPU rendering: scanlines 0-239
- VBlank period: scanlines 241-260
- VRAM access only safe during VBlank
- ~2273 CPU cycles per VBlank (NTSC)

**NMI (Non-Maskable Interrupt):**
- Triggered at start of VBlank
- Game loop synchronization
- OAM DMA, palette updates, nametable changes

## Key Learning Arcs

### Arc 1: 6502 Foundation (Tiers 1-4)
- Master 6502 instruction set through games
- Understand PPU register access
- Implement sprite and background rendering
- Handle controller input (addresses $4016/$4017)

### Arc 2: Graphics Mastery (Tiers 5-9)
- Tile-based collision detection
- Multi-directional scrolling
- Sprite management and flickering
- Nametable manipulation

### Arc 3: Advanced Systems (Tiers 10-14)
- APU programming (all 5 channels)
- Mapper chip capabilities
- CHR-RAM dynamic graphics
- Complex game state management

### Arc 4: Professional Polish (Tiers 15-16)
- Complete game development cycle
- Optimization for ROM size
- Title screens, menus, continue systems
- Cartridge preparation

## NES-Specific Challenges Addressed

### Sprite Flickering Solutions
- **Rotating sprite priority** (Tiers 4-6)
- **Strategic sprite positioning** - Keep <8 sprites per line
- **8×16 sprite mode** - Fewer sprites needed

### Scrolling Techniques
- **Seam hiding** - Status bars cover nametable edges (Tier 11)
- **Attribute updates** - Minimize colour glitches
- **Split-screen scrolling** - Different scroll values per region

### VRAM Access Windows
- **VBlank budgeting** - ~2273 cycles available
- **Deferred updates** - Queue changes, apply in VBlank
- **Mid-frame techniques** - Status bars, split-screen (advanced)

### ROM Size Management
- **Code optimization** - Every byte counts
- **Data compression** - RLE, lookup tables
- **Mapper usage** - Bank switching for large games

## Comparison with Other Platforms

| Technique | NES | Commodore 64 | ZX Spectrum |
|-----------|-----|--------------|-------------|
| **Sprites** | 64 OAM (8/line) | 8 hardware | Software only |
| **Graphics** | Tile-based PPU | Bitmap+sprites | Bitmap+attributes |
| **Scrolling** | Hardware | Hardware | Software |
| **Sound** | APU (5 channels) | SID chip | BEEP/AY chip |
| **CPU** | 6502 (1.79MHz) | 6510 (1MHz) | Z80 (3.5MHz) |
| **Development** | Cartridge ROM | RAM-based | RAM-based |

**NES advantage:** Dedicated graphics/audio hardware, large sprite capacity
**NES constraint:** Tile-only graphics, 8-sprite-per-line limit, VBlank timing

## Prerequisites

None - Phase 1 is designed for assembly beginners. No prior programming experience required.

## Builds Toward

**Phase 2+:** Advanced NES techniques, specialized genres, mapper mastery

**Skills transferable to:**
- Other 6502 systems (Apple II, Atari 8-bit, C64)
- Tile-based game engines
- Hardware-constrained programming
- Retro game development

## Resources

**Development Tools:**
- ca65/ld65 assemblers (cc65 suite)
- Mesen emulator with debugging
- NES Screen Tool (tile/nametable editor)
- FamiTracker (music composition)

**Reference Materials:**
- 6502 instruction set documentation
- NESDev Wiki (comprehensive hardware reference)
- PPU scrolling diagrams
- Mapper specifications

**Cartridge Configuration:**
- iNES header format
- NROM (no mapper) for early tiers
- MMC1/MMC3 for advanced tiers
- CHR-ROM vs CHR-RAM

## Notes for Lesson Creators

**Assembly-first approach:**
- No BASIC foundation to build on
- Teach 6502 fundamentals through immediate game development
- Hexadecimal and binary literacy from lesson 1

**Hardware-centric teaching:**
- PPU/APU are not "advanced topics"—they're lesson 1
- VBlank window is fundamental to every program
- OAM DMA is standard practice, not optimization

**Cartridge mindset:**
- Code lives in ROM (read-only)
- RAM is precious (2KB only)
- CHR data is separate from code
- Mappers extend capabilities

**NES development culture:**
- Reference classic NES games throughout
- Emphasize creative solutions to hardware limits
- Sprite flickering is acceptable (authentic to platform)
- 60fps is non-negotiable

**Tools integration:**
- FamiTracker music can be exported to assembly
- NES Screen Tool generates nametable data
- Emulator debugging is essential skill

---

**Version:** 1.0
**Last Updated:** 2025-10-23
**Status:** High-level outline - detailed tier breakdowns to be created
