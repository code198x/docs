# Finishing and delivering games

**Status:** Progression with a local Story Builder completion/handover exercise in Meet BASIC unit 04. No game build, package, native execution or external distribution was performed in this pass. Later delivery records and exercises remain proposed. Scope: Spectrum, C64, NES and Amiga; completion is relative to the intended project, not a commercial standard.

Apply [briefs](../brief.md), [unit guidance](../unit.md), [content workflow](../content-creation-workflow.md) and [website/build guidance](../../website.md). Build on [existing-code baselines](working-with-existing-code.md), [lifecycle checks](state-lifecycle-and-recovery.md), [data/assets](data-memory-tools.md) and [diagnosis](testing-and-diagnosis.md). Those documents own implementation and author publishing requirements; this plan teaches learners how to define and demonstrate a finished deliverable. It authorises no publication.

## Existing coverage

- Meet BASIC 02 distinguishes readable source, tape and snapshots. Unit 04 already saves/exports a named Story Builder tape, reloads in a fresh session and asks another person to try the instructions. **Local addition:** observable completion criteria, source/package association, a concise handover note and optional future work.
- Lucky Number's Meet BASIC 08 and the later small toys supply natural complete-loop milestones. Bright Spark 07 adds instructions, completion/failure/replay, source/tape retention and licence attribution. Sonar 09 verifies a whole visit from a fresh named tape load.
- The author workflow already requires source builds, normal startup/play/end/restart, packaging, credits and honest evidence. Its full publication checks are not a beginner's homework checklist.
- Inspected sample Makefiles: Starfield 17 assembles per-step PRGs; Dash 14 builds an NES image; Flock 11 assembles an executable then masters an ADF. The website `scripts/build-artefacts.sh` stages downloads from sources and configures tool versions/checksums. These are source-observed paths, not builds executed for this plan. Its defaults are not a permanent curriculum version promise.

The gap is a repeated learner practice: define a small release, meet its required criteria, associate source and output, then stop without letting optional ideas block completion. Larger games need more precise dependency, asset and packaged-environment evidence; not every toy needs a manifest or automation pipeline.

## Stages and project milestones

| Stage / existing home | Smallest useful completion exercise | Outcome / growth |
|---|---|---|
| 1. A recoverable toy: Meet BASIC 02/04 | Preserve source and named tape; fresh-load, answer prompts, reach the ending and run again. **Unit 04 locally authored:** write a short handover note and separate later ideas. | Someone can follow the note without the author's open session. No compiler, installer or Git prerequisite. |
| 2. A complete game loop: Lucky Number 08 → Bright Spark 07 | State start, valid input, completion/failure where applicable, replay and exit criteria; test saved package and controls with another person. | Required paths pass; blocking input/short-answer limits are stated. Optional extra rounds/art are kept separate. |
| 3. A maintainable release: Sonar 09, Crates completion | Record source checkpoint, package identity, target, assets and a few regression cases; compare a fresh load with ordinary development execution. | A changed marker/map produces a new identifiable version. Invalid map handling and repeated restart are checked where applicable. |
| 4. Assembled outputs: Meet Assembly/Meteor Storm, Starfield, Dash, Flock | Build the selected checkpoint with documented dependencies, package in the target format, then start that actual artefact outside the usual injected/debug setup. | Distinguish compile success, boot/load success and complete gameplay. Log tools/configuration and missing dependencies instead of silently using an old binary. |
| 5. External assets and multiple build steps: actual first imported sprite/sample/map | Keep asset origin, terms/permission evidence, transformations, converter version and credits beside source; reproduce output from permitted inputs. | The deliverable contains what it needs, with understood redistribution scope; provenance is not reconstructed from memory at the end. |
| 6. A larger game: later Starfield/Maelstrom, Dash/Thunder Run, Flock/Onslaught | Check representative busy play, restart/level boundaries, sound/input, resource failures and named configurations justified by the brief. Produce concise release notes and a clean source checkpoint. | Release scope and evidence are inspectable; extended regional or original-hardware support is claimed only after corresponding checks. Later project placements remain proposals. |

## Define completion before polishing indefinitely

Use observable statements: “after retry the count is zero”, “the named image starts from reset in the declared configuration”, “the instructions identify movement and quit”, or “the package includes the sample data used by the build”. Avoid “fully polished” or “works everywhere”. A game with no victory state does not need an invented success screen; describe its repeatable play cycle instead.

Keep three short lists: **required for this version**, **known limitations**, **later ideas**. A failure of a required criterion must be repaired or the scope explicitly reconsidered; calling it a limitation does not make the criterion pass. A limitation such as one supported machine model can be entirely reasonable. An extra level, optional controller or alternative soundtrack need not delay a finished version.

The first completion exercise needs only a named source/tape pair and a note. Later file-based projects can use a release commit/tag plus a short build record. A tag identifies source, not proof that a particular binary was built from it. Record the associated output or checksum where useful; never commit secrets or unrelated local changes merely to obtain a clean status.

