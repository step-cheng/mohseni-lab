from glob import glob
import tkinter as tk
from tkinter import filedialog, ttk, font
import matplotlib.backends.backend_tkagg as mplTk
import matplotlib.pyplot as plt
from matplotlib import rc, cm
from datetime import datetime
import os
from instr_inter import *
from time import sleep
import numpy as np
from scan import meas_current

def select_dir(*args):
   path= filedialog.askdirectory(title="Select a Folder")
   save_dir_val.set(path)

# Helper function to parse a comma seperated input string
def parse_csl(str):
    sub_strs = str.split(',')
    return np.array([float(sub.strip()) for sub in sub_strs])

def replot():  
    global meas_bias_v
    ax_meas.cla()
    ax_meas.set_xlabel('Measurement #')
    ax_meas.set_ylabel('Current (A)')
    if meas_bias_v is not None:
        ax_meas.set_title(f'Measurement Bias = {meas_bias_v:.3}V')
    ax_in.cla()
    ax_in.set_xlabel('Measurement #')
    ax_in.set_ylabel('Pulse Voltage (V)')

    meas_local_idx = 0
    #pulse_local_idx = 0

    # Just making sure the currents and pulse_hist are not None
    if currents is not None and pulse_hist is not None:
        for ii in range(min(currents.shape[0], pulse_hist.shape[0])):
            ax_meas.axvline(x=meas_local_idx-.5, c='k')
            v = pulse_hist[ii,0]
            for jj in range(currents.shape[1]):
                if currents[ii, jj] != np.NAN:
                    if v > 0:
                        ax_meas.plot(meas_local_idx, currents[ii, jj], 'ro')
                    else:
                        ax_meas.plot(meas_local_idx, currents[ii, jj], 'bo')
                    # Plot Pulses
                    if jj == 0:
                        plot_square(meas_local_idx, v)
                    else:
                        plot_zero(meas_local_idx, v)
                    meas_local_idx += 1

    fig_meas.tight_layout()
    fig_in.tight_layout()
    canvas_in.draw()
    canvas_meas.draw()
    canvas_in.flush_events()
    canvas_meas.flush_events()
    
def scale_change(*args):
    global plot_yscale_clicked
    try:
        val = plot_scale_clicked.get()
    except:
        return

    if val == 'symlog':
        plot_linthresh_meas.grid(column=2, row=6, sticky=tk.E, padx=5, pady=5)
        plot_linthresh_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        try:
            linthresh = plot_linthresh_val.get()
        except:
            return
        ax_meas.set_yscale(val, linthresh=linthresh)
    else:
        replot()
        plot_linthresh_meas.grid_remove()
        plot_linthresh_label.grid_remove()
        ax_meas.set_yscale(val)

    fig_meas.tight_layout()
    canvas_meas.draw()

def plot_square(idx, v):
    if v > 0:
        c = 'r'
    else:
        c = 'b'
    x = [idx-1, idx-.75, idx-.75, idx-.25, idx-.25, idx]
    y = [0, 0, v, v, 0, 0]
    ax_in.plot(x, y, c=c)

# plots the pulse graph
def plot_zero(idx, v):
    if v > 0:
        c = 'r'
    else:
        c = 'b'
    x = [idx-1, idx]
    y = [0, 0]
    ax_in.plot(x, y, c=c)

def save_data():
    lna_gain = lna_gain_mode_clicked.get().replace(' ', '_')
    lna_filter = lna_filter_clicked.get().replace(' ', '_')
    if lna_filter != 'None':
        filter_str = f'{lna_gain}_LP{lna_filter}{lna_filter_clicked.get()}Hz'
    else:
        filter_str = f'{lna_gain}_None'
    device_name = device_name_val.get()
    device_idx = device_idx_val.get()
    dir_name = save_dir_val.get()
    integ_time=dmm_integ_clicked.get()
    title = f'{device_name}_{device_idx}_{filter_str}_Integ{integ_time}'

    # Create dir if it does not exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)
    fig_meas.savefig(os.path.join(dir_name, f'{title}.png'))
    fig_in.savefig(os.path.join(dir_name, f'{title}_pulse_figure.png'))

    # Save the raw data to a directory
    headers = ['pulse_v', 'pulse_width', 'num_applied', 'meas_v'] + [f'i_{ii}' for ii in range(currents.shape[1])] # it is getting the number of measurements
    header_str = ','.join(headers)
    print("Final Pulse History: \n", pulse_hist)
    print("Unedited Currents Array\n: ", currents)
    print("Saved Currents Array\n: ", currents[-pulse_hist.shape[0]:])
    save_arr = np.hstack((pulse_hist, 
                          meas_bias_v*np.ones((pulse_hist.shape[0],1)),
                          currents[-pulse_hist.shape[0]:]))
    np.savetxt(os.path.join(dir_name, f'{title}.csv'), save_arr, 
                delimiter=",",header=header_str)

