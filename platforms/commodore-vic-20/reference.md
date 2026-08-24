# Commodore VIC-20

The VIC-20 (1981; sold in Japan from 1980 as the VIC-1001) was Commodore's
first colour computer and the first computer of any kind to sell more than a
million units. It is the **friendly first machine** — cheap, simple, and
designed to sit next to the television — and it is the direct ancestor of the
Commodore 64. If you know the C64, much here will feel familiar: the same 6502
family CPU, the same Commodore BASIC v2, the same KERNAL jump table, the same
Datassette and serial-bus plumbing. What differs is the scale. The VIC-20 ships
with **about 5 KB of RAM** and a much simpler video chip (the VIC, not the
VIC-II), and that scarcity is the whole pedagogical point: there is nowhere to
hide, so you learn what every byte is for.

This page is the curriculum-flavoured entry point for VIC-20 work. It cites the
primary reference library for every hardware fact; it does not restate the
library in full. Start here, then follow the sub-doc links for depth.

> **Scope note.** This is a *scaffold*. It records the well-established facts and
> the citations behind them, and flags the deeper specifics with explicit TODOs
> to confirm against the reference library before they go into a unit.

## Toolchain

The VIC-20 is scaffolded directly onto the family's own tooling — **Asm198x**
for builds and **Emu198x** for capture — per the dev-tooling-migration decision
([`../../../../decisions/code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md)).
There is no Docker image for this platform; it was never wired to the
third-party path the four launch platforms are migrating *off*.

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | **Asm198x** (6502 core) | 6502 opcodes complete and dialect-validated (byte-identical against ACME and ca65). The curriculum's `.asm` sources assemble unchanged. |
| Emulator / capture | **Emu198x** (`machine-commodore-vic-20` core) | Headless screenshot + video + scriptable + MCP surface. Capture parity is the per-unit integration gate. |
| Output container | **`.prg`** | Same load-address-prefixed format as the C64. Asm198x emits a flat `.bin` today; `.prg` wrapping is a shared roadmap item with the C64 — see [TOOLCHAIN-RESEARCH.md](TOOLCHAIN-RESEARCH.md). |
| ROMs | KERNAL (8 KB) + BASIC (8 KB) + character ROM (4 KB) | Open ROMs are not distributable; sourced like the other Commodore platforms. |

See [TOOLCHAIN-RESEARCH.md](TOOLCHAIN-RESEARCH.md) for the full landscape (why
Asm198x is the target, Emu198x core status, the output-container situation, and
the third-party tools kept for reference only).

## Key specifications

| Spec | Value | Source |
|------|-------|--------|
| CPU | MOS **6502** (NMOS, single accumulator) | `vic20-reference.md` §1 |
| Clock | **1.0227 MHz** (NTSC, 6560) / **1.1082 MHz** (PAL, 6561) | `vic20-reference.md` §1, §16 |
| RAM (unexpanded) | **~5 KB** — 1 KB low RAM ($0000–$03FF) + 4 KB at $1000–$1FFF | `vic20-reference.md` §1, §3 |
| Free BASIC RAM | **3583 bytes** at the READY prompt, unexpanded | `vic20-reference.md` §1, §4 |
| ROM | 8 KB BASIC ($C000–$DFFF) + 8 KB KERNAL ($E000–$FFFF) + 4 KB character ROM | `vic20-reference.md` §1, §3 |
| Video + sound | **VIC chip** — 6560 (NTSC) / 6561 (PAL); video, 3 tone voices + noise, paddle A/D, light pen, all in one part | `vic20-reference.md` §5, §8 |
| Text screen | **22 columns × 23 rows** = 506 cells (176 × 184 px default) | `vic20-reference.md` §1, §7 |
| Colours | 16 | `vic20-reference.md` §1 |
| Sprites | **None** — movement is done by repainting characters | `vic20-reference.md` §5, §17 |
| I/O | Two 6522 VIAs ($9110, $9120); one Atari-standard joystick port; Datassette; serial IEC bus | `vic20-reference.md` §9–§14 |

## Assembly dialect

6502 assembly, same instruction set as the C64. In `CodeFromFile`, VIC-20 paths
should map to **`6502`** highlighting (as C64 does). Asm198x accepts the
ACME/ca65-compatible dialects the 6502 corpus already uses; see the C64
[`6510-quick-reference`](../commodore-64/hardware/6510-quick-reference.md) for
the instruction set (the VIC-20's 6502 and the C64's 6510 share the same
programmer-visible core), and this platform's
[`language/6502-quick-reference.md`](language/6502-quick-reference.md) for the
VIC-20-specific KERNAL call conventions.

## The two gotchas that define VIC-20 curriculum

These are not footnotes — they shape every lesson on this machine.

1. **~5 KB of RAM, and only 3583 bytes free to BASIC.** The unexpanded VIC-20 is
   genuinely tiny. A program, its variables, the screen, *and* any custom
   character set all share the low 8 KB. This is the constraint we teach with:
   there is no room for waste, so the learner sees directly why a tighter loop or
   a packed data table matters. (`vic20-reference.md` §1, §4.)

2. **Screen and colour memory move when RAM is expanded.** On a stock 5 KB
   machine the screen is at **$1E00** and colour RAM at **$9600**. Add 8 KB or
   more (RAM in BLK1) and the KERNAL relocates the screen to **$1000** and colour
   RAM to **$9400** to keep BASIC's free area contiguous. A program with
   hard-coded screen addresses written for one configuration **breaks** on
   another. Portable code reads the screen page from the system pointer at
   **$0288** rather than assuming an address. This single quirk shaped how
   VIC-20 software was distributed ("for any memory configuration") and is a
   first-class teaching moment about indirection. (`vic20-reference.md` §4;
   `1983-vic-20-memory-map.txt`.)

A related trap: the **VIC chip can only see the low 4 KB of CPU RAM**
($0000–$1FFF), so custom character sets must live there, never in expansion RAM.
(`vic20-reference.md` §3, §4.)

## Reference library

Primary sources live at `reference/by-system/commodore-vic20/`
(note: the library slug is `commodore-vic20`, no hyphen before `20`; the
content/docs slug is `commodore-vic-20`, with the hyphen):

- **`vic-20-programmers-reference-guide-1st-edition-6th-printing`** — the primary
  technical source (308 pp): memory map, VIC registers, KERNAL, BASIC tokens,
  keyboard matrix.
- **`1983-vic-20-memory-map`** (Jim Butterfield) — the canonical zero-page,
  low-RAM, and ROM-routine map; the source for the screen-relocation addresses.
- **`vic20-reference.md`** — a distilled system reference (emulator + teaching
  lens) that synthesises the Programmer's Reference Guide plus seven contemporary
  games books. A convenient single-file overview; for any disputed fact, the
  Programmer's Reference Guide is the source of truth.
- **`creatingarcadegamesonthevic1984`** (COMPUTE!) — game-oriented technique
  source: custom characters, movement, collision, sound on the real constraints.
- Plus the games-book corpus (`zappowboom…`, `vicgamesforkids…`,
  `cosmicgames…`, etc.) for how real software actually used the machine.

Per the layered-reference canon, hardware facts originate in this library; these
docs cite it and stay curriculum-flavoured. See
[`../../../../decisions/shared-hardware-reference-canon.md`](../../../../decisions/shared-hardware-reference-canon.md).

## Sub-docs

- [TOOLCHAIN-RESEARCH.md](TOOLCHAIN-RESEARCH.md) — assembler/emulator landscape and the output-container situation.
- [hardware/ARCHITECTURE.md](hardware/ARCHITECTURE.md) — memory map, CPU, VIC chip, expansion behaviour.
- [language/6502-quick-reference.md](language/6502-quick-reference.md) — 6502 instruction reference + KERNAL call conventions.
- [basic.md](basic.md) — Commodore BASIC v2 overview (shared with the C64).
