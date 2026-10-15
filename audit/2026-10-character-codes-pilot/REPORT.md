# Character codes pilot: technical checks passed; learner trial pending

The seventh bounded slice corrects Working the Bits unit 3, “A Letter Is a
Number”. It now names ASCII before using its codes, checks exactly one digit
before subtraction, and bounds case conversion to the 26 ASCII letter pairs.
The existing BASIC greeting and Vault PETSCII chart provide optional connections.
Neither prior attendance nor a new machine entry route is required.

No learner is available. This report establishes source, execution and browser
observations, not educational effectiveness. [LEARNER-TASKS](LEARNER-TASKS.md) and
[ASSESSOR](ASSESSOR.md) prepare a future uncoached trial. Umbrella issues
[114](https://github.com/stevehill1981/198x/issues/114),
[115](https://github.com/stevehill1981/198x/issues/115) and
[124](https://github.com/stevehill1981/198x/issues/124) remain open.

## Findings and bounded change

- [Website #714](https://github.com/code198x/website/issues/714): the old wording
  said applying OR 32 to a digit or punctuation changed it to something else.
  ASCII "7" (55) already has this bit set, so it stays unchanged. "@" (64)
  becomes a backtick (96). The mask neither validates letters nor toggles bits.
- [Website #715](https://github.com/code198x/website/issues/715): the digit example
  was correct but lacked a validity contract. CODE "A" minus CODE "0" gives 17;
  this does not make A a digit. Spectrum CODE "73" returns the first character's
  code, 55, rather than converting the whole number 73. Empty input also needs
  an explicit length check.

Only the public lesson and its bounded browser verifier change in the website.
No interpreter, shared layout, dependency or emulator changes are involved.
The lesson adds two initially closed predictions, separates setting from clearing
a bit and points to existing language/machine explanations.

## Source checks

The original manuals supply the facts:

- Sinclair Research, *ZX Spectrum BASIC Programming*, chapter 14, printed p. 91:
  CODE takes the first character (0 for an empty string); CHR$ goes from code to
  one-character string. Appendix A supplies the character table. Ordinary ASCII
  letters and digits do not make the entire Spectrum set ASCII.
- The same manual, chapter 9, p. 58: VAL evaluates a numeric expression.
  VAL "2*3" is 6. It is not a general digit-only parser.
- Commodore Business Machines, *Commodore 64 Programmer's Reference Guide*,
  Appendix B, pp. 376–378, screen display codes; Appendix C, pp. 379–381,
  ASC/CHR$ codes. The chart's upper-case A example uses PETSCII 65 for PRINT
  and screen code 1 for direct screen memory. The selected character set also
  matters. This is a source-checked reading connection; no C64 execution was
  attempted in this Spectrum slice.

Teaching notation's CODE/CHARACTER contract remains that of
`specifications/pseudocode.md`: name the encoding. A character, its encoded
number and the glyph drawn from it are different concepts.

## Native observations

[The retained JSON](native-characters.json) records twelve actual ROM PRINT
outputs through the maintained Spectrum keyboard driver, then thirteen boundary
cases in a freshly assembled and tape-loaded Z80 fixture. No BASIC injection or
memory writes were used. The fixture itself writes its result bytes.

| Observation | Result |
| --- | --- |
| CODE A / a / 7; CHR$ 66 | 65 / 97 / 55; B |
| CODE 7 minus CODE 0; CODE A minus CODE 0 | 7; 17 (invalid digit input) |
| CODE "73"; CODE empty; LEN "73" | 55; 0; 2 |
| VAL "73"; VAL "2*3" | 73; 6 |
| CHR$ (CODE "A" + 32) | a; an ASCII-letter example, not a general case converter |
| Z80 OR 32 and AND 223 | Actual bytes agree with the masks; nonselected bits survive OR |
| Guarded case conversions | Endpoints A/Z/a/z convert; immediate neighbours and digits stay unchanged |
| Guarded digit conversion | 0, 7, 9 convert; punctuation neighbours, letters and other inputs return explicit audit sentinel 255 |

Inputs to the fixture are codes 64,65,90,91,96,97,122,123,55,48,57,47,58.
Each has five observed outputs: raw OR, raw AND, guarded lower-case conversion,
guarded upper-case conversion and guarded digit value. Range comparisons and
subtraction use independent host expectations. This is representative boundary
coverage, not an exhaustive test of every byte or encoding. String length is
checked in the lesson/task contract; this byte-only assembly fixture cannot
validate a whole string's length.

The audit requires the loaded 827-byte binary to match the freshly assembled
binary and a completion marker before inspecting results. Reads check their
length and are chunked at 256 bytes. Tool, driver, ROM and fixture hashes are
retained. Emu198x reports version 0.32.5. The ROM SHA-256 is
`d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`.
No ROM is included. The prior decimal investigation remains a separate resolved
finding; nothing here assumes decimal literal entry is always exact.

Reproduce with installed tools and a lawfully configured Spectrum 48K ROM:

```sh
python3 audit/2026-10-character-codes-pilot/verify-characters.py \
  --samples ../code-samples --emulator /path/to/emu198x-spectrum \
  --assembler /path/to/asm198x --output /tmp/characters-native
```

The driver imports the maintained completion driver, which imports its opening
transport. The audit-only assembly is retained as `ascii-boundaries.asm`; the
script regenerates it. Binary/tape hashes are recorded without shipping outputs.

## Browser and repository evidence

Baseline: website `0a43c77f0a7493565d386bff43bac9e8e3694ef0`;
docs `7585b3bec20b89679b46f24e3893225f700b2cb1`. UI kit copy was pinned at
`7eda45e1c2f8b8f919359c971b2e210822e431f2`. Installed dependencies were copied;
none were added or upgraded.

The verifier ran Chrome 155.0.8059.40 at 1440×900 and 390×900. Public baseline
captures retain the old claim. The after-mode control against that unchanged
public page exited 1: **Error: Original character-mask claim remains**.
Its JSON is retained under `evidence/control`; this establishes a check that can
fail. The proposed production build passed with the old claim absent.

Both viewports returned HTTP 200, had no document overflow and no scoped-main
axe WCAG A/AA violations. Eight behaviour groups passed: two closed answers
opened with Enter and two optional links followed by keyboard with Back return
at each width. Destination checks locate the BASIC string explanation and the
PETSCII chart. These checks do not claim the full BASIC browser runner works.
No page errors were reported. Full-page captures of both widths were inspected
in one batched visual pass: content, code/output blocks, answers, links and footer
fit the incumbent layout. No visual correction was needed. Impeccable's bounded
source detector returned no findings. These are browser observations, not
physical-device, screen-reader or performance measurements.

Reproduce after building and starting the existing preview:

```sh
node scripts/verification/character-codes-pilot.mjs \
  http://127.0.0.1:2003 /tmp/characters-browser after
```

`npm run build` passed: 2,451 pages, shared frame verified on all 2,451 and 2,453
search pages indexed. `npm run check` passed: 31 test files, 218 tests passed,
9 existing skips; sample references, Vault links and NES assembler checks passed.
Ruff and Vale passed with no findings on the new driver and revised lesson.
`git diff --check` passed. Existing build notices include chunks over 500 kB and
Pagefind's recommendation for its newer component UI; no dependency change was
made. Mise also reported sandbox-denied tracking symlinks under the user's state
folder; the actual checks/build completed successfully.

## Acceptance still pending

Prediction, explanation, modification, diagnosis and creation tasks are ready.
Their outcomes, coaching required, navigation comprehension and independent
transfer are unobserved. Do not mark the parent issues complete, or generalise
this slice to other encodings or machines. Run the prepared tasks with a beginner
when one becomes available; file observed blockers routinely and revise from
that evidence.
