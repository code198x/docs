# Commodore Amiga Curriculum

**Platform:** Commodore Amiga (OCS/ECS/AGA)
**Gateway Language:** AMOS Professional
**Assembly Language:** Motorola 68000
**Total Curriculum:** 8,256 lessons (Phase 0 + Phases 1-16)

## Overview

The Amiga curriculum teaches programming through the lens of the world's most advanced multimedia computer of the late 1980s. From AMOS Professional through 68000 assembly mastery, students experience the creative power and architectural elegance that made the Amiga legendary for games, graphics, music, and video production.

## Curriculum Structure

### Phase 0: AMOS Professional (64 lessons)
**Language:** AMOS Professional (1992)
**Focus:** Game-first discovery learning
**Deliverables:** 16+ complete games

Learn game development using AMOS Professional, the powerful BASIC dialect designed specifically for Amiga multimedia and game creation:
- BOB (Blitter OBject) sprite system
- Screen management and animation
- Sample playback and tracker music
- Fast BASIC execution with optional compilation
- Copper effects and palette manipulation
- Structured programming (no line numbers)

[Read Phase 0 Overview →](phase-0/overview.md)

### Phase 1: 68000 Assembly + Hardware Fundamentals (512 lessons)
**Language:** Motorola 68000 Assembly
**Focus:** Classic arcade games, custom chip mastery
**Deliverables:** 16 complete games at 50fps

Master 68000 assembly through arcade game development:
- Direct copper programming (display manipulation)
- Blitter operations (fast graphics)
- Hardware sprites and playfields
- Paula audio (4-channel 8-bit PCM)
- CIA timers and interrupts
- Dual playfield scrolling

[Read Phase 1 Curriculum →](PHASE-1-CURRICULUM.md)

### Phases 2-16 (7,680 lessons)
**Status:** To be detailed

Advanced Amiga development across specialized genres:
- Action games (shooters, platformers, beat-em-ups)
- AGA chipset programming (A1200, 256 colors)
- Advanced copper and blitter techniques
- Tracker music composition
- Multi-disk game structures
- Technical showcases

## Platform Characteristics

### Hardware Specifications

**Amiga 500 (OCS - Baseline):**
- CPU: Motorola 68000 @ 7.16MHz (NTSC) / 7.09MHz (PAL)
- RAM: 512KB Chip RAM (expandable to 1MB + 8MB Fast RAM)
- Chipset: OCS (Original Chip Set, 1985)
  - Agnus: Memory controller, blitter, copper
  - Denise: Playfield/sprite video
  - Paula: 4-channel 8-bit audio, I/O
- Display: 320×256 (PAL) / 320×200 (NTSC), up to 4096 colors
- Sprites: 8 hardware sprites (16 colors each)
- Playfields: Dual playfield support
- Blitter: Fast memory copy/fill with line drawing
- Copper: Display list co-processor
- Sound: 4 channels, 8-bit PCM, 28kHz max sample rate
- Storage: 3.5" floppy disk (880KB)

**Amiga 500+ (ECS - Enhanced):**
- CPU: Motorola 68000 @ 7.16MHz (NTSC) / 7.09MHz (PAL)
- RAM: 1MB Chip RAM standard (expandable to 2MB + 8MB Fast RAM)
- Chipset: ECS (Enhanced Chip Set, 1990)
  - Super Denise: Productivity modes (640×480, 1280×200)
  - Enhanced Agnus: 2MB Chip RAM support (Fat Agnus)
  - Improved flickerfixer support
  - Backward compatible with OCS
- **Programming notes:** Mostly OCS-compatible, productivity modes rarely used in games

**Amiga 1200 (AGA - Advanced):**
- CPU: Motorola 68020 @ 14.19MHz (NTSC) / 14.09MHz (PAL)
- RAM: 2MB Chip RAM (expandable to 10MB Fast RAM)
- Chipset: AGA (Advanced Graphics Architecture, 1992)
  - 256 colors on-screen from 24-bit palette (16.8M colors)
  - Enhanced blitter with 64-bit operations
  - Super-hires modes (1280×512 interlaced)
  - HAM8 mode (262,144 colors on-screen)
  - Improved sprite capabilities
- Backward compatible with OCS/ECS software

### Model Progression (Curriculum Coverage)

**OCS Era (Phases 1-9):**
- A1000 (1985) - First Amiga, 256KB Chip RAM
- A500 (1987) - **Primary reference model**, most popular
- A2000 (1987) - Professional model, expansion slots

**ECS Era (Phases 8-10):**
- A500+ (1991) - Enhanced chipset, 1MB Chip RAM
- A600 (1991) - Compact design, IDE interface
- A3000 (1990) - Workstation, 68030 CPU

**AGA Era (Phases 10-12):**
- A1200 (1992) - **Enhanced reference model**, 256-color AGA
- A4000 (1992) - Professional AGA workstation

**Not Covered:**
- CD32 (1993) - Games console, no keyboard
- CDTV (1991) - Multimedia appliance
- *(Mentioned in historical context only)*

### Unique Features

