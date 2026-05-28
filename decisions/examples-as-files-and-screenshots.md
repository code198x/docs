# Decision: Every example is a real file, shown running

## The decision

Two conventions for how code appears in the curriculum:

1. **Every runnable example is a real file, shown via `CodeFromFile`.** No inline code fences for code the reader could type or run. Each snippet — the unit's program *and* every teaching aside (a one-line variation, an insertion demo, an alternative) — is a real `.bas`/`.asm` file in `code-samples/`, displayed with `<CodeFromFile>`.

2. **Every example is shown running, with a screenshot.** Each example gets an image of the actual program's output, captured from the emulator and embedded with `<Figure>`. Screenshot density is fine — show the result of each example, small ones included.

## Why

A snippet typed into prose is a snippet that can rot: the prose says one thing, the working file says another, and nobody runs the prose. Making every example a real file means every snippet shown is the snippet that was tested — and it can be screenshotted. One source of truth, no drift.

Screenshots answer the reader's first question — "what will I see?" — which our own writing guide says to address before the how-to. A reader following along wants to confirm their screen matches; an absent screenshot leaves them guessing. The cost of an extra image is low and the reassurance is high, so when in doubt, include it.

## Rules

### 1. Runnable code → a file → `CodeFromFile`

Anything the reader could type and run is a real file in `code-samples/`, shown with `<CodeFromFile src="..." />`. This includes teaching asides: a "try changing it" variation, a multi-line demonstration, an insertion demo. Give each a descriptive name alongside the unit's main program (`goodbye.bas`, `welcome.bas`, `welcome-dashes.bas`).

Inline backticks are still fine for *fragments* — a single keyword, a value, a line referenced mid-sentence (`PRINT`, `INK 5`, `GO TO 130`). The rule is about *runnable examples*, not every mention of code.

### 2. Every example gets a screenshot

Each example is shown running via `<Figure>`. Capture the real program's output; do not mock it.

**Recipe (Spectrum):**
- Run the program in Emu198x to a representative state; for INPUT-driven programs, feed worked-example data that matches the prose (the same sample story across a game's units).
- `save_screenshot`, then upscale **3× with nearest-neighbor** (e.g. PIL `Image.NEAREST`) so the pixels stay crisp and the image fills the column instead of sitting at native ~352px.
- Embed with `<Figure src="/images/..." alt="..." caption="..." />` — **no `frame`**. The platform frames round the corners and crop pixel-art edges; a pixel screenshot already includes its own border.
- Store at `public/images/{platform}/{game}/{unit}/{name}.png`, named to match the example (`screenshot.png` for the unit's main program, `{example}.png` for asides).

### 3. Density is fine

Do not ration screenshots. A short unit with four examples gets four screenshots. Showing the result of even a trivial example (a one-word change) is worth more than the space it costs.

## Relationship to other decisions

Builds on [incremental-code-samples.md](incremental-code-samples.md) (the code that goes in the files). The screenshot mechanics extend [../specifications/unit.md](../specifications/unit.md): its "Screenshot Requirements" already mandate capturing and verifying output — this decision adds that the verified screenshot is also *shown*, and that every runnable snippet is a file rather than an inline fence.

## Drift triggers

- An inline code fence contains a runnable program or a line the reader is meant to type. → make it a file + `CodeFromFile`.
- An example is described ("the screen shows…") with no screenshot. → capture and show it.
- A screenshot uses a platform `frame` and the pixel art looks cropped or rounded. → `frame="none"`.
- A screenshot sits small at native resolution. → 3× nearest-neighbor upscale.
- Worked-example data differs between the prose and the screenshot. → make them match.

## Status

Active. Captured 2026-05-28. Builds on [incremental-code-samples.md](incremental-code-samples.md); informs the unit specification and every game's MDX.
