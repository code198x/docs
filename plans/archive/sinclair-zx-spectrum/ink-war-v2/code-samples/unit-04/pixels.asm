; Unit 4: Drawing Pixels
; Demonstrates setting individual bits in screen memory
;
; Each byte contains 8 pixels. To set one pixel:
; 1. Calculate screen address from Y coordinate
; 2. Add X/8 to get the correct byte
; 3. Calculate bit position (7 - (X AND 7))
; 4. OR the bit into the byte

    org 32768

start:
    call clear_screen
    call set_attributes

    ; Set border to black
    ld a, 0
    out ($fe), a

    ; Draw a rectangle outline
    ; Top edge: Y=32, X=64 to X=191
    ld b, 32            ; Y = 32
    ld c, 64            ; X start
top_edge:
    push bc
    call plot_pixel
    pop bc
    inc c
    ld a, c
    cp 192              ; X = 192? Stop
    jr nz, top_edge

    ; Bottom edge: Y=159, X=64 to X=191
    ld b, 159
    ld c, 64
bottom_edge:
    push bc
    call plot_pixel
    pop bc
    inc c
    ld a, c
    cp 192
    jr nz, bottom_edge

    ; Left edge: Y=32 to Y=159, X=64
    ld b, 32
    ld c, 64
left_edge:
    push bc
    call plot_pixel
    pop bc
    inc b
    ld a, b
    cp 160
    jr nz, left_edge

    ; Right edge: Y=32 to Y=159, X=191
    ld b, 32
    ld c, 191
right_edge:
    push bc
    call plot_pixel
    pop bc
    inc b
    ld a, b
    cp 160
    jr nz, right_edge

    ; Draw diagonal lines inside the box
    ; Diagonal from top-left to bottom-right
    ld b, 33            ; Y start
    ld c, 65            ; X start
diag1:
    push bc
    call plot_pixel
    pop bc
    inc b               ; Y++
    inc c               ; X++
    ld a, b
    cp 159              ; Near bottom?
    jr nz, diag1

    ; Diagonal from top-right to bottom-left
    ld b, 33
    ld c, 190
diag2:
    push bc
    call plot_pixel
    pop bc
    inc b               ; Y++
    dec c               ; X--
    ld a, b
    cp 159
    jr nz, diag2

    ; Wait for keypress
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

; ============================================
; Plot a single pixel
; Input:  B = Y coordinate (0-191)
;         C = X coordinate (0-255)
; Destroys: AF, DE, HL
; ============================================
plot_pixel:
    ; First, get screen address for this Y
    call get_screen_addr    ; HL = base address for row

    ; Add X/8 to get the correct byte
    ld a, c             ; A = X
    srl a               ; Divide by 8
    srl a
    srl a
    add a, l            ; Add to low byte
    ld l, a             ; HL = address of byte containing pixel

    ; Calculate bit position
    ; Bit 7 is leftmost pixel, bit 0 is rightmost
    ; So bit = 7 - (X AND 7), or use lookup/rotate

    ld a, c             ; A = X
    and %00000111       ; Keep low 3 bits (0-7)
    ld b, a             ; B = bit position (0-7)

    ld a, %10000000     ; Start with bit 7 (leftmost)
    jr z, do_plot       ; If position 0, use bit 7 directly

shift_bit:
    srl a               ; Shift right
    djnz shift_bit      ; Repeat B times

do_plot:
    or (hl)             ; Combine with existing pixels
    ld (hl), a          ; Write back
    ret

; ============================================
; Get screen address for pixel row
; Input:  B = Y coordinate (0-191)
; Output: HL = screen address (column 0)
; Destroys: A
; ============================================
get_screen_addr:
    ; Build high byte: 010T TSSS
    ld a, b
    and %00000111       ; Scan line bits
    or %01000000        ; Screen base
    ld h, a

    ld a, b
    and %11000000       ; Third bits
    rrca
    rrca
    rrca
    or h
    ld h, a

    ; Build low byte: RRR0 0000
    ld a, b
    and %00111000       ; Char row bits
    rlca
    rlca
    ld l, a

    ret

; Clear screen
clear_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), 0
    ldir
    ret

; Set attributes to white on black
set_attributes:
    ld hl, $5800
    ld de, $5801
    ld bc, 767
    ld (hl), %00000111  ; Black paper, white ink
    ldir
    ret

    end start
