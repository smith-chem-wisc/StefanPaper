import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from scipy.interpolate import spline
from scipy.interpolate import interp1d
from scipy.interpolate import splrep, splev

from PIL import Image
from io import BytesIO


height = 1.75 
width = 3.25 
#height = 1.75*3 
#width = 3.25*3
fig = plt.figure(figsize=(width, height))

#######

ax = fig.add_subplot(311)
x = np.array([-1,-0.5,0,0.5,1,1.5,15.5,16,16.5,20])
y = np.array([1,1,100,1,20,1,1,20,1,1])
f = interp1d(x, y)
xnew = np.linspace(-1, 20, num=211, endpoint=True)
plt.plot(xnew, f(xnew), '-')

ax.axis('off')
ax.set_xlim([-1,20])

plt.annotate('Uncalibrated\nMass Differences', xytext=(5, 27), xy=(0,0), fontsize=8)
#plt.annotate('Pro->Val', xy=(2.015650, 13), xytext=(2.015650+0.012, 27), arrowprops=dict(arrowstyle="->"))

#######

ax = fig.add_subplot(312)
x = np.array([-1,-0.1,0,0.1,0.9,1,1.1,15.9,16,16.1,20])
y = np.array([1,1,100,1,1,20,1,1,20,1,1])
f = interp1d(x, y)
xnew = np.linspace(-1, 20, num=211, endpoint=True)
plt.plot(xnew, f(xnew), '-')

ax.axis('off')
ax.set_xlim([-1,20])

plt.annotate('Calibrated\nMass Differences', xytext=(5, 27), xy=(0,0), fontsize=8)


#######

ax = fig.add_subplot(313)
for p in [
    patches.Rectangle(
        (-1, 0), 0.8, 5,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (-0.2, 0), 0.4, 5,
    ),
    patches.Rectangle(
        (0.2, 0), 0.6, 5,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (0.8, 0), 0.4, 5,
    ),
    patches.Rectangle(
        (1.2, 0), 14.6, 5,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (15.8, 0), 0.4, 5,
    ),
    patches.Rectangle(
        (16.2, 0), 3.8, 5,
        alpha=0.4,
        facecolor="red"
    )
]:
    ax.add_patch(p)


ax.set_xlim([-1,20])
ax.set_ylim([-15, 12])

#ax.axis('off')

ax.annotate('Multi-Notch Sofware Filtering', xytext=(1.7, -6.6), xy=(0,0), fontsize=8)


#plt.tight_layout()

################


ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)

ax.set_xticks([0,1,16])
ax.set_xticklabels(['0', '1', '79.966'])


plt.tick_params(axis='both', which='major', labelsize=8)
plt.tick_params(axis='both', which='minor', labelsize=8)

ax.arrow(6,20,0,-10, head_width=1, head_length=5, facecolor="red")
ax.arrow(10,20,0,-10, head_width=1, head_length=5, facecolor="red")
ax.arrow(18,20,0,-10, head_width=1, head_length=5, facecolor="red")

ax.arrow(0,20,0,-10, head_width=1, head_length=5)
ax.arrow(1,20,0,-10, head_width=1, head_length=5)
ax.arrow(16,20,0,-10, head_width=1, head_length=5)

ax.arrow(0,0,0,-8, head_width=1, head_length=5)
ax.arrow(1,0,0,-8, head_width=1, head_length=5)
ax.arrow(16,0,0,-8, head_width=1, head_length=5)


ax.annotate('Accepted Mass Diffs (Da)', xytext=(2.4, -27), xy=(0,0), fontsize=8)

plt.subplots_adjust(bottom=0.15)

#fig.text(0.45, 0.05, 'Mass difference (Da)', ha='center')

#######

# save figure
# (1) save the image in memory in PNG format

png1 = BytesIO()
plt.savefig(png1, format='png', dpi=300)

# (2) load this image into PIL
png2 = Image.open(png1)
print(png2.info['dpi'])

# (3) save as TIFF
png2.save(r'C:\Users\stepa\Source\StefanPaper\absGraphic.tiff',dpi=[300,300])

png1.close()

plt.show()
