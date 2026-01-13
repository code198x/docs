;──────────────────────────────────────────────────────────────
; BINARY TO DECIMAL CONVERSION
;──────────────────────────────────────────────────────────────
; The score is a binary number (0-255), but we display decimal
; digits. We need to extract hundreds, tens, and ones.

.proc update_score_display
    lda score               ; Binary value (e.g., 123)

    ; Extract hundreds digit
    ldx #0
@hundreds:
    cmp #100
    bcc @tens_setup         ; Less than 100? Done with hundreds
    sec
    sbc #100                ; Subtract 100
    inx                     ; Count how many times
    jmp @hundreds
@tens_setup:
    pha                     ; Save remainder (23 in example)
    txa                     ; X = hundreds digit (1)
    clc
    adc #TILE_DIGIT_0       ; Convert to tile index
    sta PPUDATA             ; Write to nametable

    pla                     ; Restore remainder

    ; Extract tens digit (same technique)
    ldx #0
@tens:
    cmp #10
    bcc @ones_setup
    sec
    sbc #10
    inx
    jmp @tens
@ones_setup:
    ; ... similar pattern for tens and ones
.endproc

; This repeated subtraction is slower than lookup tables
; but uses less ROM and is easy to understand.
