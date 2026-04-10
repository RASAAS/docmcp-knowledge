---
title: 
---

# 

**文件编号**: IMDRF/AET WG/N85 FINAL: 2024

::: tip 官方来源
[https://www.imdrf.org/documents/common-data-set-adverse-event-data-exchange-between-imdrf-regulators](https://www.imdrf.org/documents/common-data-set-adverse-event-data-exchange-between-imdrf-regulators)
:::

<!-- fulltext-start -->

---

## 全文

# Common Data Set for Adverse Event Data Exchange Between IMDRF Regulators

**Document Number**: IMDRF/AET WG/N85 FINAL: 2024

**Source**: [https://www.imdrf.org/documents/common-data-set-adverse-event-data-exchange-between-imdrf-regulators](https://www.imdrf.org/documents/common-data-set-adverse-event-data-exchange-between-imdrf-regulators)

---

Final Document  
---  
IMDRF/AET WG/N85 FINAL: 2024  
Common Data Set for Adverse Event Data Exchange Between IMDRF Regulators   
Authoring Group  
Adverse Event Terminology Working Group  

Preface

© Copyright 2023 by the International Medical Device Regulators Forum. 

This work is copyright. Subject to these Terms and Conditions, you may download, display, print, translate, modify and reproduce the whole or part of this work for your own personal use, for research, for educational purposes or, if you are part of an organisation, for internal use within your organisation, but only if you or your organisation do not use the reproduction for any commercial purpose and retain all disclaimer notices as part of that reproduction. If you use any part of this work, you must include the following acknowledgement (delete inapplicable): 

“[Translated or adapted] from [insert name of publication], [year of publication], International Medical Device Regulators Forum, used with the permission of the International Medical Device Regulators Forum. The International Medical Device Regulators Forum is not responsible for the content or accuracy of this [adaption/translation].” 

All other rights are reserved and you are not allowed to reproduce the whole or any part of this work in any way (electronic or otherwise) without first being given specific written permission from IMDRF to do so. Requests and inquiries concerning reproduction and rights are to be sent to the IMDRF Secretariat. 

Incorporation of this document, in part or in whole, into another document, or its translation into languages other than English, does not convey or represent an endorsement of any kind by the IMDRF. 

**Jeff Shuren, IMDRF chair**

Content

1\. Introduction 4

2\. Scope 5

3\. References 6

4\. Common Data Set (CDS) 7

5\. Reasons for Data Sharing 8

6\. Format for Sharing Common Data Set 9

7\. How to Exchange Information 13

8\. Confidentiality Of Data 14

Definitions 15

Appendix A 16

Appendix B 44

Appendix C 45

# Introduction 

This document has been prepared by the IMDRF Adverse Event Terminology Working Group (AET WG), charged with developing a harmonized terminology for reporting adverse events related to medical devices including in-vitro diagnostics (IVDs).

Since GHTF SG2/N54 (Medical Devices Post Market Surveillance: Global Guidance for Adverse Event Reporting for Medical Devices) was published in 2006, most GHTF members implemented adverse event reporting systems aligning with the general principles of N54. Building on the work of N54, the IMDRF AET WG developed globally harmonized terminology and codes for product problem, cause investigation, health effects, and components (IMDRF/N43). Widespread use of a single, appropriate adverse event terminology and coding system is expected to improve signal detection and validation by adverse event management systems enabling a faster response by both industry and regulatory authorities for public health safety. 

As both regulators and industry work towards implementation of IMDRF terminology, an important next step is establishing a “Common Data Set” (CDS) for global adverse event report information exchange, so that all stakeholders can utilize the full potential of the IMDRF Terminology for signal detection and trend analysis (similar to the ICH E2B standard in pharmacovigilance). Therefore, following the completion of all IMDRF Terminology (IMDRF/N43: Edition 4 2020) and outlining the process for future maintenance, (IMDRF/N44: Edition 3 2020), the group has started the process toward a CDS by reviewing the current adverse event reporting datasets collected by representative IMDRF member jurisdictions to develop a common data set for data exchange as well as guidelines for the exchange of adverse event data between regulators. This CDS will then be used to by regulators to exchange data for signal detection, with the aim of expanding it to the final goal of a harmonised CDS for global adverse event reporting. 

This document is not defining how to detect and validate signals or how the jurisdictions should manage them. This document only applies to the actual exchange of adverse event data, based on the common data set.

# Scope 

This document is intended to provide guidance on the CDS:

  * Defining the draft CDS fields and format 
  * Reasons for sharing.
  * Format for sharing.
  * Guidance on confidentiality.

# References

The following documents were used in the development of this document.

  * IMDRF/AE WG/N43 FINAL:2020 (Edition 4) IMDRF terminologies for categorized Adverse Event Reporting (AER): terms, terminology structure and codes
  * IMDRF/RPS WG/N19 FINAL:2016 Common Data Elements for Medical Device Identification
  * IMDRF/RPS WG/N45 Final :2017 Data Exchange Guidelines – Common Data Elements for medical Device Identification 
  * IMDRF/NCAR WG/N14FINAL:2023 (Edition 4) Medical Devices: Post-Market Surveillance: National Competent Authority Report Exchange Criteria and Report Form
  * IMDRF/GRRP WG/N47 FINAL:2018 Essential Principles of Safety and Performance of Medical Devices and IVD Medical Devices 
  * GHTF/SG2/N54R8:2006 Post Market Surveillance: Global Guidance for Adverse Event Reporting for Medical Devices Appendix A
  * GHTF/SG2/N87:2012 An XML Schema for the electronic transfer of adverse event data between manufacturers, authorized representatives and National Competent Authorities (Based on GHTF/SG2/N54: 2006)
  * IMDRF member jurisdiction’s adverse event reporting data-sets

# Common Data Set (CDS) 

The common data set is mostly compromised of a subset of the Universal Data Set from GHTF N54 published 15 years ago, but it also adds some additional elements which were widely collected by IMDRF members in their present reporting templates. 

There were numerous fields which the WG believed could possibly be harmonized in the future, but at present, the WG defined the minimum data set for exchange for signal detection whilst maintaining data protection.

The CDS will be updated and reviewed in the future based on learning from the exchange of data. 

The elements of the CDS at this time are defined at a high level, to allow each regulator to map their individual fields into the CDS. Formats for each field include string (alpha-numeric free text), date, picklist, and numeric. The picklist of the current CDS is understood to be a combination of each regulator’s picklist, to be further examined and harmonized in the future. 

Key points to note:

  * Not all IMDRF jurisdictions may gather all information included in the CDS, in which case only the available fields should be shared.
  * Only the most recent version of the report should be shared.
  * Data should be input into this CDS “as is” with only minimum (if any) complex re-mapping or extraction/conversion of data to “fit” the CDS- as the focus is on sharing the data. 
  * Clinical Trial/Premarket will not be exchanged.
  * Non industry reports will not be exchanged.

While the adverse event reporting system used for drugs employs a standard reporting format (Individual Case Safety Reports based on the ICH E2B standard) and global database (VigiBase, maintained by the WHO), the scope of this current common dataset is limited to data exchange between regulators. This includes details of what data should be considered for exchange as well as details of how the data can be exchanged. This document does not prescribe or suggest when a Regulator my consider the exchange data. It is up to the Regulator in individual jurisdictions to determine when they will share their data. 

This exchange differs from the NCAR exchange as this is the sharing of the actual adverse event data. This data exchange could lead to an NCAR being sent or could occur as follow-up to an NCAR.

(See Appendix A for detail of elements in the CDS.)

# Reasons for Data Sharing 

There are multiple reasons why data might need to be shared/exchanged. The following are examples of why jurisdiction may decide to exchange data.

  * Sharing on demand when one jurisdiction has a need/request.
  * Identifying whether a trend is a local or global trend.
  * Global signal analysis/identification.
  * Development and testing of analytical algorithms.
  * Learning for data collection harmonization for effective signal identification.

Data sharing/exchange may be between two jurisdictions or across multiple jurisdictions. It is expected that any jurisdiction that requests data will share any findings from their review back to the jurisdiction providing the data.

# The Exchange of Information

**How to request information**

When requesting information from another jurisdiction it is essential that the request is very clear so that the recipient can easily understand the incident reports that need to be included in the data set that is shared. 

The CDS form must be used. The form consists of two sections:

  1. A data request section that is completed by the requestor and provided to those NCAs from whom data is requested. 
  2. A data response section that is completed by the responder and should be included with the data in the response.

The form template can be found in Appendix C.

The detail below outlines how each section of the form should be completed by the requestor and the responder. 

  1. **Details to be completed by the Requestor.**

**Title of the Request**

The requestor should include a short name for the request that the responder can use in the filename of the response that is provided.

**Request Details**

This section of the form should detail who the request is from.

It should also detail when the request is being made and the expected/requested date for a reply.

**Specific Detail of the Request**

This section should detail the information that is being sought. A detailed description of what is being sought should be provided followed by guidance on how the data should be searched using the IMDRF codes.

An outline of the priority or most important codes of interest, or in which sequence the codes should be searched e.g. the search should be conducted using Annex A codes first then Annex E and then Annex G. A listing of all cases with Annex A codes should be provided with those case that include Annex A and Annex E and/or G highlighted.   
Relevant documents or links to relevant documents can be provided. 

Where the request requires an unusual / different timeframe of interest this should be specified, and rationale provided e.g. implantable devices may require a different time period.

As the requester of information, you may need to filter the data you receive.

This is to minimise the burden on the jurisdiction sharing the data, and to maximise the data shared, as some fields may not be collected by some jurisdictions or be provided by adverse event reporters. 

**Scope of the Request**

Select the appropriate sentence that best describes the “Type of request” and “the focus of the request”.

**Specific Search Criteria**

Date Period 

By default, the date period refers to the “initial date of receipt” field detailed in the CDS. 

If the search requires a different date (e.g. awareness date), please provide details in the “Specific Detail of the Request”.

Specific Device Details

Where applicable for the request use the options listed to identify the device of interest.

If the request is not specific to a device the field can be left blank.

Manufacturer Details

Please provide details of the Manufacturer’s name/manufacturers’ names. 

If the request is not specific to a manufacturer the field can be left blank.

**IMDRF Codes of Interest**

In this section, please detail the IMDRF codes of interest.

Where you wish to have a particular focus on specific codes, please detail your requirements in the “Specific Detail of the Request”.

Care should be given to the level of codes (parent or child) requested, as not all jurisdictions use all levels. By default, if you request a parent term the response should include all the associated child terms.

  1. **Details to be completed by the Responder.**

**Responder Details**

This section of the form should provide details of the organisation that is responding to the request, including the responder’s name and email address.

**Specific details of how the data was generated.**

This section should detail how your organisation has generated the data provided. 

Details of the specific search criteria used should be included.

Where you may have deviated from the original request. E.g. Date field, codes level, this should be highlighted and explained.

Where delayed reporting by the manufacturer may impact the number of reports this should be highlighted.

**Additional Comments**

Additional information can be included in this section to assist the requestor in the interpretation of the data you provided or any observation that you have noted when collating the data that you think may assist the requestor. 

# Format for Sharing Common Data Set 

General guidelines on the sharing of data include (See Appendix A for field level formats)

  * Use spreadsheet file with the defined column headers detailed in Appendix A 
  * One line for one report for one device (Incidents reported with multiple devices involved must be split into multiple lines)
  * In case a single cell contains multiple values, e.g. IMDRF adverse events codes of a single annex, these need to be separated by a semi colon, without any padding spaces.
  * In case the jurisdiction does not collect a specific field the exact string ‘ _Not collected’_ is to be used. 
  * Where no data is provided but the specific field is collected by the jurisdiction the convention is to include the field but to leave it blank.
  * The spreadsheet should be named following the guidance in Appendix A, including the “request title**”** provided in the request form.

Note: The format may be subject to change in the future to facilitate data quality checks, e.g., by sharing via XML format accompanied with a XSD to validate the data, or to allow directly for advanced queries by exchange via database formats such as SQLite.

# How to Exchange Information

It is recommended that the Common Data set should be shared via secure email. 

The IMDRF Adverse Event Terminology Working Group will establish and maintain a list of a contact points for the purpose of the exchange of Common Data Set. A copy of the latest version of the contact point listing will be made available to all jurisdictions and entities associated with the IMDRF. 

When circulating a CDS or requesting data from another jurisdiction the cover email should detail the reason why the data is being sought or provided and the confidentiality arrangement that is supporting the exchange or the request (see section 9.0 below). 

The email should also detail a recommended deadline for the response to the requested information. 

In some instances, where the content of a CDS supports or supplements the content of an NCAR that is being exchange under section 4.1 **Exchange criteria** of the Medical Devices: Post-Market Surveillance: National Competent Authority Report Exchange Criteria and Report Form IMDRF/NCAR WG/N14FINAL:2023 (Edition 4), the CDS could be added as an appendix to the NCAR. 

# Confidentiality Of Data 

Adverse event reports may contain confidential information. Different jurisdictions consider different information confidential. When sharing reports, all parties must take all precautions to keep data secure. 

  * Jurisdictions should only share data with other jurisdictions with whom they have confidentiality arrangements – either through Memoradum of Understanding (MOU) or Data Sharing Agreements (DSA). In either case, the exchange of incident level data should be allowed in the agreements.
  * Jurisdictions must satisfy themsleves that the incident level data they hold may be shared with other jurisdictions e.g that the originator of the data has consented (some jurisdictions have overarching regulations/laws that allow this)
  * Any aggregation/reporting/analsyis on the data should carefully follow the agreements in place between jurisdictions. Data received from a jurisdiction may not be shared with another jurisdiction however it may be possible to share aggregate analysis results with other jurisdiction if no individual data is shared.
  * None of the information shared may be released without the explicit authorization of the authoring NCA.
  * Each jurisdiction should determine the appropriate measures to assure secure exchange and storage of data in accordance with the agreements that are in place between parties
  * Data should be destroyed when it is no longer needed.
  * No data which can identify individual patient(s) can be shared among jurisdictions.

# Definitions

### 

Term | Meaning   
---|---  
**Sqlite**|  SQLite is an embedded SQL database engine that requires no configuration and reads and writes directly to ordinary disk files.  
**XML (Extensible Markup Language)**| **XML Extensible Markup Language is** a condensed form of Standard Generalized Markup Language (SGML) that enables developers to create customized tags that offer flexibility in organizing and presenting information. XML enables data to be organized and exchanged in ways that were previously impossible or very difficult. By using customised XML schemas, specific pieces of business data can be identified and extracted from ordinary business documents.****  
**XSD** (**XML Schema Definition**),| **XSD** (**XML Schema Definition**), a recommendation of the World Wide Web Consortium (W3C), specifies how to formally describe the elements in an Extensible Markup Language (XML) document. It can be used by programmers to verify each piece of item content in a document, to assure it adheres to the description of the element it is placed in.  
|   
|   

# Appendix A – Common Data Set Elements

Contents

File information 18

File type 18

Naming convention 18

Headers 18

A. Administrative Information 20

A.1 Regulatory authority providing information 20

A.2 Language of Report 20

A.3 Regulatory authority reference number 21

A.4 Submitter reference number 21

A.5 Initial date of receipt 21

A.6 Latest date of receipt 22

A.7 Date of incident 22

A.8 Submitter awareness date 23

A.9 Report version 23

A.10 Classification of incident 24

A.11 Report submitter 24

A.12 Manufacturer name 25

A.13 Original reporter occupation 25

A.14 Location where event occurred 26

A.15 Country where event occurred 26

D. Medical Device Information 27

D.1 Device Identifier (DI) 27

D.2 UDI Product Identifier (PI) 27

D.3 Medical device terminology used 28

D.4 Medical device nomenclature code 28

D.5 Medical device nomenclature description 29

D.6 Medical device name 29

D.7 Model 29

D.8 Combination product 30

D.9 Serial number(s) 30

D.10 Lot/batch number(s) 31

D.11 Software version 31

D.12 Firmware version 31

D.13 Device manufacturing date 32

D.14 Usage of the device 32

D.15 Device expiry date 33

D.16 Date when device was implanted 33

D.17 Date when device was explanted 34

I. Incident information 35

I.1 Incident narrative 35

I.2 Number of patients 35

P. Patient information 36

P.1 Patient age string 36

P.2 Patient sex 36

P.3 IMDRF Clinical Signs, Symptoms and Conditions terms/codes (Annex E) 37

P.4 IMDRF Health Impact terms/codes (Annex F) 37

M. Manufacturer analysis and action 39

M.1 Investigation narrative 39

M.2 IMDRF Type of Investigation terms/codes (Annex B) 39

M.3 IMDRF Investigation Finding terms/codes (Annex C) 40

M.4 IMDRF Investigation Conclusion terms/codes (Annex D) 41

M.5 IMDRF Medical Device Problem terms/codes (Annex A) 41

M.6 IMDRF Medical Device Component terms/codes (Annex G) 42

M.7 Remedial Action Taken 43

# File information

## File type

In order to share data efficiently and in a file format that is easily read and written, the IMDRF CDS currently uses spreadsheet format to communicate internally. 

## Naming convention

Every request should have a short title on the request form; the format of the filename should include this title. Filenames should be in the format YYYY-MM-DD_<3166-1 alpha-2 countrycode>_<short title>.xlsx, with the date being the date of the request (to distinguish between repeated requests with the same title), and the short title should be devoid of special characters that are not permitted in file names. 

e.g., if a request form is titled “Needle-stick injuries with Company_name needles” with a request date of October 2, 2024, a response file sent from Japan’s PMDA could be titled 2024-10-02_JP_ Needle-stick injuries with Company_name needles.xlsx

## Headers

The sample file lists the headers and has the appropriate data types selected; if setting up an excel file from a blank form the following are recommended. 

Cell A1 can have the simple title of the response file. Common Data Set for Adverse Event Data Exchange between IMDRF Regulators 

The headers for each column should reflect the names of the columns from the common data set, which are currently the following: the full field names are listed, but the spreadsheet uses names without spaces to ensure compatibility with databases and programming languages, as indicated

  1. Regulatory authority providing information
  2. Language of report
  3. Regulatory authority reference number
  4. Submitter reference number
  5. Initial date of receipt
  6. Latest date of receipt
  7. Date of incident
  8. Submitter awareness date
  9. Report version
  10. Classification of incident
  11. Report submitter
  12. Manufacturer name
  13. Original reporter occupation
  14. Location where event occurred
  15. Country where event occurred 
  16. Device Identifier (DI)
  17. UDI Product Identifier (PI)

| 

  1. Medical device terminology used 
  2. Medical device nomenclature code
  3. Medical device nomenclature description
  4. Medical device name
  5. Model
  6. Combination product
  7. Serial number(s)
  8. Lot/batch number(s)
  9. Software version
  10. Firmware version
  11. Device manufacturing date
  12. Usage of the device
  13. Device expiry date
  14. Date when device was implanted
  15. Date when device was explanted
  16. Incident narrative
  17. Number of patients
  18. Patient age string
  19. Patient sex

| 

  1. IMDRF Clinical Signs, Symptoms and Conditions terms/codes (Annex E)
  2. IMDRF Health Impact terms/codes (Annex F)
  3. Investigation narrative
  4. IMDRF Type of Investigation terms/codes (Annex B)
  5. IMDRF Investigation Finding terms/codes (Annex C)
  6. IMDRF Investigation Conclusion terms/codes (Annex D)
  7. IMDRF Medical Device Problem terms/codes (Annex A)
  8. IMDRF Medical Device Component terms/codes (Annex G)
  9. Remedial Action Taken

---|---|---  

The datatypes associated with each of these fields is documented with the descriptions of each field, below. The .xlsx format allows for up to 32,767 characters in any cell and 253 line breaks; if this is insufficient to hold the extracted data, the cell should have the fact that the data has been truncated should be noted. E.g., the cell could start with a tag like <truncated>

<truncated> Information was received from multiple sources…

# A. Administrative Information

These fields relate to the source of the report, identification numbers, dates associated with the report transmission/receipt, and other details that are about the report/reporting rather than the incident. 

## A.1 Regulatory authority providing information

User Guidance| ISO-3166-1 alpha-2 country code for the regulatory authority who received the AER from the submitter/sender and is thus sharing the report in the Common Data Set format.  
---|---  
Conformance| Required  
Data Type| String  
Value Allowed| ISO 3166-1 (alpha 2)  
Column| A  
Column name| senderOrganization  
Business Rule(s)| A two character country code will be used in all instances  

## A.2 Language of Report

User Guidance| ISO-639-1 language code for the language used in the AER by the regulatory authority. If multiple languages are present, select the language corresponding to the majority of the narrative or text provided.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| ISO-639-1  
Column| B  
Column name| language  
Business Rule(s)| A two character language code will be used in all instances  

## A.3 Regulatory authority reference number

User Guidance| Reference number assigned by regulatory authority who received the relevant AER from the submitter/sender  
---|---  
Conformance| Required  
Data Type| String  
Value Allowed| Free text  
Column| C  
Column name| ncaReportNo  
Business Rule(s)|   

## A.4 Submitter reference number

User Guidance| Submitter/sender's reference # which has been assigned by the submitter/sender.  
---|---  
Conformance| Required  
Data Type| String  
Value Allowed| Free text  
Column| D  
Column name| mfrInternalNo  
Business Rule(s)|   

## A.5 Initial date of receipt

User Guidance| Date when RA received the initial AER from the submitter/sender. This will not change with updates or new data.  
---|---  
Conformance| Required  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| E  
Column name| initialDateOfReceipt  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. There is no expectation to adjust date to UTC.  

## A.6 Latest date of receipt

User Guidance| Date when RA received the latest version of the AER from the submitter/sender. This will change for a given incident with the receipt of new data.  
---|---  
Conformance| Required  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| F  
Column name| latestDateOfReceipt  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. There is no expectation to adjust date to UTC.  

## A.7 Date of incident

User Guidance| Date when the reported incident happened.  
---|---  
Conformance| Optional  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| G  
Column name| adverseEventDate  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. If the date is specified as a date range in the system, use the start date of the date range as the date of incident. If the date is recorded as lower precision (e.g., just a year (YYYY), or as a year-month (YYYY-MM)), use the first day of that year or month (e.g., YYYY-01-01 or YYYY-MM-01). There is no expectation to adjust date to UTC.  

## A.8 Submitter awareness date

User Guidance| Date when the submitter/sender became aware of the incident.  
---|---  
Conformance| Optional  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| H  
Column name| mfrAwarenessDate  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. There is no expectation to adjust date to UTC.  

## A.9 Report version

User Guidance| Type of report submitted by the submitter/sender in terms of the situation or timing of the report.  
---|---  
Conformance| Required  
Data Type| Number  
Value Allowed| 1 = Initial2 = Update3 = Final4 = Not Reportable  
Column| I  
Column name| reportType  
Business Rule(s)| This should be the most appropriate selection based on the most recently received report. If additional information comes in after final, it will still map to final.Combined preliminary and final reports are considered final reports.   

## A.10 Classification of incident

User Guidance| Regulatory classification of the problem that happened to the patient (including operators) due to the event.  
---|---  
Conformance| Optional  
Data Type| Number  
Value Allowed| 1 = Public health threat2 = Death3 = Serious injury or deterioration in state of health4 = Potential injury or deterioration in state of health or malfunction9 = Other  
Column| J  
Column name| eventClassification  
Business Rule(s)|   

## A.11 Report submitter

User Guidance| Regulatory classification of the problem that happened to the patient (including operators) due to the event.  
---|---  
Conformance| Required  
Data Type| Number  
Value Allowed| 1 = Manufacturer2 = Importer/Distributor/Authorized Representative3 = Other Industry4 = Hospital/User Facility*5 = Public/Independent Health Care Professional*6 = Other Non-Industry*  
Column| K  
Column name| reportSubmitter  
Business Rule(s)| A two character country code will be used in all instances  

## A.12 Manufacturer name

User Guidance| The name of the manufacturer for the device involved in this adverse incident.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| L  
Column name| mfrName  
Business Rule(s)|   

## A.13 Original reporter occupation

User Guidance| Type of organization or entity who initially inform the submitter/sender to the regulatory authority under the regulation of their jurisdiction.  
---|---  
Conformance| Optional  
Data Type| Number  
Value Allowed| 1 = Healthcare professional2 = Patient/Consumer/Lay User3 = Other non-healthcare professional  
Column| M  
Column name| originalReporterRole  
Business Rule(s)|   

## A.14 Location where event occurred

User Guidance| Regulatory classification of the problem that happened to the patient (including operators) due to the event.  
---|---  
Conformance| Optional  
Data Type| Number  
Value Allowed| 1 = Hospital2 = Other healthcare facility/transport3 = Home4 = Other non-healthcare facility  
Column| N  
Column name| locationOfEvent  
Business Rule(s)|   

## A.15 Country where event occurred

User Guidance| ISO-3166-1 alpha-2 country code for the country where the reported event occurred.  
---|---  
Conformance| Required  
Data Type| String  
Value Allowed| ISO-639-1  
Column| O  
Column name| eventCountry  
Business Rule(s)| A two character country code will be used in all instances  

# D. Medical Device Information

These fields relate to the device involved in the report. These can be very specific fields (e.g., lot numbers) or very high level (e.g., a nomenclature term covering many devices).

## D.1 Device Identifier (DI)

User Guidance| A unique numeric or alphanumeric value specific to a model or version of a medical device.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| P  
Column name| udiDI  
Business Rule(s)| Validation (if implemented) would be per standard; see UDI standards online.   
GS1 is 16 numeric (14N without delimiter)HIBCC is 7-24 AN (6-23AN without delimiter)ICCBBA is 18AN (16AN without the delimiter) (12AN for blood bags only, 10AN without delimiter)  

## D.2 UDI Product Identifier (PI)

User Guidance| A numeric or alphanumeric code that identifies the unit of device production. The different types of Product Identifier(s) include serial number, lot/batch number, manufacturing date, and/or expiration date.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| Q  
Column name| udiPI  
Business Rule(s)| Validation (if implemented) would be per standard; see UDI standards online.  

## D.3 Medical device terminology used

User Guidance| Nomenclature of the medical device, which is used to identify the device type for regulatory purposes in each jurisdiction (i.e. GMDN).  
---|---  
Conformance| Optional  
Data Type| Number  
Value Allowed| 1 = GMDN2 = EMDN3 = UMDNS (ECRI)4 = GIVD / EDMS5 = MFDS6 = JMDN 7 = USFDA8 = PNC9 = Other  
Column| R  
Column name| nomenclatureSystem  
Business Rule(s)|   

## D.4 Medical device nomenclature code

User Guidance| Code for nomenclature.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| S  
Column name| nomenclatureCode  
Business Rule(s)|   

## D.5 Medical device nomenclature description

User Guidance| Description for nomenclature.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| T  
Column name| nomenclatureTerm  
Business Rule(s)|   

## D.6 Medical device name

User Guidance| A name used to assist in the identification of the regulated medical device (i.e. Brand Name, Trade Name, Proprietary Name).  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| U  
Column name| brandName  
Business Rule(s)|   

## D.7 Model

User Guidance| Represents one medical device or family of medical device to group many variations that have shared characteristics.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| V  
Column name| modelNum  
Business Rule(s)|   

## D.8 Combination product

User Guidance| Indicates whether the device is a combination product according to the regulatory authority. Simple (Yes/No) selection.  
---|---  
Conformance| Optional  
Data Type| Number  
Value Allowed| 1 = Yes2 = No  
Column| W  
Column name| combinationProduct  
Business Rule(s)|   

## D.9 Serial number(s) 

User Guidance| A unique sequence of numbers or letter in a series used to identify an individual unit of a medical device.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| X  
Column name| serialNum  
Business Rule(s)|   

## D.10 Lot/batch number(s) 

User Guidance| A value that represents one or more components or finished devices that consist of a single type, model, class, size, composition, or software version that are manufactured under essentially the same conditions and are intended to have uniform characteristics and quality within specified limits  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| Y  
Column name| batchNum  
Business Rule(s)|   

## D.11 Software version 

User Guidance| The value given by the applicant to identify a specific revision of the software for SaMD.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| Z  
Column name| deviceSoftwareVer  
Business Rule(s)|   

## D.12 Firmware version

User Guidance| The value given by the applicant to identify a specific revision of the firmware of medical device.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AA  
Column name| deviceFirmwareVer  
Business Rule(s)|   

## D.13 Device manufacturing date

User Guidance| A date determined by the regulated entity in which the medical device is considered to have been manufactured.  
---|---  
Conformance| Optional  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| AB  
Column name| deviceMfrDate  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. If the date is recorded as lower precision or the day or month is unknown (e.g., just a year (YYYY), or as a year-month (YYYY-MM)), use the first day of that year or month (e.g., YYYY-01-01 or YYYY-MM-01). There is no expectation to adjust date to UTC.  

## D.14 Usage of the device

User Guidance| Indicates the use and reuse of the medical device with respect to reprocessing.  
---|---  
Conformance| Optional  
Data Type| Number  
Value Allowed| 1 = Initial use of device2 = Reuse of a reusable medical device3 = Reuse of a single use medical device4 = Other  
Column| AC  
Column name| deviceUsage  
Business Rule(s)|   

## D.15 Device expiry date

User Guidance| A date based on the results of studies which demonstrate that the medical device will perform as intended and will meet its specifications until that date.  
---|---  
Conformance| Optional  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| AD  
Column name| deviceExpiryDate  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. If the date is recorded as lower precision or the day or month is unknown (e.g., just a year (YYYY), or as a year-month (YYYY-MM)), use the first day of that year or month (e.g., YYYY-01-01 or YYYY-MM-01). There is no expectation to adjust date to UTC.  

## D.16 Date when device was implanted

User Guidance| Date when the implantable device has been implanted.  
---|---  
Conformance| Optional  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| AE  
Column name| ImplantedDate  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. If the date is recorded as lower precision or the day or month is unknown (e.g., just a year (YYYY), or as a year-month (YYYY-MM)), use the first day of that year or month (e.g., YYYY-01-01 or YYYY-MM-01). There is no expectation to adjust date to UTC.  

## D.17 Date when device was explanted

User Guidance| Date when the implantable device has been explanted.  
---|---  
Conformance| Optional  
Data Type| Date  
Value Allowed| YYYY-MM-DD (ISO 8601)  
Column| AF  
Column name| ExplantedDate  
Business Rule(s)| If dates are stored as date and time the field should be truncated to the date. If the date is recorded as lower precision or the day or month is unknown (e.g., just a year (YYYY), or as a year-month (YYYY-MM)), use the first day of that year or month (e.g., YYYY-01-01 or YYYY-MM-01). There is no expectation to adjust date to UTC.  

# I. Incident information

These fields relate to the incident itself.

## I.1 Incident narrative

User Guidance| Provide a comprehensive description of the incident, including (1) what went wrong with the device (if applicable) and (2) a description of the health effects (if applicable), i.e. clinical signs, symptoms, conditions as well as the overall health impact.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AG  
Column name| eventDescription  
Business Rule(s)|   

## I.2 Number of patients

User Guidance| Number of patients involved in this reported incident. Patient could also mean user or other third person and the initial reporter may be a family member or other third person.  
---|---  
Conformance| Optional  
Data Type| number  
Value Allowed| Numeric  
Column| AH  
Column name| numPatientsInvolved  
Business Rule(s)| Should be a non-negative value.  

# P. Patient information

These fields relate to the patient (Age, Sex) and the consequences to the patient. The narrative portion of this is instead captured in the I.1 Incident narrative field in the Incident information section, but the IMDRF AE terminology codes for Annexes E and F are captured here. 

## P.1 Patient age string

User Guidance| Patient age in string format.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AI  
Column name| patientAgeString  
Business Rule(s)|   

## P.2 Patient sex

User Guidance| Patient sex assigned at birth.  
---|---  
Conformance| Optional  
Data Type| Number  
Value Allowed| 1 = Female2 = Male3 = Other4 = Unknown  
Column| AJ  
Column name| patientSex  
Business Rule(s)|   

## P.3 IMDRF Clinical Signs, Symptoms and Conditions terms/codes (Annex E)

User Guidance| Clinical Signs, Symptoms and Conditions terms/codes (Annex E): Annex E provides terminology to describe the observed condition of the affected persons associated with the medical device adverse event.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AK  
Column name| imdrfClinicalCodes  
Business Rule(s)| IMDRF Annex E codes consist of the upper case letter E followed by 4 or 6 digits.These should be separated by commas (a space following a comma is optional).e.g., E0101, E040501, E1609 or E0101,E040501,E1609 would both be acceptable, and represents 3 Annex E codesIf there is an identified “most relevant” code (per the MIR form), this should be the first code listed and the string should begin with an exclamation point.e.g., !E0101, E040501, E1609 would represent 3 codes with the most relevant code being !E0101  

## P.4 IMDRF Health Impact terms/codes (Annex F)

User Guidance| Health Impact terms/codes (Annex F): Annex F provides terminology to describe the resulting consequences of the medical device adverse event/incident on the person affected.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AL  
Column name| imdrfHealthImpactCodes  
Business Rule(s)| IMDRF Annex F codes consist of the upper case letter F followed by 2 or 4 digits.These should be separated by commas (a space following a comma is optional).e.g., F12,F2302,F2203 or F12, F2302, F2203would both be acceptable, and represents 3 Annex F codesIf there is an identified “most relevant” code (per the MIR form), this should be the first code listed and the string should begin with an exclamation point.e.g., !F12, F2302, F2203 would represent 3 codes with the most relevant code being !F12  

# M. Manufacturer analysis and action

These fields relate to the investigation undertaken by the manufacturer, as well as the results and conclusion of this investigation, and the actions taken in response to it. 

## M.1 Investigation narrative

User Guidance| Description of the manufacturer’s evaluation concerning possible root causes/causative factors and conclusion.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AM  
Column name| investigationNarrative  
Business Rule(s)|   

## M.2 IMDRF Type of Investigation terms/codes (Annex B)

User Guidance| Description of the manufacturer’s evaluation concerning possible root causes/causative factors and conclusion.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AN  
Column name| imdrfInvestigationTypeCodes  
Business Rule(s)| IMDRF Annex B codes consist of the upper case letter B followed by 2 digits.These should be separated by commas (a space following a comma is optional).e.g., B01, B13, B14 or B01,B13,B14would both be acceptable, and represents 3 Annex B codesIf there is an identified “most relevant” code (per the MIR form), this should be the first code listed and the string should begin with an exclamation point.e.g., !B01, B13, B14 would represent 3 codes with the most relevant code being !B01  

## M.3 IMDRF Investigation Finding terms/codes (Annex C)

User Guidance| Description of the manufacturer’s evaluation concerning possible root causes/causative factors and conclusion.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AO  
Column name| imdrfInvestigationFindingsCodes  
Business Rule(s)| IMDRF Annex C codes consist of the upper case letter C followed by 2 or 4 digits.These should be separated by commas (a space following a comma is optional).e.g., C0101, C0204, C03 or C0101,C0204,C03 would both be acceptable, and represents 3 Annex C codesIf there is an identified “most relevant” code (per the MIR form), this should be the first code listed and the string should begin with an exclamation point.e.g., !C0101, C0204, C03 would represent 3 codes with the most relevant code being !C0101  

## M.4 IMDRF Investigation Conclusion terms/codes (Annex D)

User Guidance| Description of the manufacturer’s evaluation concerning possible root causes/causative factors and conclusion.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AP  
Column name| imdrfInvestigationConclusionCodes  
Business Rule(s)| IMDRF Annex D codes consist of the upper case letter D followed by 2 or 4 digits.These should be separated by commas (a space following a comma is optional).e.g., D01, D02, D1103D01,D02,D1103would both be acceptable, and represents 3 Annex D codesIf there is an identified “most relevant” code (per the MIR form), this should be the first code listed and the string should begin with an exclamation point.e.g., !D01, D02, D1103 would represent 3 codes with the most relevant code being !D01  

## M.5 IMDRF Medical Device Problem terms/codes (Annex A)

User Guidance| Description of the manufacturer’s evaluation concerning possible root causes/causative factors and conclusion.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AQ  
Column name| imdrfDeviceProblemCodes  
Business Rule(s)| IMDRF Annex A codes consist of the upper case letter A followed by 2, 4 or 6 digits.These should be separated by commas (a space following a comma is optional).e.g., A01, A040501, A1801 or A01,A040501,A1801 would both be acceptable, and represents 3 Annex A codesIf there is an identified “most relevant” code (per the MIR form), this should be the first code listed and the string should begin with an exclamation point.e.g., !A01, A040501, A1801 would represent 3 codes with the most relevant code being !A01  

## M.6 IMDRF Medical Device Component terms/codes (Annex G)

User Guidance| Description of the manufacturer’s evaluation concerning possible root causes/causative factors and conclusion.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AR  
Column name| imdrfComponentCodes  
Business Rule(s)| IMDRF Annex G codes consist of the upper case letter G followed by 5 or 7 digits.These should be separated by commas (a space following a comma is optional).e.g., G0408201, G02026, G02002 or G0408201,G02026,G02002would both be acceptable, and represents 3 Annex G codesIf there is an identified “most relevant” code (per the MIR form), this should be the first code listed and the string should begin with an exclamation point.e.g., !G0408201, G02026, G02002 would represent 3 codes with the most relevant code being !G0408201  

## M.7 Remedial Action Taken

User Guidance| Description of the manufacturer’s evaluation concerning possible root causes/causative factors and conclusion.  
---|---  
Conformance| Optional  
Data Type| String  
Value Allowed| Free text  
Column| AS  
Column name| correctiveAction  
Business Rule(s)|   

# Appendix B – Sample Data Template

Excel Spreadsheet providing sample data template. 

# Appendix C – CDS Request Form

CDS Request Form – **Request**  
---  
**Title of the Request**  
Title of the Request (for file naming)|   
**Request Details**  
Date Request:| YYYY-MM-DD  
Date Required:| YYYY-MM-DD  
Requesting Organisation:| | Requester Name:|   
Requester Email:|   
**Specific Detail of the Request**  
Click or tap here to enter text. Guidance on how the data should be searched using the IMDRF codes should be provided in this section. Outlining the priority or most important codes of interest, or in which sequence should the codes be searched e.g. the search should be conducted using Annex A codes first then Annex E and then Annex G, a listing of all cases with Annex A codes should be provided with those case that include Annex A and Annex E and/or G highlighted.   
Relevant documents or links to relevant documents can be provided.   
**Scope of the Request**  
Type of Request: | Report to assist with an ongoing investigation. |   
Report to assist in validating a potential trend or signal. |   
| Other: |   
Focus of Request | Device Issue |   
Patient Problems |   
Manufacturer Analysis |   
**Specific Search Criteria**  
Date Period| Start Date: Finish Date:   
Specific Device Details * | Device characteristics| Values for characteristics  
Medical Device Name (Brand/Trade/ Proprietary)|   
Medical Device Model/Catalogue Reference number / product code|   
Version (Software / Firmware)|   
Medical Device UDI (UDI-DI/UDI-PI)|   
Medical Device lot/batch number|   
Nomenclature|   
Manufacturer Details | Manufacturer name:   
**IMDRF Codes of Interest**  
Medical Device Problem (Annex A)|   
Cause Investigation – Type of Investigation (Annex B)|   
Cause Investigation – Investigation Findings (Annex C)|   
Cause Investigation – Investigation Conclusion (Annex D)|   
Health Effects – Clinical Signs and Symptoms or Conditions (Annex E)|   
Health Effects – Health Impact (Annex F)|   
Medical Device Component (Annex G) |   
*If you wish to compare the data requested with a second device and /or manufacturer please submit a separate request form.   
CDS Request Form – **Response**  
**Responder Details**  
Responder Organisation:| | Responder Name:| |   
Responder Email:|   
**Specific details of how the data was generated**  
**Additional Comments**  
Other relevant details regarding the request


<!-- fulltext-end -->
