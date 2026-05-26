# Decision: Incremental Code Samples

## The decision

Each unit's code sample is the previous unit's code sample plus a small, visible change. The reader should be able to diff the two in their head: "these 3–5 lines are new, everything else is the same." Wholesale rewrites between units are not allowed.

This applies to all tracks (BASIC, assembly, AMOS) and all platforms.

## Why

When 80% of the code changes between units, the reader can't isolate the lesson from the noise. They're not learning "how RESTORE works" — they're trying to re-parse an entire unfamiliar program that happens to contain RESTORE. The teaching value of incremental progression comes from the delta being small enough to understand at a glance.

It also mirrors how programs actually evolve. You don't throw away your program and start fresh when you add a score counter. You add three lines to the working program. That's the process we're teaching: a program grows from a seed, one change at a time.

Evidence from our own curriculum: Lucky Number unit-04→05 adds exactly one line (`GO TO 30`) and teaches the entire concept of loops. That's the gold standard. By contrast, Quiz Master unit-04→05 changed 46 lines and removed 30 — the reader has to re-read the entire program. Same concept count (one), wildly different teaching effectiveness.

## Rules

### 1. Small diffs between consecutive units

Each unit's code sample should differ from the previous by no more than ~5–8 lines of meaningful change. Trivial renumbering doesn't count as "change" but does count as noise — avoid it.

If a concept genuinely requires more than 8 lines of new code, split it into two units. "Too much new code" is the signal to split, not to batch.

### 2. Stable line numbers

Choose line numbers with gaps from the start (10, 20, 30... or 100, 110, 120...). Don't renumber existing lines between units unless the renumbering IS the lesson. Renumbering is noise that makes the diff unreadable.

### 3. New code goes in gaps, not restructured throughout

When adding a feature, use empty line-number gaps to insert new lines. Don't move existing code around to "make room." If you've run out of gaps, that's a sign the line numbering was too tight at the start — fix it in the game brief, not mid-curriculum.

### 4. One structural change per unit

If a unit needs to restructure existing code (wrapping lines in a loop, moving a block to a subroutine, reorganising DATA), that restructuring IS the lesson. Explain it directly: "we're moving lines 50–70 inside a FOR loop." Don't combine restructuring with new features in the same unit.

### 5. The final unit is not a dumping ground

The last unit of a game should add 2–3 lines of polish (a title, a sound effect, a small visual touch) — not 20 new features at once. If the final unit has a huge diff, the game has too few units. Add intermediate steps.

### 6. Each unit produces a runnable program

Every code sample must compile/run on its own. The reader types (or loads) the complete program and sees a result. No "this doesn't work yet — we'll fix it next unit."

## Relationship to spiral-and-incremental.md

[spiral-and-incremental.md](spiral-and-incremental.md) defines the conceptual progression model: incremental within a phase, spiral across phases. This decision adds a concrete mechanical constraint: the CODE must also progress incrementally. A unit can introduce one new concept AND change only a few lines — these reinforce each other.

## Implications for existing content

The V1 BASIC games (Story Builder through Touchdown) and V2 games (Cipher, Quiz Master) predate this decision. Many have units where the diff is too large — particularly final units that add polish across the whole program. These need reworking to split large diffs into smaller intermediate steps. This is quality debt, not a style preference.

## Drift triggers

- A code sample diff between consecutive units exceeds ~8 lines of meaningful change.
- Line numbers are renumbered between units with no pedagogical reason.
- The final unit of a game has a diff larger than any intermediate unit.
- A unit combines restructuring AND a new feature.
- A brief plans fewer than 6 units for a game with 30+ lines of final code.
- "We'll add that in the polish unit" — if "that" is more than 2–3 lines, it needs its own unit.

## Status

Active. Captured 2026-05-26. Reinforces [spiral-and-incremental.md](spiral-and-incremental.md). Informs game briefs and the unit specification.
