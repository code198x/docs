# Embedded BASIC: stored values and error recovery

Eight live browser checks pass for the stored-value task in Meet BASIC unit 2.
The machine prints ONE twice, then TWO. Both the wrong name in stored line 30
and the lesson's immediate wrong-name command report an error; their repairs
restore successful execution. Restart and source reset also work. We found no
product defect requiring a lesson or runtime change.

This supplies current execution evidence for
[website #747](https://github.com/code198x/website/issues/747), continuing umbrella
[#115](https://github.com/stevehill1981/198x/issues/115) and
[#124](https://github.com/stevehill1981/198x/issues/124). The
[earlier supplemental result](../2026-10-spectrum-learner-journey/stored-value-pilot/supplemental-browser-failure.json)
remains a failed historical harness attempt with an unknown product outcome.
Fresh success does not establish why that discarded harness failed.

## Task, source and environment

We exercised the published
[Remember a name; keep the program](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-02-remember-and-save/)
page at `https://code198x.com`, in installed Chrome **155.0.8059.40**, through
Playwright **1.62.1** and Node **24.22.0**, on macOS 27 arm64. The viewport was
**1440 × 1000**. These were scripted desktop input events, not a learner or
physical-mobile trial.

Website source baseline: `1cb4ec62e675751a0c13006b2bff877cd0ec3f6c`. Docs baseline:
`ddb7b803d5faed6ac2518816458c1e16f468dc0b`, after approved
[docs #80](https://github.com/code198x/docs/pull/80) merged. Samples:
`163e74e18e9536fb555ef7319fa08bbc1836542b`.
[Identities](identities.json) hash the lesson, listing/machine/runner/keyboard
sources, package files, original maintained greeting and final verifier.

[Deployment metadata](deployment-metadata.json) records the latest successful
website deployment inspected for this run. It names the website baseline above.
[Actual browser results](browser-results.json) retain the fetched HTML hash and
14 JavaScript/WASM response records, including the live WASM hash. Deployment
metadata alone is not proof of runtime execution or exact source-to-binary
provenance. The response identities bind this observation to the served artefacts;
we did not rebuild the website locally. The inspected package is
`@emu198x/zx-spectrum` 0.4.3; the browser ROM fingerprint was not captured, so its
identity relative to the earlier native ROM remains unknown.

## What ran

The [five-line fixture](repeated-read.bas) is the original stored-value pilot's
complete program. We edit it through the maintained page listing and choose
**Run this code**. The page builds a tape and loads it in its bundled-ROM machine.
We observe the product's screen-text view and actual rendered canvas. We do not
replace machine execution with a source-string assertion or a simulated transcript.

| Stage | Actual result | Evidence |
| --- | --- | --- |
| Repeated reads and replacement | ONE, ONE, TWO; `0 OK, 50:1` | [Screen](repeated-read.png) and result rows |
| Change only stored line 30 to PRINT m$ | ONE, then `2 Variable not found, 30:1`; source still contains the error | [Fault screen](stored-wrong-name.png) |
| Repair that line to PRINT n$ | ONE, ONE, TWO; successful completion | [Repaired screen](stored-repaired.png) |
| Enter immediate PRINT m$ through canvas key events | `2 Variable not found, 0:1`; earlier output remains | [Immediate error](wrong-name.png) |
| Correct immediate command to PRINT n$ | An additional TWO; `0 OK, 0:1` | Complete result rows in JSON |
| Enter RUN through canvas key events | Fresh ONE, ONE, TWO; `0 OK, 50:1` | [Recovered run](recovered-run.png) |
| Restart Spectrum | Fresh tape loader header, then the complete edited program output | Result rows; header requirement prevents a stale pre-restart transcript passing |
| Reset listing to original and run | Maintained source restored exactly; Hello, Jo / from the Spectrum; `0 OK, 20:1` | [Restored original](original-restored.png) |

All six linked screenshots were visually inspected. Canvas output agrees with the
transcript for the captured stages. A nonblank rendered text-region check and hash
also accompany the restored greeting. This is not an automated glyph-recognition
check or a screen-reader qualification. No page errors were recorded.

## Harness failures and what they mean

The original supplemental harness source was not retained in its audit or in the
tracked stored-value verifier. We can reproduce current observation hazards, not
replay that exact code or establish the old empty transcript's cause.

- The first sandboxed browser launch failed before a session, reporting
  `browserType.launch: Target page, context or browser has been closed` and
  `signal=SIGABRT`. The authorised browser run then launched successfully.
  This environment failure supplies no product outcome.
- [First browser attempt](attempt-header/browser-results.json) failed with
  `Repeated-read rows differ`. It had observed the correct output, but expected
  it at row zero. Tape loading leaves a `Program: greeting` header; the earlier
  native task had entered its program directly. The retained screenshot and raw
  rows show the difference. We changed the assertion to remove only the explicit
  loader header and leading blank rows before checking all three output lines.
- [Second browser attempt](attempt-run-display/browser-results.json) passed the
  reads and immediate repair, then reported
  `TimeoutError: page.waitForFunction: Timeout 60000ms exceeded.` It expected RUN
  to append to the previous display. The fresh RUN clears it. We replaced that
  offset assumption with a complete fresh three-line result requirement.
- [The six-stage run](initial-six-stage/browser-results.json) then passed. We
  retained it separately and added the original task sheet's stored-line-30 fault
  and single-line repair, giving the final eight-stage pass.

The final run also retains startup transcript changes. The first sample says
`The Spectrum has not started yet.`; an intermediate sample has the tape header
without the completed output. A reconstructed premature assertion rejects that
initial sample. The obsolete `.basic-transcript pre` selector finds no element
and returns an empty fallback string, while the current view is
`.machine-transcript pre`. These observations show why startup status or a missing
selector cannot qualify output; they do not establish which mistake caused the
historical failure.

A known-red requirement that collapses the repeated reads into only ONE/TWO is
rejected. The actual check requires three complete ordered rows and a completion
report, so an empty observation cannot pass. Restart additionally requires the
fresh loader header, which the preceding ordinary RUN has cleared.

## Verification and remaining limits

The website verifier is `scripts/verification/embedded-basic-values.mjs`. Run from
the website checkout, with installed Chrome and the existing project dependencies:

```sh
node scripts/verification/embedded-basic-values.mjs https://code198x.com /path/to/evidence
```

Syntax checking passes. Acorn reports **zero inserted semicolons**, matching the
verification-script convention. [Evidence validation](validation.json) checks eight
positive stages, exact output/error/repair states, the failed attempts, source and
verifier identities, screenshot hashes and local links. [Artefact hashes](artifacts.json)
retain the browser attempts and screenshots, including failures.

This is current desktop Chromium qualification of one task. **Skipped:** mobile
and touch input, Safari/WebKit, screen readers, contrast/accessibility sweep,
audio, download/reload, original hardware and latency measurement. No startup
performance conclusion follows from capturing transcript transitions. **Unknown:**
the discarded harness's exact historical cause, browser/native ROM equality and
actual learner understanding, independent completion, retention or transfer.

Website #747 can close when these bounded results are accepted. The umbrella
issues remain open. Next measure end-to-end startup/edit-to-result latency under
[website #748](https://github.com/code198x/website/issues/748), using actual machine
outcomes rather than the early status or transcript alone.
