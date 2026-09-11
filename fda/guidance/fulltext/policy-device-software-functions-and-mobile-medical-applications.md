# Policy for Device Software Functions and Mobile Medical Applications: Guidance for Industry and Food and Drug Administration Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/policy-device-software-functions-and-mobile-medical-applications](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/policy-device-software-functions-and-mobile-medical-applications)

**Published:** 2022-09-28

---

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
Policy for Device Software Functions 
and Mobile Medical Applications
Guidance for Industry and
Food and Drug Administration Staff
Document issued on September 28, 2022.
Document originally issued on September 25, 2013.
This document supersedes “Policy for Device Software Functions and Mobile 
Medical Apps” issued September 27, 2019.
For questions about this document regarding CDRH-regulated devices, contact the Digital Health 
Center of Excellence by e-mail at digitalhealth@fda.hhs.gov. 
For questions about this document regarding CBER-regulated devices, contact the Office of 
Communication, Outreach, and Development (OCOD) at 1-800-835-4709 or 240-402-8010, or 
by email at ocod@fda.hhs.gov.
U.S. Department of Health and Human Services
Food and Drug Administration
Center for Devices and Radiological Health
Center for Biologics Evaluation and Research

---

<!-- Page 3 -->
Contains Nonbinding Recommendations
Preface
Public Comment
You may submit electronic comments and suggestions at any time for Agency consideration to 
https://www.regulations.gov. Submit written comments to the Dockets Management Staff, Food 
and Drug Administration, 5630 Fishers Lane, Room 1061, (HFA-305), Rockville, MD 20852. 
Identify all comments with the docket number FDA-2011-D-0530. Comments may not be acted 
upon by the Agency until the document is next revised or updated. 
Additional Copies
CDRH
Additional copies are available from the Internet. You may also send an email request to CDRH-
Guidance@fda.hhs.gov to receive a copy of the guidance. Please use the document number 1741 
and complete title of the guidance in the request.
CBER
Additional copies are available from the Center for Biologics Evaluation and Research (CBER), 
Office of Communication, Outreach, and Development (OCOD), 10903 New Hampshire Ave., 
WO71, Room 3128, Silver Spring, MD 20903, or by calling 1-800-835-4709 or 240-402-8010, 
by email, ocod@fda.hhs.gov, or from the Internet at 
https://www.fda.gov/vaccines-blood-biologics/guidance-compliance-regulatory-information-
biologics/biologics-guidances.

---

<!-- Page 4 -->
Contains Nonbinding Recommendations
Table of Contents
I. Introduction ......................................................................................................................... 1 
II. Background ......................................................................................................................... 3
III. Definitions........................................................................................................................... 5
A. Mobile Platform ............................................................................................................... 5
B. Mobile Application (Mobile App) ................................................................................... 5
C. Mobile Medical Application (Mobile Medical App) ....................................................... 5
D. Regulated Medical Device ............................................................................................... 7
E. Mobile Medical App Manufacturer ................................................................................. 7
IV. Scope ................................................................................................................................. 10
V. Regulatory Approach for Device Software Functions ...................................................... 10
A. Device software functions: Subset of software functions that are the focus of FDA’s 
regulatory oversight ............................................................................................................ 11
B. Software functions for which FDA intends to exercise enforcement discretion (meaning 
that FDA does not intend to enforce requirements under the FD&C Act) ......................... 13
VI. Regulatory Requirements.................................................................................................. 15
Appendix A  Examples of Software Functions that are NOT Medical Devices .................... 17
Appendix B  Examples of Software Functions for which FDA intends to exercise enforcement 
discretion ................................................................................................................................. 24
Appendix C  Examples of Software Functions that are the focus of FDA’s regulatory oversight 
(Device Software Functions and Mobile Medical Apps) ....................................................... 26
Appendix D  Brief description of certain device regulatory requirements ............................. 30
Appendix E  Frequently Asked Questions (FAQs)................................................................. 35
Appendix F  Additional Resources ......................................................................................... 40
A. Guidance Documents ..................................................................................................... 40
B. Standards ........................................................................................................................ 40

---

<!-- Page 5 -->
Contains Nonbinding Recommendations
1
Policy for Device Software Functions 
and Mobile Medical Applications
Guidance for Industry and
Food and Drug Administration Staff
This guidance represents the current thinking of the Food and Drug Administration (FDA 
or Agency) on this topic.  It does not establish any rights for any person and is not binding 
on FDA or the public.  You can use an alternative approach if it satisfies the requirements 
of the applicable statutes and regulations.  To discuss an alternative approach, contact the 
FDA staff or Office responsible for this guidance as listed on the title page. 
I. 
Introduction
The Food and Drug Administration (FDA) recognizes the advances in software functionality, 
the rapid pace of innovation, and their potential benefits and risks to public health. FDA is 
issuing this guidance document to inform manufacturers, distributors, and other entities about 
how FDA intends to apply its regulatory authorities to select software functions intended for 
use on mobile platforms (mobile applications or “mobile apps”) or on general-purpose 
computing platforms. Given the rapid expansion and broad applicability of software 
functions deployed on mobile or other general-purpose computing platforms, FDA is issuing 
this guidance document to clarify the subset of software functions to which FDA intends to 
apply its authority.
FDA refers to software functions that are device functions as “device software functions.”  
Device software functions may include “Software as a Medical Device (SaMD)” and 
“Software in a Medical Device (SiMD).”1, 2 Software functions that meet the definition of a 
device may be deployed on mobile platforms, other general-purpose computing platforms, or 
in the function or control of a hardware device. If a software function that meets the 
definition of a device is deployed on a mobile platform, it may be referred to as a “mobile 
medical app.” The policies described in this guidance are independent of the platform on 
which they might run, are function-specific, and apply across platforms. Therefore, the 
policies described using terms such as “mobile medical apps,” “mobile medical app 
manufacturers,” “device software functions,” and “device software function manufacturers”
1 See the FDA website on “Software as a Medical Device (SaMD),” available at https://www.fda.gov/medical-
devices/digital-health/software-medical-device-samd.
2 See the International Medical Device Regulators Forum final document, “Software as a Medical Device 
(SaMD): Key Definitions,” available at http://www.imdrf.org/docs/imdrf/final/technical/imdrf-tech-131209-
samd-key-definitions-140901.pdf.

---

<!-- Page 6 -->
Contains Nonbinding Recommendations
2
are not specific to whether the function is deployed on a mobile platform or other general 
purpose-computing platform.
Many software functions are not medical devices (meaning such software functions do not 
meet the definition of a device under section 201(h) of the Federal Food, Drug, and Cosmetic 
Act (FD&C Act)), and FDA does not regulate them as devices. Some software functions may 
meet the definition of a medical device, but because they pose a lower risk to the public, 
FDA intends to exercise enforcement discretion over these devices (meaning it does not, at 
this time, intend to enforce requirements under the FD&C Act).
Consistent with FDA’s existing oversight approach that considers functionality of the 
software rather than platform, FDA intends to apply its regulatory oversight to only those 
software functions that are medical devices and whose functionality could pose a risk to a 
patient’s safety if the device were to not function as intended. 
FDA is issuing this guidance to provide clarity and predictability for software manufacturers. 
This document was previously updated to be consistent with the guidance “Medical Device 
Data Systems, Medical Image Storage Devices, and Medical Image Communications 
Devices,” originally issued on February 9, 2015.3 This guidance was also updated on 
September 27, 2019, to be consistent with section 3060(a) of the 21st Century Cures Act 
(Cures Act), which amended section 520 of the FD&C Act, removing certain software 
functions from the definition of device in section 201(h) of the FD&C Act. The guidance was 
minorly updated in accordance with the changes described in the guidance “Changes to 
Existing Medical Software Policies Resulting from Section 3060 of the 21st Century Cures 
Act.”4 Examples of mobile apps and software on the FDA website5 (that were added after 
September 25, 2013) were incorporated into the appropriate appendices of this document for 
consistency. This guidance also is now being minorly updated to reflect the issuance of the 
final rule, “Medical Devices; Medical Device Classification Regulations To Conform to 
Medical Software Provisions in the 21st Century Cures Act” (86 FR 20278)6 and the 
guidance  “Clinical Decision Support Software” (referred to as CDS guidance throughout the 
rest of this document) issued on September 28, 20227 in this latest revision.
For the current edition of FDA-recognized standard(s) referenced in this document, see the 
“FDA Recognized Consensus Standards Database.”8 For more information regarding use of 
consensus standards in regulatory submissions, please refer to the FDA guidances titled 
“Appropriate Use of Voluntary Consensus Standards in Premarket Submissions for Medical 
3 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-
data-systems-medical-image-storage-devices-and-medical-image-communications-devices.
4 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/changes-existing-
medical-software-policies-resulting-section-3060-21st-century-cures-act.
5 Available at https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-
applications/examples-premarket-submissions-include-mmas-cleared-or-approved-fda 
6 See 86 FR 20278 at https://www.federalregister.gov/documents/2021/04/19/2021-07860/medical-devices-
medical-device-classification-regulations-to-conform-to-medical-software-provisions.
7 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-
support-software 
8 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm.

---

<!-- Page 7 -->
Contains Nonbinding Recommendations
3
Devices”9 and “Standards Development and the Use of Standards in Regulatory Submissions 
Reviewed in the Center for Biologics Evaluation and Research.”10
In general, FDA’s guidance documents do not establish legally enforceable responsibilities. 
Instead, guidances describe the Agency’s current thinking on a topic and should be viewed 
only as recommendations, unless specific regulatory or statutory requirements are cited. The 
use of the word should in Agency guidances means that something is suggested or 
recommended, but not required.
II. Background
As mobile platforms become more user friendly, computationally powerful, and readily 
available, innovators have begun to develop mobile apps of increasing complexity to 
leverage the portability mobile platforms can offer. Some of these new software functions are 
specifically targeted to assist individuals in their own health and wellness management. 
Other software functions are targeted to health care professionals as tools to improve and 
facilitate the delivery of patient care.11
In 1989, FDA prepared a general policy statement on how it planned to determine whether a 
computer-based product and/or software-based product is a device, and, if so, how FDA 
intended to regulate it. The document, “FDA Policy for the Regulation of Computer 
Products,” became known as the “Draft Software Policy.” After 1989, however, the use of 
computer and software products as medical devices grew exponentially and the types of 
products diversified and grew more complex (and that trend has continued). As a result, FDA 
determined that the draft policy did not adequately address all of the issues related to the 
regulation of all medical devices containing software. Therefore, in 2005, the Draft Software 
Policy was withdrawn.12
Although FDA has not issued an overarching software policy, the Agency has formally 
classified certain types of software applications that meet the definition of a device and, 
through classification, identified specific regulatory requirements that apply to these devices 
and their manufacturers. These software devices include products that feature one or more 
software components, parts, or accessories, as well as devices that are composed solely of 
software. 
9 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/appropriate-use-
voluntary-consensus-standards-premarket-submissions-medical-devices.
10 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/standards-
development-and-use-standards-regulatory-submissions-reviewed-center-biologics-evaluation. 
11 For the purposes of this guidance, FDA uses the term health care professional to mean an individual who is 
licensed, registered, or certified by a State, territory, or other governing body, to administer health care, 
including but not limited to, nurse practitioner, registered nurse, licensed practical nurse, clinical social worker, 
dentist, occupational therapist, pharmacist, physical therapist, physician, physician assistant, psychologist, 
respiratory therapist, speech-language pathologist, technologist, or any other practitioner or allied health 
professional.
12 Annual Comprehensive List of Guidance Documents at the Food and Drug Administration (70 FR 824 at 
890) (January 5, 2005), available at https://www.federalregister.gov/documents/2005/01/05/05-155/annual-
comprehensive-list-of-guidance-documents-at-the-food-and-drug-administration.

