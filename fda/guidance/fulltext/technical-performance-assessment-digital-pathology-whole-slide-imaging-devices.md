# Technical Performance Assessment of Digital Pathology Whole Slide Imaging Devices : Guidance for Industry and Food and Drug Administration Staff

**Source:** [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/technical-performance-assessment-digital-pathology-whole-slide-imaging-devices](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/technical-performance-assessment-digital-pathology-whole-slide-imaging-devices)

**Published:** 2016-04-20

---

<!-- Page 1 -->
Contains Nonbinding Recommendations 
 
Technical Performance Assessment 
of Digital Pathology Whole Slide 
Imaging Devices 
 
 
Guidance for Industry and Food 
and Drug Administration Staff 
Document issued on: April 20, 2016 
The draft of this document was issued on February 25, 2015 
For questions about this document, contact the Division of Molecular Genetics and 
Pathology at 301-796-6179 and Nicholas Anderson at 301-796-4310 or 
nicholas.anderson@fda.hhs.gov or Aldo Badano at 301-796-2534 or 
aldo.badano@fda.hhs.gov. 
U.S. Department of Health and Human Services 
Food and Drug Administration 
Center for Devices and Radiological Health 
 
Office of In Vitro Diagnostics and Radiological Health 
Division of Molecular Genetics and Pathology 
Molecular Pathology and Cytology Branch

---

<!-- Page 2 -->
Contains Nonbinding Recommendations 
Preface 
Public Comment 
You may submit electronic comments and suggestions at any time for Agency 
consideration to http://www.regulations.gov . Submit written comments to the Division of 
 
Dockets Management, Food and Drug Administration, 5630 Fishers Lane, Room 1061, 
(HFA-305), Rockville, MD 20852. Identify all comments with the docket number [FDA-
2015-D-0230]. Comments may not be acted upon by the Agency until the document is next 
revised or updated. 
Additional Copies 
Additional copies are available from the Internet.  You may also send an e-mail request to 
CDRH-Guidance@fda.hhs.gov to receive a copy of the guidance.  Please use the document 
number 1400053 to identify the guidance you are requesting.

---

<!-- Page 3 -->
Contains Nonbinding Recommendations 
Table of Contents 
I. 
Introduction ................................
 
............................................................................... 1
II. 
Background ............................................................................................................... 2
III. 
Scope ......................................................................................................................... 2
IV. 
Policy ......................................................................................................................... 3
IV(A). 
Description and Test Methods for Each Component .................................... 3
IV(A)(1). 
Slide Feeder........................................................................................... 5
IV(A)(1)(a). Description .................................................................................... 5
IV(A)(2). 
Light Source .......................................................................................... 5
IV(A)(2)(a). Description .................................................................................... 5
IV(A)(2)(b). Test Method.................................................................................. 6
IV(A)(3). 
Imaging Optics ...................................................................................... 6
IV(A)(3)(a). Description .................................................................................... 6
IV(A)(3)(b). Test Methods ................................................................................ 7
IV(A)(4). 
Mechanical Scanner Movement ............................................................ 7
IV(A)(4)(a). Description .................................................................................... 7
IV(A)(4)(b). Test Method.................................................................................. 8
IV(A)(5). 
Digital Imaging Sensor .......................................................................... 8
IV(A)(5)(a). Description .................................................................................... 8
IV(A)(5)(b). Test Methods ................................................................................ 8
IV(A)(6). 
Image Processing Software ................................................................... 9
IV(A)(6)(a). Description .................................................................................... 9
IV(A)(6)(b). Resources ...................................................................................... 9
IV(A)(7). 
Image Composition ............................................................................... 9
IV(A)(7)(a). Description .................................................................................... 9
IV(A)(7)(b). Test Methods .............................................................................. 10
IV(A)(8). 
Image Files Formats ............................................................................ 10
IV(A)(8)(a). Description .................................................................................. 10
IV(A)(9). 
Image Review Manipulation Software ................................................ 11
IV(A)(9)(a). Description .................................................................................. 11
IV(A)(9)(b). Resources .................................................................................... 11

---

<!-- Page 4 -->
Contains Nonbinding Recommendations 
IV(A)(10). Computer Environment ...................................................................... 11
IV(A)(10)(a). Description ................................................................................ 11
IV(A)(11). Display ............................................................................................... 12
IV(A)(11)(a). Description ................................................................................ 12
IV(A)(11)(b). Test Methods ............................................................................ 12
IV(A)(11)(c). Resources .................................................................................. 13
IV(B). 
System-level Assessment ............................................................................ 14
IV(B)(1). 
Color Reproducibility .......................................................................... 15
IV(B)(1)(a). Description .................................................................................. 15
IV(B)(1)(b). Test Methods ............................................................................... 15
IV(B)(1)(c). Resources .................................................................................... 16
IV(B)(2). 
Spatial Resolution ................................................................................ 16
IV(B)(2)(a). Description .................................................................................. 16
IV(B)(2)(b). Test Methods ............................................................................... 16
IV(B)(3). 
Focusing Test ....................................................................................... 16
IV(B)(4). 
Whole Slide Tissue Coverage.............................................................. 17
IV(B)(4)(a). Description .................................................................................. 17
IV(B)(4)(b). Test Method ................................................................................ 17
IV(B)(5). 
Stitching Error ..................................................................................... 18
IV(B)(5)(a). Description .................................................................................. 18
IV(B)(5)(b). Test Methods ............................................................................... 18
IV(B)(6). 
Turnaround Time ................................................................................. 19
IV(B)(6)(a). Description .................................................................................. 19
IV(C). 
User Interface .............................................................................................. 19
IV(C)(1). 
Description........................................................................................... 19
IV(C)(2). 
Test Methods ....................................................................................... 19
IV(C)(3). 
Resources ............................................................................................. 22
IV(D). 
Labeling ...................................................................................................... 22
IV(D)(1). 
Test Methods ....................................................................................... 23
IV(D)(2). 
Resources ............................................................................................. 23
IV(E). 
Quality Control ........................................................................................... 23

---

<!-- Page 5 -->
Technical Performance Assessment 
1 
 
