# Acorn Archimedes Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Archimedes (ARM2/3) → Risc PC introduced Phase 3 → StrongARM → Modern (Raspberry Pi)
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - BBC BASIC V (with ARM assembler)
**Historic Note:** First commercial ARM computer (1987) - ARM now powers most mobile devices

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare Archimedes vs Risc PC implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "ARM addressing modes are ARM addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Archimedes (ARM2/ARM3 @ 8-25MHz)
- Phase 3: **Risc PC introduced** - ARM610/710, modular design, revisit games
- Phase 4-6: Advanced techniques, pushing Risc PC limits
- Phase 7: **StrongARM** - 200MHz+, maximum performance
- Phase 8: Modern ARM (Raspberry Pi with RISC OS)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Acorn Archimedes (ARM2 @ 8MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- ARM instruction set fundamentals (32-bit RISC architecture)
- **BBC BASIC V inline ARM assembly - Lesson 2-3, mandatory from Lesson 3**
- RISC OS basics (Wimp, modules, SWI calls)
- Screen modes (multiple resolutions/colors)
- VIDC basics (Video and Sound Controller)
- Software sprite rendering
- Keyboard/mouse input (via RISC OS)
- Sound system (8-channel stereo via VIDC)
- VSync timing (50Hz PAL / 60Hz - configurable)

**Autoload Requirement:**
All games from Lesson 3 onwards must use BBC BASIC V with inline ARM:
```basic
10 MODE 15
20 DIM CODE% 1000
30 FOR pass% = 0 TO 2 STEP 2:P%=CODE%:[OPT pass%
40 \ ARM assembly code here
50 ]:NEXT
60 CALL CODE%
```
Or standalone RISC OS application (double-click to run).
Professional presentation: RUN from BASIC or launch from desktop, game starts automatically.

**Deliverables:** 16 complete, playable Archimedes games with professional presentation

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Archimedes (ARM2/ARM3 @ 8-25MHz)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized ARM code (conditional execution, barrel shifter)
- Software sprite optimization (ARM is fast - creative techniques)
- Advanced screen modes (256 colors, higher resolutions)
- VIDC sound programming (8-channel stereo)
- Advanced RISC OS techniques (Wimp, custom modules)
- Multi-screen game structures
- Advanced collision detection
- Memory management (efficient use of 1-4MB RAM)

**Deliverables:** 16 games with commercial-quality Archimedes features

---

### Phase 3: Modular Architecture (Risc PC)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Acorn Risc PC introduced** - ARM610/710, modular design
**Complexity:** Direct Archimedes→Risc PC comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with Risc PC, 3 new showcasing features

**Key Learning:**
- **ARM610/ARM710 CPU** (faster, with cache)
- **Direct comparison:** "Here's your Archimedes Snake. Now optimize it for Risc PC"
- Modular architecture (upgrade slots, multiple processors)
- Enhanced VIDC (VIDC20 - better modes)
- Improved screen modes (24-bit color)
- Cache-aware programming
- CD-ROM support
- Professional Archimedes optimization (for games staying on Archimedes)

**Deliverables:** 8 games - 5 Risc PC versions of earlier games, 3 new showcasing Risc PC

**Games Revisited with Risc PC:**
1. Snake III (Risc PC) - ARM610 optimization, enhanced graphics
2. Shooter III (Risc PC) - cache-aware code, better modes
3. Platformer III (Risc PC) - faster CPU, improved visuals
4. Breakout III (Risc PC) - enhanced modes, CD audio
5. One other from Phase 1-2

**New Risc PC Games:**
6. Action RPG I (showcasing ARM610 + CD-ROM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Risc PC (ARM610/710, pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced ARM programming (coprocessor instructions)
- Cache optimization techniques
- Advanced VIDC20 programming
- CD-ROM game structures
- Disk I/O optimization (RISC OS filing systems)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced Risc PC techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Risc PC mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced VIDC sound composition
- CD-ROM based games (multi-disc)
- Save/load systems

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Risc PC (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 64+ simultaneous sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme ARM optimization
- Fast CD loaders
- Large-scale Risc PC games
- Professional RISC OS development

**Deliverables:** 4 games pushing absolute limits of Risc PC

---

### Phase 7: Maximum Performance (StrongARM)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** StrongARM Risc PC (200MHz+)
**Complexity:** Large-scale games with maximum performance
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **StrongARM CPU** (SA-110 @ 200MHz+, very fast)
- **32KB cache** (optimization critical)
- StrongARM-specific optimization
- Maximum RISC OS capabilities
- Large RAM configurations (128MB+)
- Complex 3D graphics (software rendering)
- Large game worlds
- Commercial StrongARM development

**Deliverables:** 2 commercial-scale StrongARM games

---

### Phase 8: Pinnacle (Modern ARM)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern ARM (Raspberry Pi with RISC OS)
**Complexity:** Modern ARM platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- **Modern ARM CPUs** (Raspberry Pi ARM11/Cortex)
- **RISC OS on modern hardware** (spiritual successor)
- Modern development workflow
- Emulator debugging (RPCEmu, ArcEm)
- Pushing ARM limits
- Modern peripherals (HDMI, USB)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** From first commercial ARM (1987) to modern ARM devices

**Deliverables:** 2 portfolio-ready commercial-quality ARM games showcasing everything learned

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. ARM Instruction Set**
- P1: Basic ARM instructions (MOV, ADD, SUB, etc.)
- P2: Conditional execution, barrel shifter
- P3: Cache-aware programming (ARM610/710)
- P4: Coprocessor instructions
- P5+: Extreme ARM optimization
- P7: StrongARM-specific optimization

**2. Screen Mode Management**
- P1: Basic modes (256 colors, various resolutions)
- P2: Mode switching, advanced modes
- P3: Risc PC VIDC20 modes (24-bit color)
- P4: Complex mode techniques
- P5+: Advanced graphics systems

**3. Sprite Rendering**
- P1: Software sprites (ARM is fast)
- P2: Optimized sprites (barrel shifter tricks)
- P3: Cache-optimized sprites (Risc PC)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (64+ sprites)

**4. Scrolling Systems**
- P1: Basic scrolling
- P2: Smooth pixel scrolling
- P3: Cache-aware scrolling (Risc PC)
- P4: Complex scrolling (parallax)
- P5+: Advanced scrolling techniques

**5. Sound Programming**
- P1: VIDC sound basics (8-channel stereo)
- P2: Advanced VIDC programming
- P3: Enhanced audio on Risc PC
- P4: Complex audio systems
- P5+: Professional audio (tracker format)

**6. Collision Detection**
- P1: Bounding box collision
- P2: Pixel-perfect collision
- P3: Cache-optimized collision
- P5+: Multi-layer collision

**7. Memory Management**
- P1: Basic RAM usage (1-4MB)
- P2: Efficient data structures
- P3: Risc PC expanded RAM
- P4: Large data management
- P5+: Complex memory systems
- P7: StrongARM large RAM (128MB+)

**8. RISC OS Integration**
- P1: Basic SWI calls, Wimp
- P2: Advanced RISC OS techniques
- P3: Modules, custom software
- P4: Complex RISC OS programming
- P5+: Professional RISC OS development

---

## Hardware Progression

### Acorn Archimedes (Phases 1-2)
**Platform:** Archimedes (1987-1994)
**Characteristics:**
- **ARM2 CPU @ 8MHz** (first commercial ARM!)
- **ARM3 CPU @ 25MHz** (later models, with 4KB cache)
- 512KB-16MB RAM (typically 1-4MB)
- VIDC (Video and Sound Controller)
- Multiple screen modes (up to 256 colors)
- 8-channel stereo sound (VIDC)
- RISC OS (advanced OS for its time)
- No hardware sprites (fast CPU compensates)
- Mouse standard
- 50Hz PAL (configurable)

**Focus:** Master ARM fundamentals
- ARM instruction set (32-bit RISC)
- Conditional execution
- Barrel shifter
- VIDC programming
- RISC OS integration
- Fast CPU enables creative solutions

**Historic Significance:**
- First commercial ARM computer
- ARM architecture now dominates mobile/embedded
- Revolutionary RISC design

### Acorn Risc PC (Phase 3+)
**Platform:** Risc PC (1994-1998)
**Introduced Phase 3**
**Enhanced Features:**
- **ARM610 @ 30MHz** or **ARM710 @ 40MHz**
- **Modular architecture** (upgrade slots)
- **VIDC20** (enhanced video, 24-bit color)
- Better screen modes (16.8M colors)
- 4MB-256MB RAM (typically 8-32MB)
- CD-ROM drive standard
- Faster I/O
- **Direct comparison:** Archimedes vs Risc PC

**Focus:** Leverage Risc PC enhancements
- Cache optimization (ARM610/710 have cache)
- Enhanced VIDC20 modes
- CD-ROM game structures
- Faster performance

### StrongARM (Phase 7)
**Platform:** StrongARM Risc PC (1996-1998)
**Enhanced Features:**
- **StrongARM SA-110 @ 200MHz+**
- **32KB cache** (16KB instruction + 16KB data)
- Dramatically faster than ARM710
- Up to 256MB RAM
- Same VIDC20/RISC OS

**Focus:** Maximum performance
- StrongARM optimization
- Cache-critical programming
- Large RAM games
- Extreme performance

### Modern ARM (Phase 8)
**Platform:** Raspberry Pi with RISC OS
**Modern Features:**
- ARM11/Cortex CPUs (GHz speeds)
- RISC OS Pi (RISC OS on Raspberry Pi)
- Modern peripherals (HDMI, USB, etc.)
- Emulators (RPCEmu, ArcEm)
- **Historical connection:** ARM journey from Archimedes to modern devices

**Focus:** Modern workflow
- Commercial-quality games
- Modern ARM development
- Portfolio showcase
- Historical perspective on ARM evolution

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Archimedes ARM2)** (16 lessons)
- Basic grid movement (ARM fundamentals)
- Mode 15 (256 colors)
- Software sprites (fast ARM)
- VIDC sound
- 1MB RAM

**Phase 2: Snake II (Archimedes optimized)** (32 lessons)
- Conditional execution optimization
- Barrel shifter tricks
- Advanced VIDC programming
- Multi-screen levels
- Optimized ARM2/ARM3

**Phase 3: Snake III (Risc PC)** (64 lessons - REVISITED WITH RISC PC)
- **Cache-aware programming** (ARM610/710)
- **Enhanced VIDC20 modes**
- **Faster CPU optimization**
- **Direct comparison:** "Here's your Archimedes Snake. Now optimize it for Risc PC cache"

**Phase 4: Snake IV (Advanced Risc PC)** (64 lessons)
- Advanced cache techniques
- CD-ROM integration
- Complex game modes
- Disk-based levels

**Phase 6: Snake V (Risc PC limits)** (128 lessons)
- 64+ simultaneous AI snakes
- Extreme ARM optimization
- Commercial-quality
- Pushing Risc PC limits

**Phase 7: Snake Ultimate (StrongARM)** (if applicable)
- StrongARM @ 200MHz
- 32KB cache optimization
- Maximum performance

Students see evolution: ARM2 basics → ARM3 optimized → **Risc PC cache-aware** → Advanced → StrongARM → Modern ARM

---

## Key Differences from Other Platforms

**Archimedes Advantages:**
- **ARM RISC architecture** (32-bit, very fast for its era)
- **First commercial ARM** (historic significance)
- Excellent BBC BASIC V (inline ARM assembler)
- RISC OS (advanced operating system)
- Fast even by modern retro standards
- 8-channel stereo sound (VIDC)
- Educational legacy (UK schools, BBC Micro successor)

**Archimedes Considerations:**
- Less common than C64/Spectrum (primarily UK market)
- No hardware sprites (fast CPU compensates)
- Expensive when new (premium machine)
- Smaller game library than other platforms

**Similar To:**
- BBC Micro (predecessor, BBC BASIC lineage)
- Atari ST/Amiga (contemporary 16/32-bit machines)

**Unique Features:**
- **ARM architecture** (now powers most mobile devices)
- RISC OS (still maintained today)
- BBC BASIC V (best BASIC for ARM programming)
- Historical significance (first commercial ARM)

**Same Pattern Library Concepts:**
- Collision detection algorithms
- AI pathfinding
- Physics systems
- Game design patterns
- All transferable skills

**Modern Relevance:**
- ARM now dominates smartphones, tablets, embedded systems
- Apple Silicon (M1/M2/M3) is ARM-based
- Learning ARM on Archimedes = understanding foundation of modern computing

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (Archimedes and Risc PC where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete ARM games from scratch
- Understands ARM instruction set, VIDC, RISC OS
- Has 16 portfolio Archimedes games

**Phase 3 Complete:**
- Student masters cache-aware ARM programming
- Can compare/contrast Archimedes vs Risc PC implementations
- Has both Archimedes and Risc PC versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all ARM variants
- Masters Archimedes, Risc PC, StrongARM, and modern ARM
- Understands ARM evolution from 1987 to present
- Can create commercial-release quality games
- Ready for professional ARM development
- **Unique outcome:** Understanding of ARM architecture underlying most modern devices

---

## Resources Required

**Development Tools:**
- Assembler: BBC BASIC V (inline), ObjAsm
- Emulator: RPCEmu (best), ArcEm, Arculator
- Graphics: !Paint, various RISC OS tools
- Audio: Tracker tools for RISC OS
- Utilities: SparkFS, disc image tools

**Reference Materials:**
- ARM Architecture Reference Manual
- RISC OS Programmer's Reference Manual
- VIDC reference
- BBC BASIC V guide
- Archimedes Technical Reference

**Testing:**
- Emulators (development)
- Real Archimedes/Risc PC hardware (verification)
- Raspberry Pi with RISC OS (modern testing)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Risc PC introduced Phase 3
**Note:** Acorn Archimedes has Phase 0 (BBC BASIC V - enhanced with ARM assembler)
**Historic Significance:** First commercial ARM computer (1987) - ARM now powers most mobile devices worldwide
**Next Steps:** Create Archimedes 8-PHASE-GAME-PROGRESSION.md with specific game mapping
