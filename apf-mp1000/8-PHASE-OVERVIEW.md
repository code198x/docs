# APF MP1000 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** APF MP1000 (1978-1980) → Early cartridge console with keyboard!
**Approach:** Game-first, pattern library, 6800 mastery, early cartridge era
**Gateway:** BASIC available (Imagination Machine add-on only) → Direct to assembly for MP1000
**Historical Note:** APF Electronics console (1978, USA), Motorola 6800 @ 3.57MHz, 256×192 resolution, 8 colors, built-in QWERTY keyboard (unique for game console!), cartridge-based, 2 controllers (joystick + numeric keypad on each), APF Imagination Machine (1979) = MP1000 + computer add-on (BASIC, cassette tape, 9KB RAM!), ~15 games (MP1000), more software for Imagination Machine, $130 launch (expensive!), competed with Atari 2600/Channel F, commercial failure, discontinued 1980, APF exited console market, interesting hybrid console/computer concept

## 8-Phase Structure

### Phase 0: BASIC Gateway (Imagination Machine Only)
**APF Imagination Machine (1979):** MP1000 console + computer add-on module
- **BASIC interpreter** - Microsoft BASIC variant
- **9KB RAM** - Expanded from 1KB console RAM!
- **Cassette interface** - Program storage
- **QWERTY keyboard** - Full keyboard (built into console)
- **Hybrid design** - Game console + home computer!

**Note:** Standard MP1000 had NO BASIC. Only Imagination Machine add-on provided BASIC programming. Phase 0 covers BASIC for those with Imagination Machine, but most MP1000 owners did NOT have this.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 6800 fundamentals, 256×192 graphics, 8-color limitations, keyboard + controllers, understanding hybrid console/computer concept
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **6800 patterns** - Motorola 6800 @ 3.57MHz (early 8-bit CPU!)
- **256×192 resolution** - High for 1978!
- **8 colors** - Simple palette
- **1KB RAM** - Minimal (9KB with Imagination Machine!)
- **Built-in keyboard** - QWERTY (unique for console!)
- **Dual controllers** - Joystick + numeric keypad on each
- **Character-based graphics** - 32×24 character grid
- **Cartridge ROM** - 8-16KB typical
- **Simple beeper audio** - 1-bit sound
- **Hybrid console/computer** - Imagination Machine expansion

