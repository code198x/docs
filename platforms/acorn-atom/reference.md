# Acorn Atom

The Acorn Atom (1980) was **Acorn's first home computer** — the machine that came
before the BBC Micro and set the company on the road to the BBC contract and,
later, ARM. It pairs a 6502 with a tiny base RAM and a built-in BASIC that already
carried the feature the curriculum cares about most: an **assembler built into the
language**. That assembler is the direct ancestor of the inline 6502 assembler in
BBC BASIC, so the Atom is where the Acorn "BASIC and machine code in one listing"
lineage begins. The catch — and the teaching lever — is how *little* machine this
is: an unexpanded Atom ships with around **1 KB of usable RAM**, less than the
VIC-20, so every byte counts.

> **Scaffold doc.** This is a skeleton: solid structure, well-established facts
> with citations, and explicit TODOs where depth is still owed. Hardware facts are
> cited to the primary reference library; do not treat the TODOs as settled. The
> Atom is **earlier and more primitive** than the BBC Micro and Electron — its
> facts do **not** carry over from those machines and have been verified
> independently.

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | **Asm198x** (6502 backend) | 6502 opcodes complete and dialect-validated (acme / ca65 cross-checked). See [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md). |
| Emulator | **Emu198x** (`machine-acorn-atom` core) | **In active development — fixes in flight** (worked on in the Emu198x session). Capture (screenshot/video) via Emu198x once the core reaches capture parity; that is the integration gate. |
| Output container | **Open gate** — flat `.bin` today | Acorn tape/disk containers are roadmap, not shipped. See [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md) § Output containers and [`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md). |
| ROMs | Atom BASIC + COS (OS) ROM required | The Atom needs its BASIC ROM and Cassette Operating System ROM. Sourced like other platform ROMs. <!-- TODO: confirm exact ROM image set + load addresses against reference/by-system/acorn-atom/unknown-atom-technical-manual-issue-2.md (memory-map page). --> |

This platform is scaffolded straight onto the **Asm198x / Emu198x** path — there
is no Docker image and no `ghcr.io` toolchain for the Atom. That follows the
dev-tooling-migration decision (launch platforms migrate off Docker per-platform;
new platforms start on the new tooling). See
[`../../../../decisions/code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md).

## Key specifications

| Aspect | Detail | Source |
|--------|--------|--------|
| CPU | MOS 6502 | tech manual (IC22 "6502-1MHz Micro-Processor") |
| Clock | ~1 MHz | tech manual (IC22 label; §Block Diagram) |
| RAM (base) | ~1 KB usable in the unexpanded Atom (512 B upper text space + 512 B video RAM); minimal system populated to 2 KB | tech manual §Lower Text Space Extension, §Power Requirements |
| RAM (expanded) | Up to ~12 KB of text + graphics RAM by fitting more 2114 chips (lower text space + video graphics extension) | tech manual §Lower Text Space Extension, §Video Graphics Extension |
| Video controller | Motorola **MC6847** Video Display Generator (VDG), memory-mapped | tech manual §Block Diagram (IC31 6847) |
| Display modes | 9 graphics modes, 64×48 (0.5 KB) up to 256×192 (6 KB), plus text | "Atomic Theory and Practice" §11.1 Graphics Modes |
| Sound | 1-bit loudspeaker on bit 2 of the 8255 output port — bit-banged, no sound chip | "Atomic Theory and Practice" (loudspeaker on output port); tech manual §I/O |
| Keyboard I/O | INS8255 PPI driving a key matrix | tech manual §I/O (INS8255 PIA) |
| Expansion I/O | Optional 6522 VIA (base `#9800`); CUTS cassette interface, 300 baud | tech manual §I/O, §VIA |
| OS | Cassette Operating System (COS) in ROM | tech manual §ROM, §Cassette interface |
| Language | Atom BASIC (integer-oriented, with a built-in 6502 assembler) | "Atomic Theory and Practice" §Assembler Programming |

All facts above are drawn from the primary reference library at
`reference/by-system/acorn-atom/`
— principally the **Atom Technical Manual (Issue 2, 1980)** and **Atomic Theory
and Practice (1980)**. Section names (§) refer to their contents.

## Assembly dialect

6502 — the same NMOS instruction set as the C64 and NES. Asm198x's 6502 backend is
opcode-complete and validated byte-identical against acme and ca65, so Atom
assembly assembles on the same core the launch 6502 platforms use. The Atom's
distinctive flavour is **not** the CPU but two period conventions:

