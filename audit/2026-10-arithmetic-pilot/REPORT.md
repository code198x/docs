# Working It Out pilot: evidence and limits

We continued umbrella #114, #115 and #124 with a ninth bounded pilot. It covers the Working It Out overview and all three units. This report separates editorial findings, native observations, rendered checks and unobserved learner outcomes.

The approved Boolean pair was merged first: website [#722](https://github.com/code198x/website/pull/722) at `3c4e6f6c29d3b65ee92af8f8a34989c932fe939f` and docs [#68](https://github.com/code198x/docs/pull/68) at `df7c2e57ec9f9cd1bc43cac509d6fc3edf1cde32`. Those commits are this pilot's baselines. The website deployment [38741039411](https://github.com/code198x/website/actions/runs/38741039411) succeeded. A [live post-deployment check](boolean-live.json) passed eight page/viewport cases and eleven behaviour checks for the approved Boolean pages, including 76 independent table-output comparisons; its retained incomplete contrast check remains unknown. The installed shared UI remained pinned to `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

## Findings and bounded correction

[#723](https://github.com/code198x/website/issues/723) records conflicting rounding explanations and unstated numeric boundaries. Dropping the fractional digits of -3.5 gives -3; rounding down gives -4. The old positive examples were correct, but did not expose that distinction. The remainder paragraph also mixed up using a remainder to wrap a position and testing whether it is zero.

The revised third unit defines floor, shows the negative counterexample, limits introductory remainder to non-negative whole inputs and a positive whole divisor, and states the reconstruction relationship and bounds. It shows 31, 32 and 33 wrapping on a 32-column display, and notes that a multiple test includes zero. For non-negative halfway ROUND examples, it explicitly chooses the higher whole number. Negative halfway and negative remainder rules remain undefined here; target lessons must state their conventions before using them. Fractional pseudocode division is distinguished from target division and finite precision.

[#724](https://github.com/code198x/website/issues/724) records an ordering/transfer gap. The overview now recalls variables, input and output locally rather than requiring prior course attendance. Unit 1 shows equal-priority operations in left-to-right order, contrasts explicit brackets and treats a wrong-total diagnosis as a hypothesis to inspect. Its keyboard paragraph no longer presents one symbol convention as universal computing history. Unit 2 retains the correct score trace and adds a sequential-assignment prediction: assigning a=b followed by b=a loses the old a rather than swapping the values.

Each unit has one initially closed prediction question. Optional connections lead to the existing BASIC random-range operation table and an illustrative text-centring Pattern. Neither requires playing an earlier game or reading assembly. No new interpreter, dependency, component or layout was introduced. The pseudocode specification states the arithmetic conventions this lesson uses.

## Knowledge used and learner evidence

| Surface | Knowledge used | Local support and evidence boundary |
| --- | --- | --- |
| Overview and unit 1 | Ordinary numbers, variables and input | LET/ASK/SHOW recalled locally; actual rendered results checked. Input validation is acknowledged, not implemented as a new course. |
| Unit 2 | Reading a variable and adding/subtracting | Right-hand side explained; original trace checked by an independent step calculation. Swap task tests current versus old state. |
| Unit 3 | Number order and arithmetic | Floor contrasted with truncation; quotient/remainder invariant and explicit domains; target-language mapping remains separate. |
| BASIC connection | INT, scaling a random fraction | Read the existing operation table. A link journey is not a fresh game-execution claim. |
| Pattern connection | Half the unused width | Explain the odd spare column and overlong-text policy. The listing is explicitly illustrative; it was not assembled in this pilot. |

[LEARNER-TASKS.md](LEARNER-TASKS.md) includes prediction, explanation, modification, diagnosis and a small layout design. [ASSESSOR.md](ASSESSOR.md) keeps answers separate, including a three-value rotation as a transfer task. No learner was available. Completion, hint use, unaided transfer, retention and effectiveness are all **not observed**. Green technical checks do not establish those outcomes.

## Source and native checks

Primary reference: Sinclair Research, *ZX Spectrum BASIC Programming*, chapter 7, printed page 45, [Expressions](https://worldofspectrum.org/ZXBasicManual/zxmanchap7.html), and chapter 9, pages 59 and 61, [Functions](https://worldofspectrum.org/ZXBasicManual/zxmanchap9.html). Chapter 9 explicitly warns about negative INT and gives a nearest-integer calculation using INT. The report cites the original manual; the lessons define explanatory notation rather than claiming a universal language rule.

[verify-arithmetic.py](verify-arithmetic.py) uses the maintained Meet BASIC completion transport at code-samples revision `163e74e18e9536fb555ef7319fa08bbc1836542b`. It enters statements through ROM keys, observes the screen and checks normal completion. It does not inject expected results into memory. [native-arithmetic.json](native-arithmetic.json) records all rows, inputs, expectations, tool and driver hashes. Configuration: Emu198x Spectrum 0.32.5 and 48K ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`.

The final native run passed **42 numeric outputs**, **one zero-divisor error observation**, **12 assignment statements** and **12 reconstruction invariants**. It covers precedence/grouping, division, positive and negative INT, non-negative halfway calculation, repeated updates, a failed swap and a repaired swap. For twelve input/divisor pairs, independently computed quotient and remainder are compared with actual ROM results, then the actual pair must reconstruct the original and satisfy the remainder bound. Cases include zero, a group boundary, adjacent inputs and 31/32/33 wrapping.

The target uses INT expressions for floor and `n-d*INT(n/d)` for remainder. There is no claim that Sinclair BASIC has the pseudocode ROUND or REMAINDER keywords. The nearest calculation uses fractions constructed from integer division, not decimal literal conversion; the earlier [decimal investigation](../2026-10-decimal-investigation/REPORT.md) remains relevant. The actual `1/0` report was `6 Number too big` on this ROM.

The first run reached its arithmetic checks but failed while fingerprinting the ROM: a single 16,384-byte memory request did not return the complete ROM. The verifier now reads 256-byte chunks, asserts each length and asserts the total. [native-initial-failure.json](native-initial-failure.json), [native-initial-failure.txt](native-initial-failure.txt) and [failed-driver-sha256.txt](failed-driver-sha256.txt) retain the failed run and driver identity. It is not counted as a pass.

Reproduce from a family workspace with the native tool available:

```sh
python3 verify-arithmetic.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --output /path/to/output
```

## Browser, build and visual evidence

The website's `scripts/verification/arithmetic-pilot.mjs` checks the overview and three units at widths 1440 and 390 using Chrome 155.0.8059.40. Expected arithmetic is independently calculated; the authored output text is never used as its own oracle. The score trace is compared with a step-by-step state calculation. Explicit output counts prevent a missing example from passing unnoticed.

- [Published baseline](browser-baseline.json): eight page/viewport checks passed for existing worked outputs, trace, document overflow and main-content axe checks. The old boundary claim remains recorded. Technical correctness of the positive examples did not validate the general explanation.
- [Known-red control](known-red.json): the after assertions on the published baseline failed with `Original arithmetic boundary claim remains`, at the overview's old attendance requirement. This confirms that the after guard rejects the original module; it is not a learner result.
- [Proposed after](browser-after.json): eight page/viewport checks and ten behaviour checks passed. There were 22 checked output blocks across both widths, including the added grouping example, and two independently checked score traces. Six closed predictions opened by keyboard; four optional-link/Back journeys reached the expected context and returned. No main-content axe violations, document overflow or page errors were observed.

One narrow unit 3 colour-contrast check remains **incomplete** in axe. This is unknown, not a passing contrast result. Neither axe nor a keyboard journey proves screen-reader usability. All eight final [captures](screenshots/) were visually inspected together in one batched pass, covering desktop and narrow pages; no repair pass was needed. The scoped [design detector](design-detector.json) returned no findings. The baseline unit 3 captures retain the original explanation.

`npm run check` passed 31 test files: 218 tests passed and nine existing tests were skipped. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). `npm run build` produced 2,457 public pages, with shared-frame checks across all 2,457 in 38 rendering families, and Pagefind indexed 2,459 pages; see [build.log](build.log). Existing chunk-size and Pagefind notices were not changes in this pilot. Vale, Ruff and `git diff --check` passed.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2004 --ignore-lock
node scripts/verification/arithmetic-pilot.mjs http://127.0.0.1:2004 /path/to/output after
```

[SHA256SUMS](SHA256SUMS) covers the retained report and evidence. Native observations concern this ROM/configuration and selected cases; browser evidence concerns these routes and viewports. There is no cross-language, hardware, performance or learner-generalisation claim.

## Next bounded work

The [coverage map](../2026-10-foundations-coverage.md) now links this three-unit arithmetic sample. Next, inspect all four Structure units for list bounds, local names, parameter/result contracts and debugging traces before selecting corrections. Learner feedback can reorder that work. The published first-session pack remains available; expanding it and obtaining learner observations are separate from continuing the umbrella audit. The parent issues stay open.
