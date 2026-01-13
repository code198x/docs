;──────────────────────────────────────────────────────────────
; ENABLE NMI
;──────────────────────────────────────────────────────────────
; After PPU warmup, we enable NMI by setting bit 7 of PPUCTRL.
; The NMI will now fire at the start of every VBlank period.

    lda #%10000000          ; Bit 7 = NMI enable
    sta PPUCTRL

; PPUCTRL bit layout:
; 7: NMI enable (1 = generate NMI at VBlank)
; 6: PPU master/slave (usually 0)
; 5: Sprite size (0 = 8x8, 1 = 8x16)
; 4: Background pattern table (0 = $0000, 1 = $1000)
; 3: Sprite pattern table (0 = $0000, 1 = $1000)
; 2: VRAM address increment (0 = +1, 1 = +32)
; 1-0: Base nametable address (00=$2000, 01=$2400, 10=$2800, 11=$2C00)
