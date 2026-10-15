# Fractional representation: sixth bounded pilot

Working the Bits units 4–5 conflate finite precision with universal inexactness,
and fixed-point interpretation with discarding the fractional bits. The proposed
corrections distinguish exact representability, conversion, storage and display;
name the fixed-point width, scale and rounding choice; and qualify performance
and comparison advice by target and task.

[Website #708](https://github.com/code198x/website/issues/708) and
[#709](https://github.com/code198x/website/issues/709) track the bounded changes.
The separate [learner tasks](LEARNER-TASKS.md) and [assessor notes](ASSESSOR.md)
prepare a trial. No learner is available: educational effectiveness and unaided
transfer remain unverified. This snapshot is prepared for review, not published.
Umbrella #114/#115/#124 remain open.

## Scope and sources

The [plan](../../plans/2026-10-15-fractions-pilot.md) names exact files and limits.
Website baseline `5354b0abc4779f8b562726a903da8f9b6ee229c6`, docs baseline
`5ee7c9b50b4d4b53087928309b211e40eec23838`; samples
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. Isolated worktrees exclude unrelated
changes. Existing packages and the pinned UI kit were copied; no dependency was
added or installed. No whole-course arithmetic rewrite or benchmark is included.

Sinclair Research, *ZX Spectrum BASIC Programming*, chapter 24 pp.169–170,
describes the five-byte sign/exponent/significand encoding and the rounding of
one tenth. The Amstrad *ZX Spectrum +3 User Manual*, p.78, separates display
accuracy from stored precision and gives the large-number cancellation example;
p.219 describes numeric storage, and the system-variable table identifies VARS
at 23627. Fixed-point examples are exact rational derivations under explicitly
chosen width/scale rules, not claims about a universal machine format.

All-state website searches for floating-point, fixed-point and fraction, umbrella
floating searches and docs decimal searches found no matching findings before
filing. No new hardware source acquisition was needed.

## Transfer and prerequisite map

| Surface | Local contract | Boundary |
| --- | --- | --- |
| Counting in Twos; Working the Bits unit 2 | Binary places, unsigned byte pairs and explicit zero-fill shifts | Supports unfamiliar notation; not mandatory attendance for a system track. |
| Working the Bits unit 4 | Finite binary floating-point has exact values and rounded values; display need not reveal storage | Exact representability differs from a particular decimal-input conversion. Comparison needs follow the task; software arithmetic cost is target/workload dependent. |
| Working the Bits unit 5 | Unsigned 16-bit storage at scale 256; same-scale addition, quantisation and range | 384 means 1.5; high-byte extraction gives only 1. A power-of-two scale is convenient, not compulsory. More complicated arithmetic may need rescaling/intermediate width. |
| Meet BASIC unit 7 | RND range and nonnegative INT conversion, explained in a table | Optional conceptual link. Reading the table does not require playing the earlier game. Full game execution retains its own preceding-lesson knowledge. |
| Native Z80 audit fixture | Two-byte addition, high-byte extraction and unsigned wrap/carry | Audit tooling, not a new public sample. It verifies named operations, not a full fixed-point game or performance claim. |

The learner pack covers prediction, explanation, modification, diagnosis and
creation. BASIC and assembly remain independent entry routes. The preceding
bits/shifts pair was merged and live-verified; its publication evidence is retained
in website #706/#704/#705 and docs #62 comments.

## Findings and an unresolved observation

The floating-point page's “only ever an approximation” contradicts its own exact
halves and quarters. Its “never compare exactly” and “every sum adds error” rules
also overreach. Scope the explanation to binary formats, retain exact values and
rounding, and make comparison/performance choices depend on their purpose.

For fixed-point, division as interpretation is not integer right shift. At scale
256, 384/256 is 1.5; extracting its high byte yields 1 and removes the half. The
new text also gives a rounding policy for a tenth, an explicit maximum, and a
scale-10 alternative. No new interpreter or shared UI was introduced.

The first native audit expected decimal literal 0.5 to store an exact half. That
expectation failed: [retained result](initial-storage-failure.json),
`AssertionError: Expected exactly representable binary fraction`. Raw bytes show
0.5 stored just below 1/2, while the expression 1/2 stores exactly 1/2. Both print
0.5. The decoder follows the documented encoding; the discrepancy is in observed
input-to-storage results, with its mechanism not established.

[Docs #63](https://github.com/code198x/docs/issues/63) preserves that question,
including the tenth's difference from the manual's rounded worked example.
The updated audit asserts exact storage for 1/2 and 3/4, inexact storage for 1/10,
and records decimal-literal conversions as observations without assuming correct
rounding. This narrows the claim; it does not relabel the first failure as a pass.
Independent execution with a matching ROM is still required before attributing
an emulator, ROM or conversion defect. No implementation fix was attempted.

## Results

| Check | Outcome | Evidence and limits |
| --- | --- | --- |
| Existing lesson wording | Failed conceptual review | [Live baseline](browser-baseline.json) records both claims at both widths. Correct half/quarter examples are retained. |
| Actual ROM outputs | Passed twelve output checks | [Native results](native-fractions.json): exact-looking sums/comparison, cancellation, full division versus INT, quantised decoding, and six prints of stored x. Complete output and normal completion checked. Printed equality alone is not a storage proof. |
| Actual stored fractions | Passed three expected properties; three further observations retained | Read VARS and verify record name; decode all five numeric bytes using rational arithmetic. 1/2 and 3/4 are exact, 1/10 is inexact. Decimal 0.5 is below half; decimal 0.75 is exact; decimal 0.1 is inexact. The conversion discrepancy remains open in #63. |
| Scaled integer execution | Passed one fixture with three checks | [Assembly fixture](scaled-add.asm), freshly assembled/tape-loaded: 384+128 produces 512 (decoded 2); high byte of 384 is 1, differing from full decoding 1.5; 65535+1 wraps to 0 with carry. Loaded code bytes must match the newly assembled binary. No result injection. |
| Fixed-point quantisation | Exact host calculations retained | Positive nearest-integer examples at scale 256: 1/10 → 26, 1/3 → 85, 3/2 → 384. Host Fraction calculations are separate from emulator observations. They do not benchmark runtime arithmetic. |
| Production build and repository checks | Passed | 2451 pages built and shared-frame checked; 2453 search pages indexed. 31 test files, 218 passed tests and nine existing skips. Link/content/prepared-tool checks passed. Pagefind retains its existing Default UI advisory. |
| Proposed page/viewport checks | Passed within scope | [After](browser-after.json): HTTP 200, no document overflow or scoped automated WCAG A/AA violations at 1440×900 and 390×900. Four closed predictions open by keyboard; optional BASIC link/table and Back pass at both widths. Narrow unit 4 has an incomplete colour-contrast check, not a contrast pass. |
| Known-red controls | Expected independent rejections | [Unit 4](known-red-unit-04.json) and [unit 5](known-red-unit-05.json): `Original fractional-representation claim remains in unit 04` / `05`. Neither original page passes the corrected-state verifier. |
| Prose/design/Python/evidence/patch checks | Passed | Changed lessons and trial sheets have no Vale errors/warnings/suggestions after revisions; design detector `[]`; Ruff, evidence hashes and whitespace checks pass. |
| Educational outcomes, original hardware, independent decimal-conversion reproduction, screen readers, physical devices, other browsers and timing | Pending or untested | Do not infer these from the passing scoped checks. |

Chrome 155.0.8059.40, Playwright 1.62.1 and axe 4.13.0 were used on macOS.
Native Emu198x Spectrum 0.32.5 and configured ROM/tool/driver hashes are recorded
in the native JSON. Desktop viewports are not physical mobile evidence. Both
revised pages at both widths were visually inspected. Established page composition
is preserved; no shared layout or public framework changes.

## Reproduce and next step

With the website's existing prepared tooling and assets:

```sh
node scripts/verification/fractions-pilot.mjs https://code198x.com /tmp/fractions-before baseline
npm run build
npm run check
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2002 --ignore-lock
```

In another terminal:

```sh
node scripts/verification/fractions-pilot.mjs http://127.0.0.1:2002 /tmp/fractions-after after
```

From docs, using configured native tools and the maintained keyboard driver:

```sh
python3 audit/2026-10-fractions-pilot/verify-fractions.py --samples ../code-samples --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x --output /tmp/fractions-native
```

[Evidence hashes](evidence-sha256.json) cover retained observations and captures.
The old-page controls become historical after publication. Review the bounded
corrections and packs; investigate #63 independently; run the learner trial when
someone is available. Broader learning-journey evidence remains unfinished.
