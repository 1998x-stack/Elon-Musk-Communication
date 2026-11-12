# Cursor integration

The repository includes a scoped rule at [`.cursor/rules/elon-musk-communication.mdc`](.cursor/rules/elon-musk-communication.mdc). Its `alwaysApply: false` keeps communication-specific guidance from intruding on unrelated coding tasks.

To use it in another Cursor project, copy the rule and the **full canonical Skill directory** into the target project, or use:

```bash
python3 scripts/install.py --agent cursor --scope project --project /path/to/project
```

This project does not claim that Cursor reads Claude plugin metadata. See [INSTALL.md](INSTALL.md) for each agent's install paths. When updating the workflow, edit the canonical Skill, sync mirrors and keep this rule consistent.