---

<!-- Page 8 -->
Contains Nonbinding Recommendations
4
FDA has previously clarified that when a software application is used to analyze medical 
device data, it has traditionally been regulated as an accessory to a medical device13 or as 
medical device software. In 2014, the International Medical Device Regulators Forum 
established globally harmonized vocabulary for such software applications and defined the 
term “Software as a Medical Device (SaMD).”14
As is the case with traditional medical devices, certain software functions that are device 
functions (referred to in this document as “device software functions”) can pose potential 
risks to public health. Moreover, certain device software functions may pose risks that are 
unique to the characteristics of the platform on which the software function is run. For 
example, the interpretation of radiological images on a mobile device could be adversely 
affected by the smaller screen size, lower contrast ratio, and uncontrolled ambient light of the 
mobile platform. FDA intends to take these risks into account in assessing the appropriate 
regulatory oversight for these products. 
Additionally, the Cures Act, enacted on December 13, 2016, amended section 520 of the 
FD&C Act to remove certain software functions from the definition of device (201(h) of the 
FD&C Act). FDA has published the following guidance documents that help provide clarity 
on the types of software functions that do not meet the definition of device:
·
Changes to Existing Medical Software Policies Resulting from Section 3060 
of the 21st Century Cures Act15
·
Clinical Decision Support Software16
·
Medical Device Data Systems, Medical Image Storage Devices, and Medical 
Image Communications Devices17
·
General Wellness: Policy for Low Risk Devices18
This guidance clarifies and outlines FDA’s current thinking. The Agency will continue to 
evaluate the potential impact these technologies might have on improving health care, 
reducing potential medical mistakes, and protecting patients.
13 See FDA’s guidance “Medical Device Accessories - Describing Accessories and Classification Pathways,” 
available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-
accessories-describing-accessories-and-classification-pathways.
14 See the International Medical Device Regulators Forum final document, “Software as a Medical Device 
(SaMD): Key Definitions,” available at http://www.imdrf.org/docs/imdrf/final/technical/imdrf-tech-131209-
samd-key-definitions-140901.pdf.
15 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/changes-existing-
medical-software-policies-resulting-section-3060-21st-century-cures-act 
16 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-
support-software 
17 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-
data-systems-medical-image-storage-devices-and-medical-image-communications-devices 
18 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-
policy-low-risk-devices

---

<!-- Page 9 -->
Contains Nonbinding Recommendations
5
III. Definitions
A. Mobile Platform
For purposes of this guidance, “mobile platforms” are defined as commercial off-the-shelf 
(COTS) computing platforms, with or without wireless connectivity, that are handheld in 
nature. Examples of these mobile platforms include mobile computers such as smart phones, 
tablet computers, or other portable computers.
B. 
Mobile Application (Mobile App)
For purposes of this guidance, a mobile application or “mobile app” is defined as a software 
application that can be executed (run) on a mobile platform (i.e., a handheld commercial off-
the-shelf computing platform, with or without wireless connectivity), or a web-based 
software application that is tailored to a mobile platform but is executed on a server.
C. Mobile Medical Application (Mobile Medical 
App)
For purposes of this guidance, a “mobile medical app” is a mobile app that incorporates 
device software functionality that meets the definition of a device in section 201(h) of the 
FD&C Act;19 and either is intended:
·
to be used as an accessory to a regulated medical device; or
·
to transform a mobile platform into a regulated medical device.
19 Products that are built with or consist of computer and/or software components or applications are subject to 
regulation as devices when they meet the definition of a device in section 201(h) of the FD&C Act. That 
provision defines a device as “…an instrument, apparatus, implement, machine, contrivance, implant, in vitro 
reagent, or other similar or related article, including any component, part, or accessory”, that is “… intended for 
use in the diagnosis of disease or other conditions, or in the cure, mitigation, treatment, or prevention of disease, 
in man …” or “… intended to affect the structure or any function of the body of man or other animals…” and 
“does not include software functions excluded pursuant to section 520(o)” of the FD&C Act. Thus, software 
applications that run on a desktop computer, laptop computer, remotely on a website or “cloud,” or on a 
handheld computer may be subject to device regulation if they are intended for use in the diagnosis or the cure, 
mitigation, treatment, or prevention of disease, or to affect the structure or any function of the body of man. The 
level of regulatory control necessary to assure safety and effectiveness varies based upon the risk the device 
presents to public health. See Appendix C for examples.

---

<!-- Page 10 -->
Contains Nonbinding Recommendations
6
The intended use of a mobile app determines whether it meets the definition of a “device.” 
As stated in 21 CFR 801.4,20 intended use may be shown by labeling21 claims, advertising 
materials, or oral or written statements by manufacturers or their representatives. When the 
intended use of a mobile app is for the diagnosis of disease or other conditions, or the cure, 
mitigation, treatment, or prevention of disease, or is intended to affect the structure or any 
function of the body of man, the mobile app is a device under section 201(h) of the FD&C 
Act if it is not a software function excluded from the device definition by section 520(o) of 
the FD&C Act.
One example is a mobile app that makes a light emitting diode (LED) operate. If the 
manufacturer intends the system to illuminate objects generally (i.e., without a specific 
medical device intended use), the mobile app would not be considered a medical device. If, 
however, through marketing, labeling, and the circumstances surrounding the distribution, 
the mobile app is promoted by the manufacturer for use as a light source for doctors to 
examine patients, then the intended use of the light source would be similar to a conventional 
device such as an ophthalmoscope.
In general, if a software function is intended for use in performing a medical device function 
(i.e., for diagnosis of disease or other conditions, or the cure, mitigation, treatment, or 
prevention of disease), it is a medical device, regardless of the platform on which it is run. 
For example, mobile apps intended to run on smart phones to analyze and interpret EKG 
waveforms to detect heart function irregularities would be considered similar to software 
running on a desktop computer that serves the same function, which is regulated under 21 
CFR 870.2340 (“Electrocardiograph”). FDA’s oversight approach to software functions is 
focused on their functionality, just as we focus on the functionality of conventional devices. 
Our oversight is not determined by the platform. Under this guidance, FDA would not 
regulate the sale or general/conventional consumer use of smartphones or tablets. FDA’s 
oversight applies to software functions performing medical device functions, such as when a 
mobile medical app or software application transforms a mobile platform or a general 
purpose computing platform into a medical device. However, as previously noted, we intend 
to apply this oversight authority only to those software applications whose functionality 
20 “The words ‘intended uses’ or words of similar import … refer to the objective intent of the persons legally 
responsible for the labeling of devices. The intent is determined by such persons' expressions or may be shown 
by the circumstances surrounding the distribution of the article. This objective intent may, for example, be 
shown by labeling claims, advertising matter, or oral or written statements by such persons or their 
representatives. It may be shown by the circumstances that the article is, with the knowledge of such persons or 
their representatives, offered and used for a purpose for which it is neither labeled nor advertised. The intended 
uses of an article may change after it has been introduced into interstate commerce by its manufacturer. If, for 
example, a packer, distributor, or seller intends an article for different uses than those intended by the person 
from whom he received the devices, such packer, distributor, or seller is required to supply adequate labeling in 
accordance with the new intended uses. But if a manufacturer knows, or has knowledge of facts that would give 
him notice that a device introduced into interstate commerce by him is to be used for conditions, purposes, or 
uses other than the ones for which he offers it, he is required to provide adequate labeling for such a device 
which accords with such other uses to which the article is to be put.” 21 CFR 801.4.
21 “The term ‘labeling’ means all labels and other written, printed, or graphic matter (1) upon any article or any 
of its containers or wrappers, or (2) accompanying such article.” Section 201(m) of the FD&C Act, 21 U.S.C. 
321(m).

---

<!-- Page 11 -->
Contains Nonbinding Recommendations
7
could pose a risk to a patient’s safety if the software applications were to not function as 
intended.
D. Regulated Medical Device
For purposes of this guidance, a “regulated medical device” is defined as a product that meets 
the definition of device in section 201(h) of the FD&C Act and that has been cleared or 
approved by FDA’s review of a premarket submission or otherwise classified by FDA.
This definition can include novel devices, whether or not on a mobile platform, that FDA 
will clear or approve by the review of a premarket submission or otherwise classify. 
Examples of regulated medical devices are identified in Appendix C.
E. 
Mobile Medical App Manufacturer
For purposes of this guidance, a “mobile medical app manufacturer” is any person or entity 
that manufactures mobile medical apps in accordance with the definitions of manufacturer in 
21 CFR Parts 803, 806, 807, and 820.22 A mobile medical app manufacturer may include 
anyone who initiates specifications, designs, labels, or creates a software system or 
application for a regulated medical device in whole or from multiple software components. 
This term does not include persons who exclusively distribute mobile medical apps without 
engaging in manufacturing functions; examples of such distributors may include owners and 
operators of  mobile application stores (“app stores”). Examples of mobile medical app 
manufacturers include any person or entity that:
·
Creates, designs, develops, labels, re-labels, remanufactures, modifies, or creates a 
mobile medical app software system from multiple components. This could include a 
person or entity that creates a mobile medical app by COTS software components and 
markets the product to perform as a mobile medical app;
·
Initiates specifications or requirements for mobile medical apps or procures product 
development/manufacturing services from other individuals or entities (second party) 
for subsequent commercial distribution. For example, when a “developer” (i.e., an 
entity that provides engineering, design, and development services) creates a mobile 
medical app from the specifications that were initiated by the “author,” the “author” 
who initiated and developed specifications for the mobile medical app is considered a 
22 Regulatory definitions of the term “manufacturer” or “manufacture” appear in 21 CFR Parts 803, 806, 807, 
and 820. For example – under FDA’s 21 CFR 807.3(d) – establishment registration and device listing for 
manufacturers and initial importers of devices – “Manufacture, preparation, propagation, compounding, 
assembly, or processing of a device means the making by chemical, physical, biological, or other procedures of 
any article that meets the definition of device in section 201(h) of the act. These terms include the following 
activities: (1) Repackaging or otherwise changing the container, wrapper, or labeling of any device package in 
furtherance of the distribution of the device from the original place of manufacture to the person who makes 
final delivery or sale to the ultimate consumer; (2) Initial importation of devices manufactured in foreign 
establishments; or (3) Initiation of specifications for devices that are manufactured by a second party for 
subsequent commercial distribution by the person initiating specifications.”

---

