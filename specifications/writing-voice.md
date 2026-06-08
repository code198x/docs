# Writing Voice

The editorial voice across all Code198x content. Formal principles are in `docs/CONTENT-CREATION-WORKFLOW.md`; this captures the lived experience of applying them.

## The voice

**Magazine-class, not academic.** Specifically: the British 80s gaming press — *Crash*, *Zzap!64*, *Your Sinclair*, *ACE*, *The One*, *Computer + Video Games*. Warm, technical, opinionated, sometimes funny, written by enthusiasts for enthusiasts. Lloyd Mangram's tone, not a textbook author's.

The reader is curious, possibly young, possibly returning to coding after years away. Trust them to be smart. Don't assume they already know what a register is. Don't talk down to them either. It's the same balance the magazines hit: a 14-year-old in 1986 could read *Crash* and learn what a sprite was without feeling lectured.

**Never:** "highbrow academic bullshit" (per the brief). No passive voice walls of text. No "as we discussed in the previous chapter." No tutorial-mill robotic prose.

**Always:** the reader is a participant, not an audience. We're explaining something we love to someone who might love it too.

## Core qualities

- **Hardware intimacy**: show the register, the memory address, the signal. Don't hide behind abstractions.
- **Game-first pedagogy**: every concept taught through building a game. No isolated theory.
- **Honest about difficulty**: don't pretend it's easy. Acknowledge the learning curve.
- **Encouraging experimentation**: "try changing this value and see what happens" is a legitimate teaching tool.

## Language rules

- **British English** throughout: colour, learnt, centre, behaviour
- **Exception**: "program" not "programme" (for computer programs)
- **No nostalgia tourism**: focus on skills and hardware, not "remember when" feelings
- **No modern engine references**: zero tolerance for Unity, Unreal, Godot, GameMaker

## Anti-patterns

- Dense academic walls of text
- Slick startup aesthetic
- Gaudy vaporwave
- "Remember when" nostalgia framing
- Condescending simplification ("don't worry about this for now")
- Tutorial-mill robotic prose ("In this lesson, we will learn how to...")
- Over-explaining what the reader can see for themselves
- Hedging ("might possibly perhaps consider...")

## Reference reads

When stuck on a section, read a paragraph of:

- A *Crash* game review — the rhythm of opinion + technical detail
- An Oli Frey-era *Crash* hardware feature — explaining a chip without dumbing it down
- A *Zzap!64* type-in introduction — warm but expectant
- An old Usborne computer book — the "you can do this" framing for kids and adults alike

If your sentence sounds like a Wikipedia article, rewrite it.

## Tonal calibration by track

- **Assembly tracks** — *Crash* / *Zzap!64* hardware features. Technical, opinionated, treats the chip as a character. Aimed at 16+ year olds and serious returners.
- **BASIC track** — Usborne 1984 confidence-builder, *with* magazine wit. Aimed at kids, beginners, people-who-haven't-coded-in-years. Same voice, gentler ramp. Confidence over depth. (See [spectrum-basic-32-games.md](../decisions/spectrum-basic-32-games.md) for the BASIC scope decisions that drive this calibration.)
- **Vault** — magazine retrospective. Like a *Retro Gamer* feature but tighter. Treats games and people as worth caring about.

## Three quality criteria

Every unit must meet all three:

1. **It Works Fast** — immediate visible/audible feedback, creates something impressive
2. **It's Real** — hardware connection visible, honest about limitations
3. **It's Clear** — focused concept, builds logically, invites experimentation

## Visual identity

Platform-specific branding:
- **C64**: blue
- **Spectrum**: rainbow
- **NES**: red
- **Amiga**: orange
