import numpy as np
import matplotlib.pyplot as plt



height = 5
width = 3.25 
plt.figure(figsize=(width, height))

plt.subplot(311)

dates = [-100,-1,0,1,100]
values = [1,1,2,1,1]

plt.plot(dates, values, '-')

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.ylim([0.5,2.5])
plt.yticks(yTicks, ylabels)
plt.title("Narrow-Window Search")

plt.subplot(312)

dates =  [-100,-18,-17,-16,-1,0,1,41,42,43,79,80,81,100]
values = [1   ,  1,  2,  1 ,1,2,1, 1, 2, 1,1 ,2 ,1 , 1]

plt.plot(dates, values, '-')

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.title("Multi-Notch Search")
plt.ylim([0.5,2.5])

plt.yticks(yTicks, ylabels)

plt.subplot(313)



dates =  [-100,100]
values = [2 ,2]

plt.plot(dates, values, '-')

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.ylim([0.5,2.5])

plt.title("Open Search")

plt.yticks(yTicks, ylabels)
plt.tight_layout()


plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig3-searchTypes.png', format='png', dpi=600)


plt.show()
