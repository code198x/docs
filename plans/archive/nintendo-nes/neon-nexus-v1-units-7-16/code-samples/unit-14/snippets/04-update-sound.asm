;──────────────────────────────────────────────────────────────
; UPDATE SOUND
;──────────────────────────────────────────────────────────────
; Called each frame to update active sound effects.

.proc update_sound
    lda sfx_timer
    beq @done               ; No sound playing

    dec sfx_timer
    beq @silence            ; Timer just hit zero

    ; Modify pitch based on sound type
    lda sfx_type
    cmp #SFX_COLLECT
    beq @update_collect
    cmp #SFX_HIT
    beq @update_hit
    rts

@update_collect:
    ; Raise pitch every 4 frames
    lda sfx_timer
    and #%00000011
    bne @done
    lda APU_PULSE1_LO
    sec
    sbc #$20                ; Decrease period = higher pitch
    sta APU_PULSE1_LO
    rts

@update_hit:
    ; Lower pitch every 4 frames
    lda sfx_timer
    and #%00000011
    bne @done
    lda APU_PULSE1_LO
    clc
    adc #$30                ; Increase period = lower pitch
    sta APU_PULSE1_LO
    rts

@silence:
    lda #%00110000          ; Volume 0
    sta APU_PULSE1_CTRL
    lda #SFX_NONE
    sta sfx_type

@done:
    rts
.endproc
