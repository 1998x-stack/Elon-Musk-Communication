# Fast bad-news escalation playbook

**Rule: send the first credible signal as soon as it is actionable; don't wait for root-cause certainty.**

## 1. Identify the trigger

Examples: material customer harm, outage, cybersecurity exposure, regulatory deadline, budget blowout, schedule slip that changes a launch commitment, serious safety risk.

Not every concern is an emergency. Calibrate channel and urgency to measured impact and organizational policy.

## 2. Send an initial alert

- Confirmed event + when first observed + bounded impact.
- Containment in progress / completed; owner named when known.
- Next update **at a promised time** or next check-in trigger; immediate decision needed, if any.
- What remains unknown, explicitly.

If an immediate response is necessary, page or call through the official incident process; an email by itself is insufficient in many environments.

## 3. Update reliably

Maintain a clear distinction between:
- **Confirmed:** seen in logs or verified by an accountable source.
- **Suspected:** plausible and currently under investigation.
- **Unknown:** no reliable answer yet.

If no new information is available at the promised time, send a short "still investigating" update with a revised next-update time rather than silently missing the checkpoint.

## 4. Close with evidence

State recovery measurement, verification method, remaining risks and post-incident owner. Keep the detailed timeline in an incident document; the first email need not contain the entire postmortem.

## Examples

### Good initial alert (synthetic)

Subject: [Urgent] Checkout failures — mitigation underway

Checkout failures reached 8% at 14:10 UTC; the customer-impact estimate is still being verified.
On-call engineering has started rolling back the latest release, and I am coordinating the incident.
Next update is at 14:25 UTC; please approve temporary traffic throttling if rollback does not recover the error rate.

### Bad initial alert

"We may have a small problem but it is probably nothing; I'll send a report tomorrow."  
**Why it fails:** hides uncertainty behind reassurance, lacks impact, ownership and update commitment.

## Safety boundaries

Never bypass regulatory notification, emergency services, mandatory information-security handling, privacy controls or internal incident-command protocols. The "three sentences" idea never supersedes those obligations.
