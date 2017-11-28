import numpy as np
import matplotlib.pyplot as plt
import pandas

maxi = 35000 


height = 6
width =  7 

f, ((ax1), (ax3)) = plt.subplots(2, 1, sharex='col', sharey='row', figsize=(width,height))

ok = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\1mm10ppmSearch\Task1-SearchTask\aggregatePSMs_1mm.psmtsv", sep='\t')  

ok['Mass Diff (ppm)'] = pandas.to_numeric(ok['Mass Diff (ppm)'], errors='coerce')

A=ok[r"Mass Diff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue Notch"]
D=ok[r"Notch"]

print("count")
print(len(A[(C<0.01) & B]))
print("mean")
print(np.mean(A[(C<0.01) & B & (D==r'0')]))
print("st dev")
print(np.std(A[(C<0.01) & B & (D==r'0')]))

ax1.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax1.set_ylim([1,maxi])
ax1.vlines(0,0,maxi,zorder = 10)
ax1.set_ylabel('PSM count')
ax1.annotate(r"Uncalibrated", xy=(0, 0.5), xycoords=ax1.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))




ok = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\Calibrated\1mm10ppm\Task1-SearchTask\aggregatePSMs_1mm.psmtsv", sep='\t')  

ok['Mass Diff (ppm)'] = pandas.to_numeric(ok['Mass Diff (ppm)'], errors='coerce')

A=ok[r"Mass Diff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue Notch"]
D=ok[r"Notch"]

print("count")
print(len(A[(C<0.01) & B]))
print("mean")
print(np.mean(A[(C<0.01) & B & (D==r'0')]))
print("st dev")
print(np.std(A[(C<0.01) & B & (D==r'0')]))

ax3.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax3.set_ylim([1,maxi])
ax3.vlines(0,0,maxi,zorder = 10)
ax3.set_ylabel('PSM count')
ax3.set_xlabel('Mass Error (ppm)')

ax3.annotate(r"Calibrated", xy=(0, 0.5), xycoords=ax3.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))


plt.tight_layout()

plt.subplots_adjust(left=0.3)


plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig2-10ppmSearchCalib.png', format='png', dpi=600)

plt.show()
