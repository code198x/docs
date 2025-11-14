# Sega 32X Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sega 32X (1994-1996) → Genesis + 32X dual-SH-2 architecture (+ optional Sega CD!)
**Approach:** Game-first, pattern library, multi-processor coordination, SH-2 RISC mastery
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Genesis add-on (1994), adds dual SH-2 @ 23MHz + 32-bit graphics, stop-gap before Saturn, only ~40 games released, commercial failure ($159 on top of Genesis cost), but technically impressive (5 processors with Sega CD!), competed with SNES, bridged to 32-bit era, ~800K-1.2M units sold

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sega 32X is a Genesis add-on, no BASIC interpreter. Curriculum begins directly with assembly, building on Genesis knowledge while focusing on 32X-specific features.

**Prerequisite Knowledge:** Genesis/Mega Drive assembly programming (68000, VDP, Z80). This curriculum focuses on SEGA 32X-SPECIFIC features: dual SH-2 processors, 32-bit framebuffer, enhanced color, 3D capabilities.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** SH-2 fundamentals, dual-SH-2 coordination, 32-bit framebuffer, 32,768 colors, 3D rendering, Genesis pass-through
**Professional Autoload:** From lesson 1, all programs professionally load from ROM

#### Pattern Library Established:
- **Dual-SH-2 patterns** - 2× Hitachi SH-2 @ 23MHz each (46MHz combined! 32-bit RISC)
- **Master/Slave coordination** - Master SH-2 + Slave SH-2 synchronization
- **Genesis pass-through** - 68000 @ 7.67MHz + Z80 @ 3.58MHz still available
- **32-bit framebuffer** - Direct framebuffer access (320×224 or 320×240)
- **32,768 colors** - 15-bit RGB (vs Genesis 512 colors)
- **256KB 32X RAM** - Split: 128KB framebuffer + 128KB work RAM
- **3D rendering** - Software 3D on dual SH-2 (very powerful for 1994!)
- **Genesis VDP overlay** - 32X framebuffer + Genesis VDP layers (hybrid graphics!)
- **PWM audio** - 10-channel PWM stereo (in addition to Genesis YM2612/PSG!)
- **Multi-processor** - Genesis (68000+Z80) + 32X (SH-2×2) = 4 processors (5 with Sega CD!)

