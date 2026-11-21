"""Roblox 2026 memory offsets — rotate these when the game patches."""
from __future__ import annotations

VERSION = "2026.03.11"

OFFSETS: dict[str, object] = {
    "players_chain": [0x5A0, 0x48, 0x0],       # Game -> Players
    "local_humanoid_chain": [0x5A0, 0x230, 0x18],
    "can_collide": 0x18C,
    "humanoid_health": 0x184,
    "root_part": 0x1A0,
    "workspace": 0x5B8,
}