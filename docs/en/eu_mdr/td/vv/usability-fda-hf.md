# FDA Human Factors — Process vs Submission Content

Reguverse separates **two complementary FDA guidance documents**. Do not conflate them with the IEC 62366-1 Usability Engineering File (UEF) process backbone used in the product harness.

## 1. Process guidance

**Title:** *Applying Human Factors and Usability Engineering to Medical Devices*  
**Role:** How to perform HFE/UE as part of risk management and design controls (users, environments, UI, formative work, HF validation testing methods).  
**UEF mapping (typical):** Use Specification ↔ users/use environments; critical tasks ↔ hazard-related use scenarios selected for summative; formative ↔ Clause 5.8; HF validation ↔ summative Clause 5.9.

## 2. Content / marketing-submission guidance (2026)

**Title:** *Content of Human Factors Information in Medical Device Marketing Submissions*  
**Published:** 29 May 2026 (Federal Register announcement)  
**Implementation expectation:** submissions received on or after **1 August 2026**  
**Applies to:** 510(k), De Novo, PMA, HDE (CDRH medical devices)  
**Does not replace:** risk management / design controls / performing HFE activities — it tells sponsors **what level of HF documentation to file**.  
**Town hall:** CDRH 22 July 2026 (slides/transcript via CDRH Learn).

### HF Submission Categories

| Category | When (high level) | What to provide |
|----------|-------------------|-----------------|
| **1** | Modified device; no change to UI / users / uses / environments / training / labeling | Conclusion + high-level HF summary |
| **2** | No critical tasks (new) / no new or impacted critical tasks (modified), **or** Decision Point D concludes validation data need not be submitted | Cat1 content + users/UI/known-use-problems + rationale |
| **3** | Critical tasks warrant filing HF validation | Full HFE/UE report incl. preliminary analyses, **URRA**, critical tasks, HF validation of final design |

Flowchart decisions: **A** modification? → **B** UI/users/uses/env/training/labeling change? → **C** critical tasks? → **D** submit HF validation data?  
**Decision Point D** is central: critical tasks do **not** automatically force Category 3 filing.

### URRA

Use-Related Risk Analysis (guidance Table 2) and comparative URRA (Table 3) are living analyses. Typical columns: task, use error, hazardous situation, harm, severity, **critical task Y/N**, risk controls, validation method for control effectiveness.

### eSTAR

Updated eSTAR templates prompt Category selection (“Guide Me” or sponsor-chosen) and locate supporting sections.

## 3. How Reguverse implements this

| Layer | Implementation |
|-------|----------------|
| Process UEF | Built-in Usability Harness (`#231`) — IEC 62366-1 Document+Study |
| UE ↔ RM | `#233`–`#235` (same hazard table, Sync) |
| FDA submission overlay | `#236` Path B — Category wizard + **derived URRA view** + Submission Pack |
| FDA pack substantive generation | `#237` Phase 3 — **hybrid** assembly: code-injects Use Spec / UI Spec / URRA / Formative·Summative Study excerpts; LLM fills narrative slots only; Word download prefers persisted `pack_markdown` |
| Feature Visibility | Continues under `evidence_registry` (no new feature key) |
| Scope (current) | **MD only**; combination products excluded; IVD eSTAR deferred |

**Summative hard gate (process):** EU/IVDR/NMPA projects still require selected HRUS + substantive UI Spec before creating Summative Studies (`#233` D10).  
**Submission pack (FDA Cat 1/2):** may omit HF validation details even if process Summative Studies exist — UI states this explicitly.  
**Generate rule:** never invent participant counts / pass rates; missing UEF evidence becomes `[TO BE COMPLETED]`.

## Related pages

- [MDR Usability](./usability)
- [IVDR Usability](/en/eu_ivdr/td/vv/usability)
