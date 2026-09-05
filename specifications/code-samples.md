# Code samples and built outputs

Runnable curriculum sources belong in the `code198x/code-samples` repository. Pages use the website's `CodeFromFile` component so the displayed listing and downloadable source agree.

```mdx
import CodeFromFile from "@components/CodeFromFile.astro";
<CodeFromFile src="sinclair-zx-spectrum/assembly/meet-the-machine/unit-01/border.asm" />
```

Paths generally follow `{system}/{track}/{module}/unit-NN/`. Use descriptive source filenames and check the component's current language detection before adding a dialect. Source extensions include `.bas`, `.asm` and `.amos`; a shared extension does not mean shared syntax.

## Incremental construction

Each meaningful stage should build on the preceding work and produce an inspectable result. Keep stage files when readers need to run intermediate versions or reproduce captures; use the existing `steps/` convention where applicable. Explain the changed code, relevant state and observed effect. Use `CodeDiff` when it makes the change easier to follow. There is no fixed number of new lines per step or per lesson.

Do not hide essential implementation in an unexplained engine, helper file or restore mechanism. Supplied routines and assets need a clear contract and provenance. A download supports the guided experience; it is not a substitute for it.

Pseudocode and small explanatory fragments may be written in MDX where they are not presented as executable target code. Label schematic fragments honestly. Conceptual lessons can use hand-traces and diagrams; they do not need screenshots from a machine they are not teaching.

## Building and checking

Specify the host tools, versions or reproducible pins, commands, target configuration and expected output. Distinguish source from a built tape, snapshot, disk or cartridge image. Confirm that each claimed executable stage builds and runs in the stated configuration. Exercise inputs, boundaries, restart and any relevant timing or resource limits. Captures must show the matching source revision, not a later finished version.

The website builds publishable artefacts using `scripts/build-artefacts.sh`; capture work uses the sample repository's `_capture/capture.py`. Their actual supported paths determine what can be automated. See [Media capture](../infrastructure/media-capture-pipeline.md).

Keep source and reproducible build instructions in Git. Publish generated outputs through the build/deployment path rather than introducing new committed binaries. Existing tracked artefacts are a migration concern: remove them only after proving equivalent outputs can be rebuilt and preserving required downloads. Do not delete a reader's working material as incidental cleanup.

The in-page `AssembleAndRun` facility currently offers a Spectrum assembly loop using the family toolchain. It complements explained local builds and downloads. Browser convenience does not change the target's hardware, and does not establish support for another machine or language.
