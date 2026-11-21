"""Helper: dump humanoid + root-part offsets for a running Roblox session."""
from __future__ import annotations

import json
from pathlib import Path

from loguru import logger

from src.roblox_bridge.process_attach import attach_to_roblox
from src.shared.offsets import OFFSETS, VERSION


def main() -> int:
    proc = attach_to_roblox()
    if proc is None:
        logger.error("Roblox not running")
        return 1
    out = Path("offsets/dumped.json")
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({"version": VERSION, "offsets": OFFSETS}, indent=2))
    logger.success(f"Offsets dumped to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())