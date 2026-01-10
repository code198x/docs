; Unit 2: Screen Memory Layout
; Demonstrates the Spectrum's interleaved screen memory
;
; The screen is NOT stored linearly. It's divided into thirds,
; and within each third, scan lines are interleaved.
;
; This program fills each third with a different pattern,
; making the organisation visible.

    org 32768

start:
    ; Clear screen and attributes first
    call clear_screen
    call set_attributes

    ; Set border to black
    ld a, 0
    out ($fe), a

    ; Fill top third ($4000-$47FF) with solid pattern
    ; This covers screen rows 0-63 (top 64 pixels)
    ld hl, $4000
    ld bc, 2048         ; 2KB per third
    ld a, $ff           ; Solid white
    call fill_memory

    ; Fill middle third ($4800-$4FFF) with dotted pattern
    ; This covers screen rows 64-127
    ld hl, $4800
    ld bc, 2048
    ld a, $aa           ; Dotted: 10101010
    call fill_memory

    ; Fill bottom third ($5000-$57FF) with stripe pattern
    ; This covers screen rows 128-191
    ld hl, $5000
    ld bc, 2048
    ld a, $f0           ; Half: 11110000
    call fill_memory

    ; Wait for keypress
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

; Fill BC bytes at HL with value in A
fill_memory:
    ld d, a             ; Save pattern
fill_loop:
    ld (hl), d
    inc hl
    dec bc
    ld a, b
    or c
    jr nz, fill_loop
    ret

; Clear screen to zeros
clear_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), 0
    ldir
    ret

; Set all attributes to white INK on black PAPER
set_attributes:
    ld hl, $5800
    ld de, $5801
    ld bc, 767
    ld (hl), %00000111  ; Black paper, white ink
    ldir
    ret

    end start
