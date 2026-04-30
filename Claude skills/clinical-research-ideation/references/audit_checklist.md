# Audit Checklist — clinical-research-ideation

Used by **two consumers**:
1. The skill itself, as a final self-gate before delivery.
2. `output-supervisor`, as the canonical rule source when chain-triggered.

Severity grouping: **CRITICAL** (any one failing → overall FAIL) vs **WARN**.

---

## CRITICAL（缺一個就 FAIL）

### Mandatory candidate fields (Step 3)

Every candidate must have all of:

- [ ] Title
- [ ] Rationale
- [ ] Technical approach
- [ ] Data sources
- [ ] Primary endpoint
- [ ] Novelty (with explicit regional scope)
- [ ] Single point of failure (SPOF) + mitigation
- [ ] Other risks
- [ ] Timeline
- [ ] Funding fit (primary + backup, see below)

Missing any field → candidate is not deliverable.

### Scoring matrix (Step 1)

- [ ] **Part E contains a 7-criteria scoring matrix** with each candidate scored 1–5 on:
  1. Clinical unmet need
  2. Technical novelty
  3. Data feasibility
  4. Outcome measurability
  5. Regulatory path
  6. Competitive landscape
  7. Funding fit
- [ ] **No score of 5 without explicit justification** (5 means best-in-class, not "good")

### Funding fit (Step 2)

- [ ] **Each candidate names a primary funding target + one viable backup** (e.g., NSTC AI Major / NHRI 整合型 / MOHW 緊急醫療政策 / NIH R21 / EU Horizon)
- [ ] **No vague "applicable to multiple grants"** — must be specific mechanism names

### Top-3 down-select (Step 4)

- [ ] **Top 3 candidates identified** by score sum
- [ ] **One-line "why this beats the others"** per top-3 entry
- [ ] **Tie-break logic disclosed** if scores tied (lower data-feasibility risk first; then named SPOF mitigation > unmitigated)

### Anti-saturation + hygiene

- [ ] **No saturated topics** (BUSI re-classification, EchoNet re-implementation) without clear differentiator
- [ ] **AUROC vs clinical utility** never conflated — separated explicitly
- [ ] **Regional scope precise** — never claims global novelty for TW-only novel topic, or vice versa
- [ ] **Data realism** — does not propose data the user cannot realistically obtain (multi-center raw RF without IRB; real-time inter-hospital streaming without governance)
- [ ] **Timeline realism** — proposals involving claims linkage allow ≥6–9 months HWDC + IRB lead time

---

## WARN

### Divergent ideation (only if Round 2 broad-ideation mode)

- [ ] Covers ≥3 pain-point types
- [ ] Covers ≥2 modalities
- [ ] Includes at least one low-tech, one high-tech, AND one policy-leverage candidate

### Stylistic

- [ ] Candidate cards (Part D) are uniformly structured (same field order across cards)
- [ ] Rationale section ties to a pain point that biomedical-lit-search results justified
- [ ] Notes section flags any candidate where SPOF mitigation is weak even if listed
