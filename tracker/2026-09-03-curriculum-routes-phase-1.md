# Curriculum Routes — Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every curriculum module a declared dependency graph, validated at build time, that ships without changing a single page of the site.

**Architecture:** The `modules` content collection gains optional `requires` and `suggests` edges, and its `platform`/`track` pair becomes an alternative to a `section` slug so Foundations and The Craft can live in the same collection. A pure resolver in `src/lib/routes.ts` computes a route from plain data — no Astro imports — so both the site and a build-time check script consume one implementation. Node 24 strips TypeScript natively, so the `.mjs` check script imports the `.ts` resolver directly.

**Tech Stack:** Astro content collections, Zod, TypeScript, Vitest, Node 24.

**Spec:** `Code198x/docs/decisions/curriculum-routes.md`

**Repo:** all paths are relative to `Code198x/website/`.

## Global Constraints

- British English, except "program" for computer programs.
- `requires` and `suggests` both default to `[]`. The site must render identically when no edges exist anywhere.
- A reference is either a bare string (structural, no thread) or `{ module, thread?, why? }`.
- Bare references resolve within the same catalogue file. Qualified references (`foundations/numbers-and-bits`, `sinclair-zx-spectrum/machine/meet-the-machine`) cross a scope.
- The forward-reference rule applies within a catalogue only; seam edges across scopes are exempt.
- Errors exit non-zero: unresolved reference, cycle, in-scope forward reference, route that never terminates. Thread-name inconsistency is a warning and must not fail the build.
- Do not author any edges in this phase beyond the seam edges in Task 3. Populating tracks is content work.

---

### Task 1: Schema — sections and edges

**Files:**
- Modify: `src/content.config.ts:452-473` (the `modules` collection)

**Interfaces:**
- Produces: module entries may carry `requires: RouteRefRaw[]` and `suggests: RouteRefRaw[]`, where `RouteRefRaw = string | { module: string; thread?: string; why?: string }`. A catalogue file carries either `platform` + `track`, or `section`.

- [ ] **Step 1: Replace the `modules` collection schema**

Replace the whole `const modules = defineCollection({...});` block with:

```ts
// A dependency edge. A bare string is a structural reference with no thread —
// used by the seam edges between sections and tracks. The object form carries
// the thread it belongs to and why it is needed, and is what a game-to-game
// edge uses. See docs/decisions/curriculum-routes.md
const routeRef = z.union([
  z.string(),
  z.object({
    module: z.string(),
    thread: z.string().optional(),
    why: z.string().optional(),
  }),
]);

// Curriculum catalogue: either a platform track (platform + track) or a
// cross-platform section (section). Never both — a section has no language
// track, and its content sits one level shallower on disk.
const modules = defineCollection({
  loader: glob({ pattern: '**/*.yaml', base: 'src/content/modules' }),
  schema: z.object({
    platform: z.string().optional(),
    track: z.enum(['assembly', 'basic', 'amos', 'blitz', 'machine']).optional(),
    section: z.enum(['foundations', 'craft']).optional(),
    modules: z.array(z.object({
      number: z.number(),
      slug: z.string(),
      name: z.string(),
      kind: z.enum(['game', 'teaching', 'interval']).default('game'),
      game: z.string().optional(),
      pass: z.number().optional(),
      tagline: z.string(),
      skills: z.array(z.string()),
      status: z.enum(['in-progress', 'coming-soon', 'complete']),
      thumbnail: z.string().optional(),
      phase: z.string().optional(),
      requires: z.array(routeRef).default([]),
      suggests: z.array(routeRef).default([]),
    })),
  }).refine(
    (d) => (d.section != null) !== (d.platform != null && d.track != null),
    { message: 'A catalogue needs either section, or both platform and track — never both and never neither.' },
  ),
});
```

- [ ] **Step 2: Verify the existing catalogues still validate**

Run: `npx astro sync`
Expected: completes with no schema errors. Every existing `<platform>/<track>.yaml` has `platform` and `track` and no `section`, so the refine passes.

- [ ] **Step 3: Verify the site still builds**

Run: `CODE_SAMPLES_PATH=../code-samples npm run build`
Expected: PASS, and the page count is unchanged from before the edit.

- [ ] **Step 4: Commit**

```bash
git add src/content.config.ts
git commit -m "Let a catalogue describe a section, and carry dependency edges"
```

---

### Task 2: The route resolver

**Files:**
- Create: `src/lib/routes.ts`
- Create: `src/lib/routes.test.ts`

