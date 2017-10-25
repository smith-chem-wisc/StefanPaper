import numpy as np
import matplotlib.pyplot as plt
import pandas

height = 6
width = 7
plt.figure(figsize=(width, height))

#################

# data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\2017-10-20-12-48-57-zeroAndMidPhosphoSulfo\Task1-SearchTask\aggregatePSMs_custom.psmtsv", sep='\t')
data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\2017-10-24-12-02-12-noDeisotopeZeroSulfoPhospho\Task1-SearchTask\aggregatePSMs_zeroAndMidSulfoPhospho.psmtsv", sep='\t')

data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)

massDiffs=data_sorted['Mass Diff (Da)'].values
scores=data_sorted['Score'].values
notches=data_sorted['Notch'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

scoreCutoff = min(scores[(C<0.01) &(notches=="1")])

print(scoreCutoff)

massDiffsHighConf = massDiffs[scores>scoreCutoff]
TDhighConf = B[scores>scoreCutoff]

#################

ok = plt.subplot(222)

halfWidth = 0.02 
min1 = -halfWidth
max1 = halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]

print(len(massDiffsHighConf1))
print(len(massDiffsHighConf1decoy))

plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs within $\pm 0.02$ Da")

ok.set_xlim([min1, max1])
ok.set_ylim([0,75000])

#################

ok = plt.subplot(224)

halfWidth = 0.02 
centerMass = 79.961573
min1 = centerMass-halfWidth
max1 = centerMass+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]

print(len(massDiffsHighConf1))
print(len(massDiffsHighConf1decoy))

plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs within $\pm 0.02$ Da")

ok.set_xlim([min1, max1])
ok.set_ylim([0,290])



#################

# data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\500daOpen\Task1-SearchTask\aggregatePSMs_500daltonsAroundZero.psmtsv", sep='\t')
data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\2017-10-24-12-00-21-500daNoDeisotope\Task1-SearchTask\aggregatePSMs_500daltonsAroundZero.psmtsv", sep='\t')

data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)

massDiffs=data_sorted['Mass Diff (Da)'].values

scores=data_sorted['Score'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue'].values

massDiffsHighConf = massDiffs[scores>scoreCutoff]
TDhighConf = B[scores>scoreCutoff]

#################

ok = plt.subplot(221)

halfWidth = 0.02 
min1 = -halfWidth
max1 = halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]

print(len(massDiffsHighConf1))
print(len(massDiffsHighConf1decoy))

plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs within $\pm 0.02$ Da")

ok.set_xlim([min1, max1])
ok.set_ylim([0,75000])

#################

ok = plt.subplot(223)

halfWidth = 0.02 
centerMass = 79.961573
min1 = centerMass-halfWidth
max1 = centerMass+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]

print(len(massDiffsHighConf1))
print(len(massDiffsHighConf1decoy))

plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs within $\pm 0.02$ Da")

ok.set_xlim([min1, max1])
ok.set_ylim([0,290])


plt.tight_layout()


plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig6-ZeroAndPhospho.png', format='png', dpi=600)


plt.show()
