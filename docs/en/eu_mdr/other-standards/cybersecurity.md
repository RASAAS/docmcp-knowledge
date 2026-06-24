# Cybersecurity

This category contains **6** standards.

::: tip Key Standard
**IEC 81001-5-1:2021** (EN IEC 81001-5-1:2022) is considered the current state-of-the-art for medical device cybersecurity under EU MDR, even though its harmonisation has been delayed to 2028.
:::

| Standard No. | Title | Scope | GSPR |
| --- | --- | --- | --- |
| [IEC 81001-5-1:2021](https://www.iso.org/standard/76097.html) | Health software and health IT systems safety, effectiveness and security - Part 5-1: Security - Activities in the product life cycle | Secure software lifecycle processes for health software (SaMD, SiMD, MDSW) | 17, 17.1-17.4, 18, 18.8 |
| [IEC TR 60601-4-5:2021](https://webstore.iec.ch/en/publication/34263) | Medical electrical equipment - Part 4-5: Guidance and interpretation - Safety-related technical security specifications | Technical security requirements for network-connected medical electrical equipment | 17, 17.1, 17.2, 17.4, 18 |
| [IEC 80001-1:2021](https://webstore.iec.ch/en/publication/34263) | Application of risk management for IT-networks incorporating medical devices - Part 1: Safety, effectiveness and security | Risk management for networked medical devices and health IT | 17, 17.4, 18, 18.8 |
| [IEC 62443-4-1:2018](https://webstore.iec.ch/en/publication/33615) | Security for industrial automation and control systems - Part 4-1: Secure product development lifecycle requirements | Secure development lifecycle requirements (basis for IEC 81001-5-1) | 17, 17.2, 17.4 |
| [AAMI TIR57:2016/(R)2022](https://www.aami.org/store/products/tir57-2016-r-2022) | Principles for medical device security - Risk management | Cybersecurity risk management for medical devices (FDA recognized) | 17, 17.4, 18 |
| [IEC/TR 80001-2-2:2012](https://webstore.iec.ch/en/publication/7532) | Application of risk management for IT-networks - Part 2-2: Guidance for communication of medical device security needs, risks and controls | MDS2 framework for manufacturer security disclosure | 17, 17.4 |

## Standards Relationship

```
IEC 62443-4-1 (generic secure development)
    |
    v  (adapted for health software)
IEC 81001-5-1 (PROCESS requirements - "how to develop securely")
    +
IEC TR 60601-4-5 (TECHNICAL requirements - "what to implement")
    =
Complete cybersecurity framework for medical devices
```

## Regulatory Status

- **EU MDR**: IEC 81001-5-1 harmonisation delayed to 2028, but considered state-of-the-art
- **Japan**: JIS T 81001-5-1 mandatory since April 2024
- **USA/FDA**: Recognized consensus standard; aligns with FDA's SPDF and Section 524B requirements
- **MDCG 2019-16 rev.1**: EU guidance on cybersecurity for medical devices

## Data Source

`eu_mdr/other_standards/standards-cybersecurity.json`
