# Platform Variants and Modern Reimaginations

**Purpose:** Define how original platforms and modern reimaginations fit into the curriculum
**Status:** Architectural decision document

## Philosophy

The **entire core curriculum (Phases 0-16) is completable on original hardware or emulators**. This preserves:

1. **Historical authenticity** - Learn on the actual platform
2. **Accessibility** - Anyone with an emulator can complete the course
3. **Complete experience** - Master the original platform thoroughly
4. **Transferable skills** - Original techniques apply everywhere

Modern platform variants (MEGA65, Spectrum Next) are **optional extensions** after curriculum completion.

## Curriculum Integration Strategy

### Phase 0-16: Original Hardware (Core Curriculum)

**Focus:** Complete mastery of original platform

- All 17 phases completable on 1980s hardware
- Period-accurate development techniques
- Full optimization within original constraints
- Certificate-earning curriculum

**Hardware Requirements:**
- Original hardware OR emulator
- No modern variants required
- Complete authentic experience

### Phase 17+: Modern Platform Extensions (Optional)

**Focus:** Optional advanced content for modern hardware owners

**Key message:** "You've mastered the original. Here's what modern hardware adds."

**Status:** Extension phases, not core curriculum

## Platform-Specific Variants

### Commodore 64 Family

#### Original Platform (Phases 0-10)
- **Commodore 64** (1982)
- 64K RAM, VIC-II, SID chip
- 6510 CPU @ 1MHz
- All curriculum uses original specifications

#### Modern Variants

**Category 1: Enhanced Reimaginations (Phase 17+ Focus)**

These platforms add new programmable capabilities beyond the original C64:

**MEGA65** (Primary Phase 17+ platform)
- Status: Production hardware (2022+)
- Type: Enhanced reimagination with new capabilities
- Enhancements:
  - 45GS02 CPU (45MHz, enhanced 6502 with new instructions)
  - VIC-IV (128 hardware sprites, layers, tilemap modes)
  - 384KB base RAM (expandable to 8MB)
  - DMA engine, copper co-processor
  - Enhanced audio capabilities
- Curriculum entry: Phase 17
- Documentation: `commodore-64/hardware/mega65/`
- **Why Phase 17+:** New programmable features (VIC-IV, 45GS02 instructions, DMA, copper)

**Category 2: Accurate Recreations (Reference Only)**

These platforms replicate original C64 hardware with modern conveniences but no new programmable capabilities:

**Ultimate 64**
- Status: Production (2025)
- Type: Full FPGA recreation
- Features:
  - Xilinx Artix-7 FPGA, 128MB DDR2 RAM, 16MB flash
  - HDMI 1080p output, Wi-Fi, Ethernet, USB ports
  - Turbo mode up to 48MHz
  - ~99% compatibility with original software/hardware
- **Curriculum role:** Mentioned as development platform option
- **Not Phase 17+:** No new programmable capabilities (cycle-accurate C64)

**C64 Reloaded MK2**
- Status: Production (Individual Computers)
- Type: Hybrid (original chips + modern PCB)
- Features:
  - Uses original MOS chips (6510, VIC-II, SID, CIA)
  - Xilinx XC9500 CPLD for PLA logic
  - 512KB flash ROM (Kernal + JiffyDOS + user images)
  - SRAM instead of DRAM, efficient DC-DC power
- **Curriculum role:** Mentioned for builders using original chips
- **Not Phase 17+:** Uses original chipset (authentic C64 experience)

**TheC64 Mini/Maxi**
- Status: Consumer products
- Type: ARM-based emulation
- Features: Rubber-dome keyboard, HDMI output, pre-loaded games
- **Curriculum role:** Mentioned for completeness only
- **Not recommended:** Limited peripheral support, not development-focused

#### Phase 17: MEGA65 Extensions (Optional)

**Tier 1: MEGA65 Basics (L1-32)**
- Backwards compatibility mode
- C64 mode vs MEGA65 mode
- Basic enhancements (speed, RAM)
- **Retrospective:** "Remember sprite multiplexing in Phase 2?"

**Tier 2: VIC-IV Graphics (L33-64)**
- Hardware sprites (128 vs 8)
- Layer system
- Enhanced bitmap modes
- **Remake:** Phase 3 Space Invaders with VIC-IV

