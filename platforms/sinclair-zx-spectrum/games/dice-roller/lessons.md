# Dice Roller — teaching checkpoints

The [teaching specification](lesson-brief.md) defines five building lessons:
roll a die, keep tallies, compare shares, watch the live distribution, and
compare experiments. Complete runnable programs and exact editing metadata are
prepared in `code-samples/sinclair-zx-spectrum/basic/dice-roller/teaching/`.
The overview and five replacement lessons are authored locally for review.
The existing published lessons remain unchanged until publication.

The endpoint is byte-identical to the user-approved prototype. The first four
checkpoints expose separate observable results, rather than providing a hidden
engine. The opening is an eight-line new program. Later stages supply explicit
add/replace metadata and maintained changed-line listings; this sequence needs
no deletions. The last lesson groups comparison state, menu controls, display
cadence and saving around the accepted endpoint.

## Evidence

**35 execution groups pass across five checkpoints**, including all 19
prototype groups against the independently entered finished tape. Source
transitions, stored tokens, tape checksums and final identity pass. Samples
commit: `1ac3c53`.

Each source is entered independently through ROM keyword keys and recorded as
`SAVE "dice" LINE 10`. Checks load those tapes in fresh native emulator
processes under stock 48K PAL configuration. Observations read memory without
writing it. Execution records bind source and emulator SHA-256 identities;
the audit checks saved token bytes, TAP checksums, auto-start, reconstruction of
every source transition and identity with the prototype.

Intermediate checks cover twelve numbered rolls within the die's range,
nonnegative integer tallies totalling twelve, displayed rounded percentages,
two live chart states before completion, early-stop accounting and fresh RUN.
The finished tape receives the full prototype suite, including its labelled
zero/100% and accumulation-limit ROM-command fixtures. Captures from those
fixtures are diagnostic, not ordinary play. Known imperfect headless captures
are not suitable for publication.

This is emulator execution evidence, not independent learner review. The
website lessons include local explanations, exact editing instructions, source
disclosures, questions with worked reasoning, keyboard notes and primary manual
chapter links. Numeric identities and existing unit URLs are preserved. The
BASIC landing page places Dice Roller in Optional experiments; its empty earlier
games section is hidden. The release note stays draft. No native PNG is used
publicly, and no further game proposals are made mandatory.

## Website validation

Production build passes: seven test files, 69 tests and nine existing skips,
then content checks, static generation and search indexing. Five lesson/source
mappings and every add/replace instruction match the checkpoint metadata.

Twenty browser groups pass across desktop and Pixel 7 mobile emulation: all six
pages, local links, source includes, keyboard question disclosure, expanded-code
overflow, optional-experiment navigation and six preserved legacy redirects.
Twenty-four light/dark WCAG 2 A/AA and 2.1 AA accessibility checks report no axe
violations. Themes were measured with transitions disabled. The desktop overview
and mobile live-chart lesson were visually inspected. Compact records are in
`verification/lesson-browser.json` and `verification/lesson-accessibility.json`.

The local production preview is available for user review. Publication is not
performed, and the release note remains draft.
