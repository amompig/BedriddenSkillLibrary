# Domain Sub-Flow

Five domain branches. Apply the matching one as an overlay throughout the memo. If the company spans domains (e.g., AI for biotech), pick the dominant capital-formation lens and note the secondary as a footnote.

## Domain detection

Read the pitch's product description. Match against the keywords / signals below. If ambiguous (multiple matches), ask the user via AskUserQuestion before proceeding — wrong domain = wrong diligence rubric = useless memo.

| Domain | Signals |
|--------|---------|
| **Biotech** | Therapeutic / diagnostic / device / clinical / drug / FDA / CE mark / 510(k) / IND / BLA / patient outcomes / hospital / lab / molecule / pathway / mechanism |
| **SaaS** | ARR / NRR / GM / CAC / cloud / multi-tenant / API / enterprise software / platform fee / seat-based pricing / DevTool / API SaaS |
| **AI / ML** | Foundation model / LLM / training data / inference / GPU / model weights / fine-tuning / agent / RAG / multimodal / open-source competition prominent |
| **Hardware / deep tech** | Physical product / manufacturing / BOM / supply chain / hardware iteration cycle / chips / robotics / energy / batteries / quantum / aerospace |
| **General** | Anything that doesn't cleanly fit the above (consumer apps, marketplaces, services, content, fintech-not-deep) |

If the pitch claims to be "AI for X" — primary domain depends on what dominates the cost structure and time-to-market. AI tooling for software developers → AI/ML. AI for drug discovery with wet lab → Biotech (with AI overlay).

---

## Biotech overlay

### Sub-routing within Biotech

Further classify into one of:

- **Therapeutic** (drug / molecule, FDA Phase I/II/III path)
- **Diagnostic** (Dx, 510(k) or PMA path)
- **Device** (medical device, 510(k) or PMA path)
- **Real-world SaaS / clinical decision software** (SaMD, lighter regulatory)

### §3 Team — biotech-specific questions

- Does the team have **clinical operations experience**? (PIs, CROs, regulatory affairs hires)
- **Scientific advisory board (SAB)** — KOL caliber, recent publications, conflicts
- **Wet lab vs dry lab balance** — appropriate for the technical claims?
- For therapeutics: regulatory / clinical / commercial leads — gaps?

### §4 Market — biotech-specific framing

