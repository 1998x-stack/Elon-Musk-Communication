# Examples

All names, amounts, metrics and dates in this file are **fictional teaching examples**.

## 1. Routine update

```text
Subject: [Update] QA throughput — 18% under target

QA throughput is 18% below the weekly target after a test-environment slowdown.
I recommend temporarily moving two test runners to the isolated pool while the team profiles the bottleneck.
Ari will report measured throughput at 17:00 UTC tomorrow.
```

## 2. Approval request

```text
Subject: [Approve by Wed] $25k to restore build capacity

The build queue is taking 80 minutes instead of 25, delaying daily releases.
An additional $25k of monthly compute would restore the target capacity based on yesterday's load test.
Please approve the spend by Wednesday so Priya can provision it this week.
```

## 3. Bad news—do not wait

```text
Subject: [Urgent] Customer export link accessible — disabled

We confirmed one export link could be accessed beyond its intended group from 08:20 to 08:42 UTC; affected data is still being assessed.
The link is disabled and the incident commander has engaged the Security and Privacy teams.
The next factual update is due at 09:15 UTC, and required notifications are being evaluated.
```

A real incident also requires its organization's paging, security, privacy, and legal response processes.

## 4. Unknown root cause

```text
Subject: [Investigating] API p95 latency up to 460 ms

API p95 latency rose from 180 ms to 460 ms after today's deploy.
We suspect an index change but have not confirmed the cause, and the rollback test is in progress.
The on-call engineer will update the incident channel at 11:30 UTC.
```

**Anti-pattern:** Replace `We suspect` with `We confirmed` without evidence. That turns a useful message into misinformation.

More: [scenario catalog](skills/elon-musk-communication/references/scenarios.md).
