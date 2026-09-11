# Global Unique Device Identification Database (GUDID): Guidance for Industry and Food and Drug Administration Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/global-unique-device-identification-database-gudid](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/global-unique-device-identification-database-gudid)

**Published:** 2024-12-17


---

Global Unique Device Identification Database (GUDID)
Guidance for Industry and Food and Drug Administration Staff

This guidance represents the current thinking of the Food and Drug Administration (FDA or Agency) on this topic. It does not establish any rights for any person and is not binding on
FDA or the public. You can use an alternative approach if it satisfies the requirements of the applicable statutes and regulations. To discuss an alternative approach, contact the FDA staff or Office responsible for this guidance as listed on the title page.
## I. Introduction
The Food and Drug Administration (FDA) is responsible for protecting the public health by assuring the safety, effectiveness, and security of human and veterinary drugs, vaccines and other biological products, medical devices, the nation’s food supply, cosmetics, dietary supplements, and products that give off radiation; and for regulating tobacco products.
Section 226 of the FDA Amendments Act (FDAAA) of 2007 and section 614 of the FDA Safety and Innovation Act (FDASIA) of 2012 amended the Federal Food, Drug, and Cosmetic Act to add section 519(f), which directs the FDA to promulgate regulations establishing a unique device identification system for medical devices along with implementation timeframes for certain medical devices. The Unique Device Identifier (UDI) Proposed Rule was published on July 10, 2012, followed by an amendment, published on November 19, 2012, modifying the implementation time frame for certain devices. In developing the proposed rule, we solicited input from a variety of stakeholders (e.g., manufacturers, global regulatory bodies, the clinical community, patient advocates) to ensure that as many perspectives were incorporated as possible. The UDI Final Rule was published on September 24, 2013 (78 FR 58786).
This document is primarily intended for device labelers1 and provides information necessary for submitting data to the Global Unique Device Identification Database (GUDID).
1 The UDI Final Rule (http://www.fda.gov/udi) defines labeler as “any person who causes a label to be applied to a device with the intent that the device will be commercially distributed without any intended subsequent replacement or modification of the label; and, any person who causes the label of a device to be replaced or modified with the intent that the device will be commercially distributed without any subsequent replacement or modification of the label, except that the addition of the name of, and contact information for, a person who distributes the device, without making any other changes to the label, is not a modification for the purposes of determining whether a person is a labeler.”
This guidance update reflects upcoming changes to the Global Medical Device Nomenclature (GMDN) field in GUDID and other minor clarifications. Since April 2019 the GMDN Agency allows access to GMDN Terms without a paid membership. Therefore, the option to use FDA
Preferred Term (PT) Codes is no longer necessary and FDA intends to remove them from GUDID. Reference to the FDA PT codes is being removed from this guidance and GUDID users must use GMDN codes (21 CFR 830.310(b)(13)). Database enhancements to improve user experience, build in better validation rules, and other changes may continue as we receive feedback. We intend to periodically update this document to reflect system changes and enhancements.
In general, FDA’s guidance documents do not establish legally enforceable responsibilities.
Instead, guidances describe the Agency’s current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited. The use of the word should in Agency guidances means that something is suggested or recommended, but not required.
## II. Unique Device Identifier (UDI)
The “unique device identifier” (UDI) should be created and maintained by device labelers based on global device identification standards managed by FDA-accredited Issuing Agencies2. As of the publication date of this document, we have accredited three issuing agencies – GS1, HIBCC and ICCBBA. The ‘UDI Formats by FDA Accredited Issuing Agency’3 document, provides the standard UDI formats for the three issuing agencies.
A UDI is required to appear on the label of every medical device, and every device package, unless excepted (see 21 CFR 801.20). This includes combination products that contain a device constituent part; convenience kits; in vitro diagnostic products; human cells, tissues, and cellular and tissue-based products (HCT/Ps) regulated as devices; and stand-alone software4. The UDI is composed of two parts: - Device Identifier (DI) - a mandatory, fixed portion of a UDI that identifies the labeler and the specific version or model of a device; and - Production Identifier(s) (PI) - a conditional, variable portion of a UDI that identifies one or more of the following when included on the label of a device, unless excepted: o the lot or batch number within which a device was manufactured; o the serial number of a specific device; o the expiration date of a specific device; o the date a specific device was manufactured; o and, for an HCT/P regulated as a device, the distinct identification code required by 21 CFR 1271.290(c)5.
2 Refer to the UDI Final Rule (http://www.fda.gov/udi ) for details on issuing agencies and their role in UDI assignment.
4 Stand-alone software version number may be represented as Lot or Batch number production identifier.
Therefore, UDI = DI + PI.
The DI will serve as the primary key and can be used to look up information about the device in the GUDID.
Any identifiers beyond those specified in this document are outside the scope of the FDA regulated UDI.
Note that the UDI of a class I device is not required to include a PI (21 CFR 801.30(d)). Further, a class I device that bears a Universal Product Code (UPC) on its label and device packages is deemed to have met the UDI labeling requirements (21 CFR 801.40(d)). Finally, Class I devices that FDA has by regulation exempted from the good manufacturing practice requirements (other than recordkeeping requirements) do not need a UDI (21 CFR 801.30(a)(2)).
Labelers are required to enter the DI along with additional device attribute information to the GUDID, as specified in the final rule, prior to introducing a device into commercial distribution, unless subject to an exception or alternative. While we expect GUDID DI submissions to occur as soon as practicable, for device versions or models initially entering commercial distribution, the DI records for such devices should be in the published state no later than fifteen calendar days from the initial date that version or model is introduced into commercial distribution. The GUDID is a device identification repository and labelers should enter complete and accurate information into GUDID. Specifically, device identification data entered into GUDID should match the information submitted in a premarket submission (e.g., device description, device attributes). Additionally, the data entered should match and align with all submissions to FDA with regards to device identification throughout the total product life cycle of the device. This means, device identification data submitted, for example, during registration and listing, adverse event reporting, or recalls should align and match the information in GUDID.
## III. Global Unique Device Identification Database (GUDID)
As stated above, the GUDID serves as the repository of key device identification information.
The GUDID contains ONLY the DI, which serves as the primary key to obtain device information in the database. PIs are not submitted to or stored in the GUDID; the GUDID contains only production identifier flags to indicate which PI attribute(s) are on the device label, unless excepted.
The GUDID includes all of the data elements required by 21 CFR 830.310. The GUDID also includes certain ancillary administrative data used to develop and maintain the GUDID and to facilitate integration of DI information with internal FDA systems. A complete list of GUDID data elements and descriptions are provided in the ‘GUDID Data Element Reference Table’6. For those data attributes in the GUDID that appear in medical device labeling, the attribute values submitted to GUDID should be consistent with their representation in the labeling. See example in Appendix D, which maps some GUDID attributes to a fictitious device label.
HCT/P. The distinct identification code may take the form of a donation identification number, serial number, lot number, or a combination of these production identifiers. In the GUDID, labelers of HCT/Ps regulated as medical devices should select the appropriate type of production identifier that appears on the label of the device.
The design principles guiding GUDID development includes the following: · Standards-based submission with two options: §
Structured input via the GUDID Web Interface – needs manual data entry and is geared for low volume submitters.
§
Health Level 7 (HL7)7 Structured Product Labeling (SPL)8 submission via the
FDA Electronic Submissions Gateway (ESG)9 – allows for submission via xml files and is geared for high volume submitters.
- Standards-based data repository with controlled vocabularies including: o Dun & Bradstreet (D&B) Number (DUNS)10 o Global Medical Device Nomenclature (GMDN)11 o FDA Product Codes - Free and public access to the device information in GUDID via public search, including download capability.
### A. GUDID Key Concepts
The next few sections present an overview of GUDID key concepts such as GUDID account and user roles, the device identifier record, and the device identifier record life-cycle. Note that these concepts apply to both GUDID submission options – Web Interface and HL7 SPL xml file submission.
(1)
GUDID Account
Labelers should first request a GUDID account. This section presents an overview of the GUDID account, the user roles, preparatory steps to obtain a GUDID account, how to request a GUDID account and how to manage account changes. The structure of the GUDID Account and the different user roles are depicted in Figure 1.
7 HL7 is a standards development organization, whose mission is to provide messaging standards for interoperability, exchange, management, and integration of data that supports clinical patient care and the management, delivery, and evaluation of healthcare services. Visit http://www.hl7.org for more information.
8 Structured Product Labeling (SPL) is a HL7 standard for the exchange of product information using extensible markup language (XML).
9 FDA ESG enables the secure submission of regulatory information. For more information, please visit: http://www.fda.gov/esg.
10 Data Universal Numbering System or D-U-N-S® Number is a unique nine-digit identification number assigned and managed by Dun & Bradstreet to business entities. For more information, visit Business Entity Identifiers | FDA.
11 Global Medical Device Nomenclature (GMDN) is system of internationally agreed descriptors used to identify medical device products and is managed by the GMDN Agency. Visit: http://www.gmdnagency.com.
Figure 1: GUDID Account and User Roles
A Labeler Organization may have one or more GUDID accounts.
- GUDID utilizes DUNS numbers to enable identification of labeler organizations using a uniform standard and process. The DUNS number is an important component of the FDA
Unique Facility Identifier System, along with a Geocode, which specifies the exact location of the facility (GUDID does not collect Geocodes).
- Labelers should manage their company information via the DUNS number and GUDID pulls company name and address from the D&B DUNS database.
- Each GUDID account is identified by the Organization DUNS Number.
o
This DUNS number represents the labeler’s view of the highest corporate level in the labeler organization; it may be the headquarters DUNS number or the parent DUNS number for the labelers included in the GUDID account.
o
Please ensure that the name and address in the D&B DUNS database is accurate, as this number is used to identify the labeler organization in GUDID.
o
The organization DUNS number serves as the primary key for the GUDID account.
Once used, it cannot be reused to create another GUDID account.
o
The organization DUNS number can be used as a Labeler DUNS number (see below).
- Each account should have only one Regulatory Contact.
o A Regulatory Contact:12
§
Is the individual who serves as the point of contact to us on matters relating to the identification of medical devices marketed by the labeler; he/she is responsible for ensuring the labeler organization meets GUDID submission requirements (see 21 CFR 830.320(a)).
§
Is the highest point of contact for the labeler organization, i.e., we may first contact the GUDID Coordinator for issues related to the data submitted to GUDID, and if the issue is not resolved, bring it to the attention of the Regulatory Contact.
§
Does not have functional user role in GUDID i.e., no username or password to access GUDID.
§
Can also serve as GUDID Coordinator and Labeler Data Entry user, if so desired (see below); both of these user roles would have a separate username and password to access GUDID.
o You may choose to use a third-party to serve as the Regulatory Contact for GUDID as described in 21 CFR 830.320(a); you should inform us of your intent to do so during the GUDID account request process via a letter on your company letterhead, signed by a responsible official from your organization.
- Each GUDID account should have one or more labelers, identified by Labeler DUNS numbers.
o Device information would be submitted for the labelers identified in the GUDID account.
o Each device record should be associated to a Labeler DUNS number and is used to pull the labeler company name and address from the D&B DUNS database.
To ensure data consistency, the company name associated to the Labeler DUNS number should match the company name that appears on the device label. Ideally the address associated with the DUNS number should also match the address on the device label, but since address is not displayed to the GUDID public user, this is not a requirement; however, labelers are encouraged to work towards this model for new products and when making changes to existing products as appropriate.
o Organization DUNS number can be used as Labeler DUNS number.
o Labeler DUNS number, once used, cannot be reused in any other GUDID account.
- Each GUDID account should have one or more Coordinators.12
o Each Coordinator would be assigned one or more Labeler DUNS numbers, in a given GUDID account.
o Coordinators manage the GUDID account for their designated Labeler DUNS numbers. Responsibilities should include: §
Create Labeler Data Entry (LDE) user account(s) (see below).
§
Assign Labeler DUNS number(s) to LDE(s).
§
Create LDE user role for a third-party (see below), if so desired.
§
Serve as Regulatory Contact, if so desired.
§
Serve as LDE user, if so desired; separate username and password is provided for 12 GUDID Account user contact information provided is for FDA internal use only; not available via GUDID public search and retrieval.
the LDE user role.
§
Serve as the first point of contact and respond to FDA inquiries related to GUDID data quality, incorrect or inconsistent data, and other submission/data specific questions.
o
A given Labeler DUNS Number can be assigned to more than one Coordinator (see
Figure 1, Labeler DUNS Number 3 is assigned Coordinator 1 and Coordinator 2).
The Coordinators would then share responsibility for DI records associated to that Labeler DUNS number.
- Each GUDID account should have one or more LDE users13.
o
Each LDE user is assigned one or more labelers, identified by Labeler DUNS numbers, in a given GUDID account.
o An LDE user: §
Is responsible for data entry, submission, and management of device identification information for their designated Labeler DUNS into the GUDID.
§
Can serve as Regulatory Contact, if so desired.
§
Can serve as Coordinator user, if so desired; separate username and password is provided for the Coordinator user role.
o
A given Labeler DUNS Number can be assigned to more than one LDE user. The LDE users would then share responsibility for DI records associated to that Labeler DUNS number.
The labeler has the option to designate third-party submitters for GUDID submissions. A third-party submitter is a company/individual (e.g., contractor, vendor) authorized to submit GUDID information on behalf of the labeler. The third-party may submit data on behalf of the labeler, but the labeler is ultimately held responsible for the information submitted to GUDID.
- Each GUDID account may have zero or more third-party submitters.
- Web Interface submission option – a third-party may use the GUDID Web Interface to enter data for the labeler. You, the labeler, may choose to request the Coordinator user role for the third-party (request sent to FDA, see section III.A.(1).b); you may provide the third-party with LDE user access.
- HL7 SPL submission option – the third-party may: o
Provide software solution/tool to generate the HL7 SPL xml file; you, the labeler, would then submit the file via the FDA ESG. or, o
Provide end-to-end solution to the labeler, i.e., generate the HL7 SPL xml file, and submit it via the FDA ESG for the labeler. In order to enable a third party to submit to GUDID via the ESG, the following should be noted: § You, the labeler, should identify the third-party by providing the third-party DUNS number during your GUDID account request. The third party is associated to your labeler account. By identifying the third-party, you are authorizing the third-party to submit GUDID information on your behalf.
§
GUDID HL7 SPL submissions sent via the ESG by a third-party not associated to a GUDID account are rejected.
13 GUDID Account user contact information provided is for FDA internal use only; not available via GUDID public search and retrieval.
Note that the GUDID Regulatory Contact, Coordinator and LDE user contact information provided by labeler organizations is used for internal FDA purposes only and is not available via GUDID public search and retrieval.
Submission of device information to GUDID necessitates establishment of a GUDID account, regardless of the submission option chosen –via Web Interface or via FDA ESG as HL7 SPL xml files. Please note that the GUDID account is not by submission type, i.e., a separate GUDID account is not needed for each submission option. The account identifies the labeler in GUDID and enables submission of device information via both options. See section III.A.(1).b for detailed description of the account establishment process.
A GUDID account is not needed for search and retrieval of GUDID information.
a) Preparatory Steps Prior to Requesting a GUDID Account
Prior to requesting a GUDID account, labeler organizations are encouraged to ensure the following: - Familiarize yourself with the two submission options available – GUDID Web Interface and HL7 SPL xml file submission.
- Identify the DUNS Numbers to be used for your GUDID account.
o
If your company does not have a DUNS number, you can obtain one free of charge from D&B. Please note that this may take up to 30 business days; please plan accordingly.
o
Expedited options to obtain a DUNS number are available for a nominal fee.
o
Please visit Business Entity Identifiers | FDA for more information.
- Ensure the company name and address associated to the DUNS number is correct; if any changes are necessary, please update your information in the D&B DUNS database before requesting a GUDID account.
- Identify individuals for the various user roles in GUDID -- Regulatory Contact, Coordinator(s) and LDE user(s).
o
Note that one individual can take on multiple GUDID user roles.
o
If you plan to use a third-party to serve as the Regulatory Contact for GUDID as described in 21 CFR 830.320(a), please inform us of your intent to do so during the GUDID account request process via a letter on your company letterhead, signed by a responsible official from your organization.
- Identify an individual to request the GUDID account and manage all account changes.
- Identify third-party submitters, if applicable.
o
Obtain third-party DUNS number after ensuring that they have verified their information in the DUNS database as accurate.
b) GUDID Account Request Process
Once the necessary information is gathered, a GUDID account request may be submitted to us.
Visit http://www.fda.gov/udi for information on how to submit the request.
The following information should be provided when requesting a GUDID Account: - Labeler Organization DUNS Number – this DUNS number represents the labeler’s view of the highest corporate level in the labeler organization; it may be the headquarters DUNS number, or the parent DUNS number for the labelers included in the GUDID account.
- Labeler Organization Name – this is used for verification purposes only; GUDID obtains company name and address from the D&B DUNS database.
- Regulatory Contact information – name, email, phone, physical address.
- Labeler DUNS for the GUDID Account – as indicated earlier in Section III.A.(1), the company name associated to the Labeler DUNS number should match the labeler name as it appears on the device label; ideally, the company address associated to the DUNS number should also match the address on the label, but since address is not displayed to the GUDID public user, this is not a requirement for data consistency.
- Coordinator Information: o Contact information – name, email, phone o
List of Labeler DUNS that is the responsibility of the Coordinator; if there are multiple Coordinators, please specify the DUNS that each Coordinator is responsible for in GUDID.
- Third-party DUNS numbers, if applicable - Indicate the preferred submission option – Web Interface or HL7 SPL or both o HL7 SPL submitters should first complete testing as specified in the HL7 SPL
Implementation specification, prior to submitting to production GUDID. Therefore, HL7 SPL submitters are first provided with a test GUDID account. See FDA webpage Submit Data to GUDID, for additional information on submission options.
Note that the GUDID Regulatory Contact, Coordinator and LDE user contact information that you provide is used for internal FDA purposes only and is not available via GUDID public search and retrieval.
Once we receive the GUDID account request, the information is reviewed. We may contact the individual requesting the account with any questions such as discrepancies with labeler company name and address associated to DUNS numbers, third party information, or other information needed to create a GUDID account. Once all issues are resolved, we create the GUDID account using the GUDID Web Interface; the Coordinator receives login information and a temporary password via a system generated email.
Each GUDID account will have, at a minimum: ·
one Regulatory Contact ·
one Labeler DUNS number ·
one Coordinator – for submitters who are using the HL7 SPL submission option, the Coordinator user is optional.
Once a GUDID account is created: - The Web Interface submitter may login and begin using GUDID.14
o Coordinator may access the system via their temporary login and password to create LDE users.
o
Coordinator should have the following information to create an LDE user account: 14 For detailed information on logging in and using GUDID for each user role refer to the Global Unique Device Identification Database (GUDID) User Manual.
§
LDE user information: name, email, phone §
List of Labeler DUNS to be assigned to the LDE user o
Once accounts are created, the LDE user receives a temporary login and password via system generated email.
- HL7 SPL ONLY submitters, please refer to section III.B.(2) for additional details.
c) GUDID Account Changes
To make changes to an existing GUDID account, please contact the FDA UDI Help Desk. We recommend that you identify an individual in your organization to manage GUDID account changes.
Account changes may include: - Update Regulatory Contact information - Add/update Coordinator information - Change assignment of Labeler DUNS to Coordinators - Add Labeler DUNS - Add/update third-party submitter information - Account changes related to mergers/acquisitions that may impact DI records – current version of GUDID has not implemented capability to handle all use-cases surrounding mergers/acquisitions. We are actively working to identify business rules for future system implementation. We request that you please contact us if you anticipate a merger/ acquisition that may impact your DI records, so we can work proactively to address your situation.
(2)
Device Identifier (DI) Record
Recall from Section II, that a UDI = Device Identifier (DI) + Production Identifier (PI).
The DI, together with associated data attributes,15 constitutes a DI Record in the GUDID, and contains identifying information for a particular device version or model. Please note that information presented in this section applies to both GUDID submission options – Web Interface and HL7 SPL xml file submission.
The following are key characteristics of a DI Record in GUDID: · GUDID will only contain the DI; the PI is never part of the GUDID. However, the GUDID will contain production identifier flags, to indicate which PI attribute(s) (lot or batch number, serial number, expiration date, manufacturing date and donation identification number) appear on the label of the device, unless excepted.
- Primary DI: Each DI record will have a Primary DI, which is the primary key for the record.
This is the DI of the lowest level of a medical device package containing a full UDI. The lowest packaging level is also the base package.
o
Under 21 CFR 830.40(a), a version or model of a device may be identified using only one DI from a given FDA accredited issuing agency. The same version or model may be identified by UDIs from other FDA accredited issuing agencies; labelers must identify the DI from one issuing agency as the Primary DI in GUDID and the DIs from other issuing agencies may be listed as Secondary DIs (21 CFR 830.40(a)) (see
The DI record may also contain additional device identifiers: o
Secondary DI: An identifier that is an alternate (secondary) lookup for a medical device that is issued from a different FDA accredited issuing agency than the Primary
DI. o
Unit of Use DI: A virtual identifier assigned to an individual medical device when a UDI is not labeled on the individual device at the level of its unit of use. Its purpose is to associate the use of a device to/on a patient when a base package contains more than one device. The package configuration example in Appendix A, Figure 1, includes a Unit of Use DI.
o
Direct Marking DI16: An identifier that is permanently marked directly on the medical device; can be the same as or different from the Primary DI; only applicable to devices subject to Direct Marking requirements under 21 CFR 801.45.
o
Package DI: A device identifier for the package configuration that contains multiple units of the base package (does not include shipping containers17).
§
Package information for a particular version or model of a device is part of the DI record. See section III.A.(2).i below for more information.
o
Previous DI: A device identifier that was assigned to a given version/model of a medical device before the same version/model of the device was assigned a new or substitute device identifier for reasons other than changes to the device physical specifications or new indications for use that change the version or model. For example, such changes might occur due to mergers and acquisitions, where the acquiring company might decide to assign a new device identifier.
§
Note that Previous DI number should be a valid Primary DI in another DI record.
- All DIs will be checked for uniqueness in the GUDID. Once used, a DI can never be reassigned to another device, even if the original device is no longer in commercial distribution (see 21 CFR 830.40(c)).
o
When Commercial Distribution End Date &lt;= today (i.e. today or a date in the past), the device will be considered no longer held or offered for sale by the labeler. The device may or may not still be available for purchase in the marketplace.
o
The device will still be in the database and available via public search, but will be noted as “Not in Commercial Distribution”.
Each DI record will be subject to GUDID business rules to ensure data quality. GUDID business rules for each data attribute are provided in the GUDID Data Elements Reference Table, available on www.fda.gov/udi.
Business rules include the following: - Required data attributes must be provided (21 CFR 830.310) – see GUDID Data
Elements Reference Table, available on Prepare for GUDID | FDA for a list of required attributes. While some fields in GUDID are not required, we recommend that labelers 16 Refer to the FDA guidance documents titled “Unique Device Identification: Direct Marking of Devices” and “Unique Device Identification: Policy Regarding Compliance Dates for Class I and Unclassified Devices, Direct Marking, and Global Unique Device Identification Database Requirements for Certain Devices.”
17 The UDI Final Rule defines a Shipping Container as a container used during the shipment or transportation of devices, and whose contents may vary from one shipment to another.
populate all fields applicable to the device when the information is available in the device labeling. For example, while Device Description is not required in GUDID, if you populate this attribute, users will benefit from the information.
- Validation of specified attributes. For example, the system will only accept a valid FDA Listing Number.
- Data constraints on specified attributes. For example, the system will only accept a
Publish Date >= today (i.e., today or a date in the future).
- System rules that determine available user actions based on the status of the DI record.
For example, only Unpublished and Published DI records can be copied. Sections III.A.(3).a and III.B.(1).a provide system rules for each DI record state.
a) Package Information in GUDID
According to 21 CFR 801.3, a device package is a fixed quantity of a particular version or model of a device. In order to adequately identify a device throughout distribution and use, the various package configurations, i.e., each different type of package, must have a UDI, 21 CFR 801.20(a)(2). Thus, if a device is sold in individual device packages, in boxes with 30 device packages, and cartons that contain 12 boxes of 30 device packages, a different DI would be required to appear on the individual device package, on the box of 30 device packages, and on the carton of 12 boxes (see 21 CFR 830.50(b)).
Following are key points to note regarding package information in GUDID: - The Primary DI number for a DI record identifies the lowest level of medical device package containing a full UDI; also known as the base package. The Primary DI, therefore, is also the base package DI.
- The Device Count attribute provides the number of medical devices in the base package.
- Package configurations of the base package are part of the base package DI record.
- Package configurations inherit base package attribute values. Therefore, Package DIs do not need their own DI record; instead, package information can be entered in the Package DI section of the Primary DI record for that device. Attributes specific to each package can be entered and include: o
Package DI – DI for the particular package configuration (does not include shipping containers).
o
Contains DI Package – DI for the lower level package configuration contained within that particular package configuration (what is the DI for the package inside this package?).
o
Quantity per Package – number of packages contained within the particular package configuration with a unique DI (how many packages are inside this package?).
o
Package Type – optional text to describe the outer packaging of the product (e.g., box, carton) and enables users to understand higher-level packaging configurations.
o
Package Discontinue Date – indicates the date a particular package configuration is discontinued by the labeler.
o
Package Status – indicates whether the package configuration is in commercial distribution as defined under 21 CFR 807.3(b); auto-populated by the system based on Package Discontinue Date: §
If Package Discontinue Date > today (i.e., a date in the future) or null, then Package Status = “In Commercial Distribution”
§
If Package Discontinue Date =&lt; today (i.e., today or a date in the past), then Package Status = “Not In Commercial Distribution”
Figure 2 provides a package configuration example for GUDID where the DI is on the individual device with one package level.
- Oral/enteral syringe, each with Primary DI 00884838035683 and Device Count = 1.
- Box of 100 syringes, with Package DI 30884838035684 (contains 100 units of Primary DI 00884838035683).
- Package Discontinue Date is blank (null); therefore Package Status is set to “In Commercial Distribution.”
Package 30884838035684 inherits all attribute values of base package 00884838035683, except for the attributes specific to 30884838035684, as shown in the table below.
Base Package Primary Device Identifier Device Count 00884838035683 Package Information Package DI Quantity per Package Contains DI Package Package Type Package Discontinue Date Package Status 30884838035684
00884838035683
Box In Commercial Distribution
Figure 2: Package Configuration Example18
Additional examples of package configurations, along with attribute values pertinent to packages, 18Device Identifiers used in the example are fictitious. Please refer to “UDI Formats by FDA Accredited Issuing Agency” in Appendix C for correct format of the DI numbers by FDA Accredited Issuing Agencies.
are provided in Appendix A.
b) Global Medical Device Nomenclature (GMDN)
Each DI record in GUDID requires entry of at least one GMDN Term Code (see 21 CFR 830.310). The GUDID business rules allow more than one GMDN Term Code to be assigned per DI record, but this allowance was developed for the rare occurrence where more than one term is needed to accurately describe the device. It is expected that most records contain only one GMDN Term Code.
GMDN is a system of internationally agreed upon descriptors used to represent common device types for the purposes of grouping or categorization. GMDN Terms, managed by the GMDN Agency, have been developed as a vocabulary that represents the whole medical device arena, including such specialties as dental products, laboratory equipment, in vitro diagnostics, and biologic devices with cellular or tissue origins. Each GMDN Term has 3 components: Preferred
Term Code (5-digit number), Preferred Term Name, and Preferred Term Definition. GMDN is maintained and updated to represent the evolving medical device field; meaning Names and
Definitions may be edited, new terms may be developed and outdated terms may be made obsolete.
The GUDID represents the first implementation of the GMDN within FDA. To obtain access to the GMDN vocabulary and to select GMDN Terms for submission to the GUDID, companies should first become a member of the GMDN Agency. Visit http://www.gmdnagency.com for details. The GMDN Agency offers multiple membership options, including a basic membership option free of cost.
Prior to submission of DI records to the GUDID, ensure the following: - Identify and obtain the appropriate GMDN Terms for devices requiring GUDID submission.
- NOTE: if a device necessitates the development of a new device category, or a new GMDN Term, this requires time, so please plan accordingly.
o
When selecting a GMDN Term, be advised that GMDN Term Definitions may contain language with a specific regulatory definition or implication to FDA.
Assignment of a GMDN Term with such language in the Term Name or Term
Definition to your DI record does not imply agreement by FDA to a particular regulatory interpretation for your device.
- If your company has GMDN Terms that are currently in use, use the GMDN Agency as a resource to evaluate the following: o
Term fitness – determine if this GMDN Term or device category best represents the device o
Term Status – determine if terms are “active” or have been made “obsolete” o
If your company’s GMDN Term Codes have been designated as “obsolete,” identify replacements by searching the GMDN vocabulary or contacting the GMDN Agency for assistance.
- Submit only active GMDN Terms to the GUDID.
During submission of DI records: - For DI record entry via the web user interface, the GMDN Term Code should be used to assign the GMDN Term to the record; the GMDN Term Name and GMDN Term
Definitions fields will be auto-populated. (For submission of GMDN Term Codes in HL7 SPL xml files, see GUDID HL7 SPL Implementation Specification files, available at www.fda.gov/udi ) Maintaining GMDN Codes in DI Records: - It is the responsibility of labelers to make sure their DI record information is accurate and up-to-date throughout the Total Product Lifecycle (TPLC) of the device. If you maintain a paid membership with GMDN, GMDN notifies you when your terms have been modified or made obsolete. If not, it would be your responsibility to monitor your GMDN terms periodically for any changes or when needed due to validation rules.
- If a GMDN Term becomes obsolete, the labeler/LDE user should update the GMDN
Term in order to pass validation when updating any other DI record attribute.
- Once a DI record has been published in the GUDID with an active GMDN Term, that assignment remains until changed by the labeler/LDE user. There is no automatic update of GMDN terms within the GUDID.
- If GMDN information changes, the updated information must be submitted within 10 business days of the change per 21 CFR 830.330(b).
Labelers in need of assistance with term selection or new term development are encouraged to contact the GMDN Agency, www.gmdnagency.com.
NOTE: Representation of GMDN in Appendix D, Figure D1, a Fictitious Medical Device
Label is for illustration purposes ONLY. GMDN Term Name and Definition are NOT expected to appear on the label of a device.
(3)
DI Record Life-Cycle
The GUDID DI record life-cycle comprises the various states of a DI record and the associated business rules and functionality available to a user. Please note that the DI record life-cycle applies to both GUDID submission options – Web Interface and HL7 SPL xml file submission; where there are differences due to the type of submission, they have been noted.
a) DI Record States
A DI record is in one of three DI record states at any given time. The DI record state determines the applicable business rules and the GUDID functionality available to users.
A new DI record may be saved in one of the following three DI record states: Draft DI record,
Unpublished DI record, or Published DI record. Only DI records in a published state will be considered to have met the GUDID submission requirements under 21 CFR 830 Subpart E.
Draft DI Record: enables you to prepopulate and save a DI record with the available information via the GUDID Web Interface. Additionally, users may also create Draft DI records to get familiar with creating and saving DI records in GUDID; however, please do not Submit records for publishing when created solely for the purpose of familiarizing yourself with the system.
Merely creating and saving Draft DI records does not fulfill your GUDID submission requirements under 21 CFR 830 Subpart E. Please note that the Draft DI record state is only applicable to the GUDID Web Interface option. HL7 SPL submissions cannot be submitted as Draft DI records.
A Draft DI record: - Does not have to pass any business rules prior to being saved as a Draft DI record.
- Can be edited an unlimited number of times via the GUDID Web Interface.
- Can be saved in the Draft DI record state for 180 calendar days; the record will be “purged”, i.e., permanently removed from the GUDID, after 180 calendar days of inactivity.
o Please note that the 180-day cycle resets and starts over each time the Draft DI record is edited and re-saved as a draft.
Can only be viewed/edited by the LDE user who created the record.
- Is not available for public search and retrieval.

