# IC Memo Template — 11 Sections

The IC memo is the deliverable. This file is the canonical structure with per-section writing guidance.

## Top-of-memo header

Before §1, include a metadata block:

```markdown
# IC Memo — <Company Name>

| Field | Value |
|-------|-------|
| Author | (this skill, simulating tier-1 VC partner) |
| Date | YYYY-MM-DD |
| Stage | Pre-seed / Seed / Series A / Series B+ |
| Round size sought | $X (per pitch) |
| Domain | Biotech / SaaS / AI-ML / Hardware / General |
| Team size | N |
| Input mode | v1 single-file / v2 data room |
| Web search | invoked / OFFLINE (degraded) |
| Conviction | High / Medium / Low |
| **Recommendation** | **Pass / Continue diligence / Term sheet** |
```

If OFFLINE mode, add a prominent warning banner here:

> ⚠️ **OFFLINE MODE — degraded analysis.** Web search was not invoked. All competitor / market / founder claims marked `[OFFLINE — RECALL ONLY]` are based on training-time recall and may be outdated or wrong. Do NOT rely on this memo for final investment decisions.

---

## §1 Executive Summary + Recommendation (target: 200–300 words)

Single page. Lead with recommendation. Structure:

- **Recommendation** with conviction level (High / Medium / Low)
- **Three sentences** on what this company is and why it might (or might not) work
- **Three strengths** (one line each)
- **Three risks** (one line each)
- **Conditions to advance** if Continue diligence (e.g., "5 reference customer calls", "IP/FTO opinion", "top-3 customer concentration data")

Tone check: a busy partner reading only this section should know whether to spend more time. No filler.

---

## §2 Investment Thesis Fit (target: 200–400 words)

Does this company fit our fund's investment thesis? (Assume a generalist tier-1 VC fund unless context says otherwise.)

- Stated thesis fit: which fund themes / theses does this company touch?
- Strategic fit: portfolio adjacencies, network effects with existing portfolio, conflicts
- Pass-through fit: would this be a top-quartile candidate for our partners?
- Anti-fit signals: anything that makes this a structural mismatch for our fund

If using domain overlay (e.g., biotech), incorporate domain-specific thesis questions.

---

## §3 Team Assessment (target: 400–700 words; depth driven by team-size bracket)

Read `team_size_scaling.md` for bracket-specific focus. Always cover:

- **Founder-market fit**: does this team have the rare unfair advantage in this domain?
- **Track record**: prior outcomes, repeat founder pattern, exits
- **Key role coverage**: are CEO / CTO / VP Eng / VP Sales / Head of Product all present or planned? Which are gaps?
- **Single point of failure**: is the company too dependent on one person?
- **Hiring plan**: what roles need to be filled with this raise; is the budget realistic?

Verify founder claims (Step 3 item 6). If LinkedIn / public profile contradicts pitch claim, flag explicitly.

For biotech: also evaluate scientific advisory board, KOL relationships, principal investigators.

---

## §4 Market Analysis (target: 400–700 words)

**DO NOT trust the pitch's TAM number.** Recompute independently using Step 3 item 7 research.

- **TAM, SAM, SOM** with explicit methodology (top-down / bottom-up / analog)
- **Growth dynamics**: is this market growing, flat, or declining? Cite source.
- **Segmentation**: who exactly is the buyer / user? How segmented is the market?
- **Adjacent market opportunity**: realistic expansion paths (vs. fanciful TAM expansion claims)
- **Demand signals**: independent evidence demand exists at the price point claimed

If pitch's TAM is fundamentally inflated, say so directly. Pitches that claim "$80B market" for a $200M realistic opportunity are common; calling this out is the IC memo's job.

---

## §5 Product / Technology Critique (target: 300–600 words)

What is the actual product? Could it be built? Is the moat real?

- **Technical feasibility**: does the technical story hold? Anything that violates physics / math / current ML capability?
- **Build difficulty**: 12 months / 24 months / 5 years to feature parity for a competitor
- **Moat sources**: data flywheel / network effects / regulatory / IP / brand / switching cost — which are real here?
- **Open-source / research threat**: anything from Step 3 item 5 that could commoditize this in 12 months?
- **Domain-specific technical questions** (e.g., for biotech: clinical trial design, mechanism plausibility; for SaaS: architecture choices, scalability)

