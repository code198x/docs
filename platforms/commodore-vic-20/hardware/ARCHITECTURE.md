# VIC-20 Architecture

**Purpose:** Memory map, CPU, and VIC-chip overview for curriculum authors.
**Audience:** Lesson designers writing VIC-20 assembly and BASIC units.
**Facts cite:** the reference library at
`reference/by-system/commodore-vic20/` — chiefly the
**Programmer's Reference Guide** (`vic-20-programmers-reference-guide-1st-edition-6th-printing`),
the **Butterfield memory map** (`1983-vic-20-memory-map`), and the distilled
**`vic20-reference.md`**. For any disputed fact, the Programmer's Reference Guide
wins.

> **Scaffold.** Established facts are stated with citations; deeper specifics
> carry explicit `TODO` markers to confirm against the library before they reach
> a unit.

---

## The shape of the machine

The VIC-20 is unusually simple, which is exactly why it is a good machine to
learn (and to emulate). There is **no bank-switching MMU, no DMA chip, no PLA**,
and no copy of the OS in RAM — everything sits on the 6502's flat 64 KB address
space (`vic20-reference.md` §1). The custom **VIC chip** does video, sound,
paddle conversion, and light-pen latching by itself, and it generates the CPU
clock.

## CPU — MOS 6502

A stock NMOS 6502: 8-bit accumulator, X and Y index registers, 8-bit stack
pointer (stack at $0100–$01FF), 16-bit program counter, status register. Same
programmer-visible core as the C64's 6510 — so the C64
[`6510-quick-reference`](../../commodore-64/hardware/6510-quick-reference.md) and
this platform's [`6502 quick reference`](../language/6502-quick-reference.md)
both apply.

- **Clock** (derived from the VIC chip, not the other way round):
  **1.0227 MHz** NTSC (6560) / **1.1082 MHz** PAL (6561). One CPU cycle per
  memory cycle; the VIC and CPU interleave bus halves, so there are **no wait
  states and no screen hash** during display — unlike the C64's "bad lines"
  (`vic20-reference.md` §2, §5).
- **Interrupts:** IRQ comes from VIA-2 timer 1 (the 60 Hz NTSC / 50 Hz PAL jiffy
  clock, keyboard scan, cursor flash, tape state machine). NMI comes from VIA-1
  CA1 (wired to the **RESTORE key**) and the RS-232 handler. The **VIC chip does
  not generate interrupts** — there are *no raster interrupts* as on the C64; to
  sync to the beam, poll the raster register at $9004 (`vic20-reference.md` §2).
- **Reset vector** at $FFFC/$FFFD points into KERNAL ROM; a cartridge can
  override it via the autostart probe (`vic20-reference.md` §2, §19).

## Memory map

The 64 KB address space on a stock 5 KB machine (`vic20-reference.md` §3;
`1983-vic-20-memory-map.txt`):

| Range | Size | Contents (unexpanded) |
|-------|------|-----------------------|
| `$0000–$00FF` | 256 B | Zero page — BASIC/KERNAL pointers, jiffy clock, CHRGET, current key |
| `$0100–$01FF` | 256 B | 6502 hardware stack (descends from $01FF) |
| `$0200–$03FF` | 512 B | KERNAL/BASIC workspace; input + keyboard buffers; cassette buffer `$033C–$03FB` |
| `$0400–$0FFF` | 3 KB | **Block-0 RAM expansion** (RAM1/2/3) — empty on stock; used by the 3 KB / Super Expander carts |
| `$1000–$1DFF` | 3.5 KB | **User BASIC area** (unexpanded) — programs + variables live here |
| `$1E00–$1FFF` | 512 B | **Screen RAM** (unexpanded) — 22 × 23 = 506 cells |
| `$2000–$3FFF` | 8 KB | **BLK1** — expansion RAM or cartridge ROM |
| `$4000–$5FFF` | 8 KB | **BLK2** — expansion RAM or cartridge ROM |
| `$6000–$7FFF` | 8 KB | **BLK3** — expansion RAM or cartridge ROM |
| `$8000–$8FFF` | 4 KB | **Character ROM** — visible only to the VIC chip, not directly to the CPU |
| `$9000–$900F` | 16 B | **VIC chip registers** |
| `$9110–$911F` | 16 B | **VIA-1** (user port, RS-232, joystick switches 0–2 + fire, RESTORE, IEC ATN, cassette sense) |
| `$9120–$912F` | 16 B | **VIA-2** (keyboard, joystick switch 3, cassette read/write/motor, IEC clock + data) |
| `$9400–$95FF` | 512 B | **Colour RAM** when memory is added to BLK1 (relocated here) |
| `$9600–$97FF` | 512 B | **Colour RAM** on the unexpanded machine (one 4-bit nibble per cell) |
| `$9800–$9BFF` | 1 KB | I/O block 2 (cartridge devices) |
| `$9C00–$9FFF` | 1 KB | I/O block 3 (cartridge devices) |
| `$A000–$BFFF` | 8 KB | **BLK5** — cartridge ROM; KERNAL probes here for the autostart signature |
| `$C000–$DFFF` | 8 KB | **BASIC ROM** (Commodore BASIC v2.0) |
| `$E000–$FFFF` | 8 KB | **KERNAL ROM** + the IRQ/NMI/RESET vectors at the top |

Two consequences worth teaching:

- **Colour RAM is 4-bit nibbles.** Reads leave the high nibble undefined; software
  must `AND #$0F` after reading (`vic20-reference.md` §3).
