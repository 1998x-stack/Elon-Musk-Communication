# Principles and decision flow

## Executive communication is a decision interface

The best short message answers **what happened, why it matters, what happens next**. Brevity is a constraint that forces prioritization—not evidence that the issue is simple.

| Situation | First | Second | Third |
|---|---|---|---|
| Decision | Need + cost of delay | Recommendation + trade-off | Explicit decision + deadline |
| Status | Actual vs target | Gap, reason if known | Owner + next milestone |
| Operational problem | Verified symptom + impact | Most likely fix + evidence | Action, owner, checkpoint |
| Incident / bad news | Verified event + scope | Current containment | Who owns next update, when; specific help |

A *diagnostic* variant is also useful: problem → root cause (only when verified) → proposed solution. This is distinct from the *execution* variant: problem → solution → next step. Neither is universally mandated.

## Six rules

1. **Make facts falsifiable.** Prefer "checkout error rate rose from 0.3% to 4.1% during 09:00–09:20 UTC" over "payments are broken"; never fabricate a baseline.
2. **Put the recommendation in the message.** The recipient should not have to reverse-engineer the desired decision.
3. **Treat risk disclosure as time-critical.** Initial notifications may state "root cause under investigation."
4. **Route directly, with accountability.** Contact the action owner and appropriate incident/compliance recipients; avoid performative reply-all.
5. **Use cost, consequence, and time.** If material and known, mention budget, customer impact, lost capacity, and the decision cutoff.
6. **Optimize clarity, not punctuation.** Three overlong run-on sentences are worse than four clear ones.

## Decision algorithm

```text
Has a time-critical safety, security, legal, or operational risk been identified?
  YES -> Alert now using verified facts + containment + next update.
         Use mandated paging/escalation channels too. Follow up as evidence changes.
  NO  -> Does the recipient need to decide something?
           YES -> Problem + recommendation + specific ask/deadline.
           NO  -> Result/deviation + action + next checkpoint.
```

## Self-review rubric (0 / 1 / 2 for each)

- **Accuracy:** ungrounded or misleading / partial / grounded and appropriately qualified.
- **Impact:** absent / qualitative / specific and contextualized.
- **Action:** none / vague / owner-action or actionable recommendation.
- **Ask/next checkpoint:** absent / implicit / explicit.
- **Readability:** confusing / workable / scan-ready.

Aim for 8–10/10 *without sacrificing the urgency and safety gate*. This rubric is a project-maintained heuristic, not a Musk quote.
