---
title: "Technical Considerations for Medical Devices with Physiologic Closed-Loop Control Technology: Guidance for Industry and Food and Drug Administration Staff"
description: "FDA CDRH Final Guidance Document"
published: 2023-09-29
---

# Technical Considerations for Medical Devices with Physiologic Closed-Loop Control Technology: Guidance for Industry and Food and Drug Administration Staff

**Published**: 2023-09-29

**Status**: Final
**Type**: Guidance Document
**Category**: Digital Health & Cybersecurity
**Topics**: Premarket, Combination Products, Clinical - Medical, Digital Health
**Docket**: FDA-2021-D-0996

::: tip Official Source
[https://www.fda.gov/regulatory-information/search-fda-guidance-documents/technical-considerations-medical-devices-physiologic-closed-loop-control-technology](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/technical-considerations-medical-devices-physiologic-closed-loop-control-technology)
PDF: [https://www.fda.gov/media/154994/download](https://www.fda.gov/media/154994/download)
:::

<!-- fulltext-start -->

---

## Official Full Text

<!-- Page 1 -->
On February 2, 2024, FDA published the final rule to amend the Quality System (QS) regulation 
in 21 CFR part 820 (89 FR 7496, effective February 2, 2026). The revised 21 CFR part 820 is 
now titled the Quality Management System Regulation (QMSR). The QMSR harmonizes quality 
management system requirements by incorporating by reference the international standard 
specific for medical device quality management systems set by the International Organization for 
Standardization (ISO), ISO 13485:2016. The FDA has determined that the requirements in ISO 
13485 are, when taken in totality, substantially similar to the requirements of the QS regulation, 
providing a similar level of assurance in a firm’s quality management system and ability to 
consistently manufacture devices that are safe and effective and otherwise in compliance with 
the Federal Food, Drug, and Cosmetic Act (FD&C Act).
This guidance document was issued prior to the effective date of the final rule. FDA encourages 
manufacturers to review the current QMSR to ensure compliance with the relevant regulatory 
requirements.

---

<!-- Page 2 -->
Contains Nonbinding Recommendations 
 
 
0 
 
Technical Considerations for Medical 
Devices with Physiologic Closed-Loop 
Control Technology1 
______________________________________________________________________________ 
Guidance for Industry and  
Food and Drug Administration Staff  
 
Document issued on September 29, 2023.  
 
The draft of this document was issued on December 23, 2021. 
 
 
For questions about this document regarding CDRH-regulated devices, contact the Office of 
Science and Engineering Laboratories (OSEL) at (301) 796-2530 or by email 
OSEL_CDRH@fda.hhs.gov or the Division of Biomedical Physics, OSEL by email 
OSEL_Interoperability@fda.hhs.gov.  
 
 
 
 
 
 
 
 
 
U.S. Department of Health and Human Services 
Food and Drug Administration 
Center for Devices and Radiological Health 
  
 
 
1 This guidance has been prepared by the by the Center for Devices and Radiological Health (CDRH) in consultation 
with the Center for Drug Evaluation and Research (CDER) and the Center for Biologics Evaluation and Research 
(CBER) at the Food and Drug Administration.

---

<!-- Page 3 -->
Contains Nonbinding Recommendations 
 
 
1 
 
Preface 
Public Comment 
 
You may submit electronic comments and suggestions at any time for Agency consideration to 
https://www.regulations.gov. Submit written comments to the Dockets Management Staff, Food 
and Drug Administration, 5630 Fishers Lane, Room 1061, (HFA-305), Rockville, MD 20852.  
Identify all comments with the docket number FDA-2021-D-0996. Comments may not be acted 
upon by the Agency until the document is next revised or updated. 
 
 
Additional Copies 
 
Additional copies are available from the Internet. You may also send an e-mail request to 
CDRH-Guidance@fda.hhs.gov to receive a copy of the guidance. Please include the document 
number GUI01500085 and complete title of the guidance in the request.

---

<!-- Page 4 -->
Contains Nonbinding Recommendations 
 
 
2 
 
Table of Contents 
 
I. 
Introduction ............................................................................................................................. 1 
II. 
Background ............................................................................................................................. 2 
III. 
Scope .................................................................................................................................... 3 
IV. 
Definitions............................................................................................................................ 5 
V. 
Design Considerations for PCLC Devices .............................................................................. 6 
 
Risk Management Considerations .................................................................................... 7 
(1) 
Patient-related hazards .................................................................................................. 8 
(2) 
Device-related hazards ................................................................................................. 9 
(3) 
Use-related hazards..................................................................................................... 10 
 
Considerations for PCLC Device Design ....................................................................... 12 
(1) 
Control Algorithms ..................................................................................................... 14 
(2) 
Sensors ........................................................................................................................ 16 
(3) 
Actuators ..................................................................................................................... 17 
(4) 
System Integration ...................................................................................................... 18 
(5) 
System Safety Features ............................................................................................... 18 
(6) 
User Interface ............................................................................................................. 20 
 
Verification and Validation Considerations ................................................................... 21 
VI. 
Non-Clinical Testing Considerations ................................................................................. 22 
 
Animal Testing  .............................................................................................................. 23 
 
PCLC Device Testing Using Mathematical and Computational Models ...................... 24 
(1) 
Analytical Assessments .............................................................................................. 26 
(2) 
Entirely Virtual Testing .............................................................................................. 27 
(3) 
Hardware-in-the-Loop Testing ................................................................................... 27 
VII. 
Human Factors Testing ...................................................................................................... 27 
 
Training .......................................................................................................................... 28 
VIII. Labeling ............................................................................................................................... 29

---

<!-- Page 5 -->
Contains Nonbinding Recommendations 
 
1 
 
Technical Considerations for Medical 
Devices with Physiologic Closed-Loop 
Control Technology 
______________________________________________________________________________ 
Guidance for Industry and  
Food and Drug Administration Staff 
 
This guidance represents the current thinking of the Food and Drug Administration (FDA or 
Agency) on this topic.  It does not establish any rights for any person and is not binding on 
FDA or the public.  You can use an alternative approach if it satisfies the requirements of the 
applicable statutes and regulations.  To discuss an alternative approach, contact the FDA staff 
or Office responsible for this guidance as listed on the title page.  
 
I. 
Introduction 
A physiologic closed-loop controlled (PCLC) device is a system consisting of sensors, actuators, 
and control algorithms that adjusts or maintains a physiologic variable through automatic 
adjustments to delivery or removal of energy or article (e.g., drugs,2 or liquid or gas regulated as 
a medical device) using feedback from a physiologic-measuring sensor(s). PCLC technology can 
enable automation in a variety of medical device types. Such devices have the potential to deliver 
timely, accurate and consistent therapy and can play an important role in reducing cognitive 
overload, minimizing human error, and enhancing medical care including, for example, during 
emergency response and medical surge situations. Ensuring patient safety is an important 
consideration while evaluating the potential benefits of PCLC devices.   
 
This document highlights technical considerations for the development of medical devices 
employing PCLC technology to ensure safe and effective use and provides recommendations for 
the content of premarket submissions (i.e., premarket notifications (510(k)s), De Novo requests, 
premarket approval applications (PMAs), Humanitarian Device Exemptions (HDEs)) for such 
devices.  
 
For the current edition of the FDA-recognized consensus standard(s) referenced in this 
document, see the FDA Recognized Consensus Standards Database.3 For more information 
regarding use of consensus standards in regulatory submissions, please refer to the FDA 
 
2 The term drug as used in this guidance refers to both human drugs and biological products unless otherwise 
specified. 
3 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm

---

<!-- Page 6 -->
Contains Nonbinding Recommendations 
 
 
2 
 
guidance titled “Appropriate Use of Voluntary Consensus Standards in Premarket Submissions 
for Medical Devices.”4  
 
Throughout this guidance, the terms “FDA,” “the Agency,” “we,” and “us” refer to the Food and 
Drug Administration and the terms “you” and “yours” refer to medical device manufacturers. 
 
In general, FDA’s guidance documents do not establish legally enforceable responsibilities. 
Instead, guidances describe the Agency’s current thinking on a topic and should be viewed only 
as recommendations, unless specific regulatory or statutory requirements are cited. The use of 
the word should in Agency guidances means that something is suggested or recommended, but 
not required.  
 
II. Background 
Automation in PCLC devices is enabled by the control system technology in host medical 
devices such as infusion pumps, ventilators, extracorporeal systems (e.g., dialysis delivery 
systems and organ reperfusion devices), and stimulation systems. PCLC devices can benefit the 
patient by facilitating safe and effective, consistent, and timely delivery or removal of energy or 
article (e.g., drugs, or liquid or gas regulated as a medical device). Other benefits of PCLC 
devices may include improving the quality and/or accuracy of delivering the energy or article 
over time, reducing potential under- or overdosage, enabling safe and effective delivery of 
energy or articles when manual control is not suitable due to related time constraints, or reducing 
the workload of a caregiver by omitting simple manual readjustments so focus can be on other 
aspects of patient care. However, introducing automation and minimizing clinician involvement 
can incur new types of hazardous situations that can render the medical device unsafe if not 
properly designed or evaluated. Algorithm flaws, lack of operational transparency, and 
automation bias are examples of potential automation-induced hazards. 
 
The Center for Devices and Radiological Health (CDRH) held a public workshop entitled 
“Physiological Closed-Loop Controlled Devices” on October 13 and 14, 2015, with the aim of 
fostering an open discussion on design and evaluation considerations associated with PCLC 
devices used in critical care environments.5 This workshop provided a forum for medical device 
manufacturers, clinical users and academia to discuss technical considerations for automated 
medical devices with PCLC technology.6 The feedback received during this workshop and from 
 
4 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/appropriate-use-
voluntary-consensus-standards-premarket-submissions-medical-devices  
5 Available at http://wayback.archive-
it.org/7993/20170112084803/http:/www.fda.gov/MedicalDevices/NewsEvents/WorkshopsConferences/ucm457581.
htm 
6 A summary of the discussion topics of the workshop can be found in Parvinian B, Scully C, Wiyor H, Kumar A, 
and Weininger S. Regulatory Considerations for Physiological Closed-Loop Controlled Medical Devices Used for 
Automated Critical Care: Food and Drug Administration Workshop Discussion Topics. Anesthesia and Analgesia. 
2018 Jun; 126(6): 1916-1925. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6233305/

---

<!-- Page 7 -->
Contains Nonbinding Recommendations 
 
 
3 
 
numerous interactions with companies designing PCLC medical devices through the Q-
submission process7 was taken into consideration to develop this guidance.  
 
III. Scope 
This guidance provides technical considerations related to the PCLC technology when designing 
PCLC medical devices. PCLC medical devices can include functions or components8 that have 
risks separate from the PCLC functions that are not addressed in this guidance.9 Not all 
considerations in this guidance will be applicable to every PCLC device given the variety of 
device types that can incorporate PCLC technology. Manufacturers should determine and justify 
in premarket submissions which considerations are appropriate for their device based on the 
technology being used and the intended use of the device. Examples of medical device functions 
that may be considered PCLC technology include, but are not limited to: 
• Anesthesia gas machines that automatically titrate the fraction of inspired anesthetic 
agent in response to an end-tidal gas measurement or rate of infused anesthetic drug 
in response to electroencephalogram (EEG) signals of neural activity. 
• Mechanical ventilators or other oxygen therapy devices that automatically adjust 
settings (e.g., fraction of inspired oxygen, positive end expiratory pressure) in 
response to a measure of patient oxygen saturation (e.g., SpO2 from a pulse oximeter) 
or exhaled gas concentration (e.g., CO2). 
• Hemodynamic stability systems that automatically adjust fluid or vasoactive drug 
infusion rates in response to a patient’s measured blood pressure. 
• Automatic insulin delivery systems that control insulin delivery based on inputs from 
a blood glucose value. 
• Hypo- and hyperthermia systems that automatically adjust temperature in response to 
a temperature measured from the patient’s body. 
Additional examples of medical devices and device functions that incorporate PCLC technology 
can be found in Annex A of International Electrotechnical Commission (IEC) 60601-1-10 
Edition 1.2 2020-07: Medical electrical equipment - Part 1-10: General requirements for basic 
safety and essential performance - Collateral Standard: Requirements for the development of 
physiologic closed-loop controllers. Annex A “General guidance and rationale” of IEC 60601-1-
10 also includes examples of medical devices and device functions that do not involve PCLC 
technology. For questions on if a specific device is a PCLC device, we recommend 
manufacturers submit questions through the Q-Submission process; see “Requests for Feedback 
 
7 Information regarding the Q-submission process can be found in “Requests for Feedback and Meetings for 
Medical Device Submissions: The Q-Submission Program - Guidance for Industry and Food and Drug 
Administration Staff” available at https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/requests-feedback-and-meetings-medical-device-submissions-q-submission-program.  
8 In this guidance, the word component refers to the functional elements that make up a PCLC device. For example, 
the physiologic-measuring sensor(s), actuator(s), and software implementing the control algorithm are all 
components of a PCLC device, when such components are used to perform the PCLC function.  
9 In addition, this guidance does not address considerations with respect to the compatibility between a PCLC device 
and the article intended to be delivered, nor does it address the technical considerations with respect to evaluating 
whether the PCLC device is suitable for delivery of the article.

---

<!-- Page 8 -->
Contains Nonbinding Recommendations 
 
 
4 
 
and Meetings for Medical Device Submissions: The Q-Submission Program - Guidance for 
Industry and Food and Drug Administration Staff.”10 
 
Although elements of this guidance may be applicable to active implantable devices with PCLC 
technology, including neurostimulators and pacemakers, additional considerations outside the 
scope of this guidance may also need to be addressed (e.g., related to the long-term use of the 
PCLC function). In some cases, there may be device-specific guidances that should also be 
utilized, and this guidance is not intended to supersede other device-specific guidances.  
 
The technical recommendations in this document should be applied as appropriate to the 
following premarket device-related submissions:  
• Premarket notifications (510(k)); 
• De Novo requests; 
• Premarket Approval (PMA) applications; and 
• Humanitarian Device Exemptions (HDE). 
 
Overall premarket submission requirements and recommended information to provide can differ 
depending on the premarket submission type. Additional information on each submission type 
can be found on the FDA’s Premarket Submissions webpage.11 The type of premarket 
submission that is required for your PCLC device is determined by the classification of your 
device, based on the risk of the device and the level of regulatory controls necessary to provide 
reasonable assurance of safety and effectiveness for the device. This guidance document does 
not include information about the classification of PCLC devices. Questions regarding the 
regulatory requirements for specific devices, including questions of whether a device is a PCLC 
medical device, should be submitted through the Q-Submission process, see “Requests for 
Feedback and Meetings for Medical Device Submissions: The Q-Submission Program - 
Guidance for Industry and Food and Drug Administration Staff.”12 
 
Many of the recommendations here can also be useful for supporting the safety of a PCLC 
device in an Investigational Device Exemption (IDE).13 The design and testing of a device 
incorporating PCLC technology will depend on a variety of factors, including, but not limited 
to, the energy or article being delivered, environment of use, level of automation, the patient or 
user population, the type of sensor, method of control algorithm design, and properties of the 
delivery system. CDRH encourages sponsors to utilize the Q-Submission process14 to obtain 
more detailed feedback on clinical study designs evaluating the risks of their automated medical 
devices with PCLC technology.  
 
 
10 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program 
11 Available at https://www.fda.gov/medical-devices/how-study-and-market-your-device/premarket-submissions 
12 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program 
13 For additional information related to IDE submissions, see the FDA’s Investigational Device Exemption webpage 
(https://www.fda.gov/medical-devices/how-study-and-market-your-device/investigational-device-exemption-ide). 
14 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program

---

<!-- Page 9 -->
Contains Nonbinding Recommendations 
 
 
5 
 
This guidance is not intended to provide specific recommendations as they relate to machine 
learning (ML) aspects of a PCLC device design. We recommend discussing with the Agency 
through the Q-Submission process15 the design and test plan of control algorithms designed with 
and/or incorporating ML.  
  
IV. Definitions  
The definitions listed here are for the purposes of this guidance and are intended for use in the 
context of the design and evaluation of PCLC devices. Additional definitions related to the 
design and evaluation of PCLC devices are included in IEC 60601-1-10 and should be referred 
to when demonstrating conformance with that standard. 
 
Automation bias: the tendency for users to give greater belief to information from automation 
technology without verification 
 
Complacency: a phenomenon that refers to the monitoring of technology less regularly or with 
less vigilance because of a lower degree of suspicion of error and a stronger belief in its accuracy 
 
Entrance criteria: information about the patient, clinical, device, and/or environmental state 
input to the PCLC device to begin an automated mode. This information may be entered by the 
user into the PCLC device, received from other devices or components, or available from the 
PCLC device. 
 
Exit criteria: information about the patient state, device state, delivered energy or article, or 
other information communicated by the PCLC device to the user when an automated mode is 
ending 
 
Fallback mode: mode of operation (or state) into which the PCLC device transitions when the 
PCLC device stops operating due to detection of a fault16  
 
Integrated clinical environment: environment that combines interoperable heterogeneous 
medical devices and other equipment integrated to create a medical system for the care of a 
single patient17 
 
Loss of situational awareness: reduction of the user’s awareness of the patient or technology 
state due to the automation of clinical decisions and execution functions by a device 
 
 
15 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program 
16 Clause 3.11 “Fallback mode” of IEC 60601-1-10 Edition 1.2 2020-07: Medical electrical equipment - Part 1-10: 
General requirements for basic safety and essential performance - Collateral Standard: Requirements for the 
development of physiologic closed-loop controllers 
17 Modified for this guidance from “Integrated clinical environment” from Terms and Definitions of ANSI AAMI 
2700-1: Medical Devices and Medical Systems - Essential safety requirements for equipment comprising the patient-
centric integrated clinical environment (ICE) - Part 1: General requirements and conceptual model

---

<!-- Page 10 -->
Contains Nonbinding Recommendations 
 
 
6 
 
Physiologic closed-loop controlled medical device: a medical device that automatically adjusts 
or maintains a physiologic variable(s) (i.e., the controlled physiologic variable) through delivery 
or removal of energy or article18 (e.g., drugs, or liquid or gas regulated as a medical device) 
using feedback from a physiologic-measuring sensor(s)19  
 
Physiologic variable: quantity or condition, from a patient, whose value is subject to change and 
can usually be measured20  
 
Physiologic-measuring sensor: measurement component of a PCLC device that uses a 
combination of patient-contact or imaging materials, transducers, signal conditioning, and 
algorithms to estimate the value of a physiologic variable21 [Note: When the term sensor is used 
in this guidance document it is referring to a physiologic-measuring sensor.] 
 
Skill degradation: reduction of decision-making and execution ability which can lead to 
forgetting and skill decay manifestation if the clinical decision-making choices are consistently 
executed by automation 
 
V. Design Considerations for PCLC Devices 
Consistent with 21 CFR part 820.30,22 a manufacturer must establish, document, and maintain 
throughout the medical device lifecycle an ongoing process for design control activities, which 
can include activities such as identifying hazards, estimating and evaluating the associated risks, 
 
18 The term article in this guidance is used in the same way as substance in IEC 60601-1-10 Edition 1.2 2020-07: 
Medical electrical equipment - Part 1-10: General requirements for basic safety and essential performance - 
Collateral Standard: Requirements for the development of physiologic closed-loop controllers 
19 Physiologic closed-loop controlled device is used in this guidance document the same way as physiologic closed-
loop control system (PCLCS) is used in in IEC 60601-1-10 Edition 1.2 2020-07: Medical electrical equipment - 
Part 1-10: General requirements for basic safety and essential performance - Collateral Standard: Requirements 
for the development of physiologic closed-loop controllers 
20 Adapted from Clauses 3.21 “Physiologic variable,” 3.28 “Variable,” and 3.29 “Patient variable” in IEC 60601-1-
10 Edition 1.2 2020-07: Medical electrical equipment - Part 1-10: General requirements for basic safety and 
essential performance - Collateral Standard: Requirements for the development of physiologic closed-loop 
controllers 
21 The term physiologic measuring sensor in this guidance document is used in the same way as measuring transfer 
element in IEC 60601-1-10 Edition 1.2 2020-07: Medical electrical equipment - Part 1-10: General requirements 
for basic safety and essential performance - Collateral Standard: Requirements for the development of physiologic 
closed-loop controllers  
22 On February 23, 2022, FDA proposed to amend the device QS regulation, 21 CFR part 820, to align more closely 
with international consensus standards for devices (87 FR 10119; available at 
https://www.federalregister.gov/documents/2022/02/23/2022-03227/medical-devices-quality-system-regulation-
amendments). Specifically, FDA proposed to withdraw the majority of the current requirements in part 820 and 
instead incorporate by reference the 2016 edition of the International Organization for Standardization (ISO) 13485, 
Medical devices- Quality management systems for regulatory purposes, in part 820. As stated in that proposed rule, 
the requirements in ISO 13485 are, when taken in totality, substantially similar to the requirements of the current 
part 820, providing a similar level of assurance in a firm’s quality management system and ability to consistently 
manufacture devices that are safe and effective and otherwise in compliance with the FD&C Act. FDA intends to 
finalize this proposed rule expeditiously. When the final rule takes effect, FDA will also update the references to 
provisions in 21 CFR part 820 in this guidance to be consistent with that rule.

---

<!-- Page 11 -->
Contains Nonbinding Recommendations 
 
 
7 
 
controlling these risks, and monitoring the effectiveness of the controls. This process should 
include risk analysis, risk evaluation, risk control/mitigation, and incorporation of production and 
post-production information. Recommendations below related to the design process address risk 
management considerations, system and component level design considerations, and verification 
and validation considerations. Design inputs for a device with PCLC technology should consider 
the risks associated with the complete device and not only the PCLC functions. The design of a 
PCLC device should support safe and effective use in the patient population, environment, and 
clinical workflow in which the device will be used. We recommend that manufacturers follow 
development procedures as described in IEC 60601-1-10: Medical electrical equipment - Part 1-
10: General requirements for basic safety and essential performance - Collateral Standard: 
Requirements for the development of physiologic closed-loop controllers or an equivalent 
method when designing PCLC devices, as well as risk management process recommendations as 
described in International Organization for Standardization (ISO) 14971: Medical devices - 
Application of risk management to medical devices. 
 
FDA recognizes that PCLC devices may have multiple potential benefits to patient care (see 
Section II. Background) that should be considered when making regulatory decisions and 
recommends that manufacturers refer to existing FDA guidance documents to collect and prepare 
information for regulatory submissions to support benefit-risk determinations. For example, see 
the FDA guidance documents “Factors to Consider When Making Benefit-Risk Determinations 
in Medical Device Premarket Approval and De Novo Classifications”23 and “Benefit-Risk 
Factors to Consider When Determining Substantial Equivalence in Premarket Notifications 
(510(k)) with Different Technological Characteristics”24 as applicable. 
 
 
 Risk Management Considerations 
PCLC devices are complex systems. The performance of a PCLC device can be affected by -
sensors, therapy delivery devices, control algorithms, software, user interfaces, characteristics of 
the article being delivered, and the patient’s physiology. Hazards can arise from failures of 
individual device components, loss of communication between components, software failures, 
inappropriate control algorithm design, use errors, or disturbances to the patient’s physiology. 
This can result in harm to the patient due to too much or too little energy or article being 
delivered, either over a short time period or the length of time the PCLC device is used. We 
recommend manufacturers consider hazards identified in IEC 60601-1-10 (e.g., Clause 4 
“General Requirements” of IEC 60601-1-10 Edition 1.2 2020-07) and follow all 
recommendations related to risk management in this consensus standard. For PCLC devices 
comprised of interoperable medical devices, we recommend manufacturers also consider hazards 
identified in American National Standards Institute (ANSI)/Association for the Advancement of 
Medical Instrumentation (AAMI)/Underwriters Laboratories, Inc. (UL) 2800-1: Standard for 
Safety for Medical Device Interoperability. For PCLC devices that will be implemented as part 
of an integrated clinical environment, we recommend manufacturers also consider hazards 
 
23 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/factors-consider-when-
making-benefit-risk-determinations-medical-device-premarket-approval-and-de 
24 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/benefit-risk-factors-
consider-when-determining-substantial-equivalence-premarket-notifications-510k

---

<!-- Page 12 -->
Contains Nonbinding Recommendations 
 
 
8 
 
identified in ANSI/AAMI 2700-1: Medical Devices and Medical Systems - Essential safety 
requirements for equipment comprising the patient-centric integrated clinical environment (ICE) 
- Part 1: General requirements and conceptual model. Appropriate verification and validation 
techniques will depend on the risks of individual hazards as well as the type of hazard.  
 
We recommend identifying the following causes of hazards as part of the risk analysis in a PCLC 
device submission. The submitted risk analysis should include hazardous situations, the risks that 
can result from each, and how the risks were addressed. 
(1) Patient-related hazards 
The response of the patient to the energy or article being delivered or removed (i.e., the patient 
transfer element as defined in IEC 60601-1-10) is a critical factor to consider in the design. This 
response can differ between patients (inter-patient variability) and within an individual patient 
(intra-patient variability). It can be affected by disturbances caused by, for example, other 
therapies being delivered to the patient. These scenarios can affect the patient’s response and 
cause the system to not perform as anticipated, if the PCLC device is not designed and tested 
adequately, and result in the delivery of inappropriate therapy and harm to the patient. Safely 
managing such scenarios involves adequately characterizing the patient’s response and using this 
information to design appropriate controllers, safe fallback modes, and communication to the 
user. Safe mitigations are not the same for all patient populations, environments of use, or 
clinical workflows. Design considerations including risk analysis, user interface designs, safety 
features, testing needs, and training can vary depending on the specific patient population a 
PCLC device is intended for and how the device is expected to impact patient care and clinical 
workflows. We recommend manufacturers identify the following related to the patient 
population: 
 
• Intended patient population, including diseases, health status, and potential 
comorbidities. 
• Contraindications for use of the PCLC technology. 
• Environment where the device is intended to be used (e.g., patient transport, intensive 
care unit, operating room, home). 
• Current care according to accepted practice guidelines related to device objective, 
including the various therapies and physiologic variables and measurements that 
could be used to make therapy decisions related to the objective of the PCLC 
technology in the intended patient population. 
• Identification of differences between the current care according to accepted practice 
guidelines and the method that will be employed by the PCLC device (e.g., if current 
care based on accepted practice guidelines relies on a comprehensive patient 
assessment to make decisions about changes, but the PCLC technology will only use 
a single measured physiologic variable). 
 
When designing a PCLC device, manufacturers should characterize and consider disturbances 
related to the patient’s response as relevant for their PCLC device and consider the following in 
the risk analysis:

---

<!-- Page 13 -->
Contains Nonbinding Recommendations 
 
 
9 
 
• Expected response of the physiologic variable being controlled to the delivered 
energy or article in the intended patient population including delays in the response of 
the physiologic variable to the delivered energy or article and considering, as 
applicable, how changes to the article being delivered (e.g., formulation changes for a 
drug) may affect that response. 
• Variability in the physiologic response between patients (i.e., inter-patient 
variability). 
• Variability/changes in the physiologic response over time (i.e., intra-patient 
variability) due to, for example, disease progression, changes to a patient’s sensitivity 
to the administered energy or article, or regularly occurring physiologic rhythms (e.g., 
circadian). 
• Interactions between physiologic systems that can result in changes in the controlled 
physiologic variable (e.g., respiratory modulation of the arterial pressure waveforms 
or cerebral perfusion effect on the EEG). 
• Physiologic response to concurrent therapies expected for the intended patient 
population including other PCLC devices that can be applied to the patient (e.g., other 
drugs that might affect the patient’s response). 
• Disturbances to the patient’s response that can occur (e.g., change in other therapies 
being provided, movement or change in positioning of the patient, meals). 
• Other physiologic effects of the delivered energy or article in addition to those on the 
physiologic variable intended to be controlled (e.g., hypotensive effect of anesthetics, 
hypoventilation effect of opioid analgesics).  
 
Ranges of patient variability and sources of disturbances should be determined considering 
normal and worst-case clinical conditions of the intended patient population (e.g., derived from 
clinical literature) and clinical workflow scenarios. 
(2) Device-related hazards 
Device-related hazards refer to those hazards resulting from the PCLC device and its 
components, rather than the patient. Manufacturers should identify and characterize uncertainties 
in their system design and foreseeable functional disturbances given the clinical environment and 
workflow. Examples of device-related hazards that manufacturers should consider in their risk 
management process include the following related to the PCLC device: 
 
• Transient as well as persistent motion or noise artifacts in the measured feedback 
variable. 
• Sensor accuracy is not sufficient. 
• Component (e.g., sensor or actuator) no longer meets system specifications. 
• Communication failure between device components and failures within an integrated 
clinical environment, for PCLC devices implemented in an integrated clinical 
environment. 
• Cybersecurity threats and vulnerabilities.25 
 
25 For additional information on medical device cybersecurity see the FDA’s cybersecurity webpage available at 
https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity

---

<!-- Page 14 -->
Contains Nonbinding Recommendations 
 
 
10 
 
• Actual quantity of delivered energy or article not equal to that set by the control 
algorithm (e.g., due to saturation or inherent variability of the actuator). 
• Latency and delay times within the system and individual components that can result 
in unsafe conditions. 
• Other known risks associated with the individual PCLC device components, any 
single fault in the system and possible interactions between fault conditions. 
• If a PCLC device uses a component that is a legally marketed device (e.g., a 
510(k)-cleared blood pressure monitor that serves as the physiologic-measuring 
sensor in the PCLC device), we recommend you also evaluate postmarket 
information such as recalls and Medical Device Reports (MDRs).26 We 
recommend that manufacturers address any postmarket concerns identified for 
these PCLC device components that can impact the performance of the PCLC 
device, considering how the component will be used as part of the PCLC device, 
and provide information on mitigations in your device design and labeling that 
addresses this issue. This should include a description of differences in the 
component capabilities considering the use in the PCLC device (e.g., use of the 
component in an ‘open-loop’ configuration compared to ‘closed-loop’ 
configuration as part of the PCLC device), as applicable.    
• Changes to third-party components of the PCLC device that can affect the safety or 
performance of the PCLC device or changes to the article (e.g., drug) that the PCLC 
device delivers so that the PCLC device and article are no longer compatible. For 
PCLC devices implemented in an integrated clinical environment, this may also 
include changes to devices comprising the integrated clinical environment. 
• We recommend that manufacturers of PCLC devices establish processes, as part 
of their quality system (see 21 CFR part 820), to identify when changes to third-
party components used as part of their device, or changes to the articles that the 
PCLC device delivers, occur and evaluate whether the changes no longer meet the 
PCLC device specifications. 
(3) Use-related hazards 
To ensure PCLC devices with automatic decision-making capabilities operate as intended, it is 
important to have an accurate understanding of fundamental human factors considerations such 
as human cognitive capabilities and limitations, and how these impact human-automation 
interactions for the PCLC device. When designing devices with varying levels of automation, we 
recommend that manufacturers consider the possibility that users can experience reduced 
interactions with the patient and device compared to current care based on accepted practice 
guidelines. As a result of reduced interaction, the user may not have a complete understanding of 
the patient or device status (reduced situational awareness) jeopardizing their ability to provide 
appropriate interventional responses.  
 
 
26 For more information on Medical Device Reporting see the “FDA Guidance Document: Medical Device 
Reporting: Guidance for Industry and Food and Drug Administration Staff” available at 
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-reporting-
manufacturers

---

<!-- Page 15 -->
Contains Nonbinding Recommendations 
 
 
11 
 
Designers of PCLC devices should consider how a user’s role can change from active to passive 
interaction with the automated features. Careful consideration is needed to address such reduced 
interactions. Users could have the tendency to over-trust or over-rely on the device automation 
which can affect the users’ ability to recognize the need for interventions. Therefore, we 
recommend manufacturers consider that the human-automation interaction has the potential to 
introduce automation-related use errors relative to complacency, automation bias, loss of 
situational awareness, and skill degradation of the users. Determining the anticipated users will 
help in appropriately applying risk management strategies for activities such as designing the 
device user interface and developing appropriate labeling for use of the device. We recommend 
manufacturers consider the following related to the anticipated users when designing a PCLC 
device: 
 
• Whether the device will be operated by physicians, nurses, other clinical staff, 
patients (for example, if patients will be able to modify the target level), or other 
caregivers. 
• Expected training of users related to the objective of the PCLC technology in the 
intended patient population and environment of use. 
• Level of clinical supervision expected for the patient population. 
• Whether biomedical technicians or other individuals can service or configure the 
device. 
 
A PCLC device can have the capability of sensing and processing patient physiologic data and 
executing therapeutic decisions with varying levels of user involvement for a particular decision; 
this can be referred to as the level of automation of the device. Use-related risks and design 
considerations can depend on the level of automation that the PCLC device employs. 
Understanding the levels of automation and associated hazards is critical to safe operation of the 
PCLC device. These use-related risks are dependent on user’s behavior, which is difficult to 
predict. An appropriate risk management technique should be used to identify these human-
automation interaction hazards so that effective mitigation measures can be implemented. The 
manufacturer should consider human factors and user characteristics such as sensory ability, 
attention, memory, reasoning, decision-making, emotions, knowledge, experience, and skills 
associated with each automation level when deciding how to automate a device. 
 
We recommend that manufacturers perform a use-related risk analysis assessing the potential 
harm that could arise during step-by-step use of the device. Any reasonable, foreseeable misuse 
as well as known risks associated with the PCLC device components should be taken into 
account in this use-related risk analysis. However, automation-related use errors are not always 
predictable until a device is used in representative-use situations (e.g., in the clinic, operating 
room or home environment with clinician and/or patient users as applicable for the device). 
Therefore, we recommend that when clinical studies are performed, manufacturers collect data 
on device operation during representative-use situations, including when fault conditions occur 
and fallback modes are entered, to examine user responses. This information can then be 
evaluated as part of the process to identify use-related hazards.

---

<!-- Page 16 -->
Contains Nonbinding Recommendations 
 
 
12 
 
Manufacturers should follow recommendations in the FDA guidance document, “Applying 
Human Factors and Usability Engineering to Medical Devices,”27 when performing risk 
management for use-related hazards considering all device user-automation interfaces such as 
dynamic information displays, buttons, and logic of operations that can impact the device use. 
 
Considerations for PCLC Device Design 
PCLC devices can have different design and engineering parameters. The design of PCLC 
devices can include different approaches towards risk mitigation and system fault handling, 
including use of various open-loop and manual modes in case of fault occurrence and the use of 
supervisory layers that determine how and when the transition from these modes should take 
place. Regardless of the design method, we recommend that the design of the PCLC device is 
such that device safety and performance can be assessed in a clear and consistent fashion. 
Manufacturers should set design specifications such that handling of challenging clinical (e.g., 
patient variability) and functional (e.g., component malfunction) scenarios can be verified and to 
enable root cause analysis for corrective action where needed.  
 
A PCLC device includes 1) a sensor(s) that measures a physiologic variable from the patient, 2) 
a control algorithm, and 3) an actuator that delivers or removes energy or article to the patient 
(see Figure 1). We recommend manufacturers describe the technical components and 
specifications of a PCLC device as described in IEC 60601-1-10 (e.g., Clause 8.2.2 “Equipment 
Specifications” of IEC 60601-1-10 Edition 1.2 2020-07) and, if applicable, ANSI/AAMI 2700-1. 
 
 
 
