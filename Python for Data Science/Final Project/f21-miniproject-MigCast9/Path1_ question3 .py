# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:14:28 2021

@author: pedro
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy
from sklearn.model_selection import train_test_split


def inputFunctionExcel(filename):

    files = pd.ExcelFile(filename)
    #Values for the Annual Averge Daily Traffic
    # Date = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Date'])
    Day = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Day'])
    highTemp = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['High Temp (°F)'])
    lowTemp = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Low Temp (°F)'])
    precipitation = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Precipitation'])
    brooklynBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Brooklyn Bridge'])
    manhattanBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Manhattan Bridge'])
    williamsburgBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Williamsburg Bridge'])
    queensboroBridge = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Queensboro Bridge'])
    total = np.array(pd.read_excel(files, 'NYC_Bicycle_Counts_2016_Correct', index_col = 0)['Total'])
    
    dictOutput = {}
    
    # dictOutput.update({'Date':Date})
    dictOutput.update({'Day':Day})
    dictOutput.update({'highTemp':highTemp})
    dictOutput.update({'lowTemp':lowTemp})
    dictOutput.update({'precipitation':precipitation})
    dictOutput.update({'brooklynBridge':brooklynBridge})
    dictOutput.update({'manhattanBridge':manhattanBridge})
    dictOutput.update({'williamsburgBridge':williamsburgBridge})
    dictOutput.update({'queensboroBridge':queensboroBridge})
    dictOutput.update({'total':total})  

    return dictOutput

bikeDict = inputFunctionExcel('NYC_Bicycle_Counts_2016_Corrected.xlsx')

    
precipitationWrong = bikeDict['precipitation']
manhattanBridge = bikeDict['manhattanBridge']
brooklynBridge = bikeDict['brooklynBridge']
williamsburgBridge = bikeDict['williamsburgBridge']
queensboroBridge = bikeDict['queensboroBridge']
totalTraffic = bikeDict['total']

manhattanAVG = np.average(manhattanBridge)
brooklynAVG = np.average(brooklynBridge)
williamsburgAVG = np.average(williamsburgBridge)
queensboroAVG = np.average(queensboroBridge)
totalAVG = np.average(totalTraffic)
totalAvgDivided = totalAVG / 4

precipitationcorrect = []
for i in precipitationWrong:
    if i != 'T':
        precipitationcorrect.append(float(i))
    else:
        precipitationcorrect.append(0.01)
        
        
traffic_precipitation = []
traffic_NOprecipitation = []
for iteration in range(len(precipitationcorrect)):
    if  precipitationcorrect[iteration] > 0 :
        traffic_precipitation.append(float(totalTraffic[iteration]))
    elif  precipitationcorrect[iteration] <= 0:
        traffic_NOprecipitation.append(float(totalTraffic[iteration]))

print(len(totalTraffic))
print(len(traffic_precipitation))
print(len(traffic_NOprecipitation))
#Training and testing split, with 25% of the data reserved as the test set
#traffic_precipitation = traffic_precipitation.to_numpy()
#traffic_NOprecipitation = traffic_NOprecipitation.to_numpy()
[traf_precipitation_train, traf_precipitation_test] = train_test_split(traffic_precipitation,test_size=0.25, random_state=101)  
[traf_NOprecipitation_train, traf_NOprecipitation_test] = train_test_split(traffic_NOprecipitation, test_size=0.25, random_state=101) 

#Traffic with precipitation 
mean_precipitation = np.mean(traf_precipitation_train)
standard_deviation_precipitation = np.std(traf_precipitation_train)

x_values_precipitation = np.arange(0, 35000, 1)
y_values_precipitation = scipy.stats.norm(mean_precipitation, standard_deviation_precipitation)

#Traffic without precipitation 
mean_NOprecipitation = np.mean(traf_NOprecipitation_train)
standard_deviation_NOprecipitation = np.std(traf_NOprecipitation_train)

x_values_NOprecipitation = np.arange(0, 35000, 1)
y_values_NOprecipitation = scipy.stats.norm(mean_NOprecipitation, standard_deviation_NOprecipitation)

#Plot the Gausian Distribution
plt.figure(1)
plt.plot(x_values_precipitation, y_values_precipitation.pdf(x_values_precipitation),label ="Precipitation Day")
plt.plot(x_values_NOprecipitation,y_values_NOprecipitation.pdf(x_values_NOprecipitation), label ="No Precipitation Day")
plt.xlabel('Number of Cyclists in a day')
plt.ylabel('Probability')
plt.legend()
plt.title("Gaussian Distributions")

print('Size of traffic precipitation test')
print(len(traf_precipitation_test))
print('Size of traffic with no precipitation test')
print(len(traf_NOprecipitation_test))

#Testing Data
correct_predic =[]
wrong_predict = []
for iteration, value in enumerate(traf_precipitation_test):
    #index = x_values_precipitation.index(value)
    if  y_values_precipitation.pdf(x_values_precipitation)[int(value)-1] > y_values_NOprecipitation.pdf(x_values_NOprecipitation)[int(value)-1]:
        correct_predic.append(value)
    else:
        wrong_predict.append(value)
precipitation_correct_len = len(correct_predic)
precipitation_accuracy = 100* len(correct_predic)/ ( len(wrong_predict) + len(correct_predic))
print("Accuracy of raining day tests is",precipitation_accuracy,'%' )
for iteration, value in enumerate(traf_NOprecipitation_test):
    #index = x_values_NOprecipitation.index(value)
    if  y_values_NOprecipitation.pdf(x_values_NOprecipitation)[int(value)-1] > y_values_precipitation.pdf(x_values_precipitation)[int(value)-1]:
        correct_predic.append(value)
    else:
        wrong_predict.append(value)
NOprecipitation_accuracy = 100* ( len(correct_predic) - precipitation_correct_len )/ len(traf_NOprecipitation_test)
print("Accuracy of no precipitation day tests is",NOprecipitation_accuracy,'%' )
print('Total accuracy is ', 100* len(correct_predic)/ ( len(wrong_predict) + len(correct_predic)),'%' )     
