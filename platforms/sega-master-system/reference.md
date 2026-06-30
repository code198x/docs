# Sega Master System

Sega's first console to sell worldwide. Built on the same off-the-shelf 8-bit
silicon family as its rivals — a Zilog Z80A CPU, a Texas Instruments-derived
video chip, and a Texas Instruments sound chip — the Master System lost the North
American console war to Nintendo but became a genuine phenomenon in **Europe** and
especially **Brazil**, where Tectoy kept manufacturing and selling it well into
the 2010s.

For the curriculum this is a milestone: the **first console of the next tier**.
Unlike the home computers (Spectrum, C64, Amiga), there is **no operating system,
no BASIC, no editor** sitting between you and the metal. A cartridge holds your
program, the machine powers on, and your code runs. You talk to the video and
sound chips directly through the Z80's I/O ports. This is a purer, more direct
relationship with the hardware than any home computer — and a deliberate step up
in the learning arc.

Two pieces of shared chip lineage are worth surfacing early, because they connect
this platform to others learners may meet:

- The **VDP** (Sega 315-5124) is a descendant of the **TMS9918A** — the same video
  architecture family used by the **MSX** and ColecoVision. Learners who later
  meet the MSX will recognise the tile/sprite model.
- The **PSG** (SN76489) is the *same* sound chip used in the **BBC Micro** (and
  ColecoVision, and the IBM PCjr). Knowledge of three square-wave channels plus
  noise carries straight across.

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | **Asm198x** (Z80 core) | Z80 opcodes complete and dialect-validated. See [TOOLCHAIN-RESEARCH.md](./TOOLCHAIN-RESEARCH.md). |
| Emulator / capture | **Emu198x** (`machine-sega-master-system` core) | Screenshots and video via the Emu198x capture surface. |
| Output container | `.sms` cartridge ROM image | **Roadmap.** Asm198x emits a flat `.bin` today; for a fixed-size cartridge ROM the gap is small (a padded flat binary is close to a `.sms`). See [TOOLCHAIN-RESEARCH.md](./TOOLCHAIN-RESEARCH.md). |
| ROMs | **BIOS optional** | Most Master Systems shipped a BIOS, but many late Master System II units shipped without one and boot the cartridge directly. A learner cartridge must initialise its own hardware so it runs either way. <!-- TODO: confirm Emu198x's machine-sega-master-system BIOS-handling default against the Emu198x core --> |

> No Docker images. Builds target Asm198x and capture targets Emu198x, per the
> [dev-tooling-migration decision](../../../../decisions/code198x-dev-tooling-migration.md).

## Key specifications

| Component | Detail | Source |
|-----------|--------|--------|
| CPU | Zilog **Z80A** @ 3.579545 MHz (NTSC) / 3.546893 MHz (PAL) | `sms-reference.md` § System Architecture, § Clock Topology |
| System RAM | **8 KB** at `$C000-$DFFF` (mirrored to `$FFFF`) | `sms-reference.md` § CPU Memory Map |
| VDP | **Sega 315-5124** — TMS9918A-derived, adds **Mode 4**; owns 16 KB of dedicated VRAM | `sms-reference.md` § System Architecture, § VDP Integration |
| Video | 256×192 pixels, Mode 4; 64-colour master palette, 32 colours on-screen (2×16 CRAM) | `sms-reference.md` § Family Overview, § VDP Integration |
| PSG | **SN76489** — 3 square-wave tone channels + 1 noise channel, write-only | `sms-reference.md` § PSG (SN76489) Integration |
| FM (optional) | Yamaha **YM2413** (OPLL) — Japanese SMS / Mark III FM unit only; absent on Western units | `sms-reference.md` § YM2413 FM Extension |
| Cartridge | Up to 4 MB (32 Mbit) via the Sega standard mapper; first 1 KB never paged | `sms-reference.md` § CPU Memory Map, § Sega Standard Mapper |

The compendium records the SG-1000 ancestry plainly: "an 8-bit Zilog Z80 CPU
running at 3.58 MHz, with a Texas Instruments TMS9928A video processor and a Texas
Instruments SN76489 sound processor … all found in the ColecoVision"
(`sega-mastersystem-compendiumbook-pdf` p. 446, McFerran overview). The Mark III
swapped in Sega's own Mode-4-capable VDP; the Western Master System is a re-cased
Mark III (`sms-reference.md` § Family Overview).

## Assembly dialect

**Z80** assembly. The SMS shares its CPU with the ZX Spectrum, so the instruction
set, registers, and addressing modes are identical — what differs is *the machine
around the CPU*: cartridge memory map, the VDP, the PSG, and I/O-port access
instead of OS calls. Language detection in `CodeFromFile` maps SMS paths to `z80`
highlighting (same as Spectrum). See
[language/z80-quick-reference.md](./language/z80-quick-reference.md).

## Gotchas

- **No OS, no BASIC.** You initialise everything yourself — stack pointer, mapper
  registers, VDP mode, interrupt mode. A real machine may or may not have a BIOS
  to do this for you, so the cartridge must not depend on one. (`sms-reference.md`
  § Controller Protocol → "Reset and bus state", § BIOS Variants.)
- **The first 1 KB of ROM (`$0000-$03FF`) is never paged out.** The Z80's RST and
  interrupt vectors live there, so a page swap can never make them vanish.
  (`sms-reference.md` § CPU Memory Map.)
- **The VDP is the timing master**, not the CPU — the VDP divides the master
  crystal and feeds the Z80 its clock. (`sms-reference.md` § Clock Topology.)
- **You reach the VDP and PSG through I/O ports, not memory.** VRAM is *owned by
  the VDP*; the CPU has no direct access and must go through the data/control ports
  at `$BE`/`$BF`. (`sms-reference.md` § VDP Integration.)
- **The PSG is write-only** — there is no status read, so sound updates must be
  timed against the frame interrupt. (`sms-reference.md` § PSG Integration.)
- **Western units have no FM chip.** Writing to `$F0-$F2` does nothing on a
  Western Master System; the curriculum targets PSG audio. (`sms-reference.md`
  § YM2413 FM Extension.)

## Sub-documents

- [TOOLCHAIN-RESEARCH.md](./TOOLCHAIN-RESEARCH.md) — assembler/emulator landscape and the output-container situation.
- [hardware/ARCHITECTURE.md](./hardware/ARCHITECTURE.md) — memory map, mapper, VDP, PSG, and chip lineage.
- [language/z80-quick-reference.md](./language/z80-quick-reference.md) — Z80 instruction reference plus SMS I/O ports.

## Reference library

Primary sources live in the shared reference library (the source of truth — this
page is curriculum-flavoured and cites it):

- `reference/by-system/sega-master-system/sms-reference.md` — system-level
  reference (memory map, mappers, I/O ports, VDP/PSG integration, controllers).
- `reference/by-system/sega-master-system/sega-mastersystem-compendiumbook-pdf.md`
  — *SEGA Master System: a visual compendium* (Bitmap Books, 2019); history,
  developer interviews, Brazilian-market chapter. Layout-aware extract under
  `.docling/`.
- `reference/by-system/sega-master-system/magazines.md` — period magazine index.

<!-- TODO: when chip-level companion references (vdp-sms-reference.md,
psg-sn76489-reference.md) land in the library, cite them here and from
hardware/ARCHITECTURE.md -->
</content>
</invoke>
