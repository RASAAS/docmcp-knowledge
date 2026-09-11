# Technical Performance Assessment of Quantitative Imaging in Radiological Device Premarket Submissions: Guidance for Industry and Food and Drug Administration Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/technical-performance-assessment-quantitative-imaging-radiological-device-premarket-submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/technical-performance-assessment-quantitative-imaging-radiological-device-premarket-submissions)

**Published:** 2022-06-16

---

<!-- Page 1 -->
Contains Nonbinding Recommendations
1
Technical Performance Assessment 
of Quantitative Imaging in 
Radiological Device Premarket 
Submissions
Guidance for Industry and Food and 
Drug Administration Staff
Document issued on: June 16, 2022.
The draft of this document was issued on April 19, 2019.
For questions about this document, contact RadHealth@fda.hhs.gov.
U.S. Department of Health and Human Services
Food and Drug Administration
Center for Devices and Radiological Health

---

<!-- Page 2 -->
Contains Nonbinding Recommendations
2
Preface
Public Comment
You may submit electronic comments and suggestions at any time for Agency consideration to 
https://www.regulations.gov. Submit written comments to the Dockets Management Staff, Food 
and Drug Administration, 5630 Fishers Lane, Room 1061, (HFA-305), Rockville, MD 20852. 
Identify all comments with the docket number FDA-2019-D-1470. Comments may not be acted 
upon by the Agency until the document is next revised or updated.
Additional Copies
Additional copies are available from the Internet.  You may also send an e-mail request to CDRH-
Guidance@fda.hhs.gov to receive a copy of the guidance.  Please include the document number 
18017 and complete title of the guidance in the request.

---

<!-- Page 3 -->
Contains Nonbinding Recommendations
3
Table of Contents
I. 
Introduction ............................................................................................................................. 4
II. 
Background ............................................................................................................................. 5
III. Scope ....................................................................................................................................... 5
IV. Definitions............................................................................................................................... 6
V. 
Potential Sources of Measurement Error ................................................................................ 9
VI. Information to Include in a Premarket Submission .............................................................. 10
Function Description......................................................................................................... 10
Technical Performance Assessment ................................................................................. 11
Labeling (User Instructions) ............................................................................................. 13
VII. Examples ............................................................................................................................... 14
Example 1 – Manual Quantitative Imaging Function ............................................................... 14
Example 2 – Semi-automated Quantitative Imaging Function ................................................. 15
Example 3 –Fully Automated Quantitative Imaging Function ................................................. 17

---

<!-- Page 4 -->
Contains Nonbinding Recommendations
4
Technical Performance Assessment of 
Quantitative Imaging in Radiological 
Device Premarket Submissions
Guidance for Industry and Food and 
Drug Administration Staff
This guidance represents the current thinking of the Food and Drug Administration (FDA or 
Agency) on this topic.  It does not establish any rights for any person and is not binding on FDA 
or the public.  You can use an alternative approach if it satisfies the requirements of the applicable 
statutes and regulations.  To discuss an alternative approach, contact the FDA staff or Office 
responsible for this guidance as listed on the title page. 
I. Introduction
The Food and Drug Administration (FDA) is issuing this guidance to provide recommendations for 
manufacturers about the information that should be included in premarket submissions for 
radiological devices that include quantitative imaging functions.  This guidance document is broadly 
applicable to a variety of premarket submission types (i.e., premarket approval (PMA) applications, 
humanitarian device exemption (HDE) applications, premarket notification (510(k)) submissions, 
investigational device exemption (IDE) applications and De Novo requests) for these devices and 
should be used in conjunction with any existing device- and submission-specific guidance 
documents.  Overall premarket submission requirements and recommended information to provide 
can differ depending on the submission type. Additional information on each submission type can be 
found on the FDA’s Premarket Submissions webpage.1 Questions regarding the regulatory status or 
requirements should be addressed to the appropriate review division through the Q-Submission 
process; see “Requests for Feedback and Meetings for Medical Device Submissions: The Q-
Submission Program - Guidance for Industry and Food and Drug Administration Staff.”2
This guidance document clarifies that, in general, manufacturers preparing premarket submissions for 
radiological devices that include quantitative imaging functions should provide performance 
specifications for the quantitative imaging functions, supporting performance data to demonstrate 
that the quantitative imaging functions meet those performance specifications, and sufficient 
1 Available at https://www.fda.gov/medical-devices/how-study-and-market-your-device/premarket-submissions.
2 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-
meetings-medical-device-submissions-q-submission-program.

