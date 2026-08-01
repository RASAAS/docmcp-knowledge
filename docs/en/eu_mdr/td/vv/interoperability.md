# Device Interoperability Testing

**MDR Reference:** Annex I, GSPR 14.5  
**Service Item ID:** `mdr_sec06_interop`  
**Applicability:** Active devices with interfaces to other devices or systems

## Overview

Interoperability testing demonstrates that a medical device can safely and effectively exchange data and function with other devices and systems it is designed to interact with. MDR GSPR 14.5 requires that devices designed to be used in combination with other devices can do so without compromising safety and performance.

## Key Requirements

- **Connection compatibility**: Physical and logical interface validation
- **Data integrity**: Verification of data transmitted across interfaces
- **Safety in combination**: No new hazards introduced by device interactions
- **Protocol conformance**: Compliance with applicable communication standards (e.g., HL7, DICOM, IEEE 11073)

## Key Deliverables

| Document | Description |
|----------|-------------|
| Interface Specification | Protocols, connectors, data formats |
| Interoperability Test Plan | Test scenarios for device combinations |
| Interoperability Test Report | Results of combination testing |
| Risk Assessment for Combinations | Hazards from device interactions |

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 14.5 | Devices in combination: safety and performance maintained |

## Related Topics

- [Design V&V](./design-vv) -- Interoperability as part of system-level validation
- [Electrical Safety & EMC](./electrical-safety-emc) -- EMC considerations for connected devices
- [Cybersecurity](./cybersecurity) -- Network interface security
