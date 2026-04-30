# Verification Rules — Anti-Hallucination Protocol

This file defines the tagging system and the four hard rules. The IC memo's credibility depends entirely on these. A memo that hallucinates a specific company name + funding amount + deal terms is worse than no memo — it actively misleads.

## The three-tag system

Every numeric claim, specific company name, and founder claim in the memo MUST carry one of three tags:

### `[verified — <source URL or DOI>]`

Confirmed via web search or other primary source. Source must be specific enough to recheck.

✅ Good:
- `[verified — https://crunchbase.com/organization/snowflake]`
- `[verified — Tiger Global press release 2024-03-15, https://...]`
- `[verified — author's LinkedIn, retrieved 2026-04-29]`
- `[verified — Bessemer Cloud Index Q3 2025 report, https://...]`

❌ Not acceptable as `[verified]`:
- "industry consensus"
- "common knowledge"
- "AI estimate"
- "training data" (this is what `[training-recall]` is for)
- "I'm pretty sure"

### `[training-recall — VERIFY]`

Likely true based on training data, but not confirmed via web search. The reader is expected to verify before relying on this claim. **Always include the `VERIFY` suffix** as a visual reminder.

✅ Good:
- `OtterTune was acquired by Intel in 2024 [training-recall — VERIFY]`
- `Snowflake reported NRR ~158% at peak [training-recall — VERIFY; check Snowflake S-1 / 10-K]`
- `pganalyze raised Series A [training-recall — VERIFY]`

❌ Not acceptable:
- Tagging without the `VERIFY` suffix
- Using `[training-recall]` for something the memo could have web-searched (Item 6 founder verification, for example)

### `[needs-research]`

Information that should exist but the skill could not find. Either the search didn't surface it or the data is genuinely scarce.

✅ Good:
- `Top-3 customer ARR concentration: [needs-research — pitch did not disclose]`
- `OtterTune wind-down specific date: [needs-research — only "2024" available]`
- `Founder's stated 8 years at AWS RDS: [needs-research — LinkedIn profile not accessible]`

`[needs-research]` is preferred over guessing. A memo with many `[needs-research]` items is more honest than a memo that fabricates details.

---

## The 4 anti-hallucination hard rules

Violating ANY of these rules = memo overall verdict CRITICAL FAIL.

### Hard Rule 1 — No fabricated company-+-amount-+-valuation-+-headcount combinations

A statement like:
> "Acme.ai raised a Series A of $20M at a $200M valuation in March 2024, with 35 employees"

contains 4 specific facts that all need to be true together. **The skill MUST NOT produce such a statement** unless:
- All 4 are `[verified]` from a single source, OR
- The entire claim is tagged `[training-recall — VERIFY]` (acknowledging unreliability)

Mixing tags across the same sentence is forbidden — confuses the reader about what's actually verified.

**Specific examples this rule prohibits**:
- Inventing a competitor with a specific headcount because "it sounds plausible"
- Combining a real company name with a guessed valuation
- Citing a "deal" that the skill is fairly sure happened but cannot find a source for

### Hard Rule 2 — No fabricated founder-specific backgrounds

Statements like:
> "Jane Doe was a staff engineer at Stripe from 2018–2022"

require the same treatment. **The skill MUST**:
- Web-verify via LinkedIn / press / GitHub (Item 6 of research checklist), OR
- Tag the entire sentence `[training-recall — VERIFY]`, OR
- Replace with `[needs-research]` if neither is possible

**This rule especially applies to**:
- Specific employer names + tenure
- Specific titles ("staff engineer" vs "engineer" — these matter)
- Specific accomplishments ("led the X project" vs "worked on X")
- Specific schools / degrees

If the pitch makes a claim about a founder, the IC memo's verification section may quote the pitch's claim with an explicit tag like:

> Pitch claims founder was "ex-AWS RDS Principal Engineer." `[needs-research — could not verify specific title via LinkedIn]`

### Hard Rule 3 — Valuation ranges MUST have comparable methodology

§10 of the memo (Term Sheet & Valuation) cannot give:
> "We propose a $30M–$50M post-money valuation."

Without:
- Naming the methodology (comparable transactions / DCF-lite / Berkus / scorecard)
- Showing the comparables table OR scoring rubric
- Tagging each comparable's valuation `[verified]` or `[training-recall — VERIFY]`

`valuation_methodology.md` provides the templates. Skipping this turns §10 into pure guess.

### Hard Rule 4 — Untagged numbers default to fabrication risk

Any number in the memo without a tag is, by default, a hallucination risk. The verification scan before delivery should:

1. Search the memo for numeric patterns: percentages, dollar amounts, employee counts, dates, multiples
2. For each, confirm it has one of the three tags
3. If not, either tag it or remove the claim

Specific cases that often slip:

| Pattern | Default treatment |
|---------|-------------------|
| Market size figures ("$X B market") | `[verified — source]` from Item 7 research, or `[training-recall — VERIFY]` |
| ARR / NRR claims about pitch's company | `[verified — internal financials]` if pitch shows them; `[needs-research]` if not |
| Competitor employee counts | `[verified — Crunchbase / LinkedIn / company website]` or `[training-recall — VERIFY]` |
| Industry benchmarks ("median NRR for SaaS Series A is 110%") | `[verified — Bessemer / Iconiq / source]` or `[training-recall — VERIFY]` |
| Comparable deal valuations | Per Hard Rule 1 |
| Time-to-market estimates ("they could ship in 18 months") | `[assumption — basis: ...]` permitted here; this is investor judgment, not external fact |

---

## Special case: the IC memo's own assumptions

Some claims in the memo are **the IC partner's own analytical assumptions**, not external facts. These are different from claims that should be verified.

Use `[assumption — basis: <reasoning>]` for these:

✅ Good examples:
- `If hyperscalers fail to ship within 18 months, this team gets a 24-month head start [assumption — basis: history of hyperscaler enterprise SaaS shipping cadence].`
- `Conviction Medium because team has founder-market fit but the GTM hire is unproven [assumption — basis: my synthesis of §3 + §6].`

These are clearly the partner's reasoning, not unsourced facts. The reader (other partners) understands these are interpretations.

❌ Misuse:
- `[assumption — basis: I think]` — empty
- Using `[assumption]` to dress up what should be `[needs-research]`

---

## Verification scan before delivery (mandatory)

Before saving the memo and triggering supervisor:

1. **Scan for untagged numbers** (use string search for `%`, `$`, year patterns, employee counts)
2. **Scan for untagged company names** that aren't already in the original pitch
3. **Scan for untagged founder claims** that aren't direct quotes from the pitch
4. **Verify §10 valuation has methodology** (Hard Rule 3)
5. **Verify the §1 conviction level** is consistent with the # of `[needs-research]` items in the memo

If any rule fails, fix before delivery. The output-supervisor will catch missed cases via `audit_checklist.md`, but the skill should self-fix first.
