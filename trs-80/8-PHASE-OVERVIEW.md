# TRS-80 Model I/III/4 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Model I/III → Model 4 introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Level II BASIC
**Historical Note:** "1977 trinity" (TRS-80, Apple II, PET), US business/education standard

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare Model I/III vs Model 4 implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Z80 addressing modes are Z80 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres (within TRS-80 graphics constraints)
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Model I/III (16-48KB RAM, Z80 @ 1.77MHz, limited graphics)
- Phase 3: **Model 4 introduced** - 64-128KB RAM, better graphics, revisit games
- Phase 4-6: Advanced techniques, pushing Model 4 limits
- Phase 7: **Model 4 maximum** - CP/M, modern enhancements
- Phase 8: Modern TRS-80 development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** TRS-80 Model I/III (16-48KB RAM, Z80 @ 1.77MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- Z80 instruction set fundamentals
- **Level II BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- Screen memory (video RAM @ $3C00)
- Block graphics (128×48 resolution via 2×3 blocks per character)
- 64×16 character display
- Monochrome only (no color)
- Software sprite rendering (character-based)
- Keyboard input
- **No sound hardware** (silent - cassette port tricks possible)
- Cassette tape storage
- Interrupt timing (60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use Level II BASIC loader:
```basic
10 CLEAR 5000
20 SYSTEM
30 / (machine code at 5001+)
```
Or inline assembly. Professional presentation: CLOAD/RUN from cassette, game starts automatically.

**Deliverables:** 16 complete, playable Model I/III games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Model I/III (16-48KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized Z80 routines (efficient use of registers)
- Block graphics optimization (2×3 character blocks)
- Character animation techniques
- Advanced collision detection (within graphics constraints)
- Multi-screen game structures
- Sound workarounds (cassette port tricks)
- Memory management (48KB efficiently)
- Disk I/O (floppy disk drives)

**Deliverables:** 16 games with commercial-quality Model I/III features

---

### Phase 3: Enhanced Model (Model 4)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **TRS-80 Model 4 introduced** - 64-128KB RAM, better graphics
**Complexity:** Direct Model I/III→Model 4 comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with Model 4, 3 new showcasing enhancements

**Key Learning:**
- **TRS-80 Model 4** (1983, enhanced model)
- **64-128KB RAM** (expandable, much more than Model I/III)
- **Better graphics:** 640×240 monochrome high-resolution mode
- **80×24 text mode** (vs 64×16 on Model I/III)
- **Direct comparison:** "Here's your Model I/III game. Now enhance it with Model 4 graphics"
- Bank switching (128KB models)
- Improved keyboard
- CP/M capability (optional OS)
- Professional Model I/III optimization (for games staying on earlier models)

**Deliverables:** 8 games - 5 enhanced Model 4 versions, 3 new showcasing Model 4

**Games Revisited with Model 4:**
1. Snake III (Model 4) - hi-res graphics, larger display
2. Shooter III (Model 4) - better graphics, smoother
3. Platformer III (Model 4) - hi-res mode, more detail
4. Breakout III (Model 4) - enhanced visuals
5. One other from Phase 1-2

**New Model 4 Games:**
6. Action RPG I (showcasing hi-res graphics + 128KB RAM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Model 4 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced hi-res graphics (640×240 all capabilities)
- Bank switching optimization (128KB)
- Complex sprite systems (hi-res allows detail)
- Sound workarounds advanced (still no sound chip)
- Scrolling techniques (character and pixel-based)
- Disk I/O optimization
- Isometric projection
- Turn-based strategy mechanics
- CP/M programming (optional)

**Deliverables:** 8 games showcasing advanced Model 4 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Model 4 mastery
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
- CP/M utilities (if applicable)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Model 4 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous sprites (hi-res)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme Z80 optimization
- Fast disk loaders (custom routines)
- Pushing Model 4 limits
- Professional TRS-80 development

**Deliverables:** 4 games pushing absolute limits of Model 4

---

### Phase 7: Maximum TRS-80
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Model 4 (maximum capabilities) / modern enhancements
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- Maximum 128KB RAM
- CP/M advanced programming
- Hard drive support (rare but existed)
- Modern TRS-80 expansions
- Large game worlds
- Advanced graphics techniques
- Commercial TRS-80 development

**Deliverables:** 2 commercial-scale Model 4 games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern TRS-80 development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern TRS-80 development workflow
- Emulator debugging (trs80gp, MAME, SDLTRS)
- Modern expansions
- Pushing TRS-80 absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** "1977 trinity", US business/education standard

**Deliverables:** 2 portfolio-ready commercial-quality TRS-80 games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Z80 Programming**
- P1: Basic instructions (same as Spectrum, MSX, CPC)
- P2: Advanced Z80 techniques
- P3: Model 4 optimization (more RAM, better graphics)
- P4: Complex Z80 techniques
- P5+: Extreme optimization

**2. Graphics Programming**
- P1: Block graphics (2×3 blocks, 128×48)
- P2: Character animation, block optimization
- P3: **Model 4 hi-res (640×240)**
- P4: Advanced hi-res techniques
- P5+: Complex graphics systems

**3. Sprite Rendering**
- P1: Character-based sprites (block graphics)
- P2: Optimized character sprites
- P3: Hi-res sprites (Model 4, pixel-level)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Scrolling Systems**
- P1: Screen-aligned only
- P2: Character scrolling
- P3: Pixel scrolling (Model 4 hi-res)
- P4: Advanced scrolling
- P5+: Complex scrolling

**5. Sound Workarounds**
- P1: **Silent** (no sound hardware)
- P2: Cassette port tricks (limited)
- P3: Advanced cassette port techniques
- P4: Creative audio solutions
- Note: TRS-80 has no sound chip (major limitation)

**6. Memory Management**
- P1: Basic RAM (16-48KB Model I/III)
- P2: Efficient data structures
- P3: **Model 4 (64-128KB, banking)**
- P4: Bank switching optimization
- P5+: Large data management

**7. Collision Detection**
- P1: Character-based collision
- P2: Bounding box
- P3: Pixel-perfect (Model 4 hi-res)
- P5+: Multi-layer collision

**8. Disk I/O**
- P2: Basic floppy disk operations
- P3: Model 4 disk I/O
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage

---

## Hardware Progression

### Model I/III (Phases 1-2)
**Platform:** TRS-80 Model I (1977) / Model III (1980)
**Characteristics:**
- Z80 CPU @ 1.77MHz
- 4-48KB RAM (typically 16-48KB)
- **Block graphics:** 128×48 resolution (2×3 blocks per character cell)
- 64×16 character display
- **Monochrome only** (white/green/amber phosphor)
- **No sound hardware**
- Keyboard input
- Cassette tape or floppy disk storage
- 60Hz NTSC

**Focus:** Master Z80 within graphics constraints
- Z80 programming
- Block graphics creativity
- Character-based games
- **No sound** (major constraint)
- **No color** (monochrome only)

**Historical Context:**
- "1977 trinity" (TRS-80, Apple II, PET)
- Very popular in US (business/education)
- Sold ~250,000 Model I units
- Cheaper than Apple II
- Business-oriented

### Model 4 (Phase 3+)
**Platform:** TRS-80 Model 4 (1983)
**Introduced Phase 3**
**Enhanced Features:**
- Same Z80 @ 1.77MHz (optionally 4MHz)
- **64-128KB RAM** (expandable)
- **Hi-res graphics:** 640×240 monochrome
- **80×24 text mode** (vs 64×16)
- Improved keyboard
- **CP/M capable** (alternative OS)
- Still no sound hardware
- **Direct comparison:** Model I/III vs Model 4

**Focus:** Leverage enhanced graphics
- Hi-res 640×240 mode
- More RAM (64-128KB)
- Bank switching
- Better display

### Modern TRS-80 (Phase 7-8)
**Modern enhancements:**
- Emulators (trs80gp, MAME, SDLTRS)
- Modern assemblers
- FreHD (modern hard drive emulation)
- Modern expansions

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Model I/III)** (16 lessons)
- Basic grid movement (Z80 fundamentals)
- Block graphics (128×48)
- Character-based display
- **No sound**
- 16-48KB RAM

**Phase 2: Snake II (Model I/III optimized)** (32 lessons)
- Optimized Z80 code
- Better block graphics
- Character animation
- Multi-screen levels
- Optimized Model I/III

**Phase 3: Snake III (Model 4)** (64 lessons - REVISITED WITH MODEL 4)
- **Hi-res graphics** (640×240)
- **80×24 display**
- **More RAM** (64-128KB)
- **Better visuals**
- **Direct comparison:** "Here's your Model I/III Snake. Now enhance it with Model 4 hi-res"

**Phase 4: Snake IV (Advanced Model 4)** (64 lessons)
- Advanced hi-res graphics
- Bank switching
- Complex game modes
- Disk-based levels

**Phase 6: Snake V (Model 4 limits)** (128 lessons)
- 32+ simultaneous sprites
- Extreme optimization
- Commercial-quality
- Pushing Model 4 limits

Students see evolution: Model I/III basics → Model I/III optimized → **Model 4 enhanced** → Advanced → Professional

---

## Key Differences from Other Platforms

**TRS-80 Advantages:**
- **Historical significance** ("1977 trinity")
- Z80 CPU (well-documented, same as Spectrum/MSX/CPC)
- Model 4 hi-res graphics (640×240, good for monochrome)
- Business/education standard (US)
- Large software library

**TRS-80 Considerations:**
- **No sound hardware** (major limitation)
- **Monochrome only** (no color)
- Limited graphics (Model I/III block graphics)
- More business-oriented (less game-focused)

**Similar To:**
- ZX Spectrum (Z80 CPU)
- Amstrad CPC (Z80 CPU)
- MSX (Z80 CPU)

**Same Pattern Library Concepts:**
- Z80 assembly (identical to Spectrum/MSX/CPC)
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
- Expected output defined (Model I/III and Model 4 where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete Z80 TRS-80 games from scratch
- Understands block graphics (Model I/III)
- Has 16 portfolio Model I/III games
- **Unique skill:** Programming without sound or color

**Phase 3 Complete:**
- Student masters Model 4 hi-res graphics
- Can compare/contrast Model I/III vs Model 4 implementations
- Has both Model I/III and Model 4 versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all TRS-80 models
- Masters Z80 architecture
- Masters TRS-80 graphics (block and hi-res)
- Can create commercial-release quality games
- Ready for professional TRS-80 development
- **Z80 expertise** transfers to Spectrum, MSX, CPC

---

## Resources Required

**Development Tools:**
- Assembler: zmac, z80asm, modern cross-assemblers
- Emulator: trs80gp (excellent), MAME, SDLTRS
- Graphics: TRS-80 graphics editors
- Utilities: Disk image tools

**Reference Materials:**
- Z80 instruction set
- TRS-80 Technical Reference
- Level II BASIC reference
- Model 4 Technical Reference
- Memory maps

**Testing:**
- Emulators (development)
- Real TRS-80 hardware (verification)
- Model 4 (Phase 3+)
- Modern expansions (FreHD, etc.)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Model 4 introduced Phase 3
**Note:** TRS-80 has Phase 0 (Level II BASIC)
**Historical Note:** "1977 trinity" (TRS-80, Apple II, PET), US business/education standard
**Constraint Note:** No sound hardware, monochrome only (creative constraints)
**Next Steps:** Create TRS-80 8-PHASE-GAME-PROGRESSION.md with specific game mapping