## Reproduce the build, then test the package

A later build record names the selected source revision/checkpoint, actual tool versions, required assets/converters, build command, target output and launch instructions. Separate host tools from target firmware/configuration. If the source uses a relative asset path, try the documented layout from a clean work directory rather than depending on an author-specific absolute path.

An interpreted BASIC project can reproduce its program by loading the documented source/tape workflow; it does not need a compiler. An assembled game must not rely on a checked-in binary to conceal a missing build dependency. “Reproducible” here first means another person can follow the documented process to produce the intended runnable result. Byte-identical output is a stronger property to test when claimed; timestamps, packaging or tool changes can affect bytes.

| Target / inspected example | Appropriate deliverable | Packaged-result check and limits |
|---|---|---|
| Spectrum BASIC Story Builder/Sonar | Named program in exported TAP plus readable BASIC listing and loading note | Fresh 48K session, actual tape load and documented RUN/autostart behaviour. A snapshot/injected program is separate evidence, not proof of tape loading. |
| Spectrum assembly | The output and loader specified by the selected lesson/build | Confirm the actual snapshot/tape/load route and machine model; do not rename one format into another or assume all assembly checkpoints package alike. |
| C64 Starfield 17 | Selected step's PRG from its Makefile, source/build record and start instructions | Load/start the PRG through the documented path, then exercise start/result/retry. A debugger-injected capture does not establish disk/tape mastering or arbitrary C64 variants. |
| NES Dash 14 | Built `dash.nes`, source/dependencies and controller/target note | Start the cartridge image from reset in a named emulator/configuration. Identify applicable completion/restart behaviour; do not promise a desktop quit or an existing retry feature that this checkpoint lacks. Cartridge-image testing is not physical cartridge testing. |
| Amiga Flock 11 | Assembled executable and Build198x-mastered ADF as specified by its Makefile | Boot the packaged disk with named machine, memory and firmware configuration. The current halt loop is not a Workbench return. Do not claim a clean OS exit unless implemented and verified. |

Test the artefact copied into the intended delivery folder, not only the executable still inside the development tree. A fresh emulator session with the declared dependencies is a proportionate first test outside the usual setup. A second person's machine is useful later; universal hardware access is not required. Do not bundle firmware merely because the development emulator uses it.

## Assets, provenance and permissions

Begin when external material first enters the project. Explain plainly: “We need to know where this came from and whether its stated terms or permission allow the way we plan to share it.” For each imported image, sample, font, map or other asset record creator/source, exact version, source URL or accompanying notice, any permission evidence, modifications and required credit text. Identify original learner work too, so the package's contents are clear.

Finding an asset online, crediting its creator or owning a copy does not establish permission to redistribute it. Do not assume the code's licence covers every asset or that conversion changes the applicable terms. Check the actual terms for the intended use; where unclear, obtain clarification, use an alternative with understood terms or omit the asset. This is a provenance/checking workflow, not a legal conclusion about an unexamined asset. No new licence determinations are made here.

Distinguish assets needed to rebuild from those included in the runnable package. Preserve relevant notices with the materials they cover. Keep required external dependencies explicit when they cannot be included. Do not make learners download material from an unspecified private collection to reproduce the game.

## Evidence and release notes

For each checked configuration record what was built/loaded, the tool and target settings, input/test route, observed result and remaining limits. Label evidence as **build**, **emulator execution**, **real hardware execution** or **human playtest**. None implies the others. A PAL-targeted project does not need NTSC support to finish; if another region is offered, test timing/audio/controls for that named configuration rather than assuming the same source suffices.

A concise note can contain:

- Version and matching source checkpoint; what this version changes.
- Target/configuration, dependencies and exact start/controls.
- Required packaged assets and credits/notices, where applicable.
- What was tested and where; explicit untested configurations/hardware.
- Known limitations and a separate small list of possible future improvements.

No release note should turn a planned fix into an implemented feature. Keep checks proportionate: a story needs load/prompts/ending/rerun; a stateful game adds relevant failure/retry/level transitions; a timed game adds representative load and audio/input evidence. Preserve normal-path tests alongside labelled short-cap or forced-state fixtures.

## Next bounded work

1. **Local now:** Story Builder's completion criteria and handover-note exercise. Working source is unchanged; no new package or native test result is claimed.
2. **Next delivery companion proposal:** prepare a small Bright Spark source/package release record alongside its already queued native trial, using existing completion/replay tests and an actual freshly loaded TAP. No new game feature is required.
3. Later assembled-game milestones use the actual Makefiles and capture routes above. First verify the chosen build and packaged start, then expand coverage only for the promised scope.

This task saves teaching material and plans only. Publishing a website, uploading a release, distributing assets or announcing a game remains a separate explicitly authorised action.
