import numpy as np
import matplotlib.pyplot as plt
import pandas

height = 3
width = 7
plt.figure(figsize=(width, height))

#################

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\CAST\gptmd\Task1-GPTMDTask\PSMs.psmtsv", sep='\t')

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

ok = plt.subplot(121)

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

plt.annotate('?', xy=(79.962, 22), xytext=(79.955,30), arrowprops=dict(arrowstyle="->"))
plt.annotate('?', xy=(79.971, 20), xytext=(79.975,30), arrowprops=dict(arrowstyle="->"))

plt.legend()

plt.ylabel("Count")
plt.title("Uncalibrated")

ok.set_xlim([min1, max1])
ok.set_ylim([0,60])

#################

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\CAST\Calibrated\gptmd\Task1-GPTMDTask\PSMs.psmtsv", sep='\t')

data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)

massDiffs=data_sorted['Mass Diff (Da)'].values

scores=data_sorted['Score'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue'].values

massDiffsHighConf = massDiffs[scores>scoreCutoff]
TDhighConf = B[scores>scoreCutoff]

#################

ok = plt.subplot(122)

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

plt.annotate('sulfo', xy=(79.956, 23), xytext=(79.951,30), arrowprops=dict(arrowstyle="->"))
plt.annotate('phospho', xy=(79.967, 28), xytext=(79.971,30), arrowprops=dict(arrowstyle="->"))

plt.legend()

plt.ylabel("Count")
plt.title("Calibrated")

ok.set_xlim([min1, max1])
ok.set_ylim([0,60])

plt.tight_layout()


plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig7-ZeroAndPhospho.png', format='png', dpi=600)


plt.show()
