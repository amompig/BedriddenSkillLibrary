# 7-criteria evaluation framework

Each candidate is scored 1–5 per criterion. Score 5 = "best-in-class", not "good".

## 1. Clinical unmet need
Cite evidence of the gap (guideline blind spot, outcome variability, workflow bottleneck).

- **5**: Patients demonstrably suffer for lack of solution; published outcome gap
- **4**: Clear gap with measurable impact, but workarounds exist
- **3**: Improvement opportunity, not crisis
- **2**: Nice-to-have
- **1**: No clear gap

## 2. Technical novelty
What ML method, why ultrasound-specific.

- **5**: Genuinely new methodology (architecture / paradigm / data modality)
- **4**: Meaningful adaptation of existing method to a new domain
- **3**: Combination of known techniques with one twist
- **2**: Standard CNN on existing dataset with minor variation
- **1**: Re-implementation without differentiator

## 3. Data feasibility
Imaging cohort + claims linkage feasibility, including the 6–9 month HWDC + IRB lead time.

- **5**: Both imaging cohort and claims linkage credibly accessible within timeline
- **4**: One side (imaging or claims) is solid; the other has named mitigation
- **3**: Acquisition possible but with significant timeline risk
- **2**: Acquisition is the limiting factor without clear mitigation
- **1**: Required data effectively unavailable

## 4. Outcome measurability
30-day mortality, LOS, readmission, downstream imaging utilization, cost per encounter.

- **5**: Outcomes cleanly extractable from claims without strong assumptions
- **4**: Mostly claims-extractable with minor coding caveats
- **3**: Hybrid claims + chart review
- **2**: Outcomes require fragile coding assumptions
- **1**: Outcomes require chart review only

## 5. Regulatory path
SaMD class, FDA / TFDA pathway, local clinical trial registration.

- **5**: Clear precedent device exists; pathway is mapped
- **4**: Pathway is identifiable but precedent is partial
- **3**: Pathway exists but novelty creates new sub-class question
- **2**: Novel regulatory category
- **1**: Unclear class; high regulatory risk

## 6. Competitive landscape
Separate Taiwan / Asia / US / EU; cite refs for each region.

- **5**: Novel in target funding region (TW for NSTC / NHRI; US for NIH)
- **4**: Some prior art in target region but clear differentiation
- **3**: Active area in target region; need clear differentiation
- **2**: Saturated in target region
- **1**: Saturated everywhere

## 7. Funding fit
Specific agency / mechanism match.

- **5**: A named mechanism's call topics directly match
- **4**: Strong fit to a named mechanism's typical portfolio
- **3**: Fit to a generic grant mechanism
- **2**: No obvious agency aligns; cobbled funding required
- **1**: No funding pathway identified
