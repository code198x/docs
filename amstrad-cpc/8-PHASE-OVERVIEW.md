# Amstrad CPC Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** CPC 464 (64KB) → CPC 6128 (128KB) introduced Phase 3 → CPC Plus → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Locomotive BASIC

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare 64KB vs 128KB implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Sprite rendering is sprite rendering" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master CPC 464 (64KB base system)
- Phase 3: **CPC 6128 introduced** - 128KB banking, revisit games
- Phase 4-6: Advanced techniques, pushing 6128 limits
- Phase 7: **CPC Plus** - hardware sprites, enhanced palette
- Phase 8: Modern development (emulators, enhanced features)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** CPC 464 (64KB base)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- Z80 instruction set fundamentals
- **BASIC loader autoload - Lesson 2-3, mandatory from Lesson 3**
- Screen memory addressing (modes 0, 1, 2)
- Gate Array basics (palette control, pen selection)
- CRTC basics (screen timing, display control)
- Software sprite rendering
- Keyboard input (line scanning via Gate Array)
- AY-3-8912 sound basics (3-voice PSG)
- Interrupt timing (50Hz PAL / 60Hz - rare)

**Autoload Requirement:**
All games from Lesson 3 onwards must include efficient BASIC loader:
```basic
10 MEMORY &3FFF:LOAD"GAME.BIN",&4000:CALL &4000
```
Saved as single file. Professional presentation: RUN"GAME" from disk or LOAD "" from tape, game starts automatically. No manual CALL commands typed by user.

**Deliverables:** 16 complete, playable games with professional BASIC autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** CPC 464 (64KB)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized routines (lookup tables, unrolled loops)
- Software sprite optimization (pre-shifted, masked)
- Mode mixing techniques (mode 1 + mode 2)
- Advanced Gate Array programming (palette cycling, raster effects)
- Advanced CRTC programming (hardware scrolling)
- AY music sequencing (3 voices)
- Advanced collision detection
- Multi-screen game structures

**Deliverables:** 16 games with commercial-quality CPC 464 features

---

### Phase 3: Bank Switching & Memory Expansion
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **CPC 6128 introduced** - 128KB RAM with banking
**Complexity:** Direct 64KB→128KB comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with 128KB, 3 new showcasing banking

**Key Learning:**
- **CPC 6128 bank switching** (64KB base + 64KB banked via Gate Array)
- **Direct comparison:** "Here's your 64KB Snake. Now expand it with 128KB banking"
- Memory banking techniques ($7Fxx port control)
- Larger game worlds (bank-switched levels)
- Large sprite/tile libraries in banked RAM
- Advanced screen buffering (double buffering via banks)
- Professional 64KB optimization (for games staying on 464)
- Advanced CRTC effects

**Deliverables:** 8 games - 5 enhanced 6128 versions, 3 new showcasing banking

**Games Revisited with 6128:**
1. Snake III (6128) - more levels, larger playfields
2. Shooter III (6128) - multiple stages, large sprite sets
3. Platformer III (6128) - larger world, bank-switched screens
4. Breakout III (6128) - more levels, advanced graphics
5. One other from Phase 1-2

**New 6128 Games:**
6. Action RPG I (showcasing large world)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** CPC 6128 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Extreme banking optimization
- Complex CRTC tricks (overscan, border removal)
- Advanced Gate Array techniques (palette manipulation)
- Firmware bypassing (direct hardware control)
- Disk I/O (AMSDOS programming)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced CPC 6128 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** CPC 6128 mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced AY music composition (tracker format)
- Disk-based save/load systems
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** CPC 6128 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme CRTC manipulation
- Fast disk loaders (custom routines)
- Cartridge considerations (rare but exists)
- Professional CPC development

**Deliverables:** 4 games pushing absolute limits of CPC 6128

---

### Phase 7: Enhanced Hardware (CPC Plus)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** CPC Plus (464+/6128+) - hardware sprites, enhanced palette
**Complexity:** Large-scale games with enhanced graphics
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- CPC Plus ASIC programming
- Hardware sprites (16 sprites, 16×16 pixels)
- Enhanced palette (4096 colors from 24-bit palette)
- DMA operations (fast memory transfers)
- Programmable Raster Interrupt (PRI)
- Sprite priority and collision detection
- Backward compatibility (6128 vs Plus)
- Large game worlds with enhanced graphics

