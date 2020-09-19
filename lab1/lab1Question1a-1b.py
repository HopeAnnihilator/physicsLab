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
    0,0,0,0,0,0,-0.002,-0.009,-0.021,-0.036,-0.052,-0.068,-0.084,-0.099,-0.115,-0.131,-0.146,-0.161,-0.177,-0.193,-0.209,-0.225,-0.241,-0.255,-0.27,-0.285,-0.3,-0.316,-0.331,-0.346,-0.36,-0.374,-0.388,-0.404,-0.418,-0.432,-0.446,-0.46,-0.475,-0.488,-0.501,-0.515,-0.528,-0.542,-0.556,-0.57,-0.584,-0.597,-0.61,-0.624,-0.637,-0.649,-0.661,-0.674,-0.685,-0.679,-0.621,-0.484,-0.292,-0.122,-0.032,-0.011,-0.019,-0.03,-0.03,-0.016,0.002,0.008,-0.003,-0.011,-0.008,-0.001,1.11E-15,-0.002,-0.002,-4.04E-04,-1.11E-15,-4.04E-04,0,0,0,0,0,0,0,0,0,0,0,0,0,0
]
actualPositions = [
    0,0,0,0,0,0,0,0,0,-0.00072757,0.0021,0.0042,0.0073,0.011,0.0156,0.021,0.0272,0.0341,0.0417,0.0502,0.0594,0.0695,0.0804,0.092,0.1044,0.1176,0.1314,0.1461,0.1615,0.1776,0.1946,0.2123,0.2306,0.2497,0.2694,0.2901,0.3114,0.3332,0.3559,0.3793,0.4034,0.4282,0.4535,0.4796,0.5064,0.5338,0.5619,0.5908,0.6204,0.6505,0.6814,0.7129,0.745,0.7778,0.8111,0.8452,0.8799,0.9146,0.9454,0.9661,0.9735,0.9741,0.9741,0.9749,0.976,0.9779,0.9802,0.9799,0.9788,0.9786,0.9792,0.9804,0.9803,0.9798,0.9802,0.9805,0.9803,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804,0.9804
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
times = np.array(times)
accelerations = np.array(accelerations)

#calculate average acceleration
averageacc = (round(np.average(accelerations[20:50]), 7))

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
plt.plot(times[20:50], actualPositions[20:50], label = "positionsReal")
plt.plot(times[20:50], estimatedPositions[20:50], label = "positionsEst")
accLine = mpatches.Patch(color='blue', label='Acceleration')
velLine = mpatches.Patch(color='orange', label='Velocity')
realPos = mpatches.Patch(color='green', label='Real Positions')
estPos = mpatches.Patch(color='red', label='Estimated Positions')
plt.legend(handles=[accLine, velLine, realPos, estPos])
plt.show()
