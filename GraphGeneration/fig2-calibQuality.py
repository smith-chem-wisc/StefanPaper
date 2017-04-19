import numpy as np
import matplotlib.pyplot as plt
import pandas

maxi = 25000


height = 6
width = 7

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(width,height))
ax1.set_title('Uncalibrated')
ax2.set_title('Calibrated')

ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-12-15-20-37\Task1Search\allPSMs_10ppmAroundZero.psmtsv", sep='\t')  
A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]

ax1.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax1.set_ylim([1,maxi])
ax1.vlines(0,0,maxi,zorder = 10)
ax1.set_ylabel('PSM count')
ax1.annotate(r"Mouse", xy=(0, 0.5), xycoords=ax1.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))

mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.2f,%.2f]\n95.4%%: [%.2f,%.2f]\n99.7%%: [%.2f,%.2f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
print(textToDisplay)


ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\2017-04-12-15-21-10\Task1Search\allPSMs_10ppmAroundZero.psmtsv", sep='\t')  

A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]

ax2.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax2.set_ylim([1,maxi])
ax2.vlines(0,0,maxi,zorder = 10)


mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.2f,%.2f]\n95.4%%: [%.2f,%.2f]\n99.7%%: [%.2f,%.2f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
print(textToDisplay)




maxi = 35000

ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-04-12-15-22-08\Task1Search\allPSMs_10ppmAroundZero.psmtsv", sep='\t')  
A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]

ax3.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax3.set_ylim([1,maxi])
ax3.vlines(0,0,maxi,zorder = 10)
ax3.set_ylabel('PSM count')
ax3.set_xlabel('Mass Error (ppm)')

ax3.annotate(r"Jurkat", xy=(0, 0.5), xycoords=ax3.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))


mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.2f,%.2f]\n95.4%%: [%.2f,%.2f]\n99.7%%: [%.2f,%.2f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
print(textToDisplay)

ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-04-10-15-00-59\Task1Calibrate\2017-04-12-15-22-31\Task1Search\allPSMs_10ppmAroundZero.psmtsv", sep='\t')  

A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]

ax4.hist(A[(C<0.01) & B], bins  = 101, range=[-10.1,10.1])
ax4.set_ylim([1,maxi])
ax4.vlines(0,0,maxi,zorder = 10)
ax4.set_xlabel('Mass Error (ppm)')

mu = np.mean(A[(C<0.01) & B])
sigma = np.std(A[(C<0.01) & B])
textToDisplay = 'count = %d\n$\mu=%.2f$\n$\sigma=%.2f$\n68.3%%: [%.2f,%.2f]\n95.4%%: [%.2f,%.2f]\n99.7%%: [%.2f,%.2f]'%(len(A[(C<0.01) & B]), mu, sigma,mu-sigma, mu+sigma,mu-2*sigma, mu+2*sigma,mu-3*sigma, mu+3*sigma)
print(textToDisplay)

plt.tight_layout()

plt.subplots_adjust(left=0.2)

plt.savefig('fig2-calibrationQuality.eps', format='eps', dpi=1200)
plt.savefig('fig2-calibrationQuality.png', format='png', dpi=1200)

plt.show()
