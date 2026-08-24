# BBC BASIC

BBC BASIC is one of the best 8-bit BASICs ever written, and for a teaching
curriculum it has a standout feature no other launch platform offers: a **6502
assembler built into the language**. A learner can write a structured BASIC
program and, in the same listing, drop into hand-written assembly enclosed in
square brackets `[ ... ]`. BBC BASIC assembles it on the spot. That makes the BBC
a genuine bridge from BASIC to assembly — you can teach machine code *inside* the
language a learner already knows, with no separate toolchain.

> **Scaffold doc.** Overview + the inline-assembler angle, with citations and
> TODOs for the per-game/per-unit depth. Facts cite the primary reference library;
> `§` refers to
> `reference/by-system/bbc-micro/bbc-micro-reference.md`
> and the BASIC ROM User Guide is cited by section.

## Why BBC BASIC teaches well

BBC BASIC (BASIC II on the Model B) is **structured**, not the line-number spaghetti
of many contemporaries (§BBC BASIC):

- **Named procedures and functions:** `DEF PROCname` / `PROCname`,
  `DEF FNname` / `FNname` — real subroutines with local variables, not `GOSUB`
  line numbers.
- **Structured control flow:** `IF...THEN...ELSE`, `REPEAT...UNTIL`. (The richer
  `WHILE...ENDWHILE`, `CASE...OF`, and multi-line `IF...ENDIF` arrive in BASIC IV
  on the Master — the Model B has `REPEAT...UNTIL` and single-line `IF`.)
- **Fast integer variables:** a `%` suffix marks a 4-byte signed integer (`A%`,
  `score%`), which is substantially faster than floating point. The resident
  integers `A%`–`Z%` even survive `NEW`.
- **Direct memory operators:** `?addr` reads/writes one byte, `!addr` a 4-byte
  word, `$addr` a string. So `?&FE40 = 0` pokes a hardware register directly from
  BASIC (§BBC BASIC).

These features let early units teach clean program structure *and* let later
units reach the hardware — without leaving BASIC.

> **Variable-naming caution (general BASIC gotcha).** As on other 8-bit BASICs,
> avoid using language keywords as variable names. The exact reserved set differs
> from Sinclair/Commodore BASIC; confirm against the BASIC ROM User Guide before
> finalising sample listings.
<!-- TODO: confirm BBC BASIC's reserved-word / tokenisation rules for variable names against 1984-basic-rom-user-guide.md before writing .bas samples. -->

## The built-in 6502 assembler — the teaching bridge

This is the feature to build curriculum around. BBC BASIC contains a full 6502
assembler reached with **square brackets**: when the interpreter meets `[` it
switches from BASIC into assembling 6502 mnemonics, and `]` switches back
(reference: BASIC ROM User Guide §1.6 "The BASIC assembler" and ch. 6 "The
Assembler" — "The built-in 6502 assembler in BASIC is a very useful tool").

How it works, at the level a unit needs (BASIC ROM User Guide §1.6, ch. 6;
cross-referenced in `reference/by-system/bbc-micro/bbc-micro-reference.md` §BBC BASIC):

- **`P%` is the location counter** — you set `P%` to the address where the code
  should assemble, and the assembler advances it as it emits bytes.
- **Labels are BASIC variables** declared with a leading dot, e.g. `.loop`. They
  can be forward-referenced because the assembler does **two passes**.
- **`OPT` controls the pass behaviour** — listing on/off and whether errors are
  reported — which is exactly how the two-pass idiom is written: assemble once
  silently to resolve labels, once to report.
- **Directives** include `EQUB`/`EQUW`/`EQUD`/`EQUS` for laying down bytes, words,
  double-words, and strings.
- You then run the assembled code with `CALL addr` (or `USR`) from BASIC, and it
  returns to BASIC with `RTS`.

The canonical idiom (two-pass `FOR` loop around the bracketed block):

```basic
10 osasci = &FFE3
20 DIM code% 100
30 FOR pass% = 0 TO 2 STEP 2
40   P% = code%
50   [ OPT pass%
60   .start
70   LDA #ASC"!"
80   JSR osasci
90   RTS
100  ]
110 NEXT pass%
120 CALL start
```

This program assembles a tiny 6502 routine into the buffer `code%` and calls it.
The point for the curriculum is the *shape*: BASIC for setup and flow, brackets
for the machine code, `CALL` to run it. A unit can start in pure BASIC, then
replace one slow inner loop with a bracketed assembly version — teaching exactly
*why* and *when* assembly matters, on one machine, in one listing.

<!-- TODO: verify the example above assembles and runs once the BBC build/capture
     path is confirmed (Asm198x/Emu198x — see TOOLCHAIN-RESEARCH.md), then move it
     to code-samples/bbc-micro/basic/ and reference via CodeFromFile. Treat the
     listing as illustrative until then. -->

## Relationship to the assembly track

The BBC supports both tracks the curriculum uses elsewhere — a **BASIC** track
and a pure **assembly** track — but uniquely, the inline assembler means the two
can meet in the middle. A natural BBC pedagogy:

1. **BASIC** — structured programs using procedures, integers, and `?`/`!`/`$`.
2. **BASIC + inline assembly** — the bridge: bracketed 6502 inside BASIC, `CALL`
   to run, for the parts that need speed.
3. **Assembly** — standalone 6502 via Asm198x, reaching the machine through MOS
   calls (see [`language/6502-quick-reference.md`](language/6502-quick-reference.md)).

<!-- TODO: decide and record the BBC track lineup (which games/modules, BASIC vs
     assembly vs bridge) in the module catalogue + a lineup decision, per
     state-lives-in-catalogues. This doc stays a pointer once that exists. -->

## See also

- [`reference.md`](reference.md) — platform entry doc and toolchain.
- [`language/6502-quick-reference.md`](language/6502-quick-reference.md) — the 6502 instruction set and BBC OS calls.
- [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) — memory map, video, sound.
- Primary library:
  `reference/by-system/bbc-micro/1984-basic-rom-user-guide.md`
  (§1.6 The BASIC assembler; ch. 6 The Assembler) — the authoritative BBC BASIC
  reference incl. the inline assembler.