- **The VIC chip sees a different memory map from the CPU.** Its 14-bit address
  space maps so that custom character data *must* live in CPU RAM $0000–$1FFF —
  it cannot see expansion RAM in BLK1/2/3 (`vic20-reference.md` §3, §4).

## The ~5 KB constraint and memory expansion

Out of the box the VIC-20 reports **3583 BYTES FREE** to BASIC
(`vic20-reference.md` §1, §4). A whole cartridge market grew around expanding it.
The standard configurations (`vic20-reference.md` §4):

| Configuration | Total RAM | Free for BASIC |
|---------------|-----------|----------------|
| Unexpanded | 5 KB | 3583 bytes |
| +3 KB | 8 KB | 6655 bytes |
| +8 KB | 13 KB | 11 775 bytes |
| +16 KB | 21 KB | 19 967 bytes |
| +24 KB | 29 KB | 28 159 bytes |

### Why the screen moves — the defining quirk

On power-up the KERNAL walks RAM upward from $0400 to find the writable region,
then decides the layout (`vic20-reference.md` §4; Programmer's Reference Guide
power-up sequence):

- **No BLK1 RAM** (top-of-RAM < $2100): screen stays at **$1E00**, colour RAM at
  **$9600**.
- **BLK1 RAM present** (top-of-RAM ≥ $2100): the KERNAL **moves the screen to
  $1000** and **colour RAM to $9400**, so BASIC's free area stays contiguous.

So **a program written for an unexpanded VIC will not run on a +8 KB machine** if
it hard-codes screen addresses. Portable code reads the screen page from the
system pointer at **$0288** and computes the base as `$0288 × $0100`
(`vic20-reference.md` §4). This is the single most important architectural fact
for VIC-20 curriculum — teach indirection through it.

> Decide early in the curriculum which configuration units target (commonly
> unexpanded, or a fixed +8 KB), and state it per unit, the way period type-in
> listings always did. <!-- TODO: confirm the target memory configuration policy for VIC-20 units against the curriculum decision once a track plan exists -->

## The VIC chip (6560 NTSC / 6561 PAL)

A single 40-pin part doing video, sound, paddle A/D, and light-pen latching, and
mastering the system bus (`vic20-reference.md` §5). It is **not** the C64's
VIC-II — they share a name and little else (`vic20-reference.md` §17).

### Video

- Default **22 × 23** text cells of 8 × 8 pixels (176 × 184 px); columns, rows,
  and screen origin are all programmable via the registers at $9000–$9005.
- **16 colours.** Standard hi-res (foreground/background per cell) or multi-colour
  mode (bits read in pairs, 4 colours per cell at half horizontal resolution).
- **No sprites and no bitmap mode.** "High resolution" is really programmable
  characters used as a pseudo-bitmap — and with ~5 KB total, practical bitmaps are
  small (`vic20-reference.md` §5, §7).

VIC register map ($9000–$900F): horizontal/vertical origin, columns/rows + char
size, raster read, memory pointers (character + screen base), light-pen X/Y,
paddle X/Y, four voice registers, volume + aux colour, and screen/border/reverse
($900F). Full register-bit detail is in `vic20-reference.md` §6 — cite it rather
than restating. <!-- TODO: pull the exact $9000–$900F bit assignments into a graphics sub-doc from vic20-reference.md §6 + Programmer's Reference Guide when a graphics unit needs them -->

### Sound

Three square-wave tone voices (bass $900A, alto $900B, soprano $900C, staggered
to give ~5 effective octaves) plus one noise voice ($900D), with a shared 4-bit
master volume in $900E (`vic20-reference.md` §8). Audio is mixed into the
composite video signal and played through the TV — there is no separate audio
jack. Note the volume byte's **high nibble is the auxiliary colour**, so volume
writes must preserve it: `(PEEK(36878) AND 240) OR vol`. <!-- TODO: confirm the sound frequency formula and per-voice clock divisors from vic20-reference.md §8 before a sound unit -->

### PAL vs NTSC

Different VIC mask (6561 vs 6560), crystal, CPU clock, frame rate, visible region,
and musical pitch. Pick one at machine instantiation; the CPU clock is *derived*
from the video clock — ~17030 CPU cycles/frame NTSC, ~22132 PAL
(`vic20-reference.md` §16). <!-- TODO: confirm which region Emu198x's machine-commodore-vic-20 core defaults to, and standardise the curriculum on it -->

## I/O at a glance

- **Two 6522 VIAs** ($9110, $9120) handle the keyboard matrix (8 × 8), the
  joystick, the Datassette, the serial IEC bus, the user port, and RS-232
  (bit-banged in software). Full pin wiring in `vic20-reference.md` §9–§14.
- **Joystick:** one Atari-standard DE-9. Up/down/left + fire read from VIA-1
  ($9111 bits 2–5, active low); **right reads from VIA-2 PB7** ($9120 bit 7) —
  the awkward one, because PB7 is shared with the keyboard scan, so reading it
  needs the DDR set and then restored (`vic20-reference.md` §10, §11).
- **KERNAL jump table** at $FF81–$FFF5 — the portable way to do I/O (CHROUT
  $FFD2, CHRIN $FFCF, GETIN $FFE4, etc.); see
  [`../language/6502-quick-reference.md`](../language/6502-quick-reference.md).

## See also

- [reference.md](../reference.md) — platform entry point + key specs.
- [../language/6502-quick-reference.md](../language/6502-quick-reference.md) — instruction set + KERNAL calls.
- `reference/by-system/commodore-vic20/vic20-reference.md` — the full distilled system reference.
- `reference/by-system/commodore-vic20/vic-20-programmers-reference-guide-1st-edition-6th-printing` — primary source of truth.
