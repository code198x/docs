# Sinclair ZX81 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** ZX81 (1KB) → 16KB expansion introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Sinclair BASIC (ZX81 variant)
**Historical Note:** Spectrum's predecessor, first affordable computer (under £100), sold 1.5M+ units
**Constraint Note:** **EXTREME** - 1KB standard RAM, software-generated display

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare 1KB vs 16KB implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Display management is display management" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres (within extreme constraints)
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master ZX81 base (1KB RAM, **EXTREME** constraints)
- Phase 3: **16KB RAM expansion introduced** - proper game development, revisit games
- Phase 4-6: Advanced techniques, pushing 16KB limits
- Phase 7: **Modern ZX81** - modern expansions, enhanced capabilities
- Phase 8: Modern development, pathway to Spectrum

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** ZX81 base (1KB RAM - **EXTREME** constraint)
**Complexity:** Simple techniques, minimal memory
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- Z80 instruction set fundamentals
- **Sinclair BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- **EXTREME memory management** (1KB total, less after BASIC/display)
- Software-generated display (no graphics chip - CPU does everything)
- 32×24 character display
- 64-character ROM character set (text graphics)
- Pseudo-graphics (character blocks)
- Keyboard input (membrane keyboard)
- **No sound hardware** (silent)
- Display timing (slow/fast mode)

**Autoload Requirement:**
All games from Lesson 3 onwards must use minimal BASIC loader:
```basic
10 REM GAME
20 RAND USR 16514
```
Minimal bytes due to 1KB constraint. Professional presentation: LOAD from tape, game starts automatically. Every byte precious.

**Deliverables:** 16 complete, playable games within 1KB constraint (**EXTREME** discipline)

**Note:** Phase 1 games must be EXTREMELY simple due to 1KB constraint. Focus on concepts, not features.

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** ZX81 base (1KB RAM)
**Complexity:** Optimization, maximum memory efficiency
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Extreme Z80 optimization (every single byte counts)
- Self-modifying code (save space)
- Display management (software-generated, minimize CPU use)
- Creative use of character graphics (pseudo-graphics)
- Character animation techniques
- Advanced collision detection (minimal memory)
- Multi-screen games (clever state management)
- **Extreme constraint programming** (1KB is TINY)

**Deliverables:** 16 games with commercial-quality features within 1KB RAM (**EXTREME** achievement)

---

### Phase 3: Memory Expansion (16KB)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **ZX81 + 16KB RAM expansion introduced** - transforms platform
**Complexity:** Direct 1KB→16KB comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with 16KB, 3 new showcasing expansion

**Key Learning:**
- **16KB RAM expansion** (common add-on, essential for real games)
- **Direct comparison:** "Here's your 1KB Snake. Now expand it with 16KB RAM"
- Proper game development space
- Better graphics (room for display buffer)
- Sprite data storage
- Faster display modes (FAST mode practical)
- Larger game worlds
- Professional 1KB optimization (for games staying on 1KB)

**Deliverables:** 8 games - 5 enhanced 16KB versions, 3 new showcasing expansion

**Games Revisited with 16KB:**
1. Snake III (16KB) - proper playfield, better graphics
2. Shooter III (16KB) - multiple stages, sprites
3. Platformer III (16KB) - larger world, animations
4. Breakout III (16KB) - more levels, effects
5. One other from Phase 1-2

**New 16KB Games:**
6. Action RPG I (showcasing 16KB space)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** ZX81 + 16KB (pushing limits)
**Complexity:** Advanced techniques, large games (within ZX81 constraints)
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced display techniques (software-generated optimization)
- Pseudo hi-res graphics (creative character manipulation)
- Complex sprite systems (16KB allows data)
- Advanced scrolling (character-based)
- Custom character sets (redefine ROM characters - advanced)
- AI and pathfinding (within constraints)
- Isometric projection (pseudo-graphics)
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced ZX81 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** ZX81 + 16KB mastery
**Complexity:** Genre-specific deep dives, large-scale games (within platform limits)
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture (within ZX81 constraints)
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI
- Power-up progression systems
- **Sound workarounds** (ZX81 has no sound - creative solutions)
- Tape-based save/load systems
- Multi-stage games