1
of Digital Pathology Whole Slide 
2
Imaging Devices 
3
4
Guidance for Industry and Food 
5
and Drug Administration Staff 
6
7
This guidance represents the current thinking of the Food and Drug Administration 
8
(FDA or Agency) on this topic.  It does not establish any rights for any person and is 
9
not binding on FDA or the public.  You can use an alternative approach if it satisfies 
10
the requirements of the applicable statutes and regulations.  To discuss an alternative 
11
approach, contact the FDA staff or Office responsible for this guidance as listed on the 
12
title page.  
13
14
I. 
Introduction  
15
16
FDA is issuing this guidance to provide industry and agency staff with recommendations 
17
regarding the technical performance assessment data that should be provided for 
18
regulatory evaluation of a digital whole slide imaging (WSI) system.  This document 
19
does not cover the clinical submission data that may be necessary to support approval or 
20
clearance.  This document provides our suggestions on how to best characterize the 
21
technical aspects that are relevant to WSI performance for their intended use and 
22
determine any possible limitations that might affect their safety and effectiveness.   
23
24
Recent technological advances in digital microscopy, in particular the development of 
25
whole slide scanning systems, have accelerated the adoption of digital imaging in 
26
pathology, similar to the digital transformation that radiology departments have 
27
experienced over the last decade.  FDA regulates WSI system manufacturers to help 
28
ensure that the images intended for clinical uses are reasonably safe and effective for 
29
such purposes.  Essential to the regulation of these systems is the understanding of the 
30
technical performance of the WSI system and the components in the imaging chain, from 
31
image acquisition to image display and their effect on pathologist’s diagnostic 
32
performance and workflow.  Prior to performing non-technical analytical studies (i.e., 
33
those using clinical samples) and clinical studies to evaluate a digital imaging system’s 
34
performance, the manufacturer should first determine the technical characteristics that are 
35
relevant to such performance for its intended use and determine any possible limitations 
36

---

<!-- Page 6 -->
Contains Nonbinding Recommendations 
 
that might affect its safety and effectiveness.  This guidance provides recommendations 
2 
 
37
for the assessment of technical characteristics of a WSI device. 
38
39
FDA's guidance documents, including this guidance, do not establish legally enforceable 
40
responsibilities.  Instead, guidances describe the Agency's current thinking on a topic and 
41
should be viewed only as recommendations, unless specific regulatory or statutory 
42
requirements are cited.  The use of the word should in Agency guidance means that 
43
something is suggested or recommended, but not required.  
44
45
II. Background 
46
47
For over a hundred years, the reference method for the diagnosis of cancer and many 
48
other critical clinical conditions has been histopathological examination of tissues using 
49
conventional light microscopy.  This process is known as surgical pathology in the 
50
United States. 
51
52
In surgical pathology, patient tissue from surgery, biopsy or autopsy goes through a 
53
process that includes dissection, fixation, embedding, and cutting of tissue into very thin 
54
slices which are then stained, for example by the hematoxylin and eosin (H&E) protocol, 
55
and permanently mounted onto glass slides.  The slides are examined by a pathologist 
56
under a light microscope by dynamically adjusting the focus and using different 
57
magnifications.  By integrating their interpretations obtained by microscopic examination 
58
of the tissue from all slides pertaining to a case, pathologists arrive at a diagnosis of the 
59
case.  
60
61
WSI refers to the digitization of the stained entire tissue specimen on a glass slide.  The 
62
glass slide is still prepared and stained just as for conventional light microscopy.  
63
Depending on the system used, various magnifications, scanning methodologies, 
64
hardware, and software are employed to convert the optical image of the slide into a 
65
digital whole slide image.  With WSI, the pathologist views the image on a computer 
66
monitor rather than through the microscope oculars.   
67
68
III. Scope 
69
70
This document provides guidance regarding only the technical performance assessment 
71
of WSI systems for regulatory evaluation.  WSI systems are defined here as those 
72
consisting of (a) an image acquisition subsystem that converts the content of a glass slide 
73
into a digital image file, and (b) a workstation environment for viewing the digital 
74
images.  If not otherwise specified, the term “image” in the context of whole slide 
75
imaging refers to a pyramid structure consisting of multiple images at different 
76
resolutions. The baseline image has the highest resolution.  This guidance is applicable 
77
for surgical pathology tasks performed in the anatomic pathology laboratory.  It is 
78
intended to provide recommendations to industry and FDA staff regarding only the 
79
technical performance assessment data needed for the regulatory evaluation of a WSI 
80
device.  This document is not meant to provide guidance for special stain techniques or 
81

---

<!-- Page 7 -->
Contains Nonbinding Recommendations 
 
fluorescence imaging or for the non-technical analytical studies (utilizing clinical 
3 
 
82
samples) or pivotal clinical studies necessary to support safety and effectiveness, nor 
83
does this guidance alone suffice to demonstrate safety and effectiveness of WSI systems.  
84
Interpretation of WSI images on mobile platforms is beyond the scope of this guidance.  
85
86
IV. Policy 
87
88
The following subsections of this section describe the technical performance assessment 
89
data FDA believes will facilitate the regulatory evaluation of a WSI device.    
90
91
IV(A). Description and Test Methods for Each Component 
92
93
This subsection details the descriptions and the test methods at the component level that 
94
should be included in the technical performance assessment of a WSI device.  For 
95
purposes of this guidance only, a component is a piece of hardware, software, or a 
96
combination of hardware and software that processes the image signals flowing through 
97
the imaging chain.  The concept of a component is based on the transformation of the 
98
image signals.  For example, the digital imaging sensor is a hardware device that converts 
99
optical signals into digital signals.  The image composition component is a software 
100
program that stitches sub-images together to form a whole slide image.  A component 
101
and a physical device need not be in close physical proximity.  For example, the light 
102
source component and the image optics component are usually tightly coupled within the 
103
same device, while the display calibration data is often distributed in both the color 
104
profile in the computer environment component and the on-screen display settings in the 
105
display component. 
106
107
The components in a WSI device can be grouped in two subsystems: image acquisition 
108
and image display.  The image acquisition subsystem digitizes the tissue slide as a digital 
109
image file.  The image display subsystem converts the digital image file into optical 
110
signals for the human reader.  In the paradigm of telemedicine, the digital image file can 
111
be electronically sent to a remote site for reading, so the image acquisition subsystem and 
112
the image display subsystem do not need to be physically coupled.  Methods for 
113
independently testing the image acquisition and display subsystems are described in 
114
Section IV(B). 
115
116
Sponsors should provide a block diagram of the components found in the WSI system in 
117
the premarket submission.  A chart indicating the relationship among the components and 
118
the test methods utilized for the specific system characterization should also be provided.  
119
Diagram 1 on the following page is offered as an example block diagram of typical 
120
components found in current WSI systems.  The components of a particular WSI system 
121
might not include all of those listed in the diagram or may include additional 
122
components.  Sponsors are encouraged to provide additional diagrams, illustrations, and 
123
photographs of their devices as part of their submissions. 
124
125
126

---

<!-- Page 8 -->
Contains Nonbinding Recommendations 
 
Diagram 1: Example block diagram of typical components found in current WSI 
4 
 
127
systems 
128
129
 
130
 
131
 
132
 
133
 
134
 
135
 
136
 
137
 
138
 
139
 
140
 
141
 
142
 
143
 
144
 
145
 
146
 
147
 
148
 
149
 
150
 
151
 
152
 
153
 
154
 
155
 
156
 
157
 
158
 
159
 
160
 
161
 
162
 
163
 
164
 
165
 
166
167

---