# This does the sweeping
def pulse_train(v, pulse_on_period, burst_period, 
                pulse_number, trig_freq, curr_min, curr_max):
    
    print(f"Pulse Train: {v}V")
    # Set up
    relay.switch_relay(relay.NONE)
    PGen.config_pulse(pulse_voltage=v, pulse_width='in')
    # Set the LNA bias
    LNA.set_bias(round(meas_bias_v*1000))
    sleep(0.5)
    num_meas = dmm_num_val.get()
    global pulse_idx, meas_idx, currents, e_stop

    # Set up burst
    DGen.config_burst(pulse_on_period, burst_period, pulse_number, 
                      trig_freq, 2, bnc=1, channel_start=2, channel_end=3)
    DGen.config_burst(pulse_on_period, burst_period, pulse_number, 
                      trig_freq, 2, bnc=2, channel_start=4, channel_end=5)
    PGen.config_pulse(pulse_voltage=v, pulse_width='in')
    sleep(0.5)
    sens = lna_sens_clicked.get()

    # Start with pulse
    relay.switch_relay(relay.DGEN)
    DGen.trig_burst() # Triggers burst
    relay.switch_relay(relay.LNA)
    
    plot_square(meas_idx, v)
    ax_meas.axvline(x=meas_idx-.5, c='k')

    # plots the max curr and min curr
    ax_meas.plot([ii for ii in range(meas_idx, meas_idx+num_meas+1)],
                 [curr_min for jj in range(0, num_meas+1)], 'g')
    ax_meas.plot([ii for ii in range(meas_idx, meas_idx+num_meas+1)],
                [curr_max for jj in range(0, num_meas+1)], 'g')
    
    # Measurements after each burst, does plotting
    for kk in range(num_meas):

        # This is the actual measuring portion below, meas_current is in scan.py file, why does it return sens?
        currents[pulse_idx, kk], sens = meas_current(sens, LNA, DMM,
                                                    LNA_gui_var=curr_var, 
                                                    Sens_gui_var=sens_var)

        # all plotting
        if v > 0:
            ax_meas.plot(meas_idx, currents[pulse_idx, kk], 'ro')
        else:
            ax_meas.plot(meas_idx, currents[pulse_idx, kk], 'bo')
        if kk > 0:
            plot_zero(meas_idx, v)

        # ax_meas.plot(meas_idx, curr_min, 'go')
        # ax_meas.plot(meas_idx, curr_max, 'go')

        # Pause to allow plots and progress bar to update
        fig_in.tight_layout()
        canvas_in.draw()
        canvas_in.flush_events()
        fig_meas.tight_layout()
        canvas_meas.draw()
        canvas_meas.flush_events()
        sleep(0.02)

        meas_idx += 1
    pulse_idx += 1
    new_current_row = np.ones((1,currents.shape[1]))
    new_current_row[:] = np.nan
    currents = np.vstack((currents, new_current_row))
    LNA.set_bias(0)

