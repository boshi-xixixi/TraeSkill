---
name: gbr-pair
description: Pair a phone running Build Remote Agent to this Trae (or Cursor) desktop session via gbr/1. Use when the user wants a mobile spectator. Attach only Bot API 127.0.0.1:8788 or gbr-mcp stdio. Requires gbr-agent v0.6.0+.
---

# Build Remote Agent pairing

## Description

Pair the Build Remote Agent phone app to this Trae session through the free MIT `gbr-agent`. Phone is spectator + veto, not orchestrator. Protocol `gbr/1`.

Independent product by Linespotting AB. Not affiliated with xAI or SpaceX.

Website: https://grokbuildremote.com/
Agent: https://github.com/LinespottingOrg/GrokBuildRemote-Agents

## Usage Scenario

- User asks to pair a phone, spectate from mobile, or attach Build Remote Agent.
- User wants inject/veto from a phone while Trae (or Cursor via `cursor_adapter`) runs on the desktop.

## Instructions

1. Install (macOS/Linux): `curl -fsSL https://grokbuildremote.com/install.sh | bash`
2. `gbr-agent version` — need **v0.6.0+**.
3. `gbr-agent pair` — browser QR **and** printed 8-char code.
4. Phone: Build Remote Agent → scan QR **or** type the 8-char code.
5. `gbr-agent run` (leave running).
6. Attach only `http://127.0.0.1:8788` or stdio `gbr-mcp`. Trae: `.trae/mcp.json`. Cursor: `.cursor/mcp.json` after `python cursor_adapter/install.py`.
7. Verify: `curl -sS http://127.0.0.1:8788/health`
8. Never commit mailbox keys. Unpair on the phone before a new mailbox.

Loop: diagnose → open/attach → lock → inject → wait idle → harvest excerpt → iterate or close.
