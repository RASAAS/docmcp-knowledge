# Reporting of Computational Modeling Studies in Medical Device Submissions: Guidance for Industry and Food and Drug Administration Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/reporting-computational-modeling-studies-medical-device-submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/reporting-computational-modeling-studies-medical-device-submissions)

**Published:** 2016-09-21


---

This guidance represents the current thinking of the Food and Drug Administration (FDA or Agency) on this topic.  It does not establish any rights for any person and is not binding on FDA or the public.  You can use an alternative approach if it satisfies the requirements of the applicable statutes and regulations.  To discuss an alternative approach, contact the
FDA staff or Office responsible for this guidance as listed on the title page.
Introduction
For many years, computational modeling and simulation (CM&S) studies have been used by sponsors to support device design/development and have been reported in medical device submissions.  These studies have traditionally been used in the areas of fluid dynamics (e.g., calculate shear stress in ventricular assist devices), solid mechanics (e.g., determine maximum stress locations in a hip implant), electromagnetics and optics (e.g., radiofrequency safety in magnetic resonance imaging, fluorescence for fiber optic spectroscopy devices), ultrasound propagation (e.g., absorbed energy distribution for therapeutic ultrasound), and thermal propagation (e.g., temperature rises with radiofrequency and laser ablation devices).
The purpose of this guidance document is to provide recommendations to industry on the formatting, organization, and content of reports of CM&S studies that are used to support medical device submissions.  Moreover, this guidance is also for FDA Staff, to improve the consistency and predictability of the review of CM&S studies and to better facilitate full interpretation and complete review of those studies.

FDA's guidance documents, including this guidance, do not establish legally enforceable responsibilities.  Instead, guidances describe the Agency's current thinking on a topic and should be viewed only as recommendations, unless specific regulatory or statutory requirements are cited.  The use of the word should in Agency guidances means that something is suggested or recommended, but not required.
Scope
Computational modeling and simulation studies, together with bench, nonclinical in vivo, and clinical studies, can be used to evaluate the safety and effectiveness of medical devices.  In order for the CM&S studies to serve as valid scientific evidence in regulatory submissions, specific details need to be included in the report of such studies.  In this guidance, the term “CM&S report” refers to the part of a regulatory submission that provides information about a CM&S study; the term does not describe a new submission requirement.

The recommended format provided in this document aims to establish uniformity in reporting CM&S studies.  FDA recognizes that the level of detail to be reported will vary and will depend on the context of use for the CM&S studies.  Moreover, there are a variety of CM&S modalities and thus the specific details will vary across disciplines.  Therefore, we have provided a general outline in the main body of this document and five subject matter appendices for CM&S modalities that are widely used in regulatory submissions.  The main body is written in general terms to capture reporting for any modality.  The five appendices provide more background, structure, and specific terminology for the following subject areas:

### I. Fluid Dynamics and Mass Transport
## II. Solid Mechanics
## III. Electromagnetics and Optics
## IV. Ultrasound
### V. Heat Transfer

For multiphysics modeling, recommendations in several of these appendices may apply.

The scope of this guidance is limited to how CM&S studies and its outcomes can be used to support a regulatory submission when medical devices use such studies to determine safety and effectiveness.  This guidance document does not address or make a determination whether CM&S tools may be considered medical devices.

While verification and validation of the CM&S studies are necessary components of the report, this document does not establish the amount or type of verification and validation needed to support using the CM&S studies in regulatory submissions.  Further, this guidance document does not address how to conduct a computational modeling or simulation study, nor does adherence to this guidance ensure that your computational modeling or simulation study is adequate or appropriate.  This guidance only provides guidelines for reporting this information to FDA and highlights some common issues with models and simulations.

Outline of the CM&S Report
In the following section, we provide the recommended headings and details for a CM&S report contained within a regulatory submission.
### I. Executive Report Summary
We recommend that you provide a concise and complete overview of the report of the computational modeling and/or simulation study, that includes the following: • Context of use of the CM&S study including a clear identification of the quantity(s) of interest (QOI) (e.g., to determine the maximum stress value(s) and location(s))
• Scope of the analysis (e.g., for a device that has multiple sizes and/or configurations, specify which sizes and/or configurations were modeled, and how the computational model relates to the intended patient population)
• Type of analysis (e.g., fluid dynamics and mass transport, solid mechanics, electromagnetics and optics, ultrasound, heat transfer)
• Conclusions with respect to the context of use • Keywords: we recommend that you provide up to five keywords or key phrases that describe the modeling modality, the device product code, any relevant materials of the device, analysis type, and if applicable, location in the body.  For more information on the device product code, refer to the FDA guidance entitled “Medical Device Classification Product Codes” issued on April 11, 2013.  The following are examples of keywords that outline this information: − e.g., finite element analysis, MIH, nitinol, fatigue, aorta − e.g., radiofrequency dosimetry, OQG, cobalt chromium, magnetic resonance safety, hip
This information will be used for semantic text mining of CM&S reports to better understand the impact of this guidance on CM&S studies used in regulatory submissions.
## II. Background/Introduction
We recommend that you provide a brief description of the device system and intended use environment.  Discuss the context of use of the analysis, as this will dictate the relevant details necessary for review.
## III. Code Verification
We recommend that you provide a brief description of the software quality assurance (SQA) and numerical code verification (NCV) that you performed.  Code verification establishes the correctness of the code used as software tools for CM&S and establishes the correctness and fidelity of the numerical algorithms; this is accomplished through SQA and NCV.  Software tools include off-the-shelf, modified-off-the-shelf, or userdeveloped.  Code verification is important, regardless of the software type.

### A. Details
SQA ensures that the code is functioning correctly and produces repeatable results on specified computer hardware and in a specified software environment.  NCV ensures correct implementation and functioning of the numerical code, which is typically accomplished by, for example, comparison to bench-mark solutions, method of manufactured solutions.  You should briefly describe the code verification activities.
You may reference available documentation and verification results from the software developer.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the applicability of the verified code to your computational domain.  If applicable, describe and rationale for differences between the code used for verification and the code used for the context of use.
Moreover, provide rationale to support the selection of the numerical settings, regardless if the settings are default or modified.

Note that the details regarding calculation verification, the other component to the verification process, are provided in System Discretization and Numerical Implementation, sections VIII and IX, respectively.

## IV. System Configuration
We recommend that you provide information regarding the system configuration (e.g., the geometry of the device, the computational domain, the structure of a physiological control system, the in vitro test that is modeled).

### A. Details
You should describe the components of the system (e.g., device, in vivo and/or in vitro environment), including appropriately scaled/dimensioned images and/or diagrams.

You should describe the methods (e.g., image reconstruction and resolution, computer aided design (CAD)) used to generate the system configuration, including format, and discuss how the configuration was appropriately captured for the intended analysis.

You should describe the software used to generate the system configuration (e.g., CAD software, image segmentation software, control-system simulation software).
Describe the imaging modality if image reconstruction was used to generate geometry.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to generate the system configuration as compared to the actual device and environment.  If appropriate, provide a clinical rationale for the in vivo/in vitro models (e.g., size, disease state, mathematical convenience versus clinical relevance).
### V. Governing Equations/Constitutive Laws
We recommend that you provide information regarding the governing equations and/or constitutive laws used to perform the computational analysis.

### A. Details
You should provide a description of the governing equations/constitutive laws for the system.  Provide the actual equations, if appropriate.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications of the governing equations/constitutive laws chosen to represent the system.
## VI. System Properties
We recommend that you provide information regarding the biological, chemical, physical and physiological properties of the system, as appropriate.

### A. Details
You should describe and quantify all system properties used in the analysis.  These might include biological material properties (e.g., cells, tissues, organs) and/or processes (e.g., cell signals), and/or states (e.g., diseased, healthy), chemical properties, physiological properties and physical properties that define the materials and/or process characteristics.  Please also discuss the variability (e.g., temporal, spatial, across individuals/samples) of system properties, if applicable.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the system properties.  Identify the source and provide the reference for the properties (e.g., literature, in vivo, ex vivo, in vitro testing).
## VII. System Conditions
We recommend that you provide information regarding the conditions that were imposed on the system.  These might include, but are not limited to, the boundary and loading conditions, initial conditions, and other constraints that control the system.

### A. Details
You should describe the system conditions imposed on the model and their variability, if applicable.  If appropriate, provide a graphical representation of the conditions, depicting how they are applied to the system.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the conditions applied on the system.  Provide appropriate documentation (e.g., literature, test reports, clinical data, medical imaging data).
## VIII. System Discretization
We recommend that you provide information regarding the discretization and refinement techniques applied to the system for solving it numerically.

### A. Details
You should describe the system discretization methods and how they were applied to the computational domain.  Describe the calculation verification methodology (e.g., mesh refinement study) used to ensure that the computational domain was suitably resolved.  If applicable, provide a representative image of the discretization in the areas of interest of the computational domain.  You should describe the type and quality of the discretization.  As part of the calculation verification process, report the criteria used to determine that the solution was sufficiently resolved.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to discretize the computational domain.  Report the criteria used to determine that the discretization was sufficient to resolve the QOI(s).

## IX. Numerical Implementation
We recommend that you provide information regarding the numerical implementation used to solve the governing equations.