**Deliverables:** 2 commercial-scale CPC Plus-enhanced games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern development (emulators, enhanced features)
**Complexity:** Modern enhanced development, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern CPC development workflow
- Emulator debugging features
- Pushing CPC absolute limits
- Modern storage (DSK images, HxC floppy emulator)
- Commercial release preparation (itch.io, CPCWiki)
- Portfolio capstone quality
- Cross-platform CPC development (464/664/6128/Plus compatibility)
- Modern CPC community standards

**Deliverables:** 2 portfolio-ready commercial-quality games showcasing everything learned

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Screen Addressing**
- P1: Mode 1/2 basics (character/pixel addressing)
- P2: Mode 0 (low-res, 16 colors)
- P3: Bank-switched screen buffers (6128)
- P4: Advanced CRTC manipulation
- P5+: Complex screen effects
- P7: CPC Plus enhanced modes

**2. Sprite Rendering**
- P1: Simple software sprites (unmasked)
- P2: Masked sprites (AND/OR method)
- P3: Pre-shifted sprites, bank-stored sprite data
- P4: Self-modifying code, extreme optimization
- P5+: Multi-sprite management (32+ sprites)
- P7: Hardware sprites (CPC Plus)

**3. Scrolling Systems**
- P1: Character scrolling (mode 1)
- P2: Pixel scrolling via CRTC
- P3: Bank-switched playfields (large worlds)
- P4: Advanced CRTC scrolling (split-screen)
- P5+: Complex scrolling (parallax, multi-directional)
- P7: Hardware-assisted scrolling (Plus)

**4. Palette Management**
- P1: Basic Gate Array pen/ink selection
- P2: Palette cycling effects
- P3: Bank-switched palettes
- P4: Raster palette changes (mid-frame)
- P5+: Complex palette effects
- P7: Enhanced 4096-color palette (Plus)

**5. Sound Programming**
- P1: Simple AY effects (PSG registers)
- P2: Music sequencing (3 voices)
- P3: Advanced music, envelope control
- P4: Sound effects + music simultaneously
- P5+: Tracker music integration
- P7: Enhanced audio capabilities

**6. Collision Detection**
- P1: Tile-based collision
- P2: Bounding box (rectangle overlap)
- P3: Pixel-perfect (check screen memory)
- P5+: Multi-layer collision
- P7: Hardware sprite collision (Plus)

**7. Memory Management**
- P1: Basic RAM usage (64KB)
- P2: Efficient data structures
- P3: **Bank switching (6128 - 128KB)**
- P4: Complex banking strategies
- P5+: Large game data management
- P6: Extreme optimization

**8. Disk I/O**
- P3: Basic AMSDOS operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders, custom routines
- P8: Modern disk images (DSK format)

---

## Hardware Progression

### CPC 464 Base (Phases 1-2)
**Platform:** Amstrad CPC 464 (1984)
**Characteristics:**
- Z80 CPU @ 4MHz
- 64KB RAM (42KB available for programs typically)
- Gate Array: Palette control, interrupt generation
- CRTC (6845): Display timing, scrolling
- AY-3-8912 PSG: 3 voices, same as Spectrum 128K
- Mode 0: 160×200, 16 colors (from 27)
- Mode 1: 320×200, 4 colors (most games)
- Mode 2: 640×200, 2 colors
- Built-in cassette drive
- 50Hz PAL (60Hz very rare)

**Focus:** Master CPC 464 fundamentals
- Z80 programming
- Gate Array control
- CRTC programming
- Software sprite rendering
- AY sound chip
- Creative solutions within 64KB

### CPC 6128 (Phase 3+)
**Platform:** Amstrad CPC 6128 (1985)
**Introduced Phase 3**
**Characteristics:**
- Same core as 464 but:
- 128KB RAM (64KB base + 64KB banked)
- Bank switching via Gate Array ($7Fxx)
- Built-in 3" disk drive
- **Direct comparison:** 64KB vs 128KB implementations

**Focus:** Leverage memory expansion
- Bank switching techniques
- Larger game worlds
- Large sprite/tile libraries
- Screen buffering
- Disk-based games

### CPC Plus (Phase 7)
**Platform:** CPC 464+/6128+ (1990)
**Enhanced Features:**
- ASIC chip (custom hardware)
- 16 hardware sprites (16×16 pixels)
- Enhanced palette (4096 colors from 24-bit)
- DMA (fast memory transfers)
- Programmable Raster Interrupt (PRI)
- Hardware sprite collision
- Backward compatible with standard CPC
- Cartridge slot

