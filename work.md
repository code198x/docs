# Current work

This file holds bounded next work and proposals. [PROJECT.md](PROJECT.md) owns agreed direction; source files, catalogues and Git establish implementation state. The linked specifications and evidence records own the detail of finished work. Remove an item when it is done; do not keep a second status history here.

## Do next

1. **The Vault.** The [September 2026 content audit](audit/2026-09-content-audit/REPORT.md) found no Vault entry reviewed and a sample of checked claims wrong one time in six (H1). The owner has made the Vault the next priority and chose the review process in [the Vault specification](specifications/vault.md#reviewing-existing-entries): batches of about ten, one pull request each, owner approval as sign-off, and unreviewed entries kept out of search engines. Batches 1 to 63 have merged (batch 63 as website PR #535). Batch 64 is open as website PR #537 and batch 65 as #538, stacked on it. Batch 66 is in progress. The owner approves a batch on its PR; `gh stack merge <pr> --rebase` merges it with everything below it. Each PR lists the entries it queues for the next batch. [Candidates](vault-candidates.md) lists missing entries. See [Vault editorial work](#vault-editorial-work).
2. **Browser-player integration.** Merged as website PR #526 (2026-09-26), with the Playwright and accessibility suites in CI. System pages show our own capture as a poster that becomes the player; lessons get a run strip that opens a docked or overlaid panel. The spec is `docs/superpowers/specs/2026-09-25-browser-player-integration-design.md`. A panel inspector (registers, memory, labels) is a separate second project that needs Emu198x player and Debug198x work. Spectrum run strips wait on the `EMU198X_SPECTRUM_48K_ROM_B64` secret and code-samples #27 (assembly units); BASIC lessons follow from `build198x basic` (Build198x `docs/plans/2026-09-26-basic-verb.md`, in progress).
3. **Content audit follow-ups.** H4, M4, M5 and L3–L8 are fixed (website #519–#523), and every Spectrum lesson now builds with `asm198x --dialect pasmo --cpu z80 --tapbas` (#524). The Vault findings stay with item 1.
4. **Decisions the audit left with the owner.** Whether to publish the eleven What's New drafts for released work (publishing posts to Discord), and whether C64 BASIC keeps its "reflex" and "quizmaster" games, whose names were retired from Spectrum BASIC. The 71 Vault entries and 10 timeline events from 2005 onwards are decided: a post-2005 subject stays when it bears directly on the covered period, and each is judged against the [Vault specification](specifications/vault.md#writing-and-evidence) as it comes up for review.

## Curriculum implementation queue

The C and R numbers group related progression work; each checkbox is an independently reviewable delivery. The linked specifications own teaching detail and hold the evidence for the deliveries already accepted. Work on one item at a time, and do not treat approval to continue as approval to publish or to change the game lineup.

### Review what was published without its recorded review

The progression additions (C01–C04, C06–C09d and R2–R4e) were published with website PR #449 on 23 September 2026 at the owner's request, together with the four Game Feel controls-and-response lessons. Several had not completed the review their records call for:

- [ ] **Bright Spark:** confirm muted readability of labels, asterisks and result text during play and replay (C01), and review units 02/04/06/07 in the rendered site, distinguishing audible trials from paper exercises (R1).
- [ ] **R4e:** review the tune-sequencer pattern's contracts against the Flock 17/18, Starfield 17 and Dash 17 players ([evidence](specifications/experiments/audio-progression.md#sequencer-contract-review)).
- [ ] **C09c:** review Dash unit 17's complete-request companion ([evidence](../code-samples/nintendo-entertainment-system/assembly/dash/unit-17/handoff/README.md)).
- [ ] **R5 — Game Feel:** review the four controls-and-response lessons before adding more Game Feel content ([coverage map](specifications/craft-coverage.md)).
- [ ] **Learner trials:** most accepted C-series exercises record a pending learner trial. For a new exercise form, ask: can someone identify the relevant state, choose an observation and explain one changed case with the available hints? Record help needed and revise confusing wording.

### Open deliveries

- [ ] **C03a follow-up — linked audio examples.** Before promoting them as runnable starting points, repair `sinclair-zx-spectrum/assembly/audio/sound-beep.mdx` (HL changes the repetition count while the delay stays fixed; validate claimed pitch changes and local-label scope), `nintendo-nes/assembly/audio/square-wave.mdx` (DMC/sample wording, sweep muting and length-load semantics), `commodore-64/assembly/audio/sid-note-trigger.mdx` (non-instant rate 0, retrigger and ownership assumptions, unverified cost estimates) and `commodore-amiga/assembly/audio/playing-a-sample.mdx` (period versus waveform pitch, DMA cost, ownership, one-shot interrupt timing). Deliver each with its own executable check.
- [ ] **Triangle held output in Emu198x.** Before using Emu198x to teach the NES triangle's held output or clicks, fix `emu198x-ricoh-apu-2a03`'s `Triangle::output()`, which returns zero when gated, contrary to the held-output hardware contract. File it as an emu198x issue with a focused regression; do not change the lesson to match the emulator.
- [ ] **C05 — Meteor Storm: measure, overload and repair one drawing path.** Build the unit 20 profiling companion around its existing counters and `verification/checkpoints.py` (baseline, bounded extra render work, diagnosis, repair), preserving collision, simulation, course events, random-call order and input schedule. Coordinate with the Spectrum assembly rewrite first. Plans: [profiling](specifications/experiments/profiling-progression.md), [headroom](specifications/experiments/scheduling-ownership-headroom.md).
- [ ] **C09e — Dash: connect collection to feedback.** After the triangle fix, trace the input/state/audio/PPU path; compare muted collection with an isolated, bounded delayed cue. Preserve score and collision events. Plan: [feedback](specifications/experiments/timing-and-player-feedback.md).
- [ ] **C10a — Dice Roller: demonstrate mapping bias.** Enumerate remainder mapping, compare a correctly specified rejection mapping, then inspect short samples; state the different source domains for a uniform byte and a non-zero LFSR. No statistics framework. Plan: [randomness](specifications/experiments/randomness-and-reproducibility.md).
- [ ] **C11a — Port one input rule between Spectrum and NES.** Two isolated newly-pressed-action fixtures sharing one logical input/state table; test hardware readers separately from injected input, including reset while held and release/repress. Keep two understandable implementations. Plan: [abstraction and portability](specifications/experiments/abstraction-and-portability.md).

### How a delivery is done

Before editing a runnable item, record its exact baseline source and revision, target/model/region, tool versions, build/load route and recovery copy in the project's verification notes. Choose the placement deliberately: replace an explanation, add a short inline exercise, create a linked optional companion or revisit later. For timing work, measure the unchanged workload first, then name the boundary, workload and acceptable result. Record maximum observed costs as observations, not bounds.

At review, inspect the rendered exercise and ask for a prediction before revealing the answer. Check rendered length, hint ordering, keyboard-accessible reveals, backward links and the optional/essential boundary. Record static and build checks separately from native observation, listening and any learner trial.

### Keep for later, with a trigger

- **Later audio engines and advanced hardware:** AY/IM 2, SID Symphony, Thunder Run and Onslaught extensions follow a reviewed game brief. MIDI and PC sound remain explicit future coverage.
- **Replay and procedural layouts:** only when a reproducible failure or agreed mechanic justifies them and input/reset/update contracts are stable.
- **Loading recovery and OS return:** when a real loader or environment-return requirement exists. Flock's halt loop is not a Workbench exit.
- **Host profiling, compression and broad pipelines:** require a measured bottleneck or storage constraint.
- **BASIC performance revisits:** stay deferred until the owner resumes [that thread](platforms/sinclair-zx-spectrum/basic/performance-revisits.md); the progression companions do not resume it.

## Audio and performance

Audio work is part of the queue above: the C03a follow-up, the triangle fix, C05 and C09e. The [audio direction](specifications/graphics-and-audio.md) and [four-system progression](specifications/experiments/audio-progression.md) own scope and teaching detail. Do not keep a separate audio to-do list.

## Spectrum sequences

The agreed Spectrum BASIC rewrite is complete and published; the catalogue in `website/src/content/modules/sinclair-zx-spectrum/basic.yaml` and [PROJECT.md](PROJECT.md) record its games and grouping. There is no remaining batch of old BASIC games to rewrite, and the [remaining-course review](platforms/sinclair-zx-spectrum/basic/course-review.md)'s old recommendations are not the current backlog.

### Next output

No further BASIC game is commissioned. Progression work deepens the existing games through the queue above.

Spectrum assembly is a separate rewrite. The published opening is Meet Assembly → Meteor Storm. The later modules in the catalogue (Gloaming, The Long Night, Shadowkeep and Meet the Machine) are authored material whose place in the revised route is not yet agreed; the assembly session owns that reconciliation.

## Website components

Component names refer to the website's `src/components/`; their props and tests are authoritative. Use existing components before proposing new interfaces.

| Teaching need | Existing components | Use and limits |
|---|---|---|
| Explain code and changes | `CodeFromFile`, `CodeDiff`, `Output` | Real sources and focused changes; pseudocode stays distinct from executable code |
| Trace values and decisions | `TraceTable`, `FlowDiagram`, `TruthTable`, `LogicCircuit` | `TraceTable` is a static table, not an interpreter |
| Inspect representation | `MemoryMap`, `RegisterBits`, `SpriteGrid`, `SpectrumBitmapLayout` | Name assumptions; the bitmap component is Spectrum-specific |
| Draw and examine graphics | `SpriteEditor`, `Figure`, `NativeImage`, `ImageComparison` | Check format and export support before promising an asset workflow |
| Hear or see an outcome | `AudioClip`, `VideoPlayer`, `VideoEmbed`, `FieldVideo` | Pair media with captions and alternatives |
| Run or edit target code | `AssembleAndRun`, `BasicAndRun`, `NesAssembleAndRun`, `LessonPlayer`, `BrowserPlayer`, `Emulator`, `Workbench` | Each has its own machine and language contract; a browser player does not establish curriculum support |
| Ask and explain | `Question`, plain details/summary | Visible prompt with a native disclosure; no scoring engine is needed |
| Find a route or set up | `FirstStepCallout`, `CurriculumPosition`, `PathCard`, `UnitSteps`, `SetupCallout` | Support independent entry; no completion gates |

Possible additions, in order of demonstrated need:

1. **Target and build information:** a consistent table naming runtime machine, model, memory, extensions, input and host tools, factored into a `TargetConfiguration` component only if it repeats.
2. **Steppable traces:** a bounded enhancement showing state changes while keeping a printable `TraceTable`. A pseudocode interpreter is a separate proposal.
3. **Spatial and behavioural experiments:** use existing grids first; build an interactive grid only when a worked game needs to vary obstacles, tie-breaking or perception.
4. **Asset comparisons:** reuse image and audio primitives; extend conversion tools only around an agreed target format.

A wider editable-BASIC retrofit beyond Meet BASIC and Sonar is separate scope.

Any addition must keep the essential explanation readable without the interaction, and provide keyboard operation, visible focus, labelled controls, 44-pixel touch targets, narrow-screen layouts, reduced-motion support and reserved media dimensions. A visualisation names what it models and omits; a hand-authored trace is not execution evidence.

## Vault editorial work

The [content audit](audit/2026-09-content-audit/REPORT.md) sets the Vault's agenda (H1, H6, M1–M3, M8, M9, M12, L6, L7):

- **Accuracy (H1):** every entry is unreviewed. Correct the errors the fact-check sample found, then review in priority order. Set `reviewed: true` only when a person has checked the claims.
- **Private-collection wording (H6, M2, M3):** 207 rendered pages refer to "this library" or "held here", and frontmatter names local paths. Rewrite as statements about public sources; keep uncertainty, drop edit history.
- **Citations (M1):** the template renders only date citations, so most frontmatter sources are invisible, and 69% of entries cite nothing.
- **Consistency (M9, M12, L6, L7):** hype superlatives, synonymous platform identifiers, unverified manufacturer dates and stale entries.

Every entry a lesson links to is now in a batch. Batches choose the unreviewed entries that other Vault entries link to most, after any entries a batch queues. Re-rank before each batch: count the `/vault/` links to each entry whose frontmatter still says `reviewed: false`.

Open questions the reviews raised: which Paula channels are left and right (the manual contradicts itself; emu198x#1514 asks for a real-hardware recording), and whether technical claims belong in frontmatter `sources` keys or only in `<Sources>` (entries currently do both).

Two earlier investigations remain useful:

- Resolve entity mentions in Fast Facts and body prose to the correct existing entry, matching in context so that namesakes do not acquire each other's credits.
- Identify missing entries from real curriculum and Vault links, prioritising entries that help an actual lesson. [Vault candidates](vault-candidates.md) lists them with the entries that should link to each.

For game playtesting, work from the current program and its brief: held and tapped inputs, buffered actions, repeated title/retry cycles, readable feedback, audio timing and difficulty. Distinguish scripted correctness from human playtesting.

## Website editorial follow-through

Review About, the systems directory and the three editorial hubs with the homepage during the House UI review; the [preview design](https://github.com/code198x/website/blob/main/docs/superpowers/specs/2026-09-21-house-ui-preview-design.md) is a draft awaiting approval. Prepare a What's New entry when the House UI is ready to release. Try a small explanatory illustration before any site-wide visual treatment.

## Released source code to mine

Vault reviews keep turning up period games and tools whose original source has since been published. Each is a chance for lessons to read real period code rather than a reconstruction. Check each licence before quoting code on the site; the Vault entry named in brackets gives the details and sources.

- **Level 9:** Mike Austin's archive release of the A-code games and tools, December 2025 (`companies/level-9`).
- **Infocom:** Microsoft's MIT-licence release of the *Zork I–III* source, 20 November 2025 (`companies/infocom`).
- **Magnetic Scrolls:** the recovered game sources behind the Strand Games remasters (`companies/magnetic-scrolls`).
- **Elite:** Ian Bell's publication of sources for several versions in 2024, and Mark Moxon's annotated 6502 source (`games/elite`, `people/ian-bell`).
- **DAAD:** Aventuras AD's adventure system, released into the public domain and maintained today (`people/tim-gilberts`).
- **BRender:** Argonaut's 3D library, open-sourced in 2022 (`companies/argonaut`).
- **SimCity:** the original code, released under GPL v3 as *Micropolis* in January 2008 (`games/sim-city`).
- **Rogue:** BSD-licensed source (`genres/roguelike`, `techniques/procedural-generation`).
- **Alien Breed 3D II:** Team17 gave away the complete source of *The Killing Grounds* on *Amiga Format*'s cover CD, issue 95, March 1997; no licence stated (`games/alien-breed`, `companies/team17`).
- **ProTracker:** no original source, but Olav Sørensen's ProTracker 2.3F rebuilt from a disassembly of 2.3D and his C clone are BSD 3-Clause, and Frank Wille's 2.3B play routine is public domain on Aminet (`tools/protracker`).
- **Second Reality:** Future Crew's 1993 PC demo, full source and data published by Mika Tuomi (Trug) on 1 August 2013 under the Unlicense; mostly x86 assembly and C, some Pascal (`demos/second-reality`).
- **farbrausch:** the group's tools released on GitHub (farbrausch/fr_public) in April 2012: Werkkzeug3 with the source data for *debris.*, *theta* and *.kkrieger*, Werkkzeug4/Altona, kkrunchy, the V2 synthesiser and more; BSD or public domain per project (`groups/farbrausch`).
- **Elevated:** RGBA and TBC's 2009 4K intro, full source published on scene.org in 2016 under CC BY-NC-SA 3.0; rgba's Epopeia demo engine on GitHub under MIT since 2019 (`demos/elevated`, `groups/rgba`).
- **Crinkler:** the 4K/1K intro linker-compressor by Blueberry and Mentor, open-sourced under zlib in July 2020 (`techniques/size-coding`, `techniques/compression`).
- **Insert No Coins:** Razor 1911's 2010 Windows 64K intro, source on GitHub (razordemo/Insert-No-Coins); no licence file, so ask before reusing (`groups/razor-1911`).
- **Doom:** id's engine source released in December 1997 for non-profit use (later relicensed under the GPL), plus the doombsp map builder in May 1994 (`games/doom`, `communities/modding`).
- **Quake:** *WinQuake*, *GLQuake* and *QuakeWorld* released under the GPL by id on 21 December 1999 (github.com/id-Software/Quake) (`games/quake`).
- **Microsoft BASIC for 6502:** version 1.1 (1976–78), the ancestor of Commodore PET BASIC V2, released under MIT on 3 September 2025 (microsoft/BASIC-M6502); it assembles for the PET, Apple II, KIM-1 and Ohio Scientific machines (`companies/microsoft`).
- **Defender:** Williams' 6809 source, published on GitHub by historicalsource on 8 January 2021; no licence stated (`games/defender`).
- **Robotron: 2084:** Vid Kidz's 6809 source, published on GitHub by historicalsource (historicalsource/robotron) in 2021; no licence stated (`games/robotron-2084`).
- **Impulse Tracker:** Jeffrey Lim's source, published in 2014 under BSD 3-Clause (jthlim/impulse-tracker) (`culture/tracker-music`).
- **Command & Conquer:** EA's source for *Tiberian Dawn*, *Red Alert*, *Renegade* and *Generals*/*Zero Hour*, published on GitHub on 27 February 2025 under GPL v3 with additional terms, for preservation (it does not build as published); earlier, in May 2020, the *Remastered Collection*'s two game libraries and map editor (`games/command-and-conquer`, `games/red-alert`).
- **MS-DOS:** versions 1.25 and 2.0 (2014, 2018) and 4.00 (25 April 2024, MIT, with IBM) (`companies/microsoft`).
- **Galaksija:** Voja Antonić's commented ROM A listing (version 28, January 1984), the ROM images and the ROM B listing, in the public mejs/galaksija repository on GitHub; no licence stated. A Z80 machine whose CPU draws the video in its interrupt routine (`systems/galaksija`).
- **RISC OS 5:** relicensed under Apache 2.0 in October 2018 (per Wikipedia; confirm with RISC OS Open). Later than the Archimedes-era Arthur and RISC OS 2, which were not released (`systems/acorn-archimedes`).
- **Prince of Persia:** Jordan Mechner's Apple II 6502 source, published on GitHub (jmechner/Prince-of-Persia-Apple-II) in April 2012 after the disks were recovered; no standard licence stated, so check before quoting (`games/prince-of-persia` when reviewed).
- **Logo:** early Logo sources (BBN's PDP-10 Logo; MIT's CLOGO, LLOGO, 11LOGO and APLOGO) in the PDP-10 ITS archive on GitHub (`tools/logo-language`).
- **ZZT:** Tim Sweeney's own June 1991 development source (Turbo Pascal, close to ZZT 3.0), released as "The Almost of ZZT" by Adrian Siekierka on 28 January 2023 under MIT with Epic's permission; also "The Reconstruction of ZZT" (March 2020, MIT, with Sweeney's permission), a decompilation that builds an identical 3.2 executable (`tools/zzt`).

## Shared subjects

The seven Craft modules are Maths for Games, Game Feel, Game AI, Game Design, Game Data and Algorithms, Graphics and Animation, and Sound and Music; the [coverage map](specifications/craft-coverage.md) owns their responsibilities. Maths for Games has eleven published lessons, and Game Feel four published lessons awaiting review (R5). After that review, Game Design then Game AI are the next shared-subject priorities. Other modules have agreed homes, not authored sequences.
