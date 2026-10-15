# Basics ordering and input pilot

Continue umbrella #114/#115/#124 after website #736/docs #74 merge. Website
baseline 7c0fb762aef44edf6bcd8dec5f26aaa224ef4a74; docs baseline
984aa7306e4f01a0e21e70ab71b0711093829e5f. Preserve original checkouts.

1. Read all Basics units, earlier stored-value evidence, pseudocode and unit
   specifications. Deduplicate/file sequence-model and input-contract findings.
2. Edit `basics/index.mdx`, `unit-01.mdx`, `unit-02.mdx`, `unit-05.mdx`: scope
   straight-line order, separate displaying instructions from doing their jobs,
   avoid blaming every failure on the learner, name the text-input submission,
   empty and spacing rules, and show repeated-input behaviour. Use Question for
   new prompts. Add a scoped ASK authoring note in `specifications/pseudocode.md`.
3. Add native `verify-input.py`: actual ROM key-entry runs for output order,
   quoted words versus stored value, normal/repeated/empty/spaced/digit text;
   observe waiting before submission and exact string bytes after it. Keep target
   syntax distinct from teaching notation; no generic input parser or new runtime.
4. Add semicolon-complete browser verifier for the overview and units 1/2/5 at
   1440/390: outputs, questions and optional links. Retain baseline/known-red/after
   evidence; build/check, Vale/Ruff and syntax/semicolon checks. Inspect wide/narrow
   captures once and confirm at most one repair batch; measure unresolved contrast.
5. Retain learner/assessor sheets, report, source/environment identities and hashes.
   Update coverage and next bounded Decisions work. Push paired drafts, link parent
   issues, verify remote retention and clean task worktrees/caches/processes.
