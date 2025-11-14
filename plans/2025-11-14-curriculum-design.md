# Code Like It's 198x - Curriculum Design

**Date:** 2025-11-14
**Status:** Foundation Design
**Scope:** Complete curriculum redesign from clean slate

## Executive Summary

Code Like It's 198x is a comprehensive retro game development education platform teaching programming across vintage computing platforms from approximately 1975-2005. The curriculum spans multiple platforms, teaching learners to create commercial-quality games using assembly language and gateway languages (BASIC, AMOS), progressing from simple early-era games to sophisticated late-era titles.

**Scale:** Potentially 1,000-4,000+ lessons per platform across 8 assembly phases, built iteratively over years with AI-assisted content creation and rigorous automated validation.

**Initial Focus:** Parallel development of Phase 1 (assembly foundation) across four core platforms: Commodore 64, Sinclair ZX Spectrum, Commodore Amiga, and Nintendo NES.

## Core Learning Principles

All curriculum content must adhere to these fundamental principles:

1. **Fun game fast** - Every lesson builds toward a real, working, FUN game; optimize for reaching playable results within first few lessons

2. **Commercial-quality at every phase** - All games should meet commercial standards appropriate to their complexity (Phase 1 = 1982-era simple games, Phase 8 = 1992-era sophisticated games)

3. **Multiple games per platform** - Not just one game per phase, but several complete projects

4. **Self-directed learning** - No instructor dependency; all content assumes independent study

5. **Incremental visible progress** - Every lesson delivers something visible (screen color change, text output, sprite, etc.)

6. **Historical authenticity with modern optimization** - Teach period-accurate techniques first, introduce later-discovered optimizations only when learners have foundation to understand why they're better

7. **Platform completeness** - Cover base systems plus expansions and recreations from during and after original lifespan

8. **Verified accuracy** - All references and code must be historically accurate and technically correct

## Learner Philosophy

- **Entry points:** Phase 0 for absolute beginners, Phase 1+ for those with programming experience; trust learners to self-select
- **Primary path:** Single platform deep-dive through all phases (but support multi-platform explorers)
- **Progression:** Tangible milestones at tier completion; working features demonstrate learning

## Curriculum Structure

### Three-Tier Hierarchy

1. **Phase** - Major skill level
   - Phase 0: Gateway language (BASIC, AMOS, etc.) - optional for beginners
   - Phases 1-8: Assembly programming with increasing complexity

2. **Tier** - One major concept/feature
   - 8-16 tiers per phase
   - Learner has working milestone at end of each tier
   - Represents conceptual grouping and mini-milestone

3. **Lesson** - Individual teaching unit
   - 16-32 lessons per tier
   - Specific learning objective with visible result
   - Simple example → Complex example progression

### Scale Implications

- **Per phase:** 8-16 tiers × 16-32 lessons = 128-512 lessons
- **Per platform:** 8 assembly phases + 1 optional BASIC phase
- **Total per platform:** Potentially 1,000-4,000+ lessons
- **Across platforms:** Tens of thousands of lessons over time

## Platform Scope

### Core Platforms (Initial Development)

1. **commodore-64** - Commodore 64 (1982-1994)
2. **sinclair-zx-spectrum** - Sinclair ZX Spectrum (1982-1992)
3. **commodore-amiga** - Commodore Amiga (1985-1996)
4. **nintendo-nes** - Nintendo Entertainment System (1983-1994)

### Future Platform Expansion

- **8-bit home computers:** `acorn-bbc-micro`, `amstrad-cpc`, `atari-8-bit`, `msx`
- **Consoles:** `atari-2600`, `sega-master-system`, `nintendo-game-boy`, `nintendo-snes`, `sega-genesis-mega-drive`
- **16-bit computers:** `atari-st`, `sharp-x68000`
- **Early PC/DOS era:** TBD naming convention
- **Enhanced systems:** `sinclair-zx-spectrum-next`, `mega65` (treated as separate platforms, potentially Phase 9+)

### Naming Convention

- **Standard pattern:** `manufacturer-system` (kebab-case)
- **Multi-manufacturer standards:** Use standard name (e.g., `msx`)
- **Regional variants:** Combine both names (e.g., `sega-genesis-mega-drive`)
- **Product families:** Use family name (e.g., `atari-8-bit`)

## Platform Quality Benchmarks

### Commodore 64 (1982-1994)

**Phase 1: Foundation (1982-1983)**
- **Commercial Quality Era:** Early arcade ports and simple original games
- **Technical Capabilities:** Basic sprite usage, simple backgrounds, fundamental sound
- **Example Games:** Choplifter (1982), Pac-Man (1983), Wizard of Wor (1983)
- **Techniques Taught:** 6510 assembly basics, VIC-II basics, simple sprite positioning, basic SID sound, CIA input

