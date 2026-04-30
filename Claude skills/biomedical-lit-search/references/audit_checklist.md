# Audit Checklist — biomedical-lit-search

Used by **two consumers**:
1. The skill itself, as a final self-gate before delivery (mirrors what's described under "What to deliver" + "Negative constraints" in SKILL.md).
2. `output-supervisor`, as the canonical rule source when chain-triggered.

Severity grouping: **CRITICAL** (any one failing → overall FAIL) vs **WARN**.

---

## CRITICAL（缺一個就 FAIL）

### Structural

- [ ] **Output is a literature table** with all required columns: `Ref | Title | Venue | DOI/PMID/arXiv | Region | Finding | Gap`
- [ ] **Top-of-output disclosure** declares whether web search was invoked
- [ ] **If web search was unavailable** all citations are marked `[TRAINING-RECALL — user to verify]` AND this is disclosed at the top

### Verification tagging

- [ ] **Every row carries exactly one verification tag**: no-tag (verified) / `[UNVERIFIED]` / `[TRAINING-RECALL — user to verify]` / `[SEMINAL]`
- [ ] **No citation without a verification tag** anywhere in the table
- [ ] **Time window respected**: ≤ 5 years for primary refs; > 5 years allowed ONLY when tagged `[SEMINAL]` (and even then ≤ 10 years)

### Geographic differentiation

- [ ] **Region column is present and filled** for every row (TW / Asia / US / EU / Other)
- [ ] **Regional novelty is preserved** — globally novel vs novel-in-TW-only is not blurred

### Citation hygiene

- [ ] **No bare URLs as citations** — DOI / PMID / arXiv ID extracted into the dedicated column
- [ ] **Preprints flagged explicitly** in the Venue column (e.g., "arXiv (preprint)") — not conflated with peer-reviewed venues
- [ ] **No Wikipedia, news articles, or marketing pages** cited as primary clinical references

### Coupling to downstream

- [ ] **Every Part A reference is cited in at least one Part D candidate's novelty section** — papers that do not justify any candidate are removed (per Step 4)

---

## WARN

### Structural quality

- [ ] **Gap column** identifies an actual research gap, not a summary restatement of Finding
- [ ] **Citation count is reasonable for proposal scope** (typically 8–25 entries; flag if dramatically outside)
- [ ] **AUROC vs clinical utility distinction** is preserved when relevant

### Hygiene

- [ ] **DOI / PMID format consistent** (DOI as `10.xxxx/yyyy`, PMID as digits)
- [ ] **Venue field meaningful** — journal/conference name resolves uniquely
- [ ] **Order of rows is intentional** (chronological, by region, or by topic — pick one)
