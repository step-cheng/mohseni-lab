"""
This code graphs 2 retention scans on the same plot in loglog scale, separating them based on how far about each one was taken
This is used to see how much a devices changes between two retention scans, thus the device should be in LRS or HRS both for both scans
"""

from sys import path_importer_cache
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from brokenaxes import brokenaxes

device_name = 'FIB3_K5'
path_a = f'/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-28/{device_name}_9_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_b = f'/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-31/{device_name}_10_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_a)
df_b = pd.read_csv(path_b)


time_a = [*df_a['# t_0'], *df_a['t_1'], *df_a['t_2'], *df_a['t_3'], *df_a['t_4']]
res_a = [*df_a[' r_0'], *df_a[' r_1'], *df_a[' r_2'], *df_a[' r_3'], *df_a[' r_4']]
time_b = [*df_b['# t_0'], *df_b['t_1'], *df_b['t_2'], *df_b['t_3'], *df_b['t_4']]
res_b = [*df_b[' r_0'], *df_b[' r_1'], *df_b[' r_2'], *df_b[' r_3'], *df_b[' r_4']]

res_a = [x for _,x in sorted(zip(time_a,res_a))]
res_b = [x for _,x in sorted(zip(time_b,res_b))]
time_a.sort()
time_b.sort()

ctime_a0 = os.path.getctime(path_a) 
ctime_b0 = os.path.getctime(path_b)

ctime_a = datetime.fromtimestamp(ctime_a0)
ctime_b = datetime.fromtimestamp(ctime_b0)

diff = ctime_b - ctime_a  # diff becomes a timedelta object
diff_sec = diff.total_seconds()  # this gives time difference in seconds, now add to time_b
print('Time difference between scans:', diff)

time_b = [i + diff_sec for i in time_b]

plt.figure(1)
bax = brokenaxes(xlims = ((0,max(time_a)+100),(min(time_b)-100, max(time_b)+100)))
bax.semilogy(time_a, res_a)
bax.semilogy(time_b, res_b)
bax.set_xlabel('time (s)')
bax.set_ylabel('resistance (Ohm)')
bax.set_title(f'{device_name} {str(diff)}')

log = input('Log the data? (y/n) \n')
if log == 'y':
    
    # log the data
    log_res_a = np.log10(res_a)
    log_res_b = np.log10(res_b)
    log_time_a = np.log10(time_a)
    log_time_b = np.log10(time_b)

    plt.figure(2)
    plt.loglog(time_a, res_a)
    plt.loglog(time_b, res_b)
    plt.xlabel('Time (s)')
    plt.ylabel('Resistance (Ohm)')
    plt.title(f'{device_name} {str(diff)}')

plt.show()
