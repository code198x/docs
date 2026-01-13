;──────────────────────────────────────────────────────────────
; TILE 1: Player Ship (pointing up)
;──────────────────────────────────────────────────────────────
; A simple arrow/ship shape. Uses colour 1 only.
;
;   . . . X X . . .     ($18)
;   . . X X X X . .     ($3C)
;   . X X X X X X .     ($7E)
;   X X X X X X X X     ($FF)
;   X X X X X X X X     ($FF)
;   . . X . . X . .     ($24)
;   . . X . . X . .     ($24)
;   . X X . . X X .     ($66)

    ; Low plane (colour bit 0)
    .byte %00011000         ; row 0
    .byte %00111100         ; row 1
    .byte %01111110         ; row 2
    .byte %11111111         ; row 3
    .byte %11111111         ; row 4
    .byte %00100100         ; row 5
    .byte %00100100         ; row 6
    .byte %01100110         ; row 7

    ; High plane (colour bit 1) - all zeros = colour 1 only
    .byte $00, $00, $00, $00, $00, $00, $00, $00
