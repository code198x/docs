# Docker Toolchain Design

**Date:** 2025-11-15
**Status:** Design Complete
**Purpose:** Define Docker-based toolchain architecture for 71 retro computing platforms

---

## Overview

**Problem Statement:**

Building curriculum for 71 platforms (1977-2005) requires dozens of different toolchains:
- Assemblers: ACME, ca65, vasm, sjasmplus, and many more
- Validators: petcat, platform-specific tools
- Emulators: VICE, FUSE, FS-UAE, FCEUX, Mesen, etc.
- Platform-specific utilities and helpers

**Challenges:**
- Installing all toolchains directly on host machine is unwieldy
- "Works on my machine" - version inconsistencies between developers
- Cross-platform compatibility issues (Linux, macOS, Windows)
- CI/CD needs consistent, reproducible environment
- Some tools have platform-specific quirks or dependencies

**Solution: Docker-Based Toolchains**

Provide consistent, isolated development environments via Docker containers, one per platform-phase combination.

**Goals:**
1. **Consistent development environment** - Identical tool versions for all developers and CI/CD
2. **Avoid host pollution** - No need to install dozens of assemblers/emulators on host
3. **Cross-platform compatibility** - Works on Linux, macOS (Intel/Apple Silicon), Windows
4. **Automated validation** - CI/CD runs validation without complex setup
5. **Easy onboarding** - New contributors pull Docker images, start working immediately

---

## Architecture Overview

### Hybrid Approach

**In Docker:**
- Toolchains (assemblers, compilers, validators)
- Headless emulators (for CI/CD automation and runtime testing)
- Helper scripts and utilities

**On Host:**
- Native emulators (VICE, FUSE, FS-UAE, etc.) for interactive development
- Code editors/IDEs
- Git and development tools

**Rationale:**

GUI applications and audio from Docker containers are unreliable on macOS and Windows:
- X11 forwarding requires XQuartz (macOS) or WSL2 + X server (Windows) - clunky and fragile
- Audio from Docker is very difficult on macOS/Windows
- Native emulators provide better developer experience for interactive testing

Docker containers handle:
- Code validation (syntax checking)
- Compilation (generating executables)
- Headless runtime testing (automated, no GUI needed)
- CI/CD automation

### Container Architecture: Per-Platform-Phase

One Docker repository per platform-phase combination:

**Repository Naming:**
- `Code198x/commodore-64-basic-toolchain`
- `Code198x/commodore-64-assembly-toolchain`
- `Code198x/zx-spectrum-basic-toolchain`
- `Code198x/zx-spectrum-assembly-toolchain`
- `Code198x/amiga-amos-toolchain`
- `Code198x/amiga-assembly-toolchain`
- `Code198x/nes-assembly-toolchain` (no BASIC for NES)

**Total:** ~142 repositories (71 platforms × ~2 phases each, some platforms have no BASIC)

