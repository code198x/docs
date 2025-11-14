# Casio PV-1000 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Casio PV-1000 (1983) → Casio's only game console
**Approach:** Game-first, pattern library, Z80 mastery, early cartridge era study
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Casio home console (1983, Japan-only), Z80 @ 3.579MHz, 256×192 resolution (high for 1983!), 8 colors on-screen (from 27-color palette), 4KB RAM, 3-channel PSG audio, 2 joystick controllers (8-way + 2 buttons each), cartridge-based, competed with Famicom/SG-1000 (released same year!), only 13 games total (smallest library!), massive commercial failure (discontinued within 1 year!), ~$80 launch price, Casio's only console attempt, interesting historical study of market failure, MAME emulation available

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Casio PV-1000 shipped without BASIC. Curriculum begins directly with assembly, focused on Z80 architecture and understanding why this console failed so spectacularly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** Z80 fundamentals, 256×192 graphics, 8-color limitations, 3-channel PSG, understanding market failure
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **Z80 patterns** - Zilog Z80 @ 3.579MHz (standard 8-bit CPU)
- **256×192 resolution** - High resolution for 1983!
- **8 colors on-screen** - From 27-color palette
- **4KB RAM** - Limited memory
- **Character-based graphics** - 32×24 character grid
- **3-channel PSG** - Simple audio (similar to SN76489)
- **8-way joysticks** - 2 controllers, 8-way + 2 buttons each
- **Cartridge ROM** - 8-32KB typical
- **Sprites** - Limited sprite support
- **Scrolling** - Hardware scrolling support

