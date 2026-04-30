# Research Checklist — 8 Mandatory + 5 Extension

This file defines the research SOP. Step 3 of `SKILL.md` mandates all 8 items execute via web search. Step 4 allows up to 5 autonomous extension searches.

## Why this is mandatory (not advisory)

The IC memo's value is its **independent view** vs. what the pitch claims. If the skill only judges what the founder wrote down, it produces a surface-level review, not a real diligence memo. Every CRITICAL claim in the memo must have an independent source — that source comes from this checklist.

---

## The 8 mandatory items

### Item 1 — Recent same-stage funding rounds (≥5)

**Search target**: 5+ companies in this category that raised at the same stage (pre-seed / seed / Series A / etc.) in the **last 18 months**.

**Why**: establishes the actual funding environment for this category. If 5 similar companies raised at $30M post-money valuations, a $100M pitch valuation is misaligned. If only 2 raised in 18 months, the category is cold.

**Method**: web search "<category> Series <X> funding 2025" / "<category> seed round 2024-2025" / Crunchbase mentions / TechCrunch articles.

**Capture**: company name, round size, post-money (if known), date, lead investor, source URL.

**Severity**: CRITICAL.

### Item 2 — Recent exits AND failures (≥2 each)

**Search target**: 2+ recent exits (acquisition or IPO, last 5 years) AND 2+ failures (shutdown, asset sale, wind-down) in this category.

**Why**: exits anchor valuation. Failures anchor risk. Founders only show exits; the IC memo must show both.

**Method**: web search "<category> acquisition" / "<category> shutdown" / "<category> assets sold" / Pitchbook-equivalent free sources.

**Capture**: company, outcome (exit / failure), value (if disclosed), date, what killed them (for failures).

**Severity**: CRITICAL.

### Item 3 — Mid-size / specialist competitors (≥5)

**Search target**: 5+ existing public, private, or PE-owned companies in adjacent or overlapping space — NOT large incumbents, NOT stealth.

**Why**: this is the "actually competing" tier. Founders often skip it because it dilutes their narrative.

**Method**: web search "<category> companies" / "<category> alternatives to <X>" / G2 / Capterra / industry analyst lists.

**Capture**: company name, focus, rough size, year founded, source URL.

**Severity**: CRITICAL.

### Item 4 — Early-stage / stealth competitors raised <$5M (≥5)

**Search target**: 5+ early-stage companies (pre-seed / seed) in this category, ideally raised <$5M.

**Why**: this is the layer that kills "no real competition" framing. If 5 stealth competitors exist, the founder's moat is weaker than claimed.

**Method**: web search "<category> stealth startups" / "<category> seed round 2024" / YC / Techstars / Pioneer / academic spinouts / GitHub trending.

**Capture**: company name, founder background (if discoverable), traction signal, source.

**Severity**: CRITICAL.

### Item 5 — Latest research / open-source (≥3, last 18 months)

**Search target**: 3+ recent research papers (arxiv / journals) and/or active open-source projects relevant to the technical core.

**Why**: a paper achieving 90% of the product's claim erodes the moat. An OSS project with 5K stars accelerates commoditization.

**Method**: web search "<technical-claim> arxiv" / "<technical-claim> github" / Google Scholar last 18 months. For biotech: chain `biomedical-lit-search`. For arxiv-heavy AI / ML: chain `alphaxiv-paper-lookup`.

**Capture**: paper or project, year, key result, threat assessment (commoditization risk High / Med / Low).

**Severity**: CRITICAL.

### Item 6 — Founder + key-member background verification

**Search target**: verify all named founder / executive claims in the pitch. LinkedIn, prior company press releases, conference talks, GitHub.

**Why**: founder claims are often inflated ("ex-FAANG" when actually 6-month internship). Verification is non-negotiable.

**Method**: name + company web search; LinkedIn check (if accessible); GitHub for engineers; conference / paper byline checks.

**Capture**: each named person, claim from pitch, verified status (matches / partial / contradicted / unverifiable). Flag any contradictions explicitly in §3 of the memo.

**Severity**: CRITICAL.

### Item 7 — Independent market sizing

**Search target**: market size data from sources OTHER than what the pitch cites.

**Why**: pitches cite favorable analyst reports. Cross-referencing with 2–3 other sources reveals overstated TAMs.

