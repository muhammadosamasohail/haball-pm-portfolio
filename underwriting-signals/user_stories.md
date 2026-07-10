# User Stories
## Alternative-Signal Underwriting Inputs for Wisaaq

**Author:** Muhammad Osama Sohail  **Date:** 2026-07-08  **Status:** Draft, for portfolio purposes

Format: As a [role], I want [capability], so that [benefit]. Roles covered: Credit/Risk Officer (primary consumer), Product Manager (owns backlog), Distributor (indirect beneficiary).

---

**US1. Credit/Risk Officer, thin-file profile at a glance**
As a credit officer, I want to see a distributor's behavioral signal profile on one screen, so that I can start assessing a thin-file applicant who has no bureau record.

Acceptance criteria:
- The screen shows order consistency, payment timeliness, and order-volume trend for the distributor.
- Each metric shows the data window and number of observations it is based on.
- Each metric has a one-line plain-language explanation.
- The screen states that it is decision support, not an automated decision.

---

**US2. Credit/Risk Officer, know when data is too thin**
As a credit officer, I want the system to flag when a distributor's data is too thin to compute a metric, so that I do not mistake missing data for a good or bad signal.

Acceptance criteria:
- A metric with insufficient observations is shown as "insufficient data," not as a number.
- A visible data-gap callout summarizes what is missing.
- The illustrative tier label reflects thin data (for example, "Thin file, needs manual review").

---

**US3. Credit/Risk Officer, trace a metric to its source**
As a credit officer, I want to see which Haball product each signal comes from, so that I can judge how much to trust it and follow up if needed.

Acceptance criteria:
- Each metric is labeled with its source product (Blink or Wasal).
- The screen distinguishes payment-based signals (Blink) from invoice-based signals (Wasal).
- Hovering or expanding a metric reveals its plain definition and inputs.

---

**US4. Product Manager, prioritize with a clear capability definition**
As a product manager, I want a documented definition of the alternative-signal capability and its dependencies, so that I can place it in the Wisaaq backlog and sequence it against other work.

Acceptance criteria:
- The capability is broken into epics and stories with rough sizing.
- Dependencies on Blink and Wasal data availability are listed as explicit items.
- At least one investigation (spike) exists to de-risk assumptions before build.

---

**US5. Product Manager, validate before committing**
As a product manager, I want open questions routed to the right function before build, so that we do not commit engineering effort on unvalidated assumptions.

Acceptance criteria:
- Open questions are captured with a proposed owning function.
- Risk, Compliance, and Engineering each have at least one question assigned.
- No build-type story is marked ready until its blocking question is resolved.

---

**US6. Distributor, fair consideration despite no credit file**
As a distributor with no formal credit history, I want my actual trading and payment behavior on Haball's rails to count toward financing eligibility, so that I am not excluded simply because I have no bureau file.

Acceptance criteria:
- Eligibility consideration can proceed using behavioral signals when no bureau file exists.
- Absence of a bureau file alone does not end the assessment.
- The distributor is not a direct user of the internal tool; this benefit is delivered indirectly through the credit officer's review.

---

**US7. Distributor, understand the path to eligibility**
As a distributor, I want to understand that digitizing through Wasal and transacting through Blink builds the history that supports Wisaaq eligibility, so that I can make an informed choice about going digital.

Acceptance criteria:
- Distributor-facing Ops has clear messaging linking Blink/Wasal activity to future eligibility.
- The message is framed as building history over time, not an instant guarantee.
- Messaging avoids implying any automated approval.
