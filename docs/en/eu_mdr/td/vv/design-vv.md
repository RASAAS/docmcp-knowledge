# Design Verification & Validation (Performance & Safety)

**MDR Reference:** Annex II, Section 6.1 (pre-clinical data)  
**BPG Rev.4 Reference:** Section 6.1.5  
**Service Item ID:** `mdr_sec06_design_vv`  
**Applicability:** All medical devices

## Overview

Design V&V is the systematic process of confirming that device design outputs meet design inputs (verification) and that the finished device meets user needs and intended uses (validation). Under MDR, manufacturers must provide evidence that their device conforms to the applicable GSPRs through a structured design control process.

## Scope

- **Design verification**: confirms design outputs meet design input requirements (bench testing, analysis, inspection)
- **Design validation**: confirms the finished device meets user needs under actual or simulated use conditions
- **Performance testing**: demonstrates device meets its claimed performance specifications
- **Safety testing**: demonstrates device does not introduce unacceptable risks under normal and fault conditions

## Key Deliverables

| Document | Description |
|----------|-------------|
| Design Control Matrix | Traceability from user needs -> design inputs -> design outputs -> V&V evidence |
| Verification Plan & Protocols | Test methods, sample sizes, acceptance criteria for each design output |
| Verification Reports | Test results, pass/fail, deviations, statistical analysis |
| Validation Plan & Protocols | Clinical/simulated-use conditions, user population, acceptance criteria |
| Validation Reports | Results demonstrating intended use fulfilment |

## Regulatory Requirements

### MDR Annex II Section 6.1 Requirements

- Results and critical evaluation of all V&V tests/studies
- Each test linked to specific GSPRs and/or risk control measures
- All design requirements and specification documents provided
- Design control input/output traceability matrix
- Overarching design V&V plan(s) and associated report(s)
- Protocols with justified sample sizes (standards-based or risk-based), acceptance criteria, confidence intervals
- Worst-case and representative testing justification
- Pre-conditioning documented in advance with data included in reports
- Deviations/discrepancies investigated and documented with acceptance rationale
- Contract test laboratory accreditation/certification referenced

### GSPR Mapping

| GSPR | Requirement | V&V Evidence |
|------|-------------|--------------|
| 1 | Safe and perform as intended | Overall V&V conclusion |
| 3 | State of the art | Current standards applied |
| 6.1 | Chemical, physical, biological properties | Material and performance testing |
| 8 | Device and manufacturing process design | Design control documentation |

## Best Practice Guidance

- Follow ISO 13485:2016 Clause 7.3 (Design and Development) for design control structure
- Use a **Design History File (DHF)** to compile all design control records
- Statistical justification per ASTM E2709 or equivalent for sample sizes
- For historic testing on legacy devices: clear identification of which reports apply to the current device version per Annex II 6.1(b)

## Key Standards

| Standard | Title | Status |
|----------|-------|--------|
| ISO 13485:2016 | Medical devices -- QMS -- Requirements for regulatory purposes | Harmonised (EN ISO 13485:2016+A11:2021) |
| ISO 14971:2019 | Application of risk management to medical devices | Harmonised (EN ISO 14971:2019+A11:2021) |

> **Note:** Product-specific performance standards vary by device type (e.g., EN ISO 21535 for hip implants, EN ISO 25539 for vascular devices). Consult the [harmonised standards list](/en/eu_mdr/standards/) and [other applicable standards](/en/eu_mdr/other-standards/) for your device category.

## Related Topics

- [Risk Management](/en/eu_mdr/td/risk-management) -- V&V evidence feeds into risk control verification
- [GSPR Checklist](/en/eu_mdr/td/gspr) -- V&V results referenced in GSPR compliance demonstration
- [Device Lifetime Validation](./device-lifetime) -- Lifetime testing is a subset of design V&V
