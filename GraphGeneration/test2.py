import numpy as np
import matplotlib.pyplot as plt

fileName = r"C:\Users\stepa\Source\CalibrationPaper\GraphGeneration\ppm.txt"

nice = np.genfromtxt(fileName, delimiter='\t', unpack = True)
plt.figure(1)

plt.subplot(131)
A = nice[0]
plt.hist(A[~np.isnan(A)], bins  = 100, range=[-10,10])
plt.ylim([0,2000])
plt.title("prior")

plt.subplot(132)
A = nice[1]
plt.hist(A[~np.isnan(A)], bins  = 100, range=[-10,10])
plt.ylim([0,2000])
plt.title("after smooth")

plt.subplot(133)
A = nice[2]
plt.hist(A[~np.isnan(A)], bins  = 100, range=[-10,10])
plt.ylim([0,2000])
plt.title("after rf")

plt.show()
