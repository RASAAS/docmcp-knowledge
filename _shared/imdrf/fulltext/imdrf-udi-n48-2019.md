# Unique Device Identification system (UDI system) Application Guide

**Document Number**: IMDRF/UDI WG/N48FINAL:2019

**Source**: [https://www.imdrf.org/documents/unique-device-identification-system-udi-system-application-guide](https://www.imdrf.org/documents/unique-device-identification-system-udi-system-application-guide)

---

IMDRF/UDI WG/N48 FINAL: 2019

**Final Document**

**Title** : **Unique Device Identification system (UDI system)**

**Application Guide**

**Authoring Group** : IMDRF UDI WG

**Date** : 21 March 2019

Elena M. Astapenko, IMDRF Chair

This document was produced by the International Medical Device Regulators Forum. There are no restrictions on the reproduction or use of this document; however, incorporation of this document, in part or in whole, into another document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the International Medical Device Regulators Forum.

Copyright © 2019 by the International Medical Device Regulators Forum.

**Table of Contents**

1.0 Scope 5

2.0 References 5

3.0 Definitions 7

4.0 Fundamental Elements of a Harmonized UDI System 8

5.0 Guiding principles for UDI system design and operations 9

6.0 The Unique Device Identifier (UDI) 9

6.1 Content, Structure and representation of a UDI 9

6.2 The UDI carrier 10

6.3 UDI Human Readable Interpretation (HRI) Format, Structure and Content of Each Issuing Agency/Entity 11

6.4 Automatic Identification Data Capture (AIDC) representation of UDI 11

6.5 How to place a UDI carrier on the label of the device or on the device itself 12

6.5.1 Direct Marking 15

6.6 Considerations on the UDI contents of the Medical Device Label 16

6.7 Considerations on AIDC readers 16

7.0 Application of UDI to packaging levels 17

7.1 Applying UDI to Medical Device Package Level Hierarchy 17

7.2 Unit of Use (UoU) DI 17

8.0 The Unique Device Identification Database (UDID) 18

8.1 Expectations for an effective UDID design 18

8.2 UDID Data Specifications 20

8.3 Submission of information to UDID by third-party submitter 21

8.4 UDI-DI triggers 22

9.0 Recording Unique Device Identifiers into forms, databases (other than UDID), registries and other health information 23

10.0 Establishing Responsibility for Creating and Maintaining a UDI System 24

10.1 Regulatory Authority 24

10.2 Manufacturer 25

10.2.1 Own brand or private labellers 25

10.3 Issuing Agency/Entity 26

10.4 Expectations from stakeholders related to UDI 27

10.4.1 Distributors and importers 27

10.4.2 Healthcare providers and retail pharmacies 27

10.4.3 Other stakeholders 28

10.4.4 International standards and terminology development organizations 28

11.0 General Considerations to facilitate an effective UDI Implementation 28

11.1 Transitional period 28

11.2 UDI implementation arrangements 29

12.0 Special cases 29

12.1 Implantable devices 30

12.2 Reusable devices 30

12.3 Non-IVD kits 31

12.3.1 Placement of UDI carrier on the medical device contents of kits 31

12.3.2 Exemption for non-IVD kits 32

12.4 IVD kits 32

12.4.1 Medical device contents of IVD kits 33

12.4.2 Placement of UDI on IVD kits 33

12.5 Configurable medical devices 34

12.6 Software as a Medical Device 35

12.6.1 UDI Assignment Criteria 35

12.6.2 UDI Placement Criteria 35

13.0 Emerging issues with UDI which are not specifically covered by this Guide 36

**Appendix A:** UDI HRI formats to be used for each of the issuing agencies/entities 39

**Appendix B:** AIDC carriers most widely used in healthcare 43

**Appendix C:** Examples of RFID carriers 46

**Appendix D:** Examples of registration of packaging configurations 49

**Appendix E:** Examples of UoU and packaging configurations 50

**Appendix F:** Feasibility issues linked to direct marking integrity 51

**Appendix G:** Kit Examples 54

**Appendix H:** Examples of changes to configurable medical devices 57

**Appendix I:** Example of UDI assignment for software 59

#### Preface

The document herein was produced by the International Medical Device Regulators Forum (IMDRF), a voluntary group of medical device regulators from around the world. The document has been subject to consultation throughout its development.

There are no restrictions on the reproduction, distribution or use of this document; however, incorporation of this document, in part or in whole, into any other document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the International Medical Device Regulators Forum.

There are several notations, which provide clarification to the subject matter. The reader may be prompted by visual cues about the context or referenced information being presented in the document and the table below provides the visual cues used in this document.

Symbol| Description  
---|---  
|   
|   
| Reference to another section or appendix to this document.  
|   
| It is preferable to use this document together with a reference document.  
| Reference to another document.  

**Introduction**

|  The IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) provides a framework for the regulatory authorities that intend to develop their UDI systems in a globally harmonized approach.  
---|---  
| This UDI system Application Guide is to be used as a supplement to the IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) which was developed as a high-level conceptual framework containing the basic core concepts of a UDI system.   
---|---  

The document further acknowledges that additional guidance may be necessary. However, the benefit and purpose of a UDI system will only be realized if healthcare stakeholders integrate and obtain value in their systems from UDIs and data in associated Unique Device Identification Databases (UDIDs). This guide is therefore also intended to assist all relevant stakeholders within the healthcare supply chain and clinical care systems to gain a better understanding of their role and impact on the UDI system.

# Scope

This Application Guide is intended to provide the details and specifications necessary to ensure consistency for enabling a harmonized approach in the application of the requirements set forth in the IMDRF UDI Guidance Document (IMDRF/UDI WG/N7Final:2013). 

| This guide is intended to be read together with the IMDRF UDI Guidance Document (IMDRF/UDI WG/N7Final:2013).  
---|---  

It is recognized that national regulations could differ in relation to certain specific aspects dealt with in the text.

# References

  * IMDRF/UDI WG/N7Final: 2013 - UDI Guidance: Unique Device Identification (UDI) of Medical Devices 
  * IMDRF/RPS WG/N19 Final: 2016 - Common Data Elements for Medical Device Identification
  * GS1 General Specification: <http://www.gs1.org/docs/gsmp/barcodes/GS1_General_Specifications.pdf>
  * GS1 Healthcare GTIN Allocation <https://www.gs1.org/docs/gsmp/healthcare/GS1_Healthcare_GTIN_Allocation_Rules.pdf>
  * Health Industry Business Communications Council (HIBCC) UDI and Labelling Resource Center:   
<http://www.hibcc.org/udi-resources/>
  * International Council for Commonality in Blood Banking Automation (ICCBBA) - UDI Standard  
https://[www.iccbba.org/docs/tech-library/technical/st-017-isbt-128-standard-coding-and-labeling-of-medical-devices-containing-mpho.pdf](<http://www.iccbba.org/docs/tech-library/technical/st-017-isbt-128-standard-coding-and-labeling-of-medical-devices-containing-mpho.pdf>)
  * International Council for Commonality in Blood Banking Automation (ICCBBA) - Technical Specification:  
<https://www.iccbba.org/tech-library/iccbba-documents/technical-specification>
  * ISO/IEC 646:1991, Information technology - ISO 7-bit coded character set for information interchange
  * ISO/IEC15415:2011, Information technology - Automatic identification and data capture techniques. Bar code symbol print quality test specification - Two-dimensional symbols
  * ISO/IEC 15416:2016, Automatic identification and data capture techniques - Bar code print quality test specification - Linear symbols
  * ISO/IEC 15417:2007, Information technology -- Automatic identification and data capture techniques -- Code 128 bar code symbology specification
  * ISO/IEC 15420:2009, Information technology -- Automatic identification and data capture techniques -- EAN/UPC bar code symbology specification
  * ISO/IEC 15426-1:2006, Information technology- Automatic identification and data captureTechniques - Bar code verifier conformance specification — Part 1: Linear symbols
  * ISO/IEC 15426-2:2015, Information technology-Automatic identification and data capture techniques – Bar code verifier conformance specification — Part 2: Two-dimensional symbols
  * ISO/IEC 15459-2:2015, Information technology - Automatic identification and data capturetechniques - Unique identification, Part 2: Registration procedures
  * ISO/IEC 15459-4:2014, Information technology - Automatic identification and data capture techniques - Unique identification, Part 4: Individual products and product packages
  * ISO/IEC 15459-6:2014, Information technology - Automatic identification and data capture techniques - Unique identification, Part 6: Groupings
  * ISO/IEC 16022:2006, Information technology- Automatic Identification and Data CaptureTechniques-Data Matrix Bar Code Symbology Specification
  * ISO/IEC 18000-6:2013, Information technology -- Radio frequency identification for item management -- Part 6: Parameters for air interface communications at 860 MHz to 960 MHz
  * ISO/IEC 18004:2015, Information technology -- Automatic identification and data capture techniques -- QR Code bar code symbology specification
  * ISO/IEC TR 24720:2008, Information technology -- Automatic identification and data capture techniques -- Guidelines for direct part marking (DPM)
  * ISO 28219:2017, Packaging -- Labelling and direct product marking with linear bar code and two-dimensional symbols
  * ISO/IEC TR 29158:2011, Information technology - Automatic identification and data capture techniques - Direct Part Mark (DPM) Quality Guideline

# Definitions

| The reader should refer to the IMDRF UDI Guidance Document (IMDRF/UDI WG/N7Final:2013) for the definition of the most of the terms that are regularly used throughout this guide.  
---|---  

The following terms, which are essential for the understanding of this text, are new or amended definitions. 

_Base Package_

Lowest packaging level which has a UDI. Base package may contain multiple devices.

_Checksum Digit_

Digit or character calculated from data and appended as part of the data string to ensure that the data is correctly composed and transmitted.

_Direct marking_

Direct marking, for purposes of UDI requirements, is placing the UDI and, potentially the full UDI carrier, permanently on the device itself.

_Healthcare provider_

For the purpose of this document, healthcare provider shall be meant as an individual or organisation, which provides diagnostic or therapeutic services to healthcare consumers and/or contributes to public health. 

_Issuing Agency/Entity_

An organization accredited by a regulatory authority to operate a system for the issuance of UDIs.

_Kits_

For UDI purposes, kits are a collection of products, including medical devices, that are packaged together to achieve a common intended use/intended purpose and are being distributed as medical devices.   
Note: Jurisdictions may differ in their definition of kit.   
[modified from IMDRF/UDI WG/N7Final:2013]

_Packaging_

Product to be used for the containment, protection, handling, delivery, storage, transport and presentation of goods, from raw materials to processed goods, from the producer to the user or consumer, including processor, assembler or other intermediary. (ISO 21067-1:2016)

_Qualifier_