Figure 1. Basic block diagram of a PCLC device including the patient to form a closed-loop 
system. The “Patient” block includes the patient’s physiologic processes that will be affected by 
the manipulated variable (i.e., the delivered energy or article). While a “Disturbance” arrow is 
shown here to act on the patient and the patient’s physiologic processes, disturbances could 
occur at various points in the system. The “Control Algorithm,” “ Sensor,” and “Actuators” 
blocks are highlighted to correspond with Sections V.B (1), (2), and (3) below, while the variable 
terms reflect those used in IEC 60601-1-10 to show the relationship between the component 
terms in this guidance and IEC 60601-1-10. 
 
27 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-
factors-and-usability-engineering-medical-devices

---

<!-- Page 17 -->
Contains Nonbinding Recommendations 
 
 
13 
 
 
As part of the device description for a PCLC device in a premarket submission, manufacturers 
should identify and describe the elements in Section V.B (1-6) below. This should include 
information on the individual components that are part of the PCLC device design and how these 
components are integrated so that the PCLC device can function as intended. We recommend 
that, where possible, the manufacturer provide a schematic of the system configuration in the 
form of a functional block diagram with the controlled physiologic variable, sensor, control 
algorithm, actuator, delivered energy or article, and patient clearly identified within the context 
of the device description (see Figure 1). The input and output relationship of each element (e.g., 
sensor, actuator, patient) in the system should be identified to allow for a description of the 
complete system over its intended range and under various pathological conditions. We 
recommend manufacturers identify and describe all automated modes and features related to the 
PCLC technology, describe all fallback modes, and provide information on how the user 
interacts with and sets device parameters, including ranges and increments of configurable 
parameters that can be set by the user, in the device description. This should include information 
on all phases of therapy that will be controlled (e.g., induction of anesthesia, maintenance of 
anesthesia, and/or emergence from anesthesia) and whether automated PCLC technology will 
make determinations, for example, about the therapeutic objectives (e.g., by determining the 
appropriate target level for a physiologic variable). For PCLC devices that deliver drugs or other 
regulated medical products, the PCLC device manufacturer should describe how the design, 
including the control algorithm, delivers the article consistent with the labeling of the product 
that is being delivered (e.g., maximum rate and cumulative amount over time of drug the PCLC 
device can deliver). The PCLC device labeling should also include information regarding 
compatibility with the article (e.g., drugs, or liquid or gas regulated as a medical device) it is 
intended to deliver. 
 
