# Nintendo Entertainment System (NES) Curriculum

**Platform:** Nintendo Entertainment System (NES/Famicom)
**Gateway Language:** None (assembly-only platform)
**Assembly Language:** 6502
**Total Curriculum:** 7,744 lessons (Phases 1-16)

## Overview

The NES curriculum teaches programming through assembly language from the start. Unlike home computers with BASIC interpreters, the NES was a dedicated gaming console with ROM cartridges—there is no Phase 0. Students begin directly with 6502 assembly and hardware programming.

## Curriculum Structure

### Phase 1: 6502 Assembly + Hardware Fundamentals (512 lessons)
**Language:** 6502 Assembly
**Focus:** Game-first hardware mastery
**Deliverables:** 16+ complete games at 60fps

Learn NES programming through classic arcade game development:
- 6502 instruction set fundamentals
- PPU (Picture Processing Unit) programming
- Background tile rendering
- Hardware sprite system (64 OAM entries)
- APU (Audio Processing Unit) basics
- Controller input handling
- Scrolling techniques

[Read Phase 1 Overview →](PHASE-1-CURRICULUM.md)

### Phases 2-16 (7,232 lessons)
**Status:** To be detailed

Advanced NES development across specialized genres:
- Action games (platformers, shooters)
- Advanced PPU techniques
- Mapper chips (MMC1, MMC3, etc.)
- Advanced audio programming
- Complex game systems
- Multi-cart development

## Platform Characteristics

### Hardware Specifications

**CPU:**
- Ricoh 2A03 (6502-based) @ 1.79MHz (NTSC) / 1.66MHz (PAL)
- No decimal mode (BCD)
- 2KB internal RAM
- 6 audio channels built into CPU

**PPU (Picture Processing Unit):**
- 256×240 resolution (NTSC)
- 64 colours available (52 unique)
- 8×8 pixel tiles
- 2 pattern tables (256 tiles each)
- 4 nametables (background maps)
- 64 hardware sprites (8×8 or 8×16)
- 8 sprites per scanline limit

**APU (Audio Processing Unit):**
- 2 pulse wave channels
- 1 triangle wave channel
- 1 noise channel
- 1 DMC (sample) channel
- Optional cartridge expansion audio

**Memory:**
- 2KB CPU RAM
- 2KB PPU RAM (nametables)
- 256 bytes OAM (sprite data)
- Cartridge ROM (16KB+ PRG)
- Cartridge CHR ROM/RAM (8KB+)

### Unique Features

**Strengths:**
- Dedicated graphics hardware (PPU)
- 64 hardware sprites
- Smooth scrolling capabilities
- Rich colour palette
- Powerful audio system
- Mature development ecosystem

**Constraints:**
- 8 sprites per scanline
- Tile-based graphics only
- Limited CPU RAM (2KB)
- No framebuffer (direct PPU control)
- Cartridge-based development
- Timing-critical PPU access

**Creative Solutions:**
- Sprite multiplexing for >8 sprites per line
- Nametable mirroring for scrolling
- Mid-frame PPU updates (status bar)
- Mapper chips extend capabilities
- CHR-RAM for dynamic graphics

## Development Tools

**Emulators:**
- Mesen (recommended - excellent debugging)
- FCEUX (development features)
- Nintendulator (accuracy)

**Assemblers:**
- ca65/ld65 (cc65 toolchain - recommended)
- asm6 (simple, fast)
- nesasm (classic)

**Graphics Tools:**
- NES Screen Tool (tile/nametable editor)
- YY-CHR (CHR data editor)
- NEXXT (integrated NES editor)

**Audio Tools:**
- FamiTracker (music/SFX composition)
- FamiStudio (modern tracker)

## Learning Path

1. **Start with Phase 1** - 6502 assembly fundamentals
2. **Master the PPU** - Understand tile and sprite rendering
3. **Build complete games** - Experience hardware constraints
4. **Learn scrolling** - Nametable manipulation
5. **Add sound** - APU programming
6. **Specialize in genres** - Deep dive into game types
7. **Explore mappers** - Extended capabilities

## Historical Context

The Nintendo Entertainment System (1983-2003) revitalized the video game industry:
- 61.91 million units sold worldwide
- Established Nintendo as gaming leader
- Introduced iconic franchises (Mario, Zelda, Metroid)
- Defined console gaming standards
- Created third-party licensing model
- Foundation of modern gaming industry

**Iconic games:**
- Super Mario Bros. (Shigeru Miyamoto)
- The Legend of Zelda (Shigeru Miyamoto)
- Metroid (Gunpei Yokoi)
- Mega Man series (Capcom)
- Castlevania series (Konami)

## Prerequisites

None - Phase 1 is designed for assembly beginners who want to learn through game development.

## Comparison with Other Platforms

| Aspect | NES | Commodore 64 | ZX Spectrum |
|--------|-----|--------------|-------------|
| **Gateway Language** | None | BASIC V2 | Sinclair BASIC |
| **CPU** | 6502 @ 1.79MHz | 6510 @ 1MHz | Z80 @ 3.5MHz |
| **Graphics** | PPU (tile+sprite) | VIC-II (8 sprites) | Software sprites |
| **Sound** | APU (5 channels) | SID chip | BEEP/AY chip |
| **Sprites** | 64 (8 per line) | 8 hardware | Software only |
| **Display** | 256×240 tiles | 320×200 pixels | 256×192 pixels |
| **Purpose** | Game console | Home computer | Home computer |
| **Teaching Focus** | Cartridge-based dev | General computing | Creative constraints |

The NES teaches hardware programming without the BASIC foundation—students learn assembly-first development.

## Platform Variants

The NES has no modern reimagination equivalent to MEGA65 or Spectrum Next. The curriculum completes at Phase 16 on original hardware or emulators.

**Available hardware:**
- Original NES/Famicom
- NES Classic Edition (2016 - emulation device)
- Analogue Nt (FPGA recreation)
- Everdrive N8 (flash cartridge for development)

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Phase 1 outlined, Phases 2-16 to be detailed
**Documentation:** High-level structure complete
