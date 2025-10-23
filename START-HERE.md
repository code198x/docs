# C64 Reference Guide - Start Here

**Purpose:** Navigation guide for all C64 reference documentation
**Updated:** 2025-10-21
**For:** Code Like It's 198x curriculum designers and lesson creators

---

## ⚠️ Important: Game References Are Educational Only

**All classic game names mentioned in this curriculum are LEARNING REFERENCES.**

Students build **original games inspired by** classic mechanics, NOT clones. When a lesson says "Build Tetris," it means: *Build an original falling-block puzzle game using rotation and line-clearing mechanics, with your own name, graphics, sounds, and implementation.*

See [CURRICULUM-OVERVIEW.md](CURRICULUM-OVERVIEW.md) for complete legal details.

---

## Quick Navigation

Looking for something specific? Use this guide to find the right reference document.

### 🎯 Most Common Tasks

| I need to... | Use this reference |
|--------------|-------------------|
| **Read joystick or keyboard** | [commodore-64/hardware/CIA-QUICK-REFERENCE.md](commodore-64/hardware/CIA-QUICK-REFERENCE.md) |
| **Move sprites or change colors** | [commodore-64/hardware/VIC-II-QUICK-REFERENCE.md](commodore-64/hardware/VIC-II-QUICK-REFERENCE.md) |
| **Look up an assembly instruction** | [commodore-64/hardware/6510-QUICK-REFERENCE.md](commodore-64/hardware/6510-QUICK-REFERENCE.md) |
| **Convert PETSCII to screen codes** | [commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md](commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md) |
| **Find where to put my ML program** | [commodore-64/memory-and-io/C64-MEMORY-MAP.md](commodore-64/memory-and-io/C64-MEMORY-MAP.md) |
| **Call ML from BASIC** | [commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md](commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md) |
| **Use a KERNAL routine** | [commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md](commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md) |

---

## Reference Documents by Topic

### Machine Language Programming

#### Quick References (Start Here)
- **[commodore-64/hardware/6510-QUICK-REFERENCE.md](commodore-64/hardware/6510-QUICK-REFERENCE.md)** - Instruction set, addressing modes, common patterns (12KB)
- **[commodore-64/hardware/CIA-QUICK-REFERENCE.md](commodore-64/hardware/CIA-QUICK-REFERENCE.md)** - Joystick, keyboard, timers (12KB)
- **[commodore-64/hardware/VIC-II-QUICK-REFERENCE.md](commodore-64/hardware/VIC-II-QUICK-REFERENCE.md)** - Sprites, colors, screen control (17KB)

#### Comprehensive References (Deep Dives)
- **[commodore-64/hardware/6510-MICROPROCESSOR-REFERENCE.md](commodore-64/hardware/6510-MICROPROCESSOR-REFERENCE.md)** - Complete CPU specifications (85KB)
- **[commodore-64/hardware/6526-CIA-REFERENCE.md](commodore-64/hardware/6526-CIA-REFERENCE.md)** - Complete I/O chip specs (107KB)
- **[commodore-64/hardware/VIC-II-REFERENCE.md](commodore-64/hardware/VIC-II-REFERENCE.md)** - Complete video chip specs (87KB)

#### Overview and Integration
- **[commodore-64/advanced/C64-MACHINE-LANGUAGE-OVERVIEW.md](commodore-64/advanced/C64-MACHINE-LANGUAGE-OVERVIEW.md)** - ML concepts for lesson design
- **[commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md](commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md)** - SYS, USR, IRQ, vectors
- **[commodore-64/memory-and-io/C64-MEMORY-MAP.md](commodore-64/memory-and-io/C64-MEMORY-MAP.md)** - Complete memory layout $0000-$FFFF
- **[commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md](commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md)** - All 39 KERNAL routines organized by function

### Graphics and Display

#### Focused References
- **[commodore-64/graphics/SPRITES-REFERENCE.md](commodore-64/graphics/SPRITES-REFERENCE.md)** - Complete sprite programming guide
- **[commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md](commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md)** - Character codes (consolidated)
- **[commodore-64/graphics/COLOR-COMBINATIONS-REFERENCE.md](commodore-64/graphics/COLOR-COMBINATIONS-REFERENCE.md)** - Readable color pairs
- **[commodore-64/hardware/VIC-II-GRAPHICS-MODES-REFERENCE.md](commodore-64/hardware/VIC-II-GRAPHICS-MODES-REFERENCE.md)** - Bitmap, multicolor, etc.

