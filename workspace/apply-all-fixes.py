import json

# Read the condensed text file (which now has slides 8,14,15,25,26,28 condensed)
with open('replacement-text-condensed.json', 'r') as f:
    data = json.load(f)

# Apply font size fixes from fix-overflows.py for all other slides
overflow_fixes = {
    'slide-3': 42.0,
    'slide-4': 60.0,
    'slide-5': 42.0,
    # slide-8 already fixed with condensed text
    'slide-9': 48.0,
    'slide-11': 60.0,
    'slide-12': 42.0,
    'slide-13': 42.0,
    # slide-14 already fixed with condensed text
    # slide-15 already fixed with condensed text
    'slide-16': 48.0,
    'slide-19': 66.0,
    'slide-20': 54.0,
    'slide-21': 66.0,
    'slide-24': 48.0,
    # slide-25 already fixed with condensed text
    # slide-26 already fixed with condensed text
    # slide-28 already fixed with condensed text
    'slide-29': 54.0,
}

# Apply font size fixes to slides that need them
for slide, new_size in overflow_fixes.items():
    if slide in data and 'shape-0' in data[slide]:
        for para in data[slide]['shape-0']['paragraphs']:
            para['font_size'] = new_size

# Write back
with open('replacement-text-final.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Applied font size fixes to {len(overflow_fixes)} slides")
print("Applied condensed text to slides: 8, 14, 15, 25, 26, 28")
print("Output: replacement-text-final.json")