A Draft DI record needs to pass Review, i.e., pass business rules before it can be Submitted to GUDID. Upon submission, the record then can be in Unpublished or Published state based on the Publish Date: - Unpublished state means Publish Date > today (i.e., a date in the future).
- Published state means Publish Date =&lt; today (i.e., today or a date in the past).
Unpublished DI Record: enables users to complete a DI record and Submit it to GUDID prior to the required date. Saving unpublished DI records alone does not fulfill your GUDID submission requirements under 21 CFR 830 Subpart E.
An Unpublished DI record: - Has passed all business rules, i.e., has passed Review.
- Has not reached the Publish Date (Publish Date > today (i.e., a date in the future)).
- Can be edited an unlimited number of times; however, each time the record is edited, the record pass business rules, i.e., Review again.
- Can be copied to create new DI records, enabling reduction of data entry time; all attributes except for the Primary DI number and package information are copied.
- Can be viewed by the FDA and LDE users assigned to the Labeler DUNS associated to the given DI record. FDA may review your Unpublished DI records for data quality assessment and contact you with questions.
- Is not available for public search and retrieval.
- Will be checked by an automated GUDID nightly process, and when Publish Date = today, the record will move to the Published DI record state.
Published DI Record: a DI record that is available for search and retrieval by the public. We will consider you to have complied with the requirements of 21 CFR 830.330 on the date that the DI record is saved in GUDID in the published state.
A Published DI record: - Has passed all business rules, i.e., has passed Review.
- Has Publish Date =&lt; today (i.e., today or a date in the past). Please note that a DI record entered with Publish Date = today, will be available for public search immediately.
- Can be copied to create new DI records, enabling reduction of data entry time; all attributes except for the Primary DI number and package information are copied.
- Is available for public search and retrieval.
- Is subject to editing limitations as determined by the Grace Period. The Grace Period is 7 calendar days and starts the day after the DI record is published.
Publish Date Grace Period Start Date Grace Period End Date Monday, July 15, 2013 Tuesday, July 16, 2013 Monday, July 22, 2013, 11:59pm o Editing within-the-Grace-Period §
All attributes, except Publish Date can be edited.
o Editing after-the-Grace-Period will be limited §
New DI trigger attributes cannot be edited; these are core attributes which, when changed, no longer represent the same device and require a new DI (see 21 CFR 830.50).
§
Certain attributes would have limited editing capability; a complete list of edit rules are available in the Data Elements Reference Table, available on www.fda.gov/udi. For example: Ø FDA Premarket Submission Number: can ‘Add’ Premarket Submission Numbers after the grace period cannot ‘Edit’ or ‘Delete’ existing values after the grace period §
In the rare situation where New DI trigger attributes or attributes with limited editing need to be edited after-the-grace-period,19 you can ‘unlock’ the record to make the edits. See ‘GUDID Manual: Unlocking Device Records for Editing’ for more information.
Please note that Published DI records for devices removed from commercial distribution will remain in the published state and will be available for public search and retrieval. It is the responsibility of the labeler to update the DI records for discontinued devices. The Commercial
Distribution Status will be auto-populated by the system based on Commercial Distribution End Date as shown below.
- When Commercial Distribution End Date> today (i.e., a date in the future) or null,
Commercial Distribution Status = “In Commercial Distribution.”
- When Commercial Distribution End Date =&lt;today (i.e., today or a date in the past),
Commercial Distribution Status = “Not In Commercial Distribution.”
19 Edits to New DI trigger attributes and attributes with limited editing after-the-grace-period is expected to be an extremely rare occurrence. Labelers should ensure their DI record data is accurate before the record moves to the published state.
The table below provides a summary of the three DI record states: DI Record State Description System Save duration Possible Actions on the DI Record Available via Public Search?
Draft DI record Saved DI record that has not passed business rules Please note that HL SPL Submissions cannot be submitted as Draft DI records.
This state is only applicable to the GUDID Web Interface option.
Purged after 180
calendar days of inactivity; if edited and resaved as draft, the 180calendar day cycle resets and starts over
- Unlimited editing
- Resave as Draft
- Delete Draft
- Needs to pass
business rules and be Submitted to move to other DI record states
- No
- only available
to the LDE user who created the record Unpublished DI record DI record that has passed GUDID business rules, been Submitted to GUDID AND Publish Date > today (i.e., in the future) Saved indefinitely
- Copy
- Unlimited editing
- System
publishes DI record when Publish Date =
today
- No
- available for
editing by LDE users assigned to the particular Labeler DUNS number
- can be viewed
by FDA Published DI record DI record that has passed GUDID business rules, been Submitted to GUDID AND Publish Date &lt;= today (i.e., today or in the past)
- Cannot move to
other DI states without FDA staff intervention Saved indefinitely
- Copy
- Limited editing
during and after Grace Period based on business rules
- Yes
- available for
editing by LDE users assigned to the particular Labeler DUNS number
- can be viewed
by Coordinators, LDE users, FDA, Public Users
Table 1: Summary of DI Record States
### B. GUDID Modules
Now that the key GUDID concepts are familiar, this section provides a description of the GUDID Modules.
The GUDID provides two options for submission of device identification information: 1) Submission of one DI record at a time via the secure GUDID Web Interface.
2) Submission of one DI record per XML file via the HL7 SPL submission option.
Both submission options need a GUDID account. Please note that the GUDID account is not by submission type, i.e., a labeler does not need to have a separate GUDID account for each submission option. The GUDID account identifies the labeler in GUDID and enables submission of device information via both options.
The overall concepts presented in this guidance document apply to both submission options.
Where there are differences, they have been noted.
GUDID provides two information retrieval options for published DI information: 1) Search and retrieval of device information via the web interface 2) Download and web service capabilities are planned for the future GUDID accounts are NOT needed for search and retrieval of published information.
Figure 3 provides a pictorial representation of the GUDID modules described above.
Figure 3: GUDID Overview (1)
GUDID Web Interface
The GUDID Web Interface module enables creation of GUDID accounts, submission of DI records, and search and retrieval of device information. For details related to account creation, see section III.A.(1). This section focuses on submission of device information; search and retrieval details are presented in Section III.B.(3).
a) GUDID Device Identifier Module
The DI module enables creation and management of DI records by LDE users. As indicated in
Section III.A.(1).b, when coordinators create LDE users, LDE users will receive a temporary login and password via a system generated email. LDE users may then login and use the GUDID.
The DI module enables LDE users to: - Create DI records; - Save, edit, and manage Draft DI records; - Review and validate DI records against system business rules; · Copy Unpublished and Published DI records; - Edit and manage Unpublished and Published DI records; and - Search and retrieve ALL attributes of DI records for their assigned Labeler DUNS numbers. Note that this is different from public search users who can only view attributes indicated “public” in the Data Elements Reference Table, available on www.fda.gov/udi.
The next few sections detail the DI record life-cycle functions in GUDID.20 These include: · Creating a New DI Record; · Editing a Draft DI Record; · Editing Unpublished or Published DI Records; and · Copying DI Records.
i.
Creation of a New DI Record
When created using the GUDID Web Interface, the DI record life-cycle begins with the creation of a new DI record, see Figure 4. Draft DI records cannot be submitted via the HL7 SPL submission option. Once created, a new DI record may be saved as a Draft DI record and
Reviewed against the business rules. Based on the Publish Date, the record would then be promoted to the Unpublished or Published DI record state.
Figure 4 provides a pictorial representation of the new DI record creation process which is explained below.
20 For detailed information on the accessing and creating DI records in GUDID, refer to, Global Unique Device Identification Database (GUDID) User Manual.
Figure 4: Creating a New DI Record
After creating a new DI record, the LDE user may choose to: · Save the record as Draft DI record.
- Cancel creation of a new DI record.
- Review DI record to run GUDID business rules o
If the record FAILS business rules, the user can: §
Save as Draft DI record so errors can be fixed at a later time.
§
Cancel creation of new DI record.
o
If the record PASSES business rules, the user can: §
Resave as Draft DI record.
§
Edit record further; once edited, the record needs to pass business rules again; it can be saved as Draft DI record, or edits can be Cancelled.
§
Cancel creation of new DI record.
§
Submit the record to GUDID; the DI record state will be set by the system based on Publish Date.
Ø Unpublished state means Publish Date > today (i.e., a date in the future).
Ø Published state means Publish Date &lt;= today (i.e., today or a date in the past).
Note that Submitting a DI record to GUDID does not fulfill your GUDID submission requirements. We will consider you to have complied with the requirements of 21 CFR 830.330
on the date the DI record is saved in the published state.
ii.
Editing a Draft DI Record
As noted above, a new DI record created via the GUDID Web Interface can be saved as Draft DI record,21 which can move to other DI record states after it passes business rules. Draft DI records can be edited and resaved as Draft DI records.
Figure 5 provides a pictorial representation of editing a Draft DI record, which is explained 21 Draft DI records cannot be submitted via the HL7 SPL submission option.
below.
Figure 5: Editing a Draft DI Record
The LDE user can edit the Draft DI record and: - Save as Draft again. Recall that Draft DI records can be edited and resaved as drafts an unlimited number of times.
o
A Draft DI record is purged from the system, i.e., permanently removed from GUDID, after 180 days of inactivity.
o
Each time a Draft DI record is edited, the 180 calendar day clock is reset as shown in the table below.
- Delete the Draft DI record.
- Cancel the edits.
- Review the Draft DI record to run GUDID business rules. See section III.B.(1).a.i,
Creation of New DI Record, for details of the Review process.
Table 2 below provides an example of how the purge date is reset.
Primary DI Number User Action Date User Action Draft DI Record Edit Date Purge Date Comments December 7, 2023 Enter and save a DI record as a draft via the GUDID Web Interface December 7, 2023 June 5, 2024 Draft DI records are saved in the system for 180 calendar days after which the record is purged Primary DI Number User Action Date User Action Draft DI Record Edit Date Purge Date Comments December 17, 2023 Edit record, resave as draft via the GUDID Web Interface December 17, 2023 June 15, 2024 Purge date is reset each time the record is edited and saved
Table 2: Draft DI Purge Date Examples iii.
Editing Published or Unpublished DI Records
Published and Unpublished DI records can be edited as follows: - Unpublished DI records can be edited an unlimited number of times and all attributes may be edited; however, once edited, the record needs to go through Review and pass business rules again.
- The extent of editing on a Published DI record is determined by the Grace Period, which starts the day after the DI record is published and ends after 7 calendar days. As explained earlier in the document: § within- the-grace period, all attributes, except Publish Date can be edited.
§
after-the-grace-period, editing will be limited.
Ø New DI trigger attributes cannot be edited; these are attributes, which when changed, no longer represent the same device and would require a new DI (see 21 CFR 830.330(b)).
Ø Certain attributes will have limited editing capability.
Ø See the GUDID Data Elements Reference Table, available on www.fda.gov/udi, for edit rules for all attributes.
Table 3 below illustrates the Grace Period concept via an example.
Primary DI Number User/System Action Date User/System Action Publish Date Grace Period Start Date Grace Period End Date Comments July 19, 2024 Create a new DI record, pass business rules; save.
July 29, 2024 N/A N/A Unpublished record, grace period does not begin until the record is published July 23, 2024 Edit record, change publish date July 25, 2024 N/A N/A Unpublished record, grace period does not begin until the record is published Primary DI Number User/System Action Date User/System Action Publish Date Grace Period Start Date Grace Period End Date Comments July 24, 2024 GUDID nightly system process publishes the record July 25, 2024 July 26, 2024 August 1, 2024, 11:59PM July 27, 2024 Edit New DI trigger attribute within grace period, check that device is combination product July 25, 2024 July 26, 2024 August 1, 2024, 11:59PM Once published, grace period does not reset August 2, 2024 Attempts to edit a New DI trigger attribute, Version or Model Number, but can not July 25, 2024 July 26, 2024 August 1, 2024, 11:59PM New DI trigger attributes CANNOT be edited after grace period ends Table 3 Grace Period Example
In addition to editing Draft DI records as explained in Section III.B.(1).a.ii, the LDE user can edit Unpublished or Published DI records and: - Review the edited DI record to run GUDID business rules. See Section III.B.(1).a.i above on Creation of a New DI Record for details of the Review process.
- Cancel the edits.
Figure 6 provides a pictorial representation of editing an Unpublished or a Published DI record.
Figure 6: Editing an Unpublished or a Published DI Record
There is a key difference between editing a Draft DI record and editing an Unpublished or a Published DI record: · after editing a Draft DI record, it can be resaved as a Draft DI record.
- after editing an Unpublished or a Published DI record, the record CANNOT be saved as a
Draft DI record; the record has to pass business rules. The record needs to be Reviewed and Submitted or the edits will be cancelled.
All edits to Unpublished and Published DI records are logged in GUDID. LDE users may view the following information about the history of a DI record via the GUDID Web Interface – Edit Date, Edit Time and Name of the user who edited the DI record; for submissions edited via the HL7 SPL submission option, user is noted as “SPL User”. Details of which attributes were edited are presently not exposed and therefore not viewable by users. DI record history information is not exposed to public users of GUDID when a record is retrieved via GUDID Public Search.
GUDID offers two DI record submission options, the GUDID Web Interface and the HL7 SPL submission option. Entering a record via one option and editing via another option allows for the possibility of inconsistencies between the labeler’s source data and GUDID data. Therefore, for all edits to a DI record, we recommend you use the same submission option you used to initially create and submit the DI record to GUDID. The labeler is responsible for developing and maintaining SOPs for data quality and data integrity with respect to GUDID submissions.
iv.
Copying DI Records
Unpublished and Published DI records can be copied while using the GUDID Web Interface, however Draft DI records cannot.
- The GUDID Web Interface DI record “Copy” function enables the user to copy all attributes of a DI record to a new DI record, except for the Primary DI number22 and package information. This enables the user to reduce data entry time.
- A copied record begins as a Draft DI record and needs to pass business rules to be promoted to other DI record states.
Figure 7 provides a pictorial representation of the Copy functionality in GUDID as explained below.
Figure 7: Copying DI Records
The LDE user can Copy Unpublished and Published DI records and: - Save as a Draft DI record. Recall that the copied DI record begins as a Draft DI record and follows the DI record life-cycle to move to other DI record states.
- Cancel the copy action; the new DI record would not be saved in GUDID.
- Review the Copied DI record against GUDID business rules. See Section III.B.(1).a.i above on Creation of a New DI Record for details of the Review process.
(2)
HL7 SPL Submission
The HL7 SPL Submission option enables companies to electronically submit device information one DI record at a time as an HL7 SPL xml file via the FDA ESG. For detailed technical specifications on HL7 SPL submission option, please refer to the GUDID HL7 SPL
Implementation Files, available at www.fda.gov/udi.
Companies that choose the HL7 SPL submission option should do the following: - Establish a GUDID account. See Section III.A.(1) for details.
o
Coordinator and Labeler Data Entry user roles are optional for HL7 SPL submissions since submissions are sent as XML files. However, if labelers choose to have Coordinator and LDE users, they may do so.
22 Primary DI Number is the Device Identifier on the base package of a medical device.
- Use the FDA ESG to submit HL7 SPL files.
o
Complete ESG account establishment and testing process. Visit www.fda.gov/esg for more information.
- Once GUDID and ESG accounts are established, companies should complete GUDID testing prior to production submissions. Detailed information on the GUDID testing process is available as part of the GUDID HL7 SPL Implementation Files on www.fda.gov/udi - Companies may choose to use third-party submitters to submit device information on their behalf. Please review Section III.A.(1) for more information on using a third-party to submit device information to GUDID.
o
We are enabling third-parties to test their GUDID HL7 SPL submission solution by providing them with test GUDID accounts. Labelers using third-parties who may have completed testing should still complete the test scenarios listed as part of the GUDID HL7 SPL Implementation Files prior to moving to production GUDID HL7 SPL submissions.
(3)
Search/Retrieval of Device Information
The GUDID data is available for use by public users, i.e., consumers, health-care providers, hospital systems, via two public portals: AccessGUDID and OpenFDA. Published data would include all DI record attributes with a few exceptions such as:, Company Physical Address, FDA
Listing Number. Please see the GUDID Data Elements Reference Table, available on www.fda.gov/udi for a list of attributes that are not released to the public.
## IV. GUDID Submissions and 21 CFR Part 11 Requirements

