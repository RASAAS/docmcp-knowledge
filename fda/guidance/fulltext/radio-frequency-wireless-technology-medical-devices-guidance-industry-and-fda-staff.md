# Radio Frequency Wireless Technology in Medical Devices - Guidance for Industry and FDA Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/radio-frequency-wireless-technology-medical-devices-guidance-industry-and-fda-staff](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/radio-frequency-wireless-technology-medical-devices-guidance-industry-and-fda-staff)

**Published:** 2013-08-14

---

<!-- Page 1 -->
Radio Frequency Wireless 
Technology in Medical Devices  
 
 
 
Guidance for Industry and Food 
and Drug Administration Staff 
 
 
Document issued on: August 14, 2013 
 
The draft of this document was issued on January 3, 2007. 
 
 
For questions regarding this document, contact Donald Witters (CDRH) at 301-796-2483 or by 
electronic mail at donald.witters@fda.hhs.gov or CBER’s Office of Communication, Outreach 
and Development (OCOD) at 1-800-835-4709 or 301-827-1800.   
 
 
 
 
 
 
U.S. Department of Health and Human Services 
Food and Drug Administration 
Center for Devices and Radiological Health 
 
Office of Science and Engineering Laboratories 
 
Center for Biologics Evaluation and Research

---

<!-- Page 2 -->
Contains Nonbinding Recommendations 
 
 
 
 
2 
Preface 
 
Public Comment 
 
You may submit comments and suggestions at any time for Agency consideration.  Submit 
electronic comments to http://www.regulations.gov.  Submit written comments to the Division 
of Dockets Management, Food and Drug Administration, 5630 Fishers Lane, 
rm. 1061, (HFA-305), Rockville, MD, 20852.  Identify all comments with the docket number 
listed in the notice of availability that publishes in the Federal Register.  Comments may not be 
acted upon by the Agency until the document is next revised or updated. 
 
Additional Copies 
 
Additional copies are available from the Internet.  You may also send an e-mail request to 
dsmica@fda.hhs.gov to receive an electronic copy of the guidance or send a fax request to 
301-847-8149 to receive a hard copy.  Please use the document number (1618) to identify the 
guidance you are requesting. 
 
Additional copies of this guidance document are also available from the Center for Biologics 
Evaluation and Research (CBER) by written request, Office of Communication, Outreach 
and Development (OCOD) (HFM-40), 1401 Rockville Pike, Suite 200N, Rockville, MD 
20852-1448, by telephone, 1-800-835-4709 or 301-827-1800, by email, ocod@fda.hhs.gov, 
or from the Internet at 
http://www.fda.gov/BiologicsBloodVaccines/GuidanceComplianceRegulatoryInformation/de
fault.htm.

---

<!-- Page 3 -->
Contains Nonbinding Recommendations 
 
 
 
 
3 
 
Table of Contents  
 
1.  Introduction .............................................................................................................................. 4 
2.  Scope.......................................................................................................................................... 5 
3. Considerations for Design, Testing, and Use of Wireless Medical Devices ......................... 5 
A. SELECTION AND PERFORMANCE OF WIRELESS TECHNOLOGY .......................................................................... 7 
B. WIRELESS QUALITY OF SERVICE..................................................................................................................... 9 
C. WIRELESS COEXISTENCE................................................................................................................................. 9 
D. SECURITY OF WIRELESS SIGNALS AND DATA ................................................................................................. 10 
E. EMC OF THE WIRELESS TECHNOLOGY .......................................................................................................... 11 
F.   INFORMATION FOR PROPER SET-UP AND OPERATION .................................................................................... 12 
G.  CONSIDERATIONS FOR MAINTENANCE .......................................................................................................... 13 
4.  Recommendations for Premarket Submissions for Devices that Incorporate RF 
Wireless Technology ................................................................................................................... 14 
A. 
DESCRIPTION OF DEVICE ......................................................................................................................... 15 
B. 
RISK-BASED APPROACH TO VERIFICATION AND VALIDATION ................................................................... 15 
C. 
TEST DATA SUMMARIES .......................................................................................................................... 16 
D. 
LABELING RELATED TO WIRELESS MEDICAL DEVICES .............................................................................. 17 
Appendix A: Glossary for Wireless Medical Devices and Device Systems ............................ 19 
Appendix B: Reference Standards and Information ............................................................... 21

---

<!-- Page 4 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
4 
Radio Frequency Wireless Technology in 
Medical Devices 
 
 
Guidance for Industry and Food and Drug 
Administration Staff 
 
 
This guidance represents the Food and Drug Administration's (FDA's) current thinking 
on this topic.  It does not create or confer any rights for or on any person and does not 
operate to bind FDA or the public.  You can use an alternative approach if the approach 
satisfies the requirements of the applicable statutes and regulations.  If you want to discuss 
an alternative approach, contact the FDA staff responsible for implementing this 
guidance.  If you cannot identify the appropriate FDA staff, call the appropriate number 
listed on the title page of this guidance.  
 
1.  Introduction 
 
FDA has developed this guidance document to assist industry and FDA staff in identifying and 
appropriately addressing specific considerations related to the incorporation and integration of 
radio frequency (RF) wireless technology in medical devices.  There has been rapid growth in 
medical devices that incorporate RF wireless technology due to the expansion of this 
technology.  With the increasing use of RF wireless medical devices, continuing innovation 
and advancements in wireless technology, and an increasingly crowded RF environment, RF 
wireless technology considerations should be taken into account to help provide for the safe 
and effective use of these medical devices.  This guidance highlights and discusses RF wireless 
technology considerations that can have an effect on the safe and effective use of medical 
devices.  These considerations include the selection of wireless technology, quality of service, 
coexistence, security, and electromagnetic compatibility (EMC).  Consideration of these areas 
can help provide reasonable assurance of safety and effectiveness for medical devices that 
incorporate RF wireless technology, and are supplementary to other device-specific guidances 
or guidelines.   
 
