import json

# Read the current file
with open('replacement-text-condensed.json', 'r') as f:
    data = json.load(f)

# Slide 8: Remove "Starting with" and "complete"
data['slide-8']['shape-0']['paragraphs'] = [
    {
        "text": "Commodore 64:",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "8,256 lessons",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    },
    {
        "text": "100+ games",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    }
]

# Slide 14: Change to "lessons" and "Shmups"
data['slide-14']['shape-0']['paragraphs'] = [
    {
        "text": "8,192 lessons.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "100+ games.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "Pong → Platformers →",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    },
    {
        "text": "RPGs → Shmups.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    }
]

# Slide 15: Condense to 4 lines
data['slide-15']['shape-0']['paragraphs'] = [
    {
        "text": "Beyond 1980s games.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 32.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "Demoscene tricks.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 32.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "Modern techniques.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 32.0,
        "bold": True,
        "color": "01A9F5"
    },
    {
        "text": "State-of-the-art retro.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 32.0,
        "bold": True,
        "color": "01A9F5"
    }
]

# Slide 25: Remove t-shirts
data['slide-25']['shape-0']['paragraphs'] = [
    {
        "text": "Like it?",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "GitHub Sponsors. Patreon.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    },
    {
        "text": "Keep it sustainable.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    }
]

# Slide 26: Shorten
data['slide-26']['shape-0']['paragraphs'] = [
    {
        "text": "Discord. GitHub Discussions.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "Share games.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    },
    {
        "text": "Learn together.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 42.0,
        "bold": True,
        "color": "01A9F5"
    }
]

# Slide 28: Major condensing
data['slide-28']['shape-0']['paragraphs'] = [
    {
        "text": "Test & report bugs.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 30.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "Your childhood machine?",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 30.0,
        "bold": True,
        "color": "5D5B7A"
    },
    {
        "text": "Try with kids.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 30.0,
        "bold": True,
        "color": "01A9F5"
    },
    {
        "text": "Help build 70 systems.",
        "alignment": "CENTER",
        "font_name": "SN Pro Heavy",
        "font_size": 30.0,
        "bold": True,
        "color": "01A9F5"
    }
]

# Write back
with open('replacement-text-condensed.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Applied condensed text to slides: 8, 14, 15, 25, 26, 28")
