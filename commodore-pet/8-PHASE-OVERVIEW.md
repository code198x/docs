# Commodore PET Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** PET 2001 → PET 8000 series introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Commodore BASIC 2.0/4.0
**Historical Note:** "1977 trinity" (PET, Apple II, TRS-80), first fully-assembled Commodore computer

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare PET 2001 vs PET 8000 implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "6502 addressing modes are 6502 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres (within PET graphics constraints)
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master PET 2001 (8-32KB RAM, 6502 @ 1MHz, limited graphics)
- Phase 3: **PET 8000 series introduced** - 32-96KB RAM, better graphics, revisit games
- Phase 4-6: Advanced techniques, pushing PET 8000 limits
- Phase 7: **SuperPET** - 6809 second processor, advanced features
- Phase 8: Modern PET development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** PET 2001 (8-32KB RAM, 6502 @ 1MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 6502 instruction set fundamentals
- **Commodore BASIC 2.0 loader - Lesson 2-3, mandatory from Lesson 3**
- Screen memory (video RAM @ $8000)
- 40×25 character display (monochrome, green phosphor)
- PETSCII graphics characters (pseudo-graphics)
- Software sprite rendering (character-based)
- Keyboard input (chiclet keyboard - PET 2001)
- **No sound hardware** (silent - piezo beeper possible)
- Cassette tape storage (built-in)
- Interrupt timing (60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use Commodore BASIC loader:
```basic
10 POKE 1,0
20 SYS 2049
```
Or inline assembly. Professional presentation: LOAD from tape, RUN, game starts automatically.

**Deliverables:** 16 complete, playable PET 2001 games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** PET 2001/4000 (8-32KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 6502 routines (zero-page, efficient addressing)
- PETSCII graphics optimization (pseudo-graphics)
- Character animation techniques
- Advanced collision detection (within graphics constraints)
- Multi-screen game structures
- Sound workarounds (piezo beeper tricks - limited)
- Memory management (32KB efficiently)
- IEEE-488 disk drives (floppy disk)

**Deliverables:** 16 games with commercial-quality PET features

---

### Phase 3: Enhanced Models (PET 8000 series)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **PET 8000 series introduced** - 32-96KB RAM, better graphics
**Complexity:** Direct PET 2001→PET 8000 comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with PET 8000, 3 new showcasing enhancements

**Key Learning:**
- **PET 8000 series** (1981, enhanced models)
- **32-96KB RAM** (much more memory)
- **Better keyboard** (proper keyboard vs chiclet)
- **CRTC chip** (6545 - better display control)
- **80×25 display option** (vs 40×25)
- **Direct comparison:** "Here's your PET 2001 game. Now enhance it with PET 8000 features"
- Bank switching (96KB models)
- Better business graphics (still character-based)
- Professional PET 2001 optimization (for games staying on earlier models)

**Deliverables:** 8 games - 5 enhanced PET 8000 versions, 3 new showcasing PET 8000

**Games Revisited with PET 8000:**
1. Snake III (PET 8000) - more RAM, better display
2. Shooter III (PET 8000) - larger worlds, smoother
3. Platformer III (PET 8000) - better graphics, more detail
4. Breakout III (PET 8000) - enhanced visuals
5. One other from Phase 1-2

**New PET 8000 Games:**
6. Action RPG I (showcasing 96KB RAM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** PET 8000 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced CRTC programming (6545 all capabilities)
- Bank switching optimization (96KB)
- Complex sprite systems (PETSCII graphics optimization)
- Sound workarounds advanced (still very limited)
- Scrolling techniques (character-based)
- IEEE-488 disk I/O optimization
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced PET 8000 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** PET 8000 mastery
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
- Memory management (96KB efficiently)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** PET 8000 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous PETSCII sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 6502 optimization
- Fast disk loaders (IEEE-488)
- Pushing PET 8000 limits
- Professional PET development

**Deliverables:** 4 games pushing absolute limits of PET 8000

---

### Phase 7: SuperPET & Advanced Features
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** SuperPET (6809 second processor) / PET maximum capabilities
**Complexity:** Large-scale games with advanced features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **SuperPET** (1981, 6809 second processor option)
- **6809 programming** (dual-processor system)
- **Waterloo languages** (Pascal, FORTRAN, etc.)
- Dual CPU coordination (6502 + 6809)
- Maximum PET capabilities
- Large game worlds
- Advanced techniques
- Commercial PET development

**Deliverables:** 2 commercial-scale PET games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern PET development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern PET development workflow
- Emulator debugging (VICE, MAME)
- Modern PET expansions
- Pushing PET absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** "1977 trinity", first fully-assembled Commodore

**Deliverables:** 2 portfolio-ready commercial-quality PET games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 6502 Programming**
- P1: Basic instructions (same as C64, VIC-20, Apple II)
- P2: Advanced 6502 techniques
- P3: PET 8000 optimization (more RAM)
- P4: Complex 6502 techniques
- P7: **6809 programming (SuperPET)**

**2. Graphics Programming**
- P1: PETSCII graphics (40×25 character)
- P2: Character animation, pseudo-graphics optimization
- P3: PET 8000 (80×25 option, CRTC)
- P4: Advanced PETSCII techniques
- P5+: Complex graphics systems

**3. Sprite Rendering**
- P1: Character-based sprites (PETSCII)
- P2: Optimized character sprites
- P3: PET 8000 sprites (more RAM for data)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Scrolling Systems**
- P1: Screen-aligned only
- P2: Character scrolling
- P3: CRTC scrolling (PET 8000)
- P4: Advanced scrolling
- P5+: Complex scrolling

**5. Sound Workarounds**
- P1: **Silent** (no sound hardware)
- P2: Piezo beeper tricks (very limited)
- P3: Advanced beeper techniques
- Note: PET has minimal sound capabilities (major limitation)

**6. Memory Management**
- P1: Basic RAM (8-32KB PET 2001/4000)
- P2: Efficient data structures
- P3: **PET 8000 (32-96KB, banking)**
- P4: Bank switching optimization
- P5+: Large data management

**7. Collision Detection**
- P1: Character-based collision
- P2: Bounding box
- P3: Optimized collision (PET 8000)
- P5+: Multi-layer collision

**8. Disk I/O**
- P2: IEEE-488 disk operations (PET unique)
- P3: PET 8000 disk I/O
- P4: Advanced IEEE-488 access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage

---

## Hardware Progression

### PET 2001/4000 (Phases 1-2)
**Platform:** Commodore PET 2001 (1977) / PET 4000 (1980)
**Characteristics:**
- 6502 CPU @ 1MHz
- 4-32KB RAM (typically 8-32KB)
- 40×25 character display
- **Monochrome** (green phosphor typically)
- PETSCII graphics characters (pseudo-graphics)
- **No sound hardware** (piezo beeper possible)
- Chiclet keyboard (PET 2001) or proper keyboard (4000)
- Built-in cassette drive (PET 2001)
- IEEE-488 disk drives (external)
- 60Hz NTSC

**Focus:** Master 6502 within graphics constraints
- 6502 programming
- PETSCII graphics creativity
- Character-based games
- **No sound** (major constraint)
- **No color** (monochrome only)

**Historical Context:**
- "1977 trinity" (PET, Apple II, TRS-80)
- First fully-assembled Commodore computer
- Business/education market
- Led to VIC-20 and C64 development
- Sold ~219,000 PET 2001 units

### PET 8000 series (Phase 3+)
**Platform:** PET 8000 series (1981)
**Introduced Phase 3**
**Enhanced Features:**
- Same 6502 @ 1MHz
- **32-96KB RAM** (expandable)
- **CRTC chip** (6545 - better display control)
- **40×25 or 80×25 display** options
- Proper keyboard
- Better business graphics
- **Direct comparison:** PET 2001 vs PET 8000

**Focus:** Leverage enhanced features
- More RAM (96KB max)
- CRTC display control
- Bank switching
- Better keyboard

### SuperPET (Phase 7)
**Platform:** SuperPET (1981)
**Enhanced Features:**
- **6809 second processor** @ 1MHz
- Dual CPU system (6502 + 6809)
- Waterloo languages (Pascal, FORTRAN, etc.)
- Advanced for its time
- Rare (educational/scientific market)

### Modern PET (Phase 8)
**Modern enhancements:**
- VICE emulator (excellent PET emulation)
- Modern assemblers
- Modern storage solutions

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (PET 2001)** (16 lessons)
- Basic grid movement (6502 fundamentals)
- PETSCII graphics (40×25)
- Character-based display
- **No sound**
- 8-32KB RAM

**Phase 2: Snake II (PET 2001 optimized)** (32 lessons)
- Optimized 6502 code
- Better PETSCII graphics
- Character animation
- Multi-screen levels
- Optimized PET 2001

**Phase 3: Snake III (PET 8000)** (64 lessons - REVISITED WITH PET 8000)
- **More RAM** (32-96KB)
- **CRTC display**
- **80×25 option**
- **Better graphics**
- **Direct comparison:** "Here's your PET 2001 Snake. Now enhance it with PET 8000"

**Phase 4: Snake IV (Advanced PET 8000)** (64 lessons)
- Advanced CRTC techniques
- Bank switching
- Complex game modes
- Disk-based levels

**Phase 6: Snake V (PET 8000 limits)** (128 lessons)
- 32+ simultaneous sprites
- Extreme optimization
- Commercial-quality
- Pushing PET 8000 limits

Students see evolution: PET 2001 basics → PET 2001 optimized → **PET 8000 enhanced** → Advanced → Professional

---

## Key Differences from Other Commodore Platforms

**PET vs C64/VIC-20:**
- **Same 6502 CPU** family
- **No sprites** (character-based only vs C64's hardware sprites)
- **No sound** (vs C64's SID, VIC-20's voices)
- **Monochrome** (vs C64/VIC-20 color)
- **Business-oriented** (vs home/gaming)
- **IEEE-488** (different from C64/VIC-20 serial)
- **Earlier** (1977 vs 1980/1982)

**PET Advantages:**
- Historical significance (1977 trinity)
- Professional keyboard (later models)
- Business/education standard
- Led to C64/VIC-20 development

**Learning Path:**
- PET → VIC-20 → C64 (Commodore evolution)
- 6502 skills transfer directly
- Understanding Commodore history

**Same Pattern Library Concepts:**
- 6502 assembly (identical to C64/VIC-20/Apple II)
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
- Expected output defined (PET 2001 and PET 8000 where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6502 PET games from scratch
- Understands PETSCII graphics
- Has 16 portfolio PET 2001 games
- **Unique skill:** Programming without sound or color

**Phase 3 Complete:**
- Student masters PET 8000 enhancements
- Can compare/contrast PET 2001 vs PET 8000 implementations
- Has both PET 2001 and PET 8000 versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all PET models
- Masters 6502 architecture
- Masters PETSCII graphics
- Can create commercial-release quality games
- Ready for professional PET development
- **6502 expertise** transfers to C64, VIC-20, Apple II

---

## Resources Required

**Development Tools:**
- Assembler: ca65, ACME, modern cross-assemblers
- Emulator: VICE (excellent PET emulation), MAME
- Graphics: PETSCII editors
- Utilities: Disk image tools

**Reference Materials:**
- 6502 instruction set
- PET Programmer's Reference Guide
- CRTC (6545) reference
- Commodore BASIC 2.0/4.0 reference
- Memory maps

**Testing:**
- Emulators (development)
- Real PET hardware (verification)
- PET 8000 (Phase 3+)
- SuperPET (Phase 7, if applicable)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - PET 8000 introduced Phase 3
**Note:** PET has Phase 0 (Commodore BASIC 2.0/4.0)
**Historical Note:** "1977 trinity" (PET, Apple II, TRS-80), first fully-assembled Commodore computer
**Constraint Note:** No sound hardware, monochrome only, character-based graphics
**Next Steps:** Create PET 8-PHASE-GAME-PROGRESSION.md with specific game mapping
