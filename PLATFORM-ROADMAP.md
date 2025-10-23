# Platform Roadmap

**Purpose:** Master plan for all vintage computing platforms in the Code198x curriculum
**Goal:** Extensively document all vintage computing platforms with complete programming curricula
**Status:** Living document - priorities and platforms may shift based on community interest and research

---

## Philosophy

The Code198x curriculum aims to preserve and teach programming on **all significant vintage computing platforms** from the late 1970s through early 1990s. Each platform offers unique architectural insights, programming techniques, and historical context.

### Selection Criteria

Platforms are chosen based on:

1. **Historical significance** - Impact on computing/gaming history
2. **Architectural diversity** - Unique CPU, graphics, or sound systems
3. **Geographic representation** - North America, Europe, Japan, etc.
4. **Pedagogical value** - Teaches distinct programming concepts
5. **Community interest** - Active retro computing/gaming community
6. **Available tooling** - Emulators, assemblers, documentation

### Curriculum Structure (All Platforms)

- **Phase 0:** Gateway language (BASIC, etc.) - 64 lessons [*if applicable*]
- **Phases 1-16:** Assembly language mastery - 7,680 lessons (or 8,192 if no Phase 0)
- **Phase 17+:** Modern hardware extensions - 512+ lessons [*if applicable*]

**Total per platform:** 8,256 lessons (with Phase 0) or 7,744 lessons (assembly-only)

---

## Platform Status Overview

### Active Development (Documentation In Progress)

| Platform | Directory | Gateway Language | Assembly | Status |
|----------|-----------|------------------|----------|--------|
| Commodore 64 | `commodore-64/` | BASIC V2 | 6510 | Phase 0 active, Phase 1+ outlined |
| ZX Spectrum | `sinclair-zx-spectrum/` | Sinclair BASIC | Z80 | Outlined |
| NES | `nintendo-entertainment-system/` | None | 6502 | Outlined |
| Amiga | `commodore-amiga/` | AMOS Professional | 68000 | Outlined |

### Priority Tier 1 (Next to Document)

| Platform | Directory | Gateway Language | Assembly | Rationale |
|----------|-----------|------------------|----------|-----------|
| Atari ST | `atari-st/` | GFA BASIC | 68000 | Amiga rival, MIDI powerhouse |
| MSX | `msx/` | MSX-BASIC | Z80 | Japanese standard, Konami heritage |
| BBC Micro | `bbc-micro/` | BBC BASIC | 6502 | Best BASIC, educational design |
| Atari 8-bit | `atari-8-bit/` | Atari BASIC | 6502 | Early custom chips, ANTIC/GTIA |

### Priority Tier 2 (Future Development)

| Platform | Directory | Gateway Language | Assembly | Rationale |
|----------|-----------|------------------|----------|-----------|
| Dragon/CoCo | `tandy-trs-80-coco-dragon/` | Extended Color BASIC | 6809 | Unique CPU, British heritage |
| Apple II | `apple-ii/` | Applesoft BASIC | 6502 | Historical significance |
| Amstrad CPC | `amstrad-cpc/` | Locomotive BASIC | Z80 | British micro, integrated design |
| Atari 2600 | `atari-2600/` | None | 6507 | Console constraints, racing the beam |

### Under Consideration

| Platform | Directory | Gateway Language | Assembly | Notes |
|----------|-----------|------------------|----------|-------|
| TI-99/4A | `ti-99-4a/` | TI BASIC | TMS9900 | 16-bit CPU, limited library |
| VIC-20 | `commodore-vic-20/` | BASIC V2 | 6502 | Pre-C64 Commodore |
| Sega Master System | `sega-master-system/` | None | Z80 | Console, NES competitor |
| Game Boy | `nintendo-game-boy/` | None | SM83/Z80 | Portable, huge library |
| Commodore Plus/4 | `commodore-plus-4/` | BASIC 3.5 | 7501 | TED chipset |
| Commodore 128 | `commodore-128/` | BASIC 7.0 | 8502/Z80 | Dual-CPU, CP/M compatible |
| ZX81 | `sinclair-zx81/` | Sinclair BASIC | Z80 | Extreme constraints |
| Acorn Electron | `acorn-electron/` | BBC BASIC | 6502 | Budget BBC Micro |
| Oric-1/Atmos | `oric/` | Oric BASIC | 6502 | French micro |
| Sam Coupé | `sam-coupe/` | SAM BASIC | Z80 | Post-Spectrum British micro |

