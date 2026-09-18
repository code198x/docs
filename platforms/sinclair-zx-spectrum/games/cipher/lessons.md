# Cipher — teaching implementation

**Status:** Six approved replacement lessons and five verified programs are
published. Production and live checks pass. The [lesson brief](lesson-brief.md)
defines the progression. The finished game is unchanged.

## Maintained sources and scope

`code-samples/sinclair-zx-spectrum/basic/cipher/teaching/` owns complete sources,
exact editing metadata, changed-line listings and reproducible verification.
The finished checkpoint is byte-identical to the prototype. Its SHA-256 is
`bce89bd8bda7895b563a581c2035bb3a1ecd7b638afef93a8e29523fd275f41d`.

The stages are reveal, guess, rules, board and finished. The final saving lesson
reuses finished. The first program deliberately stops after a fixed T guess in
BOTTLE. The next allows unlimited guesses and Enter to quit. Rules and board
retain BOTTLE for repeatable checks before finished introduces the word list.
Each temporary limit is stated in its lesson.

## Execution evidence

**57 execution groups pass across five checkpoints**, including all seventeen
prototype groups against the independently entered finished tape. The final
suite also completes all 24 authored words through labelled ROM-command fixtures.
Each checkpoint was entered using keyword keys in a fresh 48K PAL ROM and saved
with `SAVE "cipher" LINE 10`; execution loads that tape in another process.

The source audit reconstructs every editing transition and checks literal
targets, unchanged token bytes, TAP checksums, auto-start, source/evidence hashes
and final-source identity. The evidence records the executable SHA-256 and
server identity. The local emulator reports 0.24.0 and was built from Emu198x
`e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3`.

Memory observations are read-only. The reveal lesson's L/Z experiments edit the
stated line through ROM entry, then restore T. All-word coverage selects entries
using explicit ROM commands after quitting; ordinary play supplies the captures.
Intermediate execution establishes the observed rules in this emulator, not
independent learner success or original-hardware timing.

## Website integration and validation

The overview and six topic-named lessons replace the earlier six. They provide
local explanations, exact editing actions, complete source, questions with
reasoning, keyboard notes and original manual chapter references. The published
catalogue places Cipher in Boards and deduction, preserving numeric identities.
Six canonical and six legacy topic paths redirect by subject. The system and
assembly landing pages contain no conflicting Cipher-specific claims; the BASIC
group description now includes word guesses. The release note remains a draft.

Production passes with seven test files, 69 tests and nine existing skips,
followed by content checks, static generation and search indexing. Twenty-eight
desktop/mobile browser groups cover all seven pages, local links, source includes,
images, overflow, keyboard question disclosure, six canonical redirects and
current-course placement. Twelve desktop/mobile light/dark accessibility checks
report no axe violations. Compact browser results are retained in `verification/`.

Rendered desktop lesson and mobile overview captures were visually inspected.
The overview uses the original prototype's native miss capture, whose source is
identical to finished. The board checkpoint's two-T capture was also inspected
against its worked example. No altered-state diagnostic image is used publicly.

## Publication

Samples PR [22](https://github.com/code198x/code-samples/pull/22) is merged at
`56bf2da`. README follow-up [23](https://github.com/code198x/code-samples/pull/23)
is merged at `953e809`. Website PR
[436](https://github.com/code198x/website/pull/436) is merged at `3ba81b75`.
Samples CI, website CI and code analysis pass. Pages deployment
[35344745828](https://github.com/code198x/website/actions/runs/35344745828)
succeeded. Twenty-one live HTTP checks cover the overview, all six lessons,
six canonical and six legacy topic redirects, the current-course listing and
unchanged native image. Evidence is retained in `verification/lesson-live.json`.

The [published lessons](https://code198x.com/systems/sinclair-zx-spectrum/basic/cipher/)
are available in Boards and deduction. The release note remains a draft. All
eighteen unrelated local edits retain their pre-publication contents or deletion
state.
