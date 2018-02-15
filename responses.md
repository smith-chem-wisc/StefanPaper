# Responses

## To Editor

## To Reviewer 1

## To Reviewer 2

### 1

The limited multi-notch search has functionality identical to the isotope error option in many current search tools. We made sure that the revised version is clear about this, and we removed any wording that may suggest that this is novel, such as "we propose". Still, the property that it eliminates some wrong matches parallels the discussion in the following multi-notch search section. We feel that it adds to the discussion, and is necessary to make the manuscript complete. 

### 2

The group FDR is implemented in the multi-notch search, by using notch-specific FDRs. Thus, G-PTM-D augmentation is conservative about adding modifications corresponding to exotic/problematic notches. The final results do not seem to necessitate modification-specific FDR, see original G-PTM-D paper. The reason for this is that modified decoy peptides are included in the search, something that is not possible with a standard open or multi-notch search.

### 3

Protein-level inference is done using all modified peptides, since they pass an FDR threshold. This is different from MSFragger, since the problems with accepting mass shifts are more severe than accepting modified peptides.

### 4

### 5

MetaMorpheus is designed to work on machines with 16 GB RAM. When a large amount of memory is avaiable, a user is able to select parallel searches which would utilize the avaialble memory efficiently, thus speeding up searches of mulitple files at the same time.