#### Specialized Topics
- **[commodore-64/graphics/PROGRAMMABLE-CHARACTERS-REFERENCE.md](commodore-64/graphics/PROGRAMMABLE-CHARACTERS-REFERENCE.md)** - Custom character sets
- **[commodore-64/graphics/MULTICOLOR-MODE-REFERENCE.md](commodore-64/graphics/MULTICOLOR-MODE-REFERENCE.md)** - Multicolor graphics
- **[commodore-64/graphics/BITMAP-GRAPHICS-REFERENCE.md](commodore-64/graphics/BITMAP-GRAPHICS-REFERENCE.md)** - High-res and multicolor bitmap
- **[commodore-64/memory-and-io/SCREEN-COLOR-MEMORY-REFERENCE.md](commodore-64/memory-and-io/SCREEN-COLOR-MEMORY-REFERENCE.md)** - Screen RAM and color RAM
- **[commodore-64/advanced/RASTER-INTERRUPTS-REFERENCE.md](commodore-64/advanced/RASTER-INTERRUPTS-REFERENCE.md)** - Raster effects and IRQs

### Sound
- **[commodore-64/hardware/SID-CHIP-REFERENCE.md](commodore-64/hardware/SID-CHIP-REFERENCE.md)** - Sound synthesis and music

### BASIC Programming
- **[commodore-64/basic-v2/BASIC-V2-REFERENCE.md](commodore-64/basic-v2/BASIC-V2-REFERENCE.md)** - Complete BASIC reference
- **[commodore-64/basic-v2/BASIC-V2-VOCABULARY-REFERENCE.md](commodore-64/basic-v2/BASIC-V2-VOCABULARY-REFERENCE.md)** - All BASIC keywords
- **[commodore-64/basic-v2/BASIC-V2-MATHEMATICAL-FUNCTIONS-REFERENCE.md](commodore-64/basic-v2/BASIC-V2-MATHEMATICAL-FUNCTIONS-REFERENCE.md)** - Math functions
- **[commodore-64/basic-v2/BASIC-V2-ERROR-MESSAGES-REFERENCE.md](commodore-64/basic-v2/BASIC-V2-ERROR-MESSAGES-REFERENCE.md)** - Error codes explained
- **[commodore-64/basic-v2/BASIC-V2-ABBREVIATIONS-REFERENCE.md](commodore-64/basic-v2/BASIC-V2-ABBREVIATIONS-REFERENCE.md)** - Keyword shortcuts

### I/O and Devices
- **[commodore-64/memory-and-io/INPUT-OUTPUT-GUIDE-PART-1-REFERENCE.md](commodore-64/memory-and-io/INPUT-OUTPUT-GUIDE-PART-1-REFERENCE.md)** - Cassette, RS-232, devices
- **[commodore-64/memory-and-io/INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md](commodore-64/memory-and-io/INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md)** - Serial bus, programming
- **[commodore-64/hardware/HARDWARE-PINOUTS-REFERENCE.md](commodore-64/hardware/HARDWARE-PINOUTS-REFERENCE.md)** - Physical connectors

---

## By Lesson Level

### Beginner Lessons (1-10)

**Focus:** BASIC programming, simple screen output, basic ML concepts

**Essential References:**
- commodore-64/basic-v2/BASIC-V2-REFERENCE.md
- commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md
- commodore-64/advanced/C64-MACHINE-LANGUAGE-OVERVIEW.md (for intro to ML)

**Common Tasks:**
- PRINT and INPUT
- Screen colors
- Simple graphics characters
- First ML programs with SYS

### Intermediate Lessons (11-15)

**Focus:** Assembly fundamentals, sprites, joystick control

**Essential References:**
- commodore-64/hardware/6510-QUICK-REFERENCE.md
- commodore-64/hardware/CIA-QUICK-REFERENCE.md (joystick)
- commodore-64/hardware/VIC-II-QUICK-REFERENCE.md (sprites, colors)
- commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md (SYS, USR)
- commodore-64/memory-and-io/C64-MEMORY-MAP.md

**Common Tasks:**
- Sprite movement
- Joystick reading
- Simple loops and comparisons in assembly
- POKE to screen memory

### Advanced Lessons (16-20)

**Focus:** Raster effects, music, advanced graphics

