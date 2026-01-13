;──────────────────────────────────────────────────────────────
; DIGIT TILES
;──────────────────────────────────────────────────────────────
; CHR-ROM tiles for displaying numbers 0-9.
; Each digit is an 8x8 tile stored consecutively.

.segment "CHARS"

; Tiles 5-14: Digits 0-9
; Tile 5: Digit 0
    .byte %00111100
    .byte %01100110
    .byte %01101110
    .byte %01110110
    .byte %01100110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 6: Digit 1
    .byte %00011000
    .byte %00111000
    .byte %00011000
    .byte %00011000
    .byte %00011000
    .byte %00011000
    .byte %01111110
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; ... tiles 7-14 continue for digits 2-9

; To convert a number to a tile index:
TILE_DIGIT_0 = 5              ; First digit tile
; So digit N uses tile (TILE_DIGIT_0 + N)
