import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy
import pandas

data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-02-25-13-59-40\Task4Search\aggregateintervals[-187.000-Infinity].psmtsv", sep='\t')

data_sorted = data.sort_values(['MassDiff (Da)'], ascending=True)

massDiffs=data_sorted['MassDiff (Da)'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue_notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

fig, axes = plt.subplots(nrows=1, ncols=2)

halfWidth = 0.01
center = 113.08406
min1 = center-halfWidth
max1 = center+halfWidth

bins = 25
massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]
axes[0].hist(massDiffsHighConf1, bins  = bins, range=[min1, max1], label = "Targets")
axes[0].hist(massDiffsHighConf1decoy, bins  =bins, range=[min1, max1], label = "Decoys")

from scipy.interpolate import UnivariateSpline
s = massDiffsHighConf1decoy
p, x = np.histogram(s, bins=bins) # bin it into bins
x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
f = UnivariateSpline(x, p, s=222)
axes[0].plot(x, f(x))

halfWidth = 0.01
center = 79.961573 
min1 = center-halfWidth
max1 = center+halfWidth
massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]
axes[1].hist(massDiffsHighConf1, bins  = 25, range=[min1, max1], label = "Targets")
axes[1].hist(massDiffsHighConf1decoy, bins  =25, range=[min1, max1], label = "Decoys")


ax2 = axes[1].twinx()
df = pandas.DataFrame(massDiffsHighConf1)
df.plot(ax=ax2,kind='density')



plt.show()
