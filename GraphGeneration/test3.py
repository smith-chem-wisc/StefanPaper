import numpy as np
import matplotlib.pyplot as plt
import pandas
maxi = 15000

#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-02-25-13-59-40\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t')
#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-02-25-13-59-40\Task3Search\aggregate20ppmAroundZero.psmtsv", sep='\t')

#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-02-25-13-57-45\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t')
#ok = pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Jurkat\2017-02-25-13-57-45\Task3Search\aggregate20ppmAroundZero.psmtsv", sep='\t')

#ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-14-00-36\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t') #Br
#ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-14-00-36\Task3Search\aggregate20ppmAroundZero.psmtsv", sep='\t') #Br

#ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-14-01-16\Task1Search\aggregate20ppmAroundZero.psmtsv", sep='\t') #Cl
ok = pandas.read_csv(r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-27-09-26-26\Task2Search\aggregate20ppmAroundZero.psmtsv", sep='\t')  #Cl


A=ok[r"MassDiff (ppm)"]
B=ok[r"Decoy/Contaminant/Target"]=="T"
C=ok[r"QValue_notch"]

plt.figure(1)

ok = plt.subplot(131)
plt.hist(A[C<0.01], bins  = 101, range=[-20.2,20.2])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi,zorder = 10)
plt.title("All")
#ok.set_yscale("log", nonposy='clip')

ok = plt.subplot(132)
plt.hist(A[(C<0.01) & B], bins  = 101, range=[-20.2,20.2])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi,zorder = 10)
plt.title("Target")
#ok.set_yscale("log", nonposy='clip')


ok = plt.subplot(133)
plt.hist(A[(C<0.01) & ~B], bins  = 101, range=[-20.2,20.2])
plt.ylim([1,maxi])
plt.vlines(0,0,maxi,zorder = 10)
plt.title("Decoy")
#ok.set_yscale("log", nonposy='clip')

plt.show()
