# Texas Instruments TI-99/4A Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** TI-99/4A base → 32KB RAM expansion introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - TI BASIC / Extended BASIC
**CPU Note:** **TMS9900 16-bit CPU** @ 3MHz (unique architecture, not 6502/Z80/6809/68000)
**Historical Note:** Sold 2.8 million units, very popular in US homes/schools

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare base TI-99/4A vs 32KB expansion implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "TMS9900 addressing modes are TMS9900 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master TI-99/4A base (TMS9900 @ 3MHz, 256B CPU RAM, 16KB VDP RAM)
- Phase 3: **32KB RAM expansion introduced** - proper game development, revisit games
- Phase 4-6: Advanced techniques, pushing expanded TI-99/4A limits
- Phase 7: **Geneve 9640** (enhanced TI-compatible, 80s successor)
- Phase 8: Modern TI-99/4A development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** TI-99/4A base (TMS9900 @ 3MHz, 256B CPU RAM, 16KB VDP RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- **TMS9900 instruction set fundamentals** (16-bit architecture, unique)
- **TI BASIC / Extended BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- **Unique architecture:** Only 256 bytes CPU RAM (scratchpad), 16KB VDP RAM
- TMS9918A VDP (Video Display Processor - same as MSX1)
- Screen modes: TEXT (40×24), GRAPHICS I (32×24×16 colors), GRAPHICS II (256×192×16 colors)
- Hardware sprites (32 sprites, 8×8 or 16×16 pixels)
- SN76489 PSG (3 voices + noise)
- Keyboard/joystick input
- Cassette tape or disk storage
- Interrupt timing (60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use TI BASIC/Extended BASIC loader:
```basic
100 CALL INIT :: CALL LOAD(8192,...)
110 CALL LINK("GAME")
```
Professional presentation: OLD CS1 or DSK1, game starts automatically.

**Deliverables:** 16 complete, playable TI-99/4A games within base constraints

**Note:** Phase 1 emphasizes VDP RAM usage (16KB) since CPU RAM is only 256 bytes!

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** TI-99/4A base (256B CPU RAM, 16KB VDP RAM)
**Complexity:** Optimization, creative memory management
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized TMS9900 code (efficient 16-bit operations)
- Creative memory management (256B CPU RAM + 16KB VDP RAM)
- VDP programming (TMS9918A all modes)
- Hardware sprite optimization (32 sprites)
- PSG music programming (3 voices + noise)
- Advanced collision detection (hardware sprite collision)
- Multi-screen game structures
- Cartridge ROM games (common on TI-99/4A)

**Deliverables:** 16 games with commercial-quality features within base constraints

---

### Phase 3: Memory Expansion (32KB RAM)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **TI-99/4A + 32KB RAM expansion introduced** - transforms platform
**Complexity:** Direct base→32KB comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with 32KB, 3 new showcasing expansion

**Key Learning:**
- **32KB RAM expansion** (essential for serious programming, very common)
- **Direct comparison:** "Here's your 256B+16KB Snake. Now expand it with 32KB RAM"
- Proper game development space
- Larger game worlds (room for data)
- Better sprite systems (room for sprite data)
- Music and sound effects simultaneously
- Advanced graphics (room for buffers)
- Professional base TI-99/4A optimization (for games staying on base)

**Deliverables:** 8 games - 5 enhanced 32KB versions, 3 new showcasing expansion

**Games Revisited with 32KB:**
1. Snake III (32KB) - proper playfield, more RAM
2. Shooter III (32KB) - multiple stages, sprite data
3. Platformer III (32KB) - larger world, animations
4. Breakout III (32KB) - more levels, effects
5. One other from Phase 1-2

**New 32KB Games:**
6. Action RPG I (showcasing 32KB space)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** TI-99/4A + 32KB (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced TMS9918A VDP programming
- Maximum sprite utilization (32 sprites smooth)
- Advanced PSG programming (3 voices + noise optimization)
- Complex graphics modes (GRAPHICS II advanced)
- Scrolling techniques (VDP-based)
- Disk I/O (TI disk drives)
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced TI-99/4A techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** TI-99/4A + 32KB mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced PSG music composition
- Disk-based save/load systems
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** TI-99/4A + 32KB (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32 simultaneous sprites (maximum)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme TMS9900 optimization
- Fast disk loaders
- Pushing TI-99/4A limits
- Professional TI-99/4A development

**Deliverables:** 4 games pushing absolute limits of TI-99/4A

---

### Phase 7: Enhanced Hardware (Geneve 9640)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Geneve 9640 (TI-compatible enhanced computer, 1987)
**Complexity:** Large-scale games with enhanced capabilities
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **Geneve 9640** (TI-99/4A compatible, enhanced)
- **TMS9995 CPU** @ 12MHz (faster than TMS9900)
- **512KB RAM** (massive upgrade)
- Enhanced graphics capabilities
- Better keyboard
- TI-99/4A software compatibility
- Large game worlds
- Commercial Geneve development

**Deliverables:** 2 commercial-scale Geneve 9640 games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern TI-99/4A development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern TI-99/4A development workflow
- Emulator debugging (MAME, Classic99)
- Modern TI-99/4A expansions
- Pushing TI-99/4A absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **TMS9900 mastery:** Understanding unique 16-bit architecture

**Deliverables:** 2 portfolio-ready commercial-quality TI-99/4A games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. TMS9900 Programming**
- P1: Basic instructions (16-bit, unique architecture)
- P2: Advanced TMS9900 techniques
- P3: 32KB RAM optimization
- P4: Complex TMS9900 techniques
- P5+: Extreme optimization
- **Note:** TMS9900 completely different from 6502/Z80/6809/68000

**2. Memory Management**
- P1: **EXTREME constraint** (256B CPU RAM + 16KB VDP RAM)
- P2: Creative VDP RAM usage
- P3: **32KB expansion** (transforms development)
- P4: Efficient 32KB usage
- P5+: Large data management

**3. VDP Programming (TMS9918A)**
- P1: Basic modes (TEXT, GRAPHICS I, GRAPHICS II)
- P2: Advanced VDP techniques
- P3: VDP with 32KB RAM backing
- P4: All VDP capabilities
- P5+: Extreme VDP optimization

**4. Sprite Management**
- P1: **Hardware sprites** (32 total, 4 per line)
- P2: Sprite optimization
- P3: 32KB allows more sprite data
- P4: Maximum sprites (32 smooth)
- P5+: Complex sprite systems

**5. Sound Programming**
- P1: SN76489 PSG basics (3 voices + noise)
- P2: Music sequencing
- P3: Advanced PSG (with 32KB)
- P4: Complex audio
- P5+: Professional audio

**6. Graphics Modes**
- P1: GRAPHICS I (32×24×16) and GRAPHICS II (256×192×16)
- P2: Mode optimization
- P3: Advanced graphics (32KB buffers)
- P4: Complex graphics systems
- P5+: Maximum VDP capabilities

**7. Collision Detection**
- P1: Hardware sprite collision
- P2: Bounding box refinement
- P3: Advanced collision (32KB)
- P5+: Multi-layer collision

**8. Disk I/O**
- P3: TI disk drive operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage

---

## Hardware Progression

### TI-99/4A Base (Phases 1-2)
**Platform:** Texas Instruments TI-99/4A (1981)
**Characteristics:**
- **TMS9900 16-bit CPU** @ 3MHz (very fast for era)
- **Only 256 bytes CPU RAM** (scratchpad - extreme constraint!)
- **16KB VDP RAM** (accessed via VDP chip)
- **TMS9918A VDP** (same as MSX1, Colecovision)
- Screen modes: TEXT, GRAPHICS I (32×24×16 colors), GRAPHICS II (256×192×16 colors)
- **32 hardware sprites** (8×8 or 16×16 pixels, 4 per scanline)
- **SN76489 PSG** (3 voices + noise)
- Keyboard (chiclet style) / joystick
- Cassette tape or disk drive
- 60Hz NTSC

**Focus:** Master TMS9900 within extreme constraints
- **TMS9900 16-bit architecture** (unique)
- Creative memory management (256B CPU + 16KB VDP!)
- TMS9918A VDP programming
- Hardware sprites
- PSG sound

**Historical Context:**
- Sold 2.8 million units (successful)
- Very popular in US homes/schools
- Price war with Commodore (eventually lost)
- Strong educational focus

### TI-99/4A + 32KB Expansion (Phase 3+)
**Introduced Phase 3**
**Enhanced with:**
- **32KB RAM expansion** (essential, very common)
- Transforms platform capabilities
- Proper game development possible
- **Direct comparison:** 256B+16KB vs 32KB

**Focus:** Proper development space
- Room for game data
- Sprite libraries
- Music + effects
- Larger worlds
- Professional development

### Geneve 9640 (Phase 7)
**Platform:** Geneve 9640 (1987, third-party TI-compatible)
**Enhanced Features:**
- **TMS9995 CPU** @ 12MHz (4× faster)
- **512KB RAM** (massive upgrade)
- Enhanced graphics
- TI-99/4A software compatible
- Better keyboard

### Modern TI-99/4A (Phase 8)
**Modern enhancements:**
- MAME, Classic99 emulators
- Modern assemblers
- Modern expansions
- Active community

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (TI-99/4A base)** (16 lessons)
- Basic grid movement (TMS9900 fundamentals)
- GRAPHICS I mode (32×24×16 colors)
- Hardware sprites
- PSG sound
- **256B CPU RAM + 16KB VDP RAM** (extreme constraint!)

**Phase 2: Snake II (base optimized)** (32 lessons)
- Optimized TMS9900 code
- Better VDP usage
- PSG music
- Creative memory management
- Optimized base TI-99/4A

**Phase 3: Snake III (32KB expansion)** (64 lessons - REVISITED WITH 32KB)
- **32KB RAM** (transforms development!)
- **Proper game data storage**
- **Larger playfield**
- **Music + effects**
- **Direct comparison:** "Here's your 256B+16KB Snake. Now expand it with 32KB RAM - see the transformation!"

**Phase 4: Snake IV (Advanced 32KB)** (64 lessons)
- Advanced VDP techniques
- Maximum sprites
- Complex PSG music
- Disk-based levels

**Phase 6: Snake V (TI-99/4A limits)** (128 lessons)
- 32 simultaneous sprites (maximum)
- Extreme optimization
- Commercial-quality
- Pushing TI-99/4A limits

Students see evolution: Base extreme constraints → Base optimized → **32KB transformed** → Advanced → Professional

---

## Key Differences from Other Platforms

**TI-99/4A Unique Features:**
- **TMS9900 16-bit CPU** @ 3MHz (not 6502/Z80/6809/68000)
- **Unique architecture:** Only 256B CPU RAM, 16KB VDP RAM
- **TMS9918A VDP** (same as MSX1, excellent graphics)
- **32 hardware sprites** (good for games)
- **SN76489 PSG** (decent 3-voice sound)

**TI-99/4A Considerations:**
- **Extreme memory constraint** (256B CPU RAM base)
- 32KB expansion essential for real games
- Less common than C64/Spectrum internationally
- Primarily US market

**Similar To:**
- MSX1 (same TMS9918A VDP, similar capabilities)
- Colecovision (same VDP)

**Different From Everything Else:**
- **TMS9900 CPU** (completely unique 16-bit architecture)
- Teaches different assembly paradigm
- Not 6502, not Z80, not 6809, not 68000

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
- Expected output defined (base and 32KB where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete TMS9900 TI-99/4A games from scratch
- Understands unique architecture (256B CPU + 16KB VDP)
- Understands TMS9918A VDP
- Has 16 portfolio TI-99/4A base games
- **Unique skill:** TMS9900 16-bit programming

**Phase 3 Complete:**
- Student masters 32KB expansion
- Can compare/contrast base vs 32KB implementations
- Has both base and 32KB versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across TI-99/4A configurations
- Masters TMS9900 architecture
- Masters TMS9918A VDP
- Can create commercial-release quality games
- Ready for professional TI-99/4A development
- **TMS9900 expertise** (unique 16-bit architecture)

---

## Resources Required

**Development Tools:**
- Assembler: TI assembler, modern cross-assemblers
- Emulator: MAME, Classic99 (excellent)
- Graphics: TI graphics editors
- Audio: PSG tools
- Utilities: Disk/tape image tools

**Reference Materials:**
- **TMS9900 instruction set** (unique 16-bit architecture)
- TMS9918A VDP reference
- SN76489 PSG reference
- TI-99/4A Technical Reference
- Extended BASIC reference

**Testing:**
- Emulators (development)
- Real TI-99/4A hardware (verification)
- 32KB expansion (Phase 3+)
- Geneve 9640 (Phase 7, if applicable)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - 32KB RAM expansion introduced Phase 3
**Note:** TI-99/4A has Phase 0 (TI BASIC / Extended BASIC)
**Historical Note:** Sold 2.8 million units, very popular in US homes/schools
**CPU Note:** **TMS9900 16-bit architecture** (completely unique - not 6502/Z80/6809/68000)
**Constraint Note:** Only 256 bytes CPU RAM base (extreme!), 16KB VDP RAM
**Next Steps:** Create TI-99/4A 8-PHASE-GAME-PROGRESSION.md with specific game mapping
