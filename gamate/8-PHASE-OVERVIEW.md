# Gamate Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Gamate (1990) → Taiwan's portable handheld
**Approach:** Game-first, pattern library, 6502 mastery, portable optimization
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Taiwan handheld (1990), Bit Corporation manufacturer, 6502-like CPU @ 4.43MHz, 160×152 resolution (unique!), 4 shades grayscale, Taiwan/Europe/Asia distribution, budget Game Boy competitor, link cable for 2-player, ~70 games total, 4× AA batteries (20+ hours), stereo audio (2-channel), $50-60 price, limited commercial success, discontinued early 1990s, interesting 6502-based handheld study

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Gamate shipped without BASIC. Curriculum begins directly with assembly, focused on the 6502-like architecture and portable game development.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 6502 fundamentals, 160×152 LCD, 4-shade grayscale, portable optimization, stereo audio
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **6502 patterns** - 6502-like CPU @ 4.43MHz (transfers to many platforms!)
- **160×152 LCD** - Unique vertical resolution!
- **4 shades grayscale** - White, light gray, dark gray, black
- **8KB RAM** - Standard for early handhelds
- **4KB VRAM** - Dedicated video memory
- **Hardware sprites** - 8×8 tiles
- **Stereo audio** - 2-channel PSG (left/right!)
- **D-pad + 4 buttons** - A, B, Select, Start
- **Link cable** - 2-player multiplayer
- **Portable optimization** - Battery life (4× AA, 20+ hours)

#### Example Tier 1 Lesson: "Your First Gamate Sprite"
```asm
; Gamate Assembly - Lesson 001
; Display sprite on 160×152 LCD
; 6502 @ 4.43 MHz

; 6502 architecture (classic!):
; - 8-bit accumulator (A)
; - Index registers X, Y
; - Stack pointer S (fixed page $01)
; - Processor flags (NVDIZC)
; - Zero page addressing ($00-$FF)
; - 256-byte stack ($0100-$01FF)

        .org    $4000           ; Cartridge ROM start

; Gamate memory map
RAM_BASE        = $0000         ; 8KB RAM at $0000-$1FFF
VRAM_BASE       = $2000         ; 4KB VRAM at $2000-$2FFF
LCD_CTRL        = $4000         ; LCD control register
LCD_X           = $4001         ; LCD X scroll
LCD_Y           = $4002         ; LCD Y scroll
SPRITE0_X       = $4010         ; Sprite 0 X position
SPRITE0_Y       = $4011         ; Sprite 0 Y position
SPRITE0_TILE    = $4012         ; Sprite 0 tile number
SPRITE0_ATTR    = $4013         ; Sprite 0 attributes
BUTTONS         = $4020         ; Button input
AUDIO_L         = $4030         ; Audio left channel
AUDIO_R         = $4031         ; Audio right channel
LINK_DATA       = $4040         ; Link cable data
LINK_CTRL       = $4041         ; Link cable control

; Entry point
START:  ; Initialize
        sei                     ; Disable interrupts
        cld                     ; Clear decimal mode
        ldx     #$FF
        txs                     ; Set stack pointer

        ; Initialize LCD
        lda     #$01
        sta     LCD_CTRL        ; Enable LCD

        ; Clear VRAM (4KB)
        ldx     #$00
        lda     #$00
.clear_page:
        sta     VRAM_BASE,x
        sta     VRAM_BASE+$100,x
        sta     VRAM_BASE+$200,x
        sta     VRAM_BASE+$300,x
        inx
        bne     .clear_page

        ; Load sprite tiles to VRAM
        ldx     #0
.load_tile:
        lda     SPRITE_DATA,x
        sta     VRAM_BASE,x
        inx
        cpx     #16             ; 16 bytes (8×8 tile)
        bne     .load_tile

        ; Initialize sprite 0
        lda     #80             ; X = 80 (center)
        sta     SPRITE0_X
        lda     #76             ; Y = 76 (center-ish)
        sta     SPRITE0_Y
        lda     #$00            ; Tile 0
        sta     SPRITE0_TILE
        lda     #$01            ; Visible
        sta     SPRITE0_ATTR

LOOP:   ; Main game loop
        ; Simple delay (wait for frame)
        ldx     #$FF
.delay1:
        ldy     #$FF
.delay2:
        dey
        bne     .delay2
        dex
        bne     .delay1

        ; Read buttons
        lda     BUTTONS
        and     #$01            ; Right?
        beq     .check_left

        ; Move right
        lda     SPRITE0_X
        clc
        adc     #1
        cmp     #160            ; Edge?
        bcc     .update_x
        lda     #0              ; Wrap

.update_x:
        sta     SPRITE0_X

.check_left:
        lda     BUTTONS
        and     #$02            ; Left?
        beq     .check_down

        ; Move left
        lda     SPRITE0_X
        sec
        sbc     #1
        bcs     .update_x2
        lda     #159            ; Wrap

.update_x2:
        sta     SPRITE0_X

.check_down:
        lda     BUTTONS
        and     #$04            ; Down?
        beq     .check_up

        ; Move down
        lda     SPRITE0_Y
        clc
        adc     #1
        cmp     #152            ; Edge?
        bcc     .update_y
        lda     #0              ; Wrap

.update_y:
        sta     SPRITE0_Y

.check_up:
        lda     BUTTONS
        and     #$08            ; Up?
        beq     .check_a

        ; Move up
        lda     SPRITE0_Y
        sec
        sbc     #1
        bcs     .update_y2
        lda     #151            ; Wrap

.update_y2:
        sta     SPRITE0_Y

.check_a:
        lda     BUTTONS
        and     #$10            ; A button?
        beq     .no_sound

        ; Play stereo beep
        lda     #$80            ; Frequency
        sta     AUDIO_L         ; Left channel
        lda     #$90            ; Slightly different frequency
        sta     AUDIO_R         ; Right channel (stereo!)

.no_sound:
        jmp     LOOP

; Sprite data (8×8 tile, 2 bits per pixel for 4 shades)
SPRITE_DATA:
        .byte   $3C,$3C,$7E,$7E,$FF,$FF,$FF,$FF
        .byte   $FF,$FF,$7E,$7E,$3C,$3C,$00,$00

; Interrupt vectors
        .org    $FFFA
        .word   START           ; NMI
        .word   START           ; RESET
        .word   START           ; IRQ
```

