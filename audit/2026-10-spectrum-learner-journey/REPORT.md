# Spectrum learner journey review

Reviewed on 4 October 2026 against the live https://code198x.com site following website release `b079bbc9d14f1d9410cb6e1867ed2c11bef8ae70` ([deployment](https://github.com/code198x/website/actions/runs/37196979520)).

## Assessment

The tested route works: homepage → Sinclair ZX Spectrum → assembly track → Meet Assembly → Meteor Storm. The new presentation supports readable lessons, native keyboard-operated source drawers and real editable machine experiments. The most useful next work is a small pass on entry clarity and error recovery, followed by a fresh learner trial. No additional curriculum sequence or general emulator retrofit is commissioned by this review.

This is an expert review and browser execution check, not a human learner trial. It does not establish comprehension, audible sound quality, physical-device behaviour or original-hardware accuracy. Chrome-family browser checks at narrow widths do not establish Safari or a real mobile browser result.

## Confirmed findings, in priority order

### 1. Assembly errors expose raw JSON instead of useful diagnostics

On [Meet Assembly lesson 1](https://code198x.com/systems/sinclair-zx-spectrum/assembly/meet-assembly/unit-01/), replace `ld a,2` with `ld a,not_a_label` and assemble. The visible error is a serialised diagnostic array including `span`, `file`, `col`, `expansion_frames`, `code`, `severity` and `fix`. At desktop width, its actual message is beyond the visible part of the horizontal scroll area. The status merely says “Nothing to run.” Revert and subsequent successful assembly work.

`src/components/AssembleAndRun.astro` parses the result but passes an error array's original JSON string straight to `showDiagnostics`.

**Remedy:** format each diagnostic as a readable message with source filename and line, for example “Line 6: undefined symbol `not_a_label`”. Make the named editor line easy to find. Preserve a safe fallback for unexpected diagnostics. Check both the source drawer's open and closed states, keyboard recovery and a long message at narrow width.

Evidence: [visible error](error-viewport.png), [interaction results](interactions.json), [friction checks](friction.json).

### 2. The gateway's firmware note contradicts its deployed player

The [Spectrum gateway](https://code198x.com/systems/sinclair-zx-spectrum/) says “Needs your own ROM files · nothing is uploaded.” Pressing “Play the Spectrum” instead presents “The 48K ROM is included with this player.” Pressing Start boots without uploading firmware. The lesson's separate browser emulator also runs without a firmware upload.

`src/components/PlayerStage.astro` derives its launch note from the catalogue's hardware firmware requirement, which does not express the deployed build's embedded firmware availability.

**Remedy:** make the launch note reflect the actual build/variant's firmware availability. Keep browser lessons, the standalone player and local setup requirements distinct. Do not generalise the Spectrum's included ROM to other machines.

Evidence: [player prompt](gateway-player.png), [boot check](gateway-boot.json), [friction checks](friction.json).

### 3. Browser entry is less prominent than optional local setup

On the [assembly track](https://code198x.com/systems/sinclair-zx-spectrum/assembly/), the first course card is approximately 2,545 pixels down at a 390-pixel viewport and 1,691 pixels down at 1,440 pixels. “Set up your tools” comes before it. The direct “Start: Meet Assembly” action is approximately 7,119 and 4,540 pixels down respectively. These are document positions observed in a fresh 900-pixel-high viewport, not measurements of learner difficulty.

The homepage also links directly to [Meteor Storm](https://code198x.com/systems/sinclair-zx-spectrum/assembly/meteor-storm/). That overview's start action precedes its prose link to Meet Assembly. A novice can therefore bypass the foundation despite Meteor Storm lesson 1 relying on it. This is a plausible source of confusion, not an observed human failure.

**Remedy:** put the existing first-lesson link and “No installation needed” statement in the track's opening block. Label local setup optional for browser learning. Near Meteor Storm's start action, add a short “New to assembly? Begin with Meet Assembly” link. Give BASIC and assembly a short explanation of what each route offers, preserving independent entry rather than imposing a BASIC prerequisite.

### 4. The first editor gives no convenient way to keep changes

Meet Assembly lesson 1 has no “Download source” control, whereas the later reviewed experiments and Meteor Storm do. The static listing's Copy button copies the supplied listing, not the edited text. An edited lesson-1 program is replaced by the initial source after reload. The local-build section tells readers to save their edited source but the browser editor gives no matching export action.

**Remedy:** enable current-source download in this editor and clearly state its reload/Revert behaviour. An export button and short explanation may be enough; automatic persistence is a separate choice, not a requirement inferred by this audit.

Evidence: [friction checks](friction.json). The Meteor Storm current-source download passed at both widths.

### 5. Older course wording contradicts the new opening

The assembly track correctly places Meet Assembly and Meteor Storm first, then labels Gloaming, The Long Night and Shadowkeep as earlier projects. Gloaming's catalogue tagline still calls it “the first complete game you finish in assembly,” although Meteor Storm is now the first game in the agreed opening.

**Remedy:** remove that obsolete first-game claim. Keep the older material clearly available for exploration; do not imply an agreed continuation beyond Meteor Storm until the assembly sequence is reconciled. Counts such as “36 / 36 units” could also be labelled as published availability rather than resembling learner progress.

Source: `src/content/modules/sinclair-zx-spectrum/assembly.yaml` and the live assembly track.

### 6. One early prediction reveals its answer immediately

In [Meteor Storm lesson 1](https://code198x.com/systems/sinclair-zx-spectrum/assembly/meteor-storm/unit-01/), “Predict both rows” is followed immediately by the expected `$7F,$80` answer. The warning that a mostly black screen is an expected result appears near the end, after the local build commands.

**Remedy:** use the existing prediction disclosure for that answer and place the black-screen reassurance beside the initial run instruction. This is an editorial recommendation, not an execution defect: both the original and edited bitmap values were verified from the live machine.

## Validation performed

- Seventeen public pages at 390- and 1,440-pixel widths: all returned HTTP 200; no horizontal overflow or page JavaScript errors. Pages included home, Start Here, Spectrum gateway, assembly track, both module overviews, all eight Meet Assembly lessons, and Meteor Storm lessons 1, 28 and 36. [Page results](page-checks.json).
- Actual link clicks through the recommended route at both widths.
- First lesson: real red border; edit to green using Command/Control+Enter; native disclosure keyboard operation; malformed source; Revert and successful reassembly.
- All eight Next links in order and the final lesson's explicit link to Meteor Storm lesson 1.
- Meteor Storm lesson 1: actual bitmap values `$81,$00 / $40,$80`; changed source produces `$FF,$00 / $7F,$80`; downloaded source exactly matches the edited text.
- Gateway player: included-ROM prompt and boot without a firmware upload.
- Focused execution scripts cover the byte/pixel, eight-row, loop, drawing-routine, movement, frame-clock and guided-debugger experiments. Their final results are recorded in `focused-checks.json`.

The existing focused scripts assumed visible source editors. Audit copies opened the new drawers before those visibility checks and source edits. The movement audit also waits for actual observed key presses and releases, avoiding a stale-value race during repeated edge input. These are harness adaptations; deployed code and assertions about machine results were not weakened. Initial harness timeouts are not classified as site defects.

## Independent review

Claude reviewed visible text and links from eight public pages, with all tools disabled and no repository contents supplied. Its [text-only review](claude-review.txt) supports the entry/setup, save/export, course wording and prediction findings. Codex independently checked the live browser behaviour and identified the raw diagnostic output and actual embedded-ROM mismatch. Claude's suggestion that the standalone player requires uploaded ROMs is superseded by the observed boot result. Neither review substitutes for a fresh learner trial.

## Recommended next delivery

Address readable diagnostics and truthful firmware messaging first. Then bring the browser start action forward, add first-editor source download, and correct the two small curriculum wording issues. Repeat the focused checks for each affected behaviour, then ask a fresh learner to try the opening without coaching. Record where they need help, whether they can predict a change, recover an error and explain the result.

## Implementation follow-up

[The fixes and their validation](FIXES.md) record the follow-up to this review.
