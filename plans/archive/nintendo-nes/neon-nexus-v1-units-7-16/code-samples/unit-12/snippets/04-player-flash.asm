;──────────────────────────────────────────────────────────────
; PLAYER SPRITE FLASH
;──────────────────────────────────────────────────────────────
; Visual feedback during invulnerability - player flashes.

.proc update_player_sprite
    lda invuln_timer
    beq @visible            ; Not invulnerable - always visible

    ; Flash every 4 frames using bit 2
    and #%00000100
    beq @hidden

@visible:
    lda player_y
    sta $0200
    lda #1
    sta $0201
    lda #%00000000
    sta $0202
    lda player_x
    sta $0203
    rts

@hidden:
    lda #$FF
    sta $0200               ; Y = 255 moves sprite off-screen
    rts
.endproc

; AND with %00000100 checks bit 2 of the timer.
; This bit changes every 4 frames: 0-3=off, 4-7=on, 8-11=off...
; The result is a visible flashing effect.