**Tier 3: 45GS02 CPU (L65-96)**
- New instructions (multiply, divide)
- DMA operations
- Enhanced addressing modes
- **Remake:** Phase 6 scrolling games with DMA

**Tier 4: Advanced Features (L97-128)**
- Copper programming
- Enhanced SID features
- Extra RAM banks
- **Capstone:** Original MEGA65 game

### Sinclair ZX Spectrum Family

#### Original Platform (Phases 0-10)
- **ZX Spectrum 48K** (1982)
- **ZX Spectrum 128K** (1986)
- Z80 CPU @ 3.5MHz
- ULA graphics, attribute system
- BEEP / AY sound chip

#### Modern Variants

**Category 1: Enhanced Reimaginations (Phase 17+ Focus)**

These platforms add new programmable capabilities beyond the original Spectrum:

**ZX Spectrum Next** (Primary Phase 17+ platform)
- Status: Production hardware (2020+)
- Type: Enhanced reimagination with new capabilities
- FPGA: Xilinx Spartan-6 (KS1) / Artix-7 (KS2)
- Enhancements:
  - Z80N CPU @ 28MHz (4x/8x/14x original with new instructions)
  - 128 hardware sprites (16×16, scalable, rotatable, 8-bit colour)
  - Tilemap engine (80×32 or 40×32 character display)
  - Layer system (ULA, Tilemap, Sprite with programmable priority)
  - Copper co-processor (synchronized display updates)
  - ZXN DMA (Z80 DMA-compatible transfers)
  - 3× AY-3-8912 audio chips + 4× 8-bit DACs
  - Up to 2MB RAM (1792KB free)
- Curriculum entry: Phase 17
- Documentation: `sinclair-zx-spectrum/hardware/spectrum-next/`
- **Why Phase 17+:** New programmable features (hardware sprites, tilemap, layers, copper, DMA)

**Category 2: Accurate Recreations (Reference Only)**

These platforms replicate original Spectrum hardware with extensions but focus on compatibility:

**ZX-Uno**
- Status: Open-source project (active)
- Type: FPGA recreation with optional enhancements
- FPGA: Xilinx Spartan-6 XC6SLX9
- Features:
  - Faithful 48K/128K/Pentagon timing compatibility
  - Optional ULAplus (extended colours, HiRes/HiColour modes)
  - Optional Turbosound (2× AY chips, 6 channels)
  - 512KB-2MB SRAM, 32Mbit flash
  - DivMMC + esxDOS support
  - Multiple alternative cores (Sam Coupe, Jupiter Ace, Apple II, BBC Micro, NES, etc.)
- **Curriculum role:** Mentioned as affordable FPGA development option
- **Limited Phase 17+:** ULAplus extensions could warrant brief coverage
- **Note:** Multi-core capability makes it a "universal retro platform"

**ZX Vega+**
- Status: Troubled release (consumer product)
- Type: Handheld with pre-loaded games
- **Curriculum role:** Mentioned for historical context only
- **Not recommended:** Not suitable for development

#### Phase 17: Spectrum Next Extensions (Optional)

**Tier 1: Next Basics (L1-32)**
- Backwards compatibility
- 48K/128K modes vs Next mode
- Enhanced BASIC commands
- **Retrospective:** "Remember software sprites in Phase 2?"

**Tier 2: Hardware Sprites (L33-64)**
- No more software sprites!
- 128 hardware sprites
- Attribute-free graphics
- **Remake:** Phase 3 games without colour clash

**Tier 3: Layer System (L65-96)**
- Tilemap layer
- ULA layer
- Sprite layer
- Copper programming
- **Remake:** Phase 6 scrolling with hardware layers

**Tier 4: Advanced Features (L97-128)**
- DMA operations
- Enhanced audio (no more BEEP!)
- 2MB RAM management
- **Capstone:** Original Spectrum Next game

## Documentation Organization

### Original Platform Documentation

**Location:** `{platform}/hardware/`
**Example:** `commodore-64/hardware/VIC-II-REFERENCE.md`

**Content:**
- Original 1980s specifications
- Period-accurate programming techniques
- Historical context

### Modern Platform Documentation

**Location:** `{platform}/hardware/{variant}/`
**Examples:**
- `commodore-64/hardware/mega65/VIC-IV-REFERENCE.md`
- `sinclair-zx-spectrum/hardware/spectrum-next/SPRITE-SYSTEM-REFERENCE.md`

