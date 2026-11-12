# Elon Musk Communication｜高管沟通 Agent Skill

**三句话邮件 · 坏消息立即上报 · 让管理沟通直接推动决策**

[English](README.md) · [核心 SKILL](skills/elon-musk-communication/SKILL.md) · [案例](EXAMPLES.md) · [来源与归属](skills/elon-musk-communication/references/evidence-and-attribution.md)

> 用最短的沟通路径传递准确事实、可行建议和明确的下一步动作。

这是一个**非官方、独立维护**的 Skill：参考前特斯拉高管 Jon McNeill 的公开回忆及马斯克相关公开报道，把高管邮件沟通原则转化为可复用、可测试的 AI Agent 工作流；不代表特斯拉官方政策。

## 两项核心原则

| 原则 | 目标 | Agent 输出 |
|---|---|---|
| **Three-Sentence Emails** | 减少流水账，迅速获得决策 | 问题/结果 → 建议/原因 → 下一步/请求 |
| **Bad News Travels Fast** | 坏消息不积压、不粉饰 | 已确认事实 → 当前止损 → 负责人/下次更新时间 |

补充规则：不编造数据；区分事实、推测和未知；尽可能直接找到能够解决问题的人；涉及安全、隐私、法律或重大故障时，以正式应急机制优先，**不能因为追求三句话而延迟上报**。

**出处细节：** McNeill 在不同访谈中提到过「问题 → 根因分析 → 建议方案」和「问题 → 解决方案 → 下一步」两种表达。本项目按实际沟通目的使用不同变体，不把模板说成马斯克逐字规定。

## 安装

**Claude Code 插件（在 Claude Code 内执行）**

```text
/plugin marketplace add 1998x-stack/Elon-Musk-Communication
/plugin install elon-musk-communication@elon-musk-communication
```

**Codex / Pi / OpenCode**

```bash
git clone https://github.com/1998x-stack/Elon-Musk-Communication.git
cd Elon-Musk-Communication
python3 scripts/install.py --agent codex --scope project --project /path/to/your/project
```

替换 `--agent` 可适配 `claude`、`pi`、`opencode`、`cursor`；个人安装使用 `--scope user`。详细路径见 [INSTALL.md](INSTALL.md)。

**复制下面这段 Prompt 给你的 Agent：**

```text
从 https://github.com/1998x-stack/Elon-Musk-Communication
读取 skills/elon-musk-communication/SKILL.md 与相关 references，
按当前 Agent 的目录规范安装为独立 Skill；已有同名 Skill 不要直接覆盖。
以后我要求写 CEO、高管邮件、项目延期、风险汇报或坏消息升级时，
优先输出事实准确、行动明确的三句话邮件；重大紧急事件立刻提示升级，
不得杜撰数据、根因、决策授权或已经完成的行动。
```

## 前后对比

**原文：**「最近我们多方协同，项目进度有点挑战，但大家都在积极推进。」

**改写（示例数据均为虚构）：**

```text
Subject: [Decision today] Release 2 days late

The release is two days late because two payment tests remain blocked.
I recommend delaying launch until Thursday and putting one engineer on the integration today.
Please approve the revised public launch date by 16:00 so we can notify customers.
```

## 仓库结构

- `skills/elon-musk-communication/SKILL.md`：唯一规范来源，含完整触发条件、流程和质量门禁。
- `skills/elon-musk-communication/references/`：原则、坏消息处理、场景、证据与来源。
- `skills/elon-musk-communication/assets/templates/`：三句话邮件、决策请求、紧急通报。
- `.claude-plugin/`、`.cursor/rules/`：Claude 和 Cursor 的可安装配置。
- `.codex/skills/`、`.pi/skills/`、`.opencode/skills/`：其他 Agent 的 Skill 镜像。
- `scripts/`、`tests/`：安装、静态检查和邮件规范测试。

## 质量校验

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
python3 scripts/email_lint.py examples/sample-decision.txt
```

Python 标准库即可运行，无第三方依赖。开发时须同步全部 Skill 镜像并保证测试通过。

## 声明

本仓库并非马斯克本人创作或认可，也不隶属于 Tesla / SpaceX / X。所有检查清单和具体实施模板均属项目作者整理。详细信息见 [证据与来源](skills/elon-musk-communication/references/evidence-and-attribution.md)。

MIT License。
