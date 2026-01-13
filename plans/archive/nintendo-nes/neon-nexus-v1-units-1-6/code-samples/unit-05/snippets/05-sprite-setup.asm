;──────────────────────────────────────────────────────────────
; SPRITE SETUP
;──────────────────────────────────────────────────────────────
; Shadow OAM at $0200-$02FF holds sprite data.
; Each sprite uses 4 bytes:
;   Byte 0: Y position (0-239)
;   Byte 1: Tile index (0-255)
;   Byte 2: Attributes (palette, flip, priority)
;   Byte 3: X position (0-255)

; Sprite 0: Display tile 1 (player ship) at centre screen
    lda #116                ; Y position (centre vertically)
    sta $0200
    lda #1                  ; Tile index 1 (player ship)
    sta $0201
    lda #%00000000          ; Attributes: palette 0, no flip
    sta $0202
    lda #124                ; X position (centre horizontally)
    sta $0203

; Attribute byte layout:
;   Bits 0-1: Palette number (0-3)
;   Bits 2-4: Unused
;   Bit 5:    Priority (0 = in front of background)
;   Bit 6:    Flip horizontally
;   Bit 7:    Flip vertically