#### Example Tier 1 Lesson: "Your First 6800 Game"
```asm
; APF MP1000 Assembly - Lesson 001
; Display sprite on 256×192 screen
; Motorola 6800 @ 3.57 MHz

; Motorola 6800 architecture:
; - 8-bit accumulator A, B (dual accumulators!)
; - 16-bit index register X
; - 16-bit stack pointer SP
; - 16-bit program counter PC
; - Condition codes: HINZVC
; - Simple, clean instruction set
; - No multiply/divide

        .org    $0000

; APF MP1000 memory map
ROM_BASE        = $0000         ; Cartridge ROM at $0000-$3FFF
RAM_BASE        = $6800         ; 1KB RAM at $6800-$6BFF
VRAM_BASE       = $4000         ; VRAM at $4000-$5FFF
VIDEO_CTRL      = $6C00         ; Video control port
COLOR_REG       = $6C01         ; Color register
SOUND_CTRL      = $6C02         ; Sound control
KEYBOARD        = $6C10         ; Keyboard input (QWERTY!)
JOY1            = $6C20         ; Joystick 1 port
JOY2            = $6C21         ; Joystick 2 port
KEY1            = $6C22         ; Keypad 1 (controller 1 numeric pad)
KEY2            = $6C23         ; Keypad 2 (controller 2 numeric pad)

START:  ; Initialize
        sei                     ; Disable interrupts
        lds     #$6BFF          ; Set stack pointer (top of RAM)

        ; Initialize video
        ldaa    #$01
        staa    VIDEO_CTRL      ; Enable video

        ; Clear VRAM
        ldx     #VRAM_BASE
        ldaa    #$00
.clear: staa    ,x
        inx
        cpx     #VRAM_BASE+$2000 ; 8KB VRAM
        bne     .clear

        ; Set 8-color palette
        ldaa    #%11100100      ; Palette bits
        staa    COLOR_REG

        ; Display title using keyboard keys!
        ; (MP1000's unique feature - built-in QWERTY!)
        ldx     #TITLE_TEXT
        ldy     #VRAM_BASE+64
        ldaa    #16
.text:  ldaa    ,x
        staa    ,y
        inx
        iny
        dec
        bne     .text

        ; Initialize player position
        ldaa    #128
        staa    PLAYER_X
        ldaa    #96
        staa    PLAYER_Y

MAIN_LOOP:
        ; Delay
        ldx     #$FFFF
.delay: dex
        bne     .delay

        ; Read joystick 1
        ldaa    JOY1
        staa    JOY_STATE

        ; Check right
        ldaa    JOY_STATE
        anda    #$01
        beq     .check_left
        ldaa    PLAYER_X
        inca
        cmpa    #$00
        bne     .update_x
        clra
.update_x:
        staa    PLAYER_X

.check_left:
        ldaa    JOY_STATE
        anda    #$02
        beq     .check_down
        ldaa    PLAYER_X
        deca
        staa    PLAYER_X

.check_down:
        ldaa    JOY_STATE
        anda    #$04
        beq     .check_up
        ldaa    PLAYER_Y
        inca
        cmpa    #192
        bne     .update_y
        clra
.update_y:
        staa    PLAYER_Y

.check_up:
        ldaa    JOY_STATE
        anda    #$08
        beq     .check_keypad
        ldaa    PLAYER_Y
        deca
        staa    PLAYER_Y

.check_keypad:
        ; Read numeric keypad on controller
        ldaa    KEY1
        anda    #$0F
        beq     .check_keyboard
        ; Keypad button pressed
        staa    SOUND_CTRL      ; Beep

.check_keyboard:
        ; Read QWERTY keyboard (unique to MP1000!)
        ldaa    KEYBOARD
        cmpa    #$00
        beq     .no_key
        ; Keyboard key pressed
        ; (Can use for game controls - unique!)

.no_key:
        ; Update sprite
        ldx     #VRAM_BASE
        ldaa    PLAYER_Y
        ldab    #32             ; 32 chars per row
        mul                     ; Y * 32 (6800 has no multiply!)
        ; Note: 6800 has NO multiply instruction!
        ; Need to implement multiply manually
        ; (Simplified for this example)

        jmp     MAIN_LOOP

; Data
PLAYER_X:       .db     128
PLAYER_Y:       .db     96
JOY_STATE:      .db     0
TITLE_TEXT:     .db     "APF MP1000!",0

; Interrupt vectors
        .org    $FFF8
        .word   START           ; IRQ
        .word   START           ; SWI
        .word   START           ; NMI
        .word   START           ; RESET
```

**Key teaching moment:** APF MP1000 has built-in QWERTY keyboard (unique for game console!). Motorola 6800 @ 3.57MHz (early 8-bit CPU, no multiply!). 256×192 resolution (high for 1978!). Dual controllers with joystick + numeric keypad on each. APF Imagination Machine (1979) = MP1000 + computer add-on (BASIC, cassette, 9KB RAM!). ~15 games. $130 launch (expensive!). Competed with Atari 2600 (1977). Commercial failure, discontinued 1980. Interesting hybrid console/computer concept!

**Tier progression:**
1. 6800 basics (A, B accumulators, X index register, no multiply!)
2. 256×192 graphics (high resolution for 1978!)
3. Character-based display (32×24 grid)
4. 8-color palette (simple colors)
5. VRAM manipulation (8KB video memory)
6. Joystick input (2 controllers, 8-way)
7. Numeric keypad input (on controllers!)
8. QWERTY keyboard input (built-in, unique!)
9. Simple beeper audio (1-bit sound)
10. 1KB RAM management (extreme constraint!)
11. Imagination Machine (9KB RAM expansion, BASIC, cassette)
12. Collision detection (software)
13. Animation (character cycling)
14. Two-player patterns (dual controllers)
15. Keyboard-based games (unique to MP1000!)
16. Complete MP1000 mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 6800 techniques, keyboard creativity, Imagination Machine programming

