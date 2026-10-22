# Decisions and boundaries: second pilot evidence pass

Two conceptual gaps are confirmed in Foundations' choice lesson. It confuses
input-dependent output with conditional execution, then overlooks zero in an
example of a supposedly always-true condition. The proposed correction preserves
the existing lesson and adds a negative/zero/positive prediction with a folded
answer. It is prepared for review, not published.

No learner is currently available. The [learner prompts](LEARNER-TASKS.md) and
[separate assessor notes](ASSESSOR.md) are draft trial material, not evidence that
the lessons teach effectively. Umbrella
#114,
#115 and
#124 remain open.

## Identities and method

Checked on 15 October 2026. Isolated source baseline: website
`f219ace5077ce72dedf60f601b30f4581f8b7a31`, docs
`e5864c3fb7224f4b2f8bf6acf3d39f604bd3c725`, samples
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. Existing unrelated work in the normal
checkouts was excluded. Local after checks used a production build of that
website baseline plus the proposed choice-lesson correction. Live baseline
checks confirmed both original claims independently of deployment provenance.

Chrome `155.0.8059.40`, Playwright `1.62.1`, axe `4.13.0`, macOS `27.0`.
The targeted page checks used 1440×900 and 390×900 CSS-pixel viewports. The
maintained debugger verifier used 1280×1000 and 390×844. These are desktop-browser
viewports, not physical-device results. Native runs used the configured 48K
Spectrum ROM through Emu198x's MCP keyboard route. Native results record the
actual binary/version, source hashes and configured ROM fingerprint. No firmware
or generated tape is retained here.

## Prerequisites and connections

| Surface | Knowledge used and locally supplied | Independence and limits |
| --- | --- | --- |
| Foundations `decisions/unit-01.mdx` | Uses input, variables, output and number order; explains condition, equality versus assignment, and `<`/`>` | Earlier Basics unit 5 and Working It Out unit 1 already show changing output from input. Those are counterexamples to the original opening. Pseudocode is reasoning notation, not a target language. |
| BASIC `meet-basic/unit-05-give-a-useful-clue.mdx` | Complete listing; explains numeric variables, keyboard `IF`/`THEN`, comparison, separate numbered lines and numeric input | Links the opening for entry/editing, module keyboard help and Foundations choice lesson for optional depth. No assembly dependency. Lesson 5 compares zero; lesson 6 later rejects it under the game's range rule. |
| Assembly `meet-assembly/unit-08.mdx` | Investigates the earlier timed-character program; introduces breakpoint, step, Z, PC and observations progressively | Assumes earlier assembly lessons and the program they built; BASIC is not required. Actual Z flag state is not an interchangeable language Boolean variable. The relevant zero test concerns unsigned screen position, not every possible Z80 comparison. |
| Vault `techniques/state-machine.mdx` | Source exists and supplies optional conditional game-state context | Advanced optional connection supplied in the trial pack. Its discovery, usefulness and return journey have not been tested with a learner. No new public link or mandatory prerequisite is commissioned. |

The shared objective is predicting conditional work and selecting evidence at a
boundary. A sequence can calculate different output without choosing different
instructions. Three separate BASIC conditions are all tested; an earlier true
condition does not suppress later tests. In assembly, inspect the actual flag
and branch destination rather than infer them from a symptom or source text.

## Findings filed routinely

