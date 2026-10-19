# First AMOS lesson pair: typed entry and native persistence

The two [lesson drafts](../../platforms/commodore-amiga/games/bank-or-risk/lesson-drafts/README.md)
now have native evidence for typing the message, replacing one line, diagnosing
an instruction typo, repairing it, saving and loading the saved edit in a
separately cold-booted AMOS session. They remain review drafts, off the website.

## Exact scope and setup

AMOS Professional 2.00; Emu198x source
`6ff929f366e8762d5d5b9dadf53367b2cc692821`; stock PAL A1200, 2 MiB chip RAM,
no fast RAM. Existing lawful ROM/runtime and Build198x inputs remain pinned
in `inputs.json`. The fixed binary is reused, with no dependency or source change.
The [storage follow-up](../2026-10-amos-storage-follow-up/REPORT.md) records
why this source revision matters; version 0.34.2 alone is insufficient.

The initial five-line program is typed into the blank editor using key events,
in two bounded phases. No Merge ASCII or memory injection supplies its code.
F2 reports No errors; F1 displays the title and invitation. Space allows
Wait Key to complete and Return at the end prompt returns to editing.

Three Up presses reach the second Print line. Control+Q clears that line;
typing the new Print instruction changes the invitation without changing the
other four instructions. F2 accepts it. A separate edit changes the title's
Print to Prit; F2 reports Syntax error. Restoring Print reports No errors and
runs the changed question. The captures retain the deliberate failure and repair.

## Save and independent Load

Insert the empty writable data disk before opening Save As. The requester
initially names the removed system volume and reports Device not available.
Dismiss that message and replace the directory with DF0:*.AMOS. The retained
script selects the path through the requester's Tab handling; it clicks the
filename field, types welcome.amos and confirms. The draft describes the
same two fields, rather than asking a beginner to copy the automation.

The exported OFS disk passes verify and manifest. Its 108-byte welcome.amos
contains the changed question and excludes the original invitation. Linked
OFS blocks and logical pointer ranges return identical bytes.

A separate boot starts from the unmodified runtime disk, in four 500-frame
phases; its blank editor contains no lesson code. The exported data disk is
then inserted and welcome.amos loaded through AMOS's Load requester. The
listing, F2 No errors and F1 output show the changed question. Intermediate
boot snapshots resume that boot; no edited-session snapshot supplies the
program to the new editor.

The two printed rows match before saving and after native Load. The comparison
uses native image rectangle [164,50,1444,82], covering both output rows while
excluding the pointer and text cursor. The same comparison rejects the earlier
original invitation. Other pixels and every host configuration are outside
that equality claim. The original-invitation negative control uses the inner
second-row rectangle [340,66,1200,82], away from the original pointer, so cursor
movement cannot be its reason for failing. `storage-checks.json` retains these
regions and the disk/program identities.

## Teaching and publication boundaries

Full listings in both drafts agree with the maintained opening source files.
The one-line replacement maps message.amos exactly to edited-message.amos.
Predictions precede native details/summary explanations; the typo asks for a
repair before showing it. Local links, JSON and prose checks pass. No new
rule, variable, graphic or sound is added.

The local HTML review is generated with the already-installed CommonMark
renderer and embeds the checked game capture. Its three answer disclosures
are structurally checked. Browser visual/keyboard review remains pending:
the in-app browser is unavailable. No website layout or route changes.

MCP performs host disk insertion and export in this authoring verification.
That does not qualify a desktop export route a child or parent has followed.
The selected host setup, key mapping, export operation, availability of the
fixed emulator build, rendered lesson review and an uncoached learner trial
remain release gates. No learner outcome is inferred from successful execution.

## Replaying and preservation

`sequence.json` lists the retained phases; `requests/` holds MCP JSON-RPC
arrays. Substitute `${RUN}` for an isolated output directory, `${BASELINE}`
for the lawful preceding fixed-runtime baseline, and `${REPRO}` for the
original private reproducer. Emit each array's objects as JSON lines to the
pinned binary in --mcp mode with model a1200 and the matching Kickstart.
Every subprocess is bounded to 50 seconds; preserve dependent outputs.

Licensed disks, native programs, snapshots and ROMs remain private. Public
captures, commands and reports are bound by artifact-hashes.json. Preserve
the private first-lessons output until the drafts and native evidence have
been reviewed. The active user game was not changed.
