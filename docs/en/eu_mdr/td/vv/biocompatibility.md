# Biocompatibility Evaluation

**MDR Reference:** Annex II, Section 6.1.1  
**BPG Rev.4 Reference:** Section 6.1.1  
**Service Item ID:** `mdr_sec06_biocompatibility`  
**Applicability:** Devices with direct or indirect body contact (excluding software-only)

## Overview

Biocompatibility evaluation assesses whether a medical device causes adverse biological responses when in contact with the body. Under the MDR, this is a mandatory component of the pre-clinical evidence package for any device that contacts the patient or user. The evaluation follows a risk-based approach aligned with the ISO 10993 series.

## Current Standard: ISO 10993-1:2025 (Edition 6)

ISO 10993-1:2025 was published in November 2025, replacing the 2018 edition. This sixth edition represents a major reorganisation:

- **Risk management alignment**: The standard is now fully restructured to align with ISO 14971:2019
- **Biological effects** (not endpoints): The old "biological endpoints" terminology is replaced with "biological effects" to emphasise this is not a checklist process
- **Revised categorisation**: Based on specific tissue contact rather than device type; four new tables replace the old Annex A table
- **Exposure duration**: New guidance on calculating cumulative exposure duration
- **Biological equivalence**: More structured approach for establishing biological equivalence between devices
- **Characterisation**: Enhanced requirements for material characterisation and hazard identification

> **Transition note:** EN ISO 10993-1:2025 is available. Manufacturers should perform a gap analysis against their existing evaluations. The significance of differences will influence how quickly processes and existing evaluations need updating.

## Key Deliverables

| Document | Description |
|----------|-------------|
| Biological Evaluation Plan (BEP) | Risk-based plan identifying biological hazards, contact categorisation, testing needs |
| Material Characterisation | Chemical composition, processing aids, degradation products |
| Extractable & Leachable (E&L) Studies | Chemical characterisation per ISO 10993-18 |
| Toxicological Risk Assessment | Per ISO 10993-17 (if applicable) |
| Biological Test Reports | Method, standard, lab competence, conditions, results |
| Biological Evaluation Report (BER) | Overall safety conclusion integrating all evidence |

## Evaluation Framework

### Step 1: Material Characterisation
- Device formulation/family description
- Manufacturing impact on materials (passivation, sterilisation, coatings)
- Chemical characterisation per ISO 10993-1 and ISO 10993-18

### Step 2: Contact Categorisation
- Nature of body contact (surface, external communicating, implant)
- Duration of contact (limited, prolonged, long-term/permanent)
- Contact tissue type (intact skin, mucosal membrane, breached surface, blood, tissue/bone)

### Step 3: Hazard Identification
- Potential biological risks based on material and contact profile
- Consider reasonably foreseeable misuse (new in Ed.6)

### Step 4: Gap Analysis & Testing Decision
- Evaluate existing data (literature, predicate, in-house testing)
- Determine if additional testing is needed based on gaps

### Step 5: Testing (if required)
- In vitro, ex vivo, or in vivo models
- Laboratory ISO/IEC 17025 accreditation or GLP certificate required
- Consider animal welfare (3Rs principle: Replace, Reduce, Refine)

## Key ISO 10993 Sub-parts

| Standard | Title |
|----------|-------|
| ISO 10993-1:2025 | Evaluation and testing -- General principles |
| ISO 10993-3:2024 | Genotoxicity, carcinogenicity, reproductive toxicity |
| ISO 10993-4:2024 | Selection of tests for interactions with blood |
| ISO 10993-5:2009 | Cytotoxicity -- In vitro |
| ISO 10993-6:2016 | Local effects after implantation |
| ISO 10993-10:2021 | Irritation and skin sensitization |
| ISO 10993-11:2017 | Systemic toxicity |
| ISO 10993-17:2023 | Toxicological risk assessment of medical device constituents |
| ISO 10993-18:2020 | Chemical characterisation of medical device materials |

## GSPR Mapping

| GSPR | Requirement |
|------|-------------|
| 10.1 | Devices shall not present risks from substances or particles released |
| 10.4 | Devices designed to introduce substances: additional requirements |
| 11.1 | Chemical, physical, and biological properties minimised |

## Related Topics

- [Risk Management](/en/eu_mdr/td/risk-management) -- Biocompatibility feeds into the risk management file
- [Design V&V](./design-vv) -- Biocompatibility is a component of overall V&V
- [CMR / Endocrine Disrupting Substances](./cmr-endocrine) -- Overlaps with chemical risk assessment
- [Sterilisation Validation](./sterilization) -- Sterilisation method can affect biocompatibility