Components of a PCLC device (e.g., sensors and actuators) can be specifically designed for the 
PCLC device, selected from existing off-the-shelf parts (i.e., a component that by itself is not a 
medical device), or can be existing, cleared or approved, stand-alone medical devices (e.g., 
infusion pumps, patient monitor). PCLC device component specifications should support the 
component’s function as part of the PCLC device considering the risks related to inadequate 
component performance. The performance specifications needed for a medical device used as a 
component in a PCLC device can be different from the performance specifications of the stand-
alone medical device. For example, a sensor device with a certain accuracy level could be 
appropriate for stand-alone applications, but that same accuracy level would not be adequate for 
the PCLC device to meet performance specifications. Manufacturers should also consider 
relevant FDA guidances or special controls for PCLC device components that are previously 
cleared or approved devices. For example, an infusion pump developed to serve as an actuator in 
a PCLC device should follow recommendations in the FDA guidance document, “Infusion 
Pumps Total Product Life Cycle,”28 as applicable for the PCLC device. For PCLC devices that 
include interoperable medical devices as part of the PCLC device, manufacturers should refer to 
 
28 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/infusion-pumps-total-
product-life-cycle

---

<!-- Page 18 -->
Contains Nonbinding Recommendations 
 
 
14 
 
the FDA guidance document, “Design Considerations and Premarket Submission 
Recommendations for Interoperable Medical Devices.”29 
(1) Control Algorithms 
The control algorithm determines the automated actions of a PCLC device by comparing one or 
more feedback variables from physiologic-measuring sensors with referencing values derived 
from command variables determined from user inputs to provide a controller output variable to 
an actuator (see Figure 1). The main function of the control algorithm is to determine 
adjustments to the delivered energy or article so that the PCLC device meets clinically relevant 
performance specifications as defined in IEC 60601-1-10, such as response time, settling time, 
relative overshoot, steady state-deviation, and tracking error, considering the robustness and 
stability of the system over the range of expected variability and uncertainty and switching 
between therapy modes. We recommend manufacturers specify the system response 
characteristics such as those listed in Clause 8.2.2.6 “Responses of the PCLCS” of IEC 60601-1-
10 Edition 1.2 2020-07 or define equivalent system response specifications as applicable for their 
device (e.g., based on relevant specifications in FDA-recognized consensus standards).  
 
