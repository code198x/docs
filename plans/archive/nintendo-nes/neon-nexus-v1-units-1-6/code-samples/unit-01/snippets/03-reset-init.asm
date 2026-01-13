;──────────────────────────────────────────────────────────────
; RESET HANDLER - Initial Setup
;──────────────────────────────────────────────────────────────
; The first instructions that run when the NES powers on.

.proc reset
    ; Disable interrupts during setup
    sei                     ; Set Interrupt Disable flag

    ; Clear decimal mode (6502 has it, but NES doesn't use it)
    cld                     ; Clear Decimal flag

    ; Disable APU frame counter IRQ
    ldx #$40
    stx $4017

    ; Set up the stack
    ldx #$FF
    txs                     ; Stack pointer = $FF (stack at $01FF)

    ; Disable PPU rendering and NMI
    inx                     ; X = 0
    stx PPUCTRL             ; Disable NMI
    stx PPUMASK             ; Disable rendering
    stx $4010               ; Disable DMC IRQs
