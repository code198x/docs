# The Caverns — teaching implementation

**Status:** Ten replacement lessons and eight verified programs are prepared
locally for review. The native prototype is accepted; publication is pending.
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
new lessons; numeric identities are preserved. The local BASIC listing places
The Caverns in a new Hidden worlds group after Quickstep. That grouping is part
of this review. The prepared What's New entry remains `draft: true`.

The production build passes: seven test files, 69 tests and nine existing skips,
followed by content validation, static generation and search indexing.
Thirty-six desktop/mobile browser groups cover all eleven pages, local links,
source includes, image loading, disclosure keyboard operation, page overflow,
six topic redirects and course placement. Twelve light/dark desktop/mobile
accessibility checks cover the overview and two representative lessons, with
no axe violations. Rendered desktop lesson and mobile overview captures were
visually inspected. Compact browser evidence is retained alongside this record.

Local preview: <http://127.0.0.1:4334/systems/sinclair-zx-spectrum/basic/the-caverns/>.
These lessons have not been published or announced.