**Content:**
- Enhancement descriptions
- Backwards compatibility notes
- New features and registers
- Migration guides from original

## Lesson Integration

### Phases 0-16: Original Hardware Only

```markdown
# Lesson 25: VIC-II Sprite System

**Platform:** Commodore 64 (original)
**Hardware Required:** C64 or emulator

[Teach 8 hardware sprites, multiplexing techniques]

No mention of MEGA65 - students master original 8-sprite system.
Complete curriculum on authentic hardware.
```

### Phase 17+ (Optional): Modern Platform Extensions

```markdown
# Phase 17, Lesson 25: VIC-IV Sprite System

**Platform:** MEGA65 (optional extension)
**Prerequisite:** Phase 0-16 complete (C64 mastery)

**Retrospective:** "Remember multiplexing 8 sprites in Phase 2?
Let's see how MEGA65's 128 hardware sprites eliminate that constraint."

[Teach VIC-IV hardware sprites]

**Comparison Section:**
- Original C64: 8 sprites, manual multiplexing (Phase 2)
- MEGA65: 128 sprites, hardware managed
- Remake: Phase 3 Space Invaders with 128 sprites
```

## Cross-Platform Considerations

### Why This Matters

**For C64 → MEGA65:**
- VIC-IV is enhanced VIC-II (similar registers, compatible)
- Students appreciate improvements having lived the constraints
- Natural progression: "This is what you wished you had"

**For Spectrum → Next:**
- Next solves colour clash with hardware sprites
- Layer system eliminates software sprite management
- Backwards compatibility preserves original techniques

### Teaching Approach

**Phase 0-16 mindset (Core Curriculum):**
> "Master the original platform completely. Work within authentic constraints, optimize cleverly, appreciate what was possible."

**Phase 17+ introduction (Optional Extensions):**
> "You've completed the core curriculum on authentic hardware. Now see how modern reimaginations solve the challenges you experienced, while respecting retro aesthetics."

**Extension mindset:**
> "Leverage modern capabilities to create games impossible on original hardware, while maintaining retro game feel and honouring the platform's heritage."

## Standard Pattern for All Platforms

When adding new platforms, **ALWAYS follow this structure:**

### 1. Core Curriculum (Phases 0-16)

✅ **Original hardware only**
✅ **8,256 lessons** (Phase 0-16)
✅ **Completable on emulators**
✅ **Certificate-earning track**

### 2. Extension Phases (Phase 17+) - If Modern Variant Exists

✅ **Optional content**
✅ **512+ lessons per extension phase**
✅ **Requires modern hardware**
✅ **Builds on core mastery**

### 3. Documentation Structure

```
platform-name/
├── phase-0/           # Gateway language (core)
├── phase-1/           # Assembly fundamentals (core)
├── ...
├── phase-16/          # Mastery projects (core)
├── phase-17/          # Modern variant extensions (optional)
└── hardware/
    ├── [original refs]     # Core curriculum
    └── [variant]/          # Extension references (if exists)
```

## Modern Variant Categories

Modern variants fall into two distinct categories with different curriculum implications:

### Category 1: Enhanced Reimaginations
**Curriculum Status:** Phase 17+ extension content

Platforms that add **new programmable capabilities** beyond original hardware:
- New CPU instructions
- Enhanced graphics hardware (more sprites, layers, tilemaps)
- Co-processors (copper, DMA)
- Expanded memory architecture
- New audio capabilities

**Examples:** MEGA65 (VIC-IV, 45GS02, DMA), Spectrum Next (128 sprites, layers, copper)

**Teaching approach:** "You mastered the original constraints. Now leverage modern enhancements."

### Category 2: Accurate Recreations
**Curriculum Status:** Mentioned for reference, minimal Phase 17+ content

Platforms that **replicate original hardware** with modern conveniences:
- Cycle-accurate FPGA recreations
- Original chips on modern PCBs
- Modern outputs (HDMI, VGA)
- Quality-of-life features (SD cards, USB, flash storage)
- No new programmable capabilities (or minimal extensions)

**Examples:** Ultimate 64, C64 Reloaded MK2, ZX-Uno (in compatibility mode)

**Teaching approach:** "Same programming model, better development experience."

