; Unit 9: Z80 Registers
; Demonstrates the main Z80 registers through practical use
;
; Main registers: A, B, C, D, E, H, L
; Register pairs: BC, DE, HL
; Special: IX, IY (index), SP (stack), PC (program counter)

    org 32768

start:
    call clear_screen
    call fill_screen

    ; Set border using A register
    ld a, 1             ; A = 1 (blue)
    out ($fe), a        ; Border = A

    ; Use HL as pointer to attribute memory
    ld hl, $5800        ; HL points to first attribute

    ; Use BC as counter
    ld bc, 768          ; BC = total attributes

    ; Use DE for calculations
    ld de, 0            ; DE = position counter

    ; Use A for attribute value
    ld a, %00000111     ; A = white on black

    ; Fill first 256 attributes (one third) white
fill_white:
    ld (hl), a          ; Store A at address HL
    inc hl              ; HL = HL + 1
    inc de              ; DE = DE + 1
    ; Check if DE reached 256
    ld a, d
    or a                ; Is D non-zero?
    jr z, fill_white    ; No, continue

    ; Fill next 256 attributes red (using A differently)
    ld a, %00000010     ; A = red on black
fill_red:
    ld (hl), a
    inc hl
    inc de
    ; Check if DE reached 512
    ld a, d
    cp 2                ; Is D = 2?
    jr nz, fill_red

    ; Fill remaining 256 attributes green
    ld a, %00000100     ; A = green on black
fill_green:
    ld (hl), a
    inc hl
    inc de
    ; Check if DE reached 768
    ld a, d
    cp 3                ; Is D = 3?
    jr nz, fill_green

    ; Demonstrate index register IX
    ; Use IX to point to middle of screen
    ld ix, $5800 + 384  ; IX = middle row start

    ; Change 8 cells using IX with offset
    ld a, %01000110     ; Bright yellow
    ld (ix+0), a        ; Cell at IX
    ld (ix+1), a        ; Cell at IX+1
    ld (ix+2), a        ; Cell at IX+2
    ld (ix+3), a        ; Cell at IX+3
    ld (ix+4), a
    ld (ix+5), a
    ld (ix+6), a
    ld (ix+7), a

    ; Wait for keypress
wait_key:
    xor a               ; A = 0 (quick way to zero A)
    in a, ($fe)
    cpl                 ; Invert bits
    and $1f             ; Mask key bits
    jr z, wait_key
    ret

; Clear screen memory
clear_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), 0
    ldir
    ret

; Fill screen with pattern
fill_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), $ff
    ldir
    ret

    end start