### A. Details
You should describe the numerical implementation methodology and/or numerical method used to solve the governing equations.  State the solver parameters (e.g., tolerance, relaxation) and convergence criteria.

B, Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the solver and associated parameters.  Note that rationale should be provided for the solver settings, whether they are adjusted from the default settings or not.
### X. Validation
We recommend that you provide information regarding the method(s) employed to validate the computational model for the context of use.

### A. Details
You should describe the method (e.g., in vivo, ex vivo or in vitro comparator) used to assess the validity of the computational model.  Report and compare the QOI(s) from the computational model and the comparator.  Describe the sensitivity of the QOI(s) on key parameters and provide a systematic analysis of the uncertainty in relation to the key parameters, as appropriate.

### B. Assumptions, simplifications, and rationale
You should describe and provide the rationale for the assumptions and simplifications of the method (e.g., in vivo, ex vivo or in vitro test) used to validate the computational model.  You should discuss why the method of comparison and the degree of agreement between QOI(s) from the comparator and computational model are appropriate for using the computational model in the context of use.
## XI. Results
We recommend that you present the quantitative results, the QOI(s), from the CM&S study.  You should provide the results with sufficient level of detail, including labels and legends.  The results may be presented in more than one format (e.g., table, graph).
## XII. Discussion
We recommend that you discuss how the results from the CM&S study relate to the context of use.  If appropriate, discuss the regulatory and/or clinical relevance of the results.
## XIII. Limitations
We recommend that you provide details regarding how the assumptions, simplifications, sensitivity and uncertainty analyses described in the previous sections might affect the output of the computational model, the interpretation of the results, and the relevance to the context of use.
## XIV. Conclusions
We recommend that you state the overall conclusions of the CM&S study and if the regulatory objective(s) have been met.
## XV. References
We recommend that you provide a list of the appropriate references used to support the CM&S study.
Glossary
For purposes of this guidance, the following terms are defined.

Accuracy: the difference between a parameter, variable or derived quantity (or a set of parameters or variables) within a model, simulation, or experiment and the true value or the assumed true value.

Analysis: any post-processing or interpretation of the individual values, arrays, files of data, or suites of executions resulting from a simulation.

Calculation Verification: the process of determining the solution accuracy of a particular calculation.

Code Verification: the process of determining that the numerical algorithms are correctly implemented in the computer code and identifying errors in the software.

Comparator: the experimental methodology that is used to perform validation.  The comparator data can be taken from a laboratory bench-test, an animal study, an imaging study, or a clinical study.  The selection of the comparator should be based on the context of use.

Computational domain: the spatial and/or temporal domain for which the analysis was conducted.  See also System Discretization.

Computational model: the numerical implementation of the mathematical model performed by means of a computer.

Constitutive law: an expression which describes the relationship between biological, chemical or physical quantities for a specific material or substance and an external stimuli (e.g., Hooke’s Law).

Context of use: the purpose or intent of the computational model and/or simulation study, specifically the role of the CM&S study in the regulatory submission.

Convergence analysis: the process of ensuring the solution resolves the physics of interest and the variation of the solution remains within a pre-specified range as the discretization is refined.

Governing equation: the mathematical relationship that describes the phenomena of interest.

Mathematical model: the mathematical equations, boundary values, initial conditions, and modeling data needed to describe the conceptual model.
Model: a description or representation of a system, entity, phenomena, or process (adapted from Banks, J., ed. (1998). Handbook of Simulation. New York: John Wiley & Sons).  Any data that go into a model are considered part of the model.  Models may be mathematical, physical, or logical representations of a system, entity, phenomenon, or process.  Models can be used by simulation to predict a future state, if so desired.

Quantity of Interest: the desired output from the computational model.  For a particular context of use, there can be multiple quantities of interest.

Sensitivity: the degree to which the output is affected by a particular input.

Simulation: the imitation of the characteristics of a system, entity, phenomena, or process using a computational model; a specific “run” of the model with one set of parameters that results in the quantity of interest or multiple quantities of interest.

Subject matter: a particular technical discipline, system, or process regarding computational modeling methodologies.

System discretization: the division of the computational domain of the system into discrete parts for numerical implementation.

Uncertainty: the estimated amount or percentage by which an observed or calculated value may differ from the true value (The American Heritage Dictionary of the English Language, 4th ed.).

Validation: The process of determining the degree to which a model or a simulation is an accurate representation of the real world from the perspective of the intended uses of the model or the simulation (American Society of Mechanical Engineering Verification &Validation Guide – ASME V&V 10-1-2012).

Verification: The process of determining that a computational model accurately represents the underlying mathematical model and its solution from the perspective of the intended uses of modeling and simulation (American Society of Mechanical Engineering Verification &Validation Standard – ASME V&V 20-2009).  See also Code Verification and Calculation Verification.
Subject Matter Appendix I –
Computational Fluid Dynamics and Mass Transport

For questions regarding this appendix, contact Matthew Myers, Ph.D. at (301) 796-2525 or at rrcm@fda.hhs.gov.


Introduction/Scope of the Appendix
The purpose of this appendix is to provide recommendations on the formatting, organization, and content of reports for computational fluid dynamics and mass transport modeling and simulation studies in medical device regulatory submissions.

Specific examples provided in this appendix, such as output metrics, are only examples and should not be considered as requirements or recommendations for the type of CM&S studies and validation to complete.

Outline of the Report
In the following section, we provide an outline for reporting the details of your computational modeling and simulation study.

### I. Executive Report Summary
We recommend that you provide a concise and complete overview of the report of the computational modeling and/or simulation study, which includes the following: • Briefly summarize the context of use and scope of the analysis, as well as the rationale for choosing the computational modeling approach as opposed to other approaches (e.g., experimental).
• Briefly summarize the type(s) of analysis(es) conducted in the CM&S study (e.g., fluid mechanics, diffusion, diffusion/convection).
• Briefly summarize the model, including geometry, material properties, and boundary/initial conditions.
• If the device has multiple sizes and/or configurations, provide rationale for the sizes and configurations of the device system evaluated and not evaluated.
• State whether the analysis code/software is commercially available, open source, and/or user developed.
• Discuss the simulation results, the quantities of interest, and their implications for device safety and effectiveness.  Summarize the validation activities and how they are appropriate to support the use of the CM&S study in the context of use.
• Summarize the limitations.
• Summarize the conclusion(s).
• Keywords – please provide up to five keywords or key phrases that describe the modeling modality, the device product code, any relevant materials of the device, analysis type and if applicable, location in the body (e.g., computational fluid dynamics, NIQ, stainless steel, drug transport, coronary artery).  For example, the following are sample keywords relevant to this subject matter: − biofluid mechanics, drug delivery, blood flow, transport, finite volume method, finite element method, pump.

## II. Background/Introduction
We recommend that you state the context of use of the analysis, because this will determine the relevant details necessary for review.  Provide a brief description of the device, along with its intended use environment and deployment/implantation procedure.
The details provided in this section should correspond to the objectives of the analysis, which should be outlined in the context of use statement.

## III. Code Verification
We recommend that you provide a brief description of the software quality assurance (SQA) and numerical code verification (NCV) that you performed on the software used for the CM&S study.  Software tools include off-the-shelf, modified-off-the-shelf, or user-developed.  Code verification is important, regardless of the software type.

### A. Details
You should briefly describe the code verification activities and provide the following: • comparisons to simplified systems which have an analytical solution; • sensitivity analyses of the discretization scheme and solver parameters performed using the actual system (i.e., timestep, grid size (grid refinement)) and convergence criteria (e.g., 1E-6 vs 1E-7)); • a description of how the simulation numerically converged via residual reductions and/or monitoring of physically relevant fluid flow quantity at a probe point or surface location; and • a method to demonstrate that the basic conservation laws were obeyed.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the applicability of the verified code to your computational domain.  If applicable, describe and rationale for differences between the code used for verification and the code used for the context of use.
Moreover, provide rationale to support the selection of the numerical settings, either default or modified.

Note that the details regarding calculation verification, the other component to the verification process, are provided in System Discretization and Numerical Implementation, sections VIII and IX, respectively.

## IV. System Geometry (System Configuration)
We recommend that you provide information regarding the system configuration (e.g., the geometry of the device, the computational domain, the structure of a physiological control system, the in vitro test that is modeled).

### A. Details
You should describe the components of the system (e.g., device, vessel, organ, organ system) to be evaluated.  Provide all relevant dimensions of the device and geometry.
Include diagrams, schematics, and photos, as needed.

You should describe methods/software (e.g., image reconstruction, CAD) used to generate the geometry in order to demonstrate that the configuration was captured appropriately for the intended analysis.  In particular, describe any scaling or similarities (e.g., geometric and dynamic similarity).

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to generate the system configuration as compared to the actual device and environment.

For example, if the entire device system was not modeled or if simplifications were made to the geometry, you should provide rationale for the system geometry that was analyzed (e.g., the use of symmetry, only a portion of device, or representative inlet and outlet geometries), including the following:

• Describe any differences between the model and the actual configuration.
• Discuss how manufacturing tolerance dimensions might influence the results compared to nominal dimensions.
• Describe how the inlet and outlet geometries were selected and how these might affect the flow regime.
• If the device has unique geometric features (e.g. surface topography) that might affect the analysis, then describe how those were or were not accounted for in the model.
• Include relevant information on limitations and assumptions (e.g., scaling) image resolution, smoothing, image segmentation errors, as related to the geometry.

