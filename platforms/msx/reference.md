# MSX

The MSX was not one machine — it was a *standard*. In 1983 Microsoft and ASCII
Corporation published a specification fixing the CPU, video chip, sound chip,
memory layout, BIOS entry table, cartridge connector, and BASIC dialect, so that
a single cartridge would run unchanged on machines from roughly thirty different
makers — Sony, Panasonic, Toshiba, Yamaha, Philips, Sanyo, Daewoo, and more. It
is the closest the 8-bit home-computer world ever came to an IBM-PC-style common
platform, and it was huge in Japan, Brazil, the Netherlands, Korea, and Spain
even though it barely registered in the UK or USA.

For our purposes that standard is a gift: the hardware underneath is well
documented and consistent, and the same Z80 you might already know from the ZX
Spectrum sits at its heart. If you have written Spectrum assembly, you are most
of the way to writing MSX assembly — the CPU is identical; what changes is how
you talk to the screen, the sound chip, and memory.

This page is the curriculum-flavoured entry point. It summarises the facts you
need to start and points at the primary reference library for the detail. It
covers MSX1 (the 1983 baseline) first, because that is where the curriculum
begins; later generations (MSX2, MSX2+, TurboR) are noted where they matter.

> **Source of truth.** Hardware facts below are distilled from the primary
> reference library, chiefly
> [`msx-reference.md`](../../../../reference/by-system/msx/msx-reference.md)
> (the MSX System Reference), with the
> [Sony MSX Technical Data Book](../../../../reference/by-system/msx/msx-technical-data-book.md)
> and the
> [Sony MSX-BASIC Programming Reference Manual](../../../../reference/by-system/msx/sony-msx-basic-programming-reference-manual.md)
> behind it. When a fact here and a fact there disagree, the library wins. Deep
> specifics this skeleton has not yet pinned down are flagged inline as TODOs.

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | **Asm198x** (Z80 core) | `asm198x` single binary; Z80 opcode set complete and dialect-validated. Not a Docker image — see [TOOLCHAIN-RESEARCH.md](./TOOLCHAIN-RESEARCH.md). |
| Output container | **Flat `.bin` today** | MSX cartridge `.rom`, MSX-DOS `.com`, and cassette `.cas` containers are roadmap, not yet emitted. See [TOOLCHAIN-RESEARCH.md](./TOOLCHAIN-RESEARCH.md) and the [Asm198x packaging roadmap](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md). |
| Emulator | **Emu198x** (`machine-msx` core) | Core exists; capture parity (screenshot/video) is the integration gate. |
| ROMs | **System BIOS required** | Unlike the Spectrum, an MSX needs a machine BIOS (and BASIC ROM) to boot. These are vendor-specific and not distributable; the emulator supplies/locates one. C-BIOS (an open-source BIOS replacement) is the licence-clean option for booting cartridge software. |

