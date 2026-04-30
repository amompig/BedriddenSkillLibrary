# Data Verification Protocol

Every quantitative claim in the final deck must carry a label. This protocol defines what each label means and the three-layer process for resolving missing data.

## The three layers

### Layer 1 — User's internal data

Ask first. The user's own data (financial reports, product analytics, CRM exports, lab notebooks, clinical trial data) is the strongest source for any company-specific number. Accept these formats: CSV, XLSX, PDF, or pasted text.

If the user provides data, label the resulting figures as `[verified — internal, <date or system>]`.

### Layer 2 — Re-prompt for what is most missing

If the user does not have a dataset ready, do not jump to public sources yet. Re-prompt explicitly: "Without internal data, the deck loses credibility on retention / unit economics / clinical milestones (whichever is most relevant). Can you provide at minimum X, Y, Z?"

The minimums by stage and type:
- **SaaS pre-seed/seed**: MRR or ARR, monthly active users, top-line retention, burn rate
- **SaaS Series A+**: full cohort retention curve, NRR, gross margin, CAC payback
- **Biotech (therapeutic/diagnostic)**: pipeline stage table, recent milestone results, IP filing status
- **Research/design tool SaaS**: design partner count, pilot conversion rate, ARR

Re-prompting is part of the protocol, not an annoyance — it raises the user's awareness of the data they do have but did not think to share.

### Layer 3 — Public sources

If after re-prompting the user still cannot supply data, search public sources. Acceptable sources, in rough credibility order:

- **Investment-bank and consulting reports**: Goldman Sachs, Morgan Stanley, McKinsey, Bain, BCG, Deloitte
- **Government and regulatory bodies**: FDA, SEC, EMA, TFDA, national health ministries, Eurostat, OECD
- **Industry research firms (public summaries)**: IDC, Gartner, Forrester, CB Insights, PitchBook
- **Public company financials**: 10-K filings, S-1 prospectuses, quarterly earnings calls
- **Academic literature**: PubMed, Google Scholar; for biotech, *Nature*, *NEJM*, *Lancet*, *Cell*

Always cite source and year: `[verified — Grand View Research, 2025]`, `[verified — Schrödinger 10-K, FY2024]`.

## The three labels

### `[verified — source]`

Has a real, citable source. The source can be the user's internal data or a public report. The format is `[verified — <source name>, <year if known>]`.

### `[assumption — basis]`

A reasoned estimate with explicit derivation. The basis must be specific: an analogue company's adoption curve, a known industry ratio, a logical inference from a verified upstream number. Format: `[assumption — analogue: Veeva early SaaS penetration, 2008–2012]`.

### `[needs-data]`

A number that should exist but is not yet supplied. Use 🔴 emoji to make it visible. Format: `🔴 [needs-data — should come from CRM]`.

## Forbidden output

- **Unsourced precise numbers.** "TAM is $1,234B" with no citation is forbidden, regardless of how plausible it sounds. If the only source is "AI estimate" or "industry consensus" without naming a report, it is an `[assumption]` and must be labeled as such.
- **Conversion-style precision without source.** "73.4% conversion rate" should not appear unless it is from internal data.
- **Aggregated TAM via "global market × small percentage we'll capture".** This is not a TAM, it is a fantasy. Use bottom-up SOM with explicit adoption-rate logic.

## Examples

**Good:**
- "Cheminformatics software market: ~$5–8B [assumption — multiple research firm estimates; specific report TBD by user]"
- "Eroom's Law: pharma R&D cost doubles ~every 9 years [verified — Scannell et al., *Nat Rev Drug Discov*, 2012]"
- "Q1 design partners: 3 [verified — internal CRM, 2026-04-15]"
- "Net retention 110% 🔴 [needs-data — should come from billing system]"

**Bad:**
- "TAM $4.2B" — no source, precise number
- "Net retention 110%" — no label, no source
- "Industry-leading retention" — qualitative claim disguised as quantitative
