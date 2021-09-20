#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:53:53 2021

@author: miguelcastilho
"""
################################################################################
# Author: Miguel Castilho
# Date: 02/26/2021
# This program will create a sum
# with the user inputs and an average
###############################################################################

Sum = 0
count = 0

#taking the input
number = float(input("Enter a non-negative number (negative to quit): "))

#The loop to calculate the sum based on inputs and the average with the proper outputs
while number >= 0:
    Sum = Sum + number
    count = count + 1
    number = float(input("Enter a non-negative number (negative to quit): "))
    
if count > 0:
    average = Sum / count
    print(f"Sum ={Sum: 0.2f}")
    print(f"Average ={average: 0.2f}")
        
else:
    print("No input.")
    



    


