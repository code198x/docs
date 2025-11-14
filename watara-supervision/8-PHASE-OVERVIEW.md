# Watara Supervision Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Watara Supervision (1992) → Budget Game Boy competitor
**Approach:** Game-first, pattern library, 65SC02-like CPU mastery, portable optimization
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Taiwan handheld (1992), 65SC02-like CPU @ 4MHz (6502-derived!), 160×160 resolution (square LCD!), 4 shades grayscale, budget Game Boy competitor ($50-70 vs $90 GB), Watara manufacturer, sold as Supervision/QuickShot Supervision/Hartung Supervision (rebrands), Europe/USA/Asia distribution, ~65 games, portable with 4× AA batteries (20+ hours!), link cable for multiplayer, TV adapter available, limited commercial success, discontinued mid-1990s, interesting CPU architecture

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Watara Supervision shipped without BASIC. Curriculum begins directly with assembly, focused on the 65SC02-like architecture and budget portable constraints.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 65SC02-like fundamentals, 160×160 LCD, 4-shade grayscale, portable optimization, battery efficiency
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **65SC02-like patterns** - 6502-derived CPU @ 4MHz (unusual variant!)
- **160×160 LCD** - Square screen (unique resolution!)
- **4 shades grayscale** - White, light gray, dark gray, black
- **8KB RAM** - Reasonable for 1992 handheld
- **4KB VRAM** - Dedicated video memory
- **Portable optimization** - Battery life critical (20+ hours!)
- **D-pad + 4 buttons** - A, B, Select, Start
- **Link cable** - 2-player multiplayer
- **TV adapter** - Optional accessory
- **Cartridge ROM** - 128KB-1MB typical

#### Example Tier 1 Lesson: "Your First Supervision Sprite"
```asm
; Watara Supervision Assembly - Lesson 001
; Display sprite on 160×160 LCD
; 65SC02-like CPU @ 4 MHz

; Watara Supervision CPU architecture:
; - 6502-derived (similar to 65SC02)
; - 8-bit accumulator (A)
; - Index registers X, Y
; - Stack pointer S
; - Processor flags (NVDIZC)
; - Zero page addressing
; - 256-byte stack ($0100-$01FF)

        .org    $0000

; Watara Supervision memory map
RAM_BASE        = $0000         ; 8KB RAM at $0000-$1FFF
VRAM_BASE       = $4000         ; 4KB VRAM at $4000-$4FFF
LCD_CTRL        = $2000         ; LCD control register
LCD_X           = $2001         ; LCD X scroll
LCD_Y           = $2002         ; LCD Y scroll
SPRITE0_X       = $2010         ; Sprite 0 X position
SPRITE0_Y       = $2011         ; Sprite 0 Y position
SPRITE0_TILE    = $2012         ; Sprite 0 tile number
SPRITE0_ATTR    = $2013         ; Sprite 0 attributes
BUTTONS         = $2020         ; Button input
DMA_SRC_L       = $2030         ; DMA source low
DMA_SRC_H       = $2031         ; DMA source high
DMA_DST_L       = $2032         ; DMA dest low
DMA_DST_H       = $2033         ; DMA dest high
DMA_LEN         = $2034         ; DMA length
DMA_CTRL        = $2035         ; DMA control

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
.clear: sta     VRAM_BASE,x
        sta     VRAM_BASE+$100,x
        sta     VRAM_BASE+$200,x
        sta     VRAM_BASE+$300,x
        inx
        bne     .clear

        ; Load sprite tiles to VRAM (using DMA)
        lda     #<SPRITE_DATA
        sta     DMA_SRC_L
        lda     #>SPRITE_DATA
        sta     DMA_SRC_H
        lda     #<VRAM_BASE
        sta     DMA_DST_L
        lda     #>VRAM_BASE
        sta     DMA_DST_H
        lda     #64             ; 64 bytes (8×8 tile)
        sta     DMA_LEN
        lda     #$01            ; Start DMA
        sta     DMA_CTRL

        ; Initialize sprite 0
        lda     #80             ; X = 80 (center)
        sta     SPRITE0_X
        lda     #80             ; Y = 80 (center)
        sta     SPRITE0_Y
        lda     #$00            ; Tile 0
        sta     SPRITE0_TILE
        lda     #$01            ; Visible, no flip
        sta     SPRITE0_ATTR

LOOP:   ; Main game loop
        ; Wait for VBlank (simple delay for this example)
        ldx     #$FF
.wait1: ldy     #$FF
.wait2: dey
        bne     .wait2
        dex
        bne     .wait1

        ; Read buttons
        lda     BUTTONS
        and     #$01            ; Right button?
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
        and     #$02            ; Left button?
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
        and     #$04            ; Down button?
        beq     .check_up

        ; Move down
        lda     SPRITE0_Y
        clc
        adc     #1
        cmp     #160            ; Edge?
        bcc     .update_y
        lda     #0              ; Wrap

.update_y:
        sta     SPRITE0_Y

.check_up:
        lda     BUTTONS
        and     #$08            ; Up button?
        beq     LOOP

        ; Move up
        lda     SPRITE0_Y
        sec
        sbc     #1
        bcs     .update_y2
        lda     #159            ; Wrap

.update_y2:
        sta     SPRITE0_Y

        jmp     LOOP

; Sprite data (8×8 tile, 2 bits per pixel for 4 shades)
SPRITE_DATA:
        .byte   $00,$00,$18,$3C,$3C,$7E,$7E,$FF
        .byte   $FF,$7E,$7E,$3C,$3C,$18,$00,$00
        ; ... (64 bytes total)

; Audio (simple beeper)
AUDIO_CTRL      = $2040
AUDIO_FREQ      = $2041
```