FDA's guidance documents, including this guidance, do not establish legally enforceable 
responsibilities.  Instead, guidances describe the Agency's current thinking on a topic and 
should be viewed only as recommendations, unless specific regulatory or statutory 
requirements are cited.  The use of the word should in Agency guidances means that 
something is suggested or recommended, but not required.

---

<!-- Page 5 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
5 
 
2.  Scope 
 
This guidance document addresses considerations that may affect the safe and effective use of 
medical devices that incorporate RF wireless technology (also referred to as wireless medical 
devices), including the selection of wireless technology, quality of service, coexistence, 
security, and EMC.  These issues should be considered for all medical devices that 
incorporate RF wireless technology, such as Wireless Medical Telemetry Service (WMTS); 
Medical Device Radiocommunication Service (MedRadio) (including the former Medical 
Implant Communications Service (MICS)) as well as Medical Micropower Network (MNN) 
and Medical Body Area Network (MBAN); cellular communication chipsets; and RF 
identification (RFID) products.  Such RF wireless technologies operate under a grant of 
certification and/or issuance of a license from the Federal Communications Commission 
(FCC).   
This guidance also provides recommendations for information to be included in FDA 
premarket submissions for medical devices and device systems that incorporate RF wireless 
technology.  Requirements by other agencies are not covered within this document, although 
we note that requirements established by the FCC may be applicable.     
 
The recommendations in this guidance are intended for RF wireless medical devices 
including those that are implanted, worn on the body or other external wireless medical 
devices intended for use in hospitals, homes, clinics, clinical laboratories, and blood 
establishments.  Both wireless induction-based devices and radiated RF technology device 
systems are within the scope of this guidance.  The use of RF energy to generate images of 
the internal structures of the body such as in magnetic resonance imaging systems is outside 
the scope of this guidance document.   
See Appendix A for a glossary of key terms associated with RF wireless technology and 
wireless medical devices that have been adapted from the IEC 60050-161 International 
Electrotechnical Vocabulary (IEV) and other sources. 
 
3. Considerations for Design, Testing, and Use of Wireless 
Medical Devices   
 
Designers and manufacturers of wireless medical devices should consider the ability of their 
devices to function properly in the intended use environments where other RF wireless 
technologies will likely be located.  In the design, testing, and use of wireless medical 
devices, the correct, timely, and secure transmission of medical data and information is 
important for the safe and effective use of both wired and wireless medical devices and 
device systems.  This is especially important for medical devices that perform critical 
functions such as those that are life-supporting or life-sustaining.  For wirelessly enabled

---

<!-- Page 6 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
6 
medical devices, risk management should include considerations for robust RF wireless 
design, testing, deployment, and maintenance throughout the life cycle of the product.1  
Examples of potentially problematic wireless-related hazards and effects include:  
• poorly characterized or poorly utilized wireless systems (e.g., wireless networks);  
• lost, corrupted, or time-delayed transmissions, and degradations in wireless 
transmissions including when caused by competing wireless signals or 
electromagnetic interference (EMI) to the medical device or its wireless 
transmissions;  
• lack or compromise of wireless security; and 
• potential misuse of a wireless medical device because of lack of or inadequate  
instructions for use.  
 
As part of a comprehensive quality system under 21 CFR Part 820, medical device 
manufacturers must manage risks including those associated with RF wireless technology 
that is incorporated into the medical device or device system.  ISO 14971 Second edition 
2007-03-01 Medical devices—Application of risk management to medical devices can be a 
useful tool in risk analysis and risk management.2  Because there are risks associated with RF 
wireless systems, we recommend that you carefully consider which device functions should 
be made wireless and which device functions should employ wired connectivity.   
 
FDA recommends that you address known safety issues involving RF wireless technologies 
early in the device design and development process.  Safety issues might be discovered 
during the design and development process for which risk mitigation measures might be 
necessary to ensure an overall acceptable level of risk.  FDA also recommends that risk 
acceptability criteria be based on information about the device and its intended use, 
including, but not limited to, applicable standards, accepted design practices, and experience 
with similar devices.  For example, FDA recommends that you use reports of EMI-related 
events and other relevant experience when estimating probability of occurrence as part of risk 
analysis.  In addition, where multiple alarms are incorporated into a device or device system 
via wireless links, we recommend that you address priorities for accessing the wireless 
system, and priorities related to the function of the wireless technology itself. 
 
In validating the design of your wireless medical device under 21 CFR 820.30(g), you must 
include risk analysis of RF wireless communications and control functions as part of your 
design validation.  Because it is possible for an electromagnetic disturbance (EMD) to affect 
important medical device functions, mitigation measures for some risks could aid the device 
operator in recognizing a hazardous situation and taking action to prevent harm.  For 
                                                          
1 Risk management is a key component of the quality system, and includes risk analysis, which is part of the 
design control requirements under the quality systems regulation.  21 CFR 820.30(g). 
2 ISO 14971 is on FDA’s list of recognized consensus standards, which is available at 
http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/detail.cfm?standard__identification_no=30268.

---

<!-- Page 7 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
7 
example, design validation might reveal that steps to reestablish an RF wireless connection 
such as re-initialization could compromise safety under some use conditions. 
 
When considering possible adverse outcomes, you should also consider risks to other devices 
and patients whose wireless connections might suffer from, or be the source of, interference.  
In addition, you should consider the potential impact of unintended interference and 
purposeful attempts to disrupt a wireless medical device or an associated device network’s 
functionality. 
 
The following considerations should be appropriately tailored to the selected RF wireless 
technology, and the intended use and use environments for your medical device.  The 
following discussion of these considerations includes information dealing with general and 
design considerations, risk management, verification and validation, and information shared 
with users.  Note that access to information (e.g., user manual, other device labeling) 
concerning these key considerations plays an important role in users being able to properly 
set up, use and maintain medical devices and device systems with wireless technology.     
a. Selection and performance of wireless technology  
 
