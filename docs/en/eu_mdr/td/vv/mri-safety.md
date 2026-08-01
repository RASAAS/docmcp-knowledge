# MRI Safety (Implants)

**MDR Reference:** Annex I, GSPR 14.6  
**Service Item ID:** `mdr_sec06_mri_safety`  
**Applicability:** Implantable devices (excluding software-only)

## Overview

Implantable devices must be evaluated for MRI safety to determine their conditional labelling status (MR Unsafe, MR Conditional, MR Safe). Testing follows ASTM standards and ISO/TS 10974 for active implantable devices.

## Key Standards

| Standard | Title |
|----------|-------|
| ASTM F2052 | Magnetically induced displacement force |
| ASTM F2213 | Magnetically induced torque |
| ASTM F2119 | Heating -- passive implants |
| ASTM F2182 | RF-induced heating |
| ASTM F2213 | Evaluation of MRI artifacts |
| ISO/TS 10974:2018 | Active implantable devices -- MRI safety |

## MRI Labelling Categories

| Category | Definition |
|----------|------------|
| **MR Safe** | No known hazards in all MRI environments |
| **MR Conditional** | Safe under specified MRI conditions (field strength, SAR, gradient) |
| **MR Unsafe** | Known to pose hazards in all MRI environments |

## Key Deliverables

| Document | Description |
|----------|-------------|
| MRI Safety Evaluation Report | Test results and labelling determination |
| Displacement Force Testing (F2052) | Deflection angle measurement |
| Torque Testing (F2213) | Magnetically induced torque measurement |
| RF Heating Testing (F2182) | Temperature rise under RF exposure |
| Artifact Assessment (F2119) | Image distortion characterisation |
| MRI Conditional Labelling | Specific conditions for safe MRI scanning |

## Related Topics

- [Design V&V](./design-vv) -- MRI safety as part of overall safety testing
- [Biocompatibility](./biocompatibility) -- Material properties affecting MRI compatibility
