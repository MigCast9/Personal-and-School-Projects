import numpy as np
from scipy.stats import norm
from scipy.stats import t
data = [-23, -16, -3, -9, -1, 13, -16, 15, 31, -22, -14, -25]

#------#------#------#------#------#------#------#------#------#------#
#QUESTION 1
print("---------------------------------------------------")
print("Question 1")
# dataWins = [i for i in data if i > 0]

c = 0.9
df = len(data) - 1

t_c = t.ppf(1 - (1 - c)/2, df)

stdDev = np.std(data)

stdError = stdDev / (len(data)) ** 0.5

dataMean = np.mean(data)

xMin = dataMean - t_c * stdDev / (len(data)) ** 0.5

xMax = dataMean + t_c * stdDev / (len(data)) ** 0.5

print(f"Interval: ({xMin}, {xMax})")
print(f"t-score: {t_c}")
print(f"Std Error: {stdError}")
print(f"Mean: {dataMean}")
print("Size:",len(data))

#------#------#------#------#------#------#------#------#------#------#
#QUESTION 2
print("---------------------------------------------------")
print("Question 2")
c = 0.95
df = len(data) - 1

t_c = t.ppf(1 - (1 - c)/2, df)

stdDev = np.std(data)

stdError = stdDev / (len(data)) ** 0.5

dataMean = np.mean(data)

xMin = dataMean - t_c * stdDev / (len(data)) ** 0.5

xMax = dataMean + t_c * stdDev / (len(data)) ** 0.5

print(f"Interval: ({xMin}, {xMax})")
print(f"t-score: {t_c}")
print(f"Std Error: {stdError}")
print(f"Mean: {dataMean}")
print("Size:",len(data))

#------#------#------#------#------#------#------#------#------#------#
#QUESTION 3
print("---------------------------------------------------")
print("Question 3")
c = 0.95
df = len(data) - 1

z_c = norm.ppf(1 - (1 - c)/2)

stdDev = 16.836

stdError = stdDev / (len(data)) ** 0.5

dataMean = np.mean(data)

xMin = dataMean - z_c * stdDev / (len(data)) ** 0.5

xMax = dataMean + z_c * stdDev / (len(data)) ** 0.5

print(f"Interval: ({xMin}, {xMax})")
print(f"z-score: {z_c}")
print(f"Std Error: {stdError}")
print(f"Mean: {dataMean}")
print("Size:",len(data))

#------#------#------#------#------#------#------#------#------#------#
#QUESTION 4
print("---------------------------------------------------")
print("Question 4")
df = len(data) - 1

t_c = t.ppf(1 - (1 - c)/2, df)

stdDev = np.std(data)

stdError = stdDev / (len(data)) ** 0.5

dataMean = np.mean(data)

tScore = (-dataMean * (len(data))**0.5) / stdDev

pScore = 2 * t.cdf(-abs(tScore), df)

confidenceLevel = 1 - pScore
print(f'This is the confidence level: {confidenceLevel}')