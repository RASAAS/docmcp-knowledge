# Software Verification & Validation (IEC 62304)

**MDR Reference:** Annex II, Section 6.1.2; Annex I GSPRs 17.1-17.4  
**BPG Rev.4 Reference:** Section 6.1.2  
**Service Item ID:** `mdr_sec06_software_vv`  
**Applicability:** Devices containing software, Software as a Medical Device (SaMD), AI/ML-based devices

## Overview

Software V&V demonstrates that medical device software is developed, verified, and validated according to a structured lifecycle process appropriate to its safety classification. The primary standard is IEC 62304, supplemented by IEC 82304-1 for health software products and MDCG 2019-16 for cybersecurity (covered separately in [Cybersecurity](./cybersecurity)).

## Current Standard: IEC 62304

### Edition 1 (Current Harmonised Version)
**EN 62304:2006+A1:2015** remains the harmonised version under EU MDR as of August 2026.

### Edition 2 (Publication: August 2026)
IEC 62304 Edition 2 is scheduled for publication on 12 August 2026. Key changes:

- **Scope expansion**: From "medical device software" to "health software" (broader scope)
- **Safety classification simplified**: Three classes (A/B/C) replaced by two **Software Process Rigor Levels** (I and II)
- **AI/ML lifecycle**: New clause 5.1.15 plus Annex E for AI/ML-specific requirements
- **Cybersecurity integration**: Threat modelling, secure-by-design, vulnerability management as core design controls
- **ISO 13485 and ISO 14971**: Removed as normative references (still applied in practice for regulated devices)
- **Agile guidance**: New Annex F (informative), based on AAMI TIR45:2023

> **Transition note:** Regulatory recognition of Edition 2 is expected 2-3 years after publication. EN 62304:2006+A1:2015 stays the state of the art for MDR compliance until Edition 2 is harmonised (estimated 2028-2029). New programs should consider designing to Edition 2 early.

## Key Deliverables

| Document | Description |
|----------|-------------|
| Software Safety Classification | Class A/B/C justification (Ed.1) or Rigor Level I/II (Ed.2) |
| Software Development Plan | Lifecycle model, standards, tools, V&V strategy |
| Software Requirements Specification | Functional, non-functional, GSPR 17.4, cybersecurity |
| Software Architecture Design | Components, SOUP list, interfaces |
| Software Detailed Design | Unit-level design data (Class B & C / Rigor II) |
| SOUP List | Name, version, manufacturer, functional requirements |
| V&V Plans, Protocols, Reports | Unit, integration, system testing |
| Traceability Matrix | Requirements -> Architecture -> Tests -> Results |
| Software Release Documentation | Release notes, known anomalies, residual risks |

## Safety Classification (IEC 62304 Ed.1)

| Class | Software Contribution to Hazardous Situation | Process Rigor |
|-------|----------------------------------------------|---------------|
| **A** | No contribution to hazardous situation, or hazard controlled externally | Minimal |
| **B** | Can contribute to hazardous situation that does NOT result in serious injury | Moderate |
| **C** | Can contribute to hazardous situation resulting in death or serious injury | Full |

## AI/ML-Specific Requirements

For AI/ML-based medical devices, additional documentation is expected:

- Training and testing dataset documentation (provenance, size, quality)
- Model architecture and hyperparameter selection rationale
- Performance metrics and validation methodology
- Monitoring triggers and retraining decision framework
- EU Ethics Guidelines for Trustworthy AI compliance
- Team-NB "AI in Medical Devices" questionnaire (if applicable)

See also: [MDCG 2025-6: MDR/IVDR & AI Act](/en/eu_mdr/mdcg/mdcg-2025-6)

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 17.1 | Software lifecycle according to state of the art |
| 17.2 | Software development and lifecycle processes |
| 17.3 | Mobile platforms -- IT environment requirements |
| 17.4 | Cybersecurity requirements (see [Cybersecurity](./cybersecurity)) |

## Related Topics

- [Cybersecurity](./cybersecurity) -- Security-specific lifecycle activities
- [Design V&V](./design-vv) -- Software V&V within overall design control
- [Usability / Human Factors](./usability) -- Software UI usability engineering
