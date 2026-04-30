# Data Verification Protocol — Internal Variant

Same three-layer protocol as the external skill, but with a strong emphasis: **internal decks should rely almost entirely on Layer 1 (the company's own internal data)**. The user's CRM, financials, HR system, product analytics, and lab data are the source of truth for internal updates.

## The three layers

### Layer 1 — Internal data (dominant for internal)

For internal decks, every KPI, financial metric, headcount number, burn figure, and product metric should come from the company's own systems. If the user reports something that does not have a clear system source ("our retention is around 95%"), prompt them: "What is the source — Stripe / Mixpanel / internal dashboard? Let's anchor it to the system."

Accept these formats: CSV, XLSX, PDF, screenshots from internal dashboards, pasted text. If the user prefers, ask them to paste the relevant section directly.

Label internal-sourced figures as `[verified — internal, <system + date>]`. Examples:
- `[verified — Stripe MRR, 2026-04-15]`
- `[verified — Mixpanel cohort, Q1 2026]`
- `[verified — internal financials, March 2026 close]`

### Layer 2 — Re-prompt for what is missing

If the user reports a metric without a system source, do not let it pass. Ask: "I would like to anchor this to the underlying system before writing it into the deck. Which dashboard / report is this from?" If the user pushes back ("I just remember it was about 95%"), label it `[assumption — founder recall, 2026-04-XX]` so future readers know the provenance.

### Layer 3 — Public sources (rare for internal)

For internal decks, public-source data appears mainly in two contexts:
1. **Strategy off-sites or annual planning** — discussing market context, competitive landscape, regulatory shifts
2. **Board updates** — the competitor moat re-check, where market events from public sources are integrated

For these, use the same source hierarchy as the external skill: investment banks, regulators, public company filings, industry research firms, academic literature.

## The three labels

### `[verified — source]`

Real, citable source. For internal, this should usually resolve to "internal CRM, internal HRIS, internal financials, internal product analytics, internal lab notebook, internal experimental data."

### `[assumption — basis]`

A reasoned estimate with explicit derivation. For internal, this is rare — most internal data should resolve to a system. If a number is an assumption, the basis must be specific.

### `[needs-data]`

A number that should exist in a system but is not yet supplied. Use 🔴. If a board update has more than 2-3 `🔴 [needs-data]` items, the user should pause and gather the data before the meeting — not after.

## Forbidden output

- **Founder-recall numbers presented as KPIs**. "Our retention is about 95%" without a Mixpanel / Amplitude / internal dashboard source must be labeled `[assumption — founder recall]`, not stated as fact.
- **KPIs without timestamps**. "ARR: $250K" with no date is not useful for an internal update — the audience needs to know whether this is end-of-Q1, current, or projected.
- **Aggregated data without segments visible**. "We have 50 customers" is fine for a quick mention, but a board update on a customer-concentration topic should show the distribution.

## Special note: vs-Plan reconciliation

Internal updates frequently include "vs Plan" comparisons (e.g., KPI table with Plan / Actual / Δ columns). Both Plan and Actual must be `[verified]`:
- **Plan** must come from a documented prior plan (last quarter's board materials, the operating plan, the hiring plan). If the plan is not documented, the founder should pause and document it before continuing.
- **Actual** must come from the relevant system.

If Plan is not available because this is the first update, mark Plan as 🔴 `[needs-data — first update, no prior plan available]` and propose that the next update have explicit Q-on-Q comparison.

## Examples

**Good (internal):**
- "Q1 paid pilots: 0 / Plan: 1 / Δ: -100% [verified — internal CRM, 2026-04-15]"
- "Burn rate March: $95K [verified — financials close 2026-03-31]"
- "Net retention 110% 🔴 [needs-data — billing system snapshot pending Q1 close]"

**Bad (internal):**
- "Pretty solid retention this quarter" — qualitative, no number, no source
- "ARR around $300K" — no system source, no timestamp
- "Burn was over plan" — no number, no actual amount
