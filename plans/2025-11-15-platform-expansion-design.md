# Platform Expansion Design

**Date:** 2025-11-15
**Status:** Design Complete
**Purpose:** Define comprehensive platform coverage for Code Like It's 198x curriculum

---

## Overview

This document specifies all 71 platforms to be covered in the curriculum, spanning 1977-2005. Platforms are organized into 6 eras based on technical generation and market timing.

**Key Principles:**
- Comprehensive coverage across geographic regions (US, UK, Japan, Europe, Brazil)
- Technical diversity (different CPUs, graphics architectures, sound systems)
- Historical significance and educational value
- Emulation viability (all platforms must have quality emulators)
- Flexible curriculum sizing (512 to 32,768 lessons based on platform scope)

---

## Selection Criteria

### Primary Criteria

1. **Historical Significance**
   - Commercial importance in home market
   - Cultural impact in gaming/computing history
   - Pioneer status for technical innovations

2. **Educational Value**
   - Distinct programming challenges
   - Different architectural approaches
   - Unique hardware capabilities

3. **Technical Feasibility**
   - Quality emulation available
   - Documentation accessible
   - Toolchain support (assemblers, compilers)

4. **Geographic Diversity**
   - UK market (Sinclair, Amstrad, Acorn)
   - US market (Apple, Atari, TRS-80, consoles)
   - Japanese market (NEC, Sharp, Nintendo, Sega, Sony)
   - European market (Amiga, Atari ST)
   - Brazilian market (included via platforms popular there)

5. **Technical Diversity**
   - CPUs: 6502, Z80, 6510, 68000, ARM, MIPS, SH-2/4, PowerPC, x86
   - Architectures: 8-bit, 16-bit, 32-bit, 64-bit
   - Graphics: Tile-based, bitmap, sprite systems, 3D acceleration
   - Sound: PSG, FM synthesis, PCM, wavetable

### Exclusion Criteria

- **Arcade systems** - Emulation complexity, accessibility issues
- **Kit computers pre-1977** - Too early, limited appeal (Altair, IMSAI)
- **Business-only systems** - Not gaming-focused

---

## Era Organization

### Era 1: Pioneers (1977-1981)
**Character:** First wave home computers and consoles
**Platforms:** 9
**Total Lessons:** ~29,000

### Era 2: 8-bit Golden Age (1982-1985)
**Character:** Mass market 8-bit explosion
**Platforms:** 21
**Total Lessons:** ~95,000

### Era 3: 16-bit Emergence (1986-1989)
**Character:** Transition to 16-bit, console renaissance
**Platforms:** 8
**Total Lessons:** ~56,000

### Era 4: 16-bit Dominance (1990-1993)
**Character:** Peak cartridge era, handheld emergence
**Platforms:** 9
**Total Lessons:** ~53,000

### Era 5: 32-bit/3D Transition (1994-1999)
**Character:** CD-ROM, 3D acceleration, C/C++ development
**Platforms:** 14
**Total Lessons:** ~108,000

### Era 6: Late Retro (2000-2005)
**Character:** Modern complexity, shader models
**Platforms:** 10
**Total Lessons:** ~131,000

**Grand Total:** 71 platforms, ~472,000 lessons

---

## Platform Specifications by Era

### Era 1: Pioneers (1977-1981)

| Platform | Lesson Count | Language Progression | Notes |
|----------|--------------|---------------------|-------|
| Apple II | 4,096 | Applesoft BASIC → 6502 Assembly | Historic importance, extensive software library |
| Atari 400/800 | 4,096 | Atari BASIC → 6502 Assembly | Strong graphics/sound, ANTIC/GTIA chips |
| TRS-80 Model I/III | 2,048 | Level II BASIC → Z80 Assembly | Mass market success, business focus |
| Atari 2600 | 4,096 | Direct 6502 Assembly | No BASIC, pioneering console |
| VIC-20 | 2,048 | VIC BASIC → 6502 Assembly | First million-seller computer |
| TI-99/4A | 2,048 | TI BASIC → TMS9900 Assembly | Unique 16-bit CPU in 8-bit era |
| ZX81 | 2,048 | Sinclair BASIC → Z80 Assembly | Ultra-low-cost pioneer, UK market |
| Bally Astrocade | 512 | BASIC → Z80 Assembly | Underrated console, limited curriculum |
| Commodore PET | 512 | Commodore BASIC → 6502 Assembly | Limited gaming focus, smaller curriculum |

