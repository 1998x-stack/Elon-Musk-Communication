#!/usr/bin/env python3
"""Static, dependency-free validation for the portable executive email Skill."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills/elon-musk-communication"
EXPECTED = [
    "README.md", "README.zh.md", "EXAMPLES.md", "AGENTS.md", "CLAUDE.md",
    "CURSOR.md", "INSTALL.md", "LICENSE",
    "skills/elon-musk-communication/SKILL.md",
    "skills/elon-musk-communication/references/principles.md",
    "skills/elon-musk-communication/references/bad-news-playbook.md",
    "skills/elon-musk-communication/references/scenarios.md",
    "skills/elon-musk-communication/references/evidence-and-attribution.md",
    "skills/elon-musk-communication/assets/templates/README.md",
    ".claude-plugin/marketplace.json", ".claude-plugin/plugin.json",
    ".cursor/rules/elon-musk-communication.mdc",
    ".github/workflows/validate.yml",
]


def validate() -> list[str]:
    errors = []
    for path in EXPECTED:
        if not (ROOT / path).is_file():
            errors.append("Missing required file: " + path)

    skill_file = SKILL_DIR / "SKILL.md"
    if not skill_file.is_file():
        return errors
    raw = skill_file.read_text(encoding="utf-8")
    if not raw.startswith("---\n") or "\n---\n" not in raw[4:]:
        errors.append("SKILL.md: invalid YAML frontmatter delimiters")
    else:
        front = raw.split("---", 2)[1]
        matches = dict(re.findall(r"^(name|description|license):\s*(.+)$", front, re.MULTILINE))
        if matches.get("name") != "elon-musk-communication":
            errors.append("SKILL.md: incorrect name")
        if not matches.get("description") or len(matches["description"]) > 1024:
            errors.append("SKILL.md: description missing or too long")
        if matches.get("license") != "MIT":
            errors.append("SKILL.md: expected MIT license")

    references = re.findall(r"\]\(((?:references|assets)/[^)#]+)\)", raw)
    for relative in references:
        if not (SKILL_DIR / relative).is_file():
            errors.append("Broken skill-local link: " + relative)
    for name in ("Three Sentences", "Bad News"):
        if name.lower() not in raw.lower():
            errors.append("Core concept absent: " + name)

    try:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        if plugin.get("name") != "elon-musk-communication":
            errors.append("Claude plugin name mismatch")
        if "./skills/elon-musk-communication" not in plugin.get("skills", []):
            errors.append("Claude plugin missing canonical skill path")
        if not market.get("plugins") or market["plugins"][0].get("name") != plugin.get("name"):
            errors.append("Marketplace plugin name mismatch")
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append("Invalid plugin metadata: " + str(error))
    return errors


if __name__ == "__main__":
    all_errors = validate()
    if all_errors:
        for issue in all_errors:
            print("FAIL: " + issue, file=sys.stderr)
        sys.exit(1)
    print("PASS: required files, frontmatter, local references and plugin metadata")
