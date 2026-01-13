;──────────────────────────────────────────────────────────────
; COLLECT ITEM
;──────────────────────────────────────────────────────────────
; Add to score and respawn the item at a new position.

.proc collect_item
    ; Increment score
    inc score

    ; Respawn item at new position
    ; Simple pseudo-random: use frame counter
    lda frame_counter
    asl a                   ; Multiply by 4
    asl a
    clc
    adc #32                 ; Range 32-224
    cmp #224
    bcc @x_ok
    lda #180                ; Fallback if too high
@x_ok:
    sta item_x

    lda frame_counter
    eor score               ; Mix in score for variation
    and #%01111111          ; 0-127
    clc
    adc #32                 ; Range 32-159
    sta item_y

    rts
.endproc

; The "random" position uses the frame counter.
; Since collection depends on player timing, this creates
; unpredictable placement without a true random number generator.
