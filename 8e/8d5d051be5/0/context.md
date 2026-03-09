# Session Context

## User Prompts

### Prompt 1

Please resume from where we left off.

### Prompt 2

Over here, I'm more interested in tying this project into the wider Code Like It's 198x project

### Prompt 3

We're probably not going to be able to embed the WASM emulators right now because of license issues - we'd be able to do Spectrum and NES, but C64 and Amiga would be "problematic". We do have input scripts, but they're JSON-based right now.

### Prompt 4

I want to get _good_ content. And I don't think the current units - and perhaps not even the games themselves - are ambitious enough, or high-quality enough - to hold the interest of potential readers

### Prompt 5

1. All of the above, and then some. I want this to be accessible to as many audiences as possible (this is the reason for the BASIC tracks).
2. A game which resembles those which were commercially available during the lifetime of the system. We can build up to that, but the progression should be obvious and visible.
3. Yes, I absolutely would consider that approach.

### Prompt 6

Yes, let's aim for no more than 8 games per platform, no repetition between them for at least these first four systems (we might not have any choice when we introduce future systems). Let's try these.

### Prompt 7

1. I feel like they could be compelling enough.
2. Either/or, really - Pinball Dreams is indeed iconic.
3. Maybe not even 8 games, maybe 4. Should be separate though.
4. I think they are, BUT we're not going to be doing physical packaging at any point.

Could we go any tighter, or does that put the entire project at risk? These are ambitious games - but I'm not against them.

### Prompt 8

We lose the powers of two if we drop to 6...

### Prompt 9

The other advantage of cutting to 4 is that we have more concepts available for other target systems.

### Prompt 10

Yes, though I'm not entirely convinced I can do rotoscoping :D

### Prompt 11

Yes, let's swap for a driving game.

### Prompt 12

Let's figure out the BASIC tracks

### Prompt 13

Agreed, though we don't necessarily need to cap at 50 lines. I'd be fine up to around 500 lines, but beyond that it would be unwieldy.

### Prompt 14

Here we're starting with a text adventure for all 3 systems, I don't think that's quite enough variety. They were iconic on the Spectrum, less so on the others.

### Prompt 15

I want a _game_ for all of them, so C64 #1 is not yet there

### Prompt 16

That's better, yes. Let's go with that.

### Prompt 17

Let's go with these - it would be _nice_ to specify the capstone games in more detail now, but I get it

### Prompt 18

That's fine for now. One note: "Not physical cartridge production, but a ROM that runs on real hardware via flash cart." - this should be possible for EVERY title.

### Prompt 19

Yes, please do so now.

### Prompt 20

The one trick here is that we _can_ repeat genres later on, I just don't want to for these four systems.

### Prompt 21

Better. Ok. Let's write the game specification docs

### Prompt 22

I didn't spot when you were writing them, but the BASIC entries should be split into separate docs - we have separate curricula entries for those in docs/curriculum/basic/{system} (though, thinking about it, those could be organised as docs/curriculum/{system}/{assembly,basic})

### Prompt 23

Is it worth keeping both, and defining some games that could be done in Blitz as well? It's _very_ different in terms of style.

### Prompt 24

Let's commit these for now, then decide how to proceed from there.

### Prompt 25

We should probably name the games, then we can make the game outlines based on those.

### Prompt 26

Spectrum:

1 - not keen on any of these, keep riffing
2 - Ionfire feels good
3 - Grimstone, yes!
4 - not keen on any of these

C64:

1 - Nova Storm
2 - Coldframe
3 - not keen on these
4 - not keen on these

NES:

1 - Dash
2 - Wyrdstone
3 - not keen on these
4 - not keen on these

Amiga:

1 - Exodus
2 - Duskfall
3 - Redline
4 - not keen on these

I think the problem with the game 4 names is that we haven't truly defined what those games _are_ yet - so it's tricky to come up with a good name

### Prompt 27

Spectrum - gravelight
C64 - warfront
NES - Abyssal Gate

### Prompt 28

Let's name the BASIC games too - we might even pivot to making those

### Prompt 29

Spectrum:

1 - The Cursed Manor sounds good!
2 - Night Patrol
3 - Lattice
4 - Blockstorm

C64:

1 - Depth Charge
2 - Neon Nexus
3 - Starswarm
4 - these names are terrible

AMOS:

1 - Ricochet
2 - these names are terrible
3 - Sidewinder
4 - these names are terrible

Blitz:

1 - Flashpoint
2 - Gridlock
3 - Craterfall
4 - these names are terrible

I sense the same problem with game 4 here, we haven't fully specced it

### Prompt 30

Yes, let's update

### Prompt 31

Probably the game outlines, it'll make it easier to write the content

### Prompt 32

Let's start with (1), and work from there. Each deserves focus.

### Prompt 33

1: I'd consider going even larger, but we can see.
2: I'd love a proper parser, but that might be challenging.
3: Player is invited to a party, but finds that all of the other guests are frozen in place. Must figure out why in order to escape.
4: Yes!
5: No save and load.

### Prompt 34

That sounds good, I'd enjoy playing that.

### Prompt 35

Night Patrol first

### Prompt 36

I think your plan might be correct, BUT there's the interesting pivot where you act as an intruder. Not sure which is most fun.

### Prompt 37

Yes, please

### Prompt 38

Let's do Lattice now

### Prompt 39

I think you're spot on.

### Prompt 40

Let's do Blockstorm

### Prompt 41

Agree, this sounds fine to me

### Prompt 42

Let's do the C64 BASIC, yes

### Prompt 43

[Request interrupted by user]

### Prompt 44

Actually, let's clean up the legacy Spectrum BASIC games that no longer apply

### Prompt 45

Delete all eight, please

### Prompt 46

Let's write the specs for the C64 BASIC games first, in case there's anything useful in the legacy specs

### Prompt 47

I think rhythm would be hard to do at BASIC speed. I do like game 3, but I suspect game 2 is actually doable

### Prompt 48

Is this too close to our Night Patrol concept for the Spectrum?

### Prompt 49

I like the idea. Signal Lost might be the best name.

### Prompt 50

Yes, please

### Prompt 51

I like Conduit, let's go with that - like Pipemania to a degree

### Prompt 52

Let's consider the Amiga BASIC Game 4s

### Prompt 53

AMOS: point-and-click adventure
Blitz: top-down racing game - contrasts with the assembly game 3 (pseudo-3D)

### Prompt 54

AMOS: The Lighthouse
Blitz: Tarmac

### Prompt 55

Let's figure out the assembly outlines

### Prompt 56

I'm happy to keep going. Let's do one platform at a time.

### Prompt 57

Let's start with the Spectrum again. This is doubly important because we're targeting a launch at CRASH! Live in October.

### Prompt 58

Yes, let's proceed

### Prompt 59

Let's continue, I'm happy to do that

### Prompt 60

Let's nail down the Spectrum capstone now.

### Prompt 61

I agree, let's go with the surface world

### Prompt 62

Dawnreach sounds more hopeful, rather than grim

### Prompt 63

Let's do the C64 assembly games

### Prompt 64

Sidereal

### Prompt 65

Let's go with the NES

### Prompt 66

I quite like Starweave

