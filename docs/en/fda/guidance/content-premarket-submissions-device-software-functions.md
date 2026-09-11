---
title: "Content of Premarket Submissions for Device Software Functions: Guidance for Industry and Food and Drug Administration Staff"
description: "FDA CDRH Final Guidance Document"
published: 2023-06-14
---

# Content of Premarket Submissions for Device Software Functions: Guidance for Industry and Food and Drug Administration Staff

**Published**: 2023-06-14

**Status**: Final
**Type**: Guidance Document
**Category**: Digital Health & Cybersecurity
**Topics**: Premarket, Digital Health
**Docket**: FDA-2021-D-0775

::: tip Official Source
[https://www.fda.gov/regulatory-information/search-fda-guidance-documents/content-premarket-submissions-device-software-functions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/content-premarket-submissions-device-software-functions)
PDF: [https://www.fda.gov/media/153781/download](https://www.fda.gov/media/153781/download)
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
FDA notes that in particular, the QMSR does not utilize certain terms, such as “Design 
Controls,” and “Design Validation.” The elements that comprise these terms are described in 
ISO 13485:2016, Clause 7.3 and its subclauses, which are incorporated by reference in the 
QMSR.

---

<!-- Page 2 -->
Contains Nonbinding Recommendations
Content of Premarket Submissions for 
Device Software Functions
______________________________________________________________________________
Guidance for Industry and
Food and Drug Administration Staff
Document issued on June 14, 2023. 
The draft of this document was issued on November 4, 2021.
This document supersedes Guidance for the Content of Premarket 
Submissions for Software Contained in Medical Devices, May 2005.
For questions about this document regarding CDRH-regulated devices, contact the Digital Health 
Center of Excellence at digitalhealth@fda.hhs.gov. For questions about this document regarding 
CBER regulated devices, contact the Office of Communication, Outreach, and Development 
(OCOD) at 1-800-835-4709 or 240-402-8010, or by email at ocod@fda.hhs.gov.
U.S. Department of Health and Human Services
Food and Drug Administration
Center for Devices and Radiological Health
Center for Biologics Evaluation and Research 
Center for Drug Evaluation and Research
Office of Combination Products in the Office of the 
Commissioner

---

<!-- Page 3 -->
Contains Nonbinding Recommendations
Preface
Public Comment
You may submit electronic comments and suggestions at any time for Agency consideration to 
https://www.regulations.gov. Submit written comments to the Dockets Management Staff, Food 
and Drug Administration, 5630 Fishers Lane, Room 1061, (HFA-305), Rockville, MD 20852.  
Identify all comments with the docket number FDA-2021-D-0775. Comments may not be acted 
upon by the Agency until the document is next revised or updated.
Additional Copies
CDRH
Additional copies are available from the Internet. You may also send an email request to CDRH-
Guidance@fda.hhs.gov to receive a copy of the guidance. Please include the document number 
GUI00000337 and complete title of the guidance in the request.
CBER
Additional copies are available from the Center for Biologics Evaluation and Research (CBER),
Office of Communication, Outreach, and Development (OCOD), 10903 New Hampshire Ave.,
Bldg. 71, Room 3128, Silver Spring, MD 20993-0002, or by calling 1-800-835-4709 or 240-402-
8010, by email, ocod@fda.hhs.gov or from the Internet at
https://www.fda.gov/vaccines-blood-biologics/guidance-compliance-regulatory-information-
biologics/biologics-guidances.
CDER
Additional copies are available from the Center for Drug Evaluation and Research (CDER),
Office of Communication, Division of Drug Information, 10001 New Hampshire Ave.,
Hillandale Bldg., 4th Floor, Silver Spring, MD 20993-0002, or by calling 855-543-3784 or 301-
796-3400, or by email, druginfo@fda.hhs.gov, or from the Internet at 
https://www.fda.gov/drugs/guidance-compliance-regulatory-information/guidances-drugs.

---

<!-- Page 4 -->
Contains Nonbinding Recommendations
Table of Contents
I. 
Introduction ............................................................................................................................. 1
II. 
Background ............................................................................................................................. 2
III. Scope ....................................................................................................................................... 4
IV. Definitions............................................................................................................................... 6
V. 
Documentation Level .............................................................................................................. 8
VI. Recommended Documentation ............................................................................................... 9
Documentation Level Evaluation ................................................................................... 12 
 
Software Description ...................................................................................................... 12 
 
Risk Management File ................................................................................................... 15 
 
Software Requirements Specification (SRS) ................................................................. 18 
 
System and Software Architecture Diagram .................................................................. 20 
 
Software Design Specification (SDS) ............................................................................ 22 
(1)
Basic Documentation Level ........................................................................................ 23 
(2)
Enhanced Documentation Level ................................................................................. 23 
 
Software Development, Configuration Management, and Maintenance Practices ........ 23 
(1)
Basic Documentation Level ........................................................................................ 24 
(2)
Enhanced Documentation Level ................................................................................. 24 
 
Software Testing as part of Verification and Validation................................................ 25 
(1)
Basic Documentation Level ........................................................................................ 25 
(2)
Enhanced Documentation Level ................................................................................. 26 
 
Software Version History ............................................................................................... 26 
 
Unresolved Software Anomalies .................................................................................... 27 
VII. Additional Information - Regulatory Considerations for Software Functions ..................... 28
Appendix A: Documentation Level Examples ............................................................................. 28
Appendix B: System and Software Architecture Diagram Examples .......................................... 39

---

<!-- Page 5 -->
Contains Nonbinding Recommendations
1
Content of Premarket Submissions for 
Device Software Functions
______________________________________________________________________________
Guidance for Industry and
Food and Drug Administration Staff
This guidance represents the current thinking of the Food and Drug Administration (FDA or 
Agency) on this topic. It does not establish any rights for any person and is not binding on 
FDA or the public. You can use an alternative approach if it satisfies the requirements of the 
applicable statutes and regulations. To discuss an alternative approach, contact the FDA staff 
or Office responsible for this guidance as listed on the title page.
I.
Introduction 
 
This guidance document is intended to provide information regarding the recommended 
documentation for premarket submissions for FDA’s evaluation of the safety and effectiveness 
of device software functions, which are software functions that meet the definition of a device 
under section 201(h) of the Federal Food, Drug, and Cosmetic Act (FD&C Act).1 This document 
replaces FDA’s Guidance for the Content of Premarket Submissions for Software Contained in 
Medical Devices issued on May 11, 2005, and updates FDA’s thinking related to the 
documentation FDA recommends sponsors include for the review of device software functions in 
premarket submissions.
The recommendations in this guidance are intended to facilitate FDA’s premarket review. This 
guidance describes information that would be typically generated and documented2 during 
software development, verification, and validation. The least burdensome approach was applied 
to identify the minimum amount of information that, based on our experience, would generally 
be needed to support a premarket submission for a device that uses software. During premarket 
review, FDA may request additional information that is needed to evaluate the submission. For 
example, in order to demonstrate a reasonable assurance of safety and effectiveness for devices 
1 The term “device” is defined in 201(h)(1) of the Federal Food, Drug, and Cosmetic (FD&C) Act to include an 
“instrument, apparatus, implement, machine, contrivance, implant, in vitro reagent, or other similar or related article, 
including any component, part, or accessory, which is ...intended for use in the diagnosis of disease or other 
conditions, or in the cure, mitigation, treatment, or prevention of disease, in man ... or intended to affect the structure 
or any function of the body of man...” and “does not include software functions excluded pursuant to section 520(o)” 
of the FD&C Act.
2 As a reminder, manufacturers of device software must create and maintain software-related documentation in 
accordance with the requirements of the Quality System (QS) Regulation (21 CFR 820.30 Subpart C – Design 
Controls of the Quality System Regulation).

---

<!-- Page 6 -->
Contains Nonbinding Recommendations
2
that use software, documentation related to the requirements of the Quality System Regulation 
(QSR) (21 CFR Part 820) is often a necessary part of the premarket submission. As part of QSR 
design controls, a manufacturer must “establish and maintain procedures for validating the 
device design,” which “shall include software validation and risk analysis, where appropriate” 
(21 CFR 820.30(g)). 
The documentation recommended in this guidance is based on FDA’s experience evaluating the 
safety and effectiveness of device software. However, sponsors may use alternative approaches 
and provide different documentation so long as their approach and documentation satisfy 
premarket submission requirements in applicable statutory provisions and regulations. For the 
current edition(s) of the FDA-recognized consensus standard(s) referenced in this document, see 
the FDA Recognized Consensus Standards Database.3 For more information regarding use of 
consensus standards in regulatory submissions, please refer to the FDA guidance titled 
Appropriate Use of Voluntary Consensus Standards in Premarket Submissions for Medical 
Devices4 and Standards Development and the Use of Standards in Regulatory Submissions 
Reviewed in the Center for Biologics Evaluation and Research.5
As stated above, this guidance identifies the software information FDA considers to generally be 
necessary to support a premarket submission. The recommendations in this guidance are also 
intended to facilitate FDA’s premarket review. FDA anticipates that the Agency and industry 
will need up to 60 days after the publication of this guidance to operationalize the 
recommendations discussed. However, CDRH intends to review any such information if 
submitted at any time.
In general, FDA’s guidance documents do not establish legally enforceable responsibilities. 
Instead, guidances describe the Agency’s current thinking on a topic and should be viewed only 
as recommendations, unless specific regulatory or statutory requirements are cited. The use of 
the word should in Agency guidances means that something is suggested or recommended, but 
not required.
II.
Background 
 
The purpose of this guidance is to describe FDA’s thinking on the recommended documentation 
sponsors should include in premarket submissions for FDA’s evaluation of the safety and 
effectiveness of device software functions. This thinking recognizes recent changes to the FD&C 
Act made by the 21st Century Cures Act (Cures Act), which amended section 520 of the FD&C 
Act and excludes certain software functions from the device definition. It also considers the 
rapidly evolving nature of digital health and recent FDA-recognized consensus standards related 
to software. This guidance, as described in Section III (Scope), is intended to complement other 
existing guidance documents that provide recommendations related to software, including the 
3 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm.
4 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/appropriate-use-
voluntary-consensus-standards-premarket-submissions-medical-devices.
5 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/standards-development-
and-use-standards-regulatory-submissions-reviewed-center-biologics-evaluation.

---

<!-- Page 7 -->
Contains Nonbinding Recommendations
3
guidance documents listed below. The following guidance documents represent a subset of FDA 
guidances with digital health content6 relevant to premarket software documentation activities. 
Please note the list is not exhaustive and is subject to change:
·
Multiple Function Device Products: Policy and Considerations7
·
Off-The-Shelf Software Use in Medical Devices8
·
Design Considerations and Premarket Submission Recommendations for Interoperable 
Medical Devices9
·
General Principles of Software Validation10
·
Content of Premarket Submissions for Management of Cybersecurity in Medical 
Devices11
·
Cybersecurity for Networked Medical Devices Containing Off-The-Shelf (OTS) 
Software12
·
Applying Human Factors and Usability Engineering to Medical Devices13
FDA encourages the consideration of these guidances when developing device software 
functions and preparing premarket software documentation.
The emergence of consensus standards related to software has helped to improve the consistency 
and quality of software development and documentation, particularly with respect to activities 
such as risk assessment and management. When possible, FDA harmonized the terminology and 
recommendations in this guidance with software-related consensus standards, such as the 
following examples. The following standards are not intended to represent an exhaustive list and 
are subject to change:14
·
ANSI/AAMI/ISO 14971: Medical devices - Applications of risk management to medical 
devices
·
ANSI/AAMI/IEC 62304: Medical Device Software - Software Life Cycle Processes
·
ANSI/AAMI SW91: Classification of defects in health software
6 Available at https://www.fda.gov/medical-devices/digital-health-center-excellence/guidances-digital-health-
content.
7 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/multiple-function-
device-products-policy-and-considerations.
8 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/shelf-software-use-
medical-devices.
9 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-considerations-
and-premarket-submission-recommendations-interoperable-medical-devices.
10 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-principles-
software-validation.
11 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/content-premarket-
submissions-management-cybersecurity-medical-devices.
12 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-
networked-medical-devices-containing-shelf-ots-software.
13 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-
factors-and-usability-engineering-medical-devices.
14 The most up-to-date list of voluntary FDA-recognized consensus standards is available at 
https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm.

---

<!-- Page 8 -->
Contains Nonbinding Recommendations
4
The Agency encourages the consideration of these FDA-recognized consensus standards when 
developing device software functions and preparing premarket software documentation. When 
assessing the appropriate Documentation Level for the device and the overall recommended 
documentation for inclusion in a premarket submission, please refer to Section V 
(Documentation Level) and Section VI (Recommended Documentation) of this guidance.  
Section 3308 of the Food and Drug Omnibus Reform Act of 2022, Title III of Division FF of the 
Consolidated Appropriations Act, 2023, Pub. L. No. 117-328 (“FDORA”), enacted on December 
29, 2022, added section 515C “Predetermined Change Control Plans for Devices” to the FD&C 
Act (section 515C). Under section 515C, FDA can approve or clear a predetermined change 
control plan (PCCP) for a device that describes planned changes that may be made to the device 
and that would otherwise require a supplemental premarket approval application or premarket 
notification. For example, section 515C provides that a supplemental premarket approval 
application (section 515C(a)) or a premarket notification (section 515C(b)) is not required for a 
change to a device if the change is consistent with a PCCP that is approved or cleared by FDA. 
Section 515C also provides that FDA may require that a PCCP include labeling for safe and 
effective use of a device as such device changes pursuant to such plan, notification requirements 
if the device does not function as intended pursuant to such plan, and performance requirements 
for changes made under the plan. If you are interested in proposing a PCCP in your marketing 
submission, we encourage you to submit a Pre-Submission to engage in further discussion with 
CDRH. See FDA’s guidance “Requests for Feedback and Meetings for Medical Device 
Submissions: The Q-Submission Program” available at https://www.fda.gov/regulatory-
information/search-fda-guidance-documents/requests-feedback-and-meetings-medical-device-
submissions-q-submission-program. 
III. Scope 
 
For the purposes of this document, FDA refers to a software function that meets the definition of 
a device as a device software function. For any given product, the term “function” is a distinct 
purpose of the product, which could be the intended use or a subset of the intended use of the 
product.15 For example, a product with an intended use to analyze data has one function: 
analysis. A product with an intended use to store, transfer, and analyze data has three functions: 
(1) storage, (2) transfer, and (3) analysis. As this example illustrates, a product may contain 
multiple functions.
This guidance is intended to cover device software functions. Examples include, but are not 
limited to, firmware and other means for software-based control of medical devices, software 
accessories to medical devices, and software only16 function(s) that meet the definition of a 
device. 
15 For details, see “Multiple Function Device Products: Policy and Considerations,” available at 
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/multiple-function-device-products-
policy-and-considerations.
16 “Software only” functions include device software functions intended to be operated on commercial OTS 
computing platforms.

---

<!-- Page 9 -->
Contains Nonbinding Recommendations
5
This guidance recommends the information to provide in a premarket submission that includes a 
device software function(s). For the purposes of this guidance, the term premarket submission 
includes, but is not limited to, premarket notification (510(k)) submission, De Novo 
classification request, Premarket Approval (PMA) application, Investigational Device Exemption 
(IDE), Humanitarian Device Exemption (HDE), or Biologics License Application (BLA). 
Certain devices are subject to premarket review through a BLA under section 351 of the Public 
Health Service Act.
This guidance does not apply to automated manufacturing and Quality System software17 or 
software that is not a device. For further information or to clarify the documentation 
expectations, please contact the responsible FDA review division.
Generally, the recommendations in this guidance apply to the device constituent part of a 
combination product18 (such as drug-device and biologic-device combination products) when the 
device constituent part19 includes a device software function, including combination products 
assigned to CDER and CBER regulated under drug or biological product market submission 
types. For more information, contact the FDA review Division that will have the lead review for 
the combination product.20
Other FDA guidance documents may recommend additional software-related documentation for 
inclusion in a premarket submission. For example, recommendations regarding cybersecurity 
information to include in a device premarket submission can be found in the guidances “Content 
of Premarket Submissions for Management of Cybersecurity in Medical Devices” and 
“Cybersecurity for Networked Medical Devices Containing Off-The-Shelf (OTS) Software.”21
Section II (Background) references other relevant guidance documents that supplement the 
recommendations contained in this guidance. 
17 As part of Quality System Regulation production and process controls, 21 CFR 820.70(i) states, “When computers 
or automated data processing systems are used as part of production or the quality system, the manufacturer shall 
validate computer software for its intended use according to an established protocol. All software changes shall be 
validated before approval and issuance. These validation activities and results shall be documented.”
18 21 CFR 3.2(e). 
19 21 CFR 4.2.
20 Sponsors may request in writing the participation of representatives of the Office of Combination Products (OCP) 
in meetings regarding their combination products, or to have OCP otherwise engage on regulatory matters 
concerning the product (section 503(g)(1)(A) of the FD&C Act). In addition, if you are uncertain whether your 
product is a combination product or a constituent part of a combination product, or which center has primary 
jurisdiction, you may request engagement by the Office of Combination Products. For more information on 
requesting engagement on regulation of combination products, please see FDA’s guidance “Requesting FDA 
Feedback on Combination Products,” available at https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/requesting-fda-feedback-combination-products.
21 For example, as part of the software validation and risk analysis required by 21 CFR 820.30(g), software device 
manufacturers may need to establish a cybersecurity risk management process that encompasses the total product 
lifecycle in order to address cybersecurity risks and emerging vulnerabilities.

---

<!-- Page 10 -->
Contains Nonbinding Recommendations
6
Device software functions subject to specific special controls22 may require additional software-
related documentation in a premarket submission. As applicable, please refer to the relevant 
special controls for the device. 
This guidance does not apply to the software-related documentation that may be needed to 
evaluate postmarket software device issues, including corrections and removals.23
While this guidance identifies the documentation sponsors should include in premarket 
submissions, this guidance is not meant to provide recommendations regarding how device 
software should be developed, verified, and validated. This guidance does not recommend the 
use of any specific software life cycle model or development methodology (such as waterfall 
model or other variations thereof, spiral model, Agile model, etc.). Sponsors should establish a 
software life cycle model that is appropriate for their product and organization, and meets the 
applicable regulatory requirements. The software life cycle model that is selected should cover 
the software throughout its total product life cycle. Regardless of the software lifecycle model 
being utilized, sponsors should ensure that the establishment of their design history file (DHF)24
documentation is synchronized with their software development, verification, and validation 
efforts. DHF documentation that is created retrospectively or following a prolonged period of 
time after actual software development, verification, and validation efforts could raise concerns 
regarding whether a developer has adequate control of their design process. For 
recommendations on device software development, verification, and validation, please consult 
software-related FDA-recognized voluntary consensus standards and other software-related FDA 
guidance documents referenced in this guidance (e.g., “General Principles of Software 
Validation”25).
IV. Definitions  
 
The following terms are used for the purposes of this guidance: 
Device Software Function - Software function that meets the device definition in section 201(h) 
of the FD&C Act. As discussed above, the term “function” is a distinct purpose of the product, 
which could be the intended use or a subset of the intended use of the product.
22 For more information regarding special controls, please see FDA’s Regulatory Controls webpage, available at 
https://www.fda.gov/medical-devices/overview-device-regulation/regulatory-controls.
23 See 21 CFR Part 806.
24 Each manufacturer shall establish and maintain a DHF for each type of device. 21 CFR 820.30(j). A DHF is a 
compilation of records which describes the design history of a finished device. The DHF shall contain or reference 
the records necessary to demonstrate that the design was developed in accordance with the approved design plan and 
the requirements of 21 CFR 820. See 21 CFR 820.30(j).
25 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-principles-
software-validation.

---

<!-- Page 11 -->
Contains Nonbinding Recommendations
7
Off-the-Shelf (OTS) Software26 - A generally available software component used by a device 
manufacturer for which the manufacturer cannot claim complete software life cycle control (e.g., 
operating system, printer/display libraries).
Serious Injury27 - An injury or illness that: 
1)
Is life threatening,
2)
Results in permanent impairment of a body function or permanent damage to a 
body structure, or 
3)
Necessitates medical or surgical intervention to preclude permanent impairment 
of a body function or permanent damage to a body structure. Permanent is defined 
as irreversible impairment or damage to a body structure or function, excluding 
trivial impairment or damage.
Software Verification and Software Validation - This guidance uses the terms “software 
verification” and “software validation,” which are described in further detail below.
·
For the purposes of this guidance, software verification is confirmation by objective 
evidence that the output of a particular phase of development meets all the input 
requirements for that phase. Software verification involves evaluating the consistency, 
completeness, and correctness of the software and its supporting documentation, as it is 
being developed, and provides support for a subsequent conclusion that software is 
validated. Software testing is one of several verification activities intended to confirm 
that the software development output meets its input requirements. Other verification 
activities include source code evaluations (e.g., code inspections and walkthroughs), 
document inspections, design reviews, technical evaluations (e.g., software architecture, 
software detailed design, etc.) and traceability analyses (e.g., software requirements 
specification to software design specification (and vice versa), source code to software 
design specification (and vice versa), and test cases to source code and to software design 
specification). For example, the input and output of the design phase are known as 
Software Requirements Specification (SRS) and Software Design Specification (SDS), 
respectively. In this case, software verification would involve confirming by objective 
evidence (e.g., reviews, traceability analysis) that the software design as documented in 
the SDS (i.e., output) correctly and completely implements all the requirements of the 
SRS (i.e., input).
·
For the purposes of this guidance, software validation refers to establishing, by objective 
evidence, that the software specifications conform to user needs and intended uses, and 
that the particular requirements implemented through software can be consistently 
fulfilled. Software validation is a part of design validation of the finished device. It 
involves checking for proper operation of the software in its actual or simulated use 
environment, including integration into the final device where appropriate. Software 
validation is highly dependent upon comprehensive software testing and other 
26 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/shelf-software-use-
medical-devices.
27 Serious injury as defined in 21 CFR 803.3(w).

