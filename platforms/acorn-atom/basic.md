# Atom BASIC

Atom BASIC is an early, idiosyncratic, **integer-oriented** BASIC — and it carries
the feature this curriculum cares about most: a **6502 assembler built into the
language**. That assembler is the ancestor of the inline assembler in BBC BASIC,
so Atom BASIC is where the Acorn "structured BASIC with machine code in the same
listing" idea begins. For teaching, it gives you two things at once: a small,
honest BASIC for getting started, and a built-in route down to the metal on a
machine where the metal is never far away.

> **Scaffold doc.** Overview + the built-in-assembler angle and the BBC lineage,
> with citations and TODOs for per-game/per-unit depth. Facts cite the primary
> reference library, principally **Atomic Theory and Practice (1980)** —
> [`../../../../reference/by-system/acorn-atom/1980-atomic-theory-and-practice.md`](../../../../reference/by-system/acorn-atom/1980-atomic-theory-and-practice.md).
> The Atom is earlier and more primitive than the BBC; do not import BBC BASIC
> facts here.

## What Atom BASIC is (and isn't)

- **Integer-only by default.** "BASIC only deals in whole numbers, or integers, so
  the remainder after [division] …" (Atomic Theory). Arithmetic is integer
  arithmetic; there is no fractional result unless you add the optional
  **floating-point ROM** (the FP ROM socket in the memory map enables
  floating-point statements). This is a real constraint to teach *with*, not work
  around — it forces fixed-point thinking early.
- **Idiosyncratic.** Atom BASIC is its own dialect, not Microsoft BASIC. It is
  terse, statements can be chained on a line with `;`, and it has direct memory
  operators (`?`, `!`) and graphics statements (`CLEAR`, `MOVE`, `DRAW`, `PLOT`)
  built in.
- **Small.** Each fitted 1 KB of RAM provides text space for roughly **64 lines of
  BASIC** (tech manual §Lower Text Space Extension) — so on a lightly expanded
  Atom, programs are short by necessity.

### Direct memory operators

Atom BASIC can reach memory directly, which matters on a machine where the screen
and I/O are memory-mapped (Atomic Theory):

- **`?addr`** — read/write a single byte. `?#8000=127` pokes a byte; `?#8000`
  reads one. (Period Atom hex notation uses a leading `#`.)
- **`!addr`** — read/write a 4-byte word.

These let early units poke the screen and I/O straight from BASIC before dropping
into assembly.

> **Variable-naming caution (general BASIC gotcha).** As on other 8-bit BASICs,
> avoid using language keywords as variable names. Atom BASIC's reserved set
> differs from Sinclair/Commodore BASIC; confirm against the source before
> finalising sample listings.
<!-- TODO: confirm Atom BASIC's variable-naming / reserved-word rules (and how many significant characters a name has) against Atomic Theory and Practice before writing .bas samples. -->

## Graphics from BASIC

Atom BASIC drives the MC6847 directly through built-in statements (Atomic Theory
§11):

- **`CLEAR n`** clears the screen and selects graphics mode *n* (one of the nine
  modes; see [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) § Graphics
  modes for the resolution/RAM table).
- **`MOVE x,y`** / **`DRAW x,y`** — move the graphics cursor / draw a line.
- **`PLOT k,x,y`** — a versatile plot statement (the `k` selects the plot
  operation).

Example line from the book (note the chained statements and period `#`/`;`
style):

```text
CLEAR0; MOVE 10,0; DRAW 60,50
```

<!-- TODO: verify a small Atom BASIC graphics listing assembles/runs once the Emu198x machine-acorn-atom core is capture-ready (it is currently in active development — see TOOLCHAIN-RESEARCH.md), then move it to code-samples/acorn-atom/basic/ and reference via CodeFromFile. Treat listings as illustrative until then. -->

## The built-in assembler — the teaching bridge (and the BBC ancestor)

