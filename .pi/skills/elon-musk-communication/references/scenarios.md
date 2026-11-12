# Scenarios and transformations

All numbers, people, and projects below are **fictional examples**. Do not reuse them as facts.

## A. A delayed launch

**Before:** "The team worked really hard this sprint and we ran into a few unforeseen challenges, but are committed to quality."

**After**

Subject: [Decision by Thu] Launch delay — 2 days

The release is two days behind schedule because two payment integration tests still fail.
I recommend moving launch to Thursday and assigning one engineer to isolate the failing integration today.
Please confirm the revised customer announcement deadline by 16:00.

**Why:** states deviation, recommends action, names the decision.

## B. Budget approval

Subject: [Approve $40k by Fri] Additional test capacity

Current test throughput is 18% below the level needed for the planned release.
Adding short-term cloud capacity for $40k is expected to close most of the gap, subject to load testing.
Please approve the spend by Friday so the team can provision capacity on Monday.

## C. Suspected root cause

Subject: [Investigating] API latency regression

API p95 latency increased from 180 ms to 460 ms after the 11:00 UTC deploy.
A database index change is one hypothesis, but we have not confirmed causality and are testing a rollback.
Maya owns the investigation and will update the incident channel at 11:30 UTC.

**Why:** doesn't promote a hypothesis to a proven root cause.

## D. Cross-functional handoff

Subject: [Action needed] Billing release blocked on schema review

The billing release cannot proceed because the schema change still lacks a security review.
I recommend a 15-minute direct review between billing and security today rather than another management relay.
Could the security on-call owner confirm a reviewer by 15:00?

## E. Early bad news

Subject: [Urgent] Customer exports exposed — access disabled

We confirmed that an internal export link was reachable outside its intended group from 08:20 to 08:42 UTC; affected records are under investigation.
Access has been disabled, and Security and Privacy are coordinating containment through the incident process.
The incident commander will provide a verified scope update at 09:15 UTC and assess required notifications.

**Why:** prompt disclosure, verified/unknown separation, and appropriate mandated escalation.

## Anti-patterns

| Anti-pattern | Replace with |
|---|---|
| "Everything is on track" with no metric | Actual vs target and date |
| All history, no ask | Decision-specific subject + bottom-line request |
| Unknown root cause presented as fact | "Cause under investigation" |
| "Just FYI" for critical incident | Urgent alert + incident channel + next update |
| Unjustified precise dates | Explicitly provisional checkpoint |
| "We will fix" without owner | Owner + first action + follow-up |
| Three massive sentences | Short sentences with clearly delimited facts |

## Rewrite self-check

Did the version preserve the original facts? Was any number, authority or root cause invented? Is it safe to send now, or is the situation urgent enough to require paging instead?
