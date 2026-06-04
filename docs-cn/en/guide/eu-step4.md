# Literature Screening (Step 4)

## Overview

Step 4 performs automated screening (Title/Abstract Screening) on literature search results, determining relevance of each article based on the inclusion/exclusion criteria defined in Step 3.

## Upload Search Results

Before executing Step 4, upload exported literature files:

1. Click "Upload" in the Step 4 panel
2. Select the database source
3. Upload files:
   - **PubMed**: Upload `.nbib` format files
   - **Embase / Cochrane / ScienceDirect**: Upload `.ris` format files
4. System automatically parses, counts articles, and deduplicates

## Workflow

1. **Auto batch processing**: AI screens literature in batches
2. **Progress monitoring**: Real-time progress display
3. **Review results**: View screening decisions and reasoning for each article
4. **Approve**: Confirm screening results

## Ethical Contraindications (Optional)

If the target indication has ethical constraints preventing randomized controlled trials (RCTs), enable the "Ethical Contraindications" option and describe the specific indications. When enabled, AI will not exclude articles solely for lacking RCT evidence, prioritizing observational studies and clinical experience with similar devices.

## Batch Processing

Due to potentially large numbers of articles (dozens to thousands), Step 4 uses batch processing:

- Each batch processes a group of articles
- Auto-continue mode runs batches sequentially
- Pause to switch to manual batch-by-batch confirmation
- Results are merged automatically after all batches complete

### Auto-continue Mode

- Enabled by default
- Progress bar shows real-time status
- Click "Pause" to switch to manual mode
- Auto-pauses on error for review

## Screening Output

Each article receives:
- **Relevant**: Included for full-text appraisal
- **Irrelevant**: Excluded with documented reasoning

Consolidated statistics:
- Total retrieved
- After deduplication
- Included count
- Excluded count (by exclusion reason)

## Next Step

→ [Safety Data (Step 5)](./eu-step5)
