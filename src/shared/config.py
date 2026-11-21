"""Pydantic config model loaded from config/default.toml."""
from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field

try:
    import tomllib  # py3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore


class AimbotConfig(BaseModel):
    enabled: bool = True
    fov_px: int = 180
    smoothing: float = 0.35
    bone: str = "head"


class TriggerBotConfig(BaseModel):
    enabled: bool = True
    fire_delay_ms: int = 90
    hitbox: str = "torso"


class NoClipConfig(BaseModel):
    enabled: bool = False
    restore_on_disable: bool = True


class EspConfig(BaseModel):
    enabled: bool = True
    names: bool = True
    head_dot: bool = True
    tracers: bool = False


class HubConfig(BaseModel):
    aimbot: AimbotConfig = Field(default_factory=AimbotConfig)
    triggerbot: TriggerBotConfig = Field(default_factory=TriggerBotConfig)
    noclip: NoClipConfig = Field(default_factory=NoClipConfig)
    esp: EspConfig = Field(default_factory=EspConfig)


def load_config(path: str | Path = "config/default.toml") -> HubConfig:
    p = Path(path)
    if not p.exists():
        return HubConfig()
    with p.open("rb") as f:
        data = tomllib.load(f)
    return HubConfig(**data)