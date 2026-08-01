# Cybersecurity

**MDR Reference:** Annex I, GSPR 17.2, 17.4  
**Guidance:** MDCG 2019-16 Rev.1 (July 2020)  
**Service Item ID:** `mdr_sec06_cybersecurity`  
**Applicability:** Devices containing software with network connectivity or data exchange capabilities

## Overview

Cybersecurity for medical devices addresses the protection of device functionality, data integrity, and patient safety from cyber threats throughout the device lifecycle. Under the MDR, cybersecurity is a regulatory obligation, not an optional enhancement. MDCG 2019-16 Rev.1 is the authoritative European guidance, and EN IEC 81001-5-1:2022 is the operational standard.

## Current Standards and Guidance

### EN IEC 81001-5-1:2022

The standard defines lifecycle requirements for secure development and maintenance of health software:

- **Process-oriented**: Does not prescribe specific technical solutions; requires structured security processes in the QMS
- **Supplements IEC 62304**: Adds security activities at each software lifecycle phase
- **Derived from IEC 62443-4-1**: Adapted for health software context
- **Interpretation Sheet ISH1:2025**: Clarifications published January 2025

> **Harmonisation status:** EN IEC 81001-5-1:2022 is widely recognised by Notified Bodies as state of the art for demonstrating MDR Annex I Section 17 compliance. Formal harmonisation listing in OJEU is pending as of August 2026.

### MDCG 2019-16 Rev.1

The European interpretation of MDR cybersecurity obligations:

- Explicitly references EN IEC 81001-5-1 as the operational framework
- Covers: secure design, secure implementation, verification, validation, vulnerability management, incident response, information sharing
- Used by Notified Bodies as the audit checklist for cybersecurity assessment

## Key Deliverables

| Document | Description |
|----------|-------------|
| Threat Model | Systematic identification of assets, threats, attack vectors |
| Secure Design Requirements | Security requirements derived from threat model |
| SBOM (Software Bill of Materials) | Complete inventory of software components and dependencies |
| Security V&V Reports | Penetration testing, vulnerability scanning, fuzz testing |
| Vulnerability Management Plan | Process for monitoring, assessing, and patching vulnerabilities |
| Incident Response Plan | Procedures for detecting, reporting, and responding to security incidents |
| Security Update / Patch Management | Lifecycle plan for distributing security updates |

## Cybersecurity Lifecycle Activities

### Pre-market (Design & Development)

1. **Threat modelling**: Identify assets, trust boundaries, threat agents, attack scenarios
2. **Security requirements**: Derive from threat model; integrate with software requirements
3. **Secure architecture**: Defence in depth, least privilege, secure defaults
4. **Secure coding practices**: Input validation, authentication, encryption, logging
5. **Security testing**: Static analysis, dynamic analysis, penetration testing, fuzz testing
6. **SBOM generation**: Track all third-party and open-source components

### Post-market (Maintenance & Monitoring)

7. **Vulnerability monitoring**: Continuous scanning of SBOM against CVE databases
8. **Security patch management**: Timely evaluation and deployment of patches
9. **Incident response**: Detection, triage, notification (coordinated vulnerability disclosure)
10. **Post-market security updates**: Integration with PMS and PSUR processes

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 17.2 | IT security measures, including protection against unauthorised access |
| 17.4 | Minimum requirements for hardware, IT networks, security measures |

## Related Topics

- [Software V&V](./software-vv) -- Cybersecurity is part of the software lifecycle
- [MDCG 2019-16 Guidance](/en/eu_mdr/mdcg/mdcg-2019-16) -- Detailed cybersecurity guidance
- [Device Interoperability](./interoperability) -- Network interface security
