#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:18:30 2021

@author: miguelcastilho
"""
################################################################################
# Author: Miguel Castilho
# Date: 02/27/2021
# This program will calculate the total
# number of organisms after a set of days
###############################################################################


#Take the user inputs
startOrg = float(input("Starting number, in million: "))
avgIncreasePercent = float(input("Average daily increase, in percent: "))    
days = float(input("Number of days to multiply: "))
                       
count = 1

avgIncrease = avgIncreasePercent / 100

currentOrg = startOrg

#While loop to print and modify the necessary values
print("Day   Approx. Pop")
while count <= days:
    print(f" {count:2.0f}" + f"       {currentOrg: 6.4f}")
    
    #Assign new values for count and fr the current number of organisms
    count += 1
    
    currentOrg = currentOrg * (1 + avgIncrease)
  
    
            
