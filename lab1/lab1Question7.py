#!/usr/bin/env python

#import required scripts
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
import time
import matplotlib.patches as mpatches
import math

#define starting time 
startingTime = 0
timeInterval = 0.05
mass = 0.66 #kg

velocity = [
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4.04E-04,8.08E-04,8.08E-04,4.04E-04,0,0,0,4.04E-04,8.08E-04,0.001,0.002,0.002,0.003,0.004,0.006,0.008,0.011,0.014,0.018,0.023,0.028,0.035,0.042,0.049,0.057,0.067,0.076,0.085,0.095,0.104,0.114,0.124,0.133,0.143,0.154,0.165,0.174,0.184,0.194,0.203,0.213,0.222,0.23,0.239,0.249,0.259,0.269,0.277,0.285,0.293,0.302,0.31,0.318,0.323,0.324,0.321,0.315,0.308,0.301,0.292,0.281,0.268,0.255,0.241,0.228,0.214,0.2,0.185,0.169,0.153,0.136,0.119,0.102,0.085,0.068,0.051,0.034,0.017,4.04E-04,-0.015,-0.029,-0.044,-0.059,-0.074,-0.09,-0.105,-0.12,-0.136,-0.151,-0.166,-0.18,-0.194,-0.207,-0.222,-0.236,-0.251,-0.266,-0.281,-0.295,-0.308,-0.322,-0.336,-0.35,-0.365,-0.378,-0.391,-0.405,-0.418,-0.432,-0.445,-0.458,-0.471,-0.485,-0.498,-0.511,-0.483,-0.322,-0.101,0.046,0.024
]

#empty time array to be filled out as looped
times = []
accelerations = []
thrust = []

for i in range(0, len(velocity)):
    previousVelocity = velocity[i - 1]
    currentVelocity = velocity[i]
    diffVelocity = currentVelocity - previousVelocity
    acceleration = diffVelocity / timeInterval
    accelerations.append(acceleration)
    thrust.append(mass * acceleration)
    #update current time and round to prevent float point errors and keep data clean
    startingTime = round(startingTime + timeInterval,2)
    #add to array of times
    times.append(startingTime)

thrust.pop(0)
accelerations.pop(0)
times.pop(0)
velocity.pop(0)
thrust = np.array(thrust)
times = np.array(times)
accelerations = np.array(accelerations)
maxthrust = round(np.amax(thrust), 7)
#create graph and display in popup
plt.title("Thrust Graph") 
plt.ylabel("Max Thrust = " + str(maxthrust) + "N")
plt.xlabel("Time (s)")
plt.plot(times[90:-10], accelerations[90:-10], label = "Acceleration")
plt.plot(times[90:-10], velocity[90:-10], label = "Velocity")
plt.plot(times[90:-10], thrust[90:-10], label = "Velocity")
accLine = mpatches.Patch(color='blue', label='Acceleration')
velLine = mpatches.Patch(color='orange', label='Velocity')
thrustLine = mpatches.Patch(color='green', label='Thrust')
plt.legend(handles=[accLine, velLine, thrustLine])
plt.show()
