# Boolean logic pilot: evidence and limits

We continued umbrella issues [#114](https://github.com/stevehill1981/198x/issues/114), [#115](https://github.com/stevehill1981/198x/issues/115) and [#124](https://github.com/stevehill1981/198x/issues/124) with an eighth bounded pilot: the Truth Tables overview and three units. This is technical and editorial verification. No learner has completed these tasks, so educational effectiveness remains unverified.

The first-session guide pack is already published. Further guide expansion can wait for feedback; the umbrella audit continues without waiting for a learner. The [Foundations coverage map](../2026-10-foundations-coverage.md) records ten modules and 39 units, sampled evidence and remaining gaps. It is an inventory with evidence boundaries, not a claim that every unit has been audited. Working It Out is the next bounded slice: arithmetic, grouping, remainders and rounding. Maths for Games has a separate eleven-unit directory and is not covered by the number pilots.

## Findings and changes

- [#719](https://github.com/code198x/website/issues/719): adding an AND condition can leave the passing cases unchanged; adding an OR condition can do the same. The both-true row is the last row in the displayed order. Existing table output values were correct and remain unchanged.
- [#720](https://github.com/code198x/website/issues/720): truth tables enumerate Boolean input combinations. Actual game states may reach fewer combinations. Complementary names must describe the same current state. Equal Boolean results alone do not establish equal target-language values, evaluation effects or cost.
- [#721](https://github.com/code198x/website/issues/721): the narrow third unit had an overflowing table that keyboard users could not scroll. The shared table now accepts focus and shows a focus indicator. No layout rewrite was needed.

The lessons now recall their prerequisites locally, include closed prediction questions about repeated inputs, redundant conditions and stale state, and offer optional connections to Keep Guessing and the state-machine Pattern. The pseudocode specification includes the XOR operator already taught in the lessons and distinguishes Boolean equivalence from target execution properties.

[LEARNER-TASKS.md](LEARNER-TASKS.md) contains the prompts; [ASSESSOR.md](ASSESSOR.md) keeps expected answers separate. They cover tracing, prediction, diagnosis and a small independent guard design. All learner outcomes remain unobserved.

## Sources and native execution

The target-language reference is Sinclair Research, *ZX Spectrum BASIC Programming*, chapter 13, printed pages 85–86, [Conditions](https://worldofspectrum.org/ZXBasicManual/zxmanchap13.html). It defines numeric logical results and precedence. The native observations below support a distinction between Boolean truth values and the behaviour of one concrete language; they do not establish the behaviour of every language.

[verify-logic.py](verify-logic.py) uses the maintained Meet BASIC completion transport at code-samples revision `163e74e18e9536fb555ef7319fa08bbc1836542b`. It runs Emu198x Spectrum 0.32.5 with the 48K ROM fingerprint `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. [native-logic.json](native-logic.json) retains tool, driver, source, binary, tape and ROM hashes, observations and expected results.

- The actual ROM printed 34 checked numeric results: 28 Boolean-pair results covering AND, OR, inequality as Boolean XOR and both De Morgan identities, plus six numeric-value and grouping cases. Inequality is used for Boolean XOR; there is no claimed BASIC XOR keyword.
- Both `0 AND (1/0)` and `1 OR (1/0)` produced the observed ROM error `6 Number too big`. These two observations show that these expressions did not avoid the failing operand on this configuration.
- The assembled [Z80 fixture](boolean-rows.asm) was loaded through ROM tape loading. All 372 loaded bytes matched the assembled code. Its 493-byte tape and code hashes are recorded. Execution produced 28 Boolean output bytes and eight three-input jump-guard results, checked against independent Python Boolean calculations. Only input 110 passed the jump guard. The program wrote completion marker 165 at address 0xa100; the driver read the output rather than writing expected results into memory.

The first driver attempt failed because it entered `<>` as two character keys rather than the Spectrum inequality keyword chord. [native-entry-failure.txt](native-entry-failure.txt) and [failed-driver-sha256.txt](failed-driver-sha256.txt) preserve that failure. The corrected driver enters SYMBOL+W. The failed attempt is not counted as a pass.

From a family workspace with the native tools available:

```sh
python3 verify-logic.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x \
  --output /path/to/output
```

## Rendered and interaction evidence

Baseline website revision: `b1ddbdfc5f72e79e2a97bd6ed42ae8402e25c883`. Baseline docs revision: `b076c2c0bec0be046480975f130f3770668c5f8d`. The website's pinned shared UI revision was `7eda45e1c2f8b8f919359c971b2e210822e431f2`.

The website's `scripts/verification/boolean-logic-pilot.mjs` checks four routes at widths 1440 and 390 with Chrome 155.0.8059.40. It independently calculates rendered truth-table outputs, checks expected table and column counts, and checks keyboard interactions and axe results in the main content.

- [Baseline](browser-baseline.json): eight page checks, status **findings**. The narrow third unit had one `scrollable-region-focusable` violation. It is not reported as passing accessibility.
- [Known-red control](known-red.json): applying the after assertions to the old public lesson failed with `Original Boolean-scope claim remains`. The guard can reject the original content.
- [After](browser-after.json): eight page checks and eleven behaviour checks passed. All 76 rendered output cells matched the independent oracle across both widths. The behaviour checks cover six prediction disclosures, four optional-link journeys and actual horizontal keyboard scrolling with a visible focus indicator. No document overflow, axe violations or page errors were observed.
- [Other component consumers](table-consumers.json): five tables on two Gates and the Adder routes accepted focus and showed the indicator at width 390. This is a focused shared-component regression check, not a new audit of the Gates curriculum.

The initial baseline and proposed-page runs both failed on the inaccessible table; [baseline-initial-failure.json](baseline-initial-failure.json), [after-initial-failure.json](after-initial-failure.json) and [scroll-diagnostic.json](scroll-diagnostic.json) retain the finding. The target was the scrolling table itself. The final baseline records findings explicitly, while the after run requires zero violations.

One colour-contrast check on unit 2 at width 390 remains **incomplete** in axe. This is unknown, not a passing contrast result. Automated checks do not establish screen-reader usability or learner comprehension. All eight final captures in [screenshots/](screenshots/) were visually inspected in one batched pass; no further visual correction was needed. The design detector returned [no findings](design-detector.json).

From the website checkout after building and starting preview:

```sh
node scripts/verification/boolean-logic-pilot.mjs http://127.0.0.1:2003 /path/to/output after
```

## Verification and retention

`npm run check` passed 31 test files: 218 tests passed and nine existing tests were skipped. Content, Vault links, NES assembler and browser-player checks completed successfully; see [check-final.log](check-final.log). `npm run build` built 2,457 public pages; shared-frame verification covered all 2,457 across 38 rendering families, and Pagefind indexed 2,459 pages; see [build.log](build.log). Existing large-chunk and Pagefind notices remain outside this pilot.

Vale reported no findings on the changed lesson prose and pilot documents. Ruff passed the native verifier. `git diff --check` passed. [SHA256SUMS](SHA256SUMS) covers the retained evidence and report. The Foundations inventory records actual unit titles and headings from the baseline; counts were checked as ten modules and 39 units.

These results support the bounded corrections and technical checks above. They do not close the umbrella issues or establish beginner independence, retention or transfer. Those require the separate learner trial.