When selecting the type(s) of wireless technology, it is vital to determine and understand 
the medical device functions that are to be wirelessly enabled and the intended use of the 
medical device.  The medical device functions and intended uses should be appropriately 
matched with the wireless technology’s capabilities and expected performance.  In 
addition, issues relating to the integrity of data transmitted wirelessly (including latency 
and throughput, detection, correction, and corruption control and/or prevention) and 
safety-related requirements of your device should be considered.  Potential risks that can 
affect consistent and timely wireless medical device functions include data corruption or 
loss and interference from simultaneous transmitters in a given location, which can 
increase latency and transmitted signal error rates.  For wireless medical devices and 
device systems, error control processes should be incorporated to assure the integrity of 
data transmitted wirelessly and to manage potential risks related to maximum delay of 
data transfer.  Parameters such as bit error rate, packet loss, and signal-to-noise ratio are 
useful tools in assessing and assuring data integrity and timeliness of data transmission. 
 
In addition, the device performance and specifications related to the wirelessly enabled 
medical device functions should be considered in choosing the appropriate RF wireless 
technology (e.g., WMTS, IEEE 802.11) and RF frequency of operation.  It is important to 
note that many medical devices are authorized to operate as unlicensed devices (under 
Part 15 of the FCC rules3) in the industrial, scientific, and medical (ISM) frequency bands 
(e.g., 2400-2493.5 MHz), and as such, are not entitled to interference protection.  There is 
                                                          
3 For additional information on frequency bands and use, please refer to 
http://www.fcc.gov/encyclopedia/accessing-spectrum and http://www.fcc.gov/encyclopedia/rules-regulations-
title-47.

---

<!-- Page 8 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
8 
a potential for interference in this frequency band because it is already heavily used by 
many other communications and industrial products.  In many cases, RF wireless medical 
devices and transmission streams can incorporate technology (e.g., frequency hopping 
protocols, correction protocols) to minimize effects of interference that may lead to data 
errors or corruption.  Also, to help protect against EMI to other medical devices in the 
vicinity, FDA recommends that wireless medical device manufacturers limit the RF 
output of their devices to the lowest power necessary to reliably accomplish the intended 
functions. 
 
Consideration should be given to any limitations or restrictions for proper operation and 
RF wireless performance (e.g., alarms, back-up functions, alternative modes of operation) 
when the RF wireless link is lost or corrupted.  In addition, worldwide frequency band 
allocation and international compatibility is critical to the operations of RF wireless 
devices, and should be considered in the design and development of wireless medical 
devices.   
 
When choosing a RF wireless frequency band or a commercial wireless radio component, 
FDA recommends that you consider: 
• International availability and band allocation (e.g., applicable International 
Telecommunication Union Radiocommunication Sector (ITU-R)4 
recommendations) for medical devices because medical devices serve patients 
located in multiple geographic locations and patients may change their geographic 
locations. 
• Whether your device needs to have primary or secondary radio service 
classification, which depends upon the wireless frequency band you choose.   
• Incumbent users of the selected and adjacent bands, if any, and how they can 
impact a medical device’s operation. 
• Applicable interference mitigation techniques if you are planning to use a shared 
RF wireless frequency band. 
• For implantable and body-worn medical devices, tissue propagation 
characteristics and specific absorption rate as appropriate. 
 
When considering commercial off-the-shelf RF wireless components or systems that 
conform to industry standards (such as IEEE 802.11 standards), medical device 
manufacturers should take into account that some equipment might not have been 
adequately tested or qualified to address the needs and risks for use in medical devices.  
This is because such equipment may conform to standards that are not written specifically 
for medical devices.  Under the quality system regulation, procedures and controls must 
be established for wireless medical devices and their components, including components 
                                                          
4 http://www.itu.int/en/ITU-R/Pages/default.aspx

---

<!-- Page 9 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
9 
that are purchased and included as part of the device or device system, to ensure that the 
device and its components conform to specified design requirements related to the RF 
wireless considerations noted above.5  
 
b. Wireless Quality of Service  
 
Wireless Quality of Service (QoS) refers to the necessary level of service and 
performance needed for the wireless functions of the medical device.  While the QoS of 
cellular telephone networks might be acceptable for voice communication, it might not be 
sufficient for certain medical functions.  Connections lost without warning, failure to 
establish connections, or degradation of service can have serious consequences, especially 
when the medical device relies heavily on the wireless connection.  Such situations can 
compromise the wireless transmission of high-priority medical device alarms, time-
sensitive continuous physiological waveform data, and real-time control of therapeutic 
medical devices (such as wireless footswitches).   
 
If the wireless medical device will be part of a network, wireless QoS should be carefully 
considered in conjunction with the intended use of the wireless medical device.  The 
following should be assessed:  acceptable latency, acceptable level of probability for loss 
of information within the network, accessibility, and signal priorities of the network. 
 
When the network is chosen or designated, FDA recommends use of a risk management 
approach to deployment, security, and maintenance of the network’s QoS.  Depending on 
the intended use of the device, additional failure modes may need to be considered.  Once 
failure modes and associated risks are identified, we recommend a justification of 
acceptable risk, or testing or other measures to demonstrate appropriate risk mitigation. 
 
c. Wireless coexistence  
 
A key factor affecting a wireless medical device’s performance is the limited amount of 
RF spectrum available, which can result in potential competition among wireless 
technologies for simultaneous access to the same spectrum.  Because conflicts among 
wireless signals can be expected, most wireless communication technologies incorporate 
methods to manage these conflicts and minimize disruptions in the shared wireless 
environment.  The selection of RF wireless operating frequency and modulation should 
take into account other RF wireless technologies and users that might be expected to be in 
the vicinity of the wireless medical device system.  These other wireless systems can pose 
risks that could result in medical device signal loss or delay that should be considered in 
the risk management process.  To address this issue, FDA recommends that you address 
your device’s environmental specifications and needs, including: 
                                                          
5 See, e.g., 21 CFR 820.30(f) (design verification); 21 CFR 820.30(g) (design validation); 21 CFR 820.50 
(purchasing controls); and 21 CFR 820.80 (acceptance activities).

