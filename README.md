# mohseni-lab
Wrote Python scripts to aid me in operating the measurement setup and organizing and analyzing data while researching high impedance memristors at the Mohseni Lab.

# target_pulse.py
Automates the use of a digital delay generator, pulse generator, low-noise amplifier, and digital multimeter to test and measure the memristor samples.
Follows an algorithm I wrote that sends bursts of square-wave pulses with the appropriate amplitude, pulse width, and pulses per burst to set the
device to a desired resistance range. The algorithm is easily modifiable. The algorithm stops running once the device’s resistance is within the resistance range or after the number of tries is greater than the specified max number of tries.
Uses a GUI interface.
Creates and saves graphs of the pulses sent and current measurements taken. Also saves a csv file of the current measurements and pulse configurations.

# device_minutes.py
Do this after finishing measuring a device to record the minutes. When the code asks for the name, input the name just like how you would during a pulse or retention scan, i.e. FIB3_Q7. If the file already exists, it will ask you for permission to overwrite the file. In general, say yes. After the file has been created, it will ask if you want to go through the whole process again.
Tip: If you are trying to overwrite a file for a particular device, make sure that the file is unopened before attempting to overwrite the file. Otherwise, an error occurs.

# auto_short.py
Automates the use of a digital delay generator, pulse generator, low-noise amplifier, and digital multimeter to test and measure the memristor samples. Operates with a condition that the scan stops when the memristor’s resistance falls below a specified threshold, which means the device can be pulsed with incrementally increasing  voltage amplitudes and stops device reaches a certain maximum resistance. This is useful for forming a device.

# add_retention_plots.py
Graphs 2 retention scans of the same device on the same plot in loglog scale, separating them based on the time between each scan
This is used to see how much a devices changes between two retention scans, thus the device should be in LRS or HRS both for both scans

# pulse_current_to_res.py
Takes a file with current vs measurement number data and replots the data with resistance vs measurement number. Requires voltage bias and number of measurements per burst.

# change_scale.py
Takes retention scan csv file with current vs measurement number data and converts to log instead of linear scale

# retention_aggregate.py
Gets the aggregate LRS data of all the scans I have taken so far and plotting the data on a plot to see trends.

# retention_LRS_aggregate.py
Gets the aggregate LRS data of all the scans I have taken so far and plotting the data on a plot to see trends.

# retention_HRS_aggregate.py
Gets the aggregate HRS data of all the scans I have taken so far and plotting the data on a plot to see trends.
