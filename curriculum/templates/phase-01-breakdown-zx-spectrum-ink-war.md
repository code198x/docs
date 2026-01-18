# Phase 1 Breakdown: ZX Spectrum Ink War

**Game:** Ink War (Game 1)
**Phase:** 1 of 8 (128-unit structure)
**Units:** 1-16
**Theme:** Attribute System + First Display

---

## Phase 1 Overview

The ZX Spectrum is challenging because:
- Attribute system causes "colour clash" (8×8 colour cells)
- Screen memory layout is bizarre (not linear)
- No sprites — everything is software-rendered
- Beeper audio is extremely limited

But also rewarding because:
- Hardware is simple to understand
- Attribute system creates a distinctive visual style
- Constraints breed creativity
- The machine feels "honest"

By the end of Phase 1, learners will:
- Have coloured graphics on screen
- Understand the attribute system deeply
- Know the screen memory layout
- Be able to diagnose "wrong colours" and "blank screen" problems

**Phase 1 Output:** Coloured playing field with selectable cells, keyboard-controlled cursor, and border effects.

---

## Unit Progression

### Unit 1: Your First Attribute
**Time:** 45 minutes
**Builds on:** Nothing — this is the start

**What happens:**
- Type complete working program
- Assemble and run in Fuse
- See a single coloured cell on screen

**Key code (complete, runnable):**
```asm
; Ink War - Unit 1
; Assemble: pasmonext --sna inkwar.asm inkwar.sna

        org $8000

start:
        ; Set border to black
        ld a,0
        out ($fe),a

        ; Clear the screen (pixels)
        ld hl,$4000
        ld de,$4001
        ld bc,$17ff
        ld (hl),0
        ldir

        ; Clear attributes (black on black)
        ld hl,$5800
        ld de,$5801
        ld bc,$02ff
        ld (hl),0
        ldir

        ; Set one attribute cell to bright cyan on black
        ld a,%01000101      ; Bright + cyan ink
        ld ($5800),a        ; Top-left attribute

        ; Fill that cell with pixels
        ld hl,$4000         ; Top-left of screen memory
        ld b,8              ; 8 rows per character cell
fill:
        ld (hl),$ff         ; All pixels on
        inc h               ; Next pixel row (weird addressing!)
        djnz fill

        ; Loop forever
loop:
        jr loop
```

**What learner sees:** Bright cyan square in the top-left corner. Everything else black.

**Concepts introduced (not explained):**
- Screen memory at $4000, attributes at $5800
- `ld` and `out` instructions do things
- Attributes control colour
- Screen addressing is strange (`inc h` for next row?!)

**Output:** Single coloured square.

**Experiment:** Change `%01000101` to different values. Watch colour change.

---

### Unit 2: The Attribute Byte
**Time:** 60 minutes
**Builds on:** Unit 1's working display

**What happens:**
- Decode the attribute byte format
- Understand INK, PAPER, BRIGHT, FLASH
- 8 colours × 2 brightness levels

**Attribute byte format:**
```
Bit 7: FLASH (1 = flashing)
Bit 6: BRIGHT (1 = bright colours)
Bits 5-3: PAPER (background colour, 0-7)
Bits 2-0: INK (foreground colour, 0-7)

Colour codes:
0 = Black     4 = Green
1 = Blue      5 = Cyan
2 = Red       6 = Yellow
3 = Magenta   7 = White
```

**Building attributes:**
```asm
; Bright red ink on yellow paper
; FLASH=0, BRIGHT=1, PAPER=6 (yellow), INK=2 (red)
        ld a,%01110010      ; Binary: 0 1 110 010
        ld ($5800),a

; Same thing calculated:
        ld a,2              ; INK = red
        or 6*8              ; PAPER = yellow (shift left 3)
        or 64               ; BRIGHT = on
        ld ($5800),a
```

**Concepts explained:**
- Attribute byte structure
- INK vs PAPER
- BRIGHT doubles intensity
- FLASH causes alternation (every 16 frames)

**Output:** Same square, but learner controls the colour.

**Experiment:** Try FLASH. Create all 16 colour combinations.

---

### Unit 3: The Attribute Grid
**Time:** 60 minutes
**Builds on:** Unit 2's attribute understanding

