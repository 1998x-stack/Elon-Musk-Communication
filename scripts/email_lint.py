#!/usr/bin/env python3
"""Basic STRUCTURAL checks for an email draft; not a truth or safety oracle."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def lint_email(raw: str, mode: str = "routine") -> list[str]:
    errors = []
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    if not lines or not lines[0].lower().startswith("subject:"):
        return ["First nonempty line must be Subject: ..."]
    subject = lines[0].split(":", 1)[1].strip()
    if not subject:
        errors.append("Subject must identify the issue or decision")
    body = lines[1:]
    if not body:
        errors.append("Missing email body")
        return errors

    # Validate the default three LINE pattern, not arbitrary prose sentence splitting:
    # a decimal number, an acronym, or abbreviations should not change the count.
    if mode == "routine" and len(body) != 3:
        errors.append(f"Expected 3 nonempty body lines in routine mode; got {len(body)}")
    if mode == "incident":
        if not re.search(r"\b(urgent|incident|sev[0-9]|critical|risk)\b", subject, re.I):
            errors.append("Incident subject needs an explicit urgency or incident signal")
    for index, line in enumerate(body, start=1):
        if len(line) > 500:
            errors.append(f"Body line {index} > 500 characters; consider splitting")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Plain UTF-8 email draft with a Subject line")
    parser.add_argument("--mode", choices=("routine", "incident"), default="routine")
    args = parser.parse_args(argv)
    try:
        draft = args.file.read_text(encoding="utf-8")
    except OSError as error:
        parser.error(str(error))
    errors = lint_email(draft, mode=args.mode)
    for issue in errors:
        print("FAIL: " + issue, file=sys.stderr)
    if errors:
        return 1
    print("PASS: structural checks only; human fact/safety review remains mandatory")
    return 0


if __name__ == "__main__":
    sys.exit(main())
