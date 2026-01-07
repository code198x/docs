# Future Expansion Tracks

**Status:** Planning document for post-curriculum content
**Scope:** All platforms

---

## Philosophy

The core curriculum for each platform focuses on **period-authentic skills** - what professional developers knew and used during each platform's commercial era. This ensures learners develop genuine understanding of the hardware and constraints that shaped classic games.

However, retro computing hasn't stood still. Modern hardware expansions, FPGA recreations, and enhanced successors offer new possibilities while building on the same foundations.

Expansion content falls into two categories:

1. **Enhancement Tracks** - Enhanced versions of existing games for hardware family upgrades (MEGA65, Next, AGA)
2. **Post-Capstone Games** - New games for expansion peripherals and advanced mappers (REU, VRC6, WHDLoad)

---

## Enhancement Tracks

Enhancement tracks follow the Amiga AGA model: separate versions of later games that showcase enhanced hardware while the main curriculum remains compatible with base hardware.

### Commodore 64 → MEGA65

Enhanced versions for games that benefit from VIC-IV, 40MHz, DMA, and dual SID.

| Game | Units | Enhancement Focus |
|------|-------|-------------------|
| Games 9-14 | 32 each | VIC-IV modes, DMA operations |
| Game 15 | 64 | Full MEGA65 showcase |
| Game 16 | 128 | Definitive MEGA65 version |
| **Total** | **384** | |

**MEGA65 Capabilities:**
- VIC-IV: 256 colours, hardware sprites, bitplanes
- 40MHz mode with 6502 compatibility
- DMA controller for fast memory operations
- Dual SID chips
- Ethernet, SD card integration

### Sinclair ZX Spectrum → Next

Enhanced versions for games that benefit from Z80N, hardware sprites, copper, and enhanced graphics.

| Game | Units | Enhancement Focus |
|------|-------|-------------------|
| Games 9-14 | 32 each | Hardware sprites, copper effects |
| Game 15 | 64 | Full Next showcase |
| Game 16 | 128 | Definitive Next version |
| **Total** | **384** | |

**Next Capabilities:**
- Z80N: New instructions for faster code
- Hardware sprites (64 sprites, 16 colours each)
- Copper: Raster-synchronised effects
- 256-colour modes, layer system
- DMA for fast memory operations

### Sinclair ZX Spectrum → 128K

Optional 128K-enhanced versions of select games (period-authentic, 1985+).

| Game | Enhancement Focus |
|------|-------------------|
| Select games | AY soundtrack, extra content via banked RAM |

128K enhancements are smaller scope than Next - primarily adding AY music and using banked RAM for additional content. Not every game warrants a 128K version.

### Commodore Amiga → AGA

**Already implemented.** See `/docs/curriculum/commodore-amiga-curriculum.md`.

| Game | Units | Enhancement Focus |
|------|-------|-------------------|
| Games 9-14 | 32 each | 256 colours, enhanced effects |
| Game 15 | 64 | HAM8 cutscenes |
| Game 16 | 128 | Full AGA showcase |
| **Total** | **384** | |

---

## Post-Capstone Games

New games after the main curriculum targeting expansion peripherals, advanced mappers, or professional skills. These build on complete mastery of the core platform.

### Commodore 64

**Game 17: REU Adventure** (64 units)
Programming the 1750 REU (Ram Expansion Unit).
- DMA transfers
- Extended memory management
- REU-optimised game techniques
- Bank switching patterns

### Sinclair ZX Spectrum

No post-capstone currently planned - the 128K and Next enhancement tracks provide sufficient expansion content.

### Nintendo Entertainment System

**Game 17: VRC6 Symphony** (64 units)
Audio expansion using Konami's VRC6 mapper.
- Two additional pulse channels
- One sawtooth channel
- Enhanced music composition
- Mapper programming

**Game 18: MMC5 Mastery** (64 units)
Advanced techniques using Nintendo's MMC5 mapper.
- Extended nametables
- 8×8 attribute mode
- Extra sound channel
- Split-screen effects

### Commodore Amiga

**Game 17: WHDLoad Mastery** (64 units)
Professional game packaging for hard disk installation.
- WHDLoad slave creation
- Memory detection and adaptation
- Quit key handling
- Compatibility techniques

---

## Cross-Platform Modules (Future)

Potential modules applicable across platforms:

### Preservation Skills
- Format archiving (platform-specific disk/tape formats)
- Emulator accuracy testing
- Technical documentation

### Community Integration
- Demoscene participation
- Homebrew distribution channels
- Open source contribution (emulators, tools)

### Professional Skills
- Working with retro publishers (Bitmap Soft, Psytronik)
- Crowdfunding retro projects
- Physical production (cartridges, disks)

---

## Unit Summary

