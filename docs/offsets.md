# Offsets

Roblox rotates internal class offsets on almost every patch. `src/shared/offsets.py`
is the source of truth for the current build. When aimbot/ESP break:

1. Run `python scripts/dump_offsets.py` on a fresh Roblox session.
2. Diff the JSON against `src/shared/offsets.py`.
3. Update `offsets/latest.json` and bump `VERSION`.

Known fragile offsets:
- `can_collide` (NoClip) — moved twice in Feb 2026.
- `root_part` — depends on R6 vs R15 rigs.