**What happens:**
- The screen is a 32×24 grid of attribute cells
- Each cell is 8×8 pixels
- Attributes at $5800-$5aff (768 bytes)

**Grid layout:**
```
$5800 = Row 0, Column 0 (top-left)
$5801 = Row 0, Column 1
...
$581f = Row 0, Column 31
$5820 = Row 1, Column 0
...
$5aff = Row 23, Column 31 (bottom-right)

Address = $5800 + (row × 32) + column
```

**Filling a row:**
```asm
        ld hl,$5800         ; Start of attributes
        ld b,32             ; 32 columns
        ld a,%01000010      ; Red ink
fill_row:
        ld (hl),a
        inc hl
        djnz fill_row
```

**Filling the whole screen:**
```asm
        ld hl,$5800
        ld de,$5801
        ld bc,767           ; 768-1 bytes
        ld (hl),%01000010   ; Red
        ldir                ; Copy to all attributes
```

**Concepts explained:**
- Linear attribute memory
- Row/column to address calculation
- LDIR for fast fills

**Output:** Full row or screen of colour.

**Experiment:** Create patterns. Stripes. Checkerboards.

---

### Unit 4: Screen Memory — The Weird Layout
**Time:** 75 minutes
**Builds on:** Unit 3's attribute grid

**What happens:**
- Screen pixels at $4000-$57ff
- NOT in linear order!
- Address calculation is complex

**The bizarre truth:**
```
Screen is divided into thirds (0-63, 64-127, 128-191)
Within each third, lines interleave

Line 0:   $4000
Line 1:   $4100 (not $4020!)
Line 2:   $4200
...
Line 7:   $4700
Line 8:   $4020 (back to first character row, next pixel row)
...
Line 63:  $47e0
Line 64:  $4800 (second third begins)
```

**Address calculation:**
```asm
; Calculate screen address for pixel at (x, y)
; Input: b=y (0-191), c=x (0-255)
; Output: hl=screen address, a=bit mask

get_pixel_addr:
        ld a,b
        and %00000111       ; Low 3 bits of Y
        or $40              ; Screen base high byte
        ld h,a

        ld a,b
        rra
        rra
        rra
        and %00011000       ; Bits 3-4 of Y
        or h
        ld h,a

        ld a,b
        rla
        rla
        and %11100000       ; Bits 5-7 of Y → bits 5-7
        ld l,a

        ld a,c
        rra
        rra
        rra
        and %00011111       ; X ÷ 8
        or l
        ld l,a

        rts
```

**Why this layout?**
- Optimised for the ULA chip
- Character rows are consecutive in high byte
- Makes text rendering faster
- Makes graphics... interesting

**Concepts explained:**
- Non-linear screen addressing
- Third/character-row/pixel-row breakdown
- Why Sinclair did it this way

**Output:** Understanding. Pain. Enlightenment.

**Experiment:** Use `inc h` trick for vertical lines (within character rows).

---

### Unit 5: Simpler Screen Access
**Time:** 60 minutes
**Builds on:** Unit 4's screen layout

**What happens:**
- Build helper routines
- Lookup tables for speed
- Practical approaches

**Line address table:**
```asm
; Pre-calculated addresses for each screen line
line_table:
        dw $4000,$4100,$4200,$4300,$4400,$4500,$4600,$4700
        dw $4020,$4120,$4220,$4320,$4420,$4520,$4620,$4720
        dw $4040,$4140,$4240,$4340,$4440,$4540,$4640,$4740
        ; ... continue for all 192 lines
```

**Using the table:**
```asm
; Get address of line in A
; Returns address in HL
get_line_addr:
        ld l,a
        ld h,0
        add hl,hl           ; ×2 (word table)
        ld de,line_table
        add hl,de
        ld a,(hl)
        inc hl
        ld h,(hl)
        ld l,a
        ret
```

**Concepts explained:**
- Lookup tables trade memory for speed
- Pre-calculation
- Practical workarounds

**Output:** Usable screen access routines.

**Experiment:** Draw horizontal and vertical lines easily.

---

### Unit 6: Drawing Shapes
**Time:** 60 minutes
**Builds on:** Unit 5's screen routines

