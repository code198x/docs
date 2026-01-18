# Phase 1 Breakdown: NES Neon Nexus

**Game:** Neon Nexus (Game 1)
**Phase:** 1 of 8 (128-unit structure)
**Units:** 1-16
**Theme:** PPU Fundamentals + First Display

---

## Phase 1 Overview

The NES is challenging to start because:
- No direct pixel access — everything is tiles
- PPU (Picture Processing Unit) is separate from CPU
- Strict timing — can only write to PPU during vblank
- Header format and memory mapping must be correct

By the end of Phase 1, learners will:
- Have tiles and colours on screen under their control
- Understand the PPU's nametable and palette system
- Know how to structure an NES ROM
- Be able to diagnose "black screen" problems

**Phase 1 Output:** A colourful title screen built from custom tiles, with palette cycling animation.

---

## Unit Progression

### Unit 1: Your First Tile
**Time:** 45 minutes
**Builds on:** Nothing — this is the start

**What happens:**
- Type complete working program (with header, vectors, CHR data)
- Assemble and run in FCEUX
- See a single white tile in the top-left corner

**Key code (complete, runnable):**
```asm
.segment "HEADER"
    .byte "NES", $1a    ; iNES header
    .byte $01           ; 1x 16KB PRG bank
    .byte $01           ; 1x 8KB CHR bank
    .byte $00, $00      ; Mapper 0, horizontal mirroring
    .byte $00, $00, $00, $00, $00, $00, $00, $00

.segment "CODE"

reset:
    sei                 ; Disable interrupts
    cld                 ; Clear decimal mode
    ldx #$ff
    txs                 ; Set up stack

    ; Wait for PPU to stabilise (two vblanks)
    bit $2002
:   bit $2002
    bpl :-
:   bit $2002
    bpl :-

    ; Set palette: black background, white foreground
    lda #$3f
    sta $2006           ; PPU address high
    lda #$00
    sta $2006           ; PPU address low ($3f00 = palette)
    lda #$0f            ; Black
    sta $2007
    lda #$30            ; White
    sta $2007

    ; Write tile #1 to top-left of nametable
    lda #$20
    sta $2006           ; PPU address high
    lda #$00
    sta $2006           ; PPU address low ($2000 = nametable)
    lda #$01            ; Tile index 1
    sta $2007

    ; Enable rendering
    lda #%00001000      ; Background uses left pattern table
    sta $2000
    lda #%00011110      ; Show background and sprites
    sta $2001

forever:
    jmp forever

nmi:
irq:
    rti

.segment "VECTORS"
    .word nmi, reset, irq

.segment "CHARS"
    ; Tile 0: completely empty
    .byte $00,$00,$00,$00,$00,$00,$00,$00
    .byte $00,$00,$00,$00,$00,$00,$00,$00

    ; Tile 1: solid block
    .byte $ff,$ff,$ff,$ff,$ff,$ff,$ff,$ff
    .byte $00,$00,$00,$00,$00,$00,$00,$00
```

**What learner sees:** One white square in the corner. Everything else black.

**Concepts introduced (not explained):**
- NES ROMs have a header
- There's something called PPU at addresses $2000-$2007
- Tiles are 8×8 patterns defined in CHR data
- The number you write ($01) picks which tile appears

**Output:** Single white tile on screen.

**Experiment:** Change tile 1's pattern bytes. See different shapes appear.

---

### Unit 2: The iNES Header
**Time:** 60 minutes
**Builds on:** Unit 1's working ROM

**What happens:**
- Explain what the header bytes mean
- Why "NES" + $1a magic number
- PRG banks (code) vs CHR banks (graphics)
- What mapper 0 means

**Header dissected:**
```asm
.segment "HEADER"
    .byte "NES", $1a    ; Magic number - identifies this as NES ROM
    .byte $01           ; 1 PRG bank = 16KB of code
    .byte $01           ; 1 CHR bank = 8KB of graphics
    .byte $00           ; Flags 6: Mapper low nibble, mirroring
    .byte $00           ; Flags 7: Mapper high nibble
    ; Bytes 8-15: Usually zero for basic ROMs
```

