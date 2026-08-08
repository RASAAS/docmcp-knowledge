# FDA Human Factors / Usability Engineering — Structured Summary

**Primary source:** FDA CDRH guidance *Applying Human Factors and Usability Engineering to Medical Devices* (issued **3 August 2026**; originally 3 February 2016). Nonbinding recommendations.  
**Docket:** FDA-2011-D-0469 · Document GUI00001757  
**Relationship to EU:** Complements IEC 62366-1 process evidence used for MDR/IVDR GSPR 5; FDA focuses on critical-task HF validation for premarket submissions.

> This page is a structured outline for harness / training use. It is **not** a substitute for the official guidance text.

## Document map (2026 edition)

| Section | Topic |
|---------|--------|
| 1 | Introduction |
| 2 | Scope |
| 3 | Definitions |
| 4 | Overview — HFE/UE as part of risk management |
| 5 | Device users, use environments, and user interface |
| 6 | Preliminary analyses and evaluations (critical tasks, known problems, analytical & empirical methods, formative) |
| 7 | Elimination or reduction of use-related hazards |
| 8 | Human factors validation testing (simulated-use; participants; tasks; environment; training; data) |
| App. | Examples / additional recommendations (as published) |

## Core concepts for UEF alignment

| FDA concept | Typical UEF / IEC 62366-1 counterpart |
|-------------|----------------------------------------|
| Device users / use environments / UI | Use Specification (Clause 5.1) |
| Critical tasks | Hazard-related use scenarios selected for summative (5.4–5.5) |
| Preliminary / formative evaluations | Formative evaluation (5.8) |
| HF validation testing | Summative evaluation (5.9) |
| Risk management linkage | ISO 14971 + use-related risk analysis |

## Critical tasks (FDA emphasis)

- Identify tasks where use errors could lead to serious harm.
- Use analytical methods (e.g. FMEA, fault tree, task analysis, heuristic/expert review) **and** empirical methods (contextual inquiry, interviews, formative evaluations).
- Categorize and prioritize critical tasks for HF validation protocols.

## Human factors validation testing (high level)

- Prefer simulated-use testing with representative intended users.
- Define tasks from critical-task analysis; include labelling / IFU as part of the UI.
- Document participant selection, training (or knowledge-task approach), environment fidelity, success criteria, use errors / close calls, and residual risk conclusions.
- Do **not** invent numeric sample-size rules in product files — follow current FDA expectations and manufacturer justification for the device risk profile.

## IVD / OTC / CLIA considerations

- Self-test / near-patient / OTC / CLIA-waived products may need additional lay-user HF evidence when claimed.
- Align UI and IFU with intended-use claims (for EU IVDR, also PE clinical performance in the intended environment).

## Practical use in Reguverse

- Built-in **Usability UEF Harness** (`#231`) uses IEC 62366-1 as the backbone and injects FDA notes via the regulatory crosswalk.
- Prefer applying the harness for structure; fill product-specific narrative and measured results from real studies.

## Related topics

- [MDR Usability](./usability)
- [IVDR Usability](/en/eu_ivdr/td/vv/usability)
- [MDR↔IVDR usability crosswalk](/en/eu_ivdr/td/vv/usability-crosswalk)