---

<!-- Page 12 -->
Contains Nonbinding Recommendations
8
verification tasks previously completed at each stage of the software development life 
cycle. Planning, requirements, traceability, testing, risk assessment, design reviews, 
change management, and many other aspects of good software engineering are important 
activities that together help to support a conclusion that software is validated. 
The above descriptions of software verification and software validation are consistent with 
FDA’s thinking as described in the guidance “General Principles of Software Validation.”
V.
Documentation Level 
 
The recommended documentation for a premarket submission depends on the device’s risk to a 
patient, a user of a device, or others in the environment of use. FDA intends to take a risk-based 
approach to help determine the device’s Documentation Level, which is either Basic or 
Enhanced. The purpose of the Documentation Level is to help identify the minimum amount of 
information that would support a premarket submission that includes device software functions.  
 
The Documentation Level of a device is based on the risks of its device software function(s) in 
the context of the device’s intended use,28 such that the documentation level reflects the device 
as a whole.
For the purpose of this guidance: 
Enhanced Documentation should be provided for any premarket submission that 
includes device software function(s) where a failure or flaw of any device software 
function(s) could present a hazardous situation with a probable29 risk of death or serious 
injury,30 either to a patient, user of the device, or others in the environment of use. These 
risks should be assessed prior to implementation of risk control measures. Sponsors 
should consider the risks in the context of the device’s intended use (e.g., impacts to 
safety, treatment, and/or diagnosis), and other relevant considerations.
Basic Documentation should be provided for any premarket submission that includes 
device software function(s) where Enhanced Documentation does not apply. 
When determining the Documentation Level, sponsors should consider all known or foreseeable 
software hazards and hazardous situations associated with the device, including those resulting 
from reasonably foreseeable misuse, whether intentional or unintentional, prior to the 
implementation of risk control measures. This also includes the likelihood that device 
functionality is intentionally or unintentionally compromised by inadequate device cybersecurity.
28 See 21 CFR 801.4 (“…[I]ntended uses…refer to the objective intent of the persons legally responsible for the 
labeling of an article. The intent may be shown by such persons’ expressions, the design or composition of the 
article, or by the circumstances surrounding the distribution of the article.”).
29 The term “probable” is intended to exclude the consideration of purely hypothetical risks.
30 See 21 CFR 803.3(w).

