# AGENTS.md

## Project mission

Build a portable, fact-grounded Agent Skill that turns executive communication into action. The repository is independent and does not claim Elon Musk's endorsement.

## Authoring source of truth

- Edit `skills/elon-musk-communication/SKILL.md` first.
- After changes, run `python3 scripts/sync_mirrors.py` to update mirrors.
- References contain details; keep `SKILL.md` compact enough for skill discovery and execution.
- Treat `references/evidence-and-attribution.md` as the attribution register.
- Templates are illustrative placeholders. Every numeric example must be explicitly fictional.
- No third-party runtime dependencies unless justified.

## Behavioral invariants

1. Never invent facts, metrics, dates, root causes, approvals, or actions already taken.
2. Escalate material bad news using required channels immediately; avoid delay for a perfect three-sentence draft.
3. Distinguish known facts, hypotheses, and unknowns.
4. Apply brevity as a default, not a hard restriction in emergencies.
5. Respect privacy, legal notification, and incident response policies.
6. No unauthorized email transmission or impersonation.
7. When necessary, surface one critical missing piece of information.

## Repository validation

```bash
python3 scripts/sync_mirrors.py --check
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

## Change policy

Prefer small, focused changes. Tests should cover altered output formats and cross-agent parity. Do not modify factual provenance without verifying the source. Avoid adding promotional claims or unverifiable quotations.