<!-- Page 9 -->
Contains Nonbinding Recommendations 
 
IV(A)(1). 
Slide Feeder 
5 
 
168
169
IV(A)(1)(a). 
Description 
170
171
The slide feeder is the mechanism(s) used to introduce the slide(s) to the scanner.  For the 
172
slide feeder, sponsors should provide the following information, if applicable: 
173
· Configuration of the slide feed mechanism (a physical description of the 
174
equipment) 
175
o Slide configuration (physical description of the slide (i.e., custom or 
176
commercial off-the-shelf)) 
177
o Number of slides in queue (carrier) 
178
o Class of automation (e.g., robotics, pneumatics, etc.) 
179
· User interaction 
180
o Hardware (e.g., loading of slides into carrier) 
181
o Software (e.g., does the system recognize the number of slides or is this 
182
specified by the user) 
183
o Feedback (e.g., alarms, notifications, etc.) 
184
o Failure Mode and Effects Analysis (FMEA) (including severity, 
185
likelihood, mitigations, etc.) 
186
187
IV(A)(2). 
 Light Source 
188
189
IV(A)(2)(a). 
Description 
190
191
The light source, including the light guide, generates and delivers light to the slide being 
192
imaged.  The two major components are the lamp and condenser.  For the light source, 
193
sponsors should provide the following information and specifications, if applicable: 
194
· Lamp 
195
o Bulb type (e.g., halogen, xenon arc, LED) 
196
o Manufacturer and model 
197
o Wattage 
198
o Spectral power distribution 
199
o Expected lifetime 
200
o Output adjustment control (electrical/electronic/mechanical)
201
o Optical filter(s) 
202
§ Type (e.g., heat blocking, polarization, neutral density, diffusing) 
203
o Manufacturer and model 
204
o Expected intensity variation (coefficient of variation ) 
205
§ Over the duration of scanning a single slide 
206
§ Over the course of a single workday 
207
§ Over the lifetime of the device 
208
o Expected spectral variation 
209
§ Over the duration of scanning a single slide 
210
§ Over the course of a single workday 
211
§ Over the lifetime of the device 
212
o Capability of tracking intensity and spectral degradation with lifetime 
213

---

<!-- Page 10 -->
Contains Nonbinding Recommendations 
 
· Condenser 
6 
 
214
o Illumination format (e.g., Kohler, critical) 
215
o Manufacturer and model 
216
o Numerical aperture 
217
o Focal length 
218
o Working distance 
219
220
IV(A)(2)(b). 
Test Method 
221
222
The following steps should be used to measure the spectral distribution of light incident 
223
on the slide.  Position the input of a calibrated spectrometer or monochromator at the 
224
plane where the slide would be placed, centered on the illumination spot from the 
225
condenser.  If desired, the light can be coupled into the spectrometer via light guide (e.g., 
226
fiber optic cable) or an integrating sphere.  The measurement aperture should be at least 
227
as large as the anticipated field of view on the slide at the lowest magnification of the 
228
imaging optics.  The wavelength accuracy and relative spectral efficiency of the 
229
spectrometer or monochromator in the wavelength range of 360-830 nm should be 
230
calibrated prior to measurements and reported.  Plots of the measured spectrum with at 
231
least 10 nm spectral resolution should be provided, using radiometric units (e.g., spectral 
232
irradiance in W/cm2/nm, spectral radiance in W/sr/cm2/nm). 
233
234
IV(A)(3). 
Imaging Optics 
235
236
IV(A)(3)(a). 
Description 
237
238
The imaging optics comprises the microscope objective and auxiliary lens(es) (e.g., tube 
239
lens), which optically transmit an image of the tissue from the slide to the digital image 
240
sensor.  Sponsors should provide the following information and specifications, if 
241
applicable: 
242
· Optical schematic with all optical elements identified from slide (object plane) to 
243
digital image sensor (image plane) 
244
· Microscope objective 
245
o Manufacturer 
246
o Type  
247
o Magnification 
248
o Numerical aperture (NA) 
249
o Focal length 
250
o Working distance 
251
· Auxiliary lens(es) 
252
o Manufacturer 
253
o Lens type 
254
o Focal length 
255
· Magnification of imaging optics: ISO 8039:2014 Optics and optical instruments 
256
— Microscopes — Magnification 
257
258
259

---

<!-- Page 11 -->
Contains Nonbinding Recommendations 
 
IV(A)(3)(b). 
Test Methods 
7 
 
260
261
Sponsors should conduct the following tests in conformance with the International 
262
Standards, if applicable: 
263
· Relative irradiance of imaging optics at image plane per ISO 13653:1996 Optics 
264
and optical instruments – General optical test methods - Measurement of relative 
265
irradiance in the image field 
266
· Distortion per ISO 9039:2008 Optics and photonics — Quality evaluation of 
267
optical systems —Determination of distortion 
268
· Chromatic aberrations per ISO 15795:2002 Optics and optical instruments — 
269
Quality evaluation of optical systems — Assessing the image quality degradation 
270
due to chromatic aberrations 
271
272
IV(A)(4). 
Mechanical Scanner Movement 
273
274
IV(A)(4)(a). 
Description 
275
276
The mechanical scanner addresses the physical characteristics of the stage upon which 
277
the glass slide is affixed.  The key components include stage configuration, movement, 
278
and control.  This information is relevant whether it is only the stage that is moving and 
279
the optics are stationary, or if there is movement on all axes.  For the mechanical scanner, 
280
sponsors should provide the following information and specifications, if applicable: 
281
· Configuration of the stage (a physical description of the stage) 
282
o Stage size 
283
o Stage manufacturer and model number 
284
o Stage material (e.g., anodized aluminum) 
285
o Single multi-axis or multiple stacked linear stages (manufacturer and 
286
model number) 
287
o Type of guides or ways (e.g., bearings) 
288
o Sample retention mechanism (slide holder) 
289
· Method of movement of the stage (e.g., stepper motor, servomotor, piezomotor, 
290
etc., coupled with belt, ball-screw, lead-screw, etc.) 
291
o Movement resolution for XY-axes  
292
o Movement in Z-axis 
293
o Speed range 
294
o Travel distance 
295
o Maximum scanning area 
296
o Localization and reading of bar code labels 
297
· Control of movement of the stage 
298
o Open or closed loop operation 
299
o Positional accuracy (calibration) and repeatability 
300
§ Lost motion compensation (e.g., backlash) 
301
o Physical control (e.g., joystick) for single-slide, non-batch mode 
302
o Selection of area to be scanned (in accordance to image composition 
303
software) 
304
§ whole slide 
305

---

<!-- Page 12 -->
Contains Nonbinding Recommendations 
 
§ automatically determined area with tissue content 
8 
 