- **Hex is written with a leading `#`** on the Atom (e.g. `#8000`), where the
  C64/NES world uses `$` and the BBC uses `&` ("Atomic Theory and Practice" and
  the tech manual: "The `#` sign … indicates a hexadecimal number"). Note this is
  the *opposite* of the 6502 norm, where `#` means "immediate" — so Atom source
  conventions need care. Asm198x source uses its own dialect conventions; keep
  prose and code consistent per file.
- Code reaches the screen, keyboard, cassette and sound through **COS routines**
  and direct memory access to the memory-mapped VDG, rather than a clean vectored
  OS table like the BBC's MOS. See
  [`language/6502-quick-reference.md`](language/6502-quick-reference.md).

`CodeFromFile` language detection: Atom assembly should map to `6502` highlighting
(as C64 does).
<!-- TODO: confirm/add an `acorn-atom` → 6502 path mapping in CodeFromFile's language detection (src/components/CodeFromFile.astro or lib). -->

## What makes the Atom good to teach

- **Extreme constraint.** ~1 KB of usable RAM in the base machine is the
  pedagogical lever: there is no room for waste, so it teaches memory discipline
  in a way roomier 8-bits do not. Surface the constraint, don't hide it.
- **The built-in assembler — the Acorn lineage.** Atom BASIC already lets you drop
  6502 assembly into a BASIC line with `[ ... ]` and run it with `LINK`. This is
  the seed that grew into BBC BASIC's inline assembler — a genuine BASIC-to-machine-code
  bridge, years before the BBC. See [`basic.md`](basic.md).
- **Historically important.** This is Acorn's origin — worth a sentence of context
  (the road to the BBC and ARM), but the curriculum framing stays "how do I build
  on this machine", not a history essay.

## Gotchas

- **You will run out of RAM fast.** The unexpanded machine has ~1 KB usable, split
  between the upper text space and the video RAM. Higher graphics modes *consume
  the same RAM* the program needs — mode 4 (256×192) alone wants 6 KB of video RAM
  ("Atomic Theory and Practice" §11.1). Budget memory before choosing a mode.
- **`#` means hex here, not immediate.** Atom documentation writes hexadecimal with
  a leading `#`. Don't confuse it with the 6502 immediate-mode `#`. Per-file
  consistency matters.
- **Sound is 1-bit and bit-banged.** There is no sound chip — the loudspeaker is
  wired to bit 2 of the 8255 output port, so tones are made by toggling that bit in
  a timed loop ("Atomic Theory and Practice"). Expect square-wave beeps, not
  multi-channel music.
- **Video is memory-mapped through the MC6847.** The CPU and VDG share the video
  RAM; writes are gated so the processor accesses video RAM during blanking to
  avoid on-screen interference (tech manual §Video). This is *not* the BBC's
  6845+ULA design — verify Atom behaviour from the Atom sources.
- **Two text spaces.** The Atom checks for RAM in the *lower* text space at
  power-up and uses it for programs if present; otherwise it falls back to the
  *upper* text space (tech manual §Lower Text Space Extension). Which one your
  program lives in depends on how the machine is expanded.

## Sub-documents

- [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md) — assembler/emulator landscape, the Emu198x core's in-flight status, and the honest output-container situation.
- [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) — memory map, CPU, video (MC6847), sound, the RAM constraint.
- [`language/6502-quick-reference.md`](language/6502-quick-reference.md) — 6502 instruction-set reference plus Atom-specific notes.
- [`basic.md`](basic.md) — Atom BASIC overview and its built-in assembler (the lineage to BBC BASIC).

## Primary reference library

The source of truth for Atom hardware facts lives in the shared reference library
at `reference/by-system/acorn-atom/`:

- `reference/by-system/acorn-atom/1980-atomic-theory-and-practice.md` — the Atom programming book (BASIC + assembler + graphics modes), Acorn Computers, 1980 (second edition).
- `reference/by-system/acorn-atom/unknown-atom-technical-manual-issue-2.md` — ATOM Technical Manual, Issue 2 (Acorn Computers, 1980-10) — hardware, block diagram, memory map, I/O.
- `reference/by-system/acorn-atom/magazines.md` — period magazine coverage for the Atom.

> **Note on provenance.** Both manuals are pdftotext extracts of TOSEC-PIX scans;
> year/publisher are parsed from the TOSEC filenames and not yet line-verified
> against the documents. Treat OCR'd addresses and figures with care.

When a curriculum unit needs a hardware fact not yet captured here, take it from
the library (with provenance: source file, page where known) rather than
inventing it — the layered-reference rule in
[`../../../../decisions/shared-hardware-reference-canon.md`](../../../../decisions/shared-hardware-reference-canon.md).
