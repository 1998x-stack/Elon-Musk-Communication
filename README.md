# Elon Musk Communication

**Three-Sentence Emails · Bad News Travels Fast · Action-Oriented Executive Updates**

[简体中文](README.zh.md) · [Skill](skills/elon-musk-communication/SKILL.md) · [Examples](EXAMPLES.md) · [Sources](skills/elon-musk-communication/references/evidence-and-attribution.md)

> Write so a decision-maker can understand **what happened, what to do, and what you need** in one pass.  
> Unofficial, evidence-aware communication workflow inspired by accounts of Elon Musk's executive practices.

## Why this exists

Most executive emails are too long, delay inconvenient news, blur facts with guesses, or conceal the required decision. This repository provides a reusable Agent Skill for **clear, accountable, fast communication**—not a collection of inspirational quotes.

| Principle | What it fixes | Default behavior |
|---|---|---|
| **Three-Sentence Emails** | Background-heavy, decision-free updates | Problem → recommended solution → next step/ask |
| **Bad News Travels Fast** | Late disclosure and false reassurance | Alert on verified facts; disclose what is unknown |
| **Shortest Responsible Path** | Relaying information through unnecessary layers | Speak to an action owner while honoring incident/compliance paths |
| **Facts Over Theater** | Unsupported confidence and invented metrics | Preserve verified numbers; label uncertainty |

**Important nuance:** Jon McNeill has described both **problem → root cause → solution** and **problem → solution → next step** variants. This Skill chooses the version that makes the recipient's next action clearest. **Urgency, accuracy, and safety override the three-sentence target.**

## Install in 30 seconds

### Option A: Claude Code plugin

Run these commands **inside Claude Code**:

```text
/plugin marketplace add 1998x-stack/Elon-Musk-Communication
/plugin install elon-musk-communication@elon-musk-communication
```

The plugin manifest exposes the canonical skill at `skills/elon-musk-communication/`.

### Option B: install a standalone Agent Skill

```bash
git clone https://github.com/1998x-stack/Elon-Musk-Communication.git
cd Elon-Musk-Communication
python3 scripts/install.py --agent codex --scope project --project /path/to/your/project
```

Replace `codex` with `claude`, `pi`, or `opencode`. For a personal installation, choose `--scope user`. Cursor can use the committed [rule](.cursor/rules/elon-musk-communication.mdc); the installer also supports `--agent cursor`. See [INSTALL.md](INSTALL.md) for exact behavior.

### Option C: one prompt for your agent

```text
Install the open-source executive communication skill from
https://github.com/1998x-stack/Elon-Musk-Communication .
Inspect the canonical skills/elon-musk-communication/SKILL.md and its referenced files.
Install a self-contained copy in the current agent's supported skill directory;
do not overwrite an existing skill without asking.
Then use it to rewrite my next executive update, preserve all verified facts,
and urgently surface material bad news instead of waiting for a perfect 3-sentence email.
```

## 20-second example

**Before:** "We have been coordinating across the team and encountered some challenges which we hope to address soon."

**After** (all figures hypothetical):

```text
Subject: [Decision today] Release 2 days late

The release is two days late because two payment tests remain blocked.
I recommend delaying launch until Thursday and putting one engineer on the integration today.
Please approve the revised public launch date by 16:00 so we can notify customers.
```

For incidents, **alert immediately**, include known impact, mitigation and next update, and follow required paging/security procedures. Never wait to invent a root cause merely to complete the template.

## Architecture

```text
skills/elon-musk-communication/
  SKILL.md                          # canonical source
  references/                       # rules, evidence, escalation, scenarios
  assets/templates/                 # ready-to-fill email patterns
.claude-plugin/                       # Claude plugin + marketplace manifests
.cursor/rules/                       # on-demand Cursor rule
.codex/skills/ .pi/skills/ .opencode/skills/
                                    # portable mirrors (validated for parity)
scripts/                              # installation and quality checks
tests/                                # stdlib-only automated regression tests
.github/workflows/                    # CI
CLAUDE.md / AGENTS.md / CURSOR.md     # platform guidance
EXAMPLES.md / INSTALL.md              # user-focused guides
```

## How to use

Ask your assistant: **"Rewrite this as a three-sentence CEO decision email; do not invent facts; if it is bad news, make the alert immediate and explicit."** For urgent messages, ask for an alert and a separate timeline; do not force safety-critical information into exactly three sentences.

## Validate locally

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
python3 scripts/email_lint.py examples/sample-decision.txt
```

No third-party Python dependencies are required.

## Provenance and limits

This work is **independent and not affiliated with or endorsed by Elon Musk, Tesla, SpaceX, or X**. McNeill's interviews describe experiences and experiments, not an enforceable company-wide policy. The skill's urgency exceptions, privacy standards, checks, and templates are **maintainer-authored**. Read the [source and attribution notes](skills/elon-musk-communication/references/evidence-and-attribution.md) before presenting a claim as a direct quote.

## Contribute

Help improve real-world examples, verify sources, fix cross-agent installation issues, or suggest clearer escalation scenarios. Follow [AGENTS.md](AGENTS.md), update mirrored SKILL.md copies when editing the canonical file, and run the quality checks before opening a PR.

## License

[MIT](LICENSE)