306
· Failure Mode and Effects Analysis (FMEA) (including severity, likelihood, 
307
mitigations, etc.) 
308
309
IV(A)(4)(b). 
Test Method 
310
311
Sponsors should demonstrate the mechanical performance of the stage with respect to 
312
positional repeatability and accuracy on all relevant axes, in accordance with ISO 230-
313
2:2014 Test code for machine tools—Part 2:  Determination of accuracy and 
314
repeatability of positioning numerically controlled axes. 
315
316
IV(A)(5). 
Digital Imaging Sensor 
317
318
IV(A)(5)(a). 
Description 
319
320
The digital image sensor is an array of photosensitive elements (pixels) that convert the 
321
optical signals of the slide to digital signals, which consist of a set of values 
322
corresponding to the brightness and color at each point in the optical image.  Please 
323
provide the following information and specifications: 
324
· Sensor type (e.g., CMOS, CCD) and manufacturer 
325
· Pixel information/specifications 
326
o Number and dimensions of pixels 
327
o Design of color filter array 
328
§ Configuration of color filter array 
329
§ Spectral transmittance of color filter mask 
330
· Responsivity specifications 
331
o Relative response versus wavelength 
332
o Linearity 
333
o Spatial uniformity 
334
· Noise specifications 
335
o Dark current level (electrons per second) 
336
o Read noise (electrons) 
337
· Readout rate (e.g., pixels per second, frames per second) 
338
· Digital output format (e.g., bits per pixel, bits per color channel) 
339
340
IV(A)(5)(b). 
Test Methods 
341
342
Sponsors should conduct the following tests in conformance with the corresponding 
343
International Standards, if applicable: 
344
345
· Opto-electronic conversion function per ISO 14524:2009  Photography — 
346
Electronic still-picture cameras — Methods for measuring optoelectronic 
347
conversion functions (OECFs) 
348
· Noise measurements per ISO 15739:2013 Photography — Electronic still-picture 
349
imaging — Noise measurements 
350
351

---

<!-- Page 13 -->
Contains Nonbinding Recommendations 
 
IV(A)(6). 
Image Processing Software 
9 
 
352
353
IV(A)(6)(a). 
Description 
354
355
Image processing software refers to the embedded software components of the image 
356
acquisition device.  It typically includes control algorithms for image capture and 
357
processing algorithms for raw data conversion into the digital image file.  Sponsors 
358
should provide the following information and specifications, if applicable: 
359
· Exposure control  
360
· White balance 
361
· Color correction 
362
· Sub-sampling 
363
· Pixel-offset correction  
364
· Pixel-gain or flat-field correction  
365
· Pixel-defect correction 
366
367
IV(A)(6)(b). 
Resources 
368
369
See the guidance entitled “Guidance for the Content of Premarket Submissions for 
370
Software Contained in Medical Devices” 
371
(http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocument
372
s/ucm089543.htm) for the information that should be provided. 
373
374
IV(A)(7). 
Image Composition 
375
376
IV(A)(7)(a). 
Description 
377
378
Image composition is a step present in systems that produce whole slide images as 
379
opposed to individual fields of view.  Whole slide scanning is typically performed in 
380
accordance with the positioning of a stage that moves in submicron steps.  At each 
381
location of the stage movement, an image of the field of view is acquired.  Images can be 
382
acquired with a degree of overlapping (redundancy) between them to avoid gaps in data 
383
collection.  Images can also be acquired at different depths of focus followed by the 
384
application of focusing algorithms.  At the end of this process, all acquired images are 
385
combined (stitched) together to create a composite high resolution image.  There are a 
386
number of features that can affect this process, and they are listed below.  Sponsors 
387
should provide a description of these features, if applicable: 
388
· Scanning method 
389
o Single objective or multiple miniature objectives in an array pattern 
390
o Scanning pattern: square matrix acquisition (tiling), line scanning, etc. 
391
o Overlap between scanned regions  
392
o Merging algorithms that stitch the aligned images together into a 
393
composite image file.  Such algorithms may employ functions to align 
394
adjacent fields of view in accordance to the scanning pattern, overlap, etc. 
395

---

<!-- Page 14 -->
Contains Nonbinding Recommendations 
 
o Automatic background correction functions to eliminate the effect of non-
10 
 
396
uniformities in the microscope’s illumination and image merging 
397
procedure.  These non-uniformities if not corrected might create visible 
398
borders (seams and stitch lines) between the adjacent fields of view. 
399
· Scanning speed:  time to scan the whole slide.  This time is dependent on selected 
400
magnification, and the amount of tissue on the glass slide. 
401
· Number of planes at the Z-axis to be digitized (stack depth) 
402
403
IV(A)(7)(b). 
Test Methods 
404
405
Testing for image composition can be performed on a system level using special 
406
calibration slides (such as grid patterns) that can test for line uniformity and focus 
407
quality.  Sponsors should provide the following outputs for these tests, if applicable: 
408
· Images of digitized calibration slides 
409
· Analysis of focus quality metrics 
410
· Analysis of coverage of the image acquisition for the entire tissue slide 
411
412
IV(A)(8). 
Image Files Formats 
413
414
IV(A)(8)(a). 
Description 
415
416
The final result from image acquisition can be a whole slide image consisting of a stack 
417
of all acquired fields of view and magnifications during WSI.  The complete digitized 
418
image file usually occupies between 1-20 gigabytes of storage space depending on the 
419
sample and the magnification of the objective lens used.  Images can then be stored in a 
420
number of ways and formats.  Sponsors should provide the following information: 
421
· Compression method (e.g., the wavelet-based JPEG2000 compression standard or 
422
TIFF) 
423
· Compression ratio:  ratio of uncompressed to compressed file size.  This metric 
424
should be provided along with descriptive information on the data it was 
425
measured from, since compression ratio is dependent on the content of the data 
426
applied to. 
427
· Compression type:  lossless or lossy compression 
428
· File format: can be formats easily accessible with public domain software such as 
429
JPEG or TIFF, or can be proprietary formats only accessible with specific vendor 
430
viewers.  The file format depends on the file organization and related use. 
431
· For systems that interact with DICOM-compliant software and hardware, 
432
sponsors should provide a DICOM compatibility report. 
433
· File organization:   
434
o Single file with multi-resolution information (pyramidal organization) 
435
o Stack of files at different magnifications 
436
437
438
439

---

<!-- Page 15 -->
Contains Nonbinding Recommendations 
 
IV(A)(9). 
Image Review Manipulation Software 
11 
 