The design of control algorithms used in a PCLC device should be based on a characterization of 
the response of the controlled physiologic variable to the energy or article provided by the PCLC 
device as well as the interplay of any factors that can affect such dynamics. For example, in an 
automated anesthesia system, the pharmacokinetics and pharmacodynamics and therapeutic 
index of the drug as well as time-varying patient sensitivity to the drug should be considered by 
the controller to safely induce and maintain anesthesia. Any element that affects these dynamics 
(e.g., concomitant drugs that can affect the patient’s response to the drug provided by the device 
with PCLC technology) should be considered in the controller design as it can affect the 
controller performance, stability and safety. 
 
A control algorithm should be designed to perform in the presence of inter-patient and intra-
patient variability, disturbances, environmental interference, and other related hazards discussed 
in Section V.A Risk Management Considerations of this guidance. We recommend 
manufacturers follow IEC 60601-1-10 (e.g., Clause 8.2.3.2 “Disturbance Analysis” of IEC 
60601-1-10 Edition 1.2 2020-07) to identify and characterize disturbance variables, as applicable 
to their automated medical device with PCLC technology and address how the control algorithm 
enables the PCLC device to meet specifications during these conditions. 
 
In many cases, a PCLC device with one control algorithm may not be sufficient to function as 
intended in the use scenario. As a result, PCLC technology within a medical device can consist 
of multiple control algorithms functioning simultaneously or within different modes that the 
system switches between. For example, for the purpose of automatic oxygen delivery, different 
control algorithms can be designed and activated depending on whether the patient is in a state of 
normoxemia, hypoxemia or hyperoxemia. In another example, for closed-loop anesthesia, 
individual control algorithms can be designed for induction, maintenance and emergence of 
 
