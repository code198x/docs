# Nintendo Entertainment System: curriculum tooling

Read the [project charter](../../PROJECT.md) and the actual lesson, source and capture manifest before changing a target or promising execution. This page describes the current source-defined tool path; it is not a hardware reference manual or a claim that every local tool is installed.

## Cross-development

The development host runs Asm198x with the `ca65` dialect. The target runs the built program. Build198x prepares media where required; Emu198x supplies the configured execution and capture environment. Retired platform Docker repositories are not the starting point for new tooling work.

```sh
asm198x --dialect ca65 input.asm -o output.nes
```

An iNES cartridge image. Asm198x’s supported ca65 build path emits it directly; do not assume the retired separate ca65/ld65 build is still required.

These commands reflect `code-samples/_capture/capture.py` and the corresponding unit Makefiles. Use the unit’s complete recipe, input files and explicit options for a reproducible result. The website’s `scripts/build-artefacts.sh` owns release-tool pins and publishing; installed tools may differ, so record their versions when reporting validation.

Use `nintendo-entertainment-system` for the current sample/catalogue identity. The Pattern Library currently has a separate `nintendo-nes` schema value; check the relevant collection before copying identifiers.

## Configuration and evidence

Name the model, memory, video standard, input, storage and any extension required by the program. A modern host or transfer method does not add target capabilities. A successor running a compatibility program is distinct from a successor-specific project.

Configure firmware and other runtime dependencies according to the emulator and lesson setup instructions. A built program image is not evidence that no firmware is needed. Do not make blanket redistribution or licensing claims; use the applicable public source and obtain required files through the documented route.

Inspect the capture runner’s actual supported options and manifests. Choose settle times and inputs from the program’s behaviour rather than a universal frame count. View screenshots, watch video and listen to audio before using them as evidence, and label the emulator/model tested. See [Media capture](../../infrastructure/media-capture-pipeline.md).
