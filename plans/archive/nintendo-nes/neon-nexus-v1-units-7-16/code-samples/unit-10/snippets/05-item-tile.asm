;──────────────────────────────────────────────────────────────
; ITEM TILE (CHR-ROM)
;──────────────────────────────────────────────────────────────
; A diamond shape makes the item visually distinct from
; the player ship and enemy sprites.

.segment "CHARS"

; Tile 4: Item (diamond shape)
    .byte %00011000
    .byte %00111100
    .byte %01111110
    .byte %11111111
    .byte %11111111
    .byte %01111110
    .byte %00111100
    .byte %00011000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Palette setup (from palette_data):
;   Palette 2: $0F, $2A, $1A, $0A (green shades)
;
; The diamond reads as "collectible" at a glance.
; Green colour contrasts with:
;   - White/blue player (palette 0)
;   - Red enemies (palette 1)
