"""Aimbot: finds closest target within FOV and drives the mouse toward it."""
from __future__ import annotations

import math

import mouse
from loguru import logger

from src.roblox_bridge.memory import MemoryReader
from src.roblox_bridge.process_attach import RobloxProcess
from src.shared.config import AimbotConfig
from src.shared.offsets import OFFSETS


class AimbotHandler:
    def __init__(self, cfg: AimbotConfig, roblox: RobloxProcess) -> None:
        self.cfg = cfg
        self.mem = MemoryReader(roblox)
        self._mouse_down = False

    def _candidates(self) -> list[tuple[float, float]]:
        # In real builds this walks the Players → Character → HumanoidRootPart chain
        base = self.mem.follow(0, OFFSETS["players_chain"])
        if base is None:
            return []
        return []

    def _best_target(self, cursor: tuple[int, int]) -> tuple[float, float] | None:
        best: tuple[float, float] | None = None
        best_d = self.cfg.fov_px
        for sx, sy in self._candidates():
            d = math.hypot(sx - cursor[0], sy - cursor[1])
            if d < best_d:
                best, best_d = (sx, sy), d
        return best

    def tick(self) -> None:
        if not mouse.is_pressed(button="right"):
            self._mouse_down = False
            return
        self._mouse_down = True
        cursor = mouse.get_position()
        target = self._best_target(cursor)
        if target is None:
            return
        dx = (target[0] - cursor[0]) * self.cfg.smoothing
        dy = (target[1] - cursor[1]) * self.cfg.smoothing
        mouse.move(cursor[0] + dx, cursor[1] + dy, absolute=True)

    def shutdown(self) -> None:
        logger.debug("AimbotHandler stopped")