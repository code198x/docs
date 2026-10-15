# Gates and the Adder pilot: evidence and limits

We continued umbrella [#114](https://github.com/stevehill1981/198x/issues/114), [#115](https://github.com/stevehill1981/198x/issues/115) and [#124](https://github.com/stevehill1981/198x/issues/124) with a twelfth bounded pilot: the Gates and the Adder overview and all three units. This adds source, native arithmetic and browser evidence. Learner effectiveness remains unverified.

Website baseline: `95695874b13428e7e8da1c1e1b037a4bed8f1161`; docs baseline: `945fb47017e34d212979b37442a274ff2a99459e`. These include the approved binary/hex pilot. Shared UI remains at `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

## Findings and bounded changes

[#731](https://github.com/code198x/website/issues/731) records the distinction between a settled Boolean model and a physical gate. A truth table describes the model's Boolean outputs; it does not measure voltage, propagation delay or every behaviour of a physical chip. The revised overview and unit 1 name this boundary, explain local prerequisites and link the manufacturer's specification. A zero input is a defined model value, not a disconnected wire. Gate symbols are a convention, and a processor includes state and control as well as arithmetic.

[#732](https://github.com/code198x/website/issues/732) records the carry interpretation gap. Unit 2 reconstructs a half-adder result as SUM + 2 × CARRY. Unit 3 states the ordinary zero carry-in assumption, reconstructs all three input bits, and traces 111 + 001 through three columns. Keeping the last carry gives 1000 (eight); keeping only the three sum bits gives 000. A wrong carry can stop propagating when both next inputs are zero. Forty logical gate instances counts our eight copies of the five-gate construction; it does not establish a minimum, a CPU layout or a transistor count. Related closed #702 concerns signed overflow in Counting in Twos unit 4, not this gap.

The keyboard audit reproduced [#733](https://github.com/code198x/website/issues/733): every linked truth table lacked its initial zero-input highlight. The circuit dispatches its first event before the table's listener exists. Later toggles synchronise correctly. `TruthTable.astro` now renders row zero for a linked table unless an explicit highlight was supplied. All five current linked tables are in these units. Non-linked tables retain no automatic highlight; explicit overrides remain in the code, but no current call site supplies one, so this pilot claims no rendered override fixture.

All three lessons add a closed prediction. Optional links lead to the existing carry/signed-overflow distinction and the Spectrum assembly border lesson. BASIC and assembly remain independent entry points. The ripple overview stays a static connection diagram; the full-adder controls above it are interactive. No new dependency, interpreter, layout or pseudocode rule is needed.

## Objectives and learner evidence

| Surface | Knowledge used | Selected evidence and limits |
| --- | --- | --- |
| Unit 1 | Defined 0/1 inputs | AND/OR/XOR/NOT cases and Boolean versus measured behaviour; no physical specimen |
| Unit 2 | Addition and binary place value | All four half-adder cases; reconstruct both output bits |
| Unit 3 | Incoming carry and place value | All eight full-adder cases, a three-column trace and retained/discarded carry |
| Optional system links | Locally explained arithmetic and instructions | Keyboard navigation to existing target lessons; no fresh run of their programs |

[LEARNER-TASKS.md](LEARNER-TASKS.md) separates prediction, explanation, tracing, fault diagnosis, modification and creating a two-bit tool with an explicit carry policy. [ASSESSOR.md](ASSESSOR.md) retains answers separately. All actual learner outcomes are **not observed**. We claim no unaided completion, timing, retention, transfer or educational effectiveness.

## Primary sources and native execution

Texas Instruments, *SNx4HC08 Quadruple 2-Input AND Gates*, SCLS081J, originally issued December 1982, revised February 2025: [manufacturer data sheet](https://www.ti.com/lit/ds/symlink/sn74hc08.pdf). We visually checked printed page 4 (recommended operating conditions), page 6 (switching characteristics), and page 10 (AND function table). This is a modern manufacturer revision of a period family, not an unchanged period document. [Source PR #132](https://github.com/stevehill1981/198x/pull/132) retains the source note and PDF URL, revision, byte count and SHA-256 before the derived curriculum claims.

The existing Zilog *Z80 CPU User Manual*, UM008011-0816, supplies the architecture, register/control/ALU account and ADD/ADC instruction descriptions: [manual](https://map.grauw.nl/resources/cpu/z80.pdf). Observed arithmetic is not evidence that this CPU implements our particular five-gate full adder.

[verify-adders.py](verify-adders.py) uses the maintained code-samples transport at revision `163e74e18e9536fb555ef7319fa08bbc1836542b`, Emu198x Spectrum 0.32.5 and 48K ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. [native-adders.json](native-adders.json) retains tool, driver, verifier, fixture, code, tape and ROM hashes plus every case and ripple trace.

The native run passed on its first attempt:

- Four half-adder and eight full-adder cases agree with independent Boolean expressions and whole-number addition.
- All 64 pairs of three-bit unsigned values agree with an independent Boolean ripple model and full-result reconstruction.
- Four byte cases exercise ADD/ADC and the actual processor carry. For widths one and three, the extra bit is extracted from the numeric sum; it is not claimed to be the CPU's eight-bit carry flag.
- The audit-only [fixture](adder-cases.asm) assembled to 1,548 bytes in a 1,669-byte auto-run tape. ROM tape loading read back every code byte correctly. Execution wrote completion marker 165 at 0xb100 and **160 actual result bytes for 80 cases**. Every low-result/carry pair reconstructs the full sum. Reads are length-checked; the target writes its own results.

No physical gate layout, electrical behaviour, propagation time, transistor count or original-hardware observation follows from these emulator results.

```sh
python3 verify-adders.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x \
  --output /path/to/output
```

## Browser, contrast and visual evidence

`scripts/verification/gates-adder-pilot.mjs` runs Chrome 155.0.8059.40 at widths 1440 and 390. Its Boolean/arithmetic oracles are independent of the authored output cells. It requires the expected table, circuit, input and output counts.

- [Baseline](browser-baseline.json): eight page/viewport cases and 52 circuit states completed, with **ten missing initial highlights** (five linked tables at both widths). Status is `findings`, not a clean pass.
- [Initial baseline failure](browser-initial-failure.json) and [initial proposed failure](browser-proposed-failure.json) both fail with `Highlighted input row differs`. They retain the discovery before the bounded shared-component fix. The final baseline records this known row-zero defect while still requiring correct later synchronisation and arithmetic.
- [Known-red control](known-red.json): after assertions reject the original overview with `Original gate-model claim remains`.
- [After](browser-after.json): eight page/viewport cases, **52 circuit states**, **120 truth-table output cells**, the worked three-row carry trace, six keyboard prediction reveals and four optional-link/Back journeys pass. All five linked tables show the initial row and follow keyboard changes. Unlinked tables do not gain a highlight. The ripple overview has no controls, and its two carry connections are present; this does not claim interactive execution of 64 ripple inputs.

No main-content axe violations, document overflow or page errors were observed, including after revealing answers. Raw incomplete colour-contrast records remain in the browser JSON. Axe reports short SVG text, overlapping elements and image-node limitations; those are not automated contrast passes.

The independent [SVG text probe](verify-svg-contrast.mjs) reads actual rendered text fills and their authored opaque circle, gate shape or inherited page backgrounds. [Measured results](svg-text-contrast.json) contain 296 samples across both widths, all three units, and initial/all-inputs-on states. The minimum settled text ratio is **5.9439:1**. This covers those text/background pairs, not every state, graphical boundary, focus indicator, hit area or a general accessibility assessment. The [initial probe failure](contrast-initial-failure.txt) sampled immediately after toggling while the circle fill was still in its 120ms transition; the corrected probe waits for active animations to finish. It does not claim that transitional colours were measured as passing.

All eight after captures were inspected together at wide and narrow widths. No layout repair was needed. The [design detector](design-detector.json) returned no findings. Baseline and after screenshots are retained in [screenshots](screenshots/).

`npm run check` passes **31 test files and 218 tests**, with nine existing skips. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). The final build produced 2,457 public pages, checked all 2,457 shared frames across 38 rendering families and indexed 2,459 pages; see [build.log](build.log). Existing build notices remain outside this pilot. Vale and Ruff pass. All 36 website verification modules parse with zero automatic semicolon insertions and pass syntax checks; see [semicolon-check.txt](semicolon-check.txt). `git diff --check` passes. [SHA256SUMS](SHA256SUMS) covers retained evidence and this report.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2007 --ignore-lock
node scripts/verification/gates-adder-pilot.mjs http://127.0.0.1:2007 /path/to/output after
# Run this retained probe where @playwright/test resolves from website dependencies:
node verify-svg-contrast.mjs http://127.0.0.1:2007 /path/to/svg-text-contrast.json
```

## Approved binary/hex publication

The approved binary/hex website #730 and docs #72 are merged. [CI/deployment run 38748737834](https://github.com/code198x/website/actions/runs/38748737834) completed successfully at website revision `95695874b13428e7e8da1c1e1b037a4bed8f1161`. The [actual public-site verification](binary-hex-live.json) passes all six page/viewport cases and eight keyboard behaviours. This verifies the published lesson content and interactions; the earlier report retains the contrast scope and learner limits.

## Next bounded work

The [coverage map](../2026-10-foundations-coverage.md) now links selected evidence for all three Gates and the Adder units, while physical measurement and learner trials remain unobserved. Next inspect all five From Source to Silicon units, identify one concrete source-to-bytes or execution claim, and choose the smallest native example that can test it. The umbrella issues remain open; learner availability does not pause source and technical work.
