import numpy as np
import matplotlib.pyplot as plt



height = 2
width = 7 
plt.figure(figsize=(width, height))

plt.subplot(131)

dates = [-100,-1,0,1,100]
values = [1,1,2,1,1]

plt.plot(dates, values, '-')

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.ylim([0.5,2.5])
plt.yticks(yTicks, ylabels)
plt.xlabel("Mass Diff (Da)")
plt.title("Narrow-Window Search")

plt.subplot(133)

dates =  [-100,-18,-17,-16,-1,0,1,41,42,43,79,80,81,100]
values = [1   ,  1,  2,  1 ,1,2,1, 1, 2, 1,1 ,2 ,1 , 1]

plt.plot(dates, values, '-')

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.title("Multi-Notch Search")
plt.ylim([0.5,2.5])

plt.yticks(yTicks, ylabels)
plt.xlabel("Mass Diff (Da)")

plt.subplot(132)



dates =  [-100,100]
values = [2 ,2]

plt.plot(dates, values, '-')

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.ylim([0.5,2.5])

plt.title("Open Search")

plt.yticks(yTicks, ylabels)
plt.xlabel("Mass Diff (Da)")




plt.tight_layout()


plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig3-searchTypes.png', format='png', dpi=600)


plt.show()
