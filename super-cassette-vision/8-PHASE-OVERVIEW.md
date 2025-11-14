# Super Cassette Vision Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Epoch Super Cassette Vision (1984) → Japan's Famicom competitor
**Approach:** Game-first, pattern library, µPD7801G mastery, extreme constraints
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Epoch's second console (1984, Japan-only), NEC µPD7801G @ 4MHz (Z80-like 8-bit CPU), 128×64 resolution (very low!), 1KB RAM, 512 bytes VRAM, 16 colors (4 on-screen simultaneously), 3-channel beeper audio, 2 paddle controllers + buttons, 30 games total, competed with Famicom but lost, 1.5 million units sold (modest success!), successor to Cassette Vision (1981), Japan-only market, discontinued 1987, interesting CPU architecture (µPD78xx family)

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Super Cassette Vision shipped without BASIC. Curriculum begins directly with assembly, focused on the NEC µPD7801G architecture and extreme resolution constraints.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** µPD7801G fundamentals, 128×64 low resolution, 1KB RAM constraint, 4-color limitations, paddle controllers
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **µPD7801G patterns** - NEC µPD7801G @ 4MHz (Z80-like but unique!)
- **128×64 resolution** - Very low resolution (extreme constraint!)
- **1KB RAM** - Minimal memory
- **512 bytes VRAM** - Dedicated video memory
- **16-color palette** - 4 colors on-screen simultaneously
- **3-channel beeper** - Simple audio
- **Paddle controllers** - Analog paddles + 2 buttons each
- **Cartridge ROM** - Typically 4-16KB
- **Character-based graphics** - 16×8 character grid
- **Sprite system** - 8 movable objects

#### Example Tier 1 Lesson: "Your First µPD7801G Sprite"
```asm
; Super Cassette Vision Assembly - Lesson 001
; Display sprite using NEC µPD7801G
; µPD7801G @ 4 MHz

; NEC µPD7801G architecture:
; - 8-bit CPU, Z80-like but different!
; - Accumulator A (8-bit)
; - Register pairs BC, DE, HL (like Z80)
; - Unique instruction set (NOT Z80 compatible!)
; - µPD78xx family (industrial controllers, early consoles)
; - Stack pointer
; - Flags: Zero, Carry, Sign, etc.

        .cpu    78c10           ; µPD7801G compatible

        .org    $0000

; Super Cassette Vision hardware addresses
VRAM_BASE       = $3000         ; VRAM at $3000-$31FF (512 bytes)
SPRITE_X        = $3200         ; Sprite 0 X position
SPRITE_Y        = $3201         ; Sprite 0 Y position
SPRITE_CHAR     = $3202         ; Sprite 0 character
SPRITE_COLOR    = $3203         ; Sprite 0 color
PADDLE1         = $3300         ; Paddle 1 input
BUTTON1         = $3301         ; Button 1 input
SOUND_CH1       = $3400         ; Sound channel 1
SOUND_CH2       = $3401         ; Sound channel 2
SOUND_CH3       = $3402         ; Sound channel 3

START:  ; Initialize µPD7801G
        lxi     sp,$1400        ; Set stack pointer (top of RAM)

        ; Clear VRAM (512 bytes)
        lxi     h,VRAM_BASE     ; HL = VRAM base
        mvi     b,0             ; B = 0 (256 bytes × 2)
        mvi     c,2             ; C = 2 pages
        xra     a               ; A = 0 (clear value)

CLEAR_OUTER:
        mov     m,a             ; Store 0 to [HL]
        inx     h               ; Increment HL
        dcr     b               ; Decrement B
        jnz     CLEAR_OUTER     ; Loop until B = 0
        dcr     c               ; Decrement page count
        jnz     CLEAR_OUTER     ; Loop until C = 0

        ; Set background color
        mvi     a,$00           ; Black background
        sta     VRAM_BASE       ; Store to VRAM

        ; Initialize sprite 0
        mvi     a,64            ; X = 64 (center)
        sta     SPRITE_X
        mvi     a,32            ; Y = 32 (center)
        sta     SPRITE_Y
        mvi     a,$01           ; Character 1 (square)
        sta     SPRITE_CHAR
        mvi     a,$0E           ; Color yellow (from 16-color palette)
        sta     SPRITE_COLOR

LOOP:   ; Main game loop
        ; Read paddle 1
        lda     PADDLE1         ; Load paddle value (0-255)
        mov     b,a             ; Save to B

        ; Read button 1
        lda     BUTTON1
        ani     $01             ; Check button 1
        jz      NO_BUTTON       ; Skip if not pressed

        ; Button pressed - move sprite right
        lda     SPRITE_X
        inr     a               ; Increment X
        cpi     128             ; Compare with right edge
        jc      UPDATE_X        ; Jump if < 128
        mvi     a,0             ; Wrap to left
UPDATE_X:
        sta     SPRITE_X

NO_BUTTON:
        ; Use paddle for Y position
        mov     a,b             ; Get paddle value
        rrc                     ; Divide by 2 (0-127 range)
        cpi     64              ; Compare with max Y
        jc      UPDATE_Y
        mvi     a,63            ; Clamp to max
UPDATE_Y:
        sta     SPRITE_Y

        ; Play beep on button press
        lda     BUTTON1
        ani     $01
        jz      NO_SOUND
        mvi     a,$80           ; Frequency
        sta     SOUND_CH1       ; Play on channel 1

NO_SOUND:
        ; Simple delay
        lxi     d,$0200         ; Delay counter
DELAY:  dcx     d               ; Decrement DE
        mov     a,d
        ora     e               ; Check if DE = 0
        jnz     DELAY

        jmp     LOOP            ; Loop forever

; Sprite character data would be defined in ROM
; Super Cassette Vision uses 8×8 character blocks
```

