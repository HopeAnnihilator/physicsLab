#!/usr/bin/env python

import pandas as pd
from pandas import DataFrame as df
import numpy as np
import matplotlib 
from matplotlib import pyplot as plt

#import spreadsheet data, pop first row, fill blank spaces with 0
spreadsheetData = pd.read_excel (r'lab2/Pendulum_500gr_run.xlsx')
spreadsheetData = spreadsheetData.iloc[50:-50]
spreadsheetData = spreadsheetData.fillna(0)

#create numpy arrays for each data column to KISS
timeData = np.array(df(spreadsheetData, columns= ['Time']))
positionData = np.array(df(spreadsheetData, columns= ['Position']))
velocityData = np.array(df(spreadsheetData, columns= ['Velocity']))
accelerationData = np.array(df(spreadsheetData, columns= ['Acceleration']))
forceData = np.array(df(spreadsheetData, columns= ['Force']))

#calculate time interval
timeInterval = timeData[2] - timeData[1]

#add other knowns
mass = 0.5 #kilograms
stringLength = 0.6 #meters
gravity = 9.81

minHeight = min(positionData)
maxHeight = max(positionData)
diffHeight = maxHeight - minHeight 

plt.plot(timeData, forceData)
plt.show()