29 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-considerations-
and-pre-market-submission-recommendations-interoperable-medical-devices

---

<!-- Page 19 -->
Contains Nonbinding Recommendations 
 
 
15 
 
anesthesia. We recommend manufacturers consider the following when using multiple control 
algorithms: 
 
• In cases where different control algorithms are responsible for different phases of 
therapy, the system should be designed such that switching between control 
algorithms does not adversely impact the therapy provided. 
• User interfaces should be designed so that the user is able to identify the current 
operating mode and when the control algorithm switches modes (e.g., to mitigate 
risks related to mode confusion). 
• The entrance and exit criteria for mode switching should be defined and implemented 
for each therapeutic mode. These criteria should be communicated to the user through 
the device user interface. 
• Control algorithms for all modes should be designed to meet their performance 
specifications during reasonably foreseeable disturbances. 
 
Figure 1 shows a PCLC device operating as a single ‘loop’ (i.e., the control algorithm is 
automatically adjusting therapy to control a single physiologic variable). Multiple PCLC ‘loops’ 
can be applied to the same patient simultaneously. This can occur as a manufacturer introduces a 
PCLC device with multiple objectives, a new PCLC feature is added to an existing PCLC device, 
or two or more PCLC devices are intended to function together. The interaction between control 
loops that may be used together should be characterized to identify potential hazards arising from 
the system. For example, if the objective of a PCLC device is to control mean arterial pressure 
through vasoactive drug delivery and depth of anesthesia through hypnotic drug delivery, the 
influence of each loop on the other should be considered in the design. 
 
Control algorithms can be designed using a variety of techniques that could result in varying 
levels of transparency and understanding of the control algorithm. This will have an impact on 
the methods that can be applied for verification and validation. We recommend manufacturers 
consider the following scenarios for designing a controller: 
 
• The design can follow a mathematical model-based approach. In this case, a 
mathematical model of the underlying physiologic dynamics and potential 
variabilities and disturbances that might be encountered in clinical settings is obtained 
or developed and used to design a control algorithm. This can facilitate evaluation by 
providing physiologic insight, transparency, and a framework for the design of the 
controller. See Section VI.B below for technical recommendations to establish the 
credibility of computational models used in the development of PCLC devices. 
 
• The control algorithm can be designed based on, for example, a decision table 
developed from clinical guidelines or best practices (i.e., rule-based controller). In 
these scenarios, we recommend manufacturers examine the clinical evidence 
supporting the rules that the control algorithm will implement. Any differences 
between the implementation of the rules in the control algorithm and the way studies 
were implemented to determine and/or evaluate the rules should be identified. For 
example, a clinical study could be performed so that an infusion rate is adjusted once 
per hour according to a fixed decision table while a control algorithm could be

---

<!-- Page 20 -->
Contains Nonbinding Recommendations 
 
 
16 
 
designed to implement those updates more frequently. In this example, any clinical or 
physiologic differences due to the faster update rate and how they could impact the 
safety and performance of the device should be considered.  
 
• Control algorithms can be designed using machine learning (ML) approaches and/or 
include ML as part of the design. When preparing a premarket submission for control 
algorithms using ML approaches or designs, we recommend manufacturers describe 
the model (e.g., model architecture, implementation parameters) and training process 
for the ML control algorithm design. This should include information about the study 
design (e.g., patient population, any annotation process, data collection processes, 
how the data were partitioned and used to collect data for training and testing 
purposes). Manufacturers should describe how the patient population and methods 
used to develop and test the ML algorithms are representative of the intended patient 
population and use of the device. 
(2) Sensors 
A physiologic-measuring sensor of a PCLC device provides a measured feedback variable that 
has a relationship with a controlled physiologic variable to the control algorithm (see Figure 1). 
In many scenarios, direct sensing of the controlled physiologic variable is not possible, and a 
sensor can provide a feedback variable (see Figure 1) to the control algorithm based on a 
representation of a physiologic variable. For example, when automatically delivering oxygen to 
neonates, it might not be possible to run continuous blood gas measurement to determine arterial 
oxygen saturation (SaO2), the physiologic variable intended to be controlled, and the 
manufacturer would need to rely on measurement of functional peripheral oxygen saturation 
(SpO2), the feedback variable, as sensed by a pulse oximeter. In this example, the objective of 
the PCLC technology is to control SaO2, and thus, the accuracy of SpO2 as a measure of SaO2 
should be characterized across the intended patient population and considered in the design. The 
relationship between the feedback variable measured by the sensor and the controlled 
physiologic variable of interest will affect the safety and performance of the PCLC device, and 
the performance of the feedback variable should be established and limitations of the relationship 
quantified for the intended application, user, patient population, and environment of use 
considering appropriate physiologic and environmental variability. For example, in the case of an 
automated anesthesia delivery system based on EEG sensors, the effect of concomitant drugs 
(e.g., neuromuscular blockers, vasopressors), motion artifact, and surgical disturbances (e.g., 
electrocautery artifact) on the sensed depth of hypnosis should be considered across the expected 
patient population. 
   
Manufacturers should consider the risks related to inadequate sensor performance within the 
PCLC device and determine design specifications related to the sensor to ensure that the PCLC 
device performs as intended. We recommend manufacturers consider the following when 
designing or selecting physiologic-measuring sensors to be used as part of a PCLC device:  
 
• Sensor performance including measurement accuracy and precision in relation to the 
physiologic variable of interest.

---

<!-- Page 21 -->
Contains Nonbinding Recommendations 
 
 
17 
 
• Sensor uncertainty or deviation from a best fit value in relation to the physiologic 
variable of interest across the expected measurement range as it may affect the overall 
accuracy of the PCLC system.  
• Response time (i.e., latency) and bandwidth of the sensor to a change in the 
physiologic variable of interest. Sensors inherently exhibit some delay when 
measuring a change in the physiologic variable of interest. This delay could be 
negligible in the overall performance of the PCLC device, or it could have 
detrimental impact on the performance. Manufacturers should account for and 
mitigate this response delay.  
• Any changes in sensor performance as a function of measurement range (e.g., pulse 
oximeters can have degraded accuracy at low saturations) within the relevant range 
for the PCLC device. 
• Any changes in sensor performance due to confounding factors in the intended patient 
population (e.g., interference from concomitant therapies). 
• Any change in sensor performance due to environmental factors. 
• Any change in sensor performance due to calibration drift over time. 
• Sensor update rate (i.e., the frequency that a sensor is designed to provide readings to 
the control algorithm).  
• Electronic data interface specifications. 
• Sources of signal artifacts that can affect sensor performance. Measurement devices 
can include signal quality detection mechanisms that identify when the sensed data is 
insufficient to report accurate measurements. Manufacturers of PCLC devices should 
consider if such systems are present, how the information is communicated to the 
control algorithm, and the response of the control algorithm to poor signal quality or 
missing data. 
• For some PCLC devices, it may be necessary to monitor sensor performance so that 
the system can detect faults related to the sensor or identify calibration drift over time 
and revert to back up sensors or fallback modes as appropriate. 
 
Additional sensors can be included as part of an automated medical device with PCLC 
technology to provide redundancy or additional information about the patient’s condition. For 
each sensor used as part of the PCLC device, the above items should be considered for the 
individual sensors. 
(3) Actuators 
The actuator (e.g., infusion pump, gas blender) component of a PCLC device receives a 
controller output variable from the control algorithm and converts it to the manipulated variable, 
that is the physical delivery or removal of energy or article (e.g., therapy) to the patient (see 
Figure 1). Failure of the actuator can cause therapy delivery to stop or result in delivery of 
therapy falling outside acceptable limits.  
 
We recommend manufacturers consider the following when designing or selecting an actuator to 
be used as part of a PCLC device:

---

<!-- Page 22 -->
Contains Nonbinding Recommendations 
 
 
18 
 
• Accuracy and precision of energy or article delivery across the range that can be 
applied by the PCLC device and over clinically relevant timescales for the PCLC 
device (i.e., actuator performance should be demonstrated over delivery periods 
shorter than or equal to the PCLC algorithm update periods).  
• Response time of the actuator to the signal from the control algorithm (e.g., 
considering start-up delay with an infusion pump). 
• Physical limitations of the actuator (e.g., maximum flow rate) and compatibility with 
the control algorithm (e.g., errors resulting from saturation of the actuator).  
• Electronic data interface specifications. 
• Communication delay times associated with the output of the control algorithm. 
• For some PCLC devices, it may be necessary to monitor the actuator performance so 
that the system can detect faults related to the actuator and revert to fallback modes as 
appropriate. 
(4) System Integration 
A PCLC device can be designed as a platform-based, distributed, or loosely-coupled system of 
components that exchange information with each other. For example, sensors, actuators, and 
control algorithms may be integrated as a PCLC device using an interoperability platform. In this 
case, we recommend that manufacturers consider how the design may impact the system’s ability 
to function as intended, such as related to component interfacing and system integration issues 
that can potentially affect the quality, frequency, adequacy, integrity, throughput, timeliness, and 
syntax and semantics of data and control exchanged between system components. For issues 
related to the interoperability of system components, manufacturers should refer to the FDA 
guidance document titled “Design Considerations and Premarket Submission Recommendations 
for Interoperable Medical Devices.”30 For PCLC devices comprised of interoperable medical 
devices or as part of an integrated clinical environment, we recommend manufacturers follow 
ANSI/AAMI/UL 2800-1 and ANSI/AAMI 2700-1, as applicable to their device design. 
(5) System Safety Features 
In addition to the primary control loop, there are a number of design elements for PCLC 
technology that can enhance safety and ensure the system meets its design requirements.31 We 
recommend manufacturers consider safety features of the system such as: 
 
• Fallback modes – During the presence of some patient-related disturbances or device 
failure conditions, the PCLC technology would not be able to maintain delivery of 
therapy as intended. Manufacturers should design their PCLC technology to detect 
unsafe conditions and have procedures in place for fault tolerance to ensure patient 
safety. We recommend manufacturers follow IEC 60601-1-10 (e.g., Clause 8.2.2.3 
“Fallback Mode” of IEC 60601-1-10 Edition 1.2 2020-07) related to fallback modes. 
We recommend that when a device is in a fallback mode, the ability of the user to 
safely take over delivery of therapy should not be impeded. When designing fallback 
modes that involve a user response, manufacturers should consider the user’s reaction 
 
