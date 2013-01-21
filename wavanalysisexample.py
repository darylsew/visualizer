#Example of how to extract data from a wav file using the modified library we wrote
import svt
import matplotlib
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random

centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
"""
print centroids[1]
print frequencies[1]
print volumes[1]

for i in range(0, int(len(frequencies[1])/20)):
    print frequencies[1][i]
"""
"""
numbers = []
for i in range(len(frequencies[1])):
    numbers.append(i)

#analysis codeeeeeeeee
for i in range(len(frequencies)):
    matplotlib.pyplot.scatter(numbers, frequencies[i])
    matplotlib.pyplot.show()
"""

fig = pylab.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = range(0, 2050)
sequence_containing_y_vals = range(0, 2050)
sequence_containing_z_vals = range(0, 2050)

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()