**Phase 2: Movement (1983-1984)**
- **Commercial Quality Era:** Smooth scrolling games emerge
- **Technical Capabilities:** Hardware scrolling, multi-color sprites, improved music
- **Example Games:** International Soccer (1983), Beach-Head (1983), Blue Max (1983)
- **Techniques Taught:** Smooth hardware scrolling, multi-color sprite modes, character animation, simple music routines, collision detection

**Phase 3: Sophistication (1984-1985)**
- **Commercial Quality Era:** Isometric games, advanced arcade conversions
- **Technical Capabilities:** Isometric projection, sprite multiplexing, advanced controls
- **Example Games:** Impossible Mission (1984), Ghostbusters (1984), Paradroid (1985)
- **Techniques Taught:** Isometric graphics, sprite multiplexing, raster interrupts, advanced SID techniques, menu systems

**Phase 4: Mastery Begins (1985-1987)**
- **Commercial Quality Era:** Polished commercial titles, multi-load epics
- **Technical Capabilities:** Advanced scrolling, sophisticated music, large game worlds
- **Example Games:** The Last Ninja (1987), Uridium (1986), International Karate (1985)
- **Techniques Taught:** Diagonal/multi-directional scrolling, advanced sprite multiplexing, multi-load techniques, advanced music, complex animation

**Phase 5: Technical Excellence (1987-1988)**
- **Commercial Quality Era:** Peak of 8-bit design
- **Technical Capabilities:** Parallax scrolling, advanced raster effects, polished presentation
- **Example Games:** The Last Ninja 2 (1988), R-Type (1988), IK+ (1988)
- **Techniques Taught:** Parallax scrolling, advanced raster effects, sophisticated AI, advanced collision, loader systems

**Phase 6: Innovation (1988-1990)**
- **Commercial Quality Era:** Technical showcases pushing hardware limits
- **Technical Capabilities:** Complex effects, large sprites, advanced music synthesis
- **Example Games:** Creatures (1990), Retrograde (1989), Last Ninja 3 (1991)
- **Techniques Taught:** Software sprite techniques, advanced copper-like effects, sophisticated music drivers, dynamic difficulty, advanced memory management

**Phase 7: Near-Perfection (1990-1991)**
- **Commercial Quality Era:** "Impossible" technical achievements
- **Technical Capabilities:** Everything combined at high quality
- **Example Games:** Turrican (1990), Rick Dangerous 2 (1990), SWIV (1991)
- **Techniques Taught:** Massive game worlds, screen-sized bosses, polished 60fps animation, audio-visual synchronization, save systems

**Phase 8: Ultimate Achievement (1991-1993)**
- **Commercial Quality Era:** The absolute pinnacle of C64 development
- **Technical Capabilities:** Commercial quality rivaling 16-bit systems
- **Example Games:** Turrican II (1991), Mayhem in Monsterland (1993), Creatures 2 (1992)
- **Techniques Taught:** Full-screen parallax scrolling, advanced sprite multiplexing (dozens on screen), sophisticated physics, cinematic presentation, all techniques combined

### Sinclair ZX Spectrum (1982-1992)

**Phase 1: Foundation (1982-1983)**
- **Commercial Quality Era:** Early platform games and arcade ports
- **Technical Capabilities:** Character graphics, simple attributes, basic sound
- **Example Games:** Manic Miner (1983), Jetpac (1983), Jet Set Willy (1984)
- **Techniques Taught:** Z80 assembly basics, screen memory and attributes, character graphics, beeper sound, keyboard input

**Phase 2: Color Management (1983-1984)**
- **Commercial Quality Era:** Polished platformers and arcade games
- **Technical Capabilities:** Managing color clash, animation techniques, music
- **Example Games:** Atic Atac (1983), Sabre Wulf (1984), Manic Miner clones
- **Techniques Taught:** Attribute management, color clash mitigation, character animation, simple beeper music, screen scrolling

**Phase 3: Isometric Revolution (1984-1985)**
- **Commercial Quality Era:** Filmation engine and isometric games
- **Technical Capabilities:** Isometric 3D, image masking, complex game logic
- **Example Games:** Knight Lore (1984), Alien 8 (1985), Batman (1986)
- **Techniques Taught:** Isometric projection, image masking for depth, room-based systems, object interaction, puzzle mechanics

**Phase 4: Software Sprites (1985-1986)**
- **Commercial Quality Era:** Sophisticated action games
- **Technical Capabilities:** Software sprite systems, fast graphics routines
- **Example Games:** Exolon (1987), Head Over Heels (1987), Starquake (1985)
- **Techniques Taught:** Software sprite implementation, fast block graphics, background preservation, optimized Z80 code, complex level design

**Phase 5: 128K Enhancement (1986-1987)**
- **Commercial Quality Era:** 128K-enhanced games with AY sound
- **Technical Capabilities:** 128K memory, AY-3-8912 sound chip, improved graphics
- **Example Games:** Robocop (1988), Operation Wolf (1988), Afterburner (1988)
- **Techniques Taught:** 128K memory management, AY-3-8912 music, multi-load systems, enhanced graphics, bank switching