One or more characters referring to an entity, providing the meaning of the string data[1].

_Retail pharmacy_

For the purpose of this document, retail pharmacy shall be meant as a pharmacy in which medical devices are sold directly to healthcare consumers.

_Third party_

A third party is referred to in this text as a company/individual, other than the original manufacturer of a device, that, based on a contract with that manufacturer, is authorized by the manufacturer to carry out certain operations on his/her behalf. These operations include notably submission of data to the UDI database and/or placing of the UDI carrier on the device label. 

_Unique Device Identification System (UDI system)_

A system that is intended to provide single, globally harmonized positive identification of medical devices through distribution and use, requiring the label of devices to bear a globally unique device identifier (to be conveyed by using AIDC and, if applicable, its HRI) based upon standard, with the UDI-DI of that unique identifier being also linked to a jurisdiction-specific public UDI database. For more information on the fundamental concepts of the unique device identification system, see IMDRF/WG UDI/N7Final:2013.   
[modified from the definition of “UDI system” in IMDRF/UDI WG/N7Final:2013]

_Unique Device Identifier (UDI):_

The UDI is a series of numeric or alphanumeric characters that is created through a globally accepted device identification and coding standard. It allows the unambiguous identification of a specific medical device on the market. The UDI is comprised of the UDI-DI and UDI-PI. 

Note: The word "Unique" does not imply serialization of individual production units.

# Fundamental Elements of a Harmonized UDI System

The fundamental elements of a UDI system can be summarized as follows: 

  * Development of a standardized system of Unique Device Identifiers (UDIs);
  * Placement of UDIs in human readable and AIDC formats/forms on package labels and in some cases, on the device itself;
  * Submission of core UDI data elements to a UDID;
  * Setting of appropriate transitional and implementation arrangements to ensure a smooth UDI system implementation.

Benefits of the UDI system strongly rely on effective integration of the UDI system to support various regulatory activities during the lifecycle of medical devices and uptake of the UDI system across the whole healthcare sector.

# Guiding principles for UDI system design and operations

The UDI system is being developed to facilitate adequate device identification through distribution and use on patients. 

| This system is emerging across various regulatory authorities at varying levels of system maturity based on IMDRF/UDI WG/N7Final:2013.  
---|---  

When the UDI system is fully implemented, the label of most devices will include a UDI in a human readable form and an AIDC carrier. In addition, globally harmonized metadata about devices will be available in UDIDs as populated by regulated entities.

As the UDI system matures it will require ongoing process and data improvements driven by multi-stakeholder efforts to meet both submitter and user requirements. Foundational to UDI system adoption in the device ecosystem is recognition of the existence of legacy device identifiers and the need to match UDIs to these identifiers.

The UDI and metadata stored in UDIDs are intended to be the identifiers also used in the context of business and clinical transactions, including traceability of devices in the post market setting (e.g. purchase orders, invoices, inventory maintenance/management, clinical notes etc.).

# The Unique Device Identifier (UDI)

# Content, Structure and representation of a UDI

The UDI is composed of two parts: Device Identifier (UDI-DI) + Production Identifier (UDI-PI) = Unique Device Identifier (UDI). UDI-DI + UDI-PI = UDI.

  * **Unique Device Identifier - Device Identifier (UDI-DI)** : The Device Identifier of the UDI is a unique numeric or alphanumeric code specific to a model of medical device and that is also used as the "access key" to information stored in a UDID. This mandatory, fixed portion of a UDI identifies a manufacturer’s specific product and package configuration. Examples of the UDI-DI include GS1 GTIN (Global Trade Item Number), HIBC-UPN (Universal Product Number), or ICCBBA ISBT 128-PPIC (Processor Product Identification Code).
  * **Unique Device Identifier - Production Identifier (UDI-PI)** : The Production Identifier of the UDI is a numeric or alphanumeric code that identifies the unit of device production when one or more of the following is included on the package label of the device. The different types of Production Identifier(s) include: 
    1. The Lot or Batch within which a device was manufactured;
    2. The Serial Number of a specific device;
    3. The Expiration Date of a specific device; 
    4. The date of manufacture (may not be required if other Production Identifiers are on the label);
    5. the Version[2], for Software as a Medical Device (SaMD),
    6. The Distinct Identification Code (DIC), when applicable[3]. This number is an essential identifier for medical products of human origin[4]

#  The UDI carrier

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that the UDI and UDI carrier should be based upon standards and are fundamental parts of UDI system requirements.  
---|---  

The UDI Carrier shall be on the label or on the device itself and on all higher levels of device packaging. Higher levels do not include shipping containers.

Direct marking is placing the UDI and, potentially the full UDI carrier, permanently on the device itself. 

The UDI contains the device identifier (UDI-DI) and the specific production identifiers (UDI-PI) specified in this document. 

The UDI carrier may also contain other identifiers not considered part of the UDI but carried within the UDI carrier to support sharing of standardized non-UDI information between trading partners (e.g. article number).

# UDI Human Readable Interpretation (HRI) Format, Structure and Content of Each Issuing Agency/Entity

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) requires the HRI format to follow the specifications of the UDI issuing agency/entity as sanctioned by the regulatory authority.  
---|---  
| The tables in Appendix A contain the UDI HRI formats to be used for each of the issuing agencies/entities with examples of the HRI alone, followed by a representation of the HRI combined with AIDC in linear and two-dimensional bar code (as shown in Appendix B to this document).  
---|---  

The inclusion of the qualifiers is necessary in the HRI to determine what the identifiers are in the string of characters that follow the qualifier. 

# Automatic Identification Data Capture (AIDC) representation of UDI

| There is a wide variety of AIDC carriers available; however, to meet the imperatives of the IMDRF UDI Guidance, the UDI should comply with the requirements of the global accredited issuing agencies/entities and the accepted AIDC standards, i.e., ISO/IEC 15459-2; ISO/IEC 15459-4; ISO/IEC 15459-6; ISO/IEC 646; ISO/IEC 15415; ISO/IEC 15416; ISO/IEC 16022; ISO/IEC TR 29158.  
---|---  

Each issuing agency/entity has their own general technical specifications that include information on the carrier type, size, placement and quality in addition to recommendations about the human readable presentation of the encoded. 

| For further information on issuing agencies/entities, see Section 10.3 of this document.  
---|---  

Some carriers are only approved for specific applications (e.g. retail point of sale). Therefore, it is imperative to understand the appropriate application of each carrier and allow the manufacturer to choose the appropriate carrier based upon the application for use. 

| Section 8.4 of the IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) provides additional information on this aspect.  
---|---  
| For purpose of illustration, the images shown in Appendix B depict some of the most widely used AIDC carriers used in healthcare (medical devices and pharmaceuticals) today.  
---|---  

RFID may also be an acceptable AIDC technology.

| Examples of RFID are provided in Appendix C[5].  
---|---  

# How to place a UDI carrier on the label of the device or on the device itself

The UDI carrier, as referred to in Section 6.2, should be placed on the label of the device or on the device itself, and on all higher levels of device packaging. Higher levels of packaging do not include shipping containers. Direct marking is placing the UDI and, potentially the full UDI carrier, permanently on the device itself.

| For further information on Direct marking and UDI carrier see Section 6.5.1.  
---|---  

Several technologies are available (e.g. printing, marking, Radio Frequency Identification (RFID), etc.) for applying the UDI carrier on the label or on the device. 

Regardless which technology is used, the manufacturer shall ensure that the UDI is readable for the expected service life and that placing the UDI carrier on the label or the device itself is not creating any negative impact on the benefit-risk ratio of the device. 

In this context, also the influence of the transport, storage and handling environment shall be considered. By doing so, the material on which the UDI carrier is placed and the impact of the chosen technology shall be analysed. Special consideration has to be taken into account for direct marking, including analysing the impact of the direct marking process and ensuring there is no negative impact on the stability, biocompatibility, and effectiveness of the device.

| For further information on special considerations for direct marking see Section 6.5.1.  
---|---  

When applicable, in combination with material suitability, the adequacy of the bar code/matrix resolution should be ensured to enable correct scanning by barcode readers, based on ISO/IEC standards as described in section 6.7.

The uniqueness of the UDI carrier shall be ensured, to avoid duplication or any misrecognition by AIDC readers or by human eyes among products and package levels. In particular, any stakeholders who place types of AIDC forms other than UDI on the relevant packages, labels or products themselves, shall ensure that the placing of those AIDC forms does not create the potential for confusion with the UDI carrier. 

It is also recommended that multiple bar codes are not applied on the same label of a device or on the same device or package. 

Figure 1 shows an example of the application of a UDI carrier on the label of device or on the device itself and on the package

Figure 2 compares devices with a UDI carrier on the label or on the device itself. 

Figure 3 compares packages with a UDI carrier on the adhesive sticker or directly printed on the packaging.

_Figure 1: Example of application of UDI carrier on the label of device or on the device itself and on the package_

 _Figure 2: Comparison of devices with a UDI carrier on the label or on the device itself._

_Figure 3: Comparison of packages with a UDI carrier on the adhhesive sticker or directly printed on the packaging._

|  For further information on AIDC Reader see Section 6.7.  
---|---  

# Direct Marking

| The IMDRF UDI Guidance (IMDRF/WG/N7Final:2013) states: “Medical devices that are reusable should have a UDI Carrier on the device itself. The UDI Carrier of reusable medical devices that require reprocessing between patient uses should be permanent and readable after reprocessing cycles for the intended life of the device. Manufacturers may determine that this may not be possible or warranted on some devices due to size, design, materials, processing, or performance issues.”  
---|---  

The determination of whether a device is reusable or not is to be made by the manufacturer. That determination should be reflected in the instructions of use, together with any relevant appropriate information on appropriate processes for allowing reuse. 

Direct marking is the preferred solution for placing the UDI Carrier on the device itself in the case of reusable devices. There are a variety of methods for applying direct marking, including both intrusive methods (e.g., dot pin; etching; direct laser marking; etc.) and non-intrusive methods (e.g., cast/forge/mold; laser bonding; stencil; permanent adhesive label; etc.). 

| ISO/IEC TR 24720 provides guidelines for direct marking, namely in relation to selection of methods of marking based on material. Other useful standards in this context include ISO 28219 and ISO/IEC TR 29158.  
---|---  

Issuing agencies/entities might have recommendations on key aspects of direct marking, including substrate requirements, symbol dimensions, symbol quality, and symbol placement. 

| For further references on issuing agencies/entities see Section 2.  
---|---  

Direct marking supports accurate identification and capture of a UDI (and when marked with an AIDC carrier, allows auto-capture) when the device is no longer accompanied by its label or package containing the UDI. The figure below shows examples of direct marking on surgical instruments. 

