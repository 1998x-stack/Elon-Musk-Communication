---
name: elon-musk-communication
description: Write, rewrite, and review concise executive emails, decision requests, project updates, and urgent bad-news escalations using an evidence-aware three-sentence framework. Use when a user asks for CEO communication, stakeholder reporting, escalation, or short action-oriented messages.
license: MIT
---

# Executive Communication: Three Sentences + Fast Bad News

Turn messy updates into **fast, honest, decision-ready communication**. This is an independently maintained, Musk-inspired workflow, **not an official Tesla, SpaceX, X, or Elon Musk policy**.

**Priority:** truth and safety > speed of escalation > actionability > brevity. Three sentences are a *default*, never a reason to suppress material facts or delay a warning.

## When to use

Use for drafting/revising: executive or manager emails, status updates, production blockers, incident notifications, project delays, approval requests, and cross-functional handoffs. Respond in the user's language unless asked otherwise.

Do not invoke for ordinary casual chat or silently rewrite every message. Do not send anything without explicit authorization.

## Workflow

1. **Classify** the message: `routine`, `decision`, or `urgent/bad-news`. Urgent overrides all other categories.
2. **Extract verified facts**: what happened, current impact, time, owner, evidence, what has already been done, next checkpoint. Distinguish confirmed facts from hypotheses. Never invent metrics, approval amounts, root causes, or deadlines.
3. **Select a structure**:
   - **Routine / decision:** (1) Problem or result + impact; (2) proposed solution with key trade-off; (3) next step, named owner/time, or exact approval requested.
   - **Technical diagnosis:** (1) Problem + impact; (2) confirmed root cause *or* explicitly unconfirmed working hypothesis; (3) fix, owner, and next update.
   - **Bad news:** (1) confirmed event and impact; (2) containment already underway and the accountable owner; (3) next update time and any immediate help needed. **Send the initial alert without waiting for a complete root cause or polished three sentences.**
4. **Write the subject as a decision signal**: e.g. `[Decision by Friday] Capacity plan — $40k`, `[SEV1] API errors — containment in progress`, `[Update] Launch: 2-day slip`. Tags are conventions, not factual severity labels: only use a real `SEV` level if supplied.
5. **Draft plainly**: direct language, short sentences, understandable units, specific recommendation and ask. Put background or evidence in a linked appendix if needed.
6. **Verify** using the checklist below. If one critical input is unknown, use `[confirm amount]` or ask one focused question; never fill it with fabricated specificity.

## Mandatory rules

- **Bad news travels fast.** Do not delay a safety, security, privacy, legal, or major operational escalation while refining style. Follow the organization's incident channels and mandated reporting procedures in parallel; email alone might not be sufficient.
- **Facts before narratives.** Label uncertainty: `confirmed`, `suspected`, `investigating`. Do not state a root cause as proven without evidence.
- **Solutions, not theater.** Recommend an action the sender can responsibly perform; do not invent approval or imply work is already completed.
- **Shortest responsible path.** Route to the person able to act, while respecting access controls, required notifications, and legal or safety policies. Do not unnecessarily bypass regulated escalation paths.
- **Make the ask executable.** Specify one decision, owner, deadline and consequence of delay when known.
- **No jargon or padding.** Explain essential acronyms once; remove ceremonial intros and irrelevant history.
- **Privacy and consent.** Minimize personal/customer identifiers and confidential data; present a *draft*, not a claim that an email was sent.
- **Three sentences are a tool, not a law.** Preserve any required safety steps, uncertainty, legal notice or incident details even if the body needs additional sentences.

## Output contract

Normally return:
```text
Subject: <specific signal>

<sentence 1: problem / evidence / impact>
<sentence 2: root cause or proposal / containment>
<sentence 3: next action + owner/time or exact ask>
```

For urgent incidents, put the alert first. Separate a longer factual incident log if needed; never wait for the full log before providing the short alert. For rewrite/review requests, produce a usable revision first, then at most 2–3 concise notes on missing facts.

## Quality gate

- [ ] Is the core fact unambiguous and evidence-grounded?
- [ ] Is the business/customer/safety impact stated if known?
- [ ] Is a recommendation or mitigation included, without pretending it already happened?
- [ ] Is the ask, owner and/or next update explicit?
- [ ] Is uncertainty distinguished from confirmed facts?
- [ ] Would waiting to improve brevity cause harm or delay an urgent escalation?
- [ ] Are sensitive details handled through approved channels?
- [ ] Can the recipient decide or act in about 30 seconds?

## Read only the relevant reference

- [Principles and decision flow](references/principles.md)
- [Incident/bad-news escalation](references/bad-news-playbook.md)
- [Scenario patterns and anti-patterns](references/scenarios.md)
- [Evidence and attribution](references/evidence-and-attribution.md)
- [Ready-to-use templates](assets/templates/README.md)

**Attribution:** former Tesla executive Jon McNeill described experiments with three-sentence emails, with slightly different variants across interviews. The precise templates, safety rules, scorecard, and output contract here are the maintainers' adaptations; do not present them as verbatim Musk instructions.
