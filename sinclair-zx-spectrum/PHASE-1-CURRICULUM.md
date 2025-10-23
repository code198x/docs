# Phase 1: Z80 Assembly + Hardware Fundamentals (Sinclair ZX Spectrum)

**Lessons:** 1-512 (16 tiers × 32 lessons per tier)
**Language:** Z80 Assembly Language
**Focus:** Hardware mastery through classic arcade game development

## Philosophy

Phase 1 teaches Z80 assembly through rebuilding Phase 0's games at 60fps with hardware-perfect graphics and sound. The ZX Spectrum's architecture teaches fundamental concepts applicable to all Z80-based systems.

## Structure Overview

| Tier | Focus | Lessons | Key Concepts | Deliverable |
|------|-------|---------|--------------|-------------|
| 1 | **Pong** | 1-32 | Z80 basics, screen addressing, ULA timing | 2-player paddle game (60fps) |
| 2 | **Breakout** | 33-64 | Software sprites, collision, attribute handling | Brick-breaking with smooth ball physics |
| 3 | **Space Invaders** | 65-96 | Multiple sprites, formations, bullet management | Fixed shooter with colour-clash solutions |
| 4 | **Galaxian** | 97-128 | Diving enemies, smooth curves, attack patterns | Scrolling star field background |
| 5 | **Pac-Man** | 129-160 | Maze navigation, AI pathfinding, tile maps | Ghost AI with personalities |
| 6 | **Frogger** | 161-192 | Moving platforms, multi-sprite tracking | Lane-crossing with smooth scrolling |
| 7 | **Scramble** | 193-224 | Horizontal scrolling, terrain following | Side-scrolling shooter with fuel system |
| 8 | **Defender** | 225-256 | Bi-directional scrolling, radar mini-map | Wrap-around world with kidnapping mechanics |
| 9 | **Moon Patrol** | 257-288 | Parallax scrolling, terrain collision | Multi-layer scrolling landscape |
| 10 | **Jetpac** | 289-320 | Platformer physics, multi-stage screens | Gravity, thrusting, screen-to-screen |
| 11 | **Manic Miner** | 321-352 | Pixel-perfect collision, moving platforms | Classic Spectrum platformer techniques |
| 12 | **128K Sound** | 353-384 | AY chip programming, music players | 3-voice music and sound effects |
| 13 | **Advanced Graphics** | 385-416 | Fast software sprites, masked rendering | Sprite multiplexing, smooth movement |
| 14 | **Screen Techniques** | 417-448 | Split-screen, raster effects (Spectrum limits) | HUD overlays, colour cycling |
| 15 | **Complete Game** | 449-480 | Full game integration, optimization | Commercial-quality complete game |
| 16 | **Mastery Project** | 481-512 | Student choice - complete polished game | Portfolio-ready Spectrum game |

## Spectrum-Specific Focus Areas

### Hardware Understanding

**ULA (Uncommitted Logic Array):**
- Screen memory layout (6144 bytes bitmap + 768 bytes attributes)
- Border colour and timing
- Contended memory timing
- Interrupt generation (50Hz)

**Z80 CPU:**
- 3.5MHz clock (with contention)
- 8-bit and 16-bit registers
- Instruction timing (T-states)
- Stack and subroutines

**Memory Map:**
- ROM (0-16383): System routines
- Screen (16384-22527): Display file
- Attributes (22528-23295): Colour data
- Program RAM (23296-65535): Code and data
- 128K: Paged RAM banks

### Attribute System Mastery

**Tier 3-5 focus:**
- Working within 8×8 attribute blocks
- Colour clash mitigation strategies
- BRIGHT and FLASH attributes for visual effects
- Attribute-preserving sprite drawing
- Monochrome sprite techniques

### Software Sprite Techniques

**No hardware sprites means mastering:**
- Masked sprite rendering (AND/OR/XOR methods)
- Background preservation and restoration
- Character-aligned vs pixel-aligned movement
- Sprite clipping at screen edges
- Fast sprite routines (unrolled loops, self-modifying code)