#### Example Tier 1 Lesson: "Your First 32X Framebuffer"
```asm
; Sega 32X Assembly - Lesson 001
; Draw directly to 32-bit framebuffer using Master SH-2
; SH-2 @ 23 MHz

;-------------------------------------------------
; MASTER SH-2 CODE (runs on first SH-2 @ 23MHz)
;-------------------------------------------------
        .SH2                    ; SH-2 mode

        .ORG    $06000000       ; 32X ROM space

MASTER_ENTRY:
        ; Initialize Master SH-2
        mov.l   #$06004000,r15  ; Set stack pointer

        ; Initialize 32X framebuffer
        bsr     Init32X

        ; Clear framebuffer (black)
        mov.l   #$04000000,r1   ; Framebuffer base
        mov.l   #$4000,r2       ; 320×224 words (16-bit per pixel)
        mov     #0,r0           ; Black color
.CLEAR: mov.w   r0,@r1
        add     #2,r1
        dt      r2              ; Decrement and test
        bf      .CLEAR

        ; Draw sprite (simple 32×32 square)
        mov.l   #160,r4         ; X position (center)
        mov.l   #112,r5         ; Y position (center)
        mov.l   #32,r6          ; Width
        mov.l   #32,r7          ; Height
        mov.l   #$7C00,r8       ; Color (red: 11111 00000 00000)
        bsr     DrawRect

MAIN_LOOP:
        ; Wait for vertical blank
        bsr     WaitVBL

        ; Update position (move right)
        add     #1,r4
        cmp/ge  #320-32,r4      ; Check boundary
        bf      .NO_WRAP
        mov     #0,r4           ; Wrap to left
.NO_WRAP:

        ; Erase old position (black rectangle)
        mov.l   #$0000,r8       ; Black
        bsr     DrawRect

        ; Update X
        add     #1,r4

        ; Draw new position (red rectangle)
        mov.l   #$7C00,r8       ; Red
        bsr     DrawRect

        bra     MAIN_LOOP

DrawRect:
        ; Draw filled rectangle
        ; r4=X, r5=Y, r6=width, r7=height, r8=color
        mov     r5,r1           ; Y counter
.YLOOP: mov     r4,r2           ; X counter
        mov     r1,r3
        shll8   r3
        add     r3,r3           ; r3 = Y * 320 * 2
        add     r2,r2           ; r2 = X * 2
        add     r2,r3           ; r3 = (Y*320 + X) * 2
        mov.l   #$04000000,r0   ; Framebuffer base
        add     r3,r0           ; Address = FB + offset

        mov     r6,r9           ; Width counter
.XLOOP: mov.w   r8,@r0          ; Write pixel
        add     #2,r0
        dt      r9
        bf      .XLOOP

        add     #1,r1
        dt      r7              ; Height counter
        bf      .YLOOP
        rts
        nop

Init32X:
        ; Initialize 32X hardware
        mov.l   #$A15100,r1     ; 32X control registers

        ; Enable 32X mode
        mov     #$00,r0
        mov.b   r0,@r1          ; Set adapter control

        ; Set frame mode (320×224, direct color)
        mov.l   #$A15180,r1     ; VDP register
        mov     #$00,r0
        mov.w   r0,@r1

        rts
        nop

WaitVBL:
        ; Wait for vertical blank
        mov.l   #$A15120,r1     ; Interrupt control
.WAIT:  mov.w   @r1,r0
        tst     #$8000,r0       ; Check VBL flag
        bt      .WAIT
        rts
        nop

;-------------------------------------------------
; SLAVE SH-2 CODE (runs on second SH-2 @ 23MHz)
;-------------------------------------------------
SLAVE_ENTRY:
        ; Initialize Slave SH-2
        mov.l   #$06002000,r15  ; Set stack pointer

        ; Slave can do parallel processing
        ; (Example: AI, physics while Master renders)
.IDLE:  nop
        bra     .IDLE
```

**Key teaching moment:** 32X has TWO SH-2 processors @ 23MHz each! Master + Slave coordination critical. Direct framebuffer access (no tile/sprite hardware like Genesis!). 32,768 colors (15-bit RGB). Genesis hardware still works (can overlay VDP layers!). Software 3D is powerful with dual 32-bit RISC. PWM audio adds 10 channels. Can combine with Sega CD for 5 processors total!

**Tier progression:**
1. Master SH-2 framebuffer access (direct pixel plotting)
2. Dual-SH-2 coordination (Master + Slave workload splitting)
3. 32,768 color graphics (15-bit RGB vs Genesis 512 colors)
4. Genesis VDP overlay (combining 32X + Genesis graphics)
5. PWM audio (10-channel stereo samples)
6. Sprite rendering (software, in framebuffer)
7. Collision detection (software-based, fast with SH-2)
8. Controller input (Genesis controllers work)
9. 3D basics (software 3D rendering on SH-2)
10. Texture mapping (affine via SH-2)
11. Z-buffering (depth sorting)
12. Genesis compatibility (32X-enhanced Genesis games)
13. Sega CD integration (triple-hardware games!)
14. RAM management (256KB 32X + 64KB Genesis)
15. Polish patterns (smooth 60 FPS with dual SH-2)
16. Complete 32X mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced dual-SH-2 techniques, 3D rendering engines, Genesis VDP integration, Sega CD compatibility, complex audio

