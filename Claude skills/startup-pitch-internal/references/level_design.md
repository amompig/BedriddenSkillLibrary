# Level Design — The Four Internal Levels

Internal communication has four levels with materially different rules. Get this right before drafting; the wrong level produces a useless deck.

## Quick reference

| Level | Audience | Cadence | Time | Slides | Story structure | Required sections |
|-------|----------|---------|------|--------|----------------|-------------------|
| **Team** | Direct team | Weekly / biweekly | 15–30 min | 5–10 | Internal Sync | Last period, blockers, this period, KPI snapshot |
| **Department** | Department + cross-functional partners | Monthly / quarterly | 30–60 min | 10–15 | Internal Sync (extended) | KPI vs target, dependencies, hiring, top risks, budget |
| **Board** | Board of directors | Quarterly | 60–120 min | 15–25 | Board Update | KPI vs Plan, wins/misses, surprises, moat re-check, capital, decisions |
| **All-hands** | All employees | Quarterly / half-yearly | 30–60 min | 10–15 | All-hands narrative | Vision recap, wins, challenges-with-response, roadmap, Q&A |

## Level 1: Team (weekly / biweekly)

**Purpose**: Coordination and unblocking. Not strategy.

**Required content**:
- What shipped / completed since last sync
- Blockers and what is needed to unblock them
- This week's / period's goals
- KPI snapshot (just the headline 3–5 numbers)
- Cross-team dependencies — what is the team waiting on / blocking

**Tone**: Working, can use jargon, can have implementation detail.

**Things to avoid**:
- Long narrative arcs (waste of time at this level)
- Strategic discussion (this belongs at department or higher)
- Detailed competitive analysis (irrelevant here)

**Surprises**: Mention briefly if relevant to the team's work; do not run a moat re-check at this level.

## Level 2: Department (monthly / quarterly)

**Purpose**: Coordination across functions, hiring and budget visibility, surfacing risks.

**Required content**:
- KPIs vs target (the department's core metrics)
- Cross-team dependencies and where they are stuck
- Hiring status (open roles, in-flight, recently filled)
- Budget burn vs plan
- Top 3–5 risks the department is tracking

**Tone**: Working voice with strategic awareness. Some narrative is appropriate, but the deck should still be operational.

**Things to avoid**:
- Trying to be a board update (too much strategic framing)
- Trying to be all-hands (too much motivational content)

**Surprises**: For quarterly department reviews, include a "surprises this quarter" section. For monthly, mention if relevant.

**Moat re-check**: Optional at this level. If a competitive surprise occurred, flag it for the next board meeting; the department review is the right place to flag it but not always the right place to run the full re-check.

## Level 3: Board (quarterly)

**Purpose**: Drive decisions, surface risk to the people with capital authority, align on strategy.

**Required content** — every item below is mandatory:
- **KPI vs Plan**: full headline metrics, with status colors and Δ
- **Top 3 wins**: the most material accomplishments
- **Top 3 misses**: direct, with root cause for each — no whitewashing
- **Surprises this quarter**: events not anticipated at last quarter's plan. For each surprise, tag whether it triggered a moat re-check.
- **36-month moat re-check** if any surprise relates to the competitive or technology landscape. The full weighted score must appear, not abstracted.
- **Strategy adjustments**: how the response to misses and surprises shapes the next quarter's priorities
- **Capital state**: cash position, burn rate, runway months. Compare to plan.
- **Risk register**: top 3–5 risks across technical / talent / budget / market dimensions
- **Decision items for the board**: explicit list, each with proposed action and what is being asked of the board
- **Q+1 commitments**: 3–5 specific deliverables for next board meeting

**Tone**: Strategic. Operational detail goes in the appendix or in pre-reading materials.

**Things to avoid**:
- Pretty-printing misses ("we are slightly behind on partnerships" is whitewashing if the actual number is -40%)
- Surprises without an action plan attached
- Decision items that are vague ("explore options for X" is not a decision item — "approve $120K capex for X" is)
- Pre-loading the board with detail and leaving no time for discussion

**The "surprise → moat re-check" rule**: Every surprise reported must have a tag indicating whether it triggered a moat re-check. If yes, the re-check appears in the deck. If no, the reason should be brief but explicit. Do not let surprises escape this discipline — the typical failure mode is reporting a competitive surprise and not connecting it back to the moat-check framework.

## Level 4: All-hands (quarterly / half-yearly)

**Purpose**: Build shared understanding, renew purpose, recognize people.

**Required content**:
- Vision recap (one slide is enough — do not lecture)
- Quarter wins (2–3 slides — concrete, with names and projects)
- Numbers overview (one slide, high-level, with context)
- The one big thing (one slide on the most important development of the quarter)
- Challenges with response (1–2 slides — never just challenges, always paired with what is being done)
- New people / promotions (one slide — humanize)
- Roadmap preview (1–2 slides — what is next)
- Recognition / culture moment (one slide — a story that reinforces values)
- Q&A (target 15 minutes)

**Tone**: Narrative and motivational, but not vacuous. The team can detect manufactured optimism.

**Things to avoid**:
- Bad news without an action plan (this is the worst all-hands failure mode — do not surprise the team with a major problem and then leave them with no idea what is being done)
- Manufactured optimism (cheerleading without substance creates cynicism)
- Too much detail (this is not a department review)
- No Q&A (the team needs to feel heard)

**Surprises**: Discuss only if they materially affect the team's work or morale. Otherwise leave for board / department levels.

**Moat re-check**: Do not run at this level. If competitive landscape has shifted, the all-hands message should focus on "here is what we are doing about it" — the analysis itself belongs at the board level.

## Cross-level rule: cadence of mandatory chapters

The competitor moat-check and biotech subflow chapters from `competitor_moat_check.md` and `biotech_subflow.md` are not run at every level. The cadence:

| Level | Moat re-check cadence | Biotech subflow cadence |
|-------|----------------------|-------------------------|
| Team weekly | Never | Never |
| Department monthly | Never | Never |
| Department quarterly | Optional, flag for board | Light update if changes |
| Board quarterly | Required if any surprise touches competition / technology | Light update; full annually |
| Board annual | Required (full re-check regardless of surprises) | Full re-disclosure |
| All-hands | Never | Never |

Running the full chapters at every level produces fatigue and dilutes the impact when something has actually changed. Reserve the heavy machinery for the levels and moments that warrant it.