<!-- Page 12 -->
Contains Nonbinding Recommendations
8
“manufacturer” of the mobile medical app under 21 CFR 803.3. For purposes of this 
guidance, manufacturers of a mobile medical app would include persons or entities 
who are the creators of the original idea (initial specifications) for a mobile medical 
app, unless another entity assumes all responsibility for manufacturing and 
distributing the mobile medical app, in which case that other entity would be the 
“manufacturer.”23 Software “developers” of a mobile medical app that are only 
responsible for performing design and development activities to transform the 
author’s specifications into a mobile medical app would not constitute manufacturers, 
and instead the author would be considered the manufacturer;
·
Creates a mobile medical app and hardware attachments for a mobile platform that 
are intended to be used as a medical device by any combination of the mobile medical 
app, hardware attachments, and the mobile platform;
·
Creates a mobile medical app or a software system that provides users access to the 
medical device function through a website subscription, software as a service,24 or 
other similar means.
In contrast, the following are examples of persons or entities that are NOT considered to be 
mobile medical app manufacturers (i.e., persons not within the definition of manufacturer in 
21 CFR Parts 803, 806, 807, and 820). Because they are not manufacturers, none of the 
persons or entities in these examples would have to register their establishments, list their 
products with FDA,25 or submit a premarket application:
·
Manufacturers or distributors of mobile platforms who solely distribute or market 
their platform and do not intend (by marketing claims – e.g., labeling claims or 
advertising material) the platform to be used for medical device functions. When 
mobile medical apps are run on a mobile platform, the mobile platform is treated as a 
component of the mobile medical app’s intended use.26 Therefore the mobile platform 
manufacturer is exempt from the Quality System regulation and registration and 
listing requirements.27 For example, if it is possible to run mobile medical apps on 
BrandNamePhone but BrandNamePhone is not marketed by BrandNameCompany as 
intended for use as a medical device, then BrandNameCompany would not be 
considered a mobile medical app manufacturer or a medical device manufacturer. 
Also, in this example, the BrandNamePhone sold to consumers would not be 
regulated by FDA as a medical device. FDA does not consider entities that 
exclusively distribute mobile medical apps, such as the owners and operators of app 
stores to be medical device manufacturers based on their ownership of or operation of 
23 See 21 CFR 803.3 (definition of manufacturer) and 21 CFR 807.20(a)(2).
24 By this we mean to include any “server software application” that provides a service to a client software 
application on a mobile platform.
25 See 21 CFR 807.65 and 21 CFR 807.85.
26 See 21 CFR 820.3(c), which defines a component as “any raw material, substance, piece, part, software, 
firmware, labeling, or assembly which is intended to be included as part of the finished, packaged, and labeled 
device.”
27 See 21 CFR 807.65(a) and 21 CFR 820.1(a).

---

<!-- Page 13 -->
Contains Nonbinding Recommendations
9
these app stores. FDA also does not consider mobile platform manufacturers to be 
medical device manufacturers just because their mobile platforms could be used to 
run a mobile medical app regulated by FDA.
·
Third parties who solely provide market access to mobile medical apps (i.e., solely 
distribute mobile apps), but do not engage in any manufacturing functions as defined 
in 21 CFR Parts 803, 806, 807, and 820. Examples of such third parties may include 
owners and operators that are only engaged in providing an app store that allows 
mobile medical app manufacturers to commercially distribute their mobile medical 
apps. 
·
Providers of tools, services, or infrastructure used in the development, distribution, or 
use of a mobile medical app. Examples include providers of internet connectivity 
(i.e., internet service), providers of general-purpose computer or information 
technology, or providers that host the web service for content or software application. 
Other examples of providers of tools, services, or infrastructure include customer 
support services, data center hosting services, cloud hosting services, application 
hosting services, wireless carriers, or providers of software development kits. 
However, a creator of a mobile medical app or a software system that provides users 
access to the medical device function through a website subscription, software as a 
service,28 or other similar means is considered a mobile medical app manufacturer.
·
Licensed practitioners, including physicians, dentists, and optometrists, who 
manufacture a mobile medical app or alter a mobile medical app solely for use in 
their professional practice and do not label or promote their mobile medical apps to 
be generally used by other licensed practitioners or other individuals.29,30 For 
example, if Dr. XYZ, a licensed practitioner, creates a mobile medical app called the 
“XYZ-recorder” that enables attaching an ECG electrode to a smartphone, and 
provides the “XYZ-recorder” to his/her patient to use it to record the patient’s 
electrocardiographic readings for 24 hours, Dr. XYZ is not considered a mobile 
medical app manufacturer. If Dr. XYZ is in a group practice (including a telehealth 
network) and permits other physicians in the practice to provide the XYZ-recorder to 
their patients, Dr. XYZ is not considered a mobile medical apps manufacturer. 
However, if Dr. XYZ, the licensed practitioner, distributes the “XYZ-recorder” and, 
through labeling or promotion intends to make it generally available to or to be 
generally used by other physicians (or other specially qualified persons), Dr. XYZ 
would be considered a mobile medical app manufacturer.
28 As identified in footnote 29, we mean to include any “server software application” that provides a service to a 
client software application on a mobile platform.
29 Section 510(g)(2) of the FD&C Act: – Registration of producers of drugs or devices – Exclusions from 
application of section: “practitioners licensed by law to prescribe or administer drugs or devices and who 
manufacture, prepare, propagate, compound, or process drugs or devices solely for use in the course of their 
professional practice.”
30 See 21 CFR 807.65(d).

---

<!-- Page 14 -->
Contains Nonbinding Recommendations
10
·
Persons who manufacture mobile medical apps solely for use in research, teaching, or 
analysis and do not introduce such devices into commercial distribution. We note that 
while persons conducting research using mobile medical apps involving human 
subjects are exempt from registration and listing, they may instead be subject to 
investigational device exemption regulations.31, 32
IV. Scope
This guidance explains FDA’s intentions to focus its oversight on a subset of software 
functions. Mobile medical apps, as defined in Section III, include only those mobile apps that 
meet the definition of a device and either are intended:
·
to be used as an accessory to a regulated medical device; or
·
to transform a mobile platform into a regulated medical device.
Appendix A provides examples of software functions, that do NOT meet the definition of a 
device and, therefore, are NOT device software functions or mobile medical apps for the 
purposes of this guidance.
Section V.B and Appendix B provide examples of software functions, some of which are 
mobile apps, that MAY meet the definition of a device but for which FDA intends to exercise 
enforcement discretion because they pose a low risk to patients.
FDA’s policies regarding accessories to medical devices are not unique to device software 
functions and go beyond the scope of this guidance. Specifically this guidance does not 
address FDA’s general approach for accessories to medical devices which is described in the 
guidance “Medical Device Accessories - Describing Accessories and Classification 
Pathways”.33
Additionally, FDA’s approach to software that performs patient-specific analysis to aid or 
support clinical decision-making, is described in a separate guidance titled “Clinical Decision 
Support Software”.34
If you are developing a software function that meets the definition of a device (such as a 
mobile medical app) with an entirely new intended use, we encourage you to contact FDA to 
discuss what regulatory requirements may apply.
V. Regulatory Approach for Device Software Functions
31 See 21 CFR 807.65(f).
32 See 21 CFR 812.1.
33 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-
accessories-describing-accessories-and-classification-pathways.  
34 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-
support-software

---

<!-- Page 15 -->
Contains Nonbinding Recommendations
11
As described in this guidance, FDA intends to apply its regulatory oversight to only those 
software functions that are medical devices and whose functionality could pose a risk to a 
patient’s safety if the device were to not function as intended. This approach to overseeing 
device software functions is consistent with our existing approach to overseeing medical 
device functionality of a product and the risks it poses to patients regardless of the shape, 
size, or the platform. FDA believes that this subset of device software functions poses the 
same or similar potential risks to the public health as currently regulated devices if they fail 
to function as intended.
FDA strongly recommends that manufacturers of all software functions that may meet the 
definition of a device follow the Quality System35 regulation (that includes good 
manufacturing practices) in the design and development of their device software functions, 
and initiate prompt corrections to their devices, when appropriate, to prevent patient and user 
harm.
For device software functions, manufacturers must meet the requirements associated with the 
applicable device classification. If the device, on its own, falls within a medical device 
classification, its manufacturer is subject to the requirements associated with that 
classification. A device software function, like other devices, may be classified as class I 
(general controls), class II (special controls in addition to general controls), or class III 
(premarket approval).36
A. Device software functions: Subset of software 
functions that are the focus of FDA’s regulatory 
oversight
Software functions may take a number of forms, but it is important to note that FDA intends 
to apply its regulatory oversight to only the subset of software functions identified below and 
in Appendix C. These software functions can transform a general-purpose computing 
platform or mobile platform into a regulated medical device by using attachments, display 
screens, sensors, or other such methods. Regardless of the mechanism behind the 
transformation, FDA considers such software to be device software functions.
The following are software functions that FDA considers to be device software functions 
subject to regulatory oversight:
1. Software functions that are an extension of one or more medical devices by 
connecting37 to such device(s) for purposes of controlling38 the device(s) or 
analyzing medical device data.
35 See 21 CFR Part 820.
36 See “Device Advice: Classify Your Medical Device” at https://www.fda.gov/medical-devices/overview-
device-regulation/classify-your-medical-device.
37 To meet this criterion, the device software functions or mobile medical apps need not be physically connected 
to the regulated medical device (i.e., the connection can be wired or wireless).
38 Controlling the intended use, function, modes, or energy source of the connected medical device.

---