def measure_loop(first_v, res_min, res_max, max_tries, pulse_on_period, 
                 burst_period, pulse_num, trig_freq):
    global currents, pulse_idx, meas_idx, pulse_hist, meas_bias_v, e_stop
    e_stop = False
    curr_min = meas_bias_v/res_max
    curr_max = meas_bias_v/res_min
    sens = lna_sens_clicked.get()
    relay.switch_relay(relay.LNA)
    # First measure the current to see what's up with the device
    LNA.set_bias(round(meas_bias_v*1000))
    curr, sens = meas_current(sens, LNA, DMM,
                            LNA_gui_var=curr_var, 
                            Sens_gui_var=sens_var)
    res = abs(meas_bias_v/curr)
    attempt = 0
    amplitude = first_v
    add = 0.5
    pulse_config_arr = np.ones((1, 3))
    # If resistance is not within range
    while ((res < res_min or res > res_max) and attempt < max_tries):
        if e_stop:
            relay.switch_relay(relay.NONE)
            LNA.set_bias(0)
            print("Emergency Stopped!")
            break
        print("Resistance: ", res)
        if (attempt == 0):
            pulse_train(amplitude, pulse_on_period, burst_period, pulse_num, trig_freq,
                        curr_min, curr_max)
        else:
            # if the resistance is close to the resistance range, decrease the increment
            if (1 > res_max/res > 0.5 or 1 < res_min/res < 2):
                add = 0.20
            else:
                add = 0.50

            # go through the measurement loop
            if (res < res_min):
                # if the resistance is too low but the pulse is positive, must make pulse negative
                if (amplitude > 0):
                    amplitude = -add
                    pulse_train(amplitude, pulse_on_period, burst_period, pulse_num, trig_freq,
                                curr_min, curr_max)
                # if previous pulse changed the current enough, repeat
                elif (currents.shape[0] >= 3 and abs(currents[-2,-1]/currents[-3,-1]) < 4/7):
                    pulse_train(amplitude, pulse_on_period, burst_period, pulse_num, trig_freq,
                                curr_min, curr_max)
                else:
                    amplitude -= add
                    pulse_train(amplitude, pulse_on_period, burst_period, pulse_num, trig_freq,
                                curr_min, curr_max)
            elif (res > res_max):
                # if the resistance is too high but the pulse is negative, must make pulse positive
                if (amplitude < 0):
                    amplitude = add
                    pulse_train(amplitude, pulse_on_period, burst_period, pulse_num, trig_freq,
                                curr_min, curr_max)
                elif (currents.shape[0] >= 3 and abs(currents[-2,-1]/currents[-3,-1]) > 1.75):
                    pulse_train(amplitude, pulse_on_period, burst_period, pulse_num, trig_freq,
                                curr_min, curr_max)
                else:
                    amplitude += add
                    pulse_train(amplitude, pulse_on_period, burst_period, pulse_num, trig_freq,
                                curr_min, curr_max)
        
        # Add array to pulse history
        pulse_config_arr[0, 0] = amplitude
        pulse_config_arr[0, 1] = pulse_on_period
        pulse_config_arr[0, 2] = pulse_num
        res = abs(meas_bias_v/currents[-2, -1])
        if attempt == 0:
            print("Should only print once...")
            pulse_hist = pulse_config_arr
        else:
            print("config arr: ", pulse_config_arr)
            print("small pulse hist: ", pulse_hist)
            pulse_hist = np.vstack((pulse_hist, pulse_config_arr))
        attempt += 1
        print("Number of attempts: ", attempt)
        print("Pulse History Update: \n", pulse_hist)
    
    # last row is an extra row of nan        
    currents = currents[0:-1]

