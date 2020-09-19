#/usr/bin/env python


from matplotlib import pyplot as plt 
import math
import matplotlib.patches as mpatches

metalName = 'Gallium'
liquidName = 'Mercury'
liquidTemp = '100' #in celcius

densityOfSphere = 5904 #in kg/m^3, our metal is GALLIUM!?!?
radius = 0.1 #sphere has teeny radius
area = math.pi * radius ** 2 # cross sectional area in m^2
aerodynamicCoef = 0.12 #tf is this?
airAtSeaLevel = 1.225 #density of air at sea level in Kg/m^3
gravity = 9.81 #m/s^2, acceleration of gravity
velocityArray = [] #empty array for later
densityOfLiquid = 13351 #kg/m^3
drag = 0.5 * aerodynamicCoef * densityOfLiquid * area #all-inclusive coeffecient?????????????????????????????????????????
timeStep = 0.1 #interval of time
totalDuration = 50 #seconds

#calculate volume of sphere 
volume = (4/3) * math.pi * (radius ** 3) # in kg

#calculate mass of sphere 
mass = densityOfSphere / volume

#choose our liquid since none given
#mercury!!!!!!!!!!!!!
#source: https://www.engineeringtoolbox.com/mercury-d_1002.html
#temp 100 degrees Celcius


#use this info to calculate buoyancy
buoyancy = volume * densityOfLiquid * gravity


#create list of all intervals of time
timeIntervals = []
for i in range(0, int(totalDuration * (1 / timeStep) + 1)): #weird math stuff, dw about it
    timeIntervals.append(round(i * (timeStep / 1), 7)) #weird math stuff, dw about it

#add the proper data to begin velocity data
velocityArray.append(0)
velocityArray.append(0.1)

#empty accelerations array
accelerationArray = []

#make calculations
for i in range(2, len(timeIntervals)):
    acceleration = gravity - ((drag + buoyancy) / mass) * velocityArray[i -1] ** 2
    accelerationArray.append(acceleration)
    velocityArray.append(velocityArray[i -1] + acceleration * timeStep)

#create graph and display in popup
plt.title("Velocity Graph") 
plt.ylabel("Vertical Speed (m/s)")
plt.xlabel("Time (s)")
plt.plot(timeIntervals, velocityArray)
metal = mpatches.Patch(label= "Metal: " + metalName)
liquid = mpatches.Patch(label= "Liquid: " + liquidName)
temp = mpatches.Patch(label= "Liquid Temperature: " + liquidTemp + '$^\circ$C')
plt.legend(handles=[metal, liquid, temp])
plt.show()
