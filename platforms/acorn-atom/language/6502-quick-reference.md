# 6502 Quick Reference (Acorn Atom)

**Purpose:** quick 6502 instruction-set lookup for Acorn Atom lesson creation,
plus the Atom-specific bits — the `#`-for-hex convention, the built-in assembler's
syntax, and reaching the machine through COS routines and the memory-mapped VDG.
**Audience:** curriculum designers writing Acorn Atom assembly lessons.
**For comprehensive detail:** the primary reference library (cited throughout).

> **Scaffold doc.** The 6502 core here is the same instruction set the C64 and NES
> use, so it is given in summary; the value-add for the Atom is the dialect and
> entry-point section. TODOs mark depth still owed.

The Atom's CPU is the **MOS 6502** (~1 MHz) — standard NMOS 6502. If you have
written C64 or NES assembly, the instruction set is identical; what changes is the
machine you call into and two period conventions:

- **Hex is written with a leading `#`** in Atom documentation (`#8000`) — which
  visually collides with the 6502 immediate-mode `#`. Read Atom listings with
  care, and keep each curriculum file internally consistent.
- The Atom reaches the screen, keyboard, cassette and sound through **COS
  routines** and **direct memory access** to the memory-mapped MC6847, rather than
  a clean vectored OS jump table like the BBC's MOS.

The instruction set, registers, and addressing modes below are the shared NMOS
6502 core. For the same set with fuller per-instruction examples and cycle counts,
see the C64 sibling doc — the core is identical, only the surrounding machine
differs:
[`../../commodore-64/hardware/6510-quick-reference.md`](../../commodore-64/hardware/6510-quick-reference.md),
and the BBC's
[`../../bbc-micro/language/6502-quick-reference.md`](../../bbc-micro/language/6502-quick-reference.md).

## Registers

| Register | Size | Purpose |
|----------|------|---------|
| **A** (Accumulator) | 8-bit | Arithmetic / logic, main data register |
| **X** (Index) | 8-bit | Counter, offset, loop control |
| **Y** (Index) | 8-bit | Counter, offset, loop control |
| **PC** (Program Counter) | 16-bit | Address of next instruction |
| **S** (Stack Pointer) | 8-bit | Points into the stack page `#0100`–`#01FF` |
| **P** (Status) | 8-bit | Flags: N V - B D I Z C |

Status flags: **N** negative, **V** overflow, **B** break, **D** decimal,
**I** interrupt-disable, **Z** zero, **C** carry (bit 5 unused, reads as 1).

On the Atom the stack lives in the **block zero RAM** at `#0000`–`#03FF`, which the
tech manual warns "should not normally be accessed by the user" — zero page and
stack are OS/BASIC workspace.

## Addressing modes

| Mode | Example (6502 norm) | Notes |
|------|---------------------|-------|
| Implied | `TAX` | No operand |
| Accumulator | `LSR A` | Operate on A |
| Immediate | `LDA #05` | Literal value — note `#` here is the 6502 immediate marker |
| Zero page | `LDA $70` | Address `$00`–`$FF`, faster |
| Zero page,X / ,Y | `LDA $70,X` | Zero page + index |
| Absolute | `LDA $7000` | Full 16-bit address |
| Absolute,X / ,Y | `LDA $7000,X` | Absolute + index |
| Indirect | `JMP ($0070)` | Address held at pointer |
| Indexed indirect | `LDA ($70,X)` | ZP pointer + X, then load |
| Indirect indexed | `LDA ($70),Y` | ZP pointer, then + Y (common) |
| Relative | `BNE label` | Branch −128..+127 |

> **Dialect caution.** The table above uses the conventional 6502 `$`-for-hex /
> `#`-for-immediate notation that Asm198x and the C64/NES docs use. **Period Atom
> source uses `#` for hexadecimal addresses**, which is the opposite convention.
> The curriculum will settle one consistent notation per Atom file; flag which one
> a sample uses in its header.
<!-- TODO: record the curriculum's chosen Atom source notation (Asm198x `$`/`#` convention vs period Atom `#`-hex) once the first unit is written, and state it here. -->

