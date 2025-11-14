# Emerson Arcadia 2001 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Emerson Arcadia 2001 (1982) + 30+ clone manufacturers worldwide!
**Approach:** Game-first, pattern library, Signetics 2650 mastery, understanding clone market phenomenon
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Cloned by 30+ manufacturers worldwide (Bandai Super Vision 8000, Emerson Arcadia 2001, Leisure-Vision, Intervision, Hanimex, Rowtron, etc.), Signetics 2650 CPU @ 3.58MHz (uncommon architecture), 128×208 graphics (unusual vertical resolution!), 128 bytes RAM (extreme constraint!), 1KB VRAM (dedicated video memory), 8 colors, 4 hardware sprites, 2-button analog joysticks, 51 games total across all variants, competed with Atari 2600 but lost, commercial failure in most markets (~500K units across all clones), fascinating licensing model study

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Emerson Arcadia 2001 and its 30+ clones shipped without BASIC. Curriculum begins directly with assembly, focused on the unusual Signetics 2650 architecture and understanding the clone market phenomenon.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** Signetics 2650 fundamentals, 128×208 unusual resolution, 128 bytes RAM constraint, 4 hardware sprites, 8-color graphics, clone compatibility
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **Signetics 2650 patterns** - Signetics 2650 @ 3.58MHz (rare, uncommon architecture!)
- **128×208 graphics** - Unusual vertical resolution (taller than wide!)
- **128 bytes RAM** - Extreme constraint (same as Atari 2600!)
- **1KB VRAM** - Dedicated video memory
- **8 colors** - Simple palette (black, blue, red, magenta, green, cyan, yellow, white)
- **4 hardware sprites** - Built-in sprite system
- **Analog joysticks** - 2-button controllers (8-way analog stick + fire A + fire B)
- **Clone compatibility** - 30+ manufacturers, all compatible!
- **Cartridge ROM** - Typically 2KB-4KB (small games)
- **Character-based graphics** - 26×13 character grid

#### Example Tier 1 Lesson: "Your First 2650 Sprite"
```asm
; Emerson Arcadia 2001 Assembly - Lesson 001
; Display hardware sprite using Signetics 2650
; 2650 @ 3.58 MHz

; Signetics 2650 is VERY unusual architecture:
; - 8-bit CPU with 7 general-purpose registers (R0-R6)
; - R0 is accumulator-like (most operations use R0)
; - Unique instruction set (different from 6502/Z80!)
; - PSU (Program Status Upper) and PSL (Program Status Lower)
; - Unusual addressing modes
; - Rarely used outside Arcadia 2001 and industrial controllers

        .cpu 2650

        .org $0000

; Arcadia 2001 hardware addresses
SPRITE0_X   = $2000     ; Sprite 0 X position
SPRITE0_Y   = $2001     ; Sprite 0 Y position
SPRITE0_COL = $2002     ; Sprite 0 color
SPRITE0_EN  = $2003     ; Sprite 0 enable
CONTROLLER1 = $2040     ; Controller 1 input
CONTROLLER2 = $2041     ; Controller 2 input

START:  ; Initialize 2650
        lodi,r0 $80             ; Load immediate to R0
        lpsu                    ; Load PSU (Program Status Upper)
        lodi,r0 $00
        lpsl                    ; Load PSL (Program Status Lower)

        ; Clear VRAM (1KB at $1000-$13FF)
        lodi,r3 $10             ; High byte of VRAM base
        lodi,r4 $00             ; Low byte
        lodi,r0 $00             ; Clear value
        lodi,r5 $04             ; Count (4 pages = 1KB)

CLEAR_PAGE:
        lodi,r6 $00             ; 256 bytes per page
CLEAR_LOOP:
        stra,r0 r3,r4,+         ; Store R0 to [R3:R4], increment R4
        bdrr,r6 CLEAR_LOOP      ; Decrement R6, branch if not zero
        addi,r3 $01             ; Next page
        bdrr,r5 CLEAR_PAGE      ; Decrement R5, branch if not zero

        ; Initialize sprite 0
        lodi,r1 64              ; X = 64 (center-ish)
        stra,r1 SPRITE0_X       ; Store X position
        lodi,r2 52              ; Y = 52 (center-ish)
        stra,r2 SPRITE0_Y       ; Store Y position
        lodi,r0 $06             ; Color yellow (6)
        stra,r0 SPRITE0_COL     ; Store color
        lodi,r0 $01             ; Enable sprite
        stra,r0 SPRITE0_EN      ; Enable

LOOP:   ; Main game loop
        ; Read controller 1
        loda,r0 CONTROLLER1     ; Load controller state
        andi,r0 $01             ; Check bit 0 (right)
        bctz,un MOVE_RIGHT      ; Branch if not zero

        ; Check left
        loda,r0 CONTROLLER1
        andi,r0 $02             ; Check bit 1 (left)
        bctz,un MOVE_LEFT

        ; Check down
        loda,r0 CONTROLLER1
        andi,r0 $04             ; Check bit 2 (down)
        bctz,un MOVE_DOWN

        ; Check up
        loda,r0 CONTROLLER1
        andi,r0 $08             ; Check bit 3 (up)
        bctz,un MOVE_UP

        br LOOP                 ; Branch unconditional

MOVE_RIGHT:
        ; Move sprite right
        loda,r1 SPRITE0_X       ; Load current X
        addi,r1 1               ; Increment
        cmpi,r1 128             ; Compare with edge
        bcfz,lt .UPDATE         ; Branch if less than
        lodi,r1 0               ; Wrap to left
.UPDATE:
        stra,r1 SPRITE0_X       ; Store new X
        br LOOP

MOVE_LEFT:
        ; Move sprite left
        loda,r1 SPRITE0_X       ; Load current X
        subi,r1 1               ; Decrement
        bcfz,gt .UPDATE2        ; Branch if greater than 0
        lodi,r1 127             ; Wrap to right
.UPDATE2:
        stra,r1 SPRITE0_X       ; Store new X
        br LOOP

MOVE_DOWN:
        ; Move sprite down
        loda,r2 SPRITE0_Y       ; Load current Y
        addi,r2 1               ; Increment
        cmpi,r2 104             ; Compare with bottom edge
        bcfz,lt .UPDATE3        ; Branch if less than
        lodi,r2 0               ; Wrap to top
.UPDATE3:
        stra,r2 SPRITE0_Y       ; Store new Y
        br LOOP

MOVE_UP:
        ; Move sprite up
        loda,r2 SPRITE0_Y       ; Load current Y
        subi,r2 1               ; Decrement
        bcfz,gt .UPDATE4        ; Branch if greater than 0
        lodi,r2 103             ; Wrap to bottom
.UPDATE4:
        stra,r2 SPRITE0_Y       ; Store new Y
        br LOOP

; No sound routines - Arcadia has only simple beeper
```

