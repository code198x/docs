;──────────────────────────────────────────────────────────────
; ENEMY TILE GRAPHICS
;──────────────────────────────────────────────────────────────
; An invader-style enemy sprite in CHR-ROM.

; Tile 2: Enemy (invader-style)
    .byte %01100110        ; . X X . . X X .
    .byte %11111111        ; X X X X X X X X
    .byte %11011011        ; X X . X X . X X
    .byte %11111111        ; X X X X X X X X
    .byte %01111110        ; . X X X X X X .
    .byte %00100100        ; . . X . . X . .
    .byte %01000010        ; . X . . . . X .
    .byte %10000001        ; X . . . . . . X
    ; High plane (all zeros = colour 1)
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; The design has a classic Space Invaders feel:
; - Arms reaching outward
; - Central body mass
; - "Legs" at the bottom
