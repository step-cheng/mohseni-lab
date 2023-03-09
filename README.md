# mohseni-lab
Wrote Python scripts to aid me in operating the measurement setup and organizing and analyzing data while researching high impedance memristors at the Mohseni Lab.

# target_pulse.py
Automates the use of a digital delay generator, pulse generator, low-noise amplifier, and digital multimeter to test and measure the memristor samples.
Follows an algorithm I wrote that sends bursts of square-wave pulses with the appropriate amplitude, pulse width, and pulses per burst to set the
device to a desired resistance range.
Uses a GUI interface.
Creates and saves graphs of the pulses sent and current measurements taken. Also saves a csv file of the current measurements and pulse configurations.
