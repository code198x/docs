;──────────────────────────────────────────────────────────────
; SCORE DIRTY FLAG
;──────────────────────────────────────────────────────────────
; Track when the score needs to be redrawn on screen.

.segment "ZEROPAGE"

score_dirty:    .res 1      ; Flag: 1 = needs redraw

; We can't write to the nametable anytime — only during VBlank.
; Setting a "dirty" flag tells the NMI handler to update the
; display next frame.

; Set the flag when score changes:
.proc collect_item
    inc score
    lda #1
    sta score_dirty         ; Mark for redraw
    ; ...
.endproc

; This is a common pattern in NES games:
; - Game logic sets flags during the frame
; - NMI handler processes flags during VBlank
; - Separates "when to update" from "what to update"
