# Decision: the Foundations "Logic & Gates" subtrack

**Status:** ACCEPTED — 2026-07-08. Adds a **second Foundations subtrack** alongside
[`foundations-numbers-and-bits.md`](foundations-numbers-and-bits.md). This **amends**
[`front-of-curriculum-architecture.md`](front-of-curriculum-architecture.md)'s
line that Foundations' number/bit primer is "the whole of" Number Systems + Bit
Logic: it now holds two subtracks. The amendment is deliberate and narrow — Logic & Gates passes
the same three promotion tests the architecture doc inherited from the
[`cross-system-foundations.md`](cross-system-foundations.md) seed, and it joins as a
**recommended side-path, not spine** (see § Position). **Amended 2026-09-04** by [foundations-is-language-neutral.md](foundations-is-language-neutral.md): this subtrack becomes two modules, Truth Tables and Gates and the Adder, split at the dependency in its middle — the adder needs binary and the reasoning does not. Its "recommended side-path, not spine" now holds for the whole Foundations shelf rather than this course alone. Decided; build is a later
session, native to the raised bar.

## The gap it fills

Neither existing course teaches truth-functional reasoning. General Programming
owns *what a conditional is*; Numbers & Bits unit 4 owns AND/OR/XOR/NOT *as bit
tools* (masking, setting, clearing, eight lanes wide). Between them sits the
reasoning itself — truth tables as a thinking tool, combining conditions,
De Morgan's, proving two guards equivalent — which every track currently
hand-waves: the BASIC games tangle with compound `IF`s from Volume 1, and the
assembly tracks reason about flags and branch conditions with nothing upstream to
lean on.

The course was designed as **one arc**: the reasoning first, then the payoff that the
same truth tables *are* the machine — gates, then the adder that adds Numbers & Bits'
numbers.

**Amended:** it ships as two modules, because that arc has a dependency running through its
middle. The reasoning belongs directly after General Programming's decisions, while `AND`
and `OR` are fresh; the adder lands for nobody who has not met binary, so it follows
Numbers & Bits. See
[foundations-is-language-neutral.md](foundations-is-language-neutral.md).

**Also amended:** the gap statement below says General Programming owns *what a conditional
is*, which held when this was written. It now owns *joining* conditions too, since it
cannot lean on a side-path to check that a guess is in range. The boundary is the tool
against the reasoning: General Programming teaches you to write `alive AND ammo`; this
teaches you that `NOT (a AND b)` is `NOT a OR NOT b`.

## The promotion tests (all three pass)

1. **Identical across machines** — truth tables and gates carry no
   platform-specific substance.
2. **Teachable without a specific machine** — pure concept plus trivial
   illustration.
3. **Removes real redundancy** — condition/flag reasoning is currently re-taught
   (or skipped) per track; the adder demystification exists nowhere.

## Name

**"Logic & Gates."** Follows the layer's plain-neutral convention ("General
Programming", "Numbers & Bits") and names both movements; "Logic & Truth Tables"
named the first movement twice and the payoff not at all. Foundations sits outside
the "Meet \<thing\>" family, so no "Meet Logic".

## The shape (build target) — six units, two movements

**Movement 1 — reasoning:**

1. **True and false** — propositions, NOT; the truth table as the complete map of
   a question.
2. **AND, OR, XOR** — combining conditions, game-shaped throughout ("jump if
   button pressed AND on the ground AND NOT stunned"); XOR as "different".
3. **De Morgan's and simplification** — untangling nested `IF`s; why
   "NOT (dead OR finished)" is "alive AND unfinished"; truth tables as the proof
   that two different-looking guards are the same guard.

**Movement 2 — the payoff:**

4. **From conditions to gates** — the same three tables drawn as circuits; a
   signal is true/false on a wire.
5. **The half adder** — XOR is the sum, AND is the carry; adding two bits is
   nothing but unit 2's tables.
6. **The full adder and the ripple chain** — how the machine adds the numbers
   from Numbers & Bits; closes with an honest signpost to *Meet the Machine*.

**The runnable thread:** across movement 2 the learner builds the gates and then a
working 8-bit ripple adder — feed it two numbers, watch the carry ripple. Concrete,
working at every step, and the "it's just tables" point demonstrates itself.

**Settled 2026-09-04: the diagram is the runnable thing.** This record specified Sinclair
BASIC, and made a virtue of its missing XOR — noticing that `a<>b` *is* XOR on 0/1 values
was to be part of the lesson. Both halves moved: Numbers & Bits dropped its vehicle, and
the grammar gained `BITXOR`, so the gap that lesson was built around is gone.

The answer is not another language. Movement 2's claim is that a truth table and a circuit
are the same object, so the circuit itself carries the table: `LogicCircuit` draws the
gates from their own wiring and, with `interactive`, lets a reader toggle the inputs and
watch the wires carry, while a paired `TruthTable` highlights the row they have just set.
A carry rippling along a chain is better watched than printed. Pseudocode stays available
as a second view for readers who want one; it is not the vehicle.

**The scale beat.** The module ends by saying what these gates add up to: a half adder is
two of them, a full adder a handful, an 8-bit ripple chain a few dozen — and a modern
processor holds billions of transistors, of which a gate is a handful. That is the payoff
the whole arc is buying, and it only lands because the reader has just built one by hand.
Check the figure against a current part at build rather than quoting this record.

## Build conventions

- **Concreteness — pseudocode**, as Numbers & Bits, which dropped its Sinclair BASIC
  vehicle on 2026-09-04. Whether the movement 2 adder wants something more concrete than
  the grammar is the open question above.
- Built native to the raised bar; the General Programming primer remains the
  exemplar.

## Position — after Numbers & Bits, recommended side-path

Sits in Foundations **after Numbers & Bits** (the adder needs binary place value
in hand):

```
General Programming → Numbers & Bits → [recommended: Logic & Gates] → Meet the Machine
```

**Nothing gates on it.** *Meet the Machine* / *Meet Assembly* signpost it
("if tangled conditions — or how a machine can possibly add — mystify you, this
course exists") but keep their prerequisites unchanged, so it adds no October
launch burden. Promotion to core spine is a separate, explicit decision to revisit
once the course exists and Meet Assembly's flag units show whether they genuinely
lean on it.

## Drift triggers

- It teaches what a conditional/loop/variable *is* — belongs in General
  Programming, taught once.
- A masking/setting/clearing example appears — that is Numbers & Bits unit 4;
  here the operators are propositional, one lane at a time, citing N&B rather
  than re-teaching it.
- A latch, flip-flop, ALU, or CPU model appears — the adder is the terminus;
  memory and the CPU stay concrete in *Meet the Machine* per the architecture
  doc's Tier 3 ruling.
- A per-chip specific (a flag register, a ULA quirk) appears — belongs
  downstream.
- Units go pure-abstract with nothing to look at — the over-extraction failure the seed
  warned about. Truth tables, gate diagrams and worked output answer it.
- Anything starts *requiring* Logic & Gates as a prerequisite — that is the
  spine-promotion decision, made explicitly or not at all.

## Log

| Date | Event |
|------|-------|
| 2026-07-08 | Accepted. Brainstormed in the 198x umbrella session: arc scope (reasoning + gates-to-adder, latch/ALU explicitly out), terminus at the full adder, recommended-side-path position, and the name "Logic & Gates" all settled with Steve. Build deferred to its own session. |