**What happens:**
- Fill rectangles
- Draw borders
- Clear regions

**Rectangle fill:**
```asm
; Fill rectangle with solid colour
; b=height in pixels, c=width in bytes
; hl=top-left address
fill_rect:
        push hl
        push bc
        ld a,c              ; Width in bytes
.row:
        ld (hl),$ff         ; Solid pixels
        inc l
        dec c
        jr nz,.row

        pop bc
        pop hl

        ; Move to next line (within character row)
        inc h
        ld a,h
        and 7
        jr nz,.same_char_row

        ; Crossed character boundary
        ld a,l
        add a,32
        ld l,a
        jr nc,.no_carry
        inc h
.no_carry:
        ld a,h
        sub 8
.same_char_row:

        djnz fill_rect
        ret
```

**Concepts explained:**
- Multi-row drawing
- Handling character row boundaries
- Byte-aligned shapes

**Output:** Can draw rectangles on screen.

**Experiment:** Create a game board grid.

---

### Unit 7: The Colour Clash
**Time:** 60 minutes
**Builds on:** Unit 6's drawing

**What happens:**
- THE defining Spectrum characteristic
- Each 8×8 cell can only have 2 colours
- Design WITH the limitation, not against it

**The problem:**
```
If you draw red pixels in a cell that has blue ink,
the pixels appear blue, not red.

Each cell = 1 INK colour + 1 PAPER colour
All pixels in that cell must be one or the other.
```

**Design strategies:**
```
1. EMBRACE IT: Design graphics on 8×8 grid
   - Each game element fits in cells
   - Plan colour boundaries

2. MONOCHROME PLAY AREA: Use attribute colour for
   - Borders only
   - Score/status areas
   - Play area is single colour

3. ATTRIBUTE-ONLY GRAPHICS:
   - No pixel detail
   - Each cell is solid INK or PAPER
   - Game elements are cell-sized
```

**Ink War's approach:**
- Play field is a grid of cells
- Each cell is either "claimed" (player colour) or "empty"
- No fine pixel detail needed
- Colour clash becomes a feature, not a bug

**Concepts explained:**
- Why colour clash happens
- Design approaches
- Turning limitation into style

**Output:** Understanding of what makes Spectrum games look "Spectrum-y".

---

### Unit 8: Keyboard Input
**Time:** 60 minutes
**Builds on:** Unit 7's design understanding

**What happens:**
- Keyboard is memory-mapped
- Read via IN instruction
- Half-rows of keys

**Keyboard matrix:**
```
Port $fefe: SHIFT, Z, X, C, V
Port $fdfe: A, S, D, F, G
Port $fbfe: Q, W, E, R, T
Port $f7fe: 1, 2, 3, 4, 5
Port $effe: 0, 9, 8, 7, 6
Port $dffe: P, O, I, U, Y
Port $bffe: ENTER, L, K, J, H
Port $7ffe: SPACE, SYM, M, N, B

Each row returns 5 bits (bits 0-4), active low.
Bit 0 = rightmost key in row.
```

**Reading keys:**
```asm
; Check if Q is pressed
; Q is port $fbfe, bit 0
check_q:
        ld a,$fb
        in a,($fe)
        bit 0,a
        ret                 ; Z flag set if pressed

; Check cursor keys (5,6,7,8)
check_up:                   ; 7
        ld a,$ef
        in a,($fe)
        bit 3,a
        ret

check_down:                 ; 6
        ld a,$ef
        in a,($fe)
        bit 4,a
        ret

check_left:                 ; 5
        ld a,$f7
        in a,($fe)
        bit 4,a
        ret

check_right:                ; 8
        ld a,$ef
        in a,($fe)
        bit 2,a
        ret
```

**Concepts explained:**
- IN instruction
- Keyboard matrix
- Active-low logic
- Common key mappings (QAOP, 5678)

**Output:** Can detect key presses.

**Experiment:** Multiple simultaneous keys.

---

### Unit 9: Game Loop and Timing
**Time:** 60 minutes
**Builds on:** Unit 8's input

**What happens:**
- Main game loop structure
- HALT for frame sync
- Consistent timing