**Phase 6: Arcade Conversions (1987-1988)**
- **Commercial Quality Era:** High-quality arcade ports
- **Technical Capabilities:** Smooth animation, complex game systems
- **Example Games:** Operation Thunderbolt (1989), Turbo Esprit (1986), Highway Encounter (1985)
- **Techniques Taught:** Smooth character movement, complex AI, multi-stage games, 3D perspective, advanced game state management

**Phase 7: Technical Mastery (1988-1989)**
- **Commercial Quality Era:** Pushing hardware to its limits
- **Technical Capabilities:** "Impossible" arcade conversions
- **Example Games:** R-Type (1988), Chase HQ (1989), Rainbow Islands (1990)
- **Techniques Taught:** Advanced smooth scrolling, large sprite handling, complex backgrounds, optimized rendering loops, all techniques efficiently combined

**Phase 8: Ultimate Achievement (1989-1992)**
- **Commercial Quality Era:** Peak Spectrum development
- **Technical Capabilities:** Rivaling more powerful systems
- **Example Games:** Midnight Resistance (1990), Dun Darach (1985), Pang (1990)
- **Techniques Taught:** Full Z80 optimization mastery, advanced attribute tricks, sophisticated multi-load, commercial-grade polish, all advanced techniques at high quality

### Commodore Amiga (1985-1996)

**Phase 1: Custom Chip Introduction (1985-1987)**
- **Commercial Quality Era:** Early Amiga games, learning the hardware
- **Technical Capabilities:** Basic sprite usage, simple copper effects, Paula audio
- **Example Games:** Defender of the Crown (1986), Marble Madness (1986), Faery Tale Adventure (1987)
- **Techniques Taught:** 68000 assembly basics, hardware sprite system, playfield graphics (bitplanes), basic copper programming, Paula 4-channel audio

**Phase 2: Blitter & Copper (1987-1988)**
- **Commercial Quality Era:** Utilizing Amiga's custom chips effectively
- **Technical Capabilities:** Blitter operations, copper effects, improved audio
- **Example Games:** Speedball (1988), Blood Money (1989), Xenon (1988)
- **Techniques Taught:** Blitter for fast graphics, advanced copper effects, dual-playfield scrolling, MOD music basics, sprite multiplexing

**Phase 3: Graphics Showcase (1988-1989)**
- **Commercial Quality Era:** Amiga as technical showcase
- **Technical Capabilities:** Parallax scrolling, massive sprite usage, visual effects
- **Example Games:** Shadow of the Beast (1989), Agony (1992), First Samurai (1991)
- **Techniques Taught:** Multiple parallax layers, advanced sprite multiplexing, copper list mastery, palette effects, large sprite objects (BOBs)

**Phase 4: Speed & Action (1989-1990)**
- **Commercial Quality Era:** Fast-paced action games
- **Technical Capabilities:** Optimized game loops, complex physics
- **Example Games:** Speedball 2 (1990), Shadow Fighter (1994), Apidya (1992)
- **Techniques Taught:** Optimized 68000 code for speed, fast multi-directional scrolling, complex physics simulation, advanced collision, smooth 50fps gameplay

**Phase 5: Technical Excellence (1990-1991)**
- **Commercial Quality Era:** Amiga's golden age
- **Technical Capabilities:** Everything combined at high quality
- **Example Games:** Turrican II (1991), Gods (1991), Agony (1992)
- **Techniques Taught:** Massive game worlds, screen-filled bosses, sophisticated animation, advanced audio synchronization, professional game structure

**Phase 6: Physics & Simulation (1991-1992)**
- **Commercial Quality Era:** Sophisticated gameplay mechanics
- **Technical Capabilities:** Advanced physics, realistic simulation
- **Example Games:** Pinball Dreams (1992), Stunt Car Racer (1989), Lotus Turbo Challenge (1990)
- **Techniques Taught:** Advanced physics engines, realistic ball/vehicle simulation, 3D perspective techniques, sophisticated collision systems, real-time calculations

**Phase 7: AGA Era (1992-1994)**
- **Commercial Quality Era:** AGA chipset games (Amiga 1200/4000)
- **Technical Capabilities:** 256 colors, faster CPU, CD-ROM
- **Example Games:** Banshee (1994), Super Stardust (1994), Guardian (1994)
- **Techniques Taught:** AGA chipset programming, 256-color graphics, CD-ROM streaming, advanced 3D effects, 68020/030 optimization

**Phase 8: Ultimate Achievement (1994-1996)**
- **Commercial Quality Era:** Peak Amiga sophistication
- **Technical Capabilities:** Commercial quality matching early 32-bit systems
- **Example Games:** Worms (1995), Alien Breed 3D (1995), Virtual Karting (1995)
- **Techniques Taught:** Full AGA mastery, advanced 3D rendering, complex game engines, professional-grade polish, all advanced techniques combined

### Nintendo NES (1983-1994)

