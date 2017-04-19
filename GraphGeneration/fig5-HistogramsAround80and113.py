import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#import scipy
import pandas


height = 3
width = 7


plt.figure(figsize=(width, height))

data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\2017-04-14-16-50-03\Task1Search\allPSMs_-187andUp.psmtsv", sep='\t')

data_sorted = data.sort_values(['MassDiff (Da)'], ascending=True)

massDiffs=data_sorted['MassDiff (Da)'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue_notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

ok = plt.subplot(121)

halfWidth = 0.01
center = 113.084064
min1 = center-halfWidth
max1 = center+halfWidth

bins = 21 
massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]
plt.hist(massDiffsHighConf1, bins  = bins, range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =bins, range=[min1, max1], label = "Decoys")


plt.legend()
plt.annotate('Leucine\nResidue\nMass', xy=(113.08406, 35), xytext=(113.08406-0.00857, 40), arrowprops=dict(arrowstyle="->"))

ok = plt.subplot(122)

halfWidth = 0.01
center = 79.961573 
min1 = center-halfWidth
max1 = center+halfWidth
massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]
plt.hist(massDiffsHighConf1, bins  = bins, range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =bins, range=[min1, max1], label = "Decoys")

plt.legend()

plt.annotate('Sulfo', xy=(79.956815, 28), xytext=(79.956815-0.00557, 33), arrowprops=dict(arrowstyle="->"))
plt.annotate('Phospho', xy=(79.966331, 45), xytext=(79.966331-0.00832, 50), arrowprops=dict(arrowstyle="->"))



plt.tight_layout() 
 

plt.savefig('fig5-HistogramsAround80and113.eps', format='eps', dpi=1200)
plt.savefig('fig5-HistogramsAround80and113.png', format='png', dpi=1200)



plt.show()