# Biggest loop
def dynamic_scan(*args):
    # Get pulse configs from GUI
    first_v = pulse_v_val.get()
    pulse_on_period = float(pulse_period_val.get())
    pulse_off_period = pulse_on_period
    pulse_per_burst = int(pulse_per_burst_val.get())
    pulse_number = int(pulse_per_burst_val.get())
    burst_period = (pulse_on_period+pulse_off_period)
    trig_period = pulse_per_burst*(burst_period)*2
    trig_freq = 1/trig_period
    res_range = parse_csl(res_range_val.get())
    max_tries = max_tries_val.get()
    res_min = res_range[0]
    res_max = res_range[1]
    assert res_max > res_min, "1st argument must be less than 2nd argument"

    # Cease operating GUI
    save_dir_btn['state'] = tk.DISABLED
    pb.grid(column=0, row=2, columnspan=3, sticky='EW', padx=5, pady=5)
    stop_btn.grid(column=0, row=1, columnspan=3, sticky='EW', padx=5, pady=5)
    sens_label.grid(column=0, row=3, sticky='EW', padx=5, pady=5)
    curr_label.grid(column=2, row=3, sticky='EW', padx=5, pady=5)
    sleep(0.2)

    # Pull parameters from GUI to initialize instruments
    DMM.set_integ_time(dmm_integ_clicked.get())
    lna_gain = lna_gain_mode_clicked.get().replace(' ', '_')
    lna_filter = lna_filter_clicked.get().replace(' ', '_')
    LNA.set_filter(lna_gain, lna_filter, lna_filter_freq_clicked.get())
    meas_per_volt = dmm_num_val.get()

    global currents, pulse_idx, meas_idx, pulse_hist, meas_bias_v

    # Get and Set bias for the LNA
    new_bias_v = lna_bias_clicked.get()
    is_new_bias = meas_bias_v is None or new_bias_v != meas_bias_v


    # Create/Adjust currents array
    if hold_on.get() and currents is not None and not is_new_bias:
        if currents.shape[1] < meas_per_volt:       # checks if new meas_per_volt is greater
            # First add additional columns to the original array, hstack extends an np array in horizontal dimension
            filler_arr = np.empty(currents.shape[0], meas_per_volt-currents.shape[1])
            filler_arr[:] = np.nan
            currents = np.hstack(currents, filler_arr)
        # Array: bursts vs measurements
        sub_arr = np.empty((1, currents.shape[1]))
        sub_arr[:] = np.nan
        
        # extend empty cells in the array to prepare for next measurements in the pulse_train
        currents = np.vstack((currents, sub_arr))
    else:
        meas_bias_v = new_bias_v
        pulse_idx = 0
        meas_idx = 0
        ax_meas.cla()
        ax_in.cla()

        ax_meas.set_xlabel('Measurement #')
        ax_meas.set_ylabel('Current (A)')
        ax_meas.set_title(f'Measurement Bias = {meas_bias_v:.3}V')
        ax_meas.relim()
        ax_meas.autoscale_view()
        fig_meas.tight_layout()

        ax_in.set_xlabel('Measurement #')
        ax_in.set_ylabel('Pulse Voltage (V)')
        ax_in.relim()
        ax_in.autoscale_view()
        fig_in.tight_layout()

        # THIS IS WHERE currents IS INITIALIZED
        currents = np.empty((1, meas_per_volt))
        currents[:] = np.nan


    # Measure the current to see what's up with the device
    measure_loop(first_v, res_min, res_max, max_tries, pulse_on_period,
                 burst_period, pulse_number, trig_freq)
    
    save_data()

    # Increment index
    device_idx_val.set(device_idx_val.get()+1)
    save_dir_btn['state'] = tk.NORMAL
    pb.grid_remove()
    sens_label.grid_remove()
    curr_label.grid_remove()
    stop_btn.grid_remove()

    res = abs(meas_bias_v/currents[-2, -1])
    if (res > res_min and res < res_max):
        print("done!")
    else:
        print(f"Completed all {max_tries} tries, but missed the resistance range of {res_min} to {res_max} Ohms")

        
# Intialize Instruments
relay = relay_inter.relay_inter()
relay.switch_relay(relay.NONE) # Close relay during setup
DGen = DG645.DG645()
DMM = A34410A.A34410A()
LNA = SR570.SR570()
PGen = AV1010B.AV1010B()
PGen.set_trigger('EXT')

# Initial global variables
currents = None
meas_idx = None
pulse_idx = None
pulse_hist = None
meas_bias_v = None
e_stop = False

root = tk.Tk()
root.state('zoomed')
root.title('Target Pulse GUI')
dashboard_frame = tk.Frame(root)
dashboard_frame.grid(column=0, row=0, rowspan=4, sticky=tk.N)

## Device options
device_frame = tk.Frame(dashboard_frame, bd=2, width=450)
device_frame.grid(column=0, row=0,sticky=tk.W+tk.E)
device_frame.grid_columnconfigure(0, weight=1)
# Save Dir
save_dir_label = tk.Label(device_frame, text='Save Folder')
save_dir_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
save_dir_btn = tk.Button(device_frame, text='Browse', command=select_dir)
save_dir_btn.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
save_dir_val = tk.StringVar()
save_dir_entry = tk.Entry(device_frame, text=save_dir_val, width=50)
save_dir_entry.grid(column=0, row=2, columnspan=2, sticky=tk.W, padx=5, pady=5)
now = datetime.now()
date = now.strftime('%Y-%m-%d')
save_dir_val.set(os.path.join('.', 'Measurements','Pulse', date))
# Device Name
device_name_label = tk.Label(device_frame, text='Device Name')
device_name_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
device_name_val = tk.StringVar()
device_name_meas = tk.Entry(device_frame, text=device_name_val, width=20)
device_name_meas.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
device_name_val.set('FIB3_E5_3')

