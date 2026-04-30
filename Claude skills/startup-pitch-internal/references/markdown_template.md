# Markdown Output Template (Internal Variant)

The output structure varies by level. Always start with the Mandatory Assumption Disclosure Table, then apply the level-specific template.

## Mandatory Assumption Disclosure Table (always first)

````markdown
# [Company Name] — [Level] Update — [Period]

> **Variant**: internal
> **Level**: [team / department / board / all-hands]
> **Audience**: [specific group]
> **Period**: [e.g., Q1 2026, week of 2026-04-21]
> **Meeting date**: [date]
> **Duration**: [X minutes, ~Y slides]
> **Language**: [Chinese / English / bilingual]
> **Product Type Classification**: [type] → biotech subflow depth: [full / light / N/A]
> **Story Structure**: [Internal Sync / Board Update / All-hands narrative]

---

## Mandatory Assumption Disclosure Table (Block 0)

| Step 1 question | Value | Status |
|----------------|-------|--------|
| 1. Purpose | [value] | given |
| 2. Audience | [value] | given |
| 3. Stage | [value] | given |
| 4. Duration | [value] | given |
| 5. Language | [value] | given |
| 6. Level | [team / department / board / all-hands] | given |
| 7. Existing version | [yes / no] | given |
| 8. Domain disambiguation | [if applicable, resolved domain] | given |
| 9. Product type | [classification] | given |
| 10. **Prior baseline** | [last period plan & action items, OR "first update — no prior baseline"] | [given / 🔴 needs-data] |

> Items not provided appear as 🔴 needs-data. For internal recurring updates (board / department quarterly), missing prior baseline is a major gap.

---
````

## Level-specific templates

### Team Update Template

```markdown
## Slide 1 — Cover
- Team name and period

## Slide 2 — Last period
- What shipped / completed
- Bullet list, with brief detail

## Slide 3 — Blockers and dependencies
- Each blocker with what unblocks it

## Slide 4 — This period goals
- 3–5 specific outcomes

## Slide 5 — KPI snapshot
- 3–5 headline numbers, each with [verified — system, date]

## Slide 6 — Action items / asks
- Specific items, each with owner and timing
```

### Department Update Template

```markdown
## Slide 1 — Cover
- Department name and period

## Slide 2 — Agenda

## Slide 3–4 — KPI vs Target
- Table: KPI / Target / Actual / Δ / Status
- Each Actual: [verified — system, date]

## Slide 5 — Cross-team dependencies
- What we are blocking, what we are blocked by

## Slide 6 — Hiring
- Open roles, in-flight, recently filled

## Slide 7 — Budget
- Burn vs plan
- [verified — financials, period close]

## Slide 8 — Top 3 risks
- Each with mitigation

## Slide 9 — Action items / decisions needed
- Specific, owner, timing
```

### Board Update Template

```markdown
## Slide 1 — Cover
- Period, meeting date

## Slide 2 — Agenda

## Slide 3–4 — KPI vs Plan
- Full headline metrics
- Plan / Actual / Δ / Status (color-coded)
- Every Actual cell: [verified — system, date]

## Slide 5 — Top 3 wins

## Slide 6–7 — Top 3 misses
- Each miss: number, root cause, response

## Slide 8 — Surprises this quarter
- Each surprise tagged with: "Moat re-check triggered: [Y/N] + reason"
- For triggered surprises, point to the moat re-check chapter

## Slide 9–11 — Competitor analysis & 36-month moat re-check
- Only if any surprise triggered re-check
- Full weighted-score table, prior vs current
- Verdict and response

## Slide 12–13 — Strategy adjustments
- How response to misses and surprises shapes next quarter

## Slide 14 — Capital state
- Cash position, burn vs plan, runway months
- Next-round timing

## Slide 15 — Risk register
- Top 3–5 risks across technical / talent / budget / market

## Slide 16–17 — Decision items for board (mandatory)
- Each decision: proposed action, predicted impact, what is being asked

## Slide 18 — Q+1 commitments
- 3–5 specific deliverables for next board meeting

## Slide 19 — Open Q&A
```

### All-hands Template

```markdown
## Slide 1 — Cover

## Slide 2 — Vision recap
- One slide reaffirming the why

## Slide 3–5 — Quarter wins
- Concrete: project names, customer names, milestone names

## Slide 6 — Numbers overview
- High-level company KPIs with context

## Slide 7 — The one big thing this quarter
- The most important development to celebrate or rally around

## Slide 8–9 — Challenges and our response
- Honest about hard things; never just "things are hard"
- Always paired with what is being done

## Slide 10 — New people / promotions
- Humanize, build community

## Slide 11–12 — Roadmap preview
- What is coming next quarter

## Slide 13 — Recognition / culture moment
- A story or callout that reinforces values

## Slide 14 — Q&A
```

## Common closing sections (apply to all levels)

````markdown
---

## Data Citation Table

| Slide | Data point | Source | Status |
|-------|-----------|--------|--------|
| 3 | ARR $250K | Internal financials, 2026-03-31 | verified |
| 3 | NRR 110% | 🔴 [needs-data — billing system snapshot pending] | needs-data |
| ... | ... | ... | ... |

---

## Action Items / Board Resolutions

| # | Item | Proposed action | Owner | Timing |
|---|------|----------------|-------|--------|
| 1 | [item] | [action] | [name / role] | [date or window] |
| 2 | ... | ... | ... | ... |

---

## Anti-pattern Self-check Results (internal)

- [ ] No whitewashing of misses — exact numbers and root causes shown
- [ ] No surprises without action plan attached
- [ ] (Board only) Every surprise tagged with moat re-check status
- [ ] (Board only) Decision items are concrete, not "discuss" / "explore"
- [ ] (All-hands only) Vision recap + emotional through-line + recognition moment present
- [ ] No manufactured optimism — hard things named honestly
- [ ] Time allocation respects discussion needs (board: 30–40% on discussion; all-hands: 15+ min Q&A)

---

## Notes for the founder / presenter

[Concerns about the deck, items that need to be resolved before the meeting, any moat-check verdicts that imply hard conversations]
````

## Key rules

- **Block 0 is mandatory regardless of level** — even a team-weekly deck should have it (lighter, but present)
- **For board updates, the surprises section AND the moat-recheck-trigger tags are mandatory** — this is the single most important guardrail at board level
- **Decision items / action items must be concrete** — owner and timing for every item, no exceptions
- **For all-hands, the emotional through-line is non-negotiable** — vision recap and recognition slide must be present even in a hard quarter