**Deliverables:** 4 large-scale genre-defining games (impressive on ZX81)

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** ZX81 + 16KB (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 20+ simultaneous pseudo-sprites
- Complex multi-character systems
- Real-time strategy mechanics (within constraints)
- Commercial polish techniques
- Extreme Z80 optimization
- Fast tape loaders (custom routines)
- Pushing ZX81 absolute limits
- Professional ZX81 development

**Deliverables:** 4 games pushing absolute limits of ZX81

---

### Phase 7: Enhanced ZX81
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** ZX81 + modern enhancements
**Complexity:** Large-scale games with modern capabilities
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- 32KB/56KB RAM expansions (rare but existed)
- Modern ZX81 hardware (hi-res graphics boards)
- Sound boards (Zon X-81, etc.)
- Large game worlds
- Advanced display techniques
- Modern ZX81 expansions
- Commercial ZX81 development (late-era)

**Deliverables:** 2 commercial-scale ZX81 games with enhancements

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern ZX81 development / Pathway to Spectrum
**Complexity:** Modern platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer)

**Key Learning:**
- Modern ZX81 development workflow
- Emulator debugging (EightyOne, ZXSP)
- Modern expansions
- Pushing ZX81 absolute limits
- **Pathway to Spectrum** (same Z80, evolution)
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** Gateway machine that introduced millions to computing

**Deliverables:** 2 portfolio-ready ZX81 games, **prepared for Spectrum transition**

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Memory Management**
- P1: **EXTREME** constraints (1KB total)
- P2: Every single byte optimization
- P3: **16KB expansion** (transforms development)
- P4: Efficient use of 16KB
- P5+: Larger expansions

**2. Display Management**
- P1: Software-generated display basics
- P2: Display optimization (minimize CPU)
- P3: FAST mode practical (with 16KB)
- P4: Advanced display techniques
- P5+: Pseudo hi-res graphics

**3. Sprite Rendering**
- P1: Minimal character graphics
- P2: Pseudo-graphics optimization
- P3: Proper sprites (16KB allows data)
- P4: Advanced sprite systems
- P5+: Multi-sprite (20+ pseudo-sprites)

**4. Scrolling Systems**
- P1: Screen-aligned only (1KB limit)
- P2: Minimal scrolling
- P3: Character scrolling (16KB)
- P4: Advanced scrolling
- P5+: Complex scrolling

**5. Graphics Techniques**
- P1: ROM character set (64 chars)
- P2: Creative character use
- P3: Custom character sets (redefine ROM)
- P4: Pseudo hi-res techniques
- P5+: Advanced graphics

**6. Collision Detection**
- P1: Character-based (minimal memory)
- P2: Bounding box (efficient)
- P3: Pixel-perfect (16KB allows)
- P5+: Multi-layer collision

**7. Input Handling**
- P1: Membrane keyboard
- P2: Key scanning optimization
- P3: Advanced input techniques
- P4: Multiple simultaneous keys

**8. Storage**
- P3: Tape save/load basics
- P4: Advanced tape operations
- P5: Tape-based game structure
- P6: Fast loaders
- P8: Modern storage

---

## Hardware Progression

### ZX81 Base (Phases 1-2)
**Platform:** Sinclair ZX81 (1981)
**Characteristics:**
- Z80 CPU @ 3.25MHz
- **1KB RAM** (total - display + BASIC + program share this!)
- **No graphics chip** (software-generated display)
- 32×24 character display
- 64-character ROM set (text + pseudo-graphics)
- **No sound hardware**
- Membrane keyboard (touch-sensitive)
- Display modes: SLOW (stable, 50Hz) / FAST (unstable display, faster)
- Cassette tape storage

**Focus:** EXTREME memory discipline
- 1KB is TINY (display alone uses ~800 bytes in SLOW mode)
- Every byte must be justified
- Software display generation (CPU-intensive)
- No sound hardware
- Gateway to programming (extremely affordable)

**Historical Significance:**
- Under £100 / $100 (revolutionary price)
- Introduced over 1 million people to programming
- Spectrum's predecessor (same Z80, same ecosystem)
- UK computing revolution catalyst

