# Decisions chains and saved-state pilot: evidence and limits

We continued umbrella [#114](https://github.com/stevehill1981/198x/issues/114), [#115](https://github.com/stevehill1981/198x/issues/115) and [#124](https://github.com/stevehill1981/198x/issues/124) with a fifteenth bounded pilot: Decisions overview and units 2–3. This adds first-match and saved/reset-state evidence beside the earlier choice and Boolean pilots. Learner effectiveness remains unverified.

Website baseline: `81033dc11717f5140f0e62420f6d2a3b4145d0cc`; docs baseline: `693034b18e60fd0cd5879d59997f74984d12cb92`. These include approved Basics website #739 and docs #75. Shared UI remains at `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

## Findings and bounded changes

[#740](https://github.com/code198x/website/issues/740) records a missing distinction rather than an incorrect existing output. The original low/high/equal guessing conditions are disjoint for an unchanged ordinary number. They do not expose what first-match order does when conditions overlap. Unit 2 now names its valid numeric input assumption and adds a whole-score 0–100 example with thresholds 50 and 80. A broad-first test captures high scores before their intended branch. Separate IF tests can take both paths. The table covers 49, 50, 79, 80 and 81, and explicitly shows continuation after END. A final ELSE is useful when the intended rule needs a fallback; omitting one can deliberately do nothing.

[#741](https://github.com/code198x/website/issues/741) records the saved-answer boundary. The original comparison example never changed its input afterwards. Unit 3 now stores guess < 7 at guess 4, changes guess to 9, and distinguishes the retained TRUE from a fresh FALSE. Its trace identifies a fourth row as a separate reassignment, not an automatic update. The game-over example identifies an intentional event latch, then shows why restoring lives alone does not reset it. A new game explicitly clears gameOver. Resetting on every update could erase an event before a later reader handles it. Flag visibility is bounded by where the name is available.

The overview still had the fixed-output/prior-attendance wording related to closed [#695](https://github.com/code198x/website/issues/695), whose earlier correction was confined to unit 1. We align this entry route with input-dependent output, local comparison knowledge and optional support. BASIC and assembly remain independent entry points. The pseudocode specification states that assigning a comparison stores its current value rather than a live expression. Existing correct outputs are preserved; three prompts use the existing Question component. No shared component, layout, dependency or executable pseudocode interpreter is added.

## Objectives and learner evidence

| Surface | Knowledge used | Selected evidence and limits |
| --- | --- | --- |
| Unit 2: chain | Comparisons, ordered instructions | First-match thresholds, boundaries, separate tests and common continuation; ordinary valid numbers, score example limited to whole 0–100 |
| Unit 3: saved answer | Assignment and TRUE/FALSE | Stored versus fresh comparison and explicit reassignment; no implicit reactive binding |
| Unit 3: event latch | Starting values and a later read | Event retained after lives change, then new-game reset; not a universal rule that every flag must clear each update |
| Overview support | Stored values and comparison meaning | Keyboard journeys to existing Basics/arithmetic pages; earlier attendance optional |

[LEARNER-TASKS.md](LEARNER-TASKS.md) separates prediction, tracing, explanation, a distinguishing counterexample, modification and creating a flag with a reset boundary. [ASSESSOR.md](ASSESSOR.md) retains expected answers separately. All actual learner outcomes are **not observed**. No unaided completion, timing, hints, retention, transfer or educational effectiveness is claimed.

## Native evidence and sources

[verify-state.py](verify-state.py) uses maintained ROM key entry at code-samples revision `163e74e18e9536fb555ef7319fa08bbc1836542b`, Emu198x Spectrum 0.32.5 and 48K ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. [native-state.json](native-state.json) retains actual result bytes and screen rows, tool/driver/verifier/ROM hashes and all five BASIC fixture hashes.

The first main native attempt passes five audit-only fixture runs:

- [Ordered dispatch](ordered.bas) and [broad-first dispatch](broad-first.bas) each process every integer score 0–100 through ROM BASIC. Their target-executed POKE writes one computed branch code per score; the host reads **101 actual bytes per policy**. Ordered codes 1/2/3 agree with the independent intended bands. Broad-first gives code 2 to all high scores: **21 differences at 80–100**. The native >79 and >49 tests are equivalent to the lesson's >=80 and >=50 only in the stated integer domain.
- [Separate tests](separate.bas) writes a third 101-byte table. One matching body adds 1 and the other adds 2, so code 3 at 80–100 records both matching bodies, rather than choosing one branch. The three tables supply **303 actual dispatch bytes**. All branch paths reach the common target store; Done appears once after each audit loop, not once per score. The browser table separately checks the lesson's per-score Done output.
- [Saved comparison](snapshot.bas) prints `1,0` after saving true and changing the input, then `0` after reassignment. Spectrum comparison results are numeric 1/0; these observations are not a claim that every target represents teaching TRUE/FALSE that way.
- [Latch/reset](latch-reset.bas) restores three lives while retaining the event flag. It prints `1,0`, then Game over; an explicit reset prints `0`, followed by Done. The target uses its own IF semantics and numeric state.

The main audit treats the wrong policy as an observed counterexample, not as correct implementation of the intended bands. The separate [known-red native control](known-red-native.json) requires that broad-first program to meet the intended bands and fails at all 21 scores 80–100. Its [verbatim traceback](known-red-native.log) retains `Branch policy differs at scores: [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]`. This control uses actual ROM-computed bytes, not a fabricated failed report. Non-empty table lengths, completion reports and both state traces are required.

The transport enters POKE with its actual ROM keyword key and deletes obsolete numbered lines through the editor before the state fixtures. There are no host result-memory writes. Sinclair BASIC uses separate IF/GO TO statements for this dispatch; we are not claiming native execution of the pseudocode ELSE IF syntax, numeric input validation, arbitrary score domains, performance, other machines or physical hardware.

Primary source: Sinclair Research, *ZX Spectrum BASIC Programming* (1982), [chapter 3](https://worldofspectrum.org/ZXBasicManual/zxmanchap3.html), for conditional execution, comparison and GO TO; [chapter 7](https://worldofspectrum.org/ZXBasicManual/zxmanchap7.html), for evaluating expressions/variables; [chapter 13](https://worldofspectrum.org/ZXBasicManual/zxmanchap13.html), for numeric comparison results and IF truth. Native observations name their actual configuration and input domain.

```sh
python3 verify-state.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --output /path/to/output
# Add --wrong-only for the deliberately failing broad-first control.
```

## Browser, contrast and visual evidence

`scripts/verification/decisions-state-pilot.mjs` checks the overview and units 2–3 at widths 1440 and 390 in Chrome 155.0.8059.40. [Baseline](browser-baseline.json): six page/viewport cases pass the existing correct output checks. Its pre-existing built pages come from the original checkout. All three authored sources match the pilot baseline; [baseline-identities.json](baseline-identities.json) records source and built HTML hashes without claiming the entire original build was regenerated at that revision.

[Known-red browser control](known-red-browser.json) applies the after assertions to those pages and fails with `Original fixed-output/attendance claim remains`. [After](browser-after.json): **six page/viewport cases, ten keyboard behaviours and ten program-output blocks** pass. Independent expectations check five score-boundary rows and four saved-comparison trace rows at both widths. Six visible-prompt/closed-answer checks open the three explanations by keyboard, and four optional support-link/Back journeys reach existing values/arithmetic content. These browser checks inspect authored models and feedback; they do not execute the pseudocode.

No main-content axe violations, document overflow or page errors were observed, including after revealing answers. One existing long flag-setting line at mobile width retains an incomplete colour-contrast result because the listing viewport partly obscures its background. The [independent probe](verify-scroll-contrast.mjs) measures its rendered text against the inherited listing background at both horizontal scroll endpoints: [two samples](scroll-contrast.json), both **16.8168:1**. Raw incomplete results remain; this is not a general accessibility assessment.

All six after captures were inspected in one wide/narrow batch. One wording correction clarifies optional fallbacks, intentional retained flags and where the game jobs may occur; affected pages were confirmed after rebuilding. No layout repair was needed. Baseline and after captures are in [screenshots](screenshots/). The [design detector](design-detector.json) returns no findings.

`npm run check` passes 31 test files: **218 tests passed**, nine existing skips. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). The final build produced 2,457 public pages, checked all 2,457 shared frames across 38 rendering families and indexed 2,459 pages; see [build.log](build.log). Existing build notices remain outside this pilot. Vale, Ruff and diff checks pass. All **39 verification modules** pass syntax checks and parse with zero automatic semicolon insertions; see [semicolon-check.txt](semicolon-check.txt). [SHA256SUMS](SHA256SUMS) covers retained evidence and this report.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2012 --ignore-lock
node scripts/verification/decisions-state-pilot.mjs http://127.0.0.1:2012 /path/to/output after
# Copy the retained contrast probe into website root so its dependency resolves:
cp /path/to/docs/audit/2026-10-decisions-state-pilot/verify-scroll-contrast.mjs ./
node verify-scroll-contrast.mjs http://127.0.0.1:2012 /path/to/contrast.json
```

## Earlier approved publication and next bounded work

The merged Basics lessons pass the [actual public-site audit](basics-live.json): eight page/viewport cases and ten keyboard behaviours. That supplements its earlier local evidence without establishing learner effectiveness.

The [coverage map](../2026-10-foundations-coverage.md) now links this Decisions follow-up beside the earlier choice and Boolean pilots. Next revisit Repeating units 2–3 for pre/post-test assumptions, termination and state-update/reset order. Choose a bounded case where a plausible wrong update produces a distinguishable trace. The parent issues remain open; keep the first-session pack available while learner trials wait.
