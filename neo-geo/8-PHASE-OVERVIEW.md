# Neo Geo AES/MVS Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Neo Geo base (AES/MVS) → Advanced techniques Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct assembly (no BASIC - console/arcade platform)
**Historical Note:** Arcade-quality home console (1990-2004), **same hardware for arcade and home!**
**Unique Feature:** **MVS = AES** (Multi Video System arcade, Advanced Entertainment System home)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare basic vs arcade-quality implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Sprite management is sprite management" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres (especially fighters, shooters)
- Not recreating specific arcade games (though students learn their techniques)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Neo Geo base (68000, Z80, massive sprites, arcade quality)
- Phase 3: **Advanced Neo Geo mastery** - dual-CPU, all capabilities, arcade techniques
- Phase 4-6: Advanced techniques, pushing Neo Geo limits
- Phase 7: **Maximum Neo Geo** - all capabilities, professional arcade/home quality
- Phase 8: Modern Neo Geo development (homebrew scene)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Neo Geo AES/MVS base (68000 @ 12MHz, Z80 @ 4MHz, massive RAM/VRAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 68000 instruction set fundamentals (16-bit CPU, same as Genesis, Amiga, ST)
- **Dual-CPU architecture:** 68000 (main) + Z80 (sound) - like Genesis!
- **64KB main RAM** (68000's RAM)
- **7KB sound RAM** (Z80's RAM)
- **68KB VRAM** (sprite RAM - massive sprite capacity!)
- **Video System** (custom Neo Geo chipset):
  - 320×224 resolution
  - **380+ sprites** (16×16 to 16×512 pixels - **massive sprite capacity!**)
  - **65,536 colors** (16-bit color - 5 bits R, 6 bits G, 5 bits B - **true color!**)
  - **4096 colors on-screen simultaneously** (from 65,536 palette - arcade quality!)
  - Sprite-based graphics (no tile backgrounds - pure sprite system!)
  - Hardware scaling (zoom in/out, like arcade!)
  - Auto-animation (hardware sprite animation support!)
- **Z80 sound CPU @ 4MHz** (secondary processor for audio)
- **YM2610 ADPCM** (15-channel audio - 7 FM + 4 ADPCM-A + 3 ADPCM-B + 1 PSG):
  - 7 FM synthesis channels (arcade-quality)
  - 4 ADPCM-A channels (short samples)
  - 3 ADPCM-B channels (long samples, voice)
  - 1 PSG channel (simple waveform)
  - **Arcade-quality audio!**
- **Memory card** (save games - 2KB SRAM, cross-game saves!)
- **Joystick:** 4 buttons + D-pad
- **No operating system** (direct hardware programming)
- **MVS (arcade) = AES (home)** - same hardware!
- 59.18Hz refresh rate

**No Autoload - Direct Boot:**
Cartridge inserted = game runs immediately (AES). Arcade coin for MVS.

**Deliverables:** 16 complete, playable Neo Geo games

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Neo Geo AES/MVS (68000 @ 12MHz, Z80 @ 4MHz)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 68000 code (12MHz efficiency - faster than Genesis!)
- **Basic Z80 coordination** (68000 main, Z80 sound - dual-CPU like Genesis)
- Advanced video system programming (380+ sprites, hardware scaling)
- **Massive sprite capacity** (380+ sprites - much more than any console!)
- Sprite animation (hardware auto-animation support)
- Hardware scaling (zoom effects, like arcade)
- **YM2610 ADPCM basics** (15-channel audio - arcade quality)
- Advanced collision detection (sprite-based)
- Multi-screen game structures
- **64KB main RAM + 68KB VRAM + 7KB sound RAM management**
- **Memory card support** (2KB saves, cross-game!)

**Deliverables:** 16 games with commercial-quality Neo Geo features (arcade quality!)

---

### Phase 3: Advanced Neo Geo Mastery (Dual-CPU + Arcade Techniques)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** Neo Geo dual-CPU mastery, arcade-quality techniques
**Complexity:** Direct basic→advanced dual-CPU comparison, arcade mastery
**Games:** 5 revisited from Phases 1-2 with dual-CPU, 3 new showcasing arcade techniques

**Key Learning:**
- **Dual-CPU mastery** (68000 + Z80, like Genesis/C128):
  - 68000 @ 12MHz: Main game logic, graphics, physics
  - Z80 @ 4MHz: Sound CPU, music sequencing, sound effects
  - Bus arbitration (sharing access to audio hardware)
  - 68000↔Z80 communication (command system)
- **YM2610 ADPCM mastery** (15-channel arcade-quality audio!):
  - 7 FM synthesis channels (arcade sound)
  - 4 ADPCM-A channels (short samples, drums, effects)
  - 3 ADPCM-B channels (long samples, voice, music)
  - 1 PSG channel (simple waveform)
  - Z80 sound driver development (complex sequencing)
- **380+ sprites mastery** (massive sprite capacity - **more than any console!**):
  - Sprite management (380+ simultaneous)
  - Hardware scaling (zoom effects)
  - Auto-animation (hardware support)
  - Sprite priority system
- **Direct comparison:** "Here's your basic Neo Geo game. Now add Z80 sound coordination + arcade techniques"
- **Arcade-quality techniques** (fighters, shooters, beat-em-ups)
- Professional dual-CPU architecture
- **MVS vs AES** (arcade vs home - same hardware!)

**Deliverables:** 8 games - 5 dual-CPU versions, 3 new showcasing arcade techniques

**Games Revisited with Dual-CPU:**
1. Snake III (Dual-CPU) - Z80 audio driver, 68000 game logic
2. Shooter III (Dual-CPU) - Z80 sound, 68000 rendering, 380+ sprites!
3. Platformer III (Dual-CPU) - Z80 music, 68000 physics, scaling
4. Fighter I (Dual-CPU) - Z80 audio, 68000 complex animation (genre strength!)
5. One other from Phase 1-2

**New Arcade Technique Games:**
6. Beat-em-up I (showcasing 380+ sprites, dual-CPU, arcade quality)
7. Advanced shooter (bullet hell, massive sprite count)
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Neo Geo dual-CPU (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced 68000 optimization (12MHz maximum efficiency)
- Advanced Z80 sound drivers (complex music, 15-channel mastery)
- Maximum sprite utilization (380+ sprites smooth, arcade quality)
- Advanced YM2610 programming (all 15 channels, arcade audio)
- Hardware scaling mastery (zoom effects, all capabilities)
- Advanced animation (auto-animation, smooth)
- Advanced collision detection (sprite-based, pixel-perfect)
- Isometric projection (sprite-based)
- **Fighting game mechanics** (Neo Geo strength - frame data, combos, special moves)
- **Shooter mechanics** (bullet hell, patterns, arcade quality)

**Deliverables:** 8 games showcasing advanced Neo Geo dual-CPU techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Neo Geo dual-CPU mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (fighter, beat-em-up, shooter, puzzle)

**Key Learning:**
- Large-scale game architecture (arcade quality)
- **Fighting game mastery** (Neo Geo famous for fighters!):
  - Frame data, hitboxes, hurtboxes
  - Combo systems, cancels
  - Special moves, supers
  - Character animation (large sprites!)
  - Arcade-perfect fighting
- **Shooter mastery** (bullet patterns, bosses, arcade quality)
- **Beat-em-up mastery** (multiple characters, scrolling, arcade)
- Advanced YM2610 music composition (15-channel mastery)
- Large game worlds (massive cartridges - 100+MB possible!)
- Memory card saves (2KB SRAM, cross-game)

**Deliverables:** 4 large-scale genre-defining arcade-quality games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Neo Geo (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 380+ simultaneous sprites (maximum arcade quality)
- Complex multi-character systems (fighters, beat-em-ups)
- **Fighting game perfection** (frame-perfect, arcade-perfect)
- Commercial polish techniques (arcade quality)
- Extreme 68000 optimization (12MHz maximum)
- Extreme Z80 sound driver optimization (15-channel maximum)
- Pushing Neo Geo limits (arcade perfection)
- Professional Neo Geo development (arcade/home)

**Deliverables:** 4 games pushing absolute limits of Neo Geo (arcade-perfect!)

---

### Phase 7: Maximum Neo Geo
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Neo Geo (all capabilities, arcade perfection)
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (ultimate fighter, ultimate shooter)

**Key Learning:**
- All video system capabilities (380+ sprites, scaling, animation)
- All YM2610 capabilities (15-channel arcade-quality audio)
- Dual-CPU maximum (68000 + Z80 perfection)
- Large game worlds (massive cartridges, 100+MB)
- Advanced graphics techniques (all sprite capabilities)
- Commercial Neo Geo development (arcade/home quality)
- Professional arcade-quality polish
- **MVS = AES** (arcade and home perfection)

**Deliverables:** 2 commercial-scale Neo Geo games (arcade-perfect quality)

---

### Phase 8: Pinnacle (Modern Homebrew)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Neo Geo development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (fighter, shooter, arcade-perfect)

**Key Learning:**
- Modern Neo Geo development workflow
- Emulator debugging (MAME, FinalBurn Neo, NeoRAINE)
- Modern homebrew techniques
- Modern assemblers/toolchains (NEODEV, modern cross-assemblers)
- Cross-development (modern tools)
- Commercial release preparation (homebrew market, MVS/AES carts)
- Portfolio capstone quality
- **Historical significance:** Arcade-quality home console, same hardware MVS/AES
- **Active homebrew scene** (new arcade/home games still released!)
- **Longevity:** 1990-2004 (14 years official, longer community support)

**Deliverables:** 2 portfolio-ready commercial-quality Neo Geo games (arcade-perfect!)

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 68000 Programming**
- P1: Basic instructions (16-bit RISC, same as Genesis, Amiga, ST)
- P2: Advanced 68000 techniques (12MHz - faster than Genesis!)
- P3: **Dual-CPU coordination** (68000 + Z80, like Genesis/C128)
- P4: Complex 68000 techniques
- P5+: Extreme optimization (12MHz maximum)

**2. Dual-CPU Architecture**
- P3: **68000 + Z80 coordination** (like Genesis!)
- P4: Advanced dual-CPU techniques (optimal workload distribution)
- P5: Complex dual-CPU systems
- P6: Maximum dual-CPU efficiency

**3. Sprite System Programming**
- P1: Sprite basics (380+ sprites available - massive!)
- P2: Advanced sprite management (380+ simultaneous)
- P3: **Maximum sprite mastery** (more than any console!)
- P4: Hardware scaling (zoom effects)
- P5: Auto-animation (hardware support)
- P6: Sprite perfection (arcade quality)

**4. Hardware Scaling**
- P2: Scaling basics (zoom in/out)
- P3: Advanced scaling (all capabilities)
- P5: Scaling mastery (arcade effects)

**5. Sound Programming**
- P1: YM2610 basics (15-channel arcade audio)
- P2: Basic Z80 sound coordination
- P3: **YM2610 mastery** (7 FM + 4 ADPCM-A + 3 ADPCM-B + 1 PSG)
- P4: Advanced sound drivers (Z80, 15-channel sequencing)
- P5: Professional arcade audio (15-channel mastery)
- P6: Audio perfection (arcade quality)

**6. Z80 Sound Drivers**
- P3: **Z80 sound driver development** (dual-CPU coordination)
- P4: Complex sound drivers (15-channel, music + effects)
- P5: Advanced sound drivers (all YM2610 features)
- P6: Professional arcade audio drivers

**7. Fighting Game Mechanics**
- P4: **Fighting game basics** (Neo Geo strength!)
- P5: **Fighting game mastery** (frame data, combos, specials)
- P6: **Fighting game perfection** (arcade-perfect, frame-perfect)
- P7: Ultimate fighters (arcade quality)

**8. Memory Management**
- P1: 64KB main RAM + 68KB VRAM + 7KB sound RAM
- P2: Efficient data structures
- P3: Dual-CPU memory management (shared RAM)
- P5+: Maximum memory efficiency

---

## Hardware Progression

### Neo Geo AES/MVS Base (Phases 1-2)
**Platform:** Neo Geo AES (home) / MVS (arcade) (1990)
**Characteristics:**
- **68000 CPU @ 12MHz** (main CPU, 16-bit - faster than Genesis 7.6MHz!)
- **Z80 CPU @ 4MHz** (sound CPU, 8-bit - dual-CPU, like Genesis!)
- **64KB main RAM** (68000's RAM)
- **7KB sound RAM** (Z80's RAM)
- **68KB sprite RAM** (VRAM - massive sprite capacity!)
- **Custom Video System** (Neo Geo chipset):
  - 320×224 resolution
  - **380+ hardware sprites** (16×16 to 16×512 pixels - **massive!**)
    - 381 sprites max
    - 96 sprites per scanline (no flicker!)
    - Much more than Genesis (80), SNES (128), GBA (128)
  - **65,536 colors** (16-bit true color - 5R 6G 5B)
  - **4096 colors on-screen simultaneously** (from 65,536 - arcade quality!)
  - **Sprite-based system** (no tile backgrounds - pure sprites!)
  - Hardware scaling (zoom in/out, arcade effects)
  - Auto-animation (hardware sprite animation)
  - Sprite priority system
- **YM2610 ADPCM** (15-channel arcade-quality audio!):
  - 7 FM synthesis channels (YM2610 - arcade sound)
  - 4 ADPCM-A channels (short samples, drums, effects)
  - 3 ADPCM-B channels (long samples, voice, music)
  - 1 PSG channel (simple waveform)
  - **Arcade-quality audio!**
- **Memory card:** 2KB SRAM (save games, cross-game saves - innovative!)
- **Joystick:** 4 buttons (A/B/C/D) + D-pad
- **Massive cartridges:** 100+MB possible (vs Genesis/SNES ~4-8MB typical)
- **MVS = AES:** Same hardware for arcade and home (unique!)

**Focus:** Master 68000 and arcade-quality hardware
- 68000 programming (16-bit, same as Genesis, Amiga, ST)
- Dual-CPU architecture (68000 + Z80, like Genesis)
- **380+ sprites** (massive capacity - arcade quality!)
- Hardware scaling (zoom effects)
- YM2610 ADPCM (15-channel arcade audio)
- **Arcade-quality games** (MVS = AES)

**Historical Context:**
- SNK's arcade/home console (1990-2004, 14 years!)
- **MVS (Multi Video System):** Arcade version (multi-game cabinet)
- **AES (Advanced Entertainment System):** Home version (same hardware!)
- **Same hardware arcade/home** (unique - arcade-perfect ports!)
- **Expensive:** $650 AES console (1990 - very expensive!), $200+ games
- **Premium arcade experience** at home (marketing: "Bring the arcade home!")
- **Fighting game powerhouse** (Fatal Fury, Art of Fighting, Samurai Shodown, King of Fighters series)
- **Shooters** (many excellent shmups)
- **Beat-em-ups** (multiple character sprites, smooth)
- Long lifespan (1990-2004 official, longer community)
- **Active homebrew scene** (new games still released!)

**Neo Geo vs Genesis/SNES:**
- **More sprites:** 380+ (vs Genesis 80, SNES 128 - **massive advantage!**)
- **More colors:** 4096 on-screen from 65,536 (vs Genesis 64 from 512, SNES 256 from 32,768)
- **Faster CPU:** 68000 @ 12MHz (vs Genesis 7.6MHz, SNES 3.58MHz)
- **Dual-CPU:** 68000 + Z80 (like Genesis, vs SNES single CPU)
- **Hardware scaling** (vs SNES Mode 7, Genesis limited)
- **15-channel audio** (vs Genesis 10-channel FM+PSG, SNES 8-channel samples)
- **Much more expensive:** $650 console, $200+ games (vs Genesis/SNES ~$150-200 console, $50-70 games)
- **Arcade quality** (MVS = AES - same hardware)
- **Massive cartridges:** 100+MB (vs 4-8MB typical)

**Neo Geo Advantages:**
- **380+ sprites** (more than any console - arcade capacity!)
- **4096 colors on-screen** (arcade quality)
- **Arcade-quality hardware** (MVS = AES)
- **Hardware scaling** (zoom effects)
- **15-channel audio** (YM2610 - arcade sound)
- **Dual-CPU** (68000 + Z80, professional architecture)
- **Massive cartridges** (100+MB - large games)
- **Very active homebrew scene** (new games still made!)

**Neo Geo Disadvantages:**
- **Very expensive:** $650 console, $200+ games (vs $150-200 consoles, $50-70 games)
- **Smaller library:** Fewer games than Genesis/SNES
- **Fighting game focused:** Many fighters, fewer other genres
- **Commercial failure as home console:** Arcade success, home niche

**Why Neo Geo Matters:**
- **Arcade-quality at home** (MVS = AES - unique!)
- **Learning arcade development** (professional arcade techniques)
- **Massive sprite capacity** (380+ - teaches advanced sprite management)
- **Dual-CPU architecture** (like Genesis, professional coordination)
- **Active homebrew scene** (new arcade/home games still released!)

### Advanced Neo Geo (Phase 3+)
**Introduced Phase 3**
**Enhanced Focus:**
- **Dual-CPU mastery** (68000 + Z80, like Genesis)
- **YM2610 mastery** (15-channel arcade audio)
- **380+ sprites mastery** (maximum capacity)
- **Hardware scaling mastery** (zoom effects)
- **Arcade techniques** (fighters, shooters, beat-em-ups)
- Professional arcade/home development

**Focus:** Dual-CPU + arcade mastery
- 68000↔Z80 coordination (optimal workload)
- Z80 sound driver development (15-channel sequencing)
- 380+ sprite management (arcade quality)
- Hardware scaling (all capabilities)
- Fighting game mechanics (frame data, combos, specials)
- Professional arcade development

**Why Dual-CPU + Arcade Mastery Matters:**
- **YM2610:** 15-channel audio (complex, benefits from dedicated Z80)
- **Dual-CPU:** Professional game architecture (like Genesis)
- **Fighting games:** Neo Geo famous for fighters (frame-perfect required)
- **Arcade quality:** Commercial Neo Geo games (MVS/AES perfection)

### Modern Neo Geo (Phase 8)
**Modern enhancements:**
- **MAME** (Multi Arcade Machine Emulator - cycle-accurate)
- **FinalBurn Neo** (excellent Neo Geo emulation)
- **NeoRAINE** (Neo Geo specific emulator)
- Modern assemblers/toolchains (NEODEV, cross-assemblers)
- **Very active homebrew scene** (new MVS/AES games released!)
- NeoSD (modern flash cart, MVS/AES)
- Physical cart releases (homebrew market active!)

**Focus:** Modern workflow
- MAME/FinalBurn Neo debugging
- Modern toolchains
- Homebrew development (MVS/AES)
- Physical cart releases (active market!)
- Portfolio showcase (arcade-quality!)

---

## Spiral Learning Example: Fighter

**Phase 1: Fighter I (Neo Geo base)** (16 lessons)
- Basic fighting mechanics (68000 fundamentals)
- Large character sprites (380+ sprites available!)
- Animation (auto-animation hardware)
- YM2610 basics (15-channel audio)
- 2 characters (player vs opponent)

**Phase 2: Fighter II (Neo Geo optimized)** (32 lessons)
- Optimized 68000 code (12MHz)
- More animation frames (380+ sprites smooth)
- Basic Z80 sound coordination
- YM2610 music (arcade quality)
- Special moves basics

**Phase 3: Fighter III (Dual-CPU + arcade techniques)** (64 lessons - DUAL-CPU MASTERY)
- **68000 + Z80 coordination** (dual-CPU, like Genesis!)
- **Z80 sound driver** (15-channel music + effects sequencing)
- **YM2610 mastery** (7 FM + 4 ADPCM-A + 3 ADPCM-B + 1 PSG - arcade sound!)
- **Frame data** (arcade-perfect timing)
- **Combos, specials** (fighting game mechanics)
- **Direct comparison:** "Here's your basic fighter. Now add Z80 audio + arcade techniques"

**Phase 5: Fighter IV (Fighting game mastery)** (128 lessons)
- **Fighting game perfection** (frame-perfect, hitboxes, hurtboxes)
- **Complex combos, cancels** (arcade mechanics)
- **Character roster** (multiple fighters, 380+ sprites)
- **Z80 sound driver mastery** (complex audio)
- **Arcade-quality** (commercial Neo Geo level)

**Phase 7: Fighter V (Ultimate fighter)** (256 lessons)
- **Arcade-perfect fighter** (commercial quality)
- Maximum characters, moves, stages
- Perfect frame data, timing
- Professional audio (15-channel mastery)
- Neo Geo fighting game perfection

Students see evolution: Neo Geo basics → Optimized → **Dual-CPU + arcade mastery** → Fighting game perfection → Ultimate

---

## Key Differences from Other Platforms

**Neo Geo vs Genesis/SNES:**
- **Many more sprites:** 380+ (vs Genesis 80, SNES 128)
- **More colors:** 4096 on-screen (vs Genesis 64, SNES 256)
- **Faster CPU:** 68000 @ 12MHz (vs Genesis 7.6MHz, SNES 3.58MHz)
- **Dual-CPU:** 68000 + Z80 (like Genesis, vs SNES single)
- **15-channel audio:** YM2610 (vs Genesis 10, SNES 8)
- **Much more expensive:** $650 + $200 games (vs ~$200 + $70)
- **Arcade quality:** MVS = AES (vs home consoles)

**Neo Geo vs Arcade Hardware:**
- **Neo Geo IS arcade hardware** (MVS = AES!)
- Professional arcade development
- Commercial arcade quality
- Same hardware home and arcade (unique!)

**Neo Geo Advantages:**
- **380+ sprites** (arcade capacity, more than any console!)
- **Arcade quality** (MVS = AES - same hardware!)
- **Dual-CPU** (professional architecture)
- **15-channel audio** (arcade sound)
- **Hardware scaling** (zoom effects)
- **Very active homebrew** (new games still made!)
- **Learning arcade development** (professional techniques)

**Learning Path:**
- Genesis → Neo Geo (both dual-CPU: 68000 + Z80)
- Neo Geo → Arcade development (MVS = AES, arcade techniques)
- 68000 skills transfer to Genesis, Amiga, ST, X68000
- Dual-CPU skills transfer to Genesis, C128

**Same Pattern Library Concepts:**
- 68000 assembly (same as Genesis, Amiga, ST, X68000)
- Dual-CPU coordination (like Genesis, C128)
- Collision detection algorithms
- AI pathfinding
- Physics systems
- **Fighting game mechanics** (frame data, combos, hitboxes)
- **Arcade development techniques** (professional quality)
- Game design patterns
- All transferable skills

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (single-CPU and dual-CPU where applicable)
- Verification steps included (arcade-quality standards)

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification (arcade quality)

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 68000 Neo Geo games from scratch
- Understands massive sprite system (380+ sprites)
- Understands YM2610 (15-channel arcade audio)
- Has 16 portfolio Neo Geo games

**Phase 3 Complete:**
- Student masters dual-CPU coordination (68000 + Z80)
- Masters YM2610 (15-channel audio, arcade quality)
- Masters 380+ sprite management (arcade capacity)
- Can create arcade-quality fighting games (Neo Geo strength)
- Has single-CPU and dual-CPU versions of key games
- **Dual-CPU + arcade expertise**

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing Neo Geo (arcade quality!)
- Masters 68000 architecture (transfers to Genesis, Amiga, ST, X68000)
- Masters dual-CPU coordination (68000 + Z80)
- Masters 380+ sprite management (arcade capacity)
- Masters YM2610 (15-channel arcade audio)
- Masters fighting game mechanics (frame data, combos, arcade-perfect)
- Can create commercial-release quality games (MVS/AES arcade quality)
- Ready for professional Neo Geo/arcade homebrew development
- **68000 + dual-CPU + arcade expertise** (professional arcade development!)

---

## Resources Required

**Development Tools:**
- Assembler: NEODEV, modern cross-assemblers (68000 + Z80)
- Emulator: **MAME** (cycle-accurate arcade), **FinalBurn Neo**, NeoRAINE
- Graphics: Sprite editors (Neo Geo format, large sprites)
- Audio: YM2610 tools (FM + ADPCM)
- Utilities: ROM builders (MVS/AES format)

**Reference Materials:**
- 68000 instruction set (main CPU)
- Z80 instruction set (sound CPU)
- Neo Geo Technical Reference (sprite system, video system)
- YM2610 ADPCM reference (15-channel audio - 7 FM + 4 ADPCM-A + 3 ADPCM-B + 1 PSG)
- Dual-CPU coordination reference
- Fighting game development reference (frame data, hitboxes, mechanics)
- MVS/AES hardware reference
- Memory map (64KB main, 68KB sprite, 7KB sound RAM)

**Testing:**
- Emulators (development - MAME/FinalBurn Neo recommended)
- Real Neo Geo hardware (verification - MVS arcade or AES home)
- NeoSD (modern flash cart, MVS/AES)
- Physical cart releases (homebrew market)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Dual-CPU + arcade mastery Phase 3
**Note:** No Phase 0 (console/arcade - no BASIC, direct assembly)
**Historical Note:** Arcade-quality home console (1990-2004), **MVS = AES** (same hardware arcade/home!)
**Unique Features:** **380+ sprites** (arcade capacity!), **dual-CPU** (68000 + Z80), **15-channel audio** (YM2610)
**CPU:** 68000 @ 12MHz (main) + Z80 @ 4MHz (sound) - dual-CPU like Genesis/C128!
**Signature:** **Arcade-quality home console** - MVS (arcade) = AES (home), same hardware!
**Fighting Games:** Neo Geo famous for fighters (Fatal Fury, King of Fighters, Samurai Shodown, Art of Fighting)
**Active Scene:** Very active homebrew scene - new MVS/AES games still released!
**Next Steps:** Create Neo Geo 8-PHASE-GAME-PROGRESSION.md with specific game mapping