### V. Governing Equations/Constitutive Laws
We recommend that you provide information regarding the governing equations and/or constitutive laws used to perform the computational analysis.

### A. Details
You should provide the governing equations/constitutive laws for the system, including the following: • the equations defining the model (e.g., Navier-Stokes equations for fluid flow, Fick’s equations for diffusion, Darcy’s equations for porous flow); • the constitutive relationships used in the simulation (e.g., the relation between shear stress and velocity gradient for fluid flow, the relation between diffusive flux and concentration gradient for diffusion, the relation between discharge flux and pressure gradient for porous flow); • the turbulence modeling used, if any, including any specialized wall functions used; and • any other specialized mathematical modeling employed (e.g., blood damage models).

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications of the governing equations and constitutive laws chosen to represent the system, including the following: • the simplifications of the basic mathematical equations based on assumptions and rationale (purpose) of the simulation being undertaken; • the assumptions and rationale involved in simplifying the governing equations (e.g., use of steady rather than unsteady flow); • the information that confirms that the constitutive model(s) captures the actual behavior being modeled; and • the use of any turbulence model or wall functions, as well as other equations used to capture additional phenomena (e.g., blood damage models).

## VI. System Properties
We recommend that you provide information regarding the biological, chemical, and physical properties of the system.

### A. Details
You should provide, preferably in a tabular form, all physical properties, coefficients, and descriptive equations used in the simulation and post processing, such as: • fluid viscosity and density • gas solubility and diffusivity • diffusion and reaction coefficients of constituents • permeability and porosity • temperature dependence of properties if the simulation is not isothermal
You should provide a report of any testing conducted to generate the system properties, if available.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the system properties.  Identify the sources of the physical properties and coefficients adopted (e.g., literature, in vivo, ex vivo, in vitro testing).
If literature data are cited, discuss their applicability to the specific conditions.  If testing is conducted to determine the parameters, then provide appropriate details regarding the test.  If applicable, discuss any relevant aspects related to the tissue physiology used (e.g., young versus mature, healthy versus diseased).
If there are uncertainties associated with the data (e.g., due to inaccuracies, simplifications, or variations), describe the sensitivity analysis performed, if appropriate, to address the effect of the uncertainties on the simulation results.

## VII. Boundary and Initial Conditions (System Conditions)
We recommend that you provide information regarding the conditions that were imposed on the system.  These might include, but are not limited to, the boundary and loading conditions, initial conditions, and other constraints that control the system.

### A. Details
You should describe the boundary conditions (e.g., inlet and outlet, walls) of the model.  You should describe any global boundary conditions used to represent the simulation in global terms (e.g., pressure drop, mass flow rates, revolutions per minute).

If the model was time dependent, provide the following: • the initial conditions; • if applicable, the transient boundary conditions (e.g., function, table); • if the model was pulsatile, the number of initial cycles modeled to damp out initial transient effects, if any; • any unsteady model(s) employed as an adjunct to a steady model using a rotating or moving frame of reference (e.g., for blood pump); and • a description of how the natural development and physical character of the flow was unaffected by the boundaries of the simulation;

You should provide any relevant nondimensional numbers, such as: • Reynolds number • Strouhal or Womersley number (pulsatile flows)
• Peclet or Sherwood number (diffusion/convection)
• Dean number (curved flow)

If symmetry was used to reduce the size of the model, then you should describe the symmetry boundary conditions.

If a turbulence model was used, then you should provide the turbulence boundary conditions.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the conditions applied on the system.  Provide appropriate documentation the system conditions (e.g., literature, test reports, clinical data, medical imaging data).

In particular, you should describe any differences or simplifications between the simulation environment and the actual environment, such as, • choice of initial and boundary conditions used; • operating conditions of the simulation, especially if the simulation did not cover the expected range of use of the device; and • other simplifications (e.g., use of symmetry, use of rotating frame of reference instead of unsteady simulation for centrifugal pump).

## VIII. System Discretization
We recommend that you provide information regarding the discretization and refinement techniques utilized during the numerical solution as outlined below.

### A. Details
You should describe the following regarding the spatial and temporal discretization: • the software used for generating the mesh; • the mesh in all regions of the computational domain (e.g., device, fluid, surrounding tissue); • the quality of the mesh (e.g., element/cell types, sizes, shapes, quality metrics (i.e., aspect ratios)); • the local mesh refinement in areas of interest (e.g., areas of high shear stress, recirculation zones, critical concentrations, interactions between the device and the body), and provide representative images of the mesh in these areas; • any special elements/cells used if a turbulence model (or any other numerical method requiring special elements/cells) was used; and • for unsteady models, describe how time steps were determined and were deemed appropriate for the analysis (e.g., time step refinement study).

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the following regarding the mesh refinement study that supports the mesh: • any adaptive meshing or automatic mesh refinement used; • the methods of the mesh refinement study, and provide representative images of the meshes used in the refinement study; • the mesh sensitivity analysis performed to justify the production mesh used for the subsequent simulations, that is, to demonstrate that the mesh density did not affect the numerical results; • the numerical metrics (e.g., shear rates, concentration gradients) chosen to establish the mesh density; and • the algorithm for assigning the mesh density or distribution.

## IX. Numerical Implementation
We recommend that you provide information regarding the numerical implementation used to solve the governing equations.

### A. Details
You should describe the discretization of the equations, including: • numerical method used (e.g., finite element, finite volume, finite difference); • temporal discretization, if any (e.g., explicit, implicit, semi-implicit); • spatial discretization (i.e., interpolation of field variables between grid points); and • method for interpolating from face to nodes or vice versa (e.g., upwind, power law).

You should describe the solution methods and provide the following: • solver method (e.g., Newton, multigrid); • solver parameters (e.g., linear solver and tolerance, preconditioners, analytic or numerical Jacobian); • type of software (e.g., commercial, open-source, user-developed) and name, if applicable; • details regarding code verification of the user-supplied subroutines/code; and • convergence criteria (e.g., error method, error threshold, sampling locations and variables used).

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the solver and associated parameters.  For example, provide rationale for the discretization/solver choices made (i.e., benefits over other choices) and discuss the ramifications of the particular choice (i.e., discretization errors).

### X. Validation
We recommend that you provide information regarding the method(s) employed to validate the computational model [1].  We recommend the following format for presenting that information.

### A. General Description
• You should describe, if any, the experimental or analytical comparator that was used for model validation study (e.g., velocity, wall shear stress calculations, hydrodynamic pressure loss).  If a comparator was used, describe if the comparison was made in a quantitative (preferred) or qualitative manner.
•  You should describe experimental uncertainty estimates if an experimental comparison is performed.
### B. Methods
• You should describe the validation test conditions and geometry.
• You should describe the region of interest where validation(s) are performed.
• You should provide diagrams and data to support the assessment of the model.
• You should describe instrumentation and calibration.
• If a biological process was modeled (e.g., hemolysis, platelet damage, binding of drug in vessel tissue), then you should describe how the biological calculations were verified and validated.
### C. Assumptions and Rationale
• You should describe any simplifications for experimental comparator (e.g., use of surrogates when biological information is lacking).
You should provide a rationale to support any differences between the operating and boundary conditions of the comparator experiments and simulations.
• You should describe any sensitivity analysis performed to determine how the solution varied as a function of parameters that are not well known (e.g., parameters contained in turbulence models, boundary conditions, fluid properties).
• You should provide a rationale for any geometric and dynamic scaling assumptions.
### D. Validation Study Results
• You should provide qualitative comparisons between the QOI from the computational model and experimental results.  For example, images that directly compare model and experimental results (e.g., velocity or shear stress) can provide an overall qualitative assessment of how well the model can capture relevant behavior.
• You should provide quantitative comparisons for critical areas of relevance to the goals of the study [2, 3].
### E. Discussion
• You should discuss the degree of agreement between the computational and experimental results.
• You should discuss the relevance of your validation experiment to expected clinical loading conditions, implications of model and experimental assumptions on the results, limitations on the agreement between the validation model and experiment, and the extent of predictability to your device or device-tissue model.
• If predictions of behavior are given in areas that are not accessible by experiment, you should provide a measure of confidence, as well as the risk associated and how it influenced your decision.

## XI. Results
We recommend that you present the quantitative results from the computational modeling study.  You should provide the results with sufficient level of details, including labels and legends.  The results may be presented in more than one format (e.g., table, graph, plot).

Specifically, we recommend that you present the results in regions of interest graphically and quantitatively.  Additionally, please consider providing the following, as applicable: • a statement of biological and other formulations (e.g., hemolysis); • a description of the results in relation to the goals of the study; • a method to demonstrate that the basic conservation laws were obeyed; • if limited studies were performed, a statement that the worst-case was modeled and a description of that worst-case; • for biological extrapolations, a description of relevant variables (e.g., shear rates, exposure times, recirculation zones, drug concentrations); • a description of any adverse effects of device flow on tissues or organs; and • a description of acceptable performance factors based on the results.
## XII. Limitations
We recommend that you provide details regarding how the assumptions/simplifications described in the previous sections might affect the output of the computational model and simulation, the interpretation of the results, and the relevance to the purpose of the study.

