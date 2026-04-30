# Biotech Sub-flow: IP / Regulatory / Reimbursement

This chapter is mandatory only when the company is in the biotech / health-tech space — but its depth depends on product type. The wrong move is treating every biotech-adjacent company as if it were developing a therapeutic.

## Step 1: Product type sub-routing

Before writing this chapter, classify the product type. Use the table below to decide depth.

| Product type | Examples | IP depth | Regulatory depth | Reimbursement depth |
|--------------|----------|----------|------------------|---------------------|
| **Therapeutic** | Small molecule, biologic, cell therapy, gene therapy | Full chapter | Full chapter (IND/NDA/BLA) | Full chapter (payer + coding) |
| **Diagnostic** | IVD, companion diagnostic, AI-based imaging device | Full chapter | Full chapter (510(k)/PMA/De Novo) | Full chapter (CPT application) |
| **Research / design tool SaaS** | DMTA platform, ELN, cheminformatics, lab automation software | Light (software IP only) | **N/A — short paragraph** unless 21 CFR Part 11 applies | **N/A — short paragraph** |
| **Clinical decision software (SaMD)** | CDS for clinicians, SaMD with treatment recommendation | Light (algorithm patents optional) | Full chapter (FDA SaMD/CDS rule) | Depends on integration target |
| **Service-based** | CRO, clinical network, contract research | Light | Depends on service type | Depends on service type |
| **Health-data platform** | RWE, patient registry, real-world data brokerage | Includes data-rights structure | Depends on HIPAA/GDPR/local privacy law | Depends on business model |

Confirm the classification with the user if there is any ambiguity. The wrong classification produces a chapter that either pads space with irrelevant content or under-discloses real risk.

## Depth definitions

- **Full chapter** — the three subsections below, each with detail
- **Light** — 50–150 words covering current status and main risk
- **N/A — short paragraph** — one or two sentences explaining why the chapter does not apply, plus any exception conditions (e.g., "We do not currently fall under FDA jurisdiction. If we add features supporting IND submissions, this changes — covered in 18-month roadmap")

Record the classification result in the Mandatory Assumption Disclosure Table at the top of the deck.

## Subsection 1 — IP (Intellectual Property)

### Full version covers:

- **Patent portfolio**: applications filed / granted / PCT / national-phase entries / abandoned. Include filing dates and inventor list.
- **FTO (Freedom to Operate)** analysis: whether competitor patents block our commercialization. If FTO has not been cleared by counsel, mark as `🔴 [needs-data — counsel review pending]`.
- **Patent landscape map** — competitor patents in adjacent claims, white-space opportunities
- **Trademark, trade secret, know-how** protections
- **Academic licensing status** — if the company is spun out of a university or research institute, the license terms (exclusive / non-exclusive, milestone payments, royalty rates) are material

### Light version covers:

- Software IP strategy (copyright, trade secret as primary; patents as supplementary if there is original algorithmic IP)
- Whether FTO has been considered
- Any pending patent applications

### N/A version:

A single sentence stating IP strategy is software-defensive (copyright + trade secret) without patents, plus any future-state condition that would change this.

## Subsection 2 — Regulatory

### Full version covers:

- **Regulatory pathway** — for therapeutics: IND → Phase I/II/III → NDA / BLA. For devices: 510(k) / De Novo / PMA. For SaMD: FDA Pre-Cert, CDS rule. Include international parallels: CE-MDR, PMDA, NMPA, TFDA.
- **Current milestone** — last accomplished and next gating event, with timing
- **Pre-submission interactions** — any FDA or other regulator engagement, with date and outcome
- **Major regulatory risks** and mitigation plan

### Light version covers:

- Whether the product currently falls under any regulator's jurisdiction
- Any future-state conditions that would trigger regulatory engagement
- Compliance posture (HIPAA, GDPR, 21 CFR Part 11) if applicable

### N/A version:

A single sentence: "Research and design tools do not require FDA clearance. If our product expands to support [specific regulated workflow], we will engage with [regulator] — covered in 18-month roadmap."

## Subsection 3 — Reimbursement

### Full version covers:

- **Payer strategy** — Medicare, Medicaid, commercial payers, out-of-pocket markets, national health systems
- **Coding strategy** — CPT, HCPCS, ICD-10, DRG. Existing codes vs. need for new code application.
- **Pricing assumptions** and the health-economics evidence supporting them
- **Payer engagement progress** — advisory boards, early dialogues, pilot reimbursement arrangements
- **International payment differences** if the company is multi-market

### Light version covers:

- Whether reimbursement applies at all (often it does not for B2B SaaS)
- If the product affects clinical workflow, whether the buying entity is reimbursed for time saved or quality improvement

### N/A version:

A single sentence: "B2B SaaS — paying entity is the customer biotech / pharma directly. Reimbursement / payer dynamics do not apply."

## Common errors to avoid

- **Glossing over Phase III risk** — Phase II success rates do not predict Phase III. A therapeutic deck that treats IND-cleared as "almost there" is naïve and reads as such.
- **Assuming reimbursement without payer engagement** — claims that "Medicare will cover this" without any payer dialogue is a major credibility failure.
- **Patents that do not actually block competitors** — a narrow claim or an FTO gap should be disclosed, not hidden. Investors' counsel will find it.
- **COGS comparable to a specialty drug without therapeutic equivalence** — pricing assumptions that lift the price of a generic mechanism into specialty-drug ranges need defensive justification.
- **Treating academic publication as commercial validation** — peer-reviewed proof-of-concept ≠ commercial readiness. Be explicit about the gap.