---

## Detailed Platform Specifications

### Active Development

#### Commodore 64 (1982-1994)
- **Directory:** `commodore-64/`
- **Gateway Language:** BASIC V2 (slow interpreter, requires machine language for games)
- **Assembly:** MOS 6510 @ 1MHz (6502 variant)
- **Graphics:** VIC-II (320×200, 8 hardware sprites, 16 colors)
- **Sound:** SID chip (3 voices, filters, ring modulation)
- **RAM:** 64KB (38KB BASIC free)
- **Modern Variants:**
  - **MEGA65** (Phase 17+) - VIC-IV, 45GS02 CPU, 40MHz
  - Ultimate 64, C64 Reloaded MK2 (reference only)
- **Unique Teaching:** Hardware sprites, SID synthesis, creative 8-bit programming
- **Status:** Phase 0 lessons 1-11 complete, Phase 1+ outlined

---

#### Sinclair ZX Spectrum (1982-1992)
- **Directory:** `sinclair-zx-spectrum/`
- **Gateway Language:** Sinclair BASIC (fast interpreter, keyword entry)
- **Assembly:** Z80 @ 3.5MHz
- **Graphics:** ULA (256×192, attribute system, colour clash)
- **Sound:** BEEP (1-bit) / AY-3-8912 (128K model)
- **RAM:** 48KB / 128KB
- **Modern Variants:**
  - **Spectrum Next** (Phase 17+) - Z80N @ 28MHz, 128 sprites, tilemap, copper
  - ZX-Uno (reference only)
- **Unique Teaching:** Software sprites, attribute system, creative constraints
- **Status:** Outlined

---

#### Nintendo Entertainment System (1983-2003)
- **Directory:** `nintendo-entertainment-system/`
- **Gateway Language:** None (assembly-only)
- **Assembly:** MOS 6502 @ 1.79MHz (NTSC)
- **Graphics:** PPU (256×240, 64 OAM sprites, 8 per scanline)
- **Sound:** APU (5 channels: 2 pulse, triangle, noise, DMC)
- **ROM:** Cartridge-based (16KB+ PRG, 8KB+ CHR)
- **Modern Variants:** None (Analogue Nt, MiSTer are accurate recreations)
- **Unique Teaching:** Cartridge development, PPU timing, mapper chips, VBlank budgeting
- **Status:** Outlined

---

#### Commodore Amiga (1985-1996)
- **Directory:** `commodore-amiga/`
- **Gateway Language:** AMOS Professional (game-focused BASIC, 1992)
- **Assembly:** Motorola 68000 @ 7MHz
- **Graphics:** OCS/ECS (4096 colors), AGA (256 colors from 16.8M)
- **Sound:** Paula (4-channel 8-bit PCM stereo)
- **Custom Chips:** Copper (display list), Blitter (fast bitblt)
- **RAM:** 512KB-2MB Chip RAM
- **Modern Variants:**
  - **Vampire V4** (Phase 17+) - Apollo 68080, Super AGA, AMMX
  - MiSTer, minimig (reference only)
- **Unique Teaching:** Copper programming, blitter operations, multimedia architecture
- **Model Progression:** A500 (OCS) → A1200 (AGA) in Phases 10-12
- **Status:** Outlined

---

### Priority Tier 1

