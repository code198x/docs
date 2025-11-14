# Vectrex Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Vectrex (1982-1984) → Modern homebrew (2000s+)
**Approach:** Game-first, pattern library, vector graphics mastery
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** ONLY home console with built-in vector display (9" monochrome CRT), self-contained unit with screen and controller, 3D Imager accessory (spinning color wheel!), ~1 million units sold, unique in gaming history

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Vectrex shipped without a built-in programming language. The curriculum begins directly with assembly, focused on vector graphics programming.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 6809 fundamentals, vector graphics concepts, VIA interface (6522), integrating amplifier (analog positioning), sound synthesis, vector list programming
**Professional Autoload:** From lesson 1, all programs professionally load from ROM

#### Pattern Library Established:
- **6809 CPU patterns** - 8-bit Motorola CPU @ 1.5 MHz (one of the most elegant 8-bit architectures!)
- **Vector graphics concepts** - Lines/points instead of pixels, beam positioning, intensity control
- **VIA (6522) patterns** - Versatile Interface Adapter: controls DACs for X/Y positioning and Z-axis (brightness)
- **Integrating amplifier** - Analog beam positioning (NOT digital like raster displays!)
- **Vector list programming** - Drawing lists: move beam, draw line, set intensity
- **Zero reference** - Must recenter beam periodically (analog drift!)
- **Sound synthesis** - VIA + AY-3-8910 PSG: 3 channels + 1 noise
- **Built-in BIOS** - "Vectrex ROM" with essential routines (vector drawing, text, etc.)
- **Coordinate system** - Signed bytes: -127 to +127 for X and Y
- **Intensity control** - 0-127 brightness levels per line

#### Example Tier 1 Lesson: "Your First Vector Line"
```asm
; Vectrex Assembly - Lesson 001
; Draw a simple bouncing box
; 6809 @ 1.5 MHz

        ORG     $0000

; Cartridge header
        FCC     "g GCE 1982"    ; Copyright string (required!)
        FCB     $80             ; Music flag
        FDB     $F850           ; Height/width
        FDB     $30             ; Font height
        FDB     $50             ; Font width
        FCC     "MY FIRST GAME*" ; Title (null-terminated with bit 7 set on last char)
        FCB     $80

; Program start
START:  JSR     $F192           ; Wait_Recal (zero reference beam)
        JSR     $F1AA           ; Intensity_5F (medium intensity)

LOOP:   JSR     $F192           ; Zero reference beam (critical!)

        ; Position beam to start of box
        LDD     #$2020          ; X=32, Y=32
        JSR     $F312           ; Moveto_d (move beam without drawing)

        ; Draw box (4 lines)
        LDD     #$4000          ; X=64, Y=0 (right side)
        JSR     $F3DF           ; Draw_Line_d

        LDD     #$0040          ; X=0, Y=64 (top side)
        JSR     $F3DF           ; Draw_Line_d

        LDD     #$C000          ; X=-64, Y=0 (left side)
        JSR     $F3DF           ; Draw_Line_d

        LDD     #$00C0          ; X=0, Y=-64 (bottom side)
        JSR     $F3DF           ; Draw_Line_d

        ; Animate: update position
        LDA     XPOS
        ADDA    XVEL
        STA     XPOS
        CMPA    #64             ; Check boundary
        BLT     XDONE
        NEG     XVEL            ; Reverse direction
XDONE:

        JSR     $F1A2           ; Wait for frame (60Hz)
        BRA     LOOP

XPOS:   FCB     32              ; X position
YPOS:   FCB     32              ; Y position
XVEL:   FCB     1               ; X velocity
YVEL:   FCB     1               ; Y velocity
```

**Key teaching moment:** Vector graphics are FUNDAMENTALLY DIFFERENT from raster. No pixels! You draw lines and points. The beam must be ZEROED periodically (analog drift). Intensity controlled per-line. Built-in BIOS provides essential routines.

**Tier progression:**
1. Single vector line basics (beam positioning, line drawing)
2. Multiple vectors (drawing shapes: box, triangle, etc.)
3. Vector lists (efficient drawing sequences)
4. Intensity control (bright/dim lines, flashing effects)
5. Zero reference timing (preventing analog drift)
6. Sound basics (AY-3-8910 PSG)
7. Controller input (analog joystick via VIA!)
8. Animation patterns (moving vectors, rotation)
9. Text rendering (BIOS font routines)
10. Collision detection (vector intersection math!)
11. Game state machines
12. Score display (vector-drawn digits!)
13. Enemy AI (movement patterns)
14. Difficulty progression
15. Polish patterns (explosions via intensity, particle effects)
16. Complete vector mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced vector techniques, smooth rotation, scaling, 3D wireframe basics, color overlays (plastic sheets!), optimization

#### New Patterns:
- **Rotation mathematics** - Sine/cosine tables for smooth vector rotation
- **Scaling** - Growing/shrinking vector objects
- **3D wireframe** - Basic 3D projection (Vectrex excels at this!)
- **Color overlays** - Game-specific plastic overlays (red/blue/green areas on screen)
- **Vector clipping** - Preventing offscreen drawing (beam limits)
- **Intensity modulation** - Dynamic brightness for depth effects
- **Optimized drawing** - Minimizing beam movement (faster drawing)
- **Vector lists** - Compressed drawing data
- **Music engines** - Complex AY-3-8910 compositions
- **Advanced collision** - Line-line, line-point intersection
- **Screen shake** - Offsetting all vectors for impact effects
- **Particle systems** - Explosion debris, stars, bullets

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - introducing 3D Imager accessory (1983)
**Focus:** 3D Imager programming, color wheel synchronization, stereoscopic 3D, LCD shutter glasses

#### Phase 3 Enhancement: 3D Imager
- **Spinning color wheel** - Rotating disc with red/blue/green segments (motorized!)
- **LCD shutter glasses** - Left/right eye alternation for stereoscopic 3D
- **Color programming** - Drawing different colors by timing with wheel rotation
- **3D stereoscopic** - Left/right eye images for depth perception
- **Synchronization** - Critical timing to match wheel/shutter position
- **6-color palette** - Red, green, blue, cyan, magenta, yellow (by timing!)

**Tier 40 Example - 3D Imager Color Drawing:**
```asm
; Draw colored vectors using 3D Imager

; Wait for color wheel position
WAITCOLOR:
        LDA     $D004           ; Read 3D Imager port
        ANDA    #$03            ; Mask wheel position bits
        CMPA    #$00            ; Red position?
        BNE     WAITCOLOR

; Draw red vectors
        JSR     $F192           ; Zero reference
        LDD     #$0000
        JSR     $F312           ; Move to center
        LDA     #$7F            ; Maximum intensity
        JSR     $F2AB           ; Intensity_a
        LDD     #$4000          ; 64 units right
        JSR     $F3DF           ; Draw red line

; Wait for green position
WAITGREEN:
        LDA     $D004
        ANDA    #$03
        CMPA    #$01            ; Green position?
        BNE     WAITGREEN

; Draw green vectors
        JSR     $F192
        LDD     #$0000
        JSR     $F312
        LDD     #$0040          ; 64 units up
        JSR     $F3DF           ; Draw green line

; (Continue for blue, cyan, magenta, yellow...)
```

**3D Imager Games:** Mine Storm 3D (pack-in), Crazy Coaster 3D, 3D Narrow Escape. Only ~7 commercial releases, but impressive technology for 1983!

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional game architecture, complex 3D wireframes, optimized vector lists, advanced rotation/scaling, music complexity

#### Advanced Techniques:
- **3D object modeling** - Complex wireframe objects (ships, enemies, terrain)
- **Hidden line removal** - Determining which lines to draw in 3D
- **Matrix transformations** - Proper 3D rotation/scaling/translation
- **Fixed-point math** - Fast multiplication/division without hardware support
- **Vector list compression** - Efficient data structures for complex objects
- **Multi-object management** - Many moving 3D objects simultaneously
- **Advanced AI** - Vector-based pathfinding, tracking
- **3D Imager mastery** - Full color + stereoscopic 3D simultaneously
- **Sound effects** - Explosion sounds, thrust effects, lasers (AY programming)
- **Screen edge wrap** - Asteroids-style topology
- **Variable frame rate** - Adjusting complexity based on performance

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** 3D wireframe shooters, vector art games, arcade conversions, puzzle games, racing games

#### Genre Specializations:
- **3D wireframe shooters** - Battlezone-style games (Vectrex's signature genre!)
- **Asteroids-style** - Classic vector arcade conversions (Mine Storm!)
- **Racing games** - 3D perspective, speed effects
- **Vector art games** - Creative non-game applications (drawing programs, demos)
- **Puzzle games** - Tetris-style with vector pieces
- **Maze games** - 3D first-person mazes (wireframe walls)
- **Sports games** - Creative vector representations (football fields, courts)

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum vector counts, complex 3D scenes, full-screen vector fills, performance optimization

#### Limit-Pushing Techniques:
- **Maximum vectors per frame** - Drawing as many as possible at 60Hz
- **Filled vectors** - Creating solid areas with many close lines
- **Complex 3D scenes** - Many objects, detailed wireframes
- **Smooth rotation** - Pre-calculated sine/cosine tables, interpolation
- **Advanced 3D Imager** - Full 6-color stereoscopic scenes
- **Raster emulation** - Creating pixel-like effects with vectors (characters, faces)
- **Vector compression** - Maximum detail in ROM space
- **Synchronized sound/graphics** - Music timed to visual events

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Arcade-quality 3D games, professional polish, advanced 3D Imager titles, music complexity

#### Commercial Techniques:
- **Arcade ports** - Battlezone, Tempest, Star Wars (vector arcade games!)
- **Professional 3D** - Complex wireframe objects, smooth animation
- **Advanced art** - Creative vector designs, attract modes
- **Full music scores** - Complex AY-3-8910 compositions
- **Polish effects** - Screen shake, explosions, particles, intensity modulation
- **3D Imager showcase** - Games that fully utilize color + stereoscopic 3D
- **High score systems** - Vector-drawn tables, player initials
- **Easter eggs** - Hidden vector art, bonus stages

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, flash cartridge features, community collaboration

#### Modern Development:
- **ParaJVE emulator** - Modern debugging, development tools
- **CMOC compiler** - C programming for Vectrex (6809 C compiler)
- **Modern assemblers** - VASM, AS09, cross-platform toolchains
- **Flash cartridge development** - VecMulti (multi-game cartridge)
- **Graphics tools** - Vector editors, 3D modelers for wireframe export
- **Community techniques** - Vectrex forums, competitions
- **Cross-platform patterns** - Techniques from other 6809 systems (CoCo, Dragon)
- **Modern 3D techniques** - Advanced wireframe algorithms
- **VecVox (homebrew hardware)** - Speech synthesis add-on
- **Competition entries** - Annual Vectrex homebrew competitions

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **3D Imager Patterns (Phase 3)** - 50 enhancement-specific
4. **Optimization Patterns (Phase 4-5)** - 100 performance techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Base Vectrex**
- 6809 @ 1.5 MHz (8-bit Motorola, elegant architecture)
- 1KB RAM (8KB with RAM expansion)
- 9" monochrome vector CRT (beam positioning, not pixels!)
- Integrating amplifier (analog X/Y positioning)
- VIA 6522 (controls DACs for beam, interfaces I/O)
- AY-3-8910 PSG: 3 channels + 1 noise
- Analog joystick + 4 buttons (built-in controller!)
- 8KB ROM typical (up to 32KB)

**Phase 3+: Enhanced (3D Imager)**
- +Spinning color wheel (red/green/blue segments, motorized)
- +LCD shutter glasses (stereoscopic 3D!)
- +6-color capability (red/green/blue/cyan/magenta/yellow by timing)
- +Depth perception (left/right eye alternation)
- All base features unchanged

**Phase 7-8: Modern Homebrew**
- VecMulti flash cartridge (multi-game, large ROMs)
- VecVox speech synthesis (homebrew hardware)
- Modern development tools (ParaJVE, CMOC, VASM)
- Vector editors, 3D wireframe tools
- 64KB+ ROMs possible

## Spiral Learning Example: Asteroids (Perfect for Vectrex!)

**Phase 1 (Tier 5):** Single ship sprite, rotation, thrust. Single asteroid. Basic vector drawing. (~80 lines assembly)

**Phase 2 (Tier 21):** Multiple asteroids, splitting, bullets, score. Introduces vector lists, collision detection. (~250 lines)

**Phase 3 (Tier 37):** 3D Imager version - colored asteroids (red/yellow), stereoscopic depth. (~400 lines)

**Phase 4 (Tier 45):** Advanced physics, smooth rotation (sine/cosine tables), many asteroids, enemy UFO. (~600 lines)

**Phase 5 (Tier 50):** Full arcade features, power-ups, levels, high score table. (~800 lines)

**Phase 6 (Tier 54):** Maximum asteroid count, complex breakup patterns, particle explosions. (~1000 lines)

**Phase 7 (Tier 57):** Arcade-perfect gameplay, professional polish, attract mode, complex music. (~1200 lines)

**Phase 8 (Tier 59):** Modern homebrew release, additional features (saved high scores via flash), debug mode. (~1200 lines + tooling)

## Key Differences from Other Platforms

1. **ONLY Vector Graphics Console** - Completely unique in home gaming! No pixels, only lines/points
2. **Analog Beam Positioning** - Integrating amplifier (NOT digital raster) - requires periodic zero reference
3. **9" Built-in CRT** - Self-contained unit (no TV connection!)
4. **6809 CPU** - One of most elegant 8-bit architectures (also in CoCo, Dragon)
5. **3D Imager** - Color via spinning wheel + stereoscopic 3D via shutter glasses (revolutionary for 1983!)
6. **Intensity Control** - 0-127 brightness levels per vector
7. **Built-in BIOS** - "Vectrex ROM" with drawing routines, font, utilities
8. **Coordinate System** - Signed bytes (-127 to +127) for X/Y positioning
9. **Ideal for 3D Wireframe** - Platform naturally excels at Battlezone/Tempest-style games
10. **Analog Joystick** - Continuous positioning (not digital 8-way), 4 buttons

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add rotation to your ship sprite")
- Pattern recognition exercises ("Identify the vector list optimization")
- Debugging challenges ("Fix the zero reference drift")
- Performance optimization tasks ("Draw 20% more vectors per frame")

**Summative Assessment:**
- End of each phase: Complete vector game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, vector efficiency, visual appeal, gameplay feel
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working vector game (basic shapes, movement)
- **Phase 2:** Game with rotation/scaling, smooth animation
- **Phase 3:** 3D Imager title (color + stereoscopic 3D)
- **Phase 4:** Complex 3D wireframe game (many objects)
- **Phase 5:** Genre-mastery project (3D shooter/Asteroids/racing/puzzle)
- **Phase 6:** Technical showcase (maximum vectors, filled areas)
- **Phase 7:** Commercial-quality vector game
- **Phase 8:** Modern homebrew with community release

## Success Criteria

**By Phase 4, learners can:**
- Write 6809 assembly fluently (elegant instruction set)
- Master vector graphics concepts (beam positioning, line drawing, intensity)
- Work with analog hardware (integrating amplifier, zero reference)
- Implement 3D wireframe graphics (rotation, projection, hidden line removal)
- Program AY-3-8910 sound (3 channels + noise)
- Handle analog joystick input (continuous positioning)
- Utilize 3D Imager (color wheel synchronization, stereoscopic 3D)

**By Phase 8, learners can:**
- Develop commercial-quality vector games
- Push hardware to absolute limits (maximum vectors, filled areas)
- Work with modern homebrew tools (ParaJVE, CMOC, VecMulti)
- Contribute to active Vectrex homebrew community
- Create 3D Imager titles (full color + stereoscopic)
- Port techniques from vector arcade games (Battlezone, Tempest)
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- ParaJVE emulator (cross-platform, accurate, free)
- VASM or AS09 assembler
- Text editor
- Vectrex reference documentation (6809, VIA 6522, vector programming)
- Built-in BIOS ROM (for BIOS routine usage)

**Phase 3+:**
- 3D Imager emulation (for testing color/stereoscopic features)
- Color wheel timing documentation
- LCD shutter glasses specifications

**Phase 7-8:**
- VecMulti or similar flash cartridge (optional, for real hardware)
- Original Vectrex (optional, increasingly collectible!)
- CMOC compiler (for C programming option)
- Vector graphics tools (editors, 3D wireframe exporters)
- Community resources (Vectrex forums, competitions)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement (for feedback and collaboration)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** ONLY vector graphics curriculum, 3D wireframe mastery, analog hardware understanding, 3D Imager color/stereoscopic programming, 6809 expertise (transferable to CoCo/Dragon)
