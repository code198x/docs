# Sharp X68000 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** X68000 base → X68000 ACE/EXPERT introduced Phase 3 → X68030 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Human68k BASIC (SX-BASIC)
**Historical Note:** Japanese "arcade at home" (1987-1993), powerful hardware, cult following
**Note:** Primarily Japan market, rare elsewhere

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare base X68000 vs ACE/EXPERT implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Sprite management is sprite management" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific arcade games (though X68000 excelled at arcade ports)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master X68000 base (68000 @ 10MHz, powerful hardware)
- Phase 3: **X68000 ACE/EXPERT introduced** - enhanced models, more RAM, revisit games
- Phase 4-6: Advanced techniques, pushing ACE/EXPERT limits
- Phase 7: **X68030** - 68030 CPU @ 25MHz, maximum performance
- Phase 8: Modern X68000 development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Sharp X68000 base (68000 @ 10MHz, 1-2MB RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 68000 instruction set fundamentals
- **Human68k BASIC (SX-BASIC) loader - Lesson 2-3, mandatory from Lesson 3**
- CRTC graphics controller
- Multiple screen modes (512×512, 1024×1024, various colors)
- Hardware sprites (up to 128 sprites, 16×16 pixels)
- Sprite priority system
- Text/graphics layers (4 layers)
- YM2151 FM synthesis (8 channels, arcade-quality sound)
- ADPCM audio (PCM sample playback)
- Mouse/keyboard/joystick input
- Interrupt timing (variable, 55.5Hz/61.5Hz typical)

**Autoload Requirement:**
All games from Lesson 3 onwards must be Human68k executables (.X files):
- Compiled programs or .X executable format
- Professional presentation: run from command line or desktop, game starts
- Can use SX-BASIC or pure 68000 assembly

**Deliverables:** 16 complete, playable X68000 games with professional presentation

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** X68000 base (68000 @ 10MHz)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 68000 code (efficient addressing modes)
- Hardware sprite optimization (128 sprites max)
- Advanced CRTC programming (multiple layers)
- Scrolling systems (hardware scrolling, 4 layers)
- YM2151 music composition (8-channel FM)
- ADPCM sample playback
- Sprite priority and collision
- Multi-screen game structures
- Memory management (1-2MB efficiently)

**Deliverables:** 16 games with commercial-quality X68000 features

---

### Phase 3: Enhanced Models (X68000 ACE/EXPERT)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **X68000 ACE/EXPERT introduced** - enhanced models, more RAM
**Complexity:** Direct base→ACE/EXPERT comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with ACE/EXPERT, 3 new showcasing enhancements

**Key Learning:**
- **X68000 ACE (1988)** - improved model
- **X68000 EXPERT (1989)** - enhanced version
- **More RAM** (up to 4MB standard, 12MB max)
- **Direct comparison:** "Here's your base X68000 game. Now enhance it with ACE/EXPERT"
- Better graphics capabilities
- Larger sprite libraries (more RAM)
- Larger game worlds
- Professional base X68000 optimization (for games staying on 1-2MB)

**Deliverables:** 8 games - 5 enhanced ACE/EXPERT versions, 3 new showcasing enhancements

**Games Revisited with ACE/EXPERT:**
1. Snake III (ACE/EXPERT) - more sprites, larger worlds
2. Shooter III (ACE/EXPERT) - multiple stages, better graphics
3. Platformer III (ACE/EXPERT) - larger world, more sprites
4. Breakout III (ACE/EXPERT) - enhanced visuals, effects
5. One other from Phase 1-2

**New ACE/EXPERT Games:**
6. Action RPG I (showcasing more RAM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** X68000 ACE/EXPERT (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced CRTC programming (all layers, effects)
- Maximum sprite utilization (128 sprites smooth)
- Advanced YM2151 programming (all channels)
- Complex ADPCM usage
- Scrolling optimization (4-layer parallax)
- Disk I/O (SASI/SCSI hard drives)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced X68000 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** X68000 ACE/EXPERT mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced YM2151 music composition
- SCSI hard drive games (large data)
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** X68000 ACE/EXPERT (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 128 simultaneous sprites (maximum)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 68000 optimization
- Fast SCSI loaders
- Pushing X68000 limits
- "Arcade perfect" quality games

**Deliverables:** 4 games pushing absolute limits of X68000

---

### Phase 7: Maximum Performance (X68030)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Sharp X68030 - 68030 CPU @ 25MHz
**Complexity:** Large-scale games with maximum performance
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **X68030** (1993, 68030 CPU @ 25MHz)
- **Much faster CPU** (2.5× base X68000)
- 68030 optimization techniques
- Cache optimization
- Large game worlds
- Advanced graphics (all capabilities)
- Advanced audio (all channels)
- Commercial X68030 development

**Deliverables:** 2 commercial-scale X68030 games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern X68000 development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern X68000 development workflow
- Emulator debugging (XM6, MAME)
- Pushing X68000/X68030 absolute limits
- Modern storage (SCSI2SD, etc.)
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** Cult following, "arcade at home"

**Deliverables:** 2 portfolio-ready commercial-quality X68000 games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 68000 Programming**
- P1: Basic instructions (same as Amiga, Atari ST)
- P2: Advanced 68000 techniques
- P3: ACE/EXPERT optimization (more RAM)
- P4: Complex 68000 techniques
- P7: **68030 optimization** (cache, faster)

**2. Graphics Programming**
- P1: CRTC basics (multiple layers)
- P2: Advanced CRTC techniques
- P3: ACE/EXPERT graphics (more RAM for data)
- P4: All layer effects
- P5+: Maximum CRTC capabilities

**3. Sprite Management**
- P1: **Hardware sprites (up to 128)**
- P2: Sprite optimization (priority, collision)
- P3: ACE/EXPERT sprites (more data)
- P4: Maximum sprites (128 smooth)
- P5+: Complex sprite systems

**4. Scrolling Systems**
- P1: **Hardware scrolling** (4 layers)
- P2: Multi-layer parallax
- P3: Advanced scrolling (ACE/EXPERT)
- P4: Complex scrolling effects
- P5+: Maximum scrolling techniques

**5. Sound Programming**
- P1: YM2151 FM synthesis basics (8 channels)
- P2: Music composition (FM)
- P3: Advanced YM2151 + ADPCM
- P4: Complex audio (all channels)
- P5+: Professional audio (arcade-quality)

**6. Memory Management**
- P1: Basic RAM (1-2MB)
- P2: Efficient data structures
- P3: **ACE/EXPERT (4-12MB RAM)**
- P4: Large data management
- P7: X68030 maximum RAM

**7. Collision Detection**
- P1: Hardware sprite collision
- P2: Bounding box refinement
- P3: Pixel-perfect collision
- P5+: Multi-layer collision

**8. Disk I/O**
- P3: SASI/SCSI basics
- P4: Advanced disk/hard drive access
- P5: Hard drive-based games
- P6: Fast loaders
- P8: Modern storage (SCSI2SD)

---

## Hardware Progression

### X68000 Base (Phases 1-2)
**Platform:** Sharp X68000 (1987)
**Characteristics:**
- **68000 CPU @ 10MHz** (same family as Amiga/ST, faster)
- 1-2MB RAM (expandable to 4MB)
- **Custom CRTC** (graphics controller)
- Multiple screen modes (512×512, 1024×1024, various colors)
- **128 hardware sprites** (16×16 pixels, priority system)
- **4 graphics/text layers** (independent scrolling)
- **YM2151 FM synthesis** (8 channels, arcade-quality)
- **ADPCM audio** (PCM sample playback)
- Mouse, keyboard, joystick input
- SASI/SCSI hard drive support
- 55.5Hz/61.5Hz refresh

**Focus:** Master powerful X68000 hardware
- 68000 programming
- Hardware sprites (128 max)
- Multi-layer graphics (4 layers)
- FM synthesis (YM2151)
- "Arcade at home" quality

**Historical Context:**
- Primarily Japan market
- "Arcade perfect" ports common
- Powerful for its era
- Cult following (still active)
- Expensive (workstation-class)

### X68000 ACE/EXPERT (Phase 3+)
**Platform:** X68000 ACE (1988) / EXPERT (1989)
**Introduced Phase 3**
**Enhanced Features:**
- Same 68000 @ 10MHz
- **More RAM** (4MB standard, 12MB max)
- Enhanced capabilities
- Better expansion options
- **Direct comparison:** Base vs ACE/EXPERT

**Focus:** Leverage more RAM
- Larger sprite libraries
- Larger game worlds
- More simultaneous graphics

### X68030 (Phase 7)
**Platform:** Sharp X68030 (1993)
**Enhanced Features:**
- **68030 CPU @ 25MHz** (2.5× faster)
- Same custom graphics chips
- Same audio capabilities
- Much faster performance
- Cache optimization critical

**Focus:** Maximum performance
- 68030 optimization
- Extreme speed
- Large-scale games

### Modern X68000 (Phase 8)
**Modern enhancements:**
- XM6 emulator (excellent)
- SCSI2SD (modern storage)
- Modern assemblers
- Active community (Japan)

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (X68000 base)** (16 lessons)
- Basic grid movement (68000 fundamentals)
- Hardware sprites
- Multi-layer graphics
- YM2151 sound
- 1-2MB RAM

**Phase 2: Snake II (X68000 optimized)** (32 lessons)
- Optimized 68000 code
- Better sprite usage
- FM music
- Multi-screen levels
- Optimized X68000

**Phase 3: Snake III (ACE/EXPERT)** (64 lessons - REVISITED WITH ACE/EXPERT)
- **More RAM** (4-12MB)
- **More sprites**
- **Larger worlds**
- **Better graphics**
- **Direct comparison:** "Here's your base X68000 Snake. Now enhance it with ACE/EXPERT"

**Phase 4: Snake IV (Advanced ACE/EXPERT)** (64 lessons)
- 128 sprites (maximum)
- Advanced FM music
- Complex layers
- Hard drive-based levels

**Phase 7: Snake V (X68030)** (if applicable)
- 68030 @ 25MHz
- Extreme speed
- Commercial-quality

Students see evolution: X68000 basics → X68000 optimized → **ACE/EXPERT enhanced** → Advanced → X68030

---

## Key Differences from Other Platforms

**X68000 Advantages:**
- **Very powerful** (workstation-class)
- **128 hardware sprites** (vs Amiga's 8)
- **4 graphics layers** (independent scrolling)
- **YM2151 FM** (arcade-quality, 8 channels)
- **ADPCM audio** (sample playback)
- "Arcade perfect" ports possible
- Cult following (still active)

**X68000 Considerations:**
- Primarily Japan market (rare elsewhere)
- Expensive (workstation pricing)
- Japanese documentation (mostly)
- Smaller software library than Amiga/ST

**Similar To:**
- Amiga (68000 CPU, custom chips)
- Atari ST (68000 CPU)
- Arcade hardware (similar capabilities)

**Same Pattern Library Concepts:**
- 68000 assembly (same as Amiga/ST)
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
- Expected output defined (base and ACE/EXPERT where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 68000 X68000 games from scratch
- Understands powerful X68000 hardware (sprites, layers, FM)
- Has 16 portfolio X68000 games

**Phase 3 Complete:**
- Student masters ACE/EXPERT enhancements
- Can compare/contrast base vs ACE/EXPERT implementations
- Has both base and ACE/EXPERT versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all X68000 variants
- Masters 68000 architecture
- Masters X68000 custom chips (CRTC, YM2151)
- Can create commercial-release quality games
- Ready for professional X68000 development
- **68000 expertise** transfers to Amiga, Atari ST

---

## Resources Required

**Development Tools:**
- Assembler: HAS060, Sharp assembler, modern cross-assemblers
- Emulator: XM6 (excellent), MAME
- Graphics: X68000 graphics tools
- Audio: YM2151 tracker tools
- Utilities: Disk image tools

**Reference Materials:**
- 68000 instruction set
- CRTC reference
- YM2151 FM synthesis reference
- X68000 Technical Manual (Japanese)
- Human68k OS reference

**Testing:**
- Emulators (development)
- Real X68000 hardware (verification)
- X68000 ACE/EXPERT (Phase 3+)
- X68030 (Phase 7)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - ACE/EXPERT introduced Phase 3
**Note:** X68000 has Phase 0 (Human68k BASIC / SX-BASIC)
**Historical Note:** Japanese "arcade at home" (1987-1993), powerful hardware, cult following
**CPU Note:** 68000 @ 10MHz (same family as Amiga/ST, powerful for era)
**Next Steps:** Create X68000 8-PHASE-GAME-PROGRESSION.md with specific game mapping
