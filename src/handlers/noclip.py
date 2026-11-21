"""NoClip: patches the local Humanoid state to disable collision."""
from __future__ import annotations

from loguru import logger

from src.roblox_bridge.memory import MemoryReader
from src.roblox_bridge.process_attach import RobloxProcess
from src.shared.config import NoClipConfig
from src.shared.offsets import OFFSETS


class NoClipHandler:
    def __init__(self, cfg: NoClipConfig, roblox: RobloxProcess) -> None:
        self.cfg = cfg
        self.mem = MemoryReader(roblox)
        self._patched = False

    def _local_humanoid(self) -> int | None:
        return self.mem.follow(0, OFFSETS["local_humanoid_chain"])

    def _patch(self, humanoid: int) -> None:
        try:
            self.mem._pm.write_uchar(humanoid + OFFSETS["can_collide"], 0)
            logger.info(f"NoClip patched at {humanoid:#x}")
        except Exception as exc:
            logger.warning(f"NoClip patch failed: {exc}")

    def tick(self) -> None:
        if not self.cfg.enabled or self._patched:
            return
        humanoid = self._local_humanoid()
        if humanoid:
            self._patch(humanoid)
            self._patched = True

    def shutdown(self) -> None:
        logger.debug("NoClipHandler stopped")