---

<!-- Page 13 -->
Contains Nonbinding Recommendations
9
It is the sponsor’s responsibility to proactively and comprehensively consider risks as part of the 
device’s risk assessment.31
While devices within the scope of this guidance should be individually assessed to determine the 
appropriate Documentation levels, there are certain categories of devices for which we 
recommend that Enhanced Documentation be provided in a premarket submission. Specifically, 
we recommend that Enhanced Documentation should be provided in a premarket submission for 
devices intended to test blood donations for transfusion-transmitted infections, devices used to 
determine blood donor and recipient compatibility, automated blood cell separator devices 
intended for collection of blood and blood components for transfusion or further manufacturing 
use, and blood establishment computer software (BECS).32
There are other categories of device for which we generally recommend Enhanced 
Documentation be provided in a premarket submission. FDA believes that given the nature of 
these products and their intended uses, these products may have unique risks that require further 
documentation to ensure that FDA is able to evaluate the safety and effectiveness of the device. 
These include devices that are a constituent part of a combination product (i.e., drug/device, 
biologic/device, or drug/device/biologic)33 and Class III devices. In the course of evaluating the 
appropriate Documentation Level for a device that is a constituent part of a combination product 
or a Class III device, a sponsor may determine that an Enhanced Documentation level does not 
apply. In such cases, the sponsor should provide an appropriately detailed rationale as to why 
Basic Documentation instead of Enhanced Documentation is appropriate for the premarket 
submission. As previously discussed, during the course of submission review, FDA may request 
additional information if needed to evaluate the safety and effectiveness of the device.
Sponsors may submit a Pre-Submission to obtain FDA feedback about a device’s Documentation 
Level and recommended documentation prior to a premarket submission, as described in the 
guidance “Requests for Feedback and Meetings for Medical Device Submissions: The Q-
Submission Program.”34 For additional information on how to engage with a particular Center 
with regard to a combination product, including best practices for doing so, please see the final 
guidance “Requesting FDA Feedback on Combination Products.”35
For additional information and examples of devices that demonstrate the implementation of the 
Documentation Level risk-based approach, please refer to Appendix A of this guidance. 
VI. Recommended Documentation 
This section reflects FDA’s recommendations for information to be included in premarket 
submissions for Basic and Enhanced Documentation Levels. This recommended information 
31 For information on risk assessment refer to Section VI.C of this guidance.
32 See Appendix A for rationale on enhanced documentation level for BECS.
33 21 CFR 3.2(e). 
34 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program.
35 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requesting-fda-
feedback-combination-products.

---

<!-- Page 14 -->
Contains Nonbinding Recommendations
10
should demonstrate that planning, requirements, risk assessment, design reviews, traceability, 
change management, testing plans and results, and other aspects of good software engineering 
for device software functions were employed, to support a conclusion that the device software 
function was appropriately designed, verified, and validated. 
If the device is a multiple function device product and includes software function(s) that are 
considered “other functions,” as that term is used in the guidance “Multiple Function Device 
Product: Policy and Considerations,” the recommendations described in the aforementioned 
guidance should be considered when preparing the software documentation for a premarket 
submission.
Table 1 below provides an outline of the recommended documentation for each software 
documentation element and corresponding Documentation Level. Please refer to subsections A-J 
in this section of the guidance (VI) for more detail.
Table 1. Outline of Recommended Documentation
Software 
Documentation 
Elements
Basic Documentation Level
Enhanced Documentation Level
Documentation 
Level Evaluation
(Section VI.A)
A statement indicating the Documentation Level and a description of the 
rationale for that level.
Software 
Description
(Section VI.B)
Software description, including overview of significant software features, 
functions, analyses, inputs, outputs, and hardware platforms. 
Risk 
Management File
(Section VI.C)
Risk management plan, risk assessment demonstrating that risks have been 
appropriately mitigated, and risk management report.
Software 
Requirements 
Specification 
(SRS)
(Section VI.D)
SRS documentation, describing the needs or expectations for a system or 
software, presented in an organized format, at the software system level or 
subsystem level, as appropriate, and with sufficient information to 
understand the traceability of the information with respect to the other 
software documentation elements (e.g., risk management file, software 
design specification, system and software architecture design chart, 
software testing).

---

<!-- Page 15 -->
Contains Nonbinding Recommendations
11
Software 
Documentation 
Elements
Basic Documentation Level
Enhanced Documentation Level
System and 
Software 
Architecture 
Design 
(Section VI.E)
Detailed diagrams of the modules, layers, and interfaces that comprise the 
device, their relationships, the data inputs/outputs and flow of data, and 
how users or external products (including information technology (IT) 
infrastructure and peripherals) interact with the system and software. 
Software Design 
Specification 
(SDS)
(Section VI.F)
FDA is not recommending the 
SDS as part of the premarket 
submission. Sponsor should 
document this information on 
the design via the DHF for the 
device. During premarket 
review, FDA may request 
additional information, if 
needed, to evaluate the safety 
and effectiveness of the device.
SDS documentation, including sufficient 
information that would allow FDA to 
understand the technical design details 
of how the software functions, how the 
software design completely and 
correctly implements all the 
requirements of the SRS, and how the 
software design traces to the SRS in 
terms of intended use, functionality, 
safety, and effectiveness.
Software 
Development, 
Configuration 
Management, 
and Maintenance 
Practices
(Section VI.G)
A summary of the life cycle 
development plan and a 
summary of configuration 
management and maintenance 
activities; 
OR
A Declaration of Conformity36
to the FDA-recognized version 
of IEC 62304, including 
subclauses 5.1.1-5.1.3, 5.1.6-
5.1.9, clause 6 (Software 
maintenance process), and 
clause 8 (Software configuration 
management process), among 
others as applicable.
Basic Documentation Level, PLUS 
complete configuration management and 
maintenance plan document(s);
OR
A Declaration of Conformity37 to the 
FDA-recognized version of IEC 62304, 
including subclause 5.1 (Software 
development planning), clause 6 
(software maintenance process), and 
clause 8 (software configuration 
management process), among others as 
applicable. 
36 For more information, please see Appropriate Use of Voluntary Consensus Standards in Premarket Submissions 
for Medical Devices, available at https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/appropriate-use-voluntary-consensus-standards-premarket-submissions-medical-devices.
37 For more information, please see Appropriate Use of Voluntary Consensus Standards in Premarket Submissions 
for Medical Devices, available at https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/appropriate-use-voluntary-consensus-standards-premarket-submissions-medical-devices.

---

<!-- Page 16 -->
Contains Nonbinding Recommendations
12
Software 
Documentation 
Elements
Basic Documentation Level
Enhanced Documentation Level
Software Testing 
as Part of 
Verification and 
Validation
(Section VI.H)
A summary description of the 
testing activities at the unit, 
integration and system levels;
AND
System level test protocol 
including expected results, 
observed results, pass/fail 
determination, and system level 
test report.
Basic Documentation Level, PLUS 
unit and integration level test protocols 
including expected results, observed 
results, pass/fail determination, and unit 
and integration level test reports.
Software Version 
History
(Section VI.I)
A history of tested software versions including the date, version number, 
and a brief description of all changes relative to the previously tested 
software version.
Unresolved 
Software 
Anomalies 
(Section VI.J)
List of remaining unresolved software anomalies with an evaluation of the 
impact of each unresolved software anomaly on the device’s safety and 
effectiveness.
Documentation Level Evaluation 
 
A statement indicating the Documentation Level for the device and a description of the rationale 
for such Documentation Level. The rationale should account for the device’s intended use, and 
include references, where appropriate, from the submission documentation (such as Risk 
Management File, Software Description, etc.) to support the indicated Documentation Level.     
 
 
Software Description 
 
An overview of significant software features and functions, including images, flow charts, and 
state diagrams as needed to adequately explain the software functionality38 should be provided. If 
the premarket submission is for a modified device, provide the document number of the previous 
submission and highlight pertinent software changes (e.g., changes that affect safety and 
effectiveness) since the last FDA approval or clearance.  
38 FDA may request additional architecture diagrams to address the cybersecurity risks associated with a device. For 
more information, please refer to the guidance document, “Content of Premarket Submissions for Management of 
Cybersecurity in Medical Devices.”

---

