# Graphics, sound effects and music

Asset creation is part of the curriculum. Apply [the charter](../PROJECT.md) and record each game's approach in [its brief](brief.md). Supplied assets can support a learner, but do not replace teaching how assets are made and why they work.

## Create

Teach drawing, silhouette, contrast, composition, colour, animation, sound design, composition and arrangement through concrete needs. Show enough of the creative process to make a choice deliberate: sketch alternatives, compare them in context and revise.

A sprite must remain visible in its environment. An animation should communicate action without making controls sluggish. Sound can anticipate, confirm or distinguish events. Music can establish rhythm and mood, but more notes are not automatically better.

## Prepare for the target

Explain the applicable palette, character set, tile, sprite, sample, instrument, channel, format and storage constraints. Different machines have different facilities; do not transfer one machine's terminology or capabilities without checking.

Show the relationship between the authored asset and its encoded bytes. Teach conversion settings and budgets, not only editor buttons. Separate work paid during the build from decoding, transfer and rendering paid while the game runs. Record source files and repeatable conversion steps.

Spectrum projects must distinguish stock beeper, model-specific sound hardware and extensions. Other tracks should expose their own meaningful constraints and opportunities rather than reproduce the Spectrum's sequence.

## Integrate

Develop assets alongside gameplay: readability at the intended scale, animation timing, transitions, sound priorities, channel competition, memory and frame budgets. Explain which resource a visual or sound uses and what else needs it.

Offer alternatives to colour-only and sound-only information. Test against the actual background, motion and competing audio. A loading-screen illustration, sprite sheet or tune heard alone is not proof that it works in the game.

## Progression and evidence

Early work can use a few self-authored glyphs and short feedback tones. Later work can deepen animation, tiles, instruments, melodic phrases, arrangements and dynamic responses where the target and game justify them. No fixed asset count or compulsory soundtrack applies to every game.

Use available tools and document their role. Build198x supplies conversion and preparation where implemented; Play198x can assist audition or inspection where its supported formats fit. Tool existence is not a promise of access or compatibility.

Keep editable originals, conversion instructions, provenance, permissions and credits. Verify output in the named target configuration and listen to the integrated audio. Public examples must be suitable for educational use and legally distributable.

The Craft develops shared principles; system lessons implement them; the Vault supplies sourced context; the Pattern Library records genuinely reusable techniques. Link these instead of maintaining parallel explanations.

## Agreed audio and performance direction

Audio has equal standing with graphics, input, game logic and the other areas of
game development. It needs a progressive learning path, integrated into games
throughout, with opportunities for deeper exploration. Equal standing does not
require equal lesson counts or a soundtrack in every game. Deliberate silence
remains a creative choice.

The current implementation scope is **ZX Spectrum, Commodore 64, NES and Amiga**.
Name the machine variant and audio configuration in each experiment. In
particular, do not silently give a stock Spectrum the facilities of a 128K model.