---

<!-- Page 5 -->
Contains Nonbinding Recommendations
5
information for the end user to obtain, understand, and interpret the values provided by the 
quantitative imaging functions.  
The contents of this document do not have the force and effect of law and are not meant to bind the 
public in any way, unless specifically incorporated into a contract. This document is intended only to 
provide clarity to the public regarding existing requirements under the law. FDA guidance 
documents, including this guidance, should be viewed only as recommendations, unless specific 
regulatory or statutory requirements are cited. The use of the word should in Agency guidance means 
that something is suggested or recommended, but not required.
  
II. Background
Medical imaging is used routinely in hospitals and clinics to assist with the diagnosis and 
management of patients with a variety of diseases and conditions.  Medical images provide visual 
representations of the functional physiology and internal structures of the body that may assist 
medical professionals in making diagnostic and treatment decisions.  
Most medical images are acquired with the intention of qualitative interpretation by a trained 
physician to identify the presence or absence of a structure or feature.  For example, a radiologist 
may read an x-ray to identify or rule out a fracture or a head computed tomography (CT) to look for 
hemorrhage.  
Quantitative imaging extracts additional information from medical images or medical imaging data in 
the form of numerical values.  Examples of quantitative imaging values include standard uptake 
values (SUVs) in nuclear medicine, volumetry measurements in tomographic imaging (magnetic 
resonance (MR) and CT), and relaxometry (T1 or T2 values) in MR.  Quantitative imaging values are 
usually subject to both systematic error and random variation.  Thus, a quantitative imaging value can 
often differ from the true value of the measurand (the quantity being estimated).  Systematic errors 
and random variation in quantitative imaging impact the reported outputs and may affect clinical 
decision making. 
The utility of any quantitative imaging value is greatest when the performance of the quantitative 
imaging function is well-characterized and users have sufficient information to understand and 
interpret the quantitative values being reported.  Quantitative imaging functions have a broad range 
of intended uses, making it difficult to define universal criteria for achieving a “well-characterized” 
quantitative imaging function and “sufficient user information” for all types of quantitative imaging 
functions and for all intended uses.  However, a general framework for developing and 
communicating appropriate technical performance information can be defined. 
III. Scope
This guidance document is applicable to all devices that generate quantitative imaging values across 
a wide range of radiological imaging modalities, intended uses, levels of automation, and complexity 
of algorithms.  This guidance document provides FDA’s recommendations on the information,

---

<!-- Page 6 -->
Contains Nonbinding Recommendations
6
technical performance assessment, and user information that should be included in a premarket 
submission for radiological devices that include quantitative imaging functions.  
The rigor of the technical performance assessment and the breadth/specificity of the information 
provided to the user in the labeling should ensure that the intended use of the device is adequately 
supported and considers the benefit-risk profile of the information provided by the quantitative 
imaging function.  Depending on the intended use of a device, assessment of technical performance 
alone may not be sufficient and clinical validation may be necessary.  This document is not intended 
to provide comprehensive guidance on the types of scientific evidence needed to assess the technical 
performance for specific intended uses of the device, or the benefit-risk assessment conducted as part 
of the review of the premarket submission.3
The clinical validation of any quantitative imaging values is also outside the scope of this guidance 
document.  For example, a function that reports a percent stenosis value from the ratio of two vessel 
diameters would be considered a quantitative imaging function and the technical performance 
assessment of that quantitative imaging function would be within the scope of this document.  
However, linking the probability of a cardiac event to the percentage of vessel stenosis would be 
outside the scope of this guidance document.  
IV. Definitions 
To ensure consistency throughout this document and in premarket submissions of devices that 
include quantitative imaging functions, FDA encourages use of the following terminology when 
describing quantitative imaging functions.  The terminology below is derived from Radiological 
Society of North America’s (RSNA) Quantitative Imaging Biomarker Alliance (QIBA),4,5 the 
Biomarkers, EndpointS and other Tools (BEST) glossary,6 the International Vocabulary of 
3 For more information on benefit-risk determinations, see the following guidance documents:
“Benefit-Risk Factors to Consider When Determining Substantial Equivalence in Premarket Notifications (510(k)) with 
Different Technological Characteristics,” available at https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/benefit-risk-factors-consider-when-determining-substantial-equivalence-premarket-notifications-510k;
“Factors to Consider When Making Benefit-Risk Determinations for Medical Device Investigational Device 
Exemptions,” available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/factors-consider-
when-making-benefit-risk-determinations-medical-device-investigational-device; 
“Factors to Consider When Making Benefit-Risk Determinations in Medical Device Premarket Approval and De Novo 
Classifications,” available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/factors-
consider-when-making-benefit-risk-determinations-medical-device-premarket-approval-and-de; and 
“Factors to Consider Regarding Benefit-Risk in Medical Device Product Availability, Compliance, and Enforcement 
Decisions,” available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/factors-consider-
regarding-benefit-risk-medical-device-product-availability-compliance-and. 
4 Kessler, L.G., et al., “The emerging science of quantitative imaging biomarkers terminology and definitions for 
scientific studies and regulatory submissions,” Stat Meth Med Res 24(1) 9-26 (2015).
5 Sullivan, D.C., et al., “Metrology standards for quantitative imaging biomarkers,” Radiology 277(3) 813-825 (2015).
6 BEST (Biomarkers, EndpointS, and other Tools Resource), available at 
https://www.ncbi.nlm.nih.gov/books/NBK326791/ (last accessed on June 13, 2022).

