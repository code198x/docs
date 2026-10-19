# The Pattern Library

## Purpose and agreed scope

The Pattern Library supplies concrete techniques readers can adapt. It covers the small routines needed to get a machine doing something as well as the larger structures that grow from them: reading a key, sampling a joystick, making a sound, drawing a sprite, organising a game loop, and handling more complex behaviour and presentation. A technique does not need to originate in a game study or be an advanced design pattern.

The owner approved this scope and the direction of one conceptual technique linked to distinct implementations on 19 October 2026. Implementation and navigation details still need a bounded prototype and review. Preserve current machine entry points and published URLs; a new conceptual identity must not hide the hardware-specific work. No bulk rewrite or exhaustive porting matrix is commissioned.

## Independent entry points and progression

Readers can look up one immediate job or follow a useful progression. Explain the local prerequisites and offer onward steps; do not turn the library into another compulsory course. A basic routine can be a complete, valuable entry. Build complexity by showing what a later technique adds, what it assumes and what it costs.

| Area | Small starting jobs | Useful later work |
| --- | --- | --- |
| Input | Read a key or a joystick/controller state; interpret bit masks and active states | Distinguish held/newly pressed/released input, deliberate repeat, action mapping, analogue ranges, buffering and recording |
| Sound and music | Make a beep or tone, trigger and release a note, play a sample | Non-blocking effects, envelopes and noise, voices/channels, sequencing, mixing and streaming where supported |
| Graphics and animation | Place a character or pixel, load a palette, draw or move a sprite | Tiles and maps, animation, scrolling, dirty regions, multiplexing and display-time effects where supported |
| Time and execution | Update a counter, wait for an appropriate event, structure an update loop | Separate clocks, schedule work, handle interrupts, budget work and compare frame-dependent with elapsed-time behaviour |
| Movement and collision | Move within bounds, test a tile or rectangle, represent position and velocity | Fixed-point motion, swept tests, spatial queries, camera relationships and deliberate update order |
| Data and memory | Index a table or grid, represent a small entity, copy a block safely | Pools, queues, compact formats, allocation strategies, compression and data-oriented update choices |
| Behaviour and rules | Test conditions, switch state, choose a target or legal neighbour | Perception and memory, routes, priorities, coordination, search and reusable rule/data representations |
| Storage and tools | Read or write a small format and prepare one usable asset | Loading, banked resources, conversion pipelines, save data, debugging, profiling and measured optimisation |

These are coverage directions, not assertions that all examples exist or work on every machine. Develop a branch when a concrete reader need, lesson, study or hardware capability warrants it. Keep higher-level presentation and production questions connected to useful implementations without forcing them into routine-shaped entries.

## Explain the operation and the intended result

Distinguish the layers without making one a lesser form of content:

- A hardware operation reads or writes a particular interface under stated conditions.
- An adaptable technique solves a recurring problem and identifies its assumptions.
- An implementation realises it on a particular machine, language and toolchain.
- A worked example makes the result visible or audible and shows how to integrate it.

For input, knowing that a button is down differs from deciding that one action should occur. For audio, setting up a voice differs from timing an effect while play continues. Link those jobs explicitly. Different machines may require materially different implementations, expose different capabilities or make the same apparent behaviour cost different amounts. Do not disguise those differences behind generic pseudocode.

The Craft explains intent and judgement: how a control feels, why an opponent anticipates a player, or why delayed feedback is understandable. The library explains adaptable mechanics. System tracks teach their use within growing games; Foundations explains general programming concepts; the Vault supplies historical context. Link where useful rather than duplicating a canonical explanation across all of them.

## Entry contract and evidence

Use the smallest form that serves the job. State the intended result early, name the machine/variant and language, and show the routine or refer to maintained code in code-samples. Explain inputs, outputs, representation, clobbered registers or shared state, memory ownership, timing assumptions and integration obligations where they matter. Address interactions with operating-system routines, interrupts and other users of the same hardware when relevant. Avoid ceremonial fields that add nothing.

Claims about hardware use the project's primary-reference and synthesis workflow. Existing listings are not automatically verified because they resemble a familiar idiom. Distinguish illustrative code, assembled code, observed execution on an identified configuration, and original-hardware checks. Give cost estimates a basis; distinguish estimates from measurements. Small routines need observable outcomes too: one button event rather than repeated events while held, the intended sound while the rest of a program keeps running, or a bounded write that leaves neighbouring data intact.

Do not silently upgrade an entry's evidence status or preserve an obsolete lesson number as proof of coverage. Improve or extend an existing entry before creating another under a different label.

## Discovery and the first prototype

Support both “read this machine's joystick” and “make one press cause one action”. A reader should be able to start from a familiar task without already knowing a technical name. Keep direct machine/language access alongside task-oriented discovery. Basic and advanced work belong in the same library, with useful onward relationships instead of a misleading universal ladder.

Prototype with existing input-state reading, input-edge detection, a basic sound trigger, and one study-derived technique. This deliberately includes routines that have value independently of the studies. Audit existing bodies, relation fields and incoming links first; do not create a second keyboard or joystick article merely to populate a new structure.

Before choosing a schema or migrating the catalogue, demonstrate that readers can find a small hardware operation, reach an appropriate implementation, distinguish it from an illustrative listing, identify a sensible next technique and follow old URLs. Check keyboard access, narrow/wide layouts, searching without JavaScript and representation of more than one machine or language. Keep the existing catalogue usable throughout.

The [accepted study-theme direction](../plans/2026-10-19-study-themes-and-library-scale.md) provides concrete Craft candidates. Approval of this scope does not claim that a new lesson, taxonomy, interface or implementation has shipped, and leaves the charter's current delivery priorities intact.
