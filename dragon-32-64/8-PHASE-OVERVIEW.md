# Dragon 32/64 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Dragon 32 → Dragon 64 introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Dragon BASIC
**CPU Note:** **6809 - sophisticated 8-bit architecture** (same as CoCo)
**Historical Note:** UK/European version of CoCo (licensed design)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare Dragon 32 vs Dragon 64 implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "6809 addressing modes are 6809 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Dragon 32 (32KB RAM, 6809, VDG graphics)
- Phase 3: **Dragon 64 introduced** - 64KB RAM, revisit games
- Phase 4-6: Advanced techniques, pushing Dragon 64 limits
- Phase 7: **Modern Dragon** - DragonDOS, modern expansions
- Phase 8: Modern Dragon development, CoCo 3 interoperability

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Dragon 32 (32KB RAM, 6809 @ 0.89MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- **6809 instruction set fundamentals** (sophisticated 8-bit architecture)
- **Dragon BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- VDG (Video Display Generator - MC6847) basics
- Semigraphics modes (SG4, SG6, SG8, SG12, SG24)
- PMODE graphics (256×192×2, 128×192×4, 128×96×4, 128×64×4)
- Software sprite rendering
- Joystick input (via PIA chip)
- Sound (1-bit via 6-bit DAC)
- Interrupt timing (50Hz PAL / 60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use Dragon BASIC loader:
```basic
10 CLEAR &H7FFF
20 CLOADM
30 EXEC
```
Or for disk:
```basic
10 CLEAR &H7FFF
20 LOADM"GAME"
30 EXEC
```
Professional presentation: RUN from cassette/disk, game starts automatically.

**Deliverables:** 16 complete, playable Dragon 32 games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Dragon 32 (32KB RAM)
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

**Deliverables:** 16 games with commercial-quality Dragon 32 features

---

### Phase 3: Memory Expansion (Dragon 64)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Dragon 64 introduced** - 64KB RAM
**Complexity:** Direct Dragon 32→Dragon 64 comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with Dragon 64, 3 new showcasing 64KB

**Key Learning:**
- **64KB RAM** (double the memory of Dragon 32)
- **Direct comparison:** "Here's your 32KB Snake. Now expand it with Dragon 64's 64KB"
- Larger game worlds (more room for data)
- Better graphics (room for character sets, sprites)
- Music and sound effects simultaneously
- Advanced sprite systems
- DragonDOS (disk operating system)
- Professional Dragon 32 optimization (for games staying on 32KB)

**Deliverables:** 8 games - 5 enhanced Dragon 64 versions, 3 new showcasing 64KB

**Games Revisited with Dragon 64:**
1. Snake III (Dragon 64) - larger worlds, better graphics
2. Shooter III (Dragon 64) - multiple stages, music
3. Platformer III (Dragon 64) - larger world, animations
4. Breakout III (Dragon 64) - more levels, effects
5. One other from Phase 1-2

**New Dragon 64 Games:**
6. Action RPG I (showcasing 64KB RAM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Dragon 64 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced VDG programming (custom character sets, hi-res tricks)
- Complex sprite systems (64KB allows proper data)
- Advanced sound programming (6-bit DAC)
- Scrolling techniques (character and pixel-based)
- DragonDOS programming
- Disk I/O optimization
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced Dragon 64 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Dragon 64 mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced sound programming
- Disk-based save/load systems
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Dragon 64 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 6809 optimization
- Fast disk loaders (custom DragonDOS routines)
- Pushing Dragon 64 limits
- Professional Dragon development

**Deliverables:** 4 games pushing absolute limits of Dragon 64

---

### Phase 7: Enhanced Dragon
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Dragon 64 + modern expansions
**Complexity:** Large-scale games with modern enhancements
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- Modern Dragon expansions (RAM upgrades, etc.)
- DriveWire (PC connection for disk emulation)
- Modern sound expansions
- Large game worlds
- Advanced VDG techniques
- Dragon 200 compatibility (rare model)
- Commercial Dragon development

**Deliverables:** 2 commercial-scale Dragon games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Dragon development / CoCo 3 interoperability
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern Dragon development workflow
- Emulator debugging (XRoar, MAME)
- DragonMMC (SD card interface)
- Modern expansions
- **CoCo 3 interoperability** (some Dragon users upgraded to CoCo 3 hardware)
- Pushing Dragon absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- **6809 mastery:** Understanding sophisticated 8-bit architecture

**Deliverables:** 2 portfolio-ready commercial-quality Dragon games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 6809 Programming**
- P1: Basic instructions (LDA, STA, ADD, etc.)
- P2: Advanced features (two accumulators, index registers)
- P3: Dragon 64 optimization (more RAM)
- P4: Complex 6809 techniques
- P5+: Extreme optimization
- **Note:** 6809 same as CoCo (licensed design)

**2. Graphics Programming**
- P1: VDG modes (semigraphics, PMODE)
- P2: Advanced VDG techniques
- P3: Dragon 64 graphics (more RAM for data)
- P4: Custom character sets, tricks
- P5+: Advanced graphics systems

**3. Sprite Rendering**
- P1: Software sprites (VDG)
- P2: Optimized sprites (6809 efficient)
- P3: Dragon 64 sprites (64KB allows more data)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Scrolling Systems**
- P1: Screen-aligned scrolling
- P2: Pixel scrolling (VDG)
- P3: Dragon 64 scrolling (buffering)
- P4: Complex scrolling
- P5+: Advanced scrolling

**5. Sound Programming**
- P1: 1-bit sound (6-bit DAC)
- P2: Sound synthesis techniques
- P3: Dragon 64 audio (music + effects)
- P4: Complex audio
- P5+: Modern sound expansions

**6. Memory Management**
- P1: Basic RAM (32KB Dragon 32)
- P2: Efficient data structures
- P3: **Dragon 64 (64KB RAM)**
- P4: Efficient use of 64KB
- P5+: Modern RAM expansions

**7. Collision Detection**
- P1: Bounding box collision
- P2: Pixel-perfect collision
- P3: Dragon 64 optimized collision
- P5+: Multi-layer collision

**8. Disk I/O**
- P3: DragonDOS operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage (DragonMMC)

---

## Hardware Progression

### Dragon 32 (Phases 1-2)
**Platform:** Dragon Data Dragon 32 (1982)
**Characteristics:**
- **6809 CPU @ 0.89MHz** (same as CoCo)
- **32KB RAM**
- **MC6847 VDG chip** (Video Display Generator - same as CoCo)
- Semigraphics: SG4, SG6 (64×48), SG8, SG12, SG24
- PMODE: 256×192×2, 128×192×4, 128×96×4, 128×64×4
- Sound: 6-bit DAC (1-bit typically used)
- Cassette tape standard storage
- 50Hz PAL (UK/Europe) or 60Hz NTSC

**Focus:** Master 6809 and VDG
- 6809 architecture (sophisticated 8-bit)
- VDG graphics programming
- Software sprite rendering
- 32KB RAM constraint

**Historical Context:**
- Licensed CoCo design from Tandy
- Popular in UK/Europe (especially UK)
- Sold ~200,000 units
- Competed with Spectrum, C64

### Dragon 64 (Phase 3+)
**Platform:** Dragon Data Dragon 64 (1983)
**Introduced Phase 3**
**Enhanced Features:**
- **64KB RAM** (double the Dragon 32)
- Same 6809 CPU @ 0.89MHz
- Same MC6847 VDG chip
- DragonDOS (disk operating system) available
- **Direct comparison:** 32KB vs 64KB RAM

**Focus:** Leverage memory expansion
- More ROM for graphics/sprites
- Larger game worlds
- Music + effects simultaneously
- Better game development

**Note:** Dragon never got equivalent of CoCo 3 (GIME chip)

### Modern Dragon (Phase 7-8)
**Modern enhancements:**
- DragonMMC (SD card interface)
- Modern RAM expansions
- DriveWire (PC connection)
- Modern sound expansions
- XRoar emulator (excellent)
- **CoCo 3 interoperability** (some users upgraded)

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase
- CoCo 3 compatibility (optional)

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Dragon 32)** (16 lessons)
- Basic grid movement (6809 fundamentals)
- Semigraphics or PMODE graphics
- Software sprites
- DAC sound
- 32KB RAM

**Phase 2: Snake II (Dragon 32 optimized)** (32 lessons)
- Optimized 6809 code
- Better VDG graphics
- Advanced sound
- Multi-screen levels
- Optimized Dragon 32

**Phase 3: Snake III (Dragon 64)** (64 lessons - REVISITED WITH 64KB)
- **64KB RAM** (double the memory)
- **Larger playfield**
- **Music + effects**
- **Better graphics**
- **Direct comparison:** "Here's your 32KB Snake. Now expand it with Dragon 64"

**Phase 4: Snake IV (Advanced Dragon 64)** (64 lessons)
- Custom character sets
- Advanced graphics
- Complex audio
- Disk-based levels

**Phase 6: Snake V (Dragon 64 limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing Dragon 64 limits

Students see evolution: 32KB basics → 32KB optimized → **64KB expanded** → Advanced → Professional

---

## Key Differences from CoCo

**Dragon vs CoCo:**
- **Same 6809 CPU** @ 0.89MHz
- **Same MC6847 VDG chip**
- **Similar architecture** (licensed design)
- **Different BASIC:** Dragon BASIC vs Extended Color BASIC
- **Different keyboard layout**
- **PAL timing standard** (50Hz vs CoCo's 60Hz NTSC)
- **No Dragon equivalent of CoCo 3** (GIME chip)
- **UK/European market** vs CoCo's US/Canada

**Dragon Advantages:**
- Same sophisticated 6809 CPU
- Compatible with many CoCo concepts
- PAL standard (Europe)
- Strong UK following

**Learning Path:**
- Dragon and CoCo share 6809 architecture
- Skills transfer between platforms
- CoCo 3 can be used for advanced projects (Phase 8)

**Same Pattern Library Concepts:**
- 6809 assembly (identical to CoCo)
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
- Expected output defined (Dragon 32 and Dragon 64 where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6809 Dragon games from scratch
- Understands 6809 architecture
- Understands VDG graphics
- Has 16 portfolio Dragon 32 games

**Phase 3 Complete:**
- Student masters Dragon 64 (64KB RAM)
- Can compare/contrast Dragon 32 vs Dragon 64 implementations
- Has both Dragon 32 and Dragon 64 versions of key games
- **6809 mastery** (sophisticated 8-bit architecture)

**Phase 8 Complete:**
- Student has 60 portfolio games across Dragon variants
- Masters 6809 architecture
- Masters VDG graphics programming
- Can create commercial-release quality games
- Ready for professional Dragon development
- **6809 expertise** transfers to CoCo, Thomson platforms

---

## Resources Required

**Development Tools:**
- Assembler: LWTOOLS (cross-platform), asm6809
- Emulator: XRoar (excellent), MAME
- Graphics: Dragon graphics editors
- Audio: Sound tools
- Utilities: Disk image tools

**Reference Materials:**
- **6809 instruction set** (same as CoCo)
- MC6847 VDG reference
- Dragon Technical Reference
- Dragon BASIC reference
- DragonDOS documentation

**Testing:**
- Emulators (development)
- Real Dragon hardware (verification)
- Dragon 64 (Phase 3+)
- Modern expansions (DragonMMC, etc.)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Dragon 64 introduced Phase 3
**Note:** Dragon has Phase 0 (Dragon BASIC)
**CPU Note:** **6809 - same sophisticated architecture as CoCo**
**Historical Note:** UK/European version of CoCo, licensed design
**Next Steps:** Create Dragon 8-PHASE-GAME-PROGRESSION.md with specific game mapping
