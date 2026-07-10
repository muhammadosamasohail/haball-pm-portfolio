# Wireframe Content Specification
## Alternative-Signal Underwriting Inputs for Wisaaq

**Author:** Muhammad Osama Sohail  **Date:** 2026-07-08  **Status:** Draft, for portfolio purposes

This is a content spec, not the wireframe. It defines exact sections, fields, and labels so an HTML wireframe can be built directly from it. Two screens are specified.

### Screen 1: Distributor Signal Profile (internal credit-officer review)

**Purpose:** Give a credit officer a structured behavioral view of a thin-file distributor as decision support.

**Layout, top to bottom:**

1. **Header bar**
   - Left: "Distributor Signal Profile"
   - Below title, distributor name (example: "Karachi Traders Pvt Ltd") and Distributor ID (example: "DST-04821")
   - Right: illustrative tier badge (see item 4)
   - Small text under header: "Decision-support view. Not an automated decision."

2. **Context strip (one row, three small fields)**
   - Data window: "Last 12 months"
   - Observations: "e.g. 34 order events, 31 payment events"
   - Sources active: "Blink, Wasal" (or "Blink only")

3. **Three signal metric cards (side by side on desktop, stacked on mobile)**
   - **Card A: Order Consistency**
     - Value: illustrative, for example "Steady (CV 0.18)"
     - Plain-language line: "How regular this distributor's orders are. Lower variation means steadier ordering."
     - Source tag: "From Blink"
     - Micro-note: "Based on 34 orders over 12 months."
   - **Card B: Payment Timeliness**
     - Value: illustrative, for example "88% on time"
     - Plain-language line: "Share of payments made on or before the due date."
     - Source tag: "From Blink"
     - Micro-note: "Based on 31 payments."
   - **Card C: Order-Volume Trend**
     - Value: illustrative, for example "Rising (+6% / quarter)"
     - Plain-language line: "Direction of order volume over the window. Rising, flat, or declining."
     - Source tag: "From Blink, corroborated by Wasal invoices"
     - Micro-note: "Slope over last 12 months."

4. **Illustrative tier badge (in header, defined here)**
   - Possible states: "Sufficient signal, standard review" / "Partial signal, closer review" / "Thin file, needs manual review"
   - Must carry a small label: "Illustrative only. Not a rating or a decision."

5. **Data-gap callout box (full width, only when relevant)**
   - Heading: "Data gaps"
   - Body example: "No Wasal invoice history found. Payment timeliness based on 6 payments only, below the recommended minimum. Treat metrics as low-confidence."
   - Visual treatment: distinct box, neutral warning styling, not red-alarm.

6. **Footer note (persistent)**
   - Text: "This screen presents behavioral signals to support a credit officer's judgment. It does not underwrite, score, or approve. Figures shown are illustrative."

### Screen 2: Signal Sources (reference screen)

**Purpose:** Show which Haball product each signal would come from. Simpler than Screen 1.

**Layout:**

1. **Header:** "Signal Sources" with subtitle "Where each signal input would come from within Haball's ecosystem (illustrative)."

2. **Source-mapping table**

   | Signal | Source product | What it draws on |
   |--------|----------------|------------------|
   | Order consistency | Blink | Order timestamps and values |
   | Payment timeliness | Blink | Payment due vs. settled dates |
   | Order-volume trend | Blink (+ Wasal) | Order volume over time, corroborated by invoices |
   | Digitization confirmed | Wasal | Invoice records and FBR registration status |

3. **Flywheel note (short block below table):** "Blink and Wasal generate the behavioral data. The Signal Engine reads it. Wisaaq's credit officer uses it. The more a distributor transacts and invoices on Haball's rails, the more underwritable they become."

4. **Footer note:** "Illustrative mapping for a work sample. Not a description of Haball's live data pipeline."