#### Example Tier 1 Lesson: "Your First PV-1000 Game"
```asm
; Casio PV-1000 Assembly - Lesson 001
; Display character on 256×192 screen
; Z80 @ 3.579 MHz

; Z80 architecture (standard):
; - 8-bit accumulator (A)
; - Register pairs BC, DE, HL
; - Alternate register set (AF', BC', DE', HL')
; - Index registers IX, IY
; - Stack pointer SP
; - Flags: SZPNC (Sign, Zero, Parity, N, Carry)

        .org    $0000

; Casio PV-1000 memory map
ROM_BASE        = $0000         ; ROM at $0000-$7FFF (32KB)
RAM_BASE        = $B800         ; 4KB RAM at $B800-$C7FF
VRAM_BASE       = $B000         ; VRAM at $B000-$B7FF (2KB)
PALETTE         = $C800         ; Palette RAM
VIDEO_CTRL      = $F0           ; Video control port
SPRITE_CTRL     = $F1           ; Sprite control
SCROLL_X        = $F2           ; Horizontal scroll
SCROLL_Y        = $F3           ; Vertical scroll
SOUND_CH1       = $F8           ; Sound channel 1
SOUND_CH2       = $F9           ; Sound channel 2
SOUND_CH3       = $FA           ; Sound channel 3
JOY1            = $FC           ; Joystick 1 port
JOY2            = $FD           ; Joystick 2 port

START:  ; Initialize
        di                      ; Disable interrupts
        ld      sp,$C7FF        ; Set stack pointer (top of RAM)

        ; Initialize video
        ld      a,$01
        out     (VIDEO_CTRL),a  ; Enable video

        ; Clear VRAM (2KB, character-based 32×24)
        ld      hl,VRAM_BASE
        ld      bc,$0800        ; 2KB
        xor     a
.clear: ld      (hl),a
        inc     hl
        dec     bc
        ld      a,b
        or      c
        jr      nz,.clear

        ; Set up 8-color palette (from 27-color palette)
        ; Casio PV-1000 has 27 colors: 3 levels each of RGB
        ; We select 8 for our game
        ld      hl,PALETTE
        ld      a,$00           ; Black
        ld      (hl+),a
        ld      a,$09           ; Red (high intensity)
        ld      (hl+),a
        ld      a,$06           ; Green (high intensity)
        ld      (hl+),a
        ld      a,$03           ; Blue (high intensity)
        ld      (hl+),a
        ld      a,$0F           ; Yellow
        ld      (hl+),a
        ld      a,$0C           ; Cyan
        ld      (hl+),a
        ld      a,$0A           ; Magenta
        ld      (hl+),a
        ld      a,$12           ; White
        ld      (hl),a

        ; Load character data to VRAM
        ld      hl,CHAR_DATA
        ld      de,VRAM_BASE
        ld      bc,64           ; 8×8 character
        ldir

        ; Display title text
        ld      hl,TITLE_TEXT
        ld      de,VRAM_BASE+64 ; Second row
        ld      bc,16
        ldir

        ; Initialize player position
        ld      a,128           ; X = 128 (center)
        ld      (PLAYER_X),a
        ld      a,96            ; Y = 96 (center)
        ld      (PLAYER_Y),a

MAIN_LOOP:
        ; Wait for VBlank (simple delay)
        ld      b,$FF
.delay1:
        ld      c,$FF
.delay2:
        dec     c
        jr      nz,.delay2
        djnz    .delay1

        ; Read joystick 1
        in      a,(JOY1)
        ld      b,a             ; Save input

        ; Check right
        bit     0,b
        jr      z,.check_left
        ld      a,(PLAYER_X)
        inc     a
        cp      256
        jr      c,.update_x
        xor     a
.update_x:
        ld      (PLAYER_X),a

.check_left:
        bit     1,b
        jr      z,.check_down
        ld      a,(PLAYER_X)
        dec     a
        jr      nc,.update_x2
        ld      a,255
.update_x2:
        ld      (PLAYER_X),a

.check_down:
        bit     2,b
        jr      z,.check_up
        ld      a,(PLAYER_Y)
        inc     a
        cp      192
        jr      c,.update_y
        xor     a
.update_y:
        ld      (PLAYER_Y),a

.check_up:
        bit     3,b
        jr      z,.check_button

        ld      a,(PLAYER_Y)
        dec     a
        jr      nc,.update_y2
        ld      a,191
.update_y2:
        ld      (PLAYER_Y),a

.check_button:
        ; Check button 1
        bit     4,b
        jr      z,.no_sound

        ; Play beep on channel 1
        ld      a,$80           ; Frequency
        out     (SOUND_CH1),a

.no_sound:
        ; Update sprite position
        ld      a,(PLAYER_X)
        out     (SPRITE_CTRL),a ; Sprite X
        ld      a,(PLAYER_Y)
        out     (SPRITE_CTRL+1),a ; Sprite Y

        jp      MAIN_LOOP

; Data
PLAYER_X:       db      128
PLAYER_Y:       db      96
TITLE_TEXT:     db      "PV-1000 GAME!",0
CHAR_DATA:
        ; 8×8 character data
        db      $3C,$42,$81,$81,$81,$81,$42,$3C
        ; ... (more character data)
```

**Key teaching moment:** Casio PV-1000 is Japan's BIGGEST console failure! Only 13 games total (smallest library!). Discontinued within 1 YEAR of release! Z80 @ 3.579MHz (standard CPU). 256×192 resolution (actually high for 1983!). 8 colors from 27-color palette. Competed with Famicom/SG-1000 (same year, 1983!) but lost BADLY. Casio's ONLY console attempt. $80 launch price. Interesting study of market failure despite decent hardware. MAME emulation available.

**Tier progression:**
1. Z80 basics (A, BC, DE, HL registers)
2. 256×192 graphics (high resolution for 1983!)
3. Character-based display (32×24 grid)
4. 8-color palette (from 27 colors)
5. VRAM manipulation (2KB character memory)
6. Joystick input (8-way + 2 buttons)
7. 3-channel PSG audio
8. Hardware scrolling (X/Y registers)
9. Limited sprites (hardware sprite support)
10. 4KB RAM management
11. Collision detection (software)
12. Animation (character cycling)
13. Two-player patterns (2 joysticks)
14. Game state machines
15. Simple games (early cartridge era)
16. Complete PV-1000 mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced Z80 techniques, 8-color art mastery, 3-channel audio, understanding why console failed

