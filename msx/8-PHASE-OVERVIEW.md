# MSX Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** MSX1 → MSX2 introduced Phase 3 → MSX2+/Turbo R → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - MSX-BASIC

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare MSX1 vs MSX2 implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Sprite handling is sprite handling" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master MSX1 (TMS9918A VDP, 16 colors)
- Phase 3: **MSX2 introduced** - V9938 VDP, 256 colors, revisit games
- Phase 4-6: Advanced MSX2 techniques, pushing limits
- Phase 7: **MSX2+/Turbo R** - enhanced features
- Phase 8: Modern MSX development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** MSX1 base system
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- Z80 instruction set fundamentals
- **BASIC loader autoload - Lesson 2-3, mandatory from Lesson 3**
- TMS9918A VDP basics (screen modes, pattern table)
- Hardware sprite system (32 sprites, 4 per scanline)
- Color table and name table management
- AY-3-8910/8912 PSG basics (3-voice sound)
- Keyboard/joystick input (via BIOS or direct)
- VRAM access patterns
- Interrupt timing (50Hz PAL / 60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must include efficient BASIC loader:
```basic
10 BLOAD"GAME.BIN",R
```
Or for manual execution control:
```basic
10 BLOAD"GAME.BIN",&HC000:DEFUSR=&HC000:A=USR(0)
```
Professional presentation: RUN"GAME" from disk/cassette, game starts automatically. No manual CALL/USR commands typed by user.

**Deliverables:** 16 complete, playable MSX1 games with professional BASIC autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** MSX1 base system
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized Z80 routines (lookup tables, unrolled loops)
- Sprite multiplexing (>4 sprites per scanline)
- VDP register manipulation (advanced modes)
- Character set animation (pattern table updates)
- Advanced collision detection (sprite collision register)
- PSG music sequencing (3 voices)
- Multi-screen game structures
- BIOS optimization vs direct hardware access

**Deliverables:** 16 games with commercial-quality MSX1 features

---

### Phase 3: Enhanced Graphics (MSX2)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **MSX2 introduced** - V9938 VDP, 256 colors
**Complexity:** Direct MSX1→MSX2 comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with MSX2, 3 new showcasing VDP

**Key Learning:**
- **V9938 VDP programming** (MSX2 graphics chip)
- **Direct comparison:** "Here's your MSX1 Snake. Now enhance it with MSX2's 256 colors"
- Screen modes (Screen 5-8): 256 colors, higher resolutions
- Hardware scrolling registers
- Sprite mode 2 (larger sprites, better handling)
- Enhanced palette control (512 colors available)
- Bitmap graphics modes
- Professional MSX1 optimization (for games staying on MSX1)

**Deliverables:** 8 games - 5 MSX2 versions of earlier games, 3 new showcasing VDP

**Games Revisited with MSX2:**
1. Snake III (MSX2) - 256 colors, hardware scrolling
2. Shooter III (MSX2) - enhanced graphics, larger sprites
3. Platformer III (MSX2) - hardware scrolling, better colors
4. Breakout III (MSX2) - enhanced visuals, bitmap modes
5. One other from Phase 1-2

**New MSX2 Games:**
6. Action RPG I (showcasing Screen 5/8 modes)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** MSX2 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced V9938 programming (all screen modes)
- Complex sprite systems (mode 2 optimization)
- Vertical/horizontal scrolling techniques
- Advanced PSG programming (envelopes, effects)
- Mapper support (MegaROM, various types)
- Disk I/O (MSX-DOS programming)
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced MSX2 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** MSX2 mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced PSG music (tracker format)
- MegaROM banking (large games on cartridge)
- Disk-based save/load systems

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** MSX2 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ sprites smoothly
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme V9938 optimization
- Fast loaders (custom disk access)
- Large MegaROM games (512KB+)
- Professional MSX2 development

**Deliverables:** 4 games pushing absolute limits of MSX2

---

### Phase 7: Enhanced Hardware (MSX2+/Turbo R)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** MSX2+ (V9958 VDP) / MSX Turbo R (R800 CPU)
**Complexity:** Large-scale games with enhanced features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **MSX2+ V9958 VDP** (enhanced scrolling, YJK mode, digitization)
- **MSX Turbo R R800 CPU** (Z80-compatible, much faster)
- Advanced scrolling registers
- YJK color mode (19,268 colors)
- Digitized graphics
- R800 optimization (when available)
- PCM audio (MSX-AUDIO, MSX-MUSIC)
- Large game worlds

**Deliverables:** 2 commercial-scale MSX2+/Turbo R games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern MSX development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern MSX development workflow
- Flash cartridge development (Carnivore2, MegaFlashROM)
- Emulator debugging (openMSX, BlueMSX)
- Pushing MSX absolute limits
- Modern storage (SD cards via interface)
- Commercial release preparation
- Portfolio capstone quality
- Modern MSX community standards (MSXdev)

**Deliverables:** 2 portfolio-ready commercial-quality MSX games showcasing everything learned

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. VDP Programming**
- P1: TMS9918A basics (MSX1 - modes 0-3)
- P2: Advanced TMS9918A techniques
- P3: **V9938 (MSX2) - Screen 5-8, 256 colors**
- P4: Advanced V9938 programming
- P5+: Extreme VDP optimization
- P7: V9958 (MSX2+) - YJK mode, enhanced scrolling

**2. Sprite Management**
- P1: Basic hardware sprites (32 total, 4 per line)
- P2: Sprite multiplexing (>4 per scanline)
- P3: MSX2 sprite mode 2 (larger, better)
- P4: Complex sprite systems (32+ smooth)
- P5+: Maximum sprite optimization
- P7: MSX2+ sprite enhancements

**3. Scrolling Systems**
- P1: Screen-aligned scrolling (character-based)
- P2: Software smooth scrolling
- P3: **MSX2 hardware scrolling**
- P4: Complex scrolling (parallax, multi-directional)
- P5+: Advanced scrolling techniques
- P7: MSX2+ enhanced scrolling registers

**4. Graphics Modes**
- P1: MSX1 modes (Screen 1, 2)
- P2: Advanced MSX1 techniques
- P3: **MSX2 modes (Screen 5-8, bitmap)**
- P4: Mode mixing, advanced techniques
- P5+: Complex graphics systems
- P7: MSX2+ YJK mode (19,268 colors)

**5. Sound Programming**
- P1: Simple PSG effects (AY chip)
- P2: Music sequencing (3 voices)
- P3: Advanced PSG music
- P4: Complex audio (PSG + SCC when available)
- P5+: Tracker music integration
- P7: MSX-AUDIO/MSX-MUSIC (FM synthesis)

**6. Collision Detection**
- P1: Hardware sprite collision register
- P2: Bounding box refinement
- P3: Advanced collision techniques
- P5+: Pixel-perfect collision
- P7: Enhanced collision systems

**7. Memory Management**
- P1: Basic RAM/VRAM usage
- P2: Efficient data structures
- P3: MSX2 expanded RAM
- P4: MegaROM banking (cartridge games)
- P5+: Large game data management
- P6: Extreme optimization

**8. Disk I/O**
- P3: Basic MSX-DOS operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders, optimization
- P8: Modern flash cartridges

---

## Hardware Progression

### MSX1 (Phases 1-2)
**Platform:** MSX1 standard (1983)
**Characteristics:**
- Z80 CPU @ 3.58MHz
- TMS9918A VDP (Video Display Processor)
- Screen 1: 256×192, 16 colors (from fixed palette)
- Screen 2: 256×192, 16 colors (bitmap mode)
- 32 hardware sprites (8×8 or 16×16, 4 per scanline)
- AY-3-8910/8912 PSG (3 voices)
- 8KB-64KB RAM (typically 16KB-64KB)
- Cartridge slot (ROM-based games)
- 50Hz PAL / 60Hz NTSC

**Focus:** Master MSX1 fundamentals
- Z80 programming
- TMS9918A VDP control
- Sprite system (4 per line limit)
- PSG sound
- Creative solutions within constraints

### MSX2 (Phase 3+)
**Platform:** MSX2 standard (1985)
**Introduced Phase 3**
**Characteristics:**
- Z80 CPU @ 3.58MHz (same)
- **V9938 VDP** (enhanced graphics chip)
- Screen 5: 256×212, 16 colors (from 512)
- Screen 6: 512×212, 4 colors (from 512)
- Screen 7: 512×212, 16 colors (from 512)
- Screen 8: 256×212, 256 colors (from 512)
- Hardware scrolling registers
- Sprite mode 2 (better handling)
- 64KB-512KB RAM (typically 64KB-128KB)
- **Direct comparison:** MSX1 vs MSX2 graphics

**Focus:** Leverage enhanced VDP
- 256-color graphics (Screen 8)
- Hardware scrolling
- Better sprite modes
- Higher resolutions
- Backward compatibility

### MSX2+ / Turbo R (Phase 7)
**Platform:** MSX2+ (1988) / MSX Turbo R (1990)
**Enhanced Features:**

**MSX2+:**
- V9958 VDP (enhanced V9938)
- Hardware scrolling (improved)
- YJK color mode (19,268 colors)
- Digitization support

**MSX Turbo R:**
- R800 CPU @ 7.16MHz (Z80-compatible, faster)
- Can switch between R800 and Z80 modes
- V9958 VDP
- PCM audio support

**Focus:** Enhanced capabilities
- YJK graphics mode
- R800 optimization
- Advanced scrolling
- PCM audio

### Modern MSX (Phase 8)
**Modern Development:**
- Emulators (openMSX, BlueMSX, WebMSX)
- Flash cartridges (Carnivore2, MegaFlashROM SCC+)
- Modern assemblers (sjasmplus, Compass, tniASM)
- Modern MSX hardware (1chipMSX, GR8BIT, MSX0)
- SD card interfaces

**Focus:** Modern workflow
- Commercial-quality games
- Modern development tools
- Portfolio showcase
- Community release (MSXdev, itch.io)

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (MSX1)** (16 lessons)
- Basic grid movement (Z80 fundamentals)
- Screen 1 display (256×192, 16 colors)
- Hardware sprites
- PSG sound effects
- MSX1 VDP

**Phase 2: Snake II (MSX1 optimized)** (32 lessons)
- Sprite multiplexing (>4 per line)
- Advanced VDP techniques
- Character animation
- PSG music
- Optimized MSX1

**Phase 3: Snake III (MSX2)** (64 lessons - REVISITED WITH MSX2)
- **Screen 8 mode (256 colors)**
- **Hardware scrolling**
- **V9938 VDP features**
- **Direct comparison:** "Here's your MSX1 Snake. Now enhance it with MSX2."

**Phase 4: Snake IV (Advanced MSX2)** (64 lessons)
- Complex scrolling
- Advanced sprite systems
- MegaROM support
- Disk-based levels

**Phase 6: Snake V (MSX2 limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing MSX2 limits

**Phase 7: Snake Ultimate (MSX2+/Turbo R)** (if applicable)
- YJK color mode
- R800 optimization
- Enhanced features

Students see evolution: MSX1 basics → MSX1 optimized → **MSX2 enhanced** → Advanced → Professional

---

## Key Differences from Other Platforms

**MSX Advantages:**
- Hardware sprites (32 total, unlike Spectrum)
- Standardized platform (many manufacturers)
- Cartridge-based (instant loading)
- International appeal (popular in Japan, Europe, South America)
- Strong community (still active today)

**MSX Considerations:**
- 4 sprites per scanline limit (requires multiplexing)
- VDP VRAM access timing (must respect VDP cycles)
- Z80 @ 3.58MHz (similar to Spectrum)
- Fixed 16-color palette on MSX1
- Less RAM than C64 on early models

**Similar To:**
- ZX Spectrum (Z80 CPU, similar speed)
- Colecovision (same TMS9918A VDP on MSX1)
- Sega SG-1000/SC-3000 (similar hardware)

**Unique Features:**
- Standardized MSX-BIOS (portability across manufacturers)
- Cartridge slot standard (unlike Spectrum)
- V9938/V9958 VDP (powerful graphics chips on MSX2/2+)
- Strong Japanese software library

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
- Expected output defined (MSX1 and MSX2 where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete Z80 MSX games from scratch
- Understands TMS9918A VDP, sprites, PSG sound
- Has 16 portfolio MSX1 games

**Phase 3 Complete:**
- Student masters MSX2 V9938 VDP
- Can compare/contrast MSX1 vs MSX2 implementations
- Has both MSX1 and MSX2 versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all MSX variants
- Masters MSX1, MSX2, MSX2+, and Turbo R
- Can create commercial-release quality games
- Ready for professional MSX development

---

## Resources Required

**Development Tools:**
- Assembler: sjasmplus, Compass, tniASM, asMSX
- Emulator: openMSX (best debugger), BlueMSX, WebMSX
- Graphics: MSXPen, nMSXtiles, Multipaint
- Audio: Arkos Tracker 2, PSG tools
- Utilities: MSXHub tools, disk image tools

**Reference Materials:**
- Z80 instruction set
- TMS9918A VDP reference
- V9938/V9958 VDP reference
- AY-3-8910 PSG reference
- MSX-BIOS reference
- MSX Technical Data Book

**Testing:**
- Emulators (development)
- Real MSX hardware (verification)
- MSX2/2+/Turbo R (phase appropriate)
- Flash cartridges (modern development)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - MSX2 introduced Phase 3
**Note:** MSX has Phase 0 (MSX-BASIC)
**Next Steps:** Create MSX 8-PHASE-GAME-PROGRESSION.md with specific game mapping
