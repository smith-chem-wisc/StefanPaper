import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)

ylabels = ['Reject', 'Accept']
yTicks = [1,2]

plt.subplot(411)
plt.plot([0],[2], 'go')
plt.hlines(1,-100,-2, colors = 'r')
plt.hlines(1,2,100, colors = 'r')
plt.ylim([0,3])
plt.yticks(yTicks, ylabels)
plt.title("Narrow-Mass Search")

plt.subplot(412)
plt.plot([0],[2], 'go')
plt.plot([16],[2], 'go')
plt.plot([-17],[2], 'go')
plt.plot([42],[2], 'go')
plt.hlines(1,-100,-19, colors = 'r')
plt.hlines(1,-15,-2, colors = 'r')
plt.hlines(1,2,14, colors = 'r')
plt.hlines(1,18,40, colors = 'r')
plt.hlines(1,44,100, colors = 'r')
plt.ylim([0,3])
plt.yticks(yTicks, ylabels)
plt.title("Notch Search")

plt.subplot(413)
plt.hlines(1,-100,-57, colors = 'r')
plt.plot([-16],[1], 'ro')
plt.plot([57],[1], 'ro')
plt.hlines(2,-57,-18, colors = 'g')
plt.hlines(2,-14,55, colors = 'g')
plt.hlines(2,59,100, colors = 'g')
plt.ylim([0,3])
plt.yticks(yTicks, ylabels)
plt.title("Interval Search")

plt.subplot(414)
plt.hlines(2,-100,100, colors = 'g')
plt.ylim([0,3])
plt.yticks(yTicks, ylabels)
plt.title("Wide-Mass Search")

plt.tight_layout()

plt.show()