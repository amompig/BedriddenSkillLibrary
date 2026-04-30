# Geographic differentiation and quality flags

## Region column (mandatory in Part A table)

Values: **TW / Asia / US / EU / Other**

Purpose: enable novelty triangulation. A topic that is novel in TW but saturated in US is a valid NSTC / NHRI proposal but a weak NIH proposal. Without the Region column this distinction cannot be made.

### Edge cases
- Multi-region collaborations: assign the primary affiliation
- Global meta-analyses: tag "Global" inside Other
- Asia studies with TW investigators: TW takes priority over Asia

## Quality flags to apply during review

For every paper considered for inclusion, ask:

1. **Technical AUROC ≠ clinical utility** — does the paper measure decision-impact, or only model performance?
2. **Single-center vs multi-center** — flag single-center prominently
3. **Prospective vs retrospective** — affects evidence weight
4. **External validation** — was the model tested on a held-out cohort matching the deployment population?
5. **Demographic match** — does the validation population match Taiwan / Asia demographics?
6. **Decision-change measurement** — most papers do not measure this; the rare ones that do are high-value citations

## How quality flags surface in Part A

When summarizing a paper's "Finding" column, prefer the clinical-utility framing if the paper supports it; otherwise note "technical AUROC only" explicitly. The Gap column should anticipate which downstream candidate will differentiate from this paper.