The inspiration for this discussion was Tim Follin’s *Solstice* NES title theme
([the supplied recording](https://youtu.be/4_gObHt1uZA)). We want to make some of
that apparent magic understandable through small, audible experiments. Learners
do not need to compose at Follin’s level to understand and apply individual
techniques. The recording is a listening reference, not evidence of a particular
implementation: attribute techniques to the track only with supporting evidence,
such as inspected code, a documented analysis or an attributable technical account.
Do not infer a driver technique from an impressive sound alone.

The [four-system audio progression](experiments/audio-progression.md) applies this
direction to existing projects, with prerequisites, audible exercises, playback
milestones and v1 boundaries. Its new placements remain proposals until adopted;
existing lessons and queued work are identified separately.

### Progressive understanding

This is an agreed direction, not a fixed lesson order or a new game lineup.
Revisit ideas as the games place new demands on them; introduce complexity when a
real requirement makes its purpose audible or visible.

| Thread | Progression to develop |
|---|---|
| Sound and musical ideas | Hear and distinguish pitch, duration, loudness and timbre; explore pulse, rhythm, rests, intervals, melody, harmony and arrangement through small phrases. Connect the heard result to its representation. |
| Communication and creative judgement | Make actions, warnings and outcomes distinguishable; compare alternatives in play, including silence. Consider repetition, fatigue, competing sounds and visual equivalents, as well as whether a sound is technically correct. |
| Hardware and instruments | Explain each machine’s facilities and constraints; create and revise instruments, effects and music using its applicable synthesis or sample techniques. Separate performance data, instrument definition and sound generation. |
| Playback routines | Grow from one sound to changing a sound over time, a phrase, a sequencer, multiple parts and effects/music arbitration as needed. Explain state, data, channel ownership, stopping and restoring sound; do not introduce an unexplained full player. |
| Timing and coordination | Distinguish waveform generation, note/effect updates, musical tempo, simulation and rendering. Teach interrupts, shared state and frame budgets where they solve a game requirement. |
| Measurement and diagnosis | Predict costs, measure normal and expensive paths, expose a controlled failure, explain it and compare a repair against the same baseline. Use both period techniques and modern tools. |

Possible deeper experiments include envelopes, pitch slides, vibrato, arpeggios,
noise percussion, sample loops and arrangements that share scarce channels.
These are authoring proposals to select for a target and game, not attributed
features of *Solstice* or compulsory additions to every track.

### Timing, regional differences and profiling

Audio participates in the whole game budget. Measure it alongside input,
simulation and drawing, including note changes, effect starts and competing
requests. A sound chip continuing a note does not make its playback routine free.
Separate intentional waiting from computation and hardware waiting; distinguish
average cost, worst observed cost and a justified worst-case bound.

Teach period techniques such as instruction/cycle accounting, border or raster
colour markers where supported, and hardware timers or frame counters. Pair them
with available modern emulator traces, cycle counters, debugger inspection and
audio captures or waveform views. Explain instrumentation overhead and what each
measurement observes. Tool availability must be verified for the selected target;
a browser demonstration’s elapsed time is not target-machine CPU evidence.

Name PAL/NTSC and other relevant clock or hardware variants rather than treating
50 or 60 updates per second as universal. Explore tempo and pitch separately:
changing the update schedule and changing hardware pitch values address different
questions. State the configuration, expected result and validation evidence for
each regional comparison. Hardware facts and clock values need precise primary
sources; existing lesson prose is not their authority.

The existing [BASIC performance-revisit investigation](../platforms/sinclair-zx-spectrum/basic/performance-revisits.md)
retains its own scope and measurement protocol. This direction does not activate
its deferred experiments or require assembly ports.

### How we teach it

Start with something simple, change one thing, hear or see the difference, then
explain it. Ask for a prediction before the comparison. Keep the earlier version
available so the change can be heard in context, with a visible representation
and clear playback controls where useful.

Include deliberate, controlled failures with a known working baseline and a
clear recovery: for example, omit a note-off, restore the wrong instrument after
an effect, or delay a playback update. Those are candidate experiments, not
claims about existing lessons. Diagnose which state or deadline caused the
symptom rather than presenting failure as the reader’s fault. Use comfortable
levels; a fault experiment need not produce a loud or prolonged sound.

Connect backwards to earlier ideas in numbers, tables, state, loops, clocks and
game feedback. Explain the immediate essentials locally. The Craft’s Sound and
Music module owns shared musical and creative ideas; system lessons realise
them on hardware; the Vault supplies checked context; the Pattern Library offers
reusable implementations with explicit assumptions. Review those resources before
linking, and avoid duplicating a parallel explanation in each home.

Use [our writing voice](writing-voice.md): accessible British English, “we” for
shared exploration, and a respectful tone for children, parents, teachers and
experienced adults. Musical knowledge is something to develop, not an assumed
entry qualification.

### Future coverage, outside current implementation

Preserve the following direction without adding machines, lessons or integrations
to the current four-system delivery scope:

- **MIDI:** performance instructions separate from sound generation; the same
  instructions can be interpreted by different instruments or sound generators.
- **PC speaker:** a further context for software-controlled sound and its costs.
- **AdLib/OPL:** FM synthesis and instrument design.
- **Sound Blaster:** sample playback and its data, timing and integration needs.
- **External MIDI modules:** sending performance instructions to a separate sound
  generator, with its own instruments and constraints.

## Existing coverage and gaps

This source audit (22 September 2026) inspected selected authored lessons,
maintained routines, audio patterns and Vault entries across the four systems.
It establishes existing material, not a complete correctness review, execution
verification or proof that a coherent audio course is already delivered. Paths
below are relative to website `src/content/` unless stated otherwise.

| Area | Existing evidence | Gap or review needed |
|---|---|---|
| Spectrum | `curriculum/sinclair-zx-spectrum/basic/bright-spark/unit-02-give-a-choice-a-signal.mdx` teaches panel pitches, semitones, duration and cue timing. Assembly audio patterns cover beeps, beeper music and AY tones, envelopes/noise and music. | Connect feedback choices to controlled audible comparisons and later playback costs. Keep beeper and AY routes explicit. |
| C64 | `curriculum/commodore-64/assembly/starfield/unit-17.mdx` and its maintained `steps/step-02.asm` implement a title jingle, rests, looping and voice/envelope handover. SID patterns cover voice setup, note triggering and multiple voices. | Develop instrument creation and musical judgement in smaller stages; verify timing claims rather than inheriting “twice per note” as a cost model. |
| NES | `curriculum/nintendo-entertainment-system/assembly/dash/unit-17.mdx` and `snippets/03-tune-tick.asm` contain a pulse sequencer with rests, loop/stop markers and title/ending phrases. Audio patterns progress from a pulse to effects and a music engine. | Separate musical, driver and gameplay changes into focused experiments; add measured budgets and explicit regional comparisons. The routine performs timer/state work and several sound-register writes, not a universal two-write operation. |
| Amiga | `curriculum/commodore-amiga/assembly/flock/unit-17.mdx` and `snippets/02-tunetick.asm` develop sample-based phrases, rests and a tick, with tempo and transposition experiments. Patterns cover sample playback, one-shots and four-channel music. | Connect instrument/sample creation, listening choices and resource costs into the progression; a player skeleton is not a complete tracker course. |
| Performance | Meteor Storm units 06–08 develop interrupts and clocks; unit 20 compares render scheduling and measured frame budgets. The BASIC revisit plan already defines a careful measurement protocol. Audio patterns name some PAL/NTSC assumptions and pitch tables. | Join these foundations to audio workload experiments, period instrumentation and modern profiling. Naming a region is not a taught regional comparison. |
| Shared resources | Cross-platform `audio/making-a-sound.mdx` and `audio/tune-sequencer.mdx` compare sound models and playback data. Vault entries include sound drivers, interrupt-driven music, beeper music and tracker culture. Sound and Music is an agreed Craft home, with no authored shared lesson sequence recorded in the coverage map. | Build connections rather than another parallel plan. Review sweeping “every driver”, “free”, hardware-ranking and blanket beeper-blocking claims before reuse. Some Vault entries are explicitly marked `reviewed: false`; their presence does not certify their claims. |

The main gap is a connected progression that gives musical understanding,
instrument creation, creative judgement and performance diagnosis the same care
as implementing a working effect. Existing material is a starting point to assess
and improve, not an instruction to discard it or rewrite the whole curriculum.
The bounded next implementation proposal belongs in [current work](../work.md#audio-and-performance).
