import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas


matplotlib.rcParams.update({'font.size': 24})


#data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-30-10-25-53\Task1Search\allPSMs_name.psmtsv", sep='\t')
data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-05-18-28-01\Task2Calibrate\2017-05-30-10-26-30\Task1Search\allPSMs_name.psmtsv", sep='\t')


height = 5
width = 7
plt.figure(figsize=(width, height))

data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values

B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

halfWidth = 0.03 
min1 = 79.961573-halfWidth
max1 = 79.961573+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="T")]

plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")

plt.ylabel("PSM Count")
plt.xlabel("Mass Diff (Da)")


plt.annotate('Sulfo', xy=(79.956815, 50), xytext=(79.94, 50), arrowprops=dict(arrowstyle="->"))
plt.annotate('Phospho', xy=( 79.966331, 100), xytext=(79.97, 100), arrowprops=dict(arrowstyle="->"))

plt.axis([min1, max1, 0, 150])

plt.title("Calibrated")

plt.tight_layout()

plt.savefig('figPhosphorylationCalib.eps', format='eps', dpi=1200)
plt.savefig('figPhosphorylationCalib.png', format='png', dpi=1200)


plt.show()
