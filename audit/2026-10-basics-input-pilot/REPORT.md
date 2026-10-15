# Basics sequence and input pilot: evidence and limits

We continued umbrella [#114](https://github.com/stevehill1981/198x/issues/114), [#115](https://github.com/stevehill1981/198x/issues/115) and [#124](https://github.com/stevehill1981/198x/issues/124) with a fourteenth bounded pilot: the Basics overview and units 1, 2 and 5. Earlier stored-value work principally sampled units 3–4. Together they supply selected evidence, not complete educational validation.

Website baseline: `7c0fb762aef44edf6bcd8dec5f26aaa224ef4a74`; docs baseline: `984aa7306e4f01a0e21e70ab71b0711093829e5f`. These include approved Source/Silicon website #736 and docs #74. Shared UI remains at `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

## Findings and bounded changes

[#737](https://github.com/code198x/website/issues/737) records over-generalised sequence claims. Units 1–2 described top-to-bottom execution as all that running a program is, called one instruction the smallest program, and blurred displaying socks/shoes advice with physically doing it. The revised text bounds these first sequences, distinguishes output from the actions its words describe, and distinguishes valid-but-unintended instructions from errors a language can diagnose. Debugging begins with observations and the program without asserting that every failure is the learner's fault. Missing output calls for checking the running version, progress and screen history.

[#738](https://github.com/code198x/website/issues/738) records the input contract. The old greeting promised a different answer every time. The revised example submits one line of text with Enter, preserves spaces and accepts empty text. It waits before submission and uses the stored text afterwards. Repeating Ada repeats the greeting. Empty input and three spaces differ as stored values, even if their visible output looks alike. Digits are not converted to numbers and a sensible name is not validated. The pseudocode specification records this local contract and asks authors to state relevant input rules; it does not impose these text rules on every numeric ASK or target language.

Closed [#695](https://github.com/code198x/website/issues/695) repaired Decisions' fixed-sequence versus fixed-output account. This is a distinct Basics follow-up. We preserve the existing correct outputs and target links, add three prompts through the existing `Question` component as the unit specification requires, and keep BASIC/assembly independent entry points. No shared component, layout, dependency or executable pseudocode runtime is added.

## Objectives and learner evidence

| Surface | Knowledge used | Selected evidence and limits |
| --- | --- | --- |
| Unit 1 | Reading an instruction and its result | Hello output and displaying words versus performing their action; no claim to cover every execution model |
| Unit 2 | Order and comparison | Original/swapped output sequences and the unchanged third output; target BASIC line-number contrast |
| Unit 5 | Text, stored value, joining | Submission, waiting, repeated/empty/spaced/digit text; no numeric parsing or name validation |
| Optional target links | Locally explained PRINT/INPUT syntax | Keyboard journeys to existing complete lessons; fresh execution below is an audit-only contrast |

[LEARNER-TASKS.md](LEARNER-TASKS.md) separates prediction, tracing, explanation, diagnosis, modification and creating a small conversation with an input contract. [ASSESSOR.md](ASSESSOR.md) retains expected answers separately. All actual learner outcomes are **not observed**. No unaided completion, timing, hint rate, retention, transfer or educational effectiveness is claimed.

## Native evidence and sources

[verify-input.py](verify-input.py) uses maintained code-samples ROM key entry at revision `163e74e18e9536fb555ef7319fa08bbc1836542b`, Emu198x Spectrum 0.32.5 and 48K ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. [native-input.json](native-input.json) retains every actual screen row, string descriptor/byte observation and tool/driver/verifier/fixture/ROM hashes.

The first native attempt passes all ten runs:

- Two sequence runs show First/Second/Last and Second/First/Last. The first program deliberately enters line 20 before line 10; BASIC executes by line-number order. The last displayed output remains last after swapping the first two statements.
- One quoted/value contrast displays the literal n$ and then its stored text Ada. This uses Sinclair syntax, not a claim that pseudocode executes natively.
- Seven runs of the audit-only [greeting](greeting.bas) submit Ada twice, Sam, empty text, three spaces, padded Ada and digit text 42. Before Enter, both an initial wait and the typed-but-unsubmitted state have no greeting/Done output and retain the variable-area end marker instead of an assigned string. After Enter, both output lines and a successful completion report must appear.
- Actual string descriptor lengths and bytes equal the submitted text, including zero bytes for empty input, three space bytes and preserved leading/trailing spaces. Exact padded screen rows must agree with the reconstructed greeting; visual similarity alone is insufficient. Repeated Ada gives identical final rows. Reads are length-checked and the variable-area end marker must follow the actual string.

The native program uses Spectrum string INPUT with its supplied quotation marks and PRINT semicolons for immediate joining. It is not a universal raw-line input interface: deleting those supplied quotes can request expression evaluation. We did not test numeric INPUT, quotes inside answers, maximum lengths, non-ASCII text, other ROMs/platforms or physical hardware. No expected result values were written into target memory.

Primary source: Sinclair Research, *ZX Spectrum BASIC Programming* (1982), [chapter 2](https://worldofspectrum.org/ZXBasicManual/zxmanchap2.html), for stored line-number order, INPUT strings, supplied quotes and PRINT punctuation; [chapter 24](https://worldofspectrum.org/ZXBasicManual/zxmanchap24.html), for variable representations; [chapter 25](https://worldofspectrum.org/ZXBasicManual/zxmanchap25.html), for the VARS pointer. The target observations name a configuration and inputs, not every language's semantics.

```sh
python3 verify-input.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --output /path/to/output
```

## Browser, visual and contrast evidence

`scripts/verification/basics-input-pilot.mjs` checks the overview and units 1, 2 and 5 at 1440 and 390 in Chrome 155.0.8059.40. [Baseline](browser-baseline.json): eight page/viewport cases pass existing worked-output checks. Its pre-existing built pages come from the original checkout; all four authored sources match the pilot baseline. [baseline-identities.json](baseline-identities.json) records source and built HTML hashes without claiming the entire original build was regenerated at that revision.

The [known-red control](known-red-browser.json) applies after assertions to those old pages and fails with `Original sequence/input claim remains`. [After](browser-after.json): **eight page/viewport cases, ten keyboard behaviours and ten program-output blocks** pass. Six visible-prompt/closed-answer checks open the three Question explanations by keyboard, and four optional-link/Back journeys reach target PRINT/INPUT syntax. The verifier checks the unchanged outputs and named input-contract distinctions. The overview's separate greeting hero is visually inspected; it is not counted among the program-output component assertions.

No main-content axe violations, document overflow or page errors were observed, including after revealing answers. One long ASK source line at 390 retains an incomplete colour-contrast result: the listing's horizontal viewport partly obscures its background. The [independent probe](verify-scroll-contrast.mjs) reads that text's rendered colour against its inherited listing background at both horizontal scroll endpoints. [Both samples](scroll-contrast.json) measure **16.8168:1**. This addresses those text/background pairs, not every accessibility requirement. Raw automated incompletes remain in the browser JSON.

All eight after captures were inspected in one wide/narrow batch. One wording correction aligns the page descriptions and overview summary with the bounded claims; affected pages were confirmed after rebuilding. No layout repair was needed. Baseline/after captures are in [screenshots](screenshots/). The [design detector](design-detector.json) returns no findings.

`npm run check` passes 31 test files: **218 tests passed**, nine existing skips. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). The final build produced 2,457 public pages, checked all 2,457 shared frames across 38 rendering families and indexed 2,459 pages; see [build.log](build.log). Existing build notices remain outside this pilot. Vale, Ruff and diff checks pass. All **38 verification modules** pass syntax checks and parse with zero automatic semicolon insertions; see [semicolon-check.txt](semicolon-check.txt). [SHA256SUMS](SHA256SUMS) covers retained evidence and this report.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2010 --ignore-lock
node scripts/verification/basics-input-pilot.mjs http://127.0.0.1:2010 /path/to/output after
# Copy the retained contrast probe into website root so its dependency resolves:
cp /path/to/docs/audit/2026-10-basics-input-pilot/verify-scroll-contrast.mjs ./
node verify-scroll-contrast.mjs http://127.0.0.1:2010 /path/to/contrast.json
```

## Earlier approved publication and next bounded work

The merged Source/Silicon lessons pass the [actual public-site audit](source-silicon-live.json): twelve page/viewport cases and twelve keyboard behaviours. That supplements its earlier local evidence without establishing learner effectiveness.

The [coverage map](../2026-10-foundations-coverage.md) links this Basics follow-up alongside the earlier stored-value pilot. Next inspect Decisions units 2–3 for ordered condition chains and the lifetime of stored flags, then choose a plausible wrong rule that observed state can distinguish. The parent issues remain open. Keep the first-session pack available while learner trials wait.