#### New Patterns:
- **Z80 optimization** - Efficient assembly code
- **256×192 mastery** - High-resolution graphics
- **8-color art** - Effective use of limited palette
- **Character graphics** - Creative 8×8 designs
- **3-channel PSG mastery** - Music and effects
- **Hardware scrolling** - Smooth scrolling techniques
- **Sprite usage** - Limited sprite coordination
- **4KB RAM efficiency** - Game state management
- **ROM optimization** - 8-32KB cartridge usage
- **Two-player patterns** - Dual joystick games
- **Market failure analysis** - Understanding why it failed

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - No enhancements (console discontinued!)
**Focus:** Maximizing original hardware, understanding failure

#### Phase 3 Enhancement: N/A
- **No hardware enhancements** - Discontinued within 1 year!
- **13 games total** - Smallest console library ever!
- **Market failure** - Dominated by Famicom
- **One and done** - Casio never made another console

**Note:** PV-1000 had no enhancements because it failed so quickly. Phase 3 focuses on understanding the market dynamics and technical limitations that led to failure.

**Tier 40 Example - Understanding Market Failure:**
```asm
; PV-1000 vs Famicom comparison
; This is a code example showing PV-1000's limitations

; PV-1000 limitations that hurt adoption:
; 1. Only 8 colors on-screen (Famicom: 25/52)
; 2. 4KB RAM (Famicom: 2KB, but better graphics)
; 3. Limited sprites (Famicom: 64 sprites, 8 per line)
; 4. Character-based graphics (Famicom: flexible tiles)
; 5. Poor game library (only 13 games!)
; 6. Higher price ($80 vs Famicom $75)
; 7. Casio had no game development experience
; 8. Released SAME YEAR as Famicom (bad timing!)

; Despite 256×192 resolution advantage,
; PV-1000 couldn't compete with Nintendo's ecosystem
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional Z80 programming, maximizing limited hardware, historical analysis

#### Advanced Techniques:
- **Z80 mastery** - Cycle-perfect code
- **256×192 optimization** - Maximum resolution usage
- **8-color showcase** - Best possible palette art
- **Character graphics mastery** - Creative 8×8 designs
- **3-channel composition** - Complex PSG music
- **Scrolling mastery** - Smooth hardware scrolling
- **Sprite efficiency** - Maximizing limited sprites
- **4KB RAM utilization** - Complex games in tiny memory
- **ROM efficiency** - Complete games in 8-32KB
- **Historical understanding** - Why console failed

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games that work within PV-1000's severe limitations

#### Genre Specializations:
- **Puzzle games** - Character-based puzzles
- **Simple shooters** - Space Invaders-style
- **Maze games** - Pac-Man clones
- **Action games** - Simple platformers
- **Sports games** - Basic ball games
- **Board games** - Chess, checkers
- **Two-player competitive** - Head-to-head joystick games
- **Arcade ports** - Simple arcade conversions

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum complexity despite limitations

#### Limit-Pushing Techniques:
- **Z80 maximum** - Every cycle optimized
- **256×192 showcase** - Best possible graphics
- **8-color mastery** - Beautiful limited palette
- **Character art excellence** - Creative 8×8 art
- **3-channel audio depth** - Complex PSG compositions
- **Scrolling excellence** - Smooth multi-directional
- **Sprite coordination** - Maximizing limited sprites
- **4KB RAM showcase** - Complex games, tiny memory
- **ROM optimization** - Maximum game in 8-32KB

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Best possible PV-1000 games (what could have been!)

#### Commercial Techniques:
- **Commercial quality** - Professional game development
- **Graphics polish** - Beautiful 256×192 graphics
- **8-color excellence** - Effective palette usage
- **Character graphics mastery** - Polished 8×8 art
- **Audio polish** - Engaging 3-channel music
- **Two-player polish** - Engaging multiplayer
- **Historical what-if** - Games that could have saved it?
- **Professional standards** - 1983 commercial quality

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - PV-1000 emulation support
- **Modern Z80 toolchains** - z88dk, modern assemblers
- **Flash cartridges** - Homebrew development (very rare!)
- **Community techniques** - PV-1000 preservation (tiny scene)
- **Z80 knowledge** - Transfers to MSX, ZX Spectrum, etc!
- **Historical research** - Understanding market failure
- **Modern tools** - Emulator debugging

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 optimization techniques
3. **Failure Analysis Patterns (Phase 3)** - 50 market understanding
4. **Mastery Patterns (Phase 4-5)** - 100 Z80 + graphics
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-8: Casio PV-1000 (1983, Japan-only)**
- Z80 @ 3.579MHz (standard 8-bit CPU)
- 4KB RAM
- 2KB VRAM
- 256×192 resolution (high for 1983!)
- 8 colors on-screen (from 27-color palette)
- Character-based display (32×24 grid)
- Limited sprite support
- Hardware scrolling (X/Y)
- 3-channel PSG audio (SN76489-like)
- 2 joystick controllers (8-way + 2 buttons each)
- Cartridge slot (8-32KB typical ROM)
- RF modulator (TV output)
- $80 launch price
- Only 13 games total!
- Discontinued within 1 year!

**Phase 7-8: Modern Homebrew**
- Flash cartridges (very rare, homebrew)
- Modern development tools (MAME, z88dk)
- Homebrew community (almost non-existent)

## Spiral Learning Example: Simple Action Game

**Phase 1 (Tier 10):** Player character, enemy, movement, 256×192 display. (~100 lines)

**Phase 2 (Tier 26):** Multiple enemies, scoring, 3-channel audio. (~250 lines)

**Phase 3 (Tier 34):** Analysis of why PV-1000 failed vs Famicom. (~300 lines + analysis)

**Phase 4 (Tier 42):** Complex action game, multiple levels. (~400 lines)

**Phase 5 (Tier 49):** Complete action game, polish. (~500 lines)

**Phase 6 (Tier 53):** Maximum complexity, beautiful 8-color art. (~600 lines)

**Phase 7 (Tier 57):** Commercial quality - what could have been! (~700 lines)

**Phase 8 (Tier 59):** Modern homebrew, historical significance. (~700 lines + tooling)

## Key Differences from Other Platforms

1. **Smallest Game Library** - Only 13 games! (failure!)
2. **Discontinued Within 1 Year** - Massive commercial failure
3. **Casio's Only Console** - Never tried again
4. **Released Same Year as Famicom** - Bad timing (1983)
5. **256×192 Resolution** - Actually high for 1983!
6. **8 Colors from 27** - Limited palette
7. **Z80 @ 3.579MHz** - Standard CPU
8. **$80 Launch Price** - More expensive than Famicom!
9. **Japan-Only** - Never exported
10. **Market Failure Study** - Understanding why it failed

## Success Criteria

**By Phase 4, learners can:**
- Write Z80 assembly fluently (transfers to MSX, ZX, etc!)
- Design for 256×192 high resolution
- Create effective 8-color graphics
- Program character-based display (32×24)
- Use 3-channel PSG audio
- Implement hardware scrolling
- Manage 4KB RAM efficiently
- Understand market failure dynamics

**By Phase 8, learners can:**
- Develop commercial-quality PV-1000 games
- Master Z80 architecture (transfers to many platforms!)
- Work with modern homebrew tools (MAME)
- Understand console market dynamics (failure analysis)
- Contribute to PV-1000 preservation
- Release homebrew cartridges (very rare!)
- Apply lessons from market failure to modern development

## Resources Required

**Phase 1-2:**
- MAME emulator (PV-1000 support)
- z88dk or Z80 assembler
- Text editor
- Casio PV-1000 reference documentation
- Z80 programming guides

**Phase 7-8:**
- Flash cartridge (very rare, homebrew)
- Casio PV-1000 hardware (optional, very rare collector's item!)
- Modern development tools
- Market failure analysis resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** Z80 mastery (transfers to MSX, ZX Spectrum, Sega Master System!), 256×192 high-resolution graphics programming, understanding console market failure (13 games, 1 year lifespan!), Casio's console history, early cartridge era study, market dynamics analysis, historical preservation of failed platform, learning from commercial failure!
