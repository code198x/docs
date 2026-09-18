# Yearfall — teaching implementation

**Status:** Thirteen replacement lessons and eleven verified programs are ready
for local review. The accepted native game is unchanged. Publication awaits
lesson approval. The [lesson brief](lesson-brief.md) defines the progression.

## Maintained sources

`code-samples/sinclair-zx-spectrum/basic/yearfall/teaching/` owns the complete
sources, exact editing metadata, changed-line listings and reproducible checks.
The finished source is byte-identical to the accepted prototype at `03afc02`.

The stages are ledger, food, seed, harvest, editor, planner, years, trade,
visitors, continued and finished. The shortage lesson reuses trade; saving
reuses finished. Early stages deliberately stop or resolve only one year, and
the lessons explain those limits before introducing the next behaviour.

## Execution evidence

**140 execution check groups pass across eleven checkpoints**, including all
43 accepted-prototype groups against the independently entered finished tape.
Every complete checkpoint was entered using keyword keys in a fresh 48K PAL
ROM and saved with `SAVE "yearfall" LINE 10`. Execution checks load each tape in
a separate process. Exact editing transitions, literal branch targets,
unchanged token bytes, tape checksums, auto-start, source/evidence hashes and
final-source identity pass the audit.

The evidence manifest records executable identities. The local emulator was
built from Emu198x `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3` and reports 0.24.0.
Memory observations are read-only. Incomplete snapshots while the ROM updates
strings are retried for at most eight frames.

Food and seed experiments edit the stated BASIC lines through the ROM and
restore them afterwards. The worked shortage uses ordinary ROM LET commands
after quitting, then sets planting to 100 before selling seven acres and
planting 93. Its 189–468 forecast and subsequent food requirement are checked.
Deterministic multi-year diagnostics use `RANDOMIZE 17` and `RUN 200`; they
record setup separately from legal game input. No altered-state fixture
supplies a public image.

The website uses the original accepted-prototype planning and traveller
captures, visually inspected against their captions. The finished source is
identical. Native acceptance applies to the final game; intermediate execution
is not independent learner success or original-hardware timing. Thirty-year
continuation is observed, while the four-digit editor still limits very large
settlements. Saving the program does not save campaign state.

## Website integration and validation

Thirteen topic-named lessons replace the old six. They include exact editing
instructions, complete source, questions with explanations, keyboard guidance
and original manual chapter references. Yearfall appears beside The Caverns in
Hidden worlds in the local catalogue. Canonical and legacy old topic paths
redirect to the corresponding new lessons; numeric identities are preserved.
The What's New entry remains `draft: true`.

The production build passes: seven test files, 69 tests and nine existing skips,
followed by content validation, static generation and search indexing.
Forty-two desktop/mobile browser groups cover the overview and thirteen lessons,
local links, source includes, images, question disclosure keyboard operation,
overflow, six canonical topic redirects and course placement. Twelve light/dark
desktop/mobile accessibility checks cover the overview and two representative
lessons, with no axe violations. Rendered desktop lesson and mobile overview
captures were visually inspected. Compact browser evidence is retained in
`verification/lesson-browser.json` and `verification/lesson-accessibility.json`.

The local preview is at
<http://127.0.0.1:4335/systems/sinclair-zx-spectrum/basic/yearfall/>.
No publication or live-site claim is made.