_Figure 4: Example of direct marking_

An exemption to the direct marking obligation shall be foreseen under the following circumstances:

  1. any type of direct marking would interfere with the safety or performance/effectiveness of the device;
  2. the device cannot be directly marked because it is not technologically feasible.

The applicability of those exemptions shall be based on evaluations of the characteristics of the selected direct mark technology as well as size, design, materials, processing, or performance issues related to the device in question.

| Examples of feasibility issues linked to direct marking integrity are provided in Appendix F.  
---|---  

# Considerations on the UDI contents of the Medical Device Label

| The IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) defines the UDI.   
---|---  

The contents of the UDI carrier shall be consistent with corresponding contents of the label while date formats may vary. 

| The IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) and the IMDRF document IMDRF/GRRP WG/N52Final:2019 indicate the contents of the labeling that shall appear in the UDID.  
---|---  

In this context, it is important to note that the information to be registered in the UDID should also be consistent with the relevant contents of the device label.

# Considerations on AIDC readers

AIDC readers comprise bar code readers or readers of other AIDC technologies (such as RFID readers). 

Barcode readers are designed and manufactured in many configurations (e.g. fixed mount, handheld, tethered, cordless, wearable, mobile phone, etc.) and, like many electronic devices, can be acquired with a wide range of factory and/or user selectable features and capabilities.

Barcode readers are available as “linear” scanners for “linear” symbologies only (e.g. Code 128) and as “image scanners” for linear and 2-dimensional (2D) symbologies (e.g. Code 128 and Data Matrix). 

Since image scanners can scan linear and 2D-symbologies, it is recommended for users to utilize image scanners for UDI applications. Any evaluation of scanner or reader technology should take into account the range of bar code formats, sizes, and substrates that will be scanned at the point of care. It is recommended that scanners be capable of reading two-dimensional bar codes printed both on conventional labels and marked directly on implants and other medical devices.

There is no additional technical knowledge needed to use (i.e. to scan with) a 2D/matrix versus 1D/linear scanner. In fact, both the omnidirectional reading capability of a 2D/matrix “camera” or “area imager” scanner, and the 2D/matrix scanner’s inherent ability to read both 2D/matrix and 1D/linear types of barcodes will make them easier and in the long run more economical to use in many instances. The only additional technical consideration is that every scanner (whether 2D/matrix or 1D/linear) must be properly set up and/or configured for its intended use, which is generally easily done by the firm the readers are purchased from.

Readers for UDI applications need to support the barcode symbologies in line with relevant international standard (including ISO/IEC 16022, ISO/IEC 18004, ISO/IEC 15417, ISO/IEC 15420).

Standardised barcode symbologies should have a symbology identifier registered with ISO/IEC 15424. Bar code readers transmit the symbology identifier to differentiate between the data carriers of each issuing agency/entity. 

An example of readers of other AIDC technologies is an RFID reader. Today, some RFID readers have the capability to read 1D/linear and 2D/matrix barcodes. However, barcode readers typically cannot read RFID tags without the addition of external / auxiliary RFID reading devices.

# Application of UDI to packaging levels

# Applying UDI to Medical Device Package Level Hierarchy

One of the main principles of a UDI system is to apply a UDI to each packaging level of a medical device package level hierarchy. The UDI-DI of each package level requiring UDI must be unique to distinguish between package quantities at each package level[6]. 

The device package level hierarchy is a key concept to understand in terms of UDI system. It is also important to note that, while most medical devices are contained within packages with labels, there are instances where the devices are removed from the original packaging and therefore the label no longer exists. 

| Appendix D provides some examples of package level hierarchies, including how they are captured in the UDID.  
---|---  

# Unit of Use (UoU) DI

The UoU DI is an unmarked identifier assigned to an individual medical device when a UDI is not labeled on the individual device at the level of its unit of use. Its purpose is to provide a UDI-DI to identify a device used on a patient when a UDI-DI does not appear on the label of the device. 

The UoU DI should be assigned when the base package[7], i.e., the lowest packaging level with a UDI, has a device count greater than 1[8]. 

| For further information on UoU DI assignment see Appendix E.  
---|---  

The concept of UoU DI is not generally used in industries outside healthcare. Within the healthcare context, this concept is of great significance due to the clinical needs to track individual devices within specific packages.

User education is key to assure proper assignment, entry and use of the unmarked UoU DI. The user education should include education of data submitters, data users and Electronic Health Record (EHR) system vendors.

| Examples of package level hierarchies (including UoU) are provided in Appendix E.  
---|---  

# The Unique Device Identification Database (UDID)

| Regulatory authorities are responsible for developing the UDID in their jurisdiction based upon local policy requirements and the principles developed in the IMDRF UDI Guidance (IMDRF/ UDI WG/N7Final:2013) and this document.  
---|---  

Providing public access to each UDID will further allow healthcare stakeholders to access essential information to identify devices. 

# Expectations for an effective UDID design

| The IMDRF UDI Guidance (IMDRF/UDIWG/N7Final:2013) indicates in its introductory section that: "The UDI System is intended to provide a single, globally harmonized system for positive identification of medical devices. Healthcare professionals and patients will no longer have to access multiple, inconsistent, and incomplete sources in an attempt to identify a medical device and its key attributes".  
---|---  

The UDID is a designated source for device identification information. To ensure that all stakeholders, in particular the healthcare sector, are able to obtain value from the UDI system and the UDID, regulators should consider the following principles when developing regional UDIDs.

Regulatory authorities are recommended that their UDID is designed:

  1. as a central medical device master database containing all essential information to identify devices in the jurisdiction;
  2. to include the entire package level hierarchy of a medical device (e.g. unit-of-use, base package, higher package levels). The hierarchy should be linked to a specific device and provide a parent–child relationship structure;
  3. to be freely and effectively accessible to all stakeholders, in particular the healthcare sector;
  4. in a way that relevant available UDI-DI related information can be integrated through downloads and/or Application Programming Interfaces (APIs) into:
     1. internal regulatory systems (such as adverse event reporting, recalls)
     2. device registries 
     3. healthcare supply chain systems, clinical systems (e.g. electronic health records), and clinical engineering device maintenance systems;
  5. to ensure high availability and reliability (e.g. multi-access automatic up- and downloads 24 hours /7 days);
  6. to ensure the integrity of data and data transmission processes using recognized data exchange standards, when possible;
  7. to inform manufacturers about reported data quality issues and track correction, data quality improvements and responses regarding the information submitted. This does not replace manufacturer responsibility for UDID data quality;
  8. to ensure that acknowledgment of receipt is provided to indicate success and completeness of data submission;
  9. to connect the device UDI-DI information with codes and terms of a nomenclature[9] which would enable other stakeholders to: use the UDID data for activities like purchasing, stock handling, reimbursement or research; find UDID information related to similar devices or to enable regulatory authorities to effectively assess the safety and performance of product groups in the field; 
  10. to have a set of transparent rules on UDI-DI related information updates; 
  11. to allow for necessary corrections/updates of information to improve the quality of data;
  12. to ensure that there are timely and adequate notifications of any change to the UDI system that would impact data submission and use (e.g. adding new fields, changing data definitions or values, validation rules);
  13. to keep history of UDID entries and changes and make information on changes publicly available;
  14. to ensure via security protocols that information provided by the manufacturer (or an authorized third-party acting on behalf of a manufacturer) is successfully and correctly submitted;
  15. to provide clearly defined data validation rules specific to a single data field or a combination of data fields to ensure data integrity, that including, to the extent possible, reasonable automatic plausibility “checks” so that data format requirements for all data elements required for submission to an UDID shall remain stable over a long time;
  16. to consider multiple options for submission (e.g. HL7 SPL, Excel or CSV files, Structured input via a Web-interface to allow for manual UDI data entry). Those options should be based upon user interface design principles so that data entries is intuitive for the user, data is captured in a structured manner using pre-defined list(s) of values and limit the use of free-text fields as much as possible;
  17. to accommodate the submission of data from authorized third parties;
  18. to the extent possible, have validation procedures to enhance consistency across internal regulatory systems and minimize the use of duplicate data entry by manufacturers that must enter the same data across those systems.

During the design and development of the UDID, feedback from all the stakeholders that are expected to be using the UDID should be sought. 

Manufacturers are responsible for the initial submission and updates to the information in the UDID. 

# UDID Data Specifications

Regulators should ensure that UDID data specifications for UDID data elements[10] are available to relevant stakeholders as soon as practicable, in order to ensure that they have sufficient time for developing respective systems and procedures. 

The following is a recommended data specification list at a data field level: 

  * field name;
  * field description;
  * field characteristics (numeric, alphanumeric);
  * field length (number of digits, fixed length, variable length);
  * indication whether field is a single value or multiple value field (maximum number of values allowed);
  * cardinality information in order to indicate the number of occurrences in one data element which are associated in the number of occurrences in another data element (i.e. one to one, one to many); 
  * list of predefined values (remark: value ‘blank’ or 'null' should be avoided);
  * field edit rules (e.g., value changes allowed, deletion, only new values to be added, value locked after grace period);
  * indication whether the field is mandatory, optional, conditional or autopopulated (include rules for conditional);
  * indication whether a value change triggers a new UDI-DI.

Ideally, the UDID data specifications would be constructed in a data reference table. 

| IMDRF/UDI WG/N53 FINAL: 2019 collects information on UDI data elements as collected in National UDI databases (UDID) across jurisdictions.  
---|---  
| Certain harmonized specifications for some UDID data elements are already included in the IMDRF Common Data Elements document (IMDRF/RPS WG/N19Final:2016). They provide a controlled vocabulary, standardized nomenclature, structure and definition for those UDID data elements.  
---|---  

# Submission of information to UDID by third-party submitter

| As indicated in Section 10.2 of this guide, the manufacturer is ultimately held responsible for the information submitted to the UDID.  
---|---  

Regulators that allow a third-party submitter should establish a formal process to authorize those third-party solution providers to submit UDID data on behalf of a medical device manufacturer[11]. This process might include the following:

  * the manufacturer provides third-party information, which is saved as part of the manufacturer’s account;
  * the third-party submitter completes the relevant testing on behalf of the manufacturer;
  * during submission processing, the UDID validates that third-party is authorized to submit data on behalf of the manufacturer;
  * the third-party submitter performs data validation before submitting data to the UDID.

# UDI-DI triggers

UDI-DI triggers are data elements within a device's UDID entry that, if changed, would require a device to obtain a new UDI-DI.

| The IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) provides that, at a minimum, a new UDI-DI is required whenever there is a change that could lead to misidentification of the medical device and/or ambiguity in its traceability.  
---|---  