---

<!-- Page 10 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
10 
• Associated sources of EMD expected in specific known use environments, and 
• Co-channel and adjacent channel interference from medical devices and other 
users of the RF band. 
If the RF wireless medical device is expected to be used in proximity to other RF wireless 
in-band (i.e., the same or nearby RF frequency) sources, FDA recommends addressing 
such risks through testing for coexistence of the device wireless system in the presence of 
the number and type of in-band sources expected to be in proximity to the device.  
Depending upon the wireless medical device, this should also include multiple units of 
the subject device operating in the same vicinity, such as when patients are sitting 
adjacent to one another in a waiting room.  Once failure modes and associated risks are 
identified, we recommend a justification of acceptable risk, or testing or other measures 
to demonstrate appropriate risk mitigation.     
d. Security of wireless signals and data   
 
Security of RF wireless technology is a means to prevent unauthorized access to patient 
data or hospital networks and to ensure that information and data received by a device are 
intended for that device.  Authentication and wireless encryption play vital roles in an 
effective wireless security scheme.  While most wireless technologies have encryption 
schemes available, wireless encryption might need to be enabled and assessed for 
adequacy for the medical device’s intended use.  In addition, the security measures should 
be well coordinated among the medical device components, accessories, and system, and 
as needed, with a host wireless network.  Security management should also consider that 
certain wireless technologies incorporate sensing of like technologies and attempt to 
make automatic connections to quickly assemble and use a network (e.g., a discovery 
mode such as that available in Bluetooth™ communications).  For certain types of 
wireless medical devices, this kind of discovery mode could pose safety and effectiveness 
concerns, for example, where automatic connections might allow unintended remote 
control of the medical device.  
 
FDA recommends that wireless medical devices utilize wireless protection (e.g., wireless 
encryption,6 data access controls, secrecy of the “keys” used to secure messages) at a 
level appropriate for the risks presented by the medical device, its environment of use, the 
type and probability of the risks to which it is exposed, and the probable risks to patients 
from a security breach.  FDA recommends that the following factors be considered during 
your device design and development:   
 
• Protection against unauthorized wireless access to device data and control.  This 
should include protocols that maintain the security of the communications while 
                                                          
6 At the time of publication of this guidance, this included WiFi Protected Access (WPA2) for IEEE 802.11 
technology.

---

<!-- Page 11 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
11 
avoiding known shortcomings of existing older protocols (such as Wired 
Equivalent Privacy (WEP)). 
 
• Software protections for control of the wireless data transmission and protection 
against unauthorized access. 
 
Use of the latest up-to-date wireless encryption is encouraged.  Any potential issues 
should be addressed either through appropriate justification of the risks based on your 
device’s intended use or through appropriate design verification and validation.  
For more information on this topic, see FDA’s draft guidance “Content of Premarket 
Submissions for Management of Cybersecurity in Medical Devices.” 
(http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocument
s/ucm356186.htm).  FDA’s draft guidance represents FDA’s proposed approach on this 
topic.   
e. EMC of the wireless technology 
  
FDA recommends that EMC be an integral part of the development, design, testing, and 
performance for RF wireless medical devices.  This should include consideration of 
applicable telecommunications standards and regulations and the potential for device RF 
emissions that might cause EMI with other equipment.  In addition, RF wireless 
technology (by itself and in conjunction with the medical device) would also need to meet 
applicable FCC requirements.  Risk management activities should include using risk 
analysis to identify any potential issues associated with EMC and determining risk 
acceptability criteria based on information about the device and its intended use, 
including foreseeable misuse, sources of environmental EMD (e.g., radio transmitters, 
computer RF wireless equipment), and the potential for RF emissions to affect other 
devices.  
 
EMC testing should include tests focused on the medical device wireless functions and 
technology.  Some voluntary consensus standards such as the FDA-recognized7 
consensus standard IEC 60601-1-2 “Medical Electrical Equipment – Part 1-2: General 
requirements for safety and essential performance – Collateral standard: Electromagnetic 
compatibility – Requirements and tests” contain an exemption from the electromagnetic 
immunity provisions in the “exclusion band” (passband) where the medical device’s RF 
wireless receiver or transmitter operates.  Consequently, such standards do not adequately 
address whether the wireless communications will operate properly in the presence of in-
band EMD (e.g., other RF emissions overlapping the frequency band utilized by the 
medical device wireless signals).  Therefore, the medical device’s wireless 
                                                          
7 For a current list of FDA-recognized consensus standards, see the Recognized Consensus Standards Database 
at http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm.

---

<!-- Page 12 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
12 
communication(s) should be actively transmitting while testing for susceptibility during 
all EMC immunity testing.   
 
EMC considerations are also covered in other standards that might be helpful for medical 
devices that incorporate RF wireless technology.  For example, EMC considerations for 
active implantable medical devices are covered under documents such as the ISO 14708-
1 standard (see Appendix B).   
 
Adequate information for the user is especially important if the device might be used in 
high electric or magnetic field strength environments, and particularly if the device 
cannot be made to function as intended in these environments.  To help ensure safe and 
effective use of your device, FDA recommends that the information for users include the 
following: 
• Conformance to the IEC 60601-1-2 standard or other appropriate standards, and  
• EMC susceptibilities discovered during testing, and mitigations such as 
recommended separation distances from other devices or EMD sources. 
The IEC 60601-1-2 standard specifies that certain information based upon the EMC 
testing be included in “accompanying documents.”  This information includes a summary 
of the test findings and additional EMC-related information such as classification of the 
electrical power supply and use conditions.  
 
f.   Information for proper set-up and operation 
 
To help assure proper set-up, configuration, and performance of the wireless medical 
device, appropriate information should be provided to users.  The following are suggested 
items to consider as part of this information:   
• The specific RF wireless technology type (e.g., IEEE 802.11b), characteristics of 
the modulation, and effective radiated RF power. 
• Specification of each RF frequency or frequency band of transmission and the 
preferred frequency or frequency band (if applicable), and specification of the 
bandwidth of the receiving section of the equipment or system in those bands. 
• Appropriate FCC labeling. 
• A warning that other equipment could interfere with the medical device or 
device system, even if the other equipment complies with CISPR8 emission 
requirements.  
                                                          
