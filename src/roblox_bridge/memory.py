"""Thin wrapper around pymem with cached reads and offset resolution."""
from __future__ import annotations

import struct
from typing import Any

from loguru import logger

from .process_attach import RobloxProcess


class MemoryReader:
    def __init__(self, roblox: RobloxProcess) -> None:
        self._rp = roblox
        self._pm = roblox.handle

    def read(self, address: int, size: int) -> bytes | None:
        try:
            return self._pm.read_bytes(address, size)
        except Exception as exc:
            logger.debug(f"read @ {address:#x} failed: {exc}")
            return None

    def read_ptr(self, address: int) -> int | None:
        buf = self.read(address, 8)
        return struct.unpack("<Q", buf)[0] if buf else None

    def read_float3(self, address: int) -> tuple[float, float, float] | None:
        buf = self.read(address, 12)
        if not buf:
            return None
        return struct.unpack("<fff", buf)

    def follow(self, base: int, offsets: list[int]) -> int | None:
        """Walk a pointer chain from base."""
        addr: Any = base
        for off in offsets:
            addr = self.read_ptr(addr + off)
            if not addr:
                return None
        return addr