Labelers should become familiar with all the requirements of 21 CFR Part 11 and the FDA guidance document titled “Part 11 Electronic Records; Electronic Signatures – Scope and Application.”
All submitters – must retain records in accordance with 21 CFR 830.360. If those records are kept electronically, part 11 applies. However, a record that is not itself submitted, but is used in generating a submission, is not a part 11 record. That is, a record developed to collect all the data elements required to be entered into a device record via the GUDID web user interface is not subject to part 11 requirements.
SPL submitters – must retain records in accordance with 21 CFR 830.360 and all records submitted to FDA. The HL7 SPL solution must be compliant with the requirements of part 11.
The GUDID SPL submission does not need a signature; therefore, part 11 requirements specific to electronic signatures (21 CFR 11 Subpart C) do not apply. However, please do not confuse an electronic signature with a digital certificate. A digital certificate serves to authenticate the sender and is needed for all submissions to the FDA ESG, including GUDID.
Once an SPL submission is successfully delivered to the GUDID, labelers should be able to view and edit data elements via the web interface. This allows for the possibility of inconsistencies between the labeler’s source data submitted via SPL and GUDID data. Labelers should develop and adhere to SOPs for data governance to maintain the quality of their device data.
Third-party submitters/Solutions Providers – are not responsible to the FDA to meet regulatory requirements for UDI or part 11. It is the responsibility of the labeler (or data owner) to meet the records requirements for 21 CFR 830.360 and the requirements of 21 part 11. The contractual language between labeler and third-party submitter is not within the purview of the FDA.
Appendix A – GUDID Package Information Examples23
The examples below illustrate how package information is entered into the GUDID along with attribute values pertinent to packages.
EXAMPLE 1: UNIT OF USE DI + ONE PACKAGE LEVEL
The figure below provides a package configuration example for GUDID where the medical device has Unit of Use DI Number and one package level.
- Box of 100 single use blood collection tubes with the Primary DI 20001 and Device Count = 100.
o
Note that the tubes themselves do not have the DI on them as they fall under the general exception for individual single use device under 801.30(a)(3). Each tube however, gets a virtual Unit of Use DI assigned, and in this case, 10001.
- Case of 8 boxes (800 total), with Package DI 30001 (contains 8 of Primary DI 20001), Quantity per Package = 8.
- Package Discontinue Date is blank, therefore system auto-populates Package Status to “In Commercial Distribution.”
23 Device Identifiers used in all the examples are fictitious. Please refer to “UDI Formats by FDA Accredited Issuing Agency” (see Appendix C, available on www.fda.gov/udi) for correct format of the DI numbers by FDA Accredited Issuing Agencies.
Package 30001 inherits all attribute values of base package 20001, except for the attributes specific to 30001 such as Quantity per Package, as shown in the table below.
Base Package Package DI
Figure A1: GUDID Package Configuration Example 1
EXAMPLE 2: DI ON INDIVIDUAL DEVICE + MULTIPLE PACKAGE LEVELS
The figure below provides a package configuration example for GUDID where the DI is on the individual device with two package levels.
- Catheter, 12 Fr, each with Primary DI 1001 and Device Count = 1.
- Box of 30 catheters with Package DI 2001 (contains 30 of Primary DI 1001).
- Case of 12 boxes (540 catheters), with Package DI 3001 (contains 12 of Package DI 2001).
- Box of 50 catheters with Package DI 2002 (contains 50 of Primary DI 1001).
- Package Discontinue Date is blank, therefore system auto-populates Package Status to “In Commercial Distribution.”
Package 2001, 3001 and 2002 inherit all attribute values of base package 1001, except for the attributes specific to each package, as shown in the table below.
Primary Device Identifier Device Count Unit of Use DI 20001
10001
Package DI Quantity per Package Contains DI Package Package Type Package Discontinue Date Package Status 30001
20001
Case In Commercial Distribution Base Package Primary Device Identifier Device Count 1001 Package DI Package DI Quantity per Package Contains DI Package Package Type Package Discontinue Date Package Status 2001
1001
Box In Commercial Distribution 3001
2001
Case In Commercial Distribution 2002
1001
Box In Commercial Distribution
Figure A2: Package Configuration Example 2
Appendix B – GUDID Data Elements Reference Table
For a complete list of GUDID attributes, please refer to the GUDID Data Elements Reference Table available at www.fda.gov/udi.
Appendix C – UDI Formats by FDA Accredited Issuing Agency
For information on UDI Formats by FDA Accredited Issuing Agency, please visit www.fda.gov/udi.
Appendix D – GUDID Attributes Mapped to a Fictitious Medical Device Label
Many GUDID data attributes appear on the medical device label. When a GUDID attribute appears on the medical device package/label, the values submitted to the GUDID should match the value on the label. Figure D1 shows a fictitious medical device label and identifies the GUDID data attributes that appear on the label.
Figure D1: GUDID Attributes Mapped to a Fictitious Medical Device Label NOTE: Representation of GMDN above is for illustration purposes ONLY. GMDN Term Name and GMDN Term Definition are NOT expected to appear on the label of a device.
Abbreviations & Acronyms Term Description DI Device Identifier D&B Dun & Bradstreet DUNS Data Universal Numbering System ESG FDA Electronic Submissions Gateway GMDN Global Medical Device Nomenclature GUDID Global Unique Device Identification Database HCT/P
Human Cell, Tissue or Cellular or Tissue-Based Product FDA Food and Drug Administration FDAAA FDA Amendments Act FDASIA FDA Safety and Innovation Act HL7 Health Level 7 PI Production Identifier SPL Structured Product Labeling UDI Unique Device Identifier Glossary Term Description Base Package
The lowest level of a medical device package containing a full UDI. The DI on the base package is the Primary DI.
Coordinator Individual(s) responsible for management of the GUDID account, for designated Labelers.
Data Universal Numbering System (DUNS)
A unique 9-digit identification number assigned and managed by Dun & Bradstreet to business entities.
Device Identifier (DI)
A mandatory, fixed portion of a UDI that identifies the labeler and the specific version or model of a device (21 CFR 830.3).
Device Identifier Record (DI Record)
The DI, together with associated data attributes constitutes a DI record for a particular device version or model.
DI Record Life-Cycle
Comprises of the various states of a DI record and the associated business rules and functionality available to a user.
DI Record States
A DI Record is in one of three DI Record States at any given time:
Draft DI Record, Unpublished DI Record, or Published DI Record.
Direct Marking DI
An identifier that is marked directly on the device; can be the same as or different from the Primary DI; only applicable to devices subject to Direct Marking requirements under 21 CFR 801.45.
Device Package
A package that contains a fixed quantity of a particular version or model of a device.
Draft DI Record
Saved DI record that has not passed business rules.
Electronic Submissions Gateway (ESG)
An FDA-wide solution for accepting secure electronic regulatory submissions.
Global Medical Device Nomenclature (GMDN)
A system of internationally agreed descriptors used to identify medical device products and is managed by the GMDN Agency.
Grace Period
Seven calendar days and starts the day after the DI record is published; determines the extent of editing possible on a DI record.
GUDID
Global Unique Device Identification Database, the repository of device identification information for devices specified under the FDA UDI Final Rule.
GUDID Account
A GUDID account enables companies to access and submit information to the GUDID.
Term Description GUDID Web Interface
An online interface that enables secure account creation, secure submission of DI records, and search and retrieval of device information.
Health Level 7 (HL7)
A standards development organization, whose mission is to provide messaging standards for interoperability, exchange, Term Description management, and integration of data that supports clinical patient care and the management, delivery, and evaluation of healthcare services.
Issuing Agency
Organization accredited by FDA to operate a system for the issuance of UDIs.
Labeler
Any person who causes a label to be applied to a device with the intent that the device will be commercially distributed without any intended subsequent replacement or modification of the label; and, any person who causes the label of a device to be replaced or modified with the intent that the device will be commercially distributed without any subsequent replacement or modification of the label, except that the addition of the name of, and contact information for, a person who distributes the device, without making any other changes to the label, is not a modification for the purposes of determining whether a person is a labeler. (21 CFR 801.3) Labeler Data Entry (LDE) User Individual(s) responsible for day to day entry, submission and management of device identification information for designated Labeler DUNS into the GUDID.
Listing Number
Number assigned by FDA during Registration and Listing to all devices in commercial distribution, regardless of premarket authorization requirements, per 21 CFR 807.28(f) New DI Trigger Attributes Attributes, which when changed, no longer represent the same device thereby requiring the creation of a new DI.
Device Package
A package that contains a fixed Quantity of a particular version or model of a device (21 CFR 801.3).
Package DI
A device identifier for the package configuration that contains multiple units of the base package (does not include shipping containers).
Primary DI
An identifier that is the main (primary) lookup for a medical device and meets the requirements to uniquely identify a device through its distribution and use (21 CFR see 830.3). The Primary DI would be located on the base package, which is the lowest level of a medical device containing a full UDI. For medical devices without packaging, the Primary DI number and full UDI may be on the device itself.
Product Code
Three letter classification code for premarket devices issues by FDA.
Production Identifier(s)
(PI)
A conditional, variable portion of a UDI that identifies one or more of the following when included on the label of the device (21 CFR 830.3): (i) The lot or batch within which a device was manufactured; (ii) The serial number of a specific device; (3) The expiration date of a specific device; (iv) The date a specific device was manufactured.
(v) For an HCT/P regulated as a device, the distinct identification Term Description code required by 21 CFR 1271.290(c).
Published DI Record
A DI record that is published, and therefore is available for search and retrieval by the public.
Regulatory Contact
Individual responsible for management of GUDID submission requirements for the Labelers in a given GUDID account.
Relabler Relabeler, for the purposes of 21 CFR 830.60, is a new labeler that changes the content of the labeling from that supplied from the original labeler for distribution under the new labeler's own name.
A relabeler does not include labelers that do not change the original labeling but merely add their own name.
Secondary DI
An identifier that is an alternate (secondary) lookup for a medical device that is issued from a different issuing agency than the primary DI.
Structured Product Labeling (SPL)
A HL7 standard for the exchange of product information using extensible markup language.
Support Contact
Contact for consumers and healthcare providers to obtain additional information about the device.
Third-party submitters Companies/individuals (contractors, vendors) authorized to submit GUDID information on behalf of the Labeler.
Unique Device Identifier (UDI)
A unique numeric identifier composed of the device identifier and production identifier(s) that uniquely identify a medical device through distribution and use (21 CFR 830.3).
Unit of Use DI
An identifier assigned to an individual medical device when a UDI is not labeled on the individual device at the level of its unit of use.
Its purpose is to associate the use of a device to/on a patient.
Unpublished DI Record DI record that has passed GUDID business rules AND Publish Date > today.

---

## Footnotes

[^3]: See “UDI Formats by FDA-Accredited Issuing Agency” document, available on www.fda.gov/udi.

[^5]: 21 CFR 1271.290(c) requires that the manufacturer of each HCT/P assign and label the HCT/P with a distinct identification code that allows the manufacturer to relate the HCT/P to the donor and to all records pertaining to the

[^6]: See GUDID Data Elements Reference Table, available on www.fda.gov/udi.

[^15]: See GUDID Data Elements Reference Table, available on www.fda.gov/udi for a list of data attributes. below). ·