**Era 1 Total:** 21,504 lessons

### Era 2: 8-bit Golden Age (1982-1985)

| Platform | Lesson Count | Language Progression | Notes |
|----------|--------------|---------------------|-------|
| **Commodore 64** | **8,192** | **C64 BASIC → 6510 Assembly** | **Current curriculum base** |
| **ZX Spectrum** | **8,192** | **Sinclair BASIC → Z80 Assembly** | **Current curriculum base** |
| BBC Micro | 4,096 | BBC BASIC → 6502 Assembly | Educational excellence, UK market |
| MSX | 4,096 | MSX BASIC → Z80 Assembly | Japanese standard, international reach |
| Amstrad CPC (464/664/6128) | 4,096 | Locomotive BASIC → Z80 Assembly | Merged variants, UK/Europe success |
| Jupiter Ace | 1,024 | Forth | Unique Forth-based system, counterpoint |
| Dragon 32/64 | 2,048 | Dragon BASIC → 6809 Assembly | Tandy CoCo relative, UK market |
| Oric-1/Atmos | 2,048 | Oric BASIC → 6502 Assembly | UK market, interesting sound chip |
| Enterprise 64/128 | 1,024 | BASIC → Z80 Assembly | Ambitious failure, interesting architecture |
| SAM Coupé | 1,024 | SAM BASIC → Z80 Assembly | Late 8-bit, Spectrum successor |
| PC-8801 | 4,096 | N88-BASIC → Z80 Assembly | Japanese market dominance |
| FM-7 | 2,048 | F-BASIC → 6809 Assembly | Japanese market, 6809 CPU |
| Tandy Color Computer | 2,048 | Color BASIC → 6809 Assembly | US market, 6809 architecture |
| Mattel Intellivision | 2,048 | Direct CP1610 Assembly | No BASIC, unique controller |
| ColecoVision | 2,048 | Direct Z80 Assembly | No BASIC, strong arcade ports |
| Vectrex | 1,024 | Direct 6809 Assembly | Vector graphics, unique system |
| Sinclair QL | 2,048 | SuperBASIC → 68008 Assembly | Early 68000-family, multitasking |
| Memotech MTX | 512 | MTX BASIC → Z80 Assembly | Rare UK system, limited curriculum |
| Tatung Einstein | 512 | Xtal BASIC → Z80 Assembly | Rare UK system, CP/M compatible |
| Sord M5 | 512 | BASIC I → Z80 Assembly | Japanese/European market, limited |
| SG-1000 | 1,024 | Direct Z80 Assembly | Sega's first console, Japanese market |

**Era 2 Total:** 54,528 lessons

### Era 3: 16-bit Emergence (1986-1989)

| Platform | Lesson Count | Language Progression | Notes |
|----------|--------------|---------------------|-------|
| **Amiga (OCS/ECS/AGA)** | **8,192** | **AMOS BASIC → 68000 Assembly** | **Merged variants, current curriculum** |
| **NES/Famicom** | **8,192** | **Direct 6502 Assembly** | **Current curriculum, no BASIC** |
| Atari ST/TT/Falcon | 8,192 | GFA BASIC → 68000 Assembly | Merged variants, music/MIDI focus |
| Acorn Archimedes | 4,096 | BBC BASIC → ARM Assembly | First ARM system, RISC pioneer |
| Sharp X68000 | 4,096 | X-BASIC → 68000 Assembly | Japanese arcade-quality system |
| Sega Master System | 2,048 | Direct Z80 Assembly | No BASIC, console focus |
| PC Engine/TurboGrafx-16 | 4,096 | Direct HuC6280 Assembly | Japanese success, unique CPU |
| Genesis/Mega Drive + Sega CD | 8,192 | Direct 68000 Assembly | Merged with add-on, 16-bit flagship |

**Era 3 Total:** 47,104 lessons

### Era 4: 16-bit Dominance (1990-1993)

