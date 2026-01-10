; Unit 12: Jumps and Calls
; Demonstrates JP, JR, CALL, RET, and conditional variants
;
; Control flow is how programs make decisions and repeat actions

    org 32768

start:
    call clear_screen       ; CALL to subroutine
    call fill_screen
    call clear_attributes

    ld a, 0
    out ($fe), a

    ; ========================================
    ; Unconditional jumps: JP and JR
    ; ========================================

    ; JP - Jump to address (3 bytes, any distance)
    jp demo_jr              ; Jump over this data

unused_data:
    defb 0, 0, 0, 0         ; This is skipped

demo_jr:
    ; JR - Jump relative (2 bytes, -128 to +127)
    ld a, 5
    jr skip_this            ; Short jump forward

    ; This code is skipped
    ld a, 0

skip_this:
    ; A is still 5

    ; ========================================
    ; Conditional jumps
    ; ========================================

    ; Draw different colours based on conditions
    ld hl, $5800
    ld b, 32                ; 32 cells

condition_loop:
    ld a, b                 ; A = counter
    and %00000011           ; Keep low 2 bits (0-3)

    ; Test conditions
    cp 0
    jr z, colour_black      ; Jump if Zero (A == 0)

    cp 1
    jr z, colour_red        ; Jump if Zero (A == 1)

    cp 2
    jr z, colour_green      ; Jump if Zero (A == 2)

    ; Default: blue
    ld a, %01000001
    jr store_colour

colour_black:
    ld a, %00000000
    jr store_colour

colour_red:
    ld a, %01000010
    jr store_colour

colour_green:
    ld a, %01000100
    ; Fall through to store_colour

store_colour:
    ld (hl), a
    inc hl
    djnz condition_loop     ; Decrement B, Jump if Not Zero

    ; ========================================
    ; CALL and RET - Subroutines
    ; ========================================

    ; Draw pattern using subroutines
    ld b, 5                 ; Row for first pattern
    ld c, 4                 ; Column
    call draw_box           ; Call subroutine

    ld b, 5
    ld c, 14
    call draw_box           ; Call again, different position

    ld b, 5
    ld c, 24
    call draw_box           ; And again

    ; ========================================
    ; Carry flag conditions
    ; ========================================

    ld hl, $5800 + (20 * 32)    ; Row 20
    ld b, 16

carry_demo:
    ld a, b
    sub 8                   ; A = B - 8
    jr c, below_eight       ; Jump if Carry (B < 8)

    ; B >= 8: cyan
    ld a, %01000101
    jr store_carry

below_eight:
    ; B < 8: magenta
    ld a, %01000011

store_carry:
    ld (hl), a
    inc hl
    djnz carry_demo

    ; Wait for key
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret                     ; Return from start (back to BASIC)

; ============================================
; Subroutine: Draw a 4x4 coloured box
; Input: B = top row, C = left column
; ============================================
draw_box:
    push bc                 ; Save position

    ; Calculate attribute address
    ld a, b
    add a, a
    add a, a
    add a, a
    add a, a
    add a, a                ; A = row * 32
    add a, c                ; A = row * 32 + col
    ld l, a
    ld h, $58               ; HL = attribute address

    ; Draw 4 rows of 4 cells
    ld d, 4                 ; Row counter

box_row:
    push hl                 ; Save row start
    ld e, 4                 ; Column counter

box_col:
    ld (hl), %01000110      ; Bright yellow
    inc hl
    dec e
    jr nz, box_col

    pop hl                  ; Restore row start
    ld bc, 32               ; Move to next row
    add hl, bc
    dec d
    jr nz, box_row

    pop bc                  ; Restore original position
    ret                     ; Return to caller

; Standard subroutines
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
    ld (hl), %00000111
    ldir
    ret

    end start