440
441
IV(A)(9)(a). 
Description 
442
443
For the image review manipulation software, sponsors should provide the following 
444
information, describing software features, if applicable.   
445
· Continuous panning (moving in x-y space) and pre-fetching (buffering adjacent 
446
images to speed up panning time) 
447
· Continuous zooming (magnification)  
448
· Discrete Z-axis displacement 
449
· Ability to compare multiple slides simultaneously on multiple windows 
450
· Ability to perform annotations 
451
· Image enhancement such as sharpening functions  
452
· Color manipulation, including color profile, white balance, color histogram 
453
manipulation, and color filters 
454
· Annotation tools 
455
· Tracking of visited areas and annotations  
456
· Digital bookmarks (revisit selected regions of interest) 
457
· Virtual “multihead microscope” (this is when multiple pathologists 
458
simultaneously review the same areas remotely) 
459
460
IV(A)(9)(b). 
Resources 
461
462
See the guidance entitled “Guidance for the Content of Premarket Submissions for 
463
Software Contained in Medical Devices” 
464
(http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocument
465
s/ucm089543.htm) for additional information on this subject. 
466
467
IV(A)(10). Computer Environment 
468
469
IV(A)(10)(a). 
Description 
470
471
Computer environment refers to the workstation, including both hardware and software 
472
components, that retrieves the digital image file and drives the display for the user to 
473
review the images.  Sponsors should provide the following information and 
474
specifications, if applicable: 
475
· Computer hardware  
476
· Operating system  
477
· Graphics card 
478
· Graphics card driver  
479
· Color management settings  
480
· Color profile   
481
· Display interface (e.g., DVI or DisplayPort) 
482
483

---

<!-- Page 16 -->
Contains Nonbinding Recommendations 
 
IV(A)(11). Display 
12 
 
484
485
IV(A)(11)(a). 
Description 
486
487
The final stage of a WSI system is the display component that presents the scanned image 
488
to the pathologists for reading. Technically, display refers to the optoelectronic device 
489
that converts the digital image signals in the RGB space into optical image signals. For 
490
the display, sponsors should provide the following information and specifications, if 
491
applicable:  
492
· Technological characteristics of the display device (e.g., in-plane switching LCD 
493
panel with TFT active-matrix array with fluorescent backlight) 
494
· Physical size of the viewable area and aspect ratio 
495
· For transmissive displays, backlight type and properties including temporal, 
496
spatial, and spectral characteristics  
497
· Frame rate and refresh rate 
498
· Pixel array, pitch, pixel aperture ratio and subpixel matrix scheme (e.g., chevron, 
499
RGBW) 
500
· Subpixel driving to improve grayscale resolution (e.g., spatial and temporal 
501
dithering)  
502
· Supported color spaces 
503
· Display Interface  
504
· User controls of brightness, contrast, gamma, color space, power-saving options, 
505
etc. via the on-screen display (OSD)  menu 
506
· Ambient light adaptation including the ambient light sensing method, 
507
instrumentation, and software tool description 
508
· Touch screen technology including method, functionality, and any calibration or 
509
periodical re-tuning requirements 
510
· Color calibration tools (sensor hardware and associated software), color profile, 
511
and method for color management 
512
· Frequency and nature of quality-control tests to be performed by the user and/or 
513
the physicist with associated action limits. 
514
515
IV(A)(11)(b). 
Test Methods 
516
517
· User controls: Modes and settings of the display undergoing testing should be 
518
specified, including brightness, contrast, gamma, white point, color space, etc. 
519
See 2.1 Modified-Performance Modes, IDMS 1.03. 
520
· Spatial resolution: Measurements of the transfer of information from the image 
521
data to the luminance fields at different spatial frequencies of interest typically 
522
done by reporting the modulation transfer function.  Non-isotropic resolution 
523
properties should be characterized properly by providing two-dimensional 
524
measurements or measurements along at least two representative axes. See 7.7 
525
Effective Resolution, IDMS 1.03. 
526

---

<!-- Page 17 -->
Contains Nonbinding Recommendations 
 
· Pixel defects (count and map): Measurements (counts) and location of pixel 
13 
 
527
defects. This is typically provided as a tolerance limit. Pixel defects can interfere 
528
with the visibility of small details in medical images. See 7.6 Defective Pixels, 
529
IDMS 1.03. 
530
· Artifacts: Evaluate for image artifacts such as ghosting and/or image sticking 
531
from displaying a fixed test pattern for a period of time. See 4.6 Artifacts and 
532
Irregularities, IDMS 1.03.  
533
· Temporal response: Measurements of the temporal behavior of the display in 
534
responding to changes in image values from frame to frame.  Since these 
535
transitions are typically not symmetric, rise and fall time constants are needed to 
536
characterize the system. See 10.2.3 Gray-to-Gray Response Time, IDMS 1.03. 
537
· Maximum and minimum luminance (achievable and recommended): 
538
Measurements of the maximum and minimum luminance that the device outputs 
539
as used in the application under recommended conditions and the achievable 
540
values if the device is set to expand the range to the limit. See 2.4 Vantage-Point 
541
Suite of Measurement, IDMS 1.03. 
542
· Grayscale: Measurements of the mapping between image values and the 
543
luminance. See 6.1 Grayscale, IDMS 1.03. 
544
· Luminance uniformity and Mura test: Measurements of the uniformity of the 
545
luminance across the display screen. See 8.1.2 Sampled Vantage-Point Uniformity 
546
and 8.2.3 Mura Analysis, IDMS 1.03. 
547
· Stability of luminance and chromaticity response with temperature and lifetime  
548
· Bidirectional reflection distribution function: Measurements of the reflection 
549
coefficients of the display device. Specular and diffuse reflection coefficients can 
550
be used as surrogates for the full bidirectional reflection distribution function. See 
551
11.12 Diagnostic: Characterizing Hemisphere Uniformity, IDMS 1.03. 
552
· Gray Tracking: Chromaticity at different luminance levels as indicated by the 
553
color coordinates in an appropriate units system (e.g., CIE u’v’). See AAPM Task 
554
Group 196 Report. 
555
· Color scale: Color coordinates of primary and secondary colors as a function of 
556
the digital driving level and their additivity. See 6. Gray- and Color-Scale 
557
Measurement and 5.4 Color-Signal White, IDMS 1.03. 
558
· Color gamut volume: See 5.31 Volume-Color-Reproduction Capability, IDMS 
559
1.03. 
560
561
IV(A)(11)(c). 
Resources 
562
563
Those interested in learning more about these types of display considerations should 
564
consider reading: 
565
566
· IDMS 1.03 - Information Display Measurements Standard Version 1.03, 
567
International Committee for Display Metrology, Society for Information Display, 
568
www.icdm-sid.org 
569
570
· E. Samei, A. Badano, D. Chakraborty, K. Compton, C. Cornelius, K. Corrigan, 
571
M. J. Flynn, B. Hemminger, N. Hangiandreou, J. Johnson, M. Moxley, W. 
572

---

<!-- Page 18 -->
Contains Nonbinding Recommendations 
 
Pavlicek, H. Roehrig, L. Rutz, J. Shepard, R. Uzenoff, J. Wang, and C. Willis, 
14 
 
