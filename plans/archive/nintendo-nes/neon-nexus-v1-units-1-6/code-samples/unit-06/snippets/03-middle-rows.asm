;──────────────────────────────────────────────────────────────
; FILLING MIDDLE ROWS WITH BORDER
;──────────────────────────────────────────────────────────────
; For each middle row: 1 border tile, 30 empty, 1 border tile.
; This creates a frame around the play area.

    ldy #28                 ; 28 middle rows (rows 1-28)
@row_loop:
    ; Left border tile
    lda #2                  ; Solid block
    sta PPUDATA

    ; 30 empty tiles
    ldx #30
@empty_loop:
    lda #0                  ; Empty tile (transparent)
    sta PPUDATA
    dex
    bne @empty_loop

    ; Right border tile
    lda #2
    sta PPUDATA

    dey
    bne @row_loop

; Each iteration writes exactly 32 tiles (1 + 30 + 1).
; After 28 iterations, we've filled rows 1-28.
