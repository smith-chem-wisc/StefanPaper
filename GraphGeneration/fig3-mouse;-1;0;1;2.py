import numpy as np
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-05-18-28-01\Task4Search\allPSMs_-187andUp.psmtsv", sep='\t')




height = 6
width = 7
plt.figure(figsize=(width, height))

data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values

#data_sorted = data.sort_values(['MassDiffToBestMass (Da)'], ascending=True)
#massDiffs=data_sorted['MassDiffToBestMass (Da)'].values

B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

ok = plt.subplot(221)

halfWidth = 3.5
min1 = -halfWidth
max1 = halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.01), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =int((max1-min1)/0.01), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs within $\pm 2.5$ Da")
ok.set_yscale("log", nonposy='clip')

ok = plt.subplot(222)
#ok.set_yscale("log", nonposy='clip')
halfWidth = 0.1
min1 = -1-halfWidth
max1 = -1+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()
plt.ylabel("Count")

plt.title("PSMs around -1 Da")

#plt.annotate('Glu->Lys', xy=(-0.947630, 18), xytext=(-0.947630+0.015, 33), arrowprops=dict(arrowstyle="->"))
plt.annotate('Asn->Xle', xy=(-0.958863, 20), xytext=(-0.958863+0.007, 39), arrowprops=dict(arrowstyle="->"))
plt.annotate('Asp->Asn or\nGlu->Gln\nor Amidation', xy=(-0.984016, 48), xytext=(-0.984016+0.015, 68), arrowprops=dict(arrowstyle="->"))
#plt.annotate('-1 Mm', xy=(-1.0029, 68), xytext=(-1.0029+0.020, 80), arrowprops=dict(arrowstyle="->"))
plt.annotate('H(-1)', xy=(-1.007825, 100), xytext=(-1.007825-0.05, 110), arrowprops=dict(arrowstyle="->"))
plt.annotate('H(-3) N(-1) O', xy=(-1.031634, 30), xytext=(-1.031634-0.075, 50), arrowprops=dict(arrowstyle="->"))


ok = plt.subplot(223)


#ok.set_yscale("log", nonposy='clip')

halfWidth = 0.1
min1 = 1-halfWidth
max1 = 1+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs around 1 Da")

#plt.annotate('Lys->Glu', xy=(0.947630, 60), xytext=(0.947630-0.057, 230), arrowprops=dict(arrowstyle="->"))
#plt.annotate('Xle->Asn', xy=(0.958863, 45), xytext=(0.958863-0.032, 400), arrowprops=dict(arrowstyle="->"))
plt.annotate('Deamidation', xy=(0.984016, 1300), xytext=(0.984016-0.09, 1500), arrowprops=dict(arrowstyle="->"))
plt.annotate('1 Mm', xy=(1.0029, 240), xytext=(1.027, 350), arrowprops=dict(arrowstyle="->"))



ok = plt.subplot(224)

#ok.set_yscale("log", nonposy='clip')


halfWidth = 0.1
min1 = 2-halfWidth
max1 = 2+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")


plt.title("PSMs around 2 Da")

#plt.annotate('Xle->D', xy=(1.942879, 15), xytext=(1.942879-0.05, 55), arrowprops=dict(arrowstyle="->"))
#plt.annotate('Thr->Cys', xy=(1.961506, 18), xytext=(1.961506-0.07, 125), arrowprops=dict(arrowstyle="->"))
plt.annotate('Double\nDeamidation', xy=(1.968032, 15), xytext=(1.968032-0.077, 20), arrowprops=dict(arrowstyle="->"))
plt.annotate('Val->Thr', xy=(1.979265, 25), xytext=(1.979265-0.028, 30), arrowprops=dict(arrowstyle="->"))
#plt.annotate('1Mm\nand\nDeamidation', xy=(1.0029+0.984016, 25), xytext=(1.997-0.07, 340), arrowprops=dict(arrowstyle="->"))
#plt.annotate('Glu->Met', xy=(1.997892, 22), xytext=(1.997+0.04, 180), arrowprops=dict(arrowstyle="->"))
plt.annotate('2 Mm', xy=(2.0052, 20), xytext=(2.02, 23), arrowprops=dict(arrowstyle="->"))
plt.annotate('Pro->Val', xy=(2.015650, 13), xytext=(2.015650+0.012, 17), arrowprops=dict(arrowstyle="->"))

plt.tight_layout()


plt.savefig('fig3mouse-1012.eps', format='eps', dpi=1200)
plt.savefig('fig3mouse-1012.png', format='png', dpi=1200)


plt.show()
