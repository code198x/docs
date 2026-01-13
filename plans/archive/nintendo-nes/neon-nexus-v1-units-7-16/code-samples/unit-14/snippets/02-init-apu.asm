;──────────────────────────────────────────────────────────────
; APU INITIALISATION
;──────────────────────────────────────────────────────────────
; Enable pulse channel 1 and set it to silence.

.proc init_apu
    ; Enable pulse channel 1
    lda #%00000001
    sta APU_STATUS

    ; Set up pulse 1: silence initially
    lda #%00110000          ; Duty 50%, disable length, volume 0
    sta APU_PULSE1_CTRL
    lda #$00
    sta APU_PULSE1_SWEEP    ; Disable sweep
    sta APU_PULSE1_LO
    sta APU_PULSE1_HI

    rts
.endproc

; We only enable pulse channel 1 for now.
; Setting volume to 0 in CTRL silences the channel
; until we're ready to play a sound.
