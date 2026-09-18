"""Inspect the retained BASIC source; not a native playtest."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
source=root.parents[4]/'code-samples/sinclair-zx-spectrum/basic/the-caverns/unit-06/caverns.bas'
# docs/platforms/system/games/game -> Code198x via five parent levels
text=source.read_text();rows=[]
for s in text.splitlines():
 match=re.match(r'\s*(\d+) DATA ([0-9,]+)$',s)
 if match and 1010<=int(match[1])<=1200:rows.append(list(map(int,match[2].split(','))))
assert len(rows)==20
assert rows[0]==[0,5,2,0]
assert 5 in rows[5] and 6 not in rows[0]
seen={1};todo=[1]
while todo:
 for nxt in rows[todo.pop()-1]:
  if nxt and nxt not in seen:seen.add(nxt);todo.append(nxt)
assert len(seen)==20
report={'source':'sinclair-zx-spectrum/basic/the-caverns/unit-06/caverns.bas','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'rooms_reachable_without_hazards':len(seen),'start_neighbours':rows[0],'counterexample':{'player':1,'pit':20,'creature':6,'player_action':'south to room 5','creature_action':'west to room 5','observation':'No initial creature-adjacency clue at room 1, but the same turn can end in capture after moving to room 5.'},'limits':'Source-derived graph and turn-order evidence. No emulator execution of the retained game.'}
(root/'verification/review.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
