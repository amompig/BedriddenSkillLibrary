# Data Room Ingestion (v2 mode)

When the user provides a directory rather than a single markdown file, run this protocol. The skill must (1) discover what files exist, (2) classify them by role, (3) confirm classification with the user, (4) read the relevant ones within budget.

---

## Mode detection

In SKILL.md Step 1:
- Single file path → v1 mode → skip this file
- Directory path → v2 mode → run this file

If neither is clear, AskUserQuestion before proceeding.

---

## Step A: Enumerate the directory

List all files (recursive). Capture:
- Filename
- Extension
- Size (skip if size could be derived from `ls`)
- Last-modified date if available

Do NOT read content yet.

If the directory has > 50 files, prompt the user: "Data room has N files. Would you like me to focus on a specific subset?" Default behavior if no user response: continue with classification (heuristic will narrow).

---

## Step B: Heuristic classification

Apply filename pattern matching to assign each file a likely role:

| Pattern (case-insensitive) | Likely role | Priority |
|-----------------------------|-------------|----------|
| `pitch*` / `*deck*` / `*presentation*` | Pitch deck (CRITICAL) | 1 |
| `*business*plan*` / `bp.*` / `*plan.docx` | Business plan (CRITICAL) | 1 |
| `*financial*` / `*model*` / `*projection*` | Financial model | 2 |
| `*cap*table*` / `*captable*` / `*ownership*` | Cap table | 2 |
| `*ip*` / `*patent*` / `*fto*` | IP / patents | 3 |
| `*customer*` / `*case*study*` / `*reference*` | Customer references | 3 |
| `*resume*` / `*cv*` / `*founder*background*` | Founder resumes | 3 |
| `*board*` / `*update*` / `*report*` | Prior board materials | 3 |
| `*term*sheet*` / `*safe*` / `*convertible*` | Prior round docs | 4 |
| `*compliance*` / `*soc2*` / `*iso*` | Compliance docs | 5 |
| `*contract*` / `*agreement*` | Customer / vendor contracts | 5 |
| Anything else | Unclassified | 5 |

Priority levels (1 = highest priority for diligence reading):
- **1 — CRITICAL**: must have at least one
- **2 — Cross-reference value**: read if present
- **3 — Verification value**: read if relevant to specific claims
- **4 — Background reading**: skim only
- **5 — Tangential**: only read if specifically pointed at

---

## Step C: Mandatory check — central artifact present?

Confirm at least one Priority-1 file exists (pitch deck OR business plan). If not:

```
**ABORT**: This skill requires at least one central artifact (pitch deck or business plan).
The data room provided contains only: [list classified files].

Either:
- Provide a pitch deck / business plan, OR
- Use v1 mode with a single markdown file
```

Do not attempt to write the memo without a central artifact. The memo's structure depends on the central pitch as anchor.

---

## Step D: User confirmation of classification

Present the heuristic classification to the user and ask for confirmation/override:

```
I classified the data room as follows:
- Pitch deck: pitch_deck_v3.pdf (Priority 1)
- Financial model: ProActiveDB_FinancialModel.xlsx (Priority 2)
- Cap table: ProActiveDB_CapTable.xlsx (Priority 2)
- Customer references: Q1_2026_References.pdf (Priority 3)
- Unclassified: misc_notes.txt, archive_old/ (Priority 5)

Confirm or override? Specifically:
- Did I miss anything important?
- Are any classifications wrong?
- Anything I should NOT read for any reason (confidentiality, irrelevance)?
```

Use AskUserQuestion. Wait for user before proceeding to Step E.

---

## Step E: Read budget

Apply the limits:

- **Deep read** (full content into context, used for memo writing): up to 10 files
- **Skim read** (titles, first page, key tables): up to 30 files
- **Skipped**: anything beyond these limits

Allocation logic:
1. Always deep-read all Priority-1 files (typically 1)
2. Deep-read all Priority-2 files (typically 0–3)
3. Deep-read up to 5 most-relevant Priority-3 files (driven by what claims need verification)
4. Skim up to 30 of remaining Priority-3 / -4 / -5 files
5. List anything beyond as "Not read; available if specifically requested"

---

## Step F: Tool dispatch by file type

For each file to be read, dispatch to the appropriate sub-tool. **Skill cannot directly invoke another skill** — instead, the SKILL.md tells the orchestrator (Claude) to invoke the appropriate skill.

| Extension | Tool / skill |
|-----------|--------------|
| `.md` / `.txt` | Direct Read tool |
| `.pdf` | Invoke `anthropic-skills:pdf` to extract text |
| `.pptx` | Invoke `anthropic-skills:pptx` to extract slides |
| `.xlsx` / `.xls` | Invoke `anthropic-skills:xlsx` to extract sheets |
| `.docx` | Invoke `anthropic-skills:docx` to extract text |
| `.csv` | Direct Read tool (or xlsx for tabular operations) |
| `.png` / `.jpg` | Read tool (vision) for charts / diagrams; mention in memo only if content matters |

If a needed tool / skill is unavailable, mark the file `[unread — tool unavailable]` and proceed without its content. Do not abort.

---

## Step G: Cross-document fact extraction

Once files are read, extract facts each file claims about the company. For each fact, attempt cross-reference:

| Fact source | Cross-reference target |
|-------------|-------------------------|
| Pitch deck claims ARR $X | Financial model — does it show same? |
| Pitch deck claims headcount Y | Cap table headcount + financial model salary line |
| Pitch deck claims top-3 customer concentration | Customer references — do top-3 names appear? |
| Pitch deck claims growth rate Z | Financial model historical revenue series |
| Pitch deck claims founder titles | Founder resumes — do they match? |
| Cap table shows valuation cap | Pitch deck — is it consistent? |

Discrepancies are diligence gold. Surface them in §1 as material findings:

> "Pitch claims $4M ARR; financial model shows $3.2M LTM ARR. Difference appears to be contracted-but-not-recognized revenue. Material — must clarify before proceeding."

These cross-document discrepancies are what the v2 mode adds beyond v1. They feed into §7 (Traction) and §8 (Risk) prominently.

---

## Step H: Read-trail in memo appendix

Add an appendix to the memo titled "Data Room Read Trail":

```markdown
## Appendix: Data Room Read Trail

| File | Classification | Read level | Key extractions |
|------|----------------|------------|------------------|
| pitch_deck_v3.pdf | Pitch (P1) | Deep | ARR $4M, NRR 130%, raise $20M |
| FinancialModel.xlsx | Financial model (P2) | Deep | LTM rev $3.2M, burn $400K/mo, runway 14mo |
| CapTable.xlsx | Cap table (P2) | Deep | Founder 65%, Seed 18%, ESOP 17% |
| References.pdf | Customer refs (P3) | Skim | 3 named customers; top 1 = 35% of ARR |
| misc_notes.txt | Unclassified (P5) | Skipped | — |
```

This trail must be present for v2 audits (audit_checklist.md will require it).

---

## v1 fallback path (single markdown file)

If user provides a single markdown file (or a directory containing only markdown):

- Skip Steps A–G
- Treat the markdown as the central artifact
- The memo's data integrity is bounded by what the pitch provides
- Section §7 (Traction) and parts of §10 (Valuation) will heavily rely on `[needs-research]` for missing financial-model / cap-table data
- The memo header should note: `Input mode: v1 single-file. Cross-reference verification not performed (no financial model / cap table available).`

This degraded path is fine — better than refusing to run. Just be honest about the limitation.
