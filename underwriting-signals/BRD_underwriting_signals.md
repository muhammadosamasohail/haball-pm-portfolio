# Business Requirements Document
## Alternative-Signal Underwriting Inputs for Wisaaq

### Document Control

| Field | Detail |
|-------|--------|
| Title | Alternative-Signal Underwriting Inputs for Wisaaq |
| Author | Muhammad Osama Sohail |
| Date | 2026-07-08 |
| Version | 1.0 |
| Status | Draft, for portfolio purposes |
| Document type | Business Requirements Document (BRD) |
| Related documents | SRS, User Stories, Process Flow, Wireframe Spec, Market Research Summary, Backlog Snippet, Stakeholder Notes |

### 1. Business Context and Problem

Wisaaq is Haball's Islamic supply chain financing product, using Tijarah and Murabaha structures to fund distributors buying from corporate suppliers. To extend financing, someone has to answer a basic question: is this distributor likely to repay? In most markets that question is answered, at least in part, by a credit bureau file. In Pakistan, for the distributors Wisaaq is built to serve, that file usually does not exist.

The numbers behind this are structural, not incidental:

- Roughly 90% of Pakistani retailers and distributors have zero formal digital transaction history (source: desk research).
- Pakistan's informal economy is roughly 40% of GDP and 72% of employment (source: desk research).
- Traditional lenders leave about 94% of SMEs without formal credit access. Only around 200,000 of an estimated 3.2 million SMEs have any formal bank credit relationship (source: desk research).

The implication is direct. For a large share of the distributors Wisaaq wants to reach, a conventional credit-scoring approach is not just weak, it is structurally impossible, because the underlying data was never generated. This document treats that gap as the core business problem: Wisaaq's addressable pool is constrained by the absence of a formal credit file, not by the absence of creditworthy distributors.

The starting hypothesis this document explores is that Haball's own ecosystem already produces alternative signals once a distributor is on its rails. Blink, Haball's corporate payment gateway connecting 26+ banks, generates order-frequency and payment-timeliness events as distributors pay and get paid through their networks. Wasal, Haball's digital invoicing and FBR tax-registration product, generates invoice history once a distributor digitizes. In other words, Blink and Wasal may be the data-generation engine that makes Wisaaq underwritable for distributors who have no bureau file. That is a hypothesis to validate with Haball's risk team, not a claim about how Haball currently operates.

### 2. Business Objectives

1. Expand the addressable pool of distributors Wisaaq can consider for financing without requiring a formal credit file, by defining alternative signal inputs drawn from within Haball's ecosystem.
2. Give credit and risk officers a clearer, explainable starting view of a thin-file distributor, so that manual underwriting effort is directed where it adds the most judgment rather than spent assembling basic behavioral facts.
3. Articulate how Blink and Wasal activity connects to Wisaaq eligibility, so that product and commercial teams can reason about the ecosystem as one flywheel rather than three separate products.

### 3. Stakeholders

| Role / Function | Interest in this initiative |
|-----------------|------------------------------|
| Product | Owns whether and how an alternative-signal layer enters the Wisaaq roadmap; cares about sequencing against other priorities. |
| Credit / Risk | Primary consumer of any signal output; cares that inputs are explainable, that they support rather than replace human judgment, and that they do not introduce hidden model risk. |
| Compliance / Legal | Cares about Shariah-compliance framing (Wisaaq is Islamic finance), data-use consent, and fair-treatment concerns in how distributor data feeds decisions. |
| Engineering / Data | Owns whether the required fields actually exist and are retrievable from Blink and Wasal, and at what cost; the realistic gatekeeper on feasibility. |
| Distributor-facing Ops | Interacts with distributors day to day; cares about how eligibility is communicated and how thin-file distributors are handled without friction. |

### 4. Scope

**In scope**
- Defining a small set of alternative signal inputs derived from distributor behavior already visible within Haball's ecosystem (order consistency, payment timeliness, order-volume trend).
- Specifying how those inputs would be presented to a credit officer as decision support.
- Documenting the requirements, process flow, and screen content for such a capability.

