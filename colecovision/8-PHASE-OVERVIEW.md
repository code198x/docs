# ColecoVision Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** ColecoVision (base, 1982) → SGM (Super Game Module, 1984) → Modern homebrew
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct to assembly (no built-in BASIC, though cartridge available)
**Historical Note:** Best-selling second generation console (2 million units, 1982-1984), famous for arcade-perfect ports (Donkey Kong, Zaxxon), TMS9918A video chip (same as TI-99/4A, MSX), competed with Atari 5200

## 8-Phase Structure

### Phase 0: N/A
**No built-in BASIC gateway.** ColecoVision shipped without built-in programming language. BASIC cartridge existed but rare. Curriculum begins directly with assembly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** Z80 fundamentals, TMS9918A video chip, SN76489 sound, controller input, 1KB RAM, arcade-style gameplay
**Professional Autoload:** From lesson 1, all programs professionally load from ROM

#### Pattern Library Established:
- **Z80 CPU patterns** - 8-bit Zilog processor @ 3.58 MHz (standard instruction set)
- **TMS9918A video patterns** - Texas Instruments VDP: 32 hardware sprites, 256×192 resolution, 16 colors
- **SN76489 PSG patterns** - 3 square wave channels + 1 noise channel
- **Controller patterns** - Numeric keypad (12 buttons) + joystick + 2 side fire buttons
- **VDP memory patterns** - 16KB VRAM (separate from main RAM!)
- **Sprite patterns** - 32 sprites (8×8 or 16×16), single color each, 4 sprites per scanline limit
- **Name table patterns** - 32×24 character grid (Graphics Mode I)
- **Color table patterns** - 8-pixel row color assignment (Mode I limitation)
- **Pattern table patterns** - 256 character definitions (8×8 pixels each)
- **RAM conservation** - Only 1KB main RAM (extremely limited!)

#### Example Tier 1 Lesson: "Your First Sprite"
```asm
; ColecoVision Assembly - Lesson 001
; Display bouncing ball sprite
; Z80 @ 3.58 MHz

        ORG     $8000

START:  DI                      ; Disable interrupts
        LD      SP,$7400        ; Set stack (below cartridge area)

        ; Initialize VDP
        LD      HL,VDPINIT
        CALL    INITVDP

        ; Load sprite pattern (ball)
        LD      HL,$3800        ; VDP sprite pattern table
        CALL    SETVDP
        LD      A,$FF           ; 8×8 solid circle
        OUT     (VDPDATA),A
        ; ... (load 8 bytes of pattern data)

        ; Set sprite attributes
        LD      HL,$3B00        ; VDP sprite attribute table
        CALL    SETVDP
        LD      A,100           ; Y position
        OUT     (VDPDATA),A
        LD      A,100           ; X position
        OUT     (VDPDATA),A
        LD      A,0             ; Pattern #0
        OUT     (VDPDATA),A
        LD      A,$0F           ; White color
        OUT     (VDPDATA),A

LOOP:   CALL    WAITVB          ; Wait for vertical blank

        ; Read current position
        LD      A,(XPOS)
        INC     A               ; Move right
        CP      248             ; At edge?
        JR      NZ,CONT
        XOR     A               ; Wrap to left
CONT:   LD      (XPOS),A

        ; Update VDP sprite X
        LD      HL,$3B01
        CALL    SETVDP
        LD      A,(XPOS)
        OUT     (VDPDATA),A

        JR      LOOP

XPOS:   DB      100             ; Sprite X position (in RAM)

VDPDATA EQU     $BE             ; VDP data port
VDPCTRL EQU     $BF             ; VDP control port

; VDP initialization data
VDPINIT:
        DB      $00,$80         ; Register 0: Mode 0
        DB      $E2,$81         ; Register 1: 16K, display on, sprites 16×16
        DB      $06,$82         ; Register 2: Name table at $1800
        DB      $80,$83         ; Register 3: Color table at $2000
        DB      $01,$84         ; Register 4: Pattern table at $800
        DB      $76,$85         ; Register 5: Sprite attribute at $3B00
        DB      $07,$86         ; Register 6: Sprite pattern at $3800
        DB      $F5,$87         ; Register 7: White text on cyan background
        DB      $FF             ; End marker

SETVDP:
        ; Set VDP address in HL
        LD      A,L
        OUT     (VDPCTRL),A
        LD      A,H
        OUT     (VDPCTRL),A
        RET

INITVDP:
        ; Initialize VDP registers from table at HL
        LD      BC,$0810
.LOOP:  LD      A,(HL)
        OUT     (VDPCTRL),A
        INC     HL
        DEC     C
        JR      NZ,.LOOP
        RET

WAITVB:
        ; Wait for vertical blank
        IN      A,(VDPCTRL)
        AND     $80             ; Check interrupt flag
        JR      Z,WAITVB
        RET
```

