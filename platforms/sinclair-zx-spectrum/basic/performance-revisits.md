# Revisiting games at BASIC's limits

**Status:** Basis agreed; deferred until the initial BASIC versions have been developed. Current work stays focused on those games and their teaching sequences. No performance ceiling, specific experiment, assembly port or replacement course sequence is agreed.

## The question to answer

For a named experience on a stock 48K PAL Spectrum, how much work can the program complete while keeping input, movement, drawing and sound acceptable? Define the desired behaviour and its timing budget before deciding that a language is insufficient. A larger or deeper game does not by itself require assembly.

The existing games provide known rules and accepted endpoints. Revisit one with an explicit new ambition, predict what will become expensive, measure it, and improve the BASIC representation or drawing first. If the remaining cost prevents the agreed experience, compare a small machine-code routine with the BASIC routine it replaces. Consider a complete assembly version when the shared timing and state contracts justify it. Neither outcome is required in advance.

These are investigations into choices under constraints. BASIC and assembly retain independent entry routes. A revisit may recall a familiar game, but must explain its rules and data locally for a reader arriving directly at assembly.

## Candidates and useful pressures

The baseline mechanisms below were inspected in maintained source. Extension ideas and suspected pressures are hypotheses, not measured limits.

| Game | Existing mechanism | How it could grow in BASIC | Useful pressure to investigate | When assembly would have a concrete purpose |
|---|---|---|---|---|
| Bright Spark | Stored sequence, panel redraws, sequential cue routine with `BEEP` and `PAUSE`, separate watch/reply phases | More sequence patterns, difficulty choices, alternate cue sets and richer round structure | Require more precise cue spacing, input during playback, or animation while sound runs; separate intentional cue duration from redraw and input gaps | A measured sound/input/drawing deadline needs work the revised BASIC schedule cannot provide. Merely lengthening the remembered sequence is a weak reason to change language. |
| Volley | One ball, one paddle, cell movement, changed-cell drawing and a small per-loop pause | Return rules, opponent behaviour or an additional ball, introduced separately | Faster updates, finer position changes and concurrent objects increase drawing and contact work; check input latency and collision correctness together | A particular renderer or update routine cannot meet the chosen cadence after BASIC changes. Whole-game assembly becomes interesting if several interdependent tasks need the same tight budget. |
| Touchdown | Scaled vertical position/velocity, direct lateral steps, terrain-height array, keyboard-row reads, HUD writes each update | More landing sites, fuel decisions, horizontal momentum or changed terrain data | Finer visible movement, more frequent simulation, scrolling or simultaneous effects; measure HUD and terrain work separately | The required simulation/render/input schedule exceeds the measured BASIC budget. Faster code alone does not fix a collision rule that skips intervening terrain. |
| Sonar | Player-paced probes, stored board and clues, a random hidden target | Larger boards, different clue rules, multiple targets or scenario design | Board redraw and more expensive deduction assistance; there is no automatic continuous-motion deadline | A specifically desired redraw or search response is too slow after representation/algorithm changes. Additional puzzle depth alone offers no evidence that assembly is needed. |
| Crates | Player-paced legal moves/pushes, changed tiles, three data-defined rooms | More rooms, undo history, new puzzles or a level editor | Larger views, animated transitions or an optional hint/solver search | A named drawing or search requirement misses its budget. Search strategy and representation need examination before porting the same expensive search to assembly. More room data is initially a storage/loading question. |
| Tail Chase | Twelve-slot circular body, separate occupancy grid, changed-cell drawing, random free-cell selection, minimum clock threshold | Longer rounds, different arenas or obstacles, varied food rules | Faster cadence, finer graphics, several snakes, or dense-board food placement; vary one feature at a time | A measured hot routine blocks the desired response after algorithm changes. The existing body update does not shift all segments, so body length alone is not evidence of a linear movement cost. Dense boards expose random-placement retries as a separate problem. |

Meet BASIC's short programs remain introductions rather than automatic port candidates. Their ideas can support these experiments without every introductory project acquiring an assembly sequel.

## First experiment: Volley

