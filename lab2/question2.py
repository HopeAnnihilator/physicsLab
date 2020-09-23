#!/usr/bin/env python

import pandas as pd
from pandas import DataFrame as df
import numpy as np
import matplotlib 
from matplotlib import pyplot as plt
import time
import math

#import spreadsheet data, pop first row, fill blank spaces with 0
spreadsheetData = pd.read_excel (r'lab2/Pendulum_500gr_run.xlsx')
spreadsheetData = spreadsheetData.iloc[15:-3]
spreadsheetData = spreadsheetData.fillna(0)

#create numpy arrays for each data column to KISS
timeData = np.array(df(spreadsheetData, columns= ['Time']))
positionData = np.array(df(spreadsheetData, columns= ['Position'])) #horizontal Position Data
velocityData = np.array(df(spreadsheetData, columns= ['Velocity']))
accelerationData = np.array(df(spreadsheetData, columns= ['Acceleration']))
forceData = np.array(df(spreadsheetData, columns= ['Force']))

#calculate time interval
timeInterval = timeData[2] - timeData[1]

#add other knowns
mass = 0.5 #kilograms
stringLength = 0.6 #meters
gravity = -9.81 #unsure if neg yet

# minHeight = min(positionData)
# maxHeight = max(positionData)
# diffHeight = maxHeight - minHeight 

#incorrect formula, looking for 10-15 degrees
#angleData = np.rad2deg(np.arccos((-mass * np.subtract(velocityData, forceData)) / (mass * gravity))) 

#calculate theoretical data
#theoreticalForceData = (mass / (stringLength * (stringLength ** 2 * positionData **2))) * ((stringLength ** 2 * velocityData ** 2 ) + gravity * (stringLength **2 * positionData ** 2) ** 3/2)
theoreticalForceData = ((mass * velocityData ** 2) / stringLength) + (mass * gravity * (1 - (positionData / stringLength) ** 2) ** 0.5)
theoreticalForceData = []
for i in range(0, len(timeData)):
    theoreticalForceData.append(((mass * ((velocityData[i] - velocityData[i -1]) / timeInterval) ** 2) / stringLength) + (mass * gravity * (1 - (positionData[i] / stringLength) ** 2) ** 0.5))

print(theoreticalForceData)
maxTheoreticalForce = max(theoreticalForceData)
maxForce = max(forceData)
print('Difference between maximum tension and theoritcal maximum is: ' + str(abs(maxTheoreticalForce) - abs(maxForce)))

#plt.plot(angleData, - timeData)
plt.plot(timeData, theoreticalForceData)
plt.plot(timeData, forceData)

plt.show()