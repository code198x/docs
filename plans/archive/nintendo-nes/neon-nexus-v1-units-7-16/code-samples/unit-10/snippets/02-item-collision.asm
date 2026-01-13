;──────────────────────────────────────────────────────────────
; CHECK ITEM COLLISION
;──────────────────────────────────────────────────────────────
; Test if player overlaps the collectible item.
; Uses the same bounding box technique as enemy collision.

.proc check_item_collision
    ; Check X distance
    lda player_x
    sec
    sbc item_x
    bcs @x_pos
    eor #$FF                ; Negate if negative
    clc
    adc #1
@x_pos:
    cmp #ITEM_HITBOX
    bcs @no_collision       ; X too far

    ; Check Y distance
    lda player_y
    sec
    sbc item_y
    bcs @y_pos
    eor #$FF
    clc
    adc #1
@y_pos:
    cmp #ITEM_HITBOX
    bcs @no_collision       ; Y too far

    ; Collision! Collect the item
    jsr collect_item

@no_collision:
    rts
.endproc

; Unlike enemy collision, we don't exit early.
; We call collect_item and continue - no game over here!
