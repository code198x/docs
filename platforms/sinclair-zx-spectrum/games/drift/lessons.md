# Drift teaching implementation

The user accepted the version with velocity feedback after native docking and agreed to build the teaching progression. Six standalone checkpoints now support the [eight-lesson brief](lesson-brief.md). The final listing is byte-identical to the accepted prototype. The overview and lesson prose have not yet been authored or published.

## Checkpoints

Sources live in `code-samples/sinclair-zx-spectrum/basic/drift/teaching/`. Each directory retains its full listing, exact add/replace/delete transitions and changed-line listing. The first program is presented as a new listing.

| Checkpoint | Lessons | Executed result |
|---|---|---|
| `draw-ship` | 1 | Static triangle; drawing twice restores the untouched arena bitmap |
| `heading` | 2 | Eight headings, both wrap directions, unchanged position and no leftover pixels after a full rotation |
| `flight` | 3–4 | Two-component thrust/coasting, heading independent of velocity, counterthrust, speed cap, four walls and retry |
| `readout` | 5 | Resultant/component speeds and an unrounded low-speed cue; still no docking rule |
| `docking` | 6 | The accepted box and low-speed arrival, including a complete normal-frame transfer |
| `finished` | 7–8 | Accepted endpoint, title, normal-frame docking, result exit and independently saved/reloaded tape |

Counterthrust reuses the flight checkpoint: braking follows from the existing acceleration rule. It is an experiment and explanation, not an invented new command. Saving reuses the final source. Readout introduces the future docking speed band as SLOW; docking changes the label to DOCK OK when the position rule and box exist.

## Verification

`verification/evidence/summary.json` records six checkpoints and 79 passed check groups. Every listing was entered independently through stock 48K PAL ROM keyword keys, saved with `SAVE "drift" LINE 10`, and loaded into a fresh Emu198x Spectrum 0.25.0 process. Builds identify source, tape, executable and server. No game-state fixtures were injected.

CPU-stepped checks locate BASIC statement boundaries, compare keyboard-driven movement against a host vector model and read bitmap state. They verify stored lines, rotation/erasure, two velocity components, coast, counterthrust, resultant speed capping, four wall limits, resets, docking conditions and the displayed values. The free-flight and readout stages deliberately remain active after reaching the future dock region slowly. Their lack of a success rule is checked rather than inferred from omitted source.

Separate ordinary-frame trials check held turning, thrust/coast, crash, retry, flight exit and result exit. Both docking checkpoints complete a two-axis transfer and counterthrust arrival through real key events and video frames. Endpoint controls additionally confirm that fast passage through the dock is not a win. State observation guides scripted key choices; it does not change the program's position, heading or velocity.

Every retained PNG is original emulator output. Captures come from normal video-frame execution; their top 176 display rows are compared with the current RAM bitmap. Drawing, heading, readout, title and docked examples were visually inspected. Some diagnostic captures are retained after STOP/Q to hold the scene still; they are verification images, not evidence of animation or final learner-facing figure selection. The capture records identify settling frames and scope. Images are never reconstructed or edited.

The audit replays every source transition, checks all literal branch targets, verifies fresh-loaded line identities and both TAP block checksums, and compares the final listing byte for byte with the accepted prototype. The final teaching tape also passes the maintained prototype control and timing tools.

## Limits and next work

The final teaching source has the same measured behaviour as the accepted endpoint. Its ordinary-frame run observed a median of 19 PAL frames at rest and 44 during held thrust; the latter sample includes the transition into burning. These are observations of one configuration, not fixed timing promises, host-input latency or original-hardware measurements. Intermediate programs perform less work and may run faster. CPU-stepped model traces are not timing benchmarks.

Native approval belongs to the final game. Independent learner outcomes for the stages remain untested. The next bounded task is authoring the overview and eight lessons for local review, with precise primary citations, checked conceptual links and appropriate captures. No catalogue availability or publication state has changed. Performance/assembly revisits remain deferred.
