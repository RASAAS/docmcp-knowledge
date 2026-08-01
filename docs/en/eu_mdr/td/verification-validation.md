# Product Verification & Validation

**MDR Reference:** Annex II, Section 6 (pre-clinical)  
**BPG Rev.4 Reference:** Section 6 (pp. 32-62)  
**Document Code:** AII-S6-VV  
**Responsible Party:** Manufacturer (Client) / CRO (biocompatibility evaluation)  
**Service Mode:** Assist / Review

> **Detailed V&V sub-topic guides are available:** See the [V&V Overview](./vv/) page for individual guides on each V&V area including biocompatibility, software V&V, electrical safety, cybersecurity, sterilisation, packaging, usability, and more.

## General V&V Requirements Checklist

- [ ] Results and critical evaluation of all V&V tests/studies
- [ ] Each test linked to specific GSPRs and/or risk control measures
- [ ] For existing devices without new testing: rationale per Annex II 6.1(b)
- [ ] All design requirements and specification documents provided
- [ ] Design control input/output traceability matrix (requirements -> V&V evidence)
- [ ] Overarching design V&V plan(s) and associated report(s)
- [ ] For historic testing: clear identification of which reports apply to current device version
- [ ] Protocols: justified sample sizes (standards-based or risk-based), acceptance criteria, confidence intervals
- [ ] Worst-case and representative testing justification
- [ ] Pre-conditioning documented in advance with data included in reports
- [ ] Deviations/discrepancies investigated and documented with acceptance rationale
- [ ] Contract test laboratory accreditation/certification referenced
- [ ] Device lifetime evidence (distinct from shelf life)
- [ ] For AI/ML devices: training/testing datasets, tools, environments, V&V protocols/reports, EU Ethics guidelines compliance

## 6.1 Pre-Clinical Data

### 6.1.1 Biocompatibility (per ISO 10993 series)

- [ ] Standards and references applied for biological evaluation
- [ ] Personnel qualification (biological evaluation, toxicological risk assessment)
- [ ] Device formulation/family description
- [ ] Manufacturing impact on materials (passivation, sterilisation, etc.)
- [ ] Nature and duration of body contact categorisation
- [ ] Potential biological risks and hazards identification
- [ ] Chemical characterisation per ISO 10993-1 and -18
- [ ] Extractable & leachable testing (if required)
- [ ] Toxicological risk assessment per ISO 10993-17 (if applicable)
- [ ] Testing program determination (considering animal welfare)
- [ ] Test reports with method, standard, laboratory competence, conditions, results
- [ ] Laboratory ISO/IEC 17025 accreditation or GLP certificate
- [ ] Overall Biological Evaluation Report (BER) with safety conclusion
- [ ] Reference to risk management file and PMS data

### 6.1.2 Software V&V (EN 62304 / Cybersecurity)

- [ ] Statement and rationale for medical device qualification
- [ ] Software safety classification per EN 62304 with justification
- [ ] Software version under application clearly identified
- [ ] Standards compliance checklist with direct TD references
- [ ] Software development plan and lifecycle requirements
- [ ] Development environment description (tools, settings, configurations)
- [ ] Software requirements analysis (functional, non-functional, GSPR 17.4, cybersecurity)
- [ ] Software architectural design (requirements allocated to software items, SOUP list)
- [ ] Software detailed design (Class B & C: unit-level design data)
- [ ] SOUP list (name, version, manufacturer, functional/performance requirements)
- [ ] V&V plans, protocols, reports (in-house and simulated/actual use)
- [ ] Test environment documentation
- [ ] Automated testing scripts and test log results
- [ ] Hardware and OS compatibility verification
- [ ] Mobile platform compliance with GSPR 17.3 (if applicable)
- [ ] Traceability matrix (testing -> specifications)
- [ ] For AI/ML: questionnaire per Team-NB "AI in Medical Devices"
- [ ] Cybersecurity documentation per [MDCG 2019-16](/eu_mdr/mdcg/mdcg-2019-16)

### 6.1.3 Electrical Safety & EMC

- [ ] EN 60601-1 compliance evidence
- [ ] EN 60601-1-2 (EMC) compliance evidence
- [ ] Additional collateral/particular standards (EN 60601-1-X, EN 60601-2-X)

### 6.1.4 Packaging, Stability & Shelf-Life

- [ ] Packaging validation (seal strength, distribution, etc.)
- [ ] Accelerated aging studies with justification
- [ ] Real-time aging studies (or justification for absence)
- [ ] Shelf-life claims supported by data

### 6.1.5 Performance & Safety Testing

- [ ] Design verification and validation protocols/reports
- [ ] Measuring/diagnostic function accuracy (GSPR 15)
- [ ] MR compatibility (if applicable)
- [ ] Mechanical performance testing

### 6.1.6 Usability

- [ ] Usability engineering per EN 62366-1
- [ ] Formative evaluations
- [ ] Summative evaluation (validation)
- [ ] Use-related risk analysis

## 6.2 Specific Cases

### Drug/Device Combinations (6.2.1)
- [ ] Drug Master File (DMF) reference and Letter of Access
- [ ] Competent authority consultation requirements
- [ ] For EU-approved substances: all relevant documentation

### Human Origin Matter (6.2.2)
- [ ] TSE/CJD risk assessment
- [ ] Source traceability and donor selection
- [ ] Processing validation for virus/agent inactivation

### Animal Origin Matter (6.2.3)
- [ ] Compliance with Regulation (EU) 722/2012
- [ ] TSE risk assessment
- [ ] Source animal species and origin

### Sterilisation (6.2.7)
- [ ] Applied standard and claimed SAL
- [ ] Sterilisation facility details and QMS certificate
- [ ] Sterilisation validation and revalidation (protocol and reports)
- [ ] Sterility testing (EN ISO 11737-2), bioburden testing (EN ISO 11737-1)
- [ ] Environmental monitoring and clean room validation
- [ ] ETO residuals report (if applicable, including paediatric considerations)
- [ ] Radiation dose setting/substantiation reports (if applicable)
- [ ] For end-user sterilised products: IFU validation for all claimed processes

### CMR/Endocrine Disrupting Substances (6.2.6)
- [ ] Substances > 0.1% w/w identified
- [ ] Justification per GSPR 10.4.2 (exposure analysis, alternatives analysis, substitution rationale)
- [ ] Labelling of substances > 0.1% w/w per MDR requirements

## Key Regulatory References

- MDR (EU) 2017/745, Annex II, Section 6
- ISO 10993 series (biological evaluation)
- EN 62304: Medical device software lifecycle
- EN 62366-1: Usability engineering
- EN 60601-1: Medical electrical equipment safety
- EN 60601-1-2: EMC
- EN ISO 11135 / 11137 / 17665: Sterilisation standards
- EN ISO 11737-1/-2: Bioburden and sterility testing
- [MDCG 2019-16](/eu_mdr/mdcg/mdcg-2019-16): Cybersecurity
- Team-NB BPG for TD Submission, Rev.4 (2026-04-21), Section 6

## Dependency

V&V is a **Phase 2** deliverable. Testing is performed after device design freeze and provides the evidence base for GSPR compliance (Phase 4) and feeds into the CER benefit-risk analysis (Phase 3).
