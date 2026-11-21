# Pulls the latest offsets JSON from the RIVALS hub CDN mirror.
$ErrorActionPreference = "Stop"
$dest = Join-Path $PSScriptRoot "..\offsets\latest.json"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/rivals-hub/offsets/main/rivals.json" -OutFile $dest
Write-Host "Offsets refreshed -> $dest"