<!-- Page 17 -->
Contains Nonbinding Recommendations
13
Consider and, as applicable, provide information to address the questions below when preparing 
the software description. However, FDA recognizes that these questions and examples may not 
capture all the unique aspects of device software and encourages the inclusion of additional 
information that will further FDA’s understanding of the device’s functionality to facilitate the 
review of a submission.
If the device is a multiple function device product and includes software function(s) that are 
considered “other functions,” as that term is used in the guidance “Multiple Function Device 
Products: Policy and Considerations,” the recommendations described in the aforementioned 
guidance should be considered when preparing the software description information.
·
Software Operation 
o
What is the role of the software as it relates to the intended use of the device? 
Examples: software-only device, software that controls the device hardware, 
software application that accompanies the device for data processing.
o
Who is the intended user of the software? Examples: the patient, a caregiver, a 
healthcare professional, or a combination thereof
o
What is the intended patient population? 
§
Does the software function focus on a specific disease, condition, patient 
characteristic or demographic?
§
Does the software provide information that is directly applicable to a 
specific disease or condition?
o
If the software performs analysis of signals/patterns or images, what is the 
analysis methodology? Examples: rule-based calculations, online test 
administration, artificial intelligence and machine learning (AI/ML), neural 
networks, fixed (locked) or adaptive (iterative, continuously learning) algorithms. 
o
If the device software function uses ML models trained through ML methods (i.e., 
is AI/ML-enabled, such as AI, ML, adaptive models, natural language processing 
(NLP), neural networks, and related approaches):
§
What methods, models, frameworks, and/or platforms were used?
§
What data (populations, samples) informed the model(s)? How, when, and 
where was the data collected?
§
What steps were taken to identify and address potential biases and 
limitations of the model(s)?
§
What materials, mechanisms, and/or approaches are used to provide 
transparency about the model’s development, performance, and 
limitation(s)?

---

<!-- Page 18 -->
Contains Nonbinding Recommendations
14
·
Software Specifics39
o
What hardware platforms are used?
o
What software platforms are used? 
§
If applicable, what hosting environments are used (e.g., hospital networks, 
cloud infrastructures) and for what functions (e.g., processing, storage)? 
o
Does the device use OTS software?40
o
What is the final release version (i.e., version intended to be released to end 
users)? If this version is different from the documentation’s version, explain the 
differences.
·
Software Inputs and Outputs 
o
What are the inputs and their format? Examples: signals, images (specify 
modality), measurements (specify units), reports, questionnaires, other device 
data/results.
o
Who or what provides the inputs? Examples: patients, caregivers, healthcare 
professionals, technicians, sensors/attachments, signal acquisition systems, in 
vitro diagnostic devices, other medical devices, other non-medical products or 
software.
o
What are the outputs and their format? Examples: diagnostic information, 
treatment information, control signals for device hardware, images (specify 
modality), measurements (specify units), alarms, alerts, or reports.
o
Who or what receives the outputs? Examples: patients, caregivers, healthcare 
professionals, technicians, health records, device hardware, other medical 
devices, interoperable systems.
o
Does the software impact or replace any action(s) otherwise performed manually 
by a health care professional, patient, caregiver, or other operator? What are the 
clinical workflow steps and assumptions (from beginning to end state)? 
Examples: automates steps, triages patients, provides a definite diagnosis or 
suggests likely diagnosis for further confirmation by physician, performs or 
recommends specific treatment, identifies a region of interest for further review.
39 One example approach for providing some of the identified software specifics is by providing a Software Bill of 
Materials (SBOM) that lists and provide details on software components including, but not limited to, commercial, 
open source, OTS, and manufacturer-developed software components. For some devices, information related to an 
SBOM may be required part of a premarket submission.
40 If a device uses OTS software, FDA may request additional information in premarket submissions. For more 
information, please refer to the guidance document “Guidance for Off-The-Shelf Software Use in Medical Devices.”

---

<!-- Page 19 -->
Contains Nonbinding Recommendations
15
o
Is the device designed to be interoperable?41 In other words, does the device 
transmit, exchange, and/or use information through an electronic interface (e.g., 
network, wireless) with another medical/non-medical product, system, or device? 
If yes, what other products does the device interface with, and what methods, 
standards, and specifications are used to interact and/or communicate with other 
medical/non-medical product, system, or device? Are the medical/non-medical 
products, systems, or devices networked?
If any of the information requested above is included in another document, such as the Software 
Requirements Specification (SRS), an annotation and a reference to the document in the 
submission where this information is located should be provided.
Risk Management File 
 
The risk management file should be provided as part of the premarket submission and include 
the following documentation. FDA recommends sponsors refer to an FDA-recognized version of 
ISO 14971 for additional information on the development and application of a risk management 
file. 
 
(1) Risk Management Plan 
 
FDA recommends sponsors submit a risk management plan to support the effectiveness of the 
risk management activities and processes for a particular medical device.42 In FDA’s review of 
the risk management plan, the Agency intends to primarily focus on:
·
Individual risk acceptability criteria including the need for risk reduction (control). 
·
Method to evaluate the acceptability of the overall residual risk for all residual risks after 
all risk control measures have been implemented and verified.
The risk acceptability criteria should be based on the sponsor’s process for determining 
acceptable risk. The acceptability criteria should be documented in the risk management plan 
before an initial risk evaluation is performed for the device software under review. 
It should be clear in the risk management plan how the sponsor plans to evaluate the overall 
residual risk against the benefits of the intended use of the device. 
41 More information on interoperable medical devices is available at: https://www.fda.gov/regulatory-
information/search-fda-guidance-documents/design-considerations-and-pre-market-submission-recommendations-
interoperable-medical-devices.
42 For combination products that include device software functions, a 14971-based risk management framework that 
incorporates relevant considerations from International Council for Harmonisation of Technical Requirements for 
Pharmaceuticals for Human Use (ICH) Q9 Quality Risk Management is recommended. For further information, see, 
for example, AAMI TIR 105 Risk Management Guidance for Combination Products.

---

<!-- Page 20 -->
Contains Nonbinding Recommendations
16
(2) Risk Assessment  
 
A risk assessment that includes a risk analysis, risk evaluation, risk control and a benefit-risk 
analysis (where applicable) should be provided for all device software. For software that is part 
of a system, a risk assessment should be performed on the system comprising the software and 
its whole hardware environment. If this information is covered in the system risk assessment 
documentation, this should be noted in the software documentation with reference to the 
particular section of the premarket submission. 
 
For multiple function device products, the risk assessment should include the results of a risk-
based analysis of any potential adverse impact or labeled positive impact of “other function(s),” 
as that term is used in the guidance “Multiple Function Device Product: Policy and 
Considerations,” to the safety or effectiveness of the device function(s)-under-review. 
A risk assessment should document the following items (e.g., in tabular format): 
·
Risk Analysis 
o
Identification of known or foreseeable hazards43 (and their causes) associated with 
the device based on the intended use; reasonably foreseeable misuse whether 
intentional or unintentional; and the impacts to safety, treatment, and/or diagnosis. 
For each identified hazard, the sponsor should consider the reasonably foreseeable 
sequences or combinations of events that can result in a hazardous situation,44 and 
should identify and document the resulting hazardous situation(s).
o
Estimation of the risk of each hazard and hazardous situation.45
o
Severity of the harm46 resulting from the hazardous situation.
·
Initial Risk Evaluation of the Hazardous Situation  
o
This includes assessment of acceptability (e.g., acceptable, not acceptable) and 
need for risk reduction (control) measures as defined in the risk management plan.  
 
·
Risk Control Measures  
o
This should include the following risk control measures listed in descending order 
from highest to lowest priority:
43 For the purposes of this guidance, hazard refers to a potential source of harm.
44 For the purposes of this guidance, hazardous situation refers to a circumstance in which people, property or the 
environment is/are exposed to one or more hazards.
45 It is often difficult to adequately estimate the probability of software failures that could contribute to a hazardous 
situation. Applying unrealistically low probability estimates to software failures could result in unrealistic risk 
evaluation and subsequently lead to inappropriate risk control measures. As a result, in some instances it may be 
prudent to focus on the identification of potential software functionality and failures that could result in hazardous 
situations instead of estimating probability. In such cases, considering a worse case probability is appropriate, the 
probability for the software failure occurring should be set to 1.  
46 For the purposes of this guidance, harm refers to injury or damage to the health of people, or damage to property 
or the environment.

---

<!-- Page 21 -->
Contains Nonbinding Recommendations
17
§
Design (e.g., eliminating or reducing unnecessary features, modifying the 
software architecture to prevent hazardous situations, modifying the user 
interface to prevent usability errors)
§
Protective measures (e.g., defensive programming checks that detect 
unexpected faults followed by automatic intervention to halt the delivery of 
results or therapy, alarms allowing user intervention to prevent a hazardous 
situation) 
§
Information for safety (e.g., written warnings, on-screen warnings, training) 
o
There should be verification of the implementation of the risk control measures 
and verification of the effectiveness of the implemented risk control measures 
(i.e., the implemented risk control measure reduces risk). This can be 
accomplished by tracing the identified hazard to the verified specific risk control 
measures (e.g., a requirement ID in the SRS and SDS, a test name and identifier 
in the testing documentation that shows pass/fail results, a user manual name and 
identifier, a training manual name and identifier). For example, given an 
identified hazard (e.g., HAZ-XXX47), the following could be listed for 
traceability: a design related risk control measure that is documented in a software 
requirement specification (e.g., SRS-XXX) and software design specification 
(e.g., SDS-XXX), and tested as part of a unit test case (e.g., UT-XXX), 
integration test case (e.g., INT-XXX) and system test case (e.g., SYS-XXX). FDA 
recognizes that there may be instances where a specific hazard traces to several 
requirements/specifications and tests, thereby making the presentation of 
information cumbersome in the risk assessment document. Therefore, sponsors 
may choose to present this traceability in a separate document linking together 
software requirements specifications, software design specifications, testing and 
identified hazards derived from the risk assessment.     
o
There should be an assessment of whether risk control measures introduce new 
hazards or hazardous situations or impact the initial risk evaluation. 
o
Document any risk control measures employed to mitigate increased risk or 
adverse effect on performance due to the combination of “other function(s),” as 
that term is used in the guidance “Multiple Function Device Products: Policy and 
Considerations,” with the device function-under-review. 
·
Residual Risk Evaluation of the Hazardous Situation after implemented Risk Control 
Measures.  
o
This includes assessment of acceptability (e.g., acceptable, not acceptable) as 
defined in the risk management plan.  
 
 
 
 
47 “XXX” denotes a unique number identifier for a specific hazard, software requirement specification, software 
design specification, unit test case, integration test case or system test case.

---

<!-- Page 22 -->
Contains Nonbinding Recommendations
18
·
Benefit-Risk  
o
If a residual risk is deemed not acceptable according to the acceptability criteria in 
the risk management plan and further risk control is not possible, the sponsor 
should provide documented benefit-risk analysis to demonstrate that the benefits 
of the intended use outweigh the residual risk, which may be referenced in other 
benefit-risk assessment documentation.  
 
(3)
Risk Management Report  
 
A risk management report should be provided to: 
 
·
Show how the risk management plan has been appropriately implemented.  
 
·
Demonstrate that the risk management file has been assessed by the appropriate 
personnel and the overall residual risk is acceptable.  
 
·
Demonstrate appropriate methods are established for the collection and assessment of 
relevant production and post-production information.
Software Requirements Specification (SRS) 
 