Any change of one of the following UDID data elements[12]determines the need for a new UDI-DI:

  *     1. Brand Name;
    2. Device version or model[13];
    3. Clinical Size (including Volume, Length, Gauge, Diameter);
    4. Labeled as single use;
    5. Packaged sterile;
    6. Need for sterilization before use;
    7. Quantity of devices provided in a package;
    8. Critical warnings or contraindications: e.g. containing latex or Bis (2-ethylhexyl) phthalate (DEHP).

It shall be noted that new packaging configurations require a new UDI-DI.

To date, those with experience implementing a UDI system into regulatory and healthcare systems have identified a significant challenge with the assignment of multiple UDI-DIs to products, which share essential design and manufacturing characteristics. Some manufacturers choose in many cases to use the UDI-DI as the means to manage distribution control, which means that they use it to differentiate country of origin, manufacturing locations, and other internal information[14]. This practice results in multiple UDI-DIs being assigned to medical devices that health care provider and regulatory authorities consider being clinically the same medical device[15]. 

Inconsistent applications of UDI-DI triggers by manufacturers as well as a lack of agreement among different regulatory authorities and jurisdiction-specific regulatory requirements related to UDI-DI triggers might be an additional factor determining the multiple DI issue. 

To minimize that risk, regulators that implement UDI systems and issuing agencies/entities would improve the value of the UDI system by ensuring that UDI-DI triggers other than the ones provided in the IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) are kept to a minimum and that manufacturers implement those UDI-DI triggers consistently and in a way that promotes UDI as a global standard for device identification. The manufacturer should take into account valid alternatives to manage product distribution control. 

Regulatory authorities that have started or plan to implement a UDI system should rely on sharing best-practice stakeholder communities to look closely at the issue of multiple UDI-DIs. 

| For further information on the issue of stakeholder communities see Section 13.  
---|---  

# Recording Unique Device Identifiers into forms, databases (other than UDID), registries and other health information

To take advantage of the structured data embedded in a UDI it is recommended that the UDI be parsed into discrete fields in database entries and forms[16] in order to have the UDI data properly catalogued.

A suggested example to capture the parsed UDI is as follows:

[17]

| The document IMDRF/WG UDI/N54Final:2019 provides further information on system requirements related to use of UDI in healthcare including selected use cases.  
---|---  

# Establishing Responsibility for Creating and Maintaining a UDI System

Establishing the fundamental elements of a UDI system requires that all relevant parties have a clear understanding of their role to achieve the UDI system goals.

Regulatory authorities that intend to establish a UDI system are responsible for establishing the basic regulatory requirements and vision for the UDI as a global standard. Issuing agencies/entities accredited or recognized by regulatory authorities are responsible for defining the general UDI specifications based on relevant international standards. Manufacturers are responsible for creating and maintaining globally unique UDIs for their medical devices by following the issuing agency/entity’s specifications. Distributors, importers, retail pharmacies, healthcare providers and users significantly contribute to enhance the potential of the UDI as a key standard to facilitate adequate device identification through distribution and use with patients. 

# Regulatory Authority

To avoid each regulatory authority implementing and managing local UDI systems differently, the participating IMDRF regulatory authorities have developed the details and specifications outlined in this document to harmonize their unique device identification system requirements, and increase global consistency of implementation. 

The regulatory authorities that establish a UDI system are responsible for establishing a standardized UDI system to meet local regulatory requirements and to develop and maintain a local publicly available UDID that is capable of linking, to the extent possible, to other regulatory authority UDIDs. It is recognized that local specificities and regulations could impact certain aspects of UDI implementation.

Regulatory authorities have the following key oversight roles: 

  * accrediting issuing agencies/entities and overseeing their operations to an extent which may vary depending on each regulatory authority;
  * issuing operational guidance and specifications; 
  * laying down and enforcing obligations for manufacturers in relation to the UDI system in a particular jurisdiction;
  * to promote further medical device identification in the supply chain and clinical environment by setting expectations for importers, distributors, retail pharmacies and healthcare providers to facilitate uptake of the UDI system.

Additionally, the regulatory authorities have shared responsibility with accredited issuing agencies/entities, manufacturers, and standards development organizations to strengthen the UDI as a global standard by committing to ongoing harmonization of UDID data elements, and development of common vocabularies and exchange standards used in UDI implementation. 

# Manufacturer

| The IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) states: “The medical device manufacturer should create and maintain globally unique UDIs on his medical devices.”  
---|---  

To that purpose, manufacturers shall also keep UDI related information in their documentation in accordance with jurisdictions ‘regulations.

Manufacturers are responsible for understanding both regulatory and issuing agency/entity requirements or standards to accurately assign and place the UDI in human readable and AIDC format on the label or on the device itself and on all higher levels of device package level hierarchy. Based on a contract with a manufacturer, a third party may place the UDI carrier on the label or on the device itself and on all higher levels of the device package level hierarchy on behalf of the manufacturer. However, under that scenario, the manufacturer is ultimately held responsible for the conformity of the UDI carrier[18].

Manufacturers are also responsible for the initial submission and updates to the information in the UDID. While manufacturers should also be allowed to engage with third parties who provide services to submit UDI data to the UDID, the manufacturer is however ultimately held responsible for the information submitted[19].

| For further information on submission of information to UDID by a third-party submitter, see Section 8.3.  
---|---  

# Own brand or private labellers

Own-brand/private labelers shall be meant as companies/individuals, other than the original manufacturers of a device that make available on the market that device under their own brand name.

| The IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) indicates that own brand/private labelers assume all manufacturers' obligations, related to the UDI system, including obligations to place the UDI carrier on the label and to submit UDI information to the UDID.  
---|---  

However, when a company/individual that makes available on the market a device under its own brand name enters into an agreement with the original manufacturer of the device and the original manufacturer is identified as such on the label, all relevant manufacturers ‘responsibilities for that device remain with the original manufacturer including all UDI related responsibilities.

# Issuing Agency/Entity

| The IMDRF UDI Guidance (IMDRF/WG UDI/N7Final:2013) document states that “globally accepted ISO/IEC coding standards implemented by global organizations, such as GS1, HIBCC and ICCBBA, meet the criteria of the UDI and manufacturers shall be permitted to choose which system to use. These organizations have responsibility for maintaining the global uniqueness of their coding systems.”  
---|---  

The main task of these agencies/entities is to operate a system to be used by the manufacturers for assignment of the UDIs to their devices.

Issuing agencies/entities are responsible for defining the UDI as a trade item standard. Regulatory requirements take precedence over issuing agency/entity requirements.

If the issuing agency/entity intends to update their standards or specifications that have an impact on the UDI system, they are expected to submit a request for authorization to the relevant regulatory authorities. Given the global nature of those standards or specifications, it is recommended that IMDRF regulatory authorities consult each other and the relevant stakeholders (e.g. industry) about the impact of those changes.

Issuing agencies/entities shall develop initiatives and tools to educate manufacturers on the appropriate use and implementation of the agencies’/entities’ systems for the issuance of UDIs. This includes training and development of educational material. 

Conditions for designation of agencies/entities shall include that:

  * the agency/entity operates a system for the issuance of UDIs which conforms to the relevant international standards;
  * the agency/entity undertakes to operate its system for the assignment of UDIs for a period which should be no less than 3 years to minimize possible disruptions;
  * the agency/entity undertakes to make available to the relevant national authorities, upon request, any information concerning its system for the assignment of UDIs.

Regulatory authorities may opt for setting additional agencies/entities' responsibilities. In this case, those authorities might consider establishing agreements with the issuing agencies/entities, upon their designation, under which these entities would be required: 

  * to make available to regulators their tools that validate that the UDI-DI is meeting the issuing agency/entity’s specification for a valid UDI-DI;
  * to work in cooperation with regulators and manufacturers to avoid problems listed below and correct, if needed:

  1. deficiencies in UDI creation (e.g. tests for validity, uniqueness, check digit)
  2. deficiencies in UDI placement and use (e.g. print quality, scannability, types of UDI carriers, surface and substrate impact);

  * to have procedures in place to take necessary follow-up actions up to and including restricting the use of the company prefix or prefixes for UDI purposes. The issuing agency/entity will provide timely notification to the regulators whenever they become aware of repeated and/or deliberate misuse of the Issuing agency/entity’s UDI requirements and have restricted the use of the appropriate company prefix related to UDI;
  * to maintain a maximum level of stability regarding their requirements for data formats on UDI-DI and UDI-PI and their encoding in an AIDC;
  * to involve regulators when planning additions or changes to their specifications, particularly when those specifications have an impact on the construct of a UDI and the way it is captured;
  * to have the relevant global standards implemented consistently across their regional members;
  * to continuously supply to regulators educational materials, application forms, and access to other materials the issuing agency/entity provides for its members;

It is recommended that regulatory authorities duly consider the impact of their agreements on global harmonization.

# Expectations from stakeholders related to UDI

# Distributors and importers

Distributors and importers are expected to control that, where applicable, a UDI has been assigned to devices they receive, prior to further making the device available. 

Distributors and importers should assure that UDI related information is included in their documentation in accordance with jurisdictions ‘regulations. National regulators may consider legal or regulatory measures required for this purpose.

# Healthcare providers and retail pharmacies

Regulatory authorities might require that healthcare providers and retail pharmacies assure that all device records they maintain include the UDI as an essential component to allow traceability of devices.

Healthcare providers and retail pharmacies can play a crucial role in understanding and promoting the value of UDI as well as signalling lack of compliance related to UDI requirements, as they receive and use most of the medical devices available on the market. 

National regulators should consider legal or regulatory measures required for this purpose. 

# Other stakeholders

Providing specific fields for the UDI-DI and UDI-PI and key fields in UDIDs allows for the capture of structured standardized data.

Regulatory reviewers, epidemiologists, clinical researchers and members of professional societies rely on clinical trial and real world data sources (electronic health records, registries, reimbursement data, and medical device registries) to evaluate the patient and device safety.

Currently, the device identification information collected in clinical care and device registries is not structured or standardized. Often, it is captured in text fields and narrative that cannot easily be used for device evaluation.

Integrating UDI into device evaluation methodologies likewise improves the accuracy of clinical and research data. Researchers will easily see the value of the UDI to improve the quality of research data.

Both device industry and regulatory authorities should encourage interdisciplinary participation within their own organizations between those who design and maintain UDIDs and those who are internal users of this data in order to provide value to their internal customers and support UDI adoption within their own organizations.

# International standards and terminology development organizations

Standards and terminology development organizations are crucial to global harmonization in the UDI field, as they set detailed technical specifications on aspects such as UDI allocation rules, structure and placement of UDI carrier, and relevant data exchange. Examples of international standards and terminology developments are the Issuing agencies/entities, the International Organization for Standardization (ISO), the International Electro Technical Commission (IEC), the Advancing Identification Matters (AIM), the Logical Observation Identifiers Names and Codes (LOINC), the Systematized Nomenclature of Medicine -- Clinical Terms (SNOMED) and the Health Level Seven International (HL7).