**Focus:** Enhanced graphics capabilities
- Hardware sprites
- 4096-color palette
- DMA operations
- Professional visuals
- Plus-specific techniques

### Modern Development (Phase 8)
**Modern Tools:**
- Emulators (WinAPE, CPCEC, JavaCPC)
- Modern assemblers (RASM, Pasmo, sjasmplus)
- Disk image tools (DSK format)
- HxC floppy emulator (modern hardware)

**Focus:** Modern workflow
- Commercial-quality games
- Modern development tools
- Portfolio showcase
- Community release (CPCWiki, itch.io)

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (CPC 464)** (16 lessons)
- Basic grid movement (Z80 fundamentals)
- Mode 1 display (320×200, 4 colors)
- Simple sprite rendering
- AY sound effects
- 64KB only

**Phase 2: Snake II (CPC 464 optimized)** (32 lessons)
- Optimized sprite routines (pre-shifted)
- Palette cycling effects
- CRTC scrolling playfield
- AY music sequencing
- Optimized within 64KB

**Phase 3: Snake III (CPC 6128)** (64 lessons - REVISITED WITH 128KB)
- **Bank switching for 16+ worlds**
- **Large sprite library in banked RAM**
- **128KB total memory**
- **Direct comparison:** "Here's your 64KB Snake. Now expand it with 6128 banking."

**Phase 4: Snake IV (Advanced 6128)** (64 lessons)
- Complex CRTC effects
- Advanced banking strategies
- Disk-based level sets
- Advanced AY music

**Phase 6: Snake V (6128 limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing 6128 limits

**Phase 7: Snake Ultimate (CPC Plus)** (if applicable)
- Hardware sprites
- 4096-color palette
- DMA graphics
- Plus features

Students see evolution: 64KB basics → 64KB optimized → **128KB expanded** → Advanced → Professional → Plus

---

## Key Differences from Other Platforms

**CPC Advantages:**
- Fast Z80 @ 4MHz (faster than Spectrum 3.5MHz)
- Hardware scrolling (CRTC)
- Better color than Spectrum (27 colors vs 15)
- AY sound chip standard (like Spectrum 128K)
- Built-in disk drive (6128)

**CPC Considerations:**
- Software sprites (no hardware sprites until Plus)
- Mode 1 limited to 4 colors (most games use this)
- Gate Array palette system (different from Spectrum)
- Banking system (6128 only, different from C64/Spectrum 128K)
- Less common platform (smaller community than C64/Spectrum)

**Similar To:**
- ZX Spectrum (Z80 CPU, similar programming model)
- MSX (Z80 CPU, AY sound chip)

**Unique Features:**
- CRTC chip (powerful display control)
- Gate Array (unique palette system)
- 3" disk drive (uncommon format)
- Plus ASIC (hardware sprites, 4096 colors)

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
- Expected output defined (64KB and 128KB where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete Z80 CPC games from scratch
- Understands Gate Array, CRTC, AY sound
- Has 16 portfolio CPC 464 games

**Phase 3 Complete:**
- Student masters 6128 bank switching
- Can compare/contrast 64KB vs 128KB implementations
- Has both 64KB and 128KB versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all CPC variants
- Masters CPC 464, 6128, and Plus
- Can create commercial-release quality games
- Ready for professional CPC development

---

## Resources Required

**Development Tools:**
- Assembler: RASM, Pasmo, sjasmplus (Z80)
- Emulator: WinAPE (best debugger), CPCEC, JavaCPC
- Graphics: ConvImgCpc, Multipaint
- Audio: Arkos Tracker 2 (AY music)
- Utilities: CPCDiskXP, iDSK (disk images)

**Reference Materials:**
- Z80 instruction set
- Gate Array reference
- CRTC (6845) reference
- AY-3-8912 reference
- CPC Plus ASIC reference
- Firmware guide (ROM routines)

**Testing:**
- Emulators (development)
- Real CPC hardware (verification)
- CPC Plus (Phase 7)
- HxC floppy emulator (modern storage)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - 6128 introduced Phase 3
**Note:** CPC has Phase 0 (Locomotive BASIC)
**Next Steps:** Create Amstrad CPC 8-PHASE-GAME-PROGRESSION.md with specific game mapping
