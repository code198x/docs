; Unit 3: Calculating Screen Addresses
; Demonstrates the formula for converting Y coordinates to screen addresses
;
; The Spectrum's interleaved layout requires bit manipulation:
;   High byte: 010T TSSS  (TT=third, SSS=scan line)
;   Low byte:  RRRC CCCC  (RRR=char row, CCCCC=column)

    org 32768

start:
    call clear_screen
    call set_attributes

    ; Set border to blue
    ld a, 1
    out ($fe), a

    ; Draw horizontal lines at every 8th row
    ; This demonstrates the address calculation working
    ; across all three thirds and all scan lines

    ld b, 0             ; Start at Y=0
draw_lines:
    push bc
    call get_screen_addr    ; HL = screen address for row B

    ; Fill entire row with solid pixels
    ld b, 32            ; 32 bytes per row
    ld a, $ff           ; Solid line
fill_row:
    ld (hl), a
    inc l               ; Next column (safe within row)
    djnz fill_row

    pop bc
    ld a, b
    add a, 8            ; Next line (every 8 pixels)
    ld b, a
    cp 192              ; Past bottom of screen?
    jr c, draw_lines    ; No, continue

    ; Wait for keypress
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

; ============================================
; Get screen address for pixel row
; Input:  B = Y coordinate (0-191)
; Output: HL = screen address (column 0)
; Destroys: A
; ============================================
get_screen_addr:
    ; Build high byte: 010T TSSS
    ; TT comes from bits 7-6 of Y (the third)
    ; SSS comes from bits 2-0 of Y (scan line in char)

    ld a, b             ; A = Y coordinate
    and %00000111       ; Keep scan line bits (0-7)
    or %01000000        ; Add screen base ($40)
    ld h, a             ; H = 010T TSSS (partial - TT not set yet)

    ; Now add the third selection
    ld a, b             ; A = Y coordinate again
    and %11000000       ; Keep third bits (0, 64, or 128)
    rrca                ; Rotate right 3 times
    rrca                ; to get into bits 4-3
    rrca
    or h                ; Combine with existing high byte
    ld h, a             ; H complete: 010T TSSS

    ; Build low byte: RRRC CCCC
    ; RRR comes from bits 5-3 of Y (char row within third)
    ; CCCCC is column (0 for this routine)

    ld a, b             ; A = Y coordinate
    and %00111000       ; Keep char row bits
    rlca                ; Rotate left twice
    rlca                ; to get RRR into bits 7-5
    ld l, a             ; L = RRR0 0000 (column 0)

    ret

; Clear screen
clear_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), 0
    ldir
    ret

; Set attributes to white on blue
set_attributes:
    ld hl, $5800
    ld de, $5801
    ld bc, 767
    ld (hl), %00001111  ; Blue paper (001), white ink (111)
    ldir
    ret

    end start
