# Content Collections Schema Design

## Overview

This document outlines how Astro Content Collections could be used for Code Like It's 198x. Content would move from `/src/pages/` to `/src/content/`, with schemas providing validation and enabling queries.

## Proposed Collections

### 1. Vault

Articles about people, hardware, games, techniques, culture.

**Location:** `/src/content/vault/`

**Schema:**
```typescript
import { defineCollection, z } from 'astro:content';

const vault = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    summary: z.string().max(200),
    category: z.enum([
      'people',
      'companies',
      'games',
      'techniques',
      'hardware',
      'systems',
      'culture'
    ]),
    platforms: z.array(z.enum(['c64', 'spectrum', 'amiga', 'nes'])).optional(),
    tags: z.array(z.string()).default([]),
    years: z.array(z.number()).optional(),
    related: z.array(z.string()).optional(), // slugs of related entries
  }),
});
```

**File structure:**
```
/src/content/vault/
  rob-hubbard.mdx
  vic-ii.mdx
  paradroid.mdx
  zzap64.mdx
```

**Benefits:**
- Filter index by category: `getCollection('vault').filter(e => e.data.category === 'hardware')`
- Filter by platform: `getCollection('vault').filter(e => e.data.platforms?.includes('c64'))`
- Validate required fields at build time
- Generate category pages dynamically

**URL generation:** `/src/pages/vault/[...slug].astro` renders entries, URLs become `/vault/rob-hubbard`

**For nested URLs later:** `/src/pages/vault/[category]/[slug].astro` → `/vault/people/rob-hubbard`

---

### 2. Units

Individual lesson units within games.

**Location:** `/src/content/units/`

**Schema:**
```typescript
const units = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    platform: z.enum(['commodore-64', 'sinclair-zx-spectrum', 'commodore-amiga', 'nintendo-entertainment-system']),
    language: z.enum(['assembly', 'basic', 'amos']),
    game: z.number().min(1).max(18),
    gameSlug: z.string(), // e.g., 'sid-symphony'
    gameName: z.string(), // e.g., 'SID Symphony'
    unit: z.number().min(1).max(32),
    totalUnits: z.number(),
  }),
});
```

**File structure:**
```
/src/content/units/
  commodore-64/
    assembly/
      game-01-sid-symphony/
        unit-01.mdx
        unit-02.mdx
        ...
      game-02-cosmic-patrol/
        unit-01.mdx
        ...
  sinclair-zx-spectrum/
    assembly/
      game-01-ink-war/
        unit-01.mdx
        ...
```

**Benefits:**
- Auto-generate prev/next navigation from collection query
- Query all units for a game: `getCollection('units').filter(u => u.data.game === 1 && u.data.platform === 'commodore-64')`
- Validate unit numbers, game numbers at build time
- Generate progress tracking data

**URL generation:**
```
/src/pages/[platform]/[language]/[gameSlug]/[unitSlug].astro
```
→ `/commodore-64/assembly/game-01-sid-symphony/unit-01`

**Auto prev/next example:**
```typescript
// In unit page
const allUnits = await getCollection('units');
const gameUnits = allUnits
  .filter(u => u.data.platform === platform && u.data.game === game)
  .sort((a, b) => a.data.unit - b.data.unit);

const currentIndex = gameUnits.findIndex(u => u.data.unit === unit);
const prevUnit = gameUnits[currentIndex - 1];
const nextUnit = gameUnits[currentIndex + 1];
```

---

### 3. Games

Game index pages (the landing page for each game showing overview + unit roadmap).

**Location:** `/src/content/games/`

**Schema:**
```typescript
const games = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    platform: z.enum(['commodore-64', 'sinclair-zx-spectrum', 'commodore-amiga', 'nintendo-entertainment-system']),
    language: z.enum(['assembly', 'basic', 'amos']),
    game: z.number().min(1).max(18),
    gameSlug: z.string(),
    gameName: z.string(),
    totalUnits: z.number(),
    screenshot: z.string().optional(), // path to screenshot
  }),
});
```

**File structure:**
```
/src/content/games/
  commodore-64/
    assembly/
      game-01-sid-symphony.mdx
      game-02-cosmic-patrol.mdx
    basic/
      game-01-number-guess.mdx
  sinclair-zx-spectrum/
    assembly/
      game-01-ink-war.mdx
```

**Benefits:**
- Unit roadmap auto-generated from units collection query
- List all games for a platform dynamically
- Validate game metadata

**URL generation:**
```
/src/pages/[platform]/[language]/[gameSlug]/index.astro
```

