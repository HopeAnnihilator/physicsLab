#!/usr/bin/env python

#import required scripts
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
import time
import matplotlib.patches as mpatches
import math
import json
import csv

mass = 1.42 #kg
innerRing = 5.5 #cm
outerRing = 6.5 #cm

lines = []
with open('data.csv') as f:
    data = csv.reader(f)
    for line in f:
        line = line.strip('\n')
        line = line.split(',')
        if line[-1]:
            lines.append(line[3:])
lines = lines[2:]

linearAcceleration = []
times = []
for i in lines:
    times.append(i[1])
    linearAcceleration.append((6.5 / 1000) * float(i[-1]))
averageacc = (round(np.average(linearAcceleration), 7))
theoaverageacc = round((float(linearAcceleration[-1]) - float(linearAcceleration[0]) / (float(times[-1]) - float(times[0]))), 7)

timeLabels = []
prevSpot = 0
for i in times:
    if prevSpot != math.floor(float(i)) or times[-1] == i:
        prevSpot = math.floor(float(i))
        timeLabels.append(times.index(i))
timeLabels.pop(1)
plt.title("Acceleration Graph") 
plt.ylabel("Actual Average Linear Acceleration = " + str(averageacc) +
 " m/s\N{SUPERSCRIPT TWO}\nTheoretical Average Acceleration = " + str(theoaverageacc) + " m/s\N{SUPERSCRIPT TWO}")
plt.xlabel("Time (s)")
plt.plot(times, linearAcceleration, label = "Acceleration")
plt.xticks(timeLabels)
plt.show()