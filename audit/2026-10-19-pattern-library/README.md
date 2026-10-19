# Pattern Library capability inventory

We already have substantial game-making material. The immediate opportunity is to turn selected game code and illustrative pattern listings into routines readers can find, combine and adapt. Start with a reliable game loop and a small playable composition, then develop alternatives where a real capability or cost question warrants them.

This audit supports [expansion issue #117](https://github.com/code198x/docs/issues/117). Its first tranche and wider-system choices are proposals. It changes no curriculum order, public taxonomy or publication state.

## Scope and evidence

The baseline is website `9a436eed24e5`, samples `49e350adb4f2` and documentation `63632e65a574`. The open code-first prototype is recorded separately at website `8b8e76201aa1` and samples `ca95c288b071`. [Baselines](baselines.json) retain full revisions, including the inspected emulator source.

The inventories enumerate **71 pattern pages**, **546 unit source files**, module catalogue states and **1,494 assembly/BASIC/include and related source files**. File counts are not counts of distinct techniques or qualified implementations. Sample trees include checkpoints, snippets and material for games without authored lesson bodies. [Modules](modules.csv) records catalogue status beside actual unit-file counts; neither establishes current live deployment. Getting-started and module overview pages are outside the unit count.

Close review concentrated on loop, input, movement, collision, object data, audio ownership and restart examples. The [68-cell capability matrix](capabilities.csv) selects 41 distinct lesson anchors across 17 areas and four systems. The full [lesson inventory](lessons.csv) and [sample inventory](sample-sources.csv) preserve discovery candidates beyond those anchors. This is a source inventory, not a new execution qualification run. A gap means no suitable dedicated reusable implementation was identified in the reviewed material; it does not mean the entire subject is absent from every lesson.

## Published library and lesson coverage

| System | Pattern pages | Unit source files | What the pattern labels establish |
| --- | ---: | ---: | --- |
| Spectrum | 20 | 292 | Three entries label executed machine examples; four maintain BASIC subroutines; thirteen are illustrative |
| C64 | 10 | 96 | Six label assembled/emulator-executed routines; four are illustrative |
| Amiga | 15 | 69 | One labels an assembled/emulator-executed sample driver; fourteen are illustrative |
| NES | 12 | 35 | One labels an assembled/emulator-executed pulse driver; eleven are illustrative |
| Cross-platform | 14 | — | One has an executed host Python collision reference; thirteen are illustrative |

The remaining 54 unit files are Foundations (39) and Craft (15). Amiga includes assembly, AMOS and Blitz; those languages remain peers. Spectrum includes BASIC, assembly and the machine introduction. The JSON/CSV inventories identify tracks and paths individually.

Across all 71 patterns, **55 are labelled illustrative code or pseudocode**, 11 label machine-executed examples, four maintain BASIC subroutines and one has the host Python reference. These are the pages' declared evidence levels, not a new endorsement of every retained record. The [pattern inventory](patterns.csv) preserves each exact label and maintained include path. A useful explanation may still need an executable caller, resource contract or qualification work before it meets the reusable-code goal.

Game-loop entries already exist for all four systems. Creating four more similarly named pages would duplicate them. Their illustrative status makes **improving those entries and connecting maintained implementations** the first job. Similarly, a game's inline reader does not need another article if an existing input entry can be improved.

## What each system can contribute

### Spectrum

[Meteor Storm’s clock lessons](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/meteor-storm/unit-07.mdx) and [pool traversal](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/meteor-storm/unit-13.mdx) already develop interrupt clocks, selected update rates, records and slot reuse. [Its collision lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/meteor-storm/unit-10.mdx) deliberately uses inset contact regions rather than reading lit pixels. [The rendering lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/meteor-storm/unit-21.mdx) separates simulation from drawing and compares measured budgets; [the sound-budget lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/meteor-storm/unit-26.mdx) develops sound work around the frame clock. These are stronger extraction candidates than inventing a generic engine.

[Gloaming](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/gloaming/unit-08.mdx) supplies save/restore-under drawing; [Shadowkeep](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/shadowkeep/unit-05.mdx) supplies a room graph and [its state lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/sinclair-zx-spectrum/assembly/shadowkeep/unit-07.mdx) writable world state. These are different capabilities from scrolling cameras and durable file saves. BASIC Crates adds map decoding/validation, Tail Chase slot reuse, and Drift position/velocity work. Preserve useful BASIC entries rather than making assembly the only library route.

The gaps are reusable interfaces for those contextual routines, safe composition and dedicated native collision alternatives. Existing bitmap-address, beep and profiling implementations are assets to reuse. The HALT-loop entry still needs an explicit interrupt/startup contract and measured behaviour when work misses its intended frame.

### C64

Maintained joystick, bounded movement, sprite setup, raster split, multiplexer and SID-note routines give the strongest existing assembly foundation. [Starfield](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-64/assembly/starfield/unit-02.mdx) explains a loop and joystick; [its hit test](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-64/assembly/starfield/unit-07.mdx) explains software contact and the limits of hardware flags; [its wave lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-64/assembly/starfield/unit-10.mdx) develops parallel arrays. [The final lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-64/assembly/starfield/unit-17.mdx) brings escalation, random choice, title audio and restart investigations together.

The gaps are composition and extraction: one agreed owner for CIA, sprite state, raster/interrupt work and sound writes; a callable collision test with explicit coordinate width; clean state/reset routines; and resource/cost comparisons. The smooth-scrolling and multi-voice pages are still illustrative. Moving star dots is not evidence of a reusable world camera.

### Amiga

[Flock’s steering lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-amiga/assembly/flock/unit-03.mdx) explicitly explains leaving the frame boundary before waiting for its return. [The animation lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-amiga/assembly/flock/unit-04.mdx) animates by changing sprite pointers. [The collision lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-amiga/assembly/flock/unit-06.mdx) reads the hardware collision latch once per frame and discusses its pixel-based behaviour. [The audio lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-amiga/assembly/flock/unit-11.mdx) explains frame-ticked effects, replacement and channel ownership; [the title lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/commodore-amiga/assembly/flock/unit-17.mdx) provides title/play/result transitions.

The library has many useful topics, but only its Paula sample entry carries the stronger maintained execution label. Extract the loop, controller and sprite/data contracts before treating the other listings as ready components. Keep hardware takeover, OS-friendly operation, Chip RAM, DMA and collision-group semantics explicit. Existing AMOS/Blitz introductions are extraction candidates too, not evidence that each assembly technique already has those implementations.

### NES

[Dash](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/nintendo-entertainment-system/assembly/dash/unit-02.mdx) teaches the serial controller; [The jump lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/nintendo-entertainment-system/assembly/dash/unit-03.mdx) develops signed velocity and grounded state. [Platform](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/nintendo-entertainment-system/assembly/dash/unit-07.mdx) and [wall collision](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/nintendo-entertainment-system/assembly/dash/unit-08.mdx) query level data before movement. [The score lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/nintendo-entertainment-system/assembly/dash/unit-10.mdx) updates the HUD during VBlank. [The last lesson](https://github.com/code198x/website/blob/9a436eed24e5129d3b83e15f8d0438d9f038e518/src/content/curriculum/nintendo-entertainment-system/assembly/dash/unit-17.mdx) goes further: scheduling, overload, notification counts and publication of a complete request to NMI already have concrete source examples.

The gaps are reusable reset/NMI/main ownership, bounded PPU/OAM writes, movement/tile-query contracts and packaging those existing examples. Cartridge mapper, region, zero-page usage and DMC assumptions belong to the implementation. Scrolling, column feeding and the music engine have dedicated pages but remain illustrative; they are not a reason to promise scrolling as part of the first composition.

## Coverage across the wider inventory

The [capability matrix](capabilities.json) records existing patterns, lesson and source anchors, plus a specific next step for every system in each area. It includes running/scheduling, input, world/object data, drawing, animation/feedback, movement, collision/queries, rules/interactions, behaviour, cameras/scrolling, audio, interface/text, levels/content, persistence, memory/assets, debugging/optimisation and building/releasing.

Three recurring gaps deserve particular attention:

- **Composition:** individually useful routines can disagree about interrupts, clocks, memory, drawing order and sound ownership. The small complete caller must expose those agreements.
- **Alternatives and costs:** the cross-platform AABB Python reference is not native collision evidence. Compare software boxes, multiple shapes, masks and useful hardware checks on named workloads. A box-first/mask-second path needs its own measurements; record code bytes, working and asset memory, candidate-pair counts and runtime variation. Include player-facing fairness and edge-contact rules.
- **Finishing and persistence:** games already teach score, lives, titles, restart, sound and release artefacts. Reusable menus, durable save formats/recovery, general loaders, banking/compression and content pipelines are much less established in this library. Keep RAM state, host snapshots, distributing a game and saving a player's progress distinct.

## Proposed first tranche

Use the verified draft readers/press detectors/sound callers in [samples #108](https://github.com/code198x/code-samples/pull/108) and [website #837](https://github.com/code198x/website/pull/837) as the starting dependency. They are open PRs, not published pattern coverage.

| Slice | Deliverable | Evidence needed |
| --- | --- | --- |
| 1. Game loop and ownership | Improve the four existing loop entries. Provide complete startup, frame wait/notification, input, update and render integration; name interrupt and hardware owners | Once-per-update counters, fast/slow work, deliberately missed frames, input still serviced, region/configuration recorded; no universal fixed-rate promise |
| 2. Movement and contact | Reuse C64 bounded movement; extract small Spectrum/Amiga/NES equivalents. Add a named software contact test or tile query with caller-owned response | Edge/corner/touching cases, coordinate limits, held motion, resource preservation; compare one useful hardware/software alternative before adding a mask family |
| 3. Play and restart | Title → play → result → restart in a tiny complete one-screen game. Reuse input and sound; add a small hazard/goal rather than a new genre framework | Repeated restarts reset all state; one event per new press; updates and sound coexist; a reader can change speed/bounds/contact without rewriting the loop |
| 4. Cost and extension | Record runtime/code/RAM/asset budgets for the composition, then select one later refinement that solves an observed need | Same scene and workload for comparisons, positive/negative controls, limits and contention stated; no unsourced cycle counts |

Review the small game's design before developing a lesson sequence. It is a vehicle to test the library, not a newly settled curriculum lineup. A future lesson can teach its pieces in runnable stages. After this tranche, object pools, animation clocks and map readers have particularly strong existing lesson sources; durable saves and full audio engines can follow when a project needs them.

## Bring an untaught system in alongside the core work

The [wider-system inventory](wider-systems.json) checks tracked samples and emulator profile/test-source existence for ten candidates. BBC Micro, VIC-20, MSX, Master System, Atom and Electron have only `.gitkeep` sample scaffolds at the pinned samples revision. CPC, Dragon, Vectrex and Atari ST have no authored sample tree there. None has unit bodies in the inspected website curriculum. Directory, CPU and emulator coverage do not establish a curriculum implementation.

**Propose one BBC Micro Model B qualification slice alongside the first loop work.** Make a small input → move → contact → sound example using a named MOS/BASIC configuration and learner loading route. Investigate firmware-managed services versus direct hardware ownership as the teaching contrast. Decide BASIC or assembly for this slice on that basis; do not require a new complete track. The [BBC profile](https://github.com/emu198x/emu198x/blob/6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c/crates/runtime-acorn-bbc-micro/src/profiles.rs) and [cassette tests](https://github.com/emu198x/emu198x/blob/6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c/crates/runtime-acorn-bbc-micro/tests/cassette.rs) are starting sources, not proof that this example already runs.

| Candidate | Useful contrast to investigate | Placement and remaining gate |
| --- | --- | --- |
| BBC Micro Model B | ROM/OS-managed input, pacing and sound versus hardware takeover | First proposed wider-system slice; qualify exact firmware, media, input and captures through existing [readiness #3](https://github.com/code198x/docs/issues/3) |
| VIC-20 | Reuse 6502 reasoning while exposing RAM expansion, screen/character placement and audio budgets | Next compact comparison; pin PAL/NTSC and RAM before estimating or porting |
| MSX1 and Master System | Z80 plus VDP access makes a useful contrast to Spectrum screen RAM; BIOS versus cartridge/startup choices remain distinct | Later pair of independent examples; qualify firmware/cartridge, model and controller routes separately |
| CPC464 | A further Z80 display/input/audio approach with prior evidence already linked in #3 | Existing qualification candidate; cassette scope can stand independently of broader disk models |
| Atom and Electron | More constrained or different Acorn environments; common CPU does not imply interchangeable routines | Retain in inventory, choose a concrete teaching question before scheduling |
| Dragon 32 | A different CPU and an existing runtime/configuration proposal | Coordinate [#5](https://github.com/code198x/docs/issues/5); no assumed CoCo compatibility |
| Vectrex | Vector refresh/beam work changes the meaning of the drawing loop | Coordinate [#4](https://github.com/code198x/docs/issues/4) and [#6](https://github.com/code198x/docs/issues/6); no runtime profile found at the inspected emulator revision |
| Atari ST | Shared 68000 does not transfer Amiga custom-chip routines | Existing #3 core dependency; no runtime profile found, so outside the first implementation tranche |

The current [capture runner](https://github.com/code198x/code-samples/blob/49e350adb4f2c4495c0601cb14e23a9260e304a1/_capture/capture.py) maps the core machines and Amiga language routes. Add only the required wider-system capture integration rather than a second qualification system. Public pattern publication also needs a deliberate extension of the current platform enum and route/discovery checks; named systems must not be disguised as cross-platform entries to avoid that change. A maintained sample can be developed and qualified before its public navigation is decided.

## Next decision

Agree the game-loop-led tranche and whether BBC Micro is the first wider-system probe. Then create bounded implementation children under #117, reusing #3 for readiness. Keep the broad inventory as a living coverage map: future projects can reveal needs, while useful routines can suggest future projects. Neither direction requires every system to implement every technique.


## Revalidate the inventory

From the documentation repository, run:

```sh
python3 audit/2026-10-19-pattern-library/validate.py \
  --website ../website --samples ../code-samples --docs . \
  --emulator ../../Emu198x/emu198x
```

The checker uses retained Git revisions, so later changes to main do not silently redefine this audit. It compares the pattern/unit enumerations with tracked files, checks CSV/JSON agreement, source/include/anchor paths, wider-system source claims and source permalinks. A deliberately missing source must be rejected. This checks the inventory; it does not execute the machine programs or assess reader usability.