**Essential References:**
- commodore-64/hardware/VIC-II-QUICK-REFERENCE.md (raster IRQs)
- commodore-64/hardware/SID-CHIP-REFERENCE.md
- commodore-64/advanced/RASTER-INTERRUPTS-REFERENCE.md
- commodore-64/graphics/SPRITES-REFERENCE.md (multiplexing)
- commodore-64/hardware/VIC-II-GRAPHICS-MODES-REFERENCE.md

**Common Tasks:**
- Raster interrupts
- Color cycling
- Music players
- Sprite multiplexing
- Bitmap graphics

### Expert Lessons (21+)

**Focus:** Complete games, demos, advanced techniques

**Comprehensive References:**
- commodore-64/hardware/6510-MICROPROCESSOR-REFERENCE.md (timing, advanced opcodes)
- commodore-64/hardware/6526-CIA-REFERENCE.md (timers, advanced I/O)
- commodore-64/hardware/VIC-II-REFERENCE.md (advanced display modes)
- All specialized references as needed

---

## By Programming Task

### Input/Output

| Task | Primary Reference | Secondary |
|------|-------------------|-----------|
| Read joystick | commodore-64/hardware/CIA-QUICK-REFERENCE.md | - |
| Scan keyboard matrix | commodore-64/hardware/CIA-QUICK-REFERENCE.md | - |
| Keyboard via KERNAL | commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md | commodore-64/basic-v2/BASIC-V2-REFERENCE.md |
| File I/O | commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md | commodore-64/memory-and-io/INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md |
| Serial bus (disk) | commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md | commodore-64/memory-and-io/INPUT-OUTPUT-GUIDE-PART-2-REFERENCE.md |

### Graphics

| Task | Primary Reference | Secondary |
|------|-------------------|-----------|
| Change border/background | commodore-64/hardware/VIC-II-QUICK-REFERENCE.md | - |
| Create/move sprites | commodore-64/hardware/VIC-II-QUICK-REFERENCE.md | commodore-64/graphics/SPRITES-REFERENCE.md |
| Character colors | commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md | commodore-64/hardware/VIC-II-QUICK-REFERENCE.md |
| Custom character set | commodore-64/graphics/PROGRAMMABLE-CHARACTERS-REFERENCE.md | commodore-64/hardware/VIC-II-QUICK-REFERENCE.md |
| Bitmap graphics | commodore-64/graphics/BITMAP-GRAPHICS-REFERENCE.md | commodore-64/hardware/VIC-II-GRAPHICS-MODES-REFERENCE.md |
| Multicolor mode | commodore-64/graphics/MULTICOLOR-MODE-REFERENCE.md | commodore-64/hardware/VIC-II-GRAPHICS-MODES-REFERENCE.md |
| Raster effects | commodore-64/advanced/RASTER-INTERRUPTS-REFERENCE.md | commodore-64/hardware/VIC-II-QUICK-REFERENCE.md |
| Sprite collision | commodore-64/hardware/VIC-II-QUICK-REFERENCE.md | commodore-64/graphics/SPRITES-REFERENCE.md |

### Sound

| Task | Primary Reference |
|------|-------------------|
| Simple tones | commodore-64/hardware/SID-CHIP-REFERENCE.md |
| Music player | commodore-64/hardware/SID-CHIP-REFERENCE.md |
| Sound effects | commodore-64/hardware/SID-CHIP-REFERENCE.md |

### Assembly Programming

| Task | Primary Reference | Secondary |
|------|-------------------|-----------|
| Instruction lookup | commodore-64/hardware/6510-QUICK-REFERENCE.md | commodore-64/hardware/6510-MICROPROCESSOR-REFERENCE.md |
| Addressing modes | commodore-64/hardware/6510-QUICK-REFERENCE.md | commodore-64/advanced/C64-MACHINE-LANGUAGE-OVERVIEW.md |
| Common patterns | commodore-64/hardware/6510-QUICK-REFERENCE.md | - |
| Call from BASIC | commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md | - |
| Memory layout | commodore-64/memory-and-io/C64-MEMORY-MAP.md | - |
| KERNAL calls | commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md | - |
| Timers | commodore-64/hardware/CIA-QUICK-REFERENCE.md | commodore-64/hardware/6526-CIA-REFERENCE.md |
| Interrupts | commodore-64/advanced/RASTER-INTERRUPTS-REFERENCE.md | commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md |

---

## Document Size Guide

