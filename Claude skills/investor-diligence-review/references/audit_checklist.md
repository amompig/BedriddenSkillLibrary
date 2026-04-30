# Audit Checklist — investor-diligence-review

Used by **two consumers**:
1. The skill itself, as a self-gate before delivering the IC memo (Step 7's "verification scan before delivery").
2. `output-supervisor`, as the canonical rule source when chain-triggered.

Severity grouping: **CRITICAL** (any one failing → overall FAIL) vs **WARN**.

---

## CRITICAL（缺一個就 FAIL）

### Memo structure (11 sections)

- [ ] **Top-of-memo metadata header present** with: company / date / stage / round size / domain / team size / input mode / web search status / conviction / **recommendation**
- [ ] **§1 Executive Summary + Recommendation** — 200–300w, with conviction level, three strengths, three risks, conditions to advance (if Continue/Term)
- [ ] **§2 Investment Thesis Fit** present (200–400w)
- [ ] **§3 Team Assessment** present, with explicit team-size bracket applied (per `team_size_scaling.md`)
- [ ] **§4 Market Analysis** present, **independently computed** (does NOT just copy pitch's TAM)
- [ ] **§5 Product / Technology Critique** present
- [ ] **§6 Competitive Landscape — all four layers populated** with required minimum counts (with **OFFLINE-mode exception**: a layer that consists entirely of `[needs-research]` entries with explicit OFFLINE banner at memo top counts as PASS — the layer is acknowledged but un-executable without web search; conviction must be Medium-or-lower as a consequence):
  - Layer 1 (Large incumbents): ≥3
  - Layer 2 (Mid-size / specialist): ≥5
  - Layer 3 (Early-stage / stealth <$5M): ≥5
  - Layer 4 (Latest research / OSS): ≥3
- [ ] **§7 Traction & Unit Economics** present, compared against industry benchmarks (per `domain_subflow.md`)
- [ ] **§8 Risk Matrix** present, all 5 categories covered (technical / market / team / regulatory / financial)
- [ ] **§9 Open Diligence Questions** present
- [ ] **§10 Term Sheet & Valuation** — required for Continue diligence / Term sheet (skippable for Pass)
- [ ] **§11 Final Recommendation + Conditions** present

### Research execution (8-item checklist)

- [ ] All 8 items in `research_checklist.md` executed (or marked OFFLINE for degraded mode)
- [ ] Each item delivered minimum required count (Item 1: ≥5 funding rounds; Item 2: ≥2 exits + ≥2 failures; Items 3, 4: ≥5; Item 5: ≥3; etc.) — **OFFLINE-mode exception**: items consisting entirely of `[OFFLINE — RECALL ONLY]` or `[needs-research]` entries count as PASS provided OFFLINE banner present at memo top
- [ ] If any item under-delivered, this is **noted in memo header** as "incomplete diligence — Item N partial; conviction reduced"
- [ ] **Step 4 extension searches**: ≤5 used (not exceeded); audit trail in appendix if any used

### Verification + tagging (4 hard rules)

- [ ] **Hard Rule 1** — no fabricated company-+-amount-+-valuation-+-headcount combinations. Every such tuple is `[verified — source]` or `[training-recall — VERIFY]` (entire tuple, not mixed)
- [ ] **Hard Rule 2** — no fabricated founder backgrounds. Every named founder claim is verified, training-recall tagged, or `[needs-research]`
- [ ] **Hard Rule 3** — §10 valuation has explicit methodology + comparable transactions table OR scoring rubric (when §10 is present)
- [ ] **Hard Rule 4** — every numeric claim (%, $, headcount, dates, multiples) carries one of three tags

### v2 mode specific (when input was a directory)

- [ ] **Data Room Read Trail appendix** present, listing each file's classification + read level + key extractions
- [ ] **Cross-document discrepancies surfaced** in §1 / §7 / §8 if any found
- [ ] **Central artifact actually read** (Priority-1 file deep-read confirmed)

### Persona discipline

- [ ] **No "Notes for the founder" section** (breaks persona)
- [ ] **Recommendation is one of**: Pass / Continue diligence / Term sheet (no other variants)
- [ ] **Conviction level** explicitly stated (High / Medium / Low)

---

## WARN

### Memo quality

- [ ] **Length within target** for the stage (per `stage_calibration.md`)
- [ ] **Hard cap respected** (≤7,500 words)
- [ ] **Domain overlay applied** consistently (per `domain_subflow.md`)
- [ ] **Stage weighting** roughly matches table (e.g., for Series A, §7 is heavier than §3)

### §6 Competitive completeness

- [ ] **Net competitive verdict** stated at end of §6 (who wins in 36 months)
- [ ] **Each layer has source attribution** (where these competitors / papers were found)

### §7 Traction quality

- [ ] **NRR + logo retention** both demanded if SaaS-domain (NRR alone hides churn)
- [ ] **Concentration** flagged if top-1 or top-3 ARR > 25%

### §8 Risk quality

- [ ] **Each risk has severity (High / Med / Low)**
- [ ] **Each risk has mitigation status** (mitigated / monitored / unmitigated)
- [ ] **Risks are specific**, not generic ("execution risk" without specificity is a WARN)

### §10 Valuation quality (when present)

- [ ] **Range given** (not single point)
- [ ] **Adjustment reasoning shown** (why above/below median)
- [ ] **Comparable count** matches recommendation level (Continue: ≥3; Term sheet: ≥5)

### Tone / formatting

- [ ] **Voice is p