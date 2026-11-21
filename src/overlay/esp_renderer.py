"""Draws box ESP / tracers / names over the Roblox window."""
from __future__ import annotations

import pygame
from loguru import logger

from src.shared.config import EspConfig
from src.shared.types import WorldEntity


class EspRenderer:
    BOX_COLOR = (0, 255, 140)
    HEAD_COLOR = (255, 60, 60)
    TEAM_COLOR = (60, 160, 255)

    def __init__(self, surface: pygame.Surface, cfg: EspConfig) -> None:
        self.surface = surface
        self.cfg = cfg

    def _project(self, entity: WorldEntity) -> tuple[int, int, int, int]:
        screen = entity.screen_box
        if screen is None:
            raise ValueError("entity has no projected screen box")
        return screen

    def draw_entity(self, entity: WorldEntity) -> None:
        if not entity.alive or entity.local_player:
            return
        try:
            x, y, w, h = self._project(entity)
        except ValueError:
            return
        color = self.TEAM_COLOR if entity.teammate else self.BOX_COLOR
        pygame.draw.rect(self.surface, color, (x, y, w, h), width=1)
        if self.cfg.head_dot:
            pygame.draw.circle(self.surface, self.HEAD_COLOR, (x + w // 2, y), 3)
        if self.cfg.names and entity.display_name:
            font = pygame.font.SysFont("consolas", 12)
            label = font.render(entity.display_name, True, color)
            self.surface.blit(label, (x, y - 14))

    def draw_fov_ring(self, center: tuple[int, int], radius: int) -> None:
        pygame.draw.circle(self.surface, (255, 255, 255), center, radius, width=1)