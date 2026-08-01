# Electrical Safety & EMC

**MDR Reference:** Annex II, Section 6.1.3; Annex I GSPRs 14, 18  
**BPG Rev.4 Reference:** Section 6.1.3  
**Service Item ID:** `mdr_sec06_esafety_emc`  
**Applicability:** Active electrical medical devices (excluding software-only)

## Overview

Electrical safety and electromagnetic compatibility (EMC) testing demonstrates that active medical electrical equipment does not pose electrical, mechanical, thermal, or electromagnetic hazards to patients, operators, or bystanders. Testing is performed against the IEC 60601 family of standards.

## Current Standards

### EN 60601-1 (General Safety)

The authoritative European reference is **EN 60601-1:2006+A1+A12+A2+A13:2024** (informally called "Edition 3.2"):

- **Edition 3** (2005): Major structural rewrite introducing risk management integration
- **A1** (2012): Edition 3.1 -- reworked risk management and essential performance language
- **A2** (2020/2021): Targeted clarifications across clauses
- **A13:2024**: European A-deviation updating Annexes ZA and ZZ for MDR alignment
- **Harmonised under MDR**: Since June 2026, by Commission Implementing Decision (EU) 2026/1231

### EN 60601-1-2 (EMC)

**EN 60601-1-2:2015+A1:2020** covers electromagnetic disturbances and immunity:

- Emissions limits (conducted and radiated)
- Immunity to electrostatic discharge, RF fields, power frequency magnetic fields
- Essential performance under EMC conditions

### Collateral and Particular Standards

- **EN 60601-1-X**: Collateral standards (e.g., -1-6 usability, -1-8 alarms, -1-9 requirements for environmentally conscious design, -1-11 home healthcare)
- **EN 60601-2-X**: Particular standards for specific device types (e.g., -2-1 electron accelerators, -2-2 HF surgical equipment, -2-47 ambulatory ECG)

> **Note:** Only some collateral and particular standards are individually harmonised under the MDR. Check the [current harmonised standards list](/en/eu_mdr/standards/electrical-safety).

## Key Deliverables

| Document | Description |
|----------|-------------|
| Standards Applicability Analysis | Justification for applied/excluded standards |
| Essential Performance Definition | Functions whose loss/degradation could result in unacceptable risk |
| Test Reports (EN 60601-1) | Clause-by-clause compliance evidence |
| EMC Test Reports (EN 60601-1-2) | Emissions and immunity results |
| Risk Management File References | Integration of electrical risks into ISO 14971 file |

## Test Requirements Overview

### Electrical Safety (EN 60601-1)
- Protection against electrical hazards (earthing, insulation, leakage current)
- Protection against mechanical hazards (moving parts, surfaces, pressure)
- Protection against excessive temperature
- Protection against fire
- Essential performance under single fault conditions
- Two means of protection (MOP) for patient and operator

### EMC (EN 60601-1-2)
- Radiated emissions
- Conducted emissions
- Electrostatic discharge (ESD) immunity
- Radiated RF immunity
- Electrical fast transient/burst immunity
- Power frequency magnetic field immunity
- Voltage dip and interruption immunity

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 14.1 | Protection against electrical risks |
| 14.2 | Electromagnetic disturbances and immunity |
| 18.1 | Active devices -- safety and performance under fault conditions |
| 18.8 | Active devices -- minimise risks from electromagnetic interference |

## Testing Considerations

- Test laboratory must be **ISO/IEC 17025 accredited** for the specific test methods
- Testing on the **finished device** in its intended configuration
- Essential performance must be defined and agreed with the Notified Body before testing
- For device families: worst-case configuration selection and justification required

## Related Topics

- [Design V&V](./design-vv) -- Electrical safety is part of the overall V&V plan
- [Software V&V](./software-vv) -- Software controlling safety-critical electrical functions
- [Device Interoperability](./interoperability) -- EMC considerations for connected systems
