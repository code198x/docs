;──────────────────────────────────────────────────────────────
; NMI HANDLER
;──────────────────────────────────────────────────────────────
; The NMI fires at the start of VBlank - approximately every
; 16.67ms on NTSC (60 Hz) or 20ms on PAL (50 Hz).
;
; VBlank is the ONLY safe time to write to PPU memory.
; We have about 2273 CPU cycles before rendering begins again.

.proc nmi
    ; Preserve registers on the stack
    ; We must restore them before returning, or we'll corrupt
    ; whatever the main loop was doing.
    pha                     ; Push A
    txa
    pha                     ; Push X
    tya
    pha                     ; Push Y

    ;----------------------------------------------------------
    ; VBlank tasks would go here:
    ; - Write to PPUADDR/PPUDATA (palettes, nametable)
    ; - Trigger OAM DMA
    ; - Update scroll position
    ;----------------------------------------------------------

    ; Increment frame counter
    inc frame_counter

    ; Signal main loop that VBlank has occurred
    lda #$01
    sta nmi_ready

    ; Restore registers
    pla
    tay                     ; Restore Y
    pla
    tax                     ; Restore X
    pla                     ; Restore A

    rti                     ; Return from interrupt
.endproc