**Key teaching moment:** Watara Supervision uses 6502-derived CPU (65SC02-like)! 160×160 square LCD (unique!). 4 shades of grayscale. Budget Game Boy competitor ($50-70 vs $90!). 20+ hour battery life (4× AA). Taiwan manufacturer (Watara). Sold as Supervision/QuickShot Supervision/Hartung Supervision (rebrands). Link cable for multiplayer. TV adapter available. ~65 games. Limited success vs Game Boy. Discontinued mid-1990s. 6502 knowledge transfers!

**Tier progression:**
1. 65SC02-like basics (6502-derived, A/X/Y registers)
2. 160×160 LCD (square screen, unique!)
3. 4-shade grayscale (white, light gray, dark gray, black)
4. VRAM manipulation (4KB video memory)
5. Sprite system (hardware sprites, 8×8 tiles)
6. D-pad input (4 directions)
7. Button input (A, B, Select, Start)
8. DMA transfers (hardware data copy)
9. Battery optimization (20+ hours critical!)
10. Audio (simple beeper)
11. Link cable (multiplayer protocols)
12. TV adapter (optional output)
13. Collision detection (software)
14. Animation (sprite cycling)
15. Score display (LCD space management)
16. Complete Supervision mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 6502 techniques, 4-shade graphics mastery, portable optimization, link cable multiplayer

#### New Patterns:
- **6502 optimization** - Efficient 6502-family code
- **4-shade art** - Creative grayscale graphics
- **160×160 mastery** - Effective square screen usage
- **Hardware sprites** - Multiple sprite coordination
- **DMA efficiency** - Fast data transfers
- **Battery profiling** - 30+ hour optimization
- **Link cable protocols** - 2-player multiplayer
- **TV adapter support** - Optional TV output
- **8KB RAM efficiency** - Game state management
- **ROM banking** - Larger games (128KB-1MB)
- **Audio patterns** - Simple beeper melodies
- **D-pad precision** - Responsive controls

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - TV adapter and link cable advanced usage
**Focus:** TV adapter optimization, multiplayer mastery

