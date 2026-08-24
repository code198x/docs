# MSX Architecture

A curriculum-flavoured tour of the MSX1 hardware: how memory is laid out, what
the CPU is, how the screen works, and how sound is made. The aim is to give you
enough of a mental model to start writing code and to know which primary-source
section to open when you need the exact bits.

> **Source of truth:**
> `reference/by-system/msx/msx-reference.md`
> (the MSX System Reference) and the
> `reference/by-system/msx/msx-technical-data-book.md`.
> Section numbers below (e.g. §3) refer to the System Reference. Specifics this
> skeleton has not yet pinned down are flagged `TODO`.

## The big picture

An MSX1 is four chips working together over the Z80's buses:

- **Z80A CPU** — runs your code.
- **TMS9918A VDP** — the video chip, with its own private 16 KB of VRAM.
- **AY-3-8910 PSG** — the sound chip.
- **8255 PPI** — the "glue" chip that handles slot switching, keyboard scanning,
  cassette, the CAPS lamp, and a 1-bit click.

The VDP, PSG, and PPI all live in the **I/O port space** — you reach them with
`IN`/`OUT`, not by reading and writing memory addresses. The one big exception to
"everything is simple" is memory itself, because of the slot system.

(`msx-reference.md` §2.1.)

## CPU

- **Zilog Z80A** (or a compatible second-source part) at **3.579545 MHz** — the
  NTSC colour-subcarrier frequency, shared with the video chip so the two stay
  phase-locked.
- The standard MSX1 motherboard inserts **one wait state on every M1
  (instruction-fetch) cycle**. A 4-T-state `LD A,B` becomes 5; averaged over real
  code, throughput drops ~17–21% versus a bare Z80A. Memory and I/O cycles are
  unaffected.
- Interrupts run in **IM 1** (jump to `$0038`); the source is the VDP's vertical
  blank. There is no standard use of NMI.

The wait state is the single most important timing fact for an MSX programmer
coming from another Z80 machine — see the gotcha in
[../reference.md](../reference.md). (`msx-reference.md` §§2.2–2.4.)

## Memory map and the slot system

The Z80 can address **64 KB**. MSX divides that into **four 16 KB pages**:

| Page | Address range | Typical contents (MSX1) |
|------|---------------|-------------------------|
| 0 | `$0000–$3FFF` | MSX BIOS ROM |
| 1 | `$4000–$7FFF` | MSX-BASIC ROM (or a cartridge) |
| 2 | `$8000–$BFFF` | RAM (or a cartridge) |
| 3 | `$C000–$FFFF` | RAM (the BIOS work area lives at the top) |

The clever part: each of those four pages can be independently routed to one of
**four primary slots** (slot 0–3). So the 64 KB the CPU sees is assembled, page by
page, from up to four different physical sources. By convention on MSX1, slot 0 is
BIOS+BASIC ROM, slots 1 and 2 are the cartridge slots, and slot 3 is RAM.

A primary slot can itself be **expanded** into four secondary sub-slots, each with
its own four pages — multiplying the addressable memory up to 1 MB while still
only ever showing 64 KB to the CPU at once. This is how an 8-bit machine survived
into the era of large RAM without breaking binary compatibility.

**How slot switching works:**

- The **primary slot register** is PPI port A, at **I/O port `$A8`**. Two bits per
  page select that page's slot: bits 0–1 = page 0, bits 2–3 = page 1, bits 4–5 =
  page 2, bits 6–7 = page 3. `OUT ($A8),A` writes the mapping.
- For an expanded slot, the **sub-slot register** lives at **memory address
  `$FFFF`** within that slot's page 3, with the same two-bits-per-page layout. It
  reads back *inverted*, which is how software detects whether a slot is expanded.
- The BIOS provides inter-slot primitives — `RDSLT` (`$000C`), `WRSLT` (`$0014`),
  `CALSLT` (`$001C`), `ENASLT` (`$0024`) — so code in one slot can reach memory or
  routines in another.

> **Curriculum note.** Slot switching is the genuinely unfamiliar part of MSX for
> most newcomers. Early units can stay within a single RAM configuration and lean
> on BIOS calls; slots become essential only when you grow past one cartridge page
> or want to call across slots by hand.

(`msx-reference.md` §3.)

<!-- TODO: confirm the exact default slot layout the Emu198x machine-msx core boots
     with (which slot holds RAM, whether slot 3 is expanded) against the core and
     msx-technical-data-book.md, so example code's org/slot assumptions match. -->

