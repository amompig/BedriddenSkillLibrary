# Anti-Pattern Library

Walk this checklist before delivering the deck. Each entry is a real failure mode observed in actual investor diligence rejections or post-mortem analyses of failed startups.

The point of this library is not to memorize "rules to avoid" — it is to develop the reflex that recognizes these patterns when they appear in your own draft.

## General anti-patterns

### 1. "We have no competitors"

**Trigger**: Slide says or implies that no one else solves this problem.
**Why it fails**: It signals lack of market awareness. Even if no direct competitor exists, status quo (Excel, manual processes, internal tools) is always a competitor.
**Fix**: Always include the status quo as part of the competitor list. Frame the deck position as "compared to the status quo of [doing this in spreadsheets / using consultants / building it internally], we provide..."

### 2. Over-large TAM

**Trigger**: TAM is sized by taking a huge market and multiplying by a small percentage. Example: "Global healthcare market is $8 trillion, we'll capture 0.01%."
**Why it fails**: It is not a TAM, it is a fantasy. Investors cannot diligence a number that has no bottom-up basis.
**Fix**: Use SOM (serviceable obtainable market) with explicit adoption-rate logic. "Of the ~2,500 mid-size biotech R&D groups in North America, we believe we can reach 50–100 within 24 months based on [analogue company]'s sales velocity at similar stage."

### 3. Hockey-stick projection without unit economics backup

**Trigger**: Five-year revenue projection going from $0 to $100M with no driver model.
**Why it fails**: Investors immediately ask "what assumptions about CAC, conversion rate, sales cycle, retention drive this?" — and if you cannot answer, the projection collapses.
**Fix**: If you must show projections, include a driver-model appendix. If you cannot defend the unit economics, do not show the projection.

### 4. Missing Why Now

**Trigger**: Pitch presents a problem and a solution but does not address "why this opportunity now and not 5 years ago / 5 years from now."
**Why it fails**: Most products fail not because they are bad ideas but because the market was not ready. Investors price in market timing heavily.
**Fix**: Even if Why Now is not the lead structure, include 1–2 sentences explaining why this product is appropriate to this moment. Cite a verified industry shift.

### 5. Generic team slide

**Trigger**: Team slide lists "Ex-Google / Ex-Stanford / Ex-McKinsey" without explaining what specifically each person contributed and what specifically each will contribute now.
**Why it fails**: Pedigree is shorthand; it does not substitute for relevant-experience evidence.
**Fix**: For each founder/key team member, write one specific accomplishment and one specific reason they are right for this venture. If "ex-Google" is on the slide, it should be "ex-Google search ranking team, shipped feature X used by Y users."

### 6. Bottom-up TAM ignoring adoption curve

**Trigger**: TAM assumes 100% market penetration. "There are 10,000 hospitals × $50K average contract = $500M TAM."
**Why it fails**: No product reaches 100% penetration. Investors expect adoption curves.
**Fix**: Apply realistic penetration estimates, and cite an analogue company's penetration trajectory at similar stage.

### 7. Feature-as-problem

**Trigger**: Problem slide says something like "users do not have an AI assistant" — that is not a problem, it is the absence of a feature.
**Why it fails**: A real problem has a measurable cost (time, money, opportunity). Without that, the solution sounds like a feature looking for a use case.
**Fix**: Restate the problem with cost. "Medicinal chemists waste 4-6 weeks per DMTA cycle on manual data integration across 4+ tools."

### 8. Demo without traction

**Trigger**: Pitch shows a polished demo but has zero paying customers or design partners.
**Why it fails**: A demo proves you can build the thing; traction proves someone wants the thing. Investors fund the second.
**Fix**: If traction is light, be explicit: "We are pre-revenue with 3 design partners under LOI. Goal: 1 paid pilot by end of next quarter." Honest framing beats inflated claims.

### 9. "First mover" without explanation of why incumbents have not done this

**Trigger**: Claim of being the first mover in a space, without explaining the market structure that prevented incumbents from acting earlier.
**Why it fails**: Investors immediately ask "if this is so good, why hasn't [Schrödinger / Pfizer / Salesforce] done it?" If the answer is silence, the deck loses.
**Fix**: Include a sentence on the structural reason — incumbent cannibalization risk, regulatory licensing they lack, organizational inertia, technology that only became feasible recently.

### 10. Five-year financial projection with false precision

**Trigger**: Revenue projection out to year five with figures precise to the thousand-dollar level.
**Why it fails**: No one believes that level of precision at that horizon. The false precision destroys credibility for the early-year numbers, which investors might have believed.
**Fix**: Use ranges for outer years (e.g., "Year 5: $X–Y million revenue depending on enterprise penetration"). Reserve precision for years 1–2.

## SaaS-specific anti-patterns

- **Unrealistic LTV/CAC ratio (e.g., >10x) without disclosing churn** — high LTV usually masks low retention; investors will ask
- **No retention curve** — retention is the lifeblood metric for SaaS; absence is itself a red flag
- **High customer concentration without disclosure** — if any single customer is >30% of ARR, disclose it
- **Conflating ARR with contracted revenue** — ARR should reflect annualized recurring revenue from active subscriptions; contracted revenue includes one-time and may include future-period bookings

## Biotech-specific anti-patterns

- **Skipping over Phase III risk** — Phase II → Phase III success rate is roughly 50%. A pitch treating Phase II success as "almost approval" is naïve
- **Assuming reimbursement with no payer engagement** — claims that Medicare or commercial payers will cover the product without any dialogue with payers
- **Patent claims that do not actually block competitors** — narrow claims or FTO gaps that are hidden rather than acknowledged
- **COGS pegged to specialty-drug pricing without therapeutic equivalence argument** — using a high price assumption derived from a different mechanism's pricing
- **Treating an academic publication as commercial validation** — peer-reviewed proof-of-concept does not equal commercial readiness; the gap should be explicit