#### Atari ST (1985-1993)
- **Directory:** `atari-st/`
- **Gateway Language:** GFA BASIC (compiled, fast, excellent for games)
- **Assembly:** Motorola 68000 @ 8MHz
- **Graphics:** Shifter (320×200, 16 colors from 512, no hardware sprites)
- **Sound:** YM2149 (3-channel PSG, same as Spectrum 128K)
- **RAM:** 512KB-4MB
- **MIDI:** Built-in ports (music production standard)
- **Modern Variants:** MiSTer FPGA (accurate recreation)
- **Unique Teaching:** Minimalist architecture (no custom chips), MIDI integration, CPU-driven graphics
- **Comparison:** Amiga's business/MIDI-focused rival, different philosophy (simplicity vs multimedia)

---

#### MSX (1983-1995)
- **Directory:** `msx/`
- **Gateway Language:** MSX-BASIC (Microsoft BASIC variant)
- **Assembly:** Z80 @ 3.58MHz
- **Graphics:** TI TMS9918 VDP (256×192, 16 colors, hardware sprites)
- **Sound:** PSG (3-channel), later SCC/MSX-MUSIC/MSX-AUDIO
- **RAM:** 16KB-64KB (MSX1), 64KB+ (MSX2/2+)
- **Cartridge Slots:** 2 slots standard (ROM cartridge-based software)
- **Modern Variants:** None (various FPGA recreations)
- **Unique Teaching:** Japanese game design, cartridge development, MSX standard (multiple manufacturers)
- **Model Progression:** MSX1 → MSX2 (V9938 VDP) → MSX2+ (V9958, 512 colors)
- **Notable Games:** Metal Gear, Gradius, Parodius (Konami), many Japanese-exclusive titles

---

#### BBC Micro (1981-1994)
- **Directory:** `bbc-micro/`
- **Gateway Language:** BBC BASIC (best 8-bit BASIC: structured, inline assembly, procedures)
- **Assembly:** 6502 @ 2MHz
- **Graphics:** 6845 CRTC (multiple modes), Teletext Mode 7
- **Sound:** SN76489 (3-channel + noise)
- **RAM:** 32KB (Model B standard)
- **Educational Design:** BBC Computer Literacy Project
- **Modern Connection:** Acorn → ARM → Raspberry Pi lineage
- **Modern Variants:** None (various recreations)
- **Unique Teaching:** Best-in-class BASIC, educational philosophy, ARM heritage
- **Notable Software:** Elite (original platform), educational software

---

#### Atari 8-bit (1979-1992)
- **Directory:** `atari-8-bit/`
- **Models:** 400, 800, XL, XE series
- **Gateway Language:** Atari BASIC (slow but functional)
- **Assembly:** MOS 6502 @ 1.79MHz
- **Graphics:** ANTIC (DMA display list processor) + GTIA (colors/sprites)
- **Sound:** POKEY (4-channel with distortion modes)
- **RAM:** 16KB-128KB (depends on model)
- **Modern Variants:** None (various FPGA recreations)
- **Unique Teaching:** Display list programming (early DMA concept), POKEY synthesis, first consumer custom chips
- **Historical Note:** Pre-dated C64, influenced Amiga architecture

---

### Priority Tier 2

#### Dragon 32/64 & TRS-80 Color Computer (1982-1991)
- **Directory:** `tandy-trs-80-coco-dragon/`
- **Gateway Language:** Extended Color BASIC (Microsoft with graphics extensions)
- **Assembly:** Motorola 6809 @ 0.89MHz (Dragon), 0.89-1.79MHz (CoCo)
- **Graphics:** MC6847 VDG (semigraphics and text modes)
- **Sound:** 6-bit DAC via PIA (Dragon), SN76489 (CoCo 3)
- **RAM:** 32KB-64KB (Dragon), up to 512KB (CoCo 3)
- **Modern Variants:** None (MiSTer cores for both)
- **Unique Teaching:** 6809 architecture (cleanest 8-bit CPU), British Dragon heritage
- **Curriculum Approach:** Combined curriculum acknowledging both machines (architecturally identical)