**Concepts explained:**
- ROM structure (header + PRG + CHR)
- Banks and sizes
- Why the emulator needs this information

**Output:** Same as Unit 1 (understanding, not new features).

**Experiment:** Change PRG/CHR counts — watch the emulator complain or show garbage.

---

### Unit 3: The PPU Address Bus
**Time:** 60 minutes
**Builds on:** Unit 2's ROM structure

**What happens:**
- PPU has its own memory, separate from CPU
- CPU talks to PPU through registers at $2000-$2007
- $2006 sets the address (written twice: high, then low)
- $2007 reads/writes data at that address

**The PPU communication pattern:**
```asm
    ; To write to PPU address $3f00:
    lda #$3f
    sta $2006       ; High byte of address
    lda #$00
    sta $2006       ; Low byte of address
    lda #$0f        ; Data to write
    sta $2007       ; Write it

    ; Address auto-increments after each $2007 write
```

**Concepts explained:**
- PPU has separate address space
- $2006 = address register (write twice)
- $2007 = data register
- Why we can't just STA to screen memory like C64

**Output:** Same display, but learner understands the mechanism.

**Experiment:** Write multiple values to $2007 — watch them appear sequentially.

---

### Unit 4: Palettes
**Time:** 60 minutes
**Builds on:** Unit 3's PPU addressing

**What happens:**
- NES has a fixed palette of 64 colours
- You choose 4 colours for background, 4 for sprites (simplified)
- Palette lives at PPU address $3f00-$3f1f

**NES colour palette (subset):**
```
$0f = Black         $00 = Grey
$30 = White         $10 = Light grey
$01 = Dark blue     $11 = Blue
$21 = Light blue    $31 = Pale blue
$06 = Dark red      $16 = Red
$26 = Light red     $36 = Pink
$0a = Dark green    $1a = Green
$2a = Light green   $3a = Pale green
```

**Setting a 4-colour palette:**
```asm
    lda #$3f
    sta $2006
    lda #$00
    sta $2006

    lda #$0f        ; Colour 0: Black (background)
    sta $2007
    lda #$21        ; Colour 1: Light blue
    sta $2007
    lda #$16        ; Colour 2: Red
    sta $2007
    lda #$30        ; Colour 3: White
    sta $2007
```

