import numpy as np
import matplotlib.pyplot as plt
import pandas

#data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-02-25-13-57-45\Task4Search\aggregateintervals[-187.000-Infinity].psmtsv", sep='\t')
data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-02-25-13-59-40\Task4Search\aggregateintervals[-187.000-Infinity].psmtsv", sep='\t')

data_sorted = data.sort_values(['MassDiff (Da)'], ascending=True)

massDiffs=data_sorted['MassDiff (Da)'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue_notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

ok = plt.subplot(122)

halfWidth = 0.05
min1 = 21.96-halfWidth
max1 = 21.96+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]

print(massDiffsHighConf1)


a = plt.hist(massDiffsHighConf1, bins  = 250, range=[min1, max1], label = "Targets")
b = plt.hist(massDiffsHighConf1decoy, bins  =250, range=[min1, max1], label = "Decoys")

ok.set_yscale("log", nonposy='clip')

plt.legend()

plt.xlabel("Mass Diff")
plt.ylabel("Count")
plt.title("PSMs around 113.084")
plt.annotate('Leucine Mass', xy=(113.08406, 50), xytext=(113.074, 40),
            arrowprops=dict(facecolor='black', shrink=0.05))
 
ok = plt.subplot(121)

halfWidth = 0.01
min1 = 79.961573-halfWidth
max1 = 79.961573+halfWidth

massDiffsHighConf2 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf2decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]

a = plt.hist(massDiffsHighConf2, bins  = 25, range=[min1, max1], label = "Targets")
b = plt.hist(massDiffsHighConf2decoy, bins  =25, range=[min1, max1], label = "Decoys")
 
plt.legend()
plt.xlabel("Mass Diff")
plt.ylabel("Count")
plt.title("PSMs around Sulfo and Phospho")

plt.annotate('Sulfo', xy=(79.956815, 28), xytext=(79.954, 33),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Phospho', xy=(79.966331, 50), xytext=(79.96, 40),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
