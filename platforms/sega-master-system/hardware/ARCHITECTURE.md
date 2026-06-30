# Sega Master System — Architecture

**Purpose:** Curriculum-flavoured map of the SMS hardware a learner needs to write
a first game — memory layout, the cartridge mapper, the VDP, and the PSG.
**Audience:** Programmers new to the SMS (assumes general programming ability and,
ideally, prior Z80 exposure from the Spectrum track).
**Source of truth:** `reference/by-system/sega-master-system/sms-reference.md` and
the *SEGA Master System: a visual compendium* extract. Facts below cite those;
where a deeper specific isn't yet confirmed it carries a `TODO`.

---

## The shape of the machine

Five chips, no operating system (`sms-reference.md` § System Architecture):

| Chip | Role |
|------|------|
| **Zilog Z80A** | 8-bit CPU @ 3.579545 MHz (NTSC) / 3.546893 MHz (PAL) |
| **Sega VDP (315-5124)** | Video Display Processor; owns 16 KB of dedicated VRAM |
| **SN76489** | Programmable Sound Generator — 3 tone + 1 noise channel |
| **YM2413** (optional) | FM synthesis — Japanese SMS / Mark III FM unit only |
| **8 KB SRAM** | System work RAM |

A defining point: **the VDP is the timing master.** It divides the master crystal
and feeds the Z80 its clock (Z80 = master ÷ 15). So when modelling or reasoning
about the system, the VDP drives the CPU, not the other way around
(`sms-reference.md` § Clock Topology).

