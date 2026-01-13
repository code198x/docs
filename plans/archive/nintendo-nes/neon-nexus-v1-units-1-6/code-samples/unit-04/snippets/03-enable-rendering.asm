;──────────────────────────────────────────────────────────────
; ENABLE RENDERING
;──────────────────────────────────────────────────────────────
; Now we enable both NMI and background rendering.
; The PPU will display the background colour from $3F00.

    lda #%10000000          ; Bit 7 = NMI enable
    sta PPUCTRL

    lda #%00001010          ; Bit 3 = show background
                            ; Bit 1 = show background in leftmost 8 pixels
    sta PPUMASK

; PPUMASK bit layout:
; 7: Emphasise blue
; 6: Emphasise green
; 5: Emphasise red
; 4: Show sprites
; 3: Show background
; 2: Show sprites in leftmost 8 pixels
; 1: Show background in leftmost 8 pixels
; 0: Greyscale mode
