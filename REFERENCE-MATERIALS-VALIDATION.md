# Reference Materials Validation

**Created:** 2025-10-24
**Purpose:** Document findings from authoritative sources that validate and enhance the quick reference documentation

---

## Sources Consulted

### NES (Nintendo Entertainment System)
- **NESDev Wiki** - Community-maintained authoritative technical reference
  - PPU Registers: https://www.nesdev.org/wiki/PPU_registers
  - CPU Memory Map: https://www.nesdev.org/wiki/CPU_memory_map
  - Controller Reading: https://www.nesdev.org/wiki/Controller_reading
- **Archive.org**
  - NES Programmers Reference Guide (Electronic Arts, 1989)
  - NES Programmers Reference Guide (Arti Haroutunian, Sculptured Software)

### ZX Spectrum
- **Wikipedia** - ZX Spectrum graphic modes technical article
- **Community Documentation**
  - Break Into Program - Screen Memory Layout
  - World of Spectrum - ZX Spectrum Manual Chapter 24
- **Archive.org**
  - ZX Spectrum BASIC Programming Manual (available)

### Amiga
- **Wikipedia** - Amiga Original Chip Set comprehensive article
- **Archive.org**
  - AMOS Professional Manual: https://archive.org/details/AmosProfessionalManual
  - Amiga Hardware Reference Manual (3rd Edition): https://archive.org/details/amiga-hardware-reference-manual-3rd-edition
  - Amiga Hardware Reference Manual (2nd Edition): https://archive.org/details/commodore-amiga-hardware-reference-manual-2nd

### Commodore 64 (Reference)
- **Archive.org**
  - Commodore 64 Programmer's Reference Guide: https://archive.org/details/c64-programmer-ref
  - Multiple editions available in PDF, EPUB formats

---

## Key Findings and Validations

### NES - PPU Registers

**Our quick reference correctly documents:**
- ✅ All 8 PPU registers ($2000-$2007) with correct addresses
- ✅ OAMDMA at $4014 for sprite DMA
- ✅ Register bit layouts and functions
- ✅ Read buffer mechanism for PPUDATA ($2007)
- ✅ Two-write protocol for PPUSCROLL and PPUADDR

**Critical findings to emphasize:**
1. **NMI timing race condition**: "Enabling NMI while the vblank flag is 1 will immediately trigger an NMI"
2. **PPUDATA read buffer**: Data is delayed by one read (except palette RAM)
3. **OAMADDR corruption**: Hardware bug on 2C02G - use OAMDMA instead
4. **Sprite 0 hit unreliability**: Cannot trigger at X=255 or with rendering disabled
5. **Register write order**: Must read PPUSTATUS before PPUSCROLL/PPUADDR writes
6. **Rendering conflicts**: Never access PPUDATA during rendering (causes glitches)

**Timing specifications validated:**
- OAMDMA: 513-514 cycles
- PPU ignored writes: ~29,658 NTSC cycles after power-on
- Sprite tile loading: Ticks 257-320 (OAMADDR reset to 0)

### NES - Controller Reading

**Our quick reference correctly documents:**
- ✅ Strobe protocol (write $01 then $00 to $4016)
- ✅ Button reading sequence (8 reads)
- ✅ Two-player support ($4016 and $4017)
- ✅ Button order: A, B, Select, Start, Up, Down, Left, Right

**Critical hardware quirk discovered:**
- **DPCM audio conflict**: DMC DMA can corrupt controller reads on NTSC (not PAL)
- **Mitigation**: Read multiple times and compare, or use OAM DMA sync
- **Data line polarity**: Inverted (high line = 0, low = 1)

### NES - Memory Map

**Our quick reference correctly documents:**
- ✅ 2KB internal RAM at $0000-$07FF
- ✅ Mirroring through $1FFF
- ✅ PPU registers $2000-$2007 (mirrored through $3FFF)
- ✅ APU/I/O registers $4000-$4017
- ✅ Cartridge space $4020-$FFFF
- ✅ Typical PRG-RAM at $6000-$7FFF

**Additional detail validated:**
- Zero page: $0000-$00FF (fastest access)
- Stack: $0100-$01FF (grows downward from $01FF)
- OAM buffer convention: $0200-$02FF
- Interrupt vectors: $FFFA-$FFFF (must be in all banks)

### ZX Spectrum - Screen Layout

**Our quick reference correctly documents:**
- ✅ Screen bitmap: $4000-$57FF (6144 bytes)
- ✅ Attributes: $5800-$5AFF (768 bytes)
- ✅ Resolution: 256×192 pixels
- ✅ Attribute grid: 32×24 cells (8×8 pixels each)
- ✅ Non-linear memory organization (thirds)

**Critical findings validated:**
- **Thirds organization**: Screen divided into three 2KB banks
- **Within each third**: 8 character rows with scanlines interleaved
- **Rationale**: Designed for hardware rendering speed, not programmer convenience
- **Memory shared with CPU**: VRAM access optimized to minimize CPU stalls

**Color clash validated:**
- Each 8×8 cell: 1 INK + 1 PAPER color only
- 8 base colors (0-7) with BRIGHT modifier = 15 usable colors
- FLASH bit enables INK/PAPER swap every 16 frames

### ZX Spectrum - Attribute System

**Attribute byte format validated:**
```
Bit 7: FLASH
Bit 6: BRIGHT
Bits 5-3: PAPER color (0-7)
Bits 2-0: INK color (0-7)
```

**Hardware timing validated:**
- 50Hz PAL refresh (50 frames per second)
- FRAMES counter at address 23672 (3-byte low-endian)
- Increments 50 times per second

### Amiga - OCS Chipset

