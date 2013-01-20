#Example of how to extract data from a wav file using the modified library we wrote
import svt
import matplotlib
import pylab

centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
"""
print centroids[1]
print frequencies[1]
print volumes[1]

for i in range(0, int(len(frequencies[1])/20)):
    print frequencies[1][i]
"""

numbers = []
for i in range(len(frequencies[1])):
    numbers.append(i)

#analysis codeeeeeeeee
for i in range(len(frequencies)):
    matplotlib.pyplot.scatter(numbers, frequencies[i])
    matplotlib.pyplot.show()