**Interfaces:**
- Consumes: nothing from Task 1 at runtime — this module is pure and takes plain objects, so it tests without Astro.
- Produces:
  - `type RouteRefRaw = string | { module: string; thread?: string; why?: string }`
  - `interface RouteModule { slug: string; name: string; requires?: RouteRefRaw[]; suggests?: RouteRefRaw[]; game?: string; pass?: number }`
  - `interface Scope { id: string; modules: RouteModule[] }`
  - `normaliseRef(ref: RouteRefRaw, defaultScope: string): { scope: string; slug: string; thread?: string; why?: string }`
  - `derivedRequires(scope: Scope, module: RouteModule): RouteRefRaw[]`
  - `resolveRoute(scopes: Scope[], scopeId: string, slug: string): RouteStep[]` where `RouteStep = { scope: string; slug: string; name: string; thread?: string; why?: string }`
  - `findCycle(scopes: Scope[]): string[] | null`
  - `forwardReferences(scope: Scope): Array<{ from: string; to: string }>`
  - `unresolvedReferences(scopes: Scope[]): Array<{ from: string; ref: string }>`
  - `threadVocabulary(scope: Scope): Map<string, number>`

- [ ] **Step 1: Write the failing tests**

Create `src/lib/routes.test.ts`:

```ts
import { describe, expect, it } from 'vitest';
import {
  normaliseRef,
  derivedRequires,
  resolveRoute,
  findCycle,
  forwardReferences,
  unresolvedReferences,
  threadVocabulary,
  type Scope,
} from './routes';

/** A track shaped like Spectrum BASIC's real dependency threads. */
const basic: Scope = {
  id: 'sinclair-zx-spectrum/basic',
  modules: [
    { slug: 'meet-basic', name: 'Meet BASIC', requires: ['sinclair-zx-spectrum/machine/meet-the-machine'] },
    { slug: 'story-builder', name: 'Story Builder' },
    { slug: 'reflex', name: 'Reflex' },
    { slug: 'cipher', name: 'Cipher', requires: [{ module: 'story-builder', thread: 'Where the data lives', why: 'variables that hold words' }] },
    { slug: 'sonar', name: 'Sonar', requires: [{ module: 'cipher', thread: 'Reading a world', why: 'arrays you reach by number' }] },
    { slug: 'crates', name: 'Crates', requires: [
      { module: 'sonar', thread: 'Reading a world', why: 'a grid you can read' },
      { module: 'reflex', thread: 'Moving in real time', why: 'the keyboard, live' },
    ] },
  ],
};

const machine: Scope = {
  id: 'sinclair-zx-spectrum/machine',
  modules: [{ slug: 'meet-the-machine', name: 'Meet the Machine' }],
};

describe('normaliseRef', () => {
  it('reads a bare string as a reference in the default scope', () => {
    expect(normaliseRef('sonar', 'sinclair-zx-spectrum/basic'))
      .toEqual({ scope: 'sinclair-zx-spectrum/basic', slug: 'sonar' });
  });

  it('splits a qualified string on its last segment', () => {
    expect(normaliseRef('foundations/numbers-and-bits', 'sinclair-zx-spectrum/basic'))
      .toEqual({ scope: 'foundations', slug: 'numbers-and-bits' });
  });

  it('keeps a multi-segment scope intact', () => {
    expect(normaliseRef('sinclair-zx-spectrum/machine/meet-the-machine', 'x'))
      .toEqual({ scope: 'sinclair-zx-spectrum/machine', slug: 'meet-the-machine' });
  });

  it('carries thread and why through the object form', () => {
    expect(normaliseRef({ module: 'sonar', thread: 'Reading a world', why: 'a grid' }, 'basic'))
      .toEqual({ scope: 'basic', slug: 'sonar', thread: 'Reading a world', why: 'a grid' });
  });
});

describe('derivedRequires', () => {
  it('makes a revisit require the previous pass of the same game', () => {
    const scope: Scope = { id: 't', modules: [
      { slug: 'gloaming', name: 'Gloaming', game: 'gloaming', pass: 1 },
      { slug: 'the-long-night', name: 'The Long Night', game: 'gloaming', pass: 2 },
    ] };
    const derived = derivedRequires(scope, scope.modules[1]);
    expect(derived).toEqual(['gloaming']);
  });

  it('derives nothing for a first pass', () => {
    const scope: Scope = { id: 't', modules: [
      { slug: 'gloaming', name: 'Gloaming', game: 'gloaming', pass: 1 },
    ] };
    expect(derivedRequires(scope, scope.modules[0])).toEqual([]);
  });

  it('derives nothing for a module with no game', () => {
    const scope: Scope = { id: 't', modules: [{ slug: 'meet-basic', name: 'Meet BASIC' }] };
    expect(derivedRequires(scope, scope.modules[0])).toEqual([]);
  });
});

describe('resolveRoute', () => {
  it('returns the transitive closure, dependencies before dependants', () => {
    const route = resolveRoute([basic, machine], 'sinclair-zx-spectrum/basic', 'crates');
    const slugs = route.map((s) => s.slug);
    expect(slugs).toEqual(['story-builder', 'cipher', 'sonar', 'reflex']);
  });

  it('omits modules that are not on the route', () => {
    const route = resolveRoute([basic, machine], 'sinclair-zx-spectrum/basic', 'crates');
    expect(route.map((s) => s.slug)).not.toContain('meet-basic');
  });

  it('crosses a scope seam', () => {
    const route = resolveRoute([basic, machine], 'sinclair-zx-spectrum/basic', 'meet-basic');
    expect(route).toEqual([
      { scope: 'sinclair-zx-spectrum/machine', slug: 'meet-the-machine', name: 'Meet the Machine' },
    ]);
  });

  it('returns an empty route for an entry point', () => {
    expect(resolveRoute([basic, machine], 'sinclair-zx-spectrum/basic', 'reflex')).toEqual([]);
  });

  it('visits a shared dependency once', () => {
    const scope: Scope = { id: 't', modules: [
      { slug: 'a', name: 'A' },
      { slug: 'b', name: 'B', requires: ['a'] },
      { slug: 'c', name: 'C', requires: ['a'] },
      { slug: 'd', name: 'D', requires: ['b', 'c'] },
    ] };
    const slugs = resolveRoute([scope], 't', 'd').map((s) => s.slug);
    expect(slugs.filter((s) => s === 'a')).toHaveLength(1);
    expect(slugs.indexOf('a')).toBeLessThan(slugs.indexOf('b'));
  });

  it('carries the thread and why of the edge that pulled a module in', () => {
    const route = resolveRoute([basic, machine], 'sinclair-zx-spectrum/basic', 'crates');
    const sonar = route.find((s) => s.slug === 'sonar');
    expect(sonar?.thread).toBe('Reading a world');
    expect(sonar?.why).toBe('a grid you can read');
  });
});

describe('findCycle', () => {
  it('returns null when the graph is acyclic', () => {
    expect(findCycle([basic, machine])).toBeNull();
  });

  it('names the modules in a cycle', () => {
    const scope: Scope = { id: 't', modules: [
      { slug: 'a', name: 'A', requires: ['b'] },
      { slug: 'b', name: 'B', requires: ['a'] },
    ] };
    const cycle = findCycle([scope]);
    expect(cycle).not.toBeNull();
    expect(cycle).toContain('t/a');
  });
});

describe('forwardReferences', () => {
  it('finds a module requiring one later in the same catalogue', () => {
    const scope: Scope = { id: 't', modules: [
      { slug: 'early', name: 'Early', requires: ['late'] },
      { slug: 'late', name: 'Late' },
    ] };
    expect(forwardReferences(scope)).toEqual([{ from: 'early', to: 'late' }]);
  });

  it('ignores an edge that crosses a scope', () => {
    expect(forwardReferences(basic)).toEqual([]);
  });
});

describe('unresolvedReferences', () => {
  it('reports a reference to a module that does not exist', () => {
    const scope: Scope = { id: 't', modules: [{ slug: 'a', name: 'A', requires: ['ghost'] }] };
    expect(unresolvedReferences([scope])).toEqual([{ from: 't/a', ref: 't/ghost' }]);
  });

  it('reports nothing when every reference resolves', () => {
    expect(unresolvedReferences([basic, machine])).toEqual([]);
  });

  it('checks suggests as well as requires', () => {
    const scope: Scope = { id: 't', modules: [{ slug: 'a', name: 'A', suggests: ['ghost'] }] };
    expect(unresolvedReferences([scope])).toEqual([{ from: 't/a', ref: 't/ghost' }]);
  });
});

describe('threadVocabulary', () => {
  it('counts how often each thread name is used', () => {
    const v = threadVocabulary(basic);
    expect(v.get('Reading a world')).toBe(2);
    expect(v.get('Moving in real time')).toBe(1);
  });
});
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `npx vitest run src/lib/routes.test.ts`
Expected: FAIL — `Failed to resolve import "./routes"`.

- [ ] **Step 3: Write the resolver**

Create `src/lib/routes.ts`:

```ts
/**
 * Curriculum routes — the road from where a learner is to the game they came for.
 *
 * Pure functions over plain data. No Astro imports, deliberately: the same
 * implementation serves the site and `scripts/check-curriculum-routes.mjs`, and
 * a resolver that needs a content collection can only be tested through one.
 *
 * See docs/decisions/curriculum-routes.md
 */

