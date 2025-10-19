# C64 Reference Guide - Start Here

**Purpose:** Navigation guide for all C64 reference documentation
**Updated:** 2025-10-18
**For:** Code Like It's 198x curriculum designers and lesson creators

---

## Quick Navigation

Looking for something specific? Use this guide to find the right reference document.

### 🎯 Most Common Tasks

| I need to... | Use this reference |
|--------------|-------------------|
| **Read joystick or keyboard** | [CIA-QUICK-REFERENCE.md](CIA-QUICK-REFERENCE.md) |
| **Move sprites or change colors** | [VIC-II-QUICK-REFERENCE.md](VIC-II-QUICK-REFERENCE.md) |
| **Look up an assembly instruction** | [6510-QUICK-REFERENCE.md](6510-QUICK-REFERENCE.md) |
| **Convert PETSCII to screen codes** | [PETSCII-AND-SCREEN-CODES.md](PETSCII-AND-SCREEN-CODES.md) |
| **Find where to put my ML program** | [C64-MEMORY-MAP.md](C64-MEMORY-MAP.md) |
| **Call ML from BASIC** | [BASIC-TO-ML-INTEGRATION.md](BASIC-TO-ML-INTEGRATION.md) |
| **Use a KERNAL routine** | [KERNAL-ROUTINES-REFERENCE.md](KERNAL-ROUTINES-REFERENCE.md) |

---

## Reference Documents by Topic

### Machine Language Programming

#### Quick References (Start Here)
- **[6510-QUICK-REFERENCE.md](6510-QUICK-REFERENCE.md)** - Instruction set, addressing modes, common patterns (12KB)
- **[CIA-QUICK-REFERENCE.md](CIA-QUICK-REFERENCE.md)** - Joystick, keyboard, timers (12KB)
- **[VIC-II-QUICK-REFERENCE.md](VIC-II-QUICK-REFERENCE.md)** - Sprites, colors, screen control (17KB)

#### Comprehensive References (Deep Dives)
- **[6510-MICROPROCESSOR-REFERENCE.md](6510-MICROPROCESSOR-REFERENCE.md)** - Complete CPU specifications (85KB)
- **[6526-CIA-REFERENCE.md](6526-CIA-REFERENCE.md)** - Complete I/O chip specs (107KB)
- **[VIC-II-REFERENCE.md](VIC-II-REFERENCE.md)** - Complete video chip specs (87KB)

#### Overview and Integration
- **[C64-MACHINE-LANGUAGE-OVERVIEW.md](C64-MACHINE-LANGUAGE-OVERVIEW.md)** - ML concepts for lesson design
- **[BASIC-TO-ML-INTEGRATION.md](BASIC-TO-ML-INTEGRATION.md)** - SYS, USR, IRQ, vectors
- **[C64-MEMORY-MAP.md](C64-MEMORY-MAP.md)** - Complete memory layout $0000-$FFFF
- **[KERNAL-ROUTINES-REFERENCE.md](KERNAL-ROUTINES-REFERENCE.md)** - All 39 KERNAL routines organized by function

### Graphics and Display

#### Focused References
- **[SPRITES-REFERENCE.md](SPRITES-REFERENCE.md)** - Complete sprite programming guide
- **[PETSCII-AND-SCREEN-CODES.md](PETSCII-AND-SCREEN-CODES.md)** - Character codes (consolidated)
- **[COLOR-COMBINATIONS-REFERENCE.md](COLOR-COMBINATIONS-REFERENCE.md)** - Readable color pairs
- **[VIC-II-GRAPHICS-MODES-REFERENCE.md](VIC-II-GRAPHICS-MODES-REFERENCE.md)** - Bitmap, multicolor, etc.

#### Specialized Topics
- **[PROGRAMMABLE-CHARACTERS-REFERENCE.md](PROGRAMMABLE-CHARACTERS-REFERENCE.md)** - Custom character sets
- **[MULTICOLOR-MODE-REFERENCE.md](MULTICOLOR-MODE-REFERENCE.md)** - Multicolor graphics
- **[BITMAP-GRAPHICS-REFERENCE.md](BITMAP-GRAPHICS-REFERENCE.md)** - High-res and multicolor bitmap
- **[SCREEN-COLOR-MEMORY-REFERENCE.md](SCREEN-COLOR-MEMORY-REFERENCE.md)** - Screen RAM and color RAM
- **[RASTER-INTERRUPTS-REFERENCE.md](RASTER-INTERRUPTS-REFERENCE.md)** - Raster effects and IRQs

### Sound
- **[SID-CHIP-REFERENCE.md](SID-CHIP-REFERENCE.md)** - Sound synthesis and music

