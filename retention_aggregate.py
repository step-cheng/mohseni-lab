import pandas as pd
import numpy as np
import os
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

"""
make this with a for loop!
"""

"""
This is getting the aggregate the LRS data of all the scans I have taken so far and plotting the data on a plot to see trends.
Later, lets get the HRS as well
"""

plt.rcParams["figure.figsize"] = (10,6)

hrs_times = []
hrs_res = []

path_C6_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-04/FIB3_C6_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_C6_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-06/FIB3_C6_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_C6_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-09/FIB3_C6_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_C6_1)
df_b = pd.read_csv(path_C6_2)
df_c = pd.read_csv(path_C6_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_C6_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_C6_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_C6_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

hrs_times.extend(time)
hrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_C6')

path_E8_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-27/FIB3_E8_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E8_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-03/FIB3_E8_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E8_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-10/FIB3_E8_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_E8_1)
df_b = pd.read_csv(path_E8_2)
df_c = pd.read_csv(path_E8_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_E8_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_E8_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_E8_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

hrs_times.extend(time)
hrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_E8')

path_E9_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-09-30/FIB3_E9_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E9_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-03/FIB3_E9_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E9_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-10/FIB3_E9_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_E9_1)
df_b = pd.read_csv(path_E9_2)
df_c = pd.read_csv(path_E9_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_E9_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_E9_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_E9_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

hrs_times.extend(time)
hrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_E9')

path_E10_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-03/FIB3_E10_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E10_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-06/FIB3_E10_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_E10_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-10/FIB3_E10_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_E10_1)
df_b = pd.read_csv(path_E10_2)
df_c = pd.read_csv(path_E10_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_E10_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_E10_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_E10_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

hrs_times.extend(time)
hrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_E10')

path_C6_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-04/FIB3_C6_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_C6_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-06/FIB3_C6_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_C6_3 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-09/FIB3_C6_3_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_C6_1)
df_b = pd.read_csv(path_C6_2)
df_c = pd.read_csv(path_C6_3)

time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]
time_c = [df_c['# t_0'].iat[0], df_c['t_4'].iat[-1]]
res_c = [df_c[' r_0'].iat[0], df_c[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_C6_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_C6_2))
ctime_c = datetime.fromtimestamp(os.path.getctime(path_C6_3))
diff_ab = (ctime_b - ctime_a).total_seconds()
diff_bc = (ctime_c - ctime_a).total_seconds()

time_b = [i + diff_ab for i in time_b]
time_c = [i + diff_bc for i in time_c]
time = [*time_a, *time_b, *time_c]
res = [*res_a, *res_b, *res_c]

hrs_times.extend(time)
hrs_res.extend(res)

plt.semilogy(time, res, marker = 'x', label = 'FIB3_C6')

path_C10_1 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-04/FIB3_C10_1_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
path_C10_2 = '/Users/Lab User/Documents/Memristor/Measurements/Retention/2022-10-09/FIB3_C10_2_low_drift_LP6dB6dBHz_Integ1.0_Bias-0.1V.csv'
df_a = pd.read_csv(path_C10_1)
df_b = pd.read_csv(path_C10_2)
time_a = [df_a['# t_0'].iat[0], df_a['t_4'].iat[-1]]
res_a = [df_a[' r_0'].iat[0], df_a[' r_4'].iat[-1]]
time_b = [df_b['# t_0'].iat[0], df_b['t_4'].iat[-1]]
res_b = [df_b[' r_0'].iat[0], df_b[' r_4'].iat[-1]]

ctime_a = datetime.fromtimestamp(os.path.getctime(path_C10_1) )
ctime_b = datetime.fromtimestamp(os.path.getctime(path_C10_2))
diff = (ctime_b - ctime_a).total_seconds()
time_b = [i + diff for i in time_b]
time = [*time_a, *time_b]
res = [*res_a, *res_b]

hrs_times.extend(time)
hrs_res.extend(res)


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

log_res_a = np.log10(lrs_res)
log_res_b = np.log10(hrs_res)
log_time_a = np.log10(lrs_times)
log_time_b = np.log10(hrs_times) ##

# loglog fits
m1, c1 = np.polyfit(log_time_a, log_res_a, 1)
m2,c2 = np.polyfit(log_time_b, log_res_b, 1)
x_log = 10**((c2-c1)/(m1-m2))
etime_log = [np.log10(min(min(lrs_times), min(hrs_times))), np.log10(x_log), np.log10(x_log*10)]

plt.plot([10**i for i in etime_log], [10**(m1*i + c1) for i in etime_log], label = 'lrs aggregate')
plt.plot([10**i for i in etime_log], [10**(m2*i + c2) for i in etime_log], label = 'hrs aggregate')
plt.annotate(f'INTERSECTION', xy = (10**etime_log[1], 10**(m1*etime_log[1] + c1)))
length = timedelta(seconds = 10**etime_log[1])

plt.title(f'Aggregate HRS & LRS Retention 10/15/2022, Intersection {length}')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (Ohm)')
plt.legend()
plt.show()


