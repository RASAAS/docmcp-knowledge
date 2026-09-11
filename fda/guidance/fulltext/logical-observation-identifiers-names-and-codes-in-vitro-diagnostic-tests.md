# Logical Observation Identifiers Names and Codes for In Vitro Diagnostic Tests : Guidance for Industry and Food and Drug Administration Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/logical-observation-identifiers-names-and-codes-in-vitro-diagnostic-tests](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/logical-observation-identifiers-names-and-codes-in-vitro-diagnostic-tests)

**Published:** 2018-06-15

---

<!-- Page 1 -->
Logical Observation Identifiers Names 
and Codes for In Vitro  
Diagnostic Tests 
______________________________________________________________________________ 
Guidance for Industry and  
Food and Drug Administration Staff 
 
Document issued on June 15, 2018.  
 
 
For questions about this document, contact the Digital Health Unit in the Office of the Center 
Director at (301) 796-6900 or email: DigitalHealth@fda.hhs.gov. 
 
 
 
 
 
 
 
 
 
 
 
 
U.S. Department of Health and Human Services 
Food and Drug Administration 
Center for Devices and Radiological Health 
Center for Biologics Evaluation and Research

---

<!-- Page 2 -->
Contains Nonbinding Recommendations 
 
 
Preface 
 
2 
 
 
Public Comment 
You may submit electronic comments and suggestions at any time for Agency consideration to 
https://www.regulations.gov. Submit written comments to the Dockets Management Staff, Food 
and Drug Administration, 5630 Fishers Lane, Room 1061, (HFA-305), Rockville, MD 20852.  
Identify all comments with the docket number FDA-2017-D-6982. Comments may not be acted 
upon by the Agency until the document is next revised or updated. 
Additional Copies 
Additional copies are available from the Internet. You may also send an e-mail request to CDRH-
Guidance@fda.hhs.gov to receive a copy of the guidance. Please use the document number GUD 
17032 to identify the guidance you are requesting. 
CBER 
Additional copies are available from the Center for Biologics Evaluation and Research (CBER) 
Office of Communication, Outreach and Development (OCOD), 10903 New Hampshire Ave., 
Bldg. 71, Room 3128, Silver Spring, MD 20993-0002, or by calling 1-800-835-4709 or 240-402-
8010, by e-mail, ocod@fda.hhs.gov, or from the Internet at 
https://www.fda.gov/BiologicsBloodVaccines/GuidanceComplianceRegulatoryInformation/ 
Guidances/default.htm.

---

<!-- Page 3 -->
Contains Nonbinding Recommendations 
 
 
Table of Contents 
I. 
Introduction ................................
 
3 
 
...........................................................................................................................4
II. 
Background ...........................................................................................................................................................5
III. Scope.....................................................................................................................................................................6
IV. LOINC Coding of IVDs........................................................................................................................................6
A. Is LOINC-coding mandated by FDA for IVD tests? ...............................................................6
B. Should manufacturers include LOINC codes in device labeling? ...........................................7
C. What are FDA’s views on manufacturers providing LOINC codes for uncleared or 
unapproved indications for use? ...............................................................................................7
D. Does FDA recommend a specific format for distributing LOINC codes? ...............................8

---

<!-- Page 4 -->
Contains Nonbinding Recommendations 
 
 
Logical Observation Identifiers Names 
and Codes for In Vitro  
Diagnostic Tests 
 
4 
 
 
Guidance for Industry and  
Food and Drug Administration Staff  
This guidance represents the current thinking of the Food and Drug Administration (FDA or 
Agency) on this topic. It does not establish any rights for any person and is not binding on 
FDA or the public. You can use an alternative approach if it satisfies the requirements of the 
applicable statutes and regulations. To discuss an alternative approach, contact the FDA staff 
or Office responsible for this guidance as listed on the title page. 
I. 
Introduction 
The Food and Drug Administration (FDA or Agency) recognizes that with the increasing 
implementation of electronic health records (EHR), there has been a greater demand to 
standardize the way that in vitro diagnostic (IVD) tests are coded. Efforts to harmonize and 
standardize information captured and stored in electronic healthcare systems carry important 
implications for public health, including expediting access to patient diagnostic information for 
healthcare providers, reducing burdens on laboratories for connecting new diagnostic systems to 
Laboratory Information Systems (LIS), and facilitating the use of healthcare information for 
decision support tools, in addition to many more potential uses.  
Information from IVD tests form a significant proportion of all EHRs. Laboratories commonly 
associate a LOINC® (Logical Observation Identifiers Names and Codes; owned, developed, and 
curated by the Regenstrief Institute)1 code with each test being performed by a laboratory. For 
each IVD test, LOINC provides a unique numeric code associated with test attributes that 
identify the type of IVD test such as the component, property, time, system, scale and method.2 
At present, LOINC is the IVD coding system that is most widely used by clinical laboratories 
and EHRs, and is the IVD coding standard recommended by the Office of the National 
Coordinator for Health Information Technology (ONC) in the U.S. Department of Health and 
Human Services (HHS) as an essential part of meaningful use. LOINC is a partially FDA-
                                                          
