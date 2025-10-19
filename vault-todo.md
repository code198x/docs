# Vault Entry TODO

This file tracks references to games, programmers, companies, hardware, and concepts that need Vault entries created. Extract references here during lesson authoring, then batch-create entries later.

See [VAULT-WORKFLOW.md](VAULT-WORKFLOW.md) for complete guidelines.

---

## Priority Order

1. **Hardware** - Learners need register references immediately
2. **Concepts** - Techniques referenced across multiple lessons
3. **Games/People** - Historical context enriches but isn't blocking
4. **Companies/Publications** - Background context, lowest priority

---

## Hardware

### VIC-II Chip
- **Category:** Hardware
- **Referenced in:** Phase 0, Tier 2, Lesson 18 (sprites)
- **Status:** [ ] Not started
- **Notes:** Complete register reference needed for sprite, color, screen memory

### SID Chip
- **Category:** Hardware
- **Referenced in:** Phase 0, Tier 2, Lesson 22 (sound)
- **Status:** [ ] Not started
- **Notes:** Three-voice synthesizer, ADSR envelopes, filters

### CIA Chip
- **Category:** Hardware
- **Referenced in:** Phase 0, Tier 2, Lesson 20 (joystick)
- **Status:** [ ] Not started
- **Notes:** I/O ports, timers, joystick reading at $DC00/$DC01

---

## Concepts

### Sprite Multiplexing
- **Category:** Concept
- **Referenced in:** Phase 0, Tier 3, Lesson 35 (advanced sprites)
- **Status:** [ ] Not started
- **Pioneers:** Andrew Braybrook
- **Example games:** Uridium (1986), Mayhem in Monsterland (1993)
- **Notes:** Reusing 8 hardware sprites via raster interrupts

---

## Games

### Impossible Mission
- **Category:** Game
- **Programmer:** Dennis Caswell
- **Publisher:** Epyx
- **Released:** 1984
- **Referenced in:** Phase 0, Tier 2, Lesson 23 (joystick control)
- **Status:** [ ] Not started
- **Techniques:** Smooth joystick control, digitized speech
- **Notes:** "Stay a while... stay FOREVER!"

### Uridium
- **Category:** Game
- **Programmer:** Andrew Braybrook
- **Publisher:** Hewson Consultants
- **Released:** 1986
- **Referenced in:** Phase 0, Tier 3, Lesson 35 (sprite multiplexing)
- **Status:** [ ] Not started
- **Techniques:** Sprite multiplexing, smooth scrolling
- **Notes:** Showed 20+ sprites using only 8 hardware sprites

---

## People

### Andrew Braybrook
- **Category:** Person
- **Born:** Unknown (research needed)
- **Companies:** Hewson Consultants
- **Notable works:** Uridium (1986), Paradroid (1985), Morpheus (1987)
- **Referenced in:** Phase 0, Tier 3, Lesson 35 (sprite multiplexing)
- **Status:** [ ] Not started
- **Innovations:** Sprite multiplexing technique
- **Notes:** One of the C64's most respected programmers

### Dennis Caswell
- **Category:** Person
- **Born:** Unknown (research needed)
- **Companies:** Epyx
- **Notable works:** Impossible Mission (1984)
- **Referenced in:** Phase 0, Tier 2, Lesson 23 (joystick control)
- **Status:** [ ] Not started
- **Notes:** Created one of the C64's most iconic games

### Bob Yannes
- **Category:** Person
- **Born:** 1957
- **Companies:** Commodore (1981-1984), Ensoniq (co-founder)
- **Notable works:** SID chip design
- **Referenced in:** Phase 0, Tier 2, Lesson 22 (sound)
- **Status:** [ ] Not started
- **Innovations:** Designed the SID sound chip
- **Notes:** Left Commodore frustrated management didn't understand what they had

---

## Companies

### Hewson Consultants
- **Category:** Company
- **Founded:** 1980s (research exact date)
- **Closed:** Unknown (research needed)
- **Key people:** Andrew Hewson (founder)
- **Notable releases:** Uridium, Paradroid, Cybernoid series
- **Referenced in:** Phase 0, Tier 3, Lesson 35
- **Status:** [ ] Not started
- **Notes:** Known for high-quality C64 games

### Epyx
- **Category:** Company
- **Founded:** 1978
- **Closed:** 1989 (bankruptcy)
- **Notable releases:** Impossible Mission, Summer Games series
- **Referenced in:** Phase 0, Tier 2, Lesson 23
- **Status:** [ ] Not started
- **Notes:** California-based publisher, strong C64 catalog

---

## Publications

### Zzap!64
- **Category:** Publication
- **First issue:** May 1985
- **Last issue:** 1992
- **Publisher:** Newsfield Publications
- **Key editors:** Roger Kean, Julian Rignall
- **Referenced in:** (Future lessons on C64 scene/history)
- **Status:** [ ] Not started
- **Notes:** Most influential C64 magazine in UK

---

## Events

### Commodore 64 UK Release
- **Category:** Event
- **Date:** September 1982
- **Location:** United Kingdom
- **Price:** £399
- **Referenced in:** (Future historical context lessons)
- **Status:** [ ] Not started
- **Notes:** Followed January 1982 US release ($595)

### Commodore Bankruptcy
- **Category:** Event
- **Date:** April 29, 1994
- **Participants:** Commodore International
- **Referenced in:** (Future lessons on C64 legacy)
- **Status:** [ ] Not started
- **Notes:** Company that made home computing affordable couldn't adapt to PC era. Brand spent decades being asset-stripped.

---

## Batch Creation Notes

When creating entries in batches:

1. **Research temporal data** - Get precise dates from Wikipedia, MobyGames, etc.
2. **Group by category** - Write all game entries together, all people entries together
3. **Maintain tone** - Energetic storytelling, not dry encyclopedia
4. **Cross-link bidirectionally** - Games link to programmers, programmers link to games
5. **Update global timeline** - Add events to `/vault/timeline` if it exists

---

## Template for New References

```markdown
### [Entry Name]
- **Category:** Hardware|Game|Person|Company|Event|Publication|Concept
- **[Category-specific fields]:** [Values]
- **Referenced in:** Phase X, Tier Y, Lesson ZZ (context)
- **Status:** [ ] Not started | [ ] In progress | [x] Complete
- **Notes:** [Anything important to remember]
```
