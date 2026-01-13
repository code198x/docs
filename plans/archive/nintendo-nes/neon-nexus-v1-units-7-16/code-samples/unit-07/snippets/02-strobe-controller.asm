;──────────────────────────────────────────────────────────────
; STROBE THE CONTROLLER
;──────────────────────────────────────────────────────────────
; The strobe latches the current button state inside the controller.
; Without this, the buttons would continuously shift.

    lda #$01
    sta JOYPAD1             ; Write 1 to begin strobe

    lda #$00
    sta JOYPAD1             ; Write 0 to latch button state

; After this, the controller is ready to be read.
; Each read from JOYPAD1 returns the next button's state in bit 0.
