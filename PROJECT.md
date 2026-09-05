# Code198x: purpose and direction

> You can understand the machine—and use that understanding to make things.

Code198x is developing a comprehensive games development and programming curriculum. Vintage computers give us environments small enough to understand how the pieces work together: how a variable is represented, how a loop executes, how pictures and sound become data, and how a program communicates with hardware.

We explain both how and why. Opening an abstraction should also explain why people built it, what it makes easier and what it costs. Readers should become comfortable moving between levels of detail and choosing the right one for a task. That understanding should remain useful when they return to modern hardware, languages and tools.

The purpose is understanding, creation, investigation and informed choice. Historical practice provides evidence and possibilities; it does not require us to reproduce old games or stop at original hardware configurations.

## Audience and voice

We write for children, parents and teachers, while respecting adults and experienced programmers. Clear explanations make the material accessible; childish language and assumed prior attendance do not.

The early layers take an Usborne-style approach: approachable, concrete, economical and inviting. Technical depth can grow without changing that respect for the reader. Use British English and “program” for computer software. The detailed editorial standard is [Writing voice](specifications/writing-voice.md).

## Scope across systems

The family covers computing from the 1960s through the early 2000s, with the 1970s and 1980s at its centre of gravity. Coverage is worldwide. Cultural, geographic, commercial, state-supported, socialist-bloc, kit, DIY and hobbyist-import contexts can explain different engineering choices and experiences.

Consider period, cultural and geographic coverage, support surface, form factor and role, and distribution or political-economic context when choosing a subject. A home computer, console, handheld, kit or workstation need not teach the same things.

Name the support surface precisely. Curriculum coverage, an emulator that boots a variant, and an assembler that supports its CPU are different capabilities. A system's presence in the Vault or fleet does not prove any of them.

The Spectrum is our first re-specification focus, not the destination every learner should choose or the template other systems must follow. C64, Amiga and NES tracks already provide other approaches. Wider systems enter through a concrete teaching purpose, not through a requirement to duplicate every existing game or language route.

Use BASIC or FORTH where the machine provides an appropriate environment. Where it does not, begin with assembly. C and C++ may become relevant later; they are not the present track-development priority.

## A connected curriculum

- **Lessons** guide readers through making things in meaningful stages.
- **Foundations** develops language-neutral programming concepts in pseudocode, including representation and reasoning about execution.
- **Maths for Games** develops mathematical tools through game problems, without becoming an upfront prerequisite course.
- **The Craft** develops game design, behavioural intent and practical game-making judgement in a language-neutral way.
- **System tracks** implement those ideas in concrete languages, tools and hardware.
- **The Vault** supplies encyclopaedic historical, cultural and technical context.
- **The Pattern Library** supplies concrete techniques readers can adapt, with their assumptions and trade-offs.

These are responsibilities, not a mandate to create a top-level module for every subject. [Curriculum design](specifications/curriculum.md) places the shared subjects and explains progression. Existing navigation and authored content are evidence of implementation, not limits on the intended coverage.

## Entry and progression

Readers may enter from another Code198x system, another language or outside experience. Spectrum BASIC requires neither Foundations nor assembly. Spectrum assembly requires neither BASIC nor Foundations. Shared subjects support readers when relevant.

Distinguish knowledge an example uses from lessons someone must have attended. Explain enough locally to continue, briefly recall a concept and offer a useful link for depth. Avoid both unexplained jumps and repeated full courses inside each track.

Within a game, provide a guided development sequence. Readers are not expected to invent independent projects as a condition of learning. Programs grow understandably; necessary files generally come from preceding work. Explain any supplied code and how it fits before readers must depend on it.

## What makes a finished game

A game should be complete, enjoyable, readable, responsive and deliberately finished for its agreed scope. BASIC games in particular need not meet commercial standards. A single room, a small puzzle or a short session can fulfil a worthwhile promise.

Choose failure and retry behaviour to suit each game. A reachable losing state is not compulsory: puzzles, creative games and exploration projects can provide meaningful decisions and satisfying outcomes without one. Where failure serves the experience, explain its purpose, consequences and recovery. This principle does not automatically remove failure mechanics from existing designs.