573
Assessment of display performance for medical imaging systems, Report of the 
574
American Association of Physicists in Medicine (AAPM) Task Group 18, 
575
Technical Report, AAPM (April 2005). 
576
577
· IEC 62563-1:2009, Medical electrical equipment – Medical image display 
578
systems – Part 1: Evaluation methods 
579
580
· Amendment 1 to IEC 62563-1: Medical image display systems – Part 1: 
581
Evaluation methods 
582
583
· The guidance entitled “Guidance for Industry and FDA Staff: Display Accessories 
584
for Full-Field Digital Mammography Systems-Premarket Notification (510(k)) 
585
Submissions” 
586
(http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceD
587
ocuments/ucm107549.htm).  
588
589
IV(B). System-level Assessment 
590
591
This subsection details the test methods at the system level that should be included in the 
592
technical performance assessment of a WSI device.  In this guidance, system refers to a 
593
series of consecutive components in the imaging chain with clearly defined, measureable 
594
input and output.  For example, a system-level test can be designed for the image 
595
acquisition subsystem, the image display subsystem, or a combination of both.  The goal 
596
of system-level tests is to assess the composite performance of a series of consecutive 
597
components in the imaging chain.  System-level tests should be conducted when the 
598
component-level tests are either unfeasible or unable to capture the interplay between 
599
components. 
600
601
The common framework of the system-level tests described in this section is to compare 
602
the system under test with an ideal system based on the same input, and then report the 
603
difference between their outputs quantitatively.  Designing such a system-level test 
604
typically involves the following steps: (1) define the scope of the system and its input and 
605
output, (2) define the input, which in most cases is a test target or phantom, (3) measure 
606
the input to establish the ground truth that would be generated by an ideal system, (4) 
607
measure the output of the system under test, and (5) calculate the errors between the truth 
608
and the output with a quantitative metric.  The framework of a typical system-level test is 
609
shown in Diagram 2.  Notice that the ideal system is a hypothetical device that generates 
610
the perfect output with respect to the objective of the test such as color or focus.  The 
611
purpose of the ideal system is to define the intended behavior of the system under test.  
612
The ideal system does not need to be implemented.  Instead, the ideal system should be 
613
simulated by a test method that establishes the truth of the input phantom.     
614
615
616
617
618

---

<!-- Page 19 -->
Contains Nonbinding Recommendations 
 
Diagram 2: Framework of a typical system-level test. 
15 
 
619
620
 
621
 
622
 
623
 
624
625
IV(B)(1). 
Color Reproducibility 
626
627
IV(B)(1)(a). 
Description 
628
629
Color reproducibility is one of the key characteristics of a WSI system. The color 
630
characteristics are determined by every component in the imaging chain. Therefore, the 
631
color characteristics might be best evaluated at the system level. Color reproducibility 
632
indicates the accuracy and precision of the color transformation from the tissue sample on 
633
the slide to the image on the display. The colors of the tissue specimen should be 
634
accurately and precisely reproduced on the display based on the color reproduction intent, 
635
which should be clearly defined and justified by the sponsor. 
636
637
IV(B)(1)(b). 
Test Methods 
638
639
The WSI system should be tested with a target slide. The target slide should contain a set 
640
of measurable and representative color patches. Ideally the color patches should have 
641
similar spectral characteristics to stained tissue. The color patches should include a 
642
grayscale ramp for evaluating the grayscale response. The truth of the color patches 
643
should be measured with proper apparatuses separately. 
644
645
For each color patch, the intended color (i.e., the expected output color based on the color 
646
reproduction intent defined by the Sponsor) should be calculated based on the truth of the 
647
color patches. 
648
649
The target slide should be scanned and displayed by the WSI system. The output color of 
650
each color patch should be measured from the display. 
651
652
The three datasets – truth, intended color, and output color – should be compared and 
653
analyzed. The sponsor should provide a rationale if the intended color is different from 
654
the truth.  
655
656
657
658
659
660
661
662
Error 
System under test 
Ideal system 
Input 
(Phantom) 
Output 
Truth 
f

---

<!-- Page 20 -->
Contains Nonbinding Recommendations 
 
Diagram 3: Framework of the system-level color reproducibility test. 
16 
 
663
664
665
666
 
667
 
668
 
669
 
670
671
672
IV(B)(1)(c). 
Resources 
673
674
Useful references on the subject of color reproducibility can be found at the International 
675
Color Consortium website http://www.color.org. 
676
677
IV(B)(2). 
Spatial Resolution 
678
679
IV(B)(2)(a). 
Description  
680
681
Spatial resolution is another key characteristic of a WSI system.  The goal of this system-
682
level test is to evaluate the composite optical performance of all components in the image 
683
acquisition phase (i.e., from slide to digital image file). 
684
685
IV(B)(2)(b). 
Test Methods 
686
687
The following test is recommended for assessing spatial resolution of the image 
688
acquisition phase: 
689
· Resolution and spatial frequency response: ISO 12233:2014(E) — Photography 
690
— Electronic still picture imaging — Resolution and spatial frequency responses. 
691
692
IV(B)(3). 
Focusing Test  
693
 
694
· The quality of focus in WSI can be affected by a number of inter-related factors, 
695
including the scanning method and approaches for constructing a focus map.  Due 
696
to a trade-off between the number of focus points and the overall speed of the 
697
scanning process, focusing is typically based on a sample of focus points, 
698
determined automatically (auto-focus) or manually by the user.  Since tissue can 
699
have uneven depth, auto-focus algorithms are needed to detect and adjust for 
700
different depths of focus.   
701
702
· Data demonstrating that the focus quality is acceptable, even in the presence of 
703
uneven tissue, should be provided.  Such data with proper justification could be 
704
derived from a phantom study, from clinical data, or both in a complementary 
705
fashion.  The technology of phantom construction for testing focus is under 
706
development and this guidance will be updated as such technologies become 
707
available.  Sponsors could attempt to build their own phantoms for testing depth 
708
Truth 
Meter 
Intended Color 
Output Color 
Accuracy 
Precision 
WSI under test 
Color 
Reproduction 
Intent 
Target 
Slide 
-

---

<!-- Page 21 -->
Contains Nonbinding Recommendations 
 
of focus for their device.  Alternatively, sponsors could provide experimental data 
17 
 