**Key teaching moment:** VDP has separate 16KB VRAM accessed via ports $BE/$BF. All graphics data (sprites, patterns, name table) lives in VRAM, not main RAM. This is KEY difference from Spectrum/C64.

**Tier progression:**
1. Single sprite basics (VDP programming, VRAM access)
2. Multiple sprites (32 sprite management, 4-per-scanline limit!)
3. Background graphics (name table, pattern table, color table)
4. Controller input (keypad + joystick, BIOS routines)
5. Sound basics (SN76489 PSG via port $FF)
6. Collision detection (software-based, VDP has status flags but limited)
7. RAM conservation (1KB total - extreme constraint!)
8. Arcade game patterns (smooth movement, enemy AI)
9. Score display (VDP text mode)
10. Title screens (Graphics Mode II for better colors)
11. Game state machines
12. Difficulty progression
13. Multi-level structures
14. Lives/continues systems
15. Polish patterns (sound effects, screen transitions)
16. Complete arcade-style mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced VDP modes (Graphics II, multicolor), smooth scrolling, advanced sprite multiplexing, arcade port techniques, ROM banking

#### New Patterns:
- **Graphics Mode II** - 256 unique patterns (vs 32 in Mode I), better for detailed graphics
- **Multicolor Mode** - 64×48 chunky pixels, 16 colors (for some game types)
- **Sprite multiplexing** - Overcoming 4-sprites-per-scanline limit
- **Smooth scrolling** - Character-based (8-pixel steps) and pixel-based tricks
- **ROM banking** - 32KB standard ROMs, banking for larger games
- **Advanced collision** - Multiple detection strategies (sprite overlap, sprite-background)
- **AI patterns** - Arcade enemy behaviors (Pac-Man ghosts, Donkey Kong barrels)
- **Level data compression** - Critical for 1KB RAM constraint
- **BIOS routines** - Leveraging built-in functions (controller read, random numbers)
- **Music engines** - 3-channel compositions with rhythm
- **Arcade timing** - 60Hz gameplay feel, frame-perfect input
- **High score tables** - RAM-efficient storage, no battery backup

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - introducing Super Game Module (SGM, 1984)
**Focus:** 24KB extra RAM, AY-3-8910 enhanced sound chip (3 channels with envelope control), SGM detection patterns

#### Phase 3 Enhancement: Super Game Module
- **24KB extra RAM** - Total 25KB (from 1KB!) - transforms platform!
- **AY-3-8910 PSG** - 3 square wave channels + 1 noise + envelope generator (upgrade from SN76489)
- **SGM detection** - Code must detect presence and gracefully degrade
- **Enhanced games** - Larger levels, more enemies, better music
- **Dual-sound systems** - Can drive both SN76489 AND AY-3-8910 simultaneously!

**Tier 40 Example - SGM Detection and Dual-Sound:**
```asm
; Detect SGM and enable enhanced features

DETECTSGM:
        LD      A,$50           ; Test value
        LD      ($2000),A       ; Write to SGM RAM area
        LD      A,($2000)       ; Read back
        CP      $50             ; Did it persist?
        JR      Z,SGMFOUND

        ; No SGM - use base hardware
        LD      A,0
        LD      (SGMFLAG),A
        RET

SGMFOUND:
        ; SGM detected - enable enhanced features
        LD      A,1
        LD      (SGMFLAG),A

        ; Initialize AY-3-8910 (at ports $50-$51)
        LD      A,7             ; Mixer register
        OUT     ($50),A
        LD      A,$38           ; Enable tone channels
        OUT     ($51),A
        RET

PLAYMUSIC:
        ; Play music on available sound chips
        LD      A,(SGMFLAG)
        OR      A
        JR      Z,BASEMUSIC     ; No SGM, use SN76489 only

        ; SGM present - use AY-3-8910
        LD      A,0             ; Channel A fine tune
        OUT     ($50),A
        LD      A,(NOTEA)
        OUT     ($51),A
        ; ... continue with AY programming
        RET

BASEMUSIC:
        ; Use SN76489 (port $FF)
        LD      A,$90           ; Channel 0 frequency
        OR      (NOTEA)
        OUT     ($FF),A
        ; ... continue with SN programming
        RET

SGMFLAG: DB     0
NOTEA:   DB     0
```

**SGM Games:** Only ~20 commercial SGM games released (Parker Brothers, Coleco), but homebrew community embraced it.

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional game architecture, pixel-perfect arcade ports, advanced sprite techniques, complex AI, ROM banking mastery

