# Usability / Human Factors (IVDR)

**Primary process standard:** IEC 62366-1:2015+A1:2020  
**IVDR hooks:** Annex I GSPR 5 (use error); self-test / near-patient particulars in GSPR 19–20; consistency with Performance Evaluation (Art. 56 / Annex XIII) and IFU.

## Relationship to MDR usability

The **usability engineering process** is shared (IEC 62366-1). What changes under IVDR is:

| Topic | IVDR emphasis |
|-------|----------------|
| Regime | In vitro diagnostic medical devices (`eu_ivdr`) |
| GSPR numbering | Use-error clause is **GSPR 5** in IVDR Annex I (do not cite MDR clause numbers in IVDR TD) |
| Evidence neighbours | PER / analytical & clinical performance, not MDR CER |
| Self-test / near-patient | Extra information and validation expectations |

See also: [MDR↔IVDR usability crosswalk](./usability-crosswalk.md) and the MDR page [Usability / HFE](../../../eu_mdr/td/vv/usability.md).

## Built-in UEF harness (Reguverse)

Projects can apply the **Usability UEF harness** (Evidence / V&V domain `usability`) to generate structured plan/report skeletons. Code assembles structure; AI fills product-specific narrative only. Missing data is marked `[TO BE COMPLETED]` — never invent acceptance criteria.

## China special notes (not a parallel primary pathway)

- NMPA 2024 usability guidance is aimed at medical devices and **does not apply to IVD reagents**.
- Mid/low use-risk pathways may use a **use-error assessment report** instead of a full UEF in some China submissions — treat as jurisdiction-specific, not as a substitute for IVDR UEF when claiming EU CE under IVDR.
