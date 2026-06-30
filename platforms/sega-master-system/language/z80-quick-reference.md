# Z80 Assembly Quick Reference (Sega Master System)

**Purpose:** Fast Z80 instruction lookup for SMS assembly, plus the SMS-specific
I/O ports you talk to instead of OS calls.
**Audience:** SMS curriculum designers and learners. Assumes programming ability;
prior Spectrum (Z80) exposure is a bonus but not assumed.
**Note:** The CPU is the **same Z80A as the ZX Spectrum** — the instruction set,
registers, and addressing modes here apply identically to both. What is
SMS-specific is the **I/O ports** section at the end: there is **no OS call layer**
on the SMS, so you reach the video and sound chips directly with `IN`/`OUT`.
**Source of truth:** `reference/by-system/sega-master-system/sms-reference.md` for
the SMS port map; chip-level Z80 timing should be confirmed against a Z80 CPU
companion reference (see TODOs).

---

## Registers

The Z80 has a richer register file than the 6502:

| Register | Size | Purpose |
|----------|------|---------|
| **A** | 8-bit | Accumulator (arithmetic/logic) |
| **F** | 8-bit | Flags (see below) |
| **B, C** | 8-bit each | General; pair **BC** is 16-bit (loop counter, port for `OUT (C)`) |
| **D, E** | 8-bit each | General; pair **DE** is 16-bit (often a source/dest pointer) |
| **H, L** | 8-bit each | General; pair **HL** is the primary 16-bit pointer/accumulator |
| **IX, IY** | 16-bit | Index registers (base + signed displacement) |
| **SP** | 16-bit | Stack pointer (grows downward) |
| **PC** | 16-bit | Program counter |
| **I** | 8-bit | Interrupt vector base (IM 2) |
| **R** | 8-bit | Memory refresh counter |

The Z80 also has a **shadow set** (`AF'`, `BC'`, `DE'`, `HL'`) swapped in with
`EX AF,AF'` and `EXX` — handy for fast interrupt handlers (save state in one
instruction instead of pushing).

### Flags (F register)

```
Bit 7: S  (Sign)        - set if result bit 7 = 1
Bit 6: Z  (Zero)        - set if result is zero
Bit 5: -  (unused / copy of result bit 5)
Bit 4: H  (Half-carry)  - BCD adjust
Bit 3: -  (unused / copy of result bit 3)
Bit 2: P/V (Parity/Overflow) - parity for logic, overflow for arithmetic
Bit 1: N  (Add/Subtract)     - last op was a subtract
Bit 0: C  (Carry)
```

---

## Addressing modes

| Mode | Example | Description |
|------|---------|-------------|
| Immediate | `LD A, $05` | literal byte |
| Immediate extended | `LD HL, $C000` | literal 16-bit |
| Register | `LD A, B` | register to register |
| Register indirect | `LD A, (HL)` | byte at address in HL |
| Indexed | `LD A, (IX+4)` | byte at IX + signed displacement |
| Extended (absolute) | `LD A, ($C000)` | byte at a 16-bit address |
| Relative | `JR label` | PC-relative branch (−128..+127) |
| Bit | `BIT 7, A` | test/set/reset a single bit |
| I/O | `IN A, ($BF)` / `OUT ($BE), A` | read/write an I/O port |

<!-- TODO: confirm per-instruction byte/cycle (T-state) counts against a Z80 CPU
companion reference before publishing exact timing tables -->

---

## Instruction groups

This is a grouped overview, not an exhaustive opcode table — Z80 has hundreds of
encodings. The aim is to orient a learner; cite a full Z80 reference for the
complete set.

### Load and store (`LD`)
The Z80 folds nearly all data movement into one mnemonic, `LD dst, src`:
```
LD A, $05         ; immediate into A
LD B, A           ; register to register
LD HL, $C000      ; 16-bit immediate into a pair
LD (HL), A        ; store A at address in HL
LD A, (DE)        ; load A from address in DE
LD ($C000), A     ; store A at an absolute address
LD A, (IX+2)      ; indexed load
```

### Arithmetic and logic
```
ADD A, B          ; A = A + B
ADC A, n          ; add with carry
SUB n / SBC A, n  ; subtract / with carry
AND / OR / XOR n  ; logic (result in A)
CP n              ; compare (A - n, flags only, A unchanged)
INC r / DEC r     ; increment/decrement 8- or 16-bit
ADD HL, DE        ; 16-bit add into HL
```

### Bit operations
```
BIT 7, A          ; test bit 7 (sets Z if clear)
SET 0, (HL)       ; set bit 0 of byte at HL
RES 3, B          ; reset bit 3 of B
```

### Shifts and rotates
```
RLCA / RRCA       ; rotate A (fast, no carry-through forms)
RL r / RR r       ; rotate through carry
SLA r / SRL r     ; arithmetic/logical shift
```