## Instruction groups

A summary by category — the 6502 core is identical to the C64/NES, so see those
docs for per-instruction detail:

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

The Atom's 6502 is the base NMOS set — no 65C02/65C12 extensions.

## The Atom's built-in assembler (entry from BASIC)

Atom BASIC contains a 6502 assembler reached with **square brackets** — the direct
ancestor of BBC BASIC's inline assembler (Atomic Theory §Assembler Programming).
The shape a unit needs:

- **`P` is the location counter** — set `P` to the assemble address; the assembler
  advances it as it emits bytes. (Note: the Atom uses `P`; the later BBC uses
  `P%`.)
- **`[`** switches BASIC into assembling 6502 mnemonics; **`]`** switches back.
- **`LINK addr`** runs the assembled machine code from BASIC (the Atom's
  equivalent of the BBC's `CALL`); the routine returns to BASIC with `RTS`.
- **`?addr`** reads/writes one byte and **`!addr`** a 4-byte word from
  BASIC/assembler — e.g. `?#8000=127` pokes a byte (Atomic Theory).

The book's own demonstration line (verbatim, period `#`-hex notation):

```text
P=320;[INX; LDA 0,X; STA #B002; JMP 320;
]
```

then `LINK 320` runs it — the example deliberately toggles an I/O port
(`#B002`, the 8255) so the machine "makes a buzzing noise" through the loudspeaker
(Atomic Theory §Assembler Programming). The point for curriculum is the *shape*:
BASIC for setup, brackets for machine code, `LINK` to run. See
[`../basic.md`](../basic.md) for the BASIC/assembler bridge in full.

## Reaching the machine (Atom entry points)

Unlike the BBC's tidy MOS jump table at page `#FF`, the Atom mixes **COS ROM
routines** with **direct memory access**:

- **Screen** — memory-mapped through the MC6847; write characters/pixels straight
  into video RAM (base `#8000`). See [`../hardware/ARCHITECTURE.md`](../hardware/ARCHITECTURE.md) § Video.
- **Keyboard** — scanned via the INS8255 PPI; COS provides read routines.
- **Sound** — toggle **bit 2 of the 8255 output port** in a timed loop (no sound
  chip). See ARCHITECTURE § Sound.
- **Cassette** — COS routines drive the CUTS 300-baud interface.

<!-- TODO: build an Atom COS entry-point / call table (the OSRDCH/OSWRCH-equivalent vectors and useful ROM routine addresses) from the Atom Technical Manual's OS section and Atomic Theory, with provenance. The BBC's clean MOS table does NOT apply to the Atom. -->

## Minimal shape of an Atom assembly program

Two routes a unit might take:

1. **Inside BASIC** — `P=addr; [ ... ]` then `LINK addr` (the period idiom above).
   Lowest-friction for a learner already in BASIC; the Acorn lineage.
2. **Standalone 6502 via Asm198x** — assemble to a flat `.bin` at an `org`, loaded
   by the Emu198x Atom core. The build/capture/output-container status for this
   route is in [`../TOOLCHAIN-RESEARCH.md`](../TOOLCHAIN-RESEARCH.md) (the Emu198x
   `machine-acorn-atom` core is **in active development**).

<!-- TODO: add a complete, buildable hello-world (.asm) under code-samples/acorn-atom/assembly/ and reference it here via CodeFromFile, once the Asm198x Atom target invocation and the Emu198x core are confirmed (see TOOLCHAIN-RESEARCH.md). -->

## See also

- [`../hardware/ARCHITECTURE.md`](../hardware/ARCHITECTURE.md) — memory map, video (MC6847), sound, the RAM constraint.
- [`../basic.md`](../basic.md) — Atom BASIC and its built-in assembler (the lineage to BBC BASIC).
- [`../reference.md`](../reference.md) — platform entry doc and toolchain.
- Primary library:
  `reference/by-system/acorn-atom/1980-atomic-theory-and-practice.md`
  (§Assembler Programming, §Addressing Modes and Registers, §Assembler Mnemonics),
  `reference/by-system/acorn-atom/unknown-atom-technical-manual-issue-2.md`.
