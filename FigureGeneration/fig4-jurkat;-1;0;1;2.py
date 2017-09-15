import numpy as np
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\Jurkat\2017-07-31-17-44-19\Task2Search\aggregatePSMs_3.5aroundZero.psmtsv", sep='\t')




height = 6
width = 7
plt.figure(figsize=(width, height))

data['Mass Diff (Da)'] = pandas.to_numeric(data['Mass Diff (Da)'], errors='coerce')
data_sorted = data.sort_values(['Mass Diff (Da)'], ascending=True)
massDiffs=data_sorted['Mass Diff (Da)'].values

#data_sorted = data.sort_values(['MassDiffToBestMass (Da)'], ascending=True)
#massDiffs=data_sorted['MassDiffToBestMass (Da)'].values

B=data_sorted['Decoy/Contaminant/Target'].values
C=data_sorted['QValue Notch'].values

massDiffsHighConf = massDiffs[C<0.01]
TDhighConf = B[C<0.01]

ok = plt.subplot(221)

halfWidth = 3.505
min1 = -halfWidth
max1 = halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  = int((max1-min1)/0.01), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  =int((max1-min1)/0.01), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs within $\pm 3.5$ Da")
ok.set_yscale("log", nonposy='clip')

ok = plt.subplot(223)


#ok.set_yscale("log", nonposy='clip')

halfWidth = 0.1
min1 = -1-halfWidth
max1 = -1+halfWidth

massDiffsHighConf1 = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1)]
massDiffsHighConf1decoy = massDiffsHighConf[(massDiffsHighConf>min1) & (massDiffsHighConf<max1) & (TDhighConf=="D")]



plt.hist(massDiffsHighConf1, bins  =  int((max1-min1)/0.001), range=[min1, max1], label = "Targets")
plt.hist(massDiffsHighConf1decoy, bins  = int((max1-min1)/0.001), range=[min1, max1], label = "Decoys")

plt.legend()

plt.ylabel("Count")
plt.title("PSMs around -1 Da")

plt.annotate('Oxidation\n+Ammonia Loss', xy=(-1.031634,50), xytext=(-1.031634-0.075, 80), arrowprops=dict(arrowstyle="->"))
plt.annotate('Dehydro', xy=(-1.007825, 60), xytext=(-1,80), arrowprops=dict(arrowstyle="->"))
plt.annotate('Amidation', xy=(-0.984016, 30), xytext=(-0.984016+0.03, 50), arrowprops=dict(arrowstyle="->"))

ok = plt.subplot(222)


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

plt.annotate('Xle->D', xy=(1.942879, 15), xytext=(1.942879-0.05, 25), arrowprops=dict(arrowstyle="->"))
#plt.annotate('Thr->Cys', xy=(1.961506, 18), xytext=(1.961506-0.07, 35), arrowprops=dict(arrowstyle="->"))
plt.annotate('Double\nDeamidation', xy=(1.968032, 40), xytext=(1.968032-0.077, 45), arrowprops=dict(arrowstyle="->"))
plt.annotate('Val->Thr', xy=(1.979265, 29), xytext=(1.979265-0.01, 55), arrowprops=dict(arrowstyle="->"))
#plt.annotate('1Mm\nand\nDeamidation', xy=(1.0029+0.984016, 25), xytext=(1.997-0.07, 45), arrowprops=dict(arrowstyle="->"))
#plt.annotate('Glu->Met', xy=(1.997892, 22), xytext=(1.997+0.04, 35), arrowprops=dict(arrowstyle="->"))
plt.annotate('2 Mm', xy=(2.0052, 20), xytext=(2.02, 25), arrowprops=dict(arrowstyle="->"))
#plt.annotate('Pro->Val', xy=(2.015650, 13), xytext=(2.015650+0.012, 17), arrowprops=dict(arrowstyle="->"))

plt.tight_layout()


plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig4jurkat-1012.png', format='png', dpi=600)


plt.show()