### ZX81 + 16KB Expansion (Phase 3+)
**Introduced Phase 3**
**Enhanced with:**
- **16KB RAM expansion** (common, essential for games)
- Total 17KB RAM available
- Transforms platform capabilities
- FAST mode practical (display doesn't need constant refresh)
- **Direct comparison:** 1KB vs 16KB

**Focus:** Proper game development
- Room for display buffer
- Sprite data storage
- Larger game worlds
- Professional development possible

### Modern ZX81 (Phase 7-8)
**Modern enhancements:**
- 32KB/56KB RAM expansions
- Hi-res graphics boards (WRX, etc.)
- Sound boards (Zon X-81)
- Modern emulators (EightyOne, ZXSP)
- **Pathway to Spectrum** (natural evolution)

**Focus:** Modern workflow
- Maximum ZX81 capabilities
- Portfolio showcase
- **Preparation for Spectrum** (same Z80)

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (1KB ZX81)** (16 lessons)
- Basic grid movement (Z80 fundamentals)
- Character-based graphics (32×24)
- Minimal state (fits in 1KB!)
- No sound
- **EXTREME constraint:** ~200 bytes for code

**Phase 2: Snake II (1KB optimized)** (32 lessons)
- Self-modifying code
- Optimized display
- Better character graphics
- Still within 1KB
- **Ultimate constraint challenge**

**Phase 3: Snake III (16KB expansion)** (64 lessons - REVISITED WITH 16KB)
- **Proper graphics** (room for display buffer)
- **Larger playfield**
- **Sprite data**
- **Better gameplay**
- **Direct comparison:** "Here's your 1KB Snake. Now expand it with 16KB RAM - see the transformation!"

**Phase 4: Snake IV (Advanced 16KB)** (64 lessons)
- Pseudo hi-res graphics
- Advanced display
- Custom characters
- Multiple game modes

**Phase 6: Snake V (16KB limits)** (128 lessons)
- 20+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing ZX81 limits

Students see evolution: 1KB extreme → 1KB optimized → **16KB transformed** → Advanced → Professional → **Prepared for Spectrum**

---

## Key Differences from Spectrum

**ZX81 vs Spectrum:**
- **Much less RAM:** 1KB vs Spectrum's 48KB (48× less!)
- **No graphics chip:** Software display vs Spectrum's ULA
- **No color:** Mono only vs Spectrum's 15 colors
- **No sound:** Silent vs Spectrum's BEEP
- **Same CPU:** Z80 @ 3.25MHz (similar speed)
- **Predecessor:** ZX81 led to Spectrum design

**ZX81 Advantages:**
- **Extreme discipline** (best training for constraint programming)
- **Historically significant** (gateway machine)
- **Pathway to Spectrum** (same Z80, same ecosystem)
- **Affordable** (under £100)

**Learning Path:**
- ZX81 Phase 0-8 → Spectrum Phase 0-8
- Z80 skills directly transfer
- Understanding extreme constraints improves all coding
- **Natural progression** (historical pathway)

**Same Pattern Library Concepts:**
- Z80 assembly (identical to Spectrum)
- Collision detection algorithms
- AI pathfinding
- Physics systems
- Game design patterns
- All transferable to Spectrum and beyond

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (1KB and 16KB where applicable)
- Verification steps included
- **Memory usage verification:** Must fit within constraints (critical!)

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification
- **Memory check:** Phases 1-2 must fit in 1KB (extreme!)

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete Z80 ZX81 games from scratch
- Understands **EXTREME** memory constraints (1KB)
- Has 16 portfolio ZX81 games within 1KB
- **Unique skill:** Programming under extreme constraints

**Phase 3 Complete:**
- Student masters 16KB expansion
- Can compare/contrast 1KB vs 16KB implementations
- Has both 1KB and 16KB versions of key games
- Understands memory expansion impact dramatically

**Phase 8 Complete:**
- Student has 60 portfolio games across all ZX81 configurations
- Masters 1KB constraints and 16KB development
- Can create commercial-release quality ZX81 games
- **Prepared for Spectrum:** Same Z80, natural evolution
- Ready for professional retro development

---

## Resources Required

**Development Tools:**
- Assembler: z80asm, sjasmplus, pasmo
- Emulator: EightyOne (best), ZXSP, Zesarux
- Graphics: ZX81 character editors
- Utilities: Tape tools, memory monitors

**Reference Materials:**
- Z80 instruction set (same as Spectrum)
- ZX81 BASIC Programming Manual
- ZX81 ROM disassembly
- Memory maps (1KB and expanded)
- Hardware documentation

**Testing:**
- Emulators (development)
- Real ZX81 hardware (verification)
- 16KB expansion pack (Phase 3+)
- Modern expansions (Phase 7-8)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - 16KB expansion introduced Phase 3
**Note:** ZX81 has Phase 0 (Sinclair BASIC - gateway language)
**Historical Significance:** First affordable computer (under £100), Spectrum's predecessor, sold 1.5M+ units
**Constraint Note:** **EXTREME** - 1KB standard RAM is the ultimate constraint programming challenge
**Next Steps:** Create ZX81 8-PHASE-GAME-PROGRESSION.md, then natural progression to Spectrum curriculum
