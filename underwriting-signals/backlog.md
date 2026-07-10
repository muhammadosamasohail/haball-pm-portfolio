# Backlog Snippet
## Alternative-Signal Underwriting Inputs for Wisaaq

**Author:** Muhammad Osama Sohail  **Date:** 2026-07-08  **Status:** Draft, for portfolio purposes
**Priority scheme:** MoSCoW (Must / Should / Could / Won't). **Sizing:** S / M / L (rough effort, not story points).

| ID | Title | Type | Priority | Description | Size |
|----|-------|------|----------|-------------|------|
| AS-1 | Alternative-signal decision-support layer for Wisaaq | Epic | Must | Parent epic: define, spec, and prototype behavioral signal inputs for thin-file distributor underwriting. | L |
| AS-2 | Spike: validate data availability for order-consistency signal with Engineering | Spike | Must | Confirm whether Blink exposes order timestamps and values in a retrievable form, and at what granularity. De-risks FR1. | S |
| AS-3 | Spike: confirm Shariah and data-use framing with Compliance | Spike | Must | Check that behavioral-signal definitions and distributor data use fit Wisaaq's Islamic-finance basis and consent rules. | S |
| AS-4 | Compute and display order consistency, timeliness, and trend | Story | Must | Implement the three rules-based metrics and their plain-language explanations (FR1 to FR5). | M |
| AS-5 | Thin/missing-data handling and gap callouts | Story | Must | Detect insufficient observations, suppress unsupported metrics, show data-gap callout and illustrative tier (FR6, FR7). | M |
| AS-6 | Distributor Signal Profile review screen | Story | Should | Build the credit-officer screen per the wireframe spec, decision-support framing throughout (FR4, FR8, FR9). | M |
| AS-7 | Signal Sources reference screen | Story | Could | Build the simpler Blink/Wasal source-mapping screen. | S |
| AS-8 | Distributor-facing eligibility messaging | Story | Could | Ops-facing copy linking Blink/Wasal activity to building Wisaaq eligibility over time. | S |
