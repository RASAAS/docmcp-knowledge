---
title: 
---

# 

**文件编号**: IMDRF/AIML WG/N88 FINAL:2025

::: tip 官方来源
[https://www.imdrf.org/documents/good-machine-learning-practice-medical-device-development-guiding-principles](https://www.imdrf.org/documents/good-machine-learning-practice-medical-device-development-guiding-principles)
:::

<!-- fulltext-start -->

---

## 全文

# Good machine learning practice for medical device development: Guiding principles

**Document Number**: IMDRF/AIML WG/N88 FINAL:2025

**Source**: [https://www.imdrf.org/documents/good-machine-learning-practice-medical-device-development-guiding-principles](https://www.imdrf.org/documents/good-machine-learning-practice-medical-device-development-guiding-principles)

---

Final Document  
---  
IMDRF/AIML WG/N88 FINAL: 2025  
Good machine learning practice for medical device development: Guiding principles  
Authoring Group  
Artificial Intelligence/Machine Learning-enabled Working Group  

Preface

© Copyright 2025 by the International Medical Device Regulators Forum. 

This work is copyright. Subject to these Terms and Conditions, you may download, display, print, translate, modify and reproduce the whole or part of this work for your own personal use, for research, for educational purposes or, if you are part of an organisation, for internal use within your organisation, but only if you or your organisation do not use the reproduction for any commercial purpose and retain all disclaimer notices as part of that reproduction. If you use any part of this work, you must include the following acknowledgement (delete inapplicable): 

All other rights are reserved and you are not allowed to reproduce the whole or any part of this work in any way (electronic or otherwise) without first being given specific written permission from IMDRF to do so. Requests and inquiries concerning reproduction and rights are to be sent to the IMDRF Secretariat. 

Incorporation of this document, in part or in whole, into another document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the IMDRF. 

![](data:image/jpeg;base64,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)

****

**Naoyuki YASUDA, IMDRF Chair**

Contents

1\. Introduction 4

2\. References 5

3\. Guiding principles 6

# Introduction

Artificial intelligence (AI) technologies, including machine learning, have the potential to transform health care by deriving new and important insights from the vast amount of data generated in health care every day. They use algorithms that can learn from real-world use and potentially use this information to improve the product’s performance. But they also present unique considerations due to the iterative and data-driven nature of their development. This document establishes a common set of principles for the community to promote the development of safe, effective, and high-quality medical devices that incorporate AI. These principles are important to apply across the lifecycle of the medical device.

The 10 guiding principles for Good Machine Learning Practice (GMLP) presented in this document are a call to action to international standards organizations, international regulators, and other collaborative bodies to further advance GMLP. Areas of collaboration include research, creating educational tools and resources, international harmonization, and consensus standards, to inform regulatory policies and regulatory guidelines. These guiding principles may be used to adopt practices from other sectors, tailor them to the medical technology and healthcare, and to develop novel practices for this domain. 

Further advances in AI technologies in healthcare, exemplified by generative AI, highlight the importance of clearly describing a product’s intended use/ intended purpose and identifying its regulatory status. Moreover, generative AI may heighten the importance of GMLP, including fundamental software engineering practices. For example, healthcare technologies that incorporate generative AI may employ foundation models that are not under the provenance of the medical device manufacturers, thereby potentially introducing unique risks. Generative AI may also pose a more fundamental challenge with respect to demonstrating device performance. The regulatory science of measuring performance as well as characterizing and detecting errors in these models is maturing to meet this challenge. 

As the AI medical device field continues to evolve, so too must GMLP and consensus standards. Strong partnerships with our international public health partners are essential to empower responsible innovations in this area. Thus, we expect this collaborative work can inform future IMDRF efforts and other international engagements.

# References

IMDRF/SaMD WG/N10 FINAL:2013 _Software as a Medical Device (SaMD): Key Definitions_

IMDRF/SaMD WG/N12 FINAL:2014 _Software as a Medical Device: Possible Framework for Risk Categorization and Corresponding Considerations_

IMDRF/SaMD WG/N23 FINAL:2015 _Software as a Medical Device (SaMD): Application of Quality Management System_

IMDRF/SaMD WG/N41 FINAL:2017 _Software as a Medical Device (SaMD): Clinical Evaluation_

IMDRF/CYBER WG/N60 FINAL:2020 _Principles and Practices for Medical Device Cybersecurity_

IMDRF/AIMD WG/N67 (Edition 1):2022 _Machine Learning-enabled Medical Devices: Key Terms and Definitions_

IMDRF/CYBER WG/N70 FINAL:2023 (Edition1) _Principles and Practices for the Cybersecurity of Legacy Medical Devices_

IMDRF/CYBER WG/N73 FINAL:2023 (Edition 1) _Principles and Practices for Software Bill of Materials for Medical Device Cybersecurity_

IMDRF/MC/N79 DRAFT: 2023 _Guiding Principles to Support Medical Device Health Equity_

IMDRF/SaMD WG/N81 DRAFT:2024 _Medical Device Software: Considerations for Device and Risk Characterization_

# Guiding principles

  1. **The intended use/ intended purpose of the device is well understood, and multi-disciplinary expertise is leveraged throughout the total product life cycle** : In-depth understanding of a medical device’s intended use/ intended purpose[1] including context of use within the clinical workflow, and the desired benefits and associated patient risks, can help ensure that AI-enabled medical devices[2],[3] address clinically meaningful needs over the total product life cycle of the device[4]. Multi-disciplinary expertise provides context-specific insight and experience, informs the intended use/ intended purpose, and enhances the safety and effectiveness of the device. 
  2. **Good software engineering, medical device design, and security practices are implemented throughout the total product life cycle** : Model design is implemented and maintained with attention to the fundamentals: robust software engineering practices, usability, data quality assurance, data management, cybersecurity[5],[6],[7], and quality management practices4. These practices include methodical risk management[8] and design processes that can appropriately record and communicate decisions and rationale, as well as ensure traceability, reproducibility, data authenticity, confidentiality, integrity, and availability. The infrastructure needed for model deployment, monitoring, and maintenance is carefully considered. These practices help support the rights, safety, and welfare of patients, including through the ethical use of patient data. 
  3. **Clinical evaluation includes the use of datasets that are representative of the intended patient population** : Data collection protocols aim to ensure that the relevant characteristics of the intended patient population (for example, in terms of age, gender, sex, race, ethnicity, geographical location, medical condition)[9], intended use environment, and measurement inputs are sufficiently represented in a sample of adequate size in the datasets for training, testing, and monitoring so that results can be reasonably generalized to the intended population of interest. These are fundamental for clinical evaluations[10] and important to manage any unintended bias3 or dataset drift, promote appropriate and generalizable performance across the intended patient population, assess usability, and identify circumstances and subgroups where the model may underperform including over time.
  4. **Training datasets are independent of test sets** : Training and test datasets3 are selected and maintained to be appropriately independent of one another. All potential sources of dependence, including factors related to patients, sites, and data acquisition, are considered and addressed to assure independence. The extent of external validation is proportionate to risk.
  5. **Selected reference standards are fit-for-purpose** : Accepted methods for developing fit-for-purpose reference standard3 ensure that clinically relevant and well characterized data are collected and that the limitations of reference standards are understood. This includes documentation of the rationale for the choice of reference standards based on the device’s intended use/ intended purpose and assessment of their suitability to address the intended use environment. If available, accepted reference standards in model development and testing that promote and demonstrate model robustness and generalizability across the intended patient population are used. The selection of reference standards is based on broad consensus, where available, and appropriate expertise.
  6. **Model choice and design are tailored to the available data and the intended use/ intended purpose of the device** : Model choice and design are evaluated and shown to be suited to the available data and support the active mitigation of known risks, like overfitting, performance degradation, and security risks. The clinical benefits and risks related to the product are well understood, used to derive clinically meaningful performance goals for testing, and support the product’s safety and effectiveness in achieving its intended use/ intended purpose1. Considerations include the impact on both the overall intended patient population and its subgroups as well as uncertainty and variability in the device inputs, outputs, and clinical use conditions.
  7. **The device is assessed with a focus on human-AI interactions in the intended use environment, including the performance of the human-AI team, rather than just the device in isolation.** The performance of the device is assessed in the context of the intended use environment and clinical workflow, considering interactions with health care providers, patients, and caregivers where applicable. Human factors considerations are addressed, including for example, user skills, user expertise, user understanding of the model outputs and limitations, potential for overreliance, level of device autonomy, and user error, for normal use and reasonably foreseeable misuse.
  8. **Testing demonstrates device performance during clinically relevant conditions** : Methodologically and statistically sound test plans are developed and executed to generate clinically relevant device performance10 information independently of the training dataset. Considerations include the intended patient population, relevant subgroups, clinical environment and use by the human-AI team, measurement inputs, and potential confounding factors.
  9. **Users are provided clear, essential information** : The intended audience (such as health care professionals or patients) are provided clear, contextually relevant information appropriate to their needs. This includes the product’s intended use/ intended purpose1 and indications for use, benefits and risks, performance of the model for appropriate subgroups, the study methodology, characteristics of the data used to train and test the model, acceptable inputs, known limitations, user interface interpretation, clinical workflow integration of the model, and to the extent possible the basis for model output. Users are also made aware of the scope and timing of device modifications and updates. They are provided a means to communicate product concerns to the manufacturer.
  10. **Deployed models are monitored for performance and re-training risks are managed** : Deployed models have the capability for an appropriate level of ongoing monitoring in “real world” use with a risk-based focus on maintained or improved safety and performance4,10\. Additionally, when models are retrained after deployment, there are appropriate controls in place to manage risks of overfitting, unintended bias, or degradation of the model (for example, dataset drift) that may impact the safety and performance of the model.

Disclaimer

© Copyright 205 by the International Medical Device Regulators Forum. 

This work is copyright. Subject to these Terms and Conditions, you may download, display, print, translate, modify and reproduce the whole or part of this work for your own personal use, for research, for educational purposes or, if you are part of an organisation, for internal use within your organisation, but only if you or your organisation do not use the reproduction for any commercial purpose and retain all disclaimer notices as part of that reproduction. If you use any part of this work, you must include the following acknowledgement (delete inapplicable): 

All other rights are reserved, and you are not allowed to reproduce the whole or any part of this work in any way (electronic or otherwise) without first being given specific written permission from IMDRF to do so. Requests and inquiries concerning reproduction and rights are to be sent to the IMDRF Secretariat. 

Incorporation of this document, in part or in whole, into another document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the IMDRF. 

Please visit our website for more details.

[www.imdrf.org](<http://www.imdrf.org/>)

  1. IMDRF/SaMD WG/N81 DRAFT:2024 _Medical Device Software: Considerations for Device and Risk Characterization_ ↑

  2. IMDRF/SaMD WG/N10 FINAL:2013 _Software as a Medical Device (SaMD): Key Definitions_ ↑

  3. IMDRF/AIMD WG/N67 (Edition 1):2022 _Machine Learning-enabled Medical Devices: Key Terms and Definitions_ ↑

  4. IMDRF/SaMD WG/N23 FINAL:2015 Software as a Medical Device (SaMD): Application of Quality Management System ↑

  5. IMDRF/CYBER WG/N60 FINAL:2020 _Principles and Practices for Medical Device Cybersecurity_ ↑

  6. IMDRF/CYBER WG/N70 FINAL:2023 (Edition1) _Principles and Practices for the Cybersecurity of Legacy Medical Devices_ ↑

  7. IMDRF/CYBER WG/N73 FINAL:2023 (Edition 1) _Principles and Practices for Software Bill of Materials for Medical Device Cybersecurity_ ↑

  8. IMDRF/SaMD WG/N12 FINAL:2014 _Software as a Medical Device: Possible Framework for Risk Categorization and Corresponding Considerations_ ↑

  9. IMDRF/MC/N79 DRAFT: 2023 _Guiding Principles to Support Medical Device Health Equity_ ↑

  10. IMDRF/SaMD WG/N41 FINAL:2017 _Software as a Medical Device (SaMD): Clinical Evaluation_ ↑


<!-- fulltext-end -->