Regulators, manufacturers and healthcare providers, who plan to adopt and implement a UDI system, are recommended to actively engage with those organizations.

# General Considerations to facilitate an effective UDI Implementation

# Transitional period

| The considerations listed in the IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) include a risk-based approach to UDI implementation and the “need for all supply chain stakeholders to have sufficient time to prepare their systems, process and staff, for the proper use of the UDI systems.”  
---|---  

The following is an example of an effective implementation schedule of a UDI system that regulatory authorities could consider:

  * Initial implementation period in jurisdictions should begin no less than two years from the publishing of the UDI system requirements for the highest risk devices, followed by 2 year incremental implementations (at minimum) for each risk category of medical devices.
  * Direct Marking timelines should provide an additional minimal two years for implementation at each risk level. 

Regulators shall ensure that relevant technical specifications are adopted and published. In particular, technical specification for UDI data elements and for data exchange protocols should be available well ahead of the date of application of the relevant National UDI requirements.

When setting the timelines for adoption of those specifications, regulators shall consult the relevant stakeholders. 

# UDI implementation arrangements

The following implementation arrangements should be considered by regulators for a successful UDI implementation:

  * Public forums for UDI system education and public comment on the UDI system
  * Engagement with national medical device trade and healthcare professional associations 
  * UDI system conferences to allow industry stakeholders to learn and help educate on UDI implementation
  * Help Desk service to assist industry with implementation questions
  * Guidance documents to address issues or challenges that arise
  * Process for manufacturers to apply for exceptions and/or alternative methods for marking a UDI or in relation to other UDI related aspects
  * UDID data submission training and education webinars
  * UDID user group sessions to obtain feedback from both UDID submitters and UDID users 
  * Promoting a better understanding of UDI user requirements by forming regional UDI expert clinical and supply chain groups or learning communities to identify and specify best practices for UDI implementation that can be shared globally

# Special cases

This Section intends to complement or, where necessary, clarify some of the requirements set in Section 10 of the IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013), based on learning experience with certain specific device types in the course of the last few years. 

# Implantable devices

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) indicates that: "Implantable devices should follow the rules listed below:1\. All unit packs of implantable devices (lowest level of packaging) need to be identified/AIDC marked with an UDI (UDI-DI + UDI-PI);2\. UDI-PI should have the following characteristics: a. serial number for active implantable devices,b. serial number for other implantable devices or lot number according to the manufacturer's quality management system;3\. The UDI of the implantable device must be identifiable prior to implantation.”  
---|---  

In relation to those requirements, some additional considerations can be made:

  * Implantable devices are generally not required to have a UDI carrier on the device itself (direct marking);
  * The rationale of requirements in 3. ("The UDI of the implantable device must be identifiable prior to implantation") is to minimise the risks of misidentification of the implanted device;
  * It shall be ensured that the UDI can be scanned prior to implantation and linked to any electronic system, this implying that an AIDC is present.

# Reusable devices

| The IMDRF UDI Guidance (IMDRF/WG/N7Final:2013) states: “Medical devices that are reusable should have a UDI Carrier on the device itself. The UDI Carrier of reusable medical devices that require reprocessing between patient uses should be permanent and readable after reprocessing cycles for the intended life of the device. Manufacturers may determine that this may not be possible or warranted on some devices due to size, design, materials, processing, or performance issues.”  
---|---  

The determination of whether a device is reusable or not is to be made by the manufacturer. That determination should be reflected in the instructions of use, together with any relevant appropriate information on appropriate processes for allowing reuse. 

| For further information on reusable devices and direct marking, see Section 6.5.1.  
---|---  

# Non-IVD kits

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that "The manufacturer of the Kit is responsible for identifying the Kit with a UDI including both UDI-DI and UDI-PI."  
---|---  

# Placement of UDI carrier on the medical device contents of kits

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that "Medical device contents of Kits should have a UDI Carrier on their packaging or on the device itself".  
---|---  

Where applicable and practicable, the UDI of the medical device contents of kits should be readable and scannable from the outside of the kit. In this context, it should be noted that there are situations where the presence of multiple bar code could lead to confusion scanning and the ability to read and scan the UDI of the contents of the kit from the outside of the kit does not provide any value or benefit to users.

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) indicates the following exemption to the requirement whereby medical device contents of Kits should have a UDI Carrier on their packaging or on the device itself:a. Individual single-use disposable medical devices within a Kit, whose uses are generally known to the persons by whom they are intended to be used, and which are not intended for individual use outside the context of the Kit do not require their own UDI Carrier.Example: An unpackaged sterile syringe within a sterile Kit cannot be used for another procedure, due to the lack of a sterile barrier once removed from the Kit;b. Medical devices that are normally exempted from having a UDI Carrier on the relevant level of packaging do not need to have a UDI Carrier when placed within a Kit."  
---|---  

For the example provided under b), it must be noted that this does not apply to devices that are being broken down from bulk packaging for use in a kit when the bulk package manufacturer intends them to remain in the bulk packaging until the point of use.

| Appendix G provides useful example of UDI assignment for non-IVD kits in relation to issues explored under Sections 12.3.1 and 12.3.2.  
---|---  

UDID shall capture the UDI-DI of the kit as well as of each medical device in the kit that is marked with a UDI[20]. 

# Exemption for non-IVD kits

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that"Orthopedic procedure trays whose contents are configured for a specific order are exempted from this UDI requirement“[21].  
---|---  

Figure 5 represents an example of this kind of orthopedic procedure tray. These trays are often delivered to a hospital in a stainless-steel box, then stored and sterilized by the hospital for use in a procedure. After the procedure, the hospital will normally replace used parts and re-sterilize the box with its original and replaced contents.

_Figure 5: Example of orthopedic trays used in trauma and spine surgeries_

It is important to note that these trays are made up of registered and approved medical devices, including instruments and/or implants, in their own right, and are distributed together in non-sterile metal containers strictly for healthcare provider convenience, the convenience of sterilization processing and to accommodate set replenishment in the field or the hospital. The medical devices included in the trays shall be identified individually and are subject to UDI rules at the individual level.

The original exemption provided by the IMDRF Guidance (IMDRF/UDI WG/N7Final:2013) does not address the needs of clinical users and patients for identifying the devices in those trays.

# IVD kits

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that: "The manufacturer of the IVD Kit is responsible for identifying it with a UDI including both UDI-DI and UDI-PI"  
---|---  

# Medical device contents of IVD kits

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that:1\. “Medical device contents of IVD Kits should have a UDI Carrier on their packaging or on the device itself,a. The IVD Kit is a device and all aspects of this guidance that is relevant apply to it. If an IVD Kit does not include any components which on their own are considered medical devices the only UDI is the UDI of the kit itself;b. Reagents used in automated systems bear barcodes necessary for their handling and identification by the automated systems. This does not constitute a UDI;c. Individual single-use medical devices packaged within an IVD Kit, whose uses are generally known to the persons by whom they are intended to be used, and which are not intended for individual use outside the context of the IVD Kit do not require their own UDI Carrier;d. Medical devices that are normally exempted from having a UDI Carrier on the relevant level of packaging do not need to have a UDI Carrier when placed within an IVD Kit."  
---|---  

In relation to those requirements, some additional considerations can be made:

  * IVD kits contain at least one item which on its own can be considered a medical device;
  * The reader should note that, for individual single-use medical devices packaged within an IVD Kit, whose uses are generally known to the persons by whom they are intended to be used, they do need a UDI when distributed as replacement parts for the kit.

UDID shall capture the UDI-DI of the kit as well as of each medical device in the kit that is marked with a UDI[22]. 

# Placement of UDI on IVD kits

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that: “Placement of UDI on IVD Kits:a. The IVD Kit UDI is generally affixed to the outside of the packaging;b. The UDI must be readable or in the case of AIDC scan able, whether placed on the outside of the IVD Kit package or inside a transparent package"  
---|---  
| Appendix G provides a useful example of a UDI assignment for IVD kits in relation to issues explored under Sections 12.4.1 and 12.4.2.  

# Configurable medical devices

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) indicates that: "For configurable medical device systems the rules listed below should be followed:1\. A UDI is allocated to the entire, configurable medical device system and is called the System UDI.2\. A system UDI-DI is allocated to defined groups of configurations, not per configuration within the group. A group of configurations is defined as the collection of possible configurations for a given product line as described in a regulatory file. 3\. A system UDI-PI is allocated to each individual system. A later change of a component, sub-systems or accessory of the system does not change the UDI-PI of the system.4\. The carrier of the System UDI should be put on the assembly that most likely does not get exchanged in its lifetime and should be identified as the System UDI. 5\. Each component, sub-system or accessory that is considered a medical device and a distributed or supplied unit needs a separate UDI.6\. A new UDI-DI is required when the activities performed results in modifications to a previously marketed device intended for resale leads to a new medical device. 7\. A new UDI-DI is not required when the activities performed do not result in a change/modification in performance, safety and/or intended use, of a previously marketed device intended for resale. The activities shall be performed in accordance with the manufacturer’s instructions."  
---|---  

Despite point 3 provides the general rule that the System UDI of a device already placed on the market or in use shall not be changed if there are later changes to the configuration of this device, it is necessary to make clear that for specific devices and under specific circumstances it might be necessary to be able to uniquely identify the changed device configurations in the field. 

If a change of a device in the field would significantly change the safety, performance or the intended purpose (and these changes are not within the limits of the original configuration), those changed devices should be identifiable. To make the changed device identifiable a manufacturer should provide an upgrade kit[23] (which, itself, is considered a medical device) with a correspondent UDI which meets all UDI requirement (e.g. labelling, publication to UDI database(s), etc.). The UDI of the upgrade kit together with the original System UDI will be used to identify the changed device.

An alternative would be that a manufacturer might perform this change as new installation (comparable with a resale of a modified device as described in point 6) the new installed device would need to be marked with a corresponding new System UDI.

| Appendix H provides useful examples on this specific issue.  
---|---  

# Software as a Medical Device

# UDI Assignment Criteria

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) indicates that:"The UDI should be assigned at the system level of the Software as a Medical Device (SaMD). The version number of the SaMD is considered the manufacturing control mechanism and should be displayed in the UDI-PI.The following change of a SaMD would require a new UDI-DI:• Major SaMD revisions shall be identified with a new UDI-DI;Major SaMD revisions are meant as complex or significant changes affecting:1) the original performance and effectiveness,2) the safety or the intended use of the SaMD,These changes may include new or modified algorithms, database structures, operating platform, architecture or new user interfaces or new channels for interoperability. The following change of a SaMD would require a new UDI-PI (not a new UDI-DI):• Minor SaMD revisions shall be identified with a new UDI-PI;Minor SaMD revisions are generally associated with bug fixes, usability enhancements (not for safety purpose), security patches or operating efficiency.Minor revisions shall be identified by manufacturer-specific identification methods (e.g. version, revision number, serial number, etc.)"  
---|---  

