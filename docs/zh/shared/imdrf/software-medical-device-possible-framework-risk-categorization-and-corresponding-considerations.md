---
title: 
---

# 

**文件编号**: IMDRF/SaMD WG/N12FINAL:2014

::: tip 官方来源
[https://www.imdrf.org/documents/software-medical-device-possible-framework-risk-categorization-and-corresponding-considerations](https://www.imdrf.org/documents/software-medical-device-possible-framework-risk-categorization-and-corresponding-considerations)
:::

<!-- fulltext-start -->

---

## 全文

# Software as a Medical Device: Possible Framework for Risk Categorization and Corresponding Considerations

**Document Number**: IMDRF/SaMD WG/N12FINAL:2014

**Source**: [https://www.imdrf.org/documents/software-medical-device-possible-framework-risk-categorization-and-corresponding-considerations](https://www.imdrf.org/documents/software-medical-device-possible-framework-risk-categorization-and-corresponding-considerations)

---

**IMDRF/SaMD WG/N12FINAL:2014**

**Final Document**

**Title:** “Software as a Medical Device”: Possible Framework for  
Risk Categorization and Corresponding Considerations  

**Authoring Group** : IMDRF Software as a Medical Device (SaMD) Working Group

**Date:** 18 September 2014

Jeffrey Shuren, IMDRF Chair

This document was produced by the International Medical Device Regulators Forum.   
There are no restrictions on the reproduction or use of this document; however,   
incorporation of this document, in part or in whole, into another document, or its   
translation into languages other than English, does not convey or represent an   
endorsement of any kind by the International Medical Device Regulators Forum.

Copyright © 2014 by the International Medical Device Regulators Forum.

**Table of Contents**

1.0 Introduction 4

2.0 Scope 5

3.0 Definitions 7

3.1 Software as a Medical Device 7

3.2 Intended use / Intended Purpose 7

3.3 Medical Purpose 7

3.4 SaMD Changes 9

4.0 SaMD Background and Aspects Influencing Patient Safety 9

5.0 Factors Important for SaMD Characterization 10

5.1 Significance of information provided by SaMD to healthcare decision 10

5.2 Healthcare Situation or Condition 11

6.0 SaMD Definition Statement 12

7.0 SaMD Categorization 13

7.1 Categorization Principles 13

7.2 SaMD Categories 14

7.3 Criteria for Determining SaMD Category 14

7.4 Examples of SaMD: 15

8.0 General Considerations for SaMD 20

8.1 Design and development 20

8.2 Changes 22

9.0 Specific Considerations for SaMD 23

9.1 Socio-technical environment considerations 23

9.2 Technology and system environment considerations 25

9.3 Information security with respect to safety considerations 26

10.0 Appendix 27

10.1 Clarifying SaMD Definition 27

10.2 Analysis of SaMD framework with existing classifications 29

11.0 References 30

**Preface**

The document herein was produced by the International Medical Device Regulators Forum (IMDRF), a voluntary group of global medical device regulators from around the world. The document has been subject to consultation throughout its development.

There are no restrictions on the reproduction, distribution or use of this document; however, incorporation of this document, in part or in whole, into any other document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the International Medical Device Regulators Forum.

# Introduction

Software is playing an increasingly important and critical role in healthcare with many clinical and administrative purposes. 

Software used in healthcare operates in a complex socio-technical environment—consisting of software, hardware, networks, and people—and frequently forms part of larger systems that must operate in a unified manner. This software frequently depends on other commercial off-the-shelf (COTS) software and on other systems and data repositories for source data. 

A subset of software used in healthcare meets the definition of a medical device; globally, regulatory authorities regulate such software accordingly.

Existing regulations for medical device software are largely focused on medical device software that is embedded in dedicated hardware medical devices and are focused around physical harm, transmission of energy and/or substances to or from the body, the degree of invasiveness to the body, closeness to sensitive organs, duration of use, diseases, processes and public health risk, competence of user and effect on population due to communicable diseases, etc.

Today, medical device software is often able to attain its intended medical purpose independent of hardware medical devices. It is increasingly being deployed on general-purpose hardware and delivered, in diverse care settings, on a multitude of technology platforms (e.g., personal computers, smart phones, and in the cloud) that are easily accessible. It is also being increasingly interconnected to other systems and datasets (e.g., via networks and over the Internet).

The complexity of medical device software, together with the increasing connectedness of systems, results in emergent behaviors not usually seen in hardware medical devices. 

This introduces new and unique challenges. For example:

  * Medical device software might behave differently when deployed to different hardware platforms. 
  * Often an update made available by the manufacturer is left to the user of the medical device software to install. 
  * Due to its non-physical nature (key differentiation), medical device software may be duplicated in numerous copies and widely spread, often outside the control of the manufacturer.

Furthermore, there are lifecycle aspects of medical device software that pose additional challenges. For instance, software manufacturers often:

  * Have rapid development cycles, 
  * Introduce frequent changes to their software, and
  * Deliver updates by mass and rapid distribution.

This document is focused on a selected subset of medical device software. This software is called _Software as a Medical Device_ (SaMD) and is defined in _IMDRF SaMD WG N10 / Software as a Medical Device: Key Definitions_.

![Information](data:image/jpeg;base64,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)| **Definition: Software as a Medical Device[1]**_SaMD is defined as software intended to be used for one or more medical purposes that perform these purposes without being part of a hardware medical device._  
---|---  

The objective of this document is to introduce a foundational approach, harmonized vocabulary and general and specific considerations for manufacturers, regulators, and users alike to address the unique challenges associated with the use of SaMD.

The approach developed in this document is intended only to establish a common understanding for SaMD and can be used as reference. This document is not intended to replace or modify existing regulatory classification schemes or requirements. Further efforts are required prior to the use of this foundational approach for possible regulatory purposes. 

# Scope

**Purpose of the document**

The purpose of the document is to introduce a foundational approach, harmonized vocabulary and general and specific considerations, for manufacturers, regulators, and users alike to address the unique challenges associated with the use of SaMD by;

  * Establishing common vocabulary and an approach for categorizing SaMD;
  * Identifying specific information for describing SaMD in terms of the significance of the information provided by the SaMD to the healthcare decision, healthcare situation or condition, and core functionality;
  * Providing criteria to categorize SaMD based on the combination of the significance of the information provided by the SaMD to the healthcare decision and the healthcare situation or condition associated with SaMD; and
  * Identifying appropriate considerations, during the lifecycle process (requirements, design, development, testing, maintenance and use) of SaMD.

**Field of application**

  * The categorization system in this document applies to SaMD defined in the related document, _IMDRF SaMD WG N10 / Software as a Medical Device: Key Definitions_ and does not address other types of software. 
  * Software intended as an accessory to a medical device (i.e., software that does not in itself have a medical purpose) is not in the scope of this document. 
  * This document focuses on the SaMD irrespective of software technology and/or the platform (e.g., mobile app, cloud, server).
  * This document does not address software that drives or controls a hardware medical device.

**Relationship to other regulatory classification and standards[2]**

  * This document is not intended to replace or create new risk management practices rather it uses risk management principles (e.g., principles in international standards) to identify generic risks for SaMD. 
  * The categorization framework in this document is not a regulatory classification, nor implies a convergence of classifications rules. However, it does set a path towards common vocabulary and approach. Additional work is required to align existing classification rules with this framework.
  * The categorization framework is not meant to replace or conflict with the content and/or development of technical or process standards related to software risk management activities.

# Definitions

## Software as a Medical Device

The term “Software as a Medical Device” (SaMD) _is defined as software intended to be used for one or more medical purposes that perform these purposes without being part of a hardware medical device._

_NOTES:_

  * _SaMD is a medical device and includes in-vitro diagnostic (IVD) medical device._
  * _SaMD is capable of running on general purpose (non-medical purpose) computing platforms.[3] _
  * _“without being part of” means software not necessary for a hardware medical device to achieve its intended medical purpose._
  * _Software does not meet the definition of SaMD if its intended purpose is to drive a hardware medical device._
  * _SaMD may be used in combination (e.g., as a module) with other products including medical devices._
  * _SaMD may be interfaced with other medical devices, including hardware medical devices and other SaMD software, as well as general purpose software._
  * _Mobile apps that meet the definition above are considered SaMD._

## Intended use / Intended Purpose

For SaMD intended use, the definition in GHTF/SG1/N70:2011 “Label and Instructions for Use for Medical Devices” applies:

_The term “intended use / intended purpose” is the objective intent of the manufacturer regarding the use of a product, process or service as reflected in the specifications, instructions and information provided by the manufacturer._

## Medical Purpose 

The following two terms as defined in GHTF/SG1/N71:2012 “Definition of the Terms ‘Medical Device’ and ‘In Vitro Diagnostic (IVD) Medical Device” (_italicized below_) identify medical purpose applicable to SaMD:

### Medical Device

 _‘Medical device’ means any instrument, apparatus, implement, machine, appliance, implant, reagent for in vitro use, software, material or other similar or related article, intended by the manufacturer to be used, alone or in combination, for human beings, for one or more of the specific medical purpose(s) of:_

  * _diagnosis, prevention, monitoring, treatment or allevi­ation of disease,_
  * _diag­nosis, monitoring, treatment, alleviation of or com­pensation for an injury,_
  * _inves­tigation, replacement, modification, or support of the anatomy or of a physiologi­cal process,_
  * _supporting or sustaining life,_
  * _con­trol of conception,_
  * _disinfection of medical devices,_
  * _providing information by means of in vitro examination of specimens derived from the human body;_

_and does not achieve its primary intended action by pharmaco­logical, immunological or metabolic means, in or on the human body, but which may be assisted in its intended function by such means._

**_Note:_**_Products which may be considered to be medical devices in some jurisdictions but not in others include:_

  * _disinfection substances,_
  * _aids for persons with disabilities,_
  * _devices incorporating animal and/or human tissues,_
  * _devices for in vitro fertilization or assisted reproduction technologies._

### In Vitro Diagnostic (IVD) Medical Device

 _‘In Vitro Diagnostic (IVD)_**__**_medical device’ means a medical device, whether used alone or in combination, intended by the manufacturer for the in-vitro examination of specimens derived from the human body solely or principally to provide information for diagnostic, monitoring or compatibility purposes._

**_Note 1:_**_IVD medical devices include reagents, calibrators, control materials, specimen receptacles, software, and related instruments or apparatus or other articles and are used, for example, for the following test purposes: diagnosis, aid to diagnosis, screening, monitoring, predisposition, prognosis, prediction, determination of physiological status._

**_Note2:_**_In some jurisdictions, certain IVD medical devices may be covered by other regulations._

### Additional considerations for SaMD 

_SaMD may also:_

  * _Provide means and suggestions for mitigation of a disease._
  * _Provide information for determining compatibility, detecting, diagnosing, monitoring or treating physiological conditions, states of health, illnesses or congenital deformities._
  * _Aid to diagnosis, screening, monitoring, determination of predisposition; prognosis, prediction, determination of physiological status._

## SaMD Changes

 _SaMD changes refer to any modifications made throughout the lifecycle of the SaMD including the maintenance phase._

_Software maintenance[4] can include adaptive (e.g. keeps pace with the changing environment), perfective (e.g. recoding to improve software performance), corrective (e.g., corrects discovered problems), or preventive (e.g., corrects latent faults in the software product before they become operational faults)._**__**

_Examples of SaMD changes include, but are not limited to, defect fixes; aesthetic, performance or usability enhancements; and security patches._

# SaMD Background and Aspects Influencing Patient Safety 

There are many aspects in an ever-increasing complex clinical use environment that can raise or lower the potential to create hazardous situations to patients. Some examples of these aspects include:

  * The type of disease or condition 
  * Fragility of the patient with respect to the disease or condition
  * Progression of the disease or the stage of the disease/condition
  * Usability of the application
  * Designed towards a specific user type
  * Level of dependence or reliance by the user upon the output information
  * Ability of the user to detect an erroneous output information
  * Transparency of the inputs, outputs and methods to the user
  * Level of clinical evidence available and the confidence on the evidence
  * The type of output information and the level of influence on the clinical intervention
  * Complexity of the clinical model used to derive the output information
  * Known specificity of the output information
  * Maturity of clinical basis of the software and confidence in the output
  * Benefit of the output information vs. baseline 
  * Technological characteristics of the platform the software are intended to operate on
  * Method of distribution of the software 

Although many of these aspects may affect the importance of the output information from SaMD, only some of these aspects can be identified by the intended use of SaMD. Generally these aspects can be grouped into the following two major factors that provide adequate description of the intended use of SaMD:

  1. Significance of the information provided by the SaMD to the healthcare decision, and 
  2. State of the healthcare situation or condition. 

When these factors are included in the manufacturer’s description of intended use, they can be used to categorize SaMD. 

Section 6.0 provides a structured approach for a SaMD definition statement to describe the intended use. Section 7.0 provides a method for categorizing SaMD based on the major factors identified in the definition statement.

Other aspects that are not included in the two major factors (e.g., transparency of the inputs used, technological characteristics used by particular SaMD, etc.), although still important, do not influence the determination of the category of SaMD. These other aspects influence the identification of considerations that are unique to a specific approach/method used by the manufacturer of a particular category of SaMD. For example, the type of a platform, that is constantly changing, used in the implementation of SaMD may create considerations that are unique to that implementation. These considerations can also vary by the capabilities of the manufacturer or by the process rigor used to implement the SaMD. Appropriate considerations of these aspects by the manufacturers, users and other stakeholders can significantly minimize patient safety risks. 

Section 8.0 provides general considerations and section 9.0 provides specific considerations that when taken into account can promote safety in the creation, implementation and use of SaMD.

# Factors Important for SaMD Characterization

## Significance of information provided by SaMD to healthcare decision

The intended use of the information provided by SaMD in clinical management has different significance on the action taken by the user. 

### To treat or to diagnose 

Treating and diagnosing infers that the information provided by the SaMD will be used to take an immediate or near term action:

  * To treat/prevent or mitigate by connecting to other medical devices, medicinal products, general purpose actuators or other means of providing therapy to a human body 
  * To diagnose/screen/detect a disease or condition (i.e., using sensors, data, or other information from other hardware or software devices, pertaining to a disease or condition).

### To drive clinical management 

Driving clinical management infers that the information provided by the SaMD will be used to aid in treatment, aid in diagnoses, to triage or identify early signs of a disease or condition will be used to guide next diagnostics or next treatment interventions:

  * To aid in treatment by providing enhanced support to safe and effective use of medicinal products or a medical device.
  * To aid in diagnosis by analyzing relevant information to help predict risk of a disease or condition or as an aid to making a definitive diagnosis.
  * To triage or identify early signs of a disease or conditions.

### To Inform clinical management 

Informing clinical management infers that the information provided by the SaMD will not trigger an immediate or near term action:

  * To inform of options for treating, diagnosing, preventing, or mitigating a disease or condition.
  * To provide clinical information by aggregating relevant information (e.g., disease, condition, drugs, medical devices, population, etc.)

## Healthcare Situation or Condition

### Critical situation or condition

Situations or conditions where accurate and/or timely diagnosis or treatment action is vital to avoid death, long-term disability or other serious deterioration of health of an individual patient or to mitigating impact to public health. SaMD is considered to be used in a critical situation or condition where:

  * The type of disease or condition is:
    * Life-threatening state of health, including incurable states, 
    * Requires major therapeutic interventions, 
    * Sometimes time critical, depending on the progression of the disease or condition that could affect the user’s ability to reflect on the output information. 
  * Intended target population is fragile with respect to the disease or condition (e.g., pediatrics, high risk population, etc.) 
  * Intended for specialized trained users.

### Serious situation or condition

Situations or conditions where accurate diagnosis or treatment is of vital importance to avoid unnecessary interventions (e.g., biopsy) or timely interventions are important to mitigate long term irreversible consequences on an individual patient’s health condition or public health. SaMD is considered to be used in a serious situation or condition when:

  * The type of disease or condition is:
    * Moderate in progression, often curable, 
    * Does not require major therapeutic interventions, 
    * Intervention is normally not expected to be time critical in order to avoid death, long-term disability or other serious deterioration of health, whereby providing the user an ability to detect erroneous recommendations. 
  * Intended target population is NOT fragile with respect to the disease or condition. 
  * Intended for either specialized trained users or lay users. 

Note: SaMD intended to be used by lay users in a "serious situation or condition" as described here, without the support from specialized professionals, should be considered as SaMD used in a "critical situation or condition".

### Non-Serious situation or condition

Situations or conditions where an accurate diagnosis and treatment is important but not critical for interventions to mitigate long term irreversible consequences on an individual patient's health condition or public health. SaMD is considered to be used in a non-serious situation or condition when:

  * The type of disease or condition is:
    * Slow with predictable progression of disease state (may include minor chronic illnesses or states), 
    * May not be curable; can be managed effectively, 
    * Requires only minor therapeutic interventions, and 
    * Interventions are normally noninvasive in nature, providing the user the ability to detect erroneous recommendations. 
  * Intended target population is individuals who may not always be patients. 
  * Intended for use by either specialized trained users or lay users. 

# SaMD Definition Statement 

The intended use of SaMD is normally reflected in various sources such as the manufacturer’s specifications, instructions, and other information provided by the manufacturer. 

The purpose of the SaMD definition statement and the components identified below are to provide an organized factual framework. Statement “A” and “B” are to help the SaMD developer determine the SaMD category in the categorizing framework, while statement “C” is to help the manufacturer manage changes to SaMD that may result in change of the category and to address considerations specific to SaMD. 

The SaMD definition statement should include a clear and strong statement about intended use, including the following:

  1. The “**significance of the information provided by the SaMD to the healthcare decision** ” which identifies the intended medical purpose of the SaMD. The statement should explain how the SaMD meets one or more of the purposes described in the definition of a medical device[5], e.g. supplying information for diagnosis, prevention, monitoring, treatment etc.**This statement should be structured in the following terms as defined in section 5.1.**
     * Treat or diagnose 
     * Drive clinical management 
     * Inform clinical management 
  2. The “**state of the healthcare situation or condition** ” that the SaMD is intended for. **This statement should be structured in the following terms as defined in section 5.2.**
     * Critical situation or condition
     * Serious situation or condition
     * Non-serious situation or condition
  3. **Description of the SaMD’s core functionality**[6] which identifies the critical features/functions of the SaMD that are essential to the intended significance of the information provided by the SaMD to the healthcare decision in the intended healthcare situation or condition. This description should include only the critical features. (See applicability of this in section 8.0, 9.0).

# SaMD Categorization 

This section provides an approach to categorize SaMD based on the factors identified in the SaMD definition statement. 

## Categorization Principles

The following are necessary principles important in the categorization approach of SaMD.

  * The categorization relies on an accurate and complete SaMD definition statement.
  * The determination of the categories is the combination of the significance of the information provided by the SaMD to the healthcare decision and the healthcare situation or condition.
  * The four categories (I, II, III, IV) are based on the levels of impact on the patient or public health where accurate information provided by the SaMD to treat or diagnose, drive or inform clinical management is vital to avoid death, long-term disability or other serious deterioration of health, mitigating public health.
  * The categories are in relative significance to each other. Category IV has the highest level of impact, Category I the lowest.
  * When a manufacturer's SaMD definition statement states that the SaMD can be used across multiple healthcare situations or conditions it is categorized at the highest category according to the information included in the SaMD definition statement.
  * When a manufacturer makes changes to SaMD[7], during the lifecycle that results in the change of the definition statement, the categorization of SaMD should be reevaluated appropriately. The SaMD is categorized according to the information included in the changed (new) SaMD definition statement. 
  * SaMD will have its own category according to its SaMD definition statement even when a SaMD is interfaced with other SaMD, other hardware medical devices, or used as a module in a larger system. 

## SaMD Categories

State of Healthcare situation or condition| Significance of information provided by SaMD to healthcare decision  
---|---  
Treat or diagnose| Drive clinical management| Inform clinical management  
Critical| IV| III| II  
Serious| III| II| I  
Non-serious| II| I| I  

## Criteria for Determining SaMD Category

**Criteria for Category IV –**

  1. SaMD that provides information to treat or diagnose a disease or conditions in a critical situation or condition is a Category IV and is considered to be of very high impact.

**Criteria for Category III –**

  1. SaMD that provides information to treat or diagnose a disease or conditions in a serious situation or condition is a Category III and is considered to be of high impact.
  2. SaMD that provides information to drive clinical management of a disease or conditions in a critical situation or condition is a Category III and is considered to be of high impact.

**Criteria for Category II –**

  1. SaMD that provides information to treat or diagnose a disease or conditions in a non-serious situation or condition is a Category II and is considered to be of medium impact.
  2. SaMD that provides information to drive clinical management of a disease or conditions in a serious situation or condition is a Category II and is considered to be of medium impact.
  3. SaMD that provides information to inform clinical management for a disease or conditions in a critical situation or condition is a Category II and is considered to be of medium impact.

**Criteria for Category I –**

  1. SaMD that provides information to drive clinical management of a disease or conditions in a non-serious situation or condition is a Category I and is considered to be of low impact.
  2. SaMD that provides information to inform clinical management for a disease or conditions in a serious situation or condition is a Category I and is considered to be of low impact.
  3. SaMD that provides information to inform clinical management for a disease or conditions in a non-serious situation or condition is a Category I and is considered to be of low impact.

##  Examples of SaMD:

The examples below are intended to help illustrate the application of the framework and resulting categories. 

**Category IV:**

  * SaMD that performs diagnostic image analysis for making treatment decisions in patients with acute stroke, i.e., where fast and accurate differentiation between ischemic and hemorrhagic stroke is crucial to choose early initialization of brain-saving intravenous thrombolytic therapy or interventional revascularization. 

_This example uses criteria IV.i from Section 7.3 in that the information provided by the above SaMD is used to treat a fragile patient in a critical condition that is life threatening, may require major therapeutic intervention, and is time sensitive._

  * SaMD that calculates the fractal dimension of a lesion and surrounding skin and builds a structural map that reveals the different growth patterns to provide diagnosis or identify if the lesion is malignant or benign.****

_This example uses criteria IV.i from Section 7.3 in that the information provided by the above SaMD is used to diagnose a disease that may be life threatening, may require major therapeutic intervention, and may be time sensitive._

  * SaMD that performs analysis of cerebrospinal fluid spectroscopy data to diagnose tuberculosis meningitis or viral meningitis in children.

_This example uses criteria IV.i from Section 7.3 in that the information provided by the above SaMD is used to diagnose a disease in a fragile population with possible broader public health impact that may be life threatening, may require major therapeutic intervention, and may be time sensitive._

  * SaMD that combines data from immunoassays to screen for mutable pathogens/pandemic outbreak that can be highly communicable through direct contact or other means.

_This example uses criteria IV.i from Section 7.3 in that the information provided by the above SaMD is used to screen for a disease or condition with public health impact that may be life threatening, may require therapeutic intervention and may be time critical._

**Category III:**

  * SaMD that uses the microphone of a smart device to detect interrupted breathing during sleep and sounds a tone to rouse the sleeper.

_This example uses criteria III.i from Section 7.3 in that the information provided by the above SaMD is used to treat a condition where intervention is normally not expected to be time critical in order to avoid death, long term disability or other serious deterioration of health._

  * SaMD that is intended to provide sound therapy to treat, mitigate or reduce effects of tinnitus for which minor therapeutic intervention is useful.

_This example uses criteria III.i from Section 7.3 in that the information provided by the above SaMD is used to treat a condition that may be moderate in progression, may not require therapeutic intervention and whose treatment is normally not expected to be time critical._

  * SaMD that is intended as a radiation treatment planning system as an aid in treatment by using information from a patient and provides specific parameters that are tailored for a particular tumor and patient for treatment using a radiation medical device.

_This example uses criteria III.ii from Section 7.3 in that the information provided by the above SaMD is used as an aid in treatment by providing enhanced support to the safe and effective use of a medical device to a patient in a critical condition that may be life threatening and requires major therapeutic intervention._

  * SaMD that uses data from individuals for predicting risk score in high-risk population for developing preventive intervention strategies for colorectal cancer. 

_This example uses criteria III.ii from Section 7.3 in that the information provided by the above SaMD is used to detect early signs of a disease to treat a condition that may be life-threatening disease impacting high-risk populations, may require therapeutic intervention and may be time critical._

  * SaMD that is used to provide information by taking pictures, monitoring the growth or other data to supplement other information that a healthcare provider uses to diagnose if a skin lesion is malignant or benign.

_This example uses criteria III.ii from Section 7.3 in that the information provided by the above SaMD is used as an aid to diagnosing a condition that may be life-threatening, may require therapeutic intervention and may be time critical by aggregating relevant information to detect early signs of a disease._

**Category II:**

  * SaMD that analyzes heart rate data intended for a clinician as an aid in diagnosis of arrhythmia.

_This example uses criteria from II.ii Section 7.3 in that the information provided by the above SaMD is used to aid in the diagnosis of a disease of a condition that may be moderate in progression, may not require therapeutic intervention and whose treatment is normally not expected to be time critical._

  * SaMD that interpolates data to provide 3D reconstruction of a patient’s computer tomography scan image, to aid in the placement of catheters by visualization of the interior of the bronchial tree; in lung tissue; and placement of markers into soft lung tissue to guide radiosurgery and thoracic surgery.

_This example uses criteria II.ii from Section 7.3 in that the information provided by the above SaMD is used to aid in the next treatment intervention of a patient where the intervention is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD that uses data from individuals for predicting risk score for developing stroke or heart disease for creating prevention or interventional strategies. 

_This example uses criteria II.iii from Section 7.3 in that the information provided by the above SaMD is used to detect early signs of a disease to treat a condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD that integrates and analyzes multiple tests utilizing standardized rules to provide recommendations for diagnosis in certain clinical indications, e.g., kidney function, cardiac risk, iron and anemia assessment. 

_This example uses criteria II.ii from Section 7.3 in that the information provided by the above SaMD is used to detect early signs of a disease to treat a condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

_Note: This example includes both serious and potentially non-serious conditions but per the categorization principle in Section 7.1 when a manufacturer’s SaMD definition statement states that the SaMD can be used across multiple healthcare situations or condition it will be categorized at the highest category according to the SaMD definition statement._

  * SaMD that helps diabetic patients by calculating bolus insulin dose based on carbohydrate intake, pre-meal blood glucose, and anticipated physical activity reported to adjust carbohydrate ratio and basal insulin. 

_This example uses criteria II.ii from Section 7.3 in that the information provided by the above SaMD is used to aid in treatment of a condition not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

**Category I:**

  * SaMD that sends ECG rate, walking speed, heart rate, elapsed distance, and location for an exercise-based cardiac rehabilitation patient to a server for monitoring by a qualified professional.

_This example uses criteria I.ii from Section 7.3 in that the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD that collects data from peak-flow meter and symptom diaries to provide information to anticipate an occurrence of an asthma episode**.**

_This example uses criteria I.ii from Section 7.3 in that the information provided by the above SaMD is an aggregation of data to provide best option to mitigate a condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD that analyzes images, movement of the eye or other information to guide next diagnostic action of astigmatism. 

_This example uses criteria I.i from Section 7.3 in that the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that even if not curable can be managed effectively and whose interventions are normally noninvasive in nature._

  * SaMD that uses data from individuals for predicting risk score (functionality) in healthy populations for developing the risk (medical purpose) of migraine (non-serious condition.

_This example uses criteria I.i from Section 7.3 in that the the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that even if not curable can be managed effectively and whose interventions are normally noninvasive in nature._

  * SaMD that collects output from a ventilator about a patient's carbon dioxide level and transmits the information to a central patient data repository for further consideration.

_This example uses criteria I.ii from Section 7.3 in that the the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD that stores historical blood pressure information for a health care provider's later review.

_This example uses criteria I.ii from Section 7.3 in that the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD intended for image analysis of body fluid preparations or digital slides to perform cell counts and morphology reviews.

_This example uses criteria I.ii from Section 7.3 in that the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD intended for use by elderly patients with multiple chronic conditions that receives data from wearable health sensors, transmits data to the monitoring server, and identifies higher-level information such as tachycardia and signs of respiratory infections based on established medical knowledge and communicates this information to caregivers.

_This example uses criteria I.ii from Section 7.3 in that the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

  * SaMD that uses hearing sensitivity, speech in noise, and answers to a questionnaire about common listening situations to self-assess for hearing loss.

_This example uses criteria from I.ii Section 7.3 in that the information provided by the above SaMD is an aggregation of data to provide clinical information that will not trigger an immediate or near term action for the treatment of a patient condition that is not normally expected to be time critical in order to avoid death, long-term disability, or other serious deterioration of health._

# General Considerations for SaMD

SaMD often forms part of a clinical workflow sequence in order to improve diagnosis, treatment and patient management. However, issues with the design and/or implementation of SaMD into a workflow can lead to users making incorrect choices / decisions and can cause delays in decisions being made - this may lead to adverse consequences for patients. 

Developing SaMD that are safe entails identifying risks and establishing measures that give confidence that the risks are acceptable. It is generally accepted that testing of software is not sufficient to determine that it is safe in operation. As a consequence, it is recognized that confidence should be built into software in order to assure its safety.

IEC 62304 is a standard for life-cycle development of medical device software. The standard specifies a risk-based decision model, defines some testing requirements, and highlights three major principles that promote safety relevant to SaMD: 

  * Risk management;
  * Quality management; and
  * Methodical and systematic systems engineering according to best industry practices.

The combination of these concepts allows SaMD manufacturers to follow a clearly structured and consistently repeatable decision-making process to promote safety for SaMD.

Further information on these major principles is provided below followed by discussion on some specific considerations in the areas of:

  * Socio-technical environment
  * Technology and system environments
  * Information security with respect to safety

## Design and development

Manufacturers should select and implement an adequate process for the planning, design, development, deployment, and documenting of robust and dependable software commensurate with risk—as informed by its intended purpose, reasonable foreseeable use, and the understood and defined socio-technical environment of use.

![Information](data:image/jpeg;base64,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)| _Safety needs to be addressed early in the design and development process._  
---|---  

Development of software in a quality-assured manner should consider the appropriate selection and implementation of system design and development methods that: 

  * Include a methodical and systematic development process using models, methods, architecture, and design-modelling techniques appropriate for the development language(s) and the device’s intended purpose, 
  * Cover the various software lifecycle stages through the application of software development standards, e.g., IEC 62304, and use of software engineering guidebooks, e.g., SWEBoK guide, SEBoK guide, and
  * Systematically and methodically document the design and development process (using tools as appropriate.)

### Post Market Surveillance

Software risks can never be totally eliminated so SaMD manufacturers should continually monitor customer issues to maintain the safety level. A monitoring process should include ways to capture customer feedback, e.g., through inquiries, complaints, market studies, focus groups, servicing, etc. The inherent nature of software including SaMD allows for efficient methods to understand and capture user experiences. It is recommended that SaMD manufacturers utilize these feedback techniques to understand failure modes and perform analysis to address safety situations. It is also recommended that SaMD manufacturers extend their monitoring to automatically detect errors of the software or system, i.e., discover and recover from an error before a failure can occur.

General considerations associated with the monitoring of SaMD include:

  1. Due to its non-physical nature, a SaMD may be duplicated and numerous copies and widely spread, often outside the control of the manufacturer.
  2. Often an update made available by the manufacturer is left to the user of the SaMD to install. Manufacturers should make sure that appropriate mitigations address any risks that arise from the existence of different versions of the SaMD on the market. 
  3. Incident investigations should consider any specific case or combination of use cases that may have contributed to the failure and as appropriate manufacturers should consider accident reconstruction principles, e.g., data logging, black box recorder, etc.[8]

## Changes

Manufacturers of SaMD are expected to have an appropriate level of control to manage changes. Due to the non-physical nature of software, a software change management process needs specific considerations to achieve the intended result regarding traceability and documentation.

These specific considerations include:

  * Socio-technical environment considerations
  * Technology and system environment considerations
  * Information security with respect to safety considerations

![Information](data:image/jpeg;base64,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)|  _SaMD changes may have a significant unforeseeable effect on the healthcare situation or condition and socio-technical environment of use if not managed systematically, not only with respect to a design change in itself, but also to the impact of the changed software after it is installed and implemented._  
---|---  

With any product lifecycle, change is inevitable. Failures occur and may be due to errors, ambiguities, oversights or misinterpretation of the specification that the software is intended to satisfy, carelessness or incompetence in writing code, inadequate testing, incorrect or unexpected usage of the software or other unforeseen problems. An SaMD may also fail with changes to the running environment. Changes to SaMD or its operating environment can affect its safety, quality and performance.

SaMD changes refer to any modifications made throughout the lifecycle of the SaMD including the maintenance phase. The nature of software maintenance changes can include adaptive (e.g. keeps pace with the changing environment), perfective (e.g. recoding to improve software performance), corrective (e.g. corrects discovered problems), or preventive changes (e.g. corrects latent faults in the software product before they become operational faults). These changes should be clearly identified and defined with a method of tracing the change to the specific affected software.

In order to effectively manage the changes and their impact, manufacturers must perform a risk assessment to determine if the change(s) affect the SaMD categorization and the core functionality of the SaMD as outlined in the definition statement.

Changes should undergo appropriate verification and validation before being released by the manufacturer for use.

Examples of software changes (some may be considered significant and others not):

  * Modification to an algorithm affecting the diagnosis or therapy delivered;
  * A software change that affects the way data is read or interpreted by the user, such that the treatment or diagnosis of the patient may be altered when compared to the previous version of the software;
  * Addition of a new feature to the software that may change the diagnosis or therapy delivered to the patient;
  * A software change that incorporates a change to the operating system or change to the configuration on which the SaMD runs;
  * A software change that affects clinical workflow.

# Specific Considerations for SaMD

## Socio-technical environment considerations

The term socio-technical environment concerns the SaMD's setting of use - often comprising hardware, networks, software, and people. More formally, it may be characterized into spatial (e.g., location), activity (e.g., workflow), social (e.g., responsibility), technological (e.g., devices, systems, data sources, and connections), and physical (e.g., ambient conditions) components[9]. 

SaMD supplies information and/or a structure for information. 

![Information](data:image/jpeg;base64,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)| _The proper and safe functioning of SaMD is highly dependent on a sufficient and common understanding of the socio-technical environment that includes the manufacturer and the user._  
---|---  

Manufacturers should be aware of the socio-technical environment where inadequate considerations could lead to incorrect, inaccurate, and/or delayed diagnoses and treatments; and/or additional cognitive workload (which may, over time, make clinicians more susceptible to making mistakes)[10]. 

Similarly, users should also be aware of the socio-technical environment as presumed and designed for (limitations of the SaMD’s capabilities) and by the manufacturer, as not being aware may lead to overreliance or other inaccurate use of the SaMD.

For example:

  * If the user does not have sufficient skills and expertise for correct operation of the SaMD, possible inaccurate output data may not be questioned. The same may happen if the user becomes habituated and over-reliant on SaMD over time.
  * The introduction of SaMD sometimes changes clinical workflows in unanticipated ways; these changes may be detrimental to patient safety. 
  * The user may seek alternate pathways to achieve a particular functionality, otherwise called a  _workaround_. When workarounds circumvent built-in safety features of a product, patient safety may be compromised. 

Considerations for the manufacturer when identifying effects/implications and appropriate measures to safety and performance of SaMD throughout the product's design, development, and installation: 

  * Transparency of information on limitations with algorithms, clinical model, quality of data used to build the models, assumptions made, etc. can help users question the validity of output of the SaMD and avoid making incorrect or poor decisions;
  * Integrating SaMD within real-world clinical workflows (including sufficient involvement of users from all relevant disciplines) requires attention to _in situ_ use and tasks to ensure appropriate use of safety features; 
  * SaMD (and other systems connected to the SaMD) may be configured by the user in different ways than intended or foreseen by the manufacturer; 
  * Though not specific to SaMD, design of the user interface including: whether designs are overly complex (e.g., multiple, complicated screens), the appropriateness of designs for the target platform (e.g., smart phone screen versus desktop monitor), the dynamic nature of data (e.g., showing information at appropriate times and for an appropriate duration); 
  * Though not specific to SaMD, identification of appropriate means to display information such that it is understood by the intended user (e.g., usability including regionalization parameters, language translation, and selection/display of units);
  * Communicating relevant information to the user (based on the activities conducted above) for the purpose of:
    * Enabling the user to decide whether or not the user can use the device in the organization in terms of available hardware, competence, network, required quality for data input. And, if he/she decides to do this, information necessary to do those measures in order to use it: inform users, establish different routines, obtain necessary hardware.
    * Enabling correct installation and configuration of SaMD for appropriate integration with clinical workflows.

## Technology and system environment considerations

Technology and system environment refers to the ecosystem where the SaMD resides, including installed systems, interconnections, and hardware platform(s). Instructions on how to verify the appropriateness of installation of and update to SaMD as well as any changes made to the system environment (e.g., hardware and software) should be provided to the user. Reliance on hardware over which the manufacturer does not have control (operating systems not designed for a medical purpose, general-purpose hardware, networks and servers, Internet, links) should be considered and addressed by the manufacturer during design and development of SaMD (for instance, by designing robust and resilient SaMD designs).

![Information](data:image/jpeg;base64,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)| _SaMDs are always dependant on a hardware platform and often a connected environment. SaMD can be affected by cross-link interconnections – both physical connections and interoperability, i.e., the seamless communication between devices, technology and people._  
---|---  

Disruption in the ecosystem (e.g., resulting from service disruptions, systems maintenance or upgrades, platform failures) can result in loss of information, delayed, corrupted, or mixed patient information, or inaccurate information which may lead to incorrect or inaccurate diagnoses and/or treatments. 

For example: an incorrect diagnosis is made after the connection to a clinical dataset was lost because the patient diagnosis data is not available. 

Considerations for the manufacturer when identifying effects/implications to safety and performance of SaMD:

  * Connections to other systems (e.g., reliability of the connection, resilience, quality of service, access, security, load capacity of connections to other systems and connection methods, system integration)
  * Presenting information to the users and system integrators about the system requirements and resultant performance of the SaMD (e.g., the effect that changes to firewall rules might have on the operation of the system)
  * Hardware platform(s)—such as smart phones, PC, servers—(e.g., reliability, dependencies, and interconnections with others hardware and software);
  * Operating system(s) platform—such as Windows, GNU/Linux—compatibility; and
  * Modifications and changes to the SaMD integration (e.g., platform updates) may have effects on SaMD that the manufacturer did not anticipate/foresee. 

## Information security with respect to safety considerations

 _Information security_ may be defined as the preservation of confidentiality, integrity and availability of information[11].

![Information](data:image/jpeg;base64,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)| _Incorrect management or transmission of information by an SaMD can lead to incorrect or delayed diagnosis or treatment._  
---|---  

SaMD may be affected by particular factors relating to information security that may affect the integrity, availability, or accessibility of information output from the SaMD needed for correct diagnosis or treatment:

  * SaMD are typically used by a variety of users with different access needs, e.g., restricted access or varying information security requirements
  * Platforms where a SaMD is installed typically runs many other software applications.
  * SaMD are typically connected to the Internet, networks, databases, or servers with varying information security requirements.

Considerations for the manufacturer when identifying implications for safety and performance of SaMD:

  * The SaMD information security and privacy control requirements may need to be balanced with the need for timely information availability.
  * Information security requires the identification and implementation of safe (and formalized) ways to store, convert and/or transmit data. 
  * The design should use appropriate control measures to address data integrity when common information is accessed by multiple applications and users. 
  * Manufacturers should make it feasible for users to safely implement information security updates.
  * The protection of sensitive information requires support for sufficient access control and appropriate restriction to system settings and assets for important data.
  * The design should address possible adverse system interactions with the inclusion of appropriate resilience and robustness measures.
  * Instructions for users related to information security should include how to safely:
    * Install SaMD in appropriate operating environments (e.g., OS, integration of other software); 
    * Manage authentication mechanisms; and
    * Update security software/spyware, operating environments, and other systems and applications, etc.

# Appendix

##  Clarifying SaMD Definition

This Appendix provides a representative list of features and functionalities that either meet or don’t meet the definition of SaMD. This list is not exhaustive; it is only intended to provide clarity and assistance in identifying when a feature or functionality is considered to be SaMD.

**_Examples of software that are SaMD:_**

  * Software with a medical purpose that operates on a general purpose computing platform, i.e., a computing platform that does not have a medical purpose, is considered SaMD. For example, software that is intended for diagnosis of a condition using the tri-axial accelerometer that operates on the embedded processor on a consumer digital camera is considered a SaMD.
  * Software that is connected to a hardware medical device but is not needed by that hardware medical device to achieve its intended medical purpose is SaMD and not an accessory to the hardware medical device. For example, software that allows a commercially available smartphone to view images for diagnostic purposes obtained from a magnetic resonance imaging (MRI) medical device is SaMD and not an accessory to MRI medical device. 
  * The SaMD definition notes states that “SaMD is capable of running on general purpose (non-medical purpose) computing platforms.” SaMD running on these general purpose computing platform could be located in a hardware medical device, For example, software that performs image post-processing for the purpose of aiding in the detection of breast cancer (CAD - computer-aided detection software) running on a general purpose computing platform located in the image-acquisition hardware medical device is SaMD.
  * The SaMD definition notes states that “SaMD may be interfaced with other medical devices, including hardware medical devices and other SaMD software, as well as general purpose software.” Software that provides parameters that become the input for a different hardware medical device or other SaMD is SaMD. For example, treatment planning software that supplies information used in a linear accelerator is SaMD.

**_Examples of software that are not SaMD:_**

  * The SaMD definition states “SaMD is defined as software intended to be used for one or more medical purposes that perform these purposes without being part of a hardware medical device”. Examples of software that are considered “part of” include software used to “drive or control” the motors and the pumping of medication in an infusion pump; or software used in closed loop control in an implantable pacemaker or other types of hardware medical devices. These types of software, sometimes referred to as “embedded software”, “firmware”, or “micro-code” are, not SaMD”. 
  * Software required by a hardware medical device to perform the hardware’s medical device intended use is not SaMD even if/when sold separately from the hardware medical device. 
  * Software that relies on data from a medical device, but does not have a medical purpose, e.g., software that encrypts data for transmission from a medical device is not SaMD. 
  * Software that enables clinical communication and workflow including patient registration, scheduling visits, voice calling, video calling is not SaMD.
  * Software that monitors performance or proper functioning of a device for the purpose of servicing the device, e.g., software that monitors X-Ray tube performance to anticipate the need for replacement; or software that integrates and analyzes laboratory quality control data to identify increased random errors or trends in calibration on IVDs is not SaMD. 
  * Software that provides parameters that become the input for SaMD is not SaMD if it does not have a medical purpose. For example, a database including search and query functions by itself or when used by SaMD is not SaMD.

## Analysis of SaMD framework with existing classifications 

This Annex is intended to clarify the following: 

**A – Categorization of SaMD relative to medical device classification**

There are different classification schemes for different purposes. 

Typically classification is based on a set of parameters/questions that assigns the object of interest into groups that suit a certain purpose.

Classifications may have the purpose to determine, for example

  * Appropriate levels of regulatory oversight such as requirements for
    * Levels of third party intervention 
    * Levels of conformity controls
    * Levels of quality system
  * Appropriate levels of technical measures, for example
    * Technical protective means, e.g., for
      * Laser protection 1,2 or 3
      * electrical isolation, protective earth or double insulated
      * ingress of liquids, IP XX

Classification of medical devices is commonly focused on regulatory controls based on risk classes. 

Categorization for SaMD, as in the case of laser protection, is only identifying different categories of SaMD by level of impact. Categorization in this document by itself does not imply regulatory controls needed to manage risks. It is only intended to provide guidance for appropriate considerations for SaMD**.**

**B - Relationship between this document and GHTF documents.**

It is important to note the following to understand the relationship between the categorization framework in this document and the classification principles for medical devices and in vitro diagnostic medical devices:

  * GHTF classification principles, unlike this document, were intended to build classification rules for regulatory control purposes. As explained earlier, this document identifies different categories of SaMD by level of impact and does not address corresponding regulatory risk classes identified in GHTF documents. 
  * The high-level principles used for identifying SaMD categories build substantially on the principles (rationale) underlying the classification rules established in the GHTF classification principles documents. Key factors like individual risks, public health risks, user skills, and importance of the information provided are common to both frameworks. 

#  References

IMDRF SaMD WG N10 / Software as a Medical Device: Key Definitions

GHTF/SG1/N70:2011 “Label and Instructions for Use for Medical Devices” 

GHTF/SG1/N71:2012 “Definition of the Terms ‘Medical Device’ and ‘In Vitro Diagnostic (IVD) Medical Device” 

IEC 62304:2006 - Medical device software -- Software life cycle processes

ISO/IEC 14764:2006 Software Engineering — Software Life Cycle Processes — Maintenance 

Guide to the Software Engineering Body of Knowledge - SWEBOK (2004), pp. 1-202 by Alain Abran, Pierre Bourque, Robert Dupuis, James W. Moore, Leonard L. Tripp edited by Alain Abran, Pierre Bourque, Robert Dupuis, James W. Moore, Leonard L. Tripp

[SEBoK] Guide to the Systems Engineering Body of Knowledge (<http://www.sebokwiki.org/>)

ISO/IEC 27000:2009 - Information technology — Security techniques — Information security management systems 

IEC 62366:2007 Medical devices — Application of usability engineering to medical devices

Leveson, N. ‘Engineering a Safer World: Systems Thinking Applied to Safety, MIT, USA (2011)

  1. See Section 3.0 for full definition including notes. ↑

  2. Additional details can be found in Appendix 0. ↑

  3. “Computing platforms” include hardware and software resources (e.g. operating system, processing hardware, storage, software libraries, displays, input devices, programming languages etc.).

“Operating systems” that SaMD require may be run on a server, a workstation, a mobile platform, or other general purpose hardware platform. ↑

  4. ISO/IEC 14764:2006 Software Engineering — Software Life Cycle Processes — Maintenance 

adaptive maintenance: the modification of a software product, performed after delivery, to keep a software product usable in a changed or changing environment

perfective maintenance: the modification of a software product after delivery to detect and correct latent faults in the software product before they are manifested as failures 

corrective maintenance: the reactive modification of a software product performed after delivery to correct discovered problems 

preventive maintenance: the modification of a software product after delivery to detect and correct latent faults in the software product before they become operational faults ↑

  5. IMDRF key definitions Final document “medical purposes” also repeated here in Section 3.3. ↑

  6. These could include specific functionality that is critical to maintain performance and safety profile, attributes identified by risk management process undertaken by the manufacturer of SaMD. ↑

  7. “SaMD changes” are defined in section 3.4 ↑

  8. Leveson, N. 2012. _Engineering a Safer World: Systems Thinking Applied to Safety_. Cambridge, MA, USA: MIT Press. ↑

  9. (Adapted from IEC 62366) ↑

  10. Leveson, N. 2012. _Engineering a Safer World: Systems Thinking Applied to Safety_. Cambridge, MA, USA: MIT Press. ↑

  11. (From ISO/IEC 27000:2009 - Information technology — Security techniques — Information security management systems — Overview and vocabulary) ↑


<!-- fulltext-end -->
