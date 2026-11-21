"""TriggerBot: fires when the crosshair overlaps a target's hitbox."""
from __future__ import annotations

import time

import mouse
from loguru import logger

from src.roblox_bridge.process_attach import RobloxProcess
from src.shared.config import TriggerBotConfig


class TriggerBotHandler:
    def __init__(self, cfg: TriggerBotConfig, roblox: RobloxProcess) -> None:
        self.cfg = cfg
        self.roblox = roblox
        self._last_fire = 0.0

    def _crosshair_on_target(self) -> bool:
        # Placeholder for the world-to-screen hitbox overlap test
        return False

    def tick(self) -> None:
        if not self.cfg.enabled:
            return
        now = time.monotonic()
        if now - self._last_fire < self.cfg.fire_delay_ms / 1000.0:
            return
        if self._crosshair_on_target():
            mouse.click(button="left")
            self._last_fire = now
            logger.trace("TriggerBot fired")

    def shutdown(self) -> None:
        logger.debug("TriggerBotHandler stopped")