This is the feature to build curriculum around, and the historical hook. Atom
BASIC contains a 6502 assembler reached with **square brackets** — type `[` and
BASIC starts assembling 6502 mnemonics; `]` returns to BASIC (Atomic Theory
§Assembler Programming, "To demonstrate the ATOM's assembler enter the following
line…").

How it works, at the level a unit needs:

- **`P` is the location counter** — you set `P` to the address where the code
  should assemble. (The later BBC BASIC renames this `P%`; the idea is the same.)
- **`[ ... ]`** brackets the 6502 mnemonics.
- **`LINK addr`** runs the assembled code from BASIC — the Atom's equivalent of
  the BBC's `CALL` — returning with `RTS`.

The book's canonical first example (verbatim):

```text
P=320;[INX; LDA 0,X; STA #B002; JMP 320;
]
```

then:

```text
LINK 320
```

This assembles a tiny routine at address 320 and runs it; because it writes to the
8255 port (`#B002`), "the ATOM will make a buzzing noise … playing the random
contents of its memory through its internal loudspeaker" (Atomic Theory). The
point for the curriculum is the *shape*: BASIC for setup and flow, brackets for
the machine code, `LINK` to run it — a learner can start in pure BASIC and replace
a slow inner loop with a bracketed assembly version, on one machine, in one
listing.

### The lineage: Atom → BBC BASIC

The Atom (1980) is **Acorn's first home computer**, and its built-in assembler is
the seed of the inline 6502 assembler that became one of BBC BASIC's standout
features a year later. The progression worth surfacing in curriculum:

- **Atom (1980):** `P` location counter, `[ ... ]` brackets, `LINK` to run — the
  first version, on a ~1 KB machine.
- **BBC BASIC (1981+):** `P%` location counter, `[ ... ]` brackets with `OPT` and
  a two-pass `FOR` idiom, `CALL` to run — the matured version. See the BBC sibling
  doc [`../bbc-micro/basic.md`](../bbc-micro/basic.md).

Same idea, refined: structured BASIC with machine code in the same listing, an
Acorn signature from the very first machine.

## Relationship to the assembly track

Atom BASIC supports both tracks the curriculum uses elsewhere — a **BASIC** track
and a pure **assembly** track — and, like the BBC, the built-in assembler lets the
two meet in the middle. A natural Atom pedagogy:

1. **BASIC** — short integer programs; direct memory with `?`/`!`; graphics with
   `CLEAR`/`MOVE`/`DRAW`/`PLOT`.
2. **BASIC + built-in assembly** — the bridge: `[ ... ]` 6502 inside BASIC, `LINK`
   to run, for the parts that need speed — and the place to tell the
   Atom → BBC lineage story.
3. **Assembly** — standalone 6502 via Asm198x, loaded by the Emu198x Atom core
   (see [`language/6502-quick-reference.md`](language/6502-quick-reference.md) and
   [`TOOLCHAIN-RESEARCH.md`](TOOLCHAIN-RESEARCH.md)).

<!-- TODO: decide and record the Atom track lineup (which games/modules, BASIC vs assembly vs bridge) in the module catalogue + a lineup decision, per state-lives-in-catalogues. This doc stays a pointer once that exists. -->

## See also

- [`reference.md`](reference.md) — platform entry doc and toolchain.
- [`language/6502-quick-reference.md`](language/6502-quick-reference.md) — the 6502 instruction set, the `#`-hex caution, and the built-in assembler syntax.
- [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) — memory map, video (MC6847 + graphics modes), sound.
- [`../bbc-micro/basic.md`](../bbc-micro/basic.md) — BBC BASIC's inline assembler, the matured descendant of the Atom's.
- Primary library:
  [`1980-atomic-theory-and-practice.md`](../../../../reference/by-system/acorn-atom/1980-atomic-theory-and-practice.md)
  (§Assembler Programming; §11 Graphics) — the authoritative Atom BASIC + assembler reference.
