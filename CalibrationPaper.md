# Rapid and Accurate Discovery of Peptide Posttranslational Modifications Using Calibrated Tandem Mass Spectra and Morpheus GPTM-D with Spectral Notches

# Introduction

The calibration of spectra files and algorithmic improvements in the peptide dictionary search improves the accuracy and efficiency of new posttranslational-modification (PTM) identification.

2. Motivation

Physical measurements introduce noise, and instruments that take multiple measurements often have correlated noise between different samples. Knowledge of what some of the measurements should be, paired with a correlated noise assumption, enables us to make an intelligent guess at what the noise is for the rest of the measurements. This is indeed the scenario with mass spectrometry data, where the knowledge of the true mz values for some peaks comes from identified peptide sequences.

3. Calibration

a. Describe the differences and similarities with the original calibration paper. Explain how we extended the idea.

4. Notch Search

5. Results

a. Only spectra files calibration, no additional search done. Show MSE values for different calibration functions, pick one, and say why it's better than others

b. A new normal Morpheus run comparison: 10ppm, vs 3ppm (4 runs)

i. Show that precursor mass errors are centered at zero and have smaller variance

ii. Show that there are more PTMs identified we are confident it

iii. Show that decoy PTMs are pushed down the list

Compare with 11 cell line paper, and with Jurkat/Mouse paper

c. Notches

i. Show that now are able to discern between PTMs with similar mass errors (ones that are only different because of the mass defect)

d. Show the improvement in search time due to the new notches option