---

## Platform Variant Reference

### Platforms with Enhanced Reimaginations (Phase 17+ Content)

| Platform | Enhanced Variant | Accurate Recreations | Extension Phase |
|----------|-----------------|---------------------|-----------------|
| **Commodore 64** | **MEGA65** (VIC-IV, 45GS02, DMA) | Ultimate 64, C64 Reloaded MK2, TheC64 | Phase 17+ |
| **ZX Spectrum** | **Spectrum Next** (128 sprites, layers, copper) | ZX-Uno, Pentagon clones | Phase 17+ |
| **Amiga** | Vampire V4 (Apollo accelerator) | MiSTer FPGA, minimig | Phase 17+ (planned) |
| **Atari ST** | (None identified) | MiSTer FPGA | Phase 17+ (if variant emerges) |

### Platforms Without Enhanced Variants (Phase 16 Complete)

| Platform | Accurate Recreations | Notes |
|----------|---------------------|-------|
| **NES** | Analogue Nt, MiSTer FPGA | Mapper chips provide extensions (covered in Phase 1-16) |
| **Atari 2600** | RetroN 77 (FPGA) | Original hardware sufficient for curriculum |
| **MSX** | (Various models) | MSX2/2+ provide historical progression |
| **Apple II** | (Various clones) | Original hardware focus |

## Implementation Checklist

When adding a **new platform with modern variant**:

- [ ] Create `platform-name/` directory
- [ ] Plan Phases 0-16 (core curriculum, original hardware)
- [ ] Document original hardware specifications
- [ ] Create `hardware/` subdirectory for original references
- [ ] Identify modern variant(s)
- [ ] Create `hardware/variant-name/` subdirectory
- [ ] Plan Phase 17+ (extension curriculum)
- [ ] Document modern variant specifications
- [ ] Note in README.md that Phase 17+ requires modern hardware
- [ ] Update PLATFORM-VARIANTS.md with new platform

When adding a **new platform without modern variant**:

- [ ] Create `platform-name/` directory
- [ ] Plan Phases 0-16 (complete curriculum)
- [ ] Document original hardware specifications
- [ ] Create `hardware/` subdirectory
- [ ] Note in README.md that curriculum completes at Phase 16
- [ ] Update PLATFORM-VARIANTS.md with new platform

## Decision Summary

**Approved Approach:**

✅ **Core curriculum (Phases 0-16):** Completable on original hardware or emulators
✅ **Extension phases (Phase 17+):** Optional modern platform content
✅ **Separate documentation:** `hardware/{variant}/` subdirectories for extensions
✅ **Retrospective teaching:** Show how enhancements solve experienced problems
✅ **No mixing:** Core curriculum = authentic 1980s experience
✅ **Complete standalone:** Phase 0-16 earns mastery certificate

## Benefits of This Approach

1. **Historical authenticity** - Complete curriculum on original hardware
2. **Accessibility** - Anyone with emulator can complete full course
3. **Clear completion point** - Phase 16 = mastery achieved
4. **Optional extensions** - Modern hardware for those who have it
5. **Transferable skills** - Original techniques apply universally
6. **Motivation preserved** - Extensions reward completion, don't gate it
7. **Backwards compatible** - Extensions teach both modes

## Curriculum Totals

**Per Platform:**
- Core curriculum: 8,256 lessons (Phases 0-16)
- Optional extensions: 512+ lessons (Phase 17+)
- Total available: 8,768+ lessons

**Certificate tracks:**
- **Platform Mastery:** Complete Phases 0-16 (original hardware)
- **Extended Mastery:** Complete Phases 0-17+ (with modern variants)

---

**Version:** 2.0
**Created:** 2025-10-23
**Updated:** 2025-10-23
**Status:** Approved architecture with comprehensive variant catalog

**Changelog:**
- v2.0: Added comprehensive modern variant catalog with two-category system
  - Category 1: Enhanced Reimaginations (Phase 17+ focus)
  - Category 2: Accurate Recreations (reference only)
  - Detailed specifications for MEGA65, Ultimate 64, C64 Reloaded MK2, TheC64
  - Detailed specifications for Spectrum Next, ZX-Uno
  - Updated Platform Variant Reference table
- v1.0: Initial Phase 0-16 (original) / Phase 17+ (modern) architecture
