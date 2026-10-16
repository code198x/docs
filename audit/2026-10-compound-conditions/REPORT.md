# Compound conditions: numeric domains and grouping

Decisions unit 4's two interval guards choose the correct messages. The gap is in
what they promise: the page did not state its numeric-input assumption, distinguish
an interval from whole-number validity, or show when `> 0` and `>= 1` differ.
The proposed correction preserves the examples and makes those boundaries visible.
[Website #754](https://github.com/code198x/website/issues/754) tracks the finding.

An exact-rational model and **115 actual Spectrum ROM numeric outputs** agree on
the selected cases. Two prediction/explanation blocks expose the fractional and
grouping boundaries. Separate [learner tasks](LEARNER-TASKS.md) and
[assessor notes](ASSESSOR.md) prepare independent prediction, explanation, repair,
modification and creation. No learner is available; educational effectiveness
remains unknown. Umbrella #114/#115/#124 stay open.

## Scope and sources

The [plan](../../plans/2026-10-16-compound-conditions-pilot.md) bounds this slice.
Website baseline is `e59270e838c288a014cd191ed5404dba769d69f4`, after approved
website #753 merged. Docs baseline is
`aa06e4f58267349801d6c4c2923f4a5b1b19c822`, after approved docs #84 merged.
The [identities](identities.json) retain source, specification, tool and verifier
hashes. Isolated worktrees preserved unrelated original-checkout changes. Existing
installed packages, UI kit and generated browser/sample/assembler assets were
reused; no dependency was added or installed.

The source review read the actual unit, current
[pseudocode contract](../../specifications/pseudocode.md),
[unit guidance](../../specifications/unit.md) and Meet BASIC's
[Keep guessing](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-06-keep-guessing/).
That machine lesson already separates range checks from its INT check, preserves
the supplied guess and distinguishes numeric values from input-expression parsing.
The new optional link points to that explanation; running the preceding game is
not required to finish the shared lesson.

Sinclair Research's *ZX Spectrum BASIC Programming*,
[chapter 13, Conditions](https://worldofspectrum.org/ZXBasicManual/zxmanchap13.html),
pp. 85–86, documents comparison results, numeric conditions and operation priority.
It also explains why a non-zero numeric OR operand can make the result true.
[Chapter 9, Functions](https://worldofspectrum.org/ZXBasicManual/zxmanchap9.html),
p. 59, explains INT's downward rounding. The first attempted chapter-9 URL with
a padded `09` was inaccessible through the web reader; the unpadded `9` page was
retrieved. These are the manual's target rules, not universal language semantics.

All-state compound/numeric-input/range searches found the earlier ordered-state
finding #740 and related Boolean work, not a matching unit-4 domain finding.
We retain the completed
[Boolean pilot](../2026-10-boolean-logic-pilot/REPORT.md) and
[saved-state pilot](../2026-10-decisions-state-pilot/REPORT.md) as supporting
scope-specific evidence rather than reopening their findings.

## Objective and prerequisite map

| Surface | Knowledge used or explained | Transfer boundary |
| --- | --- | --- |
| Decisions unit 4 | Numeric comparisons, Boolean AND/OR/NOT, complete operands and grouping | Ordinary numeric input is assumed; text conversion and malformed input are separate |
| Inclusive interval | Lower and upper bounds; both endpoints and interior fractions | Being in range does not establish a whole number |
| Grouped shooting rule | Current alive flag and ammo/grenade comparisons | Brackets keep alive necessary for either resource; saved flags must describe the intended current facts |
| Keep guessing | Numeric input, separate range checks and INT comparison | Sinclair BASIC has numeric conditions and its own input/keyword rules; reading the local range explanation is optional |
| Independent learner tasks | Recall supplied in the prompt, small tables and counterexamples | Paper reasoning, not a new runtime or compulsory prior course |

The [complete Foundations map](../2026-10-foundations-objectives/MAP.md) retains
its own immutable baseline. This report adds direct unit-4 evidence without
rewriting the old source snapshot or claiming all mapped objectives are validated.

## Findings and correction

For the values 0, 1, 1.5, 10 and 10.5, both original guards choose Good guess
for 1, 1.5 and 10. Accepting 1.5 is correct for a numeric interval. A whole-number
game has an additional rule. The missing distinction could otherwise encourage
a reader to copy a range check as complete input validation.

Visual inspection also found a broken inline code span in the troubleshooting
list: the source line break put `> 0` at the start of the continuation. The
rendered text showed a stray backtick. We kept the complete condition together
and added a rendered-text rejection for literal Markdown backticks. The
[observation](formatting-observation.json), [capture](inline-formatting-observation.png)
and [earlier scoped browser run](browser-before-inline-fix.json) remain retained;
that run’s passed checks had not detected this formatting defect.

The lower-bound wording also relied on an unstated domain. For whole numbers,
`guess > 0` and `guess >= 1` agree. For 0.5 they do not. The correction names
that distinction and preserves the intended inclusive boundary.

For the shooting rule, the ungrouped expression permits shooting with alive
FALSE and grenades positive. All eight Boolean combinations were enumerated;
exactly two rows distinguish the guards, one for each ammo value when alive is
FALSE and grenades is 1. The new question asks for the result and repair, rather
than only recommending brackets without an observable consequence.

Finally, `guess = 3 OR 7` does not provide two Boolean operands in the teaching
notation. That does not mean every real language reports a syntax error. Actual
Sinclair BASIC accepts its numeric operands; the tested shorthand returns 1 even
for guess 4, while the repeated-comparison version returns 0. The lesson now names
the target distinction while keeping the complete Boolean question as the rule.

## Results and limits

| Check | Result | Evidence and boundary |
| --- | --- | --- |
| Exact-rational numeric cases | Passed 11 | [Model results](model-conditions.json): endpoints, three half-unit fractions, interior/exterior numbers, wrong OR/AND, whole-number distinction and 3-or-7 membership |
| Boolean shooting rows | Passed all eight | Same model: three intended passing rows; exactly two ungrouped counterexamples |
| Actual ROM numeric expressions | Passed 99 printed numbers | [Native results](native-conditions.json): nine outputs per selected value; actual normal ROM completion and no unexpected extra output required |
| Actual ROM grouped/ungrouped guards | Passed 16 printed numbers | Same native record: two outputs for each of eight input combinations |
| Deliberately wrong native guard | Rejected with nonzero exit | [Known-red result](known-red-native/rejection.json): wrong inclusive OR accepts outside input -1; observed output retained separately from the failed policy assertion |
| Production/repository/browser checks | See retained outcomes | [Website results](website-results.json) and [browser results](browser-after.json) name exact passed checks and unqualified configurations |
| Learner outcomes | Unknown | Prompts prepared; no learner observation, retention or unaided transfer result |

[verify-conditions.py](verify-conditions.py) uses Fraction calculations and a
separately enumerated shooting policy for the model. These are host checks,
not execution of a shared pseudocode language. The command transcript in
[native-commands.txt](native-commands.txt) records actual keyboard-entered BASIC
assignments and PRINT expressions. Setup uses LET for the named inputs; it does
not inject BASIC source, write result memory or patch the ROM. Full 16K ROM reads
supply the configured ROM fingerprint; incomplete reads fail.

Fractions are entered as exact divisions such as `3/2`, avoiding an assumption
about decimal-literal conversion from the earlier investigation. Numeric checks
operate on those values, not arbitrary text, NaN, infinities or another language's
number type. INT is used only for the explicit whole-number contrast. No arbitrary
numeric truth, short-circuit behaviour, performance or original-hardware claim is
made. The ROM process is closed and its exit checked even after a failed assertion.

The [fraction screenshot](fraction-native.png) shows `0,1,1,0,1` for the second
expression group at 3/2: the whole-number interval fails, both lower bounds pass,
correct 3-or-7 membership fails, and numeric shorthand succeeds. The
[grouping screenshot](grouping-native.png) shows `0,1` for alive 0, ammo 0,
grenades 1. Both display normal `0 OK` completion and were visually inspected.

The final production build and all 237 repository tests pass. Chrome
155.0.8059.80 checks at 1440×900 and 390×900 pass six keyboard behaviour
groups, with no document overflow, page errors or scoped axe violations. Both
new answers open by keyboard; the optional BASIC explanation and Back work.
The visible prediction/answer captures were inspected at readable viewport size.
The preserved full-page images are too tall for useful chat-scale inspection.

Axe leaves four narrow code-line colour checks incomplete, including with answers
revealed. We retain those raw incomplete results. The independent rendered-colour
probe measures each affected line at both horizontal scroll endpoints: **eight
samples**, all at least **16.8168:1**. This checks those text/background
pairs, not general accessibility. Physical mobile, screen-reader use, live
publication and learner outcomes remain unqualified.

The initial sandboxed Chrome launch failed before page observations with
`browserType.launch: Target page, context or browser has been closed` and SIGABRT.
[The failure record](browser-launch-failure.json) is retained; no baseline browser
pass or screenshot is claimed. The page checks were retried outside that sandbox.
The first chosen local-server port was already occupied; binding failed with
`OSError: [Errno 48] Address already in use`. We used a different task-owned port,
without adopting the existing server. The final browser record identifies its
own localhost origin. These are harness/environment observations, not product bugs.

[Evidence validation](validation.json) checks source hashes, complete native
transcripts, browser counts and document links; a wrong source hash and a missing
transcript are deliberately rejected. [verify-evidence.py](verify-evidence.py)
repeats these checks with `--website PATH_TO_WEBSITE_REPO`. The
[SHA-256 manifest](SHA256SUMS) retains the evidence file identities.

## Next bounded step

Use the independent interval and grouping tasks when a learner is available;
record help and reasoning separately from successful execution. Meanwhile,
audit Repeating unit 1's counted-loop contract across zero/one passes and body
placement. Its shared inclusive range is not proof that a target BASIC dialect
skips the same initially empty range. Start with the existing repetition evidence
and actual target rules before proposing any new correction.
