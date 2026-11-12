#!/usr/bin/env python3
"""Keep portable in-repository Skill copies byte-identical to the canonical tree."""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "skills" / "elon-musk-communication"
MIRRORS = [
    ROOT / ".agents/skills/elon-musk-communication",
    ROOT / ".codex/skills/elon-musk-communication",
    ROOT / ".pi/skills/elon-musk-communication",
    ROOT / ".opencode/skills/elon-musk-communication",
]


def files_under(base: Path) -> dict[str, bytes]:
    if not base.is_dir():
        return {}
    return {
        str(p.relative_to(base)): p.read_bytes()
        for p in base.rglob("*") if p.is_file()
    }


def check() -> list[str]:
    expected = files_under(CANONICAL)
    if "SKILL.md" not in expected:
        return ["Canonical SKILL.md is missing"]
    errors = []
    for folder in MIRRORS:
        actual = files_under(folder)
        if expected != actual:
            missing = sorted(set(expected) - set(actual))
            extra = sorted(set(actual) - set(expected))
            different = sorted(k for k in set(expected) & set(actual)
                               if actual[k] != expected[k])
            errors.append(f"{folder.relative_to(ROOT)}: missing={missing} extra={extra} changed={different}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check instead of writing")
    args = parser.parse_args(argv)
    if args.check:
        errors = check()
        if errors:
            for error in errors:
                print("FAIL: " + error, file=sys.stderr)
            return 1
        print("PASS: all four Skill mirrors match the canonical tree")
        return 0

    if not (CANONICAL / "SKILL.md").is_file():
        print("ERROR: canonical SKILL.md missing", file=sys.stderr)
        return 1
    for destination in MIRRORS:
        if destination.is_symlink() or destination.is_file():
            destination.unlink()
        elif destination.exists():
            shutil.rmtree(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(CANONICAL, destination)
        print("Synced: " + str(destination.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