## Video — the TMS9918A VDP

The VDP is a separate processor with its own **16 KB of VRAM** that the CPU cannot
address directly. You move data in and out through two I/O ports:

- **`$98`** — VRAM data (read or write)
- **`$99`** — register / VRAM-address / status

Two things to internalise:

- To write a VDP register, send the data byte to `$99`, then the register number
  with bit 7 set to `$99`.
- Reading status port `$99` **clears the VBlank flag and dismisses the frame
  interrupt** as a side effect — essential for a working interrupt handler.

The TMS9918A has **8 write-only registers (R0–R7)** controlling display mode, table
base addresses, and colour. (`msx-reference.md` §4.1.)

### Screen modes (MSX1)

`SCREEN n` in BASIC maps to a VDP mode:

| SCREEN | VDP mode | Resolution | Colour | Notes |
|--------|----------|------------|--------|-------|
| 0 | Text 1 | 40×24 text | 2 | No sprites |
| 1 | Graphic 1 | 256×192, 32×24 cells | 16 (one fg/bg pair per group of 8 chars) | The default game mode |
| 2 | Graphic 2 | 256×192 | 16 (one pair per 8-pixel row) | The "high-resolution" mode; the banded look comes from per-row colour |
| 3 | Multicolour | 64×48 blocks | 16 | Rarely used |

MSX2 and later add SCREEN 4–12 (more colours, higher resolution, YJK) on the
V9938/V9958 — see `msx-reference.md` §4.4. The curriculum begins on MSX1's
SCREEN 1 / SCREEN 2.

### Sprites (MSX1)

- **32 sprites**, each one colour, **8×8 or 16×16** pixels (R1 selects size, and a
  magnification bit doubles each pixel).
- **Maximum 4 sprites per scanline** — the fifth on a line is dropped, and the VDP
  records the "fifth sprite" status. Sprite flicker on busy lines is a hardware
  fact of life, not a bug.
- A sprite's Y coordinate of **209** hides it and every later sprite — the standard
  way to "switch off" trailing sprites.

(`msx-reference.md` §§4.1, 4.5.)

### Palette (MSX1)

The TMS9918A has a **fixed 16-colour palette** — you choose colour *indices*, not
RGB values. Index 0 is transparent. The exact colours come from the analog
colour-burst reference and vary slightly between chip revisions; MSX2's V9938 keeps
these as defaults but lets you reprogram them. (`msx-reference.md` §4.6.)

<!-- TODO: if a unit needs exact palette RGB values, cite the table in
     msx-reference.md §4.6 rather than re-listing approximate hex here. -->

## Sound — the AY-3-8910 PSG

The Programmable Sound Generator gives you **3 square-wave tone channels, 1 noise
generator, and a hardware envelope** — the same chip family as the Spectrum 128,
Amstrad CPC, and Atari ST.

- I/O ports: **`$A0`** register select (write), **`$A1`** data (write), **`$A2`**
  data (read).
- **16 registers (R0–R15):** tone periods for channels A/B/C (12-bit each), noise
  period, a mixer/IO-direction register, per-channel amplitude, envelope period
  and shape, and two I/O ports.
- Clocked at **CPU/2 = 1.7897725 MHz**.
- The mixer register (R7) uses **inverted** logic: a set bit *disables* that
  channel.
- The PSG's I/O ports double as the **joystick interface** (read via R14, with R15
  bit 6 selecting which of the two joystick ports is routed in).

The BIOS exposes the PSG via `WRTPSG` (`$0093`) and `RDPSG` (`$0096`); BASIC via
`SOUND` (direct register access) and `PLAY` (an MML music language). There is also
a separate **1-bit click** output on the PPI (BASIC's `BEEP`), mixed in alongside
the PSG. (`msx-reference.md` §§5.1–5.2, 7.)

<!-- TODO: add a worked PSG note-frequency example (tone period from desired Hz)
     when the first sound unit is written; formula base is in msx-reference.md §5.1. -->

## Where to go next

- [../language/z80-quick-reference.md](../language/z80-quick-reference.md) — the Z80
  instruction set and the MSX BIOS calling conventions (how to actually drive the
  hardware above).
- `reference/by-system/msx/msx-reference.md` — the
  full hardware reference, including the BIOS entry table (§12), cartridge mappers
  (§8.2), and the keyboard matrix (§6.2).
