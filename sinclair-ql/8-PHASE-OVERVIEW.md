# Sinclair QL Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** QL base → Gold Card introduced Phase 3 → Q40/Q60 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - SuperBASIC
**Historical Note:** Sinclair's business computer (1984), innovative but flawed, 68000 family pioneer
**CPU Note:** 68008 - 16-bit internally, 8-bit external bus (unusual compromise)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare base QL vs Gold Card implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "68000 addressing modes are 68000 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres (within QL constraints)
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master QL base (68008 @ 7.5MHz, 128KB RAM, limited graphics)
- Phase 3: **Gold Card introduced** - 68000 @ 16MHz, more RAM, revisit games
- Phase 4-6: Advanced techniques, pushing Gold Card limits
- Phase 7: **Q40/Q60** - 68040/68060 modern QL systems
- Phase 8: Modern QL development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Sinclair QL base (68008 @ 7.5MHz, 128KB RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 68000 instruction set fundamentals (68008 subset - 8-bit external bus)
- **SuperBASIC loader - Lesson 2-3, mandatory from Lesson 3**
- Screen memory (dual-screen system, 512×256 resolution)
- 4-colour display (8 colours in flashing mode - limited)
- Software sprite rendering (no hardware sprites)
- Keyboard input (distinctive QL keyboard)
- Microdrive storage (notoriously unreliable, but original)
- QDOS operating system (multitasking!)
- Interrupt timing (50Hz PAL / 60Hz NTSC)
- **Unique constraint:** 8-bit external bus (68008) slows memory access

**Autoload Requirement:**
All games from Lesson 3 onwards must use SuperBASIC loader:
```basic
100 LBYTES "game_bin", 32768
110 CALL 32768
```
Or use multitasking features. Professional presentation: LOAD from Microdrive, RUN, game starts automatically.

**Deliverables:** 16 complete, playable QL games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** QL base (68008 @ 7.5MHz, 128KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 68000 code (despite 8-bit bus bottleneck)
- QL graphics modes (512×256, 4 colours)
- Character-based sprites (software rendering)
- Advanced collision detection
- Multi-screen game structures
- QDOS multitasking (unique feature!)
- Memory management (128KB efficiently)
- Disk I/O (floppy disk - replacing unreliable Microdrives)
- QL-specific optimizations (8-bit bus considerations)

**Deliverables:** 16 games with commercial-quality QL features

---

### Phase 3: Enhanced Systems (Gold Card)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Gold Card introduced** - 68000 @ 16MHz, more RAM
**Complexity:** Direct base QL→Gold Card comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with Gold Card, 3 new showcasing enhancements

**Key Learning:**
- **Gold Card** (popular third-party upgrade, essential for serious QL use)
- **68000 CPU @ 16MHz** (vs 68008 @ 7.5MHz - over 2× faster, full 16-bit bus!)
- **More RAM** (512KB-4MB vs 128KB)
- **Direct comparison:** "Here's your base QL game. Now enhance it with Gold Card"
- Better memory access (16-bit bus vs 8-bit)
- SMSQ/E operating system (enhanced QDOS)
- Disk systems (reliable storage)
- Professional base QL optimization (for games staying on 128KB)

**Deliverables:** 8 games - 5 enhanced Gold Card versions, 3 new showcasing Gold Card

**Games Revisited with Gold Card:**
1. Snake III (Gold Card) - faster CPU, more RAM, smoother
2. Shooter III (Gold Card) - larger worlds, better performance
3. Platformer III (Gold Card) - more detail, faster
4. Breakout III (Gold Card) - enhanced effects
5. One other from Phase 1-2

**New Gold Card Games:**
6. Action RPG I (showcasing more RAM, faster CPU)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Gold Card (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced 68000 programming (full instruction set)
- Memory management (512KB-4MB efficiently)
- Complex sprite systems (software but faster CPU)
- Advanced graphics techniques
- SMSQ/E multitasking mastery
- Disk I/O optimization
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced Gold Card techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Gold Card mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced disk I/O (large data sets)
- Multi-disk games
- SMSQ/E advanced features

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Gold Card (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 68000 optimization (16MHz maximum efficiency)
- Fast disk loaders
- Pushing Gold Card limits
- Professional QL development

**Deliverables:** 4 games pushing absolute limits of Gold Card QL

---

### Phase 7: Modern QL Systems (Q40/Q60)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Q40 (68040) / Q60 (68060) modern QL systems
**Complexity:** Large-scale games with modern QL hardware
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **Q40** (68040 @ 40MHz) - modern QL hardware
- **Q60** (68060 @ 66MHz) - ultimate QL system
- Modern QL capabilities (massive speed increase)
- SMSQ/E latest features
- Large game worlds
- Advanced graphics techniques
- Commercial QL development
- **Historical significance:** QL community still active

**Deliverables:** 2 commercial-scale modern QL games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern QL development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern QL development workflow
- Emulator debugging (Q-emuLator, uQLx, QemuLator, QLAY)
- Modern QL hardware (Q40/Q60)
- Pushing QL absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** Innovative design, active community still exists

**Deliverables:** 2 portfolio-ready commercial-quality QL games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 68000 Programming**
- P1: Basic instructions (68008 subset - 8-bit bus constraints)
- P2: Advanced 68000 techniques (despite bus limitations)
- P3: **Gold Card (68000 @ 16MHz, full 16-bit bus)**
- P4: Complex 68000 techniques
- P7: **Q40/Q60 (68040/68060 - modern speed)**

**2. Graphics Programming**
- P1: QL display basics (512×256, 4 colours)
- P2: Advanced QL graphics techniques
- P3: Gold Card graphics (faster rendering)
- P4: Complex graphics systems
- P5+: Maximum graphics capabilities

**3. Sprite Rendering**
- P1: Software sprites (character-based)
- P2: Optimized software sprites
- P3: Gold Card sprites (faster CPU allows complexity)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Scrolling Systems**
- P1: Screen-aligned scrolling
- P2: Character scrolling
- P3: Gold Card scrolling (smoother, faster)
- P4: Pixel scrolling (advanced)
- P5+: Complex scrolling effects

**5. Sound Programming**
- P1: QL beeper (simple, like Spectrum)
- P2: Creative beeper techniques
- P3: Gold Card audio (faster allows complexity)
- Note: QL has no advanced sound chip (limitation)

**6. Memory Management**
- P1: Basic RAM (128KB base QL)
- P2: Efficient data structures
- P3: **Gold Card (512KB-4MB RAM)**
- P4: Large data management
- P5+: Maximum RAM efficiency

**7. Multitasking**
- P1: QDOS multitasking basics (unique feature!)
- P2: Multi-job games
- P3: SMSQ/E multitasking (Gold Card)
- P4: Advanced multitasking techniques

**8. Disk I/O**
- P1: Microdrive operations (unreliable but original)
- P2: Floppy disk (replacing Microdrives)
- P3: Gold Card disk I/O (faster)
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders

---

## Hardware Progression

### Sinclair QL Base (Phases 1-2)
**Platform:** Sinclair QL (1984)
**Characteristics:**
- **68008 CPU @ 7.5MHz** (16-bit internally, 8-bit external bus - unusual)
- 128KB RAM (expandable to 640KB)
- 512×256 resolution (high resolution for era)
- **4 colours** (8 in flashing mode - limited palette)
- **No hardware sprites** (software rendering required)
- Simple sound (beeper, like Spectrum)
- Distinctive keyboard (not well-liked)
- **Microdrive storage** (notoriously unreliable tape loops)
- **QDOS operating system** (multitasking!)
- **SuperBASIC** (advanced, interpreted)

**Focus:** Master 68000 architecture within constraints
- 68000 family programming (68008 subset)
- 8-bit bus optimization (major constraint)
- QL graphics (512×256, 4 colours)
- QDOS multitasking (unique!)
- SuperBASIC (advanced BASIC)

**Historical Context:**
- Sinclair's business computer attempt
- Released 1984 (rushed to market)
- Commercial failure (~150,000 units)
- Innovative but flawed design
- Bridge between Spectrum (games) and business computers
- Notable bugs in early ROM versions
- Microdrive reliability issues

**Unique Features:**
- **Multitasking OS** (QDOS - ahead of its time!)
- **SuperBASIC** (very advanced interpreter)
- **68000 family CPU** (first widely-available 68000-series home computer)
- High resolution (512×256)

**Constraints:**
- 8-bit external bus (68008) - memory bottleneck
- Only 4 colours (serious limitation)
- No hardware sprites
- Unreliable Microdrive storage
- Limited sound (beeper only)

### Gold Card (Phase 3+)
**Platform:** Gold Card (third-party upgrade)
**Introduced Phase 3**
**Enhanced Features:**
- **68000 CPU @ 16MHz** (vs 68008 @ 7.5MHz)
- **Full 16-bit bus** (vs 8-bit - much faster memory access!)
- **512KB-4MB RAM** (vs 128KB)
- **SMSQ/E operating system** (enhanced QDOS)
- Better reliability
- Floppy disk support
- **Direct comparison:** Base QL vs Gold Card

**Focus:** Leverage enhanced hardware
- True 68000 (not 68008)
- 16-bit memory bus (no bottleneck)
- More RAM (512KB-4MB)
- Faster CPU (16MHz)

**Why Gold Card Matters:**
- Essential for serious QL use
- Popular third-party upgrade
- Transformed QL usability
- SMSQ/E operating system

### Q40/Q60 (Phase 7)
**Platform:** Q40 (68040) / Q60 (68060) - modern QL
**Enhanced Features:**
- **68040 @ 40MHz** (Q40) or **68060 @ 66MHz** (Q60)
- Much more RAM
- Modern capabilities
- Active QL community hardware
- SMSQ/E latest

**Focus:** Modern QL performance
- 68040/68060 optimization
- Maximum speed
- Large-scale games
- Modern QL development

### Modern QL (Phase 8)
**Modern enhancements:**
- Q-emuLator (excellent emulation)
- uQLx, QemuLator, QLAY emulators
- Modern QL hardware (Q40/Q60)
- Active community (still exists!)
- SMSQ/E ongoing development

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase
- Historical appreciation

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (QL base)** (16 lessons)
- Basic grid movement (68008 fundamentals)
- QL graphics (512×256, 4 colours)
- Software sprites
- Beeper sound
- 128KB RAM

**Phase 2: Snake II (QL optimized)** (32 lessons)
- Optimized 68000 code (despite 8-bit bus)
- Better graphics
- Character animation
- Multi-screen levels
- Optimized base QL

**Phase 3: Snake III (Gold Card)** (64 lessons - REVISITED WITH GOLD CARD)
- **68000 @ 16MHz** (vs 68008 @ 7.5MHz)
- **16-bit memory bus** (vs 8-bit - much faster!)
- **More RAM** (512KB-4MB)
- **Smoother gameplay**
- **Direct comparison:** "Here's your base QL Snake. Now enhance it with Gold Card - feel the speed difference!"

**Phase 4: Snake IV (Advanced Gold Card)** (64 lessons)
- Advanced graphics techniques
- SMSQ/E features
- Complex game modes
- Disk-based levels

**Phase 6: Snake V (Gold Card limits)** (128 lessons)
- 32+ simultaneous sprites
- Extreme optimization
- Commercial-quality
- Pushing Gold Card limits

**Phase 7: Snake VI (Q40/Q60)** (if applicable)
- 68040/68060 speed
- Modern QL capabilities

Students see evolution: QL basics → QL optimized → **Gold Card enhanced** → Advanced → Modern

---

## Key Differences from Other 68000 Platforms

**QL vs Amiga/Atari ST:**
- **68008 CPU** (vs 68000) - 8-bit external bus (major bottleneck)
- **Limited graphics:** 4 colours (vs Amiga's 4096, ST's 512)
- **No hardware sprites** (vs Amiga's 8)
- **Simpler sound:** Beeper (vs Amiga's Paula, ST's YM2149)
- **Earlier:** 1984 (vs 1985 for ST/Amiga)
- **Business-oriented** (vs games/creativity)
- **Unique:** Multitasking OS (QDOS ahead of its time)

**QL Advantages:**
- Early 68000 family adoption
- Multitasking OS (QDOS innovative)
- SuperBASIC (very advanced)
- High resolution (512×256)
- Active community (still exists)

**QL Considerations:**
- 8-bit bus bottleneck (68008)
- Limited colours (4 only)
- No hardware sprites
- Unreliable Microdrives
- Commercial failure (but technically interesting)

**Learning Path:**
- QL → Amiga/ST (68000 family evolution)
- 68000 skills transfer (QL teaches architecture)
- Understanding 68000 family history

**Same Pattern Library Concepts:**
- 68000 assembly (same as Amiga/ST/X68000)
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
- Expected output defined (base QL and Gold Card where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 68000 QL games from scratch
- Understands 68008 constraints (8-bit bus)
- Understands QDOS multitasking (unique feature)
- Has 16 portfolio QL games

**Phase 3 Complete:**
- Student masters Gold Card enhancements
- Can compare/contrast base QL vs Gold Card implementations
- Understands 16-bit bus improvement
- Has both base QL and Gold Card versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all QL systems
- Masters 68000 architecture
- Understands 68000 family evolution (68008→68000→68040/68060)
- Can create commercial-release quality games
- Ready for professional QL development
- **68000 expertise** transfers to Amiga, Atari ST, X68000

---

## Resources Required

**Development Tools:**
- Assembler: QMAC, GST assembler, modern cross-assemblers
- Emulator: Q-emuLator (excellent), uQLx, QemuLator, QLAY
- Graphics: QL graphics tools
- Utilities: Disk image tools

**Reference Materials:**
- 68000 instruction set (68008 subset)
- QL Technical Manual
- QDOS reference
- SMSQ/E reference
- SuperBASIC manual

**Testing:**
- Emulators (development)
- Real QL hardware (verification, if accessible)
- Gold Card (Phase 3+)
- Q40/Q60 (Phase 7, if accessible)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Gold Card introduced Phase 3
**Note:** QL has Phase 0 (SuperBASIC - very advanced BASIC)
**Historical Note:** Sinclair's business computer (1984), innovative but flawed, 68000 family pioneer
**CPU Note:** 68008 @ 7.5MHz - 16-bit internally, 8-bit external bus (unusual compromise, major bottleneck)
**Key Constraint:** 8-bit external bus (68008) limits performance despite 68000 architecture
**Upgrade Path:** Gold Card essential for serious QL development (68000 @ 16MHz, 16-bit bus)
**Next Steps:** Create QL 8-PHASE-GAME-PROGRESSION.md with specific game mapping