# UDI Placement Criteria

| The IMDRF UDI Guidance (IMDRF/UDI WG/N7Final:2013) states that:“a. When the SaMD is delivered on a physical medium, e.g. CD or DVD, each package level shall bear the human readable and AIDC representation of the complete UDI. The UDI that is applied to the physical medium containing the SaMD and its packaging must be identical to the UDI assigned to the system level SaMD. b. UDI should be provided on a readily accessible screen by the user in an easily readable plain-text format (e.g. an “about” file or included on the startup screen).c. The SaMD lacking a user interface (e.g. middleware for image conversion) must be capable of transmitting the UDI through an API.d. Only the human readable portion of the UDI is required in electronic displays of the SaMD. The UDI AIDC marking needs not be used in the electronic displays, e.g. about menu, splash screen, etc…; i.e. SaMD not being distributed by the use of physical carriers (CDs, DVDs or similar) will not carry an AIDC.e. The human readable format of the UDI for the SaMD should include the Application Identifiers (AI) for GS1, and Flag Characters for HIBC, to assist the end user in identifying the UDI and determining which standard is being used to create the UDI."  
---|---  

In relation to those requirements, some additional considerations can be made:

  * In relation to point a), when the SaMD is delivered on a physical medium, e.g. CD or DVD, each package level shall bear the human readable and AIDC representation of the complete UDI. The UDI that is applied to the first packaging level of the physical medium should be identical to the UDI assigned to the system level SaMD. This UDI information – HRI and AIDC - can be placed in a booklet or inlay that accompanies the physical medium. The physical medium itself is not a medical device and therefore does not require a separate UDI. The physical medium may be controlled by its own lot, batch or serial number or by another means of production control; 
  * In relation to point “c”, it shall be noted that middleware might not qualify as medical device in some jurisdictions;
  * In relation to point d), "will not carry" shall be read as "will not be required to", as manufacturers will always be in a position to opt for those SaMD to carry an AIDC. 

| Appendix I provides useful example of UDI assignment for software in relation to issues explored under Sections 12.6.1 and 12.6.2.  
---|---  

# Emerging issues with UDI which are not specifically covered by this Guide

While the application guide provides useful information for the successful implementation of a UDI system by all stakeholders, Regulatory Authorities should be aware that this guidance does not specifically cover certain emerging issues with UDI systems, such as: 

  * contact lens attributes
  * harmonisation of UDI-DI triggers and assignment of other multiple UDI-DI use cases
  * utilization of UDI along the supply chain 
  * SaMD deployment and related UDI responsibilities 
  * tools and device categorization nomenclature for grouping similar devices
  * harmonised structure for information related to data attributes in UDIDs (e.g. clinically relevant size dimensions by device type
  * low unit of measures.
  * issues related to data quality management in UDIDs and data validation criteria

**Appendices**

## **Appendix A:** UDI HRI formats to be used for each of the issuing agencies/entities

  1. **GS1 Standards**

**Issuing Agency/Entity**| **Qualifier**| **Identifier**| **Data type**| **Human Readable Field Size**| **Database Field Size**  
---|---|---|---|---|---  
GS1| (01)| DI| Numeric| 18 (incl. identifier + data delimiter)| 14  
GS1| (11)| Manufacturing/  
Production Date| numeric [YYMMDD]| 10 (incl. identifier + data delimiter)| 6  
GS1| (17)| Expiration Date| numeric [YYMMDD]| 10 (incl. identifier + data delimiter)| 6  
GS1| (10)| Batch/Lot Number| alphanumeric| 24 (max) (incl. identifier + data delimiter)| 20 (max)  
GS1| (21)| Serial Number| alphanumeric| 24 (max) (incl. identifier + data delimiter)| 20 (max)  
_GS1_| | ** _Maximum Base UDI_**| ** _alphanumeric_**|  86| ** _66_**  
**ex: (distinct 01)09506000117843(11)141231(17)201231(10)1234AB(21)5678CD**  

GS1 Sample UDI labels: 

<http://www.gs1.org/sites/default/files/docs/healthcare/udi_label_samples_-_20150317.pdf>

  1. **HIBCC Standards**

**Issuing Agency/Entity**| **Qualifier**| **Identifier**| **Data type**| **Human Readable Field Size**| **Database Field size**  
---|---|---|---|---|---  
HIBCC| +| UDI-DI| Alphanumeric| 7 to 24| 6 to 23  
HIBCC| $| Lot Number Only| Alphanumeric| 19| 18  
HIBCC| $$7| Lot Number Only (alternative option)| Alphanumeric| 21| 18  
HIBCC| $$| Expiration Date followed by Lot Number| Exp. Date: numeric [MMYY]| 6| 4  
Lot Number: alphanumeric| 18| 18  
HIBCC| $$2| Expiration Date followed by Lot Number| Exp. Date: numeric [MMDDYY]| 9| 6  
Lot Number: alphanumeric| 18| 18  
HIBCC| $$3| Expiration Date followed by Lot Number| Exp. Date: numeric [YYMMDD]| 9| 6  
Lot Number: alphanumeric| 18| 18  
HIBCC| $$4| Expiration Date followed by Lot Number| Exp. Date: numeric [YYMMDDHH]| 11| 8  
Lot Number: alphanumeric| 18| 18  
HIBCC| $$5| Expiration Date followed by Lot Number| Exp. Date: numeric [YYJJJ] – Julian Date format| 8| 5  
Lot Number: alphanumeric| 18| 18  
HIBCC| $$6| Expiration Date followed by Lot Number| Exp. Date: numeric [YYJJJHH] – Julian Date format with Hour option| 10| 7  
Lot Number: alphanumeric| 18| 18  
HIBCC| $+| Serial Number only| Alphanumeric| 20| 18  
HIBCC| $$+7| Serial Number only (alternative option)| Alphanumeric| 22| 18  
HIBCC| $$+| Expiration Date followed by Serial Number| Exp. Date: numeric [MMYY]| 7| 4  
Serial Number: alphanumeric| 18| 18  
HIBCC| $$+2| Expiration Date followed by Serial Number| Exp. Date: numeric [MMDDYY]| 10| 6  
Serial Number: alphanumeric| 18| 18  
HIBCC| $$+3| Expiration Date followed by Serial Number| Exp. Date: numeric [YYMMDD]| 10| 6  
Serial Number: alphanumeric| 18| 18  
HIBCC| $$+4| Expiration Date followed by Serial Number| Exp. Date: numeric [YYMMDDHH]| 12| 8  
Serial Number: alphanumeric| 18| 18  
HIBCC| $$+5| Expiration Date followed by Serial Number| Exp. Date: numeric [YYJJJ]| 9| 5  
Serial Number: alphanumeric| 18| 18  
HIBCC| $$+6| Expiration Date followed by Serial Number| Exp. Date: numeric [YYJJJHH]| 11| 7  
Serial Number: alphanumeric| 18| 18  
HIBCC| /S| Supplemental Serial Number, where lot number also required and included in main secondary data string| Alphanumeric| 20| 18  
HIBCC| /16D| Manufacturing Date (supplemental to secondary barcode)| numeric [YYYYMMDD]| 12| 8  
HIBCC| /14D| Expiration Date (supplemental to secondary barcode as optional format)| numeric [YYYYMMDD]| 12| 8  
 _HIBCC_| | ** _Maximum Base UDI_**| ** _Alphanumeric_**| ** _70 to 87_**| ** _58 to 75_**  
**Ex of Human Readable Barcode: *+H123PARTNO1234567890120/$$420020216LOT123456789012345/SXYZ4567890123****45678/16D20130202C***  

HIBCC Sample UDI labels:

<http://www.hibcc.org/wp-content/uploads/2016/02/HIBCC-UDI-Label-Examples.pdf>

  1. **ICCBBA Standards**

**Issuing Agency/Entity**| **Qualifiers**| **Identifier**| **Data type**| **Human Readable Barcode  
Field Size**| **Database Field Size**  
---|---|---|---|---|---  
ICCBBA| =/| UDI-DI| Alphanumeric| 18| 16  
ICCBBA| =,| Serial Number| Alphanumeric| 8| 6  
ICCBBA| =| Donation Identification Number| Alphanumeric| 16| 15  
ICCBBA| =>| Expiration Date| numeric [YYYJJJ]| 8| 6  
ICCBBA| =}| Manufacturing Date| numeric [YYYJJJ]| 8| 6  
ICCBBA| &,1| MPHO Lot Number| Alphanumeric| 21| 18  
ICCBBA| | ** _Maximum Base UDI for HCT/Ps_**| ** _Alphanumeric_**| **79**| **67**  
**Ex of Human Readable Barcode:=/A9999XYZ100T0944=,000025=A99971312345600= >014032=}013032&,1000000000000XYZ123**  
** _Blood Bags Only_**| **Identifying Symbol**| **Identifier**| **Data type**| **Eye Readable Barcode Field Size**| **Database Field Size**  
---|---|---|---|---|---  
ICCBBA| =)| UDI-DI for blood containers (bags)| Alphanumeric| 12| 10  
ICCBBA| &)| Lot Number for blood containers (bags)| Alphanumeric| 12| 10  
 _ICCBBA_| | ** _Maximum Base UDI for Blood Bags_**| ** _Alphanumeric_**| ** _24_**| ** _20_**  
**Ex of Human Readable Barcode: =)1TE123456A &)RZ12345678**  

ICCBBA Sample UDI labels: 

<https://www.iccbba.org/subject-area/medical-devices/label-examples>

## **Appendix B:** AIDC carriers most widely used in healthcare

  1. **GS1 Standards**

  * GS1 Data Matrix with UDI-DI and UDI-PI’s (Expiration Date + Lot/Batch Number)

  * GS1 Data Matrix with UDI-DI and UDI-PI’s (Expiration Date + Lot/Batch Number + Serial Number)

  * GS1-128 concatenated with UDI-DI and UDI-PI’s (Expiration Date + Lot/Batch Number)

  * GS1-128 non-concatenated (shared in 2 parts)

  1. UDI-DI only b) UDI-PI’s (Expiration Date +  
Lot/Batch Number)

 

  * EAN13 with UDI-DI only

  1. **HIBCC Standards**

  * Data Matrix with UDI-DI and UDI-PI’s (Expiration Date + Lot/Batch Number)

  * Code128 non-concatenated with UDI-DI and UDI-PI’s (Expiration Date + Lot/Batch Number)

