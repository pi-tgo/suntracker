#!/usr/bin/python

import sys
import pandas as pd
import matplotlib.pyplot as plt
# matplotlib.use('Agg')       # use the 'Agg' backend when $DISPLAY environment is not defined
plt.rcParams["figure.figsize"] = (12, 8)

filename = sys.argv[1]
data = pd.read_csv(filename)
#origindata = pd.read_csv(filename, skiprows=1)
#data = origindata.drop(origindata.index[[0,1]])

current_date = data['TIMESTAMP'][1][0:10]
data.TIMESTAMP = pd.to_datetime(data.TIMESTAMP)

data = data.set_index('TIMESTAMP')

ax = plt.gca()

ax.set_title('Solar Radiation ' + current_date)
ax.set_ylabel('Irradiance (W/m2)')
ax.grid(True, which='both')

data['Global_Horizontal_Irradiance_Avg'].astype(float).plot(kind='line',linewidth=0.5, label='Global Horizontal', ax=ax);
data['Global_Normal_Irradiance_Avg'].astype(float).plot(kind='line',linewidth=0.5, color='blue', label='Global Normal', ax=ax);
data['Direct_Normal_Irradiance_Avg'].astype(float).plot(kind='line',linewidth=0.5, color='red', label='Direct Normal', ax=ax);

leg = ax.legend()

for tick in ax.get_xticklabels():
    tick.set_rotation(25)

#savefilename = sys.argv[2]
#plt.savefig(savefilename)

plt.show()
