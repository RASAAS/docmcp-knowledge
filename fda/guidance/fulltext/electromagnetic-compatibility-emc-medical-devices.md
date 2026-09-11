# Electromagnetic Compatibility (EMC) of Medical Devices: Guidance for Industry and Food and Drug Administration Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/electromagnetic-compatibility-emc-medical-devices](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/electromagnetic-compatibility-emc-medical-devices)

**Published:** 2022-06-06

---

<!-- Page 1 -->
Contains Nonbinding Recommendations 
 
 
1 
 
Electromagnetic Compatibility (EMC) 
of Medical Devices 
 
Guidance for Industry and  
Food and Drug Administration Staff  
 
Document issued on June 6, 2022. 
 
The draft of this document was issued on November 17, 2020. 
 
This document will supersede “Information to Support a Claim of 
Electromagnetic Compatibility (EMC) of Electrically-Powered Medical 
Devices,” issued July 11, 2016, 1 year after the publication of this guidance for 
in vitro diagnostics and 60 days after the publication of this guidance for other 
device types within the scope of this guidance. 
 
For questions about this document, contact the Office of Science and Engineering Laboratories 
(OSEL) at OSEL_CDRH@fda.hhs.gov or (301) 796-2530; the Division of Biomedical Physics, 
OSEL at (301) 796-2580; or Seth Seidman at (301) 796-2477 or by email at 
seth.seidman@fda.hhs.gov. For questions about this document regarding CBER-regulated 
devices, contact the Office of Communication, Outreach, and Development (OCOD) at 1-800-
835-4709 or 240-402-8010, or by email at ocod@fda.hhs.gov. 
 
 
 
 
 
 
 
 
 
 
 
 
 
U.S. Department of Health and Human Services 
Food and Drug Administration 
Center for Devices and Radiological Health 
Center for Biologics Evaluation and Research

---

<!-- Page 2 -->
Contains Nonbinding Recommendations 
2 
Preface 
Public Comment 
You may submit electronic comments and suggestions at any time for Agency consideration to 
https://www.regulations.gov. Submit written comments to the Dockets Management Staff, Food 
and Drug Administration, 5630 Fishers Lane, Room 1061, (HFA-305), Rockville, MD 20852. 
Identify all comments with the docket number FDA-2015-D-3787. Comments may not be acted 
upon by the Agency until the document is next revised or updated. 
Additional Copies 
CDRH
Additional copies are available from the Internet. You may also send an e-mail request to 
CDRH-Guidance@fda.hhs.gov to receive a copy of the guidance. Please use the document 
number 1400057 and complete title of the guidance in the request. 
CBER 
Additional copies are available from the Center for Biologics Evaluation and Research (CBER), 
Office of Communication, Outreach, and Development (OCOD), 10903 New Hampshire Ave., 
Bldg. 71, Room 3128, Silver Spring, MD 20993-0002, or by calling 1-800-835-4709 or 240-402-
8010, by email, ocod@fda.hhs.gov or from the Internet at https://www.fda.gov/vaccine 
s-blood-
biologics/guidance-compliance-regulatory-information-biologics/biologics-guidances.

---

<!-- Page 3 -->
Contains Nonbinding Recommendations 
 
 
3 
 
Table of Contents 
 
I. 
Introduction ............................................................................................................................. 4 
II. 
Scope ....................................................................................................................................... 5 
III. 
Overview .............................................................................................................................. 5 
IV. 
EMC Information for Premarket Submissions .................................................................... 6 
 
EMC-Related Device Characteristics and Intended Use Environments .......................... 7 
 
Assessment of Medical Device Risks .............................................................................. 8 
 
Consensus Standards ........................................................................................................ 8 
(1) 
Non-implantable Medical Devices ............................................................................... 9 
(2) 
Active Implantable Medical Devices (AIMDs) .......................................................... 10 
(3) 
Special Environments ................................................................................................. 11 
 
Essential Performance and Immunity Pass/Fail Criteria ................................................ 11 
(1) 
Essential Performance ................................................................................................ 11 
(2) 
Immunity Pass/Fail Criteria ........................................................................................ 12 
 
Medical Device Configuration and Functions Tested .................................................... 13 
 
Results of EMC Testing ................................................................................................. 15 
 
Allowances ..................................................................................................................... 15 
 
Deviations ....................................................................................................................... 15 
 
Modifications ................................................................................................................. 16 
 
Common Electromagnetic (EM) Emitters ...................................................................... 16 
 
Labeling .......................................................................................................................... 17 
V. 
EMC Information to Support Investigational Device Exemption (IDE) or Investigational 
New Drug (IND) Submissions ...................................................................................................... 19 
Appendix A – Examples of Typical Medical Device Locations within Intended Use 
Environments ................................................................................................................................ 20

---

<!-- Page 4 -->
Contains Nonbinding Recommendations 
 
 
4 
 
Electromagnetic Compatibility (EMC) 
of Medical Devices 
  
 
Guidance for Industry and 
Food and Drug Administration Staff 
 
 
This guidance represents the current thinking of the Food and Drug Administration (FDA or 
Agency) on this topic.  It does not establish any rights for any person and is not binding on 
FDA or the public.  You can use an alternative approach if it satisfies the requirements of the 
applicable statutes and regulations.  To discuss an alternative approach, contact the FDA staff 
or Office responsible for this guidance as listed on the title page.  
 
I. 
Introduction 
The Food and Drug Administration (FDA) has developed this guidance document to recommend 
information that should be provided in a premarket submission (i.e., premarket approval (PMA) 
application, humanitarian device exemption (HDE), premarket notification (510(k)) submission, 
investigational device exemption (IDE), De Novo request, and certain biologics license 
application (BLA) and investigational new drug (IND)1) to demonstrate electromagnetic 
compatibility (EMC) for electrically-powered medical devices and medical devices with 
electrical or electronic functions. Typically, the review of EMC information in a submission is 
based on the risk associated with malfunction or degradation of the medical device under 
consideration, where malfunction or degradation could be caused by inadequate EMC. The 
review is also based on the use of appropriate consensus standards. This guidance, when final, 
will replace the FDA guidance, “Information to Support a Claim of Electromagnetic 
Compatibility (EMC) of Electrically-Powered Medical Devices” (hereafter referred to as the 
2016 EMC guidance), published July 11, 2016. This guidance provides additional technical 
information to address the recommendations in the 2016 EMC guidance. Throughout this 
guidance, the terms “FDA,” “the Agency,” “we,” and “us” refer to the Food and Drug 
Administration and the terms “you” and “yours” refer to medical device manufacturers. 
 
