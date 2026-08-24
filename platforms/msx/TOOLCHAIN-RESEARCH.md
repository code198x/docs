# MSX Toolchain Research

> **This is research, not a build.** It records *why* the MSX platform targets the
> family tools (Asm198x to assemble, Emu198x to run and capture) and what is and
> is not ready yet. There is deliberately no MSX Docker image — this platform is
> scaffolded straight onto the Asm198x / Emu198x path under the dev-tooling
> migration decision
> ([`code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md)).

## The assembler landscape (Z80)

MSX runs a Zilog Z80A, so any Z80 assembler can in principle build MSX code. The
field a developer would otherwise reach for:

| Tool | Notes |
|------|-------|
| **sjasmplus** | The de-facto modern Z80 assembler in the MSX and Spectrum scenes. Rich macro system, MSX-aware output options. Actively maintained. |
| **pasmo / pasmonext** | Lightweight Z80 assemblers; pasmonext is what Code198x's existing Spectrum Docker image uses. |
| **tniASM, Glass, WLA-DX** | Other assemblers with MSX users; WLA-DX is multi-CPU. |

These are the reference points, not the target. We list them so the choice of
Asm198x is an informed one and so anyone cross-checking output has a known-good
comparison.

## Why Asm198x is the target

Asm198x is the 198x family assembler — a single cross-platform binary built on a
shared, declarative ISA spec. For MSX it is a strong fit because:

- **The Z80 core is complete and dialect-validated.** Z80 was the second CPU
  Asm198x implemented (after 6502), driven by the Spectrum; its opcode set is
  finished and validated against the spec. MSX adds no new CPU work — it reuses
  the Z80 core wholesale. (See the
  [Asm198x packaging & CPU roadmap](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md),
  Z80 row: ✅ done.)
- **One toolchain across the family.** Rather than maintain a fifth Docker
  image, MSX joins the migration to Asm198x/Emu198x that the launch platforms are
  already moving onto.
- **Round-trip guarantee.** Asm198x's disassembler decodes against the same ISA
  data the assembler emits from, which is useful when verifying generated MSX
  code byte-for-byte.

Asm198x is not a syntactic clone of sjasmplus or pasmo; its per-dialect stance is
recorded in the Asm198x decisions. For MSX the practical point is that the
*instruction encoding* is settled and correct — what is still in motion is the
output container, below.

## The output-container situation (be honest)

This is the live gap. Asm198x assembles Z80 source correctly, but **what it wraps
the bytes in** is platform-specific, and MSX containers are not built yet.

- **Today:** Asm198x emits a **flat `.bin`** — the assembled bytes at the
  program's `org` address, no header, no container. That is enough to inspect
  output and to feed a raw loader, but it is **not** a runnable MSX artefact on
  its own.
- **MSX is not yet in the output-dispatch table.** The packaging roadmap's
  per-platform output table currently lists Amiga (✅), NES (✅), C64 (⏸ gap), and
  Spectrum (⏸ gap). MSX is not on it — it is a *future* platform whose containers
  are roadmap work, behind the launch platforms.
- **Roadmap MSX containers:**
  - **`.rom`** — cartridge image. The common path: a 16 KB or 32 KB ROM with the
    `AB` signature and init/entry pointers at `$4000`, mapping into page 1
    (`$4000–$7FFF`) and optionally page 2. Larger games need a mapper (Konami,
    ASCII8/16) — see
    `reference/by-system/msx/msx-reference.md` §8.2.
  - **`.com`** — MSX-DOS executable. MSX-DOS 1 is CP/M 2.2-compatible, so a `.com`
    is a flat program loaded at `$0100` and entered there
    (`msx-reference.md` §10.2). This is the *closest to flat `.bin`* of the three
    and likely the cheapest container to add.
  - **`.cas`** — cassette image, for the `BLOAD`/tape-load workflow
    (`msx-reference.md` §9).

<!-- TODO: when MSX container work is scheduled, add an MSX row to the output table
     in Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md and update
     reference.md's build command. Decide container priority (.com is likely
     cheapest; .rom is the most "native" for game distribution). -->

Until a container lands, MSX curriculum work that needs a *runnable* artefact is
gated on either (a) the Asm198x MSX container, or (b) Emu198x loading a flat image
at `org` — the same either-side choice the C64/Spectrum gaps face, owned by the
umbrella migration decision.

## Emulator status (Emu198x)

- **The `machine-msx` core exists** in Emu198x.
- **Capture parity is the integration gate.** Curriculum units need reliable
  headless screenshot and video capture (the same pipeline the other platforms
  use). MSX capture must be proven before MSX units can be verified to the DoD
  bar.
- **BIOS dependency.** An MSX core needs a system BIOS to boot (the Spectrum does
  not). C-BIOS is the licence-clean open-source BIOS that boots most cartridge
  software; vendor BIOS ROMs are not distributable.

<!-- TODO: confirm machine-msx capture-parity status against Emu198x; confirm which
     BIOS the core ships/expects. File any MSX core gaps as issues on emu198x/emu198x
     per the "emulator work goes to the Emu198x session" convention. -->

## Third-party tools (reference only)

For cross-checking and manual exploration, not part of the build:

- **openMSX** — the most accurate MSX emulator; its machine/extension config and
  `softdb.xml` mapper database are the de-facto standard for MSX emulation.
- **blueMSX** — widely used, strong debugger.
- **sjasmplus** — reference assembler for verifying Asm198x output.

## Summary

Z80 assembly via **Asm198x** (core done) → currently a **flat `.bin`**; runnable
MSX containers (`.rom` / `.com` / `.cas`) are **roadmap**. Run and capture via
**Emu198x** `machine-msx` (exists; capture parity is the gate). An MSX **system
BIOS** is required to boot — C-BIOS is the open option. No Docker image, by design.