### Quick References (< 20KB - Load First)
- commodore-64/hardware/CIA-QUICK-REFERENCE.md (12KB)
- commodore-64/hardware/6510-QUICK-REFERENCE.md (12KB)
- commodore-64/hardware/VIC-II-QUICK-REFERENCE.md (17KB)
- commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md (14KB)

### Medium References (20-40KB)
- Most focused topic references
- BASIC references
- Specialized graphics references

### Comprehensive References (> 80KB - Use Sparingly)
- commodore-64/hardware/6526-CIA-REFERENCE.md (107KB) ← Hardware specs
- commodore-64/hardware/VIC-II-REFERENCE.md (87KB) ← Hardware specs
- commodore-64/hardware/6510-MICROPROCESSOR-REFERENCE.md (85KB) ← Hardware specs

**Recommendation:** Start with quick references. Only load comprehensive references when you need hardware-level details (timing, electrical specs, pinouts).

---

## Curriculum Planning References

These documents help with lesson design and curriculum structure:

### Legal & Educational Use
- **[LEGAL-EDUCATIONAL-USE.md](LEGAL-EDUCATIONAL-USE.md)** - Important: How classic games are used as educational references (READ FIRST!)

### Curriculum Overview
- **[CURRICULUM-OVERVIEW.md](CURRICULUM-OVERVIEW.md)** - Complete 8256-lesson curriculum (Phase 0 + Phases 1-16)

### Commodore 64 Curriculum

#### Phase 0: BASIC Programming (64 lessons)
- **[commodore-64/phase-0/overview.md](commodore-64/phase-0/overview.md)** - Complete Phase 0 overview
- **[commodore-64/phase-0/tier-1/README.md](commodore-64/phase-0/tier-1/README.md)** - Discovery tier (L1-16, 6 games)
- **[commodore-64/phase-0/tier-2/README.md](commodore-64/phase-0/tier-2/README.md)** - Building tier (L17-32, 4 games)
- **[commodore-64/phase-0/tier-3/README.md](commodore-64/phase-0/tier-3/README.md)** - Mastery tier (L33-48, 3 professional games)
- **[commodore-64/phase-0/tier-4/README.md](commodore-64/phase-0/tier-4/README.md)** - Limits tier (L49-64, 3 ceiling demonstrations)
- **Individual Lessons:** [commodore-64/phase-0/tier-{1,2,3,4}/lesson-NNN.md](commodore-64/phase-0/) (64 lesson specification files)

#### Phase Curriculum Documents (Phases 1-16 - All Commodore 64)
- **[commodore-64/PHASE-1-CURRICULUM.md](commodore-64/PHASE-1-CURRICULUM.md)** - Assembly + Hardware Fundamentals (512 lessons)
- **[commodore-64/PHASE-2-CURRICULUM.md](commodore-64/PHASE-2-CURRICULUM.md)** - Action Foundations (512 lessons)
- **[commodore-64/PHASE-3-CURRICULUM.md](commodore-64/PHASE-3-CURRICULUM.md)** - Puzzle Games (512 lessons)
- **[commodore-64/PHASE-4-CURRICULUM.md](commodore-64/PHASE-4-CURRICULUM.md)** - Platformers Deep Dive (512 lessons)
- **[commodore-64/PHASE-5-CURRICULUM.md](commodore-64/PHASE-5-CURRICULUM.md)** - Beat-em-ups & Brawlers (384 lessons)
- **[commodore-64/PHASE-6-CURRICULUM.md](commodore-64/PHASE-6-CURRICULUM.md)** - Shoot-em-ups (1024 lessons)
- **[commodore-64/PHASE-7-CURRICULUM.md](commodore-64/PHASE-7-CURRICULUM.md)** - RPG Systems (1024 lessons)
- **[commodore-64/PHASE-8-CURRICULUM.md](commodore-64/PHASE-8-CURRICULUM.md)** - Adventure Games (512 lessons)
- **[commodore-64/PHASE-9-CURRICULUM.md](commodore-64/PHASE-9-CURRICULUM.md)** - Strategy Games (512 lessons)
- **[commodore-64/PHASE-10-CURRICULUM.md](commodore-64/PHASE-10-CURRICULUM.md)** - Racing & Driving (384 lessons)
- **[commodore-64/PHASE-11-CURRICULUM.md](commodore-64/PHASE-11-CURRICULUM.md)** - Fighting Games (384 lessons)
- **[commodore-64/PHASE-12-CURRICULUM.md](commodore-64/PHASE-12-CURRICULUM.md)** - Sports Games (384 lessons)
- **[commodore-64/PHASE-13-CURRICULUM.md](commodore-64/PHASE-13-CURRICULUM.md)** - Multi-Genre Synthesis (512 lessons)
- **[commodore-64/PHASE-14-CURRICULUM.md](commodore-64/PHASE-14-CURRICULUM.md)** - Complete Games (512 lessons)
- **[commodore-64/PHASE-15-CURRICULUM.md](commodore-64/PHASE-15-CURRICULUM.md)** - Technical Showcase & Epics (512 lessons)
- **[commodore-64/PHASE-16-CURRICULUM.md](commodore-64/PHASE-16-CURRICULUM.md)** - The Gauntlet + Mastery Projects (512 lessons)

