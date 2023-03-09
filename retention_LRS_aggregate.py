import pandas as pd
import numpy as np
import os
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

"""
This is getting the aggregate the LRS data of all the scans I have taken so far and plotting the data on a plot to see trends.
Later, lets get the HRS as well
"""

plt.rcParams["figure.figsize"] = (10,6)

lrs_times = []
lrs_res = []

path_E4_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-08-30/FIB3_E4_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E4_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-25/FIB3_E4_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E4_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-12/FIB3_E4_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_E4_1)
df_b = pd.read_csv(path_E4_2)
df_c = pd.read_csv(path_E4_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_E4_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_E4_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_E4_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_E4')


path_E5_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-08-30/FIB3_E5_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E5_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-25/FIB3_E5_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E5_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-13/FIB3_E5_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_E5_1)
df_b = pd.read_csv(path_E5_2)
df_c = pd.read_csv(path_E5_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_E5_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_E5_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_E5_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_E5')

path_E6_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-02/FIB3_E6_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E6_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-25/FIB3_E6_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E6_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-15/FIB3_E6_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'

df_a = pd.read_csv(path_E6_1)
df_b = pd.read_csv(path_E6_2)
df_c = pd.read_csv(path_E6_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_E6_1))
ctime_b = datetime.fromtimestamp(os.path.getctime(path_E6_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_E6_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_E6')

path_G6_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-08-23/FIB3_G6_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_G6_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-01/FIB3_G6_2_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_G6_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-25/FIB3_G6_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'

df_a = pd.read_csv(path_G6_1)
df_b = pd.read_csv(path_G6_2)
df_c = pd.read_csv(path_G6_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_G6_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_G6_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_G6_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_G6')

path_G10_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-08-30/FIB3_G10_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_G10_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-02/FIB3_G10_2_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_G10_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-15/FIB3_G10_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'

df_a = pd.read_csv(path_G10_1)
df_b = pd.read_csv(path_G10_2)
df_c = pd.read_csv(path_G10_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_G10_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_G10_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_G10_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_G10')

path_I8_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-08-22/FIB3_I8_1_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_I8_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-01/FIB3_I8_2_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_I8_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-15/FIB3_I8_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'

df_a = pd.read_csv(path_I8_1)
df_b = pd.read_csv(path_I8_2)
df_c = pd.read_csv(path_I8_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_I8_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_I8_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_I8_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_I8')

path_K5_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-08-12/FIB3_K5_1_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_K5_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-01/FIB3_K5_2_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_K5_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-19/FIB3_K5_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'

df_a = pd.read_csv(path_K5_1)
df_b = pd.read_csv(path_K5_2)
df_c = pd.read_csv(path_K5_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_K5_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_K5_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_K5_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_K5')

path_K7_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-08-08/FIB3_K7_1_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_K7_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-01/FIB3_K7_2_low_drift_LP6dB6dBHz_Integ1.0_Bias0.1V.csv'
path_K7_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-15/FIB3_K7_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'

df_a = pd.read_csv(path_K7_1)
df_b = pd.read_csv(path_K7_2)
df_c = pd.read_csv(path_K7_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_K7_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_K7_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_K7_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_K7')

path_C4_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-03/FIB3_C4_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_C4_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-06/FIB3_C4_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_C4_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-11/FIB3_C4_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'

df_a = pd.read_csv(path_C4_1)
df_b = pd.read_csv(path_C4_2)
df_c = pd.read_csv(path_C4_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_C4_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_C4_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_C4_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

lrs_times.extend(time)
lrs_res.extend(res)

plt.loglog(time, res, marker = 'x', label = 'FIB3_C4')

plt.title('Aggregate LRS Retention 10/11/2022')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (Ohm)')
plt.legend()
plt.show()