<!-- Page 16 -->
Contains Nonbinding Recommendations
12
o Examples of these types of software functions include: software that provides 
the ability to control inflation and deflation of a blood pressure cuff through a 
mobile platform and mobile apps that control the delivery of insulin on an 
insulin pump by transmitting control signals to the pumps from the mobile 
platform.
In some cases, software that meets the definition of a device may be used in 
combination with other devices. In these cases, the device software function 
may be considered an accessory if it supports, supplements, and/or augments 
the performance of one or more parent devices. FDA’s “Medical Device 
Accessories - Describing Accessories and Classification Pathways”39
guidance document should be referenced for information pertaining to the 
regulation of accessories to medical devices.
2. Software functions (typically, mobile apps) that transform the mobile platform 
into a regulated medical device by using attachments, display screens, or sensors 
or by including functionalities similar to those of currently regulated medical 
devices. Software functions that use attachments, display screens, sensors, or 
other such similar components to transform a mobile platform into a regulated 
medical device are required to comply with the device classification associated 
with the transformed platform.
o Examples of these types of software functions include: a software function that 
uses a mobile platform for medical device functions, such as attachment of a 
blood glucose strip reader to a mobile platform to function as a glucose meter; 
or attachment of electrocardiograph (ECG) electrodes to a mobile platform to 
measure, store, and display ECG signals; a software function that uses the 
built-in accelerometer on a mobile platform to collect motion information for 
monitoring sleep apnea; a software function that uses sensors (internal or 
external) on a mobile platform for creating electronic stethoscope function is 
considered to transform the mobile platform into an electronic stethoscope; 
manufacturers of such a mobile app are required to follow the requirements of 
21 CFR 870.1875(b) (Electronic stethoscope); and similarly, a software 
function that displays radiological images for diagnosis transforms the mobile 
platform into a Medical image management and processing system under 21 
CFR 892.2050.
FDA has cleared several mobile medical apps with attachments to a mobile 
platform. Specifically, patient monitoring mobile apps that monitor a patient 
for heart rate variability from a signal produced by an electrocardiograph, 
vectorcardiograph, or blood pressure monitor are classified as cardiac 
monitoring software under 21 CFR 870.2300 (Cardiac monitor (including 
39 https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-accessories-
describing-accessories-and-classification-pathways

---

<!-- Page 17 -->
Contains Nonbinding Recommendations
13
cardiotachometer and rate alarm)). Other mobile medical apps that use a 
hardware attachment or interface to a monitoring system that have been 
cleared include an automatic electronic blood pressure monitor under 21 CFR 
870.1130 and a perinatal monitoring system under 21 CFR 884.2740.
3. Software functions that become a regulated medical device by performing 
patient-specific analysis and providing specific output(s) or directive(s) to health 
care professionals for use in the diagnosis, treatment, mitigation, cure, or 
prevention of a disease or condition. Additionally, software functions that 
perform patient-specific analysis and provide patient-specific diagnosis or 
treatment recommendations to patients, caregivers, or other users who are not 
health care professionals.
o Examples of these types of software functions include: software functions that 
use patient-specific parameters and calculate dosage or create a dosage plan 
for radiation therapy; Computer Aided Detection software (CAD) image 
processing software;40 and radiation therapy treatment planning software;41
software function that analyzes patient-specific medical information to detect 
a life-threatening and/or time critical condition, such as stroke or sepsis, and 
generate an alarm or an alert to notify a health care professional;42 software 
function that analyzes readings from a blood glucose monitor and alerts the 
user of readings outside a predetermined range; software function that 
analyzes an ECG waveform output from an FDA-cleared device to detect or 
diagnose arrhythmias (e.g., atrial fibrillation).43 We believe that these types of 
software present the same level of risk to patients regardless of the platform 
on which they run.
FDA encourages manufacturers of such device software functions that perform patient-
specific analysis to contact FDA to discuss what, if any, regulatory requirements may apply. 
For additional examples see Appendix C.
B. 
Software functions for which FDA intends to 
exercise enforcement discretion (meaning that 
FDA does not intend to enforce requirements 
under the FD&C Act)
In general, FDA intends to exercise enforcement discretion for software functions that:
1. Help patients (i.e., users) self-manage their disease or conditions without providing 
specific treatment or treatment suggestions; or
40 21 CFR 892.2050.
41 21 CFR 892.2050.
42 Similar to Example 12 in Section V.C “Examples of Device Software Functions” of the CDS Guidance
43 Similar to Example 20 in Section V.C “Examples of Device Software Functions” of the CDS Guidance

---

<!-- Page 18 -->
Contains Nonbinding Recommendations
14
2. Automate simple tasks for health care professionals.
Some software functions in the above categories and listed below may be considered device 
software functions, and others might not. For these examples listed below that are devices, 
FDA intends to exercise enforcement discretion because they pose a low risk to patients.
The following examples represent software functions for which FDA intends to exercise 
enforcement discretion:
1. Software functions that provide or facilitate supplemental clinical care, by 
coaching or prompting, to help patients manage their health in their daily 
environment – These are software functions that supplement44 professional clinical 
care by facilitating behavioral change or coaching patients with specific diseases or 
identifiable health conditions in their daily environment. Examples include:
o Software functions that coach patients with conditions such as cardiovascular 
disease, hypertension, diabetes, or obesity, and promote strategies for 
maintaining a healthy weight, getting optimal nutrition, exercising and staying 
fit, managing salt intake, or adhering to pre-determined medication dosing 
schedules45 by simple prompting.
2. Software functions that are specifically marketed to help patients communicate 
with health care professionals by supplementing or augmenting the data or 
information by capturing an image for patients to convey to their health care 
professionals about potential medical conditions – These products either pose little 
or no risk, or are the sole responsibility of the health care professionals who have 
experience with them in medical applications. Examples include:
o Apps specifically intended for medical uses that utilize the mobile device’s 
built-in camera or a connected camera for purposes of documenting or 
transmitting pictures (e.g., photos of a patient’s skin lesions or wounds) to 
supplement or augment what would otherwise be a verbal description in a 
consultation between health care professionals or between health care 
professionals and patients/caregivers.
3. Software functions that perform simple calculations routinely used in clinical 
practice – These are software functions that are intended to provide a convenient way 
for clinicians to perform various simple medical calculations taught in medical 
44 By this we mean that the software function can be safely used by a patient without active oversight by a 
medical professional and, when used for serious conditions necessitating professional medical care, use of the 
software function is not intended to replace or discourage seeking treatment from a health care professional.
45 We consider these device software functions to be “medication reminders – Product code NXQ” currently 
defined as “A medication reminder is a device intended for medical purposes to provide alerts to patients or 
health care providers for pre-determined medication dosing schedules. The device may incorporate wireless 
communication.” FDA intends to not enforce applicable regulatory requirements for this specific product code 
(NXQ) identified under 21 CFR 890.5050 – Daily activity assist device.

---

<!-- Page 19 -->
Contains Nonbinding Recommendations
15
schools46 and are routinely used in clinical practice. This software is generally 
tailored for clinical use, but retains functionality that is similar to simple general-
purpose tools such as paper charts, spread sheets, timers, or generic mathematical 
calculators. Examples of such general-purpose tools include medical calculators for:
o Body Mass Index (BMI);
o Total Body Water / Urea Volume of Distribution;
o Mean arterial pressure;
o Glasgow Coma Scale score;
o APGAR score;
o NIH Stroke Scale; or
o Delivery date estimator.
See Appendix B for additional examples of software functions for which FDA intends to 
exercise enforcement discretion.
VI. Regulatory Requirements
This guidance is intended to assist manufacturers in determining if a software function meets 
the definition of a device. Additional information can be found in “Device Advice: Classify 
Your Medical Device.”47 This section describes in greater detail the regulatory requirements 
applicable to device software functions under this guidance (as described in Section V).
Manufacturers of device software functions are subject to the requirements described in the 
applicable device classification regulation below. Depending on the classification and the 
associated regulation for the device software function, manufacturers are required to follow 
associated controls established by the regulation.
In general, the associated controls for each class of device are outlined below.
Class I devices: General Controls, including:
·
Establishment registration, and Medical Device listing (21 CFR Part 807);
·
Quality System (QS) regulation (21 CFR Part 820);
·
Labeling Requirements (21 CFR Part 801);
·
Medical Device Reporting (21 CFR Part 803);
·
Premarket Notification (21 CFR Part 807);
·
Reporting Corrections and Removals (21 CFR Part 806); and
·
Investigational Device Exemption (IDE) requirements for clinical studies of 
investigational devices (21 CFR Part 812).
46 The types of information in these calculators are available in medical sources, which includes medical 
textbooks used in the curriculum of accredited medical schools.
47 Available at https://www.fda.gov/medical-devices/overview-device-regulation/classify-your-medical-device.

---

<!-- Page 20 -->
Contains Nonbinding Recommendations
16
Class II devices: General Controls (as described for Class I), Special Controls, and (for most 
Class II devices) Premarket Notification.
Class III devices: General Controls (as described for Class I), and Premarket Approval (21 
CFR Part 814).
Appendix D provides a brief summary of the above requirements. Additional information is 
available at “Overview of Medical Device Regulation”48 and “How to Study and Market 
Your Device.”49 If you need further assistance, you may contact the Division of Industry and 
Consumer Education (DICE): Email: DICE@fda.hhs.gov; phone: 301-796-7100 or 800-638-
2041. For CBER, you may contact the Manufacturers Assistance and Technical Training 
Branch (MATTB): Email: Industry.Biologics@fda.hhs.gov; phone: 240-402-8020 or 800-
835-4709.
48 Available at https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-
assistance/overview-device-regulation.
49 Available at https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/how-
study-and-market-your-device.

---

<!-- Page 21 -->
Contains Nonbinding Recommendations
17
Appendix A  Examples of Software Functions that are 
NOT Medical Devices
This Appendix provides a representative list of software functions to illustrate the types of 
software that could be used in a health care environment, in clinical care, or patient 
management, but are not considered medical devices. Because these software functions are 
not considered medical devices, FDA does not regulate them. FDA understands that there 
may be other unique and innovative software functions that may not be covered in this list 
that may also constitute health care related software. This list is not exhaustive; it is only 
intended to provide clarity and assistance in identifying when a software function is not 
considered to be a medical device.
Specific examples of software functions that FDA does not consider to be devices and with 
no regulatory requirements under the current laws administered by FDA include:
1. Software functions that are intended to provide access to electronic “copies” 
(e.g., e-books, audio books) of medical textbooks or other reference materials 
with generic text search capabilities – These are not devices because the software is 
intended to be used as reference material and is not intended for use in the diagnosis 
of disease or other conditions, or in the cure, mitigation, treatment, or prevention of 
disease by facilitating a health professional’s assessment of a specific patient, 
replacing the judgment of clinical personnel, or performing any clinical assessment. 
Examples of these types of software functions include:
o Medical dictionaries;
o Electronic copies of medical textbooks or literature articles such as the 
Physician’s Desk Reference or Diagnostic and Statistical Manual of Mental 
Disorders (DSM);
o Library of clinical descriptions for diseases and conditions;
o Encyclopedia of first-aid or emergency care information;
o Medical abbreviations and definitions; and 
o Translations of medical terms across multiple languages. 
2. Software functions that are intended for health care professionals to use as 
educational tools for medical training or to reinforce training previously 
received – These may have more functionality than providing an electronic copy of 
text (e.g., videos, interactive diagrams), but are not devices because they are intended 
generally for user education and are not intended for use in the diagnosis of disease or 
other conditions, or in the cure, mitigation, treatment, or prevention of disease by 
facilitating a health professional’s assessment of a specific patient, replacing the 
judgment of clinical personnel, or performing any clinical assessment. Examples of 
these types of software functions include:
o Medical flash cards with medical images, pictures, graphs, etc.;
o Question/Answer quiz apps;

---

<!-- Page 22 -->
Contains Nonbinding Recommendations
18
o Interactive anatomy diagrams or videos;
o Surgical training videos;
o Medical board certification or recertification preparation apps; and
o Games that simulate various cardiac arrest scenarios to train health 
professionals in advanced cardiopulmonary resuscitation (CPR) skills.
3. Software functions that are intended for general patient education and facilitate 
patient access to commonly used reference information – This software can be 
patient-specific (i.e., filters information to patient-specific characteristics), but is 
intended for increased patient awareness, education, and empowerment, and 
ultimately supports patient-centered health care. These functions are not devices 
because they are intended generally for patient education, and are not intended for use 
in the diagnosis of disease or other conditions, or in the cure, mitigation, treatment, or 
prevention of disease by aiding clinical decision-making (i.e., to facilitate a health 
professional’s assessment of a specific patient, replace the judgment of a health 
professional, or perform any clinical assessment). Examples include software 
functions that:
o Provide a portal for health care professionals to distribute educational 
information (e.g., interactive diagrams, useful links, and resources) to their 
patients regarding their disease, condition, treatment, or upcoming procedure;
o Help guide patients to ask appropriate questions to their physician relevant to 
their particular disease, condition, or concern;
o Provide information about gluten-free food products or restaurants;
o Help match patients with potentially appropriate clinical trials and facilitate 
communication between the patient and clinical trial investigators;
o Provide tutorials or training videos on how to administer first-aid or CPR;
o Allow users to input pill shape, color, or imprint, and displays pictures and 
names of pills that match this description;
o Find the closest medical facilities and doctors to the user’s location;
o Provide lists of emergency hotlines and physician/nurse advice lines; and
o Provide and compare costs of drugs and medical products at pharmacies in the 
user’s location.
4. Software functions that automate general office operations in a health care 
setting and are not intended for use in the diagnosis of disease or other conditions, or 
in the cure, mitigation, treatment, or prevention of disease. Examples include 
software functions that:
o Determine billing codes like ICD-9 (international statistical classification of 
diseases);
o Enable insurance claims data collection and processing and other apps that are 
similarly administrative in nature;
o Analyze insurance claims for fraud or abuse;
o Perform medical business accounting functions or track and trend billable 
hours and procedures;

