import numpy as np
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task2Search\allPSMs_3.5aroundZero.psmtsv", sep='\t')
#data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task4Search\allPSMs_3.5aroundZero.psmtsv", sep='\t')

#data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-04-10-15-00-59\Task2Search\allPSMs_3.5aroundZero.psmtsv", sep='\t')
#data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-04-10-15-00-59\Task4Search\allPSMs_3.5aroundZero.psmtsv", sep='\t')


data_sorted = data.sort_values(['MassDiff (Da)'], ascending=True)

massDiffs=data_sorted['MassDiff (Da)'].values
B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue_notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

ok = plt.subplot(321)

halfWidth = 3.5
min1 = -halfWidth
max1 = halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.01), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =int((max1-min1)/0.01), range=[min1, max1], label = "Decoys")

plt.legend()

#plt.xlabel("Mass Diff")
plt.ylabel("Count")
plt.title("PSMs within $\pm 2.5$")
ok.set_yscale("log", nonposy='clip')

ok = plt.subplot(322)



halfWidth = 0.1
min1 = -halfWidth
max1 = halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.title("PSMs around 0")
#plt.xlabel("Mass Diff")
plt.ylabel("Count")
ok.set_yscale("log", nonposy='clip')

plt.annotate('Lys->Gln', xy=(-0.036386, 70), xytext=(-0.036386-0.04, 100), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Gln->Lys', xy=(0.036386, 30), xytext=(0.036386+0.02, 100), arrowprops=dict(facecolor='black', shrink=0.05))




ok = plt.subplot(323)
halfWidth = 0.1
min1 = -1-halfWidth
max1 = -1+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

#plt.xlabel("Mass Diff")
plt.ylabel("Count")
#ok.set_yscale("log", nonposy='clip')
plt.title("PSMs around -1")

plt.annotate('Glu->Lys', xy=(-0.947630, 13), xytext=(-0.947630+0.05, 23), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Asn->Xle', xy=(-0.958863, 15), xytext=(-0.958863+0.01, 25), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Asp->Asn or Glu->Gln', xy=(-0.984016, 50), xytext=(-0.984016+0.03, 60), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('H(-1)', xy=(-1.007825, 50), xytext=(-1.007825-0.06, 60), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('H(-3) N(-1) O', xy=(-1.031634, 30), xytext=(-1.031634-0.06, 40), arrowprops=dict(facecolor='black', shrink=0.05))


ok = plt.subplot(324)



halfWidth = 0.1
min1 = 1-halfWidth
max1 = 1+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

#plt.xlabel("Mass Diff")
plt.ylabel("Count")
ok.set_yscale("log", nonposy='clip')
plt.title("PSMs around 1")

plt.annotate('Lys->Glu', xy=(0.947630, 13), xytext=(0.947630-0.05, 23), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Xle->Asn', xy=(0.958863, 20), xytext=(0.958863-0.05, 45), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Deamidation', xy=(0.984016, 200), xytext=(0.984016-0.10, 220), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('1 Mm', xy=(1.0025, 100), xytext=(1.024, 120), arrowprops=dict(facecolor='black', shrink=0.05))

ok = plt.subplot(325)




halfWidth = 0.1
min1 = -2-halfWidth
max1 = -2+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]
plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

#plt.xlabel("Mass Diff")
plt.ylabel("Count")
#ok.set_yscale("log", nonposy='clip')
plt.title("PSMs around -2")



ok = plt.subplot(326)

halfWidth = 0.1
min1 = 2-halfWidth
max1 = 2+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

#plt.xlabel("Mass Diff")
plt.ylabel("Count")
ok.set_yscale("log", nonposy='clip')
plt.title("PSMs around 2")

plt.annotate('Xle->Asp', xy=(1.942879, 15), xytext=(1.942879-0.07, 17), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Thr->Cys', xy=(1.961506, 21), xytext=(1.961506-0.05, 26), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Double Deamidation', xy=(1.968032, 33), xytext=(1.968032-0.05, 36), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Val->Thr', xy=(1.979265, 30), xytext=(1.979265-0.07, 33), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Glu->Met', xy=(1.997892, 30), xytext=(1.997892, 33), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('2 Mm', xy=(2.005, 28), xytext=(2.024, 30), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Pro->Val', xy=(2.015650, 20), xytext=(2.015650+0.03, 23), arrowprops=dict(facecolor='black', shrink=0.05))



plt.show()
