# First session guide pack draft

This pack gives a learner one place to begin and gives a parent or teacher enough
support to share the activity. It is a content draft for review before website
implementation. The linked lessons are already published; this pack has not been
tried with learners.

## Read the draft

Start with the [learner guide](learner-guide.md). It offers two independent
activities:

- [Make a greeting with Spectrum BASIC](activities/spectrum-basic.md).
- [Change the Spectrum border with assembly](activities/spectrum-assembly.md).

The [session sheet](session-sheet.md) provides space for predictions and notes.
The [parent and teacher guide](parent-teacher-guide.md) holds preparation,
hints and expected results. [Feedback](feedback.md) is optional and can be
returned through the person who shared the pack.

## Proposed publication

Publish the learner guide as one shareable web entry, with each activity at its
own stable address. Link the companion guide separately. Offer the session sheet
as a print view with the activity title and full lesson address visible. Use the
existing site layouts and controls. Check actual print layout before calling it
print-ready; a downloadable PDF can follow from the same content if useful.

The existing Start Here page continues to serve the wider curriculum. This pack
provides a bounded first session and links back to that wider choice. It does not
replace Start Here or turn Foundations into a prerequisite.

## Adding activities

Keep the entry guide short. As choices grow, group them by what readers want to
make or investigate, then show the machine, language and tools each uses. Offer
a small starting selection with a route to the full list. Do not rank languages
as compulsory beginner-to-advanced steps or make programming experience the
only way to choose.

Each activity needs:

- A visible result, knowledge assumed, equipment and access needs.
- A named, published lesson with working instructions and maintained samples.
- A bounded core: predict, run or trace, change, explain, and keep the result.
- A clear stopping point, optional depth and a next lesson.
- Companion notes with preparation, hints, expected results and a recovery path.
- A record of source checks, execution configuration and any learner observations.

Use descriptive names that survive reordering. The two Spectrum activities are
the first entries, not the permanent shape of the pack. Future machines, paper
activities and game-making investigations can use the same responsibilities
without copying Spectrum controls or imposing a fixed worksheet length.

Keep shared preparation and feedback in their own documents. Add only the new
activity's requirements and answers to the companion guide. Keep runnable code
and detailed teaching in the maintained samples and lessons; this pack directs
the session rather than maintaining a second version of each course.

Add an activity to the public selection only when its actual entry, result,
saving/recovery steps and links have been checked. Publish no empty routes or
promised activities. If a published activity becomes unusable, explain the
problem and offer a working route while it is repaired.

## Draft checks

The source review uses website commit
`f895b34fc8a316013b15b043d353daa6c24f4c66` and the existing
[Meet Assembly publication record](../../platforms/sinclair-zx-spectrum/assembly/meet-assembly-opening.md),
[editable BASIC record](../../platforms/sinclair-zx-spectrum/basic/browser-trial.md)
and [stored-value pilot](../../audit/2026-10-spectrum-learner-journey/stored-value-pilot/REPORT.md).
Those records distinguish native and browser evidence. This draft introduces no
new runnable listing and makes no new claim of machine execution.

Content and link checks are recorded in the PR. The pack's own public navigation,
print layout, classroom suitability and independent learner outcomes remain to
be checked. Before publication, run each exact activity and its saving/recovery
steps in the supported browser configuration, check keyboard access and narrow
layouts, and inspect the printed sheet. Do not infer a pack-level learner trial
from an earlier technical check.

Draft validation on 15 October 2026:

- All 24 relative links in the seven pack documents resolve to files. The
  shared docs index links to this pack.
- All eight linked public URLs returned HTTP 200 in Chrome 155.0.8059.40.
  Both fragment targets exist. The opening BASIC menu was expanded to check
  Download tape and Reset to original; the named assembly controls also exist.
  [Live link results](review/live-links.json) retain page titles and status.
- Expected starting outputs and changes were checked against the maintained
  greeting and first-program sources and the linked lesson explanations.
  The existing publication records cover execution; no program was run anew
  for this content-only draft.
- Vale and `git diff --check` passed. No website build or new automated tests
  are needed for these Markdown additions.

Two link-harness mistakes were corrected before the completed check. The first
looked for a hidden control before opening its menu and reported
`Error: Missing BASIC Download tape`. The second navigated from a page to its
own fragment, where Playwright supplies no new HTTP response, and reported
`Error: https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-02-remember-and-save/#reopen-your-saved-greeting: HTTP undefined`.
That [failed run](review/anchor-navigation-harness-failure.json) is retained.
The completed check opens a fresh page for each URL and verifies the fragment
separately. Neither failure establishes a product defect. The checks establish
link and control presence, not successful program execution or downloads.
