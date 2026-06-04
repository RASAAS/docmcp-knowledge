# Safety Data (Step 5)

## Overview

Step 5 collects and organizes post-market safety surveillance data from major global medical device vigilance databases. This data provides the evidence base for subsequent risk assessment and benefit-risk analysis.

## Workflow

1. **Automated retrieval**: AI automatically fetches data from multiple public databases
2. **Confirm database status**: Confirm search status for each database
3. **Supplementary upload**: Upload exported results for databases requiring manual search
4. **Review and approve**: Confirm data completeness

## Data Sources

| Database | Country/Region | Retrieval Method | Description |
|----------|---------------|-----------------|-------------|
| FDA MAUDE | USA | Automatic + supplementary upload | Adverse event reports |
| FDA Recalls | USA | Automatic | Product recall information |
| Swissmedic FSCA | Switzerland | Automatic | Field safety corrective actions |
| MHRA Alerts | UK | Automatic | Medical device safety alerts |
| BfArM FSCA | Germany | Automatic | Field safety corrective actions |
| TGA DRAC | Australia | Manual upload | Recall/alert/corrective actions |

::: info
The system automatically retrieves data from databases marked "Automatic". For TGA DRAC, users must search the official website and upload the exported file (XLSX/CSV format).
:::

## Safety Data Checklist

Before executing Step 5, complete the safety data confirmation checklist:

- Confirm status for each database:
  - **Auto-fetched** -- System retrieved data successfully
  - **Searched with results** -- Upload exported results file
  - **Searched no results** -- Confirmed search but no relevant data
  - **Not searched** -- Only for optional databases

## Uploading Supplementary Data

For databases requiring manual supplementation:

1. Visit the relevant official database website
2. Export search results (PDF, XLSX, CSV formats supported)
3. Upload files in the Step 5 panel
4. System automatically parses and extracts key information

## Next Step

→ [Safety Data Analysis (Step 6)](./eu-step6)
