# !/usr/bin/env python

import sys, re, os, random
import pandas as pd
import matplotlib.pyplot as plt
# matplotlib.use('Agg')       # use the 'Agg' backend when $DISPLAY environment is not defined
plt.rcParams["figure.figsize"] = (12, 8)

filename = ''.join(random.choice('01234567890abcdef') for i in range(16)) + '.csv'

# infile = open('header.csv', 'r')
infile = open('latest.csv', 'r')
# infile = open(sys.argv[1], 'r')
outfile = open(filename, 'a')

for line in infile:
    line = re.sub(line[:line.find("\"")], '', line)
    outfile.write(line)

infile.close()
outfile.close()

data = pd.read_csv(filename)
os.remove(filename)

current_date = 'NO DATA'
if len(data) != 0:
    current_date = data['TIMESTAMP'][0][0:10]

data.TIMESTAMP = pd.to_datetime(data.TIMESTAMP)
data = data.rename(columns={'TIMESTAMP': 'TIMESTAMP (UTC)'})
data = data.set_index('TIMESTAMP (UTC)')

ax = plt.gca()

ax.set_title('Solar Radiation ' + current_date)
ax.set_ylabel('Irradiance (W/m2)')
ax.grid(True, which='both')

data['Global_Horizontal_Irradiance_Avg'].astype(float).plot(kind='line', linewidth=0.5, label='Global Horizontal Avg',
                                                            ax=ax)
# data['Global_Horizontal_Irradiance_Max'].astype(float).plot(kind='line',linewidth=0.5, label='Global Horizontal Max', ax=ax)
# data['Global_Horizontal_Irradiance_Min'].astype(float).plot(kind='line',linewidth=0.5, label='Global Horizontal Min', ax=ax)
# data['Global_Horizontal_Irradiance_Std'].astype(float).plot(kind='line',linewidth=0.5, label='Global Horizontal Std', ax=ax)
data['Global_Normal_Irradiance_Avg'].astype(float).plot(kind='line',linewidth=0.5, label='Global Normal Avg', ax=ax)
# data['Global_Normal_Irradiance_Max'].astype(float).plot(kind='line',linewidth=0.5, label='Global Normal Max', ax=ax)
# data['Global_Normal_Irradiance_Min'].astype(float).plot(kind='line',linewidth=0.5, label='Global Normal Min', ax=ax)
# data['Global_Normal_Irradiance_Std'].astype(float).plot(kind='line',linewidth=0.5, label='Global Normal Std', ax=ax)
data['Direct_Normal_Irradiance_Avg'].astype(float).plot(kind='line',linewidth=0.5, label='Direct Normal Avg', ax=ax)
# data['Direct_Normal_Irradiance_Max'].astype(float).plot(kind='line',linewidth=0.5, label='Direct Normal Max', ax=ax)
# data['Direct_Normal_Irradiance_Min'].astype(float).plot(kind='line',linewidth=0.5, label='Direct Normal Min', ax=ax)
# data['Direct_Normal_Irradiance_Std'].astype(float).plot(kind='line',linewidth=0.5, label='Direct Normal Std', ax=ax)

leg = ax.legend(loc='upper left')

for tick in ax.get_xticklabels():
    tick.set_rotation(25)

# savefilename = sys.argv[2]
# plt.savefig(savefilename)

plt.show()
