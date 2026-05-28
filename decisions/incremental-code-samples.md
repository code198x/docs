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

### 2. Clean 10-step numbering, renumbered when too tight

Finished programs number in clean steps of 10 (10, 20, 30... or 100, 110, 120...). Choose enough spacing from the start that later units can drop new lines into 10-aligned gaps without disturbing their neighbours.

When an insert leaves no 10-aligned slot — the numbering has got too tight — renumber the program to restore clean 10-step spacing. **Renumbering to fix tightness is correct and expected; it is not the "noise" this decision warns against.** What to avoid is *gratuitous* renumbering — shuffling numbers between units for no reason. Renumber for a reason (restore spacing), never for none.

Never leave a finished program with off-step numbers like `65` or `145`. They read as unfinished, and a learner typing them in expects the canonical 10-step convention.

### 3. New code goes in gaps; renumber when the gaps run out

When adding a feature, drop new lines into empty 10-aligned gaps and leave existing code where it is. If you've run out of gaps, renumber the program — this unit and the units that share its code — so every line is a clean multiple of 10 again.

Re-spacing in the game brief is how you *prevent* tightness (plan the final shape so features land on 10s). Renumbering is how you *fix* tightness once it's happened. Both are legitimate; the wrong move is to leave the off-step numbers in place.

### 4. One structural change per unit

If a unit needs to restructure existing code (wrapping lines in a loop, moving a block to a subroutine, reorganising DATA), that restructuring IS the lesson. Explain it directly: "we're moving lines 50–70 inside a FOR loop." Don't combine restructuring with new features in the same unit.

### 5. The final unit is not a dumping ground

The last unit of a game should add 2–3 lines of polish (a title, a sound effect, a small visual touch) — not 20 new features at once. If the final unit has a huge diff, the game has too few units. Add intermediate steps.

### 6. Each unit produces a runnable program

Every code sample must compile/run on its own. The reader types (or loads) the complete program and sees a result. No "this doesn't work yet — we'll fix it next unit."

### 7. Reserve gaps on purpose, and explain them

Leave 10-aligned gaps where later units will insert lines, and tell the reader the gap is deliberate — both when you leave it and when you fill it. A jump from 50 to 130 reads as a mistake unless the prose says *"that gap is room we'll use next unit."* When a later unit drops a line into a reserved slot, call back to it: *"the title goes in the gap we left at line 30 — nothing else moves."* That turns an apparent oddity into the actual lesson: BASIC programmers numbered in tens precisely so a program could grow without renumbering.

This is the reader-facing half of rules 2 and 3: those keep the numbering clean, this makes the reserved space legible instead of arbitrary. The cost is honest — a gap reserved for content several units away (a title that arrives at unit-07) is harder to motivate than one filled next unit, so reserve where you can explain it, and lean on the call-back when you fill it. Story Builder unit-02's "Why line 130?" section is the model.

## Relationship to spiral-and-incremental.md

[spiral-and-incremental.md](spiral-and-incremental.md) defines the conceptual progression model: incremental within a phase, spiral across phases. This decision adds a concrete mechanical constraint: the CODE must also progress incrementally. A unit can introduce one new concept AND change only a few lines — these reinforce each other.

## Implications for existing content

The V1 BASIC games (Story Builder through Touchdown) and V2 games (Cipher, Quiz Master) predate this decision. Many have units where the diff is too large — particularly final units that add polish across the whole program. These need reworking to split large diffs into smaller intermediate steps. This is quality debt, not a style preference.

## Drift triggers

- A code sample diff between consecutive units exceeds ~8 lines of meaningful change (a deliberate renumber-to-restore-spacing is exempt — that renumber IS the unit's change, and should stand alone).
- Line numbers are shuffled between units for no reason at all — not even to restore 10-step spacing. (Renumbering *because* the spacing got too tight is the correct fix, not a trigger.)
- A finished program contains line numbers that aren't multiples of 10 (e.g. `65`, `145`) — the spacing got too tight and wasn't renumbered.
- A program leaves a multi-line line-number gap that the prose never explains.
- The final unit of a game has a diff larger than any intermediate unit.
- A unit combines restructuring AND a new feature.
- A brief plans fewer than 6 units for a game with 30+ lines of final code.
- "We'll add that in the polish unit" — if "that" is more than 2–3 lines, it needs its own unit.

## Status

Active. Captured 2026-05-26. Rule 7 (reserve gaps on purpose, and explain them) added 2026-05-28. Reinforces [spiral-and-incremental.md](spiral-and-incremental.md). Informs game briefs and the unit specification.
