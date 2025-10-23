#!/usr/bin/env python3
"""
Generate all phase overview and tier README files for Commodore 64 curriculum.
Creates 16 phase overviews + 16 tier READMEs per phase (variable by phase).
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path("/Users/stevehill/Projects/Code198x/docs/commodore-64")

# Phase structure: (name, tier_count, lessons_per_tier, start_lesson, games)
PHASES = {
    1: {
        "name": "Assembly + Hardware Fundamentals",
        "tiers": 16,
        "lessons_per_tier": 32,
        "start_lesson": 1,
        "total_lessons": 512,
        "games": [
            ("Pong", "2-player paddle game"),
            ("Breakout", "Brick-breaking with power-ups"),
            ("Space Invaders", "Fixed shooter with formations"),
            ("Galaxian", "Diving enemies and attack waves"),
            ("Asteroids", "Rotation, momentum, wrapping"),
            ("Missile Command", "Trajectory targeting and explosions"),
            ("Defender", "Horizontal scrolling shooter"),
            ("Scramble", "Terrain-following with fuel"),
            ("Zaxxon", "Isometric view and altitude"),
            ("Dig Dug", "Tunnel digging and inflation"),
            ("Q*bert", "Isometric hopping on diamond grid"),
            ("Frogger", "Lane-crossing with moving platforms"),
            ("Donkey Kong", "Multi-screen platformer with jumping"),
            ("Mario Bros", "Arena platformer with POW block"),
            ("Pac-Man", "Maze navigation with ghost AI"),
            ("Centipede", "Segmented enemies and mushroom field")
        ]
    },
    2: {
        "name": "Action Foundations",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 513,
        "total_lessons": 512,
        "games": [
            ("Contra", "Run-and-gun shooter"),
            ("Double Dragon", "Beat-em-up"),
            ("Mega Man", "Boss rush platformer"),
            ("Castlevania", "Gothic platformer"),
            ("Barbarian", "Sword fighter"),
            ("Smash TV", "Arena shooter"),
            ("Prince of Persia", "Cinematic platformer"),
            ("Shinobi", "Ninja action synthesis")
        ]
    },
    3: {
        "name": "Puzzle Games",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 1025,
        "total_lessons": 512,
        "games": [
            ("Tetris", "Falling blocks"),
            ("Columns", "Match-3 vertical"),
            ("Dr. Mario", "Virus puzzle"),
            ("Klax", "Conveyor stacking"),
            ("Lemmings", "Multi-unit puzzle"),
            ("Pipe Mania", "Flow puzzle"),
            ("Chip's Challenge", "Grid adventure"),
            ("Sokoban", "Push puzzles")
        ]
    },
    4: {
        "name": "Platformers Deep Dive",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 1537,
        "total_lessons": 512,
        "games": [
            ("Super Mario Bros", "Precision platforming"),
            ("Metroid", "Exploration platformer"),
            ("Sonic", "Speed platformer"),
            ("Kirby", "Copy ability platformer"),
            ("Ghouls 'n Ghosts", "Gothic platformer"),
            ("Rick Dangerous", "Puzzle platformer"),
            ("Rainbow Islands", "Vertical platformer"),
            ("New Zealand Story", "Flight platformer")
        ]
    },
    5: {
        "name": "Beat-em-ups & Brawlers",
        "tiers": 8,
        "lessons_per_tier": 48,
        "start_lesson": 2049,
        "total_lessons": 384,
        "games": [
            ("Final Fight", "3-button combat brawler"),
            ("Streets of Rage", "Desperation attacks"),
            ("Golden Axe", "Fantasy brawler with magic"),
            ("TMNT Arcade", "4-player co-op"),
            ("Bad Dudes", "Wall climbing brawler"),
            ("Renegade", "Gang fights"),
            ("Target Renegade", "Refined combat"),
            ("Kung-Fu Master", "Floor-by-floor progression")
        ]
    },
    6: {
        "name": "Shoot-em-ups",
        "tiers": 16,
        "lessons_per_tier": 64,
        "start_lesson": 2433,
        "total_lessons": 1024,
        "games": [
            ("1942", "WWII vertical shooter"),
            ("1943", "Enhanced 1942"),
            ("Xevious", "Ground + air targeting"),
            ("Twin Cobra", "Intense vertical"),
            ("Silkworm", "Helicopter + jeep co-op"),
            ("R-Type", "Force pod classic"),
            ("Gradius", "Power-up bar"),
            ("Nemesis", "Multiple weapons"),
            ("Katakubi", "Speed-based"),
            ("Delta", "Weapon variety"),
            ("Robotron 2084", "Twin-stick classic"),
            ("Smash TV Advanced", "Arena perfection"),
            ("Berzerk", "Room-based shooter"),
            ("Uridium", "Low-flying dreadnought"),
            ("Zynaps", "Weapon pods"),
            ("Armalyte", "Technical showcase")
        ]
    },
    7: {
        "name": "RPG Systems",
        "tiers": 8,
        "lessons_per_tier": 128,
        "start_lesson": 3457,
        "total_lessons": 1024,
        "games": [
            ("Ultima IV", "Western RPG with virtue system"),
            ("Zelda", "Action RPG"),
            ("Bard's Tale", "First-person dungeon crawler"),
            ("Final Fantasy", "JRPG with job system"),
            ("Wasteland", "Post-apocalyptic RPG"),
            ("Rogue", "Roguelike with permadeath"),
            ("Diablo-style", "Loot-focused action RPG"),
            ("Betrayal at Krondor", "Tactical RPG")
        ]
    },
    8: {
        "name": "Adventure Games",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 4481,
        "total_lessons": 512,
        "games": [
            ("Maniac Mansion", "Room-based adventure"),
            ("Monkey Island", "SCUMM adventure"),
            ("King's Quest", "Parser + graphics"),
            ("Police Quest", "Procedural adventure"),
            ("Uninvited", "MacVenture horror"),
            ("Shadowgate", "MacVenture fantasy"),
            ("Déjà Vu", "MacVenture noir"),
            ("The Hobbit", "Text parser excellence")
        ]
    },
    9: {
        "name": "Strategy Games",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 4993,
        "total_lessons": 512,
        "games": [
            ("Civilization", "Turn-based 4X"),
            ("Dune II", "Real-time strategy"),
            ("X-COM", "Tactical turn-based"),
            ("Populous", "God game"),
            ("SimCity", "City simulation"),
            ("Lemmings Tactical", "Puzzle-strategy hybrid"),
            ("Cannon Fodder", "Real-time squad tactics"),
            ("Syndicate", "Cyberpunk tactical squad")
        ]
    },
    10: {
        "name": "Racing & Driving",
        "tiers": 8,
        "lessons_per_tier": 48,
        "start_lesson": 5505,
        "total_lessons": 384,
        "games": [
            ("Out Run", "Sprite scaling arcade racer"),
            ("Pole Position", "Track racing"),
            ("Lotus Esprit", "Sim racer with weather"),
            ("Super Sprint", "Top-down multiplayer"),
            ("Stunt Car Racer", "3D elevated tracks"),
            ("Buggy Boy", "Off-road obstacle course"),
            ("Pitstop II", "Pit stop strategy"),
            ("Formula One GP", "F1 simulation")
        ]
    },
    11: {
        "name": "Fighting Games",
        "tiers": 8,
        "lessons_per_tier": 48,
        "start_lesson": 5889,
        "total_lessons": 384,
        "games": [
            ("Street Fighter II", "Special moves and combos"),
            ("Mortal Kombat", "Digitized sprites and fatalities"),
            ("International Karate+", "3-way fighter"),
            ("Way of Exploding Fist", "Precision martial arts"),
            ("Yie Ar Kung-Fu", "Weapon fighters"),
            ("Karateka", "Cinematic fighter"),
            ("Barbarian", "Gore sword fighter"),
            ("Budokan", "Multi-discipline martial arts")
        ]
    },
    12: {
        "name": "Sports Games",
        "tiers": 8,
        "lessons_per_tier": 48,
        "start_lesson": 6273,
        "total_lessons": 384,
        "games": [
            ("Kick Off 2", "Advanced soccer sim"),
            ("NBA Jam", "Arcade basketball"),
            ("Tony Hawk", "Skateboarding with tricks"),
            ("Sensible Soccer", "Top-down fast soccer"),
            ("International Soccer", "Simple elegant soccer"),
            ("Summer Games", "Track and field events"),
            ("Winter Games", "Winter sports events"),
            ("World Games", "International sports variety")
        ]
    },
    13: {
        "name": "Multi-Genre Synthesis",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 6657,
        "total_lessons": 512,
        "games": [
            ("Pirates!", "Trading + combat + adventure"),
            ("River Raid", "Shooter + resource management"),
            ("Rocket Ranger", "Action + strategy + adventure"),
            ("Archon", "Chess + fighting"),
            ("Mail Order Monsters", "Strategy + RPG + builder"),
            ("M.U.L.E.", "Strategy + economics + party"),
            ("Seven Cities of Gold", "Exploration + strategy"),
            ("Paradroid", "Puzzle + shooter + strategy")
        ]
    },
    14: {
        "name": "Complete Games",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 7169,
        "total_lessons": 512,
        "games": [
            ("Boulder Dash", "150 levels + editor"),
            ("Impossible Mission", "Complete mansion adventure"),
            ("Raid on Bungeling Bay", "Strategic bomber"),
            ("Elite", "Procedural galaxy trading"),
            ("The Last Ninja", "Multi-stage martial arts"),
            ("International Karate", "Tournament fighter"),
            ("Wizball", "Unique shooter-platformer"),
            ("Turrican", "Mega platformer-shooter synthesis")
        ]
    },
    15: {
        "name": "Technical Showcase & Epics",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 7681,
        "total_lessons": 512,
        "games": [
            ("Last Ninja 2", "Isometric perfection"),
            ("Creatures", "3D vector landscape horror"),
            ("Defender of the Crown", "Cinematic strategy epic"),
            ("Times of Lore", "Open-world action RPG"),
            ("Wasteland (Enhanced)", "Complete post-apoc RPG"),
            ("Ultima V", "NPC schedules, living world"),
            ("Mercenary", "Seamless 3D city"),
            ("The Sentinel", "Experimental 3D puzzle")
        ]
    },
    16: {
        "name": "The Gauntlet + Mastery Projects",
        "tiers": 8,
        "lessons_per_tier": 64,
        "start_lesson": 7681,
        "total_lessons": 512,
        "games": [
            ("Gauntlet Stage 1", "Arcade mastery test"),
            ("Gauntlet Stages 2-3", "Action + puzzle mastery"),
            ("Gauntlet Stages 4-5", "Platformer + brawler mastery"),
            ("Gauntlet Stages 6-7", "Shooter + RPG mastery"),
            ("Gauntlet Stage 8 + Final", "Ultimate synthesis boss"),
            ("Mastery Project 1", "Original game concept"),
            ("Mastery Project 2", "Technical showcase demo"),
            ("Magnum Opus", "Career-defining masterpiece")
        ]
    }
}

def create_phase_overview(phase_num, phase_data):
    """Create overview.md for a phase"""
    name = phase_data["name"]
    tiers = phase_data["tiers"]
    lessons_per_tier = phase_data["lessons_per_tier"]
    start = phase_data["start_lesson"]
    total = phase_data["total_lessons"]
    end = start + total - 1
    games = phase_data["games"]

    content = f"""# Phase {phase_num}: {name}