- Patient population (prevalence × addressable × treated × adherent)
- Reimbursement landscape (coverage policies, expected payer behavior, comparable molecules' pricing)
- For therapeutics: market access timeline post-approval
- Avoid "$XB pharma market" framing — too coarse for IC memo

### §5 Product / Tech critique — biotech-specific

- **Mechanism plausibility**: does the claimed mechanism cohere with current literature?
- **Clinical trial design**: feasible patient enrollment? Meaningful endpoints? Power calculations?
- **Manufacturing feasibility**: CMC for therapeutics; reagent supply for diagnostics
- **IP / FTO**: any patent landscape that blocks freedom-to-operate?

### §6 Competition — biotech-specific

- ClinicalTrials.gov as a primary source for active competitors (search by indication + mechanism)
- FDA approval list / orange book for incumbents
- Big pharma pipeline disclosure as potential entrant signal
- Layer 4 (research): primary literature is heavier than for SaaS — expect 5–10 papers, not 3

### §7 Traction — biotech-specific

For pre-clinical: in vivo / in vitro data, IND-enabling status
For clinical: Phase I/II/III enrollment, endpoint hit rates, comparison to natural history or standard of care
For diagnostics / devices: clinical validation studies, sensitivity / specificity vs. competitor
**ARR is rare in biotech**; don't apply SaaS metrics blindly

### §8 Risk — biotech-specific

- Clinical risk: probability of phase advancement (Phase II → III is ~30% historically)
- Regulatory risk: 510(k) timeline / Pre-Sub / advisory committee dynamics
- Reimbursement risk: payer pushback specific to mechanism / cost
- IP / FTO risk: blocking patents, expiry timing of competitors
- Manufacturing risk: scale-up CMC, single-source reagent risk

### §10 Valuation — biotech-specific

- Risk-adjusted NPV (rNPV) often used for therapeutics
- Comparable transactions: prior similar-stage biotech rounds
- Diagnostics: revenue-multiple comparable transactions

---

## SaaS overlay

### §3 Team — SaaS-specific

- Eng:GTM ratio (typically 60:40 at Series A; flag if >75:25)
- VP Sales / VP Marketing — present or planned?
- Customer success function presence
- Key engineering: principal-level talent for the domain

### §4 Market — SaaS-specific

- Bottom-up sizing: ICP company count × ACV × penetration curve
- Avoid "global software market = $XB" framing — too coarse
- Segment by ICP: SMB / mid-market / enterprise have different unit econ

### §5 Product / Tech critique — SaaS-specific

- Time-to-value: install to first measurable value
- API / integration depth (for infra SaaS)
- Multi-tenant data isolation
- Open-source threat (especially for DevTool SaaS)

### §6 Competition — SaaS-specific

- G2 / Capterra / Gartner Magic Quadrant as competitor sources
- Hyperscalers as Layer 1 always (they bundle features over time)
- DevTool SaaS especially: GitHub OSS as Layer 4 (open-source projects with 1K+ stars are real threats)

### §7 Traction — SaaS-specific (the heart of SaaS IC memos)

| Metric | Stage benchmark (rough) |
|--------|-------------------------|
| ARR | Seed $0.5–2M; Series A $1–5M; Series B $5–20M |
| YoY growth | Series A: 200%+ ideal, 100% acceptable |
| NRR | Series A: 110% acceptable, 130%+ strong |
| Logo retention (gross) | Series A: 90%+ for SMB, 95%+ for enterprise |
| GM | Infra SaaS: 70–80%; App SaaS: 75–85% |
| CAC payback | Series A: <18 months ideal, <24 months acceptable |
| Magic Number | Series A: 0.7+ ideal, 0.4+ acceptable |
| Burn multiple | Series A: <2.0 ideal, <3.0 acceptable |

Demand all of these. If pitch only shows ARR + growth, that's a yellow flag — usually means the others aren't strong.

### §10 Valuation — SaaS-specific

- ARR multiples by stage and growth (~10–25x for high-growth Series A; ~5–15x for moderate)
- Comparable transactions: recent SaaS Series A rounds with comparable ARR/growth profile

---

## AI / ML overlay

### §3 Team — AI/ML-specific

- Research vs. applied ML balance — pure researchers struggle to ship product
- Founders' publication record (NeurIPS / ICML / ACL papers)
- Compute access: dedicated cluster, cloud credits, compute partner relationships

### §5 Product / Tech critique — AI/ML-specific

- **Model moat**: is the moat the model itself (often weak — replicated in 6–12 months) or the data / workflow?
- **Inference cost**: unit economics at scale; margin compression if compute costs drop
- **Open-source threat**: Llama / Mistral / Qwen / open weights eroding closed-model premium
- **Foundation-model dependency**: building on OpenAI / Anthropic API — what if pricing changes?

### §6 Competition — AI/ML-specific

- Layer 1 always includes OpenAI / Anthropic / Google / Meta
- Layer 4 (research) is critical: arxiv last 18 months frequently shows the technical claim is replicated. Chain `alphaxiv-paper-lookup` for any specific arxiv reference.
- Open-source projects on GitHub with notable stars are Layer 4 threats

### §7 Traction — AI/ML-specific

For applied AI products: SaaS-style metrics apply
For model / infrastructure: harder to measure — usage volume, cost-per-query, retention
For agent / autonomy products: often pre-revenue at seed; weight team and tech harder

### §10 Valuation — AI/ML-specific

- Volatile multiples — AI premium has compressed since 2024. Use recent (last 12 months) comparables only.
- "AI premium" is real but harder to defend in 2026 than in 2023

---

## Hardware / deep tech overlay

### §3 Team — Hardware-specific

- Hardware iteration experience (multiple revs shipped)
- Manufacturing relationships (contract manufacturer, fabrication partners)
- Supply chain expertise — increasingly critical post-2023

### §4 Market — Hardware-specific

- Unit production cost trajectory
- Capex implications for manufacturer / customer
- Often slower TAM growth than software but more defensible

### §5 Product / Tech critique — Hardware-specific

- BOM cost realism (founders often optimistic)
- Tooling / manufacturing scale-up cost
- Time to next rev (typically 12–24 months minimum)
- Failure modes specific to hardware (reliability, yield, certification)

### §7 Traction — Hardware-specific

- LOIs / signed pre-orders if pre-revenue
- Pilot customer outcomes
- Bills-of-materials cost trajectory
- Production volume reached vs. target

### §8 Risk — Hardware-specific

- Capital intensity → larger funding gaps between rounds
- Supply chain disruption risk
- Manufacturing partner concentration risk
- Certification timeline risk (FCC / CE / FDA depending on category)

### §10 Valuation — Hardware-specific

- Lower revenue multiples than SaaS (typically 2–5x)
- Asset-based components (machinery, IP) sometimes float valuation

---

## General fallback

When the company doesn't fit Biotech / SaaS / AI-ML / Hardware-deeptech, use the standard 11-section structure without overlay. Apply common-sense investor diligence:

- Team — track record, gaps, hire plan
- Market — demand evidence, competitive density, growth dynamics
- Product — feasibility, differentiation, time to value
- Competition — 4-layer analysis with whatever sources match the domain
- Traction — revenue / users / engagement / retention as available
- Risks — apply 5-category risk matrix without domain-specific bias

Do not force-fit a domain. A consumer app is not a SaaS deck, a marketplace is not an AI deck. If genuinely general, write the memo accordingly with explicit acknowledgment that domain-specific benchmarks (e.g., NRR) don't apply.