---

<!-- Page 23 -->
Contains Nonbinding Recommendations
19
o Generate reminders for scheduled medical appointments or blood donation 
appointments;
o Help patients track, review, and pay medical claims and bills online;
o Manage shifts for doctors;
o Manage or schedule hospital rooms or bed spaces;
o Provide wait times and electronic check-in for hospital emergency rooms and 
urgent care facilities;
o Allow health care professionals or staff in health care settings to process 
payments (for example, using a HIPAA compliant app to process payments); 
and
o Track or perform patient satisfaction survey after an encounter or a clinical 
visit.
5. Software functions that are generic aids or general-purpose products – This 
software is not considered a device because it is not intended for use in the diagnosis 
of disease or other conditions, or in the cure, mitigation, treatment, or prevention of 
disease. Examples include software functions that:
o Use the mobile platform as a magnifying glass (but are not specifically 
intended for medical purposes);50
o Use the mobile platform for recording audio, note-taking, replaying audio 
with amplification, or other similar functionalities;
o Allow patients or health care professionals to interact through email, web-
based platforms, video, or other communication mechanisms (but are not 
specifically intended for medical purposes);
o Provide maps and turn-by-turn directions to medical facilities; and
o Allow health care professionals to communicate in a secure and protected 
method (for example using a HIPAA compliant app to send messages between 
health care professionals in a hospital).
6. Software functions that are intended for individuals to log, record, track, 
evaluate, or make decisions or behavioral suggestions related to developing or 
maintaining general fitness, health or wellness, such as those that:
o Provide tools to promote or encourage healthy eating, exercise, weight loss, or 
other activities generally related to a healthy lifestyle or wellness;
o Provide dietary logs, calorie counters, or make dietary suggestions;
o Provide meal planners and recipes;
o Track general daily activities or make exercise or posture suggestions;
o Track a normal baby’s sleeping and feeding habits;
o Actively monitor and trend exercise activity;
50 Medical purpose magnifiers are regulated either under 21 CFR 886.5840 – Magnifying spectacles (“devices 
that consist of spectacle frames with convex lenses intended to be worn by a patient who has impaired vision to 
enlarge images”), or under 21 CFR 886.5540 – Low-vision magnifiers (“a device that consists of a magnifying 
lens intended for use by a patient who has impaired vision. The device may be held in the hand or attached to 
spectacles”).

---

<!-- Page 24 -->
Contains Nonbinding Recommendations
20
o Help healthy people track the quantity or quality of their normal sleep 
patterns;
o Provide and track scores from mind-challenging games or generic “brain age” 
tests;
o Provide daily motivational tips (e.g., via text or other types of messaging) to 
reduce stress and promote a positive mental outlook;
o Use social gaming to encourage healthy lifestyle habits; and
o Calculate calories burned in a workout.
7. Software functions that enable individuals to interact with electronic health 
record (EHR) software certified under the ONC Health IT Certification 
Program – These are software functions that provide individuals with access to 
health record systems or enable them to gain electronic access to health information 
stored within an EHR system. Software functions that only allow individuals to view, 
transfer, or download EHR data are also included in this category. These software 
functions are generally meant to facilitate general patient health information 
management and health recordkeeping activities:
o Software functions for health care professionals certified under the ONC 
Health IT Certification Program, such as those that help track or manage 
patient immunizations by documenting the need for immunization, consent 
form, and immunization lot number.
o Software functions certified under the ONC Health IT Certification Program 
that prompt the health care professional to manually enter symptomatic, 
behavioral, or environmental information, the specifics of which are pre-
defined by a health care professional, and store the information for later 
review.
8. Software functions that enable patients or health care professionals to interact with 
EHR systems (e.g., transfer, store, convert formats, display electronic patient records) 
that are certified under the ONC Health IT Certification Program, or interact with 
personal health record (PHR) systems. 
9. Software functions that allow a user to record (i.e., collect and log) data, such as 
blood glucose, blood pressure, heart rate, weight, or other data from a device to 
eventually share with a heath care professional, or upload it to an EHR that is 
certified under the ONC Health IT Certification Program, or upload it to an online 
(cloud) database, or upload it to a PHR.
10. Software functions that provide a list of appropriate cholesterol-lowering drugs to a 
health care professional to consider based on a patient’s cholesterol levels and 
demographics found in the EHR, and the basis for the recommendations is provided

---

<!-- Page 25 -->
Contains Nonbinding Recommendations
21
to the health care professional, so the health care professional does not rely primarily 
on the recommendations in making a clinical decision about a patient.51
11. Software functions that provide health care professionals easy access to 
information related to patients’ health conditions or treatments (beyond 
providing an electronic “copy” of a medical reference), and enable the health 
care professional to independently review the basis of the information provided 
by the software function, such that the health care professional does not rely 
primarily on the information to make a clinical decision about an individual 
patient:52
o These software functions match patient-specific medical information (e.g., 
diagnosis, treatments, allergies, signs or symptoms) to reference information 
routinely used in clinical practice (e.g., practice guidelines) to facilitate 
assessments of specific patients. For example, a software function that uses a 
patient’s diagnosis and other medical information to provide an HCP with 
current practice treatment guidelines for common illnesses or conditions such 
as influenza, hypertension, and hypercholesterolemia.53
o The software function matches patient-specific medical information to peer-
reviewed literature publications on related topics and enables the health care 
professional to independently review the basis for the information. 
o Drug-drug interaction and drug-allergy contraindication notifications to avert 
adverse drug reactions. These software functions that identify drug-drug 
interactions and drug-allergy contraindications, based on the current version 
of FDA-approved drug or device labeling or other up-to-date and peer-
reviewed sources and patient-specific information, to attempt to prevent 
adverse drug reactions, and the software functions enable the health care 
professional to independently review the basis for the information. For 
example, a software function that identifies drug-disease interactions and 
contraindications, such as notifying an HCP that a patient with asthma should 
not be prescribed a non-selective beta-blocking drug.54
12. Software functions that provide patients with simple tools to organize and 
record their health information – These are software functions that provide patients 
with tools to organize and record health information without providing 
recommendations to alter or change a previously prescribed treatment or therapy. 
Examples include:
51 Similar to example 9.a in Section V.A “Examples of Non-Device CDS Software Functions” in the “Clinical 
Decision Support Software” Guidance
52 Refer to section 520(o)(1)(E) of the FD&C Act and the “Clinical Decision Support Software” guidance for 
information on the criteria relating to this description.
53 Similar to example 2 a-b in Section V.A “Examples of Non-Device CDS Software Functions” in the “Clinical 
Decision Support Software” Guidance
54 Similar to example 4 a-c in Section V.A “Examples of Non-Device CDS Software Functions” in the “Clinical 
Decision Support Software” Guidance

---

<!-- Page 26 -->
Contains Nonbinding Recommendations
22
o Software functions that provide simple tools for patients with specific 
conditions or chronic disease (e.g., obesity, anorexia, arthritis, diabetes, heart 
disease) to record their events or measurements (e.g., blood pressure 
measurements, drug intake times, diet, daily routine, or emotional state) and 
share this information with their health care professional as part of a disease-
management plan.
13. Software functions that are specifically marketed to help patients document, 
show, or communicate to health care professionals regarding potential medical 
conditions – These products either pose little or no risk, or are the sole responsibility 
of the health care professionals who have used them in medical applications. 
Examples include:
o Software that serves as a videoconferencing portal specifically intended for 
medical use and to enhance communications between patients, health care 
professionals, and caregivers.
14. Software functions that help asthmatics record (i.e., collect and log) inhaler usage, 
asthma episodes experienced, location of user at the time of an attack, or 
environmental triggers of asthma attacks. 
15. Software functions that record the clinical conversation a clinician has with a patient 
and sends it (or a link) to the patient to access after the visit. 
16. Software functions that meet the definition of Non-Device-MDDS–55  These are 
software functions that are solely intended to transfer, store, convert formats, and 
display medical device data or results, without controlling or altering the functions or 
parameters of any connected medical devices. These do not include software 
functions intended to generate alarms or alerts or prioritize patient-related information 
on multi-patient displays, which are typically used for active patient monitoring to 
enable immediate awareness for potential clinical intervention, and are considered 
device software functions because these functions involve analysis or interpretation of 
laboratory test or other device data and results.
17. Software functions that display patient-specific medical device data – These 
include software functions that display medical images directly from a Picture 
Archiving and Communication System (PACS) server; 
18. Software functions that are intended for transferring, storing, converting 
formats, or displaying clinical laboratory test or other device data and results, 
55 Non-Device-MDDS is considered to be software functions that are solely intended to transfer, store, convert 
formats, and display medical device data or results, in accordance with the Medical Device Data Systems, 
Medical Image Storage Devices, and Medical Image Communications Devices guidance, available at 
https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-data-systems-
medical-image-storage-devices-and-medical-image-communications-devices.

---

<!-- Page 27 -->
Contains Nonbinding Recommendations
23
findings by a health care professional with respect to such data and results, general 
information about such findings, and general background information about such 
laboratory test or other device, unless such function is intended to interpret or analyze 
clinical laboratory test or other device data, results and findings. Examples include:
o Software functions that transfer, store, convert formats, and display medical 
device data without modifying the data and do not control or alter the 
functions or parameters of any connected medical devices (i.e., software 
functions that meet the definition of Non-Device-MDDS);
o Software functions that meet the definition of Non-Device-MDDS and 
connect to a nursing central station and display (but do not analyze or 
interpret) medical device data to a physician’s mobile platform for review;
o Software functions that are not intended for diagnostic image review such as 
image display for multidisciplinary patient management meetings (e.g., 
rounds) or patient consultation (and include a persistent on-screen notice, 
such as “for informational purposes only and not intended for diagnostic 
use”).

---