**Concepts explained:**
- Fixed palette (can't define arbitrary RGB)
- Palette RAM at $3f00
- 4 colours per palette set

**Output:** Tile now appears in a chosen colour.

**Experiment:** Try different colour values. Create different moods.

---

### Unit 5: Tile Patterns (CHR Data)
**Time:** 60 minutes
**Builds on:** Unit 4's colour control

**What happens:**
- Each tile is 8×8 pixels
- Stored as two bitplanes (16 bytes total)
- Plane 1 + Plane 2 = 2-bit colour index (0-3)

**Tile encoding:**
```
Tile data is two 8-byte planes:
Plane 0 (bytes 0-7):  Bit 0 of each pixel's colour
Plane 1 (bytes 8-15): Bit 1 of each pixel's colour

Example - a simple smiley:
Plane 0:         Plane 1:         Result:
. . . . . . . .  . . . . . . . .  0 0 0 0 0 0 0 0
. # . . . . # .  . . . . . . . .  0 1 0 0 0 0 1 0
. . . . . . . .  . . . . . . . .  0 0 0 0 0 0 0 0
. . . . . . . .  . . . . . . . .  0 0 0 0 0 0 0 0
# . . . . . . #  . . . . . . . .  1 0 0 0 0 0 0 1
. # # # # # # .  . . . . . . . .  0 1 1 1 1 1 1 0
. . . . . . . .  . . . . . . . .  0 0 0 0 0 0 0 0
. . . . . . . .  . . . . . . . .  0 0 0 0 0 0 0 0
```

**As bytes:**
```asm
    ; Smiley tile
    .byte %00000000     ; Row 0, plane 0
    .byte %01000010     ; Row 1, plane 0 (eyes)
    .byte %00000000     ; Row 2
    .byte %00000000     ; Row 3
    .byte %10000001     ; Row 4 (mouth corners)
    .byte %01111110     ; Row 5 (mouth)
    .byte %00000000     ; Row 6
    .byte %00000000     ; Row 7
    ; Plane 1 (all zeros = colour 1 only)
    .byte $00,$00,$00,$00,$00,$00,$00,$00
```

**Concepts explained:**
- Bitplane graphics
- How 2 bits = 4 colours
- Binary notation in assembly

**Output:** Custom-designed tile on screen.

**Experiment:** Design your own tile (letter, symbol, shape).

---

### Unit 6: The Nametable
**Time:** 60 minutes
**Builds on:** Unit 5's custom tiles

**What happens:**
- The screen is a 32×30 grid of tiles
- This grid is called the "nametable"
- Nametable at $2000 (256×240 visible area)
- Each byte = one tile index

**Nametable layout:**
```
$2000 = Top-left tile
$2001 = Next tile to the right
...
$201f = End of row 0 (32 tiles)
$2020 = Start of row 1
...
$23bf = Bottom-right tile (row 29, column 31)
```

**Filling a row:**
```asm
    lda #$20
    sta $2006
    lda #$00
    sta $2006           ; Start at $2000

    ldx #32             ; 32 tiles per row
fill_row:
    lda #$01            ; Tile index 1
    sta $2007           ; PPU address auto-increments
    dex
    bne fill_row
```

**Concepts explained:**
- Tile-based display
- Grid coordinates → memory address
- Auto-increment behaviour of $2007

**Output:** Full row of tiles across the top.

**Experiment:** Fill different rows. Create patterns.

---

### Unit 7: Drawing Text
**Time:** 75 minutes
**Builds on:** Unit 6's nametable control

**What happens:**
- Create alphabet tiles (A-Z)
- Write text by placing tile indices
- "NEON NEXUS" title on screen

**Alphabet in CHR (simplified - just capital letters):**
```asm
.segment "CHARS"
    ; Tile 0: empty
    .byte $00,$00,$00,$00,$00,$00,$00,$00
    .byte $00,$00,$00,$00,$00,$00,$00,$00

    ; Tile 1: 'A'
    .byte %00111100
    .byte %01100110
    .byte %01100110
    .byte %01111110
    .byte %01100110
    .byte %01100110
    .byte %01100110
    .byte %00000000
    .byte $00,$00,$00,$00,$00,$00,$00,$00

    ; Tile 2: 'B' ... etc
```

**Writing text:**
```asm
    ; Position at row 10, column 11 (centre-ish)
    ; Address = $2000 + (10 * 32) + 11 = $214b
    lda #$21
    sta $2006
    lda #$4b
    sta $2006

    ; Write "NEON NEXUS" as tile indices
    ; N=14, E=5, O=15, N=14, space=0, N=14, E=5, X=24, U=21, S=19
    lda #14 : sta $2007  ; N
    lda #5  : sta $2007  ; E
    lda #15 : sta $2007  ; O
    lda #14 : sta $2007  ; N
    lda #0  : sta $2007  ; (space)
    lda #14 : sta $2007  ; N
    lda #5  : sta $2007  ; E
    lda #24 : sta $2007  ; X
    lda #21 : sta $2007  ; U
    lda #19 : sta $2007  ; S
```

**Concepts explained:**
- Tiles as a font
- Calculating nametable addresses
- Sequential writes for strings

**Output:** "NEON NEXUS" displayed on screen.

**Experiment:** Write your own message. Centre it properly.

---

### Unit 8: NMI and Vblank
**Time:** 75 minutes
**Builds on:** Unit 7's text display

**What happens:**
- PPU draws the screen constantly
- Vblank = brief pause between frames
- NMI = interrupt that fires at vblank
- ONLY write to PPU during vblank (or get glitches)

**The NMI handler:**
```asm
nmi:
    pha                 ; Save A
    txa
    pha                 ; Save X
    tya
    pha                 ; Save Y

    ; --- Safe to write to PPU here ---
    ; This is called 60 times per second

    pla
    tay                 ; Restore Y
    pla
    tax                 ; Restore X
    pla                 ; Restore A
    rti                 ; Return from interrupt
```

**Enabling NMI:**
```asm
    lda #%10001000      ; Enable NMI, background pattern table 0
    sta $2000
```

**Concepts explained:**
- Vblank timing
- Why NMI matters
- Register preservation in interrupts
- Frame rate (60 fps on NTSC)

**Output:** Same display, but now structured for animation.

**Experiment:** Increment a variable in NMI. Watch it count frames.

---

### Unit 9: Palette Animation
**Time:** 60 minutes
**Builds on:** Unit 8's NMI structure

**What happens:**
- Change palette colours each frame
- Create cycling/pulsing effects
- NMI is the game loop

**Palette cycling:**
```asm
.zeropage
frame_count: .res 1
colour_index: .res 1

.code
nmi:
    pha
    txa
    pha

    ; Every 8 frames, cycle the colour
    inc frame_count
    lda frame_count
    and #$07
    bne no_change

    ; Cycle through colour ramp
    inc colour_index
    lda colour_index
    and #$03            ; 4 colours in cycle
    tax
    lda colour_ramp,x

    ; Update palette
    lda #$3f
    sta $2006
    lda #$01            ; Palette colour 1
    sta $2006
    lda colour_ramp,x
    sta $2007

no_change:
    ; Reset scroll (important after PPU writes!)
    lda #$00
    sta $2005
    sta $2005

    pla
    tax
    pla
    rti

colour_ramp:
    .byte $11, $21, $31, $21  ; Blue pulse: dark → light → dark
```

**Concepts explained:**
- Animation via palette changes
- Frame counting
- Scroll reset after PPU writes
- Lookup tables for animation data

**Output:** Pulsing colour effect on title text.

**Experiment:** Different colour ramps. Different speeds.

---

### Unit 10: Multiple Palettes
**Time:** 60 minutes
**Builds on:** Unit 9's palette animation

**What happens:**
- Background has 4 palette sets (not just one)
- Attribute table controls which palette each 16×16 area uses
- More colourful displays

**Attribute table:**
```
Nametable at $2000-$23bf (960 bytes for 32×30 tiles)
Attribute table at $23c0-$23ff (64 bytes)

Each attribute byte controls a 32×32 pixel area (4×4 tiles)
Each 2 bits selects palette for one 16×16 quadrant:

    Bits 0-1: Top-left quadrant
    Bits 2-3: Top-right quadrant
    Bits 4-5: Bottom-left quadrant
    Bits 6-7: Bottom-right quadrant
```

**Setting attributes:**
```asm
    lda #$23
    sta $2006
    lda #$c0
    sta $2006           ; Start of attribute table

    ; First attribute byte controls tiles 0-3 in rows 0-3
    lda #%11100100      ; Different palette for each quadrant
    sta $2007
```

**Concepts explained:**
- Attribute table layout
- Palette per 16×16 region
- Bit packing

**Output:** Multi-coloured title screen using all 4 palettes.

**Experiment:** Create colour regions. Design a logo with multiple colours.

---

### Unit 11: Screen Layout Design
**Time:** 60 minutes
**Builds on:** Unit 10's multiple palettes

**What happens:**
- Design a complete title screen layout
- Border tiles, decorative elements
- Centre the title, add "PRESS START"

**Screen layout planning:**
```
Row 0-2:   Top border decoration
Row 3-9:   Empty (black)
Row 10:    "NEON NEXUS" (centered)
Row 11-19: Empty
Row 20:    "PRESS START" (centered, different colour)
Row 21-29: Bottom area / copyright
```

**Concepts explained:**
- Screen composition
- Visual hierarchy
- Planning before coding

**Output:** Professional-looking title screen layout.

**Experiment:** Add decorative corner tiles. Create a frame.

---

### Unit 12: Reading the Controller
**Time:** 75 minutes
**Builds on:** Unit 11's complete display

**What happens:**
- Controller at $4016/$4017
- Strobe then read 8 times for 8 buttons
- A, B, Select, Start, Up, Down, Left, Right

**Reading controller 1:**
```asm
read_controller:
    ; Strobe the controller
    lda #$01
    sta $4016
    lda #$00
    sta $4016

    ; Read 8 buttons into controller_state
    ldx #8
read_loop:
    lda $4016           ; Read one button
    lsr                 ; Shift bit 0 into carry
    rol controller_state ; Roll carry into result
    dex
    bne read_loop
    rts

; controller_state bits:
; Bit 7: A
; Bit 6: B
; Bit 5: Select
; Bit 4: Start
; Bit 3: Up
; Bit 2: Down
; Bit 1: Left
; Bit 0: Right
```

**Concepts explained:**
- Memory-mapped I/O for controllers
- Strobe/read protocol
- Bit shifting and rotation

**Output:** Controller state read each frame.

**Experiment:** Display button presses on screen (change tile colour when pressed).

---

### Unit 13: Start Button Response
**Time:** 60 minutes
**Builds on:** Unit 12's controller reading

**What happens:**
- Wait for Start button on title screen
- Transition to "game" screen
- Basic state machine

**State machine:**
```asm
.zeropage
game_state: .res 1

.code
TITLE_SCREEN = 0
GAME_SCREEN = 1

nmi:
    ; ... save registers ...

    jsr read_controller

    lda game_state
    cmp #TITLE_SCREEN
    beq do_title
    cmp #GAME_SCREEN
    beq do_game
    jmp nmi_done

do_title:
    ; Check for Start button
    lda controller_state
    and #%00010000      ; Start button mask
    beq nmi_done        ; Not pressed

    ; Transition to game screen
    lda #GAME_SCREEN
    sta game_state
    jsr draw_game_screen
    jmp nmi_done

do_game:
    ; Game logic here (placeholder)
    jmp nmi_done

nmi_done:
    ; ... restore registers ...
    rti
```

**Concepts explained:**
- State machines
- Game structure
- Screen transitions

**Output:** Press Start → screen changes.

---

### Unit 14: Integration and Polish
**Time:** 60 minutes
**Builds on:** Unit 13's state machine

**What happens:**
- Add "blinking" PRESS START text
- Sound effect stub (no APU yet — that's Phase 2)
- Clean code organisation

**Blinking text:**
```asm
blink_counter: .res 1

update_blink:
    inc blink_counter
    lda blink_counter
    and #$20            ; Toggle every 32 frames
    beq show_text
hide_text:
    ; Write spaces over "PRESS START"
    jmp blink_done
show_text:
    ; Write "PRESS START"
blink_done:
    rts
```

**Output:** Complete title screen:
- "NEON NEXUS" with palette cycling
- Blinking "PRESS START"
- Start button transitions to game screen

---

### Unit 15: What Can Go Wrong
**Time:** 60 minutes
**Builds on:** All previous units

**Common NES bugs catalogued:**

**Bug 1: Black Screen (Nothing Displays)**
```
Symptom: Emulator shows solid black
Check 1: Is $2001 set to enable rendering? (should have bits 3,4 set)
Check 2: Is header correct? (PRG/CHR bank counts)
Check 3: Did you wait for PPU warmup? (two vblank waits)
Check 4: Are palette colours all $0f? (black on black)
```

**Bug 2: Garbage on Screen**
```
Symptom: Random tiles everywhere
Check 1: CHR bank specified in header?
Check 2: Writing to correct nametable address?
Check 3: Wrote to PPU outside vblank?
```

**Bug 3: Scroll Jumping/Glitching**
```
Symptom: Screen position shifts unexpectedly
Check 1: Reset scroll after PPU address writes?
         lda #$00
         sta $2005
         sta $2005
Check 2: Doing PPU writes outside NMI?
```

**Bug 4: Controller Not Responding**
```
Symptom: Button presses ignored
Check 1: Strobe sequence correct? (write 1, then 0, to $4016)
Check 2: Reading correct number of times? (8 reads)
Check 3: Checking correct bit for button?
```

**Bug 5: Colours Wrong**
```
Symptom: Unexpected colours
Check 1: Palette address correct? ($3f00)
Check 2: Attribute table set for correct palette?
Check 3: Using colour values that exist? (some are duplicates)
```

**Debugging tools introduced:**
- FCEUX debugger: PPU viewer, nametable viewer
- How to inspect palette RAM
- How to check what's in CHR

---

### Unit 16: Fixing Broken Code
**Time:** 60 minutes
**Builds on:** Unit 15's debugging knowledge

**Exercise 1: Black Screen**
```asm
; This should show a tile. Screen is black. Why?
reset:
    sei
    cld
    ldx #$ff
    txs

    bit $2002
:   bit $2002
    bpl :-

    ; Set palette
    lda #$3f
    sta $2006
    lda #$00
    sta $2006
    lda #$0f
    sta $2007
    lda #$30
    sta $2007

    ; Write tile
    lda #$20
    sta $2006
    lda #$00
    sta $2006
    lda #$01
    sta $2007

    ; Enable display          ; <-- Bug: this section missing!
forever:
    jmp forever
```
**Fix:** No writes to $2000/$2001. Add:
```asm
    lda #%00001000
    sta $2000
    lda #%00011110
    sta $2001
```

**Exercise 2: Glitchy Scroll**
```asm
nmi:
    pha

    ; Update palette each frame
    lda #$3f
    sta $2006
    lda #$01
    sta $2006
    lda frame_colour
    sta $2007

    ; Missing something here!      ; <-- Bug

    pla
    rti
```
**Fix:** Need to reset scroll position after PPU writes:
```asm
    lda #$00
    sta $2005
    sta $2005
```

**Exercise 3: Wrong Tile Displayed**
```asm
    ; Should display tile 5, displays tile 0
    lda #$20
    sta $2006
    lda #$00            ; <-- Bug: wrote address low byte
    sta $2006
    sta $2007           ; <-- Bug: A still contains 0, not 5!
```
**Fix:** Load tile index before writing:
```asm
    lda #$20
    sta $2006
    lda #$00
    sta $2006
    lda #$05            ; Load tile index
    sta $2007
```

**Phase 1 Complete.**

---

## Phase 1 Summary

| Unit | Focus | Key Concept | Output |
|------|-------|-------------|--------|
| 1 | First tile | — | Tile on screen |
| 2 | iNES header | ROM structure | Understanding |
| 3 | PPU addressing | $2006/$2007 | Understanding |
| 4 | Palettes | Colour selection | Coloured tile |
| 5 | CHR data | Bitplane tiles | Custom tile |
| 6 | Nametable | Tile grid | Row of tiles |
| 7 | Text | Tile font | "NEON NEXUS" |
| 8 | NMI | Vblank timing | Animation ready |
| 9 | Palette animation | Frame counting | Pulsing colours |
| 10 | Attributes | Multiple palettes | Multi-colour screen |
| 11 | Layout | Screen design | Title screen |
| 12 | Controller | Input reading | Buttons read |
| 13 | State machine | Game structure | Start transitions |
| 14 | Polish | Integration | Complete title |
| 15 | Debug theory | Black screen diagnosis | Debug reference |
| 16 | Debug practice | Hands-on fixes | Fixed programs |

**Phase 1 Result:** Working title screen with animation, input, and state machine + ability to debug common PPU problems.

**Phase 2 Preview:** Sprites. Moving objects. Collision detection.

---

## NES-Specific Challenges Addressed

| Challenge | How Phase 1 Addresses It |
|-----------|-------------------------|
| No direct pixels | Units 5-6: Tile system explained thoroughly |
| PPU is separate | Unit 3: Dedicated unit on PPU communication |
| Vblank timing | Unit 8: NMI explained before any animation |
| Attribute complexity | Unit 10: Full unit on attribute table |
| Black screen terror | Units 15-16: Dedicated debugging |

---

**Version:** 1.0
**Last Updated:** 2026-01-17
