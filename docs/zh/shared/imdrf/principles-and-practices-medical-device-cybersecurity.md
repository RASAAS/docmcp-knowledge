---
title: Principles and Practices for Medical Device Cybersecurity
---

# Principles and Practices for Medical Device Cybersecurity

**文件编号**: IMDRF/CYBER WG/N60FINAL:2020

::: tip 官方来源
[https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity](https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity)
:::

<!-- fulltext-start -->

---

## 全文

# Principles and Practices for Medical Device Cybersecurity

**Document Number**: IMDRF/CYBER WG/N60FINAL:2020

**Source**: [https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity](https://www.imdrf.org/documents/principles-and-practices-medical-device-cybersecurity)

---

**IMDRF/CYBER WG/N60FINAL:2020**

**FINAL DOCUMENT**

****

**Title:** Principles and Practices for**** Medical Device Cybersecurity

**Authoring Group:** Medical Device Cybersecurity Working Group

**Date:** 18 March 2020

Dr Choong May Ling, Mimi, IMDRF Chair

This document was produced by the International Medical Device Regulators Forum. There are no restrictions on the reproduction or use of this document; however, incorporation of this document, in part or in whole, into another document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the International Medical Device Regulators Forum.

Copyright © 2020 by the International Medical Device Regulators Forum.

**Table of Contents**

1.0 Introduction 5

2.0 Scope 5

3.0 Definitions 6

4.0 General Principles 9

4.1 Global Harmonization 9

4.2 Total Product Life Cycle 9

4.3 Shared Responsibility 10

4.4 Information Sharing 10

5.0 Pre-Market Considerations for Medical Device Cybersecurity 10

5.1 Security Requirements and Architecture Design 10

5.2 Risk Management Principles for the TPLC 13

5.3 Security Testing 15

5.4 TPLC Cybersecurity Management Plan 16

5.5 Labeling and Customer Security Documentation 16

5.5.1 Labeling 16

5.5.2 Customer Security Documentation 17

5.6 Documentation for Regulatory Submission 18

5.6.1 Design Documentation 18

5.6.2 Risk Ma+agement Documentation 18

5.6.3 Security Testing Documentation 18

5.6.4 TPLC Cybersecurity Management Planning Documentation 19

5.6.5 Labelling and Customer Security Documentation 19

6.0 Post-Market Considerations for Medical Device Cybersecurity 19

6.1 Operating Devices in the Intended Use Environment 19

6.1.1 Healthcare Providers and Patients 19

6.1.2 Medical Device Manufacturers 20

6.2 Information Sharing 20

6.2.1 Key Principles 21

6.2.2 Key Stakeholders 21

6.2.3 Types of Information 22

6.2.4 Trusted Communication 23

6.3 Coordinated Vulnerability Disclosure 23

6.3.1 Medical Device Manufacturers 23

6.3.2 Regulators 24

6.3.3 Vulnerability Finders (includes security researchers and others) 25

6.4 Vulnerability Remediation 25

6.4.1 Medical Device Manufacturers 25

6.4.2 Healthcare Providers and Patients 27

6.4.3 Regulators 30

6.5 Incident Response 32

6.5.1 Medical Device Manufacturers 32

6.5.2 Healthcare Providers 33

6.5.3 Medical Device Regulators 34

6.6 Legacy Medical Devices 34

6.6.1 Medical Device Manufacturers 35

6.6.2 Healthcare Providers 37

7.0 References 38

7.1 IMDRF Documents 38

7.2 Standards 38

7.3 Regulatory Guidance 39

7.4 Other Resources and References 40

8.0 Appendices 42

8.1 Appendix A: Incident Response Roles (from ISO/IEC 27035) 43

8.2 Appendix B: Jurisdictional resources for Coordinated Vulnerability Disclosure 45

**Preface**

The document herein was produced by the International Medical Device Regulators Forum (IMDRF), a voluntary group of medical device regulators from around the world. The document has been subject to consultation throughout its development.

There are no restrictions on the reproduction, distribution or use of this document; however, incorporation of this document, in part or in whole, into any other document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the International Medical Device Regulators Forum.

# Introduction

The need for effective cybersecurity to ensure medical device functionality and safety has become more important with the increasing use of wireless, Internet, and network-connected devices. Cybersecurity incidents have rendered medical devices and hospital networks inoperable, disrupting the delivery of patient care across healthcare facilities. Such incidents may lead to patient harm through delays and/or errors in diagnoses and/or treatment interventions, etc. 

Stakeholders within the healthcare sector have a shared responsibility regarding medical device cybersecurity. This guidance intends to assist all stakeholders in gaining a better understanding of their role in support of proactive cybersecurity that helps protect and secure medical devices in anticipation of future attacks, problems, or events. 

Convergence of global healthcare cybersecurity principles and practices is necessary to ensure that patient safety and medical device performance is maintained. To date, however, current disparate regulations across governments lack the global alignment needed to ensure medical device cybersecurity.

The purpose of this IMDRF guidance document is to provide general principles and best practices to facilitate international regulatory convergence on medical device cybersecurity. The document is structured as follows: the scope of the document is defined in Section 2 followed by defined terms in Section 3. Section 4 provides an overview of the general principles of medical device cybersecurity, while Sections 5 and 6 provide a number of recommendations for stakeholders regarding best practices in the pre-market and post-market management of medical device cybersecurity. While the pre-market section primarily addresses medical device manufacturers, the post-market section includes recommendations for all stakeholders. 

This is the first IMDRF guidance document to focus exclusively on medical device cybersecurity. However, there are other relevant IMDRF documents which should be noted in terms of general security considerations. IMDRF/GRRP WG/N47 FINAL:2018 provides harmonized Essential Principles that should be fulfilled in the design and manufacturing of medical devices and IVD medical devices[1]. Those essential principles should be considered along with this guidance document throughout the total product life cycle of a medical device. IMDRF/SaMD WG/N12 FINAL:2014 describes the importance of information security with respect to safety considerations in Section 9.3 and illustrates some particular factors which affect the information security of software as a medical device (SaMD). 

# Scope

This document is designed to provide concrete recommendations to all responsible stakeholders on the general principles and best practices for medical device cybersecurity (including in vitro diagnostic (IVD) medical devices). It outlines recommendations for medical device manufacturers, healthcare providers, regulators, and users to: minimize cybersecurity risks that could arise from use of the device for its intended purposes; and to ensure maintenance and continuity of device safety and performance. For the purpose of this guidance, healthcare providers include healthcare delivery organizations.

This document considers cybersecurity in the context of medical devices that either contain software, including firmware and programmable logic controllers (e.g. pacemakers, infusion pumps) or exist as software only (e.g. Software as a Medical device (SaMD)). It is important to note that due to most regulators’ authority over medical device safety and performance, the scope of this medical device cybersecurity guidance is limited to consideration of the potential for patient harm. For example, cybersecurity risks that impact performance, negatively affect clinical operations or result in diagnostic or therapeutic errors are considered in scope of this document. While other types of harm such as those associated with breaches of data privacy are important, they are not considered within the scope of this document. Furthermore, this document acknowledges the importance of cybersecurity for the manufacturer’s enterprise, however, enterprise cybersecurity is not within the scope of this document. For additional best practices related to security of the manufacturer’s enterprise, the NIST Cybersecurity Framework serves as an important resource.

This document is intended to:

  * Employ a risk-based approach to the design and development of medical devices with appropriate cybersecurity protections;
  * Ensure the safety, performance, and security of medical devices and the connected healthcare infrastructure;
  * Recognize that cybersecurity is a shared responsibility among all stakeholders, including but not limited to medical device manufacturers, healthcare providers, users, regulators, and vulnerability finders;
  * Provide recommendations to those stakeholders to aid in minimizing the risk of patient harm across the total product life cycle;
  * Define terms consistently and describe the current best practices for achieving medical device cybersecurity;
  * Promote broad information sharing policies for cybersecurity incidents, threats, and vulnerabilities to increase transparency and to strengthen response.

It is important to note that differences across medical device types and regulatory jurisdictions, may give rise to specific circumstances where additional considerations are required.

# Definitions

For the purposes of this document, the terms and definitions given in IMDRF/GRRP WG/N47 FINAL:2018 and the following apply.

  1. _Asset:_ physical or digital entity that has value to an individual, an organization or a government (ISO/IEC JTC 1/SC 41 N0317, 2017-11-12)
  2. _Attack:_ attempt to destroy, expose, alter, disable, steal or gain unauthorized access to or make unauthorized use of an asset (ISO/IEC 27000:2018)
  3. _Authentication:_ provision of assurance that a claimed characteristic of an entity is correct (ISO/IEC 27000:2018)
  4. _Authenticity:_ property that an entity is what it claims to be (ISO/IEC 27000:2018)
  5. _Authorization:_ granting of privileges, which includes the granting of privileges to access data and functions (ISO 27789:2013)

NOTE: Derived from ISO 7498‑2: the granting of rights, which includes the granting of access based on access rights. 

  1. _Availability:_**** property of being accessible and usable on demand by an authorized entity (ISO/IEC 27000:2018)
  2. _Compensating Risk Control Measure (syn. Compensating Control):_ specific type of risk control measure deployed in lieu of, or in the absence of, risk control measures implemented as part of the device’s design (AAMI TIR97:2019)

NOTE: A compensating risk control measure could be permanent or temporary (e.g., until the manufacturer can provide an update that incorporates additional risk control measures). 

  1. _Confidentiality:_ property that information is not made available or disclosed to unauthorized individuals, entities, or processes (ISO/IEC 27000:2018)
  2. _Coordinated Vulnerability Disclosure (CVD):_ process through which researchers and other interested parties work cooperatively with a manufacturer in finding solutions that reduce the risks associated with disclosure of vulnerabilities (AAMI TIR97:2019)

NOTE: This process encompasses actions such as reporting, coordinating, and publishing information about a vulnerability and its resolution.

  1. _Cybersecurity:_ a state where information and systems are protected from unauthorized activities, such as access, use, disclosure, disruption, modification, or destruction to a degree that the related risks to confidentiality, integrity, and availability are maintained at an acceptable level throughout the life cycle.__ (ISO 81001-1)
  2. _End of Life (EOL):_ Life cycle stage of a product starting when the manufacturer no longer sells the product beyond their useful life as defined by the manufacturer and the product has gone through a formal EOL process including notification to users. 
  3. _End of Support (EOS):_ Life cycle stage of a product starting when the manufacturer terminates all service support activities and service support does not extend beyond this point.
  4. _Essential Performance_ : performance of a clinical function, other than that related to basic safety, where loss or degradation beyond the limits specified by the manufacturer results in an unacceptable risk (IEC 60601-1:2005+AMD1:2012)
  5. _Exploit:_ defined way to breach the security of information systems through vulnerability (ISO/IEC 27039:2015)
  6. _Integrity:_ property whereby data has not been altered in an unauthorized manner since it was created, transmitted or stored (ISO/IEC 29167-19:2016)
  7. _Legacy Medical Device (syn. Legacy Device):_ medical devices that cannot be reasonably protected against current cybersecurity threats
  8.  _Non-Repudiation:_ ability to prove the occurrence of a claimed event or action and its originating entities (ISO/IEC 27000:2018)
  9. _Patient Harm:_ physical injury or damage to the health of patients (Modified from ISO/IEC Guide 51:2014)
  10. _Privacy:_ freedom from intrusion into the private life or affairs of an individual when that intrusion results from undue or illegal gathering and use of data about that individual (ISO/TS 27799:2009)
  11. _Threat:_ potential for violation of security, which exists when there is a circumstance, capability, action, or event that could breach security and cause harm (ISO/IEC Guide 120)
  12. _Threat Modeling:_ exploratory process to expose any circumstance or event having the potential to cause harm to a system in the form of destruction, disclosure, modification of data, or denial of service (Adapted from ISO/IEC/IEEE 24765-2017)
  13. _Update:_ corrective, preventative, adaptive, or perfective modifications made to software of a medical device

NOTE 1: Derived from the software maintenance activities described in ISO/IEC 14764:2006.

NOTE 2: Updates may include patches and configuration changes 

NOTE 3: Adaptive and perfective modifications are enhancements to software. These modifications are those that were not in the design specifications for the medical device.

  1. _Validation:_ confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled (ISO 9000:2015)

NOTE 1: The term “validated” is used to designate the corresponding status.

NOTE 2: The use conditions for validation can be real or simulated.

  1. _Verification:_ confirmation, through the provision of objective evidence, that specified requirements have been fulfilled (ISO/IEC Guide 63)

NOTE 1: The objective evidence needed for a verification can be the result of an inspection or of other forms of determination such as performing alternative calculations or reviewing documents.

NOTE 2: The activities carried out for verification are sometimes called a qualification process.

NOTE 3: The word “verified” is used to designate the corresponding status.

  1. _Vulnerability:_ weakness of an asset or control that can be exploited by one or more threats (ISO/IEC 27000:2018)

# General Principles 

This section provides general guiding principles for medical device cybersecurity, relevant for all stakeholders to consider when developing, regulating, using, and monitoring medical devices. These themes, found throughout this guidance document, are critical to the global improvement of medical device cybersecurity and when followed, are expected to have a positive impact on patient safety. 

## Global Harmonization 

Medical device cybersecurity is an issue of global concern. Security incidents have the potential to threaten the safety of patients in healthcare systems across the world by causing diagnostic or therapeutic errors, by compromising the safe performance of a device, by affecting clinical operations, or by denying patient access to critical care. Convergence of global healthcare cybersecurity efforts is necessary to ensure that patient safety is maintained while encouraging innovation and allowing timely patient access to safe and effective medical devices. All stakeholders are encouraged to harmonize their approaches to cybersecurity across the entire life cycle of the medical device. This includes harmonization across product design, risk management activities throughout the life cycle of the device, device labelling, regulatory submission requirements, information sharing, and post-market activities. 

## Total Product Life Cycle 

Risks associated with cybersecurity threats and vulnerabilities should be considered throughout all phases in the life of a medical device, from initial conception to end of support (EOS). To effectively manage the dynamic nature of cybersecurity risk, risk management should be applied throughout the total product life cycle (TPLC) where cybersecurity risk is evaluated and mitigated in the various phases of the TPLC including but not limited to design, manufacturing, testing, and post-market monitoring activities. 

It is recognized that there is a need to balance safety and security. When incorporating cybersecurity controls and mitigations, it is critical that medical device manufacturers ensure that device safety and essential performance are maintained. 

## Shared Responsibility 

Medical device cybersecurity is a shared responsibility between stakeholders including the manufacturer, healthcare provider, users, regulator, and vulnerability finder. All stakeholders must understand their responsibilities and work closely with other stakeholders to continuously monitor, assess, mitigate, communicate, and respond to potential cybersecurity risks and threats throughout the life cycle of the medical device. 

## Information Sharing 

Cybersecurity information sharing is a foundational principle in the TPLC approach to safe and secure medical devices. All stakeholders are encouraged to adopt a proactive pre- and post-market approach to cybersecurity information sharing. The availability of timely information provides all responsible parties with enhanced capability to identify threats, assess associated risks, and respond accordingly. All responsible stakeholders are therefore encouraged to actively participate in Information Sharing Analysis Organizations (ISAOs) to foster collaboration and communication of cybersecurity incidents, threats, and vulnerabilities that may affect the safety, performance, integrity, and security of the medical devices and the connected healthcare infrastructure. These efforts promote transparency. Coordinated vulnerability disclosure is another information sharing mechanism that is encouraged as a best practice. Furthermore, the ecosystem would benefit from additional development of information sharing policies that would extend beyond manufacturers to include healthcare providers as well as users of medical devices. Regulators are also encouraged to share information with other regulators to help protect and maintain patient safety globally.

# Pre-Market Considerations for Medical Device Cybersecurity

Although medical device cybersecurity should be considered over the total product life cycle, there are important elements that a manufacturer should address during the design and development of a medical device prior to market entry. These pre-market elements include: designing security features into the product; the application of accepted risk management strategies; security testing; provision of useful information for users to operate the device securely; and having a plan in place for post-market activities. For the aforementioned pre-market elements, manufacturers should consider the intended use environment as well as reasonably foreseeable misuse scenarios. The following sections are intended to introduce these concepts and provide recommendations to manufacturers in the pre-market phase of the product’s life cycle. Note that the life cycle activities for medical device software are specified in IEC 62304:2006/AMD 1:2015. 

## Security Requirements and Architecture Design

Proactively addressing cybersecurity threats at the design stage (e.g. through efforts such as threat modeling) can better mitigate the potential for patient harm than engaging in reactive, post-market activities alone. These design inputs can come from various phases across the product’s life cycle, such as from requirements capture, design verification testing, or risk management activities in the pre- and post-market.

Security requirements should also be identified during the requirements capture stage of the life cycle design process. Some security requirements and security risk control measures can be found in AAMI TIR57:2016, IEC TR 80001-2-2, IEC TR 80001-2-8, the ISO 27000 family, and resources published by NIST (e.g. NIST’s Secure Software Development Framework (SSDF), OWASP (e.g. Security by Design principles), and the US Healthcare and Public Health Sector Coordinating Council (HPH SCC) Joint Cyber Security Working Group (JCWG) (e.g. the Joint Security Plan). 

While the following Table 1 is not meant to be an exhaustive list, it outlines some design principles that medical device manufacturers should consider in designing their product. 

**Design Principle**| **Description**  
---|---  
Secure Communications| The manufacturer should consider how the device would interface with other devices or networks. Interfaces may include hardwired connections and/or wireless communications. Examples of interface methods include Wi-Fi, Ethernet, Bluetooth, USB, etc.  
The manufacturer should consider design features that validate all inputs (not just external) and take into account communication with devices and environments that only support less secure communication (e.g., a device connected to a home network or a legacy device).  
The manufacturer should consider how data transfer to and from the device is secured to prevent unauthorized access, modification, or replay. For example, manufacturers should determine: how the communications between devices/systems will authenticate each other; if encryption is required; how unauthorized replay of previously transmitted commands or data will be prevented; and if terminating communication sessions after a pre-defined time is appropriate.  
Data Protection| The manufacturer should consider if safety-related data that is stored on or transferred to/from the device requires some level of protection such as encryption. For example, passwords should be stored as cryptographically secure hashes.  
The manufacturer should consider if confidentiality risk control measures are required to protect message control/sequencing fields in communication protocols or to prevent the compromise of cryptographic keying materials.  
Device Integrity| The manufacturer should evaluate the system-level architecture to determine if design features are necessary to ensure data non-repudiation (e.g., supporting an audit logging function).  
The manufacturer should consider risks to the integrity of the device such as unauthorized modifications to the device software.  
The manufacturer should consider controls such as anti-malware to prevent viruses, spyware, ransomware, and other forms of malicious code of being executed on the device.  
User Authentication| The manufacturer should consider user access controls that validate who can use the device or allows granting of privileges to different user roles or allow users access in an emergency. Additionally, the same credentials should not be shared across devices and customers. Examples of authentication or access authorization include passwords, hardware keys, or biometrics, or a signal of intent that cannot be produced by another device.  
Software Maintenance| The manufacturer should establish and communicate a process for implementation and deployment of regular updates.  
The manufacturer should consider how operating system software, third-party software, or open source software will be updated or controlled. The manufacturer should also plan how to respond to software updates or outdated operating environments outside of their control (e.g. medical device software running on an unsecure operating system version).  
The manufacturer should consider how the device will be updated to secure it against newly discovered cybersecurity vulnerabilities. For example, consideration could be given to whether updates will require user intervention or be initiated by the device and how the update can be validated to ensure it has no adverse effect on the safety and performance of the device.  
The manufacturer should consider what connections will be required to conduct updates and the authenticity of the connection or update through the use of code signing or other similar methods.  
Physical Access| The manufacturer should consider controls to prevent an unauthorized person from accessing the device. For example, controls could include physical locks or physically restricting access to ports, or not allowing access with a physical cable without requiring authentication.  
Reliability and Availability| The manufacturer should consider design features that will allow the device to detect, resist, respond and recover from cybersecurity attacks in order to maintain its essential performance.  

##### Table 1: Select design principles for consideration in medical device design 

Secure development principles are integral to secure device design. Many current software development life cycle models or standards do not incorporate these principles by default. It is important for device manufacturers that develop medical device software to incorporate these security principles into the development of their software. Doing so necessitates that manufacturers take a holistic approach to device cybersecurity by assessing risks and mitigations throughout the product’s life cycle. 

## Risk Management Principles for the TPLC

Sound risk management principles addressing the security and safety domains should be incorporated throughout the life cycle of a medical device. A cybersecurity risk that impacts device safety and essential performance, negatively affects clinical operations, or results in diagnostic or therapeutic errors should also be considered in the medical device’s risk management process. Risk management as described in ISO 14971:2019, and cybersecurity risk management (for example, as described in AAMI TIR57:2016; AAMI TIR97:2019) should be used by the manufacturer to take the following steps as part of their risk management process:

  * Identify any cybersecurity vulnerability;
  * Estimate and evaluate the associated risks;
  * Control those risks to an acceptable level;
  * Assess and monitor the effectiveness of the risk controls; and
  * Communicate risks via coordinated disclosure to key stakeholders.

Figure 1 below shows the security risk management process from AAMI TIR57:2016. This can be a specialized risk management process performed as part of overall risk management, or can be an integral part of the ISO 14971:2019 risk management process with appropriate mapping of vulnerability, threat and other security related terms. See ISO/TR 24971:2020 Annex F for possible mapping.

##### Figure 1: Schematic representation of the security risk management process (with permission from AAMI TIR57:2016.)

With respect to cybersecurity in medical device regulation, risk analyses should focus on assessing the risk of patient harm by considering: ­1) the exploitability of the cybersecurity vulnerability, and 2) the severity of patient harm if the vulnerability were to be exploited. These analyses should also incorporate consideration of compensating controls and risk mitigations.

