# BBC Micro Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** BBC Model B (32KB) → BBC Master (128KB) introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - BBC BASIC

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare Model B vs Master implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Screen modes are screen modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master BBC Model B (32KB, 6502 @ 2MHz)
- Phase 3: **BBC Master introduced** - 128KB, 65C12, revisit games
- Phase 4-6: Advanced techniques, pushing Master limits
- Phase 7: **BBC Master enhanced features** - advanced 65C12
- Phase 8: Modern BBC development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** BBC Model B (32KB base)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 6502 instruction set fundamentals
- **BASIC inline assembly - Lesson 2-3, mandatory from Lesson 3**
- Screen modes (MODE 0-7, different resolutions/colors)
- Video ULA basics (palette, display timing)
- 6845 CRTC basics (screen control)
- Software sprite rendering
- Keyboard input (INKEY, ADVAL for joystick)
- Sound system (SOUND/ENVELOPE commands, also direct chip access)
- Interrupt timing (50Hz PAL)

**Autoload Requirement:**
All games from Lesson 3 onwards must use efficient BBC BASIC integration:
```basic
10 MODE 1
20 DIM CODE% 1000
30 FOR I%=0 TO 2 STEP 2:P%=CODE%:[OPT I%
40 \ Assembly code here
50 ]:NEXT
60 CALL CODE%
```
Or for pre-assembled code:
```basic
10 *LOAD GAME 8000
20 CALL &8000
```
Professional presentation: *RUN or CHAIN from disk, game starts automatically. No manual CALL commands typed by user.

**Deliverables:** 16 complete, playable games with professional BBC BASIC integration

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** BBC Model B (32KB)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 6502 routines (zero-page, lookup tables)
- Software sprite optimization (pre-shifted, masked)
- Mode switching techniques (different modes per game state)
- Advanced VIA programming (6522 VIA chip - timers, I/O)
- Advanced sound programming (envelopes, effects)
- Multi-screen game structures
- Advanced collision detection
- PAGE variable management (memory protection)

**Deliverables:** 16 games with commercial-quality BBC Model B features

---

### Phase 3: Memory Expansion & Enhanced CPU
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **BBC Master introduced** - 128KB RAM, 65C12 CPU
**Complexity:** Direct Model B→Master comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with Master, 3 new showcasing features

**Key Learning:**
- **BBC Master architecture** (128KB RAM, paged memory)
- **65C12 CPU features** (new instructions, bit manipulation)
- **Direct comparison:** "Here's your Model B Snake. Now expand it with Master's 128KB"
- Memory paging (shadow RAM, sideways RAM)
- Enhanced graphics modes
- Larger game worlds (bank-switched levels)
- Advanced sound (improved synthesis)
- Professional Model B optimization (for games staying on Model B)

**Deliverables:** 8 games - 5 Master versions of earlier games, 3 new showcasing Master

**Games Revisited with Master:**
1. Snake III (Master) - larger worlds, shadow RAM graphics
2. Shooter III (Master) - multiple stages, paged graphics
3. Platformer III (Master) - larger world, bank-switched
4. Breakout III (Master) - more levels, enhanced graphics
5. One other from Phase 1-2