1 See http://loinc.org/ 
2 https://loinc.org/get-started/loinc-term-basics/

---

<!-- Page 5 -->
Contains Nonbinding Recommendations 
 
 
recognized consensus standard, where the recognition is limited to IVD tests. To review the 
classes of LOINC that are currently not recognized by FDA, see the FDA Recognized Consensus 
Standards Database Web site.
 
5 
 
3  
It is important to distinguish between LOINC codes and Unique Device Identifiers (UDIs). The 
LOINC coding system identifies the type of laboratory test being performed, and the UDI 
identifies a specific model/version of a regulated laboratory device made by a specific 
manufacturer.4 This guidance neither addresses nor affects the requirements related to the 
assignment of UDIs for regulated devices. 
FDA’s guidance documents, including this guidance, do not establish legally enforceable 
responsibilities. Instead, guidances describe the Agency’s current thinking on a topic and should 
be viewed only as recommendations, unless specific regulatory or statutory requirements are 
cited. The use of the word “should” in Agency guidance means that something is suggested or 
recommended, but not required. Similarly, the use of “should not” in this guidance does not 
suggest or create an independent legal prohibition, but indicates a recommended practice. 
II. Background 
The essential role of semantic interoperability in healthcare information technology has been 
well recognized.5 Executive Order 13410 defines interoperability as “the ability to communicate 
and exchange data accurately, effectively, securely, and consistently with different information 
technology systems, software applications, and networks in various settings, and exchange data 
such that clinical or operational purpose and meaning of the data are preserved and unaltered.”6 
FDA’s “Study Data Technical Conformance Guide” further defines semantic interoperability as 
“the ability of information shared by systems to be understood, so that nonnumeric data can be 
processed by the receiving system. Semantic interoperability is a multi-level concept with the 
degree of semantic interoperability dependent on the level of agreement on data content terminology 
and other factors. With greater degrees of semantic interoperability, less human manual processing is 
required, thereby decreasing errors and inefficiencies in data analysis. The use of controlled 
terminologies and consistently defined metadata support semantic interoperability.”7  
The unambiguous and consistent representation of laboratory tests is essential for achieving 
many of the potential benefits of electronic health records. Semantic interoperability is essential 
for developing decision support algorithms that can access and seamlessly aggregate data from 
multiple systems. For instance, in the context of infectious diseases, semantically interoperable 
EHR systems can allow for more efficient tracking of outbreaks or significant public health 
                                                          
3 See recognition consensus standards page for LOINC at 
https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfstandards/detail.cfm?id=32889. 
4 See http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/. 
5 See the shared nationwide interoperability roadmap at  https://www.healthit.gov/sites/default/files/hie-
interoperability/nationwide-interoperability-roadmap-final-version-1.0.pdf. 
6 See Executive Order 13410, Promoting Quality and Efficient Health Care in Federal Government Administered or 
Sponsored Health Care Programs, available at https://www.gpo.gov/fdsys/pkg/FR-2006-08-28/pdf/06-7220.pdf  
7 See “The Study Data Technical Conformance Guide,” available at 
https://www.fda.gov/downloads/ForIndustry/DataStandards/StudyDataStandards/UCM384744.pdf

---

<!-- Page 6 -->
Contains Nonbinding Recommendations 
 
 
threats by providing access to evaluable real-time IVD test information from multiple geographic 
locations. Consistent representation also allows EHR databases to be used to study diagnostic 
assays without having to adjust for different coding schemes at individual sites. Examples of 
studies using EHR databases might include post marketing studies that address the need for rapid 
nucleic acid assays to be routinely followed by conventional confirmatory methods, or studies 
that assess IVD performance in different clinical environments. Potential analysis of 
standardized data holds great promise for providing access to real-world evidence that may be 
useful for future regulatory actions. Unambiguous and consistent representation of IVD tests in 
EHRs can also minimize potential errors as information is transmitted across systems (for 
example, by ensuring that the correct units for test results are always maintained), helping to 
minimize patient risks as systems become increasingly interconnected. 
Semantic interoperability should be considered as a specific application of general 
interoperability. FDA’s support of the adoption of a uniform LOINC coding system for IVD tests 
is consistent with other FDA efforts in promoting aspects of medical device interoperability.
 
6 
 
8  
III. Scope 
As FDA seeks to encourage consistency in the coding of IVD tests, this guidance addresses 
questions regarding the distribution of LOINC codes by IVD test manufacturers to users, 
primarily clinical laboratories and software vendors. This guidance is restricted to the 
appropriate use of LOINC codes for specific types of IVD tests, and does not address the coding 
of test results for interoperability, for example, through the use of response sets within coding 
systems such as SNOMED-CT (Systematized Nomenclature of Medicine – Clinical Terms) or 
LOINC. It also does not address unique device identification (UDI), which identifies individual 
devices as required by statute and regulation.9  
IV. LOINC Coding of IVDs 
A. Is LOINC-coding mandated by FDA for IVD tests? 
No. LOINC, or any similar coding system for IVD tests, is voluntary and not required by FDA.10 
FDA, however, strongly encourages the use of consensus standards for coding of IVD tests and 
specifically recognizes the utility of LOINC for this purpose.11  
                                                          