**Lessons:** {start}-{end} ({total} lessons)
**Structure:** {tiers} tiers × {lessons_per_tier} lessons per tier
**Focus:** {name}

## Philosophy

[Phase-specific philosophy - see PHASE-{phase_num}-CURRICULUM.md for details]

## Tier Structure

| Tier | Focus | Lessons | Deliverable |
|------|-------|---------|-------------|
"""

    for i, (game, desc) in enumerate(games, 1):
        tier_start = start + (i-1) * lessons_per_tier
        tier_end = tier_start + lessons_per_tier - 1
        content += f"| {i} | {game} | {tier_start}-{tier_end} | {desc} |\n"

    content += f"""
## Learning Outcomes

By completing Phase {phase_num}, you will have:
- [Outcome 1 - see curriculum file]
- [Outcome 2]
- [Outcome 3]

## Prerequisites

Phase {phase_num - 1 if phase_num > 1 else 0} complete

## Builds Toward

Phase {phase_num + 1 if phase_num < 16 else "Complete"} - [Next phase focus]
"""

    return content

def create_tier_readme(phase_num, tier_num, phase_data):
    """Create README.md for a tier"""
    name = phase_data["name"]
    lessons_per_tier = phase_data["lessons_per_tier"]
    start = phase_data["start_lesson"]
    games = phase_data["games"]

    if tier_num > len(games):
        return None

    game, desc = games[tier_num - 1]
    tier_start = start + (tier_num - 1) * lessons_per_tier
    tier_end = tier_start + lessons_per_tier - 1

    content = f"""# Tier {tier_num}: {game}