| Platform | Lesson Count | Language Progression | Notes |
|----------|--------------|---------------------|-------|
| SNES/Super Famicom | 8,192 | Direct 65816 Assembly | 16-bit 6502 evolution, Mode 7 |
| Neo Geo AES + Neo Geo CD | 4,096 | Direct 68000 + Z80 Assembly | Merged variants, arcade-perfect |
| Game Boy + Game Boy Color | 4,096 | Direct Z80-like Assembly | Merged variants, handheld pioneer |
| Game Gear | 2,048 | Direct Z80 Assembly | Sega handheld, Master System architecture |
| Atari Lynx | 2,048 | Direct 65SC02 Assembly | First color handheld, unique hardware |
| FM Towns (including Marty) | 4,096 | Towns BASIC → 386 Assembly | Japanese multimedia pioneer, merged Marty |
| PC-9801 | 4,096 | N88-BASIC → 8086/286/386 Assembly | Japanese DOS platform dominance |
| Sharp X1 | 2,048 | HuBASIC → Z80 Assembly | Japanese market, interesting architecture |
| TurboGrafx-CD | - | - | Merged with PC Engine in Era 3 |

**Era 4 Total:** 30,624 lessons (not counting merged TG-CD)

### Era 5: 32-bit/3D Transition (1994-1999)

**Note:** C/C++ becomes primary language for most platforms, with assembly for optimization.

| Platform | Lesson Count | Language Progression | Notes |
|----------|--------------|---------------------|-------|
| PlayStation | 16,384 | C/C++ + MIPS Assembly | 3D pioneer, CD-ROM standard |
| Sega Saturn | 8,192 | C/C++ + SH-2 Assembly | Dual-CPU complexity, 2D excellence |
| Nintendo 64 | 8,192 | C/C++ + MIPS Assembly | Cartridge holdout, unique architecture |
| 3DO | 2,048 | C/C++ + ARM Assembly | Ambitious multimedia platform |
| Atari Jaguar | 2,048 | C + 68000/RISC Assembly | Flawed 64-bit claim, interesting hardware |
| Virtual Boy | 1,024 | C/C++ + V810 Assembly | Commercial failure, unique 3D approach |
| Neo Geo Pocket Color | 2,048 | C + TLCS-900H Assembly | Excellent handheld, SNK quality |
| WonderSwan/WonderSwan Color | 2,048 | C + V30MG Assembly | Japanese handheld, low power design |
| Game.com | 512 | C + Sharp SM8521 Assembly | Tiger Electronics handheld, limited |
| PC (DOS/Win95) | 16,384 | C/C++ + x86 Assembly | DOS → Windows transition, massive scope |
| PowerPC Mac (System 7-9) | 4,096 | C/C++ + PowerPC Assembly | RISC transition, Mac gaming era |
| Acorn RiscPC | 2,048 | C + ARM Assembly | ARM evolution, StrongARM |
| PC-FX | 1,024 | C + V810 Assembly | NEC's failed successor, limited library |
| Apple Pippin | 512 | C/C++ + PowerPC Assembly | Failed console, limited curriculum |

**Era 5 Total:** 66,560 lessons

### Era 6: Late Retro (2000-2005)

**Note:** Modern C/C++ development with shader programming, limited assembly optimization.

| Platform | Lesson Count | Language Progression | Notes |
|----------|--------------|---------------------|-------|
| Dreamcast | 8,192 | C/C++ + SH-4 Assembly | Sega's swan song, online pioneer |
| PlayStation 2 | 32,768 | C/C++ + MIPS/VU Assembly | Massive scope, emotion engine complexity |
| GameCube | 8,192 | C/C++ + PowerPC Assembly | Nintendo architecture, Dolphin SDK |
| Xbox | 8,192 | C/C++ + x86 Assembly | PC architecture in console, DirectX |
| Game Boy Advance | 4,096 | C/C++ + ARM Assembly | 32-bit handheld, 2D excellence |
| N-Gage | 1,024 | C/C++ + ARM Assembly | Nokia phone/console hybrid |
| Gizmondo | 512 | C/C++ + ARM Assembly | Commercial failure, Windows CE |
| Tapwave Zodiac | 512 | C/C++ + ARM Assembly | PDA/console hybrid, Palm OS |
| GP32 | 1,024 | C/C++ + ARM Assembly | Korean handheld, homebrew friendly |
| PC (WinXP/DirectX 9) | 32,768 | C/C++ + x86 Assembly + HLSL | Shader model era, massive scope |

**Era 6 Total:** 97,280 lessons

---

## Merged Platform Documentation

The following platforms are treated as unified curricula despite hardware variants:

### Same Curriculum, Progressive Coverage

1. **Amiga (OCS/ECS/AGA)** - Single curriculum covers chipset evolution
   - OCS: Original Chip Set (A1000, A500)
   - ECS: Enhanced Chip Set (A500+, A600)
   - AGA: Advanced Graphics Architecture (A1200, A4000)