**Key teaching moment:** Emerson Arcadia 2001 cloned by 30+ manufacturers worldwide! Same hardware, different branding (Bandai in Japan, Emerson in USA, Hanimex in Australia, etc.). Signetics 2650 CPU is VERY unusual (rarely used, unique instruction set, different from 6502/Z80!). 128×208 vertical resolution (unusual!). 128 bytes RAM (extreme constraint, same as Atari 2600!). 4 hardware sprites (nice feature!). 51 games total across all variants. Commercial failure but fascinating licensing model for historical study.

**Tier progression:**
1. 2650 basics (unusual architecture, registers, instruction set)
2. Hardware sprites (4 sprites, positions, colors, enable)
3. 128 bytes RAM management (extreme constraint)
4. Controller input (analog joystick, 2 fire buttons)
5. VRAM manipulation (1KB character memory)
6. 8-color graphics (simple palette)
7. Character-based display (26×13 grid)
8. Simple beeper sound (basic audio)
9. Collision detection (software-based)
10. Animation (sprite movement patterns)
11. Two-player patterns (2 controllers)
12. Game state machines
13. AI patterns (simple enemy movement)
14. Clone compatibility testing (testing across variants)
15. Cartridge ROM optimization (2-4KB typical)
16. Complete Arcadia 2001 mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 2650 techniques, sprite mastery, RAM optimization, character graphics, clone variant testing

#### New Patterns:
- **2650 optimization** - Efficient register usage, unusual instruction combos
- **4-sprite choreography** - Coordinating all 4 hardware sprites
- **128-byte RAM mastery** - Fitting game state in minimal RAM
- **Character graphics** - 26×13 grid optimization, custom characters
- **8-color art** - Creative use of simple palette
- **Analog joystick** - Reading analog input (most games use digital)
- **Two-player coordination** - Dual controller patterns
- **Beeper sound patterns** - Simple but effective audio
- **Score/timer systems** - Minimal display space
- **AI within constraints** - Simple but effective opponents
- **Clone variant testing** - Ensuring compatibility across 30+ clones
- **ROM banking** - Larger games (rare, most games 2-4KB)

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Understanding clone variants and their minor differences
**Focus:** Clone manufacturer variations, regional differences, compatibility tricks

