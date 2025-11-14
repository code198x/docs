# Commodore Plus/4 & C16 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Plus/4 (64KB) & C16 (16KB) → Advanced TED techniques Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - BASIC 3.5
**Historical Note:** Commodore's C64 replacement attempt (1984), commercial failure but interesting hardware
**Relationship:** NOT C64-compatible (major issue!), TED chip instead of VIC-II+SID

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare basic vs advanced TED techniques
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "7501 addressing modes are 7501 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Plus/4 & C16 (7501, TED chip, 121 colours)
- Phase 3: **Advanced TED mastery** - pushing graphics/sound limits, C16 vs Plus/4
- Phase 4-6: Advanced techniques, pushing Plus/4 limits
- Phase 7: **Maximum Plus/4** - all capabilities, professional development
- Phase 8: Modern Plus/4 development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Commodore Plus/4 (64KB) & C16 (16KB), 7501 CPU @ ~1.76MHz
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 7501 instruction set fundamentals (6502-compatible, similar to 8502)
- **BASIC 3.5 loader - Lesson 2-3, mandatory from Lesson 3**
- TED chip (Text/Graphics/Sound combined - cost-reduced design)
- 320×200 resolution (hi-res mode)
- **121 colours** from palette of 121 (more than C64!)
- **8 luminance levels** (unique to TED)
- Software sprite rendering (no hardware sprites - unlike C64!)
- TED sound (2 channels + noise - simpler than SID)
- 64KB RAM (Plus/4) or 16KB RAM (C16)
- Keyboard/joystick input
- Cassette tape storage (built-in Plus/4)
- Interrupt timing (50Hz PAL / 60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use BASIC 3.5 loader:
```basic
10 SYS 52224
20 BANK 0
30 SYS [start address]
```
Professional presentation: LOAD from tape/disk, RUN, game starts automatically.

**Deliverables:** 16 complete, playable Plus/4/C16 games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Plus/4 (64KB) & C16 (16KB)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 7501 code (6502-compatible optimization)
- TED graphics modes (320×200 hi-res, multicolour)
- **121 colours mastery** (8 luminance levels)
- Software sprite optimization (no hardware sprites)
- TED sound programming (2 channels + noise)
- Advanced collision detection
- Multi-screen game structures
- Memory management (64KB Plus/4, 16KB C16)
- Cassette/disk I/O
- BASIC 3.5 features (better than C64's BASIC 2.0)

**Deliverables:** 16 games with commercial-quality Plus/4/C16 features

---

### Phase 3: Advanced TED Mastery
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** Plus/4 & C16 advanced techniques
**Complexity:** Direct basic→advanced comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with advanced TED, 3 new showcasing mastery

**Key Learning:**
- **Advanced TED graphics** (all capabilities)
- **121 colours mastery** (all 8 luminance levels, colour cycling)
- **Plus/4 vs C16** comparison (64KB vs 16KB - like VIC-20 lesson)
- **Direct comparison:** "Here's your basic game. Now enhance it with advanced TED techniques"
- Advanced TED sound (2 channels + noise - creative usage)
- Memory optimization (especially C16's 16KB constraint)
- Professional Plus/4 development
- Comparing to C64 (why not compatible, what's different)

**Deliverables:** 8 games - 5 enhanced advanced versions, 3 new showcasing TED mastery

**Games Revisited with Advanced TED:**
1. Snake III (Advanced TED) - colour cycling, advanced graphics
2. Shooter III (Advanced TED) - 121 colours utilized, creative sound
3. Platformer III (Advanced TED) - multicolour mode, luminance effects
4. Breakout III (Advanced TED) - palette effects, colour cycling
5. One other from Phase 1-2

**New Advanced TED Games:**
6. Action RPG I (showcasing Plus/4's 64KB vs C16's 16KB)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Plus/4 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced TED programming (all graphics modes)
- Maximum colour utilization (121 colours + 8 luminance)
- Complex software sprite systems (no hardware sprites)
- Advanced TED sound (creative 2-channel + noise)
- Memory banking (64KB efficiently)
- Disk I/O (1541 compatibility)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced Plus/4 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Plus/4 mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced TED audio techniques
- Disk-based multi-level games
- Multi-disk games (if applicable)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Plus/4 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 7501 optimization
- Fast disk loaders
- Pushing Plus/4 limits
- Professional Plus/4 development

**Deliverables:** 4 games pushing absolute limits of Plus/4

---

### Phase 7: Maximum Plus/4
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Plus/4 (maximum capabilities)
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- Maximum 64KB RAM usage
- All TED capabilities (graphics, sound, everything)
- Large game worlds (disk-based)
- Advanced graphics techniques (all modes)
- Commercial Plus/4 development
- Professional quality polish

**Deliverables:** 2 commercial-scale Plus/4 games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Plus/4 development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern Plus/4 development workflow
- Emulator debugging (VICE, YAPE, Plus/4 emulators)
- Modern expansions (rare but exist)
- Pushing Plus/4 absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** C64 replacement attempt that failed, interesting hardware

**Deliverables:** 2 portfolio-ready commercial-quality Plus/4 games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 7501 Programming**
- P1: Basic instructions (6502-compatible, similar to 8502)
- P2: Advanced 7501 techniques
- P3: Advanced TED optimization
- P4: Complex 7501 techniques
- P5+: Extreme optimization

**2. Graphics Programming**
- P1: TED basics (320×200, 121 colours)
- P2: TED modes (hi-res, multicolour)
- P3: **Advanced TED** (colour cycling, luminance)
- P4: Maximum TED capabilities
- P5+: Complex graphics systems

**3. Sprite Rendering**
- P1: Software sprites (no hardware sprites!)
- P2: Optimized software sprites
- P3: Advanced sprite techniques
- P4: Complex sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Colour Programming**
- P1: **121 colours basics** (from palette)
- P2: **8 luminance levels** (unique to TED)
- P3: Colour cycling, palette effects
- P5+: Advanced colour techniques

**5. Sound Programming**
- P1: TED sound basics (2 channels + noise)
- P2: Music composition (2-channel)
- P3: Creative TED audio (advanced)
- P4: Professional audio (within limitations)
- Note: TED simpler than SID (no filters, fewer features)

**6. Memory Management**
- P1: Basic RAM (64KB Plus/4, 16KB C16)
- P2: Efficient data structures
- P3: **Plus/4 vs C16** (64KB vs 16KB optimization)
- P4: Complex memory techniques
- P5+: Maximum efficiency

**7. Collision Detection**
- P1: Software collision (no hardware support)
- P2: Bounding box optimization
- P3: Advanced collision techniques
- P5+: Multi-layer collision

**8. Disk I/O**
- P2: Cassette/disk operations
- P3: 1541 disk drive (compatible with Plus/4)
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders

---

## Hardware Progression

### Plus/4 & C16 (Phases 1-2)
**Platform:** Commodore Plus/4 (64KB) / C16 (16KB) (1984)
**Characteristics:**
- **7501 CPU @ ~1.76MHz** (6502-compatible, similar to 8502)
- **64KB RAM** (Plus/4) or **16KB RAM** (C16)
- **TED chip** (Text/Graphics/Sound combined - cost reduction)
- 320×200 resolution (hi-res)
- **121 colours** from palette of 121 (more than C64!)
- **8 luminance levels** (unique to TED)
- **No hardware sprites** (software rendering - unlike C64!)
- **TED sound:** 2 channels + noise (simpler than SID)
- Cassette tape (Plus/4 built-in)
- 1541 disk drive compatible
- **NOT C64-compatible** (major marketing problem!)

**Focus:** Master TED chip programming
- 7501 programming (6502-compatible)
- TED graphics (121 colours, 8 luminance)
- TED sound (2 channels + noise)
- Software sprites (no hardware sprites)
- BASIC 3.5 (better than C64's 2.0)

**Historical Context:**
- Commodore's C64 replacement attempt
- **Commercial failure** (~1.5 million units vs C64's ~17 million)
- **NOT C64-compatible** (killed it commercially)
- Positioned as business computer (Plus/4 had built-in software)
- Better BASIC (3.5 vs C64's 2.0)
- More colours (121 vs C64's 16)
- Simpler sound (TED vs SID)
- No sprites (vs C64's 8 hardware sprites)
- Released 1984, discontinued 1985 (very short lifespan)

**Plus/4 Built-in Software:**
- Word processor (3-Plus-1)
- Spreadsheet
- Database
- Graphics program
- Business-oriented positioning

**C16 vs Plus/4:**
- C16: 16KB RAM, no built-in software, budget model
- Plus/4: 64KB RAM, built-in business software
- Both: Same 7501 CPU, TED chip, 121 colours

### Advanced TED (Phase 3+)
**Introduced Phase 3**
**Enhanced Focus:**
- Advanced TED techniques (all graphics modes)
- 121 colours + 8 luminance mastery
- Plus/4 vs C16 comparison (64KB vs 16KB)
- Professional optimization
- Creative TED sound usage

**Focus:** Master TED capabilities
- All colour combinations (121 × 8 luminance)
- Advanced graphics modes
- Creative sound (2 channels + noise limits)
- Professional development

### Modern Plus/4 (Phase 7-8)
**Modern enhancements:**
- VICE emulator (Plus/4 support)
- YAPE emulator (dedicated Plus/4)
- Modern assemblers
- Small active community

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Plus/4 base)** (16 lessons)
- Basic grid movement (7501 fundamentals)
- TED graphics (121 colours)
- Software sprites (no hardware sprites)
- TED sound (2 channels + noise)
- 64KB RAM (Plus/4) or 16KB (C16)

**Phase 2: Snake II (Plus/4 optimized)** (32 lessons)
- Optimized 7501 code
- Better TED graphics (luminance levels)
- Better sprite rendering
- 2-channel music
- Multi-screen levels

**Phase 3: Snake III (Advanced TED)** (64 lessons - REVISITED WITH ADVANCED TED)
- **Advanced TED graphics** (colour cycling)
- **8 luminance levels** (visual depth)
- **Plus/4 vs C16** (64KB vs 16KB comparison)
- **Creative sound** (2 channels optimized)
- **Direct comparison:** "Here's your basic Snake. Now enhance it with advanced TED techniques"

**Phase 4: Snake IV (Advanced)** (64 lessons)
- Advanced colour effects
- Complex sprites
- Professional audio
- Disk-based levels

**Phase 6: Snake V (Plus/4 limits)** (128 lessons)
- 32+ simultaneous sprites
- Extreme optimization
- Commercial-quality
- Pushing Plus/4 limits

Students see evolution: Plus/4 basics → Plus/4 optimized → **Advanced TED** → Maximum capabilities → Professional

---

## Key Differences from C64

**Plus/4 vs C64:**
- **Same CPU family:** 7501 (Plus/4) vs 6510 (C64) - both 6502-compatible
- **TED chip** vs **VIC-II + SID** (cost reduction, combined chip)
- **More colours:** 121 (Plus/4) vs 16 (C64)
- **8 luminance levels** (Plus/4 unique) vs fixed brightness (C64)
- **No hardware sprites** (Plus/4) vs **8 hardware sprites** (C64)
- **Simpler sound:** TED 2-channel + noise vs SID 3-channel + filters
- **Better BASIC:** 3.5 (Plus/4) vs 2.0 (C64)
- **NOT compatible** (major problem!)
- **Built-in software** (Plus/4 only - word processor, etc.)

**Plus/4 Advantages over C64:**
- More colours (121 vs 16)
- 8 luminance levels (visual depth)
- Better BASIC (3.5 vs 2.0)
- Built-in software (Plus/4)
- Slightly faster CPU (~1.76MHz vs 1MHz)

**Plus/4 Disadvantages vs C64:**
- No hardware sprites (major!)
- Much simpler sound (TED vs SID)
- NOT C64-compatible (killed it commercially)
- Smaller software library
- Shorter lifespan (1984-1985)

**Learning Path:**
- C64 → Plus/4 (see design tradeoffs)
- Plus/4 → C64 (understand why C64 succeeded)
- 7501/6502 skills transfer (compatible)

**Same Pattern Library Concepts:**
- 6502/7501 assembly (compatible)
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
- Expected output defined (Plus/4 and C16 where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 7501 Plus/4 games from scratch
- Understands TED chip (121 colours, 8 luminance, 2-channel sound)
- Understands software sprites (no hardware sprites)
- Has 16 portfolio Plus/4/C16 games

**Phase 3 Complete:**
- Student masters advanced TED techniques
- Can compare/contrast Plus/4 (64KB) vs C16 (16KB)
- Understands Plus/4 vs C64 differences
- Has advanced TED versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing Plus/4
- Masters 7501 architecture (6502-compatible)
- Masters TED chip (graphics, sound)
- Can create commercial-release quality games
- Ready for professional Plus/4 development
- **7501/6502 expertise** transfers to C64, VIC-20, PET, Apple II

---

## Resources Required

**Development Tools:**
- Assembler: ca65, ACME, modern cross-assemblers
- Emulator: VICE (Plus/4 support), YAPE (dedicated Plus/4 emulator)
- Graphics: Plus/4 graphics tools (TED-specific)
- Audio: TED sound tools
- Utilities: Disk image tools

**Reference Materials:**
- 7501 instruction set (6502-compatible)
- TED chip reference
- Plus/4 Programmer's Reference Guide
- BASIC 3.5 reference
- Memory maps (64KB Plus/4, 16KB C16)

**Testing:**
- Emulators (development)
- Real Plus/4 hardware (verification, if accessible)
- Real C16 hardware (for 16KB testing)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Advanced TED mastery Phase 3
**Note:** Plus/4 has Phase 0 (BASIC 3.5 - better than C64's 2.0)
**Historical Note:** Commodore's C64 replacement attempt (1984), commercial failure but interesting hardware
**Key Feature:** **121 colours + 8 luminance levels** (more colours than C64!)
**Key Constraint:** **No hardware sprites** (vs C64's 8), **simpler sound** (TED vs SID)
**Critical Issue:** **NOT C64-compatible** (major marketing problem, killed it commercially)
**Next Steps:** Create Plus/4 8-PHASE-GAME-PROGRESSION.md with specific game mapping