**Strengths:**
- Custom chip architecture (Agnus, Denise, Paula)
- Copper co-processor (raster tricks, palette changes)
- Blitter (fast bitblt operations without CPU)
- 4-channel stereo 8-bit audio (hardware mixing)
- Dual playfield support (parallax scrolling)
- Hardware sprites with collision detection
- Preemptive multitasking OS (Kickstart/Workbench)
- Expansion architecture (Zorro II/III)

**Constraints:**
- Chip RAM vs Fast RAM split (DMA limitations)
- Limited sprite count (8 sprites, reusable)
- Bitplane graphics (memory intensive)
- Floppy disk storage (880KB)
- Copper timing synchronization

**Creative Solutions:**
- Copper palette tricks (>32 colors on screen)
- Blitter for sprite multiplexing
- Dual playfield for parallax
- Bob system (blitter objects)
- Tracker music format (ProTracker, .MOD files)

## Development Tools

**Emulators:**
- WinUAE (recommended - excellent debugging, Windows/Linux)
- FS-UAE (cross-platform, modern UI)
- Amiberry (Raspberry Pi optimized)

**Assemblers:**
- vasm (modern, cross-platform)
- AsmOne/AsmPro (classic Amiga assemblers)
- DevPac (professional development suite)

**AMOS Tools:**
- AMOS Professional (included compiler)
- Ultimate AMOS (modern documentation)

**Graphics Tools:**
- Deluxe Paint (IFF/ILBM format)
- Personal Paint
- Brilliance

**Audio Tools:**
- ProTracker (module music)
- OctaMED
- AudioMaster

## Learning Path

1. **Start with Phase 0** - Learn AMOS Professional fundamentals
2. **Master multimedia** - Graphics, animation, sound integration
3. **Build complete games** - Experience AMOS capabilities and limits
4. **Transition to 68000** - Unlock custom chip power
5. **Master the chipset** - Copper, blitter, Paula direct control
6. **Specialize in genres** - Deep dive into game types
7. **Explore AGA** - A1200 enhanced capabilities (Phases 10-12)

## Historical Context

The Commodore Amiga (1985-1996) revolutionized home computing:
- First affordable multimedia computer
- Defined digital music (tracker format, .MOD files)
- Pioneered video production (Video Toaster)
- Dominated European game development
- Influenced game industry (Bitmap Brothers, Psygnosis, Team17)
- Founded demoscene culture

**Iconic games:**
- Shadow of the Beast (Reflections)
- Lemmings (DMA Design)
- Speedball 2 (Bitmap Brothers)
- Sensible Soccer (Sensible Software)
- Chaos Engine (Bitmap Brothers)
- Cannon Fodder (Sensible Software)

## Prerequisites

None - Phase 0 is designed for complete beginners.

## Comparison with Other Platforms

| Aspect | Amiga | Commodore 64 | Atari ST |
|--------|-------|--------------|----------|
| **Gateway Language** | AMOS Professional | BASIC V2 | GFA BASIC |
| **CPU** | 68000 @ 7MHz | 6510 @ 1MHz | 68000 @ 8MHz |
| **Graphics** | Custom (Denise, blitter) | VIC-II (8 sprites) | Shifter (no sprites) |
| **Sound** | Paula (4ch, 8-bit PCM) | SID chip | YM2149 (3ch PSG) |
| **Co-processors** | Copper, Blitter | None | None |
| **OS** | Multitasking (Kickstart) | None | TOS (GEM) |
| **Teaching Focus** | Multimedia, custom chips | 8-bit creativity | MIDI, productivity |

The Amiga teaches modern computer architecture (co-processors, DMA, multitasking) through 1980s hardware.

## Modern Variants

### Vampire V4 (Apollo 68080)

**Category:** Enhanced reimagination (Phase 17+ content planned)

- Status: Production (2024+)
- FPGA: Altera Cyclone 5 A5
- CPU: Apollo 68080 (64-bit AMMX acceleration)
- Chipset: Super AGA (32-bit TrueColor RTG)
- RAM: 512MB DDR3
- Compatibility: 100% Amiga 500/600/1000/1200/2000/4000/CD32
- Output: HDMI with AGA compatibility

**Note:** Active development, some stability concerns reported in 2024.

### Other Modern Hardware

- **MiSTer FPGA** - Cycle-accurate Amiga core (multiple models)
- **minimig** - Original open-source FPGA Amiga
- **PiStorm** - Raspberry Pi as Amiga accelerator

See [PLATFORM-VARIANTS.md](../PLATFORM-VARIANTS.md) for Phase 17+ extension details.

---

## Alternative Gateway Languages (Not Used)

**AmigaBASIC (1985-1989):**
- Microsoft-written, shipped with OS 1.1-1.3
- Discontinued in AmigaOS 2.0
- Slower, limited game capabilities
- Historical significance only

**Blitz Basic 2 (1990):**
- Compiled BASIC (much faster than AMOS)
- Direct hardware access, inline assembly
- Used for commercial games (Skidmarks, BlitzBombers)
- **Not chosen:** Too powerful for Phase 0 (blurs BASIC/assembly boundary)
- Mentioned in historical context

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Phase 0 and Phase 1 outlined, Phases 2-16 to be detailed
**Documentation:** High-level structure complete