8 Comité Internationale Spécial des Perturbations Radioelectrotechnique (International Special Committee on 
Radio Interference).  CISPR electromagnetic emission standards are referenced in the IEC 60601-1-2 standard. 
See Appendix B.

---

<!-- Page 13 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
13 
• Information about the needed quality of service and security for the wireless 
technology. 
• Functions and performance of the wireless data transmissions including data 
throughput, latency, and data integrity. 
• Information about any limitations on the number, output power, or proximity of 
other in-band transmitters used in the vicinity that might adversely impact a 
device’s system operation. 
• Information for the user to understand the RF wireless technology’s capabilities 
and be able to recognize and address issues that might arise.  For devices with 
intended use locations that are in complex RF wireless environments and consist 
of multiple wireless products, this should include assessment and management 
of the RF wireless transmitters and their use in the vicinity including 
transmitters both inside and outside the facility.   
• Information for the user to understand the implications and limitations of using 
RF wireless technology outside the United States, where allocations and 
technical parameters may be different, possibly affecting the functioning of the 
device. 
g.  Considerations for maintenance  
 
Device Life Cycle - FDA recommends that you continue to manage the risks associated 
with the use of wireless technology described above for the entire life cycle of your 
device.  Your procedures for implementing corrective and preventive action must include, 
among other things, analyses for possible trends in nonconformance information and 
complaints, such as reports of failures, which could include erratic or unexpected 
behavior of the medical device.9  Examples of such behavior include reprogramming of 
stimulation devices, commands missed or misinterpreted by operating room controllers, 
unexplained inconsistencies of an infusion pump, and failure to activate alarm signals in 
alarm conditions.   
 
Because electromagnetic emissions and exposure can vary significantly with various 
structures, materials, and RF wireless emitter sources in the vicinity, FDA recommends 
that in analyzing failure trends, you consider factors such as location, user application, 
and repeat component failures.  Potential problems include: 
• Additional events that may have contributed to the EMI or disruption of wireless 
technology resulting in inappropriate or unnecessary diagnostic procedures or 
interventions; 
• Additional equipment used in conjunction with the device; 
• Environmental conditions that might have contributed to the event; and 
                                                          
9 21 CFR 820.100(a).

---

<!-- Page 14 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
14 
• Repeated device failures at the same facility or in other geographic areas. 
If you identify a failure or malfunction of an RF wireless function, you must investigate 
the cause and take action(s) to correct the problem and prevent its recurrence.10 You must 
analyze production and repair records and other sources of quality data to determine the 
cause of the nonconformance.11 Any corrective action and preventative action taken must 
be verified or validated to ensure that such action is effective and does not adversely 
affect the finished device.12 FDA further recommends that you assess any product lines 
that use similar designs or are subject to the same environment to determine whether 
corrective and preventive actions are needed for those products.   
 
Servicing - When servicing electrically powered medical devices, FDA recommends that 
you maintain the integrity of RF wireless functions and design elements intended to 
ensure EMC.  Care should be taken to ensure EMI protection is present and in good 
condition.  Such EMI protection can include components that may be removed during 
service such as shields, metal covers, ferrite beads, bonds, screws, ground wires and 
straps.  In addition, FDA recommends that you do not paint metal surfaces that are 
intentionally left bare for RF shielding continuity.  To reduce EMI susceptibility as 
electronic equipment ages, we recommend that you clean connector contacts that might 
have oxidized because oxidized contacts can act as semiconductors. 
 
4.  Recommendations for Premarket Submissions13 for 
Devices that Incorporate RF Wireless Technology   
 
When preparing a premarket submission for a device that incorporates RF wireless 
technology, FDA recommends that you include the following information, as appropriate, for 
your specific medical device. 
                                                          
10 21 CFR 820.100(a). 
11 21 CFR 820.100(a). 
12 21 CFR 820.100(a). 
13 This guidance document applies to the following premarket submissions for devices:  premarket notifications 
(510(k)), de novo petitions, premarket approval applications (PMA), product development protocols (PDP), 
humanitarian device exemption (HDE) applications, and Biologics License Applications (BLA).  Manufacturers 
may also consider applying the recommendations provided in this guidance, as appropriate, to investigational 
device exemption (IDE) applications and investigational new drug (IND) submissions to CBER related to BLA 
devices.

---

<!-- Page 15 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
15 
a. Description of device  
In order to facilitate the review of the submission, the device description for a wireless 
medical device should include the following information specific to the wireless 
technology and functions:   
 
• A description of the wireless technology and functions, and the intended use of the 
medical device and intended use environment.  This should include the form and 
specific type of wireless technology that is incorporated into the device (e.g., IEEE 
802.11b, IEEE 802.15 BluetoothTM), RF frequencies and maximum output powers, 
range, and where and how the wireless technology is to be used.    
 
• A description of how the design of the device’s wireless function(s) assures timely, 
reliable, accurate, and secure data and wireless information transfer.  This includes the 
wireless QoS needs and security measures. 
 
• If wireless technology is used for transmission, reception, or process involving alarm 
signals, a description of the alarm signal, its priority, and how the RF wireless-related 
risks are managed and, if appropriate, mitigated.     
 
• Identify whether other wireless products or devices are able to make a wireless 
connection to the device.  If so, summarize the products or devices and their function 
and how the subject medical device functions are protected from adverse effects of 
such connections to the other products or devices. 
 
b. Risk-based approach to verification and validation 
 
1. Wireless Quality of Service – The submission should include information to 
describe the wireless QoS needed for the intended use and use environment of the 
medical device.  This includes addressing any risks and potential performance issues 
that might be associated with data rates, latency, and communications reliability as 
described in Section 3-b.    
 
