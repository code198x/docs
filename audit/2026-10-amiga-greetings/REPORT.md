# First Amiga language greetings: bounded runtime trial

AMOS Professional 2.00 ran the maintained greeting, an edited greeting and a
repaired program after a real syntax error. A fresh AmiBlitz retry ran both the
baseline and edited greetings after importing the plain-text sample as `.ab3`.
It also produced a deliberate syntax error, but recovery was not completed.
**The paired qualification is incomplete.** [Docs #94](https://github.com/code198x/docs/issues/94),
[website #766](https://github.com/code198x/website/issues/766) and
[umbrella #116](https://github.com/stevehill1981/198x/issues/116) stay open.

## Method and identities

On 16 October 2026, manual keyboard entry and visual inspection used the native
FS-UAE 3.2.35 macOS app. The machine was PAL A1200, 68020, no FPU/MMU/JIT,
2 MB chip and 8 MB fast RAM. Kickstart was A1200 3.1 rev 40.68; Workbench was
3.1 rev 40.42. Existing local media were copied into the isolated workspace.
The AmiBlitz IDE additionally requested the matching Fonts disk, then opened
when its copy was mounted in DF1. A host directory was mounted as Tools.

[Preflight identities](preflight.json) distinguish the initially inspected
Homebrew CLI binary from the **native app binary actually used**, and hash the
ROM/Workbench/runtime inputs. [Log excerpts](emulator-log-excerpts.txt) confirm
the active CPU and RAM. [Acquisition](acquisition.json) records the two official
archives, pinned revisions/releases, sizes and SHA-256 hashes. Both language
downloads were explicitly approved as isolated test dependencies. No system
installation, additional package or licensed-media download was performed.

The AMOS repository is pinned at
[533b4b1](https://github.com/AOZ-Studio/AMOS-Professional-Official/tree/533b4b1f5acd604814513f78e02c7b4796cb0531).
The splash identified AMOS Professional Version 2.00. AmiBlitz came from its
[official v3.13.0b release](https://github.com/AmiBlitz/AmiBlitz3/releases/tag/v3.13.0b).
The fresh retry splash identified **AmiBlitz3 V3.13.0 (24.06.2026) Build 3654**;
the runtime debugger identified **RED Debugger 3.11.4**. Keep the archive release
and displayed IDE version distinct. No redistribution right for unrelated disk images
is inferred from a source licence.

[Source identities](source.json) bind the retained [AMOS](inputs/hello.amos) and
[Blitz](inputs/hello.bb2) listings to the inspected sample revision. AMOS was
manually entered and checked on screen. Blitz was first manually entered, then
loaded from an exact host copy after input/control mistakes. This is manual
configuration-specific evidence, not an automated source-to-runtime assertion.
Screenshots were inspected in the session; no screenshot files were retained.

## AMOS: observed loop

Launching `Tools:AMOS/AMOSPro` directly from Workbench produced **Cannot find
AMOS.library.** The pinned loader source `+B.s` searches
`APSystem/amos.library` relative to its current directory. The retained
[two-line script](inputs/start-amos) changes directory before launch; that
route opened the editor. It is a file-folder distribution, not a bootable ADF.

F1 on the three maintained lines displayed **Hello from AMOS!** on orange.
A key at `Wait Key` produced **End of program at line 3.**, offering
**Direct mode [ESC]** and **Editor [RETURN]**. Return restored the editor.
Changing the string to **Edited Hello from AMOS!** and pressing F1 displayed
those words.

Deleting the closing quote did **not** cause a syntax error. F1 still displayed
the edited greeting, and the quote reappeared in the editor. A trailing `+`
after the closing quote did produce the red **Syntax error.** status. Removing
that `+` and pressing F1 restored **Edited Hello from AMOS!**. This is a useful
negative and recovery check; an unclosed-quote exercise would not test that
behaviour on this version.

## AmiBlitz: first attempt boundary

The retained [launcher](inputs/start-blitz) uses `-PED` and adds the package's
Libs drawer to LIBS:. Without `-PED`, shell launch printed CLI help. With it,
the IDE requested Fonts; adding the existing matching Fonts disk let PED open.
The upstream release README states a 68020, 8 MB RAM for small work (12 MB for
serious development), 35 MB disk, Workbench 2.1 or 2.04 with locale.library, and
the included wizard.library. These are IDE requirements, not output requirements.
The bundled guide has older, different disk/OS wording; the release README
is the requirements source for this trial.

The lesson's right-Amiga+X **cut the current line**. Source inspection at
[pinned PED.ab3](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/Sourcecodes/Amiblitz3/PED/PED.ab3#L14116)
corroborates Cut on X and Compile & Run on #. After loading the exact maintained
file and visually checking all four lines, right-Amiga+# changed the status
to **Compiling…**. The next screenshot failed with
`Computer Use server error -10005: cgWindowNotFound`. App rebinding failed with
the same error while the emulator process remained present. That does not
establish whether the guest, emulator or capture connection caused the loss.
That first attempt established no successful compile, greeting, edited output or
fault/repair pass.
Further blind UI retries stopped at this boundary.

## AmiBlitz: fresh retry on 16 October

The [retry observations](retry/observations.json) retain identical archive,
emulator, media and runtime hashes. Window capture remained available throughout;
the suggestion that lunch caused the earlier loss remains a hypothesis.

Loading the maintained ASCII `hello.bb2` displayed all four lines, but compiling
reported **Garbage at the end of line** and **Hint: Maybe some unwanted
characters pending?** on the first `NPrint`. The release's bundled
`Docs/AmiBlitz3.guide`, FILEFORMAT and SMARTTOKENIZATION sections, distinguish
tokenized binary `.bb2` from plain-text `.ab2`/`.ab3` input. Copying the exact
same bytes to [hello.ab3](retry/inputs/hello.ab3) and loading that file gave
highlighted keywords and a successful compile. This diagnoses the import error;
it does not justify renaming genuine binary BB2 files. An extra Return after
loading inserted a blank first line, placing the first statement on line 2.

Right-Amiga+# built the executable, then a blank Sourcecode View appeared.
After a left click, output showed **Hello from Blitz!**, **Compiled, not
interpreted.**, **Program terminated.** and **Press <ENTER> to return to the
IDE ...**. Return restored the source listing. Editing the first string in PED
to **Edited Hello from Blitz!**, compiling again and clicking showed the edited
output and the same termination prompt. The output while waiting at `MouseWait`
was not observed, so this does not establish the intended waiting-state display.
The cause of the blank view/output handoff remains unresolved.

Appending `+` after the first string's closing quote and compiling produced
**Syntax error!** with the actual failing line in the Compile Error requester.
Return then BackSpace, Escape and Space did not visibly dismiss it or establish
a repair. The bounded trial stopped there. **No recovered rerun or complete
Blitz edit/error/repair loop is claimed.** Host-prepared edited/fault files were
not used as substitutes for that missing observation.

## Harness limits and next action

[Observation records](observations.json) include failures as well as passes.
Long host typing calls dropped characters, so text was entered in small chunks
and visually checked. Default keyboard joystick mapping consumed AMOS arrow
keys; No host device restored them. Host End opened Amiga Help. AmiBlitz
navigation/requester attempts also produced unwanted source edits and one
**No file handle set!!** request; those were discarded before loading the exact
sample. The first LHA extraction failed on a French directory name; a fresh
extraction using the already-installed 7z completed with “Everything is Ok”.

The paired website change can now correct AMOS's distribution, named setup,
launch, return-to-editor loop and actual error example. **Blitz's public setup
remains unresolved.** Its next trial should use the established plain-text `.ab3` import, resolve
output visibility and dismiss the compiler requester before verifying an actual
repair and rerun. Original Blitz BASIC 2/Ted and
whole-course AmiBlitz compatibility remain untested.

Only the baseline, string edit and stated fault/recovery are qualified for
AMOS. No save/reopen, second-Print extension, later unit, timing, audio,
assistive-technology, physical-touch or original-hardware claim follows. No
learner was available; understanding, retention and unaided transfer remain
unknown. The parent education issues remain open.
