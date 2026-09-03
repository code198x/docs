# Decision: routes to a destination

A learner arrives wanting to build a particular kind of game. The curriculum shows them the road to it, with the destination named from the first day.

## The decision

Every module declares what it depends on. The **route** to a module is the transitive closure of those dependencies, and the site renders it as the path from where a learner is to the game they came for.

```yaml
  - number: 16
    slug: crates
    name: Crates
    requires:
      - module: sonar
        thread: Reading a world
        why: two-dimensional arrays — a grid you can read
      - module: touchdown
        thread: Moving in real time
        why: the continuous game loop — things that move on their own
      - module: cipher
        thread: Where the data lives
        why: DATA as a content list — where level layouts come from
```

The catalogue order stays the recommended path. Nothing here lets a learner skip anything. What changes is that the order stops being an unexplained queue and becomes a route with a visible destination and a stated reason for every step.

## Why

Two motivations, and they are the same one seen from either end: a learner wants to build the game that appeals to them **now**, and a learner arrives with a genre in mind. Both are answered by "here is the road, and here is what each step earns you" — neither needs free choice.

Free choice was considered and rejected, because it costs more than it looks. The expensive part is not repetition; it is that **contrastive teaching stops working**. From game three onward the prose teaches by deprecation pair — *"In Story Builder and Oracle Stone, `PAPER` set a background colour that stayed put for the whole program. Here it changes during the program."* Read cold, that degrades from an insight to a statement. The mechanism is [deprecation-pairs.md](deprecation-pairs.md), it is load-bearing, and it depends on the order holding.

The route model keeps it and solves the motivation problem anyway.

**The dependencies are sparse, which is what makes this worth building.** Measured on the Spectrum BASIC track: the true route to *Crates*, game sixteen, is six games rather than fifteen — `story-builder → reflex → cipher → quiz-master → sonar → touchdown`. Ten of the sixteen games are not on it. If routes were near-total the feature would be the queue with annotations; they are not.

The threads are in the catalogue already, not invented for the design:

```
arrays:     quiz-master → locksmith → sonar → three-in-a-row → the-caverns → crates
DATA:       cipher → quiz-master → three-in-a-row → the-caverns → crates
real-time:  reflex → touchdown → crates
strings:    story-builder → bright-spark → cipher
```

## What this does not change

Stated because a reader reasonably expects otherwise:

- **The ramp stands.** Complexity still rises gently and close to monotonically; the route is a view of the order, not a way around it.
- **The spiral and deprecation pairs stand** — see above; the route model exists partly to protect them.
- **Revisits stand.** A `pass: 2` module still continues its `pass: 1`.
- **No module becomes skippable.** A route omits games because they are genuinely unrelated to the destination, never because a prerequisite was waived.

## The data model

`requires` holds objects, not slugs: a module reference, the thread it belongs to, and why it is needed.

- **Two reference forms.** The object form above carries `thread` and `why` and is what a game-to-game edge uses. A bare string is shorthand for an edge with neither — used by the structural seam edges below, which are architecture rather than pedagogy and have no thread to belong to. `suggests` takes the same two forms.
- **Scope.** Bare references resolve within the same catalogue file — one platform, one track. A **qualified** reference (`foundations/numbers-and-bits`) crosses a scope and appears only at the seams below. Routes never cross systems.
- **Upstream is declared once, not per module.** Every game in a track sits behind General Programming, the machine briefing and the language on-ramp. That chain is structural and identical for all ~90 modules, so encoding it per module would be ninety chances to drift. Each seam edge is stated exactly once and reached transitively:

  ```
  foundations/numbers-and-bits        requires  general-programming
  foundations/from-source-to-silicon  requires  numbers-and-bits
  craft/maths-for-games               requires  foundations/numbers-and-bits

  {system}/machine/meet-the-machine   requires  foundations/general-programming
  {system}/basic/meet-basic           requires  {system}/machine/meet-the-machine
  {system}/assembly/meet-assembly     requires  {system}/machine/meet-the-machine
                                            +   foundations/from-source-to-silicon
  ```

- **Revisits are derived, never authored.** A module with `game: gloaming, pass: 2` requires the `pass: 1` module of the same game by definition. Deriving it from fields that already exist means it cannot rot.
- **Empty `requires` means an entry point.** The genre-distinct starting games are not designed separately; they fall out, and the site can list exactly those.
- **`suggests` is the second, non-gating edge.** Some relationships are "once you have done this, go here", and modelling them as prerequisites would rebuild gates the curriculum deliberately does not want:
  - the BASIC games suggest `foundations/from-source-to-silicon` — the bridge, reached as an answer once games have raised the question, never as a gate ([front-of-curriculum-architecture.md](front-of-curriculum-architecture.md))
  - game modules suggest `craft/game-feel`, whose real prerequisite is a game of yours running, which is not a module at all

- **Coming-soon modules participate fully.** The destination is usually the game that does not exist yet — that is the genre-pull case. Unbuilt steps render marked.

### Foundations and The Craft need catalogues first

They have none. Their modules are bare `index.mdx` files and their order lives in a hardcoded array in a page component:

```js
// src/pages/foundations.astro
const ORDER = ['general-programming', 'numbers-and-bits', 'from-source-to-silicon'];
```