Risk assessments link design to threat modeling, patient harm, mitigations, and testing. It is therefore important to establish a secure design architecture such that risk can be adequately managed. There are numerous tools and approaches that may be leveraged in this assessment including but not limited to security risk assessment, threat modeling, and vulnerability scoring.

  * **Security Risk Assessment** : Manufacturers should consider cybersecurity risks, threats and controls throughout the product life cycle. Where applicable, cybersecurity requirements should be cross-referenced to specific device cybersecurity threats and vulnerabilities if the requirements are mitigations to identified hazards. 
  * **Threat Modeling** : Threat modeling is a process for identifying, enumerating and mitigating risks from potential threats in the device and system. Specifically, threat modeling includes consideration of risks, including but not limited to risks related to the supply chain (e.g., system components), design, production, deployment (e.g., into a hospital environment) and maintenance. Furthermore, creating sufficiently detailed system diagrams aid in the understanding of how cybersecurity design elements are incorporated into a device which further aids in threat modeling. In generating a threat model and per guidance from OWASP, device manufacturers should consider answering four basic questions as it pertains to cybersecurity:

  1. What are we building?
  2. What can go wrong? (e.g. how could it be attacked)
  3. What are we going to do about that?
  4. Did we do a good enough job?

These questions can be asked in the context of application architecture, operational data flow, or broader system-level threat modeling as appropriate. When determining what can go wrong during threat modeling, manufacturers should consider unintended or malicious misconfiguration of software and hardware (e.g. connecting a device to the Internet that was not designed to do so).

  * **Vulnerability scoring** : Vulnerability scoring provides a way to characterize and assess the exploitability and severity of a cybersecurity vulnerability. Known common vulnerabilities and exposures (CVEs) identified in design and development should be analyzed and evaluated using a consistent vulnerability scoring methodology such as the Common Vulnerability Scoring System (CVSS) or any future widely adopted vulnerability scoring system. Cybersecurity risk, vulnerability scoring, and control measures may be used to inform threat modeling and security risk assessments for new products and other risk assessment tools not specific to cybersecurity (e.g. failure mode and effects analysis (FMEA)). 

