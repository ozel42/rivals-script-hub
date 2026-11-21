"""Locate and attach to the Roblox player process."""
from __future__ import annotations

from dataclasses import dataclass

import pymem
import pymem.process
from loguru import logger

ROBLOX_PROCESS_NAMES = ("RobloxPlayerBeta.exe", "Windows10Universal.exe")


@dataclass
class RobloxProcess:
    pid: int
    handle: pymem.Pymem
    base_address: int

    def is_alive(self) -> bool:
        try:
            self.handle.read_int(self.base_address)
            return True
        except Exception:
            return False


def _find_process() -> pymem.Pymem | None:
    for name in ROBLOX_PROCESS_NAMES:
        try:
            pm = pymem.Pymem(name)
            logger.debug(f"Found process {name} (pid={pm.process_id})")
            return pm
        except pymem.exception.ProcessNotFound:
            continue
    return None


def attach_to_roblox() -> RobloxProcess | None:
    pm = _find_process()
    if pm is None:
        return None
    module = pymem.process.module_from_name(pm.process_handle, "RobloxPlayerBeta.exe")
    if module is None:
        logger.warning("RobloxPlayerBeta.exe module not enumerated (UWP?)")
        return RobloxProcess(pid=pm.process_id, handle=pm, base_address=0)
    return RobloxProcess(pid=pm.process_id, handle=pm, base_address=module.lpBaseOfDll)