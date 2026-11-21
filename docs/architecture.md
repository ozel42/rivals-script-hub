# Architecture

```
bootstrap/launcher.py
      │
      ▼
roblox_bridge.process_attach ──► pymem handle
      │
      ▼
overlay.overlay_engine ──► handlers/*.tick()
                              │
      ┌───────────────────────┼────────────────────────┐
      ▼                       ▼                        ▼
  Aimbot                 TriggerBot                NoClip / ESP
      │                       │                        │
      └──────────► shared.offsets / shared.types ◄─────┘
                              │
                              ▼
                    overlay.esp_renderer (pygame surface)
```

Executor bridge is optional and used only when the user wants to push Lua
payloads to a Synapse/Fluxus/Solara install instead of pure memory patching.