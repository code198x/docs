;──────────────────────────────────────────────────────────────
; THE MAIN LOOP
;──────────────────────────────────────────────────────────────
; For now, we just loop forever. The screen stays blank
; because we haven't enabled rendering or set up graphics.
; This is still a working NES program!

forever:
    jmp forever             ; Loop forever
.endproc
