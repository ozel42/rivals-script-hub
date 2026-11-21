# Security Policy

## Scope

`rivals-script-hub` is a desktop tool that attaches to the Roblox player process
and renders an overlay for RIVALS. Because of that, "security" here means:

- **No external network calls** other than the update check against this repo.
- **No credential harvesting** — we do not read browser data, wallets, or cookies.
- **No auto-executing binaries** fetched at runtime.

## Reporting a vulnerability

Please open a private security advisory on GitHub, or DM the maintainer on the
project Discord. Do NOT file a public issue for anything that would let a
skid pivot a user's machine.

We aim to respond within 72 hours.

## Supported versions

| Version | Supported |
|---------|-----------|
| 2026.x  | ✅        |
| 2025.x  | ❌        |

## Known limitations

- Memory offsets break on every Roblox update — expect occasional downtime.
- The overlay is blocked by fullscreen-exclusive anti-cheat sessions.