For the current edition of the FDA-recognized consensus standard(s) referenced in this 
document, see the FDA Recognized Consensus Standards Database.2 For more information 
 
1 INDs and BLAs for devices that are regulated as biological products under section 351 of the Public Health 
Service (PHS) Act. 
2 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm

---

<!-- Page 5 -->
Contains Nonbinding Recommendations 
 
 
5 
 
regarding use of consensus standards in regulatory submissions, please refer to the FDA 
guidance titled “Appropriate Use of Voluntary Consensus Standards in Premarket Submissions 
for Medical Devices.”3 
  
The contents of this document do not have the force and effect of law and are not meant to bind 
the public in any way, unless specifically incorporated into a contract. This document is intended 
only to provide clarity to the public regarding existing requirements under the law. FDA 
guidance documents, including this guidance, should be viewed only as recommendations, unless 
specific regulatory or statutory requirements are cited. The use of the word should in Agency 
guidance means that something is suggested or recommended, but not required.  
 
 
II. Scope 
This guidance applies to medical devices, including in vitro diagnostic products,4 and 
accessories5 that:  
• are electrically-powered; or 
• have functions or sensors that are implemented using electrical or electronic circuitry. 
 
FDA recognizes and anticipates that the Agency and industry may need up to 1 year to perform 
activities to operationalize the policies within the guidance, only for in vitro diagnostic products. 
Since this guidance generally reflects current practice for the assessment of EMC for other 
device types, but some activities to fully operationalize the policies are needed (e.g., updates to 
eSTAR6), FDA intends to implement this guidance 60 days after issuance for device types within 
the scope of this guidance, excluding in vitro diagnostic products. If new information regarding 
electromagnetic compatibility as outlined in this guidance is not included in a premarket 
submission for an in vitro diagnostic received by FDA before or up to 1 year after the publication 
of this guidance or for other device types within the scope of this guidance before or up to 60 
days after the publication of this guidance, FDA does not generally intend to request such 
information during the review of the submission. FDA does, however, intend to review any such 
information if submitted. 
 
III. Overview 
For the purpose of this document, EMC is defined as the ability of a medical device to function 
safely and effectively in its intended electromagnetic (EM) environment, including immunity to 
 
3 https://www.fda.gov/regulatory-information/search-fda-guidance-documents/appropriate-use-voluntary-consensus-
standards-premarket-submissions-medical-devices 
4 See 21 CFR 809.3(a) 
5 For more information, see “Medical Device Accessories - Describing Accessories and Classification Pathways: 
Guidance for Industry and FDA Staff” at https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/medical-device-accessories-describing-accessories-and-classification-pathways and “Medical Device 
Accessories” at https://www.fda.gov/medical-devices/classify-your-medical-device/medical-device-accessories  
6 Available at https://www.fda.gov/medical-devices/premarket-notification-510k/voluntary-estar-program

---

<!-- Page 6 -->
Contains Nonbinding Recommendations 
 
 
6 
 
EM disturbances (i.e., interference)7, without introducing excessive EM disturbances (i.e., 
emissions) that might interfere with other equipment. Immunity is the ability to protect against 
unacceptable degradation due to EM disturbances such as radio waves, power surges, 
radiofrequency (RF) disturbances, and electrostatic discharge (ESD). Interference can cause 
medical devices to not perform as intended and lead to hazardous situations, such as delays or 
errors in diagnosis, treatment, or monitoring that can result in serious injury or death. Emissions 
limits are established to protect radio services and minimize interference to other equipment, 
both medical and non-medical. 
 
The IEC 60601/806018 series of standards applies to medical devices and systems that directly 
apply or transfer energy to the patient, and the IEC 61010-1 standard applies to electrical 
laboratory equipment. These standards are used in the majority of premarket submissions for 
electrically-powered medical devices to support device safety. These standards attempt to 
address all hazards (e.g., mechanical, electrical, radiation). Besides addressing the wide range of 
generic safety requirements, the IEC 60601/80601 and IEC 61010 series include close to 100 
“particular standards” with safety requirements for specific types of devices, such as clinical 
thermometers, infusion pumps, infant incubators, laboratory centrifuges, medical device 
sterilizers and reprocessors, and medical washer-disinfectors.  There are also consensus 
standards for active implantable medical devices that include information on EMC. 
 
For electrically-powered medical devices and medical devices with electrical or electronic 
functions, you should provide evidence that the medical device is safe and performs as intended 
in the environments of use.  This evidence includes risk management with regard to EM 
disturbances, testing, and labeling, as recommended in this guidance. To facilitate premarket 
submissions and reviews for EMC, we recommend you include the information listed in Section 
IV. Section V contains additional information specific to IDE or IND submissions. 
 
IV. EMC Information for Premarket Submissions 
To facilitate the review of EMC information in premarket submissions, we recommend you 
include the information listed in subsections A-K below in the EMC section of the submission, 
labeled with the section headings in the same order as they are listed in this guidance.  If test 
reports or test report summaries (e.g., Accreditation Scheme for Conformity Assessment 
Summary Test Report9) or other sections of the premarket submission include any of the 
 
