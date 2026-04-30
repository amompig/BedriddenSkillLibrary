# Valuation Methodology

§10 of the IC memo (Term Sheet & Valuation Reasoning) is the most hallucination-prone section. Specific deal terms invented from thin air mislead partners worse than no number at all.

This file defines:
1. Which methodologies to use at which stage
2. The required structure for each
3. The verification rules for comparables (per Hard Rule 3 + verification_rules.md)
4. When §10 can be skipped (Pass recommendation only)

---

## When §10 is required vs. optional

| Recommendation | §10 required? | Notes |
|----------------|----------------|-------|
| Pass | **Optional** | Skip is allowed if pass reasoning is unrelated to valuation. If the pass reasoning IS valuation-related ("over-priced for stage"), include a brief §10 to explain. |
| Continue diligence | **Required** | Sketch valuation range with 1 methodology + 3+ comparables. |
| Term sheet | **Required, full** | Full valuation work: 2 methodologies, 5+ comparables, term-sheet term-by-term. |

---

## Methodology by stage

| Stage | Recommended methodology | Secondary (cross-check) |
|-------|--------------------------|--------------------------|
| Pre-seed | **Berkus** or **scorecard** | Comparable pre-seed market (e.g., recent SAFE caps in same category) |
| Seed | **Comparable transactions** (recent seed rounds) | Scorecard |
| Series A | **Comparable transactions** + **revenue multiple** | DCF-lite if traction is strong |
| Series B+ | **Revenue multiple** + **DCF-lite** | Comparable transactions |

---

## Methodology 1: Comparable transactions

**The most used method for SaaS / AI / general SaaS.**

### Required output

A table of 3–5 (or 5–8 for Term sheet recommendation) recent comparable rounds:

```markdown
| Company | Round | Date | Valuation (post-money) | ARR / Key metric | Source |
|---------|-------|------|------------------------|------------------|--------|
| Snowflake | Series F | 2020-02 | $12.4B | $96M ARR (LTM) | [verified — Snowflake S-1, 2020] |
| Acme.ai | Series A | 2024-Q3 | ~$80M | ~$3M ARR (claimed) | [training-recall — VERIFY] |
| ... |
```

### Selection criteria for comparables

- **Same stage** (or one stage adjacent — must note)
- **Same domain** (or close adjacency — must note distance)
- **Within last 18 months** for stage relevance (24 months max for early stages)
- **Disclosed valuation** — if only round size is public, derive valuation only with stated assumptions

### Verification

- Each comparable must be `[verified]` with source URL OR `[training-recall — VERIFY]`
- **Cannot mix tags within a row** (per Hard Rule 1)
- If 3+ comparables come back `[training-recall]`, the memo must flag this as "valuation work requires fresh comparable diligence before term sheet"

### Range derivation

- Take the 3–5 comparables
- Calculate median + range (e.g., 25th–75th percentile)
- Apply this company's adjustments: above/below median based on traction quality, team strength, market timing
- State the adjustment reasoning explicitly

**Example output**:
```
Median Series A SaaS valuation in this category (last 18mo): $35M post-money
Range: $20M – $60M
Adjustment: +20% for above-median NRR (130% vs. ~110% median)
Proposed range: $25M – $72M post-money, with central estimate $40M – $50M
```

---

## Methodology 2: Revenue multiple

**Standard for SaaS Series A+.**

### Calculation

```
Valuation = ARR × multiple

Where multiple depends on:
- Growth rate (200%+ commands premium)
- NRR (130%+ commands premium)
- Gross margin (75%+ infra / 80%+ app commands premium)
- Stage (Series A typically 10–25x for high-growth)
```

### Stage benchmark multiples (rough, last 18 months)

| Stage | Growth profile | ARR multiple |
|-------|----------------|--------------|
| Series A | High growth (200%+) | 15–25x |
| Series A | Moderate (100–200%) | 8–15x |
| Series B | High growth | 10–18x |
| Series B | Moderate | 5–10x |

These multiples shift with macro cycle. If the memo cites a multiple, the source year matters:

```
At Series A high-growth, ARR multiples are typically 15-25x [training-recall — VERIFY; multiples have been compressed since 2022 peak; recheck against Bessemer Cloud Index Q4 2025]
```

---

## Methodology 3: Berkus method (pre-seed only)

For pre-revenue startups. Values 5 categories at $0 – $0.5M each:

