import numpy as np
import matplotlib.pyplot as plt
import pandas

maxi = 6000 

#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-02-25-13-59-40\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t')
#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-02-25-13-59-40\Task3Search\aggregate20ppmAroundZero.psmtsv", sep='\t')

#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-02-25-13-57-45\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t')
#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-02-25-13-57-45\Task3Search\aggregate20ppmAroundZero.psmtsv", sep='\t')

#ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-14-00-36\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t') #Br
#ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-14-00-36\Task3Search\aggregate20ppmAroundZero.psmtsv", sep='\t') #Br

#ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-14-01-16\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t') #Cl
#ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-27-09-26-26\Task2Search\aggregate20ppmAroundZero.psmtsv", sep='\t')  #Cl



#start = r"C:\Users\stepa\Desktop\QE-HF_mass_cali_tests\2017-03-09-16-07-50\Task1Calibrate\c\03-07-17_YL_3e6_30K10ppmAroundZero"
#start = r"C:\Users\stepa\Desktop\QE-HF_mass_cali_tests\2017-03-09-16-07-50\Task1Calibrate\d\03-07-17_YL_3e6_60K10ppmAroundZero"
#start = r"C:\Users\stepa\Desktop\QE-HF_mass_cali_tests\2017-03-09-16-07-50\Task1Calibrate\e\03-07-17_YL_5e6_30K10ppmAroundZero"
#start = r"C:\Users\stepa\Desktop\QE-HF_mass_cali_tests\2017-03-09-16-07-50\Task1Calibrate\f\03-07-17_YL_5e6_60K10ppmAroundZero"
#start = r"C:\Users\stepa\Desktop\QE-HF_mass_cali_tests\2017-03-09-16-07-50\Task1Calibrate\a\03-07-17_YL_1e6_30K10ppmAroundZero"
#start = r"C:\Users\stepa\Desktop\QE-HF_mass_cali_tests\2017-03-09-16-07-50\Task1Calibrate\b\03-07-17_YL_1e6_60K10ppmAroundZero"
#start = r"C:\Users\stepa\Desktop\03-12-17_for-Stefan_120K_240K_cali-tests\2017-03-13-14-13-44\Task1Calibrate\03-12-17_YL_1e6_120K10ppmAroundZero"
#start = r"C:\Users\stepa\Desktop\03-12-17_for-Stefan_120K_240K_cali-tests\2017-03-13-14-13-44\Task1Calibrate\03-12-17_YL_1e6_240K10ppmAroundZero"

start = r"C:\Users\stepa\Data\CalibrationPaperData\Yeast\2017-03-13-14-25-38\Task1Calibrate\12-10-16_A17A_yeast_BU_fract8_rep1_8uL10ppmAroundZero"


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
