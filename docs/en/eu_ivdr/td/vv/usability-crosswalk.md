# Usability regulatory crosswalk (MDR / IVDR / FDA / China notes)

**Process backbone:** IEC 62366-1:2015+A1:2020 (plus IEC TR 62366-2 guidance).

This page supports Reguverse V&V Usability harness (#231) and EU IVDR project architecture (#232). China content is **special notes only**.

| Topic | IEC 62366-1 | EU MDR | EU IVDR | FDA | China special notes |
|-------|-------------|--------|---------|-----|---------------------|
| Use-error risk reduction | Cl. 5 / use specification & hazard-related scenarios | Annex I GSPR 5 | Annex I GSPR 5 | HF Engineering guidance | Mid/low use-risk may use use-error assessment report; NMPA 2024 usability guidance **does not apply to IVD reagents** |
| UEF / UER documentation | Cl. 4–5 | TD evidence + RM link | TD evidence + PE/IFU consistency | HF validation report expectations | Change registration may need QMS/declaration updates for UI changes |
| Self-test / near-patient | Representative lay/near-patient users when claimed | N/A (MD regime) | GSPR 19–20 + PE in intended environment | OTC / CLIA-waived HF when applicable | Instrument UI may still need use-related RM even when reagent guidance is out of scope |

## Product implications in Reguverse

1. Create project with **explicit EU MDR vs EU IVDR** selection (`regulation_id` + `device_regime`).
2. Usability harness is shared; IVDR projects default archetype hint `ivd_poct`.
3. Do **not** soft-fork MDR Clinical Evaluation into Performance Evaluation — PE is a separate workflow.