#### Advanced Techniques:
- **Arcade port patterns** - Donkey Kong, Zaxxon, Burgertime (ColecoVision famous for these!)
- **Pseudo-3D** - Isometric graphics (Zaxxon-style), parallax scrolling
- **Large sprite composition** - 2×2, 2×4 sprite combinations for big characters
- **Advanced AI** - Pattern-based enemies, state machines
- **SGM enhancement layers** - Games that work on base system but better with SGM
- **Sprite flicker management** - 4-per-scanline limit strategies
- **VDP timing mastery** - Raster effects (limited but possible)
- **Music complexity** - Dual-chip orchestration (SGM)
- **RAM banking** - Using SGM's 24KB efficiently
- **Attract mode patterns** - Demo playback, high score display

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Arcade action mastery, platformer techniques, maze games, puzzle games, sports games

#### Genre Specializations:
- **Arcade action** - Smooth movement, enemy patterns, power-ups (Donkey Kong-style)
- **Platformers** - Jumping physics, collision detection, level design
- **Maze games** - Pac-Man patterns, pathfinding AI, pellet management
- **Puzzle games** - Tetris-style, match-3, logic puzzles
- **Sports games** - Baseball, football (within 1KB RAM constraint!)
- **Shooters** - Scrolling shooters, bullet patterns, bosses
- **Isometric games** - Zaxxon-style 3D, Q*bert perspective

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum sprite counts, VDP mode switching, raster effects, RAM compression mastery

#### Limit-Pushing Techniques:
- **Sprite multiplexing mastery** - 64+ visible sprites (32 hardware limit overcome!)
- **VDP mode switching** - Mid-frame mode changes (Graphics I/II hybrid)
- **Raster interrupts** - Limited but creative effects possible
- **SGM RAM maximization** - 25KB efficient usage patterns
- **Data compression** - RLE, LZ variants for level data
- **Procedural generation** - Levels, enemies (RAM conservation)
- **Advanced audio** - Dual-chip (SN76489 + AY-3-8910) orchestration
- **Pixel-perfect timing** - Frame-exact gameplay (arcade authenticity)

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Arcade-perfect ports, original IPs, professional polish, advanced music, speed optimization

#### Commercial Techniques:
- **Arcade authenticity** - Pixel-perfect graphics, accurate timing, authentic sound
- **Professional sprite art** - Animation cycles, smooth movement
- **Complex music** - Multi-channel scores with harmony
- **Polish effects** - Screen transitions, particle effects, explosions
- **Difficulty curves** - Progressive challenge (arcade quarter-eating!)
- **Easter eggs** - Hidden content, bonus stages
- **Attract mode** - Demo playback, high score showcase
- **SGM enhancement** - Games that shine on SGM but work on base

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, flash cartridge features, community collaboration

#### Modern Development:
- **ColEm emulator integration** - Debugging, development cycle
- **Modern assemblers** - tniASM, VASM, cross-platform toolchains
- **CVBasic** - Higher-level language option (BASIC-like)
- **Flash cartridge development** - Mega Cart (large ROM games)
- **Modern graphics tools** - Tile editors, sprite tools
- **Community techniques** - AtariAge/CollectorVision scene
- **Cross-platform patterns** - Techniques from other Z80 systems (MSX, SMS)
- **SGM homebrew** - Fully utilizing 24KB RAM + AY sound
- **Competition entries** - AtariAge programming contests

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **SGM Patterns (Phase 3)** - 50 enhancement-specific
4. **Optimization Patterns (Phase 4-5)** - 100 performance techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Base ColecoVision**
- Z80 @ 3.58 MHz
- 1KB RAM (extremely limited!)
- 16KB VRAM (TMS9918A)
- TMS9918A VDP: 32 sprites, 256×192, 16 colors
- SN76489 PSG: 3 square wave + 1 noise
- Controller: 12-button keypad + joystick + 2 fire buttons
- 32KB ROM typical

**Phase 3+: Enhanced (SGM)**
- +24KB RAM (total 25KB - 25× increase!)
- +AY-3-8910 PSG (3 channels with envelope control)
- Dual-sound capability (SN76489 + AY simultaneously)
- All base features unchanged
- 32KB-64KB ROM typical (Mega Cart)

**Phase 7-8: Modern Homebrew**
- Mega Cart (256KB+ ROM capacity)
- Modern development tools (ColEm, tniASM, CVBasic)
- Flash cartridge debugging features
- Cross-platform development (MSX, SMS techniques applicable)

## Spiral Learning Example: Donkey Kong (ColecoVision's Killer App!)

**Phase 1 (Tier 4):** Basic platform, Mario sprite, single barrel enemy. Teaches sprite movement, collision, jumping physics. 1 screen. (~100 lines assembly)