### Sound Programming

**48K BEEP (Tiers 1-11):**
- Bit 4 of port 254 (border + speaker)
- Timing loops for pitch
- Interrupt-driven sound effects
- Multiple concurrent tones

**128K AY Chip (Tier 12+):**
- 3 square-wave channels
- Noise generator
- Envelope shaping
- Register programming
- Music player routines

## Key Learning Arcs

### Arc 1: Z80 Foundation (Tiers 1-4)
- Master Z80 instruction set through simple games
- Understand screen memory layout
- Implement core game loops
- Handle keyboard input efficiently

### Arc 2: Graphics Mastery (Tiers 5-9)
- Fast software sprite routines
- Scrolling techniques (character-based, pixel-based)
- Attribute management strategies
- Collision detection optimization

### Arc 3: Complex Systems (Tiers 10-14)
- Multi-screen game structures
- AI and pathfinding
- 128K features (sound, extra RAM)
- Advanced visual effects

### Arc 4: Professional Polish (Tiers 15-16)
- Complete game development cycle
- Optimization for speed and size
- Menu systems, title screens, high scores
- Tape loading screens and multiload

## Spectrum-Specific Challenges Addressed

### Colour Clash Solutions
- **Monochrome sprites:** Avoid clash entirely (Tiers 3-5)
- **Attribute-aligned design:** Work with 8×8 blocks, not against them (Tiers 6-8)
- **Colour cycling:** Use FLASH and BRIGHT creatively (Tiers 9-11)

### Contended Memory
- **Understanding timing:** ULA steals CPU cycles during screen display
- **Optimization strategies:** Place time-critical code in uncontended RAM
- **Interrupt handling:** Work with/around 50Hz interrupt

### Speed Optimization
- **Unrolled loops:** Trade size for speed in sprite routines
- **Self-modifying code:** Direct memory writes for maximum speed
- **Lookup tables:** Pre-calculated screen addresses, multiplication

## Comparison with Other Platforms

| Technique | ZX Spectrum | Commodore 64 | NES |
|-----------|-------------|--------------|-----|
| **Sprites** | Software | Hardware (8) | Hardware (64) |
| **Colours** | Attributes (8×8) | Per-pixel | Per-tile |
| **Scrolling** | Software | Hardware | Hardware |
| **Sound** | BEEP/AY | SID chip | 2A03 APU |
| **CPU** | Z80 (3.5MHz) | 6510 (1MHz) | 6502 (1.79MHz) |

**Spectrum advantage:** Fast CPU makes software sprites viable
**Spectrum constraint:** Attribute system requires creative solutions

## Prerequisites

**Phase 0 complete** - Understanding of:
- Spectrum memory layout (from BASIC PEEK/POKE)
- Screen addressing concepts
- Attribute system behaviour
- Game design fundamentals

## Builds Toward

**Phase 2+:** Advanced Z80 techniques, specialized genres, multi-platform Z80 development

## Resources

**Development Tools:**
- pasmo/z80asm assemblers
- Fuse/ZEsarUX emulators with debugging
- zmakebas for BASIC loaders
- Graphics tools (UDG editors, sprite designers)

**Reference Materials:**
- Z80 instruction set documentation
- Spectrum ROM disassembly
- ULA timing diagrams
- Classic game analysis

## Notes for Lesson Creators

**Teach through comparison:**
- "In BASIC this took 5 seconds, in assembly it's instant"
- Show Phase 0 game alongside Phase 1 remake

**Embrace Spectrum identity:**
- Colour clash isn't a flaw, it's character
- Many classic Spectrum games used monochrome sprites beautifully
- Fast action is possible with careful optimization

**British gaming heritage:**
- Reference classic Spectrum titles (Manic Miner, Jet Set Willy, Sabre Wulf)
- Teach the techniques that made these games legendary

---

**Version:** 1.0
**Last Updated:** 2025-10-23
**Status:** High-level outline - detailed tier breakdowns to be created
