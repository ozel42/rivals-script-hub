"""ESP handler — resolves entities each tick and hands them to the renderer."""
from __future__ import annotations

from loguru import logger

from src.roblox_bridge.process_attach import RobloxProcess
from src.shared.config import EspConfig
from src.shared.types import WorldEntity


class EspHandler:
    def __init__(self, cfg: EspConfig, roblox: RobloxProcess) -> None:
        self.cfg = cfg
        self.roblox = roblox
        self._entities: list[WorldEntity] = []

    def collect(self) -> list[WorldEntity]:
        # Real implementation walks the Players cache and projects boxes
        return []

    def tick(self) -> None:
        self._entities = self.collect()
        if self._entities:
            logger.trace(f"ESP: {len(self._entities)} entities in view")

    def entities(self) -> list[WorldEntity]:
        return self._entities

    def shutdown(self) -> None:
        logger.debug("EspHandler stopped")