In integrating a security risk management process into an existing ISO 14971:2019 risk management process, activities that address security such as threat modeling and vulnerability scoring should be taken into account.

## Security Testing 

At the verification and validation stage in the design and development process, the manufacturer should employ various types of security testing to provide assurance that the code is free of significant known vulnerabilities and that security controls have been effectively implemented. Testing should take into consideration the context of use of the device and its deployment environment. Application of software verification techniques are recommended to ensure that the software complies with the specifications and anomalies are minimized. It is also important to ensure that the medical device is tested for known vulnerabilities that could be exploited. To do this, the medical device should undergo a security assessment process or acceptance check (e.g. software testing, attack simulation, etc.). Security testing is a component of secure development framework and additional granularity regarding testing considerations may be found in the standards and resources provided in Section 5.1. Below are some high-level considerations for medical device manufacturers:

  * Perform target searches on software components/modules for known vulnerabilities or software weakness also during development. For example, periodic security testing can include: static code analysis, dynamic analysis, robustness testing, vulnerability scanning, or software composition analysis. 
  * Conduct technical security analyses (e.g. penetration testing). These include efforts to identify unknown vulnerabilities through fuzz testing, for example; or checks for alternative entry points, e.g. by reading hidden files, configuration, data streams or hardware registers. 
  * Complete a vulnerability assessment. This includes an impact analysis of the vulnerability on other in-house products (i.e. variant analysis), the identification of countermeasures, and the remediation or mitigation of vulnerability. 

## TPLC Cybersecurity Management Plan

As cybersecurity threats will continuously evolve, manufacturers should proactively monitor, identify, and address vulnerabilities and exploits as part of their cybersecurity management plan across the total product life cycle. A plan should be in place in the pre-market stage of product development and ideally maintained throughout the manufacturer’s organization. This plan should address:

  * **TPLC Vigilance** : The proactive monitoring and identification of newly discovered cybersecurity vulnerabilities, assessment of their threat, and appropriate responses. 
  * **Vulnerability Disclosure** : A formalized process for gathering information from vulnerability finders, developing mitigation and remediation strategies, and disclosing the existence of vulnerabilities and mitigation or remediation approaches to stakeholders.
  * **Updates and Remediation** : A plan outlining how software will be updated or how other remediation actions would be applied to maintain ongoing safety and performance of the device either regularly or in response to an identified vulnerability.
  * **Recovery** : A recovery plan for either the manufacturer, user, or both to restore the device to its normal operating condition following a cybersecurity incident. 
  * **Information sharing** : Participation in Information Sharing Analysis Organizations (ISAOs) or Information Sharing and Analysis Centers (ISACs) that promote the communication and sharing of updated information about security threats and vulnerabilities.

## Labeling and Customer Security Documentation

### Labeling 

Labeling communicates to end-users relevant security information, taking into account the relative cybersecurity risk. It should include the following elements:

  * Device instructions and product specifications related to recommended cybersecurity controls appropriate for the intended use environment (e.g., anti-malware software, network connectivity configuration, use of a firewall). 
  * A description of backup and restore features and procedures to regain configurations. 
  * A list of network ports and other interfaces that are expected to receive and/or send data, and a description of port functionality and whether the ports are incoming or outgoing (note that unused ports should be disabled). 
  * Sufficiently detailed system diagrams for end-users.

### Customer Security Documentation

In addition to the instructions for use, the technical documentation written by the manufacturer for installation, configuration of the device, as well as the technical requirements for their operating environments are particularly important for safe and secure use by the user. It should include the following elements:

  * Specific guidance to users regarding the supporting infrastructure requirements so that the device can operate as intended. 
  * A description of how the device is - or can be hardened - using a secure configuration. Secure configurations may include end point protections such as anti-malware, firewall/firewall rules, whitelisting, security event parameters, logging parameters, physical security detection, etc. 
  * Where appropriate, technical instructions to permit secure network (connected) deployment and servicing, and instructions for users on how to respond upon detection of a cybersecurity vulnerability or incident. 
  * A description of how the device or supporting systems will notify the user when anomalous conditions are detected (i.e., security events) where feasible. Security event types could be configuration changes, network anomalies, login attempts, anomalous traffic (e.g., send requests to unknown entities). 
  * A description of the methods for retention and recovery of device configuration by an authenticated privileged user. 
  * Where appropriate, security risks and consequences of changes to the security configuration, or to the use environment A description of systematic procedures for authorized users to download and install updates from the manufacturer.
  * Information, if known, concerning device cybersecurity end of support (see Section 6.6, Legacy Medical Devices). 
  * A Software Bill of Materials (SBOM) to inform and support operators regarding the cybersecurity of commercial, open source, or off-the-shelf software components which are included in the medical device. An SBOM creates the necessary transparency via a list identifying each software component by its name, origin, version and build. SBOMs enable device operators (including patients and healthcare providers) to effectively manage their assets and related risks, to understand the potential impact of identified vulnerabilities to the device (and the connected system) and to deploy countermeasures to maintain the device’s safety and essential performance. Device operators can use the SBOM to facilitate work with the device manufacturer in identifying software that may have vulnerabilities, update requirements, and performing appropriate security risk management. The SBOM also helps inform purchasing decisions by providing prospective buyers with visibility into the components used in applications and determining potential security risk. Manufacturers should leverage industry best practices for the format, syntax and markup used for deployment of the SBOM. Since the SBOM reveals sensitive information about the medical device, its distribution is encouraged through trusted communication channels. It is recognized that manufacturers will determine trusted ways for communicating SBOMs to the operator.

## Documentation for Regulatory Submission

In addition to the activities outlined in the preceding sections, medical device manufacturers should clearly document and summarize their activities related to cybersecurity. Depending on the risk class of the device, the regulator may require this type of documentation to assess the medical device prior to market entry or may request it during the post-market phase of the product’s life cycle. If required for premarket authorization, clear documentation describing the device’s design features, risk management activities, testing, labeling and evidence of a plan to monitor and respond to emerging threats throughout the product’s life cycle in relation to cybersecurity, should be submitted by the manufacturer. The following paragraphs provide further details on each of the above items.

###  Design Documentation

Documentation that describes the device including any interfaces or communication pathways or components (hardware and software), and all design features that were included to mitigate cybersecurity risks relating to patient harm such as those previously outlined in Section 5.1 above (in particular the rationale and assumptions leading to the selection of the measures for access control, encryption, secure updates, logging, physical security, etc.). 

### Risk Management Documentation

Documentation that clearly describes cybersecurity threats and vulnerabilities, an estimation of the associated risks, descriptions of the controls in place to mitigate those risks and evidence to demonstrate that those controls have been adequately tested. Manufacturers should consider risk controls that maximize device cybersecurity while not unduly affecting other safety controls. Specifically, the risk management documents related to cybersecurity that are submitted to the regulator should be clear and use a cybersecurity risk management standard (e.g. AAMI TIR57:2016, AAMI TIR97:2019) for guidance. The outcomes should be aligned with the overall requirements of ISO 14971:2019, to ensure that output can be used as input for the overall risk management. Risk management documents related to cybersecurity can include:

  * Comprehensive risk management documentation, such as a risk management report or security risk management report which should include any threat modeling, and identified cybersecurity threats. 
  * Discussion on any impact of security risk mitigations on the management of other risks.

### Security Testing Documentation

Test reports that summarize all tests performed to verify the security of the device and the effectiveness of any security controls. Details of specific testing, such as cross-referencing software components or subsystems with known vulnerability databases, for example, can be found in Section 5.3 above, however all testing documents should contain: 

  * Descriptions of test methods, results, and conclusions; 
  * A traceability matrix between security risks, security controls, and testing to verify those controls; and 
  * References to any standards and internal SOPs/documentation used.

### TPLC Cybersecurity Management Planning Documentation

A summary of the device’s maintenance plan describing the post-market processes by which the manufacturer intends to ensure the continued safety and performance of the device throughout its life cycle. As described in Section 5.4 above, these planned processes may include: TPLC vigilance, planned or corrective updates, coordinated vulnerability disclosure policies, and information sharing.

### Labelling and Customer Security Documentation

All user documentation that includes relevant information, as outlined in Section 5.5 above, to allow the user to effectively manage risk in the device’s intended environment. 

# Post-Market Considerations for Medical Device Cybersecurity

As vulnerabilities change over time, pre-market controls designed and implemented may be inadequate to maintain an acceptable risk profile; therefore, a post-market approach is necessary in which multiple stakeholders play a role. This post-market approach covers various elements and includes: the operation of the device in the intended environment, information sharing, coordinated vulnerability disclosure, vulnerability remediation, incident response, and legacy devices. The following sections are intended to introduce these concepts and provide recommendations to all key stakeholders in the post-market phase of the product’s life cycle.

## Operating Devices in the Intended Use Environment 

### Healthcare Providers and Patients

#### Cybersecurity best practices to be adopted by healthcare providers

Medical device cybersecurity is a shared responsibility and requires participation of all stakeholders, including healthcare providers. Healthcare providers should consider adopting a risk management process to address the safety, performance, and cybersecurity aspects of medical devices that are connected to their IT infrastructure. The process should be applied at the:

  * Initial development of the IT infrastructure; 
  * Integration of a new medical device into existing IT network; and 
  * Changing of operating systems or IT network or to the medical device itself (software and firmware) with updates or modifications. 

In order to carry out the above-mentioned risk management process, healthcare providers may refer to relevant standards such as: IEC 80001-1, ISO 31000, and the ISO 27000 series in particular ISO 27799 for adoption. The Health Industry Cybersecurity Practices: Managing Threats and Protecting Patients documents may also serve as another resource.

