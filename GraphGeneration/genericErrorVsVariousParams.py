import numpy as np
import matplotlib.pyplot as plt

fileName = r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\04-30-13_CAST_Frac9_9p5uLbeforesc1.ms1dptsv"
#fileName = r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\04-30-13_CAST_Frac9_9p5uLbeforesc2.ms1dptsv"
#fileName = r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\04-30-13_CAST_Frac9_9p5uLbeforesc4.ms1dptsv"
#fileName = r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-04-07-18-09-31\Task1Calibrate\04-30-13_CAST_Frac9_9p5uLafterfc2after.ms1dptsv"


nice = np.loadtxt(fileName, skiprows=1, unpack = True)

print("average error", sum(nice[-1])/len(nice[-1]))

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

plt.show()
