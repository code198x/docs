# Phase 1: 6502 Assembly + Hardware Fundamentals

**Lessons:** 1-512 (16 tiers × 32 lessons per tier)
**Language:** 6502 Assembly Language
**Approach:** Game-first hardware mastery

## Philosophy

Phase 1 teaches 6502 assembly and NES hardware programming through building classic arcade games at 60fps. Unlike home computers with BASIC interpreters, the NES has no BASIC layer—students begin directly with assembly language, learning to control the PPU, APU, and cartridge hardware through game development.

The Nintendo Entertainment System represents a unique pedagogical approach: **assembly-first game development**. There is no Phase 0 because there is no BASIC interpreter. Students learn low-level programming from day one, but through the immediate gratification of building games that look and feel like commercial NES titles.

## Structure

### Tier 1: Pong (L1-32)
**Game:** 2-player paddle game (60fps)
**Concepts:** 6502 basics, PPU fundamentals, background tiles, sprite basics

### Tier 2: Breakout (L33-64)
**Game:** Brick-breaking with smooth ball physics
**Concepts:** OAM sprites, collision detection, controller input, score display

### Tier 3: Space Invaders (L65-96)
**Game:** Fixed shooter with formation enemies
**Concepts:** Sprite management, formations, bullet systems, wave progression

### Tier 4: Galaxian (L97-128)
**Game:** Diving enemies with smooth trajectories
**Concepts:** Sprite multiplexing, curved movement, attack patterns

### Tier 5: Pac-Man (L129-160)
**Game:** Maze navigation with ghost AI
**Concepts:** Tile maps, maze logic, AI pathfinding, distinct behaviors

### Tier 6: Donkey Kong (L161-192)
**Game:** Platformer with multi-screen levels
**Concepts:** Platformer physics, jumping, ladders, screen transitions

### Tier 7: Mario Bros. (L193-224)
**Game:** Advanced platforming with enemy bouncing
**Concepts:** POW block mechanics, platform wrapping, two-player

### Tier 8: Excitebike (L225-256)
**Game:** Side-scrolling racing
**Concepts:** Horizontal scrolling, nametable updates, obstacle avoidance

### Tier 9: Balloon Fight (L257-288)
**Game:** Multi-directional flight
**Concepts:** Multi-directional scrolling, floating physics, screen wrapping

### Tier 10: Ice Climber (L289-320)
**Game:** Vertical platforming
**Concepts:** Vertical scrolling, multi-screen gameplay, platform breaking

### Tier 11: Advanced Scrolling (L321-352)
**Techniques:** Split-screen status bars, mid-frame updates
**Concepts:** Advanced PPU control, attribute updates, seam hiding

### Tier 12: APU Mastery (L353-384)
**System:** Music engine with sound effects
**Concepts:** All 5 APU channels, music data, FamiTracker integration

### Tier 13: Mapper Basics (L385-416)
**Capability:** ROM bank switching
**Concepts:** MMC1/MMC3, bank switching, CHR swapping, extended games

### Tier 14: Advanced Graphics (L417-448)
**Techniques:** Runtime graphics updates
**Concepts:** CHR-RAM, dynamic tiles, sprite techniques, animation

### Tier 15: Complete Game (L449-480)
**Deliverable:** Commercial-quality game
**Concepts:** Full integration, polish, optimization, menus, continues

### Tier 16: Mastery Project (L481-512)
**Deliverable:** Portfolio-ready original NES game
**Concepts:** Student choice, original design, complete development cycle

## NES-Specific Focus Areas

### Hardware Understanding

**PPU (Picture Processing Unit):**
- Pattern tables (CHR data, 256 tiles each)
- Nametables (background maps, 32×30 tiles visible)
- Attribute tables (2×2 tile colour blocks)
- OAM (Object Attribute Memory, 64 sprites)
- Palettes (background and sprite, 4 colours each)
- Scrolling registers ($2005, $2006)
- VRAM access timing (VBlank window critical)

**6502 CPU:**
- MOS 6502 instruction set (Ricoh 2A03, no decimal mode)
- 1.79MHz clock speed (NTSC) / 1.66MHz (PAL)
- 2KB CPU RAM ($0000-$07FF, mirrored to $1FFF)
- Zero page optimization ($00-$FF fast access)
- Stack operations ($0100-$01FF)
- Interrupt handling (NMI, IRQ)

