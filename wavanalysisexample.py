#Example of how to extract data from a wav file using the modified svt library.
#Also useful for graphing or playing around with data.
import svt
import matplotlib
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy

#The line needed to get data from the first channel.
centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
"""
Frequencies graphs (x axis is frequency (lower==lower frequency), y axis is intensity, frame x == time)
Graph generating code (for clarity)
http://speedcap.net/sharing/screen.php?id=files/01/be/01bec08cb0a6d05f104275d7e1b4a851.png
 frame 0
http://speedcap.net/sharing/screen.php?id=files/09/39/0939260e5185fb361a324deb425a7b62.png
frame 1
http://speedcap.net/sharing/screen.php?id=files/32/d9/32d96c138542e44a16131e0c8f1a5da1.png
frame 2
http://speedcap.net/sharing/screen.php?id=files/44/af/44afd3166c1bf769f0265b182daefa89.png

Centroids graph (x axis is time, y axis is brightness (low to high))
http://speedcap.net/sharing/screen.php?id=files/72/b7/72b7622809aeeb59f5b9227d2809c29f.png

Volumes graph (x axis is time, y axis is intensity (low to high))
http://speedcap.net/sharing/screen.php?id=files/ac/90/ac90d6b18c13225c781c77f81d7c220e.png

Simple stats:
Volumes
Max: 1.33679199219
Avg: 0.815959368812
Min: 0.000152587890625
Centroids
Max: 0.847659125302
Avg: 0.673952599689
Min: 0.144571311477
Frequencies stats are kind of complicated so dwai.
"""


"""
#Samples some of the data.
print centroids[1]
print frequencies[1]
print volumes[1]

for i in range(0, int(len(frequencies[1])/20)):
    print frequencies[1][i]
"""
#Graphs frequencies, centroids, and volumes on 2d plots; frequencies should really be 3d but I can't figure out how to 3d graph them so a number of 2d graphs should suffice for understanding the data.
#numbers = []
#for i in range(len(frequencies[1])):
#    numbers.append(i)

#analysis codeeeeeeeee
#for i in range(len(frequencies)):
#    matplotlib.pyplot.scatter(numbers, frequencies[i])
#    matplotlib.pyplot.show()

#matplotlib.pyplot.scatter(range(len(centroids)), centroids)
#matplotlib.pyplot.show()
#matplotlib.pyplot.scatter(range(len(volumes)), volumes)
#matplotlib.pyplot.show()

"""
#Failed 3d graph code
fig = pylab.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = range(0, 2050
sequence_containing_y_vals = range(0, 2050)
sequence_containing_z_vals = range(0, 2050)

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()
"""
"""
#File IO. Resulting files are way too large (well, the frequencies file, which is ~136MB). Will truncate frequencies/compress data some other way.
f = open("volumes.txt", 'w')
for item in volumes:
    print>>f, item
f.close()
f = open("centroids.txt", 'w')
for item in centroids:
    print>>f, item
f.close()
f = open("frequencies.txt", 'w')
for i in range(len(frequencies)):
    print>>f, "Frequencies at frame"+str(i)
    for item in frequencies[i]:
        print>>f, item
f.close()
"""
"""
#Simple statistics
print "Volumes"
print "Max: " + str(max(volumes))
print "Avg: " + str(numpy.mean(volumes))
print "Min: " + str(min(volumes))
print "Centroids"
print "Max: " + str(max(centroids))
print "Avg: " + str(numpy.mean(centroids))
print "Min: " + str(min(centroids))
"""