Because assumptions and simplifications are made in the generation of the model device, in the performance of the simulation, and in the interpretation of the analysis, it is important to describe the limitations of the use of the computational model and the interpretation of the results.  Therefore, we recommend that you discuss how the assumptions/simplifications might affect the output of the model and simulation and the interpretation of its relevance to device performance and safety.

For example, it is important to know whether the simulation of blood flow through a small gap in a blood pump was based on the nominal dimensions or whether it includes the limits of the manufactured component tolerances.  If you believe that your results are significantly dependent on the assumptions and/or simplifications in your model, you should consider performing sensitivity analyses on the computational model parameters associated with the assumptions and simplifications.

## XIII. Discussion/Conclusion
We recommend that you summarize the CM&S study with respect to the context of use and how it relates to the regulatory submission (e.g., selecting the device size that is expected to perform the worst under the simulated use conditions, establishing the loading conditions for bench testing).  Discuss how the results compare with experimental results, literature results and/or prior product performances, if these results exist.  Discuss the assumptions and simplifications that were made to the model and how they are expected to affect the results and interpretation of the results.  Discuss the strength of your conclusions in terms of the limitations of the model that you have identified.  Discuss how your results convey acceptable performance of the product in vivo, if applicable.
## XVI. References
Please provide a list of the appropriate references used to support the CM&S study.


Bibliography [1] ASME V&V20-2009, Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer

[2] Oberkampf, W.L., Trucano, T.G., and Hirsch, C., 2004 “Verification, validation, and predictive capability in computational engineering and physics,” Applied Mechanics Reviews, 57, pp. 345–384.

[3] Oberkampf W.L. and Barone M.F., 2006 “Measures of agreement between computation and experiment: Validation metrics,” Journal of Computational Physics, 217, pp. 5-36.
Subject Matter Appendix II –
Computational Solid Mechanics

For questions regarding this appendix, contact Jason Weaver, Ph.D. at (301)-796-2504 or at rrcm@fda.hhs.gov.

Introduction/Scope of the Appendix
The purpose of this appendix is to provide recommendations on the formatting, organization, and content of reports for computational solid mechanics modeling studies in medical device regulatory submissions.

Specific examples provided in this appendix, such as output metrics, are only examples and should not be considered as requirements or recommendations for the type of CM&S studies and validation to complete.

The scope of this appendix is limited to finite element analysis (FEA).  FDA acknowledges that there are other types of computational modeling modalities that can be used to evaluate the mechanics and kinematics of medical devices.  Additionally, FDA acknowledges the issues and considerations for non-finite element analyses are similar to those raised for FEA and aspects of this guidance might be applicable.  However, there might be aspects of the non-FEA approaches that are distinct from FEA and could present other issues which are not addressed in this appendix but should be included in the reporting of those studies.

Outline of the Report
In the following section, we provide an outline for reporting the details of your computational modeling and simulation study.

### I. Executive Report Summary
We recommend that you provide a concise, high-level overview of the entire report including the following: • You should briefly summarize the context of use of the CM&S study with respect to the regulatory submission, scope and quantities of interest of the analysis.
• You should briefly summarize the model, including geometry, material properties, and boundary conditions.
• You should state the code/software used.
• You should briefly summarize the validation method and results.
• You should discuss the simulation results and how they relate to the regulatory purpose of the CM&S study.
• You should briefly summarize the conclusion(s).
• Keywords - please provide up to five keywords or key phrases that describe the modeling modality, the device product code, any relevant materials of the device, analysis type, and location in the body for intended use (e.g., finite element analysis, MIH, nitinol, fatigue safety factors, aorta).

## II. Background/Introduction
You should describe the context of use of the CM&S study, as this will dictate the relevant details necessary for review.  We recommend that you give a brief device description along with its intended use environment, specifically noting all causes of loading/deformation on/from the device.

## III. Code Verification
We recommend that you provide a brief description of the software quality assurance (SQA) and numerical code verification (NCV) that you performed on the software used for the CM&S study.  Software tools include off-the-shelf, modified-off-the-shelf, or user-developed.  Code verification is important, regardless of the software type.

### A. Details
You should briefly describe the code verification activities.  You may reference available documentation and verification results from the software developer.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the applicability of the verified code to your computational domain.  If applicable, describe and rationale for differences between the code used for verification and the code used for the context of use.
Moreover, provide rationale to support the selection of the numerical settings, either default or modified.

Note that the details regarding calculation verification, the other component to the verification process, are provided in System Discretization and Numerical Implementation, sections VIII and IX, respectively.

## IV. System Geometry (System Configuration)
We recommend that you provide information regarding the geometry of the device, the computational domain, or the in vitro test being modeled.

### A. Details
We recommend that you provide details regarding the device and/or tissue geometry that was modeled and the method used to create the computational representation of your geometry.  This section might include CAD drawings or reconstructed digital images.

### B. Assumptions, simplifications, and rationale
If you did not model the entire device, you should describe and provide rationale for the portion of the device that was modeled (e.g., utilized symmetry).  If the device is available in different sizes or configurations, describe which sizes or configurations were modeled and provide rationale to support the analysis of those sizes.  If the device and/or tissue has unique geometric features that might affect the analysis (e.g., surface topography) then you should describe how those were or were not accounted for in the model.  Finally, regarding the method of construction, please include relevant information on limitations and assumptions (e.g., image resolution and smoothing) as related to the geometry.

### V. Constitutive Laws
We recommend that you provide details for all of the constitutive relationships used to describe the mechanical behavior of the device material(s) and, if appropriate, the surrounding anatomy.

### A. Details
You should describe the stress-strain relationship, including any material nonlinearities that were included in the model (e.g., linear, hyperelastic, elasticplastic, viscoelastic, poroelastic) of the device and/or tissue material(s).  Specify the degree of anisotropy (e.g., isotropic, orthotropic) of the material(s).  If appropriate, the constitutive relationships may be presented graphically and/or with equations. The numerical inputs for the parameters within the constitutive model should be provided in Section VI – Material Properties.

### B. Assumptions, simplifications, and rationale
You should provide rationale for the constitutive relationship chosen to represent the material behavior and discuss why the assumptions are appropriate.  For example, if you employed linear elastic constitutive laws then, in general, only small-strain deformations should be presented. A rationale should be presented if post-yield stresses are observed and plasticity is omitted.

## VI. Material Properties (System Properties)
We recommend that you provide details regarding all materials used in the CM&S study.

### A. Details
For all materials modeled, you should report the numerical inputs necessary to fully characterize the mechanical behavior.  Some examples of important material inputs include: • constitutive law coefficients • elastic modulus • ultimate tensile strength • fatigue life/endurance limit • plateau stresses and elastic strain limits for shape memory or superelastic materials (e.g., Nitinol)
• strain at break • viscoelastic properties

### B. Assumptions, simplifications, and rationale
You should provide rationale for the sources of material inputs, and state any assumptions or limitations that were inherent from the sources you reference or the testing that you conducted.
If the inputs were obtained from testing, you should provide a description of the testing (e.g., uniaxial tension, 3-point bend, in vivo imaging, implanted sensor) including sample conditions (e.g., geometry, processing, heat treatment), protocol (e.g., loading rate, frequency, mean strain), environment (e.g., temperature, humidity, solution), and, if necessary, the method(s) used to determine the material properties from the test data.

Additionally, for the material properties of the device, state whether testing was conducted on finished devices; if it was not, provide rationale. Similarly, for the material properties of the surrounding biological materials, you should state whether the materials tested capture the important aspects of the target patient population (e.g., healthy versus diseased, young versus mature); if they do not, provide rationale.

## VII. Boundary & Initial Conditions (System Conditions)
We recommend that you provide information regarding the boundary and loading conditions, initial conditions, and other constraints that control the system.


### A. Details
You should describe the conditions of the computational model.  Examples include, but are not limited to, stresses and strains imposed from manufacturing (residual), implantation, and physiologic/pathologic loading.  If applicable, we recommend the following for each analysis step: • You should provide an overall schematic or diagram that clearly depicts the location and direction of the imposed boundary conditions.
• You should specify the three-dimensional magnitude and direction of the applied displacements, forces, pressures, or moments.
• You should describe any constraints used in the model, including the location(s) and the degrees of freedom for each fixed or free constraint.
• You should explain how the components are expected to interact.  We recommend that you provide a description of the interaction (i.e., contact) between the device and other components within the model, as well as those components that self-contact (e.g., stent struts under axial compression).

### B. Assumptions, simplifications, and rationale
You should provide rationale that describes how each imposed condition is appropriate for the relevant aspect of the context of use.  You should describe the sources and/or methods used to obtain the loading mode and magnitude (e.g., literature data, standards, imaging, other analytic methods).

## VIII. Mesh (System Discretization)
### A. Details
We recommend that you provide the following details regarding the mesh.
• Specify the type and number of elements use for the mesh.  Include any mesh refinement or adaptive meshing in transition regions or regions of complex geometry.  We recommend that you provide figures depicting the mesh at relevant scales, especially in transition regions or regions of complex geometry and regions of high stress or strain.
• You should provide details of the mesh refinement or convergence analysis used to demonstrate that the QOI are independent of element size.
− Report the number of mesh densities used to demonstrate convergence stability of the QOI with respect to element size.
− Report the metric(s) of the mesh refinement analysis in graphical or tabular format and clearly identify the mesh chosen for the analysis against the criterion.

