# Z80 Assembly Quick Reference (MSX)

A programming-focused summary of the Zilog Z80 instruction set as you will use it
on the MSX, plus the MSX-specific conventions — how to call the BIOS, and how to
reach the VDP, PSG, and keyboard. This is a starting reference, not a complete
opcode table; for exhaustive timing and encoding, use the primary library and the
Asm198x Z80 spec.

> **Source of truth.** The Z80 is the same CPU the ZX Spectrum uses, so the
> instruction set is standard Zilog. MSX-specific calling conventions and BIOS
> addresses are from
> `reference/by-system/msx/msx-reference.md`
> (§§4–7, 12). Instruction *encoding* is owned by the Asm198x Z80 ISA spec
> (opcode-complete, dialect-validated). Specifics not yet pinned down are flagged
> `TODO`.

## The CPU is a Z80 — so MSX assembly is Z80 assembly

If you have written Spectrum (or Amstrad CPC, or MSX-from-another-course) Z80, the
CPU half of MSX is identical. What is MSX-specific is *how you talk to the
hardware*: through I/O ports and BIOS calls, covered at the end of this page. And
remember the **M1 wait state** — every instruction fetch costs an extra T-state on
MSX1, so raw cycle counts run ~20% slower than the Zilog datasheet
([../reference.md](../reference.md), `msx-reference.md` §2.4).

## Registers

| Group | Registers |
|-------|-----------|
| 8-bit | `A` (accumulator), `B`, `C`, `D`, `E`, `H`, `L`, `F` (flags) |
| 16-bit pairs | `AF`, `BC`, `DE`, `HL` |
| Index | `IX`, `IY` (16-bit, with `(IX+d)` / `(IY+d)` displacement addressing) |
| Special | `SP` (stack pointer), `PC` (program counter), `I` (interrupt vector), `R` (refresh) |
| Alternate set | `AF'`, `BC'`, `DE'`, `HL'` — swapped in with `EX AF,AF'` and `EXX` |

`HL` is the workhorse 16-bit pointer; `A` is the only register most arithmetic and
logic operates on. The alternate set is handy for fast interrupt handlers (swap in,
do work, swap out).

## Flags (the F register)

| Bit | Flag | Set when |
|-----|------|----------|
| 7 | S (sign) | result is negative (bit 7 set) |
| 6 | Z (zero) | result is zero |
| 4 | H (half-carry) | carry out of bit 3 (used by `DAA`) |
| 2 | P/V | parity, or signed overflow, depending on instruction |
| 1 | N | last op was a subtraction (used by `DAA`) |
| 0 | C (carry) | carry/borrow out, or shifted-out bit |

Conditional jumps/calls/returns test `Z`/`NZ`, `C`/`NC`, `P`/`M` (sign), `PE`/`PO`
(parity/overflow).

## Common instruction groups

- **Load (move data)** — `LD dst, src`. Registers, immediates, memory via `(HL)`,
  `(IX+d)`, `(nn)`. E.g. `LD A,$20`, `LD (HL),B`, `LD HL,$4000`.
- **Block moves** — `LDIR` / `LDDR` copy `BC` bytes `(HL)→(DE)` (incrementing /
  decrementing). The fast way to fill or copy memory.
- **Arithmetic** — `ADD`, `ADC`, `SUB`, `SBC`, `INC`, `DEC` (8- and some 16-bit
  forms), `CP` (compare = subtract without storing), `DAA` (BCD fix-up), `NEG`.
- **Logic** — `AND`, `OR`, `XOR`, `CPL` (complement A).
- **Bit operations** — `BIT n,r` (test), `SET n,r`, `RES n,r` (set/clear a bit).
- **Shifts/rotates** — `RLC`, `RRC`, `RL`, `RR`, `SLA`, `SRA`, `SRL`, and the
  `A`-only fast forms `RLCA`/`RRCA`/`RLA`/`RRA`.
- **Jumps** — `JP nn` (absolute), `JR e` (relative, ±127, smaller/faster),
  `DJNZ e` (decrement `B`, jump if non-zero — the canonical loop).
- **Subroutines** — `CALL nn`, `RET`, conditional forms (`CALL Z,nn`, `RET NC`),
  and the one-byte `RST n` restarts.
- **Stack** — `PUSH rr` / `POP rr` (16-bit pairs).
- **I/O** — `IN A,(n)` / `OUT (n),A`, plus register-indirect `IN r,(C)` /
  `OUT (C),r`. This is how you reach the VDP, PSG, and PPI (see below).