| Platform | Core | Enhancement | Post-Capstone | Total Available |
|----------|------|-------------|---------------|-----------------|
| C64 | 1,536 | 384 (MEGA65) | 64 (REU) | 1,984 |
| Spectrum | 1,536 | 384 (Next) + TBD (128K) | - | 1,920+ |
| NES | 1,536 | - | 128 (VRC6, MMC5) | 1,664 |
| Amiga | 2,048 | 384 (AGA) | 64 (WHDLoad) | 2,496 |

---

## Implementation Priority

**Phase 1 (with core curriculum):**
- Amiga AGA (complete)

**Phase 2 (post core curriculum):**
1. MEGA65 enhancement track - active platform, growing community
2. ZX Spectrum Next enhancement track - popular modern Spectrum
3. NES audio expansion games - high demand for VRC6/MMC5 knowledge

**Phase 3 (based on demand):**
- 128K Spectrum enhancements
- REU programming
- WHDLoad mastery
- Cross-platform modules

---

## Potential Future Platforms

Platforms under consideration for future curriculum development.

### 8-Bit Home Computers

| Platform | Language | BASIC Gateway | Enhancement Track | Notes |
|----------|----------|---------------|-------------------|-------|
| Amstrad CPC | Z80 | Locomotive BASIC | CPC Plus | Strong UK following, unique gate array |
| Atari 8-bit | 6502 | Atari BASIC | - | ANTIC/GTIA graphics, POKEY sound |
| BBC Micro | 6502 | BBC BASIC | Master | Educational heritage, excellent BASIC |
| MSX | Z80 | MSX BASIC | MSX2/MSX2+ | Japanese market, standardised hardware |
| Apple II | 6502 | Applesoft BASIC | IIgs | American classic, simple architecture |

### 16-Bit Home Computers

| Platform | Language | BASIC Gateway | Enhancement Track | Notes |
|----------|----------|---------------|-------------------|-------|
| Atari ST | 68000 | GFA BASIC | STE | MIDI standard, clean architecture |
| Acorn Archimedes | ARM | BBC BASIC V | RISC OS | First ARM platform, powerful BASIC |

### Game Consoles

| Platform | Language | Enhancement Track | Notes |
|----------|----------|-------------------|-------|
| Sega Master System | Z80 | Game Gear | Simple VDP, good entry point |
| Sega Mega Drive | 68000 | Mega CD, 32X | Blast processing, dual CPUs |
| SNES | 65816 | - | Mode 7, complex but powerful |
| TurboGrafx-16 | 6502 | CD-ROM² | HuC6280, large sprite counts |
| Game Boy | Z80 (SM83) | GBC, GBA | Handheld constraints |
| Atari 2600 | 6502 | - | Racing the beam, extreme constraints |

### Selection Criteria

When evaluating platforms for inclusion:

1. **Historical significance** - Was it commercially important or influential?
2. **Active community** - Are people still developing for it?
3. **Educational value** - Does it teach unique concepts?
4. **Tooling availability** - Are assemblers/emulators mature?
5. **Differentiation** - Does it offer something our current platforms don't?

### Platform Priorities

**High interest:**
- Sega Mega Drive (68000 skills transfer from Amiga)
- Atari ST (68000, different chipset philosophy from Amiga)
- BBC Micro (educational heritage, exceptional BASIC)

**Medium interest:**
- SNES (complex but iconic)
- Amstrad CPC (Z80 skills transfer, strong UK community)
- Game Boy (handheld constraints, huge nostalgia)

**Lower priority:**
- Atari 2600 (extremely niche, racing-the-beam is specialist)
- MSX (smaller Western audience)
- Apple II (simpler than C64, less hardware to teach)

### Enhancement Track Applicability

| Pattern | Platforms |
|---------|-----------|
| Period hardware upgrade | CPC → Plus, ST → STE, MSX → MSX2, BBC → Master |
| Modern FPGA successor | (None identified yet for non-current platforms) |
| Console variants | SMS → Game Gear, GB → GBC → GBA, MD → CD/32X |
| No clear enhancement | Atari 2600, Apple II, SNES |

---

## Design Principles

1. **Enhancement tracks build on core games** - Same game, enhanced for better hardware
2. **Post-capstone games are standalone** - New games requiring core curriculum completion
3. **Period-authentic first** - Modern hardware understanding comes from deep original knowledge
4. **Powers of 2** - All unit counts remain powers of 2 (32, 64, 128)
5. **Optional, not required** - Expansion content never gates core curriculum completion

"Learn the C64 properly, then the MEGA65 makes sense."

---

## Version History

- **2.0 (2026-01-07):** Restructured into Enhancement Tracks and Post-Capstone Games. Added concrete unit counts and implementation priorities.
- **1.0 (2025-01-07):** Initial planning document.
