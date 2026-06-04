# Generate Documents (CEP/CER/DCR)

## Document Types

| Document | Full Name | Generation Method |
|----------|-----------|-------------------|
| CEP | Clinical Evaluation Plan | AI + code injection |
| CER | Clinical Evaluation Report | AI + code injection |
| DCR | Data Collection Report | Deterministic code assembly |

## Document Pipeline

After all steps are approved:

1. Each document shows status (Ready / Generating / Completed)
2. Click "Generate" to start
3. Streaming output shows progress in real-time
4. Upon completion, available actions:
   - **Insert to Word** -- insert into current document
   - **Download** -- export as .docx file
   - **Preview** -- view content
   - **Edit** -- modify text
   - **Redo** -- regenerate (confirmation required)

## Format Standards

- Font: Times New Roman
- Body: 10.5pt, 1.5 line spacing, justified
- Tables: 1pt solid borders, 9pt font, gray headers

## AI Content Labeling

All generated documents include:
- Cover page label: "AI-Assisted Document -- Generated with Reguverse Assistant"
- Word document metadata with AI generation information
