# Responses

## To Editor

### 1

> Use superscript to match authors with institutions on Title page

Done

### 2

> •Page 18, List of supporting information: 1) As to not confuse the reader, supporting files should be referred to by the same name in the paper as they appear on the file labels.  

Done

### 3

> •References: 1) Ref# 5 and 16 should be checked for completeness

Done

### 4

> References: Remove color ink in superscript

Done by removing the hyperref package

### 5

> Supporting Information: Suppl.xlsx file: File name and caption should be inserted into the table.

Done

### 6

>  Cover page for Supporting Information is required: Use heading, Supporting Information, followed by manuscript title, list of authors & affiliations, and a table of contents (list of supplementary components and captions). Number SI pages as S-1, S-2, etc.

Done

### 7

> ORCID: Authors submitting manuscript revisions are required to provide their own validated ORCID iDs before completing the submission

My ORCID is provided in the submission, not sure what I need to do here. 

## To Reviewer 1

### 1

> Fig 1 does not enhance my understanding of the changes in the GPTMD, or its processing steps.  Have you considered a parallel
figure in which the original algorithim is traced as compared to distinguishing features in the 'enhanced' approach. The figure
itself, is also a little sloppy, boxes aligned on one margin are not aligned. For example none of the boxes align on the right margin
the effect is distracting.

Done by changing the figure to 

### 2

Done

### 3

Effect on a data set that is already calibrated is non-existent, due to the fact that the calibration procedure only accepts changes if a test database search results show improvement. We tested this, and observed that mulitple calibration tasks in MetaMorpheus do not change a file following the initial calibration round. This is noted in the calibration supplement.

### 4

TODO BRIAN COMMENTS THANKS

## To Reviewer 2

### 1

The limited multi-notch search has functionality identical to the isotope error option in many current search tools. We made sure that the revised version is clear about this, and we removed any wording that may suggest that this is novel, such as "we propose". Still, the property that it eliminates some wrong matches parallels the discussion in the following multi-notch search section. We feel that it adds to the discussion, and is necessary to make the manuscript complete. 

We amended the manuscript as follows:

> A multi-notch search is a remedy to the trade-offs caused by choosing a narrow (few ppm) or wide (few Da) precursor mass tolerance during a traditional narrow-window search. It is not novel, and many useful search tools such as Tandem, MSGF+, Comet, MSFragger, Sequest have this search functionality under names such as "isotope error option".

### 2

The group FDR is implemented in the multi-notch search, by using notch-specific FDRs. Thus, G-PTM-D augmentation is conservative about adding modifications corresponding to exotic/problematic notches. MetaMorpheus tsv outputs have a dedicated column called QValueNotch which displays the q-value for the specific notch. 

We amended the manuscript as follows:

> The results of a multi-notch search are assessed using notch-specific FDRs, computed individually for each notch, similarly to MSFragger.

We will consider having modification-specific FDRs in future software releases! Thank you for the suggestion.

### 3

Protein-level inference is currently done using all modified peptides. 

### 4

We added a note about the PeptideProphet extended mass model to the manuscript.

We amended the manuscript as follows:

> It is important to note that there exist post-processing tools that would push identifications with unknown mass shifts and large numbers of missed cleavages down the list, such as the PeptideProphet extended mass model.

### 5

MetaMorpheus is designed to work on machines with 16 GB RAM. When a large amount of memory is avaiable, a user is able to select parallel searches which would utilize the avaialble memory efficiently, thus speeding up searches of mulitple files at the same time.

NOT SURE WHERE TO INCLUDE THIS INFORMATION IN THE DOCUMENT
