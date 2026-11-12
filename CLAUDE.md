# CLAUDE.md

This repository maintains an **unofficial executive-communication Agent Skill**, not a directive from Elon Musk or any company.

## Scope

When a user asks to draft, edit, or review executive communications, use [the canonical skill](skills/elon-musk-communication/SKILL.md). Read the relevant reference only as needed. Outside that scope, do not force all text into three sentences.

## Four operating principles

1. **Accurate before concise:** preserve provided facts, label uncertainty, don't fabricate figures, root causes, approvals, or completed work.
2. **Bad news travels fast:** report material risks promptly; safety/legal/security escalation mechanisms override email aesthetics.
3. **Make decisions easy:** problem or result, recommendation or mitigation, next action or exact ask.
4. **Shortest responsible path:** contact action owners directly while respecting confidentiality and mandatory incident channels.

## Contribution instructions

Keep `skills/elon-musk-communication/SKILL.md` the canonical Skill source. Keep mirror copies under `.codex/skills/`, `.pi/skills/`, and `.opencode/skills/` byte-identical. Run:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

Do not misattribute maintainer-authored content as a verified Elon Musk quote. See [evidence notes](skills/elon-musk-communication/references/evidence-and-attribution.md).
