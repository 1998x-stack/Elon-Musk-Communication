#!/usr/bin/env python3
"""Install the complete portable skill into a supported agent directory."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "elon-musk-communication"
SKILL_NAME = "elon-musk-communication"

PROJECT_DIRS = {
    "codex": ".agents/skills",
    "claude": ".claude/skills",
    "pi": ".pi/skills",
    "opencode": ".opencode/skills",
    "cursor": ".cursor/skills",
}
USER_DIRS = {
    "codex": ".agents/skills",
    "claude": ".claude/skills",
    "pi": ".pi/agent/skills",
    "opencode": ".config/opencode/skills",
    "cursor": ".cursor/skills",
}


def plan(agent: str, scope: str, project: Path | None = None, home: Path | None = None):
    """Return destination paths; do not modify the filesystem."""
    if scope == "project":
        base = (project or Path.cwd()).expanduser().resolve()
        if not base.is_dir():
            raise ValueError("Project directory does not exist: " + str(base))
        relative = PROJECT_DIRS[agent]
    else:
        base = (home or Path.home()).expanduser().resolve()
        relative = USER_DIRS[agent]

    skill_destination = base / relative / SKILL_NAME
    extra = []
    if agent == "cursor" and scope == "project":
        extra.append((ROOT / ".cursor/rules/elon-musk-communication.mdc",
                      base / ".cursor/rules/elon-musk-communication.mdc"))
    return skill_destination, extra


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True, choices=sorted(PROJECT_DIRS))
    parser.add_argument("--scope", choices=("project", "user"), default="project")
    parser.add_argument("--project", type=Path, help="Target directory for --scope project (default: cwd)")
    parser.add_argument("--dry-run", action="store_true", help="Print intended paths, write nothing")
    parser.add_argument("--force", action="store_true", help="Replace an existing installation explicitly")
    args = parser.parse_args(argv)
    if args.scope == "user" and args.project:
        parser.error("--project is only valid with --scope project")
    if not (SOURCE / "SKILL.md").is_file():
        parser.error("Missing canonical Skill source")
    try:
        destination, extra = plan(args.agent, args.scope, args.project)
    except ValueError as error:
        parser.error(str(error))

    write_targets = [destination] + [dst for _, dst in extra]
    if not args.force:
        existing = [str(path) for path in write_targets if path.exists() or path.is_symlink()]
        if existing:
            parser.error("Destination exists; refusing to overwrite: " + ", ".join(existing) +
                         " (use --force only if replacement is intentional)")

    print("Skill: " + str(SOURCE) + " -> " + str(destination))
    for src, dst in extra:
        print("Rule: " + str(src) + " -> " + str(dst))
    if args.dry_run:
        return 0

    if destination.is_symlink() or destination.is_file():
        destination.unlink()
    elif destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination)

    for src, dst in extra:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        elif dst.exists():
            raise RuntimeError("Not a file: " + str(dst))
        shutil.copy2(src, dst)

    print("Installed: " + str(destination))
    return 0


if __name__ == "__main__":
    sys.exit(main())
