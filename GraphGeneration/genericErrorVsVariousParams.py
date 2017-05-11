import numpy as np
import matplotlib.pyplot as plt
import pandas

nice= pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-08-14-03-16\Task1Calibrate\04-29-13_B6_Frac9_9p5uLafterfc4after.ms1dptsv", sep='\t')
#nice= pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-08-14-03-16\Task1Calibrate\04-29-13_B6_Frac9_9p5uLafterfc4after.ms2dptsv", sep='\t')


plt.figure(1)
plt.subplot(331)
plt.plot(nice['mz'],nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(nice['mz']), max(nice['mz']), zorder = 10)
plt.xlabel("mz")

plt.subplot(332)
plt.plot(nice['rt'],nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(nice['rt']), max(nice['rt']), zorder = 10)
plt.xlabel("rt")

plt.subplot(333)
plt.plot(np.log(nice['intensity']),nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice['intensity'])), max(np.log(nice['intensity'])), zorder = 10)
plt.xlabel("intensity")

plt.subplot(334)
plt.plot(np.log(nice['TIC']),nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice['TIC'])), max(np.log(nice['TIC'])), zorder = 10)
plt.xlabel("TIC")

plt.subplot(335)
plt.plot(np.log(nice['InjectionTime']),nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice['InjectionTime'])), max(np.log(nice['InjectionTime'])), zorder = 10)
plt.xlabel("InjectionTime")

plt.subplot(336)
plt.plot(nice['Score'],nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(nice['Score']), max(nice['Score']), zorder = 10)
plt.xlabel("score")

plt.subplot(337)
plt.plot(nice['Peptide Monoisotopic Mass'],nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(nice['Peptide Monoisotopic Mass']), max(nice['Peptide Monoisotopic Mass']), zorder = 10)
plt.xlabel("peptide mass")

plt.subplot(338)
plt.plot(nice['Mass Diff (Da)'],nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(nice['Mass Diff (Da)']), max(nice['Mass Diff (Da)']), zorder = 10)
plt.xlabel("Mass Diff (Da)")

plt.subplot(339)
plt.plot(nice['Variable Mods'],nice['Label'], 'bo',markersize = .3)
plt.hlines(0, min(nice['Variable Mods']), max(nice['Variable Mods']), zorder = 10)
plt.xlabel("Num Var Mods")

plt.show()
