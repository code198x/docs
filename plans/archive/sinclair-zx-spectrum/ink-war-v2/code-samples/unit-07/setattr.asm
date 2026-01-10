; Unit 7: Setting Attributes
; Demonstrates colouring individual 8×8 cells
;
; This is the core mechanic for Ink War:
; Change a cell's attribute to claim territory

    org 32768

start:
    ; Clear screen and fill with pattern
    call clear_screen
    call fill_pattern

    ; Set border to black
    ld a, 0
    out ($fe), a

    ; Set all attributes to neutral (white on black)
    call clear_attributes

    ; Now demonstrate setting individual cells
    ; Create a pattern of coloured cells

    ; Red cell at row 5, column 10
    ld b, 5             ; Row
    ld c, 10            ; Column
    ld a, %01000010     ; Bright red INK, black PAPER
    call set_attribute

    ; Green cell at row 5, column 12
    ld b, 5
    ld c, 12
    ld a, %01000100     ; Bright green INK
    call set_attribute

    ; Blue cell at row 5, column 14
    ld b, 5
    ld c, 14
    ld a, %01000001     ; Bright blue INK
    call set_attribute

    ; Create a small grid pattern (like Ink War board)
    ; 8x8 grid starting at row 8, column 12

    ld d, 8             ; Start row
grid_row:
    ld e, 12            ; Start column

grid_col:
    ld b, d             ; Row
    ld c, e             ; Column

    ; Alternate colours based on position
    ld a, d
    xor e               ; XOR row and col
    and 1               ; Keep low bit
    jr z, use_cyan
    ld a, %01000110     ; Bright yellow
    jr set_cell
use_cyan:
    ld a, %01000101     ; Bright cyan
set_cell:
    call set_attribute

    inc e               ; Next column
    ld a, e
    cp 20               ; 8 columns (12-19)
    jr nz, grid_col

    inc d               ; Next row
    ld a, d
    cp 16               ; 8 rows (8-15)
    jr nz, grid_row

    ; Wait for keypress
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

; ============================================
; Set attribute at row B, column C to value A
; Input:  B = row (0-23)
;         C = column (0-31)
;         A = attribute byte
; Destroys: HL, preserves A
; ============================================
set_attribute:
    push af             ; Save attribute value
    call get_attr_addr  ; HL = attribute address
    pop af              ; Restore attribute
    ld (hl), a          ; Set the attribute
    ret

; ============================================
; Get attribute address for row B, column C
; Input:  B = row (0-23), C = column (0-31)
; Output: HL = attribute address
; Destroys: A
; ============================================
get_attr_addr:
    ld h, $58           ; Attribute base high byte
    ld a, b             ; A = row
    add a, a            ; × 2
    add a, a            ; × 4
    add a, a            ; × 8
    add a, a            ; × 16
    add a, a            ; × 32
    add a, c            ; + column
    ld l, a             ; L = offset
    ret

; Clear attributes to white on black
clear_attributes:
    ld hl, $5800
    ld de, $5801
    ld bc, 767
    ld (hl), %00000111  ; White INK, black PAPER
    ldir
    ret

; Clear screen
clear_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), 0
    ldir
    ret

; Fill screen with solid pixels
fill_pattern:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), $ff
    ldir
    ret

    end start