export type RouteRefRaw =
  | string
  | { module: string; thread?: string; why?: string };

export interface RouteModule {
  slug: string;
  name: string;
  requires?: RouteRefRaw[];
  suggests?: RouteRefRaw[];
  game?: string;
  pass?: number;
}

/** One catalogue file: a platform track (`{platform}/{track}`) or a section. */
export interface Scope {
  id: string;
  modules: RouteModule[];
}

export interface RouteRef {
  scope: string;
  slug: string;
  thread?: string;
  why?: string;
}

export interface RouteStep extends RouteRef {
  name: string;
}

/**
 * A bare string is a reference in `defaultScope` unless it carries slashes, in
 * which case the last segment is the slug and everything before it is the scope.
 * That keeps a scope id like `sinclair-zx-spectrum/machine` intact.
 */
export function normaliseRef(ref: RouteRefRaw, defaultScope: string): RouteRef {
  if (typeof ref === 'string') return splitQualified(ref, defaultScope);
  const { scope, slug } = splitQualified(ref.module, defaultScope);
  const out: RouteRef = { scope, slug };
  if (ref.thread !== undefined) out.thread = ref.thread;
  if (ref.why !== undefined) out.why = ref.why;
  return out;
}

function splitQualified(ref: string, defaultScope: string): RouteRef {
  const at = ref.lastIndexOf('/');
  if (at === -1) return { scope: defaultScope, slug: ref };
  return { scope: ref.slice(0, at), slug: ref.slice(at + 1) };
}

