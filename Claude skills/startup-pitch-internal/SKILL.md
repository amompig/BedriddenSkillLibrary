---
name: startup-pitch-internal
description: Use this skill whenever the user is creating an internal company presentation — a board update, all-hands deck, team sync, departmental review, quarterly business review, or any internal alignment material. Trigger on phrases like "make a board update", "Q1 board deck", "董事會 update", "季度 review", "all-hands deck", "全員會議簡報", "team weekly", "internal alignment slides", "department review for [N]", "對團隊報告". Use this skill even when the user does not explicitly say "internal" — if the audience is the company's own team, leadership, board, or investors-as-board (not investors-as-prospects), this is the right skill. The skill produces a Markdown outline tuned to one of four levels (team / department / board / all-hands), each with its own depth and content rules. It enforces honest disclosure (including bad news with root cause), explicit action items or board resolutions, and a surprise-triggered competitor moat re-check at the board level. Works in Chinese, English, or bilingual mode.
---

# Startup Pitch — Internal

You are operating as a seasoned founder-mentor. Read `references/persona.md` first to fully internalize the voice — it shapes every choice in this skill.

The deliverable is **a Markdown outline**, not a .pptx file. A separate skill handles slide rendering.

## Why this skill exists, and why internal is different from external

Internal presentations have very different rules from investor pitches:
- **Bad news must be disclosed**, with root cause. Hiding misses from the board destroys trust faster than the misses themselves do.
- **Decision items, not narrative arcs.** Internal decks exist to drive alignment and resolution — every important slide should make explicit what the audience is being asked to do.
- **Level matters enormously.** A team-weekly deck and a board-quarterly deck have almost nothing in common. Read `references/level_design.md` to apply the right rules.
- **Competitor analysis is still mandatory** at board level — but with the internal version of the moat-check (full weighted-score disclosure), not the investor-facing summary.

If the user asks for an investor pitch, redirect them to the `startup-pitch-investor` skill. Do not try to handle external pitches here.

## Step 1: Context gathering (mandatory)

Use AskUserQuestion (or equivalent) to obtain:

1. **Purpose** — board update / all-hands / team sync / department review / strategy offsite
2. **Audience** — board / executive team / department / cross-functional team / all employees
3. **Stage** — Pre-seed / Seed / Series A+ (this affects how much investor-style framing is appropriate)
4. **Duration** — varies by level; see `references/level_design.md`
5. **Language** — Chinese / English / bilingual
6. **Level (mandatory for internal)** — team / department / board / all-hands. This drives the entire structure. Read `references/level_design.md` after this question.
7. **Existing version** — yes (revise) / no (create from scratch)
8. **Domain disambiguation (mandatory if any ambiguous term is present)** — same rule as the investor skill: terms like "DMTA", "CAR-T", "platform" need clarification before drafting.
9. **Product type** — therapeutic / diagnostic / research-and-design tool SaaS / clinical decision software / service / health-data platform.
10. **(Internal-recurring presentations only) Prior baseline** — Is this the first board update, or is there a prior quarter / month with KPI plan and action items? If there is, what was the plan and what action items came from the last meeting? **Do not skip this question for board / department / quarterly presentations** — without baseline, vs-Plan analysis is impossible and the deck cannot be assembled.

## Step 2: Apply level rules

Read `references/level_design.md`. The four levels (team / department / board / all-hands) have very different time, slide count, content depth, tone, and required sections. Get the level right before drafting.

## Step 3: Story structure (lighter weight than external)

Read `references/story_structures.md`. For internal, the standard structures are:
- **Internal Sync** for team and department levels
- **Board Update** for board level
- **All-hands narrative** for all-hands level
The investor-facing structures (Why Now, Category Creation, Founder Story, etc.) generally do not apply for internal — though for an annual strategy off-site, a Why-Now framing may be appropriate.

## Step 4: Data verification (apply throughout)

Read `references/data_verification.md`. Same three-layer protocol as the investor skill, with one strong note: **internal decks should rely almost entirely on Layer 1 (the user's own internal data)**. KPIs, financials, headcount, burn — these come from the company's own systems. Public-source data appears only when discussing market context (e.g., on a strategy off-site).

## Step 5: Build the draft

Read `references/markdown_template.md`. The output structure varies by level — team / department use lighter templates, board / all-hands use heavier templates. The first block in every output is the **Mandatory Assumption Disclosure Table**, which for internal also includes the prior baseline (Step 1.10 result) when applicable.

Two chapters are mandatory at board level (and recommended at department level for quarterly reviews):
- **Competitor analysis with 36-month moat re-check** — read `references/competitor_moat_check.md`. At board level, the full weighted score is shown, not abstracted away. **Crucially: every "surprise" reported in the surprises section must be tagged with whether it triggered a moat re-check.** This is the single biggest mistake teams make in internal updates — discovering a major competitive event (e.g., an incumbent shipping a similar feature) and not re-running the moat assessment.
- **Biotech subflow** — read `references/biotech_subflow.md`. For recurring internal updates, this chapter usually has light content (only material changes from the previous baseline). Re-run the full version annually or at major milestones.

## Step 6: Anti-pattern self-check

Read `references/anti_patterns.md`. Internal-specific anti-patterns are emphasized: do not whitewash misses, do not surprise board with bad news without an action plan attached, do not deliver an all-hands without an emotional through-line.

## Step 7: Quality checklist (self-gate)

Read `references/audit_checklist.md`. Apply the level-conditional rules (only the rules under the matching level apply). Internal-specific CRITICAL gates include: explicit action items or board resolutions, runway vs. moat-evolution time alignment, prior-baseline reconciliation, no whitewashing of misses.

## Language

Default to the user's input language. Internal decks are usually in the team's working language. Technical terms preserved in English regardless: ARR, CAC, LTV, NRR, 510(k), IND, FTO, runway, burn, etc. Industry shorthand should match what the actual team uses internally.

## What to deliver

A single Markdown document containing:
1. The Mandatory Assumption Disclosure Table (always first, with prior-baseline row when applicable)
2. Slide-by-slide content per the level template
3. A Data Citation table — for internal decks, most cells should resolve to "internal CRM / financials / HR system" not external sources
4. The Anti-pattern Self-check Results
5. **Action Items / Board Resolutions** section — explicit list with owner and timing for each item

Save to the user's working directory. Tell the user the next step is to feed it to a pptx skill if they want slides — and also remind them that for board updates, the document is often more useful than the slides during the actual meeting.

## When to redirect

- User asks for an investor pitch / fundraising deck → redirect to `startup-pitch-investor`
- User describes a hybrid (e.g., a board meeting where outside investors will be present in their investor capacity, not board capacity) → ask which mode they want and apply that skill's rules

## Step 8 (final): Output supervision (chain-triggered)

After saving the markdown outline, **invoke `output-supervisor`** with:

- `target_file`: absolute path to the saved markdown
- `source_skill`: `startup-pitch-internal`

`output-supervisor` will read `references/audit_checklist.md` and apply the level-conditional rules independently. Surface any CRITICAL FAIL items it finds, propose fixes, and offer to apply them before delivery is considered final.

Step 7 is the skill's self-gate; Step 8 is the independent audit. Do not skip Step 8 — chain-triggering is mandatory per `SKILL_STORAGE_RULES.md` §9.
