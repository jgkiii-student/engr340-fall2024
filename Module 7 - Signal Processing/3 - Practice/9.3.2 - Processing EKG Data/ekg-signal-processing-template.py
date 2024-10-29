import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

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

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##
data = np.convolve(data, )
Second_Parameter = (2*15)/250
data = sp.butter(data,fs=250Hz, Wn=Second_Parameter)

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##


"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(signal)
plt.show()