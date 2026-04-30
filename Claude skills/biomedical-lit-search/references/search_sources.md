# Search source priority

| Source | Best for | Notes |
|---|---|---|
| PubMed (MEDLINE) | Clinical trials, guidelines, peer-reviewed clinical work | Stable PMIDs; primary for biomedical |
| Google Scholar | Breadth, citation tracing, grey literature, conference proceedings | Includes non-peer-reviewed |
| arXiv | ML / AI methods (cs.CV, cs.LG, eess.IV) | Preprints; tag explicitly |
| medRxiv / bioRxiv | Biomedical preprints when timeliness matters | Non-peer-reviewed |
| ClinicalTrials.gov | Ongoing / planned trials | Use to identify competition |
| FDA SaMD database | Cleared AI medical devices | For regulatory landscape |

## Pick by research question type
- Clinical guideline question → PubMed first
- AI method question → arXiv first, then PubMed for clinical validations
- Workflow / health services question → PubMed + Google Scholar
- Regulatory / device question → FDA SaMD database + PubMed
- Taiwan-specific health policy → PubMed (filter Taiwan affiliations) + 衛福部 official sources

## When web search tools are unavailable
Draw from training knowledge and tag every citation `[TRAINING-RECALL — user to verify]`. Disclose at the top of Part A:
> "Web search not invoked; all citations require user verification."
