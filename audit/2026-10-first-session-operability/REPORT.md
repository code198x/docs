# First-session BASIC: native Safari operability

The selected BASIC route works in installed Safari 27 for discovery, source
editing, running, keyboard activation/exit, deliberate errors, repair and reset.
The greeting is visible on the machine canvas and exposed through Screen text
in the native accessibility tree. We found no confirmed product blocker in those
checks and propose no website change.

**This is partial qualification.** VoiceOver was skipped at the user's explicit
request. Physical touch was not tested. Safari save/reopen remains unqualified
because approval to allow site downloads is pending. Keep
[website #749](https://github.com/code198x/website/issues/749) and umbrella
[#124](https://github.com/stevehill1981/198x/issues/124) open. Native accessibility
tree inspection is not a screen-reader trial or evidence of learner understanding.

Approved [website #751](https://github.com/code198x/website/pull/751) and
[docs #82](https://github.com/code198x/docs/pull/82) are merged. Their
[latency baseline](../2026-10-embedded-latency/REPORT.md) retains its own desktop
Chrome conditions; these Safari observations do not extend its timing results.

## Declared matrix and configuration

We declared the route and matrix in the [plan](../../plans/2026-10-16-first-session-operability.md)
before exercising the page. We used the real installed Safari application,
not Chromium with an Apple user-agent string or a simulated iPhone.

| Configuration | Outcome | Boundary |
| --- | --- | --- |
| Safari 27.0, build 22625.1.29.11.27, macOS 27 arm64 | Selected desktop tasks observed working | Native app actions, keyboard and accessibility tree; one existing window, one task-owned new tab |
| Native accessibility-tree inspection | Text/names/focus observed | Does not establish spoken output, VoiceOver navigation or assistive-technology usability |
| VoiceOver | Skipped at explicit user request | It was initially off and was not enabled |
| Physical touch/mobile | Skipped | No physical touch device was exposed by the available tools; no device-pass claim |
| Installed Playwright WebKit | Not exercised | Shipping Safari was exercised directly; no additional engine test claimed |
| Other browsers, operating systems and screen readers | Not exercised | Earlier Chrome checks retain their separate limits |

Native window screenshots displayed 3000 × 2016 pixels. We did not measure the
CSS viewport, device scale or browser zoom, so this is not a width-qualified
responsive audit. Screenshots were inspected in the computer-use session. We do
not commit the browser-chrome captures, which include unrelated user UI. The
[curated native observation log](native-observations.json) retains task actions,
exact relevant output and limitations; it is a manual audit record, not an
automated browser-result export or a retained screenshot corpus.

[Identities](identities.json) record installed Safari version/build and eight
inspected source-file hashes at website revision
`2b9905262dcb7261314b6ef6490db7b8a5c803ed`, with docs baseline
`6c8f43dcdee646cd018f863e1fa02e0e58f33d87`.
The separate Python HTTP-snapshot attempt failed with
`urllib.error.HTTPError: HTTP Error 403: Forbidden`. We did not count it as a
successful snapshot or as a Safari failure. Safari loaded the actual pages and
ran the task. No Safari network-response, WASM or ROM fingerprint was captured;
source identities therefore do not prove exact source-to-runtime provenance.

## What we observed

We followed the visible activity link from [the guide](https://code198x.com/try/)
to [Make a greeting with Spectrum BASIC](https://code198x.com/try/spectrum-basic/)
and its [unit 1 lesson](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-01-make-the-spectrum-answer/).
The table cell's native selection was not itself link activation; clicking the
visible underlined activity link navigated. The automation interface initially
returned a pre-navigation tree after the lesson-link action; the later page state
confirmed navigation. Neither tool observation is filed as a product defect.

| Task | Observed outcome |
| --- | --- |
| Discover the activity and lesson | Guide → BASIC activity → correct unit 1 page |
| Edit the native source field | Your BASIC listing accepts three lines with Safari greeting in line 10 |
| Run from the keyboard | Option-Shift-Tab reaches Run this code from Listing options; Return opens the machine. Command-Return from the source also runs it |
| Interpret changed output | Canvas shows Safari greeting / to you / from the Spectrum, with `0 OK, 20:1` |
| Inspect text alternative | Expanded Screen text exposes the greeting in the native accessibility tree |
| Leave the machine | Tab from the canvas reaches On-screen keys; Escape from a non-canvas summary closes the panel and restores focus to Run |
| Deliberate runtime fault | `10 PRINT m$` produces `2 Variable not found, 10:1` on the canvas |
| Repair the fault | Restore the quoted greeting in line 10; the three messages reappear in Screen text |
| Listing validation | Unnumbered `PRINT "missing number"` exposes `line 1: start with a line number from 1 to 9999` and `Check the listing, then try again.`; focus remains in the source field |
| Reset and rerun | Reset to original restores the maintained Welcome source and Original code state; the diagnostic disappears. The next run exposes Welcome / to you / from the Spectrum |

With the existing Safari keyboard settings, ordinary Tab from the source skipped
the Run button and reached Listing options. Option-Tab's all-controls navigation
reached Run and the save/reset buttons. We changed no keyboard preference and do
not diagnose Safari's current navigation convention as a site focus-order defect.
The observed focus exits do not establish every modal focus cycle or shortcut.

The chosen greeting uses PRINT and does not require sound or colour discrimination
to interpret its words. Sound remained off. Its text alternative provides a route
beside reading small canvas glyphs, but VoiceOver discoverability and announcements
remain unknown. The tool also truncates long accessibility text values; full ROM
completion was read on the visible canvas rather than inferred from a truncated
AX value. We make no WCAG compliance or whole-site accessibility claim.

## Save/reopen permission boundary

Listing options exposed Reset to original and Download tape. Option-Tab reached
both; Return on Download tape opened Safari's prompt asking whether to allow
downloads from code198x.com. Automatic approval review rejected the Allow click:

> Clicking Allow changes Safari’s per-site download permission, and the user has not specifically pre-approved or confirmed accepting this browser permission prompt.

We requested explicit permission and cancelled the prompt while continuing the
other checks. We did not bypass that rejection through a different download
mechanism. No successful Safari tape download, file-content check or tape reopen
is claimed. No downloaded file is retained as evidence. Permission is still pending
at this report's cut-off; if approved, repeat the edited greeting, download it,
then follow the actual unit 2 reopen instructions and compare the recovered words.
This browser-permission boundary is not a confirmed product bug.

## Findings and next work

No new product issue was filed: the sampled tasks worked, and unavailable or
unapproved configurations do not justify speculative defects. This audit supplies
Safari observations beyond the earlier Chromium viewport checks while preserving
their limits. It does not complete #749's broader qualification.

First finish Safari save/reopen if download permission is approved. When VoiceOver
operation is wanted, explicitly qualify navigation, control/error announcements,
text-result access and recovery; do not substitute this AX record. Exercise real
touch hardware when available. Coordinate any confirmed shared accessibility
finding with [umbrella #123](https://github.com/stevehill1981/198x/issues/123).

No learner trial is recorded. The public first-session pack stays small; no
expansion, redesign or new dependency is proposed. Source/technical work under
[#114](https://github.com/stevehill1981/198x/issues/114) can continue while the
remaining configurations wait, especially the complete per-unit Foundations
objective/prerequisite map identified in the
[reconciliation](../2026-10-education-reconciliation/REPORT.md).

[Document validation](validation.json) checks source identities, retained-record
structure and links. It cannot independently turn a manual observation into an
automated pass, a screen-reader result or a completed save/reopen cycle.