**Lessons:** {tier_start}-{tier_end} ({lessons_per_tier} lessons)
**Deliverable:** {desc}
**Complexity:** [Estimated lines of code/metrics]

## Goals

[What this tier teaches - see PHASE-{phase_num}-CURRICULUM.md for details]

## Game/System Requirements

- [Feature 1]
- [Feature 2]
- [Feature 3]

## Skills Introduced

### Hardware
- [VIC-II techniques]
- [CIA techniques]
- [SID techniques]

### Programming
- [Assembly patterns]
- [Algorithms]
- [Data structures]

## Lesson Breakdown

**Lessons {tier_start}-{tier_start+7}: [Section name]**
- Brief overview of what these lessons cover

**Lessons {tier_start+8}-{tier_start+15}: [Section name]**
- Brief overview

[Continue for all lesson groups in this tier]

## Technical Challenges

[Key technical problems solved in this tier]

## Builds Toward

**In This Phase:**
- Tier {tier_num + 1 if tier_num < len(games) else "Complete"}: [Next tier]

**In Next Phase:**
- [How this prepares for future phases]
"""

    return content

def main():
    """Generate all phase and tier documentation"""
    print(f"Generating documentation in: {BASE_DIR}")

    phase_count = 0
    tier_count = 0

    for phase_num, phase_data in PHASES.items():
        # Create phase directory
        phase_dir = BASE_DIR / f"phase-{phase_num}"
        phase_dir.mkdir(exist_ok=True)

        # Create phase overview
        overview_path = phase_dir / "overview.md"
        overview_content = create_phase_overview(phase_num, phase_data)
        overview_path.write_text(overview_content)
        phase_count += 1
        print(f"Created: phase-{phase_num}/overview.md")

        # Create tier directories and READMEs
        for tier_num in range(1, phase_data["tiers"] + 1):
            tier_dir = phase_dir / f"tier-{tier_num}"
            tier_dir.mkdir(exist_ok=True)

            readme_path = tier_dir / "README.md"
            readme_content = create_tier_readme(phase_num, tier_num, phase_data)

            if readme_content:
                readme_path.write_text(readme_content)
                tier_count += 1
                print(f"Created: phase-{phase_num}/tier-{tier_num}/README.md")

    print(f"\nSummary:")
    print(f"  Phase overviews created: {phase_count}")
    print(f"  Tier READMEs created: {tier_count}")
    print(f"  Total files created: {phase_count + tier_count}")
    print(f"\nNote: Content is templated. Review PHASE-*-CURRICULUM.md files")
    print(f"      for detailed content to fill in placeholders.")

if __name__ == "__main__":
    main()