**Key teaching moment:** Super Cassette Vision uses NEC µPD7801G - Z80-like but NOT compatible! µPD78xx CPU family (industrial controllers, early consoles). 128×64 resolution (VERY low, extreme constraint!). 1KB RAM. 16 colors but only 4 on-screen simultaneously. Paddle controllers (analog!) + buttons. 30 games total. Competed with Famicom in Japan (1984) but lost. 1.5 million units sold (modest success!). Japan-only. Successor to Cassette Vision (1981).

**Tier progression:**
1. µPD7801G basics (Z80-like, accumulator, register pairs)
2. 128×64 graphics (extreme low resolution!)
3. 1KB RAM management (minimal memory)
4. VRAM manipulation (512 bytes character memory)
5. 4-color limitations (choosing from 16-color palette)
6. Paddle input (analog controllers!)
7. Button input (2 buttons per controller)
8. Character-based graphics (16×8 grid)
9. 8 movable sprites (hardware sprite system)
10. 3-channel beeper audio (simple sound)
11. Collision detection (software-based)
12. Animation (sprite cycling)
13. Two-player patterns (2 controllers)
14. Game state machines
15. AI patterns (within 1KB RAM!)
16. Complete Super Cassette Vision mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced µPD7801G techniques, creative low-resolution graphics, paddle game design, 1KB RAM mastery

#### New Patterns:
- **µPD7801G optimization** - Efficient instruction sequences
- **128×64 creativity** - Effective graphics despite low resolution
- **4-color art** - Strategic palette choices from 16 colors
- **1KB RAM mastery** - Fitting game logic in minimal memory
- **Character graphics** - Custom 8×8 character designs
- **8-sprite choreography** - Coordinating all hardware sprites
- **Paddle precision** - Analog input handling (breakout-style games!)
- **3-channel audio** - Simple but effective sound design
- **Cartridge ROM optimization** - 4-16KB typical
- **Two-player coordination** - Dual paddle patterns
- **Collision efficiency** - Fast collision in limited CPU
- **Score display** - Minimal character space

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Understanding hardware limitations and workarounds
**Focus:** No hardware enhancements exist, focus on mastering constraints

#### Phase 3 Enhancement: N/A
- **No hardware enhancements** - Super Cassette Vision had no expansions
- **Same hardware throughout** - All units identical
- **Focus:** Mastering the constraints creatively