### Lesson Design Resources
- **[LESSON-ARCHETYPES.md](LESSON-ARCHETYPES.md)** - Discovery, Challenge, Synthesis, Deep Dive
- **[LESSON-PREFLIGHT-CHECKLIST.md](LESSON-PREFLIGHT-CHECKLIST.md)** - Quality checklist before publishing
- **[LESSON-WORKFLOW.md](LESSON-WORKFLOW.md)** - Lesson creation process
- **[TIER-1-CURRICULUM-REVIEW.md](TIER-1-CURRICULUM-REVIEW.md)** - Tier 1 analysis
- **[PATTERN-LIBRARY-ANALYSIS.md](PATTERN-LIBRARY-ANALYSIS.md)** - Common programming patterns

### Asset Creation & Contribution
- **[ASSET-GUIDELINES.md](ASSET-GUIDELINES.md)** - Creating and contributing sprites, music, and graphics (CC0 assets, tools, tutorials)

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

1. Read [commodore-64/hardware/VIC-II-QUICK-REFERENCE.md](commodore-64/hardware/VIC-II-QUICK-REFERENCE.md) - Sprite section
2. Check [commodore-64/hardware/CIA-QUICK-REFERENCE.md](commodore-64/hardware/CIA-QUICK-REFERENCE.md) - Joystick reading
3. Reference [commodore-64/hardware/6510-QUICK-REFERENCE.md](commodore-64/hardware/6510-QUICK-REFERENCE.md) - Loop instructions
4. Verify against [commodore-64/graphics/SPRITES-REFERENCE.md](commodore-64/graphics/SPRITES-REFERENCE.md) if needed

### Scenario 2: Teaching KERNAL File I/O

1. Read [commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md](commodore-64/advanced/KERNAL-ROUTINES-REFERENCE.md) - File I/O section
2. Check [commodore-64/memory-and-io/C64-MEMORY-MAP.md](commodore-64/memory-and-io/C64-MEMORY-MAP.md) - Safe memory locations
3. Reference [commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md](commodore-64/basic-v2/BASIC-TO-ML-INTEGRATION.md) - Calling from BASIC

### Scenario 3: Raster Interrupt Effect

1. Read [commodore-64/advanced/RASTER-INTERRUPTS-REFERENCE.md](commodore-64/advanced/RASTER-INTERRUPTS-REFERENCE.md)
2. Check [commodore-64/hardware/VIC-II-QUICK-REFERENCE.md](commodore-64/hardware/VIC-II-QUICK-REFERENCE.md) - IRQ registers
3. Reference [commodore-64/hardware/6510-QUICK-REFERENCE.md](commodore-64/hardware/6510-QUICK-REFERENCE.md) - IRQ handler patterns

---

## Contributing and Updates

When adding new reference documents:

1. Add entry to this guide in appropriate section
2. Include file size estimate
3. Cross-reference with related documents
4. Update "By Lesson Level" if relevant
5. Update "By Programming Task" if relevant

---

**Version:** 2.1
**Last Updated:** 2025-10-23
**Purpose:** Navigation and discovery for C64 reference library

**Changes in v2.1:**
- Completed system-first reorganization with ALL C64 references moved to commodore-64/
- Created organized subdirectories: basic-v2/, graphics/, memory-and-io/, advanced/, tools/
- Updated all reference paths throughout document to reflect new structure
- Consolidated all C64-specific content under commodore-64/ for future multi-platform support

**Changes in v2.0:**
- Restructured to system-first organization (commodore-64/)
- Added granular Phase 0 documentation (tier READMEs + 64 lesson specs)
- Updated all hardware reference paths to commodore-64/hardware/
- Added lesson-level navigation for curriculum planning
