# Citation verification tags

Every citation in Part A MUST carry exactly one tag.

| Tag | Meaning | Use when |
|---|---|---|
| (no tag) | Verified DOI / PMID / arXiv ID | Web search invoked + ID confirmed in returned results |
| `[UNVERIFIED]` | Found but ID cannot be confirmed | Search returned the title but no stable ID |
| `[TRAINING-RECALL — user to verify]` | Drawn from training knowledge | Web search not invoked or unavailable |
| `[SEMINAL]` | Pre-2021 foundational work | Allowed even outside the 5-year window |

If web search is unavailable at runtime, mark ALL citations `[TRAINING-RECALL]` and explicitly state at the top of Part A:
> "Web search not invoked; all citations require user verification."

## Time window policy
- **Primary**: last 5 years from current date (calculated from system date)
- **Allowed up to 10 years** if foundational; tag `[SEMINAL]`
- **Older than 10 years**: include only if guideline-level (e.g., BLUE protocol Lichtenstein 2008); explain inclusion in the Gap column

## Example well-formed Part A row

```
A1 | Pivetta et al., LUS-implemented ADHF dx in ED | Chest 2015 |
PMID 25950725 [SEMINAL] | EU (IT) | LUS+exam outperforms NT-proBNP+CXR
for ADHF | Single-center; no AI; no claims-linked outcomes
```

Verification tag stays alongside the ID; Region column captures geography; Finding stays terse; Gap column foreshadows the candidate-topic differentiator.
