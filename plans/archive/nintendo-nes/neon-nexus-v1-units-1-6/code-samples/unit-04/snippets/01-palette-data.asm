;──────────────────────────────────────────────────────────────
; PALETTE DATA
;──────────────────────────────────────────────────────────────
; 32 bytes total: 16 for background, 16 for sprites.
;
; NES colour values (selected examples):
;   $0F = Black
;   $00 = Dark grey
;   $10 = Light grey
;   $30 = White
;   $11 = Dark blue
;   $21 = Medium blue
;   $31 = Light blue

palette_data:
    ; Background palettes (16 bytes)
    ; The first byte ($3F00) is the universal background colour.
    ; It's visible wherever no tile is drawn.

    .byte $01               ; Universal background: dark blue
    .byte $21, $31, $30     ; Palette 0: blues to white
    .byte $01               ; (mirrors $3F00)
    .byte $19, $29, $39     ; Palette 1: greens
    .byte $01               ; (mirrors $3F00)
    .byte $15, $25, $35     ; Palette 2: magentas
    .byte $01               ; (mirrors $3F00)
    .byte $00, $10, $30     ; Palette 3: greys

    ; Sprite palettes (16 bytes)
    ; Sprite colour 0 is always transparent.

    .byte $01               ; (mirrors $3F00)
    .byte $30, $21, $11     ; Palette 0: white to dark blue
    .byte $01               ; (mirrors $3F00)
    .byte $27, $17, $07     ; Palette 1: oranges
    .byte $01               ; (mirrors $3F00)
    .byte $29, $19, $09     ; Palette 2: greens
    .byte $01               ; (mirrors $3F00)
    .byte $24, $14, $04     ; Palette 3: purples