/**
 * A revisit continues the game its previous pass built, so it requires that
 * pass by definition. Derived rather than authored: a field that restates
 * `game` + `pass` is a field that can disagree with them.
 */
export function derivedRequires(scope: Scope, module: RouteModule): RouteRefRaw[] {
  if (!module.game || !module.pass || module.pass < 2) return [];
  const previous = scope.modules.find(
    (m) => m.game === module.game && m.pass === module.pass! - 1,
  );
  return previous ? [previous.slug] : [];
}

function allRefs(scope: Scope, module: RouteModule): RouteRef[] {
  const raw = [...derivedRequires(scope, module), ...(module.requires ?? [])];
  const seen = new Set<string>();
  const out: RouteRef[] = [];
  for (const ref of raw) {
    const n = normaliseRef(ref, scope.id);
    const key = `${n.scope}/${n.slug}`;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(n);
  }
  return out;
}

function lookup(scopes: Scope[], ref: RouteRef): { scope: Scope; module: RouteModule } | null {
  const scope = scopes.find((s) => s.id === ref.scope);
  const module = scope?.modules.find((m) => m.slug === ref.slug);
  return scope && module ? { scope, module } : null;
}

/**
 * The transitive closure of a module's requirements, dependencies first, each
 * shared module appearing once. The thread and why recorded against a step are
 * those of the edge that first pulled it onto the route.
 */
export function resolveRoute(scopes: Scope[], scopeId: string, slug: string): RouteStep[] {
  const start = lookup(scopes, { scope: scopeId, slug });
  if (!start) return [];

  const out: RouteStep[] = [];
  const done = new Set<string>();
  const active = new Set<string>();

  const visit = (ref: RouteRef): void => {
    const key = `${ref.scope}/${ref.slug}`;
    if (done.has(key) || active.has(key)) return;
    const found = lookup(scopes, ref);
    if (!found) return;
    active.add(key);
    for (const next of allRefs(found.scope, found.module)) visit(next);
    active.delete(key);
    done.add(key);
    const step: RouteStep = { scope: ref.scope, slug: ref.slug, name: found.module.name };
    if (ref.thread !== undefined) step.thread = ref.thread;
    if (ref.why !== undefined) step.why = ref.why;
    out.push(step);
  };

  for (const ref of allRefs(start.scope, start.module)) visit(ref);
  return out;
}