7 To harmonize with international definitions, this document will use the word “disturbance” as the cause (per IEC 
60601-1-2) and “interference” as the effect (per IEC 60050). In the US, “interference” is often used interchangeably 
for both cause and effect. 
8 In this document, the reference to the IEC 60601/80601 series of standards includes the ANSI/AAMI ES 60601-1, 
the IEC and US adopted collaterals [60601-1-xx], the IEC 60601-2-xx, and the IEC or ISO 80601-2-xx particulars. 
9 For more information, see the FDA guidance: “The Accreditation Scheme for Conformity Assessment (ASCA) 
Pilot Program” available at https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/accreditation-scheme-conformity-assessment-asca-pilot-program and “Basic Safety and Essential 
Performance of Medical Electrical Equipment, Medical Electrical Systems, and Laboratory Medical Equipment - 
Standards Specific Information for the Accreditation Scheme for Conformity Assessment (ASCA) Pilot Program” 
available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/basic-safety-and-essential-
performance-medical-electrical-equipment-medical-electrical-systems-and

---

<!-- Page 7 -->
Contains Nonbinding Recommendations 
 
 
7 
 
recommended information below, the specific location within these documents should be noted 
in the EMC section of the submission. 
 
EMC-Related Device Characteristics and Intended Use 
Environments 
We recommend that you provide a description of all EMC-related device characteristics 
and intended use environments including: 
 
• an overview of the device and its functions and modes, including block diagrams, 
photographs, cables, relevant accessories, and device interoperability; 
• a description of the power supply (i.e., mains-powered only, internally-powered only, 
mains and internally-powered) including if the internally-powered medical device can 
be used while charging; 
• a statement regarding the environments in which the medical device is intended to be 
used (see Appendix A); 
• a description of any wireless technology (for additional considerations regarding 
wirelessly-enabled medical devices, refer to FDA guidance, Radio Frequency 
Wireless Technology in Medical Devices10); and 
• a description of any intentional RF emitters in the medical device that could be 
sources of EM disturbances. 
 
Specifying the intended use environments provides important information to determine 
the appropriate testing for expected EM disturbances. For the purposes of this guidance 
and EMC evaluation, we categorize the intended use environments into one (or more) of 
the following environments: 
 
• Professional Healthcare Facility Environment: any environment where personnel with 
medical training are continually available to oversee or administer the use of medical 
devices.  This includes, but is not limited to, hospitals, long-term care facilities, 
nursing homes, limited care facilities, emergency medical services, clinics, 
physicians’ offices, outpatient treatment facilities, and clinical laboratories. 
• Home Healthcare Environment: any environment where personnel with medical 
training are not continually available to oversee or administer the use of medical 
devices. This includes, but is not limited to, outdoor environments, office 
environments, schools, vehicles, emergency shelters, and independent living 
retirement homes. 
• Special Environment: any environment with EM characteristics different from those 
specified in EMC consensus standards. This includes, but is not limited to, aircraft, 
military areas, heavy industrial areas, medical treatment areas with high-powered 
medical devices such as magnetic resonance imaging (MRI). 
 
 
10 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/radio-frequency-
wireless-technology-medical-devices-guidance-industry-and-fda-staff.

---

<!-- Page 8 -->
Contains Nonbinding Recommendations 
 
 
8 
 
See Appendix A for examples of typical medical device locations for each of the three 
intended use environments mentioned above. 
 
When considering the intended use environments, we recommend addressing common 
EM emitters and unique medical emitters. These emitters are listed and discussed in 
detail in Section IV.J below.  
 
 
Assessment of Medical Device Risks 
We recommend that you provide a summary description of the risks associated with 
malfunction, disruption, or degradation of the performance of the subject medical device 
due to EM disturbances. This should include each potential malfunction, disruption, or 
degradation due to electromagnetic interference (EMI) that could cause harm to the 
patient, user or operator. This summary should categorize the severity of each harm into 
the following three levels based upon the FDA guidance, “Factors to Consider Regarding 
Benefit-Risk in Medical Device Product Availability, Compliance, and Enforcement 
Decisions Guidance for Industry and FDA Staff”11: 
 
• Medical device-related deaths and serious injuries12 include events (including 
procedure-related complications) in the use of the medical device that have caused or 
could cause or contribute to a death or injury or illness that is life-threatening, results 
in permanent impairment or damage to the body, or requires medical or surgical 
intervention to prevent permanent harm to the body.  
• Medical device-related non-serious adverse events include events (including 
procedure-related complications) in the use of the medical device that have caused or 
could cause or contribute to minor, temporary or medically reversible injuries that do 
not meet the criteria for classification as a medical device-related serious injury.  
• Medical device-related events without reported or potential harm include medical 
device nonconformities that have no related harm, medical device malfunctions that 
have no related harm, and procedure-related complications with no related harm. 
 
These considerations should be used in determining the immunity pass/fail criteria (see 
Section IV.D) and in addressing EMI caused by common EM emitters (see Section IV.J). 
For the 60601 series of standards, a risk analysis is used to determine the Essential 
Performance,13 upon which the immunity pass/fail criteria are based, as well as other 
aspects of EMC testing (e.g., additional modulation frequencies). 
 
Consensus Standards 
We recommend that you provide a summary describing all voluntary consensus standards 
used to evaluate EMC. When applicable, we recommend that EMC tests be performed 
 
11 https://www.fda.gov/regulatory-information/search-fda-guidance-documents/factors-consider-regarding-benefit-
risk-medical-device-product-availability-compliance-and  
12 See 21 CFR 803.3(w) 
13 Essential Performance is a defined term from ANSI/AAMI/ES 60601-1:2005 Medical electrical equipment - Part 
1: General requirements for basic safety and essential performance. See Section IV.D below for more details.

---

<!-- Page 9 -->
Contains Nonbinding Recommendations 
 
 
9 
 
using methods described in FDA-recognized consensus standards that are appropriate for 
the medical device. If you chose to declare conformity to a standard, we recommend 
providing the supporting information described in this guidance and consistent with the 
FDA guidance “Appropriate Use of Voluntary Consensus Standards in Premarket 
Submissions for Medical Devices.”14 The extent of FDA recognition of a consensus 
standard is included in the Supplemental Information Sheet (SIS) published in the FDA 
Recognized Consensus Standards Database.15 The “Extent of Recognition” section of the 
SIS can specify an acceptable deviation or non-recognized clauses from the published 
standard. The “Transition” section of the SIS can specify the date when recognition of 
one edition of a standard is superseded by the next edition. A cleared or approved device 
does not need to be assessed or submitted again as a result of any changes to an FDA-
recognized EMC consensus standard.16  
 
