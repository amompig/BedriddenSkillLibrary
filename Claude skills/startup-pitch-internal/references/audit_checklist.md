# Audit Checklist — startup-pitch-internal

Used by **two consumers**:
1. The skill itself, as Step 7 (final self-gate before delivery).
2. `output-supervisor`, as the canonical rule source when chain-triggered.

Items are grouped by severity: **CRITICAL** (any one failing → overall FAIL) vs **WARN** (only failing → overall WARN). Several CRITICAL rules are level-conditional — apply only the level identified in Step 1.6 (team / department / board / all-hands).

---

## CRITICAL（缺一個就 FAIL）

### Structural — applies to all levels

- [ ] **Mandatory Assumption Disclosure Table is the first block** — all 10 Step 1 questions listed, with status (given / assumption / needs-data) for each
- [ ] **Step 1.10 prior baseline resolved** — for board / department quarterly updates, prior plan and action items must be established or marked needs-data with explicit follow-up
- [ ] **Step 1.8 domain disambiguation completed** if the product description had any ambiguous term (DMTA, CAR-T, platform, AI agent, etc.)
- [ ] **Level (team / department / board / all-hands) explicitly stated** in metadata block
- [ ] **Level-specific template applied correctly** — per `level_design.md` and `markdown_template.md`

### Data integrity

- [ ] **Every quantitative claim has one of three labels**: `[verified — system + date]`, `[assumption — basis]`, or `🔴 [needs-data]`
- [ ] **Internal KPIs resolve to system sources** — CRM, financials, HR, product analytics, lab data — not to founder recall
- [ ] **No KPI without a timestamp** — board needs to know whether numbers are end-of-quarter, current, or projected
- [ ] **Plan numbers in vs-Plan tables are sourced** — last quarter's board materials, the operating plan, etc.
- [ ] **Data Citation Table is at the end of the document** — slide / data point / source / status for every quantitative claim

### Level-specific (apply only the matching level)

#### Team level
- [ ] Last period section present
- [ ] Blockers / dependencies section present
- [ ] This period goals section present
- [ ] KPI snapshot (3–5 headline numbers) present
- [ ] Action items section present

#### Department level
- [ ] KPI vs Target table present
- [ ] Cross-team dependencies section present
- [ ] Hiring status section present
- [ ] Budget vs plan section present
- [ ] Top risks section present

#### Board level
- [ ] **KPI vs Plan present** with full headline metrics
- [ ] **Top 3 wins / Top 3 misses** present, each miss with root cause
- [ ] **Surprises this quarter section** present
- [ ] **Every surprise tagged with moat re-check status** (Y / N + reason)
- [ ] **Moat re-check chapter present** if any surprise triggered re-check, OR if it is the annual board meeting
- [ ] **Capital state section** with cash position, burn vs plan, runway months
- [ ] **Risk register update** present
- [ ] **Decision items list present** with concrete proposed actions (not "discuss" / "explore")
- [ ] **Q+1 commitments** present
- [ ] **Runway vs moat-evolution time alignment** — is current runway ≥ time needed to evolve the weakest moat dimension to a defended state? If no, it must be flagged in the deck and surfaced as a decision item

#### All-hands level
- [ ] **Vision recap slide** present
- [ ] **Wins celebrated concretely** (project names, customer names, milestone names)
- [ ] **The one big thing slide** present
- [ ] **Challenges paired with response** — never just challenges
- [ ] **New people / promotions slide** present
- [ ] **Roadmap preview** present
- [ ] **Recognition / culture moment** present

### Internal-specific honesty rules

- [ ] **No whitewashing of misses** — exact numbers, root causes
- [ ] **No surprises without action plan** attached (board level)
- [ ] **No vague decision items** at board level — every decision item has owner + timing + predicted impact
- [ ] **No manufactured optimism** at all-hands

---

## WARN

### Anti-pattern self-check

- [ ] Walked all 8 internal-specific anti-patterns in `anti_patterns.md`
- [ ] Walked SaaS-specific anti-patterns if applicable
- [ ] Walked biotech-specific anti-patterns if applicable
- [ ] Walked relevant general anti-patterns (especially for strategy off-sites where market context is discussed)

### Board-level extras

- [ ] **Time allocation supports discussion** — the deck should leave 30–40% of meeting time for discussion, not consume the whole window with presentation

### All-hands extras

- [ ] **Q&A time allocated** (target 15 minutes)

### Language and presentation

- [ ] **Language matches Step 1.5** (Chinese / English / bilingual)
- [ ] **Technical terms preserved in English** (CAC, LTV, ARR, NRR, 510(k), IND, FTO, runway, burn)
- [ ] **No startup-jargon clichés** — "disrupt", "10x", "unicorn", "game-changer", "synergy"
- [ ] **Tone matches level** — working voice for team / dept; strategic for board; narrative for all-hands

### Final delivery sanity check

- [ ] **The user knows what to do next** — message includes guidance on whether the deck needs further data gathering before the meeting, any decisions that should be pre-aligned with key board members before the formal vote, etc.
- [ ] **Notes for the founder section** flags any concerns: needs-data items that should be resolved before the meeting, any moat-check verdicts that imply hard conversations, any decision items that may not have consensus
- [ ] **File saved to working directory** with a clear filename including period (e.g., `archbase-board-q1-2026.md`)
