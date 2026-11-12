# Installation & agent compatibility

The canonical source is `skills/elon-musk-communication/` and **must be installed as a complete directory** including `references/` and `assets/`. A lone copied `SKILL.md` has broken local reference links.

## Option 1: Claude Code plugin

Inside Claude Code:

```text
/plugin marketplace add 1998x-stack/Elon-Musk-Communication
/plugin install elon-musk-communication@elon-musk-communication
```

The registry files live in `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`. Confirm the plugin is listed before assuming activation; Claude Code must support plugin marketplaces.

## Option 2: portable skill copy

```bash
git clone https://github.com/1998x-stack/Elon-Musk-Communication.git
cd Elon-Musk-Communication
python3 scripts/install.py --agent codex --scope project --project ~/work/my-project
python3 scripts/install.py --agent pi --scope user
python3 scripts/install.py --agent cursor --scope project --project ~/work/my-project
```

Use `--dry-run` to inspect all intended paths, and `--force` **only** when intentionally replacing an existing installation. By default the installer refuses to overwrite files.

| Agent | Project install | User install |
|---|---|---|
| Claude Code | `.claude/skills/elon-musk-communication/` | `~/.claude/skills/elon-musk-communication/` |
| Codex | `.agents/skills/elon-musk-communication/` | `~/.agents/skills/elon-musk-communication/` |
| Pi | `.pi/skills/elon-musk-communication/` | `~/.pi/agent/skills/elon-musk-communication/` |
| OpenCode | `.opencode/skills/elon-musk-communication/` | `~/.config/opencode/skills/elon-musk-communication/` |
| Cursor | `.cursor/skills/elon-musk-communication/` plus project rule | `~/.cursor/skills/elon-musk-communication/` |

Codex's **current recommended** project location is `.agents/skills/`. A `.codex/skills/` mirror is also committed for workflows that explicitly load that legacy/custom path; it is **not** assumed to be auto-discovered by Codex. Cursor also receives a scoped `.cursor/rules/` rule for project installation.

**Discovery varies with agent versions and trust settings.** Verify the skill appears in your agent's own skills list after installation.

## For contributors

```bash
python3 scripts/sync_mirrors.py
python3 scripts/sync_mirrors.py --check
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

The sync script keeps full copies of the canonical directory in `.agents/`, `.codex/`, `.pi/`, and `.opencode/`. Avoid editing these copies directly.