If the consensus standard(s) referenced in the submission are not recognized by FDA,17 
sufficient justification should be provided regarding how the EMC testing performed 
adequately addresses EMC, based on the medical device’s functions, modes, indications 
for use, intended use, and intended use environments. If no consensus standard exists for 
a certain medical device type, we recommend specific EMC testing be performed based 
on foreseeable EM disturbances in the intended use environments. We recommend 
referencing an existing FDA-recognized consensus standard for a similar medical device 
type and environment and modifying the test specifications in the standard to address the 
subject medical device. Each change in test specification should be documented and 
accompanied by justification. 
 
When using consensus standards, we recommend verifying that the intended use 
environments are adequately addressed by the standards. Many consensus standards only 
address and specify test levels for the home healthcare environment and the professional 
healthcare facility environment. 
 
The medical device configuration and intended use environments can determine the 
applicability of FDA-recognized consensus standards for EMC. These can be generalized 
into one or more of the following three categories: 
(1) Non-implantable Medical Devices 
The ANSI/AAMI/IEC 60601-1-2 Medical electrical equipment – Part 1-2: General 
requirements for basic safety and essential performance – Collateral Standard: 
 
14 https://www.fda.gov/regulatory-information/search-fda-guidance-documents/appropriate-use-voluntary-
consensus-standards-premarket-submissions-medical-devices 
15 http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm  
16 For more information, refer to Section VIII of the FDA guidance, When Devices or Standards Change After 
Marketing Authorization, of the “Appropriate Use of Voluntary Consensus Standards in Premarket 
Submissions for Medical Devices” guidance available at https://www.fda.gov/regulatory-information/search-fda-
guidance-documents/appropriate-use-voluntary-consensus-standards-premarket-submissions-medical-devices. 
17 For more information on use of consensus standards that are not FDA-recognized, refer to Section IV B. General 
Use of the “Appropriate Use of Voluntary Consensus Standards in Premarket Submissions for Medical Devices” 
guidance.

---

<!-- Page 10 -->
Contains Nonbinding Recommendations 
 
 
10 
 
Electromagnetic disturbances – Requirements and tests is a collateral standard to the 
ANSI/AAMI ES 60601-1 Medical electrical equipment - Part 1: General requirements 
for basic safety and essential performance standard and is recognized by FDA for testing 
of non-implantable medical devices that are within its scope. The 60601-1-2 consensus 
standard provides details about testing medical devices for safety with regard to EM 
disturbances based on the Basic Safety18 and Essential Performance of the medical 
device, the medical device design, and the intended use environments.  
 
When using any consensus standard, careful consideration to the scope is critical. For 
example, the scope of 60601 standards is limited to medical device safety. Evaluation of 
medical device effectiveness is generally not within the scope of 60601 standards. This is 
discussed in detail in subsection D(2) below. 
 
There are over 80 particular consensus standards (e.g., IEC 60601-2-X, ISO 80601-2-X) 
that cover a wide variety of medical devices.  These particular consensus standards 
augment or supersede the specifications in 60601-1-2 and can provide more detailed or 
alternative EM test specifications. However, not all particular consensus standards are 
FDA recognized at the time of this guidance publication, and the EMC specifications in 
these particular standards should be assessed to ensure that they are appropriate for the 
medical device’s functions, modes, indications for use, intended use, and intended use 
environments. 
 
Most laboratory equipment and in vitro diagnostic devices (IVDs) are outside the scope 
of 60601-1-2. At the time of the issuance of this guidance, we partially recognize IEC 
61326-1:2020 and IEC 61326-2-6:2020 and recommend using the test methods from 
these standards. However, we recommend using acceptance criteria specific to the 
device’s functions and intended use.  Additionally, we recommend using test levels 
specified by 60601-1-2 or, alternatively, determining the reasonably foreseeable 
maximum levels of the electromagnetic phenomena in the device intended use 
environments (e.g., through study of published literature or environmental 
measurements).  
(2) Active Implantable Medical Devices (AIMDs)  
AIMDs are outside the scope of 60601-1-2. However, for AIMD systems, we recommend 
that the non-implantable subsystems (e.g., pacemaker programmer) be tested to 
consensus standards appropriate for non-implantable devices (e.g., 60601-1-2). 
Consensus standards such as ISO 14117 Active implantable medical devices -- 
Electromagnetic compatibility -- EMC test protocols for implantable cardiac 
pacemakers, implantable cardioverter defibrillators, and cardiac resynchronization 
devices and the ISO 14708 series are often referenced to address EMC for AIMDs.  
 
EMC consensus standards for AIMDs focus on EM phenomena to address the immunity 
of the medical device. The ISO 14708 Series and ISO 14117 standards assess AIMD 
 
18 Basic Safety is defined in ANSI/AAMI/ES 60601-1:2005 as “freedom from unacceptable RISK directly caused by 
physical HAZARDS when ME EQUIPMENT is used under NORMAL CONDITION and SINGLE FAULT CONDITION.”

---

<!-- Page 11 -->
Contains Nonbinding Recommendations 
 
 
11 
 
