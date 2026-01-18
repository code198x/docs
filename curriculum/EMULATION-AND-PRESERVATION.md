# Emulation & Preservation: Keeping History Alive

**Purpose:** Document the emulation and preservation movement - how it works, why it matters, and key projects and people. Essential context for anyone wanting to build emulators.

**Last Updated:** 2026-01-18

---

## Why Emulation Matters

Emulation is:
1. **Preservation** - Keeping games playable
2. **Education** - Understanding how machines worked
3. **Accessibility** - Play without original hardware
4. **Development** - Testing without real hardware
5. **Research** - Study historical software

**For this curriculum:** Emulation is how students run their code without vintage hardware.

---

## Part 1: What Is Emulation?

### Definition

**Emulation:** Software that mimics hardware behaviour, allowing software written for one system to run on another.

| Term | Meaning |
|------|---------|
| **Emulator** | The software doing the mimicking |
| **Host** | The system running the emulator |
| **Guest/Target** | The system being emulated |
| **ROM** | Software image being run |

### Emulation vs Simulation

| Aspect | Emulation | Simulation |
|--------|-----------|------------|
| **Goal** | Run original software | Model behaviour |
| **Accuracy** | Cycle-accurate possible | Approximate |
| **Use** | Play games | Education, testing |

### Emulation Accuracy Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| **Functional** | Basic compatibility | Most games work |
| **Cycle-accurate** | Exact timing | All software works |
| **Transistor-level** | Hardware simulation | Research, perfectionism |

---

## Part 2: How Emulators Work

### Core Components

```
+------------------+
|    CPU Core      |  ← Executes instructions
+------------------+
|    Memory        |  ← RAM, ROM mapping
+------------------+
|    Video         |  ← Graphics rendering
+------------------+
|    Audio         |  ← Sound synthesis
+------------------+
|    Input         |  ← Controllers, keyboard
+------------------+
|    Timing        |  ← Synchronisation
+------------------+
```

### CPU Emulation Approaches

| Approach | Description | Speed | Accuracy |
|----------|-------------|-------|----------|
| **Interpreter** | Execute instruction by instruction | Slow | High |
| **Cached interpreter** | Decode once, cache | Medium | High |
| **Dynamic recompilation** | Translate to host code | Fast | Variable |
| **Static recompilation** | Pre-translate entire ROM | Fastest | Variable |

### The CPU Instruction Loop

```pseudocode
while running:
    fetch instruction at PC
    decode instruction
    execute instruction
    update PC
    update cycle count
    check interrupts
    sync timing
```

### Memory Mapping

Emulators must handle:
- RAM regions
- ROM regions
- Memory-mapped I/O
- Bank switching
- Special addresses

### Video Emulation

| Approach | Description |
|----------|-------------|
| **Scanline** | Render line by line |
| **Per-pixel** | Cycle-accurate rendering |
| **Frame-based** | Render entire frame |

Cycle-accurate video emulation catches mid-frame changes.

### Audio Emulation

| Approach | Description |
|----------|-------------|
| **Register-level** | Track chip state |
| **Sample-based** | Generate audio samples |
| **Hybrid** | Mix approaches |

### Timing Synchronisation

| Challenge | Solution |
|-----------|----------|
| **Too fast** | Sleep, frame limiting |
| **Too slow** | Frame skip |
| **Drift** | Resync periodically |

**Vault entries:**
- `emulation-fundamentals` - Technique entry
- `cpu-emulation` - Technique entry
- `cycle-accuracy` - Technique entry

---

## Part 3: Platform-Specific Challenges

### C64 Emulation Challenges

| Component | Challenge |
|-----------|-----------|
| **VIC-II** | Flexible timing, sprites, badlines |
| **SID** | Analog filters, combined waveforms |
| **CIA** | Timer quirks |
| **Datasette** | Tape timing critical |

**Key emulators:** VICE (excellent), CCS64, Frodo

### Spectrum Emulation Challenges

| Component | Challenge |
|-----------|-----------|
| **ULA** | Contended memory timing |
| **Floating bus** | Some games depend on it |
| **Beeper** | 1-bit audio tricks |
| **Tape** | Loading schemes vary |

**Key emulators:** Fuse, SpecEmu, ZX Spin

### NES Emulation Challenges

| Component | Challenge |
|-----------|-----------|
| **PPU** | Sprite 0 hit, scrolling |
| **Mappers** | Hundreds of cartridge types |
| **APU** | DMC channel quirks |
| **Timing** | CPU/PPU sync critical |

**Key emulators:** Mesen (excellent), FCEUX, Nestopia

### Amiga Emulation Challenges

| Component | Challenge |
|-----------|-----------|
| **Custom chips** | Blitter, Copper, Paula, Denise |
| **Timing** | DMA slots complex |
| **OS** | Kickstart ROM needed |
| **Disk** | MFM, copy protection |

**Key emulators:** WinUAE (definitive), FS-UAE, Amiberry

### General Challenges