---

<!-- Page 7 -->
Contains Nonbinding Recommendations
7
Metrology,7 and the International Medical Device Regulators Forum (IMDRF) “Software as a 
Medical Device (SaMD): Clinical Evaluation” document.8
Accuracy: The closeness of agreement between a test result and the accepted reference value.
Bias: The systematic difference between a quantitative imaging value made on the same object and 
its true value.  If the true value is unknown, then bias cannot be evaluated.  However, systematic 
difference between a quantitative imaging value and an accepted value of the measurand (see 
reference value) may be evaluated.  Percent bias: Bias divided by the true value in percent. 
Characterization: Description and documentation of the performance of the quantitative imaging 
function.  That is, what values does the function consistently produce under defined conditions?
Clinical Validation: The assessment and analysis of clinical data pertaining to a medical device to 
verify the clinical safety, performance, and effectiveness of the device when used as intended by the 
manufacturer. 
Note: Clinical validation is outside the scope of this guidance document. See Software as a Medical 
Device (SaMD): Clinical Evaluation9 document for FDA’s current thinking on clinical validation.
Limits of quantitation: The lower and upper values of the measurand that can be reliably detected 
under specified experimental conditions and quantitatively determined with stated precision and 
stated bias.
Linearity: The ability to provide measured quantity values that are directly proportional to the value 
of the measurand. 
Measurand: The quantity intended to be measured. 
Measurement: The process of experimentally obtaining one or more quantity values that can 
reasonably be attributed to a quantity.
Phantom:  A specially designed physical or digital object that is scanned, imaged, or synthesized to 
evaluate, analyze, or otherwise assess the performance of imaging devices.  Examples include 
physical objects such as traceable materials, mechanical hearts, and anthropomorphic chest phantoms 
or digital phantoms such as synthetic images based on in silico modeling. 
Precision: The closeness of agreement between measured quantity values obtained by replicate 
measurements under specified conditions. 
7 Joint Committee for Guides in Metrology, “International Vocabulary of Metrology – Basic and General Concepts and 
Associated Terms (VIM 3rd edition),” JCGM 200:2012, available at 
https://www.bipm.org/en/publications/guides/vim.html (last accessed on April 13, 2022).
8 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/software-medical-device-
samd-clinical-evaluation. 
9 Ibid.

---