- **Interrupts** — `DI` / `EI` (disable/enable), `IM 1` (the MSX mode), `RETI`.

<!-- TODO: if a unit needs exact T-state counts, cite the Asm198x Z80 spec /
     msx-technical-data-book.md rather than listing per-instruction timings here;
     remember to add the MSX1 +1 M1 wait state on top of base figures. -->

## Addressing modes

| Mode | Example | Meaning |
|------|---------|---------|
| Immediate | `LD A,$10` | constant |
| Register | `LD A,B` | register to register |
| Register indirect | `LD A,(HL)` | memory pointed to by a pair |
| Indexed | `LD A,(IX+4)` | memory at index register + signed displacement |
| Extended (absolute) | `LD A,($C000)` | memory at a fixed address |
| Relative | `JR NZ,loop` | PC-relative branch (±127 bytes) |
| Bit | `BIT 7,(HL)` | single-bit test/set/reset |

## Reaching MSX hardware through I/O ports

The VDP, PSG, and PPI sit in the I/O port space — you drive them with `OUT`/`IN`,
not memory access. The key ports (full detail in
[../hardware/ARCHITECTURE.md](../hardware/ARCHITECTURE.md)):

| Ports | Chip | Use |
|-------|------|-----|
| `$98` / `$99` | TMS9918A VDP | VRAM data / register+address+status |
| `$A0` / `$A1` / `$A2` | AY-3-8910 PSG | register select / data write / data read |
| `$A8` | 8255 PPI port A | primary slot select |
| `$A9` / `$AA` | 8255 PPI ports B / C | keyboard column read / row select + cassette + CAPS + click |

(`msx-reference.md` §§4.1, 5.1, 6.1.)

## The MSX BIOS calling convention

Most of the time you should not poke hardware directly — the **BIOS** gives you a
stable, vendor-independent way in. Every BIOS routine sits at a **fixed address in
page 0** (a jump table), so the *same* `CALL` works on any MSX. Arguments go in
registers; the routine returns in registers, often using the carry flag for
success/failure.

A small, high-value subset to start with:

| Address | Name | Does |
|---------|------|------|
| `$00A2` | `CHPUT` | Print the character in `A` to the screen |
| `$009F` | `CHGET` | Wait for and return one key in `A` |
| `$009C` | `CHSNS` | Test the keyboard buffer (`Z` set = empty) |
| `$00C0` | `BEEP` | Make the beep sound |
| `$00C3` | `CLS` | Clear the screen |
| `$005F` | `CHGMOD` | Set the screen mode (`A` = mode number) |
| `$004D` | `WRTVRM` | Write `A` to VRAM address in `HL` |
| `$004A` | `RDVRM` | Read VRAM at `HL` into `A` |
| `$005C` | `LDIRVM` | Block-copy memory `→` VRAM |
| `$0093` | `WRTPSG` | Write PSG register (`A` = reg, `E` = data) |
| `$00D5` | `GTSTCK` | Read joystick direction (`A` = port → `A` = 0–8) |
| `$00D8` | `GTTRIG` | Read joystick/space trigger |

Example — print a character:

```z80
    ld   a, 'A'        ; character to print
    call $00A2         ; CHPUT — output it to the console
```

> **Two BIOS gotchas.** `CALSLT` and `ENASLT` (the inter-slot primitives) disable
> interrupts and do **not** re-enable them — you must `EI` yourself, or everything
> stops after one call (`msx-reference.md` §3.5). And if you drive the VDP
> directly, reading status port `$99` clears the VBlank flag as a side effect
> (§4.1).

The full BIOS entry table (dozens of routines: tape, disk, printer, sprites,
maths, the keyboard matrix) is in
`reference/by-system/msx/msx-reference.md` §12.

<!-- TODO: confirm exact register in/out details for each BIOS call above against
     msx-reference.md §12.2 / msx-technical-data-book.md before using in a unit;
     the table here is the starter subset, not the full contract. -->

## See also

- [../hardware/ARCHITECTURE.md](../hardware/ARCHITECTURE.md) — the chips these
  instructions drive
- `reference/by-system/msx/msx-reference.md` §12
  — the complete BIOS entry table
- [../basic.md](../basic.md) — MSX-BASIC, for the BASIC track
