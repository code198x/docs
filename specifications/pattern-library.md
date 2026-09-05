# The Pattern Library

A pattern is a concrete technique a reader can adapt to their own project. It explains a recurring problem, an implementation and the conditions under which that implementation is useful. Lessons provide guided complete experiences; shared modules develop concepts; the Vault supplies context.

## What belongs here

Select techniques that repay reusable treatment: for example an entity pool, a collision test, a readable opponent state machine, an input routine or a sound-priority policy. Do not turn every fragment into a pattern. A technique may belong to one machine or language; preserving those details is more useful than presenting a falsely universal form.

Each entry explains:

- The problem, a concrete use and when another approach would be preferable.
- An implementation with enough explanation to adapt it.
- Inputs, outputs, state, resource ownership and other contracts.
- Requirements, limits and trade-offs, including relevant timing and memory costs.
- What was built or executed and under which configuration; proposed code is labelled as such.
- Links to lessons showing the technique in a complete game, related patterns and useful conceptual or Vault context.

Compare plausible alternatives. Distinguish measured costs from estimates and avoid unsupported cycle counts or universal performance claims. A shorter listing is not necessarily faster. Explain what an optimisation enables for the player.

## Files and schema

Entries live under the website's `src/content/patterns/`. Published routes follow `/patterns/{system}/{track}/{category}/{slug}/`, with cross-platform entries under `/patterns/cross-platform/{category}/{slug}/`.

The current schema requires `title`, `summary`, `platform`, `category` and `difficulty`. Platforms currently accepted are `commodore-64`, `sinclair-zx-spectrum`, `commodore-amiga`, `nintendo-nes` and `cross-platform`. Categories are `rendering`, `input`, `audio`, `physics`, `ai` and `framework`; difficulty is `beginner`, `intermediate` or `advanced`.

`taught_in` is an optional string, tags default to an empty array, and optional `evolution` and `related` objects carry neighbouring patterns and Vault links. Check `src/content.config.ts` and current route helpers before authoring these fields. Extending the curriculum to another system may require a deliberate schema change; the current enum does not define the project's ultimate scope.

Runnable code follows [Code samples](code-samples.md). Schematic pseudocode is labelled and follows the shared [notation](pseudocode.md). Link both ways between a pattern and its lesson where useful. Confirm links and rendered code, and retain machine-specific assumptions rather than hiding them behind a “production-ready” label.
