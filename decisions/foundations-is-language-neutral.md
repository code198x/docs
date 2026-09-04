# Decision: Foundations is language-neutral, and none of it is the assembly arm

## The decision

**Numbers & Bits and Logic & Gates stop being assembly-arm material.** They join General
Programming as language-neutral modules a learner can take before choosing a machine or a
language.

**None of them gate a machine track.** Foundations stays what the architecture record calls
it, "a section of the site, not a sequence every learner walks". Assembly requires Numbers
& Bits; BASIC recommends it at the point it starts needing it; nothing blocks a reader who
wants a machine first.

**Logic & Gates splits in two**, at the dependency running through its middle.

## Why the old placement was wrong

[foundations-numbers-and-bits.md](foundations-numbers-and-bits.md) put the subtrack on the
assembly arm on one claim:

> It is the **bridge into assembly**: the BASIC track does not need it, assembly leans on it
> constantly.

The first half is false. The Spectrum BASIC track defines user-defined graphics with
`POKE USR CHR$` in four units, which is drawing a character as eight bytes of bit patterns,
and it discusses attribute clash. Its own prose gives the game away: it refers to "the
`POKE USR` **recipe** from Hi-Lo". A recipe is what you hand someone when the explanation
lives somewhere they have not been. The knowledge was on the other arm, so the track worked
around it.

Bits are not an assembly topic. They are how a computer represents anything, and a BASIC
learner meets them by the third unit of their second game. Truth tables are not an assembly
topic either: every `IF` anyone writes in any language is truth-functional reasoning.

## The shape

| Module | Holds |
|---|---|
| The Basics | a program, order, output, memory, input, arithmetic |
| Decisions | `IF`, `ELSE` and the chain, joining questions |
| Truth Tables | Logic & Gates movement 1: propositions, the table as a complete map, De Morgan's, proving two guards the same |
| Repeating | counted loop, loop-until, the loop that checks first |
| Structure | lists, named jobs, jobs that take and give back, debugging |
| Numbers & Bits | binary, hex, two's complement, the bit tools |
| Gates and the Adder | Logic & Gates movement 2: the same tables as circuits, then the adder |

Two orderings carry weight. **Truth Tables sits directly after Decisions**, while `AND` and
`OR` are still fresh from a reader having just written them. **Gates and the Adder follows
Numbers & Bits**, because an adder adds binary numbers and the payoff lands only for
someone who knows what one is.

That second point is why Logic & Gates splits. Its record designs it as one arc, reasoning
then payoff, but the payoff depends on a module the reasoning does not. Held together, one
half is always in the wrong place.

## What this amends

- **[front-of-curriculum-architecture.md](front-of-curriculum-architecture.md)** — "Numbers
  & Bits and From Source to Silicon are the assembly arm … they are not universal." Numbers
  & Bits leaves that sentence. From Source to Silicon stays: what an assembler does is a
  question you have to have earned, and the record is right that a BASIC learner arrives at
  it late, from the other direction, asking why their game is slow.
- **[foundations-numbers-and-bits.md](foundations-numbers-and-bits.md)** — the bridge-into-
  assembly framing goes, and so does the placement claim it rests on.
- **[foundations-logic-and-gates.md](foundations-logic-and-gates.md)** — one subtrack
  becomes two modules. Its "recommended side-path, not spine" holds for the whole
  Foundations shelf now, so it stops being a property of that course alone. Its gap
  statement also needs correcting: it says General Programming owns *what a conditional
  is*, which was true when it was written. General Programming now also owns *joining*
  conditions, because it cannot depend on a side-path to write a program that checks a
  guess is in range. The boundary is the tool against the reasoning: General Programming
  teaches you to write `alive AND ammo`; Truth Tables teaches you that `NOT (a AND b)` is
  `NOT a OR NOT b`.

## The cost, and the line that holds it

The runway to a machine gets longer. The site promises a real game on a real old machine,
and a reader who takes the shelf in order now meets six modules before choosing one. That
is the failure mode to watch: a beginner-friendly curriculum quietly becoming a degree.

The line that holds it is gating. Position and requirement are different questions, and
this record only answers the first. Nothing here gates a machine track, every module says
plainly who needs it, and a reader who wants to start a game on day one can.

## Numbers & Bits goes to pseudocode too

Settled after reading the six units. The vehicle goes, for the same reason it went from
General Programming, and the reading made the case stronger than the argument did.

Every BASIC snippet in the track is one line, and every one of them is `PRINT` with an
expression after it: `PRINT BIN 101`, `PRINT 256 - 1`, `PRINT 5 * 2`, `PRINT 1/3`. The
whole contribution is *here is a value, and here is what it comes to* — which is `SHOW` and
an output block, in a grammar the reader already has.

The explanations were never in the BASIC. Unit 4 teaches AND, OR, XOR and NOT in markdown
truth tables with the bit columns in plain text blocks; the listing arrives afterwards to
confirm the answer. Take it away and the teaching is untouched.

And the vehicle was costing the track something. Sinclair BASIC has no hex literal, so the
unit about hexadecimal can write `FF` in prose and in a table but never as a value in a
program. `HEX FF` says what that unit has spent six sections explaining. A vehicle that
cannot express the thing being taught is not paying for its seat.

## Reopened by this, not settled here

Whether Logic & Gates' two halves want different treatment from each other, and where
From Source to Silicon's own concreteness sits, are questions for when those get built.

## Drift triggers

- A module here gates a machine track, or a learner cannot reach a machine without
  finishing the shelf. → the runway is the thing this record is holding.
- A BASIC unit hands out a recipe for something Numbers & Bits explains. → link it; that
  workaround is the evidence this decision rests on.
- Truth Tables re-teaches joining conditions. → General Programming owns the tool; this owns
  the reasoning.
- Gates and the Adder gets read before binary. → it depends on Numbers & Bits and says so.

## Status

Active. Captured 2026-09-04. Amends
[front-of-curriculum-architecture.md](front-of-curriculum-architecture.md),
[foundations-numbers-and-bits.md](foundations-numbers-and-bits.md) and
[foundations-logic-and-gates.md](foundations-logic-and-gates.md). Builds on
[general-programming-is-language-neutral.md](general-programming-is-language-neutral.md),
whose reasoning it extends to the rest of the shelf.
