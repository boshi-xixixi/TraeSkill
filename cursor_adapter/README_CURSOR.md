# Cursor IDE Adapter for TraeSkill

This directory contains a non-invasive adapter that makes all TraeSkill skills available in [Cursor IDE](https://cursor.sh).

## How It Works

`install.py` reads `.trae/Skills/` at runtime and generates a Cursor-compatible `.cursor/skills/` directory. The original `.trae/Skills/` files are **never modified**.

- `SKILL.md` — copied as-is (format is already Cursor-compatible)
- `AGENTS.md` — content auto-merged into the generated `SKILL.md` under a `## Cursor Agent Persona` section
- `references/`, `scripts/`, `assets/` — copied verbatim

## Installation

From the TraeSkill project root, run:

```bash
python cursor_adapter/install.py
```

Cursor will automatically detect `.cursor/skills/` and activate the AI skills.

## Keeping Skills Up to Date

When the original project adds or updates skills, simply re-run:

```bash
python cursor_adapter/install.py
```

No changes to the adapter code are needed. The adapter always reflects the current state of `.trae/Skills/`.

## Notes

- `.cursor/` is listed in `.gitignore` — generated files do not enter version control
- This adapter does not modify any existing project files
