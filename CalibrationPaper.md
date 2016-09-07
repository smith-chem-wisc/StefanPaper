### Rapid and Accurate Global PTM Discovery (GPTM-D) Using Post-Acquisition Spectral Calibration and Defined Mass Windows

Stefan R. Solnstev, Michael R. Shortreed, Brian L. Frey, and Lloyd M. Smith\*

Department of Chemistry and Genome Center of Wisconsin

University of Wisconsin – Madison

Madison, WI 53706

ABSTRACT (rewrite this when paper done)

Posttranslational-modifications (PTMs) influence many aspects of protein function in biological processes, and correctly identifying the various protein modifications in biological samples is crucial for understanding proteins. Ways of identifying and localizing PTMs are limited, but emerging techniques in the field of mass spectrometry are becoming available. GPTM-D [_Journal of Very Important Results_, 1, 1 (2016)] is a recently developed tool for global identification of PTMs using a single pass database search that is promising. Spectra file calibration prior to applying the tool, and algorithmic improvements in the peptide database search greatly improve the accuracy and efficiency of new PTM identification. We describe the calibration tool developed, and present numerical results that validate the proposed enhancement.

INTRODUCTION

We have recently described a bioinformatics tool, GPTM-D, for the discovery of new PTMs from "bottom-up" tandem mass spectrometric datasets

# 1
.   The GPTM-D workflow consists of three stages: 1) An open mass database search
# 2-3
 that provides spectral matches to unmodified peptides along with the mass differences between the identified peptides and the measured parent peptide masses (hypothesized to differ in mass due to the presence of a PTM).  2) For those peptides for which the mass difference corresponds to a known PTM, a database augmentation step that adds plausible localized PTMs for the peptides to the search database. 3) A final standard narrow mass search of the augmented database to identify both modified and unmodified peptides subject to the standard FDR threshold (e.g. 1% FDR).

A critical parameter for peptide identification and PTM localization

# 4
 is mass accuracy
# 4
. Higher mass accuracy provides increased specificity and thus confidence in peptide identifications, decreasing the false discovery rate.  Instrument noise, systemic drift and miscalibration limit the mass accuracy in acquired spectra.  Multiple calibration strategies to improve mass accuracy have been devised, and fall into three general categories:  External calibration prior to the MS experiment (e.g. standard instrument calibration protocols); internal calibration during the MS experiment (e.g. real-time calibration using a lock mass standard (REF)); and subsequent to the MS experiment (post-acquisition spectral calibration, REF).  We use a post-acquisition calibration procedure, which we refer to as mzCal, that builds upon the software lock mass concept
# 5
 recently reported  by the Mann group.  In our strategy, the m/z differences between expected and observed peaks in the peptide tandem ms spectra are compiled, and then used to recalibrate the spectra.  The increased mass accuracy of the recalibrated spectra leads directly to improved identifications of both modified and unmodified peptides, as well as to increased confidence for PTM localization.

We have also modified the search strategies to run more efficiently, by using "notch" and "comb" searches of the mass space that reduce unproductive search time and add flexibility by allowing certain mass differences that correspond to things like adducts and monoisotopic errors.  The new search strategy implementing these changes was tested in the analysis of N \_\_\_\_\_ deep proteomic datasets  (describe),  for which the use of mzCal provided a \_\_% increase in overall peptide identification, and a \_\_% increase in the identification of post-translationally modified peptides. The improved search strategies account for a \_% decrease in search time, and an additional \_% increase in identification rate.

EXPERIMENTAL PROCEDURES

The mzCal software is written in C#, and works on all popular operating systems. It is released under the GPL license, and the code is available for inspection at [https://github.com/smith-chem-wisc/mzCal](https://github.com/smith-chem-wisc/mzCal).

The datasets tested are described in detail in

# 6-7
.

RESULTS AND DISCUSSION

Figure 1a shows the modified GPTM-D workflow.  Blue arrows and boxes show the previously described GPTM-D workflow, and those in green correspond to the improved workflow incorporating the mzCal calibration and comb and notch search strategies.  The input into the workflow is a standard bottom-up tandem-ms dataset obtained from a tryptically digested protein sample, and the output is a comprehensive set of peptide and PTM identifications.  Before describing the workflow in detail, it is useful to review and define the different search modes that are employed.   These are illustrated in Figure 1B, which shows four variations: standard search, notch search, comb search, and open search. These differ with respect to whether or not the entire mass space is searched, as opposed to defined subsets of the mass space; and with respect to the narrowness of the mass window employed for each element in the search space.  The smaller the fraction of the mass space, and the wider the mass window per search element, the faster the search will run (as fewer searches are executed per mass spectrum).