#### Phase 3 Enhancement: Clone Variants
- **Bandai Super Vision 8000** (Japan) - Same hardware, Japanese packaging
- **Emerson Arcadia 2001** (USA) - US branding
- **Leisure-Vision** (Canada) - Canadian market
- **Hanimex** (Australia) - Australian/European market
- **Intervision** (Switzerland) - European variant
- **Rowtron** (UK) - British market
- **30+ total manufacturers** - All electrically identical!
- **Different game names** - Same ROM, different labels
- **Regional power supplies** - Different voltages, same logic

**Note:** Arcadia variants are electrically identical. Phase 3 focuses on compatibility testing and understanding the clone phenomenon.

**Tier 40 Example - Clone Detection:**
```asm
; Detect which Arcadia clone we're running on
; (Actually impossible - they're 100% identical!)
; This demonstrates why compatibility is so good

DetectClone:
        ; There is NO WAY to detect clone variants!
        ; All Arcadia 2001 clones are electrically identical
        ; Same CPU, same memory map, same everything
        ; This is actually a STRENGTH - perfect compatibility!

        ; Best we can do: Display a message asking user
        ; which variant they have (for manual tracking)

        ; Display "Which Arcadia?" message
        lodi,r3 $10             ; VRAM base
        lodi,r4 $00
        lodi,r5 $00             ; Character counter

        ; Display message
.LOOP:  loda,r0 MESSAGE,r5,+    ; Load character from message
        cmpi,r0 $00             ; Check for null terminator
        bcfz,eq .DONE           ; Branch if zero
        stra,r0 r3,r4,+         ; Store to VRAM, increment
        br .LOOP

.DONE:  ret

MESSAGE:
        .text "WHICH ARCADIA?"
        .db $00                 ; Null terminator

; Because all clones are identical, any game works on any variant!
; This is actually IDEAL for software compatibility!
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional 2650 programming, extreme RAM efficiency, sprite mastery, character graphics optimization

#### Advanced Techniques:
- **2650 mastery** - Register choreography, efficient instruction sequences
- **128-byte RAM efficiency** - Maximum game complexity in minimal RAM
- **4-sprite maximum utilization** - Flickering techniques for >4 objects
- **Character graphics art** - Custom character sets, effective 26×13 layouts
- **8-color optimization** - Dithering, color choice for readability
- **Analog joystick precision** - Fine control (though most games ignore)
- **Beeper music** - Melodies and effects with simple beeper
- **Two-player sophistication** - Complex multiplayer interactions
- **AI optimization** - Smart opponents within severe constraints
- **ROM efficiency** - Complete games in 2-4KB
- **Clone market understanding** - Studying the licensing phenomenon

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games that work within Arcadia constraints

#### Genre Specializations:
- **Maze games** - Pac-Man style (character-based, perfect fit!)
- **Shooter games** - Space Invaders, Galaxian clones
- **Sports games** - Simple ball games (Tennis, Soccer)
- **Puzzle games** - Block puzzles, matching games
- **Two-player competitive** - Head-to-head games
- **Board games** - Chess, checkers (character display)
- **Action games** - Simple platformers, dodging games
- **Educational games** - Math, spelling (character-based UI)

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum complexity within extreme constraints

#### Limit-Pushing Techniques:
- **Maximum game in 2-4KB ROM** - Complete game, tiny space!
- **128 bytes RAM efficiency** - Every byte counts!
- **4-sprite flickering** - Displaying >4 objects via flicker
- **Character graphics mastery** - Complex scenes in 26×13 grid
- **8-color art complexity** - Dithering, shading techniques
- **Advanced analog control** - Using full joystick range (rare!)
- **Beeper showcase** - Complex audio with simple hardware
- **AI sophistication** - Smart opponents, minimal code/RAM
- **Two-player mastery** - Complex multiplayer mechanics
- **ROM banking tricks** - Rare but possible for larger games

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Best possible Arcadia games within constraints

#### Commercial Techniques:
- **Commercial quality** - Matching best original games
- **Character graphics polish** - Beautiful 26×13 displays
- **Sprite coordination** - Smooth 4-sprite choreography
- **Analog joystick ergonomics** - Natural control (even if digital)
- **Beeper audio polish** - Engaging sound effects
- **Two-player polish** - Engaging multiplayer
- **Extreme optimization** - Every byte/cycle optimized
- **Clone compatibility** - Testing across multiple variants

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - Excellent Arcadia 2001 + clone support
- **WinArcadia emulator** - Dedicated Arcadia emulator (excellent!)
- **Modern 2650 assemblers** - Cross-platform toolchains
- **Flash cartridges** - Homebrew development (rare but exist!)
- **Community preservation** - Arcadia preservation efforts
- **Clone phenomenon study** - Understanding licensing model
- **2650 knowledge** - Rare architecture expertise
- **Modern tools** - Emulator debugging features

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 optimization techniques
3. **Clone Patterns (Phase 3-4)** - 100 compatibility and variant understanding
4. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
5. **Polish Patterns (Phase 7)** - 75 professional touches
6. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~500 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-8: Emerson Arcadia 2001 + Clones (1982)**
- Signetics 2650 @ 3.58MHz (uncommon architecture!)
- 128 bytes RAM (extreme constraint!)
- 1KB VRAM (dedicated video memory)
- 128×208 resolution (unusual vertical format!)
- 8 colors (black, blue, red, magenta, green, cyan, yellow, white)
- 4 hardware sprites
- Character-based display (26×13 grid)
- Analog joysticks (2-button: fire A + fire B)
- Simple beeper audio
- Cartridge slot (2-4KB typical ROM)
- 30+ clone manufacturers (all electrically identical!)
- RF modulator (TV output)

**30+ Clone Variants (all compatible):**
- Bandai Super Vision 8000 (Japan)
- Emerson Arcadia 2001 (USA)
- Leisure-Vision (Canada)
- Hanimex HMG-2650 (Australia)
- Intervision 2001 (Switzerland)
- Rowtron Television Computer System (UK)
- Ormatu 2001 (Spain)
- Tunix Home Arcade (New Zealand)
- Many others across Europe, South America, Asia

**Phase 7-8: Modern Homebrew**
- Flash cartridges (rare, homebrew)
- Modern development tools (MAME, WinArcadia, 2650 assemblers)
- Homebrew community (small but active)

## Spiral Learning Example: Simple Maze Game (Perfect for Arcadia!)

**Phase 1 (Tier 1):** Player sprite, walls (characters), simple movement. (~100 lines)

**Phase 2 (Tier 17):** Maze layout, multiple enemies (flickering), score. (~250 lines)

**Phase 3 (Tier 33):** Testing across clone variants, compatibility verification. (~300 lines)

**Phase 4 (Tier 41):** Advanced AI, power-ups, levels. (~400 lines)

**Phase 5 (Tier 49):** Complete maze game, many levels, polish. (~500 lines)

**Phase 6 (Tier 53):** Maximum complexity, advanced enemy AI, all in 128 bytes RAM! (~600 lines)

**Phase 7 (Tier 57):** Polished game, commercial quality for 1982. (~700 lines)

**Phase 8 (Tier 59):** Modern homebrew, flash cart support, debugging. (~700 lines + tooling)

## Key Differences from Other Platforms

1. **30+ Clone Manufacturers** - Worldwide licensing phenomenon (unique!)
2. **Signetics 2650** - Uncommon CPU architecture (educational value!)
3. **128×208 Resolution** - Unusual vertical format (taller than wide!)
4. **128 Bytes RAM** - Extreme constraint (same as Atari 2600!)
5. **4 Hardware Sprites** - Nice feature for 1982
6. **Character-Based Display** - 26×13 grid (different approach)
7. **Analog Joysticks** - 8-way analog (though most games use digital)
8. **Clone Market Study** - Understanding licensing model
9. **51 Games Total** - Across all variants
10. **Commercial Failure** - But perfect compatibility success!

## Success Criteria

**By Phase 4, learners can:**
- Write Signetics 2650 assembly fluently (unusual architecture)
- Work within extreme constraints (128 bytes RAM!)
- Use 4 hardware sprites effectively
- Design character-based graphics (26×13 grid)
- Create 8-color graphics (simple palette optimization)
- Program analog joystick input
- Optimize for tiny ROM (2-4KB)
- Understand clone market phenomenon

**By Phase 8, learners can:**
- Develop commercial-quality Arcadia 2001 games
- Master Signetics 2650 architecture (rare expertise!)
- Work with modern homebrew tools (MAME, WinArcadia)
- Test compatibility across clone variants
- Contribute to Arcadia preservation
- Release homebrew cartridges
- Understand early console licensing models

## Resources Required

**Phase 1-2:**
- MAME emulator (excellent Arcadia 2001 + all clone support)
- WinArcadia emulator (dedicated, excellent for development!)
- Signetics 2650 assembler (modern toolchains)
- Text editor
- Emerson Arcadia 2001 reference documentation
- Signetics 2650 programming guides

**Phase 7-8:**
- Flash cartridge (rare, homebrew development)
- Arcadia 2001 hardware (optional, collector's item!)
- Modern development tools
- Community resources (preservation groups)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** Signetics 2650 mastery (rare architecture!), extreme constraint training (128B RAM!), understanding clone market phenomenon (30+ manufacturers!), character-based display techniques, 4-sprite hardware usage, studying licensing models in early console era, 2650 knowledge (industrial controller applications!)
