# Decision: the Foundations "Numbers & Bits" subtrack

**Status:** ACCEPTED — 2026-06-30. Resolves the two build-time open questions left
by [`front-of-curriculum-architecture.md`](front-of-curriculum-architecture.md) for
the Foundations Numbers & Bits primer (Number Systems + Bit Logic). Does not change the
scope or position that decision fixed; it only settles name and shape and records the
build conventions. Built native to the raised bar
([`incremental-construction-units.md`](incremental-construction-units.md)); the
General Programming primer is the exemplar.

## What the architecture doc already fixed

The Numbers & Bits subtrack is **Number Systems** (decimal/binary/hex, place value,
bits/nibbles/bytes, two's complement, why binary, base conversion) **+ Bit Logic**
(AND/OR/XOR/NOT, masking, shifting) — and nothing else.

**Position superseded.** This record placed the subtrack on the assembly arm, on the
grounds that it was the bridge into assembly and that the BASIC track did not need it.
That second claim was wrong: the Spectrum BASIC track defines user-defined graphics with
`POKE USR CHR$` across four units, which is drawing a character as bit patterns, and its
own prose calls it a "recipe". Numbers & Bits is language-neutral and sits with the rest
of Foundations, gating nothing; assembly requires it, BASIC needs it the moment UDGs turn
up. See [foundations-is-language-neutral.md](foundations-is-language-neutral.md).

## Resolved here

1. **One combined subtrack, not two.** Number Systems flows into Bit Logic as a
   single arc, at `curriculum/foundations/numbers-and-bits/` — **since 2026-09-05 two
   modules, `counting-in-twos/` and `working-the-bits/`, cut between reading a byte and
   doing things to one; see [foundations-is-language-neutral.md](foundations-is-language-neutral.md)**. They pair too tightly
   to split — masking and shifting are meaningless until binary and place value are
   in hand — and one cohesive track mirrors General Programming. The architecture doc
   named one combined primer the likely shape; this confirms it.

2. **Name: "Numbers & Bits."** Neutral, like "General Programming" — Foundations sits
   *outside* the "Meet \<language\>" family, so it is not "Meet the Numbers." It names
   both halves plainly. The floated working titles ("Meet the Numbers", "How Computers
   Count") are set aside.

## Build conventions

- **Concreteness — pseudocode alone.** Superseded 2026-09-04: this record used to
  specify a concrete vehicle, Sinclair BASIC, on the grounds that the subtrack sat on the
  assembly arm where a chosen machine cost the learner nothing. It does not sit there, and
  the vehicle is gone. Reading the whole track settled it — every listing was one line of
  `PRINT` with an expression after it, while the explanations lived in truth tables and bit
  columns. The pseudocode grammar gained `BIN`, `HEX`, the `BIT*` operators and the shifts,
  so it now writes what these units teach; Sinclair BASIC could not write a hex literal at
  all. See [foundations-is-language-neutral.md](foundations-is-language-neutral.md) and
  [general-programming-is-language-neutral.md](general-programming-is-language-neutral.md).
- **Exclusions held** (per the architecture doc's Tier decisions and drift triggers):
  - **No display or sound model** — those stay concrete in Meet the Machine, where
    the byte-becomes-pixel is *felt*, not lectured. Number representation (a
    character is its code) is in scope; how the screen or a sound chip works is not.
  - **No per-chip specifics** — a SID register or ULA quirk belongs downstream.
  - **No general-programming concepts** — what a loop or variable *is* stays in
    Layer 1, taught once.

## The shape (build target)

Number systems first, then the bit logic that operates on them:

1. **Counting** — ten is a habit; the machine counts in twos; a number is a pattern
   of on/off (bit, nibble, byte).
2. **The same number, three ways** — decimal, binary, hex; place value; why hex is
   the shorthand for bits; the values that keep recurring (255, 256, 65535).
3. **Negatives** — writing a minus sign with no minus sign: two's complement and the
   wrap-around.
4. **Bit logic** — AND/OR/XOR/NOT as the tools that test and combine bits; masking,
   setting, clearing.
5. **Shifting** — sliding bits left and right, and why that is multiplying and
   dividing by two.

**Extended at build (2026-06-30) with fractions**, taking the number story from integers
onwards: a deliberate extension of the architecture's integers-only scope, kept
**conceptual** — the bit-layout and the implementation (8.8/16.16, the shifts) stay in the
machine courses.

**Split in two on 2026-09-05.** One unit carrying both schemes ran to 935 words against a
track averaging around 600, and the two halves are a problem and its answer rather than one
idea: unit 6 lets the point float and finds it approximate and, on these machines, slow;
unit 7 nails it down and gets the fast arithmetic back. The split also gave fixed-point room
for what it costs you and how to choose a scale, which had been compressed into
troubleshooting bullets.

## Drift triggers

- Numbers & Bits teaches how the screen or a sound chip works — that's Meet the
  Machine; here, only that a value *is* a number.
- A specific chip register or machine quirk appears — belongs downstream.
- It teaches what a loop/variable/conditional *is* — belongs in General Programming.
- It goes pure-abstract with nothing to look at — the over-extraction failure the seed
  warned about. Tables, bit columns, diagrams and worked output are what serve that now.
