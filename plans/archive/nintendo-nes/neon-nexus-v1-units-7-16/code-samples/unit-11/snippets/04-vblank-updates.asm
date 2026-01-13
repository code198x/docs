;──────────────────────────────────────────────────────────────
; VBLANK NAMETABLE UPDATES
;──────────────────────────────────────────────────────────────
; The PPU is only safe to update during VBlank. The NMI fires
; at the start of VBlank, giving us limited time.

.proc nmi
    pha
    txa
    pha
    tya
    pha

    inc frame_counter

    ; Sprite DMA - always do this first
    lda #$00
    sta OAMADDR
    lda #$02
    sta OAMDMA

    ; Update score display during VBlank
    jsr update_score_display

    ; Reset scroll position
    lda #$00
    sta PPUSCROLL
    sta PPUSCROLL

    lda #$01
    sta nmi_ready

    pla
    tay
    pla
    tax
    pla
    rti
.endproc

; VBlank gives us about 2270 CPU cycles.
; OAM DMA uses 513 cycles.
; Remaining time: ~1750 cycles for nametable updates.
; Writing 3 digits: ~150 cycles. Plenty of headroom.
