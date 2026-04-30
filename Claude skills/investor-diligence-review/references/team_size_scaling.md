# Team Size Scaling

§3 Team Assessment in the IC memo adapts to the company's current team size. Different bracket → different focus, different diagnostic questions, different recommendations.

This file defines the four brackets and what to write for each.

---

## Bracket detection

Extract from pitch metadata. If headcount unclear, AskUserQuestion. Brackets:

| Bracket | Headcount | Typical stage |
|---------|-----------|---------------|
| **Solo / 1-2** | 1–2 people | Pre-seed (rarely seed) |
| **Early team** | 3–10 people | Pre-seed / Seed |
| **Scaling team** | 11–30 people | Seed / Series A |
| **Mature team** | 31–80 people | Series A / Series B |

>80 people is typically Series B+ scale and outside this skill's scope (memo format diverges from VC IC into PE / growth memo).

---

## Bracket 1: Solo / 1-2 (1–2 people)

### What §3 Team should focus on

The single biggest risk is **founder concentration**. Everything depends on this person not getting hit by a bus, not burning out, and shipping faster than competitors. The memo's §3 must:

- **Founder-market fit narrative** (300w): why does this exact person own this exact problem? What unfair advantage do they have?
- **Single point of failure analysis**: if founder is unavailable for 4 weeks, what stops? What happens to customer commitments, hiring, fundraising?
- **First 3 hires plan** (with budget): name the roles. Verify the budget covers them. Is there a co-founder gap (technical / commercial)?
- **Founder track record**: prior outcomes, repeat-founder pattern, public artifacts (papers / shipped products / talks)

### Diagnostic questions to surface in §9 Open Questions

- "Is there a co-founder agreement in place if a co-founder is intended but not yet hired?"
- "What is the burnout / continuity plan?"
- "Has the founder taken any equity dilution actions (e.g., advisor pool, friends-and-family) that affect the cap table?"
- "What's the founder's runway vs. company runway? (Personal financial position)"

### Common pitfalls at this bracket

- Founder optimistic about hiring velocity (typical underestimate by 2x)
- "I'll hire a CTO with the round" — verify the CTO candidate is in pipeline now, not aspirational
- "Co-founder" listed but actually advisor or part-time

### Recommendation modifiers

At this bracket:
- **Strong recommend** is rare. Default ceiling is **Continue diligence with conditions** unless founder track record is exceptional.
- If founder is first-time and solo, conviction ceiling is **Medium** regardless of recommendation.

---

## Bracket 2: Early team (3–10 people)

### What §3 Team should focus on

The team has formed but not yet specialized. The memo's §3 should evaluate:

- **Founder dynamics**: is there role clarity (CEO / CTO / etc.)? Have they worked together before? Conflict risk?
- **Key role coverage**: at 3–10, the team typically has CEO + CTO + 1–2 senior engineers. Missing critical roles?
  - For SaaS: missing product / GTM lead (will need to hire ASAP)
  - For biotech: missing regulatory / clinical lead
  - For hardware: missing manufacturing / supply chain lead
  - For AI / ML: missing applied ML engineer (separate from research scientist)
- **Hiring gaps for next 12 months**: what 3–5 hires are critical with the round? Is the org plan realistic?
- **Equity distribution**: are co-founders aligned (no significant imbalance)? Is the option pool sized appropriately for next 18 months?

### Diagnostic questions

- "What's the option pool today? What does the round require?"
- "Has any co-founder departed? Why? What was the equity treatment?"
- "What hire is the founder most worried about closing? Why?"

### Common pitfalls

- "Solo CEO with 5 engineers" — usually a missing co-founder gap
- "All eng, no GTM" — fine at pre-seed, problematic by Series A
- Founders haven't done annual review / 1:1 cadence — culture warning sign

### Recommendation modifiers

- Conviction can reach **High** at this bracket if team gaps are minor and product is shipping.
- Watch for **founder fatigue** signals — if the team has been at this 4+ years pre-seed/seed, may be losing momentum.

---