The 36-month moat test (from `startup-pitch-investor`'s `competitor_moat_check.md`) is a good external reference here, applied with investor skepticism rather than founder generosity.

---

## §6 Competitive Landscape (target: 600–1000 words)

Four-layer analysis. Each layer must be populated using Step 3 research items 3, 4, 5.

### Layer 1 — Large incumbents

Who could build this if they wanted to? List 3–5 with: market cap / employee count / strategic interest / signs of intent. For each: distance to entering this space (assets, distribution, motivation, organizational barriers).

### Layer 2 — Mid-size / specialist competitors

Public, private, or PE-owned mid-size players already in adjacent or overlapping space. List ≥5 with: rough size, focus area, what differentiates from this company, recent moves.

### Layer 3 — Early-stage / stealth competitors (raised <$5M)

The layer most often missing from founder-written competitive slides. List ≥5 with: stage, founder background, traction signals, why they might overtake. **This layer is a dealbreaker for many decks** — if 5+ stealth competitors exist, the "no real competition" framing is fatal.

### Layer 4 — Latest research / open-source

Recent papers (last 18 months) and active OSS projects. List ≥3 with: relevance, reproducibility, threat horizon. If a published paper achieves 90% of the proposed product's value, the moat erodes.

### Net competitive verdict

After 4-layer analysis: in 36 months, who wins? Default to "incumbent or open-source" unless the team has shown a structural reason otherwise. This skepticism is correct most of the time.

---

## §7 Traction & Unit Economics (target: 400–800 words; depth driven by stage)

Compare claimed traction against industry benchmarks (Step 3 item 8).

- **ARR / revenue**: real or contracted? Recent month run-rate vs. trailing-twelve-month? (Many "ARR" claims include ramping contracts.)
- **Growth rate**: does the curve match the headcount / capital intensity?
- **NRR / gross retention / logo retention**: if NRR cited but logo retention not, that hides churn. Demand both.
- **Unit economics**: ACV / GM / CAC / payback / LTV-to-CAC. Compare to stage-appropriate benchmarks.
- **Cohort retention**: does the early-cohort retention curve indicate product-market fit?
- **Concentration**: top-1 / top-3 customer share of ARR. Concentration above 25% is a Series A risk.

For pre-seed / seed: traction may be minimal; that's expected. Don't fake-FAIL the section just because numbers are early. Mark `[needs-research]` and rely on team / market / product depth.

---

## §8 Risk Matrix (target: 400–600 words)

Five categories, each with 2–4 specific risks (not generic platitudes):

1. **Technical risk**: can the product be built / scaled? Specific failure modes.
2. **Market risk**: is the market large enough? Will it grow? Will buyers actually buy?
3. **Team risk**: key-person dependency, execution gaps, founder conflict potential
4. **Regulatory risk**: FDA / GDPR / antitrust / sectoral compliance — specific to domain
5. **Financial risk**: runway gap, dilution at next round, valuation step-up risk, follow-on funding environment

Each risk gets a severity (High / Med / Low) and a mitigation status (mitigated / monitored / unmitigated).

---

## §9 Open Diligence Questions (target: 200–400 words)

Concrete questions to ask the founder before advancing. Group by category. Examples:

- "Provide top-3 customer ARR concentration as of last month"
- "Who at AWS RDS is on the founder's outreach list as a potential acqhire target?"
- "Has counsel completed an FTO scan against IBM and Oracle's database optimization patents?"

If the recommendation is **Continue diligence**, these are the conditions. If **Pass**, list them anyway as "what would change my mind."

---

## §10 Term Sheet Sketch & Valuation Reasoning (target: 300–600 words)

**Required for Continue diligence / Term sheet recommendations. Optional for Pass.**

Read `references/valuation_methodology.md`. Provide:

- **Valuation range** with explicit methodology (comparable transactions / DCF-lite / Berkus / scorecard — pick one or two and show work)
- **Comparable transactions table**: 3–5 recent deals (company / round / valuation / ARR or relevant metric / source)
- **Pre-money / post-money** preferred range
- **Round structure**: equity / SAFE / convertible; suggested option pool top-up
- **Key terms to negotiate**: liquidation preference, anti-dilution, board composition, pro-rata rights

Without `[verified]` source data on comparables, this section MUST mark every comparable `[training-recall — VERIFY]` and warn the partners that final valuation requires fresh diligence on comparables.

---

## §11 Final Recommendation + Conditions (target: 200–400 words)

Restate the recommendation from §1 with the full reasoning chain visible:

- **Recommendation**: Pass / Continue diligence / Term sheet
- **Conviction level**: High / Medium / Low
- **Why**: 3-sentence summary of the dominant reasoning
- **Conditions to advance** (if Continue / Term): list from §9
- **What would change my mind** (if Pass): the specific signals that would warrant revisiting

If the conviction is Low even with a positive recommendation, name the top reason for low conviction explicitly.

---

## Format requirements (apply throughout)

- Markdown sections use `## §N — <title>` heading style for top-level memo sections
- Tables for comparable transactions, competitor lists, risk matrix
- Every numeric claim carries a verification tag (per `verification_rules.md`)
- No bullet padding ("nice strong team", "good market") — every line earns its place
- Cite specific company names, paper titles, deal terms with sources or `[training-recall]` tags

## What NOT to include

- "Notes for the founder" section (breaks persona)
- Soft language like "the team should consider..." — IC memos don't speak to founders
- Hedging without specifics ("might be challenges in execution") — name the specific challenge
- Filler sections that don't earn their length toward the recommendation
