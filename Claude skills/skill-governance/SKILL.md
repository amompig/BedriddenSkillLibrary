---
name: skill-governance
description: Run a compliance audit on the entire D:\Claude skills\ repository against SKILL_STORAGE_RULES §10. Trigger on phrases like "audit my skills", "check skill compliance", "lint skill repo", "skills governance check", "review skill repo structure", "稽核 skills", "整理 skill 目錄", "檢查 skill 結構", "skill 倉庫合規檢查". Use after creating a new skill (mandatory per SKILL_STORAGE_RULES §8), after bulk reorganization, or as periodic hygiene. Runs deterministic checks (root structure, frontmatter validity, kebab-case naming, line count ≤150, workspace residue, cross-skill references, _meta/ subdir classification) plus an LLM-judged description-quality check. Do NOT use for auditing the content of a single skill's deliverable — that is output-supervisor's job. Do NOT use for creating or editing skills — that is skill-creator's job.
---

# Skill Governance — Repo Audit

Runs the SKILL_STORAGE_RULES.md §10 violation checklist over the entire skills repository. Catches directory drift, frontmatter issues, line-count blowouts, workspace residue, and bad descriptions before they accumulate.

## When to use

- After `skill-creator` produces a new skill (chained per SKILL_STORAGE_RULES §8 step 7).
- After bulk reorganization of `D:\Claude skills\`.
- When the user explicitly asks for a skills audit ("audit my skills", "稽核 skills" etc.).
- Periodic hygiene check (suggest monthly).

Do **NOT** use for auditing a single skill's content output — that is `output-supervisor`'s job. Do **NOT** use for creating/editing a skill — that is `skill-creator`'s job.

## What it checks

Mapping to SKILL_STORAGE_RULES.md §10 violation checklist:

| # | Rule                                                                  | Detection | Severity |
|---|------------------------------------------------------------------------|-----------|----------|
| 1 | Root only contains skill folders, README, RULES, `_meta/`              | Script    | CRITICAL |
| 2 | Each skill has uppercase `SKILL.md` with valid frontmatter (name, description) | Script | CRITICAL |
| 3 | Skill folder name is kebab-case, no `vN` suffix                        | Script    | CRITICAL |
| 4 | `SKILL.md` is ≤150 lines                                               | Script    | WARN     |
| 5 | No workspace / eval residue inside any skill folder                    | Script    | CRITICAL |
| 6 | No relative cross-skill references (paths escaping skill folder)       | Script    | CRITICAL |
| 7 | Description has bilingual triggers + exclusion clause                  | LLM       | WARN     |
| 8 | `_meta/` subdirectories match approved categories                      | Script    | WARN     |

Rule 7 is the only LLM-judged item; rules 1–6 and 8 run deterministically via `scripts/audit.py`.

## Step 1 — Identify root

Default root is `D:\Claude skills\`. If the user supplied a different path, use that. Confirm with user only if ambiguous.

## Step 2 — Run the deterministic script

```
python "<this-skill-dir>/scripts/audit.py" --root "D:\Claude skills"
```

The script prints a JSON object to stdout with shape:

```
{
  "root": "...",
  "timestamp": "YYYYMMDDTHHMMSS",
  "rules": [{"id", "name", "severity", "violations"[]}, ...],
  "descriptions": {"<skill-name>": "<description text>", ...}
}
```

Capture this JSON. If the script exits non-zero, surface stderr to the user and stop.

## Step 3 — Judge descriptions (rule 7)

Read `references/description_quality_rubric.md`. For each entry in `descriptions`:

- Apply the three-ingredient rubric (bilingual triggers + concrete verb+noun phrases + explicit exclusion clause).
- Output verdict **PASS** or **WARN** (with the missing ingredient noted).

Rule 7 violations are appended as additional entries in the rules list before final reporting.

## Step 4 — Compute final verdict

- Any rule with severity `CRITICAL` and at least one violation → overall verdict `FAIL`.
- Otherwise, any rule with severity `WARN` and at least one violation → `WARN`.
- Otherwise → `PASS`.

## Step 5 — Write the report

Write a Markdown report to:

```
<root>/_meta/audits/repo/<timestamp>__<verdict>.md
```

Sections (in order):

1. Header (root, timestamp, verdict)
2. Summary counts (CRITICAL FAIL count, WARN count, PASS count)
3. Per-rule sections (1 through 8) — for each, the rule name, severity, and list of violations (or "All clear")
4. Rule 7 details — per skill description, verdict + reason

## Step 6 — Summarize to chat

Report to the user:

- Final verdict.
- For each CRITICAL FAIL violation: skill name, rule, suggested fix (one line each).
- Count of WARN violations (not all listed; offer to expand).
- Path to full report.

If the verdict is `FAIL`, ask the user: **「要我直接修補嗎？」** Do not auto-fix without confirmation. List the specific fixes you would apply, then wait for the user.

## Notes

- The script must be runnable with the standard Python 3 interpreter — no third-party dependencies.
- Frontmatter parsing is regex-based (handles `name:` and `description:` simple key:value, including multi-line description values that fold onto the next line).
- The script never modifies the repo. Fixes are always proposed and require user confirmation.
