import numpy as np
import matplotlib.pyplot as plt
import pandas

nice = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\2017-10-12-17-10-32\Task1-CalibratingAllJurkat\120426_Jurkat_highLC_Frac16init.ms1dptsv", sep='\t')
nice2 = pandas.read_csv(r"C:\Users\stepa\Data\PaperData\JurkatTrypsin\2017-10-12-17-10-32\Task1-CalibratingAllJurkat\120426_Jurkat_highLC_Frac16round7inter-scan.ms1dptsv", sep='\t')

height = 6
width = 7

minY=-0.02
maxY=0.02

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(width,height))

ax1.plot(nice['mz'],nice['LabelTh'], 'bo',markersize = .3)
ax1.hlines(0, min(nice['mz']), max(nice['mz']), zorder = 10)
ax1.set_ylim([minY,maxY])

ax1.set_ylabel('m/z error')
ax1.annotate(r"Uncalibrated", xy=(0, 0.5), xycoords=ax1.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))

ax2.plot(nice['rt'],nice['LabelTh'], 'bo',markersize = .3)
ax2.hlines(0, min(nice['rt']), max(nice['rt']), zorder = 10)
ax2.set_ylim([minY,maxY])

ax3.plot(nice2['mz'],nice2['LabelTh'], 'bo',markersize = .3)
ax3.hlines(0, min(nice2['mz']), max(nice2['mz']), zorder = 10)

ax3.set_ylabel('m/z error')
ax3.set_xlabel('m/z')

ax3.annotate(r"Calibrated", xy=(0, 0.5), xycoords=ax3.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))
ax3.set_ylim([minY,maxY])

ax4.plot(nice2['rt'],nice2['LabelTh'], 'bo',markersize = .3)
ax4.hlines(0, min(nice2['rt']), max(nice2['rt']), zorder = 10)
ax4.set_xlabel('rt')

ax4.set_ylim([minY,maxY])

plt.tight_layout()

plt.subplots_adjust(left=0.3)

plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig1-calibErrors.png', format='png', dpi=600)

plt.show()