#### New Patterns:
- **Dual-SH-2 optimization** - Perfect load balancing (Master: render, Slave: physics/AI)
- **3D engine development** - Textured polygons, lighting, Z-buffering
- **Genesis VDP mastery** - Overlaying Genesis sprites/tiles on 32X framebuffer
- **Sega CD integration** - Genesis + Sega CD + 32X = 5 processors!
- **PWM audio engines** - 10-channel sample playback, mixing
- **Framebuffer effects** - Direct pixel manipulation advantages
- **Software scaling/rotation** - SH-2 power enables real-time scaling
- **Palette manipulation** - 256-color palette mode (for compatibility)
- **Multi-processor sync** - Genesis 68000 ↔ Master SH-2 ↔ Slave SH-2
- **Enhanced Genesis games** - Games that run on Genesis, better on 32X

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Sega CD integration + Neptune (cancelled)
**Focus:** Genesis + Sega CD + 32X triple-platform, 5-processor coordination

#### Phase 3 Enhancement: Sega CD Integration + Neptune
- **Triple-platform** - Genesis + Sega CD + 32X = 5 processors!
  - 68000 @ 7.67MHz (Genesis main)
  - 68000 @ 12.5MHz (Sega CD sub)
  - Z80 @ 3.58MHz (sound)
  - SH-2 @ 23MHz (32X master)
  - SH-2 @ 23MHz (32X slave)
- **CD-ROM + 32-bit graphics** - Sega CD data streaming + 32X rendering
- **Neptune (cancelled)** - Planned standalone Genesis+32X combo unit (never released)

**Tier 40 Example - 5-Processor Coordination:**
```asm
; Coordinate all 5 processors for maximum performance

; MASTER SH-2: 3D rendering
MASTER_SH2:
        ; Render 3D scene to framebuffer
        bsr     Render3D
        bra     MASTER_SH2

; SLAVE SH-2: Physics + AI
SLAVE_SH2:
        ; Process game physics
        bsr     UpdatePhysics
        ; Process AI
        bsr     UpdateAI
        bra     SLAVE_SH2

; GENESIS 68000: Input + game logic
GENESIS_68K:
        ; Read controllers
        bsr     ReadInput
        ; Update game state
        bsr     UpdateGameLogic
        ; Tell SH-2s to start next frame
        move.w  #1,COMM_FLAG
        bra     GENESIS_68K

; SEGA CD 68000: Stream level data from CD
SEGA_CD_68K:
        ; Read next level chunk from CD
        bsr     StreamLevelData
        ; Decompress textures
        bsr     DecompressTextures
        bra     SEGA_CD_68K

; Z80: Sound effects (YM2612 + PSG)
Z80_SOUND:
        ; Handle sound effect requests
        ; (Z80 code omitted, different assembler)
```

**Triple-platform games:** Only ~10 games supported all three (Genesis + Sega CD + 32X), including Fahrenheit (Indigo Prophecy prototype). Very complex development!

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional multi-processor architecture, advanced 3D engines, complex graphics effects, Sega CD streaming

#### Advanced Techniques:
- **Advanced 3D engines** - Texture-mapped polygons, Gouraud shading, lighting
- **Dual-SH-2 pipelines** - Master (render) | Slave (transform/light) perfect overlap
- **Genesis VDP effects** - Water effects, HUD, parallax (on VDP) + 3D (on 32X)
- **Sega CD streaming** - Continuous level/texture loading from CD
- **Multi-processor optimization** - 5-processor workload distribution
- **Texture caching** - Managing textures in limited 256KB RAM
- **Fixed-point math** - Fast 3D without FPU (SH-2 has no FPU!)
- **PWM + YM2612 hybrid** - 10 PWM channels + 6 YM2612 + 3 PSG = 19 audio channels!
- **Framebuffer tricks** - Direct pixel manipulation for effects
- **VDP overlay mastery** - Strategic use of Genesis VDP for HUD/effects

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** 3D action games, fighters, shooters, racing games, arcade conversions

