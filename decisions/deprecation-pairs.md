# Decision: Deprecation Pairs — teach the naive version first

## The decision

A hard technique is taught in two halves, across games:

1. **The naive version first** — deliberately simple, honestly limited, and *taught knowing it will be replaced*. The learner builds it, ships it, and it works.
2. **The upgrade later** — introduced only once the learner has *felt the naive version's limit* in their own running program. The limit is the motivation; the technique is the answer to a problem they already have.

The pair is bound by two authoring habits:

- **Name the assumption out loud.** When a unit leans on a simplification, say so in the prose — *"this works because the floor is always blank."* A flagged assumption is deferred teaching; an unflagged one is hidden magic that bites the reader later.
- **Vocabulary before syntax.** Introduce the named mental model before the instruction that manipulates it — *"the screen is a grid of cells; each cell's colour is one attribute byte"* before `LD (HL), A`. The reader needs the concept to hang the opcode on.

This applies to all tracks, but it is load-bearing for **assembly**, where the hardest techniques (pre-shifted sprites, masking, Y-sort) are exactly the ones a beginner cannot absorb cold.

## Why

The Spectrum assembly cliff ([spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md)) was not only *too much per unit* — it was *advanced technique with no motivation*. Masking, taught before the learner has ever seen a sprite erase the wall it walked over, is an abstract chore. Taught *after* — when their own lamplighter has just rubbed a hole in the scenery — it is the obvious fix to a problem they can see on screen. Same technique, opposite reception.

Motivation precedes technique. The naive version manufactures the motivation: it is the "before" picture that makes the "after" land. This is also how real development feels — you write the simple thing, hit its wall, and reach for the better thing. Teaching the upgrade first inverts the genuine order and teaches a technique as dogma rather than as a solution.

The naive version is not a mistake we apologise for. It is a correct, shippable solution at its scale — and the deliberate "before" half of the pedagogy.

## How this differs from spiral progression

[spiral-and-incremental.md](spiral-and-incremental.md) and this decision are complementary, not the same move:

- **Spiral *deepens* a technique that stays.** Movement gains animation timing; the beeper driver gains an SFX layer. The original technique is still there, doing more in a richer context. You build *up*.
- **A deprecation pair *replaces* a deliberately-naive technique.** Save/restore is retired in favour of masking; cell-step movement is retired in favour of pre-shifted movement. The "before" is superseded, on purpose. You swap *up*.

A curriculum needs both: spiral to compound skills, deprecation pairs to introduce the hardest techniques gently and with motivation.

## What this means

### Plant the "before" in the early games

Gloaming is the **root of the track's deprecation tree** — it invents the naive versions every later game upgrades (see its [per-unit plan](../platforms/sinclair-zx-spectrum/games/gloaming/per-unit-plan.md) § *Deprecation-pair seeds*). The settled pairs:

| Naive version (born in) | Upgraded to (in) |
|---|---|
| Cell-step movement (Gloaming) | Pre-shifted smooth movement (*Smooth Motion*) |
| Single-draw glyph + 9-byte save/restore (Gloaming) | Masked sprite drawing (*Overlap*) |
| Coloured-pip progress readout (Gloaming) | Rendered digit HUD (*Shadowkeep*) |
| A single beeper blip (Gloaming) | SFX driver + composed theme (*Shadowkeep*) |
| One screen (Gloaming) | Multi-room flick world (*Shadowkeep*) |
| Flat draw order (early games) | Y-sort + isometric (*Greypeak*) |

### Author the pair as a pair

- The "before" unit names its own assumption and flags that a later game will lift it — without teaching the upgrade. *Don't* pre-explain masking in the save/restore unit; that re-loads the early game (the drift trigger gentle-ramp guards).
- The "after" unit opens by *re-showing the limit* in the learner's running program, then introduces the upgrade as its resolution. It cites the "before" unit by name.

### Keep the budget

A deprecation pair is two techniques across two games, not two techniques in one. Introducing the naive version and its upgrade in the same game breaks the per-game technique budget ([spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md)) and erases the felt-limit gap that makes the pair work.

## Drift triggers

- An "after"/upgrade unit that doesn't first re-show the limit in the learner's own program — the motivation is the point; don't skip to the technique.
- A "before" unit that pre-explains its upgrade ("we'll mask this properly later, but for now…") — that re-loads the early game and spoils the felt limit. Name the *assumption*, not the future fix.
- Teaching the advanced version with no naive predecessor — the cliff returning under a new name.
- The naive version framed as wrong or apologised for, rather than as a correct, shippable solution at its scale.
- A unit that introduces a technique with no vocabulary laid first — syntax before the mental model.
- Both halves of a pair landing in the same game — collapses the budget and the gap.

## Status

Active. Captured 2026-06-01. Formalises the deprecation-pair pedagogy named in passing by [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md) and seeded by Gloaming's per-unit plan. Complements [spiral-and-incremental.md](spiral-and-incremental.md) (deepen vs replace) and the mechanical diff discipline in [incremental-code-samples.md](incremental-code-samples.md). Informs game briefs and the unit specification.
