# Software Requirements Specification
## Alternative-Signal Underwriting Inputs for Wisaaq

**Author:** Muhammad Osama Sohail  **Date:** 2026-07-08  **Version:** 1.0  **Status:** Draft, for portfolio purposes

### 1. Purpose and Scope

This SRS describes the requirements for a decision-support capability, referred to here as the Signal Engine, that computes plain, rules-based behavioral metrics for a distributor and presents them to a Haball credit officer reviewing a Wisaaq financing request. It is lighter and more technical than the accompanying BRD.

The Signal Engine does not underwrite. It computes arithmetic metrics from a distributor's transaction history and displays them, with explanations, for human review. There is no model, no score that decides anything, and no automated outcome.

### 2. System Context

The Signal Engine sits between Haball's existing data-generating products and a credit officer's review screen. Conceptually:

```
[Distributor activity]
        |
        v
[Blink: payment + order events]   [Wasal: invoice + FBR records]
        \                               /
         \                             /
          v                           v
             [Signal Engine: rules-based metrics]
                          |
                          v
        [Credit Officer Review Screen: decision support]
                          |
                          v
             [Human underwriting decision]
```

Blink and Wasal are treated as upstream data sources. The Signal Engine is a read-only consumer of behavioral data. The credit officer is the sole decision-maker downstream. This layout is illustrative; it describes how such a capability could sit alongside Blink and Wasal, not how Haball is wired today.

### 3. Functional Requirements

- **FR1.** The system shall compute an order-consistency metric from a distributor's order history over a rolling window, using the coefficient of variation of order values or intervals (lower variation indicates steadier ordering).
- **FR2.** The system shall compute a payment-timeliness rate, defined as the share of payments made on or before their due date over the same window.
- **FR3.** The system shall compute an order-volume trend, expressed as the slope of order volume over the window (rising, flat, or declining).
- **FR4.** The system shall display each metric with a plain-language explanation of what it measures and how to read it.
- **FR5.** The system shall indicate the data window and the number of observations each metric is based on.
- **FR6.** The system shall detect and clearly flag thin or missing data, and shall not compute a metric it cannot support with sufficient observations.
- **FR7.** The system shall present an illustrative, non-binding tier label (for example, "Thin file, needs manual review") that summarizes data sufficiency, explicitly marked as illustrative and not a decision.
- **FR8.** The system shall show, per metric, which source product (Blink or Wasal) the underlying data would come from.
- **FR9.** The system shall present all output as decision support and shall not render an approve or deny outcome.

### 4. Non-Functional Requirements

- **NFR1. Explainability and auditability.** Every displayed metric must be traceable to its inputs and computation. No opaque scoring. An officer should be able to reconstruct why a number reads the way it does.
- **NFR2. Data privacy.** Distributor data must be handled under consent and least-access principles, subject to Legal review. Only fields needed for the displayed metrics should be used.
- **NFR3. Shariah-compliance handling.** Metric definitions must stay descriptive of trading and payment behavior and must not introduce interest-based logic, pending Compliance confirmation given Wisaaq's Islamic-finance basis.
- **NFR4. Performance.** Not a concern at this scale. There is no real-time requirement; batch or on-demand computation at review time is acceptable.
- **NFR5. Simplicity.** Computation must remain rules-based arithmetic that a non-technical reviewer can understand.

### 5. Data Requirements

The following fields are hypothetical and illustrative. They describe what would be needed, not what is confirmed to exist in Haball's systems.

| Field | Likely source | Purpose |
|-------|---------------|---------|
| Order timestamp | Blink | Order intervals for consistency and trend |
| Order value | Blink | Value variation and volume trend |
| Payment due date | Blink / Wasal | Basis for timeliness |
| Payment settled date | Blink | Timeliness calculation |
| Invoice record + FBR status | Wasal | Confirms digitization; corroborates order history |
| Distributor ID | Blink / Wasal | Ties events to one distributor |
| Observation count / window | Derived | Data-sufficiency flags |

### 6. Out of Scope

- No trained machine-learning model.
- No automated approve or deny decision.
- No default-probability or accuracy figure.
- No integration with real Haball systems or real distributor data.
- No changes to Wisaaq's financing structures.

### 7. Assumptions and Dependencies

- Depends on Blink and Wasal exposing the listed fields in a retrievable form; unconfirmed.
- Assumes enough distributors have sufficient history to compute metrics over a rolling window.
- Depends on Credit/Risk agreeing which metrics are meaningful and on Compliance confirming the Shariah and data-use framing.
- Assumes definitions of "on time," window length, and minimum observation counts would be set with the risk team, not fixed here.