---

#### Apple II (1977-1993)
- **Directory:** `apple-ii/`
- **Models:** II, II+, IIe, IIc, IIgs
- **Gateway Language:** Applesoft BASIC (floating point, slow)
- **Assembly:** MOS 6502 @ 1MHz (II/II+/IIe/IIc), 65816 @ 2.8MHz (IIgs)
- **Graphics:** No custom chips, memory-mapped framebuffer (280×192 hi-res, 6 colors)
- **Sound:** Speaker toggle (II-IIc), Ensoniq synthesizer (IIgs)
- **RAM:** 48KB-128KB (II-IIc), 256KB+ (IIgs)
- **Expansion:** 7 slots for cards
- **Modern Variants:** None (various FPGA recreations)
- **Unique Teaching:** Minimal hardware (no custom chips), expansion slot architecture
- **Historical Significance:** Launched personal computer revolution, VisiCalc, educational software

---

#### Amstrad CPC (1984-1990)
- **Directory:** `amstrad-cpc/`
- **Models:** 464, 664, 6128
- **Gateway Language:** Locomotive BASIC
- **Assembly:** Z80 @ 4MHz
- **Graphics:** Gate Array (160×200 16 colors, 320×200 4 colors, 640×200 2 colors)
- **Sound:** AY-3-8912 (3-channel PSG, same as Spectrum 128K)
- **RAM:** 64KB (464/664), 128KB (6128)
- **Integrated Design:** Built-in cassette (464) or 3" floppy (664/6128), monitor
- **Modern Variants:** None (various FPGA recreations)
- **Unique Teaching:** Integrated system design, British bedroom coder scene
- **Note:** Overlaps with Spectrum (Z80, AY chip) but different graphics architecture

---

#### Atari 2600 (1977-1992)
- **Directory:** `atari-2600/`
- **Gateway Language:** None (assembly-only)
- **Assembly:** MOS 6507 @ 1.19MHz (6502 variant, 128 bytes RAM!)
- **Graphics:** TIA (Television Interface Adapter, racing the beam)
- **Sound:** TIA (2-channel)
- **RAM:** 128 bytes (yes, bytes)
- **ROM:** 2KB-4KB cartridges (early), up to 32KB+ with bankswitching
- **Modern Variants:** None (various FPGA recreations)
- **Unique Teaching:** Extreme constraints, racing the beam, kernel programming
- **Pedagogical Value:** Teaches fundamentals with minimal resources

---

### Under Consideration (Future Tiers)

#### Sega Master System (1985-1996)
- **Directory:** `sega-master-system/`
- **Gateway Language:** None (assembly-only)
- **Assembly:** Z80 @ 3.58MHz
- **Graphics:** VDP (256×192, 32 sprites, 32 colors from 64)
- **Sound:** PSG (3-channel + noise, same as BBC Micro)
- **RAM:** 8KB, 16KB VRAM
- **Modern Variants:** None (various FPGA recreations)
- **Unique Teaching:** Console development, NES competitor, different architecture approach

---

#### Nintendo Game Boy (1989-2003)
- **Directory:** `nintendo-game-boy/`
- **Gateway Language:** None (assembly-only)
- **Assembly:** SM83 (Z80-like) @ 4.19MHz
- **Graphics:** PPU (160×144, 40 sprites, 4 shades of gray)
- **Sound:** 4-channel synthesizer
- **RAM:** 8KB, 8KB VRAM
- **Cartridges:** ROM + RAM + battery backup
- **Modern Variants:** Analogue Pocket (FPGA)
- **Unique Teaching:** Portable constraints, battery life optimization, huge game library

---

