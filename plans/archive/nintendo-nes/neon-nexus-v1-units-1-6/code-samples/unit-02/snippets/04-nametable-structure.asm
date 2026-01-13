;──────────────────────────────────────────────────────────────
; NAMETABLE STRUCTURE
;──────────────────────────────────────────────────────────────
; The nametable defines which tile appears at each screen position.
; It's a 32×30 grid = 960 bytes, located at $2000 in PPU memory.
;
; Each byte is a tile index (0-255) into the pattern table.
;
; Memory layout:
;   $2000: Row 0, columns 0-31 (32 bytes)
;   $2020: Row 1, columns 0-31 (32 bytes)
;   $2040: Row 2, columns 0-31 (32 bytes)
;   ...
;   $23A0: Row 29, columns 0-31 (32 bytes)
;   $23C0: Attribute table starts here (64 bytes)
;
; Screen dimensions: 256×240 pixels = 32×30 tiles

; Example: Fill nametable with a single tile
fill_nametable:
    bit PPUSTATUS           ; Reset address latch
    lda #$20                ; High byte of $2000
    sta PPUADDR
    lda #$00                ; Low byte of $2000
    sta PPUADDR

    lda #$00                ; Tile index 0
    ldx #0
    ldy #4                  ; 4 × 256 = 1024 writes (960 + attribute)
@loop:
    sta PPUDATA             ; Write tile index
    inx
    bne @loop               ; Inner: 256 iterations
    dey
    bne @loop               ; Outer: 4 iterations
    rts
