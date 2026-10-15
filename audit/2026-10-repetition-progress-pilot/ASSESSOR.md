# Assessor notes: progress and exits

All actual learner outcomes remain **not observed**. These are expected answers,
not learner results.

1. Both answers are wrong; another ASK follows and may wait. A later 7 gives
   normal completion. Reachability does not require that the player submits it.
2. Tests see 3, 2, 1, 0. The first three run and subtract to 2, 1, 0; the last
   skips the body. A positive whole count decreases by one each completed pass
   with no reset or other change, so this stated model reaches zero.
3. Pre-test: zero passes, final 0. Post-test: one pass shows 0, subtracts to -1
   and then exits. This model uses ordinary integer arithmetic, not byte wrap.
4. First pass resets to 3 and leaves 2. Each later pass starts at 2, resets to 3
   and leaves 2. Under the same deterministic rules and no outside change, the
   state cycles. The general reasoning is separate from observing four passes.
5. Initialise outside. Missing subtraction shows 3 and leaves 3; inner reset
   shows 3 but leaves 2. Inspecting only the shown value would not distinguish
   them. Inspect the state used by the next test as well.
6. The guard intervened. Its successful stop is not natural termination under
   the original condition. Keep the guard result and natural-exit results apart.
7. Accept a consistent task whose domain and update/exit policy are stated.
   Test the explanation as well as the trace; changing a value alone is not
   sufficient if it moves away from the exit or another update undoes it.

Native evidence uses Spectrum IF/GO TO to implement the two test positions.
The four-pass cap is audit-only. It does not execute the teaching WHILE/REPEAT
syntax or establish every machine's counters, input behaviour or timing.
