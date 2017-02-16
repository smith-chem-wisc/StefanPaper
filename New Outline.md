# New Outline

1. 1.Abstract
2. 2.Introduction
  1. a.PTMs important. GPTM-D and MOD-a and others have limitations, improvements are necessary
  2. b.We propose:
    1. i.Calibration procedure short overview
    2. ii.Enhanced GPTM-D workflow short overview
    3. iii.Discovery of modifications not in database short overview

  3. c.Results summary

3. 3.Experimental Procedures
  1. a.Describe MetaMorpheus parameters
  2. b.Describe datasets
    1. i.Mouse
    2. ii.Jurkat

4. 4.Results and Discussion

Workflows overview, BEAUTIFUL FLOWCHART FIGURE

1.
  1. a.Calibration results
    1. i. **Show narrower peaks, centered at the right values (because of calibration)**

  2. b.Enhanced GPTM-D workflow detailed description
    1. i.Notch search
      1. 1. **Computational time and FDR results (because of notches)**

    2. ii.Final search with notches
      1. 1. **PSMs, Unique Peptides, Base Peptides, Proteins go up (because of notches and calibration)**

  3. c.Discovery of modifications not in database detailed description
    1. i.Comb Search
      1. 1. **Computational time and FDR results (because of notches)**
      2. 2. **Discernibility of peaks plots (because of calibration)**

    2. ii.Peak analysis heuristic. Assignment of peaks:
      1. 1.Final notches: 0, 1.003. Localizeable Modifications: Acetlyation, Methylation, Adducts, etc. Labile Modifications: Sulfo, Phospho. Combos. Substitutions and Removals
      2. 2. **Discovery of new modifications results**
        1. a.Carbon adduct?

2. 5.Conclusion
3. 6.Supplementary
  1. a.MetaMorpheus
    1. i.Addition of Calib+GPTMD
    2. ii.Custom modifications
    3. iii.Labile modifications
    4. iv.Chain search

  2. b.GPTM-D Enhancements
    1. i.Combinations
    2. ii.Missed monoisotopes

  3. c.Calibration procedure