<!-- Page 8 -->
Contains Nonbinding Recommendations
8
Quantitative Imaging: Measurement of quantities from medical images or medical imaging data. 
Quantitative Imaging Function: A medical device, or a component or part of a medical device, that 
produces quantitative imaging values.  
Quantitative Imaging Value: An objective, physical characteristic derived from a medical image or 
medical imaging data measured on a ratio or interval scale.  Types of quantitative imaging values 
include:
Ratio variable: A variable such that the difference between any two values is meaningful and 
any two values have a meaningful ratio, making the operations of multiplication and division 
meaningful.  A ratio variable possesses a meaningful (unique and non-arbitrary) zero value 
(e.g., tumor volume). 
Interval variable: A variable for which the difference between two values is meaningful, but 
the ratio of two values is not (e.g., CT Hounsfield units).
Note: Ordinal and nominal variables are not considered quantitative imaging values:
Ordinal variable: A magnitude is assigned and ordering of values has meaning, but 
differences and ratios of values have no meaning (e.g., BIRADS score). 
Nominal variable: Numbers arbitrarily assigned to categories.  Neither ordering nor arithmetic 
operations on the numbers have real meaning (e.g., a classifier).
Quantity: A property that has a magnitude which can be expressed as a number and a reference and 
is related to a physical property.  The reference can be a measurement unit, a measurement 
procedure, a reference material, or a combination. 
Reference material: Material with known properties that can be used as a reference to confirm 
measurement of specific properties.  
Reference value: The true or accepted value of the measurand.  A reference value can be a 
theoretical or established value based on scientific principles, an assigned value based on 
experimental work of some national or international organization, or a consensus value based on 
collaborative experimental work. 
Repeatability: Measurement precision under the same set of conditions over a short period of time.
Reproducibility: Measurement precision under different conditions (e.g., site, device, operator).
Sensitivity Analysis: A systematic analysis of how independent variable(s) impact a dependent 
variable under a given set of conditions/assumptions. 
Technical Performance Assessment: Establishing that the technical performance specifications of 
the quantitative imaging function correspond to the claims and uncertainty associated with the

---

<!-- Page 9 -->
Contains Nonbinding Recommendations
9
quantitative imaging function.  The technical performance assessment of a quantitative imaging 
device is based on a specified technical protocol, which may include media collection and 
processing.  
Note:  The concept of analytical validation (that is, accuracy, reliability, and precision) as described 
in the document entitled “Software as a Medical Device (SaMD): Clinical Evaluation Guidance”10
can be used in the technical performance assessment of an imaging device.
Uncertainty: A nonnegative parameter characterizing the dispersion of the quantity values being 
attributed to a measurand. 
Verification: Objective evidence that defined performance specifications have been met. 
V. Potential Sources of Measurement Error
Quantitative imaging values derived from medical images or medical imaging data may be affected 
by multiple sources of error.  Quantitative imaging values are usually subject to both systematic error 
and random variation.  Thus, a quantitative imaging value can, and usually does, differ from the true 
value of the measurand.  Errors may come from the acquisition of the medical images, patient 
characteristics, and the image processing algorithm.  An understanding of the sources of error, 
especially those with the largest impact on the measurand and the quantitative imaging values 
produced by your quantitative imaging function, is important for characterizing the performance of 
your quantitative imaging function.  A sensitivity analysis is one technique that may be used to 
determine the magnitude of impact on the output of any particular source of variability.
Some typical sources of error in quantitative imaging values that may be useful to consider include 
(but are not limited to):
·
Patient Characteristics
o
Demographic (e.g., patient age, sex, race)
o
Physiological (e.g., weight, heart rate, body temperature)
o
Temporal variability in the measurand (e.g., lesion shape, size, location, blood 
oxygenation)
o
Spatial heterogeneity of tissue (e.g., melanin content)
o
Spatial and temporal variability in surrounding tissue (e.g., respiratory motion, breast 
density, calcification adjacent to lesion)
o
Disease state, comorbidities, or exogenous material present (related or unrelated to 
quantitative imaging function, e.g., implanted devices present on MRI or tattoos in 
optical imaging)
·
Image Acquisition
o
Patient positioning and preparation during image acquisition
o
Imaging hardware (manufacturer, model, software version) of the imaging device
10 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/software-medical-device-
samd-clinical-evaluation.

---

<!-- Page 10 -->
Contains Nonbinding Recommendations
10
o Image acquisition protocol (e.g., MR sequence and timings; x-ray dose; amount, type, 
and time of acquisition after contrast media injection and the route of delivery; 
radiotracer; cardiac or respiratory gating.)
o Image data noise
o Presence of image artifacts 
o User interaction in image data acquisition (e.g., transducer position during ultrasound)
o Image reconstruction algorithm 
o Imaging device motion/vibration
·
Image Processing
o Algorithm specifics (e.g., filtering, software version, database selection)
o User interaction (e.g., manual segmentation, seed point selection)
o Non-deterministic algorithm (e.g., curve fitting for dynamic contrast enhanced MRI 
exams) 
VI. Information to Include in a Premarket Submission
FDA recommends that the premarket submission for your device that incorporates quantitative 
imaging function(s) include the information described below.
Function Description 
 
