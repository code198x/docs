# Commodore 128 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** C128 base → C128D introduced Phase 3 (dual-CPU mastery) → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - BASIC 7.0
**Historical Note:** Sold 4 million units, **THREE operating modes** (C128, C64, CP/M), most advanced 8-bit Commodore

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare C128 mode vs dual-CPU (CP/M) implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Dual-CPU coordination is dual-CPU coordination" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master C128 mode (8502 @ 2MHz, 128KB RAM, VIC-IIe)
- Phase 3: **C128D + CP/M mode introduced** - Z80 programming, dual-CPU mastery, revisit games
- Phase 4-6: Advanced dual-CPU techniques, pushing limits
- Phase 7: **Maximum C128** - all three modes coordinated
- Phase 8: Modern C128 development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Commodore 128 base (C128 mode, 8502 @ 2MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- **8502 instruction set fundamentals** (6502-compatible, enhanced)
- **BASIC 7.0 loader - Lesson 2-3, mandatory from Lesson 3**
- VIC-IIe chip (enhanced VIC-II from C64)
- 128KB RAM (banks 0 and 1)
- 40×25 or 80×25 text modes
- Bitmap graphics modes (like C64 but enhanced)
- **8 hardware sprites** (like C64)
- **SID chip** (same as C64)
- MMU (Memory Management Unit - bank switching)
- Joystick/keyboard input
- Interrupt timing (60Hz NTSC / 50Hz PAL)
- **C64 compatibility mode** (full backward compatibility)

**Autoload Requirement:**
All games from Lesson 3 onwards must use BASIC 7.0 loader:
```basic
10 BANK 15
20 SYS 4864
```
Professional presentation: LOAD from disk, RUN, game starts automatically.

**Deliverables:** 16 complete, playable C128 games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** C128 base (C128 mode)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 8502 code (2MHz vs C64's 1MHz)
- MMU bank switching (128KB efficiently)
- VIC-IIe advanced features (80-column, enhanced modes)
- Sprite multiplexing (like C64 but faster)
- SID music programming
- Advanced collision detection
- Multi-screen game structures
- 1571 disk drive (fast serial)

**Deliverables:** 16 games with commercial-quality C128 features

---

### Phase 3: Dual-CPU Mastery (C128D + CP/M Mode)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **C128D + CP/M mode introduced** - Z80 programming, dual-CPU
**Complexity:** Direct single-CPU→dual-CPU comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with dual-CPU, 3 new showcasing Z80

**Key Learning:**
- **C128D** (1986, built-in 1571 disk drive, better design)
- **CP/M mode:** Z80 @ 4MHz (third operating mode!)
- **Z80 instruction set** (completely different from 8502)
- **Dual-CPU coordination:** 8502 (graphics/sound) + Z80 (logic/AI)
- **Direct comparison:** "Here's your 8502 Snake. Now add Z80 AI processing"
- CP/M operating system basics
- Switching between C128 mode and CP/M mode
- Using both CPUs simultaneously (advanced)
- Professional C128 mode optimization (for games staying single-CPU)

**Deliverables:** 8 games - 5 dual-CPU versions of earlier games, 3 new showcasing Z80

**Games Revisited with Dual-CPU:**
1. Snake III (Dual-CPU) - Z80 AI, 8502 graphics
2. Shooter III (Dual-CPU) - Z80 logic, 8502 rendering
3. Platformer III (Dual-CPU) - Z80 physics, 8502 display
4. Breakout III (Dual-CPU) - Z80 calculations, 8502 visuals
5. One other from Phase 1-2

**New Dual-CPU Games:**
6. Action RPG I (showcasing dual-CPU architecture)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** C128D (pushing dual-CPU limits)
**Complexity:** Advanced dual-CPU techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced 8502/Z80 coordination
- MMU advanced bank switching (all 128KB efficiently)
- Complex sprite systems (VIC-IIe all capabilities)
- Advanced SID programming
- Dual-CPU task distribution (optimal workload)
- Fast serial (1571 drive optimization)
- Isometric projection
- Turn-based strategy mechanics (Z80 AI shines)

**Deliverables:** 8 games showcasing advanced C128 dual-CPU techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** C128D mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture (dual-CPU)
- Quest systems and narrative (Z80 handles complex logic)
- Interconnected world design
- Advanced enemy AI (Z80 dedicated processing)
- Power-up progression systems
- Advanced SID music
- Disk-based save/load (1571 optimization)
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** C128D (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing dual-CPU at maximum efficiency
- 64+ simultaneous sprites (extreme multiplexing)
- Complex multi-character systems (Z80 AI for all)
- Real-time strategy mechanics (Z80 perfect for this)
- Commercial polish techniques
- Extreme 8502/Z80 optimization
- Fast disk loaders (1571)
- Pushing C128 absolute limits

**Deliverables:** 4 games pushing absolute limits of C128

---

### Phase 7: Three-Mode Mastery
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** C128 (all three operating modes coordinated)
**Complexity:** Large-scale games using all three modes
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **Three operating modes:**
  - C128 mode (8502 @ 2MHz, VIC-IIe, SID)
  - C64 mode (100% C64 compatibility)
  - CP/M mode (Z80 @ 4MHz)
- Mode switching techniques
- Hybrid games (use multiple modes)
- C64 mode for compatibility testing
- CP/M utilities
- Maximum C128 capabilities
- Commercial C128 development

**Deliverables:** 2 commercial-scale C128 games using all capabilities

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern C128 development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern C128 development workflow
- Emulator debugging (VICE)
- Modern C128 expansions (REU, etc.)
- Pushing C128 absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** Most advanced 8-bit Commodore, dual-CPU pioneer

**Deliverables:** 2 portfolio-ready commercial-quality C128 games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 8502 Programming**
- P1: Basic instructions (6502-compatible, faster)
- P2: Advanced 8502 techniques
- P3: **Z80 programming** (CP/M mode, dual-CPU)
- P4: Dual-CPU coordination optimization
- P5+: Extreme dual-CPU techniques

**2. Dual-CPU Architecture**
- P3: **8502 + Z80 coordination** (unique to C128)
- P4: Task distribution (graphics vs logic)
- P5: Complex dual-CPU systems
- P6: Maximum dual-CPU efficiency

**3. Graphics Programming**
- P1: VIC-IIe basics (like C64 but enhanced)
- P2: Advanced VIC-IIe (80-column, modes)
- P3: Dual-CPU graphics (8502 render, Z80 calculate)
- P4: All VIC-IIe capabilities
- P5+: Complex graphics systems

**4. Sprite Management**
- P1: 8 hardware sprites (like C64)
- P2: Sprite multiplexing
- P3: Dual-CPU sprites (Z80 manages, 8502 renders)
- P4: Extreme multiplexing (64+ sprites)
- P5+: Complex sprite systems

**5. Sound Programming**
- P1: SID basics (same as C64)
- P2: SID music
- P3: Dual-CPU audio (Z80 sequences, 8502 plays)
- P4: Advanced SID
- P5+: Professional audio

**6. Memory Management**
- P1: Basic 128KB (MMU banking)
- P2: Efficient MMU usage
- P3: Dual-CPU memory (8502 banks + Z80 space)
- P4: Complex banking
- P5+: Maximum 128KB efficiency

**7. AI & Logic**
- P3: **Z80 dedicated AI** (perfect for game logic)
- P4: Complex AI (Z80 @ 4MHz shines)
- P5: Advanced pathfinding (Z80)
- P6: Extreme AI systems

**8. Disk I/O**
- P2: 1571 drive basics (fast serial)
- P3: CP/M file systems
- P4: Advanced disk access
- P5: Disk-based games
- P6: Fast loaders

---

## Hardware Progression

### C128 Base (Phases 1-2)
**Platform:** Commodore 128 (1985)
**Characteristics:**
- **8502 CPU @ 2MHz** (6502-compatible, 2× faster than C64)
- **128KB RAM** (MMU bank switching)
- **VIC-IIe** (enhanced VIC-II from C64)
- **8 hardware sprites** (like C64)
- **SID chip** (same as C64)
- **Z80 @ 4MHz** (for CP/M mode, not used in C128 mode initially)
- 40×25 or 80×25 text
- Bitmap graphics
- 1571 disk drive (fast serial, 170KB per side)
- **Three operating modes:**
  - C128 mode (main mode)
  - C64 mode (100% compatible)
  - CP/M mode (Z80 business software)

**Focus:** Master C128 mode (8502)
- 8502 programming (faster than C64)
- 128KB MMU banking
- VIC-IIe graphics
- SID sound

**Historical Context:**
- Most advanced 8-bit Commodore
- Sold 4 million units (successful)
- Backward compatible with C64
- Business + gaming machine

### C128D (Phase 3+) + CP/M Mode
**Platform:** Commodore 128D (1986)
**Introduced Phase 3**
**Enhanced Features:**
- **Built-in 1571 disk drive**
- Better case design (metal)
- Detached keyboard
- **CP/M mode mastery:** Z80 @ 4MHz
- **Dual-CPU programming:** 8502 + Z80 coordination
- **Direct comparison:** Single-CPU vs dual-CPU games

**Focus:** Dual-CPU mastery
- Z80 programming (CP/M mode)
- Coordinating 8502 + Z80
- Task distribution (graphics vs logic)
- Professional dual-CPU architecture

### Modern C128 (Phase 7-8)
**Modern enhancements:**
- VICE emulator (excellent C128 support)
- REU compatibility (like C64)
- Modern assemblers
- Modern expansions

**Focus:** Modern workflow
- Commercial-quality games
- All three modes mastered
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (C128 mode)** (16 lessons)
- Basic grid movement (8502 fundamentals)
- VIC-IIe graphics
- Hardware sprites
- SID sound
- 128KB RAM (MMU)

**Phase 2: Snake II (C128 optimized)** (32 lessons)
- Optimized 8502 code (2MHz)
- Sprite multiplexing
- SID music
- MMU banking
- Optimized C128

**Phase 3: Snake III (Dual-CPU)** (64 lessons - REVISITED WITH DUAL-CPU)
- **Z80 AI processing** (snake logic, food spawning)
- **8502 graphics rendering** (VIC-IIe, sprites)
- **Dual-CPU coordination**
- **CP/M mode techniques**
- **Direct comparison:** "Here's your 8502 Snake. Now add Z80 AI processing - see the difference!"

**Phase 4: Snake IV (Advanced Dual-CPU)** (64 lessons)
- Complex Z80/8502 coordination
- Advanced AI (Z80)
- Advanced graphics (8502)
- Disk-based levels

**Phase 6: Snake V (C128 limits)** (128 lessons)
- Maximum dual-CPU efficiency
- 64+ sprites
- Extreme optimization
- Pushing C128 limits

Students see evolution: C128 mode basics → C128 optimized → **Dual-CPU mastery** → Advanced → Professional

---

## Key Differences from C64

**C128 vs C64:**
- **Faster CPU:** 8502 @ 2MHz (vs C64's 1MHz)
- **More RAM:** 128KB (vs C64's 64KB)
- **Enhanced VIC:** VIC-IIe with 80-column mode
- **Same SID chip**
- **Second CPU:** Z80 @ 4MHz (C64 has none)
- **Three modes:** C128, C64, CP/M (vs C64's one mode)
- **100% C64 compatible** (C64 mode)

**C128 Unique Features:**
- **Dual-CPU architecture** (8502 + Z80)
- CP/M mode (business software)
- MMU (sophisticated banking)
- 80-column text mode

**Learning Path:**
- C64 → C128 (natural progression)
- C128 teaches dual-CPU concepts
- 8502 skills = 6502 skills (compatible)
- **Unique skill:** Dual-CPU coordination

**Same Pattern Library Concepts:**
- 8502/6502 assembly (compatible)
- Z80 assembly (new for C128)
- Collision detection, AI, physics
- All transferable skills

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (C128 mode and dual-CPU where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 8502 C128 games from scratch
- Understands MMU banking (128KB)
- Has 16 portfolio C128 mode games

**Phase 3 Complete:**
- Student masters dual-CPU programming (8502 + Z80)
- Can compare/contrast single-CPU vs dual-CPU implementations
- Has both C128 mode and dual-CPU versions of key games
- **Unique skill:** Dual-CPU game architecture

**Phase 8 Complete:**
- Student has 60 portfolio games across C128 capabilities
- Masters 8502, Z80, and dual-CPU coordination
- Masters all three operating modes
- Can create commercial-release quality games
- Ready for professional C128 development
- **Expertise:** 8502, Z80, dual-CPU architecture

---

## Resources Required

**Development Tools:**
- Assembler: KickAssembler, ACME, ca65
- Emulator: VICE (excellent C128 support)
- Graphics: C128 graphics tools
- Audio: SID Wizard, GoatTracker
- Utilities: Disk image tools

**Reference Materials:**
- 8502 instruction set (6502-compatible)
- Z80 instruction set
- VIC-IIe reference
- SID reference
- MMU reference
- CP/M reference

**Testing:**
- VICE emulator (development)
- Real C128 hardware (verification)
- C128D (Phase 3+)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - C128D + CP/M (dual-CPU) introduced Phase 3
**Note:** C128 has Phase 0 (BASIC 7.0)
**Historical Note:** Sold 4 million units, most advanced 8-bit Commodore, **dual-CPU pioneer**
**Unique Feature:** **THREE operating modes** (C128, C64, CP/M) - only computer with full dual-CPU game architecture
**Next Steps:** Create C128 8-PHASE-GAME-PROGRESSION.md with specific game mapping