2. **Atari ST/TT/Falcon** - Single curriculum covers platform evolution
   - ST: Original 68000 system
   - TT: 68030-based workstation
   - Falcon: DSP-enhanced final model

3. **Amstrad CPC (464/664/6128)** - Memory variants, same architecture
   - 464: 64KB RAM, cassette
   - 664: 64KB RAM, built-in disk
   - 6128: 128KB RAM, built-in disk

4. **Game Boy + Game Boy Color** - GBC adds features but maintains compatibility
   - GB: Original monochrome
   - GBC: Color screen, double CPU speed, backward compatible

5. **Genesis/Mega Drive + Sega CD** - Add-on merges into base curriculum
   - Genesis/MD: Base 16-bit console
   - Sega CD: CD-ROM add-on, same 68000 CPU + additional features

6. **Neo Geo AES + Neo Geo CD** - Same MVS arcade hardware, different media
   - AES: Cartridge-based home system
   - CD: CD-ROM version, same architecture

7. **FM Towns (including Marty)** - Console variant merges with computer
   - FM Towns: Multimedia computer
   - Marty: Console variant, same architecture

8. **WonderSwan/WonderSwan Color** - Color adds features, maintains compatibility
   - WS: Original monochrome
   - WSC: Color screen, backward compatible

---

## Curriculum Size Assignments

### Micro Curricula (512-1,024 lessons)
**Use for:** Commercial failures, very limited platforms, niche systems

- Bally Astrocade (512)
- Commodore PET (512)
- Jupiter Ace (1,024)
- Enterprise 64/128 (1,024)
- SAM Coupé (1,024)
- Memotech MTX (512)
- Tatung Einstein (512)
- Sord M5 (512)
- SG-1000 (1,024)
- Vectrex (1,024)
- Virtual Boy (1,024)
- Game.com (512)
- PC-FX (1,024)
- Apple Pippin (512)
- N-Gage (1,024)
- Gizmondo (512)
- Tapwave Zodiac (512)
- GP32 (1,024)

### Small Curricula (2,048 lessons)
**Use for:** Niche platforms, standard 8-bit systems, limited handheld systems

- TRS-80 Model I/III (2,048)
- VIC-20 (2,048)
- TI-99/4A (2,048)
- ZX81 (2,048)
- Dragon 32/64 (2,048)
- Oric-1/Atmos (2,048)
- Tandy Color Computer (2,048)
- FM-7 (2,048)
- Mattel Intellivision (2,048)
- ColecoVision (2,048)
- Sinclair QL (2,048)
- Sega Master System (2,048)
- Game Gear (2,048)
- Atari Lynx (2,048)
- Sharp X1 (2,048)
- 3DO (2,048)
- Atari Jaguar (2,048)
- Neo Geo Pocket Color (2,048)
- WonderSwan/WonderSwan Color (2,048)
- Acorn RiscPC (2,048)

### Standard Curricula (4,096-8,192 lessons)
**Use for:** Major 8-bit platforms, important 16-bit systems, significant consoles

- Apple II (4,096)
- Atari 400/800 (4,096)
- Atari 2600 (4,096)
- **Commodore 64 (8,192)** - Current base
- **ZX Spectrum (8,192)** - Current base
- BBC Micro (4,096)
- MSX (4,096)
- Amstrad CPC (4,096)
- PC-8801 (4,096)
- **Amiga (8,192)** - Current base
- **NES/Famicom (8,192)** - Current base
- Atari ST/TT/Falcon (8,192)
- Acorn Archimedes (4,096)
- Sharp X68000 (4,096)
- PC Engine/TurboGrafx-16 (4,096)
- Genesis/Mega Drive + Sega CD (8,192)
- SNES/Super Famicom (8,192)
- Neo Geo AES + Neo Geo CD (4,096)
- Game Boy + Game Boy Color (4,096)
- FM Towns (4,096)
- PC-9801 (4,096)
- PowerPC Mac (4,096)
- Game Boy Advance (4,096)

### Large Curricula (8,192-16,384 lessons)
**Use for:** Major 16-bit/early 32-bit platforms, complex architectures

- Sega Saturn (8,192)
- Nintendo 64 (8,192)
- Dreamcast (8,192)
- GameCube (8,192)
- Xbox (8,192)

### Massive Curricula (16,384-32,768 lessons)
**Use for:** Platforms with extraordinary depth and scope