/** The first cycle found, as `scope/slug` keys, or null. */
export function findCycle(scopes: Scope[]): string[] | null {
  const active: string[] = [];
  const activeSet = new Set<string>();
  const done = new Set<string>();

  const visit = (ref: RouteRef): string[] | null => {
    const key = `${ref.scope}/${ref.slug}`;
    if (activeSet.has(key)) return [...active.slice(active.indexOf(key)), key];
    if (done.has(key)) return null;
    const found = lookup(scopes, ref);
    if (!found) return null;
    active.push(key);
    activeSet.add(key);
    for (const next of allRefs(found.scope, found.module)) {
      const cycle = visit(next);
      if (cycle) return cycle;
    }
    active.pop();
    activeSet.delete(key);
    done.add(key);
    return null;
  };

  for (const scope of scopes) {
    for (const module of scope.modules) {
      const cycle = visit({ scope: scope.id, slug: module.slug });
      if (cycle) return cycle;
    }
  }
  return null;
}

/**
 * In-scope edges pointing at a module later in the same catalogue. The
 * catalogue order is the recommended path, so a backwards edge means the order
 * and the dependencies disagree. Cross-scope edges are exempt: order between
 * scopes is fixed by the architecture, not by array position.
 */
export function forwardReferences(scope: Scope): Array<{ from: string; to: string }> {
  const position = new Map(scope.modules.map((m, i) => [m.slug, i]));
  const out: Array<{ from: string; to: string }> = [];
  scope.modules.forEach((module, i) => {
    for (const ref of allRefs(scope, module)) {
      if (ref.scope !== scope.id) continue;
      const at = position.get(ref.slug);
      if (at !== undefined && at > i) out.push({ from: module.slug, to: ref.slug });
    }
  });
  return out;
}

/** Every `requires` or `suggests` reference that names a module nothing defines. */
export function unresolvedReferences(scopes: Scope[]): Array<{ from: string; ref: string }> {
  const out: Array<{ from: string; ref: string }> = [];
  for (const scope of scopes) {
    for (const module of scope.modules) {
      const refs = [
        ...allRefs(scope, module),
        ...(module.suggests ?? []).map((r) => normaliseRef(r, scope.id)),
      ];
      for (const ref of refs) {
        if (!lookup(scopes, ref)) {
          out.push({ from: `${scope.id}/${module.slug}`, ref: `${ref.scope}/${ref.slug}` });
        }
      }
    }
  }
  return out;
}

/** Thread names used in a scope, and how often. A near-duplicate is the tell. */
export function threadVocabulary(scope: Scope): Map<string, number> {
  const counts = new Map<string, number>();
  for (const module of scope.modules) {
    for (const ref of allRefs(scope, module)) {
      if (!ref.thread) continue;
      counts.set(ref.thread, (counts.get(ref.thread) ?? 0) + 1);
    }
  }
  return counts;
}
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `npx vitest run src/lib/routes.test.ts`
Expected: PASS, 21 tests.

- [ ] **Step 5: Commit**

```bash
git add src/lib/routes.ts src/lib/routes.test.ts
git commit -m "Compute the route from a module's declared dependencies"
```

---

### Task 3: Foundations and Craft catalogues

**Files:**
- Create: `src/content/modules/foundations.yaml`
- Create: `src/content/modules/craft.yaml`
- Modify: `src/pages/foundations.astro:9` (the hardcoded `ORDER`)
- Modify: `src/pages/craft.astro:9` (the hardcoded `ORDER`)
- Modify: `src/lib/modules.ts` (add a section accessor)

**Interfaces:**
- Consumes: the schema from Task 1.
- Produces: `getSectionModules(section: 'foundations' | 'craft'): Promise<Module[]>` in `src/lib/modules.ts`.

- [ ] **Step 1: Write the Foundations catalogue**

Create `src/content/modules/foundations.yaml`. Use the taglines exactly as given below. They are card subtitles, not the module's `description` — the house convention is that a tagline tightens the description rather than repeating it, as every shipped module does.

