# Sinclair ZX Spectrum Curriculum

**Platform:** Sinclair ZX Spectrum (48K/128K)
**Gateway Language:** Sinclair BASIC
**Assembly Language:** Z80
**Total Curriculum:** 8,256 lessons (Phase 0 + Phases 1-16)

## Overview

The ZX Spectrum curriculum teaches programming through the lens of Britain's most iconic home computer. From Sinclair BASIC through Z80 assembly mastery, students experience the creative constraints and clever solutions that defined 1980s British game development.

## Curriculum Structure

### Phase 0: Sinclair BASIC (64 lessons)
**Language:** Sinclair BASIC
**Focus:** Game-first discovery learning
**Deliverables:** 16+ complete games

Learn BASIC programming through the Spectrum's unique features:
- Attribute-based graphics system
- BEEP sound programming
- UDG (User-Defined Graphics)
- Fast BASIC execution
- 128K model enhancements

[Read Phase 0 Overview →](phase-0/overview.md)

### Phase 1: Z80 Assembly + Hardware Fundamentals (512 lessons)
**Language:** Z80 Assembly
**Focus:** Classic arcade games, hardware mastery
**Deliverables:** 16 complete games at 60fps

Master Z80 assembly through arcade game development:
- Software sprite techniques
- Attribute system mastery
- ULA timing and contended memory
- AY sound chip programming (128K)
- Scrolling and visual effects

[Read Phase 1 Curriculum →](PHASE-1-CURRICULUM.md)

### Phases 2-16 (7,680 lessons)
**Status:** To be detailed

Advanced Z80 development across specialized genres:
- Action games (shooters, platformers)
- Puzzle and strategy games
- RPG systems
- Multi-load epics
- 128K technical showcases

## Platform Characteristics

### Hardware Specifications

**ZX Spectrum 48K:**
- CPU: Z80 @ 3.5MHz
- RAM: 48KB (16K screen, ~32K for programs)
- ROM: 16KB (Sinclair BASIC + system routines)
- Display: 256×192 pixels, 15 colours (8 normal + 8 BRIGHT)
- Attributes: 8×8 character blocks for colour
- Sound: 1-bit BEEP (border port)
- Storage: Cassette tape

**ZX Spectrum 128K:**
- All 48K features plus:
- RAM: 128KB (paged memory banks)
- Sound: AY-3-8912 (3 channels)
- Enhanced BASIC commands
- Improved keyboard

### Unique Features

**Strengths:**
- Fast BASIC interpreter
- Direct graphics commands (PLOT, DRAW, CIRCLE)
- Keyword entry system
- Responsive keyboard polling
- Strong text handling
- Large software library

**Constraints:**
- Colour clash (attributes)
- No hardware sprites
- Simple sound (48K)
- Memory limitations
- Contended memory timing

**Creative Solutions:**
- Monochrome sprites avoid colour clash
- Software sprite techniques achieve smooth movement
- BRIGHT and FLASH attributes for visual interest
- Fast CPU compensates for lack of hardware support

## Development Tools

**Emulators:**
- Fuse (recommended - excellent debugging)
- ZEsarUX (advanced features, multi-platform)
- SpecEmu (Windows classic)

**Assemblers:**
- pasmo (modern, cross-platform)
- z80asm (z88dk toolchain)
- sjasmplus (advanced features)

**BASIC Tools:**
- zmakebas (BASIC to TAP/TZX)
- BasinC (IDE with syntax highlighting)

**Graphics Tools:**
- Multipaint (cross-platform pixel editor)
- CharPad (character/tile editor)
- ZX-Paintbrush (native Spectrum graphics editor)

## Learning Path

1. **Start with Phase 0** - Learn Sinclair BASIC fundamentals
2. **Master the attribute system** - Understand colour clash
3. **Build complete games** - Experience strengths and limits
4. **Transition to Z80** - Unlock full hardware potential
5. **Specialize in genres** - Deep dive into game types
6. **Master 128K features** - AY sound, extra RAM

## Historical Context

The ZX Spectrum (1982-1992) defined British home computing:
- 5 million units sold
- Bedroom coders launched game industry careers
- Distinctive visual style (colour clash, monochrome sprites)
- Tape loading culture (multicolour borders, loading screens)
- Foundation of UK game development heritage

**Iconic games:**
- Manic Miner / Jet Set Willy (Matthew Smith)
- Sabre Wulf (Ultimate Play The Game)
- Head Over Heels (Jon Ritman)
- Lords of Midnight (Mike Singleton)

## Prerequisites

None - Phase 0 is designed for complete beginners.

## Comparison with C64 Curriculum

| Aspect | ZX Spectrum | Commodore 64 |
|--------|-------------|--------------|
| **BASIC Speed** | Fast | Slow |
| **Graphics** | Software sprites, attributes | Hardware sprites, per-pixel colour |
| **Sound** | BEEP/AY chip | SID chip |
| **Screen Access** | PRINT AT, PLOT, DRAW | POKE screen memory |
| **Complexity** | Simpler hardware | More complex hardware |
| **Teaching Focus** | Creative constraints | Hardware flexibility |

Both curricula teach the same fundamental concepts through different hardware approaches.

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Phase 0 and Phase 1 outlined, Phases 2-16 to be detailed
**Documentation:** High-level structure complete
