# Commodore VIC-20 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** VIC-20 (5KB) → 32KB expanded introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - VIC BASIC
**Historical Note:** First computer to sell over 1 million units, gateway to C64

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare 5KB vs 32KB implementations
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
- Phase 1-2: Master base VIC-20 (5KB RAM, extreme constraints)
- Phase 3: **32KB expansion introduced** - proper game development, revisit games
- Phase 4-6: Advanced techniques, pushing 32KB VIC-20 limits
- Phase 7: **Maximum VIC-20** - all expansions, modern hardware
- Phase 8: Modern VIC-20 development, Ultimate VIC-20

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** VIC-20 base (5KB RAM - 3.5KB available for BASIC)
**Complexity:** Simple techniques, extreme memory constraints
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 6502 instruction set fundamentals
- **BASIC stub autoload (SYS 4109) - Lesson 2-3, mandatory from Lesson 3**
- Extreme memory management (3.5KB BASIC, even less for ML)
- VIC-I chip basics (graphics, sound, color)
- Screen: 22×23 characters (176×184 pixels)
- 16 colors (like C64)
- Software character/sprite rendering (no hardware sprites)
- 3-voice sound (simpler than SID)
- Joystick input (via VIA chip)
- Interrupt timing (60Hz NTSC / 50Hz PAL)

**Autoload Requirement:**
All games from Lesson 3 onwards must include efficient BASIC stub:
```asm
* = $1001
.byte $0C,$10,$0A,$00,$9E,$20,$34,$31,$30,$39,$00,$00,$00  ; 10 SYS 4109
* = $100D  ; ML code starts here (4109 decimal)
```
Professional presentation: LOAD "*",8,1 then RUN automatically starts game. No manual SYS commands. Minimal bytes used due to RAM constraints.

**Deliverables:** 16 complete, playable games within 5KB constraint (extreme discipline)

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** VIC-20 base (5KB RAM)
**Complexity:** Optimization, extreme memory efficiency
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Extreme 6502 optimization (every byte counts)
- Character-based graphics (creative use of 22×23 screen)
- Self-modifying code (save space)
- VIC-I sound programming (3 voices)
- Advanced collision detection (minimal memory)
- Multi-screen games (clever swapping)
- Lookup table optimization
- Creative solutions within 3.5KB constraints

**Deliverables:** 16 games with commercial-quality features within 5KB RAM

---

### Phase 3: Memory Expansion (32KB)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **VIC-20 + 32KB RAM expansion introduced** - proper development
**Complexity:** Direct 5KB→32KB comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with 32KB, 3 new showcasing expansion

**Key Learning:**
- **32KB RAM expansion** (common cartridge, transforms the platform)
- **Direct comparison:** "Here's your 5KB Snake. Now expand it with 32KB RAM"
- Proper sprite systems (room for data)
- Larger game worlds
- Music and sound effects simultaneously
- Better graphics (room for character sets)
- Hi-res graphics modes (via VIC-I tricks)
- Professional 5KB optimization (for games staying on base VIC-20)

**Deliverables:** 8 games - 5 enhanced 32KB versions, 3 new showcasing expansion

