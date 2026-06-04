# Full-text Appraisal (Step 7)

## Overview

Step 7 performs full-text quality appraisal of literature screened as "Relevant" in Step 4, using systematic scoring based on IMDRF clinical evaluation guidance and MDCG evidence grading criteria.

## Scoring System

### Four-dimension Quality Scoring

Each article is scored across four dimensions, 1-3 points each:

| Dimension | Description | Score |
|-----------|-------------|-------|
| Design (D) | Study design quality | 1-3 |
| Applicability (A) | Applicability to target device | 1-3 |
| Population (P) | Study population relevance | 1-3 |
| Reporting (R) | Completeness of result reporting | 1-3 |
| **Total (SUM)** | **Composite score** | **4-12** |

### SOTA Assessment

In addition to the four-dimension scoring, each article undergoes a State of the Art (SOTA) assessment to determine whether the literature reflects current best practices and clinical standards.

### Contribution Assessment

Evaluates each article's contribution to clinical evaluation conclusions:
- Contribution to safety argumentation
- Contribution to effectiveness argumentation
- Contribution to benefit-risk evaluation

## Ethical Contraindications (Optional)

Same as Step 4 -- if the target indication has ethical constraints preventing RCTs, enable "Ethical Contraindications". When enabled, scoring adjusts requirements for study design level and does not penalize articles for lacking RCT evidence.

## Batch Processing

Step 7 also uses batch processing:
- Each batch appraises a group of articles
- Auto-continue mode runs sequentially
- Can pause for manual batch review
- All batch results merge on completion

## Output

Each article's appraisal includes:
- Four-dimension scores (D/A/P/R) and composite score
- SOTA assessment conclusion
- Contribution evaluation
- Key findings summary
- Methodological limitations

<!-- Screenshot placeholder: Step 7 appraisal results -->

## Next Step

→ [Literature Summary (Step 8)](./eu-step8)