**Key teaching moment:** Gamate uses 6502 CPU @ 4.43MHz! Knowledge transfers to C64, NES, Apple II, Atari 8-bit! 160×152 resolution (unique vertical format!). 4 shades grayscale. Stereo audio (2-channel PSG, left/right!). Taiwan manufacturer (Bit Corporation). Link cable for 2-player. ~70 games. $50-60 price. Europe/Asia distribution. Limited success vs Game Boy. 6502 skills highly transferable!

**Tier progression:**
1. 6502 basics (A, X, Y registers, flags)
2. 160×152 LCD (unique resolution!)
3. 4-shade grayscale (palette programming)
4. VRAM tiles (4KB video memory)
5. Hardware sprites (8×8 tiles)
6. D-pad input (4 directions)
7. Button input (A, B, Select, Start)
8. Stereo audio (2-channel PSG, left/right!)
9. Link cable (2-player multiplayer)
10. Battery optimization (20+ hours)
11. Collision detection (software)
12. Animation (sprite/tile cycling)
13. Scrolling (X/Y registers)
14. Score display (LCD space)
15. Simple games (portable design)
16. Complete Gamate mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 6502 techniques, 4-shade art mastery, stereo audio, link cable multiplayer

#### New Patterns:
- **6502 optimization** - Efficient assembly code
- **4-shade art** - Creative grayscale graphics
- **160×152 mastery** - Effective vertical resolution usage
- **Hardware sprites** - Multiple sprite coordination
- **Stereo audio** - Left/right channel composition
- **Link cable protocols** - 2-player multiplayer
- **Scrolling techniques** - Smooth scrolling
- **Battery profiling** - 30+ hour optimization
- **ROM banking** - Larger games (128KB+ carts)
- **Zero page efficiency** - Fast 6502 patterns
- **8KB RAM management** - Game state optimization

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Advanced link cable and stereo features
**Focus:** Multiplayer mastery, stereo audio depth