**Games Revisited with 32KB:**
1. Snake III (32KB) - larger playfield, better graphics
2. Shooter III (32KB) - multiple stages, music
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
**Hardware:** VIC-20 + 32KB (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced VIC-I programming (custom character sets, hi-res tricks)
- Complex sprite systems (32KB allows proper data)
- Advanced sound programming (3-voice music)
- Scrolling techniques (character and pixel-based)
- Disk I/O (1541 drive)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced VIC-20 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** VIC-20 + 32KB mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture (within VIC-20 limits)
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced 3-voice music composition
- Disk-based save/load systems
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** VIC-20 + 32KB (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 20+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 6502 optimization
- Fast disk loaders (custom routines)
- Pushing VIC-20 absolute limits
- Professional VIC-20 development

**Deliverables:** 4 games pushing absolute limits of VIC-20

---

### Phase 7: Maximum VIC-20
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** VIC-20 with all expansions + modern hardware
**Complexity:** Large-scale games with maximum capabilities
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- Super expander (hi-res graphics cartridge)
- Music synthesis techniques
- Maximum RAM configurations
- Modern VIC-20 expansions
- Large game worlds
- Advanced VIC-I tricks
- Commercial VIC-20 development

**Deliverables:** 2 commercial-scale VIC-20 games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern VIC-20 development, Ultimate VIC-20
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern VIC-20 development workflow
- Emulator debugging (VICE)
- Ultimate VIC-20 (modern replacement)
- Modern expansions (SD card, etc.)
- Pushing VIC-20 absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** Gateway to C64, first million-selling computer

**Deliverables:** 2 portfolio-ready commercial-quality VIC-20 games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Memory Management**
- P1: Extreme constraints (3.5KB available)
- P2: Every byte optimization
- P3: **32KB expansion** (proper development space)
- P4: Efficient use of 32KB
- P5+: Large game data management

**2. Graphics Rendering**
- P1: Character-based graphics (22×23 screen)
- P2: Creative character manipulation
- P3: Proper sprite data (32KB allows storage)
- P4: Custom character sets, hi-res tricks
- P5+: Advanced graphics systems

**3. Scrolling Systems**
- P1: Screen-aligned scrolling
- P2: Character scrolling
- P3: Pixel scrolling (with 32KB)
- P4: Advanced scrolling techniques
- P5+: Complex scrolling

**4. Sound Programming**
- P1: Simple VIC-I sound (3 voices)
- P2: Creative sound effects
- P3: Music + effects (32KB allows both)
- P4: Advanced 3-voice composition
- P5+: Professional audio

**5. Collision Detection**
- P1: Character-based collision (minimal memory)
- P2: Bounding box (efficient)
- P3: Pixel-perfect (32KB allows complexity)
- P5+: Multi-layer collision

**6. Sprite Management**
- P1: Minimal sprites (memory constraints)
- P2: Optimized sprite routines
- P3: Proper sprite systems (32KB)
- P4: Multi-sprite (20+ sprites)
- P5+: Complex sprite systems

**7. VIC-I Programming**
- P1: Basic VIC-I (screen, color, sound)
- P2: Advanced VIC-I techniques
- P3: Custom character sets
- P4: Hi-res graphics tricks
- P5+: Extreme VIC-I optimization

**8. Disk I/O**
- P3: Basic 1541 operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage (SD cards)

---

## Hardware Progression

### VIC-20 Base (Phases 1-2)
**Platform:** Commodore VIC-20 (1980)
**Characteristics:**
- 6502 CPU @ 1MHz (like C64)
- **5KB RAM** (3.5KB available for BASIC, less for ML)
- VIC-I chip (graphics, sound, color)
- Screen: 22×23 characters (176×184 pixels max)
- 16 colors (same palette as C64)
- **No hardware sprites** (unlike C64)
- 3-voice sound (simpler than C64 SID)
- Cassette or 1541 disk drive
- 60Hz NTSC / 50Hz PAL

**Focus:** Extreme memory discipline
- Every byte counts (3.5KB is TINY)
- Creative graphics within constraints
- Efficient 6502 code
- Character-based games
- Gateway to C64 (same CPU, similar architecture)

**Historical Significance:**
- First computer to sell 1 million units
- Gateway machine (cheaper than C64)
- Introduced millions to programming
- Led directly to C64's design

### VIC-20 + 32KB Expansion (Phase 3+)
**Introduced Phase 3**
**Enhanced with:**
- **32KB RAM expansion** (common cartridge)
- Total 37KB RAM available
- Transforms platform capabilities
- **Direct comparison:** 5KB vs 32KB implementations

**Focus:** Proper game development
- Sprite systems with data
- Larger game worlds
- Music + effects simultaneously
- Better graphics (character set storage)
- Professional game development

### Modern VIC-20 (Phase 7-8)
**Modern enhancements:**
- Ultimate VIC-20 (FPGA replacement)
- Modern RAM expansions
- SD card interfaces
- Super expander (hi-res graphics)
- Modern development tools

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (5KB VIC-20)** (16 lessons)
- Basic grid movement (6502 fundamentals)
- Character-based graphics (22×23 screen)
- Minimal memory usage
- Simple sound
- **Extreme constraint:** Must fit in ~3KB

**Phase 2: Snake II (5KB optimized)** (32 lessons)
- Self-modifying code (space savings)
- Optimized routines
- Better character graphics
- Sound effects
- Still within 5KB

**Phase 3: Snake III (32KB expansion)** (64 lessons - REVISITED WITH 32KB)
- **Proper sprite graphics** (room for sprite data)
- **Larger playfield**
- **Music + effects**
- **Better visuals**
- **Direct comparison:** "Here's your 5KB Snake. Now expand it with 32KB RAM"

**Phase 4: Snake IV (Advanced 32KB)** (64 lessons)
- Custom character sets
- Scrolling playfield
- Advanced music
- Disk-based levels

**Phase 6: Snake V (32KB limits)** (128 lessons)
- 20+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing VIC-20 limits

Students see evolution: 5KB extreme constraints → 5KB optimized → **32KB transformed** → Advanced → Professional

---

## Key Differences from C64

**VIC-20 vs C64:**
- **Less RAM:** 5KB vs C64's 64KB (13× less!)
- **Smaller screen:** 22×23 vs C64's 40×25
- **No hardware sprites:** Software only (C64 has 8)
- **Simpler sound:** 3 voices vs C64's SID (advanced)
- **Same CPU:** 6502 @ 1MHz (identical)
- **Same colors:** 16 colors (same palette)
- **Cheaper:** Gateway machine to C64

**VIC-20 Advantages:**
- Extreme discipline (better programming skills)
- Gateway to C64 (same architecture)
- Historical significance (first million-seller)
- Cult following (active homebrew scene)

**Learning Path:**
- VIC-20 Phase 0-8 → C64 Phase 0-8
- Skills directly transfer
- Understanding constraints improves all coding

**Same Pattern Library Concepts:**
- 6502 assembly (identical to C64)
- Collision detection algorithms
- AI pathfinding
- Physics systems
- Game design patterns
- All transferable to C64 and beyond

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (5KB and 32KB where applicable)
- Verification steps included
- **Memory usage verification:** Must fit within constraints

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification
- **Memory check:** Phases 1-2 must fit in 5KB

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6502 VIC-20 games from scratch
- Understands extreme memory constraints (3.5KB)
- Has 16 portfolio VIC-20 games within 5KB
- **Unique skill:** Programming under extreme constraints

**Phase 3 Complete:**
- Student masters 32KB expansion
- Can compare/contrast 5KB vs 32KB implementations
- Has both 5KB and 32KB versions of key games
- Understands hardware expansion impact

**Phase 8 Complete:**
- Student has 60 portfolio games across all VIC-20 configurations
- Masters 5KB constraints and 32KB development
- Can create commercial-release quality games
- Ready for professional retro development
- **Prepared for C64:** Same CPU, similar architecture, direct path

---

## Resources Required

**Development Tools:**
- Assembler: KickAssembler, ACME, ca65
- Emulator: VICE (VIC-20 mode, excellent debugger)
- Graphics: VIC-20 character editors
- Audio: Sound tools
- Utilities: Memory monitors, disk tools

**Reference Materials:**
- 6502 instruction set (identical to C64)
- VIC-I chip reference
- VIC-20 Programmer's Reference Guide
- Memory maps (5KB and expanded configurations)
- Hardware documentation

**Testing:**
- VICE emulator (development)
- Real VIC-20 hardware (verification)
- 32KB expansion cartridge (Phase 3+)
- Modern expansions (Phase 7-8)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - 32KB expansion introduced Phase 3
**Note:** VIC-20 has Phase 0 (VIC BASIC - gateway language)
**Historical Significance:** First computer to sell over 1 million units, gateway to C64
**Next Steps:** Create VIC-20 8-PHASE-GAME-PROGRESSION.md with specific game mapping
