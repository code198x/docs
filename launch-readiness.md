# Website release readiness

This is the release checklist for Code198x, with Spectrum first. The site is already published; this checklist governs making the next release dependable. It records acceptance work, not a second curriculum roadmap. [Current work](work.md) owns future teaching deliveries; [website and publishing](website.md) owns the process.

An unchecked item is outstanding or unverified. Close it with the tested revisions, configuration, command or review, result and evidence location. A native check, browser check, listening check and learner trial are different evidence. Recheck affected items after changes; results from before the current styling do not sign off the styled release.

## Current acceptance — 7 October 2026

The visual rollout is no longer waiting for styling. The result-first homepage,
learning routes, editable BASIC and modal emulator are implemented, followed by
Vault discovery/reading, Pattern Library and browser-first Setup. The remaining
website pass adds readable game previews, connected Timeline stories and targeted
utility/editorial layout fixes. Its [implementation and verification record](https://github.com/code198x/website/blob/51cfee47/docs/plans/2026-10-07-website-finish/README.md)
identifies the candidate and test evidence. [Website PR #645](https://github.com/code198x/website/pull/645) owns publication status.

| Area | Evidence and remaining boundary |
| --- | --- |
| Accepted identity and lesson UI | Website `bcfba43b2`; [rollout checks](https://github.com/code198x/website/blob/main/docs/plans/2026-10-06-approved-design-rollout.md). The old overlay-selector failure below is historical, superseded by passing modal focus/navigation checks. |
| Vault and Pattern Library | Website `e7c7793ba`; reviewed article connections, reading layouts and task-led pattern browsing are implemented. This does not certify all Vault facts or every pattern's machine behaviour. |
| Setup and family tools | Website `7744efcb3`; [Setup record](https://github.com/code198x/website/blob/main/docs/plans/2026-10-07-setup-journey/README.md). Browser starts lead to existing lesson tools; local instructions name Asm198x, Build198x and per-machine Emu198x Homebrew packages. Docker is not the recommended entry route. |
| Dependency advisories | Website `9e80829c0` contains the dependency remediation. Its passing build is separate from visual and learner acceptance. |
| Current release checks | `npm run check:release` passed on 7 October: 187 unit tests, seven announcement regressions, content and prepared-player checks, production build, 202 browser checks and 221,603 offline link references with zero errors. The existing link exclusions omit images, assets, mail links and localhost; this is not an external-link audit. |
| Remaining page families | Desktop/mobile and both-theme checks cover utility pages, teaching/About, system facets, family explainers, editorial articles, an embedded experiment and Timeline. The finish record names the actual samples; this is template coverage, not a visual inspection of every authored page. |
| Other browser engine | 30 WebKit checks passed with desktop and iPhone emulation: Timeline navigation/filtering, game previews, search and Setup/lesson-tool routes. Physical mobile devices, Safari application behaviour, audible quality and orientation acceptance remain unverified. |
| Final review corrections | The independent reviewer scored all four material fixes resolved. The rebuilt candidate passed 82 focused Chromium checks, including both themes and desktop/mobile; the earlier full release and WebKit runs retain their stated scope. |
| Learning acceptance | The [October learner-journey review and fixes](audit/2026-10-spectrum-learner-journey/FIXES.md) establish expert review and browser execution. An uncoached learner trial remains open. |

The open rows below retain their own scope. A broad item stays unchecked when
only part has evidence. Native gameplay, listening, content review and a learner
trial are separate from shipping these website changes; do not silently reopen
completed design work or claim those human checks passed.

## 1. Freeze a concrete release candidate

- [ ] Record the final website and code-samples commit IDs for the release candidate; the accepted styling is implemented. Record the shared UI, Emu198x, Play198x and Asm198x revisions actually used locally and by deployment, plus Node/npm and Rust versions. Deployment currently checks out sibling `main` branches: a local result for the website commit alone does not identify its dependencies.
- [ ] Land sample additions before website pages that include or link to them. Reproduce the candidate from clean checkouts with lockfiles; no local build products, unpublished sources or private paths may be required.
- [ ] Record the advertised launch routes and machines. Make available lessons, retained routes and planned coverage distinguishable on home, systems and course pages. Reconcile later Spectrum assembly navigation with the assembly session; Meet Assembly → Meteor Storm is the agreed opening.
- [ ] Review the finished home, About, systems, editorial hubs and What's New together. Check the actual claims, calls to action and entry links against what a visitor can use today.

## 2. Source, downloads and machine behaviour

- [ ] Rerun `node scripts/check-spectrum-samples.mjs --build --report /tmp/spectrum-audit.json` in the website checkout with the candidate Asm198x and Build198x. Require every available Spectrum unit's maintained source, BASIC listing, build and download to agree; require valid TAP checksums and Meteor interactive/download payload parity. See [verification instructions](../website/scripts/verification/README.md).
- [ ] Rerun Meet BASIC, Meet Assembly and Meteor Storm native checks from the candidate samples. Record the emulator binary, ROM hash, target and tool versions. Include all Meteor checkpoints, endpoint and boundary checks; retain alternate-assembler parity for Meet Assembly.
- [x] Repair the Spectrum Sound Beep pattern with maintained source and executable checks. Eight callers verify pitch/length, sweep order, complete border/MIC writes and return contracts; a separate fresh ROM tape load completes the demo. Recipe and retained results: [sound-beep](../code-samples/sinclair-zx-spectrum/patterns/assembly/audio/sound-beep/README.md), checked 2026-10-01. Publication and browser acceptance remain below.
- [x] Check the repaired beeper in an isolated production render: actual completion, four sounds delivered to the AudioWorklet, editable includes, exact source/include downloads, edited-source execution, revert, Sound off and narrow-screen layout. The downloaded tape has valid checksums and matches the native binary. [Browser results](../website/scripts/verification/evidence/sound-beep/results.json), checked 2026-10-01; rerun after styling or dependent changes.
- [ ] Listen to the beeper's fixed tone, rising sweep, falling sweep and click from the release candidate. The owner's earlier Meteor impact recording sounded fine; that does not sign off this new demo.
- [ ] Play the Spectrum entry route as a visitor: start without local tools, follow Meet BASIC and Meet Assembly → Meteor Storm, obtain the current source/tape and load it independently. Exercise held/tapped input, title/retry loops, game end, restart, readability and sound. For retained BASIC games, use each game's current verification recipe and perform human play checks; source-lineage audits alone do not establish playability.
- [ ] Check every other machine route promoted at launch with its own build/load recipe. Repair or clearly withdraw misleading runnable claims in the NES square-wave, C64 SID-note and Amiga sample patterns before promoting those examples. Their individual repairs remain in [current work](work.md#open-deliveries).
- [ ] Resolve the NES triangle held-output emulator defect before presenting that player as evidence for held output or clicks. Keep the lesson's hardware contract truthful; record a focused emulator regression.

## 3. Browser and styling acceptance

- [x] Run `npm run check:release` locally against the candidate (7 October; results above). This runs unit/content checks, announcement regressions, a production build, prepared-asset checks, focused browser/accessibility tests and offline built-site links. `npm run build` alone generates output; it is not test evidence. Record any accepted exclusions or failures.
- [ ] Run `npm run test:e2e` against the intended production preview and the full `npm run test:a11y:sweep`. Check light/dark, keyboard, focus, reduced motion, touch targets, narrow/wide layouts and contrast. Keep the accessibility exception baseline honest; do not add exceptions simply to obtain green results.
- [ ] Run the focused Spectrum browser scripts in [verification instructions](../website/scripts/verification/README.md), including release and lesson-sound checks, after styling settles. Confirm actual edited machine state, source continuity, download parity and useful error recovery.
- [ ] Test real Safari/WebKit and Chrome, plus a real mobile browser; the default Playwright desktop and mobile projects use Chromium and do not establish Safari behaviour. Check audio gesture requirements, WASM loading, canvas sizing and orientation changes.
- [ ] Exercise Sound on/off, Stop, replay, route changes, keyboard focus, fullscreen and multiple panels. Stop must suspend sound; leaving a lesson must not leave an audible or input-consuming player. Check slow load, failed fetch, bad source and missing firmware recovery messages.
- [ ] Check representative home, lesson, Vault and player pages on a throttled connection and mobile device. Record loading and interaction times, layout shifts and asset sizes; confirm readable content arrives before optional players load and images have reserved dimensions.
- [ ] Verify search finds available lessons and reviewed Vault material, follows result links and works after deployment. Check navigation, breadcrumbs, prerequisites, previous/next links, redirects, 404s and independent entry without completion gates.

## 4. Teaching and editorial truth

- [ ] Have a fresh learner try the Spectrum opening without coaching through the instructions. Record where they need help, whether they can predict an outcome, explain a changed case, recover an error and continue to the next unit. Fix consequential confusion before sign-off.
- [ ] Finish the recorded reviews of already-published material: Bright Spark muted/audible presentation, R4e sequencer contracts, C09c Dash handoff and the four Game Feel controls lessons. Where new exercise forms still need learner trials, prioritise those promoted by launch routes. Their detailed scope stays in [current work](work.md#review-what-was-published-without-its-recorded-review).
- [ ] Recheck outstanding findings from the [September content audit](audit/2026-09-content-audit/TASKS.md) against current pages. Specifically inspect indexed stubs, planned courses presented as available, entry routes, incorrect hardware/flag/timing explanations, generic misleading descriptions, missing sources, broken breadcrumbs and correction/production residue. Record current findings; historical audit rows are not proof that a defect remains.
- [ ] Check public source citations are visible and checkable, uncertainty is retained and public pages/downloads contain no private-library paths or unsupported ownership claims. Verify image, ROM, audio and third-party attribution/licensing for the assets actually shipped.
- [ ] Verify unreviewed Vault entries retain the required notice and are excluded from search indexing, sitemap and external search discovery as specified. Prioritise entries used by launch lessons; continue review batches under the [Vault policy](specifications/vault.md#reviewing-existing-entries). Reviewing every remaining Vault entry is not a launch prerequisite under that policy.
- [ ] Decide the release's Spectrum BASIC polish scope against its [polish audit](audit/2026-09-basic-polish/REPORT.md). Fix functional/readability bugs and align public quality claims with the delivered games. New sound, progression, title/loading art and extra units require agreed per-game scope; do not silently commission all fifteen games.

## 5. Deployment and a recoverable release

- [x] Trim automation to match the owner's local-check preference: quick content CI; Pages builds and publishes without browser/link/test-suite gates. Fuller verification is available through `npm run check:release`. The accepted rollout is published; the final candidate still needs its own deployment and live smoke evidence.
- [ ] Verify GitHub Pages environment, permissions, custom domain, DNS, HTTPS and canonical URLs. Check the actual deployment run and live result, including build logs and artefacts; local success cannot establish hosted configuration.
- [ ] Confirm the Spectrum ROM secret is configured and the built player boots without unexpectedly asking the learner for firmware. Inspect the deployed artefact rather than exposing secret contents. Check other machine firmware requirements and visitor instructions against their advertised experience and permitted distribution.
- [ ] Check player/assembler/decoder WASM, workers, source files, tapes, images, audio, fonts and Pagefind assets over the deployed origin, with the expected MIME types and no stale version mismatch. Verify a fresh browser and a previously cached session.
- [ ] Verify the live homepage, entry lessons, beeper pattern, downloads, search, robots, sitemap, social previews and 404 page. Check broken external sources separately from the offline internal-link check.
- [ ] Review dated/scheduled What's New posts, RSS diff and announcement payloads before release. Decide whether the eleven existing drafts are to be published. Deployment can trigger Discord announcements, and the daily scheduled deployment can release date-gated content; publication needs explicit owner authorisation.
- [ ] Record the previous known-good website/dependency revisions, exact rollback route and any announcement consequences. Preserve the candidate's test reports and deployment artefact; the announcement workflow's short-lived artefacts are not a durable verification archive.
- [ ] Complete a post-deploy smoke check, name who will inspect failures and where bugs are recorded, then sign off with the deployed URL and revisions. Record unresolved findings and the owner's release decision.

## Earlier evidence and its limits

Historical evidence, superseded for styling acceptance by the October 6–7 checks above: the Spectrum ROM secret name is configured in GitHub (metadata checked on 2026-10-01; secret contents were not read). The latest inspected CI run on the styling branch `shell-redesign-kit-0.7`, revision `1cb2a0febf6efc014ff71fc05e4c5a33fc94dede`, failed the overlay inert-state test on desktop and mobile because its `nav.nav` locator found no element. [CI evidence](https://github.com/code198x/website/actions/runs/36892184339). Resolve against the finished shell and verify inert/focus behaviour rather than simply dropping the assertion. This is branch-specific evidence, not a finding about the current local main checkout.

On 2026-10-01, the Spectrum audit found 304 authored pages, 279 available units and 499 referenced files. All 274 unit Makefile directories rebuilt; 518 BASIC listings passed lint. Asm198x 0.0.57 and 0.0.58 produced identical unit outputs. Native checks passed: Meet BASIC 16 checks; Meet Assembly nine programs with 18 tape comparisons; Meteor 28 checkpoints/240 checks, 50 endpoint checks and four boundary checks. Thirteen retained BASIC lineage audits passed. The owner listened to the captured Meteor impact and accepted its sound.

The reported 20 missing Vault targets were an isolation-copy error: an unanchored `tools` exclusion omitted `src/content/vault/tools/` as well as root build tools. The actual website check on 2026-10-01 resolves all 22,210 references across 1,486 entries and 186 redirects. No Vault-content repair is required for that report. The corrected full `npm run build` passed on 2026-10-01: 115 unit tests passed (nine skipped), production rendering, built-player checks and Pagefind indexing completed. All 2,859 source files in the isolated copy matched the working tree by SHA-256, including all 21 Vault tools entries. The log is `/private/tmp/198x-beeper-audit/site-build-corrected.log`; final release-candidate checks remain required. Future isolated copies must use root-anchored exclusions and preserve the complete content tree.

These are local observations for the audited sources and stock 48K configuration, not release-candidate/browser/hardware sign-off. Detailed working reports are currently in `/private/tmp/198x-spectrum-audit/` and `/private/tmp/198x-beeper-audit/`; temporary files must be archived with revisions before they are relied on for release. The beeper's portable result record is retained alongside its sample verification recipe.

## Work that is not a prerequisite by default

New games, a changed lineup, the player inspector, the C05 profiling companion, C09e feedback exercise, C10a randomness exercise, C11a input-port fixture, advanced audio engines, BASIC performance revisits and illustration experiments remain scoped curriculum/product work. Promote one to a release requirement only when an agreed release promise depends on it. Neither the full reference library nor a complete Vault review is necessary to verify the existing Spectrum sources and visitor journey.
