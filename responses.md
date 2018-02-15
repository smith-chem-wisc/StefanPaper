# Responses

## To Editor

### 1

Done

### 2


### 3

Done

### 4

Done by removing the hyperref package

### 5

### 6

### 7

My ORCID is provided in the submission, not sure what I need to do here. 

## To Reviewer 1

### 1

Done

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

The group FDR is implemented in the multi-notch search, by using notch-specific FDRs. Thus, G-PTM-D augmentation is conservative about adding modifications corresponding to exotic/problematic notches. MetaMorpheus tsv outputs have a dedicated column called QValueNotch which displays the q-value for the specific notch. We added this note to the paper.

We will consider having modification-specific fdrs in future releases! Thank you for the suggestion.

### 3

Protein-level inference is currently done using all modified peptides. 

### 4

We added a note about the PeptideProphet extended mass model to the manuscript.

### 5

MetaMorpheus is designed to work on machines with 16 GB RAM. When a large amount of memory is avaiable, a user is able to select parallel searches which would utilize the avaialble memory efficiently, thus speeding up searches of mulitple files at the same time.

NOT SURE WHERE TO INCLUDE THIS INFORMATION IN THE DOCUMENT
