# Stage Calibration

The IC memo has 11 sections. Their **relative weights and depth** depend on the stage. Pre-seed is fundamentally about team + market + early signal; Series A is fundamentally about traction + unit economics. Forcing the same depth across stages produces bloated, unfocused memos.

This file gives the calibration table and per-stage notes.

---

## Stage detection

Extract from pitch metadata or AskUserQuestion. Acceptable stages:

- **Pre-seed** — typically <$1M raised total, 1–5 people, MVP / no revenue
- **Seed** — typically $1–4M raised, 5–15 people, early revenue or LOIs
- **Series A** — typically $4–15M raised, 15–40 people, $1M+ ARR or material traction
- **Series B+** — typically $15M+ raised, 40+ people, $5M+ ARR

If the stage is genuinely ambiguous (e.g., "seed extension" / "pre-Series A bridge"), pick the closer of the two and note in §1.

---

## Section weight table

| Section | Pre-seed | Seed | Series A | Series B+ |
|---------|----------|------|----------|-----------|
| §1 Exec Summary | 200w | 200w | 250w | 300w |
| §2 Thesis Fit | **400w** | 300w | 250w | 200w |
| §3 Team | **700w** | 600w | 500w | 400w |
| §4 Market | **600w** | 700w | 700w | 600w |
| §5 Product / Tech | 500w | **600w** | **600w** | 400w |
| §6 Competition | 500w | **600w** | **800w** | **700w** |
| §7 Traction & Unit Econ | 200w (mostly needs-research) | 400w | **800w** | **900w** |
| §8 Risk Matrix | 400w | 500w | 600w | 500w |
| §9 Open Questions | 300w | 300w | 300w | 200w |
| §10 Term Sheet & Val | 200w (sketch only) | 300w | **500w** | **600w** |
| §11 Final Recommendation | 200w | 250w | 300w | 300w |

**Bold = priority section for that stage.** Total memo size:
- Pre-seed: ~4,200w
- Seed: ~4,750w
- Series A: ~5,600w
- Series B+: ~5,000w

These are guidelines, not hard caps. Hard cap remains 7,500 words total.

---

## Per-stage notes

### Pre-seed

- **§3 Team is the heaviest section** — at this stage, you're betting on founders. Apply team-size scaling (`team_size_scaling.md`) heavily.
- **§7 Traction is mostly `[needs-research]`** — that's expected. Don't fake-FAIL the section.
- **§10 Valuation is sketch only** — 200w max. Pre-seed valuation is usually a SAFE / convertible note with cap. State the cap range, methodology = "pre-seed market for this category", don't try to be sophisticated.
- **§2 Thesis Fit is heavier** — at pre-seed, "is this our type of bet" matters more because there's nothing else to evaluate.
- Founder-market-fit must be the strongest part of the memo.

### Seed

- **§5 Product / §6 Competition both heavier** — by seed, the product hypothesis is testable. Hold it accountable.
- **§7 Traction starts mattering** — early ARR / users / pilots / LOIs. Compare to seed-stage benchmarks (e.g., $250K–$1.5M ARR is normal).
- **§10 Valuation** still SAFE-friendly but with priced-round comparable signal. 300w; 1–2 comparable seed rounds.
- Open questions (§9) can include "what would a Series A look like" — bridges the next round.

### Series A

- **§7 Traction & Unit Economics is the heaviest section.** Series A is a unit-economics moment. NRR / GM / CAC payback / Magic Number / Burn multiple all interrogated.
- **§6 Competition is heavy** — by Series A, the founder has had time to know all competitors. The memo expects 4-layer fully populated.
- **§10 Valuation is critical** — full comparable transactions table. Pre-money / post-money. Term sheet sketch.
- **§3 Team less heavy than pre-seed** — by now, team has track record on this company. Evaluate execution to date.

### Series B+

- **§7 + §10 dominate.** Series B is a financial-discipline moment. Burn multiple, gross margin trajectory, sales efficiency, all under scrutiny.
- **§6 Competition** stays heavy — by Series B, market dynamics and competitive positioning have crystallized.
- **§5 Product weights down** — by now, product is what it is. Unit economics of the existing product matter more than product roadmap fantasy.
- **§9 Open Questions becomes strategic** — board composition, governance, secondary opportunities, IPO timing readiness.
- **§10 Valuation full** — multiple methodologies (revenue multiple + DCF-lite + recent comps). Cap table modeling for follow-on.

---

## Consistency checks

The memo's stage handling should be consistent. Flag inconsistencies:

- A "Series A" pitch with $200K ARR is mislabeled — likely seed
- A "seed" pitch with $5M ARR is mislabeled — likely Series A
- "Pre-seed" pitch with 30 employees is mislabeled

If pitch's stated stage doesn't match the substantive metrics, the IC memo should call this out in §1 ("pitch claims Series A, but financials read as seed extension").

---

## When to override stage weights

Two situations override the default weights:

1. **Domain overlay forces emphasis change**: e.g., for biotech therapeutics at pre-seed, §5 Product / Tech is heavier than the table suggests because the mechanism plausibility is the central question.
2. **The investor's specific concern requires emphasis**: e.g., if the partner has a strong prior about category congestion, §6 may need to expand even at pre-seed.

In these cases, deviate from the weight table but note the deviation in the memo header (e.g., "Note: §5 expanded beyond stage default due to therapeutic mechanism diligence").