Your premarket submission should include a technical description of the quantitative imaging 
function(s) included in your device at a level of detail sufficient for the Agency to understand the
functionality.  In some instances, a more general description of the measurement process may be 
sufficient; however, you should provide a more detailed description of the processes for more 
complex quantitative imaging functions, to ensure FDA’s understanding of your device.  Details on 
the software implementation for your algorithm should be included as part of the software 
documentation following the Agency’s recommendations found in “Guidance for the Content of 
Premarket Submissions for Software Contained in Medical Devices.”11  FDA recommends including 
the following information when describing your quantitative imaging function(s):
·
A description of the quantitative imaging function, such as:
o Description of the measurand (including units);
o Name, version, and relevant characteristics of the software platform;
o
A detailed description of the algorithm employed, including algorithm inputs and 
outputs;  
o
For algorithms derived from physical processes (e.g., fluence correction, tomographic 
image reconstruction), the assumed underlying physics and its relationship to the 
mathematical components of the algorithm;
o
Level of automation (e.g., manual, automatic, or semi-automatic); and
11 Available at https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-content-premarket-
submissions-software-contained-medical-devices.

---

<!-- Page 11 -->
Contains Nonbinding Recommendations
11
o If applicable, a brief summary of your algorithm training paradigm, including how 
algorithm parameters and thresholds were established. 
·
Information about input data (e.g., images):
o Target population, including intended patient populations, organs, and 
diseases/conditions/abnormalities;
o Restrictions on input data, such as imaging modalities, as applicable, (e.g., computed 
tomography, magnetic resonance), make, model, and specific trade name for each 
modality/system, specific ancillary hardware/software necessary to produce the input 
data (e.g., magnetic resonance elastography (MRE) acoustic driver), specific image 
acquisition parameter ranges (e.g., kVp range, slice thickness, voxel size) or specific 
imaging protocol(s) (e.g., pre-exam diet, breath hold, magnetic resonance angiography 
(MRA) sequence); or
o Specific limitations, including diseases/conditions/abnormalities or imaging 
conditions, for which your quantitative imaging function has been found ineffective 
and should not be used, as applicable. 
·
Image acceptance activities (e.g., how your device ensures that input data (e.g., 
images)/preprocessing are acceptable for processing with your algorithm) and whether these 
are performed manually by a trained user or automatically by your algorithm;  
·
Information presented to the user about the derived values (including units); and   
·
The level of user interaction needed for your device to be used as intended, and if applicable, 
instructions for users (preprocessing image steps, selecting seed points, applying algorithm, 
and verifying resulting measurement for a lesion sizing tool).
Technical Performance Assessment
Your premarket submission should include performance specifications for your quantitative imaging 
function(s).  In general, quantitative imaging functions should have quantitative performance 
specifications that correspond to the claims and uncertainty associated with the quantitative imaging 
function described in the device labeling.  The appropriate performance specifications will depend on 
the intended use of the quantitative imaging function, the complexity of the measurement algorithm, 
and the availability of reference values.  Additionally, performance specifications may change 
throughout the operating range of the quantitative imaging function.  For example, the reproducibility 
of a volumetric measurement tool may depend on the size of the structure being measured, or the 
error associated with T1 values from magnetic resonance imaging may depend on the inversion time.
Supporting performance data should demonstrate that your quantitative imaging function meets the 
predefined performance specifications.  The assessment should consider the factors that can impact 
the performance of your quantitative imaging function (see the Potential Sources of Measurement 
Error in Section V of this guidance).  We recommend that you use performance specifications that 
incorporate objective reference values, if available, as this enables objective comparison between the 
subject and predicate device performance.  For example, a quantitative lesion size measurement for

---

