; Unit 5: Attribute Memory
; Demonstrates the location and mapping of attribute memory
;
; Attribute memory: $5800-$5AFF (768 bytes)
; Maps to 32 columns × 24 rows = 768 character cells
; Each cell is 8×8 pixels

    org 32768

start:
    ; Fill screen with checkerboard pattern
    ; This makes attribute colours visible
    call fill_pattern

    ; Set border to black
    ld a, 0
    out ($fe), a

    ; Now set attributes to show the mapping
    ; Each row gets a different colour combination

    ld hl, $5800        ; Attribute memory start
    ld b, 24            ; 24 rows

row_loop:
    push bc
    push hl

    ; Calculate attribute value based on row
    ; Row number (24-B) determines the colour
    ld a, 24
    sub b               ; A = row number (0-23)
    and %00000111       ; Keep low 3 bits for INK (0-7)
    ld c, a             ; Save INK

    ld a, 24
    sub b
    rrca                ; Shift to get different PAPER
    rrca
    rrca
    and %00111000       ; PAPER bits
    or c                ; Combine INK and PAPER
    ld c, a             ; C = attribute byte

    ; Fill this row with the attribute
    pop hl
    ld b, 32            ; 32 columns per row
col_loop:
    ld (hl), c
    inc hl
    djnz col_loop

    pop bc
    djnz row_loop

    ; Wait for keypress
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

; Fill screen with checkerboard pattern
; Makes attribute colours visible
fill_pattern:
    ld hl, $4000
    ld bc, 6144

fill_loop:
    ld a, h             ; Use address for pattern
    xor l
    and $55             ; Checkerboard
    ld (hl), a
    inc hl
    dec bc
    ld a, b
    or c
    jr nz, fill_loop
    ret

    end start