• QR-Code with UDI-DI and UDI-PI’s (Expiration Date + Lot/Batch Number)

  1. **ICCBBA Standards**

  * ISBT128 with UDI-DI and UDI-PI's (Donation Identification Number, Serial Number, and Expiration Date)

Data Matrix with UDI-DI and UDI-PI’s (Serial Number + Donation Identification Number + Expiration Date)

## **Appendix C:** Examples of RFID carriers

  1. **GS1 Standards**

The data encoded in a GS1 barcode can also be encoded in a RFID tag, provided that a serial number is part of the data elements.

The use of an RFID tag requires that a specific RFID emblem is applied on the label/packaging/device to indicate the presence of radio frequency identification (RFID). The ISO/IEC standard 29160 specifies the design and use of the RFID Emblem.

That standard allows using optionally other signs, such as the EPC (Electronic Product Code) seal, in addition to the required generic RFID Emblem.

The EPC seal is the sign used to notify when unique EPCs are encoded onto RFID tags. GS1's EPC Tag Data Standard (TDS) specifies the data format of the EPC, and provides encodings for numbering schemes -- including the GS1 keys -- within an EPC/RFID. 

Note: today, the relevant GS1 application standards on RFID do not yet address specific location/placement of the RFID Emblem on a label. Relevant CEN standards do state that in the absence of an appropriate application standard, the RFID Emblem shall be placed such that it is easily visible to those trying to read the RFID tag or label. To improve readability, the RFID Emblem should be located near the actual transponder. The visuals below are for example only.

  1. **HIBCC Standards**

A HIBC UDI data string for the Barcode will be encoded with an RFID tag in a 1:1 relation; therefore scanning a Data Matrix with HIBC will yield the same result as scanning a RFID tag.

For RFID applications for UDI the appropriate standards for the product and packaging levels are

  * ISO ISO 17367, Supply chain applications of RFID – Product tagging 
  * ISO ISO 17366, Supply chain applications of RFID – Product packaging

The AIDC and HRI formats are required under the UDI regulation. Therefore, the HRI is not required to be repeated for RFID again, if already present for another type of AIDC format. The ISO/IEC 29160 RFID Emblem is required to be shown as a visible indicator that an RFID is present by a generic RFID Emblem or optional by a RFID Emblem showing frequency and application by a two-character code. This optical visible indicator for frequency and application is helpful in areas where different RFID systems are in use and for diagnostic if a RFID Tag is not read.

The generic RFID Emblem according to ISO/IEC 29160 figure 2:

Fig. Generic RFID Emblem telling “RFID inside”

Table A.1 (below) of ISO/IEC 29160 shows the appropriate RFID emblems for UDI, using a two-character code assignment.

**Table A.1 — Two-character code assignments for the RFID Emblem (excerpt)**

Emblem “B5”: 860-960 MHz (UHF) ISO/IEC 18000-63 ISO 17366 Product packaging

Fig. 1b) RFID Emblem “B5” 

Emblem “B7”: 860-960 MHz (UHF) ISO/IEC 18000-63 ISO 17367 Product tagging

Fig. 2) RFID Emblem “B7” 

Examples of serialized UDI HIBC to be encoded in Barcode and optional RFID  
a) on a product +A999ABC123DE0/$+1234567Y

b) on a package +A999ABC123DE1/$+1234567Y

Fig. 3) UDI applied on a product package with Data Matrix and RFID

Fig. 4) UDI applied on a product with Data Matrix and RFID

 _Note to Fig. 3 and 4: Human Readable Interpretation (HRI) contains the UDI data within an envelope of two Stars (*)_

  1. **ICCBBA Standards**

RFID tags are not currently used to carry identification information for medical products of human origin (MPHO), although some organizations are starting to add an RFID tag as a ‘license plate’ based on the unique tag identifier. This is in addition to the barcoded information and would not carry UDI information.

## **Appendix D:** Examples of registration of packaging configurations

Base package

Higher packaging levels

Base package

Higher packaging levels

NB: Package configurations of a device are part of the same UDI-DI record in the UDID.

## **Appendix E:** Examples of UoU and packaging configurations

## **Appendix F:** Feasibility issues linked to direct marking integrity

**Surface wear / treatment**

Due to mechanical influences during use and preparation, surface abrasion occurs. Directly marked products can thereby lose readability. When reprocessing instruments, regionally different re-processing cycles and in particular cleaners are used (North America - neutral cleaners, Europe - alkaline cleaners). With highly alkaline cleaners, marking fades faster over the entire life cycle.

**Scratches Abrasion on tempering inscription Abrasion**

****

 Damage to the DM due to scratches or inclusions limits the readability of the carrier.

**Corrosion**

 Thermal and deforming influences changes material properties, which lead to corrosion in CoCr alloys. Corrosion causes the code to become unreadable. Corrosion holes can be interpreted by the scanner as marked modules.

**Material**

Thermal melting influences on plastics 

**Reflection / Contrast**

 Picture 1 - The surface is disturbed by inappropriate lighting (e.g. reflection, resolution, contrast). 

Picture 2 - With dark materials, there is a lower 

contrast ratio to the marking, which affects the readability.

_picture 1_

 _picture 2_

**Laser Marking**

Stainless steel or titanium alloys are marked with conventional systems based on an ns-laser (nanosecond laser) via the engraving effect. Too little engraving (tempering inscription) leads to faster fading. 

Passivation of stainless steel with this technique is a mandatory step to avoid corrosion. Passivation is usually done before and/or after the marking.

When marking with a ps-laser (picosecond laser), the material does not get warm due to a very short pulse duration. The surface is slightly roughened, the mark appears jet black and this regardless of the viewing direction. The passivation layer on reusable instruments is not attacked which limits the possibility to corrosion.

**Marking with ns-Laser Marking with ps-Laser**

 _On curved / cylindric devices with a diameter of 3mm a marking is possible._

_Marking 1,25 x 4mm_

 _Marking 1,75 x 5,5mm_

 _The ns-laser marking consists of several engraving lines._

_On curved / cylindric devices with a diameter of 7mm a marking is possible._

The readability of the plain text is independent of the marking method. Because of space reasons a marking of the HRI and AIDCof the UDI might not be always possible.

_1:1_

 _1:1_

 When used properly, the readability of a validated laser marking with a data-matrix is still given after at least 500 cycles. 

(based on experiences made by individual device manufacturers)[24]

## **Appendix G:** Kit Examples

  * **Non-IVD kit examples**

Example 1: This kit contains several different medical devices packaged together to achieve a specific medical purpose (central venous catheter procedures and regional anesthesia) where they are intended to remain packaged together and not replaced, substituted, repackaged, sterilized, or otherwise processed or modified before the devices are used by an end user. The Kit is composed of three trays: one tray for hygiene and disinfection; one tray for preparation of vein puncture, local anesthesia, puncture and fixation; one for catheter placement. 

This kit should be identified with one UDI.[25]

Example 2: It follows the same principles of Example 1 except the kit is customizable to meet health provider preferences. 

Best practice recommendation: While it is the manufacturer that determines when a change to a device constitutes a new model/version of the device, unless there is a relatively small number of potential customizations, using UDI-DIs to differentiate between customized variations is not recommended because it can produce a very large number of UDI-DI records. Instead, differences in customized variation can be accounted for using UDI-PIs.

This kit should be identified with one UDI.

Example 3: Several implant components (including inflatable band, access port and tubing) and multiple sterile accessories (calibration assembly, end plug, closure tool, needles) are together in one package under one label. All the contents of the package are used or disposed of in a single procedure. 

None of the devices in the kit are replaced, substituted, repackaged, sterilized, processed or modified before the devices are used by an end user. 

This kit should be identified with one UDI.

  * **Collection of items not defined as kits examples**

Example 1: A collection of finished and labeled devices that are not necessarily intended to be used together and placed in a box for delivery to the hospital. The content of the box changes from day to day depending on what the hospital orders. 

In the case, the box contains 3 stethoscopes, 6 saline bags, 10 packages of IV tubing, 2 boxes of gloves and 4 cartons of EKG electrodes. 

This is an example of a shipping container and no UDI is required on the shipping container. The collection is not itself a medical device (a “kit”) because the collection is not based on an intended use, but includes a continually varying collection based on what a customer ordered today. Note that each individual item should bear its own UDI. 

Example 2: A manufacturer manufactures two versions/models of a device. Model A is more popular than Model B. To sell more of Model B, the two models, when sent to retailers and distributors, are packaged in an assorted case that always includes 5 of Model A and 3 of Model B, i.e. a standard configuration.

Although both devices may have similar indications for use, Model A and Model B were not combined in a device package with the intent they are used together to achieve a common intended use. Rather, these two or more different models/versions of devices were packaged together for business reasons. 

This package configuration itself is neither a device nor a kit but a shipping configuration.

However, to adequately identify this fixed configuration through distribution and use, packages require UDI.

Recommended best practice is to place a UDI on each device in the packaging configuration and place a UDI on the package that contains the devices. 

  * **Example of an IVD kit (Microbial identification tests)**

Example 1: Contents of kit includes various items (e.g. swabs, reagents, control materials) intended to be used together to detect specific organisms per the device indication. 

The kit is a medical device and requires a UDI. Any items distributed separately require a UDI.

Recommended best practice: if items in this IVD kit are also in other IVD kits, then those individual items should also be identified by a UDI.

## **Appendix H:****** Examples of changes to configurable medical devices

This appendix is intended to describe if and how the System UDI is affected when changes are made to a device, which is already in commercial distribution. 

  * **Changes that makes it necessary to identify the changed devices**

This section provides some examples where changes are made to devices which are in commercial distribution and the change does impact the safety, performance, intended use or indications for use for the device. In these situations, manufacturers must ensure that the changed devices are identifiable. 

Example 1: Upgrade to system which impacts safety and/or performance

AMRI System ‘Model A’ is currently being manufactured and distributed to customers. The manufacturer develops new features and functionality (hardware or software or a combination of both) for that MRI system which are not covered by the original, approved specifications; the new features change the safety profile, the performance of the system or the intended uses. The manufacturer has determined that this results in a new model (“Model B”) of the device. As the manufacturer decides to perform this modification as a new installation he will provide to the modified device a new System UDI. Alternatively, the manufacturer may provide an upgrade kit as a medical device with a separate UDI and this UDI together with original System UDI will be used for the identification of the changed device

Example 2: Component change which impacts safety and/or performance

