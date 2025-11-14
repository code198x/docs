# Game Boy Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Game Boy base → Game Boy Color Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct assembly (no BASIC - console platform)
**Historical Note:** Portable gaming revolution (1989-2003), 118.69M units sold (massive success!)
**Unique Feature:** Portable, monochrome (4 shades), long battery life, massive success

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare Game Boy vs Game Boy Color implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Tile management is tile management" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres (within portable constraints)
- Not recreating specific classic games (though students learn their techniques)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Game Boy base (SM83, 4-shade monochrome, portable constraints)
- Phase 3: **Game Boy Color mastery** - color, more RAM, enhanced features
- Phase 4-6: Advanced techniques, pushing Game Boy limits
- Phase 7: **Maximum Game Boy** - all capabilities, GBC mastery
- Phase 8: Modern Game Boy development (homebrew scene)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Game Boy base (SM83 @ 4.19MHz, 8KB RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- SM83 instruction set fundamentals (Z80-like, Sharp custom - not quite Z80!)
- **8KB work RAM** (WRAM)
- **8KB video RAM** (VRAM)
- **PPU** (Pixel Processing Unit):
  - 160×144 resolution (20×18 tiles, 8×8 each)
  - **Monochrome:** 4 shades of gray (white, light gray, dark gray, black)
  - **40 sprites** (8×8 or 8×16 pixels)
  - Tile-based graphics (8×8 tiles)
  - 2 background layers (Background + Window)
  - Hardware scrolling (smooth, per-pixel)
- **4-channel audio** (2 square wave, 1 programmable wave, 1 noise)
- **Portable:** Battery powered, compact
- D-pad + A/B buttons (select/start)
- **No operating system** (direct hardware programming)
- 59.7Hz refresh rate

**No Autoload - Direct Boot:**
Cartridge inserted = game runs immediately. No loader required.

**Deliverables:** 16 complete, playable Game Boy games

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Game Boy base (SM83 @ 4.19MHz, 8KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized SM83 code (Z80-like optimization, 4.19MHz)
- Advanced PPU programming (tiles, sprites, scrolling)
- **40 sprites optimization** (8×8 or 8×16)
- Sprite multiplexing (more than 40 visible - flicker management)
- Advanced scrolling (background + window, smooth)
- **4-channel audio** programming (square wave, programmable wave, noise)
- Advanced collision detection (software-based)
- Multi-screen game structures
- **8KB RAM management** (efficient data structures)
- **Battery-powered constraints** (optimization for battery life)

**Deliverables:** 16 games with commercial-quality Game Boy features

---

### Phase 3: Game Boy Color Mastery
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Game Boy Color** (color, enhanced features)
**Complexity:** Direct monochrome→color comparison, GBC mastery
**Games:** 5 revisited from Phases 1-2 with GBC, 3 new showcasing GBC features

**Key Learning:**
- **Game Boy Color** (1998, enhanced Game Boy):
  - Same SM83 CPU @ 4.19MHz (or 8.4MHz CGB mode!)
  - **32KB work RAM** (vs 8KB - 4× more!)
  - **16KB video RAM** (vs 8KB - 2× more!)
  - **32,768 colors** (15-bit color - 5 bits each R/G/B)
  - **56 colors on-screen** (from 32,768 palette)
  - **Backward compatible** (plays original Game Boy games!)
  - Infrared port (IR communication)
  - Better screen (backlit on later models)
- **Direct comparison:** "Here's your monochrome game. Now add color with GBC"
- **Color palettes** (background, sprite palettes)
- **Double-speed mode** (8.4MHz vs 4.19MHz)
- **VRAM banking** (2 banks × 8KB)
- Advanced PPU techniques (all GBC capabilities)
- Professional GBC development

**Deliverables:** 8 games - 5 GBC color versions, 3 new showcasing GBC

**Games Revisited with GBC:**
1. Snake III (GBC) - color graphics, more RAM, double-speed
2. Shooter III (GBC) - color, smoother, more enemies
3. Platformer III (GBC) - color, better graphics, more sprites
4. Breakout III (GBC) - color palettes, enhanced effects
5. One other from Phase 1-2

**New GBC Games:**
6. Action RPG I (GBC - color, 32KB RAM, large world)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Game Boy/GBC (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced SM83 optimization (4.19/8.4MHz maximum efficiency)
- Maximum PPU utilization (40 sprites + multiplexing)
- Advanced scrolling (background + window, complex)
- Advanced audio (4-channel mastery)
- **GBC double-speed mode** (8.4MHz optimization)
- **VRAM banking** (2 banks optimization)
- Advanced collision detection
- Isometric projection (portable constraints)
- Turn-based strategy mechanics
- **Battery optimization** (portable power efficiency)

**Deliverables:** 8 games showcasing advanced Game Boy/GBC techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Game Boy/GBC mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture (portable)
- Quest systems and narrative (GBC color, 32KB RAM)
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced audio composition (4-channel mastery)
- Large game worlds (cartridge banking)
- Save systems (battery-backed SRAM)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Game Boy/GBC (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 40+ simultaneous sprites (multiplexing mastery, flicker minimization)
- Complex multi-character systems
- Real-time strategy mechanics (portable)
- Commercial polish techniques
- Extreme SM83 optimization
- Pushing Game Boy limits
- Professional Game Boy development
- GBC maximum capabilities (double-speed, 32KB RAM, color)

**Deliverables:** 4 games pushing absolute limits of Game Boy/GBC

---

### Phase 7: Maximum Game Boy
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Game Boy/GBC (all capabilities)
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (large GBC RPG, grand strategy/adventure)

**Key Learning:**
- All PPU capabilities (monochrome + GBC color)
- All audio capabilities (4-channel mastery)
- GBC maximum (double-speed, 32KB RAM, 56 colors)
- Large game worlds (cartridge banking, SRAM)
- Advanced graphics techniques
- Commercial Game Boy development
- Professional quality polish
- **Portable optimization** (battery life, screen visibility)

**Deliverables:** 2 commercial-scale Game Boy/GBC games

---

### Phase 8: Pinnacle (Modern Homebrew)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Game Boy development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (GBC shooter, GBC platformer)

**Key Learning:**
- Modern Game Boy development workflow
- Emulator debugging (BGB - excellent debugger!, Gambatte, mGBA, SameBoy)
- Modern homebrew techniques
- Modern assemblers (RGBDS - standard for Game Boy!)
- Cross-development (modern tools)
- Commercial release preparation (homebrew market, physical carts)
- Portfolio capstone quality
- **Historical significance:** 118.69M units sold (best-selling handheld until Nintendo DS!)
- **Active homebrew scene** (very active, physical cart releases!)

**Deliverables:** 2 portfolio-ready commercial-quality Game Boy games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. SM83 Programming**
- P1: Basic instructions (Z80-like, Sharp custom)
- P2: Advanced SM83 techniques (Z80-based optimization)
- P3: **GBC double-speed mode** (8.4MHz vs 4.19MHz)
- P4: Complex SM83 techniques
- P5+: Extreme optimization

**2. PPU Programming**
- P1: PPU basics (tiles, sprites, 4-shade monochrome)
- P2: Advanced PPU techniques
- P3: **GBC color** (32,768 colors, 56 on-screen)
- P4: All PPU capabilities
- P5+: Professional PPU programming

**3. Color Programming (GBC)**
- P3: **GBC color introduction** (32,768 colors, palettes)
- P4: Color palette optimization (56 on-screen)
- P5: Advanced color techniques
- P7: Color mastery (all capabilities)

**4. Sprite Management**
- P1: **40 hardware sprites** (8×8 or 8×16)
- P2: Sprite optimization (positioning, priority)
- P3: Advanced sprites (40+ via multiplexing)
- P4: Maximum sprite utilization (flicker minimization)
- P5+: Complex sprite systems

**5. Scrolling Systems**
- P1: **Hardware scrolling** (background + window)
- P2: Multi-layer effects (background + window tricks)
- P3: Advanced scrolling (all techniques)
- P5+: Complex scrolling effects

**6. Sound Programming**
- P1: 4-channel audio basics (2 square, 1 wave, 1 noise)
- P2: Music composition (4-channel)
- P3: Advanced audio (all channels, waveforms)
- P4: Professional audio
- P5+: Audio mastery (commercial quality)

**7. Memory Management**
- P1: 8KB work RAM + 8KB video RAM
- P2: Efficient data structures
- P3: **GBC 32KB RAM + 16KB VRAM** (4× / 2× more!)
- P3: **VRAM banking** (GBC 2 banks × 8KB)
- P5+: Maximum memory efficiency

**8. Portable Optimization**
- P1: Battery efficiency (power-saving techniques)
- P2: Screen visibility (4-shade monochrome optimization)
- P3: GBC screen optimization (color, backlit)
- P5+: Maximum portable optimization

---

## Hardware Progression

### Game Boy Base (Phases 1-2)
**Platform:** Game Boy (1989)
**Characteristics:**
- **SM83 CPU @ 4.19MHz** (Sharp custom - Z80-like, not quite Z80!)
  - Z80-like instruction set (but different!)
  - Some Z80 instructions missing
  - Some unique instructions
  - 8-bit CPU
- **8KB work RAM** (WRAM)
- **8KB video RAM** (VRAM)
- **PPU** (Pixel Processing Unit):
  - 160×144 resolution (20×18 tiles, 8×8 each)
  - **Monochrome:** 4 shades of gray (white, light gray, dark gray, black)
  - **40 hardware sprites** (8×8 or 8×16 pixels)
  - 10 sprites max per scanline (limitation - flicker if exceeded!)
  - Tile-based graphics (8×8 tiles, 256 tiles max in pattern table)
  - 2 layers (Background + Window)
  - Hardware scrolling (per-pixel, smooth)
  - Sprite priority system
- **4-channel audio**:
  - Channel 1: Square wave (sweep)
  - Channel 2: Square wave
  - Channel 3: Programmable wave (custom waveforms!)
  - Channel 4: Noise (white/brown noise)
  - No audio mixing (individual channels)
- **Portable:** AA batteries (15-30 hours typical), compact
- **Reflective LCD screen** (no backlight - needs light!)
- D-pad + A/B buttons + Select/Start
- Cartridge-based (32KB-1MB typical, banking for larger)

**Focus:** Master SM83 and portable constraints
- SM83 programming (Z80-like, Sharp custom)
- PPU tile system (4-shade monochrome, 40 sprites)
- 40 hardware sprites (10 per scanline limit!)
- Hardware scrolling (background + window)
- 4-channel audio (creative composition)
- **Portable constraints** (battery, screen visibility)
- **Monochrome optimization** (4 shades only)

**Historical Context:**
- Portable gaming revolution (1989-2003, 14 years!)
- **118.69 million units sold** (massive success - best-selling handheld until Nintendo DS!)
- Tetris (pack-in - iconic)
- Pokémon Red/Blue (1996 - cultural phenomenon, 31M units!)
- Long battery life (15-30 hours AA batteries)
- Reflective LCD (no backlight - needed light)
- Monochrome (4 shades of gray)
- Beat competitors (Game Gear, Lynx, TurboExpress)
- Revolutionized portable gaming

**Game Boy vs Game Gear:**
- **Better battery:** 15-30 hours (vs Game Gear's 3-5 hours!)
- **More successful:** 118.69M (vs Game Gear's 10.62M)
- **Monochrome:** 4 shades (vs Game Gear color - but battery life mattered more!)
- **Simpler hardware:** SM83 vs Z80 (similar complexity)
- **Cheaper:** Lower price point

**Game Boy Success Factors:**
- Long battery life (critical for portable!)
- Large game library (Tetris, Pokémon, etc.)
- Lower price (vs Game Gear)
- Nintendo brand/marketing
- Monochrome = longer battery (trade-off accepted)

### Game Boy Color (Phase 3+)
**Platform:** Game Boy Color (1998)
**Introduced Phase 3**
**Enhanced Features:**
- Same SM83 CPU @ 4.19MHz (or **8.4MHz double-speed CGB mode!**)
- **32KB work RAM** (vs 8KB - 4× more!)
- **16KB video RAM** (vs 8KB - 2× more, 2 banks!)
- **32,768 colors** (15-bit color - 5 bits each R/G/B)
- **56 colors on-screen** (from 32,768 palette)
  - 8 background palettes (4 colors each = 32)
  - 8 sprite palettes (3 colors each + transparent = 24)
- **Backward compatible** (plays original Game Boy games in color or monochrome!)
- **Infrared port** (IR communication between GBC units)
- Better screen (later models - backlit)
- Color palettes (background, sprite)
- VRAM banking (2 banks × 8KB)
- Double-speed mode (8.4MHz for demanding games)

**Focus:** GBC color + enhancements
- Color programming (32,768 colors, 56 on-screen)
- 32KB RAM (4× more data structures!)
- 16KB VRAM (2 banks, more tiles/sprites)
- Double-speed mode (8.4MHz optimization)
- VRAM banking (2 banks programming)
- Color palette mastery

**Why GBC Matters:**
- Color! (32,768 colors vs monochrome)
- More RAM (32KB vs 8KB - 4× more!)
- More VRAM (16KB vs 8KB - 2× more!)
- Double-speed mode (8.4MHz vs 4.19MHz)
- Backward compatible (entire GB library)
- Pokémon Gold/Silver (1999 - massive GBC success)
- Extended Game Boy lifespan (1998-2003)

### Modern Game Boy (Phase 8)
**Modern enhancements:**
- **BGB** (excellent emulator + debugger - cycle-accurate!)
- Gambatte, mGBA, SameBoy emulators
- **RGBDS** (Rednex Game Boy Development System - standard assembler!)
- Modern toolchains (GB development kits)
- **Very active homebrew scene** (physical cart releases!)
- Everdrive GB/GBC (modern flash carts)
- Analogue Pocket (modern hardware, FPGA)

**Focus:** Modern workflow
- BGB debugging (excellent!)
- RGBDS assembly (standard)
- Homebrew development
- Physical cart releases (active market!)
- Portfolio showcase

---

## Spiral Learning Example: Platformer

**Phase 1: Platformer I (Game Boy base)** (16 lessons)
- Basic platforming (SM83 fundamentals, Z80-like)
- Monochrome graphics (4 shades)
- Tile-based backgrounds (8×8 tiles)
- Player/enemy sprites (40 sprites, 10 per scanline)
- 4-channel audio (square wave + noise)

**Phase 2: Platformer II (Game Boy optimized)** (32 lessons)
- Optimized SM83 code (Z80-like optimization)
- Better monochrome graphics (4-shade optimization)
- Smooth scrolling (background + window)
- Sprite multiplexing (more than 10 per scanline, flicker management)
- 4-channel music (composition)

**Phase 3: Platformer III (GBC color!)** (64 lessons - GBC INTRODUCED)
- **32,768 colors!** (vs monochrome 4 shades)
- **56 colors on-screen** (palettes)
- **32KB RAM** (vs 8KB - 4× more!)
- **Double-speed mode** (8.4MHz vs 4.19MHz - smoother!)
- **Direct comparison:** "Here's your monochrome platformer. Now add color with GBC!"

**Phase 4: Platformer IV (Advanced GBC)** (64 lessons)
- Advanced color palettes (56 colors optimization)
- Double-speed mode optimization (8.4MHz)
- VRAM banking (2 banks, more graphics)
- 32KB RAM (complex game logic)

**Phase 6: Platformer V (GB/GBC limits)** (128 lessons)
- Maximum sprites (40+ smooth, flicker minimized)
- Extreme optimization
- Commercial-quality (Super Mario Land level)
- Pushing Game Boy limits

Students see evolution: GB monochrome basics → Optimized → **GBC color enhanced** → Advanced → Professional

---

## Key Differences from Other Platforms

**Game Boy vs Game Gear:**
- **Better battery:** 15-30 hours (vs Game Gear 3-5 hours - critical!)
- **More successful:** 118.69M (vs Game Gear 10.62M)
- **Monochrome** base (vs Game Gear color - but battery mattered!)
- **GBC color** later (32,768 vs Game Gear's colors)
- **Similar CPU:** SM83 vs Z80 (related architectures)

**Game Boy vs Console Competition:**
- **Portable!** (vs home consoles - different market)
- **Battery powered** (vs AC power)
- **Lower specs** (vs SNES/Genesis - but portable!)
- **Massive success** (118.69M units - handheld revolution)

**Game Boy Advantages:**
- **Portability** (play anywhere!)
- **Long battery life** (15-30 hours AA batteries)
- **Massive game library** (Tetris, Pokémon, Mario, Zelda, etc.)
- **Lower price** (vs competitors)
- **GBC backward compatible** (entire GB library)
- **Very active homebrew scene** (still very active!)

**Learning Path:**
- Game Boy → GBA (Nintendo portable evolution, SM83 → ARM)
- SM83 → Z80 family (related architectures, skills transfer)
- Portable constraints → optimization skills (battery, screen, size)

**Same Pattern Library Concepts:**
- SM83 assembly (Z80-like, skills transfer to Z80 family)
- Collision detection algorithms
- AI pathfinding
- Physics systems
- Game design patterns
- Portable optimization (battery, screen)
- All transferable skills

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (GB monochrome and GBC color where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete SM83 Game Boy games from scratch
- Understands PPU (4-shade monochrome, 40 sprites, tile system)
- Understands 4-channel audio
- **Masters portable constraints** (battery, screen visibility)
- Has 16 portfolio Game Boy games

**Phase 3 Complete:**
- Student masters GBC color (32,768 colors, 56 on-screen)
- Masters GBC enhancements (32KB RAM, double-speed, VRAM banking)
- Can compare/contrast GB monochrome vs GBC color implementations
- Has both GB and GBC versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing Game Boy/GBC
- Masters SM83 architecture (Z80-like, skills transfer)
- Masters PPU (monochrome + GBC color, all capabilities)
- Masters portable optimization (battery, screen)
- Masters 4-channel audio
- Can create commercial-release quality games
- Ready for professional Game Boy homebrew development
- **SM83/Z80-like expertise** transfers to Z80 family platforms

---

## Resources Required

**Development Tools:**
- Assembler: **RGBDS** (Rednex Game Boy Development System - standard!)
- Emulator: **BGB** (excellent debugger, cycle-accurate!), Gambatte, mGBA, SameBoy
- Graphics: Tile/sprite editors (Game Boy format)
- Audio: Game Boy music trackers (LSDj, etc.)
- Utilities: ROM builders

**Reference Materials:**
- SM83 instruction set (Z80-like, Sharp custom)
- Game Boy Programming Manual (Pan Docs - community reference)
- PPU reference (tiles, sprites, scrolling, palettes)
- GBC enhancements reference (color, double-speed, VRAM banking)
- 4-channel audio reference
- Memory map (work RAM, VRAM, registers)

**Testing:**
- Emulators (development - BGB highly recommended!)
- Real Game Boy hardware (verification)
- Real Game Boy Color (GBC games)
- Everdrive GB/GBC (modern flash cart)
- Analogue Pocket (modern FPGA hardware)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Game Boy Color Phase 3
**Note:** No Phase 0 (console - no BASIC, direct assembly)
**Historical Note:** Portable gaming revolution (1989-2003), 118.69M units sold (massive success!)
**Signature Features:** **Portable, long battery life (15-30 hours!), GBC color (32,768 colors)**
**CPU:** SM83 @ 4.19MHz (Z80-like, Sharp custom) - skills transfer to Z80 family!
**Success Factor:** **Long battery life** beat Game Gear's color (trade-off accepted by market!)
**Next Steps:** Create Game Boy 8-PHASE-GAME-PROGRESSION.md with specific game mapping
