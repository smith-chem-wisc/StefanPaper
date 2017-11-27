import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


height = 2
width = 7 
fig = plt.figure(figsize=(width, height))

#######


ax = fig.add_subplot(131)
for p in [
    patches.Rectangle(
        (-105, 0), 101, 1,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (-4, 0), 8, 1,
    ),
    patches.Rectangle(
        (4, 0), 101, 1,
        alpha=0.4,
        facecolor="red"
    )
]:
    ax.add_patch(p)


ax.set_xlim([-105,105])
ax.set_ylim([-2, 9])

ax.set_xlabel('Mass Diff (Da)')

ax.set_xlabel('Mass Diff (Da)')


plt.annotate('Only mass differences\nclose to zero allowed', xy=(0,1), xytext=(-80,4), arrowprops=dict(arrowstyle="->"))
plt.title('Narrow-Window Search')


ax.get_yaxis().set_visible(False)

#######

ax = fig.add_subplot(132)
for p in [
    patches.Rectangle(
        (-105, 0), 5, 1,
        alpha=0.4,
        facecolor="red"
    ),
    patches.Rectangle(
        (-100, 0), 200, 1,
    ),
    patches.Rectangle(
        (100, 0), 5, 1,
        alpha=0.4,
        facecolor="red"
    )
]:
    ax.add_patch(p)


ax.set_xlim([-105,105])
ax.set_ylim([-2, 9])

ax.set_xlabel('Mass Diff (Da)')

ax.set_xlabel('Mass Diff (Da)')

plt.annotate('Wide range of mass\ndifferences allowed', xy=(0,1), xytext=(-80,4), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(-50, 1), xytext=(-10, 3.3), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(50, 1), xytext=(10, 3.3), arrowprops=dict(arrowstyle="->"))
plt.title('Open Search')

ax.get_yaxis().set_visible(False)

#######

ax = fig.add_subplot(133)
for p in [
    patches.Rectangle(
        (-105, 0), 101, 1,
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
        (84, 0), 21, 1,
        alpha=0.4,
        facecolor="red"
    )
]:
    ax.add_patch(p)


ax.set_xlim([-105,105])
ax.set_ylim([-2, 9])

ax.set_xlabel('Mass Diff (Da)')

plt.annotate('Only specific mass\ndifferences allowed', xy=(0,1), xytext=(-80,4), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(42, 1), xytext=(10, 3.3), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(80, 1), xytext=(20, 3.3), arrowprops=dict(arrowstyle="->"))

plt.title('Multi-Notch Search')

ax.get_yaxis().set_visible(False)

#######

plt.tight_layout()

plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig3-searchTypes.png', format='png', dpi=600)

plt.show()