In addition to adopting a risk management system, healthcare providers should also adhere to the following general cybersecurity best practices (which are not meant to be an exhaustive list) to maintain the healthcare provider’s overall security posture:

  * Good physical security to prevent unauthorized physical access to medical device or network access points;
  * Access control measures (e.g. role based) to ensure only authorized personnel are allowed access to network elements, stored information, services and applications;
  * Employ configuration management to identify all current assets and track future configuration changes;
  * Apply the configuration and protection measures as recommended by the manufacturer;
  * Network access control to limit medical device communication;
  * Update management practices that ensure timely security updates; 
  * Malware protection to prevent attacks; and
  * Session timeout to prevent unauthorized access to devices left unattended for extended period.

The implementation of these best practices should be placed in context with the clinical use of the device. For example, adherence to some of these best practices may not be feasible in a medical emergency. Many of the practices above are described in the NIST Cybersecurity Framework.

#### Training/education for all users 

Finally, healthcare providers should take a holistic approach to prevent cybersecurity incidents from occurring in their institutions. As such, they are encouraged to provide basic cybersecurity training to create security awareness and introduce cyber hygiene practices among all users (e.g. doctors, nurses, biomedical engineers, technicians, etc.). This will include training on operating the medical devices in a secure manner (e.g. only connect their devices to secured network) and how to spot and report any anomalous device behavior (e.g. random shutdowns/ restarts, security software disabled). Such training should also be extended to patients if the connected medical devices (e.g. home use devices such as a continuous glucose monitor or portable insulin pump) are intended to be operated by the patients themselves. 

### Medical Device Manufacturers

In addition to the information contained in the product labeling and customer security documentation, manufacturers are encouraged to partner with healthcare providers, distributors, and consumers of their products when possible to ensure optimal deployment and configuration of their devices. 

## Information Sharing 

Information sharing is a vital tool for managing cybersecurity threats and vulnerabilities across multiple sectors of the global economy. Standards and best practices for intelligence and threat sharing have been developed and implemented in sectors outside of healthcare; and medical devices stakeholders are encouraged to adopt proven tools from other sectors to strengthen the security of the medical device ecosystem globally.

Because of the varied access to resources, different methods, and range of maturity levels across stakeholders, there is also a spectrum of valid approaches to information sharing. In addition, cybersecurity best practices continue to evolve and are informed by several factors, including device type, connected infrastructure, organizational size and maturity, and threat level. Therefore, this document does not favour one specific approach over another. Instead, it articulates principles that should be followed regarding information sharing. Examples are not intended to specify requirements, but rather to serve as illustrations.

### Key Principles

  * Information relating to the security of medical devices should be shared with anyone who needs that information to ensure that the medical device in question can be used safely (e.g. users, patients, other manufacturers, distributors, healthcare providers, security researchers, and the public).
  * The information shared should be balanced such that it is meaningful, consumable and actionable for different stakeholders (e.g. information about a more secure chipset could be important across manufacturers, but the information may provide no benefit to end-users of the device).
  * Information should be shared freely and in good faith as appropriate, with the aim of improving patient safety irrespective of commercial interests.
  * Ensure as much as possible, globally consistent information that is shared synchronously across jurisdictions (as appropriate) to enable stakeholders in various jurisdictions to respond accordingly.

### Key Stakeholders 

The medical device sector is regulated and global. Consequently, local or jurisdictional recommendations for information sharing may not be sufficient for a manufacturer who is supplying devices to multiple markets. Strategies for sharing information relating to the security of medical devices need to be global. Stakeholders may therefore need to be involved in multiple networks, recognizing that some networks may be international.

#### Regulators

  * Are key receivers of information related to the security of medical devices, and are often involved in information dissemination. 
  * Should aim to build processes that encourage timely disclosure of information relating to the cybersecurity of medical devices. This includes sharing information amongst regulators to facilitate a globally coordinated response. 

#### Medical Device Manufacturers

  * Should identify, assess, and share vulnerability information irrespective of where this information comes from. Manufacturers are encouraged to share any information that will help the regulator manage expectations and facilitate regulatory requirements.
  * Should aim to synchronize notification of all the regulators where the affected product is distributed to ensure globally consistent information and, if appropriate, a globally aligned response. 
  * Should use plain language, at an appropriate reading level for the intended user, to communicate actionable information regarding medical device cybersecurity vulnerabilities and threats. This may need to include information about the clinical benefits and risks associated with deploying an update, or compensating controls required until the update is available.

#### Healthcare Providers

  * Are often responsible for taking action or facilitating action. They therefore should have access to any information needed to implement a recommendation, and to ensure the protection of their patients.
  * Are also key generators of information because they work with medical devices in the field and can provide feedback regarding which devices have been affected as well as ease/efficacy of implementing the remediation or mitigation in a real-world setting.

#### Users (e.g. clinicians, patients, caregivers, and consumers)

  * Are often the ones making the final choice on whether an update or other correction is actioned. Therefore, they need clear and meaningful information so that they can make an informed decision. 

#### Other stakeholders, including governments and information sharing entities

  * Law enforcement, national security, and other government agencies may need to share medical device cybersecurity threat and vulnerability information across various parts of government to protect healthcare and other critical infrastructure. 
  * Entities that collect or share information, or provide security advice or expertise can also be important sources of security information as well as support resources. These may be government or private organizations. Examples include information sharing networks (e.g. ISAOs, ISACs), dissemination agencies (e.g. Computer Emergency Response Teams (CERTs)), and others. These stakeholders likely differ between jurisdictions and markets.

### Types of Information 

Cybersecurity vulnerabilities can pose threats to multiple product components, including software and hardware, and first-party or third-party components. In order to protect patients from harm, information shared might include, but is not limited to:

  * Information about products that are affected by a vulnerability and how they are affected; 
  * Information about vulnerabilities of components that are used in other products;
  * Information about IT equipment that may impact the security of medical devices;
  * Information about attacks, potential attacks, and availability of exploit code;
  * Confirmation of incidents (e.g., “Are you seeing this too?”);
  * Availability of patches and other security mitigations such as compensating controls; and
  * Additional instructions on the use and integration of medical devices as an interim measure

Information sharing should also include practices and methods that may mitigate threats, for example, how IT equipment can be configured to mitigate a vulnerability that impacts a medical device, or methods for responding to known exploits.

### Trusted Communication

Information sharing networks should be set up with the understanding, a written agreement if necessary, that information is shared to improve security and patient safety, and shared information is not to be used to gain a commercial advantage. One way to encourage information sharing is to offer anonymized sharing.

## Coordinated Vulnerability Disclosure 

Transparency is an essential building block in cybersecurity because it is difficult to secure what is not known. One mechanism that enhances transparency is coordinated vulnerability disclosure (CVD). CVD establishes formalized processes for obtaining cybersecurity vulnerability information, assessing vulnerabilities, developing mitigations and compensating controls, and disclosing this information to various stakeholders—including customers, peer companies, government regulators, cybersecurity information sharing organizations, and the public. 

Adopting CVD policies and procedures is a proactive approach that enables end users of impacted technologies to make more informed decisions regarding actions that they can take to better protect their medical devices, Health IT infrastructure, and patients. 

Engaging in CVD is a responsible course of action for raising awareness to security issues and**** should be viewed as a sign of a manufacturer’s maturity related to continuous quality improvement and risk management, as is noted in other industry sectors. 

Though a forward-leaning stance with respect to CVD is a sign of proactive and responsible corporate behavior, there have been several unfortunate instances of medical device manufacturers facing negative publicity as a consequence of adopting this best practice. As a best practice, CVD should be undertaken as a norm rather than as an exception and medical device stakeholders are encouraged to ask manufacturers about their CVD policies to further catalyze adoption.

### Medical Device Manufacturers

As the medical device ecosystem continues to mature, the benefits of behaving in a transparent manner will be more fully recognized. Disclosure of this type is of extreme importance by pre-emptively protecting the public from potential harm across multiple marketed products that may be impacted by the same vulnerability. Manufacturers also benefit directly from transparent behavior as it enables improved security design for new products. Healthcare providers and patients should be made aware that CVDs from manufacturers and through computer response teams such as CERTs and Computer Security Incident Response Teams (CSIRT) or government regulators are authoritative sources of information regarding vulnerabilities. There may be jurisdictional differences regarding if, how, and when the regulator communicates as a part of CVD. However, manufacturers are expected to develop and distribute information through customer bulletins, notifications, or other means in a timely manner after the matter has been assessed. Manufacturers should be aware of specific jurisdictional requirements regarding timely communications. 

No software-enabled medical device is completely free of vulnerabilities and as such, engaging in CVD should be a part of routine practice. It is not the number of vulnerabilities that serves as an indicator of a manufacturer’s cybersecurity posture, but rather the consistency and timeliness with which it responds. Therefore, CVD should be part of manufacturers’ proactive approach to medical device cybersecurity because it aids in improving patient health and safety. As it relates to a proactive CVD, manufacturers should:

  * Monitor cybersecurity information sources for identification and detection of cybersecurity vulnerabilities and risk.
  * Adopt a coordinated vulnerability disclosure policy and practice (ISO/IEC 29147:2014: Information Technology – Security Techniques – Vulnerability Disclosure). This includes acknowledging receipt of the initial vulnerability report to the vulnerability finder within a specified time frame.
  * Establish and communicate processes for vulnerability intake and handling (ISO/IEC 30111:2013: Information Technology – Security Techniques – Vulnerability Handling Processes). These processes are clear, consistent, and reproducible irrespective of the originating source of the vulnerability (e.g. security researcher or healthcare provider, etc.).
  * Assess reported vulnerabilities according to established security (e.g. CVSS) and clinical (e.g. ISO 14971:2019) risk assessment methodologies.
  * Develop a remediation if possible. If not possible, develop appropriate vulnerability mitigation and/or compensating controls with established means of reporting deployment failures and rolling back changes.
  * Engage with regulators when required so that they have awareness of forthcoming vulnerability disclosures.
  * Communicate a description to stakeholders of the vulnerability including scope, impact, risk assessment based on the manufacturer’s current understanding and describe the vulnerability mitigations and/or compensating controls. Stakeholders should also be updated as the situation changes.

In addition to its own customer communications, manufacturers are encouraged to coordinate disclosure of their vulnerabilities globally. Computer Emergency Response Teams (CERTs) and equivalent organizations often work collaboratively with the vulnerability finder and the manufacturer throughout the CVD process. In particular, CERTs often play a role in public disclosure via global and regional CERT advisories translated into local languages. For more information regarding CVD, please see the CERT® Guide to Coordinated Vulnerability Disclosure.

### Regulators 

Regulators can help support coordination of vulnerability assessment/evaluation, impact analysis, and mitigation/remediation process between the manufacturer and the vulnerability finder, which ultimately can then drive towards more timely communication to the public in order to mitigate risk of exploit. This communication includes concurrent global communications as appropriate since CVD is recognized as a best practice.

### Vulnerability Finders (includes security researchers and others)

