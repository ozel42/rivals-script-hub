# Contributing to rivals-script-hub

Thanks for wanting to help improve the RIVALS (Roblox) Script Hub.

## Ground rules

- This project is a hobbyist / educational modding tool for RIVALS on Roblox. Use it only on your own accounts and in private servers.
- No malware, no wallet stealers, no RAT payloads. PRs containing those will be reported.
- Keep PRs focused. One feature per PR.

## Development setup

```powershell
git clone https://github.com/yourname/rivals-script-hub
cd rivals-script-hub
py -3.11 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python -m src.bootstrap
```

## Folder overview

- `src/bootstrap/` — startup, config loading, executor detection
- `src/overlay/` — DirectX overlay + ESP renderer, aim FOV ring
- `src/handlers/` — Aimbot / TriggerBot / NoClip / ESP feature handlers
- `src/roblox_bridge/` — Roblox process attach, memory read, module base scan
- `src/executor_hooks/` — Lua executor bridges (Synapse-like, Fluxus-like)
- `src/shared/` — config models, offsets, shared types

## Code style

- Python 3.11+, type hints required in public APIs.
- Run `python -m compileall src` before opening a PR.
- Keep handlers free of hardcoded offsets — pull from `src/shared/offsets.py`.