# Game.com Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Tiger Electronics Game.com (1997-2000) → First touchscreen handheld!
**Approach:** Game-first, pattern library, SM8521 mastery, touchscreen programming
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Tiger Electronics handheld (1997), Sharp SM8521 @ 10MHz (Z80-like), 160×160 resistive touchscreen LCD (revolutionary for 1997!), 4 shades grayscale, stylus included, internet capable (14.4K modem cartridge!), 2-player link cable, built-in PDA features (calendar, calculator, phonebook), $69.99 launch (budget!), Game.com Pocket Pro (1999, backlight), ~20 games total, poor game quality but innovative features, commercial failure (~1M units), discontinued 2000, historically significant (first touchscreen gaming handheld!)

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Game.com shipped without BASIC. Curriculum begins directly with assembly, focused on the Sharp SM8521 architecture and touchscreen programming.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** SM8521 fundamentals, touchscreen input, 160×160 LCD, internet features, PDA integration
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **SM8521 patterns** - Sharp SM8521 @ 10MHz (Z80-like but unique!)
- **Touchscreen input** - Resistive touch, stylus (revolutionary 1997!)
- **160×160 LCD** - Square screen, 4 shades grayscale
- **Internet capable** - 14.4K modem cartridge (optional)
- **PDA features** - Calendar, calculator, phonebook (built-in!)
- **2MB RAM** - Large for 1997 handheld!
- **128KB VRAM** - Dedicated video memory
- **D-pad + buttons** - Traditional controls + touchscreen
- **Link cable** - 2-player multiplayer
- **Stylus input** - Pen-based interaction

#### Example Tier 1 Lesson: "Your First Touchscreen Game"
```asm
; Game.com Assembly - Lesson 001
; Touchscreen drawing program
; Sharp SM8521 @ 10 MHz

; Sharp SM8521 architecture:
; - Z80-like 8-bit CPU
; - Accumulator A
; - Register pairs BC, DE, HL
; - Index registers IX, IY
; - Stack pointer SP
; - Flags: SZPC (Sign, Zero, Parity, Carry)
; - Similar to Z80 but with unique instructions

        .org    $0000

; Game.com memory map
RAM_BASE        = $0000         ; 2MB RAM at $0000-$1FFFFF
VRAM_BASE       = $4000         ; 128KB VRAM
LCD_CTRL        = $2000         ; LCD control
TOUCH_X         = $2010         ; Touch X coordinate
TOUCH_Y         = $2011         ; Touch Y coordinate
TOUCH_STATUS    = $2012         ; Touch status (pressed/released)
BUTTONS         = $2020         ; D-pad + button input
MODEM_CTRL      = $3000         ; Modem control (if cartridge present)
MODEM_DATA      = $3001         ; Modem data
PDA_CALENDAR    = $5000         ; PDA calendar data
PDA_CALC        = $5100         ; PDA calculator
PDA_PHONE       = $5200         ; PDA phonebook

START:  ; Initialize
        di                      ; Disable interrupts
        ld      sp,$FFFE        ; Set stack pointer

        ; Initialize LCD
        ld      a,$01
        ld      (LCD_CTRL),a    ; Enable LCD

        ; Clear VRAM
        ld      hl,VRAM_BASE
        ld      bc,$20000       ; 128KB
        xor     a
.clear: ld      (hl),a
        inc     hl
        dec     bc
        ld      a,b
        or      c
        jr      nz,.clear

        ; Display title
        ld      hl,TITLE_TEXT
        ld      de,$4100        ; VRAM position
        call    DrawText

        ; Initialize drawing cursor
        ld      hl,80
        ld      (CURSOR_X),hl
        ld      (CURSOR_Y),hl

MAIN_LOOP:
        ; Read touchscreen
        ld      a,(TOUCH_STATUS)
        bit     0,a             ; Touch active?
        jr      z,NO_TOUCH

        ; Touch is active - get coordinates
        ld      a,(TOUCH_X)
        ld      (CURSOR_X),a
        ld      a,(TOUCH_Y)
        ld      (CURSOR_Y),a

        ; Draw pixel at touch position
        ld      a,(CURSOR_X)
        ld      h,a
        ld      a,(CURSOR_Y)
        ld      l,a
        call    DrawPixel

NO_TOUCH:
        ; Check D-pad for menu navigation
        ld      a,(BUTTONS)
        bit     4,a             ; Select button?
        jr      z,NO_SELECT

        ; Clear screen on Select
        call    ClearScreen

NO_SELECT:
        ; Check for internet modem (if cartridge present)
        ld      a,(MODEM_CTRL)
        bit     0,a             ; Modem present?
        jr      z,NO_MODEM

        ; Modem available - show indicator
        ld      hl,MODEM_TEXT
        ld      de,$4F00
        call    DrawText

NO_MODEM:
        jr      MAIN_LOOP

; Draw text to VRAM
; HL = text pointer, DE = VRAM destination
DrawText:
        ld      a,(hl)
        or      a               ; Check for null terminator
        ret     z
        ld      (de),a
        inc     hl
        inc     de
        jr      DrawText

; Draw pixel at position
; H = X, L = Y
DrawPixel:
        push    hl
        ; Calculate VRAM address: VRAM_BASE + (Y * 160) + X
        ld      a,l             ; Y
        ld      h,160
        call    Multiply        ; A = Y * 160 (in HL)
        ld      a,(CURSOR_X)
        add     a,l
        ld      l,a
        ld      bc,VRAM_BASE
        add     hl,bc           ; HL = VRAM address
        ld      a,$03           ; Dark gray
        ld      (hl),a
        pop     hl
        ret

; Multiply routine (simplified)
Multiply:
        ; A * H -> HL
        ld      l,0
        ld      h,0
        or      a
        ret     z
.loop:  add     hl,hl
        dec     a
        jr      nz,.loop
        ret

; Clear screen
ClearScreen:
        ld      hl,VRAM_BASE
        ld      bc,$20000
        xor     a
.loop:  ld      (hl),a
        inc     hl
        dec     bc
        ld      a,b
        or      c
        jr      nz,.loop
        ret

; Data
TITLE_TEXT:     db "TOUCH TO DRAW!",0
MODEM_TEXT:     db "MODEM OK",0
CURSOR_X:       db 0
CURSOR_Y:       db 0
```

