# Probability pilot: exact counts and rounded shares

We mapped all eleven published Maths for Games units and reproduced the unit 3
shares checkpoint in a native Spectrum. Seven observed cases passed. The selected
boundary is already explained correctly: rounded percentages can total 100.2%
while the underlying counts and exact shares remain consistent. We found no
lesson defect in this slice, so no website or sample correction is proposed.
Actual learner understanding remains unobserved.

This addresses the bounded technical/editorial work in
[docs #78](https://github.com/code198x/docs/issues/78), continuing umbrella
#114,
#115 and
#124. Approved reconciliation
[docs #79](https://github.com/code198x/docs/pull/79) merged at
`fe4c21505ebcd7542aa37b8dcf15f27db43718a5`, the docs baseline for this pilot.
The [reconciliation](../2026-10-education-reconciliation/REPORT.md) remains the
broader acceptance record, not a claim that every criterion is met.

## Source and objective coverage

Website revision: `1cb4ec62e675751a0c13006b2bff877cd0ec3f6c`. Samples revision:
`163e74e18e9536fb555ef7319fa08bbc1836542b`. The
[source inventory](source-inventory.json) identifies all eleven authored units,
their maintained source includes and the website integration files by SHA-256.
The [objective map](OBJECTIVES.md) records observable objectives, local
prerequisites and ownership for five probability and six aiming units.

This map comes from the authored lessons and actual source files. Probability
uses stock 48K Sinclair BASIC samples; aiming uses host-side JavaScript
experiments. The sequences have independent entry. Broader planned topics are
not counted as authored units, and no Foundations attendance rule is introduced.
Aiming's embedded teaching prose belongs to MDX; its standalone sample copy is
not another set of public curriculum units.

We read the existing source transitions and earlier
[Dice Roller execution/publication record](../../platforms/sinclair-zx-spectrum/games/dice-roller/lessons.md).
Its 35 execution groups and later publication checks remain historical evidence.
We did not rerun all five checkpoints or the six aiming controls in this pilot.

## The selected boundary

Unit 3's sample keeps exact whole counts in t(), divides each by the positive
total n and rounds the resulting percentage to one decimal place. Two distinct
questions follow:

- Do six non-negative counts account for every roll?
- Does each displayed percentage correctly represent its count/total after rounding?

Those checks can both pass when the displayed percentages do not add to exactly
100. A third question—whether the generator follows a fair, independent model—
is not answered by either accounting check or by a visually balanced sample.
The existing lesson already states those limits and explains why display must
follow the first counted roll rather than divide by zero.

The original Sinclair manual's
[chapter 11](https://worldofspectrum.org/ZXBasicManual/zxmanchap11.html) describes
the fixed pseudorandom sequence, seeding and the die expression. It supports the
lesson's distinction between a calculated sequence and physical chance. We do
not turn its approximate uniformity statement into an exact fairness or
independence claim for the mapped six faces.

## Fresh native evidence

Run [verify-shares.py](verify-shares.py) with the maintained samples checkout,
`emu198x-spectrum` executable and an output directory:

```sh
python3 -B verify-shares.py --samples /path/to/code-samples \
  --emulator /path/to/emu198x-spectrum --output /path/to/evidence
```

The configured native emulator reports **0.32.5**, on macOS 27 arm64 with Python
3.14.3. The observed 16 KiB 48K ROM SHA-256 is
`d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`.
[native-shares.json](native-shares.json) retains executable, ROM, source,
verifier and three maintained driver hashes, actual screen rows and variable
observations. [Stored token lines](stored-lines.json) retain the ROM-entered
program. No direct memory writes, source injection or ROM patching were used.

We entered the complete maintained shares listing through stock-ROM keyword
keys in a fresh process, verified its stored line set and ran it twice. Both runs
stopped deliberately after twelve rolls. We compared all six actual on-screen
counts and shares with the observed array/total. An independent exact-rational
calculation supplies rounding expectations rather than repeating the ROM's
floating-point expression as the oracle.

Four **audit-only diagnostic fixtures** then set ordinary BASIC variables through
ROM commands and call the unchanged header/display routines. They are not random
samples or normal menu interaction. Their exact commands are retained in the JSON.

| Case | Actual count vector | Observed shares (%) | Result |
| --- | --- | --- | --- |
| Ordinary first RUN | 2, 0, 2, 4, 0, 4 | 16.7, 0, 16.7, 33.3, 0, 33.3 | Pass; total twelve |
| Ordinary fresh RUN | 3, 2, 3, 0, 2, 2 | 25, 16.7, 25, 0, 16.7, 16.7 | Pass; fresh total twelve |
| Balanced twelve, diagnostic | 2, 2, 2, 2, 2, 2 | 16.7 on every row | Pass; rounded sum 100.2, exact sum 100 |
| Unequal twelve, diagnostic | 0, 1, 2, 3, 4, 2 | 0, 8.3, 16.7, 25, 33.3, 16.7 | Pass; zero and unequal counts |
| Same face-three count, smaller total, diagnostic | 0, 0, 2, 0, 2, 0 | 0, 0, 50, 0, 50, 0 | Pass; count two represents half of four |
| One counted face, diagnostic | 0, 0, 0, 0, 0, 1 | 0, 0, 0, 0, 0, 100 | Pass; positive denominator boundary |
| Ordinary RUN after diagnostics | 4, 0, 1, 2, 1, 4 | 33.3, 0, 8.3, 16.7, 8.3, 33.3 | Pass; diagnostics cleared, total twelve |

The last RUN also verified that stored program bytes were unchanged. Random
counts above are observations from these runs, not reproducibility promises for
clock-seeded RUN. Two known-red controls were rejected: asserting that the
balanced displayed total must equal 100, and replacing one observed 16.7 with
16.5. An empty or incomplete six-row observation cannot pass the checker.
No failed native attempt was needed in this run.

## Learner tasks and limits

[Six independent tasks](LEARNER-TASKS.md) and separate
[assessor notes](ASSESSOR.md) use new seven/eight-roll values, explicit ideal-model
assumptions, a proposed bad repair, a two-decimal modification and an investigation
design. They distinguish prediction, calculation, diagnosis, modification and
creation. The learner tasks do not ask for the existing lesson's worked
balanced-twelve answer.

All actual learner outcomes are **not observed**. The proposed two-decimal learner
extension is prepared but not freshly executed here; the seven native cases use
the maintained one-decimal program. No completion rate, hint rate, retention,
transfer, difficulty or educational-effectiveness claim follows from these prompts.

Fresh browser interactions, mobile/touch behaviour, accessibility/contrast,
latency, tape save/reload, aiming execution and original hardware are **skipped**
in this pilot. Their earlier evidence remains dated and configuration-specific;
there is no new browser pass. Zero-denominator fault execution is also skipped:
our observed display cases all have positive totals. The rational oracle and
native ROM are not two independent emulator implementations. These finite inputs
do not qualify every Spectrum arithmetic boundary or generator property.

## Outcome and next work

The selected technical accounting/rounding checks pass and the editorial map is
complete for the eleven current units. The existing explanation earns retention.
We did not file a speculative teaching bug or manufacture a lesson change.
Docs #78 can close when this bounded evidence is accepted; its parent issues stay
open and learner tasks stay unvalidated.

Next address the earlier retained embedded BASIC observation gap under
[website #747](https://github.com/code198x/website/issues/747). The other
[reconciliation priorities](../2026-10-education-reconciliation/REPORT.md#five-next-priorities)
remain latency, broader operability and actual learner observation. Keep the
first-session pack ready without expanding it before feedback arrives.

[Document verification](validation.json) checks current source/report identities,
seven positive native cases, both negative controls, eleven objective rows, six
task/assessor pairs and local links. This validates references and retained results,
not the skipped configurations or missing learner outcomes.