## Bracket 3: Scaling team (11–30 people)

### What §3 Team should focus on

The company has formed functions but not yet professional managers. Critical evaluation:

- **Function leadership coverage**: VP Eng / VP Sales / VP Marketing / VP Product — who's in each seat? Are any of these "founder doing two jobs"?
- **Manager-to-IC ratio**: at 20+ headcount, you should see 3–4 managers. If founders manage 15 people directly, scaling will break.
- **Hiring velocity vs. burn**: are they hiring fast enough to deploy capital? Too fast (poor ROI per head)?
- **First non-founder hire of consequence**: who was it? Did they stay? What's the founder's track record of attracting and keeping senior talent?
- **Sales motion proof**: has anyone other than the founder closed a deal? At Series A, this matters enormously.

### Diagnostic questions

- "Who's the most recent VP-level hire and what was the search process?"
- "What's regrettable attrition rate (target: <10% annual)?"
- "What roles are open today and how long have they been open?"
- "Does the founder still lead sales calls? At what ARR level should that change?"

### Common pitfalls

- "Founder as VP Sales" past $2M ARR — scaling cliff
- VP Eng who's actually senior engineer with title bump — distinguishable in 1:1 conversation
- High burn from over-hiring before product-market fit confirmed

### Recommendation modifiers

- This is the bracket where **GTM credibility** matters most. If the team can't articulate sales motion concretely, that's a major flag.
- For SaaS at this bracket: demand named accounts won by non-founder reps.
- For biotech at this bracket: demand named PIs running trials, not just the SAB.

---

## Bracket 4: Mature team (31–80 people)

### What §3 Team should focus on

By this size, the team should have professional functions. The memo's §3 should be:

- **C-suite completeness**: CEO / CTO / CFO / CRO / COO — gaps and how they affect execution
- **Department leadership depth**: 2-deep in critical functions (especially Eng and Sales)
- **OKR / performance system**: does the company run a real performance cadence? (If not, scaling will be chaotic.)
- **Hiring cadence**: how many hires last 12 months? Quality bar held?
- **Retention metrics**: voluntary attrition, especially regrettable; eng tenure curve
- **Diversity of experience**: too monoculture (e.g., all ex-FAANG) is a red flag for execution complexity

### Diagnostic questions

- "What's the hiring funnel like at IC level — how many candidates per hire?"
- "Has the company done a layoff? When? What was the criteria?"
- "Who is the company's most senior IC (not manager)? What role do they play in technical decisions?"
- "What % of leadership is internal-promote vs. external-hire?"

### Common pitfalls

- CEO has not transitioned out of doing IC work (often founder still writing code)
- CFO is title bump from accountant — not a strategic CFO
- VP Sales hired from much smaller company (downshift talent risk)

### Recommendation modifiers

- At this bracket, the memo's §7 (Traction & Unit Econ) should dominate over §3. If team is good but unit econ is broken, no amount of team praise saves the deal.
- Conviction ceiling = **High** if team is professional and unit econ is strong; **Low** if team is professional but unit econ weak (the "execution is fine but the business doesn't work" pattern).

---

## Cross-bracket: founder transition risk

A specific risk that can apply at any bracket:

- **Bracket 2→3 transition**: founder must hire first managers. Many fail.
- **Bracket 3→4 transition**: founder must hire VP-level execs. Many fail here too.
- **Bracket 4→growth**: founder may need to bring in COO / professional CEO. Not all founders accept this.

If the IC memo is being written at the cusp of a transition (e.g., 28 headcount, fundraising to scale to 60), §3 should explicitly evaluate: "is this founder ready for the next bracket?" — using the diagnostic questions from the destination bracket.

---

## What §3 should NOT do at any bracket

- List every employee by name (memo is not a roster)
- Repeat the pitch's team slide verbatim (Hard Rule 2 — verify, don't repeat)
- Make team judgments based on demographic factors not relevant to execution
- Include personal-life information about founders unless directly relevant to execution risk (e.g., travel obligations, geographic dispersion)