#### TI-99/4A (1981-1984)
- **Directory:** `ti-99-4a/`
- **Gateway Language:** TI BASIC
- **Assembly:** TMS9900 @ 3MHz (true 16-bit CPU)
- **Graphics:** TMS9918 VDP (same as MSX)
- **Sound:** SN76489 (3-channel PSG)
- **RAM:** 16KB (with expansion)
- **Modern Variants:** None (various FPGA recreations)
- **Unique Teaching:** 16-bit CPU architecture, limited adoption despite advanced hardware

---

## CPU Architecture Coverage

| CPU Family | Platforms | Rationale |
|------------|-----------|-----------|
| **6502 Family** | C64 (6510), NES (6502), BBC Micro, Apple II, Atari 8-bit, Atari 2600 (6507), VIC-20 | Most common 8-bit CPU, multiple variants |
| **Z80** | ZX Spectrum, MSX, Amstrad CPC, SMS, Game Boy (SM83) | Second most common, different architecture from 6502 |
| **68000 Family** | Amiga, Atari ST | 16/32-bit hybrid, professional platforms |
| **6809** | Dragon/CoCo | Cleanest 8-bit design, underrepresented |
| **TMS9900** | TI-99/4A | True 16-bit, unique architecture |

---

## Geographic & Cultural Coverage

| Region | Platforms | Cultural Context |
|--------|-----------|------------------|
| **North America** | C64, NES, Apple II, Atari 8-bit, Atari 2600, TRS-80 CoCo | US-dominated market |
| **United Kingdom** | ZX Spectrum, BBC Micro, Amstrad CPC, Dragon 32, Acorn Electron | Bedroom coder scene |
| **Europe** | Amiga, Atari ST, C64 | Gaming and demo scene |
| **Japan** | MSX, NES, Game Boy | Different game design philosophy |

---

## Modern Variant Categories

See [PLATFORM-VARIANTS.md](PLATFORM-VARIANTS.md) for detailed modern hardware policies.

**Category 1: Enhanced Reimaginations** (Phase 17+ content)
- MEGA65 (C64), Spectrum Next (Spectrum), Vampire V4 (Amiga)

**Category 2: Accurate Recreations** (mentioned for reference)
- Ultimate 64, C64 Reloaded, ZX-Uno, MiSTer cores, Analogue products

---

## Implementation Priority

### Current Focus (2025 Q1-Q2)
- ✅ Commodore 64: Phase 0 lessons 1-11 complete
- 🔄 Complete C64 Phase 0 (lessons 12-64)
- 🔄 ZX Spectrum Phase 0 outline
- 🔄 NES Phase 1 outline
- 🔄 Amiga Phase 0 outline

### 2025 Q3-Q4
- Atari ST outline
- MSX outline
- BBC Micro outline
- Atari 8-bit outline

### 2026+
- Dragon/CoCo outline
- Apple II outline
- Begin Priority Tier 2 platform development
- Community-driven platform priorities

---

## Contributing Platform Suggestions

Platforms under consideration are evaluated based on:

1. **Architectural uniqueness** - Does it teach something new?
2. **Historical impact** - Was it significant in computing/gaming history?
3. **Community interest** - Is there an active retro community?
4. **Available resources** - Emulators, documentation, tooling?
5. **Geographic diversity** - Does it represent underrepresented regions?

**Suggest platforms:** Open an issue on GitHub with rationale for inclusion.

---

## Platform Documentation Standards

Each platform requires:

### Minimum Documentation (Outline Stage)
- [ ] `README.md` - Platform overview, hardware specs, learning path
- [ ] `PHASE-1-CURRICULUM.md` - Assembly phase outline (512 lessons)
- [ ] `phase-0/overview.md` - Gateway language phase (if applicable)

### Full Documentation (Active Development)
- [ ] Detailed lesson specifications
- [ ] Hardware reference documents
- [ ] Development tool guides
- [ ] Code samples and examples
- [ ] Modern variant coverage (if applicable)

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Living document - priorities subject to change
**Long-term Goal:** Comprehensive programming curricula for all significant vintage computing platforms