That already sits outside [state-lives-in-catalogues.md](state-lives-in-catalogues.md), which makes `modules/*.yaml` authoritative. `foundations.yaml` (3 modules) and `craft.yaml` (2) come first — worth doing whether or not routes ship, and the seam edges above have nowhere to live until they exist.

They join the existing `modules` collection rather than a new one, since they carry the same fields. The schema's `platform` and `track` become a union with `section`: a file supplies either the platform/track pair or a section slug, never both. That keeps one loader, one route helper and one validator across the whole curriculum, and it matches the layout the router already branches on — a section's content is `{section}/{module}/unit-NN`, one level shallower than a platform's.

## What the learner sees

**On a module page — the threads.** The route grouped by the capability each line builds, converging on the destination. Six games read as three capabilities rather than a queue of six, and the grouping matches the structure the catalogue already has. Below about two threads it degrades to a plain ordered ladder, because a thread of one reads as a bug.

**On a track page — the map.** The whole track with the route lit and the rest dimmed. This is the only view that shows what a learner is *not* being asked to do, and that is the answer to "is this a curriculum or a queue".

Every step carries its `why`. Those lines are the load-bearing text of the whole feature — a route without them is a list of names.

## Edges are a design tool, not only a description

For a game that exists, `requires` records what it depends on. For a game that does not, the same field states what it is *for* — which thread it extends, and what it earns a learner who arrives having played the games before it. Written that way it is a design brief, and it is a sharper one than a tagline, because it forces the question a lineup rarely asks out loud: what can this game do that the ones before it could not?

This is the honest answer to authoring edges on unbuilt modules. Guessing at a coming-soon game's dependencies is worthless — the guess would be checked against nothing. **Deciding** them while designing the game is the opposite: the edge is a commitment the game is then built to honour, and the build check keeps the lineup's order and its dependencies agreeing as both move.

A new game whose edges cannot be written is a game whose purpose in the sequence has not been decided yet. That is worth knowing before it is authored rather than after.

## Validation

`scripts/check-curriculum-routes.mjs`, run in `npm run build` beside the existing `check-vault-*.mjs` scripts:

1. Every `requires` and `suggests` reference resolves — bare in scope, qualified across a seam.
2. No cycles.
3. **No forward references**, within a catalogue — a module may not require one later in the same file. Seam edges point at other catalogues and are exempt, since order across scopes is fixed by the architecture rather than by array position. This turns the gentle ramp from an intention into a property with a test.
4. Thread names are consistent within a track. A warning, not an error: `Reading a world` and `Reading the world` fragment the grouping silently.
5. Every module's route terminates at an entry point.

The report prints per-track columns — entry points, thread vocabulary, longest route — so an outlier across the four systems is visible. Consistency is reported, not enforced: the tracks genuinely differ, and no rule could say which difference was wrong.

**The feature is inert until edges are authored.** `requires` defaults to empty, so before a single edge exists every module is an entry point, every route is empty, and the site is unchanged. It lands structurally and populates track by track.

## Authoring order

1. `foundations.yaml` and `craft.yaml` — the seam, and the catalogue gap above.
2. **Spectrum BASIC** — seventeen complete games, the most mature track, and the one whose threads are already traced. The thread vocabulary should be discovered from finished content, not invented.
3. **Spectrum assembly** — a different shape, with revisits, exercising the derived-revisit rule.
4. C64, NES, Amiga, once the model holds on two tracks of different shape.

## Drift triggers

- Adding a `requires` edge to make a module feel important rather than because the destination genuinely needs it. A route is a claim about dependency, and a padded one is the queue returning in costume.
- Putting the bridge or Game Feel in `requires`. They are `suggests`; making either a prerequisite rebuilds a gate the curriculum removed on purpose.
- Repeating the upstream chain on individual game modules instead of reaching it through the track's on-ramp.
- Inventing thread names per module rather than reusing a track's small vocabulary.
- Authoring edges on an unbuilt game by guessing what it will teach, rather than deciding what it is for. A guess is checked against nothing; a decision is a commitment the game is built to honour.
- Reaching for a skill-level dependency graph before the module-level one has proved out. That is a normalised vocabulary across ninety modules and four systems, and it should be earned by evidence that module edges are too coarse.
- Hand-keeping an order list in a page component instead of a catalogue.

## Open

**The voice of the `why` lines.** *"DIM arrays — storage you reach by number"*, *"the continuous game loop — things that move on their own"* are placeholders. Settle the register on the first few Spectrum BASIC edges, on the page, then author the rest against it.

## Relates to

- [modules-not-games.md](modules-not-games.md) — module identity, `game`/`pass` revisits, order as catalogue data. Amended: re-ordering stays a data edit, now with the condition that it may not invert a dependency.
- [curriculum-structure.md](curriculum-structure.md) — the sequence and the gentle ramp this makes checkable.
- [deprecation-pairs.md](deprecation-pairs.md) — the contrastive teaching the linear order protects.
- [spiral-and-incremental.md](spiral-and-incremental.md) — why order carries pedagogical weight.
- [state-lives-in-catalogues.md](state-lives-in-catalogues.md) — why Foundations and The Craft need catalogues.
- [front-of-curriculum-architecture.md](front-of-curriculum-architecture.md) — the layers the seam edges encode, and the bridge.