**Phase 1: Simple Mappers (1983-1985)**
- **Commercial Quality Era:** Early Famicom/NES games
- **Technical Capabilities:** 40KB games, basic scrolling, simple mappers
- **Example Games:** Donkey Kong (1983), Super Mario Bros. (1985), Excitebike (1984)
- **Techniques Taught:** 6502 assembly basics, PPU basics (nametables, pattern tables), simple sprite management, APU sound programming, controller input

**Phase 2: Bank Switching Begins (1985-1986)**
- **Commercial Quality Era:** Larger games with basic mappers
- **Technical Capabilities:** UNROM/CNROM mappers, larger ROMs, CHR RAM
- **Example Games:** Metroid (1986), Castlevania (1986), Kid Icarus (1986)
- **Techniques Taught:** Basic bank switching (PRG), CHR RAM for dynamic graphics, password save systems, sprite multiplexing basics, scrolling techniques

**Phase 3: MMC1 Revolution (1986-1987)**
- **Commercial Quality Era:** Multi-directional scrolling, saved games
- **Technical Capabilities:** MMC1 mapper, battery saves, advanced scrolling
- **Example Games:** The Legend of Zelda (1986), Mega Man (1987), Zelda II (1987)
- **Techniques Taught:** MMC1 mapper programming, multi-directional scrolling, battery-backed save RAM, large game worlds, advanced sprite techniques

**Phase 4: Advanced Mappers (1987-1988)**
- **Commercial Quality Era:** Complex action games
- **Technical Capabilities:** Sprite multiplexing, advanced sound, custom mappers
- **Example Games:** Contra (1987), Mike Tyson's Punch-Out!! (1987), Mega Man 2 (1988)
- **Techniques Taught:** Advanced sprite multiplexing (8+ per scanline), MMC2 mapper tricks, complex animation, advanced APU techniques, boss battle programming

**Phase 5: MMC3 & Scanline Effects (1988-1989)**
- **Commercial Quality Era:** Sophisticated visual effects
- **Technical Capabilities:** MMC3 IRQ scanline counter, split-screen effects
- **Example Games:** Super Mario Bros. 3 (1988), Ninja Gaiden (1988), Kirby's Adventure (1993)
- **Techniques Taught:** MMC3 mapper and IRQ system, scanline-based raster effects, split-screen techniques (HUD + scroll), advanced scrolling windows, large ROM management

**Phase 6: Advanced Audio & Large ROMs (1989-1990)**
- **Commercial Quality Era:** Peak NES sophistication
- **Technical Capabilities:** VRC6/VRC7 audio, 512KB+ ROMs
- **Example Games:** Castlevania III (1989), Lagrange Point (1991), Teenage Mutant Ninja Turtles III (1991)
- **Techniques Taught:** VRC6 expansion audio (3 extra channels), VRC7 FM synthesis, large ROM bank management, advanced music composition, complex game states

**Phase 7: MMC5 Features (1990-1992)**
- **Commercial Quality Era:** Technical showcase titles
- **Technical Capabilities:** MMC5 advanced features, massive ROMs
- **Example Games:** Castlevania: Dracula's Curse (1989), Just Breed (1992), Metal Slader Glory (1991)
- **Techniques Taught:** MMC5 mapper mastery, advanced graphics modes, 1MB ROM management, sophisticated visual effects, complex game engines

**Phase 8: Ultimate Achievement (1992-1994)**
- **Commercial Quality Era:** Peak NES technical achievement
- **Technical Capabilities:** All advanced techniques combined
- **Example Games:** Kirby's Adventure (1993), Mr. Gimmick (1992), Battletoads & Double Dragon (1993)
- **Techniques Taught:** Full mapper mastery, advanced compression techniques, professional-grade animation, sophisticated sound engines, all techniques at commercial quality

## Modern Techniques on Original Hardware

### Integration Strategy

Modern optimization techniques discovered post-era but running on original hardware are integrated based on complexity:

- **Simple optimizations** - Taught in appropriate phase with historical context (footnote approach)
- **Advanced techniques** - Phase 8 after fundamentals are mastered
- **Topic-specific improvements** - Integrated when teaching that topic

### Examples

- C64 demo scene tricks from 2000s-2020s (FLD, VSP, advanced timing tricks)
- ZX Spectrum modern optimization techniques
- NES homebrew discoveries (new mapper tricks, compression methods)
- Amiga copper list optimizations

## Content Standards & Validation

### Technical Validation (Automated)

**Code Compilation & Execution:**
- Every code sample MUST compile without errors using period-appropriate tools
- Every compiled program MUST execute in authentic emulator
- Validation runs as mandatory step before lesson publication

**Output Verification:**
- Screenshots captured from actual emulator execution
- Visual inspection confirms expected output (no error messages, no blank screens)
- Screenshots show working features, not crashes
- Automated checks where possible (file exists, minimum size, format validation)

**Code Standards:**
- Proper commenting for learning context (every significant line explained)
- Consistent naming conventions per platform
- Period-appropriate coding style
- No reserved variable conflicts (e.g., C64 BASIC ST, TI, TI$)
- Assembly code follows platform conventions

