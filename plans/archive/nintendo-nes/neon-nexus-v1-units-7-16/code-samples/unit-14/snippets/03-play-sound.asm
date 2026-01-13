;──────────────────────────────────────────────────────────────
; PLAY COLLECT SOUND
;──────────────────────────────────────────────────────────────
; Trigger a rising-pitch "ding" when collecting an item.

.proc play_collect_sound
    lda #SFX_COLLECT
    sta sfx_type
    lda #16                 ; Duration: 16 frames
    sta sfx_timer

    ; Start with low pitch, rising
    lda #%10111111          ; Duty 50%, volume 15
    sta APU_PULSE1_CTRL
    lda #$C0                ; Low pitch (high period value)
    sta APU_PULSE1_LO
    lda #%00001000          ; Length counter load
    sta APU_PULSE1_HI

    rts
.endproc

; The period value in APU_PULSE1_LO controls pitch.
; Lower values = higher pitch, higher values = lower pitch.
; We start at $C0 (low) and decrease to raise the pitch.
