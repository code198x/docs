# Numbers and representation: fourth bounded pilot

Two Foundations explanations need correction: Counting in Twos unit 3 equates
address space with installed memory, and unit 4 conflates carry with signed
overflow. The proposed pages distinguish maximum from count, address range from
RAM fitted, full arithmetic from a stored low byte, and carry from signed overflow.
[Website #701](https://github.com/code198x/website/issues/701) and
[#702](https://github.com/code198x/website/issues/702) track the findings.

This is a review snapshot, not a publication claim. No learner is available.
The separate [learner prompts](LEARNER-TASKS.md) and [assessor notes](ASSESSOR.md)
prepare a trial; educational effectiveness and unaided transfer remain unverified.
Umbrella #114, #115 and #124 remain open.

## Scope and sources

The [plan](../../plans/2026-10-15-numbers-pilot.md) records baselines and scope.
Website baseline `eff31273bd5c9551264b2a884d9d4825ce0d161b`, docs baseline
`c0065db03fe05e683ecd7df807218c7ebde74250`; samples remain
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. Isolated worktrees excluded
unrelated edits. Existing installed packages and the pinned UI kit were copied;
no dependency was added or installed.

Zilog's *Z80 CPU User Manual*, UM008011-0816, pp.66–67, explains carry and signed
overflow independently; p.147 specifies both flags for ADD A,n. The Amstrad
*ZX Spectrum +3 User Manual*, p.182, distinguishes 65536 addressable bytes from
128K RAM and 64K ROM, selected through paging. These are source checks, not a
paging implementation test. No new hardware source acquisition was needed.

Before filing, all-state website issue searches for address space, carry,
overflow and 65536 found no matching finding. Earlier pilots remain separate.
The approved repetition pair (#700 and docs #60) was merged and live-verified;
its publication evidence is retained in the #700 and #699 comments.

## Prerequisites and transfer boundaries

| Surface | Local explanation and dependencies | Boundary |
| --- | --- | --- |
| Counting in Twos units 1–2 | Binary place values and hex, used by units 3–4 | These earlier shared units support the chosen Foundations entry, not mandatory attendance for system tracks. |
| Unit 3 | High/low byte calculation and sixteen-bit patterns | 65535 is an unsigned maximum; 65536 is the count. A byte-addressed 16-bit space selects 64K at once, not necessarily 64K RAM. Banking is introduced only to explain the distinction. |
| Unit 4 | Signed interpretation, negative patterns, low-byte addition | SHOW gives the full sum. One-byte storage is an explicit additional assumption. Carry differs from signed overflow. |
| Spectrum BASIC Meet BASIC unit 5 | Numeric variables, input and conditions; keyboard guidance and complete listings | Numeric variables are not inherently one byte. The audit uses tiny direct commands rather than changing the game. |
| Spectrum assembly Meet Assembly unit 2 | Complete source, bits, define-byte directive, register, bitmap and attribute | Bits become pixels through their use; no BASIC prerequisite. Optional link is an invitation to explore, not a claim the full assembly lesson has no local prerequisites. |
| Assembly unit 4 / unit 8 | Pointer pairs and debugger flags, built on earlier assembly work | Read for context. This slice does not qualify every instruction or the full debugger workflow. |

The learner pack covers prediction, explanation, modification, fault diagnosis and
creation. No learner answers, completion times or comprehension scores are invented.

## Results

| Check | Outcome | Evidence and limits |
| --- | --- | --- |
| Existing explanations | Failed conceptual review | Original live text appears at both widths in [baseline](browser-baseline.json). Sources distinguish the concepts the text conflates. |
| Spectrum BASIC arithmetic | Passed two cases | [Native results](native-numbers.json): actual ROM keyboard LET/PRINT stores 256 and 65536, verifies complete output and normal completion. |
| Z80 fixed-width addition | Passed three cases | The [fixture](byte-sums.asm) is assembled and tape-loaded. Loaded bytes must match the fresh binary. Actual A/F results agree with independently calculated unsigned sums and signed ranges: 255+1 → 0/C1/PV0; 127+1 → 128/C0/PV1; 5+251 → 0/C1/PV0. No memory-write injection supplies these results. |
| Existing live byte-and-pixels experiment | Passed five groups | Prediction mismatch/match and actual display crop; purposeful editing and colour restoration; second write replaces first; download/revert; narrow layout and keyboard/forced-colours control. This qualifies the linked technical route, not unaided discovery. |
| Production build and repository checks | Passed | 2451 pages built, frame validation and search index completed; 31 test files, 218 passed tests, nine existing skips; content/link and prepared tooling checks passed. Skips are not passes. Pagefind's existing Default UI advisory does not invalidate the build. |
| Proposed pages | Passed four page/viewport checks | [After](browser-after.json): HTTP 200, no page overflow and no scoped automated WCAG A/AA violations at 1440×900 and 390×900. Four closed predictions open by keyboard; optional assembly link and browser Back pass at both widths. Axe incompletes are recorded, not counted as passes. |
| Known-red control | Expected rejection | [Result](known-red-control.json): corrected-state verifier rejects the unchanged page with `Error: Original representation claim remains`. |
| Prose/design/Python/patch checks | Passed | Changed lessons: Vale zero errors/warnings/suggestions; design detector `[]`; Ruff and patch whitespace checks pass. |
| Real learners, original hardware, physical mobile, other browsers and screen readers | Pending or untested | Desktop Chrome viewport checks and one configured emulator cannot establish these. No pseudocode interpreter was introduced. |

Chrome 155.0.8059.40, Playwright 1.62.1 and axe 4.13.0 were used on macOS.
Native evidence records emulator/assembler/driver/fixture/ROM hashes. The tool
observations are configuration-specific; source evidence supplies the architectural
claims. Both revised pages at both widths were visually inspected. Existing page
composition is preserved; no shared layout or design system was changed.

## Reproduce

With the website's existing prepared assets and tooling:

```sh
node scripts/verification/numbers-pilot.mjs https://code198x.com /tmp/numbers-before baseline
node scripts/verification/byte-pixels.mjs https://code198x.com /tmp/numbers-pixels
npm run build
npm run check
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2000 --ignore-lock
```

In another terminal, run the proposed-state verifier against that preview:

```sh
node scripts/verification/numbers-pilot.mjs http://127.0.0.1:2000 /tmp/numbers-after after
```

From docs, using the maintained samples driver and configured native tools:

```sh
python3 audit/2026-10-numbers-pilot/verify-numbers.py --samples ../code-samples --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x --output /tmp/numbers-native
```

[Evidence hashes](evidence-sha256.json) cover retained observations and captures.
The known-red result is historical after publication. Review the bounded correction
and packs, then run the learner protocol when someone is available. Broader
curriculum coverage and the integrated journey still need evidence.