30 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-considerations-
and-pre-market-submission-recommendations-interoperable-medical-devices 
31 See 21 CFR 820.30

---

<!-- Page 23 -->
Contains Nonbinding Recommendations 
 
 
19 
 
time, access to the necessary device programming, and training needed to respond 
safely (e.g., considering the time needed to respond to prevent a hazardous situation). 
• Transparent entrance and exit criteria – The initiation of automated therapy 
delivery can depend on the patient state, how well the control algorithm is informed 
of that state, and the system response. We recommend manufacturers incorporate 
entrance criteria for the PCLC device so that the control algorithm has sufficient 
information about the patient state in order to initiate therapy as intended. Similarly, 
when a PCLC mode is ending the device should communicate relevant information to 
the user about the patient and device states for the user to safely manage the patient. 
• Constraints on delivered energy or article – We recommend manufacturers 
consider designing PCLC devices to constrain the energy or article delivered to 
minimize unsafe conditions. For example, where the controller is designed to 
administer the drug in a manner that is consistent with the drug labeling, such as the 
rate of infusion of a particular drug, this design would, among other things, minimize 
unsafe conditions. Another example of a clinical constraint is a closed-loop 
oxygenation and anesthesia gas delivery device in which the controller should not 
deliver oxygen below 21% to avoid hypoxic mixtures. The following provides 
examples of constraints to consider, noting that they would not be applicable to all 
device types:  
• Upper and lower limits of delivered energy or article. 
• Total delivered energy or article over time, including that which has been 
delivered but the body has not yet responded to. 
• Rate of change of energy or article delivered (e.g., critical damping to avoid 
oscillations in the system). 
• Allowable overshoot and undershoot. 
• Data logging – We recommend that PCLC devices follow IEC 60601-1-10 (e.g., 
Clause 6.3 “PCLCS Variable Logging” of IEC 60601-1-10 Edition 1.2 2020-07) 
related to data logging of variables for a PCLC device. As part of data and time 
recording capabilities, manufacturers should consider maintaining a log of system 
variables and parameters, any mode switches including entering a fallback mode, 
number of adjustments to the physiologic variable, number of clinician interventions, 
any inputs to the user interface, and any other information essential to conduct a root 
cause analysis in the event of system failure, malfunction, and/or patient harm. 
Information from data logging can be used in reporting MDRs,32 including those 
related to automation use-related faults. For PCLC devices that are part of an 
integrated clinical environment, we recommend manufacturers follow ANSI/AAMI 
2700-2-1: Medical devices and medical systems—Essential safety and performance 
requirements for equipment comprising the patient-centric integrated clinical 
environment (ICE): Part 2-1: Particular requirements for forensic data logging when 
designing their data logging systems. 
 
32 For more information on Medical Device Reporting see the “FDA Guidance Document: Medical Device 
Reporting: Guidance for Industry and Food and Drug Administration Staff” available at 
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-reporting-
manufacturers

---

<!-- Page 24 -->
Contains Nonbinding Recommendations 
 
 
20 
 
• Alarms – When manufacturers include an alarm system, as described in IEC 60601-
1-10 (e.g., Clause 6.2 “Alarm Systems” of IEC 60601-1-10 Edition 1.2 2020-07), to 
notify users when hazardous situations exist, we recommend manufacturers follow 
IEC 60601-1-8: General requirements, tests and guidance for alarm systems in 
medical electrical equipment and medical electrical systems or an equivalent method 
to evaluate the alarm system. As discussed in IEC 60601-1-8 Edition 2.2 2020-07, 
alerts intended as a means of risk control represent an alarm condition and should be 
evaluated as part of the alarm system.  
(6) User Interface 
We recommend that manufacturers consider the user interface as an important safety element of 
the PCLC device and follow IEC 60601-1-10 (e.g., Clause 6.1 “Usability” of IEC 60601-1-10 
Edition 1.2 2020-07) when developing their user interface. The user interface of a PCLC device 
directly influences aspects of a user’s understanding of the control algorithm and energy or 
article that it is delivering. We recommend manufacturers consider user interface designs for 
their PCLC device that: 
 
• Communicate relevant patient health status and device states considering a user’s 
understanding of the device’s operation and previous knowledge (e.g., with relevant 
devices) to allow appropriate responses. 
• Ensure users have operational transparency, and can understand, supervise, monitor, 
and program the PCLC device operating at different modes. 
• Provide sufficient information to avoid confusion about the current and past operating 
states of the device. 
• Identify and communicate situations when the PCLC device is approaching safe 
operating limits or cannot safely control the intended physiologic variable (e.g., 
delivery rate saturated at the maximum value for longer than expected without the 
control objective being met). 
• Notify the user when the device enters a fallback mode due to occurrence of a fault in 
the system or switches to a different mode due to a change in the patient state 
including presenting clear information of why the change occurred, current mode of 
the device, and information for the user to successfully intervene if necessary. 
• For example, if the PCLC device delivers a drug in closed-loop mode and 
encounters a non-resolvable issue (e.g., sensor disconnected), the PCLC device, 
while notifying the user, can convert to an open-loop mode where therapy 
continues to be delivered at a pre-determined level. For the user to successfully 
intervene, information about the state of the patient such as the amount of drug 
delivered during the automatic mode, history of vital signs, reason for switching 
the mode, and how the issue can be resolved, should be communicated to the user 
through the device user interface. Likewise, if the automatic mode is to be 
resumed, the device should prompt the user to input relevant information about 
therapy that was delivered by the user in order to ensure any safety constraints are 
met. 
• Communicate current and past quantity of energy or article delivered or removed, 
including with alarms as necessary, for providing transparency on device operation

---

<!-- Page 25 -->
Contains Nonbinding Recommendations 
 
 
21 
 
and, for example, preventing delayed detection of physiologic deterioration or 
identifying oscillatory behavior of the system. A PCLC device can stabilize a 
physiologic variable that has associated physiologic monitoring alarm conditions with 
automatic changes in therapy that could go unnoticed by the user. This could result in 
patient deterioration that goes unnoticed, where, without the PCLC device applied, it 
could be recognized by the user from an alarm on the patient monitor due to a change 
in the physiologic variable or due to the need to change the dose of therapy.  
 
Verification and Validation Considerations 
The verification (demonstrating that the device meets specifications) and validation 
(demonstrating that the specified design meets user needs and intended uses) activities warranted 
will depend on the level of risks associated with the device, the purpose of the PCLC technology, 
and the intended use of the device. The medical device manufacturer must verify and validate the 
PCLC device design consistent with 21 CFR 820.30. For example, a manufacturer should: 
 
• Verify that sensor(s) meet all specifications for the PCLC device. 
• Verify that actuator(s) meet all specifications for the PCLC device. 
• Verify that control algorithms meet all specifications for the PCLC device. 
• Verify that the PCLC device is correctly integrated so that the interfacing, interaction, 
and/or communication between sensors, actuators, control algorithms, and other 
system components (e.g., interoperability platform and data logger) meet device 
specifications. 
• Verify and validate the performance of all safety features including fallback modes 
and alarm systems. For fallback modes that require a user response, this should 
include verification that users can respond and perform the expected tasks. 
• Verify that the PCLC device response related to safely controlling a physiologic 
variable meets specifications during normal and foreseeable worst-case conditions 
considering the range of device configurable parameters, modes of operation, clinical 
conditions, and patient conditions (i.e., inter-patient and intra-patient variabilities) 
that can affect the system performance. This can include a parameter sensitivity 
analysis to demonstrate that the device meets specifications across all combinations 
of adjustable parameter values. When applicable, we recommend providing graphical 
presentation(s) of time-domain responses such that any overshoot and undershoot of 
the response following a change in the desired delivery rates or physiologic set points 
can be determined at settings that will be commonly used. In general, we recommend 
that you characterize the PCLC device response specifications with a patient or model 
of a patient (e.g., animal or computational model, See Sections VI.A and VI.B) in the 
loop with the PCLC device. 
• Verify the PCLC device response meets specifications during foreseeable functional 
disturbances (e.g., sensor noise and/or drop out, actuator failure, worst-case delivery 
rates) and clinical disturbances (e.g., change in the patient’s response caused by a 
change in concomitant therapy), and demonstrate that the system responds as 
intended under these conditions. When applicable, we recommend providing 
graphical presentation(s) of time-domain responses to demonstrate that the system 
responds as expected and meets performance specifications during foreseeable

---

<!-- Page 26 -->
Contains Nonbinding Recommendations 
 
 
22 
 
functional and clinical disturbances. This can include periods without changes in the 
physiologic set point but during representative intra-patient variability and 
disturbances to demonstrate, for example, any oscillatory behavior of the system or 
reporting the time within a prespecified range in relation to the command variable 
(e.g., compared to a control group). 
• Validate the user interface(s) such as evaluating that user(s) are capable of correctly 
using the interface(s) including interpreting the therapy being provided by the PCLC 
device. 
• Validate that use-related risks are mitigated to an acceptable level. 
• Validate that the users understand how the system enters and exits different modes 
including device-human exchanges in operation and what the user needs to do during 
those periods. 
• Validate risk control measures for the user to respond when fault conditions and 
automation-related use errors occur. 
• Validate that the PCLC response specifications (e.g., Clause 8.2.2.6 “Responses of 
the PCLCS” of IEC 60601-1-10 Edition 1.2 2020-07) support safe and effective 
operation during normal and foreseeable worst-case conditions (e.g., including 
conditions throughout the expected duration of use of the device in a patient). 
• Validate that the system will perform as intended. 
 
As part of the device performance testing typically submitted in a premarket submission, a 
manufacturer should include documentation on the results of verification and validation for the 
PCLC device that addresses the elements listed above. This can include bench, computational, 
animal, and/or clinical testing as discussed below in Section VI. When reporting non-clinical 
bench testing, manufacturers should consider the recommendations in the FDA guidance 
document, “Recommended Content and Format of Non-Clinical Bench Performance Testing 
Information in Premarket Submission.”33 
VI. Non-Clinical Testing Considerations  
Evaluation of medical devices with PCLC technology necessitates a broad range of assessments 
common to medical devices such as biocompatibility, electromagnetic compatibility (EMC), 
electrical safety, sterility, magnetic resonance imaging (MRI) compatibility, radio frequency 
wireless technology, cybersecurity, and software verification and validation. Manufacturers 
should refer to specific guidance documents related to these topics to determine when and what 
type of testing should be considered for their PCLC device. Additional testing not related to the 
PCLC technology could be warranted depending on the risks of the device. 
 
