# BBC Micro

The BBC Microcomputer (Acorn, 1981) was the machine of British computing
education — the reference hardware for the BBC's Computer Literacy Project, in
classrooms across the country, and the launchpad for a generation of programmers.
It pairs a fast, uncontended 6502 with a generous I/O complement and one of the
best BASICs of its era: BBC BASIC, which ships with a **built-in 6502
assembler**. That last point makes the BBC unusually well-suited to teaching,
because a learner can write structured BASIC and drop into hand-written machine
code *in the same program*, with no separate toolchain. The curriculum targets
the **Model B** (32 KB) — the family's baseline.

> **Scaffold doc.** This is a skeleton: solid structure, well-established facts
> with citations, and explicit TODOs where depth is still owed. Hardware facts
> are cited to the primary reference library; do not treat the TODOs as settled.

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | **Asm198x** (6502 backend) | 6502 opcodes complete and dialect-validated (acme / ca65 cross-checked). See [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md). |
| Emulator | **Emu198x** (`machine-acorn-bbc-micro` core) | Capture (screenshot/video) via Emu198x once the core reaches capture parity — the integration gate. |
| Output container | **Open gate** — flat `.bin` today | BBC disk/tape containers (`.ssd`/`.dsd` DFS disc, `.uef` tape) are roadmap, not shipped. See [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md) § Output containers. |
| ROMs | OS ROM + BASIC ROM required | The Model B needs the MOS (OS 1.20) ROM at `&C000`–`&FFFF` and the BBC BASIC ROM in a sideways slot. Not distributable; sourced like other platform ROMs. |

This platform is scaffolded straight onto the **Asm198x / Emu198x** path — there
is no Docker image and no `ghcr.io` toolchain for the BBC. That follows the
dev-tooling-migration decision (the launch platforms migrate off Docker
per-platform; new platforms start on the new tooling). See
[`../../../../decisions/code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md).

## Key specifications

| Aspect | Detail | Source |
|--------|--------|--------|
| CPU | MOS 6502A | reference library §System Architecture |
| Clock | 2 MHz — **uncontended** by video (unlike Spectrum/C64) | §System Architecture, §Emulation Notes |
| RAM | 32 KB (Model B) | §Family Overview |
| Video controller | 6845 CRT controller (HD6845S) + Acorn Video ULA | §Video Hardware |
| Display modes | MODE 0–7 (640×256 mono → 160×256 16-colour → teletext) | §Screen Modes |
| Teletext (MODE 7) | Mullard SAA5050 character generator | §SAA5050 Teletext |
| Sound | TI SN76489 — 3 square-wave tones + 1 noise channel, mono | §SN76489 Sound Generator |
| I/O | Two 6522 VIAs (System VIA + User VIA) | §System VIA, §User VIA |
| OS | Acorn MOS (Machine Operating System), 16 KB ROM | §Operating System (MOS) |
| Language | BBC BASIC (with inline 6502 assembler) | §BBC BASIC |

All facts in this table are drawn from the primary library reference
`reference/by-system/bbc-micro/bbc-micro-reference.md`.
Section names (§) refer to its contents list.

## Assembly dialect

6502 — the same instruction set as the C64 and NES (NMOS 6502 family). Asm198x's
6502 backend is opcode-complete and validated byte-identical against acme and
ca65, so BBC assembly source assembles on the same core the launch 6502 platforms
use. The BBC's distinctive flavour is not the CPU but the **OS interface**: code
reaches the screen, keyboard, sound and files through MOS vectored calls
(`OSWRCH`, `OSRDCH`, `OSBYTE`, `OSWORD`, `OSCLI`) rather than poking hardware
directly. See [`language/6502-quick-reference.md`](language/6502-quick-reference.md).

`CodeFromFile` language detection: BBC assembly should map to `6502` highlighting
(as C64 does).
<!-- TODO: confirm/add a `bbc-micro` → 6502 path mapping in CodeFromFile's language detection (src/components/CodeFromFile.astro or lib). -->

## What makes the BBC good to teach

- **Uncontended CPU.** The 6845 reads video RAM in the half-cycle the 6502 isn't
  using, so the CPU runs at a flat 2 MHz regardless of screen mode. Timing is
  predictable in a way the contended Spectrum and C64 are not (reference
  §Emulation Notes).
- **The inline assembler.** BBC BASIC's `[ ... ]` blocks let a program contain
  6502 assembly that BASIC assembles at run time — a genuine bridge from BASIC to
  machine code. This is the platform's standout teaching asset. See
  [`basic.md`](basic.md).
- **A clean OS API.** Almost everything goes through documented MOS calls, so the
  "how do I print a character / read a key / make a sound" answers are stable and
  well-documented, not folklore.

## Gotchas

- **No direct sound register access.** The SN76489 is *not* memory-mapped — it
  hangs off the System VIA's slow data bus and is driven through the addressable
  latch with interrupts disabled. Use the MOS `SOUND`/`OSWORD &07` path rather
  than poking the chip (reference §SN76489 Sound Generator).
- **Screen base moves with the mode.** Each MODE places screen RAM at a different
  address and consumes a different amount of RAM (MODE 0–2 = 20 KB at `&3000`;
  MODE 7 = 1 KB at `&7C00`). Read `HIMEM`/`OSHWM` rather than hard-coding
  (reference §Memory Map, §Screen Modes).
- **MODE 7 is teletext, not bitmap.** MODE 7 stores character codes and inline
  control codes for the SAA5050; it is not a pixel buffer. It is the cheapest
  mode (1 KB) and great for text UIs, but graphics there mean 2×3 "sixel" mosaics
  (reference §SAA5050 Teletext).
- **`&` is hex on the BBC.** BBC documentation and BBC BASIC write hexadecimal
  with a leading `&` (e.g. `&FE40`), where the C64/NES world uses `$`. Asm198x
  source uses its own dialect conventions — keep prose and code consistent per
  file.
- **BREAK is wired to RESET.** The BREAK key resets the 6502 directly; it never
  appears in the keyboard matrix (reference §Keyboard, §Boot Sequence).

## Sub-documents

- [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md) — assembler/emulator landscape and the honest output-container situation.
- [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) — memory map, CPU, video (6845 + MODE system), sound (SN76489).
- [`language/6502-quick-reference.md`](language/6502-quick-reference.md) — 6502 instruction-set reference plus BBC OS calls.
- [`basic.md`](basic.md) — BBC BASIC overview and the inline 6502 assembler.

## Primary reference library

The source of truth for BBC hardware facts lives in the shared reference library
at `reference/by-system/bbc-micro/`:

- `reference/by-system/bbc-micro/bbc-micro-reference.md` — distilled family reference (memory map, video, sound, MOS, variants).
- `reference/by-system/bbc-micro/1982-assembly-language-programming-for-the-bbc-microcomputer.md` — assembly tutorial (Macmillan, 1982).
- `reference/by-system/bbc-micro/1984-basic-rom-user-guide.md` — BBC BASIC reference incl. the built-in assembler.
- `reference/by-system/bbc-micro/bbc-micro-advanced-user-guide.md` — the Model B programmer's bible (Bray/Dickens/Holmes, 1983).
- `reference/by-system/bbc-micro/index.md` — library index for the system.

When a curriculum unit needs a hardware fact not yet captured here, take it from
the library (with provenance: source file, page where known) rather than
inventing it — the layered-reference rule in
[`../../../../decisions/shared-hardware-reference-canon.md`](../../../../decisions/shared-hardware-reference-canon.md).