#### Genre Specializations:
- **3D action** - Star Wars Arcade, Virtua Fighter (32X's strength!)
- **Fighting games** - Virtua Fighter, Mortal Kombat II (enhanced)
- **Shooters** - Doom 32X (best console Doom of era!)
- **Racing games** - Virtua Racing Deluxe (arcade-perfect!)
- **Arcade ports** - Space Harrier, After Burner (32-bit power!)
- **Platformers** - Knuckles Chaotix (32X exclusive)
- **Sports games** - NBA Jam TE, FIFA Soccer (enhanced)
- **Shmups** - Shadow Squadron, Metal Head

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum polygons, complex multi-processor coordination, advanced effects

#### Limit-Pushing Techniques:
- **Maximum polygons** - 50,000-100,000 polygons/sec (dual SH-2 optimized!)
- **Advanced texturing** - Perspective-correct texture mapping
- **Lighting mastery** - Dynamic lighting, multiple light sources
- **Particle systems** - Thousands of particles (SH-2 power!)
- **5-processor mastery** - Perfect utilization of all 5 CPUs
- **Sega CD streaming** - Zero-load continuous level streaming
- **Framebuffer effects** - Complex post-processing
- **VDP hybrid showcases** - Best use of Genesis VDP + 32X framebuffer

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial-quality 3D games, professional multi-processor coordination

#### Commercial Techniques:
- **Commercial 3D** - Virtua Fighter, Star Wars Arcade quality
- **Doom 32X** - Best console Doom (better than PS1/Saturn in 1994!)
- **Virtua Racing Deluxe** - Arcade-perfect 3D racing
- **Professional graphics** - Smooth 3D, texture-mapped polygons
- **Polish effects** - Smooth 60 FPS, complex effects
- **Multi-processor showcase** - Games that fully utilize all processors
- **Enhanced Genesis titles** - Games that work on Genesis, shine on 32X

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, flash cartridge features

#### Modern Development:
- **Kega Fusion emulator** - 32X emulation, debugging
- **SGDK 32X support** - Modern Sega development kit
- **Modern SH-2 toolchains** - GCC SH-2, VASM
- **Flash cartridge development** - Mega EverDrive Pro (32X support)
- **Modern graphics tools** - 3D modelers, texture converters
- **Community techniques** - Active 32X homebrew scene
- **Cross-platform patterns** - SH-2 expertise (also in Saturn!)
- **Modern compression** - Better tools for 256KB RAM management

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **Multi-processor Patterns (Phase 3)** - 50 5-processor coordination
4. **Optimization Patterns (Phase 4-5)** - 100 dual-SH-2 + 3D techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Sega 32X (1994)**
- 2× Hitachi SH-2 @ 23MHz each (32-bit RISC)
- 256KB 32X RAM (128KB framebuffer + 128KB work)
- 320×224 or 320×240 framebuffer (direct pixel access)
- 32,768 colors (15-bit RGB: 5-5-5)
- PWM audio: 10-channel stereo samples
- Genesis pass-through:
  - 68000 @ 7.67MHz
  - Z80 @ 3.58MHz
  - VDP (overlay capability!)
  - YM2612 + PSG
  - 64KB Genesis RAM
- Cartridge ROM: 2-4MB typical

**Phase 3+: With Sega CD (5 processors!)**
- +68000 @ 12.5MHz (Sega CD sub CPU)
- +512KB PRG-RAM + 256KB Word RAM (Sega CD)
- +CD-ROM 2× speed (300KB/s)
- +CD-DA audio
- +8-channel PCM
- Total: 5 processors, 19 audio channels!

**Phase 7-8: Modern Homebrew**
- Mega EverDrive Pro (flash cartridge with 32X support)
- Modern development tools (Kega Fusion, SGDK, GCC SH-2)
- Modern graphics/audio tools

## Spiral Learning Example: 3D Shooter

**Phase 1 (Tier 9):** Simple 3D room (4 walls, floor, ceiling), player movement, Master SH-2. (~200 lines assembly)

**Phase 2 (Tier 25):** Textured walls, enemies (sprites), Slave SH-2 for AI, collision. (~500 lines)

**Phase 3 (Tier 39):** Sega CD integration - streaming levels from CD, CD-DA music. (~800 lines)

**Phase 4 (Tier 47):** Weapons, lighting, particle effects, complex enemy AI. (~1200 lines)

**Phase 5 (Tier 50):** Full 3D shooter - many levels, weapon variety, multiplayer. (~1600 lines)

**Phase 6 (Tier 54):** Maximum polygons, advanced lighting, complex effects. (~2000 lines)

**Phase 7 (Tier 57):** Doom 32X quality - professional 3D, smooth gameplay. (~2800 lines)

**Phase 8 (Tier 59):** Modern homebrew - additional content, modern tools, flash cart. (~2800 lines + tooling)

## Key Differences from Other Platforms

1. **Genesis Add-On** - Requires Genesis (not standalone), $159 on top of Genesis cost
2. **Dual SH-2 @ 23MHz** - 46MHz combined, very powerful for 1994!
3. **Framebuffer Graphics** - Direct pixel access (no tile/sprite hardware)
4. **32,768 Colors** - 15-bit RGB (vs Genesis 512 colors)
5. **Genesis Pass-Through** - Can overlay Genesis VDP on 32X framebuffer
6. **5 Processors with Sega CD** - Most complex consumer console architecture!
7. **PWM Audio** - 10-channel stereo (+ Genesis YM2612/PSG)
8. **Commercial Failure** - Only ~40 games, rushed to market
9. **Stop-Gap Hardware** - Released while Saturn in development (confused market)
10. **SH-2 Architecture** - Same processor family as Saturn (dual SH-2!)

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add texture mapping with Slave SH-2 assist")
- Pattern recognition exercises ("Identify the dual-SH-2 synchronization issue")
- Debugging challenges ("Fix the framebuffer tearing")
- Performance optimization tasks ("Increase polygon count by 30%")

**Summative Assessment:**
- End of each phase: Complete 32X game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, dual-SH-2 utilization, 3D quality
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working 32X game (framebuffer, dual-SH-2, PWM)
- **Phase 2:** 3D game (textured polygons, Z-buffering)
- **Phase 3:** Triple-platform game (Genesis + Sega CD + 32X)
- **Phase 4:** Advanced 3D (lighting, complex effects)
- **Phase 5:** Genre-mastery project (3D action/fighter/shooter/racer)
- **Phase 6:** Technical showcase (maximum polygons, effects)
- **Phase 7:** Commercial-quality 3D game
- **Phase 8:** Modern homebrew with community release

## Success Criteria

**By Phase 4, learners can:**
- Program SH-2 assembly fluently (32-bit RISC)
- Coordinate dual-SH-2 processors efficiently
- Implement 3D rendering (textured polygons, Z-buffer, lighting)
- Use Genesis VDP overlay strategically
- Work with framebuffer graphics (direct pixel access)
- Integrate Sega CD (5-processor coordination)

**By Phase 8, learners can:**
- Develop commercial-quality 32X games
- Push dual-SH-2 to limits (100,000+ polygons/sec)
- Master multi-processor coordination (up to 5 processors!)
- Work with modern homebrew tools
- Contribute to 32X homebrew scene
- Understand SH-2 architecture (transfers to Saturn!)
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- Kega Fusion emulator (32X support, free)
- GCC SH-2 or VASM
- Text editor
- Sega 32X reference documentation (SH-2, framebuffer, PWM)
- Genesis reference (for pass-through features)

**Phase 3+:**
- Sega CD emulation (for triple-platform development)

**Phase 7-8:**
- Mega EverDrive Pro (flash cartridge with 32X support)
- Sega 32X hardware (optional, for real testing)
- Modern 3D tools (modelers, texture converters)
- Community resources (Sega Retro, homebrew scene)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** Dual-SH-2 RISC mastery (46MHz combined!), framebuffer graphics, 3D rendering expertise, multi-processor coordination (up to 5!), SH-2 knowledge transfers to Saturn, understanding complex console add-on architecture