Vulnerabilities, when discovered, should be reported either directly to the relevant manufacturer or to a coordinating third party, such as an appropriate government entity. The manufacturer then coordinates and communicates with the finder of the vulnerability throughout its assessment and remediation. Finally, the vulnerability finder and manufacturer should coordinate in disclosing the vulnerability publicly. As adopted from the National Telecommunications and Information Administration (NTIA) / US Department of Commerce, Vulnerability Disclosure Attitudes and Actions: A Research Report from the NTIA Awareness and Adoption Group (December 2016), as long as the manufacturer is responsive to the finder and there is no evidence of an attack using the vulnerability in the wild, coordinated disclosure means that the finder of the vulnerability does not disclose it until a fix or other mitigation is available. If the finder discloses the vulnerability ahead of a fix, then the finder and manufacturer should at least coordinate in describing a full range of possible mitigations, putting users, including healthcare providers and/or patients, in the most empowered position to operate their devices safely and securely. 

## Vulnerability Remediation

Actions associated with vulnerability remediation are essential to reducing the risk of patient harm. Remediations may include a wide-range of actions including patient notifications. As such, several stakeholder groups play critical roles in this process and these roles are described in greater detail below.

### Medical Device Manufacturers

#### Risk Management 

The first part of any response to a cybersecurity vulnerability in a medical device is risk assessment. Risk management outlined in ISO 14971:2019 is a well-established and mature practice in the medical device sector. This practice should be applied to evaluating the cybersecurity risk of a vulnerability, and then to determine patient safety impact by manufacturers and regulators alike by establishing a cybersecurity risk management process linked to risk management. A remediation strategy that is well-grounded in the context of patient safety can then be developed and agreed upon. To drive the effectiveness of this approach, information should be shared between regulators and manufacturers, especially with regard to perceived risk and justification of action as is appropriate. Since the outcome of risk assessment informs prioritization and timing of remediation, manufacturers and regulators are unlikely to agree on an appropriate remediation strategy if their respective perception of risk differ significantly. 

Manufacturers and regulators also need to take into account the risk perceived by other stakeholders who may be less familiar with risk management, quality management and regulation. This can lead to different expectations about how the manufacturer should respond to a security vulnerability and within what timeframe. Similarly, some stakeholders may not understand risk reduction mechanisms, such as compensating controls, that can be deployed to sufficiently protect a vulnerable device, hence mitigating risk of patient harm to an acceptable level. Inaccurate information that overplays the risk to patients can create a crisis of confidence in healthcare technologies.

All stakeholders need to recognise that, like other risk related to medical devices, cybersecurity vulnerabilities are managed commensurate with the risk they represent to patients and users. 

#### Third Party Components 

Third party components are a key part of the medical device supply chain, whether they are software or hardware. These components can create risk of their own, which is managed by the manufacturer through risk management, quality management, and design choice. Manufacturers should manage the cybersecurity implications of their software and hardware components. Similarly, post-market issues with a third party component may also affect the security of the medical device, and manufacturers need to manage this risk. Users expect the manufacturer to understand how a security vulnerability in an underlying component such as an operating system or processor affects the medical device. 

The response of manufacturers to a vulnerability in a third party component should be the same as for first party vulnerabilities, namely, ongoing risk management and sharing of information with customers and users. While manufacturers are unlikely to have control over the timing of resolution for a third party vulnerability (e.g., availability of an update), they are still expected to take measures to reduce risk to patients and users.

#### Communication 

As discussed in other sections of this document, clear and concise communication to those that need information to manage risk is vital. Moreover, there should be some awareness of the level of technical expertise of those managing risk. Communication should include the following key information: timeline for vulnerability resolution (e.g., when will a fix be available); mechanism for resolution (e.g., how will patch deployment occur); vulnerability score such as a CVSS score; exploitability index (e.g., low skill level) and method (e.g., remote) and interim risk mitigating measures (e.g., what actions should be taken, including use of compensating controls, while awaiting the more permanent resolution).

#### Remediation Action 

Stakeholders’ actions will depend upon multiple factors including the type of device, the regulatory jurisdiction, the risk to users/patient safety, and the intended purpose. Therefore, this document does not elaborate upon specific action that is expected for all devices. There are, however, principles that should underlie all vulnerability remediation actions:

  * Compliance with local regulatory requirements;
  * Adherence to the principles of safety and essential performance;
  * Information sharing with stakeholders to reduce the risk to patients and users; 
  * Cooperation of stakeholders to achieve the agreed remediation; and
  * Timely remediation, relative to the risk.

When the device lacks sufficient fundamental or inherent protective measures, and updates are not feasible, risk-mitigating alternatives should be applied as compensating controls. Examples may include installing a firewall between device and medical IT-network, or removing the device from the medical IT-network. These compensating controls are generally implemented by the healthcare provider based on the information provided by the manufacturer.

Regulators operate under their jurisdiction’s legislation, which means that they may impose particular requirements before remediation can be applied to medical devices in their market. Manufacturers need to consider this when planning vulnerability remediation actions. Regulators should be informed early on so as not to impede or delay the manufacturer’s remediation activities from proceeding. Early notification to regulators allows ample time to initiate any regulatory processes or required actions while concurrently supporting expedient remediation and assisting in managing stakeholders and their expectations (e.g. users, media, public). 

Information about security vulnerabilities travels rapidly in a global economy and exploits of security vulnerabilities can reach around the globe in seconds. Consequently, a global and coordinated strategy to remediate vulnerabilities is needed. If a vulnerability is corrected and disclosed in one jurisdiction, but remains unaddressed in another, it can give an adversary an advantage and leaves patients, as well as the healthcare sector at large, exposed to attack.

Manufacturers who supply to multiple markets are expected to coordinate the release of information and remediation to minimize timing gaps. The manufacturer’s coordination should extend to proactive communication with all of the regulators where affected product is in distribution.

All stakeholders need to recognise that immediate updating may not be possible, or desirable, and that interim measures may be critical to ensuring patient safety. This is particularly important where those measures must be implemented by stakeholders outside of the direct control of the manufacturer or the regulator. For example, some actions can only be taken by a hospital IT department. Successful execution of remediation strategies is often dependent upon effective information sharing and stakeholder management (including users and media). It is important to note that remediation, though ideal, may not always be possible and in that instance appropriate risk mitigations and compensating controls should be applied. 

### Healthcare Providers and Patients

#### Updates

Patients receive medical care in professional healthcare facilities and in the home healthcare environment, and each use environment is associated with unique considerations for updating.[2] In the home healthcare environment, for example, the user can be the patient, caregiver, trusted neighbor, or a family member. This section provides general guidance for updating and subsequent sections describe specific considerations for each use environment.

Subclause 6.2.5 of IEC 62304:2006 +AMD1:2015, Medical device software — Software life cycle processes, requires manufacturers to inform users and regulators about any problem in released medical software and how to obtain and install changes. Specific users of a medical device, as identified by the manufacturer and approved by the local regulatory authority, are expected to implement updates provided by a manufacturer in accordance with associated installation instructions. These users should follow manufacturer guidance to access service bulletins and other information typically provided on a web page. 

When an update cannot be applied within a reasonable time frame, the manufacturer may recommend compensating controls (e.g., segmentation of a medical IT-network) or changes to user-programmable settings of the medical device. To reduce the risk of patient harm for certain types of vulnerabilities, the local regulatory authority may direct the manufacturer to disable specific functionality of the medical device, accessories, or the supporting ecosystem (e.g., software update servers). In either case, users should follow manufacturer guidance and, as appropriate, assess risks associated with their use environment.[3]

Table 2 is adapted from patching methods documented in the Joint Security Plan.[4] The rightmost column of the table describes the primary responsibility of the user identified to implement a medical device manufacturer-approved update.

**Update method**| **Summary description**| **User responsibility**  
---|---|---  
Remote update| Updates applied via secure authorized remote service and support platforms provided by the manufacturer.| Ensure remote connectivity in accordance with instructions provided by the manufacturer.  
User administered| Approved updates are available for customer retrieval and installation from a designated source including direct download from the third-party that provides the product or component.| Retrieve and install the update in accordance with instructions provided by the manufacturer.  
Service visit| Local service facility administers cybersecurity updates (includes on-site servicing). Note, this method is applicable in cases where faulty updating has foreseeable and serious harm and local service personnel may be required for resolution.| Provide the medical device to a service facility, support an on-site service visit, or travel to a professional healthcare facility.  

##### Table 2: Update methods and user responsibility for implementation

Note, for service visits, the user is responsible for interacting with a qualified professional for update installation.

#### Considerations for the healthcare facility environment

In healthcare facilities, patients are provided care by qualified healthcare professionals (e.g., nurses, physicians) who may be licensed or unlicensed as a function of local regulatory requirements. Patients are expected to follow instructions provided by healthcare providers, including those pertaining to security, to ensure safe and effective operation of their medical device. 

Subclause 3.2 of IEC 80001-1:2010, Application of risk management for IT Networks incorporating medical devices — Part 1: Roles, responsibilities and activities, describes risk management responsibilities of the “responsible organization” including maintenance of medical devices deployed in a medical IT-network. The responsible organization can be different than the patient’s immediate healthcare provider. Updating is one type of risk control measure and subclause 4.4.4.3 provides specific guidance:

_“Risk control measures within the medical device should only be implemented by the medical device manufacturer or by the responsible organization following the instructions for use or with the documented permission of the medical device manufacturer. … Any changes to a medical device undertaken by the responsible organization without documented consent of the medical device manufacturer are not recommended.”_

These recommendations were developed to ensure efficient and safe management of medical IT-networks. Lay persons should not be permitted to install updates for medical devices that are connected to medical-IT networks. 

As highlighted in IEC 80001-1, responsibility agreements are one option to ensure that all parties understand the shared responsibility of managing devices in a medical IT-network. If a manufacturer is directed to disable certain functions of the medical device, then healthcare providers should evaluate their clinical workflow to ensure patient safety is maintained.

#### Considerations for the home healthcare environment

The home healthcare environment accommodates a diverse set of potential users as noted in FDA’s related guidance, Design Considerations for Devices Intended for Home Use:

_“The users of home use devices are different from the health care professionals who typically operate medical devices in a professional health care facility. Home users can have a large range of physical, sensory, and cognitive capabilities and disabilities, and emotional differences that should be considered in your home use device design.”_

The applicability of updating methods for the home healthcare environment is a function of many factors including medical device risk classification, resource requirements (e.g., high-speed internet connection), and usability. Due to the wide range of user capabilities, many home use devices require the “service visit” update method listed in Table 1. Update installation for an implanted medical device may require in-person interaction with the patient’s healthcare provider.

Some home use devices, especially those categorized as SaMDs, accommodate the remote update or user administered patching methods. Remote updates require the least amount of user interaction but often necessitate patient consent in accordance with processes established by the healthcare provider. With either update method, patients should follow instructions provided by their healthcare provider and, as applicable, the medical device manufacturer.

If a patient intends to travel internationally, then they should speak with their healthcare provider or the medical device manufacturer to understand software maintenance options for their device.

### Regulators

#### Post-market Updates 

Threat actors are constantly adapting and advancing exploitation techniques. As a result, frequent software maintenance activities are often required to enhance a device’s cybersecurity resilience (“cyber hygiene”), remediate vulnerabilities, or mitigate risk for vulnerabilities that cannot be remediated. If each change made “solely to strengthen cybersecurity” were subjected to the highest level of regulatory review, then the resulting review burden would soon overload most regulatory authorities.

