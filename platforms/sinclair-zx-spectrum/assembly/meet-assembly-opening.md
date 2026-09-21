# Meet Assembly — implementation and release

**Status:** All eight user-approved lessons are published and live-verified. The browser
package 0.4.0 is published and the site builds against the registry package. The recommended route is
**Meet Assembly → Meteor Storm**; Meteor Storm teaching checkpoints are next.

Apply the [introductory brief](meet-assembly.md) and [opening design](opening.md).
The website catalogue and authored pages own availability. This record explains
the source, execution environment and evidence behind the module.

## Sources and teaching boundaries

Sources live in `code-samples/sinclair-zx-spectrum/assembly/meet-assembly/opening/`.

| Source | Result | Machine-code size |
|---|---|---|
| `first-program.asm` | Red border, then hold | 6 bytes |
| `one-byte.asm` | One stored pattern becomes eight pixels | 18 bytes |
| `eight-rows.asm` | Eight explicit writes draw original artwork | 51 bytes |
| `row-loop.asm` | Data and a counted loop reproduce the artwork | 33 bytes |
| `draw-routine.asm` | Two callers use the same drawing routine | 52 bytes |
| `move-character.asm` | One bounded move per O/P press | 182 bytes |
| `clocked-character.asm` | Held movement paced by frame interrupts | 207 bytes |
| `debug-branch.asm` | Deliberately inverted left-edge branch | 207 bytes |
| `debug-trail.asm` | Deliberately incorrect erase source pointer | 207 bytes |

Seven core checkpoints serve eight lessons. The final two sources are fault cases,
not new game stages. Early programs own selected screen bytes; movement owns the
first character row. No arbitrary vertical screen-address calculation, background
restoration, collision, scoring or meteor system is hidden inside this introduction.

The editable byte and character lessons separate a prediction from an edit and
from actual machine state. A learner can explicitly keep their eight live artwork
bytes in session storage and import them into the loop and routine lessons.
Editing source alone never changes the emulator or its inspector.

## Assembly and launch

Recommend [Asm198x](https://asm198x.github.io/); upstream Pasmo is the alternative.
Use Asm198x's `pasmo` dialect with `--cpu z80`. The native verification uses
Asm198x 0.0.58 and upstream Pasmo 0.5.5, not the separately installed PasmoNext.
Both assemblers produce identical raw program bytes; tape names can differ.

The browser loads the real Asm198x WASM assembler on demand. Emu198x boots the
stock 48K ROM, installs machine code in RAM, and uses a BASIC CLEAR/RANDOMIZE USR
launcher. This avoids tape waiting while retaining the ROM environment and return
stack. Local instructions instead build a TAP and load it through the ROM.

The first programs remain in a hold loop. The press-driven program disables
interrupts. The timed program establishes IY=$5C3A, IM 1 and EI before HALT and
uses the ROM's interrupt service. It keeps input, state and rendering separate.
The ROM frame count and the program's own counters demonstrate actual elapsed
machine frames; sampled readings do not promise to show every intermediate value.

## Browser support

The module requires `@emu198x/zx-spectrum` 0.4.0. It adds direct `runCode` and
`runBasic` launch, canvas-free constructors, memory reads, bounded screen-write
and routine recordings, and debugger inspection/step/run-to controls. The BASIC
editor remains a separate, environment-gated trial.

The wrapper reuses the existing native runtime and debugger; it changes no CPU,
ULA or master-clock behaviour. Execution requests deliver pending input before
stepping. The page suspends normal frame ticks while paused in the debugger.
Source changes invalidate debugger labels until a fresh assembly. Reassembly
frees the old machine; navigation disposes its listeners and runner.

The loop lesson replays real captured screen writes. The routine lesson records
unconditional CALL/RET and bitmap writes with actual before/after registers.
Captures are bounded and incomplete results are labelled. A replay is not live
stepping. Lesson 8 uses actual stepping, disassembly and RAM with an execution
budget for run-to; an unreached label is not reported as a breakpoint hit.

## Guided investigation

Lesson 8 moves through reproduction, hypothesis, inspection, repair/retest and a
second fault. Observations and source edits persist when switching stages. The
initial view exposes position and A; Z appears for the zero test and PC for the
branch. Optional details contain other registers, bytes at HL and recent steps.

The source excerpt shows the instruction just executed alongside the actual next
instruction, so a taken branch remains explainable. Explanations stay folded
until requested. Repair requires editing and reassembly, followed by ordinary
movement and boundary checks. Revert explicitly restores faulty case 1. Loading
case 2 is an explicit action that replaces the source.

## Verification

The source-folder `verification/verify.py` compares native assembler output,
loads both tapes for every source into fresh emulated 48K PAL machines, checks
code and display RAM, exercises movement and timing, and confirms both intended
faults. The report records source, tool and output hashes. This is emulated
execution evidence, not original-hardware testing.

Website `scripts/verification/` owns focused browser checks for all interactive
lessons. They cover edits, saved artwork, actual screen/RAM agreement, recordings,
CALL/RET contracts, held and combined input, bounds, 3/6/12/0-frame intervals,
interrupt-disabled HALT, debugger predictions/repairs, stale-source handling,
downloads, keyboard operation and narrow layouts. Release verification also
checks lesson navigation, both themes and the installed registry package.

The full site build runs its unit and content checks. Nine existing decoder
checks are skipped in the local setup; CI provisions its decoder separately.
No pass here establishes physical-hardware behaviour or every arbitrary edited
program. The supported experiments and bounded failure cases define the evidence.

## Published release

The website release is [PR 441](https://github.com/code198x/website/pull/441),
commit `0ab014f2`; sources are in code-samples commit `97356e6`. The emulator
release is [PR 1511](https://github.com/emu198x/emu198x/pull/1511), npm 0.4.0.
The [live verification record](verification/meet-assembly-live.json) includes
HTTP results, all sixteen lesson/theme audits, the first-program edit and both
debugger repairs. The served WASM matches the registry package byte for byte.
The long navigation sweep had two transient request timeouts; separate fresh
browser checks passed. Production, link and deployment checks are green.

The scoped local Rust run passed 158 tests. Native verification passed all
eighteen fresh tape loads. The local site build passed 69 tests with nine existing
decoder skips, followed by all seven interactive suites and the module route,
source, theme and layout check against the installed registry package. Eight
existing shared-template accessibility checks also passed after repairing nested
main landmarks and keyboard scrolling in the lesson layout.