```yaml
# The cross-platform section. Only General Programming is universal — Numbers &
# Bits and From Source to Silicon are the assembly arm, cross-platform so they
# are taught once rather than per system. See Code198x
# docs/decisions/front-of-curriculum-architecture.md
section: foundations
modules:
  - number: 1
    slug: general-programming
    name: General Programming
    kind: teaching
    status: complete
    tagline: What a program is, and the ideas that are true in every language — sequence, variables, input and output, conditionals, loops and subroutines.
    skills:
      - What a program is
      - Sequence and variables
      - Conditionals and loops
      - Subroutines
    requires: []
  - number: 2
    slug: numbers-and-bits
    name: Numbers & Bits
    kind: teaching
    status: complete
    tagline: Binary, hex and two's complement, then the bit logic assembly leans on constantly — AND, OR, XOR, masking and shifting.
    skills:
      - Decimal, binary and hex
      - Bits, nibbles and bytes
      - Two's complement
      - Masking and shifting
    requires:
      - general-programming
  - number: 3
    slug: from-source-to-silicon
    name: From Source to Silicon
    kind: teaching
    status: coming-soon
    tagline: How the program you write becomes something a machine can run — interpreting, compiling and assembling — and why that one choice is the difference between a game that keeps up and one that can't.
    skills:
      - What "run" means
      - Interpreting as you go
      - Translating once, ahead of time
      - What speed costs you
    requires:
      - numbers-and-bits
```

- [ ] **Step 2: Write the Craft catalogue**

Create `src/content/modules/craft.yaml`:

```yaml
# The transferable-technique section. Two entry points, not one branch: Maths
# for Games needs Numbers & Bits behind it, Game Feel needs a game that already
# runs — which is not a module, so it has no requires at all.
section: craft
modules:
  - number: 1
    slug: maths-for-games
    name: Maths for Games
    kind: teaching
    status: coming-soon
    tagline: The handful of arithmetic tricks every game leans on — movement, direction, distance and chance — on machines with no fast multiply, no fractions, no square root and no sine.
    skills:
      - A direction as a lookup, not a sine
      - Distance without a square root
      - Fixed-point accumulators
      - Shifting as the free multiply
    requires:
      - foundations/numbers-and-bits
  - number: 2
    slug: game-feel
    name: Game Feel
    kind: teaching
    status: coming-soon
    tagline: The small rules that make a game feel fair, readable and finished — visible feedback, grace windows, ending dwells and clocked prompts.
    skills:
      - Visible feedback
      - Grace windows
      - Ending dwells
      - Clocked prompts
    requires: []
```

- [ ] **Step 3: Add the section accessor**

In `src/lib/modules.ts`, after `getModules`, add:

```ts
/**
 * Modules for a cross-platform section (Foundations, The Craft). A section
 * catalogue carries `section` instead of `platform` + `track`.
 */
export async function getSectionModules(section: 'foundations' | 'craft'): Promise<Module[]> {
  const all = await getCollection('modules');
  const entry = all.find((e) => e.data.section === section);
  return entry?.data.modules ?? [];
}
```

- [ ] **Step 4: Read the catalogue in `foundations.astro`**

In `src/pages/foundations.astro`, add `getSectionModules` to the imports from `../lib/modules`, then replace line 9:

```ts
const ORDER = ['general-programming', 'numbers-and-bits', 'from-source-to-silicon'];
```

with:

```ts
// Order is catalogue data, not a list in a page. See
// Code198x docs/decisions/state-lives-in-catalogues.md
const ORDER = (await getSectionModules('foundations')).map((m) => m.slug);
```

- [ ] **Step 5: Read the catalogue in `craft.astro`**

In `src/pages/craft.astro`, apply the same change, replacing:

```ts
const ORDER = ['maths-for-games', 'game-feel'];
```

with:

```ts
// Order is catalogue data, not a list in a page. See
// Code198x docs/decisions/state-lives-in-catalogues.md
const ORDER = (await getSectionModules('craft')).map((m) => m.slug);
```

- [ ] **Step 6: Verify both pages render unchanged**

Run: `CODE_SAMPLES_PATH=../code-samples npm run build`
Then: `grep -o '<h2>[^<]*</h2>' dist/foundations/index.html && grep -o '<h2>[^<]*</h2>' dist/craft/index.html`
Expected: the same module headings, in the same order, as before this task. The catalogue order matches the arrays it replaces, so the rendered output must not change.

- [ ] **Step 7: Commit**

```bash
git add src/content/modules/foundations.yaml src/content/modules/craft.yaml src/lib/modules.ts src/pages/foundations.astro src/pages/craft.astro
git commit -m "Give Foundations and The Craft catalogues of their own"
```

---

### Task 4: The build-time check

**Files:**
- Create: `scripts/check-curriculum-routes.mjs`
- Modify: `package.json` (the `build` script)