Start with the accepted single-ball version. Its limited state makes the cost of input, contact checks and drawing easier to isolate than a larger game's. First establish the current cadence with no input, held movement and scoring. Then vary the deliberate wait while preserving movement rules. This shows how much time is intentional pacing and how much is actual work; removing a wait is not itself proof of a good faster game.

Choose one visible ambition after inspecting that baseline: a specified faster cadence at the same cell resolution is the smallest comparison. Pixel movement is a separate experiment because it changes drawing and contact rules as well as workload. A second ball or opponent is another separate variable. Do not claim a maximum ball count from an unrepresentative empty court.

Tail Chase is a useful second investigation because its teaching route exposes shifted coordinates, circular storage and occupancy. Compare those actual checkpoints, then investigate the remaining work. Touchdown can follow with a clearer distinction between simulation rate, visible movement and input sampling. This ordering is a recommendation, not a new assembly lineup.

## Evidence protocol

1. **Fix the promise.** Specify machine/ROM, PAL configuration, arena, object count, graphics, sound, target update interval and acceptable input-to-visible-response delay. Select the latter two through a stated design requirement and play trial; do not invent a universal frame-rate threshold.
2. **Keep a baseline.** Record source and tape hashes, emulator build and settings. Load through the actual target workflow. Preserve the accepted game as a control and identify experimental variants explicitly.
3. **Measure boundaries that matter.** Observe input sampling, state commit, completed drawing and the next update separately. Use emulator cycle/frame observations where available, with any BASIC instrumentation and its overhead stated. Include normal movement, turns, contact, score/HUD changes, growth/food placement and sound as applicable. Capture distributions, slow cases and missed deadlines, not only a mean.
4. **Make comparisons fair.** Use matching starting states and documented input schedules or state-relative actions. Reuse random seeds where suitable; label all fixtures. Frame-timed input can produce different routes when the program's speed changes, so compare equivalent behaviour as well as throughput. Keep required output and rules constant for an implementation comparison.
5. **Improve BASIC for a reason.** Reduce unchanged drawing, avoid repeated searches, alter representation or precompute stable data only where the measured work supports it. Recheck playability and correctness: a faster loop can alter difficulty, input handling and simulation speed.
6. **Test a bounded assembly alternative.** Choose one routine and define inputs, outputs, memory ownership, preserved machine state and return behaviour. Include the cost of calling it and converting or sharing data. Explain the loader and BASIC integration. A machine-code island still needs a safe contract; it is not an unexplained binary dependency.
7. **Decide from the result.** Retain BASIC if it meets the promise. Retain a small helper if it resolves the bottleneck with a clear interface. Propose a full assembly revisit if the remaining coordination costs or desired capabilities make that worthwhile. Alternatively reduce scope deliberately. Report the trade-off without presenting a chosen ambition as an absolute language boundary.

Observe native keyboard and display response separately from emulated cycle timing. Original-hardware validation is a distinct evidence level. Tail Chase's current `timing_samples` observe movement commits during drawing, with growth at a different boundary; they are not a ready-made end-to-end latency benchmark. No current data establishes how far any of these games can be expanded before a deadline is missed.

## Source baseline and next output

Inspected sample endpoints are relative to `code-samples/sinclair-zx-spectrum/basic/`:

- `bright-spark/opening/unit-07/steps/step-02.bas`
- `volley/prototype/steps/step-08.bas`
- `touchdown/teaching/unit-11/steps/step-02.bas`
- `sonar/teaching/unit-08/steps/step-01.bas` (the saved-game lesson reuses this endpoint)
- `crates/teaching/unit-10/steps/step-01.bas` (the saved-game lesson reuses this endpoint)
- `tail-chase/prototype/tail-chase.bas`

When this thread is resumed, the first candidate deliverable is a bounded Volley measurement brief and reproducible baseline, followed by one controlled experiment. No benchmark result or machine-code implementation is claimed here. Verify hardware and ROM details against primary sources when writing the experiment; game-source inspection establishes what these programs do, not a universal statement about BASIC or the Spectrum.