### Pedagogical Standards

**Learning Progression:**
- Clear prerequisite declarations
- Concepts introduced in logical order
- Incremental complexity (simple example → complex example)
- Each lesson delivers visible progress
- Exercises build on previous lessons

**Lesson Structure:**
- Clear learning objectives stated upfront
- Working code examples with thorough explanation
- Concepts explained at appropriate depth for phase level
- Challenges/exercises that reinforce learning
- Reference material for deeper exploration

**Quality Benchmarks:**
- Code quality matches commercial standards for that phase/era
- Games are genuinely fun to play, not just technical exercises
- Balance between teaching concepts and building complete projects
- Self-directed learners can succeed without instructor

### Editorial Standards

**Voice & Tone:**
- British English throughout (colour, learnt, etc.)
- Exception: "program" for computer programs (standard computing term)
- Clear, direct explanations without marketing hype
- Authentic period perspective with modern insights where appropriate
- Encouraging without being condescending

**Terminology:**
- Period-accurate terms for hardware/techniques
- Consistent naming across lessons (establish glossary)
- Platform-specific terminology used correctly
- Modern terms introduced only when teaching modern techniques

**Historical Accuracy:**
- All technical references verified against authentic documentation
- Game examples accurately represent their era
- Techniques match period practices (unless teaching modern optimization)
- Hardware capabilities correctly described
- No anachronistic references

### Validation Workflow

**Mandatory Checklist (Before Publication):**
1. ☐ Code compiles without errors
2. ☐ Code executes in emulator successfully
3. ☐ Screenshots captured from actual execution
4. ☐ Screenshots visually inspected (no errors/blanks visible)
5. ☐ Code comments adequate for learning
6. ☐ British English verified (automated grep check)
7. ☐ Learning objectives clear and met
8. ☐ Prerequisites correctly declared
9. ☐ Manual review completed
10. ☐ All files in correct repository locations

**Three-Stage Validation:**
1. **Automated technical** - Compilation, execution, file checks
2. **Automated editorial** - British English, formatting, structure
3. **Manual review** - Pedagogy, flow, accuracy, engagement

## Content Creation Workflow

### Level 1: Curriculum Definition

**Per Platform, Define:**
- Phase 1-8 structure (benchmarks defined above)
- Tier breakdown within each phase (8-16 tiers per phase)
- Each tier represents one major concept/working feature
- Cross-reference with commercial games to ensure coverage

**Output:** Curriculum outline document per platform
- Example: `docs/curriculum/commodore-64-curriculum.md`
- Lists all phases, all tiers, tier objectives

### Level 2: Tier Specification

**For Each Tier, Define:**
- Tier learning objective (what working feature will exist at completion)
- Concepts to cover within the tier
- Prerequisites from previous tiers
- Estimated lesson count (16-32 lessons)
- Target commercial quality benchmark
- Reference games demonstrating the techniques

**Output:** Tier specification document
- Example: `docs/commodore-64/phase-1/tier-3-sprite-movement-spec.md`
- Detailed enough to guide lesson creation

### Level 3: Lesson Specification

**For Each Lesson, Define:**
- Specific learning objective (one concept or technique)
- What visible result the learner will achieve
- Code examples to include (simple → complex)
- Key teaching points
- Prerequisites from previous lessons
- Expected output (for validation)
- Exercise/challenge ideas

**Detail Level:** Detailed blueprint
- Not a complete script, but comprehensive guidance
- Ensures consistency while allowing AI creativity within bounds
- Includes validation criteria (what screenshot should show)

**Output:** Lesson specification
- Example: `docs/commodore-64/phase-1/tier-3/lesson-042-spec.md`

### Level 4: AI-Assisted Lesson Creation

**Workflow:**
1. AI drafts lesson from specification
2. AI creates code samples following standards
3. Automated validation - Compile and execute code
4. AI captures screenshots from emulator
5. AI verifies screenshots using Read tool (describes visible content, checks for errors)
6. If validation fails - Fix code → Recompile → Re-capture → Re-verify (iterate)
7. Manual review - Human checks pedagogy, flow, engagement
8. If review requires changes - Refine and re-validate
9. Final validation - Complete checklist
10. Publish - Files placed in correct locations

**Iteration:** Steps 3-6 may repeat multiple times until code works correctly

### AI Assistant Role

**What AI does:**
- Drafts lesson content from specifications
- Writes code samples following standards
- Runs validation toolchain
- Captures and verifies screenshots
- Iterates on failures until validation passes
- Formats content consistently

**What Human does:**
- Creates curriculum structure
- Writes tier and lesson specifications
- Reviews lesson pedagogy and flow
- Ensures content matches vision
- Makes final publication decisions
- Monitors quality trends

### Quality Assurance Loop

**Continuous Improvement:**
- Track common validation failures
- Update specifications to prevent recurring issues
- Refine AI prompts based on lessons learned
- Build library of successful patterns
- Document edge cases and solutions

