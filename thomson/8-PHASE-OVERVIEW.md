# Thomson MO5/TO7 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** MO5/TO7 → TO7/70 introduced Phase 3 (128KB) → TO8/TO9 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Thomson BASIC
**CPU Note:** **6809 - sophisticated 8-bit architecture** (same as CoCo/Dragon)
**Historical Note:** French educational standard (government mandate), very popular in France

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare MO5/TO7 vs TO7/70 implementations
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
- Phase 1-2: Master MO5/TO7 (48KB RAM, 6809 @ 1MHz)
- Phase 3: **TO7/70 introduced** - 128KB RAM, enhanced graphics, revisit games
- Phase 4-6: Advanced techniques, pushing TO7/70 limits
- Phase 7: **TO8/TO9** - advanced models, modern capabilities
- Phase 8: Modern Thomson development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Thomson MO5/TO7 (48KB RAM, 6809 @ 1MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- **6809 instruction set fundamentals** (sophisticated 8-bit architecture)
- **Thomson BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- Gate Array graphics chip (TO7) or simpler graphics (MO5)
- Screen modes: 320×200, 160×200, 40×25 text
- 16 colors (from palette)
- Software sprite rendering
- Sound: 6-bit DAC (1-bit typically used)
- Keyboard input (AZERTY keyboard - French layout)
- Joystick support
- Cassette tape storage
- Interrupt timing (50Hz PAL)

**Autoload Requirement:**
All games from Lesson 3 onwards must use Thomson BASIC loader:
```basic
10 LOADM"GAME",,R
```
Professional presentation: RUN from tape/disk, game starts automatically.

**Deliverables:** 16 complete, playable MO5/TO7 games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** MO5/TO7 (48KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 6809 code (two accumulators, index registers)
- Advanced graphics programming (gate array)
- Software sprite optimization
- Sound synthesis techniques (DAC)
- Advanced collision detection
- Multi-screen game structures
- Memory management (48KB efficiently)
- BASIC/assembly integration

**Deliverables:** 16 games with commercial-quality MO5/TO7 features

---

### Phase 3: Enhanced Model (TO7/70)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **TO7/70 introduced** - 128KB RAM, enhanced capabilities
**Complexity:** Direct MO5/TO7→TO7/70 comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with TO7/70, 3 new showcasing 128KB

**Key Learning:**
- **TO7/70** (128KB RAM, 2.6× more memory)
- **Enhanced graphics capabilities**
- **Direct comparison:** "Here's your 48KB Snake. Now expand it with TO7/70's 128KB"
- Memory banking (TO7/70)
- Larger game worlds (more RAM for data)
- Better graphics (room for sprite libraries)
- Music and sound effects simultaneously
- Professional MO5/TO7 optimization (for games staying on 48KB)

**Deliverables:** 8 games - 5 enhanced TO7/70 versions, 3 new showcasing 128KB

**Games Revisited with TO7/70:**
1. Snake III (TO7/70) - larger worlds, better graphics
2. Shooter III (TO7/70) - multiple stages, music
3. Platformer III (TO7/70) - larger world, animations
4. Breakout III (TO7/70) - more levels, effects
5. One other from Phase 1-2

**New TO7/70 Games:**
6. Action RPG I (showcasing 128KB RAM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** TO7/70 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced gate array programming
- Complex sprite systems (128KB allows data)
- Advanced sound programming
- Scrolling techniques (character and pixel-based)
- Disk I/O (floppy disk drives)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced TO7/70 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** TO7/70 mastery
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
**Hardware:** TO7/70 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 6809 optimization
- Fast disk loaders (custom routines)
- Pushing TO7/70 limits
- Professional Thomson development

**Deliverables:** 4 games pushing absolute limits of TO7/70

---

### Phase 7: Advanced Models (TO8/TO9)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** TO8/TO9 - advanced Thomson models
**Complexity:** Large-scale games with advanced capabilities
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **TO8/TO9** (1986-1987, advanced models)
- Enhanced graphics capabilities
- Better sound (TO8D has YM2413 FM synthesis)
- 512KB RAM (TO9+)
- Advanced disk systems
- Large game worlds
- Commercial Thomson development

**Deliverables:** 2 commercial-scale Thomson games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Thomson development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern Thomson development workflow
- Emulator debugging (DCMOTO, MAME)
- Modern expansions
- Pushing Thomson absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **6809 mastery:** Understanding sophisticated 8-bit architecture

**Deliverables:** 2 portfolio-ready commercial-quality Thomson games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 6809 Programming**
- P1: Basic instructions (same as CoCo/Dragon)
- P2: Advanced features (two accumulators, index registers)
- P3: TO7/70 optimization (more RAM)
- P4: Complex 6809 techniques
- P5+: Extreme optimization
- **Note:** 6809 same architecture as CoCo/Dragon

**2. Graphics Programming**
- P1: Gate array modes (320×200, etc.)
- P2: Advanced graphics techniques
- P3: TO7/70 graphics (128KB allows more)
- P4: Advanced gate array tricks
- P5+: Complex graphics systems

**3. Sprite Rendering**
- P1: Software sprites
- P2: Optimized sprites (6809 efficient)
- P3: TO7/70 sprites (128KB allows data)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Scrolling Systems**
- P1: Screen-aligned scrolling
- P2: Character scrolling
- P3: Pixel scrolling (TO7/70)
- P4: Complex scrolling
- P5+: Advanced scrolling

**5. Sound Programming**
- P1: 6-bit DAC basics
- P2: Sound synthesis techniques
- P3: TO7/70 audio (music + effects)
- P4: Complex audio
- P7: TO8D FM synthesis (YM2413)

**6. Memory Management**
- P1: Basic RAM (48KB MO5/TO7)
- P2: Efficient data structures
- P3: **TO7/70 (128KB RAM, banking)**
- P4: Efficient banking
- P5+: TO8/TO9 advanced RAM

**7. Collision Detection**
- P1: Bounding box collision
- P2: Pixel-perfect collision
- P3: TO7/70 optimized collision
- P5+: Multi-layer collision

**8. Disk I/O**
- P3: Floppy disk operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage

---

## Hardware Progression

### MO5/TO7 (Phases 1-2)
**Platform:** Thomson MO5 (1984) / TO7 (1982)
**Characteristics:**
- **6809 CPU @ 1MHz** (same as CoCo/Dragon)
- 48KB RAM (MO5), 8-48KB RAM (TO7)
- Gate Array graphics chip (TO7) or simpler (MO5)
- 320×200, 160×200 graphics modes
- 16 colors (from palette)
- 40×25 text mode
- Sound: 6-bit DAC (1-bit typically)
- AZERTY keyboard (French layout)
- Cassette tape storage
- 50Hz PAL

**Focus:** Master 6809 and Thomson graphics
- 6809 architecture (sophisticated 8-bit)
- Gate array graphics
- Software sprite rendering
- French educational standard

**Historical Context:**
- Government mandate (French schools)
- Very popular in France (~500,000 units)
- Rare outside France/French-speaking countries
- Educational focus

### TO7/70 (Phase 3+)
**Platform:** Thomson TO7/70 (1984)
**Introduced Phase 3**
**Enhanced Features:**
- **128KB RAM** (2.6× more than MO5)
- Enhanced graphics capabilities
- Same 6809 @ 1MHz
- Memory banking
- **Direct comparison:** 48KB vs 128KB RAM

**Focus:** Leverage memory expansion
- More room for graphics/sprites
- Larger game worlds
- Music + effects simultaneously
- Professional game development

### TO8/TO9 (Phase 7)
**Platform:** TO8/TO9 (1986-1987)
**Enhanced Features:**
- TO8D: YM2413 FM synthesis (excellent sound)
- 512KB RAM (TO9+)
- Enhanced graphics
- Better disk drives

### Modern Thomson (Phase 8)
**Modern enhancements:**
- DCMOTO emulator (excellent)
- Modern assemblers
- HxC floppy emulator
- SD card interfaces

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (MO5/TO7)** (16 lessons)
- Basic grid movement (6809 fundamentals)
- Gate array graphics
- Software sprites
- DAC sound
- 48KB RAM

**Phase 2: Snake II (MO5/TO7 optimized)** (32 lessons)
- Optimized 6809 code
- Better graphics
- Advanced sound
- Multi-screen levels
- Optimized MO5/TO7

**Phase 3: Snake III (TO7/70)** (64 lessons - REVISITED WITH TO7/70)
- **128KB RAM** (2.6× more memory)
- **Larger playfield**
- **Music + effects**
- **Better graphics**
- **Direct comparison:** "Here's your 48KB Snake. Now expand it with TO7/70"

**Phase 4: Snake IV (Advanced TO7/70)** (64 lessons)
- Advanced graphics
- Memory banking
- Complex audio
- Disk-based levels

**Phase 6: Snake V (TO7/70 limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing TO7/70 limits

Students see evolution: MO5/TO7 basics → MO5/TO7 optimized → **TO7/70 expanded** → Advanced → Professional

---

## Key Differences from Other 6809 Platforms

**Thomson vs CoCo/Dragon:**
- **Same 6809 CPU** @ 1MHz
- **Different graphics:** Gate Array vs MC6847 VDG
- **Different BASIC:** Thomson BASIC vs Extended Color BASIC/Dragon BASIC
- **AZERTY keyboard** (French layout)
- **French market** (government education mandate)
- **Similar architecture** (all 6809-based)

**Thomson Advantages:**
- Government support (French education)
- Gate Array graphics (different from VDG)
- Large French user base
- Educational focus

**Learning Path:**
- Thomson, CoCo, Dragon all share 6809 architecture
- Skills transfer between platforms
- 6809 expertise valuable

**Same Pattern Library Concepts:**
- 6809 assembly (identical to CoCo/Dragon)
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
- Expected output defined (MO5/TO7 and TO7/70 where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6809 Thomson games from scratch
- Understands 6809 architecture
- Understands gate array graphics
- Has 16 portfolio MO5/TO7 games

**Phase 3 Complete:**
- Student masters TO7/70 (128KB RAM)
- Can compare/contrast MO5/TO7 vs TO7/70 implementations
- Has both MO5/TO7 and TO7/70 versions of key games
- **6809 mastery** (sophisticated 8-bit architecture)

**Phase 8 Complete:**
- Student has 60 portfolio games across Thomson variants
- Masters 6809 architecture
- Masters gate array graphics
- Can create commercial-release quality games
- Ready for professional Thomson development
- **6809 expertise** transfers to CoCo, Dragon platforms

---

## Resources Required

**Development Tools:**
- Assembler: LWTOOLS (cross-platform), asm6809
- Emulator: DCMOTO (excellent), MAME
- Graphics: Thomson graphics editors
- Utilities: Disk/tape image tools

**Reference Materials:**
- **6809 instruction set** (same as CoCo/Dragon)
- Gate Array reference
- Thomson Technical Manual
- Thomson BASIC reference
- TO7/70 documentation

**Testing:**
- Emulators (development)
- Real Thomson hardware (verification)
- TO7/70 (Phase 3+)
- TO8/TO9 (Phase 7)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - TO7/70 introduced Phase 3
**Note:** Thomson has Phase 0 (Thomson BASIC)
**CPU Note:** **6809 - same sophisticated architecture as CoCo/Dragon**
**Historical Note:** French educational standard (government mandate), very popular in France
**Next Steps:** Create Thomson 8-PHASE-GAME-PROGRESSION.md with specific game mapping
