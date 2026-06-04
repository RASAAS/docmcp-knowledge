# EUDAMED UDI Bulk Upload

Batch generate EUDAMED XML upload files for medical device manufacturers with many UDI-DI codes.

## Background

Since May 28, 2026, the EUDAMED UDI/Devices module is mandatory (Commission Decision (EU) 2025/2371). All new devices must register UDI before market placement; existing devices must complete registration by November 28, 2026.

## Workflow

```
Upload Excel → AI Parse/Map → Preview/Confirm → Generate XML → Download ZIP
```

1. **Upload Excel** -- supports custom formats and standard template
2. **Data Validation** -- checks required fields, GS1 format (14-digit zero-padded)
3. **Preview** -- table view of parsed results, editable
4. **Generate XML** -- EUDAMED XSD v3.0.28 compliant, auto-splits at 40 identifiers
5. **Download ZIP** -- ready for EUDAMED Bulk Upload interface

## Technical Constraints

| Constraint | Detail |
|-----------|--------|
| XSD Version | v3.0.28 |
| Per-file limit | 40 device identifiers |
| GS1 format | 14-digit zero-padded |
| Services | DEVICE.POST + UDI_DI.POST |

**Available on:** All plans
