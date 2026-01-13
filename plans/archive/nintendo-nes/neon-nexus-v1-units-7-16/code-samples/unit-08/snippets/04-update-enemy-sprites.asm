;──────────────────────────────────────────────────────────────
; UPDATE ENEMY SPRITES
;──────────────────────────────────────────────────────────────
; Copy enemy positions to shadow OAM.
; Uses indexed addressing to loop through all enemies.

.proc update_enemy_sprites
    ldx #0                  ; Enemy index (0-3)
    ldy #4                  ; OAM offset (sprite 1 starts at byte 4)

@loop:
    ; Byte 0: Y position
    lda enemy_y, x
    sta $0200, y
    iny

    ; Byte 1: Tile index (tile 2 = enemy)
    lda #2
    sta $0200, y
    iny

    ; Byte 2: Attributes (palette 1 = green enemies)
    lda #%00000001
    sta $0200, y
    iny

    ; Byte 3: X position
    lda enemy_x, x
    sta $0200, y
    iny

    inx
    cpx #NUM_ENEMIES
    bne @loop

    rts
.endproc

; After this routine, sprites 1-4 display the 4 enemies.
; Sprite 0 is still the player.
