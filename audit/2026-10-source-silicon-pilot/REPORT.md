# From Source to Silicon pilot: evidence and limits

We continued umbrella #114, #115 and #124 with a thirteenth bounded pilot. We read the overview and all five units, repaired the toy translator's silent omission, and checked selected model, source/byte and browser claims. Learner effectiveness remains unverified.

Website baseline: `5569e9add8fea7d96840fac33068c1f10310f01e`; docs baseline: `cc99811729c1ec3551c18231b51c963928bdc1f1`. These include approved Gates/Adder website #734 and docs #73. Primary gate provenance #132 merged first at umbrella `0826858c7fedfa87accc4acf4c8b7a6aafea69f8`. Shared UI remains at `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

## Finding and bounded changes

[#735](https://github.com/code198x/website/issues/735) records a concrete failure: the original toy assembler prints each matching code during its scan. An unknown name has no matching branch and disappears, while later names still emit codes. The prose acknowledged the limitation but left a silently shortened program as the taught endpoint.

Unit 3 now buffers codes in `pending`, resets `found` for each source word, and keeps `valid` false after any unknown word. Only a fully valid translation emits program codes. Diagnostics remain visible, including a middle-name example whose recognised final word cannot repair the earlier failure. Empty input is a valid empty program, distinct from rejection. The fixed table contains each name once, and its two lists have corresponding positions; we do not claim validation of arbitrary replacement tables.

The overview names the local list/loop/IF knowledge and offers earlier modules as optional practice. It identifies the teaching notation as a paper trace rather than a program for a particular machine. Unit 1 distinguishes character codes for source letters from the invented instruction codes and adds a closed prediction. Unit 3 explains correcting source and translating again, including the risk of running an old output after a failed build. Units 2, 4 and 5 remain unchanged. No component, layout, dependency, interpreter or new language convention is introduced.

## Objective map and learner evidence

| Unit | Knowledge used | Evidence and limits |
| --- | --- | --- |
| 1: source and instructions | Values, operation order, code/data roles | Invented codes and source letters distinguished; separate real Z80 bytes below |
| 2: interpretation | A repeated update, stored program | Two actual ROM BASIC runs and stored token records; not an instruction-fetch trace of the whole interpreter |
| 3: translation | One-based lists, loops, IF and flags | Finite host model, emitted codes and rejection paths; not native execution of pseudocode |
| 4: responsibilities | Expected versus actual state, machine interfaces | Existing diagnosis question/link and keyboard reveal; no new cross-machine port |
| 5: measurement | Mean, deadline, named workload and clock | Independent arithmetic on the four explicitly invented observations; no new timing benchmark |

[LEARNER-TASKS.md](LEARNER-TASKS.md) separates prediction, explanation, tracing, error diagnosis, modification and creating/checking a short program. [ASSESSOR.md](ASSESSOR.md) retains answers separately. All actual learner outcomes are **not observed**. No unaided completion, hint rate, timing, retention, transfer or educational effectiveness is claimed.

## Model and native evidence

[verify-translation.py](verify-translation.py) has two distinct parts. Its host model mirrors the authored lookup/buffer/flag steps; the pseudocode itself is not an implemented language. All **121 valid programs of length 0–4** over INC/DOUBLE/SHOW match an independent encoding table. Executing their emitted codes agrees with a separate direct-name execution for final value and shown values. **144 invalid inputs** cover one unknown name inserted in every position of programs up to length three, repeated unknown names and a lower-case unknown. They emit no program codes and produce diagnostics. This is a finite set, not proof over arbitrary lengths, strings or table edits.

The [known-red model control](known-red-model.json) restores the old omission policy and fails with `Unknown name silently omitted or valid encoding differs`. The first rejected control has three DOUBLE names followed by MYSTERY: it emits three codes and no diagnostic. The empty case is positively included; a zero count is not accepted as coverage.

The native part uses the maintained ROM key-entry transport at code-samples revision `163e74e18e9536fb555ef7319fa08bbc1836542b`, Emu198x Spectrum 0.32.5 and ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. [native-translation.json](native-translation.json) retains tool, driver, verifier, ROM, source, binary and tape hashes, actual stored bytes and screen rows.

- ROM key entry stores three BASIC lines: initialise s, add ten, print s. We read the program bounds and line records, including actual LET tokens 241 and PRINT token 245. RUN prints **10** and leaves the stored program bytes unchanged.
- Replacing the addition with twenty changes the stored bytes. RUN prints **20** and again leaves those edited bytes unchanged. This observes selected data and results; a memory snapshot alone does not prove every internal execution step or measure interpreter overhead.
- The separate [Z80 fixture](source-byte-contrast.asm) starts at zero, increments twice, doubles and stores **4**, then writes completion marker 165. It assembles to **15 bytes** in a **136-byte auto-run tape**. Every byte must match an independent Z80 encoding sequence, load through ROM tape loading, and read back unchanged before the result is accepted. Its INC encoding is 0x3c, not our teaching machine's invented code 1. It stores the result rather than implementing a screen SHOW operation.

The first native verifier assumed the keyword token was the first byte of each stored BASIC line. The actual records include a leading space before the token. The [failed report](native-initial-failure.json) and [traceback](native-initial-failure.log) retain `Expected LET/LET/PRINT tokenised lines`. The corrected parser preserves raw bytes and skips leading spaces only for its keyword assertion. The subsequent complete run passes. No expected values were injected into the target's result memory.

Primary sources: Sinclair Research, *ZX Spectrum BASIC Programming* (1982), [chapter 14](https://worldofspectrum.org/ZXBasicManual/zxmanchap14.html) for keyword tokens, [chapter 24](https://worldofspectrum.org/ZXBasicManual/zxmanchap24.html) for stored line records and ROM/RAM, and [chapter 25](https://worldofspectrum.org/ZXBasicManual/zxmanchap25.html) for PROG/VARS system variables and byte order. Zilog's *Z80 CPU User Manual*, UM008011-0816, supplies the instruction encodings: [manual](https://map.grauw.nl/resources/cpu/z80.pdf). We do not infer physical timing, a compiler's output, every interpreter's design or original-hardware behaviour from these observations.

```sh
python3 verify-translation.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x \
  --output /path/to/output
# Add --old for the deliberately failing omission control.
```

## Browser, contrast and visual evidence

`scripts/verification/source-silicon-pilot.mjs` checks all six pages at 1440 and 390 in Chrome 155.0.8059.40. The [baseline](browser-baseline.json) uses pre-existing built pages from the original checkout. All six authored source files match this pilot's baseline revision; [baseline-identities.json](baseline-identities.json) records source and built HTML hashes. This is a retained built baseline, not a claim that the original checkout's entire build was regenerated at that revision.

Baseline: **12 page/viewport cases** pass existing output, table and selected trace checks. [Known-red browser control](known-red-browser.json) applies the after assertions to those pages and fails with `Original attendance prerequisite remains`. The separate model control above tests the actual silent omission. [After](browser-after.json): **12 page/viewport cases and 12 keyboard behaviours** pass: ten closed prediction reveals and two diagnosis-link/Back journeys. It checks expected output blocks, three-route and instruction tables, selected loop trace counts/endpoints, the buffer/validation steps and empty-program explanation. For unit 5, independent arithmetic confirms both means are ten milliseconds, A misses one 12ms deadline and B misses none among the four invented observations. It checks that the invented/exploratory/guest-time qualifications remain present. It does not execute or time the optional Meteor Storm experiments.

The [initial browser attempt](browser-initial-failure.json) failed before page assertions with axe's `Please use browser.newContext()`. The verifier now creates that explicit context. It is a verifier setup failure, not a product failure or pass.

No main-content axe violations, document overflow or page errors were observed, including after revealing answers. Four long source lines in unit 3 at 390 have incomplete colour-contrast results because their backgrounds are partially obscured in the horizontal listing viewport. Raw incomplete records remain. The independent [scroll probe](verify-scroll-contrast.mjs) measures those four text/background pairs at both left and right scroll positions: [eight samples](scroll-text-contrast.json), all **16.8168:1**. This addresses those rendered text colours, not every accessibility requirement or a blanket automated pass.

All twelve after screenshots were inspected in one wide/narrow batch. One wording correction names the pending-output list as well as the two lookup lists; the affected pages were confirmed after rebuilding. No layout repair was needed. Baseline and after captures are in [screenshots](screenshots/). The [design detector](design-detector.json) reports no findings; its first invocation used an unsupported format option, then the documented JSON flag was used. No design findings were suppressed.

`npm run check` passes 31 test files: **218 tests passed**, nine existing skips. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). The build produced 2,457 public pages, checked all 2,457 shared frames across 38 rendering families and indexed 2,459 pages; see [build.log](build.log). Existing build notices remain outside this pilot. Vale, Ruff and diff checks pass. All **37 verification modules** pass syntax checks and parse with zero automatic semicolon insertions; see [semicolon-check.txt](semicolon-check.txt). [SHA256SUMS](SHA256SUMS) covers retained evidence and this report.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2008 --ignore-lock
node scripts/verification/source-silicon-pilot.mjs http://127.0.0.1:2008 /path/to/output after
# Copy the retained contrast probe into the website root so its dependency resolves:
cp /path/to/docs/audit/2026-10-source-silicon-pilot/verify-scroll-contrast.mjs ./
node verify-scroll-contrast.mjs http://127.0.0.1:2008 /path/to/contrast.json
```

## Approved Gates and the Adder publication

The merged gate lessons pass the [actual public-site audit](gates-live.json): eight page/viewport cases, 52 circuit states and ten keyboard behaviours. The [first live attempt](gates-live-initial-timeout.json) timed out while following the Counting in Twos link; it is retained as a failed attempt. One complete retry passed. We did not establish the cause of that navigation timeout. The earlier gate report retains SVG contrast measurements and their limits; publication does not establish learner effectiveness.

## Next bounded work

The [coverage map](../2026-10-foundations-coverage.md) now links selected evidence across all ten Foundations modules. That does not complete their objectives or establish educational effectiveness. Return to the remaining Basics units 1–2/5: inspect ordering, output and input contracts, then choose a concrete input-boundary task and real target contrast. The parent issues remain open. Keep the first-session pack available while learner trials wait.
