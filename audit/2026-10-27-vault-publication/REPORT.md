# Twenty-eight Vault entries: approval and publication

All twenty-eight approved Vault entries are published and have passed live checks. The owner approved the earlier nineteen entries, then explicitly approved the nine new system entries on 27 October 2026. Their work was consolidated into website PR1262 and docs PR269 to share one publication run. Subsidiary website PR1292 and docs PR270 retain the separate nine-entry authoring history.

Website merge: `7bbe11303b16707c61af6653dc6d9cd4d0ca531f`. Live verification: 2026-10-27T15:06:51.261Z.

The [live results](live-results.json) positively verify all twenty-eight reviewed, indexable canonical pages and their sitemap entries; 301 public pages and 480 authored incoming/outgoing link edges; and 12 image checksums against the approved source. There are no failed checks. Verification used a normal Chromium browser because the command-line client receives Cloudflare1010; no security setting was changed.

[Candidate/path identities](candidate-paths.json) map the twenty-eight retained stable IDs to the actual published articles. Every published status in this update follows the positive live checks, rather than approval, a green build or absence from a scan. All twenty-eight writing issues can now be completed.

The nine new articles are Commodore 128, SX-64, CDTV, Atari 5200, Atari 7800, Jaguar, Falcon030, Acorn Electron and TI-99/4A. Spectrum 128 is covered by the existing model-history and hardware-port entries, with useful section links. No duplicate article or public stub was created. The new articles add 62 useful incoming links across 56 existing articles and three original explanatory diagrams.

Research, original documentation, period corroboration, source discrepancies, image provenance and authoring screenshots remain in the website's [combined evidence report](https://github.com/code198x/website/blob/main/docs/reviews/2026-10-27-approved-vault-publication/REPORT.md) and its three linked research reports. Article bodies, source citations and images were unchanged after owner approval; only reviewed flags changed. Earlier reports' unreviewed-state observations describe the authoring stage.

The new-system work retains twenty-one uncommissioned follow-ups VC-3057–VC-3077 and reuses five existing identities (TIA, TMS9918, Commodore 1571/1581, ANTIC/GTIA and BBC BASIC). Exact names and nearby identities are distinguished; candidates remain needs-triage until their scope and coverage are assessed. No writing issues were opened for those follow-ups.

Backlog after publication: 3,077 retained records, comprising 46 published, eight covered, one ready and 3,022 needing triage. There are no remaining in-progress records from these batches. The existing CSV fields and planned-candidate conventions are unchanged.

Verification: all records and website references validate; nineteen regression tests pass. Website checks pass (220 tests, the same 73 accepted baseline type errors and no new ones), production build and page-frame checks pass, and all eighteen post-approval narrow/desktop views and nine live Pixel 7 device-emulation views of the new entries pass article accessibility, image, runtime and overflow checks. [Live mobile results](live-mobile-results.json) include the mobile viewport, device pixel ratio and touch input; [remote-main source results](main-source-results.json) confirm all twenty-eight approved article files match main exactly. Deliberate missing-link rejection confirms that validation can fail. The existing unrelated Diablo 1996/1997 and Louis Castle 1965/1964 date disagreements and the emulator-template Pagefind warning remain documented rather than claimed as passing.

## Mobile audit execution note

The first public mobile accessibility attempt ended with:

```text
frame.evaluate: Error: No elements found for include in page Context
```

That attempt did not record which response or frame caused the error. A diagnostic rerun kept the same Pixel 7 profile, main-element inclusion and WCAG A/AA tags, and recorded every page separately. All nine returned HTTP200 with exactly one main element and no accessibility violations, overflow, page exceptions or image-loading failure. [Per-page log](live-mobile-log.txt) and [results](live-mobile-results.json) retain that evidence. No production code or security setting changed; the initial cause was not established and is not reported as a website defect.