### B. Assumptions, simplifications, and rationale
Regarding the mesh refinement study, you should provide rationale for the type of element selected and for the numerical criterion chosen (e.g., principal stress, displacement) to evaluate the mesh density.

## IX. Solver (Numerical Implementation)
We recommend that you provide the following details regarding the software used in the numerical implementation of the analysis.
• You should provide the name (including version number) of the software used to solve the model(s).
• If custom subroutines are used, you should provide information on code verification (e.g., test case) and details of the implementation.
• You should describe the type of analysis completed (e.g., static structural, vibration, buckling).
• You should provide details on the solver routine used including, at a minimum, the following parameters: − state whether the solver is implicit or explicit.  If the latter, include and provide rationale for the analysis time frame, time step size, material(s) density and any mass scaling used − indicate if the solver accounted for nonlinear geometric changes.
− state the convergence criteria and iteration method.

### X. Validation
We recommend that you provide information regarding the methods employed to validate the computational model [1].  The results of a validation study support the choice of the input parameters to the computational model.

You should describe how the validation study supports the context of use of the CM&S study. Specify the QOI(s) from the validation experiment and their relationship to computational model of the validation experiment. We suggest the following format for reporting the validation study.

### A. Details i.
Comparator
You should describe the comparator (e.g., physical test, in vivo study, literature) used for validation.  Include the following: a. mode of loading; b. boundary and loading conditions including the loading and unloading path, as applicable; c. environmental parameters within the experiment (e.g., temperature, humidity); and d. manufacturing processes or pre-conditioning applied to the device prior to conducting the experiment, if applicable.  For example, if the model is designed to predict safety of a nitinol cardiovascular stent, specify if the device was loaded onto a delivery systems and tracked through a representative anatomical model prior to experimental measurements.
You should describe the apparatus used to capture data during the experiment, the level of measurement accuracy and uncertainty.  For example, if the validation study compares uniaxial force-extension data between the computational model and an experiment, present the capacity and accuracy of the load cell used to measure force data.

You should describe the locations on the device or tissue where the experimental measurements were acquired.  For example, if your study is designed to analyze strain in a hip stem, describe where strain gauges were placed to acquire the data.

ii. Computational model of the Validation Setting
You should describe the boundary and loading conditions used for the validation model and describe how they relate to the experimental comparator.  For example, the rate and magnitude of applied torsion to a pedicle screw system in the computational model should match that applied to the device mounted on a mechanical testing system.

You should describe the validation model QOI.  If applicable, describe any post-processing calculations.

Include images that directly compare the validation model and experimental QOIs (e.g., deformation or stress contours) to demonstrate that the computational model is able to capture relevant behavior.

You should present a quantitative comparison of the QOI from the computational model and experimental at relevant steps in the analysis.  For example, if the validation study compared the radial force generated by the stent during the step of being loaded on to the delivery system, it might be more insightful to compare this force at several diameters between nominal and loaded diameter rather than at the final loaded diameter.

### B. Assumptions, simplifications and rationale
You should discuss the relevance of the validation experiment to expected loading conditions as described in the context of use, implications of model and experimental assumptions on the results, limitations on the agreement between the validation model and experiment, and the extent of predictive capability of the general model.

If the validation model parameters are different from those used in the computational model for the context of use, you should provide rationale for the differences.

You should list and discuss the assumptions for the validation model (i.e., neglecting viscous behavior if you are comparing instantaneous force values).

You should list and discuss the simplifications for the validation model.  These simplifications might include geometric, such as axisymmetry, or may consist of explanations for testing device sub-components (e.g., validating the wear scar on articulating components in a total disc replacement device may not necessitate modeling of the device-bone interface).

You should provide a discussion of the extent to which the validation model captures the observed validation experimental behavior and its limitations.

## XI. Results
We recommend that you provide the following for each analysis step: • rationale for the QOI(s) reported (e.g., component, principal, von Mises); • specific values for the QOI(s), along with a detailed description and/or plot demonstrating the loading history of the critical regions; and • a statement about whether the QOI(s) are reported from integration points or nodes. If applicable, provide a contact map which depicts the interactions between contact surfaces and discuss the results.

We recommend that you provide the following for monotonic loading: • a statement and rationale for the failure criterion (e.g., Maximum Shear Stress, Mohr-Coulomb), along with a graphic or equation that clearly demonstrates how factors of safety were calculated; • the QOI values and graphically display the location(s) of the critical stresses, strains, forces, or displacements; and • the safety factors.  For reporting the safety factors: − provide a table that specifies the safety factors for each case (i.e., device size, loading mode(s), and analysis step); and − show locations of minimum safety factor(s) on the device graphically.

We recommend that you provide the following for fatigue evaluation: • a description of the method used to calculate mean and alternating stresses/strains (e.g., scalar, tensor); • a statement on whether cyclic loading results in rotations of the principal directions; • a description of the fatigue criterion (e.g., Goodman, Soderberg), along with a graphic or equation that clearly demonstrates how fatigue factors of safety are calculated; and • the fatigue safety factors.  For reporting fatigue safety factors: − provide a table that specifies the critical mean and alternating stresses/strains and the resulting safety factors for each device size, loading mode(s), and analysis step; − Show locations of minimum safety factor(s) on the device graphically; and − Plot mean and/or alternating stress/strains on a point cloud graph and include fatigue criterion if applicable.

For other analysis types (e.g., vibration or buckling), we recommend that you provide all relevant results including critical stresses or strains and their locations on the device as well as describe any post-processing techniques used to evaluate safety and/or performance.

If multiple loading modes were modeled separately, we recommend that you provide rationale and discuss the implications of superposition of stress or strain states for each loading mode (e.g., location, direction, and phase of the critical stresses or strains).

## XII. Limitations
We recommend that you discuss the major limitations of the computational model identified in Sections II-XI above. Discuss any inconsistencies between the results and the assumptions and simplifications.

If the conclusions of the analysis are significantly dependent on the assumptions and/or simplifications of the computational model, we recommend that you report on a sensitivity analysis of the parameters associated with those assumptions and/or simplifications.

## XIII. Discussion/Conclusion
You should state the overall conclusions of the CM&S study and whether the objective(s) outlined in the context of use have been met.

We recommend that you discuss the results with respect to the context of use.  For example, discuss how critical stresses or strains obtained from the computational model relate to failure locations observed in bench testing and/or the potential consequences of failure at locations of minimum safety factor.

## XIV. References
Please provide a list of the appropriate references used to support the CM&S study.


Bibliography

[1] ASME V&V10-2006, Guide for Verification and Validation in Computational Solid Mechanics Subject Matter Appendix III – Computational Electromagnetics and Optics

For questions regarding this appendix, contact Leonardo Angelone, Ph.D., at (301) 796-2595 for computational electromagnetics or Quanzeng Wang, Ph.D. at (301) 796-2612 for computational optics, or both at rrcm@fda.hhs.gov.


Introduction/Scope of the Appendix
The purpose of this appendix is to provide recommendations to industry on the formatting, organization, and content of the reports for computational electromagnetic (EM) and optical modeling and simulation studies used in medical device regulatory submissions to assess (1) safety (e.g., energy deposition, temperature rise, voltages, and thermal damage induced in the human body by medical devices using EM/optical energy) and (2) effectiveness (e.g., how internal or external EM/optical sources and physical properties of devices and tissue affect the effectiveness) of medical devices.

Examples of such studies include safety and effectiveness evaluation of the following medical devices: electrophysiology monitoring devices, magnetic resonance imaging (MRI) systems, magnetic resonance (MR) Conditional passive or active implanted devices (e.g., orthopedic devices, stents, pacemakers, or neurostimulators), devices for radiofrequency ablation, optical diagnostic devices (e.g., optical coherence tomography devices, fluorescence spectroscopy devices), and optical therapeutic devices (e.g., laser surgery devices).

Outline of the Report
In the following section, we provide an outline for reporting the details of your computational modeling and simulation study.

### I. Executive Report Summary
We recommend that you provide a concise and complete overview of the report of the CM&S study that includes the following: • Context of use of the CM&S study, including any relevance/correlation to other studies (e.g., bench, clinical) for validation purposes • Type of the analysis (e.g., photobiological safety, MRI safety, spectroscopy device penetration depth)
• Scope of the analysis (e.g., for a device that has multiple sizes or configurations, discuss what sizes or configurations were modeled, and how the computational model and simulation relates to the intended patient population)
• Conclusions with respect to the context of use and how they relate to the regulatory submission.
• Keywords - please provide up to five keywords or key phrases that describe the modeling modality, the device product code, any relevant materials of the device analysis type, and if applicable, location in the body for intended use (e.g., radiofrequency dosimetry, OQG, cobalt chromium, magnetic resonance safety, hip).  The following are sample keywords relevant to this subject matter that can be used: − electrophysiology, radiofrequency, optical imaging, laser therapy, magnetic resonance imaging, active implants, Monte Carlo simulation, finite difference time domain

## II. Background/Introduction
We recommend that you provide a brief description of the device system and intended use environment.  Describe the purpose of the analysis, as this will dictate the relevant details necessary for review.  Introduce the background and principles of the model and simulation, and provide rationale for why it is appropriate to apply the model to the device system.