<!-- Page 12 -->
Contains Nonbinding Recommendations
12
magnetic resonance images may set a performance specification of bias less than 10% over the range 
of 3 – 20 mm lesions and compare measured lesion sizes to reference values from widely accepted 
phantoms.  
Phantoms can serve as a high-quality reference standard for which the ground truth is known. 
Phantoms are useful to objectively compare measurements to a known value and may be valuable 
when testing to compare across quantitative imaging algorithms.  However, they are simplifications 
and may not fully reflect the performance of the device in clinical situations. 
We recommend that the technical performance assessment of a quantitative imaging function of your 
device include the following steps:
1. Define the quantitative imaging function, its relationship to the measurand, and the use 
conditions.  For example, if the input to your algorithm is required to have a pixel size of < 1 
mm, you would not be expected to evaluate the performance of your algorithm for pixels > 1 
mm. 
2. Determine an appropriate reference standard and the performance metrics applicable to your 
device.  Bias, precision, limits of detection, limits of quantitation, linearity, sensitivity, 
specificity, and uncertainty should generally be considered as applicable.  
3. Characterize the performance of the quantitative imaging function under the conditions 
defined in the device labeling.  
4. Define the experimental unit (e.g., per lesion, per patient).
5. Define the appropriate statistical estimates of performance (e.g., limits of agreement, total 
deviation index). 
6. Define acceptance criteria (performance targets or goals) based on the intended use of the 
quantitative imaging function and other restrictions/limitations (such as minimum image 
quality requirements).
7. Specify the elements of the statistical design, the necessary data (e.g., patient population, type 
of images), and the statistical analysis plan, based on the selected performance metrics.  This 
statistical analysis should be appropriate for the task at hand. 
8. Collect the relevant data.  
9. Perform the statistical analysis. 
10. Compare the analysis results to the pre-defined acceptance criteria.
Uncertainty (see Definition section above) should be included in the performance specifications for 
all quantitative imaging functions.  Uncertainty should ideally be assessed in conditions that reflect 
the intended use of the device.  In general, an uncertainty assessment performed under controlled 
conditions as part of the technical performance assessment will likely reflect less uncertainty than can

---

<!-- Page 13 -->
Contains Nonbinding Recommendations
13
be expected during clinical use.  The most appropriate uncertainty metric will depend on your 
quantitative imaging function.  Uncertainty information should cover the entire operating range of 
your quantitative imaging function, as the uncertainty associated with a measurand may change 
throughout the operating range.  Uncertainty information should be presented in units of the 
measurand whenever possible and reported along with the conditions under which it was measured.
Any claims regarding the performance of the quantitative imaging function should be supported by 
studies with pre-defined acceptance criteria.   
In general, FDA believes that quantitative imaging functions that generate outputs without the 
opportunity for user correction (i.e., fully automated devices) should include more robust analytical 
validation and more information describing the uncertainty associated with the output than manual 
quantitative imaging functions or quantitative imaging functions for which users review and correct 
outputs (i.e., semi-automated devices).  For fully automated functions, it is also generally appropriate 
to help users understand the situations under which the quantitative imaging function will generate an 
output that is incorrect, but where the error may not be easily identifiable.  Automated devices that 
make claims of improved accuracy and reproducibility compared to manual methods should be 
supported by studies comparing quantitative imaging values produced by the device to those of 
expert users.
Labeling (User Instructions)
Your premarket submission must include labeling in sufficient detail to satisfy any applicable 
requirements for your type of premarket submission (e.g., 21 CFR 807.87(e) or 21 CFR 
814.20(b)(10)).  In addition, device labeling must satisfy all applicable FDA labeling requirements, 
including 21 CFR part 801.  Your device labeling should include sufficient information for the end 
user to obtain, understand, and interpret the values provided by the quantitative imaging function.  
Generally, this information should include:
a) A description of the measurand and the units in which it is measured.
b) A description of the algorithm inputs, including any restrictions on input data (e.g., images). 
c) Performance specifications, including uncertainty information, that cover the entire operating 
range of the quantitative imaging function.  The performance specification or claims in the 
labeling should correspond to device design requirements or specifications.  
 
Uncertainty information should facilitate interpretation of results and should be provided in 
units of the measurand whenever possible.  On-screen display of uncertainty information is 
preferred whenever possible.
  
For quantitative imaging functions for which specific performance metrics for uncertainty 
cannot be provided, the premarket submission should include information on the primary 
sources of variability affecting the quantitative imaging output (e.g., pixel size, image signal-
to-noise-ratio (SNR), patient anatomy).

---

