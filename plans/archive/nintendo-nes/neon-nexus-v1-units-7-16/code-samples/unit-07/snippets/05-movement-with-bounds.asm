;──────────────────────────────────────────────────────────────
; MOVEMENT WITH BOUNDARY CHECKING
;──────────────────────────────────────────────────────────────
; Check each direction and keep the player within the border.

.proc update_player
    ; Check UP
    lda buttons
    and #BTN_UP
    beq @check_down
    lda player_y
    cmp #9                  ; Border at 8 pixels
    bcc @check_down         ; Branch if carry clear (y < 9)
    dec player_y            ; Move up

@check_down:
    lda buttons
    and #BTN_DOWN
    beq @check_left
    lda player_y
    cmp #223                ; Bottom boundary
    bcs @check_left         ; Branch if carry set (y >= 223)
    inc player_y            ; Move down

@check_left:
    lda buttons
    and #BTN_LEFT
    beq @check_right
    lda player_x
    cmp #9
    bcc @check_right
    dec player_x

@check_right:
    lda buttons
    and #BTN_RIGHT
    beq @done
    lda player_x
    cmp #239
    bcs @done
    inc player_x

@done:
    ; Update sprite position in shadow OAM
    lda player_y
    sta $0200               ; Sprite Y
    lda player_x
    sta $0203               ; Sprite X
    rts
.endproc