2. Wireless coexistence – Any risks and potential performance issues that might be 
associated with wireless coexistence in a shared wireless environment should be 
addressed via testing and analysis with other wireless products or devices that can be 
expected to be located in the wireless medical device’s intended use environment.  See 
Section 3-c.  The information addressing coexistence should include the following:   
 
• A summary of the coexistence testing, set-up, findings, and analysis.

---

<!-- Page 16 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
16 
• The wireless products (interferers) that were used in the coexistence testing, 
and their wireless RF frequencies, maximum output powers, and separation 
distances from the device.   
 
• The specific pass/fail criteria for this testing.   
 
• How the device and wireless functions were monitored during the testing and 
determined to meet the pass/fail criteria.  
 
• If it is reasonable to expect multiple units of the subject wireless medical 
device to be used in the same vicinity, the information should also address how 
the association and security between devices is established and maintained to 
prevent cross-talk among the devices. 
 
3. Security of wireless signals and data - The submission should identify any risks, 
potential performance issues, and, if appropriate, risk mitigation measures that might 
be associated with wireless security.  The information should include the specific 
measures needed to protect against unauthorized wireless access to the medical device 
control or data and to ensure that information and data received by a device are 
intended for that device.  For wireless technology with a discovery mode or similar 
active connection mode, specific information should be included addressing the 
discovery mode and how outside users can be prevented from sensing or connecting to 
the medical device.  See Section 3-d. 
 
4. EMC of the wireless technology – Information should be provided about how 
EMC has been addressed for the device and all wireless functions.  However, as 
mentioned in section 3-e., the widely used IEC 60601-1-2 consensus standard does not 
at present adequately address wireless technology EMC.  Therefore, testing, analysis, 
and appropriate mitigation might be necessary to adequately address any risks or 
potential performance issues that might be associated with the EMC of the wireless 
medical device.  If modifications to the medical device were made to pass any EMC 
testing, please include a description of, and justification for, the modifications.   
c. Test data summaries  
 
FDA recommends that the final RF wireless and EMC testing14 and results be 
summarized in your premarket submission, which should contain the following 
information: 
 
• Description of the tests performed (e.g., RF wireless performance, EMC 
immunity and emissions, test levels or limits) and the protocol used; 
                                                          
14 By final testing we refer to testing performed on the final integrated product.

---

<!-- Page 17 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
17 
• Reference to appropriate medical device, RF wireless technology, or EMC 
standards for the tests; 
• Explanations for any deviations from the selected standards; 
• Mode(s) of device operation during testing, with an explanation of the 
significance of these modes; 
• Specific pass/fail criteria for the testing such as specific device-related 
acceptability criteria for each device mode or function tested.  These criteria 
should include the following: 
o Specific device functions that should not degrade (such as CPU failure); 
o Device functions that may degrade (such as display fluctuation); and 
o Device recovery from degradation (such as after removal of the 
electrostatic discharge (ESD)). 
• If modifications were made to the medical device in order to pass testing, a 
statement that all modifications will be incorporated into all final production 
units. 
 
d. Labeling related to wireless medical devices 
 
To facilitate the safe and effective use of the wireless medical device, the proposed 
labeling should include risk mitigation measures that address RF wireless issues and any 
precautions users should take.  You should be aware that while labeling statements, such 
as warnings, may be helpful, they are not a substitute for risk mitigation measures or 
other design control activities, and are typically not adequate to prevent adverse events.   
 
FDA recommends that the following information be included in the device labeling: 
 
• A summary of the medical device wireless functions and specific wireless 
technology incorporated into the medical device or device system including 
equipment or system specifications (e.g., the standard IEEE 802.11 b/g, IEEE 
802.15.4 BluetoothTM class II);  
 
• A summary of the operating characteristics of the wireless technology, effective 
RF radiated power output and operating range, modulation, and bandwidth of 
receiving section; 
 
• A brief description of the wireless QoS needed for safe and effective operation;  
 
• A brief description of the recommended wireless security measures such as the 
WPA2 wireless encryption for IEEE 802.11 technology;

---

<!-- Page 18 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
18 
 
• Information addressing wireless issues and what to do if problems occur;   
 
• Information about any wireless coexistence issues and mitigations. This can 
include precautions for proximity to other wireless products, and specific 
recommendations for separation distances from such products; 
 
• Appropriate EMC and telecommunications standards compliance and test 
results summary; 
 
• Appropriate RF wireless communications information such as those required by 
FCC rules; and 
 
• Warnings about possible effects from RF sources in the vicinity of the device 
(e.g., electromagnetic security systems, cellular telephones, RFID or other in-
band transmitters). 
 
In addition, FDA recommends that your labeling also include all of the information as 
outlined in the appropriate reference standards (e.g., IEC 60601-1-2).  You should also 
consider any other appropriate FDA guidances or special controls guidelines applicable to 
your device for additional labeling information.

---

<!-- Page 19 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
19 
Appendix A: Glossary for Wireless Medical Devices and 
Device Systems 
 