| a)

 | b)  |
| --- | --- |

Figure 1: a) The blue components mark the original GPTM-D workflow for identifying and localizing PTMs. The green components are the proposed enhancements to the GPTM-D workflow. b) The four different search strategies

The modified workflow consists of five steps:

**Step 1:** a standard tolerance (e.g. 10 ppm) database search is performed on the dataset. This yields a set of peptide identifications subject to a desired false discovery rate (e.g 1%; based upon the target:decoy strategy (ref)).

**Step 2:** mzCal calibration. The identifications from step 1 are used to extract peak matches from the spectra, and a semi-parametric calibration procedure is performed. The mzCal software is described in detail in appendix.

**Step 3:** A database search only using the peptide fragment ions is performed. This search is expected to produce peptide spectrum matches that match to peptides with a significantly different mass than the corresponding extracted mass from the MS spectrum. This difference is hypothesized to arise from the presence of PTMs, monoisotopic errors or adducts such as oxidation or metal contamination.

Introduction of the comb search instead of an open search is motivated by a careful review of the Unimod database of PTMs and Amino Acid substitutions. Known modifications with mass difference within 200 Daltons have values that are within [-0.1, 0.2] of every integer. PTM combinations also have this property. This allows us to pre-emptively filter the search to look only in intervals that satisfy the condition of being within the specified search windows. This alternative to the open search imporves search times and increases specificity.

Step 4:

## Notch Search Description

N



## Calibration Quality

a. Only spectra files calibration, no additional search done. Show MSE values for different calibration functions, pick one, and say why it's better than others

b. A new normal Morpheus run comparison: 10ppm, vs 3ppm (4 runs)

i. Show that precursor mass errors are centered at zero and have smaller variance

ii. Show that there are more PTMs identified we are confident it

iii. Show that decoy PTMs are pushed down the list

Compare with 11 cell line paper, and with Jurkat/Mouse paper

c. Notches

i. Show that now are able to discern between PTMs with similar mass errors (ones that are only different because of the mass defect)

d. Show the improvement in search time due to the new notches option





We first demonstrate the improvement in a standard protein database search.

|   | Uncalibrated | mzCal | mzRefinery |
| --- | --- | --- | --- |
| 10ppm Precursor |   |   |   |
| 3ppm Precursor |   |   |   |
| 1ppm Precursor |   |   |   |

## Notch Search Time Improvement

## Peptide Shaker vs Morpheus

The calibration algorithm requires a list of identifications to work with, and these identifications usually come from a database or a de-novo search.

|   | Initial Morpheus Search | Initial SearchGUI Search |
| --- | --- | --- |
| Time for first search |   |   |
| FDR in Calibrated GPTMd Search |   |   |



## Mouse Data

Calibration successfully

### Sulfation and Phosphorylation differentiation

## Jurkat Data

## 11 Cell Lines Data



1. GPTM-D.

2. Chick, J. M.; Kolippakkam, D.; Nusinow, D. P.; Zhai, B.; Rad, R.; Huttlin, E. L.; Gygi, S. P., A mass-tolerant database search identifies a large proportion of unassigned spectra in shotgun proteomics as modified peptides. _Nat Biotechnol _ **2015,** _33_ (7), 743-9.

3. Na, S.; Bandeira, N.; Paek, E., Fast multi-blind modification search through tandem mass spectrometry. _Mol Cell Proteomics _ **2012,** _11_ (4), M111 010199.

4. Scherl, A.; Shaffer, S. A.; Taylor, G. K.; Hernandez, P.; Appel, R. D.; Binz, P. A.; Goodlett, D. R., On the benefits of acquiring peptide fragment ions at high measured mass accuracy. _J Am Soc Mass Spectrom _ **2008,** _19_ (6), 891-901.

5. Cox, J.; Michalski, A.; Mann, M., Software lock mass by two-dimensional minimization of peptide mass errors. _J Am Soc Mass Spectrom _ **2011,** _22_ (8), 1373-80.

6. Shortreed, M. R.; Wenger, C. D.; Frey, B. L.; Sheynkman, G. M.; Scalf, M.; Keller, M. P.; Attie, A. D.; Smith, L. M., Global Identification of Protein Post-translational Modifications in a Single-Pass Database Search. _J Proteome Res _ **2015,** _14_ (11), 4714-20.

7. Cesnik, A. J.; Shortreed, M. R.; Sheynkman, G. M.; Frey, B. L.; Smith, L. M., Human Proteomic Variation Revealed by Combining RNA-Seq Proteogenomics and Global Post-Translational Modification (G-PTM) Search Strategy. _J Proteome Res _ **2016,** _15_ (3), 800-8.