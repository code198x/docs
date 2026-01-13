;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 2: PPU Fundamentals
;──────────────────────────────────────────────────────────────

;==============================================================
; iNES HEADER
;==============================================================
; The 16-byte header that identifies the ROM format.

.segment "HEADER"
    .byte "NES", $1A        ; Magic number: "NES" + EOF
    .byte 2                 ; PRG-ROM: 2 × 16KB = 32KB
    .byte 1                 ; CHR-ROM: 1 × 8KB
    .byte $01               ; Flags 6: Mapper 0, vertical mirroring
    .byte $00               ; Flags 7: Mapper 0 (continued)
    .byte 0,0,0,0,0,0,0,0   ; Padding (8 bytes)

;==============================================================
; PPU REGISTER DEFINITIONS
;==============================================================
; The PPU has 8 memory-mapped registers at $2000-$2007.
; We define symbolic names to make the code readable.

.segment "CODE"

; Control and status
PPUCTRL   = $2000           ; PPU control register
PPUMASK   = $2001           ; PPU mask (rendering control)
PPUSTATUS = $2002           ; PPU status register

; OAM (sprite) access
OAMADDR   = $2003           ; OAM address
OAMDATA   = $2004           ; OAM data port

; Scrolling
PPUSCROLL = $2005           ; Scroll position

; VRAM access
PPUADDR   = $2006           ; VRAM address (write twice)
PPUDATA   = $2007           ; VRAM data port

; DMA register (not in PPU, but used for sprites)
OAMDMA    = $4014           ; OAM DMA transfer

;==============================================================
; PPU ADDRESS CONSTANTS
;==============================================================
; Key locations in the PPU's 16KB address space.

PPU_PATTERN_0   = $0000     ; Pattern table 0 (background tiles)
PPU_PATTERN_1   = $1000     ; Pattern table 1 (sprite tiles)
PPU_NAMETABLE_0 = $2000     ; Nametable 0 (screen layout)
PPU_NAMETABLE_1 = $2400     ; Nametable 1
PPU_ATTRIBUTE_0 = $23C0     ; Attribute table 0 (palette zones)
PPU_PALETTES    = $3F00     ; Palette data

;==============================================================
; RESET HANDLER
;==============================================================
; Entry point when the NES powers on or resets.

.proc reset
    sei                     ; Disable IRQs
    cld                     ; Clear decimal mode (not used on NES)

    ; Disable APU interrupts
    ldx #$40
    stx $4017               ; Disable APU frame IRQ

    ; Set up stack
    ldx #$FF
    txs                     ; Stack pointer = $FF (stack at $0100-$01FF)

    ; Disable PPU features during startup
    inx                     ; X = $00
    stx PPUCTRL             ; Disable NMI
    stx PPUMASK             ; Disable rendering
    stx $4010               ; Disable DMC IRQs

    ; First VBlank wait
    ; The PPU needs time to stabilise after power-on.
@vblank_wait_1:
    bit PPUSTATUS           ; Read status (bit 7 = VBlank flag)
    bpl @vblank_wait_1      ; Loop until bit 7 is set

    ; Clear all RAM while waiting for PPU
    lda #$00
@clear_ram:
    sta $0000, x            ; Zero page ($0000-$00FF)
    sta $0100, x            ; Stack area ($0100-$01FF)
    sta $0200, x            ; OAM buffer ($0200-$02FF)
    sta $0300, x            ; General RAM
    sta $0400, x
    sta $0500, x
    sta $0600, x
    sta $0700, x            ; Last page of RAM
    inx                     ; X goes 0→255
    bne @clear_ram          ; Loop until X wraps to 0

    ; Second VBlank wait
    ; After two VBlanks, the PPU is fully ready.
@vblank_wait_2:
    bit PPUSTATUS
    bpl @vblank_wait_2

    ; PPU is now ready, but we haven't:
    ; - Loaded any palettes
    ; - Written to the nametable
    ; - Defined any tile graphics
    ; - Enabled rendering
    ; So the screen remains blank.

;--------------------------------------------------------------
; MAIN LOOP
;--------------------------------------------------------------
; Nothing happens here yet - just an infinite loop.
; The screen stays blank because:
; 1. PPUMASK = 0 (rendering disabled)
; 2. No palette colours loaded
; 3. No tile graphics defined
; 4. No nametable data written

forever:
    jmp forever             ; Loop forever
.endproc

;==============================================================
; NMI HANDLER
;==============================================================
; Called at the start of VBlank (60 times/second on NTSC).
; VBlank is the only safe time to update PPU memory.
; For now, this does nothing.

.proc nmi
    rti                     ; Return from interrupt
.endproc

;==============================================================
; IRQ HANDLER
;==============================================================
; Hardware interrupt handler. Not used in this game.

.proc irq
    rti                     ; Return from interrupt
.endproc

;==============================================================
; VECTORS
;==============================================================
; The CPU reads these addresses to find interrupt handlers.

.segment "VECTORS"
    .word nmi               ; $FFFA - NMI vector
    .word reset             ; $FFFC - Reset vector
    .word irq               ; $FFFE - IRQ vector

;==============================================================
; CHARACTER DATA (CHR-ROM)
;==============================================================
; The PPU's pattern tables - tile graphics data.
; This is empty for now. We'll add tiles in Unit 5.

.segment "CHARS"
    .res 8192               ; 8KB of empty CHR data