## Repository Structure

### Code Samples Repository

```
/code-samples/
  /commodore-64/
    /phase-0/       # BASIC (optional, deprioritized)
    /phase-1/
      /tier-1/
        /lesson-001/
          example-1.bas
          example-1.prg
          example-2.bas
          example-2.prg
        /lesson-002/
      /tier-2/
    /phase-2/
  /sinclair-zx-spectrum/
    /phase-0/       # BASIC (optional, deprioritized)
    /phase-1/
      /tier-1/
        /lesson-001/
          example-1.asm
          example-1.tap
  /commodore-amiga/
    /phase-0/       # AMOS BASIC (optional, deprioritized)
    /phase-1/
      /tier-1/
        /lesson-001/
          example-1.asm
  /nintendo-nes/
    # No Phase 0 - assembly only from start
    /phase-1/
      /tier-1/
        /lesson-001/
          example-1.asm
          example-1.nes
```

### Website Repository

```
/website/
  /src/pages/
    /commodore-64/
      /phase-0/       # BASIC lessons (optional, deprioritized)
      /phase-1/
        /tier-1/
          lesson-001.mdx
          lesson-002.mdx
        /tier-2/
      /phase-2/
    /sinclair-zx-spectrum/
      /phase-0/
      /phase-1/
        /tier-1/
          lesson-001.mdx
    /commodore-amiga/
      /phase-0/
      /phase-1/
        /tier-1/
          lesson-001.mdx
    /nintendo-nes/
      # No Phase 0
      /phase-1/
        /tier-1/
          lesson-001.mdx
  /public/images/
    /commodore-64/
      /phase-1/
        /tier-1/
          /lesson-001/
            screenshot-1.png
            screenshot-2.png
          /lesson-002/
    /sinclair-zx-spectrum/
      /phase-1/
        /tier-1/
          /lesson-001/
            screenshot-1.png
    /commodore-amiga/
      /phase-1/
        /tier-1/
          /lesson-001/
            screenshot-1.png
    /nintendo-nes/
      /phase-1/
        /tier-1/
          /lesson-001/
            screenshot-1.png
```

### Documentation Repository

```
/docs/
  /plans/
    2025-11-14-curriculum-design.md  # This document
  /curriculum/
    commodore-64-curriculum.md
    sinclair-zx-spectrum-curriculum.md
    commodore-amiga-curriculum.md
    nintendo-nes-curriculum.md
  /commodore-64/
    /phase-1/
      tier-1-spec.md
      tier-2-spec.md
      /tier-1/
        lesson-001-spec.md
        lesson-002-spec.md
      /tier-2/
  /sinclair-zx-spectrum/
    /phase-1/
      tier-1-spec.md
  /commodore-amiga/
    /phase-1/
      tier-1-spec.md
  /nintendo-nes/
    /phase-1/
      tier-1-spec.md
  /standards/
    code-standards.md
    editorial-standards.md
    validation-checklist.md
  /tooling/
    validation-scripts.md
    emulator-setup.md
```

## Tooling & Technical Infrastructure

### Commodore 64 Toolchain

**BASIC (Phase 0 - Deprioritized):**
- **Tokenizer:** petcat (from VICE)
- **Validation:** Multi-stage
  1. Tokenization: `petcat -w2 -o output.prg -- input.bas`
  2. Roundtrip verification: `petcat -text temp.prg > roundtrip.bas` → Compare
  3. Syntax validator: Research needed when building Phase 0 content
  4. Execution: `x64sc -autostart file.prg -limitcycles 20000000 -VICIIdsize -exitscreenshot path.png -sound`
  5. Screenshot analysis: AI Read tool checks for error messages
- **Reserved variable check:** `grep -iE '\<(st|ti|ti\$)\>' file.bas`

**Assembly (Phases 1-8):**
- **Assembler:** ACME or ca65
- **Validation:** Compile → Load in emulator → Execute → Capture
- **Output formats:** .prg files
- **Additional checks:** Memory range validation, no system corruption

### Sinclair ZX Spectrum Toolchain

**BASIC (Phase 0 - Deprioritized):**
- **Tool:** zmakebas or bas2tap
- **Output format:** .tap files
- **Emulator:** FUSE (Free Unix Spectrum Emulator)
- **Validation:** Compile → Load → Execute → Capture

**Assembly (Phases 1-8):**
- **Assembler:** sjasmplus or pasmo
- **Output format:** .tap or .z80 files
- **Emulator:** FUSE
- **Screenshot capture:** Manual or automated via FUSE scripting
- **Models covered:** 48K, 128K, +2, +3

### Commodore Amiga Toolchain

**AMOS BASIC (Phase 0 - Deprioritized):**
- **Tool:** AMOS Professional (in emulator)
- **Emulator:** FS-UAE
- **Output format:** .adf (disk images)
- **Validation:** Load in emulator → Execute → Capture