**Interfaces:**
- Consumes: every export of `src/lib/routes.ts` from Task 2. Node 24 strips TypeScript, so the `.mjs` script imports the `.ts` module directly — the same code the site uses.

- [ ] **Step 1: Write the check script**

Create `scripts/check-curriculum-routes.mjs`:

```js
#!/usr/bin/env node
/**
 * Check the curriculum's dependency graph before the site is built.
 *
 * The gentle ramp — "complexity rises gently and close to monotonically" — has
 * been an intention nobody could verify. Declared edges make it a property with
 * a test: a module may not require one later in its own catalogue, so a reorder
 * that inverts a dependency fails here instead of going unnoticed.
 *
 * Errors exit non-zero. Thread-name drift is a warning: `Reading a world` and
 * `Reading the world` fragment the grouping silently, but a near-duplicate is a
 * judgement call and should not block a deploy.
 *
 * See Code198x docs/decisions/curriculum-routes.md
 */
import { globSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { load } from 'js-yaml';
import {
  findCycle,
  forwardReferences,
  unresolvedReferences,
  resolveRoute,
  threadVocabulary,
} from '../src/lib/routes.ts';

const ROOT = path.join(import.meta.dirname, '..', 'src', 'content', 'modules');

const scopes = globSync('**/*.yaml', { cwd: ROOT }).sort().map((rel) => {
  const data = load(readFileSync(path.join(ROOT, rel), 'utf8'));
  const id = data.section ?? `${data.platform}/${data.track}`;
  return { id, modules: data.modules ?? [] };
});

const errors = [];
const warnings = [];

for (const { from, ref } of unresolvedReferences(scopes)) {
  errors.push(`${from} requires ${ref}, which nothing defines`);
}

const cycle = findCycle(scopes);
if (cycle) errors.push(`dependency cycle: ${cycle.join(' → ')}`);

for (const scope of scopes) {
  for (const { from, to } of forwardReferences(scope)) {
    errors.push(
      `${scope.id}/${from} requires ${to}, which comes later in the same catalogue — ` +
      `the order and the dependencies disagree`,
    );
  }
}

// Termination needs no check of its own: a route can only fail to terminate
// through a cycle or a dangling reference, and both are errors above. What is
// worth reporting is the deepest route, because a route that grows without
// anyone noticing is the queue coming back.
let deepest = { at: '', length: 0 };
if (!cycle) {
  for (const scope of scopes) {
    for (const module of scope.modules) {
      const length = resolveRoute(scopes, scope.id, module.slug).length;
      if (length > deepest.length) deepest = { at: `${scope.id}/${module.slug}`, length };
    }
  }
}

/** Edit distance, so "Reading a world" and "Reading the world" are caught. */
function distance(a, b) {
  const d = Array.from({ length: a.length + 1 }, (_, i) => [i, ...Array(b.length).fill(0)]);
  for (let j = 1; j <= b.length; j += 1) d[0][j] = j;
  for (let i = 1; i <= a.length; i += 1) {
    for (let j = 1; j <= b.length; j += 1) {
      d[i][j] = Math.min(
        d[i - 1][j] + 1,
        d[i][j - 1] + 1,
        d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1),
      );
    }
  }
  return d[a.length][b.length];
}

for (const scope of scopes) {
  const vocab = [...threadVocabulary(scope).keys()];
  for (let i = 0; i < vocab.length; i += 1) {
    for (let j = i + 1; j < vocab.length; j += 1) {
      const a = vocab[i].toLowerCase();
      const b = vocab[j].toLowerCase();
      // A quarter of the shorter name, so near-duplicates flag and genuinely
      // distinct threads do not.
      if (distance(a, b) <= Math.max(2, Math.floor(Math.min(a.length, b.length) / 4))) {
        warnings.push(`${scope.id}: thread names are near-duplicates — "${vocab[i]}" and "${vocab[j]}"`);
      }
    }
  }
}

const edges = scopes.reduce(
  (n, s) => n + s.modules.reduce((m, mod) => m + (mod.requires?.length ?? 0), 0),
  0,
);

console.log(`\nCurriculum routes: ${scopes.length} catalogues, ${edges} declared edges.`);
if (deepest.length) console.log(`  longest route: ${deepest.length} steps, to ${deepest.at}`);
for (const scope of scopes) {
  const entries = scope.modules.filter((m) => !(m.requires?.length));
  const threads = [...threadVocabulary(scope).keys()];
  console.log(
    `  · ${scope.id} — ${scope.modules.length} modules, ${entries.length} entry points` +
    (threads.length ? `, threads: ${threads.join(', ')}` : ''),
  );
}

if (warnings.length) {
  console.warn('');
  for (const w of warnings) console.warn(`  warning: ${w}`);
}

if (errors.length) {
  console.error(`\nCurriculum routes: ${errors.length} error(s).\n`);
  for (const e of errors) console.error(`  · ${e}`);
  console.error('');
  process.exit(1);
}
```