<!-- Page 28 -->
Contains Nonbinding Recommendations
24
Appendix B  Examples of Software Functions for which 
FDA intends to exercise enforcement discretion
This Appendix provides examples of software functions that MAY meet the definition of 
medical device but for which FDA intends to exercise enforcement discretion. These 
software functions may be intended for use in the diagnosis of disease or other conditions, or 
in the cure, mitigation, treatment, or prevention of disease. Even though this software MAY 
meet the definition of medical device, FDA intends to exercise enforcement discretion for 
these types of software functions because they pose lower risk to the public. FDA 
understands that there may be other unique and innovative software functions that may not be 
covered in this list that may also constitute health care related software. This list is not 
exhaustive; it is only intended to provide clarity and assistance in identifying the software 
functions that will not be subject to regulatory requirements at this time.
1. Software functions that help patients with diagnosed psychiatric conditions (e.g., 
post-traumatic stress disorder (PTSD), depression, anxiety, obsessive compulsive 
disorder (OCD)) maintain their behavioral coping skills by providing a “Skill of the 
Day” behavioral technique or audio messages that the user can access when 
experiencing increased anxiety.
2. Software functions that provide periodic educational information, reminders, or 
motivational guidance to pregnant people, smokers trying to quit, or people 
recovering from addiction. 
3. Software functions that use global positioning system (GPS) location information to 
alert asthmatics of environmental conditions that may cause asthma symptoms or 
alert an addiction patient (substance abusers) when near a pre-identified, high-risk 
location.
4. Software functions that use video and video games to motivate patients to do their 
physical therapy exercises at home.
5. Software functions that prompt a user to enter which herb and drug they would like to 
take concurrently and provide information about whether interactions have been seen 
in the literature and a summary of what type of interaction was reported.
6. Software functions that use patient characteristics such as age, sex, and behavioral 
risk factors to provide patient-specific screening, counseling, and preventive 
recommendations from well-known and established authorities. 
7. Software functions that use a checklist of common signs and symptoms to provide a 
list of possible medical conditions and advice on when to consult a health care 
professional.

---

<!-- Page 29 -->
Contains Nonbinding Recommendations
25
8. Software functions that guide a user through a questionnaire of signs and symptoms to 
provide a recommendation for the type of health care facility most appropriate to their 
needs.
9. Software functions that are intended to allow a user to initiate a pre-specified nurse 
call or emergency call using broadband or cellular phone technology.
10. Software functions that enable a patient or caregiver to create and send an alert or 
general emergency notification to first responders.
11. Software functions that keep track of medications and provide user-configured 
reminders for improved medication adherence.
12. Software functions that provide historical trending and comparison of vital signs (e.g., 
body temperature, heart rate, blood pressure, or respiratory rate).;
13. Software functions that aggregate and display trends in personal health incidents (e.g., 
hospitalization rates or alert notification rates).
14. Software functions allow a user to collect (electronically or manually entered) blood 
pressure data and share this data through email, track and trend it, or upload it to a 
personal or electronic health record.
15. Software functions that provide oral health reminders or tracking tools for users with 
gum disease.
16. Software functions that provide prediabetes patients with guidance or tools to help 
them develop better eating habits or increase physical activity.
17. Software functions that display, at opportune times, images or other messages for a 
substance abuser who wants to stop addictive behavior.
18. Software functions that provide patients and/or caregivers information about drug-
drug interactions and relevant safety information (side effects, drug interactions, 
active ingredient) as a report based on demographic data (e.g., age, sex), clinical 
information (current diagnosis), and current medications.

---

<!-- Page 30 -->
Contains Nonbinding Recommendations
26
Appendix C  Examples of Software Functions that are the 
focus of FDA’s regulatory oversight (Device Software 
Functions and Mobile Medical Apps)
This Appendix provides examples of software functions that are considered medical devices 
(i.e., device software functions), and on which FDA will focus its regulatory oversight. This 
software meets the definition of a device under section 201(h) of the FD&C Act and its 
functionality poses a risk to a patient’s safety if the software were to not function as intended. 
Each example below provides a non-exhaustive list of possible relevant product code(s) 
and/or regulation number.
FDA also encourages device software manufacturers to search FDA’s public databases, such 
as the “Product Classification”56 database and the “510(k) Premarket Notification”57
database, to determine the level of regulation for a given device and for the most up-to-date 
information about the relevant regulatory requirements.
Software functions (typically mobile apps) that transform a mobile platform into a 
regulated medical device and therefore are the focus of FDA’s regulatory oversight: 
These mobile apps use a mobile platform’s built-in features such as light, vibrations, camera, 
or other similar sources to perform medical device functions (e.g., mobile medical apps that 
are used by a licensed practitioner to diagnose or treat a disease). Possible product codes: 
Varies depending on the intended use and software function; see additional examples below.
·
Software functions that use a sensor or lead that is connected to a mobile platform to 
measure and display the electrical signal produced by the heart (electrocardiograph or 
ECG). Possible product code(s): DPS, MLC, OEY (21 CFR 870.2340), MLO, MWJ, 
DSH (21 CFR 870.2800).
·
Software functions that use a sensor or electrode attached to the mobile platform or 
tools within the mobile platform itself (e.g., microphone and speaker) to 
electronically amplify and “project sounds associated with the heart, arteries and 
veins and other internal organs” (i.e., an electronic stethoscope). Possible product 
code: DQD (21 CFR 870.1875(b)).
·
Software functions that use a sensor or electrode attached to the mobile platform or 
tools within the mobile platform itself (e.g., accelerometer) to measure physiological 
parameters during CPR and give feedback about the quality of CPR being delivered. 
Possible product code: LIX (21 CFR 870.5210).
·
Software functions that use a sensor attached to the mobile platform or tools within 
the mobile platform itself to record, view, or analyze eye movements for use in the 
56 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/classification.cfm.
57 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm.

---

<!-- Page 31 -->
Contains Nonbinding Recommendations
27
diagnosis of balance disorders (i.e., nystagmograph). Possible product code: GWN 
(21 CFR 882.1460).
·
Software functions that use tools within the mobile platform (e.g., speaker) to 
produce controlled levels of test tones and signals intended for use in conducting 
diagnostic hearing evaluations and assisting in the diagnosis of possible otologic 
disorders (i.e., an audiometer). Possible product code: EWO (21 CFR 874.1050).
·
Software functions that use a sensor attached to the mobile platform or tools within 
the mobile platform itself (e.g., accelerometer) to measure the degree of tremor 
caused by certain diseases (i.e., a tremor transducer). Possible product code: GYD (21 
CFR 882.1950).
·
Software functions that use a sensor attached to the mobile platform or tools within 
the mobile platform itself (e.g., accelerometer, microphone) to measure physiological 
parameters (e.g., limb movement, electrical activity of the brain (EEG)) during sleep 
and are intended for use in diagnosis of specific diseases or conditions such as sleep 
apnea. Possible product code(s): OLV (21 CFR 882.1400), LEL (21 CFR 882.5050), 
BZQ, MNR, PRK (21 CFR 868.2375), FLS, NPF (21 CFR 868.2377).
·
Software functions that use an attachment to the mobile platform to measure blood 
oxygen saturation for diagnosis of specific disease or condition. Possible product 
code(s): DQA, NLF, MUD, NMD (21 CFR 870.2700) or DPZ (21 CFR 870.2710).
·
Software functions that present donor history questions to a potential blood donor and 
record and/or transmit the responses to those questions for a blood collection facility 
to use in determining blood donor eligibility prior to collection of blood or blood 
components. Possible product code: MMH (21 CFR 864.9165).
·
Software functions that use an attachment to the mobile platform to measure blood 
glucose levels. Possible product code: NBW (21 CFR 862.1345).
·
Software functions that use an attachment to the mobile platform (e.g., light source, 
laser) to treat acne, reduce wrinkles, or remove hair. Possible product code: OLP, 
OHT, OHS (21 CFR 878.4810), OZC (21 CFR 890.5740).
·
Software functions that use a microphone or speaker within a mobile platform to 
serve as a audiometer to allow health care professionals to determine hearing loss at 
different frequencies. Possible product code: EWO (21 CFR 874.1050).
·
Software functions that analyze an image of a skin lesion using mathematical 
algorithms, such as fractal analysis, and provide the user with an assessment of the 
risk of the lesion.
Software functions that connect to an existing device type for purposes of controlling its 
operation, function, or energy source and therefore are the focus of FDA’s regulatory

---

<!-- Page 32 -->
Contains Nonbinding Recommendations
28
oversight: These software functions are those that control the operation or function (e.g., 
changes settings) of an implantable or body worn medical device. Possible product codes: 
Varies depending on the intended use and function of the parent medical device; see 
additional examples below.
·
Software functions that alter the function or settings of an infusion pump. Possible 
product codes: MEB, FRN, LZH, LZG, OPP, MEA (21 CFR 880.5725), FIH (21 
CFR 876.5820), LKK.
·
Software functions that act as wireless remote controls or synchronization devices for 
computed tomography (CT) or X-Ray machines. Possible product code: JAK (21 
CFR 892.1750), IZL (21 CFR 892.1720), KPR (21 CFR 892.1680).
·
Software functions that control or change settings of an implantable neuromuscular 
stimulator. Possible product code(s): GZC (21 CFR 882.5860).
·
Software functions that calibrate, control, or change settings of a cochlear implant. 
Possible product code(s): MCM.
·
Software functions that control the inflation or deflation of a blood-pressure cuff. 
Possible product code: DSJ (21 CFR 870.1100), DSK (21 CFR 870.1110), DXN (21 
CFR 870.1130).
·
Software functions that are used to calibrate hearing aids and assess the 
electroacoustic frequency and sound intensity characteristics emanating from a 
hearing aid, master hearing aid, group hearing aid, or group auditory trainer. Possible 
product code ETW (21 CFR 874.3310).
Software functions that are used in active patient monitoring or to analyze patient-
specific medical device data and therefore are the focus of FDA’s regulatory oversight:
·
Software functions that acquire or process physiological signals that connect to 
bedside (or cardiac) monitors for active patient monitoring. Possible product code(s): 
DSI, MHX, MLD (21 CFR 870.1025), DRT, MWI, MSX, PLB (21 CFR 870.2300).
·
Software functions that process uterine contraction and fetal heart rate data for remote 
monitoring of labor progress. Possible product code(s): HGM (21 CFR 884.2740).
·
Software functions that are intended to process images for diagnostic review may be 
regulated as a medical image management and processing system. Possible product 
code(s): LLZ (21 CFR 892.2050).
·
Software function that uses a variant call format (VCF) file containing patient-
specific genetic variants and mutations identified from a Next Generation Sequencing

---

<!-- Page 33 -->
Contains Nonbinding Recommendations
29
(NGS) Analyzer and provides recommendations for FDA-approved treatments based 
on those findings. Possible product code: QIC.58
·
Software function that analyzes patient-specific measurements (e.g., ST-segment 
elevation or depression as reported on ECG reports and cardiac enzyme laboratory 
results from the EHR) to identify patients potentially experiencing myocardial 
ischemia or infarction.59
·
Software function intended for health care professional management of heart failure 
patients that analyzes patient-specific medical information (e.g., daily heart rate, 
SpO2, blood pressure, or other output from wearable product) to predict heart failure 
hospitalization.60
·
Software function that analyzes the radiologist’s reported imaging findings and other 
patient-specific medical information taken by an health care professional upon 
admission as input to a stroke triage algorithm that indicates whether to transfer the 
patient to a major stroke center for an intervention.61
58 Similar to Example 18 in Section V.C “Examples of Device Software Functions” of the CDS Guidance
59 Similar to Example 23 in Section V.C “Examples of Device Software Functions” of the CDS Guidance
60 Similar to Example 24 in Section V.C “Examples of Device Software Functions” of the CDS Guidance
61 Similar to Example 28 in Section V.C “Examples of Device Software Functions” of the CDS Guidance

---