**Method**: web search "<category> market size <year>" / Gartner / IDC / academic estimates / government statistics / industry trade associations.

**Capture**: source, claimed size, methodology, year. Flag in §4 if pitch's TAM is >2x the median of independent sources.

**Severity**: CRITICAL.

### Item 8 — Industry benchmarks at stage

**Search target**: median / typical performance benchmarks for this stage (pre-seed / seed / Series A / B+) in this domain — NRR, GM, CAC payback, ARR growth, burn multiple, etc.

**Why**: §7 needs benchmarks to compare against. "130% NRR" is great or terrible depending on stage and category.

**Method**: web search "<domain> SaaS benchmarks Series A" / Bessemer Cloud Index / Iconiq Growth reports / OpenView SaaS metrics / a16z fintech metrics / etc.

**Capture**: metric, median value at stage, source.

**Severity**: WARN (lower than 1–7 because training-recall is more reliable here than for specific companies).

---

## Item completion checklist

Before writing the memo, confirm each item:

```
[ ] Item 1 — Funding rounds: N companies captured (≥5 required)
[ ] Item 2 — Exits / failures: N exits + N failures captured (≥2 each)
[ ] Item 3 — Mid-size competitors: N captured (≥5 required)
[ ] Item 4 — Early-stage competitors: N captured (≥5 required)
[ ] Item 5 — Research / OSS: N captured (≥3 required)
[ ] Item 6 — Founder verification: N people checked
[ ] Item 7 — Independent market sizing: N sources cross-referenced
[ ] Item 8 — Industry benchmarks: N metrics captured
```

If any CRITICAL item under-delivers (fewer than required), **note this prominently in the memo header** as "incomplete diligence — Item N partial; conviction reduced".

---

## Step 4 — Autonomous extension (5-search budget)

After completing the 8 mandatory items, you may run up to 5 additional web searches for following anomalies discovered during Step 3:

- "Item 1 surfaced a competitor that just raised $100M — search for context"
- "Item 4 surfaced a stealth competitor with concerning Y Combinator pedigree — verify"
- "Founder claim 'led Aurora optimizer' surfaced as ambiguous in Item 6 — try to verify via specific GitHub commits or AWS press"

**Hard cap = 5**. After 5, mark remaining anomalies as `[needs-research]` and move on. Do not exceed.

Track extension searches:

```
Extension search 1: <query> — outcome
Extension search 2: <query> — outcome
...
```

Include this audit trail in a memo appendix titled "Research Trail (extension searches)".

---

## Offline mode (degraded)

If web search is unavailable (tool error, sandbox restriction, user request):

### Step 1 — Issue a prominent warning at memo top

```markdown
> ⚠️ **OFFLINE MODE — degraded analysis.** Web search was not invoked. All competitor / market / founder claims marked `[OFFLINE — RECALL ONLY]` are based on training-time recall and may be outdated, missing recent companies, or wrong about specific deals. **Do NOT rely on this memo for final investment decisions.** Re-run with web search enabled for production use.
```

### Step 2 — Adjust expectations per item

| Item | Offline behavior |
|------|-------------------|
| 1 — Funding rounds | List recalled rounds with `[OFFLINE — RECALL ONLY]`; expect to miss last 6 months entirely |
| 2 — Exits / failures | Same; especially weak for failures (less press coverage) |
| 3 — Mid-size competitors | Reasonable from training data; tag all `[OFFLINE — RECALL ONLY]` |
| 4 — Early-stage / stealth | **Severely degraded** — training data rarely surfaces stealth. Note this gap explicitly. |
| 5 — Research / OSS | Reasonable for training-cutoff papers; tag explicitly |
| 6 — Founder verification | **Cannot verify**. Mark all named-founder claims `[needs-research]` and call this out in §3. |
| 7 — Independent market sizing | Tag all sources `[OFFLINE — RECALL ONLY]` |
| 8 — Industry benchmarks | Most reliable in offline mode (relatively stable over time); still tag |

### Step 3 — Limit conviction

Maximum conviction in offline mode: **Medium**. Never write "Conviction: High" without web verification.

### Step 4 — Recommend re-run

In §11, end with: "This memo was produced in OFFLINE mode. Before any IC discussion, re-run with web search enabled to fill `[needs-research]` and verify `[OFFLINE — RECALL ONLY]` claims."
