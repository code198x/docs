# BBC BASIC (on the Acorn Electron)

The single best thing about the Electron for a teaching curriculum is that it runs
**the same BBC BASIC as the BBC Micro** — the structured, procedure-based BASIC
with the **6502 assembler built into the language**. Everything that makes BBC
BASIC good to teach (named procedures and functions, `REPEAT...UNTIL`, fast `%`
integers, the `?`/`!`/`$` memory operators, and especially the inline `[ ... ]`
assembler reached with `CALL`) is present on the Electron, and works the same way.

That means **the BBC BASIC doc is the source of truth**, and a learner's BBC BASIC
knowledge transfers to the Electron directly:

→ [`../bbc-micro/basic.md`](../bbc-micro/basic.md)

This doc records only what a BASIC learner must know is *different* on the
Electron.

> **Scaffold doc.** Overview + the Electron caveats, with citations and TODOs for
> per-game/per-unit depth. Facts cite the shared BBC reference library; `§` refers
> to its **§Acorn Electron Differences** section unless noted.

## What transfers unchanged

- **The language.** Same BBC BASIC, same syntax, same structured features
  (`DEF PROC`/`DEF FN`, `REPEAT...UNTIL`, single-line `IF`, `%` integers, resident
  integers `A%`–`Z%`).
- **The inline 6502 assembler.** The `[ ... ]` bracketed assembler, the `P%`
  location counter, dot-labels, `OPT`, the `EQUB`/`EQUW`/`EQUD`/`EQUS`
  directives, the two-pass `FOR pass% = 0 TO 2 STEP 2` idiom, and `CALL`/`USR` to
  run the assembled code — all work on the Electron exactly as on the BBC, because
  it is the same BASIC ROM family. This is the platform's standout teaching asset,
  inherited wholesale. The canonical idiom and full explanation are in the BBC doc
  [§ The built-in 6502 assembler](../bbc-micro/basic.md).
- **The MOS-call programming model** from BASIC and from inline assembly
  (`OSWRCH`, `*FX`/`OSBYTE`, `VDU`).

## What's different on the Electron

- **Sound is one channel, no noise.** The `SOUND` command exists and works, but
  the hardware behind it is a single tone channel with a fixed envelope and **no
  noise channel** (§Acorn Electron Differences). BASIC programs that play
  multi-voice tunes or use noise for effects (drums, explosions) on the BBC's
  SN76489 will not reproduce on the Electron. `ENVELOPE` may have limited or no
  effect given the fixed-envelope hardware.
  <!-- TODO: confirm exactly how SOUND/ENVELOPE behave from BASIC on the Electron — which channels are honoured, whether ENVELOPE is a no-op — against the reference library or an OS 1.00 reference. -->
- **No standard MODE 7.** `MODE 7` (teletext) is **not available** on a stock
  Electron — the original ULA has no teletext mode (§Acorn Electron Differences).
  BBC BASIC listings that `MODE 7` for a cheap text screen, or that send teletext
  control codes, must be rewritten for a bitmap text mode (e.g. `MODE 6`) on the
  Electron. This is the most likely "BBC listing that won't run" trap.
- **MODE affects program *speed*.** Because the ULA contends for RAM, the
  effective CPU speed depends on the MODE — MODE 0–3 run at ~1 MHz, MODE 4–7 at
  ~2 MHz (§Acorn Electron Differences). A BASIC program (and especially any inline
  assembly inside it) runs noticeably slower in the high-bandwidth modes. See
  [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) § CPU.
- **No direct hardware pokes for BBC peripherals.** The `?&FE40 = …` style of
  poking a BBC System VIA register from BASIC has nothing to poke on the
  Electron — there is no 6522. `?`/`!` still work on RAM and on the ULA's own
  registers, but BBC hardware addresses are not there (§SHEILA).

> **Variable-naming caution (general BASIC gotcha).** As on the BBC and other 8-bit
> BASICs, avoid using language keywords as variable names; confirm the reserved set
> against the BASIC ROM User Guide before finalising sample listings.
<!-- TODO: confirm BBC BASIC's reserved-word / tokenisation rules for variable names against 1984-basic-rom-user-guide.md before writing .bas samples (shared with the BBC). -->

## Relationship to the assembly track

The Electron supports the same three-stage pedagogy as the BBC, and the inline
assembler means BASIC and assembly meet in the middle:

1. **BASIC** — structured programs using procedures, integers, and `?`/`!`/`$`.
2. **BASIC + inline assembly** — bracketed 6502 inside BASIC, `CALL` to run, for
   the parts that need speed. On the Electron this is *especially* relevant
   because contention makes BASIC slow in graphics modes — but note the assembly
   is also contended.
3. **Assembly** — standalone 6502 via Asm198x, through MOS calls (see
   [`language/6502-quick-reference.md`](language/6502-quick-reference.md)).

<!-- TODO: decide and record the Electron track lineup (which games/modules, BASIC
     vs assembly vs bridge) in the module catalogue + a lineup decision, per
     state-lives-in-catalogues. Given the BBC inheritance, consider whether
     Electron content is a distinct track or a "differences" overlay on BBC units.
     This doc stays a pointer once that exists. -->

## See also

- [`../bbc-micro/basic.md`](../bbc-micro/basic.md) — the full BBC BASIC overview and the inline 6502 assembler (the source of truth).
- [`reference.md`](reference.md) — platform entry doc and toolchain.
- [`language/6502-quick-reference.md`](language/6502-quick-reference.md) — the 6502 instruction set (points to the BBC) and Electron timing/OS notes.
- [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) — the ULA contention model, MODE support, single-channel sound.
- Primary library:
  `reference/by-system/bbc-micro/1984-basic-rom-user-guide.md`
  (the BBC BASIC reference, incl. the inline assembler — the same BASIC the
  Electron runs);
  `reference/by-system/bbc-micro/howtowriteadventuregamesforthebbcmicrocomputermodelbandacornelectron1984.md`
  (a 1984 book explicitly covering the Electron in BASIC).
