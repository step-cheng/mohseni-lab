"""
Do this after finishing measuring a device to record the minutes. When the code asks for the name, input the name just like how you
would during a pulse or retention scan, i.e. FIB3_Q7. If the file already exists, it will ask you for permission to overwrite the file.
In general, say yes. After the file has been created, it will ask if you want to go through the whole process again.
Tip: If you are trying to overwrite a file for a particular device, make sure that the file is unopened before attempting to overwrite
the file. Otherwise, an error occurs.
The description of how the code works is found in the comments throughout the code.
"""

import os
import openpyxl
import pandas as pd
import datetime
import glob

# while loop with again variable so you can create device minutes for multiple devices in a row
again = bool(True)
while again == True:
    # Desired Device Name
    name = input("What device name? \n")
    short = input('Did the device short? (y/n) \n')

    # retrieves days that pulse and retention measurements were taken
    pulse_days = os.listdir(r"C:\Users\Lab User\Documents\Memristor\Measurements\Pulse")
    retention_days = os.listdir(r"C:\Users\Lab User\Documents\Memristor\Measurements\Retention")

    # path templates
    p_sub = "/Users/Lab User/Documents/Memristor/Measurements/Pulse/{}/"
    r_sub = "/Users/Lab User/Documents/Memristor/Measurements/Retention/{}/"
    p_sub_ = "/Users/Lab User/Documents/Memristor/Measurements/Pulse/{}/{}"
    r_sub_ = "/Users/Lab User/Documents/Memristor/Measurements/Retention/{}/{}"

    def find_indices(li, c1, c2):
        findsc1 = []
        findsc2 = []
        if len(li) == 0:
            return []
        for x in li:
            fi = x.find(c1)
            if fi != -1:
                findsc1.append(li.index(x))
            fi = x.find(c2)
            if fi != -1:
                findsc2.append(li.index(x))
        return list(set(findsc1) & set(findsc2))


    # get pulse file names and times
    pulse_desired_names = []
    pulse_desired_times = []

    for ii in range(len(pulse_days)):
        os.chdir(p_sub.format(pulse_days[ii]))
        daily_list = os.listdir()
        desired_indices = find_indices(daily_list,name,".csv")

        # creates the list of the csv file names
        for jj in range(len(desired_indices)):
            pulse_desired_names.append(daily_list[desired_indices[jj]])
        
        for kk in range(len(pulse_desired_names)-len(desired_indices), len(pulse_desired_names)): # this range ignores file names from previous days
            temp_file_time = os.path.getmtime(p_sub_.format(pulse_days[ii], pulse_desired_names[kk]))
            file_time = datetime.datetime.fromtimestamp(temp_file_time)
            pulse_desired_times.append(file_time)

            #FIB3_O7_27_low_drift_LP6dB6dBHz_Integ1.0
        
        # sort them by time
        sub_pulse_desired_times = pulse_desired_times[:]
        sub_pulse_desired_names = pulse_desired_names[:]
        pulse_desired_times.sort()
        for x in range(len(pulse_desired_times)):
            ind = pulse_desired_times.index(sub_pulse_desired_times[x])
            pulse_desired_names[ind] = sub_pulse_desired_names[x]


    # get retention file names and times
    ret_desired_names = []
    ret_desired_times = []

    for ii in range(len(retention_days)):
        daily_list = os.listdir(r_sub.format(retention_days[ii]))
        desired_indices = find_indices(daily_list,name,".csv")

        for jj in range(len(desired_indices)):
            ret_desired_names.append(daily_list[desired_indices[jj]])

        for kk in range(len(ret_desired_names)-len(desired_indices), len(ret_desired_names)):
            temp_file_time = os.path.getmtime(r_sub_.format(retention_days[ii], ret_desired_names[kk]))
            file_time = datetime.datetime.fromtimestamp(temp_file_time)
            ret_desired_times.append(file_time)

        # sort by time
        sub_ret_desired_times = ret_desired_times[:]
        sub_ret_desired_names = ret_desired_names[:]
        ret_desired_times.sort()
        for x in range(len(ret_desired_times)):
            ind = ret_desired_times.index(sub_ret_desired_times[x])
            ret_desired_names[ind] = sub_ret_desired_names[x]
        
    # group the pulse and retention files together

    all_names = pulse_desired_names + ret_desired_names
    all_times = pulse_desired_times + ret_desired_times

    # sort everything by time, so the list entries should correspond correctly
    sub_all_times = all_times[:]
    sub_all_names = all_names[:]
    all_times.sort()
    for x in range(len(all_times)):
        ind = all_times.index(sub_all_times[x])
        all_names[ind] = sub_all_names[x]


    # create the type list
    test_types = ['Pulse']*len(all_names)
    for ii in range(len(test_types)):
        if all_names[ii].find('Bias') != -1:
            test_types[ii] = 'Retention'

    dir_template = r"C:\Users\Lab User\Documents\Memristor\Measurements\{}\{}\{}"
    directories = [0]*len(all_names)

    new_all_times =[0] * len(all_times)
    for ind,time in enumerate(all_times):
        new_all_times[ind] = str(time)[:19]

    for ii in range(len(all_names)):
        directories[ii] = dir_template.format(test_types[ii], new_all_times[ii][:10], all_names[ii])

    # Create dataframe
    df = pd.DataFrame(
        {
            "Time": new_all_times,
            "Type": test_types,
            "Name": all_names,
            "Directory": directories
        }
    )

    # Create csv file
    if short == 'n':
        new_file = str("/Users/Lab User/Documents/Memristor/Measurements/Device Minutes/"+name+"_Minutes.csv")
    elif short == 'y':
        new_file = str("/Users/Lab User/Documents/Memristor/Measurements/Device Minutes/"+name+"_Minutes_SHORT.csv")
    file_present = os.path.exists(new_file)
    if file_present:
        check = input("Warning: File for this device has already exists! Proceed? (y/n)\n")
        if check == 'y':
            df.to_csv(new_file)
            print(new_file, "has been recreated")
        else:
            print(new_file, "has not been recreated")   
    else:
        df.to_csv(new_file)
        print(new_file, "has been created")
    
    ask = input("Again? (y/n)\n")
    if ask == 'y':
        again = bool(True)
    elif ask == 'n':
        again = bool(False)