**Our quick reference correctly documents:**
- ✅ Three custom chips: Paula (audio/I/O), Agnus (DMA), Denise (display)
- ✅ 8 hardware sprites
- ✅ 4 audio channels (8-bit PCM)
- ✅ Blitter for fast memory operations
- ✅ Copper co-processor

**Display modes validated:**
- Low res: 320 pixels wide (140ns pixels)
- High res: 640 pixels wide (70ns pixels)
- PAL: 256 lines / NTSC: 200 lines
- Interlaced: doubles vertical resolution (with flicker)
- Overscan: up to 368 or 736 pixels wide (monitor dependent)

**Color system validated:**
- 1-5 bitplanes = 2-32 colors from 4096 total
- 12-bit RGB: 4 bits per component ($0RGB format)
- EHB mode (6th bitplane): 64 colors (32 + 32 half-bright)
- HAM mode: All 4096 colors via hold-and-modify

**Hardware sprites validated:**
- 8 sprites per scanline
- 16 pixels wide (fixed)
- 3 visible colors + transparent
- Sprite attachment: pairs can combine for 15 colors
- Copper can reposition sprites mid-frame (reuse)

**Blitter validated:**
- 0-3 source operands (A, B, C) + destination (D)
- Programmable Boolean operations
- Width: multiples of 16 bits
- Height: up to 1,024 lines
- Line mode: Bresenham's algorithm
- BLITHOG flag: can lock out CPU even cycles

**Copper validated:**
- Three instruction types: MOVE, WAIT, SKIP
- MOVE: writes to chipset registers
- WAIT: halts until specific beam position
- SKIP: conditional execution
- Synchronized to display beam position
- Used for mid-frame register changes (raster effects)

**Paula audio validated:**
- 4 DMA-driven channels
- 8-bit PCM samples
- 6-bit volume control (64 levels)
- Stereo output (channels 0+3 left, 1+2 right)
- Max sample rate: ~28,867 Hz (PAL) / ~29,000 Hz (NTSC)
- 12 dB/octave low-pass filter at 3.3 kHz (global)

**Memory architecture validated:**
- Chip RAM: DMA accessible (graphics, audio)
- Fast RAM: CPU only (no DMA contention)
- Original Agnus: 512KB addressing
- Fat Agnus: 512KB pseudo-fast RAM
- ECS Agnus: 1-2MB Chip RAM

**DMA priority validated:**
- Agnus controls all Chip RAM access
- Priority system: bitplanes > blitter > CPU
- CPU typically gets every other cycle
- BLITHOG can lock out CPU even cycles
- Shared bandwidth creates performance tradeoffs

---

## Corrections and Enhancements Needed

### NES Quick References

**PPU-PROGRAMMING-QUICK-REFERENCE.md:**
- ✅ Already includes critical timing warnings
- ✅ Already documents read buffer mechanism
- ✅ Already emphasizes OAMDMA over OAMDATA
- Consider adding: DPCM audio conflict note to controller section

**CONTROLLER-INPUT-QUICK-REFERENCE.md:**
- Add warning about DPCM audio conflict corrupting reads
- Add note about data line polarity inversion
- Add mitigation strategies (multiple reads, OAM DMA sync)

**6502-QUICK-REFERENCE.md:**
- ✅ Already comprehensive
- No corrections needed based on findings

**NES-MEMORY-MAP.md:**
- ✅ Already accurate
- Consider adding: DPCM sample address range ($C000-$FFFF practical)

### ZX Spectrum Quick References

**ZX-SPECTRUM-MEMORY-AND-GRAPHICS-REFERENCE.md:**
- ✅ Already includes complete screen layout formula
- ✅ Already documents color clash extensively
- ✅ Already includes assembly code for address calculation
- Hardware rationale validated (speed optimization)

**ZX-SPECTRUM-BASIC-QUICK-REFERENCE.md:**
- ✅ Already comprehensive
- No corrections needed

### Amiga Quick References

**AMIGA-HARDWARE-QUICK-REFERENCE.md:**
- ✅ Already accurate on all major points
- Validated: Display modes, sprite specs, audio specs
- Validated: DMA architecture, memory types
- Consider adding: Overscan maximum pixels (368/736)
- Consider adding: Butterworth filter specification (12 dB/oct @ 3.3 kHz)

**AMOS-COMMANDS-QUICK-REFERENCE.md:**
- ✅ Already comprehensive
- Commands align with hardware capabilities
- No corrections needed

---

## Confidence Assessment

### NES Documentation
**Confidence: VERY HIGH (95%)**
- Cross-referenced with NESDev Wiki (authoritative community source)
- All major specifications validated
- Hardware quirks and timing documented
- Minor additions recommended (DPCM conflict)

### ZX Spectrum Documentation
**Confidence: HIGH (90%)**
- Screen layout formula validated against multiple sources
- Attribute system correctly documented
- Color clash explanation accurate
- Hardware rationale confirmed (speed optimization)

### Amiga Documentation
**Confidence: VERY HIGH (95%)**
- Wikipedia article comprehensive and technical
- All chipset specifications validated
- Display modes, sprites, audio all accurate
- DMA architecture correctly explained
- Minor technical details could be added (filter specs)

---

## Recommended Next Steps

1. **Minor enhancements** to controller documentation (DPCM conflict)
2. **No major revisions needed** - quick references are accurate
3. **Archive.org manuals available** for deeper dives during lesson creation
4. **NESDev Wiki** bookmark for detailed NES development questions
5. **Ready for lesson development** across all three platforms

---

**Conclusion:** The quick reference documentation is technically accurate and well-aligned with authoritative sources. Minor additions recommended but no critical corrections needed.
