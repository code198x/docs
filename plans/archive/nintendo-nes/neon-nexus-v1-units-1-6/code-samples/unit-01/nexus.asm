;──────────────────────────────────────────────────────────────
; NEON NEXUS
; Unit 1: NES Architecture
;──────────────────────────────────────────────────────────────
; Our first NES program. This minimal code demonstrates:
; - The iNES header format
; - CPU initialisation sequence
; - Vector table setup
; - The infinite main loop
;
; What you'll see: A blank screen. But the NES is running YOUR
; code - the first step on the journey to building a full game.
;──────────────────────────────────────────────────────────────

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

;──────────────────────────────────────────────────────────────
; PPU REGISTER DEFINITIONS
;──────────────────────────────────────────────────────────────
; The PPU (Picture Processing Unit) is controlled through
; memory-mapped registers at $2000-$2007.

.segment "CODE"

PPUCTRL   = $2000           ; PPU control register
PPUMASK   = $2001           ; PPU mask register (rendering control)
PPUSTATUS = $2002           ; PPU status register

;──────────────────────────────────────────────────────────────
; RESET HANDLER
;──────────────────────────────────────────────────────────────
; This code runs when the NES powers on or is reset.
; It performs the essential initialisation sequence.

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

    ; Wait for first VBlank
    ; The PPU needs time to warm up after power-on
@vblank_wait_1:
    bit PPUSTATUS           ; Read PPU status
    bpl @vblank_wait_1      ; Loop until bit 7 (VBlank) is set

    ; Clear RAM while waiting for second VBlank
    ; This ensures we start with a clean state
    lda #$00
@clear_ram:
    sta $0000, x
    sta $0100, x
    sta $0200, x
    sta $0300, x
    sta $0400, x
    sta $0500, x
    sta $0600, x
    sta $0700, x
    inx
    bne @clear_ram

    ; Wait for second VBlank
    ; After this, the PPU is fully ready
@vblank_wait_2:
    bit PPUSTATUS
    bpl @vblank_wait_2

    ; ────────────────────────────────────────────────────────
    ; THE MAIN LOOP
    ; ────────────────────────────────────────────────────────
    ; For now, we just loop forever. The screen stays blank
    ; because we haven't enabled rendering or set up graphics.
    ; This is still a working NES program!
forever:
    jmp forever             ; Loop forever
.endproc

;──────────────────────────────────────────────────────────────
; NMI HANDLER
;──────────────────────────────────────────────────────────────
; The NMI (Non-Maskable Interrupt) fires at the start of VBlank,
; 60 times per second on NTSC. For now, it does nothing.

.proc nmi
    rti                     ; Return from interrupt
.endproc

;──────────────────────────────────────────────────────────────
; IRQ HANDLER
;──────────────────────────────────────────────────────────────
; The IRQ handler for hardware interrupts. We don't use IRQs
; in this game, but we need a handler anyway.

.proc irq
    rti                     ; Return from interrupt
.endproc

;──────────────────────────────────────────────────────────────
; VECTOR TABLE
;──────────────────────────────────────────────────────────────
; The CPU looks at $FFFA-$FFFF to find interrupt handlers.
; These MUST be at the very end of the ROM.

.segment "VECTORS"
    .word nmi               ; $FFFA - NMI vector
    .word reset             ; $FFFC - Reset vector
    .word irq               ; $FFFE - IRQ vector

;──────────────────────────────────────────────────────────────
; CHARACTER DATA (CHR-ROM)
;──────────────────────────────────────────────────────────────
; The PPU's pattern tables. For now, just empty space.
; We'll add tile graphics in later units.

.segment "CHARS"
    .res 8192               ; 8KB of empty CHR data