The SRS documents the requirements48 for the software which typically specifies inputs and 
outputs, functions that the software will perform, hardware,49 performance,50 interfaces,51 user 
interaction, error definition and handling, intended operating environment, safety related 
requirements derived from a risk assessment (Refer to Section VI.C Risk Management File) and 
all ranges, limits, defaults, and specific values that the software will accept. For additional details 
on what should be included in the software requirements specification, refer to the guidance, 
“General Principles of Software Validation.”
48 The term “requirements” is used in this section as part of the term “Software Requirements Specification,” and 
does not refer to a regulatory requirement.
49 Hardware requirements generally include, but are not limited to, requirements related to: microprocessors, 
memory devices, sensors, energy sources, safety features, and communications.
50 Software performance and functional requirements generally include, but are not limited to, requirements related 
to algorithms or control characteristics for therapy, diagnosis, monitoring, alarms, analysis, and interpretation with 
full text references or supporting clinical data, if necessary. Software performance and functional requirements may 
also include: device limitations due to software, internal software tests and checks, error and interrupt handling, fault 
detection, tolerance, and recovery characteristics, safety requirements, and timing and memory requirements. 
51 Interface requirements (e.g., external, user, internal) generally include, but are not limited to, both communication 
between system components and communication with the user such as: printers, monitors, keyboard, mouse, cloud 
servers, peripheral medical devices, mobile technology platforms.

---

<!-- Page 23 -->
Contains Nonbinding Recommendations
19
The QSR requires “a mechanism for addressing incomplete, ambiguous, or conflicting 
requirements.”52 Each requirement identified in the software requirements specification should 
be traceable and we recommend that the SRS be evaluated for accuracy, completeness, 
consistency, testability, correctness, and clarity.
A singular SRS document or set of multiple SRS documents should be provided. The 
documentation should include a description of the software requirement identification and 
tracking methodology used to support the traceability of the requirements. For example, in a 
device that includes multiple functions, components, and/or accessories, where each has its own 
individual SRS document and associated software device functions, the set of individual SRS 
documents would comprise the complete SRS.
FDA acknowledges that modern development practices may employ incremental or evolutionary 
software development practices. Additional forms of software requirements might be included in 
the submission, such as well elaborated stories, use cases, textual descriptions, screen mockups, 
and data flows. 
In order to facilitate a timely premarket review, the following recommendations should be 
considered in preparing SRS documentation:
·
Format the SRS to be well-organized, easily navigable and readable with the labeling 
and/or grouping of requirements (such as by modules or units of a function). 
 
·
Note any relevant traceability between requirements listed in the SRS and information 
related to those requirements in other software documentation (such as the SDS, System 
and Software Architecture Diagram, etc.). 
·
If the premarket submission involves a modification to an existing approved or cleared 
device, highlight all pertinent differences in software requirements.
·
Identify the requirements the sponsor believes are most critical (i.e., could have the most 
significant impact) to the device’s safety and effectiveness. These requirements could be 
highlighted within the SRS document and/or consolidated in a supplemental document 
that includes these requirements of interest in a summarized format. This technique may 
help facilitate the presentation of those requirements that most critically affect clinical 
functionality or performance specifications that are directly associated with the intended 
use of the device, or would otherwise impact the device’s safety and effectiveness. 
52 See 21 CFR 820.30(c) (“Design input. Each manufacturer shall establish and maintain procedures to ensure that 
the design requirements relating to a device are appropriate and address the intended use of the device, including the 
needs of the user and patient. The procedures shall include a mechanism for addressing incomplete, ambiguous, or 
conflicting requirements. The design input requirements shall be documented and shall be reviewed and approved 
by a designated individual(s). The approval, including the date and signature of the individual(s) approving the 
requirements, shall be documented.”).

---

<!-- Page 24 -->
Contains Nonbinding Recommendations
20
·
If any of the information requested above is included in another document, an annotation 
and a reference to the document in the submission where this information is located 
should be provided.
Documentation of requirements included in the premarket submission for the device function-
under-review should include adequate detail to describe any expected relationship, utility, 
reliance, or interoperability with any “other function,” as that term is used in the guidance 
“Multiple Function Device Products: Policy and Considerations.”
System and Software Architecture Diagram 
 
The purpose of the system and software architecture diagram is to present a roadmap of the 
device design to facilitate a clear understanding of:
·
The modules and layers that make up the system and software;
·
The relationships among the modules and layers;
·
The data inputs/outputs and flow of data among the modules and layers; and
·
How users or external products, including IT infrastructure and peripherals (e.g., 
wirelessly connected medical devices) interact with the system and software. 
For purposes of the system and software architecture diagram, this guidance considers a module 
to be a discrete unit or architectural item within the system or software. A module could 
represent, for example, a finished hardware device within a system of hardware and software 
products, a hardware component within a finished hardware device, a finished software product 
within a system of software products, or a software function within a finished software product. 
A module is not specifically meant to describe code-level software functions, although such 
code-level software functions could be considered modules if appropriate. The sponsor should 
determine what constitutes a module in the context of its system and software.
Sponsors should provide the appropriate level of detail in the system and software architecture 
diagram to convey the information in a manner that can facilitate an efficient premarket review, 
including descriptive text (in the diagram or in an accompanying document) to explain the 
architecture diagram where appropriate. A system and software architecture diagram that is not 
appropriately tailored (e.g., too high-level, too detailed, or overly confusing) or that is illegible 
(e.g., cropped diagrams, inadequate font size, unreadable without high magnification) could lead 
to requests for additional information from the FDA review division. To the extent appropriate, 
the system and software architecture diagram can be communicated in one or more diagrams and 
in one or more formats, and may convey different dimensions of the system and software. The 
system and software architecture diagram may comprise multiple static diagrams (e.g., those 
illustrated in Appendix B), dynamic diagrams (e.g., state diagrams), cybersecurity architecture 
diagrams, and others as needed for adequate detail. If more than one diagram is used, the sponsor

---

<!-- Page 25 -->
Contains Nonbinding Recommendations
21
should provide a high-level diagram that communicates the overview and points to the other 
diagrams that provide additional detail. The relationship between diagrams should also be clearly 
communicated. In general, the sponsor should take note of the following visual, language, and 
reference considerations when developing an effective system and software architecture diagram:
·
Visual Considerations 
o
The diagram and the means for communicating information in the diagram should 
be visually consistent (e.g., a solid arrow should convey a specific meaning as 
compared to a dashed arrow; icons should be used consistently; lines that intersect 
should clearly communicate whether the intersection is a crossing or connection) 
and the meaning ascribed should be clearly communicated (e.g., through the use 
of standard symbols and notation). 
o
The level of detail provided in the diagram should be consistent throughout unless 
areas of less detail are clearly explained (e.g., in the case of functions, within the 
system or software, that are not under review).
o
Modules should be grouped in a logical and obvious manner.
o
Use of color or other visual means (e.g., dashed boxes within solid boxes) should 
be used to convey layering within the system, software, or module.
o
Visual clutter should be avoided, and the diagram should be scaled according to 
the complexity and amount of information presented.
·
Language Considerations 
o
Annotations should be used to provide additional information about a particular 
module or data element (e.g., a plain language explanation of the module purpose 
or a pointer to a document or requirement within the premarket submission).
o
Use of terminology and naming conventions should be consistent within the 
diagram and the remainder of the premarket submission materials.
o
Use of acronyms, jargon, or terms that are not defined in the diagram itself should 
be avoided.
·
Reference Considerations 
o
The diagram should reference other documents in the submission (e.g., Software 
Description, Software Requirements Specification), as appropriate.
o
For submissions related to modification(s) to a previously cleared or approved 
device, the diagram should identify and reference the modules that are affected by 
the modification(s).
The above considerations are intended to serve as a guide and may not apply in every case or 
may apply differently for different diagrams. When developing the system and software

---

<!-- Page 26 -->
Contains Nonbinding Recommendations
22
architecture diagram, sponsors are encouraged to leverage industry best practices within and 
outside the medical device industry. OTS modeling languages or platforms may be used to 
develop the system and software architecture diagram. Any modeling language- or platform-
specific terminology should be defined or supported by reference to a publicly-available 
consensus standard or specification. The resulting architecture diagram should be provided in a 
form that aligns with eCopy guidelines recommended in the guidance “eCopy Program for 
Medical Device Submissions.”53
For multiple function device products, the system and software architecture diagram should 
clearly delineate between the device functions-under-review and the “other functions,” as that 
term is used in the guidance “Multiple Function Device Products: Policy and Considerations.” 
The system and software architecture diagram should include adequate detail to understand how 
or if the “other function(s)” interact with or impact the device function-under-review. 
Example system and software architecture diagrams are provided in Appendix B of this 
guidance, illustrating approaches to effectively convey the recommended information to 
facilitate an efficient premarket review. These simplified examples demonstrate how the 
considerations described in this section can be implemented into a system and software 
architecture diagram. The modules in the example are intended for illustration purposes only and 
are not intended to document or represent a comprehensive or complete system and software 
architecture diagram for a specific medical device or system. The illustrated approach does not 
prescribe any specific modeling languages or platforms to allow for flexibility in development 
and documentation. The approaches illustrated can be applied to any system and software 
architecture diagram.
Software Design Specification (SDS) 
 
The Software Design Specification (SDS) may contain both a high level summary of the design 
and detailed design information. In terms of the relationship between the Software Requirement 
Specification (SRS) and the SDS, the SRS describes what the software function will do and the 
SDS describes how the requirements in the SRS are implemented. The information presented in 
the SDS should be sufficient to ensure that the work performed by the software engineers who 
created the device software function was clear and unambiguous, with minimal ad hoc design 
decisions. The use of minimal ad hoc design decisions reflects the general principle that the 
creation of SDS should occur as a prospective activity rather than documented retrospectively 
after the software design has been implemented by ad hoc design methods. Documentation of 
specifications included in the premarket submission for the device function-under-review should 
include adequate detail to describe any expected relationship, utility, reliance, or interoperability 
with any “other function,” as that term is used in the guidance “Multiple Function Device 
Products: Policy and Considerations.”
53 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/ecopy-program-
medical-device-submissions.

---

<!-- Page 27 -->
Contains Nonbinding Recommendations
23
(1) Basic Documentation Level 
 
FDA is not recommending the SDS as part of the premarket submission. Sponsors should 
document this information on the design internally via the DHF for the device. During premarket 
review, FDA may request additional information on the design, if needed, to evaluate the safety 
and effectiveness of the device.
(2) Enhanced Documentation Level 
 
A singular SDS document or set of SDS documents that provide the technical design details of 
how the software functions, how the software design completely and correctly implements all the 
requirements of the SRS and how the software design traces to the SRS in terms of intended use, 
functionality, safety, and effectiveness. The software functional units or modules along with the 
interfaces among them identified in the architectural (i.e., high-level) design should be 
documented with the corresponding detailed (i.e., low-level) design information in the SDS. The 
information provided for review should be sufficient to ensure that the work performed in 
developing the software functional units or modules and their interfaces was clear and 
unambiguous, with minimal ad hoc design decisions. For example, the creation of the SDS is 
expected to have occurred as a prospective activity where the SDS was used to guide the design, 
development and testing of the software rather than documented retrospectively after the 
software design has been implemented by ad hoc design methods. 
For additional details on what should be included in the software design specification, refer to 
the guidance, “General Principles of Software Validation.”
Software Development, Configuration Management, and 
Maintenance Practices 
 
