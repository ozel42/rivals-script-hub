from __future__ import annotations

from typing import TYPE_CHECKING

from .aimbot import AimbotHandler
from .triggerbot import TriggerBotHandler
from .noclip import NoClipHandler
from .esp import EspHandler

if TYPE_CHECKING:
    from src.roblox_bridge.process_attach import RobloxProcess
    from src.shared.config import HubConfig


def build_handlers(cfg: "HubConfig", roblox: "RobloxProcess") -> list:
    handlers = []
    if cfg.aimbot.enabled:
        handlers.append(AimbotHandler(cfg.aimbot, roblox))
    if cfg.triggerbot.enabled:
        handlers.append(TriggerBotHandler(cfg.triggerbot, roblox))
    if cfg.noclip.enabled:
        handlers.append(NoClipHandler(cfg.noclip, roblox))
    if cfg.esp.enabled:
        handlers.append(EspHandler(cfg.esp, roblox))
    return handlers


__all__ = [
    "build_handlers",
    "AimbotHandler",
    "TriggerBotHandler",
    "NoClipHandler",
    "EspHandler",
]