**Key teaching moment:** Game.com has TOUCHSCREEN in 1997! First touchscreen gaming handheld (revolutionary!). Sharp SM8521 CPU (Z80-like). Resistive touch + stylus. Internet capable (14.4K modem cartridge!). Built-in PDA features (calendar, calculator, phonebook). $69.99 budget price. 2MB RAM (huge for handheld!). Link cable multiplayer. Poor game quality but innovative hardware. ~1M units sold. Commercial failure but historically significant. Pre-dates Nintendo DS touchscreen by 7 years!

**Tier progression:**
1. SM8521 basics (Z80-like, registers, instructions)
2. Touchscreen input (X/Y coordinates, stylus)
3. 160×160 LCD (square screen, 4 shades)
4. Stylus-based UI (touch-friendly interfaces)
5. D-pad + buttons (traditional controls)
6. PDA integration (calendar, calculator, phonebook)
7. Internet modem (14.4K, optional cartridge)
8. 2MB RAM management (large memory)
9. Drawing programs (stylus art)
10. Touch calibration (resistive touch accuracy)
11. Link cable (2-player multiplayer)
12. VRAM manipulation (128KB video)
13. Simple audio (piezo beeper)
14. Touch-based games (tap, drag, draw)
15. Hybrid controls (touch + D-pad)
16. Complete Game.com touchscreen apps

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced touchscreen techniques, internet applications, PDA integration, touch + D-pad hybrids

