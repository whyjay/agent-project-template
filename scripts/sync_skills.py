#!/usr/bin/env python3
"""
Synchronize canonical skills into Agent-specific discovery folders.

Canonical source:
    skills/<skill-name>/SKILL.md

Generated copies:
    .agents/skills/<skill-name>/SKILL.md
    .claude/skills/<skill-name>/SKILL.md
"""

from __future__ import annotations

import argparse
import filecmp
from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "skills"
TARGET_ROOTS = [
    ROOT / ".agents" / "skills",
    ROOT / ".claude" / "skills",
]
IGNORE_PATTERNS = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def skill_dirs(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(
        [p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()],
        key=lambda p: p.name,
    )


def compare_dirs(left: Path, right: Path) -> list[str]:
    diffs: list[str] = []
    if not right.exists():
        return [f"missing target: {right.relative_to(ROOT)}"]

    cmp = filecmp.dircmp(left, right, ignore=["__pycache__", ".DS_Store"])
    for name in cmp.left_only:
        diffs.append(f"missing in target: {(right / name).relative_to(ROOT)}")
    for name in cmp.right_only:
        diffs.append(f"extra in target: {(right / name).relative_to(ROOT)}")
    for name in cmp.diff_files:
        diffs.append(f"different file: {(right / name).relative_to(ROOT)}")
    for name, subcmp in cmp.subdirs.items():
        diffs.extend(compare_dirs(left / name, right / name))
    return diffs


def sync(prune: bool = False) -> None:
    sources = skill_dirs(SOURCE_ROOT)
    source_names = {p.name for p in sources}

    for target_root in TARGET_ROOTS:
        target_root.mkdir(parents=True, exist_ok=True)

        for source in sources:
            target = target_root / source.name
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(source, target, ignore=IGNORE_PATTERNS)
            print(f"synced {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")

        if prune:
            for target in skill_dirs(target_root):
                if target.name not in source_names:
                    shutil.rmtree(target)
                    print(f"removed stale skill {target.relative_to(ROOT)}")


def check() -> int:
    sources = skill_dirs(SOURCE_ROOT)
    if not sources:
        print("No canonical skills found in skills/", file=sys.stderr)
        return 1

    all_diffs: list[str] = []
    for target_root in TARGET_ROOTS:
        for source in sources:
            target = target_root / source.name
            all_diffs.extend(compare_dirs(source, target))

    if all_diffs:
        for diff in all_diffs:
            print(diff, file=sys.stderr)
        return 1

    print("skills are synchronized")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Synchronize Agent skill copies.")
    parser.add_argument("--check", action="store_true", help="Only verify synchronization.")
    parser.add_argument("--prune", action="store_true", help="Remove copied skills absent from skills/.")
    args = parser.parse_args()

    if args.check:
        return check()

    sync(prune=args.prune)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