## III. Code Verification
We recommend that you provide a brief description of the software quality assurance (SQA) and numerical code verification (NCV) that you performed on the software used for the CM&S study.  Software tools include off-the-shelf, modified-off-the-shelf, or user-developed.  Code verification is important, regardless of the software type.

### A. Details
You should briefly describe the code verification activities.  You may reference available documentation and verification results from the software developer.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the applicability of the verified code to your computational domain.  If applicable, describe and rationalize the differences between the code used for verification and the code used for the context of use.
Moreover, You should provide rationale to support the selection of the numerical settings, either default or modified.

Note that the details regarding calculation verification, the other component to the verification process, are provided in Section VIII System Discretization and Section IX Numerical Implementation, respectively

## IV. System Geometry (System Configuration)
We recommend that you provide information regarding the device and tissue geometry that was modeled (e.g., the geometry of the device, the computational domain, the in vivo or in vitro test that is modeled).

### A. Details
You should describe the components of the system (e.g., device, in vivo or in vitro environment) to be evaluated.  Include images, diagrams (with appropriate scaling bar or dimensions), and a brief description of the model.

You should describe the methods (e.g., image reconstruction, computer aided design) used to generate the system configuration and discuss how the configuration was captured appropriately for the intended analysis. If image reconstruction was used to generate geometry, describe the imaging modality.

You should describe the software used to generate the system configuration (e.g., computer aided design software, image segmentation software) and describe the methods used to verify the software.

You should describe the geometrical characteristics necessary for a comprehensive description of the methodology.

Because there are different applications of computational EM and optical modeling, we have provided the following examples.

1. For EM simulations in MRI environment, please describe: • the geometrical and physical characteristics of the radiofrequency coils (e.g., geometrical dimensions, number of rungs, number of sources, lumped elements used, tuning/matching elements, if any) and their clinical significance; • the physical characteristics of the phantom/anatomical models (e.g., size, dimensions, posture, body mass index, and number of anatomical structures) used in the simulations and their clinical significance with respect to the indications of use; • the landmark positions of the phantom/anatomical models with respect to the coil and their clinical significance; • the geometrical and physical characteristics of the device (e.g., material properties, path of the implant inside anatomical model) and their clinical significance.
2. For optical simulations, please describe: • the geometrical and physical characteristics of the light source, such as the distance and angle between the light source and tissue surface, the beam size, and beam intensity profile (e.g., Gaussian beam). Describe whether and how the illumination takes into consideration of specific optical components, such as fiber optic probes, lenses or mirrors; • the geometrical and physical characteristics of the detector, such as the detected wavelength range, the aperture used to select optical signal, spatial and angular restrictions on detected light, as well as the justification for these restrictions (or lack of restrictions); • the geometrical characteristics of the simulated tissue (e.g., size of simulated region, mesh density for simulation, surface morphology, and tissue structures such as layers, vessels, tumors or cysts) and the rationale for implementation of this geometry (e.g., tissue types represented, layers or structures present, and simulated conditions such as normal, metaplastic or neoplastic tissue).

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to generate the system configuration (e.g., excluding static field magnet or gradient field coil in MRI RF models, assuming the tissue has a flat interface between two layers in the model) as compared to the actual device, tissue object, and environment.  If appropriate, provide clinical rationale for the in vivo/in vitro models (e.g., size, disease state, mathematical convenience versus clinical relevance).

### V. Governing Equations/Constitutive Laws
We recommend that you provide information regarding the governing equations and/or constitutive laws used to perform the computational analysis.

### A. Details
You should provide the governing equations/constitutive laws for the system.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications of the governing equations (e.g., Laplace, Maxwell, Radiative Transport) or constitutive laws chosen to represent the system.  If a thermal analysis is included, please report the results as recommended in Appendix V Computational Heat Transfer.

## VI. System Properties
We recommend that you provide information regarding the relevant system properties (e.g., biological, chemical, physiological, physical).

### A. Details
You should provide the parameters used in the analysis that define the material and/or process characteristics, and their variability, if applicable.  These might include properties of biological materials (e.g., cells, tissues, organs), non-biological materials (device components, implants, contrast agents), and/or processes (e.g., cell signals), such as states (e.g., diseased, healthy), biological properties, chemical properties, and physical properties.  Identify the source of biological, chemical, and physical properties (e.g., literature, in vivo, in vitro testing).

Specifically please provide the following inputs, when appropriate for your simulation.
1. For EM simulations, provide electrical properties of the device (e.g., conductivity, permittivity), the tissue (e.g., conductivity, permittivity, anisotropy), and any relevant, nonbiological materials (e.g., air, water, high-dielectric pads surrounding the body).
2. For optical simulations, • provide optical properties of the device (e.g., refractive index of probe surface, numerical aperture, beam convergence or divergence, focal spot size), the tissue or non-tissue object (e.g., absorption coefficient, scattering coefficient, refractive index, scattering anisotropy, quantum yield for fluorescence), and any relevant, non-biological materials (e.g., contrast agents, nanoparticles), along with their variation in space and time (e.g., different tissue components, dynamic changes due to temperature or hydration); • describe any simplifications of the optical properties (e.g., phase function) for the tissue and any relevant, non-biological materials (probes, nanoparticle or dye-based contrast agents)  and state whether a diffusion condition was assumed; • provide the key properties of the optical radiation simulated, including the spectral distribution of irradiance, total energy and/or power, spatial intensity distribution, and angular illumination distributions; • state whether or not coherence, polarization and fluorescence were considered.
3. For simulations that also include thermal analysis, • provide the system properties of the object (tissues and non-tissue) used for the simulations (e.g., mass density, thermal conductivity, capacitance, blood perfusion rate, Arrhenius thermal damage coefficients, electrical conductivity and permittivity); • provide data (e.g., equation, table or graph) describing any assumed temperature dependence; • specify any non-linear or coupling between EM/optical and thermal models.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the system properties.  If the properties are derived from literature data, please provide a reference to the publications and discuss their applicability to the specific study (e.g. ex-vivo vs. in-vivo).  If the properties are derived from bench testing, please provide a full and comprehensive report of the test.

You should describe any assumptions made with respect to the variation of the object system (tissue or non-tissue) properties with position, direction, time, wavelength, light intensity, temperature, and thermal damage.  Please describe any assumptions made with respect to the nonlinearity of system properties incorporated in the model and whether they may affect the modeling results.  Please specify any spatial heterogeneity, including anisotropy, and any time dependence.  Please describe the sensitivity of outcome results on key parameters and provide a systematic analysis of data uncertainty in relation to system properties.

## VII. System Conditions
We recommend that you provide information regarding the conditions that were imposed on the system.  These might include, but are not limited to, the boundary and loading conditions, initial conditions, and other constraints that control the system.
### A. Details
You should describe the system conditions imposed on the model and their variability, if applicable.  If appropriate, provide a graphical representation of the conditions, depicting how they are applied to the system.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the conditions applied on the system.  Provide appropriate documentation (e.g., literature, test reports, clinical data, medical imaging data) to support the system conditions.

Specifically, state whether the boundary conditions of the simulations represent a true physical boundary.  You should provide evidence demonstrating that boundary conditions do not cause the simulation to generate non-physical results.  Moreover, where relevant, you should describe how the physical properties of surrounding materials between device and tissue (e.g., air, water) will affect the boundary conditions and how the boundary condition will in turn affect the simulation results.

For simulations of optical systems with the purpose of calculating light intensity or energy delivered to human tissue, you should provide information on all the assumptions made to model each optical element.  For example, light intensity or energy attenuated by each optical element due to reflection, absorption, and scattering at certain wavelength or incident angle, should be specified to properly obtain light intensity and energy delivered to the human tissue.

## VIII. System Discretization
We recommend that you provide information regarding the discretization and refinement techniques applied to the system for solving it numerically.

### A. Details
You should describe the system discretization methods and how they were applied to the computational domain.  Describe the methodology (e.g., mesh refinement study) used to verify proper numerical discretization.  If applicable, provide a representative image of the discretization in the areas of interest of the computational domain.
Report the criteria used to determine that the discretization was sufficient to resolve the physics of interest.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the assumptions and simplifications used to discretize the computational domain.

## IX. Numerical Implementation
We recommend that you provide information regarding the numerical implementation strategy that yielded the solution to the governing equations.
### A. Details
You should describe the numerical implementation methodology (e.g., boundary element method, finite difference time domain, methods of moments, finite element method, and Monte Carlo simulation) and numerical solver employed to yield the solution to the governing equation.  Explain the calculation verification process used to ensure the governing equations were solved correctly.  State the solver parameters (e.g., tolerance, relaxation) and convergence criteria, and describe any stability criteria required.  For integral models (e.g., Arrhenius equation), discuss the method of numerical integration.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the assumptions and simplifications used to choose the solver and associated parameters. Specifically, please provide rationale  quantitative analysis demonstrating that the parameters selected are sufficient to achieve a convergent solution appropriate for the context of use, specify the convergence criteria and describe why it was appropriate (e.g., time-steps used for finite difference time domain; simulation stopping criteria such as number of photons for Monte Carlo simulation).

### X. Validation
We recommend that you provide information regarding the methods employed to validate the computational model [1].

