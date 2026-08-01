# Sterilisation Validation

**MDR Reference:** Annex II, Section 6.2.7; Annex I GSPR 11.1  
**BPG Rev.4 Reference:** Section 6.2.7  
**Service Item ID:** `mdr_sec06_sterilization`  
**Applicability:** Devices supplied sterile or requiring sterilisation before use

## Overview

Sterilisation validation demonstrates that the sterilisation process consistently achieves the claimed Sterility Assurance Level (SAL), typically SAL 10^-6, without adversely affecting device safety and performance. The validation approach depends on the sterilisation method used.

## Key Standards by Sterilisation Method

| Method | Primary Standard | Key Aspects |
|--------|-----------------|-------------|
| Ethylene oxide (EO) | ISO 11135:2014 | Process development, validation, routine control, parametric release |
| Radiation (gamma/e-beam) | ISO 11137-1:2006+A2:2019, -2:2013+A1:2023, -3:2017+A1:2020 | Dose setting, dose mapping, routine monitoring |
| Moist heat (steam) | ISO 17665-1:2024 (Ed.2) | Saturated steam, steam-air mixtures; replaces 2006 edition |
| Dry heat | ISO 20857:2010 | High-temperature sterilisation |
| Vaporised H2O2 / Ozone | ISO 22441:2022 | Low-temperature chemical sterilisation |
| Aseptic processing | ISO 13408-1 | Partially harmonised under MDR (Part 1 only) |

### Supporting Standards

| Standard | Title |
|----------|-------|
| ISO 11737-1:2018+A1:2021 | Bioburden determination |
| ISO 11737-2:2019 | Sterility testing |
| ISO 10993-7:2008+A1:2019 | EO sterilisation residuals |

## Key Deliverables

| Document | Description |
|----------|-------------|
| Sterilisation Method Justification | Rationale for selected method |
| SAL Claim | Sterility Assurance Level (typically 10^-6) |
| Bioburden Testing Reports | Routine bioburden per ISO 11737-1 |
| Process Validation (IQ/OQ/PQ) | Equipment qualification and process performance |
| Dose Setting/Substantiation | For radiation: dose audit, VDmax, or Method 1/2 per ISO 11137-2 |
| EO Residuals Report | For EO: residual EO and ECH per ISO 10993-7 (including paediatric considerations) |
| Sterility Testing | Per ISO 11737-2 |
| Environmental Monitoring | Cleanroom classification and monitoring data |
| Sterilisation Facility QMS Certificate | ISO 13485 or equivalent |
| Revalidation Schedule | Periodic revalidation protocol |

## Special Considerations

### EO Residuals (ISO 10993-7)
- Maximum allowable limits for ethylene oxide (EO) and ethylene chlorohydrin (ECH)
- Special limits for paediatric devices
- Aeration time validation

### End-user Sterilisation
- If the device is sterilised by the end user: IFU validation for all claimed sterilisation processes
- See also [Reprocessing Validation](./reprocessing)

### Radiation Dose Audit
- Regular dose audit per ISO 11137-2 to confirm continued appropriateness of sterilisation dose
- Bioburden trending over time

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 11.1 | Devices supplied sterile: validated sterilisation method |
| 11.5 | Conditions for safe storage and transport |
| 10.1 | Minimise risks from substances (EO residuals) |

## Related Topics

- [Packaging Validation](./packaging) -- Sterile barrier must be validated alongside sterilisation
- [Biocompatibility](./biocompatibility) -- Sterilisation can affect material biocompatibility
- [Reprocessing Validation](./reprocessing) -- For reusable devices requiring re-sterilisation
