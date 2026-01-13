;──────────────────────────────────────────────────────────────
; READ ALL BUTTONS
;──────────────────────────────────────────────────────────────
; Read 8 buttons into a single byte.
; Uses LSR to get bit 0 into carry, then ROL to shift it into 'buttons'.

.proc read_controller
    ; Strobe the controller
    lda #$01
    sta JOYPAD1
    lda #$00
    sta JOYPAD1

    ; Read 8 buttons
    ldx #8
@loop:
    lda JOYPAD1             ; Read button (bit 0 = pressed)
    lsr a                   ; Shift bit 0 into carry
    rol buttons             ; Roll carry into buttons variable
    dex
    bne @loop

    rts
.endproc

; After this routine:
;   - Bit 0 set = A pressed
;   - Bit 1 set = B pressed
;   - ...
;   - Bit 7 set = Right pressed
