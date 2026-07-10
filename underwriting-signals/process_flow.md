# Process Flow
## Wisaaq Financing Request with Alternative-Signal Layer

**Author:** Muhammad Osama Sohail  **Date:** 2026-07-08  **Status:** Draft, for portfolio purposes

### Numbered steps

1. **Distributor requests Wisaaq financing.** Request enters through the normal Wisaaq intake (via a corporate supplier relationship or distributor-facing Ops).
2. **Identity and basic eligibility check.** Confirm the distributor is a real entity on Haball's rails and meets baseline product criteria.
3. **Bureau/formal-file check.** Look for a conventional credit file.
   - If a usable formal file exists, it proceeds through the standard path (out of scope for this document) and can also be enriched by the signal layer.
   - If no usable file exists (the common case), continue to the alternative-signal layer.
4. **Alternative-signal layer runs (Signal Engine).** Pull the distributor's Blink and Wasal history and compute the three metrics: order consistency, payment timeliness, order-volume trend.
5. **Data-sufficiency check.** Determine whether there are enough observations over the rolling window.
   - If data is sufficient, compute and display metrics.
   - If data is thin or missing, compute what is possible, flag the gaps, and set the illustrative tier to "Thin file, needs manual review."
6. **Credit officer reviews the signal profile.** The officer sees metrics, explanations, source labels, data-gap callouts, and the illustrative tier. This is decision support only.
7. **Human underwriting decision.** The officer applies judgment, combining the signal profile with any other context and policy. The decision is theirs.
8. **Outcome recorded and communicated.** Approve, decline, or request more information. On approval, Wisaaq's existing disbursement process continues (funds disbursed in 5 seconds once approved, per product facts).
9. **Thin-data follow-up loop (optional).** If declined or paused for thin data, distributor-facing Ops can guide the distributor on building history through Blink and Wasal, feeding back into a future request.

### Text-based flow diagram

```
[Distributor requests Wisaaq financing]
                |
                v
[Identity + basic eligibility check]
                |
                v
[Formal credit file check] --yes--> [Standard underwriting path]
                |                            (out of scope, may
                | no                          also use signals)
                v
[Signal Engine: compute 3 metrics from Blink + Wasal]
                |
                v
[Data sufficiency?] --thin--> [Flag gaps + "Thin file, needs manual review"]
                |                          |
             sufficient                    |
                |                          |
                v                          v
[Credit Officer Review Screen: decision support] <-----+
                |
                v
[Human underwriting decision]
                |
     +----------+-----------+
     v          v           v
[Approve]   [Decline]   [Request more info]
     |          |
     v          v
[Wisaaq      [Ops guides distributor to build
 disburses]   history via Blink + Wasal] --> (future request)
```
