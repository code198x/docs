# Spacewar!: two ships, a star and the people around the screen

Two people share a display. Each has a ship to steer and an opponent to hit. Turning changes where the ship points; thrust changes its motion. Those are different actions, and learning to coordinate them is part of learning the game.

The basic contest is easy to describe. Playing it requires you to think about where both ships will be, rather than only where they are. A shot takes time to cross the intervening space. Your opponent can move while it travels. The movement that gives you a promising shot may also leave you badly placed for the next encounter. This is a useful way to begin investigating Spacewar!: watch the consequences of a decision continue after the decision itself.

By April 1962, Dan Edwards and Martin Graetz were describing the game in *Decuscope*. Their account includes the players and the people watching them, and offers both symbolic and binary program tapes through Steve Russell. It presents a game people were already gathering around, as well as a demonstration of a computer's real-time capabilities. [Edwards and Graetz, April 1962, mirrored transcription](https://www.wheels.org/spacewar/decuscope.html)

## Which Spacewar!?

For this study, the reference is the edition labelled **Spacewar! 3.1, 24 Sep 62** in [Norbert Landsteiner's browser emulator](https://www.masswerk.at/spacewar/). Its documentation identifies an archived binary tape as the source. The browser also supplies a title screen, keyboard controls, a simulated display and other facilities that are not the original program.

That distinction matters. A preserved game, a reconstruction, a later variant and a modern presentation can share a name while differing in behaviour. We should identify the edition and settings whenever we compare an observation. The browser checks accompanying this draft use version 3.1 with all six sense switches off; the engine and module hashes are recorded separately. They do not establish the appearance, timing or physical controls of an actual PDP-1.

## Learning to move and to aim

Graetz's paper in the proceedings of the 1962 DECUS meetings describes thrust accelerating a ship along the direction it faces. A torpedo begins with the ship's velocity plus its launch velocity. The central star affects the ships but not the torpedoes. These rules make the ship's movement part of aiming. [Graetz, “Spacewar! Real-Time Capability of the PDP-1,” pp. 37–38; proceedings published 1963](https://bitsavers.computerhistory.org/pdf/dec/decus/confProceedings/DECUS_1962.pdf#page=39)

Suppose you turn towards an opponent while drifting sideways. The nose shows the direction of the launcher, but your existing motion also matters. The interesting task is to learn a relationship among orientation, velocity, distance and time. We can explain that relationship without first requiring a course in mechanics.

The other player makes the problem change. They can notice your approach, turn away, fire first or force you to spend attention on avoiding a threat. Prediction becomes a conversation between two people making decisions, rather than an exercise with a fixed target.

The same paper describes translation to the screen's antipoint after star capture and an early three-jump hyperspace device. These rules describe that paper's development state, not every edition. [Graetz, pp. 37–38](https://bitsavers.computerhistory.org/pdf/dec/decus/confProceedings/DECUS_1962.pdf#page=39)

A useful design question follows: how does a shared environmental rule change the choices available to both players? Before answering, we should try the named configuration, observe it and compare what each person expected. Changing one setting can support a later experiment; it should not be mistaken for playing an untouched historical configuration.

## Reading a battle from a few marks

A ship's shape has work to do. You need to distinguish it from the other ship, read its orientation and notice when thrust is being applied. Graetz's contemporary description identifies different outlines, a visible exhaust and torpedoes drawn as moving points. It also warns that torpedoes resemble stars. [Graetz, p. 38, “The Spaceships”](https://bitsavers.computerhistory.org/pdf/dec/decus/confProceedings/DECUS_1962.pdf#page=40)

That gives us something concrete to examine. Which marks can you recognise immediately? Which require motion or context? What information do you lose while concentrating on your own ship? A sparse picture still demands interpretation, and adding more visible detail would not automatically make its important information clearer.

A brief browser check showed exhaust during a thrust input, a visible projectile after a fire input and the first ship disappearing after a hyperspace input. These are limited observations of the selected implementation. They do not measure skill, establish a probability of survival or tell us how a pair of people experiences a match.

There is also more to presentation than the image. In a 2008 interview, Russell recalled quiet controller switches that prevented a player from hearing an opponent repeatedly try to fire after exhausting their supplies. He also recalled earlier controllers failing under heavy use. Sound, physical arrangement and durability could affect play even when they were outside the displayed world. [Russell, interview by Al Kossow, 9 August 2008, pp. 15–16](https://archive.computerhistory.org/resources/access/text/2012/08/102746453-05-01-acc.pdf#page=15)

This is a recollection, not a measured comparison of surviving controllers. It nevertheless suggests a useful question for our own designs: what information does the whole playing arrangement reveal, including information we did not intend it to reveal?

## The imagination behind the ships

Writing in 1981, Graetz connected the group's ideas with their enjoyment of E. E. “Doc” Smith's *Skylark* and *Lensman* stories and spectacular science-fiction films. He remembered discussing space-film sequences they could not make. He also recalled Wayne Wiitanen being called to active military duty during the Berlin crisis and consequently missing the development of an idea he had helped conceive. These are attributed memories of influences and circumstances. [Graetz, “The Origin of Spacewar,” sections I and II, later recollection in an annotated transcription](https://www.masswerk.at/spacewar/SpacewarOrigin.html)

The visible shapes do not have to depict everything a player imagines. A recognisable ship, a star and motion with consequences can invite someone to supply a larger setting. That is an interpretation of the relationship between the game and its fiction, not evidence that all its players imagined the same adventure.

This makes a useful investigation of our own assumptions possible. What do we bring to the display from other games, books or films? What seems self-explanatory only because we have encountered something similar before? Ask two people what they think the marks represent before giving them the names. Their disagreement may tell us something useful about the picture.

## A game made through contributions

The Computer History Museum credits the conception to Russell, Graetz and Wiitanen, and describes the first implementation and subsequent contributions from a wider group. Its account identifies Peter Samson's and Dan Edwards's work as part of the game's development. Spacewar! should not be presented as the complete invention of a lone programmer. [Computer History Museum, PDP-1 restoration project](https://www.computerhistory.org/pdp-1/spacewar/)

Graetz later described overlapping work rather than a tidy succession of completed steps. His account connects additions to perceived problems in play and presentation: a background to help read movement, gravity to change the contest, and controls to improve the physical arrangement. [Graetz, “The Origin of Spacewar,” sections II–III](https://www.masswerk.at/spacewar/SpacewarOrigin.html)

For a production study, this suggests examining both the program and the conditions of iteration. Who could try it? Who could change it? How quickly could an observation become a modification? A later retelling can make that process look inevitable. We should resist inventing a project plan, budget, release deadline or formal playtest method where the evidence does not supply one.

Russell's later account also complicates the idea of a single correct pace. He remembered choosing parameters that allowed more time for marksmanship, and acknowledged that he was not representative of every arcade player. A setting can embody a preference without being the universally best setting. [Russell, 2008, p. 14](https://archive.computerhistory.org/resources/access/text/2012/08/102746453-05-01-acc.pdf#page=14)

## Reaching people without a shop shelf

The April 1962 newsletter gives us a concrete distribution mechanism: contact Russell for program tapes. The game needed a suitable computer and people who could obtain and run it. We can study that route without treating it as equivalent to buying a cassette in a shop. [Edwards and Graetz, April 1962](https://www.wheels.org/spacewar/decuscope.html)

The museum describes the game being used to demonstrate the PDP-1 to prospective customers. Its public role could therefore extend beyond the people operating the controls. [Computer History Museum, “Spacewar!”](https://www.computerhistory.org/pdp-1/spacewar/)

This provides a different business question from the one we might ask about a packaged home-computer release. How can a compelling use help people understand the value of a machine? The available account establishes use in demonstrations; it does not establish the number of computers sold because of the game. We should keep those claims separate.

## The audience changes, and so does the game

Stewart Brand's December 1972 *Rolling Stone* report describes organised play at Stanford, spectators, competition and a Spacewar variant running on a PDP-10. Its multiple ships and match arrangements are evidence of that later scene, not a description of our two-ship reference edition. Brand places computing within a wider cultural argument; his enthusiasm is part of the source's perspective. [Brand, “Spacewar: Fanatic Life and Symbolic Death Among the Computer Bums,” 7 December 1972, mirrored transcription](https://www.wheels.org/spacewar/stone/rolling_stone.html)

That change of audience matters to a whole-game study. A program can become a shared activity, acquire local variants and later become an object of preservation. A report of excitement in one laboratory does not measure the response of everyone who encountered it. A museum's decision to preserve a game is another kind of reception, not a substitute for its original players' accounts.

Today's browser presentation changes access again. It makes an encounter possible without standing at the original machine, while introducing a keyboard, a modern display, timing decisions and interface elements of its own. We can value that access and still name what it cannot reproduce. The [museum's separate browser edition](https://www.computerhistory.org/pdp-1/playspacewar/) explicitly documents changes to ship size and timing, a useful reminder to inspect each implementation rather than assume equivalence.

## Investigating what makes it special

An initial reading is that Spacewar!'s interest lies in the interaction of movement, prediction, another person's decisions and a legible fictional setting. The surrounding evidence adds collaborators, physical controls, access to a machine, program exchange and people watching. None of these alone explains the whole experience.

Try a short investigation with another person:

1. Choose and record the edition, controls and settings. Let each player explore turning and thrust before trying to win.
2. Predict what releasing thrust will do, then observe it. Describe the result without treating a prediction as a mistake to hide.
3. Play several encounters. Identify a moment when a choice helped or hindered you, and ask what the other player thought was happening.
4. Compare one setting or control arrangement. Record what changed and what remained constant; avoid changing several things and crediting one of them.
5. Explain which observation might inform a game of your own, and where the comparison would stop being useful.

These are proposed activities, not results of a completed two-player trial. Someone can investigate through playing, discussion or a drawing without implementing a PDP-1 program. Deeper work can examine the physics, display and code when the question calls for it.

The study should continue to test that initial reading. What is difficult to learn? Which details become readable with experience? Who finds the contest inviting, and who does not? What changes when the version or playing arrangement changes? Understanding the game includes those differences as well as its achievements.