**Phase 2 (Tier 20):** Multiple barrels, ladders, collision detection, score display. Introduces sprite multiplexing, enemy AI. (~300 lines)

**Phase 3 (Tier 36):** SGM enhanced - better music (AY-3-8910), more barrels simultaneously (24KB RAM), smoother animation. (~500 lines)

**Phase 4 (Tier 44):** Multiple stages (girders, elevators, rivets), Donkey Kong animations, Pauline sprite. (~800 lines)

**Phase 5 (Tier 50):** Arcade-accurate physics, exact enemy patterns, bonus countdown. (~1000 lines)

**Phase 6 (Tier 54):** All 4 stages, arcade-perfect timing, sprite flicker management (many barrels/fireballs). (~1500 lines)

**Phase 7 (Tier 57):** Pixel-perfect arcade port, authentic sound effects, attract mode demo. (~2000 lines)

**Phase 8 (Tier 59):** Modern homebrew release, additional stages (not in original), debug features. (~2000 lines + tooling)

## Key Differences from Other Platforms

1. **Arcade Port Focus** - ColecoVision's identity was arcade-perfect ports (Donkey Kong pack-in changed the industry)
2. **TMS9918A VDP** - Same chip as TI-99/4A, MSX1 (cross-platform knowledge!)
3. **Separate VRAM** - 16KB VRAM independent of main RAM (all graphics data here)
4. **Extreme Base RAM** - Only 1KB main RAM (vs 16KB+ on most platforms) - forces creative solutions
5. **SGM Transformation** - 24KB RAM upgrade completely changes platform capabilities (1KB→25KB!)
6. **Dual Sound Chips** - SGM allows simultaneous SN76489 + AY-3-8910 programming
7. **4-Sprites-Per-Scanline** - Hard VDP limit requires multiplexing strategies
8. **12-Button Keypad** - Unique controller (shared with Intellivision design philosophy)
9. **Z80 @ 3.58 MHz** - Standard speed for era (same as SMS, Game Gear)
10. **No Hardware Scrolling** - Character-based scrolling only (8-pixel steps)

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add enemy AI to your game")
- Pattern recognition exercises ("Identify the sprite multiplexing pattern")
- Debugging challenges ("Fix the VDP timing issue")
- Performance optimization tasks ("Reduce RAM usage to fit in 1KB")

**Summative Assessment:**
- End of each phase: Complete arcade-style game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, RAM efficiency, arcade feel, visual polish
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working arcade game (1KB RAM constraint)
- **Phase 2:** Multi-level game with smooth scrolling
- **Phase 3:** SGM-enhanced game (detect and utilize SGM features)
- **Phase 4:** Arcade port (Donkey Kong, Pac-Man, or similar quality)
- **Phase 5:** Genre-mastery project (platformer/maze/shooter/puzzle)
- **Phase 6:** Technical showcase (pushing VDP/RAM limits)
- **Phase 7:** Arcade-perfect port or commercial-quality original
- **Phase 8:** Modern homebrew with community release

## Success Criteria

**By Phase 4, learners can:**
- Write Z80 assembly fluently (standard 8-bit techniques)
- Master TMS9918A VDP programming (sprites, patterns, name tables, VRAM)
- Work within extreme RAM constraints (1KB efficiently)
- Implement arcade-style gameplay (smooth movement, enemy AI, collision)
- Program dual sound systems (SN76489 + AY-3-8910 on SGM)
- Handle controller input (keypad + joystick via BIOS)
- Detect and utilize SGM expansion

**By Phase 8, learners can:**
- Develop arcade-perfect ports or commercial-quality originals
- Push VDP to absolute limits (sprite multiplexing, raster effects)
- Work with modern homebrew tools (ColEm, CVBasic, Mega Cart)
- Contribute to active ColecoVision homebrew community
- Port techniques from other TMS9918A platforms (MSX, TI-99/4A)
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- ColEm emulator (cross-platform, accurate, free)
- tniASM or VASM assembler
- Text editor
- ColecoVision reference documentation (Z80, TMS9918A, SN76489)
- BIOS ROM image (for BIOS routine usage)

**Phase 3+:**
- SGM emulation/hardware (for testing SGM features)
- AY-3-8910 documentation (sound programming)
- RAM testing utilities (SGM detection)

**Phase 7-8:**
- Mega Cart or similar flash cartridge (optional, for real hardware)
- Original ColecoVision (optional)
- CVBasic (for prototyping)
- Graphics tools (tile editors, sprite editors)
- Community resources (AtariAge forums, CollectorVision)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement (for feedback and collaboration)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** Arcade port mastery, TMS9918A expertise (transferable to MSX/TI-99/4A), extreme RAM constraint training, SGM dual-sound programming
