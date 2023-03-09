"""
Takes retention csv file and converts to log instead of linear
"""

import matplotlib.pyplot as plt
import os
import pandas as pd
import csv

device = 'test_5GOhm'
index = '0'
date = '2022-10-19'
path = f'/Users/Lab User/Documents/Memristor/Measurements/Retention/{date}/{device}_{index}_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
data = pd.read_csv(path)

time = [*data['# t_0'], *data['t_1'], *data['t_2'], *data['t_3'], *data['t_4']]
res = [*data[' r_0'], *data[' r_1'], *data[' r_2'], *data[' r_3'], *data[' r_4']]
curr = [*data[' i_0'], *data[' i_1'], *data[' i_2'], *data[' i_3'], *data[' i_4']]

res = [x for _,x in sorted(zip(time,res))]
curr = [x for _,x in sorted(zip(time,curr))]
time.sort()

fig, (axc, axr) = plt.subplots(2,1, sharex = True)
axc.set_yscale('symlog')
axr.set_yscale('log')
axc.plot(time,curr)
axr.plot(time,res)
axc.set_title('current')
axr.set_title('resistance')

v_bias = '-0.1'
fig.suptitle(f'{device}_{index} Retention {v_bias}V')

fig.tight_layout()
plt.show()