---

### 4. Patterns

Code patterns (currently just spec, no content).

**Location:** `/src/content/patterns/`

**Schema:**
```typescript
const patterns = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    platform: z.enum(['commodore-64', 'sinclair-zx-spectrum', 'commodore-amiga', 'nintendo-entertainment-system', 'cross-platform']),
    category: z.enum(['rendering', 'input', 'audio', 'physics', 'ai', 'framework']),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    taughtIn: z.string().optional(), // e.g., "Game 9, Unit 8"
    tags: z.array(z.string()).default([]),
    evolution: z.object({
      previous: z.string().optional(),
      next: z.string().optional(),
    }).optional(),
    related: z.object({
      patterns: z.array(z.string()).default([]),
      vault: z.array(z.string()).default([]),
    }).optional(),
  }),
});
```

**File structure:**
```
/src/content/patterns/
  commodore-64/
    rendering/
      sprite-multiplexing-basic.mdx
      scrolling-character.mdx
    framework/
      raster-interrupts.mdx
  cross-platform/
    sprite-collision.mdx
```

**Benefits:**
- Filter by platform, category, difficulty
- Build evolution chains automatically
- Generate cross-platform comparison pages

---

## Combined Config

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const vault = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    summary: z.string().max(200),
    category: z.enum(['people', 'companies', 'games', 'techniques', 'hardware', 'systems', 'culture']),
    platforms: z.array(z.enum(['c64', 'spectrum', 'amiga', 'nes'])).optional(),
    tags: z.array(z.string()).default([]),
    years: z.array(z.number()).optional(),
  }),
});

const units = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    platform: z.enum(['commodore-64', 'sinclair-zx-spectrum', 'commodore-amiga', 'nintendo-entertainment-system']),
    language: z.enum(['assembly', 'basic', 'amos']),
    game: z.number().min(1).max(18),
    gameSlug: z.string(),
    gameName: z.string(),
    unit: z.number().min(1).max(32),
    totalUnits: z.number(),
  }),
});

const games = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    platform: z.enum(['commodore-64', 'sinclair-zx-spectrum', 'commodore-amiga', 'nintendo-entertainment-system']),
    language: z.enum(['assembly', 'basic', 'amos']),
    game: z.number().min(1).max(18),
    gameSlug: z.string(),
    gameName: z.string(),
    totalUnits: z.number(),
  }),
});

const patterns = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    platform: z.enum(['commodore-64', 'sinclair-zx-spectrum', 'commodore-amiga', 'nintendo-entertainment-system', 'cross-platform']),
    category: z.enum(['rendering', 'input', 'audio', 'physics', 'ai', 'framework']),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    taughtIn: z.string().optional(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { vault, units, games, patterns };
```

---

## Migration Path

### Phase 1: Vault (lowest risk, highest benefit)
1. Create `/src/content/vault/` and config
2. Move 48 vault articles, update frontmatter
3. Create `/src/pages/vault/[...slug].astro` to render
4. Update vault index to query collection
5. Delete old `/src/pages/vault/*.mdx` files

### Phase 2: Patterns (new content, no migration)
1. Create `/src/content/patterns/` and config
2. Create patterns as collection entries
3. Update `/src/pages/patterns/` to query collection

### Phase 3: Games + Units (largest migration)
1. Create collections and config
2. Migrate game index files
3. Migrate unit files (156+)
4. Update routing pages
5. Remove redundant frontmatter (prev/next now auto-generated)

---

## What Changes for Content Authors

**Before (pages):**
```yaml
---
layout: ../../layouts/VaultLayout.astro
title: "Rob Hubbard"
subtitle: "Composer of the Commodore"
summary: "..."
system_tags: [C64]
people_tags: ["Composers"]
years: [1955, 2024]
---
```

**After (collection):**
```yaml
---
title: "Rob Hubbard"
subtitle: "Composer of the Commodore"
summary: "..."
category: "people"
platforms: ["c64"]
tags: ["composers", "sid"]
years: [1955, 2024]
---
```

- No `layout` needed (handled by render page)
- Structured `category` field (validated)
- Consistent `platforms` array
- Build fails if required fields missing

---

## Recommendation

Start with **Vault only** (Phase 1). It's:
- Self-contained (48 files)
- Immediate benefit (filtering, validation)
- Low risk (doesn't affect units/curriculum)
- Good learning exercise for the pattern

If that works well, proceed with Patterns (Phase 2), then Games + Units (Phase 3).
