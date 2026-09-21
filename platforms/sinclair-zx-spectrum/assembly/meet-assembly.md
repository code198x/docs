# Meet Assembly — introductory module

**Status:** All eight user-approved lessons are published and live-verified.
The title is **Meet Assembly**. Seven runnable checkpoints and two fault cases
support the introduction. The [implementation record](meet-assembly-opening.md)
owns execution and release evidence.

Apply the [opening design](opening.md) and [unit specification](../../../specifications/unit.md).
The route is **introductory module → Meteor Storm**. Neither BASIC nor prior
Foundations attendance is required. This replaces the old introduction on its
teaching merits; it is not a commitment to retain its sixteen-unit structure.

## Promise and boundary

Make the machine do something, explain the state that changed, and investigate
when the result differs from a prediction. Short visible experiments introduce
the vocabulary and tools before a game combines them.

End with a small controllable marker and an observable update rhythm. There are
no meteors, object pools, collision rules, scores or game engine in this module.
A small input-and-display experiment is enough of a destination. The first game
then has room to teach game construction rather than reintroducing every word.

## Lesson sequence

| Lesson | Observable result | Concepts and check |
|---|---|---|
| 1. Change the border | Run six bytes of code, then change the colour | Host and target, source and machine code, A, ports, directives, labels and a hold loop. |
| 2. A byte becomes pixels | Predict eight pixels and inspect their actual byte | Bits, binary, addresses, registers versus RAM, bitmap versus attributes. |
| 3. Build an eight-row shape | Design a character and investigate a misplaced row | Screen layout, explicit destination writes and artwork as data. |
| 4. Draw with a counted loop | Reproduce the character and replay actual writes | HL, DE, B, pointer steps, DJNZ, bounded iteration and wrap. |
| 5. Call a drawing routine | Draw twice and inspect calls and returns | CALL/RET, stack, caller-supplied inputs, changed registers and a routine contract. |
| 6. Move your character | Move one cell per O/P press and inspect the old and new cells | Active-low input, masks, release-to-rearm, stored state, flags, bounds, erase/redraw. |
| 7. Give movement a clock | Hold a key; compare three, six and twelve frame intervals | ROM interrupt dependency, IM 1, IY, EI/HALT, countdown, opportunities versus moves, overrun limits. |
| 8. Find the first wrong step | Investigate and repair two faulty variants | Reproduction, hypotheses, breakpoints, predictions, actual state, a minimal repair and boundary retests. |

The final lesson introduces readings when needed and folds away explanations and
repairs. Case 1 guides the investigation; case 2 asks for more independent work.
Neither adds a progression checkpoint. Inspectors must show actual machine state;
recorded execution must be distinguishable from live stepping.

The clock experiment explicitly borrows the stock 48K ROM's service and preserves
its expected environment. Detailed private interrupt setup belongs in Meteor Storm,
where the game gives it a purpose.

## Handoff to Meteor Storm

Readers should be able to assemble and load a small program, distinguish register
and memory state, trace a branch or loop, call a routine with a stated contract,
read a key, move a stored position and inspect a failure. They need awareness of
a clock, not mastery of interrupt modes, sprite optimisation or the instruction set.

[Meteor Storm](../games/meteor-storm/lesson-brief.md) begins in a fresh project
with a complete, inspectable version of the small drawing/input basis. Name each
reused routine and link back to the experiment that explains it. Recap concepts
at use; do not depend on an opaque binary, accumulated engine or undocumented
final state from a previous game. Readers with equivalent experience can enter
there using that complete source and the short recap.

Keep source transitions and visible outcomes reproducible. The release checks
both assemblers and fresh tape loading for every source, alongside browser
execution. Hardware and instruction claims cite primary sources in the lessons.

## Tooling routes

Recommend Asm198x and give upstream Pasmo as an alternative, using the same
portable source and checking it with both tools. For these opening programs use
Asm198x's `pasmo` dialect and explicit Z80 target, not Next extensions. Do not
confuse a PasmoNext executable with upstream Pasmo when claiming compatibility.

Asm198x already has a Z80 WASM package, and the website already has an editable
`AssembleAndRun` component. Reuse it for a low-friction in-page experiment beside
the local build/load instructions. The learner should understand that the real
assembler produces the same machine code in both routes. The
[opening implementation record](meet-assembly-opening.md) distinguishes native,
WASM and browser execution evidence.