The following definitions were adapted from IEC 60050-161 International Electrotechnical 
Vocabulary (IEV), IEEE Standard 802.15.2™-2003, the IEEE Standard 11073-00101™ -
2008, and other sources.15  
Data integrity — Assurance that transmitted files are not deleted, modified, duplicated, or 
forged without detection. 
Electromagnetic compatibility (EMC) — the ability of a device to function (a) properly in 
its intended electromagnetic environment, and (b) without introducing excessive 
electromagnetic disturbances that might interfere with other devices. 
Electromagnetic disturbance (EMD) — any electromagnetic phenomenon that might 
degrade the performance of an equipment, such as medical devices or any electronic 
equipment.  Examples include power line voltage dips and interruptions, electrical fast 
transients (EFTs), electromagnetic fields (radio frequency radiated emissions), electrostatic 
discharges, and conducted emissions. 
Electromagnetic interference (EMI) — degradation of the performance of a piece of 
equipment, transmission channel, or system (such as medical devices) caused by an 
electromagnetic disturbance.  Note: Disturbance and interference are cause and effect, 
respectively. 
Electrostatic discharge (ESD) — the rapid transfer of an electrostatic charge between 
bodies of different electrostatic potential, either in proximity in air (air discharge) or through 
direct contact (contact discharge). 
Emissions — electromagnetic energy emanating from a device generally falling into two 
categories: conducted and radiated.  Both categories of emission can occur simultaneously, 
depending on the configuration of the device.  
Conducted emissions — electromagnetic energy emanating from a product through a 
conductor by means of resistance, inductance, or capacitance.  Conductors include AC 
power cords, metallic enclosures of a subsystem, or cables that interconnect subsystems 
or the patient to the product.  Conducted emissions include power line harmonics, surges, 
and radio frequency energy, especially in the frequency range 150 kHz to 80 MHz. 
Radiated emissions — electromagnetic energy emanating from a device and propagating 
through space or a medium (which can affect the distance and direction of propagation).  
Radiated emissions include both intentional emissions such as radio transmissions 
                                                          
15 Sources include:  Federal Standard 1037C Telecommunications: Glossary of Telecommunications Terms.

---

<!-- Page 20 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
20 
carrying information and unintentional emissions associated with electrically powered 
equipment such as motors, power supplies, and computer components. 
Immunity — the ability of an electrical or electronic product to operate as intended without 
performance degradation in the presence of an electromagnetic disturbance. 
Latency — the time it takes for a unit of information to cross a wireless link or network 
connection from sender to receiver, which is also known as transfer delay. 
Quality of service (QoS) — the necessary level of performance in a data communications 
system or other service, typically encompassing multiple performance parameters, such as 
reliability of data transmission, transfer rate, error rate, and mechanisms and priority levels 
for time-critical signals.   
Radio frequency (RF) — a frequency in the portion of the electromagnetic spectrum that is 
between the audio-frequency and the infrared portions, and is useful for radio transmission. 
Commonly used radio frequencies range from 9 kHz to 100 GHz. 
Radio frequency interference (RFI) — one type of EMI resulting from radiated emissions 
at one or more radio frequencies, which causes degradation of the reception of a wanted 
signal by a radio-frequency electromagnetic disturbance.  
Radio frequency (RF) wireless medical device — a medical device that includes at least 
one function that is implemented using RF wireless communications; examples of functions 
that might be implemented wirelessly include data transfer, device control, programming, 
power transmission, remote sensing and monitoring, and identification.  
Security — a collection of services, policies, mechanisms, and controls that provides 
information confidentiality, integrity, and availability by restricting unauthorized parties from 
accessing, manipulating, or leveraging particular system resources.  Some security services 
might include data encryption, data integrity-checking, user and device authentication, and 
non-repudiation. 
Specific absorption rate (SAR) — a measure of the rate at which energy is absorbed by the 
body when exposed to an RF electromagnetic field. It is defined as the power absorbed per 
mass of tissue and has units of watts per kilogram. SAR is usually averaged either over the 
entire body, or over a small sample volume (typically 1 g or 10 g of tissue). 
Susceptibility — the potential for equipment (including medical devices) to respond to an 
electromagnetic disturbance. The inability of a device, equipment or system to perform 
without degradation in the presence of an electromagnetic disturbance. Note: Susceptibility is 
a lack of immunity. 
Wireless coexistence — the ability of one wireless system to perform a task in a given 
shared environment where other systems (in that environment) have an ability to perform 
their tasks and might or might not be using the same set of rules.

---

<!-- Page 21 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
21 
Appendix B: Reference Standards and Information    
 
FDA recommends that you refer to the FDA Recognized Consensus Standards Database at 
http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm, and type 
“electromagnetic compatibility” in the title search for EMC standards that FDA recognizes 
for use in premarket submissions.  For information on recognized consensus standards, see 
the guidance document “Frequently Asked Questions on Recognition of Consensus 
Standards,” 
http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocuments/uc
m074973.htm.   
The list below illustrates national and international consensus standards and other standards, 
and documents and information related to EMC, medical device EMC, and 
telecommunications.  FDA recognizes some of these standards for use in regulatory 
submissions.  However, this list serves as a reference only and is not intended to substitute 
for or represent specific suggestions or recommendations.  We recommend that you refer to 
FDA guidances or special controls guidelines applicable to your specific device.  
 
Association for the Advancement of Medical Instrumentation (AAMI)  
AAMI TIR No. 18-2010, Guidance on electromagnetic compatibility of medical devices in 
healthcare facilities   
ANSI/AAMI PC69:2007, Active implantable medical devices—Electromagnetic 
compatibility—EMC test protocols for implantable cardiac pacemakers and implantable 
cardioverter defibrillators 
ANSI/AAMI/IEC 60601-1-2:2007/ (R) 2012, Medical Electrical Equipment—Part 1–2: 
General requirements for basic safety and essential performance – Collateral standard: 
Electromagnetic compatibility – Requirements and tests.  This is the U.S. version of the IEC 
60601-1-2 standard (see IEC below) 
 
American National Standards Institute (ANSI) Accredited Standards Committee C63 
(ASC C63) 
ANSI C63.4:2009, American National Standard for Methods of Measurement of Radio-Noise 
Emissions from Low-Voltage Electrical and Electronic Equipment in the Range of 9 kHz to 
40 GHz 
ANSI C63.10:2009, American National Standard for Methods for Testing Unlicensed 
Wireless Devices

---

<!-- Page 22 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
22 
ANSI C63.18:1997, American National Standard Recommended Practice for an On-Site, Ad 
Hoc Test Method for Estimating Radiated Electromagnetic Immunity of Medical Devices to 
Specific Radio-Frequency Transmitters  
ANSI C63.19:2007, American National Standard Methods of Measurement of Compatibility 
between Wireless Communications Devices and Hearing Aids 
 
