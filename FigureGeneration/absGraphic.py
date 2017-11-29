import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from PIL import Image
from io import BytesIO


height = 1.75 
width = 3.25 
fig = plt.figure(figsize=(width, height))

#######

ax = fig.add_subplot(111)
for p in [
    patches.Rectangle(
        (-110, 0), 106, 1,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (-4, 0), 8, 1,
    ),
    patches.Rectangle(
        (4, 0), 34, 1,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (38, 0), 8, 1,
    ),
    patches.Rectangle(
        (46, 0), 30, 1,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (76, 0), 8, 1,
    ),
    patches.Rectangle(
        (84, 0), 26, 1,
        alpha=0.4,
        facecolor="red"
    )
]:
    ax.add_patch(p)


ax.set_xlim([-110,110])
ax.set_ylim([-2, 9])

plt.annotate('Multiple specific mass\ndifferences allowed', xy=(0,1), xytext=(-103,4), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(42, 1), xytext=(10, 3.3), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(80, 1), xytext=(20, 3.3), arrowprops=dict(arrowstyle="->"))

plt.title('Multi-Notch Search')

ax.get_yaxis().set_visible(False)

################

fig.text(0.45, 0.05, 'Mass difference (Da)', ha='center')

#######

blue_patch = patches.Patch(label='Allowed')
red_patch = patches.Patch(color='red', label='Not\nAllowed', alpha=0.4)


plt.tight_layout()

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
