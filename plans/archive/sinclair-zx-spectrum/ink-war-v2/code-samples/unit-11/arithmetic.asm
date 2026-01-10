; Unit 11: Arithmetic
; Demonstrates ADD, SUB, INC, DEC operations
;
; Arithmetic is how we calculate positions, scores, and game logic

    org 32768

start:
    call clear_screen
    call fill_screen
    call clear_attributes

    ld a, 0
    out ($fe), a        ; Black border

    ; ========================================
    ; INC - Increment (add 1)
    ; ========================================
    ; Draw a diagonal line using INC for both X and Y

    ld hl, $5800        ; Start at top-left
    ld b, 24            ; 24 rows

inc_demo:
    ld (hl), %01000010  ; Bright red
    ; Move diagonally: add 33 to get next row, next column
    ; (32 for next row + 1 for next column)
    ld de, 33
    add hl, de
    djnz inc_demo

    ; ========================================
    ; DEC - Decrement (subtract 1)
    ; ========================================
    ; Draw opposite diagonal using DEC

    ld hl, $5800 + 31   ; Start at top-right
    ld b, 24

dec_demo:
    ld (hl), %01000100  ; Bright green
    ; Move diagonally down-left: add 31
    ; (32 for next row - 1 for previous column)
    ld de, 31
    add hl, de
    djnz dec_demo

    ; ========================================
    ; ADD - Addition
    ; ========================================
    ; Calculate positions using ADD

    ld hl, $5800 + (10 * 32)  ; Row 10
    ld b, 8             ; 8 cells
    ld c, 0             ; Starting colour

add_demo:
    ld a, c             ; Get current colour
    or %01000000        ; Add BRIGHT
    ld (hl), a          ; Store
    inc hl
    ld a, c
    add a, 1            ; ADD 1 to colour
    ld c, a
    djnz add_demo

    ; ========================================
    ; SUB - Subtraction
    ; ========================================
    ; Create countdown effect

    ld hl, $5800 + (12 * 32) + 8  ; Row 12, col 8
    ld b, 8
    ld c, 7             ; Start at colour 7

sub_demo:
    ld a, c
    or %01000000        ; BRIGHT
    ld (hl), a
    inc hl
    ld a, c
    sub 1               ; SUB 1 from colour
    ld c, a
    djnz sub_demo

    ; ========================================
    ; ADD with register pairs
    ; ========================================
    ; ADD HL, DE - 16-bit addition

    ld hl, $5800 + (14 * 32)  ; Row 14
    ld de, 2            ; Step by 2 columns
    ld b, 8

add16_demo:
    ld (hl), %01000101  ; Bright cyan
    add hl, de          ; HL = HL + DE (skip one cell)
    djnz add16_demo

    ; ========================================
    ; Multiplication by repeated ADD
    ; ========================================
    ; Calculate row * 32 using ADD

    ld a, 16            ; Row 16
    ld b, a             ; Counter
    ld hl, 0            ; Result

multiply:
    ld de, 32           ; Add 32 each time
    add hl, de
    djnz multiply

    ; HL now = 16 * 32 = 512
    ; Add attribute base
    ld de, $5800
    add hl, de          ; HL = $5800 + 512 = $5A00

    ; Fill this row with yellow
    ld b, 32
    ld a, %01000110     ; Bright yellow

fill_row:
    ld (hl), a
    inc hl
    djnz fill_row

    ; Wait for key
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

clear_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), 0
    ldir
    ret

fill_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), $ff
    ldir
    ret

clear_attributes:
    ld hl, $5800
    ld de, $5801
    ld bc, 767
    ld (hl), %00000111  ; White on black
    ldir
    ret

    end start
