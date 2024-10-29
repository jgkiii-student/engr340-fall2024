import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

data = np.loadtxt(path, skiprows=2, delimiter=',')

# save each vector as own variable
column1 = data[0:,0]
column2 = data[0:,1]
column3 = data[0:,2]

# use matplot lib to generate a single

fig1 = plt.plot(column1)
plt.show()
fig2 = plt.plot(column2)
plt.show()
fig3 = plt.plot(column3)
plt.xlim(0, 1000)
plt.xlabel('Time')
plt.ylabel('Voltage?')
plt.title('EKG Data')
plt.show()