**Basic game loop:**
```asm
main_loop:
        halt                ; Wait for interrupt (frame sync)

        call read_input
        call update_game
        call draw_screen

        jr main_loop
```

**Frame timing:**
```
PAL Spectrum: 50 frames per second
Each frame: 20ms

HALT waits for the next vertical blank interrupt.
This gives consistent 50fps timing.
```

**Enabling interrupts:**
```asm
        ei                  ; Enable interrupts
main_loop:
        halt                ; Wait for frame
        ; ... game code ...
        jr main_loop
```

**Concepts explained:**
- Interrupt-driven timing
- HALT instruction
- Frame rate
- Why consistent timing matters

**Output:** Stable game loop.

---

### Unit 10: Moving a Cursor
**Time:** 60 minutes
**Builds on:** Unit 9's game loop

**What happens:**
- Store cursor position
- Move based on input
- Boundary checking

**Cursor movement:**
```asm
cursor_x:   db 16           ; Column (0-31)
cursor_y:   db 12           ; Row (0-23)

move_cursor:
        ; Check left (5)
        ld a,$f7
        in a,($fe)
        bit 4,a
        jr nz,.not_left
        ld a,(cursor_x)
        or a                ; At left edge?
        jr z,.not_left
        dec a
        ld (cursor_x),a
.not_left:

        ; Check right (8)
        ld a,$ef
        in a,($fe)
        bit 2,a
        jr nz,.not_right
        ld a,(cursor_x)
        cp 31               ; At right edge?
        jr z,.not_right
        inc a
        ld (cursor_x),a
.not_right:

        ; ... similar for up/down ...
        ret
```

**Concepts explained:**
- Variables in memory
- Boundary checking
- Responding to input

**Output:** Movable cursor position.

---

### Unit 11: Drawing the Cursor
**Time:** 60 minutes
**Builds on:** Unit 10's cursor movement

**What happens:**
- Highlight current cell
- Use BRIGHT or FLASH for visibility
- Erase/redraw pattern

**Cursor display:**
```asm
draw_cursor:
        ; Calculate attribute address
        ld a,(cursor_y)
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl           ; ×32
        ld a,(cursor_x)
        add a,l
        ld l,a
        ld de,$5800
        add hl,de           ; HL = attribute address

        ; Set cursor colour (flashing white)
        ld (hl),%11000111   ; FLASH + BRIGHT + white on white
        ret

erase_cursor:
        ; Same calculation, reset to background
        ; ...
        ld (hl),%00000000   ; Black on black
        ret
```

**Concepts explained:**
- Coordinate to attribute address
- Visual feedback
- Erase/redraw cycle

**Output:** Visible, moving cursor.

---

### Unit 12: Game Board Setup
**Time:** 60 minutes
**Builds on:** Unit 11's cursor

**What happens:**
- Define play area (e.g., 16×16 cells)
- Draw border
- Set initial colours

**Board setup:**
```asm
BOARD_X     equ 8           ; Left offset
BOARD_Y     equ 4           ; Top offset
BOARD_W     equ 16          ; Width in cells
BOARD_H     equ 16          ; Height in cells

draw_board:
        ; Draw border
        call draw_border

        ; Fill play area with empty colour
        ld hl,$5800 + (BOARD_Y * 32) + BOARD_X
        ld b,BOARD_H
.row:
        push hl
        push bc
        ld b,BOARD_W
        ld a,%00000000      ; Black (empty cell)
.cell:
        ld (hl),a
        inc hl
        djnz .cell
        pop bc
        pop hl
        ld de,32
        add hl,de           ; Next row
        djnz .row
        ret
```

**Concepts explained:**
- Game area definition
- Constants for configuration
- Nested loops

**Output:** Bordered game board.

---

### Unit 13: Cell Claiming
**Time:** 60 minutes
**Builds on:** Unit 12's board

**What happens:**
- Press fire to claim cell
- Cell changes to player colour
- Track claimed cells

