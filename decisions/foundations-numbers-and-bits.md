# Decision: the Foundations "Numbers & Bits" subtrack

**Status:** ACCEPTED — 2026-06-30. Resolves the two build-time open questions left
by [`front-of-curriculum-architecture.md`](front-of-curriculum-architecture.md) for
the Foundations Layer 2b primer (Number Systems + Bit Logic). Does not change the
scope or position that decision fixed; it only settles name and shape and records the
build conventions. Built native to the raised bar
([`incremental-construction-units.md`](incremental-construction-units.md)); the
General Programming primer is the exemplar.

## What the architecture doc already fixed

Foundations Layer 2b is **Number Systems** (decimal/binary/hex, place value,
bits/nibbles/bytes, two's complement, why binary, base conversion) **+ Bit Logic**
(AND/OR/XOR/NOT, masking, shifting) — and nothing else. It is the **bridge into
assembly**: the BASIC track barely needs it, assembly leans on it constantly. It sits
after General Programming, before Meet the Machine:

```
General Programming → Numbers & Bits → Meet the Machine → Meet Assembly → games
```

## Resolved here

1. **One combined subtrack, not two.** Number Systems flows into Bit Logic as a
   single arc, at `curriculum/foundations/numbers-and-bits/`. They pair too tightly
   to split — masking and shifting are meaningless until binary and place value are
   in hand — and one cohesive track mirrors General Programming. The architecture doc
   named one combined primer the likely shape; this confirms it.

2. **Name: "Numbers & Bits."** Neutral, like "General Programming" — Foundations sits
   *outside* the "Meet \<language\>" family, so it is not "Meet the Numbers." It names
   both halves plainly. The floated working titles ("Meet the Numbers", "How Computers
   Count") are set aside.

## Build conventions

- **Concreteness — pseudocode + one concrete vehicle (Sinclair BASIC)**, exactly as
  Layer 1. Each idea is stated in neutral pseudocode and shown running in Spectrum
  BASIC, framed as "here in BASIC; the same idea everywhere." Spectrum BASIC suits it
  (`BIN` for binary literals, `CODE`/`CHR$` for character codes).
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

## Drift triggers

- Numbers & Bits teaches how the screen or a sound chip works — that's Meet the
  Machine; here, only that a value *is* a number.
- A specific chip register or machine quirk appears — belongs downstream.
- It teaches what a loop/variable/conditional *is* — belongs in General Programming.
- It goes pure-abstract with no BASIC illustration — the over-extraction failure the
  seed warned about.