performance when exposed to commonly encountered EM sources as well as particular 
sources that an implantable device is likely to encounter. For example, cardiac 
implantable electronic device consensus standards (e.g., ISO 14117) include immunity 
testing for exposure to defibrillation devices, which inject high-energy electrical signals 
into the heart for life-saving functions.  
(3) Special Environments 
It is important to understand the scope and limitations of each standard. For example, 
60601-1-2 is generally applicable to both the home healthcare environment and the 
professional healthcare facility environment. However, if a medical device is intended to 
be used in a special environment, we recommend that you provide additional EMC 
information and perform testing for the given special environment. This could be 
achieved by referencing appropriate standards for each special environment. For 
example, we recommend immunity testing to RTCA DO-160 Environmental Conditions 
and Test Procedures for Airborne Equipment for non-implantable medical devices that 
are intended or expected to be used in an aircraft environment. Note that some AIMD 
consensus standards do not specify EMC test parameters for use in a magnetic resonance 
imaging (MRI) environment (e.g., exposure within the bore of an MRI system). Where an 
applicable AIMD standard does not specify such requirements, we recommend test 
methods specific to this potentially high-risk environment, such as those described in 
ISO/TS 10974 Assessment of the safety of magnetic resonance imaging for patients with 
an active implantable medical device.  
 
 
Essential Performance and Immunity Pass/Fail Criteria 
We recommend that you provide clear immunity pass/fail criteria, and, if applicable, a 
clear statement of the device’s Essential Performance. The Essential Performance and 
immunity pass/fail criteria are fundamental to performing and assessing the adequacy of 
EMC testing to demonstrate that the medical device is safe and performs as intended. 
(1) Essential Performance 
Essential Performance is defined in ANSI/AAMI/ES 60601-1:2005 as “performance of a 
clinical function, other than that related to Basic Safety, where loss or degradation 
beyond the limits specified by the manufacturer results in an unacceptable risk. Note: 
Essential Performance is most easily understood by considering whether its absence or 
degradation would result in an unacceptable risk.” If you reference 60601-1-2, 60601-2-
X, or 80601-2-X, you should specify the Essential Performance of the medical device. 
Essential Performance should be specific to each medical device and be determined by 
you by assessing the risk to the patient. The Essential Performance should be determined 
by:  
 
• identifying the performance of the clinical functions,  
• specifying performance limits for fully functional performance versus loss or 
degradation of the identified performance, and

---

<!-- Page 12 -->
Contains Nonbinding Recommendations 
 
 
12 
 
• evaluating the risk from the loss, disruption, deviation, degradation, or over-delivery 
of the identified performance.  
 
If the resulting risk is determined to be unacceptable, then the identified performance is 
Essential Performance.  
 
It is also possible for a medical device to have no Essential Performance. A determination 
of no Essential Performance should be accompanied by scientific justification and risk 
analysis. Even for medical devices that have no Essential Performance, appropriate 
immunity pass/fail criteria should be used to demonstrate that the device is safe and 
performs as intended.  
 
See informative annex “General guidance and rationale” of ANSI/AAMI ES 60601-1 and 
Clause 2.3.4 of AAMI CR500:2019 Basic Introduction to the IEC 60601 Series for 
additional information regarding Essential Performance. 
(2) Immunity Pass/Fail Criteria 
Immunity pass/fail criteria should address the degradation of the medical device’s 
functions caused by the test disturbance. Your EMC test plan should specify which 
degradations are considered acceptable. Acceptance criteria should be documented in the 
EMC test plan prior to testing.  We recommend that you specify detailed immunity 
pass/fail criteria that are (1) quantitative, (2) specific to the medical device and functions, 
and (3) observable. These criteria should be determined based on the medical device’s 
functions, modes, indications for use, intended use, and Essential Performance (if 
applicable). If a medical device has multiple medical device subsystems (e.g., an AIMD 
with active external parts) or more than one function (e.g., a ventilator with physiological 
monitoring), then each medical device subsystem or function can have specific immunity 
pass/fail criteria. We recommend that you specify how the immunity pass/fail criteria 
were derived, quantified, and monitored, and justify how they demonstrate that the 
medical device remains safe and performs as intended.  
 
Immunity pass/fail criteria can be different for transient EM phenomena and for 
continuous EM phenomena. Transient phenomena include ESD, electrical fast 
transients/bursts, surges, and voltage dips and interruptions. Continuous phenomena 
include conducted and radiated RF disturbances and power-frequency magnetic fields. 
For transient phenomena, it might be acceptable that the medical device provides the 
specified performance after application of the test disturbance. A recovery time can be 
acceptable and should be specified based on the risk analysis. For continuous phenomena, 
the medical device should provide the specified performance during and after application 
of the test disturbance. 
 
Some EMC test standards list general examples of immunity pass/fail criteria for a 
medical device or general descriptions of immunity pass/fail criteria (e.g., Performance 
Criterion A, Operates as Intended). However, these general immunity pass/fail criteria are 
not sufficiently specific to the medical device’s functions, modes, indications for use, 
intended use, and Essential Performance (if applicable). Even devices with the same

---

<!-- Page 13 -->
Contains Nonbinding Recommendations 
 
 
13 
 
hardware could have different immunity pass/fail criteria. For example, immunity 
pass/fail criteria for a ventilator for adult patients would be expected to be different from 
that for neonatal patients because of the different physiological characteristics of the 
intended use populations.  
 
If a submission references a standard in the 60601 family of standards, then the immunity 
pass/fail criteria should address both Basic Safety and Essential Performance. Many 
particular standards (e.g., 60601-2-X) specify the Essential Performance and some 
specify immunity pass/fail criteria. As noted in subsection C(1) above, the scope of 
60601 standards is limited to safety (i.e., Basic Safety and Essential Performance). 
Therefore, we recommend that the immunity pass/fail criteria include considerations to 
demonstrate that the device performs as intended. We recommend conforming to IEC TR 
60601-4-2 Medical electrical equipment - Part 4-2: Guidance and interpretation - 
Electromagnetic immunity: performance of medical electrical equipment and medical 
electrical systems to assess the immunity of the performance associated with the intended 
use because the test methods are similar to 60601-1-2 and can be tested at the same time. 
 
See IEC 60601-1-2 informative annex “Identification of IMMUNITY pass/fail criteria” 
for additional information and examples on determination of specific immunity pass/fail 
criteria.  
 
Medical Device Configuration and Functions Tested 
We recommend that you provide a detailed description of the medical device under test, 
including the configuration, functions, modes, and settings that were tested. We 
recommend testing functions and modes that include a feature or control such that the 
failure or malfunction would most likely result in an unacceptable risk or to not achieve 
its intended use. The description of the device under test should include the medical 
device name, model number, manufacturer, and an indication of whether the device is the 
final production-ready medical device currently under review.  
 