An X-Ray system with a 50 kV generator is changed to a 100 kV generator. These generator options are not specified for the original configuration(s), and the performance of the system is changed. The manufacturer has determined that this constitutes a new version/model of the system because the change in the generator of the X-ray system results in a new model/version of the system. If the manufacturer decides to perform this modification as a new installation he will provide to the modified device a new System UDI. Alternatively, the manufacturer may provide an upgrade kit as medical device with a separate UDI and this UDI together with original System UDI will be used for the identification of the changed device.

Example 3: New diagnostic feature, not previously approved, added to a device

A new diagnostic algorithm is introduced on a cardiac ultrasound system allowing new data calculations and imaging options. The algorithm introduces new indications for use and changes the performance of the system, and therefore the manufacturer has determined that this upgrade/model change does result in a new model/version of the cardiac ultrasound system according to their documented procedures for assessing device changes. As the manufacturer decides to perform this modification as a new installation he will provide to the modified device a new System UDI. Alternatively, the manufacturer may provide an upgrade kit as medical device with a separate UDI and this UDI together with original System UDI will be used for the identification of the changed device

  * **Examples for Changes where UDI remains unchanged**

This section provides some examples where a change is made to a device which is in commercial distribution, however, the change does not require a special identification of the change device and does not impact the UDI. 

Example 1: System component changed of an installed device; no change in safety or performance

An installed CT system has an x-ray tube which has reached the end of its life and is replaced with a newer model tube by the original manufacturer without other changes to the device or its labeling. The manufacturer has determined that this does not constitute a new version/model of the system, according to their documented and approved description of the configuration (e.g. the safety profile, the performance of the system and the intended use are unchanged). As there is no significant change to the safety, performance or the intended purpose, the UDI remains unchanged.

Example 2: A customer-selectable option changed for an installed device

A CT system has an approved medical device registration/license, which includes several diagnostic algorithms. When a customer orders the device, they can choose which algorithms they would like activated based on their business model and budget. If a customer with an installed system subsequently purchases another diagnostic algorithm (which was approved for that system), due to changing business needs, that additional algorithm may be installed/activated and would not result in a new model/version of the system; the UDI remains unchanged.

Example 3: Addition of an accessory for an installed device

The addition of an accessory that is covered by what is originally specified for the defined groups of configurations does not result in a new model/version of the system. Under this circumstance, the system UDI remains unchanged. 

## **Appendix I:** Example of UDI assignment for software

It is a guiding principle that UDI-PI or/and UDI-DI are only altered in case of changes to the SaMD itself. Please note that, in order to reduce the number of illustrations, all visualizations in this Appendix are constructed in a way that UDI is independent from the issuing entity-specific standards. They are fictitious and solely intended to show the iterations of UDI-DI and UDI-PI for the use cases in a simplified manner.

NB: SaMD version might be captured in the lot UDI-PI in certain national regulations.

NB: SaMD version might be captured in the lot UDI-PI in certain national regulations.

The following examples demonstrate how UDI for Software as a Medical Device (SaMD) can be allocated in case the same SaMD(s) is/are distributed by the use of different media types/channels. The guiding principle is that UDI-DI and UDI-PI of the “RAW” SaMD are not changed (i.e. remains the same) no matter on what media/channel (e.g. CD, DVD, USB-Thumb Drive, SD-Card etc.) the SaMD is distributed. (UDI-PI or/and UDI-DI are only altered in case of changes to the SaMD itself.)

Please note: To reduce the number of illustrations all visualizations are constructed in a way that UDI is independent from the issuing entity-specific standards. They are fictitious and solely intended to show the iterations of UDI-DI and UDI-PI for the use cases in a simplified manner.

Case 1a shows the approach where one SaMD is distributed exclusively by DVD and where the physical media (DVD) is production-controlled by SERIAL NUMBER. In this case the media (DVD) carries the same UDI-DI as the RAW SaMD (SW-Version in ‘BATCH/LOT’) and SERIAL NUMBER is added as an additional UDI-PI (only on the DVD).   
The corresponding entry in the UDI-Database (UDID) indicates both SW/BATCH/LOT-Version and SERIAL NUMBER as UDI-PIs.

Case 1b shows the approach where one SaMD is distributed exclusively by one media (DVD) and where the physical media (DVD) is production-controlled by BATCH/LOT. In this case the media (DVD) is allocated a different DI as the RAW SaMD as BATCH/LOT related to the ‘RAW’ SaMD is already ‘occupied’ by SW-Version.   
There will be two corresponding entries in the UDI-Database (UDID): One reflecting the ‘RAW’ SaMD and one for the physical media. The latter refers in the device description to the record of the ‘RAW’ SaMD. 

Case 2a shows the approach where one SaMD is distributed on different media/channels and where the physical media/channels (USB-Thumb Drive, WWW-Distribution, DVD) are production-controlled by SERIAL NUMBER respectively BATCH/LOT for WWW-Distribution. In this case, the physical media/channels are allocated different DIs/PIs to make them distinguishable from the RAW SaMD. 

In this example there will be four corresponding entries in the UDI-Database (UDID): one reflecting the ‘RAW’ SaMD and one for each physical media/channel. The latter refer in the device description to the record of the ‘RAW’ SaMD. 

Case 2b shows the approach where one SaMD is distributed on different media/channels and where the physical media/channels (USB-Thumb Drive, WWW-Distribution, DVD) are production-controlled by BATCH/LOT. In this case the physical media/channels are allocated different DIs/PIs to make them distinguishable from the RAW SaMD. 

In this example there will be four corresponding entries in the UDI-Database (UDID): one reflecting the ‘RAW’ SaMD and one for each physical media/channel. The latter refer in the device description to the record of the ‘RAW’ SaMD. 

Case 3a shows the approach where more than one SaMD are distributed exclusively by DVD and where the physical media (DVD) is production-controlled by SERIAL NUMBER. In this case the physical media is allocated different DIs/PIs to make it distinguishable from the RAW SaMDs. 

In this example there will be four corresponding entries in the UDI-Database (UDID): three reflecting the ‘RAW’ SaMDs and one for the physical media. The latter refer in the device description to the records of the three ‘RAW’ SaMDs. 

Case 3b shows the approach where more than one SaMD are distributed exclusively by DVD and where the physical media (DVD) is production-controlled by BATCH/LOT. In this case the physical media is allocated different DIs/PIs to make it distinguishable from the RAW SaMDs.

In this example there will be four corresponding entries in the UDI-Database (UDID): three reflecting the ‘RAW’ SaMDs and one for the physical media. The latter refer in the device description to the records of the three ‘RAW’ SaMDs. 

Case 4a shows the approach where more than one SaMD are distributed on different media/ channels and where the physical media/channels (USB-Thumb Drive, WWW-Distribution, DVD) are production-controlled by SERIAL NUMBER respectively BATCH/LOT for WWW-Distribution. In this case the physical media/channels are allocated different DIs/PIs to make it distinguishable from the RAW SaMDs. 

In this example there will be six corresponding entries in the UDI-Database (UDID): three reflecting the ‘RAW’ SaMDs and three for the physical media. The latter refer in the device description to the records of the three ‘RAW’ SaMDs. 

Case 4b shows the approach where more than one SaMD are distributed on different media/channels and where the physical media/channels (USB-Thumb Drive, WWW-Distribution, DVD) are production-controlled by BATCH/LOT. In this case the physical media/channels are allocated different DIs/PIs to make it distinguishable from the RAW SaMDs. In this example, there will be six corresponding entries in the UDI-Database (UDID): three reflecting the ‘RAW’ SaMDs and three for the physical media. The latter refer in the device description to the records of the three ‘RAW’ SaMDs. 

  1. This is also referred to as data delimeter ↑

  2. SaMD version might be captured in the lot Production Identifier under certain national regulations. ↑

  3. The Donation Identification Number, also referred to as a donor number or distinct identification code, corresponds to the donation identification number in ISBT 128. This number is an essential identifier for medical products of human origin. ↑

  4. Medical products of human origin (MPHO) include blood, organs, bone marrow, cord blood, corneas, tissues, reproductive cells and milk derived from humans for therapeutic use. The use of DIC in UDI is limited to MPHO products regulated as medical devices. ↑

  5. It should be noted that regulatory authorities might choose to opt for certain AIDC systems only. ↑

  6. The UDI directly marked on the device should differ from the UDI placed on the label of any package containing that device. This is to distinguish the unpackaged device from any device package containing the device. ↑

  7. From a supply chain perspective the item cannot be replenished at any level lower than the lowest packaged level. ↑

  8. It is important to distinguish the UoU DI from the unit of use package level, which corresponds to the base package. ↑

  9. | According to Section 9.2 of the IMDRF UDI Guidance (IMDRF/UDIWG/N7Final:2013), nomenclature is listed as one of the core UDID data elements.  
---|---  

↑

  10. | Section 9.2 of the IMDRF UDI Guidance (IMDRF/UDIWG /N7Final:2013) provides a list of core UDID data elements  
---|---  

↑

  11. Some jurisdictions might not have a specific process in place to authorize third-party solution providers ↑

  12. | Description of UDI data elements is provided in the document IMDRF/UDI WG/N53 FINAL:2019  
---|---  

↑

  13. In some jurisdictions, catalogue/REF number are included in the UDID and any change to the catalogue/REF number (when provided on the label) will trigger a new UDI-DI. ↑

  14. There are historical reasons for that as manufacturers were the early adopters of UDI standards to facilitate collaborative commerce between trading partners with a specific focus on supply chain. Use of UDI for regulatory purpose has been introduced and consolidated at a later stage. ↑

  15. This risk also limiting the usefulness of UDI for healthcare purposes ↑

  16. It should be recalled that PIs are not recorded in UDIDs. UDIDs are outside the scope of Section 9.0. ↑

  17. It should be noted that the format of certain elements (e.g. date format) may vary depending on jurisdictions requirements. ↑

  18. It should be noted that certain jurisdictions might consider those third-parties as legally responsible for placing the UDI carrier on the label or on the device itself and on all higher levels of device packaging. ↑

  19. It should be noted that certain jurisdictions might consider those third-parties as legally responsible for submission of data to the UDI database ↑

  20. This does not imply a requirement for the UDID to link the UDI-DI of the kit with the UDI-DI of each medical device in the kit that is marked with a UDI. ↑

  21. Jurisdictions may differ in relation to the qualification of these trays as medical devices. ↑

  22. See footnote 21. ↑

  23. An “upgrade kit” (to be distinguished from the term “kit” defined in this document) is a term commonly used in industry to denote a packaged medical device used to upgrade an installed medical device (after this latter has been sold and first use or installation is completed). The “upgrade kit” includes all of the components or constituents required for the medical device upgrade and may also include installation instructions, service manuals and user manuals. ↑

  24. Users should discard using a reusable instrument, if damage (e.g. corrosion, chipping, discoloration, etc.) is seen. ↑

  25. ↑
