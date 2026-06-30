# 6502 Quick Reference (BBC Micro)

**Purpose:** quick 6502 instruction-set lookup for BBC lesson creation, plus the
BBC-specific bit — reaching the machine through the **MOS OS calls** rather than
poking hardware.
**Audience:** curriculum designers writing BBC Micro assembly lessons.
**For comprehensive detail:** the primary reference library (cited throughout).

> **Scaffold doc.** The 6502 core here is the same instruction set the C64 and
> NES use, so it is given in summary; the value-add for the BBC is the OS-call
> section. TODOs mark depth still owed.

The BBC's CPU is the **MOS 6502A** — standard NMOS 6502. If you have written C64
or NES assembly, the instruction set is identical; what changes is the OS you
call and the convention that **hex is written with `&`** (e.g. `&FFEE`) in BBC
documentation.

## Registers

| Register | Size | Purpose |
|----------|------|---------|
| **A** (Accumulator) | 8-bit | Arithmetic / logic, main data register |
| **X** (Index) | 8-bit | Counter, offset, loop control |
| **Y** (Index) | 8-bit | Counter, offset, loop control |
| **PC** (Program Counter) | 16-bit | Address of next instruction |
| **S** (Stack Pointer) | 8-bit | Points into the stack page `&0100`–`&01FF` |
| **P** (Status) | 8-bit | Flags: N V - B D I Z C |

Status flags: **N** negative, **V** overflow, **B** break, **D** decimal,
**I** interrupt-disable, **Z** zero, **C** carry (bit 5 unused, reads as 1).

## Addressing modes

| Mode | Example | Notes |
|------|---------|-------|
| Implied | `TAX` | No operand |
| Accumulator | `LSR A` | Operate on A |
| Immediate | `LDA #&05` | Literal value |
| Zero page | `LDA &70` | Address `&00`–`&FF`, faster |
| Zero page,X / ,Y | `LDA &70,X` | Zero page + index |
| Absolute | `LDA &7000` | Full 16-bit address |
| Absolute,X / ,Y | `LDA &7000,X` | Absolute + index |
| Indirect | `JMP (&0070)` | Address held at pointer |
| Indexed indirect | `LDA (&70,X)` | ZP pointer + X, then load |
| Indirect indexed | `LDA (&70),Y` | ZP pointer, then + Y (common) |
| Relative | `BNE label` | Branch −128..+127 |

## Instruction groups

A summary by category — see the C64 sibling doc
[`../../commodore-64/hardware/6510-quick-reference.md`](../../commodore-64/hardware/6510-quick-reference.md)
for the same instruction set with fuller per-instruction examples and cycle
counts (the 6502 core is identical).

- **Load / store:** `LDA LDX LDY` / `STA STX STY`
- **Transfer:** `TAX TAY TXA TYA TSX TXS`
- **Arithmetic:** `ADC SBC` (always `CLC` before add, `SEC` before subtract);
  `INC DEC INX DEX INY DEY`
- **Logic:** `AND ORA EOR BIT`
- **Shift / rotate:** `ASL LSR ROL ROR`
- **Compare:** `CMP CPX CPY`
- **Branch:** `BEQ BNE BCC BCS BMI BPL BVC BVS`
- **Jump / subroutine:** `JMP JSR RTS`
- **Stack:** `PHA PLA PHP PLP`
- **Flags:** `CLC SEC CLD SED CLI SEI CLV`
- **Other:** `NOP BRK RTI`

> **Master / 65C12 note.** The Master series uses the 65C12, which adds ~27
> instructions (`PHX PLX PHY PLY`, `INC A`/`DEC A`, `BRA`, `STZ`, and bit ops).
> The Model B's 6502A does **not** have these — curriculum code targeting the
> Model B should stay on the base NMOS 6502 set (reference §Master 128).

<!-- TODO: if a BBC unit needs exact cycle counts, add a timing table; the 6502 timings match the C64 doc but the BBC runs at 2 MHz (1 cycle ≈ 0.5 µs), not ~1 MHz. -->

## BBC OS calls (the MOS interface)

