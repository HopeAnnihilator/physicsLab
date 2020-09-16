#!/usr/bin/env python

#import required scripts
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
import time
import matplotlib.patches as mpatches
import math

#define starting time 
startingTime = 0.05
timeInterval = 0.05

#array of velocities
velocity = [
0,-0.232,-0.247,-0.262,-0.278,-0.293,-0.31,-0.326,-0.342,-0.357,-0.371,-0.387,-0.403,-0.418,-0.433,-0.448,-0.463,-0.478,-0.493,-0.508,-0.522,-0.537,-0.552,-0.567,-0.582,-0.596,-0.61,-0.625,-0.638,-0.652,-0.666,-0.679,-0.693,-0.703,-0.686,-0.621,-0.446,-0.197,0.015,0.11,0.103,0.085,0.067,0.05,0.035,0.022,0.008,-0.005,-0.017,-0.026,-0.032,-0.036,-0.041,-0.047,-0.055,-0.065,-0.078,-0.091,-0.103,-0.089,-0.044,0.003,0.021,0.009,-0.007,-0.019,-0.017,-0.004,0.005,4.04E-04,-0.006,-0.004,0,4.04E-04,-0.002,-0.001,-0.001,0
]
actualPositions = [
    0.0441,0.0553,0.0673,0.08,0.0935,0.1078,0.1228,0.1387,0.1555,0.1729,0.1911,0.21,0.2298,0.2503,0.2716,0.2936,0.3164,0.3399,0.3642,0.3893,0.415,0.4414,0.4687,0.4966,0.5253,0.5548,0.585,0.6158,0.6474,0.6797,0.7125,0.7462,0.7806,0.8155,0.8513,0.8863,0.9155,0.9376,0.9337,0.9272,0.9216,0.9169,0.9131,0.9102,0.9081,0.9068,0.906,0.9058,0.9066,0.9076,0.9092,0.9109,0.9127,0.9149,0.9175,0.9203,0.9239,0.928,0.933,0.9384,0.9445,0.9432,0.9415,0.9406,0.9406,0.9414,0.9429,0.9441,0.9431,0.9426,0.9431,0.944,0.9435,0.9433,0.9438,0.9437,0.9437,0.9438
]


#empty time array to be filled out as looped
times = []
accelerations = []

for i in range(0, len(velocity)):
    previousVelocity = velocity[i - 1]
    currentVelocity = velocity[i]
    diffVelocity = currentVelocity - previousVelocity
    accelerations.append(diffVelocity / timeInterval)
    #update current time and round to prevent float point errors and keep data clean
    startingTime = round(startingTime + timeInterval,2)
    #add to array of times
    times.append(startingTime)

velocity.pop(0)
times.pop(0)
accelerations.pop(0)
actualPositions.pop(0)
velocity.pop(0)
times.pop(0)
accelerations.pop(0)
actualPositions.pop(0)
times = np.array(times)
accelerations = np.array(accelerations)

#calculate average acceleration
averageacc = (round(np.average(accelerations[:34]), 7))

estimatedPositions = []
for i in range(0,len(velocity)):
    currentVelocity = 0 - velocity[i]
    currentTime = times[i]
    estimatedPositions.append(currentVelocity * currentTime + 0.5 * averageacc * currentTime ** 2)



#create graph and display in popup
plt.title("Acceleration Graph") 
plt.ylabel("Average Acceleration = " + str(averageacc) + " m/s\N{SUPERSCRIPT TWO}")
plt.xlabel("Time")
plt.plot(times, accelerations, label = "Acceleration")
plt.plot(times, velocity, label = "Velocity")
plt.plot(times[:34], actualPositions[:34], label = "positionsReal")
plt.plot(times[:34], estimatedPositions[:34], label = "positionsEst")
accLine = mpatches.Patch(color='blue', label='Acceleration')
velLine = mpatches.Patch(color='orange', label='Velocity')
realPos = mpatches.Patch(color='green', label='Real Positions')
estPos = mpatches.Patch(color='red', label='Estimated Positions')
plt.legend(handles=[accLine, velLine, realPos, estPos])
plt.show()
