# Decision: From Source to Silicon is five units of pseudocode, and the clock moves to the machine

**Status:** ACCEPTED — 2026-09-05. Builds the last Foundations module. Amends the seven-unit
sketch that lived in the module folder as `UNIT-BREAKDOWN.md`, now deleted.

## The decision

**Five units, in the same pseudocode as the rest of the shelf.** The program is not what
runs; translating as you go; translating once, in which the reader builds an assembler out
of two lists and a loop; what speed costs you; put it on the clock. The last two were one
unit at first, a bill of three costs with the send-off tacked on its end. The send-off is
where the module has been heading, so it is a unit of its own: what speed buys, and the
measurement pseudocode cannot make.

**The timed demonstration leaves the module.** The sketch's device was "the idea twice —
shape, then timed in Sinclair BASIC", and two of its seven units were empirical: put a
near-empty loop on a frame counter and watch the time climb. Pseudocode has no clock. Those
units go to the machine tracks, where the clock is real, as one unit per machine in *Meet
Assembly*: *the same thousand, three ways*, timed. That unit is filed, not built. The
hand-off names Meet the Machine for the briefing and the clock, and Meet Assembly for the
table, which is the distinction the architecture record's drift trigger exists to keep.

**Requires `structure` and `counting-in-twos`**, not `working-the-bits`. The toy assembler
uses lists; the numbers a processor runs are the ones from Counting in Twos. Nothing here
leans on the bit tools.

## Why

The shelf went pseudocode-only in this same sequence of work, and this module could not
follow the way the others did. Numbers & Bits used BASIC to *confirm* results the prose had
already taught, so dropping it cost nothing. Here the BASIC was the argument: "interpreting
is slower" is an empirical claim, and the sketch's answer to "says who?" was a stopwatch.
Stripped to prose it becomes assertion, which is the failure this shelf has spent two days
removing everywhere else.

So the module keeps what pseudocode can honestly carry. It **counts** rather than times: a
trace table showing "work out what this line means" happening on every one of a thousand
passes, then the same table with that column lifted out above the loop. Counting steps on
paper is something a beginner can check for themselves. It **builds** rather than describes:
the assembler is eight lines the reader already has the grammar for, and it produces the row
of numbers unit 1 showed as the machine's version of a program. The names (`INC`, `DOUBLE`,
`SHOW`) are invented so that they belong to no machine.

What it gives up is its biggest moment, and it says so. Unit 5 ends by telling the reader
that everything here was counted because there is no clock in pseudocode, and that the first
thing worth doing on a real machine is timing the loop both ways. The architecture record
already places this module as the bridge a BASIC learner reaches *after* games have made
the question real; that learner has a machine, and the clock belongs on it.

## Drift triggers

- A timing claim with a number in it appears in this module. → there is no clock here;
  count, or send the reader to the machine.
- The toy machine grows a fourth instruction or an operand. → three instructions and one
  box is enough to show the shape; more is a real instruction set, which belongs to a
  machine.
- The module presents itself to a BASIC learner as a prerequisite. → it is an answer,
  reached after the games raise the question.

## Relates to

- [front-of-curriculum-architecture.md](front-of-curriculum-architecture.md) — places the
  module as the assembly arm and the bridge back from BASIC.
- [foundations-is-language-neutral.md](foundations-is-language-neutral.md) — the shelf
  this completes, and the grouping it now sits in.