Electrostatic Discharge Association (ESD Association) 
ANSI/ESD S20.20-2007, ESD Association Standard for the Development of an Electrostatic 
Discharge Control Program for Protection of Electrical and Electronic Parts, Assemblies and 
Equipment (Excluding Electrically Initiated Explosive Devices) 
 
Federal Communications Commission16 
Code of Federal Regulations, Title 47 – Telecommunications, Chapter I - Federal 
Communications Commission, Subchapter A – General 
• Part 2 – Frequency Allocations and Radio Treaty Matters; General Rules and 
Regulations  
• Part 15 – Radiofrequency Devices 
• Part 18 – Industrial, Scientific, and Medical Equipment 
Subchapter D - Safety and Special Radio Services 
• Part 95 – Personal Radio Services 
 
International Electrotechnical Commission (IEC) 
The IEC 60601 family specifies safety standards for medical electrical equipment.  EMC is 
addressed in IEC 60601-1-2, and IEC 60601-2-X provides standards for particular types of 
medical electrical equipment.  
IEC 60601-1-2:2007, Medical Electrical Equipment – Part 1-2: General requirements for 
basic safety and essential performance– Collateral standard: Electromagnetic compatibility – 
Requirements and tests.  This is a collateral standard to the third edition of IEC 60601-1.  The 
third edition of IEC 60601-1-2 was published in 2007 and contains essentially the same 
                                                          
16 For further information about these or other FCC requirements, please refer to 
http://www.fcc.gov/encyclopedia/rules-regulations-title-47 .

---

<!-- Page 23 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
23 
information that was in the second edition IEC 60601-1-2:2001 and Amendment 1:2004, 
reformatted according to the third edition of the IEC 60601-1 standard.  Emissions and 
immunity requirements in the third edition IEC 60601-1 are specified under Clause 17.   
IEC 60601-2-X standards are for particular types of medical electrical equipment.  
Requirements of IEC 60601-2-X standards supersede those of IEC 60601-1 and IEC 60601-
1-2.  Some IEC 60601-2-X standards specify higher immunity test levels or special test 
setups for EMC.  Some might not have been amended yet to reference the third (2007) 
edition of IEC 60601-1-2 and might still reference an earlier edition.  Modifications to IEC 
60601-1 for EMC are specified in Clause 17 in the IEC 60601-1-2:2007 edition and Clause 
36 in earlier editions.  (NOTE: Subclause numbers for similar provisions in IEC 60601-1-
2:2007 are different from those in earlier editions.) 
IEC 61326-1:2005, Electrical equipment for measurement, control and laboratory use – EMC 
requirements - Part 1: General requirements.  Edition 2.0 was published in 2012.  
IEC 61326-2-1:2005, Electrical equipment for measurement, control and laboratory use - 
EMC requirements - Part 2-1: Particular requirements - Test configurations, operational 
conditions and performance criteria for sensitive test and measurement equipment for EMC 
unprotected applications. Edition 2.0 was published in 2012. 
IEC 61326-2-6:2005, Electrical equipment for measurement, control and laboratory use - 
EMC requirements - Part 2-6: Particular requirements - In vitro diagnostic (IVD) medical 
equipment. Edition 2.0 was published in 2012. 
IEC 60050-161:1990, International Electrotechnical Vocabulary – Chapter 161: 
Electromagnetic compatibility. Amendment 2 was published in 1998.  IEV online: 
http://www.electropedia.org/ 
IEC TR 80001-2-3: 2012, Application of Risk Management for IT-Networks Incorporating 
Medical Devices – Part 2-3: Guidance for wireless networks 
 
Institute of Electrical and Electronic Engineers (IEEE) 
P11073-00101™-2008 - Guide for Health Informatics–Point-of-Care Medical Device 
Communication–Guidelines for the Use of RF Wireless Technology. There are several 
standards under the IEEE 11073 family that address health informatics point-of-care medical 
device communications and provide useful information. 
IEEE Std 802.15.2™-2003 IEEE Recommended Practice for Information Technology— 
Telecommunications and Information Exchange between Systems— Local and Metropolitan 
Area Networks— Specific Requirements Part 15.2: Coexistence of Wireless Personal Area 
Networks with Other Wireless Devices Operating in Unlicensed Frequency Bands.

---

<!-- Page 24 -->
Contains Nonbinding Recommendations 
 
 
 
 
 
 
 
24 
 
International Organization for Standardization (ISO)  
Most ISO standards for medical electrical equipment reference clauses in IEC 60601-1, 
including Clause 17 (previously Clause 36) and IEC 60601-1-2.  
ISO/TR 16056-1, Health informatics – Interoperability of telehealth systems and networks — 
Part 1: Introduction and definitions  
ISO/TR 16056-2, Health informatics – Interoperability of telehealth systems and networks — 
Part 2: Real-time systems 
ISO/TR 18307, Health informatics – Interoperability and compatibility in messaging and 
communication standards – Key characteristics 
ISO 14708-1, Implants for surgery – Active implantable medical devices – Part 1: General 
requirements for safety, marking, and for information to be provided by the manufacturer 
ISO 14708-2, Implants for surgery — Active implantable medical devices — Part 2: Cardiac 
pacemakers 
ISO 14708-3, Implants for surgery - Active implantable medical devices - Part 3: Implantable 
neurostimulators. 
ISO 14708-4, Implants for surgery — Active implantable medical devices — Part 4: 
Implantable infusion pumps 
ISO 14971 Second edition 2007-03-01 Medical devices — Application of risk management 
to medical devices 
ISO 14117, Active implantable medical devices – Electromagnetic compatibility – EMC test 
protocols for implantable cardiac pacemakers, implantable cardioverter defibrillators, and 
cardiac resynchronization devices. 
ISO technical report TR 21730, Health Informatics – Use of mobile wireless communications 
and computing technology in healthcare facilities – Recommendations for the management of 
unintentional electromagnetic interference with medical devices (ISO/TR 21730: 2007(E)).   
 
RTCA, Inc. 
RTCA/DO-160G, Environmental Conditions and Test Procedures for Airborne Equipment