| Challenge | Notes |
|-----------|-------|
| **Undocumented behaviour** | Games use bugs as features |
| **Analog components** | Filters, CRT effects |
| **Copy protection** | May need special handling |
| **Peripherals** | Disk drives, printers, etc. |

---

## Part 4: Key Emulators

### By Platform

#### Commodore 64

| Emulator | Platform | Notes |
|----------|----------|-------|
| **VICE** | Multi | Definitive, cycle-accurate |
| **CCS64** | Windows | Long history |
| **Frodo** | Multi | Lighter weight |

#### ZX Spectrum

| Emulator | Platform | Notes |
|----------|----------|-------|
| **Fuse** | Multi | Excellent accuracy |
| **SpecEmu** | Windows | Accurate |
| **ZX Spin** | Windows | User-friendly |

#### NES

| Emulator | Platform | Notes |
|----------|----------|-------|
| **Mesen** | Multi | Highly accurate |
| **FCEUX** | Multi | Debugging features |
| **Nestopia** | Multi | Good accuracy |

#### Amiga

| Emulator | Platform | Notes |
|----------|----------|-------|
| **WinUAE** | Windows | The gold standard |
| **FS-UAE** | Multi | Cross-platform |
| **Amiberry** | RPi/ARM | Optimised |

#### Multi-System

| Emulator | Systems | Notes |
|----------|---------|-------|
| **MAME** | Arcade, computers | Comprehensive |
| **RetroArch** | Many (via cores) | Frontend + emulators |
| **Mednafen** | Many | Accurate |
| **BizHawk** | Many | TASing focus |
| **OpenEmu** | Many | macOS |
| **Higan/bsnes** | Nintendo | Accuracy-focused |

**Vault entries:**
- `vice-emulator` - Software entry
- `winuae` - Software entry
- `mame` - Software entry
- `retroarch` - Software entry
- `mesen` - Software entry

---

## Part 5: Key People

### Emulation Pioneers

| Person | Contribution |
|--------|--------------|
| **Nicola Salmoria** | MAME founder |
| **Toni Wilen** | WinUAE maintainer |
| **byuu (Near)** | higan/bsnes - accuracy pioneer |
| **Peter Wendrich** | VICE contributor |
| **Martin Korth** | NO$GBA, NO$SNS, comprehensive docs |

### byuu's Legacy

**byuu** (Near, 1983-2021) pioneered accuracy-focused emulation:
- Created bsnes/higan
- Documented undocumented hardware
- Pushed for cycle-accuracy
- Proved accurate emulation possible
- Tragically lost in 2021

His work influenced all subsequent accuracy-focused emulators.

**Vault entries:**
- `byuu-near` - People entry (significant)
- `nicola-salmoria` - People entry
- `toni-wilen` - People entry

---

## Part 6: Preservation

### Why Preservation Matters

| Threat | Risk |
|--------|------|
| **Media decay** | Magnetic media degrades |
| **Hardware failure** | Machines break |
| **Knowledge loss** | Techniques forgotten |
| **Legal issues** | Access restricted |
| **Server shutdown** | Online games disappear |

### Preservation Projects

| Project | Focus |
|---------|-------|
| **Internet Archive** | Software, manuals, magazines |
| **MAME** | Arcade preservation |
| **No-Intro** | Verified ROM sets |
| **TOSEC** | Comprehensive cataloguing |
| **Redump** | Optical media |
| **Hidden Palace** | Prototypes, unreleased |

### The Internet Archive

| Collection | Contents |
|------------|----------|
| **Software Library** | Playable in browser |
| **Console Living Room** | Console games |
| **Magazines** | Scanned publications |
| **Manuals** | Game documentation |

### Platform-Specific Preservation

| Project | Platform |
|---------|----------|
| **World of Spectrum** | Spectrum |
| **Lemon64** | C64 |
| **GameBase64** | C64 |
| **Amiga Hall of Light** | Amiga |
| **SMS Power** | Master System |
| **NESdev** | NES |
| **SegaRetro** | Sega platforms |

**Vault entries:**
- `internet-archive-gaming` - Culture entry
- `mame-preservation` - Culture entry
- `no-intro` - Culture entry
- `world-of-spectrum` - Culture entry

---

## Part 7: ROM Dumping

### Hardware Tools

| Tool | Purpose |
|------|---------|
| **Kryoflux** | Disk preservation, captures raw flux |
| **SuperCard Pro** | Similar to Kryoflux |
| **Retrode** | Cartridge dumper |
| **INLretro** | Cartridge dumper |
| **DataPath** | Tape preservation |

### Disk Imaging Challenges

| Format | Challenge |
|--------|-----------|
| **Standard formats** | Relatively easy |
| **Protected disks** | Need flux-level capture |
| **Weak sectors** | Special handling |
| **Timing-based** | Kryoflux essential |

### Tape Preservation

| Challenge | Solution |
|-----------|----------|
| **Degradation** | Digitise now |
| **Custom loaders** | Capture audio, analyse |
| **Timing critical** | High sample rate |

**Vault entries:**
- `kryoflux` - Hardware entry
- `rom-dumping` - Technique entry