709
using clinical tissue slides.  Sampling of cases for such an experiment should be 
710
enriched for uneven tissue cases within a range representative of typical 
711
laboratory output.   Alternative approaches for assessing the focus quality of a 
712
WSI will be considered along with proper justification.  In addition, the following 
713
specifications should be provided, if applicable:    
714
o Focus method: auto-focus for high-throughput or user-operated focus 
715
points  
716
o Instructions for the selection of manual focus points (if applicable), 
717
including number of focus points and location in relation to a tissue 
718
sample 
719
o Metrics used to evaluate focusing and description of methods to extract 
720
them 
721
o Methods for constructing focus map from sample focus points 
722
723
Diagram 4: Framework of the system-level focusing test. 
724
725
726
727
728
729
730
731
732
733
IV(B)(4). 
Whole Slide Tissue Coverage 
734
735
IV(B)(4)(a). 
Description 
736
737
During the scan phase, WSI systems usually skip blank areas where tissue is absent in 
738
order to reduce scan time and file size.  The purpose of the whole slide tissue coverage 
739
test is to demonstrate that all of the tissue specimen on the glass slide is included in the 
740
digital image file.  
741
742
IV(B)(4)(b). 
Test Method 
743
744
Sponsors should include a test that demonstrates the completeness of the tissue coverage.  
745
Sponsors should describe the test method and include the following items: 
746
· Selection of the input tissue slide 
747
· How to determine the complete coverage of the input tissue slide 
748
· How to measure the actual coverage of the WSI output 
749
· Calculate the ratio of the actual to complete coverage 
750
751
752
753
754
Error 
WSI under test 
WSI with perfect 
focusing capability 
Phantom 
Slide 
Actual 
Focus 
 
Optimal 
Focus 
f

---

<!-- Page 22 -->
Contains Nonbinding Recommendations 
 
Diagram 5: Framework of the system-level whole slide tissue coverage test 
18 
 
755
756
 
757
 
758
 
759
 
760
 
761
 
762
763
IV(B)(5). 
Stitching Error 
764
765
IV(B)(5)(a). 
Description 
766
767
Stitching is the technique that enables a WSI system to combine thousands of sub-images 
768
into a single whole-slide image.  Although during the scanning process a certain amount 
769
of overlapping between adjacent sub-images is maintained for alignment purposes, 
770
successful stitching relies on the texture present in the overlapped area.  When the 
771
stitching algorithm fails to align two sub-images seamlessly, the error may or may not be 
772
perceivable by the human reader depending on whether noticeable stitching artifacts are 
773
generated.  Therefore, a system-level test should be conducted when assessing the 
774
stitching quality of the WSI system.   
775
776
IV(B)(5)(b). 
Test Methods 
777
778
Sponsors should include a test that evaluates the stitching errors and include the 
779
following items: 
780
· Selection of the input test slide 
781
· Method for sampling of the stitching boundaries where stitching errors might 
782
occur 
783
· How to determine the ideal stitching as the ground truth 
784
o For example, the region of the stitching boundaries can be re-imaged in 
785
one shot such that there is no stitching artifact.    
786
· How to evaluate quality of the actual stitching based on the perfect stitching 
787
o For example, compare the image of stitching boundaries with the perfect 
788
one that does not have stitching artifact.  The difference between these two 
789
images can be used as a figure of merit of the stitching quality.  
790
791
Diagram 6: Framework of the system-level stitching error test 
792
793
 
794
 
795
 
796
 
797
 
798
 
799
 
800
Error 
WSI under test 
WSI with perfect 
stitching capability 
Tissue 
Slide 
Actual 
Stitching 
 
Perfect 
Stitching 
f 
Error 
WSI under test 
WSI with complete 
coverage capability 
Tissue 
Slide 
Actual 
Coverage 
 
Complete 
Coverage 
f

---

<!-- Page 23 -->
Contains Nonbinding Recommendations 
 
19 
 
801
IV(B)(6). 
Turnaround Time 
802
803
IV(B)(6)(a). 
Description 
804
805
Turnaround time is the time required by the WSI system to execute a particular user 
806
operation such as panning/zooming where the software and I/O (input/output) devices 
807
retrieve image data, execute the computation, and refresh the image on the display. The 
808
turnaround time starts when the user enters a command via a keyboard stroke or a mouse 
809
click/movement and finishes when the image is completely updated on the display. 
810
Turnaround time is important for a WSI system when fast and repetitive panning 
811
operations are performed during a search task, which is delay-free in an optical 
812
microscope.  Prolonged, unpredictable turnaround time may impact the user’s diagnostic 
813
performance. The user interface should properly prompt the user when the operation is 
814
incomplete and the requested image is not available . The turnaround time may vary 
815
greatly depending on the user-requested operation, image content, data size/location, 
816
computer workload, display size, etc. The sponsor should report the typical turnaround 
817
time as well as the test method and test conditions.   
818
  
819
IV(C). User Interface  
820
821
IV(C)(1). 
Description 
822
823
The user interface covers all components and accessories of the WSI system with which 
824
users interact while loading the slides and acquiring, manipulating, and reviewing the 
825
images.  It also includes preparing the system for use (e.g., unpacking, set up, 
826
calibration), and performing maintenance.  Elements of the user interface have been 
827
noted in many of the preceding sections and include two broad categories: 
828
· Options through which the user operates the WSI system, such as:  
829
o Software menu options (e.g., scanning parameters) 
830
o Physical controls (e.g., clips on the slide feeder) 
831
o Connectors and connections (e.g., cables connecting system components) 
832
· Information presented to the user through  
833
o Visual displays (e.g., scanned image, software menus) 
834
o Sounds (e.g., tone played when scanning completed)  
835
o Instructions (e.g., software users’ manual) 
836
o Labels 
837
838
IV(C)(2). 
Test Methods 
839
840
It is recommended that the analysis to identify the use-related hazards of the WSI system 
841
include the consideration of use errors involving failure to acquire, perceive, read, 
842
interpret, and act on information from the WSI system correctly or at all and the harm 
843
that could be caused by such errors.  A human factors/usability validation test should be 
844
performed to demonstrate that representative users of the WSI system can perform 
845
essential tasks and those critical to safety under simulated use conditions. 
846

---

<!-- Page 24 -->
Contains Nonbinding Recommendations 
 
20 
 
847
When selecting participants for validation testing, sponsors should carefully consider user 
848
capabilities and expectations that could potentially impact the safe and effective use of 
849
the WSI system.  Examples of items that should be considered, if applicable, include 
850
visual acuity and type of vision correction and the impact of expectations formed from 
851
prior experience with other systems (e.g., optical microscope). 
852
853
When selecting the critical tasks to be evaluated, sponsors should incorporate all known 
854
use related errors and problems from similar devices (devices having similar 
855
technological characteristics and indications for use) into the validation testing.  
856
Consideration also should be given to whether task performance changes over time, and 
857
if test duration needs to account for user fatigue.  Examples might include a user altering 
858
a task sequence in response to fatigue from repetitive image selection and manipulation 
859
with mouse or keyboard. 
860
861
When creating the simulated use conditions for validation testing, special consideration 
862
should be given to the location of the WSI system primary workstation, its components, 
863
their arrangement and how their locations affect user performance.  Examples of location 
864
considerations might include multiple monitors, a monitor with sub-optimal display 
865
settings, or glare on a monitor from indoor lighting. 
866
867
A human factors/usability validation test report should generally include the information 
868
found in Table 1. 
869
870
Table 1: Items a Human Factors/Usability Validation Test Report Should Include 
871
872
Section 
Contents 
1 
Intended device users, uses, use environments, and training  
· 
Intended user population(s) and critical differences in 
capabilities between multiple user populations  
· 
Intended uses and operational contexts of use  
· 
Use environments and key considerations  
· 
Training intended for users and provided to test participants  
2 
Device user interface  
· 
Graphical depiction (drawing or photograph) of device user 
interface  
· 
Verbal description of device user interface  
3 
Summary of known use problems  
· 
Known problems with previous models  
· 
Known problems with similar devices

