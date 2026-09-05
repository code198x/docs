# Spectrum sequence re-specification

**Status: review scope; no replacement game lineup has been adopted.** The [project charter](../../PROJECT.md) and [game-brief specification](../../specifications/brief.md) govern the work. The agreed quality standard is a complete, enjoyable and deliberately finished game for its scope; BASIC games need not meet commercial standards.

## Evidence to start from

The website has a substantial BASIC sequence and an assembly opening, with sample sources and existing plans in this directory. Inspect `src/content/modules/sinclair-zx-spectrum/`, the corresponding unit metadata and authored MDX, and `code-samples/sinclair-zx-spectrum/` together. Availability labels alone are insufficient evidence of what a learner can build.

Existing ideas include introductory BASIC programs, deduction and guessing games, quizzes and stories, grid puzzles, resource decisions and action games. The assembly material includes machine/language introductions, Gloaming and Shadowkeep, with plans extending beyond the implemented opening. Retain these as candidates and evidence, not an instruction to port each BASIC game to assembly.

Foundations now uses pseudocode. Read the actual rewrite rather than assuming the old Sinclair BASIC coverage. Maths for Games and Game Feel already have material under Craft, including planned unit breakdowns; a landing page or breakdown does not establish authored lessons. The broader Craft, AI, data-structure and asset coverage in the charter remains work to develop.

## Review questions

For each existing or proposed game, explain its recurring activity and appeal; its fit to Spectrum and language; what it introduces, reinforces or recalls; and the programming, maths, design, asset and hardware ideas that grow together. Map links to shared explanations, the Vault and useful reusable patterns without making those links essential missing instructions.

Plan meaningful runnable stages and a complete endpoint. Specify target configuration, host tools, source/build outputs and checks. Compare alternative game choices where they teach something different. Do not preserve arbitrary counts, commercial comparisons or genre exclusivity as requirements.

BASIC and assembly each admit independent entry. A brief recall of programming concepts can accompany the first real example; an explanation of syntax and machine behaviour must remain local. Gloaming's compact assembly scope and Shadowkeep's room-based systems deserve assessment for their distinct teaching roles; neither fixes the new sequence in advance.

## Models and wider systems

The existing Spectrum opening uses a stock 48K target; previous plans also discuss 128K facilities and Spectrum Next use. Keep the distinction between running a stock-compatible program on a Next and requiring Next-specific facilities. Before changing a game's target, check its actual source, brief, build recipe and execution evidence. Do not transfer a later model's capabilities into an earlier model's description.

A later expanded-machine project may be valuable if it explains the extension, what the Spectrum still does, the communication interface, changed constraints and new bottlenecks. Cross-development tools are host conveniences, not target expansions.

Keep useful contrasts with C64, Amiga, NES and future systems visible. Reusing a mechanic should illuminate a difference in language, CPU, memory, display, sound or input; it is not a requirement for identical projects or lesson counts.

## Next output

Produce reviewable game briefs and a sequence mapping before lesson rewrites. Record concrete missing shared explanations, Vault entries, patterns and component needs. Resolve substantive conflicts with the briefing and separate recommendations from decisions. Historical versions remain in Git; the current specifications should not require reading amendment chains to discover the project goals.