#### New Patterns:
- **6800 optimization** - Efficient code (no multiply/divide!)
- **256×192 mastery** - High-resolution graphics
- **8-color art** - Effective palette usage
- **Character graphics** - Creative 8×8 designs
- **Keyboard creativity** - QWERTY for game input!
- **Controller + keypad** - Hybrid control schemes
- **1KB RAM efficiency** - Extreme constraint
- **Imagination Machine** - 9KB RAM, BASIC, cassette
- **Beeper patterns** - Simple 1-bit audio effects
- **Two-player depth** - Dual controller games
- **Hybrid console/computer** - Understanding unique positioning

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - APF Imagination Machine (1979)
**Focus:** Imagination Machine computer add-on, BASIC programming, 9KB RAM

#### Phase 3 Enhancement: APF Imagination Machine (1979)
- **Imagination Machine** - Computer add-on for MP1000
- **9KB RAM** - Expanded from 1KB console!
- **Microsoft BASIC** - Programming language
- **Cassette interface** - Program storage
- **QWERTY keyboard** - Full keyboard (built-in MP1000)
- **Hybrid system** - Game console + home computer!
- **More software** - Educational, productivity apps
- **Higher price** - $700 complete system!

**Tier 40 Example - Imagination Machine Detection:**
```asm
; Detect if Imagination Machine is connected

DetectImaginationMachine:
        ; Try to write to expanded RAM
        ldaa    #$AA
        staa    $7000           ; Beyond 1KB console RAM
        ldaa    $7000
        cmpa    #$AA
        beq     has_imagination

no_imagination:
        ; Standard MP1000 (1KB RAM)
        ldaa    #0
        staa    RAM_TYPE
        rts

has_imagination:
        ; Imagination Machine (9KB RAM!)
        ldaa    #1
        staa    RAM_TYPE
        ; Can now use BASIC, cassette, more RAM
        rts

RAM_TYPE:       .db     0       ; 0=MP1000, 1=Imagination Machine
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional 6800 programming, keyboard game design, Imagination Machine mastery

#### Advanced Techniques:
- **6800 mastery** - Cycle-perfect code
- **256×192 optimization** - Maximum resolution usage
- **8-color showcase** - Beautiful limited palette
- **Character mastery** - Complex 8×8 art
- **Keyboard game design** - QWERTY-centric games!
- **Hybrid controls** - Joystick + keypad + keyboard
- **1KB RAM mastery** - Extreme efficiency (or 9KB with IM)
- **Imagination Machine** - BASIC + assembly hybrid
- **Cassette I/O** - Program loading/saving
- **Beeper depth** - Complex 1-bit audio

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games leveraging keyboard, hybrid console/computer features

#### Genre Specializations:
- **Keyboard-centric games** - Text adventures, typing games
- **Educational software** - Imagination Machine focus
- **Puzzle games** - Keyboard + joystick hybrid
- **Action games** - Traditional controller games
- **Strategy games** - Keyboard for complex input
- **Two-player competitive** - Dual controller games
- **BASIC + assembly** - Hybrid programming (IM)
- **Productivity apps** - Imagination Machine software

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum capability despite 1KB RAM, keyboard mastery

#### Limit-Pushing Techniques:
- **6800 maximum** - Every cycle optimized
- **256×192 showcase** - Best possible graphics
- **8-color mastery** - Beautiful palette art
- **Keyboard showcase** - QWERTY game mastery
- **1KB RAM showcase** - Complex games, tiny memory!
- **9KB RAM utilization** - Imagination Machine max
- **BASIC + assembly** - Hybrid programming depth
- **Cassette efficiency** - Fast loading/saving
- **Beeper excellence** - Complex 1-bit audio

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Best possible MP1000 and Imagination Machine software

#### Commercial Techniques:
- **Commercial quality** - Professional game development
- **Graphics polish** - Beautiful 256×192 graphics
- **Keyboard excellence** - QWERTY-optimized games
- **Imagination Machine showcase** - Full computer capabilities
- **Audio polish** - Engaging beeper sound
- **Hybrid polish** - Console + computer strengths
- **Historical authenticity** - 1978-1980 experience
- **Professional standards** - Late 1970s quality

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - APF MP1000 and Imagination Machine support
- **Modern 6800 toolchains** - Cross-assemblers
- **Flash cartridges** - Homebrew development (very rare!)
- **Community techniques** - APF preservation (tiny scene)
- **6800 knowledge** - Transfers to other Motorola systems
- **Historical research** - Understanding hybrid console/computer
- **Modern tools** - Emulator debugging

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Keyboard Patterns (Phase 2)** - 75 QWERTY techniques
3. **Imagination Machine Patterns (Phase 3)** - 50 computer add-on
4. **Mastery Patterns (Phase 4-5)** - 100 6800 + keyboard
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: APF MP1000 (1978-1980)**
- Motorola 6800 @ 3.57MHz (no multiply!)
- 1KB RAM
- 8KB VRAM
- 256×192 resolution (high for 1978!)
- 8 colors
- Character-based display (32×24 grid)
- Built-in QWERTY keyboard (unique!)
- 2 controllers (joystick + numeric keypad on each)
- Simple beeper audio (1-bit)
- Cartridge slot (8-16KB typical ROM)
- RF modulator (TV output)
- $130 launch price
- ~15 games

**Phase 3+: APF Imagination Machine (1979)**
- Same MP1000 console + computer add-on
- 9KB RAM (expanded from 1KB!)
- Microsoft BASIC interpreter
- Cassette tape interface
- QWERTY keyboard (built-in MP1000)
- Home computer functionality
- Educational and productivity software
- $700 complete system price

**Phase 7-8: Modern Homebrew**
- Flash cartridges (very rare, homebrew)
- Modern development tools (MAME, 6800 assemblers)
- Homebrew community (almost non-existent)

## Spiral Learning Example: Keyboard-Based Game (Unique to MP1000!)

**Phase 1 (Tier 15):** Simple typing game, QWERTY input, character display. (~120 lines)

**Phase 2 (Tier 31):** Text adventure, keyboard + joystick, beeper audio. (~300 lines)

**Phase 3 (Tier 39):** Imagination Machine version, 9KB RAM, BASIC hybrid. (~450 lines)

**Phase 4 (Tier 47):** Complex keyboard game, word puzzles, education. (~600 lines)

**Phase 5 (Tier 50):** Complete keyboard-centric game (unique MP1000 strength!). (~750 lines)

**Phase 6 (Tier 53):** Maximum keyboard usage, complex input patterns. (~900 lines)

**Phase 7 (Tier 57):** Commercial quality keyboard game. (~1050 lines)

**Phase 8 (Tier 59):** Modern homebrew, historical significance. (~1050 lines + tooling)

## Key Differences from Other Platforms

1. **Built-in QWERTY Keyboard** - Unique for game console!
2. **Imagination Machine** - Hybrid console/computer add-on
3. **Motorola 6800** - No multiply/divide instructions!
4. **256×192 Resolution** - High for 1978!
5. **Dual Controllers** - Joystick + numeric keypad on each
6. **1KB RAM** - Extreme constraint (9KB with IM)
7. **$130/$700 Price** - Expensive (console/complete system)
8. **~15 Games** - Small library
9. **1978-1980** - Early cartridge era
10. **Commercial Failure** - APF exited console market

## Success Criteria

**By Phase 4, learners can:**
- Write 6800 assembly fluently (no multiply workarounds!)
- Design for 256×192 high resolution
- Create keyboard-centric games (unique!)
- Program hybrid joystick + keypad + keyboard controls
- Work with 1KB RAM constraint (or 9KB with IM)
- Integrate BASIC + assembly (Imagination Machine)
- Use cassette I/O (program storage)
- Understand early hybrid console/computer concept

**By Phase 8, learners can:**
- Develop commercial-quality APF MP1000 games
- Master 6800 architecture
- Work with modern homebrew tools (MAME)
- Create innovative keyboard-based games
- Contribute to APF preservation
- Release homebrew cartridges (very rare!)
- Understand hybrid console/computer market positioning

## Resources Required

**Phase 1-2:**
- MAME emulator (APF MP1000 + Imagination Machine support)
- 6800 assembler
- Text editor
- APF MP1000 reference documentation
- Motorola 6800 programming guides

**Phase 7-8:**
- Flash cartridge (very rare, homebrew)
- APF MP1000/Imagination Machine hardware (optional, rare!)
- Modern development tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** 6800 mastery (Motorola architecture!), built-in QWERTY keyboard programming (unique for console!), keyboard-centric game design, hybrid console/computer concept (Imagination Machine!), early cartridge era study (1978!), understanding hybrid positioning, 256×192 high-resolution graphics, 1KB RAM extreme constraint, 6800 knowledge transfers to other Motorola systems!
