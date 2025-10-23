#!/bin/bash

# Script to generate all phase overview and tier README files

# Phase 1: 16 tiers, 32 lessons each
# Phases 2-4: 8 tiers, 64 lessons each (but Phase 1 has 16 games so special case)
# Continue pattern for all 16 phases

# Phase data (phase_num:tier_count:lessons_per_tier:start_lesson)
PHASES=(
  "1:16:32:1"      # Phase 1: 1-512
  "2:8:64:513"     # Phase 2: 513-1024
  "3:8:64:1025"    # Phase 3: 1025-1536
  "4:8:64:1537"    # Phase 4: 1537-2048
  "5:8:48:2049"    # Phase 5: 2049-2432
  "6:16:64:2433"   # Phase 6: 2433-3456
  "7:8:128:3457"   # Phase 7: 3457-4480
  "8:8:64:4481"    # Phase 8: 4481-4992
  "9:8:64:4993"    # Phase 9: 4993-5504
  "10:8:48:5505"   # Phase 10: 5505-5888
  "11:8:48:5889"   # Phase 11: 5889-6272
  "12:8:48:6273"   # Phase 12: 6273-6656
  "13:8:64:6657"   # Phase 13: 6657-7168
  "14:8:64:7169"   # Phase 14: 7169-7680
  "15:8:64:7681"   # Phase 15: 7681-8192
  "16:8:64:7681"   # Phase 16: 7681-8192 (same as 15, special structure)
)

# Create directories for all phases
for phase in {1..16}; do
  mkdir -p "/Users/stevehill/Projects/Code198x/docs/commodore-64/phase-${phase}"
done

echo "Created all phase directories"
echo "Phase overviews and tier READMEs need to be generated from curriculum files"
echo "This requires parsing the curriculum markdown files"
echo ""
echo "Due to the complexity and size (272 files), this should be done with a proper script"
echo "that reads the curriculum files and extracts tier information."
