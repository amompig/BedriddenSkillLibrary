# Mandatory fields per candidate topic

Every Part D candidate must have ALL of the following. Missing fields = candidate not ready to propose.

## Required fields

1. **Title** — clear, specific, fundable-sounding
2. **One-paragraph rationale** — why this matters now, what it unlocks
3. **Technical approach** — model class, training paradigm, validation strategy
4. **Data sources** — imaging cohort + claims linkage
5. **Primary endpoint** — outcome that determines success / failure
6. **Novelty vs prior work** — cite refs, with **explicit regional scope** ("globally novel" / "novel in TW only" / etc.)
7. **Single point of failure (SPOF)** — the one most likely reason this project fails to produce a first-author paper within 18 months
8. **Mitigation for SPOF** — concrete plan, or explicit acknowledgment that none exists
9. **Other risks** — secondary risks not captured by SPOF
10. **Timeline / resources** — months to milestones, FTE / equipment / cost
11. **Funding fit** — primary mechanism + backup mechanism (per `funding_fit_table.md`)

## Why SPOF is mandatory

Most research proposals fail not from random aggregation of small risks but from one dominant risk. Naming it forces:
- Honest assessment of feasibility
- Pre-planning of the one critical mitigation
- Reviewer confidence (named risks are perceived as credible plans)

Common SPOF patterns for ED-ultrasound + claims projects:
- Multi-center prospective imaging cohort recruitment speed
- Federated infrastructure operational complexity
- POCUS uncoded → claims-only signal dilution
- Regulatory pathway uncertainty for novel SaMD subclass
- Single-PI bandwidth across multiple complex deliverables

If your candidate's SPOF matches one of these patterns, double-check that the mitigation is independent of any assumption that already failed in similar studies.

## Down-selection rule for Top 3

- Rank by total score on the 7 criteria
- Provide a one-line "why this beats the others" per top-3 entry
- **Tie-breaker**: prefer the candidate with lower data-feasibility risk (criterion 3)
- **Second tie-breaker**: prefer candidate with named SPOF mitigation over candidate with acknowledged-but-unmitigated SPOF