1. [Website #695](https://github.com/code198x/website/issues/695): distinguish
   input-dependent output from conditional execution. The opening's claim that
   earlier programs cannot react contradicts earlier greeting and sum examples.
   Native straight-line input/output observations reproduce the distinction.
2. [Website #696](https://github.com/code198x/website/issues/696): correct the
   zero boundary in the condition example. `0 > 0` is false even though zero is
   not negative. A request to enter positive values is not an enforced domain.

Open and closed issues were searched for decisions, the lesson title and zero,
along with umbrella condition-related work, before filing. Both findings belong
to one bounded correction in `foundations/decisions/unit-01.mdx`. No rewrite or
new dependency is needed. The likely learner confusion is a hypothesis; nobody
has been observed making these errors in this pilot.

## Evidence and outcomes

| Check | Outcome | Evidence and limits |
| --- | --- | --- |
| Original choice lesson at two widths | Failed conceptual review; passed selected technical checks | [Baseline](browser-baseline.json) confirms both original claims, HTTP 200, no document overflow and zero reported scoped automated WCAG A/AA violations. These are direct page loads, not an uncoached discovery trial. |
| Lucky Number's maintained native experiments | Passed 12 cases | [Native experiments](native-experiments.json): changed secret, numeric expressions, undefined input, syntax recovery and rejected boundary/fraction cases in lesson 6. This does not claim lesson 5 validates those values. |
| New ROM boundary and comparison observations | Passed nine cases | [Native results](native-boundaries.json) and [driver](verify-boundaries.py): strict `>` for -1/0/1, two input-dependent straight-line outputs, published low/equal/high clues, and deliberate overlapping conditions producing both wrong messages. Complete output rows and termination report are checked. |
| Maintained live assembly debugger | Passed four groups | [Results](live-debugger.json): symptom with actual input, progressive machine-state inspection, ordinary branch repair plus zero boundary, independent erase-data fault/repair, narrow layout, keyboard step and zero scoped axe violations. These are emulator observations, not original hardware. |
| Isolated production build | Passed after setup correction | Shared page frame verified and search indexed. Two earlier setup attempts failed on Astro compile metadata for symlink-resolved UI/package source; a local copy of the existing pinned kit and installed packages resolved the workspace problem. No new dependency was installed. |
| Proposed page at two widths | Passed | [After](browser-after.json): original claims absent, no overflow or reported scoped automated WCAG A/AA violations; answer initially closed, Enter opens all three correct comparison rows. Narrow/wide captures visually inspected. |
| Known-red control | Expected failure, confirming rejection | [Control](known-red-control.json): the same after-check run against the unchanged live lesson exited nonzero with `Error: Original misconception remains`. This expected rejection is separate from the passing proposed-page check. |
| Local repository check | Passed | 31 test files; 218 tests passed and nine existing skips; content/link and prepared NES assembler/player checks passed. Decoder-dependent skips are not decoder passes. |
| Prose, design detector, Python and patch checks | Passed | Vale reports zero errors/warnings/suggestions for the changed lesson; mechanical detector returned `[]`; Ruff passes the new driver; `git diff --check` clean. |
| Real learner understanding and integrated discovery | Pending | Trial pack prepared, no responses collected. Existing BASIC → Foundations link is source-confirmed; the broader discovery/Vault/return tasks need observation. |
| Physical mobile, other host/browser combinations, screen readers, audible output, original hardware and startup latency | Skipped or unknown | Not established by this slice. Selected viewport checks do not establish any of these. |

The first pilot's failed supplemental BASIC browser assertion remains a failed
harness result in its own report. This slice does not retry or reclassify it;
BASIC observations here use the maintained native ROM route.

## Proposed bounded improvement

Keep the lesson's examples and sequence. Replace the opening with the accurate
distinction between changing input/output and conditional instruction execution.
Replace the faulty troubleshooting example with boundary testing, then ask
readers to predict `guess > 0` for -1, 0 and 1. Keep the table behind a native
keyboard-operable disclosure. Explain comparison versus assignment and why a
condition can be always true under actual prior validation, rather than a prompt.

Compare [before at 390px](before-390.png), [after at 390px](after-390.png) and
[after at 1440px](after-1440.png). This establishes an explicit correct model and
working presentation, not improved comprehension. No public lesson route,
architecture, runnable sample or dependency changes.

## Reproduce and continue

From the website checkout, using its existing installed tools and prepared assets:

```sh
node scripts/verification/decisions-boundary-pilot.mjs https://code198x.com /tmp/decisions-before baseline
node scripts/verification/guided-debugger.mjs https://code198x.com /tmp/decisions-debugger
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 1996 --ignore-lock
```

In another terminal:

```sh
node scripts/verification/decisions-boundary-pilot.mjs http://127.0.0.1:1996 /tmp/decisions-after after
```

From the docs checkout, with a configured native emulator:

```sh
python3 audit/2026-10-decisions-boundary-pilot/verify-boundaries.py --samples ../code-samples --emulator /path/to/emu198x-spectrum --output /tmp/decisions-native
```

The Lucky Number sample README supplies the maintained `verify_experiments.py`
recipe. [Evidence hashes](evidence-sha256.json) identify retained observations and
captures. The known-red control is expected to stop being a useful unchanged
baseline after this correction is published.

Next bounded step: editorial review of the correction and trial pack, followed by
a real learner trial when available. Broader Foundations coverage, independent
machine pathways and integrated learner experience remain wider obligations of
the three parent issues.
