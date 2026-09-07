# Bright Spark

**Status: agreed replacement specification, approved on 6 September 2026.** The opening route **Meet BASIC → Bright Spark → Touchdown** is agreed. The seven teaching groups and 16-round challenge are implementation defaults to test and refine; the first two replacement lessons were approved on 7 September 2026. The [board-and-cue prototype record](prototype.md) distinguishes implementation and execution evidence from the specification.

**Target:** stock 48K ZX Spectrum, 50 Hz display configuration, Sinclair BASIC, keyboard and beeper. No expansion, Spectrum Next feature or assembly helper.

Apply the [project charter](../../../../PROJECT.md), [unit guidance](../../../../specifications/unit.md) and [Meet BASIC direction](../../basic/meet-basic.md). All fifteen Meet BASIC lessons are published. Bright Spark develops a sustained game from those capabilities; it does not require attendance at those lessons.

## Experience and finished scope

The computer presents a sequence using four labelled panels and distinct short tones. The player repeats the order with keys 1–4. Each successfully completed round adds one new choice to the existing sequence. A wrong valid choice ends the game; an unrelated key does not consume a choice. Consecutive identical choices are allowed and must be visibly and audibly separable.

Retain the mechanic because its representation and behaviour are closely connected: the stored sequence drives both presentation and checking. Making a panel respond is satisfying early; building a longer sequence gives that response a purpose. The game suits BASIC because it alternates presentation and input rather than requiring a continuously simulated world. Waiting and beeper output have costs, but those costs can be understood within this design.

Propose a **16-round challenge** as the initial finished scope. Completing round 16 produces a success ending before any seventeenth item is appended. This is an adjustable design default, not a claim about human memory or the maximum capacity of a Spectrum string. A finite target makes the ending and boundary tests explicit. Playtesting may justify another cap without changing the representation. Do not describe the sequence as unlimited.

Score means **rounds completed**: 0 after failing the first round, 3 after completing three rounds and failing the fourth, and 16 after finishing the challenge. Show the failed round separately if useful. Use neutral, specific wording; omit the existing ability ratings and unsupported claims about a universal seven-item memory limit.

The complete game needs instructions before input, clear WATCH and YOUR TURN phases, an ordinary quit route, a failure or success result, replay with fresh state, and a saved program that loads and plays. It does not need music, high-score persistence, a centring framework, sprites, machine code or a fixed source-line budget. Saving the program is required; saving a personal record is a different feature.

## What exists and what changes

Reviewed on 6 September 2026:

- [Six lesson files and index](https://github.com/code198x/website/tree/c24abe76694749245d7a87646af22548dbe08b1d/src/content/curriculum/sinclair-zx-spectrum/basic/bright-spark).
- [Six BASIC sources](https://github.com/code198x/code-samples/tree/eb253f79dc4029ac256d2b40da30196d23da8925/sinclair-zx-spectrum/basic/bright-spark), one per existing unit. No capture manifest or verification script was found under this game directory. The website has images; their existence does not verify the revised route.
- The existing game brief and completed Meet BASIC source/lesson mapping. This document replaces the old brief rather than appending competing decisions.

The following are source-review findings. Bright Spark was not executed during this specification review.

| Existing material | Finding | Recommendation |
|---|---|---|
| Unit 1, `board.bas`, 550–620 | Each filled row repeats its panel digit. Drawing and a routine arrive together in a compressed listing. | Retain character-cell panels. Build one rectangle first, add one persistent label per panel, then assemble the board. Extract repeated work when the reader has seen the work itself. |
| Units 2–6, flash routine 640–740 | Lines 700 and 730 repaint with spaces: neither restores the digit. The prose describes temporary blanking, but the resting repaint also lacks the label. | Separate identity from cue state. Preserve or redraw labels during both lit and resting states. Test all four after repeated cues. |
| Unit 2, random flash | Random selection hides which panel a reader is trying to check. | Begin with a deliberately selected panel, then exercise all four. Reintroduce chance when extending the game sequence. |
| Unit 3, `sequence.bas`, 140–230 | It starts with an empty string, appends once and stops after playback. There is no growing sequence across rounds in this checkpoint. The prose calls strings unlimited and bundles concatenation, indexing, `LEN`, `STR$` and `VAL`. | Trace a fixed sequence first, separate representation from playback, then add growth after the player can complete a fixed round. Explain memory limits and representation assumptions. |
| Units 4–6, 270–280 | The empty-input test and assignment read `INKEY$` separately. A release between reads can change the value. This is a timing risk identified from source, not a reproduced emulator defect. | Capture once into `k$`, test that value, and validate before conversion. Specify release handling and phase transitions explicitly. |
| Units 5–6, 390–440 | `score=LEN s$-1` counts completed rounds after failure, while the screen says the sequence was that long. Unit 5's description and caption also disagree with its explanatory paragraph. | Store or derive one well-defined completed-round score and use matching text. Test first-round failure and cap completion separately. |
| Unit 6, 510–530 | Replay is unconditional after `PAUSE 0`; there is no ordinary quit choice. A general centring routine is imported from an earlier Oracle version. | Add replay/quit choices with local explanations. Use a fixed, readable title position unless a general routine has a demonstrated purpose. |
| Index and lesson prose | Assumes Reflex and the separate Oracle/Lucky Number courses; treats `BRIGHT` as already taught; points onward to Hi-Lo. | Link to specific Meet BASIC explanations without requiring attendance. Teach `BRIGHT`, indexing and routine inputs here. Point the recommended next route towards Touchdown. |

## Knowledge used and taught

Briefly recall numeric/string variables, `IF`, `FOR`/`NEXT`, `GO TO`, `GO SUB`/`RETURN`, `PRINT AT`, colours, `BEEP`, random ranges and keyboard polling. The opening supplies the exact small program and editing actions; no external scaffold or earlier project file is required. Explain each new keyword's Host Keyboard entry when it first appears.

Develop deliberately:

- **Representation:** one panel choice per digit in a string. The text `"3"` and the number `3` serve different operations. String indices begin at 1; screen coordinates begin at 0. Neither is a BASIC line number.
- **Operations:** append a choice, obtain the length, read the item at a position, traverse and compare. Trace `"314"`, repeated choices such as `"22"`, and the first/last valid indices before random input can obscure errors.
- **Conversion:** `STR$` obtains a textual representation; `VAL` evaluates a numeric expression. It is broader than “undo STR$”. Only convert a character already established as a valid panel identifier. Do not present `VAL` as general safe validation of arbitrary input.
- **Structure:** a routine can operate on a caller-supplied shared variable. Sinclair `GO SUB` does not create the local parameters and value-return semantics used by Foundations pseudocode. Document what each routine reads, changes and restores.
- **Coordination:** presentation, input, judgement and restart visit different parts of the program. A held key or previous round's index must not leak into a new phase unnoticed.
- **Costs:** playing a sequence of length n requires n cues and n comparisons on a successful round. Replaying lengths 1 through n requires 1+2+…+n cues; longer games grow in duration as well as difficulty. Appending strings uses memory and may involve copying; do not state an exact allocation or timing cost without measurement/source evidence.

A string is appropriate for four one-character identifiers. A separate variable for every position is awkward to traverse; a fixed numeric array is a plausible alternative when teaching richer items or predetermined capacity. Compare those choices without requiring an array implementation here. Multi-digit identifiers would break the one-character-per-item convention: `"112"` alone cannot distinguish 1,1,2 from 11,2.

## Proposed runnable teaching sequence

These seven groups are provisional lesson boundaries, not a quota. Split an overloaded group after developing the sources; do not compress steps merely to retain seven lessons. Every numbered checkpoint is a complete runnable state, accompanied by exact add/replace/delete instructions. Short changed routines may accompany a linked full source as the program grows; essential instructions must not depend on CodeDiff.

| Group | Runnable growth and result | New learning, design and assets | Checks |
|---|---|---|---|
| **1 — Four choices on the screen** | Draw one labelled rectangle; expand to four labelled positions and a short instruction line. | Fill character cells with spaces; choose contrasting label ink; distinguish panel identity from colour. Recall coordinates and counted repetition locally. | Legal row/column bounds; one clear label per panel; no scrolling or overwritten instructions. All panels identifiable with colour removed. |
| **2 — Give a choice a signal** | Light and restore a known panel; add its brief tone; let the same explained routine operate on each of four supplied identifiers. | Introduce `BRIGHT` as state applied when repainting, a visible active marker as well as brightness, and routine inputs through shared variables. Create and compare four pitches. | Each cue restores its resting appearance and label; all four pitches/positions map correctly; repeated cues do not alter unrelated cells or loop variables. |
| **3 — Remember an order** | Keep the board but print a temporary diagnostic sequence such as `"314"`; inspect its length and individual characters; append a literal choice and inspect the result. | Concatenation, `LEN`, one-based indexing, text versus numeric values. Temporary diagnostic output is explained and removed when playback replaces it. | `"314"` has length 3, first item `"3"`, last item `"4"`; appending `"2"` preserves the prefix. Label intentional out-of-range experiments separately. |
| **4 — Play the stored order** | Traverse the fixed string and call the cue routine for each item; add an explicit resting interval between items. | `VAL` on known valid stored digits, iteration through data, one outer loop with a distinct rendering-loop variable, WATCH status. | Present `"314"`, `"22"` and `"1234"` exactly once in order; identical adjacent choices have two distinct activations. All labels survive playback. |
| **5 — Let the player repeat it** | Accept one valid fresh choice; echo it; compare successive choices against the fixed sequence and reach a correct/wrong result. | Capture input once, validate before conversion, wait for release, keep the response index separate from stored data, show YOUR TURN. Add a quit branch before conversion. | Correct sequence, wrong first/middle/last item, held and rapid repeated keys, irrelevant keys, empty readings and release at phase boundaries. No new choice may be silently consumed by an idle release loop. |
| **6 — Grow a new round** | Begin with one choice; after a correct whole round append one random identifier and replay the unchanged prefix. Add completed-round scoring and the finite challenge ending. | `RND`, `INT` and `STR$` combined only after the fixed game works. Initialisation versus within-game progression; completion versus attempted length. | Seeded tests and known sequences; failure first round scores 0; completing 3 then failing 4 scores 3; completing 16 scores 16 and does not append item 17. No counter or prefix resets between successful rounds. |
| **7 — Finish, replay and keep it** | Add readable start and result screens; offer another game or quit; refine the cues and instructions through playtesting; save, reopen and play. | Fresh state on replay, control hand-off, clear end messages, source/media organisation and proportionate credits. Keep graphics/audio refinements tied to observed readability. | Two complete games without restarting the emulator; valid exit from defined phases; controls and status visible with sound off; named tape load into a fresh process; independent reader follows instructions. |

The fixed-sequence game in group 5 is already playable. Groups 6–7 fulfil the finished Bright Spark scope rather than declaring that a small program only becomes a “real game” when decorated.

## State, routine and input contracts

Use a small state table before final source line numbering:

| State | Meaning and lifetime |
|---|---|
| `s$` | Current sequence, containing only `"1"`–`"4"`. Created for a new game, extended only after a completed round. |
| `i` | Current item during playback or checking. Reinitialised at the start of each traversal. Never changed by the cue renderer. |
| `p` | Numeric panel identifier 1–4 supplied to the cue routine. Caller validates before invoking it. |
| `k$` | One captured keyboard reading. Compared as text before conversion. |
| completed count | Fully repeated rounds. Reset for a new game; increment only after every item of a round matches. Final spelling can follow the source design. |
| rendering variables | Panel row, column, colour, pitch and a separate single-letter `FOR` variable. Shared state, documented as such; never silently reuse `i`. |

The cue routine must leave its panel resting, retain/repaint its label, and restore the text drawing attributes it promises to restore. A drawing routine takes an explicit active/resting state or has two explained entry behaviours; do not hide a general graphics engine behind a call.

Use **one captured reading per polling attempt**. Empty input loops back to capture; unrelated input is ignored and released; a valid choice is echoed once and then requires release before the next choice. A transition into YOUR TURN first drains any held playback/start key. A key held for two expected identical items must count only once.

Propose lower-case **q** as the ordinary quit key during input and readiness/result prompts, matching the marker experiment. During playback, check for q between cues and instruct the player to hold it until exit; a `BEEP` is allowed to finish before exit. Document and measure the resulting delay instead of promising instantaneous interruption. If a direction/number is held in a release loop, release it before q; Spectrum BREAK remains an emergency route, not the only normal exit.

The world does not advance while the player considers a response; there is no response deadline in the baseline. A pause menu and time pressure are optional future variations, not necessary infrastructure. A sequence-length challenge is sufficient.

## Graphics, audio and pacing

Use four fixed character-cell panels with one persistent digit each. Keep instructions and WATCH/YOUR TURN/result text in reserved rows. Label ink, panel background and active appearance must remain distinguishable: propose a visible marker or outline change alongside `BRIGHT`, so brightness or hue alone does not carry the event. Test the actual captured display in monochrome as well as colour before accepting the treatment.

The learner chooses and auditions four short notes with stable panel associations. Their exact pitches and durations remain implementation defaults to test, not a demand to reproduce a historical device's sound. Use a brief, distinct failure cue without a punitive prolonged buzz. Silence between cues creates separation, particularly for `"22"`. No backing music competes with the cue vocabulary.

Explain that changing an attribute selection is not the same as repainting existing cells. Explain that `BEEP` occupies the program while sounding, and `PAUSE` can be interrupted by a key. Early stages may expose that behaviour as an experiment. Before shipping playback, either provide a measured, explained wait that meets the key-interference tests, or explicitly define a permitted interruption behaviour that preserves readable cues. Do not quietly substitute a calibrated busy loop and call it an accurate timer. The [prototype](prototype.md) supports permitting the extra pause to shorten while retaining the complete note and repaint. This is the current implementation choice; revisit it if cue drawing, duration or target changes.

Create the panel design and sound vocabulary within the lessons: compare candidate contrasts, active indicators, intervals and durations. The assets are source text, character-cell arrangement and note data. No external image editor or supplied art pack is needed. The original artwork/code terms and any historical reference credits must be clear when sharing the game.

## Shared explanations and wider connections

| Destination | Useful connection | What stays local |
|---|---|---|
| [Meet BASIC: Put it somewhere](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-12-put-it-somewhere/) | Position as stored row/column values. | Exact panel coordinates, rectangular fills and reserved display rows. |
| [Meet BASIC: Write the repeated job once](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-11-write-the-repeated-job-once/) | Calls and distinct return points. | A cue routine's inputs, scratch variables and effects; no assumed centring helper. |
| [Meet BASIC: One press, one step](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-15-one-press-one-step/) | Capturing input and waiting for release. | Choice validation and hand-off between playback, input and replay. |
| [Foundations: Doing It Again](https://code198x.com/foundations/repeating/unit-01/) | Trace counted visits. | BASIC syntax, sequence length, one-based character positions and distinct loop variables. |
| [Foundations: Telling a Job What to Work On](https://code198x.com/foundations/structure/unit-03/) | Explain why a routine needs an input. | Its pseudocode uses local parameters and returned values; Sinclair `GO SUB` here uses shared variables and a return address. They are not equivalent scoping mechanisms. |
| [Foundations: Making a Choice](https://code198x.com/foundations/decisions/unit-01/) | Validating and comparing a response. | When validation occurs, what counts as an attempt and why no key must differ from a wrong choice. |
| Maths for Games and The Craft | Range derivation, accumulating work, readable feedback, anticipation and challenge. | Their current indexes/plans do not supply complete lessons for all these topics. Develop the necessary explanation here and link to authored shared units only when useful ones exist. |

Do not create another top-level data-structures module as a dependency. This game provides a concrete ordered-sequence example for later shared treatment. Candidate Pattern Library work is a **bounded digit-string sequence** with its one-character limitation and a **fresh-choice input routine** with its blocking limitation. The existing [cross-platform edge-detection pattern](https://code198x.com/patterns/cross-platform/input/edge-detection/) compares current and previous input bitmasks. That is a related alternative to blocking release waits, not the same implementation; preserve the distinction before extracting another pattern.

A future Vault entry on Simon would help contextualise the mechanic. No dedicated Simon game entry was located in the inspected Vault tree; a Ralph Baer entry exists. Check primary historical evidence and collaborative attribution before using that entry or adding origin claims. The lesson does not need a historical anecdote to proceed.

Useful system contrasts remain optional: another BASIC may use different substring syntax, a different index convention or another sound interface. Teach the shared operation before comparing its particular spelling. Source-check a specific machine before adding a concrete comparison. The move to **Touchdown** is a direct design contrast: gravity/fuel updates must continue while the player decides, so this game's blocking input and cue routines cannot be copied unchanged.

## Sources and available execution route

Technical passages inspected: Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (Sinclair Research, 1983): chapter 4, counted loops; chapter 5, subroutines; chapter 8, p. 51, string subscripting and slicing; chapter 9, string/numeric functions; chapter 11, pp. 73–75, random selection; chapter 15, positioned printing; chapter 16, colour/brightness; chapter 18, pp. 129–131, input and interruptible pauses; chapter 19, beeper output; appendix C, `LEN`, `STR$`, `VAL`, `INKEY$` and `BRIGHT`.

These support language/hardware explanations, not the quality of the proposed game. In particular, one-based string access, concatenation and `VAL` expression evaluation are source-checked; the exact chosen layout, pacing and control response require execution.

The available baseline is released **Emu198x Spectrum v0.22.1**, Apple silicon, with the configured lawfully supplied 48K ROM and the MCP transport used for the completed Meet BASIC checks. ROM key entry, screen queries, frame stepping, screenshots, audio capture and named tape save/load have been exercised in that module. Native Host Keyboard uses left Option/Alt for SYMBOL SHIFT and Shift+left Option/Alt for extended mode. Read and verify each new keyword chord in implementation.

The learner can type and edit on the target and save a BASIC tape program. Modern host-edited `.bas` files are maintained alongside the lessons. If a converter is introduced, call the workflow **cross-development**, distinguish host text from tokenised tape output, and verify the exact converter command before making it a learner requirement. No converter, original-hardware run, other-model run or new Bright Spark execution is established by this specification. The assembler is not required to execute this BASIC game.

## Verification and publication

Develop the first two groups' sample checkpoints before drafting the full lesson prose. Use known panel choices to settle label retention, active visibility, cue/rest separation and routine contracts. Prototype consecutive identical cues and key interference early; they could change the recommended visual or wait implementation.

Maintain complete sources and a reproducible check for every stage. Test the player's actual entry and save path as well as any faster authoring setup. Record fixed seeds, test-only sequences, source/binary hashes and the exact emulator/model. Inspect moving/cycling states over time, listen to the captured cues, and distinguish native interaction from MCP observations. If a blocker is reproduced in Emu198x, isolate it and file an emulator issue rather than making a silent curriculum workaround.

Required completion cases:

- Every panel at rest/active/rest, with its label intact; all four notes; audible and visible separation for repeated identical items; labels/active identity with sound off and colour removed.
- Fixed `"314"`, `"22"`, `"1234"`; first/last index; append preserves the prefix; random choices remain within the supported representation. A finite sample does not prove fairness.
- Correct input, wrong first/middle/last choice, no input, irrelevant keys, held keys, release during polling, repeated same-key presses, and keys held across phase boundaries. Specify simultaneous-key behaviour based on the target; do not promise general chord recognition.
- Failure in round 1, failure after several completed rounds, success at the cap, and no out-of-range next item. Displayed score must match its definition.
- Replay resets sequence, score, traversal and input readiness. Quit in every documented phase; no invisible background progress while waiting for a reply. Test playback key interference and report observed wait/exit behaviour.
- No scrolling or damaged labels/status after sustained play. Save and load into a fresh process, then play, restart and exit. A source listing or screenshot alone does not establish this.

Use existing public URLs while the replacements are developed. Assign descriptive routes only after lesson boundaries are stable; map all six old URLs and incoming fragments before redirecting or retaining them. Keep their source files and images available until every consumer is accounted for. At release, update the game index, unit catalogue, track/module descriptions and onward route together. The existing six-page catalogue status describes existing material, not completion of this proposed replacement.

Record feedback on clarity, recognition and control feel, not a required player score. Adjust panel treatment, cue timing, cap or stage boundaries when observation warrants it. The immediate deliverable after agreeing this specification is a small verified board-and-cue prototype, not a bulk rewrite of all seven proposed lessons.
