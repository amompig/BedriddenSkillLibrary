---
name: output-supervisor
description: Audit a skill's deliverable (currently markdown only) against that skill's audit checklist. Trigger on phrases like "audit this output", "check this pitch deck against the rules", "review this deliverable", "supervise the output", "second-pair-of-eyes review", "驗收 skill 輸出", "稽核 pitch outline", "檢查產出是否符合 skill 規則", "對這份輸出做監督檢查". Designed to be chain-triggered automatically at the end of a content-producing skill (per SKILL_STORAGE_RULES §9), but can also be invoked manually. Reads the source skill's `references/audit_checklist.md` (canonical) — if missing, falls back to extracting checks from the source SKILL.md and warns the user to add a checklist file. Produces a CRITICAL/WARN classified audit report at `_meta/audits/output/<source-skill>/<timestamp>__<verdict>.md`. Do NOT use this skill for governance of the skills repository structure (use skill-governance for that). Do NOT use for non-markdown deliverables in v1 (docx/pptx/xlsx audit will come in v2).
---

# Output Supervisor — Generic Deliverable Auditor

A second pair of eyes for any content-producing skill. After a skill produces a deliverable, this skill reads the source skill's audit checklist and verifies item-by-item that the deliverable satisfies each rule.

## When to use

- **Chain trigger** (default): A content-producing skill ends with "Step N: invoke output-supervisor with target_file and source_skill". This is wired into `startup-pitch-investor`, `startup-pitch-internal`, etc.
- **Manual invocation**: User asks "audit this output", "驗收這份 outline", or hands you a markdown file plus the name of the skill that produced it.

Do **NOT** use for auditing the skills-repo structure — that is `skill-governance`'s job. Do **NOT** use for docx/pptx/xlsx in v1 — markdown only.

## Input contract

Two parameters required:

1. **`target_file`** — absolute path to the markdown file to audit
2. **`source_skill`** — name of the skill that produced it (must match a folder name under `D:\Claude skills\`)

If either is missing, ask the user via AskUserQuestion before proceeding. Do not guess.

## Step 1 — Locate the audit checklist

Look in this order:

1. `D:\Claude skills\<source_skill>\references\audit_checklist.md` ← **canonical source** (per SKILL_STORAGE_RULES §9)
2. If missing → run **fallback** (see Step 1b)

### Step 1b — Fallback when checklist is missing (graceful degradation)

If `audit_checklist.md` is absent:

1. Read `D:\Claude skills\<source_skill>\SKILL.md`.
2. Read `references/checklist_extraction_fallback.md` for the extraction heuristic.
3. Apply heuristic to derive an *ad-hoc* checklist from SKILL.md.
4. **In the audit report header, prominently flag** that this skill lacks an `audit_checklist.md` and that the audit is therefore best-effort. Recommend the user create one for stable supervision.
5. Continue with the audit. Do not abort — the goal is to surface signal to the user, not block them.

## Step 2 — Read the target file

Read the full markdown content. Note structural anchors (section headers, tables, code fences) that the checklist will reference.

## Step 3 — Run each checklist item

For each item:

- Determine severity from its tag (`CRITICAL` or `WARN`). If untagged in the source, default to `WARN` and note this.
- Search the target for evidence the rule is satisfied.
- Verdict: **PASS** / **FAIL** / **WARN**.
- Capture **evidence**: a quoted excerpt or line reference from the target file, OR the absence note ("no `[verified]` labels found anywhere in deck").

### Severity conventions

- `CRITICAL` rule violated → contributes to overall `FAIL`.
- `WARN` rule violated → contributes to overall `WARN` (only if no CRITICAL).
- All clear → `PASS`.

### Judgment principles

- Evidence-first: every FAIL must cite a passage (or its absence). Do not hand-wave.
- Be charitable on phrasing variations; be strict on the rule's substance. (E.g., "competitor analysis" can be titled "誰已經在做" — same rule.)
- If the rule is genuinely ambiguous given the target's structure, mark `INDETERMINATE` and explain. Do not silently pass.

## Step 4 — Compute final verdict

- Any `CRITICAL` violation → `FAIL`
- Otherwise any `WARN` violation → `WARN`
- Otherwise → `PASS`

## Step 5 — Write the report

Path: `D:\Claude skills\_meta\audits\output\<source_skill>\<timestamp>__<verdict>.md`

(Create directories if missing.)

Sections:

1. Header: target file path, source skill, timestamp, verdict, fallback flag (if any)
2. Summary: counts of CRITICAL FAIL / WARN / PASS / INDETERMINATE
3. Per-checklist-item findings: rule text, severity, verdict, evidence (or absence note)
4. Recommended fixes: for each FAIL, one-sentence concrete suggestion

## Step 6 — Summarize to user

In chat, report:

- The final verdict and one-line reason.
- All `CRITICAL FAIL` items with rule + evidence + suggested fix (full list).
- Count of `WARN` and `INDETERMINATE` items (offer to expand on request).
- Path to the full report.

If verdict is `FAIL`, ask: **「要我依建議直接修補目標檔案嗎？」** Wait for confirmation. Do not silently edit the target.

If `audit_checklist.md` was missing (fallback was used), close with: **「建議在 `<source_skill>/references/audit_checklist.md` 補上正式 checklist，讓未來稽核更穩定。要我幫你起草一份嗎？」**

## Notes

- This skill never modifies the target file without explicit user confirmation.
- Reports accumulate in `_meta/audits/output/<source-skill>/`. They are not auto-pruned; consider periodic cleanup.
- v2 (future): support docx/pptx/xlsx targets — likely via reading the deliverable through the corresponding skills' read tools.
