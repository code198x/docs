# Acorn Electron

The Acorn Electron (1983) is the BBC Micro's budget cousin: Acorn's home-market
answer to the £100 ZX Spectrum, built to bring as much of the BBC's world as
possible to a cheaper machine. It runs the **same 6502 family CPU** and the
**same BBC BASIC** — including the built-in inline 6502 assembler — as the BBC
Model B, and shares most of the BBC's MOS operating-system call interface. What
makes it cheaper is a single custom chip, the **ULA**, that replaces the BBC's
6845, Video ULA, two 6522 VIAs, sound generator and cassette interface all at
once. That one substitution is the source of nearly every Electron difference:
it is slower, sounds simpler, and drops some BBC hardware compatibility — but the
*programming model a learner sees* is overwhelmingly the BBC's.

Because of that inheritance, **this tree is written as a derivative of the BBC
Micro tree**. It documents what *differs* on the Electron rather than
re-deriving the shared 6502, BBC BASIC, and MOS material. Where a fact is shared,
it links to the BBC doc; where the Electron diverges, it says so and cites the
source.

> **Scaffold doc.** This is a skeleton: solid structure, well-established facts
> with citations, and explicit TODOs where Electron-specific depth is still owed.
> Hardware facts are cited to the shared BBC reference library (which carries a
> dedicated *Acorn Electron Differences* section); do not treat the TODOs as
> settled.

## Relationship to the BBC Micro

The Electron and the BBC share the layers that matter most for teaching:

| Layer | Shared with BBC? | Where it lives |
|-------|------------------|----------------|
| CPU instruction set | **Yes** — 6502 (the Electron uses a 6502A) | [BBC `6502-quick-reference.md`](../bbc-micro/language/6502-quick-reference.md) |
| BBC BASIC + inline assembler | **Yes** — the same language ROM family | [BBC `basic.md`](../bbc-micro/basic.md), [`basic.md`](basic.md) |
| MOS OS-call interface (`OSWRCH`, `OSBYTE`, …) | **Mostly** — source-compatible at the OSBYTE/OSWORD level | [BBC `6502-quick-reference.md` § BBC OS calls](../bbc-micro/language/6502-quick-reference.md) |
| Screen MODE numbers | **Mostly** — MODE 0–6 (no standard MODE 7) | [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) |
| Video/sound/IO *hardware* | **No** — one ULA replaces the BBC's chip set | [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) |
| CPU timing | **No** — the ULA contends for RAM and slows the CPU | [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) |

The rule of thumb: **code that goes through MOS calls and BBC BASIC transfers;
code that pokes BBC hardware registers directly does not** (reference library
§Acorn Electron Differences).

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | **Asm198x** (6502 backend) | Same 6502 backend the BBC, C64 and NES use — opcode-complete and dialect-validated. No new CPU work for the Electron. See [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md). |
| Emulator | **Emu198x** (`machine-acorn-electron` core) | The core exists in the Emu198x workspace alongside `machine-acorn-bbc-micro`. Capture (screenshot/video) parity is the integration gate. See [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md). |
| Output container | **Open gate** — flat `.bin` today | Acorn tape/disc containers (`.uef` cassette; ADFS for the Plus 3) are roadmap, not shipped — the same situation as the BBC. See [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md) § Output containers. |
| ROMs | OS 1.00 ROM + BBC BASIC ROM | The Electron needs its **OS 1.00** ROM (unique to the Electron) plus the BBC BASIC ROM. Not distributable; sourced like other platform ROMs. |