When developing and evaluating a PCLC device, a combination of bench, computational, 
animal, and/or clinical test methods could be needed. Regardless of the specific test methods, we 
recommend that manufacturers consider following a structured method of designing disturbance 
and uncertainty scenarios to stress-test the PCLC device and ensure that the PCLC device is 
tested in clinically relevant worst-case conditions on the final finished device. The information in 
 
33 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/recommended-content-
and-format-non-clinical-bench-performance-testing-information-premarket

---

<!-- Page 27 -->
Contains Nonbinding Recommendations 
 
 
23 
 
this section is intended to provide manufacturers with considerations for designing non-clinical 
testing for medical devices with PCLC technology. Clinical study designs for PCLC devices are 
expected to vary because of the variety of intended uses, risk profiles, and device designs. 
Therefore, this guidance document does not provide specific recommendations for performing 
clinical studies. Manufacturers are encouraged to refer to the FDA guidance document, “Design 
Considerations for Pivotal Clinical Investigations for Medical Devices” 34 and to interact with 
the Agency through the Q-Submission process35 when designing clinical studies for PCLC 
devices. 
 
Animal Testing 36 
Animal testing of PCLC devices should address factors that cannot be evaluated through 
analysis, bench tests or in a clinical study. Manufacturers are encouraged to refer to the FDA 
guidance document, “General Considerations for Animal Studies Intended to Evaluate Medical 
Devices”37 for more information on animal studies. When in vivo animal studies are used to 
evaluate a PCLC device, we recommend manufacturers consider the following in their study 
design and include this information in premarket submissions as applicable:  
 
• The clinical relevance of the animal model. The animal model should provide a test 
system that reasonably simulates use in humans. Manufacturers should provide 
scientific evidence to support the animal model chosen. 
• Identification of the relevant physiologic and anatomic differences between the 
animal model and intended human use. Manufacturers should justify why the animal 
model is appropriate given the physiologic and anatomic differences between the 
animal model and human use. 
• Differences in the expected intra- and inter-subject variability in the response of the 
physiologic variable to the delivered energy or article in the selected animal model 
compared to human use. 
• If the PCLC device used in the testing differs from the final finished device, an 
assessment of why any differences between the device used and final finished device 
do not affect the study results.  
• Use of a risk-based approach in developing animal study protocols. The animal study 
should address known risks of the PCLC device, which can be identified through 
literature review, device design, bench testing and basic exploratory studies. The risks 
inherent to the indications for use should be considered as well. 
 
34 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-considerations-
pivotal-clinical-investigations-medical-devices 
35 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program 
36 FDA supports the principles of the “3Rs,” to replace, reduce, and/or refine animal use in testing when feasible. 
We encourage sponsors to consult with us if they wish to use a non-animal testing method they believe is suitable, 
adequate, validated, and feasible. We will consider if such an alternative method could be assessed for equivalency 
to an animal test method. 
37 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-considerations-
animal-studies-intended-evaluate-medical-devices

---

<!-- Page 28 -->
Contains Nonbinding Recommendations 
 
 
24 
 
• Study conduct should be guided by a protocol with pre-defined objectives that assess 
each identified risk, and acceptance criteria should be developed with a scientific 
rationale. Objectives to evaluate potential adverse effects on the structure and 
function of tissue locally and systemically should be included. 
• Best practices for the development, conduct and presentation of these animal studies 
while incorporating modern animal care and use strategies.  
• Any differences in the timeline (i.e., amount of time the PCLC device is applied to 
the animal) of the animal study versus the clinical study or anticipated clinical use.  
 
Animal studies intended to evaluate safety must be performed in compliance with 21 CFR Part 
58, Good Laboratory Practice for Nonclinical Laboratory Studies (GLP). Prior to performing 
animal studies, we recommend that manufacturers seek FDA input on the animal study protocol 
using the Q-Submission Program.38 In addition, if you are proposing to use a non-animal testing 
method that you believe is suitable, adequate, validated, and feasible, we also recommend that 
you discuss the proposal using the Q-Submission Program. We will consider if such an 
alternative method could be assessed for equivalency to an animal test method.  
 
PCLC Device Testing Using Mathematical and 
Computational Models  
PCLC devices are complex and there are many types of disturbances that could lead to unsafe 
conditions or to the device not functioning as intended. Evaluating a PCLC device in all possible 
clinically relevant scenarios using animal and/or clinical studies may not be feasible. Closed-
loop systems across engineering domains are traditionally designed using computational and 
mathematical modeling approaches to increase efficiency (e.g., by effective iterative design), 
reduce costs, and prevent errors during system development. Evaluation of a PCLC device using 
a computational and/or mathematical model of the patient response can provide an alternative to 
or supplement animal and/or clinical studies. We recommend that manufacturers refer to the 
FDA guidance document “Reporting of Computational Modeling Studies in Medical Device 
Submissions” 39 for FDA’s current thinking on information on computational modeling studies 
that should be collected and included in a premarket submission. 
 
The validity of a model-based evaluation of a PCLC device will depend on, among other study 
design aspects, the computational model used and the evidence supporting that model. Generally, 
the patient model(s) used to design the control algorithm for a PCLC device will be different 
than the model(s) used for evaluation to validate device performance. For example, the model 
used for design may be a low-order model (e.g., lumped-parameter model) that captures basic 
physiologic responses directly related to the inputs and outputs of the PCLC device, while the 
model used for evaluation may have a higher level of fidelity including, for example, a broader 
range of physiologic responses, clinical inputs, and interactions with other physiologic systems 
in order to simulate clinically relevant scenarios. We recommend each computational model used 
in PCLC device development, whether used for design or evaluation, be evaluated for predictive 
capability within its context of use.  
 
 
39 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/reporting-
computational-modeling-studies-medical-device-submissions

---

<!-- Page 29 -->
Contains Nonbinding Recommendations 
 
 
25 
 
 
When developing a computational patient model (or selecting a previously developed 
computational patient model) for testing a PCLC device, we recommend the following 
considerations: 
 
• Characterization of the input and output response of interest. 
• Identification and characterization of other physiologic system responses known to be 
impacted by the input or that interact with the physiologic system of interest (e.g., 
cardiovascular and pulmonary system interactions can result in therapy to one system 
affecting the other). 
• Identification and characterization of inter-patient variabilities (e.g., range of 
responses expected from different patients). 
• Identification and characterization of intra-patient variabilities (e.g., degree to which 
an individual response can change over the course of a procedure). 
• Identification and characterization of physiologic and clinical disturbance scenarios 
expected (e.g., changes in other therapies provided to the patient). 
• Assumptions of the model and how they can impact the testing and interpretation of 
the results. 
• Parameter selection including how parameters were identified and values selected, 
and why the values are applicable to the intended patient population. 
 
Model evaluation should be focused around the proposed model context of use, that is the role of 
the model in performance testing of the PCLC device under the intended clinical scenarios. We 
recommend credibility assessment of the computational patient model include consideration of: 
 
• Model verification,40 by addressing the credibility factors in American Society of 
Mechanical Engineering (ASME) V&V 40 Assessing Credibility of Computational 
Modeling Through Verification and Validation: Application to Medical Devices (i.e., 
“Verification” clause). We recommend manufacturers: 
• Identify sources of numerical error to include in calculation verification for the 
testing and computational patient model. Numerical Solver Error in ASME V&V 
40 would not be relevant for patient models that are systems of ordinary 
differential equations only.  
• Include justification of the selections of numerical error sources in the study 
report. 
• Model validation, that is, comparison of model predictions against independent 
experimental or clinical data that were not used for model development, by 
addressing the credibility factors in ASME V&V 40 (i.e., “Validation” clause). We 
recommend that manufacturers consider the following: 
• An assessment of the assumptions in the model to demonstrate that physiologic 
processes that have not been included in the model are not likely to impact results. 
 
40 Verification and validation in this section refer to the evaluation of computational models and are used as defined 
in the FDA guidance document, “Reporting of Computational Modeling Studies in Medical Device Submissions”

---

<!-- Page 30 -->
Contains Nonbinding Recommendations 
 
 
26 
 
• Uncertainty quantification and sensitivity analyses to evaluate the impact of inter-
patient and intra-patient variability on key parameters relevant to the input, 
output, and physiologic response of interest being evaluated.  
• Information on the subjects and conditions in the experimental or clinical studies 
that provide the comparative data in the context of computational patient models 
to enable an assessment of the validation results.  
• Assessment of the relevance of the validation activities to the context of use (for 
example, if a physiologic model is validated against data derived from animal studies, 
the validity of this extrapolation to predict human physiologic response should be 
assessed). 
 
Information to support the use of a computational patient model can come from validation results 
for sub-models of the overall patient model, historical validation results from previous versions 
of the patient model or related patient models, historical evidence of the model’s predictive 
ability for other contexts of use, or calibration results demonstrating good fits to experimental or 
clinical data. We recommend manufacturers provide a description of how the information used 
supports the model for its context of use.  
 
We encourage manufacturers to seek feedback on their credibility assessment plans for 
computational models and simulations used in PCLC device testing via the Q-Submission 
Program41 prior to performing model evaluation activities. 
(1) Analytical Assessments 
Analytical methods can sometimes be applied as part of the development process or to support a 
premarket submission to evaluate the performance, stability and robustness of a PCLC device. 
These methods generally use a mathematical model of the response of the physiologic variable to 
the delivered energy or article. The choice of analytical approach and its role in PCLC device 
evaluation will depend on the particular PCLC device, control algorithm design method (e.g., 
model-based), and the physiologic response. When analytical methods with mathematical models 
are used as part of a PCLC device evaluation, we recommend manufacturers consider the 
following and include this information in premarket submissions as applicable, along with the 
information above in Section VI.B. for each model used, in the testing: 
 
• Description of the analytical method and why it is applicable for the application given 
the processes to which it is applied (e.g., phase and gain margin for linear processes). 
• Description of how the analytical method is applicable to the particular PCLC 
application.  
• Limitations of the analysis methods to predict clinical performance (e.g., how 
simplifying assumptions impact the results). 
• Description of how device safety mechanisms and fallback modes mitigate any 
degradation in performance, stability, and robustness of the PCLC device due to the 
limitations and simplifying assumptions. 
 
41 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program

---

<!-- Page 31 -->
Contains Nonbinding Recommendations 
 
 
27 
 
