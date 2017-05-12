import numpy as np
import matplotlib
import matplotlib.pyplot as plt


matplotlib.rcParams.update({'font.size': 24})


height = 10 
width = 7 
plt.figure(figsize=(width, height))

plt.subplot(411)

dates = [-100,-1,0,1,100]
values = [1,1,2,1,1]

plt.plot(dates, values, '-', linewidth=5)

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.ylim([0.5,2.5])
plt.yticks(yTicks, ylabels)
plt.title("Narrow-Mass Search")

plt.subplot(412)

dates =  [-100,-18,-17,-16,-1,0,1,41,42,43,79,80,81,100]
values = [1   ,  1,  2,  1 ,1,2,1, 1, 2, 1,1 ,2 ,1 , 1]

plt.plot(dates, values, '-', linewidth=5)

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.title("Notch Search")
plt.ylim([0.5,2.5])

plt.yticks(yTicks, ylabels)
plt.subplot(413)




dates =  [-100,-87,-86,-15,-14,-13,56,57,58,100]
values = [1   ,  1, 2, 2,  1,  2, 2,1 ,2 ,2]
plt.plot(dates, values, '-', linewidth=5)

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.ylim([0.5,2.5])

plt.title("Interval Search")
plt.yticks(yTicks, ylabels)
hehe =plt.subplot(414)



dates =  [-100,100]
values = [2 ,2]

plt.plot(dates, values, '-', linewidth=5)


ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.ylim([0.5,2.5])

hehe.set_xlabel('Mass Diff (Da)')

plt.title("Wide-Mass Search")

plt.yticks(yTicks, ylabels)
plt.tight_layout()


plt.savefig('figAposter.eps', format='eps', dpi=1200)
plt.savefig('figAposter.png', format='png', dpi=1200)


plt.show()