**Note:** Super Cassette Vision had no actual hardware enhancements. Phase 3 focuses on advanced constraint mastery and creative problem-solving within severe limitations.

**Tier 40 Example - Maximum Sprite Flickering:**
```asm
; Display >8 sprites via flickering technique

MAX_OBJECTS     = 16            ; Want 16 objects, have 8 sprites

FlickerSprites:
        ; Alternate which objects are visible each frame
        lda     frame_count     ; Load frame counter
        ani     $01             ; Odd or even frame?
        jnz     show_odd

show_even:
        ; Show objects 0,2,4,6,8,10,12,14 on sprite 0-7
        lxi     h,objects       ; Object array
        lxi     d,SPRITE_X      ; Sprite hardware
        mvi     b,8             ; 8 sprites
        mvi     c,0             ; Even offset (0,2,4...)

.loop_even:
        mov     a,c             ; Get object index
        rrc                     ; Multiply by object size
        rrc
        rrc
        mov     e,a
        mvi     d,0
        dad     d               ; HL = object address

        mov     a,m             ; Load object X
        stax    d               ; Store to sprite X
        inx     d
        inx     h
        mov     a,m             ; Load object Y
        stax    d               ; Store to sprite Y
        inx     d
        inx     h

        inr     c               ; Next even object
        inr     c
        dcr     b
        jnz     .loop_even
        ret

show_odd:
        ; Show objects 1,3,5,7,9,11,13,15 on sprite 0-7
        ; (Similar logic for odd objects)
        ret

objects:        .space  128     ; 16 objects × 8 bytes each
frame_count:    .db     0
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional µPD7801G programming, extreme constraint mastery, creative low-resolution design

#### Advanced Techniques:
- **µPD7801G mastery** - Cycle-efficient code
- **128×64 mastery** - Beautiful graphics despite resolution
- **1KB RAM efficiency** - Complex games in minimal memory
- **4-color art complexity** - Dithering, effective palettes
- **Character graphics art** - Creative 8×8 designs
- **8-sprite maximum utilization** - Flickering for >8 objects
- **Paddle game design** - Breakout, Pong, Arkanoid-style
- **3-channel music** - Melodies despite simple beeper
- **ROM efficiency** - Complete games in 4-16KB
- **Two-player polish** - Engaging paddle games

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games that work within severe constraints (paddles, low resolution)

#### Genre Specializations:
- **Paddle games** - Breakout, Pong (perfect for SCV!)
- **Simple shooters** - Space Invaders-style
- **Maze games** - Pac-Man clones (character-based!)
- **Puzzle games** - Block puzzles, Tetris-style
- **Sports games** - Simple ball games (Tennis, Hockey)
- **Action games** - Dodging, simple platformers
- **Two-player competitive** - Head-to-head paddle games
- **Board games** - Simple board game adaptations

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum complexity within extreme constraints

#### Limit-Pushing Techniques:
- **Maximum game in 4-16KB ROM** - Complete games, small space
- **1KB RAM efficiency** - Every byte critical!
- **128×64 maximum detail** - Best possible low-res graphics
- **8-sprite flickering mastery** - Displaying many objects
- **4-color art showcase** - Beautiful constrained palettes
- **Paddle precision mastery** - Perfect analog control
- **3-channel audio showcase** - Complex beeper music
- **Character graphics mastery** - Creative 8×8 art
- **Collision optimization** - Fast detection, minimal CPU

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Best possible Super Cassette Vision games

#### Commercial Techniques:
- **Commercial quality** - Matching best original 30 games
- **Low-resolution polish** - Beautiful 128×64 graphics
- **Paddle game perfection** - Perfect Breakout-style games
- **4-color art mastery** - Effective palette usage
- **Audio polish** - Engaging 3-channel sound
- **Two-player excellence** - Competitive paddle games
- **Extreme optimization** - Every byte/cycle optimized
- **Historical authenticity** - 1984 gaming experience

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - Super Cassette Vision support
- **Modern µPD78xx toolchains** - Cross-platform assemblers
- **Flash cartridges** - Homebrew development (rare!)
- **Community preservation** - Super Cassette Vision scene
- **µPD78xx knowledge** - Industrial controller applications
- **Modern tools** - Emulator debugging features
- **Historical research** - Understanding Japanese market (1984)

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 optimization techniques
3. **Constraint Patterns (Phase 3-4)** - 100 extreme constraint mastery
4. **Genre Patterns (Phase 5-6)** - 150 paddle game specializations
5. **Polish Patterns (Phase 7)** - 75 professional touches
6. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~500 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-8: Super Cassette Vision (1984, Japan-only)**
- NEC µPD7801G @ 4MHz (Z80-like but unique!)
- 1KB RAM
- 512 bytes VRAM
- 128×64 resolution (very low!)
- 16-color palette (4 on-screen simultaneously)
- 8 hardware sprites (8×8 characters)
- Character-based graphics (16×8 grid)
- 3-channel beeper audio
- 2 paddle controllers (analog!) + 2 buttons each
- Cartridge slot (4-16KB typical ROM)
- RF modulator (TV output)
- 30 games total
- 1.5 million units sold

**Phase 7-8: Modern Homebrew**
- Flash cartridges (rare, homebrew)
- Modern development tools (MAME, µPD78xx assemblers)
- Homebrew community (very small)

## Spiral Learning Example: Paddle Game (Perfect for SCV!)

**Phase 1 (Tier 5):** Simple paddle game, ball, brick, 128×64 graphics. (~80 lines)

**Phase 2 (Tier 21):** Multiple bricks, score, power-ups, 3-channel audio. (~180 lines)

**Phase 3 (Tier 37):** Advanced paddle physics, ball spin. (~220 lines)

**Phase 4 (Tier 45):** Complex brick layouts, multiple levels. (~300 lines)

**Phase 5 (Tier 49):** Complete Breakout-style game, many levels. (~380 lines)

**Phase 6 (Tier 53):** Maximum complexity, two-player mode, all in 1KB RAM! (~450 lines)

**Phase 7 (Tier 57):** Polished game, commercial quality for 1984. (~500 lines)

**Phase 8 (Tier 59):** Modern homebrew, flash cart support. (~500 lines + tooling)

## Key Differences from Other Platforms

1. **NEC µPD7801G** - Z80-like but NOT compatible (unique!)
2. **128×64 Resolution** - Extremely low (severe constraint!)
3. **1KB RAM** - Minimal memory
4. **4 Colors On-Screen** - From 16-color palette
5. **Paddle Controllers** - Analog paddles (unique control!)
6. **Japan-Only** - Never exported
7. **1.5M Units** - Modest success (vs Famicom's dominance)
8. **30 Games Total** - Small library
9. **Competed with Famicom** - Lost to Nintendo
10. **Epoch Console** - Successor to Cassette Vision (1981)

## Success Criteria

**By Phase 4, learners can:**
- Write µPD7801G assembly fluently (Z80-like architecture)
- Work within extreme constraints (1KB RAM, 128×64!)
- Create effective 4-color graphics (from 16 palette)
- Design character-based graphics (16×8 grid)
- Program paddle controllers (analog input)
- Use 8 hardware sprites effectively
- Create 3-channel beeper music
- Optimize for tiny ROM (4-16KB)

**By Phase 8, learners can:**
- Develop commercial-quality Super Cassette Vision games
- Master µPD7801G architecture
- Work with modern homebrew tools (MAME)
- Create compelling low-resolution graphics
- Contribute to Super Cassette Vision preservation
- Release homebrew cartridges
- Understand Japanese console market (1984)

## Resources Required

**Phase 1-2:**
- MAME emulator (Super Cassette Vision support)
- µPD78xx assembler (modern toolchains)
- Text editor
- Super Cassette Vision reference documentation
- NEC µPD7801G programming guides

**Phase 7-8:**
- Flash cartridge (rare, homebrew)
- Super Cassette Vision hardware (optional, collector's item!)
- Modern development tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** µPD7801G mastery (Z80-like but unique!), extreme constraint training (1KB RAM, 128×64!), paddle game design, understanding Japanese market (1984), µPD78xx knowledge (industrial controllers!), low-resolution graphics creativity, 4-color palette mastery