We recommend you perform testing on the final finished device. If the device tested is 
not the final finished device, the description of the device under test should include an 
explanation and a scientific justification of how test results are applicable to the final 
finished device. When leveraging EMC test results from a prior or different medical 
device model/version to another model/version, we recommend that you: 
 
• identify and summarize all modifications or changes from the previously tested 
medical device and include any changes in the medical device’s indications, intended 
use, and intended use environments, 
• provide an analysis of whether each modification could affect EMC of the medical 
device, and 
• assess whether the consensus standard used for the prior EMC testing has been 
superseded/replaced by a revised version. 
 
New EMC testing should be performed if any of the analyses of the device differences 
indicate that the prior testing might not support the EMC of the updated medical device

---

<!-- Page 14 -->
Contains Nonbinding Recommendations 
 
 
14 
 
model/version. We also recommend applying these considerations when you perform 
EMC testing on only a subset of models within a product family. 
 
We recommend that you consider the following to help determine the appropriate device 
configuration(s) for testing: 
 
• The device should be tested as a system with all medical device accessories, 
components, and subsystems connected and functioning as intended. If non-medical 
equipment is used in a medical system and could affect the ability of the medical 
device to meet the immunity pass/fail criteria, the non-medical equipment should also 
be tested as part of the medical device system. Examples of non-medical equipment 
include mobile phones, tablets, and computers. Any non-medical equipment, medical 
device accessories, or subsystems not included in the EMC test should be listed with 
a rationale for why they were not tested. You should provide a scientific justification 
for how the test configuration demonstrates EMC of the entire medical device system.  
• If a medical device has multiple subsystems or accessories (e.g., a left ventricular 
assist device (LVAD) that includes an implantable blood pump and external 
controller), or more than one function (e.g., a ventilator with physiological 
monitoring), then the medical device system test specifications should consider all 
EMC-related consensus standards applicable to those subsystems, accessories, and 
functions.  This can be used to formulate an appropriate superset of test 
specifications. 
• If EMC testing is performed on a subsystem basis, each subsystem not included in the 
testing should be simulated, including any potential third-party medical devices or 
connections. 
• Medical device and test or ancillary equipment should be configured in the modes 
and with settings considered to be representative of the medical device’s intended 
use. For example, a medical device that can operate in battery power mode and in 
mains power mode should be tested in both modes. Additionally, batteries with 
embedded electronic circuitry (i.e., smart batteries) that are intended to be handled by 
the user should be removed from the medical device and tested separately for 
immunity to ESD due to the potential of ESD damaging the circuitry of the battery. 
• Patient simulators should be used where specified by the referenced EMC consensus 
standards or as appropriate for the medical device. For example, certain EMC test 
methods for AIMDs specify that the medical device be submerged in a saline 
phantom with specific conductivity. Other consensus standards such as 60601-1-2 
specify that patient coupled medical devices be electrically loaded in a way that 
simulates a patient and be provided with electrical or mechanical signals that simulate 
a patient.  
• If wireless technology is used in the medical device to achieve its intended use, the 
wireless technology should be “on” and communicating with other medical device 
subsystems or ancillary equipment during EMC testing. This is important because 
having active connections at each antenna could affect whether the subject medical 
device operates as intended when exposed to EM disturbances.

---

<!-- Page 15 -->
Contains Nonbinding Recommendations 
 
 
15 
 
You should also include a description of how the medical device was monitored during 
EMC testing. Monitoring methods should include a means to quantitatively observe 
performance associated with the immunity pass/fail criteria without significant 
perturbation or effect on the test being performed or to the device under test.  
 
Results of EMC Testing 
We recommend that you provide a summary of EMC testing. This information should 
summarize the medical device emissions and the immunity to EM disturbances at test 
levels appropriate for the medical device’s intended use environments. If neither the test 
methods nor the acceptance criteria are well-defined in the EMC consensus standard(s), 
we recommend that information requested in this guidance be supported by the inclusion 
of EMC test reports.19 We recommend that the summary of EMC testing include the 
following: 
 
• Name and location of the test facility, the date of the testing.  
• Results for each emissions test. Pass/Fail criteria should be expressed in terms of 
limits, against which the medical device’s measured emissions are compared and 
should not exceed.  
• Results for each immunity test performed (e.g., ESD, voltage dips, radiated 
immunity). This should include any degradations that were observed during and after 
each immunity test for continuous phenomena and after each immunity test for 
transient phenomena. For all degradations, you should detail how the medical device 
continued to meet the immunity pass/fail criteria and if any additional mitigations will 
be implemented. 
 
Allowances 
Allowances are specifications within a consensus standard that permit well-defined or 
conditional variations of, or exemptions from, certain requirements of the standard. In 
general, an allowance of a standard can include the test setup, test methodology, 
immunity test levels, or immunity test modulations. For example, a consensus standard 
might provide an exemption from certain immunity and emissions tests that are 
applicable for permanently installed large medical electrical equipment or medical 
electrical systems with a rated input current more than 16 A per phase. We recommend 
that you provide a description of all allowances used, with a justification to support the 
use of each allowance. The allowance should only be used if all the specified conditions 
of the allowance are satisfied. The use of allowances should not increase risks to patients 
or operators. If the conditions for use of an allowance cannot be justified, then the 
allowance should not be used.   
 
Deviations 
A deviation from a consensus standard is when a requirement of the consensus standard 
is intentionally not satisfied, or testing is performed in an alternative way other than that 
 
19 https://www.fda.gov/regulatory-information/search-fda-guidance-documents/appropriate-use-voluntary-
consensus-standards-premarket-submissions-medical-devices

---

<!-- Page 16 -->
Contains Nonbinding Recommendations 
 
 
16 
 
specified and allowed in the standard. The difference between a deviation and an 
allowance is that an allowance is specified in a standard, whereas a deviation is not. We 
recommend that you provide a description of all deviations used along with a justification 
to support the use of each deviation. Deviations from a referenced consensus standard 
should be supported with a justification that explains how the deviation would not 
adversely impact the safety or performance of the medical device.  
 
