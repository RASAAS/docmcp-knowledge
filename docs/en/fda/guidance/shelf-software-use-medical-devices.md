---
title: "Off-The-Shelf Software Use in Medical Devices: Guidance for Industry and Food and Drug Administration Staff"
description: "FDA CDRH Final Guidance Document"
published: 2023-08-11
---

# Off-The-Shelf Software Use in Medical Devices: Guidance for Industry and Food and Drug Administration Staff

**Published**: 2023-08-11

**Status**: Final
**Type**: Guidance Document
**Category**: Digital Health & Cybersecurity
**Topics**: Premarket, Digital Health
**Docket**: FDA-2019-D-3598

::: tip Official Source
[https://www.fda.gov/regulatory-information/search-fda-guidance-documents/shelf-software-use-medical-devices](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/shelf-software-use-medical-devices)
PDF: [https://www.fda.gov/media/71794/download](https://www.fda.gov/media/71794/download)
:::

<!-- fulltext-start -->

---

## Official Full Text

This guidance represents the current thinking of the Food and Drug Administration (FDA or Agency) on this topic. It does not establish any rights for any person and is not binding on FDA or the public. You can use an alternative approach if it satisfies the requirements of the applicable statutes and regulations. To discuss an alternative approach, contact the
FDA staff or Office responsible for this guidance as listed on the title page.
validation. The least burdensome approach was applied to identify the minimum amount of information that, based on our experience, would generally be needed to support a premarket submission for a device that uses OTS software.
The documentation recommended in this guidance is based on FDA’s experience evaluating the safety and effectiveness for a device that uses OTS software. However, sponsors may use alternative approaches and provide different documentation so long as their approach and documentation satisfy premarket submission requirements in applicable statutory provisions and regulations.
On September 27, 2019, this guidance was revised through a Level 2 update in accordance with the 21st Century Cures Act, with the changes described in the guidance “Changes to Existing Medical
Software Policies Resulting from Section 3060 of the 21st Century Cures Act.”4  This guidance was most recently revised through a Level 2 update in addition to the documentation described in FDA’s final guidance titled “Content of Premarket Submissions for Device Software Functions.”5
In general, FDA’s guidance documents do not establish legally enforceable responsibilities.
Instead, guidances describe the Agency’s current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited. The use of the word should in Agency guidances means that something is suggested or recommended, but not required.
## II. Scope
This guidance is intended to provide information regarding the recommended documentation in a premarket submission for a medical device that uses Off-the-Shelf software (OTS software), which is considered a generally available software component, used by a medical device manufacturer for which the manufacturer cannot claim complete software life cycle control (e.g., operating system, printer/display libraries).
For the purposes of this guidance, unless otherwise stated, the term premarket submission includes, but is not limited to, premarket notification (510(k)) submission, De Novo classification request, Premarket Approval (PMA) application, Investigational Device Exemption (IDE), or Humanitarian Device Exemption (HDE).
If the device is a multiple function device product and includes software function(s) that are considered “other functions,” as that term is used in the guidance “Multiple Function Device and instead incorporate by reference the 2016 edition of the International Organization for Standardization (ISO)
13485, Medical devices- Quality management systems for regulatory purposes, in part 820. As stated in that proposed rule, the requirements in ISO 13485 are, when taken in totality, substantially similar to the requirements of the current part 820, providing a similar level of assurance in a firm’s quality management system and ability to consistently manufacture devices that are safe and effective and otherwise in compliance with the FD&C Act. FDA intends to finalize this proposed rule expeditiously. When the final rule takes effect, FDA will also update the references to provisions in 21 CFR part 820 in this guidance to be consistent with that rule.
Product: Policy and Considerations,”6 the recommendations described in the aforementioned guidance should be considered when preparing the software documentation for a premarket submission.
## III. OTS Software Documentation Elements
As discussed in the guidance titled “Content of Premarket Submissions for Device Software Functions,”7 the recommended documentation for a premarket submission depends on the device’s risk to a patient, a user of a device, or others in the environment of use. FDA intends to take a risk-based approach to help determine the device’s Documentation Level, which is either Basic8 or Enhanced.9 The purpose of the Documentation Level is to help identify the minimum amount of information that would support a premarket submission that includes device software functions.  The Documentation Level of a device is based on the risks of its device software function(s) in the context of the device’s intended use,10 such that the documentation level reflects the device as a whole.
For the purposes of this guidance, Table 1 below provides an outline of the recommended documentation for each OTS software documentation element and corresponding Documentation
Level as determined in the “Content of Premarket Submissions for Device Software Functions”11 for the device software function. Please refer to subsections A-D in this section of the guidance for more detail.
Table 1. Outline of Recommended Documentation Software Documentation Elements Basic Documentation Level Enhanced Documentation Level Description of OTS Software (Section III.A)
An overview and description of the OTS software and actions taken for the continued safe and effective use of the medical device.
Risk Assessment of OTS Software (Section III.B)
Risk assessment demonstrating that risks related to the use of OTS software have been appropriately mitigated.
8 The documentation level provided for any premarket submission that includes device software function(s) where Enhanced Documentation does not apply.
9 The documentation level provided for any premarket submission that includes device software function(s), where a failure or flaw of any device software function(s) could present a hazardous situation with a probable risk of death or serious injury, either to a patient, user of the device, or others in the environment of use. These risks should be assessed prior to implementation of risk control measures. Sponsors should consider the risks in the context of the device’s intended use (e.g., impacts to safety, treatment, and/or diagnosis), and other relevant considerations.
Software Documentation Elements Basic Documentation Level Enhanced Documentation Level Software Testing as part of Verification and Validation (Section III.C)
Test plans and results for the OTS software, commensurate with the
Documentation Level (i.e., Basic or Enhanced) for the device.
Assurance of Development Methodologies and Continued Maintenance of OTS Software (Section III.D) FDA is not recommending this documentation as part of the premarket submission. Sponsors should document this information via the DHF for the device. During premarket review, FDA may request additional information, if needed, to evaluate the safety and effectiveness of the device.
Information to provide an assurance that the product development methodologies used by the OTS software developer are appropriate and sufficient, and mechanisms exist for assuring the continued performance, maintenance, and support of the OTS software.
### A. Description of OTS Software
For both Basic and Enhanced Documentation Levels as discussed in the guidance titled “Content of Premarket Submissions for Device Software Functions,”12 an overview and description of the OTS software features and functions should be provided.  Sponsors should consider and, as applicable, provide information to address the questions below when preparing the OTS software description. However, FDA recognizes that these questions and examples may not capture all the unique aspects of the device software and encourages the inclusion of additional information that will further FDA’s understanding of the device’s functionality to facilitate the review of a submission.
1. What is it?
For each component of OTS software used, the following should be specified: · Title and Manufacturer of the OTS software.
- Version Level, Release Date, Patch Number, and Upgrade Designation, as appropriate.
- Any OTS software documentation that will be provided to the end user.
- Why is this OTS software appropriate for this medical device?
- What are the expected design limitations of the OTS software?
Note: The sponsor should only use the OTS software as specified in an appropriate document (i.e., design history file). If the version of the OTS software changes, the appropriate document
For what configuration will the OTS software be validated? The following should be specified: - Hardware specifications: processor (manufacturer, speed, and features), RAM (memory size), hard disk size, other storage, communications, display, etc.
- Software specifications: operating system, drivers, utilities, etc. The software requirements specification (SRS) listing for each item should contain the name (such as Microsoft Windows
Operating System, Microsoft Windows Drivers, etc.), specific version levels (such as 4.1, 5.0, etc.) and a complete list of any patches that have been provided by the OTS software manufacturer.
3.  How will you assure appropriate actions are taken by the End User?
The following should be specified: - What aspects of the OTS software and system can (and/or must) be installed/configured?
- What steps are permitted (or must be taken) to install and/or configure the product?
- How often will the configuration need to be changed?
- What education and training are suggested or required for the user of the OTS software?
- What measures have been designed into the medical device to prevent the operation of any non-specified OTS software (e.g., word processors, games)? Operation of non-specified OTS software may be prevented by system design, preventive measures, or labeling. Introduction may be prevented by disabling input (USB, CD, modems).
4.  What does the OTS Software do?
What function does the OTS Software provide in this device? The following should be specified: - What is the OTS software intended to do? The sponsor’s design documentation should specify exactly which OTS components will be included in the design of the medical device and to what extent OTS software is involved in error control and messaging in device error control.
- What are the links with other software including software outside the medical device (not reviewed as part of this or another application)? The links to outside software should be completely defined for each medical device/module. The design documentation should include a complete description of the linkage between the medical device software and any outside software (e.g., networks).
5.   How do you know it works?
- Based on documentation Level (i.e., Basic or Enhanced) determined for the device software as discussed in the guidance titled “Content of Premarket Submissions for
Device Software Functions,”13 sponsors should: Describe testing, verification, and validation of the OTS Software and ensure it is appropriate for the device hazards Provide the results of the testing.
- Is there a current list of OTS Software problems (bugs) and access to updates?
For more information on software testing, verification, and validation, please see section III.C.
6. How will you keep track of (control14) the OTS Software?
An appropriate plan should answer the following questions: - What measures have been designed into the medical device to prevent the introduction of incorrect versions? On startup, ideally, the medical device should check to verify that all software is the correct title, version level, and configuration. If the correct software is not loaded, the medical device should warn the operator and shut down to a safe state.
- How will you maintain the OTS software configuration?
- Where and how will you store the OTS software?
- How will you ensure proper installation of the OTS software?
- How will you ensure proper maintenance and life cycle support for the OTS software?
### B. Risk Assessment of OTS Software
As discussed in the guidance titled “Content of Premarket Submissions for Device Software Functions,”15 a risk management file should be provided as part of a device software premarket submission. For both Basic and Enhanced Documentation Levels this should include a risk management plan. It should be clear in the risk management plan how the sponsor plans to evaluate the overall residual risk. In addition, the risk management file should also include a risk assessment demonstrating that risks have been appropriately mitigated, and a risk management report. For OTS software, the risks associated with the functions of the OTS software used in the device should be documented in the risk management file.
For more information on risk management files, please refer to the FDA guidance titled “Content of Premarket Submissions for Device Software Functions.”
### C. Software Testing as Part of Verification and Validation
Sponsors should include documentation regarding test plans and test results as part of the verification and validation activities for the OTS software. Testing activities include not only those performed by the OTS software developer, but also include those performed by the sponsor when qualifying the OTS software for its use in the specific medical device. Commensurate with the Documentation Level (i.e., Basic or Enhanced) determined for the device software as 14 As discussed in 21 CFR 820.50 (Purchasing controls), each manufacturer shall establish and maintain procedures to ensure that all purchased or otherwise received product and services conform to specified requirements.
Functions,” sponsors should: - Describe testing of the OTS software and demonstrate it is appropriate and adequate for the hazards associated with the OTS software as documented in the risk management file.
o Note: FDA recommends that software test plans identify the exact OTS software (title and version) that is to be used. When the software is tested, it should be integrated and tested using the specific OTS software.  Testing activities include those performed by the sponsor when qualifying the OTS software for its use in the specific medical device but may also include those performed by the OTS software developer.
- Provide the results of the testing.
o Note: If the sponsor allows the use of the medical device with different versions of OTS software, then the sponsor should validate the medical device for each OTS software version.
- Provide a current list of OTS software defects.16
### D. Assurance of Development Methodologies and Continued Maintenance of OTS Software
Generally, the following recommendations for premarket documentation are applicable to devices with Enhanced Documentation, where controls17 address the use of OTS software:
1. Provide assurance to the FDA that the product development methodologies used by the
OTS software developer are appropriate and sufficient for the intended use of the OTS software within the specific medical device. For example, this may include a review of the OTS software developer’s design and development methodologies used in the construction of the OTS software. This review should thoroughly assess the development and qualification documentation generated for the OTS software. If such an assurance is not possible, and if the residual risk evaluation of the hazardous situation after implemented risk control measures is not acceptable as defined in the risk management plan, the use of such OTS software may not be appropriate for the intended medical device application.
2. Demonstrate the existence of appropriate mechanisms for assuring the continued
performance, maintenance and support of the OTS software should the original OTS software developer either make changes to the OTS software and/or terminate their support of the OTS software.
## IV. OTS Software in Marketing Applications
The following recommendations are made available to help sponsors consider the use of OTS software as it relates to existing regulatory mechanisms and pathways.
Premarket Submissions for Device Software Functions” available at https://www.fda.gov/regulatoryinformation/search-fda-guidance-documents/content-premarket-submissions-device-software-functions.
17 As discussed in 21 CFR 820.50 (Purchasing controls), each manufacturer shall establish and maintain procedures to ensure that all purchased or otherwise received product and services conform to specified requirements.
### A. Master Files for Devices (MAFs)
Much of the information regarding development and validation of OTS software may not be readily available to the medical device manufacturer who wishes to use the OTS software as a device component. Commercial OTS software vendors who wish to make their OTS software available for use in medical devices, but do not want to share the confidential and/or proprietary details of their software development and validation with customers (medical device manufacturers), may direct the information in a device master file to the FDA. For more information on Master Files for Devices, please refer to the FDA Master File website.18
### B. OTS Software Changes requiring a 510(k)
The conditions under which a new or changed medical device including OTS software will require a new 510(k) are the same as for a device not involving OTS software. The decision as to whether a new 510(k) is required depends on the intended use of the device; the function of the OTS software; and to what extent the risks due to OTS software have been mitigated.
These conditions are given in the FDA guidances, “Deciding When to Submit a 510(k) for a
Change to an Existing Device,”19 and “Deciding When to Submit a 510(k) for a Software Change to an Existing Device.”20
### C. Investigational Device Exemption and Changes to OTS Software
The requirements for an investigational device exemption (IDE) are the same whether or not the medical device contains OTS software. The OTS software may be a component of a medical device or the OTS software may be the entire medical device, e.g., diagnostic software. The conditions that would require submission of an IDE are specified in section 21 CFR 812 and generally include changes to OTS software during an IDE study that would affect the patient population for which the medical device is intended; conditions of use of the device (including those recommended or suggested in the labeling or advertising; the probable benefit from the use of the device weighed against any probable injury or illness from such use); or the reliability of the medical device.21
Some specific issues related to OTS software might include initial (beta) testing of an OTS software medical device in clinical studies. Such a study must comply with applicable IDE requirements.22 For non-significant risk medical devices, that includes approval by an
During the Conduct of a Clinical Investigation, available at https://www.fda.gov/regulatory-information/search-fdaguidance-documents/changes-or-modifications-during-conduct-clinical-investigation-final-guidance-industry-andcdrh.
### D. Premarket Approval and OTS Software
The criteria and requirements for premarket approval (PMA) applications are discussed in section 21 CFR 814. When a manufacturer submits a PMA submission for a medical device, there must be valid scientific evidence (including clinical evidence, if needed) to support a reasonable assurance of safety and effectiveness of the device.24
The OTS software used in a medical device is evaluated in the context of the overall medical device. The extent to which the medical device manufacturer ensures that the OTS software was developed using appropriate life cycle control depends upon the overall risk of the medical device, the role of the OTS software, and the probable risk of death or serious injury,25 either to a patient, user of the device, or others in the environment of use, associated with possible failures or flaw of the OTS software component.26
### E. Product Labeling
FDA recommends that the user’s manual specify the version(s) of the OTS software that can be used with the medical device. Such specification would not be needed for embedded software (i.e., the user does not select the OTS software and cannot change the software provided by the medical device manufacturer).
The user’s manual should contain appropriate warnings to the user indicating that the use of any software other than those specified will violate the safety, effectiveness, and design controls of the medical device and that such use may result in an increased risk to users and patients. For more information on medical device labeling, please see FDA website “Device Labeling”27 as well as relevant guidance documents titled “Device Labeling Guidance #G91-1 (Blue Book Memo)”
28 and Labeling – Regulatory Requirements for Medical Devices (FDA 89-4203).29
25 Serious injury, as defined in 21 CFR 803.3(w), is an injury or illness that: 1) is life threatening, 2) results in permanent impairment of a body function or permanent damage to a body structure, or 3) necessitates medical or surgical intervention to preclude permanent impairment of a body function or permanent damage to a body structure.
Permanent is defined as irreversible impairment or damage to a body structure or function, excluding trivial impairment or damage.
Functions, available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/contentpremarket-submissions-device-software-functions.
If the hardware on which the OTS software runs is a stand-alone computer and the user is not “locked out” by hardware or software system features, then the user should be warned against installing any other software (utilities or applications programs) on the computer.
Appendix A: General Considerations for OTS Software
The purpose of this Appendix is to provide background information and general topic areas sponsors may want to consider when preparing a premarket submission for FDA’s evaluation of OTS software used in a medical device. While these various topics may not be applicable to all OTS software, FDA believes that this remains pertinent information for sponsors to consider.
### A. Maintenance and Obsolescence
Maintenance activities are generally considered to begin after the establishment and distribution of a medical device product baseline. The distinction between maintenance and product development is an important one. Product development design activities generally lead to a system structure of highly integrated components and logic. Maintenance activities introduce changes into this structure that may lead to a loss in the integrity of the structure.
Structure integrity may be affected through changes due to new design requirements, corrections, or environmental adaptations. These types of changes may impact the integrity of the structure organization, architecture, logic, integration, or any combination of these characteristics. Maintenance of products with OTS software components may be particularly problematic for reasons discussed in the main body of this document (i.e., the sponsor does not have control of the OTS software component life cycle process).
In particular, this section identifies general safety and effectiveness, design, software testing as a part of verification/validation, change, installation, and decommissioning concerns. These concerns may be applied to all regulated medical device software and stand-alone medical software devices. The appropriate evaluation will depend on the probable risk of death or serious injury, either to a patient, user of the device, or others in the environment of use.
Each concern below corresponds to a product development life cycle phase. The concerns identify fundamental maintenance concerns relevant to medical devices that include software.
Generally, when considering these topics, sponsors should follow the Quality System
Regulations (21 CFR Part 820), which include requirements for Design Control (21 CFR 820.30) and Corrective and Preventive action (21 CFR 820.100).
(1)
Safety
Introduction of new or modified OTS software component(s) to a product baseline may impact the safety of the product. Therefore, a safety impact assessment of the medical device should be performed, and associated hazards documented in a Risk Management File. For more information on risk management files, please refer to the FDA guidance titled “Content of
Premarket Submissions for Device Software Functions.” Traceability between these identified hazards, their design requirements, and test reports should be provided.
Analysis should include the review of release bulletins (known error reports), user manuals, specifications, patches, and literature and internet searches for other user’s experience with the OTS software component(s).
The submission should answer the following questions: - Has a risk assessment with traceability to requirements and test reports been provided?
- Are safety functions isolated from new OTS software component(s)?
- Does the new OTS software component(s) affect system safety integrity?
- What new human factors conditions are introduced with new OTS software component(s)?
(2)
Design
Introduction of new or modified OTS software component(s) to a product baseline may impact the original design of the product. This impact may result from necessary changes to the product structure organization, architecture, logic, integration, or a combination of these characteristics.
Problems attributable to structural changes include: - New system resource requirements, such as shared and/or fixed memory; · New timing considerations; - New memory organization (e.g., 16 bit to 32 bit to 64 bit words), partitioning; · New human factor issues; · New data integrity issues; and - New software required to create the final code (build tools).
Consequently, the submission should answer the following questions: - How will the new OTS software component(s) change the performance characteristics?
- How will the new OTS software component(s) change the operational environment?
- Is data integrity preserved?
(3)
Software Testing as Part of Verification and Validation
As in the establishment of a product baseline, verification and validation (V&V) activities should occur when maintenance changes are made to a product baseline. Analysis of these changes directs necessary V&V activities. New OTS software component(s) in a product baseline introduce unknown logic paths and complexities into the product. “Black-box” testing of OTS software component(s) may allow some validation claims to be made. However, the unknown logic paths and complexities of OTS software component(s) make it important to know that design structure or logic elsewhere in the system is not impacted. This means a full system regression test should be performed. Results of these testing activities should be documented.  For more information on software testing as part of verification and validation, please refer to the FDA guidance titled “Content of Premarket Submissions for Device Software Functions.”
The submission should answer the following questions: - Do test reports provide objective evidence that identified OTS software component hazards have been addressed?
- Do test reports provide objective evidence that all identified system hazards have been addressed?
- Has a system regression test been performed?
(4)
Installation
Changes in a product baseline structure resulting from the integration of new OTS software component(s) may impact installation requirements. This impact can range from minor documentation changes to field upgrades. The sponsor should ascertain the impact of OTS software component changes on fielded products.
The submission should answer the following question: What is the impact of new OTS software component(s) on fielded medical device products? For example, do new OTS software component(s) correctly operate within the specifications of medical devices currently fielded?
(5)
Obsolescence
Rapid technology changes, economics, and market demand are shrinking product life spans. A direct consequence of these phenomena is that an OTS software component today may not exist two years from now. Short life spans are a particular characteristic of software because it is relatively easy to change. Obsolescence of OTS software component(s) can have significant impact on regulated products because the device manufacturer may lose the ability to properly support fielded products. The sponsor needs to support fielded medical device products with OTS software components.
The submission should answer the following questions: - Will the old OTS software component(s) still be available for fielded medical devices?
- Is there a retirement plan for OTS software component(s) to be replaced/eliminated?
- Do new OTS software component(s) replace fielded components?
(6)
Product Configuration
The submission must identify the product to be considered. Therefore, the product configuration provided should specify: - Hardware platform (e.g., microprocessor, minimum memory required, addressable word size); - Software platform (such as operating system, communications, databases, necessary utilities, etc.); · OTS component(s) other than Utilities and Drivers (Appendix A, Section B) above (see recommended content discussed in the main body of this document); and · Internally developed application(s).
### B. Operating Systems, Drivers, and Utilities
The operating system software is the primary software program that manages the basic functions of the computer and its associated hardware, including peripherals. The operating system provides a basic user interface, is responsible for managing applications programs and tasks, controlling memory allocation and data storage devices, and providing input/output for the computer, as well as any additional peripheral devices that are present.
“Open” hardware (mass market) architecture computers vary widely in architectural and organizational characteristics such as timing, addressing, and processing. Operating systems and application software executing on these platforms should be “robust” enough to perform appropriately in this environment.
OTS operating systems are commonly considered for incorporation into medical devices as the use of general-purpose computer hardware becomes more prevalent. The use of OTS operating system software allows device manufacturers to concentrate on the application software needed to run device-specific functions. However, an OTS operating system software is intended for general-purpose computing and may not be appropriate for a given specific use in a medical device. Developers of OTS operating systems typically design their systems for generalpurpose business or consumer computing environments and tasks where software failures and errors are more accepted. This acceptability of errors in the general- purpose computing environment may make the OTS operating system software inappropriate for less error-tolerant environments or applications.
The incorporation of OTS operating system software may also introduce unnecessary functions and complexity into a medical device. General-purpose functional requirements typically result in the OTS operating system software being large and unwieldy in the attempt to incorporate more functionality into the operating system. This excess functionality is typically never used for specific medical device applications and increases the likelihood that errors may be introduced into the operating system. The basic functions of an OTS operating systems used for medical device applications are typically the graphical user interface environment and the hardware interface functions. There are a number of operating systems used for timing- or resource-critical applications that provide the basic functionality needed to support user and hardware interfaces, but do not have many of the disadvantages of general-purpose business or consumer operating systems.
OTS driver software packages provide interface functions between the CPU, operating system, and the input/output peripheral. However, the performance and functionality of the OTS driver software may be affected by the overall system configuration and the OTS hardware. In most cases, a particular software driver derives from a particular interface protocol and contains the data signals, control signals, and timing signals for proper operation.
Since tests for most input/output interface/bus configurations require the particular bus analysis or logic analysis, scope, and knowledge of the particular interface protocol, the validation process for the OTS driver software package should be part of the system interface validation process. This includes the verification of the data values in both directions for the data signals; various mode settings for the control signals in both directions (if applicable); and the input/output interrupt and timing functions of the driver with the CPU and operating system.
Utility software is generally designed to work with a specific operating system. Unlike applications software, utility software is intended to supplant or enhance functions typically performed by the operating system. Examples of utility programs are memory managers, file managers, and virus checkers. Networking software can also be considered as utility software in that it allows multiple computers to access the same resources. Operating systems can also be designed to support or enable network operations without any additional utility software.
OTS utility software packages can perform the following functions: math functions (fast
Fourier transform, sin, cos); display functions (graphic); management functions (copy, delete, store various computer data/files); and the data manipulation function (transfer from one
Boolean type or both). The validation for these types of the software should be appropriate to the probable risk of death or serious injury, either to a patient, user of the device, or others in the environment of use as it pertains to use with a medical device.
### C. Local Area Networks (LANs) and Other Networks
Medical devices, particularly multi-parameter patient monitors and imaging systems, are increasingly networked for clinical work groups, centralized monitoring, and storage of patient medical data and records. LANs and other networks support more and more communication and sharing of images, measurement data, audio, video, graphics, text, etc. This heterogeneous media environment comes at a cost of more processing power, higher bandwidth or network speed, sophisticated object-relational databases, and security and access considerations.
The evaluation of networked medical devices begins with a definition of the technical requirements of the network application and the understanding of those requirements.
(1)
Requirements Analysis
### B. Speed – The response time required for safe and effective operation determines the LAN
data rate (bandwidth) for the medical device system. The CPU processing power and clock speed required at device monitors, workstations, and client machines should be appropriate so that bottlenecks do not occur.
### C. LAN Architecture – The size of the LAN (the number of user nodes) and the topology of the LAN should be specified.
1. Discuss to what extent the LAN needs to be fault tolerant (e.g., when a workstation fails).
2. Discuss to what extent the LAN needs to be scalable (i.e., can new user nodes be added without degrading system performance?).
3. Discuss to what extent the main device software needs to be computationally selfsufficient or distributed.
### D. Network Operating System (NOS) – Whether OTS or proprietary, this selection
should consider the trade-off between robustness and flexibility.
### E. Data Integrity – One of the most important issues for any medical device operating in a
network is data integrity. The manufacturer should ensure that the network system software and hardware incorporate error checking, handling, and correction measures as determined by a cybersecurity risk assessment.
1. Transmission of data packets and files should include error detection and protection measures, such as digital signatures or cryptographic integrity checks.
2. Transaction rollback after non-committed changes or network failure, supports data integrity in medical device LANs.
3. Critical data and files may be stored in duplicate at separate locations.
### F. Network Management and Security – User authorization and authentication
should precede accesses to sensitive patient information.
The above five items are not independent. Decisions made in one item area may affect the performance of the LAN in another area.
(2)
Implementation
The speed required by the medical device system dictates the hardware selection, the network interface cards and transmissions protocols. For example, if the conventional Ethernet protocol is too slow for the intended application, then a different transmission protocol will be needed.
Simplicity of the LAN architecture versus fault tolerance is a trade-off that may arise in the implementation of the networked medical device systems. The LAN could be implemented as a linear bus network (perhaps the simplest scheme), but if any connecting link on the bus fails, the whole network can fail. A star topology with redundant centralized hub is an example of a more complex but more robust network structure.
Segmentation of high bandwidth applications may be employed to improve LAN performance.
Limiting the data traffic to data intensive clusters reduces traffic throughout the overall LAN.
### D. Innovative Technologies
FDA recognizes OTS Software can perform advanced functions, which may involve the use of innovative technologies, such as artificial intelligence and machine learning. Relevant recommendations regarding the use of these advanced functions and their unique considerations will continue to evolve and become available through FDA guidance. The latest FDA guidance documents are available on FDA webpages, such as the Digital Health Center of Excellence’s Guidances with Digital Health Content.30
Appendix B: Examples
Examples of medical devices using OTS software are described in this section. This list of examples is intended to illustrate the reasoning that leads to determining Documentation Level for a medical device and the corresponding OTS documentation recommended in a premarket submission. Please note that these generalized examples do not necessarily account for every possible detail, risk, or consideration a sponsor should evaluate. These examples do not define the appropriate Documentation Level for a particular device type or the corresponding OTS documentation to be included in a premarket submission. The rationales in the examples below are abbreviated and FDA encourages sponsors to provide a detailed assessment that accounts for the specifics of their device, including its corresponding OTS.
(1)
A traumatic brain injury (TBI) eye movement assessment aid Description: The device is a prescription device that is intended to track a patient’s eye movements using a commercial OTS mobile phone and camera and analyze the tracked eye movements to aid in the assessment of mild TBI, commonly known as “concussion.” The device provides a positive or negative indicator about the presence of eye movements that are consistent with mild TBI.
Example OTS Software: An OTS operating system on the mobile platform.
OTS Software Documentation: A failure or latent flaw of the device software function(s) would not present a hazardous situation with a probable risk of death or serious injury to either a patient, user of the device, or others in the environment of use, prior to the implementation of risk control measures. The device is intended for use as an aid in the assessment of mild (nonsevere) injury and is not intended as a standalone diagnostic. Therefore, since the device has a
Basic Documentation Level,31 the OTS Software Documentation will follow the Basic Documentation Level in this guidance.
(2)
A device software function on a commercial OTS head-mounted display (e.g., augmented reality/virtual reality/mixed reality (AR/VR/MR)) that superimposes pre-surgical images on a patient’s body Description: The device is intended to provide real-time superimposition of medical images on the patient during a surgical procedure, but is neither intended to directly guide surgical planning or procedures nor be worn by the lead surgeon.
Example OTS Software: An OTS on-board processing and operating system.
OTS Software Documentation: A failure or latent flaw of the device software function(s) would not present a hazardous situation with a probable risk of death or serious injury to either a patient, user of the device, or others in the environment of use prior to the implementation of risk control measures, since the device is neither intended to directly guide surgical planning or procedures nor be worn by the lead surgeon. Therefore, since the device has a Basic Functions, available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/contentpremarket-submissions-device-software-functions.
Documentation Level,32 the OTS Software Documentation will follow the Basic Documentation Level in this guidance.
(3)
A retinal diagnostic software device Description: The device is limited to prescription use and incorporates an AI/ML-enabled algorithm that is intended to evaluate images for diagnostic screening to identify retinal diseases or conditions.
Example OTS Software: OTS cloud-based platforms and operating systems on local computers.
OTS Software Documentation: A failure or latent flaw of the device software function(s), such as a diagnostic algorithm failure that provides a false result, could present a hazardous situation with a probable risk of death or serious injury to the patient prior to the implementation of risk control measures. Therefore, since the device has an Enhanced
Documentation Level,33 the OTS Software Documentation will follow the Enhanced Documentation Level in this guidance.
Functions, available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/contentpremarket-submissions-device-software-functions.
Functions, available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/contentpremarket-submissions-device-software-functions.

