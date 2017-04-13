import numpy as np
import matplotlib.pyplot as plt
import pandas

maxi = 3000


#start =  r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-04-10-15-00-59\Task1Calibrate\120426_Jurkat_highLC_Frac19_allPSMs_10ppmAroundZero"
start =  r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-04-10-15-00-59\Task1Calibrate\120426_Jurkat_highLC_Frac14_allPSMs_10ppmAroundZero"

#start =  r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\04-30-13_CAST_Frac3_6uL_allPSMs_10ppmAroundZero"
#start =  r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\04-30-13_CAST_Frac9_9p5uL_allPSMs_10ppmAroundZero"
#start =  r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\04-29-13_B6_Frac9_9p5uL_allPSMs_10ppmAroundZero"


plt.figure(num=1,figsize=(10.9,6))

plt.suptitle(start.split('\\')[-1], fontsize=14)

plt.figure(1)


ok = pandas.read_csv(start+".psmtsv", sep='\t')  
A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]


ok = plt.subplot(131)
plt.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi*.65,zorder = 10)

mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.3f,%.3f]\n95.4%%: [%.3f,%.3f]\n99.7%%: [%.3f,%.3f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.9)
plt.text(-10,maxi*0.69, textToDisplay,fontsize=14 ,bbox=props)
plt.title("Uncalibrated")


ok = pandas.read_csv(start+"test.psmtsv", sep='\t')  


A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]




ok = plt.subplot(132)
plt.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi*.65,zorder = 10)

mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.3f,%.3f]\n95.4%%: [%.3f,%.3f]\n99.7%%: [%.3f,%.3f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.9)
plt.text(-10,maxi*0.69, textToDisplay,fontsize=14 ,bbox=props)


plt.title("Linear Calibration")

ok = pandas.read_csv(start+"test2.psmtsv", sep='\t')  

A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]



ok = plt.subplot(133)
plt.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi*.65,zorder = 10)

mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.3f,%.3f]\n95.4%%: [%.3f,%.3f]\n99.7%%: [%.3f,%.3f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.9)
plt.text(-10,maxi*0.69, textToDisplay,fontsize=14 ,bbox=props)


plt.title("Nice Calibration")

plt.savefig('myimage.png', format='png', dpi=1200)

plt.show()
