# Markdown Output Template

The deliverable is a single Markdown document with the structure below. Do not deviate from this skeleton — downstream pptx skills depend on the slide-by-slide convention, and the assumption disclosure table is the single biggest credibility lever.

## Required document skeleton

````markdown
# [Company Name] — Investor Pitch Draft

> **Variant**: investor (external)
> **Stage**: [Pre-seed / Seed / Series A+]
> **Audience**: [Specific firm / type]
> **Story Structure**: [Problem-Solution-Market / Why Now / Category Creation / Founder Story]
> **Duration**: [X minutes, ~Y slides]
> **Language**: [Chinese / English / bilingual] — [literal / localized] mode
> **Product Type Classification**: [therapeutic / diagnostic / research-tool SaaS / SaMD / service / data platform] → biotech subflow depth: [full / light / N/A]

---

## Mandatory Assumption Disclosure Table (Block 0)

| Step 1 question | Value | Status |
|----------------|-------|--------|
| 1. Purpose | [user-provided value] | given |
| 2. Audience | [value] | given |
| 3. Stage | [value] | given |
| 4. Duration | [value] | given |
| 5. Language | [value] | given |
| 6. Existing version | [yes / no] | given |
| 7. Domain disambiguation | [if any ambiguous term, the resolved domain] | given |
| 8. Product type | [classification] | given |
| Founder background | [value or —] | [given / 🔴 needs-data] |
| Existing traction | [value or —] | [given / 🔴 needs-data] |

> Items not provided by the user appear as 🔴 needs-data. Items derived from assumptions appear as [assumption — basis].

---

## Slide 1 — Title
- Company name: [name]
- One-line positioning (10 words or fewer): [tagline]
- Logo placeholder

## Slide 2 — [first-narrative-slide-per-structure]
- [content with verified / assumption / needs-data labels on every quantitative claim]

## Slide 3 — [next slide]
...

## Slide N — Competitor Analysis (mandatory)

### Complete competitor list
[Existing direct + indirect + potential entrants + status quo, table form]

### Big-incumbent capability assessment
[Table: big player / assets / distance / resources / signs of intent / entry barrier]

### Defensibility narrative
[1–2 paragraphs answering "what protects this for 36 months", written for the investor audience — based on the moat-check verdict but not showing the raw weighted score]

## Slide M — IP / Regulatory / Reimbursement (mandatory if biotech)

[Per product-type classification, full / light / N/A treatment]

## Slide [last-1] — Ask
- Round size: [amount]
- Use of funds: [breakdown]
- Milestones to next round: [3–5 items, each with timing]
- Timeline: [target close date]

## Slide [last] — Why Us, Why Now (closing)
[Tie back to the lead narrative]

---

## Data Citation Table

| Slide | Data point | Source | Status |
|-------|-----------|--------|--------|
| 2 | [claim] | [source name + year, or —] | [verified / assumption / needs-data] |
| 4 | [claim] | [source] | [verified] |
| ... | ... | ... | ... |

---

## Anti-pattern Self-check Results

- [x] No "we have no competitors" statement — status quo included
- [x] TAM uses bottom-up SOM logic, no "global market × small percentage" math
- [x] Why Now present and verified
- [x] Team slide has specific contributions per person — not just pedigree
- [ ] Retention curve included — 🔴 needs-data, will add when CRM data available
- [x] Big-incumbent assessment included
- [x] 36-month moat check completed — weighted score [X.X], verdict [strength / disclose-and-mitigate / reconsider product]
- [x] Biotech subflow handled per product type — [full / light / N/A]

---

## Notes for the user

[Any specific concerns about the deck — usually relating to the moat-check verdict, items needing data, or assumptions that need verification before the pitch]
````

## Key rules for the template

- **Block 0 (Assumption Disclosure) is non-negotiable**. If you skip it, future readers cannot tell what was confirmed vs. assumed, and the deck loses traceability.
- **Every quantitative claim has a label**. No exceptions. If you cannot label something, mark it `🔴 [needs-data]` rather than letting it slide.
- **Slide N (Competitor Analysis) and Slide M (Biotech subflow if applicable) are mandatory regardless of story structure**. The position varies; the inclusion does not.
- **The Anti-pattern Self-check Results section at the bottom is for the user, not for investors.** It documents that you ran the check. The user can remove it before circulating to investors, but it should be present in the working draft.

## Notes on language

If the document is bilingual, structure as:
- Top: shared metadata block + Mandatory Assumption Disclosure Table (single language, the primary one)
- Then: a horizontal rule, then the same content in the second language
- Or: side-by-side Markdown tables for the slide content

Default mode is "localized" — re-tune phrasing for the target audience. Switch to "literal translation" only if the user wants identical structure across languages (rare; usually requested for compliance or translation-firm handoff reasons).