This platform is being scaffolded directly onto the Asm198x / Emu198x path —
there is no MSX Docker image, by design. The dev-tooling migration decision
([`code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md))
applies: new platforms start on the family tools rather than spawning a fifth
Docker toolchain.

## Build command

The exact invocation is settled once the MSX output container lands. Until then
Asm198x assembles Z80 source to a flat binary at the program's `org` address:

```bash
# Shape, not a frozen command — flat .bin output, no container wrapping yet.
asm198x asm code-samples/msx/assembly/input.asm -o code-samples/msx/assembly/output.bin
```

<!-- TODO: confirm final asm198x CLI flags + MSX target name once the .rom/.com/.cas
     container work lands; mirror the C64/NES rows in
     Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md when done. -->

## Key specifications (MSX1)

| Component | Detail |
|-----------|--------|
| CPU | Zilog Z80A (or compatible — Sharp LH0080A, NEC D780C) |
| Clock | 3.579545 MHz (the NTSC colour-subcarrier frequency), with **one wait state per M1 fetch** — about 17–21% slower than a bare Z80A |
| RAM | 8–64 KB (most software assumes 64 KB) |
| Video | Texas Instruments **TMS9918A** VDP, 16 KB dedicated VRAM, fixed 16-colour palette |
| Sound | General Instrument **AY-3-8910** PSG — 3 tone channels + 1 noise + envelope (Yamaha YM2149 second-source) |
| I/O | Intel **8255** PPI — slot select, keyboard scan, cassette, CAPS lamp, 1-bit click |
| Cartridge | 50-pin standardised edge connector |

Source:
[`msx-reference.md`](../../../../reference/by-system/msx/msx-reference.md) §§1–2,
4–6.

Later generations keep the Z80A and AY-3-8910 but upgrade the video: MSX2 uses
the Yamaha V9938 (programmable palette, more colours, a hardware blitter, 80-column
text), and MSX2+/TurboR use the V9958 (hardware horizontal scroll, YJK colour
modes). The TurboR adds the faster, Z80-binary-compatible R800 CPU. The
curriculum starts on MSX1; see
[`msx-reference.md`](../../../../reference/by-system/msx/msx-reference.md) §§4.2–4.4
and §15 for the deltas.

## Assembly dialect

Standard **Z80** assembly — the same instruction set as the ZX Spectrum, built
by the Asm198x Z80 core (opcode-complete and dialect-validated). What makes MSX
code *MSX* is not the CPU but the conventions around it:

- You reach the screen, sound, keyboard, and joystick through **BIOS calls** at
  fixed addresses (e.g. `CALL $00A2` to print a character), not by poking
  hardware directly — though you can do both.
- The VDP, PSG, and PPI live in the **I/O port space** (`IN`/`OUT`), not the
  memory map.
- Memory is **slot-banked** (see [ARCHITECTURE.md](./hardware/ARCHITECTURE.md)),
  so where your code and data live matters more than on a flat-memory machine.

See [language/z80-quick-reference.md](./language/z80-quick-reference.md) for the
instruction-set summary and the MSX BIOS calling conventions.

## Reference library links

The primary, source-of-truth documents for MSX hardware and BASIC:

- [`reference/by-system/msx/msx-reference.md`](../../../../reference/by-system/msx/msx-reference.md)
  — MSX System Reference (all four generations; the main hardware document)
- [`reference/by-system/msx/msx-technical-data-book.md`](../../../../reference/by-system/msx/msx-technical-data-book.md)
  — Sony MSX Technical Data Book (342 pp, OCR)
- [`reference/by-system/msx/sony-msx-basic-programming-reference-manual.md`](../../../../reference/by-system/msx/sony-msx-basic-programming-reference-manual.md)
  — Sony MSX-BASIC Programming Reference Manual (200 pp)
- [`reference/by-system/msx/index.md`](../../../../reference/by-system/msx/index.md)
  — the index for the above

## Gotchas

- **The M1 wait state.** Every instruction fetch costs one extra T-state on a
  standard MSX1, so timing loops tuned on a bare Z80 (or a Spectrum) run ~20%
  slow here. Some MSX2+/TurboR machines drop the wait state, so the *same* code
  then runs faster. Do not hard-code cycle counts across machines without
  checking. (`msx-reference.md` §2.4.)
- **An MSX needs a BIOS to boot.** Unlike the Spectrum, you cannot run bare
  cartridge code without a system BIOS in slot 0. The emulator must supply one;
  C-BIOS is the open-source option.
- **PAL vs NTSC changes the frame rate, not the CPU clock.** The interrupt rate
  follows the VDP's vertical blank — 60 Hz on NTSC machines, 50 Hz on PAL. Code
  that counts frames for timing behaves differently between regions.
  (`msx-reference.md` §2.3.)
- **Talk to the VDP through ports, with the right handshake.** Reading status
  port `$99` clears the VBlank flag as a side effect; forget that and your VBlank
  handler will not behave. (`msx-reference.md` §4.1.)
- **Reading port `$99` also dismisses the frame interrupt** — see above; it is
  the single most common source of "the interrupt fires forever" bugs.

## Sub-documents

- [hardware/ARCHITECTURE.md](./hardware/ARCHITECTURE.md) — memory map, the slot
  system, CPU, VDP screen modes, PSG sound
- [language/z80-quick-reference.md](./language/z80-quick-reference.md) — Z80
  instruction-set summary and MSX BIOS calling conventions
- [basic.md](./basic.md) — MSX-BASIC overview
- [TOOLCHAIN-RESEARCH.md](./TOOLCHAIN-RESEARCH.md) — assembler/emulator landscape
  and the output-container situation