**68000 Assembly (Phases 1-8):**
- **Assembler:** vasm (Volker Barthelmann's assembler)
- **Syntax:** `vasmm68k_mot -Fhunkexe -o output input.asm`
- **Emulator:** FS-UAE
- **Models covered:** A500, A1200 (OCS/ECS/AGA chipsets)
- **Kickstart versions:** 1.3, 2.0, 3.1

### Nintendo NES Toolchain

**6502 Assembly (Phases 1-8):**
- **Assembler:** ca65 (from cc65 suite)
- **Linker:** ld65
- **Output format:** .nes files
- **Emulator:** FCEUX or Mesen
- **Screenshot capture:** Emulator screenshot function
- **Mapper validation:** Verify correct mapper configuration in iNES header

### Docker-Based Build Environment

**Container Strategy:**
```yaml
services:
  workspace:
    image: retro-dev-env:latest
    volumes:
      - ./code-samples:/workspace/code-samples
      - ./build-output:/workspace/output
    environment:
      - PLATFORM=commodore-64
```

**Per-Platform Containers:**
- Each platform has toolchain pre-installed
- Consistent build environment across development machines
- Version-controlled Dockerfiles ensure reproducibility

### Automated Validation Pipeline

**Three-Stage Validation:**

**Stage 1: Compilation**
- Runs platform-specific compiler/assembler
- Captures compilation errors
- Verifies output files generated
- Exit code 0 = success, otherwise fail

**Stage 2: Execution**
- Loads compiled program in emulator
- Runs for specified cycles/time
- Captures screenshot at completion
- Verifies emulator didn't crash

**Stage 3: Screenshot Verification**
- AI uses Read tool to examine screenshot
- Describes visible content
- Checks for error messages (regex patterns per platform)
- Checks for blank screens (image analysis)
- Confirms expected output visible

**Validation Report Example:**
```
✓ Compilation successful
✓ Execution completed (2M cycles)
✓ Screenshot captured: screenshot-1.png
✓ Visual verification: Green platforms visible, red sprite at position (120,80), score display "000000"
✗ Error detected: "?SYNTAX ERROR IN 150" visible in screenshot
→ FAILED - Fix required
```

### British English Validation

**Automated Grep Pattern:**
```bash
# Check for American spellings (excluding code blocks)
grep -nE '(color|flavor|honor|neighbor|center|optimize|ize\b)' \
  --exclude-dir=code-samples \
  lesson.mdx
```

**Exceptions:**
- Code samples use platform-specific spelling (C64 BASIC has "COLOR" command)
- Technical terms: "program" (not "programme"), "disk" (not "disc" for floppy)

### Screenshot Management

**Capture Standards:**
- Native resolution per platform (320x200 for C64, 256x192 for Spectrum, etc.)
- PNG format for web delivery
- Filename convention: `screenshot-{number}.png`
- Organized by lesson in `/public/images/{platform}/phase-{n}/tier-{n}/lesson-{nnn}/`

**Storage Considerations:**
- With potentially thousands of lessons, screenshot storage grows significantly
- Git LFS for large binary files, or CDN hosting
- Optimization: PNG compression without quality loss

### Repository Management

**Git Structure:**
- `/code-samples` - Separate git repository
- `/website` - Separate git repository
- `/docs` - Part of main project repository or separate
- Allows different update cadences

**Version Control:**
- All lesson content versioned
- Code samples tagged per release
- Curriculum documents tracked for evolution
- Automated validation scripts versioned

## Development Strategy & Timeline

### Initial Development Focus

**Phase 0 Strategy:**
- Deprioritized for initial launch
- Optional beginner on-ramp, not required for experienced learners
- Can be added later after Assembly tracks prove successful
- Platforms: commodore-64 (BASIC), sinclair-zx-spectrum (BASIC), commodore-amiga (AMOS)
- Note: nintendo-nes has no Phase 0 (assembly-only from start)

**Phase 1-8 Priority:**
- Primary focus: Assembly tracks
- Start with Phase 1 across all four core platforms in parallel
- Discover cross-platform patterns early
- Build validation tooling alongside content

### Parallel Platform Development

**Approach:**
1. **Phase 1 Tier 1** - Build across all 4 platforms simultaneously
2. **Evaluate** - Validate tooling, refine workflow, identify issues
3. **Phase 1 Tier 2** - Apply learnings, build next tier
4. **Iterate** - Continue through Phase 1 completion
5. **Expand** - Move to Phase 2 across platforms, or complete one platform first based on learnings

**Benefits:**
- Surface platform differences early
- Validate curriculum structure works universally
- Build reusable patterns and tooling
- Maintain momentum across multiple platforms

**Risks:**
- Slower progress on any single platform
- Context-switching overhead
- May discover need to restructure after starting

**Mitigation:**
- Strong specifications prevent rework
- Automated validation catches issues early
- AI assistance handles mechanical execution
- Regular review points to course-correct

### Delivery Milestones

**Milestone 1: Phase 1, Tier 1 Complete**
- All 4 platforms have working Tier 1 (foundation lessons)
- Validation tooling proven
- Workflow established
- First playable results for learners

**Milestone 2: Phase 1 Complete**
- All 4 platforms have complete Phase 1 (8-16 tiers each)
- 128-512 lessons per platform published
- Commercial-quality games from early era (1982-1985 equivalent)
- Public launch possible at this stage

**Milestone 3: Phase 1-2 Complete**
- Two complete phases per platform
- Demonstrates progression from foundation to intermediate
- Learners can build increasingly sophisticated games
- Platform expansion decisions made

**Long-term Vision:**
- Phases 1-8 across core 4 platforms (potentially years)
- Expand to additional platforms based on demand
- Phase 0 tracks added for beginner on-ramps
- Enhanced platforms (Spectrum Next, MEGA65) as separate tracks
- Community contributions and collaborators join

### Success Metrics

**Quality Indicators:**
- Validation pass rate >95% on first attempt (after workflow matures)
- Code samples compile and execute correctly
- Screenshots show working games, no errors
- Manual review identifies minimal issues

**Learning Indicators:**
- Learners complete lessons independently
- Games produced are genuinely fun
- Progression feels achievable
- Commercial quality benchmarks met

**Operational Indicators:**
- Lesson creation time decreases as patterns emerge
- AI-assistance improves with refined specifications
- Repository structure scales cleanly
- Documentation stays current

## Immediate Next Steps

### Priority 1: Foundation Documents

1. **Create curriculum outlines** for all 4 core platforms
   - `docs/curriculum/commodore-64-curriculum.md`
   - `docs/curriculum/sinclair-zx-spectrum-curriculum.md`
   - `docs/curriculum/commodore-amiga-curriculum.md`
   - `docs/curriculum/nintendo-nes-curriculum.md`

2. **Define content standards** in detail
   - `docs/standards/code-standards.md`
   - `docs/standards/editorial-standards.md`
   - `docs/standards/validation-checklist.md`

3. **Document tooling setup**
   - `docs/tooling/validation-scripts.md`
   - `docs/tooling/emulator-setup.md`
   - `docs/tooling/docker-environments.md`

### Priority 2: Technical Setup

1. **Set up Docker environments** for each platform
2. **Create validation scripts** for automated checking
3. **Test toolchain** for each platform (compile, execute, screenshot)
4. **Verify emulator automation** works correctly

### Priority 3: Phase 1 Tier 1 Specification

1. **Define Phase 1 Tier 1** for all 4 platforms
2. **Write tier specifications** with detailed objectives
3. **Break down into lesson specifications** (16-32 lessons per tier)
4. **Prepare for AI-assisted content creation**

### Priority 4: Pilot Content Creation

1. **Create first lesson** on one platform (e.g., commodore-64)
2. **Run through complete validation workflow**
3. **Identify workflow issues** and refine process
4. **Document lessons learned**
5. **Apply to remaining platforms**

## Design Decisions Summary

### Confirmed Decisions

- ✅ Phases 0-8 structure (Phase 0 = gateway language, Phases 1-8 = assembly)
- ✅ Phase 0 deprioritized; assembly (Phases 1-8) is primary focus
- ✅ 8-16 tiers per phase, 16-32 lessons per tier
- ✅ Parallel Phase 1 development across 4 core platforms
- ✅ Commercial quality benchmarks mapped to historical eras
- ✅ Full system slug naming convention (`manufacturer-system`)
- ✅ Modern techniques integrated into phases based on complexity
- ✅ Enhanced systems (Spectrum Next, MEGA65) as separate platform tracks
- ✅ Comprehensive validation (compilation + execution + screenshot verification)
- ✅ British English throughout with documented exceptions
- ✅ AI-assisted content creation with human review
- ✅ Top-down planning (curriculum → tier → lesson specifications)

### Deferred Decisions

- ⏸️ C64 BASIC syntax validator tool (research when building Phase 0)
- ⏸️ Exact Docker container configuration (define during technical setup)
- ⏸️ Git LFS vs CDN for screenshot hosting (decide based on scale)
- ⏸️ Specific lesson specification template format (refine during pilot)
- ⏸️ Platform expansion priority beyond core 4 (decide after Phase 1 complete)

## Conclusion

This design establishes a comprehensive, scalable curriculum for teaching retro game development across multiple vintage platforms. The focus on commercial-quality output, verified accuracy, rigorous validation, and self-directed learning positions this as a serious educational platform for aspiring retro game developers.

The parallel development strategy across four core platforms, combined with AI-assisted content creation and automated validation, provides a realistic path to creating thousands of high-quality lessons over time while maintaining consistency and educational value.

Success depends on:
- Rigorous adherence to validation standards
- Strong specifications guiding AI content creation
- Regular human review ensuring pedagogical quality
- Incremental delivery with frequent evaluation points
- Community engagement and learner feedback

The foundation is now established. Implementation begins with creating detailed curriculum documents, setting up technical infrastructure, and producing pilot content to validate the workflow.