- [ ] **Step 2: Run it against the real catalogues**

Run: `node scripts/check-curriculum-routes.mjs`
Expected: exit 0. It reports every catalogue including `foundations` and `craft`, with 4 declared edges (three in Foundations and Craft, plus `craft/maths-for-games`), and every platform track showing all its modules as entry points because no track edges are authored yet.

- [ ] **Step 3: Prove the forward-reference check fails a bad graph**

Temporarily add `requires: [gloaming]` to the **first** module in `src/content/modules/sinclair-zx-spectrum/assembly.yaml` (`meet-the-machine`), which sits before `gloaming` in that file.

Run: `node scripts/check-curriculum-routes.mjs`
Expected: exit 1, with `sinclair-zx-spectrum/assembly/meet-the-machine requires gloaming, which comes later in the same catalogue`.

Then revert that edit: `git checkout src/content/modules/sinclair-zx-spectrum/assembly.yaml`

- [ ] **Step 4: Prove the unresolved-reference check fails**

Temporarily change `foundations.yaml`'s `numbers-and-bits` requires to `- general-programmming` (three m's).

Run: `node scripts/check-curriculum-routes.mjs`
Expected: exit 1, with `foundations/numbers-and-bits requires foundations/general-programmming, which nothing defines`.

Then revert: `git checkout src/content/modules/foundations.yaml`

- [ ] **Step 5: Wire it into the build**

In `package.json`, add the script to the `build` chain immediately after `vitest run`, so a broken graph fails before Astro starts:

```
"build": "vitest run && node scripts/check-curriculum-routes.mjs && node scripts/check-vault-imagery.mjs && node scripts/check-vault-platform-balance.mjs && node scripts/check-vault-links.mjs && astro build && node scripts/mark-redirects-noindex.mjs && ([ -f ./tools/pagefind/pagefind ] && PAGEFIND_BINARY_PATH=./tools/pagefind/pagefind npx pagefind --site dist || npx pagefind --site dist)",
```

- [ ] **Step 6: Verify the full build still passes**

Run: `CODE_SAMPLES_PATH=../code-samples npm run build`
Expected: PASS, with the routes report in the output and the page count unchanged.

- [ ] **Step 7: Commit**

```bash
git add scripts/check-curriculum-routes.mjs package.json
git commit -m "Fail the build when the curriculum's order and its dependencies disagree"
```

---

## Not in this phase

- **The two route views.** Threads on the module page, the map on the track page. They get their own plan once real edges exist — the spec deliberately settles the voice of the `why` lines on authored content rather than in the abstract.
- **The platform-side seam edges.** The spec declares `{system}/basic/meet-basic requires {system}/machine/meet-the-machine` and the assembly equivalent. Most cannot be authored yet: `meet-assembly` does not exist until the rename in `splitting-the-assembly-on-ramp.md`, and only the Spectrum has a `machine` track at all. Authoring the Spectrum's alone would encode a shape the other three contradict. They land with that rollout.
- **Authoring edges.** Content work, per the spec's authoring order: Spectrum BASIC first, then Spectrum assembly, then the other three systems.
- **Nothing else.** The four tasks above are the whole phase.

## One decision needed before Task 4

The check script must parse YAML before Astro runs, so it cannot use the content collection. Checked on 2026-09-03:

- `yaml` does not resolve — `ERR_MODULE_NOT_FOUND`.
- `js-yaml` **is** in `node_modules`, but transitively. Nothing in `package.json` declares it, so it is present by another package's grace and can vanish on any upgrade.

The plan above imports `js-yaml`. Relying on it undeclared would be a build that breaks for reasons nobody changed, so it wants adding to `devDependencies` — a new direct dependency, already physically installed, so no new code arrives in the tree. **That needs approval before Task 4 runs.**

The `.ts`-from-`.mjs` import needs no such decision: `scripts/support-gaps.mjs` already does `import { ASM198X_ISAS } from '../src/lib/surfaces.ts'`, so the pattern is established here.
