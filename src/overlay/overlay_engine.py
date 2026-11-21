"""Main loop: polls feature handlers at fixed tick and paints the overlay."""
from __future__ import annotations

import time

import pygame
from loguru import logger

from src.handlers import build_handlers
from src.roblox_bridge.process_attach import RobloxProcess
from src.shared.config import HubConfig

TICK_HZ = 144


class OverlayEngine:
    def __init__(self, cfg: HubConfig, roblox: RobloxProcess) -> None:
        self.cfg = cfg
        self.roblox = roblox
        self.handlers = build_handlers(cfg, roblox)
        self._running = False
        self._surface: pygame.Surface | None = None

    def _init_overlay(self) -> None:
        pygame.init()
        pygame.display.set_caption("rivals-script-hub overlay")
        self._surface = pygame.display.set_mode(
            (0, 0), pygame.NOFRAME | pygame.SRCALPHA
        )
        logger.info("Overlay surface created")

    def run(self) -> None:
        self._init_overlay()
        self._running = True
        frame_budget = 1.0 / TICK_HZ
        while self._running:
            t0 = time.perf_counter()
            for handler in self.handlers:
                handler.tick()
            pygame.display.flip()
            elapsed = time.perf_counter() - t0
            if elapsed < frame_budget:
                time.sleep(frame_budget - elapsed)

    def shutdown(self) -> None:
        self._running = False
        for handler in self.handlers:
            handler.shutdown()
        pygame.quit()
        logger.info("Overlay shutdown complete")