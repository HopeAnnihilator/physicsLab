#/usr/bin/env python


from matplotlib import pyplot as plt 
import math

mass = 1.0 #in kg
radius = 0.1 #in meters
area = math.pi * radius ** 2 # cross sectional area in m^2
aerodynamicCoef = 0.12 #tf is this?
airAtSeaLevel = 1.225 #density of air at sea level in Kg/m^3
gravity = 9.81 #m/s^2, acceleration of gravity
velocityArray = [] #empty array for later
drag = 0.5 * aerodynamicCoef * airAtSeaLevel * area #all-inclusive coeffecient?????????????????????????????????????????
timeStep = 0.1 #interval of time
totalDuration = 50 #seconds

#create list of all intervals of time
timeIntervals = []
for i in range(0, int(totalDuration * (1 / timeStep) + 1)): #weird math stuff, dw about it
    timeIntervals.append(round(i * (timeStep / 1), 7)) #weird math stuff, dw about it

#add the proper data to begin velocity data
velocityArray.append(0)
velocityArray.append(0.1)

for i in range(2, len(timeIntervals)):
    acceleration = gravity - (drag / mass) * velocityArray[i -1] ** 2
    velocityArray.append(velocityArray[i -1] + acceleration * timeStep)

#create graph and display in popup
plt.title("Velocity Graph") 
plt.ylabel("Vertical Speed (m/s)")
plt.xlabel("Time (s)")
plt.plot(timeIntervals, velocityArray)
plt.show()
