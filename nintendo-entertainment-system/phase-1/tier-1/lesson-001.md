# Lesson 001: Minimal NES Program

**Arc:** Hello, NES
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** ~50 bytes of assembly code

## Learning Objectives

- Write your first 6502 assembly program for the NES
- Understand the iNES ROM file format
- Learn the basic structure of every NES program
- Display a solid color on the screen
- Experience the assembly toolchain (ca65, ld65)

## Prerequisites

**From Previous Lessons:**
None - this is the starting point for NES development

**Assembly Knowledge:**
- None required - first assembly program

**Tools Required:**
- ca65/ld65 assemblers (cc65 toolchain)
- Mesen or FCEUX emulator
- Text editor

## Key Concepts Introduced

### iNES ROM Format
NES programs are distributed as .nes ROM files. The file starts with a 16-byte header that tells the emulator (or console) how the cartridge is configured:
- How much program code (PRG-ROM)
- How much graphics data (CHR-ROM)
- Which mapper chip (0 = NROM, no mapper)
- Mirroring mode (horizontal or vertical)

### Reset Vector
When the NES powers on, the CPU reads address $FFFC-$FFFD to find where to start executing code. This is called the reset vector. Our program puts the address of our initialization code here.

### PPU Initialization
The Picture Processing Unit (PPU) is the graphics chip. After reset, we must wait for it to warm up (2 VBlank periods) before we can safely use it. We check bit 7 of $2002 (PPUSTATUS) to detect VBlank.

### Infinite Loop
Unlike BASIC programs that end with STOP, NES programs run forever. We use an infinite loop (`loop: jmp loop`) to prevent the CPU from executing random memory as code.

### Displaying a Color
The PPU's palette register ($3F00 in VRAM) controls the background color. We write a color value (0-63) to set what appears on screen.

## Code Pattern

```asm
; minimal.asm - Smallest working NES program

.segment "HEADER"
  .byte "NES", $1A      ; iNES magic signature
  .byte $02             ; 2 × 16KB PRG-ROM
  .byte $01             ; 1 × 8KB CHR-ROM
  .byte $00             ; Mapper 0 (NROM), horizontal mirroring
  .byte $00             ; No special features
  .res 8, $00           ; Padding to 16 bytes

.segment "VECTORS"
  .word 0               ; NMI vector (unused for now)
  .word Reset           ; Reset vector (start here on power-on)
  .word 0               ; IRQ vector (unused for now)

.segment "CODE"
Reset:
  ; Wait for PPU to be ready (first VBlank)
  bit $2002             ; Read PPUSTATUS
: bit $2002             ; Check bit 7
  bpl :-                ; Loop until VBlank occurs

  ; Wait for second VBlank (PPU is now stable)
: bit $2002
  bpl :-

  ; Set background color to light blue
  lda $2002             ; Read PPUSTATUS to reset address latch
  lda #$3F              ; High byte of palette address ($3F00)
  sta $2006             ; Write to PPUADDR
  lda #$00              ; Low byte of palette address
  sta $2006             ; Write to PPUADDR
  lda #$12              ; Color $12 = light blue
  sta $2007             ; Write to PPUDATA (palette RAM)

  ; Infinite loop
loop:
  jmp loop

.segment "CHR"
  .res 8192, $00        ; Empty CHR-ROM (8KB of zeros)
```

**Note:** 6502 assembly uses hexadecimal ($) and labels (like `Reset:` and `loop:`). The `bit`, `lda`, `sta`, and `jmp` are 6502 instructions we'll learn throughout this tier.

## Hardware Interaction

**Chips Involved:**
- Ricoh 2A03 CPU (6502-based, executing our code)
- PPU (Picture Processing Unit, displaying output)

**Memory Addresses:**
- $2002: PPUSTATUS register (read to detect VBlank)
- $2006: PPUADDR register (set VRAM address)
- $2007: PPUDATA register (write to VRAM)
- $3F00: Palette RAM address (background color 0)
- $FFFC-$FFFD: Reset vector (CPU reads this at power-on)

**PPU Palette:**
The NES has 64 possible colors (0-63). Common colors:
- $0F: Black
- $30: White
- $12: Light blue (used in example)
- $16: Red
- $1A: Green

## Common Pitfalls

1. **Forgetting iNES header:** Without the 16-byte header, emulators won't recognize the file
2. **Not waiting for PPU:** Writing to PPU before 2 VBlanks causes glitches
3. **Wrong PPUADDR sequence:** Must write high byte first, then low byte
4. **Missing infinite loop:** CPU will execute garbage data if program ends
5. **Incorrect segment names:** Must use "HEADER", "VECTORS", "CODE", "CHR" exactly

## Extension Ideas

- Change the color value ($12) to other colors (try $16 for red, $1A for green)
- Try other palette addresses ($3F01-$3F03 affect different parts of background)
- Add comments explaining what each instruction does
- Experiment with different CHR-ROM sizes in the header

## Builds Toward

**In This Tier:**
- L2: Understanding how the PPU works in detail
- L3: Learning the 6502 CPU and NES memory map
- L4: VBlank synchronization for timing

**In Next Tier:**
- Complex graphics (tiles and sprites)
- Controller input
- Game logic and physics

## Quick Reference

**iNES Header Format:**
```
Byte 0-3:   "NES" $1A (magic signature)
Byte 4:     PRG-ROM size (in 16KB units)
Byte 5:     CHR-ROM size (in 8KB units)
Byte 6:     Mapper + mirroring flags
Byte 7:     Mapper + system type
Byte 8-15:  Unused (zeros)
```

**Essential PPU Registers:**
- $2002: PPUSTATUS (read bit 7 for VBlank)
- $2006: PPUADDR (set VRAM address, write twice: high then low)
- $2007: PPUDATA (read/write VRAM at current address)

**Basic 6502 Instructions (Lesson 1):**
- `bit address`: Test bits in memory (doesn't change A)
- `lda #value`: Load accumulator with immediate value
- `lda address`: Load accumulator from memory address
- `sta address`: Store accumulator to memory address
- `jmp label`: Jump to label (infinite loop with self-reference)
- `bpl label`: Branch if plus (bit 7 = 0)

**Assembler Directives:**
- `.segment "NAME"`: Define memory segment
- `.byte value`: Emit raw byte
- `.word address`: Emit 16-bit address (little-endian)
- `.res count, value`: Reserve space (count bytes of value)
- `:` (anonymous label): For local loops (`:` and `:-` syntax)

**Build Commands:**
```bash
ca65 minimal.asm -o minimal.o
ld65 minimal.o -C nes.cfg -o minimal.nes
```

**Common Linker Config (nes.cfg):**
Defines segment locations (HEADER at $0000, CODE at $8000, VECTORS at $FFFA, CHR at end of file).

## NES-Specific Notes

**Why wait for 2 VBlanks?**
The PPU takes approximately 2 frames (~33ms) to stabilize after power-on. Writing to it earlier causes unpredictable behavior.

**Why the infinite loop?**
The NES has no operating system. If your program ends, the CPU will continue executing whatever data is in memory, which will likely crash.

**Why $3F00?**
The PPU's VRAM is mapped to specific addresses:
- $0000-$1FFF: Pattern tables (graphics)
- $2000-$2FFF: Nametables (background layout)
- $3F00-$3F1F: Palettes (colors)

**PPUADDR write sequence:**
PPUADDR is 8 bits wide but PPU addresses are 16 bits. You must write twice: high byte first, then low byte. The PPU has an internal latch that flips with each write.

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Lesson specification complete
