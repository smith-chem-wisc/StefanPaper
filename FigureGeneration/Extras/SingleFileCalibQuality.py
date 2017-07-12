import numpy as np
import matplotlib.pyplot as plt
import pandas

maxi = 3000


start = r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-07-10-17-50-26\Task1Calibrate\04-30-13_CAST_Frac5_4uL"

plt.figure(num=1,figsize=(10.9,6))

plt.suptitle(start.split('\\')[-1], fontsize=14)

plt.figure(1)


ok = pandas.read_csv(start+"PSMsBeforeLinearCalib.psmtsv", sep='\t')  
#A=ok[r"Mass Diff (ppm)"]
A=ok[r"Improvement Possible"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue"]


ok = plt.subplot(131)
plt.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi*.65,zorder = 10)

plt.title("Uncalibrated")


ok = pandas.read_csv(start+"PSMsBeforeNonLinearCalib.psmtsv", sep='\t')  

#A=ok[r"Mass Diff (ppm)"]
A=ok[r"Improvement Possible"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue"]





ok = plt.subplot(132)
plt.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi*.65,zorder = 10)


plt.title("Linear Calibration")

ok = pandas.read_csv(start+"PSMsAfterCalib.psmtsv", sep='\t')  

#A=ok[r"Mass Diff (ppm)"]
A=ok[r"Improvement Possible"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue"]



ok = plt.subplot(133)
plt.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi*.65,zorder = 10)


plt.title("Nice Calibration")

plt.savefig('myimage.png', format='png', dpi=1200)

plt.show()
