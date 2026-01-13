;──────────────────────────────────────────────────────────────
; iNES HEADER
;──────────────────────────────────────────────────────────────
; Every NES ROM starts with a 16-byte header that tells the
; emulator (or hardware) about the cartridge configuration.

.segment "HEADER"
    .byte "NES", $1A        ; Magic number - identifies this as NES ROM
    .byte 2                 ; PRG-ROM size: 2 × 16KB = 32KB
    .byte 1                 ; CHR-ROM size: 1 × 8KB = 8KB
    .byte $01               ; Flags 6: Vertical mirroring, no battery, no trainer
    .byte $00               ; Flags 7: Mapper 0 (NROM)
    .byte 0, 0, 0, 0        ; Flags 8-11: Unused (set to zero)
    .byte 0, 0, 0, 0        ; Flags 12-15: Unused (set to zero)