Modifications 
If the device was modified or altered to pass the EMC testing, such as after initial EMC 
test failure, then we recommend that you include a description and analysis of those 
medical device modifications. Many types of modifications can alter medical device 
EMC, including hardware, software, firmware, and even cosmetic changes (e.g., use of a 
metallic material for labeling where the prior labeling was non-conductive). Some 
common device modifications made to pass EMC testing include incorporating ferrite 
beads, adding filters or EMC shielding materials, and changes or updates to firmware or 
software. When a medical device is modified to pass EMC testing, we recommend the 
following information be provided: 
 
• A description of all changes or modifications that were made to the medical device in 
order to pass EMC testing. 
• A statement whether the provided EMC test results occurred before or after the 
modifications were incorporated into the medical device. If EMC testing was not 
performed after the modifications were made to the medical device, a risk analysis 
and scientific justification should be provided that the modified medical device does 
not adversely impact the safety or performance of the medical device. 
• A statement indicating that the changes will be incorporated into the final finished 
medical device prior to marketing; the changes must be documented in the design 
history file in accordance with design controls.20 
• An analysis as to whether these modifications might impact other aspects of the 
medical device safety or performance, such as whether they increase risks to patients 
or operators, alter the biocompatibility or sterility, affect electrical safety, or introduce 
software anomalies/defects. 
 
Common Electromagnetic (EM) Emitters 
Certain emitters commonly found in some use environments might not be adequately 
addressed by FDA-recognized consensus standards. This could be because a consensus 
standard specifies a range of frequencies that omits some bands, such as emitters in the 
kHz range, or it could be because a technology is adopted so quickly that consensus 
standards cannot keep up with the rapidly changing EM environment. You should be 
familiar with their intended use environments and reasonably foresee the potential for 
interference from emitters commonly found in those environments.  
 
At the time of publication of this guidance, some examples of common EM emitters not 
adequately addressed by FDA-recognized consensus standards are radiofrequency 
 
20 21 CFR 820.30

---

<!-- Page 17 -->
Contains Nonbinding Recommendations 
 
 
17 
 
identification (RFID) readers, electronic security systems (e.g., metal detectors, electronic 
article surveillance), near-field communications (NFC) systems, wireless power transfer 
(WPT), Cellular 5G, and unique medical emitters such as electrocautery, MRI, 
electrosurgical units, and diathermy equipment. The EM disturbances caused by these 
emitters should be taken into account during the risk management process. 
 
We recommend mitigating the risks associated with these common EM emitters and 
unique medical emitters based on the intended use environments and the potential 
severity of harm the medical device could cause (see Section IV.B above). For medical 
devices in the risk category “Medical device-related events without reported or potential 
harm,” we recommend that the medical device labeling (e.g., user manual, instructions 
for use) mention the potential for EMI from emitters expected to be nearby. If you make 
specific claims or specify a specific intended use regarding any particular emitter, we 
recommend that those claims be supported with additional testing, engineering analysis, 
or computer modeling.  For medical devices in the risk category “Medical device-related 
deaths and serious injuries” or “Medical device-related non-serious adverse events” we 
recommend that: 
 
• testing be performed according to FDA-recognized consensus standards (e.g., FDA-
recognized AIM 7351731 Medical Electrical Equipment and System Electromagnetic 
Immunity Test for Exposure to Radio Frequency Identification Readers - An AIM 
Standard or IEC 60601-1-2:2020 Clause 8.11 for RFID emitters), or equivalent EMC 
test methods, with justification. If no consensus standards exist, specific immunity 
testing should be performed to demonstrate that the medical device is safe with regard 
to each identified emitter that is foreseeable in the intended use environment; and 
 
• labeling be specific to the risks to patients and operators and include any mitigations 
and warnings needed, based on the test results. 
 
Labeling 
It is important to include EMC-related information in the labeling because EMC testing 
alone may be insufficient to mitigate the risk associated with use in all environments. For 
example, EMC specifications in the labeling can help end users select equipment with 
electromagnetic immunity that is compatible with the environments in which the device 
is intended to be used, or to compare EMC characteristics of candidate equipment prior to 
purchase. Providing EMC information in the labeling (e.g., instructions for use) can help 
make users aware of the degradations that can be caused by EMI and to understand the 
circumstances to avoid. We recommend that the submission include EMC information to 
be included in the labeling to enable safe and effective installation and use of the medical 
device in the intended EM environments over the expected service life. EMC-related 
information can be presented as physical markings on the medical device related to EMC, 
or in accompanying documents, such as instructions for use, user manual, and/or 
technical and service manuals. The EMC-information included in the labeling should 
meet the specifications of the referenced medical device consensus standards (e.g.,

---

<!-- Page 18 -->
Contains Nonbinding Recommendations 
 
 
18 
 
60601-1-2, 60601-4-2).21 We recommend that the medical device labeling include the 
following information related to EMC: 
 
• The environments of use for which the medical device is suitable to be used/exposed. 
• Accessories and other equipment with which the device has been determined to be 
compatible. 
• The medical device’s functions/performance and a description of what the operator 
can expect if the functions/performance are lost or degraded due to EM disturbances. 
For 60601-4-2, these are the functions/performance needed to demonstrate the 
medical device performs as intended, and for all other 60601 standards this is Basic 
Safety and Essential Performance. 
• The compliance level for each emissions and immunity test. 
• The use of any deviations from, or allowances specified by, the referenced standards. 
• Precautions regarding sources of EM energy that: 
• emit levels of EM energy that exceed the immunity test levels of the referenced 
EMC standards used, or 
• have other emission characteristics to which the medical device has not been 
tested for immunity.  
• Specifications of the wireless communication for medical devices with RF wireless 
functions. 
• Any maintenance instructions needed to ensure that the medical device remains safe 
and performs as intended with regard to EM disturbances throughout the expected 
service life. 
• Markings affixed to the medical device and warnings for certain types of known EM 
environments, such as in or near an MRI scanner. Medical devices intended for use in 
the MR environment that have not been shown to be MR Safe or MR Conditional 
should be marked with the ASTM F2503 symbol for MR Unsafe. (See ASTM F2503-
13 Standard Practice for Marking Medical Devices and Other Items for Safety in the 
Magnetic Resonance Environment.) 
• The FCC term “harmful interference” has a meaning that is different from that of the 
term “harm” as used in medical device risk management and ANSI/AAMI/ISO 14971 
Medical devices - Application of risk management to medical devices. To avoid 
confusion and concern regarding the FCC term, we recommend adding the note 
specified below after the FCC warning in the labeling:  
• NOTE: “Harmful interference” is defined in 47 CFR §2.122 by the FCC as 
follows: Interference which endangers the functioning of a radionavigation 
service or of other safety services or seriously degrades, obstructs, or repeatedly 
interrupts a radio communication service operating in accordance with the [ITU] 
Radio Regulations. 
 
