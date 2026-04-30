---
name: clinical-research-ideation
description: Use whenever the user wants to brainstorm, evaluate, rank, or score clinical / translational research topics for fundability and feasibility — especially in the Taiwan funding ecosystem (NSTC / NHRI / MOHW) plus international agencies (NIH R21/R01, EU Horizon). Trigger on phrases like "find research topics", "ideate", "evaluate this research idea", "score these candidates", "rank by fundability", "fundable topics", "research direction", "score matrix", "ranked recommendations", "什麼題目值得做", "題目發想", "可行性評估", "計畫書方向", "研究主題排序", "幫我想題目". Enforces 7-criteria scoring (clinical need / technical novelty / data feasibility / outcome measurability / regulatory path / competitive landscape / funding fit), mandatory single-point-of-failure check per candidate, funding-fit mapping to specific Taiwan + international mechanisms, and negative constraints against saturated topics. Do NOT trigger for: pure literature search without ideation (use biomedical-lit-search); execution-stage protocol writing for an already-chosen topic; budget arithmetic; manuscript writing.
---

# Clinical / Translational Research Ideation Framework

This skill governs how candidate research topics are generated, scored, and ranked for fundability — typically Parts D and E of a research-ideation document.

## When to use
- Brainstorming candidate research topics in a defined domain
- Scoring or ranking existing topic candidates
- Evaluating fundability of a research direction
- Building a top-3 recommendation matrix

## Step 1: Apply 7-criteria evaluation framework
Read `references/seven_criteria.md`. Each candidate scored 1–5 on: (1) clinical unmet need, (2) technical novelty, (3) data feasibility, (4) outcome measurability, (5) regulatory path, (6) competitive landscape, (7) funding fit. Score 5 only when "best-in-class".

## Step 2: Map to specific funding mechanism
Read `references/funding_fit_table.md`. For each candidate, name a **primary** funding target plus **one viable backup** (e.g., NSTC AI Major / NHRI 整合型 / MOHW 緊急醫療政策計畫 / NIH R21 / etc.). "Applicable to multiple grants" is too vague.

## Step 3: Fill mandatory candidate fields
Read `references/candidate_fields.md`. Every candidate must have: title, rationale, technical approach, data sources, primary endpoint, novelty (with regional scope), single point of failure (SPOF) + mitigation, other risks, timeline, funding fit. Missing fields = candidate not ready to propose.

## Step 4: Down-select Top 3
Sum 7-criteria scores. Provide a one-line "why this beats the others" for each top-3 entry. **Tie-breaker**: prefer the candidate with lower data-feasibility risk (criterion 3). **Second tie-breaker**: prefer candidate with named SPOF mitigation over candidate with acknowledged-but-unmitigated SPOF.

## Step 5: Apply divergent heuristics if generating broad ideation list (Round 2 of staged mode)
Read `references/divergent_heuristics.md`. Cover ≥3 pain-point types, ≥2 modalities, include at least one low-tech / one high-tech / one policy-leverage candidate.

## What to deliver
- **Part D**: candidate cards with all mandatory fields filled.
- **Part E**: 7-criteria scoring matrix (1–5 each) + ranking + tie-break-aware "why beats others" line per top-3 entry.

## Negative constraints
- Do not recommend saturated topics (BUSI re-classification, EchoNet re-implementation) without a clear differentiator.
- Do not conflate technical AUROC with clinical utility — always separate the two.
- Do not claim global novelty if the topic is only TW-novel, or vice versa — be precise about regional scope.
- Do not propose data the user cannot realistically obtain (multi-center raw RF data without IRB; real-time inter-hospital streaming without governance).
- Do not propose timelines that ignore the 6–9 month HWDC + IRB lead time when claims linkage is involved.
- Do not score a 5 on any criterion without explicit justification — 5 means "best-in-class", not "good".
