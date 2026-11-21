"""Shared dataclasses used across overlay, handlers and roblox bridge."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Vec3:
    x: float
    y: float
    z: float


@dataclass
class WorldEntity:
    address: int
    display_name: str | None = None
    position: Vec3 = field(default_factory=lambda: Vec3(0, 0, 0))
    screen_box: tuple[int, int, int, int] | None = None
    alive: bool = True
    teammate: bool = False
    local_player: bool = False