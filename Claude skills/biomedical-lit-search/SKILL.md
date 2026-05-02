---
name: biomedical-lit-search
description: Use whenever the user wants to search, build, or audit a biomedical / clinical / AI-medical literature landscape — finding peer-reviewed papers, building a Part A reference table for a research proposal, or verifying citation IDs. Trigger on phrases like "find papers on", "literature review", "PubMed search", "arXiv search", "Google Scholar", "build a literature landscape", "shape a reference table", "lit review", "盤點文獻", "文獻搜尋", "文獻表格", "查論文", "建立 Part A", "做一輪 lit review", "文獻地圖". Enforces verification tags ([UNVERIFIED] / [TRAINING-RECALL] / [SEMINAL]), time-window policy, geographic differentiation Region column, and the rule that every cited paper must justify a downstream candidate topic. Do NOT trigger for: non-biomedical literature (legal, financial, general academic); factual questions where citations are nice-to-have but not the deliverable; consumer health Q&A; news searches.
---

# Biomedical Literature Search Protocol

This skill governs how literature is searched, verified, and presented when building a research-proposal landscape — typically Part A of a research-ideation document.

## When to use
- User asks to search, review, summarize, or build a landscape of biomedical / clinical / AI-medical literature
- User is building Part A of a research proposal (literature table)
- User wants to audit existing citations for verification

## Step 1: Determine search source priority
Read `references/search_sources.md`. Different question types favor different databases (PubMed for clinical, arXiv for ML methods, Scholar for breadth). Pick the right source(s) before searching.

## Step 2: Apply verification protocol throughout
Read `references/verification_tags.md`. Every citation must carry exactly one tag: no-tag (verified) / `[UNVERIFIED]` / `[TRAINING-RECALL — user to verify]` / `[SEMINAL]`. Time window is 5 years primary, 10 years allowed for `[SEMINAL]` works. If web search tools are unavailable, mark ALL citations `[TRAINING-RECALL]` and disclose at top of output.

## Step 3: Apply geographic differentiation
Read `references/geographic_and_quality.md`. Part A's table MUST include a Region column (TW / Asia / US / EU / Other). This enables novelty triangulation — distinguishing "globally novel" from "novel in Taiwan only" — which directly affects downstream funding-fit evaluation.

## Step 4: Quality-tag and couple to downstream candidates
Read `references/output_coupling.md`. Note when papers report only technical AUROC without clinical utility. Every Part A reference MUST be cited in at least one Part D candidate's novelty section; if a paper does not justify any candidate, remove it from Part A.

## What to deliver
A literature table with columns: **Ref | Title | Venue | DOI/PMID/arXiv | Region | Finding | Gap**. Every row carries a verification tag. Top of output declares whether web search was invoked.

## Negative constraints
- Do not cite without a verification tag.
- Do not pad Part A with references unrelated to candidates.
- Do not use bare URLs as citations — extract DOI / PMID / arXiv ID.
- Do not conflate preprint with peer-reviewed status — flag preprints explicitly in the Venue column.
- Do not cite Wikipedia, news articles, or marketing pages as primary references for clinical claims.

## Step 5 (final): Output supervision (chain-triggered)

After producing the literature table, **save it to a markdown file** in the user's working directory (if it isn't already), then **invoke `output-supervisor`** with:

- `target_file`: absolute path to the saved markdown
- `source_skill`: `biomedical-lit-search`

`output-supervisor` will read `references/audit_checklist.md` and independently verify column completeness, verification tags, region coverage, citation hygiene, and downstream coupling. Surface any CRITICAL FAIL items, propose fixes, and offer to apply them before delivery is final. Per `SKILL_STORAGE_RULES.md` §9, this step is mandatory.
