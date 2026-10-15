# Foundations and Spectrum understanding pilot

Agreed approach: one bounded pilot contributing separate evidence to umbrella
[#114](https://github.com/stevehill1981/198x/issues/114),
[#115](https://github.com/stevehill1981/198x/issues/115) and
[#124](https://github.com/stevehill1981/198x/issues/124).

## Objective and boundaries

Follow a stored value, predict what a read will show, and explain what a later
write changes. Use Foundations' assignment model, Sinclair BASIC's named
variables and Z80 reads and writes without implying that a BASIC variable, an
assembler label and a register are interchangeable.

BASIC and assembly remain independent entry points. Foundations and the Vault
provide optional depth; completing them is not a prerequisite. This pilot does
not complete the wider Foundations audit or commission a course rewrite.

Reuse the [4 October journey review](../audit/2026-10-spectrum-learner-journey/REPORT.md)
and [published fixes](../audit/2026-10-spectrum-learner-journey/FIXES.md).
They provide historical browser evidence, not current execution or learner
validation. The outstanding learner trial remains outstanding.

## Baseline identities

Source inspection on 15 October 2026:

- Website: `290146661779c23562c089adf61b71ee50d693d4`.
- Code samples: `e3cf3694b7122adb5f383029a3c9e8c33c9d784b`.
- Documentation: `746fc7746309b4ebd3a039f30ad9e96095986f3a`;
  existing local README/work queue edits are outside this change.

The website's `src/content/modules/foundations.yaml` inventories ten modules
across programming, numbers and the machine underneath. This pilot samples
Basics; numbers, logic, game maths and wider dependencies remain unaudited.
Catalogue `complete` status is not evidence of learner understanding.

## Tasks and verification

1. **Map the selected objective and prerequisite knowledge.** Inspect website
   files `src/content/curriculum/foundations/basics/unit-03.mdx` and
   `unit-04.mdx`, `sinclair-zx-spectrum/basic/meet-basic/unit-02-remember-and-save.mdx`,
   and `sinclair-zx-spectrum/assembly/meet-assembly/unit-02.mdx`, all under
   `src/content/curriculum/`. Record which terms each explains locally and where
   it sends a beginner. Check `specifications/pseudocode.md`. Verify statements
   against the actual lesson and sample, not the catalogue alone.
2. **Establish the technical and navigation baseline.** Use the BASIC sample
   `sinclair-zx-spectrum/basic/meet-basic/opening/unit-02/steps/step-01.bas`
   and assembly sample
   `sinclair-zx-spectrum/assembly/meet-assembly/opening/one-byte.asm` in
   code-samples. Read their existing verification recipes before running them.
   Record source, tool/ROM identity, build/load route and actual observations.
   Inspect discovery from `/start-here/`, optional Foundations links, both
   independent machine routes, and `/vault/techniques/variables-memory/`.
   Record missing connections as observations; do not assume that this route
   already exists. Check the Vault entry's suitability for a beginner rather
   than making its detailed storage discussion compulsory.
3. **Prepare understanding tasks using existing controls.** Ask for a prediction
   before revealing an answer: read the same stored value twice; replace it and
   read again; explain why earlier output is unchanged. In assembly, distinguish
   a source edit from assembling/running, and distinguish changing the source
   byte from changing the copy already in screen memory. Include one deliberate
   wrong-name/address fault and one new task without a supplied solution.
   Supply assessor expectations separately from learner prompts. Check that
   unfamiliar syntax is explained and that the tasks test the objective.
4. **Review the rendered experience.** Record exact URLs, revision/deployment,
   browser/version, OS and viewport sizes. Check keyboard use, readable code,
   reveal order, mobile layout, source editing, run/recovery and startup time.
   Record unavailable browsers, assistive technology and physical devices as
   skipped or unknown. Reuse existing checks where applicable.
5. **Prioritise and agree one bounded improvement.** Keep up to five prioritised
   findings for #124. Fix confirmed bugs before adding features. Capture the
   unchanged baseline, then comparable after evidence. Changes to lessons,
   samples or controls belong in their owning repositories and follow their
   existing editorial/publication requirements.
6. **Run a real learner trial and report limits.** Use the independent entry
   routes without coaching learners through a preceding language. Record task
   outcomes, explanations, help needed and confusions, with consent and without
   publishing identifying information. Lack of access to learners leaves this
   step pending; AI responses and scripted runs cannot pass it. Report
   editorial, technical, UX and learner evidence separately to each parent.

Store prompts and evidence beside the existing journey audit, with explicit
passed/failed/skipped/unknown/pending outcomes. Every reported result must name
the check and its actual evidence. Do not overwrite the earlier review.

## Finding and issue workflow

During each step, check open and closed issues in the owning repository and the
umbrella before filing. Reuse an existing issue when it describes the same
problem; earlier closed reviews do not prove a new route works.

File confirmed, actionable findings routinely in the repository that owns the
fix. Include the exact page/source revision, observed and expected behaviour,
reproduction or conflicting passages, learner consequence as a hypothesis where
untested, bounded acceptance checks and the relevant umbrella links. Record
unconfirmed concerns as questions rather than defects. Link filed issues from
the pilot evidence and relevant umbrella issues; do not create another pilot
epic or duplicate implementation plan.

Initial source finding: [website #689](https://github.com/code198x/website/issues/689).
Foundations Basics unit 4 opens with a claim that showing
a value makes the computer forget it. The same page later displays `score` and
retains it in a trace. Correctness of the opening wording needs a bounded
editorial fix. Source inspection establishes the inconsistency; no learner
effect or current emulator behaviour has been measured in this planning pass.

## Current evidence

- **Passed:** source inspection identifies shared stored-value material in all
  three selected lessons and an existing BASIC-to-Foundations link.
- **Failed:** Foundations unit 4's opening claim is inconsistent with its own
  retained-variable example.
- **Pending:** full prerequisite map, new technical execution, current browser
  baseline, assessment prompts, improvement comparison and actual learner trial.
- **Unknown:** whether the wording has caused learner misunderstanding.

Next bounded step: complete the selected pages' prerequisite map and prepare
the repeated-read/replacement tasks before changing the learning experience.