#### Phase 3 Enhancement: Advanced Features
- **Link cable** - 2-player multiplayer support
- **Stereo audio** - Left/right PSG channels
- **No hardware variants** - Same hardware throughout
- **Regional distribution** - Taiwan, Europe, Asia

**Note:** Gamate had no actual hardware enhancements. Phase 3 focuses on advanced link cable and stereo audio techniques.

**Tier 40 Example - Stereo Audio Composition:**
```asm
; Stereo audio composition using left/right channels

PlayStereoMusic:
        ; Play melody on left channel
        ldx     #0
.melody_loop:
        lda     MELODY_L,x
        beq     .melody_done
        sta     AUDIO_L

        ; Delay for note duration
        ldy     #$FF
.note_delay:
        dey
        bne     .note_delay

        inx
        jmp     .melody_loop

.melody_done:
        ; Play harmony on right channel simultaneously
        ldx     #0
.harmony_loop:
        lda     MELODY_R,x
        beq     .done
        sta     AUDIO_R

        ; Delay
        ldy     #$FF
.delay:
        dey
        bne     .delay

        inx
        jmp     .harmony_loop

.done:
        rts

; Musical data (frequencies)
MELODY_L:       .byte   $80,$90,$A0,$B0,$C0,$00
MELODY_R:       .byte   $70,$80,$90,$A0,$B0,$00
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional 6502 programming, portable game mastery, stereo audio excellence

#### Advanced Techniques:
- **6502 mastery** - Cycle-perfect code
- **4-shade showcase** - Beautiful grayscale art
- **160×152 optimization** - Perfect vertical usage
- **Sprite coordination** - Many sprites via flickering
- **Stereo composition** - Complex left/right music
- **Link cable sophistication** - Advanced multiplayer
- **Scrolling mastery** - Smooth, responsive
- **Battery excellence** - 40+ hour optimization
- **ROM efficiency** - Large games optimized
- **Zero page mastery** - Fast 6502 patterns

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games optimized for 160×152 vertical screen

#### Genre Specializations:
- **Puzzle games** - Tetris, match-3
- **Action games** - Platformers, shooters
- **RPGs** - Turn-based adventures
- **Sports games** - Simple sports
- **Board games** - Chess, checkers
- **Arcade ports** - Classic arcade games
- **Link cable multiplayer** - 2-player competitive
- **Stereo showcases** - Audio-focused games

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum 6502 performance, stereo mastery

#### Limit-Pushing Techniques:
- **6502 optimization** - Every cycle optimized
- **4-shade mastery** - Best possible grayscale
- **160×152 maximum** - Perfect vertical design
- **Sprite flickering** - Many objects on-screen
- **Stereo showcase** - Complex dual-channel audio
- **Link cable mastery** - Advanced multiplayer protocols
- **Scrolling excellence** - Multi-layer effects
- **50+ hour battery** - Extreme optimization
- **ROM showcase** - Large-scale games

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Best possible Gamate games

#### Commercial Techniques:
- **Commercial quality** - Professional games
- **Grayscale polish** - Beautiful 4-shade art
- **Stereo excellence** - Engaging left/right audio
- **Portable perfection** - Ideal handheld experience
- **Link cable polish** - Engaging multiplayer
- **Battery perfection** - Long play sessions
- **Vertical screen mastery** - 160×152 optimization
- **Professional polish** - Commercial standards

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - Gamate emulation support
- **Modern 6502 toolchains** - cc65, ca65, modern assemblers
- **Flash cartridges** - Homebrew development (rare!)
- **Community techniques** - Gamate preservation
- **6502 knowledge** - Transfers to C64, NES, Apple II!
- **Modern tools** - Emulator debugging

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 optimization techniques
3. **Stereo/Link Patterns (Phase 3)** - 50 multiplayer + audio
4. **Mastery Patterns (Phase 4-5)** - 100 6502 + portable
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-8: Gamate (1990, Taiwan)**
- 6502-like CPU @ 4.43MHz
- 8KB RAM
- 4KB VRAM
- 160×152 LCD (unique vertical resolution!)
- 4 shades grayscale
- Hardware sprites (8×8 tiles)
- Stereo audio (2-channel PSG, left/right!)
- D-pad + 4 buttons (A, B, Select, Start)
- Link cable (2-player multiplayer)
- 4× AA batteries (20-40 hours)
- Cartridge slot (128KB typical)
- $50-60 price

**Distribution:**
- Taiwan (Bit Corporation)
- Europe
- Asia

**Phase 7-8: Modern Homebrew**
- Flash cartridges (rare, homebrew)
- Modern development tools (MAME, cc65)
- Homebrew community (very small)

## Spiral Learning Example: Puzzle Game (Vertical Screen!)

**Phase 1 (Tier 5):** Simple puzzle, blocks, 160×152 screen. (~90 lines)

**Phase 2 (Tier 21):** Advanced puzzle, stereo audio, scoring. (~220 lines)

**Phase 3 (Tier 37):** 2-player link cable mode, stereo music. (~300 lines)

**Phase 4 (Tier 45):** Complex puzzle rules, multiple modes. (~400 lines)

**Phase 5 (Tier 49):** Complete puzzle game, many levels. (~520 lines)

**Phase 6 (Tier 53):** Maximum complexity, beautiful 4-shade art. (~640 lines)

**Phase 7 (Tier 57):** Commercial quality puzzle game. (~760 lines)

**Phase 8 (Tier 59):** Modern homebrew, flash cart support. (~760 lines + tooling)

## Key Differences from Other Platforms

1. **6502 CPU** - Knowledge transfers to C64, NES, Apple II!
2. **160×152 Resolution** - Unique vertical format!
3. **Stereo Audio** - 2-channel PSG (left/right!)
4. **Taiwan Manufacturer** - Bit Corporation
5. **Link Cable** - 2-player multiplayer
6. **$50-60 Price** - Budget handheld
7. **~70 Games** - Small library
8. **Europe/Asia Distribution** - Regional focus
9. **4 Shades Grayscale** - Simple but effective
10. **6502 Transferable Skills** - Highly valuable!

## Success Criteria

**By Phase 4, learners can:**
- Write 6502 assembly fluently (transfers to C64, NES, Apple II!)
- Design for 160×152 vertical screen
- Create 4-shade grayscale graphics
- Program stereo audio (left/right channels)
- Implement link cable multiplayer
- Optimize for battery life (20-40 hours)
- Use hardware sprites effectively
- Manage 8KB RAM efficiently

**By Phase 8, learners can:**
- Develop commercial-quality Gamate games
- Master 6502 architecture (transfers to many platforms!)
- Work with modern homebrew tools (MAME, cc65)
- Create compelling portable games
- Contribute to Gamate preservation
- Release homebrew cartridges
- Apply 6502 skills across multiple platforms

## Resources Required

**Phase 1-2:**
- MAME emulator (Gamate support)
- cc65 or ca65 (6502 assembler/compiler)
- Text editor
- Gamate reference documentation
- 6502 programming guides

**Phase 7-8:**
- Flash cartridge (rare, homebrew)
- Gamate hardware (optional, collector's item!)
- Modern development tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** 6502 mastery (transfers to C64, NES, Apple II, Atari 8-bit!), 160×152 vertical screen design (unique!), stereo audio programming (left/right channels!), link cable multiplayer, portable game design, battery optimization, understanding Taiwan handheld market, 6502 knowledge highly transferable across multiple classic platforms!
