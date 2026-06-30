# Sega Master System — Toolchain Research

**Purpose:** Record the assembler/emulator landscape for the SMS and explain why
Code198x builds onto **Asm198x** + **Emu198x** rather than a third-party chain.
This is research, not a build recipe — it captures *why* the choices were made and
what gaps remain.

**Status:** Scaffold. The SMS is being scaffolded directly onto the Asm198x /
Emu198x path per the
[dev-tooling-migration decision](../../../../decisions/code198x-dev-tooling-migration.md);
there is no legacy Docker toolchain to retire here (unlike the launch platforms).

---

## CPU and the short version

The Master System CPU is a **Zilog Z80A** — the same processor as the ZX
Spectrum. Asm198x's **Z80 core is complete and dialect-validated**, so the
assembler side is effectively already solved: the same core that builds Spectrum
code builds SMS code. What is SMS-specific is *not the CPU* but the output
container and the capture/emulation core.

---

## Assembler landscape (Z80)

| Tool | Notes | Verdict for Code198x |
|------|-------|----------------------|
| **Asm198x (Z80 core)** | Family assembler. Z80 opcodes complete; dialect validated against `pasmo`/`pasmonext` and `sjasmplus`. Single binary, cross-platform, no dead-OS dependency. | **Target.** |
| **WLA-DX** | The de-facto SMS homebrew assembler; rich SMS support (`.sms` output, header directives, banking). Widely used in the scene. | Reference only — informs what a complete SMS output path should produce. |
| **sjasmplus** | Strong Z80 assembler, popular for Spectrum/SMS; one of Asm198x's Z80 dialect validation references. | Reference only (validation peer). |
| **pasmo / pasmonext** | Z80 assembler used by the Spectrum Docker toolchain; the other Z80 dialect validation reference. | Reference only (validation peer). |

**Why Asm198x is the target:** one toolchain across the whole family, no Docker
image and no emulated dead OS to run a period assembler, and a Z80 core already
proven on the Spectrum. The marginal cost of adding the SMS is the *output
container*, not the assembler.

The CPU/dialect status is recorded in the Asm198x roadmap — Z80 is marked done
(`Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md` § CPU / assembler
roadmap).

---

## Emulator / capture landscape

| Tool | Notes | Verdict for Code198x |
|------|-------|----------------------|
| **Emu198x (`machine-sega-master-system`)** | Family emulator. The SMS core exists. Provides the scriptable/MCP capture surface used for curriculum screenshots and video. | **Target.** |
| **Emulicious** | Highly accurate SMS/GG/Game Boy emulator with an excellent debugger; a scene standard for development. | Reference only (accuracy/debugging precedent). |
| **MEKA** | Omar Cornut's emulator; its development notes are cited in the library for VDP/mapper edge cases. | Reference only (documentation source). |
| **Emulator (BIZ/Mednafen cores, etc.)** | Various general-purpose multi-system emulators include SMS cores. | Reference only. |

**Integration gate:** the open question is **capture parity** — confirming the
`machine-sega-master-system` core renders and captures a learner cartridge
faithfully (correct Mode 4 output, palette, sprites; clean screenshot and video
through the Emu198x capture path). That verification is the gate before SMS units
can ship with captured media.

<!-- TODO: confirm machine-sega-master-system capture parity (screenshot + video)
and BIOS-handling default against the Emu198x core; file findings as a Code198x
issue / Emu198x issue per the emulator-work-routing convention -->

---

## Output container — the honest situation

This is the one real gap, and it is **small** for a console.

- **Today:** Asm198x emits a **flat `.bin`** (the assembled bytes at `org`).
- **Target:** the SMS cartridge ROM image, conventionally **`.sms`**.
- **The gap is narrow.** An SMS cartridge ROM is, physically, a fixed-size ROM
  chip. A `.sms` file is essentially the raw ROM image — there is no complex
  container framing like the Spectrum `.sna` snapshot (which serialises CPU
  registers + full memory state) or the C64 `.prg` load-address prefix. For a
  fixed-size cartridge, **a flat binary padded to the ROM size (e.g. 32 KB) is
  already very close to a valid `.sms`.**

What a complete `.sms` path still needs beyond "pad the flat binary":

1. **Pad to a valid ROM size** — 32 KB for the smallest carts (`sms-reference.md`
   § Cartridge Slot and Card Slot lists 32 KB as the smallest commercial size).
2. **A valid Sega header at `$7FF0-$7FFF`** *if* the program is to boot on a
   real BIOS-equipped console — the BIOS validates the `TMR SEGA` signature and a
   16-bit checksum and refuses to boot on mismatch (`sms-reference.md` § BIOS
   Variants → "Cart-detect logic"). A no-BIOS Master System II skips this check
   and jumps straight to `$0000`, so for emulator-first learning the header is
   optional at first — but a curriculum that aims at real hardware should compute
   it. <!-- TODO: confirm whether Emu198x machine-sega-master-system enforces the
   header checksum; if not, header generation is optional for capture but still
   recommended -->
3. **Mapper-aware banking** for ROMs over 48 KB (the Sega standard mapper, three
   16 KB slots via `$FFFC-$FFFF`). Early learner cartridges fit in 32 KB and need
   no banking; this only matters as games grow (`sms-reference.md` § Sega Standard
   Mapper).

The container roadmap is owned by Asm198x
(`Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md` § Output containers per
platform). That table currently lists Amiga and NES as emitted, with C64 `.prg`
and Spectrum `.sna` as the in-flight gaps for the launch platforms; an SMS `.sms`
target is a *new* output path of the same kind, and — per that decision's "either
gap can instead be closed on the Emu198x side" note — could alternatively be
handled by Emu198x loading a flat image at `org`.

<!-- TODO: confirm there is (or open) an Asm198x roadmap entry for the .sms output
container before SMS units that target real hardware ship -->

---

## Summary

- **Assembler:** solved in principle — Asm198x Z80 core is complete; SMS reuses
  the Spectrum CPU path.
- **Emulator:** core exists (`machine-sega-master-system`); capture parity is the
  integration gate.
- **Output container:** flat `.bin` today; `.sms` is roadmap but the gap is small
  (pad to ROM size; add Sega header + checksum for real-hardware boot; banking
  only for larger ROMs).
- **Third-party tools (WLA-DX, Emulicious, MEKA, sjasmplus, devkitSMS) are
  reference only** — consulted for precedent on what a complete SMS output and
  accurate emulation should look like, not part of the build.
</content>