### Jumps, calls, returns
```
JP $0038          ; absolute jump
JP NZ, label      ; conditional jump
JR label          ; relative jump (shorter, faster)
JR Z, label       ; conditional relative jump
DJNZ label        ; dec B, jump if non-zero (tight loops)
CALL label        ; push PC, jump (subroutine)
RET / RET Z       ; return / conditional return
RETI / RETN       ; return from interrupt / NMI
```

### Stack
```
PUSH HL / POP HL  ; 16-bit push/pop (also AF, BC, DE, IX, IY)
```

### Block instructions (a Z80 strength)
```
LDIR              ; copy (HL)->(DE), inc both, dec BC, repeat until BC=0
LDDR              ; same, decrementing
OTIR / OTDR       ; OUT (C) from (HL) repeatedly — fast port streaming
INIR / INDR       ; IN to (HL) repeatedly
```
`LDIR` and the `OTIR` family matter on the SMS: `OTIR` streams a buffer to a port
in a tight hardware loop — useful for pushing data to the VDP, though the VDP's
own VRAM-copy mode is faster for VRAM-to-VRAM moves (`sms-reference.md` § VDP
Integration → "DMA-style VRAM fills").

### Interrupt control
```
DI / EI           ; disable / enable interrupts
IM 1              ; interrupt mode 1 — REQUIRED on the SMS
```
The SMS uses **IM 1**: on interrupt the Z80 jumps to the fixed `$0038`. IM 0 and
IM 2 do not work in the usual way because the SMS provides no vector on the data
bus (`sms-reference.md` § VDP Integration → "Interrupt handling").

<!-- TODO: expand each group into per-instruction byte/cycle tables once a Z80 CPU
companion reference is in the library; keep this grouped overview as the summary -->

---

## SMS I/O ports — talking to the hardware directly

This is the SMS-specific heart of the reference. There is **no OS and no BASIC** —
you reach the VDP, the PSG, and the controllers with the Z80's `IN`/`OUT`
instructions. The Z80 uses only the low 8 bits of the port address, and many SMS
ports respond to a *range* rather than one exact address (`sms-reference.md`
§ I/O Port Map).

| Port | Read | Write |
|------|------|-------|
| `$3E` | — | Memory control (BIOS / cart / I/O enable bits) |
| `$3F` | — | I/O control (controller TH-pin direction — light gun, etc.) |
| `$7E` | V counter (current scanline) | PSG data |
| `$7F` | H counter (latched) | PSG data |
| `$BE` | VDP data | VDP data |
| `$BF` | VDP status | VDP control |
| `$DC` | Controller port A (player 1) | — |
| `$DD` | Controller port B (player 2 + misc) | — |
| `$F0`/`$F1`/`$F2` | YM2413 (Japanese SMS only) | YM2413 FM |

Practical patterns:

```
; --- Write a byte to the PSG (sound) ---
    LD A, $9F
    OUT ($7F), A          ; PSG is write-only; any port in $40-$7F works

; --- Set a VDP VRAM write address, then stream data ---
    LD A, $00
    OUT ($BF), A          ; low byte of address
    LD A, $7F             ; $40 = VRAM-write op | high byte $3F
    OUT ($BF), A
    LD A, tile_byte
    OUT ($BE), A          ; data port auto-increments

; --- Write a VDP register (e.g. register 1, mode control) ---
    LD A, $E2             ; value
    OUT ($BF), A
    LD A, $81             ; $80 = register-write op | $01 = register number
    OUT ($BF), A

; --- Read player 1 input (active-low: pressed = 0) ---
    IN A, ($DC)           ; bits: up/down/left/right/B1/B2 ...
```

Two gotchas that bite SMS beginners (`sms-reference.md` § VDP Integration,
§ PSG Integration):

- **The VDP control port has a first-byte/second-byte latch.** Reading the status
  register at `$BF` (e.g. to clear the frame interrupt) *resets the latch*. If an
  interrupt handler reads `$BF` mid-sequence, the next two control writes can be
  misread. Structure interrupt handlers so they never interrupt a control-port
  sequence.
- **The PSG has no status and no interrupt.** Drive sound updates from the frame
  interrupt (a music tick at 50/60 Hz), not a busy loop.

For controller bit layouts, the TH-pin protocol (light gun, paddle), the pause
NMI, and the full port decoding, see `sms-reference.md` § Controller Protocol and
§ I/O Port Map. The chip-level VDP/PSG register detail is summarised in
[../hardware/ARCHITECTURE.md](../hardware/ARCHITECTURE.md).

---

## See also

- [../reference.md](../reference.md) — platform entry doc and toolchain.
- [../hardware/ARCHITECTURE.md](../hardware/ARCHITECTURE.md) — memory map, mapper,
  VDP, PSG, and chip lineage.
- `reference/by-system/sega-master-system/sms-reference.md` — system reference
  (the source of truth for the port map and integration detail).
- The ZX Spectrum track's Z80 material — same CPU, different machine; cross-read
  for instruction-level depth.
</content>
