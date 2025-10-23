# Phase 1 Curriculum: 6502 Assembly + Hardware Fundamentals (Lessons 1-512)

> **⚠️ STRUCTURED:** This curriculum uses granular documentation files for better organization and context efficiency.

## Primary Documentation

**Start here:** [`phase-1/overview.md`](phase-1/overview.md)

This provides the Phase 1 overview with philosophy, structure, and learning outcomes for assembly-first NES development.

## Detailed Documentation

| What you need | Where to find it |
|---------------|------------------|
| **Tier 1 details** (Pong, L1-32) | [`phase-1/tier-1/README.md`](phase-1/tier-1/README.md) |
| **Tier 2 details** (Breakout, L33-64) | [`phase-1/tier-2/README.md`](phase-1/tier-2/README.md) |
| **Tier 3 details** (Space Invaders, L65-96) | [`phase-1/tier-3/README.md`](phase-1/tier-3/README.md) |
| **Tier 4 details** (Galaxian, L97-128) | [`phase-1/tier-4/README.md`](phase-1/tier-4/README.md) |
| **Tier 5 details** (Pac-Man, L129-160) | [`phase-1/tier-5/README.md`](phase-1/tier-5/README.md) |
| **Tier 6 details** (Donkey Kong, L161-192) | [`phase-1/tier-6/README.md`](phase-1/tier-6/README.md) |
| **Tier 7 details** (Mario Bros., L193-224) | [`phase-1/tier-7/README.md`](phase-1/tier-7/README.md) |
| **Tier 8 details** (Excitebike, L225-256) | [`phase-1/tier-8/README.md`](phase-1/tier-8/README.md) |
| **Tier 9 details** (Balloon Fight, L257-288) | [`phase-1/tier-9/README.md`](phase-1/tier-9/README.md) |
| **Tier 10 details** (Ice Climber, L289-320) | [`phase-1/tier-10/README.md`](phase-1/tier-10/README.md) |
| **Tier 11 details** (Advanced Scrolling, L321-352) | [`phase-1/tier-11/README.md`](phase-1/tier-11/README.md) |
| **Tier 12 details** (APU Mastery, L353-384) | [`phase-1/tier-12/README.md`](phase-1/tier-12/README.md) |
| **Tier 13 details** (Mapper Basics, L385-416) | [`phase-1/tier-13/README.md`](phase-1/tier-13/README.md) |
| **Tier 14 details** (Advanced Graphics, L417-448) | [`phase-1/tier-14/README.md`](phase-1/tier-14/README.md) |
| **Tier 15 details** (Complete Game, L449-480) | [`phase-1/tier-15/README.md`](phase-1/tier-15/README.md) |
| **Tier 16 details** (Mastery Project, L481-512) | [`phase-1/tier-16/README.md`](phase-1/tier-16/README.md) |
| **Individual lesson specs** | [`phase-1/tier-{1-16}/lesson-NNN.md`](phase-1/) |

## Why This Structure?

**Organized by tier and lesson**

**Benefits:**
- **60-70% less context** when working on specific lessons
- **Better organization** with clear hierarchy (phase → tier → lesson)
- **Easier navigation** to find specific game or concept
- **Scalable** for all phases and platforms

## NES-Specific Features

This curriculum highlights the NES's unique characteristics:

- **Assembly-first approach** - No BASIC layer, direct 6502 programming
- **PPU programming** - Tile-based graphics with 64 hardware sprites
- **VBlank synchronization** - 60fps timing through NMI interrupts
- **OAM sprite system** - Hardware-accelerated sprite rendering
- **APU audio** - 5-channel sound (2 pulse, triangle, noise, DMC)
- **Cartridge development** - ROM-based programming with mappers
- **Dedicated gaming hardware** - Purpose-built console architecture

## Navigation

- **View all phases:** [`./`](./)
- **Hardware references:** Coming soon (6502, PPU, APU, mapper specs)
- **Documentation index:** [`../START-HERE.md`](../START-HERE.md)

---

**Last updated:** 2025-10-23
**Version:** 2.0
**Status:** Tier 1 overview and sample lesson complete, remaining tiers to be detailed
