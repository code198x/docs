# Output: text, values and explicit spaces

Basics unit 3's examples already produce the stated output. This slice adds two
independent predictions and a repair explanation, then distinguishes the shared
notation's joining comma from Sinclair BASIC's separators.
[Website #758](https://github.com/code198x/website/issues/758) tracks that bounded
explanation and transfer gap, not a broken calculation.

Eleven finite host models and **15 fresh Spectrum ROM PRINT contrasts** pass.
The proposed lesson preserves both original output panels and adds local recall
for independent entry. [Learner tasks](LEARNER-TASKS.md) and
[assessor notes](ASSESSOR.md) prepare an unaided trial. No learner is available:
effectiveness, retention and unaided transfer remain unknown. Umbrella
#114/#115/#124 remain open.

## Scope and source review

The [plan](../../plans/2026-10-16-output-joining-pilot.md) bounds this work.
Approved website #757 and docs #86 were merged before starting; the baselines
are `0bd828f0189006602076817acb1a13173f6ea172` and
`e5ea2c80cbc8c155aa46a06bcfcf5ea7b122c5ed` respectively.
[Identities](identities.json) retain source, specification, tooling and prior
report hashes. Existing installed packages, generated assets and the pinned UI
kit were reused in isolated checkouts. No dependency was added or installed.

[Curriculum design](../../specifications/curriculum.md),
[unit guidance](../../specifications/unit.md) and
[pseudocode](../../specifications/pseudocode.md) govern independent entry and
notation. The shared guide already states that SHOW's comma adds no space.
The current unit's quoted sum, evaluated sum and labelled result are correct.
Its explanation needed a way for the reader to predict a new case, repair a
missing space and avoid transferring punctuation unchanged to a target language.

The earlier [stored-value pilot](../2026-10-spectrum-learner-journey/stored-value-pilot/REPORT.md) and
[input pilot](../2026-10-basics-input-pilot/REPORT.md) supply related evidence;
the latter already checks submitted string spaces and PRINT joins. They remain
earlier evidence. This slice directly observes literal/arithmetic output,
missing/repaired spaces, print zones and continuation. All-state issue searches
for quotation, joining and separators found no matching unit-3 finding.
The [full objective map](../2026-10-foundations-objectives/MAP.md) retains its
immutable baseline; this report adds selected direct evidence.

Sinclair Research's *ZX Spectrum BASIC Programming* (1982),
[chapter 2](https://worldofspectrum.org/ZXBasicManual/zxmanchap2.html), pp. 17–18,
explains immediate semicolon joining, comma positions and how a final separator
suppresses the usual new line.
[Chapter 15](https://worldofspectrum.org/ZXBasicManual/zxmanchap15.html) gives the
PRINT controls and 32-column screen context. Those rules concern Spectrum BASIC;
they do not define our teaching notation or every BASIC dialect.

## Execution evidence

[verify-output.py](verify-output.py) compares structured literal/integer parts
with independently written expected strings. The [11 models](model-output.json)
cover quoted and unquoted sums, labels, absent/repaired spaces, leading and
final spaces, multiple pieces, adjacent digit text and empty text. The host model
is a finite check of the documented rule, not a pseudocode parser or a general
number formatter. A wrong join that inserts spaces automatically is rejected.

The [fresh native record](native-output.json) retains all 24 screen rows for each
keyboard-entered immediate PRINT command, using the maintained sample transport.
We require the complete expected output, blank remaining output rows and normal
ROM completion. No source/result memory injection or ROM patch is used. ROM
identity reads are length checked; the emulator closes and its exit is checked
on success and failure.

Eleven corresponding PRINT commands agree with the model. Four additional cases
observe comma zones for a labelled number and two letters, a final semicolon's
continuation into a second PRINT, and ordinary PRINT's new line. In the selected
comma cases the second item begins at zero-based column 16. This does not test
all cursor positions or wrapping.

The [space repair capture](repaired-space.png) displays `Score: 5`; the
[comma capture](comma-zone.png) shows the larger gap. Both were visually
inspected. A visible Z follows the significant final space in `" A "`:
` A Z` distinguishes a printed space from unused screen padding. Right padding
is stripped by the transport, so it cannot prove a final space on its own.

The [wrong-separator control](known-red/rejection.json) exits nonzero against
an immediate-join expectation. Its actual comma-zone output and failure remain
in [the rejected transcript](known-red/native-output.json). A green check must
therefore distinguish the intended rule from this plausible wrong transfer.

Two harness failures are retained separately. The
[first attempt](native-entry-failure.json) could not type a vertical-bar marker:
`ValueError: Unmapped character: '|'`. After switching to a supported Z, an
incomplete fixture edit left the expected marker unchanged; the
[second attempt](native-fixture-failure.json) failed with
`AssertionError('Complete ROM output differs: visible-boundary')`.
We corrected the fixture consistently before the successful full run. These are
failed harness attempts, not failed lesson examples or passing observations.

## Website and evidence checks

The final production build and all 237 tests in 32 files pass; see
[website results](website-results.json). The build retains an existing Pagefind
Classic UI deprecation notice; tool configuration also logs sandbox-denied mise
tracking links. Neither prevented these checks from completing.

The [browser record](browser.json) checks 1440×900 and 390×900: the original exact
output text, four keyboard answer reveals, and the optional story link and Back
at each width. Closed and revealed answers have zero scoped axe violations or
incomplete results. No document overflow or page errors were observed. Readable
wide/narrow answer captures were inspected. These are selected local production
checks, not whole-site access or live publication evidence.

The optional story explains its own semicolons, spaces, variables and input.
The new link points to “Give the words somewhere to go”; running that whole
program remains optional. The next Foundations unit introduces named values.
No prerequisite game, new variable lesson, parser, component or layout is added.

[Evidence validation](validation.json) checks baseline/proposed source hashes,
model/native correspondence, full transcripts, browser records and local links.
Wrong source hashes and missing native rows must fail. Run
[verify-evidence.py](verify-evidence.py) with `--website PATH_TO_WEBSITE_REPO`.
The [manifest](SHA256SUMS) retains the evidence file hashes.

Actual learner outcomes, physical devices, screen readers, arbitrary numeric
formatting, other dialects and original hardware remain untested. The prepared
prompts keep technical correctness separate from demonstrated understanding.

## Next bounded work

When a learner is available, observe the independent tasks. Meanwhile inspect
From Source to Silicon unit 2's interpreter trace: distinguish repeated source
operations from processor instructions, and test an independent prediction about
changed loop bounds. Start from the existing translation pilot and current
source; do not assume an incorrect example or make timing claims from one run.