---

## Part 8: Legal Considerations

### The Legal Landscape

| Aspect | Status |
|--------|--------|
| **Emulators** | Legal (Sony vs Connectix) |
| **ROMs you own** | Grey area |
| **ROM distribution** | Generally illegal |
| **Abandonware** | Legally dubious, often tolerated |
| **Preservation exceptions** | Vary by jurisdiction |

### Key Legal Cases

| Case | Outcome |
|------|---------|
| **Sony vs Connectix** | Emulation legal |
| **Sony vs Bleem** | Bleem won but bankrupted |
| **Nintendo vs Various** | ROM sites sued |

### The Ethical Framework

| Position | Argument |
|----------|----------|
| **Pro-preservation** | History must be saved |
| **Pro-copyright** | Creators have rights |
| **Practical** | Old games unavailable anyway |
| **Compromise** | Focus on truly abandoned |

---

## Part 9: Technical Documentation

### Essential Resources

| Resource | Content |
|----------|---------|
| **NESDev Wiki** | NES hardware deep dive |
| **SMS Power** | Master System docs |
| **Codebase64** | C64 programming |
| **World of Spectrum** | Spectrum docs |
| **Amiga Hardware Manual** | Official docs |
| **Various datasheets** | Chip specifications |

### Documentation Sources

| Type | Example |
|------|---------|
| **Official manuals** | Programmer's references |
| **Reverse engineering** | Community research |
| **Patent filings** | Hardware details |
| **Die shots** | Chip photography |

### The Visual6502 Project

| Aspect | Notes |
|--------|-------|
| **What** | Transistor-level 6502 simulation |
| **How** | Chip photography, analysis |
| **Why** | Ultimate documentation |
| **Impact** | Revealed undocumented behaviour |

**Vault entries:**
- `nesdev` - Culture entry
- `visual6502` - Culture entry

---

## Part 10: Building Emulators

### Getting Started

| Step | Approach |
|------|----------|
| 1 | Choose a simple system (CHIP-8, Game Boy) |
| 2 | Read documentation thoroughly |
| 3 | Implement CPU first |
| 4 | Add simple graphics |
| 5 | Test with known-good ROMs |
| 6 | Iterate and improve |

### Recommended First Projects

| System | Why |
|--------|-----|
| **CHIP-8** | Very simple, good first emulator |
| **Game Boy** | Well documented, simple enough |
| **NES** | Good docs, manageable complexity |
| **Space Invaders** | Single game, simple |

### Resources for Emulator Development

| Resource | Content |
|----------|---------|
| **Emulator101** | Game Boy tutorial |
| **NESDev** | NES development |
| **Copetti.org** | Console architecture |
| **Various blogs** | Developer write-ups |

### Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| **Starting too big** | Begin with CHIP-8 |
| **Ignoring timing** | Timing matters early |
| **Poor testing** | Use test ROMs |
| **Guessing** | Read documentation |

---

## Part 11: The Future

### Current Trends

| Trend | Status |
|-------|--------|
| **FPGA** | Hardware-level accuracy |
| **Browser emulation** | JavaScript emulators |
| **Cloud gaming** | Streaming emulation |
| **Machine learning** | Upscaling, completion |

### FPGA Emulation

| Project | Platform |
|---------|----------|
| **MiSTer** | Multi-system FPGA |
| **Analogue** | Commercial FPGA consoles |

FPGA recreates hardware in hardware - ultimate accuracy.

### Preservation Challenges Ahead

| Challenge | Risk |
|-----------|------|
| **Online-only games** | Servers shut down |
| **DRM/always-online** | Can't preserve |
| **Complexity** | Modern systems harder |
| **Legal barriers** | Increasingly strict |

---

## Part 12: Curriculum Connection

### Why This Matters For Us

| Need | Solution |
|------|----------|
| **Run student code** | Emulators |
| **Verify screenshots** | Automated emulation |
| **Cross-platform** | Students use any host |
| **Accuracy** | Cycle-accurate where needed |

### Our Emulator Stack

| Platform | Emulator |
|----------|----------|
| **C64** | VICE |
| **Spectrum** | Fuse |
| **NES** | Mesen or FCEUX |
| **Amiga** | FS-UAE |

### The Long-Term Goal

Building your own emulators would:
- Prove deep hardware understanding
- Allow customisation for education
- Ensure curriculum independence
- Be ultimate capstone project

---

## Summary: New Vault Entries

| Category | Entries |
|----------|---------|
| **Software** | VICE, WinUAE, MAME, RetroArch, Mesen | 12 |
| **People** | byuu, Salmoria, Wilen, Korth | 6 |
| **Culture** | Preservation projects, documentation | 10 |
| **Hardware** | Kryoflux, MiSTer, FPGA | 5 |
| **Techniques** | Emulation methods, ROM dumping | 8 |

**Total new entries: ~41**

---

## Running Vault Total

| Previous | This Document | New Total |
|----------|---------------|-----------|
| ~1338 | +41 | **~1379 entries** |