Selected later projects can be substantially more ambitious. Their scope must serve their experience and teaching, not match a commercial price tier or feature census. Assembly does not automatically require commercial scale.

Programming, design, graphics, sound and finishing develop together. Appropriate treatment matters more than equal quantities: deliberate silence or a small visual vocabulary can be a design choice. Runnable intermediate stages can be incomplete; a claimed finished game must fulfil its stated scope.

There are no fixed game counts, unit counts or universal language progressions. Historical games can inspire, explain or provide comparisons; a canonical ancestor is not a condition for a new teaching project. Reusing a mechanic across systems is welcome when it makes a useful contrast.

## Threads to keep visible

**Representation and approximation:** numbers, text, images and sound as data; precision, rounding, overflow and sampling.

**Time and coordination:** the CPU, display, sound and peripherals operate on different schedules. Their deadlines and communication shape programs.

**Interfaces and contracts:** routines, asset formats, build tools and devices agree on what data means. Make those agreements visible.

**Experimental reasoning:** predict, observe, explain discrepancies and revise the model. Code, documentation, hardware variants and emulators can all contain surprises or faults.

**Human engineering:** people made these systems under real constraints. Preserve their mistakes, compromises, collaboration and ingenuity without inventing motives or convenient origin stories.

## Present-day relevance

Make specific connections where they illuminate the work: algorithm costs and responsiveness; representation, allocation and data movement; frame and audio deadlines; input latency; bandwidth and buffering; shared-resource scheduling; asset size and decoding; interrupts and asynchronous events; cross-development and deployment targets; debugging and measurement.

Explain the limits. Fewer instructions do not automatically mean less energy, smaller code need not run faster, and an optimisation for one architecture may hurt another. Connect efficiency to what it enables: richer behaviour, smooth animation, better sound, predictable response or opportunities to save energy. Do not add a repetitive relevance sidebar to every lesson.

## Hardware configurations and cross-development

Separate the host used to develop a game from the target required to run it. Explain source, built output, asset conversion, assembly, emulation and transfer. Build-time convenience does not add runtime hardware capabilities.

Teach development on the target, historical cross-development and the modern workflow when relevant. Historical examples must be specific and sourced, including hobbyist and professional practice where evidence permits; workflows evolved during a machine's lifetime.

Original configurations are useful starting points, not permanent limits. For an expansion or modern peripheral, specify what it provides, what the original machine still does, how they communicate, which constraint changes and where the new bottleneck appears. Keep stock, expanded and successor-machine claims distinct.

## Evidence and responsible history

Check technical and historical claims against reliable sources, preferring primary evidence where appropriate. Identify the original publication, author, edition, issue, page, section or other precise locator so a claim can be checked. Public material, including open-source repositories, must cite the original source or relevant public pages, not private research locations or unavailable local collections.

Distinguish proposed design, source-checked claims, code that builds, behaviour checked by execution and behaviour checked only in a named emulator or hardware configuration. Tool or repository existence is not evidence that an execution integration is available.

For people and organisations, distinguish established facts, recollections, disputed accounts, allegations and interpretation. Do not invent dialogue, motives or anecdotes. Acknowledge documented wrongdoing proportionately without sensationalising it or treating technical achievement as an excuse. Use age-appropriate language without concealing relevant facts. Avoid unsupported “first”, “invented by” and single-author origin stories.

## Current work and authority

The immediate task is to re-specify the ZX Spectrum BASIC and assembly game sequences, then develop the lessons from agreed specifications. Retain, reshape or replace existing choices for their appeal, teaching value and suitability. The recommended sequences in the initial review remain proposals; only the scope-relative quality standard has been agreed from that review.

The website catalogues, lesson files, sample sources and Git establish what exists. A plan is not an implementation, a catalogue entry is not execution proof, and a future subject is not an authored module. The October 2026 launch target and four initial system on-ramps remain planning context, not evidence of completion or a boundary on the curriculum's purpose.

This charter is the current Code198x direction under the family [Principles](PRINCIPLES.md). Specifications explain how to apply it. When intent changes, edit the relevant current document and explain why in the pull request; do not maintain a competing policy or a chain of amendment banners. Git preserves prior decisions. Narrow technical specifications and game briefs must identify their status and cannot silently override this charter.