---

## Footnotes

[^4]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/changes-existing-medical- software-policies-resulting-section-3060-21st-century-cures-act.

[^5]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/content-premarket- submissions-device-software-functions.

[^6]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/multiple-function-device- products-policy-and-considerations.

[^7]: See footnote 5.

[^10]: See 21 CFR 801.4.

[^11]: See footnote 5.

[^12]: See footnote 5. should be updated to reflect the change. 2.  What are the Computer System Specifications for the OTS Software?

[^13]: See footnote 5. associated with the OTS Software. ·

[^15]: See footnote 5. discussed in the guidance titled “Content of Premarket Submissions for Device Software

[^16]: For additional information on unresolved software anomalies, please refer to the FDA guidance titled “Content of

[^18]: Available at https://www.fda.gov/medical-devices/premarket-approval-pma/master-files.

[^19]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/deciding-when-submit- 510k-change-existing-device.

[^20]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/deciding-when-submit- 510k-software-change-existing-device.

[^21]: For more information on changes during clinical study please see FDA Guidance titled Changes or Modifications

[^22]: See 21 CFR 812. institutional review board (IRB) and patient informed consent. For significant risk studies, the initial user testing (beta testing) protocol would be included in an IDE submission. For example, beta testing of radiation treatment planning software, including any OTS software modules, would be conducted under a full IDE with FDA approval as a prerequisite. See the guidance on “Significant Risk and Nonsignificant Risk Medical Device Studies”23 for more information.

[^23]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/significant-risk-and- nonsignificant-risk-medical-device-studies.

[^24]: See 21 CFR 860.7.

[^26]: For more information, please see the FDA guidance Content of Premarket Submissions for Device Software

[^27]: Available at https://www.fda.gov/medical-devices/overview-device-regulation/device-labeling.

[^28]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/device-labeling- guidance-g91-1-blue-book-memo.

[^29]: Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/labeling-regulatory- requirements-medical-devices-fda-89-4203. OTS Software labeling should indicate the minimum hardware platforms on which the software is validated to run (e.g., processor, memory, interface). The appropriate testing for the user to assure proper installation should also be described in the labeling.

[^30]: Available at https://www.fda.gov/medical-devices/digital-health-center-excellence/guidances-digital-health- content.

[^31]: See Example #6 in Appendix A of the FDA Guidance Content of Premarket Submissions for Device Software

[^32]: See Example #11 in Appendix A of the FDA Guidance Content of Premarket Submissions for Device Software

[^33]: See Example #25 in Appendix A of the FDA Guidance Content of Premarket Submissions for Device Software

<!-- fulltext-end -->
