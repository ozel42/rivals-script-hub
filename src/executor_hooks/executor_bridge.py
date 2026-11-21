"""Bridges to common Roblox Lua executors for pushing our script payloads."""
from __future__ import annotations

import subprocess
from pathlib import Path

from loguru import logger

KNOWN_EXECUTOR_PATHS = {
    "synapse": Path(r"%LOCALAPPDATA%\Synapse\bin\synapse.exe"),
    "fluxus": Path(r"%LOCALAPPDATA%\Fluxus\fluxus.bin"),
    "solara": Path(r"%LOCALAPPDATA%\Solara\solara.exe"),
}


class ExecutorBridge:
    def __init__(self, executor: str, exe: Path) -> None:
        self.executor = executor
        self.exe = exe

    def execute(self, lua_source: str) -> bool:
        script = Path("scripts/generated/_rivals_payload.lua")
        script.parent.mkdir(parents=True, exist_ok=True)
        script.write_text(lua_source, encoding="utf-8")
        try:
            subprocess.run(
                [str(self.exe), "--script", str(script)],
                check=True,
                timeout=30,
            )
            logger.success(f"Payload pushed via {self.executor}")
            return True
        except subprocess.SubprocessError as exc:
            logger.error(f"Executor {self.executor} failed: {exc}")
            return False


def detect_executor() -> ExecutorBridge | None:
    for name, path in KNOWN_EXECUTOR_PATHS.items():
        expanded = Path(str(path).replace("%LOCALAPPDATA%", str(Path.home() / "AppData/Local")))
        if expanded.exists():
            logger.info(f"Detected executor: {name}")
            return ExecutorBridge(name, expanded)
    return None