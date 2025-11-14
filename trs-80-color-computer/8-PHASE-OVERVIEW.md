# TRS-80 Color Computer Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** CoCo 1/2 (6809) → CoCo 3 introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Extended Color BASIC
**CPU Note:** **6809 - sophisticated 8-bit architecture** (different from 6502/Z80)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare CoCo 1/2 vs CoCo 3 implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Stack operations are stack operations" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master CoCo 1/2 (6809, VDG graphics)
- Phase 3: **CoCo 3 introduced** - GIME chip, 128KB RAM, enhanced graphics, revisit games
- Phase 4-6: Advanced techniques, pushing CoCo 3 limits
- Phase 7: **Maximum CoCo 3** - all features, modern expansions
- Phase 8: Modern CoCo development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** CoCo 1/2 (6809 @ 0.89MHz, VDG graphics)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- **6809 instruction set fundamentals** (new CPU architecture)
- **Extended Color BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- VDG (Video Display Generator) basics
- Semigraphics modes (SG4, SG6, SG8, SG12, SG24)
- PMODE graphics (256×192×2, 128×192×4)
- Software sprite rendering
- Joystick input (via PIA chip)
- Sound (1-bit via 6-bit DAC)
- Interrupt timing (60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use Extended Color BASIC loader:
```basic
10 CLEAR 200,&H3FFF
20 LOADM"GAME"
30 EXEC
```
Or inline assembly via BASIC. Professional presentation: RUN from cassette/disk, game starts automatically.

**Deliverables:** 16 complete, playable CoCo 1/2 games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** CoCo 1/2 (6809, VDG)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 6809 code (two accumulators, index registers)
- Advanced VDG programming (PMODE graphics optimization)
- Semigraphics creative techniques
- Software sprite optimization
- Sound synthesis techniques (DAC)
- Advanced collision detection
- Multi-screen game structures
- Cartridge ROM games (optional)

**Deliverables:** 16 games with commercial-quality CoCo 1/2 features

---

### Phase 3: Enhanced Graphics & Memory (CoCo 3)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **CoCo 3 introduced** - GIME chip, 128KB RAM, enhanced graphics
**Complexity:** Direct CoCo 1/2→CoCo 3 comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with CoCo 3, 3 new showcasing GIME

**Key Learning:**
- **GIME chip programming** (Graphics Interrupt Memory Enhancement)
- **Enhanced graphics modes:**
  - 320×192×16 colors (from 64 palette)
  - 640×192×4 colors
  - 320×225×16 colors (composite)
  - 640×225×4 colors (composite)
- **128KB RAM** (banked memory)
- **Direct comparison:** "Here's your VDG Snake. Now enhance it with GIME graphics"
- Faster CPU (1.78MHz vs 0.89MHz)
- Hardware scrolling registers
- Professional CoCo 1/2 optimization (for games staying on earlier models)

**Deliverables:** 8 games - 5 CoCo 3 versions of earlier games, 3 new showcasing GIME

**Games Revisited with CoCo 3:**
1. Snake III (CoCo 3) - GIME graphics, 320×192×16 colors
2. Shooter III (CoCo 3) - enhanced modes, faster CPU
3. Platformer III (CoCo 3) - hardware scrolling, better colors
4. Breakout III (CoCo 3) - high resolution, 128KB RAM
5. One other from Phase 1-2

**New CoCo 3 Games:**
6. Action RPG I (showcasing GIME + 128KB)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** CoCo 3 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced GIME programming (all modes)
- Memory banking (128KB efficiently)
- Hardware scrolling optimization
- Advanced sound synthesis
- Disk I/O (OS-9 or RSDOS)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced CoCo 3 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** CoCo 3 mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced sound programming
- OS-9 multitasking (optional advanced topic)
- Disk-based save/load systems

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** CoCo 3 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 6809 optimization
- Fast disk loaders (custom routines)
- 512KB RAM expansions
- Professional CoCo 3 development

**Deliverables:** 4 games pushing absolute limits of CoCo 3

---

### Phase 7: Maximum CoCo
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** CoCo 3 (maximum capabilities) + modern expansions
**Complexity:** Large-scale games using all features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- Maximum RAM (512KB-2MB expansions)
- Hard drive support
- OS-9 Level II advanced features
- Modern sound expansions (PSG chips, etc.)
- Large game worlds
- Advanced GIME techniques
- Networking (DriveWire, CoCoSDC)
- Commercial CoCo development

**Deliverables:** 2 commercial-scale CoCo 3 games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern CoCo development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern CoCo development workflow
- Emulator debugging (VCC, MAME)
- CoCoSDC (SD card interface)
- Modern expansions
- Pushing CoCo 3 absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **6809 mastery:** Understanding sophisticated 8-bit architecture

**Deliverables:** 2 portfolio-ready commercial-quality CoCo games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 6809 Programming**
- P1: Basic instructions (LDA, STA, ADD, etc.)
- P2: Advanced features (two accumulators, index registers)
- P3: CoCo 3 optimization (faster CPU)
- P4: Complex 6809 techniques
- P5+: Extreme optimization
- **Note:** 6809 different from 6502/Z80 (more sophisticated)

**2. Graphics Programming**
- P1: VDG modes (semigraphics, PMODE)
- P2: Advanced VDG techniques
- P3: **GIME graphics (CoCo 3 - 320×192×16)**
- P4: All GIME modes
- P5+: Advanced graphics systems

**3. Sprite Rendering**
- P1: Software sprites (VDG)
- P2: Optimized sprites (6809 efficient)
- P3: GIME sprites (better modes, faster CPU)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Scrolling Systems**
- P1: Screen-aligned scrolling
- P2: Pixel scrolling (VDG)
- P3: **Hardware scrolling (CoCo 3 GIME)**
- P4: Complex scrolling
- P5+: Advanced scrolling

**5. Sound Programming**
- P1: 1-bit sound (DAC)
- P2: Sound synthesis techniques
- P3: Enhanced sound (CoCo 3)
- P4: Complex audio
- P5+: Modern sound expansions

**6. Memory Management**
- P1: Basic RAM (4KB-64KB depending on model)
- P2: Efficient data structures
- P3: **CoCo 3 banking (128KB)**
- P4: Complex banking
- P5+: Large RAM expansions (512KB-2MB)

**7. Collision Detection**
- P1: Bounding box collision
- P2: Pixel-perfect collision
- P3: GIME-optimized collision
- P5+: Multi-layer collision

**8. Disk I/O**
- P3: RSDOS/OS-9 file operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage (CoCoSDC)

---

## Hardware Progression

### CoCo 1/2 (Phases 1-2)
**Platform:** TRS-80 Color Computer 1/2 (1980-1986)
**Characteristics:**
- **6809 CPU @ 0.89MHz** (sophisticated 8-bit architecture)
- 4KB-64KB RAM (typically 16KB-64KB)
- **VDG chip** (Video Display Generator - MC6847)
- Semigraphics: SG4, SG6 (64×48), SG8, SG12, SG24
- PMODE: 256×192×2 colors, 128×192×4 colors
- Sound: 6-bit DAC (1-bit typically used)
- Cassette or disk storage
- 60Hz NTSC

**Focus:** Master 6809 and VDG
- **6809 architecture** (different from 6502/Z80)
- Two 8-bit accumulators (A, B) that combine to D (16-bit)
- Two index registers (X, Y)
- Two stack pointers (S, U)
- Sophisticated addressing modes
- VDG graphics programming
- Software sprite rendering

**CPU Significance:**
- 6809 considered one of best 8-bit CPUs
- More orthogonal than 6502
- Influenced later processors

### CoCo 3 (Phase 3+)
**Platform:** TRS-80 Color Computer 3 (1986)
**Introduced Phase 3**
**Enhanced Features:**
- **6809E CPU @ 1.78MHz** (2× faster)
- **GIME chip** (Graphics Interrupt Memory Enhancement)
- **Enhanced graphics modes:**
  - 320×192×16 colors (from 64-color palette)
  - 640×192×4 colors
  - 320×225×16 colors (composite)
  - 640×225×4 colors (composite)
- **128KB RAM standard** (banked)
- **Hardware scrolling** registers
- **RGB output** (crisp graphics)
- **Direct comparison:** VDG vs GIME graphics

**Focus:** Leverage GIME enhancements
- Enhanced graphics modes
- 16 colors on-screen
- Faster CPU (2×)
- Hardware scrolling
- 128KB banked RAM

### Modern CoCo (Phase 7-8)
**Modern enhancements:**
- CoCoSDC (SD card interface)
- 512KB-2MB RAM expansions
- Hard drive support
- Modern sound expansions
- DriveWire (PC connection)
- Modern development tools

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (CoCo 1/2 VDG)** (16 lessons)
- Basic grid movement (6809 fundamentals)
- Semigraphics or PMODE graphics
- Software sprites
- DAC sound
- 16KB-64KB RAM

**Phase 2: Snake II (CoCo 1/2 optimized)** (32 lessons)
- Optimized 6809 code
- Better VDG graphics
- Advanced sound
- Multi-screen levels
- Optimized VDG

**Phase 3: Snake III (CoCo 3 GIME)** (64 lessons - REVISITED WITH COCO 3)
- **GIME graphics** (320×192×16 colors)
- **Hardware scrolling**
- **Faster CPU** (1.78MHz)
- **128KB RAM**
- **Direct comparison:** "Here's your VDG Snake. Now enhance it with GIME"

**Phase 4: Snake IV (Advanced CoCo 3)** (64 lessons)
- Advanced GIME modes
- Memory banking
- Complex graphics
- Disk-based levels

**Phase 6: Snake V (CoCo 3 limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme 6809 optimization
- Commercial-quality
- Pushing CoCo 3 limits

Students see evolution: VDG basics → VDG optimized → **GIME enhanced** → Advanced → Professional

---

## Key Differences from Other Platforms

**CoCo Advantages:**
- **6809 CPU** (sophisticated 8-bit, different from 6502/Z80)
- CoCo 3 GIME (excellent graphics for 8-bit)
- OS-9 (real multitasking OS, advanced for home computers)
- Strong US educational presence
- Active hobbyist community

**CoCo Considerations:**
- 6809 assembly different from common 6502/Z80
- VDG graphics limited (CoCo 1/2)
- Less common than C64/Spectrum internationally
- Primarily US/Canada market

**6809 vs 6502:**
- More registers (6809 has A, B, D, X, Y, S, U vs 6502's A, X, Y)
- More sophisticated addressing modes
- Two stack pointers (U and S)
- More orthogonal instruction set
- Considered more elegant architecture

**Similar To:**
- Dragon 32/64 (licensed CoCo design)
- Thomson MO5/TO7 (also 6809)

**Same Pattern Library Concepts:**
- Collision detection algorithms
- AI pathfinding
- Physics systems
- Game design patterns
- All transferable skills

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (VDG and GIME where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6809 CoCo games from scratch
- Understands 6809 architecture (different from 6502/Z80)
- Understands VDG graphics
- Has 16 portfolio CoCo 1/2 games

**Phase 3 Complete:**
- Student masters CoCo 3 GIME
- Can compare/contrast VDG vs GIME implementations
- Has both CoCo 1/2 and CoCo 3 versions of key games
- **Unique skill:** 6809 assembly programming

**Phase 8 Complete:**
- Student has 60 portfolio games across all CoCo variants
- Masters 6809 architecture
- Masters VDG and GIME graphics
- Can create commercial-release quality games
- Ready for professional CoCo development
- **6809 expertise** transfers to Dragon, Thomson platforms

---

## Resources Required

**Development Tools:**
- Assembler: LWTOOLS, EDTASM, modern cross-assemblers
- Emulator: VCC (best), MAME (accurate)
- Graphics: CoCo graphics editors
- Audio: Sound tools
- Utilities: Disk image tools

**Reference Materials:**
- **6809 instruction set** (different from 6502/Z80)
- VDG (MC6847) reference
- GIME chip reference
- CoCo 3 Technical Reference
- Extended Color BASIC reference
- OS-9 documentation

**Testing:**
- Emulators (development)
- Real CoCo hardware (verification)
- CoCo 3 (Phase 3+)
- Modern expansions (CoCoSDC, etc.)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - CoCo 3 (GIME) introduced Phase 3
**Note:** CoCo has Phase 0 (Extended Color BASIC)
**CPU Note:** **6809 - sophisticated 8-bit architecture, different from 6502/Z80**
**Next Steps:** Create CoCo 8-PHASE-GAME-PROGRESSION.md with specific game mapping