One way a sponsor could address this documentation element of a premarket submission is to 
provide the recommended information on related software development, configuration 
management, and maintenance practices and procedures. In another approach, a sponsor could 
provide a Declaration of Conformity to specific clauses of the FDA-recognized version of 
ANSI/AAMI/IEC 62304 Medical Device Software - Software Life Cycle Processes or the FDA-
recognized version of IEC 62304 Medical device software - Software life cycle processes 
(hereafter referred to collectively as ANSI/AAMI/IEC 62304). A sponsor could also provide a 
Declaration of Conformity to the complete ANSI/AAMI/IEC 62304 standard. However, a 
Declaration of Conformity to the complete ANSI/AAMI/IEC 62304 standard is not needed due 
to known differences in categorization of device software functions and other recommended 
documentation.

---

<!-- Page 28 -->
Contains Nonbinding Recommendations
24
(1) Basic Documentation Level 
 
A summary of the processes and procedures that are in place to manage the software life cycle 
development, software configuration and change management, and software maintenance 
activities should be provided. This summary information should include an adequate description 
of: 
 
·
Processes and procedures used in software development, verification, and validation. 
 
·
Software coding standards, methods, and tools used in software development.
·
Main deliverables of the typical activities and tasks involved in software development, 
verification, and validation.
·
Processes, procedures, and tools used to link user needs, system requirements, software 
requirements, software design specifications, software testing and implemented risk 
control measures (i.e., traceability).
·
Processes and procedures used in software configuration and change management.
·
Processes and procedures used in software maintenance that includes risk assessment of 
software changes, initial testing that evaluates the correctness of the implemented 
software change(s), and regression analysis and testing.
Alternatively, to address the recommendations for this documentation element, a sponsor may 
provide a Declaration of Conformity to the FDA-recognized version of ANSI/AAMI/IEC 62304 
Medical Device Software - Software Life Cycle Processes, including subclauses 5.1.1 (“Software 
development plan”), 5.1.2 (“Keep software development plan updated”), 5.1.3 (“Software 
development plan reference to system design and development”), 5.1.6 (“Software verification 
planning”), 5.1.7 (“Software risk management planning”), 5.1.8 (“Documentation planning”), 
5.1.9 (“Software configuration management planning”), clause 6 (“Software maintenance 
process”), and clause 8 (“Software configuration management process”),54 among others as 
applicable.
(2) Enhanced Documentation Level
Documents implementing the configuration management and maintenance plans should be 
provided in addition to the summary documentation requested for the Basic Documentation 
Level, as described above.
Alternatively, to address the recommendations for this documentation element, a sponsor may 
provide a Declaration of Conformity to the FDA-recognized version of ANSI/AAMI/IEC 62304 
54 References to clauses and subclauses based on ANSI/AAMI/IEC 62304:2006 & A1:2016.

---

<!-- Page 29 -->
Contains Nonbinding Recommendations
25
Medical Device Software – Software Life Cycle Processes, including subclause 5.1 (Software 
development planning), clause 6 (“Software maintenance process”), and clause 8 (“Software 
configuration management process”),55 among others as applicable.
Software Testing as part of Verification and Validation 
 
Refer to Section IV (Definitions) for important information pertaining to FDA’s thinking on 
verification and validation, as it relates to this guidance. Additionally, please refer to guidance 
“General Principles of Software Validation” for additional details regarding FDA’s thinking 
regarding software testing, particularly unit level (module or component) testing, integration 
level (internal and external interfaces) testing, and system level (functional) testing.
The recommendations in this guidance do not address other forms of testing, such as non-clinical 
bench, animal, or clinical testing. For more information regarding other forms of device 
performance testing, sponsors should refer to relevant special controls,56 FDA-recognized 
voluntary consensus standards,57 and device-specific guidances. If the premarket submission 
leverages information from other device performance testing section(s) to address software 
verification and validation, the sponsor is encouraged to appropriately reference the other 
performance testing material to facilitate the navigation between submission sections, reduce 
instances of duplication, and improve readability.
(1) Basic Documentation Level 
 
The following software testing documentation should be provided:
·
A summary description of the testing activities at the unit, integration, and system levels. 
The summary description should include the software version tested and the overall 
pass/fail test results for all test protocols (i.e., collection of test procedures for specific 
software functionality) executed. If the device is a modified version of a previously 
cleared or approved device, provide a summary of the modifications compared with the 
previous cleared or approved version along with a summary description of the additional 
testing activities performed at the unit, integration, and system levels as compared with 
the previously cleared or approved version.  
 
·
Any intentional changes made in response to failed tests and documentation of test results 
demonstrating that the intentional changes were implemented correctly.  
 
·
A regression analysis and regression testing with pass/fail test results (where applicable) 
to account for unintended effects of a software change.
55 References to clauses and subclauses based on ANSI/AAMI/IEC 62304:2006 & A1:2016.
56 For more information regarding special controls, please see FDA’s Regulatory Controls webpage, available at 
https://www.fda.gov/medical-devices/overview-device-regulation/regulatory-controls.
57 The most up-to-date list of voluntary FDA- recognized consensus standards is available at 
https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm.

---

<!-- Page 30 -->
Contains Nonbinding Recommendations
26
o
Regression analysis is a documented evaluation of the impact of a software 
change based on review of the relevant documentation (e.g., software 
requirements specification, software design specification, source code, test plans, 
test cases, test scripts, etc.) to determine whether regression testing is needed. If 
regression testing is needed as determined by the regression analysis, the sponsor 
should identify the necessary regression tests to be run. Regression testing is the 
rerunning of test cases that a program has previously executed correctly and 
comparing the current result to the previous result in order to detect unintended 
effects of a software change.
·
System level test protocol including expected results derived from software requirements, 
actual results that are observed and recorded, objective pass/fail determination (i.e., 
actual results are acceptably equivalent to expected results) and a system level test report. 
The system level test report should demonstrate that the protocol has been acceptably 
executed with passing test results and any unresolved anomalies have been acceptably 
deferred based on a risk assessment for the candidate release version.
(2) Enhanced Documentation Level 
 
In addition to the documentation requested for the Basic Documentation Level, all unit and 
integration level test protocols and reports should be provided, including expected results derived 
from software requirements and design, actual results that are observed and recorded, and 
objective pass/fail determination (i.e., actual results are acceptably equivalent to expected 
results). The unit and integration level test reports should demonstrate that the protocols have 
been acceptably executed with passing testing results and any unresolved anomalies have been 
acceptably deferred based on a risk assessment for the candidate release version.
Software Version History 
 
The documentation should include the history of software versions that were tested and 
documented at the unit, integration, and system levels as part of verification and validation 
activities, beginning with the version that became subject to the design controls, as described in 
21 CFR 820.30. This typically takes the form of a line-item tabulation including the date, version 
number that was tested (including, if applicable, bench, animal, and clinical testing) and a brief 
description of all changes in the version relative to the previously tested version.  
 
The last entry in a line-item tabulation should be the final version to be incorporated in the 
released device. This entry should also include any differences between the tested version of 
software and the released version, along with an assessment of the potential effect of the 
differences on the safety and effectiveness of the device.
If the software version history includes a version(s) that corresponds to a previously released 
cleared or approved version of the software, the sponsor should highlight in the version history 
document each prior released cleared or approved version and the premarket submission 
number(s) associated with that release.

---

<!-- Page 31 -->
Contains Nonbinding Recommendations
27
If the device is a multiple function device product and includes software function(s) that are 
considered “other functions,” as that term is used in the guidance “Multiple Function Device 
Products: Policy and Considerations,” the recommendations described in the aforementioned 
guidance should be considered when preparing the software version history.
Unresolved Software Anomalies  
An anomaly is any condition that deviates from the expected behavior based on user needs, 
requirements, specifications, design documents, or standards. Anomalies may be found during 
the review, test, analysis, compilation, or use of the software (whether before or after release, or 
whether inside a sponsor’s organization or outside it) or at other times. An unresolved software 
anomaly is a defect that still resides in the software because a sponsor deemed it appropriate not 
to correct or fix the anomaly, according to a risk-based rationale about its impact to the device’s 
safety and effectiveness.
A list of unresolved anomalies should document the following items (e.g., in tabular format) for 
each unresolved anomaly present in the software: 
·
A description of the anomaly;
·
Identification of how the anomaly was discovered and, where possible, identification of 
the root cause(s) of the anomaly;
·
Evaluation of the impact of the anomaly on the device’s safety and effectiveness, 
including operator usage and human factors considerations; 
·
Outcome of the evaluation; and 
·
Risk-based rationale for not correcting or fixing the anomaly in alignment with the 
sponsor’s risk management plan or procedure(s).
Additionally, the Agency recommends considering the utilization of a defect classification 
system, or taxonomy, for each anomaly, such as ANSI/AAMI SW91’s Classification of defects 
in health software.58 Regardless of the defect classification system used, the sponsor should 
evaluate the impact of an unresolved anomaly on the device’s safety and effectiveness based on 
the software’s intended use.
Where appropriate, a sponsor should communicate to end users any mitigations or possible 
work-arounds for unresolved anomalies to assist in the proper operation of the device to fulfill its 
intended use. FDA recommends that any planned or already distributed communication
58 As stated in ANSI/AAMI SW91, a defect classification system, or taxonomy, is used to classify or categorize the 
types of defects that might exist in software.  A defect classification system is neutral with respect to programming 
language, methodology, product, intended use, risk (severity of anomalies), and regulatory status.

---

<!-- Page 32 -->
Contains Nonbinding Recommendations
28
(customer notification, labeling, etc.) to end users regarding unresolved anomalies is referenced 
in the premarket submission.
VII. Additional Information ­ Regulatory Considerations for 
Software Functions 
Section 3060(a) of the Cures Act amended section 520 of the FD&C Act on December 13, 2016, 
removing certain software functions from the definition of device in section 201(h) of the FD&C 
Act. Sponsors should consider the following reference materials to learn more about FDA’s 
regulatory considerations for software functions: 
·
Changes to Existing Medical Software Policies Resulting from Section 3060 of the 21st 
Century Cures Act59
·
General Wellness: Policy for Low Risk Devices60
·
Policy for Device Software Functions and Mobile Medical Applications61
·
Medical Device Data Systems, Medical Image Storage Devices, and Medical Image 
Communications Devices62
·
How to Determine if Your Product is a Medical Device63
·
Clinical Decision Support Software64
Appendix A: Documentation Level Examples
The following list of example devices is intended to demonstrate the implementation of the 
Documentation Level risk-based approach. Please note that these generalized examples do not 
necessarily account for every possible detail, risk, or consideration a sponsor should evaluate, 
and should not be taken to mean that the devices described do or do not require a certain 
Documentation Level. These examples do not define the appropriate Documentation Level for a 
particular device type. As such, the Documentation Level should be uniquely considered for each 
particular device or device modification and in consideration of the device’s intended use. The 
rationales in the examples below are abbreviated and FDA encourages sponsors to provide a 
detailed assessment that accounts for the specifics of their device (such as the device’s risk 
assessment,65 software description, etc.) when addressing the recommendations in Sections V 
and VI.A of this guidance.
59 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/changes-existing-
medical-software-policies-resulting-section-3060-21st-century-cures-act.
60 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-
policy-low-risk-devices.
61 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/policy-device-software-
functions-and-mobile-medical-applications.
62 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-data-
systems-medical-image-storage-devices-and-medical-image-communications-devices.
63 Available at https://www.fda.gov/medical-devices/classify-your-medical-device/how-determine-if-your-product-
medical-device.
64 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-
support-software.
65 For more information on risk assessment refer to Section VI.C of this guidance.