**Cell state array:**
```asm
; 16×16 = 256 bytes, one per cell
; 0 = empty, 1 = player 1, 2 = player 2
cell_states:
        defs 256,0          ; All empty initially

claim_cell:
        ; Calculate cell index
        ld a,(cursor_y)
        sub BOARD_Y
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl           ; ×16 (board width)
        ld a,(cursor_x)
        sub BOARD_X
        add a,l
        ld l,a
        ld de,cell_states
        add hl,de

        ; Check if already claimed
        ld a,(hl)
        or a
        ret nz              ; Already claimed

        ; Claim for player 1
        ld (hl),1
        call update_cell_colour
        ret
```

**Concepts explained:**
- Game state arrays
- Index calculation
- State checking

**Output:** Cells can be claimed and show player colour.

---

### Unit 14: Integration and Polish
**Time:** 60 minutes
**Builds on:** All previous units

**What happens:**
- Title screen
- Score display
- Border colour feedback
- Complete game loop

**Complete program structure:**
```asm
main:
        call init_screen
        call show_title
        call wait_for_key
        call init_game
game_loop:
        halt
        call read_input
        call update_cursor
        call check_claim
        call update_display
        call check_win
        jr nz,game_loop
        call show_winner
        jr main
```

**Output:** Complete Phase 1 game:
- Title screen
- 16×16 game board
- Keyboard cursor control
- Cell claiming
- Basic scoring

---

### Unit 15: What Can Go Wrong
**Time:** 60 minutes
**Builds on:** All previous units

**Common Spectrum bugs catalogued:**

**Bug 1: Wrong Colours (Colour Clash)**
```
Symptom: Colours appear in wrong places
Check 1: Are you respecting 8×8 cell boundaries?
Check 2: Did you set PAPER and INK correctly?
Check 3: Are pixels in the right cells?

Remember: Each 8×8 cell = ONE ink + ONE paper colour.
If your sprite crosses cell boundaries, expect colour clash.
```

**Bug 2: Blank Screen / No Display**
```
Symptom: Screen stays black
Check 1: Did code actually run? (set border colour to verify)
Check 2: Are attributes all black-on-black ($00)?
Check 3: Are pixels set in screen memory?
Check 4: Is screen cleared but attributes not set?
```

**Bug 3: Corrupt Screen**
```
Symptom: Garbage, wrong positions
Check 1: Screen addressing correct? (remember weird layout!)
Check 2: LDIR count correct?
Check 3: Crossing third boundaries correctly?
```

**Bug 4: Keyboard Not Responding**
```
Symptom: No reaction to keys
Check 1: Using correct port for that key row?
Check 2: Checking correct bit?
Check 3: Active LOW — bit is 0 when pressed, not 1!
Check 4: Are interrupts enabled? (needed for HALT)
```

**Bug 5: Timing Issues**
```
Symptom: Flickering, inconsistent speed
Check 1: Using HALT for frame sync?
Check 2: Game logic completing within frame time?
Check 3: Too much work in one frame?
```

**Bug 6: Border Colour Wrong**
```
Symptom: Border not changing
Check 1: OUT instruction correct? (out ($fe),a)
Check 2: Only bits 0-2 matter for colour
Check 3: Bit 4 (MIC) might cause audio buzz if set
```

**Debugging tools:**
- Fuse debugger
- Memory viewer
- Attribute viewer
- Step through code

---

### Unit 16: Fixing Broken Code
**Time:** 60 minutes
**Builds on:** Unit 15's debugging knowledge

**Exercise 1: Black Screen**
```asm
; Should show a red square. Screen stays black.
        org $8000

start:
        ; Clear screen
        ld hl,$4000
        ld de,$4001
        ld bc,$17ff
        ld (hl),0
        ldir

        ; Bug: No attribute set!

        ; Fill pixels
        ld hl,$4000
        ld b,8
fill:   ld (hl),$ff
        inc h
        djnz fill

loop:   jr loop
```
**Fix:** Need to set attribute:
```asm
        ld a,%01000010      ; Red ink
        ld ($5800),a
```

**Exercise 2: Keyboard Not Working**
```asm
; Should detect SPACE. Doesn't work.
check_space:
        ld a,$7f
        in a,($fe)
        bit 0,a             ; <-- Bug: SPACE is bit 0 on port $7ffe
        ret                 ; but we used $7f, not $7f + FE
```
**Fix:** Port address construction:
```asm
        ld a,$7f            ; High byte of port
        in a,($fe)          ; Full port = $7ffe
        ; This IS correct — A goes to high byte of port address
        ; But bit 0 is the check for SPACE — that's right too
        ; Actually the bug is: SPACE returns 0 when pressed (active low)
        ; So BIT 0,A sets Z if pressed — that's correct
        ; Let me reconsider...
```