In the context of cybersecurity, the regulatory authority should establish two fundamental questions to determine if a software change requires approval prior to release:

  1. Is the change intended to solely strengthen cybersecurity and has been determined to not have any other impact on the software or device?

The manufacturer should evaluate their system to ensure that such changes do not impact the safety or performance of the device by performing necessary analysis, verification, and/or validation. If a manufacturer becomes aware of any incidental or unintended impacts of the change on other aspects of the software or device, then the regulatory authority may determine that review of the proposed modification, pre-deployment, is appropriate.

  1. Is the change intended to remediate or reduce the risk of a vulnerability associated with unacceptable residual risk related to patient harm?

Post-market vulnerability risk assessments should be based on an evaluation of exploitability and the severity of potential patient harm and is used to determine whether residual risk is acceptable or unacceptable. Note, the definition of “patient harm” is a subset of “harm” as defined in ISO 14971:2019, Medical devices — Application of risk management to medical devices.[5] The narrow definition of patient harm has the net effect of prioritizing regulatory review of those changes necessary to protect public health. 

Table 3 presents a recommended framework for regulators to consider when considering the regulatory oversight required for the various types of software maintenance activities. It is acknowledged that the levels presented in this table are not prescriptive, but provide a guide to the recommended relative levels of regulatory oversight. 

**Purpose of Update**| **Proposed level of Regulatory Requirements**| **Examples**  
---|---|---  
Enhances security (“cyber hygiene”)| Low| A Software as a Medical Device (SaMD) application (“app”) manufacturer is informed of a host operating system update that adds security controls to support a defense-in-depth strategy. The SaMD app requires modification to be compatible with low-level interface changes in the host operating system. The associated SaMD app modifications are not related to any known vulnerability.  
Vulnerability remediation or risk reduction strategy for vulnerabilities that cannot be remediated| Acceptable residual risk of patient harm| Medium| A device manufacturer receives a user complaint that a blood gas analyzer has been infected with malware and there was concern that the malware may alter the data on the device. The outcome of a manufacturer investigation and impact assessment confirms the presence of malware and finds that the malware does not result in the manipulation of unencrypted data stored and flowing through the device. The device’s safety and essential performance is not impacted by the malware and the manufacturer’s risk assessment determines that the risk of patient harm due to the vulnerability is acceptable.**[6]**  
Unacceptable residual risk of patient harm| High| A manufacturer is made aware of open, unused communication ports. The manufacturer acknowledges receipt of the vulnerability report to the vulnerability finder and subsequent analysis determines that the device’s designed-in features do not prevent a threat from downloading unauthorized firmware onto the device, which could be used to compromise the device’s safety and essential performance. Although there are no reported serious adverse events or deaths associated with the vulnerability, the risk assessment concludes the risk of patient harm is unacceptable.**[7]**  

##### Table 3: Software updates and recommended level of regulatory oversight

If the proposed software change affects multiple vulnerabilities, or alternatively improves “cyber hygiene” and affects at least one vulnerability, then the manufacturer should consider the highest applicable level indexed in Table 3 to inform subsequent actions. For example, a single software change could enhance system security, reduce risk for Vulnerability A (acceptable residual risk of patient harm), and remediate Vulnerability B (unacceptable residual risk of patient harm). In this case, the “high” level of regulatory requirements associated with Vulnerability B would apply.

For any level, the regulatory authority may, at their discretion, request evidence that the manufacturer is following established life cycle processes and other regulatory requirements for software maintenance including those identified in IEC 62304:2006/AMD 1:2015.

## Incident Response 

### Medical Device Manufacturers

Medical device manufacturers should prepare for response to cybersecurity incidents and events which may impact their products and customers including patients. As such, manufacturers should establish an incident response management policy which can be scalable and build an incident response team based on its product portfolio. The aim of an incident response team is to provide appropriate capacity for assessing, responding to and learning from cybersecurity incidents, and providing the necessary coordination, management, feedback and communication, for timely and pertinent action during the next incident. 

Preparedness includes establishing an incident management policy, developing detailed incident response plans, building an incident response team, routinely testing and exercising incident response, and continuously improving this capability through lessons learned.

Incident management as defined in ISO/IEC 27035 includes the following at a high-level (see roles and responsibilities section for additional detail): plan and prepare, detection and reporting, assessment and decision, responses and lessons learned (see Appendix A for item description).

#### Roles and Responsibilities 

The incident response team can be divided into the following groups: manager, planning, monitoring, responding, implementation, analysing, and sometimes external experts. Each group has different roles and responsibilities. The team should assign members to these groups based on their skills and knowledge and some of the positions may be filled by more than one team members. The members assigned to the relevant groups should be responsible for the same or similar work. More detailed information on the roles of those groups is provided in Appendix A. 

#### Communication Expectations

Customers should be provided contact information of the medical device manufacturer to report cybersecurity incidents and events, or otherwise submit through regular customer support channels. The incident response team should establish a routine cadence for providing updates to all stakeholders impacted by an incident and work towards delivering customer-targeted communications as soon as possible after an initial discovery (manufacturers should be aware of specific jurisdictional requirements regarding timely communications). Achieving the aforementioned timing for bulletins or notifications by the manufacturer during incidents may be dependent on timely and accurate communication with customers.

Medical device cybersecurity incidents which impact patient safety and privacy must be reported to applicable regulatory agencies as required by regulation. When criminal activity has been identified through the course of investigation, local and applicable law enforcement agencies should be notified. CERTs and ISAOs should be contacted for further coordination on global cybersecurity attacks and events.

### Healthcare Providers

Healthcare providers should establish policies for handling security incidents and mechanisms to mitigate or resolve a security incident and to disclose the related information to internal and external stakeholders. To that purpose, healthcare providers should consider the planning and the resource management for mitigating device vulnerabilities. This could include ensuring that spare or extra devices will be available, as needed, during an incident.

####  Policy and Roles

Vulnerability or security incident handling policy and roles should be in place in a healthcare provider organisation. Those policies should establish the way healthcare providers will receive and disseminate information from manufacturer disclosure documents (e.g. Manufacturer Disclosure Statement for Medical Device Security (MDS2), SBOM, vulnerability/update information), and information sharing institutions or participating ISAOs. To that end, a list of point of contacts must be maintained and verified periodically to inform and be informed. Similarly, service level agreements (SLAs), established before installation and periodically reviewed, provide the substance and terms which manufacturers and other vendors are obligated to fulfil, during or in response to an incident. Healthcare providers are encouraged to establish their own Security Incident Response Team. 

####  Training by Roles

Requirements for training each relevant role should be established and periodically reviewed to determine if they need to be updated. Security experts who evaluate evidence of security incidents should have training in security forensic analysis in addition to practical experience. Those who participate in the incident response process should be trained in that process and the theory of incident response, in addition to practical experience. Training processes should be evaluated periodically and an incident response exercise may be played to perform that evaluation.

####  Analysis and Response

Healthcare providers should evaluate the impact of any incidents or reported vulnerabilities and cooperate with stakeholders including the medical device manufacturer by providing information describing the result of any investigation. When any actions for the resolution are needed, the status of the investigation and its timetable should be included in the result. Healthcare providers should keep patients informed with safety related information including best practices and mitigation measures. When the resolution includes remediation, validation including regression testing must be performed before applying the remediation to the entire facility. Those tests should provide assurance that the remediation does not disrupt existing system functionality. Healthcare providers should update remediation and mitigation information as necessary.

### Medical Device Regulators

Regulators should also be engaged in medical device cybersecurity incident response. As noted in the manufacturers’ response section above, regulators should be notified of cybersecurity incidents so that they are aware, can request additional information for regulatory decision making, and can take additional actions as needed. As appropriate, additional actions may include but are not limited to the assessment of patient safety impact, assessment of the benefit/risk of a manufacturer’s proposed mitigation, communication to stakeholders (including non-traditional stakeholders, e.g. cybersecurity researchers), and engagement with other governmental agencies and regulators. 

## Legacy Medical Devices 

For purposes of this IMDRF guidance, medical devices that cannot be reasonably protected (via updates, and/or compensating controls) against current cybersecurity threats are considered legacy devices. The legacy condition represents an especially complex challenge for the present state of the healthcare ecosystem globally since device cybersecurity may not have been considered in the initial device design and maintenance for many devices in use today. Today’s challenge is further exacerbated by the fact that the clinical utility of a device often outlasts its security supportability as the shift to digital technology within medical devices has offered expanded functionality that could never be realized within older analog devices. While beneficial to patient care, the combination of software, hardware, and network connectivity in these technologies puts new demands on the device lifetime, which often consists of capital equipment (e.g. scanner hardware) as well as commodity components (e.g. servers, workstations, databases and operating systems). It is important to note, however, that device age is not a sole determinant of legacy status. In other words, a device that cannot be reasonably protected against current cybersecurity threats may be less than five years old; irrespective of its age, this device would still be considered legacy. On the other hand, a device may be 15 years old, but if it maintains the capability of being reasonably protected against current cybersecurity threats, it would not be considered legacy. 

As efforts to address the TPLC of medical device cybersecurity starting from the earliest device design and development stage continue to advance, availability of devices that maintain the capability of reasonable protection against cybersecurity threats through its use lifetime will become more and more the norm, and the imbalance observed with respect to the multitude of legacy devices in current clinical use - - posing a security threat to healthcare providers and their networks - - will lessen. The following subsections of this IMDRF guidance articulate a conceptual framework driving towards an optimal future state of medical device cybersecurity where legacy devices (those that cannot be reasonably protected against current cybersecurity threats) are decommissioned/phased out of use, with appropriate advanced notification to healthcare providers to enable business continuity planning. (See Figure 2).