| Category | Value range | Logic |
|----------|-------------|-------|
| Sound idea | $0 – $0.5M | Defensible product hypothesis |
| Prototype / MVP | $0 – $0.5M | Reduces tech risk |
| Quality of management team | $0 – $0.5M | Reduces execution risk |
| Strategic relationships | $0 – $0.5M | Reduces market risk |
| Production / sales | $0 – $0.5M | Reduces commercialization risk |

Total: $0 – $2.5M pre-money valuation

### When to use

- Pre-revenue, pre-seed
- US market most relevant (Berkus less applied internationally)
- When comparable transactions are hard to find at this scale

### Adjustments

- Multiply by 1.5x – 3x for hot categories
- Multiply by 0.5x – 0.8x for cold / saturated categories

---

## Methodology 4: Scorecard method (pre-seed / seed)

Compares to "average" pre-seed valuation in the geography, then adjusts:

| Factor | Weight | This company adj |
|--------|--------|-------------------|
| Strength of management | 30% | +15% |
| Size of opportunity | 25% | +0% |
| Product / technology | 15% | +10% |
| Competitive environment | 10% | -5% |
| Marketing / sales / partnerships | 10% | +0% |
| Need for additional investment | 5% | -5% |
| Other | 5% | +0% |

Sum the adjustments and apply to baseline (e.g., baseline $3M pre-money × 1.15 = $3.45M).

### When to use

- Pre-seed / early seed where Berkus feels too rigid
- Domains with clear "average" valuation benchmarks

### Verification

- The "baseline" must come from a `[verified]` source (e.g., AngelList annual report, Pitchbook quarterly summary, regional VC association data)
- Adjustments are the partner's `[assumption]` — clearly tag as such

---

## Methodology 5: DCF-lite (Series A+ with revenue trajectory)

For companies with measurable revenue and clear scaling path. Not a full DCF — a 5-year projection with:

- Revenue: ARR × growth × NRR
- Costs: GM × revenue + fixed cost trajectory
- Terminal value: revenue multiple × year-5 ARR

### Required disclosures

- Discount rate used (typical: 25–35% for Series A; 20–25% for Series B)
- Growth assumptions year-by-year
- Margin assumptions year-by-year
- Terminal multiple assumption with comparable basis

### Verification

- Discount rate: `[assumption — basis: stage-typical VC required IRR]`
- Growth assumptions: `[assumption — basis: pitch's claim ± skepticism adjustment]`
- Terminal multiple: `[verified]` from comparable transactions OR `[training-recall — VERIFY]`

DCF-lite is most useful as a **sanity check** alongside revenue multiple — if DCF-lite gives 50% of comp multiple valuation, dig into why.

---

## Term sheet sketch (when recommendation = Term sheet)

If recommending term sheet, include a term-by-term sketch:

| Term | Proposed | Rationale |
|------|----------|-----------|
| Round size | $X | Founder's ask (or counter-proposal) |
| Pre-money | $X | From valuation methodology above |
| Post-money | Pre + round | — |
| Liquidation preference | 1x non-participating | Standard for clean Series A |
| Anti-dilution | Broad-based weighted average | Standard |
| Board composition | 2 founders + 2 investors + 1 independent | Standard at Series A |
| Pro-rata rights | Yes, for round investors | Standard |
| Option pool top-up | Pre-money to X% | Sized for next 18 months hiring |
| Vesting | 4y / 1y cliff for new hires; refresh for founders if needed | — |
| Drag-along | Standard | — |
| Information rights | Quarterly financials + cap table | — |

Each term: state proposal + 1-line rationale. Don't pad. Don't over-engineer.

---

## What to NEVER do in §10

1. Cite a specific deal valuation without a tag (Hard Rule 1)
2. Quote a "rule of thumb" multiple without context (multiples shift; year matters)
3. Give a single-point valuation without a range
4. Skip methodology disclosure ("we propose $X" with no work shown)
5. Mix `[verified]` and `[training-recall]` claims within the same calculation step
6. Include term-sheet detail when recommendation is Pass

---

## Output format check

Before considering §10 complete, verify:

- [ ] Methodology chosen and stated
- [ ] Comparables table (if used) has source per row
- [ ] Range given (not a single point)
- [ ] Adjustment reasoning shown
- [ ] All comparable valuations / multiples carry `[verified]` or `[training-recall — VERIFY]` tag
- [ ] Range matches conviction level (High conviction = tight range; Low = wide range)
- [ ] Term sheet section appears only if recommendation = Term sheet