<!-- Page 14 -->
Contains Nonbinding Recommendations
14
d) Instructions for image acceptance or quality assurance activities to be performed by the user.  
If the performance for the quantitative imaging function is dependent on quality assurance by 
the user (e.g., ensuring that SNR is acceptable, slice thickness is within a given range, that the 
image is free of artifacts), the device labeling should include quality assurance protocols (e.g., 
what characteristics to test for, how to execute test methods and calculate metrics), as well as 
clear instructions on actions to be taken when quality assurance fails.  A detailed description 
of all necessary phantoms and/or instructions on how to obtain phantoms should be included.
e) A description of the qualifications and training needed for a user to be within the device’s 
intended user population.
f) Quantitative imaging functions that provide a comparison to a reference database should 
include information about the composition of the reference database (e.g., subject 
demographics, number of subjects within each stratum or bin of the database).  If the database 
is well known and publicly available, we recommend you include a reference or a hyperlink 
to the publicly available reference in your labeling.  For in-house developed reference 
databases, information on subject composition (e.g., number of subjects, subject 
demographics (e.g., sex, race, age), disease conditions) should be provided.  
VII. Examples
The purpose of these examples is to illustrate the range of possibilities that exist for a single type of 
quantitative imaging function, in this case a vessel stenosis measurement tool.  The examples are not 
intended to describe any particular device, but rather, to illustrate how the validation and labeling for 
a quantitative imaging function can vary based on the design and outputs of the quantitative imaging 
function.  As stated previously, the appropriate validation and labeling for any particular device will 
depend on the device’s intended use, the device functionality, and the performance claims.   
Example 1 – Manual Quantitative Imaging Function 
Guiding Principles:  Making a quantitative measurement using a fully manual function should be a 
transparent process.  Manual quantitative imaging functions are often used for a variety of clinical 
tasks, and users should have sufficient information to determine whether the performance of the 
quantitative imaging function will meet their clinical needs.  A simple, fully-manual quantitative 
imaging function may not have been clinically validated for any specific task, and this should also be 
made clear to the end user.  Alternately, if performance specifications for a specific task were pre-
specified and validated, this important information should also be clearly communicated to the end 
user.    
Function Description 
The device description should clearly describe the functionality of the quantitative imaging function, 
including inputs, outputs, limitations on patient population, or input images (e.g., imaging modalities,

---

<!-- Page 15 -->
Contains Nonbinding Recommendations
15
acquisition techniques).  Any algorithms implemented by the quantitative imaging function should be 
clearly specified.  
Technical Performance Assessment
The premarket submission should include documentation of software verification activities 
demonstrating that the algorithm underlying the quantitative imaging function has been correctly 
implemented.  This should include confirmation that measurement and user interface functions in the 
software have been implemented correctly.  Software verification could be achieved using a software 
phantom with simple geometric features and test objects spanning the range of relevant clinical 
scenarios whenever possible.
It may not be possible to generate pre-specified clinical performance specifications for a quantitative 
imaging function that relies heavily on user input.  However, depending on your device’s intended 
use, it may be appropriate to characterize the performance of the quantitative imaging function as 
part of your validation for a range of different users expected in clinical use.  A quantitative imaging 
function of this type may or may not include performance claims: any performance claims should be 
adequately supported.  
Labeling (User Instructions)
The labeling should clearly describe the functionality of the quantitative imaging function by 
addressing labeling elements VI.C.a – VI.C.f, discussed above, including specifying how the 
quantitative imaging function calculates output values, and providing the geometric formulas 
employed to generate those results.  
If pre-specified performance specifications were defined, those performance specifications should be 
clearly communicated to the user.  If performance specifications are unavailable, the user should be 
clearly informed that the performance of the quantitative imaging function under any specific clinical 
use scenario is unknown.  It may be appropriate to identify the sources of variability that most impact 
the output value.
    
Any limitations on input images (e.g., imaging modalities and acquisition techniques) should be 
clearly specified, including delineation of which quality control activities the user is expected to 
perform versus the activities performed automatically by the quantitative imaging function. Warnings 
should be developed for known limitations of the device and should note that variability in device 
output can be expected across users. 
Example 2 – Semi-automated Quantitative Imaging Function
Guiding Principles:  Making a measurement using a semi-automated quantitative imaging function 
may involve some “black box” steps that are not transparent even to an expert user.  Risks of gross 
errors due to the performance of the quantitative imaging function are still reasonably mitigated by 
the expertise of the user, since users are generally expected to inspect and concur with generated 
results.  Modest errors or small biases in function, however, may not be readily detected, making a

---

