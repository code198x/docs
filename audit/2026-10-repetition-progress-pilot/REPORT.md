# Repetition progress and exit pilot: evidence and limits

We continued umbrella #114, #115 and #124 with a sixteenth bounded pilot: Repeating overview and units 2–3. The earlier repetition pilot retains counted-loop/random-secret evidence. This follow-up supplies progress, test-position and intervention evidence; learner effectiveness remains unverified.

Website baseline: `114f3614f5f0f6be107e550aa64d26785afa07a2`; docs baseline: `fa2f02934d3f075a9afdb37d26c18422f1996d5a`. These include approved Decisions website #742 and docs #76. Shared UI remains at `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

## Findings and bounded changes

[#743](https://github.com/code198x/website/issues/743) distinguishes a reachable exit from guaranteed completion. Submitting seven can finish the guessing loop, but valid wrong answers can continue and ASK can wait for another submission. A reachable winning case does not require the player to supply it. The revised unit names valid numeric guesses, distinguishes waiting from busy non-progress, and presents its game-loop shape as one model rather than every game's required structure. The overview names local values/comparison knowledge and optional Decisions practice without requiring prior attendance. The earlier random-repeat/fixed-secret placement correction is preserved.

[#744](https://github.com/code198x/website/issues/744) exposes why changing a value is insufficient if a reset undoes it. Unit 3 states a non-negative whole starting count, one subtraction per completed pass and no other changes. Its trace shows tests at 3, 2, 1 and 0. The positive whole count decreases to zero under those rules. An inner reset instead puts lives back to three on each pass, leaving two at the next test. Under the stated deterministic rules with no outside change, that state repeats. This reasoning is separate from a finite observed run.

Three Question prompts ask about input-dependent completion, reset placement and zero-start pre/post-test behaviour. The zero-start post-test body shows zero and subtracts to minus one before testing; that is ordinary model arithmetic, not byte underflow. A saved-flag connection recalls that testing a stored answer differs from recomputing lives > 0. The specification asks authors to name progress or an external event and distinguish audit guards from natural exits. Existing outputs/diagram structure remain; the guessing caption states its normal completion/waiting scope. No shared component, layout, dependency or executable pseudocode runtime is added.

## Objectives and learner evidence

| Surface | Knowledge used | Selected evidence and limits |
| --- | --- | --- |
| Unit 2 | Valid numeric answers and comparison | Winning case reachable but input-dependent; wrong answers and waiting distinct; no fresh keyboard-input trial in this native run |
| Unit 3: progress | Whole values, subtraction and comparison | Four-row explanation plus selected native starting values; not every machine's representation |
| Unit 3: test position | Before/after body order | Zero-start boundary and positive starts 1–3; no claim that post-test spending suits a no-lives rule |
| Unit 3: reset | Assignment and repeated state | Inner-reset counterexample, bounded guard and explicit initialization boundary |

[LEARNER-TASKS.md](LEARNER-TASKS.md) separates prediction, tracing, explanation, diagnosis, modification and creating a repeated task with an exit policy. [ASSESSOR.md](ASSESSOR.md) keeps expected answers separate. All actual learner outcomes are **not observed**. We claim no unaided completion, timing, hint rate, retention, transfer or educational effectiveness.

## Native evidence and sources

[verify-progress.py](verify-progress.py) uses maintained ROM key entry at code-samples revision `163e74e18e9536fb555ef7319fa08bbc1836542b`, Emu198x Spectrum 0.32.5 and 48K ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. [native-progress.json](native-progress.json) retains all actual trace bytes, pass/final-value/completion records, screen rows and tool/driver/verifier/fixture/ROM hashes.

The first main native attempt passes nine audit-only BASIC runs:

- [Pre-test fixtures](pre-3.bas), starting at 0, 1, 2 and 3, finish naturally after 0, 1, 2 and 3 passes, with final value zero. The zero case requires the explicit Done 0,0 record and End/completion report; it is not counted because an empty read happened to pass.
- [Post-test fixtures](post-0.bas), with the same starts, finish after 1, 1, 2 and 3 passes. At zero, the body records zero, subtracts to -1 and then leaves. At positive starts, the recorded descending values agree with the independent expected ranges. These eight natural cases supply **13 actual trace bytes**.
- The [inner-reset fixture](reset-3.bas) records **four actual bytes [3,3,3,3]**, final lives two, and Guard 4,2. The explicit four-pass audit guard intervened; the original condition did not naturally end the loop. Together the nine cases supply **17 observed trace bytes**. Successful intervention is not relabelled as successful termination.

The separate [missing-update control](missing-3.bas) leaves lives unchanged. The [known-red report](known-red-native.json) records Guard 4,3 and four threes, then rejects them as natural progress. Its [verbatim traceback](known-red-native.log) reports `Expected natural progress differs` with the actual guarded result. Missing subtraction and inner reset can show the same body value but leave different values for the next test, so final state is observed as well as shown values.

Every fixture includes the same explicit four-pass guard. All natural cases finish before it; the counterexamples depend on it. Completion reports, pass bounds and length-checked target-written trace data are required. There are no host writes of expected result memory. The transport enters POKE with its actual ROM keyword key. These are Spectrum IF/GO TO implementations of the test positions, not native execution of teaching WHILE/REPEAT syntax. No keyboard waiting, numeric input parser, arbitrary starting range, target overflow, performance or original-hardware claim follows from this run.

Primary source: Sinclair Research, *ZX Spectrum BASIC Programming* (1982), [chapter 3](https://worldofspectrum.org/ZXBasicManual/zxmanchap3.html) for conditional execution/GO TO, [chapter 4](https://worldofspectrum.org/ZXBasicManual/zxmanchap4.html) for repeated work through counters and conditional jumps, and [chapter 24](https://worldofspectrum.org/ZXBasicManual/zxmanchap24.html) for POKE/PEEK. The earlier repetition and Basics reports retain their own random/input observations; we do not claim a fresh run of those programs here.

```sh
python3 verify-progress.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --output /path/to/output
# Add --missing-update for the deliberately failing guarded control.
```

## Browser, contrast and visual evidence

`scripts/verification/repetition-progress-pilot.mjs` runs Chrome 155.0.8059.40 at 1440 and 390. [Baseline](browser-baseline.json): six page/viewport cases pass existing output and populated flow-diagram checks. It uses the original checkout's pre-existing build. All three authored source files match the pilot baseline; [baseline-identities.json](baseline-identities.json) records source/built HTML hashes without claiming the entire original build was regenerated at that revision.

[Known-red browser control](known-red-browser.json) applies after assertions to those pages and fails with `Original universal-loop/attendance claim remains`. [After](browser-after.json): **six page/viewport cases, twelve keyboard behaviours and eight program-output blocks** pass. Independent expectations check the four-row progress table at both widths. Six new visible-prompt explanations, two existing random-repeat reveals and four optional-link/Back journeys pass by keyboard. Both existing flow diagrams remain populated and contain the correct tests; this verifies authored diagrams, not execution of pseudocode.

No main-content axe violations, document overflow or page errors were observed, including after revealing answers. Raw incomplete contrast records concern existing SVG text/background overlap and two mobile source lines within horizontal listing viewports. The independent [flow-text probe](verify-flow-contrast.mjs) measures **22 actual text/background pairs**, across both diagrams and widths, with minimum **5.2586:1**; see [flow-contrast.json](flow-contrast.json). It uses authored step fills or the page background beneath the transparent SVG. The independent [source probe](verify-scroll-contrast.mjs) measures both long ASK lines at both scroll endpoints: [four samples](scroll-contrast.json), all **16.8168:1**. These text-colour observations do not qualify every graphical stroke, dark theme, focus state, zoom level or general accessibility requirement.

The first flow probe failed with `Expected opaque RGB: rgba(0, 0, 0, 0)` because it did not resolve the transparent SVG background to the page beneath; see [failure note](contrast-initial-failure.txt). Its next run, concurrent with the final rebuild, wrote a [zero-sample report](flow-probe-empty.json) labelled passed. **That result is invalid and is not counted as evidence.** The [retained note](flow-probe-empty-note.txt) names the missing HTTP/populated-diagram guards. The corrected probe runs after build completion and requires successful responses, one populated diagram on each page and four non-empty page/viewport rows before evaluating colours. The [first source probe](scroll-initial-failure.txt), also concurrent with the rebuild, failed its positive line-count/scroll guard; no measured pass follows from it. Both final probes pass on the completed build. These are verifier/coordination defects, not measured low-contrast findings or product passes.

All six after captures were inspected in one wide/narrow batch. One wording correction fixes an overview editing error, bounds the game-description wording and removes two prose suggestions; affected pages were confirmed after rebuilding. No layout repair was needed. Captures are in [screenshots](screenshots/). The [design detector](design-detector.json) returns no findings.

`npm run check` passes 31 test files: **218 tests passed**, nine existing skips. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). The final build produced 2,457 public pages, checked all 2,457 shared frames across 38 rendering families and indexed 2,459 pages; see [build.log](build.log). Existing build notices remain outside this pilot. Vale, Ruff and diff checks pass. All **40 verification modules** pass syntax checks and parse with zero automatic semicolon insertions; see [semicolon-check.txt](semicolon-check.txt). [SHA256SUMS](SHA256SUMS) covers retained evidence and this report.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2014 --ignore-lock
node scripts/verification/repetition-progress-pilot.mjs http://127.0.0.1:2014 /path/to/output after
# Copy retained probes into website root so their dependency resolves:
cp /path/to/docs/audit/2026-10-repetition-progress-pilot/verify-*-contrast.mjs ./
node verify-flow-contrast.mjs http://127.0.0.1:2014 /path/to/flow.json
node verify-scroll-contrast.mjs http://127.0.0.1:2014 /path/to/scroll.json
```

## Earlier approved publication and next bounded work

The merged Decisions lessons pass the [actual public-site audit](decisions-live.json): six page/viewport cases and ten keyboard behaviours. That supplements their earlier local evidence without establishing learner effectiveness.

The [coverage map](../2026-10-foundations-coverage.md) links this follow-up beside earlier repetition evidence. Next consolidate the umbrella acceptance criteria against the retained results, separating fresh technical gaps, specification choices and learner-dependent evidence before choosing another slice. All parent issues remain open. Keep the first-session pack available while learner trials wait.
