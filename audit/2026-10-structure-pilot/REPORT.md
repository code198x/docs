# Structure pilot: evidence and limits

We continued umbrella [#114](https://github.com/stevehill1981/198x/issues/114), [#115](https://github.com/stevehill1981/198x/issues/115) and [#124](https://github.com/stevehill1981/198x/issues/124) with a tenth bounded pilot. We read the Structure overview and all four units, preserved the useful routine/debugging material, and proposed corrections only to the overview and units 1 and 3.

The user-approved semicolon follow-up [#726](https://github.com/code198x/website/pull/726) was merged at website `98d6f00cb57a106ef04093e2155d0407a62a6186`; that is the website baseline. Docs baseline is `df7c2e57ec9f9cd1bc43cac509d6fc3edf1cde32`. The arithmetic pair, website [#725](https://github.com/code198x/website/pull/725) / docs [#69](https://github.com/code198x/docs/pull/69), remains a separate draft. Continuing Structure does not imply approval of that pair. Shared UI remained at `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

## Finding and correction

[#727](https://github.com/code198x/website/issues/727) records two related gaps. Unit 1 did not state the complete valid index range or show an empty list. Unit 3 explained local parameter names, but its unchanged parameter could not expose accidental changes to caller state. These are source-level gaps; no learner failure has been observed.

Unit 1 now names whole indices from 1 through the list length, including that an empty list has no valid index and its FOR EACH body does no work. A closed question contrasts a one-item list before and after APPEND. The introductory iteration keeps list size fixed rather than implying universal rules about mutation during traversal. Silence is treated as evidence to investigate, not a certain diagnosis of an empty list.

Unit 3 changes the local numeric parameter before returning it, then reads the caller's same-named variable and the separate result. Its closed question distinguishes changing a local copy from assigning the returned result to the caller. It makes no promise about real-language list sharing, memory layout or copying cost. The optional BASIC connection explains that ordinary GO SUB variables are shared and RETURN resumes execution without supplying an expression value.

The overview recalls the knowledge used and preserves independent BASIC/assembly entry. The existing unit 2 shared-job prediction and call trace, and unit 4 hypothesis/comparison/debugging traces, remain intact. No component, layout, dependency or interpreter was introduced. The pseudocode specification now states the list-bound and fixed-size introductory traversal conventions.

## Objectives, prerequisites and assessment

| Unit | Knowledge used and objective | Selected evidence |
| --- | --- | --- |
| 1: lists | Values, assignment and repeated work; indexing, replacement, append, empty traversal and nested-loop order | Rendered outputs, explicit boundary question, independent grid calculation and native fixed-array contrast |
| 2: named jobs | Sequential instructions; definition versus call, return point, shared change and contract | Existing call trace and both divider outputs checked; existing prediction opened by keyboard |
| 3: parameters/results | Variables and calls; local numeric copy, result versus printing and caller assignment | Original result preserved, added caller/result output checked, two keyboard predictions; actual shared GO SUB contrast |
| 4: debugging | Arithmetic and tracing a loop; repeatable symptom, falsifiable hypothesis, repair/regression | Existing comparison and running-total tables independently checked; prediction and debugger link exercised |

[LEARNER-TASKS.md](LEARNER-TASKS.md) covers prediction, explanation, modification, diagnosis and creating a small value-returning job. [ASSESSOR.md](ASSESSOR.md) keeps answers separate. A broken total task requires zero, one and several-item cases: a one-item success alone cannot distinguish replacement from accumulation. All learner outcomes are **not observed**. No pass rate, hint rate, completion time, retention or independent transfer has been measured.

## Primary sources and target observations

The target references are Sinclair Research, *ZX Spectrum BASIC Programming*, chapter 5, printed page 37, [Subroutines](https://worldofspectrum.org/ZXBasicManual/zxmanchap5.html), and chapter 12, page 79, [Arrays](https://worldofspectrum.org/ZXBasicManual/zxmanchap12.html). Chapter 5 explains saved return points; chapter 12 defines one-based fixed arrays and says DIM initialises elements to zero and deletes an existing same-named array. These explain one target implementation, not the semantics of every language.

[verify-structure.py](verify-structure.py) uses the maintained Meet BASIC completion transport at code-samples revision `163e74e18e9536fb555ef7319fa08bbc1836542b`. It enters statements through ROM keys, reads actual display rows, verifies completion and fingerprints the complete ROM in checked 256-byte chunks. It does not write expected answers into memory. [native-structure.json](native-structure.json) retains tool/driver/verifier hashes, inputs and observations.

Configuration: Emu198x Spectrum 0.32.5, 48K ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. The final run passed **12 numeric outputs**, **two array-bound error observations** and **12 entered statements**:

- Array entries 1–3 hold 10,20,30; replacing entry 2 leaves 10,99,30. Accessing index 0 and index 4 each reports `3 Subscript wrong`.
- Re-dimensioning that array to four entries produces four zeros. DIM is not the growable-list APPEND operation and does not preserve the previous values.
- Entered lines 100/110 double ordinary variable n and RETURN. GO SUB changes caller-visible n from 5 to 10 and from 3 to 6. This intentionally contrasts with the copied numeric parameter in our pseudocode; it is not a native execution of that pseudocode.

The first driver attempt incorrectly required a direct-command `0 OK` report after storing a numbered program line. The ROM instead displayed the stored line in edit mode. The corrected verifier positively checks the displayed stored line, then verifies its effect through actual GO SUB execution. [native-initial-failure.json](native-initial-failure.json), [native-initial-failure.txt](native-initial-failure.txt) and [failed-driver-sha256.txt](failed-driver-sha256.txt) retain the failed attempt and identity. It is not counted as a pass or described as an emulator defect.

```sh
python3 verify-structure.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --output /path/to/output
```

## Browser and build checks

The website's `scripts/verification/structure-pilot.mjs` visits all five routes at widths 1440 and 390 in Chrome 155.0.8059.40. It independently calculates list outputs, nested-loop order, double results and running totals, checks explicit output/table counts, and checks the call/return trace. This is an oracle for the authored explanation, not a new pseudocode interpreter.

- [Published baseline](browser-baseline.json): ten page/viewport cases passed the existing worked-output and trace assertions. Positive examples being correct does not close the boundary and copy-demonstration gaps.
- [Known-red control](known-red.json): after assertions reject the old overview with `Original attendance requirement remains`. The proposed after guard can fail on the original module.
- [After](browser-after.json): ten page/viewport checks and fourteen keyboard behaviours passed. It checked 22 output blocks across both widths, the call trace, debugging comparison rows and running-total rows. Ten closed predictions opened by keyboard and four optional-link/Back journeys reached the expected target context and returned to the expected Structure title.

No document overflow, page errors or main-content axe violations were observed, both before and after revealing answers. Narrow units 1, 2 and 4 retain **incomplete** automated colour-contrast checks; those are unknown, not passing contrast results. Neither automation nor keyboard use establishes screen-reader usability or learner comprehension.

All ten after captures were inspected in one batched visual pass. A duplicated introductory recall in unit 1's summary was shortened in one correction batch; the affected desktop/narrow pages were then confirmed. The final captures are retained in [screenshots/](screenshots/). The scoped [design detector](design-detector.json) returned no findings.

`npm run check` passed 31 test files: **218 tests passed**, nine existing tests skipped. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). The final build produced 2,457 public pages, checked the shared frame on all 2,457 across 38 rendering families and indexed 2,459 pages with Pagefind; see [build.log](build.log). Existing chunk-size/Pagefind notices remain outside this pilot.

All 33 JavaScript verification modules pass syntax parsing and have **zero automatic semicolon insertions**, including the new verifier. Vale passed the three edited public pages and pilot documents; unchanged units 2/4 retain three advisory prose suggestions. Ruff and `git diff --check` passed. [SHA256SUMS](SHA256SUMS) covers the retained report and evidence.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2005 --ignore-lock
node scripts/verification/structure-pilot.mjs http://127.0.0.1:2005 /path/to/output after
```

## Remaining work

The [coverage map](../2026-10-foundations-coverage.md) now links this selected Structure evidence. It does not establish real-language list aliasing, every target contract or learner understanding. Next inspect binary/hex conversion in Counting in Twos units 1–2, outside the earlier numbers pilot's principal units 3–4 scope. Learner availability does not pause that work. The first-session pack remains shareable; the parent issues remain open.