<!-- Page 16 -->
Contains Nonbinding Recommendations
16
more thorough evaluation of the performance of the quantitative imaging function advisable 
compared with a manual measurement tool.
Function Description
The device description should clearly describe the functionality of the quantitative imaging function, 
including inputs, outputs, limitations on patient population, or input images (e.g., imaging modalities, 
acquisition techniques), and operations expected to be performed by the user versus functions 
implemented by the quantitative imaging function.  Any algorithms implemented by the quantitative 
imaging function should be clearly specified.  
Technical Performance Assessment 
In addition to the verification and validation activities outlined above for the fully-manual 
quantitative imaging function, supporting performance data for a semi-automated quantitative 
imaging function should verify that the performance specifications for the quantitative imaging 
function have been met when the measurement tool is used as intended.  This assessment may be 
performed on phantom data, clinical images, or both; however, it may be difficult to characterize 
accuracy based only on measurements of clinical images.  The following points should be considered 
when choosing the test method:
·
If relying only on phantom data to validate the tool, you should include a rationale as to why 
the semi-automated tool is expected to perform similar to or consistent with a manual tool on 
clinical images; and
·
Testing should evaluate the quantitative imaging values produced when the tool is used as 
intended, including any editing steps; however, the testing should also capture performance of 
the automated steps sufficient to demonstrate the automation performs as intended.  
Any claims that the quantitative imaging function improves accuracy and reproducibility over 
manual methods should be adequately supported with studies involving multiple clinicians and a 
range of clinical use scenarios.  It is important to keep in mind that improvements in reproducibility 
may not reflect improvements in accuracy and vice versa.
Labeling (User Instructions)
The labeling should clearly describe the functionality of the quantitative imaging function by 
addressing labeling elements VI.C.a – VI.C.f, discussed above, including tasks performed by the 
quantitative imaging function versus tasks that are the responsibility of the end user.  The user 
instructions should summarize the testing that was performed to demonstrate that the quantitative 
imaging function met its pre-specified performance specifications.  Known and potential sources of 
substantial measurement error should be listed, and their potential impact discussed.  If applicable, 
common failure modes, known and potential sources of substantial error, and known limitations of 
the quantitative imaging function should be communicated to the user.  Any performance claims

---

<!-- Page 17 -->
Contains Nonbinding Recommendations
17
made in the labeling should be consistent with the device specifications and adequately supported by 
performance data. 
Example 3 –Fully Automated Quantitative Imaging Function 
Guiding Principles:  A fully automated quantitative imaging function may bypass important 
evaluation steps that would normally be performed by an expert user.  A fully automated quantitative 
imaging function may not have the same opportunities for clinicians to identify and mitigate risks due 
to gross errors associated with imaging issues or major performance failures of the quantitative 
imaging function.  Therefore, in addition to characterizing performance, the performance testing 
should demonstrate that the likelihood of unintended performance has been adequately validated 
across the variety of expected use cases. 
Function Description
The device description should clearly describe the functionality of the quantitative imaging function, 
including inputs, outputs, limitations on patient population, or input images (e.g., imaging modalities, 
acquisition techniques).  Any algorithms implemented by the quantitative imaging function should be 
clearly specified.  
Technical Performance Assessment 
A fully automated quantitative imaging function should have pre-specified performance 
specifications and be tested on clinical data that represent the variety of expected use cases, including 
cases that are expected to challenge the algorithm.  Depending on intended use, these use cases may 
need to include a variety of imaging modalities (and manufacturers, models, etc., depending on the 
device’s intended use), a range of clinically relevant settings, and an appropriately diverse patient 
data set.  For a fully automated quantitative imaging function, phantom data may be useful but likely 
cannot completely replace the need for clinical data because phantoms may be an incomplete 
representation of clinical data.
Labeling (User Instructions)
The labeling should clearly describe the functionality of the quantitative imaging function by 
addressing labeling elements VI.C.a – VI.C.f, discussed above.  The user instructions should clearly 
summarize the pre-specified performance specifications for the quantitative imaging function and 
summarize the testing that was conducted to verify that the quantitative imaging function met these 
performance specifications.  Known and potential sources of substantial measurement error should be 
listed, and their potential impact discussed.  Common failure modes, known and potential sources of 
substantial error, and known limitations of the quantitative imaging function should be 
communicated to the user.  Any performance claims made in the labeling should be consistent with 
the device specifications and adequately supported by performance data.
