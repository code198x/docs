; Unit 14: Draw the Game Board
; Creating the 8×8 Ink War game board
;
; The board uses the attribute grid directly - each cell is one attribute square

    org 32768

; Board constants
BOARD_TOP    equ 8           ; Start at row 8 (centred vertically)
BOARD_LEFT   equ 12          ; Start at column 12 (centred horizontally)
BOARD_SIZE   equ 8           ; 8×8 grid

; Colours
BORDER_ATTR  equ %01000000   ; Bright black (border cells)
EMPTY_ATTR   equ %00111000   ; White paper, black ink (empty cells)
GRID_ATTR    equ %01000111   ; Bright white (grid lines)

start:
    ; Clear everything first
    call clear_screen
    call clear_attributes

    ; Set border colour
    ld a, 0                  ; Black border
    out ($fe), a

    ; Draw the game board
    call draw_board

    ; Hold display
hold:
    jr hold

; ============================================
; Draw the complete game board
; An 8×8 grid of cells with border
; ============================================
draw_board:
    push af
    push bc
    push de
    push hl

    ; First, draw the outer border (10×10 area around the 8×8 board)
    ; Top border row
    ld hl, $5800 + ((BOARD_TOP - 1) * 32) + (BOARD_LEFT - 1)
    ld b, 10
    ld a, BORDER_ATTR
draw_top_border:
    ld (hl), a
    inc hl
    djnz draw_top_border

    ; Bottom border row
    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE) * 32) + (BOARD_LEFT - 1)
    ld b, 10
    ld a, BORDER_ATTR
draw_bottom_border:
    ld (hl), a
    inc hl
    djnz draw_bottom_border

    ; Left and right borders (middle rows)
    ld hl, $5800 + (BOARD_TOP * 32) + (BOARD_LEFT - 1)
    ld d, BOARD_SIZE         ; 8 rows
draw_side_borders:
    ld (hl), BORDER_ATTR     ; Left border
    ld bc, 9
    add hl, bc
    ld (hl), BORDER_ATTR     ; Right border
    ld bc, 23                ; Move to next row (32 - 9 = 23)
    add hl, bc
    dec d
    jr nz, draw_side_borders

    ; Now draw the 8×8 board cells
    ; Each cell gets a different shade to show the grid
    ld hl, $5800 + (BOARD_TOP * 32) + BOARD_LEFT
    ld d, BOARD_SIZE         ; 8 rows

draw_board_rows:
    push hl                  ; Save row start
    ld e, BOARD_SIZE         ; 8 columns

draw_board_cols:
    ; Create checkerboard pattern for visibility
    ld a, d                  ; Row counter
    xor e                    ; XOR with column counter
    and 1                    ; Keep only lowest bit
    jr z, use_light

    ; Odd cells - slightly darker
    ld a, %00111000          ; White paper (light grey appearance)
    jr store_cell

use_light:
    ; Even cells - lighter
    ld a, %01111000          ; Bright white paper

store_cell:
    ld (hl), a
    inc hl
    dec e
    jr nz, draw_board_cols

    pop hl                   ; Restore row start
    ld bc, 32                ; Move to next row
    add hl, bc
    dec d
    jr nz, draw_board_rows

    pop hl
    pop de
    pop bc
    pop af
    ret

; ============================================
; Clear screen memory
; ============================================
clear_screen:
    push af
    push bc
    push de
    push hl

    ld hl, $4000
    ld (hl), 0
    ld de, $4001
    ld bc, 6143
    ldir

    pop hl
    pop de
    pop bc
    pop af
    ret

; ============================================
; Clear attributes to black
; ============================================
clear_attributes:
    push af
    push bc
    push de
    push hl

    ld hl, $5800
    ld (hl), %00000000       ; Black paper, black ink
    ld de, $5801
    ld bc, 767
    ldir

    pop hl
    pop de
    pop bc
    pop af
    ret

    end start
