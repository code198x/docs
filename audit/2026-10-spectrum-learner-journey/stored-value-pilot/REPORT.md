# Stored-value pilot: first evidence pass

The selected material supports a concrete read/replace pilot across Foundations,
Spectrum BASIC and Spectrum assembly. One conceptual error is confirmed:
Foundations says output makes a computer forget a value. The proposed correction
removes that claim in both affected lessons and asks readers to predict repeated
reads and replacement before revealing a trace. The correction is prepared for
editorial review, not published. [Website PR #694](https://github.com/code198x/website/pull/694)
contains the correction and bounded verifier at commit `080d205ea`.

No learner is currently available, as confirmed by the owner. The trial pack is
ready for review; educational effectiveness remains unknown. Keep umbrella
[#114](https://github.com/stevehill1981/198x/issues/114),
[#115](https://github.com/stevehill1981/198x/issues/115) and
[#124](https://github.com/stevehill1981/198x/issues/124) open.

## Scope and identities

Checked on 15 October 2026. The website source baseline is
`290146661779c23562c089adf61b71ee50d693d4`; samples are
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. The latest successful deployment
reported by GitHub during this pass was
[run 38583068042](https://github.com/code198x/website/actions/runs/38583068042)
at the same website source commit. That is deployment provenance, not proof that
every live response comes from those bytes. Live pages were inspected separately.

Browser checks used headless Chrome `155.0.8059.40`, Playwright `1.62.1`, axe
`4.13.0`, macOS `27.0`, and 1440×900 and 390×900 CSS-pixel viewports. The maintained
byte experiment verifier used 1280×1000 and 390×844. These are desktop-browser
viewports, not physical mobile devices. Local after evidence uses the production
build served at `http://127.0.0.1:1994`, with the proposed changes to Foundations
Basics units 3–4 on the baseline above. The PR diff identifies the changed source.

Installed website packages: Astro `7.2.9`, `@asm198x/z80` `0.3.0` and
`@emu198x/zx-spectrum` `0.4.3`. These identify the local build; no browser-package
version is inferred solely from the live site's source revision.

Native checks used Emu198x Spectrum `0.32.5`, stock 48K PAL configuration, and
Asm198x `0.0.64`. The installed comparator identified itself as **PasmoNext
0.1.3**, not upstream Pasmo. The two assemblers produced equal program bytes and
both fresh tapes executed, but this is not an upstream-Pasmo compatibility result.
[Native assembly evidence](native-assembly.json) records binary and source hashes.
The [configured native ROM fingerprint](native-firmware.json) was read from a
fresh emulated machine; no firmware bytes are retained here. Browser ROM identity
was not captured, so native and browser firmware equality is unknown.

## What passed, failed and remains unknown

| Check | Outcome | Evidence and limits |
| --- | --- | --- |
| Selected objective/prerequisite map | Passed source inspection | [Map](PREREQUISITES.md). Shared read/replace reasoning exists; the three storage models remain distinct. |
| Foundations' original retention explanation | Failed | [Website #689](https://github.com/code198x/website/issues/689); unit 3 transition and unit 4 opening conflict with retained-variable examples. Live baseline confirms the unit 4 wording at both widths. |
| Direct page reachability and layout | Passed for selected routes | [Baseline](browser-baseline.json): 14 URLs at two widths, all HTTP 200, no document-width overflow. These were direct loads, not uncoached discovery trials. |
| Foundations → BASIC link by keyboard | Passed | Focused and activated the actual lesson link with Enter; destination matched. This does not establish the whole route's keyboard usability. |
| Automated accessibility of selected main content | Passed within tested scope | Six baseline analyses: Foundations unit 4, BASIC lesson 2 and assembly lesson 2 at two widths, zero reported WCAG A/AA violations. Incomplete automated rules are recorded, not treated as passes. Dialog states and screen readers were not qualified. |
| Native BASIC opening | Passed 16 named checks | [Results](native-basic.json): ROM keyboard entry, changing the stored name, wrong-name report, save/export and fresh-process load/run/edit. Native GUI interaction was not tested. |
| Native repeated reads and replacement | Passed two checks | [Results](native-repeated-read.json): complete listing produces `ONE`, `ONE`, `TWO`; wrong `m$` name reports `Variable not found`. The earlier output remains visible. |
| Native one-byte program | Passed both configured tool routes | [Results](native-assembly.json): equal 18-byte code, fresh tape loads, code bytes, bitmap and attribute checks. Comparator limitation above applies. |
| Maintained live byte experiment | Passed five groups | [Results](live-byte-checks.json): predictions versus actual RAM/screen crop, source-edit versus running state, separate attributes, replacement write, exact edited download/revert, narrow layout, keyboard toggle and forced-colour state. |
| Supplemental custom BASIC browser assertion | Failed harness; product outcome unknown | [Failure](supplemental-browser-failure.json). Final error: `Error: Repeated-read result: `, with an empty sampled transcript. Earlier setup/obsolete-selector errors are retained. This path was removed rather than counted as a pass or used to diagnose a product defect. |
| Proposed Foundations correction | Passed build/render checks | [After results](browser-after.json): both corrected pages at both widths; no old unit 4 claim, two automated main-content accessibility analyses with zero reported violations, closed prediction answer, Enter opens correct three output lines and five trace rows. |
| Prose and mechanical design checks | Passed | Vale: `0 errors, 0 warnings and 0 suggestions in 2 files`; Impeccable detector: `[]`; `git diff --check` clean. |
| Production build | Passed | Astro completed; shared frame verified on 2,451 public pages; Pagefind indexed 2,453 pages. Vite emitted its chunk-size warning; Pagefind emitted its existing Default UI notice. No dependency was added or changed. |
| Actual learner tasks and before/after comprehension | Pending | [Prompts](LEARNER-TASKS.md) and [assessor notes](ASSESSOR.md) prepared; no learner responses collected. |
| Physical mobile, touch typing, Safari, Windows/Linux browsers, screen readers, audible output and original hardware | Skipped | Not exercised in this pass. Do not generalise Chrome viewport/native emulator evidence to these environments. |
| Embedded startup latency | Unknown | No valid startup latency measurement retained. The supplemental BASIC harness cannot supply one. |

The new website verifier, `scripts/verification/stored-value-pilot.mjs`, preserves
the bounded page/accessibility and Foundations after checks. It fails on HTTP
errors, document overflow, automated violations, missing/incorrect trace content
or broken keyboard disclosure. The discarded supplemental BASIC path is not
included in this verifier's passing result.

## First prioritised finding and bounded improvement

**#689: output does not consume a stored value.** Replace the two false
transitions, state that a read leaves the value available, then extend the worked
trace with a second read before assignment. Put the output and trace behind a
native disclosure so the reader can predict first. Explain that replacing the
variable does not rewrite earlier output. No new component, dependency, storage
model or compulsory route is introduced.

Compare the [live before page at 390px](before-foundations-390.png),
[built after page at 390px](after-foundations-390.png) and
[opened five-step trace](after-revealed-trace.png). Desktop after composition,
the narrow trace and the maintained byte experiment's narrow capture were also
visually inspected. This establishes the changed presentation and explicit
conceptual model; improved comprehension remains a hypothesis for the trial.

No additional product defect is established by this bounded sample. The assembly
lesson has no direct Foundations/Vault link in its main content; that is a
source/navigation observation, not proof that a compulsory extra link would help.
The existing optional BASIC ↔ Foundations connection works. The Vault article's
storage detail is useful optional depth, not a suitable beginner prerequisite.
The trial pack supplies that optional connection for evaluation without
commissioning a new public sequence.

## Reproduce and continue

From the website checkout, with existing dependencies and Chrome installed:

```sh
node scripts/verification/stored-value-pilot.mjs https://code198x.com /tmp/stored-value-baseline baseline
node scripts/verification/byte-pixels.mjs https://code198x.com /tmp/stored-value-byte
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 1994 --ignore-lock
```

In another terminal, check that exact built preview:

```sh
node scripts/verification/stored-value-pilot.mjs http://127.0.0.1:1994 /tmp/stored-value-after after
```

For native execution, use the existing BASIC opening and Meet Assembly opening
README recipes, selecting `one-byte.asm` for assembly and recording the actual
comparator identity. For the additional repeated-read task, enter the five-line
listing retained in `native-repeated-read.json` through the ROM editor and run;
then replace line 30 with `30 PRINT m$` and run again. The expected full-screen
observations and driver hash are retained. [Evidence hashes](evidence-sha256.json)
cover the retained JSON and screenshots.

The next bounded step is editorial review of the correction and trial prompts.
After acceptance/publication, run a fresh learner trial when one is available,
using the independent entry protocol. Until then the engineering/editorial
preparation can advance, but no issue should claim educational validation. The
rest of Foundations and broader browser coverage remain outside this slice.
