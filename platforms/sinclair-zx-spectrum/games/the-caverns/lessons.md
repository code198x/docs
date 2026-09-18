# The Caverns — teaching implementation

**Status:** Ten approved replacement lessons and eight verified programs are
published. Production and live checks pass. The native prototype is accepted.
The [lesson brief](lesson-brief.md) defines the progression.

## Maintained sources

`code-samples/sinclair-zx-spectrum/basic/the-caverns/teaching/` owns the sources,
exact editing metadata, changed-line listings and reproducible verification.
The finished source is byte-identical to the accepted prototype at `7c3fcfe`.

| Program | Execution focus |
|---|---|
| `room` | Named room, description and deliberate STOP |
| `map` | Twelve room records, four exits, DATA/READ and deliberate STOP |
| `walk` | All rooms, directions, held/invalid keys, walls, waiting and reset |
| `treasure` | One-time collection, directional glints and cleared clues |
| `pit` | Warning, entry loss, retained result and replay |
| `patrol` | Independent circuit, entry loss, arrival grace and repeated arrival |
| `expedition` | Three treasures plus entrance; win before creature update |
| `finished` | Title and all nineteen accepted-prototype check groups |

## Evidence

**97 execution check groups pass.** Each complete checkpoint was entered using
keyword keys in a fresh 48K PAL ROM and saved with `SAVE "caverns" LINE 10`.
Execution checks load the resulting tape in a separate process. Observation is
read-only, with no injected game states. Exact editing transitions, literal
targets, unchanged token bytes, tape checksums, auto-start, evidence hashes and
final-source identity pass the audit.

The evidence manifest records each executable identity. The local emulator was
built from Emu198x `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3` and reports 0.24.0.
One observation caught the ROM relocating its string-variable table during
INKEY$. Advancing one frame without input produced a complete state. The reader
now retries incomplete snapshots for at most eight frames; the original and
resolved observation are retained in `input-sampling.json`, with retry counts
in stage results. No game or emulator change was needed.

The website uses the original accepted-prototype arrival capture, whose source
matches the finished checkpoint. The worked trace escapes west; the lesson also
explains why north permits another creature arrival and another escape turn.
Native acceptance establishes play feedback, not original-hardware timing or
independent learner success.

## Website integration and validation

Ten topic-named lessons replace the old six. Each has exact editing instructions,
complete source, questions with explanations, relevant keyboard notes and
original manual chapter references. The overview uses the existing House
presentation. Old canonical and legacy topic URLs redirect to corresponding
new lessons; numeric identities are preserved. The approved BASIC listing places
The Caverns in a new Hidden worlds group after Quickstep. That grouping is approved. The prepared What's New entry remains `draft: true`.

The production build passes: seven test files, 69 tests and nine existing skips,
followed by content validation, static generation and search indexing.
Thirty-six desktop/mobile browser groups cover all eleven pages, local links,
source includes, image loading, disclosure keyboard operation, page overflow,
six topic redirects and course placement. Twelve light/dark desktop/mobile
accessibility checks cover the overview and two representative lessons, with
no axe violations. Rendered desktop lesson and mobile overview captures were
visually inspected. Compact browser evidence is retained alongside this record.

## Publication

Samples PR [20](https://github.com/code198x/code-samples/pull/20) is merged at
`80c3ee2`. Website PR [434](https://github.com/code198x/website/pull/434) is merged
at `0dbfc671`. Samples CI, website CI and code analysis pass. Pages deployment
[35327408943](https://github.com/code198x/website/actions/runs/35327408943)
succeeded. Twenty-five live HTTP checks cover the overview, all ten lessons,
six canonical and six legacy topic redirects, the current-course listing and
unchanged arrival image. Evidence is retained in `verification/lesson-live.json`.

The [published lessons](https://code198x.com/systems/sinclair-zx-spectrum/basic/the-caverns/)
are available in Hidden worlds. The release note remains a draft. All eighteen
unrelated local edits retain their pre-work contents or deletion state.