**APU (Audio Processing Unit):**
- Pulse 1 and 2 (square waves, duty cycle control)
- Triangle wave (bass tones)
- Noise channel (percussion, explosions)
- DMC (Delta Modulation Channel, samples)
- Frame counter (4-step / 5-step modes)

**Memory Map:**
```
$0000-$07FF: CPU RAM (2KB, mirrored)
$2000-$2007: PPU registers (mirrored to $3FFF)
$4000-$4017: APU and I/O registers
$6000-$7FFF: Cartridge RAM (if present)
$8000-$FFFF: Cartridge ROM (PRG-ROM)
```

### Sprite System Mastery

**OAM (Object Attribute Memory):**
- 64 sprite slots (4 bytes each: Y, tile, attributes, X)
- DMA transfer ($4014) for fast updates during VBlank
- Sprite priority (behind/in front of background)
- Horizontal and vertical flipping

**8-sprites-per-scanline limit:**
- Hardware constraint requiring strategic management
- Sprite flickering techniques (rotate priority)
- Sprite 0 hit detection for timing
- 8×16 sprite mode reduces sprite count needs

### Background Tile System

**Nametables:**
- 4 nametable addresses ($2000, $2400, $2800, $2C00)
- Mirroring modes (horizontal, vertical, single-screen, 4-screen)
- 32×30 tiles visible (256×240 pixels)
- 33×31 tiles buffered for scrolling headroom

**Attributes:**
- 2×2 tile blocks share one 4-colour palette
- 4 background palettes × 4 sprite palettes
- Strategic tile arrangement for colour assignments

**Scrolling techniques:**
- Nametable switching for large worlds
- Seam concealment with status bars
- Mid-frame scroll updates (advanced)

### PPU Timing and VBlank

**Critical concept for every NES program:**
- PPU rendering active: scanlines 0-239 (drawing)
- VBlank period: scanlines 241-260 (safe VRAM access)
- Approximately 2273 CPU cycles available per VBlank (NTSC)
- NMI (Non-Maskable Interrupt) triggers at VBlank start

**Game loop structure:**
1. Wait for VBlank (NMI)
2. Update OAM via DMA
3. Update palettes, scroll, nametables
4. Exit NMI handler
5. Game logic during rendering
6. Repeat

## Key Learning Arcs

### Arc 1: 6502 Foundation (Tiers 1-4, L1-128)
- Master 6502 instruction set through game development
- Understand PPU register access patterns
- Implement sprite and background rendering
- Handle controller input ($4016/$4017 registers)
- Build complete games with smooth 60fps gameplay

### Arc 2: Graphics Mastery (Tiers 5-9, L129-288)
- Tile-based collision detection (maze logic)
- Multi-directional scrolling techniques
- Sprite management and flickering solutions
- Nametable manipulation for large worlds
- Attribute table updates for colour changes

### Arc 3: Advanced Systems (Tiers 10-14, L289-448)
- APU programming (all 5 channels simultaneously)
- Mapper chip capabilities (bank switching)
- CHR-RAM for dynamic graphics updates
- Complex game state management
- Music engines and sound effect systems

### Arc 4: Professional Polish (Tiers 15-16, L449-512)
- Complete game development cycle (design to cartridge)
- Optimization for ROM size constraints
- Title screens, menus, continue systems
- Save systems (battery-backed RAM or password)
- Cartridge preparation and testing

## NES-Specific Challenges Addressed

### Sprite Flickering Solutions
- **Rotating sprite priority** (learned Tiers 4-6)
  - Cycle which sprites appear first
  - Distributes flicker across all sprites evenly
- **Strategic sprite positioning**
  - Keep fewer than 8 sprites per scanline when possible
  - Vertical spacing reduces conflicts
- **8×16 sprite mode**
  - Taller sprites mean fewer needed
  - Uses both pattern tables automatically

### Scrolling Techniques
- **Seam hiding with status bars** (Tier 11)
  - Status bar covers nametable edge during updates
  - Mid-frame scroll change splits screen
- **Attribute updates**
  - Minimize colour glitches during scrolling
  - Pre-update attributes before tiles appear
- **Split-screen scrolling**
  - Different scroll values per region
  - Requires precise PPU timing

### VRAM Access Windows
- **VBlank budgeting**
  - Only ~2273 cycles available (NTSC)
  - Must prioritize OAM, palettes, critical updates
- **Deferred updates**
  - Queue nametable changes
  - Apply over multiple frames if needed
- **Mid-frame techniques** (advanced, Tier 11+)
  - Sprite 0 hit for timing
  - Status bars, parallax effects