**Out of scope**
- Building or training a credit-scoring model of any kind.
- Producing an accuracy figure, a default-probability estimate, or an automated approve/deny decision.
- Integrating with real Haball systems or accessing real distributor data.
- Redesigning Wisaaq's underlying financing structures or Shariah governance.

### 5. Business Rules and Constraints

- The capability must support human underwriting, not replace it. The output is an input to a credit officer, not a decision.
- Signal inputs must be explainable in plain language. No black-box scoring; a credit officer should be able to see why a metric reads the way it does.
- The framing must respect Shariah compliance, since Wisaaq is Islamic finance. Signals describe trading and payment behavior; they do not introduce interest-based logic or anything that would conflict with the product's structure. This would need validation with Compliance.
- The capability must degrade gracefully on thin or missing data. Absence of signal must be shown as absence, not silently treated as a negative or positive score.
- Distributor data use must respect consent and privacy expectations, subject to Legal review.

### 6. Supporting Evidence: The Digitization Tipping Point

A fair objection to the whole premise is that many distributors stay cash-based on purpose, to limit tax exposure, which means they never generate the digital signals described above. That tension is real. The point of this table is narrower: to show why the signal data is likely to exist over time, because external pressure is moving distributors toward digitization regardless.

FBR's mandatory e-invoicing rollout (effective Nov 2025) changes the arithmetic of staying informal.

| Factor | Staying informal (cash-based) | Digitizing (Wasal + Blink on Haball rails) |
|--------|-------------------------------|---------------------------------------------|
| Upfront cost | Low or none directly, but rising exposure | Roughly PKR 100,000 to 500,000 setup cost (source: desk research) |
| FBR non-compliance risk | Penalties up to 2% of transaction value under the e-invoicing mandate (source: desk research) | Compliant by construction via Wasal's instant FBR registration |
| Access to financing | Effectively none; no file, no eligibility | Generates the invoice, order, and payment history that could make Wisaaq underwriting tractable |
| Trajectory | Increasing friction as the mandate tightens | One-time cost, then eligibility and compliance both improve |

The takeaway is hedged: the mandate does not instantly digitize the smallest merchants, and the upfront cost genuinely pushes some further away in the short term. But the direction of travel is toward more distributors generating exactly the signal data this initiative depends on. That makes the alternative-signal approach worth scoping now rather than treating the data as permanently absent.

### 7. Assumptions

- Blink and Wasal capture, or could capture, the behavioral events described (order events, payment timing, invoice records) in a retrievable form. This is assumed, not confirmed.
- A meaningful and growing subset of Wisaaq-relevant distributors will have enough Blink and Wasal history to compute the signals over a rolling window.
- Haball's credit officers would find behavioral signal inputs useful as decision support for thin-file cases. This should be validated through interviews.
- Nothing here conflicts with Wisaaq's Shariah governance, pending Compliance confirmation.

### 8. Success Criteria (business-level)

- A credit officer can look at a thin-file distributor and see a structured behavioral profile they could not previously assemble quickly.
- The share of distributor applications that can be moved past the initial "no file, cannot assess" wall increases, subject to risk-team acceptance.
- Product, Risk, and Compliance can point to one shared artifact describing how Blink and Wasal activity relates to Wisaaq eligibility.
- No increase in decisions made without human review, since the capability is explicitly decision-support only.

### 9. What This Document Is Not

This is not a proposal for what Haball should build. Haball's team has almost certainly considered underwriting for thin-file distributors in more depth than an outside applicant can, with data, regulatory, and risk constraints not visible from the outside. This document is a work sample: it shows how I take a real, researched problem in Haball's space, the credit-scoring void facing Wisaaq, and turn it into structured requirements thinking. Where it states things about Haball's internal systems, those are stated as assumptions to be validated, not as facts I claim to know.
