- Use superscript to match authors with institutions on Title page

•Page 18, List of supporting information:
1) As to not confuse the reader, supporting files should be referred to by the same name in the paper as they appear on the file labels.  

•References:
1) Ref# 5 and 16 should be checked for completeness
2) Remove color ink in superscript

•Supporting Information files:
1) Suppl.xlsx file: File name and caption should be inserted into the table.
2) Cover page for Supporting Information is required:
Use heading, Supporting Information, followed by manuscript title, list of authors & affiliations, and a table of contents (list of supplementary components and captions). Number SI pages as S-1, S-2, etc.

•ORCID: Authors submitting manuscript revisions are required to provide their own validated ORCID iDs before completing the submission, if an ORCID iD is not already associated with their ACS Paragon Plus user profiles. This iD may be provided during original manuscript submission or when submitting the manuscript revision. You can provide only your own ORCID iD, a unique researcher identifier. If your ORCID iD is not already validated and associated with your ACS Paragon Plus user profile, you may do so by following the ORCID-related links in the Email/Name section of your ACS Paragon Plus account. All authors are encouraged to register for and associate their own ORCID iDs with their ACS Paragon Plus profiles. The ORCID iD will be displayed in the published article for any author on a manuscript who has a validated ORCID iD associated with ACS Paragon Plus when the manuscript is accepted. Learn more at http://www.orcid.org.

Format for Response to reviewers’ comments:

•Your response to Reviewer's comments should 1) use the same reviewer I.D. Number, as in Reviewer's comments provided in our email, 2) be placed after the reviewer's comments, with detailed description of the changes made to the manuscript, or provide a rebuttal, 3) also provide as separate files per each response.

•Provide a highlighted version with changes made as ”Supporting Information for Review Only” in addition to an unmarked version

•This revision is due on 21-Mar-2018, with a maximum extension of 30 days with the Editor’s approval.  Special circumstance would be considered.

To Revise Your Manuscript on the Web:

To revise your manuscript, log into ACS Paragon Plus with your ACS ID at http://paragonplus.acs.org/login and select "My Authoring Activity". There you will find your manuscript title listed under "Revisions Requested by Editorial Office." Your original files are available to you when you upload your revised manuscript. If you are replacing files, please remove the old version of the file from the manuscript before uploading the new file.

ACS Publications uses CrossCheck's iThenticate software to detect instances of similarity in submitted manuscripts. In publishing only original research, ACS is committed to deterring plagiarism, including self-plagiarism. Your manuscript may be screened for similarity to published material.

Thank you for considering the Journal of Proteome Research as a forum for the publication of your work.

With sincere regards,

John Yates
Editor-in-Chief
Journal of Proteome Research
Phone: 858-784-2706
Fax: 202-559-0828
Editor Email: eic@jpr.acs.org

------------------------------------

Reviewer(s)' Comments to Author:

Reviewer: 1

Comments to the Author

Here the authors present a concise and well documented manuscript detailing significant changes to the Morpheus engine and the GPTMD
search space.  There are no major problems with the paper, and the outcome of the approach, its goals and results are clear
and well documented. I have a few minor concerns I wouuld like addressed below, but overall the manuscript is excellent and
well written.


Fig 1 does not enhance my understanding of the changes in the GPTMD, or its processing steps.  Have you considered a parallel
figure in which the original algorithim is traced as compared to distinguishing features in the 'enhanced' approach. The figure
itself, is also a little sloppy, boxes aligned on one margin are not aligned. For example none of the boxes align on the right margin
the effect is distracting.

Fig 2. Mass error and mass in figure 2 have units of Th ? I am not familiar with this unit, does it mean thousands ? Maybe
mmu on the y and Da or m/z on X would be more

What is the effect on a data set that is already well calibrated. The systematic drift in the ideal data set is large and not
Gaussian. For a data set of Gaussian distribution or not as wide, the improvement is likely minimal, or potentially worse as
it might recalibrate to some local-minima and not improve the results and/or processing.  Potentially testable for quick comment
by reprocessing data set after calibration (eg. twice) or taking a random file from you lab you know has better m/z error distribution
properites.


Notch improvement
I think the implementation of notch processing is very well presented and timely. I am not satisfied that its utility in this
context has been adequately addressed. All other aspects of the improvements in the GPTM are addrssed in specific computed detail, but notch
improvements are described but not readily verified. Eg there isn't an accepted number of right and wrong answers for the test
dataset. I would like to see a case in which you take a defined or previously published SILAC, dimethyl dataset and simply set the notches for the
corresponding mass shift (delta 4, 8) etc. In this way you can very quickly and accurate define the catch rate and other
factors from notch search as compared to simply defining light and heavy explicitly.  In the case of SILAC data in particular, this may offer
important advantages to partial incorporations due to arginine pathways which are hard to supress

