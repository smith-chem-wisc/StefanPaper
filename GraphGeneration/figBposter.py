import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas


matplotlib.rcParams.update({'font.size': 24})


data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-05-18-28-01\Task4Search\allPSMs_-187andUp.psmtsv", sep='\t')

height = 5
width = 7
plt.figure(figsize=(width, height))

data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values

B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

halfWidth = 0.1 
min1 = 1-halfWidth
max1 = 1+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]

plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")

plt.ylabel("PSM Count")
plt.axis([0.9, 1.1, 0, 1200])

plt.title("Mass Diffs Around 1 Da")

plt.annotate('Deamidation', xy=(0.984016, 900), xytext=(0.984016+0.02, 700), arrowprops=dict(arrowstyle="->"))
plt.annotate('1 Mm', xy=(1.0029, 150), xytext=(1.027, 180), arrowprops=dict(arrowstyle="->"))


plt.tight_layout()

plt.savefig('figBposter.eps', format='eps', dpi=1200)
plt.savefig('figBposter.png', format='png', dpi=1200)


plt.show()