<!-- Page 34 -->
Contains Nonbinding Recommendations
30
Appendix D  Brief description of certain device regulatory 
requirements
This Appendix provides a high level description of certain regulatory requirements for 
medical devices, including device software functions. FDA has additional resources and 
publications online that describe these and other requirements in detail.
1. Establishment Registration and Medical Device Listing
Under 21 CFR Part 807, manufacturers of medical devices are required to annually register 
their establishments62 with FDA and provide a list of the devices they market. The 
registration and listing requirement is a means of keeping FDA advised of who is 
manufacturing devices, and of the types of devices an establishment is manufacturing. 
Medical device manufacturers are required to register their establishments with FDA and to 
list63 by identifying to FDA the devices they are marketing.
Additional information can be found in “Device Advice: Device Registration and Listing.”64  
If you need further assistance, you may contact the Division of Risk Management 
Operations, Regulatory Policy and Systems Branch: Email: reglist@fda.hhs.gov, phone: 301-
796-7400. Assistance is also available from, Division of Industry and Consumer Education 
(DICE): Email: DICE@fda.hhs.gov, phone: 301-796-7100 or 800-638-2041. For CBER, you 
may contact the Manufacturers Assistance and Technical Training Branch (MATTB): Email: 
Industry.Biologics@fda.hhs.gov; phone: 240-402-8020 or 800-835-4709.
2. Investigational Device Exemption (IDE) requirements
Conducting clinical studies in accordance with the IDE requirements (21 CFR 812)65 helps to 
ensure clinical data are credible, accurate, and ethically procured. Furthermore, an IDE 
allows an investigational device to be used in a clinical study, for example in order to collect 
safety and effectiveness data required to support66 a marketing submission to FDA (e.g., 
Premarket Approval (PMA), Premarket Notification (510(k)), De Novo, Humanitarian 
Device Exemption (HDE)). Clinical studies with devices of significant risk must be approved 
62 Under 21 CFR 807.3(c), “Establishment” is defined as “a place of business under one management at one 
general physical location at which a device is manufactured, assembled, or otherwise processed.”
63 See 21 CFR Part 807.
64 Available at https://www.fda.gov/medical-devices/how-study-and-market-your-device/device-registration-
and-listing.
65 Available at https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812 
66 If you intend to use the data from a clinical investigation to support a marketing submission, we encourage 
you to refer to the guidance “Acceptance of Clinical Data to Support Medical Device Applications and 
Submissions: Frequently Asked Questions” available at https://www.fda.gov/regulatory-information/search-
fda-guidance-documents/acceptance-clinical-data-support-medical-device-applications-and-submissions-
frequently-asked

---

<!-- Page 35 -->
Contains Nonbinding Recommendations
31
by FDA and by an Institutional Review Board67 (IRB) before the study can begin. Studies 
with devices of non-significant risk must be approved by the IRB only before the study can 
begin.
Medical device manufacturers who intend to conduct research involving human subjects are 
encouraged to engage with FDA through the Q-submission Program68 to receive feedback on 
testing and development activities.
Further information regarding the investigational device exemption and Good Clinical 
Practice (GCP) can be found in the webpage, “Device Advice: Investigational Device 
Exemption.”69
3. Labeling requirements
Medical device manufacturers are required to comply with applicable labeling regulations 
found in 21 CFR Part 801 for medical devices and 21 CFR Part 809 for in vitro diagnostic 
products.
4. Premarket submission for approval or clearance
Medical device manufacturers should identify the current classification covering their device. 
Manufacturers are required to prepare and submit to FDA an appropriate premarket 
submission, as required for their device classification.
Additional information can be found in “Device Advice: Device Registration and Listing.”70
5. Quality System Regulation (QS Regulation)
Medical device manufacturers are required to comply with the QS regulation.71 The QS 
regulation does not prescribe in detail how a manufacturer must produce a specific device, 
but provides a framework for all manufacturers to develop and follow to help ensure that 
their products consistently meet applicable requirements and specifications. As part of this 
framework, manufacturers are required to develop requirements for their products that will 
result in devices that are safe and effective, and to establish methods and procedures to 
design, produce, and distribute their devices.
67 An IRB must comply with all applicable requirements of the IRB regulation (Part 56) and the IDE regulations 
(Part 812) in reviewing and approving device investigations involving human testing. Additional IRB 
information can be found on the following FDA webpage: https://www.fda.gov/medical-
devices/investigational-device-exemption-ide/ide-institutional-review-boards-irb 
68 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-
and-meetings-medical-device-submissions-q-submission-program 
69 Available at https://www.fda.gov/medical-devices/how-study-and-market-your-device/device-advice-
investigational-device-exemption-ide.
70 Available at https://www.fda.gov/medical-devices/how-study-and-market-your-device/device-registration-
and-listing.
71 Available at https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820

---

<!-- Page 36 -->
Contains Nonbinding Recommendations
32
Furthermore, manufacturers are required, as part of the QS regulation (21 CFR 820.30), to 
appropriately verify and validate their device software functions along with the computing 
platform to ensure safe and effective operation of the device.
Manufacturers are required to ensure that adequate controls and processes are in place 
through purchasing controls to ensure safe distribution, installation, and operation of the 
device software function.
Additional information regarding the QS regulation can be found at “Quality System (QS) 
Regulation/Medical Device Good Manufacturing Practices.”72
6. Medical Device Reporting (MDR) (Adverse event reporting)
The Medical Device Reporting (MDR) regulation requires manufacturers and importers of 
medical devices to submit reports to FDA whenever they receive or otherwise become aware 
of information, from any source, that reasonably suggests that a device they market may have 
caused or contributed to a death or serious injury, or has malfunctioned and the device or a 
similar device that they market would be likely to cause or contribute to a reportable death or 
serious injury if the malfunction were to recur.73 MDR requires medical device 
manufacturers to:
·
Submit MDR reportable events involving their medical devices as described in 21 
CFR 803.10(c) and 803.50;
·
Submit 5-day reports as described in 21 CFR 803.53;
·
Submit supplemental reports as described in 21 CFR 803.56;
·
Develop, maintain, and implement written procedures for the identification and 
evaluation of all medical device events to determine whether the event is MDR 
reportable as described in 21 CFR 803.17;
·
Conduct an investigation of each event and evaluate the cause of the event as 
described in 21 CFR 803.50(b)(3); and
·
Establish and maintain complete files for all complaints concerning adverse medical 
device events as described in 21 CFR 803.18.
The MDR report (FDA Form 3500A)74 must contain all the information described in 21 CFR 
803.52 that is reasonably known to the manufacturer. Information reasonably known includes 
any information that:
·
Can be obtained by contacting a user facility, importer, or other initial reporter;
·
Is in the possession of the manufacturer; or
72 Available at https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-system-qs-
regulationmedical-device-good-manufacturing-practices.
73 See 21 CFR Part 803.
74 Available at https://www.fda.gov/safety/medical-product-safety-information/medwatch-forms-fda-safety-
reporting.

---

<!-- Page 37 -->
Contains Nonbinding Recommendations
33
·
Can be obtained by analysis, testing, or other evaluation of the device.
For additional instructions on how to complete the 3500A form, refer to the document titled 
“Instructions for Completing Form FDA 3500A.”75
For additional guidance on the MDR regulation and the reporting requirements, refer to the 
FDA guidance “Medical Device Reporting for Manufacturers.”76
For Questions about Medical Device Reporting, including interpretation of MDR policy:
·
Call: (301) 796-6670 (voice)
·
Email: RSMB@fda.hhs.gov 
·
Mail: Food and Drug Administration, Center for Devices and Radiological Health, 
Reporting Systems Monitoring Branch, 10903 New Hampshire Avenue, WO Bldg. 
66, Room 3217, Silver Spring, MD 20993-0002
7. Correcting Problems
A medical device manufacturer may voluntarily take action at any time or may be requested 
to take action by FDA to correct problems. Voluntary action is usually taken by device 
manufacturers. Examples of the types of actions that a device manufacturer may be requested 
to take include, but are not limited to:
·
Inspecting the device for problems;
·
Repairing the device;
·
Adjusting settings on the device; and
·
Upgrading software to reduce risk from a “bug” or unintended response.
Under certain circumstances, FDA may initiate a request that a manufacturer address a 
problem with a device through other means, including by removal of the product from the 
market. When recommending corrective action, FDA intends to take into account the 
essential role that certain device software functions take as an integral part of a larger patient 
care system.
Reporting Corrections to FDA: 
In accordance with 21 CFR 806.10, medical device manufacturers are required to promptly 
report, within 10 working days from the time the correction is initiated, to FDA certain 
actions concerning device corrections and removals. Specifically, medical device 
manufacturers are required to report to FDA any corrections made to a device to reduce a risk 
to health posed by the device or to remedy a violation of the FD&C Act caused by the device 
that may present a risk to health.
75 Available at https://www.fda.gov/safety/forms-reporting-fda/instructions-completing-form-fda-3500.
76 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-
reporting-manufacturers.

---

<!-- Page 38 -->
Contains Nonbinding Recommendations
34
The reporting requirement does not extend to all modifications to devices. For example, 
certain actions that would improve the quality of a mobile medical app but that would not 
reduce a risk to health posed by the mobile medical app or remedy a violation of the FD&C 
Act are not required to be reported under 21 CFR 806.1(b).77 If there is not a “risk to health” 
involved, a report to FDA is not required, but the device manufacturer must keep a record of 
the correction. An example of such action taken by the manufacturer could be changes made 
to correct a defect that creates a nuisance for the user but does not present a risk to the health 
of the user or patient.
More information about reporting requirements under 21 CFR Part 806 is available in 
“Device Advice: Recalls, Corrections, and Removals.”78
77 Under 21 CFR 806.1(b), the following actions are exempt from the reporting requirements of Part 806: 
(1) Actions taken by device manufacturers or importers to improve the performance or quality of a device but 
that do not reduce a risk to health posed by the device or remedy a violation of the act caused by the device. 
(2) Market withdrawals as defined in 21 CFR 806.2(i).
(3) Routine servicing as defined in 21 CFR 806.2(l). 
(4) Stock recoveries as defined in 21 CFR 806.2(m).
78 Available at https://www.fda.gov/medical-devices/postmarket-requirements-devices/recalls-corrections-and-
removals-devices.

---

<!-- Page 39 -->
Contains Nonbinding Recommendations
35
Appendix E  Frequently Asked Questions (FAQs)
1) I have a software function that is not identified in this guidance. What is the best 
way to get additional information from FDA about my product?
Answer: FDA recognizes that this guidance does not describe all types of software used in 
health care. Some manufacturers may be unsure whether their software function is 
considered a medical device that is subject to regulatory oversight, or whether their medical 
device could be under FDA’s intent to exercise enforcement discretion. If the device is 
subject to regulatory oversight, manufacturers may have questions about which regulatory 
requirements are applicable to their software function.
After reviewing this guidance, FDA encourages software manufacturers to contact the 
Agency to obtain more information using one of the following ways:
- 
Phone or email – For information about regulatory requirements, contact the Division of 
Industry and Consumer Education (DICE). Email: DICE@fda.hhs.gov; phone: 301-796-
7100 or 800-638-2041.  
 