- PlayStation (16,384)
- PC DOS/Win95 (16,384)
- PlayStation 2 (32,768)
- PC WinXP/DirectX 9 (32,768)

---

## Language Progression Strategy

### Eras 1-4 (1977-1993): BASIC → Assembly

**Phase 0 (Gateway):** 64 lessons - BASIC programming
- Game-first approach for novices/children
- Platforms with available BASIC interpreters
- NOT AVAILABLE: Consoles without BASIC (Atari 2600, NES, etc.)

**Phases 1-8 (Mastery):** ~4,000-8,000 lessons - Assembly programming
- Deep hardware access
- Professional techniques
- Real-time game development

### Eras 5-6 (1994-2005): C/C++ + Assembly

**Hybrid Approach:**
- **Primary:** C/C++ for game logic, structure
- **Secondary:** Assembly for optimization, hardware access
- **Advanced:** Shader programming (Era 6 only)

**Rationale:**
- Professional development moved to C/C++ by mid-1990s
- 3D math and physics require higher-level languages
- Assembly remains important for performance-critical sections
- Shader programming becomes essential (Era 6)

**Potential Structure:**
- Phase 0: C/C++ fundamentals (if applicable)
- Phases 1-4: Game engine architecture in C/C++
- Phases 5-6: Assembly optimization techniques
- Phases 7-8: Platform-specific advanced features
- Phase 9+: Shader programming, modern techniques (Era 6)

**Note:** Exact structure for Eras 5-6 to be refined when reached in curriculum development.

---

## Expansion Phasing Recommendations

### Current Status (January 2025)
**Active Platforms:** 4
- Commodore 64 (8,192 lessons) - BASIC + 6510 Assembly
- ZX Spectrum (8,192 lessons) - BASIC + Z80 Assembly
- Amiga (8,192 lessons) - AMOS BASIC + 68000 Assembly
- NES/Famicom (8,192 lessons) - Direct 6502 Assembly

**Total Active:** 32,768 lessons across 4 platforms

### Expansion Strategy

**Principle:** Add 2-4 platforms at a time to maintain quality and allow parallel development.

**Priority Tier 1 (Next 4 Platforms):**
1. **Apple II** (4,096) - Era 1 pioneer, educational importance
2. **Atari 2600** (4,096) - Era 1 console, unique challenges
3. **BBC Micro** (4,096) - Era 2 educational excellence
4. **Atari ST** (8,192) - Era 3 professional system

**Rationale:** Mix of eras, different CPUs (6502, Z80, 68000), both computer and console, different markets (US, UK).

**Priority Tier 2 (Next 4 Platforms):**
1. **SNES** (8,192) - Era 4 console dominance
2. **Genesis/Mega Drive** (8,192) - Era 3 console competition
3. **MSX** (4,096) - Era 2 Japanese standard
4. **Amstrad CPC** (4,096) - Era 2 UK market

**Priority Tier 3 (Next 4 Platforms):**
1. **Game Boy** (4,096) - Era 4 handheld revolution
2. **PlayStation** (16,384) - Era 5 3D pioneer
3. **PC-8801** (4,096) - Era 2 Japanese dominance
4. **Sharp X68000** (4,096) - Era 3 arcade-quality

**Ongoing:** Continue adding 2-4 platforms per phase, balancing:
- Era representation
- Geographic diversity
- CPU architecture variety
- Computer vs console mix
- Market size and historical importance

---

## Technical Diversity Coverage

### CPU Architectures

| CPU Family | Platforms | Example |
|------------|-----------|---------|
| 6502 | 14 | Apple II, Atari 400/800, Atari 2600, VIC-20, C64, NES, PC Engine, Lynx |
| Z80 | 18 | TRS-80, ZX81, ZX Spectrum, MSX, CPC, Master System, Game Gear, Game Boy |
| 6809 | 4 | Dragon 32/64, FM-7, Tandy CoCo, Vectrex |
| 68000 | 8 | Amiga, Atari ST, Genesis, Neo Geo, Sharp X68000, Sinclair QL, Jaguar (68000 component) |
| ARM | 8 | Archimedes, 3DO, NGPC, WonderSwan, GBA, N-Gage, Gizmondo, Zodiac, GP32, RiscPC |
| MIPS | 3 | PlayStation, Nintendo 64, PS2 |
| x86 | 4 | PC-9801, FM Towns, PC (DOS/Win95), PC (WinXP) |
| PowerPC | 3 | PowerPC Mac, GameCube, Xbox (modified) |
| SH-2/SH-4 | 2 | Sega Saturn (SH-2), Dreamcast (SH-4) |
| Other | 7 | TI-99/4A (TMS9900), Intellivision (CP1610), V810 (Virtual Boy, PC-FX), etc. |

