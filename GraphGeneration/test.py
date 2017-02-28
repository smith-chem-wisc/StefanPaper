import numpy as np
import matplotlib.pyplot as plt

fileName = r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-13-26-00\02-14-17_Cl-1_rep1beforesc1.ms1dptsv"

nice = np.loadtxt(fileName, skiprows=1, unpack = True)

print(sum(nice[-1])/len(nice[-1]))

plt.figure(1)
plt.subplot(231)
plt.plot(nice[0],nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(nice[0]), max(nice[0]), zorder = 10)
plt.xlabel("mz")
plt.subplot(232)
plt.plot(nice[1],nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(nice[1]), max(nice[1]), zorder = 10)
plt.xlabel("rt")
plt.subplot(233)
plt.plot(np.log(nice[2]),nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice[2])), max(np.log(nice[2])), zorder = 10)
plt.xlabel("log(intensity)")
plt.subplot(234)
plt.plot(np.log(nice[3]),nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice[3])), max(np.log(nice[3])), zorder = 10)
plt.xlabel("log(TIC)")
plt.subplot(235)
plt.plot(np.log(nice[4]),nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice[4])), max(np.log(nice[4])), zorder = 10)
plt.xlabel("log(injection time)")

if len(nice)==7:
    plt.subplot(236)
    plt.plot(nice[5],nice[-1], 'bo',markersize = .3)
    plt.hlines(0, min(nice[5]), max(nice[5]), zorder = 10)
    plt.xlabel("isolation mz")


plt.figure(2)

fileName = r"C:\Users\stepa\Desktop\02-15-17_Cys-tag_light\2017-02-25-13-26-00\02-14-17_Cl-1_rep1afterfc2after.ms1dptsv"

nice = np.loadtxt(fileName, skiprows=1, unpack = True)

print(sum(nice[-1])/len(nice[-1]))

plt.subplot(231)
plt.plot(nice[0],nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(nice[0]), max(nice[0]), zorder = 10)
plt.xlabel("mz")
plt.subplot(232)
plt.plot(nice[1],nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(nice[1]), max(nice[1]), zorder = 10)
plt.xlabel("rt")
plt.subplot(233)
plt.plot(np.log(nice[2]),nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice[2])), max(np.log(nice[2])), zorder = 10)
plt.xlabel("log(intensity)")
plt.subplot(234)
plt.plot(np.log(nice[3]),nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice[3])), max(np.log(nice[3])), zorder = 10)
plt.xlabel("log(TIC)")
plt.subplot(235)
plt.plot(np.log(nice[4]),nice[-1], 'bo',markersize = .3)
plt.hlines(0, min(np.log(nice[4])), max(np.log(nice[4])), zorder = 10)
plt.xlabel("log(injection time)")

if len(nice)==7:
    plt.subplot(236)
    plt.plot(nice[5],nice[-1], 'bo',markersize = .3)
    plt.hlines(0, min(nice[5]), max(nice[5]), zorder = 10)
    plt.xlabel("isolation mz")

plt.show()