# Meas Idx
device_idx_label = tk.Label(device_frame, text='Index')
device_idx_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
device_idx_val = tk.IntVar()
device_idx_meas = tk.Entry(device_frame, text=device_idx_val, width=20)
device_idx_meas.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
device_idx_val.set(0)

## LNA Options
lna_frame = tk.Frame(dashboard_frame, bd=2, width=375)
lna_frame.grid(column=0, row=1, sticky=tk.W+tk.E)
lna_frame.grid_columnconfigure(0, weight=1)
# Label for the subframe
tk.Label(lna_frame, text='LNA', font=('Arial',12)).grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
# Gain Mode
lna_gain_mode_label = tk.Label(lna_frame, text='Gain Mode')
lna_gain_mode_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
lna_gain_mode_options = [m.replace('_', ' ') for m in list(SR570.SR570.gain_modes.keys())]
lna_gain_mode_clicked = tk.StringVar()
lna_gain_mode_clicked.set(lna_gain_mode_options[2])
lna_gain_mode_menu = tk.OptionMenu(lna_frame, lna_gain_mode_clicked ,*lna_gain_mode_options)
lna_gain_mode_menu.config(width=len(max(lna_gain_mode_options)))
lna_gain_mode_menu.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
# Filter Type
lna_filter_label = tk.Label(lna_frame, text='LP Cutoff')
lna_filter_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
lna_filter_options = list(SR570.SR570.filters.keys())
lna_filter_options[0] = 'None' # Convert None to a string
lna_filter_clicked = tk.StringVar()
lna_filter_clicked.set(lna_filter_options[1])
lna_filter_menu = tk.OptionMenu(lna_frame, lna_filter_clicked ,*lna_filter_options)
lna_filter_menu.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
# Filter cutoff frequency
lna_filter_freq_label = tk.Label(lna_frame, text='LP Cutoff Frequency (Hz)')
lna_filter_freq_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
lna_filter_freq_options = [f'{f}' for f in SR570.SR570.filter_freqs]
lna_filter_freq_clicked = tk.DoubleVar()
lna_filter_freq_clicked.set(lna_filter_freq_options[3])
lna_filter_freq_menu = tk.OptionMenu(lna_frame, lna_filter_freq_clicked ,*lna_filter_freq_options)
lna_filter_freq_menu.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
# Initial Sens
lna_sens_label = tk.Label(lna_frame, text='Initial Sensitivity')
lna_sens_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
lna_sens_options = list(range(len(SR570.SR570.sens_table)))
lna_sens_clicked = tk.IntVar()
lna_sens_clicked.set(lna_sens_options[0])
lna_sens_menu = tk.OptionMenu(lna_frame, lna_sens_clicked ,*lna_sens_options)
lna_sens_menu.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
# LNA bias during measurement
lna_bias_label = tk.Label(lna_frame, text='LNA Measurement Bias (V)')
lna_bias_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
lna_bias_clicked = tk.DoubleVar()
lna_bias_clicked.set(-0.1)
lna_bias_menu =  tk.Entry(lna_frame, text=lna_bias_clicked, width=10)
lna_bias_menu.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
# Offset correction
lna_offset = tk.BooleanVar()
lna_offset_check = tk.Checkbutton(lna_frame, text='Offset Correction', variable=lna_offset)
lna_offset_check.grid(column=0, row=6, columnspan=2, padx=5, pady=5)