**Benefits:**
- Pull only what you need (working on C64 BASIC? Only pull that container)
- Clear separation and independent versioning per platform-phase
- Scales to full 71-platform roadmap
- Independent updates (C64 toolchain update doesn't affect Spectrum)
- Reusable by other projects (not tied to Code198x curriculum)

**Each Container Includes:**
- Assemblers/compilers for that platform-phase
- Validators (syntax, semantic where available)
- Headless emulator for runtime testing
- Helper scripts (PRG generation, British English checker, etc.)
- Platform-specific utilities

**Each Container Excludes:**
- Copyrighted ROMs (handled via package managers or user-provided mounts)
- GUI emulators (developers use native installations on host)
- Development tools (editors, IDEs - use host tools)
- Example code (lives in code-samples repo)

---

## Repository Structure

### Standard Toolchain Repository Contents

```
{platform}-{phase}-toolchain/
├── Dockerfile                 # Container definition
├── README.md                  # Usage, installation, examples
├── CHANGELOG.md               # Version history
├── LICENSE                    # Open source license (MIT/GPL)
├── .github/
│   └── workflows/
│       ├── build.yml          # Build multi-platform, test, publish
│       └── test.yml           # PR validation
├── scripts/
│   ├── validate.sh            # Syntax validation wrapper
│   ├── compile.sh             # Generate executables
│   ├── test-runtime.sh        # Headless emulator testing
│   └── helpers/               # Platform-specific utilities
├── tests/
│   ├── test-validation.sh     # Test that validation catches errors
│   ├── test-compilation.sh    # Test executable generation
│   └── fixtures/              # Test files (valid/invalid examples)
└── examples/
    ├── hello.bas              # Basic working example
    └── syntax-error.bas       # Example that should fail validation
```

### Published Docker Images

Each repository publishes multi-platform Docker images to GitHub Container Registry:

**Image Naming:**
- `ghcr.io/code198x/commodore-64-basic-toolchain:latest`
- `ghcr.io/code198x/commodore-64-basic-toolchain:v1.2.3` (semver tags)

**Platforms:**
- `linux/amd64` - Intel/AMD processors
- `linux/arm64` - Apple Silicon (M1/M2/M3 Macs)

### CI/CD Workflow

**On Pull Request:**
1. Build Docker image (single platform, fast feedback)
2. Run test suite
3. Validate example files compile
4. Report results as PR checks

**On Tag/Release (v*.*.*):**
1. Build multi-platform images (AMD64 + ARM64)
2. Run comprehensive test suite
3. Publish to GitHub Container Registry with version tags
4. Update `latest` tag
5. Generate release notes from CHANGELOG.md

**CI Configuration Example:**

```yaml
# .github/workflows/build.yml
name: Build and Publish

on:
  push:
    tags:
      - 'v*.*.*'
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build image
        run: docker build -t test-image .

      - name: Run tests
        run: |
          docker run --rm test-image /scripts/test-validation.sh
          docker run --rm test-image /scripts/test-compilation.sh

  publish:
    if: startsWith(github.ref, 'refs/tags/v')
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract version
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT

      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          platforms: linux/amd64,linux/arm64
          push: true
          tags: |
            ghcr.io/code198x/commodore-64-basic-toolchain:latest
            ghcr.io/code198x/commodore-64-basic-toolchain:v${{ steps.version.outputs.VERSION }}
```

---

## Code Samples Repository Integration

### Repository Structure

The `code-samples` repository uses toolchain Docker images for validation:

```
code-samples/
├── docker-compose.yml         # Toolchain service definitions
├── scripts/
│   ├── commodore-64/
│   │   ├── validate-basic.sh
│   │   ├── validate-assembly.sh
│   │   ├── compile.sh
│   │   └── test-runtime.sh
│   ├── zx-spectrum/
│   │   ├── validate-basic.sh
│   │   ├── validate-assembly.sh
│   │   └── test-runtime.sh
│   ├── amiga/
│   │   └── ...
│   └── nes/
│       └── ...
├── commodore-64/
│   ├── phase-0/              # BASIC lessons
│   │   └── tier-1/
│   │       └── lesson-001/
│   │           ├── example-1.bas
│   │           └── example-1.prg
│   └── phase-1/              # Assembly lessons
│       └── tier-1/
│           └── lesson-001/
│               ├── example-1.asm
│               └── example-1.prg
├── zx-spectrum/
│   └── ...
└── ...
```

### docker-compose.yml (Single Source of Truth)

Defines all toolchain services with pinned versions:

```yaml
services:
  c64-basic:
    image: ghcr.io/code198x/commodore-64-basic-toolchain:v1.2.3
    volumes:
      - .:/workspace
    working_dir: /workspace

  c64-assembly:
    image: ghcr.io/code198x/commodore-64-assembly-toolchain:v1.2.3
    volumes:
      - .:/workspace
    working_dir: /workspace

  spectrum-basic:
    image: ghcr.io/code198x/zx-spectrum-basic-toolchain:v1.1.0
    volumes:
      - .:/workspace
    working_dir: /workspace

  spectrum-assembly:
    image: ghcr.io/code198x/zx-spectrum-assembly-toolchain:v1.1.0
    volumes:
      - .:/workspace
    working_dir: /workspace

  amiga-amos:
    image: ghcr.io/code198x/amiga-amos-toolchain:v1.0.5
    volumes:
      - .:/workspace
    working_dir: /workspace

  amiga-assembly:
    image: ghcr.io/code198x/amiga-assembly-toolchain:v1.0.5
    volumes:
      - .:/workspace
    working_dir: /workspace

  nes-assembly:
    image: ghcr.io/code198x/nes-assembly-toolchain:v1.0.0
    volumes:
      - .:/workspace
    working_dir: /workspace

  # ... all 142 platform-phase combinations
```

### Wrapper Script Example (Smart Wrapper)

```bash
#!/bin/bash
# scripts/commodore-64/validate-basic.sh

set -euo pipefail

# Validate inputs
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file.bas>"
    echo ""
    echo "Validates Commodore 64 BASIC syntax using petcat."
    exit 1
fi

FILE="$1"

# Check file exists
if [ ! -f "$FILE" ]; then
    echo "Error: File not found: $FILE"
    exit 1
fi

# Check extension
if [[ ! "$FILE" =~ \.bas$ ]]; then
    echo "Error: File must have .bas extension"
    echo "Got: $FILE"
    exit 1
fi

# Convert to workspace-relative path for Docker
WORKSPACE_PATH="/workspace/$FILE"

# Run validation in container
echo "Validating $FILE..."
docker compose run --rm c64-basic \
    petcat -text -o /dev/null -- "$WORKSPACE_PATH" 2>&1 | \
    grep -v "^$" || true  # Filter empty lines

EXIT_CODE=${PIPESTATUS[0]}

if [ $EXIT_CODE -eq 0 ]; then
    echo "✓ Validation passed"
else
    echo "✗ Validation failed (exit code: $EXIT_CODE)"
    echo ""
    echo "Common issues:"
    echo "  - Unmatched quotes in strings"
    echo "  - Invalid BASIC V2 keywords"
    echo "  - Line numbers out of range (0-63999)"
fi

exit $EXIT_CODE
```

**Script Features:**
- ✅ Input validation (file exists, correct extension)
- ✅ Helpful error messages
- ✅ Path conversion for Docker
- ✅ Clean output formatting
- ✅ Meaningful exit codes
- ✅ Common issue hints

### Developer Workflow

```bash
# First time setup
docker compose pull  # Pull all toolchain images

# Validate a file
./scripts/commodore-64/validate-basic.sh commodore-64/phase-0/tier-1/lesson-001/example-1.bas

# Compile to executable
./scripts/commodore-64/compile.sh commodore-64/phase-0/tier-1/lesson-001/example-1.bas

# Runtime test (headless emulator)
./scripts/commodore-64/test-runtime.sh commodore-64/phase-0/tier-1/lesson-001/example-1.prg
```

### CI/CD in Code Samples Repository

Per-platform-phase workflows trigger on path changes:

```yaml
# .github/workflows/commodore-64-basic.yml
name: Commodore 64 BASIC Validation

on:
  push:
    paths:
      - 'commodore-64/phase-0/**'
      - 'scripts/commodore-64/**'
      - 'docker-compose.yml'
  pull_request:
    paths:
      - 'commodore-64/phase-0/**'
      - 'scripts/commodore-64/**'
      - 'docker-compose.yml'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Pull toolchain
        run: docker compose pull c64-basic

      - name: Validate all BASIC files
        run: |
          find commodore-64/phase-0 -name "*.bas" -print0 | \
          xargs -0 -I {} ./scripts/commodore-64/validate-basic.sh {}

      - name: Generate all PRG files
        run: |
          find commodore-64/phase-0 -name "*.bas" -print0 | \
          xargs -0 -I {} ./scripts/commodore-64/compile.sh {}

      - name: Test runtime (sample)
        run: |
          find commodore-64/phase-0 -name "*.prg" -print0 | \
          head -z -n 5 | \
          xargs -0 -I {} ./scripts/commodore-64/test-runtime.sh {}

      - name: Report errors with annotations
        if: failure()
        run: |
          # Parse error logs and output GitHub Actions annotations
          # Format: ::error file={file},line={line}::{message}
          echo "::error file=commodore-64/phase-0/tier-1/lesson-001/example-1.bas,line=10::Syntax error: unmatched quote"

      - name: Upload artifacts on failure
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: validation-logs
          path: |
            **/*.log
            **/*.err
```

**CI Features:**
- ✅ Triggers only on relevant file changes
- ✅ Validates all affected files
- ✅ Tests runtime for sample files
- ✅ Structured error annotations (show in PR file view)
- ✅ Uploads debug artifacts on failure
- ✅ Clear failure reporting

**Scaling:** ~142 workflow files (one per platform-phase), each triggers independently based on paths.

---

## Licensing and Distribution Constraints

### What We Can Ship

✅ **Open source tools:**
- Assemblers: ACME, ca65, vasm, sjasmplus (all open source)
- petcat (part of VICE, GPL)
- Helper scripts and utilities we write
- Dockerfile configurations

✅ **Open source emulators:**
- VICE (GPL) - installed via package manager
- FUSE (GPL) - installed via package manager
- FS-UAE (GPL) - installed via package manager
- FCEUX, Mesen (GPL/MIT)
- Most emulators are open source

✅ **Our code and documentation:**
- Wrapper scripts
- Validation tools
- Examples we create
- Documentation and guides

### What We Cannot Ship

❌ **Copyrighted ROMs:**
- C64 BASIC ROM, KERNAL ROM, CHAR ROM
- ZX Spectrum ROMs
- Amiga Kickstart ROMs
- NES/Famicom BIOS
- Any copyrighted system ROM

❌ **Licensed software:**
- Proprietary development tools
- Commercial software (even for reference)
- Third-party libraries with restrictive licenses

❌ **Third-party assets:**
- Copyrighted sprites, music, graphics from games
- Licensed fonts or artwork
- Commercial game code

### ROM Handling Strategies

#### Strategy 1: Package Manager (Preferred)

Many Linux distributions package emulators with ROMs included under their own licensing arrangements:

```dockerfile
# Dockerfile for commodore-64-basic-toolchain
FROM ubuntu:22.04

# Install VICE from package manager
# Ubuntu/Debian packages include ROMs under their distribution license
RUN apt-get update && \
    apt-get install -y \
        vice \
        petcat \
    && rm -rf /var/lib/apt/lists/*

# ROMs handled by package maintainers
# Legal responsibility on distro maintainers
```

**Applies to:**
- VICE (C64) - ROMs included in most distro packages
- FUSE (ZX Spectrum) - ROMs included in most distro packages
- FS-UAE (Amiga) - May or may not include Kickstart ROMs

**Benefits:**
- ✅ Legal responsibility on distribution maintainers
- ✅ Simplest approach for developers
- ✅ No manual ROM acquisition needed

#### Strategy 2: User-Provided ROMs (When Necessary)

For platforms where package managers don't include ROMs (e.g., Amiga Kickstart):

```dockerfile
# Dockerfile for amiga-assembly-toolchain
FROM ubuntu:22.04

# Install FS-UAE emulator (without Kickstart)
RUN apt-get update && \
    apt-get install -y fs-uae && \
    rm -rf /var/lib/apt/lists/*

# Volume for user-provided ROMs
VOLUME /roms

# Configure emulator to use ROM path
ENV KICKSTART_PATH=/roms
```

**README.md documents:**

```markdown
## ROM Requirements

This toolchain requires Amiga Kickstart ROMs, which are copyrighted by Cloanto/Amiga, Inc.

**You must legally own these files to use them.**

### Obtaining ROMs Legally

You can obtain Kickstart ROMs from:
- **Original Amiga hardware** - If you own an Amiga, you can dump the Kickstart ROM
- **Amiga Forever** - Licensed package from Cloanto (https://www.amigaforever.com/)
- **Cloanto** - Official distributor of Amiga IP

### Installation

Place ROM files in the `/roms` directory:
- `/roms/kick31.rom` - Kickstart 3.1 (recommended)
- `/roms/kick20.rom` - Kickstart 2.0 (alternative)

### Usage

Mount the ROMs directory when running the container:

```bash
docker run --rm \
  -v ./roms:/roms:ro \
  -v ./code-samples:/workspace \
  amiga-assembly-toolchain validate example.asm
```

### Verification

Run ROM validation to ensure files are correct:

```bash
docker run --rm -v ./roms:/roms amiga-assembly-toolchain verify-roms
```

Expected checksums:
- kick31.rom: [SHA256 hash]
- kick20.rom: [SHA256 hash]
```

**Benefits:**
- ✅ Legally compliant (users provide own ROMs)
- ✅ Clear documentation on legal acquisition
- ✅ Verification ensures correct files
- ✅ Read-only mount prevents accidental modification

#### Strategy 3: Open Source Alternatives (Fallback)

Use open-source ROM replacements where available:

```dockerfile
# Install OpenROMs or similar open-source BIOS replacements
RUN wget https://example.com/openroms.tar.gz && \
    tar xzf openroms.tar.gz -C /usr/share/roms/
```

**Note limitations:**
- May not be 100% compatible with original hardware
- Some software may not work correctly
- Primarily useful for basic validation, not comprehensive testing

**Applies to:**
- Some platforms have community-created open ROMs
- Useful for CI/CD where full compatibility isn't critical
- Document differences from original hardware

### Code Sample Distribution

Learners download code samples directly from GitHub using raw URLs:

```markdown
<!-- In lesson MDX -->
## Download the Code

Try this yourself:
- [example-1.bas](https://raw.githubusercontent.com/Code198x/code-samples/main/commodore-64/phase-0/tier-1/lesson-001/example-1.bas)
- [example-1.prg](https://raw.githubusercontent.com/Code198x/code-samples/main/commodore-64/phase-0/tier-1/lesson-001/example-1.prg)
```

**Benefits:**
- ✅ Simple, works immediately
- ✅ No extra infrastructure needed
- ✅ Files served directly from GitHub
- ✅ Version control built-in (can link to specific commits/tags)

**Future Enhancement:**

Copy samples to website's public directory during build:
```markdown
Download: [example-1.bas](/code-samples/commodore-64/phase-0/tier-1/lesson-001/example-1.bas)
```

Serves from same domain, cleaner URLs, but requires build-time copy step.

---

## Future Considerations

### ROM-Based CI Testing (Deferred Decision)

For platforms requiring copyrighted ROMs (especially Amiga), CI testing may need ROMs to run comprehensive validation.

**Potential Approach:**

Use GitHub Secrets to provide ROMs for CI without exposing them publicly:

```yaml
# .github/workflows/test-with-roms.yml
name: Full Validation (with ROMs)

on:
  push:
    branches: [main]  # Only on main branch, not PRs from forks

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Decode ROMs from secrets
        run: |
          echo "${{ secrets.AMIGA_KICKSTART_31 }}" | base64 -d > /tmp/kick31.rom
          echo "${{ secrets.AMIGA_KICKSTART_20 }}" | base64 -d > /tmp/kick20.rom

      - name: Run tests with ROMs
        run: |
          docker run --rm \
            -v /tmp:/roms:ro \
            -v $(pwd):/workspace \
            amiga-toolchain test

      - name: Cleanup ROMs (always runs)
        if: always()
        run: rm -f /tmp/*.rom
```

**Security Measures:**
- ✅ ROMs only exist in runner's `/tmp` during job
- ✅ Mounted read-only to container
- ✅ Cleaned up even if tests fail
- ✅ Not accessible to forked PRs (GitHub Secrets restriction)
- ✅ Not visible in logs (if not echoed/listed)
- ✅ Only runs on protected branches (main, release tags)

**Risks:**
- ❌ Someone with write access could modify CI to exfiltrate secrets
- ❌ Logs must be carefully reviewed to prevent leakage
- ❌ Requires trust in repository maintainers

**Decision:** Deferred until Amiga samples are ready. May be essential for comprehensive Amiga validation.

### DevContainer Support

Optional VS Code devcontainer.json configurations for IDE integration:

```json
// .devcontainer/commodore-64-basic/devcontainer.json
{
  "name": "C64 BASIC Development",
  "dockerComposeFile": "../../docker-compose.yml",
  "service": "c64-basic",
  "workspaceFolder": "/workspace",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.hexeditor",
        "bierner.markdown-preview-github-styles"
      ]
    }
  }
}
```

**Benefits:**
- Seamless IDE integration
- Terminal automatically inside container
- Extensions pre-configured
- One-click setup for new contributors

**Scope:** Optional enhancement, not required for initial rollout.

### Automated Screenshot Capture

Extend toolchains to support headless screenshot capture for lesson screenshots:

```bash
# scripts/commodore-64/capture-screenshot.sh
docker compose run --rm c64-basic \
  x64sc -autostart example.prg -limitcycles 20000000 \
  -VICIIdsize -exitscreenshot /workspace/screenshot.png +sound
```

**Benefits:**
- Automated screenshot generation during validation
- Consistent screenshot quality and timing
- Reproducible across all developers

**Challenges:**
- Requires headless X11 setup in containers
- Timing issues (when to capture)
- Platform-specific screenshot commands

**Scope:** Future enhancement, manual screenshots sufficient initially.

---

## Migration Plan

### Phase 1: Rename Existing Repository

**Current:** `Code198x/commodore-64-dev`
**Target:** `Code198x/commodore-64-basic-toolchain`

**Steps:**
1. Rename repository on GitHub (preserves stars, issues, PRs, history)
2. Update README to reflect new purpose and naming convention
3. Update Dockerfile to match new comprehensive structure
4. Add CI/CD workflows (build.yml, test.yml)
5. Add test suite and fixtures
6. Publish first versioned release (v1.0.0) to GitHub Container Registry
7. Update code-samples repo to reference new image

### Phase 2: Create Assembly Toolchain

**New:** `Code198x/commodore-64-assembly-toolchain`

**Steps:**
1. Create new repository following standard structure
2. Dockerfile with ACME/ca65, headless VICE, helpers
3. Test suite with assembly examples
4. CI/CD workflows
5. Publish v1.0.0 to GitHub Container Registry
6. Update code-samples docker-compose.yml with new service

### Phase 3: Expand to Other Platforms

**Priority Order:**
1. ZX Spectrum (basic-toolchain, assembly-toolchain)
2. Amiga (amos-toolchain, assembly-toolchain)
3. NES (assembly-toolchain only, no BASIC)
4. Additional platforms as curriculum expands

**Process per platform:**
1. Create toolchain repositories
2. Build and test locally
3. Set up CI/CD
4. Publish to GitHub Container Registry
5. Update code-samples docker-compose.yml
6. Create wrapper scripts in code-samples/scripts/{platform}/
7. Document in toolchain README

### Phase 4: CI/CD Integration

**Code-samples repository:**
1. Create per-platform-phase workflows (.github/workflows/)
2. Configure path-based triggering
3. Test validation on sample files
4. Add error reporting and annotations
5. Document workflow in code-samples README

**Timeline:**
- Phase 1 (C64 BASIC): 1-2 weeks
- Phase 2 (C64 Assembly): 1 week
- Phase 3 (Per platform): 1-2 weeks each
- Phase 4 (CI/CD): Ongoing as platforms added

---

## Summary

**Architecture:**
- Per-platform-phase Docker repositories (~142 total)
- Hybrid approach: toolchains in Docker, native emulators on host
- Published to GitHub Container Registry with multi-platform support (AMD64, ARM64)

**Developer Experience:**
- Pull toolchain images via docker-compose
- Use smart wrapper scripts for common tasks
- Native emulators for interactive development
- Consistent environment across Linux, macOS, Windows

**CI/CD:**
- Per-platform-phase workflows with path-based triggering
- Automated validation on every commit
- Multi-platform image builds on release
- Structured error reporting with annotations

**Licensing:**
- Open source tools and emulators via package managers
- User-provided ROMs where necessary (documented clearly)
- Code samples distributed via GitHub raw URLs

**Migration:**
- Start with C64 (rename existing repo, create assembly repo)
- Expand to ZX Spectrum, Amiga, NES
- Add remaining 67 platforms as curriculum develops

**Foundation complete for scalable, consistent toolchain infrastructure across 71 platforms.**