Reviewer: 2

Comments to the Author
The manuscript by Solntsev et al. describes improvements to a previously published computational strategy G-PTM-D. Overall, G-PTM-D strategy, and the corresponding MetaMorpheus software tool, is a very valuable option in the arsenal of tools for global PTM analysis.  The multi-notch strategy is perhaps the most interesting part in the manuscript. However, I have several technical questions and concerns that need to be addressed.

1. One of the ‘new’ components described in the text is what the authors call “limited multi-notch”.  In fact, almost 3 pages of the manuscript are dedicated to that part, including a sentence “We propose a limited multi-notch search…”.  Unless I misunderstand something here, I cannot see how it is different from what has been implemented in most existing search tools for years. Every useful tool I know, Tandem, MSGF+, Comet, MSFragger, Sequest, etc. have an ‘isotope error option’.  For example, in X! Tandem, it is specific using the following option:
<note type="input" label="spectrum, parent monoisotopic mass isotope error">yes</note>
You can read more about this option here: http://www.thegpm.org/tandem/api/spmmie.html

In Comet: see here http://comet-ms.sourceforge.net/parameters/parameters_201701/isotope_error.php

In MSFragger use isotope error option e.g.    isotope_error = /0/1/2       # 0=off, -1/0/1/2/3 (standard C13 error)

I suggest that the authors shorten the text related to the limited multi-notch approach. For me it would be enough if they just said that they implemented a common strategy for allowing C12/C13 errors as in other tools.

2. The authors do not really address the issue of FDR estimates, even at the PSM level, with respect to modified peptides. While the global (dataset-wide) FDR may be accurate, FDR for different subsets of PSMs is expected to vary widely. When performing searches such as multi-notch searches, open searches, or searches with many variable modifications or proteogenomic searches, it is important to realize that FDR for subsets of peptides with unusual modifications/mass-shifts or novel peptides will be significantly higher than that for the typical unmodified tryptic peptides. Thus, there is a need to perform class-specific (also referred to as group-specific FDR). In MSFragger, for example, this is addressed by modeling PSMs using a probability model that separates peptides into groups with different mass shifts. This ensures that PSM scores (probabilities) are re-calibrated to take into account the differences in the likelihood of observing a peptide with a particular modification (mass-shift) in the dataset. I recommend that the authors discuss this, and if not currently implemented in MetaMorheus, consider this for future work.

3. It is not clear if the authors present MetaMorpheus with G-PTM-D as a tool that can be applied for standard proteomic analysis (and not just as a complementary tool to look for more PTMs). If the former, they need to discuss the protein inference strategy in the context of multi-notch searches. As discussed in the MSFragger manuscript, a conservative option is recommended in which peptides with mass shifts are excluded from the protein inference step except those corresponding to C12/C13 errors, M+16, and N-term +42. While using 208 known modifications in MetaMorheus is not as risky as performing open search in that regard, perhaps not all of those 208 mass shifts should be considered (especially if MetaMorheus does not perform modification-specific modeling, see my point # 2 above). Please comment on this.

4. The authors discuss advantages of multi-notch searches compared to open searches. While I agree with their statement as it relates to ‘bare’ open searching, I want to point out that some of those concerns for open searches can and should be addressed by downstream tools. For example, on p.14, the authors illustrate their case using a peptide ATPARA… that was identified in open search with a score of 17.231, 1 missed cleavage, and large and unexpected negative mass-shift of -416.303. The correct PSM in this case is a shorter peptide, slightly lower scoring (16.246), without missed cleavage, and having an explainable mass shift of 79.9655. As described in the MSFragger manuscript, open search results (and any search results in general) have to be carefully modeled post-database search using downstream statistical tools such as TPP, Percolator, etc. For example, the extended mass model of PeptideProphet (which also uses the number missed cleavages) would likely penalize the incorrect identification (with the unusual -416.303 mass shift and 1 missed cleavage) to the point where it would not pass strict FDR cutoffs. It is true that the post-database search modeling in its simplest form would not rescue the second best match to this spectrum (correct PSM) if only the top match is considered. However, at least it would not let this false identification to get through. If not this one ID in particular, it would reduce significantly the number of such mistakes dataset-wide.  I hope the authors can discuss the importance of post-database search tools in addressing some of the limitations of open searches, or any searches for that matter including multi-notch searches.

5. The results shown in the manuscript were obtained on a pretty powerful workstation with 24 cores and 128Gb RAM. Are there any RAM limitations for running MetaMorheus on large datasets like the multi-fraction Jurkat dataset?