The other defining point: **there is no OS layer.** On the home computers a ROM
routine or BASIC sits between your code and the hardware. Here, your cartridge code
*is* the system software. You set up the stack, the mapper, the VDP mode, and the
interrupt mode yourself (`sms-reference.md` § Controller Protocol → "Reset and bus
state").

---

## CPU memory map

The Z80 sees a flat 64 KB address space. Everything below `$C000` is the
**cartridge**; RAM and the mapper control window are at the top
(`sms-reference.md` § CPU Memory Map):

```
$0000-$03FF  Cartridge ROM, fixed page 0 — NEVER paged out
              holds Z80 RST vectors ($00/$08/.../$38) and the IM 1 vector ($0038)
$0400-$3FFF  Cartridge ROM, mapper slot 0   (selected by $FFFD)
$4000-$7FFF  Cartridge ROM, mapper slot 1   (selected by $FFFE)
$8000-$BFFF  Cartridge ROM, mapper slot 2   (selected by $FFFF) — or cart RAM
$C000-$DFFF  System RAM (8 KB)
$E000-$FFFB  System RAM mirror
$FFFC        Mapper control register (cart-RAM / page-2 bits)
$FFFD        Mapper page register for slot 0
$FFFE        Mapper page register for slot 1
$FFFF        Mapper page register for slot 2
```

Two things to fix in mind:

- **The CPU sees no RAM below `$C000`.** There is only 8 KB of system RAM, mirrored
  into the top of the address space. Code commonly puts the stack high in RAM (e.g.
  `$DFF0`) so it stays clear of the mapper bytes near `$FFFC`.
- **`$0000-$03FF` is special.** The first 1 KB of cartridge ROM is wired so the
  mapper can never page it out — the interrupt and restart vectors must always be
  present. A mapper page-swap that hit those addresses would crash the machine
  (`sms-reference.md` § CPU Memory Map, § Sega Standard Mapper → "Page-zero
  protection").

---

## The cartridge mapper

The console only has 8 KB of RAM; cartridges can hold up to 4 MB. The bridge is a
**mapper** — and the mapper lives *on the cartridge*, not in the console. The cart
slot presents the raw Z80 bus and the cartridge decides what to do with it
(`sms-reference.md` § System Architecture → "What lives on the cartridge vs the
console").

The **Sega standard mapper** (used by virtually every official game) gives three
16 KB banking slots, each driven by a register in the high RAM mirror
(`sms-reference.md` § Sega Standard Mapper):

| Register | Controls | Reset value |
|----------|----------|-------------|
| `$FFFC` | cart-RAM enable + page-2 high bits | `$00` |
| `$FFFD` | page into slot 0 (`$0000-$3FFF`, bottom 1 KB excepted) | `$00` |
| `$FFFE` | page into slot 1 (`$4000-$7FFF`) | `$01` |
| `$FFFF` | page into slot 2 (`$8000-$BFFF`) | `$02` |

Pages are 16 KB, page numbers are 8-bit → max 256 × 16 KB = **4 MB**. Setting bit 4
of `$FFFC` turns slot 2 into battery-backed cartridge save RAM (used by *Phantasy
Star*, *Wonder Boy III*, etc.).

**For a first game this barely matters:** a learner cartridge that fits in 32 KB
needs no banking at all — but it still must write the default page values
(`0/1/2`) into `$FFFD-$FFFF` at startup, because a no-BIOS console leaves those
bytes undefined (`sms-reference.md` § Sega Standard Mapper → "Reset behaviour").

> Other mappers exist (Codemasters, several Korean variants) but none appear in
> the official Sega catalogue and none concern the curriculum.
> (`sms-reference.md` § Codemasters Mapper, § Korean Mapper Variants.)

---

## The VDP (Sega 315-5124) — and its lineage

The Video Display Processor is a **Sega evolution of the Texas Instruments
TMS9918A** (`sms-reference.md` § System Architecture, § VDP Integration). This is
worth dwelling on for cross-platform context:

- The **TMS9918/9918A family** is the same video architecture used by the **MSX**
  and ColecoVision. The SG-1000 (the SMS's direct ancestor) used a stock
  TMS9928A; the Mark III added Sega's own VDP with a new graphics mode
  (`sega-mastersystem-compendiumbook-pdf` p. 446, p. 464).
- Sega's addition is **Mode 4** — the SMS-native graphics mode (256×192,
  tile-based, with a 64-colour master palette and per-tile palette selection).
  The legacy TMS9918A modes 0–3 still exist and are what makes SG-1000
  backwards-compatibility work, but **no commercial SMS game uses them**
  (`sms-reference.md` § VDP Integration → "Mode 4").

Key integration facts (`sms-reference.md` § VDP Integration):

- **VRAM (16 KB) is owned by the VDP.** The CPU has no direct access — all VRAM
  reads/writes go through the VDP **data port `$BE`** after setting an address via
  the **control port `$BF`**.
- The control port takes **two-byte commands**; the top two bits of the second
  byte select the operation (set VRAM read address / set VRAM write address /
  write a VDP register / set CRAM palette address).
- **Frame interrupt (vblank)** and **line interrupt** are both raised by the VDP
  on the Z80's `/INT`. The frame interrupt is cleared by reading the status
  register at `$BF`. Line interrupts (VDP register 10) drive raster effects like
  status-bar splits and parallax.
- The Z80 runs in **IM 1**: the SMS provides no interrupt vector on the data bus,
  so the interrupt jumps to the fixed `$0038` (which is in the never-paged first
  1 KB).

```
; Set VRAM write address to $3F00 (sms-reference.md § VDP Integration)
    LD A, $00         ; low byte
    OUT ($BF), A
    LD A, $7F         ; $40 = "VRAM write" | $3F = high byte
    OUT ($BF), A
; subsequent OUT ($BE), A writes auto-increment through VRAM
```

VDP status register bits, read at `$BF` (reading clears the sticky flags):

| Bit | Meaning |
|-----|---------|
| 7 | Frame interrupt pending |
| 6 | Sprite overflow (>8 sprites on a scanline) |
| 5 | Sprite collision |
| 4–0 | Fifth-overflowing-sprite number (TMS9918A legacy) |

<!-- TODO: confirm Mode 4 detail (name/sprite table layout, CRAM palette format,
sprite size/count limits) against a chip-level VDP companion reference when it
lands in reference/by-system/sega-master-system/ -->

---

## The PSG (SN76489) — also shared silicon

The sound chip is the Texas Instruments **SN76489** — the *same* PSG used in the
**BBC Micro**, ColecoVision, and the IBM PCjr (`sms-reference.md` § PSG (SN76489)
Integration). Anyone who learns SMS sound has learned BBC Micro sound.

What matters at the system level:

- **Three square-wave tone channels + one noise channel.** Tone channels are
  10-bit dividers off the 3.58 MHz clock; noise is selectable periodic / white.
- **Write-only.** You stream latch/data bytes to any port in `$40-$7F` (most code
  uses `$7F`). There is **no status read and no interrupt** — so a music engine
  must be driven from the frame interrupt (a "music tick" at 50/60 Hz).
- **Mono on the Master System.** (The Game Gear adds stereo panning via port
  `$06`; not relevant to SMS curriculum.)

```
; A PSG write is just an OUT to $7F (sms-reference.md § PSG Integration)
    LD A, $9F         ; latch: channel 0, volume off (example byte)
    OUT ($7F), A
```

<!-- TODO: confirm SN76489 latch/data byte format (tone vs volume vs noise
register encoding) against a chip-level PSG companion reference when it lands -->

---

## FM audio (YM2413) — Western units don't have it

The Yamaha YM2413 ("OPLL") adds nine FM channels, but it is **only present on the
Japanese Master System and the Mark III FM Sound Unit** — **Western Master
Systems do not have the chip**, and writes to its ports (`$F0-$F2`) do nothing
(`sms-reference.md` § YM2413 FM Extension). The curriculum targets **PSG audio**
so games run on the worldwide hardware learners are most likely to emulate.

---

## Startup checklist (no-OS boot)

Because a real machine may have no BIOS, a cartridge must do its own setup. The
canonical prologue (`sms-reference.md` § Controller Protocol → "Reset and bus
state"):

1. Set the **stack pointer** high in RAM (e.g. `$DFF0`).
2. Write `$00`, `$01`, `$02` to `$FFFD`, `$FFFE`, `$FFFF` (default mapper pages).
3. Configure the **VDP** (Mode 4, enable display/sprites, scroll = 0).
4. Set **IM 1** and `EI`.

<!-- TODO: turn this into a worked, building startup sample under
code-samples/sega-master-system/assembly/ once the Asm198x .sms output path and
Emu198x capture parity are confirmed -->

---

## Chip-lineage summary (cross-platform hooks)

| Chip | Shared with | Carries across |
|------|-------------|----------------|
| Z80A CPU | **ZX Spectrum** | identical instruction set, registers, addressing |
| VDP (315-5124) | **MSX**, ColecoVision (TMS9918A family) | tile/sprite video model |
| SN76489 PSG | **BBC Micro**, ColecoVision, PCjr | 3 square + 1 noise sound model |

This shared lineage is a deliberate teaching asset: the SMS is a console-shaped
recombination of chips a learner may already have met, presented without an OS in
the way.
</content>
