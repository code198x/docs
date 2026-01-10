; Unit 1: The Spectrum's Display
; Demonstrates the 256×192 pixel display and memory mapping
;
; The ZX Spectrum screen lives at $4000-$57FF (6144 bytes)
; Each byte represents 8 horizontal pixels
; 256 pixels / 8 = 32 bytes per row
; 192 rows × 32 bytes = 6144 bytes total

    org 32768

start:
    ; Clear the screen first
    call clear_screen

    ; Set border to blue
    ld a, 1
    out ($fe), a

    ; Fill screen memory with stripes
    ; This shows all 6144 bytes of display memory
    ld hl, $4000        ; Screen memory start
    ld bc, 6144         ; Total bytes in display

fill_loop:
    ld a, l             ; Use low byte of address for pattern
    and $01             ; Alternate pattern every byte
    jr z, pattern_a
    ld a, $aa           ; Pattern: 10101010
    jr store_pattern
pattern_a:
    ld a, $55           ; Pattern: 01011010
store_pattern:
    ld (hl), a
    inc hl
    dec bc
    ld a, b
    or c
    jr nz, fill_loop

    ; Now set attributes to show colour
    ; Attribute memory is at $5800 (768 bytes for 32×24 cells)
    ld hl, $5800        ; Attribute memory
    ld b, 24            ; 24 rows

attr_row:
    push bc
    ld b, 32            ; 32 columns per row

attr_col:
    ; Create attribute: INK 7 (white), PAPER 1 (blue)
    ld a, %00001111     ; PAPER 1 (001), INK 7 (111)
    ld (hl), a
    inc hl
    djnz attr_col

    pop bc
    djnz attr_row

    ; Wait for a key
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key

    ret

; Clear screen - fills display with zeros
clear_screen:
    ld hl, $4000        ; Screen start
    ld de, $4001        ; Destination = start + 1
    ld bc, 6143         ; Count = 6144 - 1
    ld (hl), 0          ; Clear first byte
    ldir                ; Copy zero through entire screen

    ; Also clear attributes to black on black
    ld hl, $5800
    ld de, $5801
    ld bc, 767
    ld (hl), 0
    ldir
    ret

    end start
