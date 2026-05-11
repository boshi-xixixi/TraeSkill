#!/usr/bin/env python3
"""
TraeSkill → Cursor IDE Adapter
================================
Reads .trae/Skills/ and generates a Cursor-compatible .cursor/skills/ directory.

Features:
- Non-invasive: never modifies any file under .trae/Skills/
- Dynamic: re-running always reflects the latest state of .trae/Skills/
- Merges AGENTS.md content into the generated SKILL.md when present
- Copies references/, scripts/, assets/ subdirectories verbatim

Usage:
    python cursor_adapter/install.py
"""

import re
import shutil
import sys
from pathlib import Path

TRAE_SKILLS_DIR = ".trae/Skills"
CURSOR_SKILLS_DIR = ".cursor/skills"
SKILL_DIR_PATTERN = re.compile(r"^\d{2,}_")

AGENTS_MERGE_HEADER = """

---

## Cursor Agent Persona

<!-- The following content is auto-merged from AGENTS.md for Cursor IDE -->

"""


def find_project_root() -> Path:
    """Walk up from cwd until we find .trae/Skills or give up."""
    candidate = Path.cwd()
    for _ in range(5):
        if (candidate / TRAE_SKILLS_DIR).is_dir():
            return candidate
        candidate = candidate.parent
    print(f"Error: could not find '{TRAE_SKILLS_DIR}' from {Path.cwd()}", file=sys.stderr)
    sys.exit(1)


def copy_resource_dirs(src_skill_dir: Path, dst_skill_dir: Path) -> None:
    for sub in ("references", "scripts", "assets"):
        src = src_skill_dir / sub
        dst = dst_skill_dir / sub
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)


def install_skill(skill_dir: Path, cursor_skills_root: Path) -> bool:
    """
    Install one skill into .cursor/skills/.
    Returns True if AGENTS.md was merged.
    """
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False

    dst_dir = cursor_skills_root / skill_dir.name
    dst_dir.mkdir(parents=True, exist_ok=True)

    skill_content = skill_md.read_text(encoding="utf-8")

    agents_md = skill_dir / "AGENTS.md"
    merged_agents = False
    if agents_md.exists():
        agents_content = agents_md.read_text(encoding="utf-8")
        skill_content = skill_content.rstrip() + AGENTS_MERGE_HEADER + agents_content
        merged_agents = True

    (dst_dir / "SKILL.md").write_text(skill_content, encoding="utf-8")

    copy_resource_dirs(skill_dir, dst_dir)

    return merged_agents


def main() -> None:
    root = find_project_root()
    trae_skills_root = root / TRAE_SKILLS_DIR
    cursor_skills_root = root / CURSOR_SKILLS_DIR

    # Wipe and recreate to ensure a clean, idempotent state on every run
    if cursor_skills_root.exists():
        shutil.rmtree(cursor_skills_root)
    cursor_skills_root.mkdir(parents=True)

    skill_dirs = sorted(
        d for d in trae_skills_root.iterdir()
        if d.is_dir() and SKILL_DIR_PATTERN.match(d.name)
    )

    if not skill_dirs:
        print(f"No skills found in {trae_skills_root}")
        sys.exit(0)

    total = 0
    merged = 0

    for skill_dir in skill_dirs:
        had_agents = install_skill(skill_dir, cursor_skills_root)
        total += 1
        if had_agents:
            merged += 1
        status = "(+AGENTS.md)" if had_agents else ""
        print(f"  ✓  {skill_dir.name} {status}".rstrip())

    print()
    print("=" * 50)
    print(f"Cursor adapter installed successfully.")
    print(f"  Skills generated : {total}")
    print(f"  AGENTS.md merged : {merged}")
    print(f"  Output directory : {cursor_skills_root.relative_to(root)}")
    print("=" * 50)
    print()
    print("Cursor will auto-detect .cursor/skills/ in this project.")
    print("Re-run this script any time to sync with the latest .trae/Skills/ changes.")


if __name__ == "__main__":
    main()
