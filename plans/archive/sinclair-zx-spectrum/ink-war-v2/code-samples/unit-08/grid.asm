; Unit 8: The 32×24 Grid
; Visualises the complete attribute grid
; Shows how Ink War's 8×8 board maps to screen coordinates

    org 32768

start:
    call clear_screen
    call fill_pattern

    ; Set border to black
    ld a, 0
    out ($fe), a

    ; Draw the complete 32×24 grid
    ; Each cell gets a colour based on its position
    ; This shows the mapping from coordinates to screen

    ld hl, $5800        ; Start of attributes
    ld d, 0             ; Row counter

row_loop:
    ld e, 0             ; Column counter

col_loop:
    ; Calculate colour based on position
    ; Creates a gradient effect showing coordinates

    ld a, d             ; Row (0-23)
    and %00000111       ; Keep low 3 bits for PAPER
    rlca
    rlca
    rlca                ; Shift to PAPER position
    ld b, a             ; Save PAPER

    ld a, e             ; Column (0-31)
    and %00000111       ; Keep low 3 bits for INK
    or b                ; Combine PAPER and INK
    ld (hl), a          ; Store attribute
    inc hl

    inc e
    ld a, e
    cp 32               ; 32 columns?
    jr nz, col_loop

    inc d
    ld a, d
    cp 24               ; 24 rows?
    jr nz, row_loop

    ; Now overlay the Ink War board position
    ; 8×8 board centred on screen (rows 8-15, cols 12-19)

    ; Draw board outline by making border cells brighter
    ; Top border
    ld b, 7             ; Row 7 (above board)
    ld c, 11            ; Start column
border_top:
    call highlight_cell
    inc c
    ld a, c
    cp 21               ; End column + 1
    jr nz, border_top

    ; Bottom border
    ld b, 16            ; Row 16 (below board)
    ld c, 11
border_bottom:
    call highlight_cell
    inc c
    ld a, c
    cp 21
    jr nz, border_bottom

    ; Left border
    ld b, 7
    ld c, 11
border_left:
    call highlight_cell
    inc b
    ld a, b
    cp 17
    jr nz, border_left

    ; Right border
    ld b, 7
    ld c, 20
border_right:
    call highlight_cell
    inc b
    ld a, b
    cp 17
    jr nz, border_right

    ; Wait for keypress
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

; Highlight a cell by adding BRIGHT
highlight_cell:
    push bc
    call get_attr_addr  ; HL = attribute address
    ld a, (hl)
    or %01000000        ; Set BRIGHT bit
    ld (hl), a
    pop bc
    ret

; Get attribute address
get_attr_addr:
    ld h, $58
    ld a, b
    add a, a
    add a, a
    add a, a
    add a, a
    add a, a
    add a, c
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

; Fill with solid pixels
fill_pattern:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), $ff
    ldir
    ret

    end start