For information about whether your software or mobile app is considered a medical 
device, contact digitalhealth@fda.hhs.gov. 
If your question relates to apps used in blood establishments or another area of CBER 
regulation, contact the Office of Communication, Outreach and Development, Center for 
Biologics Evaluation and Research; email: ocod@fda.hhs.gov; phone: 1-800-835-4709 or 
240-402-7800.
- 
Online – FDA has several resources and publications online that describe various 
regulatory requirements in detail. FDA’s “Device Advice”79 website and online courses 
at “CDRH Learn”80 are a good place to start. Other sections in this guidance provide links 
to more detailed information related to more specific topics. 
- 
Letter – For written feedback about the classification and the regulatory requirements that 
may be applicable to a device software function, manufacturers should use the 513(g) 
process. Specifically, a manufacturer should submit the following for a 513(g) 
submission:
·
User fee;
·
Cover letter;
·
Description of the software;
·
Description of what the software is to be used for; and
79 Available at https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance.
80 Available at https://www.fda.gov/training-and-continuing-education/cdrh-learn.

---

<!-- Page 40 -->
Contains Nonbinding Recommendations
36
·
Any proposed labeling or promotional material for the software and, as 
applicable, any labeling or promotional material of a similar, legally marketed 
device, if available.
FDA will generally issue a response to the 513(g), in the form of a confidential letter to the 
manufacturer, within 60 days of receipt of the request for information. For more specific 
information about what to include in a 513(g) and where to send it, refer to FDA’s guidance 
“FDA and Industry Procedures for Section 513(g) Requests for Information Contains 
Nonbinding Recommendations Under the Federal Food, Drug, and Cosmetic Act.”81 For 
more information about 513(g) user fees, refer to FDA’s guidance “User Fees for 513(g) 
Requests for Information”82
2) Why does FDA recommend that manufacturers follow the Quality System (QS) 
regulation for those software that MAY be devices and could be device software 
functions but for which FDA intends to exercise enforcement discretion?
Answer: FDA believes all manufacturers of medical device software should have in place an 
adequate quality management system that helps ensure that their products consistently meet 
applicable requirements and specifications and can support the software throughout its total 
life cycle. Adequate quality management systems incorporate appropriate risk management 
strategies, good design practices, adequate verification and validation, and appropriate 
methods to correct and prevent risks to patients and adverse events that may arise from the 
use of the product. All of these elements are part of FDA’s QS regulation.
3) Is FDA’s QS regulation similar to software development practices I already use?
Answer: Most likely. Though not all of the principles in the QS regulation are applicable to 
the development and manufacture of quality device software functions,83 the majority of 
them are applicable and are consistent with commonly used and accepted good software 
development practices, such as those from the Institute of Electrical and Electronics 
Engineers’ (IEEE), Software Engineering Body of Knowledge (SWEBOK), and Carnegie 
Mellon Software Engineering Institute’s Capability Maturity Model Integration (CMMI) 
methods.
FDA’s approach to QS regulation is also harmonized with certain international standards 
such as ISO 9001 and ISO 13485.84 Similar to these international standards, the QS 
regulation does not prescribe in detail how a manufacturer must produce a specific device, 
but provides a framework for all manufacturers to develop and follow to help ensure that 
81 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/fda-and-industry-
procedures-section-513g-requests-information-under-federal-food-drug-and-cosmetic.
82 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/fda-and-industry-
procedures-section-513g-requests-information-under-federal-food-drug-and-cosmetic.
83 Certain portions of the QS regulation that apply to medical device hardware (such as the production and 
process controls outlined in 21 CFR 820.70) may not clearly apply to device software functions.
84 ISO 9001 Quality management systems – Requirements and ISO 13485 Medical devices – Quality 
management systems – Requirements for regulatory purposes.

---

<!-- Page 41 -->
Contains Nonbinding Recommendations
37
their products consistently meet applicable requirements and specifications. The QS 
regulation can apply to and be scaled for any size manufacturer and any type of product. It 
also allows for a manufacturer to choose those requirements most appropriate for its given 
device and manufacturing process.85
4) What are some examples of parts of the QS regulation that are of particular 
importance to device software functions and where can I find more information 
about them?
Answer: Though not a complete list, some examples of principles within the QS regulation 
that are relevant to all device manufacturers include risk assessment and management, design 
controls, and corrective and preventive actions. Risk assessment and management is a critical 
part of good quality management systems. Good design practices are important to the 
development and manufacture of safe medical devices. It is also important for manufacturers 
to have procedures in place to identify, analyze, correct, and prevent software-related causes 
of patient or user harm. References related to these examples are provided in Appendix D of 
this guidance. Additional references about these principles that manufacturers may find 
useful include FDA’s guidances on “Design Control Guidance for Medical Device 
Manufacturers,”86 and “General Principles of Software Validation.”87
5) Do all the device software function manufacturers have to submit a premarket 
submission and receive FDA clearance or approval before marketing?
Answer: No, not all manufacturers have to submit a premarket submission (i.e., a 510(k) or 
PMA) prior to marketing their device software function. This determination depends on the 
classification of the device. Manufacturers of devices that are exempt from 510(k) or PMA 
requirements do not have to file a submission with FDA prior to marketing their device. For 
example, the majority of class I devices are exempt from the premarket submission 
requirements and are subject to the least regulatory control.
Regardless of whether medical devices are subject to the premarket submission requirements, 
most medical devices (including Class I devices) have to comply with other basic regulatory 
requirements that are called “General Controls.” More information about what “General 
Controls” are and what a medical device manufacturer should do to comply with these 
requirements, can be found in “Device Advice: General Controls for Medical Devices”88 and 
“Regulatory Controls.”89
85 See 21 CFR 820.1 (stating “if a manufacturer engages in only some operations subject to the requirements in 
this part, and not in others, that manufacturer need only comply with those requirements applicable to the 
operations in which it is engaged.”).
86 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/design-control-
guidance-medical-device-manufacturers. 
87 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-principles-
software-validation. 
88 Available at https://www.fda.gov/medical-devices/regulatory-controls/general-controls-medical-devices. 
89 Available at https://www.fda.gov/medical-devices/overview-device-regulation/regulatory-controls.

---

<!-- Page 42 -->
Contains Nonbinding Recommendations
38
6) Some FDA classifications state they are “510(k) exempt.” What does 510(k) 
exempt mean and how do I know if it applies to my product?
Answer: If a classification states the device type is “510(k) exempt,” this means that the 
manufacturer is not required to submit a premarket notification (i.e., a 510(k)) prior to 
marketing the device. However, the 510(k) exemption may be subject to certain limitations. 
Manufacturers are encouraged to confirm the device’s exempt status and any limitations to 
that status that may apply in accordance with 21 CFR Parts 862 – 892. The webpage 
“Medical Device Exemptions 510(k) and GMP Requirements” contains additional 
information about 510(k) exempt devices.90
7) If a 510(k) is required for my device software function, what type of software 
documentation does FDA recommend I include in the submission?
Answer: FDA’s recommendations for the software-related documentation that you provide 
in your premarket submission are addressed in detail in FDA’s “Guidance for the Content of 
Premarket Submissions for Software Contained in Medical Devices.”91
If the device software function uses off-the-shelf software, manufacturers should also refer to 
FDA’s “Guidance for Industry, FDA Reviewers, and Compliance on Off-the-Shelf Software 
Use in Medical Devices.”92
8) I am a medical device manufacturer and making my product labeling available 
electronically using a mobile app. Is my app considered a mobile medical app?
Answer: Mobile apps that provide electronic access and are intended for use as a digital 
version of medical device labeling or instructions for use are not considered a medical device 
on their own and therefore are not considered mobile medical apps. These are apps from a 
device manufacturer that provide information to support the company’s own device. 
Examples include apps that provide an electronic copy of cleared or approved medical device 
labeling or apps that provide video instruction for how to use a medical device. These types 
of apps are not considered devices within themselves, but instead are considered part of the 
medical device labeling and are subject to the regulatory labeling requirements relevant to 
that particular product.
9) Is an electronic method of collecting clinical investigations, for example through 
a mobile app, considered a device software function, and if so, what 
requirements apply?
Answer: Software used for data collection in clinical studies (such as electronic Patient 
Reported Outcomes (ePRO) apps) is not considered on its own to be a device software
90 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpcd/315.cfm 
91 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-content-
premarket-submissions-software-contained-medical-devices.
92 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/shelf-software-use-
medical-devices.

---

<!-- Page 43 -->
Contains Nonbinding Recommendations
39
function. However, manufacturers and users of this type of software should see FDA’s 
guidance related to use of computers in clinical trials, “Electronic Source Data in Clinical 
Investigations,”93 issued on September 17, 2013.
10) I am a medical device manufacturer. Is an electronic method of collecting and 
storing quality systems information in my manufacturing process considered a 
medical device?
Answer: Software used in the production process for medical devices, or for collecting, 
storing and maintaining quality system data collection for medical devices (including 
complaint submissions) is not considered a medical device on its own. This software does not 
meet the definition of medical device, but is part of the quality system. However this 
software is required to comply with the appropriate good manufacturing practices (GMP) 
regulations.94
93 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/electronic-source-
data-clinical-investigations.
94 See 21 CFR Part 820.

---

<!-- Page 44 -->
Contains Nonbinding Recommendations
40
Appendix F  Additional Resources
A. Guidance Documents
The webpage “Guidances with Digital Health Content”95 contains an up-to-date list of all 
guidance documents with Digital Health content.
B. 
Standards
The “Recognized Consensus Standard database”96 can be searched for the most up-to-date 
list of voluntary consensus standards recognized by FDA. A standard’s inclusion in the list 
below does not indicate it is currently recognized by FDA.
AAMI = Association for the Advancement of Medical Instrumentation
ANSI = American National Standards Institute
IEC 
= International Electrotechnical Commission
IEEE = Institute of Electrical and Electronics Engineers
ISO 
= International Organization for Standardization
1. ISO/IEC/IEEE 90003 Software engineering – Guidelines for the application of ISO 
9001:2015 to computer software. 
2. ISO 9001 Quality management systems – Requirements. 
3. ISO 13485 Medical devices – Quality management systems – Requirements for 
regulatory purposes. 
4. ISO 9000 Quality management systems – Fundamentals and vocabulary. 
5. ISO 14971 Medical devices — Application of risk management to medical devices. 
6. IEC 62304 Medical device software – Software life cycle processes. 
7. IEEE Std 1012 IEEE Standard for System, Software, and Hardware Verification and 
Validation. 
8. ISO/IEC 25051 Software engineering – Systems and software product Quality 
Requirements and Evaluation (SQuaRE) – Requirements for quality of Ready to Use 
Software Product (RUSP) and instructions for testing.
9. ISO/IEC/IEEE 12207 Systems and software engineering – Software life cycle processes.
95 Available at https://www.fda.gov/medical-devices/digital-health-center-excellence/guidances-digital-health-
content 
96 Available at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm

---

<!-- Page 45 -->
Contains Nonbinding Recommendations
41
10. AAMI TIR36 Validation of software for regulated processes.
11. IEC/TR 80002-1 Medical device software – Part 1: Guidance on the application of ISO 
14971 to medical device software. 
12. ANSI/AAMI ES60601-1 Medical electrical equipment – Part 1: General requirements 
for basic safety and essential performance (particularly clause 14).
13. IEC 61508-2 Functional safety of electrical/electronic/programmable electronic safety-
related systems – Part 2: Requirements for electrical/electronic/programmable electronic 
safety-related systems.