![A screenshot of a cell phone Description automatically generated](data:image/jpeg;base64,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iIgIiICIiD44FzSAS0kcx2LQMldE+G5Nx+qxpuIVVdWzsczXOGjTqN3HbmTbn610BEBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQFW5gwnx9gFdhRqpaVtXC6F00VtTQedr+jb2qyRBqGQOj3Duj+gqqeiqJqmSqkD5ZpgATYWAAHYLn3rb0RAREQEREBERAREQEREBERAREQEREBERAREQEUHEMYocMgdNV1MUUbebnvDQPaVpGIdMGX6VxZA+apI7YYiR7yQrETPJL2dFRcrj6a8LLwH0Vaxvfoaf4ArZMH6ScvYvI2KOuZHK7YRzAxuJ9F9j70mmYLw3BF4jmZK27HXXtRRERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAWjZ6z/TZZp+BAGzV0gvHFfYD853c37Vf5oxyHAMCqa6bcRsJ033ceQb7Tt71+YcRxCpxXEZ66skL55nanH7APQOS3RTdmqbMuLY1iGOVZqcRqXzP/JB2awdzRyCgKVR4dXYgJjRUc9RwWa5OFGXaG95sttoOjDGK/KUuNgujlDXPjonQniSNHaO6+9hb7V2vEOdplpCKXUYXiFJSR1VTQ1MNPI4sZJLEWtcRzAuoio3LKPSFiWXJ44aiSSqw+9jG43fGO9hP2HZfoHCMWpcZw+KspJWyRSN1Nc3tH/rs7F+TFv3RfmqTB8bbhk0n9Eq3WYHHZkvZ7DyPsXOunzhqmryfoRFy6s6Z6agrZ6SowKrbNBIY3jit5grB9/Kh/sSq/etXPRLeqHWEXJ/v5UP9iVX71qffyof7Eq/3rU0VGqHWEXJ/v5UP9iVX71qffyof7Eqv3rU0VGqHWEXJ/v5UP9iVX71qffyof7Eqv3rU0VGqHWEXJ/v5UP8AYlV+9an38qH+xKr961NFRqh1hFyf7+VD/YlV+9an38qH+xKr961NFRqh1hFyf7+VD/YlV+9an38qH+xKr961NFRqh1hFyf7+VD/YlV+9an38qH+xKr961NFRqh1hFoOWelCkzJiElIzD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H93L9ezV6N1E25qZKqKQOBZJTgGw9RI39N1PqMVo699c2pjnjjnkjkY6OznXa3Tvew3Hb3q58gXfXx8CeQLvr4+BKcpmqY0xT9u/uVZzKVTqmv79vZBdXUNdFisrxNHTuip2ADSXgtNr25HkvNLW0c7auK0raSDDuC0kgSO64JNuV7nkrDyBd9eHwJ5Au+vD4F03GavfR8x7z/Ln4jKWtr6eU+0fwp2YtSQiKlYyZ1G2nkge8gCQ6zcuAvbYgbJS4tR0UtDHC2d9PTyvle97QHOc5unYA2AHrVx5Au+vj4E8gXfXx8Cz4bNxN9P27+zU5nJTFtX39/b3a3QVVPDS1tNU8UMqGNAdGAS0tdfkSFAW5+QLvr4+BPIF318fAuU5HMzERNPL3ju6xtDKxMzFXP2ns0xFufkC76+PgTyBd9fHwLP0/M+n5ju19Sy3q+J7NMWei/Hqf9q37VtnkC76+PgXuHIzoZ45fDQdDg62jnYrVGQzEVRM0/Md2a9o5aaZiKviezc0RF+kfmBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREEKf6Wo/wBSX/apqhz/AErSfs5f9qmICIiAiIgIiICIiAiIgIiICIiAiIgIiIPL/wAG71FR8M+iqT9iz7ApLvmO9Si4X9FUn7Fn2IJaIiAiIgIiICIiAiIgIiICIiAiIgIiIChYhu+j/wAQ37HKaodd+Fov8QP5XIJiIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIghz/StJ+zl/2qYoc30rSfspf9qmICIiAiIgIiICIiAiIgIiICIiAiIgIiIPjvmn1KLhn0XS/sm/YpZ5FRML+iqX9k37EEtERAREQEREBERAREQEREBERAREQEREBRKz8PRD+//wBjlLUSr/GqAf35/wCm9BLREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREEOb6Vpf2Un2tUxQ5fpam/YyfaxTEBERAREQEREBERAREQEREBERAREQEREBQ8L+i6X9mFMUPCvoum/ZhBMRR62tpsOo5KurlbFBGLue71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NrdQMb2/KGzw3UAAdt78lBGGVoe14ezU03BMt19dhlc+QyOezWSSTxe9S8dS09EiHDKZtRTtkZUzslDjraNLTs6zeV9XVGy90+DQCKnlmZO4ybGK4ubsc5tjbnty39nJQvFNYAAHRixv+F7U8VVm3XZty+V5JeOpaeiVHhUUzIXHijWyNp4bR8ndpOp/o29HavjcJpXOYBJPsWNfZoNy6MuFrAkC4tffvUbxTWb9aPfY/K80GFVgNw6MH0SpeOpaeiHPEYKiSIixY4tIuDyPeFjU/wAUVXfF+8TxRVf3X7xa109U0z0QEU/xRVf3X7xPFFV/dfvE109TTPRART/FFV/dfvE8UVX91+8TXT1NM9G/Ze/8b9Yq+VFl4bSnsLjur1eN6RERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERBjmiEsZaVz7MWAvimfVUzLjnIwDl+kPQuiqNVUjahvc4ciFqmqaZvCVUxMWcdRbriuXIJXue5joZD+XG27T62/8ACoZMvVYJ4MsEwHc/SfcV6IxKZcJomFQisxgGIk7wsaO90jQPtWaPA44zerrGC3NkHXd/wtTXTHmkUVSq6enlqpmwwsL3u5ALZKXDmmPxbTniF5/pMo5H9EegKVRYfLIzgUUBp4HfOed3v9ZW0YbhcVBEA1o1dpXnrxNXCHamizHR4HR01O1gibsO5SPFdJ5pvuUxFzbQ/FdJ5pvuTxXSeab7lMRBD8V0nmm+5PFdJ5pvuUxEEPxXSeab7k8V0nmm+5TEQQ/FdJ5pvuTxXSeab7lMRBD8V0nmm+5PFdJ5pvuUxEEPxXSeab7k8V0nmm+5TEQQ/FdJ5pvuTxXSeab7lMRBjhgjgFo2gBZERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREHlzGvFnAEKHNhNLN85gU5EFOcvUhO7VIhwakhNxGCfSrBEHlkbIxZrQF6REBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQ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)

##### Figure 2: Legacy device conceptual framework as a function of product life cycle for cybersecurity

### Medical Device Manufacturers

Attention to medical device cybersecurity begins during device design and development, well before commercial release, as depicted in Figure 2. Aligning with the TPLC framework, full support of medical devices to ensure reasonable protection against current cybersecurity threats should continue through the manufacturer’s published cybersecurity End of Life date (EOL). The manufacturer’s cybersecurity EOL date signifies the diminished capacity to provide comprehensive cybersecurity support of the medical device. Upon approaching the cybersecurity EOL, the manufacturer should release a communication to its customers notifying them of the limited support that remains available beyond the EOL, with clear communication of the device’s cybersecurity End of Support (EOS) date. No support should be expected for any medical device past the established cybersecurity EOS date. 

Per this conceptual framework, when a medical device reaches its cybersecurity EOS date, it is considered a legacy medical device that cannot be reasonably protected against current cybersecurity threats and should be decommissioned. The responsibility for maintaining device security and assumption of risk for its ongoing use beyond the EOS date would transfer at this point to the customer, e.g., the healthcare provider. 

It is important to note that while design changes to some devices may not be feasible (e.g. an obsolete operating system that is no longer supported and cannot be patched for security purposes), compensating controls may be able to provide some level of protection. In the presence of available and successfully deployed compensating controls, the medical device would not be considered legacy per this framework. As appropriate, regulators may encourage medical device manufacturers to leverage compensating controls to address present day device security challenges after EOL date, to enable ample time for healthcare providers to conduct business continuity planning for EOS when no further security support is available from the manufacturer. Device design, vulnerability management, and customer communications all play an important role in addressing device cybersecurity challenges. Recommendations for manufacturers as a function of device life cycle stage include the following:

  * Development:
    1. Take into consideration the support life cycle of hardware and software components that comprise the medical device. In order to provide comprehensive support of a medical device, the manufacturer should be able to obtain support from the corresponding hardware and software vendors, by means of software/firmware updates that address quality, performance and security concerns. A manufacturer should anticipate the need to support safety and efficacy of a product throughout its use. The manufacturer should consider that the third-party vendor support for a component may end within the healthcare provider’s projected use life of the device, and this may adversely impact the manufacturer’s ability to support secure operation of the device. 
    2. Design and develop devices under a secure development framework to minimize the number of legacy devices in the future. These devices, at a minimum, should meet a security baseline and include mechanisms for updates and patches. 
  * Support:
    1. Monitor medical devices for vulnerabilities with unacceptable risk and provide a best-effort response and maintain ongoing risk documentation aligned to the total product life cycle of the device as a part of risk management.
    2. Clearly communicate key life cycle milestones, including cybersecurity EOL dates of devices as part of procurement and installation processes - customer responsibilities should be integrated into communications at these time points. 
    3. Notify customers proactively of third-party vendor end of support for device components. 
    4. Release a customer notification that signals ongoing but limited support through the cybersecurity EOS date, beyond which the device would be considered unsupportable and in a legacy state. The timing of this customer communication should occur upon approaching the EOL date and will enable advanced notice for device decommissioning/phase out and business continuity planning for healthcare providers. Clearly communicating helps healthcare organizations understand their responsibilities as well as device risk so that they can plan device retirement and replacement and budget accordingly. 
  * Limited Support (EOL begins here):

  1. Continue to communicate timelines for cybersecurity EOS dates to allow ample time for customers to prepare for EOS and the associated customer responsibilities. 
  2. Continue actions “a” and “c” from the Support life cycle phase above.

  * End of Support (Legacy begins here):

  1. Full transfer of responsibility from manufacturer to customer. Following formal cybersecurity EOS for the device, users of devices should not expect any level of support.

### Healthcare Providers 

Many healthcare providers plan for device use much longer than the communicated life of the device given by the manufacturer in its published cybersecurity EOL. However, as the threat landscape changes over time and new threats emerge, the risk and costs of using outdated technology increases and must be accounted for through a shared responsibility between the medical device manufacturer and the healthcare provider. The following recommendations, as a function of device life cycle stage, are expected to help address healthcare providers’ challenges with medical devices, to plan in advance for a defined cybersecurity EOS date:

  * Support:
    1. Request clear points of contact and communication processes with device manufacturers to ensure product life cycle planning, understanding, and transparency. 
    2. Request an SBOM, as software components with the shortest support life cycle will ultimately affect the supportability and security of those devices. Obtaining an SBOM helps customers better understand those components affecting the device life cycle and can include information for additional hardware for risk control measures such as compensating controls.
    3. Ensure proper support and maintenance of their medical devices while in use, either through the medical device manufacturer, 3rd party service agents or through internal resources and controls. This includes proper support of network security, asset security, identity and access management, and security operations.
    4. Evaluate new and evolving risks within their environment and make every effort to control risks through proper mitigations, including but not limited to network segmentation, user access roles, risk assessment, security testing, network monitoring, etc.
    5. Plan ahead for the manufacturer’s cybersecurity EOS date, so that an unsupported legacy device (potentially jeopardizing patient safety and healthcare network security), can be appropriately phased out and replaced with a securable and supported medical device.
  * Limited Support:
    1. Continue actions “c”, “d”, and “e” under the Support device life cycle phase above
  * End of Support:
    1. Accept responsibility for management of device security and assumption of security risk for its ongoing use beyond the cybersecurity EOS date if unable to decommission the device without impacting continuity of care.

# References

## IMDRF Documents

  1. Software as a Medical Device: Possible Framework for Risk Categorization and Corresponding Considerations IMDRF/SaMD WG/N12:2014 (September 2014)
  2. Essential Principles of Safety and Performance of Medical Devices and IVD Medical Devices IMDRF/GRRP WG/N47 FINAL:2018 (November 2018)

## Standards

AAMI TIR57:2016 Principles for medical device security—Risk management

AAMI TIR 97:2019, Principles for medical device security—Postmarket risk management for device manufacturers

IEC 60601-1:2005+AMD1:2012, Medical electrical equipment - Part 1: General requirements for basic safety and essential performance

IEC 62304:2006/AMD 1:2015, Medical device software – Software life cycle processes

IEC 62366-1:2015, Medical devices - Part 1: Application of usability engineering to medical devices

IEC 80001-1:2010, Application of risk management for IT-networks incorporating medical devices - Part 1: Roles, responsibilities and activities

IEC TR 80001-2-2:2012, Application of risk management for IT-networks incorporating medical devices - Part 2-2: Guidance for the disclosure and communication of medical device security needs, risks and controls

  1. IEC TR 80001-2-8:2016, Application of risk management for IT-networks incorporating medical devices – Part 2-8: Application guidance – Guidance on standards for establishing the security capabilities identified in IEC 80001-2-2

ISO 13485:2016, Medical devices – Quality management systems – Requirements for regulatory purposes

ISO 14971:2019, Medical devices – Application of risk management to medical devices

ISO/TR 80001-2-7:2015, Application of risk management for IT-networks incorporating medical devices – Application guidance – Part 2-7: Guidance for Healthcare Delivery Organizations (HDOs) on how to self-assess their conformance with IEC 80001-1

ISO/IEC 27000 family - Information security management systems

  1. ISO/IEC 27035-1:2016, Information technology – Security techniques – Information security incident management – Part 1: Principles of incident management 
  2. ISO/IEC 27035-2:2016, Information technology – Security techniques – Information security incident management – Part 2: Guidelines to plan and prepare for incident response
  3. ISO/IEC 29147:2018, Information Technology – Security Techniques – Vulnerability Disclosure
  4. ISO/IEC 30111:2013, Information Technology – Security Techniques – Vulnerability Handling Processes

ISO/TR 24971:2020, Medical devices – Guidance on the application of ISO 14971 

UL 2900-1:2017, Standard for Software Cybersecurity for Network-Connectable Products, Part 1: General Requirements

UL 2900-2-1:2017, Software Cybersecurity for Network-Connectable Products, Part 2-1: Particular Requirements for Network Connectable Components of Healthcare and Wellness Systems

## Regulatory Guidance

  1. ANSM (Draft): Cybersecurity of medical devices integrating software during their life cycle (July 2019)
  2. China: Medical Device Network Security Registration on Technical Review Guidance Principle (January 2017)
  3. European Commission: REGULATION (EU) 2017/745 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 5 April 2017 on medical devices, amending Directive 2001/83/EC, Regulation (EC) No 178/2002 and Regulation (EC) No 1223/2009 and repealing Council Directives 90/385/EEC and 93/42/EEC (May 2017)
  4. European Commission: REGULATION (EU) 2017/746 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 5 April 2017 on in vitro diagnostic medical devices and repealing Directive 98/79/EC and Commission Decision 2010/227/EU (May 2017)
  5. FDA (Draft): Content of Premarket Submissions for Management of Cybersecurity in Medical Devices (October 2018)
  6. FDA: Cybersecurity for Networked Medical Devices Containing Off-the-Shelf (OTS) Software (January 2005)
  7. FDA: Design Considerations for Devices Intended for Home Use (November 2014)
  8. FDA: Postmarket Management of Cybersecurity in Medical Devices (December 2016)
  9. Germany: Cyber Security Requirements for Network-Connected Medical Devices (November 2018)
  10. Health Canada: Pre-market Requirements for Medical Device Cybersecurity (June 2019)
  11. Japan: Ensuring Cybersecurity of Medical Device: PFSB/ELD/OMDE Notification No. 0428-1 (April 2015)
  12. Japan: Guidance on Ensuring Cybersecurity of Medical Device: PSEHB/MDED-PSD Notification No. 0724-1 (July 2018)
  13. Singapore Standards Council Technical Reference 67: Medical device cybersecurity (2018)
  14. TGA: Medical device cybersecurity - Consumer information (July 2019)
  15. TGA: Medical device cybersecurity guidance for industry (July 2019)
  16. TGA: Medical device cybersecurity information for users (July 2019)

## Other Resources and References

  1. CERT® Guide to Coordinated Vulnerability Disclosure

<https://resources.sei.cmu.edu/asset_files/SpecialReport/2017_003_001_503340.pdf>

  1. The NIST Cybersecurity Framework

<https://www.nist.gov/cyberframework>

  1. NIST’s Secure Software Development Framework (SSDF)

<https://csrc.nist.gov/CSRC/media/Publications/white-paper/2019/06/07/mitigating-risk-of-software-vulnerabilities-with-ssdf/draft/documents/ssdf-for-mitigating-risk-of-software-vulns-draft.pdf>

  1. Medical Device and Health IT Joint Security Plan (January 2019)

<https://healthsectorcouncil.org/wp-content/uploads/2019/01/HSCC-MEDTECH-JSP-v1.pdf>

  1. MITRE medical device cybersecurity playbook (October 2018)

<https://www.mitre.org/publications/technical-papers/medical-device-cybersecurity-regional-incident-preparedness-and>

  1. MITRE CVSS Healthcare Rubric

<https://www.mitre.org/publications/technical-papers/rubric-for-applying-cvss-to-medical-devices>

  1. Health Industry Cybersecurity Practices: Managing Threats and Protecting Patients (HICP)

<https://www.phe.gov/Preparedness/planning/405d/Pages/hic-practices.aspx>

  1. Open Web Application Security Project (OWASP)

<https://www.owasp.org/index.php/Main_Page>

  1. Manufacturer Disclosure Statement for Medical Device Security (MDS2)  
<https://www.nema.org/Standards/Pages/Manufacturer-Disclosure-Statement-for-Medical-Device-Security.aspx>
  2. ECRI approach to applying the NIST framework to MD

<https://www.ecri.org/components/HDJournal/Pages/Cybersecurity-Risk-Assessment-for-Medical-Devices.aspx>

  1. National Telecommunications and Information Administration (NTIA) / US Department of Commerce, Vulnerability Disclosure Attitudes and Actions: A Research Report from the NTIA Awareness and Adoption Group

<https://www.ntia.doc.gov/files/ntia/publications/2016_ntia_a_a_vulnerability_disclosure_insights_report.pdf>

  1. <https://republicans-energycommerce.house.gov/wp-content/uploads/2018/10/10-23-18-CoDis-White-Paper.pdf>
  2. <https://resources.sei.cmu.edu/asset_files/SpecialReport/2017_003_001_503340.pdf>

# Appendices

## Appendix A: Incident Response Roles (from ISO/IEC 27035)

**Incident management – ISO/IEC 27035**  
---  
Plan and prepare| Establish an information security incident management policy, form an Incident Response Team etc.  
Detection and reporting| Someone has to spot and report “events” that might be or turn into incidents.  
Assessment and decision| Someone must assess the situation to determine whether it is in fact an incident.  
Responses| Contain, eradicate, recover from and forensically analyze the incident, where appropriate  
Lessons learned| Make systematic improvements to the organization’s management of information risks as a consequence of incidents experienced.  
**Incident response team**  
---  
**Roles**| **Responsibilities**| **Main actions**  
Manager| Leads and makes decisions on major issues concerning cybersecurity incident response| a) commitment and support to incident response, including the provision of necessary resources (manpower, financial and material);b) review and approval of incident response policies and plans, and supervision of the implementation;c) review and revision of incident response plans;d) internal and external coordination of the team.  
Planning Group| Operates the incident response| a) establishing and planning security policies;b) implementing security processes;c) adjusting the risk priorities;d) communicating with higher-level organizations and other third-party organizations;e) supporting administration;f) discussing/registering/approving vulnerability reports on the target organizations;g) performing other activities directed by the manager.  
Monitoring group| Performs the real-time security monitoring activities| a) daily monitoring and operation;b) intrusion detection, registering incidents, and first responses;c) performing the security updates;d) implementation of the security policy and backup management;e) help desk;f) facility management;g) performing other activities directed by the manager.  
Responding group| Provides services such as real-time responses, technical support| a) propagating and reporting incidents;b) correlation analysis between monitoring systems;c) incident investigation and recovery supports;d) vulnerability analysis on the target incident;e) performing other activities directed by the manager.  
Implementation group| Performs the total action of the incident response| a) analyzing incident response requirements;b) determining incident response policies and levels;c) implementation of incident response policies and plans;d) projecting incident response plans;e) summarizing the incident response work and report;f) deployment and use of incident response resources;g) performing other activities directed by the manager.  
Analysing group| Performs incident analysis| a) planning vulnerability analysis for the team and manufacture;b) improving the security analysis tools and checklist;c) improving the monitoring rules;d) publication of newsletter;e) performing other activities directed by the manager.  

