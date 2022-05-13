import numpy as np
from scipy.stats import norm
from scipy.stats import t

with open('engagement_0.txt', 'r') as fid:
    ent0Raw = fid.readlines()
    
with open('engagement_1.txt', 'r') as fid1:
    ent1Raw = fid1.readlines()

#Changing strings to floats then doing calculations
#Sample 0
ent0Float = [float(i) for i in ent0Raw]

ent0Mean = np.mean(ent0Float)

stdDev0 = np.std(ent0Float, ddof = 1)

ent0Size = len(ent0Float)

stdError0 = stdDev0 / ent0Size**0.5

#Sample 1
ent1Float = [float(j) for j in ent1Raw]

ent1Mean = np.mean(ent1Float)

stdDev1 = np.std(ent1Float, ddof = 1)

ent1Size = len(ent1Float)

stdError1 = stdDev1 / (ent1Size**0.5) #(1278**0.5)  # ##

zScore1 = (ent1Mean - 0.75) / stdError1

pValue1 = 2*norm.cdf(-abs(zScore1))
#-----------#-----------#-----------#-----------#-----------#-----------#
#QUESTION 2 - PRINTING WHAT THE QUESTION WANTS BASED ON THE COMPUTED VARIABLES ABOVE
print("Question 2")
print(f"Size is {ent1Size}")
print(f"Average is {ent1Mean}")
print(f"Std error is {stdError1}")
print(f'This is the Z score {zScore1}')
print(f"This is the p-value {pValue1}")
print("---------------------------------------------------")

#-----------#-----------#-----------#-----------#-----------#-----------#
#QUESTION 3 - CHECKING THE LARGEST P-VALUE BEFORE 0.05
print("Question 3")
zScoreQuestion3 = norm.ppf(1 - (0.05)/2)

stdErrorQ3 = abs(ent1Mean - 0.75) / zScoreQuestion3

newSizeQ3 = (stdDev1 / stdErrorQ3) ** 2

print(f"This is the Z-Score for Question 3: {zScoreQuestion3}")
print(f'This is the Standard Error for question 3: {stdErrorQ3}')
print(f"The new sample size will be of {newSizeQ3}")
print("---------------------------------------------------")

#-----------#-----------#-----------#-----------#-----------#-----------#
#QUESTION 5 - COMPARING TWO POPULATIONS
print("Question 5")
print(f'This is Engagement 0 size: {ent0Size}')
print(f'This is Engagement 1 size: {ent1Size}')

print(f"This is the mean for engagement 0: {ent0Mean}")
print(f"This is the mean for engagement 1: {ent1Mean}")

print(f"This is the standard error 0: {stdError0}")
print(f"This is the standard error 1: {stdError1}")

stdErrorTotal = (((stdDev0 ** 2) / ent0Size) + ((stdDev1 ** 2) / ent1Size)) ** 0.5
zScoreTotal = (ent0Mean - ent1Mean) / stdErrorTotal
pValueTotal = 2*norm.cdf(-abs(zScoreTotal))

print(f"Standard Error Total: {stdErrorTotal}")
print(f'z-score: {zScoreTotal}')
print(f"P value: {pValueTotal}")




