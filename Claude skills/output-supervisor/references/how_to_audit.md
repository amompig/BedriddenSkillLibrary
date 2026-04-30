# How to Audit — Detailed Mechanics

This file expands on Steps 3–5 of `SKILL.md`. Read it when running an audit if you need detail beyond the SKILL.md outline.

## Reading the audit_checklist.md

`audit_checklist.md` is a **prose checklist with severity headers**. Expected shape:

```markdown
# Audit Checklist for <source-skill>

## CRITICAL（缺一個就 FAIL）

- [ ] <Rule 1>
- [ ] <Rule 2>
...

## WARN

- [ ] <Rule A>
- [ ] <Rule B>
...
```

Each rule line is the canonical statement of what to check. The severity is determined by which `## CRITICAL` / `## WARN` section it sits under, NOT by any inline tag.

If a rule line contains an inline `[CRITICAL]` or `[WARN]` tag that conflicts with the section header, the section header wins — note the inconsistency in the audit report as a `housekeeping` note.

## Verdict per rule

For each rule, choose ONE:

| Verdict | When to use |
|---------|-------------|
| **PASS** | Evidence in the target clearly satisfies the rule. |
| **FAIL** | Either (a) clear violation, or (b) rule mandates presence of X and X is absent. |
| **WARN** | Partial satisfaction — present but weak (e.g., disclosure exists but lacks specificity). Only valid for `WARN`-severity rules; for `CRITICAL`-severity, "weak" still counts as FAIL. |
| **INDETERMINATE** | Genuinely ambiguous (e.g., target uses unusual structure that may or may not satisfy rule). Always explain why. |

## Evidence requirement

Every FAIL and INDETERMINATE must cite evidence. Evidence types:

1. **Quoted passage**: copy 1–3 lines of the target file showing the violation, with line number if available
2. **Absence statement**: explicit "Searched for X in target; no occurrence found"
3. **Structural reference**: "Section 'Competitor Analysis' is missing from the target"

Do NOT write FAIL without evidence. If you cannot find evidence, mark INDETERMINATE.

## Charitable matching

Authors will phrase things differently from the rule. Match on substance:

- Rule: "Competitor analysis with 36-month moat test"
  - Match: a section titled "誰會在 36 個月內追上我們" with a moat table
  - Match: a section titled "Defensibility" with weighted scoring against the six dimensions
  - **No match**: a section titled "Why we win" with vague claims and no scoring

- Rule: "Every quantitative claim has a `[verified]` / `[assumption]` / `[needs-data]` label"
  - Match: explicit tags on every number
  - **No match**: tags appear sometimes but not on the obvious numbers in the TAM slide

## Common deliverable patterns

Most content-producing skills in this repo output Markdown with these conventions:

- A "Mandatory Assumption Disclosure Table" near the top — search for it; absence is almost always a CRITICAL FAIL for pitch outputs.
- Slide-by-slide content under `### Slide N` headers.
- A "Data Citation" or similar table near the end.
- An "Anti-pattern Self-check Results" section at the bottom.

When auditing pitch outputs specifically, these structural anchors are your first-pass scan targets.

## Writing the report

The report file at `_meta/audits/output/<source-skill>/<timestamp>__<verdict>.md` should be readable standalone — someone who didn't run the audit should be able to make sense of it.

Recommended structure:

```markdown
# Output Audit — <source-skill>

- Target: <absolute path>
- Source skill: <name>
- Timestamp: <YYYYMMDDTHHMMSS>
- Verdict: <PASS | WARN | FAIL>
- Fallback used: <yes/no — if yes, explain>

## Summary

- CRITICAL FAIL: <n>
- WARN: <n>
- INDETERMINATE: <n>
- PASS: <n>

## CRITICAL violations

### 1. <Rule text>
- Verdict: FAIL
- Evidence: <quote or absence note>
- Suggested fix: <one-line>

(repeat per CRITICAL FAIL)

## WARN violations
(same shape, lower severity)

## INDETERMINATE
(same shape, with explanation of why)

## PASS items
(can be a one-line list — do not pad)
```

## OFFLINE-mode awareness for count-threshold rules

Some `audit_checklist.md` rules require minimum counts (e.g., "Layer 3 ≥5 named competitors", "≥3 comparable transactions"). These rules typically depend on web search being available.

**When auditing a memo produced in OFFLINE mode**:

- If a count-threshold rule depends on web-search-only data (stealth competitors, comparable deal valuations, specific funding rounds, fresh market sizing), and the memo has:
  - Prominent OFFLINE banner at the top, AND
  - The relevant section consists entirely of `[needs-research]` or `[OFFLINE — RECALL ONLY]` entries with explicit acknow