#### Phase 3 Enhancement: TV Adapter + Link Cable
- **TV adapter** - Optional accessory for TV output
- **Same resolution** - 160×160 on TV (scaled)
- **Link cable** - 2-player multiplayer support
- **Compatible rebrands** - QuickShot, Hartung variants (same hardware)

**Tier 40 Example - Link Cable Multiplayer:**
```asm
; Link cable communication for 2-player game

LINK_DATA       = $2050         ; Link cable data register
LINK_STATUS     = $2051         ; Link cable status

SendByte:
        ; Send byte in A via link cable
        sta     LINK_DATA       ; Write data
.wait:  lda     LINK_STATUS
        and     #$01            ; Check if sent
        beq     .wait
        rts

ReceiveByte:
        ; Receive byte via link cable
        ; Returns in A
.wait:  lda     LINK_STATUS
        and     #$02            ; Check if received
        beq     .wait
        lda     LINK_DATA       ; Read data
        rts

; Example: Send player position
SendPosition:
        lda     PLAYER_X
        jsr     SendByte
        lda     PLAYER_Y
        jsr     SendByte
        rts

; Example: Receive opponent position
ReceivePosition:
        jsr     ReceiveByte
        sta     OPPONENT_X
        jsr     ReceiveByte
        sta     OPPONENT_Y
        rts
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional 6502 programming, portable game design mastery, multiplayer sophistication

#### Advanced Techniques:
- **6502 mastery** - Cycle-perfect code
- **4-shade mastery** - Dithering, effective art
- **Square screen design** - 160×160 optimization
- **Sprite coordination** - Many sprites via flickering
- **DMA mastery** - Efficient transfers
- **Battery excellence** - 40+ hour optimization
- **Link cable sophistication** - Complex multiplayer
- **TV adapter optimization** - Best TV display
- **8KB RAM utilization** - Maximum game complexity
- **ROM optimization** - Efficient cartridge usage
- **Audio depth** - Beeper music/effects

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games that work well on portable square screen

#### Genre Specializations:
- **Puzzle games** - Perfect for square screen! (Tetris, match-3)
- **Action games** - Platformers, shooters
- **Sports games** - Simple sports (Tennis, Soccer)
- **Board games** - Chess, checkers (square board!)
- **Card games** - Solitaire, poker
- **RPGs** - Simple turn-based RPGs
- **Arcade ports** - Space Invaders, Pac-Man
- **Link cable multiplayer** - 2-player competitive games

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum portable performance, battery efficiency

#### Limit-Pushing Techniques:
- **6502 optimization** - Maximum CPU usage
- **4-shade showcase** - Beautiful grayscale art
- **160×160 maximum** - Best square screen graphics
- **Sprite flickering** - Many objects on-screen
- **DMA showcase** - Fast graphics updates
- **50+ hour battery** - Extreme optimization!
- **Link cable mastery** - Complex multiplayer protocols
- **TV adapter excellence** - Best TV display quality
- **RAM utilization** - 8KB maximum usage
- **ROM showcase** - Large games (1MB cartridges)

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Best possible Supervision games

#### Commercial Techniques:
- **Commercial quality** - Matching best original games
- **Grayscale polish** - Beautiful 4-shade graphics
- **Square screen mastery** - Perfect 160×160 usage
- **Portable excellence** - Ideal handheld experience
- **Battery perfection** - Long play sessions
- **Link cable polish** - Engaging multiplayer
- **TV adapter support** - Optional TV quality
- **Extreme optimization** - Every byte/cycle optimized

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - Supervision emulation support
- **Modern 6502 toolchains** - cc65, ca65, modern assemblers
- **Flash cartridges** - Homebrew development
- **Community techniques** - Supervision preservation scene
- **6502 knowledge** - Transfers to Apple II, C64, NES!
- **Modern tools** - Emulator debugging features
- **Historical research** - Budget handheld market study

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 optimization techniques
3. **Multiplayer Patterns (Phase 3)** - 50 link cable techniques
4. **Mastery Patterns (Phase 4-5)** - 100 6502 + portable
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-8: Watara Supervision (1992)**
- 65SC02-like CPU @ 4MHz (6502-derived!)
- 8KB RAM
- 4KB VRAM
- 160×160 LCD (square screen!)
- 4 shades grayscale (white, light gray, dark gray, black)
- Hardware sprites (8×8 tiles)
- DMA transfer support
- D-pad + 4 buttons (A, B, Select, Start)
- 4× AA batteries (20-40 hours!)
- Link cable (2-player multiplayer)
- TV adapter (optional, scales 160×160)
- Cartridge slot (128KB-1MB ROM typical)
- Budget price ($50-70)

**Rebranded Variants (identical hardware):**
- Watara Supervision (original)
- QuickShot Supervision (Europe)
- Hartung Supervision (Germany)

**Phase 3+: Optional Accessories**
- TV adapter (TV output)
- Link cable (multiplayer)

**Phase 7-8: Modern Homebrew**
- Flash cartridges (homebrew development)
- Modern development tools (MAME, cc65, ca65)
- Homebrew community (small)

## Spiral Learning Example: Puzzle Game (Perfect for Square Screen!)

**Phase 1 (Tier 5):** Simple block-falling puzzle, 160×160 grid. (~100 lines)

**Phase 2 (Tier 21):** Advanced puzzle mechanics, scoring, 4-shade graphics. (~250 lines)

**Phase 3 (Tier 37):** 2-player link cable mode, TV adapter support. (~350 lines)

**Phase 4 (Tier 45):** Complex puzzle rules, multiple modes. (~450 lines)

**Phase 5 (Tier 49):** Complete puzzle game, many levels. (~550 lines)

**Phase 6 (Tier 53):** Maximum complexity, beautiful 4-shade art. (~650 lines)

**Phase 7 (Tier 57):** Polished game, commercial quality. (~750 lines)

**Phase 8 (Tier 59):** Modern homebrew, flash cart support. (~750 lines + tooling)

## Key Differences from Other Platforms

1. **160×160 Square LCD** - Unique resolution!
2. **6502-Derived CPU** - Knowledge transfers to many platforms!
3. **Budget GB Competitor** - $50-70 vs $90 Game Boy
4. **4 Shades Grayscale** - Simple but effective
5. **20-40 Hour Battery** - Excellent life (4× AA)
6. **Link Cable** - 2-player multiplayer
7. **TV Adapter** - Optional TV output
8. **Taiwan Manufacturer** - Watara
9. **Multiple Rebrands** - Supervision/QuickShot/Hartung
10. **~65 Games** - Small library, limited success

## Success Criteria

**By Phase 4, learners can:**
- Write 6502 assembly fluently (transfers to C64, NES, Apple II!)
- Design for 160×160 square screen
- Create effective 4-shade grayscale graphics
- Optimize for battery life (20-40 hours)
- Program hardware sprites and DMA
- Implement link cable multiplayer
- Support TV adapter output
- Manage 8KB RAM efficiently

**By Phase 8, learners can:**
- Develop commercial-quality Supervision games
- Master 6502 architecture (transfers to many platforms!)
- Work with modern homebrew tools (MAME, cc65)
- Create compelling portable games
- Contribute to Supervision preservation
- Release homebrew cartridges

## Resources Required

**Phase 1-2:**
- MAME emulator (Supervision support)
- cc65 or ca65 (6502 assembler/compiler)
- Text editor
- Watara Supervision reference documentation
- 6502 programming guides

**Phase 7-8:**
- Flash cartridge (homebrew development)
- Watara Supervision hardware (optional)
- Modern development tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** 6502 mastery (transfers to C64, NES, Apple II, Atari 8-bit!), square screen design (unique!), budget portable development, 4-shade grayscale art, battery optimization, link cable multiplayer, understanding budget handheld market, portable game design, 6502 knowledge highly transferable!
