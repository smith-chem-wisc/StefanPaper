import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas

maxi = 30000

matplotlib.rcParams.update({'font.size': 24})

height = 5
width = 14 

f, ((ax1, ax2)) = plt.subplots(1, 2, sharex='col', sharey='row', figsize=(width,height))
ax1.set_title('Uncalibrated')
ax2.set_title('Calibrated')

ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-05-18-28-01\Task1Search\allPSMs_10ppmAroundZero.psmtsv", sep='\t')  
A=ok[r"Mass Diff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue Notch"]

ax1.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax1.set_ylim([1,maxi])
ax1.vlines(0,0,maxi,zorder = 10)
ax1.set_ylabel('PSM count')
ax1.set_xlabel('Error (PPM)')

mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.2f,%.2f]\n95.4%%: [%.2f,%.2f]\n99.7%%: [%.2f,%.2f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
print(textToDisplay)


ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-05-05-18-28-01\Task3Search\allPSMs_10ppmAroundZero.psmtsv", sep='\t')  

A=ok[r"Mass Diff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue Notch"]

ax2.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax2.set_ylim([1,maxi])
ax2.vlines(0,0,maxi,zorder = 10)
ax2.set_xlabel('Error (PPM)')


mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.2f,%.2f]\n95.4%%: [%.2f,%.2f]\n99.7%%: [%.2f,%.2f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
print(textToDisplay)

plt.tight_layout()

plt.savefig('figCalibrationPoster.eps', format='eps', dpi=1200)
plt.savefig('figCalibrationPoster.png', format='png', dpi=1200)

plt.show()