---

<!-- Page 25 -->
Contains Nonbinding Recommendations 
 
21 
 
· 
Design modifications implemented in response to user 
difficulties  
4 
User task selection, characterization and prioritization  
· 
Risk analysis methods  
· 
Use-related hazardous situation and risk summary  
· 
Critical tasks identified and included in HFE/UE validation tests 
5 
Summary of formative evaluations  
· 
Evaluation methods  
· 
Key results and design modifications implemented  
· 
Key findings that informed the HFE/UE validation testing 
protocol  
6 
Validation testing  
· 
Rationale for test type selected (i.e., simulated use or clinical 
evaluation)  
· 
Number and type of test participants and rationale for how they 
represent the intended user populations  
· 
Test goals, critical tasks and use scenarios studied  
· 
Technique for capturing unanticipated use errors  
· 
Definition of performance failures  
· 
Test results: Number of device uses, success and failure 
occurrences  
· 
Subjective assessment by test participants of any critical task 
failures and difficulties  
· 
Description and analysis of all task failures, implications for 
additional risk mitigation  
7 
Conclusion 
A statement to the effect that “The <device name/model> has been 
found to be reasonably safe and effective for the intended users, uses 
and use environments” should be included under the following 
conditions: 
· 
The methods and results described in the preceding sections 
support this conclusion.  
· 
Any residual risk that remains after the validation testing would 
not be further reduced by modifications of design of the user 
interface (including any accessories and the Instructions for Use 
(IFU)), is not needed, and is outweighed by the benefits that

---

<!-- Page 26 -->
Contains Nonbinding Recommendations 
 
22 
 
may be derived from the device’s use.  
873
Recommended methods for performing a human factors/usability validation test are 
874
described in the resources listed in section IV(C)(3) entitled “Resources” directly below.  
875
The goal of testing is to assure that users can operate the WSI system successfully for the 
876
intended uses without negative clinical consequences to the patient and that potential use 
877
errors or failures have been eliminated or reduced. 
878
879
IV(C)(3). 
Resources 
880
881
FDA recognizes standards published by national and international organizations that 
882
apply human factors engineering/usability engineering (HFE/UE) principles to device 
883
design and testing.  The recognized standards listed below provide suggestions on 
884
conducting an analysis of use-related hazards and a human factors/usability validation 
885
test to assess the safety and effectiveness of the final device design.  
886
887
· ISO 14971:2007, Medical Devices – Application of Risk Management to Medical 
888
Devices:  Provides systematic process to manage the risks associated with the use 
889
of medical devices. 
890
· AAMI/ANSI HE75:2009, Human Factors Engineering – Design of Medical 
891
Devices:  Comprehensive reference of recommended practices related to human 
892
factors design principles for medical devices. 
893
· IEC 62366-1:2015, Medical devices – Application of usability engineering to 
894
medical devices: Describes the process to conduct medical device usability testing 
895
and incorporate results into a risk management plan.  
896
In addition, FDA has published guidance with human factors related recommendations to 
897
assist manufacturers and facilitate premarket review.  The guidance entitled “Guidance 
898
for the Content of Premarket Submissions for Software Contained in Medical Devices” 
899
(http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocument
900
s/ucm089543.htm).  This guidance document provides recommendations to industry 
901
regarding premarket submissions for software devices, including stand-alone software 
902
applications and hardware-based devices that incorporate software.  It includes test 
903
methods to assure that the software conforms to the needs of the user and to check for 
904
proper operation of the software in its actual or simulated use environment.  
905
906
IV(D). Labeling 
907
908
The premarket application must include labeling in sufficient detail to satisfy the 
909
requirements of 21 CFR Part 801 and 21 CFR 809.10.  The labeling includes 
910
supplementary information necessary to use and care for the WSI system such as 
911
instruction books or direction sheets and software user manuals.   
912
913

---

<!-- Page 27 -->
Contains Nonbinding Recommendations 
 
Although instructions, labeling, and training can influence users to use devices safely and 
23 
 
914
effectively, they should not be the primary strategy used to control risk.  Modification of 
915
the user interface design is a more effective approach to mitigate use-related hazards.  
916
917
IV(D)(1). 
Test Methods 
918
919
It is recommended that studies on labeling and training be conducted separately from 
920
other human factors/usability validation testing.  Human factors/usability validation 
921
testing should be conducted with the final version of the labeling and related materials.  
922
Timing and content of training should be consistent with that expected of actual users. 
923
924
IV(D)(2). 
Resources 
925
926
FDA has published several guidance documents on labeling to facilitate premarket 
927
review and assist manufacturers. 
928
· The guidance entitled “Labeling - Regulatory Requirements for Medical Devices” 
929
(http://www.fda.gov/downloads/MedicalDevices/DeviceRegulationandGuidance/
930
GuidanceDocuments/UCM095308.pdf).   
931
o This publication covers labeling issues that device manufacturers, 
932
reconditioners, repackers, and relabelers should consider when a product 
933
requires labeling.  Labeling includes adequate instructions for use, 
934
servicing instructions, adequate warnings against uses that may be 
935
dangerous to health, or information that may be necessary for the 
936
protection of users. 
937
· The guidance entitled “Device Labeling Guidance #G91-1 (blue book memo)” 
938
(http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceD
939
ocuments/ucm081368.htm).   
940
o This guidance is intended to ensure the adequacy of, and consistency in 
941
device labeling information.  It is intended for use by industry in preparing 
942
device labeling. 
943
· The guidance entitled “Human Factors Principles for Medical Device Labeling” 
944
(http://www.fda.gov/downloads/MedicalDevices/DeviceRegulationandGuidance/
945
GuidanceDocuments/UCM095300.pdf).   
946
o This report presents the principles of instruction, human factors, and 
947
cognitive psychology that are involved in designing effective labeling for 
948
medical devices. 
949
950
IV(E). Quality Control 
951
952
Sponsors should provide information on the quality control procedures, including 
953
frequency and testing methods to be performed by the laboratory technologists and/or 
954
field engineers with associated quantitative action limits.  Discussions of tests for 
955
constancy should include discussions of the slide feeder and scanning mechanisms, 
956
coverage of the entire tissue slide, the bar code reader, the light source, the imaging 
957
sensor device, and the calibrations at the component and system level.  A detailed quality 
958
control manual should be provided. 
959