(2) Entirely Virtual Testing 
In the context of this guidance, entirely virtual testing refers to testing that is performed 
completely in a simulated computer environment so that all parts of the system including the 
patient’s physiology and PCLC device components (e.g., physiologic-measuring sensor, control 
algorithm, actuator) are modeled. The advantage of this type of testing is that conditions can be 
simulated across a wide range of scenarios including inter-patient and intra-patient variability 
and uncertainty, device variability and uncertainty, and device failure modes. Data from such 
simulations can, for example, potentially identify situations that can result in unsafe conditions, 
demonstrate expected performance of the system across the intended patient population prior to a 
clinical and/or animal study, or provide an alternative to or supplement animal and/or clinical 
studies. 
 
When performing virtual testing, information demonstrating the validity of the individual models 
as well as the modeled system is important to support the virtual testing within its context of use. 
We recommend manufacturers consider the credibility assessment as discussed above in Section 
VI.B. for each model (e.g., patient’s physiology, physiologic-measuring sensor, actuator), as well 
as their interaction and the overall system implementation. This can include activities such as 
uncertainty quantification to evaluate how uncertainties associated with the individual models 
propagate through the simulations and affect the overall result. 
(3) Hardware-in-the-Loop Testing 
Hardware-in-the-loop testing can be performed using computational models of the patient’s 
physiology interfaced with the PCLC device hardware. This can enable testing of the PCLC 
device in real time and with the device hardware. In some situations, this can provide a more 
realistic type of testing that can be used to identify system failure modes and hardware 
limitations. In addition, both physiologic and non-physiologic disturbances expected during 
clinical use can be simulated on the bench, thereby identifying unsafe conditions early in the 
device development lifecycle.  
 
The patient model should be integrated with the device components in hardware-in-the-loop 
testing in a manner that would minimally affect the functionality of the system and not alter the 
realistic nature of the test (e.g., by introducing additional delays to the system). This will 
generally involve actuator transfer mechanisms to relay the actual output from the actuator to the 
computational patient model, and signal simulation and generation tools to communicate the 
output of the computational patient model to the sensor. The characteristics of these testing tools 
can impact the relationship between the bench testing results and device performance in a 
clinical environment. We recommend that manufacturers characterize the performance of the 
actuator transfer mechanisms and signal generators, including accuracy and time delays, and 
account for these properties in their test plans and analyses. 
 
VII. Human Factors Testing 
We recommend that manufacturers performing human factors testing of the PCLC device 
consider recommendations in the FDA guidance document, “Applying Human Factors and

---

<!-- Page 32 -->
Contains Nonbinding Recommendations 
 
 
28 
 
Usability Engineering to Medical Devices,”42 which identifies different types of human factors 
validation testing, including simulated use testing and actual use testing. Simulated use testing in 
the context of PCLC devices can include hardware-in-the-loop configurations as described above 
in Section VI.B.(3) that use computational models of patient physiology. While human factors 
validation testing is typically conducted under simulated use conditions in order to ensure the 
testing of all risk management measures related to critical tasks, testing in a clinical setting might 
be needed to enable realistic and meaningful evaluation because automation-related use errors 
might not be predictable. In these cases, it would be appropriate to perform human factors 
validation testing during actual use of the device. We recommend manufacturers consider if 
simulated environments are sufficient to evaluate each use scenario related to device automation 
or if actual use testing may be warranted. When performing human factors testing in either 
simulated or actual use environments, we recommend that use scenarios and post-test surveys be 
designed to capture information on automation-related hazards such as complacency and 
automation bias. When labeling includes instructions for the user to recognize an emergent 
unsafe condition and intervene to prevent harm, results of human factors testing should be 
provided to show that reliance on user intervention constitutes an adequate risk control measure. 
Whether simulated or actual use testing is used, test participants should receive training that is 
representative of the training provided during actual use of the device. We encourage 
manufacturers to seek feedback on the human factors testing protocol for the PCLC device via 
the Q-Submission Program43 prior to conducting the test.  
 
Training 
We recommend appropriate training be developed for users of the PCLC device in accordance 
with the FDA guidance document, “Applying Human Factors and Usability Engineering to 
Medical Devices.”44 The training plan should be provided in your premarket submission and 
should be designed to demonstrate and document that users have a level of competence to safely 
use the PCLC device after receiving the training. When designing training materials for intended 
users of PCLC devices, we recommend manufacturers consider how the training ensures the 
user’s understanding of the following: 
 
• The role the device plays in the management of the patient. 
• Factors and conditions that can affect the PCLC device performance. 
• Configuring and operating the device through the user interface. 
• The different automated and non-automated modes including: 
• Which modes the device can automatically switch to and when it will switch to 
those modes (e.g., fallback modes). 
• Which modes the user can select and when each mode should be used in the 
clinical management of the patient. 
 
42 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-
factors-and-usability-engineering-medical-devices 
43 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program 
44 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-
factors-and-usability-engineering-medical-devices

---

<!-- Page 33 -->
Contains Nonbinding Recommendations 
 
 
29 
 
• How to switch out of an automated mode (e.g., when the user considers the 
therapy being delivered to not be as expected or appropriate based on the clinical 
situation).  
• How to detect when the control strategy is nearing its limitations and could fail (for 
example, if the therapy is being delivered at the maximum rate and the patient is not 
responding) and what the response of the user should be.  
• Steps to take to respond to device errors or warning messages (e.g., troubleshooting 
expected device issues). 
• Responding to automation-related use errors that would be unanticipated by the user.  
 
The training should include information about limitations of automation technology, as well as 
the potential use errors anticipated during the use of the device. Training plans for PCLC devices 
could include simulation-based training in appropriate clinical settings in addition to a standard 
training program. For example, simulation-based training could be dedicated to device 
automation interaction functions and related hazards, while a standard training program could be 
dedicated to non-automated device interaction considerations and hazards. 
 
It may be important for trainees to experience complacency, automation bias, and loss of 
situational awareness related to use-related hazards (see Section V.A(3)), automation failures, 
alert or warning failures, infrequent critical events, and inappropriate responses. Experiencing 
these hazardous situations during practice sessions can help reduce automation-related use errors 
by encouraging critical thinking when using automated systems. Experiencing these hazardous 
situations will also facilitate training in automation-related use error management and 
development of the skills needed to appropriately respond to use errors.  
 
VIII. Labeling 
The following recommendations are intended to help prepare labeling that satisfies the applicable 
requirements of 21 CFR parts 801 and 809, and applicable labeling requirements for premarket 
submissions (e.g., 21 CFR 807.87(e) and 21 CFR 814.20(b)(10)).  
 
We recommend that devices with PCLC technology include in the labeling all information 
identified in Clause 5.1 “Instructions for Use” and Clause 5.2 “Technical Description” in IEC 
60601-1-10 Edition 1.2 2020-07, as summarized in Annex C of that document, or equivalent 
information. In addition, we recommend that the following information be included in the device 
labeling as appropriate: 
 
• Description of the PCLC device including the following components: 
• Physiologic measuring sensor including performance specifications, identification 
of specific models, software versions, and configuration (e.g., bandwidth) that the 
system can be used with, and any limitations on how or where the sensor can be 
applied to the patient compared to the cleared or approved standalone device (e.g., 
a standalone patient monitoring medical device might have sensors that could be 
applied to different anatomical locations, but the PCLC device could be validated 
to only place the sensor at a specific anatomical location).

---

<!-- Page 34 -->
Contains Nonbinding Recommendations 
 
 
30 
 
• Actuator including performance specifications, energy or articles that the system 
can deliver, identification of specific models, software versions, and configuration 
that the system can be used with and, as applicable, maximum and minimum 
delivery rates of the article or maximum amount of article that the system can 
deliver. 
• Description of control algorithm for all modes where the device can operate and 
performance specifications related to the PCLC device response for each mode 
including, for example, the time it takes to reach a target level and steady-state 
error and any constraints on the delivery of energy or article (e.g., so that the 
delivery is consistent with the drug label, see Section V.B.(5)). 
• Alarm information including descriptions of the alarm conditions, related 
hazardous situations, and how the user is expected to respond. 
 
• Descriptions of the conditions under which the device has been validated to operate 
including patient conditions, disturbances (e.g., other therapies provided to the 
patient, sensor noise), device configurations (e.g., range of parameters), and device 
use conditions (e.g., duration of PCLC device use during clinical studies). This can 
include summaries of clinical and/or non-clinical testing to provide the user 
information on how the device should be configured. 
 
• Description of how the PCLC device operates (i.e., mental model as discussed in IEC 
60601-1-10) that is sufficient to allow the user to understand when the device is 
reaching its limitations, potentially creating a hazardous situation, and the appropriate 
actions to mitigate the risk of the hazardous situation. 
 
• Descriptions of what the PCLC device does and does not do related to managing or 
treating the patient and what the user should do to ensure appropriate patient 
monitoring and management. This should include a description of the user’s 
responsibilities related to the PCLC device operation. 
 
• Identification of entrance criteria related to the patient’s condition and what 
information should be provided by the user for each PCLC mode to operate. 
 
• Descriptions of fallback modes including scenarios that can result in the device 
entering a fallback mode and the expected response of the user (e.g., instructions for 
the user to switch to a different mode). 
 
• Information on the system data logging features, including who has access to them. 
 
• Information on how to program and operate the system, including how to change the 
set point and operational mode of the device. 
 
• Information on how the user interface communicates the patient’s condition, 
delivered energy or article, and operating mode of the device.

---

<!-- Page 35 -->
Contains Nonbinding Recommendations 
 
 
31 
 
• Accessories that have been tested to function as intended with the PCLC device (for 
interoperable medical devices, see the FDA guidance document “Design 
Considerations and Pre-market Submission Recommendations for Interoperable 
Medical Devices”45 for additional labeling recommendations). 
 
• Instructions for device users on how device functionality should be confirmed before 
use including testing that all components (e.g., sensors and actuators), device modes, 
and safety features are functioning as intended. 
 
• Identification of any PCLC components that should not be replaced, for example, 
during maintenance or if only representatives from the manufacturer should replace 
certain components or perform maintenance including, where appropriate, 
information on the device of who to contact for servicing.   
 
• For reusable (e.g., medical facility) PCLC components, we recommend affixing a 
label that identifies who to contact in the event servicing is needed and the use life of 
the PCLC component. 
 
• Procedures to verify operation of all device modes and safety features following 
software updates. 
 
 
 
 
 
 
45 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-considerations-
and-pre-market-submission-recommendations-interoperable-medical-devices

<!-- fulltext-end -->
