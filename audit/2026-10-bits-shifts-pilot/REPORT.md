# Bits and shifts: fifth bounded pilot

Working the Bits units 1–2 need explicit operation contracts. Unit 1 calls all
four operations binary even though BITNOT takes one input; its complement example
also refers back to a different XOR mask. Unit 2 leaves right-shift fill and signed
interpretation implicit and promises universally fastest scaling. Correct those
claims while preserving the valid tables and examples.

[Website #704](https://github.com/code198x/website/issues/704) and
[#705](https://github.com/code198x/website/issues/705) track the findings. The
proposed pages add closed predictions and an optional existing assembly connection.
They are prepared for review, not published. No learner is available: the separate
[learner tasks](LEARNER-TASKS.md) and [assessor notes](ASSESSOR.md) prepare a trial,
but do not establish educational effectiveness. Umbrella #114/#115/#124 remain open.

## Scope and identities

The [plan](../../plans/2026-10-15-bits-shifts-pilot.md) records the bounded scope.
Website baseline `1a419f5806eb73e522dc4ccd8628824c2ff76e5c`; docs baseline
`e053dc3082864d130ded437a39f1fc6e967db753`; samples
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. Isolated worktrees excluded unrelated
shared-checkout changes. Existing installed packages and pinned UI kit were copied;
no dependency was added or installed. Floating-point and fixed-point are outside
this slice. The agreed period 64K wording from the preceding pilot is unchanged.

Chrome 155.0.8059.40, Playwright 1.62.1 and axe 4.13.0 checked desktop viewports
1440×900 and 390×900 on macOS. These are not physical-device observations. Native
Emu198x Spectrum 0.32.5 used configured 48K ROM entry and a freshly loaded tape.
[Native evidence](native-bits.json) records emulator, assembler, ROM, maintained
driver, generated fixture, code and tape hashes. Ruff checked the Python audit driver.

## Sources and prerequisite map

Zilog's *Z80 CPU User Manual*, UM008011-0816, AND/OR/XOR/CPL entries establish
bitwise operations. SLA pp.230–231 copies old bit 7 to carry and shifts in zero;
SRL pp.236–237 shifts in zero and copies old bit 0 to carry; SRA pp.233–234 preserves
old bit 7. ADD A,r p.145 takes four T-states, including ADD A,A; SLA r takes eight.
These timings are manual evidence, not a measured emulator or browser benchmark.
The Amstrad *ZX Spectrum +3 User Manual*, Conditions pp.99–101, states BASIC's
conditional numeric AND/OR/NOT rules. Actual 48K ROM checks independently agree
with the selected numeric expressions; do not infer identical semantics in every dialect.

All-state website searches for shift, fastest, mask and BITNOT and umbrella shift
searches found no matching findings. Existing keyboard/accessibility work was not
duplicated. No new hardware source acquisition was needed.

| Surface | Knowledge explained or used | Transfer boundary |
| --- | --- | --- |
| Foundations Counting in Twos | Binary/hex place values and signed versus unsigned readings | Supports the shared entry; not mandatory attendance for BASIC or assembly. |
| Foundations Decisions | Question-joining AND/OR/NOT | The taught Boolean notation does not establish a real language's numeric operator semantics. |
| Working the Bits unit 1 | Bitwise truth tables, keeping/setting/flipping, width-dependent complement | Three operations pair inputs; BITNOT takes one. Preserve unrelated bits according to the particular mask operation. |
| Working the Bits unit 2 | Eight-bit unsigned zero-fill model, left truncation and right remainder | Signed arithmetic right shift is different; a byte result and saved carry are separate. Left scaling matches multiplication only while it fits. |
| Spectrum BASIC conditions | Numeric comparisons and conditional expressions | Native PRINT checks exercise AND/OR/NOT, not invented BITAND syntax. BASIC arithmetic produces 400 for 200*2 and 2.5 for 5/2. |
| Meet Assembly unit 2 | Complete source, bit/pixel mapping, register and screen memory | Optional destination explains its starting program locally, requires no BASIC. The trial pack supplies and explains the inserted AND instruction. |
| The register is the bitfield | Existing From the Metal port-mask example | Read as a possible deeper connection, not execution-qualified here. It is not added as a compulsory beginner route. |

The native audit fixture is test tooling, not a new public lesson sample. Existing
public runnable samples and page architecture are preserved.

## Observations and proposed correction

The numeric bitwise examples and truth tables inspected in unit 1 are correct.
The defect is in the general operand description and the complement's reference
to an earlier mask. Clarify those and illustrate the concrete BASIC/Z80 difference.

For shifts, specify width, unsigned reading and incoming zero before using the
operators. Show 200 shifted left into a byte as 144, distinguish zero-fill and
sign-preserving right shifts for the same 10000000 input, and retain shifted-out
bits in Z80 carry rather than describing them as necessarily lost. Replace the
universal speed claim with a sourced instruction-dependent comparison. The shared
notation remains explanatory pseudocode; no interpreter was introduced.

## Results

| Check | Outcome | Evidence and limits |
| --- | --- | --- |
| Existing wording | Failed conceptual review | [Live baseline](browser-baseline.json) captures both old claims at both widths. Sources and the shared pseudocode grammar supply the conflicting contracts. |
| ROM BASIC expressions | Passed nine cases | [Native results](native-bits.json): AND/OR/NOT zero and nonzero cases, 5*2, 5/2 and 200*2. Complete output and normal completion checked; real keyboard tokens, no injected source or results. |
| Z80 masks/complement | Passed ten cases | AND/OR/XOR at representative masks including 0/255, XOR twice, and CPL. Expected results are computed independently; unaffected bits are asserted separately. |
| Z80 shifts/doubling | Passed twenty cases | SLA/SRL/SRA at 0, 1, 5, 128, 200 and 255, plus ADD A,A at 5/200. Actual result/carry agree with independent arithmetic/range expectations. The 272 loaded code bytes must match the newly assembled binary; memory reads validate every chunk length. |
| Instruction comparison | Source checked; result bytes observed | SLA and ADD both produce 10 for 5 and 144 for 200; recorded F bytes differ. Four/eight T-state claims come from the manual, not a timing measurement. |
| Production and repository checks | Passed | 2451 pages built; shared frame verified on 2451 pages; search indexed 2453. 31 test files, 218 tests passed and nine existing skips. Link/content/prepared-tooling checks passed. Pagefind retains its Default UI advisory. |
| Both proposed pages | Passed four page/viewport checks | [After](browser-after.json): HTTP 200, no document overflow or scoped automated WCAG A/AA violations. Four closed predictions open by keyboard. Axe reports one incomplete colour-contrast check on narrow unit 1; this is not a contrast pass. |
| Optional actual mask transfer | Passed at both widths | Keyboard link, source edit, assemble/run: 202 AND 15 produces actual bitmap byte 10. The sampled real screen crop matches all eight expected ink/paper pixels and alpha. Browser Back returns to the shared lesson; saved draft restore/revert also passes. Nine behaviour groups overall. |
| First transfer harness | Failed; retained | [Initial failure](browser-readonly-failure.json) and [stage retry](browser-stage-retry-failure.json): `locator.fill: Timeout 20000ms exceeded.` The second visit's textarea was readonly. Desktop editing had saved a draft; the narrow visit correctly required a recovery choice. |
| Harness diagnosis | Corrected after an unsuccessful assumption | Selecting the stage was first assumed to unlock editing; source inspection disproved that. `assembly-draft.ts` locks when a saved draft exists. The final check uses visible Restore and Revert controls, verifies both outcomes, and then edits. No product guard was disabled. |
| Maintained live byte/pixels verifier | Passed five groups | [Results](live-byte-pixels.json): prediction/display agreement, edits/stale-result labels/colours, replacement write, download/revert, narrow keyboard and forced-colours checks. |
| Known-red controls | Expected rejection of each old lesson | [Unit 1](known-red-unit-01.json) and [unit 2](known-red-unit-02.json): `Original bits/shift claim remains in unit 01` / `02`. Separate nonzero exits prove neither old page passes the corrected-state verifier. |
| Prose/design/Python/patch checks | Passed | Changed lessons and learner/assessor packs: Vale zero errors/warnings/suggestions. Design detector `[]`; Ruff and whitespace checks pass. Initial Python import spacing was corrected before final lint. |
| Actual learner outcomes, physical devices, screen readers, other browsers, original hardware and latency | Pending or untested | Neither technical correctness nor scripted navigation establishes unaided understanding, discovery or performance. |

Both revised pages at both widths were visually inspected using their rendered
captures. The established reading layout is preserved; no shared layout or visual
identity changes. The scoped checks do not amount to a full accessibility audit.

## Reproduce and next step

From the website with its existing prepared tooling and assets:

```sh
node scripts/verification/bits-shifts-pilot.mjs https://code198x.com /tmp/bits-before baseline
node scripts/verification/byte-pixels.mjs https://code198x.com /tmp/bits-pixels
npm run build
npm run check
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --host 127.0.0.1 --port 2001 --ignore-lock
```

In another terminal:

```sh
node scripts/verification/bits-shifts-pilot.mjs http://127.0.0.1:2001 /tmp/bits-after after
```

From docs, using the configured native tools and maintained samples driver:

```sh
python3 audit/2026-10-bits-shifts-pilot/verify-bits.py --samples ../code-samples --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x --output /tmp/bits-native
```

The audit script regenerates the retained [assembly fixture](bits-shifts.asm).
[Evidence hashes](evidence-sha256.json) cover retained observations, source and captures.
The old-page controls are historical after publication. Next: review the bounded
corrections and pack, then run the independent learner trial when someone is
available. Wider logic, fractional arithmetic and integrated journey outcomes
remain outside the completed evidence.