**New Master Games:**
6. Action RPG I (showcasing 128KB memory)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** BBC Master (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Extreme paging optimization
- Advanced CRTC programming (custom screen modes)
- Complex VIA techniques (user port, advanced I/O)
- Tube interface (second processor - optional)
- Disk I/O (ADFS/DFS programming)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced BBC Master techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** BBC Master mastery
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
**Hardware:** BBC Master (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 65C12 optimization
- Fast disk loaders (custom routines)
- Tube co-processor techniques (6502 second processor)
- Professional BBC development

**Deliverables:** 4 games pushing absolute limits of BBC Master

---

### Phase 7: Advanced Hardware Features
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** BBC Master (advanced features) / Master Turbo
**Complexity:** Large-scale games using advanced features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- BBC Master Turbo (4MHz 65C02 option)
- Extreme memory paging techniques
- Advanced CRTC modes (custom timings)
- Second processor optimization (Tube interface)
- Complex disk systems (ADFS networking)
- Teletext mode integration (unique BBC feature)
- Large game worlds
- Commercial BBC development

**Deliverables:** 2 commercial-scale BBC Master games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern BBC development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern BBC development workflow
- Emulator debugging (BeebEm, JSBeeb)
- Pushing BBC absolute limits
- Modern storage (MMB disk images, SD cards)
- Cross-assembler development
- Commercial release preparation
- Portfolio capstone quality
- Modern BBC community standards

**Deliverables:** 2 portfolio-ready commercial-quality BBC games showcasing everything learned

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Screen Mode Management**
- P1: Basic modes (MODE 1, MODE 2)
- P2: Mode switching, custom palettes
- P3: Master shadow RAM (independent graphics)
- P4: Custom CRTC modes
- P5+: Complex mode techniques
- P7: Extreme mode manipulation

**2. Sprite Rendering**
- P1: Simple software sprites (unmasked)
- P2: Masked sprites (AND/OR method)
- P3: Pre-shifted sprites, shadow RAM optimization
- P4: Self-modifying code, extreme optimization
- P5+: Multi-sprite management (32+ sprites)

**3. Scrolling Systems**
- P1: Character scrolling (mode-dependent)
- P2: Pixel scrolling via CRTC
- P3: Shadow RAM double buffering
- P4: Advanced CRTC scrolling
- P5+: Complex scrolling (parallax, multi-directional)

**4. Sound Programming**
- P1: BASIC SOUND command, simple effects
- P2: Direct sound chip access, envelopes
- P3: Advanced synthesis, music
- P4: Complex audio (effects + music)
- P5+: Professional audio techniques

**5. Memory Management**
- P1: Basic RAM usage (32KB Model B)
- P2: PAGE variable, memory protection
- P3: **Master paging (128KB, shadow RAM)**
- P4: Complex paging strategies
- P5+: Large game data management
- P6: Extreme optimization

**6. Collision Detection**
- P1: Tile-based collision
- P2: Bounding box (rectangle overlap)
- P3: Pixel-perfect (check screen memory)
- P5+: Multi-layer collision

**7. Input Handling**
- P1: Keyboard (INKEY)
- P2: Joystick (ADVAL), multiple inputs
- P3: Advanced input techniques
- P4: Custom input systems

**8. Disk I/O**
- P3: Basic DFS/ADFS operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders, custom routines
- P8: Modern disk images (MMB, SD cards)

---

## Hardware Progression

### BBC Model B (Phases 1-2)
**Platform:** BBC Microcomputer Model B (1981)
**Characteristics:**
- 6502 CPU @ 2MHz
- 32KB RAM (Model B standard)
- Video ULA (palette control)
- 6845 CRTC (screen timing, scrolling)
- 8 display modes (different resolution/color trade-offs)
  - MODE 0: 640×256, 2 colors
  - MODE 1: 320×256, 4 colors (common for games)
  - MODE 2: 160×256, 16 colors
  - MODE 4: 320×256, 2 colors (text mode)
  - MODE 7: Teletext (40×25, unique feature)
- Sound: Texas Instruments SN76489 or similar
- 6522 VIA chips (I/O, timers)
- DFS/ADFS (disk filing systems)
- 50Hz PAL

**Focus:** Master BBC Model B fundamentals
- 6502 programming
- Screen mode selection
- Software sprite rendering
- Sound programming
- VIA I/O control
- Creative solutions within 32KB

### BBC Master (Phase 3+)
**Platform:** BBC Master 128 (1986)
**Introduced Phase 3**
**Characteristics:**
- 65C12 CPU @ 2MHz (enhanced 6502)
- 128KB RAM (paged memory)
- Shadow RAM (independent graphics buffer)
- Enhanced graphics modes
- Improved sound capabilities
- Tube interface (second processor support)
- 3.5" disk drive option (ADFS)
- **Direct comparison:** Model B vs Master

**Focus:** Leverage Master enhancements
- 65C12 new instructions
- 128KB paged memory
- Shadow RAM techniques
- Larger game worlds
- Enhanced graphics

### BBC Master Enhanced (Phase 7)
**Additional capabilities:**
- Master Turbo (4MHz 65C02 option)
- Second processor (6502, Z80, or ARM)
- Advanced paging techniques
- Complex disk systems

### Modern Development (Phase 8)
**Modern Tools:**
- Emulators (BeebEm, JSBeeb, B-Em)
- Cross-assemblers (BeebAsm, ca65)
- MMB disk images (multi-disk support)
- SD card interfaces (modern hardware)
- Raspberry Pi co-processor

**Focus:** Modern workflow
- Commercial-quality games
- Modern development tools
- Portfolio showcase
- Community release

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Model B)** (16 lessons)
- Basic grid movement (6502 fundamentals)
- MODE 1 display (320×256, 4 colors)
- Simple sprite rendering
- SOUND effects
- 32KB only

**Phase 2: Snake II (Model B optimized)** (32 lessons)
- Optimized sprite routines
- Advanced sound (envelopes)
- VIA timer techniques
- Multi-screen levels
- Optimized within 32KB

**Phase 3: Snake III (Master)** (64 lessons - REVISITED WITH MASTER)
- **Shadow RAM double buffering**
- **Paged memory for large worlds**
- **65C12 optimization**
- **128KB total**
- **Direct comparison:** "Here's your Model B Snake. Now expand it with Master."

**Phase 4: Snake IV (Advanced Master)** (64 lessons)
- Complex paging techniques
- Advanced CRTC effects
- Disk-based levels
- Advanced sound

**Phase 6: Snake V (Master limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing Master limits

Students see evolution: Model B basics → Model B optimized → **Master expanded** → Advanced → Professional

---

## Key Differences from Other Platforms

**BBC Micro Advantages:**
- Excellent BBC BASIC (inline assembly support)
- 8 display modes (flexibility)
- Educational design (well-documented)
- 6522 VIA chips (versatile I/O)
- Teletext mode (unique feature)
- Tube interface (second processor)

**BBC Micro Considerations:**
- Software sprites (no hardware sprites)
- Limited color in high-resolution modes
- 6502 @ 2MHz (not the fastest)
- Mode 7 Teletext is character-based
- Model B limited to 32KB

**Similar To:**
- Atari 8-bit (6502 family)
- Apple II (6502 CPU, similar architecture)

**Unique Features:**
- BBC BASIC (best BASIC of the era)
- Teletext mode (MODE 7)
- Tube interface (second processor)
- Educational legacy (UK schools standard)

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
- Expected output defined (Model B and Master where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6502 BBC games from scratch
- Understands screen modes, VIA I/O, sound
- Has 16 portfolio Model B games

**Phase 3 Complete:**
- Student masters BBC Master features
- Can compare/contrast Model B vs Master implementations
- Has both Model B and Master versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all BBC variants
- Masters Model B, Master, and enhanced features
- Can create commercial-release quality games
- Ready for professional BBC development

---

## Resources Required

**Development Tools:**
- Assembler: BeebAsm, ca65, inline BBC BASIC
- Emulator: BeebEm (best Windows), JSBeeb (browser), B-Em
- Graphics: BeebSprite, MODE 7 editor
- Audio: Sound editor tools
- Utilities: DFS Explorer, MMB Manager

**Reference Materials:**
- 6502/65C12 instruction set
- BBC Micro Advanced User Guide
- Video ULA reference
- 6845 CRTC reference
- 6522 VIA reference
- BBC BASIC reference

**Testing:**
- Emulators (development)
- Real BBC hardware (verification)
- BBC Master (Phase 3+)
- Modern BBC hardware (enthusiast builds)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - BBC Master introduced Phase 3
**Note:** BBC Micro has Phase 0 (BBC BASIC - widely regarded as the best 8-bit BASIC)
**Next Steps:** Create BBC Micro 8-PHASE-GAME-PROGRESSION.md with specific game mapping