Actually, let me provide a clearer bug:

**Exercise 2: Keyboard Wrong Key**
```asm
; Should detect Q (up). Detects W instead.
check_q:
        ld a,$fb
        in a,($fe)
        bit 1,a             ; <-- Bug: Q is bit 0, not bit 1
        ret
```
**Fix:** Q is bit 0:
```asm
        bit 0,a             ; Q is bit 0 on port $fbfe
```

**Exercise 3: Corrupt Display**
```asm
; Should fill top third of screen. Corrupts.
fill_third:
        ld hl,$4000
        ld de,$4001
        ld bc,$0800         ; <-- Bug: should be $07ff (2048-1)
        ld (hl),$ff
        ldir
        ret
```
**Fix:** LDIR copies BC+1 bytes, so use length-1:
```asm
        ld bc,$07ff         ; 2048-1 = $7ff
```

**Exercise 4: Attribute Address Wrong**
```asm
; Should highlight row 5, column 10. Highlights wrong cell.
        ld a,5
        ld l,a
        ld h,0
        add hl,hl           ; ×2
        add hl,hl           ; ×4
        add hl,hl           ; ×8
        add hl,hl           ; ×16
        ; Bug: only ×16, should be ×32!
        ld a,10
        add a,l
        ld l,a
        ld de,$5800
        add hl,de
        ld (hl),%01111111
        ret
```
**Fix:** Need one more shift for ×32:
```asm
        add hl,hl           ; ×32
```

**Phase 1 Complete.**

---

## Phase 1 Summary

| Unit | Focus | Key Concept | Output |
|------|-------|-------------|--------|
| 1 | First colour | — | Coloured square |
| 2 | Attribute byte | INK/PAPER/BRIGHT | Colour control |
| 3 | Attribute grid | 32×24 layout | Row/screen fill |
| 4 | Screen memory | Bizarre addressing | Understanding |
| 5 | Screen helpers | Lookup tables | Usable routines |
| 6 | Drawing | Rectangles | Shape drawing |
| 7 | Colour clash | Design constraint | Design approach |
| 8 | Keyboard | IN instruction | Input reading |
| 9 | Game loop | HALT timing | Frame sync |
| 10 | Cursor | Movement | Moving position |
| 11 | Cursor display | Highlight | Visible cursor |
| 12 | Game board | Setup | Bordered area |
| 13 | Cell claiming | State array | Game mechanic |
| 14 | Polish | Integration | Complete game |
| 15 | Debug theory | Wrong colours | Debug reference |
| 16 | Debug practice | Hands-on fixes | Fixed programs |

**Phase 1 Result:** Working game with coloured board, cursor, and cell claiming + ability to debug colour and display problems.

**Phase 2 Preview:** Two players. Beeper sound. Animation.

---

## Spectrum-Specific Challenges Addressed

| Challenge | How Phase 1 Addresses It |
|-----------|-------------------------|
| Attribute system | Units 1-3, 7: Deep coverage |
| Screen layout | Units 4-5: Full explanation + workaround |
| Colour clash | Unit 7: Dedicated design discussion |
| No sprites | Units 6, 11: Software drawing |
| Input quirks | Unit 8: Keyboard matrix explained |

---

## Keyboard Quick Reference (For Debugging)

```
Port    Keys (bit 0 → bit 4)
$fefe:  SHIFT, Z, X, C, V
$fdfe:  A, S, D, F, G
$fbfe:  Q, W, E, R, T
$f7fe:  1, 2, 3, 4, 5
$effe:  0, 9, 8, 7, 6
$dffe:  P, O, I, U, Y
$bffe:  ENTER, L, K, J, H
$7ffe:  SPACE, SYM, M, N, B

Remember: Active LOW — bit is 0 when pressed, 1 when not pressed.
```

---

**Version:** 1.0
**Last Updated:** 2026-01-17
