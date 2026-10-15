# Binary and hex pilot: evidence and limits

We continued umbrella [#114](https://github.com/stevehill1981/198x/issues/114), [#115](https://github.com/stevehill1981/198x/issues/115) and [#124](https://github.com/stevehill1981/198x/issues/124) with an eleventh bounded pilot: the Counting in Twos overview and units 1–2. The earlier numbers pilot principally sampled units 3–4; this adds conversion and interpretation evidence without claiming learner outcomes.

Website baseline: `3235b0352f9f8201b0d35826d134977c18b260bb`. Docs baseline: `3aed21029c553b3932bff6a1e7ccf44b2b06accc`. Shared UI remained at `7eda45e1c2f8b8f919359c971b2e210822e431f2`. The approved arithmetic/Structure publication completed in [deployment 38745470315](https://github.com/code198x/website/actions/runs/38745470315); separate live verification is retained below.

## Finding and bounded changes

[#729](https://github.com/code198x/website/issues/729) records the distinction between numeric notation, chosen storage width and interpretation. Unit 1's current/no-current account of a wire was too literal, and its unqualified byte maximum omitted the unsigned assumption. Leading zeros were mentioned, but not distinguished from reserving storage. Unit 2's existing conversions were correct; a short-pattern grouping example and a carry beyond FF make useful boundaries visible.

The revised overview names the arithmetic used without requiring earlier attendance. Unit 1 identifies a bit as information, labels the switch picture as a model, and uses the manual's voltage description for the concrete Spectrum example. It works decimal 45 back into binary place values, distinguishes 256 patterns from unsigned maximum 255, and adds a closed question about leading zeros and a nine-digit binary value. The opening/summary wording matches that bounded explanation.

Unit 2 groups a short pattern from the right after introducing A–F, distinguishes left-padding from right-padding, and shows full numeric results for 0F+1 and FF+1. Its closed question tests base and unsigned-byte fit separately. Optional links connect a byte to the existing pixel lesson and the later address-space explanation. The correct table, original F0 figure and earlier outputs remain unchanged. No component, layout, dependency or interpreter was introduced. The pseudocode specification states that BIN/HEX mark a base, not allocated storage.

Completed [#409](https://github.com/code198x/website/issues/409) improved hex entry and example clarity, and [#411](https://github.com/code198x/website/issues/411) supplied the F0 figure. This is a distinct boundary follow-up, not a repeat of those completed tasks. Related [#702](https://github.com/code198x/website/issues/702) addressed signed overflow in unit 4, which remains outside this edit.

## Objectives and learner evidence

| Surface | Knowledge used | Selected evidence and limits |
| --- | --- | --- |
| Unit 1 | Addition and doubling place values | Weighted conversion, leading zeros, unsigned width and pattern count; no measurement of circuits |
| Unit 2 | Four-bit grouping and place values | Six table rows, two nibble groups, full carry results and base markers; no promise of a target storage overflow policy |
| Pixel connection | One bit per pixel, locally explained syntax | Keyboard journey to existing complete program; this pilot does not claim a fresh run or edit of that game |
| Wider-value connection | Unsigned place value across two bytes | Keyboard journey and address-space context; earlier target evidence retains its own scope |

[LEARNER-TASKS.md](LEARNER-TASKS.md) separates prediction, explanation, conversion, diagnosis, modification and creating/checking a pattern. [ASSESSOR.md](ASSESSOR.md) retains expected answers separately. All actual learner outcomes are **not observed**. No completion time, hint rate, retention, unaided transfer or educational effectiveness is claimed.

## Source and native execution

Primary reference: Sinclair Research, *ZX Spectrum BASIC Programming*, appendix E, printed pages 217–219, [Binary and hexadecimal](https://worldofspectrum.org/ZXBasicManual/zxmanappe.html). It supplies the target's voltage explanation, grouping from the right and BIN notation. We retain a source-specific explanation rather than generalising the manual's simplified hardware account to every computer. The historical explanation for decimal counting is not needed to teach place value.

[verify-conversions.py](verify-conversions.py) uses the maintained Meet BASIC completion transport at code-samples revision `163e74e18e9536fb555ef7319fa08bbc1836542b`. Configuration: Emu198x Spectrum 0.32.5 with 48K ROM SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`. [native-conversions.json](native-conversions.json) records all inputs/results and tool, driver, verifier, fixture, code, tape and ROM hashes.

The native run passed on its first attempt:

- **Eleven actual ROM BIN outputs** include zero, one, padded/unpadded five, place boundaries, F0/FF values and the nine-digit binary value 256. Literal notation can name a value beyond one unsigned byte; it does not choose byte storage.
- The audit-only [Z80 fixture](byte-conversions.asm) was assembled to 45 bytes in a 166-byte auto-run tape, loaded through ROM tape loading, and read back byte-for-byte. Execution wrote completion marker 165 at 0xb100.
- For every unsigned byte value 0–255, the fixture emits eight individual binary digits and two nibble values: **256 rows and 2,560 observed output bytes**. Actual digit strings must match independent Python formatting, a weighted place-value sum and high×16+low reconstruction. Binary and hex decoding must agree. Reads are length-checked.

Hex text in the report is host formatting of the actual emitted nibble values. It is not machine-rendered ASCII, a Sinclair BASIC HEX keyword or a demonstration of every machine's representation. We make no signed, floating-point, electrical, timing or original-hardware claim. The target writes its own results; the driver does not inject expected values.

```sh
python3 verify-conversions.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x \
  --output /path/to/output
```

## Browser, visual and build evidence

`scripts/verification/binary-hex-pilot.mjs` checks the overview and both units at 1440 and 390 in Chrome 155.0.8059.40. It computes expectations independently, requires the expected output/table/diagram counts, checks six conversion rows and both nibble groups, and verifies the decimal-to-binary place row and reconstruction.

- [Baseline](browser-baseline.json): six page/viewport cases passed the existing output/table/figure checks. Correct worked examples did not settle the interpretation gap.
- [Known-red control](known-red.json): after assertions reject the original overview with `Original notation/physical-state claim remains`.
- [After](browser-after.json): six page/viewport cases and eight keyboard behaviours passed. It checked 14 output blocks, the six-row conversion table and F0 figure at both widths, plus the new weighted-place example. Four closed prediction checks and four optional-link/Back journeys passed.

No main-content axe violations, document overflow or page errors were observed, including after revealing answers. Axe's incomplete contrast results concern the figure's two downward arrow glyphs and say `Element content contains only non-text characters`. The arrows are in the aria-hidden diagram; its visible caption explains the same grouping. An independent [rendered-colour check](figure-contrast.json) measures both arrows at both widths as 16.8168:1 and checks the text equivalent. The raw automated incomplete status is retained; it is not a measured low-contrast result or a general accessibility pass.

The first browser verifier split rendered preformatted text on layout newlines and failed with `TypeError: Cannot read properties of null (reading 'map')`. It now reads the two source-line spans and asserts exactly eight places/bits. The next run reached the links but failed with `Destination context missing`: its assertion expected “installed”, while the target says “An address space is not a promise of that much RAM”. The assertion now checks that verified sentence. [browser-initial-failure.json](browser-initial-failure.json), [browser-link-failure.json](browser-link-failure.json) and the two failed-driver hash files retain both attempts. These were verifier defects, not lesson failures or passes. A separate inventory guard initially expected 34 modules; the actual baseline includes both the arithmetic and Structure additions, so the corrected positive count is 35.

All six final captures were inspected in one batched pass. One wording correction batch aligned the opening/summary with the bit model and removed the overview's “free” subtraction claim; affected pages were then confirmed. No layout correction was needed. The [design detector](design-detector.json) returned no findings.

`npm run check` passed 31 test files: **218 tests passed**, nine existing tests skipped. Content, Vault links, NES assembler and browser-player checks completed; see [check.log](check.log). The final build produced 2,457 public pages, checked all 2,457 shared frames across 38 rendering families and indexed 2,459 pages with Pagefind; see [build.log](build.log). Existing build notices remain outside this pilot. Vale reported no errors/warnings and one advisory suggestion in unchanged overview wording. Ruff and `git diff --check` pass. All 35 JavaScript verification modules pass syntax parsing with zero automatic semicolon insertions; see [semicolon-check.txt](semicolon-check.txt). [SHA256SUMS](SHA256SUMS) covers retained evidence and this report.

```sh
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2006 --ignore-lock
node scripts/verification/binary-hex-pilot.mjs http://127.0.0.1:2006 /path/to/output after
```

## Earlier approved publication

After deployment 38745470315 succeeded, the [actual public arithmetic pages](arithmetic-live.json) passed eight page/viewport cases and ten keyboard behaviours, and [Structure](structure-live.json) passed ten cases and fourteen behaviours. These retained live results supplement their earlier local evidence. Their original incomplete colour-contrast records remain visible; the separate Structure follow-up explains the scrolling-text measurements. Neither live sweep establishes learner effectiveness.

## Next bounded work

The [coverage map](../2026-10-foundations-coverage.md) now links selected evidence for both halves of Counting in Twos, without claiming complete learner validation. Next inspect all three Gates and the Adder units: distinguish the Boolean model from physical gates, check half/full-adder combinations and trace carry across more than one bit. Learner availability does not pause source and technical work. The parent issues remain open.