## DMM Options
dmm_frame = tk.Frame(dashboard_frame, bd=2, width=375)
dmm_frame.grid(column=0, row=2, sticky=tk.W+tk.E)
dmm_frame.grid_columnconfigure(0, weight=1)
# Label for the subframe
tk.Label(dmm_frame, text='DMM', font=('Arial',12)).grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
# Integration time
dmm_integ_label = tk.Label(dmm_frame, text='Integration Time (* 1/60 s)')
dmm_integ_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
dmm_integ_options = A34410A.A34410A.integ_times
dmm_integ_clicked = tk.DoubleVar()
dmm_integ_clicked.set(dmm_integ_options[4])
dmm_integ_menu = tk.OptionMenu(dmm_frame, dmm_integ_clicked ,*dmm_integ_options)
dmm_integ_menu.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
# Measurements per voltage
dmm_num_label = tk.Label(dmm_frame, text='Measurements per voltage')
dmm_num_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
dmm_num_val = tk.IntVar()
dmm_num_meas = tk.Entry(dmm_frame, text=dmm_num_val, width=5)
dmm_num_meas.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
dmm_num_val.set(5)
# Initial measurements to discard per voltage
dmm_discard_label = tk.Label(dmm_frame, text='Initial discarded')
dmm_discard_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
dmm_discard_val = tk.IntVar()
dmm_discard_meas = tk.Entry(dmm_frame, text=dmm_discard_val, width=5)
dmm_discard_meas.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
dmm_discard_val.set(0)

