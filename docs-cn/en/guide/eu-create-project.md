# Create EU MDR Project

## Overview

Create a project to start the EU MDR clinical evaluation workflow. After creation, the system guides you through 10 steps to generate CEP, CER, and DCR documents.

## Steps

1. Click "Projects" in bottom navigation
2. Click "+ New Project"
3. Fill in project information:
   - Project name
   - Regulatory framework: EU MDR
   - Device name, classification (I/IIa/IIb/III)
   - Manufacturer name
   - Product description
4. Click "Create"

## Project Dashboard

After creation, the dashboard shows:
- Project information
- Task list (add multiple workflow tasks)
- Document pipeline

## Prerequisite: Device Description

::: warning Important Pre-step
Before starting the clinical evaluation workflow, it is recommended to complete the Device Description first. Structured information from the Device Description is automatically injected into multiple CEP/CER document sections (features, principles of operation, intended purpose, etc.), ensuring accuracy and consistency.
:::

The Device Description module allows you to fill in structured device information:

- **Features & Functions** -- Technical features and core capabilities
- **Configurations & Variants** -- Different models and options
- **Accessories** -- Accompanying accessories and components
- **Previous Generations / Similar Devices** -- Prior versions and market equivalents
- **Principles of Operation** -- Technical working principles

**How to fill:**
- Manually fill each field
- Click "AI Fill" to automatically extract device information from uploaded context files

<!-- Screenshot placeholder: Device Description module -->

## Context Files

Upload reference documents for AI to use:
- IFU / Technical specifications
- Design documents
- Existing clinical data
- Equivalent device information
- PDF / Word / Excel supported

::: tip
Upload detailed device information documents. AI will extract key information for analysis in subsequent steps.
:::

## Available Tasks

Click "+ Add Task" to select a workflow:

| Task Type | Description | Plans |
|-----------|-------------|-------|
| Clinical Evaluation | 10-step EU MDR CE workflow | All |
| Risk Management | ISO 14971 compliant RM | All |
| GSPR Compliance | Annex I compliance check | Pro/Max |
| PMS Plan | Post-market surveillance plan | Pro/Max |
| PMCF Plan | Clinical follow-up plan | Pro/Max |
| CE Update | Clinical evaluation update | Pro/Max |
| PMCF Report | PMCF evaluation report | Pro/Max |
| PSUR | Periodic safety update report | Pro/Max |
| Evidence Registry | Evidence traceability | Pro/Max |
| V&V Execution | Verification & validation | Pro/Max |

## Next Step

After creating a project, completing Device Description, and adding a Clinical Evaluation task, start the 10-step workflow:

→ [Device Info (Step 1)](./eu-step1)
