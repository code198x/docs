# 6502 Quick Reference (VIC-20)

**Purpose:** Quick 6502 instruction-set lookup for VIC-20 lesson creation, plus
the VIC-20-specific KERNAL call conventions.
**Audience:** Curriculum designers writing VIC-20 assembly units.
**Facts cite:** the **VIC-20 Programmer's Reference Guide**
(`reference/by-system/commodore-vic20/vic-20-programmers-reference-guide-1st-edition-6th-printing`)
and the distilled `vic20-reference.md` (KERNAL jump table, §18 and Appendix D).

> **Scaffold + cousin doc.** The VIC-20 runs a stock **6502**, whose
> programmer-visible core is identical to the C64's **6510**. Rather than
> duplicate the full instruction tables, this doc summarises and points to the
> C64 [`6510-quick-reference`](../../commodore-64/hardware/6510-quick-reference.md)
> for the exhaustive per-instruction detail, then covers what is
> **VIC-20-specific**: the KERNAL calling conventions. Deeper expansions carry
> explicit `TODO`s.

---

## Registers

| Register | Size | Purpose |
|----------|------|---------|
| **A** (Accumulator) | 8-bit | Arithmetic / logic, the main working register |
| **X** (Index) | 8-bit | Counter, offset, loop control |
| **Y** (Index) | 8-bit | Counter, offset, loop control (the indirect-indexed register) |
| **PC** (Program Counter) | 16-bit | Address of the next instruction |
| **SP** (Stack Pointer) | 8-bit | Top of the stack at `$0100–$01FF` |
| **P** (Status) | 8-bit | Flags: N V - B D I Z C |

### Status flags (P)

```
Bit 7: N (Negative)   Bit 3: D (Decimal)
Bit 6: V (Overflow)   Bit 2: I (Interrupt disable)
Bit 5: - (unused, =1) Bit 1: Z (Zero)
Bit 4: B (Break)      Bit 0: C (Carry)
```

## Addressing modes

| Mode | Example | Bytes |
|------|---------|-------|
| Implied | `TAX` | 1 |
| Accumulator | `LSR A` | 1 |
| Immediate | `LDA #$05` | 2 |
| Zero Page | `LDA $80` | 2 |
| Zero Page,X / ,Y | `LDA $80,X` / `LDX $80,Y` | 2 |
| Absolute | `LDA $1E00` | 3 |
| Absolute,X / ,Y | `LDA $1E00,X` | 3 |
| Indirect | `JMP ($0080)` | 3 |
| Indexed Indirect | `LDA ($80,X)` | 2 |
| Indirect Indexed | `LDA ($80),Y` | 2 |
| Relative | `BNE LABEL` | 2 |

## Instruction groups

Same 151 documented opcodes as every NMOS 6502. Grouped for lesson design (full
tables, flag effects, and worked examples in the C64
[`6510-quick-reference`](../../commodore-64/hardware/6510-quick-reference.md)):

- **Load / store:** `LDA LDX LDY` / `STA STX STY`
- **Transfer:** `TAX TAY TXA TYA TSX TXS`
- **Arithmetic:** `ADC SBC INC DEC INX INY DEX DEY` (always `CLC` before `ADC`, `SEC` before `SBC`)
- **Logic / shift:** `AND ORA EOR BIT ASL LSR ROL ROR`
- **Compare:** `CMP CPX CPY`
- **Branch:** `BEQ BNE BCC BCS BMI BPL BVC BVS` (range −128…+127)
- **Jump / subroutine:** `JMP JSR RTS`
- **Stack:** `PHA PLA PHP PLP`
- **Flags:** `CLC SEC CLD SED CLI SEI CLV`
- **Other:** `NOP BRK RTI`

### VIC-20 notes that differ from the C64 in practice

- **Clock:** 1.0227 MHz (NTSC) / 1.1082 MHz (PAL) — roughly 1 cycle ≈ 1 µs, same
  ballpark as the C64, but PAL/NTSC timing differs (see
  [`../hardware/ARCHITECTURE.md`](../hardware/ARCHITECTURE.md)).
- **No raster interrupt.** Unlike the C64's VIC-II, the VIC chip raises no IRQ;
  beam-sync code polls the raster register at `$9004` or rides VIA-2 timer 1.
- **Decimal mode:** `CLD` at start as on every Commodore — the KERNAL expects
  binary mode.

## KERNAL call conventions (VIC-20-specific)

The KERNAL is the OS in ROM ($E000–$FFFF). Call it through the **jump table** at
the top of ROM, never into the implementation addresses — the jump table is the
stable contract across ROM revisions, and it is the *same* table the C64
inherited (`vic20-reference.md` §18, Appendix D).

General convention:

- Arguments and results are passed in **A / X / Y**.
- On error, a routine returns with **carry set** and an error code in **A**
  (0 = STOP pressed, 1 = too many files, 2 = file open, 3 = file not open,
  4 = file not found, 5 = device not present) (`vic20-reference.md` §18).
- Save any registers you need across a call (`PHA`/`PLA`) — KERNAL routines
  clobber freely.

### The calls a first VIC-20 unit needs

| Address | Name | Use |
|---------|------|-----|
| `$FFD2` | **CHROUT** | Print the character in A to the current output (the screen by default). The workhorse for "hello world". |
| `$FFCF` | **CHRIN** | Read one character from the current input (keyboard line). |
| `$FFE4` | **GETIN** | Get a key from the keyboard buffer without waiting (0 = none) — the game-loop input call. |
| `$FFE1` | **STOP** | Test the RUN/STOP key (Z set if pressed) — the polite way to let the user break out. |
| `$FFD5` | **LOAD** | Load a file. |
| `$FFD8` | **SAVE** | Save a file. |
| `$FF9F` | **SCNKEY** | Scan the keyboard matrix. |
| `$FFE7` | **CLALL** | Close all files. |

Minimal "print a character" example (CHROUT):

```assembly
        LDA #65         ; PETSCII 'A'
        JSR $FFD2       ; CHROUT — print it
        RTS
```

The fuller jump table (file/serial/time routines: `SETLFS $FFBA`, `SETNAM
$FFBD`, `OPEN $FFC0`, `CHKIN $FFC6`, `CHKOUT $FFC9`, `CLRCHN $FFCC`, `RDTIM
$FFDE`, `PLOT $FFF0`, …) is in `vic20-reference.md` Appendix D. <!-- TODO: pull the file-I/O calling sequences (SETLFS/SETNAM/OPEN/CHKOUT) verbatim from the Programmer's Reference Guide when a load/save unit needs them -->

### PETSCII and screen codes

`CHROUT` takes **PETSCII**, but writing directly to screen RAM ($1E00 on a stock
machine) takes **screen codes** — a different encoding. Mixing them up is the
classic beginner trap. <!-- TODO: add a VIC-20 PETSCII / screen-code table (cite Programmer's Reference Guide character-set appendix; the C64 petscii-and-screen-codes.md is a close but not identical reference) -->

## See also

- [../hardware/ARCHITECTURE.md](../hardware/ARCHITECTURE.md) — memory map, VIC chip, the moving-screen quirk.
- [../../commodore-64/hardware/6510-quick-reference.md](../../commodore-64/hardware/6510-quick-reference.md) — full instruction tables, flag effects, worked patterns (the 6510 core matches the VIC-20's 6502).
- `reference/by-system/commodore-vic20/vic20-reference.md` §18 + Appendix D — KERNAL jump table.
