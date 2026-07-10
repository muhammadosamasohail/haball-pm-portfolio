# Open Questions and Stakeholder Owners
## Alternative-Signal Underwriting Inputs for Wisaaq

**Author:** Muhammad Osama Sohail  **Date:** 2026-07-08  **Status:** Draft, for portfolio purposes

These are questions I could not answer from outside Haball. They would need cross-functional validation before this went anywhere.

| Question | Why it matters | Proposed Owner / Function |
|----------|----------------|----------------------------|
| Do Blink and Wasal actually capture and expose the fields the metrics need, and at what granularity? | The whole approach depends on this data existing in a usable form. If it does not, the initiative stops. | Engineering / Data |
| Do the proposed signals fit Wisaaq's Shariah governance and distributor consent requirements? | Wisaaq is Islamic finance; a framing that conflicts with Shariah or consent rules is a non-starter. | Compliance / Legal |
| Which signals do credit officers actually find useful, and what thresholds do they trust? | The output is for them; guessing definitions without them risks building the wrong thing. | Credit / Risk |
| What minimum observation count and window length make a metric trustworthy versus noise? | Thin data shown as confident is worse than showing nothing; this sets the data-sufficiency rules. | Credit / Risk with Data |
| How should thin-file distributors be handled and communicated so eligibility feels fair? | Poor handling creates friction and fairness concerns at the distributor relationship. | Distributor-facing Ops with Product |
| Where does this sit against other Wisaaq priorities, and is it worth sequencing now? | Even if feasible, it competes for roadmap space; someone has to own that call. | Product Leadership |
