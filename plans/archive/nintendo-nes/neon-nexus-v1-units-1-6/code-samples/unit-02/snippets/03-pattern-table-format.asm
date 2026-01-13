;──────────────────────────────────────────────────────────────
; PATTERN TABLE FORMAT
;──────────────────────────────────────────────────────────────
; Each tile is 8×8 pixels, stored as two bit planes.
; 16 bytes per tile: 8 bytes low plane + 8 bytes high plane.
;
; Example: A simple arrow tile
;
;    Pixel pattern:        Bit plane 0:    Bit plane 1:
;
;    . . . X . . . .       $08             $00
;    . . . X X . . .       $0C             $00
;    . . . X X X . .       $0E             $00
;    X X X X X X X .       $FE             $00
;    X X X X X X X .       $FE             $00
;    . . . X X X . .       $0E             $00
;    . . . X X . . .       $0C             $00
;    . . . X . . . .       $08             $00
;
; Colour value = (high bit × 2) + low bit
; 0 = transparent, 1-3 = colours from palette

arrow_tile:
    ; Low bit plane (determines colour bit 0)
    .byte %00001000         ; ...X....
    .byte %00001100         ; ...XX...
    .byte %00001110         ; ...XXX..
    .byte %11111110         ; XXXXXXX.
    .byte %11111110         ; XXXXXXX.
    .byte %00001110         ; ...XXX..
    .byte %00001100         ; ...XX...
    .byte %00001000         ; ...X....

    ; High bit plane (determines colour bit 1)
    .byte $00, $00, $00, $00, $00, $00, $00, $00
