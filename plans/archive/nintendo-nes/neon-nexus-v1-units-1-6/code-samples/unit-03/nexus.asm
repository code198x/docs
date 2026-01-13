;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 3: VBlank and NMI
;──────────────────────────────────────────────────────────────

;==============================================================
; iNES HEADER
;==============================================================

.segment "HEADER"
    .byte "NES", $1A        ; Magic number
    .byte 2                 ; PRG-ROM: 2 × 16KB = 32KB
    .byte 1                 ; CHR-ROM: 1 × 8KB
    .byte $01               ; Flags 6: Mapper 0, vertical mirroring
    .byte $00               ; Flags 7: Mapper 0 (continued)
    .byte 0,0,0,0,0,0,0,0   ; Padding

;==============================================================
; VARIABLES
;==============================================================
; Zero page is fast memory - use it for frequently accessed data.

.segment "ZEROPAGE"

nmi_ready:      .res 1      ; Set by NMI, cleared by main loop
frame_counter:  .res 1      ; Increments every frame (wraps at 256)

;==============================================================
; PPU REGISTER DEFINITIONS
;==============================================================

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

; DMA register
OAMDMA    = $4014           ; OAM DMA transfer

;==============================================================
; RESET HANDLER
;==============================================================

.proc reset
    sei                     ; Disable IRQs
    cld                     ; Clear decimal mode

    ; Disable APU interrupts
    ldx #$40
    stx $4017

    ; Set up stack
    ldx #$FF
    txs

    ; Disable PPU during startup
    inx                     ; X = $00
    stx PPUCTRL             ; Disable NMI
    stx PPUMASK             ; Disable rendering
    stx $4010               ; Disable DMC IRQs

    ; First VBlank wait
@vblank_wait_1:
    bit PPUSTATUS
    bpl @vblank_wait_1

    ; Clear RAM
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

    ; Second VBlank wait
@vblank_wait_2:
    bit PPUSTATUS
    bpl @vblank_wait_2

    ;----------------------------------------------------------
    ; PPU is ready. Now enable NMI.
    ;----------------------------------------------------------
    ; Setting bit 7 of PPUCTRL enables NMI generation.
    ; The NMI will fire at the start of every VBlank period.

    lda #%10000000          ; Bit 7 = NMI enable
    sta PPUCTRL

    ; Note: We still have PPUMASK = 0, so rendering is disabled.
    ; The screen stays blank, but NMIs are now firing.

;--------------------------------------------------------------
; MAIN LOOP
;--------------------------------------------------------------
; The main loop waits for VBlank (signalled by NMI), then runs
; game logic. This ensures we update the game 60 times per
; second (NTSC) in perfect sync with the display.

main_loop:
    ; Wait for NMI to set the ready flag
    lda #$00
    sta nmi_ready           ; Clear the flag

@wait_for_nmi:
    lda nmi_ready           ; Check flag
    beq @wait_for_nmi       ; Loop until NMI sets it

    ; NMI has fired - we're now in VBlank
    ; This is where we would:
    ; 1. Update PPU (palettes, nametable, etc.)
    ; 2. Transfer sprite data via DMA
    ; 3. Set scroll position
    ;
    ; After VBlank ends, we run game logic:
    ; - Read controller input
    ; - Update game state
    ; - Prepare data for next frame
    ;
    ; For now, we just loop - no game logic yet.

    jmp main_loop
.endproc

;==============================================================
; NMI HANDLER
;==============================================================
; The NMI fires at the start of VBlank - approximately every
; 16.67ms on NTSC (60 Hz) or 20ms on PAL (50 Hz).
;
; VBlank is the ONLY safe time to write to PPU memory.
; We have about 2273 CPU cycles before rendering begins again.

.proc nmi
    ; Preserve registers on the stack
    ; We must restore them before returning, or we'll corrupt
    ; whatever the main loop was doing.
    pha                     ; Push A
    txa
    pha                     ; Push X
    tya
    pha                     ; Push Y

    ;----------------------------------------------------------
    ; VBlank tasks would go here:
    ; - Write to PPUADDR/PPUDATA (palettes, nametable)
    ; - Trigger OAM DMA
    ; - Update scroll position
    ;----------------------------------------------------------

    ; Increment frame counter
    inc frame_counter

    ; Signal main loop that VBlank has occurred
    lda #$01
    sta nmi_ready

    ; Restore registers
    pla
    tay                     ; Restore Y
    pla
    tax                     ; Restore X
    pla                     ; Restore A

    rti                     ; Return from interrupt
.endproc

;==============================================================
; IRQ HANDLER
;==============================================================

.proc irq
    rti
.endproc

;==============================================================
; VECTORS
;==============================================================

.segment "VECTORS"
    .word nmi               ; $FFFA - NMI vector
    .word reset             ; $FFFC - Reset vector
    .word irq               ; $FFFE - IRQ vector

;==============================================================
; CHARACTER DATA (CHR-ROM)
;==============================================================

.segment "CHARS"
    .res 8192               ; 8KB of empty CHR data