### BASIC Programming
- **[BASIC-V2-REFERENCE.md](BASIC-V2-REFERENCE.md)** - Complete BASIC reference
- **[BASIC-V2-VOCABULARY-REFERENCE.md](BASIC-V2-VOCABULARY-REFERENCE.md)** - All BASIC keywords
- **[BASIC-V2-MATHEMATICAL-FUNCTIONS-REFERENCE.md](BASIC-V2-MATHEMATICAL-FUNCTIONS-REFERENCE.md)** - Math functions
- **[BASIC-V2-ERROR-MESSAGES-REFERENCE.md](BASIC-V2-ERROR-MESSAGES-REFERENCE.md)** - Error codes explained
- **[BASIC-V2-ABBREVIATIONS-REFERENCE.md](BASIC-V2-ABBREVIATIONS-REFERENCE.md)** - Keyword shortcuts

### I/O and Devices
- **[INPUT-OUTPUT-GUIDE-PART-1-REFERENCE.md](INPUT-OUTPUT-GUIDE-PART-1-REFERENCE.md)** - Cassette, RS-232, devices
- **[INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md](INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md)** - Serial bus, programming
- **[HARDWARE-PINOUTS-REFERENCE.md](HARDWARE-PINOUTS-REFERENCE.md)** - Physical connectors

---

## By Lesson Level

### Beginner Lessons (1-10)

**Focus:** BASIC programming, simple screen output, basic ML concepts

**Essential References:**
- BASIC-V2-REFERENCE.md
- PETSCII-AND-SCREEN-CODES.md
- C64-MACHINE-LANGUAGE-OVERVIEW.md (for intro to ML)

**Common Tasks:**
- PRINT and INPUT
- Screen colors
- Simple graphics characters
- First ML programs with SYS

### Intermediate Lessons (11-15)

**Focus:** Assembly fundamentals, sprites, joystick control

**Essential References:**
- 6510-QUICK-REFERENCE.md
- CIA-QUICK-REFERENCE.md (joystick)
- VIC-II-QUICK-REFERENCE.md (sprites, colors)
- BASIC-TO-ML-INTEGRATION.md (SYS, USR)
- C64-MEMORY-MAP.md

**Common Tasks:**
- Sprite movement
- Joystick reading
- Simple loops and comparisons in assembly
- POKE to screen memory

### Advanced Lessons (16-20)

**Focus:** Raster effects, music, advanced graphics

**Essential References:**
- VIC-II-QUICK-REFERENCE.md (raster IRQs)
- SID-CHIP-REFERENCE.md
- RASTER-INTERRUPTS-REFERENCE.md
- SPRITES-REFERENCE.md (multiplexing)
- VIC-II-GRAPHICS-MODES-REFERENCE.md

**Common Tasks:**
- Raster interrupts
- Color cycling
- Music players
- Sprite multiplexing
- Bitmap graphics

### Expert Lessons (21+)

**Focus:** Complete games, demos, advanced techniques

**Comprehensive References:**
- 6510-MICROPROCESSOR-REFERENCE.md (timing, advanced opcodes)
- 6526-CIA-REFERENCE.md (timers, advanced I/O)
- VIC-II-REFERENCE.md (advanced display modes)
- All specialized references as needed

---

## By Programming Task

### Input/Output

| Task | Primary Reference | Secondary |
|------|-------------------|-----------|
| Read joystick | CIA-QUICK-REFERENCE.md | - |
| Scan keyboard matrix | CIA-QUICK-REFERENCE.md | - |
| Keyboard via KERNAL | KERNAL-ROUTINES-REFERENCE.md | BASIC-V2-REFERENCE.md |
| File I/O | KERNAL-ROUTINES-REFERENCE.md | INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md |
| Serial bus (disk) | KERNAL-ROUTINES-REFERENCE.md | INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md |

### Graphics

| Task | Primary Reference | Secondary |
|------|-------------------|-----------|
| Change border/background | VIC-II-QUICK-REFERENCE.md | - |
| Create/move sprites | VIC-II-QUICK-REFERENCE.md | SPRITES-REFERENCE.md |
| Character colors | PETSCII-AND-SCREEN-CODES.md | VIC-II-QUICK-REFERENCE.md |
| Custom character set | PROGRAMMABLE-CHARACTERS-REFERENCE.md | VIC-II-QUICK-REFERENCE.md |
| Bitmap graphics | BITMAP-GRAPHICS-REFERENCE.md | VIC-II-GRAPHICS-MODES-REFERENCE.md |
| Multicolor mode | MULTICOLOR-MODE-REFERENCE.md | VIC-II-GRAPHICS-MODES-REFERENCE.md |
| Raster effects | RASTER-INTERRUPTS-REFERENCE.md | VIC-II-QUICK-REFERENCE.md |
| Sprite collision | VIC-II-QUICK-REFERENCE.md | SPRITES-REFERENCE.md |

### Sound

| Task | Primary Reference |
|------|-------------------|
| Simple tones | SID-CHIP-REFERENCE.md |
| Music player | SID-CHIP-REFERENCE.md |
| Sound effects | SID-CHIP-REFERENCE.md |

