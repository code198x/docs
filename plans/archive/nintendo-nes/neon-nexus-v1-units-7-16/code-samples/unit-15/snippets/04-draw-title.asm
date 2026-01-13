;──────────────────────────────────────────────────────────────
; DRAW TITLE SCREEN
;──────────────────────────────────────────────────────────────
; Clear screen and draw title text.

.proc draw_title_screen
    ; Hide all sprites
    ldx #0
    lda #$FF
@hide_sprites:
    sta $0200, x
    inx
    bne @hide_sprites

    ; Clear nametable
    jsr clear_nametable

    ; Draw "NEON" at row 10, centred
    bit PPUSTATUS
    lda #$21
    sta PPUADDR
    lda #$4E                ; Row 10, column 14
    sta PPUADDR

    lda #TILE_N
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA
    lda #TILE_O
    sta PPUDATA
    lda #TILE_N
    sta PPUDATA

    ; Draw "NEXUS" at row 12
    ; ... similar pattern ...

    ; Draw "PRESS START" at row 18
    ; ... similar pattern ...

    lda #$00
    sta PPUSCROLL
    sta PPUSCROLL

    rts
.endproc