## Pulse Parameters
pulse_frame = tk.Frame(dashboard_frame, bd=2, width=375)
pulse_frame.grid(column=0, row=3, sticky=tk.W+tk.E)
pulse_frame.grid_columnconfigure(0, weight=1)
# Label for the subframe
tk.Label(pulse_frame, text='Pulse Measurement', font=('Arial',12)).grid(column=0, row=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
# Starting Pulse Voltage
pulse_v_label = tk.Label(pulse_frame, text='Starting Pulse Amplitude (V)')
pulse_v_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
pulse_v_val = tk.DoubleVar()
pulse_v_meas = tk.Entry(pulse_frame, text=pulse_v_val, width=25)
pulse_v_meas.grid(column=1, row=1, sticky=tk.E+tk.W, padx=5, pady=5)
pulse_v_meas.grid_columnconfigure(1, weight=1)
pulse_v_val.set(8.0)
# Pulse period
pulse_period_label = tk.Label(pulse_frame, text='Pulse On Period (s)')
pulse_period_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
pulse_period_val = tk.StringVar()
pulse_period_meas = tk.Entry(pulse_frame, text=pulse_period_val, width=25)
pulse_period_meas.grid(column=1, row=2, sticky=tk.E+tk.W, padx=5, pady=5)
pulse_period_meas.grid_columnconfigure(1, weight=1)
pulse_period_val.set('500e-9')
# Pulse per Burst
pulse_per_burst_label = tk.Label(pulse_frame, text='Pulses per burst')
pulse_per_burst_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
pulse_per_burst_val = tk.StringVar()
pulse_per_burst_meas = tk.Entry(pulse_frame, text=pulse_per_burst_val, width=25)
pulse_per_burst_meas.grid(column=1, row=3, sticky=tk.E+tk.W, padx=5, pady=5)
pulse_per_burst_meas.grid_columnconfigure(1, weight=1)
pulse_per_burst_val.set('1000')

# Dynamic Parameters
dynamic_frame = tk.Frame(dashboard_frame, bd=2, width=375)
dynamic_frame.grid(column=0, row=4, sticky=tk.W+tk.E)
dynamic_frame.grid_columnconfigure(0, weight=1)
# Label for the subframe
tk.Label(dynamic_frame, text="Dynamic Targets", font=("Arial",12)).grid(column=0, row=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
# Resistance Limit
res_range_label = tk.Label(dynamic_frame, text = 'Resistance Limit (min, max)')
res_range_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
res_range_val = tk.StringVar()
res_range_meas = tk.Entry(dynamic_frame, text=res_range_val, width=25)
res_range_meas.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
res_range_meas.grid_columnconfigure(1, weight=1)
res_range_val.set('1e6, 1e7')
# Tries Limit
max_tries_label = tk.Label(dynamic_frame, text = 'Max Tries')
max_tries_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
max_tries_val = tk.IntVar()
max_tries_meas = tk.Entry(dynamic_frame, text=max_tries_val, width=25)
max_tries_meas.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
max_tries_meas.grid_columnconfigure(1, weight=1)
max_tries_val.set(30)


## Plot Settings
plot_frame = tk.Frame(dashboard_frame, bd=2, width=375)
plot_frame.grid(column=0, row=5, sticky=tk.W+tk.E)
plot_frame.grid_columnconfigure(0, weight=1)
# Button to start sweep
ft = font.Font(size='14', weight='bold')
save_dir_btn = tk.Button(plot_frame, text='Start Pulsing', command=dynamic_scan, font=ft)     # THIS STARTS THE SCAN!!
save_dir_btn.grid(column=0, row=0, columnspan=3, sticky='EW', padx=5, pady=5)
# Progress bar for the scan
progress_var = tk.DoubleVar()
pb = ttk.Progressbar(plot_frame, orient='horizontal', mode='determinate', variable=progress_var)
# Labels for the current sens and current
sens_var = tk.StringVar()
curr_var = tk.StringVar()
sens_label = tk.Label(plot_frame, textvariable=sens_var)
curr_label = tk.Label(plot_frame, textvariable=curr_var)
def set_e_stop():
    global e_stop
    e_stop = True
stop_btn = tk.Button(plot_frame, text='Stop', command=set_e_stop, 
                    bg='red', fg='white', font=ft)

# Keep previous plots
hold_on = tk.BooleanVar()
plot_hold_on_check = tk.Checkbutton(plot_frame, text='Hold On', variable=hold_on)
hold_on.set(True)
plot_hold_on_check.grid(column=0, row=4, padx=5, pady=5)
# Set linthresh for symlog
plot_linthresh_label = tk.Label(plot_frame, text='Symlog linthresh')
plot_linthresh_val = tk.DoubleVar()
plot_linthresh_meas = tk.Entry(plot_frame, text=plot_linthresh_val, width=10)
plot_linthresh_val.set(1e-9)
# Plot Scale
plot_scale_label = tk.Label(plot_frame, text='Y-Scale')
plot_scale_label.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
plot_scale_options = ['linear', 'log', 'symlog']
plot_scale_clicked = tk.StringVar()
plot_scale_clicked.set(plot_scale_options[0])
plot_scale_menu = tk.OptionMenu(plot_frame, plot_scale_clicked ,*plot_scale_options)
plot_scale_menu.config(width=6)
plot_scale_menu.grid(column=2, row=4, sticky=tk.E, padx=5, pady=5)

plot_linthresh_val.trace('w', scale_change)
plot_scale_clicked.trace('w', scale_change)

## Figure settings
font = {'size'   : 12}
rc('font', **font)

# Measurement Figures
fig_meas, ax_meas = plt.subplots(1, 1)
fig_meas.set_size_inches(2*8,2*2.25)
canvas_meas = mplTk.FigureCanvasTkAgg(fig_meas, master=root)
canvas_meas.get_tk_widget().grid(column=1, row=0, sticky=tk.W+tk.E)
ax_meas.set_xlabel('Measurement #')
ax_meas.set_ylabel('Current (A)')
fig_meas.tight_layout()

frame_meas_toolbar = tk.Frame(root)
frame_meas_toolbar.grid(row=1, column=1, sticky=tk.E)
toolbar_meas = mplTk.NavigationToolbar2Tk(canvas_meas, frame_meas_toolbar)
toolbar_meas.update()

# Pulse figure
fig_in, ax_in = plt.subplots(1,1)
fig_in.set_size_inches(2*8,2*2.25)
canvas_in = mplTk.FigureCanvasTkAgg(fig_in, master=root)
canvas_in.get_tk_widget().grid(column=1, row=2, sticky=tk.W+tk.E)
ax_in.set_xlabel('Measurement #')
ax_in.set_ylabel('Pulse Voltage (V)')
fig_in.tight_layout()

frame_in_toolbar = tk.Frame(root)
frame_in_toolbar.grid(row=3, column=1, sticky=tk.E)
toolbar_in = mplTk.NavigationToolbar2Tk(canvas_in, frame_in_toolbar)
toolbar_in.update()

root.mainloop()

# # ADDED PART
# res_limit = input('Res Limit: \n')
# current = 


""""
Two options:
1. New function with while loop with resistance range, max number of tries, etc
    aka While not Done, where Done is boolean to check if I hit res range, max # tries, etc
    then two if statements, if below or if above bound, else we good
    need to call functions already written by Leo, might be hard if you have to edit the functions to be compatible
    need to make sure currents variable updates continuously without overwriting
    Need to do start scan so it calls the new function dynamic
2. Add while loop within new function
    function similar to option 1, but instead of calling old function, paste entire pulse_train

Better to do option 1
"""