---

<!-- Page 33 -->
Contains Nonbinding Recommendations
29
1. A hardware-only non-patient-matched hip prosthesis. 
 
Description: The device is a non-patient-matched hip prosthesis that contains no 
firmware or other means for software-based control. 
Rationale: The device does not contain software. 
Outcome: No Documentation Level
2. A non-contact infrared thermometer intended for intermittent measurement of body 
temperature from the forehead.  
 
Description: The device is intended to measure body temperature from the 
forehead using an infrared sensor. The device is a hand-held, battery powered, 
reusable device for home and professional healthcare facility use.
Rationale: In general, a failure or latent flaw of the device software function(s) 
would not present a hazardous situation with a probable risk of death or serious 
injury to either a patient, user of the device, or others in the environment of use, 
prior to the implementation of risk control measures.
Outcome: Basic Documentation Level
3. A non-invasive blood pressure monitor with inflatable cuff.  
 
Description: The device is intended to measure a person’s systolic and diastolic 
blood pressure in units of mmHg through software-controlled inflation and 
deflation of the cuff. The device is a battery powered, reusable device for home 
and professional healthcare facility use. 
Rationale: In general, a failure or latent flaw of the device software function(s) 
would not present a hazardous situation with a probable risk of death or serious 
injury to either a patient, user of the device, or others in the environment of use, 
prior to the implementation of risk control measures. 
Outcome: Basic Documentation Level
4. A device software function for optical camera-based measurement of pulse rate and 
breathing rate.  
 
Description: The device is intended for non-contact, periodic, spot measurement 
of pulse rate and breathing rate when the subject is at rest. The software analyzes 
compatible video signals of subjects in single occupancy rooms of subjects that do 
not require continuous vital signs monitoring or critical care. The device is

---

<!-- Page 34 -->
Contains Nonbinding Recommendations
30
intended for use by trained staff and is not intended to be the sole method of 
checking the physical health of a subject. 
Rationale: A failure or latent flaw of the device software function(s) would not 
present a hazardous situation with a probable risk of death or serious injury to 
either a patient, user of the device, or others in the environment of use, prior to the 
implementation of risk control measures.
Outcome: Basic Documentation Level
5. A computerized behavioral therapy device to treat psychiatric disorders.  
 
Description: The device is a prescription software device intended to provide a 
computerized version of condition-specific cognitive behavioral therapy as an 
adjunct to clinician supervised outpatient treatment to patients who have been 
previously diagnosed with a psychiatric condition. It is intended to provide 
patients access to therapy tools used during treatment sessions to improve 
recognized treatment outcomes.  It is not intended to substitute for routine in-
person therapy sessions.
Rationale: A failure or latent flaw of the device software function(s) would not 
present a hazardous situation with a probable risk of death or serious injury to 
either a patient, user of the device, or others in the environment of use, prior to the 
implementation of risk control measures.
Outcome: Basic Documentation Level
6. A traumatic brain injury (TBI) eye movement assessment aid.  
 
Description: The device is a prescription device that is intended to track a 
patient’s eye movements using a commercial OTS mobile phone and camera and 
analyze the tracked eye movements to aid in the assessment of mild TBI, 
commonly known as “concussion.” The device provides a positive or negative 
indicator about the presence of eye movements that are consistent with mild TBI. 
Rationale: A failure or latent flaw of the device software function(s) would not 
present a hazardous situation with a probable risk of death or serious injury to 
either a patient, user of the device, or others in the environment of use, prior to the 
implementation of risk control measures. The device is intended for use as an aid 
in the assessment of mild (non-severe) injury and is not intended as a standalone 
diagnostic.
Outcome: Basic Documentation Level
7. An implantable sensor for measuring pulmonary artery (PA) pressure.

---

<!-- Page 35 -->
Contains Nonbinding Recommendations
31
Description: The device is a system comprising a permanent implant that is 
placed in the PA and an external software-controlled reader that retrieves and 
transmits PA pressure measurements. The PA hemodynamic data are used by the 
physician for heart failure management and with the goal of reducing heart failure 
hospitalizations. There are no device software functions located on the implant.
Rationale: While the device is a class III device, a failure or latent flaw of the 
device software function(s) would not present a hazardous situation with a 
probable risk of death or serious injury to either a patient, user of the device, or 
others in the environment of use, prior to the implementation of risk control 
measures. Risks of death or serious injury to the patient in this scenario are due to 
the implantable nature of the device and failure of the hardware or implant 
procedure itself, not the device software function(s). 
Outcome: Basic Documentation Level
8. Over-the-counter (OTC) application for identification of irregular heart rhythms.  
 
Description: The software application is intended for analysis of 
photoplethysmograh data, identification of episodes of irregular heart rhythms 
suggestive of Atrial Fibrillation (AF), and providing notification to the user of the 
irregular rhythm episodes. It is intended to opportunistically provide a notification 
of possible AF and the absence of a notification is not intended to indicate that no 
disease is present. It is intended for OTC use and it is not intended to replace 
traditional methods of diagnosis or treatment.
Rationale: A failure or latent flaw of the device software function(s) would not 
present a hazardous situation with a probable risk of death or serious injury to 
either a patient, user of the device, or others in the environment of use, prior to the 
implementation of risk control measures.
Outcome: Basic Documentation Level
9. An in vitro nucleic acid test for the qualitative detection of Human Papillomavirus (HPV) 
DNA in human cervical specimens.  
Description: The test is intended for routine cervical cancer screening as per 
professional medical guidelines, including triage of ASC-US (atypical squamous 
cells of undetermined significance) cytology, co-testing (or adjunctive screen) 
with cytology, and HPV primary screening of women to assess the risk for 
cervical precancer and cancer. Patients should be followed-up in accordance with 
professional medical guidelines, results from prior screening, medical history, and 
other risk factors.

---

<!-- Page 36 -->
Contains Nonbinding Recommendations
32
Rationale: While the test is classified as a class III device, a failure or latent flaw 
of the device software function(s) would not present a probable risk of death or 
serious injury to either a patient, user of the device, or others in the environment 
of use prior to the implementation of risk control measures. There are several 
alternatives for the detection of cervical cancer precursors including testing by 
cytology alone, co-testing with HPV alongside or as a follow-up to cytology or 
HPV testing as a first line screening test for cervical cancer. The patient’s age, 
medical history, and thorough physical examination will provide further 
information on the risk of cervical disease, as well as the need for referral to 
colposcopy. The test should only be used in conjunction with this clinical 
information in accordance with professional clinical patient management 
guidelines.
Outcome: Basic Documentation Level
10. An in vitro nucleic acid test for the qualitative detection and differentiation of influenza 
A virus, influenza B virus, and respiratory syncytial virus (RSV) RNA in nasopharyngeal 
swabs from human patients with signs and symptoms of respiratory tract infection in 
conjunction with clinical and epidemiological risk factors.  
 
Description: The test is intended for use as an aid in the differential diagnosis of 
influenza A, influenza B, and RSV viral infections in humans. Negative results do 
not preclude influenza virus or RSV infection and should not be used as the sole 
basis for treatment or other patient management decisions.
Rationale: A failure or latent flaw of the device software function(s) would not 
present a hazardous situation with a probable risk of death or serious injury to 
either a patient, user of the device, or others in the environment of use prior to the 
implementation of risk control measures.  
Outcome: Basic Documentation Level
11. A device software function on a commercial OTS head-mounted display (e.g., augmented 
reality/virtual reality/mixed reality (AR/VR/MR)) that superimposes pre-surgical images 
on a patient’s body.  
 
Description: The device is intended to provide real-time superimposition of 
medical images on the patient during a surgical procedure, but is neither intended 
to directly guide surgical planning or procedures nor be worn by the lead surgeon. 
Rationale: A failure or latent flaw of the device software function(s) would not 
present a hazardous situation with a probable risk of death or serious injury to 
either a patient, user of the device, or others in the environment of use prior to the 
implementation of risk control measures, since the device is neither intended to 
directly guide surgical planning or procedures nor be worn by the lead surgeon.

---

<!-- Page 37 -->
Contains Nonbinding Recommendations
33
Outcome: Basic Documentation Level
12. A laser system for the treatment of acne vulgaris.  
 
Description: The device is a laser system used in dermatology offices used to 
treat acne vulgaris through heating of dermal tissue. The device software only 
operates the laser engine. Delivery of therapy requires the operator to depress a 
physical switch on the handpiece. 
Rationale: A failure or latent flaw of the device software functions(s), such as not 
delivering the laser energy when directed, would not present a hazardous situation 
with a probable risk of death or serious injury to the patient prior to the 
implementation of risk control measures. 
Outcome: Basic Documentation Level
13. A radiological display device.  
 
Description:  The device is intended for displaying clinical radiology images for 
review, analysis, and diagnosis by trained medical practitioners. The software 
contained in the device is limited to the following functionalities: display controls, 
ambient light sensing, luminance calibration tools, and quality-control software.
Rationale: A failure or latent flaw of the device software function(s), such as 
inadequate quality of displayed images, would not present a hazardous situation 
with a probable risk of death or serious injury to either a patient, user of the 
device, or others in the environment of use, prior to the implementation of risk 
control measures.
Outcome: Basic Documentation Level
14. An electric breast pump.  
 
Description: The device is intended to be used by lactating women to express and 
collect milk from their breasts. The device uses a DC-powered motor driving the 
vacuum pump which is controlled electronically to provide a range of user-
selected suction levels at specified cycle frequencies. The device display provides 
the user with information on the pumping mode, timer, battery level, and suction. 
Rationale: A failure or latent flaw of the device software function(s) (e.g., 
software fails to properly control the suction level) would not present a hazardous 
situation with a probable risk of death or serious injury to either a patient, user of 
the device, or others in the environment of use prior to the implementation of risk 
control measures.  
Outcome: Basic Documentation Level

---

<!-- Page 38 -->
Contains Nonbinding Recommendations
34
15. An implantable cardiac pacemaker used to treat bradycardia.  
 
Description: The device is an implanted, programmable dual-chamber pulse 
generator intended to provide rate-adaptive bradycardia therapy as well as other 
therapeutic and diagnostic functionality. It senses the heart’s electrical activity 
and generates electrical impulses to cause the heart to contract or beat according 
to the programmed patient’s needs. It communicates with a programmer and the 
patient’s home monitoring device.
Rationale: A failure or latent flaw of the device software function(s), such as 
failure to pace or a latent flaw leading to incorrect sensing of an ectopic beat, 
would lead to a hazardous situation that would present a probable risk of death or 
serious injury to the patient prior to the implementation of risk control measures. 
Outcome: Enhanced Documentation Level
16. A facility use continuous ventilator. 
 