### Assembly Programming

| Task | Primary Reference | Secondary |
|------|-------------------|-----------|
| Instruction lookup | 6510-QUICK-REFERENCE.md | 6510-MICROPROCESSOR-REFERENCE.md |
| Addressing modes | 6510-QUICK-REFERENCE.md | C64-MACHINE-LANGUAGE-OVERVIEW.md |
| Common patterns | 6510-QUICK-REFERENCE.md | - |
| Call from BASIC | BASIC-TO-ML-INTEGRATION.md | - |
| Memory layout | C64-MEMORY-MAP.md | - |
| KERNAL calls | KERNAL-ROUTINES-REFERENCE.md | - |
| Timers | CIA-QUICK-REFERENCE.md | 6526-CIA-REFERENCE.md |
| Interrupts | RASTER-INTERRUPTS-REFERENCE.md | BASIC-TO-ML-INTEGRATION.md |

---

## Document Size Guide

### Quick References (< 20KB - Load First)
- CIA-QUICK-REFERENCE.md (12KB)
- 6510-QUICK-REFERENCE.md (12KB)
- VIC-II-QUICK-REFERENCE.md (17KB)
- PETSCII-AND-SCREEN-CODES.md (14KB)

### Medium References (20-40KB)
- Most focused topic references
- BASIC references
- Specialized graphics references

### Comprehensive References (> 80KB - Use Sparingly)
- 6526-CIA-REFERENCE.md (107KB) ← Hardware specs
- VIC-II-REFERENCE.md (87KB) ← Hardware specs
- 6510-MICROPROCESSOR-REFERENCE.md (85KB) ← Hardware specs

**Recommendation:** Start with quick references. Only load comprehensive references when you need hardware-level details (timing, electrical specs, pinouts).

---

## Curriculum Planning References

These documents help with lesson design and curriculum structure:

- **[PHASE-0-CURRICULUM.md](PHASE-0-CURRICULUM.md)** - Complete Phase 0 curriculum outline
- **[LESSON-ARCHETYPES.md](LESSON-ARCHETYPES.md)** - Discovery, Challenge, Synthesis, Deep Dive
- **[LESSON-PREFLIGHT-CHECKLIST.md](LESSON-PREFLIGHT-CHECKLIST.md)** - Quality checklist before publishing
- **[LESSON-WORKFLOW.md](LESSON-WORKFLOW.md)** - Lesson creation process
- **[TIER-1-CURRICULUM-REVIEW.md](TIER-1-CURRICULUM-REVIEW.md)** - Tier 1 analysis
- **[PATTERN-LIBRARY-ANALYSIS.md](PATTERN-LIBRARY-ANALYSIS.md)** - Common programming patterns

---

## Deprecated/Replaced Documents

These have been consolidated into newer references:

### Replaced by PETSCII-AND-SCREEN-CODES.md:
- ~~PETSCII-SCREEN-CODES.md~~
- ~~SCREEN-CODES-REFERENCE.md~~
- ~~PETSCII-REFERENCE.md~~

**Note:** Old files remain for compatibility but use the consolidated version.

---

## How to Use This Guide

### Scenario 1: Creating a Sprite Movement Lesson

1. Read [VIC-II-QUICK-REFERENCE.md](VIC-II-QUICK-REFERENCE.md) - Sprite section
2. Check [CIA-QUICK-REFERENCE.md](CIA-QUICK-REFERENCE.md) - Joystick reading
3. Reference [6510-QUICK-REFERENCE.md](6510-QUICK-REFERENCE.md) - Loop instructions
4. Verify against [SPRITES-REFERENCE.md](SPRITES-REFERENCE.md) if needed

### Scenario 2: Teaching KERNAL File I/O

1. Read [KERNAL-ROUTINES-REFERENCE.md](KERNAL-ROUTINES-REFERENCE.md) - File I/O section
2. Check [C64-MEMORY-MAP.md](C64-MEMORY-MAP.md) - Safe memory locations
3. Reference [BASIC-TO-ML-INTEGRATION.md](BASIC-TO-ML-INTEGRATION.md) - Calling from BASIC

### Scenario 3: Raster Interrupt Effect

1. Read [RASTER-INTERRUPTS-REFERENCE.md](RASTER-INTERRUPTS-REFERENCE.md)
2. Check [VIC-II-QUICK-REFERENCE.md](VIC-II-QUICK-REFERENCE.md) - IRQ registers
3. Reference [6510-QUICK-REFERENCE.md](6510-QUICK-REFERENCE.md) - IRQ handler patterns

---

## Contributing and Updates

When adding new reference documents:

1. Add entry to this guide in appropriate section
2. Include file size estimate
3. Cross-reference with related documents
4. Update "By Lesson Level" if relevant
5. Update "By Programming Task" if relevant

---

**Version:** 1.0
**Last Updated:** 2025-10-18
**Purpose:** Navigation and discovery for C64 reference library
