# Usability / Human Factors Engineering

**MDR Reference:** Annex II, Section 6.1.6; Annex I GSPRs 5, 19  
**BPG Rev.4 Reference:** Section 6.1.6  
**Service Item ID:** `mdr_sec06_usability`  
**Applicability:** All medical devices (with varying depth based on risk profile)

## Overview

Usability engineering ensures that medical devices can be used safely and effectively by the intended users in the intended use environment. It is a risk-driven process that identifies and mitigates use-related hazards through iterative design and evaluation.

## Current Standard: IEC 62366-1:2015+A1:2020

The primary standard defines the usability engineering process for medical devices:

> **Harmonisation status:** IEC 62366-1 is **not harmonised** under MDR as of 2026. Compliance must be independently justified. However, it is universally accepted as the state-of-the-art standard for usability engineering by Notified Bodies.

### Supplementary Guidance
- **IEC/TR 62366-2:2016**: Guidance on applying IEC 62366-1
- **MDCG 2024-10**: Orphan devices guidance (includes usability considerations)
- **EN 60601-1-6:2010+A1:2013+A2:2020**: Usability for medical electrical equipment

## Key Deliverables

| Document | Description |
|----------|-------------|
| Use Specification | Intended users, patients, use environments, use scenarios |
| Use-related Risk Analysis | Hazard-related use scenarios, use errors, severity assessment |
| User Interface Specification | UI design requirements derived from use specification and risk analysis |
| Formative Evaluations | Iterative design reviews, expert reviews, early-stage user testing |
| Summative Evaluation (Validation) | Final human factors validation with representative users |
| Usability Engineering File | Complete record of the usability engineering process |

## Process Overview (IEC 62366-1)

1. **Use specification**: Define intended users, use environments, clinical workflow
2. **Use-related risk analysis**: Identify hazard-related use scenarios and potential use errors
3. **User interface specification**: Design requirements for the user interface
4. **User interface design**: Implement design based on specifications
5. **Formative evaluation**: Iterative testing to identify and fix usability issues
6. **Summative evaluation**: Final validation with representative users and tasks
7. **Residual risk assessment**: Evaluate remaining use-related risks

## Summative Evaluation Essentials

- Representative users (number, demographics, experience level)
- Critical tasks selected based on risk analysis
- Simulated or actual use environment
- Pass/fail criteria defined before testing
- Use errors, close calls, and difficulties documented and analysed
- Root cause analysis for any critical task failures

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 5 | Ergonomic design principles, user environment, user capabilities |
| 19 | IFU and labels: understandable by intended users |

## Related Topics

- [Design V&V](./design-vv) -- Usability validation is part of design validation
- [Software V&V](./software-vv) -- Software UI usability
- [Risk Management](/en/eu_mdr/td/risk-management) -- Use-related risk analysis feeds into the risk management file
