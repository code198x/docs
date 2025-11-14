# Pokémon Mini Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Pokémon Mini (2001-2002) → Smallest cartridge console ever!
**Approach:** Game-first, pattern library, extreme constraint mastery, ultra-portable design
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Nintendo's smallest cartridge console (2001), 96×64 monochrome LCD (0.9" diagonal!), 4-shade grayscale, S1C88 CPU (8-bit Epson), ultra-portable (fits in pocket!), infrared communication, built-in shock sensor + rumble, 10 official games, cult following, active homebrew scene, ~1 million units sold, discontinued 2002

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Pokémon Mini shipped without BASIC. Curriculum begins directly with assembly, focused on extreme constraints and ultra-portable design.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** S1C88 fundamentals, 96×64 LCD, extreme constraints (4KB RAM!), shock sensor, infrared, ultra-portable optimization
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **S1C88 patterns** - Epson S1C88 @ 4MHz (8-bit, unique architecture)
- **96×64 LCD** - Tiny monochrome display (4 shades, 0.9" diagonal)
- **Extreme constraints** - 4KB RAM total (smallest in modern era!)
- **Shock sensor** - Built-in accelerometer (innovative for 2001!)
- **Rumble motor** - Haptic feedback
- **Infrared communication** - Wireless data transfer between units
- **Ultra-portable** - Battery life critical (AAA battery, 40+ hours)
- **Cartridge ROM** - 64KB-512KB typical
- **Monochrome graphics** - Creative 4-shade usage
- **Sound** - Simple beeper (1-bit audio)

#### Example Tier 1 Lesson: "Your First Mini Sprite"
```asm
; Pokémon Mini Assembly - Lesson 001
; Display sprite on 96×64 LCD
; S1C88 @ 4 MHz

        .equ    LCD_CTRL, 0x2000
        .equ    LCD_DATA, 0x2100
        .equ    VRAM_BASE, 0x1000

        .org    0x2100          ; Cartridge entry point

START:  ; Initialize hardware
        ld      sp, 0x2000      ; Set stack

        ; Initialize LCD
        ld      a, 0x01         ; LCD on
        st      a, [LCD_CTRL]

        ; Clear VRAM (96×64 = 768 bytes)
        ld      ix, VRAM_BASE
        ld      bc, 768
        ld      a, 0
.CLEAR: st      a, [ix]
        inc     ix
        dec     bc
        jr      nz, .CLEAR

        ; Draw 8×8 sprite at center
        ld      ix, SPRITE_DATA
        ld      iy, VRAM_BASE + (32*12) + 44  ; Center position
        ld      b, 8            ; 8 rows
.DRAW:  ld      a, [ix]
        st      a, [iy]
        inc     ix
        add     iy, 96/8        ; Next row (96 pixels / 8 bits)
        dec     b
        jr      nz, .DRAW

LOOP:   ; Main loop
        ; Wait for VBlank
        call    WaitVBL

        ; Check buttons
        ld      a, [0x2052]     ; Read buttons
        bit     0, a            ; A button?
        jr      z, .NO_A
        ; Move sprite right
        ; ... (implementation)
.NO_A:

        jr      LOOP

WaitVBL:
        ; Wait for vertical blank
        ld      a, [0x2050]     ; Status register
        bit     7, a            ; VBL flag?
        jr      z, WaitVBL
        ret

SPRITE_DATA:
        ; 8×8 sprite (1 bit per pixel, 4 shades via dithering)
        .db     0x3C, 0x7E, 0xFF, 0xFF, 0xFF, 0xFF, 0x7E, 0x3C
```

**Key teaching moment:** Pokémon Mini is SMALLEST cartridge console ever! 96×64 monochrome LCD (0.9"!). 4KB RAM (extreme constraint!). S1C88 CPU (Epson, unusual). Shock sensor + rumble (innovative!). Infrared communication. 40+ hour battery life. Ultra-portable design (fits in pocket). Active homebrew scene despite 10 official games only.

**Tier progression:**
1. LCD basics (96×64, 4 shades)
2. Sprite rendering (software sprites, no hardware)
3. Extreme RAM conservation (4KB total!)
4. Button input (A, B, C, directional)
5. Sound basics (1-bit beeper)
6. Shock sensor (accelerometer, game control)
7. Rumble motor (haptic feedback)
8. Infrared communication (unit-to-unit)
9. Battery optimization (40+ hours target)
10. 4-shade graphics (dithering techniques)
11. Animation (sprite cycling)
12. Collision detection (software-based)
13. Score display (tiny font rendering)
14. Game state machines
15. Polish patterns (efficient graphics)
16. Complete Pokémon Mini mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 4-shade graphics, shock sensor mastery, infrared networking, extreme optimization

#### New Patterns:
- **4-shade mastery** - Dithering, gradients, pseudo-grayscale
- **Shock sensor gameplay** - Accelerometer-based mechanics
- **Rumble patterns** - Haptic feedback timing
- **Infrared protocols** - Unit-to-unit communication
- **Tiny screen design** - Readable graphics on 0.9" display
- **4KB RAM mastery** - Extreme efficiency
- **Battery profiling** - 50+ hour optimization
- **Cartridge ROM optimization** - Fitting games in 64-512KB
- **Compression** - Critical for ROM space
- **Mini game design** - Quick-play portable games

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Advanced accessories and techniques
**Focus:** Infrared multiplayer, shock sensor advanced use, homebrew hardware

#### Phase 3 Enhancement: Advanced Features
- **Infrared multiplayer** - 2-player wireless games
- **Shock sensor precision** - Advanced gesture recognition
- **Custom cartridges** - Homebrew flash carts
- **Battery extension** - Ultra-long play sessions

**Tier 40 Example - Infrared Multiplayer:**
```asm
; Infrared communication for 2-player game

IRSend:
        ; Send byte via infrared
        ; a = byte to send
        ld      b, 8            ; 8 bits
.LOOP:  sla     a               ; Shift left
        jr      c, .SEND_1

.SEND_0:
        ; Send 0 bit
        ld      [IR_CTRL], 0
        call    IRDelay
        jr      .NEXT

.SEND_1:
        ; Send 1 bit
        ld      [IR_CTRL], 1
        call    IRDelay

.NEXT:  dec     b
        jr      nz, .LOOP
        ret

IRReceive:
        ; Receive byte via infrared
        ; Returns byte in a
        ld      b, 8
        ld      a, 0
.LOOP:  sla     a
        ld      c, [IR_STATUS]
        bit     0, c
        jr      z, .NEXT
        or      1
.NEXT:  call    IRDelay
        dec     b
        jr      nz, .LOOP
        ret

IR_CTRL:    .equ    0x2060
IR_STATUS:  .equ    0x2061
```

### Phase 4-8: Advanced Development (Tiers 41-60)

**Phase 4:** Professional ultra-portable game design, 4KB RAM mastery, shock sensor innovation
**Phase 5:** Genre specializations - puzzle games, mini-RPGs, action games (perfect for portable!)
**Phase 6:** Maximum efficiency, advanced shock control, infrared mastery
**Phase 7:** Commercial-quality mini games, professional polish
**Phase 8:** Modern homebrew, flash carts, emulation (PokeMini emulator, MAME)

## Key Differences from Other Platforms

1. **Smallest Cartridge Console** - 0.9" screen, pocket-sized!
2. **Extreme Constraint** - 4KB RAM (smallest modern console)
3. **96×64 Monochrome** - Tiny 4-shade display
4. **Shock Sensor** - Built-in accelerometer (2001!)
5. **Infrared Communication** - Wireless multiplayer
6. **Rumble Motor** - Haptic feedback
7. **40+ Hour Battery** - Single AAA battery
8. **S1C88 CPU** - Epson architecture (unusual)
9. **10 Official Games** - But active homebrew scene!
10. **Cult Following** - Strong homebrew community

## Success Criteria

**By Phase 4:** S1C88 assembly fluency, 4KB RAM mastery, shock sensor programming, infrared communication, ultra-portable design
**By Phase 8:** Commercial-quality mini games, extreme optimization, homebrew release capability

## Resources Required
- PokeMini emulator (excellent, accurate)
- MAME (Pokémon Mini support)
- Modern S1C88 toolchains
- Flash cartridges (homebrew development)
- Community resources (active homebrew scene)

---

**Total:** 4,096 lessons | **Unique:** Smallest console, extreme constraints, shock sensor, infrared, ultra-portable mastery
