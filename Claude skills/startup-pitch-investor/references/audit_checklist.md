# Audit Checklist — startup-pitch-investor

Used by **two consumers**:
1. The skill itself, as Step 6 (final self-gate before delivery).
2. `output-supervisor`, as the canonical rule source when chain-triggered.

Items are grouped by severity: **CRITICAL** (any one failing → overall FAIL) vs **WARN** (only failing → overall WARN). Within each group the order roughly matches the natural review pass.

---

## CRITICAL（缺一個就 FAIL）

### Structural

- [ ] **Mandatory Assumption Disclosure Table is the first block** — all 8 Step 1 questions listed, with status (given / assumption / needs-data) for each
- [ ] **Step 1.7 domain disambiguation completed** if the product description had any ambiguous term (DMTA, CAR-T, platform, AI agent, etc.)
- [ ] **Story structure stated in the metadata block** and consistent throughout — no mid-deck narrative shift
- [ ] **Competitor analysis chapter present** at the position appropriate to the story structure (see `competitor_moat_check.md` position table)
- [ ] **Biotech subflow chapter present** if applicable, with depth matching product-type classification

### Data integrity

- [ ] **Every quantitative claim has one of three labels**: `[verified — source]`, `[assumption — basis]`, or `🔴 [needs-data]`
- [ ] **No unsourced precise numbers** anywhere in the deck (e.g., no "TAM $1,234B" without citation)
- [ ] **Data Citation Table is complete and at the end of the document** — slide / data point / source / status for every quantitative claim
- [ ] **Verified claims have real, specific sources** — "industry consensus" or "AI estimate" is not a source; if that is all you have, the claim is `[assumption]`

### Competitor analysis

- [ ] **Competitor list is complete** — existing direct, existing indirect, potential entrants, and status quo all included
- [ ] **No "we have no competitors" statement** anywhere in the deck
- [ ] **Big-incumbent capability table present** with at least the most relevant 2–3 players the investor will ask about
- [ ] **36-month moat check completed**, with weighted score calculated using Maybe = 0.5 weighting
- [ ] **Verdict acted on**:
  - If score ≥ 3.0: deck stopped, user told to reconsider product (not just slides)
  - If score 2.0–2.5: deck has explicit slide addressing each Y / Maybe with mitigation
  - If score ≤ 1.5: defensibility narrative leads with this strength

### Investor-specific

- [ ] **Ask slide is concrete** — round size, use of funds, milestones to next round, timeline. Not "we are raising a Series A" — specific.

---

## WARN

### Investor-pitch quality

- [ ] **Slide count matches duration** — roughly 1 slide per minute, with 1–2 buffer slides
- [ ] **Risk framing is appropriate for external audience** — risks are surfaced but presented with mitigation, not raw

### Anti-pattern self-check

- [ ] Walked all 10 general anti-patterns in `anti_patterns.md`
- [ ] Walked SaaS-specific anti-patterns if applicable (LTV/CAC, retention, customer concentration, ARR vs contracted revenue)
- [ ] Walked biotech-specific anti-patterns if applicable (Phase III risk, reimbursement assumptions, FTO gaps, COGS assumptions, academic-publication confusion)
- [ ] Anti-pattern Self-check Results section is at the bottom of the deck, with each item marked

### Language and presentation

- [ ] **Language matches Step 1.5** (Chinese / English / bilingual)
- [ ] **Technical terms preserved in English** even in Chinese drafts (CAC, LTV, ARR, NRR, 510(k), IND, BLA, FTO, SAFE, etc.)
- [ ] **No startup-jargon clichés** — "disrupt", "10x", "unicorn", "game-changer", "synergy" do not appear
- [ ] **Bilingual mode**: both versions present, with localization vs. literal-translation choice respected per Step 1

### Final delivery sanity check

- [ ] **The user knows what to do next** — message includes guidance on feeding to a pptx skill if they want slides, or iterating on content first
- [ ] **Notes for the user section** flags any concerns: needs-data items, assumption that should be verified, or moat-check verdicts that imply product-level conversation
- [ ] **File saved to working directory** with a clear filename
