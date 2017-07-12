import numpy as np
import matplotlib.pyplot as plt
import pandas

nice= pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-07-10-17-50-26\Task1Calibrate\04-30-13_CAST_Frac5_4uLinLinearbeforesc1.ms1dptsv", sep='\t')
nice2= pandas.read_csv(r"C:\Users\stepa\Data\CalibrationPaperData\Mouse\2017-07-10-17-50-26\Task1Calibrate\04-30-13_CAST_Frac5_4uLinNonLinearafterfc4.ms1dptsv", sep='\t')


height = 6
width = 7

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(width,height))

ax1.plot(nice['mz'],nice['Label'], 'bo',markersize = .3)
ax1.hlines(0, min(nice['mz']), max(nice['mz']), zorder = 10)

ax1.set_ylabel('m/z error')
ax1.annotate(r"Uncalibrated", xy=(0, 0.5), xycoords=ax1.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))

ax2.plot(nice['rt'],nice['Label'], 'bo',markersize = .3)
ax2.hlines(0, min(nice['rt']), max(nice['rt']), zorder = 10)

ax3.plot(nice2['mz'],nice2['Label'], 'bo',markersize = .3)
ax3.hlines(0, min(nice2['mz']), max(nice2['mz']), zorder = 10)

ax3.set_ylabel('m/z error')
ax3.set_xlabel('m/z')

ax3.annotate(r"Calibrated", xy=(0, 0.5), xycoords=ax3.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center', xytext=(0,0.5))

ax4.plot(nice2['rt'],nice2['Label'], 'bo',markersize = .3)
ax4.hlines(0, min(nice2['rt']), max(nice2['rt']), zorder = 10)
ax4.set_xlabel('rt')

plt.tight_layout()

plt.subplots_adjust(left=0.3)

plt.savefig(r'C:\Users\stepa\Source\StefanPaper\fig1-calibErrors.png', format='png', dpi=600)

plt.show()
