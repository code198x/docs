;──────────────────────────────────────────────────────────────
; PALETTE LAYOUT
;──────────────────────────────────────────────────────────────
; Palettes live at $3F00-$3F1F in PPU memory (32 bytes total).
;
; Background palettes:
;   $3F00: Universal background colour (shared by all)
;   $3F01-$3F03: Background palette 0 (3 colours)
;   $3F05-$3F07: Background palette 1 (3 colours)
;   $3F09-$3F0B: Background palette 2 (3 colours)
;   $3F0D-$3F0F: Background palette 3 (3 colours)
;
; Sprite palettes:
;   $3F10: Mirrors $3F00 (not usable)
;   $3F11-$3F13: Sprite palette 0 (3 colours)
;   $3F15-$3F17: Sprite palette 1 (3 colours)
;   $3F19-$3F1B: Sprite palette 2 (3 colours)
;   $3F1D-$3F1F: Sprite palette 3 (3 colours)
;
; Note: $3F04, $3F08, $3F0C, $3F14, $3F18, $3F1C mirror $3F00

palette_data:
    ; Background palettes (16 bytes)
    .byte $0F               ; $3F00: Black background
    .byte $21, $31, $30     ; Palette 0: Light blue, pale blue, white
    .byte $0F               ; $3F04: (mirrors $3F00)
    .byte $19, $29, $39     ; Palette 1: Greens
    .byte $0F               ; $3F08: (mirrors $3F00)
    .byte $15, $25, $35     ; Palette 2: Magentas
    .byte $0F               ; $3F0C: (mirrors $3F00)
    .byte $17, $27, $37     ; Palette 3: Oranges

    ; Sprite palettes (16 bytes)
    .byte $0F               ; $3F10: (mirrors $3F00)
    .byte $30, $21, $11     ; Palette 0: White to dark blue
    .byte $0F               ; $3F14: (mirrors $3F00)
    .byte $27, $17, $07     ; Palette 1: Orange gradient
    .byte $0F               ; $3F18: (mirrors $3F00)
    .byte $29, $19, $09     ; Palette 2: Green gradient
    .byte $0F               ; $3F1C: (mirrors $3F00)
    .byte $24, $14, $04     ; Palette 3: Purple gradient
