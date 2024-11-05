import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from numpy.ma.core import shape

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = 0
## YOUR CODE HERE ##
data = np.loadtxt(signal_filepath, skiprows=2, delimiter=',')

column1 = data[0:,0]
column2 = data[0:,1]
column3 = data[0:,2]

plt.plot(column2)
plt.xlim(0, 5000)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('EKG Data Raw')
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##
#data = np.convolve(data, )
#critical_freq = (2*15)/250
#data = sp.butter(data, Wn=250,)

fs_sampling_rate=250 #look at data and calculate the desired sampling rate
fc=15 #sampling "cutoff" for the lowpass filter
N_order=6 #stronger filter response with an increase in N, 'taps'
#frequency = 1 / T
#omega = 2*np.pi*frequency

weights = sp.signal.butter(N=N_order, Wn=fc, btype='lowpass', fs=fs_sampling_rate, output='sos')
print(weights)
low_pass_data = np.convolve(column2, weights[0,0], mode='same')

plt.plot(column2)
plt.xlim(0, 5000)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('EKG Data Low Pass')
plt.show()

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##

diff_data = np.diff(column2)

plt.plot(diff_data)
plt.xlim(0, 5000)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('EKG Data Differentiated')
plt.show()


"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##

squared_data = np.square(diff_data)

plt.plot(squared_data)
plt.xlim(0, 5000)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('EKG Data Squared')
plt.show()

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals

ones_array = np.ones(20)
print(ones_array)
maverage_data = np.convolve(squared_data, ones_array, mode='same')

plt.plot(maverage_data)
plt.xlim(0, 5000)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('EKG Data after Moving Filter')
plt.show()