This platform is scaffolded straight onto the **Asm198x / Emu198x** path — there
is no Docker image and no `ghcr.io` toolchain for the Electron, following the
dev-tooling-migration decision (new platforms start on the new tooling). See
[`../../../../decisions/code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md).

## Key specifications

| Aspect | Detail | Source |
|--------|--------|--------|
| CPU | MOS 6502A | reference library §Family Overview, §Acorn Electron Differences |
| Clock | 2 MHz nominal — **ULA-contended**: effectively ~1 MHz during MODE 0–3 (high-bandwidth modes), 2 MHz during MODE 4–7 | §Acorn Electron Differences |
| RAM | 32 KB DRAM, single configuration (ULA contends for it during graphics) | §Acorn Electron Differences |
| Video + IO controller | A single custom **ULA** at SHEILA `&FE00`–`&FE0F` (replaces the BBC's 6845, Video ULA, both 6522 VIAs, sound generator and cassette interface) | §SHEILA, §Acorn Electron Differences |
| Display modes | MODE 0–6 (no standard MODE 7 / teletext in the original ULA) | §Acorn Electron Differences |
| Sound | **Single tone channel**, fixed envelope, **no noise channel** — driven through the ULA, not an SN76489 | §Acorn Electron Differences |
| Storage | Cassette only by default (1200 baud, BBC-compatible tape format); Plus 3 expansion adds an ADFS 3.5" floppy | §Acorn Electron Differences |
| OS | Acorn MOS **OS 1.00** (unique to the Electron), source-compatible with BBC OS 1.20 at the OSBYTE/OSWORD level | §Acorn Electron Differences |
| Language | BBC BASIC (with the inline 6502 assembler) — the same as the BBC | §BBC BASIC |
| Released | October 1983 | §Acorn Electron Differences |

Facts above are drawn from the shared BBC primary library reference
[`bbc-micro-reference.md`](../../../../reference/by-system/bbc-micro/bbc-micro-reference.md),
whose **§Acorn Electron Differences** section covers the Electron explicitly.
There is no dedicated `acorn-electron` folder in the reference library — the
Electron shares the BBC system tree.

## Assembly dialect

6502 — identical instruction set to the BBC, C64 and NES (NMOS 6502 family; the
Electron's 6502A is the same as the BBC's). Asm198x's 6502 backend covers it with
no new work. As on the BBC, the Electron's distinctive flavour is the **OS
interface**: code reaches screen, keyboard and sound through MOS vectored calls
(`OSWRCH`, `OSRDCH`, `OSBYTE`, `OSWORD`, `OSCLI`) — and on the Electron this is
not just idiom but *necessity*, because the BBC's direct-hardware register
layout (the 6522 VIAs, the 6845) **does not exist** behind the ULA. See
[`language/6502-quick-reference.md`](language/6502-quick-reference.md).

`CodeFromFile` language detection: Electron assembly should map to `6502`
highlighting (as the C64 and BBC do).
<!-- TODO: confirm/add an `acorn-electron` → 6502 path mapping in CodeFromFile's language detection (src/components/CodeFromFile.astro or lib), mirroring the bbc-micro mapping. -->

## What makes the Electron good — and awkward — to teach

- **Knowledge transfers from the BBC almost wholesale.** The same BASIC, the same
  inline assembler, the same 6502, the same MOS calls. A learner who has done the
  BBC on-ramp already knows most of the Electron.
- **Timing is the lesson.** The Electron is the family's clearest case of
  **memory contention**: the ULA fetches display data from the same DRAM the CPU
  uses, so effective CPU speed depends on the screen MODE — roughly 1 MHz in the
  high-bandwidth MODE 0–3, 2 MHz in MODE 4–7 (reference §Acorn Electron
  Differences). This is the *opposite* design choice from the BBC's
  zero-contention 6845, and it makes "choose your MODE for the speed you need" a
  concrete, measurable decision.
- **A simpler sound model.** One tone channel, no noise — less to teach, but also
  less to work with than the BBC's three-tone-plus-noise SN76489.

## Gotchas

- **The CPU slows down in graphics modes.** Unlike the BBC, the Electron's 6502
  is contended by the ULA. MODE 0–3 run the CPU at roughly half speed; MODE 4–7
  are faster. Loop timing that holds on the BBC will not hold on the Electron, and
  changes with the MODE (reference §Acorn Electron Differences).
- **No BBC hardware registers.** There is **no System VIA, no User VIA, no User
  Port** and no 6845. Code that pokes `&FE40` (System VIA) or programs the 6845
  on the BBC simply fails on the Electron — everything is the single ULA at
  `&FE00`–`&FE0F` instead. Go through MOS (reference §SHEILA, §Acorn Electron
  Differences).
- **No standard MODE 7.** The original Electron ULA has **no teletext mode**;
  third-party teletext add-ons exist but are not standard. Do not assume MODE 7
  for cheap text UIs the way the BBC tree does (reference §Acorn Electron
  Differences).
- **Sound is one channel, no noise.** Multi-channel music and noise effects
  written for the BBC's SN76489 will not reproduce. Use the single ULA tone via
  the MOS `SOUND` path (reference §Acorn Electron Differences).
  <!-- TODO: confirm exactly which SOUND channels/parameters the Electron honours via MOS (does SOUND 0 noise no-op? channels 1-3 collapse to one?) against the reference library or OS 1.00 docs. -->
- **OS 1.00, not 1.20.** Many *hardware-specific* OSBYTEs return errors or no-op
  on the Electron even though the everyday calls (`OSWRCH`, `OSRDCH`, `OSBYTE`
  read/write, `OSWORD`) are source-compatible. Test BBC code rather than assuming
  it transfers (reference §Acorn Electron Differences).
- **Cassette transfers, disc generally does not.** The cassette format is
  identical to the BBC's, so tape software for the Model B usually loads on the
  Electron — but the Plus 3 uses ADFS, not the BBC's DFS, so BBC disc software
  generally will not (reference §Acorn Electron Differences).
- **`&` is hex.** As on the BBC, BBC BASIC and Electron documentation write
  hexadecimal with a leading `&` (e.g. `&FE00`), where the C64/NES world uses `$`.

## Sub-documents

- [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md) — the (short) toolchain story: same 6502/Asm198x path as the BBC, Electron-specific notes, Emu198x core status.
- [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) — memory map, the **ULA contention model** (the centrepiece), MODE support, single-channel sound, and how each differs from the BBC.
- [`language/6502-quick-reference.md`](language/6502-quick-reference.md) — points to the BBC 6502 reference for the shared core, adding Electron-specific timing and OS notes.
- [`basic.md`](basic.md) — BBC BASIC on the Electron (the same BASIC + inline assembler), with the sound/MODE caveats.

## Primary reference library

The Electron **shares the BBC system tree** in the shared reference library at
[`../../../../reference/by-system/bbc-micro/`](../../../../reference/by-system/bbc-micro/)
— there is no separate `acorn-electron` folder:

- [`bbc-micro-reference.md`](../../../../reference/by-system/bbc-micro/bbc-micro-reference.md) — distilled family reference. **§Acorn Electron Differences** and the family-overview table cover the Electron explicitly; the SHEILA table marks which registers exist on the Electron (the ULA at `&FE00`–`&FE0F`).
- [`howtowriteadventuregamesforthebbcmicrocomputermodelbandacornelectron1984.md`](../../../../reference/by-system/bbc-micro/howtowriteadventuregamesforthebbcmicrocomputermodelbandacornelectron1984.md) — a 1984 book that **explicitly covers the Electron** alongside the Model B; useful for Electron-aware BASIC/adventure idioms.
- [`1984-basic-rom-user-guide.md`](../../../../reference/by-system/bbc-micro/1984-basic-rom-user-guide.md) — BBC BASIC reference incl. the built-in assembler (the same BASIC the Electron runs).
- [`index.md`](../../../../reference/by-system/bbc-micro/index.md) — library index for the BBC/Electron system tree.

When a curriculum unit needs an Electron-specific hardware fact not yet captured
here, take it from the library (with provenance) rather than inventing it — and
**do not silently copy a BBC fact that differs on the Electron**. The
layered-reference rule:
[`../../../../decisions/shared-hardware-reference-canon.md`](../../../../decisions/shared-hardware-reference-canon.md).