Description: The device is intended to provide continuous ventilation for adult, 
pediatric, and neonatal patients who require invasive or noninvasive respiratory 
support. It allows clinicians to set ventilator control parameters, set alarm limits, 
and view monitored values and waveforms for patient management. It includes 
respiratory monitoring as well as both mandatory and spontaneous ventilation 
modes. It is intended for use in professional healthcare facilities. 
Rationale: A failure or latent flaw of the device software function(s), such as 
failure to provide appropriately timed ventilation, would present a hazardous 
situation with a probable risk of death or serious injury to a patient, prior to the 
implementation of risk control measures.
Outcome: Enhanced Documentation Level
17. A multi-parameter patient monitor for use in a professional healthcare facility.  
 
Description: The device is a multi-parameter monitor intended for use on adult, 
pediatric, and neonatal patients in a professional healthcare facility. It is used for 
monitoring of various hemodynamic and respiratory vital signs and parameters, 
including central venous oxygen saturation, electrocardiogram (ECG), arrhythmia 
detection, invasive and non-invasive blood pressure, temperature, cardiac output, 
hemoglobin concentration, pulse oximetry, spirometry, airway gases, and gas 
exchange. It is designed to detect alarm conditions and generate alarm signals. It 
can be connected to the hospital network and other monitors to allow for remote 
viewing and management of patients.

---

<!-- Page 39 -->
Contains Nonbinding Recommendations
35
Rationale: A failure or latent flaw of the device software function(s), such as 
incorrect calculation of parameters or an exploited cybersecurity vulnerability that 
compromises its ability to provide life-threatening arrhythmia detection and 
alarms, would present a hazardous situation with a probable risk of death or 
serious injury to a patient, prior to the implementation of risk control measures.
Outcome: Enhanced Documentation Level
18. A Blood Establishment Computer Software (BECS) or BECS accessory.  
 
Description:  The device is used in the manufacture of blood and blood 
components to assist in the prevention of disease in humans by identifying 
ineligible donors, by preventing the release of unsuitable blood and blood 
components for transfusion or for further manufacturing into products for human 
treatment or diagnosis, by performing compatibility testing between donor and 
recipient, or by performing positive identification of patients and blood 
components at the point of transfusion to prevent transfusion reactions. A BECS 
accessory is a device intended for use with BECS to augment the performance of 
the BECS or to expand or modify its indications for use.
Rationale: A failure or latent flaw of the device software function(s), such as a 
failure to prevent the release of unsuitable blood and blood components, would 
present a hazardous situation with a probable risk of death or serious injury to a 
patient, prior to the implementation of risk control measures.
Outcome: Enhanced Documentation Level
19. A qualitative in vitro nucleic acid screening test for the direct detection of Babesia DNA 
and RNA in whole blood samples from individual human donors.  
 
Description: The device is a screening test that includes device software for 
detection of Babesia DNA and RNA in whole blood samples to prevent the 
release of unsuitable blood and blood components.
Rationale: A failure or latent flaw of the device software function(s), such as an 
inaccurate result in the identification of a transfusion-transmitted infection, would 
present a hazardous situation with a probable risk of death or serious injury to a 
patient, or serious injury, prior to the implementation of risk control measures.
Outcome: Enhanced Documentation Level
20. An infusion pump intended for use in a health care facility to pump fluids and 
medications into a patient.  
 
Description: The device is intended for use on adults, pediatrics, and neonates for 
the intermittent or continuous delivery of fluids, medications, blood, and blood

---

<!-- Page 40 -->
Contains Nonbinding Recommendations
36
products through clinically accepted routes of administration (intravenous, intra-
arterial, subcutaneous, epidural, and enteral). It is intended for use by trained 
health care professionals in healthcare facilities. 
Rationale: A failure or latent flaw of the device software function(s), such as 
providing the incorrect flow rate or failing to deliver fluids/medications, would 
present a hazardous situation with a probable risk of death or serious injury to 
either a patient, user of the device, or others in the environment of use, prior to the 
implementation of risk control measures.
Outcome: Enhanced Documentation Level
21. An in vitro nucleic acid test for the quantitative measurement of Cytomegalovirus (CMV) 
DNA in human plasma or whole blood.  
 
Description: The test is intended for use as an aid in the management of CMV in 
solid organ transplant patients and in hematopoietic stem cell transplant patients. 
In patients receiving anti-CMV therapy, DNA measurements can be used to 
assess viral response to treatment.  The results from the test must be interpreted 
within the context of all relevant clinical and laboratory findings and is not 
intended for use as a screening test for blood or blood products
Rationale: The test is classified as a class III device.  Furthermore, a failure or 
latent flaw of the device software function(s), such as failure to provide correct 
test results, would present a hazardous situation with a probable risk of death or 
serious injury to the patient prior to the implementation of risk control measures.  
Outcome: Enhanced Documentation Level
22. A device software function that provides a sepsis alarm to a healthcare provider in a 
critical care environment.  
 
Description: Software intended to analyze patient demographics, vital signs, and 
lab results from an electronic medical record to provide asepsis alarm identifying 
patients with sepsis or at risk of developing sepsis earlier than a healthcare 
provider would otherwise. The patient clinical data used as an input for the 
software is part of ongoing or active monitoring of the patient’s current health 
state in a critical care environment.  
Rationale: A failure or latent flaw of the device software function(s), such as 
failure to provide a sepsis alarm) would present a hazardous situation with a 
probable risk of death or serious injury to either a patient, user of the device, or 
others in the environment of use prior to the implementation of risk control 
measures.  
Outcome: Enhanced Documentation Level

---

<!-- Page 41 -->
Contains Nonbinding Recommendations
37
23. A continuous glucose monitoring system.  
 
Description: The device is intended to provide real time, continuous glucose 
monitoring for the management of diabetes in persons 2 years of age and older. It 
is intended to replace fingerstick blood glucose testing for diabetes treatment 
decisions. It aids in the detection of episodes of hyperglycemia and hypoglycemia 
and facilitates both acute and chronic therapy adjustments. 
Rationale: A failure or latent flaw of the device software function(s), such as 
failure to provide correct blood glucose measurement or detection of 
hypoglycemia, would present a hazardous situation with a probable risk of death 
or serious injury to either a patient, user of the device, or others in the 
environment of use prior to the implementation of risk control measures.  
Outcome: Enhanced Documentation Level
24. Powered Lower Extremity Exoskeleton.  
 
Description: A powered lower extremity exoskeleton is a prescription device that 
is composed of an external, powered, motorized orthosis that is placed over a 
person's paralyzed or weakened limbs for medical purposes.
Rationale: A failure or latent flaw of the device software function(s), such as loss 
of remote control or movement signal processing, could present a hazardous 
situation with a probable risk of death or serious injury to the patient prior to the 
implementation of risk control measures.  
Outcome: Enhanced Documentation Level
25. A retinal diagnostic software device.  
 
Description: The device is limited to prescription use and incorporates an 
AI/ML-enabled algorithm that is intended to evaluate images for diagnostic 
screening to identify retinal diseases or conditions.  
Rationale: A failure or latent flaw of the device software function(s), such as a 
diagnostic algorithm failure that provides a false result, could present a hazardous 
situation with a probable risk of death or serious injury to the patient prior to the 
implementation of risk control measures.  
Outcome: Enhanced Documentation Level
26. A radiation therapy treatment system (e.g., Linear accelerator).

---

<!-- Page 42 -->
Contains Nonbinding Recommendations
38
Description: The device is intended to noninvasively deliver a focal dose of 
radiation to a specified volume of a patient's anatomy while sparing the 
surrounding normal tissues and structures.
Rationale: A failure or latent flaw of the device software function(s), such as 
under- or overdose to a target volume or delivery to the wrong volume, could 
present a hazardous situation with a probable risk of death or serious injury to the 
patient prior to the implementation of risk control measures.
Outcome: Enhanced Documentation Level
27. A drug-device combination, with the device constituent part detecting ingestion of the 
drug component to prevent treatment failure. 
 
Description: The product is a combination product comprised of two regulated 
components (drug and device). The “primary mode of action”66 is the drug 
component, provided as a tablet. The device constituent part detects ingestion of 
the tablet component to monitor adherence to the drug regimen. A missed dose 
greatly increases the likelihood of treatment failure for a life-threatening 
condition. The device constituent part includes hardware (sensors) and software 
(signal processing). 
Rationale: A failure or latent flaw of the device software function(s), such as a 
false detection of tablet ingestion, would present a hazardous situation with a 
probable risk of death or serious injury to either a patient (through worsening of 
the life-threatening disease), user of the device, or others in the environment of 
use, prior to the implementation of risk control measures.
Outcome: Enhanced Documentation Level
66 Section 503(g)(1)(C) of the FD&C Act states that the term “primary mode of action” means “the single mode of 
action of a combination product expected to make the greatest contribution to the overall intended therapeutic 
effects of the combination product.”

---

<!-- Page 43 -->
Contains Nonbinding Recommendations
39
Appendix B: System and Software Architecture Diagram 
Examples 
The three example diagrams below are simplified for the purpose of demonstrating how the 
considerations described in Section VI.E (System and Software Architecture Diagram) could be 
implemented into diagrams that facilitate a clear understanding of the system and software. Each 
diagram is supported by descriptive text and a brief discussion on notable features. The examples 
are intended for illustration purposes only and do not describe a complete and comprehensive 
system and software architecture diagram. 
The illustrative diagrams are based on the following distinct example devices:
1. A hand-held diagnostic device
2. An implantable therapeutic device with patient- and provider-facing applications
3. A cloud-based device algorithm for analyzing previously captured medical images
The diagrams are largely static diagrams with high-level identification of interfaces between 
system and software components. The use of any specific design or formatting features is only 
provided as a suggestion and does not preclude the use of alternative approaches and/or OTS 
modeling languages or platforms.

---

<!-- Page 44 -->
Contains Nonbinding Recommendations
40
Figure 1: Example System and Software Architecture Diagram – Hand-Held Diagnostic 
Device
Figure 1 depicts a static, high-level system and software architecture diagram of the modules in a 
fictional hand-held diagnostic device. A legend is provided to describe visual features used to 
identify different components. References are provided to documents containing more 
information, including other static diagrams, dynamic diagrams, and detailed descriptions. An 
annotation is provided to improve clarity on the purpose of one module. Text is provided with 
adequate clarity and font size for readability.

---

<!-- Page 45 -->
Contains Nonbinding Recommendations
41
Figure 2: Example System and Software Architecture Diagram – Implantable Therapeutic 
Device with Patient- and Provider-Facing Applications
Figure 2 depicts a static, high-level system and software architecture diagram of the modules in a 
fictional implantable therapeutic device. The example depicts the implementation of device 
software functions on OTS platforms, including a cloud computing platform and a smartphone 
application.

---

<!-- Page 46 -->
Contains Nonbinding Recommendations
42
Figure 3: Example System and Software Architecture Diagram - Cloud-based Device 
Algorithm for Analyzing Previously Captured Medical Images
Figure 3 depicts a static, high-level system and software architecture diagram of the modules in a 
fictional cloud-based algorithm for analyzing previously captured medical images. The example 
shows how a software-only function can be described from a platform-level perspective.

<!-- fulltext-end -->
