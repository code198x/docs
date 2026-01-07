# Future Expansion Tracks

**Status:** Planning document for post-curriculum content
**Scope:** All platforms

---

## Philosophy

The core curriculum for each platform focuses on **period-authentic skills** - what professional developers knew and used during each platform's commercial era. This ensures learners develop genuine understanding of the hardware and constraints that shaped classic games.

However, retro computing hasn't stood still. Modern hardware expansions, FPGA recreations, and enhanced successors offer new possibilities while building on the same foundations. These **expansion tracks** are optional modules for learners who've completed the core curriculum and want to explore further.

---

## Commodore 64 Expansion Tracks

### Expansion Hardware
- **REU (Ram Expansion Unit):** 1700/1750 programming, DMA transfers, extended memory
- **SuperCPU:** 20MHz mode, 16-bit registers, enhanced addressing
- **GeoRAM/NeoRAM:** Alternative RAM expansion approaches

### Modern Hardware
- **Ultimate 64/1541 Ultimate:** Integration, REU emulation, network features
- **SD2IEC:** Modern storage, directory handling, compatibility
- **Turbo Chameleon:** Cartridge-based expansion programming
- **BackBit:** Modern cartridge development

### MEGA65
- **BASIC 65:** Enhanced BASIC with structures, long variables
- **Enhanced graphics:** VIC-IV, extended colour modes, sprites
- **DMA controller:** Hardware-accelerated operations
- **Enhanced SID:** Dual SID, extended capabilities
- **40MHz mode:** High-performance computing
- **Ethernet/SD:** Modern I/O integration

### Modern Tooling
- **Cross-development:** VS Code, modern assemblers, CI/CD pipelines
- **Debugging:** VICE monitor, memory inspection, breakpoints
- **Asset pipelines:** Automated graphics/music conversion
- **Emulator testing:** Automated test suites

---

## Sinclair ZX Spectrum Expansion Tracks

### Expansion Hardware
- **Interface 1/Microdrive:** Network and storage expansion
- **AY sound chip:** 128K sound programming
- **DivMMC/DivIDE:** Mass storage integration
- **Multiface:** Memory access, snapshot development

### Modern Hardware
- **ZX Spectrum Next:** Enhanced Spectrum with Z80N, copper, DMA
- **Sprites:** Hardware sprites (Next-specific)
- **Enhanced graphics:** 256-colour modes, layer system
- **SD card integration:** Modern storage workflows

### Modern Tooling
- **Cross-assemblers:** z88dk, sjasmplus workflows
- **Fuse/ZEsarUX:** Emulator debugging features
- **TAP/TZX creation:** Distribution format tooling

---

## Commodore Amiga Expansion Tracks

### Expansion Hardware
- **Accelerators:** 68020/030/040/060 programming
- **RTG graphics:** Picasso, CyberGraphX
- **Fast RAM:** Extended memory usage
- **PCMCIA:** Storage and expansion

### Modern Hardware
- **Vampire accelerators:** FPGA-based Apollo core, 68080
- **PiStorm:** Raspberry Pi accelerator integration
- **Wicher/TF cards:** Modern accelerator cards
- **SD/CF storage:** Modern mass storage

### MorphOS/AmigaOS 4
- **Modern AmigaOS:** Programming for current AmigaOS variants
- **PowerPC considerations:** Architecture differences
- **Compatibility layers:** Writing for multiple targets

### Modern Tooling
- **Cross-compilers:** GCC, VBCC toolchains
- **WHDLoad:** Game packaging and installation
- **FS-UAE:** Emulator debugging and testing

---

## Nintendo Entertainment System Expansion Tracks

### Mapper Deep Dives
- **Advanced mappers:** MMC5, VRC6/7, FME-7
- **Audio expansion:** VRC6, Namco 163, Sunsoft 5B sound
- **Enhanced graphics:** MMC5 extended attributes, split scrolling

### Modern Hardware
- **Flash cartridges:** EverDrive, PowerPak development
- **FPGAs:** MiSTer, Analogue Nt considerations
- **Modern reproduction:** Creating physical cartridges

### Modern Tooling
- **cc65 advanced:** C development for NES
- **NESmaker:** High-level development tools
- **Mesen debugging:** Advanced debugging features

---

## Cross-Platform Modules

### Preservation Skills
- **Format archiving:** Platform-specific disk/tape formats
- **Emulator accuracy:** Testing and verification
- **Documentation:** Technical writing for preservation

### Community Integration
- **Demoscene:** Competition participation, size coding
- **Homebrew releases:** Modern distribution channels
- **Open source:** Contributing to emulators and tools

### Professional Skills
- **Retro game industry:** Working with publishers like Bitmap Soft, Psytronik
- **Kickstarter/crowdfunding:** Funding retro projects
- **Physical production:** Cartridge/disk manufacturing

---

## Structure

Each expansion track would be structured as:
- **Prerequisites:** Which core curriculum games must be completed
- **Units:** 16-64 units depending on scope
- **Projects:** Practical applications of new skills
- **Integration:** How skills combine with core knowledge

Expansion tracks are **not required** for curriculum completion. They exist for learners who want to:
1. Work with specific hardware they own
2. Target modern retro platforms (MEGA65, Next, etc.)
3. Contribute to the modern retro development community
4. Pursue professional retro game development

---

## Priority

Initial expansion track development (post core curriculum completion):

1. **MEGA65 (C64)** - Active platform with growing community
2. **ZX Spectrum Next** - Popular modern Spectrum
3. **Advanced NES mappers** - High demand for audio expansion knowledge
4. **Amiga WHDLoad** - Practical distribution skill

Lower priority:
- Older expansion hardware (REU, SuperCPU) - smaller audience
- Preservation skills - specialist interest
- Cross-platform tooling - varies by learner setup

---

## Notes

- Expansion tracks should **build on** core curriculum, not replace it
- Period-authentic skills remain the foundation
- Modern hardware understanding comes from deep original hardware knowledge
- "Learn the C64 properly, then the MEGA65 makes sense"
