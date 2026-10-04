# Learner journey fixes

The findings in [the review](REPORT.md) are addressed by [website PR #617](https://github.com/code198x/website/pull/617), merged as `3484ed4a5592cb4cd8bc50aa4ea9c9a65d0fff12` on 4 October 2026.

- Assembly diagnostics now show the actual message and original source line. “Edit line…” opens the correct main or companion editor and selects that line. Expanded includes retain their original file/line mapping. The error panel wraps messages and uses the existing ink tokens for readable text.
- The gateway launch note follows the selected variant's bundled-firmware metadata. Required firmware included by the build is distinguished from missing firmware, optional files and built-in demonstrations.
- The assembly track's starting link is in its opening block. Local setup is explicitly optional for browser learning. The gateway, homepage and Meteor Storm overview clarify independent beginner routes and the Meet Assembly foundation.
- The first Meet Assembly editor exports current source and explains what reload, leaving the page and Revert do to edits.
- Gloaming's obsolete first-game claim is removed; complete course counts describe published units. No continuation beyond Meteor Storm is commissioned.
- The early Meteor Storm answer is behind the existing prediction disclosure. The expected mostly black screen is explained at the first run instruction.
- Focused checks identified an additional byte-experiment regression: switching stages folded the source drawer instead of its explanation. Byte and routine experiments now select the intended explanation explicitly. Execution fixtures open source drawers explicitly; movement input checks await actual pressed/released readings, and navigation checks accept canonical URLs with or without a trailing slash.

## Verification

The local candidate `b9c3b234` passed 160 unit tests (nine existing skips), content/route/imagery/reference and prepared-asset checks, a 2,428-page production build, 216 desktop/mobile browser checks, eight focused Spectrum execution/release scripts, focused visible-error accessibility, seven announcement regressions, and offline built-site links with zero errors. The final eight new journey tests also passed after adding the visible-error accessibility assertion.

[Focused execution results](fix-focused-checks.json) retain the actual-machine assertions. The tests cover edited source export, diagnostic line selection, source-drawer continuity, both movement boundaries, real frame timing, guided repairs and all eight lesson transitions. Maintained executable sources in code-samples are unchanged.

[Deployment succeeded](https://github.com/code198x/website/actions/runs/37223377347). [Live desktop and narrow-width checks](fix-live-checks.json) passed on https://code198x.com: the first-lesson link is fully visible in the opening viewport, edited source downloads exactly, errors display the readable line-6 message, keyboard activation selects the faulty editor line, Revert successfully runs the original program, the gateway reports the included ROM, and changing byte experiments preserves the editor while folding the explanation. No page JavaScript errors were observed.

A fresh learner trial remains outstanding. Neither these checks nor Claude's text review establishes uncoached comprehension, audible sound quality, Safari behaviour or physical mobile-device behaviour.