### A. Details
You should describe the method used to assess the predicative capability of the computational model (e.g., in vivo or in vitro comparator) for the context of use.  You should provide sufficient details that describe how the measurements were taken from the comparator and post-processing of the computational model, and used to assess the accuracy of the predicted numerical output.  For example, validation for RF simulations in MRI may be conducted with respect to B1 field, validation for optical modeling might be conducted with respect to detected light intensity, and validation for optical/thermal or radiofrequency/thermal modeling might be conducted with respect to temperature or thermal damage.  Please demonstrate that the error level provides sufficient accuracy for the given application. If an analytical closed-form equation is used to support the validation, please provide the source of the equation.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the assumptions and simplifications of the method used to validate the computational model.  Explain the difference between the measured and predicted value, and discuss its significance with respect to the purpose of the analysis.

## XI. Results
We recommend that you present the quantitative results from the computational modeling study.  You should provide the results with sufficient level of details, including labels and legends.  The results may be presented in more than one format (e.g., tables, graphs, plots).

## XII. Discussion
We recommend that you discuss how the results relate to the purpose of the computational modeling study and the clinical relevance, if appropriate, and how the results compare with the experimental and literature results.

## XIII. Limitations
We recommend that you provide details regarding (1) how the assumptions and simplifications described in the previous sections might affect the output of the computational model and simulation, (2) the interpretation of the results, and (3) the relevance to the purpose of the study.  Describe the outcomes and implications of the uncertainty analysis performed on the system properties and conditions.

## XIV. Conclusions
We recommend that you summarize the computational study with respect to the purpose of the study and how it relates to the regulatory submission.

## XV. References
You should provide a list of the appropriate references used to support the CM&S study.


Bibliography

[1] IEEE 1597.1-2008 - IEEE Standard for Validation of Computational Electromagnetics Computer Modeling and Simulations Subject Matter Appendix IV – Computational Ultrasound

For questions regarding this appendix, contact Joshua Soneson, Ph.D. at (301) 796-2512 or at rrcm@fda.hhs.gov.


Introduction/Scope of the Appendix
The purpose of this appendix is to provide recommendations on the formatting, organization, and content of reports for studies in computational ultrasound in support of device submissions.

Outline of the Report
In the following section, we provide an outline for reporting the details of your computational modeling and simulation study.

### I. Executive Report Summary
We recommend that you provide a concise, high-level overview of the assumptions and rationale for the methodology/modeling approach, and the following: • Context of use of the CM&S study including a clear identification of the quantity(s) of interest and describe any relevance/correlation to bench testing for validation purposes • Describe the type(s) of analysis(es) conducted in the computational modeling study (e.g., wave propagation, heat transfer, fluid flow, thermal dose)
• State whether the analysis software is open-source, commercial, or developed in-house • Keywords - please provide up to five keywords or key phrases that describe the modeling modality, the device product code, any relevant materials of the device, analysis type, and if applicable, location in the body for intended use (e.g., finite difference method, KZK, ultrasound, hystotripsy, prostate).  For example, the following are sample keywords relevant to this subject matter that can be used: − imaging, cavitation, therapeutic ultrasound, histotripsy, acoustic radiation force impulse, Sommerfeld integral, Rayleigh integral, Westervelt, KZK.

## II. Background/Introduction
We recommend that you provide a brief device description along with its intended use environment, deployment/implantation procedure and patient population, as appropriate.
Additionally, describe the purpose and scope of the analysis, as this will dictate the relevant details necessary for review.  The details provided in this section should correspond to the objectives of your analysis.

## III. Code Verification
We recommend that you provide a brief description of the software quality assurance (SQA) and numerical code verification (NCV) that you performed on the software used for the CM&S study.  Software tools include off-the-shelf, modified-off-the-shelf, or user-developed.  Code verification is important, regardless of the software type.

### A. Details
You should briefly describe the code verification activities.  You may reference available documentation and verification results from the software developer.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the applicability of the verified code to your computational domain.  If applicable, describe and rationale for differences between the code used for verification and the code used for the context of use.
Moreover, provide rationale to support the selection of the numerical settings, either default or modified.

Note that the details regarding calculation verification, the other component to the verification process, are provided in System Discretization and Numerical Implementation, sections VIII and IX, respectively.

## IV. System Geometry (System Configuration)
We recommend that you provide details regarding the device and/or tissue geometry that was modeled.  The configuration defines the geometry of the device, computational domain and the anatomical structure included within the computational domain.

### A. Details
You should describe the components of the system (e.g., device, in vivo and/or in vitro environment) to be evaluated.

Regarding the ultrasound source, you should include images, diagrams (with appropriate scaling bar or dimensions), and a brief description of the model(s).
Specifically, discuss whether the ultrasound source is a spherical bowl or phasedarray transducer.  If it is the latter, include a scaled diagram indicating the arrangement of the elements.  Finally, provide the dimensions of the device and its geometry.

Regarding the anatomy, you should describe the methods (e.g., image reconstruction) used to generate the simulated anatomy and discuss the techniques used to demonstrate that the configuration was captured appropriately for the intended analysis, if applicable.  For example, if bone is included in the computational domain, describe how it was modeled.  If blood vessel are included in the computational domain, describe the blood vessels that were modeled and represented (e.g., statistically versus simulating a single representative geometry).  Indicate how other anatomical features are included.  Finally, describe any scaling or similarities used in the modeling approach.
### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to generate the system configuration as compared to the actual device and environment.  If the entire device system was not modeled or if simplifications were made to the geometry, then provide rationale for the system geometry that was analyzed (e.g., use of symmetry).  You should describe the difference between the model and the real situation as it pertains to the purpose of the computational modeling study.  For example, if bones are present, describe if the shear-wave propagation (and heating due shear-wave absorption) was modeled.  Indicate the transducer apodization.  If integral methods are used, discuss how acoustic diffraction affects the solution.  Additionally, as manufacturing tolerances can affect device functionality, describe how the range of design and manufacturing tolerance dimensions influence the results compared to nominal dimensions.

### V. Governing Equations
We recommend that you provide information regarding the governing equations used to perform the computational analysis.

### A. Details
You should describe the basic equations used in the simulation.  Specifically, state whether the propagation model is full-wave or parabolic, and linear or nonlinear.  For nonlinear or broadband modeling, discuss the frequency dependence of acoustic attenuation.  Indicate whether the pressure wave or displacement wave is modeled, and whether shear waves are taken into account.  If acoustic streaming, mechanical, and/or thermal effects are included, discuss the coupling of the system.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications of the basic mathematical equations that were implemented for the model and simulation, specifically regarding the type of propagation model employed.

## VI. System Properties
We recommend that you provide, preferably in tabular format, all physical properties, coefficients, descriptive equations used in the simulation and post processing.

### A. Details
We have provided the following as an example of how to report the system properties.

Tissue properties Property Numerical value Unit Small signal sound speed


Mass density


Absorption


Coefficient of nonlinearity Heat capacity


Thermal conductivity


Perfusion rate



Transducer characteristics



We recommend that you indicate the dependence of properties on other variables, such as temperature, frequency, thermal dose and location, if included.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the system properties.  Identify the sources of the physical properties and coefficients adopted (e.g., literature, in vivo, ex vivo, in vitro testing).

If literature data are cited and the data are condition-specific, discuss their applicability to the model.  If testing is conducted to determine the parameters, you should describe describe the test methods and results as applicable to the model.

If there are uncertainties associated with the data (i.e., due to accuracies, simplifications, or variations), perform a sensitivity analysis, if appropriate, to address the effect of the uncertainties on the simulation results.

## VII. Boundary & Initial Conditions (System Conditions)
We recommend that you provide a complete description of the initial and boundary conditions that are imposed on the model.  These include, but are not limited to, absorbing boundaries and transducer loading.  If absorbing boundaries are used, discuss the details of the implementation and show their effectiveness.  You should provide a rationale for the choice of the initial/boundary conditions and if appropriate, provide a graphical representation of the conditions, depicting how they are applied to the system.

## VIII. System Discretization
We recommend that you provide the following details regarding the spatial discretization.

### A. Details
You should describe the spatial discretization method and, if applicable, the technique used to integrate the evolution variable.  If complex geometry requires the use of a non-uniform mesh, provide images/diagrams of the mesh.  Additionally, you should indicate the details of the mesh.  Specifically, Characteristic Numerical value Unit Acoustic power


Frequency


Pressure/phase distribution • you should describe and provide rationale for the quality of the mesh (e.g., element/cell types, sizes, shapes, quality metrics (e.g., aspect ratios) and formulations chosen for the production mesh for the analysis domain); and.
• you should discuss mesh refinement in areas of interest, for example, where the field changes rapidly in space.
If adaptive meshing refinement techniques were employed, then you should discuss the methods and provide details regarding the finished mesh.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the assumptions and simplifications used to discretize the computational domain and, if applicable, the integration scheme. Perform a convergence analysis (solution as a function of mesh density) and provide details that demonstrate that discretization adequately resolved the physics of interest.

## IX. Numerical Implementation
We recommend that you provide the following details regarding the software used in the numerical implementation of the analysis.  For models using differential equations, discuss the method used to solve the discrete equations.  For integral models, discuss the method of numerical integration.  You should provide a rationale for the choice of the methods used and possible effects on the solution.  Finally, you should describe and provide rationale for any techniques used to accelerate the computation, such as neglecting terms in regions where they have subleading order, adaptive time-stepping or variable number of harmonics.