#### New Patterns:
- **Advanced touch** - Handwriting recognition (simple)
- **Touch gestures** - Tap, drag, draw patterns
- **Internet applications** - Modem-based online features (if cartridge)
- **PDA sophistication** - Deep integration with built-in apps
- **Hybrid controls** - Touch + D-pad combined
- **Touch calibration** - Resistive touch accuracy
- **Stylus precision** - Fine drawing/pointing
- **2MB RAM utilization** - Large game states
- **Link cable protocols** - 2-player multiplayer
- **VRAM efficiency** - 128KB video management
- **Touch-based UI** - Point-and-click interfaces
- **Text input** - On-screen keyboard (stylus)

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Game.com Pocket Pro (1999) improvements
**Focus:** Pocket Pro enhancements, backlight optimization

#### Phase 3 Enhancement: Game.com Pocket Pro (1999)
- **Pocket Pro** (1999) - Upgraded Game.com
- **Backlight** - Lit screen (original had no backlight!)
- **Same CPU/resolution** - SM8521, 160×160
- **Improved contrast** - Better LCD visibility
- **Backward compatible** - All original games work
- **Same features** - Touch, modem, PDA, link cable

**Tier 40 Example - Detect Pocket Pro:**
```asm
; Detect original Game.com vs Pocket Pro

DetectModel:
        ; Check hardware revision register
        ld      a,($2FFF)       ; Hardware ID
        and     $F0
        cp      $A0             ; Pocket Pro marker
        jr      z,is_pocket_pro

is_original:
        ; Original Game.com (1997)
        ld      a,0
        ld      (MODEL),a
        ret

is_pocket_pro:
        ; Pocket Pro (1999)
        ; Enable backlight optimization
        ld      a,1
        ld      (MODEL),a
        ld      a,$01
        ld      ($2FFE),a       ; Backlight control
        ret

MODEL:  db      0               ; 0=original, 1=Pocket Pro
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional touchscreen programming, internet application mastery, sophisticated PDA integration

#### Advanced Techniques:
- **SM8521 mastery** - Efficient Z80-like code
- **Touch precision** - Accurate resistive touch handling
- **Handwriting recognition** - Simple letter/number recognition
- **Internet protocols** - TCP/IP over 14.4K modem
- **PDA depth** - Full calendar/calculator/phonebook integration
- **Hybrid game design** - Touch + D-pad mastery
- **2MB RAM complexity** - Large-scale applications
- **VRAM optimization** - Fast graphics updates
- **Link cable sophistication** - Complex multiplayer
- **Text input mastery** - On-screen keyboards
- **Touch UI excellence** - Professional interfaces

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Touch-optimized genres, internet apps, PDA features

#### Genre Specializations:
- **Touch puzzle games** - Stylus-based puzzles
- **Drawing applications** - Paint programs
- **Internet browsers** - Simple web browsing (modem)
- **PDA applications** - Productivity software
- **Touch RPGs** - Menu-driven with touch
- **Strategy games** - Touch-based strategy
- **Card games** - Solitaire, poker (touch-friendly!)
- **Educational software** - Handwriting practice

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum touchscreen innovation, internet features

#### Limit-Pushing Techniques:
- **Touch mastery** - Precise resistive touch handling
- **Gesture recognition** - Complex touch patterns
- **Internet complexity** - Advanced modem features
- **PDA showcase** - Full-featured productivity
- **Hybrid excellence** - Perfect touch + D-pad
- **2MB utilization** - Maximum RAM usage
- **VRAM showcase** - Fast, smooth graphics
- **Handwriting recognition** - Accurate character recognition
- **Link cable mastery** - Complex 2-player protocols

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial touchscreen applications, internet services

#### Commercial Techniques:
- **Commercial quality** - Professional touch apps
- **Touch polish** - Responsive, accurate
- **Internet services** - Online content (modem)
- **PDA excellence** - Full productivity suite
- **Graphics polish** - Best 4-shade grayscale
- **Hybrid perfection** - Seamless control mixing
- **Backlight optimization** - Pocket Pro features
- **Professional UI** - Commercial interface quality

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - Game.com emulation support
- **Modern Z80 toolchains** - z88dk, modern assemblers
- **Flash cartridges** - Homebrew development (rare!)
- **Community techniques** - Game.com preservation scene
- **Touchscreen expertise** - Early touch programming study
- **Historical significance** - First touchscreen handheld!
- **Modern tools** - Emulator debugging

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Touch Patterns (Phase 2)** - 75 touchscreen techniques
3. **Pocket Pro Patterns (Phase 3)** - 50 backlight + improvements
4. **Advanced Patterns (Phase 4-5)** - 100 SM8521 + touch mastery
5. **Genre Patterns (Phase 5-6)** - 150 touch-optimized games
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Game.com (1997)**
- Sharp SM8521 @ 10MHz (Z80-like)
- 2MB RAM (huge for 1997!)
- 128KB VRAM
- 160×160 resistive touchscreen LCD (revolutionary!)
- 4 shades grayscale
- Stylus included
- D-pad + 4 buttons (A, B, C, D)
- Internet capable (14.4K modem cartridge, optional)
- Built-in PDA (calendar, calculator, phonebook)
- Link cable (2-player multiplayer)
- 4× AA batteries
- $69.99 launch price

**Phase 3+: Game.com Pocket Pro (1999)**
- Same SM8521 CPU
- Backlight (major improvement!)
- Better LCD contrast
- Backward compatible
- Same features (touch, modem, PDA, link)

**Phase 7-8: Modern Homebrew**
- Flash cartridges (rare, homebrew)
- Modern development tools (MAME, z88dk)
- Homebrew community (very small)

## Spiral Learning Example: Touch Puzzle Game (Perfect for Game.com!)

**Phase 1 (Tier 14):** Simple touch puzzle, tap blocks, stylus input. (~150 lines)

**Phase 2 (Tier 30):** Advanced puzzle, drag-and-drop, gestures. (~350 lines)

**Phase 3 (Tier 38):** Pocket Pro backlight optimization. (~400 lines)

**Phase 4 (Tier 46):** Complex puzzle mechanics, hybrid touch + D-pad. (~550 lines)

**Phase 5 (Tier 49):** Complete puzzle game, many levels, polish. (~700 lines)

**Phase 6 (Tier 53):** Gesture recognition, handwriting input. (~850 lines)

**Phase 7 (Tier 57):** Commercial quality touch puzzle game. (~1000 lines)

**Phase 8 (Tier 59):** Modern homebrew, flash cart support. (~1000 lines + tooling)

## Key Differences from Other Platforms

1. **First Touchscreen Handheld** - Revolutionary 1997!
2. **Resistive Touch + Stylus** - 7 years before Nintendo DS!
3. **Internet Capable** - 14.4K modem cartridge
4. **Built-in PDA** - Calendar, calculator, phonebook
5. **2MB RAM** - Huge for 1997 handheld!
6. **Sharp SM8521** - Z80-like CPU @ 10MHz
7. **$69.99 Budget Price** - Affordable
8. **Pocket Pro Backlight** - 1999 upgrade
9. **Poor Game Quality** - Innovation > execution
10. **Historical Significance** - First touch gaming handheld!

## Success Criteria

**By Phase 4, learners can:**
- Write SM8521 assembly fluently (Z80-like)
- Program resistive touchscreen input
- Design stylus-based interfaces
- Implement internet features (modem)
- Integrate PDA functionality
- Create hybrid touch + D-pad controls
- Manage 2MB RAM efficiently
- Optimize for 4-shade grayscale

**By Phase 8, learners can:**
- Develop commercial-quality Game.com applications
- Master SM8521/Z80-like architecture
- Work with modern homebrew tools (MAME)
- Create innovative touchscreen games
- Contribute to Game.com preservation
- Release homebrew cartridges
- Understand early touchscreen gaming history

## Resources Required

**Phase 1-2:**
- MAME emulator (Game.com support)
- z88dk or Z80 assembler
- Text editor
- Game.com reference documentation
- Sharp SM8521 programming guides

**Phase 7-8:**
- Flash cartridge (rare, homebrew)
- Game.com hardware (optional, collector's item!)
- Modern development tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** Touchscreen programming (first gaming handheld with touch!), SM8521/Z80-like mastery, resistive touch handling, stylus interface design, internet application development (modem), PDA integration, hybrid control schemes, understanding early touch gaming history (pre-dates DS by 7 years!), historical significance study
