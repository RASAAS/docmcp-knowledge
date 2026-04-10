# UDI Guidance: Unique Device Identification (UDI) of Medical Devices

**Document Number**: IMDRF/UDI WG/N7FINAL:2013

**Source**: [https://www.imdrf.org/documents/udi-guidance-unique-device-identification-udi-medical-devices](https://www.imdrf.org/documents/udi-guidance-unique-device-identification-udi-medical-devices)

---

**IMDRF/UDI WG/N7FINAL:2013**

**Final Document**

**Title** : UDI Guidance

Unique Device Identification (UDI) of Medical Devices

**Authoring Group** : IMDRF UDI Working Group

**Date** : 9 December 2013

Despina Spanou, IMDRF Chair

This document was produced by the International Medical Device Regulators Forum. There are no restrictions on the reproduction or use of this document; however, incorporation of this document, in part or in whole, into another document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the International Medical Device Regulators Forum.

Copyright © 2013 by the International Medical Device Regulators Forum.

Contents

1\. Preamble 3

2\. Introduction 3

2.1 Traceability 4

2.2 Identification 4

2.3 Adverse Event Reporting and Field Safety Corrective Actions 4

2.4 Medical errors 5

2.5 Documentation 5

2.6 Other considerations 5

3\. Rationale, purpose and scope 5

3.1 Rationale 5

3.2 Purpose 5

3.3 Scope 6

4\. References 6

5\. Definitions 7

6\. Guidance for a UDI System 9

7\. The UDI 10

8\. UDI Carrier 11

9\. The UDI Database (UDID) 13

9.1 General principles of the UDID 13

9.2 The core UDID data elements 13

10\. Rules for specific device types 15

10.1 Implantable devices 15

10.2 Reusable devices requiring reprocessing between uses 15

10.3 Non IVD kits 15

10.4 IVD Kits 16

10.5 Configurable medical device systems 16

10.6 Software as a Medical Device (SaMD)__ 17 __

10.6.1. UDI Assignment Criteria 17

10.6.2 UDI Placement Criteria 17

11\. Annex 19 

# 1\. Preamble

This document is inscribed in the framework of the International Medical Device Regulators Forum (IMDRF). It replaces the "_Guidance on a Unique Device Identification (UDI) System for Medical Devices_ " adopted by the Global Harmonization Task Force (GHTF) on 16 September 2011. 

The IMDRF Guidance on a "_Unique Device Identification (UDI) System for Medical Devices_ " clarifies and supplements the above mentioned GHTF Guidance by providing non-binding rules for use in the regulation of medical devices, and has been subject to consultation throughout its development.

There are no restrictions on the reproduction, distribution or use of this document; however, incorporation of this document, in part or in whole, into any other document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the IMDRF.

# 2\. Introduction

This guidance provides a framework for those regulatory authorities that intend to develop their UDI Systems that achieves a globally harmonized approach to the UDI. The framework can be used at a local, national, or global level such that these systems are implemented without regional or national differences. This guidance is intended to provide a high-level conceptual view of how a global UDI System should work. It is recognized that further additional guidance may be needed once these core concepts are accepted.

The fundamental concepts of a globally harmonized UDI System include:

  1. the UDI and UDI Carrier are based on standards,
  2. a UDI applied to a medical device anywhere in the world should be able to be used globally and to meet the UDI requirements of its regulatory authority,
  3. national or local identification numbers should NOT be a substitute for UDI,
  4. regulatory authorities should not specify the procedure for modifying these UDI standards
  5. the UDID core elements should not be modified,
  6. the UDID should use the Health Level Seven International (HL7) Structured Product Label (SPL) and web based interface for data submission,
  7. every medical device needs to be identified by a UDI, unless it is exempted

The UDI System is intended to provide a single, globally harmonized system for positive identification of medical devices. Healthcare professionals and patients will no longer have to access multiple, inconsistent, and incomplete sources in an attempt to identify a medical device and, its key attributes. The UDID is a designated source for additional information. It is critical to note that the benefits of UDI can only accrue if all stakeholders, from the manufacturer to healthcare providers and patients, use UDI throughout their workflow systems. Therefore, it is imperative that all stakeholders be educated about the development and use of a UDI System.

A globally harmonized and consistent approach to UDI is expected to increase patient safety and help optimize patient care by facilitating the:

  1. traceability of medical devices, especially for field safety corrective actions,
  2. adequate identification of medical devices through distribution and use, 
  3. identification of medical devices in adverse events,
  4. reduction of medical errors,
  5. documenting and longitudinal capture of data on medical devices.

## _2.1 Traceability_

The global use of a UDI will facilitate traceability throughout distribution.

In order to achieve traceability, it is necessary to involve all stakeholders to capture and store the UDI (Device Identifier (UDI-DI) + Production Identifier (UDI-PI)) throughout distribution and use.

This is especially important for field safety corrective actions. 

Though the UDID does not capture UDI-PI, it is expected that supply chain operators will capture and use these identifiers. This is critical during field safety corrective actions. In addition, the foundational use of UDI can help fight counterfeiting and secure the supply chain for all stakeholders. 

Traceability can be facilitated by[1]:

  1. recording medical devices from manufacturer to healthcare provider throughout the supply chain,
  2. recording medical device use in patients,
  3. implementation of medical device field safety corrective actions, 
  4. a standardized way to input medical device identification into health related registries.

## _2.2 Identification_

UDI will facilitate the unambiguous identification of the medical device through distribution and use by providing a single global identifier that can be used to link and integrate existing government, clinical, hospital, and industry databases. UDI should allow for improved procurement, inventory management, and accounting. The existence of a single UDI-DI to link disparate data bases should allow creative new medical and business applications, and synergy among those applications.

## _2.3 Adverse Event Reporting and Field Safety Corrective Actions_

UDI will allow industry and regulatory authorities to more rapidly identify medical devices involved in adverse events. UDI will be available for inclusion in adverse event reports, allowing greater accuracy in reporting, and more rapid aggregation of related reports. Using this information, Health Authorities can more rapidly collate and analyze problem reports and identify the most-appropriate solution for a particular concern. UDI will allow more targeted safety alerts and field safety corrective actions on the specific medical devices that are of concern.

## _2.4 Medical errors_

By providing rapid and electronic access to critical patient safety information, such as clinical size, sterilization status, etc. related to a medical device, the UDI system may help clinicians more safely select and use the proper medical device for a patient. UDID data could be downloaded by healthcare providers to be used for internal reference of safety related information.

## _2.5 Documentation_

The use of UDI System will facilitate and simplify the documentation of medical device use in various patient records including traditional as well as electronic health records and registries. UDI should also enable linkages of medical device information across various systems and across geographies. These applications of UDI could help identifying medical device problems and enhance comparative effectiveness.

## _2.6 Other considerations_

Other considerations essential for the successful development and implementation of a globally harmonized UDI System include:

  1. a risk-based approach which is essential given the huge diversity of the medical devices,
  2. application to kits, systems and other groups of devices which need to be managed appropriately,
  3. requirements which should be phased in over a period of years based on risk classes, starting with the highest risk class, to reduce the burden of implementation,
  4. the need for all supply chain stakeholders to have sufficient time to prepare their systems, processes and staff, for the proper use of the UDI System,
  5. Effective data retrieval systems.

# 3\. Rationale, purpose and scope

## 

##  _3.1 Rationale_

There are currently no global definitions of what constitutes a UDI or UDI System. As a consequence, discrepancies between different national approaches do exist and will most likely increase. Common globally harmonized UDI System requirements would offer significant benefits to manufacturers, healthcare providers, patients, and regulatory authorities. In addition, a globally harmonized UDI System will limit the cost of regulatory compliance.

## _3.2 Purpose_

This guidance intends to avoid country-specific requirements regarding the core elements of the UDI System by developing common guidance for:

  1. creating, using and maintaining a UDI,
  2. applying a UDI Carrier,
  3. establishing the UDID model/structure, with a defined list of Data Elements,
  4. establishing basic requirements for a data submission format based on HL7 SPL and web based interface and
  5. establishing basic requirements for a common data exchange standard. 

This document does not address the use of the UDI System, e.g. by healthcare providers. Therefore it does not directly address issues associated with counterfeit medical devices or how to enable better control of purchasing which will depend on the use of the UDI System by healthcare providers.

## _3.3 Scope_

This document applies to all products to be placed on the market that are regulated as medical devices. For a definition of a medical device, see the GHTF document entitled "_Information Document Concerning the Definition of the Term “Medical Device_ ”". 

This document is addressed to the regulatory authorities and affects medical device manufacturers and other relevant stakeholders.

# 4\. References

\- GHTF SG1/N071:2012 Definition of the Terms ‘Medical Device’ and ‘In Vitro Diagnostic (IVD) Medical Device’;

\- GHTF SG1/N070:2011 Label and Instructions for Use for Medical Devices;

\- GHTF SG1/N055:2009 Definitions of Terms Manufacturer, Authorized Representative, 

Distributor and Importer;

\- GHTF SG1/N065:2010 Registration of Manufacturers and other Parties and Listing of Medical Devices;

\- GHTF SG1/N77:2012 Principles of Medical Devices Classification

-__ GHTF SG1/N044:2008 Role of Standards in the Assessment of Medical Devices

\- GHTF SG2/N5:2006 Contents of Field Safety Notice

\- IMDRF SaMD WG/N10/FINAL:2013 Software as a Medical Device (SaMD): Key Definitions;

\- ISO/IEC 15459-2 – Information technology - Unique identifiers – Part 2: Registration procedures;

\- ISO/IEC 15459-4:2008 – IT Unique identifiers Part 4: Individual items;

\- ISO/IEC 15459-6:2007 – IT Unique identifiers Part 6: Unique identifier for product groupings;

\- ISO/IEC 16022:2006 – Information technology – Automatic identification and data capture   
techniques – Data Matrix bar code symbology specification;

\- ISO/IEC 18004:2006 – IT AIDC techniques QR Code 2005 bar code symbology specification;

\- ISO/IEC 15417:2007 – IT AIDC techniques – Code 128 bar code symbology specification.

# 5\. Definitions 

_Accessory_

Accessory means an article intended specifically by its manufacturer to be used together with a specific medical device(s), to enable the medical device to be used in accordance with its intended use [modified draft GHTF definition –GHTF/SG1/N071:2012].

_Automatic Identification and Data Capture (AIDC)_

A technology used to automatically capture data. AIDC technologies include bar codes, smart cards, biometrics and RFID.

_Configurable medical device system_

A configurable medical device system consists of several components which can be assembled in multiple configurations. Those individual components may be medical devices itself and/or non-medical devices.

Examples are Computed Tomography (CT) systems, Ultrasound systems, Anesthesia systems, Physiological Monitoring systems, Radiology Information System (RIS). 

_Configuration_

Configuration is a combination of items of equipment, as specified by the manufacturer, that operate together to provide an intended use or purpose as a medical device. The combination of items may be modified, adjusted or customized to meet a customer need.

Examples: 

1\. CT: gantry, tube, table, console are items of equipment that can be configured/combined to deliver an intended function. 

2\. Anesthesia: ventilator, breathing circuit, vaporizer are items of equipment that can be configured/combine to deliver an intended function.

_Device Identifier (UDI-DI)_

The UDI-DI is a unique numeric or alphanumeric code specific to a model of medical device and that is also used as the "access key" to information stored in a UDID. Examples of the UDI-DI include GS1 GTIN (Global Trade Item Number), HIBC-LIC (Labeler Identification Code), ISBT 128-PPIC (Processor Product Identification Code).

_Human Readable Interpretation (HRI)_

Human Readable Interpretation is a legible interpretation of the data characters encoded in the UDI Carrier.

_Implantable device_

Any device, including those that are partially or wholly absorbed, which is intended: -

  * to be totally introduced into the human body or,
  * to replace an epithelial surface or the surface of the eye,

by surgical intervention which is intended to remain in place after the procedure. 

Any device intended to be partially introduced into the human body through surgical intervention and intended to remain in place after the procedure for at least 30 days is also considered an implantable device. [GHTF SG1/N77:2012]

_Kits_

Kits are a collection of products, including medical devices, that are packaged together to achieve a common intended use and is being distributed as a medical device. These could also be called procedure packs or convenience kits.

Note: Jurisdictions may differ in their definition of kit. 

_Label_

Written, printed, or graphic information either appearing on the medical device itself, or on the packaging of each unit, or on the packaging of multiple devices [GHTF/SG1/N070:2011].

_Manufacturer_

Manufacturer means any natural or legal person[2] with responsibility for design and/or manufacture of a medical device with the intention of making the medical device available for use, under his name; whether or not such a medical device is designed and/or manufactured by that person himself or on his behalf by another person(s) [GHTF SG1/N55:2009]. 

This includes reprocessors and remanufacturers that take responsibility for the device and reintroduce it into commercial distribution.

_Own Brand/Private Labelers_

An Own Brand or Private Labeler relabels a device from a 3rd party with his own name without making any further changes to the device thereby taking responsibility for it as the manufacturer.

_Packaging Levels_

Packaging levels means the various levels of device packages that contain a fixed quantity of medical devices, e.g. each, carton, case. 

Note: This does not include shipping containers.

_Production Identifier (UDI-PI)_

The Production Identifier is a numeric or alphanumeric code that identifies the unit of device production. 

The different types of Production Identifier(s) include serial number, lot/batch number, Software as a Medical Device (SaMD) version and manufacturing and/or expiration date.

_Radio Frequency Identification (RFID)_

RFID is a technology that uses communication through the use of radio waves to exchange data between a reader and an electronic tag attached to an object, for the purpose of identification.

_Shipping containers_

Shipping container is a container where the traceability is controlled by a process specific to logistics systems.

_Software as a Medical Device (SaMD)_

The term SaMD is defined as software intended to be used for one or more medical purposes that perform these purposes without being part of a hardware medical device. [IMDRF SaMD WG/ N10R4FINAL:2013] 

_Standard_

Document, established by consensus and approved by a recognized body, that provides, for common and repeated use, rules, guidelines or characteristics for activities or their results, aimed at the achievement of the optimum degree of order in a given context. [GHTF/SG1/N044:2008]

_Unit of Use (UoU) UDI-DI_

The UoU UDI-DI is an identifier assigned to an individual medical device. It is assigned in instances when a UDI is not labelled at the level of the device unit of use (e.g. several units contained in a plastic bag). Its purpose is to associate the use of a device to/on a patient.[3]

_Unique Device Identification_

The UDI is a series of numeric or alphanumeric characters that is created through a globally accepted device identification and coding standard. It allows the unambiguous identification of a specific medical device on the market. The UDI is comprised of the UDI-DI and UDI-PI. 

Note: The word "Unique" does not imply serialization of individual production units.

_UDI System_

The UDI System is the framework for:

  1. UDI production ,
  2. UDI application on the label or on the device, and 
  3. UDI Database (UDID) fundamental contents

 _UDI Carrier_

The UDI Carrier is the means to convey the UDI by using AIDC and, if applicable, its HRI. 

Note: Carriers can include ID/linear bar code, 2D/Matrix bar code, RFID, etc…

 _UDI Database (UDID)_

The UDID contains identifying information and other elements associated with the specific medical device.

# 6\. Guidance for a UDI System

A UDI System comprises 3 parts:

  1. the development of the UDI using globally accepted standards, (see section 7)
  2. the application of that UDI on the label, (see section 8) and 
  3. the submission of appropriate information to a UDID (see section 9).

In order to facilitate a globally harmonized approach to UDI, it is imperative that: 

  1. the marking of the UDI should be an additional requirement – it does not replace any other   
marking or labeling requirements. However UDI should replace any existing medical device   
identifier used in accordance to local regulations with the same purpose of the UDI System;
  2. the manufacturer should create and maintain globally unique UDIs on his medical   
devices;
  3. only the manufacturer can establish the UDI on the device or its packaging. Reprocessors   
of single use medical devices, remanufacturers, relabelers and own brand/private labelers   
are considered the manufacturer of the reprocessed, remanufactured or relabeled device and,   
as such, are also subject to these requirements;
  4. globally accepted ISO/IEC coding standards implemented by global organizations, such as   
GS1, HIBCC and ICCBBA, meet the criteria of the UDI and manufacturers shall be   
permitted to choose which system to use. These organizations have responsibility for   
maintaining the global uniqueness of their coding systems. It is imperative that these coding   
systems be adopted and implemented, without national deviations or changes to these global   
coding systems; proliferation of coding systems must be discouraged;
  5. national or regional regulatory requirements shall not restrict methods of AIDC as this will   
hinder the establishment of a globally harmonized UDI System;
  6. the national/regional regulation for UDI System shall include a robust and transparent   
mechanism for evaluating and adjudicating requests for UDI exemptions in alternative   
placements of UDI-DI and UDI-PI. Such exemptions should cover all the products with the   
same characteristics;
  7. the regulators of the UDI System shall specify harmonized exemptions for certain   
devices such as investigational devices and custom made devices from UDI   
requirements;
  8. common criteria for recognition are:
  9. The employed UDI must meet the requirements of the globally harmonized UDI   
System to adequately identify a device through its distribution,
  10. The employed UDI is in compliance with globally accepted standards ISO/IEC 15459-2, ISO/IEC 15459-4 and ISO 15459-6,
  11. The employed UDI will be available to all users according to a single set of   
consistent fair and reasonable terms and conditions. 

To meet the public health objectives of this guidance and to ensure that medical device user facilities, healthcare providers, regulatory authorities, and others will be able to make efficient and effective use of the UDI System, there could be a need to limit the number of accredited global organizations and available coding systems.

# 7\. The UDI

  1. A UDI shall be assigned to the device itself or its package. Higher levels of packaging shall have their own UDI.
  2. Shipping containers should be exempted. As an example, UDI is not required on a logistics unit; when a healthcare provider orders multiple medical devices using the UDI or model number of individual devices and the manufacturer places these devices in a container for shipping or to protect the individually packaged devices, the container (logistics unit) is not subject to UDI requirements. 
  3. The UDI contains two parts: an UDI-DI and an UDI-PI.
  4. The UDI-DI (e.g., GS1 GTIN, HIBC-LIC, ISBT-PPIC) should be globally unique at all levels of device packaging.
  5. If a lot number, serial number, software version or expiration date appears on the label, they should be part of the UDI-PI. If there also is a manufacturing date on the label, it does NOT need to be included in the UDI-PI. If there is only a manufacturing date on the label, this should be used as the UDI-PI. 
  6. When a UDI is not assigned to the device at the level of its unit of use, then a UoU UDI-DI should be assigned, to associate the use of a device with a patient. [for example, a UoU UDI-DI would be assigned to an individual electrode when the electrode is distributed in a package of 10 – and lowest level UDI is assigned to that package of 10]
  7. Each component, sub-system or accessory that is considered a medical device and is commercially available needs a separate UDI unless the components are part of a convenience, medical procedure, IVD kit or configurable medical device system that is marked with its own UDI.
  8. Kits should have their own UDI.
  9. The manufacturer assigns the UDI to a device following the relevant coding standard.
  10. Any change of one of the following UDID data elements determines the need for a new UDI-DI:
  11. Brand Name,
  12. Device version or model,
  13. Clinical Size (including Volume, Length, Gauge, Diameter),
  14. Labeled as single use,
  15. Packaged sterile,
  16. Need for sterilization before use,
  17. Quantity of devices provided in a package,
  18. Critical warnings or contraindications: e.g. containing latex or DEHP.
  19. At a minimum, a new UDI-DI is required whenever there is a change that could lead to misidentification of the medical device and/or ambiguity in its traceability.
  20. Reprocessors of single use medical devices, remanufacturers, Own Brand/Private Labelers shall create their own, new UDI for the reprocessed, remanufactured, or relabeled medical device which will replace the OEM’s UDI where it exists.
  21. Reprocessors of single use medical devices, remanufacturers, Private (Own Brand) Labelers shall retain record of the Original Equipment Manufacturer’s (OEM) UDI.
  22. A change of the label to display or modify a UDI-DI should not (in and of itself) require a premarket submission and/or re-registration. Manufacturers may be requested to notify/inform the Regulator.

# 8\. UDI Carrier

  1. The UDI Carrier (AIDC and HRI representation of the UDI) shall be on the label or on the device itself and on all higher levels of device packaging. Higher levels do not include shipping containers.
  2. In case of significant space constraints on the UoU package the UDI carrier may be placed on the next higher package level.
  3. The UDI Carrier for single use medical devices of risk class A and B packaged and labeled individually does not need to be on its package but rather on higher level of packaging e.g. carton. However when the healthcare provider is not expected to have access (home healthcare settings) to the higher level of device packaging, the UDI should be on its package.
  4. Non-prescription medical devices exclusively for retail Point of Sale (POS) do not need to encode Production Identifiers in AIDC on the point of sale package.
  5. No particular AIDC methods should be required by a regulatory authority. Globally accepted AIDC methods based on ISO standards that have been adopted by the global organization (e.g., GS1, HIBCC or ICCBBA) shall be used.
  6. RFID should comply with open, commercially acceptable, international standards such as ISO 17366:2013 Supply chain application of RFID – Product packaging and be vendor neutral.
  7. When AIDC carriers other than the UDI Carrier are part of the product labeling, the UDI Carrier shall be readily identifiable. 
  8. If linear bar codes are used, the UDI-DI and UDI-PI can be concatenated or non-concatenated in two or more bar codes. All parts and elements of the linear bar code shall be distinguishable and identifiable.
  9. If there are significant constraints limiting the use of both AIDC and HRI on the label, the AIDC format shall be favored. However, certain environments or use situations, such as home care, may warrant the use of HRI over AIDC. 
  10. The HRI format shall follow the rules of the UDI code issuing organization.
  11. In case of RFID, a linear or 2D bar code shall also be provided on the label.
  12. Medical devices that are reusable should have a UDI Carrier on the device itself.

The UDI Carrier of reusable medical devices that require reprocessing between   
patient uses should be permanent and readable after reprocessing cycles for the   
intended life of the device. Manufacturers may determine that this may not be   
possible or warranted on some devices due to size, design, materials, processing,   
or performance issues.

  1. The UDI Carrier should be readable during normal use and throughout intended life of the medical device. 
  2. If the UDI Carrier is readily readable through the medical device’s package, then the UDI Carrier does not also need to be on the package.
  3. A single finished medical device made up of multiple parts that have to be assembled may have the UDI Carrier only on one part. 
  4. The placement of the UDI Carrier should be done in a way that AIDC method can be accessed during normal operation or storage. 
  5. The bar code carrier(s) that includes UDI data identifiers “DI” and “PI” may also include essential data for the medical device to operate. The UDI issuing agencies identify these data elements by application identifiers or flag characters. The regulator shall not limit the use of the UDI carrier to only “DI” and/or “PI” data but allow for other relevant data.

Example: 

GS1 General Specification allows for Application Identifier (91) through (99) for company use. This data could be used by the manufacturer as an activation key for a device or IVD analyzer. A GS1 bar code could carry (01) GTIN (17) expiration date (10) LOT (91) internal device activation key. Standard scanners set in the GS1 mode will parse the 4 data elements. (01) is the static DI, (17) and (10) are dynamic PI data. 

They could be uploaded into hospital inventory systems. (91) would be ignored by the MMIS system but if the product is then placed into use, this AI data could activate the medical device .

# 9\. The UDI Database (UDID)

# _9.1 General principles of the UDID_

  1. The UDID shall support the use of all the core UDID data elements.
  2. No product commercial confidential information shall be included in the UDID.
  3. The manufacturer is responsible for the initial submission and updates to the identifying information and other medical device data elements in the UDID.
  4. Appropriate methods/procedures for validation of the provided data shall be implemented.
  5. The manufacturers shall periodically reconfirm all the data relevant to their medical devices, except for discontinued medical devices. 
  6. The core data elements in the UDID shall be accessible to the public free of charge.
  7. The presence of the medical device UDI-DI in the UDID does not mean that the medical device is authorized in all jurisdictions. 
  8. The database should allow for the linking of all the packaging levels of the medical device.
  9. The data for new UDI-DI must be available at the time the medical device is placed on the market. 
  10. Manufacturers should update the relevant UDID record within 30 days when a change is made to an element that does NOT require a new UDI-DI.
  11. The UDID shall use HL7 Structured Product Labeling (SPL) standard for data submission and updates. Additional submission means could also be accommodated.
  12. The core elements are the minimum elements needed to identify a medical device through distribution and use. Regional or National UDID may contain additional elements; these additional elements should be kept to a minimum.
  13. The design of the UDID should support the official languages required in the jurisdictions where the medical device is put on the market. The use of free-text fields should be minimized to reduce the burden of language translations.
  14. Data relating to discontinued medical devices shall be retained in the UDID. 

# _9.2 The core UDID data elements_

All the core UDID data elements are mandatory, unless marked “optional”. “If applicable” means the information is mandatory to be in the UDID if it is on the label. 

Data elements and their definitions for the UDID are listed below:

  1. For every device packaging level – the following shall be provided in a related way (for entire packaging hierarchy):

  * UDI-DI (UDI type, e.g. GS1 GTIN, HIBC-LIC, ISBT-128 PPIC),
  * Quantity per package configuration: (e.g., each, 10 each, 5 shelf packs),
  * Additional device identifier(s) (if applicable) e.g. GS1, HIBC, or ISBT-128;

  1. The Unit of Use UDI-DI (see section 7.6) code; 
  2. Manufacturer’s name (if applicable);
  3. Manufacturer’s address (if applicable~~)~~ ; 
  4. Manufacturer's customer service contact information (country/region specific, could be multiple);(If applicable)
  5. Authorized Representative's name (regional representatives responsible for the medical device) (country/region specific, could be multiple) (if required by the local/regional regulatory authority) (see GHTF/SG1/N55:2009); 
  6. Authorized Representative's contact information (country specific, could be multiple);
  7. Global Medical Device Nomenclature (GMDN) preferred code/term (valid at the time of the UDI submission);
  8. Brand Name (if applicable);
  9. SaMD version;
  10. Device model or version; (see section 10.6)
  11. Reference and/or catalogue number (if applicable);
  12. How the device is controlled: serial, lot/batch number, and/or expiration date (or manufacturing date) or software version or software released date or ISBT-128 – check boxes (if applicable); 
  13. Clinical Size (including Volume, Length, Gauge, Diameter) (if applicable) (e.g. 8F catheter); 
  14. Additional product Description (optional) – Additional clinically relevant information, e.g. radio-opaque;
  15. Storage conditions, as labeled or in the IFU (if applicable) – to include temperature range, needs to be refrigerated, relative humidity range, pressure range, avoid direct sunlight;
  16. Handling conditions (if different than storage conditions), on the label or in the IFU (if applicable) – to include temperature range, needs to be refrigerated, relative humidity range, pressure range, avoid direct sunlight;
  17. Labeled as single use? (Yes/No);
  18. Packaged sterile? (Yes/No);
  19. Need for sterilization before use? (Yes/No) – _if yes, then the method of sterilization should be indicated_ ;
  20. Restricted number of reuses (if applicable);
  21. License and/or marketing authorization or registration number (if required by the relevant regulatory authority)
  22. URL for additional information, e.g. electronic IFU (optional);
  23. Critical warnings or contraindications (as labeled) – if a particular regulation requires that the label of the device contains a critical warning or contraindication associated with the use of the device 
  24. [e.g.: Labeled as containing latex? (Yes/No),
  25. Labeled as containing DEHP? (Yes/No)
  26. Labeled as MRI compatible? (Yes/No).]
  27. Date of discontinuance (referring to devices no longer placed on the market).

# 10\. Rules for specific device types

##  _10.1 Implantable devices[4]_

Implantable devices should follow the rules listed below:

  1. All unit packs of implantable devices (lowest level of packaging) need to be identified/AIDC   
marked with an UDI (UDI-DI + UDI-PI);

2\. PI should have the following characteristics: 

  1. serial number for active implantable devices,
  2. serial number for other implantable devices or lot number according to the manufacturer's   
quality management system;

3\. The UDI of the implantable device must be identifiable prior to implantation. For example:   
tear-away tag bearing the UDI, peel-off labels bearing the UDI affixed to autoclave box   
holding the implantable device.

## _10.2 Reusable devices requiring reprocessing between uses_

  1. The UDI of these products shall be on the device and be readable after each reprocessing;
  2. PI characteristics (e.g. lot or serial number) shall be defined by the manufacturer according   
to the manufacturer's quality management system;

## _10.3 Non IVD kits_

  1. The manufacturer of the Kit is responsible for identifying the Kit with a UDI including both UDI-DI and UDI-PI;
     1. Orthopedic procedure trays whose contents are configured for a specific order are exempted from this UDI requirement. 

Example: a hospital orders 30 different orthopedic devices for total joint replacement surgery. The 30 devices are delivered to the hospital in a stainless steel box where the devices can be stored and sterilized by the hospital when needed. After a procedure the hospital may replace used parts and re-sterilize the box with its contents;

  1. Medical device contents of Kits should have a UDI Carrier on their packaging or on the device itself.

_Exemptions_ :

  1. Individual single-use disposable medical devices within a Kit, whose uses are generally known to the persons by whom they are intended to be used, and which are not intended for individual use outside the context of the Kit do not require their own UDI Carrier.

Example: an unpackaged sterile syringe within a sterile Kit cannot be used for another procedure due to the lack of a sterile barrier once removed from the Kit;

  1. Medical devices that are normally exempted from having a UDI Carrier on the relevant level of packaging do not need to have a UDI Carrier when placed within a Kit.
  2. Placement of the UDI Carrier on Kits:
  3. The Kit UDI Carrier is generally affixed to the outside of the packaging;
  4. The UDI must be readable or in the case of AIDC scan able, whether placed on   
the outside of Kit package or inside a transparent package.

## _10.4 IVD Kits_

IVD kits should follow the rules listed below:

  1. The manufacturer of the IVD Kit is responsible for identifying it with a UDI including both UDI-DI and UDI-PI,
  2. Medical device contents of IVD Kits should have a UDI Carrier on their packaging or on the device itself,
     1. The IVD Kit is a device and all aspects of this guidance that is relevant apply to it. If an IVD Kit does not include any components which on their own are considered medical devices the only UDI is the UDI of the kit itself;
     2. Reagents used in automated systems bear barcodes necessary for their handling and identification by the automated systems. This does not constitute a UDI;
     3. Individual single-use medical devices packaged within an IVD Kit, whose uses are generally known to the persons by whom they are intended to be used, and which are not intended for individual use outside the context of the IVD Kit do not require their own UDI Carrier;
     4. Medical devices that are normally exempted from having a UDI Carrier on the relevant level of packaging do not need to have a UDI Carrier when placed within an IVD Kit.
  3. Placement of UDI on IVD Kits:
     1. The IVD Kit UDI is generally affixed to the outside of the packaging;
     2. The UDI must be readable or in the case of AIDC scan able, whether placed on the outside of the IVD Kit package or inside a transparent package.

## _10.5 Configurable medical device systems_

For configurable medical device systems the rules listed below should be followed:

  1. A UDI is allocated to the entire, configurable medical device system and is called the System   
UDI.
  2. The system UDI-DI is allocated to defined groups of configurations, not per configuration   
within the group. A group of configurations is defined as the collection of possible   
configurations for a given product line as described in a regulatory file. 
  3. A system UDI-PI is allocated to each individual system. A later change of a component, sub-  
systems or accessory of the system does not change the UDI-PI of the system.
  4. The carrier of the System UDI should be put on the assembly that most likely does not get   
exchanged in its lifetime and should be identified as the System UDI. 

Each component, sub-system or accessory that is considered a medical device and a   
distributed or supplied unit needs a separate UDI;

6\. A new UDI-DI is required when the activities performed results in modifications to a   
previously marketed device intended for resale leads to a new medical device. 

7\. A new UDI-DI is not required when the activities performed do not result in a   
change/modification in performance, safety and/or intended use, of a previously marketed   
device intended for resale. The activities shall be performed in accordance with the   
manufacturer’s instructions.

_10.6 Software as a Medical Device (SaMD)_

****_10.6.1 UDI Assignment Criteria_

The UDI should be assigned at the system level of the Software as a Medical Device (SaMD). 

The version number of the SaMD is considered the manufacturing control mechanism and should be displayed in the UDI-PI.

The following change of a SaMD would require a new UDI-DI:

  * Major SaMD revisions shall be identified with a new UDI-DI;

Major SaMD revisions are meant as complex or significant changes affecting

  1. the original performance and effectiveness,
  2. the safety or the intended use of the SaMD,

These changes may include new or modified algorithms, database structures, operating platform, architecture or new user interfaces or new channels for interoperability. 

The following change of a SaMD would require a new UDI-PI (not a new UDI-DI), 

  * Minor SaMD revisions shall be identified with a new UDI-PI;

Minor SaMD revisions are generally associated with bug fixes, usability enhancements (not for safety purpose), security patches or operating efficiency.

Minor revisions shall be identified by manufacturer-specific identification methods (e.g. version, revision number, serial number, etc…) 

****_10.6.2 UDI Placement Criteria_

  1. When the SaMD is delivered on a physical medium, e.g. CD or DVD, each package level shall bear the human readable and AIDC representation of the complete UDI. The UDI that is applied to the physical medium containing the SaMD and its packaging must be identical to the UDI assigned to the system level SaMD. 
  2. UDI should be provided on a readily accessible screen by the user in an easily-readable plain-text format (e.g. an “about” file or included on the startup screen).
  3. The SaMD lacking a user interface (e.g. middleware for image conversion) must be capable of transmitting the UDI through an Application Programming Interface (API).
  4. Only the human readable portion of the UDI is required in electronic displays of the SaMD. The UDI AIDC marking needs not be used in the electronic displays, e.g. about menu, splash screen, etc…; i.e. SaMD not being distributed by the use of physical data carriers (CDs, DVDs or similar) will not carry an AIDC.
  5. The human readable format of the UDI for the SaMD should include the Application Identifiers (AI) for GS1, and Flag Characters for HIBC, to assist the end user in identifying the UDI and determining which standard is being used to create the UDI. 

**11\. Annex**

**Category**| **Unpacked UoU** 🡪 Direct Part Marking (DPM)| **Base****Package**| **Bulk Package** Higher package configuration| **Remarks**  
---|---|---|---|---  
**Single-use MD**|  | | |   

  * IMDRF class A (low-risk)

| -| -| DI + PI| 

  * Flexibility on possible exemption for PI

  * IMDRF class B (medium-r.)

| -| -| DI + PI|   

  * IMDRF classes C+D (high-r.)

| -| DI + PI| DI + PI|   
**Reusable MD**| | | | 

  * Require reprocessing between uses

  * All risk-classes 

| DI + PI| DI + PI| DI + PI| 

  * Not all package levels necessarily exist, e.g.: surgical instruments, intravenous (IV) infusion pumps.

**Implantable MD**| | | | 

  * PI = Serial number for active implants

  * Sterile

| -| DI + PI| DI + PI| 

  * Usually single packed (1 piece)

  * Non-sterile

| Must be identifiable| DI + PI| DI + PI| 

  * Often multiple packed ("n" pieces)
  * Not necessarily DPM, other technological options allowed to identify the unpacked MD

**Others**|  |  |  |   

  * Kits (IVD / non-IVD)

| -| DI + PI| DI + PI| 

  * Concerns the kit package itself

  * SaMD

| DI + PI| DI + PI| -| 

  * Must not necessarily be packed 

  * Configurable MD Systems

| DI + PI| -| | 

  * AIDC carrier to be placed on a ‚main part‘ 

(primary mode of action)  

  * OTC exclusively

| -| -| DI (linear bar code)| 

  * Point-of-Sale scanners can‘t work with PI

  * OTC + other channels

| -| -| DI + PI (non-concatenated)| 

  * PI should be presented in a separate AIDC carrier due to Point-of-Sale scanners

  1. In the case of medical devices containing medical products of human origin, the traceability chain must, for purposes of vigilance, begin with the donor, and trace the human material through all of its processing steps. For these kind of devices the ISBT 128 system has been developed to ensure a complete traceability chain from donor to patient as required for medical devices containing medical products of human origin.

. ↑

  2. The term “person” that appears here includes legal entities such as a corporation, a partnership or an association. ↑

  3. Because of their nature, the Unit of Use is not appropriate to _in vitro_ diagnostic medical devices. ↑

  4. For the definition refer to GHTF SG1/N77:2012. ↑
