# Commodore 64 — Getting the ROMs

**Purpose:** Explain to learners why the C64 needs system ROMs, and how to obtain them legally
**Audience:** C64 curriculum learners (and curriculum authors writing setup copy)
**Last Updated:** 2026-06-02

---

## A note on ROMs

To run anything on a C64 — real or emulated — you need the machine's **system ROMs**: the built-in
software (the KERNAL, BASIC, and character ROM) that makes the machine a machine. An emulator
without them is an empty shell.

Here's the honest part. **This course is free, and always will be — but the ROMs aren't ours to give
away.** They're still owned (today, by a company called Cloanto, who've kept these platforms legally
alive for decades), and we're not going to hand out copies of someone else's work to save you a
step. Preserving these machines *properly* — with respect for the people and the history behind them
— is the whole point of this project. Quietly pirating the ROMs would rather undercut that.

So you'll bring your own. It's cheaper and easier than it sounds, and you only do it once.

## Your options

Pick whichever fits you:

1. **Want it to just work? — C64 Forever.** Cloanto's [C64 Forever](https://www.c64forever.com/)
   (Plus edition, ~$10) gives you every official ROM, legally, in a couple of clicks. The simplest
   path if you don't have real hardware — and you're buying from the people who preserved them.
2. **Own a real C64?** Dump the KERNAL, BASIC and character ROMs from it — they're already yours.
3. **Want it completely free? — OpenROMs.** The community's open-source KERNAL/BASIC replacements
   ([OpenROMs](https://github.com/MEGA65/open-roms)) are free to use. Great for the **assembly**
   track — but their BASIC isn't finished, so the **BASIC** lessons will hit gaps. Use OpenROMs for
   assembly; use a real BASIC ROM for the BASIC track.

## In the in-browser playground

C64 assembly examples run instantly (we use the open ROMs). For C64 BASIC, you'll drop in your own
ROM the first time — it stays in your browser and never touches our servers.

---

*Binding decision: [`198x/decisions/system-rom-sourcing.md`](../../../../decisions/system-rom-sourcing.md).
Live learner-facing version: [`/setup/roms`](https://code198x.com/setup/roms).*