This is what makes BBC assembly *BBC* assembly. Rather than poking video, keyboard
and sound hardware directly, programs call the **Machine Operating System (MOS)**
through fixed addresses in page `&FF`. Each is a `JSR` to a jump-table entry that
the OS routes (and that filing systems / the Tube can intercept). The standard
practice is to define equates, e.g. `OSWRCH = &FFEE`, then `JSR OSWRCH`
(reference: 1982 assembly book, "OSWRCH … every machine has"; jump table in
[`bbc-micro-reference.md`](../../../../../reference/by-system/bbc-micro/bbc-micro-reference.md)
§Vectored OS Calls).

### The everyday calls

| Call | Address | Does | Registers |
|------|---------|------|-----------|
| **OSWRCH** | `&FFEE` | Write a character to the current output (screen) | `A` = character |
| **OSASCI** | `&FFE3` | Like OSWRCH but turns CR into CR+LF | `A` = character |
| **OSNEWL** | `&FFE7` | Write a newline (CR+LF) | — |
| **OSRDCH** | `&FFE0` | Read a character from the current input (keyboard) | returns `A` |
| **OSWORD** | `&FFF1` | Multi-byte call (parameter block at `XY`) — sound, clock, pixel read, etc. | `A` = reason, `X`/`Y` = block ptr |
| **OSBYTE** | `&FFF4` | Single-byte call (the `*FX` calls) — modes, keyboard, timers, flags | `A` = function, `X`/`Y` = params |
| **OSCLI** | `&FFF7` | Run a `*` command line (e.g. `*LOAD`, `*RUN`) | `XY` = command string ptr |
| **OSFILE** | `&FFDD` | Load/save a whole file | `A` = action, `XY` = block ptr |

`VDU` control codes (0–31) sent through OSWRCH drive the screen — clear screen,
set MODE, plot, position cursor, define the palette, program the 6845. For
example `LDA #12 : JSR OSWRCH` clears the screen, and `LDA #22 : JSR OSWRCH`
followed by a mode number selects a MODE (reference: 1982 assembly book §OSWRCH
usage).

### OSBYTE and OSWORD, briefly

- **OSBYTE** (`JSR &FFF4`, the assembly form of BASIC's `*FX A,X,Y`) is the
  catch-all for OS settings: select input/output streams, set flash rates,
  auto-repeat, **wait for vertical sync** (`A=&13`), read `HIMEM`/`OSHWM`
  (`A=&84`/`&83`), detect the machine type, and more (reference §OSBYTE
  Reference). For codes `&80`–`&FF` the `<new> = (<old> AND Y) EOR X` formula does
  atomic read-modify-write of OS flags.
- **OSWORD** (`JSR &FFF1`) is used when a call needs more than two bytes of
  parameters, passed in a block addressed by `X` (low) / `Y` (high). Notable:
  `A=&07` generate sound, `A=&08` define envelope, `A=&00` read a line of input,
  `A=&01` read the system clock, `A=&09` read a pixel (reference §OSWORD
  Reference).

<!-- TODO: add a worked "print a string" example (loop with OSWRCH, or OSASCI),
     a "wait for frame" example (OSBYTE &13), and a "make a sound" example
     (OSWORD &07 parameter block) once the first BBC units define their style. -->

## Minimal shape of a BBC assembly program

The conventional structure is: set an origin, define MOS-call equates, do the
work via `JSR` to MOS, then return (to BASIC via `RTS`, since BBC machine code is
typically reached with `CALL` from BASIC — see [`../basic.md`](../basic.md)).

<!-- TODO: add a complete, buildable hello-world (.asm) under
     code-samples/bbc-micro/assembly/ and reference it here via CodeFromFile,
     once the Asm198x BBC target invocation is confirmed (see TOOLCHAIN-RESEARCH.md). -->

## See also

- [`../hardware/ARCHITECTURE.md`](../hardware/ARCHITECTURE.md) — memory map, video, sound.
- [`../basic.md`](../basic.md) — BBC BASIC and its inline 6502 assembler (the BASIC→assembly bridge).
- Primary library:
  [`1982-assembly-language-programming-for-the-bbc-microcomputer.md`](../../../../../reference/by-system/bbc-micro/1982-assembly-language-programming-for-the-bbc-microcomputer.md),
  [`bbc-micro-reference.md`](../../../../../reference/by-system/bbc-micro/bbc-micro-reference.md) (§Vectored OS Calls, §OSBYTE Reference, §OSWORD Reference).
