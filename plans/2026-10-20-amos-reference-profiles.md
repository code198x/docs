# Identify AMOS references and evaluate parser ownership

Follow the approved research direction without implementing or merging a parser.

1. Reconsult family boundaries and existing BASIC/parser decisions. Compare a
   dedicated language-tooling home, an explicit Asm198x scope extension and a
   temporary Code198x implementation. Keep all ownership options unadopted.
2. Inspect available AMOS media and existing native evidence read-only. Record
   media/component hashes, exact evidence level and unresolved distributions;
   distinguish located media from a working reference installation. Do not
   download runtimes, launch the user's session or change source media.
3. Add `platforms/commodore-amiga/amos/reference-profiles.md` and a bounded
   evidence record under `audit/2026-10-amos-reference-profiles/`. Add a linked
   ownership-options section to the parser proposal, citing binding decisions.
4. Verify hashes, JSON, links, privacy and prose. Commit/push to the existing
   parser proposal PR, with the recommendation ready for an explicit ownership
   decision. Any adopted sibling boundary belongs at the umbrella level later.
5. Verify remote retention, then remove the task worktree and scratch outputs.

Task worktree: `/private/tmp/198x-amos-reference-profiles`. Private scratch, if
needed: `output/amos-reference-profiles/` under the umbrella; retain only unique
reproduction material with an explicit removal condition. No new dependencies,
repositories, parser implementation or runtime qualification is authorised here.

## Outcome

Sixteen candidate payloads were inspected read-only against catalogue identities;
2 pass the filesystem check and 14 retain rejection diagnostics. None was newly
booted. The existing Pro working disk preserves all 78 original file bytes. A
separate nominal Pro 2.00 candidate differs only in its startup script (77 files
match), and Easy's first disk contains installation payloads rather than an
installed reference. No source media was changed.

The reviewable ownership proposal recommends a dedicated language-tooling sibling,
with an explicit Asm198x frontend scope as the other permanent-home option. The
existing BASIC parser/LSP demand and undecided ownership are linked. The adopted
choice must be recorded at umbrella level before implementation.