## Appendix B: Jurisdictional resources for Coordinated Vulnerability Disclosure

**Australia**

CERT Australia

<https://www.cert.gov.au/>

AusCERT

<https://www.auscert.org.au/>

**Brazil**

All Certs in Brazil

<https://www.cert.br/csirts/brazil/>

**Canada**

Canadian Centre for Cyber Security

<https://www.cyber.gc.ca/>

**Europe**

CERT European Union

<https://cert.europa.eu>

**France**

ANSM

<https://ansm.sante.fr/>

<https://www.ansm.sante.fr/Declarer-un-effet-indesirable/Votre-declaration-concerne-un-dispositif-medical/Votre-declaration-concerne-un-dispositif-medical/(offset)/0>

French Ministry of Health and Solidarity

<https://solidarites-sante.gouv.fr/soins-et-maladies/signalement-sante-gouv-fr/>

Shared Health Information Systems Agency

<https://www.cyberveille-sante.gouv.fr/>

ANSSI - National Agency for Information Systems Security

<https://www.ssi.gouv.fr/en/>

**Germany**

CERT Germany

<https://www.cert-bund.de/>

**Italy**

<https://www.csirt-ita.it/>

**Japan**

Japan Computer Emergency Response Team/Coordination Center (JPCERT/CC)  
<https://www.jpcert.or.jp/vh/top.html> or <https://www.jpcert.or.jp/english/>

**Singapore**

SingCERT

<https://www.csa.gov.sg/singcert/news/advisories-alerts>

**United States**

Industrial Control Systems CERT (ICS-CERT)

<https://www.us-cert.gov/ics>

US CERT

<https://www.us-cert.gov/>

  1. Section 5.8 of N47 describes important requirements on information security and cybersecurity such as the protection against unauthorized access. They should be considered along with this guidance document throughout the total product life cycle of the medical device. ↑

  2. IEC 60601-1-11:2015, _Medical electrical equipment — Part 1-11: General requirements for basic safety and essential performance – Collateral Standard: Requirements for medical electrical equipment and medical electrical systems used in the home healthcare environment_ , defines the “home healthcare environment” as “dwelling place in which a patient lives or other places where patients are present, excluding professional healthcare facility environments ...” and includes examples of “In a car, bus, train, boat or plane, in a wheelchair or walking outdoors.” ↑

  3. It is acknowledged that in certain situations, the user cannot appropriately assess risks. ↑

  4. _Medical Device and Health IT Joint Security Plan_ , Healthcare and Public Health Sector Coordinating Council (HSCC), January 2019. Note, the first two columns incorporate minor changes to improve clarity and the “ad hoc” patching method is removed (only validated patches are considered). ↑

  5. ISO 14971:2019 defines “harm” as “physical injury or damage to the health of people, or damage to property or the environment” whereas “patient harm” only includes the first phrase of this definition. ↑

  6. Adapted from examples provided in _Guidance for Industry and Food and Drug Administration Staff, Postmarket Management of Cybersecurity in Medical Devices_. Dec. 2016. ↑

  7. Ibid. ↑


<!-- fulltext-end -->
