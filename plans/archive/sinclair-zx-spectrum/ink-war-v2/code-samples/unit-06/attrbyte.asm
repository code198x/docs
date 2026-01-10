; Unit 6: Attribute Byte Structure
; Demonstrates INK, PAPER, BRIGHT, and FLASH bits
;
; Attribute byte format: FBPPPIII
;   F   = FLASH  (bit 7) - alternates INK/PAPER
;   B   = BRIGHT (bit 6) - increases intensity
;   PPP = PAPER  (bits 5-3) - background colour 0-7
;   III = INK    (bits 2-0) - foreground colour 0-7

    org 32768

start:
    ; Fill screen with pattern to show colours
    call fill_pattern

    ; Set border to black
    ld a, 0
    out ($fe), a

    ; Create a colour chart showing all combinations
    ; Top half: Normal colours (BRIGHT=0)
    ; Bottom half: Bright colours (BRIGHT=1)

    ; First, fill top 12 rows with normal colours
    ; Each row shows one PAPER colour, columns show INK
    ld hl, $5800        ; Attribute start
    ld b, 8             ; 8 PAPER colours
    ld d, 0             ; PAPER counter

paper_loop_normal:
    push bc
    push de

    ; Fill one row with all INK colours on this PAPER
    ld a, d             ; A = PAPER value
    rlca                ; Shift to bits 5-3
    rlca
    rlca
    ld e, a             ; E = PAPER in position

    ld b, 32            ; 32 columns
    ld c, 0             ; INK counter (wraps at 8)

ink_loop_normal:
    ld a, e             ; PAPER bits
    or c                ; Add INK bits
    ld (hl), a          ; Store attribute
    inc hl
    inc c
    ld a, c
    and %00000111       ; Wrap INK 0-7
    ld c, a
    djnz ink_loop_normal

    pop de
    inc d               ; Next PAPER colour
    pop bc
    djnz paper_loop_normal

    ; Now fill bottom 8 rows with BRIGHT versions
    ld b, 8
    ld d, 0

paper_loop_bright:
    push bc
    push de

    ld a, d
    rlca
    rlca
    rlca
    or %01000000        ; Set BRIGHT bit
    ld e, a

    ld b, 32
    ld c, 0

ink_loop_bright:
    ld a, e
    or c
    ld (hl), a
    inc hl
    inc c
    ld a, c
    and %00000111
    ld c, a
    djnz ink_loop_bright

    pop de
    inc d
    pop bc
    djnz paper_loop_bright

    ; Fill remaining rows with FLASH examples
    ; Last 8 rows: FLASH + various colours
    ld b, 8
    ld d, 0

flash_loop:
    push bc
    push de

    ld a, d
    rlca
    rlca
    rlca
    or %10000000        ; Set FLASH bit
    or d                ; INK = PAPER number for contrast
    xor %00000111       ; Invert INK for visibility
    ld e, a

    ld b, 32

flash_fill:
    ld (hl), e
    inc hl
    djnz flash_fill

    pop de
    inc d
    pop bc
    djnz flash_loop

    ; Wait for keypress
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

; Fill screen with solid blocks
fill_pattern:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), $ff        ; Solid pixels
    ldir
    ret

    end start