### X. Validation
We recommend that you provide information regarding the methods employed to validate the computational model.  Specifically, you should describe the method(s) used to assess the predictive capability of the computational model with appropriate bench methods, conserved quantities and known analytical solutions.  You should provide diagrams and data to support the assessment of the model.  You should provide details on how the measurements were taken from the bench test and compared to the computational model.
Discuss any differences between bench testing/known solutions and results from the computational model.

## XI. Results
We recommend that you present the quantitative results from the computational modeling study over the range of intended use parameters.  You should provide the results with a sufficient level of details, including labels and legends.  The results may be presented in more than one format (e.g., table, graph, plot).

## XII. Discussion
We recommend that you discuss how the results relate to the context of use of the CM&S study, and if appropriate the clinical relevance and how the results compare with experimental and literature results, if these results exist.
## XIII. Limitations
Describe the assumptions/simplifications made in the model generation, simulation and analysis.  Discuss how those assumptions/simplifications might affect the output of the model and the interpretation of its relevance to the device and safety.  You should describe the outcomes and implications of all the available uncertainty analyses performed on the system properties and conditions.

## XIV. Conclusions
We recommend that you summarize the CM&S study with respect to the context of use and how it relates to the regulatory submission.

## XV. References
You should provide a list of the appropriate references used to support the CM&S study.
Subject Matter Appendix V –
Computational Heat Transfer

For questions regarding this appendix, contact Joshua Soneson, Ph.D. at (301) 796-2512 or at rrcm@fda.hhs.gov.


Introduction/Scope of the Appendix
The purpose of this appendix is to provide recommendations on the formatting, organization, and content of reports for studies in computational heat transfer in support of device submissions.

Outline of the Report
In the following section, we provide an outline for reporting the details of your computational modeling and simulation study.

### I. Executive Report Summary
We recommend that you provide a concise, high-level overview of the assumptions and rationale for the methodology/modeling approach, and the following: • Context of use of the CM&S study including a clear identification of the quantity(s) of interest and describe any relevance/correlation to bench testing for validation purposes • Describe the type(s) of analysis(es) conducted in the computational modeling study (e.g., radiation or conduction heat transfer, fluid flow, chemical reaction, EM or acoustic absorption)
• State whether the analysis software is open-source, commercial, or developed in-house • Keywords - please provide up to five keywords or key phrases that describe the modeling modality, the device product code, any relevant materials of the device, analysis type, and if applicable, location in the body for intended use (e.g., finite difference method, MNB, heat conduction, thermal ablation, uterus).  For example, the following are sample keywords relevant to this subject matter that can be used: − thermal diffusivity, source, diffusion equation, heat capacity, radiation, conduction.

## II. Background/Introduction
We recommend that you provide a brief device description along with its intended use environment, deployment/implantation procedure and patient population, as appropriate.
Additionally, you should describe the purpose and scope of the analysis, as this will dictate the relevant details necessary for review.  The details provided in this section should correspond to the objectives of your analysis.

## III. Code Verification
We recommend that you provide a brief description of the software quality assurance (SQA) and numerical code verification (NCV) that you performed on the software used for the CM&S study.  Software tools include off-the-shelf, modified-off-the-shelf, or user-developed.  Code verification is important, regardless of the software type.

### A. Details
You should briefly describe the code verification activities.  You may reference available documentation and verification results from the software developer.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the applicability of the verified code to your computational domain.  If applicable, describe and rationale for differences between the code used for verification and the code used for the context of use.
Moreover, provide rationale to support the selection of the numerical settings, either default or modified.

Note that the details regarding calculation verification, the other component to the verification process, are provided in System Discretization and Numerical Implementation, sections VIII and IX, respectively.

## IV. System Geometry (System Configuration)
We recommend that you provide details regarding the device and/or tissue geometry that was modeled.  The configuration defines the geometry of the device, computational domain and the anatomical structure included within the computational domain.

### A. Details
You should describe the components of the system (e.g., device, in vivo and/or in vitro environment) to be evaluated.

Regarding the heat source, you should include images, diagrams (with appropriate scaling bar or dimensions) and a brief description of the model(s).  Additionally, provide dimensions of device and geometry.

Regarding the anatomy, you should describe the methods (e.g., image reconstruction) used to generate the simulated anatomy and discuss the techniques used to demonstrate that the configuration was captured appropriately for the intended analysis, if applicable.  Finally, describe any scaling or similarities used in the modeling approach.

You should describe the methods for quantifying temperature-induced bioeffects such as phase change or thermal damage.
### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to generate the system configuration as compared to the actual device and environment.  If the entire device system was not modeled or if simplifications were made to the geometry, then provide rationale for the system geometry that was analyzed (e.g., use of symmetry).  You should describe the difference between the model and the real situation as it pertains to the purpose of the computational modeling study.  Additionally, as manufacturing tolerances can affect device functionality, describe how the range of design and manufacturing tolerance dimensions influence the results compared to nominal dimensions.


### V. Governing Equations
We recommend that you provide information regarding the governing equations used to perform the computational analysis.

### A. Details
You should describe the basic equations used in the simulation.  Specifically, state whether materials are isotropic and if not, describe how anisotropy is addressed.  You should describe the coupling to other physical processes (i.e., fluid flow, heat sources in domain or on boundary) that were included in the model.

### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications of the basic mathematical equations that were implemented for the model and simulation, as well as the methods for quantifying thermal damage.

## VI. System Properties
We recommend that you provide, preferably in tabular format, all physical properties, coefficients and descriptive equations used in the simulation and post processing.

### A. Details
We have provided the following as an example of how to report the system properties.

Tissue properties Property Numerical value Unit Mass density


Heat capacity


Thermal conductivity


Perfusion rate



We recommend that you indicate the dependence of properties on other variables, such as temperature, frequency, thermal damage and location, if included.
### B. Assumptions, simplifications, and rationale
You should describe and provide rationale for the assumptions and simplifications used to determine the system properties.  Identify the sources of the physical properties and coefficients adopted (e.g., literature, in vivo, ex vivo, in vitro testing).

If literature data are cited and the data are condition specific, you should discuss their applicability to the model.  If testing is conducted to determine the parameters, you should describe the test methods and results as applicable to the model.

If there are uncertainties associated with the data (i.e., due to accuracies, simplifications or variations), perform sensitivity analysis, if appropriate, to address the effect of the uncertainties on the simulation results.

## VII. Boundary & Initial Conditions (System Conditions)
We recommend that you provide a complete description of the initial and boundary conditions that are imposed on the model.  You should provide rationale for the choice of the initial/boundary conditions and if appropriate, provide a graphical representation of the conditions, depicting how they are applied to the system.

## VIII. System Discretization
We recommend that you provide the following details regarding the spatial discretization.

### A. Details
You should describe the spatial discretization method and, if applicable, the technique used to integrate the evolution variable.  If complex geometry requires the use of a non-uniform mesh, provide images/diagrams of the mesh.  Additionally, indicate the details of the mesh.  Specifically, you should: • describe and provide rationale for the quality of the mesh (e.g., element/cell types, sizes, shapes, quality metrics (e.g., aspect ratios) and formulations chosen for the production mesh for the mesh of the analysis domain); and.
• discuss mesh refinement in areas of interest, for example, where the field changes rapidly in space.
If adaptive meshing refinement techniques were employed, then you should discuss the methods and provide details regarding the finished mesh.

### B. Assumptions, simplifications and rationale
You should describe and provide rationale for the assumptions and simplifications used to discretize the computational domain and, if applicable, the integration scheme. You should perform a convergence analysis (solution as a function of mesh density), a stability analysis where applicable, and provide details that demonstrate that the discretization adequately resolved the physics of interest.

## IX. Numerical Implementation
We recommend that you provide the following details regarding the software used in the numerical implementation of the analysis.  For models using differential equations, discuss the method used to solve the discrete equations.  For integral models, discuss the method of numerical integration.  You should provide a rationale for the choice of the methods used and possible effects on the solution.  Finally, you should describe and provide rationale for any techniques used to accelerate the computation, such as neglecting terms in regions where they have subleading order, adaptive stepping, etc.

### X. Validation
We recommend that you provide information regarding the methods employed to validate the computational model.  Specifically, you should describe the method(s) used to assess the predictive capability of the computational model with appropriate bench methods, conserved quantities and known analytical solutions.  Provide diagrams and data to support the assessment of the model.  Provide details on how the measurements were taken from the bench test and compared to the computational model.  Discuss any differences between bench testing/known solutions and results from the computational model.

## XI. Results
We recommend that you present the quantitative results from the computational modeling study over the range of intended use parameters.  You should provide the results with sufficient level of details, including labels and legends.  The results may be presented in more than one format (e.g., table, graph, plot).


## XII. Discussion
We recommend that you discuss how the results relate to the context of use of the CM&S study, and if appropriate the clinical relevance and how the results compare with experimental and literature results, if these results exist.

## XIII. Limitations
You should describe the assumptions/simplifications made in the model generation, simulation and analysis.  Discuss how those assumptions/simplifications might affect the output of the model and the interpretation of its relevance to the device and safety.
Describe the outcomes and implications of all the available uncertainty analyses performed on the system properties and conditions.

## XIV. Conclusions
We recommend that you summarize the CM&S study with respect to the context of use and how it relates to the regulatory submission.

## XV. References
You should provide a list of the appropriate references used to support the CM&S study.
