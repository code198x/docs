# Three in a Row — teaching implementation

**Status:** The user-approved overview and ten replacement lessons are published, supported by eight verified programs. Production and live checks pass. The [lesson brief](lesson-brief.md) defines the progression.

## Maintained sources

`code-samples/sinclair-zx-spectrum/basic/three-in-a-row/teaching/` owns the checkpoints, exact editing metadata, ordinary changed-line listings and reproducible verification scripts. The final source is byte-identical to the accepted prototype at samples commit `46ca3c6`.

| Program | Execution focus |
|---|---|
| `board` | Fresh tape, zeroed array, numbered grid and deliberate STOP |
| `place` | Invalid/occupied/held input, nine crosses, reset and quit |
| `turns` | Alternating X/O, full-board stop, stable final state |
| `results` | Early win, draw, all eight lines for both marks, last-cell win before draw |
| `reply` | First-empty choices, truthful reasons and no O move after a human win |
| `tactics` | Block and win paths; legal 1/3/7/6 trace and separate win-before-block fixture |
| `policy` | Accepted positional preferences, fork win, centre opening and corner response |
| `finished` | Complete prototype suite against an independently entered tape |

## Evidence

**101 execution check groups pass.** Every program was entered in a fresh 48K PAL ROM with keyword keys, saved through `SAVE "three" LINE 10`, then loaded in a separate process. The final program passes all forty prototype check groups, including both starters, session tally, reset/replay, ignored/held input, reasons, wins, draws and every quit route.

`verification/audit.py` confirms exact source reconstruction from stated edits, literal targets, identical token bytes for unchanged lines, tape block checksums, auto-start line 10, source/evidence hashes and final-source identity. `verification/evidence/manifest.json` records the configuration and executable identity for each checkpoint. The local executable is built from Emu198x commit `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3` and reports 0.24.0.

Memory observation is read-only. Winning-line and priority fixtures are explicitly entered as ordinary ROM DIM/LET commands after STOP; they are separate from normal play and do not supply public captures. The website's fork image is an unchanged original prototype capture whose source matches the finished checkpoint. Its caption describes O's completed block and the remaining X win.

Native feedback accepted the final game's feel and reported mostly draws. It does not establish a measured draw rate, perfect strategy, original-hardware timing or independent learner success.

## Website integration

The overview uses the existing House presentation. Ten topic-named lessons replace the older six, with exact add/replace/delete instructions, full source checkpoints, questions with explanations, keyboard notes and original manual chapter citations. Old canonical and legacy URLs redirect to corresponding topics. Numeric catalogue and lesson identities are preserved. Three in a Row joins Boards and deduction after Locksmith; the BASIC landing description includes opponent decisions. System and assembly entry pages remain accurate and need no content change.

A What's New entry is prepared with `draft: true`; it is not announced. The fork supplies a concrete lesson example without requiring a separate essay. The user approved the rendered lessons and authorised publication.

## Site validation

The production build passes: seven test files, 69 tests passed and nine existing
skips, followed by content checks, static generation and search indexing.
Thirty-six desktop/mobile browser groups check the overview, all ten lessons,
local links, code includes, image loading, disclosure keyboard operation,
no page overflow, six topic redirects and current-course placement. Twelve
additional desktop/mobile light/dark accessibility checks cover the overview,
first coding lesson and fork lesson, with no axe violations. Original emulator
captures and rendered overview/lesson screenshots were inspected.

Samples were developed at `adf0af6` (checkpoint sources and evidence in
`09391c5`, retained ROM-saved tapes in `adf0af6`). The final accepted source is
unchanged. All eighteen unrelated local edits were checked against the retained
baseline and are unchanged.

## Publication

Samples PR [19](https://github.com/code198x/code-samples/pull/19) is merged at
`23906e8`. Website PR [433](https://github.com/code198x/website/pull/433) is
merged at `ea56fbed`. Pages deployment
[35322776090](https://github.com/code198x/website/actions/runs/35322776090)
succeeded. Nineteen live HTTP checks cover the overview, all ten lessons, six
topic redirects, current-course listing and unchanged fork image. The release
note remains a draft; no separate community announcement was requested.
