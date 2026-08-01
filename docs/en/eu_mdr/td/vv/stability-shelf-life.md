# Stability & Shelf-life Validation

**MDR Reference:** Annex II, Section 6.1.4; Annex I GSPR 6.6  
**BPG Rev.4 Reference:** Section 6.1.4  
**Service Item ID:** `mdr_sec06_stability`  
**Applicability:** Non-software devices with shelf-life claims (excluding software-only)

## Overview

Stability and shelf-life validation demonstrates that the device maintains its safety and performance characteristics throughout its claimed shelf life. This includes both the device itself and its packaging, and is distinct from [device lifetime validation](./device-lifetime) which covers the in-use period.

## Key Standards

| Standard | Title | Scope |
|----------|-------|-------|
| ASTM F1980 | Accelerated aging of sterile barrier systems | Arrhenius-based accelerated aging methodology |
| ASTM D4169 | Performance testing of shipping containers | Transport simulation and distribution environment |
| EN ISO 11607-1:2020+A1:2023 | Packaging for terminally sterilised medical devices -- Part 1 | Packaging system requirements (overlaps with [Packaging](./packaging)) |
| ICHE Q1A-Q1E | Stability testing guidelines | Applicable to drug-device combinations |

## Key Deliverables

| Document | Description |
|----------|-------------|
| Shelf-life Claim Justification | Rationale for claimed expiry date |
| Accelerated Aging Protocol & Report | Test design, Q10 factor, temperature, duration, results |
| Real-time Aging Plan | Concurrent real-time study design (if accelerated aging used) |
| Transport Simulation Report | Distribution environment testing per ASTM D4169 or ISTA protocols |
| Post-aging Functional Testing | Device performance after aging exposure |

## Accelerated Aging (ASTM F1980)

- Based on the Arrhenius reaction rate theory
- **Q10 factor**: Typically Q10 = 2 (conservative); must be justified if different
- Accelerated aging temperature usually 55-60degC (must not exceed material limits)
- Accelerated aging time = (Desired shelf life) / Q10^((T_accelerated - T_ambient) / 10)
- **Real-time aging is the gold standard**: Accelerated aging supports initial market entry; real-time data must be completed concurrently

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 6.6 | Shelf life demonstrated by appropriate testing |
| 11.5 | Safe transport and storage conditions |

## Related Topics

- [Packaging Validation](./packaging) -- Package integrity after aging
- [Device Lifetime Validation](./device-lifetime) -- In-use lifetime (distinct from shelf life)
- [Sterilisation Validation](./sterilization) -- Sterility maintenance throughout shelf life