### Graphics Architectures

- **Character/tile-based:** ZX Spectrum, C64, BBC Micro, MSX, NES, Master System
- **Bitmap:** Amiga, Atari ST, Archimedes
- **Sprite systems:** C64, NES, Genesis, SNES, Neo Geo
- **3D acceleration:** PlayStation, Saturn, N64, Dreamcast, PS2, Xbox, GameCube
- **Shader models:** PC (DirectX 9), Xbox

### Sound Systems

- **Beeper:** ZX81, ZX Spectrum (early)
- **PSG (Programmable Sound Generator):** TI-99/4A, ColecoVision, Master System
- **Custom chips:** C64 (SID), Amiga (Paula), NES (APU), SNES (SPC700)
- **FM synthesis:** Genesis (YM2612), PC-8801, X68000
- **PCM/sample-based:** Amiga, later consoles
- **Wavetable:** GBA, later systems

---

## Geographic Market Coverage

### United Kingdom
- ZX81, ZX Spectrum, Dragon 32/64, Oric-1/Atmos, BBC Micro, Amstrad CPC, Enterprise, SAM Coupé, Sinclair QL, Jupiter Ace, Memotech MTX, Tatung Einstein, Acorn Archimedes, Acorn RiscPC

### United States
- Apple II, TRS-80, Atari 400/800, Atari 2600, VIC-20, C64, Tandy CoCo, Intellivision, ColecoVision, Vectrex, Atari ST, Atari Lynx, Atari Jaguar, 3DO, Xbox

### Japan
- PC-8801, FM-7, Sharp X1, Sharp X68000, MSX, SG-1000, Master System (initial), PC Engine, NES/Famicom, Genesis/Mega Drive, SNES, Neo Geo, Game Boy, PlayStation, Saturn, N64, Dreamcast, PS2, GameCube, WonderSwan, NGPC, PC-FX, PC-9801, FM Towns

### Europe (Continental)
- Amiga (commoditized in UK but German/Netherlands design)
- Atari ST (strong in Germany, France)
- MSX (Netherlands, Spain)

### International/Multi-Regional
- Sega systems (Japan/US/Europe)
- Nintendo systems (Japan/US/Europe)
- Sony PlayStation systems (worldwide)
- PC platforms (worldwide)

---

## Emulation Viability

All 71 platforms have mature, actively maintained emulators:

### Excellent Emulation
- C64 (VICE), ZX Spectrum (Fuse), Amiga (FS-UAE), NES (FCEUX, Mesen), SNES (bsnes), Genesis (Gens), PlayStation (DuckStation), N64 (Project64), Dreamcast (Redream), PS2 (PCSX2)

### Good Emulation
- Apple II (AppleWin), Atari 2600 (Stella), Atari ST (Hatari), MSX (openMSX), BBC Micro (BeebEm), Game Boy (SameBoy), Saturn (Mednafen), GBA (mGBA)

### Adequate Emulation
- Most remaining platforms have functional emulators
- Some rare platforms may require specific configurations
- All platforms tested and confirmed workable for lesson development

### Toolchain Support
- **Assembly:** Cross-assemblers available for all platforms (ACME, ca65, vasm, sjasmplus, etc.)
- **C/C++:** Modern cross-compilers for all Era 5-6 platforms
- **BASIC:** Emulators include built-in BASIC interpreters OR tools to convert modern BASIC to tokenized form

---

## Summary

**Total Platforms:** 71
**Total Estimated Lessons:** ~472,000
**Eras Covered:** 6 (1977-2005)
**CPU Architectures:** 10+ families
**Geographic Regions:** 4 primary markets
**Current Active Platforms:** 4 (C64, Spectrum, Amiga, NES)
**Next Expansion:** 4 platforms (Apple II, Atari 2600, BBC Micro, Atari ST)

**Development Approach:**
- Add 2-4 platforms per phase
- Maintain quality over speed
- Balance era/region/architecture diversity
- Flexible curriculum sizing (512-32,768 lessons)
- Hybrid language approach for modern platforms (C/C++ + Assembly)

**Foundation Complete:** Ready for systematic platform expansion.
