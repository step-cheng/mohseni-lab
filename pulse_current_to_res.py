import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# input the path
f_path = ("/Users/Lab User/Documents/Memristor/Measurements/Pulse/2022-06-07/FIB3_E3_19_low_drift_LP6dB6dBHz_Integ1.0.csv") # input date, file name
df = pd.read_csv(f_path)

# input measurement bias
v_bias = 0.01
meas_number = 5

n_ind = []
p_ind = []
all_pulses = df['# pulse_v']
for x in range(len(all_pulses)):
    if all_pulses[x] < 0:
        n_ind.append(x)
    elif all_pulses[x] >= 0:
        p_ind.append(x)

n_pts = []
for i in n_ind:
    n_next = [meas_number*i, meas_number*i+1, meas_number*i+2, meas_number*i+3, meas_number*i+4]
    n_pts = n_pts + n_next

p_pts = []
for i in p_ind:
    p_next = [meas_number*i, meas_number*i+1, meas_number*i+2, meas_number*i+3, meas_number*i+4]
    p_pts = p_pts + p_next

n_currents = []
for i in n_ind:
    n_curr = [df['i_0'][i], df['i_1'][i], df['i_2'][i], df['i_3'][i], df['i_4'][i]]
    n_currents = n_currents + n_curr

n_res = [abs(v_bias/i) for i in n_currents]

p_currents = []
for i in p_ind:
    p_curr = [df['i_0'][i], df['i_1'][i], df['i_2'][i], df['i_3'][i], df['i_4'][i]]
    p_currents = p_currents + p_curr

p_res = [abs(v_bias/i) for i in p_currents]

fig, ax = plt.subplots(1,1)
fig.set_size_inches(2*8,2*2.25)
ax.plot(p_pts, p_res, 'o', markersize = 5, color = 'r')
ax.plot(n_pts, n_res, 'o', markersize = 5, color = 'b')
ax.set_yscale('symlog')
ax.set_xlabel('Measurement Number')
ax.set_ylabel('Resistance (Ohm)')
title = '{} Measurement Bias = {}V'
fig.suptitle(title.format('FIB3_E3', v_bias))
for i in range(len(df['# pulse_v'])):
    plt.axvline(x = 5*i-0.5, c = 'k')
plt.show()


# break the part into two with negative voltage pulses grphed at one time and positive voltage pulses graphed at another