21 The labeling specifications of IEC 60601-1-2:2020 and IEC TR 60601-4-2:2016 are in Clause 5 and summarized 
in Annex B. 
22 Available at https://www.govinfo.gov/content/pkg/CFR-2018-title47-vol1/xml/CFR-2018-title47-vol1-sec2-1.xml

---

<!-- Page 19 -->
Contains Nonbinding Recommendations 
 
 
19 
 
V. EMC Information to Support Investigational Device 
Exemption (IDE) or Investigational New Drug (IND) 
Submissions 
 
When evaluating EMC of a medical device in an IDE or IND submission, we recommend that 
you consider all applicable points detailed in Section IV of this guidance that are applicable to 
patient and operator safety. We recognize that there are often iterations to the design of the 
medical device during a clinical study, and thus comprehensive EMC testing to consensus 
standards might not be the least burdensome approach to demonstrate EMC. Other appropriate 
EMC mitigations can be used to support a favorable benefit/risk determination.23 If immunity 
testing has not been performed using appropriate consensus standards (see Section IV.C) for the 
medical device under study, you should provide in the IDE or IND submission, a description of 
alternative mitigations, such as ad-hoc testing and a list of labeling mitigations (e.g., continuous 
oversight from medical professionals, procedures to prevent harm to operators, ESD mitigation 
precautions) along with an explanation of how the mitigations protect the safety of patients and 
operators. If emissions testing has not been performed for the medical device under study per 
appropriate consensus standards, then you should provide in the IDE or IND submission a 
description of potential risks to patients and operators in case the subject medical device 
introduces excessive emissions that might interfere with other medical or non-medical 
equipment.  This should include a justification about how each risk will be mitigated. 
 
23 For more information see the FDA guidance “Factors to Consider When Making Benefit-Risk Determinations for 
Medical Device Investigational Device Exemptions” at https://www.fda.gov/regulatory-information/search-fda-
guidance-documents/factors-consider-when-making-benefit-risk-determinations-medical-device-investigational-
device

---

<!-- Page 20 -->
Contains Nonbinding Recommendations 
 
 
20 
 
Appendix A – Examples of Typical Medical Device Locations within Intended Use 
Environments24 
 
Professional Healthcare 
Facility Environment 
Home Healthcare Environment 
Special Environment 
• Physician offices 
• Outpatient facilities a) 
• Dental offices 
• Clinics 
• Nursing homes b) 
• Hospital facilities including 
emergency rooms, patient 
rooms, intensive care, 
surgery rooms, etc., (except 
areas with high-powered 
medical equipment) 
• Limited care facilities 
• Surgical centers 
• Birthing centers 
• Laboratories c) 
• Personal residences 
• Dormitories 
• Independent living retirement 
homes 
• Restaurants and cafes 
• Shops, stores, markets 
• Cars, buses, trains, boats, 
ambulances d) 
• Office buildings 
• Schools 
• Churches 
• Libraries 
• Theaters and stadiums 
• Outdoor environments (e.g., 
streets, sidewalks, parks)  
• Medical treatment areas with high-
powered medical equipment  
o (e.g., high-frequency surgical 
equipment, short-wave therapy 
equipment, inside the RF 
shielded room of an MRI 
system) 
• Military areas (e.g., submarines, 
radar installations, weapons 
control systems) 
• Heavy industrial areas (e.g., power 
plants, steel and paper mills, 
foundries, automotive and 
appliance manufacturing, smelting 
and mining operations, oil and gas 
refineries) 
• Aircraft environments (e.g., 
planes, helicopters) e) 
 
a) Facilities where outpatient services, i.e., medical procedures or tests that can be performed without an overnight 
stay, can be performed (e.g., medical center, rehabilitation center).  
b) Refer to the SIS for the scope of FDA’s recognition of IEC 60601-1-11 Medical electrical equipment - Part 1-11: 
General requirements for basic safety and essential performance - Collateral Standard: Requirements for medical 
electrical equipment and medical electrical systems used in the home healthcare environment.  The FDA considers 
nursing homes in the United States to be Professional Healthcare Facilities because professionals with medical 
training are available when patients are present.25 
c) Laboratories have operators with medical training or operators without medical training. For the purpose of this 
guidance, we include laboratories under the Professional Healthcare Facility Environment in either case. This is 
because, in the latter case, there are generally no patients. According to IEC 60601-1-11, a patient is necessary to be 
included in the Home Healthcare Environment.   
d) Although healthcare professionals are present in an ambulance, the EM environment is similar to that of the 
Home Healthcare Environment. 
e) IEC 60601-1-2 includes aircraft in the Home Healthcare Environment while referencing RTCA DO-160G for 
higher immunity test levels. Since the test levels are potentially different than the Home Healthcare Environment, 
aircraft is included in the Special Environment (see Section IV.C(3)for more details). 
 
  
 
24 Adapted from IEC 60601-1-2 with modification 
25 See definitions from FDA Guidance, “Design Considerations for Devices Intended for Home Use,” available at 
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-considerations-devices-
intended-home-use.