8 See “Medical Device Interoperability,” available at 
http://www.fda.gov/medicaldevices/digitalhealth/ucm512245.htm. 
9 See http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/. 
10 As stated earlier, this guidance neither addresses nor affects UDI requirements. 
11 See recognition consensus standards page for LOINC at 
https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfstandards/detail.cfm?standard__identification_no=32889.

---

<!-- Page 7 -->
Contains Nonbinding Recommendations 
 
 
B. Should manufacturers include LOINC codes in device 
labeling? 
FDA supports the voluntary inclusion of LOINC codes for IVD tests in labeling if the 
information is accurate and consistent with the approved or cleared indications for the device. 
FDA does not intend to perform premarket review of LOINC codes that manufacturers may 
choose to provide to clinical laboratories or to other users. However, device labeling remains 
generally subject to other requirements of the Federal Food, Drug, and Cosmetic Act, including 
misbranding and adulteration.  
Manufacturers may choose to include LOINC codes in printed labeling or to include a reference 
to a location external to the labeling that lists or otherwise provides LOINC codes for the IVD 
test. For example, labeling could include a hyperlink to a web site with a table of LOINC codes 
associated with the manufacturer’s test(s). LOINC codes incorporated directly into devices – for 
example, LOINC codes included with device output that is directly transferred to an external 
system such as an LIS – may be subject to quality system requirements applicable to the device. 
C. What are FDA’s views on manufacturers providing LOINC 
codes for uncleared or unapproved indications for use? 
In general, LOINC codes provided by the manufacturer should be consistent with FDA-cleared 
or FDA-approved Indications for Use for that IVD test. A manufacturer’s dissemination, 
through, for example, inclusion in printed labeling or on manufacturer website, of a LOINC code 
that suggests an unapproved or uncleared indication for use may be considered evidence of a 
new intended use and result in the device being considered adulterated and/or misbranded under 
the FD&C Act.
 
7 
 
12  
However, FDA understands that a clinical laboratory or other persons may make individual, 
unsolicited requests to manufacturers for LOINC codes for specific uncleared or unapproved 
indications for use. In that event, where the manufacturer’s response provides the appropriate 
LOINC coding for the specific circumstance named in the request or identifies the need for a 
new LOINC code to address the clinical use referenced in the request, FDA does not intend to 
consider that response as evidence of the firm’s intent that the product be used for unapproved or 
uncleared uses.13  
                                                          
12 See sections 501(f)(1), 502(o), 513(f)(1), and 515 of the FD&C Act (21 U.S.C. 351(f)(1), 352(o)), 360c(f)(1), and 
360e).  See also FDA’s guidance for industry Drug and Device Manufacturer Communications with Payors 
Formulary Committees, and Similar Entities – Questions and Answers available at 
https://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm537347.pdf
13 See, e.g., FDA’s draft guidance Responding to Unsolicited Requests for Off-Label Information About Prescription 
Drugs and Medical Devices Practices available at 
https://www.fda.gov/downloads/drugs/guidancecomplianceregulatoryinformation/guidances/ucm285145.pdf.  When 
final, this guidance will represent FDA’s current thinking on this topic.

---

<!-- Page 8 -->
Contains Nonbinding Recommendations 
 
 
This guidance does not alter the requirements for when IVD tests are required to submit a new 
premarket notification submission (510(k)) or new Premarket Approval Application (PMA).  
Additionally, this guidance does not affect requirements applicable to clinical laboratories under 
other statutes or regulations currently in place. 
D. Does FDA recommend a specific format for distributing 
LOINC codes? 
No. There is no specific FDA recommended format for distributing LOINC codes. FDA 
acknowledges that LOINC codes may be displayed as simple text in a table format, or in 
structured formats such as Java Script Object Notation (JSON) or Extensible Markup Language 
(XML).  
However, FDA strongly encourages the use of an FDA-recognized consensus standard as the 
mechanism to communicate or disseminate the LOINC codes provided by manufacturers or 
others (for example, the Regenstrief Institute), to laboratories or other end users. The LOINC 
transmission document for IVDs (LIVD) standard is one communication standard explicitly 
developed for this purpose by the IVD Industry Connectivity Consortium.
 
8 
 
14 Standardized 
formats can facilitate a laboratory’s ability to adopt new LOINC codes, incorporate updates or 
changes to existing LOINC codes, and maintain a database of LOINC codes applicable for local 
use. FDA recommends that manufacturers follow developments in this area as standards for 
electronically transmitting recommended LOINC codes are modified or expanded, or as new 
standards emerge, as these may further contribute to greater semantic interoperability within and 
across laboratories.  
                                                          
14 See http://ivdconnectivity.org/livd/
