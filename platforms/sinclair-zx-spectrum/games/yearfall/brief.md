# Yearfall — Brief

**Title (working):** Yearfall
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 7 of 8 (slot 15)
**Headline concept:** Consequences — choices land later
**Embedded concept:** Trade-offs — every allocation sacrifices something else
**Topics:** 10 topics, ~10–14 hours
**Constraint position:** period-faithful

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach that game state persists and compounds across turns — decisions made in year 1 shape what is possible in year 5 — so the learner arrives at Crates understanding that game mechanics create consequences, not just immediate results.

---

## 2. Classic Ancestors

- **Hamurabi** (Doug Dyment, 1968; popularised by David Ahl, 1973) — the resource-management simulation. Rule a kingdom: allocate grain to feeding, planting, and land. Population grows or starves. Harvests vary. The mechanic: year-by-year allocation with compounding consequences.
- **Kingdom** / **Santa Paravia** — the lineage of text-based kingdom simulators in BASIC, published in every home-computer magazine and in Ahl's *BASIC Computer Games* (1978).

---

## 3. Core Experience

You rule a small domain. Each year you allocate resources: how much grain to feed your people, how much to plant, how much land to buy or sell. A harvest comes — good or bad, partially random. Your people grow or starve based on your choices *last* year. The pleasure is in watching a kingdom thrive through careful management — and the dread of watching it collapse when a bad harvest compounds a bad decision.

---

## 4. Visual Direction

- DRAW castle silhouette on title screen — two towers (DRAW rectangles + triangle roofs) connected by wall (horizontal DRAW). Simple, immediately says "kingdom." ~8 DRAW commands.
- INVERSE header bar: "*** YEARFALL ***  Year: N". Block-graphic divider between status and input areas.
- **Population bar** — row of CHR$ 143 (solid blocks) in INK 4 (green), length proportional to population. Shrinks on starvation, grows on births. The player SEES the population, not just reads a number.
- **Starvation alarm** — brief BORDER 2 (red) flash when people die. Like an alarm. ~1 line.
- Year-end report: block-graphic coloured bars for metrics (green harvest, red starvation, cyan births). Mini Dice Roller style visualisation per year.
- Austere palette maintained — this is a game about scarcity.

---

## 5. Audio Direction

- **Good harvest.** Ascending tone.
- **Bad harvest.** Descending tone.
- **Starvation.** A harsh low buzz — people died.
- **Year transition.** A brief neutral tone marking the new year.

---

## 6. Level Design Direction

- **Content source:** No DATA — all state is computed from player choices and random events.
- **Difficulty curve.** Early years are forgiving — the starting conditions are comfortable. By year 5–10, one bad harvest can trigger a crisis. The compounding effect of decisions *is* the difficulty curve.
- **Scale:** 10 years per game. A session lasts 10–15 minutes.
- **Pacing.** Each year is one turn: read state → allocate → see results. The cycle is fast enough to feel like a rhythm but slow enough to think.
- **Onboarding.** Year 1 starts with ample resources — the player can allocate badly and still survive. Year 2's report shows the consequences clearly.

---

## 7. Anti-goals

- No military or combat — pure resource management. War mechanics add complexity without teaching the design concept.
- No technology tree — resources are grain, land, and people. Three variables, deeply intertwined.
- No random events beyond harvest variation — famine is a consequence of decisions, not of dice.
- No win state — the game runs 10 years. The score is the final population. The player *manages*, they do not *win*.
- Maximum ~50 lines of BASIC.

---

## 8. Topic Progression

1. **The kingdom.** Variables for population, grain, and land. PRINT a status report: "Year 1. Population: 100. Grain: 2800. Land: 1000 acres." **New:** multiple state variables representing a simulation. **Program:** ~6 lines.

2. **Feeding the people.** INPUT: how much grain to feed? Each person needs 20 grain per year. If you feed less, people starve. Calculate deaths: `LET deaths = INT((pop - grain_fed / 20))`. **New:** allocation as a player decision, consequences computed from input. **Program:** ~12 lines.

3. **Planting.** INPUT: how many acres to plant? Each acre needs 1 unit of grain to seed and 1 person to farm. The player must balance planting against feeding — grain spent on seed cannot feed people. **New:** competing resource demands (the trade-off). **Program:** ~18 lines.

4. **The harvest.** Yield is partially random: `LET yield = INT(RND * 6) + 1` bushels per acre planted. Total harvest adds to grain. A good yield (5–6) rewards planting; a bad yield (1–2) punishes it. **New:** random variation on a player decision, amplifying or punishing risk. **Program:** ~22 lines.

5. **The year cycle.** Wrap in a FOR loop: 10 years. Each iteration: display status → feed → plant → harvest → compute births/deaths → update state. The game now plays from year 1 to year 10. **New:** a multi-turn simulation loop with compounding state. **Program:** ~28 lines.

6. **Population growth.** Births depend on feeding: well-fed populations grow (e.g., 3% natural growth if everyone fed), starving populations shrink. The player sees the delayed consequence: starving in year 3 means fewer workers in year 4, which means less planting, which means less harvest in year 5. **New:** compound consequences (feedback loop across turns). **Program:** ~32 lines.

7. **Buying and selling land.** INPUT: buy or sell acres? Buying costs grain; selling provides grain. Land is a long-term investment — more land means more planting capacity, but the grain cost is immediate. **New:** investment decisions (spend now for future returns). **Program:** ~38 lines.

8. **End-of-game score.** After year 10, evaluate: final population vs starting population. A rating: population doubled is "Wise ruler", stayed steady is "Competent", halved is "The people suffer", collapsed is "Disaster." **New:** final evaluation of long-term management. **Program:** ~42 lines.

9. **Year-by-year report.** At each year's end, display births, deaths, harvest yield, grain consumed — not just the new state. The report shows *why* the state changed, not just *what* changed. **New:** event log as explanation (the player sees cause and effect). **Program:** ~46 lines.

10. **Make it yours.** Title screen ("*** YEARFALL ***"). Colour the reports — green years (population grew), red years (population fell). The design lesson: every allocation was a trade-off. Feeding more meant planting less. Buying land meant less grain now. **Consequences** compound — year 1's choice shapes year 10's outcome. **New:** none (polish + design reflection). **Program:** ~50 lines.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] Starvation correctly computed from feeding vs population
- [ ] Planting correctly constrained by grain and population
- [ ] Harvest yield varies randomly within a reasonable range
- [ ] Population growth/decline compounds correctly across years
- [ ] Land buying/selling correctly adjusts grain and land
- [ ] 10-year loop completes and shows final evaluation
- [ ] Player cannot allocate more grain/land than they have
- [ ] British English throughout
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **framework** — multi-turn simulation loop: state → decision → outcome → update → repeat. The pattern behind every management game, every turn-based strategy. Cross-platform.
- **framework** — compound consequences: decisions in turn N affect the state in turn N+1, which constrains decisions in turn N+2. The design pattern that creates depth from simple mechanics.
- **basic** — allocation-with-constraint: INPUT a value, validate against available resources, compute the remainder. The pattern behind every budget, inventory, and resource screen.

---

## 11. Vault Tie-ins

- **Hamurabi** (Doug Dyment, 1968) — the original kingdom resource manager.
- **David Ahl** — *BASIC Computer Games* (1978), which popularised Hamurabi for the home-computer generation.
- **Resource management** — the design principle that competing demands on finite resources create meaningful decisions.
