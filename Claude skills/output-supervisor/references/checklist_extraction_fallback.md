# Checklist Extraction Fallback

This is the heuristic used when a source skill lacks `references/audit_checklist.md`. Read this when Step 1b fires.

The goal is **best-effort signal**, not authoritative audit. The fallback report must clearly mark itself as such (see Step 1b in `SKILL.md`).

---

## Source materials to scan

In order of priority:

1. `D:\Claude skills\<source_skill>\SKILL.md` — primary source
2. `D:\Claude skills\<source_skill>\references\quality_checklist.md` — if exists, this is a near-equivalent of audit_checklist.md (older naming convention). Treat its items as `WARN` by default unless the file uses CRITICAL/WARN sections.
3. `D:\Claude skills\<source_skill>\references\anti_patterns.md` — extract each anti-pattern as a `CRITICAL` "do not produce X" rule.
4. `D:\Claude skills\<source_skill>\references\*.md` for any other file whose name contains "verify", "check", "validate", "rules" — extract structural rules.

## Extraction patterns

Look for these phrasing patterns in SKILL.md and references/:

| Pattern in source                                                | Extract as rule                                       | Severity |
|-------------------------------------------------------------------|-------------------------------------------------------|----------|
| "must" / "mandatory" / "non-negotiable" / "always" / "必須" / "一律"  | Hard requirement                                      | CRITICAL |
| "do not" / "forbidden" / "禁止" / "不可"                            | Hard prohibition                                      | CRITICAL |
| "should" / "recommended" / "建議" / "傾向"                          | Soft expectation                                      | WARN     |
| "first block" / "always at the top" / "the first … must be …"     | Structural placement rule                             | CRITICAL |
| "if X, then Y" / "若 X 則必須 Y"                                   | Conditional rule (record the condition)               | derive from inner phrasing |
| Numbered/bulleted "Quality Checklist" or similar list             | Each item becomes a rule; severity from list framing  | derive   |

## Examples

Source: SKILL.md says "The first block of every output is a **Mandatory Assumption Disclosure Table**"
Extracted rule: `[CRITICAL] Output begins with a Mandatory Assumption Disclosure Table as the first block`

Source: anti_patterns.md says "Anti-pattern: 'no competitors' statement"
Extracted rule: `[CRITICAL] Output does not contain a 'no competitors' or equivalent statement`

Source: SKILL.md says "Slide count matches duration — roughly 1 slide per minute"
Extracted rule: `[WARN] Slide count is within ±20% of (duration in minutes)`

## Cap on extracted rules

To avoid exploding the audit, cap at:

- 12 CRITICAL rules (drop the least specific if more are extracted)
- 12 WARN rules

If the source has more than this, that itself is a signal worth surfacing: "Source skill has rich rules but no canonical checklist — strongly recommend creating one."

## Fallback report header

The report MUST open with:

```markdown
> ⚠️ **Fallback mode** — `<source_skill>` does not have `references/audit_checklist.md`. Rules below were extracted heuristically from SKILL.md and references/. Coverage is best-effort. To stabilize future audits, create an explicit `audit_checklist.md`.
```

This is non-negotiable. Without this header, future readers may mistake fallback findings for canonical findings.

## Things NOT to extract

- General persona / voice guidance (not auditable rules)
- Step-by-step instructions to the skill itself (these guide the producer, not the deliverable)
- Examples / illustrations
- "Read references/X.md" pointers
- Frontmatter

## Final note for the orchestrator

After running a fallback audit, **always** include in the chat summary an offer to draft a real `audit_checklist.md`. Even if the user declines, planting the suggestion repeatedly will eventually nudge them to create one — at which point the fallback path retires for that skill.
