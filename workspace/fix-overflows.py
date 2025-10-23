import json

# Read the replacement file
with open('replacement-text.json', 'r') as f:
    data = json.load(f)

# Slides that need font size reduction based on overflow errors
# Round 3: Final aggressive reductions
overflow_fixes = {
    'slide-3': 42.0,  # Still 0.25" overflow -> go to 42pt
    'slide-4': 60.0,  # Fixed
    'slide-5': 42.0,  # Still 0.25" overflow -> go to 42pt
    'slide-8': 42.0,  # Still 0.25" overflow -> go to 42pt
    'slide-9': 48.0,  # Fixed
    'slide-11': 60.0,  # Fixed
    'slide-12': 42.0,  # Fixed
    'slide-13': 42.0,  # Fixed
    'slide-14': 42.0,  # Still 0.25" overflow -> go to 42pt
    'slide-15': 32.0,  # Still 0.49" overflow -> go to 32pt
    'slide-16': 48.0,  # Fixed
    'slide-19': 66.0,  # Fixed
    'slide-20': 54.0,  # Fixed
    'slide-21': 66.0,  # Fixed
    'slide-24': 48.0,  # Fixed
    'slide-25': 42.0,  # Still 0.25" overflow -> go to 42pt
    'slide-26': 42.0,  # Still 0.25" overflow -> go to 42pt
    'slide-28': 30.0,  # Still 1.29" overflow -> go to 30pt
    'slide-29': 54.0,  # Fixed
}

# Apply fixes
for slide, new_size in overflow_fixes.items():
    if slide in data and 'shape-0' in data[slide]:
        for para in data[slide]['shape-0']['paragraphs']:
            para['font_size'] = new_size

# Write back
with open('replacement-text-fixed.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Fixed {len(overflow_fixes)} slides")
