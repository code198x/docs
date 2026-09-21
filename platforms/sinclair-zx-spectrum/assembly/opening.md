# Spectrum assembly — replacement opening

**Status:** Replacement direction agreed following the [opening review](course-review.md).
This is the working teaching design. Meteor Storm is accepted after native play; its [teaching progression](../games/meteor-storm/lesson-brief.md) now has
[seventeen executed programs](../games/meteor-storm/checkpoints.md). Full game lessons
are the next authoring work, with no fixed lesson-count target.

## Promise

Learn to give the Z80 instructions, understand what those instructions change,
and use them to make a small game worth playing. Readers need neither BASIC nor
completion of Foundations. Explain programming concepts locally as needed;
comparisons with another language are optional.

The existing game names, engine and sixteen-unit introduction impose no
constraints on the replacement. Preserve useful experiments only when they
serve this opening. Do not turn the instruction set into a checklist that must
be completed before play begins.

## Two modules

The agreed route is **Meet Assembly → Meteor Storm**. The
eight introductory lessons are user-approved. Its [teaching brief](meet-assembly.md)
owns the first experiments; the [game progression](../games/meteor-storm/lesson-brief.md)
owns their application and deeper game systems.

## First contact with the machine

Use a separate introductory module of purposeful experiments that feed into the first game. These
are outcomes to establish, not a fixed set of units:

| Outcome | Explanation needed | Evidence the reader can inspect |
|---|---|---|
| Build a visible change | Source, assembler, output, target; instruction versus directive | Change a value, assemble, load and observe it |
| Draw an object of our own | Bytes and bits; bitmap versus attributes; addresses and labels | Edit an eight-row shape and identify the changed pixels |
| Control its position | Memory-held state, input, comparisons, branches and boundaries | Move left/right; explain a rejected move at an edge |
| Make the world update | A repeated input/update/draw cycle and an explicit clock | An object moves without further input; changing its update interval has a predictable effect |
| Find a fault | Expected state, actual state, register/memory inspection and a small hypothesis | Step through one routine and explain the first disagreement |

Explain the initial hold loop and startup state to the extent needed to use them;
return to interrupts and the stack when the work needs their detail. Name every
supplied dependency and its role. A short helper may be developed separately and
then reused with a stated input/output/clobber contract; there is no unexplained
starter engine.

## First complete game

The [Meteor Storm brief](../games/meteor-storm/brief.md) defines the selected
first project: race through a fixed scattered storm, dodging gently drifting
meteors and collecting vertical stars. One hit ends the run. Unlimited held boost
doubles course progress and star value; faster finishes earn a larger bonus.
Separate session records reward fastest completion and highest score. The user
accepted this native endpoint. Author from its executed teaching checkpoints, splitting lessons wherever
understanding requires a smaller step. A driving game remains a later possibility, not a promised sequel.

Aim for an early playable choice, then deepen it. Build graphics, sound and
readability as their mechanics arrive. A title and retry should complete a game
whose central activity already works; they should not be the first opportunity
to assess its appeal.

Keep game state separate from the image. Position, object type, activity and
contact rules live in explicit data. Colour changes may affect readability, but
must not change solidity, scoring or damage. Start with the smallest representation
that expresses the agreed game, not a general entity framework.

Teach a drawing method that fits the prototype. Smooth pixel movement is a useful
candidate, not a requirement to introduce masking, pre-shifting, buffering and
optimisation at once. If an implementation shortcut later needs replacing, make
the need observable and the transition understandable.

## Tools and explanation

Use a modern host with Asm198x, explicitly selecting stock Z80, and a named 48K
Spectrum emulator configuration. Explain cross-development and distinguish it
from the target's capabilities. Recommend Asm198x as the primary assembler and give upstream Pasmo as a verified
alternative for the portable opening sources. The existing Asm198x WASM package
and website editor provide an in-page route using the same source. See the
[opening implementation](meet-assembly-opening.md) for actual parity and execution
evidence. Use one primary build command and loading path;
introduce snapshots as a debugging convenience separately from a distributable
tape. Establish stack, entry address and interrupt assumptions in the source.

Give exact editing instructions and an inspectable complete source at each
runnable stage. Optional diffs may help comparison. Explain registers, flag
effects and signed/unsigned interpretations for the instructions actually used.
Provide a concrete debugger exercise with the selected tool, rather than merely
asking readers to open an unspecified memory view.

Use shared subjects for depth: input and response in Game Feel, quantities and
contact in Maths, representation in Foundations. Explain immediate essentials
inside the assembly lesson; unavailable shared lessons cannot be prerequisites.

## Evidence required before lesson authoring

- The selected game is accepted after native play, including held and combined
  input, difficulty, readable consequences, sound and retry.
- A stock-target build and fresh tape load reach the complete game.
- State, drawing and contact remain consistent at edges and unusual overlaps.
- The code can be decomposed into meaningful stages with explained dependencies.
- Every stage transition matches its stated starting and ending sources.

Only then choose lesson boundaries and prepare a replacement publication plan.
Existing URLs should continue to reach useful material during the transition.
The later assembly lineup remains open, and BASIC performance revisits remain a
separate investigation rather than an entry requirement.