### ROM Size Management
- **Code optimization**
  - Every byte counts in small ROM sizes
  - Lookup tables vs computed values
- **Data compression**
  - RLE (Run-Length Encoding) for tiles
  - Metatiles (2×2 or 4×4 tile blocks)
- **Mapper usage** (Tier 13+)
  - Bank switching extends game size
  - MMC1, MMC3 for commercial-scale games

## Comparison with Other Platforms

| Technique | NES | Commodore 64 | ZX Spectrum | Amiga |
|-----------|-----|--------------|-------------|-------|
| **Sprites** | 64 OAM (8/line) | 8 hardware | Software only | BOBs (blitter) |
| **Graphics** | Tile-based PPU | Bitmap+sprites | Bitmap+attributes | Bitmap+BOBs |
| **Scrolling** | Hardware (nametable) | Hardware (smooth) | Software (chunky) | Hardware (dual playfield) |
| **Sound** | APU (5 channels) | SID chip | BEEP/AY chip | Paula (4-channel PCM) |
| **CPU** | 6502 @ 1.79MHz | 6510 @ 1MHz | Z80 @ 3.5MHz | 68000 @ 7.14MHz |
| **Gateway** | None (assembly) | BASIC V2 | Sinclair BASIC | AMOS Professional |
| **Development** | Cartridge ROM | RAM-based | RAM-based | RAM/disk |

**NES advantage:** Dedicated graphics/audio hardware, 64 sprites, mature tooling
**NES constraint:** Tile-only graphics, 8-sprite-per-line limit, strict VBlank timing, ROM-based

## Prerequisites

None - Phase 1 is designed for assembly beginners who want to learn through game development. No prior programming experience required.

**Helpful but not required:**
- Basic understanding of hexadecimal/binary notation (taught in Tier 1)
- Familiarity with classic arcade games (helpful for motivation)

## Builds Toward

**Phase 2:** Advanced Action Games (detailed genre focus)
**Phase 3+:** Specialized genres, advanced mapper programming, commercial techniques

**Skills transferable to:**
- Other 6502 platforms (Apple II, Atari 8-bit, Commodore 64)
- Tile-based game engines (modern engines use similar concepts)
- Hardware-constrained programming (embedded systems, retro consoles)
- Game Boy development (similar tile/sprite architecture)

## Resources

**Development Tools:**
- ca65/ld65 assemblers (cc65 toolchain - recommended)
- Mesen emulator with integrated debugger
- NES Screen Tool (tile and nametable editor)
- YY-CHR (CHR pattern editor)
- FamiTracker/FamiStudio (music composition)

**Reference Materials:**
- NESDev Wiki (comprehensive hardware documentation)
- 6502 instruction set reference
- PPU scrolling and rendering diagrams
- Mapper specifications (MMC1, MMC3)
- Cartridge pinouts and configurations

**Cartridge Configuration:**
- iNES header format (.nes files)
- NROM (no mapper) for Tiers 1-12
- MMC1/MMC3 introduced Tier 13
- CHR-ROM vs CHR-RAM considerations

## Notes for Lesson Creators

**Assembly-first approach:**
- No BASIC foundation exists on NES
- Teach 6502 fundamentals through immediate game results
- Hexadecimal and binary from lesson 1 (necessary for hardware access)
- Memory-mapped I/O is fundamental, not advanced

**Hardware-centric teaching:**
- PPU and APU are not "advanced topics"—they're lesson 1
- VBlank window is fundamental to every NES program
- OAM DMA is standard practice (not an optimization)
- Sprites and tiles are the only graphics options

**Cartridge mindset:**
- Code lives in ROM (read-only, cannot self-modify easily)
- RAM is precious (only 2KB for everything)
- CHR data is separate from program code
- Mappers extend capabilities but add complexity

**NES development culture:**
- Reference classic NES games throughout curriculum
- Emphasize creative solutions to hardware limits
- Sprite flickering is acceptable (authentic to platform)
- 60fps is non-negotiable (NES standard)

**Tools integration:**
- FamiTracker exports assembly-ready music data
- NES Screen Tool generates nametable initialization code
- Emulator debugging is an essential skill (not optional)
- Build process includes assembling, linking, creating .nes file

**American spelling:** The NES was primarily an American console (despite Japanese origin), so use American English conventions.

---

**Version:** 1.1
**Last Updated:** 2025-10-27
**Status:** Tier 1 (L1-32) complete (32-lesson Pong game), Tier 2-16 specs to be created
