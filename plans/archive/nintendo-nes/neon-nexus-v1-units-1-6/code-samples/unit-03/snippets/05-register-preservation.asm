;──────────────────────────────────────────────────────────────
; REGISTER PRESERVATION
;──────────────────────────────────────────────────────────────
; Interrupts can fire at ANY time during the main loop.
; If the NMI modifies A, X, or Y, it could corrupt the main
; loop's calculations.
;
; Solution: Save registers at the start, restore at the end.

; At the START of the NMI handler:
    pha                     ; Push A onto stack
    txa                     ; Copy X to A
    pha                     ; Push X (via A) onto stack
    tya                     ; Copy Y to A
    pha                     ; Push Y (via A) onto stack

; Stack now contains (from top): Y, X, A, return address

; ... do NMI work here ...

; At the END of the NMI handler:
    pla                     ; Pop Y (into A)
    tay                     ; Restore Y from A
    pla                     ; Pop X (into A)
    tax                     ; Restore X from A
    pla                     ; Pop A

; The 6502 has no "push X" or "push Y" instructions,
; so we transfer through A first. Order matters:
; First in, last out. Push A-X-Y, pop Y-X-A.
