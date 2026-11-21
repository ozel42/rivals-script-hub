"""Entry point — validates environment, loads config, starts the hub."""
from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger

from src.overlay.overlay_engine import OverlayEngine
from src.roblox_bridge.process_attach import attach_to_roblox
from src.shared.config import load_config


def _setup_logging() -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    logger.add(log_dir / "hub_{time:%Y%m%d}.log", rotation="10 MB", level="DEBUG")


def main() -> int:
    _setup_logging()
    logger.info("rivals-script-hub starting (2026 build)")

    cfg = load_config()
    proc = attach_to_roblox()
    if proc is None:
        logger.error("Roblox not running — launch RIVALS first, then re-run.")
        return 1

    logger.success(f"Attached to Roblox PID={proc.pid}")
    engine = OverlayEngine(cfg=cfg, roblox=proc)

    try:
        engine.run()
    except KeyboardInterrupt:
        logger.info("Shutdown requested (Ctrl+C)")
    finally:
        engine.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())