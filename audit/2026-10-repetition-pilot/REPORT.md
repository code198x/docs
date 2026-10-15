# Loops and repetition: third pilot evidence pass

The selected lessons explain loop entry and iteration using different language
constructs. The assembly row-loop lesson already explains that B=0 does not skip
a DJNZ body. Preserve that distinction. One correction is needed in Foundations:
a fresh random choice is not guaranteed to differ from the last choice. BASIC's
existing explanation already permits repeated choices and fixed seeds.

[Website #699](https://github.com/code198x/website/issues/699) tracks the
confirmed inconsistency. The proposed change corrects the claim, explains why
the secret assignment is outside the guess loop, and adds a prediction and
optional BASIC connection. It is prepared for review, not published.

No learner is available. The [learner tasks](LEARNER-TASKS.md) and
[assessor notes](ASSESSOR.md) prepare a trial without claiming educational
effectiveness. Umbrella #114, #115 and #124 remain open.

## Identities and scope

Checked on 15 October 2026 in isolated linked worktrees. Website baseline
`d12fdad9030586c8b5ee6c7a2109c5feb33eeac4`, documentation baseline
`3c7aec317995647ce0c2825f04126a6a58d3e526`, samples
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. Unrelated changes in the normal
checkouts were excluded. Existing installed dependencies and pinned UI kit were
copied for the isolated build; no dependency was added or installed.

Headless Chrome `155.0.8059.40`, Playwright `1.62.1`, axe `4.13.0`, macOS
`27.0`. The changed-page checks used 1440×900 and 390×900 viewports; the maintained
live row-loop verifier used 1280×1000 and 390×844. These are desktop viewport
checks, not physical-mobile observations. Native ROM entry used Emu198x Spectrum
`0.32.5`; the [native results](native-repetition.json) record binary, driver and
configured ROM hashes. Python `3.14.3` and Ruff `0.16.4` checked the audit driver.

The local after checks used a production build of the baseline plus the proposed
Foundations change. Live checks confirm rendered content independently of source
commit identity; the current live repetition lesson remains unchanged at the time
of the baseline and known-red control.

## Prerequisite and transfer map

| Surface | What the material explains | Transfer boundary |
| --- | --- | --- |
| Foundations Repeating unit 1 | Inclusive counted ranges and loop counter; empty 1-to-0 range | These are the taught pseudocode conventions, not a promise about every instruction that uses a counter. |
| Foundations Repeating units 2–3 | Post-test REPEAT, pre-test WHILE, back edge and stopping question; random assignment before the guess loop | The secret is chosen once per round and held through guesses; a new choice can repeat a prior value. Pseudocode was traced, not run in an invented interpreter. |
| BASIC Meet BASIC unit 6 | IF/GO TO expresses a guess loop; returning to line 30 avoids reinitialisation | Complete listings and the linked preceding lesson explain keyboard entry and numeric conditions. BASIC does not use the pseudocode's literal REPEAT/WHILE syntax. |
| BASIC Meet BASIC unit 7 | ROM RND, range mapping, normal and fixed seeding, possible repeats | Already agrees with the proposed correction. Fixed-seed repetition is useful for reproducing a run, not evidence that all outcomes are equally likely. |
| Assembly Meet Assembly unit 4 | Source/destination pointers, B count, DJNZ and actual write replay | Assumes earlier assembly lessons, not BASIC. Already warns that zero B runs 256 turns, reading beyond this eight-byte table. Live checks here use safe counts 4 and 8; zero is reasoned from the taught instruction semantics rather than executed against the drawing table. |
| Optional LFSR pattern | Illustrative intermediate algorithm, same seed/same sequence | Not the ROM's generator and not an execution-qualified listing. It is an optional discovery/return task in the trial pack, not a mandatory beginner prerequisite. |

The route's live row-loop transfer test also checks a genuine cross-page task:
execute artwork in lesson 3, keep it in the same tab, then import it into lesson 4
and inspect the actual writes. That technical result does not establish that a
learner can discover and explain the workflow unaided.

## Confirmed finding and bounded proposal

The sentence “the secret is different every time” overpromises uniqueness. The
source contains one random assignment outside the loop and no previous-choice
comparison. BASIC lesson 7 explicitly says the new choice may be the same.
Website open/closed searches for random, secret and repeating, plus umbrella
random-related searches, found no matching issue before filing #699.

Replace the claim with a fresh choice that may repeat, keep the assignment before
REPEAT, and ask whether two rounds can both choose 7. Explain that moving the
assignment into the loop changes the target while the player guesses. Use a
native answer disclosure and an optional link to the existing BASIC explanation.
No sample, public route, new framework or curriculum gate changes.

The native bounded sequence contains `6, 6` and later `2, 2`. The identical
32-value sequence returns after the same explicit seed is restored. These are
observations of the ROM expression used by the lesson, not a statistical
qualification or a complete gameplay test. The likely effect on learner
expectations is a hypothesis until a learner trial is available.

## Results

| Check | Outcome | Evidence and limits |
| --- | --- | --- |
| Original random-choice claim | Failed conceptual review | Source contradiction with BASIC unit 7; [live baseline](browser-baseline.json) confirms the original claim at both widths. |
| Native counted loops | Passed three cases | [Native evidence](native-repetition.json): FOR 1-to-0, 1-to-1 and 1-to-3 produce zero, one and three body outputs, with complete output and completion checks. Configuration-specific ROM observation, not every BASIC dialect. |
| Native pre/post-test routes | Passed four cases | Explicit BASIC IF/GO TO pre-tests at 0, 1 and 3, plus a post-test toy at 0. The toy displays 0 once and decrements to -1 before stopping. This does not claim native BASIC WHILE/REPEAT statements. |
| Fixed-seed bounded sequence | Passed | Two 32-draw series agree; all observed mapped values are 1–10; repeated and consecutive repeated values are recorded. No fairness or security inference. |
| First native harness attempt | Failed setup, then corrected | Typing began while NEW was still resetting the machine, so the first FOR line was not stored. A diagnostic showed the ready copyright screen had not returned; after readiness it stored correctly. The driver now waits for that positive signal with a bounded limit before entry. This was not classified as a loop-semantics failure. |
| Maintained live row-loop verifier | Passed four groups | [Results](live-row-loop.json): eight ordered writes and replay/reset, same-tab executed artwork transfer, stale-result label, exact four-write stop, repeated-address replacement, edited download/revert, narrow layout and keyboard replay. |
| Production build and repository check | Passed | Production frame/search checks passed; 31 test files, 218 tests passed and nine existing skips; content/link and prepared assembler/player checks passed. Existing skipped checks are not passes. |
| Before/after page checks | Passed within selected scope | [Baseline](browser-baseline.json) and [after](browser-after.json): HTTP 200, no document overflow and zero reported scoped automated WCAG A/AA violations at both widths. The answer starts closed, opens by keyboard, and explains repeated choices. |
| Optional BASIC connection and return | Passed technical route | At both widths the actual authored link is keyboard-activated, destination explanation checked, and browser Back returns to the source lesson. Navigation animations are allowed to complete before the harness resizes. This is not unaided learner discovery. |
| First combined browser after-check | Failed harness timing | [Failure](browser-transition-failure.json): `InvalidStateError: Transition was aborted because of invalid state. Viewport size changed`. The harness resized during the return animation; waiting for the returned document and animation completion avoids that collision. Resize during an active transition remains outside the passing scope. |
| Known-red control | Expected rejection | [Control](known-red-control.json): the after verifier rejects the unchanged live page with `Error: Original uniqueness promise remains`. |
| Prose, design, Python and patch checks | Passed with one advisory note | Changed lesson Vale has zero errors/warnings/suggestions; design detector returned `[]`; Ruff passes. Trial-pack Vale has one advisory suggestion, no errors/warnings. Patch whitespace checks pass. |
| Actual learner outcomes, physical mobile, other hosts/browsers, screen readers, audible output, original hardware and startup latency | Pending, skipped or unknown | Not established by this slice. |

The first pilot's supplemental BASIC browser assertion remains a separate failed
harness result; it has not been retried or relabelled here.

Compare [before at 390px](before-390.png), [after at 390px](after-390.png) and
[after at 1440px](after-1440.png). Both proposed compositions were visually
inspected. The comparison establishes presentation and an explicit accurate
model, not improved comprehension.

## Reproduce and next step

From the website checkout with the existing prepared tools/assets:

```sh
node scripts/verification/repetition-pilot.mjs https://code198x.com /tmp/repetition-before baseline
node scripts/verification/row-loop.mjs https://code198x.com /tmp/repetition-rows
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 1998 --ignore-lock
```

In another terminal:

```sh
node scripts/verification/repetition-pilot.mjs http://127.0.0.1:1998 /tmp/repetition-after after
```

From the docs checkout, with the configured native emulator:

```sh
python3 audit/2026-10-repetition-pilot/verify-repetition.py --samples ../code-samples --emulator /path/to/emu198x-spectrum --output /tmp/repetition-native
```

[Evidence hashes](evidence-sha256.json) cover retained observations and captures.
The known-red control depends on the unchanged live page; it is historical
evidence after publication. Next: review the correction and trial pack, then run
the independent learner protocol when a learner is available. Wider Foundations
coverage and integrated learning-journey evidence remain unfinished.
